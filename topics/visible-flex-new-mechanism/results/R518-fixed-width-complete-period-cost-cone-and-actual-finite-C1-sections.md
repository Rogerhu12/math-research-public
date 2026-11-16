# R518：固定物理宽度的完整 period 成本满锥与实际有限 C1 截面

日期：2026-11-16。**完整纸面证明。没有执行科学程序、符号化简、profile 求积、旧秩或新的数值搜索。**

本稿保持原母库、全部真实幅度和后缀、共同右锚及 canonical 成本。改变的是控制目标的选择：只要求最终实际使用的同一物理宽度上的全部 period 累计量为零，并保其有限平移闭包；不额外要求这些累计量在所有正伸缩后的输入上也为零。

这一区分不改变原 period 方程。R463 的 $J_{\rm aff}$ 是给原控制证明增加的仿射闭包；本稿的 $J_{\rm tr}$ 仍包含最终原方程所需的每一行。R513 对完整正 $A_f$ cap 五门的分离，不禁止下面的 $J_{\rm tr}$ 构造；本稿也不声称那些五门变成了零。

结论分为三层：

1. 对 R459 从起点选出的共同物理宽度库，$J_{\rm tr}$ 的完整真实成本闭锥是整个像。
2. 同一 $J_{\rm tr}$ 下，有限真实同端口、$M=\mathbf T=0$ 参数族的导数张满该像。因此存在一个保持全部真实基准的实际 $C^1$ 开球。
3. 满闭锥和这个开球，通过有限实际块的非负配平与整数复制，给任意紧目标集的同一个有限实际 $C^1$ 截面。最后可用一次共同正 $\omega$ 平移和原受控桥，将整个有限构造放回指定合法 profile 窗口及原 scalar germ。

所有 signed 差与谱分解只用于证明有限维线性关系；真正构造仅使用正长度路径、正整数复制、原真实桥及其真倒行。

