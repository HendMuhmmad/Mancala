class Node:
    def __init__(self,state=None,value=None,beta=None,alpha=None,type=None):
        self.state = state
        self.value = value
        self.beta = beta
        self.alpha = alpha
        #type true maximizer
        #type false minimizer
        self.type=type
        self.children = []
        self.parent = None

    def addNode(self, node):
        node.parent = self
        self.children.append(node)

def state_update(state,cell_number,mode):
    pass


def print_state(state):
    pass


def apply_minimax_alpha_beta(root):
    pass

            
def build_tree(root,num_levels,mode):
    pass 
        
def find_next_possible_states(node,count_value,mode):
    pass
 

def get_best_node(root):
    pass


def start_game(state,mode,player,level):
   pass

if __name__ == "__main__":
    pass