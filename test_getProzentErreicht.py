from Noten import getProzentErreicht, getNoteFromProzent
import pytest
import unittest

def test_getProzentErreicht__null_punkte():
    #Arrange
    punkteMaximal = 6
    punkteErreicht = 0
    sollProzent = 0
    #Act
    prozent = getProzentErreicht(punkteMaximal, punkteErreicht)
    #Assert
    assert prozent == sollProzent

def test_getProzentErreicht__volle_punkte():
    #Arrange
    punkteMaximal = 100
    punkteErreicht = 100
    sollProzent = 100
    #Act
    prozent = getProzentErreicht(punkteMaximal, punkteErreicht)
    #Assert
    assert prozent == sollProzent

def test_getProzentErreicht__75_prozent():
    #Arrange
    punkteMaximal = 100
    punkteErreicht = 75
    sollProzent = 75
    #Act
    prozent = getProzentErreicht(punkteMaximal, punkteErreicht)
    #Assert
    assert prozent == sollProzent

def test_getProzentErreicht__invalid_value_erreicht():
    #Arrange
    punkteMaximal = 6
    punkteErreicht = -1
    #Act
    with pytest.raises(ValueError):
        getProzentErreicht(punkteMaximal, punkteErreicht)
    #Assert

def test_getProzentErreicht__points_bigger_than_points_max():
    #Arrange
    punkteMaximal = 6
    punkteErreicht = 7
    #Act
    with pytest.raises(ValueError):
        getProzentErreicht(punkteMaximal, punkteErreicht)
    #Assert

def test_getProzentErreicht__points_max_less_than_six():
    #Arrange
    punkteMaximal = 5
    punkteErreicht = 0
    #Act
    with pytest.raises(ValueError):
        getProzentErreicht(punkteMaximal, punkteErreicht)
    #Assert

def test_getProzentErreicht__invalid_points_max():
    #Arrange
    punkteMaximal = "100"
    punkteErreicht = 25
    #Act
    with pytest.raises(TypeError):
        getProzentErreicht(punkteMaximal, punkteErreicht)
    #Assert

def test_getProzentErreicht__invalid_points():
    #Arrange
    punkteMaximal = 100
    punkteErreicht = "25"
    #Act
    with pytest.raises(TypeError):
        getProzentErreicht(punkteMaximal, punkteErreicht)
    #Assert

#############################

def test_getNoteFromProzent__ungenuegend_bottom():
    #Arrange
    prozentErreicht = 0
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "ungenügend"

def test_getNoteFromProzent__ungenuegend_top():
    #Arrange
    prozentErreicht = 29
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "ungenügend"

def test_getNoteFromProzent__mangelhaft_bottom():
    #Arrange
    prozentErreicht = 30
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "mangelhaft"

def test_getNoteFromProzent__mangelhaft_top():
    #Arrange
    prozentErreicht = 49
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "mangelhaft"

def test_getNoteFromProzent__ausreichend_bottom():
    #Arrange
    prozentErreicht = 50
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "ausreichend"

def test_getNoteFromProzent__ausreichend_top():
    #Arrange
    prozentErreicht = 66
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "ausreichend"

def test_getNoteFromProzent__befriedigend_bottom():
    #Arrange
    prozentErreicht = 67
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "befriedigend"

def test_getNoteFromProzent__befriedigend_top():
    #Arrange
    prozentErreicht = 80
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "befriedigend"

def test_getNoteFromProzent__gut_bottom():
    #Arrange
    prozentErreicht = 81
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "gut"

def test_getNoteFromProzent__gut_top():
    #Arrange
    prozentErreicht = 91
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "gut"

def test_getNoteFromProzent__sehr_gut_bottom():
    #Arrange
    prozentErreicht = 92
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "sehr gut"

def test_getNoteFromProzent_sehr_gut_top():
    #Arrange
    prozentErreicht = 100
    #Act
    note = getNoteFromProzent(prozentErreicht)
    #Assert
    assert note == "sehr gut"

def test_getNoteFromProzent__TypeError():
    #Arrange
    prozentErreicht = "35"
    #Act
    with pytest.raises(TypeError):
        getNoteFromProzent(prozentErreicht)
    #Assert

def test_getNoteFromProzent__minus_one():
    #Arrange
    prozentErreicht = -1
    #Act
    with pytest.raises(ValueError):
        getNoteFromProzent(prozentErreicht)
    #Assert

def test_getNoteFromProzent__hundred_one():
    #Arrange
    prozentErreicht = 101
    #Act
    with pytest.raises(ValueError):
        getNoteFromProzent(prozentErreicht)
    #Assert

if __name__ == '__main__':
    unittest.main()