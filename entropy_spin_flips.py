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

# Main
spins = []
for i in range(50):
	spins.append(1)

print("Press Enter for the next round; type exit() to exit.")
print(string_from_spins(spins))

while 1 == 1:
	i = input("")
	if i == "exit()":
		break

	for s in range(len(spins)):
		if random.random() > 0.5:
			spins[s] = spins[s] * -1
	print(string_from_spins(spins))