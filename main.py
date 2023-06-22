import os
from enum import Enum
import re
import unicodedata
from fontTools.ttLib import TTFont
# from fontTools.otlLib import OTFont
current_dir = os. getcwd()

class file_or_filder(Enum):
    file = "file"
    folder = "folder"


def print_stx(text):
    try:
        print(text)
    except UnicodeEncodeError as e:
        encoded_text = text.encode('unicode_escape').decode('utf-8')
        print(encoded_text)



def char_in_font(unicode_char, font):
    for cmap in font['cmap'].tables:
        print(ord(unicode_char))
        # if cmap.isUnicode():
        if True:
            # print(ord(unicode_char))
            if ord(unicode_char) in cmap.cmap:
                # print(ord(unicode_char))
                return True
    return False




def find_files(filename, search_path, file_or_folder: file_or_filder):
    result = []

# Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if file_or_folder == file_or_filder.file:
            if filename in files:
                result.append(os.path.join(root, filename))
        elif file_or_folder == file_or_filder.folder:
        # else:
            if filename in dir:
                result.append(os.path.join(root, filename))
                
    if len(result) > 0:
        return result[0]
    else:
        return None

# lang_pattern = ":(.*$)"
lang_pattern = r":\s*(.*)"


print(os.listdir( current_dir+r"\langfile")[0])
langfile = current_dir+r"\langfile\\"+str(os.listdir( current_dir+r"\langfile")[0])
font_path = current_dir+r"\font\\"+str(os.listdir( current_dir+r"\font")[0])


if font_path.endswith(".otf") or font_path.endswith(".ttf"):
    font = TTFont(font_path)
else:
    raise ValueError("Unsupported font format. Only TTF and OTF are supported.")

print(langfile, font)
print()
print()
print()
o_lang = open(langfile, "r", encoding="utf-8")
o_lang_text = o_lang.read()
# all_matches = re.findall(lang_pattern, o_lang_text)

# bypass regex
all_matches = o_lang_text

print_stx(o_lang_text)
print()

list_missing = []


for i in range(1, len(all_matches)): 
    # print_stx(all_matches[i])
    for i2 in range(0, len(all_matches[i])):
        print()
        print_stx(all_matches[i][i2])
        # print(all_matches[i][i2])
        if not char_in_font(all_matches[i][i2], font):
            if not all_matches[i][i2] in list_missing:
                list_missing.append(all_matches[i][i2])

print()
print()
print()
print()
for i3 in range(0, len(list_missing) - 1):
    print_stx(list_missing[i3])
output = open(current_dir+r"\outfile.txt", "w+", encoding="utf-8")
output.write(str(list_missing))

debug1 = open(current_dir+r"\debug.txt", "w+", encoding="utf-8")
debug1.write(str(all_matches))