# 三条原 j=0 Euler 原函数：不同 Stokes 模与同 charge 组合的准确边界

日期：2026-11-14。状态：下述局部不相消结论已证明；它排除一种候选的整盘改善机制，不证明原中央非零，也不占 R555。本文由 R62 的完整 Stokes 分解继续，避免把同一个中央原函数公式换成 j=0 后重复登记。

## 1. 同一原来源，全部 Newton 尾

在共同 $E_1:y^2=x^3+1$、原微分 $dz=dx/(2y)$ 上，用 R301/R402/R469 已识别的三个固定来源
$$
A_{17}=S_{34},\qquad A_{36}=T_{72},\qquad A_{68}=U_{136}.
$$
下标是 $\Theta=x\sigma^2$ 的次数，不是 sigma 次数。每个实际来源都有首项 $z^6$，只含六的倍数次；没有另造同次数截面。

固定 $p>83$、$p\equiv5\bmod6$，记
$$
d=p+1,\quad c=[z^d]\log(\sigma/z),\quad \kappa_0=2c,\quad
a_m=m\kappa_0\quad(m=17,36,68),
$$
$$
R=p^{-1/(2p)},\qquad
S=p^{-p/(p^2-1)}<R.
\tag{1}
$$
这里 $v_p(c)=-1$ 是真实首分母，不能自由替换。原三个解析证明均支付
$$
G_m=A_m e^{-a_mz^d}\in K\langle z/R\rangle,\qquad
\|G_m\|_R\le R^6.
\tag{2}
$$
$K$ 是容纳原固定单位的有限 $p$ 进系数域，赋值以 $v_p(p)=1$ 归一。半径不在值群时可作有限扩张，或用同一加权 Tate 范数；结论不受此选择影响。

定义不随 $p$ 改变的 Euler 原函数以及其真正 regularization：
$$
H_m(z)=\int_0^z A_m(v)\frac{dv}{v},\qquad
K_m=e^{-a_mz^d}H_m.
\tag{3}
$$
它们先是形式恒等式；没有要求单独取出的指数在 $R$ 盘收敛。令 $D=z\partial_z$。准确方程是
$$
(D+a_md z^d)K_m=G_m.
\tag{4}
$$

原 Newton 系数 $a_{m,h}=a_m^{-h}[z^{dh}]G_m$ 满足
$$
v_p(a_{m,h})\ge
\left\lceil\frac{h(p-1)+6}{2p}\right\rceil.
\tag{5}
$$
所以 $J'_{m,p}(0)=\sum_{h\ge1}(-1)^{h-1}(h-1)!a_{m,h}$ 完整收敛。若其为零，则中央归一方程
$$
(X\partial_X+X)B_m=\sum_{h\ge1}a_{m,h}X^h,\qquad B_m(0)=0
$$
的系数满足准确尾表达
$$
b_{m,h}
=-\frac{(-1)^h}{h!}
 \sum_{i>h}(-1)^i(i-1)!a_{m,i},
\qquad
v_p(b_{m,h})\ge
\left\lceil\frac{(h+1)(p-1)+6}{2p}\right\rceil.
\tag{6}
$$
理由是 $(i-1)!/h!$ 在 $i>h$ 时整，且 (5) 的下界不减。这就是 R62 中央 Stokes 论证在当前原来源上的准确归一，并不是一条新的乘积零传播。

## 2. 每条原函数都有已付的非中央单位

按次数模 $d$ 分解。对 $j\in\{0,6,\ldots,d-6\}$，写
$$
g_{m,j,h}=[z^{dh+j}]G_m.
$$
对 $j>0$ 置 $x_j=j/d$，真实 shifted Newton 常数为
$$
\mathcal S_{m,j}
=\sum_{h\ge0}(-1)^h(x_j)_{\overline h}
a_m^{-h}g_{m,j,h}.
\tag{7}
$$
(2) 给
$$
v_p(a_m^{-h}g_{m,j,h})
\ge
\left\lceil\frac{h(p-1)+6-j}{2p}\right\rceil .
\tag{8}
$$
特别 $j=6$ 时，所有 $h\ge1$ 项都在 $p\mathcal O_K$，而 $g_{m,6,0}=1$。故
$$
\boxed{\mathcal S_{m,6}\equiv1\pmod p
\quad(m=17,36,68).}
\tag{9}
$$
这一行没有使用中央零或中央非零假设。

为明确闭尾而非只引用形式模型，R62 的逐余类递推在 (2) 下给
$$
K_m=\frac1d\sum_j\mathcal S_{m,j}E_{m,j}+\mathcal R_m,
\qquad
\mathcal R_m\in K\langle z/R\rangle,\quad
\|\mathcal R_m\|_R\le R^{p+5},
\tag{10}
$$
其中中央常数取 $\mathcal S_{m,0}=-J'_{m,p}(0)$，且
$$
E_{m,0}=e^{-a_mz^d},\qquad
E_{m,j}=z^j\sum_{h\ge0}
\frac{(-a_m)^hz^{dh}}{(x_j)_{\overline{h+1}}}\quad(j>0).
\tag{11}
$$
具体尾项在 $i>h$ 时，除去 $(x_j)_{\overline{h+1}}$ 后留下整乘积；其加权赋值至少 $(p+5)/(2p)$。$G_m$ 的加权系数趋于零给 (10) 的闭盘 Tate 衰减，不只给有界性。中央情形把该乘积换为 $(i-1)!/h!$，证明相同。

