# R1009 — 固定的新最高图扩张、1-motive 张量范畴障碍与跨 ℓ 比较的准确范围

日期：2026-11-27。会话：`Astra-rank2-Sha-0b097461-20261127`。

**已证明。** 本篇先固定 R1006 的一个真实代数循环，再用已支付的
7993 检测证明其三个原最高扩张均非平凡。它们甚至在这个单一素数处
也不属于有限个 1-motive 经张量、对偶和子商生成的表示范畴。此排除
针对混合扩张；其纯 CM 分次本来就由椭圆曲线的张量构成。

另证明两个准确的范围结论：Frobenius 特征多项式不能判定这些扩张
是否分裂；一次固定有限域约化只能为固定循环提供有限多个 ℓ 的
挠检测。本文不将已证的纯 monodromy 独立性改写成数域上的混合
Abel–Jacobi 保真定理，也不据此宣称其它 ℓ 的非零。

## 1. 先固定一个实际循环，且准确检测原 $P_-$

记 $K=\mathbf Q(\omega)$、$\delta=1+2\omega$，系数域
$E=\mathbf Q(\zeta_9)$。沿用 R1006 的 $E_{27}:y^2+y=x^3$、
曲面 $S$、全部54条 degree34 图、全部有限角色和有限定义域 $L/H/K$。
这里字母 $E$ 表示系数域，$E_{27}$ 表示椭圆曲线。

**现在固定一次**
$$
p_*=7993,\qquad \mathfrak p_*=(69-32\omega),\qquad
\omega\mapsto4748,\quad\zeta_{18}\mapsto203\pmod {7993}.
\tag{1}
$$
这正是 R817 的指定素位与系数嵌入，不另选 ordinary 方向。
对 $j=4,10,16$ 置
$$
Y_j=P_-e_{\eta_j}\operatorname{Cor}_{L/H}
 Z_{j,p_*,L}^{[p_*]}.
\tag{2}
$$
右侧完全采用 R1006(3)–(4)、(55)：每一条图都保留其修正项及
三个系数 $1,-A_{p_*}/p_*^2,1/p_*^2$；次数是
$34,34p_*,34p_*^2$，$e_{\eta_j}=18^{-1}\sum\eta_j(\sigma)^{-1}\sigma$。
$P_-$ 是 R995 的严格 Chow projector。由此(2)是一个先于后续
实现素数 ℓ 固定的、带 $E$ 系数的同调零循环。

准确地说，(2)先是 $H$ 上的 $\eta_j$ 特征投影；将它与
$\eta_j^{-1}$ 的 Artin 动机一起下降，就得到 $K$ 上的固定 Chow
对象及其 AJ 类。也可先在一个包含全部有限定义数据的固定数域
$F/K$ 上工作，再保留这个 Artin 标号。这两种说法不把“几何作用
于循环”改成“同时共轭系数”。

### 1.1 非零只经原 Katz 值输入，不经旧循环的帽号

R817(23)–(24)已经严格证明原三个单位负二矩 $I_{j,-2,p_*}$ 非零。
R806(33)是
$$
\mathcal K^{\rm prim}_{34\delta}(\widehat\nu_j)
=34^2c_j\theta^9\Omega_{p_*}I_{j,-2,p_*}^{\,2},
\quad
\nu_j=\eta_j\psi_0^{-1}\bar\psi_0^2,
\tag{3}
$$
其中全部显示因子非零。这里不使用 R817 关于旧 R814 循环的
任何 projector 标签。

R1002(13)、(16)及 R1006 保持的角色是同一个完整 $\nu_j$。
从模数 $34\delta$ 改写到 $\mathfrak c=34\delta^2$ 没有增加
被移去的素理想：$\nu_j$ 已在 $2,\delta,17$ 分歧。因此两种
Katz 记法的坏 Euler 因子均为1，模数提升只是同一有限角色的
inflation。若换用 $E_{27}$ 的原微分及 CM period，须同时换复、
$p$ 周期；这种平凡化变化在固定权处乘非零因子。由同一
Katz 插值/分布关系，(3)给
$$
\mathscr K_{p_*,\mathfrak c}(\nu_j)\ne0.
\tag{4}
$$
这一步使用完整角色，未把其在(1)处的值 $-1$ 当作全局角色。

