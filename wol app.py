import pickle
from tkinter import *
from tkinter.ttk import *
from wakeonlan import send_magic_packet
import ast
root = Tk()

global mlis
global ilis
global plis
global nlis

i = 0
mlis = []
ilis = []
plis = []
nlis = []

db = {}
db['mac'] = mlis
db['ip'] = ilis
db['port'] = plis
db['name'] = nlis

def inf():
    dbfile = open('PickleDatabase.pickle', 'rb')
    bdb = pickle.load(dbfile)
    db = bdb.decode("utf-8")
    db = ast.literal_eval(db)
    mlis = db['mac']
    ilis = db['ip']
    plis = db['port']
    nlis = db['name']
    dbfile.close()
    itm = str(saved.curselection())
    itm = itm.replace("", "")
    itm = itm.replace(")", "")
    itm = itm.replace("(", "")
    itm = itm.replace(",", "")
    itm = int(itm)
    name = nlis[itm]
    mac = mlis[itm]
    ip = ilis[itm]
    port = str(plis[itm])
    inl.configure(text = 'Name: ' + name + ' MAC: ' + mac + ' Ip: ' + ip + ' Port: ' + port )

def sgl():
    bdb = str(db).encode('utf-8')
    dbfile = open('PickleDatabase.pickle', 'ab')
    pickle.dump(bdb, dbfile)
    dbfile.close()

def save():
    ms = str(mt.get())
    ips = str(it.get())
    ns = str(nt.get())
    nlis.append(ns)
    indx = len(nlis) + 1
    nindex = len(nlis) - 1
    saved.insert(indx, nlis[nindex])
    if ips == '':
        mlis.append(ms)
    else:
        ps = int(pt.get())
        mlis.append(ms)
        ilis.append(ips)
        plis.append(ps)

def imp():
    dbfile = open('PickleDatabase.pickle', 'rb')
    bdb = pickle.load(dbfile)
    db = bdb.decode("utf-8")
    db = ast.literal_eval(db)
    mlis = db['mac']
    ilis = db['ip']
    plis = db['port']
    nlis = db['name']
    dbfile.close()
    i = 1
    while i <= len(nlis):
        saved.insert(i, nlis[i-1])
        i = i+1

root.title("WOL App")
root.geometry('600x600')

label1 = Label(root, text='Saved computers:')
label1.grid()
saved = Listbox(height=10, width=66, activestyle="dotbox", font="Helvetica", fg="black", selectmode="single ")
saved.grid()
ml = Label(root,text="Enter hardware address (only info required to wake on local network),\n (format ('ff.ff.ff.ff.ff.ff', '00-00-00-00-00-00','FFFFFFFFFFFF')):")
ml.grid()
mt = Entry(root, width=20)
mt.grid()
il = Label(root, text="Enter public ip address:")
il.grid()
it = Entry(root, width=20)
it.grid()
pl = Label(root, text="Enter port:")
pl.grid()
pt = Entry(root, width=20)
pt.grid()
nl = Label(root, text="Enter name (info only required to save PC):")
nl.grid()
nt = Entry(root, width=20)
nt.grid()

def wake():
    itm = str(saved.curselection())
    itm = itm.replace("", "")
    itm = itm.replace(")", "")
    itm = itm.replace("(", "")
    itm = itm.replace(",", "")
    itm = int(itm)
    print(itm)
    q = ilis[itm]
    if q =='':
        mac = mlis[itm]
        send_magic_packet(mac)
    else:
        mac = mlis[itm]
        ip = ilis[itm]
        port = plis[itm]
        send_magic_packet(mac, ip_address=ip, port=port)



wake = Button(root, text='Wake computer', command=wake)
wake.grid()
save = Button(root, text="Save computer", command=save)
save.grid()
test = Button(root, text = "Import Previous Session", command=imp)
test.grid()
pg = Label(root, text="Before quitting, PLEASE SAVE GLOBALLY")
pg.grid()
gl = Button(root, text = "Save Globally", command=sgl)
gl.grid()
inf = Button(root, text="Show Info", command=inf)
inf.grid()
inl = Label(root, text = "",)
inl.grid()
root.mainloop()
