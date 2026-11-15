# R788：原 sigma 六秩核的跨 p Cartier 修正与第一 p 阶耦合

日期：2026-11-15。状态：**原有限修正式、准确秩六和全部 Schur 关系已证明。真正本原同标签的共同非零仍未证明。**

本篇将 R702 的原首 pole 块与 R784 的原六秩加法核结合。
所得约束包含同一个非零 Cartier 常数 $B$，并作用于两个原
第一 $p$ 阶 Taylor 多项式。它不是对任意 critical 向量成立的
形式左逆，但也尚不是所需非零定理。

## 1. 原多项式与有限环

固定
$$
p=6N+5\ge41,\qquad E_0:y^2=x^3-1,\qquad dz=dx/(2y),
$$
$$
\sigma(z)=z+O(z^7),\quad (\log\sigma)''=-x,\quad
F=x\sigma^6,\quad G=-xy\sigma^6.
\tag{788.1}
$$
仍用原规范
$$
B=(-1)^{N+1}\binom{3N+2}{2N+1}\in\mathbf F_p^\times,
\qquad \kappa=6B.
\tag{788.2}
$$
令
$$
\begin{aligned}
P(z)&=\sum_{m=0}^{p-1}[z^m]F\,z^m
=z^4\sum_{i=0}^{N}f_i z^{6i},\\
Q(z)&=\sum_{m=0}^{p-1}[z^m]G\,z^m
=z\sum_{j=0}^{N}g_j z^{6j}.
\end{aligned}
\tag{788.3}
$$
此处 $f_i,g_j$ 是原有理 Taylor 系数，随后才模 $p$ 约化。
R760 证明这些系数均整；$P$ 的次数至多 $p-1$，$Q$ 的次数至多
$p-4$。本篇较 R770 的 critical 截断各多保留指标 $N$，
没有将 $f_{N+1},g_{N+1}$ 当成整系数。

采用两个有限自由环
$$
R_{\mathbf Z_p}=\mathbf Z_p[z,t]/(z^p,t^p),\qquad
R_p=\mathbf F_p[z,t]/(z^p,t^p).
\tag{788.4}
$$
每个保留下来的单项总次数至多 $2p-2$。下文所有跨 $p$ 除法
均先在 $R_{\mathbf Z_p}$ 中证明整除性，再约化。

## 2. 完整跨 p 修正式

定义显式多项式
$$
\boxed{
\Phi_p(z,t)=
-2\kappa
\sum_{\substack{2\le r\le p-1\\r\ {\rm even}}}
\frac{z^{p+1-r}t^r}{r(r-1)}
\quad\in R_p.}
\tag{788.5}
$$
所有显示分母均为模 $p$ 单位。$\Phi_p$ 的总次数为 $p+1$，
在 $R_p$ 中 $\Phi_p^2=0$。

**定理 788.1。** 原核在这个有限环中的准确约化为
$$
\boxed{
F(z+t)G(z-t)
=(1+\Phi_p(z,t))P(z+t)Q(z-t)
\quad\text{于 }R_p.}
\tag{788.6}
$$
左侧先由原六秩核取各变量次数小于 $p$ 的整系数，再约化；
下面也直接证明这一约化的合法性。右侧是两个原整多项式与
显示的 Cartier 修正，不含未知高阶有限部。

### 2.1 原高块只有所需的一阶 pole

R702 (702.15) 在原普通坐标中证明
$$
pF(z)\equiv-\kappa z^{p+1}F_0(z),\qquad
pG(z)\equiv-\kappa z^{p+1}G_0(z)
\pmod{p,z^{2p}},
\tag{788.7}
$$
且 $F_0,G_0$ 整并与 $F,G$ 在所需低阶相同。
取 $\widetilde\kappa\in\mathbf Z_p^\times$ 为 $\kappa$ 的任一提升。
在次数小于 $2p$ 的有限范围中，可写
$$
\begin{aligned}
F(z)&=P(z)-\frac{\widetilde\kappa}{p}z^{p+1}P(z)+R_F(z),\\
G(z)&=Q(z)-\frac{\widetilde\kappa}{p}z^{p+1}Q(z)+R_G(z),
\end{aligned}
\tag{788.8}
$$
其中 $R_F,R_G$ 的保留系数均在 $\mathbf Z_p$ 中。
这里等式理解为模 $z^{2p}$；(788.7) 保证每个被吸入
$R_F,R_G$ 的高系数确实整，而非只假定有一个形式剩余项。
由原 $\mu_6$ 权与 (788.3)，
$$
\operatorname{ord}R_F\ge p+5,\qquad
\operatorname{ord}R_G\ge p+2.
\tag{788.9}
$$
如果某个剩余项为零，相应不等式自然成立。

### 2.2 全部被删乘积的次数与整性

把 (788.8) 分别代入 $z+t,z-t$。在 $R_{\mathbf Z_p}$ 中：

