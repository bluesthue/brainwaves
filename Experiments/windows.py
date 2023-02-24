import curses
import math
import sys

def main(argv):
    screen=curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(True)
    if curses.has_colors():
        curses.start_color()
    screen.keypad(True)
    exceps = ""
    winh=20
    winw=60
    try:
        topMostY=math.floor((curses.LINES - winh)/2) #Yposition of the window box 
        leftMostX=math.floor((curses.COLS - winw)/2) #Xposition of the window box
        screen.addstr(curses.LINES-1,0,"Press Q to quit")
        screen.refresh()
        curses.init_pair(1,curses.COLOR_RED, curses.COLOR_BLACK)

        index=0
        running=True
        while True == running:
            if 0 != index:
                ch=screen.getch()
                if ch== ord('Q') or ch == ord('q'):
                    running=False
            #mainWindow = curses.newwin(winh,winw,topMostY,leftMostX)
            mainWindow = curses.newwin(winh,winw,topMostY,leftMostX)
            strtitle=""
            with open("splashtitle.txt",'r') as titlefile:
                strtitle=titlefile.read()
            mainWindow.bkgd(' ',curses.color_pair(1))
            if 0 == index % 2:
                mainWindow.box()
            else:
                mainWindow.border(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
            mainWindow.addstr(1,1,"this is text in window")
            mainWindow.addstr(1,1,strtitle)
            mainWindow.refresh()

            screen.addstr(0,0,"Iteration ["+str(index)+"]")
            screen.refresh()
            index = index + 1

    except Exception as err:
        exceps = str(err)

    curses.nocbreak()
    curses.curs_set(True)
    screen.keypad(False)
    curses.endwin()

    if "" != exceps:
        print ("ERROR:" + exceps)

if __name__ == "__main__":
    main(sys.argv[1:])