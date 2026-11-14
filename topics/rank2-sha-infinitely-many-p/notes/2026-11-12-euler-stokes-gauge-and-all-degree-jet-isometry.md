# Euler 中央 Stokes 规范与所有次数的实际 jet 等距

日期：2026-11-12。状态：本文的局部整格等距、初值限制、实际三维
闭包及复增长门槛均已证明。没有得到跨素数的中央非零，也没有得到
R151 尚缺的统一混合列 arithmeticity 上界。

本篇处理的是原固定 theta 截面的实际 Euler 原函数，不另造模型。
结论适用于全部截面次数和全部 jet 阶；它说明某个局部 Stokes 系数的
大小不能单独决定这些未标记图像的评价范数。全局固定初值仍须保留。

## 1. 固定对象和中央常数的整性

沿用 R62 的 $E_0:y^2=x^3-x$ 规范，令

$$
A(z)=z^4+O(z^8)\in\mathbb Q[[z^4]],\qquad
\mathscr H(z)=\int_0^z\frac{A(v)}v\,dv,
\qquad \mathscr H(0)=0.
\tag{1.1}
$$

固定参考为 $f_0(z)=\theta_T((4-i)z)$，其中 $T=(0,0)$，$f_0(0)=1$。
记

$$
w=z^4,\qquad H_4(w)=4\mathscr H(z),\qquad
Y(w)=\frac{4\mathscr H(z)}{f_0(z)},\qquad R_0(w)=\frac1{f_0(z)}.
\tag{1.2}
$$

$H_4\in\mathbb Q[[w]]$，而 $Y,R_0\in\mathbb Q(i)[[w]]$。
本篇所有 $k$ 均为 $w$ 阶；若改回自然 $z$ 阶，必须同步乘四。

固定惰性素数 $p\ge7$。设

$$
d=p+1=4r,\quad a=17c\in\mathbb Q_p,\quad v_p(a)=-1,
\quad E_0(z)=e^{-az^d},
$$
$$
G=E_0A,\qquad K=E_0\mathscr H,\qquad G_0=E_0f_0.
\tag{1.3}
$$

R54/R62 给 $G,G_0,G_0^{-1}$ 在同一较大闭盘解析，且 $G_0(0)=1$。
以下只需要这些正式恒等式及 R62 的完整分解

$$
K=\frac1d\sum_{j\in\{0,4,\ldots,d-4\}}\mathcal S_jE_{p,j}
       +\mathcal R_p,
\qquad E_{p,0}=E_0,
\qquad \mathcal S_0=-J_{A,p}'(0).
\tag{1.4}
$$

中央系数不仅有限，而且

$$
\boxed{\quad \mathcal S_0/d\in p\mathbb Z_p.\quad}
\tag{1.5}
$$

确实，写 $g_h=[z^{dh}]G$，已证 Gauss 界是

$$
v_p(a^{-h}g_h)\ge
\left\lceil\frac{h(p-1)+4}{2p}\right\rceil\ge1
\qquad(h\ge1).
$$

R62 的收敛式
$\mathcal S_0=\sum_{h\ge1}(-1)^h(h-1)!a^{-h}g_h$
遂属于 $p\mathbb Z_p$。又 $d=p+1$ 为单位，得到 (1.5)。
这个论证不假定 $J_{A,p}'(0)=0$。

## 2. 共同输出规范的精确作用

设 $B$ 为有限扩张 $\mathbb Q_p$，$\mathcal O$ 为其整数环。
对一组实际输出 $f_\nu(w)\in B[[w]]$，在源格 $\mathcal O^N$ 上令

$$
L_k=\left\{v\in\mathcal O^N:
 [w^j]\sum_\nu v_\nu f_\nu=0\ (0\le j<k)\right\}.
\tag{2.1}
$$

这就是先取 $B$ 上的核再与标准整格相交的饱和前缀格。
若所有输出同乘 $U(w)\in B[[w]]^\times$，且 $U(0)\in\mathcal O^\times$，
则每个 $L_k$ 不变，而第 $k$ 阶评价仅乘 $U(0)$。
因此每个 jet 评价范数准确不变。

证明只用
$$
\operatorname{ord}_w(UF)=\operatorname{ord}_wF,\qquad
[w^k](UF)=U(0)[w^k]F\quad\text{当 }\operatorname{ord}_wF\ge k.
$$
不要求 $U$ 的高阶系数整，也不要求它在原较大闭盘收敛。
这是对输出的共同乘法，不能替代对源截面格的检验。

## 3. 有理 Euler 平面的所有 $D,k$ 等距

