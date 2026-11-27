# R12 附录：全部实际子商的正序交织方向与真实闭逆来源费

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

本稿继续[全部普通限制的本质正序障碍](R12-appendix-all-invariant-restrictions-essential-hyponormal-obstruction.md)留下的非可逆交织接口。新的结论不要求交织是相似或有下界：从实际 Haar 子商到 hyponormal 算子的任何有界交织都为零，反向的 cohyponormal 交织也全为零。相反方向有明确的迹类拟亲和；它的闭逆确实存在，却承担原四次来源费。各方向在下面分别证明。

## 1. 准确使用的原子商输入

令 $Q=M/N\ne0$ 是原 $A$ 的一个闭不变子商，也允许先作有限放大。用实际 Hilbert 商范数表示 $A_Q$。

[R140 §§1、6](R140-invariant-subquotient-type-and-fixed-first-regularization.md)已经证明
$$
\ker A_Q=\{0\},\qquad
\overline{\operatorname{Ran}A_Q}=Q,\qquad
r(A_Q)=0. \tag{1}
$$
这些结论来自原高阶多项式强近似单位，不能仅由全空间 $A$ 单射而推给商。本稿直接消费 (1)，不把它重新登记为新结果。

若 $f$ 是零点附近非恒定的解析芽，写
$$
f(z)-f(0)=z^r g(z),\qquad r\ge1,\quad g(0)\ne0,
$$
则
$$
B=f(A_Q)-f(0)I=A_Q^r g(A_Q) \tag{2}
$$
同样单射、值域稠密且拟幂零。因为 $g(A_Q)$ 有界可逆，前两项来自 (1)，第三项来自拟幂零算子的解析函数演算。这里包括 $B=A_Q$。

此外，R140 的原权界给
$$
\|B^n\|\le W_{rn}\|g(A_Q)\|^n,\qquad
-\log W_m\ge\frac{100}{15}m^4-105m^3. \tag{3}
$$

## 2. 一个自含的局部轨道引理

称有界算子 $S$ 为 hyponormal，若
$$
S^*S-SS^*\ge0,
$$
即 $\|S^*z\|\le\|Sz\|$ 对所有 $z$ 成立。则
$$
\|Sy\|^2
=\langle S^*Sy,y\rangle
\le\|S^*Sy\|\,\|y\|
\le\|S^2y\|\,\|y\|. \tag{4}
$$
对 $S^{n-1}y$ 使用 (4)，得到 $a_n=\|S^ny\|$ 的对数凸性
$$
a_n^2\le a_{n-1}a_{n+1}. \tag{5}
$$
如果 $Sy\ne0$，所有 $a_n$ 均非零，且相邻比值非减，所以
$$
\|S^ny\|\ge
\|y\|\left(\frac{\|Sy\|}{\|y\|}\right)^n.
\tag{6}
$$
因此
$$
\limsup_{n\to\infty}\|S^ny\|^{1/n}=0
\quad\Longrightarrow\quad Sy=0. \tag{7}
$$
这只使用同一个向量的实际轨道，没有用未知限制的谱分类。

## 3. 有界交织的两个完整零方向

**定理 3.1。** 设 $B$ 有界、拟幂零且值域稠密，$S$ 是任意 Hilbert 空间上的有界 hyponormal 算子。若有界 $X$ 满足
$$
SX=XB,
$$
则 $X=0$。

对任意 $x$，
$$
\|S^nXx\|\le\|X\|\,\|B^n\|\,\|x\|.
$$
右侧的 $n$ 次根趋零。由 (7)，$SXx=0$，故 $XB=0$。利用 $\operatorname{Ran}B$ 稠密和 $X$ 连续，得 $X=0$。

**定理 3.2。** 设 $B$ 有界、拟幂零且单射，$S$ 为 cohyponormal，即 $S^*$ hyponormal。若有界 $X$ 满足
$$
BX=XS,
$$
则 $X=0$。

取伴随，得到
$$
S^*X^*=X^*B^*.
$$
由 $\ker B=0$，$B^*$ 值域稠密；它仍拟幂零。定理 3.1 直接给 $X^*=0$。

于是对 (2) 的全部原实际子商，有准确方向表：

| 原方程 | 目标或来源的正序假设 | 结论 |
|---|---|---|
| $SX=XB$ | $S$ hyponormal | 每个有界 $X$ 都为零 |
| $BX=XS$ | $S$ cohyponormal | 每个有界 $X$ 都为零 |
| 任一方向 | $S$ normal | 每个有界 $X$ 都为零 |

有界次正规算子是 hyponormal：若 $S=N|_K$ 为正规算子的闭不变限制，则
$\|S^*y\|\le\|N^*y\|=\|Ny\|=\|Sy\|$。
故第一行也涵盖所有次正规目标。

这里不要求 $X$ 紧、单射、稠密像或属于原 Calkin 角；允许任意有界 $X$。加入标量也不改变结果，因为 $S-\lambda I$ 仍 hyponormal 或 cohyponormal。

定理不把“hyponormal 加一个紧算子”当作 hyponormal。对于这样的非可逆交织，(4) 一般不再可用，所以该更宽目标不能凭本稿关闭。

## 4. 相反方向确有显式迹类拟亲和

