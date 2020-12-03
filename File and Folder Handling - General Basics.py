from pathlib import Path
import os
import shelve
import pprint
import re

str_atbswp = r"D:\Online Module Notes\Assorted Code Files\Automate the Boring Stuff with Python"
path_atbswp = Path(str_atbswp)
# os.chdir(path_atbswp)
os.chdir(str_atbswp)

"""
Used IDLE.
When a generator object was created, its contents could only be
accessed once even if stored in a variable. After successfully
listing the contents of Path.glob(somePath) once, the next call
returned an empty list.
"""


def list_files(path_object, regex_pattern):
    filenames_list = list(path_object.glob(regex_pattern))

    print("""\n*Files Found using "{}":\n""".format(regex_pattern))

    for item in filenames_list:
        print(item, '\n')

    return filenames_list


list_files(path_atbswp, "*.py")
list_files(path_atbswp, "*")


def write_txt(
    str_filename="text.txt",
    str_text="Hello World!",
    path_object=Path.cwd()
        ):

    if isinstance(path_object, str):
        path_object = Path(path_object)

    path_object = path_object/str_filename
    chars_written = path_object.write_text(str_text)
    print("Done. Wrote", chars_written, "characters to", str_filename)
    return chars_written


"""
write_txt(path_atbswp, "test.txt", "Four")

Code not working even when copied literally from resource.

nearly all objects, notably file and generator (returned by glob) objects can
only be accessed once.
Two successive calls to same object return empty results for the second call.
"""

str_textpath = r"D:\Online Module Notes\Assorted Code Files\Automate the Boring Stuff with Python\text.txt"
# Only works on 3.6 and later.
# file_text = open(Path(str_path))
file_text = open(str_textpath)
# str_file = file_text.read() File object can only be accessed once
# print("File contents as string:\n", str_file)
lst_file = file_text.readlines()
print("File contents as list of each string after new line:\n")
for line in lst_file:
    print('\t', line)

# Create a shelf object to "persist" variables.
os.chdir(str_atbswp + r"/Shelves")
shelf_atbswp = shelve.open("FolderData")
shelf_atbswp["AllFilenames"] = list(Path(str_atbswp).glob("*"))
shelf_atbswp.close()
