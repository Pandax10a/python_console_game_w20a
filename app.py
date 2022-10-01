import mariadb
import dbhelpers as dh


def check_skill_list():
    cursor = dh.just_connect()
    the_skill_list = dh.cursor_result(cursor, "CALL skill_selection_list")
    dh.the_closer(cursor)
    return the_skill_list

skill_list = check_skill_list()

def signing_up():
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





# calling stored procedure to create the account on database
def create_account(the_info):
    cursor = dh.just_connect()
    dh.cursor_no_result(cursor, 'CALL create_account(?,?)', [the_info[0], the_info[1]])
    dh.the_closer(cursor)


def test_run():
    ask_user = signing_up()
    create_account(ask_user)
    
test_run()


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


def create_new_or_use_old():
    fighter_container = []
    try:
        while True:
            answer_new_old_char = input('Would you like to createa new fighter or continue from previous? 1 for new, 2 for continue ')
            if(answer_new_old_char == '1'):
                fighter_name = input
                for x in skill_list:
                    print (x[0], " ", x[1].decode("UTF-8")," min: ", x[2]," max: ", x[3])
                    

            elif(answer_new_old_char == '2'):
                print(answer_new_old_char)
    except:
        print('the error 2')

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

