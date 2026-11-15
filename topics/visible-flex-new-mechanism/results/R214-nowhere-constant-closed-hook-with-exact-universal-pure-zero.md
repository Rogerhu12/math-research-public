# R214：无开常状态段的真实全 pure 控制与精确闭 hook

日期：2026-11-15。作者及推导责任：tail_cost；root 阅读后登记。**完整纸面存在证明；没有新的研究编译、profile 评价或几何计算。**

依据 [R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R71](R71-third-holonomy-commutators-and-complete-fourth-P1.md)、[R72](R72-same-state-zero-second-third-arbitrary-frame-bridge.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R189](R189-nowhere-constant-state-matrix-bridges-and-closed-hook-geometry.md)、[R206](R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md)、[R208](R208-every-universal-pure-response-has-a-second-jet-representative.md)、[R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) 和 [R212](R212-C1-sections-for-complete-real-pure-cost-control.md)。

本稿补齐 R210/R212 特别留下的精确零迁移门。没有把“pure 零连续”误当作一个开条件，也不假设 R189 的九参数矩阵已经包含完整第三算子。完整 T 改用真实路径词恒等式保持；真正的全 pure 非线性约束先用有限维 IFT 解掉，之后才使用 Baire。

## 1. 命题与端口类别

固定 scalar 端值 $g=(h_*,k_*,\omega_*)$，$h_*>0$。本稿的**平端口**表示两端所有正阶 scalar 导数都为零、端值固定；不要求端点附近有一个正长度开常区间。frame 与 scalar 端 jets 的匹配仍足以使有限拼接光滑。

记 $\mathcal S_{\rm nc}$ 为以下实际路径的集合：有限、光滑、同平端口、frame $I\to I$、$M=T=0$，并且内部没有任何非空开区间使 $(h,k,\omega)$ 同时常值。仍用 R210 的整个 universal pure 空间 $P=\pi U$。

**定理 A。**

$$
\boxed{\{\pi V_B:B\in\mathcal S_{\rm nc}\}=P.}
\tag{1}
$$

这是实际有限路径结论，不是闭锥或线性 span 结论。对每个指定目标 p，可选一个准确实现 p 的无开常段路径；它还位于一个低阶条件保持的局部 $C^1$ pure 满秩族中。本文只保证被选中的目标路径无开常段，不宣称该性质对邻近全部目标是开性质。

**定理 B。** 存在有限光滑闭合周期浸入带，其 scalar 状态无开常段，且

$$
\boxed{
M=0,\quad T=\kappa\mathfrak H\ne0,\quad
F_{\rm end}=F_{\rm start},\quad
\alpha_{\rm end}=\alpha_{\rm start},\quad
\pi V=0
}
\tag{2}
$$

为完整同右锚 universal 函数身份。其可选 R183/R199 合法重叠 profile 圆，完整二、三阶 range 保持，最右 pure period 必要门准确为零。

本稿不授完整 mixed period/ruling、嵌入、reach、幅度或同一固定度量上的有限等距族。最终几何改变度量；应先选定它，再固定后续目标。

## 2. 平端口成本仍在原有限空间中

R105 的 U 先由开常值 germs 上的实际 M=T0 成本定义。不能只把这个定义中的 germ 改一个词就扩大空间。

R109 的原式局部化在任意光滑切点成立；它不要求中途插入开常段，也不重置历史。对整块 M0，有

$$
V_B-\int_B L\,ds\in R,\qquad
L=v-\mathcal B_mN.
\tag{3}
$$

其初始常势项由整块 M0 消去。R130 用同一 $\Gamma$ 减去 $\Gamma m_0,\Gamma m_2$；全矩阵积分为零，故积分不变。R129 的两个边界势 $P_1,P_3$ 具有正几何导数权：全部端 scalar 正阶 jets 为零，就足以使其端值为零，不需要开常区间。

因此对本稿平端口、M0 路径，式 (3) 的积分仍是 R130 十四族状态系数值的有限维积分，属于 K。由于 R130 已证明原空间

$$
U=R+K,
\tag{4}
$$

便有

$$
V_B\in U,\qquad \pi V_B\in P.
\tag{5}
$$

这里可先在 R130 的固定有限真实环境 E 中取积分，再用 (3)、(4) 得到归属；没有把冗余原式当独立坐标。