在 $\mathbb P^2_\mathcal O$ 的仿射图中使用坐标 $(w,H_4)$。
$\mathcal O(D)$ 的标准格是次数至多 $D$ 的多项式格，列为

$$
w^aH_4^b,\qquad a+b\le D,
\qquad N_D=\binom{D+2}{2}.
\tag{3.1}
$$

对任意 $C\in\mathcal O$，令 $\mathscr H_C=\mathscr H+C$。
仿射平移

$$
(w,H_4)\longmapsto(w,H_4+4C)
\tag{3.2}
$$

是 $\mathbb P^2_\mathcal O$ 的射影线性自同构。在 (3.1) 上的矩阵为

$$
w^a(H_4+4C)^b
 =\sum_{j=0}^b\binom bj(4C)^{b-j}w^aH_4^j.
\tag{3.3}
$$

其对角为一，逆矩阵把 $C$ 换成 $-C$，故属于
$\mathrm{GL}_{N_D}(\mathcal O)$。于是对全部 $D,k$，两图像的饱和
前缀格由同一整可逆源变换识别，且

$$
\boxed{\quad
\|\varphi^k_D(H_4+4C)\|_p=\|\varphi^k_D(H_4)\|_p.
\quad}
\tag{3.4}
$$

这里包括冗余前缀行和评价为零的情形；不要求某个矩阵满秩。
直接源变换还保留每个前缀矩阵的所有阶子式理想。

源基点由 $(0,0)$ 变为 $(0,4C)$，两者都在同一整仿射图。
射影坐标 $X_0=1$ 的 $\mathcal O(D)$ 平凡化被 (3.2) 原样保持。
形式曲线的参数始终是 $w$，所以余切线基 $dw$ 及其第 $k$ 次张量也
原样保持。没有额外的基点范数、目标切线或 $D$ 次幂损失。

若需要在 Stokes 规范直接看这个矩阵，先把所有列同乘 $E_0^D$。
由 §2，实际列等距地变为

$$
w^a(4K)^bE_0^{D-b}.
\tag{3.5}
$$

$K\mapsto K+CE_0$ 时，其展开正是 (3.3) 在这些列中的同一矩阵。
即使 $E_0$ 的系数有分母，源矩阵仍只有整的二项式系数及 $4C$。

## 4. 局部消去中央模型不消去原中央导数

在 (1.4) 中选择

$$
C_p=-\mathcal S_0/d=J_{A,p}'(0)/d\in p\mathbb Z_p.
\tag{4.1}
$$

则 $K_{C_p}=K+C_pE_0$ 的 $E_0$ 系数为零，其他 $\mathcal S_j$ 及
较大盘余项不变。因而无须假定原中央导数消失，也能使这个**改变
初值之后**的中央投影在较大盘解析，同时保留 (3.4) 的全部范数。

准确变换律是

$$
\mathcal S_{0,C}=\mathcal S_0+dC,
\qquad \mathscr H_C(0)=C,
\qquad z\mathscr H_C'=A.
\tag{4.2}
$$

$J_{A,p}$ 由固定 $A$ 定义，故并未改变。R62 的
$\mathcal S_0=-J_{A,p}'(0)$ 使用了原初值 $\mathscr H(0)=0$；
对新初值必须使用 (4.2)，不能再次套用零初值公式。
若把 $\mathscr H_C$ 减去其在零点的值以恢复原规范，恰好回到
$\mathscr H$，被移去的 $E_0$ 项也恢复。

这只证明：通过允许整平移后的局部 Stokes 形状，不能单独获得
原图像 jet 范数的改善。它不排除同时使用固定 $\mathbb Q$ 初值、
固定全局整数 ODE 及各素数兼容性的论证。各 $C_p$ 目前只是分别定义
的局部数，不是一个已知全局代数常数；不能对它们直接使用乘积公式。

## 5. 原参考商必须增加一个真实坐标

对原平面 $(w,Y)$，变换是 $Y\mapsto Y+4CR_0$，并不是一般的平面
多项式源变换。因此不能把 (3.4) 直接宣称为原 $Y$ 平面的结论。

考虑具体的三维仿射 ambient

$$
(w,Y,R_0)\in\mathbb A^3_{\mathbb Q(i)},
\qquad (w,Y,R_0)(0)=(0,0,1).
\tag{5.1}
$$

在此 $Y\mapsto Y+4CR_0$、其余坐标不变，确为
$\mathbb P^3_\mathcal O$ 的整线性 shear。标准源列为

$$
w^aY^bR_0^c,\qquad a+b+c\le D,
\qquad N_D^{(3)}=\binom{D+3}{3}.
\tag{5.2}
$$

