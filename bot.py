# STARTLESS
import re, os, random, time, requests, json,sys
from bs4 import BeautifulSoup
os.system('clear')
x = "= " * 30
pass_sc = open("Scr.ml","r") 
rg = pass_sc.read(100000) 
pass_c = open("29991.txt","r")
pass_cc = pass_c.read(1000000) 
if rg == "on": 
  pass_mm = input("Mật khẩu: ") 
  if pass_mm == pass_cc:
   print(" Successs", end="\r") 
   time.sleep(1)
   os.system('clear')
  else:
    print(' Pass sai! ') 
    exit(0)
name_ai = "AI_TESTER => "
tra_cuu = ["tra","Tra","Cứu","cứu","tìm","Tìm","dữ liệu","Hiểu","hiểu","tìm kím","tra cứu","dữ liệu","xem","xem coi","điều tra"]
list_math = ["tính","toán","math","Math", "Tính","Toán","giải toán","tính toán","giải toán tử"]
dong_y_command = ["đồng","ý","ok","có","giúp","được","Có","Đồng","Ý","Giúp","Được"] 
set_nam = ["Biệt danh","gọi tôi","gọi tao","Gọi","Gọi mày","Gọi tao này","Gọi","gọi","gọi tên","tao","gọi Tên","Name","name","reset name","change name"] 
ma_hoa = ["mã hóa","mã hóa văn bản","encode","utf-12","utf-32","utf-64","utf-128","Mã","utf-8"]
scerytu = ["Bảo","Mật","mật khẩu","Khẩu","bảo mật","đặt lại mật khẩu","đặt lại"] 
covid = ["covid"] 
dia_chi = ["khu phố","Khu","Phố","địa","chỉ","nơi ở","Địa","Chỉ"] 
tep_tin = ["tạo tệp tin","tạo file","file txt","Txt","tạo File","tệp","Tệp","tệp tin"]
khac = ["khác","Khác"] 
spam_by = ["Spam dung lượng","Spam bộ nhớ","làm đầy dung lượng","làm đầy bộ nhớ"]
scan_dia_chi = ["ip","ipchecker","IP"] 
khen_goi = ["đánh giá về tôi","Đánh giá con người tôi","Tui","đánh giá","Đánh giá","khen","gợi"] 
level_exp = ["mật thiết","thân nhau"]
ma = open("tenchu.txt","r") 
ten_chu = ma.read(10000099900) 
gioitinh = open("gioitinh.gt","r").read(1000)
male = ["Nam","nam","nữ","Nữ"]
cua_toi = ["chính mình","mình","Mình","Tôi","tôi","me","Tao","tao","Tui","tui",ten_chu] 
avalibe = ["plugin khả dụng","plugin sài được","plugin hoạt động"]
plugin = ["plugin","chức năng"]
print(x) 
k = "Author: Tran Trong Hoa".center(60) 
print(k)
k = "Project: AI Văn Bản".center(60) 
print(k)
k = "Verison: 0.0.1".center(60) 
print(k)
print(x)
input_command = input(" Câu lệnh: ")
giai_mang = f"{input_command}".split(" ")
len_mang = len(giai_mang) 
list_pl = """
[1] Giải toán
[2] Rename Admin 
[3] Change Pass 
[4] Encode Text 
[5] Search 
[6] Local check 
[7] Folder 
[8] Ipchecker 
[9] Spam File 
[10] Đánh Giá Con Người
[11] Độ Mật Thiết v1.0
"""
# search Math 
for toan in range(len(list_math)): 
  if list_math[toan] in input_command:
    acctive = "toan"
# Đổi tên
for doiten in range(len(set_nam)): 
  if set_nam[doiten] in input_command: 
    acctive = "doiten"
# Đổi pass
for setpass in range(len(scerytu)): 
  if scerytu[setpass] in input_command:
    acctive = "setpass" 
# Mã hóa văn bản 
for encoder in range(len(ma_hoa)):
  if ma_hoa[encoder] in input_command:
    acctive = "encoder"
# Tra cứu 
for tracuu in range(len(tra_cuu)): 
  if tra_cuu[tracuu] in input_command: 
    acctive = "tracuu"
# địa Chỉ 
for diachi in range(len(dia_chi)): 
  if dia_chi[diachi] in input_command: 
    acctive = "diachi"
