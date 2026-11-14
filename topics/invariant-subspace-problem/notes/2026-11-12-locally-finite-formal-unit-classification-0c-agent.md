# 局部有限形式单位的完整分类与非零锚分支的矩分离

日期：2026-11-12。会话：Astra-ISP-0c017065，子任务 l2_moments。

**状态：已证明的中间结论，供登记 R59。** 本条关闭 R55 的 $\alpha\beta\ne0$ 分支，并且最终同时删除有限 Walsh 次数与柱均值收敛假设。对于 Walsh 支撑逐位局部有限的任意两个 $L^2$ 向量，全部双线性矩消失迫使至少一个向量为零；通常内积版本也成立。§7 先证明均值有极限的情形，§8 再证明零矩条件本身排除所有缺少极限的剩余情形。

核心代数结论更独立：逐位局部有限的 Walsh 形式表达式若有同类的形式乘法逆，则二者实际上都只涉及有限多个位。这里不假定无限形式级数有正收敛半径；先在形式域中证明它们有理，之后才使用有理函数的零极点。有限柱之间仍有非平凡互逆，之前的低两位例子得到完整保留。

未证明一般 $L^2$ 向量都满足局部有限性，未决定没有局部有限假设的一般有限 chaos 对的矩分离，未解决完整 Hilbert 不变子空间问题。

依赖：R9/R13 的权积与无进位乘法；R24 的双线性型；R40 §2–3 对任意 $L^2$ 向量成立的精确有限链公式及放大误差。以下形式单位分类及其全部新步骤自含证明。

## 1. 权积与两种不同的生成函数

沿用

$$
W_0=1,\qquad W_n=\prod_{r=1}^n a_{v_2(r)},\qquad
d_j=W_{2^j},\qquad \eta_j=a_{j+1}/a_j.
$$

本模型满足

$$
W_n=\prod_{j:b_j(n)=1}d_j,\qquad
d_{j+1}=\eta_jd_j^2,\qquad
0<\eta_j<1,\qquad W_n^{1/n}\longrightarrow0.
\tag{1.1}
$$

最后一个性质可直接由明确权列得到，也可由 $d_j^{1/2^j}\to0$ 推出：给定 $\varepsilon>0$，对充分大的 $j$ 有 $d_j\le\varepsilon^{2^j}$；把二进制展开中的有限低位与全部高位分开即可得到 $\limsup W_n^{1/n}\le\varepsilon$。

定义

$$
q_j(z)=1+\frac{z^{2^j}}{d_j},\qquad
x_j(z)=\frac{1-z^{2^j}/d_j}{1+z^{2^j}/d_j},\qquad
P_M(z)=\prod_{j<M}q_j(z).
\tag{1.2}
$$

由二进制无进位乘法，

$$
H(z):=\sum_{n\ge0}\frac{z^n}{W_n}
=\prod_{j\ge0}q_j(z)
\tag{1.3}
$$

是一个**形式**幂级数恒等式。$H$ 的解析收敛半径不参与任何一步。

另一方面，

$$
\Theta(t):=\sum_{n\ge0}W_nt^n
=\prod_{j\ge0}(1+d_jt^{2^j})
\tag{1.4}
$$

是一个**整函数**恒等式。确切地说，(1.1) 保证左边整；对每个紧集，$\sum_jd_j|t|^{2^j}$ 一致收敛，所以右边乘积正常收敛，其 Taylor 系数由 (1.1) 给出。

**引理 1.1。** $\Theta$ 的全部零点为

$$
\mathcal Z=\bigcup_{j\ge0}\{\lambda\in\mathbb C:
1+d_j\lambda^{2^j}=0\},
\tag{1.5}
$$

而且全部是非零简单零点。不同 $j$ 的零点模互不相同。

