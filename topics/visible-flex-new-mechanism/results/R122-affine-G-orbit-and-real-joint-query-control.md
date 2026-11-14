# R122：G 的有限仿射轨道商与真实多查询支付

日期：2026-11-14。**已证明。** 纸面构造，不进行新的研究计算。使用 [R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R102](R102-finite-query-fourth-cost-control-and-cone-quotient.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R117](R117-static-weight-one-reduction-and-reciprocal-costs.md)、[R118](R118-static-G-exact-separation-and-nonzero-fourth-cost-quotient.md)、[R120](R120-G-lineality-of-the-closed-fourth-cost-cone.md) 及 [R121](R121-central-baseline-correction-and-joint-fourth-query-control.md)。

R120 是闭凸锥结论。本稿保留全部真实成本，使用先固定大缩放、再取有限 bulk 圈数、最后取有限响应复制次数的构造，实际支付一个有限仿射轨道商的多个查询。它没有以闭锥极限代替实际路径。

## 1. 有限轨道商及未知整数 s

记

$$
R=\mathcal R_8,\qquad
\mathcal A=R+
\operatorname{span}\{\mathsf P_{H,d}G:H>0,\ d\in\mathbb R\}
\subseteq\mathcal U_4,
$$

$$
r=\dim R,\qquad s=\dim(\mathcal A/R).
\tag{1}
$$

R118 给 $s\ge1$；R105 给 $r,s<\infty$。本稿不预设 $s>1$，也不把原式模板数当成这个维数。

令 $\mathsf N$ 为真实平移的生成元：

$$
\mathsf P_{1,d}=\exp(d\mathsf N).
$$

R105 的有限坐标多项式表示使 $\mathsf N$ 幂零；它在 profile 权上降一，并保 $R$。$G$ 为权一，故在商中

$$
[G],\ [\mathsf NG],\ [\mathsf N^2G],\ldots
$$

依次属于不同权。若某一项先为零，后面全为零。设第一个为零的编号是 $s$，则前面 $s$ 项均非零，因权不同而独立，且恰张成 $\mathcal A/R$。这与 (1) 中的 $s$ 一致。

纯缩放不会增加这个轨道 span：按真实仿射作用的组合规则，

$$
\mathsf P_{H,d}G
=H\,\mathsf P_{1,d/H}G.
$$

可以取任意 $s$ 个互异实数 $d_j$，例如 $0,\ldots,s-1$，令

$$
G_j=\mathsf P_{1,d_j}G,\qquad j=1,\ldots,s.
\tag{2}
$$

它们模 $R$ 独立，因为在上述链基中系数矩阵是
$(d_j^i/i!)_{0\le i<s}$，行列式是非零 Vandermonde 常数。

选择线性查询

$$
Q:\mathcal U_4\longrightarrow\mathbb R^s,\qquad Q(R)=0,
$$

使

$$
K_G=(Q(G_1)\ \cdots\ Q(G_s))
\tag{3}
$$

可逆。这里查询先定义于有限真实算子空间；随后可由 R96 表成同一合法光滑三矩圆上的有限点/模式查询的线性组合。

## 2. 原始中央族的完整商式

取 R117 的真实中央路径族：正互反对的 $h=1+t$，负互反对的 $h=1$，$|t|\le\delta<1/2$；$d=0$。每个对内部与外部都用真实零矩连接，固定首末 germ 和 frame。再串联真倒行，使整条路径 $M=T=0$。

每个 bulk 同乘正整数 $N$，连接族一开始固定。记完整成本为 $V_{N}(t)$。R109 给商中的准确恒等式

$$
[V_N(t)]=2Nq(t)+e(t),\qquad
q(t)=q_+(1+t)+q_-(1).
\tag{4}
$$

$e(t)$ 包含全部真实连接、校 frame、端口势和倒行成本。它连续；不是零，也不是任意选取的自由项。未取商的 $V_N(t)$ 仍可能有 $N^2,N^3$ 的 $R$ 历史。

沿用 R120，$\kappa=15\tau(2)/2>0$，且

$$
q_\pm(1)=\pm\kappa[G]+\sum_{w\le0}q_{\pm,w}.
$$

配平成本的真实缩放已经通过整路径变换后取 $N$ 商极限证明。因此

$$
q(t)=\kappa t[G]
+\sum_{w\le0}\bigl((1+t)^wq_{+,w}+q_{-,w}\bigr).
\tag{5}
$$

有限和中所有 $q_{\pm,w}$ 都是固定真实商向量。由于 $1+t$ 离零有统一间隙，(5) 在整个闭 $t$ 盒上连续且有界；没有对未知 $o(1)$ 求导。

## 3. 真缩放与平移，统一控制低权余项

对第 $j$ 条中央族，先作 R89 的真实缩放 $\mathsf P_H$，再作固定平移 $\mathsf P_{1,d_j}$。这些是真实路径变换，全部 profile 仍是同一个全局 $(f,g)$；不能在不同路径中重新选择独立圆。