R1002 又给 $\beta_j=\psi_{27}\eta_j$ 的
$\mathscr K_{p_*,\mathfrak c}(\beta_j)\ne0$。于是 R1006(5)、(55)
准确给
$$
\operatorname{AJ}_{p_*}(Y_j)(\Omega_S\omega_{E_{27}})^2
=\iota_{p_*}(-486\omega34^2)[L:H]^2\Omega_{p_*}^2
\mathscr K_{p_*,\mathfrak c}(\nu_j)
\mathscr K_{p_*,\mathfrak c}(\beta_j)\ne0.
\tag{5}
$$
式(5)按原 $H$ 上有限和写；下降至指定 Artin de Rham 基再乘
R1006(57)的非零 $a_{j,p_*}^{-1}$，不改变非零。这里不要求任一
代数常数为7993单位，也不重算7993。

令 $\chi_{27,\ell}$ 是 $T_\ell E_{27}$ 上的算术 CM 角色，
$\varepsilon_\ell$ 是 cyclotomic 角色。**原目标**始终是
$$
V_{j,\lambda}
=E_\lambda(\eta_j^{-1}\chi_{27,\ell}^3\varepsilon_\ell^{-1}),
\qquad\lambda\mid\ell.
\tag{6}
$$
由 $\psi_{27}^3=\psi_0^3$，(6)是 R804 的原完整角色。
按 R1006(53)，它是 $H^3(2)$ 的 $P_-$ 行；测试微分在 $P_+$
行，二者由转置配对。本文没有把 $P_+$ 的上同调帽号移到(6)。

记(2)的原下降 AJ 类为
$$
a_{j,\lambda}=\operatorname{AJ}_{\lambda}(Y_j)
\in H^1(K,V_{j,\lambda}).
\tag{7}
$$
在(1)选定的 $\lambda_*\mid7993$，有 $E_{\lambda_*}=\mathbf Q_{7993}$，
且由(5)
$$
a_{j,\lambda_*}\ne0\qquad(j=4,10,16).
\tag{8}
$$
其它两个允许的系数嵌入会置换三个标签；R817 已支付三者全非零，
所以没有将该置换猜成某个新角色同一。

有限扩域不杀(8)。对任意有限 $F/K$，restriction 后再
corestriction 是 $[F:K]$ 倍；在特征零系数中该数可逆。因此
$$
\operatorname{res}_{F/K}a_{j,\lambda_*}\ne0.
\tag{9}
$$

## 2. 这个非平凡扩张的幺幂部分恰为原最高线

固定一个 $j$，暂写 $k=\mathbf Q_{7993}$、$V=V_{j,\lambda_*}$。
类(8)给非分裂扩张
$$
0\longrightarrow V\longrightarrow\mathcal E_j
\longrightarrow k\longrightarrow0.
\tag{10}
$$
在一个向量空间分裂中，矩阵为
$$
\rho_{\mathcal E_j}(g)=
\begin{pmatrix}\rho_V(g)&c(g)\\0&1\end{pmatrix}.
\tag{11}
$$
令 $G_j$ 为其代数 monodromy 群。若 $R_u(G_j)=1$，则其
单位连通分支是特征零 reductive 群，有限分支群也线性约化；
所以表示(10)完全可约，与(8)矛盾。

另一方面，(11)使 $R_u(G_j)$ 是上三角平移群 $\mathbf G_a$
的代数子群。特征零下非平凡连通子群只能是整个
$\mathbf G_a$。对平移参数的共轭作用正是 $\rho_V$。故
$$
\boxed{R_u(G_j)=\mathbf G_a,\qquad
\operatorname{Lie}R_u(G_j)\simeq V
\quad\text{作为 }G_K\text{ 模。}}
\tag{12}
$$
这里非平凡性不是由纯角色的无限像猜得，而是(8)实际保证。
(9)说明任意有限扩域后(12)仍成立。

约定 $\mathbf Q_\ell(n)$ 的 **Tate 指数**为 $n$，以免与相反号
的 Hodge–Tate weight 记法混淆。对(1)的普通位 $v$，
$\chi_{27,\ell}$ 的指数是1，而在 $\bar v$ 是0。
有限 $\eta_j$ 的指数为0。于是(6)给
$$
\operatorname{Tex}_{v}(V)=2,\qquad
\operatorname{Tex}_{\bar v}(V)=-1.
\tag{13}
$$
这也直接核回 R804/R811 的原 $(2,-1)$，有限扩域不改这些局部
指数。

