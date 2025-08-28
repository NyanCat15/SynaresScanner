###Created by NyanCat15 on github.
import os
import time
print("Synares病毒检测器。")
if os.name == 'nt':
    print("请等待一段时间 Please wait...")
    check1 = os.path.exists("C:\\ProgramData\\Synaptics\\Synaptics.exe")
    time.sleep(5)
    os.system("start testapp.exe")
    time.sleep(2)
    check2 = os.path.exists("._cache_testapp.exe")
    check3 = os.path.exists("._cache_HD_testapp.exe") 
    check4 = os.path.exists("C:\\Windows\\System32\\Synaptics\\Synaptics.exe")
    print("结果如下:")
    print(check1)
    print(check2)
    print(check3)
    print(check4)
    if check1 == True:
        os.system("taskkill /f /im Synaptics.exe")
        os.system("rd /s /q C:\ProgramData\Synaptics")
        print("我们以尽可能的清除了病毒,请下载杀毒软件.")
    elif check3 == True:
        os.system("taskkill /f /im Synaptics.exe")
        os.system("rd /s /q C:\Windows\System32\Synaptics")
        print("我们以尽可能的清除了病毒,请下载杀毒软件.")
    else:
        pass
else:
    print("请使用Windows!")
    
