# R422　当前准确 C 闭场的完整点对集合与 reach 绑定

2026-11-15，geometry，OpenAI / ChatGPT，AI 作者。

**状态：条件来源适配与已有几何定理的完整应用说明。** 独立源码把 R416 的准确活动场、R417 的两帽及 R413 的原 cuff 绑定到 R279、R241、R280–R282 的既有连续几何门。没有实际 accepted450 输入，没有运行本消费者，也没有选取或预填 $K$、$\tau$、$D$ 或数值证书。源码不改 R418、R409、193、任何 BVP/FD/验收门，也不增加前置 fixture 或独立审核门。

源码为 [geometry_20261115_current_C_ten_complete_reach_cover.py](../computations/geometry_20261115_current_C_ten_complete_reach_cover.py)。完整执行接口单独列出输入、源 pins、CLI、输出及未付范围；本文不以阶段完成代替课题完成。

## 422.1　审读后的真实断口

原 [R241](R241-immersion-cover-embedding-and-normal-cones.md) 已证明从闭正则浸入的完整点对覆盖同时得到嵌入和 reach，不能因换到当前场而重复制造一套判据。原 [R248](R248-finite-C2-phase-family-and-global-reductions.md) 已支付正确的相位族与哪些几何量可约到一个相位。原 [R279](R279-finite-field-direct-continuous-curvature-certificate.md)、[R280](R280-joint-endpoint-all-phase-normal-balls-and-finite-cover.md)、[R281](R281-exact-rational-phase-disjunction-and-finite-cover.md)、[R282](R282-local-cross-Gram-cuff-charts-and-complete-phase-responsibility.md) 分别提供直接六 jet 曲率、法向球联合门、完整 RP1 相位覆盖和真实 cuff 局部责任。

实际源码分工如下。

| 既有源与函数 | 已有作用 | 不能直接重标为当前结果的部分 |
|---|---|---|
| 675 `certify_cell`、`cell_specs` | 完整闭活动块的位置球、单位法向球、R279 与两反射片格点集合 | 原 CLI 的 ac635/e70d 场加载器；本次不调用它 |
| R417 `CurrentTenFixedCaps.cell` | 当前全部 marker 的 Cartesian 图六 jet、球、曲率与闭盘交 | 不能用旧 a3 binder 的 marker/schema 代替当前完整绑定 |
| 0b52 `CuffOwner` | 同一 collar 完整系数、共同材料角及逐叶局部 membership | 其常数通过不支付整 rank；其参数不能换成旧场 |
| 4e31 `CompleteCombiner` | 完整 active×cap 的空间×两 RP1 责任 | 结果明确未付 active–active、cap–cap 和全局曲率；其旧绑定不是 R416 |
| b1c2 `ImageBounds` | 已覆盖位置域的整个 $F_0$ 直径上界，及可选全相位共同上界 | 其旧完整入口锁定旧 cover、旧 $K,\tau$ 和 schema；其位置盒本身不证明 reach |
| 原 v3/fc5 静态/R24 路径 | 旧具体场、原完整点对算法和给定连续误差包络下的条件覆盖 | 旧数值中心、旧 renderer、旧目标和旧包络不属于新 R416 场 |

原 v3 的 `worst` 长度上限只是显示见证的截断；不能拿它作新 pair universe。原失败 prefix 的少量 children 也不是当前所有 piece、两反射片和两帽的完整覆盖。R422 因此保留旧源与旧结果不动，独立枚举当前场的完整集合，而不是替换字符串后沿用旧通过标志。

原 static-base 加 [R24](R24-weak-markers-with-explicit-reach-margin.md) 的路线仍可使用。它需要真正同场的未标记 reach、全 marker-support 至整面补集的距离及原幅度/梯度/Hessian 余量；R422 未把这些条件设为已付，也不从某个 marker 的盘内边界余量推得全局 $d_0$。

## 422.2　唯一被比较的准确场

输入沿以下已经发表的具体构造到达。

