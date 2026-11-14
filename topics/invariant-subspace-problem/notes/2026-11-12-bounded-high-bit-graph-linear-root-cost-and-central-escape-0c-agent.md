# 有界高位头图的线性根成本与逐位中央逃逸

日期：2026-11-12。状态：完整必要条件及精确图恒等式；不宣称排除慢分支核。

本稿从并发会话的有界高位头图出发，补上较强的实际范数估计，并把它与 R208、R212 的中央分解直接连接。使用 $\mathscr J_j$ 表示乘以第 $j$ 位 Walsh 符号的物理反射，使用 $G_j$ 表示 Walsh 头图，避免两个不同的 $J$ 混淆。

## 1. 实际设置与删除下界

沿用 R208：

$$
X=a_*I+\sum_{j\ge0}a_jV_j,\qquad
a\in\ell^2\setminus\ell^1,
\qquad Y=\phi(B_2),\qquad T=X-Y,
$$

$$
0\ne M=\ker T,\qquad M\perp CM.
\tag{1.1}
$$

$X,T$ 是其真实闭实现，$\phi$ 是零点邻域上的标量解析芽并用通常全纯演算代入。记

$$
g=\|a\|_2,\quad
\eta_* =\sup_j\eta_j<1,
\quad L_0=\|T^*|_M\|<\infty.
$$

$L_0$ 有界来自 R161 的通常伴随同域与有界自交换子；例如

$$
L_0\le \sqrt{\|Y\|^2+\|C_a\|}+\|Y\|.
\tag{1.2}
$$

令 $b_j$ 为第 $j$ 位 Walsh 删除，$n_j=b_j^*b_j$。R208 的完整域交换子是

$$
[b_j,T]
=a_j(I-2n_j+2b_j)+E_j,
\qquad \|E_j\|\le r_j,
\tag{1.3}
$$

其中可取

$$
r_j=\frac{36g\eta_{j-1}}{\sqrt{1-\eta_*^2}}
+16|a_j|\eta_j
+C_\phi(432g^2\eta_{j-1}+72|a_j|^2)
\quad(j\ge1).
\tag{1.4}
$$

$C_\phi$ 来自固定的真实全纯演算轮廓，不要求 Taylor 级数在 $\|B_2\|$ 处收敛。

对单位 $f\in M$，$b_jf\in\operatorname{Dom}T$，且

$$
\langle[b_j,T]f,f\rangle
=-\langle b_jf,T^*f\rangle.
$$

置 $s=\|b_jf\|\le1$，由 $\langle n_jf,f\rangle=s^2$ 得

$$
|a_j|-r_j
\le2|a_j|s^2+(2|a_j|+L_0)s
\le(4|a_j|+L_0)s.
$$

所以当分子为正时，真实删除下界为

$$
\boxed{\quad
\|b_jf\|\ge\beta_j\|f\|\quad(f\in M),
\qquad
\beta_j=\frac{(|a_j|-r_j)_+}{L_0+4|a_j|}.
\quad}
\tag{1.5}
$$

这里只对 $\beta_j>0$ 的位使用后续头图。该估计不声称 $b_jM\subset M$。

## 2. 有界真实头图的确切含义

固定满足 (1.5) 且 $\beta_j>0$ 的位 $j$。抽出该位，将其余位记为 $H^{\widehat j}$。在该位的 Walsh 基中，$b_j(u,v)=(v,0)$。第二坐标映射在 $M$ 上下方有界，故其像 $L_j\subset H^{\widehat j}$ 闭，且存在有界 $G_j:L_j\to H^{\widehat j}$ 使

$$
M=\{(G_jy,y):y\in L_j\},
\qquad
\|G_j\|\le\sqrt{\beta_j^{-2}-1}\le\beta_j^{-1}.
\tag{2.1}
$$

这里 $L_j$ 仍包括低于 $j$ 的有限放大因素，不能当成已经识别的整个尾空间。

令 $B=N_{j+1}$ 作用于 $H^{\widehat j}$，$t=\eta_j B$。实际 $N_j$ 的 Walsh 矩阵为

$$
N_j=\frac12
\begin{pmatrix}I+t&I-t\\-I+t&-I-t\end{pmatrix}.
\tag{2.2}
$$

由 $M$ 的 $B$ 不变性，$BL_j\subset L_j$ 且 $BG_j=G_jB$。由 $N_j$ 不变性，

$$
-\frac12[(I-t)G_j+(I+t)]y\in L_j.
$$

因此 $(I-t)G_jy\in L_j$。$\|t\|\le\eta_j<1$，其 Neumann 逆保持 $L_j$，故 $G_jL_j\subset L_j$。以下 $G_j$ 是 $L_j$ 上的有界算子。图的第一坐标方程给

$$
(G_j+I)^2=t(G_j-I)^2.
\tag{2.3}
$$

