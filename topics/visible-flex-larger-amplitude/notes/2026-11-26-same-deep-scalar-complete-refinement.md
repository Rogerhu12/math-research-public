# 同一深谷固定度量的完整精化入口

2026-11-26，Astra-larger-e4e2a2bf-20261126 / construction。

本实现将 [R676 的准确符号节点/quintic 包含和位置迁移](../results/R676-fixed-metric-refinement-and-complete-observation-transfer.md) 用在 [R690 的新深谷固定输入](../results/R690-quasimonotone-tail-and-deep-valley-input.md) 上，接完整 q/core/H、原 H² 母范数、所有原 Gram 行、原几何 C 和已刊 v2 D/L 幅度行。它与已刊首个 deep solver 具有同一个实际目标

\[
g_n=ds^2+a_{\rm new}(s)^2d\theta^2.
\]

本条是可执行实现和精化语义，不是已返回的数值精化结论。没有在本地执行场、Gram、J/J*、区间证明或数值 fixture；根已收到实际 deep 首批末态 `b788c32879aa5ff5ff3d5f2ed81b92205b54fc0da61a1a2b84ace8345a3f22eb`；现有 ready 入口使用该父所在路径。其直接来源准入仅为原 d3 完整体或本 fine 完整体；后续新增 SOC 父必须另付完整 source 绑定，不能冒用原 d3 身份。何时执行仍由真实误差、Pg/tolerance 和回溯结果决定，不因源码就绪自动多跑粗场。

## 1. 不随精化改变的数学对象

固定 profile 的 canonical definition 和其独立哈希保持逐字相同；当前 R690 profile identity 为 `383168fbd269d52a16586fca626632c28243bf230df62a5882e7ed2048625d7d`。原解析输入、准确 S、新 a/I/R 的完整公式、固定 core 前三个系数、width、lambda=1、物理 eta 起终点及帽配方不变。增加积分精度或改变完整尾包围的工作 cutoff 不改变 profile；所有未细分的无限尾都必须仍在完整误差盒内。

对于 eta，固定的是两端的准确仿射符号 `alpha*S+beta`。一轮径向二分把原 eta 起点索引 885 映射为 1770；这只是该实例的映射，不是可在后续轮次硬编码的常数。coordinator 从真实 `refined_model.eta_start_node` 读取细层索引。起终点 symbolic 定义与父模型逐字核验。

本条固定 g 的数值问题保留父当前 R 的 binary64 字面 carrier。新完整标量 oracle 仍重新求同一准确 R 的包围，并针对这个实际保存的旧字面 R 支付误差；不会因为 300 秒积分的叶集略有不同，就悄悄换帽界面的数值半径。真实准确 R 仍是 R690 的同一个数。

## 2. 完整 transfer-only

`refine_fixed_deep_scalar.py` 只调用字节冻结 R676 源中的纯限制、误差和地点函数，不调用它的旧 scalar `main`、旧 `prepare_scalar` 或硬编码 p8 的 `CommonGridReadout`。新父通过新 factory 的正常 `from_files` 读取。已核对的实际 dense/batch/observed 源绑定完成后，父 canonical definition 必须完整相等；此步不创建或重算父场。

q 的纯径向 Reader 使用当前新 profile 的准确 S/R 盒，只供通用 Hermite/Bernstein 公式。它不会构造旧 scalar canonical reader。R676 的完整仿射接口检查保持：所有旧 q/core/H 字、固定 core、帽 q 端点和依赖的 core T 槽语义都保留。

每个旧 quintic 以准确符号中点二分。新中点的 value/first/second jets 来自 outward Hermite 盒的字面中点，并保存其真实舍入误差。新 q 是连续 C² 的 piecewise quintic；理想准确限制恰为旧 q，实际字面细场与理想限制的全角六 jet 差异按 R676 给出。若增加 M，只对新频率零填充，不删旧变量。

这里的“lift 差异为零”指同一准确深谷 profile、同一准确物理 eta、同一 core/H 的解析 lift。不同轮次的 a/I 数值 carrier 误差另行记录，不能从 q 的误差界中删除。

