# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'

studs = [Belov, Smith, Sarada]

courses = set()
for stud in studs:
    for subject in stud:
        courses.add(subject)

print(len(courses))