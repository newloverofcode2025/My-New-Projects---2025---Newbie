# Game Outcome Solution

This repository contains a Python implementation of a game outcome prediction problem. The goal is to determine the winner of a game where Alice and Bob take turns picking resources based on their perceived values.

## Problem Description - Maximizing Resource Allocation
Alice and Bob are tasked with allocating resources from a shared pool to maximize their individual benefits. There are n resources available, each with a value that Alice and Bob perceive differently. The players take turns picking resources, starting with Alice.

You are given two integer arrays of length n, aliceValues and bobValues. Each aliceValues[i] and bobValues[i] represents how much Alice and Bob, respectively, value the i-th resource. Once a resource is picked, it cannot be chosen again.

The goal for both players is to maximize their total perceived value. Both players play optimally, meaning they always pick the resource that maximizes their advantage over the other player. If both players end up with the same total value, the game is considered a draw.

Your task is to determine the outcome of the game:

If Alice ends up with more value than Bob, return 1.
If Bob ends up with more value than Alice, return -1.
If both have the same total value, return 0.
### Input:
- Two arrays, `aliceValues` and `bobValues`, representing the perceived values of resources by Alice and Bob.

- Constraints:
n == aliceValues.length == bobValues.length
1 <= n <= 10^5
1 <= aliceValues[i], bobValues[i] <= 100

### Output:
- `1` if Alice wins.
- `-1` if Bob wins.
- `0` if the game results in a draw.

## Example Usage
```python
aliceValues = [5, 4, 3]
bobValues = [3, 5, 4]
print(gameResult(aliceValues, bobValues))  # Output: 0

## License
This project is open-source and available under the [MIT License](LICENSE).
