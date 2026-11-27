# R150：整个原 L0 的 G 曲线为空

作者：AI-assisted GPT-6 Astra Pro；会话 `Astra-ISP-8542378f-20261127`。日期：2026-11-27（Asia/Taipei）。

**结论。** 在原 unit211 的 L0 图上，整个 G(lambda,w)=0 分支不存在物理解。证明包括已经独立关闭的 w 首项零纤维，以及本稿从完整原九式得到的全部有限参数域。只关闭这条曲线；G 非零下的其余原交点、一般 unit211 及普通 ISP 仍须继续。

本次[自含精确源](../notes/2026-11-27-unit211-L0-G-complete-original-return-8542.py)从原 Frobenius 乘法、Gram 和同根 P/N 重建所有输入，不读取任何缓存系数。实际运行 25.192543 秒，exit 0。下文说明投影、有限域证据和原参数返回各自的逻辑；没有把多变量 gcd 或一个有限域单位理想当成复域排空。

## 1. 原曲线、同一参数及已付除数

沿用[原 P1 双零完整排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-P1-double-zero-complete-exclusion.md)的 rho、lambda、w，保持原二次代数 kappa²=Delta 的两个根。写

$$
A=2\lambda^2-2\lambda+1,\quad
B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
R=\lambda-1-w,\quad C=RB-A^2,
$$
$$
u=R/\rho,\quad V_2=A/\rho^2,\quad
Q=\frac{2A\rho-B}{\rho^2R},\quad
\Delta=1-Q,\quad \ell=(2u-V_2)/Q,
$$
$$
P_0=\tfrac12\big((2-3u)V_2-Qu+2u^3\big).
$$
原物理单位为 rho、lambda、w、w−1、R、C，以及 Delta、Q、P0、u−1、ell 的已清分母分子。ell 非零由[完整零权和排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-zero-weight-sum-exclusion.md)支付；不是一般位置假设。A 可为零，始终没有除 A。

准确曲线为 G=sum(g_j w^j,j=0..4)，其中

$$
\begin{aligned}
g_4={}&-8\lambda(\lambda-1)(4\lambda^2-5\lambda+2)(4\lambda^2-2\lambda+1),\\
g_3={}&384\lambda^7-1472\lambda^6+2304\lambda^5-1936\lambda^4
       +952\lambda^3-264\lambda^2+28\lambda+4,\\
g_2={}&576\lambda^7-1904\lambda^6+2592\lambda^5-1916\lambda^4
       +828\lambda^3-194\lambda^2+10\lambda+4,\\
g_1={}&192\lambda^7-464\lambda^6+368\lambda^5-20\lambda^4
       -156\lambda^3+120\lambda^2-42\lambda+6,\\
g_0={}&32\lambda^6-96\lambda^5+120\lambda^4-84\lambda^3
       +36\lambda^2-9\lambda+1.
\end{aligned}
\tag{1}
$$

[全部 g4=0 纤维](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-G-leading-w-zero-exclusion.md)已经独立返回原式并排空，因此本稿可支付 g4。另有[W 整曲线](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-linear-lambda-curve-exclusion.md)

$$
W=4\lambda w+2\lambda-2w^2-4w-1=0
\tag{2}
$$

已经关闭，W 可作后续原参数返回的单位。

令原 P1=alpha·t+beta。已闭整个 alpha=beta=0 分支；原解上 P1=0 故 alpha=0 会迫 beta=0。因此 alpha 在所有现余原解上非零。源中的 alpha0 只除原已付单位，与 alpha 的非零性等价。

## 2. 只作原必要式与已付伪余式

完整原九式为 E1、EB 的偶/奇分量、P1、PB 的偶/奇分量、N1、NB 的偶/奇分量。对其中关于 t 的多项式 H=sum(c_j t^j,j=0..d)，定义

$$
F_H=\sum_{j=0}^d c_j(-\beta)^j\alpha^{d-j}.
\tag{3}
$$