## 3. 排除整个有限 1-motive 张量范畴

令 $F/K$ 是任意有限扩张，$\mathcal T_{1,F,\lambda_*}$ 为以下
表示的最小 Tannakian 子范畴：$F$ 上各 1-motive 的
$\lambda_*$-adic 实现。允许有限直和、张量、对偶、子对象、商
以及有限系数扩张。Artin 表示和 Tate 对象也在此范畴内。

**定理。** 对每个 $j=4,10,16$，
$$
\boxed{\mathcal E_j|_{G_F}\notin
\mathcal T_{1,F,\lambda_*}.}
\tag{14}
$$
即使仅要求在单一 $7993$ 实现处有这样的表示同构也不可能。

**证明。** 假设属于该范畴。构造一个有限维对象只涉及有限个
1-motive；取它们的直和 $M$，则 $\mathcal E_j$ 是
$V_{\lambda_*}M$ 的有限张量、对偶和子商构造。

Jossen [J, Theorem2(3)] 对有限生成数域给一个半阿贝尔簇
$P(M)$，其 Tate 实现就是 1-motive 的幺幂 Galois Lie 代数。
在代数 monodromy 记法下，结论是
$$
\operatorname{Lie}R_u(G_M)\simeq V_{\lambda_*}P(M)
\quad\text{作为 }G_F\text{ 模。}
\tag{15}
$$
说明(15)与原文的 Lie 记法一致：原文先写紧 ℓ-adic Galois
像的 Lie 代数 $\mathfrak l_M$ 及其 $W_{-1}$。
[J, Theorem1、§2]给其 $W_{-1}$ 等于 mixed Mumford–Tate
群的 $W_{-1}$；Brylinski 的绝对 Hodge 张量比较使有限扩域后
代数 Galois 群包含于该 Mumford–Tate 群。另一方面，纯分次的
Galois 群由阿贝尔簇、torus 和有限格构成，单位分支 reductive。
所以 Galois 群的幺幂根恰是其权核。更显式地，一方面
$\operatorname{Lie}R_u(G_M)\subset W_{-1}\mathfrak h_M\otimes\mathbf Q_{7993}$；
另一方面，$W_{-1}\mathfrak l_M$ 是该权核 Lie 代数的子空间，
而 Theorem1 使它等于右侧。两包含因此给等号。这里的代数群
包含由 [J, Proposition2.9、§2.10及Theorem2.1的证明] 中有限个
绝对 Hodge 张量的共同稳定子得出。这个步骤不假设阿贝尔簇的完整
Mumford–Tate 猜想，也不把一个任意紧群的 Lie 代数与其
Zariski 闭包无条件相认。

半阿贝尔簇的 Tate 模是 torus Tate 模与阿贝尔簇 Tate 模的
扩张。在 $\lambda_*$ 的每个局部位，其 Tate 指数只可能为
$0,1$；torus 项只有1。de Rham 表示的子商仍 de Rham，
指数多重集在短正合列中相加。因此(15)的任何 Galois 子商
只能有指数 $0,1$。

Tannakian 子范畴给代数群的商映射
$G_M\twoheadrightarrow G_j$。对特征零代数群，幺幂根在满射
下满射到商群的幺幂根：先模去 $R_u(G_M)$ 后，剩下 reductive
群的商仍 reductive。因此微分给
$$
V_{\lambda_*}P(M)
\twoheadrightarrow\operatorname{Lie}R_u(G_j)\simeq V.
\tag{16}
$$
(13)的指数2（另一普通位的 $-1$ 也可）与(16)矛盾。
由(9)，有限扩域不会使这个矛盾失去非平凡扩张前提。
$\square$

此处有两个容易混淆的边界。

1. **纯 $V$ 没有被排除。** 它由 $H^1(E_{27})$ 的三次张量、
   Tate 和有限 Artin 对象构成，完全在纯阿贝尔型范畴中。
   (14)排除的是带非零扩张类的 $\mathcal E_j$。
2. 对整个(10)同时 Tate twist，或同时张量同一个一维纯角色，
   不改变两个分次之比，因而不改变共轭模
   $\operatorname{Lie}R_u(G_j)=\operatorname{Hom}(k,V)$。
   这不会把(13)移到允许区间。若另行关闭于**任意新扩张**，
   就已经离开本文的张量子商范畴；Jossen 的定理没有把这种
   更大的混合动机范畴一并处理。

