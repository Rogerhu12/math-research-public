# R206：pure 闭锥为全空间与真实有限 pure 半群为全空间的等价

日期：2026-11-15。**完整条件等价定理；无新研究计算。** 本稿没有证明 pure 闭锥已经为全空间。所补的是另一层逻辑：在已经证明的 R201 权零像等号下，若该闭锥为全空间，则确实能够用有限真实路径准确支付任意完整 pure 目标，而不止取得闭锥近似。

来源：[R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R101](R101-finite-replication-and-signed-fourth-character-costs.md)、[R102](R102-finite-query-fourth-cost-control-and-cone-quotient.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R121](R121-central-baseline-correction-and-joint-fourth-query-control.md)、[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md)、[R202](R202-pure-cost-cone-and-three-remaining-negative-character-weights.md)。

## 1. 定义与准确结论

固定同一 scalar 常值 germ g、frame $I\to I$、canonical 规则和共同右锚，令

$$
\mathcal S=\{V_B:B\text{ 是有限真实同端口路径， }M_B=T_B=0\},
\qquad U=\operatorname{span}_{\mathbb R}\mathcal S.
$$

这里没有指定单路径的空间末位移为零。成本取完整 universal profile 算子，所有实际历史均按原传递保留。设

$$
P=\pi U,\qquad S=\pi\mathcal S,\qquad
C_{\rm p}=\overline{\operatorname{cone}(S)},\qquad
L=\pi R,\qquad Q=P/L,\qquad q:P\to Q,                       \tag{1}
$$

其中 $\pi V=V_{-4}$，R 是 R102 的完整真实响应空间。P、L、Q 均为有限维真实函数空间或其商；闭包在其普通有限维拓扑中取。

**定理。** 由已经证明的 $\pi U_0=\pi R_0$，有

$$
\boxed{C_{\rm p}=P\quad\Longleftrightarrow\quad S=P.}         \tag{2}
$$

右侧的意义是：每个指定的 universal pure 算子 $p\in P$ 都是某条**有限真实**同 scalar/frame、$M=T=0$ 路径的完整 pure 成本。不是允许负路径、实次数重复或极限路径。

任意有界商目标集还具有一族连续依赖目标的真实校正路径，所用重复次数可以在该有界集上固定。这一连续性是后面同时支付 L 分量所需的实际接口。

本定理不预给统一总长、中心线位移、导数盒、reach 或任意窄物理区间。给定目标所需的全部有限辅助路径和紧参数族固定后，可选共同合法物理区间；后续整数复制不扩大其 scalar 包络。

## 2. 响应商没有缩放零权

R105/R202 给真实正仿射表示，且 pure 投影与之交换。R 及 L 在该作用下不变，所以缩放在 Q 上是

$$
D_H=e^{(\log H)D},\qquad H>0,\qquad
Q=\bigoplus_{\sigma\in\mathbb Z}Q_\sigma,\qquad
D|_{Q_\sigma}=\sigma\operatorname{id}.                     \tag{3}
$$

R201 的整个权零等号给

$$
Q_0=\pi U_0/\pi R_0=0.
$$

因此

$$
\boxed{D:Q\to Q\text{ 可逆}.}                              \tag{4}
$$

这里需要的是**整个**权零 pure 像等号，单个 pure 目标的成员身份不足以推出 (4)。其他权是否已经在响应像中，不是本证明的前提。

若 $Q=0$，R102 对 L=P 的完整有限坐标直接给 $S=P$，保留其自身基准成本。以下先处理 $d=\dim Q>0$。

## 3. 从满闭锥取有限个实际成本的严格正配平

现在假设 $C_{\rm p}=P$。连续商映射给

$$
\overline{\operatorname{cone}(qS)}=Q.                       \tag{5}
$$

可从 qS 中选有限个实际成本

$$
q_i=q\pi V_{B_i},\qquad 1\le i\le m,\qquad
M_{B_i}=T_{B_i}=0,
$$

使它们的正锥就是 Q。说明有限选择这一步：先在 Q 中取一组基及其相反向量；由 (5) 在这些向量的足够小邻域内取有限正组合，保证它们的凸包仍含零为内点。展开这些有限正组合所用的实际 qS 向量，即得所需有限集合。

由 $\operatorname{cone}\{q_i\}=Q$，向量 $-\sum_iq_i$ 有非负表示 $\sum_i\beta_iq_i$。于是

$$
\boxed{\alpha_i=1+\beta_i>0,\qquad\sum_i\alpha_iq_i=0.}       \tag{6}
$$

