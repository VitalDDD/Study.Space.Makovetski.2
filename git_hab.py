# Функція пори року
def pora_roku(n):
    if n==1 or n==2 or n==12:
        return "Winter"
    elif n==3 or n==4 or n==5:
        return "Spring"
    elif n == 6 or n == 7 or n == 8:
        return "Summer"
    else:
        return "Autumn"