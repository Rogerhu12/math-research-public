# R1069：全素数上的 Bernoulli 单位角色与唯一全局标签

日期：2026-11-27（Asia/Taipei）。  
会话：Astra-serre-24b8836b-20261126；root，o2_high_coefficient 独立纸核。

**已证明。** 对全部 $p>37$，不用 regular 或 Vandiver 假设，
原 $X=X_{\rm ns}^+(p)$ 的实际 cuspidal $p$-torsion 含一个明确的子模块
$W_{\rm good}$。在这个子模块上，R1067 的 $p$-only 全局标签空间
到 $p$-local 标签空间是同构。因此原每个 $\mathbf Q_p$ 圆盘仍只给
一个实际全局候选，全部候选至多
$p\,n_{\mathbf Q_p}(p)=O(p^{3/2}\log p)$。

令
$$
r_0=\lfloor p/4\rfloor-1,\qquad
\mathcal H_p=2p\left(\frac{(p-1)(p-2)}{24p}\right)^{(p-1)/4}.
\tag{1069.1}
$$
则这个真实子模块的维数满足
$$
\boxed{\quad
d_{\rm good}\ge r_0-\lfloor\log_p \mathcal H_p\rfloor
=\frac{\log24}{4}\frac p{\log p}-O(1).
\quad}
\tag{1069.2}
$$
右边的等号只说明所显示下界的渐近，不宣称实际维数等于该量。
特别 $d_{\rm good}=\Omega(p/\log p)$，对每个允许素数均有这样的
实际连通 $p^{d_{\rm good}}$ 次原覆盖。

没有删掉剩余坏角色的类群项，也没有把候选有限性当成候选排除。
原整曲线、非整 $j$、完整 $I_p$ 和变化二次域均在本结论范围；
原共同辅助像排除仍开放。全部为纸面证明，没有数学程序执行。

## 1. 固定原模块和两种不同的角色方向

沿用 R1062/R1067 的
$$
F=\mathbf Q(\zeta_p)^+,\quad K=\mathbf Q(\zeta_p),\quad
G=\operatorname{Gal}(F/\mathbf Q),\quad
\Delta=\operatorname{Gal}(K/\mathbf Q),\quad
m=(p-1)/2.
$$
$\omega:\Delta\to\mathbf Z_p^\times$ 是 Teichmüller 字符。
非平凡偶字符写为
$$
\chi=\omega^r,\qquad 2\le r\le p-3,\qquad r\ {\rm even}.
\tag{1069.3}
$$
同时用同一符号表示其模 $p$ 约化。
对数列 $B_r$ 采用 $B_1=-1/2$ 的通常 Bernoulli 归一化。
此范围的 $B_r$ 均为 $p$-整，因此
“$p\nmid B_r$”的意思是 $B_r\in\mathbf Z_p^\times$。

记原模块
$$
V=U_p/pU=C_\Sigma[p]
$$
为 R1062 的真实 cuspidal Kummer 模块，其中 $U_p$ 是除子被 $p$
整除的原模单位格。数值上界 $\mathcal H_p$ 与这个格无关。
R1062 已证明 $V^G=0$，其每个非零角色至多一维，且包含
$$
\chi_j=\omega^{-2j},\qquad 1\le j\le r_0.
\tag{1069.4}
$$
不重证或扩大这组 forced characters。

称 (1069.3) 为 good，若 $p\nmid B_r$。定义
$$
W_{\rm good}=
\bigoplus_{\substack{\chi=\omega^r,\ V_\chi\ne0\\p\nmid B_r}}V_\chi
\subset V.
\tag{1069.5}
$$
它可包含 (1069.4) 之外的 good 角色；下界只使用 (1069.4)。

必须分清下列两个方向：
$$
\begin{array}{c|c}
\text{Herbrand 要杀的类群角色}&\omega^{1-r}\\
\text{其 Stickelberger/Bernoulli 标量}&B_{1,\omega^{r-1}} .
\end{array}
\tag{1069.6}
$$
二者互为逆，不能把它们统一改成同一个角色。

## 2. 一个 good 角色已足以杀对应 real class group

