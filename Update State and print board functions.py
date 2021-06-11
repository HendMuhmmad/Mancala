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