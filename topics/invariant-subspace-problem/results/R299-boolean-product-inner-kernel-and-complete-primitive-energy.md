# 逐位内函数的真实正核、primitive 源保持 Gauss 分解与完整平方能量

日期：2026-11-14（UTC）。作者：Astra-ISP-789f / literature_audit。

**状态：以下有限维恒等式及正核完整证明。** 它们保留全部正乘积权及物理内积，适用于所有出生。尚未从此正核提取硬端 $L_1A_U$ 所需的准确 Schur 块，因而本文不证明任何新的统一加强相邻常数。它与 R267 的幂零块 Blaschke 正则器不同：这里作用于每个物理位的自伴翻转，目标是同一个 primitive 源及相邻出生的共同正核。

## 1. 逐位规范与一个显式内函数

在每位有序正交基 $(e_0,e_1)$ 中，$e_0$ 为空位、$e_1$ 为占据位，定义

$$
E_i=|e_0\rangle\langle e_1|,
\quad E_i^*=|e_1\rangle\langle e_0|,
\quad n_i=E_i^*E_i=|e_1\rangle\langle e_1|,
\quad X_i=E_i+E_i^*.
$$

因此 $n_i$ 是**占据**投影；$X_i=X_i^*=X_i^{-1}$。不同位的全部算子交换。固定 $b_i>0$，写

$$
d=\sum_i b_iE_i,\qquad d^*=\sum_i b_iE_i^*,\qquad
p=\prod_i b_i,\qquad \mathfrak c=\prod_iX_i.
$$

对上半平面参数 $z$ 定义

$$
B_i(z)=\frac{zI-i b_iX_i}{z+i b_i},
\qquad
B(z)=B_M(z)\cdots B_1(z).                                  \tag{1.1}
$$

置 $P_i^+=(I+X_i)/2$。在 $P_i^+$ 上，$B_i$ 是标量函数 $(z-i b_i)/(z+i b_i)$；在 $I-P_i^+$ 上则恒为 $1$。若 $\operatorname{Im}z>0$，前者模不超过一；分母的零点在下半平面。因此 $B_i$ 与 $B$ 都解析且收缩。对实数 $x$，每个 $B_i(x)$ 酉，故 $B(x)$ 酉。$z=0$ 也没有极点，且

$$
B(0)=(-1)^M\mathfrak c,\qquad B(\infty)=I.                  \tag{1.2}
$$

这些性质在此只用了两个特征值的直接计算，无需引用一般内函数定理。

## 2. 同一物理空间上的完整正核

对 $\operatorname{Im}z,\operatorname{Im}w>0$，令

$$
\mathscr K(z,w)=
\frac{I-B(w)^*B(z)}{-i(z-\overline w)}.                       \tag{2.1}
$$

单个因子的直接分式运算给

$$
\frac{I-B_i(w)^*B_i(z)}{-i(z-\overline w)}
=\frac{2b_i}{(\overline w-i b_i)(z+i b_i)}P_i^+.              \tag{2.2}
$$

记 $B_{<i}=B_{i-1}\cdots B_1$，$B_{<1}=I$，并定义实际物理映射

$$
F_i(z)=\frac{\sqrt{2b_i}}{z+i b_i}P_i^+B_{<i}(z).
$$

逐项消去乘积的相邻项便得

$$
\boxed{\mathscr K(z,w)=\sum_{i=1}^M F_i(w)^*F_i(z).}         \tag{2.3}
$$

从而任取有限多个上半平面点 $z_a$ 及同一物理空间中的向量 $v_a$，

$$
\sum_{a,b}\langle v_b,\mathscr K(z_a,z_b)v_a\rangle
=\sum_i\left\|\sum_aF_i(z_a)v_a\right\|^2\ge0.              \tag{2.4}
$$

特别可以在同一式中使用不同 primitive 出生的源；它们的交叉项由共同的 $F_i$ 给出，未换成若干独立单出生不等式。式 (2.3) 还允许对参数作有限阶导数，再取相应真正的联合 Gram；任何这种操作都须保留完整非交换源次序。