同 k 真倒行、第三 composition、零 M 块的第四加法都只需要平滑匹配与同锚。R189 §5 已逐项说明全端 jets 足够。因此它们在新的端口类别仍准确成立。特别 M0、frameI、同平端口的 $B B^{\rm rev}$ 有 M=T0、成本 $2V_B$，倒行第四仍为正号。

式 (5) 保证后文所有新 pure 残差都在同一个 P，不需要额外的“邻近函数空间”假设。

## 3. 带自由 h 扰动的正则实际原语

### 3.1 正则原语的定义

先取 R70 的某个固定有限正则桥族。用 $\theta$ 表示后来需要的有限端数据或矩阵目标参数，用 $a\in\mathbb R^8$ 表示其八个内部正则参数。原族满足：

- 给定首末 scalar 端值与全端 jets；
- 给定首末 frame，且这一 frame 匹配对全部邻近 a 精确；
- 在目标解 $a_*(\theta)$ 处，$D_aM$ 可逆；
- 原 omega 终值对 a 已固定；
- k 的导数在桥中不恒零。

最后一点由 R70 的正、负辅助圆之间的连接保证。真实辅助圈数已固定，不随自由扰动改变。

把整个原语记录在 $x\in[0,1]$，同时保真实长度 $L(a,\theta)$ 和速度因子。写原 scalar 为 $k_{a,\theta}(x),h_{a,\theta}(x)$。选择一个紧支撑 $\zeta$，使

