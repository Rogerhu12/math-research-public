# R12. 不使用有理基点的 Poincaré torsor 提升

**2026-11-12 后续加强：** [R14](R14-canonical-poincare-translation.md) 证明本构造中特殊的 Picard 类自动具有规范的有理 $d$ 次除根，因此额外将对应 $f$ 乘以 $d$ 并非必要；R14 亦解决好约化整数模型上平凡化的存在与同时归一化。本文原充分构造仍有效，涉及一般不可除性和好约化存在缺口的说明应以 R14 的精确结论为准。

日期：2026-11-12。会话：`serre-uniformity-astra/2026-11-12`。

**状态：已证明的代数构造。** 正次数有理除子可以替代有理基点：把对应乘以除子次数，再作一个确定的有理平移，可使曲线上拉回的 Poincaré 线丛在 $\mathbb Q$ 上平凡。

本结果不声称已完成整数模型上的提升、无方程线丛平凡化算法、全部局部 QC 计算，或随模曲线层一致排除非 CM 点。

## 1. 设定与结论

令 $X/\mathbb Q$ 是光滑射影几何连通曲线，亏格 $g\ge1$，
$$
J=\operatorname{Pic}^0_{X/\mathbb Q},\qquad J^\vee=\operatorname{Pic}^0_{J/\mathbb Q}.
$$
记 $\mathcal P$ 为 $J\times J^\vee$ 上沿两个零截面刚性化的 Poincaré 线丛，$\mathcal P^\times$ 为去掉零截面的总空间。

给定定义于 $\mathbb Q$ 的除子 $D$，次数为 $d>0$，令
$$
u=\iota_D:X\longrightarrow J,\qquad x\longmapsto[d\cdot x-D].
$$
任取几何点 $b\in X(\overline{\mathbb Q})$，记 $\iota_b(x)=[x-b]$。经典 Jacobian 自对偶性给出同构
$$
a=\iota_b^*:J^\vee\longrightarrow J.
\tag{1.1}
$$
下文证明它与 $b$ 无关，并定义于 $\mathbb Q$。定义 (1.1) 也固定了极化可能存在的符号约定。

设
$$
f\in\operatorname{Hom}_{\mathbb Q}(J,J^\vee),
\qquad
\mathcal L=(u,f\circ u)^*\mathcal P,
\qquad \deg\mathcal L=0.
\tag{1.2}
$$
记实际线丛 $\mathcal L$ 在 Picard scheme 中的类为 $\kappa\in J(\mathbb Q)$，并定义
$$
c=-a^{-1}(\kappa)\in J^\vee(\mathbb Q),
\qquad
h:J\longrightarrow J^\vee,\quad z\longmapsto d\,f(z)+c.
\tag{1.3}
$$
$h$ 是有理态射，通常不是群同态。

**定理。** 在上述设定下，
$$
\mathcal L'=(u,h\circ u)^*\mathcal P
$$
作为 $\mathbb Q$ 上的实际线丛平凡。因此存在定义于 $\mathbb Q$ 的提升
$$
\widetilde u:X\longrightarrow\mathcal P^\times
$$
使其在 $J\times J^\vee$ 上的投影为 $(u,h\circ u)$。所有这样的提升相差一个 $\mathbb Q^\times$ 标量；其几何纤维有限。

## 2. 自对偶同构与基点无关

