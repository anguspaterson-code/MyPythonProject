### This function takes the input of one number and squares it
def squareNum():
    num = input("What number would you like to square:" )
    ConvertNum = int(num)
    squarednum = ConvertNum * ConvertNum
    print(squarednum)
    return squarednum

### Runs the squared number function
squareNum()