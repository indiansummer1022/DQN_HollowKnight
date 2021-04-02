from Tool.WindowsAPI import key_check
import time


# check whether a game is end
def is_end(next_self_blood, min_hp, next_boss_blood, boss_blood):
    if next_self_blood ==9 and min_hp <= 3:    
        return True
    elif next_boss_blood - boss_blood > 200:   
        return True
    return False

# get mean score of a reward seq
def mean(d):
    t = 0
    for i in d:
        t += i
    return t / len(d)

# count play hp change, and give reward 
def count_self_reward(next_self_blood, self_hp):
    if next_self_blood - self_hp < 0:
        return 11 * (next_self_blood - self_hp)
    return 0

# count boss hp change, and give reward 
def count_boss_reward(next_boss_blood, boss_blood):
    if next_boss_blood -  boss_blood < 0:
        return int((boss_blood - next_boss_blood)/9)
    return 0

# JUDGEMENT FUNCTION, write yourself
def action_judge(boss_blood, next_boss_blood, self_blood, next_self_blood):
    # get action reward
    # Player dead
    if next_self_blood <= 0:    
        print("Player dead.")
        reward = -11
        done = 1
        
        return reward, done
    #boss dead
    elif next_boss_blood <= 0 or next_boss_blood > 900:   

        reward = 20
        done = 2
        print("Boss dead.")
        return reward, done
    # playing
    else:
        self_blood_reward = count_self_reward(next_self_blood, self_blood)
        boss_blood_reward = count_boss_reward(next_boss_blood, boss_blood)
        reward = self_blood_reward + boss_blood_reward
        done = 0
        return reward, done

# Paused training
def pause_game(paused):
    op, d = key_check()
    if 'T' in op:
        if paused:
            paused = False
            print('start game')
            time.sleep(1)
        else:
            paused = True
            print('pause game')
            time.sleep(1)
    if paused:
        print('paused')
        while True:
            op, d = key_check()
            # pauses game and can get annoying.
            if 'T' in op:
                if paused:
                    paused = False
                    print('start game')
                    time.sleep(1)
                    break
                else:
                    paused = True
                    time.sleep(1)
    return paused