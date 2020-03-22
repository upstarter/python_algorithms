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
