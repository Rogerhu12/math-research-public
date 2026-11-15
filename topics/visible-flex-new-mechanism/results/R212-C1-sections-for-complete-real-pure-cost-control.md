# R212：完整真实 pure 成本的 C1 截面与精确校正接口

日期：2026-11-15。作者及推导责任：tail_cost；root 阅读后登记。**完整纸面证明，无新的研究计算。** 本稿在 [R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) 已证明实际有限 pure 半群为全空间后，将 R206 的最后存在性步骤加强为固定有限词中的 $C^1$ 目标截面。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R101](R101-finite-replication-and-signed-fourth-character-costs.md)、[R102](R102-finite-query-fourth-cost-control-and-cone-quotient.md)、[R189](R189-nowhere-constant-state-matrix-bridges-and-closed-hook-geometry.md)、[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md)、[R206](R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md)。

这里的参数是参考几何设计参数，不是已构造的同一度量有限等距弯曲参数。本稿不宣称已将完整 pure 零迁移到无开常段几何；该项还需联合低阶约束的独立证明。

## 1. 真实全 pure 截面定理

固定同一 scalar 端口、frame $I\to I$、共同右锚与 canonical 规则，令

$$
P=\pi U,\qquad L=\pi R,\qquad Q=P/L,\qquad q:P\to Q.
\tag{1}
$$

**定理。** 对任意紧集 $K\subset P$，存在有界开邻域 $\mathcal O\supset K$ 和一族有限真实路径 $\mathscr D(p)$，$p\in\mathcal O$，使

$$
\boxed{
M_{\mathscr D(p)}=T_{\mathscr D(p)}=0,\qquad
F_{\mathscr D(p)}:I\longrightarrow I,\qquad
\pi V_{\mathscr D(p)}=p.
}
\tag{2}
$$

首末 scalar germs 固定。所有构件、词排列和整数复制次数在 $\mathcal O$ 上固定；只有有限个连续几何参数按 p 作 $C^1$ 变化。按固定参数区间记录真实长度、frame、scalar 和位置后，实际路径族也是 $C^1$ 的。

所用 scalar 包络紧，h 有统一正下界；可在其外选择一个共同合法物理区间。没有保证任意预定窄 I、统一总长、位移闭合、嵌入或 reach。

特别地，

$$
D_p\bigl(\pi V_{\mathscr D(p)}\bigr)=\operatorname{id}_P.
\tag{3}
$$

因此，在真正满足本定理全部低阶条件的实际几何族上，完整 pure 成本映射有有限维右逆导数。不是只在形式 coefficient 空间中求一个逆。

## 2. 完整基准 E 的真实 C1 性

R206 §7 只在最后一步用了 E 连续。其实际构造可以取 $C^1$，下面支付这一加强所需的条件。

### 2.1 固定小矩阵族和大有限参数

R70 在固定充分大有限辅助整数后，对矩阵目标与 scalar/frame 端数据给局部光滑桥截面。先选固定光滑族

$$
A_j(s),\qquad |s|<\varepsilon_j,\qquad
M_{A_j(s)}=sP_j,
\tag{4}
$$

它保持同一 scalar 端口与 frame I；真实 h、k、omega、长度及连接都光滑依赖 s。不是对不同目标任意独立选桥。

对一个以后已固定的有限 t 盒，选同一个整数 $m_j$，使 $|t_j/m_j|<\varepsilon_j$，令

$$
A_{j,t_j}=A_j(t_j/m_j)^{m_j}.
\tag{5}
$$

R101 §4 给 $M_{A_{j,t_j}}=t_jP_j$；固定整数重复不扩大 scalar 包络。(5) 仍是光滑参数族，自己的第三、第四成本完整保留。

### 2.2 场恢复及参数区间

固定有限词与共同物理间隙后，R56 的二、三、四阶恢复只含有限次真实积分、ODE、乘法、微分以及分母有正下界的系数。右锚不变，传入 scalar 历史沿整个词保留。所以完整成本随有限参数为 $C^1$。

也可固定 P 上有限个 faithful profile 查询作坐标：这些真实查询均由上述恢复给出 $C^1$ 标量函数，有限维坐标逆固定线性，因而成本在 P 中为 $C^1$。这里未将 Volterra history 当自由变量。

每个可变长度构件在固定 $x\in[0,1]$ 上记录时，同时保留真实 $ds/dx>0$；frame 方程和全部积分使用这个速度因子。拼接处全 jets 匹配，原常值 germs 保证移动接点的有限参数光滑性。不存在重参数化后偷用单位 s 速度的步骤。真实中心线位置仍按原方程累计。

