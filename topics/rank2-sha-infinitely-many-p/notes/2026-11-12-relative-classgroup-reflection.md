# 2026-11-12：相对类群、有限层 strict Selmer 与固定椭圆单位

**状态：第 1–4 节的比较和充分条件已证明；所需的变化素数上界未证明。** 固定
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
p=\pi\bar\pi\ge13,\quad p\ne17.
$$
沿用 R7 的 $c_p$ 与 $\varepsilon_p$。R12 已完成前一份探索笔记未作的识别：$c_p$ 恰等于单 $\pi$ 除法域的相对类群维数 $r_\pi(E)$，并给出实际同构。

## 1. 类群块就是两个 $p$-局部条件都为零的有限层群

令 $V=E[\pi]$、$L=K(E[\pi])$、$G=\operatorname{Gal}(L/K)$，其作用字符为 $\chi_\pi$。令 $S_K$ 为 $K$ 中位于 $2,17,p$ 上的素点，定义
$$
\mathcal U_\pi=
\{z\in H^1(K,V):z\text{ 在 }S_K\text{ 之外无分歧}\},
$$
$$
\mathcal R_\pi=
\{z\in\mathcal U_\pi:
\operatorname{loc}_{\mathfrak p}z=
\operatorname{loc}_{\bar{\mathfrak p}}z=0\}.
$$
R7 已证明位于 $2,17$ 上的局部 $H^1(K_v,V)$ 本身为零，所以无需另加这两处条件。这里的 $\mathcal R_\pi$ 是有限系数 $V$ 的 strict 群，与 R8 的 $\mathbb Q_p$ 系数对象应加以区分。

**命题。** 限制和全局类域论给出
$$
\mathcal R_\pi\simeq
\operatorname{Hom}_G(\operatorname{Cl}(L),E[\pi]).\tag{1.1}
$$
因此
$$
\dim_{\mathbb F_p}\mathcal R_\pi
=\dim_{\mathbb F_p}\operatorname{Cl}(L)[p]^{\chi_\pi}
=c_p.\tag{1.2}
$$

**证明。** $p\nmid|G|$，故限制将 $H^1(K,V)$ 同构到 $H^1(L,V)^G$。在 $L$ 上系数 $V$ 平凡；在每个有限素点无分歧的同态恰通过 Hilbert 类域，所以对应 $\operatorname{Hom}(\operatorname{Cl}(L),V)^G$。

还需严格核对“在 $L$ 上处处无分歧”与 (1.1) 左边局部条件相同。在 $v\mid p$，局部除法域的分解群 $D_v$ 在 $V$ 上非平凡：$v=\mathfrak p$ 时来自全分歧的 $p-1$ 次除法扩张；$v=\bar{\mathfrak p}$ 时由 R7 的 $E(K_v)[p]=0$。在 $L_w$ 上，平凡系数的无分歧 $H^1$ 是 $\operatorname{Hom}(\widehat{\mathbb Z},V)=V$，其 $D_v$ 作用在无分歧 Frobenius 商上为平凡、在系数上为 $\chi_\pi$。故其 $D_v$-不变部分为零。局部限制又因 $p\nmid|D_v|$ 单射，所以在 $L_w$ 上无分歧恰强迫在 $K_v$ 上局部类为零。

位于 $2,17$ 的局部群已为零；其他素点曲线好约化且与 $p$ 互素，除法域与系数均无分歧，限制保持并反映无分歧条件。各复素点无额外上同调。于是局部条件确实一致。

最后，有限 $p$-群的 $\chi_\pi$ 分量模 $p$ 商与 $p$-挠子群维数相同；取 $G$-等变同态到一维 $\chi_\pi$ 模恰计数这个维数。再用 R12，得到 (1.2)。这里不是不经解释地把类群与其线性对偶规范等同。$\square$

## 2. 两个一维局部缺陷相加恰为 $1$

