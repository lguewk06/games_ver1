import random

random_number = random.randint(1, 100)
count = 0
record = 0

while True:
    user = input('숫자를 입력하세요: ')
    if(user.isdigit()):
        user = int(user)
        print(random_number)

        if user < random_number:
            print('업')
            count += 1

        elif user > random_number:
            print('다운')
            count += 1

        else:
            print('정답입니다!!')
            count += 1
            print(f'시도한 횟수: {count}')

            regame = input('다시하시겠습니까? (y/n)')
            if regame == 'y':
                if record < count or record == 0:
                    record = count
                if record > 0:
                    print(f'이전 게임 플레이어 최고 시도 횟수: {record}')
                random_number = random.randint(1, 100)
                count = 0
            else:
                break

    else:
        print('#####숫자가 아닙니다. 숫자만 입력해주세요#####')