$$
c_\omega=-\frac12\int_0^1
\frac{k'_{a_*,\theta_*}(x)\zeta(x)}{h_{a_*,\theta_*}(x)^2}\,dx
\ne0.
\tag{6}
$$

缩小有限参数邻域后，相关导数保持非零、$D_aM$ 保持可逆。

### 3.2 非线性九约束先准确求解

令

$$
\mathcal X_\infty=
\{\eta\in C^\infty([0,1]):
\eta^{(j)}(0)=\eta^{(j)}(1)=0\text{ 对全部 }j\ge0\}.
\tag{7}
$$

对小 $\eta$ 和一个附加实参数 b，取

$$
\widehat h=h_{a,\theta}+\eta+b\zeta,\qquad
\widehat k=k_{a,\theta},\qquad
\widehat\omega(x)=\omega_-(\theta)
+\int_0^x\frac{k'_{a,\theta}(t)}{2\widehat h(t)}\,dt.
\tag{8}
$$

frame 沿原 k 和真实长度求解，所以 frame 目标仍精确。h 严格正；全端 scalar jets 保持。omega 的末值由下列约束恢复：

$$
G(a,b,\eta,\theta)=
\bigl(\widehat M-M_*(\theta),\
\widehat\omega(1)-\omega_+(\theta)\bigr)=0.
\tag{9}
$$

在原解处，

$$
D_{(a,b)}G=
\begin{pmatrix}
D_aM&D_bM\\
0&c_\omega
\end{pmatrix}
\tag{10}
$$

可逆。所有矩阵都使用 (8) 的真实 omega，未在 h 改变后保留旧 omega。

取足够高的一个有限 r，使所有有限场恢复、成本和约束在 $C^r$ 邻域中为 $C^1$。在端 jets 至 r 阶为零的 Banach 参数空间上，带参数的有限 IFT 给

$$
a=a(\eta,\theta),\qquad b=b(\eta,\theta),
\tag{11}
$$

使 (9) 对整个邻域**非线性地准确**成立。将其限制到 (7)，每条路径空间上仍为 $C^\infty$，映射对 Fréchet 拓扑连续，并沿光滑方向 $C^1$。需要给定有限 $C^m$ 精度时，先取 r 足够大，再缩小扰动邻域。

这就是后文的一个“正则实际原语”。其 M、omega/frame 端点已准确保持，但 T 和第四成本可以改变；不为单个原语声称 T 固定。

### 3.3 正则前缀加任意固定后缀

还允许以下类型原语。取任意固定同端口 M0/frameI 路径 B，并在前面加一个 R70 正则 M0/frameI 桥 $A(a)$，形成

$$
W(a)=A(a)B^N
\tag{12}
$$

，其中 N 为固定有限整数。原族中第二矩阵相加，故 $D_aM_W=D_aM_A$ 可逆；frame 和 omega 端点对 a 保持；k 不恒定由 A 保证。

将**整个** (12) 作为一个原语使用 (8)–(11)。自由 h 扰动遍及前缀、后缀及其所有内部常段，不只扰动 A。扰动后不再假设内部 B 副本的矩阵仍各自为零，也不逐段重置 omega；只使用整块 (9) 准确给的 M0。这一点允许给任意旧实际成本添加可用的正则自由参数。

## 4. 用正则配对原语保留有限满锥见证

由 R210 的 $C_{\rm p}=P$，可选有限个原实际 M=T0、frameI 成本 $p_i=\pi V_{B_i}$，其正锥就是 P。等价地，可选有限正组合的凸包使零在内点；这个有限满锥性质对各向量的小扰动稳定。

取固定正则 M0 前缀 A，把

$$
W_i=A B_i^N,\qquad D_i=W_iW_i^{\rm rev}.
\tag{13}
$$

作为新的实际见证。原未扰动处，准确第四加法给

$$
M_{D_i}=T_{D_i}=0,\qquad
\pi V_{D_i}=2\pi V_A+2Np_i.
\tag{14}
$$

于是

$$
\frac{\pi V_{D_i}}{2N}=p_i+\frac{\pi V_A}{N}.
\tag{15}
$$

选一个充分大但有限的 N，有限向量组 (15) 仍有满正锥。这里除以 $2N$ 只用于正锥的向量比较，不代表分数次实际路径。

每个 $W_i$ 现在按 §3.3 作正则原语。对所有允许自由扰动，其整块 M0/frameI/平端口精确保持，所以整个配对 $D_i$ 的 M=T0 仍由真倒行精确保持，不要求 $T_{W_i}$ 固定。足够小的扰动也保留有限满锥性质。

这提供可用于 R206 的满锥见证，同时把其所有可能常段放进自由扰动原语中。没有保留一个不能修改的固定 B 内部常区间。

若 P=0，不需要满锥见证，只需任取一个正则 M0 原语接其真倒行；后文 Baire 论证仍适用。

## 5. 纯响应基可以全部用完整第三交换子词实现

这里不假设任意完整 $W$ 方向都具有一个新光滑第三右逆。

R208 §2 从旧完整 151 列的 sound 覆盖证明

$$
W_\Delta=(W_{71})_\Delta,\qquad
W_{71}=\operatorname{span}\{[\Phi_i,\Phi_j]:i<j\}.
\tag{16}
$$

而纯响应的完整原式只读 cubic diagonal：

$$
\pi\mathcal B_E(\tau)
=\frac18\left(
D\tau_\Delta(q)[E(q,q)]-2E(q,\tau_\Delta(q))
\right).
\tag{17}
$$

所以整个 $L=\pi R$ 由有限个
$\pi\mathcal B_{E_a}([\Phi_i,\Phi_j])$ 张成。可从这些**单个实际生成器**中选 L 的基；不须把一个抽象线性组合直接当成路径。

R71 §5 的精确词使用同一实际族 $A(t)$，矩阵为 $tP$，及固定矩阵为 Q、$-Q$ 的 B、C：

$$
W(t)=A(t)BA(-t)C,\qquad
\mathcal L(t)=W(t)W(-t)^{\rm rev}.
\tag{18}
$$

$W(\pm t)$ 整块 M0，因此真倒行合法，且

$$
\boxed{M_{\mathcal L(t)}=0,\qquad
T_{\mathcal L(t)}=2t[P,Q].}
\tag{19}
$$

把 A、B、C 都替为 §3 的正则实际原语，只要它们的矩阵、frame 和端口保持，(19) 对每个自由扰动仍是**完整外/内三槽算子**身份。未知 $T_{A(t)},T_{A(-t)},T_B,T_C$ 在相同对称词中准确消掉。

同一个 A 族的各次出现必须共享同一自由扰动；不能在 $W(t)$ 与 $W(-t)$ 中用两条无关路径。代码式计数在此只用于有限词索引，没有新的研究运行。

式 (16) 仅用于选择 pure 响应基；没有声称完整 $W=W_{71}$，也没有把 diagonal 相等误作完整第三算子相等。所选 prototypes 的完整 T 始终由 (19) 自己给定。

## 6. 整个 pure 控制词的低阶数据逐类保持

重新按 R206/R212 的证明构造完整 pure $C^1$ 截面，使用 §4 的正则配对见证、§5 的交换子 prototypes，以及 §3 的矩阵/变端口桥。所有整数和词在一个固定目标邻域内固定。其原语只有有限种、实际出现次数有限。

引入每种原语的自由 h 参数后，暂时仍使用**原来** R212 截面中的连续控制参数函数，不重新假设商成本已匹配。各低阶条件按以下真正恒等式保持：

| 路径词 | 所需原语约束 | 精确保持的数据 |
|---|---|---|
| $W_iW_i^{\rm rev}$ | 整块 $W_i$ 的 M0/frameI/平端口 | M=T0 |
| R71 的 (18) | 同一个 $A(\pm t)$、固定 $tP,Q,-Q$ | M0，完整 $T=2t[P,Q]$ |
| 商缩放夹心 $A(H)(D_i^H)^nA(H)^{\rm rev}$ | $A(H)$ 的 M0、准确变端口/frame；$D_i$ 的 M=T0 | 同原端口/frame，M=T0 |
| prototype 加商校正 | 原第三 prototype 加 M=T0 字 | 原完整 $\tau_j$ 不变 |
| R101 的响应复制字 | 准确 $M_{A(t)}=tE$、同一 $\pm t$ 族、prototype M0/T固定 | 整个字 M=T0 |
| 最后商校正及各大块拼接 | 各大块 M=T0 | M=T0，第四成本准确相加 |

缩放是真实 $h\mapsto Hh,\omega\mapsto\omega/H$；frame 保持，M=T0 的零值保持。变端口桥的实际 omega 终值由 (9) 支付。夹心两端 scalar 端口准确返回，并保真实桥第四成本的两倍。

R101 的响应词中，$C_t=A(t)A(-t)$ 整块 M0，完整 $T_{C_t}$ 是 t 的偶函数；最后接 $(C_{-t})^{\rm rev}$ 后 T 准确相消。这不要求单个 $A(t)$ 的 T 保持，也没有把真实倒行第四成本变号。

每个非零 frame 桥若出现，按 R72 的 $B B^{\rm rev}$ 半角构造；原语 B 保 M0、frame $I\to A$，其复合 frame 是 $ADA^TD$，T 准确相消。h 自由扰动不改变这个指定 frame。

于是自由扰动后的整条控制族，记为

$$
\mathscr D_\eta(u),
\tag{20}
$$

对所有邻近 $\eta,u$ 仍有完整 M=T0、frameI、同一平端口。商成本可能改变，L 成本也可能改变；两者都留给下一步的**全 P 校正**。

## 7. 非线性全 pure 校正先于 Baire

固定一个目标 $p_*\in P$。先在 $\eta=0$ 时用 R212 取得其邻域上的完整截面，因此

$$
\Phi_0(u):=\pi V_{\mathscr D_0(u)}=u.
\tag{21}
$$

只需要目标邻域足够小，使所有有限原语调用的连续参数留在 §3 的正则域内。若同一原语出现多个参数值，取这些有限值附近的共同小域；原函数同名重复使用同一实际族，不能任意重选分支。

设原语自由参数总空间为有限乘积

$$
\mathcal X=\prod_{j=1}^{J}\mathcal X_\infty.
\tag{22}
$$

这里先取 r 足够大，覆盖本有限词的全部原式最高有限 jets、约束及成本的一阶参数导数。Banach 自由空间取 $C^r$ 中端点至 r 阶 jets 全零的闭子空间。$C^\infty$ 全端平函数在该空间中稠密：先用端点 flat cutoff，再在内部作光滑逼近，可使全部至 r 阶导数收敛。对这些光滑参数，§2 已给成本在 P 中；(9) 的 IFT 解及真实成本在固定有限真实环境 E 中为 $C^1$，故由逼近和有限维 P 的闭性，P 归属也延伸到整个所用 Banach 邻域。因 P 是线性闭子空间，成本的一阶导数同样取值于 P。

因此在这个 Banach 参数邻域上，(9) 的所有有限 IFT 及完整成本均为 $C^1$，并准确有

$$
\Phi_\eta(u)=\pi V_{\mathscr D_\eta(u)}\in P
\tag{23}
$$

有定义；在原点 $D_u\Phi_0=I_P$。先应用**全 P** 的带 Banach 参数 IFT，得到

$$
u=u(\eta),\qquad
\boxed{\Phi_\eta(u(\eta))=p_*}
\tag{24}
$$

在一个非空邻域内准确成立。其整数和词不变。这里不是只调 r 个响应参数；自由扰动产生的 Q 分量也由 (24) 支付。

将这个解域与 (22) 相交，得 Fréchet 空间中一个非空开集 $\mathcal U$。对所有 $\eta\in\mathcal U$，完整低阶和 pure 目标已非线性地准确满足。每个成员在空间变量上为 $C^\infty$，并沿光滑参数方向可微。

因此后面的 Baire 不是拿一个有限一阶核替代原方程。它是在已求出的全体精确解中，选出没有开常段的一个。

## 8. 所有原语发生位置的坏集都闭且无内点

### 8.1 固定发生位置和固定局部区间

把 (20) 的有限整数词展开。对每个原语发生位置 o，在其自身固定坐标 $x\in[0,1]$ 中记实际 scalar 为

$$
h_\eta^o(x),\qquad k_\eta^o(x).
$$

所有连续参数已取 (24)。同一原语的不同调用共享相应 $\eta_j$；它们的连续参数值可以不同，但实际调用数仍有限。

真正倒行只反转局部坐标，正缩放只将 h 乘非零正数，ambient 左旋不改 scalar。记 $\sigma_o$ 为发生位置坐标到其原语自由坐标的映射：在上述单位区间约定下，它是恒等或 $x\mapsto1-x$。无开常段与正重参数化无关，所以可在每个发生位置的固定 x 坐标检查，不冻结参数变化中的全局移动分段位置；自由 h bump 必须通过 $\sigma_o$ 拉回到实际原语坐标。

对有理端点 $0<a<b<1$，置 $J=[a,b]$，

$$
\mathcal B_{o,J}
=\{\eta\in\mathcal U:
(h_\eta^o)'=(k_\eta^o)'\equiv0\text{ 于 }J\}.
\tag{25}
$$

omega 由真实方程给出，所以 (25) 正是该处三 scalar 同时为常数。由 $C^1$ 空间连续性，坏集在 $\mathcal U$ 中闭。

### 8.2 同时杀掉全部有限补偿的一阶变化

任取 $\eta_0\in\mathcal B_{o,J}$，设发生位置 o 来自第 j 类原语。将坏区间拉回其原语自由坐标，只改变 $\eta_j$，取方向

$$
\psi\in C_c^\infty\bigl(\sigma_o((a,b))\bigr).
$$

在当前实际参数值处，对同一第 j 类原语的**每一次有限调用**，加入其九约束 (9) 对自由 h 的一阶变化为零的条件。必要时同一个参数值重复出现只算同一条件；无需减去重复才能成立。

另外加入全 P 成本映射在固定外坐标 u 时的条件

$$
D_\eta\Phi_{\eta_0}(u(\eta_0))[\psi]=0.
\tag{26}
$$

这些都是 $\psi$ 上有限个连续实线性泛函。拉回后的开区间仍非空，其紧支撑光滑函数空间无限维，故存在非零 $\psi$ 同时满足全部条件。例如取多于这些行数的互不交 bump 再取一个非零核向量即可；这只证明存在，不进行任何新的研究积分。

沿 $\eta(t)=\eta_0+t\psi$，由 (24) 与可逆 $D_u\Phi_{\eta_0}$，

$$
u'(0)=0.
\tag{27}
$$

因此所有外部连续原语参数的一阶变化为零。由各个九约束的可逆 Jacobian (10) 及刚选的自由一阶变化为零，每次调用的内部补偿也满足

$$
a'(0)=b'(0)=0.
\tag{28}
$$

(26) 中的 $\Phi$ 是已经包含内部补偿的真实完整映射；即使不预先利用九行条件，也定义无误。两组条件同时取核只会增加有限行，仍有非零自由方向。

### 8.3 真实 h 的一阶变化确实非零

在选中的发生位置 o，(27)、(28) 给真实 k、长度及外部缩放参数的一阶变化为零，真实 h 的一阶变化准确为 $c\,\psi\circ\sigma_o$，其中 $c>0$ 为可能的正缩放因子。倒行的坐标导数为负，不能把该导数符号省掉。

非零紧支撑 $\psi$ 不可能处处导数为零，取 $y_0\in\sigma_o((a,b))$ 使 $\psi'(y_0)\ne0$，再令 $x_0=\sigma_o^{-1}(y_0)$。因为当前是坏区间，

$$
(h_{\eta(t)}^o)'(x_0)
=t\,c\,\sigma_o'(x_0)\psi'(\sigma_o(x_0))+o(t)\ne0
\tag{29}
$$

对充分小非零 t 成立，因为 $\sigma_o'=\pm1$ 非零。于是任意坏点邻域都有精确解不在该坏集，$\mathcal B_{o,J}$ 无内点。

有限发生位置与有理区间的集合可数；$\mathcal U$ 是 Baire 空间的非空开子集，故

$$
\mathcal U\setminus\bigcup_{o,J}\mathcal B_{o,J}
\tag{30}
$$

稠密且非空。选其中任一 $\eta_*$。

此时每个原语的每个实际调用都没有开常段。有限拼接、复制、真倒行、正缩放及 ambient 左旋不会生成开常段：任何跨接点的非空开区间仍含某个原语内部的非空开区间。所有修正桥、正则前缀、商夹心、第三 prototypes、响应字及最终校正都已在这些发生位置中；没有遗留一个未被扰动的常段控制块。

由 (24)，最终路径仍准确实现 $p_*$。这证明定理 A。

## 9. 非零第三 hook 和真实空间闭合也一起保持

可以先使用 R189 已有的无开常段闭 hook 背景，再用定理 A 作 R210 的四副本 pure 校正。为更明确地把**所有**构件放进同一证明，也可直接采用以下联合版本。

R180 的 hook prototype 使用 R71 的真实 $\mathcal L(t)$，$t\ne0$，以及 R72 的两个零 M、零第三 frame 桥。它们都可用 §3 的正则原语表示；完整 T 与 frame 按 §6 的原恒等式保持。令其未校正 Klein 闭词为 $X_\eta^0$，则对所有自由扰动，

$$
M_{X_\eta^0}=0,\qquad
T_{X_\eta^0}=\kappa\mathfrak H\ne0
\tag{31}
$$

准确成立。

把 (20) 的同一个 M=T0 控制块插入其中一类 prototype，并按 Klein 八边词使用四次。由于每类 prototype 在

$$
\mathcal G=\{I,g_1,g_2,g_1g_2\},
\qquad \sum_{g\in\mathcal G}g=0
$$

的四个左旋位置各出现一次，**每个扰动后的新真实位移**分别相消，frame/scalar 平端 jets 也准确匹配。没有先给单桥位移设零。

新总 pure 成本为

$$
\Theta_\eta(u)=\pi V_{X_\eta^0}
+4\pi V_{\mathscr D_\eta(u)}.
\tag{32}
$$

未扰动处由 R212，

$$
\Theta_0(u)=\pi V_{X_0^0}+4u,\qquad D_u\Theta_0=4I_P.
\tag{33}
$$

在 $u_*=-\pi V_{X_0^0}/4$ 附近，先用全 P 的 IFT 精确解 $\Theta_\eta(u(\eta))=0$。第 8 节的 Baire 论证只需将 (26) 换为 $D_\eta\Theta[\psi]=0$，并把背景 hook/frame 原语也包括在有限发生位置中。所有论证不变。

得到的最终闭词同时满足 (2)，且任何内部开区间都非恒状态。这不是先扰动 pure-zero 几何再只保小残差；(32) 的完整非线性目标在 Baire 选择之前就已经准确解出。它也不要求一个未证明的完整第三 Jacobian：T 由 (18)、R101、真实配对和 R72 的结构式保持。

## 10. 物理区间、合法圆及剩余任务

所有整数、原语类型和连续参数小邻域均有限，h 与 omega 有统一界。先固定这些有限控制域，再取共同物理 I，使 h 与 $\xi+\omega$ 保正间隙；最后将自由扰动邻域缩小以保该间隙。所有旧右锚、真实 omega 累计和输入历史保持，没有逐块重置空间位置或 profile。

全端 jets 匹配使原真实有限 range 恢复仍合法。可以在最终几何上选 R183/R199 的重叠导数分包圆：M0、同非零 hook 和八包有限差分支付完整二、三阶 range，$\pi V=0$ 又准确支付 R198 的整个最右单 profile period 门。无开常段仅移除了 R187/R193 某些常状态障碍的一个前提，不说明剩余 mixed/ruling 条件自动可解。

定理 A/B 的全 pure 正则性和无开常段现在共同成立。下一仍须处理 [R211](R211-finite-range-conditions-and-Green-inverse-for-fixed-circle-period-gauges.md) 的两 mixed 目标、内部通量/平台条件及 R184 同一个二阶 gauge 的 ruling 商。不能分别选不同的 w，也不能据本稿声称最终几何同原参考 g。完整有限等距族、全时嵌入、reach 和宏观幅度均另欠。
