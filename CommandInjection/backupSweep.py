import os
from shutil import make_archive, move, rmtree

print("Zip Clean Up Tool: Which folder do you want to zip?")
path = input("Type in full folder path:")
folder = path.split('/')[-1]

# booleans to determine correct input
no_command = not path.__contains__(';')
no_admin = path.split('/')[1] == "Users"
is_filepath = len(path.split(' ')) == 1 and os.path.exists(path)

if no_admin and is_filepath and no_command:
    make_archive(folder, 'zip', path)
    move(os.getcwd() + "/%s.zip" % folder, path.replace(folder, "") + "/%s.zip" % folder)
    rmtree(path)

    print("\n%s Folder has been zipped!\nOriginal folder has been deleted!" % folder)
elif not no_admin:
    print("Must be a user folder")
else:
    print("Path does not exist! Hint: Path must not contain any spaces")
