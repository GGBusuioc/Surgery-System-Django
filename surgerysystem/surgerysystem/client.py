import requests

print("Welcome to the client!")
while True:
    print("Another command?")
    x = input()

    try:
        param1, param2 = x.split(" ")
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
        print("Please enter your password");
        p = input()
        # get the password from the server
        r = requests.get('http://localhost:8000/'+param1+'/'+param2+'/')
        if(str(p)==r.text):
            print("You are succesfully logged in, id %d" % (int(param2)))
            b = requests.post('http://localhost:8000/'+param1+'/'+param2+'/')
        else:
            print("Password was incorrect. Try loging in again.")


    print(b.text)
    print(b.url)
