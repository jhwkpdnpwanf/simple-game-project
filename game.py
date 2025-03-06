from random import *
import time

def start_message():

    print(" -----------------------------------------------")
    print("|                        _               _      |")
    print("|     _____      ____   | |   ________  | |     | ")                     
    print("|    |  ___|    |  __| _| |  |__    __| | |     | ")                                        
    print("|    | |___     | |   |_  |     |  |    | |     | ")                                
    print("|    |_____|    | |__   | |    / /! |   | |     | ")                                     
    print("|   _________   |____|  | |   / /  ! !  | |     |")
    print("|  |___   ___|          |_|  /_/    !_} | |     |")                                          
    print("|      |_|                              |_|     |")
    print("|                                               |")
    print("|                                               |")
    print("|             마을에 떨어지다!!                 |")
    print(" -----------------------------------------------")



# 미니게임 두더지잡기 함수 
def draw():
    a = []
    a.append("           |") #0
    a.append("    ___    |") #1
    a.append("   |.. |   |") #2
    a.append("   |<  |   |") #3
    a.append(" -----------") #4
    
    return a

def make_mole():
    mole = []
    mole_num = randint(0,8)
    mole.append(mole_num)
    
    mole_num = randint(8,15)
    while (mole_num > 0):
        r = randint(8,24)
        mole_len = len(mole)
        if (r > mole[mole_len - 1]):   # 무조건 더 큰값이 나오게함 
            mole.append(r)
        mole_num = mole_num - 1

    return mole

