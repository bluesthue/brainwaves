import curses
import cursesmenu
from cursesmenu import CursesMenu
import pyfiglet
from pyfiglet import Figlet

a_list=["red","blue","green"]

screen=curses.initscr()

menu=CursesMenu.make_selection_menu(a_list,"Select an Option")
menu.show()
menu.join()
selection=menu.select_option
col=1
match selection:
    case 'red':
        col=1
    case 'green':
        col=2
    case 'blue':
        col=3


curses.start_color()
curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_BLACK)

with open("splashtitle.txt",'r') as titlefile:
    strtitle=titlefile.read()

screen.addstr(strtitle,curses.color_pair(col))

screen.refresh()
curses.napms(10000)
screen.clear()

curses.endwin()