**证明。** 第 $j$ 层零点的模是 $d_j^{-1/2^j}$。由 $d_{j+1}=\eta_jd_j^2$ 及 $\eta_j<1$，这些模严格递增，所以不同层不相交；单个多项式的零点也简单。若各因子都非零，正常收敛乘积不为零：在尾部各项与 $1$ 的差小于 $1/2$，可以取在 $1$ 邻域的对数，其绝对收敛保证尾乘积非零。因此零点恰为 (1.5)，且乘上其余非零因子不改变简单性。证毕。

## 2. 逐位局部有限的形式表达式

以下先不需要 $L^2$ 假设。令 $(c_S)$ 按非空有限子集 $S\subset\mathbb N_0$ 编号，并满足：

$$
\text{对每个 }j,\quad
\#\{S:j\in S,\ c_S\ne0\}<\infty.
\tag{2.1}
$$

不限制所有 $|S|$ 的统一上界。给定 $\alpha\in\mathbb C$，定义

$$
\Phi(z)=\alpha+
\sum_{\varnothing\ne S\Subset\mathbb N_0}
c_S\left(\prod_{j\in S}x_j(z)-1\right).
\tag{2.2}
$$

这是良定义的形式幂级数：对一个固定正阶 $n$，只有包含某个 $j\le\lfloor\log_2n\rfloor$ 的 $S$ 能贡献；(2.1) 保证这样的非零项只有有限多个。

令 $\mathcal L$ 为全部 (2.2) 所成的线性空间。它不是预先假定对乘法封闭的代数。

给定 (2.2)，对普通非负整数 $r$ 定义

$$
\widehat f(r)=\alpha+
\sum_Sc_S\bigl((-1)^{|S\cap J(r)|}-1\bigr),
\qquad J(r)=\{j:b_j(r)=1\}.
\tag{2.3}
$$

这是有限和，$\widehat f(0)=\alpha$。这里的 $\widehat f(r)$ 是由系数定义的整数数据，并未对任意 $L^2$ 等价类擅自取点值。

**引理 2.1。** 有形式恒等式

$$
F(z):=\sum_{r\ge0}\frac{\widehat f(r)}{W_r}z^r
=H(z)\Phi(z).
\tag{2.4}
$$

**证明。** 对单个有限集合 $S$，二进制乘积直接给

$$
\sum_{r\ge0}\frac{(-1)^{|S\cap J(r)|}}{W_r}z^r
=H(z)\prod_{j\in S}x_j(z).
$$

相减再乘 $c_S$ 即得单项公式。对任一固定系数，求和涉及的项由 (2.1) 保证有限，故可以逐系数求和，得到 (2.4)。证毕。

**引理 2.2。** 对每个固定 $r$，充分大的 $j$ 满足

$$
\widehat f(r+2^j)-\widehat f(r)
=\widehat f(2^j)-\widehat f(0).
\tag{2.5}
$$

**证明。** 取 $j$ 大于 $r$ 使用的所有位，并避开所有与 $J(r)$ 相交的非零支撑项中的全部位。这只排除有限多个 $j$。此时，没有非零 $c_S$ 同时涉及 $j$ 和 $J(r)$，所以翻转第 $j$ 位产生的差与是否已翻转 $J(r)$ 无关。这就是 (2.5)。证毕。

## 3. 根单位旋转使互逆对先变成有理函数

记 $\mu_{2^\infty}=\bigcup_m\{\zeta:\zeta^{2^m}=1\}$。

**引理 3.1。** 对 $\Phi\in\mathcal L$ 及每个 $\zeta\in\mu_{2^\infty}$，

$$
\Phi(z)-\Phi(\zeta z)\in\mathbb C(z).
\tag{3.1}
$$

**证明。** 若 $\zeta^{2^m}=1$，则 $x_j(\zeta z)=x_j(z)$ 对 $j\ge m$ 成立。因此只有与 $\{0,\ldots,m-1\}$ 相交的非零支撑项参与差值。(2.1) 使这些项只有有限多个，每项本来就是有理函数。证毕。

