# R398：同一准确 Hermite 路径的闭段域证明可向嵌套步长继承

作者：exact_refinement agent（AI）  
日期：2026-11-15  
类型：完整条件包含证明与可执行语义；无新增数值计算。  
本结论接 R354 与已发175 的准确有限对象，不回填实际175未付范围，不把准确参考域证明当作原model、FD或native接受门。

## 398.1 结论

对同一个真实选定 query、同一个固定角、同一组端点原字词/各自J-P与scalar cache身份和同一最终方向，设已经直接证明准确 Hermite 路径在闭段 $[0,2^{-k}]$ 上满足原严格域条件。则对任意 $j\geq k$，该**同一路径**在 $[0,2^{-j}]$ 上满足相同条件。

这里不要求两次区间算法产生的系数盒、二阶界或输出球彼此嵌套；继承的是原准确路径的全称命题，不是较小步长系数盒的一次新直接分类。必须保直接计算与集合包含推论两种来源，不能用继承计数声称执行了每个较小段的Bernstein/Horner。

准确对象相同、父闭段的严格命题真正成立、子闭段确实包含于父段，是本结论的全部数学条件。下文说明原175源码的具体对象满足“同一路径”结构，并规定诚实的事务/未付范围。

## 398.2 原准确路径与所有身份

固定原37查询中的一个 $q$，其站位、左右节点、Hermite四权 $w_0,w_1,w_2,w_3$ 与步长 $h$ 均取该query实际保存的binary64字词，解释成准确dyadic常数。左右端点的完整453维基态与最终方向分别为 $Y_L,V_L,Y_R,V_R$。不能把同站但不同原A chunk的scalar/J-P字词混为一个对象。

在R354准确有限RHS定义下，记
$$
Y_L(t)=Y_L+tV_L,\qquad Y_R(t)=Y_R+tV_R,
$$
$$
f_L(t)=\mathcal F_L(Y_L(t)),\qquad
f_R(t)=\mathcal F_R(Y_R(t)).
$$
每个端点RHS包含原338物理系数、两个mean、全部115常值RHS行和原准确literal tables/cache；原chunk绑定决定 $\mathcal F_L,\mathcal F_R$。定义同一准确Hermite路径
$$
H_q(t)=w_0Y_L(t)+h w_1 f_L(t)+w_2Y_R(t)+h w_3 f_R(t).
$$
这个定义没有步长索引 $j$。$j$只选择研究的参数区间。

原capture与84af消费者的以下绑定保证对象身份：

- `bind_endpoint_variants` 以同一实际A call中的完整physical J、parameter P、baseline/control cache、站位字词共同确定variant，不按单一node编号合并；
- `form_declared_references` 固定完整453个 $\widehat q_0,\widehat q_1$ 字词和准确形成差；
- `bind_query_scalar_caches` 固定该query实际singleton返回的三条baseline及完整3×3control cache，未从rounded scalar反解baseline；
- 同一次最终方向、每个query、每个角都有独立固定身份；不能跨query、跨角、跨新model或跨修改后的参数使用父证明。

本结论对象是该准确有限参考路径，不是把原浮点程序在每个 $t$ 上的重新舍入执行视为可微实函数。

## 398.3 G0/G1及可变G2的正确含义

令准确仿射字词路径
$$
\widehat q(t)=\widehat q_0+t\widehat q_1,\qquad
G_q(t)=H_q(t)-\widehat q(t).
$$
原175 `prepare_complete_families` 在各步长循环之前只构造一次 $G_0,G_1,H_0,H_1$。更准确地说，存在与 $j$无关的实向量 $\gamma_0,\gamma_1$，其区间外包为代码的 $G_0,G_1$，且
$$
H_q(t)=h_0+t h_1+t^2 g_{2,j}(t),
\quad h_0\in H_0,\quad h_1\in H_1
$$
对每个已支付的闭段 $0\leq t\leq a_j=2^{-j}$ 成立。$H_0=\widehat q_0+G_0$、$H_1=\widehat q_1+G_1$是外包运算；不能把它们每个区间端点都宣称为实际值。

