import time
import getpass


# import getpass.getuser to  print the function creator
# import time in order to use time.ctime() function to see the creation date


FunctionBody = '''Created on {0} by {1},
This function was made for....,
Global variables ,{{,,{2},,}},
Local variables,{{,,{3},,}}
,,{{
,,, 
Your code here.
,,,}}'''.replace(',', '\n')    # replace all  COMMA(or any caracter of your choice) in the funtion body with a new line("\n")


class MainGenerator():

    def __init__(self):
        self.x = 50
        self.globalV = "unsigned CHECK_MOTOR_SLV"
        self.localV = "String Diag_SET_PARAM"

    def __str__(self):
        return(FunctionBody.format(time.ctime(), getpass.getuser(), self.globalV, self.localV))


const = MainGenerator()
print(const)

# transform the const object to a string in order to export it( if not file.write will see the const as a class object and it will not be able to export it)
fileExport = str(const)


file = open('FunctionName.txt', 'w')
file.write(fileExport)
file.close
