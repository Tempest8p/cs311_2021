import random
import string
import itertools

NODE_COUNT_LAYER = [4,3,2]

class node:
    def __init__(self):
        self.children = [] #connection to children
        self.weights = []  #weight of connections

        self.node_name=''.join(random.choice(string.ascii_letters) for i in range(4)) #makes names for nodes

    def make_children(self, current_layer, nodes_in_layer):
        if current_layer >= len(nodes_in_layer): return #ends recursion
        for i in range(nodes_in_layer[current_layer]):
            self.children.append(node())
        self.children[0].make_children(current_layer+1 , nodes_in_layer) #recusion for next layer
        for i in range(1,len(self.children)):
            self.children[i].children = self.children[0].children[:]
    
    def print_layer(self, current_layer, nodes_in_layer):

        indent = '\t'*current_layer
        if current_layer >= len(nodes_in_layer):
            print(f"{indent} {self.node_name}")
            return #end recursion
        print(f"{indent}{self.node_name} is connected to")
        for i in range (len(self.children)):
            self.children[i].print_layer(current_layer+1,nodes_in_layer)
            try:print(f"{indent} Weight of {self.weights[i]}")
            except: pass
            
        return
    def random_weighs(self, current_layer, nodes_in_layer):
        if current_layer >= len(nodes_in_layer):return #eject from recustion
        self.weights = [0.0]*len(self.children)
        for i in range(len(self.children)):
            self.weights[i]= random.uniform(0, 1) 
            self.children[i].random_weighs(current_layer+1,nodes_in_layer)
        return

        
my_node = node()
my_node.make_children(0,NODE_COUNT_LAYER)
my_node.random_weighs(0,NODE_COUNT_LAYER)

my_node.print_layer(0, NODE_COUNT_LAYER)