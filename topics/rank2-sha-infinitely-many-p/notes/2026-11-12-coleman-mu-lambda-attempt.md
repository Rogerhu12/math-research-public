# 固定 Coleman 函数的 μ、λ 与人为中心因子

**日期：2026-11-12。可信度：第 1–5 节为已证明结论；第 6 节明确记录尚未闭合的路线。**

固定 $E:y^2=x^3-17x$、$K=\mathbb Q(i)$，始终设
$$
p\ge13,\qquad p\equiv1\pmod4,\qquad p\ne17.
$$
沿用 R20 的 $\pi_E=\psi(\mathfrak p)$、$K_n=K(E[\mathfrak p^n])$、$\Delta\times\Gamma$、$\rho_E$、$\widetilde\chi$、$e_\chi$，并固定
$$
\rho_E(\gamma)=1+p,\qquad \mathcal A_p=\mathbb Z_p[[T]],\qquad T=\gamma-1.
$$
令 $\Phi\in K(E)^\times$ 为 R19 的固定函数。已完成的 [Coleman 塔笔记](2026-11-12-phi-coleman-tower.md) 证明
$$
\varepsilon_n=\Phi(P_{\pi^n})\in\mathcal O_{K_n}^\times,
\qquad N_{n+1,n}\varepsilon_{n+1}=\varepsilon_n,
$$
以及 $e_\chi\varepsilon_\infty$ 生成 $C_\infty^\chi$。取 R20 的自由局部单位格生成元 $u_\infty$，写
$$
e_\chi\varepsilon_\infty=H_p(T)u_\infty.
$$
这里 $H_p$ 与 R20 的 $h_p$ 只差一个 $\mathcal A_p$ 单位，因此
$$
H_p=(T-p)^2G_p,\qquad
\nu_p=v_p(H_p(0))=2+v_p(G_p(0)).\tag{0.1}
$$
全局单位及定位的非零性已由 [字符非零性笔记](2026-11-12-unit-character-nonvanishing.md) 证明，所以本式中的赋值有限。这里的 $G_p$ 与 R20 的 $g_p$ 也只差单位。

## 1. 既有定理确实给出所有这些 p 的 μ=0

**命题 1。** 对全部上述 $p$，
$$
\mu(H_p)=\mu(G_p)=0.\tag{1.1}
$$

**证明。** Schneps 的论文开头定义
$$
F_\infty=K(E[\mathfrak p^\infty]),\qquad
X_\infty=\operatorname{Gal}(M_\infty/F_\infty),
$$
其中 $M_\infty$ 是 $F_\infty$ 的极大阿贝尔 pro-$p$ 扩张，且只允许在 $\mathfrak p$ 以上分歧。其 Theorem IV 证明 $\mu(X_\infty)=0$。论文的条件是 $K$ 类数一、$E/K$ 有 $\mathcal O_K$ 复乘、$p>3$ 为分裂好素数；全部适用于这里。

因此这正是 R20 所用的单个 $\mathfrak p$ 除法塔及 $X_\infty$，不需要将 cyclotomic 塔的定理转移过来。$\Delta$ 的阶是 $p-1$，全部字符值在 $\mathbb Z_p$ 中；整幂等元给出 $X_\infty$ 的字符直和分解。每块的 $\mu$ 非负，而直和的 $\mu$ 是其和，故 $\mu(X_\infty^\chi)=0$。R20 的主定理比较
$$
\operatorname{char}_{\mathcal A_p}(X_\infty^\chi)=(H_p)
$$
给出 $\mu(H_p)=0$。最后 $\mu(T-p)=0$，由乘积的 $\mu$ 可加性和 (0.1)，得到 $\mu(G_p)=0$。$\square$

这条定理消除了“整个级数的系数都有额外 $p$ 因子”这一可能性；它没有指定第一个单位系数的位置，更没有给出 $G_p(0)$ 的单位性。

