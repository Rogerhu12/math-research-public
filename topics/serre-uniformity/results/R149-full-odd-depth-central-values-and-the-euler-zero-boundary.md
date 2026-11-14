# R149：全奇数同余深度、中心值整除与多重 Euler 零的精度边界

日期：2026-11-12。

**状态：已证明。** 沿用 R19 的实际非 CM 曲线 $E$、参考曲线 $A:y^2=x^3-x$ 和原素数 $p>37$。令
$$
g=\gcd_{q\mid Z}v_q(Z),\qquad M=pg,
$$
并令 $S$ 为 $q\mid Z$ 中 $E$ 有分裂乘法约化的素数集合，$s=|S|$。记
$$\mathscr L_E=L(E,1)/\Omega_E^+\in\mathbb Q,$$
约定 $v_\ell(0)=+\infty$。R128 已证明 $M$ 的全部素因子模四余三，且 $(M,Z)=1$。

本篇证明，对每个 $\ell\mid M$，令 $n=v_\ell(M)$，则
$$
\boxed{
v_\ell(\mathscr L_E)=0\quad(s=0),\qquad
v_\ell(\mathscr L_E)\ge n\quad(s>0).
}
\tag{149.1}
$$
因此 $s>0$ 且 $\mathscr L_E\ne0$ 时，$M$ 整除 $\mathscr L_E$ 的既约分子；其既约分母与 $M$ 互素。$s=0$ 时该分子、分母均与 $M$ 互素。这推广 R146 的原 $p$ 单位结论到准确的全部奇数同余层。

同时证明两个结构事实：所有乘法符号下，匹配的旧稳定化周期都与 $A$ 的周期相差单位；该旧形式与 $f_E$ 的**完整 Fourier 同余深度恰为 $n$**。虽然旧形式的中心 Euler 乘积含有 $s$ 个至少 $n$ 阶的零因子，(149.1) 不能由这一同余直接加强为 $sn$。本文明确区分这两种精度，不宣称新的统一排除。

## 1. 以真实 Tate 直线选择模 $\ell^n$ 的根

固定 $\ell\mid M$。由 R128，
$$
\ell\equiv3\pmod4,\qquad \ell\nmid 2Z,\qquad
E[\ell^n]\simeq A[\ell^n].
\tag{149.2}
$$
允许 $\ell=3$，也允许 $\ell$ 为 $g$ 的变化大素因子。令 $\mathcal O$ 为 $\mathbb Q_\ell(i)$ 的整数环；这是未分歧二次扩张，仍以 $\ell$ 为一致化元。

对 $q\mid Z$，记
$$\varepsilon_q=a_q(E)\in\{1,-1\}.$$
要选择好约化多项式
$$U^2-a_q(A)U+q=(U-\alpha_q)(U-\beta_q)$$
的根，使
$$\alpha_q\equiv\varepsilon_q\pmod{\ell^n\mathcal O}.\tag{149.3}$$
仅有模 $\ell^n$ 的迹与行列式同余，在重根情形不足以直接保证 (149.3)，所以下面使用完整的实际模块同构。

### 1.1 $q\equiv3\pmod4$

此时 $a_q(A)=0$。Tate 表示的未分歧二次扭曲给 Frobenius 的迹为 $\varepsilon_q(q+1)$，故
$$q\equiv-1\pmod{\ell^n}.$$
多项式 $U^2+q$ 的模 $\ell$ 根 $\varepsilon_q$ 是单根。Hensel 引理给唯一根 $\alpha_q\in\mathbb Z_\ell$ 满足 (149.3)，并令 $\beta_q=q/\alpha_q$。

### 1.2 $q\equiv1\pmod4$

此时 $A$ 的 Frobenius 是高斯整数 $\pi_q\in\mathbb Z[i]$ 或其共轭，满足
$$N(\pi_q)=q,\qquad \pi_q+\overline\pi_q=a_q(A).$$
$A[\ell^n]$ 是 $\mathcal O/\ell^n$ 的自由秩一模。Tate 模块有一个原始循环子模，Frobenius 在其生成元上作用为 $\varepsilon_qq$。经 (149.2) 搬到 $A[\ell^n]$ 后，这个原始生成元是 $\mathcal O/\ell^n$ 的单位：$\ell$ 惰性，非 $\ell$ 倍的坐标恰是该局部环的单位。因此
$$\pi_q\equiv\varepsilon_qq\pmod{\ell^n\mathcal O}.$$
取范数得 $q\equiv q^2\pmod{\ell^n}$；由于 $q$ 可逆，
$$q\equiv1\pmod{\ell^n},\qquad
\pi_q\equiv\overline\pi_q\equiv\varepsilon_q\pmod{\ell^n\mathcal O}.
\tag{149.4}
$$
可选择两根中的任一个为 $\alpha_q$，另一根为 $\beta_q$。这里没有假定 Tate 的商线有一个 Frobenius 本征向量提升；使用的是其实际原始**子线**，最初的本征值为 $\varepsilon_qq$。

