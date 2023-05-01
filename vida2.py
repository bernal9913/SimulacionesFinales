
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

''''
The game_of_life function takes a board as input and returns the next generation of the board according to the rules of 
the Game of Life. The function creates a copy of the board to store the next generation and iterates over each cell in 
the board. For each cell, it counts the number of live neighbors and applies the rules of the game to determine whether 
the cell should be alive or dead in the next generation.

The update function is called at each frame of the animation. It takes as input the current frame number, an image 
object, and the current state of the board. The function computes the next generation of the game using the game_of_life 
function and updates the image data to show the new state of the board.

The rest of the code sets up an initial board and uses matplotlib to create an animation that shows how the board 
evolves over time. The FuncAnimation function is used to create an animation that calls the update function at each 
frame.
'''
def game_of_life(board):
    # Get the number of rows and columns
    rows = len(board)
    cols = len(board[0])

    # Create a copy of the board to store the next generation
    next_gen = np.copy(board)

    # Iterate over each cell in the board
    for row in range(rows):
        for col in range(cols):
            # Get the number of live neighbors
            live_neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    if row + i >= 0 and row + i < rows and col + j >= 0 and col + j < cols:
                        if board[row + i][col + j] == 1:
                            live_neighbors += 1

            # Apply the rules of the game
            if board[row][col] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    next_gen[row][col] = 0
            else:
                if live_neighbors == 3:
                    next_gen[row][col] = 1

    # Return the next generation
    return next_gen


def update(frameNum, img, board):
    # Compute the next generation of the game
    new_board = game_of_life(board)

    # Update the image data
    img.set_data(new_board)

    # Update the board
    board[:] = new_board[:]

    return img,


# Set up the initial board
board = np.zeros((10, 10))
board[1:4, 1:4] = [[0, 1, 0],
                   [0, 1, 0],
                   [0, 1, 0]]

# Set up the animation
fig, ax = plt.subplots()
img = ax.imshow(board, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, board), frames=10,
                              interval=500)

plt.show()
