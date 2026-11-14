# 固定 E17 的 theta 平方范数与同一 sigma 截面的两个 Mellin 因子

日期：2026-11-12。状态：以下固定对象与因子分解已证明；跨素数的中心简单零点尚未证明。

本笔记使用已发表的 theta 提升公式，把本课题真正的固定四次特征保留下来。结论不是把另一条 CM 曲线的整数平方递推移植过来：存在一个固定代数 sigma 截面，其系数与其复共轭系数的乘积给出所需中央值；在每个普通素数处，它们又给出实际反圆分分支的两个有界 Mellin 因子。这里没有证明两个因子相同，也没有证明它们的中心零点都是简单的。

## 1. 固定记号与结论

沿用 [theta 对角笔记](2026-11-12-anticyclotomic-theta-diagonal.md)：

$$
 E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
 \omega=\frac{dx}{2y},\quad f=34(1+i),\quad Nf=2312.
$$

取正实周期 $\Omega_E$，周期格为 $\Omega_E\mathbb Z[i]$。令 $\sigma_E(z)=z+\cdots$ 为这一格的 Weierstrass sigma 函数。方格情形的 Eisenstein 常数为零，故这就是该笔记采用的 reduced theta；其 Taylor 系数在 $\mathbb Q$ 中。

设 $\psi$ 是本曲线的 Hecke 特征。固定 theta 对角 $d_m$ 及其有理归一化为

$$
 e_m=\frac{d_m}{f^{2m+1}}
 =\frac{(\pi_{\mathbb C}/Nf)^m}{m!\,\Omega_E^{2m+1}}
       L_f(\psi^{2m+1},m+1)\in\mathbb Q.                 \tag{1}
$$

这里复共轭 Hecke 特征的 $L$ 值与右边相等，见上述笔记；$\pi_{\mathbb C}$ 表示实圆周率。本笔记只需 $m\ge0$ 且 $4\mid m$。有限导子在这一组权中恰为 $(f)$。

**结论。** 存在固定的偶整数 $L>0$、固定数域 $M\subset\overline{\mathbb Q}$、固定非零函数 $R\in M(E)$ 及固定正实代数数 $\kappa$，满足：

1. $L$ 的素因子只可能为 $2,17$；记 $d=L^2$。
2. 实际可取 $R=P(x^2)$，其中 $P\in M[X]$ 是固定非零多项式，且 $\deg P\le d/4-1$。
3. 固定整函数

   $$
   S(z)=R(x(z),y(z))\sigma_E(z)^d=\sum_{m\ge0}s_mz^m
                                                              \tag{2}
   $$

   的全部系数属于一个固定数域（扩大 $M$ 后仍记为 $M$）。
4. 对每个 $4\mid m$，

   $$
   \boxed{\displaystyle e_m=
      \kappa(Nf\,d)^{-m}s_m\overline{s_m}.}                    \tag{3}
   $$

复共轭在固定代数系数域上作用；它不表示在某个固定 $p$ 位上的连续自同构。

设 $p\equiv1\pmod4$，$p\ge13$，$p\ne17$，固定 $K\hookrightarrow\mathbb Q_p$ 及 $\pi=\psi(\mathfrak p)$，其中 $v_p(\pi)=1$。令 $\Omega_p\in\mathcal O_{\mathbb C_p}^\times$ 与 theta 对角笔记一致。存在有界测度 $\nu_p,\nu_p^\dagger$ 于 $\mathbb Z_p$，满足

$$
 \int x^m\,d\nu_p=\Omega_p^m m!s_m,\qquad
 \int x^m\,d\nu_p^\dagger=\Omega_p^m m!\overline{s_m}.         \tag{4}
$$

把它们限制到 $\mathbb Z_p^\times$ 后定义

$$
 G_p(T)=\int_{\mathbb Z_p^\times}
    (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}\,d\nu_p(x),
 \quad G_p^\dagger(T)\text{ 同样定义}.                        \tag{5}
