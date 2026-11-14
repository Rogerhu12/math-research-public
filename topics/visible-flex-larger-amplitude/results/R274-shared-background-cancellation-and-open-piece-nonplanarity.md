# R274. 公共径向背景的角差消去与有限细分后的开片非平面性

作者：ChatGPT（geometry agent）  
日期：2026-11-14  
状态：已证明（完整条件命题）。没有新的数值计算，也没有断言当前新闭面已通过 δE、reach、全局嵌入或所有 C² 接缝。

本结果说明 [R258](R258-complete-field-tail-cardinal-marker-chain.md) 的同半径四角仿射行列式证据如何用于一个**明确的共享径向位置背景**。它还说明：在已证明行列式非恒零的径向片内加入有限多个背景节点，不必重新寻找每个细分片内的非零见证。原目标 metric 的定义不随这个背景改变。

## 274.1. 精确对象与假设

设 $I=[r_-,r_+]$ 为非退化闭区间，角变量属于连通实解析圆 $\mathbb T=\mathbb R/(2\pi\mathbb Z)$。给定有限径向分割

$$
r_-=s_0<s_1<\cdots<s_N=r_+,
\qquad J_\ell=(s_{\ell-1},s_\ell).
$$

这里包含圆 collar、实际 tail 的共享径向节点，以及 outer-correction 起止位置等原构造断点。每个 $J_\ell$ 上设

$$
V:J_\ell\times\mathbb T\longrightarrow\mathbb R^3,
\qquad
h_i:J_\ell\longrightarrow\mathbb R,
\quad i=0,1,2.
$$

对每个固定 r，$V(r,\cdot)$ 实解析。三个 $T_i,U_i:\mathbb T\to\mathbb R^3$ 也是实解析角函数；它们可随原径向片改变。它们在应用中分别是完整前缀的目标 cut jets、同一非公共背景部分的原 cut jets。

令 $e_z=(0,0,1)$。给定一个**与角无关**的位置背景 $B:I\to\mathbb R$ 和三个实数 $b_i$，定义

$$
\begin{aligned}
F_{B,b}(r,\theta)
={}&V(r,\theta)+B(r)e_z\\
&+\sum_{i=0}^{2}h_i(r)
\left[T_i(\theta)-U_i(\theta)-b_i e_z\right]. \tag{274.1}
\end{aligned}
$$

在实际共享 B 的外侧 Hermite 修补中，$U_i=\partial_r^iV(c,\cdot)$、$b_i=B^{(i)}(c)$，$h_i$ 是固定宽度修补的三个 Hermite 基函数。没有修补的片上取 $h_i=0$。下面的消去恒等式甚至不需要先假设 $b_i$ 是 B 的导数；这个区别使“角差证明”与“接口 C² 证明”保持分离。

定义去公共项的辅助表达式

$$
G(r,\theta)=V(r,\theta)+
\sum_{i=0}^{2}h_i(r)\left[T_i(\theta)-U_i(\theta)\right]. \tag{274.2}
$$

对每个 $J_\ell$，假设存在四个固定角
$\theta_{\ell,0},\ldots,\theta_{\ell,3}$，使

$$
D_\ell(r)=\det\left[
G(r,\theta_{\ell,1})-G(r,\theta_{\ell,0}),\;
G(r,\theta_{\ell,2})-G(r,\theta_{\ell,0}),\;
G(r,\theta_{\ell,3})-G(r,\theta_{\ell,0})
\right] \tag{274.3}
$$

在 $J_\ell$ 实解析且不恒等于零。把三向量写成矩阵的行或列不影响非零性，只须整个证明采用同一种约定。

一个充分条件是：$V$ 在该片的 r 变量为有限次数多项式，系数是角解析函数，$h_i$ 为多项式。此时每个固定角差的各坐标是 r 的多项式，$D_\ell$ 也是实系数多项式。系数可以包含记录角 $\beta$ 的精确实 $\cos\beta,\sin\beta$；它们对 r 仍是常数，不改变该结论。结论也允许更一般的实解析径向表达式。

