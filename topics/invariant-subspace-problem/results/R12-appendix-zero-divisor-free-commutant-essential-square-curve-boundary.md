# R12 附录：无零因子交换子的实际平方曲线仍可有本性奇点

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127，stable_kernel_return。AI-assisted，GPT-6 Astra Pro。

**状态：完整反检验。** 本文给一个独立的双边权移模型，严格排除下列推理：仅由“交换子代数无零因子、每个参数算子单射且像稠密、首位型二阶符号作用、全空间连续 $J$ 对称、平方全纯延拓”，便认为根曲线只能有可去奇点或有限极点。

这个模型不是原 Haar 算子。它有明确超不变尾空间，并且不满足原稿已经支付的“全部原旗子商上像稠密”。因此它没有排除原全旗输入，也没有给出任何 Hilbert 不变子空间问题反例。

## 1. 实际算子与全空间范围

在 $H=\ell^2(\mathbb Z)$ 的标准正交基上，令
$$
T e_n=w_n e_{n+1},\qquad
w_n=\exp(-(n+1)^2)>0.
\tag{1}
$$
$T$ 有界且 $\|T\|=1$。因 $w_n\to0$ 当 $|n|\to\infty$，截去有限个中间权后剩余算子的范数趋零，故 $T$ 紧。

每个权均非零，所以 $T$ 单射；每个基向量都属于 $\operatorname{Ran}T$，故该像稠密。其每个正整数幂同样单射且像稠密。准确地，
$$
\|T^k\|
=\sup_{n\in\mathbb Z}
\exp\!\left(-\sum_{j=1}^k(n+j)^2\right)
\le\exp\!\left(-\frac{k(k^2-1)}{12}\right).
\tag{2}
$$
最后一步是先允许实数 $n$，在 $n=-(k+1)/2$ 处求平方和最小值。因此 $\|T^k\|^{1/k}\to0$，$T$ 拟幂零。

定义
$$
Ue_n=(-1)^n e_n,\qquad
Je_n=e_{-1-n},
\tag{3}
$$
其中 $J$ 反线性延拓。则 $U=U^*=U^{-1}$，$J$ 为共轭，且
$$
UTU=-T,\qquad UJ=-JU,\qquad T^*=JTJ.
\tag{4}
$$
后一式逐基向量核算：
$JTJe_n=w_{-1-n}e_{n-1}=e^{-n^2}e_{n-1}=T^*e_n$。

## 2. 完整 $T'$ 的矩阵来源与无零因子

这一节证明实际完整交换子的结构，不仅证明多项式子代数的性质。

对 $r\ge0$ 记
$$
b_{j,r}=\prod_{\nu=j}^{j+r-1}w_\nu,\qquad b_{j,0}=1,
$$
对 $h\ge1$ 记
$$
b_{j,-h}=\left(\prod_{\nu=j-h}^{j-1}w_\nu\right)^{-1}.
$$
若 $A\in T'$，写 $a_{ij}$ 为其基矩阵。由 $AT=TA$，
$$
w_j a_{i,j+1}=w_{i-1}a_{i-1,j}.
\tag{5}
$$
固定偏移 $r=i-j$，此递推和全部 $w_j\ne0$ 给唯一标量 $\alpha_r$，使
$$
a_{j+r,j}=\alpha_r b_{j,r}\qquad(j\in\mathbb Z).
\tag{6}
$$
当 $r=-h<0$ 时，$b_{j,-h}\to\infty$ 当 $j\to+\infty$；但每个矩阵元绝对值至多 $\|A\|$。所以
$$
\alpha_r=0\qquad(r<0).
\tag{7}
$$
非零 $A$ 因而有最小非负偏移
$$
m(A)=\min\{r\ge0:\alpha_r\ne0\}.
\tag{8}
$$
这里没有声称级数 $\sum\alpha_rT^r$ 在算子范数中收敛；(6) 是逐矩阵元的完整身份。

若 $B\in T'$ 对应系数为 $\beta_r$，则固定非负偏移 $r$ 的乘积矩阵元只涉及有限个中间指标，由 (7) 准确得到
$$
(AB)_{j+r,j}
=b_{j,r}\sum_{k=0}^r\alpha_{r-k}\beta_k.
\tag{9}
$$
因此 $AB=BA$。若 $A,B$ 都非零，在偏移 $m(A)+m(B)$ 处的和只剩
$\alpha_{m(A)}\beta_{m(B)}\ne0$，故
$$
AB\ne0.
\tag{10}
$$
所以完整 $T'$ 是交换的，并且没有非零零因子；这不是谱推断。

