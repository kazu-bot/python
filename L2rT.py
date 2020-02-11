import random

hands = ['グー', 'チョキ', 'パー']
results = {'win':'勝ち', 'lose':'負け', 'draw':'あいこ'}

def start_message():
    print('じゃんけんスタート')

def get_my_hand():
    print('自分の手を入力してください')
    out_message = '' #出力メッセージ初期化
    cnt = 0
    # list件数分ループ。oneHandに１件ずつ積む
    for oneHand in hands:
        out_message = out_message + str(cnt) + ':' + oneHand
        if cnt < 2:
            out_message = out_message + ', '
        cnt = cnt + 1
    return int(input(out_message))

def get_you_hand():
    return random.randint(0, 2)

def get_result(hand_diff):
    if hand_diff == 0:
        result = 'draw'
    elif hand_diff == -1 or hand_diff == 2:
        result = 'win'
    else:
        result = 'lose'

def view_result(result):
    print(results(result))


def get_hand_name(hand_number):
    return hands[hand_number]


def view_hand(my_hand_name, you_hand_name):
    print('あなたの手は ' + my_hand_name)
    print('相手の手は ' + you_hand_name)


start_message()
my_hand = get_my_hand()
my_hand_name = get_hand_name(my_hand)

you_hand = get_you_hand()
you_hand_name = get_hand_name(you_hand)

view_hand(my_hand_name, you_hand_name)
hand_diff = my_hand - you_hand
view_result(get_result(hand_diff))