R7 已给出
$$
\dim\mathcal U_\pi=1+c_p,
\qquad
\operatorname{Sel}_\pi(E/K)
=\ker(\mathcal U_\pi\xrightarrow{\operatorname{loc}_{\bar{\mathfrak p}}}
H^1(K_{\bar{\mathfrak p}},V)).
$$
两个 $p$-局部 $H^1$ 各为一维。把
$$
\delta_p=\operatorname{rank}\left(
\operatorname{loc}_{\mathfrak p}:
\operatorname{Sel}_\pi(E/K)\to H^1(K_{\mathfrak p},V)
\right)\in\{0,1\}
$$
作为第二个缺陷参数。由第 1 节，后一映射的核正是 $\mathcal R_\pi$，故
$$
\dim\operatorname{Sel}_\pi=c_p+\delta_p.
$$
与 R7 的 $\dim\operatorname{Sel}_\pi=1+c_p-\varepsilon_p$ 相比，得到精确关系
$$
\boxed{\varepsilon_p+\delta_p=1.}\tag{2.1}
$$
等价地，$\mathcal U_\pi$ 在两个 $p$-局部 $H^1$ 的直和中的总像始终恰为一维。它不是两个独立的一维局部自由度。

由 R7 已证明的偶性，还得到
$$
\begin{array}{c|c|c|c}
c_p\text{ 奇偶}&\varepsilon_p&\delta_p&\dim\operatorname{Sel}_\pi\\\hline
\text{奇}&0&1&c_p+1\\
\text{偶}&1&0&c_p
\end{array}\tag{2.2}
$$
这把反射/类域论中常见的“相差至多一维”压缩成了具体的局部映射秩；没有引入 $\Sha$ 有限性假设。

## 3. 显式点的非 Wieferich 条件只决定奇偶，尚不决定大小

若任意全局点 $R\in E(K)$ 在 $E(K_{\mathfrak p})/\pi E(K_{\mathfrak p})$ 中非零，则其 Kummer 类使 $\delta_p=1$。于是
$$
\varepsilon_p=0,\qquad c_p\text{ 为奇数},\qquad
\dim\operatorname{Sel}_p(E/\mathbb Q)=c_p+1.\tag{3.1}
$$
对有理点可用一个直接的有限精度条件判定。令 $n_p=\#E(\mathbb F_p)$。R7 已证明 $p\nmid n_p$；乘 $n_p$ 把点送入形式群。形式对数识别 $E_1(\mathbb Q_p)$ 与 $p\mathbb Z_p$，而 $[\pi]$ 的像为 $E_2(\mathbb Q_p)$。因此
$$
R\in\pi E(\mathbb Q_p)
\Longleftrightarrow
\log_E([n_p]R)\equiv0\pmod{p^2}.
$$
定义
$$
q_{E,p}(R)=p^{-1}\log_E([n_p]R)\bmod p.
$$
如果 R4 的 $P=(-1,4)$ 或 $Q=(9,24)$ 中至少一个满足 $q_{E,p}(R)\ne0$，则 (3.1) 成立。这里 $[\bar\pi]$ 在 $E(\mathbb Q_p)$ 上为自同构，所以局部 $\pi$-可除与局部 $p$-可除相同；这就是相应的椭圆 Wieferich 条件。

必须保留两个逻辑区别。第一，$c_p$ 为奇数仍允许 $c_p=3,5,\ldots$，故即使对无穷多个 $p$ 证明这种点的非 Wieferich 性，也**尚未**证明主目标。第二，$P,Q$ 的两个 $q_{E,p}$ 都为零，并不自动给出 $\delta_p=0$：其他 Selmer 类仍可能有非零局部像。反向可无条件断言的是 $c_p$ 为偶数时，所有全局点的局部 Kummer 类均为零。

R8 中非扭点的 $p$-进对数总非零，与本节某个模 $p$ 归一化对数可以为零并不矛盾：非零性与 $p$-进单位性是不同要求。

## 4. 选一个对所有 $p$ 都有效的固定椭圆单位辅助理想

