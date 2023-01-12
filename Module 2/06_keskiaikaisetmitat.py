leiviskä = float(input("Anna leiviskät:"))
naula = float(input("Anna luodit:"))
luoti = float(input("Anna naulat:"))

g_luoti = luoti*13.3
g_naula = naula*(32*13.3)
g_leiviskä = leiviskä*(20*32*13.3)

yht = (g_leiviskä+g_naula+g_luoti)/1000

print(yht)
