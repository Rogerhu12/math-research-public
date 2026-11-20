# R676：固定同一度量的符号网格／频率精化与完整观察迁移

2026-11-20，Astra-larger-resume-24b2ab87-20261120 / recover_evidence。

**状态：已证明的转移定理与可执行入口；尚无本条新的 Actions 数值应用。** 本条建立原 fullclosed 或 R671 固定解析尾模型的嵌套空间、准确符号二分、全部旧观察与永久几何位置的迁移，并把实际 binary64 新三 jet 与理想准确限制分开。给出的两个小源码已作静态阅读、AST 解析及依赖文件 SHA 检查；没有在本地执行新场求值、标量计算、求解或数值 fixture。

它解决题 README 第 5 项所需的“保持同一 $g$ 的精化入口”。**转移、重新读数、启动一次 finer solve 都不等于已经证明或数值显示误差持续趋零。** 本条不宣布误差达到 $10^{-6}$，不继承原候选的嵌入、reach 或标记证书，也不替代 R657/R674 等连续度量消费者。

## 1. 固定的数学对象与已付工具

保留原 FullHold 的全部参数、准确终点 $S$、准确帽半径 $R$、函数 $a(s)>0$、材料度量

$$
g=ds^2+a(s)^2d\theta^2,\qquad 0\le s\le S,
\tag{676.1}
$$

以及原相位范围和固定帽。原上半场以材料角变换 $\theta=\Theta_c(\phi)$ 表示。记 $\rho_c=\Theta_c'$；core 系数 $c$、高度 $H$ 仍是原来允许的自由量，固定的前三个 core 系数不改变。精化转移本身保持所有现有 core 系数和 $H$，新增 core 频率补零，故此时 $\Theta_c,\rho_c$ 都准确不变。

径向节点的数学定义始终是

$$
s_i=\alpha_iS+\beta_i,\qquad \alpha_i,\beta_i\in\mathbb Q,
\quad h_i=s_{i+1}-s_i>0.
\tag{676.2}
$$

节点间 $q$ 是共享二阶 jet 的 quintic；其系数列顺序为

$$
(R_0,\ldots,R_M;\ T_1,\ldots,T_M;\ Z_0,\ldots,Z_M).
\tag{676.3}
$$

物理角表达为 $R_j\cos(2j\phi)e_r(\phi)$、$T_j\sin(2j\phi)e_\theta(\phi)$、$Z_j\cos(2j\phi)e_z$ 的和。完整场为原模型

$$
F=q+\chi(s)(R+S-s)e_r(\Theta_c(\phi))+\chi(s)H e_z,
\tag{676.4}
$$

或 R671 的固定模型

$$
F=q+f_\lambda(s)e_r(\Theta_c(\phi))+
\{h_\lambda(s)H+k_\lambda(s)\}e_z.
\tag{676.5}
$$

后一情形把 $\lambda$ 及 $\eta$ 的两个**符号物理端点**固定。精化不会改变 $\lambda$，不会改变 $\eta$ 的物理位置，也不会把 $a$ 或 $g$ 作重参数化。新的整数节点索引仅是同一位置在新数组中的地址。

本条直接使用以下已证结论，不重新登记它们：

- [R655](R655-node-midpoint-blind-space-and-Gauss-control.md) 的完整观察、Hermite 三 jet 与 Gauss 控制；六点不能冒充完整连续相对 Gram 证书。
- [R653](R653-exact-quarter-angle-closed-Gram-reduction.md) 的准确角重数约化。
- [R656](R656-fullclosed-continuous-geometry-with-complete-analytic-lift.md) 所采用的准确自由系数／派生端口重建、Hermite–Bernstein 公式与 f512 向外算术；本条仅调用其径向公式，不重复旧曲率扫描。
- [R660](R660-positive-spectral-Gram-blocks-and-maximum-control.md) 的正谱目标、同一 $p,\epsilon,c$ 及全残差行接口。
- [R671](R671-exact-reference-tail-affine-lift.md) 的完整 $f_\lambda,h_\lambda,k_\lambda$ 和仿射自由空间。
- [R248](R248-finite-C2-phase-family-and-global-reductions.md) 的共同材料面、固定帽与全相位归约。径向／频率精化不改变这套族的参数定义；本条没有另行给出新的时间离散收敛结论。

