# 全输出角积分增益与宽领圈外端配对

2026-11-13，independent-audit。

**已证明：**第1–3节给完整非 Toeplitz 符号的角积分强界；第4节给准确自由 Airy 模型的最小紧支 gap；第5节给包含 regular 槽的真实外帽配对恒等式及保抵消比较界。实际有理预算已在 V8 中运行并通过30门。

**尚未完成：**新的宽领圈真实源符号 $C_0,C_2$、完整宽域误差及真实外帽参照形式 $M$ 还未付。本篇的自由模型下界不是实际 DN 或精确存在的反例。

## 1. 不删低输出的一阶角积分界

角坐标为 $x=4q\phi$，四重模以 $e^{ijx}$ 编号。采用相应正交归一基。
设 $X$ 为 Hilbert 空间，例如带正权的径向 $L^2$ 空间。令

$$
(Bu)(y,x)=\sum_{j\ne0} b_j(y,x)u_j e^{ijx},
$$

符号可依赖输入 $j$；不要求 Toeplitz。假设完整符号有

$$
\sup_{j\ne0}\|b_j\|_{L^2_yL^\infty_x}\le C_0,\qquad
\sup_{j\ne0}\|\partial_x^2b_j\|_{L^2_yL^\infty_x}\le C_2.
\tag{A.1}
$$

以一般 $X$ 代替 $L^2_y$ 时，取足以保证下列 Fourier 系数 $X$ 范数界的同样假设。二次角向积分分部给

$$
\|\widehat b_j(0)\|_X\le C_0,\qquad
\|\widehat b_j(l)\|_X\le C_2/l^2\quad(l\ne0).
\tag{A.2}
$$

逐 lag 的算子从 $\ell^2_j$ 到 $\ell^2_k(X)$ 的范数不超过对应上界，故

$$
\|B\|\le C_0+\frac{\pi^2}{3}C_2.
\tag{A.3}
$$

令 $\Pi$ 删去输出均值，$\Gamma e_j=4q|j|e_j$（$j\ne0$）。
在有限 Fourier 向量上

$$
\Gamma^{-1}\Pi B\Gamma=\Pi B+K,
$$

$$
K_{kj}=\frac{|j|-|k|}{|k|}\widehat b_j(k-j),
\qquad k\ne0,\quad j\ne0.
\tag{A.4}
$$

对 $k=j$，$K_{kj}=0$；其余由 $||j|-|k||\le|k-j|$ 得

$$
\|K_{kj}\|_X\le\frac{C_2}{|k|\,|k-j|}.
$$

因此 $K$ 是真正 Hilbert–Schmidt 算子，且

$$
\begin{split}
\|K\|^2
&\le\|K\|_{\rm HS}^2\\
&\le C_2^2\sum_{k\ne0}\frac1{k^2}
          \sum_{\substack{j\ne0\\j\ne k}}\frac1{(k-j)^2}\\
&\le C_2^2\left(\frac{\pi^2}{3}\right)^2.
\end{split}
\tag{A.5}
$$

结合(A.3)，通过稠密性得到完整强界

$$
\boxed{\;
\|\Gamma^{-1}\Pi B\Gamma\|
\le C_0+\frac{2\pi^2}{3}C_2
<C_0+\frac{20}{3}C_2 .
\;}
\tag{A.6}
$$

$\partial_\phi^{-1}$ 比 $\Gamma^{-1}$ 只多一个非零模上的酉符号因子，所以相同结论成立。特别地，$P_{\ge J}$ 表示输入 $|j|\ge J$，则

$$
\boxed{\;
\|\partial_\phi^{-1}\Pi B P_{\ge J}\|
\le\frac{C_0+(2\pi^2/3)C_2}{4qJ}.
\;}
\tag{A.7}
$$

这是完整输出算子界。所有 $0<|k|<J$ 和异号输出都包含在(A.5)中，没有把它们投影掉。它也是一个**输入右侧一整阶**的强界，而不只是逐列估计。若 $b_j$ 本身已按输入 $\Gamma^g$ 加权后满足(A.1)，同一证明给 $\partial_\phi^{-1}\Pi B\Gamma^{g+1}$ 的对应界。

用简单的 lag 绝对求和直接推(A.6)会多要三阶角导数；Hilbert–Schmidt 分解避免了这笔额外正则费用。

### 1.1 高输入上的进一步 Hilbert–Schmidt 衰减

不改变原空间。对整数 $j\ne0$，部分分式求和给准确等式

