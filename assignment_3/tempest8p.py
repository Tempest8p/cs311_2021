import argparse
import random



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')
    
    
    args = parser.parse_args()
    move= args.last_opponent_move
    anger=0
    multi=0
    #donut
    if move != "0":
        r=open("storm.txt","r")
        anger= int(r.readline())
        multi=int(r.readline())+1
        r.close()
    if move == "confess":
        anger=anger+multi
        multi=multi+1
        if anger>10: anger=10
    elif move == "silent": 
        anger=anger-2
        if anger<0: anger=0
        multi=0
   
    r=open('storm.txt','w')
    r.write(str(anger))
    r.write('\n')
    r.write(str(multi))
    r.close()
    action=list(random.choices(['confess', 'silent'], weights=(anger+3,12-anger),k=20))
    print( random.choice(action) )
    #print (action) #left for testing
    #print (anger)
    #print(multi)