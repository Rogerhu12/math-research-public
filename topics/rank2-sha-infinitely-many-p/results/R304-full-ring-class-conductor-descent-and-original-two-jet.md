# R304：原全环类 trace 的 conductor 下降与同一 $\delta^2$ 类

日期：2026-11-13。**状态：已证明。** 本文证明完整 conductor 下降、全部原标签下的二阶 jet 比较及相同 Hilbert Heegner 点的 Kummer 等式。它补付 R296 的 optimal order 到 maximal order 的实际来源比较；没有新增跨 $p$ 非零结论。

## 1. 同一原来源和全部 conductor 纤维

保留 R281、R285 的固定曲线
$$
E:y^2+y=x^3+x^2-2x,\qquad N=389,
$$
及合法 $(p,F)$：$p\ge7$，$389$ 在 $F$ 分裂，$p$ 不分歧，$\mathcal O_F^\times=\{\pm1\}$，其余满像、普通非异常等原假设不变。取一个真实 admissible $q$，记其原 quaternionic 函数为 $\varphi_{p,q}$。它对 $r\nmid Npq$ 满足 $T_r\varphi_{p,q}=a_r(E)\varphi_{p,q}$，使用 R276/R281 的原 level、$q$ 取向及 CM reduction。

写
$$
H_c=F[c],\qquad H_1=H,\qquad
\mathcal C_c=\operatorname{Pic}(\mathbb Z+c\mathcal O_F),\qquad
C=\operatorname{Cl}(F)_{(p)},\qquad k=\mathbb F_p.
\tag{1}
$$
始终取 $\gcd(c,Npq)=1$；允许 conductor 素数在 $F$ 分歧，允许 $p\mid[H_c:H]$，也允许 $p$ 类群有多个方向。令 $\rho_c:\mathcal C_c\to C$ 为真实环类映射再取 $p$ 部分。

选择同一 $N$ 理想取向下兼容的原 CM 点 $x(c)$，其在原 modular parametrisation 下的点记为 $P[c]$。对 R285 同一杀扭整数 $t_F$，定义
$$
\Theta_c^{\max}
=\bar t_F\sum_{a\in\mathcal C_c}
\varphi_{p,q}(\operatorname{Red}_q x(c)^a)\,[\rho_c(a)]^{-1}
\ \in k[C].
\tag{2}
$$
这里对所有 conductor 纤维及原阶与 $p$ 互素部分作完整和，绝不除以纤维次数。(2) 中上标只表示目标群环为最大阶 $C$，不表示把 $x(c)$ 的节点换成了最大阶节点。$\Theta_1^{\max}=\Theta_1$ 是 R281 的原全来源，且
$$
J=\ker(k[C]\longrightarrow k),\qquad \Theta_1\in J.
\tag{3}
$$
(3) 来自同一个完整基层 Heegner 迹被 $t_F$ 杀掉，不能用于一个选中的闭路子和。

## 2. 实际 CM 邻点与完整 norm

固定 $r\nmid Npq$，置 $a=a_r(E)$、$\chi=\left(\frac{\operatorname{disc}F}{r}\right)\in\{-1,0,1\}$。在最大阶类群中定义水平算子
$$
\mathcal H_r=
\begin{cases}
0,&\chi=-1,\\
[\mathfrak r]+[\mathfrak r]^{-1},&\chi=1,\\
[\mathfrak r],&\chi=0.
\end{cases}
\tag{4}
$$
在分歧情形 $\mathfrak r^2=(r)$。以下可先在完整最大阶群环写 (4)，再送到 $\mathbb Z_p[C]$ 或任一实际 Hilbert 商。

**引理 2.1（原纤维）。** 若 $r\nmid c_0$，conductor $c_0$ 的原 CM 点有 $1+\chi$ 个水平 $r$ 邻点，其余 $r-\chi$ 个为 conductor $c_0r$ 的完整环类纤维。若 $r\mid c_0$，则有一个上升邻点，其余 $r$ 个为下一层的完整纤维。相应原 norm 为
$$
\begin{aligned}
\operatorname{Tr}_{H_{c_0r}/H_{c_0}}P[c_0r]
   &=(a-\mathcal H_r)P[c_0] &&(r\nmid c_0),\\
\operatorname{Tr}_{H_{c_0r}/H_{c_0}}P[c_0r]
   &=aP[c_0]-P[c_0/r] &&(r\mid c_0).
