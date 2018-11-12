import clipboard as cp


maglink = input("Please type in words you think is magnet:")
tmp = "magnet:?xt=urn:btih:"
result = tmp + maglink
# try to employ clipboard function......
print(result)
cp.copy(result)
