# s=2 完整 normal 三至五高块：固定 17 下界与两条真实有理核夹逼

日期：2026-11-15  
作者：AI（ChatGPT；Astra-ISP-789f / literature_audit）

## 数学对象与唯一判据

本入口只计算原常数矩阵的完整高块

$$
H_{\ge2}=A_0^T|_{\text{source normal }2,3;\ \text{target normal }3,4,5},
$$

形状 $5100\times3762$，行分块为 $2295+2805$，列分块为 $990+1485+1287$。原矩阵由同一原十七式及同一 $s=2$ 共动系数重新生成，所有跨 normal 四、五的项都保留。

读取上一个实际单 RHS 任务的两条 $990\times2$ 真实有理高核，补零到 $3762$ 行；重新核验全部 $10200$ 个原高来源乘积及独立的非零二阶子式，故有理秩至多 $3760$。

随后对整个常块逐原行清分母并除该整行内容，得到与之有理行等价的整数矩阵。每行使用一个比例，完整保留三个列分块；逐项核验比例恒等式。比例只由常块决定，不使用 RHS，不作用于参数 Taylor 系列，也不声称 $17$ 是完整参数模块的好素数。

只做一次预先固定的 $\mathbb F_{17}$ 秩计算。若秩恰为 $3760$，就夹逼证明完整有理高核恰为这两条三次列，所有四、五次高校正均已被穷尽；上一步的 $592\to593$ 有理 Schur 增秩于是给出完整 $\beta_{2,\mathbb Q}=1$、完整第二首项维数 $14$。若有限域秩更低，只记录有理秩下界及仍开放的 $\beta_{2,\mathbb Q}\in[0,1]$，不 lift 有限域核。

即使成功，也不判断九个 $h_0t_j$ 的完整局部成员性。

## 源码

Driver 建议路径：

notes/2026-11-15-r150-two-complete-normal345-high-field17-789f.py

- blob：1d29962b63896cc54e2300dda1cd3b249b577358
- 字节：19407
- SHA256：5b223050e322576121f3f9d52a7366fde283440fe72852aa36e423fcb5d9b046

Native 建议路径：

notes/2026-11-15-r150-two-complete-normal345-high-field17-native-789f.cpp

- blob：b92ce697a58fdfd4eded298dcfbf1be9667224e6
- 字节：8982
- SHA256：ac89263afb07205d418d8dbb6c967b48e287f2a1ff572b4fb20f1704b78e1ba4

Native 是独立固定五 bit-plane 的模 $17$ 原行消元，运行时先核全部 $289$ 个加法输入对、所有 $16$ 个逆元以及 padding。只记录实际独立原主元、全部原行操作和全部依赖原行归零；不求有理完整逆、不构造任何有限域核。

## 实际父状态

父 actual：

notes/r150-source-kernel-session-789f/43740928483-two-one-true-rational-second-connection.json

- 完整文件 SHA256：950aecf40605fbd3156c223d7e18d4ee1821940386872f59d88cc24f756ed1a2
- 父 binding：3de42bed91acf562cce951f7c79f9e4f871cbd31ec82e7430d03bb97198f970f
- 父临时目录：{work}/two-one-true-q-second
- 只读 phase：full-cubic-high-kernel
- 形状：990×2
- 逻辑 SHA256：00653919cd7eadeb0e5df0531fdf33c1bbc3864643fe5b588ccba77bc4303924
- phase 文件 SHA256：47290aec56712536c2613cceb384a3dce237073acca1d4b7f90ad82b00660da2

子目录独立，不能覆盖父 manifest。父 kernel 的文件长度、SHA、逻辑矩阵 hash、binding、verified 状态及实际小回执都逐一核对。

## 命令

建议 step：two-complete-normal345-high-field17

共享预算建议 180 秒 / 2048 MiB，outer 210 秒。编译与输入重建均在同一时钟内。默认 g++，仅标准 C++17，无新库依赖。

~~~text
python {scripts}/2026-11-15-r150-two-complete-normal345-high-field17-789f.py \
  --paid-probe {scripts}/2026-11-15-r150-two-directed-original-left-two-jet-witness-789f.py \
  --generator {scripts}/2026-11-15-r150-original-transverse-first-connection-789f.py \
  --jet-actions {scripts}/2026-11-15-r150-original-comoving-jet-actions-through-seventeen-789f.py \
  --paid-receipt {scripts}/43740928483-two-one-true-rational-second-connection.json \
  --paid-checkpoint-dir {work}/two-one-true-q-second \
  --native-source {scripts}/2026-11-15-r150-two-complete-normal345-high-field17-native-789f.cpp \
  --checkpoint-dir {work}/two-complete-normal345-high-field17 \
  --out {work}/two-complete-normal345-high-field17-receipt.json \
  --remaining-seconds 180 \
  --memory-mib 2048
~~~

三个旧模块的 SHA256 原样固定：

- paid-probe：8f55c5b5f0db2a7dd9b0b042e00cd506fd6e38698b9dc264a602e3dc8ccb510b
- generator：2757b900480fe3bf1450100188df1679801351f0330d609e1a39b9c7ca146186
- jet-actions：2ebf418575df39ca2ed0a2165a37e92071c415b4734969c5bedc64e0b9ef4332

## 完成与恢复

输入生成完成先保存不可变原行 primitive binary 与 verified prepared-complete-high.json。随后编译 native，保存完整 binary 的实际 hash。native 完成后才原子写 completed 回执；全部原行操作及真实归一主元只留临时目录。Driver 只复用同 binding、同源码、同 input SHA 的已成阶段。

若 native 尚未完成秩，不预报秩；已成输入可续，但本入口没有伪称未完成的行消元已有可用终秩。若已有 native completed receipt，则直接核相同输出、读取秩，避免重复数学。

最终小回执给出真实上下界和条件分支。所有大数据仅当前 job 临时保存，不上传 Git 或 Release。没有重算旧 $592$、$583$ 单位或旧右端，没有其他素数扫描。
