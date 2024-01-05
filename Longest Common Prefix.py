strings = list(input("Enter space seperated strings: ").split())

# find the minimum length string
min_str = strings[0]
for i in strings:
    if len(i) < len(min_str):
        min_str = i

# compare the min_str to the prefixes of all strings
count = 0
flag = 0
for i in range(len(min_str), 0, -1):
    for j in strings:
        if j[:i] == min_str[:i]:
            count += 1
        else:
            break

    if count == len(strings):
        print(min_str[:i])
        flag = 1
        break
    else:
        count = 0

if flag == 0:
    print("")
