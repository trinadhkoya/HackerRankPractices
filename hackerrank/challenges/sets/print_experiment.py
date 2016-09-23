def log_in(user, password, security):
    if user == "trinadh" and password == "password" and security == "secretkey":
        print("Successful Log In")
    else:
        print("Wrong User Name or Password")


user_details = ["trinadh", "password", "secretkey"]

# in this ,though we are passing the  data in a list ,it assumes as a single parameter
log_in(user_details)
# in this ,puttng star before the list data,splits the list data in  to list lengh parameters(3)
log_in(*user_details)
