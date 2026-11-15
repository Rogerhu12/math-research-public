# R282 同场局部 owner 与完整 mixed 组合器

2026-11-15，geometry，AI 辅助研究。**状态：两份独立 source-only 实现；只有 AST、源码和身份核，没有实际场计算。** 原已冻的活动、两帽、mixed/R281、shared loader 及全部求解源不改。当前没有实际接受场，故不存在可以提前填入的场 SHA、$m$、通过 rank 数或全局结论。

证明见 [R282](../results/R282-local-cross-Gram-cuff-charts-and-complete-phase-responsibility.md)。本实现补其真实常数、材料图 membership 与完整逐叶责任生产者；不增加求解接受门，也不等待 fixture 作为证明或发布门。

## 1. 两源与依赖边界

| 新源 | 职责 |
|---|---|
| geometry_20261115_local_cuff_cross_gram_owner.py | 从同一 ExactFiniteField 的完整 collar、共享 B 和原 marker 定义形成有理常数；对真实空间—相位闭叶验证共同材料图 |
| geometry_20261115_local_mixed_phase_cover.py | 继承原 mixed 输入 binding 和完整 rank；两 RP1 根域与全部空间闭区间 DFS；保原 R281 OR，完整记录未决叶与未访问 rank |

两个入口实际计算的入口均要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public。科学依赖在这一条件之后才加载。本次没有 import 两新源或其科学依赖来执行任何函数。

组合器明确 pin 新 owner 的完整 SHA，以及原 active/mixed/cap 三源。再调用旧 mixed.load_phase：该原函数核原 R281、R280、R62、shared cover、full cover、v3 cover 和 active/cap 的源。随后调用旧 active.initialise_runtime：该原函数核 shared assembly、normal form、saved prefix、large-core assembly、inlet、full cover、refined tail、refined closed assembly、R62 的完整源。

原 shared loader 自己的 check_sources 及原 full-bundle/accepted-tail 来源检查继续完整执行，包括其原 lifted-modes 源和原恢复的 source-topic 依赖。没有复制一个简化 loader 来跳过真实接受、完整 native response/J/audit、H、均值、配准、原配置或 source 检查。所需 numpy/scipy/python-flint 等运行时继续用原 closed/shared 链的实际固定环境；新额外区间算术只复用已冻 active 的 Arb API（原接口为 python-flint 0.9.0），未替换数值库。

随附源级回执把上述新入口与已有明示 verifier 的源 pin 合并列明。它区分直接入口 pin、旧明示 verifier 闭包与原 loader 继续承担的完整原生来源责任，不把一个缩短的依赖列表冒作全部旧科学来源。

## 2. 同场恢复与实际输入

组合器首先复用已冻 complete_mixed_phase_component.bind_inputs。实际输入仍为：

1. 已冻活动结果及其实际 SHA，连同原 input-binding、exact-field-expression 和完整活动流。
2. 已冻完整两帽结果及其实际 SHA。
3. 同一场的原 shared continuous cover 结果及其实际 SHA。
4. 与活动 producer 同一批真实 shared/source closed 目录、shared B descriptor、accepted checkpoint、port/config、最终 native tail response、完整 radial readout 和原 source-topic。

原 active/cap/cover 的完整 field binding、mean/SE2、B/帽参数、轴和原 $\tau$ 按原 binder 核对。组合器在同一原 load_shared_bundle 中恢复 ExactFiniteField，比较完整 field.binding 与准确表达式元数据。它不把旧 field 标签贴到新重建值上。

原 expression 的 native 完整节点表是准确有限场身份的一部分。每次懒读取 FFT 节点后，组合器核当前完整 node record 与该原表逐项相同。若需要的节点缺少原身份或字节身份改变，保存失败，不能重标另一个有限场。当前 local 常数只需原 node(0) 的完整三阶节点数据；后续非局部子 cell 求值可能读其它实际原节点。

同一固定帽源的 bind_geometry 重新读取真实 plan/assembly 并核回旧 cap.input_binding；这保留原 marker 的全部图参数，未用另一组拟合参数或名义 kappa 替代实际导数。cuff 半径、共享 B 的准确 $H,0,0$ 节点与同场帽高一致。

## 3. 常数生成的完整数学范围

局部 owner 只读取原 tail_coefficients(-1)，保全部频率、三坐标、实虚两部分和六个幂系数。左端 $0/1/2$ 为零和 B 首端 $H,0,0$ 是原准确 Hermite 定义的身份条件。它不把原有限 Gauss 的 ap 标签当作几何背景的导数。

用 R62 的有理平方根上界，逐 $j,k$ 形成完整复三向量系数的上界 $\nu_{jk}$，再得到 R282 的 $L_j,T_j$。原均值零模与 Nyquist 均保；payload 字段明确为 zero_mode_mean_and_Nyquist_retained，**不是将均值置零**。