**一手出处。** L. Schneps, *On the μ-invariant of p-adic L-functions attached to elliptic curves with complex multiplication*, Journal of Number Theory **25** (1987), 20–33，§0–1 的对象与假设、Theorem IV（p.30，证明至 p.33）；[作者全文](https://webusers.imj-prg.fr/~leila.schneps/Schnepsmu.pdf)，[DOI](https://doi.org/10.1016/0022-314X(87)90013-8)。Oukhaba–Viguié, *On the μ-invariant of Katz p-adic L functions attached to imaginary quadratic fields and applications*, Theorems 1.1–1.2，[arXiv:1311.3565](https://arxiv.org/abs/1311.3565)，还陈述并推广相同的单素数分歧塔结论；本命题只需 Schneps 的已发表结果。

## 2. 任意层数的固定有理函数变形

Hecke 导子为 $\mathfrak f=(34(1+i))$。取固定整数
$$
a=69.
$$
由于 $a-1=68=34(1+i)(1-i)$，有 $a\equiv1\pmod{\mathfrak f}$，从而 $\psi((a))=a$。$a$ 的素因子 $3,23$ 都是 $K/\mathbb Q$ 中的惰性素数，所以任何所列 $p$ 都不整除 $a$。

对满足 $F(O)=1$ 的有理函数定义
$$
\mathcal D_aF(P)=\frac{F([a]P)}{F(P)^a},
\qquad
\Phi_r=\mathcal D_a^r\Phi\quad(r\ge0).\tag{2.1}
$$
这里 $r$ 是预先固定的非负整数，$\Phi_r$ 不随 $p$ 改变。显式地，
$$
\Phi_r(P)=
\prod_{j=0}^{r}\Phi([a^j]P)^{\binom rj(-a)^{r-j}}.\tag{2.2}
$$
特别地，$\Phi_2=\Phi\circ[a^2]\cdot\Phi^{a^2}/(\Phi\circ[a])^{2a}$。

**命题 2。** 每个固定 $r$ 都有以下性质：

1. $\Phi_r\in K(E)^\times$ 非常数，$\Phi_r(O)=1$，且 $\Phi_r(-P)=\Phi_r(P)^{-1}$。
2. 在每个所列 $p$ 处，$\Phi_r(t)\in1+t^3\mathbb Z_p[[t]]$，其中 $t=-x/y$ 是原固定模型的参数。
3. 所有 $\Phi_r(P_{\pi^n})$ 都是全局单位，组成范数相容系统。
4. 固定 $r$ 后，这些代数单位的绝对对数高度有不依赖 $p,n$ 的上界。

**证明。** (2.2) 直接给出有理性、在 $O$ 的值与奇性。乘法形式群幂级数 $[a](t)$ 在好素数处整，故 R19 的 $\Phi(t)\in1+t^3\mathbb Z_p[[t]]$ 给出第 2 条。对整系数且常数项为一的幂级数，任意正、负整数次幂仍整，因此 (2.2) 中的负指数没有引入分母。

证明非恒定性时，在特征零取形式对数参数 $z$，写
$$
\log\Phi(\exp_E z)=\sum_{k\ge3}b_kz^k.
$$
$\Phi$ 非常数且在 $O$ 正则、值为一，所以存在某个 $k\ge3$ 满足 $b_k\ne0$。由 $[a]\exp_Ez=\exp_E(az)$，
$$
\log\Phi_r(\exp_Ez)
=\sum_{k\ge3}(a^k-a)^rb_kz^k.\tag{2.3}
$$
因 $a>1$，所有 $k\ge3$ 都有 $a^k-a\ne0$，故这个级数非零，$\Phi_r$ 非常数。

令 $\sigma_a$ 为 $(a)$ 在 $K_\infty/K$ 的 Artin 元。CM 互反律及 $a\equiv1\pmod{\mathfrak f}$ 给出
$$
\sigma_aP_{\pi^n}=[a]P_{\pi^n}.
$$
因此 (2.2) 的每个因子都是已知全局单位 $\Phi(P_{\pi^n})$ 的 Galois 共轭。单位性成立；Galois 作用与范数交换，故这些乘积仍范数相容。

也可直接核对分布式。因 $p\nmid a$，$[a]$ 双射置换 $E[\mathfrak p]$，从原分布式得到
$$
\prod_{Q\in E[\mathfrak p]}(\mathcal D_aF)(P+Q)
=\frac{F([\pi_E][a]P)}{F([\pi_E]P)^a}
=(\mathcal D_aF)([\pi_E]P).
$$
迭代即得 $\Phi_r$ 的精确分布式，常数始终为一。

最后，固定有理函数在椭圆曲线上的高度估计给出
$h(\Phi_r(R))\le A_r\widehat h_E(R)+B_r$，只要取值不是零或极点。这里全部 $R=P_{\pi^n}$ 为挠点，且已经证明取值为单位，所以 $\widehat h_E(R)=0$。因此高度至多 $B_r$，与 $p,n$ 无关。$\square$

## 3. 精确的局部深度和 Iwasawa 因子

定义
$$
\zeta_p=\omega_p(a)\in\mu_{p-1},\qquad
\langle a\rangle_p=a/\zeta_p,\qquad
b_p=\frac{\log_p\langle a\rangle_p}{\log_p(1+p)}\in\mathbb Z_p.
$$
$b_p\ne0$：若为零，则 $a$ 是 $\mathbb Q_p$ 中的根单位；一个大于一的有理整数不可能具有有限乘法阶。令
$$
\kappa_p=v_p(b_p)
=v_p(a^{p-1}-1)-1\ge0.\tag{3.1}
$$
最后一个等式由 $\log$ 在 $1+p\mathbb Z_p$ 上保持赋值及 $v_p\log(1+p)=1$ 得到。

在 $\chi$ 分量上，$\sigma_a-a$ 对应
$$
q_p(T)=\zeta_p(1+T)^{b_p}-a
=\zeta_p\bigl((1+T)^{b_p}-(1+p)^{b_p}\bigr).
\tag{3.2}
$$
因此
$$
e_\chi\bigl(\Phi_r(P_{\pi^n})\bigr)_n
=q_p(T)^rH_p(T)u_\infty.\tag{3.3}
$$
在第一层 $T=0$，故若 $\nu_{p,r}$ 表示该变形函数的局部深度，
$$
\boxed{\quad
\nu_{p,r}=\nu_p+r(\kappa_p+1)\ge2+r.
\quad}\tag{3.4}
$$
所有这些深度有限，因为 $q_p(0)=\zeta_p-a\ne0$，且原来的 $\nu_p$ 有限。

**命题 3。** $q_p$ 满足
$$
\mu(q_p)=0,
\qquad \lambda(q_p)=p^{\kappa_p},
\qquad \operatorname{ord}_{T=p}q_p=1.\tag{3.5}
$$
因此
$$
\mu(q_p^rH_p)=0,
\qquad
\lambda(q_p^rH_p)=\lambda(H_p)+rp^{\kappa_p}.\tag{3.6}
$$

**证明。** 写 $b_p=p^{\kappa_p}d_p$，$d_p\in\mathbb Z_p^\times$。模 $p$ 的连续幂级数恒等式给出
$$
(1+T)^{b_p}
\equiv(1+T^{p^{\kappa_p}})^{d_p}\pmod p.
$$
又 $(1+p)^{b_p}\equiv1\pmod p$，故 $q_p\bmod p$ 的第一个非零系数出现在 $T^{p^{\kappa_p}}$，其系数为 $\bar\zeta_p\bar d_p\ne0$。这同时证明 $\mu=0$ 及所述 $\lambda$。而
$$
q_p(p)=0,\qquad
q_p'(p)=\zeta_pb_p(1+p)^{b_p-1}\ne0
$$
证明中心零点恰为一阶。乘积的 $\mu,\lambda$ 可加，结合命题 1 即得 (3.6)。$\square$

另一方面，(2.3) 对每个 $k$ 给出准确的矩公式
$$
\delta^k\log\Phi_r(O)
=(a^k-a)^r\delta^k\log\Phi(O).
\tag{3.7}
$$
在 $k=p$ 处，$v_p(a^p-a)=\kappa_p+1$。故对数矩的深度也统一增加 $r(\kappa_p+1)$，与第一层单位的增加完全一致。

## 4. 这不是实际曲线的反例：失去的正是原始生成元

原系统 $e_\chi\varepsilon_\infty$ 生成 $C_\infty^\chi$。而对 $r\ge1$，变形系统只生成
$$
q_p(T)^r C_\infty^\chi
\subsetneq C_\infty^\chi.\tag{4.1}
$$
包含是严格的：$q_p(0)$ 被 $p$ 整除，所以 $q_p$ 是局部环 $\mathcal A_p$ 的非单位；$C_\infty^\chi$ 是秩一自由模，乘以非零非单位不可能满射。特别地，(3.6) 的新 $\lambda$ 是 $U_\infty^\chi/q_p^rC_\infty^\chi$ 的不变量，不能当成原 $X_\infty^\chi$ 的不变量。

于是对每个预先给定的深度阈值 $B$，取 $r\ge\max(0,B-2)$，便得到一个仍然固定、非常数、在挠点给全局单位、满足原范数分布、整性、统一高度界且 $\mu=0$ 的有理函数；其局部深度对所有所列 $p$ 都至少 $B$。这些一般性质不足以推出无穷多个 $p$ 的深度小于 $4$。

这不否定原 $\Phi$ 的目标，也不证明具有原始椭圆单位生成元性质的函数可以如此变形。相反，(4.1) 精确指出变形丢失了哪项算术条件。固定函数在 $K(E)^\times\otimes\mathbb Q$ 中能否由 $[a]^*-a$ 除出的除子障碍，由主会话的 R22 单独处理；本笔记不从这种固定函数原始性推断逐 $p$ 的 $G_p(0)$ 上界。

## 5. λ 小可以给更弱但足够的有限性判据

**命题 4。** 若某个所列 $p$ 满足
$$
\lambda(H_p)\le3,
\quad\text{即}\quad \lambda(G_p)\le1,
\tag{5.1}
$$
则 $\Sha(E/\mathbb Q)[p^\infty]$ 有限。

**证明。** R20 的 extended Selmer 比较与中心长度界给出
$$
2\le s_p^\infty
\le\operatorname{ord}_{T=p}H_p
\le\lambda(H_p),
$$
其中 $s_p^\infty$ 是有理 $p^\infty$-Selmer 群的 $\mathbb Z_p$ 余秩。最后一项成立是因为 $\mu(H_p)=0$，Weierstrass 分解的 distinguished polynomial 次数为 $\lambda(H_p)$，而幂级数单位在 $T=p$ 非零。R7 使用的 $p$-parity 定理以及 $E$ 的根数 $+1$ 给出 $s_p^\infty$ 为偶数。故 (5.1) 强迫 $s_p^\infty=2$，与已知代数秩相等，初级部分有限。$\square$

这个路线比 R16 的小深度条件更宽，但仍需一个真正的跨素数 $\lambda$ 上界。以下形式例子准确区分三个条件，例子不声称来自本椭圆曲线：

后续 [R25](../results/R25-lambda-controls-finite-selmer.md) 已证明 $\dim\operatorname{Sel}_p\le\lambda(H_p)$，因此这里 $\lambda(H_p)\le3$ 的结论可加强为整个初级部分为零。加强依赖原始 $X_\infty^\chi$ 没有非零有限子模，不能对仅有同一特征理想的任意模直接使用。

- $H(T)=(T-p)^4$ 有 $\mu=0,\lambda=4$，仍允许大于二的中心零点阶。因此 $\mu=0$ 本身不推出有限性。
- 对任意 $N\ge1$，$H(T)=(T-p)^2(T+p^N)$ 有 $\mu=0,\lambda=3$，中心零点恰为二阶，但 $v_pH(0)=N+2$ 可任意大。因此小 $\lambda$ 不等价于小局部深度。
- 当 $\mu(G_p)=0$ 时，$v_pG_p(0)$ 大只说明常数系数被高次 $p$ 整除；第一个单位系数可能在 $T$ 项，也可能更后。不能从 $G_p(0)\equiv0\pmod{p^2}$ 推断 $\lambda(G_p)\ge2$。

## 6. Mellin 变换路线目前保留的具体问题

Schneps 的 §1–2 写出一个在 $p$ 处依赖于曲线和普通素数的形式群同构
$$
\beta_p:\widehat{\mathbb G}_m\longrightarrow\widehat E,
\qquad w\longmapsto\beta_p(w).
$$
将固定椭圆有理函数的展开 $R(t)$ 改写成 $R(\beta_p(w))$ 后才得到乘法形式群上的测度；再取随 $p$ 改变的 tame 字符与 $\Gamma$-transform。$R(t)$ 在固定 $t$ 中有理，并不说明 $R(\beta_p(w))$ 是次数一致有界的 $w$ 的有理函数。Schneps 的 Theorem I–III 使用椭圆形式乘法的代数独立性来证明模 $p$ 的非零性，Theorem IV 给出上面已经应用的 $\mu=0$；此处尚未从这些定理得到 $\lambda(G_p)\le1$ 的无穷性。

Rosenberg, *On the Iwasawa invariants of the Γ-transform of a rational function*, Journal of Number Theory **109** (2004), 89–95，[DOI](https://doi.org/10.1016/j.jnt.2004.06.016)，还给出 rational-function Γ-transform 的 $\lambda$ 上界。其原文暂未取得，但已有可核对的后续一手结果：Anglès, *On the p-adic Leopoldt transform of a power series*, Acta Arithmetica **134** (2008), 349–367，[arXiv:0709.2838](https://arxiv.org/abs/0709.2838)，导言转述 Rosenberg 对 conductor $p$ 的 Dirichlet 分支给出 $(4p(p-1))^{\varphi(p-1)}$ 上界，并在自身 Theorem 4.5(2) 证明 conductor 的素于 $p$ 部分为 $d$ 时
$$
\lambda(f(T,\theta))<
\left(\frac{p-1}{2}\varphi(d)\right)^{\varphi(p-1)}.
$$
这个上界随 $p$ 增长，而且其对象是 Dirichlet cyclotomic 分支。这里既没有把它移用于 CM 分支，也没有把它误读为固定常数上界。关于本 $R(\beta_p(w))$ 甚至不代数于 $K_p(w)$ 的严格障碍，另见主会话的 R23。

另一项真实但仅负责传递的定理是 Lei–Loeffler–Zerbes, *On the Asymptotic Growth of Bloch–Kato–Shafarevich–Tate Groups of Modular Forms over Cyclotomic Extensions*, Canadian Journal of Mathematics **69** (2017), 826–850，Proposition 2.2，[DOI](https://doi.org/10.4153/CJM-2016-034-x)。在其 cyclotomic Mellin 规范化下，若
$$
\mathfrak M(g)=(1+z)\varphi(f),\qquad
f\in\mathcal O[[z]],\quad g\in\mathcal O[[\Gamma_1]],
$$
则 $\mu(g)=\mu(f)$ 且 $\lambda(g)=\lambda(f)$。比较的是先去掉 $(1+z)$ 和 Frobenius 后的 $f$，并不是把 $\mathfrak M(g)$ 本身与 $g$ 视为具有同一个 $z$-阶数。其证明来自 Loeffler–Zerbes, *Wach modules and critical slope p-adic L-functions*, Proposition 7.2，[arXiv:1012.0175](https://arxiv.org/abs/1012.0175)：相同关系给出 $0<s<1$ 的 Newton 函数 $v_s(f)=v_s(g)$。它能传递一个已经得到的 $\lambda$ 界；目前本题还没有满足所需小上界的 $f$。

下一实际目标是识别原始 $\Phi$ 在 Mellin 模 $p$ 下第一个单位系数的位置，或证明一个固定有限曲线集合中至少一个对应 $\lambda\le3$ 的素数有无穷多个。仅有 $\mu=0$、函数非恒定、固定极点和原始生成元的名称，都尚未给出这个量化结论。