每个 (11) 的收敛半径恰是 $S$。对非中央模型，
$$
v_p((x_j)_{\overline{h+1}})
=\frac{h+1}{p-1}+O_p(\log(h+2))
$$
由逐 $p^e$ 计数得到，故 Cauchy–Hadamard 给所述半径。$j=6$ 在 $p>83$ 时不等于 $1,d-1$，沿 $h=p^n$ 还准确有
$$
v_p((x_6)_{\overline{p^n+1}})=\frac{p^n-1}{p-1}.
$$
因此其闭 $S$ 盘加权系数不会趋零。各 $j$ 支撑互不相交，(10) 的大盘尾不能抵消它们。由 (9)，每个 $K_m$ 的半径都准确为 $S$，不论三个原中央导数是否为零。

这一步的内容是原 R62 的实际三来源专门化。下节才是不同 charge 联合时额外需要的证明。

## 3. 在大盘亚纯域中三个坏类两两不同构

任取 $S<r\le R$，令
$$
\mathcal F_r=\operatorname{Frac}(K\langle z/r\rangle)
\subset K((z)).
$$
必要时先作有限系数扩张使 $r$ 在值群中；也可先取值群内的任意 $r$，这已足以判定是否有严格半径改善。$D$ 保持 $\mathcal F_r$。商
$$
\mathcal Q_r=K((z))/\mathcal F_r
$$
是一个带 Leibniz 导子的 $\mathcal F_r$ 向量空间。

首先 $K_m\notin\mathcal F_r$。否则将它写成闭盘亚纯函数。它在原点的形式展开正规，而在任何非零点，(4) 的最高极项来自导数，比乘法项的极高一阶，不能由解析的 $G_m$ 抵消。因此它在整个闭盘无极。Tate 代数的一元 Weierstrass 分解遂使它属于 $K\langle z/r\rangle$，与其准确半径 $S<r$ 矛盾。相同论证适用于后面的一阶齐次方程。

由 (4)，非零类 $v_m=[K_m]$ 满足
$$
Dv_m=-a_md z^d v_m.
\tag{12}
$$
所以 $L_m=\mathcal F_r v_m$ 是一个秩一简单微分模。

若 $L_m,L_n$ 同构，则某个 $f\in\mathcal F_r^\times$ 必满足
$$
Df=(a_m-a_n)d z^d f
$$
或其同时反号版本。在原点写 Laurent 展开；因为右侧系数恰从 $z^d$ 起，最低次强制 $f$ 的阶为零。特征零的逐项解因此唯一为
$$
f=f(0)\exp((a_m-a_n)z^d).
\tag{13}
$$
三个非零权差是 $19,51,32$；在 $p>83$ 时全为单位。所以
$$
v_p(a_m-a_n)=-1,
$$
(13) 的准确半径仍为 $S$。若它属于 $\mathcal F_r$，上面的无极论证又会使它在整个 $r$ 盘解析，矛盾。

故 $L_{17},L_{36},L_{68}$ 两两不同构。一族两两不同构的简单子微分模之和是直和：对有限族归纳，若最后一项与前面的直和有非零交，则它被包含其中；投到至少一个直和因子给非零微分模映射，从而给秩一同构，矛盾。因此
$$
\boxed{
L_{17}\oplus L_{36}\oplus L_{68}
\ \subset\ \mathcal Q_r.
}
\tag{14}
$$
这是同一形式域中的内部直和，不是增加自由来源。

由此得到准确的不相消结论：
$$
\boxed{
f_{17}K_{17}+f_{36}K_{36}+f_{68}K_{68}\in\mathcal F_r,
\quad f_m\in\mathcal F_r
\quad\Longrightarrow\quad
f_{17}=f_{36}=f_{68}=0.
}
\tag{15}
$$
系数甚至可依赖 $p$；只要它们确实属于这个大盘亚纯域，结论就成立。

## 4. 乘回同一 Gaussian degree 也不能消去坏块

原共同单位
$$
U_\Theta=\Theta e^{-\kappa_0z^d}
$$
及其逆在 $R$ 盘解析。原角 $t=-1/x^3$ 也在此盘解析。因此每个有定义的非零有理角系数 $r_m(t)$ 属于 $\mathcal F_r$。

固定整数 $M\ge68$，考虑确切同 charge 组合
$$
\mathcal H_M
=\sum_{m\in\{17,36,68\}}
r_m(t)\Theta^{M-m}H_m.
\tag{16}
$$
它的完整 Gaussian degree 是 $M$，不能分别删错指数。真正 regularization 恰为
$$
e^{-M\kappa_0z^d}\mathcal H_M
=\sum_m r_m(t)U_\Theta^{M-m}K_m.
\tag{17}
$$
只要至少一个 $r_m$ 非零，(15) 使 (17) 不属于任何 $S<r\le R$ 的 $\mathcal F_r$。所以这类同 charge 线性组合不能得到严格超过 $S$ 的亚纯收敛半径。

这里同时保留真实角系数与真实 Gaussian。结论不把 (16) 称为新的算术来源，不给它中央零，也没有把原来源乘积的 Mellin 值写成乘积。

## 5. 对当前主线的影响

完整中央零仍准确改善各自的 $p$ 依赖中央投影，式 (6) 保全部 Newton 深度。R62 已说明不能因此改善整个单一固定原函数；(14)–(17) 进一步证明，三个已识别 j=0 来源的不同 Gaussian 也不能用大盘亚纯系数线性组合来互相消掉非中央坏块。

它不排除更高扩张、带实际代数关系的非线性构造，或直接使用 $p$ 依赖投影的整数格。但这些构造若要影响 R418 的真饱和 jet，仍须给它们同一来源上的完整局部预算。尤其不能因有三个完整中央零，就给全部 $S^uT^vU^w$ 的中央投影赋零。

本篇不修改原 $P_{134}/U_0$、首核、两条十三行 carry 或 R552 的实际仿射 forcing 商；它没有从局部来源饱和推物理像饱和。R555 继续保留给原实际类的非零或消失判定。
