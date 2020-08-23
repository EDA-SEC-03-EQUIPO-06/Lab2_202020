def lessaverage(element1, element2):
    if float(element1["vote_average"]) < float(element2["vote_average"]):
        return True
    return False

def greateraverage(element1,element2):
    if float(element1["vote_average"]) > float(element2["vote_average"]):
        return True
    return False

def lesscount(element1, element2):
    if float(element1["vote_count"]) < float(element2["vote_count"]):
        return True
    return False

def greatercount(element1,element2):
    if float(element1["vote_count"]) > float(element2["vote_count"]):
        return True
    return False