以上完整证明 (149.3)，且所有根均可同时放在同一个未分歧二次 $\mathcal O$ 中。

## 2. 同一实际层的旧形式及其原始整周期

置
$$N=32\operatorname{rad}|Z|,
\qquad
h_\ell=\prod_{q\mid Z}(1-\beta_qV_q)f_A.
\tag{149.5}
$$
这是层 $N$ 的归一化全部 Hecke 特征形式，$U_qh_\ell=\alpha_qh_\ell$。与 R146 相同，所有特征零 Satake 根不同，故 $h_\ell$ 的完整 Hecke 特征空间一维。

### 2.1 使用的 Ihara 引理及其范围

对 $q\nmid n\ell$，经典模曲线 Ihara 引理断言
$$
H^1(X_0(n),\mathbb F_\ell)^2_{\mathfrak m}
\longrightarrow H^1(X_0(nq),\mathbb F_\ell)_{\mathfrak m},
\quad (x,y)\longmapsto d_1^*x+d_q^*y
\tag{149.6}
$$
在非 Eisenstein 极大理想处单射。只需残余表示不可约，不要求其像包含 $\mathrm{SL}_2$。

原始证明可核 Ribet，*Congruence relations between modular forms* (1984)，§4、Theorem 4.1、Corollary 4.2：$\Gamma_0$ 退化映射在 Jacobian 上的核包含在两个 Shimura 子群之积中，非 Eisenstein 局部化将其消去。相同的经典模曲线陈述也在 Manning–Shotton (2021) 引言中明确列出。后者关于一般 Shimura 曲线的新大像定理不是本篇输入。

此处每个中间层均为 $32$ 乘某个平方自由数，新增 $q$ 与 $\ell$ 不同，而残余表示为 $A[\ell]$。它在二处的忠实 $Q_8$ 惯性已经保证绝对不可约。故 (149.6) 逐次适用，包括 $\ell=3$；使用的是紧化曲线/Jacobian 的上同调，不因小特征而遗漏群上同调的挠元问题。

### 2.2 逐次保持原始性

先在 $X_0(32)$ 上取 $A$ 的原始整 $+$ Betti 类。其周期与 $\Omega_A^+$ 相差 $\ell$-单位：这是最优商的整同调满射和好约化处 Manin 常数单位的直接积分结论，与 R146 §6 的证明相同。

若 $\delta$ 是当前层对应旧形式的原始整类，则一个稳定化步骤给
$$\delta'=d_1^*\delta-\frac{\beta_q}{q}d_q^*\delta.\tag{149.7}$$
系数 $\beta_q/q$ 是单位。模 $\ell$ 后，(149.6) 把非零向量
$$\left(\overline\delta,-\frac{\overline\beta_q}{q}\overline\delta\right)$$
送到非零类，所以 $\delta'$ 仍原始。归纳得
$$\frac{\omega_{h_\ell}^+}{\Omega_A^+}$$
在 $X_0(N)$ 的相应局部化整格中原始，至多差一个固定单位。这里 $\omega_f=2\pi if(z)\,dz$。

### 2.3 从 $\Gamma_0$ 格到 Vatsal 的 $\Gamma_1$ 格

还须防止 $X_1(N)\to X_0(N)$ 的覆盖度被 $\ell$ 整除时丢失原始性。其 Picard 拉回
$$J_0(N)\longrightarrow J_1(N)$$
的核是 Shimura 子群 $\Sigma(N)$，为常值有限群的 Cartier 对偶。对 $r\nmid N\ell$，Frobenius 在 $\Sigma(N)[\ell]$ 上作用为 $r$，Eichler–Shimura 关系遂给
$$T_r=1+r\quad\text{在 }\Sigma(N)[\ell]\text{ 上}.$$
因此这个核是 Eisenstein。

通过 $H^1_{\mathrm{et}}(-,\mathbb F_\ell(1))\simeq J[\ell]$ 和 Betti 比较，得到
$$H^1(X_0(N),\mathbb F_\ell)_{\mathfrak m}
\hookrightarrow H^1(X_1(N),\mathbb F_\ell)_{\mathfrak m}
\tag{149.8}$$
为单射。此论证不除以覆盖度，也不假定 $\ell\nmid\varphi(N)$。

