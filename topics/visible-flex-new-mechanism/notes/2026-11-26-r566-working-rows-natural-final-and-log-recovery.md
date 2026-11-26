# B030 working rows：原终态与完整日志恢复收据

日期：2026-11-26。**数值证据/失败输入闭账**。原科学 run45828479581 /
job139938706452，触发 commit
`9704840a2a00dd8345435f8024fea07187dd9923`。
原 job于14:02:24 UTC自然终态 success；科学程序主动clock后返回0。
**这一轮接受0步，真实保留81q与原输入相同；没有取得新的完整fine合格状态。**

## 1. 为什么使用只读恢复 run

专用 logs connector 对原 job多次返回 Transport closed，未返回科学正文。
随后公开只读恢复 run45844119049 / job139993191345，commit
`c70c116243652706ac07bce7901c292de399a026`
先核对原 run/job/commit均为终态，再一次流式读取原完整stdout。
它只使用标准库解析、hash和元数据；**科学评价0**，没有重跑模型、ODE、
求积、Jacobian、优化或旧验证。

恢复器由
[源码](../scripts/r566_terminal_log_recovery_20261126.py)、
[请求](../computations/request-r566-terminal-log-recovery-20261126.json)
和对应workflow绑定。它逐行解析全部670个带标签JSON，
325个完整checkpoint、4个outer完成记录和1个FINAL都读取了；
81q binary64身份和累积计数单调检查无错误。
全记录计数还包括326个完整Jacobian、5个backend start、
1个新限制映射观察和1个明确clock stop。

本会话在恢复run自然success后一次读取完整恢复stdout，
其3个JSON记录再次全部解析，无错误。
原38.7MB stdout没有写入Git、blob、artifact或Release；
恢复器也没有将它整篇重印。只恢复必要最后完整实际状态。

| 对象 | 字节数 | SHA256 |
|---|---:|---|
| 原job完整HTTP stdout | 38712407 | `f1b4897168262c1a6afaa23c721eb10d4e7bf5c9d643dbd28cda7c5e331b6a02` |
| 原科学FINAL原JSON | 132427 | `913c9cfc28e19e0b237d4cbbefb080d7a70b30b545e30754706f4e1ddadd1761` |
| 恢复run完整stdout | 235865 | `f3fd0bd306937d524f111958fa09403b1c1552d1065bbfa941f146edb8cef1d2` |
| 全解析收据JSON | 88567 | `2a667fb707bde2a49250e05e9cec72feb09f155c75a6c44f3bffc8219c1b8bc7` |

原HTTP Content-Length也是38712407，与完整流式读取字节数相同。
恢复run的解析/下载时间单列为元数据工作，没有加入原科学时间。

## 2. 实际状态、待应用状态和未接受试探

原科学FINAL时间为14:02:19.9509158 UTC，状态
`cooperative_clock_or_unresolved_localizer_checkpoint`。
具体stop消息为科学clock到下一原子操作，**不是未解决的角定位返回**：
本run没有启动任何完整角定位。

实际保留状态如下：

- 81q binary64 SHA256：
  `7e708ba7a973e8505a81e94073707e8c39504d1f3285253f97e3564382992080`；
  和原完整START相同，全部记录仅出现这一个接受状态的q身份。
- 真实必要库仍为571个径向节点、1276个实际峰轨道、1536整圈FFT。
- 实际working rows为150；它们只定义局部优化矩阵，不删除任何必要物理行。
- 未应用物理峰0、未应用working rows0。
- 实际trust和已记录拟议trust都为0.3003387451171875。
  当前outer4的后端trust决定尚未完成，不能擅自再折半或膨胀。
- 沿用的已付完整fine/实际角峰资格仍为原START：
  accepted eta `0.25895160785933824`、几何违约0、
  1144×3072加1116个实际角峰。它没有在本run重新计算，
  也没有被冒充成新的资格观察。

原保留资格的曲率峰16.451983793155406，球半径峰1.0114938725138363，
条带峰0.39260310843325497，det最小0.8645634647471048，
meanE最小0.9975955022279087。这些仍是该有限网/有限实际峰库上的来源读数，
不是连续reach证书。

最后试探明确未接受：工作行违约
`0.000012247873499654505`，
backend epigraph0.22506668652071263，q身份
`0a83a5cf9cf2d10fcd15494a7e290552c39aba8205e90306f3685fc12c7d0659`。
它未完成完整coarse、fine或定位，不能用作后继实际状态。

最后一个自然返回的SLSQP记录也不是接受点：status9、
Iteration limit reached、nit80/nfev81/njev81，
其epigraph为0.14643148073031023。这个更小数字未通过完整必要约束，
不能当作 eta进展。

