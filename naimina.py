import os
filecolor=open("settings/color.txt","r+")
filetitle=open("settings/title.txt","r+")
filestartup=open("settings/startup.txt","r+")
startup=filestartup.read(3)
startup=str(startup)
temp=filecolor.read(2)
temp2="color "+str(temp)
os.system(temp2)
temp=filetitle.read(100)
temp2="title "+str(temp)
os.system(temp2)
scanned=0
bitcoin=0
import msvcrt
import datetime
import time
import sys
import random
x=1
phase="startup" #Starting state
page=0
jreturn=0
selected=1
optionsperpage=10
quiznum=0
soc=0
eco=0
answer=0
pagenum=3 #Number of pages
select=['*',' ',' ',' ',' ',' ',' ',' ',' ',' ']

menuoptions=['Hacker Pro','Memo Manager','Bank Account','Political Compass Quiz','Option 5','Option 6','Option 7','Option 8','Option 9','Option 10'
             ,'Option 11','Option 12','Option 13','Option 14','Option 15','Option 16','Option 17','Option 18','Option 19','Option 20',
             'Settings','Credits','Option 23','Option 24','Option 25','Option 26','Option 27','Option 28','Restart','Shutdown']

if startup=="off":
    temp="Toggle Startup Screen (OFF)"
if startup=="1":
    temp="Toggle Startup Screen (1 second)"
if startup=="2":
    temp="Toggle Startup Screen (2 seconds)"

settingsoptions=['Change Colour','Change Title',temp]
colouroptions=['White','Red','Yellow','Lime','Cyan','Blue','Purple','Pink']
ecoquestions=['Government Regulation does more harm than good.',
              'Capitalism always eventually concentrates wealth into a super-rich elite.',
              'The freer the markets, the freer the people.',"The rich aren't being taxed enough.",
              "The government should seize the means of production."]
ecokey=[1,-1,1,-1,-1]
socquestions=['Freedom of Speech should be limited for the public good.','Abortion should be illegalized in most/all cases',
              '"If you have nothing to hide, nothing to fear."',
              'The Government should help promote helpful values in the education system.',
              'What two consenting adults do in a bedroom is none of the concern of the government.']
sockey=[-1,-1,-1,-1,1]
quizoptions=['Stongly Agree','Somewhat Agree',"Neutral/Don't Know",'Somewhat Disagree','Strongly Disagree']
memooptions=['Create Memo','View Memo','Rename Memo','Delete Memo']
localcity=['Saint John','Sussex','Quispamsis','Rothesay','Moncton','Fredricton','St. Stephen','Bathurst','Campebello','Halifax','Charlottetown']
globalcity=['New York','Boston','Washington DC','Atlanta','Miami','Chicago','Dallas','Houston','Los Angeles','San Diego','Sacramento','Seattle','Austin','Detroit',
            'Toronto','Montreal','Vancouver','Calgary','Edmonton','Ottawa','Winnipeg','Regina','London','Edinburgh','Glascow','Manchester','Liverpool','Oxford',
            'Paris','Monaco','Lyon','Brussels','Amsterdam','Hamburg','Berlin','Frankfurt','Munich','Stockholm','Oslo','Warsaw','Kiev','Madrid','Vienna','Tallin',
            'Budapest','Riga','Helenski','Moscow','St. Petersburg','Istanbul','Tehran','Mumbai','New Delhi','Bangalore','Hyperabad','Shanghai','Beijing','Guangzhou',
            'Hong Kong','Macau','Taipei','Wuhan','Chongqing','Seoul','Pyongyang','Tokyo','Sydney','Canberra']
options=menuoptions

selnum=1


def cls():
    os.system('cls')
    return

def header():
    print("NAIMINA OS VERSION V3.0")
    global page
    global optionsperpage
    time=str(datetime.datetime.now())
    time=time[:16]
    print("Current Time:",time)
    print()
    print(phase)

