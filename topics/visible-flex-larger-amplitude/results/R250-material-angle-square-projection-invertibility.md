# R250. 对称单调材料换角的非均值方块投影可逆

2026-11-14，amplitude，AI 辅助。

**状态：已证明。** 对下述固定、完整、严格单调的对称材料换角，连续余弦投影的前 $M$ 个非均值行与前 $M$ 个非均值列组成的方块具有严格正行列式。实际使用的偶数均匀角网格，在精确算术和精确逆映射的意义下也有相同结论。证明分别由行列式展开与 Fubini、有限 Cauchy–Binet 展开给出。

这里的可逆性只涉及固定换角后的线性高度投影。它不提供条件数下界，不证明完整非线性 DN 或整个 BVP 的线性化可逆，也不把有限材料角截断余项记为零。

## 1. 完整换角与一个单调区间映射

设 $\Phi:\mathbb R\to\mathbb R$ 是 $C^1$ 函数，满足

$$
\Phi'(\varphi)>0,\qquad
\Phi(-\varphi)=-\Phi(\varphi),\qquad
\Phi(\varphi+\pi)=\Phi(\varphi)+\pi.
\tag{250.1}
$$

于是 $\Phi$ 是实线上的严格递增双射，且诱导圆周上的保向微分同胚。记其逆映射为 $\psi$。逆映射同样满足奇对称及 $\pi$ 平移关系。由这两项对称性，

$$
\Phi(0)=0,\qquad \Phi(\pi/2)=\pi/2,\qquad
\Phi(\pi-\varphi)=\pi-\Phi(\varphi),
\tag{250.2}
$$

$\psi$ 也满足相同关系。

本课题 [R240](R240-canonical-material-metric-and-refinement.md) 中的有限完整核心给出一个实例：

$$
\Phi_c(\varphi)
=\varphi+\sum_{m=1}^{K}\frac{1-4m^2}{2m}\,c_m\sin(2m\varphi),
\qquad
\rho_c=\Phi_c'
=1+\sum_{m=1}^{K}(1-4m^2)c_m\cos(2m\varphi).
\tag{250.3}
$$

只要对所有 $\varphi$ 都有 $\rho_c(\varphi)>0$，(250.1) 成立。这里的核心模数 $K$ 不必等于下文高度投影的模数 $M$。假设针对完整核心，而不是删去高模后的核心；有限角网格上的正值本身不证明全角正性。

在 $0\le\theta\le\pi/2$ 上定义

$$
x=\cos(2\theta),\qquad
u(x)=\cos\!\left(2\psi\!\left(\tfrac12\arccos x\right)\right).
\tag{250.4}
$$

$\tfrac12\arccos x$ 随 $x$ 严格递减，$\psi$ 严格递增，而 $\cos(2\varphi)$ 在 $[0,\pi/2]$ 上严格递减。因此 $u$ 是 $[-1,1]$ 到自身的连续严格递增双射，且 $u(-1)=-1$、$u(1)=1$。由 (250.2) 和周期关系，对任意实数 $\theta$ 都有

$$
\cos(2\psi(\theta))=u(\cos(2\theta)).
\tag{250.5}
$$

这一步是对称性所承担的作用：相同的 $x=\cos(2\theta)$ 对应同一个 $u(x)$，包括不同四分之一圆中的角度。

令 $T_j$ 为 Chebyshev 多项式，$T_j(\cos t)=\cos(jt)$，$T_0=1$。则

$$
\cos(2j\psi(\theta))=T_j(u(x)),\qquad
\cos(2i\theta)=T_i(x).
\tag{250.6}
$$

再令 $\mu$ 为反正弦概率测度

$$
d\mu(x)=\frac{dx}{\pi\sqrt{1-x^2}},\qquad -1<x<1.
$$

对连续函数 $f$，逐四分之一圆换元给出

$$
\frac1{2\pi}\int_0^{2\pi}f(\cos(2\theta))\,d\theta
=\int_{-1}^1 f(x)\,d\mu(x).
\tag{250.7}
$$

## 2. 连续投影的精确方块

固定整数 $M\ge1$，定义 $M\times M$ 的非均值投影矩阵

$$
P_{ij}
=\frac1\pi\int_0^{2\pi}
\cos(2i\theta)\cos(2j\psi(\theta))\,d\theta
=2\int_{-1}^1 T_i(x)T_j(u(x))\,d\mu(x),
\quad 1\le i,j\le M.
\tag{250.8}
$$

因此对于法线角高度 $z(\varphi)=z_0+\sum_{j=1}^M z_j\cos(2j\varphi)$，材料角高度 $z(\psi(\theta))$ 的前 $M$ 个非均值余弦系数是 $P(z_1,\ldots,z_M)^{\mathsf T}$。换角一般会产生非零均值及超过 $M$ 的材料角高模；(250.8) 没有把它们删去后认作完整函数。

**定理 250-A。** 在 (250.1) 下，$\det P>0$。

### 2.1 加上常数行、列