## 2. 准确限制给出嵌套的完整 quintic 空间

### 定理 676-A：径向二分及频率补零

对每个旧胞插入准确节点

$$
s_{i+1/2}=\frac{s_i+s_{i+1}}2
=\frac{\alpha_i+\alpha_{i+1}}2S+
\frac{\beta_i+\beta_{i+1}}2.
\tag{676.6}
$$

在旧节点保留原三 jet，在新节点取**原 quintic 的准确值、一阶、二阶导数**。用这些三 jet 在两半胞重新作 quintic 插值，得到的函数逐点准确等于原 $q$。全部原节点、core／帽端口、$C^2$ 接缝以及完整自由坐标条件保持。

若另取 $M'\ge M$，把 (676.3) 的每个旧频道复制到新对应频道，新增模式设为零，则 $q,\Theta_c,\rho_c$ 以及未截断的解析 lift 均逐点不变。因而理想的径向／频率转移在同一材料面、同一 $g$ 上准确保持完整场；它不是一次新的拟合。

**证明。** 旧胞上的 $q$ 限制到任一子胞仍是次数至多五的多项式，其两端值及前两阶导数就是指定的新三 jet。两个满足相同六个条件的五次多项式之差，在两个不同端点各有三重零点；若不恒零，次数至少六，矛盾。因此限制与重新插值相等。相邻胞在旧节点保留共同的三 jet，在新中点也取同一个原多项式的三 jet，所以仍为 $C^2$。

core 和终端没有插入替代端点。所有端口自由或派生量照原公式保留，特别是 core 的派生 $T_j=-2jc_j$ 按准确实数关系解释，不能以两个分别舍入后的槽差替代。频率补零后，各有限三角和的旧项完全相同，新项全为零。core 的有限 $\Theta_c-\phi$、$\rho_c-1$ 同理；因此 $e_r(\Theta_c)$ 是同一个完整函数。两类 lift 的所有径向函数和 $H$ 保持，得到完整场恒等。证毕。

### 准确中点公式

对任一系数列，令旧胞端点三 jet 为 $(Y_0,U_0,A_0)$、$(Y_1,U_1,A_1)$，胞宽为真实 $h>0$。则

$$
\begin{aligned}
Y_m&=\frac{Y_0+Y_1}{2}
 +\frac{5h}{32}(U_0-U_1)
 +\frac{h^2}{64}(A_0+A_1),\\
U_m&=\frac{15}{8h}(Y_1-Y_0)
 -\frac7{16}(U_0+U_1)
 +\frac h{32}(A_1-A_0),\\
A_m&=\frac3{2h}(U_1-U_0)-\frac14(A_0+A_1).
\end{aligned}
\tag{676.7}
$$

这些式子可由原六个 Hermite 基在 $u=1/2$ 的值及前两阶导数直接得到；也可把第 3 节的六个 Bernstein 控制值代入二分公式。它们与原算子的字面 node/midpoint 权一致，特别注意 $U_m$ 的末项是 $A_1-A_0$。

源码实现的列迁移是

$$
\begin{aligned}
[0,M+1)&\longrightarrow[0,M+1),\\
[M+1,2M+1)&\longrightarrow[M'+1,M'+M+1),\\
[2M+1,3M+2)&\longrightarrow[2M'+1,2M'+M+2).
\end{aligned}
\tag{676.8}
$$

其余列补零；旧节点索引 $i$ 在二分后为 $2i$。这避免把旧 $T/Z$ 频道按新 $M'$ 错位读取。

## 3. 理想限制与实际 binary64 新场之间的严格差界

