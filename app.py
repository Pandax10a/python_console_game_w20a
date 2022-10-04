
import mariadb
import dbhelpers as dh


def check_skill_list():
   
    the_skill_list = dh.run_statement("CALL skill_selection_list")
   
    return the_skill_list

skill_list = check_skill_list()

# sign up on positive path
def signing_up():
    print('You are are almost ready to play!!')
    temp_user_storage = []
    try:
        while True:
            username_input = input('enter username: ')
            password_input = input('enter a password: ')
            if(len(username_input) > 4 and len(password_input)) > 4:
                temp_user_storage.append(username_input)
                temp_user_storage.append(password_input)
                return temp_user_storage
            else:
                print('type a longer username or password.  both needs to min 5 char long')
    except:
        print('user and pw something went wrong')


# use this for log in, will return tuple inside an array
def find_client_id(user_info=[]):
    
    result = dh.run_statement('CALL checking_credentials(?,?)', [user_info[0], user_info[1]])
    
    return result


# aa = find_client_id('test user 9', 'ii999')
# print(aa)

# calling stored procedure to create the account on database
def create_account(the_info):
    
    dh.run_statement('CALL create_account(?,?)', [the_info[0], the_info[1]])
    the_id=dh.run_statement('CALL checking_credentials(?,?)', [the_info[0], the_info[1]])
    
    print(the_id)
    return the_id

# config figher
def config_fighter(the_info):
    
    dh.run_statement('CALL configuring_player(?,?,?,?,?,?,?)', 
    [the_info[0], the_info[1], the_info[2], the_info[3], the_info[4], the_info[5], the_info[6],])
    

#character list, for client id
def character_selection(client_id):
    
    character_list = dh.run_statement('CALL character_selection_list(?)', [client_id[0][0]])
    if(len(character_list) < 1):
        print('You have no fighter created yet ')
    else:
        for x in character_list:
            print(x[0], x[1].decode("UTF-8"), "hp:", x[2], "points: ", x[3])
        return character_list

#signing in
def sign_in():
    temp_info = []
    user = input('enter your username: ')
    password = input('enter your password: ')
    temp_info.extend([user, password])
    the_id = find_client_id(temp_info)
    print(temp_info)
    return the_id

#mob list
def mob_list():
    
    mob_list = dh.run_statement('CALL mob_list')
    
    return mob_list

def random_move():
    import random
    four_move = [13,14,15,16]
    return random.choice(four_move)
    


generic_mob = mob_list()

import math
# this is to adjust hp, or the strength of the opponent
def adjust_strength(multiplier):
    multiplier_hp = [multiplier]

    basic_mob = []
    basic_mob.append(generic_mob[0][0])
    basic_mob.append(generic_mob[0][1].decode("UTF-8"))
    multiplier_hp.append(generic_mob[0][2])
  

    basic_mob.extend([math.prod(multiplier_hp), generic_mob[0][3], generic_mob[0][4], generic_mob[0][5], generic_mob[0][6]])
    return basic_mob


weak_opponent = adjust_strength(0.1)
fair_opponent = adjust_strength(100)
strong_opponent = adjust_strength(1000)

#convert move id to move name and damage
def convert_id_move(move_id):
    name_attack = dh.run_statement('CALL convert_id_move(?)', [move_id])
    return name_attack

# function to roll a number within 2 numbers range
def rolling_for_damage(low, high):
    import random
    the_damage = random.randrange(low, high)
    return the_damage

#with client id and fighter id, loads info of that fighter
def current_fighter(client_id, fighter_id):
    character_list = character_selection(client_id)
    current_fighter = character_list[int(fighter_id)-1]

    return current_fighter

def update_points(fighter_id, points):
    dh.run_statement("CALL kill_count(?, ?)", [fighter_id, points])
    return loot
loot = [1, 1]
test_add_1 = update_points(1, 3)
print(test_add_1)
# i split the choose an opponent part into 2 functions
def choose_opponent(choice):
    # choice = input('choose an opponent: (1,2,3) ')
    while True:
        match choice:
            case 1:
                return weak_opponent
            case 2:
                return fair_opponent
            case 3:
                return strong_opponent
            case _:
                print('try again')

def ask_choice():
    print('Choose an opponent: ')
    print('1. Weak opponent awards 1 point')
    print('2. Fair opponent awards 2 points')
    print('3. Strong opponent awards 4 points')
       
    while True:
        try:
            client_choice = int(input('what is your decision? ')) 
            if(client_choice == 1 or client_choice == 2 or client_choice == 3):
                return client_choice
            else:
                print('choose again with a number with 1, 2 or 3 ')
        except ValueError:
            print('that is not a number')

      