每个帽侧分别使用该侧所有原 marker 的完整支撑。支撑严格位于原 cuff 内时，以有理平方根上界得到 marker-free gap。选择本地坐标宽度

$$
\delta_\ell=\frac{\min(R,h,h_B,\mathrm{gap}_\ell)}{4\,2^\ell},
\qquad \omega_\ell=\frac1{8\,2^\ell}.
$$

这些只是图宽，不改变物理场、$g$、reach 目标或原求解预算。每级完整保存 $M_r,M_\theta,E_u,E_v,\varepsilon$ 和

$$m=1-2\varepsilon-\varepsilon^2.$$

严格 $m>0$ 才给 local constants certified。支撑不符合或资源级数用完只令本 local 分支未决，原 R281 分支仍可使用。R282 已证明真实有限系数及严格支撑条件下，提高级数和平方根精度会在有限级获得正余量；本次没有为任何实际场运行或预填这一余量。

## 4. 每闭叶的共同材料 membership

活动根域读取真实 closed_radial_interval 与 closed_normalized_physical_angle_interval，后者是 $q$，$\phi=2\pi q$。帽根域是 parameter_box_xy 与原 closed disk 的交集。

local 只处理同侧 collar/cap，要求整个活动径向子区间进入 $[R,R+\delta]$、整个帽子域进入 $[R-\delta,R]$。帽的径向下界可用完整 Cartesian box 的准确最小半径平方；帽上界来自始终保留的原 disk 交集，不能错误要求外接 box 本身完全位于 disk 内。

每叶从帽 box 的有理中心形成一个准确 RP1 有理单位向量 $e$。它不必是帽面上的点，也不先假定它的方向正确。图中心取法只是一项确定的搜索选择；**真正的支付条件**是两侧所有允许点的三个严格扇区不等式：

$$e\cdot z>0,\qquad
\omega(e\cdot z)-e^\perp\cdot z>0,\qquad
\omega(e\cdot z)+e^\perp\cdot z>0.$$

帽侧按完整 box 的线性式准确取下界。活动侧使用

$$z=R_\alpha e_{\Phi(2\pi q)},$$

保原全部 core 和完整 Arb 闭区间；不使用变形后 XY 的方向、不令 $\phi=\theta$，不数值反解材料角。

物理角 phi 与材料角累加量在代码中使用分离的值和普通加法；不依赖扩展区间类型可能存在的原地加法/别名行为。相位的 $\cos\alpha,\sin\alpha$ 用原 t/u 两图的有理式。区间 $z^2$ 的上下界由实际同一个相位变量的准确平方范围形成，分母保持正的 $1+z^2$；这与交叉 Gram 中两个独立变量的区间乘积不是同一问题。

圆周图中心不需要预先生成采样 atlas。每条成功叶自己保存准确中心、严格余量和整个 leaf 域；最终完整叶覆盖本身就是所用有限图的覆盖证据。闭端点、$q=0/1$ 的原周期身份及原 cuff 商识别均保留。局部门证明的是所有不同材料点的非零切向弦，不通过像距离接近来删除点或 rank。

## 5. 全部 rank 和闭空间—相位 DFS

仍按原 rank=$iN_C+j$ 枚举全部原活动 cell 与全部帽 cell。每个 rank 有 t/u 两个完整 $[-1,1]$ 根域。根域还保该 rank 的全部活动 r/q 和帽 XY 空间 product。

一个叶依次尝试：

1. 准确空帽 disk 交集，只有完整 box 最小半径平方严格大于 $R^2$ 才能判空；切圆边界不删。
2. R282 local 常数与完整共同材料图 membership。它不依赖先有原单位法向球，因为真实正交叉 Gram 本身已给该图正则性和两端非零切向量。
3. 原 R280/R62 整圆 OR；其中原非严格整圆距离分支也保留。
4. 原 R281 catalog_for 和 strict_interval，对**当前相位闭子区间**保原 distance/moving/fixed/joint 四门 OR。

若需空间细分，活动子 cell 仍调用原 active.certify_cell 求同一准确有限场的完整六 jet/真实归一化法向球；固定帽子 cell 仍用原 cap.cap_cell 对同一图作包围。没有重求 native、重算目标 $g$、截掉 Fourier 模或换一组节点。新子 cell 的精度、范围、完整返回值及来源写入临时账。原整 cell 球在适用时直接复用；只细分相位时不必重复形成相同空间球。

未决节点按 r、q、cap-x、cap-y、phase 的确定顺序循环二分。两子域闭且并为父域，公共端点重复覆盖。每个叶保存真实 owner 或具体未决原因；一个 local 叶不能支付其原 rank 的其他空间或相位。

DFS 预算用完时，全部剩余 stack 节点作为完整未测试终端域保存；不是只保若干最坏例。之后保原 rank 的精确未访问后缀。只有两图所有叶均已支付，当前 rank 才完整支付；只有全部原 rank 均已支付，complete_mixed_component_paid 才为 true。

