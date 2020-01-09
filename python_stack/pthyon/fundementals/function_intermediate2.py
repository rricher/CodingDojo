def updateVals():
    x = [ [5,2,3], [10,8,9] ] 
    students = [
        {'first_name': 'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'}
    ]
    sports_directory = {
        'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
        'soccer' : ['Messi', 'Ronaldo', 'Rooney']
    }
    z = [ {'x': 10, 'y': 20} ]
    x[1][0] = 15
    students[0]['last_name'] = "Bryant"
    sports_directory['soccer'][0] = "Andres"
    z[0]['y'] = 30

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(someList):
     for i in range(len(someList)):
         print(f"first_name - {someList[i]['first_name']}, last_name - {someList[i]['last_name']}")
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for k in some_dict.keys():
        print(f"{len(some_dict[k])} {k}")
        for val in some_dict[k]:
            print(val)

