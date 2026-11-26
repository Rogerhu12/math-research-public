# R984 — 原三个规范 Heegner 收缩循环在几何 Griffiths 商中非零且独立

日期：2026-11-26。会话：Astra-rank2-Sha-0b097461-20261127。
**状态：已证明。**

本文保留 [R854](R854-original-canonical-cm-contraction-and-threefold-heegner-cycles.md)
的同一个 Kuga–Sato 三维、同一个先于 p 固定的 good pair、
同一个有限 isogeny orbit、全部 norm 权及三个有限角色。
由已付的唯一普通素数7993检测，证明原三份收缩循环在
**几何 Griffiths 群** 中仍非零且线性独立。
证明实际经过曲线对应、Picard Kummer、Betti–étale 比较和有限扩域限制；
不把 Hodge 型本身当成关于 Chow 类的注入定理。

## 1. 固定的三维、循环与已付检测

沿用 R814、R817、R854：
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad \delta^2=-3,
\qquad A_0:y^2=x^3+1,
$$
$$
W=W_2,\qquad \dim W=3,\qquad
X=W\times A_0^2,\qquad \dim X=5.
\tag{1}
$$
固定 $\psi=\psi_{\rm b}\alpha$、weight4 的 $g=\theta_\psi$、
三个有限角色 $\chi_j=\lambda_j/\psi$，其中 $j=4,10,16$。
取包含原全部循环和对应的有限数域 $F\supset K$，
及包含原有限角色值、Hecke 系数的系数数域 $\mathcal E$。

本文的循环是 R854(19) 中的原对象
$$
\mathcal H_j
 =\mathscr C_\delta(\Delta_j)
 =\mathscr E_j\sum_{a\in\mathcal O}
       b_{j,a}\frac{d_{\varphi_a}}{34}\,
       \epsilon_W i_{B_a,*}[\Gamma_{[34\delta]}]
 \in\operatorname{CH}^2(W_F)_{\rm hom}\otimes\mathcal E.
\tag{2}
$$
这里 $\mathcal O,b_{j,a},\mathscr E_j$ 全是原固定有限构造。
尤其不删去 $d_{\varphi_a}/34$，不更换 $\chi_j$，也不改换 level 向量。
R854 的实际对应满足
$$
\mathscr C_\delta(Z)
  =p_{W,*}(Z\cdot p_{A_0^2}^{*}D_\delta),\qquad
D_\delta=\Gamma_{[\delta]}-[A_0\times0]-3[0\times A_0],
$$
$$
\mathscr C_\delta\mathscr I_\delta=-6,\qquad
\mathscr I_\delta(Y)=Y\times D_\delta,
\qquad
\mathscr P_\delta\Delta_j
 =-\frac16\mathcal H_j\times D_\delta.
\tag{3}
$$

设 $e_g$ 为原 $g$ 的 cuspidal cohomological projector，
由原 Hecke/Scholl 代数对应实现；所需旧形式 level 向量仍在其像中。
这里只使用该实际对应在同调上的作用，不由一个同调投影任意选新的循环。
对 $\mathcal E$ 的任一复嵌入，该 weight4 cuspidal 部分的 Hodge 型是
$$
e_gH^3_{\rm B}(W)(\mathbf C):\qquad (3,0),(0,3).
\tag{4}
$$
允许原 level 的重数不会加入 $(2,1)$ 或 $(1,2)$ 型。
有限角色的 Artin 因子是 $(0,0)$ 型，因此也不改变(4)。