$$

这些是有界系数的幂级数。记 $F_p^{\Theta,-}$ 为 theta 对角笔记严格定义的 Katz/Yager 归一化分支。则有整条解析分支的恒等式

$$
 \boxed{\displaystyle
 F_p^{\Theta,-}(T)=\kappa f\Omega_p\,
      (1+T)^{a_p^\circ}\,G_p(T)G_p^\dagger(T),\qquad
 a_p^\circ=\frac{\log_p\langle f^2/d\rangle}{\log_p(1+p)}
         \in\mathbb Z_p.}                                  \tag{6}
$$

上标 $\circ$ 区分这个指数与通常的 Frobenius 迹 $a_p(E)$。常数 $\kappa f\Omega_p$ 非零；除一个固定有限素数集外，它是单位，且两个测度可取整系数。对零点阶，所有所列普通 $p$ 均适用，不需要排除这些额外有限素数。

## 2. 外部已证输入及其准确范围

使用 Tonghai Yang，*Theta liftings and Hecke L-functions*，J. reine angew. Math. **485** (1997), 25–53，作者全文：

<https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。

使用位置是 Theorem 2.6、式 (2.19)，及 Theorem 2.15 对相应局部 Schwartz 向量的存在性。该定理允许 $K=\mathbb Q(i)$，没有“CM 单位都实”或“2 分裂”的假设。有限分裂处的向量是 Corollaries 2.13–2.14 的显式向量；局部调整因子见 Theorem 1.11。所需的复值公式在第 6 节写全。

Yang 的另一篇 *Eigenfunctions of the Weil representation of unitary groups of one variable*，Trans. AMS **350** (1998), 2393–2407，明确只给奇剩余特征的显式 lattice 公式；本证明在 $2$ 处不使用那篇的显式公式，而使用前一篇的一般存在定理及有限平均。

无穷处的规范另有直接一手核对：Yang，*Nonvanishing of central Hecke L-values and rank of certain elliptic curves*，Compositio Math. **117** (1999), 337–359，Lemma 1.1（印刷 p.339）给相应第 $m$ 阶 Hermite 特征向量及范数；Appendix (A3)（p.352）给 unitary splitting 的显式特征因子。全文：

<https://www.cambridge.org/core/services/aop-cambridge-core/content/view/915B51D40C0BD146C3DBC94DE4041BDD/S0010437X99000433a.pdf/nonvanishing_of_central_hecke_lvalues_and_rank_of_certain_elliptic_curves.pdf>。

用于比较的 Nomoto，*The rank of a CM elliptic curve and a recurrence formula*，JNT **238** (2022), 60–81，arXiv:2103.08947，Theorem 2.10 给的是 $y^2=x^3+x$ 的特定平方公式。它不是本证明的 E17 输入。

## 3. 权重变化时有限角色与 Hermitian 空间固定

令

$$
 \chi_m=\psi^{2m+1}\mathrm N^{-m-1/2},\qquad 4\mid m,
 \qquad \eta=1.                                             \tag{7}
$$

这是 unitary Hecke 特征，且 $\chi_m|_{\mathbb A_{\mathbb Q}^\times}
=\epsilon_{K/\mathbb Q}$。其无穷分量为

$$
 (\chi_m)_\infty(z)=(z/|z|)^{-(2m+1)}.                       \tag{8}
$$

### 3.1 有限单位上的限制固定

在 PID $\mathbb Z[i]$ 上，可写

$$
 \psi((\alpha))=\epsilon_f(\alpha)\alpha,
 \qquad \epsilon_f(\alpha)\in\mu_4,
$$

其中有限特征的导子为 $(f)=(1+i)^3(17)$。因 $2m+1\equiv1\pmod4$，所有有限处单位群上的角色与 $\chi_0$ 相同。

