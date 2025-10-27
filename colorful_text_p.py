import time  # it is imported to use sleep function

text = "Python is awesome😎😎"
colors = [31, 32, 33, 34, 35, 36, 37]  # it is a list of ANSI color code(31-37)

for i in range(10):
    line = ""
    for idx, char in enumerate(text):

        color_code = colors[(idx + i) % len(colors)]  # it creating the rainbow effect

        line += f"\033[1;{color_code}m{char}\033[0m"
        """  ANSI escape secquence  == used to print the selected color  ANSI escape sequence: The f-string creates an ANSI escape sequence, which is used to print the character in the selected color. The sequence is:
       \033[1;{color_code}m: Sets the color and makes the text bold.
     {char}: The character to be printed.
     \033[0m: Resets the color to default."""

        print(line)
        time.sleep(0.3)  # it pauses the execution for specified time
