import requests

# r = requests.get('http://localhost:8000/checkin/222')
# print(r.text)
#
# a = requests.get('http://localhost:8000/checkin/122')
# print(a.text)
#
# b = requests.get('http://localhost:8000/checkin/123')
# print(b.text)
print("Welcome to the client!")
while True:
    print("Another command?")
    x = input()
    # if(x.split(" ")==True):
    #     x.split(" ")
    #     param1, param2 = x.split(" ")
    #     print(param1 + " 2nd param " + param2)
    # else:
    #     param1 = x

    try:
        param1, param2, param3 = x.split(" ")
    except ValueError:
        param1 = x
        print("One param")
        print(param1)
    else:
        print("Two params")
        print(param1 + " " + param2)

    if param1=="quit":
        b = requests.delete('http://localhost:8000/delete/'+param2+'/')
    if param1=="doctors":
        b = requests.get('http://localhost:8000/'+param1+'/')
    if param1=="checkin":
        b = requests.post('http://localhost:8000/'+param1+'/'+param2+'/')
    if param1=="position":
        b = requests.get('http://localhost:8000/'+param1+'/'+param2+'/')
    if param1=="login":
        b = requests.post('http://localhost:8000/'+param1+'/'+param2+'/')


    print(b.text)
    print(b.url)