新结果仍不自动支付 whole-surface curvature、active-active、fixed-fixed、中央/远端接缝、同 $g$、held 或 $\delta_E$。full_surface_certified、actual_reach_certified、task_completed 保 false，原 static+R24 全部责任保留。

## 6. 完整 CLI

以下全部大写参数均须由实际原运行产生；当前不填未来 SHA：

    python computations/geometry_20261115_local_mixed_phase_cover.py \
      --directory ACTUAL_SHARED_RENDER --basename surface \
      --source-directory ACTUAL_ORIGINAL_RENDER --source-basename surface \
      --descriptor ACTUAL_SHARED_BACKGROUND_DESCRIPTOR \
      --checkpoint ACTUAL_ACCEPTED_COMPLETE_PREFIX \
      --port ORIGINAL_PORT --config ORIGINAL_NATIVE_CONFIG \
      --tail-response ACTUAL_FINAL_NONLINEAR_AUDITED_RESPONSE \
      --complete ACTUAL_COMPLETE_RADIAL_READOUT \
      --source-topic ACTUAL_RESTORED_ORIGINAL_SOURCE \
      --active-result ACTUAL_ACTIVE_RESULT \
      --active-result-sha256 ACTUAL_ACTIVE_RESULT_SHA \
      --fixed-caps ACTUAL_FIXED_CAP_RESULT \
      --fixed-caps-sha256 ACTUAL_FIXED_CAP_RESULT_SHA \
      --original-cover ACTUAL_SHARED_COVER \
      --original-cover-sha256 ACTUAL_SHARED_COVER_SHA \
      --precision-bits 192 --sqrt-bits 128 \
      --max-depth 25 --max-constant-levels 32 \
      --max-nodes 1000000 --max-pairs 1000000 \
      --cache-entries 32 --budget-seconds 3600 \
      --out "$RUNNER_TEMP/complete-local-mixed-responsibility"

code-directory 默认新入口所在 computations 目录，也可显式给出该目录。原 loader 所需 directory/source-directory、两个 basename 和 descriptor/checkpoint/port/config/tail-response/complete/source-topic 键逐项相同；没有另造 loader 参数别名。根 cell 深度来自实际 active result，不接受覆盖它的另一个输入 depth。

这里列的是明确的资源默认值，不是将来 workflow 已选择或实际耗费的预算。未付预算不改变科学真值；消费者不会降低原门槛来制造成功。未派发本入口或任何 fixture。

## 7. 临时输出与范围

入口输出 result.json、input-binding.json；完整可重算数据统一置于 large-arrays/：

| 文件 | 内容 |
|---|---|
| complete-collar-coefficients.json.gz | 同场完整实/虚/Cartesian/power 系数、准确 B、原 inner FFT 身份 |
| local-cuff-constants.json.gz | 全频率上界、两侧全部常数尝试和实际严格余量 |
| complete-space-phase-responsibility.jsonl.gz | 全部 rank 根域、真实空间球/原相位目录、每次 split、所有终端叶和 pair-end |
| actual-used-FFT-node-identities.json | 本次实际懒读节点对原准确场的逐项身份结果 |

catalog 的空间 key 包含准确空间范围、实际区间精度和平方根精度。计数器区分原整 cell 复用、真正新子 cell 求值与空间—相位节点数。预算停止的未决 stack 与未访问 suffix 都保，不从少量例子推完整性。

数学/输入/运行异常保存 failure.json 和已有完整临时流，不把异常冒为几何反例或完整通过。科学进程仍报实际异常。result 的 completed 表示本入口已正常收尾，完整数学 component 另由专门布尔值与完整未决计数决定。

所有这些临时输出都是可重算数据，按 README 第 15 条不入 Git 或 Release；只保源码、参数、真实 run、输出 SHA 与紧凑 stdout/结论。当前只有源和本接口，没有结果 payload，也没有 SDK/存储操作。

## 8. 最后源差异与本次静态范围

相对 root 已读的 15,289 B / 28,501 B 两草稿，最后只做：

- coefficient payload 字段改为 zero_mode_mean_and_Nyquist_retained；
- 物理 phi 与材料角累加值明确分离，去掉对区间对象原地加法行为的依赖；完整 Phi 公式不变；
- 完整性说明字段限定为 processed_pair_phase_roots_and_closed_spatial_endpoints_accounted_for，未访问 rank 由显式 suffix 负责；
- combiner 回填新 owner 的最终 SHA。

两份完整 unified diff 一并提供。全部源只有 AST/文本检查，未 import 科学、未实例化 field、未计算任何示例或真实系数、未执行 Arb/FFT/Sturm、未 Git mutation。旧冻结源保持原 SHA。R282 证明的独立登记不依赖本实现运行。