## 3. 源保持的 Gauss 分解：顺序与占据约定

对 $z\ne0$，在上述 $(e_0,e_1)$ 基上直接有

$$
\frac1{z+i b_i}
\begin{pmatrix}z&-i b_i\\-i b_i&z\end{pmatrix}
=
\begin{pmatrix}1&0\\-i b_i/z&1\end{pmatrix}
\begin{pmatrix}
z/(z+i b_i)&0\\
0&(z^2+b_i^2)/(z(z+i b_i))
\end{pmatrix}
\begin{pmatrix}1&-i b_i/z\\0&1\end{pmatrix}.                 \tag{3.1}
$$

将不同位的因子交换到一起，得到

$$
\boxed{
B(z)=\exp(-i d^*/z)\,
\alpha(z)D(z)\,
\exp(-i d/z),
}                                                            \tag{3.2}
$$

其中

$$
\alpha(z)=\frac{z^M}{\prod_i(z+i b_i)},
\qquad
D(z)=\prod_i\left(I+\frac{b_i^2}{z^2}n_i\right)
=\prod_i(1+b_i^2/z^2)^{n_i}.                                 \tag{3.3}
$$

右端指数最先作用：它是删除指数 $\exp(-i d/z)$；左端才是创建指数。不能交换这两个指数与中间占据因子。式 (3.3) 的幂投影记号只是 $I-n_i+(1+b_i^2/z^2)n_i$，不需要选复对数。

若 $f\in K_s(b)=\ker d\cap\mathcal H_s$，则 $\exp(-i d/z)f=f$，故

$$
\boxed{B(z)f=\alpha(z)\exp(-i d^*/z)D(z)f.}                 \tag{3.4}
$$

因此这个源在全部参数上都不会出现次数低于 $s$ 的物理分量。准确的第 $s+j$ 层是

$$
P_{s+j}B(z)f
=\alpha(z)\frac{(-i/z)^j}{j!}(d^*)^jD(z)f,
\qquad0\le j\le M-s.                                       \tag{3.5}
$$

虽然 (3.2) 的单独因子在 $z=0$ 有极点，左侧 (1.1) 无极点；下节给出在同一源上直接可见的全部多项式消去。没有在 $z=0$ 单独取某个发散因子的值。

## 4. 完整边界平方恒等式

对任意实数 $t$，置

$$
D_t=\prod_i(I+t^2b_i^2n_i).
$$

由 (3.4)、(3.5)，取实 $x\ne0$、$t=x^{-1}$，利用 $B(x)$ 酉和物理次数层两两正交，得到

$$
\boxed{
\sum_{j=0}^{M-s}t^{2j}
\left\|\frac{(d^*)^j}{j!}D_t f\right\|^2
=\prod_i(1+t^2b_i^2)\,\|f\|^2,
\quad f\in K_s(b).
}                                                            \tag{4.1}
$$

这里 $|\alpha(x)|^2=\prod_i(1+b_i^2/x^2)^{-1}$，所以没有遗漏整体归一化。$t=0$ 由代入或连续性同样成立。

还有完全不含分母的直接证明。定义多项式向量

$$
\mathcal P_f(t)=\prod_i(I-i t b_iX_i)f.
$$

把 (3.1) 乘回标量分母，逐位再相乘即得

$$
\mathcal P_f(t)
=\exp(-i t d^*)D_t\exp(-i t d)f
=\exp(-i t d^*)D_t f.                                       \tag{4.2}
$$

每个因子满足

$$
(I-i t b_iX_i)^*(I-i t b_iX_i)=(1+t^2b_i^2)I
$$

且不同位交换，故 $\|\mathcal P_f(t)\|^2=\prod_i(1+t^2b_i^2)\|f\|^2$；按物理次数分解 (4.2) 就是 (4.1)。由极化，(4.1) 也是同一 $K_s$ 上的完整矩阵恒等式，而不只是逐个特选源的范数观察。

