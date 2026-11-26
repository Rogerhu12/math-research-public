# 新 SO3 闭合场的完整有限几何、原 192 行与幅度约束接口

日期：2026-11-26。本文只登记新的可执行源和完整导数/接口事实，不登记任何尚未返回的数值或连续证书。实际科学求值只在公有仓库 Actions 中执行。

源为 scripts/resume_20261126/so3_closed_meridian_geometry.py，SHA256 72f3825913c9ac07b30dcbc47f34e4d8ad901c2f6b6cab0cdc50f35ab99a3cc6，43884 字节。主物理表示来自独立的 so3_closed_meridian_operator.py；本模块在真实执行时逐个核对它的 grid_fields、point_fields、point_vjp、prepare、domain 的实际源字节与完整 model.source_sha256，并复算完整模型身份。它不把新场写成 R671 的旧坐标场，也不接旧 R671 物理点转置。

本模块确实复用两份已发表源：a2a5d27edddc6fc20f88fde62677d904bb52db5fa9af37ca82d95272cb21a854 的坐标不变主曲率微分和有限极值选择；e783c8a3929a7a31946e8f9ceba86e504a1c4f2139c62c0e7d5eb0c21417abb8 的原完整 192 行选择器。后者的选择、保护点、同胞邻域代表、实际直径伙伴及非齐次右端完全不改。新的 world 六 jet 与全自由量 VJP 由明确的新物理 shim 提供。

## 1. 当前表示和历史地址的精确含义

新表示的角参数为固定父材料图的参数 phi0，theta0(phi0)=Theta_parent(phi0)。当前 core 的法向角 phi_c 每次由

$$
\Theta_c(\phi_c)=\Theta_{\rm parent}(\phi_0)
$$

反解。因此当前自由 core 不冻结；在实际完整物理 VJP 中，其隐式角变化和全部原 free core 的变化都仍在。

历史点的保存语义必须和这一新图相符：本入口保留历史的每一个 literal binary64 (cell,u,phi)，并将其中的数值 phi 当作新图的 phi0 逐一读取。这保存了完整的一组新表示查询地址，**不声称**旧模型的 current normal-angle 查询点和新模型的这一查询点是同一物理点。旧场的点值、曲率、直径、embedding、K、reach 或幅度证书一项也不传递。

新发现的全部极值地址均明确属于新 phi0 图；不四舍五入，不按工作行数删永久点。径向 cell/u 仍是当前同一符号网格上的 literal 地址。本模块不另行实施历史 Theta_c 到 Theta_parent 的物理点迁移。当前隐式反解的残差、数值积分与单位向量归一化误差由物理 operator 如实报告，本文没有为它们支付连续误差。

当前闭合场为

$$
T=\exp(\omega\times)T_0,\quad
G=P_{\rm cap}+\int_S^sT(\sigma,\phi_0)\,d\sigma,\quad
\Delta=\Gamma_c-G(0,\cdot),\quad
F=G+h\Delta.
$$

特别地，$F_s=T+h'\Delta$。完整径向 Gram 残差并没有因 $T$ 单位长度而消失。模块要求实际 model 明示保留这一项以及全 free core、全部旋转变量和最后的 H。

## 2. 为什么 quarter 加两个 witness 符号够用

omega 的三 world 分量分别使用 sin(odd phi0)、cos(odd phi0)、sin(even phi0)。对于 y 反射 $S_y=\operatorname{diag}(1,-1,1)$，有

$$
\omega(-\phi_0)=\det(S_y)S_y\omega(\phi_0).
$$

对于 x 反射 $S_x=\operatorname{diag}(-1,1,1)$，phi0 换成 pi−phi0 后也有相同的轴向向量变换律。这给出

$$
\exp((\det S)S\omega\times)=S\exp(\omega\times)S^{-1}.
$$

父 T0、固定材料图、当前对称 core、cap 和径向 h 同样服从这些反射，所以新完整 F 的反射对称性由精确表示继承。反射保持欧氏范数、面积和主曲率绝对值。赤道点 $p=(0,r_0,0)$ 在 x/y 反射下或者保持或者换成 −p，故 quarter 上必须同时读取两个符号。下半面的 z 反射保持这两个赤道点的距离。

这只说明精确新公式的有限点集可以用 quarter 对称轨道读取。它不把有限轨道变成完整连续 s/phi 的覆盖；也不支付数值积分、求根和曲率浮点运算误差。

## 3. 完整有限真值扫描

GeometryScreen.scan(x,witnesses,radius_witnesses) 的工作顺序如下。

