# 混合权 period 图、通常 Selmer 范围与高度差新文献核查

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**可信度：文献及既有证明接口核查；不登记新的算术结论。**
本轮直接读取 Kato 2004、BKO 2021、BKO 2024、AH 2006 的原文，
核查 R970 的通常全 Selmer 桥是否被“只对 rank 至多一成立”或
高权 motivic 比较的未证部分截断。下面把实际检查到的逻辑写出，
不把结果编号本身当作证明，也不声称重新证明 R970 的全部 theta 来源。
主目标仍未完成。

## 1. 审核的准确链条

固定 R970 的曲线

$$
E_*:y^2=x^3+65^3,
\qquad E_1:y^2=x^3+1,
\qquad K=\mathbf Q(\sqrt{-3}).
$$

惰性部分的相关链条为 R970 §9 → R959 的惰性桥 → R303 §§3–6。
关键不是只在有限阶角色处的插值，而是对所有
$m>0$、$p+1\mid m$ 的相对赋值式

$$
v_p\mathcal A_{*,p}(x_m)
=v_p\mathscr E_{*,m}-v_p\mathscr E_{1,m},
\qquad
\mathscr E_{j,m}
=\frac{(2\pi/\sqrt3)^m L(\psi_j^{2m+1},m+1)}
 {m!\varpi_j^{2m+1}}.
\tag{1}
$$

R970 的式 (45) 再把 (1) 与原来源的全权平方及参考系数卷积合并。
若 (1) 只差一个依赖于 $m$、赋值未知的 period，后续比较
$m=(p+1)p^n$ 的消失阶就不成立。因此必须检查 period 的实际身份。

## 2. Kato 的两张图足以完成这个 period 拉回

### 2.1 原文的已证部分与明确未证部分

Kato，*p-adic Hodge theory and values of zeta functions of modular forms*，
Astérisque **295** (2004), 117–290：

- §15.8，印刷页 256–258：CM Hecke character 的 Betti 线、
  $S(\psi)$、period map 及 de Rham 比较，由 CM 椭圆曲线的
  **秩一张量幂**构成。
- Lemma 15.11，印刷页 260–262：任选一个
  $s:S(\psi)\simeq S(f)\otimes L$ 后，分别定义一个 étale 比较
  $\iota_{\rm et}$ 和一个 Betti 比较 $\iota_B$；前者使 de Rham
  图交换，后者使复 period 图交换。
- 紧接着的印刷页 263：作者明确说，权至少三时，不知道
  $\iota_B$ 与 $\iota_{\rm et}$ 是否来自同一个 motivic 比较。
- **式 (15.16.1)，印刷页 265，是已证明的独立陈述：**
  椭圆单位类乘相应 CM tensor 向量后的像，等于以
  $\gamma'=\iota_B(\gamma)$ 为标签的 Beilinson–Kato 类。
  该等式没有要求前一条未证明的 motivic 相容性。
- Theorem 12.5(1)，印刷页 221：该标签的 Kato 类在任一临界
  cyclotomic 权的 dual exponential，经 period map 后给相应
  $L$ 值及 $(2\pi i)^{k-r-1}$ 因子。

所以，仅引用 p.263 的保留并不能否定 R303。必须检验其论证是否
偷偷把两种比较当成相同；当前桥使用的是上面的已证复合。

### 2.2 中间缩放如何实际消去

令 $N=2m+1$，取 $\psi_j^N$ 对应的新形式 $f_{j,m}$，权为
$k=N+1=2m+2$。把 $D_j=S(\psi_j^N)$ 看成 CM 微分的秩一张量线。
取张量微分 $d_j$ 和与真实 CM 格对应的 Betti 基 $b_j$，于是

$$
\operatorname{per}_{\psi_j^N}(d_j)=\varpi_j^N b_j.
\tag{2}
$$

任选 $s_j:D_j\simeq S(f_{j,m})\otimes L$。
两张定义性图分别给

$$
D_{\rm dR}(\iota_{{\rm et},j})(d_j)=s_j(d_j),
\qquad
\operatorname{per}_{f_{j,m}}(s_j(d_j))
=\varpi_j^N\iota_{B,j}(b_j).
\tag{3}
$$

Kato (15.16.1) 把同一 elliptic-unit tensor 类送到
$z^{\rm Kato}_{\iota_{B,j}(b_j)}$。在 Theorem 12.5(1) 中取
$r=m+1$，其 exponential 的 period 是

$$
(2\pi i)^m L^{(p)}(\psi_j^N,m+1)\,
  \iota_{B,j}(b_j)^{(-1)^m}.
\tag{4}
$$

这里上标表示所需的复共轭特征投影，不表示幂。
把 (4) 用 (3) 拉回 $D_j$，所得系数为

$$
\frac{(2\pi i)^m L^{(p)}(\psi_j^N,m+1)}{\varpi_j^N}.
\tag{5}
$$

