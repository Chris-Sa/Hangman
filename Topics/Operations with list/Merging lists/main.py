

def merge_lists(list_one, list_two):

    # print(list_one)
    # print(list_two)
    list_one.extend(list_two)
    # print(list_one)
    return list_one


list_one = ['Washington, D.C.', 'Chicago', 'New York']
list_two = ['Los Angeles', 'Las Vegas']
merge_lists(list_one, list_two)
