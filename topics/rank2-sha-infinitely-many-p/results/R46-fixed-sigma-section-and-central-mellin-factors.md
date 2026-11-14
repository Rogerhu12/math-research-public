# R46. 固定 sigma 截面及中央分支的两个 Mellin 因子

日期：2026-11-12。**状态：已证明；各因子的中心零阶尚未确定。**

## 1. 结论

固定 $E:y^2=x^3-17x$、$f=34(1+i)$、$Nf=2312$，
并沿用 $e_m=d_m/f^{2m+1}\in\mathbb Q$。
存在一个固定偶整数 $L$、数域 $M$、非零多项式 $P\in M[X]$
及正实代数数 $\kappa$，满足：

- $L$ 只有素因子 $2,17$；记 $d=L^2$。
- $\deg P\le d/4-1$。
- 固定整函数
  $$
  S(z)=P(x(z)^2)\sigma_E(z)^d=\sum_{m\ge0}s_mz^m
  $$
  的全部系数属于 $M$，且 $s_m=0$ 除非 $4\mid m$。
- 对每个 $m\ge0$、$4\mid m$，
  $$
  \boxed{e_m=\kappa(Nf\,d)^{-m}s_m\overline{s_m}.}
  \tag{1}
  $$

对每个 $p\equiv1\pmod4$、$p\ge13$、$p\ne17$，
固定本课题使用的嵌入 $K\hookrightarrow\mathbb Q_p$ 和普通周期 $\Omega_p$。
同一个 $S$ 及其系数共轭定义两个有界测度 $\nu_p,\nu_p^\dagger$：
$$
\int_{\mathbb Z_p}x^m\,d\nu_p=\Omega_p^m m!s_m,\qquad
\int_{\mathbb Z_p}x^m\,d\nu_p^\dagger=\Omega_p^m m!\overline{s_m}.
\tag{2}
$$
记其限制到单位区间的 principal Mellin 变换为
$$
G_p(T)=\int_{\mathbb Z_p^\times}
 (1+T)^{\log_p\langle x\rangle/\log_p(1+p)}\,d\nu_p(x),
$$
$G_p^\dagger$ 同样定义。则实际 Katz/Yager 中央分支满足
$$
\boxed{
F_p^{\Theta,-}(T)=\kappa f\Omega_p
 (1+T)^{a_p^\circ}G_p(T)G_p^\dagger(T),\qquad
a_p^\circ=\frac{\log_p\langle f^2/d\rangle}{\log_p(1+p)}.
}
\tag{3}
$$
$a_p^\circ\in\mathbb Z_p$，常数 $\kappa f\Omega_p$ 非零；
除固定有限素数外它是单位，且两个测度为整测度。

由 R40 与完整 theta/Katz 单位比较，得到准确判据
$$
\boxed{
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\iff \operatorname{ord}_0G_p+\operatorname{ord}_0G_p^\dagger=2.
}
\tag{4}
$$
所有所列普通 $p$ 均适用 (3)–(4)，不必为零阶判据排除测度的有限分母。

## 2. 固定有限向量及复 theta 公式

以下各步的全部局部规范、常数和证明见
[固定 theta 平方范数证明](../notes/2026-11-12-fixed-sigma-theta-square-factorization.md)；
这里给出从已发表输入到 (1)–(4) 的完整论证链。

令
$$
\chi_m=\psi^{2m+1}\mathrm N^{-m-1/2},\qquad4\mid m.
$$
它限制到 $\mathbb A_{\mathbb Q}^\times$ 为二次特征
$\epsilon_{K/\mathbb Q}$，无穷型为
$(z/|z|)^{-(2m+1)}$。有限单位上的限制不随 $m$ 变化；
在 $2$ 处完整局部特征也不变，因为在统一化元 $1+i$ 上的比值是
$i^{-m}=1$。

Yang 1997 Theorem 2.6、式(2.19)及 Theorem 2.15 适用。
所有非分裂未分歧处、分裂处与无穷处的局部 dichotomy 允许
Hermitian 参数 $\alpha=1$；$2$ 处由根数 $+1$ 及局部符号乘积确定。
在 $2$ 处用一般存在性和紧平均选代数值向量，
在 $17$ 处用 Corollaries 2.13–2.14 的固定向量及固定等距变换。
因此可以固定一个单位范数有限 Schwartz 向量 $\phi_f$，
而只改变无穷处的 Hermite 阶。