先用 Herbrand 的正向定理及 Kummer congruence：
$$
B_{1,\omega^{r-1}}\equiv B_r/r\pmod p,\qquad
p\nmid B_r\Longrightarrow
\operatorname{Cl}(K)[p]_{\omega^{1-r}}=0.
\tag{1069.7}
$$
这里 $1-r\not\equiv1\pmod{p-1}$，所以没有 $\omega$ 异常项。
来源和所用准确范围见末节；无需 Herbrand 的逆定理。

下面直接证明所需 reflection 方向，避免仅援引一个含方向约定的
反射不等式。假设 $\operatorname{Cl}(F)[p]_\chi\ne0$。
因 $p\nmid|G|$，$\mathbf Z_p[G]$ 的字符幂等元整，
$\chi$-主分量有一个非零一维模 $p$ 商。
类域论因此给一个 everywhere unramified cyclic degree-$p$
extension $M/F$，且共轭作用在
$\operatorname{Gal}(M/F)$ 上恰为 $\chi$。
所取核 $G$-稳定，故 $M/\mathbf Q$ 正规。

$[K:F]=2$ 与 $p$ 互素，所以 $MK/K$ 仍是非平凡、
everywhere unramified、degree-$p$ extension，
其 Galois 群作为 $\Delta$-模块仍为 $\chi$。
Kummer pairing
$$
\operatorname{Gal}(MK/K)\times
\operatorname{Rad}(MK/K)\longrightarrow\mu_p
$$
是 $\Delta$-等变完美配对。故其一维 radical 的角色准确为
$$
\psi=\omega\chi^{-1}=\omega^{1-r}.
\tag{1069.8}
$$

令
$$
D(K)=\{a\in K^\times:
v_{\mathfrak q}(a)\equiv0\pmod p
\text{ 对所有有限 }\mathfrak q\}/K^{\times p}.
$$
因 $MK/K$ 在所有有限素点不分歧，其非零 radical 在 $D(K)$ 中：
若某个 valuation 不被 $p$ 整除，Kummer extension 在该素点
的 ramification index 必被 $p$ 整除。
完整标准 exact sequence 为
$$
0\longrightarrow E_K/E_K^p
\longrightarrow D(K)
\longrightarrow\operatorname{Cl}(K)[p]
\longrightarrow0.
\tag{1069.9}
$$
映射把 $\operatorname{div}(a)=pD$ 送到 $[D]$，因此不反转角色。

$\psi$ 是奇字符且 $\psi\ne\omega$。
CM 单位的奇部分模 $p$ 只有根单位 $\mu_p$，其角色为 $\omega$；
等价地，$E_K/(\mu(K)E_F)$ 的阶至多二。
故
$$
(E_K/E_K^p)_\psi=0.
$$
由 (1069.9)，非零 radical 单射到
$\operatorname{Cl}(K)[p]_\psi$，与 (1069.7) 矛盾。遂
$$
\boxed{\ p\nmid B_r
\Longrightarrow\operatorname{Cl}(F)[p]_{\omega^r}=0.\ }
\tag{1069.10}
$$
这个论证保留 Kummer 的 $\omega$ 扭转和 units 的唯一奇异常项。
没有假设整个 $\operatorname{Cl}(F)[p]$ 消失。

## 3. 原 p-only 全局到局部同构

令 $\mathfrak p$ 为 $F$ 中唯一的 $p$ 上素点，
$L=F_{\mathfrak p}=\mathbf Q_p(\zeta_p)^+$。
R1067 已证明原每个有理点的标签属于
$$
\operatorname{Hom}_G(V,F(\{p\},p)),\qquad
F(\{p\},p)=
\{a\in F^\times:v_{\mathfrak q}(a)\equiv0\bmod p\
(\mathfrak q\nmid p)\}/F^{\times p}.
\tag{1069.11}
$$
该输入适用于全部原 $X(\mathbf Q)$，没有整 $j$ 条件。
完整 $S$-unit/class-group sequence 给
$$
0\longrightarrow
\mathcal O_F[1/p]^\times/
  \mathcal O_F[1/p]^{\times p}
