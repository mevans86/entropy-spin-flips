import random

def string_from_spins(spins):
	out = ""
	for s in spins:
		if s > 0:
			out += "↑"
		else:
			out += "↓"
	return out

spins = []
for i in range(20):
	spins.append(1)

print("Press Enter for the next round; type exit() to exit.")
while 1 == 1:
	i = input("")
	if i == "exit()":
		break

	for s in range(20):
		if random.random() > 0.5:
			spins[s] = spins[s] * -1
	print(string_from_spins(spins))