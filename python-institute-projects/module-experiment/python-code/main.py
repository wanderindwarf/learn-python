from sys import path


path.insert(0, "./python-institute-projects/module-experiment/modules")


from module import prodl, suml


ones_list = [1 for _ in range(5)]

print(prodl(ones_list), suml(ones_list), sep='\n')