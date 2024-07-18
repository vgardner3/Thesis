'''def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    security_question = input("Enter your security question: ")
    security_answer = input("Enter your security answer: ")
    user_database[username] = {'password': password, 'security_question': security_question, 'security_answer': security_answer}
    print("Registration successful!")
    def get_user_input(prompt):
    return input(prompt)
'''
def save_user_data(username, password, security_question, security_answer):
    user_database[username] = {'password': password, 'security_question': security_question, 'security_answer': security_answer}

def register():
    username = get_user_input("Enter your username: ")
    password = get_user_input("Enter your password: ")
    security_question = get_user_input("Enter your security question: ")
    security_answer = get_user_input("Enter your security answer: ")
    save_user_data(username, password, security_question, security_answer)
    print("Registration successful!")