# Tệp tin 
for teptin in range(len(tep_tin)): 
  if tep_tin[teptin] in input_command: 
    acctive = "tep_tin"
# Địa chỉ IP
for ipc in range(len(scan_dia_chi)): 
  if scan_dia_chi[ipc] in input_command: 
    acctive = "ipc"
# Spam bytes 
for bytes_ in range(len(spam_by)): 
  if spam_by[bytes_] in input_command: 
    acctive = "spamfile" 
# list plguin 
for listpl in range(len(plugin)): 
  if plugin[listpl] in input_command: 
    acctive = "pluginlist" 
for khen_goi_ in range(len(khen_goi)): 
  if khen_goi[khen_goi_] in input_command: 
    acctive = "khen_goi" 
 # Mật thiết
for matthiet in range(len(level_exp)): 
  if level_exp[matthiet] in input_command: 
    acctive = "matthiet" 
 # plugin acctive hoạt động!
for ava in range(len(avalibe)): 
  if avalibe[ava] in input_command: 
    acctive = "ava" 
if acctive == "toan": 
   toral = []
   so_luu = []
   so_luu_2 = []
   bao_luu = []
   stt = 0
   print(f"{name_ai} Hãy nhập những bài toán ra , tôi sẽ giúp {ten_chu}!\n")
   while True:
     input_command = input("Ghi bài toán ra (ex: so1 + so2  | khi nào không muốn tính nữa thì enter nhé): ")
     stt = stt + 1
     if input_command == "":
       print("/=========================================\ \n                Tổng Kết : \n\=========================================/")
       for i in range(len(toral)):
         print(f"Bài số {i} | {so_luu[i]} {bao_luu[i]} {so_luu_2[i]} = {toral[i]}\n")
         
       exit(0)
      
     else:
       giai_mang = f"{input_command}".split(" ")
       if giai_mang[1] == "+":
         ket_qua = int(giai_mang[0]) + int(giai_mang[2])
       elif giai_mang[1] == "-":
         ket_qua = int(giai_mang[0]) - int(giai_mang[2])
       elif giai_mang[1] == ":":
         ket_qua = int(giai_mang[0]) / int(giai_mang[2])
       elif giai_mang[1] == "x":
         ket_qua = int(giai_mang[0]) * int(giai_mang[2])
       else:
         print(" Không tìm thấy ")
       print(f"Kết quả: {ket_qua}")
       
       ketqua_total = toral.append(ket_qua)
       hi_1 = so_luu.append(giai_mang[0])
       hi_2 = so_luu_2.append(giai_mang[2])
       hi_3 = bao_luu.append(giai_mang[1])
elif acctive == "doiten":
    tach_10 = input_command.split("'")[1]
    op = open("tenchu.txt","w+") 
    op.write(tach_10) 
    print(f"{name_ai} Ok từ nay tôi sẽ gọi {ten_chu} là {tach_10}") 
   
elif acctive == "encoder":
    bytesn = input(f"{name_ai} Tôi có thể giúp {ten_chu} mã hóa văn bản dưới dạng utf-8, utf-32, utf-16: ") 
    van_ban = input(f"{name_ai} Mời {ten_chu} nhập dữ liệu văn bản: ") 
    msg = bytes(van_ban, bytesn) 
    print(f"{name_ai} Kết quả: {msg}") 
elif acctive == "setpass": 
    print(f"{name_ai} Ok, {ten_chu} tôi sẽ giúp bạn đặt mật khẩu\n") 
    tach_10 = input_command.split("'")[1]
    pass_l = open("Scr.ml","w+") 
    matkhau = open("29991.txt","w+")
    pass_l.write("on") 
    matkhau.write(tach_10) 
    print(f"{name_ai} {ten_chu} đã đặt mật khẩu thành công!") 
