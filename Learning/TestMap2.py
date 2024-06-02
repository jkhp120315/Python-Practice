
def printUsersName(listUsers):
    listofuserName = list(map(lambda user: user['name'], listUsers))
    print(listofuserName)





listUsers = [
    {
        'name' : 'Himanshu',
        'age' : 38,
        'gender' : 'male'
    },
    {
        'name' : 'Rob',
        'age' : 37,
        'gender' : 'male'
    },
    {
        'name' : 'Nidhi',
        'age' : 24,
        'gender' : 'female'
    }
]

printUsersName(listUsers)