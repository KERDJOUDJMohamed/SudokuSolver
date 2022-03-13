import pygame
 #pre initialized board with empty spacese
def default():
    temp = [ [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],]
    return temp
#default board 
default_board = [   [5,3,0,0,7,0,0,0,0],
                    [6,0,0,1,9,5,0,0,0],
                    [0,9,8,0,0,0,0,6,0],
                    [8,0,0,0,6,0,0,0,3],
                    [4,0,0,8,0,3,0,0,1],
                    [7,0,0,0,2,0,0,0,6],
                    [0,6,0,0,0,0,2,8,0],
                    [0,0,0,4,1,9,0,0,5],
                    [0,0,0,0,8,0,0,7,9]]
#update the entier screen
def refresh():
    pygame.display.flip()
#General Infomation 
class Information :

    screen_resolution = (511,600)
    sudoku_board = pygame.image.load("sudoku blank grid.png")
    initial_position = (0,0)
    white_color = (255,255,255)
    info_background = (0,0,511,600)
    launched = True
#displace number at given position on surface
def display_number_at(surface,number,position):
    
    if number == 0 :
        return None
    
    origin = (25,18)#x y 
    pos_x = origin[0] + 54*position[0]
    pos_y = origin[1] + 50*position[1]

    surface.blit(pygame.image.load("numbers/"+str(number)+".PNG"),(pos_x,pos_y)) 
#Class (init:board,surface)
class Sudoku_solver:
    def __init__ (self,board,surface):
        self.board = board
        self.surface = surface

    def display_board(self):
        for i in range(0,9):
            for j in range(len(self.board[0])):
                self.On_board(self.board[i][j],(i,j))
            
    def empty_space(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0 :
                    return (i,j) 
        return None

    def valid (self,value,position):
    
        #Check Row
        for i in range(len(self.board[0])):
            if self.board[position[0]][i] == value and i != position[1]:
                return False 

        #Check Column
        for j in range(len(self.board[0])):
            if self.board[j][position[1]] == value and j != position[0]:
                return False 

        #Check Box
        x=(position[0]//3)*3
        y=(position[1]//3)*3
        
        for i in range(x,x+3):
            for j in range(y,y+3):
                
                if self.board[i][j] == value:
                    return False
        
        return True 

    def On_board(self,number,position):
        display_number_at(self.surface,number,position)

    def solve(self):
        x = self.empty_space()
        if x == None  :
            return True 
        else :
            for i in range(1,10):
                if self.valid(i,x) :
                    self.board[x[0]][x[1]]=i
                    self.On_board(i,(x[0],x[1]))
                    pygame.time.delay(0) #time delay
                    refresh()
                    if self.solve() :
                        return True
                    self.board[x[0]][x[1]]=0
            return False
#key pressed
def key_pressed(key,pos_x,pos_y,brd):
    
    if pos_x == 9:
        pos_x=0
        pos_y=pos_y+1

    display_number_at(window_surface,key,(pos_x,pos_y))
    print("({},{})<-{}".format(pos_x,pos_y,key))
    brd[pos_x][pos_y]=key
    pos_x=pos_x+1
    return pos_x,pos_y

#Display
pygame.init()
pygame.display.set_caption("Sudoku Solver")#set Name
window_surface = pygame.display.set_mode(Information.screen_resolution)#set resolution
pygame.draw.rect(window_surface,Information.white_color,Information.info_background)#white backgrondL
window_surface.blit(Information.sudoku_board,Information.initial_position)#set board

#Text
jump = 20
arial_font = pygame.font.SysFont("arial",18,bold=True)
text = arial_font.render("  ***You cant use the programme without creating a new instance***",True,(0,0,0))
window_surface.blit(text,(20,480))
text = arial_font.render("  - Press <n> to creat new suduku ",True,(0,0,0))
window_surface.blit(text,(20,480+jump))
text = arial_font.render("  - Press <012...9> corresponding for the current case , 0 for a blank ",True,(0,0,0))
window_surface.blit(text,(20,480+2*jump))
text = arial_font.render("  - Press <space> to start calculationg ",True,(0,0,0))
window_surface.blit(text,(20,480+3*jump))
text = arial_font.render("  - Press <d> to use default suduku ",True,(0,0,0))
window_surface.blit(text,(20,480+4*jump))


refresh()

#Events
new_instance = False
default_instance = False
while Information.launched:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            Information.launched = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                print("Creating new instance ...")
                b= default()
                pos_x =0
                pos_y =0
                window_surface.blit(Information.sudoku_board,Information.initial_position)#clear the board
                s = Sudoku_solver(b,window_surface)  
                new_instance = True #Creation New instance S
            if event.key == pygame.K_1 and new_instance : #1
                (pos_x,pos_y)=key_pressed(1,pos_x,pos_y,brd=b)
            if event.key == pygame.K_2 and new_instance : #2
               (pos_x,pos_y)= key_pressed(2,pos_x,pos_y,brd=b)
            if event.key == pygame.K_3 and new_instance : #3
               (pos_x,pos_y)= key_pressed(3,pos_x,pos_y,brd=b)
            if event.key == pygame.K_4 and new_instance : #4
               (pos_x,pos_y)= key_pressed(4,pos_x,pos_y,brd=b)
            if event.key == pygame.K_5 and new_instance : #5
               (pos_x,pos_y)= key_pressed(5,pos_x,pos_y,brd=b)
            if event.key == pygame.K_6 and new_instance : #6
               (pos_x,pos_y)= key_pressed(6,pos_x,pos_y,brd=b)
            if event.key == pygame.K_7 and new_instance : #7
               (pos_x,pos_y)= key_pressed(7,pos_x,pos_y,brd=b)
            if event.key == pygame.K_8 and new_instance : #8
               (pos_x,pos_y)= key_pressed(8,pos_x,pos_y,brd=b)
            if event.key == pygame.K_9 and new_instance : #9
               (pos_x,pos_y)= key_pressed(9,pos_x,pos_y,brd=b)
            if event.key == pygame.K_0 and new_instance : #0
               (pos_x,pos_y)= key_pressed(0,pos_x,pos_y,brd=b)
            if event.key == pygame.K_SPACE : #valid
                if  new_instance:
                    if default_instance :
                        s1.solve()
                        default_instance = False
                    else:
                        s.solve()
                        new_instance = False
                else :
                    print("You havent created an instance yet , Creat one by pressing n ...")
            if event.key == pygame.K_ESCAPE:
                Information.launched = False #Quit
            if event.key == pygame.K_d : #default
                if new_instance:
                    print("default board loaded ...") 
                    window_surface.blit(Information.sudoku_board,Information.initial_position) #clear the board 
                    s1 = Sudoku_solver(default_board,window_surface) #creat new instance S1
                    s1.display_board() #display board before traitement
                    default_instance = True
                else :
                    print("You havent created an instance yet , Creat one by pressing n ...")                      
        refresh()