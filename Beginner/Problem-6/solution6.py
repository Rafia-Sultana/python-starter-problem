def isLandscape(width, height):
    if width > height :
        return "Landscape"
    else:
        return "Portrait"

print(isLandscape(800,600))
print(isLandscape(600,800))