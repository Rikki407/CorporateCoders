# Python 3 code
server = int(input())
a, b, c, d, e = map(int, input().split())


def updateServer(servers, e):
    if e < 50:
        return int(servers / 2)
    else:
        return int(2 * servers + 1)


print(updateServer(server, e))
