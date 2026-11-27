# R1141：原低权端点的算术支撑与实际圆单位杯积方向

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，范围如下。** 在 $p>37$ 且 $p\nmid B_{p-5}$ 时，原
$X=X_{\rm ns}^+(p)$ 上、在 $p$ 外整模型上延拓的
$\theta=\omega^{-6}$ 杯积目标中，通常 Hecke 特征值
$\ell^{-2}+\ell^3$ 的整个本征空间，由一个指定的原杯积
$\{F_{\chi_1},\beta_{\chi_2}\}$ 张成，允许这个杯积本身为零。
这里 $\chi_1=\omega^{-2}$、$\chi_2=\omega^{-4}$，
$F_{\chi_1}$ 是原规范函数，$\beta_{\chi_2}$ 是原全局圆单位基。

因此 R1140 的实际端点分量落在这个明确方向。若再有
$p\nmid B_{16}B_{p-15}$，原两个函数的裸杯积可通过原第二槽的一个
真正全局常数 twist 消去。本文没有确定该 twist 的标量，也没有把
函数域中的杯积零提升成 proper 曲线上的 $H^2$ 零或四阶覆盖。

## 1. 原对象与准确的算术目标

置
$$
K=\mathbb Q(\zeta_p),\qquad
S=\operatorname{Spec}\mathcal O_K[1/p],\qquad
S_0=\operatorname{Spec}\mathbb Z[1/p],\qquad
\Delta=\operatorname{Gal}(K/\mathbb Q).
\tag{1141.1}
$$
令 $\mathscr X/S$ 为 R1067 §§2–3 支付的原 smooth proper 模型，
$\mathcal J=\operatorname{Pic}^0_{\mathscr X/S}$，泛纤维为原
$J_{\rm ns}=\operatorname{Jac}(X)$。全部原 cusp 在 $S$ 上给互不相交的
sections；特别存在 degree-one section，但不选择一个新的规范基点。

固定原角色与实际函数
$$
\chi_1=\omega^{-2},\qquad
\chi_2=\omega^{-4},\qquad
\theta=\chi_1\chi_2=\omega^{-6},\qquad m=(p-1)/2.
\tag{1141.2}
$$
以 norm residue 同构识别函数域上的 $K_2/p$ 与
$H^2(K(X),\mu_p^{\otimes2})$，定义
$$
\mathcal B_\theta
 =\operatorname{im}\left(
 H^2(\mathscr X,\mu_p^{\otimes2})_\theta
 \longrightarrow H^2(K(X),\mu_p^{\otimes2})\right).
\tag{1141.3}
$$
这是原算术整模型的实际像，比仅在 $X_K$ 上 compact 的条件更强。
本文没有将整个 field $K_2/p$ 认成此像。

保留原 $\zeta_p$ 后，把一个 $\mu_p$ 因子消去，会把角色改为
$$
\xi=\theta\omega^{-1}=\omega^{-7}.
\tag{1141.4}
$$
因此 (1141.3) 对应 $\operatorname{Br}(\mathscr X)[p]_\xi$；
不是 $\theta$-分量的 Brauer 群，也不是平凡角色的整 $K_2[p]$。
$\mathscr X$ 正规且 regular，Brauer 群向函数域单射，故这里不再有
Brauer 层的 generic kernel。Kummer exact sequence 中的 Picard 项
将在 §3 明确保留。

## 2. 原两个函数及所有实际 Hecke 像确有这个支撑

R1067 §4、§7 对原规范
$f_u=u^m/\prod_c\operatorname{lc}_c(u)$ 已证明：

- 水平 divisor 的每个系数都是 $p$ 的倍数；
- 在每个 $\mathfrak q\nmid p$，唯一垂直纤维的系数也是 $p$ 的倍数；
- 这些结论包括 $2,3$，也包括全部 cusp sections。

R1070 的真实整函数比较把当前 $F_{\chi_i}$ 保持在同一规范
Kummer 类中。因而在 regular $\mathscr X$ 上
$\operatorname{div}(F_{\chi_i})=pD_i$，其中 $D_i$ 是 Cartier divisor。
由线丛 $\mathcal O(D_i)$ 及该 $p$ 次平凡化得到
$$
\kappa_i\in H^1(\mathscr X,\mu_p)_{\chi_i}.
\tag{1141.5}
$$
这直接延拓整个 proper torsor，不只说明有理点处的值为 $p$-unit。
改变函数的 $p$ 次幂代表不改变 (1141.5)。

