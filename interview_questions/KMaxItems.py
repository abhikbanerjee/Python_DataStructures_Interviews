

# Given a list of animals , find the top K animals by frequency (max or min both can work)

animal_names = ["cat","mouse","horse", "cat", "cat", "elephant", "horse", "mouse", "crane", "jaguar", "cheetah", "mouse", "cat", "horse", "cheetah"]


def top_k_animals(animals=animal_names, max_animals=3):
	animals_dict = {}
	for animal in animals:
		if animal in animals_dict.keys():
			animals_dict[animal] += 1
		else:
			animals_dict[animal] = 1
	print(animals_dict)

	#  sort the dict using sorted
	sorted_animals = sorted(animals_dict.items(), key=lambda x: x[1], reverse=True)
	return [k[0] for k in sorted_animals[:max_animals]]


# call the top K animals from the list
print(top_k_animals(animal_names, 4))


# abc = ["ant", "cat", "mat", "dog"]
# abc.sort()
# print(abc)
