# enable importing of custum package up one directory
import sys
sys.path.append("..")

# allows importing of package when running pytest from root dir
# another option is use "python -m pytest" instead 
sys.path.append(".")

# possible fix for relative paths when running pytest from root dir
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# import external packages
import numpy as np
import pandas as pd

# import local package
import package
package.module_1.print_1()
package.subpackage.module_a.print_a()

# read data
data = pd.read_csv("../data/raw/data.csv")
print(data)

# run function 
def sum(x: int, y: int, z: int) -> int:
    return x + y + z
print(f"the sum is: {sum(1,2,3)}")