\end{aligned}
\tag{5}
$$
第一行的水平 Artin 类在 $\operatorname{Pic}(\mathcal O_{c_0})$ 中解释，推至最大阶即为 (4)。同样的等式先在实际 CM 除子上把 $a$ 换为 $T_r$ 成立，因此在 $q$ reduction 后对原 $\varphi_{p,q}$ 求值仍为 (5)。

**证明。** 将循环 $r$-isogeny 识别为 CM 椭圆曲线的 $r+1$ 个阶 $r$ 子群。局部最大整环作用的稳定线数分别为零、二、一，给三个水平情形；其余线的目标 endomorphism order 的 conductor 乘 $r$。局部单位商
$$
(\mathcal O_F/r\mathcal O_F)^\times/(\mathbb Z/r\mathbb Z)^\times
$$
对向下邻点简单传递，其阶为 $r-\chi$。较深层有唯一上升线，局部 conductor 商对其余 $r$ 条线简单传递。因为全局单位仅 $\{\pm1\}$，没有额外单位指数。由 CM 主定理，这些就是完整 Galois 纤维；没有要求其阶与 $p$ 互素。

全部 isogeny 的次数与 $Nq$ 互素，故原循环 $N$ 子群及 $q$ 取向随真实 isogeny 一并运输。Hecke 对应在 CM 除子上的定义于是给出 (5)，modular parametrisation 的 Hecke 等变性给点的等式。此即 Darmon 的已发表 Proposition 3.10 的原 norm 关系；这里同时保留它在原有限 CM 来源上的实现。证毕。

## 3. Prime-power 初始项及一般 conductor 的精确算子

令 $S_{-1}=0$，并定义
$$
S_0=1,\quad S_1=a,\quad
S_n=aS_{n-1}-rS_{n-2}\quad(n\ge2).
\tag{6}
$$
令 $E_{r,0}=1$，对 $n\ge1$ 置
$$
E_{r,n}=S_n-\mathcal H_r S_{n-1}+\chi S_{n-2},
\tag{7}
$$
其中 $n=1$ 的最后一项为零。准确初始项及递推是
$$
\begin{aligned}
E_{r,1}&=a-\mathcal H_r,\\
E_{r,2}&=aE_{r,1}-(r-\chi),\\
E_{r,n}&=aE_{r,n-1}-rE_{r,n-2}\quad(n\ge3).
\end{aligned}
\tag{8}
$$
第二行必须减 $r-\chi$，不能减 $r$。原因是将第二层的唯一上升点继续 trace 至 $H$ 时，该点已在 $H$，故出现 $[H_r:H]=r-\chi$；其后才出现每层的次数 $r$。

对 $c=\prod_r r^{n_r}$，定义
$$
E_c=\prod_{r\mid c}E_{r,n_r},\qquad
e_{r,n}=\operatorname{aug}(E_{r,n})
  =S_n-(1+\chi)S_{n-1}+\chi S_{n-2},\qquad
e_c=\prod_{r\mid c}e_{r,n_r}.
\tag{9}
$$
以上 $S_n$ 在每个 $r$ 都使用原 $a_r(E)$。

**定理 3.1（全来源的实际下降）。** 对兼容的原 CM 基点，精确有
$$
\boxed{\quad
\operatorname{Tr}_{H_c/H}P[c]=E_cP[1],\qquad
\Theta_c^{\max}=\bar E_c\Theta_1.
\quad}
\tag{10}
$$
**证明。** 单个素数的公式由 (5) 逐层取真实 trace 得 (8)，从而得 (7)。不同 conductor 素数的局部 isogeny 对应交换，且环类映射兼容，因此对互素 conductor 逐个应用 (5) 得乘积 (9)。点的证明使用原 $a_r$；有限来源的证明先在 CM 除子上使用 $T_r$，再应用原 $\varphi_{p,q}$。最后对全部 $\operatorname{Cl}(F)$ 标签求和，conductor 纤维给 (2)，Artin 逆号与 (4) 兼容。证毕。

一个任意给定的原闭路可能使 conductor-$c$ 基点与预先选定的 $x(c)$ 相差 $b\in\mathcal C_c$。此时 (10) 的右端完整乘 $[\rho_c(b)]$ 或其逆，随 (2) 的 Artin 约定确定。此相位是实际群元，不能先删掉其一次项；但它是群环单位，保持是否落入 $J^3$。也可直接以该闭路的唯一逐层上升 CM 点作兼容 $x(1)$，此时 (10) 无额外相位。

