# 同一准确闭场的分片曲率与完整像尺度账

作者：ChatGPT（geometry agent，AI 辅助）。日期：2026-11-15。

**状态：独立 source-only 消费者及其完整数学责任说明。** 没有实际接受场，没有运行本入口，没有新曲率、直径、reach 或 metric 数值。旧源、求解门、参数和原 $\tau$ 均不改。新文件为 geometry_20261115_shared_curvature_diameter_budget.py。

## 1. 已有入口与实际缺口

本次先对照当前 open 第 3、4 项，并阅读了以下已实现入口，避免重复：

| 已有入口 | 已付责任 | 本次不重复的范围 |
|---|---|---|
| R251 / geometry_20261114_full_prefix_operator.py | 同一原 scalar 的完整 prefix 相对 Gram 四正性；明确 finite-Gauss 真实函数及 scalar 包络 | 不重做 prefix 证书、旧解析 fixture，或以 $B'$ 改目标 $g$ |
| R279 / geometry_20261115_shared_active_interval_balls.py | 同一准确有限表达的全部六 jet、正则法向球；指定 $K$ 时逐闭 cell 的真实 R279 区间 | 不重求 jet、FFT、native 或另一条曲率公式 |
| geometry_20261115_fixed_cap_rational_balls.py | 原实际两帽完整 Cartesian disk cover、真实 graph 位置/法向球和各 cell 的 Hessian 上界 | 不重造帽、替换 stored height/radius 或把另存 kappa 当导数 |
| shared cover / shared held 两入口 | 同场绑定、原全对/static+R24 路线、整像 held 距离及原阈值消费者 | 不把样点或另一组场接进已有结果，不把 reach 通过当 held 的前置门 |

活动结果仍明确 full_surface_curvature_certified=False；原 cover/held 使用的连续 $K$ 和完整像 $D$ 仍含外部包络责任。现在已有完整的正确位置球、活动 R279 记录和帽的真实 Hessian，缺的是一个**同场、完整覆盖、不改变尺度定义**的汇总器。

新入口只补这一步：流读全部已生成的 active cell，完整核对两帽的闭 disk 分区，合成分片曲率界和完整相位零像的直径上界，再与实际原 $\tau$ 比较。它不证明全域 C² 接缝、嵌入或 reach，也不把条件假设换成 schema 布尔值。

## 2. 准确对象与来源

设实际有限表达的活动相位零像为 $A$，两帽实际带 marker 的固定像为 $C$。沿原 producer 已绑定的同轴族，

$$
F_\alpha(M)=R_\alpha A\cup C,
$$

其中材料移位是原同一完整材料圆的重参数化。$R_\alpha$ 绕原 $z$ 轴；没有把旧静态 point pair 的某一端临时旋转。

README 的尺度始终是

$$
D_0=\operatorname{diam}F_0(M)=\operatorname{diam}(A\cup C).
$$

本入口另可给所有相位共用的上界 $D_{\mathrm{all}}^+$。它只是 $D_0$ 的一个保守上界，**不把 $D_0$ 定义改为全相位直径上确界**。未标记基面 $A\cup C_{\mathrm{flat}}$ 的账另存，绝不将其直径冒作 README 的完整带标记 $D_0$。

输入沿已冻 mixed consumer 的 bind_inputs，为三份真实结果及它们的实际 SHA：

1. --active-result：675ab8df 定义的完整准确表达 active component，连同它所引用的 input-binding、exact-field-expression、完整 gzip cell 流。
2. --fixed-caps：a3ada50b 的完整两帽结果，包含实际 marker 参数、两侧全部闭 disk cell 及准确省略域。
3. --original-cover：同一 shared field 的原 continuous cover。只继承它的实际场身份、原 marked $\tau$、原 unmarked base $\tau$ 与原 $K$ 等已打印字段，不要求它已通过 reach。

该 binder 已核完整 checkpoint/config/tail/complete readout、原 port、全部 closed bundle、mean、唯一 SE(2)、R249 身份、共享 B、同一轴和原 family 定义。新入口不再次实例化场或运行 loader，不借此制造新的 native 接受。

新入口完整绑定实际 finite-expression 身份，保实际完整节点表和原 literal_reflection_trace_conditions。这些信息会原样列入 seam 责任，但不因存在字段就宣布全域 C²。

## 3. 全部活动闭 cell 的 R279 汇总

活动完整区分仍是两个反射 sheet、每个准确径向 piece、所有原深度下的闭径向和物理角 cell。复用原 active_rows 的逐 ordinal/范围核，不只取正常返回、最坏点或已通过子集。

