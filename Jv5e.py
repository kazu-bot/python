import random

hands = ['グー', 'チョキ', 'パー']
results = {'win': '勝ち', 'lose': '負け', 'draw': 'あいこ'}


def start_message():
    print('じゃんけんスタート')


def get_my_hand():
    print('自分の手を入力してください')
    out_message = ''  # 出力メッセージ初期化
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
    return result


def get_hand_name(hand_number):
    return hands[hand_number]


def view_hand(my_hand, you_hand):
    print('あなたの手は ' + get_hand_name(my_hand))
    print('相手の手は ' + get_hand_name(you_hand))


def view_result(result):
    print(results[result])


def play():
    my_hand = get_my_hand()
    you_hand = get_you_hand()

    view_hand(my_hand, you_hand)
    hand_diff = my_hand - you_hand
    result = get_result(hand_diff)

    view_result(result)
    return result


# Main
start_message()

judge = play()
cnt = 0
# あいこである限りループ
while judge == 'draw':
    cnt = cnt + 1
    print('あいこの回数：' + str(cnt) + '回。')
    judge = play()