二项式展开把 $(a,b,c)$ 送到 $(a,j,c+b-j)$，总次数不变，矩阵仍为
整幺三角矩阵，逆用 $-C$。基点变成 $(0,4C,1)$，$X_0=1$ 和 $dw$
的平凡化均保持。因此 (5.2) 的全部饱和评价范数准确不变。

同乘 $G_0^D$ 后，(5.2) 等价于具体列

$$
\boxed{\quad
w^a(4K)^b E_0^cG_0^{D-b-c},\qquad a+b+c\le D.
\quad}
\tag{5.3}
$$

这给出保留参考的所有混合列和准确的整源变换。
它没有把 $E_0$ 或 $R_0$ 免费加入原平面格：新增的第三坐标确实
增加了源空间，下一节还证明本实际图像的闭包确为三维。

## 6. 实际三维闭包：参考零点轨道上的端点增长

**命题。** $f_0(z)$ 与 $\mathscr H(z)$ 在 $\mathbb C(w)$ 上代数独立。
因此 (5.1) 的 Zariski 闭包维数准确为三。

先用已经证明的实际商

$$
A/f_0=R_*\in\mathbb Q(i)(E_0),\qquad
\operatorname{Pole}(R_*)=[4-i]^{-1}(T)\setminus\{T\}.
\tag{6.1}
$$

右边十六点都是真简单极点，而 $f_0$ 在这些点有简单零点。
可选一个复对数 $z_0$，使
$f_0(z_0)=0$、$A(z_0)\ne0$。

设原方格周期为 $\Omega\mathbb Z[i]$、$\Omega>0$。取一个正实双周期
$L$，消去 theta 的有限半字符。方格的 CM 准周期关系及 Legendre
关系给 $\eta(\Omega)=\pi/\Omega>0$；于是

$$
f_0(z+L)=e^{17\eta(L)(z+L/2)}f_0(z),\qquad
A(z+L)=e^{17\eta(L)(z+L/2)}A(z).
\tag{6.2}
$$

第一式使用 $\eta((4-i)L)=(4+i)\eta(L)$，第二式也可由 (6.1)
的周期性直接得到。置

$$
\gamma=\frac{17\eta(L)}{2L}>0,\qquad
B(z)=e^{-\gamma z^2}A(z),\qquad z_n=z_0+nL.
\tag{6.3}
$$

$B$ 为 $L$-周期整函数。固定包含 $\operatorname{Im}z_0$ 的闭水平带；
其与一个周期条的交为紧集，故 $B,B'$ 在这个带上有统一界。
由 $\mathscr H'=A/z$，沿 $z_0$ 所在水平线分部积分，得到

$$
\mathscr H(z_n)
 =\frac{e^{\gamma z_n^2}B(z_0)}{2\gamma z_n^2}
       \bigl(1+O(n^{-1})\bigr).
\tag{6.4}
$$

为说明误差和基点常数：从一个固定充分大的正实部开始，