式 (4.1) 不是声称每个关于 $t$ 的系数都非负：一个范数多项式的中间系数仍可能包含交叉项。可直接使用的正性是整个平方和，以及更强的多参数联合 Gram (2.3)。

## 5. 无需极限交换的高次消去与硬端首尾系数

写

$$
D_t=\sum_{a=0}^s t^{2a}O_a,\qquad
O_a e_I=e_a((b_i^2)_{i\in I})e_I.
$$

左侧定义的 $\mathcal P_f$ 次数至多 $M$。其第 $s+j$ 个物理分量在 (4.2) 中是唯一的

$$
\frac{(-i)^j}{j!}\sum_a t^{j+2a}(d^*)^jO_af.
$$

于是所有超出总次数的系数都严格消失：

$$
\boxed{(d^*)^jO_af=0\quad\text{若 }j+2a>M.}                \tag{5.1}
$$

特别 $O_s=\operatorname{diag}(b_I^2)|_{\mathcal H_s}$；$a=s$ 恢复倒数权真顶层的消去。这里同时保留其余 $O_a$，未把整个创建源替成顶层的一项。

现在专取奇数硬端 $M=2r+1$、$r\ge1$、$u\in U=K_r(b)$。定义

$$
A=\sum_i b_i^{-1}E_i,\qquad
e=A^*=\sum_i b_i^{-1}E_i^*,\qquad A_U=A|_U.
$$

从多项式左侧逐项选择因子直接可读出

$$
[t^0]\mathcal P_u=u,\qquad
[t^1]\mathcal P_u=-i d^*u,\qquad
[t^M]\mathcal P_u=(-i)^M p\,\mathfrak c u,
$$

$$
\boxed{
[t^{M-1}]\mathcal P_u
=(-i)^{M-1}p\,\mathfrak c(A+e)u.
}                                                            \tag{5.2}
$$

由 [R297 实际硬端消逆](R297-appendix-odd-hard-top-innovation-and-dual-lowering-cancellation.md)，在硬端 $e|_U=\mathcal J_{1,r}$：因为 $[d,e]=I$ 于第 $r$ 层，$deu=u$，而中央完整 $d:\mathcal H_{r+1}\to\mathcal H_r$ 可逆，故这个预像就是完整最小逆。因此 (5.2) 的两个物理次数分量准确为

$$
P_r[t^{M-1}]\mathcal P_u
=(-i)^{M-1}p\,\mathfrak c\mathcal J_{1,r}u,
$$

$$
P_{r+2}[t^{M-1}]\mathcal P_u
=(-i)^{M-1}p\,\mathfrak c A_Uu.                              \tag{5.3}
$$

而低端的 $d^*u$ 保留 [R296 真实两带分解](R296-all-birth-residual-regression-two-band-lift-and-physical-innovation.md) 的两塔

$$
d^*u=\mathcal J_{1,r}C_1u-\mathcal J_{2,r-1}Bu,
\qquad B=\left.\sum_i b_i^3E_i\right|_U.
$$

因此原权、倒数权、真正第一 MP 和三次桥同时出现在同一个向量内函数的首尾系数中。

## 6. 尚缺的实际接口

硬端统一目标仍是

$$
A_U^*L_1L_3^{-1}L_1A_U\preceq\kappa I_U.
$$

上文已给共同正核、源保持的完整 Gauss 分解和实际首尾系数。它们还没有把 $L_1A_U$ 识别成 (2.3) 的某个已经计算的压缩块或 Schur 交叉块；尤其 (5.3) 只有 $A_U$，不能把所需的完整第一最小逆 $L_1$ 免费插入。后续若用边界参数的导数或 Schur 消元，必须显式证明所得源、完整逆次序、顶层 $L_3$ 度量正是上述目标。本文不以“内函数有正核”或“边界平方和成立”代替这一步。
