import random

def start_message():
  print('じゃんけんスタート')

def get_my_hand():
  print('自分の手を入力してください')
  return int(input('0:グー, 1:チョキ, 2:パー'))

def get_you_hand():
  return random.randint(0, 2)

def view_result(hand_diff):
  if hand_diff == 0:
    print('あいこ')
  elif hand_diff == -1 or hand_diff == 2:
    print('勝ち')
  else:
    print('負け')

def get_hand_name(hand_number):
    hands = ['グー','チョキ','パー']
    if hand_number == 0:
        return hands[0]
    elif hand_number == 1:
        return hands[1]
    else:
        return hands[2]
def view_hand(my_hand_name,you_hand_name):
    print('あなたの手は ' + my_hand_name)
    print('相手の手は ' + you_hand_name)


start_message()
my_hand = get_my_hand()
my_hand_name = get_hand_name(my_hand)

you_hand = get_you_hand()
you_hand_name = get_hand_name(you_hand)

view_hand(my_hand_name,you_hand_name)
hand_diff = my_hand - you_hand
view_result(hand_diff)