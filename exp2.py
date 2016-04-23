import re
x = 'From cwenhjhjhjhjhjhjh@iupui.edu Thu Jan  3 16:23:48 2008'
#y = re.findall('(.*\S@\S+)',x)
y = re.findall('(\S+@\S+)',x)
print y