**定理 3.2（形式互逆蕴含有理）。** 若 $\Phi,\Psi\in\mathcal L$ 且

$$
\Phi\Psi=c\ne0,
\tag{3.2}
$$

则 $\Phi,\Psi\in\mathbb C(z)$。

**证明。** 若 $\Phi$ 为常数，结论显然。否则选一个 $\zeta\in\mu_{2^\infty}$ 使 $\Phi(\zeta z)\ne\Phi(z)$：取 $\Phi$ 的第一个非常数非零系数对应的阶数 $n$，再选阶大于 $n$ 的 dyadic 根即可。置

$$
a=\Phi(z)-\Phi(\zeta z),\qquad
b=\Psi(z)-\Psi(\zeta z).
$$

由引理 3.1，$a,b$ 有理；且 $a\ne0$。由于 $\Psi=c/\Phi$，也有 $b\ne0$。比较 (3.2) 与旋转后的等式，

$$
\Phi\Psi=(\Phi-a)(\Psi-b),
$$

得到

$$
b\Phi^2-ab\Phi+ca=0.
\tag{3.3}
$$

所以 $\Phi$ 在 $\mathbb C(z)$ 上的代数次数至多二。

反设它不是有理函数。则

$$
\mathbb C(z,\Phi)=\mathbb C(z,\sqrt R)
\tag{3.4}
$$

对某个非平方 $R\in\mathbb C(z)^\times$ 成立。例如可取 (3.3) 的判别式

$$
R=a^2-\frac{4ca}{b},
\qquad \sqrt R=2\Phi-a.
\tag{3.5}
$$

这里 $\sqrt R\in\mathbb C((z))$，因为 $\Phi$ 是形式幂级数，$a$ 是有理函数。特别地，

$$
\operatorname{ord}_0R=2\operatorname{ord}_0\sqrt R
\quad\text{为偶数}.
\tag{3.6}
$$

对任意 $\xi\in\mu_{2^\infty}$，引理 3.1 给 $\Phi(\xi z)-\Phi(z)$ 有理，故

$$
\mathbb C(z,\Phi(\xi z))
=\mathbb C(z,\Phi(z)).
$$

把 (3.4) 旋转后便有

$$
\mathbb C(z,\sqrt{R(\xi z)})
=\mathbb C(z,\sqrt{R(z)}).
\tag{3.7}
$$

两个非平凡二次扩张相等意味着 $R(\xi z)/R(z)$ 是有理函数的平方。此事实可以直接验证：若 $\sqrt{R(\xi z)}=u+v\sqrt{R(z)}$，$u,v$ 有理，则平方后非有理项的系数为 $2uv$，所以 $uv=0$；左边不是有理函数，故 $v\ne0$、$u=0$，从而比值等于 $v^2$。

令

$$
T=\{t\in\mathbb C^\times:\operatorname{ord}_tR\text{ 为奇数}\}.
$$

$R$ 有理，故 $T$ 有限。(3.7) 的平方比值保证 $T$ 在全部 $\xi\in\mu_{2^\infty}$ 的乘法旋转下保持不变。任何非零复数的这种轨道都无限，故 $T=\varnothing$。

结合 (3.6)，$R$ 在每个有限点的零极点阶数都是偶数；在无穷远处也为偶数，因为全部阶数之和为零。复常数都有平方根，所以把 $R$ 的有限零极点分解后即知 $R$ 本身是有理函数的平方，与 (3.4) 非平凡矛盾。

因此 $\Phi$ 有理，再由 $\Psi=c/\Phi$ 得 $\Psi$ 有理。证毕。

整个论证在形式 Laurent 域及有理函数域中进行；没有对无限表达式 (2.2) 的解析零极点作任何假设。

## 4. 有理且局部有限，迫使一个整函数卷积方程

现在只假设 $\Phi\in\mathcal L\cap\mathbb C(z)$，不再需要互逆向量。写

$$
\Phi(z)=\sum_{k\ge0}r_kz^k.
\tag{4.1}
$$

