game_config = (800, 600, 10)

try:
    game_config[0] = 1024

except TypeError:
    print("Error: system configration can not be altered.")