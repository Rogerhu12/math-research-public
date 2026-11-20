# R12 附录：自适应硬截断复制递推的五次费用下界

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：以下递推、最优 Deddens 成本及五次下界均已证明。** 本稿关闭的是一个明确的正向复制机制：即使各截断深度按同一条实际输入序列自适应选择，只要递推保持非零范数下界，其累计对数 Deddens 成本仍至少为常数乘 $n^5$。这不是所有 Deddens 选择的下界，也不排除软截断、源依赖的非复制重排或其他普通不变子空间方法。

内部对象为 [R9](R9-radial-odometer-and-nilpotent-approximants.md) 的原 Haar 算子；Deddens 定义与已知范围见 [完整边界附录](R12-appendix-deddens-algebra-localizing-and-uniform-cost-obstruction.md)。本稿所需成本另作直接证明，无需预先调用新的有限头成本公式。

## 1. 算子与精确结论

固定

$$
H=L^2(\mathbb Z_2,\mu),\qquad Uf(y)=f(y-1),\qquad A=M_wU,
$$

$$
w(0)=0,\quad w(y)=\alpha_{v_2(y)}\ (y\ne0),\qquad
\alpha_j=e^{-L_j},
$$

$$
L_j=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3},
\qquad \alpha_0=e^{-20}.
\tag{1.1}
$$

令 $P_{\rm odd}$ 为奇数类的乘法投影。对整数 $J\ge2$，置

$$
q_J(x)=\mathbf1_{\{x\bmod2^J\ne2^J-1\}},\qquad
R_J=\alpha_0^{-1}(I+U)P_{\rm odd}M_{q_J}.
\tag{1.2}
$$

即先在同一个输入端删去低 $J$ 位的最后一格，再将每个保留的奇数格复制到该奇数格和紧随其后的偶数格。该 cut 保证后一平移没有越过 $2^J$ 边界。

对给定 $f_0\in H$ 和任意整数序列 $J_i\ge2$，定义

$$
f_i=R_{J_i}Af_{i-1}\quad(i\ge1),\qquad j_i=J_i-1.
\tag{1.3}
$$

允许 $J_i$ 依赖此前全部实际输入和输出，不假定预先选定、独立性或任何尾速率。

Deddens 成本为

$$
c_A(X)=\inf\{C:\|A^\ell Xf\|\le C\|A^\ell f\|,
\ \ell\ge1,\ f\in H\}.
\tag{1.4}
$$

**主定理。**

1. 对每个 $J\ge2$，

   $$
   \boxed{\|R_J\|=\frac{\sqrt2}{\alpha_0},\qquad
   c_A(R_J)=\sqrt{\alpha_0^{-2}+\alpha_{J-1}^{-2}}.}
   \tag{1.5}
   $$

2. 若同一条实际递推满足某个非零范数下界

   $$
   \inf_{n\ge1}\|f_n\|\ge a>0,
   \tag{1.6}
   $$

   则存在只依赖 $f_0,a$ 的 $0<\delta<1$，使每个 $n\ge1$ 都有

   $$
   \boxed{\sum_{i=1}^n\log c_A(R_{J_i})
   \ge \frac{20\delta^5}{(1-\delta)^4}\,n^5.}
   \tag{1.7}
   $$

3. 原幂范数 $\beta_n=\|A^n\|$ 满足显式界

   $$
   0<-\log\beta_n\le\frac{940}{7}\,n^4\qquad(n\ge1).
   \tag{1.8}
   $$

因此，这个复制家族不能通过按 $v_2(i)$ 稀疏支付深层 carry，将实际累计成本降到原 $\beta_n$ 的四次对数衰减预算内。五次损失不是逐步粗取最大值造成的。

## 2. 同一输入上的真实复制递推

写

$$
g_i(z)=f_i(2z),\qquad g_0(z)=f_0(2z).
\tag{2.1}
$$

$g_0\in L^2(\mathbb Z_2)$，且 $\|g_0\|_2^2\le2\|f_0\|_2^2$。在奇数上 $w=\alpha_0$。将 (1.2)–(1.3) 分别代入偶数与奇数输出，得到

$$
g_i(z)=
\mathbf1_{\{z\notin2^{j_i}\mathbb Z_2\}}g_{i-1}(z-1),
\tag{2.2}
$$

$$
f_i(2z+1)=
\mathbf1_{\{z+1\notin2^{j_i}\mathbb Z_2\}}g_{i-1}(z)
=g_i(z+1).
\tag{2.3}
$$

特别地，对每个 $i\ge1$，

$$
\|f_i\|_2^2
=\frac12\int\big(|g_i(z)|^2+|g_i(z+1)|^2\big)\,d\mu(z)
=\|g_i\|_2^2.
\tag{2.4}
$$

定义同一初始输入坐标上的存活集合

