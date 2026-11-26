# R146 补篇：原完整 high 压缩逆、有限列 Gram 与联合源

2026-11-26，visible-exact-astra-198c63d-20261126 / correlated_energy。

**已证明（纯解析）：** 以下给真正原 high97 压缩逆的一个完整乘子比较、
有限列的准确短接 Gram，以及无需验证有限逆的试探上界。没有运行新科学目标。
R146 actual 45765780668/1 已排除当前 CV/RA 非负费用预算；本篇不重开该预算，
也不宣称实际 PDE 可达迹、完整根型、全逆或课题完成。

## 1. 已付 high 下界保留为乘子，不压成最小值

记 $\mathcal H$ 为原归一 $L^2$ odd-fourfold scalar 空间，
$P=P_{1\le j\le96}$、$Q=1-P=P_{j\ge97}$。所有运算仍在同一真根、
同一 $Q_{\rm repair}$ 和实际全圈 frame；$P$ 不是新 cutoff。

[HP.1、HP.8–HP.12](R138-supplement-original-high-principal-and-signed-compact-bound.md)
逐项给出的型下界实际上是

$$
D_H\succeq Q M_aQ-\varepsilon I_{Q\mathcal H}
       =:D_b,\qquad b=a-\varepsilon.
\tag{JI.1}
$$

这里 $\varepsilon$ 是原 high actual
notes/original_high_root_lower_bound_ci/run-44750653724-1/
中四个已完成 upper 的和：

- principal_error_upper；
- signed_local_error_upper；
- mean_rank_error_upper；
- complete_primitive_error_upper。

各项先按原完整保存球读回，向上取界。原 actual 的正门证明
$a_{\min}-\varepsilon>0$，所以 $b(\phi)\ge b_->0$。
这仅使用负平方项的单侧界，**不**将 signed_local_error_upper 冒充整个
compact 算子范数或输出尾范数。$a$ 使用真实 even-fourfold principal；
若换人工轴参数，必须先按 F.9a 投影并另证整个参数域的 $b>0$。

因此 $D_H$、$D_b$ 均正且可逆，逆序关系为

$$
0<D_H^{-1}\preceq D_b^{-1}.
\tag{JI.2}
$$

不把 $D_H^{-1}$ 换成一个虚构的 pointwise 逆；下一节显式保留压缩。

## 2. 准确压缩逆与不必先算 high 投影的公式

令 $\beta=1/b$，并把 $P\mathcal H$ 与原96维空间识别。定义

$$
B=P M_\beta P,\qquad
\mathscr S_b=M_\beta-M_\beta P B^{-1}P M_\beta.
\tag{JI.3}
$$

由于 $0<b_-\le b\le b_+<\infty$，
$B\succeq b_+^{-1}I_P$，故这个有限逆在解析上存在。准确有

$$
P\mathscr S_b=\mathscr S_bP=0,\qquad
\mathscr S_b=Q D_b^{-1}Q.
\tag{JI.4}
$$

**证明。** 对 $f\in Q\mathcal H$，令
$y=\beta f-\beta P B^{-1}P(\beta f)$。于是 $Py=0$，而
$Q(by)=Q[f-PB^{-1}P(\beta f)]=f$。这证明 $y=D_b^{-1}f$。
(JI.3) 左右自伴，且在 $P\mathcal H$ 上为零，得到(JI.4)。证毕。

特别，$Q M_{1/b}Q$ 单独不是压缩逆；它漏掉原 low96 的完整校正。

## 3. 只有有限个输入列时，完整 high 费用就是有限 Gram

令 $F:\mathbb R^d\to\mathcal H$ 是任意**完整**有界列算子，
不要求其每列已投到 high。取

$$
U=P M_\beta F,\qquad G=F^*M_\beta F.
$$

由(JI.4)立刻得到

$$
\boxed{\quad
(QF)^*D_b^{-1}(QF)=G-U^*B^{-1}U=:G_{\rm short}.
\quad}
\tag{JI.5}
$$

例如 $F=KP$ 的原96列就给
$C^*D_H^{-1}C\preceq G_{\rm short}$；这里
$C=QKP$ 含原**全部** high。$F$ 的实际 mean rank 和两个非局部 primitive
必须来自同一完整 $K$，不能以理想角 ODE 或有限输出截断替代。

(JI.5)中的 $B,U,G$ 分别是96阶、96乘$d$、$d$阶的全角加权 Gram。
有限的是输入列数；角积分和乘子 $\beta$ 没有截掉任何 high。
若数值表示仍截 Fourier，仍必须支付其积分/表示尾，不能将“有限 Gram”
理解为任意有限网格本身精确。

它还有准确的变分形式

$$
v^*G_{\rm short}v
=\min_{x\in\mathbb R^{96}}
 \|\beta^{1/2}(Fv-Px)\|_2^2.
\tag{JI.6}
$$

极小点是 $x=B^{-1}Uv$。这既证明 $G_{\rm short}\succeq0$，
也证明把 $F$ 改成 $F+PT$ 不改变结果。因而无需先求每列完整 high
Fourier 投影；可直接使用其原全角函数并由同一个短接式自动消去 low。

## 4. 准确 dyadic 试探矩阵给完整上界，不需验证有限逆

