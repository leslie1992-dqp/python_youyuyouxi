import random
from misc import *

class Block():
    def __init__(self, coordinate, block_size, border_size, **kwargs):
        self.coordinate = coordinate
        self.block_size = block_size
        self.border_size = border_size
        self.is_visited = False
        # 上下左右有墙
        self.has_walls = [True, True, True, True]
        self.color = (0, 0, 0)    #迷宫线条的颜色

    '''画到屏幕上'''
    '''依次判别上下左右是否有墙，确定x1,x2,y1,y2的坐标'''
    def draw(self, screen):
        directions = ['top', 'bottom', 'left', 'right']
        '''这样可以分别检测0，1，2，3是否有墙，上下左右确定x1,x2,y1,y2的坐标'''
        for idx, direction in enumerate(directions):   #enumerate函数，将内容加上索引显示出来
            if self.has_walls[idx]:
                if direction == 'top':
                    x1 = self.coordinate[0] * self.block_size + self.border_size[0]
                    y1 = self.coordinate[1] * self.block_size + self.border_size[1]
                    x2 = (self.coordinate[0] + 1) * self.block_size + self.border_size[0]
                    y2 = self.coordinate[1] * self.block_size + self.border_size[1]
                    pygame.draw.line(screen, self.color, (x1, y1), (x2, y2))
                elif direction == 'bottom':
                    x1 = self.coordinate[0] * self.block_size + self.border_size[0]
                    y1 = (self.coordinate[1] + 1) * self.block_size + self.border_size[1]
                    x2 = (self.coordinate[0] + 1) * self.block_size + self.border_size[0]
                    y2 = (self.coordinate[1] + 1) * self.block_size + self.border_size[1]
                    pygame.draw.line(screen, self.color, (x1, y1), (x2, y2))
                elif direction == 'left':
                    x1 = self.coordinate[0] * self.block_size + self.border_size[0]
                    y1 = self.coordinate[1] * self.block_size + self.border_size[1]
                    x2 = self.coordinate[0] * self.block_size + self.border_size[0]
                    y2 = (self.coordinate[1] + 1) * self.block_size + self.border_size[1]
                    pygame.draw.line(screen, self.color, (x1, y1), (x2, y2))
                elif direction == 'right':
                    x1 = (self.coordinate[0] + 1) * self.block_size + self.border_size[0]
                    y1 = self.coordinate[1] * self.block_size + self.border_size[1]
                    x2 = (self.coordinate[0] + 1) * self.block_size + self.border_size[0]
                    y2 = (self.coordinate[1] + 1) * self.block_size + self.border_size[1]
                    pygame.draw.line(screen, self.color, (x1, y1), (x2, y2))
        return True


'''随机生成迷宫类'''
'''主要思想是，首先创建一个所有方块的四周都是墙的网格，在从起点依次访问每一个方块，
   访问的形式相当于在走迷宫，为迷宫开辟路径，以一个方块为中心，有上下左右四个方向，
   若为上，则将当前的方块的上和上面方块的下设置为没有墙...下左右同理，
   由于每次方向都是随机的，所以迷宫的产生也是随机的
   由于每个方块能走到，所以，边界的任何一个位置都可以设置为终点
   
   '''

class RandomMaze():
    def __init__(self, maze_size, block_size, border_size, **kwargs):
        self.block_size = block_size
        self.border_size = border_size
        self.maze_size = maze_size
        self.blocks_list = RandomMaze.createMaze(maze_size, block_size, border_size)
        self.font = pygame.font.SysFont('Consolas', 15)
        self.step_num = 0
        self.flag_step = 1


    '''创建迷宫'''

    @staticmethod
    def createMaze(maze_size, block_size, border_size):
        '''随机选择一个方向的方块作为下一个要检测的'''
        def nextBlock(block_now, blocks_list):
            directions = ['top', 'bottom', 'left', 'right']
            blocks_around = dict(zip(directions, [None] * 4))
            block_next = None
            count = 0
            # 查看上边block
            '''首先查看是否出了边界，再看是否已经访问，若没有则加入下一个的队列中'''
            if block_now.coordinate[1] - 1 >= 0:
                '''获取上面的的方块，若没有被访问过则，加入top的行列中'''
                block_now_top = blocks_list[block_now.coordinate[1] - 1][block_now.coordinate[0]]
                if not block_now_top.is_visited:
                    blocks_around['top'] = block_now_top
                    count += 1
            # 查看下边block
            if block_now.coordinate[1] + 1 < maze_size[0]:
                block_now_bottom = blocks_list[block_now.coordinate[1] + 1][block_now.coordinate[0]]
                if not block_now_bottom.is_visited:
                    blocks_around['bottom'] = block_now_bottom
                    count += 1
            # 查看左边block
            if block_now.coordinate[0] - 1 >= 0:
                block_now_left = blocks_list[block_now.coordinate[1]][block_now.coordinate[0] - 1]
                if not block_now_left.is_visited:
                    blocks_around['left'] = block_now_left
                    count += 1
            # 查看右边block
            if block_now.coordinate[0] + 1 < maze_size[1]:
                block_now_right = blocks_list[block_now.coordinate[1]][block_now.coordinate[0] + 1]
                if not block_now_right.is_visited:
                    blocks_around['right'] = block_now_right
                    count += 1
            '''若count>0,则说明相邻的四个方向有没有被访问过的方块'''
            if count > 0:
                while True:
                    direction = random.choice(directions)
                    '''获取方向，得到下一个方块的位置'''
                    if blocks_around.get(direction):
                        block_next = blocks_around.get(direction)
                        '''获取方向，得到下一个方块的位置'''
                        '''保证相邻的方块的墙是同一个'''
                        if direction == 'top':
                            block_next.has_walls[1] = False
                            block_now.has_walls[0] = False
                        elif direction == 'bottom':
                            block_next.has_walls[0] = False
                            block_now.has_walls[1] = False
                        elif direction == 'left':
                            block_next.has_walls[3] = False
                            block_now.has_walls[2] = False
                        elif direction == 'right':
                            block_next.has_walls[2] = False
                            block_now.has_walls[3] = False
                        break
            return block_next
        #block_list的每一个元素都是一个Block对象
        blocks_list = [[Block([col, row], block_size, border_size) for col in range(maze_size[1])] for row in
                       range(maze_size[0])]
        block_now = blocks_list[0][0]
        records = []
        step_num = 0
        flag_step = 1
        '''从开始位置检测每一个方块，直到所有的方块都遍历过了，就退出循环'''
        '''若这个方块没有被访问，则将其标为访问过的，加入队列中。对下一个进行访问，若访问过的，则直接pop（）掉'''
        '''直到records在、的长度为零，才是访问过所有方块的'''
        while True:
            if block_now:
                if not block_now.is_visited:
                    block_now.is_visited = True
                    records.append(block_now)
                block_now = nextBlock(block_now, blocks_list)

            else:
                block_now = records.pop()
                if len(records) == 0:
                    break
        return blocks_list



    '''画到屏幕上'''

    def draw(self, screen):
        for row in range(self.maze_size[0]):
            for col in range(self.maze_size[1]):
                self.blocks_list[row][col].draw(screen)
        ''' 起点和终点标志'''
        showText(screen, self.font, 'S', (255, 0, 0), (self.border_size[0] - 10, self.border_size[1]))
        showText(screen, self.font, 'D', (255, 0, 0), (self.border_size[0] + (self.maze_size[1] - 1) * self.block_size,
                                                       self.border_size[1] + self.maze_size[0] * self.block_size + 5))
