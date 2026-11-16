# 原 Bell 四次方全偶扩张：首次实际内存边界

作者：Astra-ISP-789f / normal_annihilator。AI-assisted: GPT-6 Astra Pro。2026-11-16 UTC。

本记录只登记已完成作业的执行范围、诊断及输出身份，不把计算资源失败解释为数学否定。原 source、参数和输入 pins 均保持不变。

## 1. 已完成的实际作业

- Actions run **43862258541**，job **133281798325**；
- 主 source commit：`2774f7322145fa028c1fdbead75656e308a462f5`；
- source：`2026-11-16-r150-original-bell-fourth-even-extension-789f.py`；
- 原 source SHA256：`a07425b29d36c685a7165436ae3acb51d633d159ccc7864294c21e9c92a580d2`；
- 预算600秒、4096 MiB；外层660秒；
- 外层实际 exit1，墙时521.1204194759999秒；主入口记录 elapsed520.872364279秒；
- 真实 Singular 版本为4.4.1（44105，64 bit）；
- job 于2026-11-16 12:06:45 UTC结束，结论为 failure。

首个原系数审计实际 exit0，墙时6.878610858000002秒。其完整4311字节回执 SHA256 为
~~~
ee662a70e96154d806015798291639dad8c5b86dd07bb1900d78267e433b5fb5
~~~
该次 audit 的 execution source commit 为
~~~
08684dc750ee0a17c50fa3494279a38cf30a3bc9
~~~

## 2. 实际通过的数学与程序门

原三个有理四次目标各有364877个非零有理单项式；1094631个新有理系数全部通过7整性检查，三个完整独立模7乘积全部通过。所有17个原变量与17个原梯度保留；未构造完整权十二 Macaulay 矩阵。

随后真实运行的双级 Singular 自测耗时0.20060912799999642秒、exit0，已核：

- degree2前缀没有非法纯参数三次列；
- 原 SSI 前缀继续到degree3并得到预期纯三次；
- 三个目标的原来源、完整单位矩阵、SSI往返；
- 三个独立 FLINT 原乘积；
- 全偶投影自测中的奇项相消及原环来源。

该自测日志322字节，SHA256为
~~~
f69b99ed8d00db9b4154b578ec2b30651026ef4c96c1880b451cb3fb5dbcbe33
~~~

## 3. 实际失败的位置

第二个 Singular 子进程只有起始标记
~~~
@@SLIMGB17-START 12
~~~
在460.26112888秒后以 **exit14** 返回，真实诊断包含
~~~
Singular error: no more memory
halt 14
~~~
子进程最大常驻4172848 KiB，父进程最大常驻1337444 KiB。该次失败发生于原17式、全偶扩张的 degree12 `slimgb` 本体，尚未返回完整发现阶段终标。

该日志196字节，SHA256为
~~~
34e20512f9b75af2ab365497e4a7a6d3550119b75dd238c4e741caf5e7d2658d
~~~
实际 Singular 输入25387668字节，SHA256为
~~~
6f6868bb502b28674a6f7378e1a93231d3cd1d19184838371185e6d47f1aba07
~~~

没有已完成的原17式 GB/SSI 候选，没有51条原来源，三个原场来源核验列表为空；后继特征零消费者未运行。完整 manifest 的 generation 为2，只有原模型、三个目标与已通过的自测阶段。

因此本次不允许按 exit75 续算，不允许把进程内部未保存的候选视为检查点，也没有得到 $b^4$ 的成员性或非成员性结论。若以后重新使用已付前缀，仍须从真正可获得的输入重建并逐完整SHA核验；这个已结束job的临时数组不假定存活。

## 4. 完整原回执与可复核身份

完整原主回执8009字节，其 SHA256为
~~~
7b3c1f0bbf14cad11062bb641277a3884677ea4cb1961a25b2a8ebf65821c859
~~~
binding保持为
~~~
99564113529d2a6ee2e6ef494ecfe162ba5c0fcc4810035173580fed4f78b899
~~~

已从完成job的完整日志恢复原主回执：只补回日志摘要略去的已锁source descriptor，移除摘要新增的空events字段，依原source的实际canonical序列化重建；全部8009字节及SHA精确匹配。首个4311字节audit回执也同样精确匹配。没有改写失败状态、用时、子进程诊断或任何数学对象。

仓库只保以下执行身份及本说明，完整数学数组和原回执仍不进入仓库：

- [首个原系数审计执行身份](r150-original-bell-fourth-even-execution-789f/43862258541-original-bell-fourth-complete-prime7-audit90.json)；
- [原四次入口执行身份](r150-original-bell-fourth-even-execution-789f/43862258541-original-bell-fourth-even-three-source600.json)；
- [原接口](2026-11-16-r150-original-bell-fourth-even-extension-interface-789f.md)。

后继将优先利用已证明的原九生成元完整表示构造12个参数上的小模候选，保留全部原来源与所有参数例外；不以单纯增加时间或内存把本次失败冒作已完成前缀。
