import sys

#Oracle SQl Scraper for WordPress


if len (sys.argv) != 4 :
	print "Usage: news.sql news_body.sql outfile.sql "
	sys.exit (1)
	

f1=open((sys.argv[1]),'r+')	
f2=open((sys.argv[2]),'r+')	
oF = ((sys.argv[3]),'w+')

with open((sys.argv[1]), 'r') as inF:
    for line in inF:
	
	if ("values (") in line:		
		curLine = line;
		lineSplit = line.split(",")
		STORYID = lineSplit[12]
		TITLE = lineSplit[20]
		
	with open((sys.argv[2]), 'r') as inF2:
		for line2 in inF2:	
	 
			if ("'",STORYID,"'") in line2:
				lineSplit = line2.split(",")
				BODY.append(lineSplit[5])
	 
				print >>(sys.argv[3]),(STORYID,TITLE,BODY)
			
			
inF.close()

print "File Written",sys.argv[3]
			