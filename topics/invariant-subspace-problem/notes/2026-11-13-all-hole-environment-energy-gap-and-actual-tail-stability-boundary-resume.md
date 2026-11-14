# 纯尾及实际尾的全孔层联合能量下界：一个有限交换子证书

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065 / boundary_resume；AI 辅助：GPT-6 Astra Pro。显式短证书由 root 提供并全文复核。
状态：本文证明全环境联合能量的严格下界。它没有证明受限链 Gram 的下界，也没有完成无权核内饱和。

## 1. 对象与结论

令 $m\ge5$，在完整有限子集尾空间上取
$$
a_j=(j+1)^{-2},\quad D=D_m=\sum_{j\ge m}a_jE_j,\quad
S=\sum_{j\ge m}a_j^2,\quad W=\sum_{j\ge m}a_j^2 n_j.
$$
所有和按算子范数收敛，$n_j=E_j^*E_j$。置
$$
a=a_m,\qquad k=4(m+1),\qquad
L_m=a^{-1}\left(\frac{2\|D\|^2}{a^2}\right)^k .
\tag{1.1}
$$
则在整个尾 Hilbert 空间、同时在任意额外头因子的张量积上，
$$
\boxed{D^*D+DD^*\ \ge\ \frac1{4L_m^2}I.}
\tag{1.2}
$$
常数不依赖孔数；不要求预先限制于某个有限层。

特别，$x\in\ker D$ 时，
$$
\|D^*x\|\ge\frac1{2L_m}\|x\|.
\tag{1.3}
$$
这里是环境 $D^*$，不是受限算子 $D:\ker D^2\to\ker D$ 的伴随。

## 2. 隔离单个位的矩阵单元

同位矩阵关系给
$$
[D,D^*]=S I-2W,\qquad [W,E_j]=-a_j^2E_j.
$$
定义有限嵌套交换子
$$
Z_k=\frac1a\left(-a^{-2}\operatorname{ad}_W\right)^kD
=E_m+\sum_{j>m}(a_j/a)^{2k+1}E_j .
\tag{2.1}
$$
第二个等式由范数收敛级数逐项计算而来。余项的范数至多
$$
\begin{aligned}
\varepsilon_m
&=\sum_{j>m}\left(\frac{m+1}{j+1}\right)^{4k+2}\\
&\le \int_{m+1}^{\infty}
\left(\frac{m+1}{x}\right)^{4k+2}\,dx
=\frac{m+1}{4k+1}<\frac1{16}.
\end{aligned}
\tag{2.2}
$$
这使用正的递减函数的右端和，不需要额外的指数尾近似。

令 $C=[D,D^*]$。由于 $\operatorname{ad}_W=-\frac12\operatorname{ad}_C$，
$$
Z_k=2^{-k}a^{-(2k+1)}\operatorname{ad}_C^kD .
\tag{2.3}
$$
将每次交换子及每个 $C=DD^*-D^*D$ 完全展开，所得词均长 $2k+1$，
没有常数项，绝对系数总和至多 $4^k$。
对
$$
\mathcal E(x)=\|Dx\|^2+\|D^*x\|^2
$$
每个词的最右因子是 $D$ 或 $D^*$，故
$$
\|Z_kx\|\le L_m\mathcal E(x)^{1/2},
\qquad
\|Z_k^*x\|\le L_m\mathcal E(x)^{1/2}.
\tag{2.4}
$$
第二式同样对完全展开后的伴随词使用最右因子估计。

## 3. 从矩阵单元得到统一能量

实际单位置恒等式是
$$
E_m^*E_m+E_mE_m^*=I.
$$
结合 (2.2)，在两个分量的 Hilbert 直和中用三角不等式，
$$
\begin{aligned}
\bigl(\|Z_kx\|^2+\|Z_k^*x\|^2\bigr)^{1/2}
&\ge \bigl(\|E_mx\|^2+\|E_m^*x\|^2\bigr)^{1/2}
-\sqrt2\,\varepsilon_m\|x\|\\
&\ge(1-\sqrt2/16)\|x\|.
\end{aligned}
$$
另一方面，(2.4) 将左侧控制在 $\sqrt2 L_m\mathcal E(x)^{1/2}$。
由于 $(1-\sqrt2/16)^2/2>1/4$，这证明 (1.2)。

