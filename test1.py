# te = 3 / 2
# print(te)
#
#
#
#
# a = [v for v in range(1,101)]
# a.sort()
# print("min:" + str(a[0]))
# print("min:" + str(min(a)))
# print("max:" + str(a[-1]))
#
# sum = 0
# for b in a:
#     sum += b
# print("sum:" + str(sum))
#
#
# c = list(range(1,21,2))
# print(c)


def test(a, b, c=''):
    if c:
        print(a + b + c)
    else:
        print(a + b)


test("aaa", "bbb")
