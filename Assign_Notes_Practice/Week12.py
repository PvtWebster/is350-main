'''
Week 12 - No book chapter assigned
'''

lineBreak = "----------"

print(f"{lineBreak} Pygame Snake {lineBreak}")
import random
import curses

s = curses.initscr() #initialize screen
curses.curs_set(0) #hide the cursor
sh, sw = s.getmaxyx() #get width and height
w = curses.newwin(sh, sw, 0, 0) #use width/height to create window for the game
w.keypad(1) #set game to accept input from keyboard
w.timeout(100) #refresh the game ever 100 ms

#create snake initial position
snk_x = sw/4
snk_y = sh/2
#create snake body parts
snake = [[snk_y, snk_x],#head
[snk_y, snk_x-1],#middle
[snk_y, snk_x-2],#tail
]
print(curses.ACS_PI)
#add food
food = [sh/2, sw/2]#food location, center screen
w.addch(food[0], food[1], curses.ACS_PI)#add food, type PI

#give snake initial direction
key = curses.KEY_RIGHT

print(curses.ACS_PI)

#infinite loop
while True:
	next_key = w.getch() #get next key
	key = key if next_key == -1 else next_key #get nothing or the next key
	 #check if player lost - snake hits window edge or itself
	if snake[0][0] in [0, sh] or snake[0,1] in [0,sw] or snake[0] in snake[1:]:
		curses.endwin()
		quit()
	
	#determine new head of snake
	new_head = [snake[0][0], snake[0][1]]#take old head of snake
	
	#determine the key input
	if key == curses.KEY_DOWN:
		new_head[0] += 1
	if key == curses.KEY_UP:
		new_head[0] -= 1
	if key == curses.KEY_LEFT:
		new_head[1] -= 1
	if key == curses.KEY_RIGHT:
		new_head[1] += 1

	snake.insert(0, new_head)#insert new nead

	#snake gets food; create new food location
	if snake[0] == food:
		food = None
		while food is None:
			new_food = [random.randit(1, sh-1), random.randit(1, sw-1)]
			food= new_food if new_food not in snake else None
		w.addch(food[0], food[1], curses.ACS_PI)
	else:
		#pop off tail
		tail = snake.pop() 
		w.addch(tail[1], tail[1], ' ')

	w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

print(f"{lineBreak} Django vs Flask {lineBreak}")
'''
-both are frameworks to help with web development with python
-flask is lightweight; may require additional code writing to implement things
-django more libraries included, but more advanced
'''