# R271 附录：六位一特殊权的完整 S2、尖锐平方迹预算与原标量门反例

数据保存说明（2026-11-28）：可重算载荷已按根规矩8/15从main移除，相关旧链接只定位既有历史；当前保留生成源、参数定义、run与SHA，原数学及执行身份不变。


- 日期：2026-11-28（Asia/Taipei）
- 会话：Astra-ISP-8542378f-20261127
- 对象：六个原 Boolean 物理权 $b=(\sqrt t,1,1,1,1,1)$，$t>0$。
- 原来源：[六位完整 pair companion 输入](../notes/2026-11-28-six-bit-birth-two-s2-full-pair-companion-8542.md)。本篇保留其中同一个完整上来源、低来源、两个交叉项和物理伴随。
- 本篇不声称六个任意独立正权的 S2 已闭；不声称内部 $j=2$ half、七位来源或原边界 $N=M$ 已闭。

## 1. 结论和精确范围

在上述完整原 S2 中，记低空间为 $L=\ker d_1$，上空间为 $K=\ker d_2$。令
$$
L_j=P_LF_{j,1}^{-1}|_L,\qquad
G_u=P_KF_{1,2}^{-1}|_K,\qquad C_u=G_u^{-1},
$$
其中
$$
F_{j,k}=\frac{d^{\,j}d^{*j}}{(j!)^2}\bigg|_{H_k}.
$$
所有逆先取完整正 Gram 的逆，随后作真实正交压缩。

令 $B=P_Ld_{b^3}|_K$，并保留实际的两个来源：
$$
A=\frac12\bigl(C_uB^*L_2+B^*L_2L_3^{-1}L_2\bigr),\qquad
\mathsf K=A^*G_uA.
$$
完整 S2 左边是
$$
\mathsf S=\mathsf K+L_1L_2^{-1}L_1.
\tag{1.1}
$$

本一参数族上，$L$ 正交分解为一维尾置换不变块和四维尾标准块，并且
$$
\mathsf K=0\oplus \kappa(t)I_4,\qquad
\kappa(t)=
\frac{t(t-1)^2(3t+5)^2}{27(t+3)^2(t+1)^3}.
\tag{1.2}
$$
因此
$$
0\le\mathsf K<\frac13I_L,\qquad
0<\mathsf S<\frac12I_L,
\tag{1.3}
$$
且这两个一致常数分别由 $t\to\infty$ 达到上确界。更具体地，
$$
\operatorname{Tr}_L(\mathsf K^2)=4\kappa(t)^2<\frac49,
\qquad
\sup_{t>0}\operatorname{Tr}_L(\mathsf K^2)=\frac49.
\tag{1.4}
$$

故六位任意正权上的统一充分门
$\operatorname{Tr}(\mathsf K^2)<1/4$ **不成立**。这不是
$\mathsf K<I/2$ 或完整 S2 的反例；本篇在同一反例族上反而证明了更强的 (1.3)。

## 2. 物理坐标和完整正交块

把原物理坐标写成
$$
u_I=\left(\prod_{i\in I}b_i\right)f_I,\qquad z_i=b_i^2.
$$
于是物理内积是
$$
\|f\|^2=\sum_I z_I|f_I|^2,
$$
原下降和真实伴随分别为
$$
(df)_J=\sum_{i\notin J}z_i f_{J\cup\{i\}},\qquad
(d^*g)_I=\sum_{i\in I}g_{I\setminus\{i\}}.
\tag{2.1}
$$
所以不能将以下矩阵的普通转置冒充物理伴随。立方权下降在此坐标的系数为 $z_i^2$。

把特殊位置记为 $0$，尾位置为 $1,\dots,5$。对任意
$u=(u_1,\dots,u_5)$、$\sum_i u_i=0$，二孔尾标准的两复制写为
$$
f_{0i}=a u_i,\qquad f_{ij}=c(u_i+u_j)\quad(1\le i<j\le5).
$$
因为
$\sum_{i<j}|u_i+u_j|^2=3\sum_i|u_i|^2$，两复制的真实度量是
$$
\operatorname{diag}(t,3)\,\|u\|^2.
\tag{2.2}
$$
在此完整两复制上，下降、伴随和完整上 Gram 为
$$
R=(t,3),\qquad R^*=\binom11,\qquad
F_u=d_3d_3^*=
\begin{pmatrix}3&3\\t&t+4\end{pmatrix}.
\tag{2.3}
$$
这也可由
$F_u=(t+5)I-2\operatorname{diag}(t+1,2)+R^*R$
直接得到。矩阵 $\operatorname{diag}(t,3)F_u$ 对称，且
$$
\det F_u=12,\qquad
F_u^{-1}=\frac1{12}
\begin{pmatrix}t+4&-3\\-t&3\end{pmatrix}.
\tag{2.4}
$$
这里的完整逆在压缩之前已全部保留。