若把 $s_j$ 乘任意非零代数标量，(3) 中的 étale 图和 Betti 标签
同时按同一标量改变；(5) 不变。此消去逐权成立，不需要标量随权
解析，也不需要断言 $\iota_B\otimes L_\lambda=\iota_{\rm et}$。
这给出了 R303 §4.1 中“中间缩放消去”的具体图运算。

在 $δ=i\sqrt3$ 的规范下，(5) 与 $\mathscr E_{j,m}$ 相差

$$
\delta^m m!\,\left(1+\frac1p\right).
\tag{6}
$$

$m!$ 和 $1+1/p$ 可能不是单位；它们是两条曲线完全相同的因子，
在相对式中抵消。不能分别把它们丢掉。

### 2.3 两条特化路线与整模型

对完整 ray-class 椭圆单位系统作反圆分角色特化，或先作
$N$ 次 CM tensor 再作 Kato 的中央 cyclotomic 特化，两条路径均为

$$
T_j^{-N}(m+1),
\qquad
\mathbf u_j\otimes b_j^{\otimes N}\otimes\zeta^{\otimes m}.
\tag{7}
$$

这里使用 $\chi_m^{-1}=\psi_j^{-2m}\chi_{\rm cyc}^{m}$。
$6\mid m$ 消掉有限 CM 扭转，而 $p+1\mid m$ 消掉惰性 tame 分支；
所以是同一反圆分角色，不是移到另一分支以后借用非零值。
tensor、norm、局部化和特化作用于同一系统，(7) 支付了“同一个类”接口。

在 $p\nmid 2\cdot3\cdot5\cdot13$、$p\equiv5\pmod6$ 时，
取 $\theta^6=65^3$。因 $\mathbf F_p^\times$ 包含于
$\mathbf F_{p^2}^{\times6}$，$\theta$ 可取为 $\mathbf Z_{p^2}^\times$
中的元素。于是

$$
F_\theta:E_1\simeq E_* ,
\qquad F_\theta^*\omega_*=\theta^{-1}\omega_1
\tag{8}
$$

是光滑整模型及完整 CM Tate 格的同构；$N$ 次 tensor 比为
$\theta^{-N}$，仍是单位。有限射线类下降的次数只含 $2,3$：
目标导子 $(130\delta)$ 的射线类次数为 $3456$。
Kato 的 canonical CM-pair 和原模型之间的导子 isogeny 次数只含
相应导子素因子。这里不通过带阶乘分母的对称幂投影。

若为书写两系统而扩大参考的有限导子，必须保留 norm 产生的
Euler 因子。R970 单独保留了 split $13$ 的权依赖因子；它沿
$p+1\mid m$ 的当前分支模 $p$ 为 $12/13$，故在这些 $p$ 为单位。
它不是一个可以在所有权上直接代入的常数。惰性 $5$ 因子为
$6/5$，同样为单位。以上对整性的检查与 (6) 的准确抵消分开。

**核查结果：**在 R970 已给原全权平方的前提下，未发现其式 (45)
在 Kato period 比较这一环节的缺口。这里不由此替代对 R970
有限 theta 来源或后续中央非零问题的证明。

## 3. BKO 的上界确实包括完整通常 Selmer 群

BKO 2021，*Rubin's conjecture on local units in the anticyclotomic
tower at inert primes*，Annals **194** (2021), 943–966：

- §2，印刷页 948–949：平凡角色的 conductor 是 $1=p^0$，属于
  $\Xi^+$；Theorem 2.1 给完整 signed 整分解。
- §6.0.2，印刷页 961–962：假设 $p\nmid h_K$，CM Q-curve 满足
  Shimura 条件且在 $p$ 好约化；并没有把有限导子限制为仅含分歧素数。
  Theorem 6.1 给 signed Selmer 模的 characteristic ideal。
- **Theorem 6.2，印刷页 962–963，正文中间量是**
  $\dim\operatorname{Sel}(K_n,V_pE)^\chi$，而不只是 Mordell–Weil 秩。
  证明最后一行把正确信号处的 signed 基层局部条件与通常条件相等。
  因此根数正、平凡角色处给
  $\dim\operatorname{Sel}(K,V_pE)\le\operatorname{ord}_0 L_p$，无加一项。
- 紧后的 Remark 6.3 把 **等号和完整 $p$-adic BSD 公式**限制于
  解析秩至多一；这个限制不回溯到 Theorem 6.2 的一般上界。

对 $E_*$，$h_K=1$，且与 $-3$ 二次扭转有有理三同源。
在 $p\ne2,3$，restriction、corestriction、二次特征投影及该同源
给通常 Selmer 的 $\mathcal O$-余秩恰为

$$
2+\operatorname{corank}_{\mathbf Z_p}\Sha(E_*/\mathbf Q)[p^\infty].
$$

因此 R970 使用的方向确实控制完整通常 Selmer 群；没有先把未知
$V_p\Sha$ 去掉。BKO 2024 Corollary 4.11(i) 的证明另行给出：
参考中央代数值为 $p$-单位时，参考 Rubin 函数是
$\Lambda^\times$。这支持 R303/R970 用参考类作为实际 signed 整基，
而不是任意指定未知局部 period 为单位。