1. R400 原真实连续十族、全部十参数冻结及真正完整450来源。
2. [R409](R409-current-continuous-ten450-full-radial-shared-background-and-seam-construction.md) 的完整径向数据、准确节点定义、同一 shared $B$、全部 mean/FFT/Nyquist、两反射片及完整帽列表。
3. [R416](R416-current-C-cut-atlas-compatibility-and-accurate-geometric-patch.md) 的**独立准确 cut patch**及其同一 C/DAG 实系数。旧 seven-tuple 中的数值 `A` 只保来源，不被当作这个新 patch 的 renderer。
4. R413 原 dyadic $r_{\rm cuff}$、同原 C 的 cuff target atlas，及 R417 实际两张完整 Cartesian 图帽。

R416/R417/R413 的 binding 重新核同一原输入、完整 marker 列表、side、高度 datum、cuff 和来源 SHA。原 root 选择族、原连续 C 和当前十参数均不由本消费者改变；没有借用旧有限 Gauss 目标、旧尾 J/graph 或 $1+B'^2$。

若准确模型仍含原允许的 C root 族，则以下每个区间均包围该**同一个已声明族**的所有允许成员。结论是每个同成员匹配的 $(g_\xi,F_{\alpha,\xi})$ 的统一充分条件。把两端区间独立相乘只可能扩大包围，不能把一个成员的几何与另一个成员的目标重新定义成新的对象。

675 的活动六 jet 在 prefix、原 native 径向片、collar、准确 cut patch 及其反射片上直接调用 R416 `field.evaluate`。它们是准确 Hermite/有限 Fourier/shared-$B$/材料角复合表达式的真实导数，不是浮点 renderer 的 jet 标签。R417 的帽则准确为

$$
F_{\mathrm{side}}(x,y)=
\bigl(x,y,\mathrm{side}(H+b_{\mathrm{side}}(x,y))\bigr),
\qquad \mathrm{side}\in\{-1,1\}.
\tag{422.1}
$$

每个 $b_{\rm side}$ 是原该侧全部 compact bump 的和，允许重叠及负振幅。下帽不是 $-H+b$。同一准确 cuff 与支持严格在盘内的既有约束保证固定帽在 cuff 附近的原平环带；本消费者不重新挑 cuff。

## 422.3　抽象闭面、接缝与全相位

抽象材料域由两张活动半环带在中央圆上粘合，外侧分别与两闭盘在原 cuff 圆上粘合。按原周期角识别 $q=0$ 和 $q=1$；同一接缝两种坐标以及同一帽 Cartesian 点按原商关系识别。所得紧、连通、无边界抽象面可取 $S^2$。这条拓扑陈述不预先给出浸入或嵌入。

R409 的准确共享节点/反射和 R416 的准确 cut 过渡支付结构性两 jet 相合；R413/R417 支付真实原 cuff 与帽的共同图。这里使用的是这些源的准确定义和已证接缝条件，不能用一个小的浮点 gap 代替恒等，也不能把 R409 的旧数值 $v,b$ 放回 R416 的准确过渡系数。

在所有活动块，令物理角 $\phi=2\pi q$，材料角为

$$
\Theta=\Phi(\phi),\qquad \Phi'>0,
\tag{422.2}
$$

其中完整原系数和实际正下界均由当前 loader 保留。全族按原真实定义

$$
F_\alpha(u,\Theta)=R_\alpha F_0(u,\Theta-\alpha)
\tag{422.3}
$$

作用于活动片，两帽保持固定。所有接缝的等式对完整材料圆成立，因此这仍是紧致材料面上的联合连续到二阶的族，并给 $\alpha\mapsto F_\alpha$ 的强 $C^2$ 连续。原课题 $\alpha=\pi t/2$、$t\in[0,1]$ 包含在本组件使用的完整相位圆中。

**块如何随相位运输。** 一个 phase-zero 活动块在材料角中的集合记为 $C$；在相位 $\alpha$ 使用逆参数作用对应的材料块 $\psi_\alpha C$，于是它的像正是 $R_\alpha F_0(C)$。每相位这些运输块仍覆盖全部活动片。两活动块的全部位置、法向、路径因而共同刚转；两帽块共同固定；只有活动块与固定帽的组合出现相对旋转。这不是假设物理 $q$ 做等量平移，也不是把旧静态 pair 的一端任意旋转。

