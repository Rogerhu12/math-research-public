# R769 原完整次数格在 693 界内的精确排除

日期：2026-11-14。状态：**精确穷尽完成**。公开 [Actions run 43628341694](https://github.com/Rogerhu12/math-research-public/actions/runs/43628341694) 在原 R759 的完整整数周期格中得到
$$
\boxed{\text{不存在 }0\ne f\text{ 满足 }\deg f\le693.}
\tag{769.1}
$$
这里固定原 R735 正目标、原正有理 Hom 空间、原 $c_0$ 基点和 R759 完整格；不对其他目标或其他有理因子声称同一界。核心时间为 0.013586944999996575 秒。本次没有重复原周期、HNF、LLL 或交配计算。

## 1. 这是一份完整有界排除

完整算法证明见[预运行方法](../notes/R769-retained-degree-lattice-bounded-search-method.md)。读取 R759 已存十二维 LLL 次数 Gram 矩阵 $G$，其原几何含义为
$$
d(v)=\tfrac12v^tGv,\qquad v\in\mathbf Z^{12}.
\tag{769.2}
$$
R759 的完整饱和证明保证这覆盖该原空间的全部整数周期映射，不仅覆盖十二个基向量。

对原矩阵进行准确有理 LDL：
$$
G=\mu\operatorname{diag}(r_i)\mu^t,\quad r_i>0,\qquad
v^tGv=\sum_i r_i\left(v_i+\sum_{j>i}\mu_{ji}v_j\right)^2.
\tag{769.3}
$$
此次保存了完整矩阵、全部有理 $\mu,r_i$，并逐项重建验证 (769.3)。

倒序固定坐标时，每层保留的整数恰是
$(v_i-c_i)^2\le R_i$ 的全部解。若 $c_i=a/b$、$R_i=r/s$，
令 $K=\lfloor\sqrt{\lfloor b^2r/s\rfloor}\rfloor$，准确闭区间是
$$
\left\lceil\frac{a-K}{b}\right\rceil
\le v_i\le
\left\lfloor\frac{a+K}{b}\right\rfloor.
\tag{769.4}
$$
整个过程只用整数、Fraction 和 isqrt，没有浮点舍入或经验 LLL 质量估计。每一条范数不超过 1386 的向量必落在逐层的这些区间内；正定性保证全部区间递归有限。没有按正负号或 $\zeta$ 对称性删除轨道。

实际运行最后 DFS 栈为空，全部进入的 frame 均已完成，每个闭区间的已试整数数目等于其完整长度。唯一到达叶子的向量是零，且通过原整数 Gram 再核范数。因此 (769.1) 是穷尽结论，不是超时搜索失败。

## 2. 真实搜索计数与完成状态

最终证书的状态是 exhausted，found=false，complete=true。按坐标层 $0,\ldots,11$，准确记录为：

| 计数 | 实际向量 |
|---|---|
| frames entered | (1,1,3,9,15,27,23,23,13,9,3,1) |
| frames finished | (1,1,3,9,15,27,23,23,13,9,3,1) |
| integer candidates | (1,1,1,3,9,15,27,23,23,13,9,3) |
| empty intervals | (0,0,2,6,6,12,2,4,0,2,0,0) |

完整审计有 385 个事件、两份 gzip block，终态 active_stack_frames=0，leaves=zero_leaves=1，witness=null。最终链摘要为
c55b8c94a23612bc75da68cfd9fafd8d4a9053fde58900e8d26e4f22e69f80ec。
它绑定原配置、准确区间、整数候选、完整结束和唯一零叶子。公开源码与这些完整阶段共同给出可检查的有限证书。

## 3. 来源与全部产物绑定

| 项目 | 实际值 |
|---|---|
| run / attempt | 43628341694 / 1 |
| source commit | 4faaf06db52eb9110cf15766616aa501ff177889 |
| 核心源 SHA-256 | 395ab85cd065cf5eab9fb1684464bd849f5fc3bd03b2275d3b90ba71998eaca9 |
| 方法 SHA-256 | 844b806b9510023e6262b05bd353b67ce3c8218b490b923ec6697bd1c295163e |
| request SHA-256 | 6fcdf1223bff73551e2ec17d0474d338137ae10f4907e185f50f79dd833c5209 |
| 最终证书 SHA-256 | 97e1949ef4dfc890c5ac975533cfaa9ff73682321b1b4030ac6723259a4fc26a |
| wrapper 完成时刻 | 2026-11-14T18:45:19.379899+00:00 |

唯一生产者是成功 R759 run 43625474728、source 4728e6868e2509556e5c60e138fd97c9b4120d8e，其 manifest SHA 为
fb61ded80deb7f6904de7e0aa2e7a3f3b161a0ecd2f5f0c329e96935c4e9f1aa。
所读证书、LLL、原 maps 文件的 SHA 分别为
7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0、
5a1b6d44694389ac3fe48686a00c1745976726fefd8ff5196e2f60d4ef063825、
037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc。
两份已存 Gram 相等、对角次数与原证书相等、所有原配置相同，均在本次核实。

[公开小证书和小 LDL 文件](../computations/R769-retained-degree-lattice-bounded-search/43628341694-1/)连同全部 receipt 已保存。完整 artifact 为
serre-global-R769-retained-degree-lattice-bounded-search-43628341694-1，
ID 14126529570，ZIP 56513 字节，ZIP SHA-256
b086ff0331fca198b3cc41a698e807df8d0bc6af06c53d5306fa2efd7b50df95。

| 阶段 | SHA-256 |
|---|---|
| 原 Gram 与准确 LDL 小文件 | 012d5cb224b4da26e036a5102f4d7db19505d359ed782368de6463906d6f2b16 |
| 完整终态 checkpoint | 5d781bf9bd843fa59aa7024ed1e00931474e81fa731690c45b504a388857cdbc |
| audit manifest | 08a51c145b67f05447e4be5d5db3e36b0bbccaf7485ecd513da8e7632d893cc0 |
| audit block 0 | dfd60e1215b6b2267045c265bf9947f0411d65004086e340d28b0d847c1da3a5 |
| audit block 1 | cd558b1e01e146e6908c6668c444496732ad44fa2ab4f869d6a2f6478edcb6ca |
| 完整执行源 archive | e9bd48ed8ea0982f0abbb89723d3d4fa4206ef58e76126fd4baac05a2a88b523 |
| core receipt | be9467ba81ea7b74826f55f613d84cea8a7ba827577efcc57812a5522b34d92f |
| run receipt | c65a9befdabf836d0b266e0da845adbd62dfb241f97c98ac1fe3c458080012b6 |

本次完整输出 manifest SHA 为 44ccc89bbba731081facba337fd55cca99488dc3014fab87b3af010a2d785b8a。全部可复现审计和源码 archive 保 artifact，小证书/矩阵/receipt/脚本与 SHA 保 Git。搜索没有待恢复的未完成分支。

## 4. 几何含义及继续的准确路线

由 R764，完整原格的全部映射把 20 个 cusp 和 $c_0$ 送到 $O$。原 deck 的这 21 个固定点在该纤维各贡献 $1\bmod3$，非固定轨道贡献 $0\bmod3$，故每个非零映射的次数满足
$$
d\equiv0\pmod3.
$$
结合本次排除，其次数至少为 696；这仍不声称实际最小值已知。

选择搜索界 693，是因为它保证原商上
$\deg((t)_0-(y)_\infty)=820-d\ge127$，从而 Riemann–Roch 无条件给出非零分母。这一由次数界保证的较小恢复方案在原完整格中不存在。不能据此排除所有可能特殊除子的较小表示。

实际已选 $d=1206$ 的映射继续用原 $D=2(t)_0$、权十二维数 1514 的确定路线。R767 已证明完整基构造与有限前缀，R764 已证原平移为零；下一步仍是真正基、函数、$\beta$ 和高度。不会把此次有限格排除当作全 $p$ Serre 一致性证明。

依据：[R759 原完整整数格与次数](R759-certified-original-integral-period-lattice-and-map-degrees.md)、[R764 原全部尖点像](R764-certified-original-cusp-images-and-base-translation.md)、[R767 原 RR 构造](R767-original-quotient-low-weight-RR-basis-and-cusp-order-bound.md)和上述真实公开产物。