$S$ 是原 FullHold 定义的真实数，通常不能当成有理数。即使全部旧自由 jet 为准确 binary64 数，(676.7) 中含真实 $h$，新的准确三 jet 也不必可由 binary64 表示。因此本条不把“准确限制存在”偷换成“写入双精度数组后逐字同场”。

源码从原节点报告读取已经包围真实 $S,R$ 的准确有理端点，转成向外二进制区间；通过 (676.2) 计算胞宽区间并要求其下端严格正。旧自由系数是其 literal binary 值的准确点区间；core 派生 $T$ 先按 $-2jc_j$ 向外重建。所有 (676.7) 的运算均调用 f512 向外算术。

令得到的新理想三 jet 包围为 $J_m\in[J_m^-,J_m^+]$。保存一个有限的 binary64 中心载体 $\widehat J_m$，同时保存

$$
\widehat J_m-J_m\in
\operatorname{outward}\bigl(\widehat J_m-[J_m^-,J_m^+]\bigr).
\tag{676.9}
$$

旧节点的准确数学 jet 没有改变，故其差明确为零。若一个频道两端完整三 jet 全为零，其旧多项式恒零，新增该频道也准确置零，不让零恒等式被无意义的向外宽度污染。纯频率／角网格精化不插新节点，因而本项差准确为零。

这里的差场是“实际新 binary 自由系数在准确新符号节点上定义的数学场”减去“原数学场”。**不是**把 ordinary double 运算所得的一组点值称为连续场证书。numerical operator 使用的 carrier mesh/a/R 仍有其普通浮点误差；报告明确把这件事与 (676.9) 分开。

### 定理 676-B：完整六 jet 差的连续包围

令每个新胞左右端的系数三 jet 差区间为 $\Delta Y_0,\Delta U_0,\Delta A_0$、$\Delta Y_1,\Delta U_1,\Delta A_1$，其真实胞宽为 $h>0$。差多项式的五次 Bernstein 控制值准确为

$$
\begin{aligned}
B_0&=\Delta Y_0,\\
B_1&=\Delta Y_0+h\Delta U_0/5,\\
B_2&=\Delta Y_0+2h\Delta U_0/5+h^2\Delta A_0/20,\\
B_3&=\Delta Y_1-2h\Delta U_1/5+h^2\Delta A_1/20,\\
B_4&=\Delta Y_1-h\Delta U_1/5,\\
B_5&=\Delta Y_1.
\end{aligned}
\tag{676.10}
$$

径向导数控制值为 $5(B_{j+1}-B_j)/h$，再次作同一公式得到二阶导数的四次到三次控制值。角导数保留物理旋转基的连接项：对频率 $\nu=2j$ 的系数 $(r,t,z)$，

$$
\begin{array}{c|ccc}
 & e_r(\phi)&e_\theta(\phi)&e_z\\ \hline
\partial_\phi&-(\nu r+t)\sin\nu\phi&(r+\nu t)\cos\nu\phi&-\nu z\sin\nu\phi\\
\partial_{\phi\phi}&-((\nu^2+1)r+2\nu t)\cos\nu\phi&-((\nu^2+1)t+2\nu r)\sin\nu\phi&-\nu^2z\cos\nu\phi .
\end{array}
\tag{676.11}
$$

对任一需要的径向／角导数组合，在每个控制值的三个物理频道上分别取全部系数绝对值之和 $b_R,b_T,b_Z$。则对应整个胞、整个角圆周上的向量范数满足

$$
\|\Delta \partial_s^u\partial_\phi^v F\|\le
\max_{\text{controls}}\sqrt{b_R^2+b_T^2+b_Z^2},
\quad (u,v)\in\{(0,0),(1,0),(0,1),(2,0),(1,1),(0,2)\}.
\tag{676.12}
$$

用向外算术计算右端，并在全部新胞取最大值，便得源码输出的六项全域上界。

