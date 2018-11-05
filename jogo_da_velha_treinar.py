import numpy as np
import tkinter as tk
import pickle as pickle
import copy

from q_jogo_da_velha import Game, QPlayer

root = tk.Tk()
epsilon = 0.9
player1 = QPlayer(mark="X", epsilon=epsilon)
player2 = QPlayer(mark="O", epsilon=epsilon)
game = Game(root, player1, player2)

exit()

N_episodes = 200000
for episodes in range(N_episodes):
    game.play()
    game.reset()    

Q = game.Q

filename = "aprendizado_q_{}.p".format(N_episodes)
pickle.dump(Q, open(filename, "wb"))