对任意固定 $96\times d$ 矩阵 $X$，令

$$
G_X=(F-PX)^*M_\beta(F-PX)
    =G-U^*X-X^*U+X^*BX.
\tag{JI.7}
$$

由(JI.6)，或直接完成平方，

$$
\boxed{\quad
G_X-G_{\rm short}
 =(X-B^{-1}U)^*B(X-B^{-1}U)\succeq0,
\qquad
(QF)^*D_H^{-1}(QF)\preceq G_X.
\quad}
\tag{JI.8}
$$

一个浮点近似解只可用于选择随后**按准确 dyadic 固定**的 $X$。
最终证明完全消费全角 $(F-PX)$ 的完整 directed Gram；不把浮点逆当真逆，
不要求为得到这个 upper 另行验证 $B^{-1}$，也不靠不稳定差值猜正性。
所有原三项 signed96/97 条目仍只读，不因换积分表示而重算。

本式可实际降低未来完整有限费用的实现成本，但已被 R146 排掉的 CV/RA
不能据此重跑 Gram：其任何合法 $X$ 仍受原根必要下界约束。

## 5. 完整 root/source 的共同消元及准确的有限性范围

令 $\mathcal X$ 是原完整环境源 $h=\mathsf H$ 的
$H^{-1/3}_\phi$ 空间，含其真实 C4/reflection 资格和零模。
[U.8–U.14](R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md)
及 [F.1–F.2](R138-supplement-root-source-elimination-and-concave-finite-gate.md)
给出的真实相容式、mean 列与源 primitive 为

$$
\ell_h=\mathcal D^{-1}\langle h\rangle\cdot\ell,\qquad
V_h=I(h-g_m\ell_h),\qquad \mathcal D>17/20.
\tag{JI.9}
$$

这里 $I$ 是完整环境 $2\pi$ 圈 primitive，不改为 scalar 的 $1/4$ 界。
从 F.2 的准确有界交叉型定义 $L_L:\mathcal X\to P\mathcal H$、
$L_H:\mathcal X\to Q\mathcal H$，并从纯源型定义有界自伴 $Q_h$，
约定所有交叉都带系数2。于是完整归一根型准确写成

$$
\begin{split}
\widetilde{\mathcal B}_L/(2\pi)
={}&\langle A_Lz_L,z_L\rangle
 +2\langle Cz_L,z_H\rangle+\langle D_Hz_H,z_H\rangle\\
 &+2\langle L_Lh,z_L\rangle
 +2\langle L_Hh,z_H\rangle+\langle Q_hh,h\rangle.
\end{split}
\tag{JI.10}
$$

这些算子由 Riesz 表示定义于上述同一 Hilbert 空间。
其有界性由 F.3–F.7 和原 high actual 的完整源列界保证，不额外假设
$h$ 点态有界或为零。

置 $\xi=(z_L,h)$，
$\mathscr F\xi=Cz_L+L_Hh$，并记

$$
\mathscr A=
\begin{pmatrix}A_L&L_L\\L_L^*&Q_h\end{pmatrix}.
$$

直接对完整 $z_H$ 完成平方得到准确式与比较下界

$$
\inf_{z_H}\widetilde{\mathcal B}_L/(2\pi)
=\langle(\mathscr A-\mathscr F^*D_H^{-1}\mathscr F)\xi,\xi\rangle
\ge
\langle(\mathscr A-\mathscr F^*\mathscr S_b\mathscr F)\xi,\xi\rangle.
\tag{JI.11}
$$

不拆成分别最坏的 root/source 范数，也不付人为 $0<\vartheta<1$ 的 high
分配损失；所有 mean 和混合符号仍在。

**但 $\mathcal X$ 是无限维。** 对原完整 $h$，(JI.11)是完整算子恒等式，
不能仅因 $P$ 有96维就称其右侧是有限矩阵。只有原源在已证明的有限列中
因子化时，才可直接对联合 $F$ 使用第3节的有限 Gram。

若用一个有限正交源投影 $\Pi$，必须保留整个余项
$L_H(I-\Pi)h$。例如令

$$
u=Cz_L+L_H\Pi h,\qquad v=L_H(I-\Pi)h.
$$

对任意 $\tau>0$，

$$
\|\mathscr S_b^{1/2}(u+v)\|^2
\le(1+\tau)\|\mathscr S_b^{1/2}u\|^2
 +(1+\tau^{-1})b_-^{-1}\|L_H(I-\Pi)h\|_2^2.
\tag{JI.12}
$$

第一项可用(JI.7)的有限列 Gram；第二项须另用真实完整尾界。
没有新尾界时，原 actual 的
$2\|L_H\|\le C_{H,\mathrm{cross}}$
仍给一个合法但粗的完整上界。$\Pi$ 应保原完整 mean；
即便保了 mean，也不能免费删除其余非零源频率。

(JI.11)仍不包含 PDE 可达性。若要以源与根迹的相关性突破 R146 所排
非负费用格式，必须把同一真实输运和完整边界问题决定的 $h$ 一并接入；
任意选择 $h$ 或仅检查这个角 Gram 都不能授予实际齐次核排除。
当前实际可继续入口仍是正在运行的直接有限逆，以及其真实 high/mean/ν 接入。
