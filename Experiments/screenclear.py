import curses
import pyfiglet
from pyfiglet import Figlet

screen=curses.initscr()
curses.start_color()
curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)


fig=Figlet(font='graffiti')
strtitle=fig.renderText("ARCADE PIRATE")
with open("splashtitle.txt",'r') as titlefile:
    strtitle=titlefile.read()
strtitle=strtitle+"\n PRESENTS..."

screen.addstr(strtitle,curses.color_pair(2))
screen.refresh()
curses.napms(2500)
screen.clear()

with open("splash2.txt",'r') as titlefile:
    strtitle=titlefile.read()

screen.addstr(0,0,strtitle,curses.color_pair(1))
screen.refresh()
curses.napms(5000)

curses.endwin()