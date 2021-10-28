#Page is created by me

from django.http.response import HttpResponse  #import HttpResponse
from django.shortcuts import render #import render

def index(request):
    return render( request,'index.html')
#________________________________________________________________

#________________________________________________________________
def analyzetext(request):
    #get the text from textarea
    djtext=request.POST.get('textarea_text','default') #textarea_text first argument take when text in textarea / else default print hote enviranment madhe  || IN index.html textarea_text must be added as name of textarea
    # print(djtext) #for developer enviranment

    #For getting value of removepunc ON or Off
    removepunc = request.POST.get('removepunc','off') #when checkbox on then removepunc argument work / else unchecked then off argument work
    
    #For getting value of newlineremove ON or Off
    newlineremover = request.POST.get('newlineremover','off') #when checkbox on then removepunc argument work / else unchecked then off argument work

    #For getting value of fullcaps ON or off
    fullcaps = request.POST.get('fullcaps','off')
    
    #For getting value of extraspaceremover ON or off
    extraspaceremover = request.POST.get('extraspaceremover','off')

    #For getting value of fullcaps ON or off
    charcounter = request.POST.get('charcounter','off')

    if removepunc == "on":
        punctuations='''!()-{}[]:;'"\/,<>.?@#$%^&*~+'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        #to render
        params = {'purpose':'Remove Punctuations', 'analyzed_text':analyzed}
        return render(request,'analyzetext.html',params)
    
    #adding fullcaps logic
    elif(fullcaps == 'on'):
        analyzed = ''
        for char in djtext:
            analyzed = analyzed + char.upper()  #.upper()  function in python for convert lowercase --> uppercase

        #To display
        params = {'purpose':'Change To Uppercase', 'analyzed_text':analyzed}
        return render(request,'analyzetext.html',params)

    #adding new line remover logic
    elif(newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            '''
            if char !='\n':                   this not wotk after pre tag  we need check carrage return
                analyzed = analyzed + char
            '''  
            if char !='\n' and char != '\r':         #  network madhe newline charctor la transport karnyasathi \n & \r taktat ya case madhe donhi not equal to katayla lagtil
                analyzed = analyzed + char
        params = {'purpose':'Remove New Line', 'analyzed_text': analyzed}
        return render(request,'analyzetext.html',params)

    #adding extra space Remover Logic        
    elif(extraspaceremover == 'on'):
        analyzed = ''
        for index, char in enumerate(djtext): #for loop konty index vr challa ahy he kadnyasathi index ani enumerate() wapartat.
            if not (djtext[index] == ' ' and djtext[index + 1] == ' '): # jr double space asel tr 
                analyzed = analyzed + char

        params = {'purpose':'Extra Space Remove', 'analyzed_text': analyzed}
        return render(request,'analyzetext.html',params)
    
    #adding charcounter logic
    elif(charcounter=='on'):
        analyzed =''
        for char in djtext:
            analyzed = len(djtext)

        params = {'purpose':'Char Count', 'analyzed_text': analyzed}
        return render(request,'analyzetext.html',params)

    else:
        return HttpResponse('Error ( please on CHECKBOX )')
        
#__________________________________________________________________________
'''ABOUT US'''

def about(request):
    return render(request,'about.html') 



#logic

'''
Frontend :- 

index.html :

yat fakt heading & form madhe--> ( textarea & submit button ahy )

Form madhe action analyzetext ahy
method get ahy
--> Tyamule jase aapan submit karu tasa te analyzetext madhe janar

 analyzetext aapan define keli ahy urls.py madhe tyacha path ahy views.analyzetext


'''
#logic in views.py

'''
views.py madhe analyzetext(request) ase Function ahy

tyat by using get
 first djtext madhe textarea madhil text gheto
 second removepunc checkbox on ahy ki off tyachi value gheto 

Jr punctuations  checked means on asel tr 
     aapan kahi punctuations chi string diliya
     ani analyzed chi null string banavli ahy

     for loop ne djtext madhlya char gheto
          ani ( if char not in punctuations:) means aasha char gheto jya 
                                              punctuations chya string madhe nastil 

           analyzed = analyzed + char  -->means null analyzed madhe te char 
                                          add kele

    return render karun 3rd argument of render vaprun alalyzetext.html 
    madhe te analyzed (bina punctaions wale char) display kele                                      
          
'''
#WHATS NEW
#enumerate()   line 62

# CHALLANGE: charactor counter