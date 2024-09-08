import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.geometry('400x400')
root.configure(bg='darkorange')
label1=tk.Label(root,text="YAHTZEE GAME",anchor='center',font=('Times_New_Roman',10),bg='cyan')
label1.grid(row=0,column=2)
count=0
turn_count=0


def turn_input():
    global turn_list
    turn_list=list(map(int,input("Enter 5 numbers from 1 to 6 separated by space : ").split()))
   

def turn_button():
    global turn_list
    global b
    #turn_list=[]
    b=tk.Button(root,text=f"TURN { turn_count+1}",width=10,bg="coral",command=turn_input)
    b.place(x=100,y=350)

def aces(*args):                        
    global turn_list
    global aces_value
    global turn_count
    global b
    aces_value=turn_list.count(1)
    e1.config(state="normal")
    e1.insert(0,aces_value)
    e1.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b1.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")
   
def twos(*args):
    global turn_list
    global twos_value
    global turn_count
    global b
    twos_value=turn_list.count(2)*2
    e2.config(state="normal")
    e2.insert(0,twos_value)
    e2.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b2.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")
   
       
def threes(*args):
    global turn_list
    global threes_value
    global turn_count
    global b
    threes_value=turn_list.count(3)*3
    e3.config(state="normal")
    e3.insert(0,threes_value)
    e3.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b3.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")
   
   
def fours(*args):
    global turn_list
    global fours_value
    global b
    global turn_count
    fours_value=turn_list.count(4)*4
    e4.config(state="normal")
    e4.insert(0,fours_value)
    e4.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b4.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")
   

def fives(*args):
    global turn_list
    global fives_value
    global b
    global turn_count
    fives_value=turn_list.count(5)*5
    e5.config(state="normal")
    e5.insert(0,fives_value)
    e5.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b5.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")
 
def sixes(*args):
    global turn_list
    global sixes_value
    global b
    global turn_count
    sixes_value=turn_list.count(6)*6
    e6.config(state="normal")
    e6.insert(0,sixes_value)
    e6.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b6.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")
   
def ts(*args):
    global aces_value
    global twos_value
    global threes_value
    global fours_value
    global fives_value
    global sixes_value
    global ts_value
    ts_value=aces_value+twos_value+threes_value+fours_value+fives_value+sixes_value
    e14.config(state="normal")
    e14.insert(0,ts_value)
    e14.config(state="readonly")
    b14.config(state="disabled")

def bonus(*args):  
    global ts_value
    global bonus
    global b
    global turn_count
    if ts_value>=63:
     bonus=35
    else:
     bonus=0
    e15.config(state="normal")
    e15.insert(0,bonus)
    e15.config(state="readonly")
    b15.config(state="disabled")

def total_upper(*args):
    global ts_value
    global bonus
    global total_upp
    total_upp=ts_value+bonus
    e16.config(state="normal")
    e16.insert(0,total_upp)
    e16.config(state="readonly")
    b16.config(state="disabled")
                                                          #LOWER
                              #CALCULATION OF THREE OF A KIND,FOUR OF A KIND,FULL HOUSE,SMALL STRAIGHT,LARGE STRAIGHT(LOWER)


def tok(*args):                                # CALCULATION OF THREE OF A KIND
    global tok_value
    global turn_list
    global b
    global turn_count
    if(turn_list[0]==turn_list[2] or turn_list[1]==turn_list[3] or turn_list[2]==turn_list[4]):
        tok_value=sum(turn_list)
    else:
        tok_value=0
                                        #INSERTING THE VALUE INTO THREE OF A KIND ENTRY
    e7.config(state="normal")
    e7.insert(0,tok_value)
    e7.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b7.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")

def fok(*args):
    global turn_list
    global fok_value
    global b
    global turn_count
    if turn_list[0]==turn_list[3] or turn_list[1]==turn_list[4]:
      fok_value=sum(turn_list)
    else:
      fok_value=0
    e8.config(state="normal")
    e8.insert(0,fok_value)
    e8.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b8.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")

def fh(*args):
    global turn_list
    global fh_value
    global b
    global turn_count
    if ((turn_list[0]==turn_list[2] and turn_list[3]==turn_list[4]) or (turn_list[0]==turn_list[1] and turn_list[2]==turn_list[4]) or (turn_list[0]==turn_list[4] and turn_list[1]==turn_list[3])) and len(set(turn_list))==2:
        fh_value=25
    else:
        fh_value=0
   
    e9.config(state="normal")
    e9.insert(0,fh_value)
    e9.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b9.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")

