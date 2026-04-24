# import numpy as np

# board=np.zeros((3,3),dtype=int)
# print(board)

# def print_board(b):
#     symbols={0:" ", 1:"X", -1:"O"}
#     for r in range(3):
#         row=" | ".join(symbols[val] for val in b[r])
#         print(" "+row)
#         if r<2:
#             print("---+---+---")
#     print()

# def check_winner(b):
#     if 3 in np.sum(b,axis=1) or 3 in np.sum(b,axis=0):
#         return "X"
#     if -3 in np.sum(b,axis=1) or -3 in np.sum(b,axis=0):
#         return "O"
#     if np.trace(b)==3 or np.trace(np.fliplr(b))==3:
#         return "X" #trace will calculate the sum of digonal and fliplr will flip the array
#     if np.trace(b)==-3 or np.trace(np.fliplr(b))==-3:
#         return "O"
#     if not 0 in b:
#         return "DRAW"
    
#     return None



# current=1

# print("Welcome to TIC TAC TOE")
# print_board(board)

# while True:
#     if current==1:
#         player = 'X'
#     else:
#         player = 'O'

#     try:
#         row =int(input(player+"enter row (0,1,2)"))
#         col =int(input(player+"enter col (0,1,2)"))

#     except ValueError:
#         print("please enter only \n")
#         continue

#     if row <0 or row >2 or col <0 or col >2:
#         print("row and col must be between 0 and 2")

#     if board[row,col] !=0:
#         print("cell is already taken")        
     
#     board[row,col]=current
#     print_board(board)

#     result = check_winner(board)

#     if result is not None:
#         if result =="DRAW":
#             print("ohoo it's a DRAW")
#         else:
#             print(result,"wins")

#         break

#     if current==1:
#         current=-1
#     else:
#         current=1

import streamlit as st
import numpy as np

# ----------- PAGE CONFIG -----------
st.set_page_config(page_title="Tic Tac Toe", layout="centered")

# ----------- DARK THEME + SQUARE CELLS -----------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}

/* Square buttons */
.stButton > button {
    width: 100%;
    aspect-ratio: 1 / 1;   /* ✅ makes perfect square */
    font-size: 40px;
    font-weight: bold;
    border-radius: 12px;
    background-color: #1f2937;
    color: white;
    border: 1px solid #444;
}

/* Hover effect */
.stButton > button:hover {
    background-color: #374151;
}

/* Title center */
h1 {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ----------- INITIAL STATE -----------
if "board" not in st.session_state:
    st.session_state.board = np.zeros((3,3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False

# ----------- FUNCTIONS -----------
def check_winner(b):
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return "X"
    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return "O"
    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"
    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"
    if not 0 in b:
        return "DRAW"
    return None

def make_move(i, j):
    if st.session_state.board[i, j] == 0 and not st.session_state.game_over:
        st.session_state.board[i, j] = st.session_state.current
        result = check_winner(st.session_state.board)

        if result:
            st.session_state.game_over = True
            if result == "DRAW":
                st.warning("😐 It's a Draw!")
            else:
                st.success(f"🎉 {result} Wins!")
        else:
            st.session_state.current *= -1

def reset_game():
    st.session_state.board = np.zeros((3,3), dtype=int)
    st.session_state.current = 1
    st.session_state.game_over = False

# ----------- UI -----------
st.title("🎮 Tic Tac Toe")

player = "X" if st.session_state.current == 1 else "O"
st.subheader(f"Current Player: {player}")

symbols = {0: " ", 1: "X", -1: "O"}

# ----------- BOARD -----------
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            st.button(
                symbols[st.session_state.board[i, j]],
                key=f"{i}-{j}",
                on_click=make_move,
                args=(i, j)
            )

# ----------- RESET BUTTON -----------
st.markdown("---")
if st.button("🔄 Restart Game"):
    reset_game()




























































# current<=9:
#     r=int(input("enter the row no."))
#     c=int(input("enter the col no."))

#     if board[r,c] !=0:
#         print("Block already filled")
#     else:
#         fill=input("enter whaw you want to fill")
#         if fill=="X" or fill=="x":
#             board[r,c]=1
#         elif fill=="O" or fill=="o":
#             board[r,c]=-1
#         else:
#             print("Enter the valid option  from 'X' or 'Y'")
#     current+=1