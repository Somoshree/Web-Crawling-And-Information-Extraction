import urllib.request, urllib.error, urllib.parse
import ply.lex as lex
import ply.yacc as yacc
import re

result= {'moviename':'','genre':'','director':'','writers':'','producer':'','language':'','cast':'','storyline':'','boxoffice':'','runtime':'','youmaylike':dict(),'wheretowatch':''}
tokens = (
	'LMOVIENAME',
	'LDIRECTOR',
	'LGENRE',
	'RDP',
	'LPRODUCER',
	'RPRODUCER',
	'LSTORY',
	'LBOX',
	'LNAME',
	'LWRITER',
	'NAME',
	'LCREW',
	'RCREW',
	'LCHARACTER',
	'RCHARACTER',
	'LRUNTIME',
	'LLANG',
	'LLINK',
	'LMNAME',
	'WHERETOWATCH'
)  #list of tokens

def t_LMOVIENAME(t):
	r'\s*<meta\shttp\-equiv\=\"x\-ua\-compatible\"\scontent\=\"ie\=edge\">\s*<meta\sname\=\"viewport\"\scontent\=\"width\=device\-width\,\sinitial\-scale\=1\">\s*<title>'
	return t

def t_WHERETOWATCH(t):
	r'<affiliate\-icon\sname\=\"[(a-z|A-Z|\-|\:|\,|0-9)]*\"'
	return t

def t_LGENRE(t):
	r'\s*<div\sclass\=\"meta-label\ssubtle\"\sdata\-qa\=\"movie\-info\-item\-label\">Genre\:<\/div>\s*<div\sclass\=\"meta\-value\sgenre\"\sdata\-qa\=\"movie\-info\-item\-value\">\s*'
	return t

def t_LDIRECTOR(t):
	r'<a\shref\=\"[(a-z|A-Z|0-9|\/|\;|\:|\_|\-|\,|\.)]*\"\sdata-qa="movie-info-director">'
	return t

def t_RDP(t):
	r'<\/a>'
	return t

def t_LBOX(t):
	r'\s*<div\sclass\=\"meta-label\ssubtle\"\sdata\-qa\=\"movie-info-item-label\">Box\sOffice\s\(Gross\sUSA\)\:<\/div>\s*<div\sclass\=\"meta\-value\"\sdata\-qa\=\"movie\-info\-item\-value\">'
	return t

def t_LPRODUCER(t):
	r'\s*<div\sclass\=\"meta-label\ssubtle\"\sdata-qa\=\"movie-info-item-label\">Producer\:<\/div>\s*<div\sclass\=\"meta-value\"\sdata-qa\=\"movie-info-item-value\">\s*'
	return t

def t_RPRODUCER(t):
	r'\s*<\/div>'
	return t

def t_LSTORY(t):
	r'\s*<div\sid\=\"movieSynopsis\"\sclass\=\"movie_synopsis\sclamp\sclamp\-6\sjs\-clamp\"\sstyle\=\"clear\:both\"\sdata-qa\=\"movie-info-synopsis\">\s*'
	return t

def t_LNAME(t):
	r'\,?\s*<a\shref\=\"\/celebrity\/[(a-z|A-Z|0-9|\/|\:|\_|\-|\s)]*\">'
	return t

def t_LWRITER(t):
	r'\s*<div\sclass\=\"meta-label\ssubtle\"\sdata-qa\=\"movie-info-item-label\">Writer\:<\/div>\s*<div\sclass\=\"meta-value\"\sdata-qa\=\"movie-info-item-value\">\s*'
	return t

def t_NAME(t):
	r'[(a-z|A-Z|\s|0-9|\,|\'|\.|\$|\-|\(|\)|\#|\&|\;|\:|\!|\u00C0-\u00CF|\u00D0-\u00DF|\u00E0-\u00EF|\u00F0-\u00FF)]*[(a-z|A-Z|0-9|\,|\!|\'|\.|\$|\s|\-|(|\)|\#|\&|\;|\:|\u00C0-\u00CF|\u00D0-\u00DF|\u00E0-\u00EF|\u00F0-\u00FF)]'
	return t