### 2.3 R101 的完整复制身份

对同一个小族及实际第三 prototype，R101 给

$$
M_{Z_j(t_j,n)}=T_{Z_j(t_j,n)}=0,\qquad
\pi V_{Z_j(t_j,n)}
=E_j(t_j)+n(2\pi v_j+t_j\kappa_j).
\tag{6}
$$

$E_j$ 是有限个 (5) 构件与真倒行的完整成本之和，故是 $C^1$，与最后复制数 n 无关。有限个 j 拼接所得 $E_P(t)$ 同样是 $C^1$。本稿没有把 E 或其导数设零。

## 3. 商校正已有 C1 截面

R201 给 $Q_0=0$；缩放生成元在 Q 上可逆。R210 又给 pure 闭锥满，所以 R206 §§3–5 的有限正配平、真实缩放桥、floor 整数和统一 IFT 全部可用。

对任意紧 $Y\subset Q$，那些步骤给定义在 Y 的一个开邻域上的实际 $C^1$ 截面

$$
C(y),\qquad M_{C(y)}=T_{C(y)}=0,\qquad
q\pi V_{C(y)}=y.
\tag{7}
$$

为强调正则性不是任意选根，其方程是

$$
G_N(t)=N^{-1}
\left\{\sum_i\lfloor N\alpha_i\rfloor e^{t_iD}q_i+E_Q(t)\right\}
=\frac yN.
\tag{8}
$$

有限 N 选定后，floor 是固定整数；$DG_N$ 在同一小盒内统一接近可逆矩阵。由第 2 节，桥成本 $E_Q$ 是 $C^1$。R206 的统一收缩给唯一参数选择，IFT 给其 $C^1$ 性，所以实际 C 也为 $C^1$。

后文先固定 Y，再固定这个商截面及其整数次数，最后才选响应 n。不会按未知 n 追改桥基准。

## 4. 准确清掉第三 prototypes 的商基准

令 $r=\dim L>0$，取实际原响应

$$
\kappa_j=\pi\mathcal B_{P_j}(\tau_j),\qquad j=1,\ldots,r,
\tag{9}
$$

为 L 的基，及实际第三 prototypes $L_j$，其 $M=0$、frame I、$T=\tau_j$。它们的完整成本 $v_j$ 属于 U：真正的 $L_jL_j^{\rm rev}$ 有 M=T0、成本 $2v_j$。这个归属不是把第三非零路径直接塞入定义。

对有限个目标 $-q\pi v_j$ 用一个固定商截面，选实际 M=T0 控制 $C_j$，令

$$
\widehat L_j=L_jC_j,\qquad
\widehat v_j=v_j+V_{C_j}.
\tag{10}
$$

于是

$$
T_{\widehat L_j}=\tau_j,\qquad q\pi\widehat v_j=0.
\tag{11}
$$

$\widehat v_j$ 的所有 L 成本仍保留。

固定 $P=L\oplus J_Q$，令 $\ell:P\to\mathbb R^r$ 为 (9) 基下的 L 坐标投影，并设

$$
v^0=2\sum_j\ell(\pi\widehat v_j),\qquad t^0=-v^0.
\tag{12}
$$

在 $t^0+[-2,2]^r$ 邻域内先按 (5) 固定小族复制次数。R101/R206 的实际响应词准确满足

$$
M_Z=T_Z=0,\qquad
\pi V_{Z(t,n)}
=E_P(t)+n\left(2\sum_j\pi\widehat v_j+
\sum_jt_j\kappa_j\right),
\tag{13}
$$

并且 $q\pi V_Z=qE_P(t)$ 与 n 无关。此时 E 已是固定 $C^1$ 函数。

## 5. 最后一步的统一收缩和隐函数定理

取有界开集 $\mathcal O\supset K$，闭包紧。置

$$
\mathcal C=t^0+[-1,1]^r,\qquad
Y=\{qp-qE_P(t):p\in\overline{\mathcal O},\,t\in\mathcal C\}.
\tag{14}
$$

Y 紧。用第 3 节选一个定义在其开邻域上的真实 $C^1$ 商截面 C，随后固定其全部构件和整数。

定义真实路径

$$
\widetilde Z(t,n,p)=Z(t,n)\,C(qp-qE_P(t)).
\tag{15}
$$

两个大块 M=T0，第四成本准确相加。所以