活动 proposal $K_A$ 只从该实际 producer 的 parameters.curvature_upper 读取，没有另一个新 CLI 选择 $K$。若该运行未请求 R279，本入口仍可完成位置尺度账，但活动曲率责任明确未付。

每个 cell 必须有自己的原 $K_A$、原正的叉积平方下界，以及 R279 两个区间 $A_{K_A},B_{K_A}$ 的严格正下端点，才能计为已付。只检查原已生成的这些记录；不在这里重算六 jet 或区间多项式。

只在所有计划中的闭 cell 都已读到并已付时，得到各活动闭片上的

$$
|\kappa_i|<K_A.
$$

粗区间未通过仅为 unresolved；没有 R279 记录或原异常也保原范围。资源结束或 producer 自身 partial 都保确切未访问 ordinal 后缀，不用部分最大值替代全域。

## 4. 两帽完整 Hessian 到主曲率

### 4.1 原实际图函数

每个 marker 仍是原 stored height/radius/center 定义的准确实函数

$$
b_j(x)=a_j\left(1-\frac{|x-c_j|^2}{r_j^2}\right)_+^4.
$$

上帽为 $(x,y,H+\sum_jb_j)$，下帽为 $(x,y,-H-\sum_jb_j)$。任意有限 $H$ 都适用于以下局部图结论；不增加正 $H$ 门。原 accepted loader 自己的几何要求仍保留。

以 $u=|x-c_j|^2/r_j^2$ 记支撑内部径向变量。Hessian 的两个特征值是

$$
-\frac{8a_j}{r_j^2}(1-u)^3,\qquad
-\frac{8a_j}{r_j^2}(1-u)^2(1-7u).
$$

在 $0\le u\le1$ 上两者的绝对值均不超过 $8|a_j|/r_j^2$。第二项的非平凡部分可直接验证：当 $u\le1/7$ 时显然不超过一；当 $u\ge1/7$，令 $v=1-u$，待估量为 $(6-7v)v^2$，在 $[0,6/7]$ 的最大值为 $32/49<1$。支撑边界二阶导数连续为零，闭边界包含在此界中。

对一个完整帽 cell 的外接闭矩形，保留所有支撑与矩形相交或相切的 marker。三角不等式给

$$
\|D^2b\|_{\mathrm{op}}\le
K_C(\mathrm{cell})
:=\sum_{\text{touching }j}\frac{8|a_j|}{r_j^2}.
$$

允许 marker 支撑相互重叠。新入口按原参数与该完整矩形的准确距离重建 touching 集合及此和，核回原 cell 的 Hessian 记录；不采用独立打印的 nominal kappa。

### 4.2 主曲率界

对任何图 $G(x,y)=(x,y,b(x,y))$，

$$
Q=I+\nabla b\,\nabla b^T\succeq I,\qquad
II=\frac{D^2b}{\sqrt{1+|\nabla b|^2}}.
$$

对称形算子代表为 $Q^{-1/2}IIQ^{-1/2}$。因此

$$
\max_i|\kappa_i|
\le
\frac{\|D^2b\|_{\mathrm{op}}}{\sqrt{1+|\nabla b|^2}}
\le\|D^2b\|_{\mathrm{op}}
\le K_C(\mathrm{cell}).
$$

下帽只是对应空间反射，绝对主曲率界不变。这是**非严格**上界，不能把其中的 $\le$ 改标为 $<$。

### 4.3 完整闭 disk，而非 cell 样本

原帽域是 Cartesian box 与 $x^2+y^2\le R^2$ 的交集。新入口逐 quadtree 路径重建准确 box，核两帽保留同一完整路径集。只有最小半径平方严格大于 $R^2$ 的闭 box 才能省略；等号切触保留。

所有保留与省略叶必须 prefix-free，且在共同最大深度的四进面积权重之和恰为根的权重。有限个闭 quadtree 叶由此覆盖整个根方形，进而包含完整 disk。上下帽使用全部保留叶，公共边界有意重复覆盖。

于是

$$
K_C^\pm=\max_{\text{该帽全部 cell}}K_C(\mathrm{cell})
$$

是完整两帽各自的主曲率上界。与活动结果合并后，

$$
K_{\mathrm{charts}}=\max(K_A,K_C^+,K_C^-)
$$

支付全部已声明闭参数片的非严格绝对曲率界。

## 5. 从分片界到整个 C² 闭面：明确保留的条件

如果该同一实际场的全部 C² 拼接已在真实共同图中成立，连续性把上述闭片界传到所有接缝，故整个闭面的绝对主曲率不超过 $K_{\mathrm{charts}}$。再在 R248 的实际完整材料圆、活动像旋转、两帽固定及全相位 cuff 条件下，同一个界适用于全部相位。