在 $2$ 处还有完整局部特征相同。比值 $\chi_m/\chi_0$ 在单位上平凡；对统一化元 $1+i$，由全局主 idèle 关系，其他有限处的比值为 $1$，无穷处的比值为 $i^{-m}=1$。故此比值在 $K_2^\times$ 上恒为 $1$。

在惰性奇素数处，局部特征均未分歧，统一化元 $\ell$ 的值为 $-1$，也不随 $m$ 变化。分裂处允许统一化元上的值变化；后面只用它们在紧单位子群上的固定限制，及 Yang 向量对这一变化的独立性。

### 3.2 局部 dichotomy 可统一取 $\alpha=1$

取 Yang 的纯虚元 $\delta=i$，标准加法特征。在所有未分歧非分裂有限处，局部条件对 $\alpha=1$ 成立；在分裂处范数映射满射，所需局部符号也是 $1$。

无穷处的标准 Schrödinger 模型给出这一点的直接验证。令

$$
 \mathcal H=-\frac1{4\pi_{\mathbb C}}\frac{d^2}{dx^2}
                   +\pi_{\mathbb C}x^2.
$$

以下把取向展开。Yang 的标准基在这里是 $e=\delta=i$、
$f_0=1/(\delta^2\alpha)=-1$。右乘 $g_\theta=e^{i\theta}$ 的矩阵为

$$
 r_\theta=\begin{pmatrix}\cos\theta&\sin\theta\\
                    -\sin\theta&\cos\theta\end{pmatrix},
 \qquad J=\left.\frac{d}{d\theta}r_\theta\right|_0
          =E_+-E_-,
$$

其中 $E_+$、$E_-$ 分别为上、下三角的标准幂零矩阵。取
$\psi_\infty(u)=e^{2\pi_{\mathbb C}iu}$。在与 Yang 分裂处公式
$\phi(x)\mapsto|a|^{1/2}\phi(ax)$ 一致的 Schrödinger 规范中，直接微分两个 unipotent 算子给

$$
 d\omega_\psi(E_+)=\pi_{\mathbb C}ix^2,\qquad
 d\omega_\psi(E_-)=\frac{i}{4\pi_{\mathbb C}}\frac{d^2}{dx^2},
 \qquad d\omega_\psi(J)=i\mathcal H.
$$

单位ary splitting 的特征因子沿 $\theta\in\mathbb R$ 的提升为

$$
 (\chi_m)_\infty(e^{i\theta/2})
       =e^{-i(m+1/2)\theta}.
$$

这里两个半角因子在 $\theta\mapsto\theta+2\pi$ 时同时变号，乘积才是 $G(\mathbb R)$ 的真正作用；这个选择在 $\theta=0$ 为恒等。也可在 $0<\theta<2\pi$ 上由
$(g_\theta-1)/i=2\sin(\theta/2)e^{i\theta/2}$ 核对 splitting 的特征部分。因此

$$
 d\omega_{1,\chi_m}(J)=i(\mathcal H-m-\tfrac12),\qquad
 \omega_{1,\chi_m}(g_\theta)h_n=e^{i(n-m)\theta}h_n.         \tag{8a}
$$

这证明第 $m$ 个 Hermite 函数恰为平凡角色向量。Yang 1999 Lemma 1.1 的 Hermite 及范数公式换成 physicists' $H_m$ 后正是 (9)；该文 (A3) 的 $\chi(i(g_\theta-1))$ 在 $\theta>0$ 足够小时等于 $-e^{-i(m+1/2)\theta}$，其余 Weil-index/Hilbert-symbol 因子局部常数，因此也直接核实上述 Lie 导数。若把全部右作用改记成相反的左作用，$J$ 与 splitting 的角度同时取负，(8a) 的指数整体取负；其不变空间仍恰为 $\mathbb C h_m$，并不允许只改变两个半角中的一个符号。

