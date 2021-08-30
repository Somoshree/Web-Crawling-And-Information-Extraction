import urllib.request, urllib.error, urllib.parse
import ply.lex as lex
import ply.yacc as yacc
import re

result= {'moviename':'','director':'','writers':'','producer':'','language':'','cast':'','storyline':'','boxoffice':'','runtime':''}
tokens = (
	'L_MOVIENAME',
	'LDIRECTOR',
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
	'LLANG'
)  #list of tokens

def t_L_MOVIENAME(t):
	r'\s*<meta\shttp\-equiv\=\"x\-ua\-compatible\"\scontent\=\"ie\=edge\">\s*<meta\sname\=\"viewport\"\scontent\=\"width\=device\-width\,\sinitial\-scale\=1\">\s*<title>'
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
	r'[(a-z|A-Z|\s|0-9|\,|\'|\.|\$|\-|\(|\)|\#|\&|\;|\:|\u00C0-\u00CF|\u00D0-\u00DF|\u00E0-\u00EF|\u00F0-\u00FF)]*[(a-z|A-Z|0-9|\,|\'|\.|\$|\s|\-|(|\)|\#|\&|\;|\:|\u00C0-\u00CF|\u00D0-\u00DF|\u00E0-\u00EF|\u00F0-\u00FF)]'
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

def t_error(t):
	t.lexer.skip(1)

#Parsing rules

def p_start(t):
	'''start : moviename
						| director
						| writers
						| producer
						| cast
						| story
						| boxofc
						| runtime
						| language'''
	pass

def p_empty(p):
	'empty :'
	pass
 
def p_moviename(t):
 	'moviename : L_MOVIENAME NAME'
 	if result['moviename']=='':
 		result['moviename']=str(t[2]).split('-')[0]
 	else:
 		result['moviename']=result['moviename']+str(t[2]).split('-')[0]

def p_director(t):
	'director : LDIRECTOR NAME RDP'
	if result['director']=='':
		result['director']=str(t[2])
	else:
		result['director']=result['director']+", "+str(t[2])

def p_producer(t):
	'producer : LPRODUCER LNAME NAME RDP names RPRODUCER'
	if result['producer']=='':
		result['producer']=str(t[3])+", "+str(t[5])
	else:
		result['producer']=result['producer']+", "+str(t[3])+", "+str(t[5])

def p_writers(t):
	'writers : LWRITER LNAME NAME RDP names RPRODUCER'
	if result['writers']=='':
		result['writers']=str(t[3])+", "+str(t[5])
	else:
		result['writers']=result['writers']+", "+str(t[3])+", "+str(t[5])

def p_story(t):
	'story : LSTORY names RPRODUCER'
	if result['storyline']=='':
		result['storyline']=str(t[2])
	else:
		result['storyline']=result['storyline']+str(t[2])

def p_cast(t):
	'cast : LCREW NAME RCREW LCHARACTER names rchar'
	if result['cast']=='':
		result['cast']=str(t[2])+" as "+str(t[5])
	else:
		result['cast']=result['cast']+" | "+str(t[2])+" as "+str(t[5])

def p_language(t):
	'language : LLANG NAME'
	result['language']=str(t[2])

def p_boxofc(t):
	'boxofc : LBOX NAME RPRODUCER'
	result['boxoffice']=str(t[2])

def p_runtime(t):
	'runtime : LRUNTIME NAME'
	result['runtime']=str(t[2])

def p_rchar_c(t):
	'rchar : RCHARACTER'

def p_rchar_crew(t):
	'rchar : RCREW'

def p_names(t):
	'names : LNAME NAME RDP names'
	t[0]=str(t[2])+","+str(t[4])

def p_names_empty(t):
	'names : empty'
	t[0]=''
def p_names_single(t):
	'names : NAME'
	t[0]=t[1]


def p_error(t):
	pass


