# 原二阶源的395长度充分证书：复用已成行列式与无穷远子式

日期：2026-11-15。状态：**充分判据与次数/来源接缝已证明；二阶新行列式及其 gcd 尚未运行，不预称判据通过。**

本篇消费 [R835](../results/R835-certified-original-order4-termination-and-reduced-D.md) 已完成的原 $I_4=\mathscr C$ 和
[R836](../results/R836-original-reduced-D-fixed-branch-pencil-and-short-RR-kernels.md) 的原二阶重数公式。
它使用已经完成的原 $q=4$ 来源中的较早三层，不重算导数、正规坐标、$C$ 坐标整除、原算子、Krylov 或任何 Hermite 操作。

## 1. 真正的特征零源及其长度下界

固定 $L$、原 $f_4,y,E$、同一原 canonical free1186 和原 R827 的合法素点
$\mathfrak p$，剩余域 $k=\mathbf F_{1000000753}$。记
$$
E=\mathcal C_0+P_0+3D,
\quad \deg\mathcal C_0=20,\quad \deg D=395.
\tag{L1}
$$
R835 已证 $D$ 约化，故 $\epsilon=\operatorname{mult}_{P_0}D\in\{0,1\}$。
R836 逐 DVR 重数公式给
$$
I_2=\mathcal O_Y(-E_2),\quad
E_2=\mathcal C_0+D+\epsilon P_0,
\quad \operatorname{length}_L(\mathcal O_Y/I_2)=415+\epsilon.
\tag{L2}
$$

原 canonical $B$ 不是从有限域随意 lift 的向量。原 R787 单位选行块及完整核维数28，给一个准确的 $\mathfrak p$-整特征零 $B\in H^0(5H-E)$；其模向量正是原 R824/R827 已消费的 free1186 方向。这一存在与唯一性只用真实单位子式，可以保持为准确 solve/adjugate 表达式，而不要求全部大有理坐标已展开。

在原两张仿射图，用 $B$ 乘全部272个原正规基，再取原导数层 $0,1,2$。按 R827 的原齐次权和两图运输把这些列延拓为同一 proper 整模型上的全局源映射；记其像为 $\mathcal J_2$。泛纤维上每条源列都属于原完整 $I_2$，因此
$$
\mathcal J_{2,L}\subseteq I_2\subseteq\mathcal O_Y(-\mathcal C_0).
\tag{L3}
$$
这里不假设 $\mathcal J_2$ 是全部 $I_2$，也不假设单个 $B$ 没有残余零。源的正规基乘法、导子、齐次化及合法约化全部沿原 R827，而不是从同样维数的抽象矩阵代替。

在第一图中，它包含原三层完整矩阵的像
$$
C_\tau(z)G^{(2)}(z),\qquad
G^{(2)}=[G_0,G_1,G_2]\in\operatorname{Mat}_{272\times816}(k[z]),
\tag{L4}
$$
其中 $G_r$ 就是已成 `R827-tau-layer-rrr-C-column-ccc.json.gz` 的272列。
$C_\tau$ 的 determinant 是原首一20次 $P_\tau$。所有列的准确 $C$ 整除和乘回已完成；新程序不重新执行。

## 2. 少数投影的 gcd 给全商长度的上界

对任意明确常数投影 $V_i\in\operatorname{Mat}_{816\times272}(k)$，置
$$
d_i(z)=\det(G^{(2)}(z)V_i),\qquad
g(z)=\gcd_i d_i(z),
\tag{L5}
$$
并要求至少一个 $d_i\ne0$。令 $\Delta(z)$ 是 $G^{(2)}$ 全部272阶子式的首一 gcd。$k[z]$ 为 PID，Smith 正规形给
$$
\operatorname{length}_k\operatorname{coker}G^{(2)}=\deg\Delta,
\qquad \Delta\mid g.
\tag{L6}
$$
因此，不需要计算整个 Smith/Hermite 或全部最大子式，就有
$$
\operatorname{length}_k\operatorname{coker}(C_\tau G^{(2)})
=20+\deg\Delta\le20+\deg g.
\tag{L7}
$$
等号中的20来自原 $C_\tau$ 的真实 determinant，不是额外猜定的 cusp 数值。
若全局像 $\mathcal J_{2,k}$ 还包含其他同源齐次化列，其余商只会更小，所以上界仍成立。

有限个投影未取得小 gcd 只说明本次充分检验不够；不能宣称原完整 $I_2$ 比预期大，也不能宣称剩余因子确是真实额外点。

## 3. 无穷远已经有更早一阶源的实际非零子式

原成功来源的
`R827-sigma-infinity-order-0004-certificate.json.gz`
为377881 bytes，SHA256
`25b2cb95b4fb9ad921067cf641b6bf5ba08ed8bfd36d47dba3d45d0d59b84cd3`。
实际列顺序为先导数层、再原272个正规基列。
其已成非零272阶子式的列号精确为
$$
0,1,\ldots,251;\quad272;\quad345,346,\ldots,363,
\tag{L8}
$$
实际 determinant 为 $695832206\in k^\times$。
这些列全部属于导数层0和1，因而同一个已成子式就是二阶源的无穷远满秩见证。
这只读取原列号及已有 determinant，不重新求秩或计算 minor，也不从“q4成功”抽象推断“q2成功”。