**证明。** (676.10) 的 Bernstein 多项式有指定端点三 jet，由定理 676-A 的唯一性即为差场。导数控制值公式来自 Bernstein 基的直接微分。对 $e_r'=e_\theta$、$e_\theta'=-e_r$ 作完整乘积法则得到 (676.11)，没有丢掉旋转基项。每个角三角函数的绝对值不超过一，三个物理基在同一个 $\phi$ 正交，故单个控制向量范数不超过相应平方和根。Bernstein 基非负且和为一，向量范数的凸性给出 (676.12)。真实胞宽和端点误差均在其向外盒内，逐运算包含性保持上界。最后，core、$H$、$f/h/k$ 都未变，解析 lift 的差准确为零，故 q 的差就是完整 F 的差。证毕。

(676.12) 是 $(s,\phi)$ 图中的六 jet，不把它直接叫作不带条件的全局材料 $C^2$ 范数。若还用已经支付的 $\rho\ge m>0$ 与 $|\rho'|\le L$，则同一 core 下

$$
\|\Delta F_\theta\|\le\|\Delta F_\phi\|/m,\quad
\|\Delta F_{s\theta}\|\le\|\Delta F_{s\phi}\|/m,
\quad
\|\Delta F_{\theta\theta}\|\le
\|\Delta F_{\phi\phi}\|/m^2+L\|\Delta F_\phi\|/m^3.
\tag{676.13}
$$

这只是链式法则的严格换算；源码不虚构尚未输入的 $m,L$，也不因此复制旧 reach 数值。

## 4. 每个新观察点仍查询原准确标量

对任一新胞及其声明的局部参数 $u$，实际点的数学定义为

$$
s(u)=\{(1-u)\alpha_L+u\alpha_R\}S+
(1-u)\beta_L+u\beta_R.
\tag{676.14}
$$

保存的 $u$ 是其 literal binary64 数所代表的准确有理数。源码用 Fraction 构造 (676.14)，再调用**同一个原 FullHold 输入、同一整数 oracle 源、同一 Hold 源、同一 panels 参数**的 `affine_time` 和 `at_box`。每个新增节点、中点、六 Gauss 载体及保留旧行都这样取 $a$，仅按完全相同的 $(\alpha,\beta)$ 定义缓存查询。不会用旧 $a$ 数组插值，不会重新拟合一个标量，不会把 $a$ 随场重参数化。

每个 $a$ 载体和时间载体的绝对误差均从整数包围向外转换。core 的 $a(0)=1$ 以及终端 $a(S)=R$ 使用原准确端点身份及其载体。报告重建当前节点表、当前 J/M/行数和当前误差字段；它**不**复制旧 warm 的 J/stage 数、旧 `true_a_stage_boxes`、旧投影诊断或旧 bundle 身份。

冻结 R657 `Scalar` 还需要每个当前 node/midpoint 的准确 $a$ 锚盒。因此入口直接保留本次 `at_box` 已经返回的前 $2J'-1$ 个整数盒，用原 `full.enclosure` 写成新的 `true_a_stage_boxes`，逐项保持新 node/midpoint 顺序与准确有理上下端。没有额外 oracle 查询，也没有从旧盒或误差上界插值。这使当前 fine node report 可直接供 R657 与依赖它的 R674/R675 连续读者消费。

FullHold 的数学函数由原参数固定；整数 panels 是其包围／载体精度参数，不改变 (676.1)。本入口仍显式保留源节点报告的 panels 值。ordinary double 场读数和目标不是向外的连续相对 Gram 最大值；严格连续结论需用其准确标量余项消费者。

## 5. R671 模型的准确重绑定

canonical 模型由 `reference_tail_model_json` 给出，含 `lambda_value`、$\eta$ 两端的 `eta_start_symbolic` / `eta_end_symbolic`、当前节点索引、M、mesh SHA、node-report SHA、carrier SHA 和原标量／算子源身份。`reference_tail_lambda`、`exact_tail_lambda` 与 JSON 中的值若同时存在，必须一致。

