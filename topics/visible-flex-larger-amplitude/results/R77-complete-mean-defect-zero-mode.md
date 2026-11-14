# R77：完整均值约束对候选 Darboux 缺陷零模的全角控制

作者：tail_refinement，GPT-6 Astra Pro，AI-assisted。日期：2026-11-12。

**已证明的条件工具。** 对一个满足真实完整连接均值方程的兼容高度候选，其 Darboux 缺陷的零模由全部非零模控制。下面的恒等式及上界逐真实半径成立，因此可以在已经覆盖整个径向区间的面板上使用。它不要求候选满足 Darboux 方程，也不以角采样、某个中心点或有限均值投影代替全角积分。

本结果是 [R75](R75-complete-mean-transport-and-shear-constraint.md) 的非线性候选推论。它不删除 R75 线性化公式中的 $\delta W\,\widehat R_K$ 项，不提供外侧 Green/Schur 逆，也不把候选变成已证明的精确外尾。

## 1. 对象、正分支和同一候选

取与 [R44](R44-compatible-outer-height-and-continuous-defect.md)、[R64](R64-general-outer-mean-and-compatible-defect.md) 相同的真实背景和正则性。令 $r,w>0$，$r_x>0$，$s=r_x/r$，$\ell=w_x/w$，$z=w^2$，$E=1+z$。在每个真实 source 图上，候选非均值高度及其导数定义

$$
P=\frac{h_\theta}{rw},\qquad K=\frac{h_r}{w}-1,
\qquad T=P_\theta,\quad U=K_\theta-P.
$$

这里 $K$ 包含通过真实完整标量方程选定的零模 $c(x)$。假定 R64 已证明其唯一正分支、径向可微性和全角分母条件。特别地，

$$
S=1-zP^2>0,\quad D=ES-z(1+K)^2>0,\quad
L=1+K+ET>0,
$$

且完整均值 $\mathcal M(P,K;x)=0$ 对整个区间恒成立。候选使用真实导数，所以兼容残差 $f_P=0$。记

$$
R_K=K_x+\ell(2K+T)-\mathcal N(P,K),\qquad J=L R_K.
\tag{77.1}
$$

$J$ 由同一候选的实际导数计算，不由重新解 PDE 来定义。在实际有限高度 $m=2,4,\ldots,40$ 的情形，完整 $J$ 是包含零模及全部 $m\le80$ 的有限 Fourier 多项式；$c,c_x$ 本身来自完整无限级数定义的均值，未被有限模替换。

## 2. 完整恒等式

**定理 77.1。** 在上述条件下，逐个真实 $x$ 有

$$
\langle J D^{-3/2}\rangle=0.
\tag{77.2}
$$

置 $J_0=\langle J\rangle$、$J_\perp=J-J_0$，以及 $d_0=\langle D\rangle$。对 $F(t)=t^{-3/2}$，有精确表达式

$$
\boxed{
J_0=-\frac{\langle (F(D)-F(d_0))J_\perp\rangle}
{\langle F(D)\rangle}.}
\tag{77.3}
$$

**证明。** R75.11 给出

$$
\mathcal M_x+2\ell\mathcal M
=\left\langle \frac{L}{D^{3/2}}(f_K-\alpha f_P)\right\rangle.
$$

在当前兼容候选上，左侧和 $f_P$ 均精确为零，$f_K=R_K$；代入 (77.1) 即得 (77.2)。将 $J=J_0+J_\perp$ 代入，利用 $\langle J_\perp\rangle=0$，可在非均值项内减去角度无关的 $F(d_0)$。正分支保证 $\langle F(D)\rangle>0$，得到 (77.3)。证毕。

式 (77.3) 不要求 $J=0$。它正是在候选存在真实残差时，把零模与其余残差连接起来的恒等式。

## 3. 连续全角上界和整数幂版本

设同一完整径向面板上已严格证明

$$
0<d_-\le D(x,\theta)\le e_+,\quad e_+\ge1,
\qquad \|D(x,\cdot)-d_0(x)\|_\infty\le q_D.
\tag{77.4}
$$

$d_0$ 也处于 $[d_-,e_+]$。在这个整个实区间上，$|F'(t)|\le(3/2)d_-^{-5/2}$。因此中值定理和 (77.3) 给

