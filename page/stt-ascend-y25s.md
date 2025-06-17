# 昇腾学习资源

## 相关帖子

- 如何基于香橙派AIpro对视频/图像数据进行预处理；https://www.hiascend.com/forum/thread-0276149134135468062-1-1.html
- 如何基于香橙派AIpro开发AI推理应用；https://www.hiascend.com/forum/thread-0255148180622671006-1-1.html
- 如何在香橙派AIpro开发板升级CANN软件包；https://www.hiascend.com/forum/thread-0295148017012941005-1-1.html
- 香橙派AIpro学习资源一站式导航；https://www.hiascend.com/forum/thread-0285140173361311056-1-1.html
- 基于昇腾310的智能打卡系统（课程大作业）；https://www.hiascend.com/forum/thread-0225132546449339134-1-1.html
- 小藤 GPIO、40pin管脚使用教学；https://www.hiascend.com/forum/thread-0267128000548963084-1-1.html
- 张小白小藤官方样例测试汇总；https://www.hiascend.com/forum/thread-0247128437094382095-1-1.html
- 【CANN训练营】Atlas 200I DK A2开发板基于Yolact的实例分割模型；https://www.hiascend.com/forum/thread-0225125981716845011-1-1.html
- 昇腾计算硬件常用链接；https://www.hiascend.com/forum/thread-0214125199560918011-1-1.html
- Atlas200 DK A2与Arduino进行UART串口通信；https://www.hiascend.com/forum/thread-0260123430838468031-1-1.html
- 开发版上 torch-npu 跑不起来；https://www.hiascend.com/forum/thread-02108183175033158182-1-1.html

- 绑定到一个核；https://www.hiascend.com/forum/thread-0248184302877709045-1-1.html。给出了 torch_npu 的样例代码？

- Pytorch程序迁移 ；https://www.hiascend.com/forum/thread-0267127979937017079-1-1.html。信息：您好，一般是将pytorch模型转成onnx格式，再转成om格式，就可以在小藤上用了。//这边调推理卡用的就是om格式的模型文件 //好的，谢谢。我转过去试试

# GPIO

<!-- # gpio_pin = {
#     # 40PIN管脚号: {名称，GPIO组号，GPIO的管脚号}
#     "11" :{"name":"GPIO17","group":"2","pin":"18"},
#     "13" :{"name":"GPIO27","group":"2","pin":"06"},
#     "15" :{"name":"GPIO22","group":"2","pin":"15"},
#     "16" :{"name":"GPIO23","group":"2","pin":"16"},
#     "18" :{"name":"GPIO24","group":"0","pin":"25"},
#     "22" :{"name":"GPIO25","group":"0","pin":"02"},
#     "26" :{"name":"GPIO07","group":"2","pin":"19"},
#     "31" :{"name":"GPIO06","group":"2","pin":"20"},
#     "33" :{"name":"GPIO13","group":"4","pin":"00"},
#     "36" :{"name":"GPIO16","group":"2","pin":"17"},
#     "37" :{"name":"GPIO26","group":"0","pin":"03"},
#     } -->
0PIN管脚号 - GPIO组号 - GPIO的管脚号
- 11 - 02 - 18
- 13 - 01 - 06
- 15 - 02 - 15
- 16 - 02 - 16
- 18 - 00 - 25
- 22 - 00 - 02
- 26 - 02 - 19
- 31 - 02 - 20
- 33 - 04 - 00
- 36 - 02 - 17
- 37 - 00 - 03

参考：https://www.hiascend.com/document/detail/zh/Atlas%20200I%20A2/250RC1/RC/driverdevelopmentguide/atlasdg_11_0035.html

表3 GPIO管脚编号映射表
GROUP PIN_RANGESTART_IDEND_ID

0   0~31    0   31
1   0~31    32  63
2   0~31    64  95
3   0~31    476 507
4   0~31    128 159
5   0~31    160 191
7   0~31    224 255

此表说明GPIO管脚与其编号的对应关系。比如第N组第M个管脚的编号GPIO_ID为第N组的START_ID+M。

40PIN 之 13号管脚为例
- 对应组1、06号
- start_id = 32
- 因此，gpio_id = start_id + M = 32 + 6 = 38


<!-- # 导出GPIO -->
echo 38 > /sys/class/gpio/export

```
root@davinci-mini:/sys/class/gpio# ls -l
total 0
--w------- 1 root root 4096 Jun 16 13:45 export
lrwxrwxrwx 1 root root    0 Jun 16 13:45 gpio48 -> ../../devices/platform/c4050000.gpio/gpiochip3/gpio/gpio48
lrwxrwxrwx 1 root root    0 Jun 16  2025 gpiochip0 -> ../../devices/platform/c4040000.gpio/gpio/gpiochip0
```

<!-- # 设置为输出 -->
echo out > /sys/class/gpio/gpio38/direction

<!-- # 输出高电平 -->
echo 1 > /sys/class/gpio/gpio38/value
<!-- # 输出低电平 -->
echo 0 > /sys/class/gpio/gpio38/value

<!-- # 读取输入（需先设置为输入） -->
echo in > /sys/class/gpio/gpio35/direction
cat /sys/class/gpio/gpio35/value

<!-- # ATC 模型装换（250616） -->

参考：https://www.hiascend.com/document/detail/zh/Atlas200IDKA2DeveloperKit/23.0.RC2/Application%20Development%20Guide/tmuacop/tmuacop_0025.html?sub_id=%2Fzh%2FAtlas200IDKA2DeveloperKit%2F23.0.RC2%2FAppendices%2Fttmutat%2Fatctool_errorcode_0003.html

参考：https://www.hiascend.com/document/detail/zh/Atlas200IDKA2DeveloperKit/23.0.RC2/Appendices/ttmutat/atctool_000108.html

export ASCEND_SLOG_PRINT_TO_STDOUT=1
atc --model=model.onnx --framework=5 --output=model --soc_version=Ascend310B4 --log=warning
> framework=5,指ONNX
> sco_version=AScendB310B4，指昇腾开发板。可以运行 npu-smi info 查看

# 250615

<!-- 验证安装是否成功 -->
<!-- 作为Linux 命令执行 -->
<!-- NPU -->
time python3 -c "import torch; import torch_npu; from datetime import datetime; print(f'[{datetime.now()}][NPU] torch.randn start ...'); a = torch.randn(3, 4).npu(); print(a + a); print(f'[{datetime.now()}][Python] end.')"

<!-- NPU + torch.npu.set_compile_mode(jit_compile=False); -->
time python3 -c "import torch;import torch_npu; torch.npu.set_compile_mode(jit_compile=False); a = torch.randn(3, 4).npu(); print(a + a);"
time python3 -c "import torch; import torch_npu; from datetime import datetime; print(f'[{datetime.now()}][NPU + JIT_False] torch.randn start ...'); torch.npu.set_compile_mode(jit_compile=False); a = torch.randn(3, 4).npu(); print(a + a); print(f'[{datetime.now()}][Python] end.')"

<!-- CPU -->
<!-- time python3 -c "import torch;a = torch.randn(3, 4); print(a + a);" -->
time python3 -c "import torch; import torch_npu; from datetime import datetime; print(f'[{datetime.now()}][CPU] torch.randn start ...'); a = torch.randn(3, 4); print(a + a); print(f'[{datetime.now()}][Python] end.')"

<!-- CPU 但 import torch_npu -->
time python3 -c "import torch;import torch_npu; a = torch.randn(3, 4); print(a + a);"


time python3 -c "import torch; import torch_npu; from datetime import datetime; print(f'[{datetime.now()}][CPU] torch.randn start ...'); a = torch.randn(3, 4); print(a + a); print(f'[{datetime.now()}][Python] end.')"
time python3 -c "import torch; import torch_npu; from datetime import datetime; print(f'[{datetime.now()}][NPU + JIT_False] torch.randn start ...'); torch.npu.set_compile_mode(jit_compile=False); a = torch.randn(3, 4).npu(); print(a + a); print(f'[{datetime.now()}][Python] end.')"
time python3 -c "import torch; import torch_npu; from datetime import datetime; print(f'[{datetime.now()}][NPU] torch.randn start ...'); a = torch.randn(3, 4).npu(); print(a + a); print(f'[{datetime.now()}][Python] end.')"


# 一、安装固件、驱动、CANN等（250612，工单要求）

- CANN社区版，8.1.RC1.beta1
    Ascend-hdk-310b-npu-driver-soc_25.0.rc1.1_linux-aarch64.run
    Ascend-hdk-310b-npu-firmware-soc_7.7.0.1.231.run
    Ascend-cann-toolkit_8.1.RC1_linux-aarch64.run
    Ascend-cann-kernels-310b_8.1.RC1_linux-aarch64.run
- PyTorch : 2.1.0
- torch-npu: 2.1.0.post12
- Python: 3.10.x

<!-- - CANN社区版，8.2.RC1.alpha001
Ascend-hdk-310b-npu-firmware-soc_7.7.0.1.231.run
Ascend-hdk-310b-npu-driver-soc_25.0.rc1.1_linux-aarch64.run
Ascend-cann-kernels-310b_8.2.RC1.alpha001_linux-aarch64.run
Ascend-cann-toolkit_8.2.RC1.alpha001_linux-aarch64.run -->

## 1.1 安装驱动和固件

参考：https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/81RC1beta1/softwareinst/instg/instg_0005.html?Mode=PmIns&InstallType=local&OS=Ubuntu&Software=cannToolKit

