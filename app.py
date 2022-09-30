import mariadb
import dbhelpers as dh


def check_skill_list():
    cursor = dh.just_connect()
    the_skill_list = dh.cursor_result(cursor, "CALL skill_selection_list")
    dh.the_closer(cursor)
    return the_skill_list

skill_list = check_skill_list()




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



def create_new_or_use_old():
    try:
        while True:
            answer_new_old_char = input('Would you like to createa new fighter or continue from previous? 1 for new, 2 for continue ')
            if(answer_new_old_char == '1'):
                for x in skill_list:
                    print (x[0], " ", x[1].decode("UTF-8")," min: ", x[2]," max: ", x[3])
    except:
        print('the error 2')

# function to tie in all the functions
def run_through():
    answer_to_choice = choose_signup_login()
    print(answer_to_choice)
    answer_to_new_old = create_new_or_use_old()
    print(answer_to_new_old)

test_1 = run_through()