# pip install pyautogui

import pyautogui
import time

osse = ""
ip = ""
intt = ""
dg = ""
dns = ""

def oss():
    global osse
    global ip
    global intt
    global dg
    global dns


    while True:
        print("設定したいOS\n1. centos \n2. ubuntu")
        osse = input(">")
        try:
            if osse == "1":
                sett = 1
                break
            elif osse == "2":
                sett = 2
                break
            else:
                raise Exception
        except:
            print("エラーが発生しました")

    print("指定したいIPアドレス(CIDR表記でサブネットまで入力)")
    ip = input(">")
    print("IPアドレスを設定するインターフェース名")
    intt = input(">")
    print("デフォルトゲートウェイ")
    dg = input(">")
    print("DNSの設定")
    dns = input(">")
    
    
    print("10秒後にネットワークの設定を行います。設定するウィンドウをアクティブにしてください。")
    time.sleep(10)
    
    if sett == 1:
        centos()
    else:
        ubuntu()

def centos():
    global osse
    global ip
    global intt
    global dg
    global dns

    print("centosのネットワーク設定を行います。")
    
    inttt = "nmcli c m " + str(intt) + " connection.autoconnect yes"
    pyautogui.write(inttt, interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    
    ip = "nmcli c modify " + str(intt) + " ipv4.addresses " + str(ip)
    pyautogui.write(ip, interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    
    dg = "nmcli c modify " + str(intt) + " ipv4.gateway " + str(dg)
    pyautogui.write(dg, interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    
    dns = "nmcli c modify " + str(intt) + " ipv4.dns " + str(dns)
    pyautogui.write(dns, interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    
    con1 = "nmcli c modify " + str(intt) + " ipv4.method manual"
    pyautogui.write(con1, interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    
    con2 = "nmcli c down " + str(intt) + "; nmcli c up " + str(intt)
    pyautogui.write(con2, interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    
    con3 = "nmcli d show " + str(intt)
    pyautogui.write(con3, interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    
    pyautogui.write("ip addr", interval=0.25)
    pyautogui.press('enter')
    time.sleep(1)
    
    pyautogui.write("systemctl restart network", interval=0.25)
    pyautogui.press('enter')

    time.sleep(1)
    pyautogui.write("ping google.com", interval=0.25)
    pyautogui.press('enter')
    
        
def ubuntu():
    global osse
    global ip
    global intt
    global dg
    global dns
    
    pyautogui.write("nano /etc/netplan/99-config.yaml", interval=0.25)
    pyautogui.press('enter')
    
    pyautogui.write("network", interval=0.25)
    pyautogui.press('enter')
    
    
    pyautogui.write("  version: 2", interval=0.25)
    pyautogui.press('enter')
    
    pyautogui.write("  renderer: networkd", interval=0.25)
    pyautogui.press('enter')
    
    pyautogui.write("  ethernets:", interval=0.25)
    pyautogui.press('enter')
    
    pyautogui.write("    ", interval=0.25)
    pyautogui.write(intt, interval=0.25)
    pyautogui.write(":", interval=0.25)
    pyautogui.press('enter')
    
    pyautogui.write("      dhcp4: false", interval=0.25)
    pyautogui.press('enter')
    pyautogui.write("      addresses:", interval=0.25)
    pyautogui.press('enter')
    pyautogui.write("        - ", interval=0.25)
    pyautogui.write(ip, interval=0.25)
    pyautogui.press('enter')
    
    
    pyautogui.write("      gateway4: ", interval=0.25)
    pyautogui.write(dg, interval=0.25)
    pyautogui.press('enter')
    
    pyautogui.write("      nameservers:", interval=0.25)
    pyautogui.press('enter')
    
    pyautogui.write("        addresses: [", interval=0.25)
    pyautogui.write(dns, interval=0.25)
    pyautogui.write(",8.8.8.8]", interval=0.25)
    pyautogui.press('enter') 
    
    
    
    pyautogui.hotkey('ctrl', 'x')
    pyautogui.write("y", interval=0.25)
    pyautogui.press('enter') 
    
    
    pyautogui.write("sudo netplan apply", interval=0.25)
    pyautogui.press('enter')
    
    pyautogui.write("ping google.com", interval=0.25)
    pyautogui.press('enter')
    
    
    
    
def main():
    oss()
    

main()