$\Phi$ 在 $0$ 解析，因此存在 $C,R_0<\infty$、$R_0\ge1$，使

$$
|r_k|\le CR_0^k\qquad(k\ge0).
\tag{4.2}
$$

由 (2.4)，

$$
\widehat f(n)=W_n\sum_{k=0}^n\frac{r_k}{W_{n-k}}.
\tag{4.3}
$$

置 $N=2^j$、$C_j=W_{N-1}$。对 $0\le n<N$，无进位乘法及权积反射给

$$
W_{N+n}=a_jC_jW_n,\qquad
W_{N-h}=\frac{C_j}{W_{h-1}}\quad(1\le h\le N).
\tag{4.4}
$$

第二式由 $v_2(N-r)=v_2(r)$，$1\le r<N$，直接成立。把 (4.3) 中 $k\le n$ 的部分与 $k=n+h$ 的部分分开，得到**精确**恒等式

$$
\boxed{
\widehat f(2^j+n)-\widehat f(n)
=a_jW_n\sum_{h=1}^{2^j}r_{n+h}W_{h-1}.
}
\tag{4.5}
$$

对固定 $n$，充分大的 $j$ 可应用 (2.5)，再与 (4.5) 的 $n=0$ 情形比较，除以非零的 $a_j$，得到

$$
W_n\sum_{h=1}^{2^j}r_{n+h}W_{h-1}
=\sum_{h=1}^{2^j}r_hW_{h-1}.
\tag{4.6}
$$

(4.2) 及 $\Theta$ 整保证所有极限绝对收敛。令 $j\to\infty$，写

$$
S_n=\sum_{h\ge0}W_hr_{n+h+1},
$$

则

$$
W_nS_n=S_0\qquad(n\ge0).
\tag{4.7}
$$

另一方面，

$$
|W_nS_n|\le CR_0^{n+1}W_n\Theta(R_0)\longrightarrow0
\tag{4.8}
$$

由 $W_n^{1/n}\to0$ 成立。因此 $S_0=0$，(4.7) 又给

$$
\boxed{\sum_{h\ge0}W_hr_{n+h+1}=0\qquad(n\ge0).}
\tag{4.9}
$$

这是使用局部有限性的实质约束；任意有理函数并不自动满足它。

## 5. 卷积方程完整刻画允许的有限零极点

**引理 5.1。** 若一个在 $0$ 解析的有理函数 $R(z)=\sum r_nz^n$ 满足 (4.9)，则

$$
R(z)=c_0+\sum_{\lambda\in E}\frac{c_\lambda}{1-\lambda z},
\qquad E\subset\mathcal Z\text{ 有限}.
\tag{5.1}
$$

特别地，所有极点简单，位置是 $\Theta$ 零点的倒数，而且 $R$ 在无穷远处有界。

**证明。** 对有理函数作部分分式分解，系数具有形式

$$
r_n=p_n+\sum_{\lambda\in E_0}\lambda^nP_\lambda(n),
\tag{5.2}
$$

其中 $(p_n)$ 有有限支撑，$E_0$ 为有限个非零复数，$P_\lambda$ 为非零多项式。$P_\lambda$ 的次数比对应极点的阶数少一。

当 $n$ 大于 $(p_n)$ 的支撑时，(4.9) 给

$$
0=\sum_{\lambda\in E_0}\lambda^{n+1}
\sum_{h\ge0}W_h\lambda^hP_\lambda(n+h+1).
\tag{5.3}
$$

内和是关于 $n$ 的多项式；所需的全部加权 $h$ 矩由 $\Theta$ 为整函数保证绝对收敛。不同非零 $\lambda$ 的多项式指数序列线性无关。一个直接证明是：对指定 $\lambda$，用移位算子 $T$ 作用 $\prod_{\mu\ne\lambda}(T-\mu)^{\deg Q_\mu+1}$，其中 $Q_\mu$ 是当前内和的非零多项式，零项直接略去；它消去其他底数，且在底数 $\lambda$ 的多项式上保留最高次数并把最高系数乘以非零数；因此该多项式也只能为零。

