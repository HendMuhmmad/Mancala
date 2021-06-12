class Node:
    def __init__(self,state=None,value=None,beta=None,alpha=None,type=None):
        """
        Parameters: state: List
                    Board state associated with the node.

                    value: int
                    The value associated with the nod’s state according to the utility function.

                    alpha: int
                    alpha value of node according to the minimax algorithm.

                    beta: int
                    beta value according the minimax algorithm.

                    type: boolean
                    node type in the tree True for a maximizer, False for minimizer. 

        """
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
        """
        Append the given node to the calling node children.
        Parameters: node: object 
                    The child node

        """
        node.parent = self
        self.children.append(node)

def state_update(state,cell_number,mode):
    """
    Gives the resulting state after moving stones in a given pocket.
    Parameters: state: List 
                The current board state.

                cell_number: int
                The number of pocket must be from 1 to 12 only.

                mode: int 
                Determine mode 1 for stealing and 0 for non-stealing.

    Return      new_state,double_turn: tuple of list and int

                The list contains the next state or empty if the pocket is empty.
                double_turn is  1 if the user is to be play again
                               -1 if the computer is to play again
                                0 otherwise

    """
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
    """
    Prints the board‘s state.
    Parameters:  state: List
    """
    print("__________________________________________")
    print(f"{str(state[0])}  | {str(state[1:7])}   | {str(state[13])}")
    print(f"   | {str(state[7:13])} | ")
    print("__________________________________________")


def apply_minimax_alpha_beta(root):
    """
    Traverse the game tree while applying minimax algorithm with alpha beta pruning to calculate node values.
    Parameters: root: node object
                The root of the tree to apply the algorithm on.

    """

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
    """
    Build the game tree starting from the node root input by generating all possible state nodes played at each turn.
    Parameters: root: object
                The input node containing the current state of the game.

                num_levels: int
                Tree required depth.

                mode: int 
                Determine mode 1 for stealing and 0 for non-stealing.

    """
    count_value = False
    if num_levels == 0:
        return
    if num_levels == 1:
        count_value = True
    find_next_possible_states(root,count_value,mode)
    for node in root.children:
        build_tree(node,num_levels-1,mode) 
        
def find_next_possible_states(node,count_value,mode):
    """
    Add children nodes to the given node with the next possible states from the input node state.
    Parameters: node: node object
                The input node containing the state to add children to it.

                count_value: boolean
                True count the value of the added node states and false otherwise.
                
                mode: int 
                Determine mode 1 for stealing and 0 for non-stealing.

    """
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
    """
    Get the node with maximum value from the root of the input tree direct children
    Parameters: root: node object
                The root of the tree.

    Return:     max_node: node object
                The node that has the max value.

    """
    max_value = -10000
    max_node = None
    for node in root.children:
        if node.value != None and node.value > max_value:
            max_value = node.value
            max_node = node
    return max_node
    


def start_game(state,mode,player,level):
    """
    Starts the game loop until one of the players win.
    Parameters: state: List 
                The initial board state.
                player: int
                player code 0 for player.
                                        1 for computer
                mode: int 
                Determine mode 1 for stealing and 0 for non-stealing.
                level: int
                determines the difficulty 1 for easy
                                          2 for medium
                                          3 for hard

	return: play_again: int
            1 if the user wants to play again
            0 to exit

    """
    winner = 0
    while(1):
        print("\nCurrent State:")
        print_state(state)
        #player
        if player == 0:
            print("Enter a number from 1 to 6")
            ip = input("Pocket number: ")
            pocket = int(ip)+6
            if pocket >= 7 and pocket <= 12:         
                new_state,play_again = state_update(state,pocket,mode)
                if new_state == []:
                    print("!!!!!!!!!!!!!!!!! Empty Pocket Try Again !!!!!!!!!!!!!!!!!!!!")
                else:
                    state = new_state
                    # print_state(state)
                    if play_again == 1:
                        player = 0
                    else:
                        player = 1
            else:
                print("!!!!!!!!!!!!!!!!! Invalid Move Try Again !!!!!!!!!!!!!!!!!!!!")
        else:
            print("Computer is thinking .........")
            root = Node(state=state,alpha=-10000,beta=10000,type=True)
            build_tree(root,level,mode)
            apply_minimax_alpha_beta(root)
            node = get_best_node(root)
            state = node.state
            # print_state(state)
            if node.type:
                player = 1
            else:
                player = 0


        if state[1:7] == [0,0,0,0,0,0]:
            rest_stones = sum(state[7:13])
            state[7:13] = [0,0,0,0,0,0]
            state[13] += rest_stones
            winner = 1

        elif state[7:13] == [0,0,0,0,0,0]:
            rest_stones = sum(state[1:7])
            state[1:7] = [0,0,0,0,0,0]
            state[0] += rest_stones
            winner = 1
            
        if winner:
            print_state(state)
            if state[0] > state[13]:
                print("******************** You Lose ************************")
            elif state[0] < state[13]:
                print("******************** You win  ************************")
            else:
                print("******************** Draw   ************************")

            print("Press 1 to play again")
            print("Press 0 to exit")
            return int(input("-> "))
            

if __name__ == "__main__":
    while True:
        current_state = [0,4,4,4,4,4,4,   4,4,4,4, 4 ,4,0]
                    # 0,1,2,3,4,5,6,  7,8,9,10,11,12,13

        print("------------------- Welcome to Mancala --------------------")
        print("Press 1 For Easy mode")
        print("Press 2 For Medium mode")
        print("Press 3 For Hard mode")
        level = int(input("Difficulty: "))*3
        print("Press 0 for normal mode")
        print("Press 1 for stealing mode")
        mode = int(input("Mode: "))
        print("Press 0 to play first")
        print("Press 1 to play second")
        player = int(input("Player: "))

        print("------------------- The game is on ------------------------")
        again = start_game(current_state,mode,player,level)
        if again == 0:
            break

