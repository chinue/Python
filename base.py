# -*- coding: utf-8 -*-
"""
    date: 2017-03-21
    by: Chen Yu
    function: printf, print2
    class: Timer
"""
import platform

isWindows=(platform.system()=="Windows")
#print(isWindows)
import ctypes

STD_OUTPUT_HANDLE= -11

# 用于Printf字体颜色参数
TEXT_COLOR_BLACK     = 0  # - black
TEXT_COLOR_DaBLUE    = 1  # - dark blue
TEXT_COLOR_DaGREEN   = 2  # - dark green
TEXT_COLOR_DaCYAN    = 3  # - dark cyan
TEXT_COLOR_DaRED     = 4  # - dark red
TEXT_COLOR_DaMAGENTA = 5  # - dark magenta
TEXT_COLOR_GOLDEN    = 6  # - golden
TEXT_COLOR_GRAY      = 7  # - gray
TEXT_COLOR_DaGRAY    = 8  # - dark gray
TEXT_COLOR_BLUE      = 9  # - blue
TEXT_COLOR_GREEN     = 10 # - green
TEXT_COLOR_CYAN      = 11 # - cyan
TEXT_COLOR_RED       = 12 # - red
TEXT_COLOR_MAGENTA   = 13 # - magenta
TEXT_COLOR_YELLOW    = 14 # - yellow
TEXT_COLOR_WHITE     = 15 # - white

if(isWindows):
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

#import sys
import types
win_color_map = {"black":0, "dark blue":1,"dark green":2, "dark cyan":3, "dark red":4, "dark magenta":5, "dark pink":5, "golden":6, 
        "gray":7, "dark gray":8, "blue":9, "green":10, "cyan":11, "red":12, "magenta":13, "pink":13, "yellow":14, "white":15}

linux_color_map={"end":"\033[0m", "black":"\033[0;30m", "red":"\033[1;31m", "green":"\033[1;32m", "yellow":"\033[1;33m", 
                 "blue":"\033[1;34m", "magenta":"\033[1;35m", "cyan":"\033[1;36m", "white":"\033[1;37m","gray":"\033[0;37m",
                 "dark blue":"\033[0;34m", "dark red":"\033[0;31m", "dark green":"\033[0;32m", "golden":"\033[0;33m", 
                 "dark magenta":"\033[0;35m", "dark gray":"\033[0;37m", "dark cyan":"\033[0;36m"}
linux_color_list=["black", "red", "green", "yellow","blue", "magenta", "cyan", "white", "gray", "dark blue", "dark red", "dark green",
                   "golden", "dark magenta", "dark gray", "dark cyan"]

def printf(print_text, *args, textColor="white", end = ""):
    ''' 
    printf is similar to print but with more text color parameter AND do not append a newline by default.
    textColor: use const int value [TEXT_COLOR_RED, TEXT_COLOR_GREEN, TEXT_COLOR_BLUE, TEXT_COLOR_YELLOW, TEXT_COLOR_WHITE, ...]
               or string value ['red', 'green', 'blue', 'yellow', 'white', ...]
    print_text: text to print
    args: more arguments to print
    '''
    if(isWindows):
        if(type(textColor)==type('a')):
            textColor=textColor.lower()
            textColor=win_color_map[textColor]
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, textColor)
        print(print_text % args, end=end, flush=True)
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, TEXT_COLOR_WHITE)
    else:
        if(type(textColor)==type(1)):
            textColor=linux_color_list[textColor]
        textColor=textColor.lower()
        s = print_text % args
        s = linux_color_map[textColor] + s +linux_color_map["end"]
        print(s, end=end, flush=True)

def print2(print_text, *args, textColor="white", end = "\n"):
    ''' 
    print2 is similar to print but with more text color parameter.
    textColor: use const int value [TEXT_COLOR_RED, TEXT_COLOR_GREEN, TEXT_COLOR_BLUE, TEXT_COLOR_YELLOW, TEXT_COLOR_WHITE, ...]
               or string value ['red', 'green', 'blue', 'yellow', 'white', ...]
    print_text: text to print
    args: more arguments to print
    '''
    n=len(args)
    if(isWindows):
        if(type(textColor)==type('a')):
            textColor=textColor.lower()
            textColor=win_color_map[textColor]
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, textColor)
        if(n==0):
            print(print_text, end=end)
        elif(n==1):
            print(print_text, args[0], end=end)
        else:
            print(print_text, args, end=end)
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, TEXT_COLOR_WHITE)
    else:
        if(type(textColor)==type(1)):
            textColor=linux_color_list[textColor]
        textColor=textColor.lower()
        s = linux_color_map[textColor] + print_text +linux_color_map["end"]
        if(n==0):
            print(s, end=end)
        elif(n==1):
            print(s, args[0], end=end)
        else:
            print(s, args, end=end)

if(isWindows!=True):
    import time

class Timer:
    """
    usage: 
          T=Timer()
          T.begin()
          # the code you want to estimate timing
          T.end("Fun")
    """
    def __init__(self):
        if(isWindows):
            freq=ctypes.c_longlong(0)
            ctypes.windll.kernel32.QueryPerformanceFrequency(ctypes.byref(freq))
            self.__freq=freq.value
        else:
            self.__freq=1.0

    def begin(self):
        if(isWindows):
            t=ctypes.c_longlong(0)
            ctypes.windll.kernel32.QueryPerformanceCounter(ctypes.byref(t))
            self.__t1=t.value
        else:
            self.__t1=time.time()
        return self.__t1

    def end(self, tag = 'run', isPrint=True, end='\n'):
        """
        used to print program running time
        tag: main message to print
        isPrint: whether print or not

        the return value is the milliseconds which between begin() and end()
        """
        if(isWindows):
            t=ctypes.c_longlong(0)
            ctypes.windll.kernel32.QueryPerformanceCounter(ctypes.byref(t))
            self.__t2=t.value
        else:
            self.__t2=time.time()
        diff=1000.0*(self.__t2-self.__t1)/self.__freq
        if(isPrint):
            if(diff>1000):
                printf("%s time=%.3f sec", tag, diff/1000.0, textColor="red", end=end)
            elif(diff>1):
                printf("%s time=%5.3f ms", tag, diff, textColor="green", end=end)
            else:
                printf("%s time=%.0f us", tag, diff*1000.0, textColor="yellow", end=end)
        self.__t1=self.__t2
        return diff
