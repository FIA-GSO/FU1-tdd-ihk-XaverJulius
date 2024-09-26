def getProzentErreicht(points_max: int, points: int):

    if type(points) != int:
        raise TypeError("Points is not an int")
    
    if type(points_max) != int:
        raise TypeError("Points max is not an int")
    
    if points < 0:
        raise ValueError("Points is less than zero")

    if points_max < points:
        raise ValueError("Points max is less than points")
    
    if points_max < 6:
        raise ValueError("Points max is less than six")
    
    return int((points / points_max) * 100)

def getNoteFromProzent(percentage: float):

    if type(percentage) != int:
        raise TypeError("percentage is not an int")
    
    if percentage < 0:
        raise ValueError("percentage is less than 0")
    
    if percentage > 100:
        raise ValueError("percentage is higher than one hundred")
    
    if 92 <= percentage <= 100:
        return "sehr gut"
    
    if 81 <= percentage <= 91:
        return "gut"
    
    if 67 <= percentage <= 80:
        return "befriedigend"
    
    if 50 <= percentage <= 66:
        return "ausreichend"
    
    if 30 <= percentage <= 49:
        return "mangelhaft"
    
    if 0 <= percentage <= 29:
        return "ungenügend"
