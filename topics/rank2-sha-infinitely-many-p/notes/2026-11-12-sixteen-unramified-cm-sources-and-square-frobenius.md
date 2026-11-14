# 十六个完整类群源的非分歧证书与平方 Frobenius 简单零

日期：2026-11-12。**已证明。** 本篇保留 R150 的实际完整类群
映射，另选一个十六域族，使全部原 CM 中心的特征零微分非零。
再处理 CM 点可能只在 $\mathbb F_{p^2}$ 上定义的情形，证明源
互反函数非简单零的坏素数为 $O(X^{3/4})$。这些坏素数可在
R149 的同一大素因子筛集合中删除。

本篇不修改 R150，也不把总迹的简单零点当成原 $D_2Q$ 非零。

## 1. 新的固定十六域及实际类群映射

目标仍为
$$
 E=389\mathrm a1:y^2+y=x^3+x^2-2x,\qquad
 f=\sum_{n\ge1}a_nq^n,\quad
 \pi:X_0(389)\longrightarrow E,\quad\pi(\infty)=O.
\tag{1}
$$
把 R150 的 $D=-19$ 换成 $D=-532$，得固定集合
$$
 \mathcal D=\{-7,-11,-67,-20,-24,-35,-52,-187,-232,-267,
             -372,-483,-555,-795,-1435,-532\}.
\tag{2}
$$
其余十五域及 ramified 理想基保持 R150 的规范。新增域为
$F=\mathbb Q(\sqrt{-133})$，基本判别式 $D=-532$，其全部
reduced forms 是
$$
 (1,0,133),\quad(2,2,67),\quad(7,0,19),\quad(13,12,13).
\tag{3}
$$
它们都自反。norm 为 $1,2,7,14$ 的分歧理想乘积逐个约化，
准确给 (3) 的四个不同类。因此
$$
 h_F=4,\qquad\operatorname{Cl}(F)\simeq C_2^2,\qquad
 R_D=\{2,7\},\quad D_0=14.
\tag{4}
$$
还存在真正的 principal ordinary 素数
$$
 q_D=137=N(2+\sqrt{-133}),\qquad a_{137}(E)=-2.
\tag{5}
$$
$(D/389)=1$，并且 (2) 的十六个平方类独立。
附带脚本用有限 reduced-form 穷举、整数二元消元和 E 的点数
直接验证这些断言；没有调用类数或模形式数据库。

对每个 $D\in\mathcal D$，仍取
$$
 \Phi_D=\sum_{d\mid D_0}\pi\circ d_d:
       X_0(389D_0)\longrightarrow E,\qquad
 f_D(\tau)=\sum_{d\mid D_0}d\,f(d\tau).
\tag{6}
$$
$d_d$ 是实际退化映射。$\Phi_D^*\omega_E$ 是同一个非零
Manin 标量乘 $2\pi i f_D(\tau)d\tau$。
R150 §2 的证明适用于 (4)：选定基的各环类 lift 真为阶二，
在每个素于 $D_0$ 的导子上生成整个最大阶类群的一个补群。
所以 (6) 是全部类群和，不是可随意改变权的线性组合。

以下 $\Sigma_D$ 始终指最大阶、全部 $h_D$ 个理想类、两个
389 理想方向、以及 $D_0$ 的唯一分歧核给出的原 $2h_D$ 个点。
选固定 $t_0$ 杀掉 (2) 全部域的相关阿贝尔挠群，令
$\Psi_D=[t_0]\Phi_D$。R150 的完整基层迹证明给
$$
                         \Psi_D(c)=O\qquad(c\in\Sigma_D).
\tag{7}
$$
新族共有 $82$ 个这样的中心。

## 2. 真正 CM 标签与全部中心的严格微分证书

### 2.1 一个代表为何足够

令 $A=389D_0$，选下表的 b，并置
$$
 C=\frac{b^2-D}{4A},\qquad
 \tau_D=\frac{-b+i\sqrt{|D|}}{2A}.
\tag{8}
$$
脚本逐项证明 $(A,b,C)$ primitive、判别式为 D，且模 $2A$
的 primitive 根恰为 $b,2A-b$。

这确实给所需的层结构。记
$\beta=(-b+\sqrt D)/2=A\tau_D$。格
$\Lambda=\mathbb Z+\mathbb Z\tau_D$ 的自同态环为
$\mathcal O_F$，循环 A 子群由 $1/A$ 生成。
因 $\beta/A=\tau_D$，该子群为 $\mathcal O_F$ 稳定；其 A
部分分解为所选分歧理想核与一个 389 理想核。
中间 d 商就是 (6) 的 $d_d$，同时运输同一 389 方向。
因此它的 $d\mid D_0$ 项恰为完整理想类轨道。

