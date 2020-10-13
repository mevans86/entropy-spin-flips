# See "16 Entropy and Probability" in
# Google Drive > CHEM 1310 > In-class Activities.

import random

def string_from_spins(spins):
	out = ""
	for s in spins:
		if s > 0:
			out += "↑"
		else:
			out += "↓"
	return out

def count_spins_string(spins):
	up = 0
	down = 0
	for s in spins:
		if s > 0:
			up = up + 1
		else:
			down = down + 1
	return (str(up) + "\t" + str(down))

# Main
spins = []
for i in range(50):
	spins.append(1)

print("↑\t↓")
print(count_spins_string(spins))

for x in range(500):
	for s in range(len(spins)):
		if random.random() > 0.5:
			spins[s] = spins[s] * -1
	print(count_spins_string(spins))