精化按定理 676-A 保留旧节点，故原 $\eta$ 两端仍各自出现在新符号节点表中。以它们的符号对寻找新索引；二分时原索引自然翻倍。新的 context 使用新 mesh、新观察 carrier、新节点报告、原 scalar 输入和同一个固定 $\lambda$，并生成**新的正确 canonical JSON**。物理 $\eta$ 的端点准确未动，因此 R671 的 $\eta,\chi,a,I,f_\lambda,h_\lambda,k_\lambda$ 全部还是同一实函数。

实际源码先写不含陈旧模型 JSON 的新坐标载体，再用 frozen factory 建立当前 context、保存当前解析尾 profile carrier，最后用 `bundle_arrays` 输出新场身份。它不把旧 JSON 直接附在新 mesh 上，也不绕过 factory 普通 `transfer_seed` 对“同模型”的检查：后继 solver 接收的是已经合法重绑定的 fine bundle，在**相同 fine 模型与相同 $\lambda$**下执行 `keep-q`。

解析尾对新数值观察点的 oracle 值可能因重新查询产生新的载体误差；其准确实函数保持是上述符号恒等式，不能以 carrier hash 相同代替证明。新的连续 R674/R675 消费者可据新模型身份直接读 fine mesh；父非平面／曲率标签不自动转移。

## 6. 所有旧行完整保留，且每行权重严格为正

首先构造新网格原生的节点／中点前缀，长度 $2J'-1$；每个新胞按原 lift 的准确符号断点分 piece，加入六个 Gauss 数值载体。旧 $S-\mathrm{width}$ 节点被保留，所以不从 carrier 相减另造一个伪细胞。

对原胞位置 $(i,u)$，二分映射为

$$
(i,u)\longmapsto
\begin{cases}(2i,2u),&0\le u\le1/2,\\
(2i+1,2u-1),&1/2<u\le1.
\end{cases}
\tag{676.15}
$$

源码先在 Fraction 中作运算，再核转换后的 binary64 数准确等于该有理数。该处没有小数位舍入。$u=1/2$ 选择左子胞的 $u'=1$；相邻表示在准确共享三 jet 下给同一点的相同六 jet。

对旧每一行，用 (676.14) 的准确符号对检查其物理 $s$ 未变：若新计划已有该点，则映射到已有行；否则追加旧点及其新的 $3\times6$ Hermite 三 jet 权。旧节点／中点在二分后已是新节点；旧 Gauss 和更早保留的点则完整继承。`refinement_parent_stage_map` 保存每个旧行的准确新地址。没有以新六点替换、删去旧观察点。

令 $S_{\rm new}$ 是新 composite Simpson 规则，$G_{\rm new}$ 是新六 Gauss 规则，$Q_{\rm old}$ 是旧 carrier 中**完整**的 quadrature 规则，含前次精化保留的行。新 carrier 的 quadrature 设为

$$
Q_{\rm new}=\tfrac12G_{\rm new}+\tfrac12Q_{\rm old},
\qquad
W_{\rm new}=\tfrac12S_{\rm new}+\tfrac12Q_{\rm new}
=\tfrac12S_{\rm new}+\tfrac14G_{\rm new}+\tfrac14Q_{\rm old}.
\tag{676.16}
$$

相同物理行上的权相加。新节点／中点有正 Simpson 权；新 Gauss 点有正新 Gauss 权；每个需额外保留的旧点有正的旧 quadrature 权。故全部行在 $W_{\rm new}$ 中均为正。实现核其实际浮点权有限且严格正，所有残差、Jv、转置和目标使用同一完整观察 plan；新的行没有被零权排除。

在准确规则的数学层面，三个规则都作用于同一径向区间，权和均为 $S$。对任意固定连续被积函数，若径向二分持续使最大胞宽趋零，则 $S_l,G_l$ 的误差趋零，递推 $Q_l=(G_l+Q_{l-1})/2$ 的误差也趋零。证明：给任意正数 $\varepsilon$，从某个 $L$ 起 $G_l$ 误差不超过 $\varepsilon$，于是