固定一个 389 方向后，$\operatorname{Cl}(F)$ 在全部 $h_D$
个源点上传递；分歧核唯一，不增添另一套标记。
(6) 在 $\mathbb Q$ 上定义，故微分是否为零在这个轨道上不变。
另一个方向由复共轭得到。因此只需证明
$$
                            f_D(\tau_D)\ne0
\tag{9}
$$
就得到 $\Phi_D$、$\Psi_D$ 在 $\Sigma_D$ 的全部点非分歧。
这没有从类群不变性推断分歧或非分歧。

### 2.2 区间、完整系数和解析尾

下表最后一列是严格的实部开区间；并非舍入后的近似值。

| $D$ | $D_0$ | $b$ | $\operatorname{Re} f_D(\tau_D)$ |
|---:|---:|---:|---:|
| $-7$ | 1 | 185 | $(-19,-18)$ |
| $-11$ | 1 | 355 | $(-36,-35)$ |
| $-67$ | 1 | 189 | $(-16,-15)$ |
| $-20$ | 2 | 330 | $(-39,-38)$ |
| $-24$ | 2 | 216 | $(30,31)$ |
| $-35$ | 5 | 1595 | $(-17,-16)$ |
| $-52$ | 2 | 470 | $(-40,-39)$ |
| $-187$ | 11 | 3927 | $(-41,-40)$ |
| $-232$ | 2 | 508 | $(9,10)$ |
| $-267$ | 3 | 1137 | $(16,17)$ |
| $-372$ | 6 | 1866 | $(19,20)$ |
| $-483$ | 21 | 2037 | $(-46,-45)$ |
| $-555$ | 15 | 3975 | $(-25,-24)$ |
| $-795$ | 15 | 1305 | $(-75,-74)$ |
| $-1435$ | 35 | 2345 | $(-107,-106)$ |
| $-532$ | 14 | 2366 | $(26,27)$ |

全部 $a_n$，$n\le M=10000$，由两种独立的有限域点数产生：
一是 $y^2+y$ 的值频数，二是
$4x^3+4x^2-8x+1$ 的二次字符和。两者在所有所需素数一致；
再用乘法性、好位递推及 $a_{389}=1$ 产生全部整数系数。
系数向量的 SHA256 为

fb0e6b8e5cd6bf515097b4ed5af33d7f7fabd00c6c0343d875237d25ad500a44。

实际截断系数是
$$
 [q^n]f_D=\sum_{\substack{d\mid D_0\\d\mid n}}d\,a_{n/d}.
\tag{10}
$$
Hasse 界与 Hecke 递推给 $|a_n|\le d(n)\sqrt n\le2n$。
令 $y=\operatorname{Im}\tau_D$、$r_d=e^{-2\pi dy}$、
$M_d=\lfloor M/d\rfloor$。故整个被省略的复尾满足
$$
 \left|\sum_{n>M}[q^n]f_D\,e^{2\pi in\tau_D}\right|
 \le
 \sum_{d\mid D_0}2d\,r_d^{M_d+1}
 \left(\frac{M_d+1}{1-r_d}+\frac{r_d}{(1-r_d)^2}\right).
\tag{11}
$$
脚本以 Arb/Acb 的 192 位带误差运算求有限和及 (11)，全部尾
小于 $8\cdot10^{-31}$；再把该实尾上界同时加到实部和虚部的
误差半径，严格验证上表。于是 (9) 全部成立。

被替换的 $D=-19$ 在同一 $M=10000$、512 位的定向复核中
仅给
$$
 |\operatorname{Re}f(\tau_{-19})|,
 |\operatorname{Im}f(\tau_{-19})|<7.37\cdot10^{-148}.
\tag{12}
$$
区间仍含零，且此时误差由严格尾主导。本篇**没有**证明它为
零，也不用它证明非零；(2) 的替换使后续论证完全不依赖这一点。

证书：
[check-sixteen-full-class-cm-differentials.py](../scripts/check-sixteen-full-class-cm-differentials.py)。
依赖仅为已有的 python-flint。完整运行同时验证 (3)–(5)、
平方类秩、实际 CM forms、两套整数系数和上表各区间。

## 3. 完整旧形式对应的实际去 p 函数

