leiviskä = float(input("Anna leiviskät:"))
naula = float(input("Anna luodit:"))
luoti = float(input("Anna naulat:"))

g_luoti = luoti*13.3
g_naula = naula*(32*13.3)
g_leiviskä = leiviskä*(20*32*13.3)

yht = g_leiviskä+g_naula+g_luoti

print(f"Paino on nykymittoissa: {yht // 1000:.0f}kg ja {yht % 1000:.2f}g")