$$
|J_0(x)|\le C_D\,\|J_\perp(x,\cdot)\|_\infty,
\qquad
C_D=\frac32 e_+^{3/2}d_-^{-5/2}q_D.
\tag{77.5}
$$

这里分母使用了 $\langle F(D)\rangle\ge e_+^{-3/2}$。所有量都是整面板界，没有用点值替代 $x$ 或 $\theta$ 的上确界。

为了只进行精确有理运算，令 $d_* =\min(1,d_-)$。因为 $e_+\ge1$、$0<d_*\le1$，所以

$$
C_D\le \widehat C_D
:=\frac32\frac{e_+^2}{d_*^3}\,q_D.
\tag{77.6}
$$

这只把已证明的上界向上放宽，不改动均值方程。真实定义还自动给出

$$
D=E(1-zP^2)-z(1+K)^2\le E\le1+w_+^2,
\tag{77.7}
$$

故可取 $e_+=1+w_+^2$，其中 $w_+$ 是原面板的严格上端。

若没有单独保存 $D_\perp$，一个足够的输入是完整 Wiener 范数

$$
q_D\ge\|1-D\|_{W^1_\tau}.
\tag{77.8}
$$

因为非零 Fourier 系数的总绝对值不超过这个完整范数，(77.8) 蕴含 (77.4) 所需的 $\|D-\langle D\rangle\|_\infty$ 界。原 R64 代码中名为 `full_D_nonconstant_W1` 的字段事实上由完整 $z(2K+K^2+EP^2)=1-D$ 的代数范数构造，**包括其常数项**。这里只用这个已核实的更强语义，不从字段名字推断它已经丢掉常数项。

## 4. 与实际物理缺陷的统一单位

记 $\|J_\perp\|_{\ell^1}$ 为全部非零 Fourier 系数的总绝对值。则 (77.5)–(77.6) 给

$$
\|J\|_{\ell^1}\le(1+\widehat C_D)\|J_\perp\|_{\ell^1}.
\tag{77.9}
$$

对 R44 同一物理 Darboux 归一，转换因子为

$$
\mathfrak f(x)=\frac{w(x)^2}{r(x)r_x(x)E(x)^2}>0.
$$

若已存面板界 $B_\perp\ge\mathfrak f\|J_\perp\|_{\ell^1}$，则

$$
\mathfrak f |J_0|\le\widehat C_D B_\perp,
\qquad
\mathfrak f\|J\|_{\ell^1}\le(1+\widehat C_D)B_\perp.
\tag{77.10}
$$

可以同时保留原零模包围 $B_0$ 与原完整上界 $B_{\rm old}$，只在**同一个面板、同一个候选、同一个物理单位**上使用

$$
B_{\rm new}
=\min\{B_{\rm old},\ B_\perp+\min(B_0,\widehat C_D B_\perp)\}.
\tag{77.11}
$$

以上并未把保留频率外的 $J$ 丢掉：在有限高度应用中，$B_\perp$ 要包括 $2,4,\ldots,80$，其中 $42,\ldots,80$ 的完整二次贡献仍在。均值约束只控制 $m=0$。

## 5. 可重建的逐面板应用

独立工具 [tail_outer_mean_constraint_stream.py](../computations/tail_outer_mean_constraint_stream.py) 只使用 Python 标准库整数和 `Fraction`。它要求原连续计算正式退出零、原完整 stream-check 通过，并重新守卫真实候选输入、所有源 SHA、每个原径向叶、全部有符号有限频率和正分母余量。

工具逐叶读取原 $w$、$D$ 下界、完整 $1-D$ 范数及已付非零模物理上界，执行 (77.6) 与 (77.11)。所有运算为有理数，序列化最后才向上舍入为 48 位有效二进制 dyadic；任意小的非零量保留其指数。原主要记录不修改、不复制；新汇总保留输入 SHA、每子段的全叶数、最大值见证与完整重建命令的资源记录。

执行后的独立数值应用见同目录 `tail-r77-*` 笔记及其 manifest。本文的条件证明不依赖某个特定候选的点值或数值成功状态。外 $0,\ldots,11$ 的全频 Green/Schur 支付、参数化真内头接合、几何误差转移仍须分别完成。