删固定有限个素数：坏模型、层结构、Manin 标量、$t_0$、CM
微分非零值的分子分母，以及 $p\le5$。固定一个在 $F_D$ 分裂
且 E 好普通的剩余 p。所有 $\Sigma_D$ 中的源曲线均普通。

令 $\mathrm{Ha}$ 为 Hasse invariant，$\Theta$ 为 Katz 的
holomorphic theta，定义权零函数
$$
 g_{D,p}=
 \frac{\Theta^{p-2}\bar f_D}{\mathrm{Ha}^p}
 \in\mathbb F_p(X_0(389D_0)).
\tag{13}
$$
它在 ordinary locus 正则。必要时先在固定细模覆盖定义，再
按原 $\Gamma_0$ 标记下降。

若 $g_p$ 是原 level 389 的同一函数，则准确有
$$
                 g_{D,p}=\sum_{d\mid D_0}d_d^*g_p.
\tag{14}
$$
证明可直接看 q 展开：$(13)$ 的系数为
$\sum_{p\nmid n}([q^n]f_D)/n\,q^n$，(10) 使它等于
$\sum_{d\mid D_0}\sum_{p\nmid m}a_m/m\,q^{dm}$。
这是权零等式，故 q 展开原则给 (14)。特别地 (14) 没有
额外的 d 权；d 权属于微分 $f_D$。

对 $\bar c\in\Sigma_D$，每个 $d_d(c)$ 均为原 level 389 的
canonical-lift 点。Buium–Poonen（2009）Theorems 3.5、
3.17(2) 对原 newform 参数化适用：目标 E 非 CM，所以不能
是 canonical lift。该定理用于这些真实点的整数和，并结合
$(t_0\Phi_D)(c)=O$，给
$$
                            g_{D,p}(\bar c)=0.
\tag{15}
$$
这里没有把 $f_D$ 误称为新 level 的 newform，也没有漏掉完整
类群项。所有项使用同一个目标微分规范，故原 Manin 单位共同
提出。源的 $j=0,1728$ 约化只增添固定有限例外。

由于 $p\nmid389D_0$，$f_D$ 满足原 E 的 p-Hecke 递推。
同权 q 展开原则准确给
$$
 \Theta^{p-1}\bar f_D
 =\mathrm{Ha}^{p+1}\bar f_D
       -a_p(E)\,\mathrm{Ha}^{p-1}\bar f_D^{\,p}.
\tag{16}
$$
两边权均为 $p^2+1$。因此在 $\mathrm{Ha}=1$ 的 Igusa 框架，
以 $\mathcal D$ 记实际 Kodaira–Spencer 导数，
$$
                      \mathcal Dg_{D,p}=h-a_p(E)h^p,
                  \qquad h=\bar f_D\big|_{\rm Igusa}.
\tag{17}
$$
Igusa 覆盖在 ordinary locus étale，这个导数在中心是局部
参数导数的单位倍。第 2 节保证 $h(\bar c)\ne0$，故 (15) 是
简单零当且仅当 (17) 在该点非零。

## 4. 类群指数二时的平方 Frobenius 与完整周期规范

不能在本族直接断言每个 split p 的 CM 点都在 $\mathbb F_p$
上定义。其定义域为 Hilbert 类域；Frobenius 的类群阶至多二。
所以原 CM 对象及循环层结构可在 $\mathbb F_{p^2}$ 上取模型。
具体地，原 j 值在 $\mathbb F_{p^2}$；取这个 j 的一个模型，
其普通几何自同态环仍是最大阶 $\mathcal O_F$。Frobenius 与
整个交换的自同态环相交换，因此所需 CM 理想核均在
$\mathbb F_{p^2}$ 上定义。选另一模型的二次扭曲不改变这些核。
若需细模标记，可再作有限扩域，但下述 weight-two 值本来就在
原 $\Gamma_0$ 对象上定义，不需把该扩域的 Frobenius 误作 p。

选择这个 $\mathbb F_{p^2}$ 模型的非零不变微分 $\omega_0$，令
$$
 A=\mathrm{Ha}(C_c,\omega_0)\in\mathbb F_{p^2}^{\times},\qquad
 f_0=\bar f_D(C_c,\text{原层结构},\omega_0)
                      \in\mathbb F_{p^2}^{\times}.
\tag{18}
$$
存在 $\omega_{\rm Ig}=\Omega\omega_0$，满足
$$
           \Omega^{p-1}=A,\qquad h=\Omega^{-2}f_0.
\tag{19}
$$
这是微分之比的方向，不能用形式群同构导数的倒数规范替换。
因为 $f_0^{p^2}=f_0$，
$$
                    h^{p^2}=A^{-2(p+1)}h.