变换后端口可能改变。用真实零矩、frame $I\to I$ 桥 $B_{H,j}$ 从共同固定 germ 接到该端口，再接其真倒行返回。它与 $t,N$ 无关，且不要求自身 $T=0$；前后第三成本准确相消。变换后的整词仍有 $M=T=0$。

将 $s$ 条路径串联，得到实际有限成本 $Y_{H,N}(z)$，其中
$z=(z_1,\ldots,z_s)\in[-\delta,\delta]^s$。对固定的 $H$，它满足

$$
\boxed{
Q(Y_{H,N}(z))
=2N\kappa H K_Gz+2NR_H(z)+E_H(z).
}
\tag{6}
$$

其中

$$
R_H(z)=
\sum_{j=1}^s\sum_{w\le0}
H^w Q\!\left(
\mathsf P_{1,d_j}
\bigl((1+z_j)^wq_{+,w}+q_{-,w}\bigr)
\right).
\tag{7}
$$

有限 $s$、有限权和、固定 $d_j$ 及 $|z_j|\le\delta$ 给

$$
\sup_{H\ge1,\ |z_j|\le\delta}\|R_H(z)\|_\infty<\infty.
\tag{8}
$$

$E_H(z)$ 是所有变换后真实连接、端口桥和固定校正的完整 $Q$ 成本。对每个固定有限 $H$，它在盒上连续有界，且不依赖外整数 $N$。**不要求它对 $H$ 统一有界。** 这正是下面必须先固定 $H$，再选择 $N$ 的原因。

路径首末 constant germs 的相容性由实际变换及真实桥支付；没有用群元重置近似 frame。空间位移自由，未在这里指定单桥终点位置。

## 4. 单独支付 s 个商查询

令

$$
A=2\kappa K_G.
$$

先取一个固定大但有限的 $H$，使 (8) 保证

$$
\sup_z\|A^{-1}(2R_H(z)/H)\|_\infty<\delta/3.
\tag{9}
$$

对任意目标 $y\in\mathbb R^s$，再选一个有限正整数 $N$，使

$$
\sup_z
\left\|A^{-1}\frac{y-E_H(z)}{NH}\right\|_\infty
<2\delta/3.
\tag{10}
$$

于是连续映射

$$
z\longmapsto
A^{-1}\left(
\frac{y-E_H(z)}{NH}
-\frac{2R_H(z)}H
\right)
\tag{11}
$$

把闭盒映到自身。Brouwer 不动点给一个真实参数 $z$，使 (6) 准确等于 $y$。

所以，$Q$ 的全部 $s$ 个目标可以用实际有限 $M=T=0$ 路径同时支付。这个结论没有选择逐点根的连续分支，也不需要 $E_H$ 的可微性。

$H$ 可一次固定，与目标无关；目标只影响整数 $N$。增大 $N$ 只重复已有完整圈，不扩大 scalar 包络。因而对该控制族选定共同物理区间后，不会因要求更大的目标而自动离开它。

## 5. 先清真实第三 prototype 的商基准

还要与全部 $R$ 查询联合，不能直接把第 4 节和 R102 两个独立满射拼起来。

从真实原响应中选择 $R$ 的一组基

$$
K_i=\mathcal B_{P_i}(\tau_i),\qquad i=1,\ldots,r.
$$

取给 $\tau_i$ 的真实零矩、frame $I\to I$ 第三路径 $L_i$，其完整第四成本为 $v_i$。第 4 节给某一条实际 $M=T=0$ 路径 $C_i$，满足

$$
Q(V_{C_i})=-Q(v_i).
$$

把它接到 $L_i$ 后，得到修改后的 prototype：

$$
M_{\widehat L_i}=0,\qquad T_{\widehat L_i}=\tau_i,\qquad
\widehat v_i=v_i+V_{C_i},\qquad Q(\widehat v_i)=0.
\tag{12}
$$

第三算子和 $K_i$ 完全不变。这只需为有限个固定目标各取一条真实路径，不要求随目标连续选根。

R101–R102 的真实复制词于是给

$$
V_{\mathrm{resp}}(t,n)
=E(t)+n\left(v_*+\sum_{i=1}^rt_iK_i\right),
\qquad v_*=2\sum_i\widehat v_i.
\tag{13}
$$

$E(t)$ 是全部真实二阶词基准，连续，独立于复制整数 $n$。由 (12)，

$$
\boxed{Q(V_{\mathrm{resp}}(t,n))=Q(E(t)).}
\tag{14}
$$

这一步准确去掉了可能妨碍联合构造的 $nQ(v_*)$，而不是把基准默认设成零。

## 6. r+s 个查询的乘积盒 Brouwer

选另一个线性查询

$$
L:\mathcal U_4\longrightarrow\mathbb R^r
$$

使

