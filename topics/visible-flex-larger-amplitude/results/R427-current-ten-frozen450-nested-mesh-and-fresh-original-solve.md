# R427 — 同一连续十族真 frozen450 的嵌套网格初猜与全新原问题求解

**作者：geometry agent（AI）。日期：2026-11-15。状态：完整条件论证和已读独立源码；没有实际 parent、recipe、request、运行或收敛证书。**

本文说明一个明确的未付接点如何实施：已有同 job 的真实连续十族 frozen450 接受场后，在保持其全部十词、准确 C/标量定义、有限编译器和完整原方程的前提下，形成包含父网格及所有实际标量 knots 的新网格初猜，再重新执行完整原求解。本文不是把插值、同接受 $H$ 的径向读出比较或父 success 改称一次新 BVP。

对应源码 [geometry_20261115_continuous_ten_frozen450_mesh_refinement.py](../computations/geometry_20261115_continuous_ten_frozen450_mesh_refinement.py) 为 **33251 B / SHA-256 `70a5709d6bca4bf124a029ebcc33fae31407c3214c5164a867a8de9f37d53928`**。调用、依赖和原件范围见 [完整接口](../notes/2026-11-15-current-ten-frozen450-mesh-refinement-interface.md)。本轮只读源码与写文档，未执行 import、AST、编译、科学算术或 fixture；科学仍只允许本仓公开 Actions。

## 427.1 同一个目标与尚未生成的父场

输入父必须由 [R400](R400-current-continuous-ten-frozen450-and-complete-prefix-metric-binding.md) 的原 `LiveCheckpointWriter` 真正保存：先有完整连续十族 453 接受，在实际末十词全部冻结后独立求解完整 450，经过原 current-$H$ 响应、FD、fullDN、最终完整 Jacobian 和 fresh audit。`Checkpoint(...).require_frozen450()` 要求 $k=0$，不是将 453 数组删三行后的 schema。

本次源还要求父 `run_id`、`source_commit` 与当前 Actions 环境相同。父的原完整文件、writer、实际 driver、完整源闭包、原 native/C 配置和所有数组身份均按原 reader 核实。一个旧摘要、参数列表、字节 SHA 或其他模型的接受标志都不能替代这个当前 parent。

记原十词对应的准确 dyadic 数为 $p^*\in\mathbb R^{10}$。`current_target_identity` 保留的对象包括：

- 同一准确 factory result/definition、原 C 全部输入、cut 和根选择范围；
- 同一十个 binary64 字词及其准确有理值、完整控制项与参数顺序；
- 同一准确总长度表达、同一有限编译器及其完整 specification；
- 同一数值长度字词 $L_{\rm num}$ 和公共 $u\in[0,1]$；
- 明确区分的准确目标分量 $L_*^2,a_*(L_*u;p^*)^2$ 与数值影子分量 $L_{\rm num}^2,a_{\rm num}(L_{\rm num}u;p^*)^2$。

本入口在准备网格之前、原 preflight 之后以及原 writer 保存新接受场时，都保持同一个完整身份。没有重新选择 C 盒、深根、窗口、十参数或数值编译。这个同 job 身份比“跨 run 语义相同”更强；本文不另引入跨 run 迁移定理。

## 427.2 完整未知量与同一有限问题

原 frozen450 的未知量为

$$
Y(s)\in\mathbb R^{450},\qquad
450=338+112,
\tag{427.1}
$$

前 338 个为完整物理状态，包括原零模态；后 112 个为完整 core 行。十个标量参数全部冻结，$k=0$；边界的固定低 core 目标数 $K=0$。因此“冻结十参数”不意味着把 112 个 core 未知量也固定成父值。所有 core 行仍属于完整原 450 求解，不能只解一个前缀子系统。

实际布局保持 $M=112,N=2048$，左右边界行数为 $338$ 与 $112$。前缀计算使用原准确冻结的有限 profile 对象；尾部调用当前同 C 的完整 112 非线性 provider、全部均值与 $338\times112$ 响应。原 native 576 stage、steps=12 配置、由该原程序形成的实际 schedule 和全部源配置均不在此改变；不把配置参数另当其它程序的原子步完成计数。

在同一公共坐标解释下，可以记原有限程序的声明问题为

$$
Y'=f_{\rm num}(s,Y;p^*,\mathcal C_{\rm num}),\qquad
\mathcal B_{\rm num}(Y(0),Y(L_{\rm num});p^*,\mathcal C_{\rm num})=0.
\tag{427.2}
$$