令 $m=M+1$，并对 $0\le i,j\le M$ 定义

$$
G_{ij}=\int T_i(x)T_j(u(x))\,d\mu(x),\qquad
D=\operatorname{diag}(1,2,\ldots,2),\qquad A=DG.
\tag{250.9}
$$

由 (250.7)，$G_{00}=1$，并且

$$
G_{i0}=\frac1{2\pi}\int_0^{2\pi}\cos(2i\theta)\,d\theta=0
\quad(1\le i\le M).
$$

因此

$$
A=
\begin{pmatrix}
1 & *\\
0 & P
\end{pmatrix},
\qquad
\det P=\det A=2^M\det G.
\tag{250.10}
$$

常数列的这一精确正交性使全矩阵的正行列式传到非均值方块；不能对任意非正交求积权重直接略去这一步。

### 2.2 行列式积分恒等式的自含证明

对 $x_0,\ldots,x_M\in[-1,1]$，记

$$
\Delta_T(x)=\det[T_i(x_\ell)]_{i,\ell=0}^M,\qquad
\Delta_{T,u}(x)=\det[T_j(u(x_\ell))]_{j,\ell=0}^M.
$$

我们证明

$$
m!\det G
=\int_{[-1,1]^m}\Delta_T(x)\Delta_{T,u}(x)
\,d\mu(x_0)\cdots d\mu(x_M).
\tag{250.11}
$$

两个行列式的展开项分别以排列 $\sigma,\tau$ 标记：

$$
\Delta_T(x)=
\sum_\sigma \operatorname{sgn}(\sigma)
\prod_{i=0}^M T_i(x_{\sigma(i)}),
\qquad
\Delta_{T,u}(x)=
\sum_\tau \operatorname{sgn}(\tau)
\prod_{j=0}^M T_j(u(x_{\tau(j)})).
$$

所有函数连续有界，$\mu$ 为有限测度，求和有限，所以可以交换求和与积分，并按独立变量使用 Fubini。固定 $\sigma,\tau$，令 $\pi=\tau^{-1}\sigma$。变量 $x_{\sigma(i)}$ 的两个因子正是 $T_i$ 与 $T_{\pi(i)}\circ u$，故该项积分为

$$
\prod_{i=0}^M G_{i,\pi(i)}.
$$

它的符号为 $\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)=\operatorname{sgn}(\pi)$。每个固定的 $\pi$ 恰有 $m!$ 对 $(\sigma,\tau)$，因为可以任取 $\tau$，再令 $\sigma=\tau\pi$。合并后恰为 $m!\det G$，证明了 (250.11)。

### 2.3 正性

$T_j$ 的次数为 $j$，首项系数为

$$
a_0=1,\qquad a_j=2^{j-1}>0\quad(j\ge1).
$$

从单项式基到 $T_j$ 的变换是下三角的，对角元为 $a_j$。因此 Vandermonde 行列式公式给出

$$
\Delta_T(x)=\left(\prod_{j=0}^M a_j\right)
\prod_{p<q}(x_q-x_p),
\qquad
\Delta_{T,u}(x)=\left(\prod_{j=0}^M a_j\right)
\prod_{p<q}(u(x_q)-u(x_p)).
\tag{250.12}
$$

由于 $u$ 严格递增，每对差的符号相同。两行列式之积在各 $x_\ell$ 不同时严格为正，有重复点时为零。选择 $m$ 个互不相交、按大小排列且位于 $(-1,1)$ 内的闭小区间，它们的 $\mu$ 测度均正；这些区间的笛卡尔积上，两行列式之积连续且严格为正。故 (250.11) 的积分严格为正。由 (250.10)，$\det P>0$。证毕。

## 3. 均匀 DFT 的精确算术版本

取本课题使用的原点对齐均匀材料角网格

$$
\theta_k=\frac{2\pi k}{N},\qquad 0\le k<N,
$$

并使用同一个完整映射的精确逆值 $\psi(\theta_k)$。定义

$$
P^{(N)}_{ij}=\frac2N\sum_{k=0}^{N-1}
\cos(2i\theta_k)\cos(2j\psi(\theta_k)),
\quad 1\le i,j\le M.
\tag{250.13}
$$

**定理 250-B。** 若 $N$ 为偶数且 $N>4M$，则 $\det P^{(N)}>0$。

这里的均匀网格包含关于 $0$ 的反射对及相差 $\pi$ 的点。由完整逆映射的对称性，它们的重复 $x_k=\cos(2\theta_k)$ 对应相同的 $u(x_k)$。把所有重复 $x_k$ 合并，得到严格递增的不同支撑点

