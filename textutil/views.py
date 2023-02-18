from django.http import HttpResponse
from django.shortcuts import render

# Home View
def index(request):
    return render(request,'index.html')

def analyze(request):
   
    djtext = request.POST.get('text','default')
    
    #Buttons
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    charlen = request.POST.get('charlen','off')
    #Logic:
    #Remove Punc
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations','analyzed_text':analyzed}
        return render (request,'analyze.html',params)
    #Capitalize
    elif (fullcaps == 'on'):
        
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Your Text has been capitalized','analyzed_text':analyzed}
        return render (request,'analyze.html',params)
    #Length of Characters
    elif (charlen == 'on'):        
        analyzed = ""
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose':'Length of your charaters is','analyzed_text':analyzed}
        return render (request,'analyze.html',params)
    else:
        return HttpResponse('Error')