elif acctive == "tracuu": 
    lay_ma = len(giai_mang)
    so_ma = lay_ma - 1 
    tach_10 = input_command.split("'")[1]
    #exit(0)
    #print(giai_mang[so_ma])
    url = f"https://vi.m.wikipedia.org/w/index.php?search={tach_10}&title=%C4%90%E1%BA%B7c+bi%E1%BB%87t%3AT%C3%ACm+ki%E1%BA%BFm&profile=default&fulltext=1&ns0=1"
    rq = requests.get(url).text
    beau = BeautifulSoup(rq,"html.parser")
    convert = beau.get_text()
    tach_2 = convert.split(",") 
    len_sp = len(tach_2) - 3
    stt = 0
    a = "- "
    ia = a * 30
    for i in range(3):
      print(f"{name_ai} Chờ chút nhé {ten_chu} [/]", end="\r") 
      time.sleep(0.5) 
      print(f"{name_ai} Chờ chút nhé {ten_chu} [\]", end="\r") 
      time.sleep(0.5)
      print(f"{name_ai} Chờ chút nhé {ten_chu} [-]", end="\r") 
      time.sleep(0.5)
    print(f"{ia}")
    print(f"{name_ai} Có {len_sp} kết quả mà tôi tìm thấy được cho {ten_chu} với chủ đề về {tach_10}!") 
    print(f"{ia}")
    for i in range(len_sp):
      stt = stt + 1
      
     # print(f"{ia}")
     # print(f"{ia}")
      print(f"{tach_2[stt]}")
    print(f"{ia}")
    exit(0)
elif acctive == "diachi":
    url = "https://www.google.com/search?q=covid+19&oq=cov&aqs=chrome.0.69i59j69i57j69i60l3.2390j0j4&client=ms-android-oppo&sourceid=chrome-mobile&ie=UTF-8" 
    rq = requests.get(url).text
    beau = BeautifulSoup(rq,"html.parser")
    convert = beau.get_text() 
    my = convert.split(">")[1]
    #print(my)
    local = my.split('\xa0-\xa0Từ')[0]
    print(f"{name_ai} {ten_chu} Hiện giờ đang ở{local}") 
    exit(0)
elif acctive == "tep_tin":
    timkim = input_command.find("'") 
    if timkim == -1:
      print(f"{name_ai} Chào {ten_chu} tôi đoán không lầm bạn có muốn tạo một file văn bản không?\n ") 
      tra_loi = input("Reply: ") 
      for dy in range(len(dong_y_command)): 
        if dong_y_command[dy] in tra_loi: 
            acctive = "yes"
      if acctive == "yes": 
        input_name = input(f"{name_ai} {ten_chu} muốn tạo file tên gì?: ")
        open_f = open(input_name,"w+") 
        print(f"{name_ai} Đã tạo thành công {input_name} !")
        print(f"{name_ai} {ten_chu} Bạn có muốn ghi gì vào file không?\n ") 
        tra_loi = input("Reply: ") 
        for dy in range(len(dong_y_command)): 
         if dong_y_command[dy] in tra_loi: 
            acctive = "y"
        if acctive == "y": 
          input_vb = input(f"{name_ai} Mời {ten_chu} nhập nội dung văn bản!: ") 
          open_f.write(input_vb)
          print(f"{name_ai} Thêm nội dung vào file {input_name} ")
        else:
          print("tạm biệt") 
          exit(0)
      else:
        print(' Tạm biệt ') 
        exit(0) 
    else:
      tach_co = input_command.split("'")[1] 
      tach_10 = input_command.split("'")[3] 
      open_file = open(tach_co,"w+") 
      open_file.write(tach_10) 
      print(f"{name_ai} Đã tạo file {tach_co} và thêm nội dung vào file {tach_co}")
      exit(0) 
elif acctive == "ipc": 
     timkim = input_command.find("'") 
     for cua in range(len(cua_toi)): 
        if cua_toi[cua] in input_command: 
            timkim = "chinh"
     if timkim == -1:
        print(f"{name_ai} Hmmm....!") 
        print(f"{name_ai} {ten_chu} có muốn kiểm tra ip của mình không?\n ") 
        ip_connect = input("Reply: ") 
        for dy in range(len(dong_y_command)): 
          if dong_y_command[dy] in ip_connect: 
              acctive = "yes"
        for other in range(len(khac)): 
          if khac[other] in ip_connect: 
              acctive = "khac"     
        if acctive == 'yes': 
          ip = "me"
        elif acctive == "khac":
          ip = input(f"{name_ai} {ten_chu} hãy nhập ip muốn check: ") 
        else:
          print("Bùm") 
          exit(0)
       
     elif timkim == "chinh":
        ip = "me" 
      
     else:
        ip = input_command.split("'")[1] 
     url = f"https://api.hextool.tk/ip.php?ip={ip}"
     connect = json.loads(requests.get(url).text)
     ip_chinh = connect["ip"] 
     ip_phu_1 = connect["ip_1"] 
     ip_phu_2 = connect["ip_2"] 
     quocgia = connect["quoc_gia"] 
     khu_vuc = connect["khu_vuc"] 
     internet = connect["internet"] 
     gr_internet = connect["group_internet"] 
      
     chau_luc = connect["chau_luc"] 
      
     print(f"{name_ai} Điều tra:\n IP Điêu Tra: {ip_chinh} \n IP Phụ: {ip_phu_1} \n IP Phụ 2: {ip_phu_2} \n Quốc Gia: {quocgia} \n Khu Vực: {khu_vuc} \n Hãng Internet: {internet} \n Mảng Internet: {gr_internet} ") 