无穷处采用单位范数
$$
h_m(x)=\frac{2^{1/4}}{\sqrt{2^m m!}}
 H_m(\sqrt{2\pi_{\mathbb C}}x)e^{-\pi_{\mathbb C}x^2}.
$$
Yang 的基 $e=i,f_0=-1$ 给
$d\omega(J)=i(\mathcal H-m-\tfrac12)$，其中
$\mathcal H=-\partial_x^2/(4\pi_{\mathbb C})+\pi_{\mathbb C}x^2$。
因此 $h_m$ 恰为平凡角色向量；两个半角因子必须同时保留。
这一规范另由 Yang 1999 Lemma 1.1 和 Appendix (A3) 直接核对。

因 $\mathbb Z[i]$ 类数一，norm-one torus 有
$$
G(\mathbb A)=G(\mathbb Q)\mathcal K,\qquad
G(\mathbb Q)\cap\mathcal K=\mu_4.
$$
固定有限紧平均 $\phi_f^{\rm av}$ 后，可取同一个偶数 $L$
使其支撑包含于 $L^{-1}\widehat{\mathbb Z}$，并在
$L\widehat{\mathbb Z}$ 下平移不变。
令 $a_n=\phi_f^{\rm av}(n/L)$，则 $a_{n+d}=a_n$、$d=L^2$，
全部 $a_n$ 代数；$L$ 只有素因子 $2,17$。

Yang 原规范中
$\operatorname{vol}(\mathcal K)/\operatorname{vol}(G(\mathbb Q)\backslash G(\mathbb A))=4$，
Theorem 1.11 给 $c(0)=17/256$。
其式(2.19)因而准确成为
$$
L_f(\psi^{2m+1},m+1)=\frac{32\pi_{\mathbb C}}{17}
 \left|\sum_n a_nh_m(n/L)\right|^2.
\tag{5}
$$
令
$$
B(t)=e^{-t^2}\sum_na_n
 \exp\!\left(-\pi_{\mathbb C}(n/L)^2+
  2\sqrt{2\pi_{\mathbb C}}(n/L)t\right)=\sum_mb_mt^m.
$$
Hermite 生成式给
$$
L_f(\psi^{2m+1},m+1)
 =\frac{32\sqrt2\pi_{\mathbb C}}{17}\frac{m!}{2^m}|b_m|^2.
\tag{6}
$$

## 3. 一个共同代数截面，及四次对称性

记 $T=\sqrt{\pi_{\mathbb C}/2}L$、$c=T/\Omega_E$。
固定权重的周期性给
$$
B(t+T)=e^{2Tt+T^2}B(t),\qquad
B(t+iT)=e^{-2iTt+T^2}B(t).
$$
所以 $B(cz)/\sigma_E(z)^d$ 是仅在 $O$ 有至多 $d$ 阶极点的椭圆函数。

其代数性不能只由准周期律断言。
将 $B$ 展开在 $d$ 个 residue theta 函数 $B_r$ 上。
归一化平移
$$
\mathcal XF(t)=e^{-2at-a^2}F(t+a),\qquad
\mathcal YF(t)=e^{2iat-a^2}F(t+ia),\qquad a=T/d
$$
满足
$$
\mathcal XB_r=B_{r-1},\quad\mathcal YB_r=\zeta_d^rB_r,\quad
\mathcal X^d=\mathcal Y^d=1,\quad
\mathcal X\mathcal Y=\zeta_d\mathcal Y\mathcal X.
$$
它们覆盖代数 $d$-torsion 平移。
$\mathcal O_E(dO)$ 的相应代数 lifts 可将 $d$ 次幂归一化为一；
与上述解析 lifts 的差于是为代数根单位。
每个 $\mathcal Y$ 特征空间一维，
$\mathcal X$ 又强制这 $d$ 个解析基向量与代数基向量具有同一个比例。
因此存在固定非零复数 $C$ 和 $R\in\overline{\mathbb Q}(E)$，
使
$$
B(cz)=C\,R(x(z),y(z))\sigma_E(z)^d.
\tag{7}
$$
有限个代数系数生成固定数域。

全局 theta 分布在 $i\in G(\mathbb Q)$ 下不变，
有限平均也在 $i$ 下不变，而无穷 Hermite 第 $n$ 层具有特征 $i^n$。
故 $b_n=0$ 除非 $4\mid n$，并有 $R([i]P)=R(P)$。
固定域是 $M(x^2)$；没有有限极点迫使 $R=P(x^2)$。
极点阶给 $\deg P\le d/4$。

