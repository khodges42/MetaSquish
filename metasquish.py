# -*- coding: utf-8 -*-
import sys
import re
import json
#Parses one file for unfinished URLs, and looks for finished URLs in another file with the image names.
import datetime
if len (sys.argv) != 3 :
	print "Usage: postmeta.sql outfile.sql "
	sys.exit (1)
	

f1=open((sys.argv[1]),'r+')		
oF = open((sys.argv[2]),'w+')

def urlChop(postID,metaB4):	
	with open((sys.argv[1]), 'r') as f1:
		for line in f1:
		#if (".jpg") in line:
			#lineSplit=line.split('"')
			
			#print >>oF, lineSplit[7]			
			#findURL(lineSplit[7])
			if ('VALUES("'+str(metaB4)+'"') in line:
			#lineSplit=line.split('"')			
			#print >>oF, lineSplit[7]			
			#postID=lineSplit[3]
			#metaB4=(int(lineSplit[1]))-1
			#print postID+" "+str(metaB4)
			#urlChop(postID,metaB4)
				a = re.sub(r"[1-9000]+(\/)+[1-9000]+(\/)+\w+(.)+(jpg)","/thumbs/"+postID+".jpg",line)
				b = re.sub(r"(\/)+\w+(-)+\w+(\/)+\w+(\/)+\w+(.)+(jpg)","/thumbs/"+postID+".jpg",a)
				print >>oF, b
				#

with open((sys.argv[1]), 'r') as f1:
    for line in f1:
		#if (".jpg") in line:
			#lineSplit=line.split('"')
			
			#print >>oF, lineSplit[7]			
			#findURL(lineSplit[7])
		if ("_thumbnail_id") in line or ("fig_thumbnail") in line:
			lineSplit=line.split('"')			
			#print >>oF, lineSplit[7]			
			postID=lineSplit[3]
			metaB4=(int(lineSplit[1]))-1
			
			urlChop(postID,metaB4)
			print >>oF, line
		#else:
			#print >>oF, (line)
			