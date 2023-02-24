import curses
from curses import wrapper
import math

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(True)
    if curses.has_colors():
        curses.start_color()
        curses.init_pair(1,curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2,curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(3,curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(4,curses.COLOR_BLACK,curses.COLOR_RED)
        curses.init_pair(5,curses.COLOR_WHITE, curses.COLOR_BLUE)
        curses.init_pair(6,curses.COLOR_BLUE,curses.COLOR_WHITE)

    intMaxcol=curses.COLS
    intMaxrow=curses.LINES
    lside=math.floor(intMaxcol/2)-2
    rside=intMaxcol-lside-4 #-2 for offset from left/right padding
    height=intMaxrow-2
    keychar=''


    running=True
    intColor=2
    intReverse=5
    intSelPanel=0 #0=menu, 1=whatever is in right panel

    
    intTracks=8
    
    intBtnHeight=math.floor((intMaxrow-4)/4)
    intBtnWidth=math.floor((rside-4)/4)
    

    #lside:
    win1=curses.newwin(height,lside,1,1) #1heigh, 20wide, y,x
    #rside: 
    win2=curses.newwin(height,rside,1,lside+2)

    #multitrack:
    btnA=None
    btnB=None
    btnC=None
    btnD=None
    btnE=None
    btnF=None
    btnG=None
    btnH=None
    btns=[btnA,btnB,btnC,btnD,btnE,btnF,btnG,btnH]
    chnls=[10,10,4,5,1,2,3,6]
    trackstates=[1,1,1,1,1,1,1,1] #0=off, 1=on, 2=record, 6=wavplay read new state on each loop
    trackfiles=['','','','','','','','']

    #menu system
    menuopts=['PERFORM','EDIT TRACK','SAVE TRACK','TUNER','SCREEN SAVER']
    intMenuopts=len(menuopts)
    intActiveView=0
    intMenuWidth=16
    padWidth=lside-8
    padHeight=height-6-intMenuopts
    padX=4
    padY=10+intMenuopts
    anipad=curses.newpad(padHeight,padWidth)
    anipad.bkgd(' ',curses.color_pair(6))
    aniloopstep=0
    aniloopmaxstep=padWidth
    #LT = 201 or 169 or 213
    #RT = 187 or 170 or 191
    #LB = 200 or 192 or 212 
    #RB = 188 or 217 or 190
    
    #clock
    intMaxSteps=32
    intCurStep=1
    intPlaybackState=0
    intTempo=120
    intMilTempo=math.floor(60000/intTempo)
    clockrun=False
    
    while running == True:
        #MENU:
        win1.clear()
        win1.box()
        win1.addstr(1,1,"[[MENU]]")
        win1.bkgd(' ',curses.color_pair(intColor))
        for i in range(intMenuopts):
            xtr=intMenuWidth-len(menuopts[i])
            xspc=''
            for j in range(xtr):
                xspc=xspc+' '
            if i == intActiveView:
                win1.addstr(i+3,4,"-["+menuopts[i]+xspc+"]-",curses.color_pair(intReverse))
            else:
                win1.addstr(i+3,4," :"+menuopts[i]+xspc+": ",curses.color_pair(intColor))
        win1.refresh()

        with open("splashtitle.txt",'r') as titlefile:
            anitext=titlefile.read()
        #anipad.addstr(0,0,anitext)
        #aniloopstep=aniloopstep+1
        #anipad.refresh(0,0,padY,padX+aniloopstep,padHeight,padWidth)

        #WINDOW:
        win2.clear()
        win2.box()
        win2.addstr(1,1,"[["+menuopts[intActiveView]+"]]")
        win2.bkgd(' ',curses.color_pair(intColor))
        win2.addstr(height-2,1,str(keychar))
        win2.refresh()

        match intActiveView:
            case 0:
                for i in range(intTracks):
                    ypos=4
                    xpos=(i*intBtnWidth)+2 #+lside+5
                    if(i>math.floor((intTracks/2)-1)):
                        ypos=intBtnHeight+4
                        xpos=(i-4)*intBtnWidth+2 #+lside+5
                    btns[i]=win2.derwin(intBtnHeight,intBtnWidth,ypos,xpos)
                    if(trackstates[i]==1):
                        btns[i].bkgd(' ',curses.color_pair(intReverse))
                    else:
                        btns[i].bkgd(' ',curses.color_pair(intColor))
                    btns[i].box()
                    btns[i].addstr(1,1,chr(i+65)+':'+str(chnls[i]))
                    btns[i].refresh()

        c=stdscr.getch()
        keychar=c
        if c==ord("q") or c==ord("Q"):
            stdscr.clear()
            running=False
        elif c==ord("a"):
            trackstates=toggleTracks(trackstates,0)
        elif c==ord("b"):
            trackstates=toggleTracks(trackstates,1)
        elif c==ord("c"):
            trackstates=toggleTracks(trackstates,2)
        elif c==ord("d"):
            trackstates=toggleTracks(trackstates,3)
        elif c==ord("e"):
            trackstates=toggleTracks(trackstates,4)
        elif c==ord("f"):
            trackstates=toggleTracks(trackstates,5)
        elif c==ord("g"):
            trackstates=toggleTracks(trackstates,6)
        elif c==ord("h"):
            trackstates=toggleTracks(trackstates,7)
        elif c==258 and intSelPanel==0: #down arrow when menu selected
            intActiveView=menuchange(1,intActiveView,intMenuopts)
        elif c==259 and intSelPanel==0: #up arrow when menu selected
            intActiveView=menuchange(-1,intActiveView,intMenuopts)

def toggleTracks(ts,tt):
    if ts[tt]==1:
        ts[tt]=0
    else:
        ts[tt]=1
    return ts

def menuchange(dir,active,opts):
    i=active+dir
    if i<0:
        i=opts-1
    if i==opts:
        i=0
    return i

def updatetempo(t):
    intTempo=t
    intMilTempo=math.floor(60000/intTempo)


wrapper(main)