### 非恒零见证的准确范围

在 $J_\ell$ 内一个点有严格 $D_\ell(r_*)\ne0$，已经足以建立不恒零。若见证选在该片闭区间的端点，则要求这里使用的**同一片表达式**连续延拓到该端点；端点值非零由连续性给出邻近内点非零，所以也足够。

精确有理行列式的非零值或覆盖精确实旋转系数、并排除零的 Arb 区间可以承担这一见证。普通浮点打印值非零本身不是严格非恒零证书。本命题不把尚未完成的实际 R258 检查当作已满足假设。

## 274.2. 公共背景与 cut 公共项严格消去

**命题 274-A。** 对 (274.1) 的任意 B、任意 $b_i$、任意同一个 r 及两角 $\theta,\vartheta$，有

$$
\begin{aligned}
F_{B,b}(r,\theta)-F_{B,b}(r,\vartheta)
={}&V(r,\theta)-V(r,\vartheta)\\
&+\sum_{i=0}^{2}h_i(r)
\left[T_i(\theta)-T_i(\vartheta)
-U_i(\theta)+U_i(\vartheta)\right]\\
={}&G(r,\theta)-G(r,\vartheta). \tag{274.4}
\end{aligned}
$$

因此在 (274.3) 的四个角计算的仿射行列式，对所有 B、$b_i$ 都精确等于 $D_\ell(r)$。

**证明。** 由 (274.1)–(274.2)，

$$
F_{B,b}(r,\theta)=G(r,\theta)+
\left(B(r)-\sum_{i=0}^{2}h_i(r)b_i\right)e_z. \tag{274.5}
$$

第二项与角无关，在同一 r 的两次取值相减时逐项抵消，得到 (274.4)。仿射行列式只使用这三个同半径位置差，所以结果相同。此证明没有近似、没有小振幅展开，也没有将曲面本身的高度 mean 置零。证毕。

尤其当两个背景具有不同的 cut 值/一阶/二阶导数、并各自重形成正确 Hermite 修补时，$F_{B,b}$ 的绝对位置一般改变，但四角差证据仍完全相同。这里不能漏掉修补中 $-h_i(r)b_i e_z$ 的公共项；它们和 B 一样需要在同 r、不同角的差中一起消去。

## 274.3. 排除参数平面开片

**命题 274-B。** 在 §274.1 的每片角解析性和 $D_\ell$ 实解析非恒零假设下，(274.1) 不存在非空参数开集 $U\subset (r_-,r_+)\times\mathbb T$，使 $F_{B,b}(U)$ 包含在一个仿射平面内。

只要求 (274.1) 在相关参数点有定义；B 的径向导数不参与这一非平面性证明。如果还要求讨论一张连续或 C² 曲面，则该正则性必须由对象的其余构造另行提供。

**证明。** 假设有非空开集 U 和一个仿射平面

$$
P=\{x\in\mathbb R^3:n\cdot x=d\},\qquad n\ne0,
$$

满足 $F_{B,b}(U)\subset P$。原径向断点集合有限，故可以在 U 内选取一个非空矩形 $J'\times A$，其中 $J'$ 是某个 $J_\ell$ 的非空开子区间，A 是角圆上的非空开弧。

对每个固定 $r\in J'$，函数

$$
q_r(\theta)=n\cdot F_{B,b}(r,\theta)-d
$$

是连通角圆上的实解析函数：$V(r,\cdot)$、$T_i$、$U_i$ 实解析，B 和所有 $b_i,h_i(r)$ 在这里仅为常数。它在 A 上恒为零。实解析函数的恒等定理给出 $q_r\equiv0$ 于整个角圆。