$
\sum_{\substack{k\ne0\\k\ne j}}\frac1{k^2(k-j)^2}
=\frac{2\pi^2}{3j^2}-\frac6{j^4}.
\tag{A.6a}
$

例如把被加数写成
$j^{-2}[k^{-2}+(j-k)^{-2}]+2j^{-3}[k^{-1}+(j-k)^{-1}]$，
先对对称有限范围求和再取极限；两个一阶分式的和已绝对收敛，
其总和为 $-2/j$，得到(A.6a)。

因此 $J>1$ 时(A.4)的真正高输入尾满足

$
\|K P_{\ge J}\|
\le \frac{2\pi C_2}{\sqrt{3(J-1)}}.
\tag{A.6b}
$

若另已知完整 $B$ 的算子范数 $B_0$，可以直接用

$
\boxed{\;
\|\partial_\phi^{-1}\Pi B P_{\ge J}\|
\le \frac{B_0+2\pi C_2/\sqrt{3(J-1)}}{4qJ}.
\;}
\tag{A.6c}
$

没有另一个 $B_0$ 时取(A.3)。这比在高输入上再次付完整(A.5)更紧，
但没有把低输出删除。实际有理报告另列这个改善后的全部费用。

## 2. 均值、实际费用和源空间

输出均值不能通过(A.7)丢掉。由(A.2)，$J>1$ 时

$$
\|\Pi_0 B P_{\ge J}\|
\le C_2\left(2\sum_{j=J}^\infty j^{-4}\right)^{1/2}
\le C_2\sqrt{\frac{2}{3(J-1)^3}}.
\tag{A.8}
$$

对于右乘 $\Gamma$ 的强档，另有

$$
\|\Pi_0 B\Gamma P_{\ge J}\|
\le4qC_2\sqrt{\frac{2}{J-1}}.
\tag{A.9}
$$

输入均值也是原有限槽，需按其真实列保留。R108 的 stream 根均值修正、完整 Fourier 尾以及相应 regular 标量 $\lambda=m/\sqrt q$ 全部照旧；(A.6)不改变这个归一。

从已经保存的 R99 同族实际报告读取

$$
9.72<q<10.
$$

该报告的小 UTF-8 摘要为 2026-11-12-ci-canonical-v1-scaled-Wiener-summary.json，SHA256
c0050bf6f15666f1b0283d7d232c10a167d08a4bb69e42c6cc5653dc51c94c3b；
实际频率原球逐字保存在新预算报告中。取 $J=K+1$ 并用 $2\pi^2/3<20/3$，完整向上费用为：

| $K$ | $C_0$ 系数上界 | $C_2$ 系数上界 |
|---:|---:|---:|
|64|.000395694841|.002637965601|
|128|.000199381122|.001329207474|
|256|.000100078462|.000667189744|
|512|.000050136774|.000334245155|
|1024|.000025092844|.000167285624|

再用(A.6c)和(A.3)，$K=256$ 时得到更紧的严格上界

$
.000100078462\,C_0+.000356434552\,C_2.
$

若已有独立的完整 $B_0$，相应费为

$
.000100078462\,B_0+.000022839680\,C_2.
$

实际报告保存更多有效数字及其准确有理端点。这个改善只来自已证明的完整矩阵尾，不是节点或截断矩阵估计。

相比 R108 使用的统一 $(4q)^{-1}$，这里保留了真实高输入尺度。这个表还不是新的 source 总数：必须先支付完整符号的 $C_0,C_2$，包括 cutoff、真实高度、所有 $E_{ij}$、无限 Fourier 尾及输入频率依赖。

若源中出现 $y^{-1/2}$，可以直接取 $X=L^2(dy/y)$，但必须先支付根可去性和该空间中的(A.1)。不能由未加权的 $L^2$ 值免费转授。

## 3. 四阶径向 spline 与二阶 canonical 角导

本节只给正则性层次，不替代实际导数上界。

当前真实物理 $F$ 在有限 collar 上为径向 $C^4$、逐 scalar span 光滑、角向光滑的同一函数。R37 的 fixed-type grounded 主矩阵使用 $F$ 的至多二阶径向导数及有界分母，故在分母门成立的有限域上：

- $B$ 为全局 $C^2$；
- 每个有限 span 的三阶径向及所需混合导数有界；
- 因二阶迹在 knots 连续，$B$ 的三阶弱导数没有 delta 项。

根匹配多项式高度 $\tau_*$ 与六阶有限坐标 $\Psi$ 是从同一 root span 中的真根系数定义的光滑函数。若已付 $J>0,\tau_*>0$，则