## 422.4　完整闭块与点对集合

对 R416 原 `field.pieces` 每一片、两张反射 sheet，以及 $[0,1]$ 的完整物理 $q$ 圆，使用原 675 `cell_specs` 的闭有理格。设每轴初分为 $d=2^h$，piece 数为 $P$，则活动 root 数

$$
N_A=2Pd^2.
\tag{422.4}
$$

两帽各先作为一个完整闭 disk root；其含原始方形的四叉子盒实际域始终是“闭矩形与原闭盘的交”。只在矩形至原点的最小距离平方**严格大于** $r_{\rm cuff}^2$ 时省略该空交。切触盘边、坐标轴、四叉公共边和 seam 均保留。

点对 universe 是以下三个不相交的来源类别，组内参数块仍可重叠：

$$
\begin{array}{c|c|c}
\text{类别}&\text{完整 root pair}&\text{相位责任}\\
AA&0\le i\le j<N_A&\text{共同旋转，静态门有效}\\
CC&\text{上/上、上/下、下/下}&\text{两帽固定}\\
AC&0\le i<N_A,\quad c\in\{+,-\}&\text{全部相对相位}
\end{array}
\tag{422.5}
$$

总数为

$$N_{\rm pair}=N_A(N_A+1)/2+3+2N_A.\tag{422.6}$$

同块 pair 和两反射片之间的所有 pair 都在其中。对角线不是删掉的索引集：门必须对块内所有**不同抽象材料点**成立；相同材料点只由既定商关系识别。角边界 $q=0=1$、中央反射圆、cut、native/B 分段节点及两个 cuff 的重复表示不会变成漏检的开放带。

## 422.5　从同场完整一 jet 得到真实短路径

本节只落实 R241 已允许的“实际路径长度上界”输入，不假定 R418 的小 metric 误差已经成立。

### 422.5.1　整个原 piece 的导数包围

对每一原活动 piece 的全部闭参数域及两 sheet，完整曲率 DFS 的所有 terminal leaf 同时保留原六 jet。设经完整并集得到

$$
\|\partial_uF_0\|\le U_i,\qquad
\|\partial_qF_0\|\le V_i,
\tag{422.7}
$$

其中 prefix 的 $u$ 是其实际 $s_{\rm num}$，径向片的 $u$ 是实际 $r$。若一个导数分量的区间为 $[a_j,b_j]$，使用

$$
\sqrt{\sum_j\max(|a_j|,|b_j|)^2}
\tag{422.8}
$$

的有理向上根界。对完整 leaf 并集取最大值即得 (422.7)。没有完成全部原 piece/角/两 sheet 时，不将已见的最大值声称为全局界。

### 422.5.2　径向拼接不是把两个坐标等同

从中央圆向上 cuff 的实际顺序为：prefix 的 $s$ 递增，再从 $r=R_{\rm cut}$ 沿全部径向片递减至原 cuff。源码逐原闭端点核连续有序，不能跳过 patch、collar、某个 native/B 子片。

在这一链上定义一个单调的**路径长度上界坐标** $S$：每 piece 的增量是 $U_i$ 乘该 piece 的真实坐标长度；反向的径向片用 $r_{i,+}-r$。加上的常数偏移在每个 seam 接齐。下 sheet 取负号，因此两 sheet 中央 seam 都对应 $S=0$。$S$ 不是 target 的弧长坐标，不改 $g$，也没有断言 prefix 的 $ds$ 等于 tail 的 $dr$。

共同 $q$ 穿每个 seam 表示同一个实际点，是原 R400/R409/R416 的完整物理 $\phi$、同一 $\Phi$ 和记录的同一 SE2 的来源责任。R416 的准确 radial chart 在 cut 有其自身真实过渡；沿固定 $q$ 的分段路径只在公共端点拼接，长度分别按各侧 (422.7) 计。若实际 q 标记不相同，就必须采用真正过渡映射及相应导数界；本源码不接受换标签的旧 renderer 来省略它。

