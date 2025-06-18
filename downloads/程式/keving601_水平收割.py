def turn(n):
    for _ in range(n):
        turn_left()

def new_move(n):
    for _ in range(n):
        move()

def harvest_one_cell():
    while object_here():
        take()

# 起始移動（根據你的田地調整）
turn_left()
new_move(2)
turn(3)
new_move(2)

# 之字形收割（6排，每排6格）
for row in range(6):
    for i in range(6):
        harvest_one_cell()
        if i != 5:
            move()
    if row != 5:  # 最後一排不轉彎
        if row % 2 == 0:  # 偶數排往東
            turn_left()
            move()
            turn_left()
        else:             # 奇數排往西
            turn(3)
            move()
            turn(3)