剩下的 $2$ 处由全局符号确定。$\chi_m$ 的根数等于 $\chi_0$ 的根数：$2$ 处角色完全固定；$17$ 处分裂角色与其逆的 epsilon 因子乘积只依赖 $\chi_{m,17}(-1)$；无穷 epsilon 因子的比值为 $i^{2m}=1$；其他处未分歧。E17 的根数为 $+1$，已在 [局部输入笔记](2026-11-12-cm-local-inputs.md) 证明。局部 dichotomy 符号之积为 $+1$，所以 $2$ 处也为 $1$。

因此同一 $\alpha=1$ 对全部 $4\mid m$ 可用。这里没有从中央值非零倒推局部可行性。

## 4. 可选同一个有限 Schwartz 向量

在 $\mathbb Q_v$ 的标准极化上选取 Yang 的向量。

* 对 $v\ne2,17,\infty$，取 $\phi_v=\mathbf1_{\mathbb Z_v}$。
* 在 $17$ 处，有限导子指数是 $1$。Corollary 2.13 先取
  $17^{1/2}\mathbf1_{1+17\mathbb Z_{17}}$，再用 Corollary 2.14 的固定等距变换 $\rho$ 搬回标准极化。$\rho$ 只依赖固定 $\delta=i,\alpha=1$、加法特征和极化，因此所得 $\phi_{17}$ 不随 $m$ 变化。
* 在 $2$ 处，局部 Weil 表示完全固定。由 Yang 的非分裂局部存在性，选一个平凡角色的单位范数向量 $\phi_2$，以后固定。

有限向量可以取代数值。对 $2$ 处而言，先从局部 Schwartz 空间的特征函数基中取一个在平凡等型分量上投影非零的向量，再对紧群 $K_2^1$ 平均。该向量的轨道是有限集，所以平均是有限和。Weil 作用的有限 Gauss 和、角色值及体积都代数；其正的范数平方也代数，故单位范数归一化只需乘一个代数数。$17$ 处显式有限 Fourier 变换同理。各处的支撑、局部常值模数只含 $2,17$。

无穷处取

$$
 h_m(x)=\frac{2^{1/4}}{\sqrt{2^m m!}}
 H_m(\sqrt{2\pi_{\mathbb C}}x)e^{-\pi_{\mathbb C}x^2},        \tag{9}
$$

其中 $H_m$ 为 physicists' Hermite 多项式，生成式为

$$
 \sum_{m\ge0}\frac{H_m(X)}{m!}t^m=e^{2Xt-t^2}.
$$

由 Hermite 微分方程，$\mathcal Hh_m=(m+\tfrac12)h_m$，且
$\int_{\mathbb R}|h_m|^2dx=1$。这正是第 3.2 节所需的平凡角色单位范数向量。注意指标是 $m$，不是 $2m$；其 $m!$ 规范在后面不能丢掉。

## 5. 类数一把 torus 平均压成固定 theta 权重

令 $G=K^1$，并令

$$
 \mathcal K_f=\prod_v K_v^1\quad(v\text{ 非分裂}),
 \qquad\mathcal K_v=\mathbb Z_v^\times\quad(v\text{ 分裂}),
 \qquad\mathcal K=G(\mathbb R)\mathcal K_f.
$$

因 $\mathbb Z[i]$ 类数一，任意 norm-one 有限 idèle 在分裂素数处的赋值可用一个 $a/\bar a\in G(\mathbb Q)$ 消去；非分裂处赋值本来为零。故

$$
 G(\mathbb A)=G(\mathbb Q)\mathcal K,
 \qquad G(\mathbb Q)\cap\mathcal K=\mu_4.                    \tag{10}
$$

对固定有限向量作归一化紧平均

$$
 \phi_f^{\rm av}=\int_{\mathcal K_f}
                \omega_{1,\chi_0}(k)\phi_f\,dk,
 \qquad \operatorname{vol}(\mathcal K_f)=1.                  \tag{11}
$$