只剥原物理单位，得到源码 P1_E1、P1_N1、P1_EBe 等。式 (3) 来自同一个 t，不把平方根或 P/N 的根独立重选。

把 F_H 对 G 作 w 伪除法，实际回乘

$$
g_4^sF_H=GQ_H+R_H,\qquad \deg_wR_H<4.
\tag{4}
$$

只剥 (1) 已付首项及原物理单位后，取三个必要式 E、N、J：

| 原式 | (rho,lambda,w) 次数 | 项数 |
|---|---:|---:|
| P1_E1 的原伪余式 E | (4,71,3) | 1367 |
| P1_N1 的原伪余式 N | (4,76,3) | 1479 |
| P1_EBe 的原伪余式 J | (6,79,3) | 2137 |

(4) 保留所有 rho 首项零和降次纤维，没有在 rho 上除一个未付首项。

## 3. 完整一元参数覆盖

取完整 Sylvester 结式

$$
H_1(\lambda,w)=\operatorname{Res}_{\rho}(E,N).
$$

剥已付单位，再按 (4) 对 G 作 w 伪余式，得到 Hbar1，实际次数 (lambda,w)=(637,3)。于是每个原解都必须满足

$$
P(\lambda)=\operatorname{Res}_w(G,\overline H_1)=0.
\tag{5}
$$

仍只剥已付单位。源实际得到 P 次数 914，其平方自由部分 S 次数 306。通过准确因子分解及乘积回乘，S 有十一项不可约因子，次数依次为

$$
1,2,2,2,6,7,8,8,20,46,204.
\tag{6}
$$

平方自由化也实际检查 P=gcd(P,P')·(P/gcd(P,P'))。因此 (6) 是完整必要覆盖，没有遗漏多重参数根。以下 phi20、phi46、phi204 分别指 S 中唯一相应次数的因子；两条八次因子以其整系数常数项 97 和 −9 区分。全部低次系数与哈希在实际回执中，完整高系数由源的定义重算。

P 的 SHA256 为 `fce6e0598a3bf287b1b51f38803e43359f96024819daeb0a12cfc8ecd716c500`；首一 S 的 SHA256 为 `7f66899c158f6ccbae76a6474f129dc53e5c1ffc0e0b13c0051fb45ea7dd60af`。

## 4. 204 次因子的特征零一元排除

另取真正原必要投影

$$
H_2=\operatorname{Res}_\rho(E,J),\qquad
P_2=\operatorname{Res}_w(G,H_2).
\tag{7}
$$

不需把 P2 的全部巨大有理系数写入仓库。取 p=1031；源逐系数检查 E、J、G 的所有分母在该素数下可逆。原 rho 次数 4、6 及 w 次数 3、3 在模 p 后保持；故 H2 的 w 次数至多 30，而其实际模 p 结果式的 w 次数等于 30，证明原次数准确为 30。G 的 w 次数 4 也保持。因此源码所算的第二层模结果式确实是 (7) 的准确模像，次数为 2920。

phi204 在模 p 后仍为 204 次，首项未消失。源在 F_p[lambda] 实际计算并回乘

$$
s\overline{\phi}_{204}+t\overline P_2=c,\qquad c\ne0.
\tag{8}
$$

这严格推出 gcd_QQ(phi204,P2)=1。确切地，phi204 和 P2 属于 Z_(p)[lambda]，phi204 的首项在该局部环中可逆。若有正次数的有理公因子，将它规范成首一因子后，由 Gauss 引理及首一整性，它及两个余因子的相关除法均可在这个局部环中进行；其模像次数不会下降，并会同时整除 (8) 左边两式，矛盾。

所以 phi204 的任何复根都不能同时满足原必要投影 (7)。这里证明的是一个明确**一元有理公因子不存在**的精确模证据；不是有限域多变量理想为空的泛推断。没有假定 P2 的全部 lambda 首项在模 p 后保持，也不需要该假定。

