import re

double_quote = "\""
print(double_quote)

raw_string = r"""
Literals: '. \n\t."*"
"""
print(raw_string)

# Only avialable in Python 3.6 or higher. "F-strings."
dict_ignames = {
    "Joachim Rives": "J_Rives",
    "Maximillan Rives": "M_Rives",
    "Johannes Martin Apilas": "vliantpigeon"
    }

# print(f"""
# In-game Names, in alphabetical order:
# Maximillan Rives:{dict_ignames[Maximillan Rives]},
# Joachim Rives:{dict_ignames[Joachim Rives]},
# Johannes Martin Apilas:{dict_ignames[Johannes Martin Apilas]}
# """)

# fstring = f"Has escape characters treated as strings: `{raw_String}`"

# Regular Expressions

str_regex_email = r"""
([a-zA-Z0-9_.]{1,32}?)
(@\w{1,32}\.[a-zA-Z]{1,8})
"""

str_regex_phone = r"""
\(?
(\d\d\d)
\)?
[\.\- ]
(\d\d\d)
[\.\- ]
(\d\d\d\d)
[\.\- ]{,4}
[ex|ext\.|x]?[ ]{,4}
(\d{1,4})?
"""
regex_email = re.compile(str_regex_email, (re.I | re.VERBOSE))
regex_phone = re.compile(str_regex_phone, (re.I | re.VERBOSE))

test_text = """
Running the Program
For an example, open your web browser to the No Starch Press contact page at https://nostarch.com/contactus/, press CTRL-A to select all the text on the page, and press CTRL-C to copy it to the clipboard. When you run this program, the output will look something like this:

Copied to clipboard:
800-420-7240
415-863-9900
415-863-9950
info@nostarch.com
media@nostarch.com
academic@nostarch.com
info@nostarch.com

Ideas for Similar Programs
Identifying patterns of text (and possibly substituting them with the sub() method) has many different potential applications. For example, you could:
"""

matchobject_email = regex_email.findall(test_text)
matchobject_phone = regex_phone.findall(test_text)

print("\nResults for Email\n", matchobject_email)
print("\nResults for Phone Numbers\n", matchobject_phone)
