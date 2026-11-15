# R694 — 原 Kummer 根的复乘下降、完整稳定子及单一域迹

日期：2026-11-15。**状态：已证明。** 主课题仍未完成。

本篇确定 R691 留下的实际稳定子：对每个允许的惰性素数，
它都是整个范数一群 H。原指定根全部已经在完整 p 除点域 F 中；
R691 的不分歧 Kummer 扩张因而平凡。这里的输入是原除点函数，
不是类数假设，也不是重新选择的一组形式根。

证明先将相对根放进一个明确的阿贝尔除点域，再用 H 上的 Kummer 配对
和增广模消去它们。原边界和由此成为一条全 H 域迹。
这关闭了“实际 J 是否最小”的问题，但没有证明该迹非零或原中央传播。

## 1. 原符号和结论

沿用 R688/R691：
$$
p=6s-1>101,\quad d=p+1,\quad q=p^2,\quad
K_0=\mathbf Q(\omega),\quad E:y^2=x^3+17,
$$
$$
F=K_0(E[p]),\qquad
\operatorname{Gal}(F/K_0)=\mathbf F_q^\times,\qquad
H=\ker\operatorname{Norm}_{\mathbf F_q/\mathbf F_p}.
$$
因此 $|H|=d$、$\mu_p\subset F$、$F^H=K_0(\mu_p)$，H 在 $\mu_p$ 上作用平凡。
保原
$$
\alpha=\omega^2+p\omega,\quad \nu=p^2-p+1,\quad n=p+1,
\qquad
a_T=\psi_\alpha(T)^{2s}/\psi_n(T)^{2s-1}.
\tag{1}
$$
$\psi_\alpha$ 和偶 $\psi_n$ 都是原 sigma 归一；特别不改偶除点式的符号。

R691 的实际根、cocycle 和 Kummer 模为
$$
r_{h,T}=\zeta_hP_{\zeta_h}(u_T),\qquad
r_{h,T}^{\,p}=a_T/a_{hT},\qquad
r_{hk,T}=r_{h,T}\,h(r_{k,T}),
\tag{2}
$$
$$
D_T=\langle(1-h)[a_T]:h\in H\rangle_{\mathbf F_p}
\subset F^\times/F^{\times p},\qquad
M_T=F(r_{h,T}:h\in H).
\tag{3}
$$
所有根仍是原有限 jet 指定的根，$\zeta_h$ 仍仅先在 $K_p$ 中解释。

**定理。** 对每个上述 p 和每个非零 $T\in E[p]$，
$$
\boxed{D_T=0,\qquad M_T=F,\qquad
J_T=\operatorname{Stab}_H[a_T]=H,\qquad r_{h,T}\in F.}
\tag{4}
$$
此外，若 $G(T)=T_g(u_T)$ 为原完整规范值，则
$$
\boxed{G(T)^d=-\prod_{h\in H}r_{h,T}\in F^\times.}
\tag{5}
$$
故单个实际值满足
$$
\boxed{[\mathbf Q(G(T)):\mathbf Q]\le 2(p+1)(p^2-1).}
\tag{6}
$$
不把这个单值次数界直接用于全部正阶 jet 或任意合成域。

## 2. 固定复嵌入和原 Klein 因子

为证明代数域包含，暂取一个复嵌入。仍使用原代数不变微分对应的
sigma 函数，不作依 p 的变换。
其周期格为
$$
\Lambda=\Omega(\mathbf Z\omega+\mathbf Z).
$$
令 $\eta_\lambda$ 为 Weierstrass zeta 的准周期，并将
$\lambda\mapsto\eta_\lambda$ 从格唯一实线性延拓到整个 $\mathbf C$。

原 sigma 满足 $\sigma(\omega z)=\omega\sigma(z)$，从其对数导数得
$\eta_{\omega\lambda}=\omega^{-1}\eta_\lambda$。
实线性延拓遂满足同式。写 $\eta_z=A z+B\bar z$，则
$A\omega=A\omega^{-1}$，故 $A=0$。于是
$$
\boxed{\eta_z=B\bar z,\qquad
\eta_{\beta z}\,\beta z=N(\beta)\eta_z z
\quad(\beta\in K_0).}
\tag{7}
$$
这里 $B$ 可以含周期；仅使用反线性关系，不宣称它是代数数。

定义
$$
\mathfrak k(z)=\exp(-\eta_z z/2)\sigma(z).
\tag{8}
$$
这是固定格上的 Klein 因子。它不是一个在整个复平面上任意取幂的
新的 p 进解析规范；下文只用它比较原除点函数的有限挠点值。

