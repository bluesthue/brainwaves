import curses
import sys


def main(argv):
    #pnl0=None
    pnl0_Dims=["TRACK",25,30,1,1] #Title,W,H,X,Y

    screen=curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(True)
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1,curses.COLOR_RED, curses.COLOR_BLACK)
    screen.keypad(True)
    exceps = ""

    try:
        running=True
        while True == running:
            ch=screen.getch()
            if ch== ord('Q') or ch == ord('q'):
                running=False
            screen.addstr(1,1,"RUNNING")
            #pnl0=curses.newwin(pnl0_Dims[1],pnl0_Dims[2],pnl0_Dims[3],pnl0_Dims[4])
            #pnl0.addstr(1,1, "TEST")
            #pnl0.bkgd(' ',curses.color_pair(1))
            #pnl0.box()
            #pnl0.refresh()
            screen.refresh()

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