version = input().split('.')
number = int(version[0] + version[1] + version[2]) + 1
new_version = str(number)
print('.'.join(new_version))

