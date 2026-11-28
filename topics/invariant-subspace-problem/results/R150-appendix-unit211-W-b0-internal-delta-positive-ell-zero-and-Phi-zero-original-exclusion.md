# R150：W/b0 内部 delta 正估值的 ell 零剩余与 Phi 零剩余两支排除

作者：GPT-6 Astra Pro（AI-assisted），Astra-ISP-8542378f-20261127 / r150_open_geometry。日期：2026-11-29（Asia/Taipei）。

**结论。** 在当前正确 W、完整 $b_0=0$、物理 $D_{\rm phys}\ne0$ 原图，剩余特征1009的赋值满足
$$
v(e)=v(k)=v(u)=0,\qquad v(\delta)>0
\tag{1}
$$
时，下面两个分支分别为空：

- $v(\ell)>0$，即本图中 ell 的剩余值为零；
- $\bar u=3/4$，即 ell 整且 $3\bar u-2\ne0$ 时 Phi 的剩余值为零。

两支只用原 b0、q2、R6，不使用含 Phi 逆的 N5。证明完整保 mu 的零值、任意正阶与极点；无新执行、投影、初始理想或因式计算。一般 delta 图的其他剩余值仍须另行处理，不能据本稿宣整个 W 排空。

## 1. 原同点定义与剩余权

原定义见 [完整 b0/N5 源](../notes/2026-11-28-unit211-W-entire-b0-new-full-N5-two-low-original-scalars-8542.py)，blob **47281af16fdd0ad7500ecda377c3cb9f9d65e725**、SHA-256 **e356e79c8570b34ef3d041f828a3906006d82bc813b3719ef606e7ce068cbfe8**。这里只引用其中准确原定义及已经成立的必要性，不执行其旧目标。

令
$$
\begin{gathered}
u=e+1,\quad Q=ek,\quad\delta=1-Q,\quad
\ell=\frac{u((k+2)^2-2ek)}{k(uk+2)},\\
m=u-\ell,\quad M=\ell^2\delta-m^2,\quad
J=2u(1-u)+\ell Q,\quad A_*=4uQ-J,\quad
C_*=A_*m^2+J\delta\ell^2,\\
\mu=2\lambda-3,\quad
A_2=(\mu^2+4\mu+5)/2,\quad
B_3=(\mu^3+6\mu^2+12\mu+7)/2 .
\end{gathered}
\tag{2}
$$
在整个 b0 图，原 Astar 非零且
$$
A_*T=uQ\ell\mu,\qquad
D=\ell A_2-T^2,\qquad
K=\ell^2B_3-3\ell A_2T+2T^3.
\tag{3}
$$
同点原必要式为
$$
q_2=2C_*A_2+2M\ell Q(3-4\lambda)-8uQ\delta\ell T^2=0,
\qquad
R_6=MK^2-4m^2D^3=0.
\tag{4}
$$
所有后续比较都针对这些准确原式，不把分量范数零拼成原值充分条件。

写 $U=\bar u\ne0,1$。当 $3U-2\ne0$ 时，$\bar Q=1$ 给
$$
\ell_0=\frac{U(2U^2-1)}{3U-2},\quad
m_0=-\frac{U(U-1)(2U-1)}{3U-2},\quad
(A_*)_0=\frac{U(4U^2+2U-3)}{3U-2},
$$
$$
\Phi_0=-\frac{2(U-1)^2(4U-3)}{3U-2}.
\tag{5}
$$
若 U=2/3，ell 分子剩余非零，因此 ell 有极点，不属于下文两个分支。该极点分支由已刊 [全 W/b0 的 ell 整性](R150-appendix-unit211-W-b0-global-ell-integrality-and-Vbar-positive-finite-weight-chart.md) 排除；本稿不重做该证明。

## 2. 整个 ell 正阶分支

设 $b=v(\ell)>0$。由 (5)，
$$
2U^2-1=0.
\tag{6}
$$
这两个剩余根均不同于 $0,1,-1,1/2,2/3$；所以 m、M、Astar 是赋值环单位，
$$
m_0=U,\quad M_0=-U^2,\quad (A_*)_0=2U(U+1)\ne0.
$$
由原 b0，$T=\ell\beta\mu$，其中 $\beta=uQ/A_*$ 是赋值环单位。