故对每个 $\lambda$，(5.3) 的内和多项式恒为零。设 $P_\lambda(n)$ 的次数为 $d$、最高系数为 $a_d\ne0$。内和的 $n^d$ 系数为

$$
a_d\Theta(\lambda),
$$

因此 $\Theta(\lambda)=0$。若 $d\ge1$，$n^{d-1}$ 系数在这个条件下为

$$
a_dd\sum_{h\ge0}W_h\lambda^h(h+1)
=a_dd\,\lambda\Theta'(\lambda)\ne0,
$$

因为 $\lambda\ne0$ 且引理 1.1 说明零点简单。这是矛盾，所以 $d=0$。于是全部指数项都来自 $\lambda\in\mathcal Z$，且仅有简单极点。

这些常数多项式指数项本身对每个 $n\ge0$ 满足 (4.9)。减去它们后，有限支撑序列 $(p_n)$ 也满足 (4.9)。若存在最大的 $N\ge1$ 使 $p_N\ne0$，取 $n=N-1$ 便得 $p_N=0$，矛盾。因此只有 $p_0$ 可以保留，即有理函数的多项式部至多为常数。这证明 (5.1)。证毕。

**定理 5.2（局部有限有理函数的分类）。**

$$
\boxed{
\mathcal L\cap\mathbb C(z)
=\bigcup_{M\ge0}
\left\{\frac{P(z)}{P_M(z)}:\deg P\le2^M-1\right\}.
}
\tag{5.4}
$$

右边 $M=0$ 表示常数。

**证明。** 若 $\Phi\in\mathcal L$ 有理，§4 和引理 5.1 说明其所有极点简单，并包含在有限多个 $q_j$ 的零点中。选 $M$ 包含这些层，则 $\Phi$ 的分母整除 $P_M$。又 $\Phi$ 在无穷远处有界，所以

$$
\Phi=P/P_M,\qquad \deg P\le\deg P_M=2^M-1.
$$

反之，给定这样一个 $P$，对 $0\le r<2^M$ 定义有限柱函数

$$
v(r)=W_r[z^r]P(z).
\tag{5.5}
$$

由无进位因式分解，

$$
\sum_{n\ge0}\frac{v(n\bmod2^M)}{W_n}z^n
=P(z)\prod_{j\ge M}q_j(z),
$$

除以 $H$ 得到 $P/P_M$。有限柱函数有有限 Walsh 展开，所以其形式表达式属于 $\mathcal L$。证毕。

## 6. 从有限分母回到原 Walsh 支撑

为了排除隐藏的无限支撑表达式，需要补上表示的唯一性。

**引理 6.1。** 若 (2.1) 成立，且 (2.3) 定义的整数数据 $\widehat f$ 只依赖低 $M$ 位，则

$$
c_S=0\qquad\text{对所有 }S\text{ 与 }\{M,M+1,\ldots\}\text{ 相交}.
\tag{6.1}
$$

**证明。** 固定 $j\ge M$。对非负整数 $r$ 翻转第 $j$ 位，记为 $r\triangle2^j$。由 (2.3)，

$$
\widehat f(r\triangle2^j)-\widehat f(r)
=-2\sum_{S\ni j}c_S(-1)^{|S\cap J(r)|}.
\tag{6.2}
$$

左边为零；右边由局部有限性是一个有限 Walsh 多项式。它在全部普通非负整数上为零，而任意有限位的所有赋值都由这样的整数实现，所以有限 Walsh 正交性给全部 $c_S=0$（$S\ni j$）。对每个 $j\ge M$ 重复即得 (6.1)。证毕。

定理 5.2 中 $\Phi=P/P_M$ 与 (2.4) 给

$$
F=P\prod_{j\ge M}q_j.
$$