所以原
$$
\beta=\frac4{m^2}\{F_{\chi_1},F_{\chi_2}\}
\tag{1141.6}
$$
属于 $\mathcal B_\theta$。

还须支付辅助素数 $n$ 自身处的支撑，而不能仅在
$\mathcal O_K[1/(np)]$ 上工作。对原通常 Hecke correspondence，
在 regular 三维模型 $\mathscr X\times_S\mathscr X$ 取其水平闭包。
它是 codimension-one Cartier cycle。其 cycle class、两次投影的
pullback 与 smooth-proper trace 定义
$$
a\longmapsto
(\operatorname{pr}_2)_*
 \bigl(\operatorname{pr}_1^*a\cup[\overline{\Gamma_n}]\bigr)
\tag{1141.7}
$$
在 $H^2(\mathscr X,\mu_p^{\otimes2})$ 上的作用。
限制到泛纤维正是原 $T_n$；不要求 $n$ 在 $S$ 上可逆。
这也保留 Picard 子群及 Leray filtration。在 $R^1$ 上所得作用，
由泛纤维及 abelian scheme 的延拓唯一性，正是 $\mathcal J[p]$
上的原 Hecke endomorphism。

于是 $\mathcal B_\theta$ 对所有 $n\ne p$ 的通常 Hecke 稳定。
R1140 中
$$
V_n=n^4-n^{-4}T_n+n^{-11},\qquad
\beta_{\rm Eis}=v_{n_0}^{-1}V_{n_0}\beta
\tag{1141.8}
$$
以及 $\beta_8=\beta-\beta_{\rm Eis}$ 都属于这个同一算术像。
其中 $v_n=n^{-11}(n^5-1)(n^{10}-1)$，
$n_0>3$ 为 R1140 选定的 primitive-residue 辅助素数。

## 3. 全部 base 与 Picard 项之后的 Brauer 单射

首先
$$
\operatorname{Br}(S)=0.
\tag{1141.9}
$$
确实，一个来自 $\operatorname{Br}(S)$ 的数域 Brauer 类在所有
$\mathfrak q\nmid p$ 的 local invariant 都为零。$K$ 无实位，
而且只有一个 $p$ 上素位。全球 invariant 之和为零迫最后一个
invariant 也为零；全球 Brauer 单射给 (1141.9)。
这里没有丢掉某个额外的 $2$ 或 $3$ 支撑。

对 $\mathscr X/S$ 使用有限系数 Leray spectral sequence。
有
$$
R^1f_*\mu_p=\mathcal J[p],\qquad
R^2f_*\mu_p=\mathbb F_p,
\tag{1141.10}
$$
后者是 degree trace，$\Delta$ 作用平凡。
$\xi=\omega^{-7}$ 非平凡，因此
$H^2(\mathscr X,\mu_p)_\xi$ 的几何 top 部分为零。
其 edge class 落在 $H^1(S,\mathcal J[p])_\xi$。

必须同时取完整 Kummer 商：
$$
0\longrightarrow\operatorname{Pic}(\mathscr X)/p
 \longrightarrow H^2(\mathscr X,\mu_p)
 \longrightarrow\operatorname{Br}(\mathscr X)[p]
 \longrightarrow0.
\tag{1141.11}
$$
存在 cusp section，使 degree-zero relative line bundles 全部可在
$\mathscr X$ 上实现；换言之，$\operatorname{Pic}(\mathscr X)$ 的
degree-zero 部分向 $\mathcal J(S)$ 满射，核来自 $\operatorname{Pic}(S)$。
其 edge 正是 $\mathcal J(S)/p$ 的 Kummer map。
degree 部分在非平凡 $\xi$ 上没有贡献；不需要 section 本身
$\Delta$-不变。

因此 edge 在 (1141.11) 的 Brauer 商上给
$$
\iota:\operatorname{Br}(\mathscr X)[p]_\xi
 \hookrightarrow H^1(S,\mathcal J)[p]_\xi.
\tag{1141.12}
$$
为核单射，若 edge 在右侧为零，先减去实现该 Kummer 类的
degree-zero line bundle 的 Chern class。剩余 $H^2$ 类来自
$H^2(S,\mu_p)$，它在 Brauer 商上的像来自
$\operatorname{Br}(S)$，由 (1141.9) 为零。
这个论证保留 $\operatorname{Pic}(S)/p$，没有声称它为零；
也没有假设整个 Leray sequence 在对象层面分裂。

