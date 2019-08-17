responses=["welcome","my name is tanay","sorry","thanks"]
def extract_num_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def lcm(a,b):
    l=a if a>b else b
    while L<=a*b:
        if l%a==0 and l%b==0:
            return l
        l=l+1
def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b
def end():
    print(responses[3])
    input("press enter to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[2])
operation={"plus":add,"add":add,"addition":add,"sum":add,"summation":add,"minus":sub,"subtract":sub,"subtraction":sub,"difference":sub,"product":mul,"multiply":mul,"multiplication":mul,"division":div,"divide":div}
commands={"name":myname,"end":end,"exit":end,"close":end}

print(responses[0])
print(responses[1])
while True:
    print()
    text=input("enter some text ")
    for word in text.split(' '):
        if word in operation.keys():
            try:
                l=extract_num_from_text(text)
                r=operation[word](l[0],l[1])
                print(r)
            except:
                print("something is wrong")
            finally:
               break
        elif word in commands.keys():
           commands[word]()
           break
    else:
        sorry()