$$
q\pi V_{\widetilde Z}=qp,
\tag{16}
$$

$$
\ell\pi V_{\widetilde Z}=n(v^0+t)+F(t,p),
\qquad
F(t,p)=\ell E_P(t)+\ell\pi V_{C(qp-qE_P(t))}.
\tag{17}
$$

F 在 $\mathcal C\times\overline{\mathcal O}$ 邻域为 $C^1$。完整商校正的未知 L 成本都在 F 中；F 在最后 n 之前已经固定。

采用 max 范数及诱导矩阵范数，记

$$
M_0=\sup_{\mathcal C\times\overline{\mathcal O}}
\|\ell p-F(t,p)\|,\qquad
M_1=\sup_{\mathcal C\times\overline{\mathcal O}}\|D_tF(t,p)\|.
\tag{18}
$$

两者有限。选择一个固定有限整数

$$
n>2\max\{1,M_0,M_1\}.
\tag{19}
$$

对每个 $p\in\mathcal O$ 定义

$$
\mathcal T_p(t)=t^0+\frac1n\{\ell p-F(t,p)\}.
\tag{20}
$$

它将 $\mathcal C$ 映入半径 $1/2$ 的内部盒，收缩常数小于 $1/2$，故有唯一不动点 $t(p)$，并有

$$
n(v^0+t(p))+F(t(p),p)=\ell p.
\tag{21}
$$

矩阵

$$
nI+D_tF(t(p),p)
\tag{22}
$$

统一可逆，逆范数至多 $2/n$。IFT 及不动点唯一性使所有局部解拼成同一个 $C^1$ 映射，且

$$
D_pt(p)=
\bigl(nI+D_tF\bigr)^{-1}\bigl(\ell-D_pF\bigr).
\tag{23}
$$

最终取

$$
\boxed{\mathscr D(p)=\widetilde Z(t(p),n,p).}
\tag{24}
$$

(16)、(21) 同时给完整 pure 身份 (2)。所有整数和词固定，连续参数 $C^1$，因此实际路径族也 $C^1$。这证明第 1 节定理。没有负路径、实数次复制或无限长度极限。

### 5.1 退化维数

若 $r=0$、P 非零，$P=Q$，第 3 节本身给全 pure 截面。若 $Q=0$，省去 (15) 的商校正因子，仅用响应部分即可；省一个因子不是把空路径当作曲面。

若 P=0，任取同端口 M0/frameI 的非空实际桥接其真倒行，得到 M=T0、pure 自动为零的常值族。

### 5.2 选择顺序和共同物理区间

先选有限满锥见证、近 1 缩放/桥小族、响应原生成器、实际第三 prototypes 和小二阶族；它们有一个共同紧 scalar 包络。然后依次：

1. 固定商截面，清有限个 prototype 的商基准；
2. 由真实新基准决定 $t^0$，固定覆盖其盒的小族复制数；
3. 对目标紧集的 Y 固定第二个商截面；
4. 在 F 和其导数均固定后，最后选 (19) 的 n。

重复不扩大 scalar 包络。共同物理区间可在第一批有限小族的包络外选择；后续只增加有限重复，不循环改 I。路径的长度和位移可能增加，这些实际量从未设零。

## 6. 已可严格使用的校正推论

### 6.1 同一低阶数据内的精确 pure 校正

设 $B_\varepsilon$ 已是一个 $C^1$ 真实族，首末 scalar/frame 固定，完整 $M=0$、$T=T_*$ 精确成立，且 $\pi V_{B_\varepsilon}\in P$。选择覆盖其所需紧目标的截面，令

$$
D_\varepsilon=\mathscr D(-\pi V_{B_\varepsilon}).
\tag{25}
$$

那么

$$
\boxed{
M_{B_\varepsilon D_\varepsilon}=0,\quad
T_{B_\varepsilon D_\varepsilon}=T_*,\quad
\pi V_{B_\varepsilon D_\varepsilon}=0.
}
\tag{26}
$$

该族按 $\varepsilon$ 为 $C^1$。更一般的 $C^1$ pure 目标 $p_*(\varepsilon)$，只需在 (25) 中取差 $p_*(\varepsilon)-\pi V_{B_\varepsilon}$。不需改变 profile 或重选一个非连续根。

若要保空间闭合，可如 R210 把控制目标除以四，插入 Klein 同一 prototype 的四个 ambient 副本；使用新 prototype 的真实位移相消。完整 mixed 成本和基础度量一般改变。

