import requests, json, os, pprint
#DEBUGGING 
debug =  False
#CACHE CHECKING
def cache_check(file_name,url,debug):
	value = os.path.exists('cache/' + file_name)
	if value == True and debug == True:
		json_data = open('cache/' + file_name).read()
		json_data = json.loads(json_data)
	else:
		raw =  requests.get(url)
		json_data = json.loads(raw.text)
		with open('cache/' + file_name,'w') as file:
			json.dump(json_data,file)
		json_data = open('cache/' + file_name).read()
		json_data = json.loads(json_data)
	return json_data
#FIRST
def first_run(debug):
    #file name
	file_name = 'courses.json'
	#url
	url = 'http://saral.navgurukul.org/api/courses'
	#checking cache
	json_data = cache_check(file_name,url,debug)
	#printing a list of available courses	
	courses = json_data["availableCourses"]
	for course in courses:
		print(str(courses.index(course) + 1) + ". " + str(course['name']))
	#user input
	user_input = int(input('\n\nChoose any Course:(example : 1)\n>>>'))
	#finding id
	id = courses[user_input-1]['id']
    #url
	url = 'http://saral.navgurukul.org/api/courses/{}/exercises'.format(id)
	#file name
	file_name = 'exercises_' + str(id) + '.json' 
	#checking cache
	json_data = cache_check(file_name,url,debug)
	data = json_data["data"]
	for exercises in data:
		index_1 = str(data.index(exercises)+1) +". " 
		print(index_1 + exercises["name"])
		if exercises['childExercises'] != []:
			for exercise in exercises['childExercises']:
				index = str(exercises['childExercises'].index(exercise)+1) +" " 
				print("    " + index_1[:-1] + index + str(exercise['name']))
	#Slug
	user_input = (input("\n\nChoose any Exercise:(example: 1 or 1.1)\n>>>"))
	data = json_data["data"]
	if '.' in user_input:
		index_1 = int(user_input[0].strip()) - 1
		index = int(user_input[2].strip()) - 1
		slug = data[index_1]['childExercises'][index]['slug']
		file_name = 'content_' + str(index_1 + 1) + "_"+str(index + 1) +  '.json'
	else:
		index = int(user_input.strip()) - 1
		slug = data[index]['slug']
		file_name = 'content_' + str(index + 1) + '.json'
	url = 'http://saral.navgurukul.org/api/courses/{}/exercise/getBySlug?slug={}'.format(id,slug)
	contents = cache_check(file_name,url,debug)
	print(contents['content'])
	if '.' in user_input:
		return [id,index_1,index,data]
	else:
		return [id,index,data]
#next
def next(values):
	id = values[0]
	data = values[-1]
	if len(values) == 4:
		index_1 = int(values[1]) + 1
		index = int(values[2]) + 1
		slug = data[index_1]['childExercises'][index]['slug']
		file_name = 'content_' + str(index_1 + 1) + "_"+str(index + 1) +  '.json'
	else:
		index = int(values[1]) + 1
		slug = data[index]['slug']
		file_name = 'content_' + str(index + 1) + '.json'
	url = 'http://saral.navgurukul.org/api/courses/{}/exercise/getBySlug?slug={}'.format(id,slug)
	contents = cache_check(file_name,url,debug)
	print(contents['content'])
	if len(values) == 4:
		return [id,index_1,index,data]
	else:
		return [id,index,data]
#previous
def prev(values):
	id = values[0]
	data = values[-1]  
	if len(values) == 4:
		index_1 = int(values[1]) - 1
		index = int(values[2]) - 1
		slug = data[index_1]['childExercises'][index]['slug']
		file_name = 'content_' + str(index_1 + 1) + "_"+str(index + 1) +  '.json'
	else:
		index = int(values[1]) - 1
		slug = data[index]['slug']
		file_name = 'content_' + str(index + 1) + '.json'
	url = 'http://saral.navgurukul.org/api/courses/{}/exercise/getBySlug?slug={}'.format(id,slug)
	contents = cache_check(file_name,url,debug)
	print(contents['content'])
	if len(values) == 4:
		return [id,index_1,index,data]
	else:
		return [id,index,data]
values = first_run(debug)
while True:
	prompt  = '\n\nNavigations:\nu = Up\nn = Next\np = Previous\ne = Exit\n>>>'
	nav = input(prompt)
	if nav == 'u':
		values = first_run(debug)
	elif nav == 'n':
		values = next(values)
	elif nav == 'p':
		values = prev(values)
	elif nav == 'e':
		exit()
	else:
		exit()