这里及以下把 $t$ 限制到 $L_j$；仍有 $\|t\|\le\eta_j$。

因为 $B|_{L_j}$ 拟幂零，(2.3) 的交换因子给 $r(G_j+I)=0$。所以 $\sigma(G_j)=\{-1\}$，$G_j-I$ 真正可逆。转回物理基，置

$$
R_j=(G_j+I)(G_j-I)^{-1}.
$$

则有真实图与根式

$$
M=\{(R_jz,z):z\in L_j\},
\qquad R_j^2=t=\eta_j B|_{L_j}.
\tag{2.4}
$$

映射 $F_jz=(R_jz,z)$ 满足

$$
N_jF_j=F_jR_j.
\tag{2.5}
$$

因而这个平方根来自实际 $N_j|_M$ 的有界相似，而不是形式除法。

## 3. 根范数只付一次 Walsh 图范数

由 $R_j^2=t$ 与 Cayley 变换，得到精确线性恒等式

$$
\boxed{\quad
R_j=-\frac12\big[(I-t)G_j+(I+t)\big].
\quad}
\tag{3.1}
$$

可以直接验证：把右侧乘以 $G_j-I$，使用 (2.3) 展开的二次式，结果恰为 $G_j+I$。也可以从

$$
G_j=-(I+t+2R_j)(I-t)^{-1}
\tag{3.2}
$$

读出 (3.1)。因此

$$
\frac{(1-\eta_j)\|G_j\|-(1+\eta_j)}2
\le\|R_j\|
\le\frac{(1+\eta_j)(\|G_j\|+1)}2
\le\frac{1+\eta_j}{\beta_j}.
\tag{3.3}
$$

最后一步只用 $0<\beta_j\le1$。这个估计不需要额外的 $\eta_j(1+\|G_j\|)^2<4$ 条件。

特别地，当 $\beta_j\ge c|a_j|$ 时，

$$
\|R_j\|=O(|a_j|^{-1}),
\tag{3.4}
$$

改进了经一般逆范数估计得到的 $O(|a_j|^{-2})$ 安全界。

## 4. 固定核向量迫使这些根的范数发散

固定 $0\ne f\in M$。因为 $b_j\to0$ 强，$d_j(f)=\|b_jf\|\to0$。在任何使用 (2.1) 的位上 $d_j(f)>0$，且 Walsh 两坐标正交给出

$$
\|G_j\|
\ge\frac{\sqrt{\|f\|^2-d_j(f)^2}}{d_j(f)}.
$$

所以由 (3.3)，

$$
\boxed{\quad
\|R_j\|\ge
\frac12\left[
(1-\eta_j)\sqrt{\frac{\|f\|^2}{d_j(f)^2}-1}
-(1+\eta_j)\right].
\quad}
\tag{4.1}
$$

特别地，沿任意趋于无穷的可用位列，

$$
\|R_j\|\longrightarrow\infty,
\qquad \|R_j^2\|\le\eta_j\longrightarrow0.
\tag{4.2}
$$

这是必要的强非正规性，没有矛盾：小的平方范数不控制根本身的范数。

该相似的条件数也有准确解释。由于 $R_j$ 拟幂零，它不能下方有界，故

$$
\|F_j\|=\sqrt{1+\|R_j\|^2},
\qquad \|F_j^{-1}\|=1.
\tag{4.3}
$$

因此 (2.5) 的相似条件数必发散。

令 $P_{j,0},P_{j,1}$ 为该物理位的两个正交柱投影。由 (2.4)，

$$
\|P_{j,0}|_M\|
=\frac{\|R_j\|}{\sqrt{1+\|R_j\|^2}}
\longrightarrow1,
\qquad \|P_{j,1}|_M\|=1.
\tag{4.4}
$$

这里取范数的核向量可以随 $j$ 变化。式 (4.4) 不提供一个共同向量，不给出多位柱的统一质量，也不控制固定低头右逆成本。

## 5. 物理反射交换子的准确图公式

把 $R=R_j$ 简记。因为 $R:L_j\to L_j$，$M$ 位于 $L_j\oplus L_j$，而物理反射 $\mathscr J_j=\operatorname{diag}(I,-I)$ 保持该空间。两个标准等距图参数为

$$
U=\binom RI(I+R^*R)^{-1/2},
\qquad
V=\binom I{-R^*}(I+RR^*)^{-1/2}.
$$

它们分别满射到 $M$ 和其在 $L_j\oplus L_j$ 中的正交补。于是

$$
V^*\mathscr J_jU
=2(I+RR^*)^{-1/2}R(I+R^*R)^{-1/2}
=2R(I+R^*R)^{-1}.
$$

图外的 $(L_j\oplus L_j)^\perp$ 不产生额外分量。因此，对原全空间正交投影 $P=P_M$，

$$
\boxed{\quad
\|[P,\mathscr J_j]\|
=\|(I-P)\mathscr J_jP\|
=\|2R_j(I+R_j^*R_j)^{-1}\|.
\quad}
\tag{5.1}
$$

