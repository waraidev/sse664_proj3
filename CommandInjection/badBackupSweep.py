import subprocess

print("Zip Clean Up Tool: Which folder do you want to zip?")
path = input("Type in full folder path:")
zipName = input("What do you want to name your zip file?:")
cwd = path.replace(path.split('/')[-1], "")
print(cwd)

z = subprocess.Popen("zip -r %s %s" % (zipName, path), cwd=cwd, shell=True)
z.communicate()

r = subprocess.Popen("rm -r %s" % path, shell=True)
r.communicate()

if z.returncode is 0:
    print("%s Folder has been zipped!" % zipName.split('.')[0])
else:
    print("Path does not exist!")

if r.returncode is 0:
    print("%s Folder was deleted" % zipName.split('.')[0])
else:
    print("Error in deleting folder")