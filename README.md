# Game Outcome Solution

This repository contains a Python implementation of a game outcome prediction problem. The goal is to determine the winner of a game where Alice and Bob take turns picking resources based on their perceived values.

## Problem Description
Alice and Bob take turns picking resources from a shared pool. Each resource has a value perceived differently by Alice and Bob. Both players play optimally, and the winner is determined by who accumulates the most points.

### Input:
- Two arrays, `aliceValues` and `bobValues`, representing the perceived values of resources by Alice and Bob.

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