height = float(input("Enter your height in meters: "))
if 1.6 < height < 1.9:
    print("Correct height to be an astronaut")
elif height <= 1.6:
    print("Below minimum astronaut height")
elif height >= 1.9:
    print("Above maximum astronaut height")
