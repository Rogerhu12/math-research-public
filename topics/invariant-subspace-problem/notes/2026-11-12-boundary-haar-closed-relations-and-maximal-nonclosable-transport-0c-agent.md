# 闭图传输附注：负整数边界与 Haar 模型的所有闭不变关系分裂

日期：2026-11-12（UTC）。作者：l2_moments。状态：完整证明；作为 R174 的加强附注，不另占结果编号。

本文把 R174 的“没有非零有界交织”加强到真实不变域上的全部可闭交织，并给出从边界循环子空间到 Haar 循环子空间的代数传输的准确图闭包。它不决定 R185/R188 中的边界像饱和问题，也不把边界核当成原 Haar 核。

## 1. 两个实际归一化幂极限

原 Haar 算子记为 $A$，负整数边界表示记为
$$
Be_0=0,\qquad Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1)
$$
作用于 $\mathcal H_-=\ell^2(\mathbb N_0)$。取
$$
d_j=\|A^{2^j}\|=\|B^{2^j}\|,\qquad
N_j^+=A^{2^j}/d_j,\qquad N_j^-=B^{2^j}/d_j.
$$
R174 所用的实际极限为
$$
N_j^+\ \xrightarrow{\rm WOT}\ \tfrac12 I_H,\qquad
N_j^-\ \xrightarrow{\rm SOT}\ 0.
\tag{1.1}
$$

第二式也可直接证明：$\|N_j^-\|=1$，而对每个固定有限支撑向量，$B^{2^j}$ 最终把它杀掉。由有限支撑向量稠密及一致范数界，得到强收敛。第一式是原 Haar 模型的实际高位归一化幂弱极限，不能移到边界表示后继续使用。

这两个极限保持于有限放大以及闭不变子商。准确说，令 $T$ 为 $A$ 或 $B$ 的某个固定有限放大，$\mathcal N\subseteq\mathcal M$ 为闭 $T$ 不变空间，并用
$$
\mathcal K=\mathcal M\ominus\mathcal N
$$
代表商 $\mathcal M/\mathcal N$。诱导算子 $T_{\mathcal Q}$ 满足
$$
p(T_{\mathcal Q})=P_{\mathcal K}p(T)|_{\mathcal K}
\tag{1.2}
$$
对每个多项式 $p$ 成立。这是商表示的乘法性质；也可由 $\mathcal N$ 不变逐幂证明。因此相应归一化幂在 Haar 子商上弱趋 $\tfrac12 I_{\mathcal K}$，在边界子商上强趋 $0$。

以下用 $T_-$、$T_+$ 分别表示任意这样取得的边界、Haar 限制或子商算子。零空间允许存在，结论仍成立。

## 2. 所有闭不变关系的分裂

**命题。** 若
$$
\mathcal L\subseteq\mathcal K_-\oplus\mathcal K_+
$$
是闭线性子空间，且
$$
(T_-\oplus T_+)\mathcal L\subseteq\mathcal L,
$$
则存在闭不变子空间 $\mathcal L_-\subseteq\mathcal K_-$、
$\mathcal L_+\subseteq\mathcal K_+$，使
$$
\boxed{\mathcal L=\mathcal L_-\oplus\mathcal L_+.}
\tag{2.1}
$$
特别，
$$
\boxed{
\operatorname{Lat}(T_-\oplus T_+)
=
\{\mathcal L_-\oplus\mathcal L_+:
\mathcal L_\pm\in\operatorname{Lat}T_\pm\}.
}
\tag{2.2}
$$

证明：由于 $\mathcal L$ 不变，每个归一化幂
$$
\frac{(T_-\oplus T_+)^{2^j}}{d_j}
$$
保持 $\mathcal L$。固定 $(x,y)\in\mathcal L$，(1.1)—(1.2) 给
$$
\frac{(T_-\oplus T_+)^{2^j}}{d_j}(x,y)
\rightharpoonup (0,y/2).
$$
闭线性子空间在弱拓扑下仍闭，因此 $(0,y)\in\mathcal L$。相减得
$(x,0)\in\mathcal L$。故 $\mathcal L$ 保持于两个坐标正交投影，并且
$$
\mathcal L_-=\{x:(x,0)\in\mathcal L\},\qquad
\mathcal L_+=\{y:(0,y)\in\mathcal L\}
$$
是闭线性子空间。原有不变性分别给其 $T_\pm$ 不变性，证明完成。

这里不需要坐标投影属于多项式代数的范数闭包；固定向量上的弱极限与闭线性关系已经足够。也不要求任何未知核上的归一化幂强收敛。

## 3. 没有非零可闭的真实域交织

设 $X:\operatorname{Dom}X\subseteq\mathcal K_-\to\mathcal K_+$ 为线性算子，假设
$$
T_-\operatorname{Dom}X\subseteq\operatorname{Dom}X,\qquad
XT_-x=T_+Xx\quad(x\in\operatorname{Dom}X).
\tag{3.1}
$$
这是包含真实域的交织关系，不只是有限形式系数恒等式。