$$
\left(\frac{e^{\gamma z^2}B(z)}{2\gamma z^2}\right)'
 =\frac{e^{\gamma z^2}B(z)}z
  +e^{\gamma z^2}\left(\frac{B'(z)}{2\gamma z^2}
                         -\frac{B(z)}{\gamma z^3}\right).
$$

误差积分的绝对值至多
$O(e^{\gamma\operatorname{Re}(z_n^2)}/n^3)$，可由
$\int^x e^{\gamma t^2}t^{-2}dt=O(e^{\gamma x^2}x^{-3})$ 直接估计。
有限初段和 $\mathscr H$ 的基点值为固定常数，相对主项指数趋零。
又 $B(z_0)\ne0$，所以 (6.4) 给

$$
\log|\mathscr H(z_n)|=\gamma L^2n^2+O(n+\log n).
\tag{6.5}
$$

若存在非零 $P(w,X,Z)\in\mathbb C[w,X,Z]$ 使
$P(z^4,f_0(z),\mathscr H(z))=0$，先除去 $P$ 的最大公共 $X$ 因子。
则 $P(w,0,Z)$ 非零。对足够大的 $n$，其关于 $Z$ 的最高次系数在
$w=z_n^4$ 不为零（若它与 $Z$ 无关，已直接矛盾）。普通多项式根界
使其所有根至多按 $|z_n|$ 的某个固定幂增长。这与 (6.5) 矛盾。
故不存在这样的 $P$。因为
$R_0=1/f_0$、$\mathscr H=Y/(4R_0)$，三维结论随之成立。

这还证明 $H_4(w)$ 为非多项式整函数，两个平面图像 $(w,H_4)$、
$(w,Y)$ 的闭包均为二维。

## 7. 复增长、数域和截面次数的真实成本

固定 theta 截面 $A,f_0$ 在 $z$ 平面都是增长至多二阶的整函数。
(1.1) 的积分保持此上界。它们都在 $z\mapsto iz$ 下不变，故在
$w=z^4$ 平面下降为增长至多 $1/2$ 阶的整函数。
实际三维映射有无公共零点的齐次提升

$$
w\longmapsto[f_0(w):w f_0(w):4\mathscr H(w):1],
\tag{7.1}
$$

从而确实给 Herblot Definition 5.1 意义下的 $\rho\le1/2$ 一致化。
这里 $f_0(w),\mathscr H(w)$ 表示其四次商下降，不改原归一。

数域也不能省略。$(w,Y,R_0)$ 的数值基点虽为 $(0,0,1)$，其 germ
一般只在 $K=\mathbb Q(i)$ 上定义。为使用 Herblot 的闭点定理，取
$X=\mathbb P^3_K$ 并把它视为 $\mathbb Q$-scheme；其所选闭点的剩余域
才是 $K$，次数 $d_0=2$。不能把原 $\mathbb A^3_\mathbb Q$ 的那个有理
坐标点本身称为次数二的点。

在这个模型中，$K$ 上截面维数为 $\binom{D+3}{3}$，作为
$\mathbb Q$ 空间则再乘二。因此实际 Hilbert 维数尺度为 $D^3$，
相应一维 jet 比较在 $D\asymp k^{1/3}$ 的范围进行。
原平面是 $D^2$、$D\asymp\sqrt k$。新增坐标不能仍沿用原平面的
全部 $D,k$ 预算。

Herblot Definition 5.4 对每个闭点选择一个上方几何点，即一个
$K\hookrightarrow\mathbb C$ 嵌入；它不要求同一连通曲线同时穿过
全部共轭。算术定义仍保留全部共轭及数域次数。对这里的两个共轭，
$C_p\in\mathbb Q_p$、$a\in\mathbb Q_p$，所以 §3–5 的整矩阵分别成立；
$f_0$ 换成 $\bar f_0$ 不产生非单位成本。不能把它们免费另算为两个
有理点的贡献。

用该定理的 $1/(\alpha d_0)\le r\rho/(r-1)$，准确门槛为：

| 固定模型 | 闭点次数 | 实际闭包维数 | 源截面增长 | 严格代数化范围 |
|---|---:|---:|---:|---:|
| $(w,H_4)$，在 $\mathbb Q$ 上 | $1$ | $2$ | $D^2$ | $\alpha<1$ |
| $(w,Y)$，在上述 $K/\mathbb Q$ 模型 | $2$ | $2$ | $D^2$ | $\alpha<1/2$ |
| $(w,Y,R_0)$，在上述 $K/\mathbb Q$ 模型 | $2$ | $3$ | $D^3$ | $\alpha<2/3$ |

这些范围均指真正饱和评价映射的算术上界；本文没有证明其中任意一条
所需的上界。各模型已知非代数，所以若将来得到相应严格上界，才产生
矛盾。§3–5 的局部等距本身并未产生这种上界。

## 8. 留给混合列的准确任务

R151 的有限 Newton 行、联合全失败及所有混合列的对偶条件继续有效。
本篇把 Euler 路线的一项规范自由度完整付清：对未标记的 $H_4$ 平面，
或保留 $R_0$ 的实际三维格，局部移动常数能消去中央 $E_0$ 系数，
同时所有 $D,k$ 的范数不变。

因此后续若要借中央失败改善无界深带，必须使用同一个固定初值和
固定 ODE 的真正共同包络，不能只使用局部可选 Stokes 规范。
特别地，三维格的结论不反向宣称原 $Y$ 平面等距，也不把逐素数
平移后的 germs 当成一个新的全局代数 germ。

### 直接来源

- R54、R62、R151：同一 $A$ 的较大盘分解、中央 Stokes 和式及饱和
  jet 定义。本篇没有改变实际半因子的归一。
- [实际参考商和十六个简单极点](2026-11-12-actual-rational-reference-pure-logarithmic-form.md)，§1。
- [CM sigma 准周期](2026-11-12-cm-sigma-division-and-common-resonance.md)，§1；
  [NIST DLMF §23.2](https://dlmf.nist.gov/23.2) 的准周期及 Legendre 公式。
- M. Herblot，*Algebraic points on meromorphic curves*，Definition 2.5、
  5.1、5.4–5.5，Theorem 6.1，[原文](https://arxiv.org/abs/1204.6336)。
  本篇仅采用明确显示的增长/闭点不等式，不假定中央消失等于
  $p$-curvature 消失。
