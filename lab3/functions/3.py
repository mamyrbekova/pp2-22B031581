def solve(numheads, numlegs):
    legs = 2 * numheads
    extra = numlegs - legs
    rabbits = int(extra / 2)
    chickens = int(numheads - rabbits)
    print(chickens, rabbits)


numheads = 35
numlegs = 94
solve(numheads, numlegs)