$$
|e(Q_l)|\le2^{-(l-L)}|e(Q_L)|+
\varepsilon\sum_{j=1}^{l-L}2^{-j}
\le2^{-(l-L)}|e(Q_L)|+\varepsilon.
\tag{676.17}
$$

故 (676.16) 是同一个积分目标的相容离散，不另造 $g$。这里说的是**固定连续被积函数**的相容性；若每层场变化且没有统一正则性控制，不能把这个论证冒充整列数值解的最大误差收敛。实际 double Gauss 节点／权及 carrier 宽是数值规则；其 ordinary double 加权和也不称为准确积分等式。R671 的 $a,I$ 一般非多项式，更不把六点当作其积分的有限代数精确公式。

角 grid 取 $N'=2^kN$，$N,N'$ 均为四的倍数、$N>4M$、$N'>4M'$。旧理想角是新角的子集；当前 quarter FFT 的 binary 角载体也按该二倍伸缩保持，源码读取时直接核对子集。端点角重数为 2，内部为 4，保留原全圆和。M 增大但 N 不变时仍要求有限三角空间的 FFT 条件 $N>4M'$；这不把非多项式解析 lift 或谱损失称为有限带宽积分。

## 7. 跨层比较必须使用共同的旧有限泛函

令 $r=(e,f,g)$ 为完整相对 Gram 的三个分量，$\lambda_\pm(r)$ 为其对称矩阵特征值。使用固定参数 $p=8$、$\epsilon=.001$、$c=.05$，点损失为

$$
\ell(r)=\left(\frac{\lambda_+^2+\epsilon^2}{c^2}\right)^4+
\left(\frac{\lambda_-^2+\epsilon^2}{c^2}\right)^4.
\tag{676.18}
$$

新层完整目标由 (676.16) 和新角数定义。**由于行与混合权变化，不能直接用 $\Phi_{\rm fine}-\Phi_{\rm coarse}$ 的符号证明求解改善。** 同一场在更密且不同权的规则上数值变大或变小都不具有这种含义。

源码另给 `CommonGridReadout`。它把**当前 fine 场**读在全部父观察的准确新地址和父角子集上，使用父 carrier 的 literal $a_i$ 及父权

$$
W_{\rm parent}=\tfrac12S_{\rm parent}+\tfrac12Q_{\rm parent}.
\tag{676.19}
$$

只在这个完全相同的有限泛函上，与已登记且身份匹配的父读数比较才有意义。新完整网格使用重新查询的同 oracle $a$；common 读数明确使用父 $a$ 载体来固定比较算术，不称此数组为 $a(s)$ 的插值。

共同读数给出全部父行数、实际读取行数、父完整角数、谱参数、最小径向权、归一化分母、mean Phi、加权 Frobenius SSE、最大相对 Gram 与最坏地址、相对行列式最小值。其初次读取复用 fine 全行流式场值，不另计算原父场；后继 `read-common` 仅对实际求解后的新 bundle 读取包含父行的第一 jet 块。

若 fine 求解后来改变自由 core，共同泛函仍按同一原 $s,\phi$ grid 与当前准确公式的 $\rho_c$ 读相对 Gram；不能把“相同 chart 网格”额外解释成所有点的材料 $\theta$ 也与父逐点不变。转移瞬间 core 未动，二者才同时相同。整个目标对应的材料参考函数 $a(s)$ 和 (676.1) 始终没有更换。

common 读数本身仍是 ordinary double 的有限点读数。它不支付连续最大相对 Gram，不证明精确解存在，也不支付 README 所需的多层真实下降。若已保存的父报告没有同参数、同 carrier、同权的可比值，应如实列出不可直接比较；不得补造一个父数值。

## 8. 永久曲率／半径位置的准确迁移

永久 manifest 中的 `curvature_points`、`radius_points`、`protected_curvature_points` 都按准确 binary 数值三元组 $(i,u,\phi)$ 保存。径向应用 (676.15)，$\phi$ 原值逐项保留，再以 (676.14) 核对准确 $s$ 身份。protected 点并入曲率集合且保留标签。只有数值完全相同的三元组可合并；不同 binary 实数位置不按 13 位小数归并。