由 sigma 准周期公式，若 $\lambda\in\Lambda$，则
$$
\mathfrak k(z+\lambda)
=\chi(\lambda)
 \exp\!\left(\frac{\eta_\lambda z-\eta_z\lambda}{2}\right)
 \mathfrak k(z),
\qquad \chi(\lambda)\in\{\pm1\}.
\tag{9}
$$
取 $z=(a\omega_1+b\omega_2)/p$、$\lambda=m\omega_1+n\omega_2$，
Legendre 关系将指数中的交错积化为 $2\pi i$ 的 $\frac1{2p}$ 整数倍。
因此
$$
z\in p^{-1}\Lambda
\ \Longrightarrow\
\mathfrak k(z+\lambda)/\mathfrak k(z)\in\mu_{2p}.
\tag{10}
$$
相位可以有 p 部分，本篇没有把它当作与 p 互素的根单位。
同一原六次对称还给
$$
\mathfrak k(\omega^2 z)=\omega^2\mathfrak k(z).
\tag{11}
$$

取非零挠点 T 的任一复代表 $z_T\in p^{-1}\Lambda\setminus\Lambda$。
由于 $[\alpha]T=[\omega^2]T$、$[n]T=T$，
存在 $\lambda_\alpha,\lambda_n\in\Lambda$ 使
$$
\alpha z_T=\omega^2z_T+\lambda_\alpha,\qquad
n z_T=z_T+\lambda_n.
$$
原除点归一给
$$
\psi_\alpha(T)=\frac{\sigma(\alpha z_T)}{\sigma(z_T)^\nu},
\qquad
\psi_n(T)=\frac{\sigma(nz_T)}{\sigma(z_T)^{n^2}}.
\tag{12}
$$
由 (7)，把 sigma 换成 (8) 时两个指数因子**准确消去**，故
$$
\psi_\alpha(T)=\xi_{\alpha,T}\omega^2
                   \mathfrak k(z_T)^{1-\nu},
\qquad
\psi_n(T)=\xi_{n,T}\mathfrak k(z_T)^{1-n^2},
\quad \xi_{\alpha,T},\xi_{n,T}\in\mu_{2p}.
\tag{13}
$$
(12) 的首系数与偶式已经由 R684/R688 支付，不在此改用 monic 多项式。

准确 Bezout 指数是
$$
2s(1-\nu)-(2s-1)(1-n^2)
=-p\{2s(p-1)-(2s-1)(p+2)\}=-p.
$$
所以
$$
\boxed{a_T=\xi_T\mathfrak k(z_T)^{-p},\qquad \xi_T\in\mu_{6p}.}
\tag{14}
$$
换代表只改变相位，(14) 左边始终是原代数数。

## 3. Klein 比属于明确的阿贝尔除点域

令
$$
N=12p^2,\qquad A=K_0(E[N]).
$$
对两个非零 p 挠点 T,U，写
$z_T=\Omega(a_T^\circ\omega+b_T^\circ)$、
$z_U=\Omega(a_U^\circ\omega+b_U^\circ)$，
其中两对有理数的 primitive denominator 都是 p。
圆圈上标仅表示有理坐标，与 (1) 的 $a_T$ 无关。

按 [S] §2.2.2 的规范，Klein form 和 Siegel function 满足
$$
t_{\mathbf a}(\Omega\omega,\Omega)=
\Omega t_{\mathbf a}(\omega),\qquad
h_{\mathbf a}(\tau)=2\pi\eta(\tau)^2t_{\mathbf a}(\tau)
=-i\,g_{\mathbf a}(\tau).
$$
因此共同周期和 eta 因子在比中消去：
$$
\boxed{
\frac{\mathfrak k(z_U)}{\mathfrak k(z_T)}
=\frac{t_{\mathbf a_U}(\omega)}{t_{\mathbf a_T}(\omega)}
=\frac{g_{\mathbf a_U}(\omega)}{g_{\mathbf a_T}(\omega)}.}
\tag{15}
$$
没有在 (15) 取额外 $12p$ 次根。

[JKS] Lemma 2.3(i) 给出：primitive denominator 为 p 的
$g_{\mathbf a}$ 本身就是级 $12p^2$ 的 modular unit，
其 Fourier 系数在 $\mathbf Q(\zeta_{12p^2})$。
不是仅仅 $g_{\mathbf a}^{12p}$ 属于某个模函数域。

为避免误用 [JKS] 后文排除 $K_0=\mathbf Q(\sqrt{-3})$ 的生成定理，
这里直接证明本题所需的有限值包含。完整层模曲线
$Y(N)/\mathbf Q(\zeta_N)$ 在 $N\ge3$ 表示带给定 Weil pairing
的完整 N 层结构；见 [M] Proposition 59、§3.9。
在原 E 上取由 $\Omega\omega/N,\Omega/N$ 给出的有序层结构。
其两点都在 A，且 Weil pairing 给 $\zeta_N\in A$。
故这一定义的 $Y(N)$ 点在 A 上有理。