紧群上的 Weil 表示与 $m$ 无关：在分裂处这由 Yang Corollary 2.10 的公式及固定单位角色直接得到；$2$ 处整个表示已固定；其他处向量未分歧。故 (11) 同时适用于全部 $\chi_m$。

存在一个偶整数 $L$（只有素因子 $2,17$），使 $\phi_f^{\rm av}$ 支撑在 $L^{-1}\widehat{\mathbb Z}$，且在加法子群 $L\widehat{\mathbb Z}$ 下不变。扩大同一个 $L$ 可以同时满足两个条件。于是

$$
 a_n=\phi_f^{\rm av}(n/L)\in\overline{\mathbb Q},
 \qquad a_{n+L^2}=a_n.                                      \tag{12}
$$

所有 $a_n$ 在同一数域中。

设 $V=\operatorname{vol}(G(\mathbb Q)\backslash G(\mathbb A))$。由 (10)、无穷向量的平凡角色性质及绝对收敛，Yang 的 theta 平均满足

$$
 \frac{\theta_{h_m\otimes\phi_f}(1)(1)}{V}
       =A_m:=\sum_{n\in\mathbb Z}a_nh_m(n/L).                \tag{13}
$$

这一步保留了原曲线在 $17$ 处的四次角色；它通过固定向量 $\phi_{17}$ 及平均权重 $a_n$ 进入公式。

## 6. 全部复常数与 Hermite 阶乘

Yang Theorem 1.11 的集合在此为 $S_1=\varnothing$、$S_2=\{17\}$，导子指数 $1$，所以

$$
 c(0)=17^{-1}(1-17^{-1})^{-2}=\frac{17}{256}.                \tag{14}
$$

该文 (1.16) 所用、记作 $\operatorname{Tam}(G)$ 的体积比是
$\operatorname{vol}(\mathcal K)/V$。由 (10) 直接得此比为 $4$。这里按该文写出的体积比计算，不另外替换 Haar 或 Tamagawa 规范。

其式 (2.19) 因而给出

$$
 L_f(\psi^{2m+1},m+1)
  =\frac{2L(1,\epsilon_{K/\mathbb Q})}{4c(0)}|A_m|^2
  =\frac{32\pi_{\mathbb C}}{17}|A_m|^2.                    \tag{15}
$$

定义同一个整函数

$$
 B(t)=e^{-t^2}\sum_{n\in\mathbb Z}a_n
       \exp\!\left(-\pi_{\mathbb C}(n/L)^2
                    +2\sqrt{2\pi_{\mathbb C}}(n/L)t\right)
      =\sum_{m\ge0}b_mt^m.                                 \tag{16}
$$

在紧集上可逐项微分。由 (9)，

$$
 A_m=2^{1/4}\sqrt{m!/2^m}\,b_m,
$$

所以

$$
 L_f(\psi^{2m+1},m+1)
  =\frac{32\sqrt2\pi_{\mathbb C}}{17}\cdot
                  \frac{m!}{2^m}|b_m|^2.                    \tag{17}
$$

目前只对 $4\mid m$ 使用 (15)–(17)。这足以覆盖所有目标 $m=p-1$ 和 R40 的全部测试权。

## 7. 固定有限 theta 基的代数性

写 $d=L^2$、$T=\sqrt{\pi_{\mathbb C}/2}\,L$。由 (12) 换指标，(16) 满足

$$
 B(t+T)=e^{2Tt+T^2}B(t),\qquad
 B(t+iT)=e^{-2iTt+T^2}B(t).                                  \tag{18}
$$

令 $c=T/\Omega_E$。因 $d$ 为偶数，$B(cz)$ 与 $\sigma_E(z)^d$ 有相同的两条准周期律。因此它们的比是椭圆函数，只可能在 $O$ 有阶数至多 $d$ 的极点。

还要证明这个椭圆函数除一个共同非零复标量外具有代数系数；仅有准周期律不够。

对 $r\in\mathbb Z/d\mathbb Z$ 定义

