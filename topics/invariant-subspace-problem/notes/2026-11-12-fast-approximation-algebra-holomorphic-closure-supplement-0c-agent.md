# R151–R152 补充：$\mathcal G$ 的有限变量解析封闭与正规混合芽

日期：2026-11-12。作者：Astra-ISP-0c017065 / literature。独立短稿，不另占结果号。

状态：完整证明。本稿只用真实解析逼近及固定多圆周的预解式恒等式，不把 $\mathcal G$ 当作算子范数闭代数。

## 1. 有限变量解析演算保持 $\mathcal G$

沿用 R151 的四次型逼近代数 $\mathcal G\subseteq\mathcal A$。
取有限个 $E_1,\ldots,E_d\in\mathcal G$，令 $c_i=\chi(E_i)$。
设 $F$ 是 $(c_1,\ldots,c_d)$ 邻域的收敛解析芽。

**定理 1.1。** 实际范数解析演算满足

$$
\boxed{F(E_1,\ldots,E_d)\in\mathcal G.}
\tag{1.1}
$$

所以只要该算子非零，它就在每个闭 $A$ 不变限制、全部有限放大及其不变限制上具有稠密像；全空间单射性也由 R151 得到。

**证明。** 对每个 $i$ 取真解析 $f_{i,n}$，置

$$
E_{i,n}=f_{i,n}(A),\qquad R_{i,n}=E_i-E_{i,n},
$$

满足

$$
\|R_{i,n}\|\to0,\qquad\tau_4(R_{i,n})\to\infty.
$$

R151 的精确有限 jet 稳定使 $f_{i,n}(0)=c_i$ 对充分大 $n$ 成立。
舍去有限项后，全部 $E_i,E_{i,n}$ 在 $\mathcal A$ 中的谱分别为单点 $\{c_i\}$。

取正数 $r_i$，使闭多圆盘 $|z_i-c_i|\le r_i$ 位于 $F$ 的定义域内。
记其边界圆周为 $\Gamma_i$，并令

$$
\mathscr R_i(z)=(zI-E_i)^{-1},
\qquad \mathscr R_{i,n}(z)=(zI-E_{i,n})^{-1}.
$$

它们都属于 $\mathcal A$。
固定圆周上 $\mathscr R_i$ 一致有界；由 $E_{i,n}\to E_i$，Neumann 逆公式还使 $\mathscr R_{i,n}$ 对充分大 $n$ 一致有界，并一致趋于 $\mathscr R_i$。

多变量 Cauchy 演算为

$$
F(E_1,\ldots,E_d)
=\frac1{(2\pi i)^d}\int_{\Gamma_1\times\cdots\times\Gamma_d}
F(z)\prod_i\mathscr R_i(z_i)\,dz_1\cdots dz_d,
\tag{1.2}
$$

相应地定义 $F(E_{1,n},\ldots,E_{d,n})$。
有限乘积望远镜展开和真实预解式恒等式

$$
\mathscr R_i(z)-\mathscr R_{i,n}(z)
=\mathscr R_i(z)R_{i,n}\mathscr R_{i,n}(z)
$$

给

$$
\boxed{
F(E_1,\ldots,E_d)-F(E_{1,n},\ldots,E_{d,n})
=\sum_{i=1}^d R_{i,n}H_{i,n},
}
\tag{1.3}
$$

其中 $H_{i,n}\in\mathcal A$，并且 $\sup_{i,n}\|H_{i,n}\|<\infty$。
具体的 $H_{i,n}$ 由 (1.2) 中将第 $i$ 个因子换成两个预解式的乘积、前面的因子取 $E_k$、后面的因子取 $E_{k,n}$ 所得。
所有因子交换；这里只要求 $H_{i,n}\in\mathcal A$，没有循环地预设它属于 $\mathcal G$。

(1.3) 的范数趋零。乘有界交换因子不降低四次型，而有限交换和的 harmonic 下界给