因此在这个固定 r，(274.3) 的四个完整曲面位置都属于 P，其三个差向量都属于同一个二维向量平面 $n^\perp$。它们的行列式为零。由命题 274-A，$D_\ell(r)=0$。这对所有 $r\in J'$ 成立。

$D_\ell$ 在连通区间 $J_\ell$ 实解析，且在非空开子区间 $J'$ 恒零，所以再次由恒等定理得到 $D_\ell\equiv0$，与假设矛盾。证毕。

注意两个解析性步骤承担不同任务：角解析性把“一个角开弧在同一平面”推广到完整纬圈；径向实解析性把开区间内行列式恒零与已有非恒零证据联系起来。只凭孤立四个样点不共面、而没有这些结构，不能作同样推论。

## 274.4. 加入有限背景节点不丢失证据

**命题 274-C。** 假设某片 $J_\ell$ 的 $D_\ell$ 已满足上述非恒零条件。在该片中加入任意有限多个新径向节点，例如共享 B 的节点，得到有限个非退化开子区间。那么同一个 $D_\ell$ 在每个这样的开子区间仍不恒零。因此命题 274-B 对原分割与背景分割的共同细分仍成立。

**证明。** 若 $D_\ell$ 在任一非空开子区间恒零，实解析恒等定理立即使它在整个 $J_\ell$ 恒零，矛盾。所以每个细分片内都有非零点，虽然原程序保存的那个见证点未必落在这个细分片内。由于 B 和其 cut 公共项仍由 (274.4) 消去，这些角差函数并未因新增 B 节点更换。有限多个节点本身没有参数二维内点；任何非空参数开集仍包含落在某个非退化细分片内的开矩形，命题 274-B 的证明完整适用。证毕。

这个结论不声称原见证点在每个新子片中，也不伪造新的数值评估。它只使用原行列式的同一实解析表达式及其已经严格建立的非恒零性。若四角差本身因其他几何修改而换了表达式，则不能套用本命题；必须先核对 (274.4) 所列 V、T、U、h 确实保持。

## 274.5. 有限共享 quintic B 与全曲面 C² 的边界