def ss(*args):
    global ss_value
    global turn_list
    global b
    global turn_count
    if (turn_list[0]==2 and turn_list[3]==5) or (turn_list[0] ==1 and turn_list[3]==4) or (turn_list[0] ==3 and turn_list[3]==6) or (turn_list[1] ==1 and turn_list[4]==4) or (turn_list[1] ==2 and turn_list[4]==5) or (turn_list[1] ==3 and turn_list[4]==6) :          
      ss_value=30
    else:
      ss_value=0
    e10.config(state="normal")
    e10.insert(0,ss_value)
    e10.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b10.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")


def ls(*args):
    global turn_list
    global ls_value
    global b
    global turn_count
    if ((turn_list[0]==1 and turn_list[4]==5) or (turn_list[0] ==2 and turn_list[4]==6)) and (len(set(turn_list))==5):
      ls_value=40
    else:
      ls_value=0
    e11.config(state="normal")
    e11.insert(0,ls_value)
    e11.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b11.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")

def yahtzee(*args):
    global count
    global turn_list
    global yaht_value
    global b
    global turn_count
    if len(set(turn_list))==1:
      yaht_value=50
      count=count+1
    else:
       yaht_value=0  
    if count<=1:     #only if the count =0(no yahtzee) or count=1(yahtzee for the first time,entry is made)
     e12.config(state="normal")    
     e12.insert(0,yaht_value)
     e12.config(state="readonly")

    turn_count=turn_count+1
    if turn_count<=13:               # HERE YAHTZEE BUTTON IS NOT DISABLED AS ONE CAN GO FOR IT AGAIN TO GET A BONUS OF 100
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")
   

def yaht_bon(*args):
    global count
    global yaht_bonus
    global b
    global turn_count
   
    if count>1:
        yaht_bonus=100  
    else:
        yaht_bonus=0
   
    e17.config(state="normal")
    e17.insert(0,yaht_bonus)
    e17.config(state="readonly")
    b12.config(state="disabled")  # disable yahtzee button ONCE BONUS IS CALCULATED
    b17.config(state="disabled")  # disable bonus button
 

def chance(*args):
    global chance_value
    global turn_list
    global b
    global turn_count
    chance_value=sum(turn_list)
    e13.config(state="normal")
    e13.insert(0,chance_value)
    e13.config(state="readonly")
    turn_count=turn_count+1
    if turn_count<=13:
        b13.config(state="disabled")
        turn_button()
    else:
        print("No more turns left")
        b.config(state="disabled")


def total_lower(*args):  
    global total_low
    global tok_value
    global fok_value
    global fh_value
    global ss_value
    global ls_value
    global yaht_value
    global yaht_bonus
    global chance_value
    total_low=tok_value+fok_value+fh_value+ss_value+ls_value+yaht_value+yaht_bonus+chance_value
   
    e18.config(state="normal")
    e18.insert(0,total_low)
    e18.config(state="readonly")

def grand_total(*args):
    global total_upp
    global total_low
    grand_tot=total_upp+total_low
   
    e19.config(state="normal")
    e19.insert(0,grand_tot)
    e19.config(state="readonly")


turn_button()
                   
                                #GUI FOR BUTTONS AND ENTRIES
                            #GUI FOR BUTTONS AND ENTRIES FOR UPPER
b1=tk.Button(root,text="ACES",width=10,bg='mediumspringgreen',fg='black')
b1.grid(row=5,column=1)
e1=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e1.grid(row=5,column=2)
b1.bind("<Button-1>",aces)

b2=tk.Button(root,text="TWOS",width=10,bg='coral2',fg='black')
b2.grid(row=6,column=1)
e2=tk.Entry(root,state="readonly",font=15,width=8,bg='blue',fg='black')
e2.grid(row=6,column=2)
b2.bind("<Button-1>",twos)

b3=tk.Button(root,text="THREES",width=10,bg='peachpuff2',fg='black')
b3.grid(row=7,column=1)
e3=tk.Entry(root,state="readonly",font=15,width=8,bg='blue',fg='black')
e3.grid(row=7,column=2)
b3.bind("<Button-1>",threes)

