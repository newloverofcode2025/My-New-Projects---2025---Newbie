def gameResult(aliceValues, bobValues):
    # Step 1: Combine the values into a list of tuples (combinedValue, aliceValue, bobValue)
    combined = [(aliceValues[i] + bobValues[i], aliceValues[i], bobValues[i]) for i in range(len(aliceValues))]
    
    # Step 2: Sort the combined list in descending order of combinedValue
    combined.sort(reverse=True, key=lambda x: x[0])
    
    # Step 3: Simulate the game
    aliceScore, bobScore = 0, 0
    for i, (_, aliceVal, bobVal) in enumerate(combined):
        if i % 2 == 0:  # Alice's turn
            aliceScore += aliceVal
        else:           # Bob's turn
            bobScore += bobVal
    
    # Step 4: Determine the result
    if aliceScore > bobScore:
        return 1
    elif aliceScore < bobScore:
        return -1
    else:
        return 0