def choose_signup_login():
    try:
        while True:
            answer_new_or_login = input('Would you like sign up for account or sign in?: type 1 for new account or 2 for sign in ')
            if (answer_new_or_login == '1'):
                print(answer_new_or_login)
                print('sign up it is')
                return answer_new_or_login
            elif(answer_new_or_login == '2'):
                print(answer_new_or_login)
                print("heading to login")
                return answer_new_or_login
    except:
        print("in error")

# for character config, player have to choose 4 skill
def which_skill_choice():
    temp_skill_hold = []    
    try:
        answer_skill_choice = float(print('which skill did you want? just type the number'))
        while (len(temp_skill_hold) < 5):
            temp_skill_hold.append(answer_skill_choice)
            for (y, index) in temp_skill_hold:
                print(index, y)
    except ValueError:
        print('not a number')

# testing = which_skill_choice()





def create_new_or_use_old():
    answer = input('Create new?: type 1 or Continue to selection screen: type 2')
    match answer:
        case 0:
            return 0
        case 1:
            return 1
        case 'new':
            return 0
        case 'continue':
            return 1
        case default:
            return 0
 
    #         answer_new_old_char = input('Would you like to create a new fighter or continue from previous? 1 for new, 2 for continue ')
    #         if(answer_new_old_char == '1'):
    #             fighter_container = create_fighter()
    #             return fighter_container
                    

    #         elif(answer_new_old_char == '2'):
    #             print(answer_new_old_char)
    # except:
    #     print('the error 2')

def create_fighter(answer):
    if (answer == '1'):
        fighter_container = []
        fighter_name = input('enter a name for your fighter: ')
        print(fighter_name, " is this correct?")
        for x in skill_list:
            print (x[0], " ", x[1].decode("UTF-8")," min: ", x[2]," max: ", x[3])

        skill_1 = input('pick your skill 1 using the number: ')
        skill_2 = input('pick your skill 2 using the number: ')
        skill_3 = input('pick your skill 3 using the number: ')
        skill_4 = input('pick your skill 4 using the number: ')
        fighter_container.extend([skill_1, skill_2, skill_3, skill_4])
        print(fighter_container)
        return fighter_container
    else:
        create_new_or_use_old()



# created a set of value in function that is needed to satisfy stored procedure configuring_player
def choose_skill(the_id):
    fighter_container=[]
    fighter_container.append(the_id[0][0])
    fighter_name = input('enter a name for your fighter: ')
    fighter_container.append(fighter_name)
    print(fighter_name, " is this correct?")
    for x in skill_list:
        print (x[0], " ", x[1].decode("UTF-8")," min: ", x[2]," max: ", x[3])

    while (len(fighter_container)<7):
        try:
            skill_1 = int(input('pick your skill 1 using the number: '))
            skill_2 = int(input('pick your skill 2 using the number: '))
            skill_3 = int(input('pick your skill 3 using the number: '))
            skill_4 = int(input('pick your skill 4 using the number: '))
            fighter_container.extend([skill_1, skill_2, skill_3, skill_4, 50000])
            print(fighter_container)
            if (len(fighter_container) >= 7):
                
                print(fighter_container)
                return fighter_container
            else:
                print('keep going')
        except ValueError:
            print('enter number: ')


# function to tie in all the functions
# def run_through():
#     answer_to_choice = choose_signup_login()
#     print(answer_to_choice)
#     if (answer_to_choice == 1):
#         cursor = dh.just_connect()
#         dh.cursor_result(cursor, "CALL create_account(?, ?)", []")
#         dh.the_closer(cursor)
        
#     answer_to_new_old = create_new_or_use_old()
#     print(answer_to_new_old)