1. 核当前完整 x，核 prepared.core 的 free 前缀和 prepared.height 的最后坐标。
2. 遍历实际 grid_fields 的全部角块。每块包含全部 P 个径向观测。用角覆盖位集拒绝重叠、越界或缺失，读取每个点的 F、Fs、Fphi、Fss、Fsphi、Fphiphi。rho0 与 closure_delta 只是另外明确检查的真实诊断，绝不当作六 jet 坐标。
3. 对完整 grid 读取主曲率两支、半径、两种 witness 距离和 body 球界；非有限值或非正切向面积立即给 complete=false。grid 的曲率公式采用旧源的有限计算式，不冒充向外舍入。
4. 将两个永久点集合取无损并集，逐一读取同场完整六 jet。每点仍读两支主曲率、半径和两个 witness 符号。曲率使用旧源的实际 generalized symmetric eigenvalue 微分函数，供工作行复用同场值。
5. 将本次真实 worst、farthest、原选择器的工作代表以及幅度代表加入永久记忆；这些点都已经在本次真实 grid 或永久点查询中读到。新增位置返回主 driver，拒绝 trial 的新位置也继续保留。
6. 最后将完整实际 K 极值与完整实际 D 点下界配对，读取必要量 reach_ratio D K。它与全部幅度值的最大超量决定 passed，不从线性 C、Phase I slack 或下降的 Phi 推断几何可行。

这里

$$
D_{\rm point}=\max\{2,\ 2|H|,\ 2\max_{\rm all\ read}|F|\}.
$$

它是原对称闭合场中的必要点下界，仍不是全域 D 上界。scalar cap 球界另行必读。返回的 complete 仅表示本轮所有声明的有限观测及全部永久地址实际完成；continuous_geometry_certified、continuous_metric_certified 和 old_continuous_certificates_inherited 都为 false。

缓存只对字节相同的完整 x 有效。换父场就清空 field/grid cache。它避免同一次完整扫描被 selector 重新计算，不跨候选继承几何值。完整 grid 读取时已经存在的精确 grid 地址从实际块中提取；不是把旧缓存当新场。

## 4. 同场幅度值与完整 world 导数

这里沿用已登记的同场整体球/指定 witness 预算策略，不能说这是所有可能达到幅度的场都必须满足的条件。固定预算记为 marked Dbar、Lbar 和 Hmin；marker 高度 h0=1/1000。body 预算 B 是精确 binary64 Dbar−2h0 的向下舍入值；额外幅度高度下限是 Lbar+h0 的向上舍入值，实际高度下限取它与 Hmin 的较大者。R 是同一个固定 deep 标量的 cap 半径载体，绝无自由 R 导数。

Budgets 要求 Dbar≤4.5、5Lbar≥Dbar、R>9/20、Hmin>1。它们保留固定直径 0.9 grip 与 cap 的既有语义。以上只有标量边界舍入；并不认证 F 的浮点计算。

赤道的两个指定点是

$$
p_\sigma=\sigma(0,r_0,0),\qquad r_0=1+\sum_{\text{all core}}c_j,\qquad \sigma=\pm1.
$$

在每个实际新图地址读三个无量纲值

$$
g_D=\frac{4|F|^2}{B^2}-1,\qquad
g_{L,\sigma}=1-\frac{|F-p_\sigma|^2}{L_{\rm bar}^2}.
$$

这一次 p 是 **world 坐标**常向量；不再使用旧旋转局部坐标中的随角向量。固定图 phi0 的 y 轴点给出的当前赤道位置仍是 $p_\sigma$，因为所有 support 频率为偶数、相应正弦在轴上为零。

令 $w_\sigma=F-p_\sigma$。全变量微分为

$$
dg_D=\frac{8F\cdot dF}{B^2},
\qquad
dg_{L,\sigma}
=-\frac{2w_\sigma\cdot dF}{L_{\rm bar}^2}
+\frac{2\sigma(w_\sigma)_y}{L_{\rm bar}^2}
   \sum_{\text{free core}}dc_j.
$$

第一项由实际 SO3 point_vjp 接收 world F covector。第二项加到**每一个**原 free-core 前缀条目，然后才经过完整 H2 坐标转置。固定前三 core 的微分是零；它们的值仍包含在 r0 中。没有遗漏任何当前 free core 对指定 witness 本身的变化。H、积分、旋转和闭合 lift 对 F 的变化均在完整 point_vjp 中。

另外两条 scalar 约束必有：

$$
g_{\rm cap}=\frac{4(R^2+H^2)}{B^2}-1,\qquad
g_H=\frac{H_{\rm effective}-H}{L_{\rm bar}}.
$$

它们的全自由梯度只在最后 H 槽分别为 $8H/B^2$ 和 $-1/L_{\rm bar}$。

工作点选择上，最多两个 body 球界地点、四个距离地点；每个已选距离地点永远同时追加两个符号。每类最坏点保留，后续点按声明的 active_band 选择。cap/H 必加，最多 $2+2\times4+2=12$ 行。有限真筛和永久记忆没有这个行数截断。

