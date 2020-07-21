# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    ten_coins = money // 10
    five_coins = (money % 10)//5
    one_coins = ((money % 10) % 5) // 1
    return ten_coins + five_coins + one_coins


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