1. apt 改成华为源
```
root@davinci-mini:~# cat /etc/apt/sources.list
deb https://mirrors.huaweicloud.com/ubuntu-ports/ jammy main restricted universe multiverse
deb https://mirrors.huaweicloud.com/ubuntu-ports/ jammy-security main restricted universe multiverse
deb https://mirrors.huaweicloud.com/ubuntu-ports/ jammy-updates main restricted universe multiverse
deb https://mirrors.huaweicloud.com/ubuntu-ports/ jammy-proposed main restricted universe multiverse
deb-src https://mirrors.huaweicloud.com/ubuntu-ports/ jammy main restricted universe multiverse
deb-src https://mirrors.huaweicloud.com/ubuntu-ports/ jammy-security main restricted universe multiverse
deb-src https://mirrors.huaweicloud.com/ubuntu-ports/ jammy-updates main restricted universe multiverse
deb-src https://mirrors.huaweicloud.com/ubuntu-ports/ jammy-proposed main restricted universe multiverse
```
2. apt update
```
root@davinci-mini:~# apt-get update
```
3. 安装依赖
```
root@davinci-mini:~# apt-get install -y dkms gcc 
```
> 没有apt-get install -y linux-headers-$(uname -r), 应为 uname -r 输出5.10.0，找不到这个包。
> 上面安装中，安装了 linux-headers-5.15.0-142 (5.15.0-142.152)，应该可以满足要求。

4. check
```
root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# ./Ascend-hdk-310b-npu-driver-soc_25.0.rc1.1_linux-aarch64.run --check
root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# ./Ascend-hdk-310b-npu-firmware-soc_7.7.0.1.231.run --check
```

5. 安装驱动
```
root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# ./Ascend-hdk-310b-npu-driver-soc_25.0.rc1.1_linux-aarch64.run --full
```
```
[Driver] [2025-06-12 13:30:57] [INFO]Driver package has been installed on the path /var/davinci, the version is 23.0.rc3, and the version of this package is 25.0.rc1.1,do you want to continue?  [y/n] 
...
[Driver] [2025-06-12 13:32:18] [INFO]Driver package installed successfully! Reboot needed for installation/upgrade to take effect! 
[Driver] [2025-06-12 13:32:18] [INFO]End time: 2025-06-12 13:32:18
```
> root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# ./Ascend-hdk-310b-npu-driver-soc_25.0.rc1.1_linux-aarch64.run --full --install-for-all 
不认识 --install-for-all，去掉。

6. （没有reboot，继续）安装固件
```
root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# ./Ascend-hdk-310b-npu-firmware-soc_7.7.0.1.231.run --full
```
```
[Firmware] [2025-06-12 13:34:33] [INFO]Firmware package installed successfully! Reboot now or after driver installation for the installation/upgrade to take effect.
[Firmware] [2025-06-12 13:34:33] [INFO]End time: 2025-06-12 13:34:33
```

7. reboot
```
root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# reboot
Connection to dk100 closed by remote host.
Connection to dk100 closed.
```

8. 重启后重新登录查看
```
root@davinci-mini:~# npu-smi info
+--------------------------------------------------------------------------------------------------------+
| npu-smi 25.0.rc1.1                               Version: 25.0.rc1.1                                   |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 0       310B4                 | OK              | 7.4          52                15    / 15            |
| 0       0                     | NA              | 0            1331 / 3514                             |
+===============================+=================+======================================================+
```

## 1.2 安装CANN



参考：https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/81RC1beta1/softwareinst/instg/instg_0008.html?Mode=PmIns&InstallType=local&OS=Ubuntu&Software=cannToolKit

1. 激活已有的 Python 3.10 虚拟环境
```
(gdenv310) root@davinci-mini:~# python3 --version
Python 3.10.12
(gdenv310) root@davinci-mini:~# which python3
/root/gdenv310/bin/python3
(gdenv310) root@davinci-mini:~# 
```
2. 安装依赖
```
(gdenv310) root@davinci-mini:~# apt-get install -y python3 python3-pip
(gdenv310) root@davinci-mini:~# pip3 install attrs cython numpy==1.24.0 decorator sympy cffi pyyaml pathlib2 psutil protobuf==3.20 scipy requests absl-py  
```

3. 安装toolkit
```
(gdenv310) root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# chmod +x Ascend-cann-toolkit_8.1.RC1_linux-aarch64.run
(gdenv310) root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# ./Ascend-cann-toolkit_8.1.RC1_linux-aarch64.run --check
```
```
(gdenv310) root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# ./Ascend-cann-toolkit_8.1.RC1_linux-aarch64.run --install
```
```
...
Release date: November,9th 2023Do you accept the EULA to install CANN?[Y/N]y
...
===========
= Summary =
===========

Driver:   Installed in /var/davinci/driver.
Toolkit:  Ascend-cann-toolkit_8.1.RC1_linux-aarch64 install success, installed in /usr/local/Ascend.

Please make sure that the environment variables have been configured.
-  To take effect for all users, you can add "source /usr/local/Ascend/ascend-toolkit/set_env.sh" to /etc/profile.
-  To take effect for current user, you can exec command below: source /usr/local/Ascend/ascend-toolkit/set_env.sh or add "source /usr/local/Ascend/ascend-toolkit/set_env.sh" to ~/.bashrc.
```
```
(gdenv310) root@davinci-mini:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux# cat ascend_toolkit_install.info 
package_name=Ascend-cann-toolkit
version=8.1.RC1
innerversion=V100R001C21SPC001B238
compatible_version=[V100R001C15],[V100R001C18],[V100R001C19],[V100R001C20],[V100R001C21]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.1.RC1/aarch64-linux
```
并且在 /etc/profile 中增加 `source /usr/local/Ascend/ascend-toolkit/set_env.sh`

4. 安装 kernels
```
(gdenv310) root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# chmod +x Ascend-cann-kernels-310b_8.1.RC1_linux-aarch64.run
(gdenv310) root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# ./Ascend-cann-kernels-310b_8.1.RC1_linux-aarch64.run --check
```
```
(gdenv310) root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# ./Ascend-cann-kernels-310b_8.1.RC1_linux-aarch64.run --devel
```
```
...
Release date: November,9th 2023Do you accept the EULA to install CANN?[Y/N]y
...
[kernels_310b] [20250612-15:02:08] [INFO] Ascend-cann-kernels-310b_8.1.RC1_linux-aarch64 install success. The installation path is /usr/local/Ascend/ascend-toolkit.
```
## 1.3 安装torch_npu 

```
(gdenv310) root@davinci-mini:~/tmp2506/pkg8.1.RC1.beta1# pip3 install torch-npu==2.1.0.post12
Looking in indexes: https://mirrors.huaweicloud.com/repository/pypi/simple
Collecting torch-npu==2.1.0.post12
  Downloading https://mirrors.huaweicloud.com/repository/pypi/packages/ab/62/6ef0dfcc565de7892dd70a503180e27a6debc4a6c98bfc73b969e6af5b16/torch_npu-2.1.0.post12-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (14.2 MB)
```

## 1.4 验证

1. 设置环境变量
```
(gdenv310) root@davinci-mini:~# export ASCEND_SLOG_PRINT_TO_STDOUT=1
(gdenv310) root@davinci-mini:~# export ASCEND_GLOBAL_LOG_LEVEL=0
```

```
(gdenv310) root@davinci-mini:~# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);" > err250612.log
```



---

## 安装 torch_npu

在昇腾开发板上安装 torch_npu。

参考：https://gitee.com/ascend/pytorch/tree/master/
参考：https://www.hiascend.com/document/detail/zh/Pytorch/700/index/index.html;Ascend Extension for PyTorch
参考：方式一：二进制软件包安装，https://www.hiascend.com/document/detail/zh/Pytorch/700/configandinstg/instg/insg_0004.html
参考：CANN，https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/82RC1alpha002/softwareinst/instg/instg_0003.html?Mode=PmIns&OS=Ubuntu&Software=cannNNRT

还安装 pyyaml pip3 install pyyaml
选择如下配置版本：

PyTorch 2.5.1
Python 3.11.x
torch-npu v2.5.1-7.00
CANN 8.1.RC1，4个包选了如下：
    Ascend-cann-kernels-310b_8.1.RC1_linux-aarch64.run
    Ascend-cann-nnrt_8.1.RC1_linux-aarch64.run
    Ascend-hdk-310b-npu-driver-soc_25.0.rc1.1_linux-aarch64.run
    Ascend-hdk-310b-npu-firmware-soc_7.7.0.1.231.run

(myenv311) root@davinci-mini:/home1/root/tmp2506# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);"