新观察 plan 含全部旧准确符号观测点，并增加新节点/中点和六点 Gauss 观测。旧 Gauss 正权作为明确正的混合分量保留；当前求解的径向 measure 明确采用原 Simpson 与新旧 Gauss 的混合。旧完整 measure 不被称作与细网格 measure 相同，而是在第 4 节单独原样复读。每个新、旧观察点的 a 都由新 profile 的准确点查询重算，不对旧 a 数组插值。时间与 a 的载体误差保存。I 及各一、二阶 scalar jets 由普通新 factory 在细层重建。

所有原永久曲率/半径/保护地点先在真实父 carrier 上解析，再用 R676 的准确 dyadic local-u 映射。每个不同 binary64 phi 原样保留，没有 round13 合并、大小上限或 LRU。额外位置源必须属于实际父 carrier。失败 trial、active、final、已见 SOC 地点都在 complete-history union 内。

## 3. 新节点 producer 与真实模型身份

细层 node report 使用合法的新 schema `deep-valley-fixed-scalar-symbolic-nodes-v1`，并记录本独立 refiner 的真实 `source_sha256`。不能把这个字段伪写为首 prepare factory 的 SHA。它还保存真实新 carrier/mesh SHA、完整 profile definition、准确符号 nodes、a/time 误差和原父来源。

细层 canonical definition 从父模型仅改变 M、mesh/node/observation 来源、eta 的新索引及其字面 carrier。随后普通新 factory 的 `from_files/create_pair` 独立从真实新文件重构全部 definition 并要求完整等号，最后才保存 fine seed 和 reference profiles。旧模型 guard 不改标签、不移除字段。

新连续 reader 的 `--node-producer-source` 必须传真实 `refine_fixed_deep_scalar.py`；首次 prepare 的默认 producer 是 4ae factory，不能沿用为本条。认证还须使用实际 solver 返回的新 reference carrier，不能拿父 reference array 代替细层场。当前连续 reader 的独立新 scalar/节点/观察/canonical 核验不因 producer 可选而减弱。

## 4. 同一个父测度与父字面目标 carrier

`fullclosed_refined_deep_scalar_amplitude_qp.py` 是已刊 d3 完整求解器的独立完整源码。原 J/J*、当前新 scalar coarse Gram、v5、原母范数、C 与幅度行、所有 nonlinear 真筛均不变；只加入同父比较及其明确来源。

父 report 必须实际完整，source 是已刊 d3 或本完整 fine source 的上一层；profile、physical eta、解析输入及实际源一致。父 carrier SHA、其全部正权、完整角点、父 spectral p/epsilon/scale 和 centered/uncentered evaluator 都直接核对。

同一准确 a 的新数值 carrier 可能与父 carrier 有微小不同。因此，不能直接取 fine residual 的子数组就称作同父数值问题。设细层在父准确符号点与父角点上的已有 raw residual 为

\[
e_f=|F_s|^2-1,\quad f_f=\frac{F_s\cdot F_\phi}{a_f\rho},\quad
d_f=\frac{|F_\phi|^2}{a_f^2\rho^2}-1,
\]

并令 \(r=a_f/a_p\)，其中 \(a_p\) 是真实父 carrier。则同一当前物理 Gram 在父数值归一化下恰为

\[
e_p=e_f,\qquad f_p=r f_f,\qquad
d_p=r^2d_f+(r-1)(r+1).
\]

最后一式采用展开式，避免无必要地先加 1 再减 1。计算仍是普通浮点读数，不冒称 outward。当前 rho 和当前物理 F 一直相同；没有替换为父 rho 或父场。

对这些值使用父原 positive radial weights、原 quarter-orbit multiplicity、父全部角点和同一 spectral 参数，得出 `common_parent_measure`。父本身的 Phi/max 从其真实完整 final report 读取；细层值来自本来就已计算的 residual，额外父场/J/J* 调用为零。既报告细层初始也报告细层每个 trial/最终在父测度的值。

只有这些共同测度值可与父 Phi 相减。细层自己的 measure 仍用于真实细层优化，其 Phi 只能在自己的同测度初始/末态之间相减。两套读数分别存储，不把正权网格扩充造成的 objective 变化记作优化进展。

## 5. 完整求解与真实停止语义

`launch_refined_deep_scalar_actions.py` 有两种显式输入：