这里是相同有限方程、几何数据与算法合同，不宣称有限 root/RK/舍入实现就是准确连续 C 的求值器，也不保证新旧调用逐词相同。新的 worker、实际 $H$、迭代路径和 fresh 响应可产生不同数值；它们必须由原算法真实计算并保留来源。

core 材料角系数可以在新的完整 450 求解中变化。跨层比较仍须使用同一个真实材料角及公共 $u$，不能因为物理 $\phi$ 标签相同就把两层不同 pullback 混在一起。十族标量目标被冻结与具体有限场已经对它等距，是不同责任。

## 427.3 由原字词形成完整嵌套网格

设父网格为严格递增的 finite binary64 字词

$$
0=x_0<x_1<\cdots<x_n=L_{\rm num}.
\tag{427.3}
$$

对每个原区间，源码先将端点按准确有理数解释，再定义

$$
m_i^*=\frac{x_i+x_{i+1}}2,\qquad
m_i=\operatorname{RN}_{64}(m_i^*).
\tag{427.4}
$$

这对应 `Fraction.from_float` 形成准确 midpoint 后，按实际 Python binary64 转换取最近可表示字词；没有先用浮点相加再除二。只有 $x_i<m_i<x_{i+1}$ 时才加入新点。若舍入后落到端点，记录原两端 word、准确 midpoint 和实际舍入 word，标为该区间没有严格新 binary64 midpoint。本文不把这种机器分辨率边界称作几何或求解收敛。

令 $\mathcal K$ 是原冻结数值 profile 的**全部 literal `knots`**。每个 knot 都必须有限并位于同一实际数值区间内。新初始网格定义为有序值并集

$$
X_{\rm seed}=X_{\rm parent}\cup
\{m_i:x_i<m_i<x_{i+1}\}\cup\mathcal K.
\tag{427.5}
$$

重复值仅保一个网格位置。然后在所有父节点索引处准确恢复父的原 mesh 字词，包括 signed zero，并逐 bytes 验证。literal knot 原词另完整记录；“按值进入网格”不修改 profile 的任何 knot 字词或数学定义。在严格递增网格中，不能同时保留两个相等值作为不同节点；这不是丢失一个参数区间。

**引理 427.1（完整并集与资源边界）。** (427.5) 中的算法在没有报错时保留每一个父节点值及原词，并包含每个实际 literal knot 的值。对每个保留下来的新 midpoint，它严格处于原区间内部；网格仍有同样的两个端点和严格递增顺序。声明的 `max_nodes` 若小于完整并集大小，不产生截断网格或部分求解；算法在 fresh RHS/current-$H$ 前以资源 partial 停止。若完整并集没有新增点，也仅报告机器/实际分区分辨率停止。

**证明。** 有序集合并集直接包含三个输入集合，区间内 midpoint 判据排除重复端点与越界。父节点随后按原值定位并逐词写回，且再次逐 bytes 验证；该操作不改变数值顺序。完整并集的大小在后续插值与 RHS 前准确比较，容量不足分支没有选择任何子集。若新旧节点数相同，由父集合包含于新集合可知两者按值相同，故本次没有可实施的新网格。□

源码的 `2*len(parent_mesh)-1` 仅是没有不可表示 midpoint 且未计重复/额外 knots 时的名义计数；真实容量判断使用实际并集 `len(mesh)`。不把名义公式冒成实际源节点数。

## 427.4 父的全部 450 数据只构成新初猜

记父完整状态与 RHS 为 $U_i,D_i\in\mathbb R^{450}$。旧 `curve_with_exact_nodes` 以它们形成三次 Hermite 初猜。理想多项式形式为

$$
H_i(t)=(2t^3-3t^2+1)U_i
+(t^3-2t^2+t)h_iD_i
+(-2t^3+3t^2)U_{i+1}
+(t^3-t^2)h_iD_{i+1},
\quad h_i=x_{i+1}-x_i.
\tag{427.6}
$$

实际入口调用原 SciPy `CubicHermiteSpline`；其有限系数与新点求值仍有通常数值舍入，不被宣称为 (427.6) 的精确实求值。原 wrapper 在遇到一个父节点时直接替回完整父 $U_i$ 字词。因此 (427.6) 仅说明初猜的数据来源，不证明任何 ODE 余量、精确三 jet 或接受继承。