在二孔尾置换不变两复制 $f_{0i}=a,\ f_{ij}=c$ 上，
下降的输出是 $(5a,ta+4c)$，所以没有非零核。
另外五维的纯尾二孔分量满足每一尾行和为零，特殊位置坐标为零；
它同时被 $d_2$ 和 $d_{b^3}$ 消去。因而 $K$ 的九维分解为：
上述标准两复制中的四维核，以及这五维纯尾核。
所有 Gram、压缩、逆和 $B$ 都保持这些正交块；这也可直接从
(2.1) 的尾置换对称性与这三个坐标描述检查。
特别地，$B^*$ 在低一维不变块为零，不会有遗漏的上来源。

## 3. 同一完整上来源的压缩和费用

标准两复制内 $K$ 的方向为
$$
v=(3,-t),\qquad \|v\|_{\rm phys}^2=3t(t+3)\|u\|^2.
$$
从完整 (2.4) 后压缩可得
$$
G_u=\frac{\langle F_u^{-1}v,v\rangle_{\rm phys}}
{\|v\|_{\rm phys}^2}
=\frac{t+1}{t+3},\qquad
C_u=\frac{t+3}{t+1}.
\tag{3.1}
$$
立方权下降在两复制上是 $C=(t^2,3)$，故
$$
Cv=3t(t-1),\qquad
BB^*=\frac{3t(t-1)^2}{t+3}I_4.
\tag{3.2}
$$
输出已经在低标准块，无需改变低来源。

低标准块的完整除阶 Gram 是
$$
F_{j,1}=\binom3j+t\binom3{j-1}.
$$
这由 (2.1) 对尾零和向量直接计数得到。因此
$$
L_1=\frac1{t+3},\qquad
L_2=\frac1{3(t+1)},\qquad
L_3^{-1}=3t+1
\tag{3.3}
$$
均作用在同一个四维标准块。

将 (3.1)–(3.3) 代回原来的两个来源，先相加、再平方：
$$
C_uL_2+L_2L_3^{-1}L_2
=\frac{2(3t+5)}{9(t+1)^2}.
$$
于是
$$
\begin{aligned}
\mathsf K|_{\rm std}
&=\frac14\,BB^*G_u
 \left(C_uL_2+L_2L_3^{-1}L_2\right)^2\\
&=\frac{t(t-1)^2(3t+5)^2}
 {27(t+3)^2(t+1)^3}I_4.
\end{aligned}
$$
这一步保留了两个交叉项，且始终使用同一个 $B$、$G_u$ 和低块。

## 4. 低不变块及完整 S2

低不变两复制 $f_0=a,\ f_i=c$ 的真实度量是
$\operatorname{diag}(t,5)$，低核方向是 $(5,-t)$。
在这个完整两复制上，
$$
F_{1,1}=\begin{pmatrix}5&5\\t&t+8\end{pmatrix},
\qquad
F_{2,1}=\begin{pmatrix}10&20\\4t&8t+18\end{pmatrix}.
$$
其行列式分别为 $40,180$。先完整求逆再压缩到 $(5,-t)$，给出
$$
L_1=\frac{t+2}{2(t+5)},\qquad
L_2=\frac{t+1}{2(t+5)}.
$$
这与已刊[六位 first/last half](R271-appendix-six-independent-positive-weights-birth-one-sharp-half-first-last-edges.md)
的同一不变块公式一致；本篇使用它来完成同一 S2。

因此
$$
\mathsf S|_{\rm triv}=
\frac{(t+2)^2}{2(t+5)(t+1)}<\frac12,
\tag{4.1}
$$
因为 $(t+5)(t+1)-(t+2)^2=2t+1>0$。
在标准块，
$$
\mathsf S|_{\rm std}
=\left(\kappa(t)+\frac{3(t+1)}{(t+3)^2}\right)I_4.
\tag{4.2}
$$