$$
V_*=-\frac{\tau_*}{J}\operatorname{div}(B\nabla\tau_*)
$$

在有限 collar 上具有两阶有界弱导数。经过真实光滑坐标变换，它在固定 canonical $y$ 的角向也属于 $W^{2,\infty}$。跨 scalar knots 时第一阶导数连续，因此二阶角弱导仍没有集中项。这正适配(A.6)只需要二阶角导的条件。

这里特意使用新多项式高度。若直接令 $\tau=A_{11}^{-1/2}$ 并把其高阶径向导数全部带进 $V$，不能沿用上述低阶论证。

本节不声称混合坐标中存在正解析或 direct-log 角宽。它也没有把有限区间上的分片值自动当作已经完成的全域导数预算；所有 span 上的实际界仍须计算和覆盖。

## 4. 当前宽度的准确自由 Airy benchmark

取准确自由密度 $C_0=\operatorname{diag}(1,y)$，$0\le y\le H$。
对一个正交归一的非零模，$\lambda=4q|j|$。
设 $A_0=\operatorname{Ai}(0)$、$m_0=-\operatorname{Ai}'(0)/A_0>0$、
$c=m_0^{-1/2}$。保留自由衰减解的两条根迹

$$
u_0=c\lambda^{-1/3}A_0,\qquad
p_0=c\lambda^{1/3}\operatorname{Ai}'(0)
=-\lambda^{2/3}m_0u_0 .
\tag{A.10}
$$

考虑所有在 $H$ 处可零延拓的 primal/dual 对：$v(0)=u_0$、
$v(H)=0$，$\operatorname{div}j=0$、$j_y(0)=p_0$、$j_y(H)=0$。
定义准确 gap

$$
\mathcal R^2=\int_0^H
 \left(|v_y-j_y|^2+
 y^{-1}|i\lambda yv-j_\phi|^2\right)dy.
$$

令 $f,g$ 为 $h''=zh$ 的两个基本解，

$$
f(0)=1,\ f'(0)=0,\qquad g(0)=0,\ g'(0)=1.
$$

置 $Z=H\lambda^{2/3}$。有限区间 Dirichlet 与 Neumann 的正 DN 数为

$$
m_D=\lambda^{2/3}\frac{f(Z)}{g(Z)},\qquad
m_N=\lambda^{2/3}\frac{f'(Z)}{g'(Z)}.
$$

Dirichlet 原理给最小 primal 能量 $m_D|u_0|^2$。
dual 原理或直接写 $j_y=w_y,\ j_\phi=i\lambda yw$ 给最小 dual 能量
$|p_0|^2/m_N$。两者的交叉项恒为 $2\operatorname{Re}(\bar u_0p_0)$。
因此准确下确界是

$$
\inf\mathcal R^2=
A_0^2\left[
 \frac{f(Z)}{m_0g(Z)}
 +m_0\frac{g'(Z)}{f'(Z)}-2\right].
\tag{A.11}
$$

端点为零的能量极小函数可用邻端短 cutoff 逼近，故同一个下确界适用于在端点邻域恒零的构造。这个补充仅为确定其紧性；下界本身直接适用于所有紧支对。

Wronskian 为 $fg'-f'g=1$。对(A.11)用算术—几何均值不等式，