\tag{20}
$$

令 $\pi_{c,p^2}\in\mathcal O_{F_D}$ 为该模型的 $p^2$-Frobenius，
$T=\operatorname{Tr}_{F_D/\mathbb Q}\pi_{c,p^2}$。则
$$
                         A^{p+1}\equiv T\pmod p.
\tag{21}
$$
这里的 Hasse 规范可不依赖周期文献而直接校准：写源模型为
$y^2=P(x)$、$\omega_0=dx/(2y)$，则 A 是
$P(x)^{(p-1)/2}$ 的 $x^{p-1}$ 系数。有限域点数给 T 模 p 为
$P(x)^{(p^2-1)/2}$ 的 $x^{p^2-1}$ 系数。
分解为 $Q(x)Q^{(p)}(x^p)$，其中 $Q=P^{(p-1)/2}$，
且 $\deg Q=3(p-1)/2<2p-1$。在 $j+pk=p^2-1$ 中唯一可能的
指标为 $j=k=p-1$，故该系数正是 $AA^p$。
任意改选 $\mathbb F_{p^2}$ 微分不改变 $A^{p+1}$；二次扭曲
最多改变 T 的符号，下面只用其平方。

若 (17) 为零，则 $h=a_p(E)h^p$，再取 p 次幂并用 (20)，得到
$$
                         a_p(E)^2\equiv T^2\pmod p.
\tag{22}
$$
这是必要条件，足够用于上界；本篇不把它在剩余次数二时
升级为充分条件。尤其所有周期和单位尺度均已在 (18)–(21)
明确处理。

## 5. 固定二次型给全部坏素数 $O(X^{3/4})$

取 $\mathfrak p\mid p$ 使 $(\pi_{c,p^2})=\mathfrak p^2$；
若方向相反，交换两个 p 理想即可。选 R150 的一个真实
ramified 乘积理想 $\mathfrak a$，使
$$
 [\mathfrak a]=[\mathfrak p],\qquad
 N\mathfrak a=d,\quad d\mid D_0,\qquad
 \mathfrak a^2=(d).
\tag{23}
$$
于是 $\mathfrak p\mathfrak a=(\beta)$，$N\beta=dp$，
且 $\mathfrak p^2=(\beta^2/d)$。本族的单位只有 $\{\pm1\}$，
故
$$
 \pi_{c,p^2}=\pm\frac{\beta^2}{d},\qquad
 \beta=\frac{a+b\sqrt D}{2},\quad
 a^2+|D|b^2=4dp.
\tag{24}
$$
D 偶时 a 为偶数；只数所有整数 a,b 是合法上界。
由 $\beta^2/d\in\mathcal O_F$，
$$
                 T=\pm\left(\frac{a^2}{d}-2p\right),
\tag{25}
$$
特别 $a^2/d$ 是整数。结合 (22)，有某个
$\varepsilon\in\{\pm1\}$ 使
$$
       \frac{a^2}{d}-\varepsilon a_p(E)=kp,\qquad
                        k\in\{0,1,2,3,4\}
\tag{26}
$$
对 $p>4$ 成立；这使用 $0\le a^2/d\le4p$ 和 Hasse 界
$|a_p(E)|\le2\sqrt p<p$。

若 $p\le X$，消去 p 得
$$
 |(4-k)a^2-k|D|b^2|\le8d\sqrt X,\qquad
 |a|\le2\sqrt{dX},\quad |b|\le2\sqrt{dX/|D|}.
\tag{27}
$$
$D,d$ 来自固定有限集合。$k=0,4$ 时，一个变量为
$O(X^{1/4})$、另一个为 $O(X^{1/2})$，故各为
$O(X^{3/4})$ 对。当 $1\le k\le3$，在非负象限写
$\alpha=\sqrt{k|D|/(4-k)}$。$b\le X^{1/4}$ 时两变量均为
$O(X^{1/4})$；其余 b 上，(27) 给
$$
              |a-\alpha b|\ll\sqrt X/b.
\tag{28}
$$
逐 b 求和为 $O(\sqrt X\log X)$。加上符号、d、D 和有限中心，
所有例外素数的并集满足
$$
 \#\{p\le X:\ p\text{ split 某 }F_D,\ 
       g_{D,p}\text{ 在某个原中心非简单零}\}
                         =O(X^{3/4}).
\tag{29}
$$
每个格点由 (24) 确定唯一 p，所以上界没有隐藏一个额外的 p
求和。全部固定有限坏位可吸收到同一常数中。