## 3. 这一新后端实际做了什么

科学实际耗时 **2370.471193446 s**。
启动5个outer，完成4个；2次自然后端返回。
真正接受metric步0、恢复步0。

| 实际工作 | 数量/时间 |
|---|---:|
| 完整working Jacobian | 326 |
| 参数方向块 | 5428 |
| 完整working Jacobian计时 | 2308.635677389999 s |
| working value keys | 329 |
| working不可行callback拒绝 | 322 |
| 完整coarse扫描 | 7 |
| 完整coarse必要行拒绝 | 2 |
| working库交换 | 2 |
| 完整fine扫描/角定位/物理库交换 | 0 / 0 / 0 |
| 新限制映射观察 | 1 |

326个Jacobian记录中的最大工作行数150、最大子径向网29；
没有重新构建原两百万行dense Jacobian。
完整物理必要行计数仍为2030126。

新限制映射观察读到full/subradial值最大差
`3.3306690738754696e-16`，
方向绝对差 `2.1864758892320424e-9`，
相对L2差 `1.5180163934360555e-9`；
全部参数块的最大值重建差0。
这是本次新增限制映射的有限数值观察，不是证明，
也不是旧oracle parity重跑。

全live/retired oracle只折叠一次后的实际累计为：

| 计数/成本 | 值 |
|---|---:|
| FFT状态 / uniform geometry | 6351 / 6351 |
| oracle构造 | 24 |
| oracle构造秒 | 10.639079716999987 |
| prepare秒 | 2009.3813645429905 |
| 点评价调用 | 10910 |
| 点参数方向 | 10082992 |
| 点值 | 909008 |
| 点评价秒 | 338.67042398000365 |
| 非均匀Fourier点 | 328902 |
| uniform gather点 | 580106 |
| Fourier primitive fields | 57159 |
| 实际core弧长准备点 | 31711 |

这些层级与Jacobian计时有包含关系，不能相加当独立总秒数。
FINAL的active working未折叠计数为null，保留了当前全部oracle累计。
未闭合原子操作的已耗时间包含在总elapsed中，不伪装成一个已完成Jacobian。

原来源链已知科学下界2875.870845068 s仍保留；
加本run后已知下界为5246.342038514 s。
更早三段外部shutdown的未冲刷工作仍未知，墙钟
46.3705572、27.382752和68.2931574 s单列；
本轮自然clock不会把那些未知来源成本补成0，也不据此断言旧shutdown原因。

## 4. 规则、源码和运行身份

原科学源码
[working_rows](../scripts/r566_working_rows_full_acceptance_20261126.py)
为47510 B / SHA256
`90499f5c107b9ef68c9ad69eeabd28ae59755afec1346f19ef79d696629b2ad0`。
正式请求为191771 B / SHA256
`6756f5945133fd9f3f747906f43ec3befaacdde3e3404c036bb4bf1ae33cd4b4`。
完整原START来源输入163589 B / SHA256
`320b8cb2428a146251885717d21d11eb5e694dd242d2eb3203dd85eb4c0bf536`。

原runner实际pull公开仓库完成于13:22:38 UTC：
`9704840a2a00dd8345435f8024fea07187dd9923`
到 `9508ad3286243b49004fd4bee81f6add40f3acd9`。
根和本题README均空diff，blob与请求一致。
私仓实际pull于13:22:42 UTC完成，读到
`1dee3d5d06d7f1f117ce2e0eded0e5ec9f8109a4`，
根规则blob一致，QUEUE唯一且为本会话进行中。
Python3.12.14、NumPy2.3.5、SciPy1.17.0，
科学执行前凭据已移除。runner结束14:02:19.995676 UTC，returncode0。

## 5. 结论范围与实际后继

工作行子oracle减少了局部Jacobian大小，但本轮仍几乎全部耗在未达到工作行可行性的内部试探上：
322次工作行拒绝之后，只有2次试探进入完整coarse并触发学习，
没有一次进入完整fine/角定位。这里没有新的物理库容量瓶颈，
也不能把较小epigraph当成可行进展。

后继从本节的**真实保留81q、真实trust和完整必要库**出发，
对实际试探方向先作工作行可行性回溯/必要恢复；
工作行合格后仍须通过全部原coarse、fine、真实角定位和原资格规则。
回溯失败保留真实q，最后SLSQP点和最后试探不升级为输入。
原限制映射观察不再重跑；新增求解计费。
这只是明确下一输入，整张固定度量闭面的构造及课题完成标准仍未达到。
