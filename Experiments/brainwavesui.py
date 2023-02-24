import curses
import math
import sys


def main(argv):
    screenMaxX=1024
    screenMaxY=600

    intPanels=5
    #pnl0=None
    pnl0_Dims=["TRACK",25,30,1,1] #Title,W,H,X,Y
    pnl1=None
    pnl1_Dims=["IN",25,30,1,33] #Title,W,H,X,Y
    pnl2=None
    pnl2_Dims=["OUT",25,30,1,66] #Title,W,H,X,Y
    pnl3=None
    pnl3_Dims=["Menu",80,10,28,1] #Title,W,H,X,Y
    pnl4=None
    pnl4_Dims=["Tracks",80,80,28,13] #Title,W,H,X,Y

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
            pnl0=curses.newwin(pnl0_Dims[1],pnl0_Dims[2],pnl0_Dims[3],pnl0_Dims[4])
            pnl0.addstr(1,1, "TEST")
            pnl0.bkgd(' ',curses.color_pair(1))
            pnl0.box()
            pnl0.refresh()
            #pnl1=curses.newwin(pnl1_Dims[1],pnl1_Dims[2],pnl1_Dims[3],pnl1_Dims[4])
            #pnl1.bkgd(' ',curses.color_pair(1))
            #pnl1.box()
            #pnl2=curses.newwin(pnl2_Dims[1],pnl2_Dims[2],pnl2_Dims[3],pnl2_Dims[4])
            #pnl2.bkgd(' ',curses.color_pair(1))
            #pnl2.box()
            #pnl3=curses.newwin(pnl3_Dims[1],pnl3_Dims[2],pnl3_Dims[3],pnl3_Dims[4])
            #pnl3.bkgd(' ',curses.color_pair(1))
            #pnl3.box()
            #pnl4=curses.newwin(pnl4_Dims[1],pnl4_Dims[2],pnl4_Dims[3],pnl4_Dims[4])
            #pnl4.bkgd(' ',curses.color_pair(1))
            #pnl4.box()
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