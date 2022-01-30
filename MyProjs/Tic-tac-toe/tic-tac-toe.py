# Modules
import time as t

# all global varables
avalabel_sign = ["X","Y","A","B","P","Z","S","O"]

# Classes
class game_board:
    def __init__(self):
       self.one = "1"
       self.two = "2"
       self.three = "3"
       self.four = "4"
       self.five = "5"
       self.six = "6"
       self.seven = "7"
       self.eight = "8"
       self.nine = "9"
    @property
    def now_board(self):
       return f"""
      |     |
   {self.one}  |  {self.two}  |  {self.three}
______|_____|______
      |     |
   {self.four}  |  {self.five}  |  {self.six}
______|_____|______
      |     |
   {self.seven}  |  {self.eight}  |  {self.nine}
      |     |
   """
    def set_pos(self,pos:str,sym:str):
       if pos == "1" or pos == "one": self.one = sym
       elif pos == "2" or pos == "two": self.two = sym
       elif pos == "3" or pos == "three": self.three = sym
       elif pos == "4" or pos == "four": self.four = sym
       elif pos == "5" or pos == "five": self.five = sym
       elif pos == "6" or pos == "six": self.six = sym
       elif pos == "7" or pos == "seven": self.seven = sym
       elif pos == "8" or pos == "eight": self.eight = sym
       elif pos == "9" or pos == "nine": self.nine = sym
       else: raise NameError("Wrong position or wrong symbol")

# Functions
def whos_sym(sym,pla1,pla2):
   if sym == pla1:
      return "player_1"
   elif sym == pla2:
      return "player_2"
   else:
      raise KeyError(f"None on the symbol match to this {sym}")

def aft_set(check_win_func_res):
   if check_win_func_res[0] == True:
      print(f"{check_win_func_res[2]} win!")
      print(check_win_func_res[3])
      yield True
   else:
      print(check_win_func_res[3])
      yield False