b4=tk.Button(root,text="FOURS",width=10,bg='SlateBlue2',fg='black')
b4.grid(row=8,column=1)
e4=tk.Entry(root,state="readonly",font=15,width=8,bg='blue',fg='black')
e4.grid(row=8,column=2)
b4.bind("<Button-1>",fours)

b5=tk.Button(root,text="FIVES",width=10,bg='lightgoldenrod',fg='black')
b5.grid(row=9,column=1)
e5=tk.Entry(root,state="readonly",font=15,width=8,bg='blue',fg='black')
e5.grid(row=9,column=2)
b5.bind("<Button-1>",fives)

b6=tk.Button(root,text="SIXES",width=10,bg='medium aquamarine',fg='black')
b6.grid(row=10,column=1)
e6=tk.Entry(root,state="readonly",font=15,width=8,bg='blue',fg='black')
e6.grid(row=10,column=2)
b6.bind("<Button-1>",sixes)

b14=tk.Button(root,text="Total Score",width=10,bg='lemon chiffon',fg='black')
b14.grid(row=11,column=1)
e14=tk.Entry(root,state="readonly",font=15,width=8,bg='blue',fg='black')
e14.grid(row=11,column=2)
b14.bind("<Button-1>",ts)

b15=tk.Button(root,text="BONUS",width=10,bg='lime green',fg='black')
b15.grid(row=12,column=1)
e15=tk.Entry(root,state="readonly",font=15,width=8,bg='blue',fg='black')
e15.grid(row=12,column=2)
b15.bind("<Button-1>",bonus)

b16=tk.Button(root,text="Total Upper",width=10,bg='cyan',fg='black')
b16.grid(row=13,column=1)
e16=tk.Entry(root,state="readonly",font=15,width=8,bg='blue',fg='black')
e16.grid(row=13,column=2)
b16.bind("<Button-1>",total_upper)



                               
                               #GUI FOR BUTTONS AND ENTRIES OF LOWER
b7=tk.Button(root,text="3 Of A Kind",width=10,bg='greenyellow',fg='black')
b7.grid(row=5,column=3)
e7=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e7.grid(row=5,column=4)
b7.bind("<Button-1>",tok)

b8=tk.Button(root,text="4 Of A Kind",width=10,bg='palevioletred',fg='black')
b8.grid(row=6,column=3)
e8=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e8.grid(row=6,column=4)
b8.bind("<Button-1>",fok)

b9=tk.Button(root,text="Full House",width=10,bg='yellow',fg='black')
b9.grid(row=7,column=3)
e9=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e9.grid(row=7,column=4)
b9.bind("<Button-1>",fh)

b10=tk.Button(root,text="Small Straight",width=10,bg='DodgerBlue2',fg='black')
b10.grid(row=8,column=3)
e10=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e10.grid(row=8,column=4)
b10.bind("<Button-1>",ss)

b11=tk.Button(root,text="Large Straight",width=10,bg='light coral',fg='black')
b11.grid(row=9,column=3)
e11=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e11.grid(row=9,column=4)
b11.bind("<Button-1>",ls)

b12=tk.Button(root,text="YAHTZEE",width=10,bg='SlateBlue1',fg='black')
b12.grid(row=10,column=3)
e12=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e12.grid(row=10,column=4)
b12.bind("<Button-1>",yahtzee)

b13=tk.Button(root,text="Chance",width=10,bg='snow4',fg='black')
b13.grid(row=11,column=3)
e13=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e13.grid(row=11,column=4)
b13.bind("<Button-1>",chance)

b17=tk.Button(root,text="Yahtzee Bonus",width=10,bg='light salmon',fg='black')
b17.grid(row=12,column=3)
e17=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e17.grid(row=12,column=4)
b17.bind("<Button-1>",yaht_bon)

b18=tk.Button(root,text="Total Lower",width=10,bg='cyan',fg='black')
b18.grid(row=13,column=3)
e18=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e18.grid(row=13,column=4)
b18.bind("<Button-1>",total_lower)

b19=tk.Button(root,text="GRAND TOTAL",width=10,bg='cyan',fg='black')
b19.grid(row=15,column=2)
e19=tk.Entry(root,state="readonly",font=15,width=8,bg='pink',fg='black')
e19.grid(row=15,column=3)
b19.bind("<Button-1>",grand_total)


root.mainloop()