1. 两个 pole 因子相乘，其最低总次数为
   $(p+5)+(p+2)=2p+7>2p-2$，完全在保留范围外。
2. 任一 pole 与另一因子的高整剩余项相乘，同样最低总次数
   至少 $2p+7$。所以不会出现“整剩余项乘 $1/p$ 后仍影响内部”
   的遗漏。
3. 两个高整剩余项相乘也在该范围外。
4. 单个高整项乘另一低多项式虽可能保留总次数，但它的每个
   $(z\pm t)^m$ 均有 $m\ge p$。模 $p$ 后
   $(z\pm t)^p=z^p\pm t^p$，因此属于理想 $(z^p,t^p)$；
   因其系数已整，这一步才可以直接删去。

原次数至少 $2p$ 的项代入齐次线性式后仍有总次数至少 $2p$，
也不能进入有限方框。于是原核在 $R_{\mathbf Z_p}$ 中取模 $p$
只剩
$$
P(z+t)Q(z-t)
-\frac{\widetilde\kappa}{p}
\bigl((z+t)^{p+1}+(z-t)^{p+1}\bigr)
P(z+t)Q(z-t).
\tag{788.10}
$$

### 2.3 二项式分母在约化以前准确抵消

因为 $p+1$ 为偶数，
$$
(z+t)^{p+1}+(z-t)^{p+1}
=2\sum_{\substack{0\le r\le p+1\\r\ {\rm even}}}
\binom{p+1}{r}z^{p+1-r}t^r.
$$
$r=0,p+1$ 两个纯幂在 $R_{\mathbf Z_p}$ 中已经为零；
$r=1$ 和 $r=p$ 为奇数，在相加时准确抵消，不是将一个
不可除的端点系数强行除以 $p$。

剩余每个 $2\le r\le p-1$ 均满足
$$
\frac1p\binom{p+1}{r}
=\frac{p+1}{r(r-1)}\binom{p-1}{r-2}\in\mathbf Z_p.
\tag{788.11}
$$
对偶数 $r$，其约化是
$$
\frac1p\binom{p+1}{r}\equiv\frac1{r(r-1)}\pmod p,
\tag{788.12}
$$
因为 $\binom{p-1}{r-2}\equiv(-1)^{r-2}=1$。
所以 (788.10) 的除 $p$ 在有限自由环中合法，且其第二项正是
$\Phi_pP(z+t)Q(z-t)$。这证明 (788.6)。$\square$

特别，(788.6) 保留的只是原一阶 pole 残差；高块的未知整有限部
确实全部消失。不能先删去 $1/p$ 项，再把右侧错写成没有
$\Phi_p$ 的普通代换。

## 3. 原 p×p 系数矩阵的秩恰为六

定义
$$
M_{ab}=[z^at^b]\bigl((1+\Phi_p)P(z+t)Q(z-t)\bigr),
\qquad0\le a,b<p.
\tag{788.13}
$$
按 R784 的原六截面
$$
\begin{array}{lll}
S_0=-x^2y\sigma^{12},&S_1=-2y(x^3+2)\sigma^{12},
&S_2=3xy(x^3-4)\sigma^{12},\\
T_0=(x^3-4)^2\sigma^{12},&
T_1=x^2(x^3-4)\sigma^{12},&
T_2=x^4\sigma^{12},
\end{array}
\tag{788.14}
$$
有
$$
F(z+t)G(z-t)=
\sum_{\nu=0}^2\bigl(S_\nu(z)T_\nu(t)-T_\nu(z)S_\nu(t)\bigr).
\tag{788.15}
$$
每个截面次数小于 $p$ 的 Taylor 系数均整：
R784 的原 $u$ 表达只使用 $T^2,C,Z$ 至指标 $N$，
仍在 R760 已证范围内。因此 (788.15) 确可逐项约化为六个
长度 $p$ 向量的三个外积，给 $\operatorname{rank}M\le6$。

另一方面，原 $F=z^4+O(z^{10})$、$G=z+O(z^7)$，
而 $\Phi_p$ 的总次数为 $p+1$。
在行列指标 $0,\ldots,5$ 的 $6\times6$ 方块里，
唯一可能的总次数是五；下一个原总次数为十一，已超出该方块。
故这个原方块恰是 $(z+t)^4(z-t)$ 的反对角系数矩阵：
$$
A:=M_{\{0,\ldots,5\},\{0,\ldots,5\}}
=
\begin{pmatrix}
0&0&0&0&0&-1\\
0&0&0&0&-3&0\\
0&0&0&-2&0&0\\
0&0&2&0&0&0\\
0&3&0&0&0&0\\
1&0&0&0&0&0
\end{pmatrix},
\qquad \det A=36.
\tag{788.16}
$$
这些低阶常数分别也来自
$T_0=1+\cdots$、$S_2=-3z+\cdots$、
$T_1=z^2+\cdots$、$S_1=2z^3+\cdots$、
$T_2=z^4+\cdots$、$S_0=z^5+\cdots$。
所以它是原规范下的单位 minor，不是改基后任选的归一。
因此
$$
\boxed{\operatorname{rank}_{\mathbf F_p}M=6.}
\tag{788.17}
$$
同时 $M$ 为交错矩阵，且
$$
M_{ab}=0\quad\text{除非 }a+b\equiv5\pmod6.
\tag{788.18}
$$