\longrightarrow F(\{p\},p)
\longrightarrow\operatorname{Cl}(\mathcal O_F[1/p])[p]
\longrightarrow0.
\tag{1069.12}
$$

对 good 非平凡 $\chi$，(1069.10) 使右侧的 $\chi$ 分量为零。
唯一素点 $\mathfrak p$ 的 valuation 模块是平凡 $G$-角色；
所以左侧非平凡 $\chi$ 分量与 $(E_F/E_F^p)_\chi$ 相同。
由 Dirichlet unit 的 $G$-表示（regular representation 去掉平凡角色），
$$
F(\{p\},p)_\chi=(E_F/E_F^p)_\chi,\qquad
\dim_{\mathbf F_p}F(\{p\},p)_\chi=1.
\tag{1069.13}
$$
整格约化不改变这个重数，因为 $p\nmid|G|$。

选一个奇整数 $a$，其在 $G$ 中生成，定义原圆单位
$$
\eta_a=\zeta_p^{(1-a)/2}
       \frac{1-\zeta_p^a}{1-\zeta_p},\qquad
\beta_\chi=e_\chi[\eta_a].
\tag{1069.14}
$$
R1062 的真实截断对数公式给 $\chi=\omega^r$ 的 leading coefficient
$$
\frac{B_r(a^r-1)}{r\,r!}.
\tag{1069.15}
$$
此处 $r,r!$ 为单位，且非平凡 $\chi$ 给 $a^r\ne1\bmod p$。
good 条件恰保证 (1069.15) 为单位。故
$\operatorname{loc}_p\beta_\chi\ne0$。
这复用的是 R1062 的 $\lambda$-adic 截断；
不把实际 $\log(\zeta_p)=0$ 当作一个非零参数，
也不声称 $\eta_a/a$ 是全局单位。

同一实际局部角色 $(L^\times/L^{\times p})_\chi$ 为一维，
于是
$$
\boxed{\quad
\operatorname{loc}_p:
F(\{p\},p)_\chi
 \xrightarrow{\ \sim\ }
(L^\times/L^{\times p})_\chi .
\quad}
\tag{1069.16}
$$
在 (1069.5) 上取 $\operatorname{Hom}_G$，得到无正则性假设的
$$
\boxed{\quad
\operatorname{Hom}_G(W_{\rm good},F(\{p\},p))
 \xrightarrow{\ \sim\ }
\operatorname{Hom}_G(W_{\rm good},L^\times/L^{\times p}).
\quad}
\tag{1069.17}
$$

## 4. 用相对类数给 good forced 角色的统一下界

令 $i(p)$ 为通常 irregular index，即
$2\le r\le p-3$ 的偶数中 $p\mid B_r$ 的个数。
这里先给一个完全足够且常数明确的上界，
不引用未核的 irregular-index 密度猜想。

### 4.1 p-adic 类数 valuation 计入每个 irregular index

对复奇 Dirichlet 字符 $\theta$（conductor $p$），置
$$
B_{1,\theta}=\frac1p\sum_{a=1}^{p-1}a\theta(a),\qquad
h_p^-=\frac{h(K)}{h(F)}.
$$
prime cyclotomic field 的 Hasse unit index 为一，
故相对类数公式准确为
$$
h_p^-=2p\prod_{\theta\ {\rm odd}}\left(-\frac{B_{1,\theta}}2\right).
\tag{1069.18}
$$
取绝对值时 $h_p^->0$。

把字符值嵌入 $\overline{\mathbf Q}_p$，全部奇字符变为奇次
Teichmüller 幂。唯一可能非整的项为 $\theta=\omega^{-1}$：
$$
pB_{1,\omega^{-1}}
=\sum_{a=1}^{p-1}a\omega(a)^{-1}
\equiv p-1\equiv-1\pmod p,
$$
所以其 valuation 恰为 $-1$，准确抵消 (1069.18) 的前因子 $p$。
其它项均整；直接模 $p$ 求和也可见其分子被 $p$ 整除。