类群上界的另一条实际路线是椭圆单位的指数。这里可以消除“每个 $p$ 另选辅助理想”的变化：固定
$$
\mathfrak a=(7)\subset\mathbb Z[i].
$$
$7$ 在 $K$ 中惰性，曲线在 $7$ 好约化，且 $a_7=0$。最后一点直接来自 $x\mapsto-x$ 与 $\left(\frac{-1}{7}\right)=-1$ 对点数的配对。于是平方 Frobenius 为 $[-7]$，对应 Hecke 角色满足
$$
N\mathfrak a=49,
\qquad\psi(\mathfrak a)=-7,
\qquad N\mathfrak a-\psi(\mathfrak a)=56.
$$
在本笔记的全部素数范围内，$56$ 都是 $p$-进单位；$\mathfrak a$ 也与 $6p\mathfrak f$ 互素，其中 $\mathfrak f$ 是固定 Hecke 导子，支撑仅在 $2,17$。

此辅助理想对应的标准椭圆单位函数甚至可以简写。若 $\Psi_7(x)$ 为标准七除法多项式（首项 $7x^{24}$），$\Delta=64\cdot17^3$，则
$$
\Theta_{E,(7)}(R)=\frac{\Delta^{48}}{\Psi_7(x(R))^{12}}.\tag{4.1}
$$
这是从定义直接化简：非零七挠点的横坐标乘积为
$$
\prod_{T\in E[7]\setminus\{O\}}(x-x(T))
=\left(\frac{\Psi_7(x)}7\right)^2,
$$
再代入 $7^{-12}\Delta^{48}\prod_T(x-x(T))^{-6}$，所有 $7$ 的因子消去。

固定导子生成元 $f$、周期 $\Omega$ 和 $S=\xi(\Omega/f)$。对固定射线类群的 Artin 代表理想 $\mathfrak b$，定义固定的有理函数
$$
\Lambda(R)=
\prod_{\mathfrak b}
\Theta_{E,(7)}\bigl(R+[\psi(\mathfrak b)]S\bigr).
$$
取 $P_\pi=\xi(\Omega/\psi(\mathfrak p))$，得到
$$
\eta_p=\Lambda(P_\pi)\in\mathcal O_L^\times.\tag{4.2}
$$
这里曲线、导子扭点和函数全部固定，只有所代入的 $\pi$-挠点变化。式 (4.2) 是 Rubin 的标准 Euler-system 单位 $\eta_1^{((7))}(\mathcal O_K)$；其为全局单位的结论是下述来源 Proposition 8.2 的一部分。换一个非零 $\pi$-挠点只作 Galois 共轭，因而不改变目标字符分量的 $p$-可除深度。

### 4.1 导子点、范数次数与坏素数处单位性的逐项核查

这里使用的是经过导子点平移并相乘的 $\Lambda(P_\pi)$，不是裸值 $\Theta(P_\pi)$。具体核对如下。