def t_LCREW(t):
	r'\s*(<a\shref\=\"[(a-z|A-Z|0-9|\/|\_|\-|\:|\s)]*\"\sclass\=\"unstyled\sarticleLink\"\s*data-qa\=\"cast-crew-item-link\">)*\s*<span\s*title\=\"[(a-z|A-Z|0-9|\,|\-|\_|\'|\.|\:|\;\s|\#|\&|\u00C0-\u00CF|\u00D0-\u00DF|\u00E0-\u00EF|\u00F0-\u00FF)]*\">\s*'
	return t

def t_RCREW(t):
	r'\s*<\/span>\s*(</a>\s*)*'
	return t

def t_LCHARACTER(t):
	r'\s*<span\s*class\=\"characters\ssubtle\ssmaller\"\s*title\=\"[(a-z|A-Z|0-9|\,|\-|\_|\'|\.|\:|\;|\s|\#|\&|\u00C0-\u00CF|\u00D0-\u00DF|\u00E0-\u00EF|\u00F0-\u00FF)]*\">\s*<br\/>\s*'
	return t

def t_RCHARACTER(t):
	r'\s*(<br\/>)*\s*[(a-z|A-Z|0-9|\s)]*<\/span>'
	return t

def t_LRUNTIME(t):
	r'\s*<div\sclass\=\"meta\-label\ssubtle\"\sdata\-qa\=\"movie\-info\-item\-label\">Runtime\:<\/div>\s*<div\sclass\=\"meta\-value\"\sdata\-qa\=\"movie\-info\-item\-value\">\s*<time\sdatetime\=\"[(a-z|A-Z|0-9|\s)]*\">\s*'
	return t

def t_LLANG(t):
	r'\s*<div\sclass\=\"meta\-label\ssubtle\"\sdata\-qa\=\"movie\-info\-item\-label\">Original\sLanguage\:<\/div>\s*<div\sclass\=\"meta\-value\"\sdata\-qa\=\"movie\-info\-item\-value\">'
	return t

def t_LLINK(t):
	r'<a\shref\=\"[(a-z|A-Z|0-9|\/|\_|\-)]*\"\sclass\=\"recommendations\-panel\_\_poster\-link">'
	return t

def t_LMNAME(t):
	r'<span\sslot\=\"title\"\sclass\=\"recommendations\-panel\_\_poster\-title\">'
	return t

def t_error(t):
	t.lexer.skip(1)

#Parsing rules

def p_start(t):
	'''start : moviename
						| genre
						| director
						| writers
						| producer
						| cast
						| story
						| boxofc
						| runtime
						| language
						| youmaylike
						| wheretowatch'''
	pass

def p_empty(p):
	'empty :'
	pass
 
def p_moviename(t):
 	'moviename : LMOVIENAME NAME'
 	t[2]=re.sub("&#39;","'",t[2])  #replace &#39; with apostrophe
 	t[2]=re.sub("&amp;","&",t[2])  #replace &amp; with &
 	global result
 	listitems=str(t[2]).split('-')
 	s=""
 	for i in range(0,len(listitems)-1):
 		if i!=0:
 			s=s+"-"+listitems[i]
 		else:
 			s+=listitems[i]
 	if result['moviename']=='':
 		result['moviename']=s
 	else:
 		result['moviename']=result['moviename']+s

def p_genre(t):
	'genre : LGENRE NAME RPRODUCER'
	t[2]=re.sub("&#39;","'",t[2])  #replace &#39; with apostrophe
	t[2]=re.sub("&amp;","&",t[2])  #replace &amp; with &
	global result
	result['genre']=str(t[2])

def p_wheretowatch(t):
	'wheretowatch : WHERETOWATCH'
	global result
	if result['wheretowatch'] == '':
		result['wheretowatch']=str(t[1]).split('"')[1]
	else:
		result['wheretowatch']=result['wheretowatch']+"\n"+str(t[1]).split('"')[1]