### 6.2 低阶已经保持时的 IFT 稳定性

使用已经建立的**全部 P 目标坐标** u，而不是仅 r 个响应参数 t。设外部参数 z 将实际族 $\mathscr D(u)$ 扰动为 $\mathscr D_z(u)$，且对每个 z、u，scalar/frame 与 M=T0 条件仍**准确**保持。假设该实际族及成本按参数为 $C^1$，并在一个包含 K 的固定紧邻域上 $C^1$ 接近原族。定义

$$
\Phi_z(u)=\pi V_{\mathscr D_z(u)}\in P.
\tag{27}
$$

由 (2)、(3)，$\Phi_0(u)=u$、$D_u\Phi_0=I_P$。因此充分小 z 时，$D_u\Phi_z$ 在上述邻域统一接近恒等，可用全维隐函数定理解

$$
\boxed{\Phi_z(u(p,z))=p.}
\tag{28}
$$

为使同一紧 K 上的选择明确，先取 $\delta>0$，令 K 的闭 $\delta$ 邻域仍在 $\mathcal O$。缩小 z 后可令 $\|D_u\Phi_z-I_P\|<1/2$，并令 $\|\Phi_z(p)-p\|<\delta/2$ 对全部 $p\in K$ 成立。在每个以 p 为中心的闭 $\delta$ 球上，

$$
u\longmapsto p-\{\Phi_z(u)-u\}
\tag{29}
$$

是自映射且为严格收缩；其唯一不动点由 IFT 按 (p,z) 为 $C^1$。这些唯一局部解在重叠处一致，给 K 邻域上的同一个实际精确校正。

这一步同时支付扰动的 Q 和 L 分量。一般外部扰动未必保留 (16) 的商身份，故不能只凭 r 维矩阵 (22) 修复它；只有另外证明商身份继续准确时才可仅调 t。新公式 (27)–(29) 不作这一额外假设。低阶条件仍须已经结构保持或另行准确补偿，不能以小残差替代。

## 7. 联合去常段的准确边界

R189 的九参数正则块包含八个 M 坐标和真实 omega 终值；frame 由其原 k/长度族保持。一般 h 扰动还会改变完整第三算子，**这九行不包含完整 T**。本稿给的是 M=T0 层内的 pure 正则方向，不能据此补掉任意第三误差。

设 e 表示所有还需保持的有限真实低阶约束，包含完整第三数据；若另有补偿参数 a，并已证明 $D_ae$ 可逆，则本稿 pure 截面参数 p 对这些低阶量的导数为零。对任意传入低阶历史，M=T0 控制只增加自己的完整第四成本，所以联合 Jacobian 有块形式

$$
\begin{pmatrix}
D_ae&0\\
*&I_P
\end{pmatrix}.
\tag{30}
$$

这时联合可逆性确实成立。pure 坐标在约束层上用 P 的有限 faithful 查询表示；离开该层时，同一实际查询仍有定义，不必预先把离层输出放进 P。

但是，本稿没有证明所需完整 $D_ae$ 已存在。它也可以被一个真正保持全部低阶数据的**结构恒等词**替代，条件仍须逐词支付。

若随后以 Baire 去掉开常区间，还须检查非线性约束已由联合 IFT 精确求解，并在每个坏区间找到非零 h bump 同时杀全部有限一阶补偿泛函，使有限参数的一阶修正为零，真实 h 一阶变化仍是该 bump。只找到有限泛函的核，不等于已经满足全非线性约束。

因此这里不授：

- 由 R189 的 $8M+\omega$ 自动得到完整 T 正则性；
- 由 pure 零的连续性自动迁移到无开常段；
- 加一条可能有常段的控制块后，整条路径就无常段；
- 将全端 jets 平坦与正长度开常值 germ 混为一谈。

已完成的是实际满秩的 $C^1$ 全 pure 模块；联合无常段性质留作明确的新命题。

## 8. 主线范围

R210 已支付最右 pure period 门。本稿给可微的有限控制参数，使后续在全部低阶已经精确保持时，仍能保住这个成功。

[R211](R211-finite-range-conditions-and-Green-inverse-for-fixed-circle-period-gauges.md) 的 mixed period Green/通量条件和 R184 同一个二阶 gauge 的 ruling 商仍另需支付。参考几何参数变化通常改变基础度量；选择最终几何后，仍需按同一个固定目标完成其余各阶、有限连续嵌入族、全时 reach 与宏观幅度。
