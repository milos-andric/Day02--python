from time import sleep


def ft_progress(ranged):
    for i in ranged:
        print(str(i) + " / " + str(len(ranged)))
        yield i


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print(ret)