## 4. 二阶 jet 的准确标量化

记 $I=\ker(\mathbb Z_p[C]\to\mathbb Z_p)$，其模 $p$ 像为 $J$。在 $\mathbb Z_p[C]$ 中，分歧 $\mathfrak r$ 的 $p$ 部分为一，因为它的阶整除二。因此非分裂素数的 $E_{r,n}$ 是标量。分裂素数则准确有
$$
E_{r,n}-e_{r,n}
=-S_{n-1}\bigl([\mathfrak r]+[\mathfrak r]^{-1}-2\bigr)
\in I^2.
\tag{11}
$$
因此 $\bar E_c-e_c\in J^2$。与 (3) 相乘，得到
$$
\boxed{\qquad
\Theta_c^{\max}\equiv\bar e_c\Theta_1\pmod{J^3}.
\qquad}
\tag{12}
$$
这在完整、可能非循环的 $p$ 类群上成立；没有用半单 Fourier。

若 $\psi:C\twoheadrightarrow C_p$，写 $T=\tau-1$，原完整来源的首三系数为 $(m_0,m_1,m_2)$。则
$$
m_0=0,\qquad
(m_{c,1},m_{c,2})=\bar e_c(m_1,m_2).
\tag{13}
$$
具体地，若 $\psi(\mathfrak r)=s_r$，则分裂项在 $T^2$ 的系数为 $-S_{n_r-1}s_r^2$。乘上原 $m_0=0$ 后它准确消失，不能将它单独当作额外非零二矩。

于是
$$
\begin{array}{ll}
p\nmid e_c:&
\Theta_c^{\max}\notin J^3\ \Longleftrightarrow\ \Theta_1\notin J^3,\\[2mm]
p\mid e_c:&
\Theta_c^{\max}\in J^3.
\end{array}
\tag{14}
$$
特别，完整 conductor 下降不会制造一个新的二阶最大阶来源。它准确保留或杀掉原来源，而非仅给一个单向估计。

## 5. 同一 Hilbert Heegner 点的全局 Kummer 等式

保留 R285 每个实际 Hilbert 商 $L_\psi/F$、norm-one variety $A_\psi$、完整格 $A_0=A_\psi(F)\otimes\mathbb Z_p$ 及
$$
\delta=\tau^{(p-1)/2}(\tau-1),\qquad
\delta^2=\tau+\tau^{-1}-2,\qquad
\mathcal O=\mathbb Z_p[\zeta_p].
$$
定义同一 conductor 来源的点
$$
Q_{c,\psi}=[t_F]\operatorname{Tr}_{H_c/L_\psi}P[c],\qquad
Q_\psi=Q_{1,\psi}.
\tag{15}
$$
全部 $p$-primary class norm 仍包含在 (15) 中。由 (10)，在原完整点格中准确有
$$
Q_{c,\psi}=E_{c,\psi}(\tau)Q_\psi\in A_0.
\tag{16}
$$
对任意整数 $s\ge1$，恒等式
$$
\tau^s+\tau^{-s}-2
=\delta^2\,\tau^{1-s}(1+\tau+\cdots+\tau^{s-1})^2
\tag{17}
$$
证明 $E_{c,\psi}\equiv e_c\pmod{\delta^2\mathcal O}$。因此在完整 $A_\psi[\delta^2]$ 上，$E_{c,\psi}$ 的实际作用为标量 $\bar e_c$，从 Kummer 函子的自然性得到
$$
\boxed{\quad
\kappa_{\delta^2,A_\psi}(Q_{c,\psi})
=\bar e_c\,\kappa_{\delta^2,A_\psi}(Q_\psi).
\quad}
\tag{18}
$$
这不是只在已知 MW 子空间上的配对等式。R285 的所有 $H^1$ 及局部通常 Selmer 条件均保留。

若 $p\nmid e_c$，$E_{c,\psi}$ 是 $\mathcal O$ 单位，所以两点的 $\delta^2$ 原始性等价。若 $p\mid e_c$，则 $p/\delta^2\in\mathcal O$，且 (16) 有明确的原全局除点
$$
\frac{Q_{c,\psi}}{\delta^2}
=\left(
 \frac{E_{c,\psi}-e_c}{\delta^2}
 +\frac{e_c}{p}\frac{p}{\delta^2}
 \right)Q_\psi\in A_0.
