import random

asked = 0

print("\n=====[  UP & DOWN GAME  ]=====\n")
DefRandomValue = random.randint(1, 100)

while (asked < 20):
    userinput = input("수를 입력하세요. ({}번째 시도)  >> ".format(asked + 1))
    asked += 1
    userinput2int = int(userinput)
    if (userinput2int == DefRandomValue):
        print("\n일치합니다!")
        break
    elif (userinput2int > DefRandomValue):
        print("\n입력 된 값이 더 큽니다!")
    elif (userinput2int < DefRandomValue):
        print("\n입력 된 값이 더 적습니다!")

print("질문이 종료되었습니다! | 답 : {} | 시도 횟수 : {}".format(DefRandomValue, asked + 1))