$$
 B_r(t)=e^{-t^2}\sum_{n\equiv r\ (d)}
   \exp\!\left(-\pi_{\mathbb C}(n/L)^2
                +2\sqrt{2\pi_{\mathbb C}}(n/L)t\right).
$$

这 $d$ 个函数线性独立，且 $B=\sum_ra_rB_r$，$a_r$ 代数。令 $a=T/d$，取归一化平移

$$
 \mathcal X F(t)=e^{-2at-a^2}F(t+a),\qquad
 \mathcal Y F(t)=e^{2iat-a^2}F(t+ia).
$$

直接换指标得

$$
 \mathcal X B_r=B_{r-1},\qquad
 \mathcal Y B_r=\zeta_d^rB_r,\qquad
 \mathcal X^d=\mathcal Y^d=1,
 \quad\mathcal X\mathcal Y=\zeta_d\mathcal Y\mathcal X.        \tag{19}
$$

缩放到 $E$ 后，这些平移覆盖两个代数 $d$ 挠点。线丛 $\mathcal O_E(dO)$ 的平移同构可取代数：它们由挠点对应的主除子有理函数给出。把各同构的 $d$ 次幂归一化为 $1$ 只需开一个代数 $d$ 次根。解析同构 (19) 与这种代数同构之比是常数；两者的 $d$ 次幂均为 $1$，故这个比是代数根单位。因此 (19) 本身在代数截面空间上作用。

取 $\mathcal Y$ 的特征值 $1$ 的一个非零代数特征向量，再逐次用 $\mathcal X$ 得到代数基。交换式说明这些特征值互异，共有 $d$ 个；由于 $\dim H^0(E,\mathcal O_E(dO))=d$，每个特征空间维数恰为一。解析基 $B_r(cz)$ 与该代数基的相对比例由 $\mathcal X$ 强制相同，故只有一个共同非零复标量 $C$。

于是存在 $R\in\overline{\mathbb Q}(E)$，只在 $O$ 有阶至多 $d$ 的极点，使

$$
 B(cz)=C R(x(z),y(z))\sigma_E(z)^d=C S(z).                   \tag{20}
$$

有限个有理函数系数生成一个数域。由 $E$ 的有理不变量、$\sigma_E$ 的有理 Taylor 系数及 (20) 在 $O$ 的正则性，全部 $s_m$ 属于该同一个数域。

函数非零可由已证 R40 得到：若所有 $4\mid m$ 的中央值都为零，任取一个普通 $p$，R40 的 $m=(p-1)p^n$ 插值值全零，且相应参数趋于中心，迫使其非零解析分支恒为零，矛盾。因而至少一个这样的 $b_m$ 非零。

### 7.1 四次对称性将 $R$ 降为 $x^2$ 的多项式

这一点不需把 (17) 扩展到其他权。用固定全局特征 $\chi_0$ 考察 theta 分布
$\mathscr T(\phi)=\sum_{x\in\mathbb Q}\phi(x)$。有限向量 $\phi_f^{\rm av}$ 在紧群下不变，特别是

$$
 \omega_{1,\chi_0,f}(i)\phi_f^{\rm av}=\phi_f^{\rm av}.
$$

由 (8a)，$\omega_{1,\chi_0,\infty}(i)h_n=i^nh_n$。全局 theta 分布在 $G(\mathbb Q)$ 的全局 splitting 下不变。因此对 $\phi=h_n\otimes\phi_f^{\rm av}$，有严格的张量等式

$$
 \mathscr T(\phi)=\mathscr T\bigl(\omega_{1,\chi_0}(i)\phi\bigr)
                =i^n\mathscr T(\phi),
 \quad\text{即}\quad
 \sum_x\phi_f^{\rm av}(x)h_n(x)
   =i^n\sum_x\phi_f^{\rm av}(x)h_n(x).
$$