其第 $n=2^Mk+r$ 个系数乘 $W_n$ 后等于 (5.5)，所以 $\widehat f$ 确实只依赖低 $M$ 位。因此，**任何局部有限表达式代表一个有理函数时，它的原始非零 Walsh 系数也全部只涉及有限多个位。**

结合定理 3.2，得到所需单位分类：

**定理 6.2（局部有限形式单位只有有限位）。** 若 $\Phi,\Psi\in\mathcal L$ 且 $\Phi\Psi=c\ne0$，则二者的局部有限表达式均只有有限支撑。

甚至可把所有非零单位对写明：存在两个互不相交的有限集合 $E_+,E_-\subset\mathcal Z$，满足 $|E_+|=|E_-|$，使

$$
\Phi(z)=\alpha\,\frac{\prod_{\lambda\in E_+}(1-\lambda z)}
{\prod_{\lambda\in E_-}(1-\lambda z)},
\qquad
\Psi(z)=\beta\,\frac{\prod_{\lambda\in E_-}(1-\lambda z)}
{\prod_{\lambda\in E_+}(1-\lambda z)},
\qquad \alpha\beta=c.
\tag{6.3}
$$

确切理由是：$\Phi$ 与 $1/\Phi$ 的极点都简单且只能在 (1.5) 零点的倒数处；二者在无穷远均有界，所以零点数与极点数相同。反过来，任意这样的有限因子比及其逆都由定理 5.2 属于 $\mathcal L$。

它保留此前低两位互逆反例；新增结论是这种零极点搬运不能无穷延伸并仍保持逐位局部有限。

## 7. 任意 L² 局部有限向量的矩分离

回到实际 $L^2$ 向量。设

$$
f=\sum_{S\Subset\mathbb N_0}c_S\chi_S,\qquad
g=\sum_{S\Subset\mathbb N_0}d_S\chi_S
\tag{7.1}
$$

为各自的 $L^2$ Walsh 展开。假设两支撑满足 (2.1)，但不限制 Walsh 次数。定义实际零柱均值

$$
\alpha_m=\int f(2^mz)\,d\mu(z)
=\sum_{S\subset\{0,\ldots,m-1\}}c_S,
$$

$$
\beta_m=\int g(2^mz)\,d\mu(z)
=\sum_{S\subset\{0,\ldots,m-1\}}d_S.
\tag{7.2}
$$

每个和有限。对固定 $m$，柱限制算子从 $L^2$ 到 $L^2$ 有界，范数不超过 $2^{m/2}$，所以这些等式由有限 Walsh 和传到极限合法。

**定理 7.1。** 如果

$$
\alpha_m\to\alpha\in\mathbb C,\qquad
\beta_m\to\beta\in\mathbb C,
\tag{7.3}
$$

且

$$
B(A^nf,g)=0\qquad(n\ge0),
\tag{7.4}
$$

则 $f=0$ 或 $g=0$。

**证明。** 记

$$
h_m(z)=f(2^mz),\qquad k_m(z)=g(2^mz).
$$

对固定非负整数 $r$，局部有限性使充分大的 $m$ 满足精确 $L^2$ 恒等式

$$
f(r+2^mz)=h_m(z)+a_r,\qquad
a_r=\sum_Sc_S\bigl((-1)^{|S\cap J(r)|}-1\bigr).
\tag{7.5}
$$

这是有限项差值：取 $m$ 包含所有与 $J(r)$ 相交的非零支撑项。其余 Walsh 项在两种低位赋值下相同。对固定 $m$ 的有界限制算子保证 $L^2$ 恒等式。同样记 $g$ 的有限差值为 $b_r$。

R40 §2–3 对一般 $L^2$ 向量给：对每个固定 $r\ge0$，

$$
\sum_{i=0}^r\frac{
B_{\rm tail}\bigl(f(i+2^m\,\cdot),g(r-i+2^m\,\cdot)\bigr)}
{W_iW_{r-i}}
\longrightarrow0.
\tag{7.6}
$$