(1141.12) 对原 Hecke 等变：对应的 $R^1$ 算子已由 (1141.7)
识别为 $\mathcal J[p]$ 的真实算子，Picard 商也稳定。
它对 $\Delta$ 自然等变，选择 cusp 仅用于证明有关满射和单射。

## 4. 实际 DVR 块的 cohomology socle 提升

假设
$$
p\nmid B_{p-5}.
\tag{1141.13}
$$
R1131 取 $j=1$，所需两个 Bernoulli 条件是
$B_6=1/42$ 与 $B_{p-5}$ 为单位，故前者对 $p>37$ 自动成立。
记
$$
\mathfrak m=
 \bigl(p,T_\ell-\ell^{-2}-\ell^3:\ell\ne p\bigr),
\qquad
\mathcal O=\mathbb T_{\mathfrak m}.
$$
R1131 已证明 $\mathcal O$ 是 DVR、真实 Tate 格为自由秩二，
并且原有限 étale sheaf 的泛纤维是
$$
0\longrightarrow\mathbb F_p(\omega^{-2})
 \longrightarrow J_{\rm ns}[\mathfrak m]
 \longrightarrow\mathbb F_p(\omega^3)
 \longrightarrow0.
\tag{1141.14}
$$
左线由原 $\kappa_1$ 的 divisor 类生成。
这是实际格的非分裂方向，不另选半单化相同的表示。

以下提升引理防止把一个 cohomology 本征类直接认成有限 socle 的类。

**引理。** 在这个块上，存在满射
$$
H^1(S,\mathcal J[\mathfrak m])_\xi
 \longrightarrow H^1(S,\mathcal J)[\mathfrak m]_\xi.
\tag{1141.15}
$$

**证明。** 先对全部 $p^a$ 的 Kummer sequences 取 direct limit：
$$
0\longrightarrow
D:=\mathcal J(S)\otimes\mathbb Q_p/\mathbb Z_p
 \longrightarrow H^1(S,\mathcal J[p^\infty])
 \longrightarrow H^1(S,\mathcal J)[p^\infty]
 \longrightarrow0.
\tag{1141.16}
$$
在这些真实 $p$-primary 模块上取 completed-Hecke block 及
Teichmüller $\xi$ projector；两者都是实际 exact idempotents。

设 $\pi$ 为 $\mathcal O$ 的 uniformizer，写 $p=u\pi^e$。
$D_{\mathfrak m,\xi}$ 是 $p$-divisible，因此也是 $\pi$-divisible：
若 $pd'=d$，则 $\pi(u\pi^{e-1}d')=d$。
给定右侧被 $\mathfrak m$ 杀掉的 $\tau$，取 (1141.16) 中的
lift $y$。有 $\pi y\in D_{\mathfrak m,\xi}$，故可减去一个
$d\in D_{\mathfrak m,\xi}$ 使 $\pi(y-d)=0$。

真实 Tate 格 $\mathcal O^2$ 给 $p$-divisible sheaf factor 的 exact sequence
$$
0\longrightarrow\mathcal J[\mathfrak m]
 \longrightarrow\mathcal J[p^\infty]_{\mathfrak m}
 \xrightarrow{\pi}\mathcal J[p^\infty]_{\mathfrak m}
 \longrightarrow0.
\tag{1141.17}
$$
其 cohomology long exact sequence 把 $y-d$ 从左侧 $H^1$ 提升。
再取 $\xi$ 分量即得 (1141.15)。这里仅对实际 $p$-divisible
sheaf factor 使用 $\pi$，没有假设存在一个整分解的 abelian scheme
$\mathcal J_{\mathfrak m}$。证毕。

## 5. 两个准确的圆分角色与 $B_{10}$

有限 étale 覆盖 $S/S_0$ 的次数为 $p-1$。
Hochschild–Serre 的正次数 $\Delta$-cohomology 为零，故
$$
H^1(S,\mathcal J[\mathfrak m])_\xi
 \simeq H^1(S_0,\mathcal V),\qquad
\mathcal V=J_{\rm ns}[\mathfrak m]\otimes\omega^7.
\tag{1141.18}
$$
(1141.14) 因而准确变为
$$
0\longrightarrow\mathbb F_p(\omega^5)
 \longrightarrow\mathcal V
 \longrightarrow\mathbb F_p(\omega^{10})
 \longrightarrow0.
\tag{1141.19}
$$
所有 sheaves 均在 $p$ 外 finite étale；这不需要将普通
$H^1$ 换成一个未支付的 Selmer 条件。