置 $n=t(t-1)^2(3t+5)^2$、
$d=27(t+3)^2(t+1)^3$。直接整数恒等式为
$$
d-3n=243+816t+1302t^2+888t^3+207t^4>0
\tag{4.3}
$$
以及
$$
d-2n-162(t+1)^4
=81+193t+310t^2+214t^3+57t^4+9t^5>0.
\tag{4.4}
$$
(4.3) 给 $\kappa<1/3$；(4.4) 恰是
$2d$ 乘以 (4.2) 距离 $1/2$ 的差。
由 (4.1)–(4.4) 得到完整 (1.3)。
当 $t\to\infty$，$\kappa(t)\to1/3$，
(4.1) 趋于 $1/2$，故两个常数及 (1.4) 都是本族的尖锐上确界。

## 5. 原统一平方迹门的实际反例

取 $t=36$，即原物理权 $b=(6,1,1,1,1,1)$。
$$
\kappa(36)=\frac{62568100}{231129639},
\qquad
\operatorname{Tr}(\mathsf K^2)
=\frac{15659068550440000}{53420910024270321}>\frac14.
\tag{5.1}
$$
最后严格不等式的交叉相减为
$9215364177489679>0$。

这里 $\mathsf K$ 的四个相同非零特征值各自小于 $1/3$；
平方迹的四重累加损失使 $1/4$ 门失败。
完整 S2 同时满足 $\mathsf S<I/2$。
因此下一步应处理同一完整矩阵预算或其真实谱，
不能再试图证明这个已被 (5.1) 排除的统一平方迹上界。

## 6. 唯一实际返回、保存参数和计算范围

原首次运行 run **46052984288**、job **140688624777**：
内层 **24.720906012 秒 / 378284 KiB / exit 0**，
状态 **EXACT_SCALAR_READY**。完整 $15\times15$ 上逆在
$0.553607569$ 秒形成，完整原费用在 $1.548203111$ 秒形成，
原平方迹标量在 $24.382204952$ 秒形成。外层绿色和此状态本身都不证明正性。

原标量 $N/D$ 的共同加权次数为 $144$；
完整表 $119401$ 行，$N$ 非零项 $119367$。
83 段载荷共 $13500093$ 字节，SHA-256：
$$
\texttt{423b912b07b261926425ae25ef7cf581fa24acd2e3755e558081b70404f3dab4}.
$$
已实际逐行核 $D-4N$，并在 $t=36$ 对全部原系数作 BigInt 求值，
结果与 (5.1) **精确相等**，不是浮点筛查。

原分母为
$$
D=S^2e_4^4(\det F_1)^4(\det F_2)^6(\det F_u)^2.
$$
原 $N$ 的整数 content 恰等于
$4^4\,9^6\,9216^2=11555266180939776$，可全消。
对三个完整 primitive 因子的精确单除法均出现非零余项；
这不声称其可能的真因子已全部互素。该尝试没有降低次数，
也不再作为追逐已失败平方迹门的理由。

小文件保留了原全部十五个上特征系数、原正分母因子、唯一运行与标量哈希；
不把已无证明用途的 13.5 MB 全表拆入仓库。
独立的完整纸面证明是 §§2–5，
小型 V8 整数证书同时核了真实两复制逆、同源两个交叉项、
(4.3)–(4.4)、(5.1) 与全部保存标量在该点的精确一致性。
新证书实际耗时见对应 JSON；没有重放原矩阵逆或原标量构造。

配套：
- [完整物理一参数证书](../notes/2026-11-28-six-bit-s2-one-parameter-exact-8542.mjs)
- [实际回执](../notes/2026-11-28-six-bit-s2-one-parameter-exact-8542.json)
- [原十五特征及正分母小参数](https://github.com/Rogerhu12/math-research-public/blob/3b9cda56dfa6a1ae9d4ca2a35fa81798a5f156c9/topics/invariant-subspace-problem/notes/2026-11-28-six-bit-s2-retained-exact-parameters-8542.json)

**未付范围：** 一般六个独立正权的完整 S2、一般原内部 $j=2$ half、
更高出生层和原无限边界的同源费用均保持开放。