def print_mole(row, mole):
    print(draw()[4], draw()[4], draw()[4], draw()[4], draw()[4])
    a = [0, 0, 0, 0, 0]
    t = []
    for i in mole:
        if (i // 5 == row): # 두더지가 존재하는 위치의 행을 구함
            j = i % 5 # 두더지가 존재하는 위치의 열을 구함
            a[j] = 1 # 두더지가 존재하면 +1
            t.append(j) # t 리스트에 추가
            
    for k in range(3):
        print("|", draw()[a[0]], draw()[a[1]], draw()[a[2]], draw()[a[3]], draw()[a[4]]) # 두더지가 존재하는 
        for l in t:
            a[l] = a[l] + 1 # 두더지가 존재하는 위치에만 두더지를 그림


def make_grid():
    mole = make_mole()
    result = mole

    print_mole(0, mole)
    print_mole(1, mole)
    print_mole(2, mole)
    print_mole(3, mole)
    print_mole(4, mole)
    print(draw()[4], draw()[4], draw()[4], draw()[4], draw()[4])

    return mole


           
"""
 ----------------------------------------------------------- 
   

    



 ----------------------------------------------------------- 
"""
#========================================================
# 그림 그리기
#========================================================
def pic_mole():
    print("               ,_______,")
    print("             ,~~~~~~~~---, ")
    print("            ,~~~~~~~~~~~--,")
    print("            ,~~~^ ~~~^ ~~~-,")
    print("            ,~~~~___~~~~~~~,")
    print("            ,~~~|___|~~~~~~,")   
    print("            ,~~~~~~~~~~~~~~,") 
    print("            ,~~~~~~~~~~~~~~,") 
    print("            ,~~~~~~~~~~~~~~,")  
    print("            ,~~~~~~~~~~~~~~,")
    print("         ,==~~~~~~~~~~~~~~~==,")
    print("        ,=====================,")
    print("        ,=====================,")

def pic_moleking():
    print("                 ^^^^^")
    print("                |-0-0-| ")
    print("                |0-0-0| ")
    print("               ,_______,")
    print("             ,~~~~~~~~---, ")
    print("            ,~~~~~~~~~~~--,")
    print("            ,~~~^ ~~~^ ~~~-,")
    print("            ,~~~~___~~~~~~~,")
    print("            ,~~~|___|~~~~~~,")   
    print("            ,~~~~~~~~~~~~~~,") 
    print("            ,~~~~~~~~~~~~~~,") 
    print("            ,~~~~~~~~~~~~~~,")  
    print("            ,~~~~~~~~~~~~~~,")
    print("         ,==~~~~~~~~~~~~~~~==,")
    print("        ,=====================,")
    print("        ,=====================,")

def pic_falldownMe():
    print("                 _")
    print("              / ]")
    print("              (_)----         _")
    print("                 --  |       ( )")
    print("                   | |      / /")
    print("                  ^   z-__-  /")
    print("                 /_______   ,")
    print("              ,_-         /")
    print("             ___        }")
    print("       ___, /. .}     /")
    print("      o___, ( o |   )")
    print("                 / /")
    print("                /_/")
    print("                 o")


def pic_tiredMe():
    print("              ___ ")
    print("             /. .}     ")
    print("           __{ o )  ")
    print("          /    -    ")
    print("         /     | ")
    print("        /    | | ")
    print("       <     |_| ")
    print("       <   _/    ")
    print("        | |  ) ) ")
    print("        ) )  | | ")
    print("       / /  / / ")
    print("      /_/  /_/ ")

def pic_me(n):
    a = []
    a.append("        _______    ____")
    a.append("      ,/       ]  | ?? |") #1
    a.append("      1-----___]  |_ __|") #2
    a.append("       { =   = }    V") #3
    a.append("       (_  -  )   _o") #4
    a.append("        _|   |___/ /")
    a.append("       /      ____/")
    a.append("      / /     ]")
    a.append("     / /|     |")

    if(n == 1):
        a[1] = ("      ,/       ]  | .. |") #1
        a[2] = ("      1-----___]  |_ __|") #2
        a[3] = ("       { .   . }    V") #3
        a[4] = ("       (_  -  )   _o") #4
        
    if(n == 2): # 안좋음
        a[1] = ("      ,/       ]  | :( |") #1
        a[2] = ("      1-----___]  |_ __|") #2
        a[3] = ("       { .   . }    V") #3
        a[4] = ("       (_  n  )   _o") #4
        
    if(n == 3): # 기분좋음 
        a[1] = ("      ,/       ]  | :) |") #1
        a[2] = ("      1-----___]  |_ __|") #2
        a[3] = ("       { .   . }    V") #3
        a[4] = ("       (_  v  )   _o") #4

    for i in range(len(a)):
        print(a[i])

        
#========================================================
# 대화박스 
#========================================================       
              
def box(dialogue):
    print(" ------------------------------------------------")
    print("  ",dialogue)
    print(" ------------------------------------------------")
    print()
    input()

def box_noInput(dialogue):
    print(" ------------------------------------------------")
    print("  ",dialogue)
    print(" ------------------------------------------------")
    print()

#========================================================
# 게임 인트로
#========================================================
def intro():
    box("세상에는 지구를 제외하고 수많은 세계관이 존재한다.")

    box("한 세계에 존재하면서.. \n   다른 세계에 존재하고 싶어하는 자들에게")

    box("그들에게 왕은 다른 세계로의 모험을 허락한다.")

    box("그러나 의도치 않은 실수로 인해 \n   다른 세계로 떨어지게 되는 사건도 종종 발생하였으니.. ")

    box("...")
    
    
    pic_mole()
    box("내 이름은 두더지")
    
    box("이 두더지 마을에 살고 있는\n   평범한 두더지이다")

    box("매년 두더지 마을의 식량을 책임져주는\n   인간들이 소환됐었는데..\n   올해는 어째서인지 아무도 오질 않는다..")

    box("왕님께 듣기론 다른 세계에 관심이 많은 자들 중\n   이맘때 쯤 소환된다고 했는데 ..")

    box("올해는 언제쯤 나타.. ")

    box("펑!!!")
    
    pic_falldownMe()
    box("???")
    
    pic_mole()
    box("??? ")
    box("뭐야 정말 소환되었잖아?")
    pic_tiredMe()
    box("여긴 어디지 ...?")

    pic_mole()
    box("안녕하세요!! ")
    pic_me(0)
    box("..? 두더지가 말을 하잖아 ..")

    pic_mole()
    box("저.. 저희 마을의 식량문제를 위해 오신건가요 ..?")
    box("맞으시다면 ..\n   저희 마을을 위해 지렁이 백마리만 구해다 주세요!!")

    pic_me(1)
    box("......")
    box("아닌데.. ")
    box("난 그냥 집에서 자고 있었는데 ..")
    pic_me(2)
    box("머야 나 돌려보내줘 ㅜㅜ ")
    box("그래도.. 도와주면 재밌는 일들이 많이 생길거같은데\n   조금은 도와줘볼까?")
    # 탈출할지 조건을 받아줄지 선택 



#========================================================
# 스토리1 (조건을 받아줌)
#========================================================

#=================================
# 1번 지렁이 찾기 게임
#=================================
def miniGameStory_one():
    pic_mole()
    box_noInput("게임을 그만하고 싶으면 quit을 입력해주세요!\n   100마리를 다 모았으면 quit을 치고 나오면 돼요!")
    print()
    print()
    box_noInput("지렁이 찾기 게임은 조금 머리를 써야돼요!")
    q = input()
    if (q == "quit"):
        return q
    
    box_noInput("다섯개의 칸에 지렁이가 있는 곳이 있어요!")
    q = input()
    if (q == "quit"):
        return q
    
    box_noInput("지렁이가 있는 칸의 번호를 하나씩 쓰면 돼요!\n   첫칸부터 순서대로, 1 2 3 4 5 번째 칸이에요!")
    q = input()
    if (q == "quit"):
        return q

    box_noInput("그럼 열심히 지렁이를 모아주세요!")
    q = input()
    if (q == "quit"):
        return q
    
def worm_draw():
    a = []
    a.append("           |") #0
    a.append("   ____    |") #1
    a.append("  ['_  |   |") #2
    a.append("     | |_  |") #3
    a.append("     |___| |") #4
    a.append(" -----------") #5
    return a

#1. 지렁이 찾기 게임 
def miniGamePlay_one():
    worm = 0 # 추가할지렁이 수
    
    qq = miniGameStory_one()
    if(qq == "quit"):
        return worm
    
    box_noInput("시작")
    q = input()
    if (q == "quit"):
        return worm
    
    while(q != "quit"):
        a = []
        random_worm = randint(0,4)
        a.append(random_worm)
        
        if (random_worm != 4): # 4가 아니라면
            two = randint(0,2)
            if (two == 0): # 1/3 확률로 지렁이가 2개 나옴
                random_wormPlus = randint(random_worm + 1,4)
                a.append(random_wormPlus)
        t = [0,0,0,0,0]
        for i in a:
            t[i] = 1 # 지렁이가 있는 곳을 1로 만들어줌
            
        print(worm_draw()[5], worm_draw()[5], worm_draw()[5], worm_draw()[5], worm_draw()[5])
        for j in range(4): # 0이 아닐때만 +1
            print("|", worm_draw()[t[0]], worm_draw()[t[1]], worm_draw()[t[2]], worm_draw()[t[3]], worm_draw()[t[4]])
            for k in range(5):
                if (t[k] != 0):
                    t[k] = t[k] + 1
        print(worm_draw()[5], worm_draw()[5], worm_draw()[5], worm_draw()[5], worm_draw()[5])
        print() # 지렁이 위치를 다 그림


        for i in range(len(a)): # 지렁이 개수만큼 반복
            q = input()
            
            if (q == "quit"):
                return worm
            m = 0
            for idx, i in enumerate(a):
                 # 정답인지 기억
                if (q == str(i+1)): 
                    m = 1
                    a[idx] = -1 # 0으로 바꿨을때 특정 상황에서 버그 발생 -> -1로 바꿈
                    worm = worm + 1 # 지렁이 개수 추가
                    print("정답! 이번 게임에서 얻은 지렁이 수: ", worm)
            if (m == 0):
                print("땡! 이번 게임에서 얻은 지렁이 수: ", worm)
                    
    
#=================================
# 2번 지렁이 땅파기 게임
#=================================
def miniGameStory_two():
    pic_mole()
    box_noInput("게임을 그만하고 싶으면 quit을 입력해주세요!\n   100마리를 다 모았으면 quit을 치고 나오면 돼요!")
    print()
    print()
    box_noInput("지렁이 땅파기 게임은 아주 간단해요!")
    q = input()
    if (q == "quit"):
        return q
    
    box_noInput("그냥 엔터키를 마구마구 누르면 돼요!\n   (아주 적은 확률로 지렁이 두마리를 발견할지도 ..)")
    q = input()
    if (q == "quit"):
        return q

    box_noInput("그럼 열심히 지렁이를 모아주세요!")
    q = input()
    if (q == "quit"):
        return q


# 지렁이 땅파기 미니게임 
def miniGamePlay_two():
    worm = 0 # 지렁이 수

    qq = miniGameStory_two()
    if(qq == "quit"):
        return worm

    box_noInput("시작")
    q = input()
    if (q == "quit"):
        return worm
    
    i = 0 # 땅 판 횟수
    print("땅을 판 횟수: ", i)
    
    while(True):
        q = input()
        if (q == "quit"):
            return worm
        i = i + 1
        print("땅을 판 횟수: ", i)
        if (i % 10 == 0): # 10번째마다 +1
            worm = worm + 1
            print("지렁이 발견! 현재 지렁이 수: ", worm)
            
            
        w = randint(1,100) # 1퍼센트 확률로 지렁이 두마리 발견
        if(w == 1):
            worm = worm + 2
            print("지렁이 두마리 발견!!! 현재 지렁이 수: ", worm)
    
#=================================
# 3번 지렁이 도박 게임 
#=================================
def miniGameStory_three():
    pic_mole()
    box_noInput("게임을 그만하고 싶으면 quit을 입력해주세요!\n   100마리를 다 모았으면 quit을 치고 나오면 돼요!")
    print()
    print()
    box_noInput("지렁이 홀짝 도박 게임은 조금 위험하긴한데 ..")
    q = input()
    if (q == "quit"):
        return q
    
    box_noInput("먼저 지렁이를 베팅하고 ..\n   홀수와 짝수 중 하나를 고르면 돼요!")
    q = input()
    if (q == "quit"):
        return q
    
    box_noInput("정답을 맞추면 베팅한 지렁이만큼\n   지렁이를 얻을 수 있어요 ..")
    q = input()
    if (q == "quit"):
        return q
    box_noInput("그치만 정답을 맞추지 못하면 베팅한 지렁이를\n   전부 잃어버리니 조심해주세요 ..")
    q = input()
    if (q == "quit"):
        return q
    
    box_noInput("그럼 열심히 지렁이를 모아주세요!")
    q = input()
    if (q == "quit"):
        return q
    
# 지렁이 홀짝 도박 게임실행 
def miniGamePlay_three(now_worm): # 가지고 있던 지렁이로 도박을 함

    qq = miniGameStory_three()
    if(qq == "quit"):
        return now_worm

    box_noInput("시작")
    q = input()
    if (q == "quit"):
        return now_worm
    
    while (True):
        if (now_worm <= 0):
            print("게임에 참여하려면 지렁이가 최소 하나는 있어야해 !")
            print("지렁이를 모아서 다시 도전해줘!")
            print()
            return now_worm
        

        
        while (True):
            
            print("현재 지렁이 수 : ", now_worm)
            betting_worm = input("베팅할 지렁이 수: ")
            while(True): # 숫자가 아닌값 방지
                if (betting_worm == "quit"):
                    return now_worm
                print()

                ck = [] # 숫자가 아니면 되돌리기 
                for c in range(1, now_worm+1):
                    ck.append(str(c))
                    
                if betting_worm in ck: # 사용가능한 값인지 확인
                    betting_worm = int(betting_worm)
                    break
                else:
                    print("  숫자를 입력해줘!")
                    print("현재 지렁이 수 : ", now_worm)
                    betting_worm = input("베팅할 지렁이 수: ")
                
                    
            if (betting_worm > now_worm):
                print("가지고 있는 지렁이 보다 많으면 안돼 !")
                print("다시 선택해줘")
            else:
                break
            
        while (True):
            print("홀수와 짝수 중 하나를 고르시오")
            print("  1. 홀수")
            print("  2. 짝수")

            select = input()
            if (select == "quit"):
                return now_worm
            if (select != '1' and select != '2'):
                print("1번과 2 번중 다시 골라줘")
            else:
                break
        
        num = randint(1,100)
        print()
        if (num % 2 == 0): # 짝수
            if (select == '1'):
                print(num, "은 짝수였어 .. 오답이야")
                now_worm = now_worm - betting_worm
            else:
                print(num, "은 짝수!! 정답이야")
                now_worm = now_worm + betting_worm
        else: # 홀수
            if (select == '1'):
                print(num, "은 홀수!! 정답이야")
                now_worm = now_worm + betting_worm
            else:
                print(num, "은 홀수였어 .. 오답이야")
                now_worm = now_worm - betting_worm
                
        print()
        print("한판 더 할래?")
        print("하고 싶으면 엔터키를 눌러줘! (quit을 쳐서 나가기)")
        print()
        q = input()
        if (q == "quit"):
            return now_worm

#=================================
# 4번 선택지 도망가기
#=================================
def miniGameStory_run():
    while(True):
        print()
        print(" ------------------------------------------------")
        print("  모은 지렁이가 전부 초기화되고, 되돌릴 수 없어.")
        print("  그래도 정말 도망갈 거야?")
        print()
        print()
        
        print("  1. 응. 도망갈래.. 여긴 너무 힘들어.")
        print("  2. 아니야.. 조금 더 노력해서 지렁이를 모아볼게!")
        print(" ------------------------------------------------")

        run = input()
                
        if (run == '1'):
            a = "Go Story two"
            return a
                
        elif (run == '2'):
            print("  잘 생각했어! 조금 더 노력해보자!")
            return 
            
        else:
            print("  다시 입력해줘!")

#========================================================
# 스토리 1 메인 
#========================================================
def story1_board(worm, n):
    if (n == 0):
        print(" ------------------------------------------------")
        print("  지렁이 백마리를 구해라!")
        print("                              현재 지렁이: ", worm)
        print("  1. 지렁이 줍기")
        print("  2. 지렁이 땅파기")
        print("  3. 지렁이 홀짝 도박")
        print("  4. 도망가기")
        print(" ------------------------------------------------")
        print()
        print()
    else:
        print(" ------------------------------------------------")
        print("  지렁이 백마리를 구해라!")
        print("                              현재 지렁이: ", worm)
        print("  1. 지렁이 줍기")
        print("  2. 지렁이 땅파기")
        print("  3. 지렁이 홀짝 도박")
        print(" ------------------------------------------------")
        print()
        print()
        
def story1(n):
    if (n == 0): # 수락을 받아준경우
        pic_mole()
        box("역시 수락해주실 줄 알았어요!!")
        box("지렁이 백마리만 구해다 주시면\n   원래 세계로 돌아가실 수 있도록 왕님께 데려다 드릴게요!")
        print()

    if (n == 1):
        print()
        print()
        pic_mole()
        box("그러게 도망을 쳐버리시면 어떡해요 ㅜㅜ")
        box("얼른 지렁이 백마리만 구해다 주시고\n   원래 세계로 돌아갑시다!")
        
    worm = 0 # 지렁이
    
    while(worm < 100):
        story1_board(worm, n)
        
        a = input()
        print(a)
        if (a == '1'):
            worm = worm + miniGamePlay_one()
            
        elif (a == '2'):
            worm = worm + miniGamePlay_two()
            
        elif (a == '3'):
            worm = miniGamePlay_three(worm)
            
        elif (a == '4' and n == 0):    
            a = miniGameStory_run()
            if (a == "Go Story two"):
                return a

        else:
            print("  다시 입력해줘!")



#========================================================
# 스토리 2 (도망가기)
#========================================================
def go_city():
    pic_me(1)
    box("...")
    box("중앙마을 가는길")
    box("...")
    box("후.. 내가 어쩌다가 이런 곳에 떨어졌을까..")
    box("그래도 왕에게 가면 원래 세계로 돌아갈 수 있겠지?")
    box("어? 저기가 왕국인가..?")
    box("얼른 가야겠..")

    pic_mole()
    box("찾았다!! 저기있다!!")

    pic_me(2)
    box("!!!")
    box("으어어 빨리 도망가야겠다!")

    box("도와주는 두더지를 강도로 착각한 당신\n   두더지를 피해서 왕이 있는 곳까지 달려가라!")
    box("각 칸은 0부터 24까지이다!\n   두더지가 있는 위치를 전부 입력하라!\n   실패할수록 남은 횟수가 늘어나!")
    
    count = 10
    fail = 0

    print("  남은 횟수: %d" %count)
    while(count > 0):
        m = make_grid()
        m_len = len(m)
        
        num_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']


        for i in range(m_len):
            while True:
                print("=*0 ~ 24 숫자로만 입력해줘!!*=")
                num = input("두더지가 있는 위치: ")
                if num in num_set:
                    num = int(num)
                    break

            if num in m:
                count = count - 1
                print("성공이야! 남은 횟수: %d" %count)
                m.remove(num)
            else:
                count = count + 1
                print("실패야.. 남은 횟수: %d" %count)
                
            print()
            if (count == 0):
                return




def go_town():
    pic_tiredMe()
    box("여기 왜 이렇게 넓은거야 ..")
    box("하루종일 걷다보니 너무 힘들...")
    
    pic_falldownMe()
    box("으악 !!")
    box("이런 곳에서 넘어지..")
    
    pic_mole()
    box("뭐야 이런 외진곳에 인간이??\n   잡으면 지렁이를 많이 들고있겠지???\n   잡아라!!!")

    pic_tiredMe()
    box("외곽으로 오는게 아니였는데 ..")
    box("저 강도 두더지들을 피해서 다시 돌아가야겠어!!")
    
    box("강도 두더지들을 피해가며\n   중앙마을 쪽으로 도망가라!\n\n   enter키를 마구 눌러서 도망가자!")

    i = 0
    print("enter키를 눌러주세요")    
    while(True):
        input()
        i = i + 1
        print("도망 %d! " %i)
        if (i == 10):
            print("조금 더 힘내서 달려봐!")
        if (i ==25):
            print("거의 다 따돌렸어!!")
        if (i ==40):
            print("성공!!")
            break
        
    pic_tiredMe()
    box("후.. 힘들었다. 진작에 중앙마을로 갈걸")
    box("다시 열심히 가봐야겠다.")
    
def story2():
    pic_mole()
    box("뭐야 인간이 어디갔지?")
    box("왕에게 가는 길엔 강도 두더지들이 많을텐데 .. \n   무사히 잘 도착할 수 있으려나?")
    box("얼른 도와주러 가야겠다!")
    
    pic_tiredMe()
    box("헉... 어디로 도망가야되지 .. ")
    box("그래.. 아까 중앙마을에 왕이 있다고 했던거 같아..!")
    box("근데 마을 외곽으로 도망가는게 나으려나?")
    box("음 .. 어디로 가지?")

    box_noInput("왕에게 찾아가려는 당신, 당신의 목적지는?\n   1. 중앙마을로 간다.\n   2. 외곽으로 빠진다.")
    num = input()
    while (True):
        if (num == '1'):
            fail = go_city()
            break
        elif(num == '2'):
            go_town()
            num = '1'
        else:
            print("1번과 2번중 골라주세요")
            box_noInput("당신의 선택은?\n   1. 중앙마을로 간다.\n   2. 외곽으로 빠진다.")
            num = input()

    pic_tiredMe()
    box("후.. 드디어 다 왔다 !!")
    box("두더지 왕님.. 안녕하세요 전 인간마을에서 온..")

    print()
    box("그렇게 난 수십 분 동안\n   이때까지 있었던 일들을 전부 말해줬다.")
    
    pic_moleking()
    box("크흠.. 그런 일이..")
    box("내 소환 의식 때 큰 실수가 있었나봅세..\n   미안하오")
    box("그런데.. 자네를 돌려보내기 위해서\n   지렁이 100마리가 필요하오")
    box("지렁이 100마리만 구해오면 다시 돌려보내 주겠네")

    pic_me(1)
    box("...")
    pic_me(0)
    box("아니 그럼 내가 왜 굳이 이 고생ㅇ@$%#&!!!")
    box("... 가져다 드릴게요.. 조금만 기다려봐요")
    box("...")
    
def story1_end():
    print("지렁이 100마리를 다 구했습니다!")
    print("왕에게 전달하러 갑니다.")
    print()
    box("...")
    
    pic_moleking()
    box("왔는가 허허. 고생많았네")
    box("정말 지렁이 백마리를 전부 구했구만.")
    box("이제 집으로 돌아가게 해주마.")
    box("!@##@$@#@#!!")
    box("펑!!!!!")
    
def ending():
    pic_falldownMe()
    box("으어.. 이건 정말 적응이 안되네")
    pic_me(1)
    box("...")
    
    pic_me(3)
    box("돌아왔다.. \n   돌아왔어 !!!!!")
    box("너무 힘든 날들이였어.. 마치 꿈을 꾼 것만 같은 ..")
    box("... ")
    box("꿈인가?")
    box("어? 무슨 일들이 있었지?")
    box("........")
    box("아무 기억도 없는데 왜 이렇게 몸이 뻐근하지?")
    box("... (주머니에 손을 슥 넣는다)")

    print("      ____    ") 
    print("     ['_  |   ") 
    print("        | |_  ")
    print("        |___| ")
    
    box("으어 뭐야 !! 이게 왜 내 주머니 속에 ..")
    box("...?")
    
    

#====================================================
# 시작
#====================================================
if __name__ == "__main__":
    start_message()
    print("전체 화면에서 모험을 더 잘 즐길 수 있어요!")
    print("**화면이 깨질시엔 화면을 키우거나 글자크기를 줄여주세요**")
    print()
    print("시작을 원하시면 엔터키를 눌러주세요!")
    input()

    intro()

  
    while(True):
        print(" --------------------------------------")
        print("  당신의 선택은? ")
        print("  1. 조건을 수락한다")
        print("  2. 도망간다")
        print(" --------------------------------------")

        a = input()
        if (a != '1' and a != '2'):
            print("다시 입력해주세요")

            
        if (a == '1'):
            checkGoStoryTwo = story1(0)
            if (checkGoStoryTwo == "Go Story two"):
                a = '2'
            else:
                break
                
        if (a == '2'): # 도망
            story2()
            break
                

    while True:
        if (a == '1'):
            story1_end()
            break
        
        if (a == '2'): # 도망가서 왕을 만남
            story1(1)
            story1_end()
            break


    ending()
    start_message()
    print("지금까지 두더지마을에 떨어지다! 였습니다.")
    print("감사합니다!")