级 N、Fourier 系数在 $\mathbf Q(\zeta_N)$ 的模函数，
是该标准模曲线模型上的有理函数。这也可由标准 cusp 的 q-expansion
下降判据看出：Galois 共轭具有相同展开则是同一有理函数。
当函数在这个点有限，其值属于点的剩余域 A。
Siegel 函数在上半平面没有零极，故 (15) 的分子分母均可评价，得到
$$
\frac{\mathfrak k(z_U)}{\mathfrak k(z_T)}\in A^\times.
\tag{16}
$$
使用完整层结构后，j=0 的额外自同构不造成评价的例外。

最后，原 E 的所有 $\mathbf Z[\omega]$ 复乘均在 $K_0$ 定义。
由复格描述
$$
E[N]\simeq N^{-1}\Lambda/\Lambda
\simeq\mathbf Z[\omega]/N
$$
是自由秩一 $\mathbf Z[\omega]/N$ 模。
$K_0$ 的 Galois 作用与这个作用交换，因此
$$
\operatorname{Gal}(A/K_0)
\hookrightarrow(\mathbf Z[\omega]/N)^\times
$$
是阿贝尔群。这是本题的直接除点域证明，不需要 ray class field
恰由某个特定 Weber 函数生成。

从 (14) 对 T,U 相除，
$$
\frac{a_T}{a_U}
=\frac{\xi_T}{\xi_U}
 \left(\frac{\mathfrak k(z_U)}{\mathfrak k(z_T)}\right)^p.
\tag{17}
$$
$\xi_T/\xi_U\in\mu_{6p}$ 的**任一** p 次根都在 $\mu_{6p^2}$；
而 $6p^2\mid N$，所以这些根单位都在 A。
结合 (16)，(17) 的每个 p 次根都在 A：
$$
\boxed{\{x:x^p=a_T/a_U\}\subset A.}
\tag{18}
$$
因此 (18) 尤其包含 R691 指定的原局部根，而非只包含某个新选的复根。
在固定代数闭包里换复嵌入只运输同一代数包含，不改变其 p 进分支。

## 4. 阿贝尔性和增广模迫使所有 H 根下降

(18) 给 $F\subset M_T\subset A$。
A/$K_0$ 阿贝尔，因此 $M_T/F^H$ 亦为阿贝尔扩张。
特别，H 对 $\operatorname{Gal}(M_T/F)$ 的共轭作用平凡。

同时 H 固定 $\mu_p$。由准确 Kummer 配对
$$
D_T\times\operatorname{Gal}(M_T/F)\longrightarrow\mu_p,
\qquad ([u],\sigma)\longmapsto
\sigma(u^{1/p})/u^{1/p},
$$
及其 H 等变性、非退化性，H 对 $D_T$ 也作用平凡。
这一步同时使用了扩张阿贝尔性和 $\mu_p$ 的平凡作用，
不能只用后者。

另一方面，在 $F^\times/F^{\times p}$ 上置
$$
\mathcal N_H=\sum_{h\in H}h.
$$
由于 H 为群，对每个 k 有
$\mathcal N_H(1-k)[a_T]=0$。
所以 $\mathcal N_H D_T=0$。
而 H 在 $D_T$ 上平凡又给
$\mathcal N_H|_{D_T}=d\,\mathrm{id}$。
因 $p\nmid d=p+1$，乘 d 在 $\mathbf F_p$ 上可逆，于是 $D_T=0$。

Kummer 对偶遂给 $M_T=F$，每个原 $r_{h,T}$ 都在 F，
且实际 $J_T=H$。这证明 (4)。
R691 的不分歧性质仍然正确；本篇将其具体商确定为平凡商，
没有推断 $\operatorname{Cl}(F)[p]$ 本身为零。

## 5. 原完整规范的 d 次幂和正确根

R688 的原等式为
$$
G(hT)=G(T)/P_{\zeta_h}(u_T)
=\frac{\zeta_hG(T)}{r_{h,T}},
\qquad
\prod_{h\in H}G(hT)=1.
$$
H 与 $\mu_d$ 的原局部对应保全部 d 个根。d 为偶数，故
$\prod_h\zeta_h=-1$。将上式逐项相乘即得 (5)，再用
$[F:K_0]=p^2-1$ 得 (6)。

这里不是宣称 $G(T)\in F$，也没有把局部 $\mu_d\subset K_p$
错误放进 F；只在完整乘积中消去了它们。
$d$ 与 p 互素，(5) 的不同根之比为 $\mu_d$。
原单位邻域中至多有一个这样的根。
存在性由原 $G(T)$ 给，所以仍可保 R681 的
$v_p(G(T)-\tau_d(u_T))>1/(p-1)$ 原选根条件。
不增加任何可自由指定的相位。