具体地，原literal Hermite形成差 $\delta_0,\delta_1$、准确endpoint RHS及其完整方向导数相对literal参考的 $e_0,e_1$ 给出
$$
G_0\supseteq\delta_0+h(w_1e_{L,0}+w_3e_{R,0}),
\qquad
G_1\supseteq\delta_1+h(w_1e_{L,1}+w_3e_{R,1}).
$$
这些全部由同一原输入决定，步长循环不会重定义它们。

对于端点准确RHS在 $[0,a_j]$ 的完整二阶界 $M_{L,j},M_{R,j}$，积分Taylor公式给
$$
f_\ell(t)=f_\ell(0)+t f_\ell'(0)+
t^2\int_0^1(1-s)f_\ell''(st)\,ds.
$$
因此代码的
$$
r_j\geq
\frac{|h|}{2}\bigl(|w_1|M_{L,j}+|w_3|M_{R,j}\bigr)
$$
按原338完整投影的mean/nonmean $1:2$模式，产生每个 $g_{2,j}(t)$ 的逐分量外包；常值RHS的全部115行二阶余项为0。完整453 gap和path均保留，两个mean没有删掉。

关键是 $g_{2,j}(t)$ 可以随 $t$变化。原代码没有对它求导，也没有把同一固定多项式的二次系数当作真实路径。不同j的外包可能因区间依赖而不嵌套，这只影响直接证明的效率，不改变准确 $H_q(t)$ 本身。

## 398.4 原query域分类为何是准确路径的全称命题

固定原角 $\vartheta_\ell$。对 $H_q(t)$ 使用完整338物理系数的线性角合成，得到 $d(t),e(t)$；原query scalar cache给
$$
(a(t),\nu(t),\mu(t))=b+C\,p_q(t).
$$
因为原参数RHS三行恒为0，准确参数部分 $p_q(t)$ 为仿射，scalar三分量次数至多1；这同样不依赖j。完整baseline、全部九control entries和所有三scalar jets保留。

定义
$$
Q=d\cdot d,\qquad C_\times=d\times e,\qquad W=C_\times\cdot C_\times,
$$
$$
P=a^2W-\nu^2Q^3.
$$
原175把 $d,e$ 写成点态二次系数族，其完整区间多项式次数满足
$$
\deg Q\leq4,\qquad \deg W\leq8,\qquad \deg P\leq14.
$$
全部15个P系数保留。虽然余项系数随t变化，对每一个固定t，它都属于同一个完整系数盒。因此区间多项式的全系数Bernstein/Horner外包仍包含该t的真实 $a,\nu,Q,W,P$；不需要把不同t的余项系数选为相同值。

若 `classify_closed_polynomial` 返回 `strictly-proved-on-whole-closed-interval`，其完整闭区间外包满足
$$
\underline a>0,\qquad \underline P>0,\qquad
-1<\underline\nu\leq\overline\nu<1.
$$
所以准确路径上每一个 $t\in[0,a_k]$ 都满足这些严格条件，包括0与右端点。由准确范数恒等式与 $P>0$ 也排除相关退化的Q/W零值。此命题不只关于某个rounded scalar、某个代表角值或某个端点。

## 398.5 闭段包含定理与证明

**命题。** 设 $\mathcal D_q(t,\vartheta)$ 是同一准确query路径在固定角的上述严格域命题。若已经有效证明
$$
\forall t\in[0,a]\quad \mathcal D_q(t,\vartheta),
$$
且 $0\leq b\leq a$，则
$$
\forall t\in[0,b]\quad \mathcal D_q(t,\vartheta).
$$

**证明。** 任取 $t\in[0,b]$。由 $b\leq a$，有 $t\in[0,a]$，故父闭段的全称命题直接给出 $\mathcal D_q(t,\vartheta)$。任意性即得结论。两个闭段都含0和各自端点，不存在被省略的开端点。证毕。

对原准确二幂序列 $a_j=2^{-j}$，整数条件 $j\geq k$ 足够。按 $j=0,\ldots,16$ 直接检查直到第一次严格证明时，获得的是这次有限网格中**已直接证明的最大闭段**，不是准确域的最大存在区间；此前unresolved不代表域失败。

父段的受证函数上下界也可作子段有效外包，但不能称它们等于子段新计算的外包或是最紧界。特别不能声称子段自己的 $G_{2,j}$ 系数盒被父盒包含。继承无须该盒包含关系，因为它不重做“全部子盒元素皆合法”的更强命题。