若 B 的有限节点为 $b_0<\cdots<b_m$，且每个节点附有同一份实数 jet $(B_j,B'_j,B''_j)$，在每个闭节点区间用唯一五次 Hermite 多项式匹配两端这六个值，则 B 是一个明确的 C² 实函数。证明只是：每个片内是多项式，相邻片的值、一阶、二阶单侧极限在公共节点逐项等于同一记录的 jet，故能连续拼接到二阶。

这仅支付这个一维公共位置背景的 C² 定义。它不能代替下列条件：非圆 tail 部分和 collar 的真实规范形、完整 target jets 与参数换图的一致性、prefix/cut/反射/帽接缝、renderer 相对精确规范形的误差、浸入或嵌入。特别是 $b_i=B^{(i)}(c)$ 与 $U_i=\partial_r^iV(c,\cdot)$ 对完整 C² cut 拼接具有实质意义；它们虽然不影响 (274.4) 的消去恒等式，却不能因消去而在 gluing 论证中省略。

[R260](R260-scalar-jet-consistency-and-forced-metric-evolution.md) 所讨论的原 finite-Gauss scalar 真导数、返回 ap/app、原 metric 与有限角投影误差属于另外的对象一致性/误差账。本命题不把目标 metric 改为 B 的导数所诱导的 metric，也不从 B 的 C² 推出原 g 的等距误差已达标准。

## 274.6. 对称相位、反射与测试的非必要性

对活动片应用固定角平移 $\theta\mapsto\theta-\alpha$ 和一个固定正交变换 Q，四个见证角同步平移，行列式乘以 $\det Q\in\{1,-1\}$；非零性不变。故在 [R248](R248-finite-C2-phase-family-and-global-reductions.md) 所列实际相位和反射关系的假设下，同一非平面性条件可以传递到其活动相位片及下半反射片。这不表示带固定 marker 的整个曲面由一个全局刚体变换得到，也不支付其全 t reach。

四角行列式非恒零是这里采用的**充分条件**，不是开片非平面性的必要条件。公共 B 对一般曲面的平面开片性质并没有无条件的双向不变性。例如在 $r>0$ 的环带上，

$$
V(r,\theta)=(r\cos\theta,r\sin\theta,0),\qquad
B_0(r)=0,\quad B_1(r)=r^2,
$$

且无 outer correction 时，前者是平面环带，后者是抛物面环带。二者每个固定 r 的纬圈都在一个水平面内，所以所有同半径四角行列式都是零。抛物面没有平面参数开片：若 $Ax+By+C(x^2+y^2)=d$ 在一个非空平面开集成立，作为多项式的各系数必须都为零，不能定义一个仿射平面。这个例子说明不能把本命题改写为“任意 B 不改变平面开片是否存在”；准确结论是**已通过的同半径非恒零测试，对所有这些公共背景继续有效**。例子只说明测试的逻辑范围，不是本题同 g 等距族的候选。

## 274.7. 本仓当前有限对象的接线

[`geometry_20261114_shared_background_normal_form.py`](../computations/geometry_20261114_shared_background_normal_form.py) 用同一原背景表的实际节点 jets 定义共享实 B；
[`geometry_20261114_shared_background_closed_assembly.py`](../computations/geometry_20261114_shared_background_closed_assembly.py) 保原 actual tail、完整前缀、原目标 metric、mean/固定帽及已记录 SE2，并在自己的 B 上重新形成完整 cut correction。

新增 [`geometry_20261114_shared_background_planar_germ.py`](../computations/geometry_20261114_shared_background_planar_germ.py) 显式使用这个新 loader。它保原 [R258](R258-complete-field-tail-cardinal-marker-chain.md) 的 `ActualFFTNodes`、`prefix_cut_terms`、`prove_tail` 及 [R254](R254-exact-full-prefix-no-planar-germ.md) 的完整前缀证明内核，只调整新对象的绑定与只针对同一前缀的 identity-only metadata 视图。真实共享闭包的 guard 没有删除；共同材料角和所有 native Fourier 模式没有截断。

在这些精确有限定义下：

- 每个非圆径向片的实际全部 FFT 共享节点 Hermite 是有限次数多项式，outer Hermite 修补也是多项式；精确 SE2 角的 cos/sin 只作实常系数，因此 §274.1 的径向实解析结构成立。
- 有限 Fourier 角函数是实解析的；完整 prefix 的材料角换图在原全局正密度证明下是实解析局部逆，故完整角目标仍实解析。
- 共享 B 自己的有限背景节点只作命题 274-C 所允许的有限细分。
- 每一片所需的严格非恒零见证、前缀证据与 marker 代数仍必须由这份**实际新场**的 Actions 消费者产生；本结果不填写尚未运行的数值证据。

旧 R258 已有报告不能只因其 theorem 名相同就改标为新的 shared field；同一 V/T/U/h、实际 FFT 节点、同一 prefix/SE2、同一新 loader、输入 SHA 与原报告条件都要保持。新增消费者把这些来源明确列入 binding，其 `actual_delta_E_certified` 和 `all_R238_hypotheses_paid` 仍为 false。

## 274.8. 结论的准确范围

在所列解析性、有限分割及每片严格非恒零证据假设成立时，已证明的是活动参数域不存在平面开片；公共径向 B 及其 cut 公共 Hermite 项不改变该充分证据，有限背景细分不会使它失效。

本结果没有证明当前新场全部假设已实际满足，没有给出连续 metric 或曲率上界，没有证明全局单射/嵌入、reach 或真实整像幅度，也没有据此独立得出 $\delta_E>0$。[R238](R238-planar-germ-marker-rigidity.md) 的其余假设仍需同一完整对象的实际证据。没有新增六或九 jet 必须机器精度收敛的完成门。