### 422.5.3　AA 的闭块路径界

令 $V=\max_iV_i$。任意两活动点先在第一点的径向层沿最短物理 $q$ 圆弧走，再沿同一个 $q$ 的真实径向链走到第二点，得到

$$
d_M(x,y)\le |S(x)-S(y)|+V\,d_{\mathbb R/\mathbb Z}(q_x,q_y).
\tag{422.9}
$$

这个选择不要求径向链是测地线。对两个完整闭块，分别取右侧两项的上界。圆差上界在完整差区间上准确检查两端与 $\pm1/2$，因此相邻的 $q=0$、$q=1$ 小块不会被误当成相距一整周。该计算也不假定实际角速度单调。

按 (422.3) 运输上述整条材料路径后，其像只是原路径的共同刚转，故长度界对所有相位保持。这里需要材料逆作用；不能以 $q\mapsto q+\alpha/(2\pi)$ 代替一般非线性 $\Phi$ 的逆。

在全闭场曲率界 $K$ 已付的条件下，源码仅当

$$K L_{ij}<\pi_-<\pi\tag{422.10}$$

时使用 R241 短路径门；$\pi_-$ 来自实际有理向外包围的下端。原严格 $\pi/K$ 边界没有改成非严格。若全曲率未付或原 piece 的一 jet 并集未完成，该门保持未付，不能用已有小部分界推过去。

### 422.5.4　同帽路径与同图引理

同一闭帽 disk 是凸的。若全部该侧 marker 给出 $\|Db\|\le G$，两参数点的直线段在 disk 内，其图像长不超过

$$\sqrt{1+G^2}\,|(x_2,y_2)-(x_1,y_1)|.\tag{422.11}$$

对两闭盒与 disk 的交，取整盒间距离上界仍合法，即便盒中心在 disk 外。该界也只在同一帽使用，不把两帽之间的空间直线当曲面路径。

还有更薄的既有 [R24 §3](R24-weak-markers-with-explicit-reach-margin.md) 同图引理。若

$$H_b\ge\|D^2b\|_{\rm op,\infty},\qquad H_b\tau\le1,\tag{422.12}$$

则对同帽图中任意点对直接有

$$2|n_x\cdot(F(y)-F(x))|\le H_b|y-x|^2\le |F(y)-F(x)|^2/\tau.\tag{422.13}$$

图的水平两坐标是恒等，故不同 Cartesian 参数点不可能有零弦。源码使用全部同侧支持的保守和

$$
G=\sum_i\frac{8|A_i|}{R_i},\qquad
H_b=\sum_i\frac{8|A_i|}{R_i^2}.
\tag{422.14}
$$

负振幅和重叠均按完整和处理；不假设原特殊四-marker 布局。两侧图的法向符号不改变 (422.13)。这只是 R24 已证同图引理，不代表未标记基面的 reach、跨支持全局 $d_0$ 或 R24 弱标记转移不等式已付。

## 422.6　曲率、法向球与原四个 OR 门

对活动域，675 在同一完整六 jet 上计算

$$X=F_u,\quad Y=F_q,\quad N=X\times Y,\quad\Delta=|N|^2.$$

只有闭块 $\Delta_->0$ 时才给原完整单位法向归一化球。请求的 $K>0$ 采用原 R279 的两个严格标量下界，而非离散主曲率样本。对 R417 帽，使用其原真实 graph Hessian 上界与 $Q=I+Db\otimes Db\succeq I$ 的主曲率界；$K$ 边界保原非严格比较。角度、radius 或参数块细分不改变准确场、目标或 root 族。

在位置球 $B(c_i,e_i)$、$B(c_j,e_j)$ 和单位法向球 $B(\nu_i,\eta_i)$、$B(\nu_j,\eta_j)$ 上，令

$$d_0=c_j-c_i,\quad e=e_i+e_j,\quad D_+\ge|d_0|.$$