# test run for sign up works
def attack_available(current_fighter):
    four_attacks = []
    attack_1=convert_id_move(current_fighter[4])
    attack_2=convert_id_move(current_fighter[5])
    attack_3=convert_id_move(current_fighter[6])
    attack_4=convert_id_move(current_fighter[7])
    four_attacks.extend([attack_1, attack_2, attack_3, attack_4])

    print(attack_1[0][1], " second test")
       
    print('fighter id: ', current_fighter[0])
    print('name : ', current_fighter[1].decode("UTF-8"))
    print('max hp : ', current_fighter[2])
    print('points : ', current_fighter[3])
    print("attack 1: name: ", attack_1[0][0].decode("UTF-8"), "|| min damage: ", attack_1[0][1], "|| max damage: ", attack_1[0][2])
    print("attack 2: name: ", attack_2[0][0].decode("UTF-8"), "|| min damage: ", attack_1[0][1], "|| max damage: ", attack_1[0][2])
    print("attack 3: name: ", attack_3[0][0].decode("UTF-8"), "|| min damage: ", attack_1[0][1], "|| max damage: ", attack_1[0][2])
    print("attack 4: name: ", attack_4[0][0].decode("UTF-8"), "|| min damage: ", attack_1[0][1], "|| max damage: ", attack_1[0][2])
    return four_attacks

def combat_phase(figher_damage, enemy_damage):
    temp_hp_tracker = []
    fighter=rolling_for_damage(figher_min, fighter_max)
    opponent=rolling_for_damage(opp_min, opp_max)

def enemy_move(training_answer):
    cpu_damage_container = []
    cpu_number = random_move()
    if (training_answer == 3):
        current_move = convert_id_move(cpu_number)
        cpu_damage_container.extend([current_move[0][1]*1000, current_move[0][2]*1000])
        print(current_move[0][0].decode("UTF-8"), "damage range: ", cpu_damage_container)
        the_damage = rolling_for_damage(cpu_damage_container[0], cpu_damage_container[1])
        print("using ", current_move[0][0].decode("UTF-8"), " it did ", the_damage, " damages to YOU!!!") 
        return the_damage

# testing_2 = enemy_move(3)
# print(testing_2)



def test_run():
    print('Welcome to Text Battle Arena!!')
    answer = choose_signup_login()
    if(answer == '1'):
        ask_user = signing_up()
        the_id = create_account(ask_user)
        config_character = choose_skill(the_id)
        config_fighter(config_character)
        character_selection(the_id)
        
        return config_character
    elif(answer == '2'):
        print('Account Sign In: ')
        client_id = sign_in()
        character_list = character_selection(client_id)
        while True:
            if(len(character_list) < 1):
                fighter_storage = create_fighter(client_id)
                config_fighter(fighter_storage)
                break
            else:
                while True:
                    try:   
                        choose_fighter = int(input("choose your fighter by number: "))
                        fighter_used = current_fighter(client_id, int(choose_fighter) - 1)
                        attack_available(fighter_used)
                        print("what would you like to train on to earn points? ")
                        print("1. weak opponent, worth 1 point")
                        print("2. fair opponent, worth 2 point")
                        print("3. strong opponent, worth 4 point")
                        training_answer = input('well?: ')
                        temp_opponent = []
                        match training_answer:
                            case '1':
                                temp_opponent = weak_opponent
                            case '2':
                                temp_opponent = fair_opponent
                            case '3':
                                temp_opponent = strong_opponent
                            case default:
                                print("try again")
                        print(temp_opponent[1], "hp: ", temp_opponent[2])
                        print("attack the opponent with attack 1 to 4")
                        print(random_move())
                        temp_hp_tracker = []
                        temp_hp_tracker.append(fighter_used[2])
                        temp_hp_tracker.append(temp_opponent[2])
                        print(temp_hp_tracker)
                        while (temp_hp_tracker[0] > 0 or temp_hp_tracker[1] > 0):
                            choose_attack = input("enter 1 to 4 to attack: ")
                            if(temp_hp_tracker[1] <= 0):
                                print(choose_attack)
                    except ValueError:
                        print("choose a number")

# aa = test_run()





        # else:

        # while True:
            
        #     try:            
        #         selected_fighter = input('select your fighter, use number or q for quit ')
        #         if(selected_fighter == None  and selected_fighter == 'q'):
        #             break
        #         elif(selected_fighter != num):


        #             if (int(selected_fighter) < 1 or int(selected_fighter) > len(character_list)):
        #                 match selected_fighter:
        #                     case len(selected_fighter):
        #                         print(selected_fighter)
        #             else:
        #                 print('choose a number within range')
                   
        #         elif(selected_fighter == 'q'):
        #             break
        #         else:
        #             print('try again with the available options: ')
        #         store_choice = ask_choice()
        #         stored_opponent = choose_opponent(store_choice)

        #         print(stored_opponent)
        #     except ValueError:
        #         print('try again with the either your list of fighter or q for quit')

                


        # print('goodbye for now')



# bbb = ask_choice()
# aaa = choose_opponent(bbb)
# print(aaa)

    

    
# test_run()

# create_new_or_use_old()