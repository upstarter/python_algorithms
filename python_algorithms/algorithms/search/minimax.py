# A simple Python3 program to find
# maximum score that
# maximizing player can get
import math


def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):

    # base case : targetDepth reached
    if curDepth == targetDepth:
        return scores[nodeIndex]

    if maxTurn:
        return max(
            minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth),
        )

    else:
        return min(
            minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
            minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth),
        )


scores = [1, 3, 0, 7, 10, 3, 21, 21]

treeDepth = math.log(len(scores), 2)

print("The optimal value is : ")
print(minimax(0, 0, True, scores, treeDepth))

# pseudo
# def minimax(position, depth, maximizingPlayer)
#     if depth == 0 or game over in position
#         # looks only at the current position and does not
#         # explore possible moves (therefore static)
#         return static evaluation of position
#
#     if maximizingPlayer
#         maxEval = -infinity
#         for each child of position
#             eval = minimax(child, depth - 1, false)
#             maxEval = max(maxEval, eval)
#         return maxEval
#
#     else
#         minEval = +infinity
#         for each child of position
#             eval = minimax(child, depth - 1, true)
#             minEval = min(minEval, eval)
#         return minEval
#
#
# // initial call
# minimax(currentPosition, 3, true)