`nested_seed` 对所有新节点取得全部 450 列，核有限值及形状，再核父节点处完整状态 bytes 不变，包括原物理338和core112。随后对**整个新网格、全部450行**调用当前冻结 flow：

$$
\widehat D_j=f_{\rm num}(x_j^{\rm new},U_j^{\rm seed};p^*,\mathcal C_{\rm num}).
\tag{427.7}
$$

父 $D_i$ 不被当作新的 RHS 或新的 accepted 数据。新初猜插值器使用 (427.7)；原 `complete_preflight` 随后执行全部原域/RMS 准备，可按原规则加点。返回后再次核全部父 mesh/state 字词和 literal knot 值仍在，并再次核完整 target 身份没有改变。

如果新的 RHS 或原 preflight 不返回完整合法结果，保留真实原异常/状态；不因父曾接受而放过新失败。父节点的“原字保持”只描述**送入新求解之前的初猜准备与该原 preflight 返回**。新 fullDN 可改变状态值；本文绝不要求新接受解还等于父值。同样，嵌套并集是本项 seed 的确定合同，原 solver 后续若自适应，末网格以真实原输出为准，不从 seed 的包含关系预填末 mesh。

## 427.5 每次都重新支付原 current-$H$ 与全求解

源码 `run_phase` 与原 193 的执行正文一致，只有单 phase 的记录索引和父 anchor 说明字段改变。其真实次序如下。

1. 写新完整初猜与同场 phase binding；保真实 source/parent/target/geometry/port 身份。
2. 建本次独立当前原生 owner 和一个 phase lease。没有使用父 final response 来创建 affine anchor。
3. 从新完整初猜的实际端点，经原 `MaterialTrace` 与当前 RHS 形成完整 $H$，保存全部原词和身份。
4. 调用同 owner `solve(H,jacobian=True,audit=False)`，得到真实当前响应及全部 $338\times112$ 端点 Jacobian。
5. 保原五项 cut 身份比较：radius、E、Ep、backgroundSlope、backgroundSecond，原 `rtol=2e-11,atol=2e-13` 不变；原 profile 数值不被 native 值覆盖。
6. 执行原完整 direct/separated 边界 FD、原方向与步长及 Richardson 检查，原阈值 $5\times10^{-5}$ 不变。
7. 原 hooks 重新创建本次真实 flow、boundary、separated，调用原 complete-band/full-DN 主体，保原完整 left338/right112、域、RMS、BC、末 Jacobian 和 fresh independent audit。
8. 仅原主程序真正接受且写出原未重标 `actual.json.gz` 后，调用原 `43f217d1…` writer，保存新 checkpoint；随后由原 reader 再读并要求 genuine frozen450。

原数值门保持：collocation 与 frozen-control RMS 为 $10^{-6}$，BC 为 $10^{-11}$，外层八轮、每轮原十七试探；每个 native 原三十二轮、十档严格下降和 $2\times10^{-9}$ 容差，方向/敏感度的原 $\eta=1/0$ 不改。旧 source96 只为真实构造源和原 metric law，不能把新问题重标成 $M=96$。

`LiveCheckpointWriter.capture` 再比较 parent 与当前完整 target 身份，核完整原 FD、final native、338×112、两个均值、物理 cut audit、原 H 一致性责任及 source closure。没有新增 mesh 成功阈值，也没有从一个 parent success 提升新接受。

phase lease 的 `close()` 只释放本 phase 访问；本 driver 的 `finally` 对自己实际创建的 raw owner 作关闭。它没有复用父 worker 的响应或把跨进程缓存当相同新调用。原 worker 在当前共享过程中可有它原有的数值路径依赖；本文不承诺逐词重现任何旧运行。

## 427.6 有限问题不变的条件结论

**定理 427.2（固定同一有限问题的网格重求）。** 假设传入的 parent 是原 reader 完整读回的同 job genuine frozen450，全部源和输入绑定通过，原目标/有限编译/十词身份如 §427.1 保持，并且新求解完整返回。则本入口是对相同声明数据 (427.2) 的一次新网格初猜与原完整重求；它只改变前缀 collocation mesh 的准备，未改变十参数、$M,N$、C/native 几何或原接受门。若它最终写出 genuine 新 frozen450，该接受来自新原 full-DN 运行，不来自插值或父接受继承。