对任意整数 $s$，相同 restriction 与 Kummer identification 给
$$
H^1(S_0,\mathbb F_p(\omega^s))
 \simeq H^1(S,\mu_p)_{\omega^{1-s}}.
\tag{1141.20}
$$
特别，$s=10$ 的 Kummer 角色是 $\omega^{-9}$。
完整 $S$-unit/class-group exact sequence 为
$$
0\longrightarrow
 \mathcal O_K[1/p]^\times/
       \mathcal O_K[1/p]^{\times p}
 \longrightarrow H^1(S,\mu_p)
 \longrightarrow\operatorname{Pic}(S)[p]
 \longrightarrow0.
\tag{1141.21}
$$
奇单位部分只有 $\mu_p$ 的 $\omega$，而唯一 $p$ 位的 valuation
角色平凡；故左项的 $\omega^{-9}$ 分量为零。
Herbrand 的正向定理作用于
$\omega^{1-10}=\omega^{-9}$，且 $B_{10}=5/66$ 对 $p>37$ 为单位，
故 $\operatorname{Cl}(K)[p]_{\omega^{-9}}=0$。
局部化的类群是其商，所以
$$
H^1(S_0,\mathbb F_p(\omega^{10}))=0.
\tag{1141.22}
$$

$s=5$ 对应 $\omega^{-4}=\chi_2$。
由 R1069 §§2–3 的已付反射与原圆单位定位，(1141.13) 给
$$
H^1(S,\mu_p)_{\chi_2}
 =\mathbb F_p\,\beta_{\chi_2},\qquad
\beta_{\chi_2}=e_{\chi_2}[\eta_a]\ne0,
\quad
\eta_a=\zeta_p^{(1-a)/2}\frac{1-\zeta_p^a}{1-\zeta_p}.
\tag{1141.23}
$$
$a$ 仍为原固定奇生成元。R1069 在实子域上的结论向 $K$ 的
偶分量运输使用 degree-two restriction–norm，其次数为 $p$-单位。

由于 $H^0(S_0,\omega^{10})=0$，(1141.19)–(1141.23) 得
$$
H^1(S_0,\omega^5)\xrightarrow{\;\sim\;}H^1(S_0,\mathcal V),
\qquad \dim_{\mathbb F_p}H^1(S_0,\mathcal V)=1.
\tag{1141.24}
$$
这只断言有限 sheaf 的 $H^1$ 为一维；其后到
$H^1(S,\mathcal J)$ 的像仍可能被 Mordell–Weil Kummer 项杀掉。

## 6. 该唯一方向正是原常数乘原函数的杯积

选择真正全局单位 $\epsilon_2$ 代表 (1141.23) 的原类，定义
$$
B_{12}:=\{F_{\chi_1},\epsilon_2\}
       =\{F_{\chi_1},\beta_{\chi_2}\}
       \in\mathcal B_\theta.
\tag{1141.25}
$$
第一槽的 geometric Kummer image 是 (1141.14) 的原非零 cusp
vector $D_1$。第二槽来自 $H^1(S,\mu_p)_{\chi_2}$。
消去固定 $\zeta_p$ 因子后，Leray edge 是
$$
-\bigl(\kappa(\epsilon_2)/\zeta_p\bigr)\otimes D_1
 \in H^1(S,\mathcal J[p])_{\omega^{-7}}.
\tag{1141.26}
$$
负号是按第一槽 fibre degree one、第二槽 base degree one 的
通常 Leray product convention；不影响张成方向。
其角色可直接核：
$(\chi_2\omega^{-1})\chi_1=\omega^{-7}$。

由 (1141.18)–(1141.24)，(1141.26) 正是
$H^1(S,\mathcal J[\mathfrak m])_\xi$ 的指定生成方向。
因此 (1141.12)、(1141.15) 给出
$$
\boxed{\quad
\{b\in\mathcal B_\theta:
   T_\ell b=(\ell^{-2}+\ell^3)b
   \text{ 对所有 }\ell\ne p\}
 =\mathbb F_p\,B_{12}.
\quad}
\tag{1141.27}
$$
右边的包含也须说明：$D_1$ 上的原 Hecke 特征是
$\ell^{-2}+\ell^3$，所以 (1141.26) 的 edge 有该特征；
(1141.12) 单射使原 Brauer 类本身有该特征。
没有留下一个未控制的 base 常数差。

