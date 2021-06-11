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
    new_state = state.copy()
    player =  1 if cell_number < 7 else 2
    mancala = 0 if player == 1 else 13
    double_turn = 0
    num_stones = new_state[cell_number]
    #invalid move
    if num_stones == 0:
        return [],0
    
    new_state[cell_number] = 0
    index = cell_number
    while num_stones != 0:

        if index == 13:
            index = 6
            new_state[index] += 1

        elif index > 6 and index < 13:
            index += 1
            if index == 13 and player == 1:
                continue
            else:
                new_state[index] += 1 
            
        elif index > 0 and index <= 6:
            index -= 1
            if index == 0 and player == 2:
                continue
            else:
                new_state[index] += 1 

        elif index == 0:
            index = 7 
            new_state[index] += 1

        num_stones -=1
    
    # repeat move and stealing
    if index == 13:
        #player
        double_turn = 1
    elif index == 0:
        #computer
        double_turn = -1
    else:
        index_player = 1 if index < 7 else 2
        #stealing mode
        if new_state[index] == 1 and mode == 1 and player == index_player and new_state[(index+6)%12] > 0 :
            new_state[mancala] += new_state[index] + new_state[(index+6)%12]
            new_state[index] = 0
            new_state[(index+6)%12] = 0 

    return new_state,double_turn


def print_state(state):
    print("__________________________________________")
    print(f"{str(state[0])}  | {str(state[1:7])}   | {str(state[13])}")
    print(f"   | {str(state[7:13])} | ")
    print("__________________________________________")


def apply_minimax_alpha_beta(root):
    for node in root.children:
        if(node.value == None):
            node.alpha = root.alpha
            node.beta = root.beta
            apply_minimax_alpha_beta(node)
            node.value = node.alpha if (node.type) else node.beta
        value = node.value
        if root.type:
            if value > root.alpha:
                root.alpha = value
        else:
            if value < root.beta:
                root.beta = value 

        if root.alpha >= root.beta:
                break
    

            
def build_tree(root,num_levels,mode):
    count_value = False
    if num_levels == 0:
        return
    if num_levels == 1:
        count_value = True
    find_next_possible_states(root,count_value,mode)
    for node in root.children:
        build_tree(node,num_levels-1,mode) 
        
def find_next_possible_states(node,count_value,mode):
    i = 0 if node.type==True else 6
    for x  in range(1,7) :        
        value = None        
        new_st = state_update(node.state,x+i,mode)
        if new_st[0]:
            type = node.type if new_st[1]!=0 else not(node.type)
            
            if count_value or new_st[0][1:7] == [0,0,0,0,0,0] :
                value = new_st[0][0]

            if new_st[0][7:13] == [0,0,0,0,0,0]:
                rest_stones = sum(new_st[0][1:7])
                value =new_st[0][0] + rest_stones
            

            node.addNode(Node(state=new_st[0],type=type,value=value)) 
 

def get_best_node(root):
    max_value = -10000
    max_node = None
    for node in root.children:
        if node.value != None and node.value > max_value:
            max_value = node.value
            max_node = node
    return max_node
    


def start_game(state,mode,player,level):
   pass

if __name__ == "__main__":
    pass