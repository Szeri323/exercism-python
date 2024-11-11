def response(hey_bob):
    hey_bob = hey_bob.strip()
    
    if not hey_bob:
        return "Fine. Be that way!"
    if hey_bob.isupper():
        if hey_bob[-1] != "?":
            return "Whoa, chill out!"
        return "Calm down, I know what I'm doing!"
    if hey_bob[-1] == "?":
        return "Sure."    
    return "Whatever."