因此 $b_n=0$ 除非 $4\mid n$，即 $B(it)=B(t)$。由 $d=L^2\equiv0\pmod4$ 和 $\sigma_E(iz)=i\sigma_E(z)$，得到 $R([i]P)=R(P)$。

固定域 $M(E)^{\langle i\rangle}=M(x^2)$。又因 $R$ 没有有限极点，它在 $x^2$ 上没有有限分母，所以 $R=P(x^2)$ 为多项式。$x^2$ 在 $O$ 的极点阶为四，故 $\deg P\le d/4$。第 8 节给 $s_0=0$；而次数恰为 $d/4$ 的项在 $P(x(z)^2)\sigma_E(z)^d$ 中贡献唯一的非零常数项。因此实际上 $\deg P\le d/4-1$，且 $S(iz)=S(z)$。

## 8. 固定代数常数与系数范数公式

由 (20)，$b_mc^m=Cs_m$。代入 (17)，再代入 (1)，$m!$ 与尺度精确消去，得到

$$
 e_m=\frac{32\sqrt2\pi_{\mathbb C}|C|^2}{17\Omega_E}
       (Nf\cdot d)^{-m}s_m\overline{s_m}\qquad(4\mid m).          \tag{21}
$$

取一个已知存在的非零系数 $e_{m_0}$，令

$$
 \kappa=
   \frac{e_{m_0}(Nf\cdot d)^{m_0}}{s_{m_0}\overline{s_{m_0}}}.
$$

它是正的非零代数数，且由 (21) 与 $m$ 无关，故得到 (3)。这里不需要单独识别超越标量 $C$；也没有按 $m$ 重新选择标量。

已知 $e_0=0$，因此 $s_0=0$。但这只给后面测度的总质量为零，不直接给其在 $\mathbb Z_p^\times$ 上的质量为零。

## 9. 普通处的有界测度来自同一个 sigma 截面

本曲线在全部所列普通 $p$ 的 Mazur–Tate sigma 是同一个固定有理级数

$$
 \Sigma(t)=\sigma_E(\log_E t),
$$

且 $\Sigma(t)\in t\mathbb Z_p[[t]]$，见
[固定 sigma 与高度笔记](2026-11-12-fixed-sigma-height-and-inert-denominator.md)。

把 $R\in L(dO)$ 写成椭圆曲线的 Riemann–Roch 基的线性组合：基元是极点阶不超过 $d$ 的 $x^j$ 和 $yx^j$。它们在 $t$ 中为整系数 Laurent 级数，极点阶至多 $d$。所以

$$
 S(\log_E t)=R(x(t),y(t))\Sigma(t)^d
$$

是有界系数的正则幂级数；除固定有限多个素数外它整。其复共轭系数版本同理。

普通正式群同构

$$
 t=\exp_E\bigl(\Omega_p\log(1+Z)\bigr)
$$

具有整系数，$\Omega_p$ 为单位。因此

$$
 \mathcal A_p(Z)=S\bigl(\Omega_p\log(1+Z)\bigr),\qquad
 \mathcal A_p^\dagger(Z)=\overline S\bigl(\Omega_p\log(1+Z)\bigr)
                                                                  \tag{22}
$$

有界。由 Amice 对应定义 $\nu_p,\nu_p^\dagger$。对 (22) 作用 $(1+Z)d/dZ$ 的 $m$ 次幂并在零处取值，即得 (4)。$\overline S$ 仅共轭固定代数系数；两边使用同一个 $\Omega_p$，没有把某个 $p$-进周期错误地作复共轭。

## 10. 从精确复公式到整条 Katz 分支：去掉 $p$-支撑的误差

对正整数 $m\equiv0\pmod{p-1}$，theta 对角笔记的精确插值式是

$$
 F_p^{\Theta,-}(t_m)=\Omega_p^{2m+1}(m!)^2(Nf)^m
        \left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2d_m,
 \qquad t_m=(1+p)^m-1.                                      \tag{23}
$$

