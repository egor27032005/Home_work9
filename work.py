from telebot import TeleBot, types
from random import randint
TOKEN=''
bot = TeleBot(TOKEN)
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]

@bot.message_handler(commands=['start', 'help'])
def answer(msg: types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=f'👋ходи за крестик')
    bot.send_message(chat_id=msg.from_user.id, text=f' 1 2 3 \n4 5 6 \n7 8 9')
    for i in range(9):
        maps[i]=i+1
maps=[1,2,3,4,5,6,7,8,9]

@bot.message_handler()
def answer(msg: types.Message):
    a = int(msg.text)
    win=0
    
    if maps[a-1]=="X" or maps[a-1]=="O":
        bot.send_message(chat_id=msg.from_user.id, text=f'это место уже занято, ходи нормально')
        a = int(msg.text)
        maps[a-1]='X'
    elif maps[a-1]!="X" and maps[a-1]!="O":
        maps[a-1]='X' 

    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            bot.send_message(chat_id=msg.from_user.id, text=f'{maps[0]} {maps[1]} {maps[2]} \n{maps[3]} {maps[4]} {maps[5]} \n{maps[6]} {maps[7]} {maps[8]}')
            bot.send_message(chat_id=msg.from_user.id, text=f'ты выйграл')
            win=1
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O" and win==0:
            bot.send_message(chat_id=msg.from_user.id, text=f'{maps[0]} {maps[1]} {maps[2]} \n{maps[3]} {maps[4]} {maps[5]} \n{maps[6]} {maps[7]} {maps[8]}')
            bot.send_message(chat_id=msg.from_user.id, text=f'ты проиграл')
            win=1

    if maps.count('X')==5:
        bot.send_message(chat_id=msg.from_user.id, text=f'game over')
        for i in range(9):
            maps[i]=i+1        
    if maps.count('X')<5 and win==0 and maps.count('O')<maps.count('X') :

        if (maps[0]=="X" and maps[1]=="X") or (maps[0]=="O" and maps[1]=="O"):
            b=3
        elif maps[0]=="X" and maps[2]=="X" or maps[0]=="O" and maps[2]=="O":
            b=2
        elif maps[1]=="X" and maps[2]=="X" or maps[1]=="O" and maps[2]=="O":
            b=1

        elif maps[3]=="X" and maps[4]=="X" or maps[3]=="O" and maps[4]=="O":
            b=6
        elif maps[3]=="X" and maps[5]=="X" or maps[3]=="O" and maps[5]=="O":
            b=5
        elif maps[4]=="X" and maps[5]=="X" or maps[4]=="O" and maps[5]=="O":
            b=4

        elif maps[6]=="X" and maps[7]=="X" or maps[6]=="O" and maps[7]=="O":
            b=9
        elif maps[6]=="X" and maps[8]=="X" or maps[6]=="O" and maps[8]=="O":
            b=8
        elif maps[8]=="X" and maps[7]=="X" or maps[8]=="O" and maps[7]=="O":
            b=7
        

        elif (maps[0]=="X" and maps[3]=="X") or (maps[0]=="O" and maps[3]=="O"):
            b=7
        elif maps[0]=="X" and maps[6]=="X" or maps[0]=="O" and maps[6]=="O":
            b=4
        elif maps[3]=="X" and maps[6]=="X" or maps[3]=="O" and maps[6]=="O":
            b=1

        elif maps[1]=="X" and maps[4]=="X" or maps[1]=="O" and maps[4]=="O":
            b=8
        elif maps[1]=="X" and maps[7]=="X" or maps[3]=="O" and maps[7]=="O":
            b=5
        elif maps[4]=="X" and maps[7]=="X" or maps[4]=="O" and maps[7]=="O":
            b=2

        elif maps[2]=="X" and maps[5]=="X" or maps[2]=="O" and maps[5]=="O":
            b=9
        elif maps[2]=="X" and maps[8]=="X" or maps[2]=="O" and maps[8]=="O":
            b=6
        elif maps[5]=="X" and maps[8]=="X" or maps[5]=="O" and maps[8]=="O":
            b=3


        elif maps[0]=="X" and maps[4]=="X" or maps[0]=="O" and maps[4]=="O":
            b=9
        elif maps[0]=="X" and maps[8]=="X" or maps[0]=="O" and maps[8]=="O":
            b=5
        elif maps[4]=="X" and maps[8]=="X" or maps[4]=="O" and maps[8]=="O":
            b=1

        elif maps[2]=="X" and maps[4]=="X" or maps[2]=="O" and maps[4]=="O":
            b=7
        elif maps[2]=="X" and maps[6]=="X" or maps[2]=="O" and maps[6]=="O":
            b=5
        elif maps[6]=="X" and maps[4]=="X" or maps[6]=="O" and maps[4]=="O":
            b=3


        elif maps.count('X')==2 and maps[0]!="O":
            b=1
        elif maps.count('X')==2 and maps[2]!="O":
            b=3
        elif maps.count('X')==2 and maps[6]!="O":
            b=7
        elif maps.count('X')==2 and maps[8]!="O":
            b=9

        elif maps.count('X')==1 and maps[4]!="O" :
            b=5
        else:
            b=randint(1,8)
        while maps[b-1]=='X'or maps[b-1]=='O':
            b=randint(1,8)
        maps[b-1]="O"
    
        
    if win!=1:
        for i in victories:
            if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
                bot.send_message(chat_id=msg.from_user.id, text=f'{maps[0]} {maps[1]} {maps[2]} \n{maps[3]} {maps[4]} {maps[5]} \n{maps[6]} {maps[7]} {maps[8]}')
                bot.send_message(chat_id=msg.from_user.id, text=f'ты выйграл')
                win=1
            if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O" and win==0:
                bot.send_message(chat_id=msg.from_user.id, text=f'{maps[0]} {maps[1]} {maps[2]} \n{maps[3]} {maps[4]} {maps[5]} \n{maps[6]} {maps[7]} {maps[8]}')
                bot.send_message(chat_id=msg.from_user.id, text=f'ты проиграл')
                win=1 
    if win!=1:
        bot.send_message(chat_id=msg.from_user.id, text=f'{maps[0]} {maps[1]} {maps[2]} \n{maps[3]} {maps[4]} {maps[5]} \n{maps[6]} {maps[7]} {maps[8]}')
        bot.send_message(chat_id=msg.from_user.id, text=f'ходи ')
    if win==1:
        for i in range(9):
            maps[i]=i+1
        win=0

bot.polling()