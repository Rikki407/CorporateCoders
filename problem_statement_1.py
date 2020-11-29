server = int(input())
input_array = []

for i in range(0, 5):
    ele = int(input())
    input_array.append(ele)


def updateServer(servers, input_array):
    if input_array[4] < 50:
        return servers / 2
    else:
        return 2 * servers + 1


print(updateServer(server, input_array))