## 6. 和实际无穷小高度输入在同一筛中合并

新增域 (4)–(5) 满足 R150 §2–6 用到的全部具体假设：
真实指数二 ramified 基、principal ordinary q、389 Heegner
条件和完整类群的固定映射。因此可把 R150 的固定进程 C、
阈值和 t0 同时为 (2) 选定；不改变其原 ST/Gauss/整数
$q-N_n$ 证明。新的 B 在应用筛法之前一次固定。

(2) 仍有十六个独立二次字符，所以 R149 的全部惯性坏类比例
仍恰为 $2^{-16}$，其绝对常数 64 和正余量均保持。
由 R150 的同一联合删除，得到 $\gg_B x/\log x$ 个
$$
 \ell\equiv-1\pmod B,\qquad
 p=P^+(\ell+1)>x^\theta,\quad\theta=667/1000,
\tag{30}
$$
其中 p 至少在一个新族域中分裂，原 E 普通非异常、
$a_\ell(E)$ 为 p 单位，且全部十六域的完整原点均非扭、
范数零、高度 $o(p)$。

还须把 (29) 转成同一组 $\ell$ 的坏量，而不是直接相交密度。
每个坏 $p>x^\theta$ 至多对应 $x/p+1\ll x/p$ 个
$\ell=pu-1\le x$。由 (29) 的分部求和，
$$
 \#\{\text{因 (29) 删除的 }\ell\}
 \ll x\sum_{\substack{p>x^\theta\\p\ {\rm bad}}}\frac1p
 \ll x^{1-\theta/4}
                         =o(x/\log x).
\tag{31}
$$
这里求和可截止 x；无限尾上界也收敛。有限多个域的并集已经
纳入 (29)，因此不会改变正筛余量。

有限鸽巢最终给一个固定 $F_*$，以及无穷多个不同的 p 与相应
$\ell$，同时满足 R150 (26) 的全部实际小高度和分裂条件，
并且
$$
  g_{D_*,p}\text{ 在 }\Sigma_{D_*}\text{ 的每个原 CM 中心
  都是简单零点}.
\tag{32}
$$
真实 $\ell+1$ 个 Hecke 分支的总迹仍为
$a_\ell(E)g_{D_*,p}$，所以其原源零点也简单。
这保留原 $h_{F_*}u$ 个类群与 U 项；没有改成可任意选择的
另一个 Cartan 标记。

范数一簇 Sha 有限、原点 O 指数的已有上界仍适用。
(32) 本身不排除指定 $C_p$ 纤维的二阶矩全部为零：
还需 R142/R145/R148 所保留的实际共同零/判别式条件。
故本篇没有证明 $a\le1$，也没有宣称主课题完成。

## 来源与可重复证书

- C. Cornut，*Mazur's conjecture on higher Heegner points*，
  Invent. Math. **148** (2002), 495–523，
  [作者发表版](https://webusers.imj-prg.fr/~christophe.cornut/papers/mcinv_published.pdf)，
  引言 pp.2–3、§1.4 的 CM 互反作用、§4 Theorem A。
  本篇的具体 primitive forms 与 ramified 基另由整数证书核定。
- N. Katz，*A result on modular forms in characteristic p*，
  LNM **601** (1977), 53–61，
  [作者全文](https://web.math.princeton.edu/~nmk/old/modformcharp.pdf)，
  §I 的 Hasse 定义与 q 展开原则、§II 的 theta 定理；
  *Serre–Tate local moduli*，LNM **868** (1981), 138–202，
  [作者全文](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)，
  Main Theorems 4.3.1–4.3.2。
- A. Buium、B. Poonen，*Independence of points on elliptic curves
  arising from special points on modular and Shimura curves, II:
  local results*，Compositio Math. **145** (2009), 566–602，
  [作者全文](https://math.mit.edu/~poonen/papers/local.pdf)，
  Theorem 3.5、Remark 3.6、Theorem 3.17(2)，§4.3 式 (4.8)。
  这里仅对原 level 389 使用 newform 识别，再对真实退化点相加。
- F. Johansson，*Arb: Efficient Arbitrary-Precision Midpoint-Radius
  Interval Arithmetic*，IEEE Trans. Computers **66** (2017),
  1281–1292，[作者预印本](https://arxiv.org/abs/1611.02831)。
- [完整整数与 Arb 脚本](../scripts/check-sixteen-full-class-cm-differentials.py)；
  R136 已付 E389 的模型、原 newform 和参数化规范；
  R149–R150 已付完整筛法、指定 ST 分支及高度预算。
