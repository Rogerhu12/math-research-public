# 共同 annihilator 不变空间上的仿射锐性：不能替代逐坐标平方零

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / boundary_core。

**状态。** 下述是一个完全显式的两模式、四层有限维反例。它表明：即使分级子空间对每一个 bosonic annihilator 都不变，而且所需的完整一阶、二阶下降均可逆，首边仍不具有与空间无关的有限常数。此例恰好饱和仿射下界，但不属于 Boolean 硬核空间；它不反驳任意正权 Boolean 首边猜想。它只准确划出 [仿射传输主稿](2026-11-14-bosonic-affine-gram-transfer-789f-next.md) 的一般适用范围，与该主稿的证明相容。

## 1. 两模式 Fock 空间与四个实际分级子空间

取两个 bosonic 模式，标准正交归一向量记作 $e_{r,k}$，其中 $r,k\ge0$，总粒子数为 $r+k$。令
$$
a_xe_{r,k}=\sqrt r\,e_{r-1,k},\qquad
a_ye_{r,k}=\sqrt k\,e_{r,k-1},
$$
并约定负指标向量为零。固定任意 $t>0$，记
$$
x=e_{1,0},\qquad y=e_{0,1},
$$
$$
u=e_{1,1}+t e_{0,2},\qquad
w=e_{2,0}+2t e_{1,1},
$$
$$
v=\sqrt2\,e_{2,1}+2t e_{1,2},
$$
$$
p=e_{3,0}-2\sqrt3\,t^2e_{1,2}-2\sqrt2\,t^3e_{0,3}.
$$
定义相互正交的实际分级子空间
$$
\mathcal M_0=\mathbb C e_{0,0},\qquad
\mathcal M_1=\operatorname{span}\{x,y\},
$$
$$
\mathcal M_2=\operatorname{span}\{u,w\},\qquad
\mathcal M_3=\operatorname{span}\{v,p\},
$$
以及 $\mathcal M_j=\{0\}$（$j\ge4$），令 $\mathcal M=\bigoplus_{j=0}^3\mathcal M_j$。这里使用从完整 Fock 空间继承的 Hilbert 范数；没有把 $u,w$ 或 $v,p$ 人为设为正交或单位向量。$u,w$ 线性无关，因为只有 $w$ 含 $e_{2,0}$；$v,p$ 线性无关，因为只有 $p$ 含 $e_{3,0}$。

## 2. 对两个 annihilator 的共同不变性

二、三层的全部八个导数为
$$
\begin{array}{c|cc}
 & a_x & a_y\\ \hline
u & y & x+\sqrt2\,t y\\
w & \sqrt2\,x+2t y & 2t x\\
v & 2u & \sqrt2\,w\\
p & \sqrt3\,(w-2t u) & -2\sqrt6\,t^2u.
\end{array}
\tag{2.1}
$$
例如
$$
a_xp=\sqrt3\,e_{2,0}-2\sqrt3\,t^2e_{0,2}
=\sqrt3\,(w-2t u),
$$
而
$$
a_yp=-2\sqrt6\,t^2e_{1,1}-2\sqrt6\,t^3e_{0,2}
=-2\sqrt6\,t^2u.
$$
第一层另有
$$
a_xx=e_{0,0},\quad a_xy=0,\quad
a_yx=0,\quad a_yy=e_{0,0},
$$
且两个 annihilator 都消灭 $\mathcal M_0$。因此
$$
a_x\mathcal M_j\subseteq\mathcal M_{j-1},\qquad
a_y\mathcal M_j\subseteq\mathcal M_{j-1}
$$
对全部 $j$ 成立。因而 $\mathcal M$ 对两个坐标导数及其任意线性组合共同不变，限制后的两个下降仍然交换。

完整 Fock 空间的 Euler 身份也准确保留：对 $z\in\mathcal M_j$，
$$
\|a_xz\|^2+\|a_yz\|^2=j\|z\|^2.
\tag{2.2}
$$
所以不能用“只对一个下降不变”或“丢失全部坐标 Euler 能量”来解释下文首边的失败。

## 3. 完整下降可逆与真正 primitive Gram