主要来源：
[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、
[R101](R101-finite-replication-and-signed-fourth-character-costs.md)、
[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、
[R120](R120-G-lineality-of-the-closed-fourth-cost-cone.md)、
[R127](R127-positive-affine-character-of-the-fourth-cost-cone.md)、
[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、
[R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)、
[R206](R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md)、
[R212](R212-C1-sections-for-complete-real-pure-cost-control.md)、
[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)、
[R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md)、
[R459](R459-one-common-signed-witness-for-all-internal-fluxes-of-the-equal-width-library.md)、
[R460](R460-automatic-simple-critical-point-residues-and-complete-smooth-period-gluing.md)、
[R463](R463-real-partial-quotients-translation-defect-and-finite-affine-control-interface.md)、
[R465](R465-complete-zero-weight-affine-head-and-two-mirror-self-membership-gates.md)、
[R466](R466-complete-mirror-anchor-identity-and-enhanced-minus6-minus4-cone-reduction.md)、
[R467](R467-conditional-actual-highest-gauge-control-and-one-complete-thirteen-row-normalization.md)、
[R468](R468-real-height-pulse-fills-affine-residual-and-completes-actual-enhanced-cost-control.md)。

## 1. 固定真实成本与最终所需的映射

固定原 scalar 常值 germ $g$、frame $I\to I$、共同右锚、canonical 规则以及零传入历史，记
$$
\mathcal S_g=\{V_B:B\text{ 为有限真实同端口路径},
\ M_B=\mathbf T_B=0,\ F_B:I\to I\},
\qquad U=\operatorname{span}_{\mathbb R}\mathcal S_g .
\tag{1}
$$
$U$ 是 R105 的有限维完整真实函数空间，$\mathcal R\subset U$ 是完整响应空间。这里先按 R120 使用 universal 原式延拓；不会把其中某条路径在移动极点另一侧直接解释为合法曲面。第8节把实际使用的有限族统一放回给定合法窗口。

两个各自 $M=0$ 的块，第四成本按 R83/R101 完整相加。若同端口块另有 $\mathbf T=0$，则其任意正整数次复制仍在(1)的同一类中。真倒行的第四成本同号；从未用倒行制造负成本。

固定 R459 的同宽新库，包括 R455 的唯一共同简单 $A_f$ 镜对、R450 的 $8\times12$ 完整复制以及从起点纳入的全部原幅度和角色。母形在共同内区的同三矩路径上变化，全部外 cap 与根 germ 相同。使用 R433 的
$$
J_0=J^+=(E,\mathcal A,\mathcal O_{\rm all}),
\qquad E=(\pi,\mathcal Q).
\tag{2}
$$
各部分的准确范围是：

- $\pi$ 是 whole pure 成本，$\mathcal Q$ 是 whole self 左二次尾；
- $\mathcal A$ 是当前实际母 self 与所需右侧矩基的 ordered 查询，以及它们原已付的有限共同正仿射闭包；不是 universal self natural 函数；
- $\mathcal O_{\rm all}$ 是 universal ordered $3+2$ natural 函数。它在有限维 $U$ 上仍是一个有限秩线性映射，可用固定有限真实坐标承载全部函数，而非仅令几个采样值为零。

令 $F$ 为最终所有实际微包角色、每个真实 $A_f$ 镜点的两条原累计通量 $H_d,H_e$。必须先沿 R463(2)在整个 $U$ 上定义同一个线性延拓。例如原相位查询为
$$
D_V^\circ=V(f^2,g),\qquad
E_V^\circ=V\!\left(f^2,\frac{f+g}{\sqrt2}\right)
-\frac12V(f^2,g).
\tag{3}
$$
在 $\pi V=0$ 时它们回到原两个 period forcing。对每个原左锚与实际根作原 $\int f'(\cdot)''$，并保持 R463/R459 的幅度归一，就定义了 $F$；对不在 $\ker\pi$ 中的 prototype 也仍使用(3)，不偷用 pure-zero 极化。

以 $N$ 表示原真实平移生成元，$D$ 表示真实正伸缩生成元。R190/R203 给真权支撑 $[-9,3]$，故 $N^{13}=0$。定义
$$
J=J_{\rm tr}
=\bigl(J_0,\ (FN^j)_{0\le j\le12}\bigr),
\qquad P=J(U),\qquad K=\ker J.
\tag{4}
$$
因此 $K$ 对 $N$ 稳定，且 $J$ 包含实际原 $F$ 本身。这里只加入有限平移闭包，物理宽度始终是同一个 $w_0$。

$F=0$ 包括所有真实 suffix 的两通道累计条件，因而也包括每个实际角色的
$R_iH_e+T_iH_d=0$。本稿不将它改称整个形式39坐标 current 恒零；后者比原 period 所需条件更强。R459 的核见证恰好满足形式 current 零，可用于证明，但最终控制目标没有免费增加这一要求。

以
$$
J_a=J_{\rm aff}
=\bigl(J_0,\ FN^j\Pi_\sigma\bigr)_{\sigma,j}
\tag{5}
$$
记 R463 的最小仿射行闭包。它包含(4)的全部行，因为
$FN^j=\sum_\sigma FN^j\Pi_\sigma$。所以
$$
\boxed{\ker J_a\subseteq K.}
\tag{6}
$$
(6)仅是同一个 $U$ 上两个明确线性映射的核包含，不依赖 $N\lambda=0$。本稿不要求 $J_a$ 的实际目标为零。

## 2. 同宽 signed 核见证保留整个平移闭包

R459(35)—(38)构造了一个完整原成本
$$
V_\#=H_*+J_4-R_C-W\in U,
\qquad
J_0(V_\#)=0,\qquad \lambda_+(V_\#)=1.
\tag{7}
$$
$R_C$ 是完整同权零 current 修正，$W$ 是同一个可能混权的原响应。该稿不是仅匹配有限采样：其两个完整 self partial 平移多项式同时为零，整个形式 current 也为零，故任意真实三矩 suffix、全部角色和允许中心的 $H_d,H_e$ 都为零。

R459(8)—(9)的真实共同平移同时输运输入、根位置和三矩。因 current 对任意矩均为零，且 self 多项式对全部中心为零，
$$
F(e^{cN}V_\#)=0
$$
在一个真实公共平移小区间成立。有限多项式身份遂给所有系数
$FN^jV_\#=0$。$J_0$ 原已仿射稳定，故
$$
\boxed{JV_\#=0,\qquad\lambda_+(V_\#)=1.}
\tag{8}
$$
此处只用同一个物理宽度。没有将 $W$ 投到权零，也没有要求
$F(P_{H,0}V_\#)=0$ 对 $H\ne1$ 成立；R513 的障碍恰可留在那些额外行上。

## 3. 完整真实锥、桥及双极端引理

记 universal 成本闭锥
$$
C=\overline{\operatorname{cone}(\mathcal S_g)}\subset U,
\qquad
C_J=\overline{\operatorname{cone}(J\mathcal S_g)}\subset P.
\tag{9}
$$
R120/R127 已在同一 complete canonical 空间证明 $C$ 与端口无关，且在全部真实正仿射作用下不变。这一性质保留完整桥成本。

具体说，对任意 $B\in\mathcal S_g$ 和固定 $H>0$，R89 变换后的 $B^H$ 位于新 germ $g_H$。取 R70 的同锚、$M=0$、frame $I\to I$ 桥 $A_H:g\to g_H$，则
$$
A_H(B^H)^nA_H^R
\quad\text{满足}\quad
M=\mathbf T=0,
$$
$$
V_{A_H(B^H)^nA_H^R}
=2V_{A_H}+nP_{H,0}V_B .
\tag{10}
$$
$2V_{A_H}$ 是实际 $A_HA_H^R$ 的完整成本；不能删。若 $\lambda\ge0$ 于 $\mathcal S_g$，由(10)除以正整数 $n$ 并令 $n\to\infty$，才得到
$\lambda(P_{H,0}V_B)\ge0$。平移同理。所用正性始终针对(1)的全部真实成本，而不是一个人为限制为固定 $H$ 的控制子库。

因 $K$ 对 $N$ 稳定，真实平移在 $P=U/K$ 上良定义，$C_J$ 对它不变。假设 $C_J\ne P$。有限维闭锥分离给非零
$\ell\in P^*$，令 $\lambda=\ell J$。于是
$$
\lambda\ne0,\quad \lambda(C)\ge0,\quad \lambda K=0.
\tag{11}
$$
原响应 lineality，或 R101(8)—(11)的完整两号复制，给
$\lambda\mathcal R=0$。

沿 R127 的两向平移步骤，令 $j$ 是 $\lambda N^j\ne0$ 的最大整数。因为 $K$ 对 $N$ 稳定，所有 $\lambda e^{cN}$ 仍杀 $K$；它们由(10)的平移版仍在 $C^*$。以 $|c|^{-j}$ 归一，$c\to\pm\infty$ 两极限分别给
$\lambda N^j/j!$ 与 $(-1)^j\lambda N^j/j!$。$C^*$ 尖，因为
$\operatorname{span}\mathcal S_g=U$，故 $j$ 为偶数。以
$\nu=\lambda N^j$ 替换，得到
$$
\nu\ne0,\quad \nu(C)\ge0,\quad
\nu N=0,\quad \nu\mathcal R=0,\quad \nu K=0.
\tag{12}
$$

现在才使用(6)：$\nu$ 也杀 $\ker J_a$。写其有限真权分解
$$
\nu=\sum_{\sigma=-9}^{3}\nu_\sigma,\qquad
m=\max\{\sigma:\nu_\sigma\ne0\},\quad
l=\min\{\sigma:\nu_\sigma\ne0\}.
$$
由(10)，$\nu P_{H,0}$ 对全部真实成本非负。$\ker J_a$ 对正伸缩稳定，因此这些泛函全杀 $\ker J_a$。有限维极限给
$$
H^{-m}\nu P_{H,0}\longrightarrow\nu_m\quad(H\to\infty),
\qquad
H^{-l}\nu P_{H,0}\longrightarrow\nu_l\quad(H\downarrow0).
\tag{13}
$$
两者非零、非负、杀 $\mathcal R$ 及 $\ker J_a$。又因 $N$ 降一权，$\nu N=0$ 逐权迫
$\nu_\sigma N=0$。所以(13)是同一个 $J_a$ 中的两个单权正仿射字符。

**这里只保证极端分量杀 $\ker J_a$，不宣称它们仍杀 $K$。** 下一步会先证明原 $\nu$ 本身只有权零，然后才重新使用原来一直保持的 $\nu K=0$。

R465/R466 在此同一母库中，独立于 $\mathfrak h,\mathfrak y$ 是否成比例，已经排除了全部非零权的这类字符：

| 真权 | 已付完整理由 |
|---|---|
| 奇权 | R145 的真实曲率反号及同锚作用 |
| $-8$ | R465 的完整增强响应等像 |
| $-6,-4$ | R466(1)(2)、§9，送回原 $J_0$ 后排除 |
| $-2$ | R188 对整个 $U$ 的正字符排除 |
| $2$ | R190 的 $U_2=\mathcal R_2$ |

故(13)的最大、最小非零权都必须为零，即 $m=l=0$。于是原 $\nu$ 自身是权零正字符。R196 给
$$
\nu=a\lambda_+,\qquad a>0.
$$
但(8)(12)给 $0=\nu(V_\#)=a$，矛盾。证明了
$$
\boxed{C_J=P.}
\tag{14}
$$

这一步修补的是 R463 §7 留下的混权问题：不能只取一个极端后把它当作仍下降到固定宽度；但两个极端分别在更大的稳定映射中排除全部非零权，足以强迫原混权泛函本身纯零权。

## 4. 所有真实参数导数的 span

满闭锥本身还不是实际实现。以下直接在完整 $P$ 上找一个真正开球，不先借 $J_a$ 的有条件截面。

令 $\mathscr T\subseteq P$ 是下列所有向量的实 span：
$$
\frac{d}{dt}J(V_{B(t)})\bigg|_{t=t_0},
\tag{15}
$$
其中 $B(t)$ 是有限真实 $C^1$ 族，$t_0$ 为参数开区间内部点，所有 $t$ 保同一 $g$、frame $I\to I$、$M=\mathbf T=0$、同一 canonical 规则及右锚。原长度变化按 R212 的固定参数区间记录并保真实 $ds$ 因子。

### 4.1 原响应属于导数 span

对任一原生成响应 $K_*= \mathcal B_E(\tau)$，R101 取一个真实第三 prototype $L$，其完整成本为 $v$，并给同端口实际族
$$
V_{Z(t,n)}=E_*(t)+n(2v+tK_*),
\qquad M_{Z(t,n)}=\mathbf T_{Z(t,n)}=0.
\tag{16}
$$
$E_*$、$v$ 都完整保留。R70 的同一小矩阵族经固定整数复制，给参数开区间中的 $C^1$ 族；R212 §2 保证完整恢复随参数 $C^1$。

对两个实际正整数 $n,n+1$，在同一个 $t_0$ 求导后相减：
$$
\partial_tJ(V_{Z(t,n+1)})-
\partial_tJ(V_{Z(t,n)})
=J K_* .
\tag{17}
$$
每个被相减的向量都属于(15)，所以
$$
J\mathcal R\subseteq\mathscr T.
\tag{18}
$$
(17)只在导数 span 中取差；没有把 $Z(t,n+1)Z(t,n)^{-1}$ 当成路径。

### 4.2 真正伸缩和平移导数也属于同一个 span

对任意 $B\in\mathcal S_g$，以一个固定小开区间上的原光滑桥 $A(t)$，连接 $g$ 与真实 $H=e^t$ 变换后的端口。对每个正整数 $n$，
$$
W_n(t)=A(t)(B^{e^t})^nA(t)^R
$$
是(15)所允许的真实族，且
$$
V_{W_n(t)}=2V_{A(t)}+nP_{e^t,0}V_B.
\tag{19}
$$
在 $t=0$ 对相邻 $n$ 的导数作差，准确得到 $J(DV_B)$。对真平移桥同理得到 $J(NV_B)$。原有限桥基准及其导数在这两个差式中消去，但每条实际族的值仍包含它们。

由 $U=\operatorname{span}\mathcal S_g$，
$$
\boxed{J(\mathcal R+DU+NU)\subseteq\mathscr T.}
\tag{20}
$$
这里不要求 $D$ 在 $P$ 上良定义；$JDU$ 是先对完整 $U$ 施加 $D$ 再应用 $J$ 的像，不能写成一个未经证明的 $DP$。

## 5. 原高度脉冲排掉最后的导数 annihilator

若 $\mathscr T\ne P$，取非零 $\ell\in P^*$ 杀 $\mathscr T$，置
$\lambda=\ell J$。由(20)，
$$
\lambda\mathcal R=0,\qquad \lambda D=0,\qquad\lambda N=0.
\tag{21}
$$
$\lambda D=0$ 使它只含真权零；R196 的完整二维头分类因而给
$$
\lambda=\lambda_{x,y}.
\tag{22}
$$
此处没有假定 $\lambda$ 非负；R196 的二维头首先是全部真实线性字符，正性只在另外一步才分类。

若 $y\ne0$，只调用 R468 §§3—5 中的**局部真实几何族**，不调用该稿需要
$\mathfrak h\in\operatorname{span}\{\mathfrak y\}$ 的整份截面主定理。该局部族与任何母的五门关系无关：

- 从同一 $g$、frame $I\to I$、$M=0$ 的实际平端路径 $B$ 出发；
- 在一个常值 collar 内置
  $\log h=\log h_0+\varepsilon a\chi((s-s_0)/\varepsilon)$，
  $k=k_0,\omega=\omega_0$，$a$ 在 $1$ 附近；
- 原八矩变化 $\Delta M=O_{C^1(a)}(\varepsilon)$，由独立同端口前缀
  $A(-\Delta M)$ 精确支付；
- 先形成整块 $W=A(-\Delta M)B_{\varepsilon,a}$，其 $M=0$，再接同一整块真倒行，得
  $\mathscr D_{\varepsilon,a}=WW^R$，$M=\mathbf T=0$。

一般 $A(-\Delta M)$ 和 $B_{\varepsilon,a}$ 各自矩阵非零，所以没有
$V_W=V_A+V_B$ 这一断言。R468 使用的是整块 $M=0$ 后才合法的原标量 action；该 action 的局部积分可以按段相加。

完整公式给
$$
\lambda_{x,y}(V_{\mathscr D_{\varepsilon,a}})
=C_*+\frac{2ya^2}{\varepsilon}\int(\chi'')^2
+O_{C^1(a)}(\varepsilon),
\tag{23}
$$
全部前缀基准在 $C_*$ 和余项中。取一个充分小但有限的 $\varepsilon>0$ 并冻结，则
$$
\partial_a\lambda_{x,y}(V_{\mathscr D_{\varepsilon,a}})\big|_{a=1}
=\frac{4y}{\varepsilon}\int(\chi'')^2+O(\varepsilon)\ne0.
\tag{24}
$$
这是(15)中的一个真实导数，与 $\ell\mathscr T=0$ 矛盾。

故 $y=0$。按 R196 的规范，$\lambda_{x,0}=-x\lambda_+$。即使不假定符号，(8)和 $\lambda=\ell J$ 也给
$$
0=\lambda(V_\#)=-x,
$$
所以 $\lambda=0$，再次矛盾。证明
$$
\boxed{\mathscr T=P.}
\tag{25}
$$

这一证明保持同一最终母及全部查询。高度脉冲只是改变真实几何控制块，不重新选择输入母、第三规范或 cap；(23)是原 universal action 对当前这些查询 pullback 泛函的准确作用。

## 6. 从导数 span 取得一个实际 C1 开球

令 $m=\dim P$。由(25)，可以从实际族(15)的导数中取 $m$ 个独立向量；每个族只需保一个真实标量参数。将这有限条路径依次拼接：
$$
\mathscr B(t_1,\ldots,t_m)=B_1(t_1)\cdots B_m(t_m).
$$
每一块自身 $M=\mathbf T=0$，同 germ、同 frame 端口。因此原完整成本准确相加：
$$
J(V_{\mathscr B(t)})=\sum_{i=1}^{m}J(V_{B_i(t_i)}).
\tag{26}
$$
其在基点的导数矩阵可逆。所有原恢复和可变长度依 R212 为 $C^1$。真实有限维逆函数定理给一个 $\epsilon>0$、$b\in P$ 和同一有限真实词族 $\mathscr G(z)$，使
$$
J(V_{\mathscr G(z)})=b+z,\qquad \|z\|<\epsilon,
\quad
M_{\mathscr G(z)}=\mathbf T_{\mathscr G(z)}=0.
\tag{27}
$$
在一个稍小闭球上，参数图册、全部构件、真实 lengths、scalar jets 及 frames 构成固定紧族。

$b$ 是所有构件的完整基准和，不是零。也没有把某个导数向量自己当成一个可直接行走的 signed 成本。(27)是由实际参数族的原式映射取得的真实开球。

## 7. 满闭锥和一个开球给精确有限实际截面

先说明从闭锥到有限正锥的准确一步。有限维凸锥
$\operatorname{cone}(J\mathcal S_g)$ 的闭包若为 $P$，则该锥本身已为 $P$。一种直接证明是：在一组基的正负向量附近，从该锥中各选一个足够近的向量，使其有限凸包仍含零为内点；把每个所选向量的有限非负实际表示全部展开，所得有限实际向量的正锥就是 $P$。

故由(14)，可选有限实际块 $S_1,\ldots,S_q\in\mathcal S_g$，记
$s_i=J(V_{S_i})$，并取有限实数 $\alpha_i\ge0$，使
$$
\sum_{i=1}^{q}\alpha_i s_i=-b.
\tag{28}
$$
实数 $\alpha_i$ 只用于下面取整数；不对应实数次路径复制。

给定任意紧目标集 $\mathcal K\subset P$，令
$$
n_i(N)=\lfloor N\alpha_i\rfloor,\qquad
e_N=Nb+\sum_i n_i(N)s_i
=-\sum_i\{N\alpha_i\}s_i.
\tag{29}
$$
因此
$$
\|e_N\|\le B_0:=\sum_i\|s_i\|,
\tag{30}
$$
与 $N$ 无关。取一个固定有限正整数 $N$，使
$$
\frac{\sup_{x\in\mathcal K}\|x\|+B_0}{N}<\epsilon/2 .
$$
在 $\mathcal K$ 的一个有界开邻域定义
$$
z_N(x)=\frac{x-e_N}{N},\qquad
\mathscr D_N(x)=\mathscr G(z_N(x))^N
S_1^{n_1(N)}\cdots S_q^{n_q(N)} .
\tag{31}
$$
零次项仅省略；所有真正出现的复制次数均为正整数。由(27)—(29)及全部块的真实 $M=\mathbf T=0$，
$$
\boxed{
J(V_{\mathscr D_N(x)})=
N(b+z_N(x))+\sum_i n_i(N)s_i=x.
}
\tag{32}
$$
这是完整函数等式，不是极限或锥近似。$N$、$n_i(N)$、词顺序和全部构件固定，只有 $z_N(x)$ 按 $x$ 作 $C^1$ 变化。所以(32)是同一有限真实 $C^1$ 截面。

所有未清的 prototype、桥及开球基准都已进入 $b,s_i,e_N$；没有把随 $N$ 增长的成本藏成 $O(1)$。只有由整数取整产生的中心误差 $e_N$ 有一致界，开球半径则被实际 $N$ 次复制放大到 $N\epsilon$。

本节不使用负时间、倒行变号、任意实数复制，或“closed cone 等于 actual semigroup”的无条件替代。实际开球(27)正是必需的新几何输入。

## 8. 同一个固定物理窗口与原 scalar germ 的合法化

以上有限选择在 universal 成本延拓中完成。现在保持最终母、其物理宽度、全部中心及右锚不变，将真正使用的有限紧路径族放进指定物理窗口。

设全部实际 profiles 的支持包络在有限区间 $I=(\ell,r)$ 内，指定原常值 germ $g$ 已在该窗口合法，即
$\omega_g+\ell>0$。选
$$
-\ell<\Omega<\omega_g.
$$
第6—7节只用有限个固定块及一个固定紧参数球。它们的 $\omega$ 有共同有限下界。取一个足够大的固定 $c>0$，对这些控制块统一作 R89 的真实变换
$$
h\mapsto h,\quad k\mapsto k,\quad\omega\mapsto\omega+c.
\tag{33}
$$
所有变换后路径均有 $\omega>\Omega$；其共同端口是 $g_c$，frame 及 $M=\mathbf T=0$ 保持。变换的成本是 $e^{cN}V$，全部输入和输出协变均由 R89 的同锚完整身份保证。

因 $K=\ker J$ 对 $N$ 稳定，存在一个确定可逆线性作用 $\mathsf T_c$ 于 $P$，使
$$
J(e^{cN}V)=\mathsf T_c J(V).
\tag{34}
$$
本稿没有改变最终 profiles 的位置或宽度；(34)只是同一查询映射下对实际几何成本变换的准确代数记录。

使用 R354 §§8—9 的带严格 $\omega$ 下界版本，固定一条真实桥
$$
A:g\longrightarrow g_c,\qquad
M_A=0,\quad F_A:I\to I,\quad\omega_A>\Omega.
$$
它及同一桥的真倒行都在原窗口合法。定义
$$
a_A=J(V_{AA^R})=J(2V_A)\in P.
$$
这里 $AA^R$ 是实际 $M=\mathbf T=0$ 字，故不需要先假定开桥 $V_A$ 自身属于 $U$。

整个控制字只在最外层加这一个桥对。其完整成本为
$$
V_{A\,(\mathscr D_N(x')\text{ 的变换})\,A^R}
=2V_A+e^{cN}V_{\mathscr D_N(x')}.
\tag{35}
$$
给定原目标 $x$，取
$$
x'=\mathsf T_c^{-1}(x-a_A).
\tag{36}
$$
(32)—(36)准确给原目标 $x$。选择顺序很重要：

1. 先冻结第6节的小开球族和(28)的有限配平块；
2. 冻结共同 $c$、合法桥 $A$ 及其全部基准；
3. 将目标紧集按(36)变换；
4. 最后按(30)—(31)选一个有限 $N$。

整数复制不扩大第1步的 scalar 包络。因此不存在为未知 $N$ 追改 $c$、窗口、母形或原规范的循环。所有实际路径满足
$h>0$、$x+\omega(s)>0$；原 $\alpha_s=h^2T$ 及中心线位移仍逐段真实累计，没有重设位置。

这给出固定合法 $I$、固定最终母和固定原 $g$ 上的结论：
$$
\boxed{
\text{任意紧 }\mathcal K\subset J_{\rm tr}(U)
\text{ 都有同端口、frame }I,\ M=\mathbf T=0
\text{ 的有限实际 }C^1\text{ 截面。}
}
\tag{37}
$$
不附加总长、scalar 导数盒、嵌入或 reach 上界。若另有这些约束，需单独证明；本稿不沿用一个未包含新有限控制块的旧度量实例。

## 9. 与原两个 period 和同一个十三行规范的接线

(37)同时控制 whole $E$、当前自然 totals、全部 universal ordered 通量以及最终库每个实际 Af 点的两通道 partial。故在原共同零目标中：

- whole pure 与 whole self-$Q$ 为零，真实平台二次尾条件保留；
- $\mathcal A$ 给原 self 和 ordered 总通量，$\mathcal O_{\rm all}=0$ 给 R433 的真实 current 身份；
- $F=0$ 给所有真实角色、全部后缀、全部对应复制的内部 Af 累计条件。

R460 的 simple-$p$ 分析因此可按原前提使用：多个简单 $p$ 零点自动无新增 residue，Af 根则由这里真正支付的 partial 保证；左平端与右端总通量仍由原完整 identities 支付。它给两条原 period forcing 的真实 smooth range，gap 积分与平台连接继续按 R460/R464 的同一逆选择处理。这里没有先假定逆存在再把通量当作零，也没有为两条 period 分别改一个输入圆。

若基准几何含指定非零 hook $T=\tau\mathfrak H$、非恒端 germs 或既定 incoming，则把其**完整**成本记为原 $V_{\rm base}$，按 R467/Klein 的准确组合
$$
V_{\rm total}=V_{\rm base}+4V_B
$$
选目标
$$
J(V_B)=-J(V_{\rm base})/4 .
\tag{38}
$$
控制块自身 $M=\mathbf T=0$，所以不改变原低阶 hook 和端 germs；基准的所有新旧通量均在(38)内。这里使用的是原已给该组合公式的共同基准，不从单条开桥任意外推。

最高规范行也保原已付入口。R467 的
$K_P=\mathcal B_P\mathfrak H$ 满足 $\ker J_{\rm aff}$，因此也满足 $\ker J_{\rm tr}$；其在同一固定 $\tau$ 和同一输入库上的真实最高变化为
$-\eta_P/\tau\ne0$。R467 的 finite vertical 增强证明只需要一个原联合映射的实际 $C^1$ 截面、这个原 kernel 方向及完整非零基准。现在用(37)替换其中原有条件的 $J_{\rm aff}$ 截面，便能在保持全部实际 period 行的同一真实字中付该最高 $d$ 目标；不要求额外 $H$ 查询同时零。

在原 R450/R464 从起点已完成的 $8\times12$ 包装和 $M_3\ne0$ 等前提下，选择其同一个真实多项式 particular：最高 $e$ 行与九行 odd 部分按原完整差分消去；余九行及三合法行按 R461/R464 的同相位、同一个独立二阶规范完成。所有 third incoming、同一个 $\tau$、gap 修正及端口基准按这些原稿留在右侧；本稿不宣任意另选 particular 的读出也自动相同。

以上接线只替换原来未闭的实际 partial 成本接口。它不支付其余 $s$ 段全部第四 ruling 的 source quotient compatibility，也不使任意真实桥自动满足点态 ruling 方程。R492/R494/R505 等原全路径条件、嵌入与最终可见弯曲仍须在同一机制上继续完成，不能把(37)称为 README 主问题已经解决。

还须保母库身份：本稿是 R459 从起点允许共同内区变形、保持原 $q/F^\star$ 和共同 cap 的母库。[R512](R512-fixed-compact-second-mother-and-complete-linear-path-gauge-obstruction.md) 与 [R517](R517-periodic-scalar-ruling-and-automatic-real-matrix-return.md) 使用的则是另一字面同形母库；二者的收据不能直接拼成同一个输入圆。本稿实际控制字中的常态 collar、原 prototype 和高度脉冲也没有由成本截面自动获得逐点 $K=0$。后继必须在这同一母库、同一个固定规范和完整历史下支付非恒连接或另给从起点一致的新机制。

## 10. 与 cap 障碍的准确关系

R513 排除的是：在该合法正 Af 完成图中，两个完整 weight-zero self 类满足使 $J_{\rm aff}$ 满锥所需的五个 cap 条件。因此对那个**加厚后的映射**，$\lambda_+$ 可以下降，实际正时长零目标受到真实阻碍。

本稿不改变 cap 的符号、双端 germs、真实 $C$ 尾或原完整成本。它保留原 period 所需的 $J_{\rm tr}$，而利用(6)、双极端正性和(8)证明其没有非零正分离泛函。这个较小映射的核中允许混权的 $V_\#$；它不属于加厚后的核，正好解释两结论为何相容。

从 signed 核见证到 actual 的缺口由第4—7节的新证明支付：完整真实导数张成、一个非零基准开球、有限实际正配平和整数复制。不是从 $JV_\#=0$ 直接宣称 $V_\#$ 可行走，也不是将桥的成本或真实 suffix 删除。

本稿最终交付的是(37)的固定宽度完整实际截面及第9节的原 period／规范接线。后继应在这个同一个实际字上继续处理剩余点态 ruling 与全局几何条件，不再为取得那些额外正伸缩 partial 的零目标搜索已被 R513 排除的 cap。