固定 R817 的 $p_*=7993$ 及其指定系数嵌入 $\iota_*:\mathcal E\hookrightarrow
\overline{\mathbf Q}_{7993}$，令 $E_*$ 包含其像。
原三条负二余值为 $2522,2828,3696$，均非零。
R854(24)–(27) 已给出
$$
\mathcal B_{j,p_*}
 =\operatorname{AJ}_{W,p_*}(\mathcal H_j)(\omega'_g)
 =-2\delta\,\mathcal A_{j,p_*}\ne0.
\tag{5}
$$
这是原实际普通局部 AJ 配对。因其来自全局 étale AJ 的限制及
Bloch–Kato 对数，(5)特别蕴含
$$
e_g\operatorname{AJ}^{\rm et}_{F,p_*}(\mathcal H_j)\ne0
\quad\hbox{于}\quad
H^1\bigl(F,e_gH^3_{\rm et}(W_{\overline F},E_*)(2)\bigr).
\tag{6}
$$
没有重新计算7993，亦没有由这三个余数的大小推出线性独立。

## 2. 曲线对应的型障碍：先证明实现上的零映射

设 $F'/F$ 为任意有限扩域，$C/F'$ 为光滑射影曲线，
$\Gamma\in\operatorname{CH}^2(C\times W)\otimes\mathcal E$。
由于 $\dim C=1$，此 codimension2 对应在 cycle 群上给出
$$
\Gamma_*:\operatorname{CH}^1(C)
 \longrightarrow\operatorname{CH}^2(W),
\qquad
z\longmapsto p_{W,*}(p_C^*z\cdot\Gamma).
\tag{7}
$$
其 Betti 同调作用准确为
$$
e_g\Gamma_{*,\rm B}:H^1_{\rm B}(C)
 \longrightarrow e_gH^3_{\rm B}(W)(1).
\tag{8}
$$
两边均为 weight1。左边只有 $(1,0),(0,1)$；
由(4)，右边只有 $(2,-1),(-1,2)$。
代数对应及 Tate normalization 使(8)为 $(0,0)$ 型 Hodge morphism。
把系数域经每个复嵌入展开后，左右没有共同 Hodge 型，故
$$
\boxed{e_g\Gamma_{*,\rm B}=0.}
\tag{9}
$$

对任意有理素数 $\ell$ 及任意系数嵌入
$\iota_\ell:\mathcal E\hookrightarrow E_\ell\subset\overline{\mathbf Q}_\ell$，
选择 $F'\hookrightarrow\mathbf C$ 后的 Betti–étale comparison
与**同一个实际代数对应**的 pullback、cycle class、cup product 和 pushforward
交换。因此(9)推出
$$
e_g\Gamma_{*,\ell}:H^1_{\rm et}(C_{\overline {F'}},E_\ell)
 \longrightarrow e_gH^3_{\rm et}(W_{\overline {F'}},E_\ell)(1)
 \quad\hbox{为零}.
\tag{10}
$$
再作一次 Tate twist，得到 AJ 所需的准确映射
$$
\boxed{
e_g\Gamma_{*,\ell}:H^1_{\rm et}(C_{\overline {F'}},E_\ell)(1)
 \longrightarrow e_gH^3_{\rm et}(W_{\overline {F'}},E_\ell)(2),
 \qquad e_g\Gamma_{*,\ell}=0.
}
\tag{11}
$$
(8)的 $H^3(1)$ 是用来比较 weight1 Hodge 型的对象；
(11)的 $H^3(2)$ 才是 codimension2 étale AJ 的系数表示。
这两个 Tate 移位不能互换。

## 3. Picard Kummer 与 codimension2 AJ 的完整交换

设 $J_C=\operatorname{Pic}^0(C)$。曲线的 Abel–Jacobi 映射是 Kummer 映射
$$
\kappa_{C,\ell}:J_C(F')\otimes E_\ell
 \longrightarrow H^1(F',V_\ell J_C),
\qquad
V_\ell J_C\simeq H^1_{\rm et}(C_{\overline {F'}},E_\ell)(1).
\tag{12}
$$
这里若 $C$ 原来没有有理点，可以先作有限扩域；
在下面 algebraic equivalence 的应用中已同时使所用点有理。
对 $z\in\operatorname{Pic}^0(C)(F')$，
$\Gamma_*z$ 同调平凡。
cycle class 与 Hochschild–Serre edge map 的 functoriality 给交换图
$$
\begin{array}{ccc}
J_C(F')\otimes E_\ell
 &\xrightarrow{\ \Gamma_*\ }&
\operatorname{CH}^2(W_{F'})_{\rm hom}\otimes E_\ell\\[2mm]
\big\downarrow\kappa_{C,\ell}&&
\big\downarrow e_g\operatorname{AJ}^{\rm et}_{F',\ell}\\[2mm]
H^1(F',H^1_{\rm et}(C)(1))
&\xrightarrow{\ H^1(e_g\Gamma_{*,\ell})\ }&
H^1(F',e_gH^3_{\rm et}(W)(2)).
\end{array}
\tag{13}
$$
图中下行省略的 cohomology 系数一律是 $E_\ell$。
由(11)，下方箭头为零，于是
$$
\boxed{
e_g\operatorname{AJ}^{\rm et}_{F',\ell}(\Gamma_*z)=0.
}
\tag{14}
$$
此处只需 Kummer/AJ 的 functoriality，不需要 Kummer 的注入性，
也不需要关于一般 codimension2 AJ 注入的任何猜想。

## 4. 从几何代数等价到有限扩域上的真实对应

记
$$
\operatorname{Griff}^2(W_{\overline F})_{\mathcal E}
 =\frac{\operatorname{CH}^2(W_{\overline F})_{\rm hom}
                \otimes\mathcal E}
        {\operatorname{CH}^2(W_{\overline F})_{\rm alg}
                \otimes\mathcal E}.
\tag{15}
$$
分母表示 algebraically equivalent to zero 的子群；
它比 rationally equivalent to zero 的要求弱，
所以非零 Chow 类不能未经论证直接放入这个商后仍称非零。

若一个 $Z\in\operatorname{CH}^2(W_F)_{\rm hom}\otimes\mathcal E$
在(15)中为零，则由代数等价的曲线族定义，在 $\overline F$ 上有一个
**有限和**
$$
Z_{\overline F}
 =\sum_{u=1}^{s}a_u\Gamma_{u,*}([P_u]-[Q_u]),
\quad a_u\in\mathcal E,
\quad \Gamma_u\in\operatorname{CH}^2(C_u\times W),
\tag{16}
$$
其中各 $C_u$ 光滑射影，$P_u,Q_u$ 为其点。
从最初的光滑连通曲线族取光滑射影紧化，并把 total cycle 取闭包，
就在两个原有良好纤维处给出(16)；
必要时分解族及取有限和，覆盖代数等价生成关系。
cycle 群中的有理等价证据也只涉及有限多个子簇和有理函数。
因此可取一个有限扩域 $F'/F$，使全部 $C_u,\Gamma_u,P_u,Q_u$、
系数和等式同时在 $F'$ 上定义，且 $P_u,Q_u\in C_u(F')$。

把(14)逐项应用于(16)，得到每个 $\ell$、每个系数嵌入下
$$
e_g\operatorname{AJ}^{\rm et}_{F',\ell}(Z_{F'})=0.
\tag{17}
$$
AJ 与 base change 相容，故(17)就是
$$
\operatorname{res}_{F'/F}
 \bigl(e_g\operatorname{AJ}^{\rm et}_{F,\ell}(Z)\bigr)=0.
\tag{18}
$$
对这些有理 $E_\ell$ 系数的 Galois cohomology，
$$
\operatorname{cor}_{F'/F}\operatorname{res}_{F'/F}
 =[F':F].
\tag{19}
$$
有限非零整数 $[F':F]$ 在 $E_\ell$ 中可逆，
包括 $\ell\mid[F':F]$ 的情形。
所以 restriction 在这里注入，(18)给出
$$
\boxed{
Z\text{ 几何代数平凡}\quad\Longrightarrow\quad
e_g\operatorname{AJ}^{\rm et}_{F,\ell}(Z)=0
\quad\hbox{对每个 }\ell.
}
\tag{20}
$$
这完整地处理了“只在某个有限扩域上代数等价”的可能，
没有把 $F$ 上的关系与 $\overline F$ 上的关系混为一谈。

## 5. 应用于原三份循环及实际有限角色

若原 $\mathcal H_j$ 在(15)中为零，(20)取 $\ell=7993$
就与(6)矛盾。因此
$$
\boxed{
[\mathcal H_j]\ne0
\quad\hbox{于}\quad
\operatorname{Griff}^2(W_{\overline F})_{\mathcal E},
\qquad j=4,10,16.
}
\tag{21}
$$

R854 的原 finite-character 作用在共同有限轨道上，且
$$
\chi_{10}=\chi_4\epsilon,\qquad
\chi_{16}=\chi_4\epsilon^2,
\qquad \epsilon^3=1,\quad\epsilon\ne1.
\tag{22}
$$
取原共同有限 Galois 群 $G$ 上的相应正交幂等元 $e_j$，
约定其作用与 R854 的原 cycle-factor action 完全相同。
于是
$$
e_j\mathcal H_k=\delta_{jk}\mathcal H_k.
\tag{23}
$$
每个 Galois translate 把一个代数等价族送到其共轭族，
故 $\operatorname{CH}^2_{\rm alg}$ 在这个作用下稳定；
$e_j$ 因而确实诱导(15)上的线性算子。
这里固定系数域，**不让系数嵌入同时随 Galois 共轭**。

若有 $a_4,a_{10},a_{16}\in\mathcal E$ 满足
$$
a_4[\mathcal H_4]+a_{10}[\mathcal H_{10}]
       +a_{16}[\mathcal H_{16}]=0,
\tag{24}
$$
施 $e_j$ 得 $a_j[\mathcal H_j]=0$。
由(21)及 $\mathcal E$ 是域，$a_j=0$。
故
$$
\boxed{
\dim_{\mathcal E}
 \operatorname{span}\{[\mathcal H_4],[\mathcal H_{10}],
                         [\mathcal H_{16}]\}=3.
}
\tag{25}
$$

同样，(3)的真实代数对应保持 algebraic equivalence。
若 $\sum_j a_j[\mathscr P_\delta\Delta_j]$ 在
$\operatorname{Griff}^3(X_{\overline F})_{\mathcal E}$ 中为零，
施 $\mathscr C_\delta$ 即给(24)。所以三个原 mixed 分量也独立：
$$
\dim_{\mathcal E}
 \operatorname{span}\{[\mathscr P_\delta\Delta_j]:j=4,10,16\}
 =3
\quad\hbox{于 }\operatorname{Griff}^3(X_{\overline F})_{\mathcal E}.
\tag{26}
$$
这里是指定的 $\mathscr P_\delta$ 分量，未把 $\Delta_j$ 的其余 CM 分量抹掉。

## 6. 这个位置结论对后续来源的实际限制

(21)–(26)给出原固定循环的几何位置。
例如不存在有限扩域 $F'/F$、曲线 $C_u/F'$、
$\Gamma_u\in\operatorname{CH}^2(C_u\times W)_{\mathcal E}$
及 $z_u\in\operatorname{Pic}^0(C_u)(F')_{\mathcal E}$，
使原某个非零组合满足
$$
\sum_j a_j\mathcal H_j=\sum_u\Gamma_{u,*}z_u
\quad\hbox{于 }\operatorname{CH}^2(W_{F'})_{\mathcal E}.
\tag{27}
$$
右边几何代数平凡，故(27)由(25)排除。
特别是用这样的实际代数对应，把这些规范循环等同于普通 CM 椭圆曲线
上 Mordell–Weil 点的 Kummer 来源，不能成立。

本篇没有断言整个 $e_g\operatorname{CH}^2_{\rm alg}$ 为零；
证明的是其指定 étale AJ 分量为零。
也没有由纯 CM motive 的分解或 Betti–étale comparison 推出
mixed extension 的 $\ell$-adic realization 忠实。
(20)是“几何代数平凡蕴含 AJ 零”的单向结论；
它不把 $[\mathcal H_j]\ne0$ 反推为任意其它 $\ell$ 的 AJ 非零。

仍须另付的原主门是：实际原端点与这些规范类的比较、
无穷多个目标普通 p 的非零、及 rank2 usual full Selmer 的完整桥。
R859 的 $E_0^3$ 原端点 shadow 不能直接用于 $W$ 上的(2)，
除非给出携带这个具体 Chow 类的实际对应。

## 7. 依据与引用范围

1. [R814](R814-common-fixed-good-pair-and-three-original-aj-squares.md)：
   先于 p 固定的同一个 $g,\psi,\chi_j$ 及有限 CM orbit。
2. [R817](R817-fixed-prime-original-negative-two-and-nonzero-fixed-cycles.md)：
   唯一固定 p=7993 的三条原负二非零检测及指定系数嵌入。
3. [R854](R854-original-canonical-cm-contraction-and-threefold-heegner-cycles.md)，
   §1–§6：真正 $W_2$、codimension2 收缩循环、$d_\varphi/34$、
   $-6$ 分裂和 $-2\delta$ AJ 比较；本文逐项沿用。
4. M. Bertolini, H. Darmon, K. Prasanna,
   *Generalized Heegner cycles and p-adic Rankin L-series*,
   Duke Math. J. **162** (2013), 1033–1148，
   [发表全文](https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP1.pdf)，
   §2.1–§2.4、§3.1–§3.4：Scholl 部分、实际 graph cycles 及 étale/de Rham AJ。
5. J. Nekovář, *p-adic Abel–Jacobi maps and p-adic heights*,
   CRM Proc. Lecture Notes **24** (2000), 367–379，
   [作者存档](https://webusers.imj-prg.fr/~jan.nekovar/pu/banff.pdf)，§1：
   cycle class、Hochschild–Serre 构造及 divisor 情形的 Picard Kummer。
   (13)由这些 functorial cycle-class 操作直接给出。

本文无新数值计算、无新素数扫描、无可重算输出文件。