令实际下降为 $D=a_x|_{\mathcal M}$，固定出生 $s=1$。因为 $Dx=e_{0,0}$、$Dy=0$，
$$
K_1=\ker(D|_{\mathcal M_1})=\mathbb C y,qquad \|y\|=1.
$$
一阶完整映射 $D:\mathcal M_2\to\mathcal M_1$ 满足
$$
Du=y,\qquad Dw=\sqrt2\,x+2t y.
$$
在域基 $(u,w)$、值域基 $(y,x)$ 中其矩阵为
$$
\begin{pmatrix}1&2t\\0&\sqrt2\end{pmatrix},
$$
故可逆。这里矩阵只用于证明线性可逆，不用于计算 Hilbert 伴随。

第二归一完整映射 $D^2/2:\mathcal M_3\to\mathcal M_1$ 满足
$$
\frac{D^2}{2}v=y,\qquad
\frac{D^2}{2}p=\frac{\sqrt6}{2}x.
$$
在域基 $(v,p)$、值域基 $(y,x)$ 中它是可逆对角矩阵
$\operatorname{diag}(1,\sqrt6/2)$。事实上 $D:\mathcal M_3\to\mathcal M_2$ 本身也可逆，因为
$$
Dv=2u,\qquad Dp=-2\sqrt3\,t u+\sqrt3\,w.
$$
因此下面的最小逆均是先在**完整实际层**上取逆，再限制源到 $K_1$；没有先压缩 primitive 再求逆的歧义。

按归一幂约定
$$
\mathcal J_1=(D|_{\mathcal M_2})^\dagger|_{K_1},\qquad
\mathcal J_2=(D^2/2|_{\mathcal M_3})^\dagger|_{K_1},\qquad
\Gamma_j=\mathcal J_j^*\mathcal J_j,
$$
唯一预像准确给出
$$
\mathcal J_1y=u,\qquad \mathcal J_2y=v.
$$
于是，在单位源向量 $y$ 上，
$$
\boxed{\Gamma_1=1+t^2,\qquad \Gamma_2=2+4t^2.}
\tag{3.1}
$$
这里 $D$ 的单模式系数平方和为 $S=1$。

## 4. 仿射下界等号与首边无统一常数

由 (3.1)，
$$
\boxed{\Gamma_2=4\Gamma_1-2I.}
\tag{4.1}
$$
等价地，$X_1=\Gamma_1$、$X_2=\Gamma_2/2$ 满足
$X_2=I+2(X_1-I)$。所以 $r=1,n=2$ 的 bosonic 仿射传输，在对全部 annihilator 共同不变的有限分级空间类中已经取等号。

另一方面，真正相邻比是
$$
\Gamma_1\Gamma_2^{-1}\Gamma_1
=\frac{(1+t^2)^2}{2+4t^2}\,I_{K_1}.
\tag{4.2}
$$
它在 $t^2>1+\sqrt2$ 时大于 $I$，并且
$$
\frac{(1+t^2)^2}{2+4t^2}\sim\frac{t^2}{4}\longrightarrow\infty
\qquad(t\longrightarrow\infty).
$$
因此不存在一个与这类空间无关的有限常数 $C$，使全部共同 annihilator 不变空间都满足
$$
\Gamma_1\Gamma_2^{-1}\Gamma_1\preceq C I.
$$
反例同时满足完整一阶与二阶可逆，所以不能把失败归因于 Moore–Penrose 伪逆的非闭值域、部分源域、硬顶退化或某个非法逆。

## 5. 与实际 Boolean 硬核约束的边界

此例不满足逐坐标平方零。例如
$$
a_y^2u=\sqrt2\,t\,e_{0,0}\ne0
\qquad(t>0),
$$
且 $a_x^2w=\sqrt2\,e_{0,0}\ne0$。因此它不位于
$\ker a_x^2\cap\ker a_y^2$，不是两个 Boolean 位，也不能替换实际任意位数、任意正权的硬核空间。

在沿 $a_x$ 的 occupation 分解中，$u=|1\rangle y+t|0\rangle e_{0,2}$，而 $v$ 只有 occupation $2$ 和 $1$ 分量；其额外零-mode 联合能量为零。真正 Boolean 模型的联合约束还要求每个实际坐标满足 $a_i^2=0$。要从仿射传输推进一般首边，必须用到该逐坐标硬核结构或与它等价的额外精确关系；共同导数不变、全部 Euler 身份和合法完整最小逆本身不足以完成这一步。