此处截断误差至多

$$
\frac{2^{2m}a_m}{W_{2^m-1}}\|f\|_2\|g\|_2\longrightarrow0.
\tag{7.7}
$$

它不依赖有限 Walsh 次数，也不需要柱限制范数有任何额外界。特别地，取 $r=0$ 得

$$
B_{\rm tail}(h_m,k_m)\longrightarrow0.
\tag{7.8}
$$

将 (7.5) 及 $g$ 的对应式代入 (7.6)，再用 (7.3)、(7.8)，得到

$$
\sum_{i=0}^r
\frac{(\alpha+a_i)(\beta+b_{r-i})-\alpha\beta}
{W_iW_{r-i}}=0.
\tag{7.9}
$$

令

$$
F(z)=\sum_{r\ge0}\frac{\alpha+a_r}{W_r}z^r,\qquad
G(z)=\sum_{r\ge0}\frac{\beta+b_r}{W_r}z^r,
\qquad \Phi=F/H,\quad\Psi=G/H.
$$

引理 2.1 保证 $\Phi,\Psi\in\mathcal L$，而 (7.9) 等价于

$$
\Phi\Psi=\alpha\beta.
\tag{7.10}
$$

若 $\alpha\beta=0$，形式级数环无零因子，所以 $F=0$ 或 $G=0$。以 $F=0$ 为例，$r=0$ 给 $\alpha=0$，所有 $a_r=0$。对每个固定 $j$，(6.2) 的有限 Walsh 差分恒为零，于是所有包含 $j$ 的非空系数消失。遍历 $j$ 得 $f$ 为常数，再由 $\alpha=0$ 得 $f=0$。另一情形同理。

若 $\alpha\beta\ne0$，定理 6.2 迫使 $f,g$ 均为有限柱函数（常数项不受影响，非空支撑已被引理 6.1 排除到有限位内）。因此充分大的 $m$ 有

$$
h_m\equiv\alpha,\qquad k_m\equiv\beta,
$$

从而 $B_{\rm tail}(h_m,k_m)=\alpha\beta\ne0$，与 (7.8) 矛盾。这关闭非零锚分支，定理得证。

## 8. 删除柱均值收敛假设

**定理 8.1（本条最终矩分离定理）。** 设 $f,g\in L^2(\mathbb Z_2)$ 的 Walsh 支撑均逐位局部有限。若

$$
B(A^nf,g)=0\qquad(n\ge0),
\tag{8.1}
$$

则 $f=0$ 或 $g=0$。不假设有限 Walsh 次数、任意柱均值收敛或任意局部迹存在。

**证明。** 沿用 (7.2)、(7.5) 的 $\alpha_m,\beta_m,a_r,b_r$，并令

$$
t_m=B_{\rm tail}(h_m,k_m).
$$

由近整周期零矩，(7.6)、(7.8) 在没有均值收敛的情况下照样成立，所以 $t_m\to0$。

现在引入与锚值无关、常数项为零的形式级数

$$
U(z)=\sum_{\varnothing\ne S}c_S\left(\prod_{j\in S}x_j(z)-1\right),
\qquad
V(z)=\sum_{\varnothing\ne S}d_S\left(\prod_{j\in S}x_j(z)-1\right).
\tag{8.2}
$$

引理 2.1 的 $\alpha=0$ 版本给

$$
\sum_{r\ge0}\frac{a_r}{W_r}z^r=HU,\qquad
\sum_{r\ge0}\frac{b_r}{W_r}z^r=HV.
$$

在 (7.6) 中使用精确共同尾分解 (7.5)，对每个固定阶数 $r$ 得到

$$
[z^r]\left\{H^2(t_m+\beta_mU+\alpha_mV+UV)\right\}
\longrightarrow0.
$$

由于 $H^2$ 是常数项为一的形式单位，乘以它的形式逆时，每个固定系数只使用有限多个较低系数；因此上述逐系数极限等价于