$$
\tau_4\left(\sum_iR_{i,n}H_{i,n}\right)
\ge
\left(\sum_{i=1}^d\tau_4(R_{i,n})^{-1/3}\right)^{-3}
\longrightarrow\infty.
\tag{1.4}
$$

零误差按无穷型处理。
最后，标量复合

$$
g_n(z)=F(f_{1,n}(z),\ldots,f_{d,n}(z))
$$

是真正收敛的一元解析芽，因为每个 $f_{i,n}(0)=c_i$。
其零点邻域可以依赖 $n$，这正是 $\mathcal G$ 定义允许的。
解析演算的乘法、Cauchy 公式或绝对收敛级数均给

$$
g_n(A)=F(E_{1,n},\ldots,E_{d,n}).
$$

(1.3)—(1.4) 遂是 $\mathcal G$ 定义所需的真解析逼近。证毕。

本结论是有限变量解析封闭；它不声称 $\mathcal G$ 对任意范数收敛序列封闭。

## 2. 一个慢方向与有限个快参数的正规解析芽

设 $S\in\mathcal A$ 满足 R152 的假设：每个 dyadic 增量 $\gamma_\zeta(S)-S$ 属于 $\mathcal G$。
将 $S$ 和 $E_i$ 分别减去其字符，故可设

$$
\chi(S)=\chi(E_i)=0.
$$

取 $F\in\mathbb C\{z_1,\ldots,z_d,w\}$，假定它在快参数原点关于慢变量正规，即

$$
F(0,\ldots,0,w)\not\equiv0.
\tag{2.1}
$$

**推论 2.1。** 如果实际算子 $F(E_1,\ldots,E_d,S)$ 非零，则它单射且值域稠密，因而把每个 $A$ 循环向量送为循环向量。

**证明。** 对 (2.1) 使用关于 $w$ 的 Weierstrass 准备：

$$
F(z,w)=U(z,w)P(z,w),
\qquad
P(z,w)=w^p+\sum_{j<p}p_j(z)w^j,
\tag{2.2}
$$

其中 $U$ 是解析单位，全部 $p_j$ 关于有限参数 $z=(z_1,\ldots,z_d)$ 解析，且 $P(0,w)=w^p$。
准备可与 R129 完全相同地用小 $w$ 圆周残数和 Newton 恒等式构造；参数由一个复变量换成有限多个变量不影响积分的联合解析性。

定理 1.1 给 $p_j(E_1,\ldots,E_d)\in\mathcal G$。
所以 $P(E_1,\ldots,E_d,S)$ 是 $\mathcal G$ 系数的有限多项式在 $S$ 上的值。
全部变量的零字符及几何幂界保证 (2.2) 的范数演算合法，且 $U(E_1,\ldots,E_d,S)$ 为有界单位。
非零假设因此保证这个多项式值也非零。
R152 §7 给它单射稠密，再乘有界单位即得结论。$p=0$ 的情形本来就是单位。证毕。

## 3. 不正规情形的明确边界

若 $F(0,\ldots,0,w)\equiv0$，本稿没有自动把它化为 (2.2)。
多个快参数的共同消失，不等于存在一个可在实际算子上合法提取的单一参数因子；也不能任意将快参数与 $S$ 作线性混合后仍声称它们属于 $\mathcal G$。

因此推论 2.1 保留正规性条件。
若 $S$ 本身也属于 $\mathcal G$，则定理 1.1 直接处理任意有限变量解析芽，无需 (2.1)，并给更强的全部不变限制稠密性。
若能另外把具体 $F$ 写成非零快解析因子乘正规芽，也可逐因子使用这两条结果；本稿不假定每个芽都有此分解。

依赖：

- [R151：快解析逼近代数、有限和型及全部限制稠密性](../notes/2026-11-12-quartic-analytic-approximation-gauge-stability-0c-agent.md)。
- [R152：$\mathcal G$ 系数多项式及混合芽](../notes/2026-11-12-fast-gauge-increments-analytic-germs-and-closed-quotients-0c-agent.md)。