完整交换子也保留全空间 $J$ 对称。原权满足
$$
b_{-1-j-r,r}=b_{j,r}\qquad(r\ge0).
$$
结合 (6)，直接计算 $JA^*J$ 的各矩阵元得到 $JA^*J=A$。于是对所有 $A\in T'$，
$$
A^*=JAJ,\qquad
[Ax,y]=[x,Ay],\qquad [x,y]=\langle x,Jy\rangle.
\tag{11}
$$
该双线性形式连续且非退化。$U$ 共轭给 $T'$ 上的等距代数自同构
$\gamma(A)=UAU$，且 $\gamma^2=\mathrm{id}$。

## 3. 原有界曲线、准亲和与本性奇点

定义整个算子值多项式
$$
P(z)=T^3+zT^2.
\tag{12}
$$
当 $z\ne0$ 时，$P(z)=T^2(zI+T)$，而 $zI+T$ 是有界可逆元；当 $z=0$ 时 $P(0)=T^3$。所以每个 $P(z)$ 都单射且像稠密。

对 $s\ne0$，定义
$$
X(s)=sT
\sum_{k\ge0}\binom{1/2}{k}\frac{T^k}{s^{2k}}.
\tag{13}
$$
由 (2)，级数在每个闭环域上算子范数绝对且一致收敛。其平方由同一解析芽函数演算或绝对 Cauchy 乘积给出：
$$
\boxed{
X(s)^2=T^3+s^2T^2=P(s^2),\qquad
\|X(s)^2-P(0)\|=|s|^2\|T^2\|.
}
\tag{14}
$$
括号内的解析算子平方为 $I+T/s^2$，其零点常数为一，故它及其逆均有界。因此每个 $X(s)$ 的实际像恰为 $\operatorname{Ran}T$，且它单射；每个参数值都是 quasiaffinity。

同一范数 Laurent 展开为
$$
X(s)=\sum_{k\ge0}\binom{1/2}{k}T^{k+1}s^{\,1-2k}.
\tag{15}
$$
对全部 $k\ge1$，系数都非零：二项式系数不为零且 $T^{k+1}$ 单射。因此零点具有无穷多个非零负 Laurent 项，是真正的本性奇点。它不是有限极点，也不可能可去。

此外直接由 (4)、(13) 得
$$
X(-s)=-X(s),\qquad
\gamma(P(z))=-P(-z),\qquad
\boxed{\gamma(X(s))=iX(is).}
\tag{16}
$$
若 $H^\pm(s)=\gamma(X(s))\pm iX(s)$，则
$$
H^+(s)H^-(s)=2s^2T^2\longrightarrow0
\quad\text{于算子范数}.
\tag{17}
$$
这些性质与全空间连续 $J$ 对称及完整交换子无零因子同时成立。

## 4. 为什么没有支付原全旗情形

对每个整数 $j$，令
$$
L_j=\overline{\operatorname{span}}\{e_n:n\ge j\}.
$$
由 (7)，每个 $L_j$ 都对完整 $T'$ 不变，所以它是明确的非零真超不变子空间。并且
$$
\overline{T^rL_j}=L_{j+r}\qquad(r\ge1).
\tag{18}
$$
解析可逆元 $zI+T$ 及其逆保持 $L_j$；(13) 中的解析单位及其逆也保持它。故
$$
\overline{P(z)L_j}=
\begin{cases}
L_{j+2},&z\ne0,\\
L_{j+3},&z=0,
\end{cases}
\qquad
\overline{X(s)L_j}=L_{j+1}.
\tag{19}
$$
这些像都不在 $L_j$ 中稠密。因此本例不具有[原同参数构造](R267-appendix-all-factor-complex-parameter-odd-target-and-norm-square-source.md) 的全旗准亲和性质，更不满足“原算子没有超不变子空间”的假设。

结论仅为：从无零因子这一代数后果出发，不能把本性奇点自动排掉。若继续原 Haar 路线，必须实际使用其更强的全旗来源、原同一列的费用，或另一个已支付的原模型输入。