$$
\boxed{\;
\inf\mathcal R^2
\ge2A_0^2\left(\sqrt{1+\frac1{g(Z)f'(Z)}}-1\right).
\;}
\tag{A.12}
$$

这避免了大指数下分别相减 $\operatorname{Ai}$ 与 $\operatorname{Bi}$。
$g,f'$ 的幂级数系数全正，故可在严格更大的 $Z_+$ 评价右侧下界。
使用已在 R109 paired-E 笔记中自证的 $A_0>7/20$，并取实际已付平图宽度
$H=7/2000=.0035$，对首高模 $j=K+1$ 真实有理计算得到：

| $K$ | 使用的 $Z_+$ | $\inf\mathcal R$ 严格下界 |
|---:|---:|---:|
|64|$2/3$|.65120897360172|
|128|$16/15$|.36445242541220|
|256|$5/3$|.16188720325294|
|512|$8/3$|.03599681938716|
|1024|$21/5$|.00210337448457|

每个 $Z_+$ 均实际检查 $H^3[40(K+1)]^2<Z_+^3$。
正幂级数保留40项，余项由之后递减的项比几何和支付；平方根使用整数开方得到有理上下界。没有调用浮点特殊函数。

**这只检查自由模型的这一紧支比较方式。** 它没有给当前实际 $C_*$ 的 gap 下界，也没有给实际 DN 或精确族的反例。它说明在 $y=.0035$ 处强制两槽都归零会付出显著代价；自由模型本身若继续采用真正衰减外解，则可有零 gap。下一接线应保留外端配对，而非只继续压小局部 $E$ 数值。

## 5. 真外帽的配对 Wronskian 与二次误差费

取一个真实外帽模块，从 collar 的外切口到既有 regular 端口，使用同一个 grounded form、真实非零模 Robin 和 regular 均值槽。其完整 trace 为

$$
h=(a,\xi),
$$

完整 dual 边界数据为 $g=(d,\lambda)$。$d$ 按该外帽的外法向定义；若 collar 向外的径向通量为 $p_H$，则 $d=-p_H$。

设完整 DN/Schur 形式为 $S\ge0$。常数联合迹可能构成其核；在准确常数商上运算，并要求 dual 数据满足相应总通量兼容。这个商只是全局常数规范，regular 槽和两端均值仍在 $h,g$ 中，没有删除。

取实际调和 primal $u_h$ 和同一形式下的最小能量 solenoidal dual $j_g$。
regular 非零模的 dual 能量为 $\langle\Gamma^{-1}p_R^\perp,p_R^\perp\rangle$。
完整 gap 中对应的 Robin mismatch 是
$\Gamma^{1/2}u_R^\perp+\Gamma^{-1/2}p_R^\perp$。
Green 恒等式消去这两个交叉项后，

$$
\boxed{\;
\mathcal R_{\rm ext}^2
=\langle Sh,h\rangle+\langle S^\dagger g,g\rangle
 -2\operatorname{Re}\langle h,g\rangle
=\|S^{-1/2}(Sh-g)\|^2 .
\;}
\tag{A.13}
$$

因此 collar 切口的交叉项准确为
$+2\operatorname{Re}\langle a,p_H\rangle$，
regular 交叉项仍是 $-2\operatorname{Re}(\bar\xi\lambda)$。
它与内部配对的切口项准确抵消。若分别粗估两块能量而先丢掉这个项，会损失真实 Wronskian 抵消。

设另有同一 trace 空间、同一核和正交归一的已付参照形式 $M$，并且

$$
(1-\epsilon)M\le S\le(1+\epsilon)M,\qquad 0\le\epsilon<1.
\tag{A.14}
$$

在能量完成空间写
$C=M^{-1/2}SM^{-1/2}=I+E$，$\|E\|\le\epsilon$，
$b=M^{1/2}h$、$d_0=M^{-1/2}g$。
则(A.13)给

$$
\boxed{\;
\mathcal R_{\rm ext}
\le\frac{\|b-d_0\|+\epsilon\|b\|}{\sqrt{1-\epsilon}}.
\;}
\tag{A.15}
$$

证明是
$Sh-g=M^{1/2}[(b-d_0)+Eb]$ 和 $C^{-1}\le(1-\epsilon)^{-1}I$。
相较把两个能量上界独立相加，这里以线性的 $\epsilon$ 支付配对误差，
而不是先形成一个 $\sqrt\epsilon$ 量级的 gap 费。

所有 height、Piola 与角测度变换必须先放进同一个 $h,g,M,S$。
从 canonical 平均角矩阵换到两个正交归一基时仍须使用 R103 的 $\sqrt q$ 因子；
不能把在另一个 frame 的 Wronskian 搬来。仅拥有某个压缩高体块的逆，也不满足(A.14)的完整外帽前提。

有限 strip 的 Dirichlet/Neumann 能量可给真实外帽 $S$ 的上下界，但 Neumann 的均值核、regular 及所有低高耦合必须保留。尚未计算这些真实全形式时，(A.15)是已证接口，不是已经完成的外帽数值。

## 6. 实际计算与范围

源码：scripts/fourfold_wide_stream_and_Airy_benchmark.mjs。

报告：notes/2026-11-13-wide-stream-and-Airy-benchmark.json。

全部30门由同源码的纯 BigInt 核实际运行。当前环境只允许该 V8 核；Node 文件入口没有运行，报告对此明确标记。源码保留原生入口，恢复后可直接重放。

本篇后续工作是实际支付宽 collar 完整符号及真实外端参照/匹配，不把自由模型 benchmark 或(A.7)的系数表冒称已得到完整强反馈逆。