普通素数部分也核过 AH，*Anticyclotomic Iwasawa theory of CM
elliptic curves*，AIF **56** (2006), 1001–1048，Theorem 2.4.17(1)，
印刷页 1034。根数 $+1$ 时的 torsion/characteristic-ideal 陈述
没有 rank 至多一假设；整版本另要求
$p\nmid[K(\mathfrak f):K]$，对当前导子其次数 $3456$ 已满足。
这只核查外部定理范围；原 ordinary 测度及其 source 身份仍由
R295/R959/R970 中各自的局部构造承担。

## 4. 新高度差预印本没有支付秩二 determinant 或无穷素数

直接取得并读取 Taiga Adachi、Yu Katagiri、Ryota Shii，
*A difference formula of p-adic height pairings via the Bloch–Kato
logarithm map*，arXiv:2609.35626v1，2026-09-28。

其 Theorem 1.1 在两个 Frobenius eigenspace 给 Hodge splitting 的
假设下，写出两个 cyclotomic 高度之差为局部 Bloch–Kato 对数的平方。
Corollary 1.3 在不同 eigenvalue、非零 localization 下推出至少一个
高度**不恒为零**；特征多项式不可约时两者都不恒为零。

这里有三个必要的范围界限：

1. Hypothesis 4 要求 $\omega,\varphi\omega$ 独立。导言 p.3
   明确说明，对有好约化的椭圆曲线它等价于没有 ordinary CM；
   因此不能直接应用到本课题的 ordinary CM 素数。
2. Remark 1.2(4) 明确说明，椭圆曲线的高度差公式是已知结果，
   新推广主要针对高权二维自对偶表示。
3. 即使在本课题的惰性素数应用其结论，不恒为零也不等于秩二
   regulator 非零，更不限制额外的 $V_p\Sha$ 方向。

最后一点有保留 Galois 共轭性的精确线性代数模型。
取域 $F$、二次扩域 $L/F$，令 $\alpha,\beta$ 是不可约二次式的两根，
在任意维数 $s\ge2$ 的 $F$-空间 $S$ 上取非零 $F$-线性形式 $\ell$。
置

$$
h_\alpha(x,y)=\alpha\ell(x)\ell(y),\qquad
h_\beta(x,y)=\beta\ell(x)\ell(y).
$$

这两个对称配对互为 Galois 共轭、均非零，差为
$(\alpha-\beta)\ell(x)\ell(y)$；但两者都有余维一的共同 radical。
任意增大 $s$ 仍满足同样差公式。因此差公式与非零 localization
本身不能推出 $s=2$ 或秩二 determinant 非零。
本例只否定该逻辑推论，不声称实际算术高度等于这个模型。

一般秩二形式的 rank-one update 还给

$$
\det(H+t\ell\ell^t)
=\det H+t\ell^t\operatorname{adj}(H)\ell.
$$

右侧第二项正是 strict 对数核方向的自高度；R39 已把此项列为
未解非线性 period 条件。本轮不把这个旧障碍重复登记为新结果。
也不采用该预印本中任何未在此完整证明的结论来宣布主目标完成。

## 5. 一手来源与后续实际接口

- K. Kato (2004)：[完整原文](https://www.numdam.org/article/AST_2004__295__117_0.pdf)。
- A. Agboola、B. Howard (2006)：[完整原文](https://www.numdam.org/article/AIF_2006__56_4_1001_0.pdf)。
- A. Burungale、S. Kobayashi、K. Ota (2021)：
  [完整原文](https://par.nsf.gov/servlets/purl/10336626)，
  [出版页](https://annals.math.princeton.edu/2021/194-3/p08)。
- 同三位作者 (2024)，*p-adic L-functions and rational points on CM
  elliptic curves at inert primes*，JIMJ **23**, 1417–1460：
  [完整原文](https://catalog.lib.kyushu-u.ac.jp/opac_download_md/7330258/7330258.pdf)。
- A. Lei、D. Loeffler、S. Zerbes，*Critical slope p-adic L-functions of
  CM modular forms*，Lemma 2.26 和 Theorem 2.28，分别重述 Kato
  两张不同图及已证的 elliptic-unit/Kato 类身份：
  [作者原文](https://antoniolei.com/wp-content/uploads/2014/09/critical.pdf)。
- Adachi、Katagiri、Shii (2026)：
  [预印本](https://arxiv.org/abs/2609.35626)，
  [完整原文](https://arxiv.org/pdf/2609.35626)。

本轮未重复上一会话
[全局路线记录](2026-11-26-global-7d29.md) 已排除的固定 $p$、改变曲线、
Selmer 秩至多一或条件性的广义 Kato 路线。
已核接口继续允许把研究精力放在 R970 原 degree-$130$ 中央项的
真正非零、完整来源提取及跨素数机制上；当前文献核查没有给出
“无穷多个 $p$”的替代定理。
