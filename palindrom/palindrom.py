def func_p(word):
    print(word[::-1])
    a = word[::-1]
    if word == a:
        print("yes")
    else:
        print("no")

func_p(str(input()))