import urllib.request, urllib.error, urllib.parse
from urllib.request import urlopen
import os.path
from os import path
import string
from task_grammar import *

def save_pages(url,nameofpage):   #saves the html webpage of a given url
	response = urllib.request.urlopen(url)
	webContent = response.read()
	f = open(nameofpage, 'wb')
	f.write(webContent)
	f.close()

def list_movies():   #lists out all the genres and prompts the user to pick one
	genre = input("Enter a genre of your choice from the below mentioned list of genres in the exact format as mentioned below or enter 'E' to exit:\n\
	 	1. Action and adventure\n\
	 	2. Animation \n\
	 	3. Drama \n\
	 	4. Comedy \n\
	 	5. Mystery and suspense \n\
	 	6. Horror \n\
	 	7. Sci-fi \n\
	 	8. Documentary \n\
	 	9. Romance \n\
	 	10. Classics \n")
	if genre == 'E':
		exit()
	if genre=="Action and adventure":
		f=open('top_100_action__adventure_movies.html','r')
		return f,"Action and adventure"
	elif genre=="Animation":
		f=open('top_100_animation_movies.html','r')
		return f,"Animation"
	elif genre=="Drama":
		f=open('top_100_drama_movies.html','r')
		return f,"Drama"
	elif genre=="Comedy":
		f=open('top_100_comedy_movies.html','r')
		return f,"Comedy"
	elif genre=="Mystery and suspense":
		f=open('top_100_mystery__suspense_movies.html','r')
		return f,"Mystery and Suspense"
	elif genre=="Horror":
		f=open('top_100_horror_movies.html','r')
		return f,"Horror"
	elif genre=="Sci-fi":
		f=open('top_100_scifi_movies.html','r')
		return f,"Sci-fi"
	elif genre=="Documentary":
		f=open('top_100_documentary_movies.html','r')
		return f,"Documentary"
	elif genre=="Romance":
		f=open('top_100_romance_movies.html','r')
		return f,"Romance"
	elif genre=="Classics":
		f=open('top_100_classics_movies.html','r')
		return f,"Classics"
	else:
		print("Wrong genre entered!Please enter a correct genre from the above list!\n")
		f1,genre1=list_movies()
		return f1,genre1
	
