import qrcode
url = r"C:\Users\tejas\OneDrive\Desktop\sublit.txt"
with open(url,'r')as f:
    for i in range(133):
        d = f.readline().strip()
        code = qrcode.make(d)
        code.save("dataset/"+d+".png")