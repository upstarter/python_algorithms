# Algorithmic Problem Solving & Design
## General Principles
1. Understand & Define the problem (hardest part, take your time)
  - conduct research
  - ask questions
  - explore givens, constraints, options, goals
  - decompose into subproblems
  - abstraction, analogy, metaphor
2. Representation
  - goals, targets, invariants
  - options, constraints, decisions
  - set of variables, relations, constraints, etc.
3. Approach / Strategy
  - recursive/iterative
  - divide and conquer
  - branch and bound
  - greedy
  - backtracking
  - dynamic programming (check relations between subproblems)
    - know the subproblems (most important thing)
    - table, grid, etc.
  - randomization
4. Construct Algorithm
5. Experiment (testing, time/space complexity improvements)
  - (B)ottlenecks
  - (U)nnecessary work
  - (D)uplicate work

## Practical Problem Solving Tips
1. Brute Force
2. Think of and Solve the simplest or different version of the problem, and expand
  1. how would you manually solve the simplest, solve larger version
  2. write out manual steps you took in step 1 above
  3. code above step by step
    - break into subproblems
    - use processed elements (seen, max_so_far, moving_avg, etc.)
    - use auxiliary data structure (map, tuple, set, stack, queue, heap, tree)
    - track multiple indices, vars, diffs, sums, counts, factors, multiples, remainders, divisors, stats, vectors
3. Think with simpler examples -> try noticing a pattern
  - reduce number of elements
4. Use Visualization
  - grid, table, mapping, tree, etc.
5. Test solution on a few examples

## Sequences

- will sorting help?
- use dict/set for previously processed elements
- use multiple pointers(indices)
- map to counts using collections.counter
- contiguous sequences
  - sliding window

#### Max Contiguous Subarray Sum
  - break into subproblems
    - what is max contiguous sum we can achieve with the subsequence ENDING at each index (largest sum ending at index)
    1. what is max previously processed sum
    2. choices at each element - `max(max_here, max_seen_so_far)`

### Sliding Window Technique
- good for contiguous sequence problems
  - strings, arrays, linked lists
- string permutations

#### When to use
  - everything grouped sequentially
  - min, max, running avg, longest, shortest, contained, etc..

##### Fixed Variant
  - window same size always

##### Dynamic variant
  - window not fixed size k, grows and shrinks during processing
  - longest substring w/ no more than k distinct characters (track occurences of chars in map)

### String Searching
- tradeoff storage for speed by using stack, map, etc.. or vice versa
- use multiple indices
- map chars to counts using collections.counter

## Greedy
- choose best possible choice as you go, never reconsidering choices (main difference from dynamic programming, which is exhaustive and guaranteed to find a solution)
- optimal substructure - globally optimal solution contains local optimal solutions to subproblems
  - **Examples**
    - Activity Selection Problem
    - Huffman coding
    - Job Sequencing
    - Fractional Knapsack
    - Primms minimum spanning tree

# Seeing the End Game - **Retrograde Analysis**
## Working backwards to solve problems

### Chess Grandmaster Techniques

1. Chunking
  - possibilities for group of chess pieces
2. Pattern Recognition
  - a lot of positions that look similar, extrapolate from that
3. Stepping Stone method
  - freeze a position in your mind, guess the next position, repeat
4. Retrograde Analysis (it pays to look backward)

### Toward the end game of chess, grandmaster games often boil down to simple board layouts with simple tactically oriented pockets
  - grandmasters study these simple layouts
  - when your checkmate , it's because i knew where you were going

### After reading this sentence, you will realize that the the brain doesn't recognize a second 'the'.
  - but if you read it backwards, you would automatically get it, great for proofreading

### Bacteria that double every 24 hours fill a lake it has infested after precisely 60 days. On what day was the lake half-full?
  - if you do it backwards, you get to the answer right away, 60 / 2 = day 30

RA Used in:
- Law
- Science
- Medicine
- Insurance
- Finance
- Politics
- Career Planning
