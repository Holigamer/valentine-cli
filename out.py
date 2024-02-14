from termcolor import colored
import time
import os

def output(f):
    print()
    for line in f:
        output_line = ""
        buf_text = ""
        cur_color = ""
        for char in line:
            if char=='1':
                if cur_color != "":
                    # there is a color for line
                    output_line += colored(buf_text, cur_color, attrs=["bold"])
                    buf_text = ""
                cur_color = "red"
            elif char=='2':
                if cur_color != "":
                    # there is a color for line
                    output_line += colored(buf_text, cur_color, attrs=["bold"])
                    buf_text = ""
                cur_color = "white"
            elif char=='0':
                # there is a color for line
                output_line += colored(buf_text+"\n", cur_color, attrs=["bold"])
                buf_text = ""
                cur_color = ""
            else:
                buf_text+=char
        print(output_line, end="")
    print()

b = True
while True:
    b = not b
    os.system('clear')
    if b:
        f1 = open("s1.txt", "r")
        output(f1)
        f1.close()
    else:
        f2 = open("s2.txt", "r")
        output(f2)
        f2.close()
    time.sleep(1)

#cprint("Hello", "white", "on_red", attrs=["bold"])