如果输入仍是已声明完整角数下的原 grid 地址，则先以该旧 plan 的 cell/u 和该角数恢复其原数值 $\phi$，再做同样迁移。当前 core 补零保持 $\Theta_c$，所以转移时这些点的材料角也保持。旧点上的曲率、半径、可行性数值都不继承，实际新场必须重新读它们。

新的纯位置 manifest 采用紧凑 JSON 空白格式，无任意 100 KB 文件大小截断。大小不是数学域条件；结构明确为已有 `immutable-curvature-history-locations-v1` 和完整三元组列表。source carrier SHA、实际新 bundle SHA、来源 manifest SHA 和迁移源 SHA 都记录。它只携带位置和来源，未附带声称可沿用的旧几何值。

后继 bridge 从两份 frozen 完整 QP driver 中派生一个**另有路径与 SHA 的 fine driver**，只作以下局部源变更：

1. 用显式纯位置 schema／三元组结构取代原 manifest 的任意 100000 字节上限。
2. 在 `load_witnesses` 与 `add_actual_location` 的六处位置键中，把 `round(float(...),13)` 改为原 `float(...)` 数值键。

完整残差、正谱目标、残差 Hessian、完整 H² 坐标、全部自由空间、几何行、线搜与数值参数均不改。这里“目标未改”指**同一 fine 输入 plan 上**相对于 frozen driver 的源变更；不声称 (676.16) 与父层离散目标相同。原来已经排队或执行的 driver 文件不改字节。

## 9. 完整 Actions 接口与输出边界

主源目标路径为

`scripts/resume_20261120/refine_fixed_g_fullclosed.py`

本次 48985 B，SHA-256：

`2e8ae99813c105982b10b896606538c1c42baf0abf089457412b32e265d4411a`。

它绑定并记录 frozen 原 observed、batch、dense、FullHold、整数 oracle、Hold、区间、R662 差公式、R671 factory、任意点六 jet、几何读者及 R660 源的路径／SHA。关键依赖：

| 源 | SHA-256 |
|---|---|
| `gauss_observed_closed_gram.py` | `26f61a83505938d409ad97fdfd2b3a96d77dd0233810980aa8cd19faa9920d0d` |
| `resume_20261120_batched_closed_gram.py` | `02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a` |
| 原 FullHold oracle | `a1ed8fa5d2186f400ea50a1d609574ec6996e59317a57638a6820a59cf0e7670` |
| f512 向外算术 | `f512c96cbc1fb3896fc144c5e9d8d29aaa80e321d08d9cdbf1745beb54a5c57d` |
| R671 canonical factory | `2e0219c50543d859a9c649553bc4dde863df24daab26ffa75e5112baa4a90216` |

下列命令中，所有输入都是本次公开 Actions 实际生成的文件；环境变量只用作命令示例，不替代真实输入 SHA。

```bash
python "$TOPIC/scripts/resume_20261120/refine_fixed_g_fullclosed.py" \
  --repo "$REPO" --bundle "$ACTUAL_PARENT" \
  --carrier "$ACTUAL_OBSERVATIONS" --node-report "$ACTUAL_NODES" \
  --scalar-input "$ORIGINAL_SCALAR_INPUT" \
  --manifest "$COMPLETE_ACTUAL_LOCATIONS" \
  --radial-factor 2 --modes 160 --source-angles 2048 --angles 2048 \
  --stage-block 64 --outdir "$WORK/refined-r2-m160"
```

`--modes` 省略时保留父 M；不能用示例 M160 截去一个已经大于160的父。纯频率精化可用 `--radial-factor 1 --modes 192`；角数仍必须满足前述条件。`--manifest` 可重复以取完整位置并集。`--transfer-only` 只跳过最后的有限场读数，不跳过准确符号转移、同标量新查询、完整 carrier 和模型重绑定。

默认输出的实际数据只保留在 runner，包含：

