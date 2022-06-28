import random

def randomEvent(DefRandomValue):

    asked = 0
    while(asked < 20):
        userinput = input("수를 입력하세요. ({}/{})  >> ".format(asked + 1, 20))
        asked += 1
        userinput2int = int(userinput)
        if (userinput2int == DefRandomValue):
            print("\n입력 값과 설정 값이 일치합니다!")
            break
        elif (userinput2int > DefRandomValue):
            print("\n입력 된 값은 설정된 값보다 큽니다!")
        elif (userinput2int < DefRandomValue):
            print("\n입력 된 값은 설정된 값보다 작습니다!")
        else:
            print("\n알 수 없는 오류가 발생했습니다.")

    print("\n질문이 종료되었습니다!")

randomValue = ("{}".format(random.randint(0, 100)))
randomEvent(int(randomValue))