静态门保留以下 OR：

$$
|d_0|^2\ge(2\tau+e)^2;\qquad
|d_0\times\nu_i|^2>(e+D_+\eta_i)^2;\qquad
|d_0\times\nu_j|^2>(e+D_+\eta_j)^2;
\tag{422.15}
$$

以及原 R280 的联合条件

$$
|d_0\times\nu_i|^2+|d_0\times\nu_j|^2>
(e+D_+\eta_i)^2+(e+D_+\eta_j)^2.
\tag{422.16}
$$

位置门可非严格，切向和 joint 门必须严格。法向中心不要求单位长；实际单位法向才用于误差推导

$$|d\times n-d_0\times\nu|\le e+D_+\eta.$$

因此每个切向门均排除零弦及非零双法向；联合门若通过，至少一个端点的切向投影非零。没有把 joint 单独替换原两个单端门。AA 因共同旋转保这些值，CC 因固定保这些值。

AC 首先可用原 R37 整圆距离下界。其余情况逐字调用 R280 `evaluate_joint` 和 R281 `catalog_for/strict_interval`：

$$t=\tan(\alpha/2)\in[-1,1],\qquad u=\cot(\alpha/2)\in[-1,1].\tag{422.17}$$

两张闭图覆盖整个 RP1；第二图保持原四次齐次系数倒序，包含 $u=0$ 的 $\alpha=\pi$。每闭相位区间用原 Sturm 链检查严格正，而不是相位端点采样。距离、移动端、固定端、joint 四门仍为 OR。原可一次付完整圆周的非严格距离替代项也保留。

如果当前包围未能给出单位法向球，本次不伪造法向或把一个中心向量规范化后当实际场；位置距离门仍可使用，未付部分继续空间/相位细分或明确停在未付。

## 422.7　真正 cuff 近对角线的逐叶责任

AC 的某个闭乘积可能包含相同 cuff 材料点，严格距离和严格切向球门不可能支付这些零弦。因此原 R282 owner 保持独立优先尝试，其输入是**当前 field** 的完整 collar Fourier/mean/Nyquist 系数、当前 shared $B$、实际 $\rho_-$ 与当前全部帽 marker。

R416 只改变靠近 cut 的准确 patch，不改变 collar。原 owner 的窄图宽度满足 $\delta\le(r_{\rm inner}-r_{\rm cuff})/4$，实际支撑位于同一 marker-free cuff 环带，故其既有系数推导可直接复用。

每一被支付叶都必须同时满足：同一 side、整个 active 闭径向区间在局部 collar 内、整个 cap 盒与闭 disk 的交在局部环带内、两个完整角域在同一严格扇区内，以及原正 cross-Gram 常数。移动端使用真正的

$$\Theta=\Phi(2\pi q)+\alpha,$$

通过两 RP1 图对完整相位区间包围。它不是取变形后 XY 方向，也不把物理 $q$ 当材料角。

正 cross-Gram 的积分论证同时支付图内不同材料点的非零弦和非零端点切向投影。相同材料点只按原 cuff 商关系识别。某一 rank 有局部 cuff 零弦，不代表整个 rank 或整个相位圆由该门支付；其余空间/相位叶仍由原 R281 门承担。完整闭边界由两个闭子域共享，未删除 tangent、角 seam 或精确等号点。

## 422.8　完整条件结论的合法顺序

固定同一个允许的准确 C 成员。假设未来真实输入经原 guard 到达本组件，并实际取得：

1. 当前源定义的完整闭 $C^2$ 场；其结构接缝与同一材料图按 R409/R416/R413/R417 保持。
2. 全部闭活动块和两帽的正则性及完整曲率 $|\kappa|\le K$，没有未付叶。
3. (422.5) 的全部 root pair、每个闭空间细分及 AC 两 RP1 根都由上述原门支付，没有未访后缀。
4. 原非严格 $K\tau\le1$。

