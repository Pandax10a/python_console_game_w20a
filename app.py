import mariadb
import dbhelpers as dh


def check_skill_list():
    cursor = dh.just_connect()
    the_skill_list = dh.cursor_result(cursor, "CALL skill_selection_list")
    dh.the_closer(cursor)
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
def find_client_id(user, password):
    cursor = dh.just_connect()
    result = dh.cursor_result(cursor, 'CALL checking_credentials(?,?)', [user, password])
    dh.the_closer(cursor)
    return result


# aa = find_client_id('test user 9', 'ii999')
# print(aa)

# calling stored procedure to create the account on database
def create_account(the_info):
    cursor = dh.just_connect()
    dh.cursor_no_result(cursor, 'CALL create_account(?,?)', [the_info[0], the_info[1]])
    the_id=dh.cursor_result(cursor, 'CALL checking_credentials(?,?)', [the_info[0], the_info[1]])
    dh.the_closer(cursor)
    print(the_id)
    return the_id

# config figher
def config_fighter(the_info):
    cursor = dh.just_connect()
    dh.cursor_no_result(cursor, 'CALL configuring_player(?,?,?,?,?,?,?)', 
    [the_info[0], the_info[1], the_info[2], the_info[3], the_info[4], the_info[5], the_info[6],])
    dh.the_closer(cursor)

#character list, for client id
def character_selection(client_id):
    cursor = dh.just_connect()
    character_list = dh.cursor_result(cursor, 'CALL character_selection_list(?)', [client_id[0][0]])
    dh.the_closer(cursor)
    for x in character_list:
        print(x[0], x[1].decode("UTF-8"), "hp:", x[2], "points: ", x[3])
    return character_list

#signing in
def sign_in():
    user = input('enter your username: ')
    password = input('enter your password: ')
    the_id = find_client_id(user, password)
    print(user, password)
    return the_id

#mob list
def mob_list():
    cursor = dh.just_connect()
    mob_list = dh.cursor_result(cursor, 'CALL mob_list')
    dh.the_closer(cursor)
    return mob_list

generic_mob = mob_list()


import math
# this is to adjust hp, or the strength of the opponent
def adjust_strength(multiplier):
    multiplier_num = [multiplier]
    basic_mob = []
    basic_mob.append(generic_mob[0][0])
    basic_mob.append(generic_mob[0][1].decode("UTF-8"))
    multiplier_num.append(generic_mob[0][2])
    basic_mob.extend([math.prod(multiplier_num), generic_mob[0][3], generic_mob[0][4], generic_mob[0][5], generic_mob[0][6]])
    return basic_mob


weak_opponent = adjust_strength(0.1)
fair_opponent = adjust_strength(10)
strong_opponent = adjust_strength(100)

# def fighter_damage(skill_id):



      

def choose_signup_login():
    try:
        while True:
            answer_new_or_login = input('Would you like sign up for account or sign in?: type 1 for new account or 2 for sing in ')
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

testing = which_skill_choice()



def create_new_or_use_old():
    fighter_container = []
    try:
        while True:
            answer_new_old_char = input('Would you like to create a new fighter or continue from previous? 1 for new, 2 for continue ')
            if(answer_new_old_char == '1'):
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
                    

            elif(answer_new_old_char == '2'):
                print(answer_new_old_char)
    except:
        print('the error 2')


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
            selected_fighter = int(input('select your fighter, use number '))
            if (selected_fighter < 1 or selected_fighter > len(character_list)):
                print('try again')
            else:
                print('Choose an opponent: ')
                print('1. Weak opponent awards 1 point')
                print('2. Fair opponent awards 2 points')
                print('3. Strong opponent awards 4 points')
                client_choice = print('what is your decision? ')

                choices = mob_list()
                print(choices)
                choose_mob = input('Which opponent did you want to try?')
                


        print('goodbye for now')
    
# test_run()

# create_new_or_use_old()