Hodge 型也显示同一位置：未作 AJ twist 的 $H^3(1)$ 最高部分
类型为 $(2,-1),(-1,2)$；AJ 真正使用的 $H^3(2)$ 类型为
$(1,-2),(-2,1)$，均为 level3。半阿贝尔 Lie 部分的 Hodge
型只来自 $(-1,0),(0,-1),(-1,-1)$。但上述证明以(8)、(13)
和 Jossen 为依据，**未假设**这个固定循环的 Betti AJ 非零，
也未从 Betti AJ 非零倒推 ℓ-adic 非零。

## 4. Frobenius 兼容性为何不能补这个混合输入

对任意好素位 $q\nmid\ell$，由(11)
$$
\det(1-T\rho_{\mathcal E_j}(\operatorname{Frob}_q))
=(1-T)\det(1-T\rho_V(\operatorname{Frob}_q)).
\tag{17}
$$
它完全不含 $c(g)$。原纯 CM 系统 $(V_{j,\lambda})_\lambda$
已有共同的 $E$ 有理 Frobenius 特征多项式。现在定义一个
**用于检验推理范围的表示族**：在 $\lambda_*$ 取真实(10)，
其它 $\lambda$ 全取 $V_{j,\lambda}\oplus E_\lambda$。
在包含真实扩张分歧的一个共同有限坏集外，该族满足通常的
Serre $E$ 兼容性；(17)在每处给同一多项式。
其幺幂根却仅在 $\lambda_*$ 非平凡。

因此，仅从共同 Frobenius 多项式、纯分次的 CM 性、半单化的
monodromy 独立性，不能推出(7)跨 $\lambda$ 非零。这个反例族
**不声称**来自同一个固定代数循环；它准确说明，若想对固定
循环使用兼容系统定理，所需的额外“几何混合扩张保真”假设
不能被半单化信息取代。

同理，若原 AJ 实现已具有 de Rham 或原 $f$ 条件，给其它位置
换成分裂扩张不会破坏那些位置的对应局部条件；局部分次的
Hodge–Tate 多重集也完全相同。只罗列这些分次条件仍不能
消除(17)的盲区。

## 5. 一次固定有限域约化只提供有限多个 ℓ 的挠检测

把全部固定数据扩到一个数域 $F$，取一个共同好约化位，残域
$\mathbf F_Q$。再固定有限残域扩张 $\mathbf F_{Q^r}$，使所用
循环和对应都定义于其上。这里 $Q,r$ 在随后变化 ℓ 之前固定。

令 $F_Q$ 为**几何** Frobenius。$V_{j,\lambda}$ 是
$H^3(2)$ 的纯权 $-1$ 因子，故其全部复 Frobenius 特征值的
绝对值是 $Q^{-1/2}$。因此 $F_Q^r-1$ 在每个
$V_{j,\lambda}$ 上可逆，且
$$
H^1(\mathbf F_{Q^r},V_{j,\lambda})
=V_{j,\lambda}/(F_Q^r-1)V_{j,\lambda}=0
\quad(\ell\ne\operatorname{char}\mathbf F_Q).
\tag{18}
$$
这是纯权计算，不假设 Tate 或 Beilinson 猜想。

对共同纯 CM 系统的整格 $T_{j,\lambda}$，置
$A_{j,\lambda}=V_{j,\lambda}/T_{j,\lambda}$。
共同 Frobenius 多项式给
$$
d_r=\det(F_Q^r-1\mid V_j)\in E^\times.
\tag{19}
$$
清去 $Q$ 与固定对应/整模型的有限分母，再取到 $\mathbf Q$
的范数，得到一个固定非零整数 $D_r$。当
$\ell\nmid QD_r$ 且不碰那些固定分母时，$F_Q^r-1$ 在整格
上可逆，故
$$
A_{j,\lambda}^{F_Q^r=1}=0.
\tag{20}
$$
任何 Galois 等变的有限域挠 AJ/cycle-class 检测，在一个定义于
$\mathbf F_{Q^r}$ 的固定循环上，必须落在(20)的 invariants。
所以它最多在固定有限集合内的 ℓ 非零。