先证明单射：距离、切向及 joint 门排除零弦；R241 短路径门对不同材料点给正弦弦下界；同一帽图由水平坐标恒等排除自交；R282 局部图同样排除零弦。同一抽象材料点的多坐标表示不进入“不同点”反例。因此完整紧正则浸入为嵌入。

此后才应用 [R37](R37-double-normal-bottleneck-and-distance-cover.md)：若 reach 小于 $\tau\le1/K$，存在短于 $2\tau$ 的非零双法向瓶颈。短路径门由原 $\pi/K$ 论证排除它；空间距离门、切向/joint 门、R282 门均排除它；同图 (422.13) 也排除它。故

$$\operatorname{reach}(F_\alpha(M))\ge\tau\quad\text{对全部实际相位成立}.\tag{422.18}$$

R37 所用 Fenchel 总曲率下界已有原证明处理分段曲线和角点。这里核阅了原论文的 Satz I，而未增加新的 reach 外部假设：W. Fenchel，*Über Krümmung und Windung geschlossener Raumkurven*，Math. Ann. 101 (1929), 238–252，[DOI](https://doi.org/10.1007/BF01454836)，[Göttingen 原始数字化全文](https://gdz.sub.uni-goettingen.de/download/pdf/PPN271020091/PPN271020091.pdf)。本文不复制原论文，也不重证已经支付的 R37/R241。

这个结论对上述同 root 族包围所涵盖的每个成员一致成立；不把区间盒中任意拼装的中点向量声称为真实成员。

## 422.9　完整 $D$ 与比例的范围

原 b1c2 `ImageBounds` 只接收当前完整六 jet/帽图产生的位置球和 Cartesian 盒。所有原闭域完成后，才允许给整个标记 $F_0(M)$ 的 $D_+$。若仍有缺叶，显示的只是已覆盖子域的界，完整 $D_+$ 为空。

定义始终为

$$D=\operatorname{diam}F_0(M),\tag{422.19}$$

包含两帽和全部活动片。共同旋转轴圆柱或球给出的全相位上界可以作为 $D$ 的保守上界，不能改变这个定义。三维位置盒不会支付浸入、嵌入或 reach；(422.18) 必须由完整点对和曲率另外得到。

仅当已经得到 (422.18) 且真实输入的固定 $\tau$ 满足 $\tau\ge(3/100)D_+$ 时，本组件才报告该 reach 比例的充分条件已付。它不重新选择 $\tau$ 或 $K$，也不把某个 core 的直径或材料点位移当完整 $D$。

## 422.10　完整未付范围与执行边界

所有数值执行仍只允许本库公开 Actions。源码编写、原源/论文阅读和本文纸面推导不产生实际输出；未运行 fixture、未选未来场或参数。

曲率 DFS 与 pair DFS 均在资源检查前保留当前 stack 顶，不先 pop。只有完整 terminal 或 split 记录写入后才退休该节点；发生已捕获停止时保当前未退休闭 frontier、兄弟节点和原 root/rank 后缀。最大深度用尽的所有未付 terminal 地址仍完整留在临时账本中。`max_pairs` 是资源范围，不是小样本 universe。

全 root 枚举、全叶曲率通过、全 pair 通过、$K\tau$ 与比例是不同字段。某个下界不正或预算结束不是几何失败。当前 source 也不承诺有限预算一定终止；固定的准确模型族区间宽度、图宽、曲率或分离余量不足，都可能留下未付，不能靠增加工作预算虚构严格余量。

临时账本保全部实际闭域、原门记录、来源和字节身份；对外只返单份不超过 90000 B 的必要摘要。账本 SHA/行数不等于本地逐数值复核。源码不自动清理未读输出，不上传 raw，不把大数据分包或编码回传。

即使将来此 reach 组件全部通过，下列责任仍独立存在：原完整非线性与物理门；准确场相对原同一 $g$ 的全域 metric；固定有内点握持域及其直径；整像 held/Hausdorff 下界；包括反射的 Euclidean 非全等间隙；原 RK 轨迹、数值影子与新准确场的误差比较；同一目标的后续精化及课题其余标准。R422 不在子组件完成处结束任务。