## 4. 可直接使用的完整低块约束

令 $I=\{0,\ldots,5\}$。由 (788.16)–(788.17)，所有行列均满足
$$
\boxed{
M_{ab}=M_{aI}A^{-1}M_{Ib}\qquad(0\le a,b<p).
}
\tag{788.19}
$$
反之，如果 (788.13) 定义的矩阵满足 (788.19)，它的秩就是六，
因为 $A$ 本身已经可逆。因此这些 Schur 等式与准确秩六等价；
也可写成全部八阶主 Pfaffian 为零。

这里的 $M$ 每个元素都是两个原第一 $p$ 阶系数向量的双线性式，
并有 (788.5) 的明确 $\kappa=6B$ 项。
(788.19) 因而给出包含原 Cartier 单位的非线性耦合约束。
它并非对任意 $f_i,g_j$ 都成立；例如丢掉 $\Phi_p$ 就改变了这组
约束。另一方面，本篇也未证明 (788.19) 足以刻画原 sigma，
不将其任意形式解当作原对象。

### 4.1 未筛 critical 全零的一个必要后果

令 $d=p-6$，$a_i=f_i g_{N-1-i}$。因为
$\deg\Phi_p=p+1>d$，$M$ 的总次数 $d$ 部分恰是 R784 的
原 critical 矩阵。若假设
$$
a_i=0\quad(0\le i<N),
\tag{788.20}
$$
则其整个总次数 $d$ 齐次部分为零。

按 R784 的 $S_\nu=z^{r_\nu}A_\nu(z^6)$、
$T_\nu=z^{s_\nu}B_\nu(z^6)$ 记法，取该齐次部分的
$t^0,\ldots,t^5$，依次得到
$$
A_{0,N-1}=B_{2,N-1}=A_{1,N-1}
=B_{1,N-1}=A_{2,N-1}=B_{0,N-1}=0.
\tag{788.21}
$$
使用的低端乘数依次为 $1,3,1,-2,1,-1$，全为单位。
由于 (788.14) 的六个截面各占唯一的 $\mu_6$ 权，
(788.21) 进一步迫使
$$
\boxed{
M_{r,b}=0\quad
(p-11\le r\le p-6,\ 0\le b<p).
}
\tag{788.22}
$$
这是六个完整零行的必要条件。它尚未与 (788.19) 推出矛盾，
也不声称 (788.22) 反推 (788.20)。

## 5. 真本原单项问题须保留原筛

真正的非端点目标只要求在
$$
\mathcal S_p=
\left\{0\le i<N:
\gcd(6i+7,p+1)=1,\
P_{6i+6}(1/s)\ne0\right\},\qquad s^2=-3,
\tag{788.23}
$$
中有一个 $a_i\ne0$。这是
$P_{6a}(1/s)f_{a-1}g_{N-a}\ne0$ 的准确重编号。
这里 $P_r$ 是原 Legendre 多项式，与 (788.3) 的多项式 $P(z)$
仅按其带指标记号区分。

若目标失败，已知的只是 $a_i=0$ 对所有 $i\in\mathcal S_p$ 成立，
不能据此假定全部 $a_i$ 为零或使用 (788.22)。
可以把真实筛后的单项零条件直接与 (788.19) 联立；
也可以用 R784 的准确左逆，将每个这样的单项条件运输到
$M$ 的 degree $p-6$ 齐次部分。无论哪种写法，都不能用一个
可能相消的总和代替这些逐标签条件。

目前未证明该联立系统排除原数据上的所有筛后单项零，
也未得到强于 R734/R741 且足以保证交集的共同零计数。
端点 $h=1$ 仍由 R760 的独立两个系数保留。
因此原同标签三单位问题、真实高度排除和 Serre 完成标准均保持开放。

## 依赖

- [R697](R697-original-sigma-six-sections-and-integral-square-roots.md)：原两个 degree 六截面及普通导数规范。
- [R702](R702-first-pole-block-and-uniform-shifted-units.md)：原全部首 pole 块，特别 (702.15) 的有限范围与残差。
- [R760](R760-original-critical-sigma-jets-from-four-digit-division-data.md)：原指标至 $N$ 的整性及原标签。
- [R784](R784-original-full-sigma-kernel-and-primitive-preserving-left-inverse.md)：原三 wedge 完整核、六截面与筛的准确运输。
- [2026-11-15 降阶研究记录](../notes/2026-11-15-sigma-matrix-research.md)：十二阶单一源项及其未消高带，作为本篇转向完整方框的原因。

本篇是有限形式代数与整性证明；没有新增正式计算或有限素数扫描。