这些实数只用于选择后面的整数重复次数；没有把 $\alpha_iB_i$ 当作一条路径。所选 $q_i$ 张满 Q。由 (4)，可重排使前 d 个 $Dq_i$ 独立。

## 4. 缩放环的真实端口修复和完整连接成本

R89 对整条路径作真正几何变换

$$
h\mapsto Hh,\qquad k\mapsto k,\qquad
\omega\mapsto\omega/H,\qquad\alpha\mapsto H^2\alpha.
$$

原 frame 不变，$\omega_s=k_s/(2h)$ 仍成立。若 $B_i$ 同端口且 M=T=0，其缩放路径 $B_i^H$ 也同端口、frameI、M=T=0，且完整 pure 成本为

$$
\pi V_{B_i^H}=\mathsf D_H^{\rm p}\pi V_{B_i},\qquad
q\pi V_{B_i^H}=D_Hq_i.                                    \tag{7}
$$

新 scalar 端口是 $g_H$，通常不同于 g，所以 (7) **不**说明实际半群 S 已在固定端口下直接缩放不变。

取 $H=e^t$，只允许 t 在一个固定的小闭区间内。由 R70 的端数据光滑依赖，选一族真实桥

$$
A_i(t):g\longrightarrow g_{e^t},\qquad
M_{A_i(t)}=0,\qquad F:I\longrightarrow I,
$$

两端 scalar germs 准确，桥按 t 光滑依赖。桥的第三算子可非零。用真正倒行 $A_i(t)^R$ 返回；对 frame $I\to I$，其 frame 为 $D_0F(L-s)D_0$，$D_0=\operatorname{diag}(-1,1,-1)$，scalar 沿原值倒行。R83 的零矩规则给

$$
T_{A_i^R}=-T_{A_i},\qquad V_{A_i^R}=V_{A_i}.
$$

对任意正整数 n，路径

$$
W_i(t,n)=A_i(t)\,(B_i^{e^t})^n\,A_i(t)^R
$$

因此准确满足

$$
\boxed{
M_{W_i}=T_{W_i}=0,\qquad
\pi V_{W_i}=n\mathsf D_{e^t}^{\rm p}\pi V_{B_i}
+2\pi V_{A_i(t)}.
}                                                           \tag{8}
$$

倒行第四为正号，连接成本并未消失。$2V_{A_i(t)}$ 本身是实际零矩零第三字 $A_i(t)A_i(t)^R$ 的成本，因而属于 U；无需另将任意开桥成本假设在某个未证明的环境空间内。

这些桥和缩放环都取固定紧参数族。其 scalar 包络紧、h 有正下界；任意有限复制只重复已选轨迹，不扩大包络。实际中心线位移仍逐段累加，未在 (8) 中重设位置。

## 5. floor 整数与一个统一的实际商校正族

对充分大正整数 N，令

$$
n_i(N)=\lfloor N\alpha_i\rfloor\ge1.
$$

只让前 d 个缩放参数变化，其余置零。拼接 (8) 的 m 个路径，得到 $C_N(t)$，其商成本准确为

$$
\mathcal Q_N(t)=q\pi V_{C_N(t)}
=\sum_{i=1}^m n_i(N)e^{t_iD}q_i+E_Q(t),                    \tag{9}
$$

其中 $t_i=0$ 对 $i>d$，而

$$
E_Q(t)=2\sum_iq\pi V_{A_i(t_i)}
$$

是固定光滑函数，与 N 无关。这一式保留全部真实初始历史、桥成本和右锚。

把 (9) 除以 N。由于 $n_i(N)/N\to\alpha_i$，在一个固定小 t 盒上有 $C^1$ 收敛

$$
G_N(t):=N^{-1}\mathcal Q_N(t)
\longrightarrow G_\infty(t):=\sum_i\alpha_i e^{t_iD}q_i.
\tag{10}
$$

由 (6)，$G_\infty(0)=0$，并且

$$
\boxed{DG_\infty(0)
=(\alpha_1Dq_1\ \cdots\ \alpha_dDq_d)
\text{ 可逆}.}                                               \tag{11}
$$

**统一截面命题。** 对任意给定有界闭集 $Y\subset Q$，存在一个有限 N，以及连续、事实上局部光滑的参数选择 $t_N(y)$，$y\in Y$，使

$$
\boxed{q\pi V_{C_N(t_N(y))}=y.}                             \tag{12}
$$

所有 $t_N(y)$ 留在同一个已经固定的小盒中。

