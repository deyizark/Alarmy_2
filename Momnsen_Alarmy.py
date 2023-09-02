import os
import pygame
import sys
import time

def femen_odinate(tan_atant):
    if sys.platform.startswith('win'):
        os.system(f'shutdown /s /f /t {tan_atant}')
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system(f'shutdown -h +{tan_atant}')

def redemare_odinate(tan_atant):
    if sys.platform.startswith('win'):
        os.system(f'shutdown /r /f /t {tan_atant}')
    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
        os.system(f'shutdown -r +{tan_atant}')

def jwe_son(lezotan):
    pygame.mixer.init()
    son = pygame.mixer.Sound('tes.wav')
    pygame.time.wait(lezotan * 1000) 
    son.play()

def main():
    print()
    print("Chwazi aksyon ou ta renmen nou ekzekite sou òdinatè a:")
    print()
    print("1. Fèmen òdinatè")
    print("2. Redemare òdinatè")
    print("3. Jwe yon son")
    print("4. Kite pwogram nan")
    
    chwa = input("\nTanpri chwazi yon nimewo nan lis sa a pou aksyon ou vle fè a : ")
    
    if chwa == '1':
        tan_atant = int(input("\nAntre nan kantite tan avan òdinatè a fèmen, ekzanp 10 pou 10 segond : "))
        print(f"\nÒdinatè a pral fèmen nan {tan_atant} segond.")
        femen_odinate(tan_atant)
        print()
        user = input("\nPeze A pou w anile aksyon an : ").upper()
        while (not user.isalpha()):
            user = input("\nPa rantre chif, peze A pou w anile aksyon an : ").upper()
        if user == "A":
            if sys.platform.startswith('win'):
                os.system('shutdown -a')
                print("\nAksyon anile ak siksè")
                time.sleep(2)
                main()
            elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                os.system('sudo shutdown -c')
                print("\nAksyon anile ak siksè")
                time.sleep(2)
                main()
        else:
            while user not in ["A"]:
                print("\nMove sentaks")
                user = input("\nPeze A pou w anile aksyon an : ").upper()
                if user == "A":
                    if sys.platform.startswith('win'):
                        os.system('shutdown -a')
                        print("\nAksyon anile ak siksè")
                        time.sleep(2)
                        main()
                    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                        os.system('sudo shutdown -c')
                        print("\nAksyon anile ak siksè")
                        time.sleep(2)
                        main()
    elif chwa == '2':
        tan_atant = int(input("\nAntre nan kantite tan avan òdinatè a redemare, ekzanp 10 pou 10 segond : "))
        print(f"\nÒdinatè a pral redemare nan {tan_atant} segond.")
        redemare_odinate(tan_atant)
        print()
        user = input("\nPeze A pou w anile aksyon an : ").upper()
        while (not user.isalpha()):
            user = input("\nPa rantre chif, peze A pou w anile aksyon an : ").upper()
        if user == "A":
            if sys.platform.startswith('win'):
                os.system('shutdown -a')
                print("\nAksyon anile ak siksè")
                time.sleep(2)
                main()
            elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                os.system('sudo shutdown -c')
                print("\nAksyon anile ak siksè")
                time.sleep(2)
                main()
        else:
            while user not in ["A"]:
                print("\nMove sentaks")
                user = input("\nPeze A pou w anile aksyon an : ").upper()
                if user == "A":
                    if sys.platform.startswith('win'):
                        os.system('shutdown -a')
                        print("\nAksyon anile ak siksè")
                        time.sleep(2)
                        main()
                    elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
                        os.system('sudo shutdown -c')
                        print("\nAksyon anile ak siksè")
                        time.sleep(2)
                        main()
    elif chwa == '3':
        lezotan = input("\nAntre nan kantite tan pou tann anvan son an jwe, ekzanp 5 pou 5 segond : ")
        while (not lezotan.isdigit()):
            lezotan = input("\nAntre nan kantite tan pou tann anvan son an jwe, ekzanp 5 pou 5 segond : ")
        lezotan = int(lezotan)
        print(f"\nSon an pral jwe nan {lezotan} segond.")
        jwe_son(lezotan)
        print("\nOu deklanche fonksyonalite jwe son an, peze yon touch epi Enter pou w kanpe l epi tou kite pwogram nan : ")
        input()
    elif chwa == "4":
        time.sleep(2)
        quit
    else:
        print("\nMove sentaks !!!")
        main()

main()