所以第 2.2 节的旧类在 $\Gamma_1$ 的局部化格中仍原始。Vatsal 的规范类也原始，且其特征空间一维，故
$$\boxed{\mathcal P_{h_\ell}^+/\Omega_A^+\in\mathcal O^\times.}\tag{149.9}$$
这对所有符号 $\varepsilon_q$ 成立，不要求 $s=0$。R146 的单位中心积分法没有引用 Ihara；这里增加 Ihara 正是为了处理中心积分本身可被 $\ell$ 整除的情形。

## 3. 全系数同余具有精确深度 $n$

由 (149.2)、(149.3)，在好约化素数及新增素数处分别有迹同余和 $U_q$ 特征值同余。二处 $U_2=0$。在特征素数 $\ell$，两曲线都好约化；$A$ 的 niveau 二惯性排除 $E$ 普通，故两者都超奇异。对 $\ell\ge7$，有 $a_\ell(E)=a_\ell(A)=0$。

对 $\ell=3$ 不能单凭超奇异性断言迹为零：迹还可能为 $\pm3$。这里利用原始的另一同余：由 R19 有 $3\nmid N_E$，真实 $E[p]\simeq A[p]$ 与 $p>37$ 给
$$a_3(E)\equiv a_3(A)=0\pmod p,$$
而 Hasse 界 $|a_3(E)|\le2\sqrt3<p$ 迫其为零。后一论证覆盖三族而无需再选模型。因此在所有 $\ell\mid M$，
$$a_\ell(E)=a_\ell(A)=a_\ell(h_\ell)=0.$$
Hecke 递推给
$$\boxed{f_E\equiv h_\ell\pmod{\ell^n\mathcal O}.}\tag{149.10}$$

该完整 Fourier 同余不可能模 $\ell^{n+1}$ 仍成立。否则在远离 $2\ell Z$ 的全部素数处，$E$ 与 $A$ 的模 $\ell^{n+1}$ 迹相同。Chebotarev 把这提升为对所有 Galois 元素的迹相同；残余绝对不可约使两个表示同构。

最后一句可直接证明。对 $R=\mathbb Z/\ell^{n+1}$，残余 Burnside 定理及 Nakayama 引理说明每个表示的 $R$-线性包为 $M_2(R)$。若 $\sum a_g\rho_1(g)=0$，用 $\rho_1(h)$ 配对并比较迹，得到
$$\operatorname{tr}\left(\left(\sum a_g\rho_2(g)\right)\rho_2(h)\right)=0\quad\text{对全部 }h.$$
$M_2(R)$ 的迹配对完美，故 $\sum a_g\rho_2(g)=0$。这给出 $M_2(R)$ 的 $R$-代数自同构，将 $\rho_1(g)$ 送到 $\rho_2(g)$；局部环上的矩阵代数自同构为内自同构。因此两表示共轭。

于是 $E[\ell^{n+1}]\simeq A[\ell^{n+1}]$，与 R128 的准确充要条件及 $n=v_\ell(M)$ 矛盾。因此
$$\boxed{\text{(149.10) 的最大整数精度恰为 }n.}\tag{149.11}$$
这与如何选择第 1.2 节的两个高斯根无关。

## 4. 中心值整除

Vatsal 的 prime-to-$\ell$ 规范周期同余定理适用：权二小于 $\ell$，$\ell\nmid N$，残余绝对不可约，两个特征零 Hecke 局部因子均为域。即使 $\ell=3$ 也满足 $2<\ell$。

由 (149.10)，可相容选择规范周期，使
$$
\frac{L(E,1)}{\mathcal P_E^+}
\equiv\frac{L(h_\ell,1)}{\mathcal P_{h_\ell}^+}
\pmod{\ell^n\mathcal O}.
\tag{149.12}
$$
两项均整。另一方面
$$
L(h_\ell,1)=\prod_{q\mid Z}(1-\alpha_q^{-1})L(A,1),
\qquad L(A,1)/\Omega_A^+=1/4.
\tag{149.13}
$$
由 (149.9) 及 R146 §6 的 Néron 周期比较，存在 $u_\ell\in\mathcal O^\times$ 使
$$
\boxed{\mathscr L_E\equiv
\frac{u_\ell}{4}\prod_{q\mid Z}(1-\alpha_q^{-1})
\pmod{\ell^n\mathcal O}.}
\tag{149.14}
$$
这个单位取决于相容周期的选择；不宣称其数值规范。

若 $s=0$，所有根都满足 $\alpha_q\equiv-1\pmod\ell$，右侧为单位，因此 $v_\ell(\mathscr L_E)=0$。

若 $s>0$，至少一处满足 $\alpha_q\equiv1\pmod{\ell^n}$，右侧被 $\ell^n$ 整除，因此 $v_\ell(\mathscr L_E)\ge n$。$\mathscr L_E$ 有理，故从 $\mathcal O$ 的赋值下降至通常的有理数赋值，证明 (149.1)。对所有 $\ell\mid M$ 合并即得分子整除结论。

