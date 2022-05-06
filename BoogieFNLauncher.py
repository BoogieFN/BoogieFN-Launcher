import wpf
import webbrowser
from System.Windows import Application, Window
import os
import time

class MyWindow(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'BoogieFNLauncher.xaml')
    def launch_Click(self, sender, e):
        path = "C:\Program Files\Epic Games\Fortnite"
        backend_url = ""
        ses = requests.Session()
        request = ses.get(backend_url + "/hybrid/ssl.dll")
        with open(path + '\FortniteGame\Binaries\Win64\ssl.dll', 'wb') as f:
            f.write(request.content)
        eacreq = ses.get(backend_url + "/hybrid/FortniteClient-Win64-Shipping_EAC.exe")
        with open(path + '\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping_EAC.exe', 'wb') as f:
            f.write(eacreq.content)
        bereq = ses.get(backend_url + "/hybrid/FortniteClient-Win64-Shipping_BE.exe")
        with open(path + '\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping_BE.exe', 'wb') as f:
            f.write(bereq.content)

        os.startfile(path + '\FortniteGame\Binaries\Win64\FortniteClient-Win64-Shipping')

    def discord_Click(self, sender, e):
        webbrowser.open('https://discord.gg/HfNfDQnPb6')
    def github_Click(self, sender, e):
        webbrowser.open('https://github.com/boogiefn')
    def srcl_Click(self, sender, e):
        webbrowser.open('https://github.com/boogiefn/boogiefn-launcher')
    def tut_Click(self, sender, e):
        webbrowser.open('https://www.youtube.com/watch?v=2Ma_tEQGxp4')
    def dashbrd_Click(self, sender, e):
        webbrowser.open('https://dashboard.boogiefn.cf/me/')
    def Button_Click(self, sender, e):
        webbrowser.open('https://dashboard.boogiefn.cf/me/')


if __name__ == '__main__':
    Application().Run(MyWindow())