Traceback (most recent call last):
  File "/home1/root/myenv311/lib/python3.11/site-packages/torch/__init__.py", line 2637, in _import_device_backends
    entrypoint = backend_extension.load()
                 ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/metadata/__init__.py", line 201, in load
    module = import_module(match.group('module'))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1206, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/home1/root/myenv311/lib/python3.11/site-packages/torch_npu/__init__.py", line 39, in <module>
    import torch_npu.npu
  File "/home1/root/myenv311/lib/python3.11/site-packages/torch_npu/npu/__init__.py", line 331, in <module>
    from .memory import *  # noqa: F403
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home1/root/myenv311/lib/python3.11/site-packages/torch_npu/npu/memory.py", line 16, in <module>
    from ._memory_viz import memory as _memory, segments as _segments
  File "/home1/root/myenv311/lib/python3.11/site-packages/torch_npu/npu/_memory_viz.py", line 11, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/home1/root/myenv311/lib/python3.11/site-packages/torch/__init__.py", line 2665, in <module>
    _import_device_backends()
  File "/home1/root/myenv311/lib/python3.11/site-packages/torch/__init__.py", line 2641, in _import_device_backends
    raise RuntimeError(
RuntimeError: Failed to load the backend extension: torch_npu. You can disable extension auto-loading with TORCH_DEVICE_BACKEND_AUTOLOAD=0.

-- 就安装 pyyaml

========

(myenv311) root@davinci-mini:/home1/root/tmp2506# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is Add.
Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
[ERROR] 2025-06-04-09:22:23 (PID:80151, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
EH9999: Inner Error!
EH9999  [Init][Env]init env failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        TraceBack (most recent call last):
        build op model failed, result = 500001[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

- 应该是CANN相关问题


===========
(myenv311) root@davinci-mini:~/tmp2506# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);"
/root/myenv311/lib/python3.11/site-packages/torch/_subclasses/functional_tensor.py:295: UserWarning: Failed to initialize NumPy: No module named 'numpy' (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
  cpu = _conversion_method_template(device=torch.device("cpu"))
Traceback (most recent call last):
  File "/root/myenv311/lib/python3.11/site-packages/torch/__init__.py", line 2637, in _import_device_backends
    entrypoint = backend_extension.load()
                 ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/metadata/__init__.py", line 201, in load
    module = import_module(match.group('module'))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1206, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/__init__.py", line 66, in <module>
    from torch_npu import profiler
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/profiler/__init__.py", line 3, in <module>
    from .profiler import (
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/profiler/profiler.py", line 13, in <module>
    from .profiler_interface import _ProfInterface, supported_activities
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/profiler/profiler_interface.py", line 31, in <module>
    from .analysis._npu_profiler import NpuProfiler
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/profiler/analysis/_npu_profiler.py", line 6, in <module>
    from ._profiling_parser import ProfilingParser
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/profiler/analysis/_profiling_parser.py", line 10, in <module>
    from .prof_config._parser_config import ParserConfig
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/profiler/analysis/prof_config/_parser_config.py", line 30, in <module>
    from ..prof_view._memory_timeline_parser import MemoryTimelineParser
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/profiler/analysis/prof_view/_memory_timeline_parser.py", line 10, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/root/myenv311/lib/python3.11/site-packages/torch/__init__.py", line 2665, in <module>
    _import_device_backends()
  File "/root/myenv311/lib/python3.11/site-packages/torch/__init__.py", line 2641, in _import_device_backends
    raise RuntimeError(
RuntimeError: Failed to load the backend extension: torch_npu. You can disable extension auto-loading with TORCH_DEVICE_BACKEND_AUTOLOAD=0.

========
Installing collected packages: numpy
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
te 0.4.0 requires attrs, which is not installed.
te 0.4.0 requires cloudpickle, which is not installed.
te 0.4.0 requires decorator, which is not installed.
te 0.4.0 requires psutil, which is not installed.
te 0.4.0 requires scipy, which is not installed.
te 0.4.0 requires synr==0.5.0, which is not installed.
te 0.4.0 requires tornado, which is not installed.
schedule-search 0.0.1 requires absl-py, which is not installed.
schedule-search 0.0.1 requires decorator, which is not installed.
opc-tool 0.1.0 requires attrs, which is not installed.
opc-tool 0.1.0 requires decorator, which is not installed.
opc-tool 0.1.0 requires psutil, which is not installed.
auto-tune 0.1.0 requires decorator, which is not installed.
Successfully installed numpy-2.2.6
========

(myenv311) root@davinci-mini:~/tmp2506# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is Add.
Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
Note: ASCEND_LAUNCH_BLOCKING=1 will force ops to run in synchronous mode, resulting in performance degradation. Please unset ASCEND_LAUNCH_BLOCKING in time after debugging.
[ERROR] 2025-06-04-15:25:25 (PID:160356, Device:0, RankID:-1) ERR00100 PTA call acl api failed.
EH9999: Inner Error!
EH9999  [Init][Env]init env failed![FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        TraceBack (most recent call last):
        build op model failed, result = 500001[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]

=========
(myenv311) root@davinci-mini:~# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);"
Traceback (most recent call last):
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/__init__.py", line 39, in <module>
    import torch_npu.npu
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/npu/__init__.py", line 127, in <module>
    from torch_npu.utils import _should_print_warning
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/utils/__init__.py", line 1, in <module>
    from torch_npu import _C
ImportError: /usr/local/Ascend/ascend-toolkit/latest/lib64/libdatatransfer.so: undefined symbol: _Z15DlogWithKVInneriiP5tagKViPKcz

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/root/myenv311/lib/python3.11/site-packages/torch/__init__.py", line 2637, in _import_device_backends
    entrypoint = backend_extension.load()
                 ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/metadata/__init__.py", line 201, in load
    module = import_module(match.group('module'))
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1206, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1178, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1149, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 690, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 940, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/__init__.py", line 41, in <module>
    from torch_npu.utils._error_code import ErrCode, pta_error
  File "/root/myenv311/lib/python3.11/site-packages/torch_npu/utils/__init__.py", line 1, in <module>
    from torch_npu import _C
ImportError: /usr/local/Ascend/ascend-toolkit/latest/lib64/libdatatransfer.so: undefined symbol: _Z15DlogWithKVInneriiP5tagKViPKcz

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/root/myenv311/lib/python3.11/site-packages/torch/__init__.py", line 2665, in <module>
    _import_device_backends()
  File "/root/myenv311/lib/python3.11/site-packages/torch/__init__.py", line 2641, in _import_device_backends
    raise RuntimeError(
RuntimeError: Failed to load the backend extension: torch_npu. You can disable extension auto-loading with TORCH_DEVICE_BACKEND_AUTOLOAD=0.


250605
====
pip3 install attrs cython numpy==1.24.0 decorator sympy cffi pyyaml pathlib2 psutil protobuf==3.20 scipy requests absl-py


### 安装 torch_npu

昇腾社区：https://www.hiascend.com/zh
选择开发者，到：https://www.hiascend.com/developer
再选开发|资源下载中心，到：https://www.hiascend.com/developer/download
    选社区版，
    AI框架：选PyTorch
    产品系列：开发者套件
    产品型号：Atlas 200I DK A2 开发者套件
    点：查找配套资源，
    
进入：https://www.hiascend.com/developer/download/community/result?module=pt+cann&product=5&model=25
    PyTorch：选v5.0.0-pytorch2.1.0
        点获取源码，进入：https://gitee.com/ascend/pytorch//releases/tag/v5.0.0-pytorch2.1.0
        点击下载： torch_npu-2.1.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
    CANN：选了相关包

在https://gitee.com/ascend/pytorch//releases/tag/v5.0.0-pytorch2.1.0，点pytorch，
进入https://gitee.com/ascend/pytorch 

PyTorch 2.10
Python 3.10

Python：3.10（根据 torch_npu whl包上的cp310选择的）
PyTorch：2.10
torch_npu：torch_npu-2.1.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
CANN 7.00 选了：
    Ascend-cann-kernels-310b_7.0.0_linux.run
    Ascend-cann-toolkit_7.0.0_linux-aarch64.run
    Ascend-hdk-310b-npu-driver-soc_23.0.0_linux-aarch64.run
    Ascend-hdk-310b-npu-firmware-soc_7.1.0.3.220.run

#### 安装驱动和固件

apt-get install -y dkms gcc linux-headers-$(uname -r)
    分成几个执行，因为linux-headers-$(uname -r)不存在
    - apt-get install dkms，OK
    - apt-get install gcc，已存在
    - uname -r = 5.10.0 ,报 linux-headers-5.10.0 不存在。apt list | grep linux-headers，有一堆高版本的，比如 5.15.0-xx

chmod +x

./Ascend-hdk-310b-npu-driver-soc_23.0.0_linux-aarch64.run --full --install-for-all
    不认识--install-for-all
./Ascend-hdk-310b-npu-driver-soc_23.0.0_linux-aarch64.run --full
    Driver package has been installed on the path /var/davinci, the version is 25.0.rc1.1, and the version of this package is 23.0.0,do you want to continue?  [y/n] y
(gdenv310) root@davinci-mini:~/tmp2506/pkg2# ./Ascend-hdk-310b-npu-driver-soc_23.0.0_linux-aarch64.run --full
Verifying archive integrity...  100%   SHA256 checksums are OK. All good.
Uncompressing ASCEND-HDK-310B-NPU DRIVER RUN PACKAGE  100%  
[Driver] [2025-06-06 08:55:06] [INFO]Start time: 2025-06-06 08:55:06
[Driver] [2025-06-06 08:55:06] [INFO]LogFile: /var/log/ascend_seclog/ascend_install.log
[Driver] [2025-06-06 08:55:06] [INFO]OperationLogFile: /var/log/ascend_seclog/operation.log
[Driver] [2025-06-06 08:55:06] [INFO]base version is 25.0.rc1.1.
[Driver] [2025-06-06 08:55:06] [WARNING]Do not power off or restart the system during the installation/upgrade
[Driver] [2025-06-06 08:55:06] [INFO]set username and usergroup, HwHiAiUser:HwHiAiUser
[Driver] [2025-06-06 08:55:06] [INFO]driver and firmware version relationship check success
[Driver] [2025-06-06 08:55:06] [INFO]Driver package has been installed on the path /var/davinci, the version is 25.0.rc1.1, and the version of this package is 23.0.0,do you want to continue?  [y/n] 
y
[Driver] [2025-06-06 08:55:38] [INFO]upgradePercentage:10%
[Driver] [2025-06-06 08:55:38] [INFO]upgradePercentage:40%
[Driver] [2025-06-06 08:55:52] [INFO]upgradePercentage:60%
[Driver] [2025-06-06 08:55:52] [INFO]upgradePercentage:80%
[Driver] [2025-06-06 08:56:00] [INFO]upgradePercentage:100%
[Driver] [2025-06-06 08:56:00] [INFO]Driver package installed successfully! Reboot needed for installation/upgrade to take effect! 
[Driver] [2025-06-06 08:56:00] [INFO]End time: 2025-06-06 08:56:00

----
(gdenv310) root@davinci-mini:~/tmp2506/pkg2# ./Ascend-hdk-310b-npu-firmware-soc_7.1.0.3.220.run --full
Verifying archive integrity...  100%   SHA256 checksums are OK. All good.
Uncompressing ASCEND310B FIRMWARE RUN PACKAGE  100%  
[Firmware] [2025-06-06 08:56:55] [INFO]Start time: 2025-06-06 08:56:55
[Firmware] [2025-06-06 08:56:55] [INFO]LogFile: /var/log/ascend_seclog/ascend_install.log
[Firmware] [2025-06-06 08:56:55] [INFO]OperationLogFile: /var/log/ascend_seclog/operation.log
[Firmware] [2025-06-06 08:56:55] [INFO]base version is 7.7.0.1.231.
[Firmware] [2025-06-06 08:56:55] [WARNING]Do not power off or restart the system during the installation/upgrade
[Firmware] [2025-06-06 08:56:55] [INFO]Firmware package has been installed on the path /usr/local/Ascend, the version is 7.7.0.1.231, and the version of this package is 7.1.0.3.220,do you want to continue?  [y/n] 
y
[Firmware] [2025-06-06 08:57:05] [INFO]upgradePercentage: 0%
[Firmware] [2025-06-06 08:57:14] [INFO]upgradePercentage: 6%
[Firmware] [2025-06-06 08:57:22] [INFO]upgradePercentage: 84%
[Firmware] [2025-06-06 08:57:30] [INFO]upgradePercentage: 100%
[Firmware] [2025-06-06 08:57:30] [INFO]Firmware package installed successfully! Reboot now or after driver installation for the installation/upgrade to take effect.
[Firmware] [2025-06-06 08:57:30] [INFO]End time: 2025-06-06 08:57:30

---

reboot
---
(base) root@davinci-mini:~# npu-smi info
+--------------------------------------------------------------------------------------------------------+
| npu-smi 23.0.0                                   Version: 23.0.0                                       |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 0       310B4                 | OK              | 7.6          51                15    / 15            |
| 0       0                     | NA              | 0            1350 / 3514                             |
+===============================+=================+======================================================+

(base) root@davinci-mini:~# vim /etc/profile
(base) root@davinci-mini:~# source /etc/profile
配置最大线程数（可选）

---
root@davinci-mini:~/gdenv310/bin# source activate
(gdenv310) root@davinci-mini:~/gdenv310/bin# ldd $(which python3.10)
	linux-vdso.so.1 (0x0000e7ffc6b1a000)
	libm.so.6 => /lib/aarch64-linux-gnu/libm.so.6 (0x0000e7ffc6470000)
	libexpat.so.1 => /lib/aarch64-linux-gnu/libexpat.so.1 (0x0000e7ffc6430000)
	libz.so.1 => /lib/aarch64-linux-gnu/libz.so.1 (0x0000e7ffc6400000)
	libc.so.6 => /lib/aarch64-linux-gnu/libc.so.6 (0x0000e7ffc6250000)
	/lib/ld-linux-aarch64.so.1 (0x0000e7ffc6ae1000)
(gdenv310) root@davinci-mini:~/gdenv310/bin# 

CANN支持Python3.7.x至3.11.4版本，若未安装、版本不满足或者未包含动态库libpython3.x.so请参考编译安装Python操作。
有点不符合

---
pip3 install attrs cython numpy==1.24.0 decorator sympy cffi pyyaml pathlib2 psutil protobuf==3.20 scipy requests absl-py     
安装依赖
-i https://repo.huaweicloud.com/repository/pypi/simple/ 用华为源安装成功

---

安装Toolkit开发套件包
chmod +x
(gdenv310) root@davinci-mini:~/tmp2506/pkg2# ./Ascend-cann-toolkit_7.0.0_linux-aarch64.run --install

===========
= Summary =
===========

Driver:   Installed in /var/davinci/driver.
Toolkit:  Ascend-cann-toolkit_7.0.0_linux-aarch64 install success, installed in /usr/local/Ascend.

Please make sure that the environment variables have been configured.
-  To take effect for all users, you can add "source /usr/local/Ascend/ascend-toolkit/set_env.sh" to /etc/profile.
-  To take effect for current user, you can exec command below: source /usr/local/Ascend/ascend-toolkit/set_env.sh or add "source /usr/local/Ascend/ascend-toolkit/set_env.sh" to ~/.bashrc.

(gdenv310) root@davinci-mini:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux# cat ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=7.0.0
innerversion=V100R001C15SPC003B226
compatible_version=[V100R001C15],[V100R001C29],[V100R001C30],[V100R001C13],[V100R003C10],[V100R003C11]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/7.0.0/aarch64-linux


=====
安装kernels

(gdenv310) root@davinci-mini:~/tmp2506/pkg2# ./Ascend-cann-kernels-310b_7.0.0_linux.run --devel

Do you accept the EULA to install CANN?[Y/N]y
[kernels_310b] [20250606-10:41:58] [INFO] install start
[kernels_310b] [20250606-10:41:58] [INFO] The installation path is /usr/local/Ascend/ascend-toolkit.
[kernels_310b] [20250606-10:41:58] [INFO] install package Ascend310B-opp_kernel-7.1.0.3.220.run start
[kernels_310b] [20250606-10:44:03] [INFO] Ascend310B-opp_kernel-7.1.0.3.220.run --full --quiet --nox11 install success
[kernels_310b] [20250606-10:44:03] [INFO] Ascend-cann-kernels-310b_7.0.0_linux install success. The installation path is /usr/local/Ascend/ascend-toolkit.

(gdenv310) root@davinci-mini:/usr/local/Ascend/ascend-toolkit/latest/opp# cat version.info
Version=7.1.0.3.220
version_dir=7.0.0

om ，ACL（PyACL）

==== 
安装 PyTorch 2.1.0
(gdenv310) root@davinci-mini:~# pip3 install torch==2.1.0

====
安装 torch_npu
(gdenv310) root@davinci-mini:~/tmp2506/pkg2# pip3 install torch_npu-2.1.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl


====

(gdenv310) root@davinci-mini:~/tmp2506# cat test_npu_250606.py
import torch
import torch_npu

# 检查 NPU 设备是否可识别
print(torch_npu.npu.is_available())  # 期望输出 True

# 尝试在 NPU 上运行计算
if torch_npu.npu.is_available():
    a = torch.randn(3, 4).npu()
    print(a + a)
else:
    print("NPU 不可用，请检查驱动和版本兼容性。")

/root/gdenv310/lib/python3.10/site-packages/torch_npu/dynamo/__init__.py:18: UserWarning: Register eager implementation for the 'npu' backend of dynamo, as torch_npu was not compiled with torchair.
  warnings.warn(
True
Traceback (most recent call last):
  File "/root/tmp2506/test_npu_250606.py", line 9, in <module>
    a = torch.randn(3, 4).npu()
  File "/root/gdenv310/lib/python3.10/site-packages/torch/utils/backend_registration.py", line 153, in wrap_tensor_to
    device_idx = _normalization_device(custom_backend_name, device)
  File "/root/gdenv310/lib/python3.10/site-packages/torch/utils/backend_registration.py", line 109, in _normalization_device
    return _get_current_device_index()
  File "/root/gdenv310/lib/python3.10/site-packages/torch/utils/backend_registration.py", line 103, in _get_current_device_index
    return getattr(getattr(torch, custom_backend_name), _get_device_index)()
  File "/root/gdenv310/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 51, in current_device
    torch_npu.npu._lazy_init()
  File "/root/gdenv310/lib/python3.10/site-packages/torch_npu/npu/__init__.py", line 203, in _lazy_init
    torch_npu._C._npu_init()
RuntimeError: Unsupported soc version: Ascend310B4

====
安装 ./Ascend-cann-toolkit_7.0.RC1_linux-aarch64.run --install

参考：求助！Unsupported soc version: Ascend310B4！；https://www.hiascend.com/forum/thread-0280136700753784025-1-1.html

还是没有用！！！


# 再次换版本安装（250608）

## 安装依赖
```bash
(myenv311) root@davinci-mini:~/tmp2506/pkg4% pip3 install attrs cython numpy==1.24.0 decorator sympy cffi pyyaml pathlib2 psutil protobuf==3.20 scipy requests absl-py
pip3 install attrs cython numpy==1.24.0 decorator sympy cffi pyyaml pathlib2 psutil protobuf==3.20 scipy requests absl-py
```
<mark>有一些error，后续解决吧</mark>
Installing collected packages: mpmath, urllib3, sympy, six, pyyaml, pycparser, psutil, protobuf, numpy, idna, decorator, cython, charset-normalizer, certifi, attrs, absl-py, scipy, requests, pathlib2, cffi
<mark>
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
te 0.4.0 requires cloudpickle, which is not installed.
te 0.4.0 requires synr==0.5.0, which is not installed.
te 0.4.0 requires tornado, which is not installed.
op-compile-tool 0.1.0 requires getopt, which is not installed.
op-compile-tool 0.1.0 requires inspect, which is not installed.
op-compile-tool 0.1.0 requires multiprocessing, which is not installed.
</mark>
Successfully installed absl-py-2.3.0 attrs-25.3.0 certifi-2025.4.26 cffi-1.17.1 charset-normalizer-3.4.2 cython-3.1.1 decorator-5.2.1 idna-3.10 mpmath-1.3.0 numpy-1.24.0 pathlib2-2.3.7.post1 protobuf-3.20.0 psutil-7.0.0 pycparser-2.22 pyyaml-6.0.2 requests-2.32.3 scipy-1.15.3 six-1.17.0 sympy-1.14.0 urllib3-2.4.0

## 安装tPyTorch 2.1.0

(myenv311) root@davinci-mini:~/tmp2506/pkg4# pip3 install torch==2.1.0
Successfully installed MarkupSafe-3.0.2 filelock-3.18.0 fsspec-2025.5.1 jinja2-3.1.6 networkx-3.5 torch-2.1.0 typing-extensions-4.14.0

## 安装torch-nput2.1.0post
(myenv311) root@davinci-mini:~/tmp2506/pkg4# pip3 install torch_npu-2.1.0.post10-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
Successfully installed torch-npu-2.1.0.post10

至此，pip3 list 查看

(myenv311) root@davinci-mini:~/tmp2506/pkg4# pip3 list | grep torch

torch              2.1.0
torch-npu          2.1.0.post10

## 验证

(myenv311) root@davinci-mini:~/tmp2506/pkg4# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);"
<frozen importlib._bootstrap>:1049: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:1049: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:673: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/dsl/unify_schedule/extract_image_patches_without_cbuf_schedule.py:317: SyntaxWarning: "is not" with a literal. Did you mean "!="?
  if _ is not 1:
^CProcess ForkServerPoolWorker-4:
Process ForkServerPoolWorker-3:


### 

## 驱动和固件

### 安装依赖

(myenv311) root@davinci-mini:~/tmp2506/pkg4# apt-get install -y dkms
在dkms安装中，gcc也看到装了，linux-headers-$(uname -r)（版本高一些的）也装了

重启 reboot

250609：mac共享不成功。各种重新设置、重启，就又可以了。


### 先装固件

原来没有固件

(myenv311) root@davinci-mini:~/tmp2506/pkg4# ./Ascend-hdk-310b-npu-firmware-soc_7.5.0.2.220.run --full
[Firmware] [2025-06-09 12:27:43] [INFO]Firmware package installed successfully! Reboot now or after driver installation for the installation/upgrade to take effect.
[Firmware] [2025-06-09 12:27:43] [INFO]End time: 2025-06-09 12:27:43

(myenv311) root@davinci-mini:~/tmp2506/pkg4# ./Ascend-hdk-310b-npu-driver-soc_24.1.0_linux-aarch64.run --full

--install-for-all 不认识

[Driver] [2025-06-09 12:30:54] [INFO]Driver package installed successfully! Reboot needed for installation/upgrade to take effect! 
[Driver] [2025-06-09 12:30:54] [INFO]End time: 2025-06-09 12:30:54

reboot

(base) root@davinci-mini:~# npu-smi info
+--------------------------------------------------------------------------------------------------------+
| npu-smi 24.1.0                                   Version: 24.1.0                                       |
+-------------------------------+-----------------+------------------------------------------------------+
| NPU     Name                  | Health          | Power(W)     Temp(C)           Hugepages-Usage(page) |
| Chip    Device                | Bus-Id          | AICore(%)    Memory-Usage(MB)                        |
+===============================+=================+======================================================+
| 0       310B4                 | OK              | 7.7          53                15    / 15            |
| 0       0                     | NA              | 0            1327 / 3514                             |
+===============================+=================+======================================================+


(base) root@davinci-mini:~/tmp2506/pkg4# ./Ascend-hdk-310b-npu-driver-soc_24.1.0_linux-aarch64.run --check
Makeself logfile: /root/log/makeself/makeself.log
Verifying archive integrity...  100%   SHA256 checksums are OK. All good.
Verifying archive integrity...  100%   SHA256 checksums are OK. All good.
Uncompressing ASCEND-HDK-310B-NPU DRIVER RUN PACKAGE  100%  
[Driver] [2025-06-09 12:34:47] [INFO]Start time: 2025-06-09 12:34:47
[Driver] [2025-06-09 12:34:47] [INFO]LogFile: /var/log/ascend_seclog/ascend_install.log
[Driver] [2025-06-09 12:34:47] [INFO]OperationLogFile: /var/log/ascend_seclog/operation.log
[Driver] [2025-06-09 12:34:48] [INFO]base version is 24.1.0.
[Driver] [2025-06-09 12:34:48] [INFO]driver and firmware version relationship check success
[Driver] [2025-06-09 12:34:48] [INFO]End time: 2025-06-09 12:34:48

(base) root@davinci-mini:~/tmp2506/pkg4# ./Ascend-hdk-310b-npu-firmware-soc_7.5.0.2.220.run --check
Makeself logfile: /root/log/makeself/makeself.log
Verifying archive integrity...  100%   SHA256 checksums are OK. All good.
Verifying archive integrity...  100%   SHA256 checksums are OK. All good.
Uncompressing ASCEND310B FIRMWARE RUN PACKAGE  100%  
[Firmware] [2025-06-09 12:35:02] [INFO]Start time: 2025-06-09 12:35:02
[Firmware] [2025-06-09 12:35:02] [INFO]LogFile: /var/log/ascend_seclog/ascend_install.log
[Firmware] [2025-06-09 12:35:02] [INFO]OperationLogFile: /var/log/ascend_seclog/operation.log
[Firmware] [2025-06-09 12:35:02] [INFO]base version is 7.5.0.2.220.
[Firmware] [2025-06-09 12:35:02] [INFO]End time: 2025-06-09 12:35:02


## 安装依赖

(myenv311) root@davinci-mini:~/myenv311/bin# apt-get install python3
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
python3 is already the newest version (3.10.6-1~22.04.1).
0 upgraded, 0 newly installed, 0 to remove and 384 not upgraded.
(myenv311) root@davinci-mini:~/myenv311/bin# python3
Python 3.11.0rc1 (main, Aug 12 2022, 10:02:14) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
(myenv311) root@davinci-mini:~/myenv311/bin# which python3
/root/myenv311/bin/python3


(myenv311) root@davinci-mini:~/myenv311/bin# apt-get install python3-pip
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libexpat1 libexpat1-dev libjs-sphinxdoc libjs-underscore libpython3-dev libpython3.10 libpython3.10-dev libpython3.10-minimal libpython3.10-stdlib python3-dev python3-wheel python3.10
  python3.10-dev python3.10-minimal

  Failed to retrieve available kernel versions.

Failed to check for processor microcode upgrades.

Restarting services...
Daemons using outdated libraries
--------------------------------

  1. avahi-daemon.service  2. dbus.service  3. networkd-dispatcher.service  4. polkit.service  5. unattended-upgrades.service  6. vncserver@1.service  7. none of the above

(Enter the items or ranges you want to select, separated by spaces.)

Which services should be restarted? 

reboot

### 编译安装Python3.11.0

./configure --prefix=${HOME}/python3.11.0 --enable-loadable-sqlite-extensions --enable-shared
make
make install

### 安装依赖

pip3 install attrs cython numpy==1.24.0 decorator sympy cffi pyyaml pathlib2 psutil protobuf==3.20 scipy requests absl-py --user

## 安装Toolkit开发套件包

root@davinci-mini:~/tmp2506/pkg4# ./Ascend-cann-toolkit_8.0.0_linux-aarch64.run --install
root@davinci-mini:~/tmp2506/pkg4# ./Ascend-cann-toolkit_8.0.0_linux-aarch64.run --install
Verifying archive integrity...  100%   SHA256 checksums are OK. All good.
Uncompressing ASCEND_RUN_PACKAGE  100%  
[Toolkit] [20250609-15:21:25] [INFO] LogFile:/var/log/ascend_seclog/ascend_toolkit_install.log

[Toolkit] [20250609-15:42:24] [INFO] install package Ascend-test-ops_8.0.0_linux.run start
[Toolkit] [20250609-15:42:25] [INFO] Ascend-test-ops_8.0.0_linux.run --full --quiet --nox11 install success
[Toolkit] [20250609-15:42:25] [INFO] Write Toolkit_InstallPath to /etc/Ascend/ascend_cann_install.info.

===========
= Summary =
===========

Driver:   Installed in /var/davinci/driver.
Toolkit:  Ascend-cann-toolkit_8.0.0_linux-aarch64 install success, installed in /usr/local/Ascend.

Please make sure that the environment variables have been configured.
-  To take effect for all users, you can add "source /usr/local/Ascend/ascend-toolkit/set_env.sh" to /etc/profile.
-  To take effect for current user, you can exec command below: source /usr/local/Ascend/ascend-toolkit/set_env.sh or add "source /usr/local/Ascend/ascend-toolkit/set_env.sh" to ~/.bashrc.


root@davinci-mini:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux# cat ascend_toolkit_install.info
package_name=Ascend-cann-toolkit
version=8.0.0
innerversion=V100R001C20SPC001B251
compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux


root@davinci-mini:~/tmp2506/pkg4# ./Ascend-cann-kernels-310b_8.0.0_linux-aarch64.run --devel
Verifying archive integrity...  100%   SHA256 checksums are OK. All good.
Uncompressing ASCEND_RUN_PACKAGE  100%  
[kernels_310b] [20250609-15:51:49] [INFO] LogFile:/var/log/ascend_seclog/ascend_kernels_310b_install.log

[kernels_310b] [20250609-15:58:32] [INFO] Ascend310B-opp_kernel-7.6.0.1.220-linux.aarch64.run --devel --quiet --nox11 install success
[kernels_310b] [20250609-15:58:32] [INFO] Ascend-cann-kernels-310b_8.0.0_linux-aarch64 install success. The installation path is /usr/local/Ascend/ascend-toolkit.

----

固件和驱动：
Ascend-hdk-310b-npu-driver-soc_25.0.rc1.1_linux-aarch64.run
Ascend-hdk-310b-npu-firmware-soc_7.7.0.1.231.run

资源下载：
https://www.hiascend.com/developer/download/community/result?module=pt+cann
应该选哪个？
CANN最高还只是 8.1.RC1.beta1

source /usr/local/Ascend/ascend-toolkit/set_env.sh

PyTorch：2.1.0
Python：3.10
系统架构：AArch64
CANN版本：8.0.RC2
安装方式：Pip
torch_npu：6.0.rc2

# （失败）尝试安装（250609）

CANN:8.00
    (base) root@davinci-mini:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux# cat ascend_toolkit_install.info
    package_name=Ascend-cann-toolkit
    version=8.0.0
    innerversion=V100R001C20SPC001B251
    compatible_version=[V100R001C15],[V100R001C17],[V100R001C18],[V100R001C19],[V100R001C20]
    arch=aarch64
    os=linux
    path=/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux
    (base) root@davinci-mini:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux# 

PyTorch: 2.1.0
torch-npu: 2.1.0.post10

    https://gitee.com/ascend/pytorch
    CANN版本	支持的PyTorch版本	支持的Extension版本	Gitee分支
    CANN 8.0.0	2.4.0	2.4.0.post2	v2.4.0-6.0.0
    2.3.1	2.3.1.post4	v2.3.1-6.0.0
    2.1.0	2.1.0.post10	v2.1.0-6.0.0

Python: 3.10.x
    https://gitee.com/ascend/pytorch
    PyTorch版本	Python版本
    PyTorch1.11.0	Python3.7.x(>=3.7.5), Python3.8.x, Python3.9.x, Python3.10.x
    PyTorch2.1.0	Python3.8.x, Python3.9.x, Python3.10.x, Python 3.11.x

(gdenv310) root@davinci-mini:~/gdenv310/bin# source /usr/local/Ascend/ascend-toolkit/set_env.sh
(gdenv310) root@davinci-mini:~/gdenv310/bin# python3 -c "import torch;import torch_npu; from datetime import datetime;print(datetime.now()); a = torch.randn(3, 4).npu(); print(a + a);print(datetime.now());"

A module that was compiled using NumPy 1.x cannot be run in
NumPy 2.2.6 as it may crash. To support both 1.x and 2.x
versions of NumPy, modules must be compiled with NumPy 2.0.
Some module may need to rebuild instead e.g. with 'pybind11>=2.12'.

If you are a user of the module, the easiest solution will be to
downgrade to 'numpy<2' or try to upgrade the affected module.
We expect that some modules will need time to support NumPy 2.

Traceback (most recent call last):  File "<string>", line 1, in <module>
  File "/root/gdenv310/lib/python3.10/site-packages/torch/__init__.py", line 1382, in <module>
    from .functional import *  # noqa: F403
  File "/root/gdenv310/lib/python3.10/site-packages/torch/functional.py", line 7, in <module>
    import torch.nn.functional as F
  File "/root/gdenv310/lib/python3.10/site-packages/torch/nn/__init__.py", line 1, in <module>
    from .modules import *  # noqa: F403
  File "/root/gdenv310/lib/python3.10/site-packages/torch/nn/modules/__init__.py", line 35, in <module>
    from .transformer import TransformerEncoder, TransformerDecoder, \
  File "/root/gdenv310/lib/python3.10/site-packages/torch/nn/modules/transformer.py", line 20, in <module>
    device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),
/root/gdenv310/lib/python3.10/site-packages/torch/nn/modules/transformer.py:20: UserWarning: Failed to initialize NumPy: _ARRAY_API not found (Triggered internally at /pytorch/torch/csrc/utils/tensor_numpy.cpp:84.)
  device: torch.device = torch.device(torch._C._get_default_device()),  # torch.device('cpu'),
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/root/gdenv310/lib/python3.10/site-packages/torch_npu/__init__.py", line 17, in <module>
    import torch_npu.npu
  File "/root/gdenv310/lib/python3.10/site-packages/torch_npu/npu/__init__.py", line 306, in <module>
    from .memory import *  # noqa: F403
  File "/root/gdenv310/lib/python3.10/site-packages/torch_npu/npu/memory.py", line 16, in <module>
    from ._memory_viz import memory as _memory, segments as _segments
  File "/root/gdenv310/lib/python3.10/site-packages/torch_npu/npu/_memory_viz.py", line 11, in <module>
    import yaml
ModuleNotFoundError: No module named 'yaml'



(gdenv310) root@davinci-mini:~/gdenv310/bin# pip3 list | grep numpy
numpy                  2.2.6
(gdenv310) root@davinci-mini:~/gdenv310/bin# pip3 install numpy==1.24.0
Looking in indexes: https://mirrors.huaweicloud.com/repository/pypi/simple
Collecting numpy==1.24.0
  Downloading https://mirrors.huaweicloud.com/repository/pypi/packages/9c/46/49ba030beef06d8a5d64fd533b9f837078b1a84ddda1a4ef18081ba5fbfb/numpy-1.24.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (14.0 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.0/14.0 MB 2.7 MB/s eta 0:00:00
Installing collected packages: numpy
  Attempting uninstall: numpy
    Found existing installation: numpy 2.2.6
    Uninstalling numpy-2.2.6:
      Successfully uninstalled numpy-2.2.6
Successfully installed numpy-1.24.0
(gdenv310) root@davinci-mini:~/gdenv310/bin# pip3 list | grep numpy
numpy                  1.24.0

(gdenv310) root@davinci-mini:~/gdenv310/bin# pip3 install pyyaml
Looking in indexes: https://mirrors.huaweicloud.com/repository/pypi/simple
Collecting pyyaml
  Downloading https://mirrors.huaweicloud.com/repository/pypi/packages/49/ee/14c54df452143b9ee9f0f29074d7ca5516a36edb0b4cc40c3f280131656f/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (718 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 718.5/718.5 KB 1.0 MB/s eta 0:00:00
Installing collected packages: pyyaml
Successfully installed pyyaml-6.0.2

(gdenv310) root@davinci-mini:~/gdenv310/bin# python3 -c "import torch;import torch_npu; from datetime import datetime;print(datetime.now()); a = torch.randn(3, 4).npu(); print(a + a);print(datetime.now());"
2025-06-09 21:21:56.022869
...run stack spill compile error:  In file included from <built-in>:1:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_runtime_wrapper.h:39:
/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_vector_types.h:19:2: warning: The vector size is manually reset. [-W#warnings]
#warning The vector size is manually reset.
 ^
In file included from <built-in>:1:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_runtime_wrapper.h:68:
/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_vector_intrinsics.h:20:10: fatal error: 'type_traits' file not found
#include <type_traits>
         ^~~~~~~~~~~~~
1 warning and 1 error generated.

[W compiler_depend.ts:387] Warning: E40021: [PID: 35515] 2025-06-09-21:25:59.698.173 Failed to compile Op [Add1]. (oppath: [Compile /usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/add.py failed with errormsg/stack: File "/usr/local/Ascend/ascend-toolkit/8.0.0/python/site-packages/tbe/tvm/error_mgr/tbe_python_error_mgr.py", line 111, in raise_tbe_python_err
    raise TBEPythonError(args_dict)

tvm.error_mgr.tbe_python_error_mgr.TBEPythonError: [EB9999] [errClass:N/A][errCode:EB0500][message:compile error In file included from <built-in>:1:In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_runtime_wrapper.h:39:/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_vector_types.h:19:2: warning: The vector size is manually reset. [-W#warnings]#warning The vector size is manually reset. ^In file included from <built-in>:1:In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_runtime_wrapper.h:68:/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_vector_intrinsics.h:20:10: fatal error: \'type_traits\' file not found#include <type_traits>         ^~~~~~~~~~~~~1 warning and 1 error generated.:][errPcause:N/A][errSolution:N/A]During handling of the above exception, another exception occurred:tvm.error_mgr.tbe_python_error_mgr.TBEPythonError: [errClass:N/A][errCode:EB0500][message:compile cce error : , dirpath: /tmp/tmpstcp_6nv/, path_target: /root/gdenv310/bin/kernel_meta/kernel_meta_11089108732813996852/kernel_meta/te_add_943d4a5a626e992b93a6f6b51cd0a7f760326a87cb344ab204c37e8f1aae5b49.o][errPcause:N/A][errSolution:N/A]', 'errPcause': ' ', 'errSolution': ' '}
], optype: [Add])
        Solution: See the host log for details, and then check the Python stack where the error log is reported.
        TraceBack (most recent call last):
        Compile op[Add1] failed, oppath[/usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/add.py], optype[Add], taskID[2]. Please check op's compilation error message.[FUNC:ReportBuildErrMessage][FILE:fusion_manager.cc][LINE:367]
        [SubGraphOpt][Compile][ProcFailedCompTask] Thread[255082704400672] recompile single op[Add1] failed[FUNC:ProcessAllFailedCompileTasks][FILE:tbe_op_store_adapter.cc][LINE:1069]
        [SubGraphOpt][Compile][ParalCompOp] Thread[255082704400672] process fail task failed[FUNC:ParallelCompileOp][FILE:tbe_op_store_adapter.cc][LINE:1116]
        [SubGraphOpt][Compile][CompOpOnly] CompileOp failed.[FUNC:CompileOpOnly][FILE:op_compiler.cc][LINE:1190]
        [GraphOpt][FusedGraph][RunCompile] Failed to compile graph with compiler Normal mode Op Compiler[FUNC:SubGraphCompile][FILE:fe_graph_optimizer.cc][LINE:1410]
        Call OptimizeFusedGraph failed, ret:4294967295, engine_name:AIcoreEngine, graph_name:partition0_rank1_new_sub_graph2[FUNC:OptimizeSubGraph][FILE:graph_optimize.cc][LINE:119]
        subgraph 0 optimize failed[FUNC:OptimizeSubGraphWithMultiThreads][FILE:graph_manager.cc][LINE:815]
        build graph failed, graph id:0, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1618]
        [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
 (function ExecFunc)
Traceback (most recent call last):
  File "<string>", line 1, in <module>
RuntimeError: The Inner error is reported as above. The process exits for this inner error, and the current working operator name is Add.
Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
[ERROR] 2025-06-09-21:26:00 (PID:35515, Device:0, RankID:-1) ERR00100 PTA call acl api failed


(gdenv310) root@davinci-mini:~/gdenv310/bin# export ASCEND_LAUNCH_BLOCKING=1
(gdenv310) root@davinci-mini:~/gdenv310/bin# echo $ASCEND_LAUNCH_BLOCKING
1


(gdenv310) root@davinci-mini:~/gdenv310/bin# python3 -c "import torch;import torch_npu; from datetime import datetime;print(datetime.now()); a = torch.randn(3, 4).npu(); print(a + a);print(datetime.now());"
2025-06-09 21:33:43.531664
...run stack spill compile error:  In file included from <built-in>:1:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_runtime_wrapper.h:39:
/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_vector_types.h:19:2: warning: The vector size is manually reset. [-W#warnings]
#warning The vector size is manually reset.
 ^
In file included from <built-in>:1:
In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_runtime_wrapper.h:68:
/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_vector_intrinsics.h:20:10: fatal error: 'type_traits' file not found
#include <type_traits>
         ^~~~~~~~~~~~~
1 warning and 1 error generated.

Traceback (most recent call last):
  File "<string>", line 1, in <module>
RuntimeError: InnerRun:build/CMakeFiles/torch_npu.dir/compiler_depend.ts:218 OPS function error: Add, error code is 500002
[ERROR] 2025-06-09-21:37:13 (PID:44097, Device:0, RankID:-1) ERR01100 OPS call acl api failed
[Error]: A GE error occurs in the system.
        Rectify the fault based on the error information in the ascend log.
E40021: [PID: 44097] 2025-06-09-21:37:13.361.785 Failed to compile Op [Add1]. (oppath: [Compile /usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/add.py failed with errormsg/stack: File "/usr/local/Ascend/ascend-toolkit/8.0.0/python/site-packages/tbe/tvm/error_mgr/tbe_python_error_mgr.py", line 111, in raise_tbe_python_err
    raise TBEPythonError(args_dict)

tvm.error_mgr.tbe_python_error_mgr.TBEPythonError: [EB9999] [errClass:N/A][errCode:EB0500][message:compile error In file included from <built-in>:1:In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_runtime_wrapper.h:39:/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_vector_types.h:19:2: warning: The vector size is manually reset. [-W#warnings]#warning The vector size is manually reset. ^In file included from <built-in>:1:In file included from /usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_runtime_wrapper.h:68:/usr/local/Ascend/ascend-toolkit/8.0.0/aarch64-linux/ccec_compiler/lib/clang/15.0.5/include/__clang_cce_vector_intrinsics.h:20:10: fatal error: \'type_traits\' file not found#include <type_traits>         ^~~~~~~~~~~~~1 warning and 1 error generated.:][errPcause:N/A][errSolution:N/A]During handling of the above exception, another exception occurred:tvm.error_mgr.tbe_python_error_mgr.TBEPythonError: [errClass:N/A][errCode:EB0500][message:compile cce error : , dirpath: /tmp/tmp2r43zjji/, path_target: /root/gdenv310/bin/kernel_meta/kernel_meta_1822236422885645930/kernel_meta/te_add_943d4a5a626e992b93a6f6b51cd0a7f760326a87cb344ab204c37e8f1aae5b49.o][errPcause:N/A][errSolution:N/A]', 'errPcause': ' ', 'errSolution': ' '}
], optype: [Add])
        Solution: See the host log for details, and then check the Python stack where the error log is reported.
        TraceBack (most recent call last):
        Compile op[Add1] failed, oppath[/usr/local/Ascend/ascend-toolkit/8.0.0/opp/built-in/op_impl/ai_core/tbe/impl/dynamic/add.py], optype[Add], taskID[2]. Please check op's compilation error message.[FUNC:ReportBuildErrMessage][FILE:fusion_manager.cc][LINE:367]
        [SubGraphOpt][Compile][ProcFailedCompTask] Thread[255083593199904] recompile single op[Add1] failed[FUNC:ProcessAllFailedCompileTasks][FILE:tbe_op_store_adapter.cc][LINE:1069]
        [SubGraphOpt][Compile][ParalCompOp] Thread[255083593199904] process fail task failed[FUNC:ParallelCompileOp][FILE:tbe_op_store_adapter.cc][LINE:1116]
        [SubGraphOpt][Compile][CompOpOnly] CompileOp failed.[FUNC:CompileOpOnly][FILE:op_compiler.cc][LINE:1190]
        [GraphOpt][FusedGraph][RunCompile] Failed to compile graph with compiler Normal mode Op Compiler[FUNC:SubGraphCompile][FILE:fe_graph_optimizer.cc][LINE:1410]
        Call OptimizeFusedGraph failed, ret:4294967295, engine_name:AIcoreEngine, graph_name:partition0_rank1_new_sub_graph2[FUNC:OptimizeSubGraph][FILE:graph_optimize.cc][LINE:119]
        subgraph 0 optimize failed[FUNC:OptimizeSubGraphWithMultiThreads][FILE:graph_manager.cc][LINE:815]
        build graph failed, graph id:0, ret:4294967295[FUNC:BuildModelWithGraphId][FILE:ge_generator.cc][LINE:1618]
        [Build][SingleOpModel]call ge interface generator.BuildSingleOpModel failed. ge result = 4294967295[FUNC:ReportCallError][FILE:log_inner.cpp][LINE:161]
        [Build][Op]Fail to build op model[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]
        build op model failed, result = 500002[FUNC:ReportInnerError][FILE:log_inner.cpp][LINE:145]



# 尝试（250610）
- CANN：7.0.RC1
    root@davinci-mini:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux# cat ascend_toolkit_install.info
    package_name=Ascend-cann-toolkit
    version=7.0.RC1
    innerversion=V100R001C13SPC005B246
    compatible_version=[V100R001C29],[V100R001C30],[V100R001C13],[V100R003C10],[V100R003C11]
    arch=aarch64
    os=linux
    path=/usr/local/Ascend/ascend-toolkit/7.0.RC1/aarch64-linux
- PyTorch : 2.1.0
    - 参考：https://gitee.com/ascend/pytorch
    CANN版本	支持的PyTorch版本	支持的Extension版本	Gitee分支
    CANN 7.0.RC1	2.1.0	2.1.0.rc1	v2.1.0-5.0.rc3
- Python：3.10
    - 参考：https://gitee.com/ascend/pytorch
    PyTorch版本	Python版本
    PyTorch2.1.0	Python3.8.x, Python3.9.x, Python3.10.x, Python 3.11.x

- 创建并启动 python3.10 虚拟环境
  - root@davinci-mini:~# apt install python3.10-venv
  - root@davinci-mini:~# python3.10 -m venv gdenv310
  - root@davinci-mini:~/gdenv310/bin# source activate

- pip配置华为源
- 在python3.10虚拟环境安装tPyTorch 2.1.0
  - (gdenv310) root@davinci-mini:~# pip3 install torch==2.1.0
- 安装依赖
  - 参考：https://www.hiascend.com/document/detail/zh/canncommercial/80RC3/softwareinst/instg/instg_0006.html?Mode=PmIns&OS=Ubuntu&Software=cannToolKit
  - (gdenv310) root@davinci-mini:~# pip3 install attrs cython numpy==1.24.0 decorator sympy cffi pyyaml pathlib2 psutil protobuf==3.20 scipy requests absl-py
    - ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
te 0.4.0 requires cloudpickle, which is not installed.
te 0.4.0 requires synr==0.5.0, which is not installed.
te 0.4.0 requires tornado, which is not installed.
op-compile-tool 0.1.0 requires getopt, which is not installed.
op-compile-tool 0.1.0 requires inspect, which is not installed.
op-compile-tool 0.1.0 requires multiprocessing, which is not installed.
Successfully installed absl-py-2.3.0 attrs-25.3.0 certifi-2025.4.26 cffi-1.17.1 charset-normalizer-3.4.2 cython-3.1.2 decorator-5.2.1 idna-3.10 numpy-1.24.0 pathlib2-2.3.7.post1 protobuf-3.20.0 psutil-7.0.0 pycparser-2.22 pyyaml-6.0.2 requests-2.32.3 scipy-1.15.3 six-1.17.0 urllib3-2.4.0

- 下载torch_npu v5.0.rc3-pytorch2.1.0
  - 参考：https://www.hiascend.com/developer/download/community/result?module=pt+cann&pt=5.0.RC3&cann=7.0.RC1.3.beta1
  - (gdenv310) root@davinci-mini:~/tmp2506# wget https://gitee.com/ascend/pytorch/releases/download/v5.0.rc3-pytorch2.1.0/torch_npu-2.1.0rc1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
  - (gdenv310) root@davinci-mini:~/tmp2506# pip3 install torch_npu-2.1.0rc1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
    Looking in indexes: https://mirrors.huaweicloud.com/repository/pypi/simple
    Processing ./torch_npu-2.1.0rc1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl
    Installing collected packages: torch-npu
    Successfully installed torch-npu-2.1.0rc1

- 验证。报错，不支持Ascend310B4
(gdenv310) root@davinci-mini:~/tmp2506# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);"
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/root/gdenv310/lib/python3.10/site-packages/torch/utils/backend_registration.py", line 153, in wrap_tensor_to
    device_idx = _normalization_device(custom_backend_name, device)
  File "/root/gdenv310/lib/python3.10/site-packages/torch/utils/backend_registration.py", line 109, in _normalization_device
    return _get_current_device_index()
  File "/root/gdenv310/lib/python3.10/site-packages/torch/utils/backend_registration.py", line 103, in _get_current_device_index
    return getattr(getattr(torch, custom_backend_name), _get_device_index)()
  File "/root/gdenv310/lib/python3.10/site-packages/torch_npu/npu/utils.py", line 50, in current_device
    torch_npu.npu._lazy_init()
  File "/root/gdenv310/lib/python3.10/site-packages/torch_npu/npu/__init__.py", line 197, in _lazy_init
    torch_npu._C._npu_init()
RuntimeError: Unsupported soc version: Ascend310B4


# 工单要求提供信息（250610）

## 环境说明

- CANN：7.0.RC1
```
root@davinci-mini:/usr/local/Ascend/ascend-toolkit/latest/aarch64-linux# cat ascend_toolkit_installinfo
package_name=Ascend-cann-toolkit
version=7.0.RC1
innerversion=V100R001C13SPC005B246
compatible_version=[V100R001C29],[V100R001C30],[V100R001C13],[V100R003C10],[V100R003C11]
arch=aarch64
os=linux
path=/usr/local/Ascend/ascend-toolkit/7.0.RC1/aarch64-linux
```
- PyTorch：2.1.0
- Python：3.10
- torch-npu: 2.1.0.rc1



  参考 https://gitee.com/ascend/pytorch， 由 CANN 版本选取了配套的 PyTorch 2.1.0，再由 PyTorch 2.1.0 选取了配套的 Python 3.10。部分参考信息摘录如下：

  |CANN版本|	支持的PyTorch版本|	支持的Extension版本|Gitee分支|
  |---|---|---|---|
  |CANN 7.0.RC1|	2.1.0|	2.1.0.rc1|	v2.1.0-5.0.rc3|

  |PyTorch版本|	Python版本
  |---|---|
  |PyTorch2.1.0|	Python3.8.x, Python3.9.x, Python3.10.x, Python 3.11.x|

## 安装和操作

1. 更新
```
root@davinci-mini:~# apt-get update
```
2. 安装 python3.10-venv（用于创建 python 虚拟环境）
```
root@davinci-mini:~# apt install python3.10-venv
```

3. 创建 Python3.10 虚拟环境并激活
```
root@davinci-mini:~# python3 -m venv gdenv310
root@davinci-mini:~# cd gdenv310
root@davinci-mini:~/gdenv310# cd bin
root@davinci-mini:~/gdenv310/bin# source activate
(gdenv310) root@davinci-mini:~/gdenv310/bin# 
```

4. 配置 PIP的华为源

5. 安装依赖
（参考：https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/82RC1alpha002/softwareinst/instg/instg_0007.html?Mode=PmIns&OS=Ubuntu&Software=cannToolKit）
```
(gdenv310) root@davinci-mini:~# pip3 install attrs cython numpy==1.24.0 decorator sympy cffi pyyaml pathlib2 psutil protobuf==3.20 scipy requests absl-py
```

6. 安装 PyTorch 2.1.0
```
(gdenv310) root@davinci-mini:~# pip3 install torch==2.1.0
```

7. 安装 torch-npu 2.1.0.rc1（实际要升级到 2.1.0.post3）
```
(gdenv310) root@davinci-mini:~# pip3 install torch-npu==2.1.0.rc1
Looking in indexes: https://mirrors.huaweicloud.com/repository/pypi/simple
Collecting torch-npu==2.1.0.rc1
  Downloading https://mirrors.huaweicloud.com/repository/pypi/packages/8a/fc/394f24feb50e07e8db84ab029c56bd8cf953606b9a6e3f636a298c93fb06/torch_npu-2.1.0rc1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (7.2 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.2/7.2 MB 4.6 MB/s eta 0:00:00
Installing collected packages: torch-npu
Successfully installed torch-npu-2.1.0rc1
```

8. 设置环境变量
```
(gdenv310) root@davinci-mini:~# source /usr/local/Ascend/ascend-toolkit/set_env.sh
```

9. 测试验证

运行以下指令，报错：不支持 Ascend310B4
```
(gdenv310) root@davinci-mini:~# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);"
...
RuntimeError: Unsupported soc version: Ascend310B4
```
升级 torch-npu 到 2.1.0.post3，不再报“不支持Ascend310B4”的错误。

---

10. 收集 err.log
```
(gdenv310) root@davinci-mini:~# python3 -c "import torch;import torch_npu; a = torch.randn(3, 4).npu(); print(a + a);" > err.log
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/context/op_context.py:38: DeprecationWarning: currentThread() is deprecated, use current_thread() instead
  return _contexts.setdefault(threading.currentThread().ident, [])
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:671: ImportWarning: TEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
/usr/lib/python3.10/tempfile.py:1008: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/tmp/tmpbpz2_zrf'>
  _warnings.warn(warn_message, ResourceWarning)
  ```

  ---

  11. 收集 err.log.with_jit_compile_false
  ```
  (gdenv310) root@davinci-mini:~# python3 -c "import torch;import torch_npu; torch.npu.set_compile_mode(jit_compile=False); a = torch.randn(3, 4).npu(); print(a + a);" > err.log.with_jit_compile_false
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
/usr/local/Ascend/ascend-toolkit/latest/python/site-packages/tbe/common/context/op_context.py:38: DeprecationWarning: currentThread() is deprecated, use current_thread() instead
  return _contexts.setdefault(threading.currentThread().ident, [])
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:671: ImportWarning: TEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:914: ImportWarning: TEMetaPathFinder.find_spec() not found; falling back to find_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
<frozen importlib._bootstrap>:671: ImportWarning: TBEMetaPathLoader.exec_module() not found; falling back to load_module()
[E OpParamMaker.cpp:273] call aclnnAdd failed, detail:EZ9999: Inner Error!
EZ9999  Cannot parse json for config file [add.json].
        TraceBack (most recent call last):
        Failed to parse kernel in add.json.
        AclOpKernelInit failed opType
        launch failed for Add, errno:561108.

[ERROR] 2025-06-10-22:03:37 (PID:79003, Device:0, RankID:-1) ERR01005 OPS internal error
Exception raised from operator() at third_party/op-plugin/op_plugin/ops/base_ops/opapi/AddKernelNpuOpApi.cpp:43 (most recent call first):
frame #0: c10::Error::Error(c10::SourceLocation, std::string) + 0x68 (0xe7ffe796d898 in /root/gdenv310/lib/python3.10/site-packages/torch/lib/libc10.so)
frame #1: c10::detail::torchCheckFail(char const*, char const*, unsigned int, std::string const&) + 0x6c (0xe7ffe79262a8 in /root/gdenv310/lib/python3.10/site-packages/torch/lib/libc10.so)
frame #2: <unknown function> + 0x82968c (0xe7ffd3f0968c in /root/gdenv310/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #3: <unknown function> + 0xe27840 (0xe7ffd4507840 in /root/gdenv310/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #4: <unknown function> + 0x56aa70 (0xe7ffd3c4aa70 in /root/gdenv310/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #5: <unknown function> + 0x56ae98 (0xe7ffd3c4ae98 in /root/gdenv310/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #6: <unknown function> + 0x568d70 (0xe7ffd3c48d70 in /root/gdenv310/lib/python3.10/site-packages/torch_npu/lib/libtorch_npu.so)
frame #7: <unknown function> + 0x946ec (0xe7ffe79946ec in /root/gdenv310/lib/python3.10/site-packages/torch/lib/libc10.so)
frame #8: <unknown function> + 0x7d5c8 (0xe7fff0f2d5c8 in /lib/aarch64-linux-gnu/libc.so.6)
frame #9: <unknown function> + 0xe5d1c (0xe7fff0f95d1c in /lib/aarch64-linux-gnu/libc.so.6)

Traceback (most recent call last):
  File "<string>", line 1, in <module>
RuntimeError: The Inner error is reported as above.
 Since the operator is called asynchronously, the stacktrace may be inaccurate. If you want to get the accurate stacktrace, pleace set the environment variable ASCEND_LAUNCH_BLOCKING=1.
[ERROR] 2025-06-10-22:03:37 (PID:79003, Device:0, RankID:-1) ERR00100 PTA call acl api failed
/usr/lib/python3.10/tempfile.py:1008: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/tmp/tmp7jo255on'>
  _warnings.warn(warn_message, ResourceWarning)

  ```