## 5. 旧 Euler 乘积的准确赋值及不能自动得到的加强

由第 1 节，可以精确计算 (149.13) 的旧 Euler 乘积赋值。非分裂乘法素数贡献零。对 $q\in S$，有
$$
k_{q,\ell}:=v_\ell(1-\alpha_q^{-1})
=\begin{cases}
v_\ell(q+1),&q\equiv3\pmod4,\\[2pt]
\tfrac12v_\ell(q+1-a_q(A)),&q\equiv1\pmod4.
\end{cases}
\tag{149.15}
$$
第一式来自 $\alpha_q^2=-q$、$\alpha_q+1$ 为单位。第二式来自
$$N(1-\pi_q)=q+1-a_q(A)$$
以及 $\ell$ 在高斯域中惰性；范数将其未分歧二次赋值乘二。两式不依赖第 1.2 节的根选择，且 $k_{q,\ell}\ge n$。

因此
$$v_\ell\left(L(h_\ell,1)/\mathcal P_{h_\ell}^+\right)
=\sum_{q\in S}k_{q,\ell}\ge sn.\tag{149.16}$$
但实际新形式与旧形式只已知并且恰好模 $\ell^n$ 同余。故 (149.12) 对 $\mathscr L_E$ 给出的是 $n$，不是 $sn$。例如当 $s\ge2$ 时，抽象整数 $\ell^{sn}$ 与 $\ell^n$ 模 $\ell^n$ 相同，却有不同赋值；该例仅说明推理限制，不声称它们由实际曲线实现。

局部 Tamagawa 因子也须保持准确：对新增分裂乘法素数，
$$c_q(E)=p\,v_q(Z),$$
因此
$$v_\ell\left(\prod_{q\in S}c_q(E)\right)
=\sum_{q\in S}v_\ell(pv_q(Z))\ge sn.\tag{149.17}$$
非分裂乘法处的 $c_q$ 为 $1$ 或 $2$，对奇 $\ell$ 无贡献。旧 Euler 项 (149.15) 衡量参考 CM Frobenius 与 $1$ 的接近程度；Tamagawa 项 (149.17) 衡量实际 Tate 参数的判别式赋值。这是两种不同数据，本文没有证明其逐项相等，也没有从 BSD 猜想反推这种相等。

所以，R50 的实际 Selmer 交替矩阵、(149.16) 的旧中心值和 (149.17) 的实际 Tamagawa 乘积，尚缺一个能控制**新形式超过同余深度的中心值**的全局联系。单纯累乘已知 Euler 零因子不能填上这个缺口。

## 6. 已核来源与适用界限

- K. A. Ribet，**Congruence relations between modular forms**，Proceedings of the ICM (Warsaw, 1983)，PWN (1984)，503–514，§4，尤其 Theorem 4.1、Corollary 4.2，印刷页 511–513。[作者扫描原文](https://math.berkeley.edu/~ribet/Articles/icm.pdf)。经典模曲线退化核只由 Shimura 子群产生。
- J. Manning、J. Shotton，**Ihara’s lemma for Shimura curves over totally real fields via patching**，Mathematische Annalen **379** (2021)，187–234，[原刊全文](https://link.springer.com/article/10.1007/s00208-020-02048-8)。只用其引言重述的经典模曲线 Ihara 引理；不将 Theorem 1.1 的大像假设忽略后套给本题。
- R. Greenberg、V. Vatsal，**On the Iwasawa invariants of elliptic curves**，Invent. Math. **142** (2000)，17–63，§3、Proposition 3.3 及其证明。[作者全文](https://arxiv.org/pdf/math/9906215)。其中 Shimura 子群为常值群的 Cartier 对偶，以及好约化处 Manin 常数比较，供第 2 节使用；不使用普通 Iwasawa 主结论。
- V. Vatsal，**Canonical periods and congruence formulae**，Duke Math. J. **98** (1999)，397–419，§§1.1–1.3、Proposition 1.7、Theorem 1.13。[作者全文](https://personal.math.ubc.ca/~vatsal/research/bah.PDF)。全部系数模 $\ell^n$ 同余给规范中心值的同精度同余。
- 仓库 [R128](R128-all-odd-congruence-depth-and-split-prime-power-exclusion.md)、[R132](R132-maximal-congruence-level-and-split-multiplicative-prime-bound.md)、[R146](R146-nonsplit-multiplicative-support-and-a-unit-central-value.md)：准确深度 $M=pg$、CM 模与 Tate 原始线、规范周期/Néron 周期比较。R149 不以这些结果未提供的高度上界、BSD 等式或 $p$-逆定理为前提。