先允许 mu 有任意极点，记 $s=v(\mu)<0$。则
$$
v(T)=b+s,\quad v(A_2)=2s,\quad v(B_3)=3s.
$$
D 的两项阶为 $b+2s$ 和 $2b+2s$，因此
$$
v(D)=b+2s.
$$
K 的前三项阶分别为 $2b+3s,2b+3s,3b+3s$，允许前两项任意相消，仍有
$$
v(K)\ge2b+3s.
$$
因此 R6 第一项阶至少 $4b+6s$，第二项阶准确 $3b+6s$；后者严格更低，矛盾。mu 的所有极点已经排除，不需要任何 K 首项单位。

现在 mu 整，T 的阶至少 b。Cstar 是赋值环单位，q2 的其余两项分别至少 b 和 $v(\delta)+3b$，所以
$$
v(A_2)\ge b.
\tag{7}
$$
特别剩余 lambda 满足 $2\lambda^2-2\lambda+1=0$。该式下
$$
B_3=-\lambda\ne0
$$
作为剩余域恒等式；不选其中某个根。由 (3)、(7)，
$$
v(D)\ge2b,\qquad v(K)=2b.
$$
K 的最低项是 $\ell^2B_3$；另外两项阶至少3b。R6 第一项阶准确4b，第二项阶至少6b，再次不可能相消。

因此 ell 正阶整个分支排除。证明包括 mu 恰零或任意非负阶；没有先付 mu 单位，也不要求 D 首项未相消。

## 3. Phi 零剩余的整个 U 等于四分之三支

当 ell 整且 $3U-2\ne0$ 时，(5) 与 U 不等于1表明 Phi 剩余零恰为
$$
U=3/4.
$$
此时
$$
\ell_0=m_0=3/8,\qquad M_0=-9/64,\qquad
(A_*)_0=9/4,\qquad
\overline{uQ\ell/A_*}=1/8 .
\tag{8}
$$
这些量都是赋值环单位。原 q2 对 mu 的二次头在 delta=0 的剩余是 $m_0^2(A_*)_0\ne0$，所有其他系数也整，所以 mu 必整。这里完全不倒 Phi：只使用 (2)–(4)。

原 q2 的剩余归一为
$$
q(\mu)=3\mu^2+14\mu+18=0.
\tag{9}
$$
以下在剩余域中省略 mu 的横线；同点 $\bar T=\mu/8$。直接按 (3) 并仅用 (9) 作普通二次余式，得到
$$
D_0=-\frac{5\mu+9}{96},\qquad
K_0=-\frac{118\mu+279}{1152}.
\tag{10}
$$
M0=-m0平方，因此原 R6 必给 $K_0^2+4D_0^3=0$。在 (9) 下，
$$
1327104(K_0^2+4D_0^3)=642\mu-6777.
\tag{11}
$$
这只是两个小普通恒等式的纸面化简，并非新运行。642 与214在特征1009均非零，所以 (11) 迫
$$
\mu=2259/214.
$$
将其代回 (9)，分子为
$$
3\cdot2259^2+14\cdot2259\cdot214+18\cdot214^2
=22901535\equiv262\pmod{1009},
\tag{12}
$$
非零。于是整 Phi 零剩余支排除。

(10)–(12) 是整个剩余二次商中的恒等式，覆盖任意剩余域扩张与全部根。没有从某个有限域数值点外推 QQ 空性，也没有借用因 Phi 逆失效的 N5 恢复。

## 4. 准确范围

本稿只关闭 (1) 中 ell 剩余零及 Phi 剩余零两支。mu 的每个估值范围都完整保留到原式比较；所有最终整数在特征1009均非零。ell 极点、深 m、Astar 正阶和一般剩余开图的处理各有独立来源，不能把这些不同范围混写成单次执行。

**执行说明。** 本文没有新脚本、Actions run 或复算。使用原 q2/R6 的纸面估值，以及 (9)–(12) 的显示二次余式恒等式；不保存或传输任何可重算系数载荷。
