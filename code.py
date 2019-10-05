from sys import exit
try:
    from colorama import *
except:
    print("can't import colorama")
    print()
    exit()
try:
    import math
except:
    print("can't import math")
    print()
    exit()
try:
    import random
except:
    print("can't import random")
    print()
    exit()
print()
q = [" | | ", " | | ", " | | "]
r = Fore.CYAN + "\u2500\u253C\u2500\u253C\u2500" + Style.RESET_ALL
x = 0
y = 0
o = 0
st = ""
labelCoordinate = {"A": {"x":0, "y":0},
"B": {"x":1, "y":0},
"C": {"x":2, "y":0},
"D": {"x":0, "y":1},
"E": {"x":1, "y":1},
"F": {"x":2, "y":1},
"G": {"x":0, "y":2},
"H": {"x":1, "y":2},
"I": {"x":2, "y":2}}


def show_label_tip():
    colorprint("A|B|C")
    print(r)
    colorprint("D|E|F")
    print(r)
    colorprint("G|H|I")
def show_board():
#  print("\x1B[26;0H")
  colorprint(q[0])
  print(r)
  colorprint(q[1])
  print(r)
  colorprint(q[2])
  print()
def colorprint(row, isIntro = False):
    newrow = ""
    for ch in row:
        cc = ch
        if ch == "x" and not(isIntro):
            cc = Fore.RED + "x" + Style.RESET_ALL
        if ch == "o" and not(isIntro):
            cc = Fore.RED + "o" + Style.RESET_ALL
        if ch == "|":
            cc = Fore.BLUE + "\u2502" + Style.RESET_ALL
        if ch == "-" and isIntro:
          cc = Fore.BLUE + "\u2500" + Style.RESET_ALL
        if isIntro:
          cc = Fore.BLUE + ch + Style.RESET_ALL
        newrow = newrow + cc
    print(newrow)
def check():
    global x
    global y
    RNTBC = q[y]
    if RNTBC[x + x] == " ":
        return False
    else:
        return True
def win():
    global st
    wins = [[0, 2, 4], [8, 10, 12], [16, 18, 20], [0, 8, 16], [2, 10, 18],
            [4, 12, 20], [0, 10, 20], [4, 10, 16]]
    for win in wins:
        st = ""
        for cell in win:
            x = cell % 8
            y = cell / 8
            y = math.floor(y)
            st = st + q[y][x]
        if st == "ooo" or st == "xxx":
            return True
def good_input():
    global x
    global y
    global labelCoordinate
    while True:
      label = input("label of an empty space: ").upper()
      try:
        xycoordinates = labelCoordinate[label]
        x = xycoordinates["x"]
        y = xycoordinates["y"]
        if not(check()):
          break
        else:
          print("Try a different letter")
      except:
        print("Try a different letter")
def place(player_number):
    global x
    global y
    good_input()
    t = ""
    if player_number == 1:
        t = "o"
    else:
        t = "x"
    row = q[y]
    newrow = row[:x + x] + t + row[x + x + 1:]
    q[y] = newrow
    show_board()
def computerplace():
  global x
  global y
  while True:
    x = random.randrange(0, 2 + 1)
    y = random.randrange(0, 2 + 1)
    if not(check()):
      break
#  print("I will choose the empty space at (%s, %s)" % (x, y))
  print("I will choose the empty space whith the label of %s" % ("ABCDEFGHI"[3 * y + x]))
  row = q[y]
  newrow = row[:x + x] + "o" + row[x + x + 1:]
  q[y] = newrow
  print()
  show_board()
def choosemode():
  while True:
    a = input("Which mode?(1 player or 2 player) ")
    if a == "1 player":
      return "1pmode"
    elif a == "2 player":
      return "2pmode"
def main():
    global st
    global o
    o = 0
    player_number = 0
    a = ""
    colorprint("\u250C----------------------------------------------------------------------------\u2510", True)
    colorprint("|                   Welecome to the tic tac toe game!                        |", True)
    colorprint("|                                                                            |", True)
    colorprint("| How to play:                                                               |", True)
    colorprint("| Enter the label of an empty space on the board to place a piece there      |", True)
    colorprint("|                                                                            |", True)
    colorprint("| How to win:                                                                |", True)
    colorprint("| Try to get your piece in a vertical, across, or a diagonal line to win!    |", True)
    colorprint("|                                                                            |", True)
    colorprint("\u2514----------------------------------------------------------------------------\u2518", True)
    if choosemode() == "1pmode":
#      print("Sorry, this mode is still unavalable yet")
      print("The tip for the labels:")
      show_label_tip()
      print("let's play the game!")
      show_board()
      while True:
        oneplayerrungame(player_number % 2)
        player_number += 1
    else:
      print("The tip for the labels:")
      show_label_tip()
      print("let's play the game!")
      show_board()
      while True:
        twoplayerrungame(player_number % 2)
        player_number += 1
def twoplayerrungame(player_number):
    global o
    place(player_number)
    if win():
        print(Fore.GREEN + st[0], Style.RESET_ALL + "won")
        input("press enter to quit ")
        exit()
    o += 1
    if o == 9:
        print(Fore.YELLOW + "Tie")
        input("press enter to quit ")
        exit()
def oneplayerrungame(playernumber):
    global o
    if playernumber == 0:
      place(0)
    else:
      computerplace()
    if win():
        print(Fore.GREEN + st[0], Style.RESET_ALL + "won")
        input("press enter to quit ")
        exit()
    o += 1
    if o == 9:
        print(Fore.YELLOW + "Tie")
        input("press enter to quit")
        exit()
if __name__ == "__main__":
  main()
