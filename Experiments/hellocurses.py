import curses

print("Preparing to init screen")
screen = curses.initscr()
print("init complete")

screen.addstr(0,0, "this is at (0,0")
screen.addstr(3,1,"test text 3,1")
screen.addstr(4,4,"x")
screen.addstr(5,5,"y")
screen.refresh()
curses.napms(3000)
curses.endwin()
print("window end")