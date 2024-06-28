import random

random_number = random.randint(0,2)

RPS = ['가위', '바위', '보']

record = [0, 0, 0]        #승, 패, 무

while True:
    user = input('가위, 바위, 보 중 하나를 선택하세요: ')
    if(user == '가위'): user_RPS = 0
    if(user == '바위'): user_RPS = 1
    if(user == '보'): user_RPS = 2

    if(user in RPS):
        print(f'사용자: {user}, 컴퓨터: {RPS[random_number]}')
        if(user_RPS == random_number):
            print('무승부!')
            record[2] += 1
        elif(user_RPS > random_number):
            if((user_RPS-random_number) % 2 == 1):
                print('사용자 승리!')
                record[0] += 1
            else:
                print('컴퓨터 승리!')
                record[1] += 1
        elif (user_RPS < random_number):
            if ((user_RPS-random_number) % 2 == 0):
                print('사용자 승리!')
                record[0] += 1
            else:
                print('컴퓨터 승리!')
                record[1] += 1
        regame = input('다시 하겠습니까? (y/n): ')
        if(regame.lower() == 'y'):
            random_number = random.randint(0, 2)
        else:
            print('게임을 종료합니다')
            print(f'승: {record[0]} 패: {record[1]} 무승부: {record[2]}')
            break
    else:
        print('유효한 입력이 아닙니다.')