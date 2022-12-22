import random

l=["rock" ,"paper" ,"scissor" ]
'''
Rock vs paper->    Paper win
Rock vs scissor->  Rock win
Paper vs Scissor-> Scissor win

'''
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start....
1 Yes
2 NO | Exit 

    '''))
    if uc==1:
        for a in range(1,6):
           userInput=int(input('''
1 Rock
2 Scissor
3 Paper
'''))
           if userInput==1:
               uchoice="rock"
           elif userInput==2:
              uchoice="scissor"
           elif userInput==3:
                 uchoice="paper"
           Cchoice=random.choice(l)
           if Cchoice==uchoice:
               print("Cumputer value",Cchoice)
               print("user value",uchoice)
               print("Game Draw")
               ucount=ucount+1
               ccount=ccount+1
           elif (uchoice=="rock" and Cchoice=="scissor") or ( uchoice
              =="paper" and Cchoice=="rock") or (uchoice=="scissor" and Cchoice=="paper"):
               print("you win")
               print("Cumputer value", Cchoice)
               print("user value", uchoice)
               ucount=ucount+1
           else:
               print("Cumputer value", Cchoice)
               print("user value", uchoice)
               print("computer win")
               ccount=ccount+1

        if ucount==ccount:
          print("final game draw")
          print("user score",ucount)
          print("computer score",ccount)
        elif ucount>ccount:
          print("final you win")
          print("user score", ucount)
          print("computer score", ccount)
        else:
          print("final computer win")
          print("user score", ucount)
          print("computer score", ccount)