其余奇角色可唯一写成 $\theta=\omega^{r-1}$，
$2\le r\le p-3$ 为偶数。Kummer congruence (1069.7) 给
$$
p\mid B_r\Longrightarrow v_p(B_{1,\omega^{r-1}})\ge1.
$$
各 $r$ 对应不同因子，没有重复计数。因此
$$
i(p)\le v_p(h_p^-)\le\log_p h_p^-.
\tag{1069.19}
$$
这里只用正向整除，无需假设各 class-group eigenspace 循环，
也无需把 valuation 与 irregular index 宣为相等。

### 4.2 奇字符正交与精确常数24

对 $1\le a,b\le p-1$，奇字符正交关系为
$$
\sum_{\theta\ {\rm odd}}\theta(a)\overline{\theta(b)}
=m\bigl(\mathbf1_{a=b}-\mathbf1_{a=p-b}\bigr).
$$
故
$$
\begin{aligned}
\frac1m\sum_{\theta\ {\rm odd}}|B_{1,\theta}|^2
&=\frac1{p^2}
 \left(\sum_{a=1}^{p-1}a^2
       -\sum_{a=1}^{p-1}a(p-a)\right)\\
&=\frac{(p-1)(p-2)}{6p}.
\end{aligned}
\tag{1069.20}
$$
这里保 $1/p$ 的 Bernoulli 归一化、$m$ 个奇角色和
$a\leftrightarrow p-a$ 的第二项。

对这些非负平方用算术—几何平均不等式，
再代入 (1069.18)，得
$$
\begin{aligned}
h_p^-
&=2p\,2^{-m}\prod_{\theta\ {\rm odd}}|B_{1,\theta}|\\
&\le 2p\,2^{-m}
 \left(\frac{(p-1)(p-2)}{6p}\right)^{m/2}\\
&=2p\left(\frac{(p-1)(p-2)}{24p}\right)^{(p-1)/4}
=\mathcal H_p.
\end{aligned}
\tag{1069.21}
$$
这个 bound 的推导已在此完整给出；它不依赖任何有限 prime scan。

### 4.3 返回原 forced 模块

(1069.4) 的角色 $\chi_j$ 对应
$$
r_j=p-1-2j,\qquad 1\le j\le r_0.
$$
这些是互不相同、位于 $[2,p-3]$ 的偶整数。
其中 bad 的个数至多 $i(p)$，所以
$$
d_{\rm good}\ge r_0-i(p)
 \ge r_0-\lfloor\log_p \mathcal H_p\rfloor,
$$
证明 (1069.2) 的准确整数下界。

将 (1069.1) 取对数，
$$
\log_p \mathcal H_p
=1+\frac{\log2}{\log p}
 +\frac{p-1}{4}
  \left(1-\frac{\log24}{\log p}
   +\frac{\log((1-1/p)(1-2/p))}{\log p}\right).
$$
末项贡献 $O(1/\log p)$，且
$r_0=(p-1)/4+O(1)$，于是得到所称的 $\Omega(p/\log p)$。
一个不使用渐近记号的较弱下界为
$$
d_{\rm good}>
\frac{(p-1)\log24}{4\log p}
 -\frac52-\frac{\log2}{\log p}.
\tag{1069.22}
$$
它来自 $(p-1)(p-2)/(24p)<p/24$ 及
$r_0\ge(p-1)/4-3/2$。
例如仅用 $p\ge41$、$(x-1)/\log x$ 在该区间递增、
$\log41<4$、$\log24>3$ 与 $\log_p2<1/4$，
右侧严格大于 $19/4$。所以全部 $p>37$ 至少有五个
这样的原 forced good 角色。这个保守整数结论没有取代准确 (1069.2)。

## 5. 同一个原圆盘、真实覆盖和全部辅助条件

R1064 对任意实际 $W\subset V$ 的构造现在取
$W=W_{\rm good}$：
$$
H_{\rm good}=\operatorname{Hom}(W_{\rm good},\mu_p).
$$
原规范函数 $f_u=u^m/\prod_c\operatorname{lc}_c(u)$ 给一个
几何连通、全曲线 étale 的 $\mathbf Q$-torsor，
其 degree 恰为 $p^{d_{\rm good}}$。
子模块来自原 cusp 格，故这里不是另造一个抽象大秩覆盖。