为完整说明这一 uniform IFT，用 $J=DG_\infty(0)$。先取固定小半径 $\delta$，使

$$
\sup_{\|t\|\le\delta}\|I-J^{-1}DG_\infty(t)\|\le1/4.
$$

再取 N 足够大，使相同上界对 $G_N$ 至多为 $1/2$。由 (6) 和 floor 误差，$G_N(0)=O(1/N)$。有界 Y 又给 $y/N=O(1/N)$，故同一有限大 N 使

$$
\sup_{y\in Y}\|J^{-1}(G_N(0)-y/N)\|\le\delta/2.
$$

映射

$$
t\longmapsto t-J^{-1}(G_N(t)-y/N)
$$

是这个固定闭球上的自映射、收缩常数至多 $1/2$。其唯一不动点连续依赖 y，证明 (12)。这同时给一个包含 Y 的开放邻域上的光滑局部截面；不依赖逐点任意选择根。

将 (12) 的实际路径简记为 $C(y)$。其**完整** pure 成本 $\pi V_{C(y)}\in P$ 连续，L 分量未控制但在紧 Y 上有界。

成本关于紧路径参数的 $C^1$ 连续性来自 R56 的有限真实恢复和 R70 的光滑参数族：固定共同物理间隙后，全部系数、有限积分与端值均光滑。也可在有限 P 上用有限个真实 profile 查询作坐标验证；这里没有假设未付的 norm 拓扑或原函数独立历史。

## 6. 先把每个响应 prototype 的商成本准确清零

取 $r=\dim L$。若 $r=0$，(12) 已给 $S=P$。以下令 r>0。

从有限个实际原生成方向中选

$$
K_j=\mathcal B_{P_j}(\tau_j),\qquad
\kappa_j=\pi K_j,\qquad 1\le j\le r,
$$

使 $\kappa_1,\ldots,\kappa_r$ 为 L 的真基。每个 $\tau_j$ 有同端口实际零矩第三环 $L_j$，记其完整第四成本 $v_j=V_{L_j}$。虽然 $L_j$ 的 T 可非零，真实拼接 $L_jL_j^{\rm rev}$ 的 M、T 均为零、成本为 $2v_j$，故 $v_j\in U$，下面的 $q\pi v_j$ 有定义；这里取正半倍只用于线性空间归属，并未声称半条路径实际可用。

对有限个目标 $-q\pi v_j$ 使用 (12)，选择实际 $M=T=0$ 校正 $C_j$，并改 prototype 为

$$
\widehat L_j=L_jC_j,\qquad
\widehat v_j=V_{\widehat L_j}=v_j+V_{C_j}.
$$

于是

$$
M_{\widehat L_j}=0,\qquad T_{\widehat L_j}=\tau_j,\qquad
\boxed{q\pi\widehat v_j=0.}                                \tag{13}
$$

第三算子完全不改，因此响应方向 $K_j$ 仍是同一个原方向。校正可能给 L 分量很大的新成本，这个成本保留在 $\widehat v_j$ 中。

## 7. 真实响应复制、商的连续校正及最后的 Brouwer

固定任意线性分解 $P=L\oplus J_Q$，令 $\ell:P\to\mathbb R^r$ 是 L 在 $\kappa_j$ 基下的坐标投影，且 $q$ 是商坐标。此处 $J_Q$ 只是线性补空间，不是额外真实控制空间。

对新的 prototypes $\widehat L_j$ 应用 R101 的复制字，拼接得到 $Z(t,n)$。准确式为

$$
M_Z=T_Z=0,\qquad
\pi V_{Z(t,n)}=E_P(t)+n\left(2\sum_j\pi\widehat v_j+
\sum_jt_j\kappa_j\right).                                  \tag{14}
$$

$E_P(t)$ 是完整、连续的真实偶基准。由 (13)，

$$
q\pi V_{Z(t,n)}=qE_P(t),                                   \tag{15}
$$

与 n 无关。

设目标为 $p\in P$。先令

$$
t^0=-2\sum_j\ell(\pi\widehat v_j),\qquad
\mathcal C=t^0+[-1,1]^r.
$$

向量 $t^0$ 中的求和按 $\kappa$ 坐标理解。利用 R101 固定有限次复制原小二阶族，先覆盖这个紧立方体；它不扩大最初的小族 scalar 包络。于是 $E_P$ 已是一个固定连续函数。

集合

$$
Y_p=\{qp-qE_P(t):t\in\mathcal C\}
$$

