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
    check3 = os.path.exists("C:\\Windows\\System32\\Synaptics\\Synaptics.exe")
    print("结果如下:")
    print(check1)
    print(check2)
    print(check3)
else:
    print("请使用Windows!")
    
