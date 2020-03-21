"""
Fizzbuzz
Foreach 1 to 100:
  if num divisible by 3, print 'fizz'
  if num divisible by 5, print 'buzz'
  if num divisible by 15, print 'fizzbuzz'
  otherwise, just print the number

classes of things -> classification
"""

from typing import List
import numpy as np

from train import train
from nn import NeuralNet
from layer import Linear, Tanh

# codec dealing with output
def fizz_buzz_encode(x: int) -> List[int]:
    if x % 15 == 0:
        return [0, 0, 0, 1]
    elif x % 5 == 0:
        return [0, 0, 1, 0]
    elif x % 3 == 0:
        return [0, 1, 0, 0]
    else:
        return [1, 0, 0, 0]


# now what to do with input
# can't train on 1 to 100 (actual set under consideration),
# so  we'll train on numbers bigger than 100
def binary_encode(x: int) -> List[int]:
    """
    10 digit binary enconding of x
    """
    return [x >> i & 1 for i in range(10)]


# train numbers bigger than 100
inputs = np.array([binary_encode(x) for x in range(101, 1024)])


targets = np.array([fizz_buzz_encode(x) for x in range(101, 1024)])

net = NeuralNet(
    [
        Linear(input_size=10, output_size=50),
        Tanh(),
        Linear(input_size=50, output_size=4),
    ]
)

train(net, inputs, targets, num_epochs=5000)

for x in range(1, 101):
    predicted = net.forward(binary_encode(x))
    predicted_idx = np.argmax(predicted)
    actual_idx = np.argmax(fizz_buzz_encode(x))
    labels = [str(x), "fizz", "buzz", "fizzbuzz"]
    print(x, labels[predicted_idx], labels[actual_idx])