def p_director(t):
	'director : LDIRECTOR NAME RDP'
	t[2]=re.sub("&#39;","'",t[2])  #replace &#39; with apostrophe
	t[2]=re.sub("&amp;","&",t[2])  #replace &amp; with &
	global result
	if result['director']=='':
		result['director']=str(t[2])
	else:
		result['director']=result['director']+", "+str(t[2])

def p_producer(t):
	'producer : LPRODUCER LNAME NAME RDP names RPRODUCER'
	t[3]=re.sub("&#39;","'",t[3])  #replace &#39; with apostrophe
	t[3]=re.sub("&amp;","&",t[3])  #replace &amp; with &
	global result
	if result['producer']=='':
		result['producer']=str(t[3])+", "+str(t[5])
	else:
		result['producer']=result['producer']+", "+str(t[3])+", "+str(t[5])

def p_writers(t):
	'writers : LWRITER LNAME NAME RDP names RPRODUCER'
	t[3]=re.sub("&#39;","'",t[3])  #replace &#39; with apostrophe
	t[3]=re.sub("&amp;","&",t[3])  #replace &amp; with &
	global result
	if result['writers']=='':
		result['writers']=str(t[3])+", "+str(t[5])
	else:
		result['writers']=result['writers']+", "+str(t[3])+", "+str(t[5])

def p_story(t):
	'story : LSTORY names RPRODUCER'
	global result
	if result['storyline']=='':
		result['storyline']=str(t[2])
	else:
		result['storyline']=result['storyline']+str(t[2])

def p_cast(t):
	'cast : LCREW NAME RCREW LCHARACTER names rchar'
	t[2]=re.sub("&#39;","'",t[2])  #replace &#39; with apostrophe
	t[2]=re.sub("&amp;","&",t[2])  #replace &amp; with &
	global result
	if result['cast']=='':
		result['cast']=str(t[2])+" as "+str(t[5])
	else:
		result['cast']=result['cast']+" | "+str(t[2])+" as "+str(t[5])

def p_language(t):
	'language : LLANG NAME'
	t[2]=re.sub("&#39;","'",t[2])  #replace &#39; with apostrophe
	t[2]=re.sub("&amp;","&",t[2])  #replace &amp; with &
	global result
	result['language']=str(t[2])

def p_boxofc(t):
	'boxofc : LBOX NAME RPRODUCER'
	t[2]=re.sub("&#39;","'",t[2])  #replace &#39; with apostrophe
	t[2]=re.sub("&amp;","&",t[2])  #replace &amp; with &
	global result
	result['boxoffice']=str(t[2])

def p_runtime(t):
	'runtime : LRUNTIME NAME'
	global result
	result['runtime']=str(t[2])

def p_youmaylike(t):
	'youmaylike : LLINK names LMNAME NAME RCREW'
	t[4]=re.sub("&#39;","'",t[4])  #replace &#39; with apostrophe
	t[4]=re.sub("&amp;","&",t[4])  #replace &amp; with &
	global result
	temp=str(t[1])
	flag=0
	temp2=""
	for i in range(0,len(temp)):
		if temp[i]=='\"' and flag==0:
			flag=1
		elif flag==1:
			if temp[i] != '\"':
				temp2=temp2+temp[i]
			else:
				break
	movie_link="https://www.rottentomatoes.com"+temp2	
	result['youmaylike'][str(t[4])]=movie_link

def p_rchar_c(t):
	'rchar : RCHARACTER'

def p_rchar_crew(t):
	'rchar : RCREW'

def p_names(t):
	'names : LNAME NAME RDP names'
	t[2]=re.sub("&#39;","'",t[2])  #replace &#39; with apostrophe
	t[2]=re.sub("&amp;","&",t[2])  #replace &amp; with &
	t[0]=str(t[2])+","+str(t[4])

def p_names_empty(t):
	'names : empty'
	t[0]=''
def p_names_single(t):
	'names : NAME names'
	t[1]=re.sub("&#39;","'",t[1])  #replace &#39; with apostrophe
	t[1]=re.sub("&amp;","&",t[1])  #replace &amp; with &
	t[0]=t[1]


def p_error(t):
	pass

