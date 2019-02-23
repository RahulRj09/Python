#Subsets
class Subsets():
	def makeSubsets(self,main_set):
		sub_sets = []
		ms = set(main_set)
		sub_sets.append(ms)
		for num in main_set:
			temp = set([num])
			sub_sets.append(temp)
		for subset in range(2,len(main_set)):
			mainSet = main_set[:]
			if subset == 2:
				for index in range(len(mainSet)):
					element = mainSet.pop(0)
					for num in mainSet:
						temp = set([num,element])
						sub_sets.append(temp)
			elif subset == 3:
				mainSet1 = main_set[:]
				mainSet2 = main_set[:]
				mainSet3 = main_set[:]
				for x in mainSet1:
					for y in mainSet2:
						for z in mainSet3:
							temp = {x,y,z}
							if temp not in sub_sets:
								sub_sets.append(temp)
			elif subset == 4:
				mainSet1 = main_set[:]
				mainSet2 = main_set[:]
				mainSet3 = main_set[:]
				mainSet4 = main_set[:]
				for w in mainSet1:
					for x in mainSet2:
						for y in mainSet3:
							for z in mainSet4:
								temp = {w,x,y,z}
								if temp not in sub_sets:
									sub_sets.append(temp)
				
			
		
		return sub_sets
s = Subsets()
print(s.makeSubsets([1,2,3,4,5]))