def check_win(board_ins:game_board,pla1_sym:str,pla2_sym:str):
    if board_ins.one == board_ins.two == board_ins.three:
        return [True,board_ins.one,whos_sym(board_ins.one,pla1_sym,pla2_sym),f"""
      |      |
 --{board_ins.one}--|--{board_ins.two}--|--{board_ins.three}--
______|_____|______
      |     |
   {board_ins.four}  |  {board_ins.five}  |  {board_ins.six}
______|_____|______
      |     |
   {board_ins.seven}  |  {board_ins.eight}  |  {board_ins.nine}
      |     |
   """]
    elif board_ins.four == board_ins.five == board_ins.six:
        return [True,board_ins.four,whos_sym(board_ins.four,pla1_sym,pla2_sym),f"""
      |     |
   {board_ins.one}  |  {board_ins.two}  |  {board_ins.three}
______|_____|______
      |     |
 --{board_ins.four}--|--{board_ins.five}--|--{board_ins.six}--
______|_____|______
      |     |
   {board_ins.seven}  |  {board_ins.eight}  |  {board_ins.nine}
      |     |
   """]
    elif board_ins.seven == board_ins.eight == board_ins.nine:
        return [True,board_ins.seven,whos_sym(board_ins.seven,pla1_sym,pla2_sym),f"""
      |     |
   {board_ins.one}  |  {board_ins.two}  |  {board_ins.three}
______|_____|______
      |     |
   {board_ins.four}  |  {board_ins.five}  |  {board_ins.six}
______|_____|______
      |     |
 --{board_ins.seven}--|--{board_ins.eight}---|--{board_ins.nine}--
      |     |
   """]

    elif board_ins.one == board_ins.five == board_ins.nine:
        return [True,board_ins.one,whos_sym(board_ins.one,pla1_sym,pla2_sym),f"""
  \   |     |
   {board_ins.one}  |  {board_ins.two}  |  {board_ins.three}
_____\|_____|______
      |\    |
   {board_ins.four}  |  {board_ins.five}  |  {board_ins.six}
______|____\|______
      |     |\\
   {board_ins.seven}  |  {board_ins.eight}  |  {board_ins.nine}
      |     |   \\
   """]
    elif board_ins.three == board_ins.five == board_ins.seven:
        return [True,board_ins.three,whos_sym(board_ins.three,pla1_sym,pla2_sym),f"""
      |     |   /
   {board_ins.one}  |  {board_ins.two}  |  {board_ins.three}
______|_____|/_____
      |    /|
   {board_ins.four}  |  {board_ins.five}  |  {board_ins.six}
______|/____|______
     /|     |
   {board_ins.seven}  |  {board_ins.eight}  |  {board_ins.nine}
 /    |     |
   """]
    elif board_ins.one == board_ins.four == board_ins.seven:
        return [True,board_ins.one,whos_sym(board_ins.one,pla1_sym,pla2_sym),f"""
   |  |     |    
   {board_ins.one}  |  {board_ins.two}  |  {board_ins.three}
___|__|_____|______
   |  |     |
   {board_ins.four}  |  {board_ins.five}  |  {board_ins.six}
___|__|_____|______
   |  |     |
   {board_ins.seven}  |  {board_ins.eight}  |  {board_ins.nine}
   |  |     |
   """]
    elif board_ins.two == board_ins.five == board_ins.eight:
        return [True,board_ins.two,whos_sym(board_ins.two,pla1_sym,pla2_sym),f"""
      |  |  |    
   {board_ins.one}  |  {board_ins.two}  |  {board_ins.three}
______|__|__|______
      |  |  |
   {board_ins.four}  |  {board_ins.five}  |  {board_ins.six}
______|__|__|______
      |  |  |
   {board_ins.seven}  |  {board_ins.eight}  |  {board_ins.nine}
      |  |  |
   """]
    elif board_ins.three == board_ins.six == board_ins.nine:
        return [True,board_ins.one,whos_sym(board_ins.three,pla1_sym,pla2_sym),f"""
      |     |  |
   {board_ins.one}  |  {board_ins.two}  |  {board_ins.three}
______|_____|__|___
      |     |  |
   {board_ins.four}  |  {board_ins.five}  |  {board_ins.six}
______|_____|__|___
      |     |  |
   {board_ins.seven}  |  {board_ins.eight}  |  {board_ins.nine}
      |     |  |
   """]
    else: return [False]
    
print("WELCOME TO TIC-TAC-TOE!\n")
main_loop = True
while main_loop:
   while True:
       pl1_sym = input(f"Player 1 can choose there symbol from avablable symbols {avalabel_sign}\n")
       pl2_sym = input(f"Player 2 can choose there symbol from avablable symbols {avalabel_sign}\n")
       if pl1_sym in avalabel_sign and pl2_sym in avalabel_sign and pl2_sym != pl1_sym:
          break
       else:
          print(f"Please choose you symbols carefully! Player1 was choosed: {pl1_sym} and player 2 was choosed {pl2_sym}")

   Main_boad = game_board()
   print(Main_boad.now_board)
   draw_or_not = 0
   while True:
      draw_or_not += 1
      p1_cho = input("Player 1 turn! Choose a number.")
      Main_boad.set_pos(p1_cho,pl1_sym)
      con = list(check_win(Main_boad,pl1_sym,pl2_sym))
      if con[0] == True:
         print(f"{con[2]},Win!")
         print(con[3])
         break
      else:
         print(Main_boad.now_board)
         pass
      if draw_or_not >= 9:
         print("Match is draw!")
         break
      print(draw_or_not)
      draw_or_not += 1
      p2_cho = input("Player 2 turn! Choose a number.")
      Main_boad.set_pos(p2_cho,pl2_sym)
      con = check_win(Main_boad,pl1_sym,pl2_sym)
      if con[0] == True:
         print(f"{con[2]},Win!")
         print(con[3])
         break
      else:
         print(Main_boad.now_board)
         pass
      if draw_or_not >= 9:
         print("Match is draw!")
         break
      print(draw_or_not)
   t.sleep(3)
   cont_or_not = input("Do you like to continue?[y/n]:")
   cont_or_not = cont_or_not.upper()
   if cont_or_not == "YES" or cont_or_not == "Y": pass
   else: break





      