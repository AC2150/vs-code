def showtime(seconds):
    a=str (seconds // 3600)
    b=str (seconds % 3600 // 60)
    c=str (seconds % 3600 % 60)
    return "{:02}:{:02}:{:02}".format(a,b,c)

print (showtime(500))