**导子与域。** 本曲线的 Hecke 导子为 $\mathfrak f=2(1+i)17\mathcal O_K$，见 Coates–Liang–Sujatha，*The Tate-Shafarevich group for elliptic curves with complex multiplication*，[arXiv:0901.3832](https://arxiv.org/abs/0901.3832)，Lemma 3.2 及 §3 的 $D=17$ 明示数据。令 $F=K(\mathfrak f)$ 为射线类域，则
$$
[F:K]=\frac{\varphi(\mathfrak f)}4
=\frac{4\cdot16^2}{4}=256.
$$
$F/K$ 在 $\mathfrak p$ 无分歧，而 $L/K$ 在 $\mathfrak p$ 全分歧且次数为 $p-1$（R12）。故 $F\cap L=K$。CM 除法域理论给出 $F,L\subset K(\mathfrak f\mathfrak p)$，射线类群的次数又给出
$$
[K(\mathfrak f\mathfrak p):F]=p-1.
$$
因而 $K(\mathfrak f\mathfrak p)=FL$。

**范数指数。** $S$ 在 $E[\mathfrak f]$ 中为生成元，$P_\pi$ 在 $E[\mathfrak p]$ 中为生成元。因为两理想互素，$S+P_\pi$ 的精确零化理想为 $\mathfrak f\mathfrak p$。$\operatorname{Gal}(FL/L)\simeq\operatorname{Gal}(F/K)$ 固定 $P_\pi$，并使 $S$ 遍历原定义中每一个共轭，恰一次。因此
$$
\eta_p=\Lambda(P_\pi)
=N_{K(\mathfrak f\mathfrak p)/L}
\bigl(\Theta_{E,(7)}(S+P_\pi)\bigr).\tag{4.2a}
$$
没有遗漏单位根轨道造成的第四次幂，也没有额外的 $256$ 次幂：范数群的阶本身就是 $256$，原乘积已经对这 $256$ 个元素各取一次。即使 $S$ 的某些坐标重复，范数与群元素乘积仍带同样的重数。

**在 $2,17$ 处是单位。** Rubin Theorem 7.4(iii) 说明：在与 $\mathfrak a$ 互素、且不是素理想幂的零化理想上，$\Theta$ 的原始值为全局单位。这里 $\mathfrak f\mathfrak p$ 同时含 $2,17,p$ 上的素因子，满足其条件。也可直接检查该证明在坏素数处没有遗漏：$\Theta$ 在曲线同构下不变，故在任意给定坏素点的代数闭包中改用一个好约化模型；CM 曲线具有这种模型。$S+P_\pi$ 保留非零的 $\mathfrak p$-初等部分，因而在剩余特征 $2$ 或 $17$ 处不在形式群中。它与任一非零七挠点之和或差仍保留这个部分，也不在形式群中。所以二者横坐标之差为单位；好模型的判别式和 $7$ 也都是单位，给出 $\Theta(S+P_\pi)$ 的赋值为零。有限域范数保持单位，故 (4.2a) 在 $2,17$ 上仍为单位。其他素点由同一 Theorem 7.4 的计算覆盖，包括辅助素数 $7$。

**常数因子。** $\Delta^{48}$ 不能单独当成全局单位删掉：坏素数处的单位性来自完整比值中的赋值消去。对最终的非平凡字符投影而言，$K^\times$ 中的乘法常数确实消失；这是在 $L^\times\otimes\mathbb Z_p$ 中作
$$
e_{\widetilde\chi_\pi}
=\frac1{p-1}\sum_{g\in G}\widetilde\chi_\pi(g)^{-1}g
$$
后，由 $\sum_g\widetilde\chi_\pi(g)^{-1}=0$ 得到。因为完整的 $\eta_p$ 已证明为单位，其投影才可放回全局单位格中。本笔记的 $z_p$ 始终投影完整 $\eta_p$。

**与 Rubin 的字符及 Euler-system 记号。** Rubin §9 使用 $M^\chi=M(p)\otimes_{\mathbb Z_p[G]}R_\chi$，其中 $g$ 在 $R_\chi$ 上作用为 $\chi(g)$，故它与上述 $e_\chi$ 特征分量一致；Definition 10.7 的 $\chi_E$ 正是在 $E[\mathfrak p]$ 上的作用字符，即本笔记的 $\chi_\pi$，不取倒数。Definition 8.1 在 $n=1,r=\mathcal O_K$ 时恰为 (4.2)，而 Proposition 8.2 及 §8.2 给出其 Euler-system 性质。Theorem 9.5 的 $C_\eta$ 只要求由这个 Euler system 的首项及单位根生成；不要求首项生成“全部椭圆单位”的目标格。故使用 Corollary 9.6 的指数上界，不需要一个尚未核实的全椭圆单位生成元比较。

### 4.2 指数界给出的深度条件

设 $\widetilde\chi_\pi$ 为字符的 Teichmüller 提升，令
$$
\mathscr E_p=
\left((\mathcal O_L^\times/\mu_L)\otimes\mathbb Z_p\right)^{\widetilde\chi_\pi}.
$$
Dirichlet 单位定理给出 $\mathscr E_p\simeq\mathbb Z_p$。记 $z_p$ 为 $\eta_p$ 在此自由秩一模中的投影，以加法记号书写；定义
$$
m_p=\max\{m\ge0:z_p\in p^m\mathscr E_p\},
$$
若 $z_p=0$ 则约定 $m_p=\infty$。这个整数不依赖单位模生成元的选择。

$m_p$ 衡量的是 **$\widetilde\chi_\pi$ 投影之后的 $p$-进单位格**，不是断言原始单位 $\eta_p$ 在整个 $\mathcal O_L^\times$ 中为某个 $p^{m_p}$ 次幂。因此对原始单位的低高度估计，不能不经字符投影比较就用于压低 $m_p$。

Rubin 的椭圆单位 Euler-system 指数界给出
$$
\#\operatorname{Cl}(L)[p^\infty]^{\widetilde\chi_\pi}
\le[\mathscr E_p:\mathbb Z_pz_p]=p^{m_p}
\quad(m_p<\infty).
$$
因此由 R12，
$$
1\le c_p=r_\pi(E)\le m_p.
$$
特别得到一项统一的代数整除结论，以及一条具体的充分条件：
$$
z_p\in p\mathscr E_p\quad\text{对所有所列 }p;
$$
$$
\boxed{\quad
z_p\notin p^3\mathscr E_p
\quad\Longrightarrow\quad
c_p\le2
\quad\Longrightarrow\quad
\Sha(E/\mathbb Q)[p^\infty]=0.
\quad}\tag{4.3}
$$
如果 $z_p=0$，第一项仍然成立，第二项的前提则不成立。本文没有假定指数有限来掩盖这个情形。

这里的完整外部输入是 Rubin，*Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，[作者讲义全文](https://swc-math.github.io/notes/files/99RubinCM.pdf)，Definitions 7.1、7.16、8.1，Proposition 8.2，以及 Theorem 9.5 / Corollary 9.6。所引用的指数界比较的是目标类群的**阶**与单位指数；它没有断言两群同构。

## 5. 为什么反射与单位秩一尚不给变化素数上界

有限层反射已把两个实现中的类群维数完全接起来，并决定唯一的一维局部缺陷。它没有给 $c_p$ 上界：公式
$\dim\operatorname{Sel}_p=2\lceil c_p/2\rceil$
对任意正整数 $c_p$ 都自洽。

单位模秩一也不意味着目标类群循环。即使某个指数公式给出
$$
\#A=p^m=\#(\mathbb Z_p/p^m\mathbb Z_p),
$$
仍可有 $A=(\mathbb Z/p\mathbb Z)^m$。不能从阶相等或 Euler-system 阶的上界，推出 $p$-秩为 $1$。本任务至少还需要控制 $m_p$ 的大小，或引入比零阶指数更细的类群不变量。

固定四次扭转的范数也不提供这个上界。对于四次群 $J$ 的非平凡一维字符 $\eta$，抽象模 $(\mathbb F_p)^m\otimes\eta$ 对任意 $m$ 都具有零不变部分、零范数；因而“基域类群小”和“扩张次数为 $4$”这些已用群论信息并不约束非平凡块的维数。这里并非声称任意此类模都由数域类群实现，而是明确指出现有映射恒等式所缺的算术限制。

剩余的一条具体充分命题是：对无穷多个分裂 $p$，固定函数 (4.1)–(4.2) 产生的单位投影不属于 $p^3\mathscr E_p$。本次尚未证明此命题，也没有把它与通常的点非 Wieferich 条件视为等价。有限个 $p$ 的非消失、同一个 $p$ 的 Euler-system 辅助素数无穷性，以及一个固定 $p$ 的 Iwasawa 变量非消失，都不能替代此处变化 $p$ 的量词。