$$
G_n=\mathbb Z_2\setminus
\bigcup_{i=1}^n\left(-i+2^{j_i}\mathbb Z_2\right).
\tag{2.5}
$$

从 (2.2) 逐次展开，

$$
g_n(z)=g_0(z-n)
\prod_{i=1}^n
\mathbf1_{\{z-n+i\notin2^{j_i}\mathbb Z_2\}}.
$$

所以

$$
\boxed{\|f_n\|_2^2
=\int |g_0(x)|^2\mathbf1_{G_n}(x)\,d\mu(x).}
\tag{2.6}
$$

这里没有把输入替换成其有限头条件期望，也没有为每一步重新选择一个不同的初始向量。$G_n$ 单调递减，公式对任意自适应选择产生的实际整数序列 $j_i$ 都成立。

若 (1.6) 成立，取有限 $M>0$，使

$$
\int_{\{|g_0|^2>M\}}|g_0|^2\,d\mu\le a^2/2.
$$

由 (2.6)，

$$
a^2\le M\mu(G_n)+a^2/2,
\qquad
\mu(G_n)\ge a^2/(2M).
\tag{2.7}
$$

适当减小该正数后，可固定 $0<\delta<1$ 使
$\mu(G_n)\ge\delta$ 对全部 $n$ 成立。这是固定 $L^2$ 输入的积分绝对连续性，不需要 $g_0\in L^\infty$。

## 3. 复制算子的最优 Deddens 成本

令 $N=2^J$，按低 $J$ 位的数字 $0,\ldots,N-1$ 分解 Hilbert 空间。$R_J$ 只使用奇输入列

$$
s=1,3,\ldots,N-3.
$$

每个这样的列分别送到输出 $s$ 与 $s+1$，两个系数都为 $\alpha_0^{-1}$；不同列的输出对互不相交。因此

$$
\|R_J\|=\sqrt2/\alpha_0.
\tag{3.1}
$$

记

$$
h_\ell(x)=\prod_{b=1}^{\ell}w(x+b).
$$

保测平移给
$\|A^\ell f\|^2=\int h_\ell^2|f|^2$。
在尾变量固定时，用 $h_\ell$ 对输入与输出坐标加权，则奇列 $s$ 的两个系数变成

$$
\alpha_0^{-1},\qquad
\alpha_0^{-1}
\frac{h_\ell(s+1+Nz)}{h_\ell(s+Nz)}.
\tag{3.2}
$$

相邻乘积相消给

$$
\frac{h_\ell(s+1+Nz)}{h_\ell(s+Nz)}
=\frac{w(s+1+Nz+\ell)}{w(s+1+Nz)}
\quad\text{a.e.}
\tag{3.3}
$$

因为 $s+1$ 是 $2,\ldots,N-2$ 内的偶数，

$$
w(s+1+Nz)=\alpha_{v_2(s+1)}
\ge\alpha_{J-1},
\qquad w(s+1+Nz+\ell)\le\alpha_0.
\tag{3.4}
$$

加权后各列的输出对仍互不相交，故完整矩阵范数至多

$$
\sqrt{\alpha_0^{-2}+\alpha_{J-1}^{-2}}.
$$

这对全部 $\ell\ge1$ 成立，所以给出 (1.5) 的成本上界。

下界已经在 $\ell=1$ 取到。选择偶输出
$r=2^{J-1}$、奇输入 $s=r-1$，则

$$
w(r+Nz)=\alpha_{J-1},\qquad
w(r+Nz+1)=\alpha_0
$$

对全部尾变量成立。因此该列在 (3.2) 的加权范数恰为上面的数。用支撑在该输入列的任意非零 $L^2$ 向量测试，即得相同下界。这证明最优常数，而非仅一个充分预算。

## 4. 最大 dyadic 圆柱的计数与 Jensen 下界

固定 $n$。令

$$
E_n=G_n^c
=\bigcup_{i=1}^n C_i,\qquad
C_i=-i+2^{j_i}\mathbb Z_2.
\tag{4.1}
$$

两个 dyadic 圆柱若相交，则一个包含另一个。故从有限族 $C_i$ 中删去被其他圆柱真包含的项及重复项后，得到两两不相交的最大圆柱

$$
D_1,\ldots,D_M,\qquad
D_t=b_t+2^{k_t}\mathbb Z_2,\qquad p_t=2^{-k_t}.
\tag{4.2}
$$

每个最大圆柱仍是原族中的一个实际圆柱。由 $\mu(G_n)\ge\delta$，

$$
\sum_{t=1}^M p_t=\mu(E_n)\le1-\delta.
\tag{4.3}
$$

注意被覆盖的整数点准确是

$$
-1,-2,\ldots,-n.
$$

这些点都属于 $E_n$。模 $2^{k_t}$ 的一个同余类，在这 $n$ 个连续整数中至多出现
$\lfloor n/2^{k_t}\rfloor+1\le np_t+1$ 次。因此