$$
K_R=(L(K_1)\ \cdots\ L(K_r))
$$

可逆。给定联合目标 $(y_L,y_Q)$。

先置

$$
t_0=-K_R^{-1}L(v_*),\qquad t=t_0+x,\quad
x\in[-1,1]^r.
\tag{15}
$$

R101 的有限细分与重复把整个固定 $t$ 盒实现为真实小族的有限词；没有要求单个原小参数族直接容纳任意大 $t_0$。

考虑实际路径成本之和

$$
V_{\mathrm{tot}}=
V_{\mathrm{resp}}(t,n)+Y_{H,N}(z).
$$

每段都是真实 $M=T=0$，所以 R83 给完整第四成本准确相加。未知数为 $(x,z)$。

沿用 (9) 先固定 $H$。固定 $t$ 盒后，$Q(E(t))$ 有界。再选有限 $N$，使

$$
z\longmapsto
A^{-1}\left(
\frac{y_Q-Q(E(t))-E_H(z)}{NH}
-\frac{2R_H(z)}H
\right)
\tag{16}
$$

对所有 $t,z$ 都落在 $[-\delta,\delta]^s$。这不依赖最后的响应复制数 $n$，因为 (14) 已准确成立。

$H,N$ 固定后，完整的 $L(Y_{H,N}(z))$ 在 $z$ 盒上连续有界。这里允许它很大，也允许它含 $N^2,N^3$ 的历史；没有在未取商的查询中删除它们。

最后选择有限整数 $n$，使

$$
x\longmapsto K_R^{-1}
\frac{y_L-L(E(t))-L(Y_{H,N}(z))}{n}
\tag{17}
$$

对所有 $x,z$ 都落在 $[-1,1]^r$。式 (16)、(17) 合成一个连续乘积盒自映射。Brouwer 给共同不动点，从而

$$
\boxed{
L(V_{\mathrm{tot}})=y_L,\qquad
Q(V_{\mathrm{tot}})=y_Q.
}
\tag{18}
$$

选择顺序明确为：

1. 有限真实基与固定 $z$ 盒；
2. 固定有限大 $H$，压低统一低权余项；
3. 为有限 prototype 做固定基准修正，并确定 $t$ 盒；
4. 固定有限 $N$，处理商查询的真实连接基准；
5. 最后固定有限 $n$，处理包括 $N^2,N^3$ 在内的其余查询。

没有循环依赖，也没有以一个闭锥成员来代替实际有限词。

## 7. 共同物理区间、同一 profile 与整函数充分门

所有小族、固定缩放和平移、端口桥及 prototype 基准修复只涉及有限多个紧 scalar 控制族。整数 $N,n$ 的变化只重复它们已有的完整圈或词。可以在这些控制族之后固定共同物理区间，再用 R96/R105 的忠实表示把 $L,Q$ 转成同一合法非退化 $C^\infty$ 三矩圆上的有限实查询。

如果需要对所有目标保同一圆，可以先固定上述族及 $H$；目标只改变整数重复次数。prototype 修复是预先固定的有限工作，$t$ 盒也不随联合目标变化。随后所选公共区间与圆不因 $N,n$ 增大而改变。这里没有任意预给窄区间、统一长度上界或导数盒保证。

(18) 支付 $r+s$ 个独立查询。其他 $\mathcal U_4/\mathcal A$ 分量可以同时改变，不能认为它们也为零。

有一个准确的进一步充分门：

$$
\boxed{\mathcal U_4=\mathcal A
\ \Longrightarrow\
\text{任意完整 canonical 第四成本目标均可由实际有限 }M=T=0\text{ 词实现}.}
\tag{19}
$$

因为这时 $r+s=\dim\mathcal U_4$，可使 $(L,Q)$ 为整个真实函数空间的坐标映射；(18) 的查询一致就等于整个函数身份。当前没有证明 (19) 的前提。即使前提以后成立，第四 ruling、低阶双 collar 与更高阶仍须另付。

## 8. 最小的下一原式门

不必盲算整个仿射轨道。由第 1 节，

$$
\mathsf NG\in R\quad\Longrightarrow\quad s=1.
\tag{20}
$$

因此最小新目标是原式 $\mathsf NG$ 的权零成员门。若有准确原式关系，轨道商在第一步即终止；若有真实原式分离子式，则 $s\ge2$。后续依次检验 $\mathsf N^jG$，一旦出现真成员就停止，因为 $R$ 平移不变。

每步目标与完整响应均使用原表达式、同一右锚、同一 profile。先以原式验过的响应依赖给上界，再用有理 Volterra 原评价达到该上界并取增广非零子式，才可报非成员。模小秩或不完备 word 余项都不够。不同权下的非零商链自动独立，所以无须对已证明的前块重复联合拟合。

本稿没有计算 $s$，没有宣称新增第二个轨道方向；它提供了有限真实构造及一个可以只消费现有 DAG 的具体最小接口。
