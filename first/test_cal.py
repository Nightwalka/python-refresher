from calculator import square 
import pytest 
def main ():
    test_square()


def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negetive():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(0) == 0
#     assert square(-2) == 4
#     assert square(-3) == 9
    # assert square("cat") == 0
  




























#     try:
    
#         assert square(2) == 4
#     except  AssertionError:
#         print("2 sq is not 4")
 
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 sq is not 9")


#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 sq is not 0")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 sq is not 9")


    # if square(2) !=4:
    #     print("2 sq is not 4")

    # if square(3) !=9:
    #     print("3 sq is not 9")


if __name__ == "__main__":
    main()