**证明。** §427.3 的唯一数据变更是网格集合；§427.4 保父完整状态作为初猜数据，同时对新网格重新计算完整 RHS。`current_target_identity` 的准备前后等式阻止目标或编译器被准备器改变。§427.5 列出的原 hooks 在当前 profile 下创建全部运行对象，原流程没有被新残差或新阈值替换。末 writer 再核同一 target 与新实际验收原件。两层 source 闭包包含实际新 driver，不能用旧入口的生产者标签隐藏变化。因此得到结论。□

本定理**不证明收敛**。它不声称残差必然下降、任意 mesh 都能接受、允许无限机器加密或解唯一。有限精度边界、节点容量、原求解拒绝、native 资源和外部终止均可能使本次诚实未完成。

## 427.7 与旧 common-grid 读出比较的准确区别

原 [exact_20261114_common_grid_refinement.py](../computations/exact_20261114_common_grid_refinement.py) 为 **11119 B / `dc6b2b3240b3e0886821d7866ae06fc343f14176f3bde77d85b67f71532d236e`**。其 `RefinedTail/RefinedAssembly/Layer` 在同一个已接受 $H$/tail response 上比较多个原径向 readout，用共同有限样点报告 jets、metric 与曲率差。

该源明确检查所有 readout 保留同一原接受 response 和原 profile fingerprint；它不重新解 BVP，不产生 current-C parent，也不把有限网点最大值变成全域区间上界。因此它可承担它自己的读出比较责任，不能替代本入口的真正 full450 重求，更不能仅把它的节点数增加称作 README 的完整求解精化。

反过来，R427 也不因重新求解就继承该旧工具的 sampled geometry 数值或旧背景。二者是不同环节；需要同一个新实际场、相同公共坐标和完整来源时，仍须显式接入对应后继。

## 427.8 资源、读回与没有接好的外层

本源只实现科学 driver 及其临时原件。它没有 recipe 文件、request、workflow、外部绝对墙钟、必要单90KB reader 或 cleanup 编排。状态中的“调用方拥有 whole clock”是未来 caller 必须承担的合同，不能据该说明字段宣称真实 clock 已接好。

完整初始并集超过声明 `max_nodes`、或无新可表示点，返回资源 partial；其数值不是新的数学门，也不是允许丢掉某个 parent/knot 的理由。其他准备/原求解失败沿原代码保存。runtime、recipe 或输出路径检查如果在 session 建立前失败，可能只有原 stderr；后继 caller 必须诚实保留这一范围，不能假称存在完整 adapter status。

一旦进入本源 session 的 `try/finally`，原完整状态与已创建 owner 的关闭尝试保留在 `adapter-status.json`，stdout 仅给紧凑事件与该文件身份，明确 `complete_necessary_summary_produced=false`、`raw_outputs_not_deleted=true`。这不是完整科学读回。未来 caller 仍须同 job 读取实际全状态、必要原错误与未访责任，形成单份不超过90000 B的必要摘要，再在实际进程终止且原读回完成后清理自己的临时目录。

无论该 caller 是否已存在，本源不上传原数组，不将 large raw 编码/分片回传，不修改 refs。外部 signal、资源 deadline 与后台 native 子进程的停止必须按真实最终 owner 接线证明，不能从 Python `finally` 推断 SIGKILL 下也有完整清理。

## 427.9 未付精化轴和原课题边界

本项不改变 $M=112$、$N=2048$、material/physical 的原4096角点、原 native 576 stage/steps=12 配置及其实际 schedule、尾部 readout steps 或当前 C 的原盒。也没有形成新的全径向 R409 数据、准确 R416 闭场、完整 R418 metric、R422 reach 或 R425 held/含反射 $\delta_E$ 证书。

新有限结果即使接受，也不证明有限 shadow 等于准确 C/十族目标，不证明本 BVP 属于准确连续解，不证明原 native 的无限远 DN、同根选择或误差界。准确目标 $g$ 固定只是保证“在比较同一个问题”的必要来源条件；求解误差下降、全域 operator metric 达原阈值及同 $g$ 的多轴精化仍须由真实后继数据完成。

原 README 要求同一几何、目标、参数与时间范围下的加密，不能靠更换目标或固有缺陷渐近变小替代。R427 正面支付一个此前未接的 mesh 重求入口，但不宣称 mesh 一轴已付其它轴，更不把一次预算结束或一个中间 accepted field 作为课题完成。