$$
\xi_1<\cdots<\xi_L,\qquad
w_\ell=\frac{\#\{k:x_k=\xi_\ell\}}N>0,\qquad
\sum_{\ell=1}^L w_\ell=1.
\tag{250.14}
$$

一般地，$e^{2i\theta_k}=e^{4\pi i k/N}$ 遍历
$Q=N/\gcd(N,2)$ 个不同的单位根，余弦值的个数为

$$
L=\lfloor Q/2\rfloor+1.
\tag{250.15}
$$

在本定理的偶数网格中，$L=\lfloor N/4\rfloor+1$，故 $N>4M$ 保证 $L\ge M+1$。并且几何级数求和给出

$$
\frac1N\sum_{k=0}^{N-1}\cos(2i\theta_k)=0
\quad(1\le i\le M),
\tag{250.16}
$$

因为 $N\nmid 2i$。对重复点合并之后，(250.16) 仍然成立。

定义全矩阵

$$
G^{(N)}_{ij}
=\sum_{\ell=1}^L w_\ell T_i(\xi_\ell)T_j(u(\xi_\ell)),
\qquad 0\le i,j\le M.
\tag{250.17}
$$

令 $F_{i\ell}=\sqrt{w_\ell}\,T_i(\xi_\ell)$，
$B_{j\ell}=\sqrt{w_\ell}\,T_j(u(\xi_\ell))$，则 $G^{(N)}=FB^{\mathsf T}$。
有限 Cauchy–Binet 展开是

$$
\det G^{(N)}
=
\sum_{\substack{S\subset\{1,\ldots,L\}\\|S|=m}}
\left(\prod_{\ell\in S}w_\ell\right)
\det[T_i(\xi_\ell)]_{\substack{0\le i\le M\\\ell\in S}}
\det[T_j(u(\xi_\ell))]_{\substack{0\le j\le M\\\ell\in S}},
\tag{250.18}
$$

每个 $S$ 内的列按 $\xi_\ell$ 的递增次序排列。为自含地验证此公式，把 $FB^{\mathsf T}$ 的每一列写成 $F$ 各列的线性组合，然后按行列式的列多线性展开。重复选择某个 $F$ 列的项为零；对同一组不同列 $S$，再对其全部排列求和，恰好得到 $B$ 相应子矩阵的行列式。抽出两侧的 $\sqrt{w_\ell}$ 就是 (250.18)。

由 (250.12) 和 $u$ 的严格递增性，(250.18) 每一项都严格为正；由于 $L\ge m$，至少存在一项，故 $\det G^{(N)}>0$。由 (250.16)，$DG^{(N)}$ 的常数列是 $(1,0,\ldots,0)^{\mathsf T}$，其非均值方块正是 (250.13)。因此

$$
\det P^{(N)}=2^M\det G^{(N)}>0.
\tag{250.19}
$$

证毕。

证明也说明了两个条件各自的作用：至少 $M+1$ 个不同正权支撑点保证全矩阵的正行列式，常数列的精确正交性再把结论传到非均值方块。如果全矩阵只有 $L<M+1$ 个不同支撑点，则由 (250.17) 其秩不超过 $L$，不可能满秩。偶数 $N>4M$ 是实际网格的一个充分条件；本文不据此修改任何程序对角网格或 Nyquist 模式的约束。

## 4. 对当前完整 DN 接口的确切含义

1. 固定满足 (250.1) 的完整核心，并固定相同的投影定义时，前 $M$ 个法线角非均值高度系数不会在精确的前 $M$ 个材料角投影行中丢失线性维数。如果保留 $T\ge M$ 个材料角行，则其前 $M$ 行构成上述可逆方块，故这个 $T\times M$ 线性高度投影具有满列秩。本文没有改变实际接口的 $T\ge M$ 条件。
2. 非均值方块一般既不对称，也不是二次型意义下的正定矩阵。$\det P>0$ 或 $\det P^{(N)}>0$ 本身不提供可用的最小奇异值下界；不能从中推出良好条件数。求逆误差、有限精度逆角值和舍入都仍可能影响实际计算。
3. 均匀 DFT 定理以精确角点、精确逆映射和精确算术为前提。程序中的迭代逆角误差、对称性舍入误差及浮点求和须由实际响应或误差分析处理；本文不把近似矩阵逐位等同于 (250.13)。同样，$\rho_c>0$ 必须针对所有角度成立。
4. 高度投影的可逆性不表示全部材料角高模已被表示，也不界定截断后的高度、斜率、二阶导数或完整 Cartesian 六 jet 误差。那些误差仍要在实际接受切口上按完整材料场量测及精化。
5. 完整右边界还包含物理场的径向演化、真实非线性尾映射及其 Jacobian、核心对材料换角的导数，并在初设计时包含 scalar 控制。全 BVP 的约化 QR 矩阵也包含整段状态传递。因此本定理不证明这些更大的 Jacobian 可逆，不排除实际近核方向，不替代真实线性残差与回溯结果。

本结论是在固定完整材料图上的精确秩事实。它可用于区分“高度换角方块在精确数学中丢失维数”与“实际耦合系统存在条件性、截断或其它核方向”这几类问题；后一类问题必须由完整实际求解继续判别。当前 M112/T112 求解源、原 M96 源、接受门及已保存的数值结果均不因本文而改变。
