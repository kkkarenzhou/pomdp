
#get inputs
inputs = input("enter here : ")
inputs = inputs.split(" ")

def inputd(a):
    a = a.strip("(")
    a = a.strip(")")
    a  = a.split(",")
    return a


init = inputd(inputs[0])
init = [int(x) for x in init if x != ""]
init = tuple(init)
actions = inputd(inputs[1])
evids = inputd(inputs[2])
evids = [ int(x) for x in evids]

#create an initial dictionary for belief state
states = [(x,y) for x in range(1,5) for y in range(1,4)]
states.remove((2,2))
b=dict()
if init == ():
    b = { a: (1/9) for a in states }
    b[(4,3)] = 0
    b[(4,2)] = 0
else:
    b = { a: 0 for a in states }
    b[init] = 1

#create a sensor model 
sensor = [(e,s) for e in range(1,3) for s in states]
obs = { a: 0 for a in sensor}
for s in sensor:
    if s[1] == (4,3) or s[1] == (4,2):
        obs[s] = 0
    else:
        if s[0] == 1:
            if s[1][0] == 3:
                obs[s] = 0.9
            else :
                obs[s] = 0.1
        if s[0] == 2:
            if s[1][0] == 3:
                obs[s] = 0.1
            else:
                obs[s] = 0.9

#create a dictionary for action and state
a_s = {a:list() for a in states}
for s in states:
    us = (s[0],s[1]+1)
    ds = (s[0],s[1]-1)
    rs = (s[0]+1,s[1])
    ls = (s[0]-1,s[1])
    for a in ("up","down","left","right"):
        if a == "up":
            if us in states:
                a_s[us].append((a,s,0.8))
            else:
                a_s[s].append((a,s,0.8))
            if rs in states:
                a_s[rs].append((a,s,0.1))
            else:
                a_s[s].append((a,s,0.1))
            if ls in states:
                a_s[ls].append((a,s,0.1))
            else:
                a_s[s].append((a,s,0.1))
        if a == "down":
            if ds in states:
                a_s[ds].append((a,s,0.8))
            else:
                a_s[s].append((a,s,0.8))
            if rs in states:
                a_s[rs].append((a,s,0.1))
            else:
                a_s[s].append((a,s,0.1))
            if ls in states:
                a_s[ls].append((a,s,0.1))
            else:
                a_s[s].append((a,s,0.1))
        if a == "right":
            if rs in states:
                a_s[rs] .append((a,s,0.8))
            else:
                a_s[s].append((a,s,0.8))
            if ds in states:
                a_s[ds].append((a,s,0.1))
            else:
                a_s[s].append((a,s,0.1))
            if us in states:
                a_s[us].append((a,s,0.1))
            else:
                a_s[s] .append((a,s,0.1))
        if a == "left":
            if ls in states:
                a_s[ls] .append((a,s,0.8))
            else:
                a_s[s] .append((a,s,0.8))
            if ds in states:
                a_s[ds].append((a,s,0.1))
            else:
                a_s[s] .append( (a,s,0.1))
            if us in states:
                a_s[us] .append((a,s,0.1))
            else:
                a_s[s].append((a,s,0.1))


    



for i in range(len(actions)):
        #for all b(s)
    new_b = dict()
    for s in b:
        prob = 0
            #probability of all the states that can reach s
            #with action a times b(s)
        for p in a_s[s]:
            if p[0] == actions[i]:
                prob += p[2]*b[p[1]]
        new_b[s] = obs[(evids[i],s)]*prob
    norm = sum(new_b.values())
    for s in new_b:
        new_b[s] = new_b[s]/norm
    b = new_b

print(b)