\tag{19}
$$
没有局部选根、改变 MW 格或忽略 Sha 的步骤。$\delta$ 在 $A_0$ 上单射，故这是唯一原除点。它解释 (14) 的第二行为何会让所有 admissible $q$ 的原两层观察同时消失。

## 6. 同一原 88 类的完整 conductor-$3$、$9$ 运输

这里只对 R296 已有的 $p=11,q=13,F=\mathbb Q(\sqrt{-6671})$ 验证新下降公式，不增加目标素数或搜索新样本。保留其全部 88 个原最大阶嵌入、原 level $389$ 点和 $C_{11}$ 标签。已知 $3$ 在 $F$ 分裂，$\psi(\mathfrak3)=5$，$a_3=-2$。

原四个 norm-$3$ isogeny 逐一作用后，每个最大阶点恰有两个水平点，真实标签差为 $5,-5$，另两个向下点给 conductor $3$。全部 176 个向下原嵌入互异，正好是 $h(\mathcal O_3)=176$；再对每点保留三个向下邻点，得到全部 $h(\mathcal O_9)=528$ 个原嵌入。每一节点保留其原 quaternionic 坐标、level 点、isogeny 和最大阶 Artin 标签。

若最大阶生成元为 $\eta$，$\operatorname{tr}\eta=1$、$\operatorname{N}\eta=1668$，则下一层使用 $3\eta-1$，再下一层使用 $9\eta-4$。相应原 $389$ 特征值为
$$
322,\qquad187,\qquad171.
$$
对每条真实 norm-$3$ 代表 $a$，向下嵌入准确为 $a\eta\bar a-1$，同时 level 线按 $a_{389}$ 运输。全纤维的原 $q$ 取向与每个 $389$ 特征线均直接核验；未把有限图节点重标记成任意类群元素。

在 $k[C_{11}]$ 中准确有
$$
E_{3,1}=-2-\tau^5-\tau^6,\qquad
E_{3,2}=-2E_{3,1}-2,
\tag{20}
$$
原全来源首三矩及其实际下降为
$$
\begin{array}{c|c|c|c}
\text{conductor}&\#\text{完整 CM 类}&e_{3,n}\pmod{11}&(m_0,m_1,m_2)\\\hline
1&88&1&(0,0,9)\\
3&176&7&(0,0,8)\\
9&528&6&(0,0,10).
\end{array}
\tag{21}
$$
证书逐系数比较全部 theta 元素与 $E_{3,n}\Theta_1$，而非只比较矩。若在 $n=2$ 错减 $3$ 而非 $2=3-\chi$，所得完整 theta 确实不同；此处不能省去初始 fibre 次数。

## 7. 对真实闭路路线的作用范围

R296 的原闭路最优阶可能是 $\mathcal O_c$。只要按 (2) 收齐其全部原环类轨道，并沿真实环类映射保留全部最大阶标签，(10) 已支付 conductor 下降及原 level 运输；无需假设 conductor fibre 次数与 $p$ 互素。若该完整来源的二阶 jet 非零，(14) 立即给原最大阶 jet 非零，再按 R281/R285 接回固定 E389。

但 (2) 的完整求和仍须实际完成。单个 $p$ 闭路的非零值不是 (2)，而 $e_c$ 的单位性也不控制其余 Hilbert coset 的和。更强地，(18) 说明改变 conductor 而只观察最大阶 Hilbert 商时，不会避开原 $Q_\psi$ 的 $\delta^2$ 原始性问题。后续非零工作应落在这个原完整类上，而不是把 conductor 的水平二次项当作新的低 jet。

## 证书与来源

- [check-full-ring-class-conductor-descent.py](../scripts/check-full-ring-class-conductor-descent.py) 及同名 JSON：17 项准确检验全部通过；保存同一原 176、528 类的完整稀疏运输，未保存大稠密矩阵。
- R276、R281、R285、R296：原 quaternionic 函数、CM 标签、整个通常 Selmer 及 Hilbert $\delta^2$ 接口。
- Henri Darmon, *Rational Points on Modular Elliptic Curves*, CBMS Regional Conference Series in Mathematics 101, AMS, 2004，Proposition 3.10：[作者全文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/36.NSF-CBMS/chapter.pdf)。本文第 2 节给出所用全部 CM fibre 与 norm 证明，第 3–5 节证明其在原完整来源及 Kummer 两层上的具体后果。
