# Some basic function for Printing and Timing
  two function for colorful printing, a class for timing.

## Requirements

- [Python 3.x](https://www.python.org/downloads/)

## Function list
- **<font color=#ff8000>printf</font>**(print_text, \*args, textColor='white', end=' ')    
    The usage of this function is similer to 'printf' in C/C++ but you could set your own text color.             
    ```python
       printf("i=%d\n", 10, textColor='green')
       printf("i=%d\n" % 10, textColor='red')
       printf("i=%d\n", 10)
       printf("i=%d\n" % 10)
    ```
- **<font color=#ff8000>print2</font>**(print_text, \*args, textColor='white', end='\n')
    The usage of this function is similer to 'print' in Python but with a key parameter 'textColor' more
    ```Python
       print2("i=%d" % 10, textColor='green')
       print2("i=%d" % 10, [1, 2, 3], textColor='red')
       print2("i=%d" % 10, [1, 2, 3])
    ```
## Class list
- **<font color=#0000ff>class</font> <font color=#0080ff>Timer</font>**
    ```Python
       T=Timer()
       T.begin()
       # some function
       T.end("Func")
    ```
## Author

Chen Yu / [@Chen Yu](https://github.com/chinue)
