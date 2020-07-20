import os
import subprocess
from shutil import make_archive, move

print("Zip Clean Up Tool: Which folder do you want to zip?")
path = input("Type in full folder path:")
folder = path.split('/')[-1]

if os.path.exists(path):
    make_archive(folder, 'zip', path)
    move(os.getcwd() + "/%s.zip" % folder, path.replace(folder, "") + "/%s.zip" % folder)
    subprocess.call(['rm', '-r', path])

    print("\n%s Folder has been zipped!\nOriginal folder has been deleted!" % folder)
else:
    print("Path does not exist!")