$$
n\le\sum_{t=1}^M(np_t+1)
\le n(1-\delta)+M,
\qquad M\ge\delta n.
\tag{4.4}
$$

每个 $D_t$ 来自不同的保留指标，故

$$
\sum_{i=1}^n16^{j_i}
\ge\sum_{t=1}^M16^{k_t}
=\sum_{t=1}^M p_t^{-4}.
\tag{4.5}
$$

函数 $u\mapsto u^{-4}$ 在正实数上凸。Jensen 不等式、(4.3)–(4.4) 给

$$
\sum_{t=1}^M p_t^{-4}
\ge M\left(\frac{\sum_t p_t}{M}\right)^{-4}
=\frac{M^5}{(\sum_t p_t)^4}
\ge\frac{\delta^5 n^5}{(1-\delta)^4}.
\tag{4.6}
$$

这个论证允许任意重叠与嵌套，并未把所有被删圆柱的测度直接相加。即便截断深度专门按 $v_2(i)$ 或此前输入进行安排，(4.6) 也不改变。

由 (1.1)，$L_0=20$，而对 $j\ge1$，

$$
\begin{aligned}
L_j-20\,16^j
&=\frac{220}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}\\
&\ge\frac{85}{3}16^j+300\,2^j-\frac{850}{3}>0.
\end{aligned}
\tag{4.7}
$$

这里用了 $90\,8^j\le45\,16^j$。所以 $L_j\ge20\,16^j$。由最优常数 (1.5)，

$$
\log c_A(R_{J_i})\ge L_{j_i}\ge20\,16^{j_i}.
\tag{4.8}
$$

将 (4.6) 代入即得主下界 (1.7)。

## 5. 原幂范数的显式四次上界

原权的同余类计数给

$$
-\log\beta_n
=nL_0+\sum_{r\ge1}(L_r-L_{r-1})
\left\lfloor\frac n{2^r}\right\rfloor.
\tag{5.1}
$$

为使这里自含，每段 $n$ 个连续数中模 $2^r$ 零同余类至少出现
$\lfloor n/2^r\rfloor$ 次，这给范数上界；在 $0$ 的足够小的 $2$-进邻域内，$x+1,\ldots,x+n$ 与 $1,\ldots,n$ 的阶同时一致，因而该上界在正测集合取到，得到等式。

设 $k=\lfloor\log_2n\rfloor$，则 (5.1) 的 $r>k$ 项为零。对 $r\ge1$，有
$90\,8^r\ge300\,2^r$，故 $L_r\le100\,16^r$；又 $L_r-L_{r-1}\le L_r$。于是

$$
\begin{aligned}
-\log\beta_n
&\le20n+100n\sum_{r=1}^{k}8^r\\
&=20n+\frac{800}{7}n(8^k-1)\\
&\le20n+\frac{800}{7}n^4\\
&\le\frac{940}{7}n^4.
\end{aligned}
\tag{5.2}
$$

当 $k=0$ 时几何和为空，上式同样成立。这给出 (1.8)，没有以粗略“超指数”替代实际次数比较。

## 6. 这个机制准确关闭到哪里

由于本稿递推次序是 $R_{J_i}A$，标准 Deddens 移动不等式准确写成

$$
\|f_n\|
\le
\|R_{J_n}\|
\left(\prod_{i=1}^{n-1}c_A(R_{J_i})\right)
\beta_n\|f_0\|.
\tag{6.1}
$$

最左侧的 $R_{J_n}$ 使用普通算子范数；其余各 $R_{J_i}$ 依次通过前面的 $A$ 幂，用定义 (1.4) 支付。不能把这个次序误写成所有 $A$ 都自动与 $R_J$ 交换。

若真实递推保持 (1.6)，对前 $n-1$ 步应用 (1.7)，再用 (5.2)，便知 (6.1) 右侧的预算因子至少增长为

$$
\frac{\sqrt2}{\alpha_0}
\exp\left(
\frac{20\delta^5}{(1-\delta)^4}(n-1)^5
-\frac{940}{7}n^4
\right).
\tag{6.2}
$$

它不会趋零。这是在说明该上界预算无法产生矛盾，**不是**声称实际 $\|f_n\|$ 发散。实际范数始终由 (2.6) 的存活质量控制。

如果目标是让每一步返回一个不含零的固定闭球，则自然满足一个非零范数下界，所以本稿结论直接适用。深度自适应、圆柱重叠或依据 $v_2(i)$ 的稀疏安排，都不能改变这个硬截断复制家族的五次费用门。

要继续正向研究，须改变存活集合为递减圆柱补集的结构，例如引入保留部分质量的软截断，或利用同一来源的实际分量进行非复制重排。本稿未给出这些替代机制的费用上界，也没有从本机制的失败推断一般普通不变子空间问题。