Schoen 关于 $\overline{\mathbf F}_Q$ 上挠 AJ 像或满射性的
定理允许循环与定义域随挠阶改变；不能把它改成这一个固定
数域循环在无穷 ℓ 的 rational AJ 非零。(18)–(20)只排除
**固定的一次约化及固定定义域**作为该桥；不排除改变约化
素位、残域扩张或循环所得的其它方法。

## 6. 已核原始定理的量词

| 原始来源 | 实际对象和结论 | 对(7)的适用范围 |
|---|---|---|
| Jossen [J] Theorems1–2 | 有限生成域上的 1-motive；以半阿贝尔簇比较幺幂 Lie 部分 | 真正的混合定理，但(14)排除了本扩张所在范围 |
| Cadoret [C] Theorem1.2(2) | smooth proper 家族；固定 ℓ 后，非例外纤维的幺幂根与泛点相同 | 独立的是纤维点，不是固定数域扩张的 ℓ；取零维基不能产生新结论 |
| Cadoret–Hui–Tamagawa [CHT] Theorems1.1–1.2 | 代数闭基域上的 smooth proper 家族之几何 monodromy；大 ℓ 模 ℓ 半单与 maximality | 不处理这里 $G_K$ 的非平凡算术 AJ 扩张 |
| Chin [Ch] 主定理 | 有限域上曲线的纯、半单兼容 lisse 系统；共同 connected reductive 群 | 半单假设先去掉了(12) |
| D’Addezio [D] Theorem1.2.1 | 有限域上光滑簇的半单 coefficient objects，含 overconvergent $F$-isocrystals | 去掉部分纯性限制仍保半单；不是数域的混合扩张保真 |
| Schoen [S] | 代数闭有限域上的挠 cycle-class/AJ 像 | 与固定数域循环的 rational AJ 不同，固定约化另受(18)–(20)限制 |

这张表只记录逐篇核过的这些定理，不声称整个文献中“不存在”
任何更广的混合比较。下一实质输入仍须处理(10)这种 level3
混合 CM 扩张本身，或直接支付原 $\mathscr K_p(\nu_j)$ 的
无穷素数非零。本文没有把(14)当作课题停止的理由。

## 原始来源与已付输入

- [J] P. Jossen, *On the Mumford–Tate conjecture for 1-motives*,
  Inventiones Math. **195** (2014), 393–439；Theorems1–2，
  §§1.3–1.5、2、6。
  [作者预印本](https://arxiv.org/pdf/1107.5259)。
- [C] A. Cadoret, *On ℓ-independency in families of motivic ℓ-adic
  representations*, Manuscripta Math. **147** (2015), 381–398；
  Theorem1.2(2)。
  [作者全文](https://webusers.imj-prg.fr/~anna.cadoret/l-IndepMAMA.pdf)。
- [CHT] A. Cadoret, C.-Y. Hui, A. Tamagawa, *Geometric monodromy —
  semisimplicity and maximality*, Annals Math. **186** (2017),
  205–236；Theorems1.1–1.2。
  [原文](https://annals.math.princeton.edu/wp-content/uploads/annals-v186-n1-p05-p.pdf)。
- [Ch] C. Chin, *Independence of ℓ of monodromy groups*, JAMS
  **17** (2004), 723–747。
  [作者预印本](https://arxiv.org/abs/math/0206147)。
- [D] M. D’Addezio, *The monodromy groups of lisse sheaves and
  overconvergent F-isocrystals*, Selecta Math. **26** (2020), Article45；
  Theorem1.2.1。
  [原文](https://link.springer.com/article/10.1007/s00029-020-00569-3)。
- [S] C. Schoen, *On the computation of the cycle class map for
  nullhomologous cycles over the algebraic closure of a finite field*,
  Ann. Sci. ENS **28** (1995), 1–50。
  [原文](https://www.numdam.org/article/ASENS_1995_4_28_1_1_0.pdf)。
  另见其 *On the image of the ℓ-adic Abel–Jacobi map for a variety
  over the algebraic closure of a finite field*, JAMS **12** (1999),
  795–838。
- R804、R806(33)、R811、R817(1)–(7)、(23)–(24)、R991、R995、
  R997、R1002、R1006：固定原角色、7993 实测、严格对应及新54图
  的完整平方公式。

本篇没有新增数学程序运行，没有重跑7993，也没有启动第二个原几何作业。