- `refined-seed.npz`：实际新 free jets／H/core 和正确模型身份。
- `refined-same-g-observations.npz`：全部新旧行、三 jet 权、同 oracle 标量与误差、父行地址映射。
- `refined-symbolic-nodes.json`：当前准确符号节点、同标量身份及当前全部 node/midpoint 的准确 $a$ 锚盒。
- `transfer-jet-error-boxes.npz`：式 (676.9) 的误差盒。
- `refined-permanent-locations.json`：所有永久位置及其来源。
- R671 情形另外的当前 reference-tail profile carrier。
- `refinement-report.json`：所有实际输入／输出 SHA、转移范围、六 jet 连续舍入差界、全新有限网格与共同父 grid 的各自读数。

有限读数使用完整物理六 jet，包括 R671 的固定 $k'$、$k''$。它流式读取全部观察／角值，给出 Phi、最大相对 Gram、相对行列式、有限曲率／半径及每个永久位置的新几何值。无效浸入点如实登记；报告中的连续度量、连续几何、reach、精化收敛、课题完成标志都保持 false。

后继 bridge 目标路径为

`scripts/resume_20261120/launch_fixed_g_refinement_qp.py`

本次 12978 B，SHA-256：

`100e57c66e1f5b592fe22570c6c7894a6ab75e082b714edfff42514098d5c622`。

它分别绑定原完整 driver SHA

`5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a`

及 R671 完整 driver SHA

`b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8`。

```bash
python "$TOPIC/scripts/resume_20261120/launch_fixed_g_refinement_qp.py" \
  --repo "$REPO" --work "$WORK" \
  --refinement-report "$WORK/refined-r2-m160/refinement-report.json" \
  --outdir "$WORK/fine-full-phi-01" --damping "$EXPLICIT_DAMPING" \
  --directions 1 --maxiter 256 --active-rows 192 --stage-block 64
```

bridge 自动选择原／R671 路径，给出显式新 driver 字节与 derivation SHA，读取该 fine carrier 的全部行，完整 QP 自由维数由新 J/M 计算。R671 路径保持相同 fine $\lambda/\eta$，不借精化再作一次模型 homotopy。正常返回后，无论是否实际接受一步，都从真实 `final.npz` 和 solver `final_bundle_sha256` 取得当前场，并自动执行 `read-common`。该读者也可单独调用：

```bash
python "$TOPIC/scripts/resume_20261120/refine_fixed_g_fullclosed.py" read-common \
  --repo "$REPO" \
  --refinement-report "$WORK/refined-r2-m160/refinement-report.json" \
  --bundle "$WORK/fine-full-phi-01/final.npz" \
  --out "$WORK/fine-full-phi-01/common-parent-grid.json" --stage-block 64
```

`--print-command` 仅生成可审阅 argv 与新 driver 源，不启动科学子进程。实际转移、标量求值、场读数和 solver 都要求当前公开仓库的 Actions 环境。每次应用应登记实际 run 编号、输入／输出 SHA、参数、是否接受方向、共同 grid 的可比结果及新的连续误差范围；没有真实返回就不能填入这些数值。

## 10. 对完成标准的准确意义

本条已支付的是：同 $S/R/a/g$、同参数范围、原或固定 R671 模型的完整嵌套空间；理想恒等转移；实际载体舍入差的连续六 jet 包围；准确符号位置和全部旧观察／永久位置保留；同一父有限泛函上的明确比较接口；可执行的完整 finer solve 入口。

仍未支付的是：当前或新父的连续最大相对 Gram 达到 $10^{-6}$，固定 $g$ 下跨网格／频率／参数加密的实际误差持续下降直到容差，或精确等距解的存在定理。旧场即使已经有连续几何证书，新 literal binary 场与其后接受的非线性场仍须按实际差界或同候选消费者支付对应范围。新空间包含旧空间只说明更细的模型没有因表示能力而丢掉理想旧场；它不保证非线性 solver 收敛，不保证当前固定空间存在准确零残差解，更不允许放宽课题原完成标准。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