(1141.27) 允许 $B_{12}=0$，所以其实际像维数是零或一。
本文不以原圆单位非零推这个杯积非零，也不声称对应标量总是唯一。

## 7. 对 R1140 指定端点与原裸杯积的结论

R1140 的 $\beta_{\rm Eis}$ 有全部原 Hecke 特征值
$\ell^{-2}+\ell^3$。§2 已证明它属于 $\mathcal B_\theta$，
故在仅有 (1141.13) 的条件下，存在 $a_p\in\mathbb F_p$ 使
$$
\boxed{\quad
\frac4{m^2}\{F_{\chi_1},F_{\chi_2}\}
 =a_p\{F_{\chi_1},\beta_{\chi_2}\}+\beta_8,
\qquad V_n\beta_8=0 .
\quad}
\tag{1141.28}
$$
这里 $\beta_8$ 是 R1140 的同一个原分量，仍保全部辅助素数
$n>3,n\ne p$，没有扩大到未证明的 target 商关系。

若进一步
$$
p\nmid B_{16}B_{p-15},
\tag{1141.29}
$$
则 R1139/R1140 的准确低混合门消去 $\beta_8$。
令 $c_p=m^2a_p/4$，得到
$$
\boxed{\quad
\{F_{\chi_1},F_{\chi_2}\}
 =c_p\{F_{\chi_1},\beta_{\chi_2}\},
\qquad
\{F_{\chi_1},F_{\chi_2}/\epsilon_2^{\,c_p}\}=0
 \quad\text{于 }K_2(K(X))/p .
\quad}
\tag{1141.30}
$$
指数取任意整数提升；等式不依赖提升或 $\epsilon_2$ 的
$p$ 次幂代表。

$F_{\chi_2}/\epsilon_2^{c_p}$ 是原 torsor 家族的一个真正
常数 twist。它不重定义原 leading-normalized $F_{\chi_2}$，
不改变原标签基，也没有证明 $c_p=0$。
特别，$\epsilon_2$ 不是某个局部任意单位。

## 8. 继续保留的 proper 与高阶问题

(1141.30) 是原函数域 $K_2/p$ 的严格结论。
proper 曲线上的 cup lift 若在函数域为零，仍可能来自
$$
\operatorname{Pic}(\mathscr X)/p\otimes\mu_p
 \longrightarrow H^2(\mathscr X,\mu_p^{\otimes2}).
\tag{1141.31}
$$
§3 是为了准确控制 Brauer 商，不能反过来删掉 (1141.31)。
因此本文尚未给出 proper Heisenberg lift、指定四阶 cover，
也没有确定原有理点对应的 twist 必为 (1141.30) 的那个值。

下一项实际输入是 $a_p/c_p$ 的指定来源，或相应 proper Picard
cochain 的消去。R1140 的完整端点 map、原 cusp leading 规范、
$\beta_8$ 的门外部分及四阶非重复邻对全部保留。

## 来源与所用范围

- R1067 §§2–4、§7：原 smooth proper 模型、全部 cusp 与
  $2,3$ 在内的垂直 divisor 和 finite étale torsor。
- R1069 §§2–3：准确 Herbrand 角色、所需 real reflection、
  原 $\beta_{\chi_2}$ 与唯一全局 Kummer 方向。
- R1131 §§1–4：同一个真实 Eisenstein DVR、自由秩二 Tate 格、
  原 cusp 子线及有限扩张方向。
- R1138–R1140：原 Hecke、裸杯积、两个实际 target 部分及明确混合门。
- J.-L. Colliot-Thélène and A. N. Skorobogatov,
  *The Brauer–Grothendieck group*, 2021；
  [作者 2019 草稿](https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf)：
  本文亲读 §2.2.3 的 Leray sequence、§2.5 的 Picard functor，
  Theorem 3.5.4 的 generic injectivity，
  §12.1.2/Theorem 12.1.8 的 global invariant exact sequence。
  上文只由这些标准工具作所显示的 diagram chase。
- R. Sharifi, [*Iwasawa Theory*, Chapter 4](https://math.ucla.edu/~sharifi/notes/iwasawa-ch04.html)，
  Theorem 4.5.7 的 Herbrand 正向消去；用于 (1141.22) 的角色明确为
  $\omega^{-9}$，相应 Bernoulli 是 $B_{10}$。

全部为纸面推导，没有数学程序执行。o2 独立核 §4 的真实
$p$-divisible sheaf、completed projector 与 $\pi$-divisibility 提升。