## 5. 其余十个域始终保同一 lambda、w

对每个余不可约 phi，在真实数域 K_phi=QQ[lambda]/(phi) 中，将 G 与 Hbar1 取关于 w 的公共因子。源码使用无分式 Euclid；每步实际核

$$
a^sP=QD+R,\qquad a=\operatorname{lc}_wD\ne0\text{ in }K_\phi.
\tag{9}
$$

不可约性使 a 是这个准确数域的单位。每次清有理内容也完整回乘。该方法避免旧普通域逆计算的系数膨胀，不丢参数嵌入。

前八个域的所有 w 因子由下列已付原单位排尽，重数重复除去：

| phi 的次数或明确多项式 | 原 w 公因子次数 | 付清原因 |
|---|---:|---|
| 2lambda−1 | 3 | w，重复三次 |
| 2lambda²−2lambda+1 | 1 | R=lambda−1−w |
| 3lambda²−2lambda+1 | 2 | C=RB−A²，重复两次 |
| 8lambda²−6lambda−1 | 1 | w−1 |
| phi6 | 1 | C |
| phi7 | 1 | R |
| phi8，常数项 97 | 1 | 原 P0 分子 |
| phi8，常数项 −9 | 1 | 已闭 W 曲线 |

所有除法均按 (9) 回乘，除去一个单位因子后保留余商为新的原必要式，直到非零常数。没有只检查平方自由因子而遗留重复因子。

## 6. 20、46 次域返回原 rho

余两个域的 w 公因子都为 a(lambda)w+b(lambda)。源码以“乘 a”的准确有理矩阵解

$$
M_a\,\mathbf w=-\mathbf b,
\tag{10}
$$

并核 M_a·w=−b 及原 a·w+b=0。实际有理矩阵在模 1031 的行列式分别为 893、639，均非零，所有矩阵分母在该模下可逆。由此付清真实的唯一 w 值，另外逐项核原 G(lambda,w)=0。始终在同一个 K_phi 中代入，未选择不相关的根。

现在把**原未降次**的 P1_E1、P1_N1 代回同一 lambda,w，得到 rho 一元式。通过 (9) 的无分式版本取公共因子，再剥原单位：

| 参数域 | 原公共 rho 因子次数 | 全部原单位返回 |
|---|---:|---|
| phi20 | 2 | 原 Q 分子两次 |
| phi46 | 3 | 原 Q 分子一次、已付 alpha0 两次 |

全部伪除法与余商实际回乘，最后均为非零常数。alpha0 的非零性来自 §1 的**已完成整个 P1 双零排除**，不是在本分支上偷加一般位置条件。于是两个域的全部相关复嵌入和全部原 rho、t 都排尽。

结合 §4、§5 和既有 g4=0 排除，整个 G 曲线为空。

## 7. 实际运行、边界和接续

[实际回执](../notes/2026-11-27-unit211-L0-G-complete-original-execution-8542.json)记录 Python 3.12.14、python-flint 0.9.0、300 秒 alarm、4 GiB 地址空间上限。实际 exit 0，25.192543 秒，峰值 RSS 125164 KiB；共 35 个原分母、4 个完整多变量伪除身份、178 个数域伪除身份、356 个有理内容回乘。自含源 24332 字节，SHA256：

```
be8068dbf2c3cfd4ff4f1ba1b4f979b0ee5ab8076dda01c542fe600ae28d3884
```

旧 G 的 465 秒/4 GiB 单位门没有重跑；本稿使用原 w 四次伪余式和低次同根返回。中途未完成的普通域逆和大投影试探如实保留为未决运行，不从其超时推出空性。

下一实际剩余为 G 非零下的原 L0 交点；本定理也没有支付全局理想的 Bell 自然幂来源、其他 unit211 图或算子桥。