至少一个 $4\mid m$ 的中央值非零：
否则在一个固定普通 $p$ 上，R40 的全部
$m=(p-1)p^n$ 插值值为零，累积到中心，矛盾于实际分支非恒零。
所以 $P\ne0$。

把 $b_mc^m=Cs_m$ 代入 (6)，并使用
$$
e_m=\frac{(\pi_{\mathbb C}/Nf)^m}
 {m!\Omega_E^{2m+1}}L_f(\psi^{2m+1},m+1),
$$
得到 (1)，其中
$\kappa=32\sqrt2\pi_{\mathbb C}|C|^2/(17\Omega_E)$。
取一个非零 $e_{m_0}$，由
$\kappa=e_{m_0}(Nf\,d)^{m_0}/(s_{m_0}\overline{s_{m_0}})$
可知它是固定正实代数数。
$e_0=0$ 进而给 $s_0=0$，排除次数 $d/4$ 的项，
故 $\deg P\le d/4-1$。

## 4. 同一测度与整条分支

普通处 $\Sigma(t)=\sigma_E(\log_Et)\in t\mathbb Z_p[[t]]$。
因为 $R$ 在 $O$ 的极点阶不超过 $d$，
$$
R(x(t),y(t))\Sigma(t)^d
$$
为有界的正则幂级数。
代入整正式群同构
$t=\exp_E(\Omega_p\log(1+Z))$，
得到有界 Amice 变换
$$
\mathcal A_p(Z)=S(\Omega_p\log(1+Z)).
$$
共轭系数版本使用同一个 $\Omega_p$。
其对数导数的全部矩正是 (2)。

对 $m>0$、$p-1\mid m$，原 theta 插值公式与 (1)–(2) 准确给
$$
F_p^{\Theta,-}(t_m)=
 \kappa f\Omega_p(f^2/d)^m
 \left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)^2M_mM_m^\dagger,
\quad t_m=(1+p)^m-1.
\tag{8}
$$
这里 $M_m$ 是整个 $\mathbb Z_p$ 上的矩。
测度有界意味着删去 $p\mathbb Z_p$ 上的贡献产生
$v_p$ 至少 $m-O_p(1)$ 的误差。
Euler 因子与一的差也至少有赋值 $m$。

固定 $p-1\mid m_0$，取
$m_n=m_0+(p-1)p^n$。
该列在实数中趋于无穷，在 $\mathbb Z_p$ 中趋于 $m_0$。
因此 (8) 的误差趋于零，而两个单位矩分别趋于
$G_p(t_{m_0})$ 和 $G_p^\dagger(t_{m_0})$；
$(f^2/d)^{m_n}$ 趋于 $(1+t_{m_0})^{a_p^\circ}$。
这给 (3) 在全部这些点成立。
再取 $m_0=(p-1)p^j$，互异点趋于零，解析恒等定理给整条 (3)。

这保留了完整共同权参数、两个阶乘和同一周期；
没有逐值重选单位或忽略不趋于零的误差。
两个因子非恒零，取零阶并用 R40 即得 (4)。

## 5. 范围与继续任务

除固定有限素数外，(1) 还给
$$
v_p(d_{p-1})=v_p(s_{p-1})+v_p(\overline{s_{p-1}}).
$$
但复共轭可以改变 $p$ 位，不能将右边直接写成
$2v_p(s_{p-1})$。
$s_0=0$ 也只控制测度总质量，尚不控制单位区间的质量 $G_p(0)$。

下一项真正需要的结论是：两个实际因子的总中心零阶对无穷多个
普通 $p$ 等于二。固定截面、代数 Taylor 系数、复中央值非零及
单个 $p$ 的分支非恒零均不自动证明这一结论。

### 已核一手来源

- Tonghai Yang, *Theta liftings and Hecke L-functions*,
  J. reine angew. Math. **485** (1997), 25–53，
  Theorems 1.11、2.6、2.15，式(1.16)、(2.19)，
  Corollaries 2.13–2.14：
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
- Tonghai Yang, *Nonvanishing of central Hecke L-values and rank of certain
  elliptic curves*, Compositio Math. **117** (1999), 337–359，
  Lemma 1.1、Appendix (A3)：
  [出版社全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/915B51D40C0BD146C3DBC94DE4041BDD/S0010437X99000433a.pdf/nonvanishing_of_central_hecke_lvalues_and_rank_of_certain_elliptic_curves.pdf)。
- 固定 sigma 的整性、完整 theta/Katz 比较及 R40 的 Selmer 判据，
  使用本课题对应已证结果；完整证明笔记逐项链接这些输入。