- `--refinement-report`：核同 g transfer 的实际 seed/carrier/node/manifest 全部 SHA，并核实际 coarse parent。
- `--parent-report`：继续本完整 fine solver 的实际末态，保同一个 fine carrier 和原 comparison-parent measure。

两种情况都用实际 fine eta 索引；额外 manifest 必须属于这个 fine carrier。transfer 记录中的父 provenance 不会被当成 fine grid 地址重新遍历。全部原几何工作行作为 prefix 保留，新增幅度地点仍在曲率与半径两套永久内存中。

`refine_deep_scalar_actions.py` 顺序执行完整父地点 union、同 g transfer、真正细层 full solve。它继承父的 spectral 参数、原正权混合比例、angular H² transition、coarse low modes 和物理 centers、原 C 工作参数、QP 容差、line-search 参数、幅度预算及实际 stopping target。默认 damping 从实际父的 `final_damping` 读取；显式 override 会单列记录，不能伪称自动继承。

方向数和 QP advance 预算可明确加大，以便实际求解而非在迭代上限处自称数值能力极限。QP 的实际 Pg/tolerance、状态、advance 和真回溯仍在完整报告中。

父已过有限几何/幅度屏是记录，不是被继承的 fine 接受条件。细层完整 driver 自己重读实际初始和所有潜在接受 trial。没有新增粗场 fixture；若实际新读数不能启动可行原点，就返回真实原因，不能宣布数学上不可能。

初始误差已低于停止参数而零步退出，也不叫持续下降。报告保 `zero_direction_exit`、实际方向/接受数、细层自身 max 改变量、共同父测度 max/Phi 改变量，并始终写 `fixed_g_refinement_convergence_claimed=False`。首设计的 5e-7、deep 初始算法的 1e-9，都不能改写 README 的原求解容差定义。真正完成仍须实际同固定问题的精化序列、有效求解精度、连续误差与完整几何证明。

## 6. 源码和执行路径

| 完整源码 | Bytes | SHA256 |
|---|---:|---|
| `refine_fixed_deep_scalar.py` | 24172 | `5f1b285fd021971cdbeb6680d28b8ef0c5ec24cdea5f9a0f830b3e87aebc06df` |
| `fullclosed_refined_deep_scalar_amplitude_qp.py` | 76811 | `1745cfae02b7ad0335577a340cfee52f179e1f27508c8d20ef1487abec00f154` |
| `launch_refined_deep_scalar_actions.py` | 24503 | `6b06187c0bd5957ff0c1658f6da7a4c7077a6b9c59ed948a5a23881b1379cd75` |
| `refine_deep_scalar_actions.py` | 17264 | `991d824531f596e82306db2bd00442e52d454e397c74941809cb4513602fbf10` |
| `read_refined_deep_scalar_report.py` | 15906 | `c0e3f6569e8a26668ea10183e2b8cb6873210c732f2f57905bb13d05dbf2b583` |

全部源码 AST/compile 检查和尾空白检查通过。pure `--print-command` 构造得到 163 个 argv、80 个唯一 flags，与完整 fine driver 的 argparse 静态比对无未知或重复 flag；该检查不读场、不运行数值 solver。R676 kernel、new 4ae/e091 factory/profile 和所有依赖逐字绑定。

已准备 `deep-fixed-scalar-refinement-ready-steps.json` 的顺序入口，供实际 deep 父 b788c328 返回后按真实求解进度选用。默认一次径向二分、保持父 M/N，2 directions × 64 advances；M、N、方向和 advance 可作为明确执行预算选择。它不默认宣布某个阶段适合精化。其路径示例为：

```text
parent:  {work}/deep-fixed-scalar-amplitude-first/
inputs:  {work}/deep-fixed-scalar-prepare-first/
plan:    {work}/deep-fixed-scalar-refinement-first/refinement-plan.json
transfer:{work}/deep-fixed-scalar-refinement-first/transfer/
solve:   {work}/deep-fixed-scalar-refinement-first-solve/
summary: {work}/postprocess/deep-fixed-scalar-refinement-first-summary.json
```

源 SHA、真实 source commit、输入和输出 byte identities、实际 scalar accuracy 与所有运行读数都由公开 `Rogerhu12/math-research-public` Actions 记录。此入口未执行时不写数值结论；实际执行若没下降、被筛拒绝或达到 advance 上限，照实登记并据此继续求解或换方向。