令 $B$ 为任意有界、单射、拟幂零算子，固定 $x\ne0$。记标准单边移位为
$$
Se_n=e_{n+1}\quad(n\ge0),
$$
并定义
$$
X_x:\ell^2(\mathbb N_0)\longrightarrow H_B,\qquad
X_xc=\sum_{n\ge0}c_nB^nx. \tag{8}
$$
拟幂零性给 $\sum_n\|B^n\|<\infty$，所以 (8) 是实际范数收敛的秩一算子和，且
$$
\|X_x\|_1\le\sum_{n\ge0}\|B^nx\|<\infty. \tag{9}
$$
由逐列恒等式并用有界性延拓，
$$
BX_x=X_xS. \tag{10}
$$

$X_x$ 单射。事实上若 $c\ne0$，则
$$
F(z)=\sum_{n\ge0}c_nz^n=z^mG(z),\qquad G(0)\ne0
$$
是单位圆盘中的非零解析函数。由于 $r(B)=0$，其在 $B$ 处的级数绝对收敛，$G(B)$ 有界可逆。因此
$$
X_xc=F(B)x=B^mG(B)x\ne0. \tag{11}
$$
这里并未把 $\|B\|<1$ 当作前提。

置
$$
C_x=\overline{\operatorname{span}}\{B^nx:n\ge0\}.
$$
有限支撑列给
$$
\overline{\operatorname{Ran}X_x}=C_x. \tag{12}
$$
所以把目标限制到这个实际闭循环子空间后，$X_x$ 是从单边移位到 $B|_{C_x}$ 的迹类拟亲和。

这一构造的方向与定理 3.1 相反。它表明不能交换两个方程中的算子而沿用零结论。对 $B^*$ 作同一列构造再取伴随，也给从实际 $B$ 到反向单边移位 $S^*$ 的非零迹类交织；该方向同样未被定理 3.2 排除。

## 5. 原 A 子商中，所有非零移位不变空间的像都稠密

现在专取 $B=A_Q$，且 $C_x$ 是上节同一个空间。由于 $C_x$ 是 $A_Q$ 的实际不变子空间，其在 $M$ 中的闭提升仍为原 $A$ 不变空间。R140 的 (1) 因而给
$$
\overline{BC_x}=C_x. \tag{13}
$$
这一步确实使用了原子商定理；一般单射拟幂零算子的循环限制未必满足 (13)。

令 $L\ne\{0\}$ 为 $\ell^2(\mathbb N_0)$ 的任意闭 $S$ 不变空间。不需要对 $L$ 作任何分类。选 $0\ne c\in L$，以上节的 $F(z)=z^mG(z)$ 记它的系数函数。所有多项式 $p$ 都满足 $p(S)c\in L$，而
$$
X_xp(S)c=p(B)F(B)x.
$$
在 $C_x$ 上，$G(B)$ 及其逆保持该空间，(13) 又给 $B^mC_x$ 稠密。因此
$$
\overline{\{p(B)F(B)x:p\in\mathbb C[z]\}}
=\overline{F(B)C_x}=C_x.
$$
于是
$$
\boxed{\overline{X_xL}=C_x\quad\text{对每个非零闭 }S\text{ 不变 }L.}
\tag{14}
$$

因此，此明确的迹类拟亲和没有将一个真移位不变空间推出一个更小的闭 $A_Q$ 不变空间。如果 $C_x$ 本身为真子空间，普通不变子空间已经由 $x$ 得到；本稿没有证明存在这样的 $x$。也没有声称 $X_xL$ 本身闭。

## 6. 闭逆确实交织，但必须承受实际四次费用

将 $X_x$ 视为从 $\ell^2$ 到 $C_x$ 的单射有界算子，取其实际逆
$$
Y_x=X_x^{-1},\qquad
D(Y_x)=\operatorname{Ran}X_x\subset C_x.
$$
$Y_x$ 稠密定义且闭，因为它的图是有界 $X_x$ 的闭图翻转。由 (10)，
$$
B D(Y_x)\subset D(Y_x),\qquad
Y_xB=SY_x\quad\text{于 }D(Y_x). \tag{15}
$$
这确实给出一个通向 hyponormal 单边移位的闭交织，未与定理 3.1 的有界结论矛盾。

对任意 $0\ne c\in\ell^2$ 及 $y=X_xc$，每个 $B^ny$ 都在这个同一实际域内，且
$$
\|Y_xB^ny\|=\|S^nc\|=\|c\|. \tag{16}
$$
若 $B$ 为 (2) 中的原解析子商，结合 (3)，得到
$$
\frac{\|Y_xB^ny\|}{\|B^ny\|}
\ge
\frac{\|c\|}{\|y\|}
\exp\left[
\frac{100}{15}r^4n^4-105r^3n^3
-n\log\|g(A_Q)\|
\right]. \tag{17}
$$
这是同一个实际来源序列的强制增长，不是通过更换向量获得的算子范数估计。

$C_x$ 无限维，因为它容纳单射 $X_x$；又 $X_x$ 紧，所以其逆不可能有界。式 (17) 给出了更具体的原权费用。故从这个闭逆寻求有界交织、可保持未知不变空间的分母或域核心时，仍须支付该费用，不能把闭性、稠密定义域或形式恒等式 (15) 当作已经完成的有界化。

本文关闭的是两个确定的有界正序交织方向，并给出相反方向的完整实际模型与原费用。普通 ISP、原未知 $C_x$ 的真性、其它紧扰动目标及真正特殊闭域仍保持开放。
