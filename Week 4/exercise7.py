""""
Exercise 7: Converting from seconds to hh:mm:ss
@Author : Eduardo Alarcón
@version: 1.0
"""
time = int(input('Input the seconds you want to convert to the format hh:mm:ss: '))
hours = time // 3600
minutes = (time // 60)-(hours*60)
seconds = (time % 3600) - (minutes*60)

"""time %= 3600
minutes = time / 60
hours = time / 3600
time %= 60
print(hours)
print(minutes)
print(seconds)"""

print("%02i:%02i:%02i" % (hours, minutes, seconds))