def menu():
    print("Page",page+1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    counter=0
    while counter<optionsperpage: #Just renders the options
        temp=str(counter+1+page*optionsperpage)+'.'
        if counter+1+page*optionsperpage<10:
            temp=' '+str(counter+1+page*optionsperpage)+'.'
        print(select[counter],temp,options[counter+page*optionsperpage])
        counter=counter+1
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
    print("WASD keys to move around, number keys to select certain options. J to select.")
    print("B to return to main menu.")
    return

def key():
    global quiznum
    global selnum
    global select
    global selected
    global phase
    global page
    char=msvcrt.getch() #Gets character
    char=str(char) #Some fancy shit to make it easier to execute
    char=char[2]
    char=char.lower()
    if char=="w": #Selection Up
        up()
        cls()
        return
    if char=="s": #Selection down
        down()
        cls()
        return
    if char=="1" or char=="2" or char=="3" or char=="4" or char=="5" or char=="6" or char=="7" or char=="8" or char=="9":
        if int(char)<optionsperpage+1:
            select[selnum-1]=' ' #Number Handling
            selnum=int(char)
            select[selnum-1]='*'
            cls()
            return
    if char=="0": #Extra case for 0
        if 10<optionsperpage+1:
            select[selnum-1]=' '
            selnum=10
            select[selnum-1]='*'
            cls()
            return
    if char=="a": #Page to the left
        a()
        cls()
        return
    if char=="d": #Page to the right
        d()
        cls()
        return
    if char=="j": #Selection
        j()
        cls()
        return
    if char=="b": #Home
        phase="Main Menu"
        quiznum=99
        cls()
        return
    cls()
    return

def j(): #Selection, redirect.
    global answer
    global selected
    global selnum
    global phase
    global page
    global quiznum
    global eco
    global soc
    global startup
    selected=selnum+page*10
    if phase=="Main Menu": #Options from main Main Menu
        if selected==1:
            phase="Hacker Pro"
            cls()
            scanned=0
        if selected==2:
            phase="Memo Manager"
            cls()
        if selected==3:
            phase="Bank Account"
            cls()
        if selected==4:
            phase="Political Quiz"
            soc=0
            eco=0
            quiznum=0
            cls()
        if selected==21:
            phase="Settings"
        if selected==22:
            phase="Credits"
        if selected==29:
            phase="Restart"
        if selected==30:
            phase="Shutdown"
        page=0
        return
    if phase=="Settings": #Options from Settings
        if selected==1:
            phase="Change Colour"
        if selected==2:
            phase="Change Title"
        if selected==3: #Startup toggle options
            if startup=="2":
                filestartup=open("settings/startup.txt","w")
                del settingsoptions[-1]
                settingsoptions.append("Toggle Startup Screen (OFF)")
                filestartup.write("off")
                startup="off"
                return
            if startup=="off":
                filestartup=open("settings/startup.txt","w")
                del settingsoptions[-1]
                settingsoptions.append("Toggle Startup Screen (1 seconds)")
                filestartup.write("1")
                startup="1"
                return
            if startup=="1":
                filestartup=open("settings/startup.txt","w")
                del settingsoptions[-1]
                settingsoptions.append("Toggle Startup Screen (2 seconds)")
                filestartup.write("2")
                startup="2"
                return
        return
    if phase=="Change Colour": #Change colour, exactly what it says on the tin
        filecolor=open("settings/color.txt","w")
        if selnum==1:
            os.system("color 07")
            filecolor.write("07")
        if selnum==2:
            os.system("color 0c")
            filecolor.write("0c")
        if selnum==3:
            os.system("color 0e")
            filecolor.write("0e")
        if selnum==4:
            os.system("color 0a")
            filecolor.write("0a")
        if selnum==5:
            os.system("color 0b")
            filecolor.write("0b")
        if selnum==6:
            os.system("color 09")
            filecolor.write("09")
        if selnum==7:
            os.system("color 05")
            filecolor.write("05")
        if selnum==8:
            os.system("color 0d")
            filecolor.write("0d")
        filecolor=open("settings/color.txt","r+")
        return
    if phase=="Political Quiz":
        if selnum==1:
            answer=2
        if selnum==2:
            answer=1
        if selnum==3:
            answer=0
        if selnum==4:
            answer=-1
        if selnum==5:
            answer=-2
        if quiznum<5:
            eco=eco+(answer*ecokey[quiznum])
        else:
            soc=soc+(answer*sockey[quiznum-5])
        quiznum=quiznum+1
        return
    if phase=="Memo Manager":
        if selnum==1:
            phase="Create Memo"
        if selnum==2:
            phase="View Memo"
        if selnum==3:
            phase="Rename Memo"
        if selnum==4:
            phase="Delete Memo"
        return

def up(): #Up
    global selnum
    global select
    global mode
    select[selnum-1]=' '
    selnum=int(selnum)-1
    if selnum==0:
        selnum=optionsperpage
    select[selnum-1]='*'
    return

def down(): #Down
    global selnum
    global select
    global mode
    select[selnum-1]=' '
    selnum=int(selnum)+1
    if selnum==optionsperpage+1:
        selnum=1
    select[selnum-1]='*'
    return

def a(): #Left Page
    global page
    page=page-1
    if page==-1:
        page=pagenum-1
    return

def d(): #Right Page
    global page
    page=page+1
    if page==pagenum:
        page=0
    return

while x==1:
    while phase=="startup": #Startup screen
        if startup!="off":
            print("=======================================================")
            print("  _   _       _           _                ___  ____ ")
            print(" | \ | | __ _(_)_ __ ___ (_)_ __   __ _   / _ \/ ___|")
            print(" |  \| |/ _` | | '_ ` _ \| | '_ \ / _` | | | | \___ \ ")
            print(" | |\  | (_| | | | | | | | | | | | (_| | | |_| |___) |")
            print(" |_| \_|\__,_|_|_| |_| |_|_|_| |_|\__,_|  \___/|____/ ")
            print("=======================================================")
            print("By DarkErminia, Powered by Python.")
            time.sleep(int(startup))
            cls()
        phase="Main Menu"
    while phase=="Main Menu": #Main Menu
        optionsperpage=10 #Sets up the Settings for Main Menu
        pagenum=3
        options=menuoptions
        header()
        menu()
        key()
    while phase=="Hacker Pro": #Hacker Pro
        print("Welcome to Hacker Pro, do 'help' for a list of commands.")
        command=input(">")
        command=str(command)
        if command=="help":
            print()
            print("Hacker Pro commands:")
            time.sleep(0.01)
            print("help - displays the help screen")
            time.sleep(0.01)
            print("scan - scans the local area for vulnerable ips")
            time.sleep(0.01)
            print("scan local/global - scans either the local or global area for vulnerable ips")
            time.sleep(0.01)
            print("hack - hacks found ips, requires you scan first.")
            time.sleep(0.01)
            print("hack (user) - hacks specific user")
            time.sleep(0.01)
            print("dox (user) - leaks personal info about user")
            time.sleep(0.01)
            print("superdox (user) - oh god, superdox. use only as last resort")
            time.sleep(0.01)
            print("mine - mines bitcoins (value) times")
            time.sleep(0.01)
            print("exit - returns to main menu")
            time.sleep(0.01)
            print()
            break
        if command=="scan" or command=="scan local":
            print()
            print("Scanning...")
            time.sleep(1)
            rand=random.randint(3,5)
            print("Finished,",rand,"IPs found.")
            counter=1
            while counter<rand:
                time.sleep(0.01)
                ip1=random.randint(1,255)
                ip2=random.randint(1,255)
                ip3=random.randint(1,255)
                ip4=random.randint(1,255)
                temp=random.randint(1,len(localcity))
                ip=str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
                temp=str(ip)+" ("+localcity[temp-1]+")"
                print(temp)
                counter=counter+1
            print()
            scanned=1
            break
        if command=="scan global":
            print()
            print("Scanning...")
            time.sleep(1)
            rand=random.randint(5,10)
            print("Finished,",rand,"IPs found.")
            counter=1
            while counter<rand:
                time.sleep(0.01)
                ip1=random.randint(1,255)
                ip2=random.randint(1,255)
                ip3=random.randint(1,255)
                ip4=random.randint(1,255)
                temp=random.randint(1,len(globalcity))
                ip=str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
                temp=str(ip)+" ("+globalcity[temp-1]+")"
                print(temp)
                counter=counter+1
            print()
            scanned=1
            break
        if command=="hack":
            print()
            if scanned==0:
                print("You have to scan before you can hack.")
                print()
                break
            print("Hacking",rand,"IP addresses...")
            rand2=random.randint(100,200)
            rand2=rand2*rand
            time.sleep(1)
            print("Successful!",rand2,"bitcoins transferred to account.")
            bitcoin=bitcoin+rand2
            print()
            break
        if command[:5]=="hack ":
            print()
            target=command[5:]
            temp=str(target)+"..."
            print("Hacking",temp)
            time.sleep(1)
            rand2=random.randint(100,200)
            print("Successful!",rand2,"bitcoins transferred to account.")
            bitcoin=bitcoin+rand2
            print()
            break
        if command[:4]=="dox ":
            print()
            target=command[4:]
            temp=str(target)+"..."
            print("Doxxing",temp)
            time.sleep(1)
            print("Successful!",target,"has been doxxed!")
            break
        if command[:9]=="superdox ":
            print()
            target=command[9:]
            print("Oh god, here we go.")
            print("Superdoxxing...")
            time.sleep(1)
            print("Successful,",target,"got doxxed so hard that they got deleted from this plane of existence.")
            print("I hope you're happy with yourself.")
            print()
            break
        if command=="mine" or command=="mine bitcoin":
            print()
            print("How many transfers do you wish to do?")
            transfer=input(">")
            try:
                transfer=int(transfer)
            except BaseException:
                print("That is not a valid number.")
                print()
                break
            print("Starting",transfer,"transfers...")
            counter=1
            total=0
            while counter<transfer:
                time.sleep(0.01)
                ip1=random.randint(1,255)
                ip2=random.randint(1,255)
                ip3=random.randint(1,255)
                ip4=random.randint(1,255)
                ip=str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
                ip1=random.randint(1,255)
                ip2=random.randint(1,255)
                ip3=random.randint(1,255)
                ip4=random.randint(1,255)
                iptwo=str(ip1)+"."+str(ip2)+"."+str(ip3)+"."+str(ip4)
                rand=random.randint(1,10000)
                print("Transferring",rand,"bitcoins from",ip,"to",iptwo,"...")
                total=total+rand*0.01
                counter=counter+1
            total=round(total,2)
            print("Finished!",total,"bitcoins transferred to account!")
            bitcoin=bitcoin+total
            print()
            break
        if command=="exit":
            cls()
            phase="Main Menu"
            break
        print("That is not a valid command, do 'help' for a list of commands.")
        print()
        break              
    while phase=="Bank Account": #Bank Account
        header()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        cad=bitcoin*9900
        cad="("+str(cad)+" CAD)"
        print("Your bank balance:",bitcoin,"bitcoins.",cad)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Press any key to continue...")
        char=msvcrt.getch()
        cls()
        phase="Main Menu"
    while phase=="Political Quiz": #Political Quiz
        while quiznum<5:
            optionsperpage=5
            pagenum=1
            options=quizoptions
            header()
            print("Social Score:",soc)
            print("Economic Score:",eco)
            print("Select the answer which is closest to how you feel about the following statement.")
            print()
            print(ecoquestions[quiznum])
            print()
            menu()
            key()
        while quiznum<10 and quiznum>4:
            header()
            print("Social Score:",soc)
            print("Economic Score:",eco)
            print("Select the answer which is closest to how you feel about the following statement.")
            print()
            print(socquestions[quiznum-5])
            print()
            menu()
            key()
        if quiznum==99:
            break
        print("Social Score:",soc)
        print("Economic Score:",eco)
        if soc<0 and eco<0:
            type="a"
        if soc<0 and eco>0:
            type="c"
        if soc>0 and eco>0:
            type="l"
        if soc>0 and eco<0:
            type="p"
        temp=abs(soc)+abs(eco)
        if temp<5:
            pol="Centrist"
        if temp>4 and temp<13:
            if type=="a":
                pol="Soft Authoritarian"
            if type=="c":
                pol="Soft Conservative"
            if type=="l":
                pol="Neoliberal"
            if type=="p":
                pol="Soft Liberal"
        if temp>12 and temp<19:
            if type=="a":
                pol="Authoritarian"
            if type=="c":
                pol="Conservative"
            if type=="l":
                pol="Libertarian"
            if type=="p":
                pol="Progressive"
        if temp>18:
            if type=="a":
                pol="Totalitarian"
            if type=="c":
                pol="Pinochetian"
            if type=="l":
                pol="Anarcho-Capitalist"
            if type=="p":
                pol="Anarcho-Communist"
        print("Your political position:",pol)
        print("Press any key to continue...")
        char=msvcrt.getch()
        cls()
        phase="Main Menu"
    while phase=="Memo Manager": #Memo Manager
        optionsperpage=4
        options=memooptions
        pagenum=1
        header()
        menu()
        key()
        break
    while phase=="Create Memo": #Create Memo
        content=""
        header()
        print()
        print("Put name of memo here.")
        memoname=input(">")
        cls()
        temp2="memos/"+str(memoname)+".txt"
        memo=open(temp2,"w")
        temp="("+str(memoname)+".txt)"
        print('Write your memo here, type "/end" to finish.',temp)
        print()
        breakloop=0
        while breakloop==0:
            content=input()
            content=str(content)+"\n"
            if content=="/end\n":
                breakloop=1
            else:
                memo.write(content)
        memo.flush()
        cls()
        phase="Memo Manager"
        break
    while phase=="View Memo": #View Memo
        print("Memo Manager has found the following memos.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        os.system("dir memos /b")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Type which one you want to view.")
        view=input(">")
        temp2="memos/"+str(view)+".txt"
        try:
            viewer=open(temp2,"r")
        except BaseException:
            print("We could not find that file. Please make sure the name is spelled correctly and try again.")
            print("Press any key to continue...")
            msvcrt.getch()
            cls()
            break
        printer=viewer.readlines()
        newprinter=[x[:-1] for x in printer]
        print()
        counter=0
        cls()
        temp="("+str(temp2)+")"
        temp2=temp+":"
        print(temp2)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        while counter<len(newprinter): #For some goddamn reason for loops just don't work. I dunno why they just don't :/
            print(newprinter[counter])
            counter=counter+1
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print()
        print("Press any key to continue...")
        msvcrt.getch()
        phase="Memo Manager"
        cls()
    while phase=="Rename Memo": #Rename Memo
        header()
        print("Memo Manager has found the following memos.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        os.system("dir memos /b")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Type which one you want to rename.")
        view=input(">")
        temp2="memos/"+str(view)+".txt"
        if os.path.exists(temp2):
            temp=temp
        else:
            print("We could not find that file. Please make sure the name is spelled correctly and try again.")
            print("Press any key to continue...")
            msvcrt.getch()
            cls()
            phase=="Memo Manager"
            break
        print()
        print("What do you want to rename it to?")
        rename=input(">")
        rename="memos/"+str(rename)+".txt"
        try:
            os.rename(temp2,rename)
        except BaseException:
            print("Unfortunately, we can't rename anything you have accessed during this session.")
            print("Please restart Naimina OS and try again. Sorry :/")
            print("Press any key to continue...")
            msvcrt.getch()
            cls()
            phase="Memo Manager"
            break
        print()
        print("Rename successful, renamed to",rename)
        print("Press any key to continue...")
        msvcrt.getch()
        cls()
        phase="Memo Manager"
    while phase=="Delete Memo":
        header()
        print("Memo Manager has found the following memos.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        os.system("dir memos /b")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Type which one you want to delete.")
        view=input(">")
        temp2="memos/"+str(view)+".txt"
        try:
            viewer=open(temp2,"r")
            asdf=open(temp2,'r') #Opens and closes the file
            asdf.close() #Close
        except BaseException:
            print()
            print("That file does not appear to exist.")
            print("Press any key to continue...")
            msvcrt.getch()
            phase="Memo Manager"
            cls()
            break
        try:
            viewer.close()
        except BaseException:
            temp=temp
        os.remove(temp2)
        print()
        print("Deletion Successful. Press any key to continue...")
        msvcrt.getch()
        cls()
        phase="Memo Manager"
        break
    while phase=="Settings": #Settings
        optionsperpage=3
        options=settingsoptions
        pagenum=1
        header()
        menu()
        key()
    while phase=="Change Colour": #colour changer
        optionsperpage=8
        options=colouroptions
        header()
        menu()
        key()
    while phase=="Change Title": #Title Changer
        filetitle=open("settings/title.txt","w")
        print("Please input your new title here.")
        temp=input(">")
        temp2="title "+str(temp)
        os.system(temp2)
        filetitle.write(temp)
        filetitle=open("settings/title.txt","r+")
        phase="Settings"
        cls()
    while phase=="Credits": #Credits
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("All coding done by DarkErminia.")
        print("Press any key to continue...")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        char=msvcrt.getch()
        cls()
        phase="Main Menu"
    while phase=="Restart": #Restart
        os.startfile('naimina.py')
        sys.exit(0)
    while phase=="Shutdown": #Shutdown
        sys.exit(0)
        
    
        
        

            
            
