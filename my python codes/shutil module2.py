#use of shutil.copy
# import shutil
# shutil.copy("shutil module.py","shutil module2.py")


# use of shutil.copy2

# import shutil
# shutil.copy2("shutil module.py","shutil module2.py")


import shutil

source = r"C:\Users\Nitesh Singh Negi\OneDrive\Desktop\my code"
destination = r"C:\Users\Nitesh Singh Negi\OneDrive\Desktop\my python codes"

shutil.copytree(source, destination, dirs_exist_ok=True)