结合 $d_m=f^{2m+1}e_m$、(3)、(4)，记 $b=f^2/d\in K^\times$，得到

$$
 F_p^{\Theta,-}(t_m)
 =\kappa f\Omega_p\cdot b^m
  \left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2
  M_m M_m^\dagger,                                         \tag{24}
$$

其中 $M_m=\int_{\mathbb Z_p}x^m d\nu_p$。有限的 $m!$ 已全部保留在测度的矩里。

存在一个依赖 $p$、不依赖 $m$ 的常数 $B_p$，使测度范数至多 $p^{B_p}$。所以

$$
 v_p\!\left(M_m-\int_{\mathbb Z_p^\times}x^m d\nu_p\right)
      \ge m-B_p,                                           \tag{25}
$$

共轭版本亦然；Euler 因子与 $1$ 的差也有赋值至少 $m$。因此 (24) 与把两个矩都限制到单位、并把两个 Euler 因子换成 $1$ 的表达式之差，在 $m\to+\infty$ 时趋于零，其赋值至少 $m-O_p(1)$。

固定任意非负整数 $m_0\equiv0\pmod{p-1}$，取

$$
 m_n=m_0+(p-1)p^n.
$$

这列整数实趋于无穷、$p$-进趋于 $m_0$。在单位部分，矩连续趋于 $G_p(t_{m_0})$ 与 $G_p^\dagger(t_{m_0})$。因为 $b\in\mathbb Q_p^\times$ 是单位，且 $m_n\equiv0\pmod{p-1}$，

$$
 b^{m_n}=\langle b\rangle^{m_n}
 \longrightarrow(1+t_{m_0})^{a_p^\circ}.
$$

令 (24) 中 $n\to\infty$，得到 (6) 在每个 $t_{m_0}$ 的取值。再取 $m_0=(p-1)p^j$，这些互异点趋于零，解析恒等定理即给出整条幂级数恒等式 (6)。

这是共同测度与共同权参数上的比较。误差趋于零的论证只移除单位区间之外的测度支撑及已写出的 Euler 因子，没有逐值选择新的周期或不定标量。

## 11. 已得到什么，仍缺什么

由 (6) 和 theta/Katz 与 R40 分支的共同单位比较，所有目标普通 $p$ 都有

$$
 \operatorname{ord}_{T=0}F_p^-
   =\operatorname{ord}_{T=0}G_p
    +\operatorname{ord}_{T=0}G_p^\dagger.                    \tag{26}
$$

两个因子均不恒零。R40 因此给出精确判据

$$
 \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
 \iff \operatorname{ord}_0G_p+\operatorname{ord}_0G_p^\dagger=2.
                                                                  \tag{27}
$$

除固定有限素数外，(3) 又给出目标系数的精确赋值分解

$$
 v_p(d_{p-1})=v_p(s_{p-1})+v_p(\overline{s_{p-1}}).          \tag{28}
$$

以上仍没有证明 (27) 在无穷多个 $p$ 成立。特别是：

* $s_0=0$ 给 $\nu_p(\mathbb Z_p)=0$，不能略过 $p\mathbb Z_p$ 部分而宣称 $G_p(0)=0$。
* 固定系数的复共轭会改变所选 $p$ 位，因此 (28) 不能在未证明额外实结构时写成 $2v_p(s_{p-1})$。
* 一般 theta 提升的非零判据与中央 $L$ 值非零等价；它本身不提供所需的中心简单零点。
* (2) 已经给出一个固定代数对象，但其 Mellin 中心仍取决于变化的普通素数、正式群同构与单位区间投影。固定对象不自动意味着这些中心由一个固定有限 Galois 表示的 Frobenius 元素决定。

可以继续实际研究的对象已从变化的高阶 Kronecker 双导数改成两个固定 sigma 截面的 Mellin 因子；尚待的新算术输入是它们在无穷多个普通素数处的总中心零阶恰为二，或等价地为 R40 提供非零二次项。
