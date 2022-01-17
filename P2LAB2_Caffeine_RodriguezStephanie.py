caffeine_mg = float(input())

x = 2

half_life = caffeine_mg / x

half_life2 = half_life / x

half_life3 = (half_life2 / x) / x

print('After 6 hours: ' , format(half_life, ".2f"), ' mg', sep="")

print('After 12 hours: ' , format(half_life2, ".2f"), ' mg', sep="")

print('After 24 hours: ' , format(half_life3, ".2f"), ' mg', sep="")