原证书还保 $P_\sigma(0)\ne0$，所以该 raw normal 子式与完整 $C$ 目标的满秩等价。补点 $t=0$ 已覆盖，(L7) 就给整个特殊纤维余商长度上界。

## 4. proper 长度夹逼：不要求余商先平坦

**定理 L.1。** 保持原 R827 的整源、原两图齐次化及同一 $\mathfrak p$-整 canonical $B$。若新的真实投影计算准确得到
$$
\deg g\le395,
\tag{L9}
$$
则
$$
\boxed{\epsilon=0,\qquad \mathcal J_{2,L}=I_2,
\qquad E_2=\mathcal C_0+D.}
\tag{L10}
$$

**证明。** 在 R827 的 proper 模型上取余商 $\mathcal Q=\mathcal O/\mathcal J_2$；也可在原有限 $\pi:Y\to\mathbf P^1$ 后，对完整正规基丛取同一个余商。由至少一个非零子式及(L8)，特殊纤维的支撑是有限集合，长度至多 $20+\deg g$。泛纤维中一个非零源截面的除子也有限。于是余商支撑 proper 且各纤维零维，故支撑到离散赋值环基底是有限态射。其推前是一个有限 DVR 模 $M$。

不需要预设 $M$ 平坦。有限 DVR 模的结构定理直接给
$$
\dim_{\operatorname{Frac}A}(M\otimes_A\operatorname{Frac}A)
\le \dim_k(M/\mathfrak p M).
\tag{L11}
$$
由(L3)、(L2)、(L7)得到
$$
415+\epsilon
\le\operatorname{length}_L(\mathcal O/\mathcal J_{2,L})
\le20+\deg g\le415.
\tag{L12}
$$
因此全部等号，$\epsilon=0$，且 $I_2/\mathcal J_{2,L}$ 长度为0。包含即相等。证毕。

这里只用真实全图多项式长度，不是单点秩或概率论。若计算给 $\deg g=396$，没有额外证据就不能从(L12)选定 $\epsilon$ 或宣布相等；该值也可能包含一个由投影选择带来的多余因子。

## 5. 首次只需一个新行列式

原 R835 已准确完成
$$
d_0(z)=\det G_0(z),\qquad \deg d_0=1320,
\tag{L13}
$$
文件 `R827-det-projection-000-exact-determinant-polynomial.json.gz`，8646 bytes，SHA256
`43b2935f834edee41c8bff17abd3e943679d636bd3855cdb9ac769ecfa2055bf`。
其原节点、次数1340上界、完整插值及代回已经认证；新消费者直接读原多项式，不重新计算1341个节点。

新增明确投影仅取
$$
V_1=\begin{pmatrix}I_{272}\\I_{272}\\I_{272}\end{pmatrix},
\qquad d_1(z)=\det(G_0+G_1+G_2).
\tag{L14}
$$
原正规基权 $\epsilon=(0,1^{144},2^{127})$，总和398；层 $r$ 的第 $c$ 列权为 $5+\epsilon_c+2r$。
所以(L14)每列最高权为 $9+\epsilon_c$。依原 determinant 次数证明，先扣全部行权398，再由原 $P_\tau$ 的真实20次整除扣20，得到
$$
\deg d_1\le\sum_c(9+\epsilon_c)-398-20=2428.
\tag{L15}
$$
准确计算节点 $0,1,\ldots,2428$ 的 determinant，共2429个，原子保存；用与已成功 R835 相同的整数节点 Newton 插值，核完整次数及全部节点代回。最后计算首一 $g=\gcd(d_0,d_1)$，并保存完整扩展 Euclid 乘回。

若(L9)成立，立即以(L10)结束；若不成立，只记录真实 gcd 及未通过充分条件，不自动增加投影。更后请求可明确增加另一个三层投影并继续 gcd，已成两个 determinant 不重算。

本任务的真正新数学只是：三个旧矩阵块相加所得投影系数、2429个有限域 determinant、完整插值、一次扩展 Euclid。旧导数列、原两个算子、原 C 整除、σ jets、原1341节点和任何 Hermite 记录均不重做。

## 6. 给短 RR 消费者的准确新边界

若(L10)实际完成，原 $I_2$ 就有一个由原 canonical $B$、完整正规基及其前两阶导数定义的真正特征零生成表达式；不再只是“某个包含于 $I_2$ 的单 B 子空间”。这些表达式可保持单位选行块的精确 adjugate/solve recipe，无需假装旧模列已经是展开的有理矩阵。

但(L10)本身不输出 $H^0(4H-E_2)$ 的547个展开坐标，也不把某张模线性核直接当成完整特征零 RR 空间。后继可从该准确全局像作低权截取/饱和、或给真正包含的短 $T'_m$；R836 仍要求准确包含及295维核或272个低权生成元的实际完整次数证书。

首次 active carrier 最小保原三层816个完整 C 列、原三个 layer index、原 C reduction、原 source audit/配置/manifest 链、(L8)原 σ∞证书、(L13)旧已成 determinant 及其成功生产者链。机器字段须分清 `actual_gcd_degree`、`source_infinity_minor_reused`、`original_J2_equals_I2` 与 `actual_short_RR_coordinates_computed=false`。

源码、参数、纸面证明与简明 run/SHA 可入Git；矩阵、节点、gcd系数、机器回执及当前源载体只在一日 active artifact 中续传。
