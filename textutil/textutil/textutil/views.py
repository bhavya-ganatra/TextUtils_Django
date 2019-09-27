#I have made this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #maps={'name':'jarvis','owner':'ironman'}
    #return render(request,'index.html',maps)  {{owner}} has {{name}} Write this in html
    #return HttpResponse("<h1>No end point     hello</h1>")
    return render(request,'index.html')

def about(request):
    return HttpResponse('''In about Hello <a href="https://www.fast2sms.com/sidtalk/">Click Here</a>''')

def intxt(request):
    f1=open("D:\python\one.txt","r")
    #return HttpResponse("<h1>%s</h1>"%(f1.read()))
    return HttpResponse("%s"%f1.read())


def analyze(request):
    #Get the text
    #print(request.GET.get('text','default'))   #print this in terminal window

    djtext=request.POST.get('text','default')
    rempunc=request.POST.get('removepunc','off')
    fulca=request.POST.get('fullcap','off')
    newlinerem=request.POST.get('newlineremove','off')
    spacerem=request.POST.get('spaceremove','off')
    chcount=request.POST.get('charcount','off')

    #print("remove punction:",rempunc)
    #print("full cap:",fulca)
    print(djtext)




    if rempunc=="on":
    #return HttpResponse("removepunc")
    #Now instead of Httprsponse we will use render
    #analyzed=djtext
        analyzed=""
        punctions=''',./';[]!@#$%^&*()_+\}{":?><'''
        for i in djtext:
            if i not in punctions:
                analyzed= analyzed + i

        para={'purpose':'Removed Punctuation','analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',para)


    if fulca =="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()

        para={'purpose':'Change to UPPERCASE','analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',para)

    if newlinerem == "on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed+= char
        para={'purpose':'New Line Removed','analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',para)

    if spacerem == "on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed+= char
        para={'purpose':'Space Removed','analyzed_text': analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',para)

    if chcount == "on":
        para={'purpose':'Number Of charcters','analyzed_text': len(djtext)}
        #return render(request,'analyze.html',para)


    if rempunc!="on" and fulca !="on" and newlinerem != "on" and  spacerem != "on" and chcount != "on":
        return HttpResponse("ERROR")

    return render(request,'analyze.html',para)
#def removepunc(request):
#    #Get the text
#    #print(request.GET.get('text','default'))   #print this in terminal window
#    djtext=request.GET.get('text','default')
#    print(djtext)
#    return HttpResponse("removepunc")


#def capit(request):
#    return HttpResponse("capit")

#def newlineremove(request):
#    return HttpResponse("newlineremove")

#def spaceremove(request):
 #   return HttpResponse("spaceremove <a href='/'>Back</a>")
#def charcount(request):
#    return HttpResponse("charcount")