令 $s_j=\|R_j\|$。正算子 $|R_j|$ 的谱包含其范数，连续演算给

$$
\|[P,\mathscr J_j]\|
\ge\frac{2s_j}{1+s_j^2}.
\tag{5.2}
$$

由 (4.2)，充分大的可用位满足 $s_j\ge1$。此时 (3.3) 给

$$
\boxed{\quad
\|[P,\mathscr J_j]\|
\ge s_j^{-1}
\ge\frac{\beta_j}{1+\eta_j}.
\quad}
\tag{5.3}
$$

本节全是 Hilbert 正交图计算，并不要求 $\widehat C L_j=L_j$，也不把 R208 的双线性反对称性转成通常反自伴性。

## 6. 对 R212 中央逃逸的逐位加强

采用 R212 的实际正交分解

$$
H=M\oplus K\oplus CM,
\qquad K=(M\oplus CM)^\perp,
$$

并记

$$
\kappa_j=\|P_K\mathscr J_jP_M\|,
\qquad e_j=\|P_{CM}\mathscr J_jP_M\|.
$$

R208 单位反射附录给

$$
e_j\le C_*\frac{\eta_{j-1}}{|a_j|}
\tag{6.1}
$$

在其全部充分大的可用位成立。两个输出空间正交，故

$$
\|[P_M,\mathscr J_j]\|
\le\sqrt{\kappa_j^2+e_j^2}.
$$

结合 (5.3)，得到点态必要条件

$$
\boxed{\quad
\kappa_j\ge
\left[\frac{\beta_j^2}{(1+\eta_j)^2}-e_j^2\right]_+^{1/2}
\ge\frac{\beta_j}{1+\eta_j}-e_j.
\quad}
\tag{6.2}
$$

最后一个较弱下界允许右侧为负。

这给出 R212 可和余项结论的另一种、逐位的证明。取

$$
\mathcal I=\{j\ge1:a_j\ne0,\ |a_j|\ge2^j\sqrt{\eta_{j-1}}\}.
\tag{6.3}
$$

补集满足

$$
\sum_{j\notin\mathcal I}|a_j|
\le\sum_{j\ge1}2^j\sqrt{\eta_{j-1}}<\infty
$$

（另加有限首位）。沿 $\mathcal I$ 趋于无穷，(1.4) 给 $r_j/|a_j|\to0$，故最终

$$
\beta_j\ge c_1|a_j|,
\qquad c_1=\frac1{2(L_0+4g)}>0.
$$

同时由 (6.1)、(6.3)，

$$
\frac{e_j}{|a_j|}\le C_*4^{-j}.
$$

因此存在 $j_0$，使所有 $j\in\mathcal I$、$j\ge j_0$ 满足

$$
\boxed{\quad
\kappa_j\ge c_2|a_j|,
\qquad c_2=\frac{c_1}{2(1+\eta_*)}>0.
\quad}
\tag{6.4}
$$

也就是说，在删去一个原系数绝对可和的位集后，中央逃逸有逐位的线性下界。特别地 $\sum_j\kappa_j=\infty$。对规范交替慢行 $a_j=(-1)^j(j+1)^{-\sigma}$、$1/2<\sigma\le1$，(6.4) 对所有充分大的 $j$ 成立。

该结论仍只是必要成本。它没有给中央压缩交换子中两个跨块项相对于 $a_j$ 的小量估计；R212 中央附录的精确抵消式仍须保留。

## 7. 全平面谱不迫中央广义核存在

一个实际一致性边界是：取交替慢行 $a_j=(-1)^j(j+1)^{-\sigma}$、$1/2<\sigma\le1$，原一阶 $X$ 由 R138 满足 $\sigma(X)=\mathbb C$，但 R125 给

$$
\ker(X-\lambda I)=0\qquad(\lambda\in\mathbb C),
$$

而 R172 的真实自然幂同样没有非零广义核。它仍具 $C$ 自伴、通常伴随同域、有界自交换子，以及固定共同正则器的最大图和原参数图核心。

因此，中央算子继承的这些接口与全平面谱，不能单独迫使新的零核出现。继续递归需要利用它确实由原非零核剥离所得的两个跨块算子，而不是仅重用上述抽象域和谱性质。

## 8. 依赖及未作的推断

本稿的真实输入为 R161、R208 的完整域及高位交换子、R212 的中央分解，以及并发会话已经给出的有界头图构造。为避免依赖未登记的简称，第 1–2 节重写了实际删除下界和图转化。

没有证明 $L_j$ 对尾共轭保持，没有在 $L_j$ 上自动建立 UHF 表示，没有从逐位柱质量推出多位联合柱质量，也没有把小的根平方范数视为根范数小。所有式子均发生在已经识别的有界图或真实闭域上。