## 5. 原 192 行、真实右端和 Phase I 单位

e783 原 selector 的行是

$$
g_i={\tt reach\_ratio}\,D_i|\kappa_i|-{\tt safety},\quad
a_i={\tt reach\_ratio}
 (D_i\operatorname{sign}(\kappa_i)\,d\kappa_i
  +|\kappa_i|\,dD_i)\,T,
$$

其中 T 是完整新坐标到完整原变量的线性映射；所有实际曲率、半径、core 和 H 都属于本次新场。旧 pure curvature_cotangent 对 world 六 jet 同样成立，因为其全部量由欧氏内积、叉积与 generalized eigenpair 构成。它的 cotangent 经新 point_vjp 返回完整新自由梯度，绝不调用旧场 pullback。

每条原行的 $\|a_i\|>0$ 检查仍保留，原式

$$
C_i=a_i/\|a_i\|,\qquad b_i=-g_i/\|a_i\|
$$

也原样保留。父点不满足某个约束时 b_i 可以为负；本适配不因负 b 删除原行。protected 原始点、当前同胞邻域代表、最强实际 D 伙伴和原工作集选择顺序都不改。

幅度行使用相同完整 T。若真实坐标梯度范数正，则 scale 取其范数；若为零，scale=1，**零幅度梯度行仍保留**，包括正违约的零梯度行。每条返回：

- physical_g：当前物理值减其 own upper_bound；
- physical_current_value 与 upper_bound：reach 是 product 和 safety；幅度是 g 和 0；
- gradient_coordinate_norm：真实完整坐标梯度的范数，可以为零；
- row_normalization_scale：严格正的实际归一化因子；
- normalized_bound：恰为 −physical_g/scale。

注意：原 e783 prefix 对 norm≤0 仍会明确抛错，这不是已接通的零曲率梯度 Phase I 机制。这里没有暗改旧 selector，也不把“新增幅度零梯度可保留”说成“所有原零梯度情况都已经解决”。

主 driver 的共同松弛必须在**同物理单位**写成

$$
g_i+a_i z\le\tau_0+\delta\tau,\qquad \tau_0+\delta\tau\ge0.
$$

可以在每行再乘任意已声明的正数，例如除以 $\sqrt{\|a_i\|^2+1}$。不可把已归一化 C 的每行直接配上同一个未换算的 tau 系数。模块同时提供真实 norm 和 scale，使主 driver 可以正确处理普通行与零幅度梯度行。松弛下降不是几何可行，必须重新完整真扫，且 restoration 的实际最大正违约按主 driver 规则严格下降。

## 6. 缓存与真实内存范围

原 selector 先写自己的完整 mmap prefix。随后本模块刷新并关闭这份视图，核真实 byte length，原位扩展**同一个文件**，只写末端新增幅度行；已有 prefix 不移动、不重写，不创建第二份完整 prefix。

因此同一 cache 既保存原全部已选行，又保存全部新增幅度行。metadata 区分原 prefix bytes、完整 row cache bytes 与实际 st_blocks。所有数组、缓存和逐点数据只在 runner scratch；明确拒绝将科学 cache 路径放在仓库树内。

## 7. 可直接接主 driver 的接口与状态

构造：

~~~python
budgets = Budgets(Dmarked, L, q.R, Hmin)
screen = GeometryScreen(
    q, repo, budgets, reach_ratio=.03, reach_safety_factor=.992,
    amplitude_top_radius=2, amplitude_top_distance=4)
~~~

完整真读：

~~~python
geometry = screen.scan(x, witnesses, radius_witnesses)
~~~

完整行：

~~~python
C, b, metadata = screen.build_rows(
    x, coordinates.transpose, coordinate_size=q.free_size,
    witnesses=witnesses, radius_witnesses=radius_witnesses,
    current_geometry=geometry, matrix_workdir=runner_scratch,
    max_rows=192, active_band=.025, block_columns=32768)
~~~

schema 为 complete-SO3-world-geometry-and-original-192-amplitude-rows-v1。主 driver 必须把每次返回的新位置永久并入历史，实际重读任何拒绝 trial 新增的位置，并在输出中绑定实际新 operator/source/model/parent。

本源已完成 AST、compile、重复 literal key/keyword 静态检查；solver 独立静态复核 world 幅度导数、全 grid/永久集与 mmap prefix 未发现阻断，construction 在核主 driver 接线。这些不是科学试验，不生成有限几何或连续结论。当前尚无该源的实际 Actions 返回。本入口的作用是让新的输入/表示保留完整几何与原约束，继续实际求解；它不完成题目的全域 metric、C² embedding、reach、所有 t、同固定问题精化或非平凡 held/E3 责任。
