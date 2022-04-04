def check_email(string):

    valid = True

    if " " in string:
        #print("space")
        valid = False
    elif "@." in string:
        #print("@.")
        valid = False
    elif "@" not in string:
        #print("no at")
        valid = False

    if valid:
        at = string.find("@")
        #print(at)
        if string.find('.', at + 1) != -1:
            # print(string.find('.', at + 1))
            # print("True")
            return "True"
        else:
            # print("False")
            return "False"
    else:
        # print("False")
        return "False"