此处没有新的条件定理缺口；所缺的是具体场的接缝证据。新消费者**不冒充该证据的生产者**，因此结果中始终保留：

- all_closed_chart_curvature_bound_certified：根据全部真实 cell 的结果填写。
- actual_seam_responsibility.global_C2_seams_discharged_here=False。
- full_surface_curvature_certified=False。

它列出真实 expression 已保存的三个 reflection trace、完整材料密度下界与准确节点/patch 身份，同时保留径向共同节点、外 cut 的合法共同坐标、反射入口、完整材料角、cuff 与 marker 支撑的实际全域责任。没有收到独立实际 seam 证据时，不从 schema、浮点 mesh 连通、正常法向球或单个窄局部图推全域 C²。

这一分离不新增求解 gate。之后实际 seam 证据与本分片结果组合即可支付其逻辑结论，不需要为了“获得 true 标签”重跑本入口。

## 6. 正确完整位置球到 $D_0$ 上界

设已付的完整位置球为

$$
F_0(U_i)\subseteq \overline B(c_i,e_i).
$$

球中心无须属于场或其参数 cell。新入口保留全部活动和两帽域，不取 renderer 顶点的直径。

每个球给各坐标区间 $[c_{ij}-e_i,c_{ij}+e_i]$。活动 producer 的原 Cartesian 位置 box 也是同一点集的包络，可取二者交集。帽则可用其真实参数 box 的 $x,y$ 区间，及图函数的 Lipschitz 竖直包络再收紧。帽的矩形中心即使在 disk 外仍合法：准确图定义在整个平面，其与域内点的线段留在这个矩形内。

对全部实际域取坐标下界 $l_j$、上界 $u_j$。则

$$
D_0\le D_{\mathrm{box}}^+
:=\sqrt{\sum_{j=1}^3(u_j-l_j)^2}.
$$

这里仅对真实位置球作有限合并，不要求曲面已浸入或嵌入。完整像仍是同一被绑定的有限场之全部参数像；不能将这一个尺度结论改说成拓扑闭合或 C² 已证。

再令

$$
R^+=\max_i(\,|c_i|+e_i\,),\qquad
P^+=\max_i(\sqrt{c_{ix}^2+c_{iy}^2}+e_i).
$$

原活动像绕同一 $z$ 轴转动保范数、水平半径和 $z$ 坐标；帽固定。因此对所有相位，

$$
\operatorname{diam}F_\alpha(M)
\le2R^+,
$$

$$
\operatorname{diam}F_\alpha(M)
\le\sqrt{\,4(P^+)^2+(u_z-l_z)^2\,}.
$$

第二式仅使用水平圆柱中两点距离不超过 $2P^+$、竖直差不超过 $u_z-l_z$。据此取

$$
D_{\mathrm{all}}^+
=\min\left(2R^+,\sqrt{4(P^+)^2+(u_z-l_z)^2}\right),
$$

$$
D_0^+=\min(D_{\mathrm{box}}^+,D_{\mathrm{all}}^+).
$$

所有平方根使用原 R62 的准确有理上界；若平方根恰为有理数则保准确值。有限精度只会向外，不把浮点平方根当严格上界。

注意 $D_0^+$ 可能保守。没有保证它足以支付未来某个实际 $\tau$；失败只说明这组已存包络尚不足，不能据此推原几何失败。也不能因保守就重新选择原 $\tau$。

另有原未标记基面账：复用同一活动球，帽换成它们真正的原平圆盘 $(x,y,\pm H)$，用准确 disk 位置界。它只服务原 static+R24 的尺度说明，字段明确不是 README 的 marked $D_0$。

## 7. 原 $\tau$、局部曲率预算和其余责任

原 marked target $\tau$ 按 original cover 的**实际 binary64 值**精确提升为有理数。README 比例则保持准确的 $3/100$，不拿浮点乘法打印值当等式。

本入口记录

$$
\tau-\frac{3}{100}D_0^+,
\qquad
K_{\mathrm{charts}}\tau.
$$

若第一式非负，则已有这个充分尺度关系：

$$
\tau\ge\frac3{100}D_0.
$$

但这不表示 reach 已经达到 $\tau$。第二式小于一仅支付相应局部曲率半径预算；还必须保全部实际 C²/浸入、全对责任、R241 嵌入与 double-normal 证明。源码同时记录严格 <1 与非严格 <=1，不把原边界情况偷偷改成新增严格门。

原 unmarked base 的 $K$、required unmarked $\tau$ 及它们的准确乘积也逐原字段保留，绝不被新 marked $K_{\mathrm{charts}}$ 覆盖。若新分片曲率 proposal 与原 cover supplied $K$ 不同，只报告真实身份不一致；不换原静态/R24 输入。