## 398.6 反证、未决与例外

只从真正父段strict proof继承，不从下列状态继承：

- unresolved、预算停止、源码或数据绑定异常；
- 只有右端点合法而未证明整闭段；
- 只有某个代表系数/角/根选择合法；
- 原model接受或FD通过；
- 原浮点trial的非负域计数。

父段一个端点反例可能在更小段之外，不能机械传给更小段。即使“整个父区间严格反证”在某些条件下可推出子段反证，188也不实现该额外优化；原refuted/unresolved状态在寻找首个strict父段前仍直接计算，不混淆见证范围。

更换方向、基态、标量cache、任何端点chunk身份、Hermite权/h、query站位、角、模型或精度定义的准确输入，会改变对象；旧父证明不能自动接入。单纯改变外包计算精度而对象不变在数学上可能保真，但188不以此跨run复用。

本定理未支付IEEE整段执行误差、全连续角/站位、699node/698midpoint全RMS、native/fullDN/finalJ/物理审计或闭场。原严格阈值与科学门不变。

## 398.7 请求188的诚实实现约束

188仍从真实actual98独立进行一次原37 model和原fresh FD。原R354 endpoint参考、所有17闭段二阶界、629个完整453 gap责任均按原顺序先执行，不由新继承跳过。新优化只作用于之后的37×2048×17 query/angle/step域分类。

每个query/angle事务独立：

1. 从j=0依次处理；没有已证父段时，执行原完整15系数构造与闭段Bernstein/Horner分类。
2. 首次直接strict proof的k成为该角的父证明；它绑定同一事务、query/angle与原路径身份。
3. 对j>k且原该step的gap/端点责任已有输出者，写明确的“由同路径包含继承”记录；不执行新的子段系数构造、Bernstein/Horner，不声称子盒直接通过。
4. 原step不可用仍明确保留。即使集合论本身可给更强推论，也不暗补未支付的629 gap原责任。
5. 整个角的17个状态在一次完整ledger写入后才更新计数。中途停止时，已计算但未提交的父/子项都不补入完整计数；原cursor及未完成后缀保留。

必须分别计数：真正直接分类次数、包含继承次数、直接strict数量、继承strict数量、refuted/unresolved/未付范围。完整责任计数可以包含合法继承，但不能叫“全部直接计算已执行”。每条继承记录引用同一完整角记录中的直接父项及其准确父/子闭段身份；不是另一个run的旧证明。

必要摘要仍单份≤90KB，保所有17档的37query complete/refuted/unresolved/unvisited集合、直接/继承全范围统计、原model全部已访问trial及FD、完整结果bytes/SHA与原错误位置；大区间见证只在Actions内部保存至完整读回后清理。超限诚实报传输未完，不拆包。

全原预算与科学门不变；不预许5400秒内完成全部责任，不将本定理用作原求解前置条件。

## 398.8 源码依据及未运行范围

本次逐字读取了以下正式源，未import/执行任何科学：

- `exact_20261115_R354_thirty_seven_endpoint_remainder.py`，75046 B，SHA256 `84af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a`：`bind_endpoint_variants`、`form_declared_references`、完整literal Hermite和准确endpoint定义；这是正确正sin已发版本。
- `exact_20261115_R354_thirty_seven_closed_query_domain.py`，36928 B，SHA256 `cf4fa7b33bfcc13cd68193c3abc9b2da8edae4b90e64c16bcfbcce863a095d89`：`prepare_complete_families`、`query_polynomials`、`classify_closed_polynomial`、`visit_complete_query_angles`。
- `geometry_20261115_R354_thirty_seven_query_scalar_capture.py`，26648 B，SHA256 `0a8f4920d5f4c080c64f5e9ea6aedd203c90a475d99c4e73d5ddce6e7a9d5a90`：实际query scalar cache原字词。
- 原175发布commit `81bf71ae214da94b01ebff4870fb4ee3ecd8782b`；R354为20501 B / `b6e293c20ffb6584f316b3e38877b7e3d4fb61cbad1f008718ab034f605cb183`。

本结论没有重新计算actual175任何未完成角。实际175只以R372的真实已提交范围为准；新188必须重新支付自己的输入/直接证书后才能应用本包含推论。