R1065 证明原 $p$-local 标签在每个 $\mathbf Q_p$ 模 $p$ 圆盘恒定，
R1066 给每个这样的圆盘一个指定局部 embedding 的有界 CM 代表。
限制到 $W_{\rm good}$ 后仍成立。对每个 good $\chi$，
若该盘的实际标签读成
$$
\Phi_{x_p}(u_\chi)
=c_\chi\,\operatorname{loc}_p(\beta_\chi),
\qquad c_\chi\in\mathbf F_p,
$$
则 (1069.17) 给其唯一全局候选
$$
\phi(u_\chi)=c_\chi\beta_\chi.
\tag{1069.23}
$$
因此不同原盘可能给相同候选，但总候选数仍至多
$$
p\,n_{\mathbf Q_p}(p)
 \le\frac{2}{\pi}p^{3/2}\log(4p).
\tag{1069.24}
$$
全局候选是原局部值经 (1069.17) 的逆像，
不是某个高次数 CM 点的全局 norm 或未经证明的全局评价。

R1067 的所有 $\ell\ne p$ 好模型、真实 étale twists、
原圆单位剩余值与同一个 $y\in X(\mathbf F_\ell)$ 的全部角色方程，
逐字限制到 $W_{\rm good}$ 即可使用，包含 $\ell=2,3$。
R1068 的全部实际点集也不变，只把读数投到这些角色。

对 forced good $\chi_j$，实际可见性仍为
$$
\ell^{2j+1}=1\pmod p.
\tag{1069.25}
$$
选择 good 角色不会使不可见角色突然可见。
完整同标签的必要条件仍是
$$
\operatorname{loc}_\ell(\phi)
 \in\delta_{\ell,W_{\rm good}}(X(\mathbf F_\ell)),
$$
各角色及全部剩余 embedding 必须来自同一个原点 $y$。
未证明这些共同像排除每一个非 CM 候选，
也未证明坏角色无用或其类群为零。

## 来源与核读范围

- R. Sharifi, [Iwasawa Theory，Chapter 4](https://math.ucla.edu/~sharifi/notes/iwasawa-ch04.html)。
  实读 Lemma 4.2.17 的 prime-power Hasse unit index、
  Theorem 4.2.20 的相对类数公式、
  Theorems 4.5.6–4.5.7 的 Stickelberger/Herbrand 正向消去。
  本篇使用的具体标量与角色在 (1069.6)–(1069.7) 写明；
  real class group 的所需反射方向在 §2 自证。
- K. Prasanna, [Lecture 10: Herbrand's theorem](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/L10.pdf)，
  Theorem 10.1、Corollaries 10.2–10.3 的证明。
  只消费 $3\le i\le p-2$ 奇数范围的
  $B_{1,\omega^{-i}}\equiv B_{p-i}/(p-i)\bmod p$
  和 $\omega^{-1}$ 因子的唯一 valuation $-1$；
  不消费其后关于逆定理的叙述。
- R1062：原模块、forced 角色、准确 Galois 方向、
  原圆单位的截断对数及非平凡局部角色维数。
- R1064–R1068：原覆盖、每个实际 $p$-disk、
  有界 CM 代表、无条件 $p$-only 支撑和全部辅助约化点。

root 推导并逐式核原 forced 模块、Kummer 角色、
奇字符正交及类数上界；o2_high_coefficient 独立核
两个互逆角色、单位 kernel、常数24和完整整数下界。
全篇没有假设正则素数具有某个密度，没有用有限数据代替全素数结论。


[R1071](R1071-original-p-local-cuspidal-label-polynomials.md)
现给原每个 $p$-local residue disk 的完整有限多项式坐标；
在本篇 good 角色上按同一原 circular-unit 基除以非零 $b_\chi$，
准确产生本篇唯一 global 候选。其余 class-group 角色未因此消失，
实际辅助共同像排除仍须继续。
