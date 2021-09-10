# Step 1 receive user input, split by empty space.
# element 1 is n total judges, element 2 is loop max for judges with a score already

str1 = input().split(' ')
n = int(str1[0])
k = int(str1[1])

# Step 2 receive input k amount of times and store the aggregate of those ratings
totalPoints = 0
for i in range(k):
    r = int(input())
    totalPoints = totalPoints + r
    i += 1

# Step 3 Have a min/max variable where the difference of total judges and judges who have a score
unknownR = n-k

# Step 4 multiplied amount of missing scores by max score possible and min scores possible

minScore = -3
maxScore = 3
maxTotalPossible = totalPoints + (unknownR * maxScore)
minTotalPossible = totalPoints + (unknownR * minScore)

# Step 5 find average of both by dividing total number of judges
maxPossible = maxTotalPossible/n
minPossible = minTotalPossible/n

print(str(minPossible) + ' ' + str(maxPossible))