elif acctive == "spamfile": 
  find = input_command.find("'") 
  if find == -1:
    print(f"{name_ai} {ten_chu} Vui lòng nhập thông tin!\n")
    spam_type = input("Cấp độ spam: ") 
    timesleep = input("Thời gian delay: ") 
  else:
    spam_type = int(input_command.split("'")[1])
    timesleep = int(input_command.split("'")[3])
  rans = int(spam_type)
  s = 0
  x = "= " * 30
  while True:
    ran_sl = random.randint(1, rans)
    hi = random.randint(1, 1000000000000)
    hi2 = str(hi) * ran_sl
    load = hi * 10000
    # create + write on file 
    taofile = open(str(hi),"w+") 
    ghi_vao = taofile.write(hi2) 
    docfile = open(str(hi),"r") 
    read_spam = docfile.read()
    s = s + 1
    get_bytes = sys.getsizeof(read_spam) 
    from decimal import *
    getcontext().prec = 1
    if get_bytes < 10000:
      kb_menory = Decimal(get_bytes) / Decimal(1068)
      chi_thi = f"{kb_menory} KB"
    if get_bytes > 10000:
      kb_menory = Decimal(get_bytes) / Decimal(10680)
      chi_thi = f"{kb_menory} MB"
    if get_bytes > 1000000000: 
      kb_menory = Decimal(get_bytes) / Decimal(10680000) 
      chi_thi = f"{kb_menory} GB"
    print(x)
    print(f"=> [{s}] -> Success Spam: ") 
    print(f"=> [Bytes] -> {get_bytes}")
    print(f"=> [Kb] -> {chi_thi}") 
    print(f"=> [Pwd]: ↴'") 
    os.system('pwd')
    print(f"=> [name spam] -> {hi}")
    time.sleep(int(timesleep))
elif acctive == "pluginlist": 
  print(list_pl)
elif acctive == "khen_goi": 
  if gioitinh == "no":
    print(f"{name_ai} Hãy cho tôi biết giới tính của {ten_chu}!\n") 
    gioitinh_sc = input("Reply: ") 
    for gt in range(len(male)): 
      if male[gt] in gioitinh_sc:
        ghu_gt = male[gt]
        acc = "y" 
    if acc == "y":
      print("")
    else:
      print(f"{name_ai} Bạn không phải nam/nữ à ? thế chắc khác, bạn vui lòng điền vào dươi đây._.: ") 
      gioitinh_sc = input(" Reply: ") 
    open_f = open("gioitinh.gt","w+") 
    open_f.write(gioitinh_sc)
  else:
    if gioitinh == "Nam":
      print(f"{name_ai} {ten_chu} là một nam nhân đẹp trai cao ráo xuất sắc nhất hệ mặt trời!") 
    elif gioitinh == "nam":
      print(f"{name_ai} {ten_chu} là một nam nhân đẹp trai cao ráo xuất sắc nhất hệ mặt trời!") 
    elif gioitinh == "nữ": 
      print(f"{name_ai} {ten_chu} là một nữ nhân đẹp gái cao ráo xuất sắc nhất hệ mặt trời!") 
    elif gioitinh == "Nữ": 
      print(f"{name_ai} {ten_chu} là một nũ nhân đẹp gái cao ráo xuất sắc nhất hệ mặt trời!") 
    else:
      print(f"{name_ai} {ten_chu} là một {gioitinh} tài ba hiểu cao rộng, mong bạn sớm tìm được giới tính của mình!")
