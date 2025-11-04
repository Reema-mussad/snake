import random
import curses

screen = curses.initscr()
#for hiding mouse
curses.curs_set(0)

#set the window hight and width
height, width= screen.getmaxyx()

#creat a window from curses 
window = curses.newwin(height, width,0 ,0)

#read the botton
window.keypad(1)

#update
window.timeout(100)

# set coordinates for head
head_x = width  // 2
head_y = height // 4

snake = [[head_y,head_x],[head_y,head_x-1],[head_y,head_x-2]]
#where the food will show
food = [height // 2, width // 2]
window.addch(food[0],food[1],curses.ACS_PI)

# where to go by defult
key = curses.KEY_RIGHT


#snake movement
while True: 
    key_next = window.getch()
    #-1 in .getch() means nothing pressed
    
    key = key if key_next == -1 else key_next
#snake head hit the height Y or width X or head hit the body
    if snake[0][0] in [0,height] or snake[0][1] in [0,width] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0],snake[0][1]]

    if key == curses.KEY_DOWN :
        new_head[0] += 1
    if key == curses.KEY_UP :
        new_head[0] -= 1
    if key == curses.KEY_RIGHT :
        new_head[1] += 1
    if key == curses.KEY_LEFT :
        new_head[1] -= 1

    snake.insert(0,new_head)

    if snake[0] == food :
        food = None
        while food == None:
            new_food = [random.randint(1,height-1),random.randint(1,width-1)]
            food = new_food if new_food not in snake else None
        window.addch(food[0],food[1],curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0],tail[1], ' ')

    window.addch(snake[0][0],snake[0][1],curses.ACS_CKBOARD)

    window.refresh()