$$
\boxed{\beta_mU+\alpha_mV+UV\longrightarrow0
\quad\text{逐系数}.}
\tag{8.3}
$$

这里先用 $t_m\to0$ 消去了常数项。这个步骤没有假设 $\alpha_m,\beta_m$ 有界，也没有交换任何无限分析极限。

先处理 $U=0$。此时全部 $a_r=0$；引理 6.1 证明中的逐位有限差分使 $f$ 为常数 $c$。若 $c=0$ 已完成；若 $c\ne0$，则 $\alpha_m=c$，(8.3) 迫使 $V=0$。同理 $g$ 为常数 $d$，而 $t_m=cd\to0$ 迫使 $d=0$。$V=0$ 的情形对称。

剩下 $U,V$ 都非零。若它们线性相关，写 $V=\lambda U$，其中 $\lambda\ne0$。令 $d\ge1$ 是 $U$ 的首个非零阶数，$u_d=[z^d]U\ne0$，并置 $s_m=\beta_m+\lambda\alpha_m$。(8.3) 的第 $d$ 阶给

$$
s_mu_d\longrightarrow0,
$$

所以 $s_m\to0$。第 $2d$ 阶再给

$$
s_m[z^{2d}]U+\lambda u_d^2\longrightarrow0,
$$

从而 $\lambda u_d^2=0$，矛盾。因此这个情形不可能。

若 $U,V$ 线性无关，则可选择两个固定正阶 $r,s$，使

$$
\begin{pmatrix}
[z^r]V &[z^r]U\\
[z^s]V &[z^s]U
\end{pmatrix}
$$

可逆。取 (8.3) 的这两个系数，得到该固定可逆矩阵乘 $(\alpha_m,\beta_m)^{\mathsf T}$ 趋于固定向量

$$
-\begin{pmatrix}[z^r](UV)\\[z^s](UV)\end{pmatrix}.
$$

所以 $\alpha_m,\beta_m$ 必分别收敛到有限值。现在定理 7.1 的全部假设都已得到，它给 $f=0$ 或 $g=0$。所有情形均已覆盖，证毕。

记 $\mathscr L_2$ 为 Walsh 支撑逐位局部有限的全部 $L^2$ 向量。它是线性空间，且反射共轭

$$
(Cg)(y)=\overline{g(-1-y)}
$$

保持该类，因为它把 Walsh 系数变为 $(-1)^{|S|}\overline{d_S}$，不改变支撑。因此还得到

$$
\boxed{f,g\in\mathscr L_2,\quad
\langle A^nf,g\rangle=0\ (n\ge0)
\quad\Longrightarrow\quad f=0\text{ 或 }g=0.}
\tag{8.4}
$$

没有额外的 $0$ 柱或 $-1$ 柱均值条件。

## 9. 覆盖范围与保留的假设

1. R55 的有限 chaos、零锚乘积及柱均值收敛条件已全部删除。新类允许无界 Walsh 次数、无限支撑和发散的柱均值；唯一的支撑条件是每个位只涉及有限多个非零 Walsh 系数。
2. 例如 $\sum_j(j+1)^{-1}\chi_j$ 的零柱均值发散，但仍在定理 8.1 中。也允许互不相交有限块上的任意平方可和 Walsh 单项式之和，块大小可以趋于无穷。
3. 不要求在任何整数处存在局部平方均值迹。R55 的二阶弱零但范数不退化例子仍在覆盖范围内；本证明处理的是形式互逆和真实尾配对之间的兼容性。
4. 对不满足局部有限性的有限 chaos，固定低位差分仍可能是非柱的无限尾函数，根单位旋转差未必有理；本条未解决那个分支。
5. $\mathscr L_2$ 含有稠密的柱函数核心，但不能据此把两端均在该类内的矩分离扩张到任意两个 $H$ 向量，也不能宣称该类中每个非零向量循环。一般不变子空间问题仍未解决。
