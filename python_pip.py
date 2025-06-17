import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))


#pip freeze
#pip freeze is a command used in Python's package management system, pip, to output a list of installed packages in a format that can be used to recreate the environment. This is particularly useful for sharing environments or for deployment purposes.

#Usage
#
#Unix/macOS
#
#Windows
#py -m pip freeze [options]
#Description
#Output installed packages in requirements format.
#
#packages are listed in a case-insensitive sorted order.
#
#Options
#
#-r, --requirement <file>
#Use the order in the given requirements file and its comments when generating output. This option can be used multiple times.
#
#(environment variable: PIP_REQUIREMENT)
#
#-l, --local
#If in a virtualenv that has global access, do not output globally-installed packages.
#
#(environment variable: PIP_LOCAL)
#
#--user
#Only output packages installed in user-site.
#
#(environment variable: PIP_USER)
#
#--path <path>
#Restrict to the specified installation path for listing packages (can be used multiple times).
#
#(environment variable: PIP_PATH)
#
#--all
#Do not skip these packages in the output: setuptools, pip, wheel, distribute
#
#(environment variable: PIP_ALL)
#
#--exclude-editable
#Exclude editable package from output.
#
#(environment variable: PIP_EXCLUDE_EDITABLE)
#
#--exclude <package>
#Exclude specified package from the output
#
#(environment variable: PIP_EXCLUDE)
#
#Examples
#Generate output suitable for a requirements file.
#
#
#Unix/macOS
#
#Windows
#C:\> py -m pip freeze
#docutils==0.11
#Jinja2==2.7.2
#MarkupSafe==0.19
#Pygments==1.6
#Sphinx==1.2.2
#Generate a requirements file and then install from it in another environment.
#
#
#Unix/macOS
#
#Windows
#env1\bin\python -m pip freeze > requirements.txt
#env2\bin\python -m pip install -r requirements.txt