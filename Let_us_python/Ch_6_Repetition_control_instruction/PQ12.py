for i in range(1,25):
    if i<12:
        print(f"{i}:00","AM")
    elif i==12:
        print(f"{i}:00","Noon")
    elif i>12:
        print(f"{i}:00","PM")
        i+=1