证明只使用有限次交换子、一个真实矩阵单元及显式尾和。
不需要调用无限张量积 $C^*$ 代数的无字符定理。

## 4. 自适应头下只有次幂损失

积分比较给 $\|D\|\le\sum_{j\ge m}(j+1)^{-2}\le1/m$，所以
$$
L_m\le(m+1)^2
\left(\frac{2(m+1)^4}{m^2}\right)^{4(m+1)}
\le(m+1)^2\bigl(8(m+1)^2\bigr)^{4(m+1)}.
\tag{4.1}
$$
因此
$$
\log L_m=O(m\log(m+1)).
\tag{4.2}
$$
沿原全整数头 $m(q)=O(\log\log q)$，
$$
4L_{m(q)}^2=q^{o(1)}.
\tag{4.3}
$$
该次幂常数来自环境联合能量，不得将它替换为原最小修复常数。

## 5. 对实际尾和的稳定版本

令
$$
X_N=\sum_{j\ge m}a_jN_j,\qquad
X_Y=\sum_{j\ge m}a_jY_j
$$
为两个模型的实际尾和。原矩阵及 Cayley 逆差估计给
$\|N_j-E_j\|\le\eta_j$、$\|Y_j-E_j\|\le4\eta_j$，从而两型统一有
$$
\|X_\bullet-D\|\le8\eta_m,\qquad
\eta_m\le e^{-770\,16^m}.
\tag{5.1}
$$
由 (4.1) 粗取 $\log L_m\le16(m+1)^2$，对 $m\ge5$ 有
$$
32\sqrt2 L_m\eta_m\le1.
\tag{5.2}
$$
例如其对数至多
$\log(32\sqrt2)+16(m+1)^2-770\,16^m<0$；
这里 $(m+1)^2\le16^m$ 已足够。

在两个分量的直和中，
$$
\begin{aligned}
(\|X_\bullet x\|^2+\|X_\bullet^*x\|^2)^{1/2}
&\ge(\|Dx\|^2+\|D^*x\|^2)^{1/2}
-\sqrt2\|X_\bullet-D\|\|x\|\\
&\ge\frac1{4L_m}\|x\|.
\end{aligned}
$$
所以实际尾也满足
$$
\boxed{X_\bullet^*X_\bullet+X_\bullet X_\bullet^*
\ge\frac1{16L_m^2}I.}
\tag{5.3}
$$
这里没有把完整 $T=A_m+X_\bullet+\text{carry}$ 换成纯尾。

## 6. 为什么它不消除受限伴随投影

对 $x\in\ker D$，实际受限伴随为
$$
\left(D:\ker D^2\to\ker D\right)^*x=P_{\ker D^2}D^*x.
$$
且准确有
$$
D^2D^*x=-2D_3x,\qquad D_3=\sum_{j\ge m}a_j^3E_j.
\tag{6.1}
$$
故 (1.3) 不支付 $(I-P_{\ker D^2})D^*x$。

一个有限维校准已能显示区别：令 $D=aE_0+bE_1$，
$a,b>0$ 且 $a\ne b$，并取
$$
h=(b|10\rangle-a|01\rangle)/\sqrt{a^2+b^2}.
$$
则 $Dh=0$，
$$
D^*h=\frac{b^2-a^2}{\sqrt{a^2+b^2}}|11\rangle\ne0,
$$
但 $D^2|11\rangle=2ab|\varnothing\rangle\ne0$，而
$\ker D^2$ 正好由真空及全部一孔向量组成。因此
$$
P_{\ker D^2}D^*h=0.
$$
该有限例只排除从环境能量直接下传受限链的推理，不断言原无限模型有相同坏核。

与 [R271 远尾双行 Hodge 稿](../results/R271-appendix-far-tail-two-row-hodge-inverse-and-optimal-joint-vacuum-jets.md)
衔接时，仍须在真实源上支付所用 $D_3$ 受限原像的成本与投影损失；仅有环境联合能量不支付这些量。
本稿没有完成这一接口，也没有推出 $N=M$。