若 $X$ 闭，则其图 $\mathcal G(X)$ 为第 2 节的闭不变关系。对任意
$(x,Xx)\in\mathcal G(X)$，(2.1) 给 $(0,Xx)\in\mathcal G(X)$。单值性迫
$Xx=0$。所以
$$
\boxed{X=0.}
\tag{3.2}
$$
此处没有要求 $\operatorname{Dom}X$ 稠密；当 $X$ 闭时，其零算子的域自然是闭不变子空间。

若 $X$ 仅可闭，由 $T_-\oplus T_+$ 有界，$\mathcal G(X)$ 的闭包仍然不变；可闭性保证这个闭包是一个单值算子的图。于是同一论证给 $\overline X=0$，从而 $X=0$。

反方向的算子
$$
Y:\operatorname{Dom}Y\subseteq\mathcal K_+\to\mathcal K_-
$$
也相同：把其图按边界、Haar 的次序写成
$\{(Yx,x):x\in\operatorname{Dom}Y\}$，应用坐标分裂即可。综上，
$$
\boxed{
\text{任一方向的真实域交织，只要可闭，就恒为零。}
}
\tag{3.3}
$$

这排除了通过一个非零闭无界交织把边界不变空间移到原 Haar 模型的办法。它不排除没有上述不变域关系的线性映射，也不排除一般非线性构造。

## 4. 代数循环传输的完整图闭包

对有界算子 $T$ 及向量 $x$，记
$$
\operatorname{cyc}_T(x)=
\overline{\{p(T)x:p\in\mathbb C[z]\}}.
$$

取 $g\in\mathcal H_-$，假设不存在非零多项式 $p$ 使 $p(B)g=0$。
任取 $h\in H$，则代数映射
$$
K_0:p(B)g\longmapsto p(A)h
\tag{4.1}
$$
在 $\mathbb C[B]g$ 上定义良好。其图
$$
\mathcal G_0=\{(p(B)g,p(A)h):p\in\mathbb C[z]\}
$$
对 $B\oplus A$ 不变。令
$$
\mathcal M_g=\operatorname{cyc}_B(g),\qquad
\mathcal M_h=\operatorname{cyc}_A(h).
$$
第 2 节给 $\overline{\mathcal G_0}$ 在
$\mathcal M_g\oplus\mathcal M_h$ 中分裂。因为两个坐标的投影分别包含
$\mathbb C[B]g$ 和 $\mathbb C[A]h$，其闭包分别是全部 $\mathcal M_g$、
$\mathcal M_h$，所以
$$
\boxed{
\overline{\mathcal G_0}
=\mathcal M_g\oplus\mathcal M_h.
}
\tag{4.2}
$$

也可直接先对 $(g,h)$ 应用归一化幂，得到
$(0,h/2)\in\overline{\mathcal G_0}$，再使用不变性、线性和闭性获得
$0\oplus\mathcal M_h$ 与 $\mathcal M_g\oplus0$。

若 $h\ne0$，(4.2) 不是任何单值算子的图，因而 $K_0$ 不可闭。更准确地，对每个 $y\in\mathcal M_h$，存在多项式序列 $p_n$，使
$$
p_n(B)g\longrightarrow0,\qquad p_n(A)h\longrightarrow y.
\tag{4.3}
$$
这是 Hilbert 直和中图闭包的序列刻画，不是声称有统一的多项式范数控制。

选择已经证明循环的 Haar 真空 $h=1$，便得到
$$
\boxed{
\overline{\mathcal G(K_0)}
=\operatorname{cyc}_B(g)\oplus H.
}
\tag{4.4}
$$
因此这种最直接的代数传输不只是“尚未证明有界”，其图闭包事实上具有最大的垂直部分 $H$。

## 5. 真实无限头边界向量满足无多项式湮灭条件

$B$ 拟幂零，且实际非零权给
$$
\ker B^r=\operatorname{span}(e_0,\ldots,e_{r-1}).
\tag{5.1}
$$
任意非零多项式可写为
$$
p(z)=z^r u(z),\qquad u(0)\ne0.
$$
由于 $\sigma(B)=\{0\}$，$u(B)$ 为有界可逆算子，并与 $B^r$ 交换。因此
$$
\ker p(B)=\ker B^r.
\tag{5.2}
$$
所以每个具有无限物理头支撑的边界向量都满足第 4 节的无多项式湮灭条件。

特别，R185/R188 构造的两种慢边界核 $M=\ker T_N$、
$M=\ker T_Y$ 都满足
$$
M\cap\ker B^r=\mathbb Ce_0\quad(r\ge1).
$$
故任意 $g\in M\setminus\mathbb Ce_0$ 必有无限头支撑，(4.2)—(4.4) 均适用。

## 6. 本附注没有补上的内部稠密性

R200 中
$$
N=\overline{BM},\qquad
N=M\ \Longleftrightarrow\
M\cap\operatorname{Ran}B\text{ 在 }M\text{ 中稠密}
$$
仍是边界模型内部的准确未决条件。第 2 节分裂的是边界与 Haar 的直和关系，不是两个同属边界模型的闭不变空间。因此本文不能用来证明或否定 $N=M$。

同样，(4.4) 说明一个具体代数图桥无法经闭包成为算子；它没有构造原 Haar 的非平凡不变子空间，也没有把边界慢核的存在传回原 Hilbert 不变子空间问题。
