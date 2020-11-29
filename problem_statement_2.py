#Python 3 code

breads, vada, samosa = map(int, input().split())
vadapav_cost, somasapav_cost = map(int, input().split())

def max_profit(breads, vada, samosa, vadapav_cost, somasapav_cost):
    vadapav_num = 0
    somasapav_num = 0
    if vadapav_cost > somasapav_cost:
        if breads >= 2*vada:
            vadapav_num = vada
            breads = breads - 2*vadapav_num
        else:
            vadapav_num = int(breads/2)
            breads = breads % 2
        if breads >= 2*samosa:
            somasapav_num = samosa
            breads = breads - 2*somasapav_num
        else:
            somasapav_num = int(breads/2)
            breads = breads % 2
    else:
        if breads >= 2*samosa:
            somasapav_num = samosa
            breads = breads - 2*somasapav_num
        else:
            somasapav_num = int(breads/2)
            breads = breads % 2
        if breads >= 2*vada:
            vadapav_num = vada
            breads = breads - 2*vadapav_num
        else:
            vadapav_num = int(breads/2)
            breads = breads % 2

    return (vadapav_num * vadapav_cost) + (somasapav_num * somasapav_cost)


print(max_profit(breads, vada, samosa, vadapav_cost, somasapav_cost))
