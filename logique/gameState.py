def gameState(secret, line, currentLine):
    if(currentLine >= 16):
        return (True, False)
    
    i = 0

    while(i < len(secret)):
        if(secret[i] != line[i]):
            return (False, False)
        i += 1
        
    return (True, True)