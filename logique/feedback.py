def feedback(secret, comb):
    i = 0

    wellPlaced = 0
    goodColor  = 0

    setSecret = set()
    setComb = set()

    while(i < len(secret)):
        secretColor = secret[i]
        combColor = comb[i]

        if(secretColor == combColor):
            wellPlaced += 1
        else:
            setSecret.add(secretColor)
            setComb.add(combColor)
        
        i += 1

    goodColor = len(setComb.intersection(setSecret))

    return (wellPlaced, goodColor)