经典自对偶性断言 $\iota_b^*$ 在 $\operatorname{Pic}^0$ 上为同构。可核对 Milne, *Jacobian Varieties*, 原载 *Arithmetic Geometry* (1986), Chapter VII, §6，Theorem 6.6、Lemma 6.9、Remark 6.10(c)；[作者修订版](https://jmilne.org/math/xnotes/JVs.pdf)保留原编号。这里只把自对偶性作为标准 Jacobian 理论输入。

若换成 $b'\in X(\overline{\mathbb Q})$，则
$$
\iota_{b'}=t_{[b-b']}\circ\iota_b.
$$
阿贝尔簇的平移在其 $\operatorname{Pic}^0$ 上作用恒等，故
$$
\iota_{b'}^*=\iota_b^*.
$$
这证明 $a$ 与几何基点无关。对每个 $\sigma\in G_{\mathbb Q}$，$\sigma(a)$ 是用几何基点 $\sigma b$ 定义的同一个同构，所以 $\sigma(a)=a$；由下降，$a$ 定义于 $\mathbb Q$。

在 $\overline{\mathbb Q}$ 上令 $e=[d\cdot b-D]$，则
$$
u=t_e\circ[d]\circ\iota_b.
$$
在 $\operatorname{Pic}^0(J)$ 上，平移拉回恒等，而 $[d]^*$ 是乘以 $d$。因此有 $\mathbb Q$ 同态恒等式
$$
u^*=d\,a:J^\vee\longrightarrow J.
\tag{2.1}
$$
这里的 (2.1) 是 Picard scheme 中类的恒等式；并没有选择 $\mathbb Q$ 上的点 $b$。

## 3. Poincaré 双线性消去 Picard 类

对于 $c\in J^\vee(\mathbb Q)$，记
$$
\mathcal P_c=\mathcal P|_{J\times\{c\}},
$$
它是实际定义于 $\mathbb Q$ 的线丛。Poincaré 丛在第二变量上的双线性及乘法性质给出实际线丛同构
$$
\begin{aligned}
\mathcal L'
&=(u,d f\circ u+c)^*\mathcal P\\
&\simeq (u,f\circ u)^*\mathcal P^{\otimes d}\otimes u^*\mathcal P_c\\
&=\mathcal L^{\otimes d}\otimes u^*\mathcal P_c.
\end{aligned}
\tag{3.1}
$$
这些同构定义于 $\mathbb Q$。因 $\mathcal P_c$ 代数等价于零，$\mathcal L'$ 也有次数零。由 (2.1)、(3.1)，它在 $J(\mathbb Q)$ 中的类等于
$$
[\mathcal L']=d\kappa+u^*(c)
 =d\kappa+d\,a(c)
 =d\kappa-d\kappa=0.
\tag{3.2}
$$

选择 $h=d f+c$ 而不是直接 $h=f+c$ 的原因在这里：后者会要求在 $J(\mathbb Q)$ 中求解 $d\,a(c)=-\kappa$，一般不能无条件除以 $d$。乘对应以 $d$ 后，$c=-a^{-1}\kappa$ 是自动存在的有理点。

## 4. 从零 Picard 类到真正的有理平凡化

无有理基点时，不应把所有 $J(\mathbb Q)$ 的点直接当作 $X$ 上定义于 $\mathbb Q$ 的线丛：这是有 Brauer 障碍的一般问题。这里没有作这个假设。

$\mathcal L'$ 已经由 (3.1) 给出为实际 $\mathbb Q$ 线丛；(3.2) 说明它在 $\overline{\mathbb Q}$ 上平凡。故
$$
H^0(X_{\overline{\mathbb Q}},\mathcal L'_{\overline{\mathbb Q}})
\simeq\overline{\mathbb Q}.
$$
射影曲线的上同调与域扩张相容，因此 $H^0(X,\mathcal L')$ 是一维 $\mathbb Q$ 向量空间。选择其任意非零向量 $s$；扩标量后它是平凡线丛的非零常数截面，处处不消失。于是 $s$ 本身也处处不消失，给出
$$
\mathcal O_X\xrightarrow{\sim}\mathcal L'
$$
的 $\mathbb Q$ 同构。

处处非零截面正是到 $\mathcal P^\times$ 的所求提升。任意两个此类截面的比为全局单位；因为 $X$ 射影且几何连通，
$$
H^0(X,\mathcal O_X^\times)=\mathbb Q^\times,
$$
所以提升的歧义恰为一个 $\mathbb Q^\times$ 标量。

最后，$u=t_e\circ[d]\circ\iota_b$ 在几何纤维上是 Abel–Jacobi 闭嵌入与有限同源的复合，故其纤维有限。$\widetilde u$ 的任一纤维包含于 $u$ 的某一纤维中，因此同样有限。定理得证。

## 5. 次数零条件不依赖有理基点

本定理明确保留条件 $\deg (u,f\circ u)^*\mathcal P=0$。它是 QC 对应需要满足的条件之一，不能只因 $f\ne0$ 就省略。

可以在任意几何基点 $b$ 上检查它。仍写 $u=d\iota_b+e$。双线性给出
$$
(u,f u)^*\mathcal P\simeq
(\iota_b,f\iota_b)^*\mathcal P^{\otimes d^2}
\otimes(\iota_b,f(e))^*\mathcal P^{\otimes d}
\otimes(e,f\iota_b)^*\mathcal P^{\otimes d}
\otimes\mathcal P_{(e,f(e))}.
\tag{5.1}
$$
后面三个因子次数为零：前两个是代数等价于零的丛的拉回，最后一个来自基域的一维向量空间。因此
$$
\deg (u,f u)^*\mathcal P
=d^2\deg(\iota_b,f\iota_b)^*\mathcal P.
\tag{5.2}
$$
所以在通常 Abel–Jacobi 归一化下满足次数零条件的对应，在 $u=\iota_D$ 下仍满足。这里选择的 $b$ 仅用于证明等式，不参与最终的 $\mathbb Q$ 定义数据。

## 6. 对当前非分裂 Cartan 路线的含义

同日笔记 `notes/2026-11-12-qc-without-cm-basepoints.md` 已证明：对无穷多个素数层 $p$，$X_{\rm ns}^+(p)$ 没有有理 CM 点，因此不能在全层算法中总是假定存在已知有理 CM 基点。

可以具体取所有几何尖点的约化和
$$
D_{\rm cusp}=\sum_{c\text{ 为几何尖点}}c.
$$
[R4](R4-runge-cover-obstruction.md) 证明这些尖点有 $(p-1)/2$ 个并构成一个 Galois 轨道，所以 $D_{\rm cusp}$ 是有理除子，次数
$$
d=(p-1)/2.
$$
各尖点宽度都是 $p$：宽度整除 $p$，而正规化子阶素于 $p$，不包含非平凡的模 $p$ 单幂元，所以宽度不可能为 $1$。因此 $j^*(\infty)=pD_{\rm cusp}$ 也可使用，但不必多乘一个 $p$。

R12 进一步给出：对满足 (1.2) 的有理对应，可在 $\mathbb Q$ 上构造其仿射修正 $h$ 及一个代数 torsor 提升，而不要求有理基点、也不要求 $\kappa$ 可被 $d$ 整除。这补上的是**存在性层面的线丛平凡化**。

尚未包含在结论中的步骤有：在正规整数模型的合适开集上实现提升，追踪坏素数的垂直除子修正，用无方程表示计算 $\kappa$ 与非零截面 $s$，固定兼容的 $\mathbb Q^\times$ 标定，以及证明最终 QC 函数确实一致排除非 CM 候选。尤其不能由代数提升的存在推得其整数点闭包已经可计算。

还有一个精确的积分限制：乘以 $d$ 在 $\mathbb Q$ 上无碍，但若辅助素数 $\ell\mid d$，则它在 $\mathbb Z_\ell$ 上不是单位，可能使模 $\ell$ 系数退化。特别是固定 $\ell=5$、$p\equiv1\pmod{10}$ 时，$5\mid(p-1)/2$。因此不能凭 R12 推断 equationless QC 的积分满射条件、所选坐标的可逆性或有效的模 $\ell$ 二次筛在替换后自动保留。R9 在 $\ell=5$ 的 CM 点分离与此处的积分非退化是两个不同问题。

这与 Hashimoto–Lido–Lombardo–Mascot–Parent, *Equationless quadratic Chabauty for non-split Cartan modular curves* (2026), Remark 3.0.8 提到的无有理基点问题相关；[预印本](https://arxiv.org/abs/2608.10919)。R12 的证明没有调用该预印本的未公认结论，而是从经典 Jacobian 自对偶性和 Poincaré 双线性直接推出。
