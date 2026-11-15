# 原无穷远第六连接之前的完整常高核

日期：2026-11-15 UTC。作者：Astra-ISP-789f / normal_annihilator。AI-assisted：GPT-6 Astra Pro。

## 当前范围

本入口只新计算原常高块

$$
H=A_0^{\mathsf T}
\big|_{\text{source normal }2,3;\ \text{target normal }3,4,5}
\in\mathbb Q^{5100\times3762}.
$$

全部 $2295+2805$ 原来源行和全部 $990+1485+1287$ 靶坐标保留。
尤其保留 normal 四、五间与三、四间的全部交叉，不能用单块注入代替本矩阵的核。

此前原小投影已经实际完整，特征零谱长 $61$。本入口直接读取其已验证原系数缓存；
不重做小投影、任何旧 $4340$ 消元或十八条第五链。
固定模 $31$ 仅用于这个完整常数有理块的秩下界，不扫描新素数、不把有限域核提升为有理核。

## 两条真上界列来自何处

当前第五缓存 phase high-fifth-lifts 的真实形状是 $999\times11$。
读取其前两列，实际核最后九个 head 坐标为零，
再取前 $990$ 个原三次横向坐标，得 $Z_3\in\mathbb Q^{990\times2}$。
两个原自由坐标 $164,494$ 上的块实际为 $I_2$。

将这两列补零到 normal 四、五，程序在未经缩放的完整原高矩阵上核

$$
H\binom{Z_3}{0}=0.
$$

这对应 $5100\cdot2=10200$ 个真有理产品。
所以 $\operatorname{rank}_{\mathbb Q}H\le3760$。

逐原行清分母、除整行内容，只产生一个非零有理行比例。
程序核该比例在整行所有三个列分块上的完整恒等式，
并把所得到的同一个整数块约化模 $31$。若实际秩为 $3760$，
则上下界夹等，完整有理高核恰为上述两条三次列。
所有合法高核的 normal 四、五坐标因而严格为零。

若实际有限域秩较低，只记录下界；不预填 $3760$，也不以维数不足否定有理秩。
行清分母仅用于常数矩阵，不作用于任何高阶 forcing。
其是否在 $31$ 处也是单位按实际数据另记。

## 为什么这是第六完整性需要的对象

原 full 与小投影的常头均为 $27$，前五连接秩相同：
$(4,0,1,3,1)$。
同头原链相减后除以 $u$ 的递归，证明任意 full 五阶链的每个系数都在 pure/one-normal 靶支撑内。

所以第六 forcing 的全部 $5100$ 高来源行严格为零。
常数项 $F_0$ 的纯部分又为零，因此 $\lambda_6$ 的 normal 零、一、二部分不出现在这些高行。
它的 normal 三、四、五部分必须完整落在 $\ker H$。

若本次夹等成功，后继只需将两条 $Z_3$ 的低行返回加入真实低系统。
这会支付高支撑完备性，但不直接支付第六连接秩；第六两个真实投影退出方向仍须做低行乘回。
本入口不会声称第六连接已经计算。

## 冻结源码

Driver：

- notes/2026-11-15-r150-infinity-complete-normal345-high-field31-789f.py
- blob adf8b6b50367fcafc89888e54181d3f385d232bf
- 21406 字节
- SHA256 1a578441929247d114b7f39e9824b243dbc0433de781dd2ffce4d4e11dea4122

Native：

- notes/2026-11-15-r150-infinity-complete-normal345-high-field31-native-789f.cpp
- blob 501dbe55901564c2e2acfe5cb5a7b50fc70dc22f
- 9078 字节
- SHA256 cee59e862dc22bd5ade469177ce9e4541d2a6b4743ab811684a5e387a4402ba4

Native 从已实际运行的二点完整高块 worker 独立分叉。
只把固定素数换成 $31$、重算逆表、改协议 magic 与精确审计字段。
五 bit-plane 的完整行消元保持；运行时实际核全部 $961$ 对加法输入、全部三十个逆元和 padding。
全部原依赖行都归零，实际独立原主元与全部原行操作只在临时目录保存。

源码已冻结，未在本地编译、AST 或执行新数学；最终结论以本次 Actions 实际回执为准。

## 调用

~~~text
python {scripts}/2026-11-15-r150-infinity-complete-normal345-high-field31-789f.py
  --projection-consumer {scripts}/2026-11-15-r150-infinity-small-original-projection-smith-789f.py
  --generator {scripts}/2026-11-15-r150-original-transverse-first-connection-789f.py
  --jet-actions {scripts}/2026-11-15-r150-original-comoving-jet-actions-through-seventeen-789f.py
  --projection-receipt {scripts}/43740928483-infinity-small-original-projection-smith.json
  --projection-out {work}/infinity-small-original-projection-smith
  --fifth-receipt {scripts}/43740928483-infinity-fifth-true-shifted-incoming.json
  --fifth-checkpoint-dir {work}/infinity-fifth-true-incoming-checkpoint
  --native-source {scripts}/2026-11-15-r150-infinity-complete-normal345-high-field31-native-789f.cpp
  --checkpoint-dir {work}/infinity-complete-normal345-high-field31
  --out {work}/infinity-complete-normal345-high-field31-receipt.json
  --remaining-seconds 60
  --memory-mib 2048
~~~

编译使用 g++、标准 C++17 和 -O3，无新库。
输入、编译、实际 field 计算共用六十秒时钟；建议外层一百秒。
下一次同源码、同 out 调用会核原输入和已完成 native 输出，复用真实完成阶段。
未完成的 native 行消元没有被冒称可直接续的数学终值。

主要门槛是 parameters.conclusion.completeHighQKernelEqualsPaidTwoCubicColumns。
只有实际 finite rank 为 $3760$ 才为 true。
其他全部原行、跨块和 $10200$ 有理乘回门槛都必须同时满足。
所有数据只在当前任务临时保存，永久只保存小源码、参数、run 和 SHA。
