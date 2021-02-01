# get inputs
#inputs = input("enter here : ")
#mdp_inputs = inputs.split(" ")

#create an initial dictionary for belief state
bs_dic = dict()
states = [(x,y) for x in range(1,5) for y in range(1,4)]
bs_dic = { a: (1/9) for a in states }
del bs_dic [(2,2)]
bs_dic[(4,1)] = 0
bs_dic[(4,2)] = 0

#create a sensor model 
obser = dict()
sensor = [(e,s) for e in range(1,3) for s in states]
print(sensor)