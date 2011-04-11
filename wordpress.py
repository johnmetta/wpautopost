#!/usr/bin/python
import sys, os, xmlrpclib

logfile = open('/Users/john/Desktop/log.txt','w')
log = lambda x: logfile.write(`x` + "\n")

blog_address = 'http://mettadore.com' #The address of the blog that you're posting to
blog_id = 17 #The ID of your blog

#Hacky code follows

blogpath = blog_address + "/xmlrpc.php"
user = os.environ['WPUSER']
passwd = os.environ['WPPASS']

server = xmlrpclib.ServerProxy(blogpath)

html = open(sys.argv[1]).readlines()
html = html[14:-2]
log(html)
title = html.pop(0).replace("<p>","").replace("</p>","")
log(title)
content = " ".join(html)
log(content)

blog_content = { 'title' : title, 'description' : content }

post_id = int(server.metaWeblog.newPost(blog_id, user, passwd, blog_content,0))
log(post_id)

result = server.metaWeblog.getCategories(blog_id, user, passwd)
lst = []
for f in result: 
    log("%s: %s" % (f['categoryName'], f['categoryId']))

#server.mt.setPostCategories(post_id, user, passwd, categories) # not work
#server.mt.publishPost(post_id, user, passwd)