相同地，旧 cover 的 marked diameter 上界与本次独立 $D_0^+$ 的比较只是说明：当后者不超过前者时，它可独立支付旧上界的保守性；否则不下结论。

所有 continuous_reach_interval_certificate、all_phase_embedding_certified、held_or_delta_E_certified、all_domain_relative_metric_certified、task_completed 均不由此汇总器改为 true。

## 8. 最小实际 CLI 与依赖

没有未来结果 SHA 可填。实际执行时：

~~~bash
python computations/geometry_20261115_shared_curvature_diameter_budget.py \
  --active-result ACTUAL_ACTIVE_RESULT \
  --active-result-sha256 ACTUAL_ACTIVE_SHA \
  --fixed-caps ACTUAL_TWO_CAP_RESULT \
  --fixed-caps-sha256 ACTUAL_TWO_CAP_SHA \
  --original-cover ACTUAL_ORIGINAL_SHARED_COVER \
  --original-cover-sha256 ACTUAL_ORIGINAL_COVER_SHA \
  --sqrt-bits 128 \
  --max-active-cells 1000000 \
  --budget-seconds 3600 \
  --out "$RUNNER_TEMP/same-field-curvature-scale"
~~~

--code-directory 默认本源所在 computations。它不需要再传 native seed、全 J、原 solver 参数、场的 $K$ proposal、新的 $\tau$ 或任何 synthetic fixture。

三个直接 source pin：

| 源 | SHA-256 |
|---|---|
| complete_mixed_phase_component | dbdedb450ca2280f37802258377e5fd8728b9f20ce2545f22ec141b6965bc3ed |
| fixed_cap_rational_balls | a3ada50b5389a075f1da2d2237269a1a1ccc83c29aa35bc889d721eac0e2552e |
| shared_active_interval_balls | 675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b |

实际导入的 frozen mixed/cap/root-R62 模块仅用标准库。复用 cap 的 load_sqrt_kernel 还核其原四个 source pin：R62 ecea0ef5...、refined tail 6b06db6c...、large-core assembly e70d27a9...、shared assembly ac635c11...。后面三者这里只核原定义 source 字节，不重新实例化 field。原 producer 的更完整 source closure 留在输入 binding，不将“此汇总器只需要七个源文件”冒成整个场只有七个来源。

入口开始要求 GITHUB_ACTIONS=true 及 GITHUB_REPOSITORY=Rogerhu12/math-research-public。有理合并、帽曲率和平方根上界只在该 Actions 入口执行。本次只 AST 和源文本检查，未执行这些函数。

资源预算在逐 active cell 前检查，前置实际绑定和完整帽分区/参数检查保原完整范围；它不是科学阈值。预算停止仍输出已付范围、准确 unvisited suffix；没有足够完整位置覆盖时，只输出 covered_subset 的包络，完整 $D_0$ 与全场共同直径字段为 null。错误保原异常及临时账，不宣称几何反例。

## 9. 输出与继续责任

结果 result.json 保紧凑计数、分片 $K$、完整尺度账、原 $\tau$ 对照及所有未付责任。completed=True 仅表示消费者正常收尾；完整参数覆盖、分片曲率和 $D_0$ 分别由自己的布尔值及未访问范围表述。

临时 large-arrays/ 中有：

- input-binding.json.gz：完整继承来源和同一准确 finite-expression 身份。
- all-closed-chart-curvature-and-position-domains.jsonl.gz：全部实际帽 cell 及逐个被读取的 active cell，含准确曲率责任和该 cell 来源 hash。

按 README 第 15 条，这些可重算输出不入 Git 或 Release，只保脚本、参数、真实 run、输出 SHA 和紧凑结论。本轮无实际运行。

该组件一旦取得真实完整原件，可立即接在既有 active/cap producer 之后，不依赖 mixed pair cover 成功，也不依赖 held 先通过。原 held 可在自己真实来源合同下消费已付完整 $D_0$ 上界；不能直接把一个数写进旧 cover 后重标旧输出。

下一条仍存在的独立责任是原全域 relative metric：R251 已付 prefix，shared-B 尾、材料 cut 和原 finite-Gauss target 的同源包络仍须据准确表达补全。此汇总器没有拿曲率、位置球或 $B'$ 来支付该 metric 责任。

参考：[R279](../results/R279-finite-field-direct-continuous-curvature-certificate.md)、[R251](../results/R251-direct-relative-operator-metric-certificate.md)、[R248](../results/R248-finite-C2-phase-family-and-global-reductions.md)、[R282](../results/R282-local-cross-Gram-cuff-charts-and-complete-phase-responsibility.md)。