原 R688 的 pd 次幂公式由 (5) 再取 p 次幂立即恢复：
$$
\left(-\prod_h r_{h,T}\right)^p
=-\prod_h(a_T/a_{hT})
=-a_T^d/\operatorname{Norm}_{F/F^H}(a_T).
$$
偶式的负号与新公式准确相容。

## 6. 现在真正剩下的是全 H 迹

因全部原 $r_h$ 在 F 且满足 (2)，Hilbert 90 给
$b_T\in F^\times$，使
$$
r_{h,T}=b_T/h(b_T).
\tag{19}
$$
可仍用 R691 的显式构造
$b_T=\sum_{h\in H}r_{h,T}\,h(c)$，
为某个 $c\in F$ 该和非零；存在性由不同域自同构的线性独立性给出。
所以没有附加“找不到 b”条件。

对原两个固定 $m=34,72$ 与原 $\phi_m$，
$$
\boxed{
\sum_{h\in H}r_{h,T}^{\,m}\phi_m(hT)
=b_T^m\,
 \operatorname{Tr}_{F/F^H}\!\left(b_T^{-m}\phi_m(T)\right).}
\tag{20}
$$
原边界的完整关系为
$$
v_T^{\,d-m}\mathcal B_m(v_T^d)
=\frac{G(T)^{-m}b_T^m}{d}
 \operatorname{Tr}_{F/F^H}\!\left(b_T^{-m}\phi_m(T)\right).
\tag{21}
$$
每个外因子均非零。故原边界为零准确等价于这一条指定迹为零。
仍须对全部 $p-1$ 个 H 轨道保 (21)，没有删掉非首轨道。

(19) 还给 $b_T^p/a_T\in F^H$；
b 的另一选择只乘 $(F^H)^\times$，所以迹的零判定不变。

R691 的条件命题“若 $J=\mu_6$ 则边界非零”保留其逻辑正确性；
但在本题实际 $p>101$ 中，(4) 给 $J=H$、$|H|>6$，
该充分条件的假设不成立。因此 open 中不再寻找“实际 J 最小”或
以 p 类数单位性迫使该条件；接下来处理的是 (20) 的真实迹。

**尚未证明：** (20) 在无穷多个 p 非零，或原中央 $j=0$
迫全部边界余数消失。R663 的 X 下降仍需原 $j=0$ 与
$Q^{d-m}\mid\mathcal B_m$ 等完整条件。此次下降不自动支付这些条件，
也不把一个阿贝尔域中的迹叫作新的算术中央零。

## 依赖与可核来源

- [R684](R684-original-division-orbit-phase-and-uniform-height.md)：
  同一 CM sigma 除点式及其首系数。
- [R688](R688-full-division-field-phase-cancellation-and-original-kummer-sums.md)：
  原全除点域、完整轨道积、偶除点负号、准确 p 次根及全部边界和。
- [R691](R691-original-unit-kummer-field-and-stabilizer-trace-criterion.md)：
  原 cocycle、Kummer 配对、稳定子和显式 Hilbert 90 迹。
- [S] M. Streng, *Generators of the group of modular units for
  $\Gamma^1(N)$ over the rationals*, Annales Henri Lebesgue 6 (2023), 95–116，
  §2.2.2、(2.3)、Lemma 2.13：
  [期刊全文](https://numdam.org/item/10.5802/ahl.160.pdf)。
  这里只用 Klein/Siegel 的规范、齐次性与变换式。
- [JKS] H. Y. Jung, J. K. Koo, D. H. Shin,
  *Application of Weierstrass units to relative power integral bases*,
  Rev. Mat. Iberoam. 30 (2014), 1489–1498，§2 的 $F_N$ 定义、
  Lemma 2.3(i)：
  [出版社全文](https://ems.press/content/serial-article-files/38521?nt=1)。
  使用的是一般模函数引理，未使用其 §3–4 排除本 CM 域的定理。
- [M] H. Darmon，F. Gispert 记录，
  *Complex multiplication*, 2020，Proposition 59、§3.9：
  [课程官方讲义](https://www.math.mcgill.ca/darmon/courses/20-21/cm/francesc-notes.pdf)。
  使用完整层结构的模曲线；本篇另写出本题除点域阿贝尔性的直接证明。
- sigma 准周期及 Legendre 规范：
  [NIST DLMF §23.2](https://dlmf.nist.gov/23.2)，
  与 (9) 的实线性延拓相配。

本篇为一般 p 的符号证明，无辅助素数扫描、数值猜测或待执行证书。
