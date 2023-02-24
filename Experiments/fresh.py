import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(True)
    maxcol=curses.COLS
    maxrow=curses.LINES
    lside=60
    rside=curses.COLS-lside-2 #-2 for offset from left/right padding

    running=True
    #lside:
    win1=curses.newwin(10,lside,1,1) #1heigh, 20wide, y,x 
    win2=curses.newwin(10,lside,11,1)
    win3=curses.newwin(10,lside,21,1)
    #rside:
    win4=curses.newwin(5,rside,1,lside+1)
    win5=curses.newwin(maxrow-5-2,rside,6,lside+1)

    while running == True:
        win1.clear()
        win1.box()
        win1.addstr(1,1,f"Cols:{maxcol} Rows:{maxrow}")
        win1.refresh()

        win2.clear()
        win2.box()
        win2.addstr(1,1,"test2")
        win2.refresh()

        win3.clear()
        win3.box()
        win3.addstr(1,1,"test3")
        win3.refresh()

        win4.clear()
        win4.box()
        win4.addstr(1,1,"test4")
        win4.refresh()

        win5.clear()
        win5.box()
        win5.addstr(1,1,"test5")
        win5.refresh()

        c=stdscr.getch()
        if c==ord("q") or c==ord("Q"):
            stdscr.clear()
            running=False


wrapper(main)