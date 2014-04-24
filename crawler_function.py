from urllib import *
from re import *
from sets import Set
i=0

def scrape_email(url, depth):
    data = urlopen(url).read()
    fil = open("data.csv","w")
    links = findall(r'<a href="(http.*?)"',data)
    for link in links:
        inner = urlopen(link).read()
        title = "".join(findall(r'<title.*?>[\n]?(.*?)</title>',inner))
        email = findall(r'([a-z\._A-Z0-9]+@[a-z\._A-Z0-9]+)',inner)
        email_set = Set(email)
        print title
        print email_set
        title_data = "".join(title)
        email_data = " ".join(email_set)
        final_data = title_data+","+email_data+"\n"
        fil.write(final_data)
    fil.close()
    return email

def crawler(addr, depth):
    global i
    path = ""+str(i)
    path += ".html"
    i+=1
    a = urlopen(addr)
    fileobj = open(path,"w")
    html = a.read()
    links = findall(r'<a href="(http.*?)"',html)
    for link in links:
        a_child = urlopen(link)
        html_child = a_child.read()
        title = "".join(findall(r'<title.*?>[\n]?(.*?)</title>',html_child)) 
        content = "".join(findall(r'<meta name="[Dd][Ee][Ss].*?" content="(.*?)"',html_child))
        print "\n"+link
        html_data = '<a href="'+link+'"><h2>'+title+'</h2></a>'
        html_data = html_data + content
        html_data = html_data + '<h4 style="color:blue">'+link+'</h4><br/>'
        fileobj.write(html_data)
        if (depth):
            print "--------------------in innner fuction-----------------------"
            depth-=1
            crawler(link,depth)
        else:
            depth+=1
            print "--------------------in outer fuction-----------------------"
            fileobj.close()
            return
scrape_email("http://www.codechef.com",2)