def main():
	#crawls all the webpages at once and stores them if they are not already stored
	print("Started crawling...")
	if path.exists('top_100_action__adventure_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/','top_100_action__adventure_movies.html')
	if path.exists('top_100_animation_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/','top_100_animation_movies.html')
	if path.exists('top_100_drama_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_drama_movies/','top_100_drama_movies.html')
	if path.exists('top_100_comedy_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_comedy_movies/','top_100_comedy_movies.html')
	if path.exists('top_100_mystery__suspense_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_mystery__suspense_movies/','top_100_mystery__suspense_movies.html')
	if path.exists('top_100_horror_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_horror_movies/','top_100_horror_movies.html')
	if path.exists('top_100_scifi_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_science_fiction__fantasy_movies/','top_100_scifi_movies.html')
	if path.exists('top_100_documentary_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_documentary_movies/','top_100_documentary_movies.html')
	if path.exists('top_100_romance_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_romance_movies/','top_100_romance_movies.html')
	if path.exists('top_100_classics_movies.html')==False:
		save_pages('https://www.rottentomatoes.com/top/bestofrt/top_100_classics_movies/','top_100_classics_movies.html')
	print("Crawling done!!!\n")
	f,genre=list_movies()
	movie_links=dict()   #dictionary used to store the movie links of the 100 movies of a particular genre as entered by user
	numlines=1
	while True:
		line = f.readline()
		if not line:
			break #end of file reached
		line=line.strip()
		if (line.find('class=\"unstyled articleLink\"') != -1) and line.strip().startswith('<a href'):
			_,href,_,_=line.split(' ')
			href=href.replace('href=\"','')
			href=href.replace('\"','')
			moviename=f.readline()
			moviename=moviename.strip()
			moviename=moviename.replace('</a>','')
			movie_links[moviename]="https://www.rottentomatoes.com/"+href
			print(str(numlines)+". "+moviename)   #prints the movies under a given genre one by one
			numlines+=1
	f.close()
	print()
	mvname=input("Enter a movie name from the above list of movies in the exact format as mentioned above or enter 'E' to exit!\n")
	if mvname=='E':
		exit()
	flag=0
	actual_moviename=''
	while flag==0:
		for key,value in movie_links.items():
			if key.lower()==mvname.lower():
				flag=1
				actual_moviename=key
				response=urllib.request.urlopen(value)
				webContent=response.read()
				f=open(mvname+'.html','wb')
				f.write(webContent)
				print("The corresponding movie page's HTML file has been saved successfully!\n")  #saves the html webpage of the corresponding movie entered by the user
				f.close()
				break
		if flag==0:
			mvname=input("The movie name that you entered wasn't found!Please enter a correct movie name from the list of movies shown to you earlier or enter 'E' to exit!\n")
			if mvname=='E':
				exit()
	name=mvname+'.html'
	print("Parsing the HTML file...\n")
	with open(name, 'r') as myfile:
		data = myfile.read()
		lexer = lex.lex()   #lexical analyzer that generates the tokens
		parser = yacc.yacc()  
		parser.parse(data)   #parses the html webpage
	print("Parsing completed!!\n")
	fileptr=open("result_log.txt","a+")
	while True:
		field_name = input("Enter the field name that you wish to view for your movie named: "+actual_moviename+". Enter a field from the following list of choices:\n\
			1. Movie name \n\
			2. Director \n\
			3. Writers \n\
			4. Producer \n\
			5. Original Language \n\
			6. Cast and Crew \n\
			7. Storyline \n\
			8. Box office collection \n\
			9. Runtime \n\
			10. You May Also Like \n\
			11. Where To Watch \n\
			Press 'E' to exit and query details about another movie!\n")
		if field_name=='E':
			break
		list_of_genres=result['genre'].split(',')
		genre=""
		if len(list_of_genres)==1:
			genre=list_of_genres[0].strip()
		else:
			for i in range(0,len(list_of_genres)-1):
				genre=genre+list_of_genres[i].strip()+", "
			genre=genre+list_of_genres[len(list_of_genres)-1].strip()
		if "movie name"==field_name.lower():   #field name to be retrieved is movie name
			print("Movie Name : ",result['moviename']+"\n")
			fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Movie Name"+">"+" <"+result['moviename']+">\n")
		elif "director"==field_name.lower():  #field name to be retrieved is director
			list_of_directors=result['director'].split(',')
			if len(list_of_directors)==0:
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Director"+">"+" <"+"Couldn't be retrieved"+">\n")
				print("Directors' names couldn't be retrieved!\n")
				continue
			for item in list_of_directors:
				if item.strip() != '':
					fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Director"+">"+" <"+item.strip()+">\n")
			if len(list_of_directors)==2:
				if list_of_directors[0].strip() != '' and list_of_directors[1].strip() != '':
					print("Directors' Names: ",result['director']+"\n")
				elif list_of_directors[0].strip() != '':
					print("Directors' Names: ",list_of_directors[0]+"\n")
				else:
					print("Directors' Names: ",list_of_directors[1]+"\n")
			else:
				for i in range(0,len(list_of_directors)-1):
					if i==0 and list_of_directors[i].strip() != '':
						print("Directors' Names : ",list_of_directors[i]+", ",end='')
					elif i==len(list_of_directors)-2 and list_of_directors[i].strip() != '':
						print(list_of_directors[i],end='')
					elif list_of_directors[i].strip() != '':
						print(list_of_directors[i]+", ",end='')
				if len(list_of_directors)==1 and list_of_directors[0].strip() != '':
					print("Directors' Names : ",list_of_directors[0])
				elif list_of_directors[-1].strip() != '':
					print(", "+list_of_directors[-1])
				print("\n")
		elif "writers"==field_name.lower():  #field name to be retrieved is writer
			list_of_writers=result['writers'].split(',')
			if len(list_of_writers)==0 or result['writers']=='':
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Writer"+">"+" <"+"Couldn't be retrieved"+">\n")
				print("Writers' names couldn't be retrieved!\n")
				continue
			for item in list_of_writers:
				if item.strip() != '':
					fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Writer"+">"+" <"+item.strip()+">\n")
			if len(list_of_writers)==2:
				if list_of_writers[0].strip() != '' and list_of_writers[1].strip() != '':
					print("Writers' Names: ",result['writers']+"\n")
				elif list_of_writers[0].strip() != '':
					print("Writers' Names: ",list_of_writers[0]+"\n")
				else:
					print("Writers' Names: ",list_of_writers[1]+"\n")
			else:
				for i in range(0,len(list_of_writers)-1):
					if i==0 and list_of_writers[i].strip() != '':
						print("Writers' Names : ",list_of_writers[i]+", ",end='')
					elif i==len(list_of_writers)-2 and list_of_writers[i].strip() != '':
						print(list_of_writers[i],end='')
					elif list_of_writers[i].strip() != '':
						print(list_of_writers[i]+", ",end='')
				if len(list_of_writers)==1 and list_of_writers[0].strip() != '':
					print("Writers' Names : ",list_of_writers[0])
				elif list_of_writers[-1].strip() != '':
					print(", "+list_of_writers[-1])
				print("\n")
		elif "producer"==field_name.lower():   #fieldname to be retrieved is producer
			list_of_producers=result['producer'].split(',')
			if len(list_of_producers)==0:
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Producer"+">"+" <"+"Couldn't be retrieved"+">\n")
				print("Producer name couldn't be retrieved!\n")
				continue
			for item in list_of_producers:
				if item.strip() != '':
					fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Producer"+">"+" <"+item.strip()+">\n")
			if len(list_of_producers)==2:
				if list_of_producers[0].strip() != '' and list_of_producers[1].strip() != '':
					print("Producers' Names: ",result['producer']+"\n")
				elif list_of_producers[0].strip() != '':
					print("Producers' Names: ",list_of_producers[0]+"\n")
				else:
					print("Producers' Names: ",list_of_producers[1]+"\n")
			else:
				for i in range(0,len(list_of_producers)-1):
					if i==0 and list_of_producers[i].strip() != '':
						print("Producers' Names : ",list_of_producers[i]+", ",end='')
					elif i==len(list_of_producers)-2 and list_of_producers[i].strip() != '':
						print(list_of_producers[i],end='')
					elif list_of_producers[i].strip() != '':
						print(list_of_producers[i]+", ",end='')
				if len(list_of_producers)==1 and list_of_producers[0].strip() != '':
					print("Producer Name : ",list_of_producers[0].strip(','))
				elif list_of_producers[-1].strip() != '':
					print(", "+list_of_producers[-1].strip(','))
				print("\n")
		elif "original language"==field_name.lower():  #field name to be retrieved is original language
			if result['language'] != '':
				print("Language : ",result['language']+"\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Original Language"+">"+" <"+result['language'].strip()+">\n")
			else:
				print("Language couldn't be retrieved!\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Original Language"+">"+" <"+"Couldn't be retrieved"+">\n")
		elif "cast and crew"==field_name.lower():   #field name to be retrieved is cast and crew
			if result['cast'] == '':
				print("Cast and crew information couldn't be retrieved!\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Cast and Crew"+">"+" <"+"Couldn't be retrieved"+">\n")
			else:
				print("Cast members : ")
				for s in result['cast'].split('|'):
					temp=" ".join(s.split("\n"))
					temp2=""
					for i in range(0,len(temp)):
						if temp[i] in string.whitespace and i+1<len(temp) and temp[i+1] in string.whitespace:
							continue
						else:
							temp2=temp2+temp[i]
					print(temp2+"\n")
					fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Cast and Crew"+">"+" <"+temp2.strip()+">\n")
		elif "storyline"==field_name.lower():   #field name to be retrieved is storyline
			if result['storyline'] != '':
				print("Storyline of the movie is : ")
				print(result['storyline']+"\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Storyline"+">"+" <"+result['storyline'].strip()+">\n")
			else:
				print("Storyline of the movie couldn't be retrieved!\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Storyline"+">"+" <"+"Couldn't be retrieved"+">\n")
		elif "box office collection"==field_name.lower():   #field name to be retrieved is box office
			if result['boxoffice'] != '':
				print("Box Office (Gross USA) : ",result['boxoffice']+"\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Box Office Collection"+">"+" <"+result['boxoffice'].strip()+">\n")
			else:
				print("Box office collection of the movie couldn't be retrieved!\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Box Office Collection"+">"+" <"+"Couldn't be retrieved"+">\n")
		elif "runtime"==field_name.lower():  #field name to be retrieved is runtime
			if result['runtime'] != '':
				print("Runtime: ",result['runtime']+"\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Runtime"+">"+" <"+result['runtime'].strip()+">\n")
			else:
				print("Runtime of the movie couldn't be retrieved!\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Runtime"+">"+" <"+"Couln't be retrieved"+">\n")
		elif "you may also like"==field_name.lower():  #field name to be retrieved is you may also like
			if result['youmaylike'] != {}:
				print("The movies that you may like are: \n")
				for key in result['youmaylike']:
					print(key+"\n")
					fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"You May Also Like"+">"+" <"+key+">\n")
				movie_name=input("Enter a movie name in the exact same format as displayed from the above enlisted movies or enter 'E' to exit!\n")
				if movie_name=='E':
					exit()
				flag=0
				while flag==0:
					for key,value in result['youmaylike'].items():
						if key.lower()==movie_name.lower():
							flag=1
							actual_moviename=key
							response=urllib.request.urlopen(value)
							webContent=response.read()
							f=open(movie_name+'.html','wb')
							f.write(webContent)
							print("The corresponding movie page's HTML file has been saved successfully!\n")  #saves the html webpage of the corresponding movie entered by the user
							f.close()
							break
					if flag==0:
						movie_name=input("The movie name that you entered wasn't found!Please enter a correct movie name from the list of movies shown to you earlier or enter 'E' to exit!\n")
						if movie_name=='E':
							exit()
				name=movie_name+'.html'
				print("Parsing the HTML file...\n")
				result['moviename']=''
				result['genre']=''
				result['director']=''
				result['writers']=''
				result['producer']=''
				result['language']=''
				result['cast']=''
				result['storyline']=''
				result['boxoffice']=''
				result['runtime']=''
				result['youmaylike']=dict()
				result['wheretowatch']=''
				with open(name, 'r') as myfile:
					data = myfile.read()
					lexer = lex.lex()   #lexical analyzer that generates the tokens
					parser = yacc.yacc()  
					parser.parse(data)   #parses the html webpage
				print("Parsing completed!!\n")
				actual_moviename=result['moviename']
				continue
		elif "where to watch"==field_name.lower():  #field name to be retrieved is where to watch
			if result['wheretowatch']!='':
				print("Available online platforms where the movie is streaming are:")
				l=result['wheretowatch'].split('\n')
				for item in l:
					print(item.strip()+"\n")
					fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Where To Watch"+">"+" <"+item+">\n")
			else:
				print("Available online platforms to watch the movie couldn't be retrieved!\n")
				fileptr.write("<"+genre+">"+" <"+actual_moviename+">"+" <"+"Where To Watch"+">"+" <"+"Couldn't be retrieved"+">\n")
		else:
			print("You entered an incorrect field name!\n")

	fileptr.close()
if __name__ == "__main__":
	main()
