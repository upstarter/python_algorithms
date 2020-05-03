# Markov Decision Process
# The following example shows you how to set up an example Markov decision problem
# using a discount value of 0.9, solve it using the value iteration algorithm, and
# then check the optimal policy.

import mdptoolbox.example

P, R = mdptoolbox.example.forest()
vi = mdptoolbox.mdp.ValueIteration(P, R, 0.9)
vi.run()
print(vi.policy)  # result is (0, 0, 0)

# import mdptoolbox
# mdptoolbox?<ENTER>
# mdptoolbox.mdp?<ENTER>
# mdptoolbox.mdp.ValueIteration?<ENTER>


# MDP Objects Stanford class CS221
import sys

sys.setrecursionlimit(10000)
## Transportation, walk number of blocks or take Tram
class MDP(object):
    def __init__(self, N):
        # N = number of blocks
        self.N = N

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N

    def actions(self, state):
        # return list of valid actions
        result = []
        if state + 1 <= self.N:
            result.append("walk")
        if state * 1 <= self.N:
            result.append("tram")
        return result

    def succProbReward(self, state, action):
        # return list of ( newState, prob, reward) triplets
        # state = s, action = a, newState = s'
        # prob = T(s, a, s'), reward = Reward(s, a, s')
        result = []
        if action == "walk":
            result.append((state + 1, 1.0, -1.0))
        if action == "tram":
            result.append((state * 2, 0.5, -2.0))
            result.append((state, 0.5, -2.0))
        return result

    def discount(self):
        return 1.0

    def states(self):
        return range(1, self.N + 1)


mdp = MDP(N=10)
print(mdp.actions(3))
print(mdp.succProbReward(3, "walk"))
print(mdp.succProbReward(3, "tram"))