紧。现在对这个集合选择第 5 节的同一个实际连续截面 $C(y)$，并令

$$
\widetilde Z(t,n)=Z(t,n)C(qp-qE_P(t)).
$$

每块 M=T=0，第四成本严格相加。因此其商准确等于 qp；L 坐标为

$$
\ell\pi V_{\widetilde Z(t,n)}
=F(t)+n\left(2\sum_j\ell(\pi\widehat v_j)+t\right),          \tag{16}
$$

其中

$$
F(t)=\ell E_P(t)+\ell\pi V_{C(qp-qE_P(t))}
$$

连续且在 $\mathcal C$ 上有界。它保留全部商校正的未知 L 成本，并在选取最后的 n 前已经固定。

取有限大 n，使

$$
t\longmapsto t^0+n^{-1}(\ell p-F(t))
$$

将 $\mathcal C$ 映入自身。Brouwer 给一个 $t_*$，使 (16) 等于 $\ell p$。商与 L 坐标同时准确匹配，所以

$$
\boxed{\pi V_{\widetilde Z(t_*,n)}=p}
$$

为完整函数身份。这证明 (2) 的非平凡方向。反向 $S=P\Rightarrow C_{\rm p}=P$ 直接由定义成立。

若 P=0，可取任一非空实际 M0、frameI 同端口桥并接其真倒行，得到非空 M=T0 路径；其 pure 成本自动为零。退化情形没有依赖一个虚构的负长度或空曲面。

## 8. 选择顺序、共同区间与空间闭合

证明涉及两个不同的大整数尺度，不能互相替换。

1. 由满锥选有限实际 $B_i$ 和严格正配平 (6)，固定其近 H=1 的缩放族及 R70 端口桥族。
2. 固定有限个响应原生成器、实际第三 prototypes 和小二阶族；若使用下述空间闭合推论，也在这一步固定背景 hook prototype 及全部 scalar/frame 桥。上述所有原路径与小参数闭邻域只有一个紧 scalar 包络。
3. 先用一个有限 N 的商截面清掉有限个 prototype 的商成本，得到 (13)。这些 N 仅增加重复数，不扩大第 1 步包络。
4. 由实际 $\widehat v_j$ 决定 $t^0$，固定覆盖其立方体所需的小族重复次数，因而固定 $E_P$。
5. 对紧 $Y_p$ 选取商校正族的另一个有限 N，固定完整连续的 F。
6. 最后才选响应复制数 n，并使用 Brouwer。

因此没有“先按未知 n 选择商校正，再改变它的基准”的循环。所有缩放参数始终在固定近 1 小盒内，所有大幅二阶参数用原小族有限重复实现。可以在第 2 步的共同包络外选择同一个合法物理 I；步骤 3–6 不扩大它。反过来，本结论不授任意预定窄 I 或统一长度上界。

路径的真实中心线位移自由而保留。若给定一个 R180 闭 hook prototype 作为背景，将所构 M=T0 控制插入其中一类 prototype，再作 Klein 八边闭合，完整成本准确增加 $4V_B$。对背景 $V_{\rm base}$ 取目标 $p=-\pi V_{\rm base}/4$，便在假设 $C_{\rm p}=P$ 下构造一个空间闭合、同一非零第三 hook、**整个 universal pure 周期为零**的真实有限几何。

随后可在共同 I 中选择 R183/R199 的合法重叠圆，或从一开始固定包络内的这类圆；其低阶支付只依赖 M0 和同一第三 hook。几何设计改变目标度量；选定最终几何后再固定该目标。此结论仍未支付 mixed 周期与 fourth ruling。

## 9. 它怎样改变剩余问题，而不预判答案

R202 给 pure 闭锥不满时必有有限候选权中的非零纯正字符；本稿把“满闭锥”这个条件的后果从闭锥近似加强成真实有限 pure 可达性。它不把某个已知完整正字符自动下降到 pure，也不把 signed span 当作路径。

因此后续若准确排除所有剩余 pure 正字符，就不再需要另补“闭锥是否足以给有限 pure 零字”的缺口；(2) 已支付该升级。若某个 pure 正字符存在，则它直接阻止 $S=P$。当前没有在本稿判断剩余字符是否存在。

即使条件成立并构造了完整 pure 零几何，完整两模式周期、同一二阶 gauge 的 joint ruling、全部高阶、收敛、嵌入、reach 与宏观幅度仍是独立未付任务。严格正的完整 canonical 字符与 pure 可达性并不冲突，因为 R201 已证明它可在 pure 核上非零。
