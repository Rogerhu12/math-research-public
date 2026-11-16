# 原末 51 系数的整个后缀 minimax：模型合同

日期：2026-11-16。政策：true58-full51-whole-suffix-v1。
实现：scripts/frame_metric_current168_full51_whole_suffix.py。

本文件和模块只作纸面与源码构造；未作本地导入、执行、编译、测试、
数值或符号计算。实际科学调用只在本公开仓库新 Actions scope 内
发生并计费。旧 whole34 已关闭，本次不重启该问题。

## 1. 几何改变和已闭祖账

本次新增原末 51 个独立 u/v 系数中此前被冻结的 17 个 R0 方向。
旧问题在准确 R0 平面内仅有 34 个控制；新问题有全部 51 个原系数
方向。共同曲率目标仍覆盖两个原完整角网的整个 21 行后缀，不退回
终端单环，不重建旧 34 维核或旧三 jet 逆。

旧 whole34 的真实 SLSQP 返回是 status 9 / success false，
nit 120、nfev 142、njev 120，raw K 为
18.45692174062725，raw h 为 63.87343696103953；
原准确物理盒的 58、61 两行超界，没有候选、预测或 actual。
该 scope 新增 184.71003744799998 秒后，闭合祖账为
3231.8129525510003 秒 / 147 个原 full 值，接受索引仍为 58。
这些数字来自该次原回执，不是本合同重新计算。

该次 MODEL/J/TRACE 的完整正文目前无法取回。原日志 API 与 run
ZIP 只保留末尾三条记录；MODEL、NONLINEAR、SOLVE_TRACE 的存在/
大小/哈希回执不等于其数组内容。第五个日志来源只负责闭合祖账，
绝不作为本模块免费科学输入。原四个完整来源仍按固定 run/job/source
和原 JSON 身份恢复：accepted58、permanent55 构造源、free36 完整
MODEL/RING_SOLUTION、prefix102 完整 MODEL。各来源只读一次的
编排和账本由外层 transfer/scope 负责。

依据：[R514](../results/R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)、
[原 whole34 合同](true58-R1-R2-whole-suffix-model-contract-20261116.md)、
[prefix102 合同](true58-fixed-ring-prefix102-model-contract-20261116.md)、
[新 scope 设计](true58-full51-whole-suffix-design-20261116.md)。

## 2. 新 53 变量、准确注入和唯一初点

后端固定顺序为 z51, K, h。令

\[
J=(54,\ldots,80,129,\ldots,152),
\qquad
P_{J_i,i}=1/4,\quad P_{j,i}=0\ (j\ne J_i).
\]

P 是新的准确 172 x 51 注入。前 27 列为 u，后 24 列为 v。
51 个非零元落在互异原坐标行，因此准确秩为 51；不借用旧核的
浮点秩或数值同一性判据。对应的独立 168 行使用相同索引，另外
所有原系数保持 q58，原固定 g/b0 和高度不变。

实际候选按

\[
q(z)=\operatorname{RN}\bigl(q_{58}+P\,Q(z)\bigr)
\]

形成。每个输入 binary64 先转为其准确有理值，在准确有理数中
合成完整和，最后每个独立坐标只舍入一次。不能先浮点计算增量和，
不能替换成相对已舍入 q_R 的另一参数化。实际 rounded q168、对应
完整 172 物理坐标、未舍入两套坐标、舍入差和准确盒判断同时保留。

唯一初点是 z=0, K=58, h=0，准确重现真正 accepted58。
旧 free36 的未接受 q_R 只作为已付几何/标量基准，不是另一个初点，
也不是候选备用点。不运行第二个 solver、phase-I、重启或换种子。

初始后缀的严格 metric 余量只由该次必要的新初始值给出；不能从
原全域峰的位置推断其通过。若初值对新严格预算不可行，仍保持
同一个已经声明的 SLSQP 目标和约束。

## 3. 目标、原盒向内 bounds 与范数终门

目标及区间为

\[
\min(K+10^{-6}h),\qquad
1000/61\le K\le58,\qquad
0\le h\le18014398507545773/281474976710656.
\]

hmax 直接读原 free36 MODEL 已存
binding.original_box_sufficient_hmax_exact，要求与上述准确值相同；
不重新推导或计算旧 hmax 数据。K 下端点取不低于准确目标的最小
binary64，h 上端点取不高于准确 hmax 的最大 binary64。准确值、
实际浮点端点和其准确 binary64 有理值分别记入 binding。

原 172 物理盒的全部上下界仍作为 344 个线性行保留，另有 102 个
范数行及 K/h 的四个区间行，合计 450 行。范数行按原未缩放
LP_ROW_TOLERANCE 判断，不另改容差。

另给 SLSQP 接入原盒的保守逐坐标 bounds。对活动物理行 j 的
准确原区间 \([l_j,u_j]\)，令 \(l_j^\mathrm{in}\) 为区间内最小
binary64，\(u_j^\mathrm{in}\) 为区间内最大 binary64，再对

\[
4(l_j^\mathrm{in}-q_{58,j})\le z_i
 \le4(u_j^\mathrm{in}-q_{58,j})
\]

各向内取 binary64。接受态本身必须位于这些端点内。后端 z 在
该区间内时，准确未舍入候选位于两个 binary64 系数端点之间；
RN 的单调性保证其最后舍入值也在这两个端点之间，因而仍在原盒。
这些 bounds 只是同一个原盒的充分接线，不增加允许误差，不替代
终门的完整 172 维准确盒检查。

P 的 1/4 给出未舍入范数恒等式

\[
4\|Pz\|_\infty=\|z\|_\infty.
\]

但是实际 RN 后的 \(4\|q-q_{58}\|_\infty\) 可能比未舍入值大几个
ulp；原线性容差也不能推出准确 \(h\ge\|z\|_\infty\)。
本模型没有声称这些问题被 backend bounds 解决。终门另外准确
检查

\[
4\|q-q_{58}\|_\infty\le Q(h_{\mathrm{raw}}).
\]

它直接使用真实返回的 h，不能事后抬 h、替换 raw53、投影 q 或
修补盒外分量。唯一初点的真实增量与 h 均为零，因此该门不强制
初点失败；一般返回仍可能仅因 ulp 或线性容差而被准确终门拒绝。
这项保守筛选保留了原真实物理范数要求，没有将它放松为容差声明。

候选记录分别保存未舍入 norm、舍入后 norm、两种 norm 到 raw h
的准确差，以及两个独立真假值。未舍入 epigraph 的准确真假单独
报告；450 个原线性行仍按原容差筛。全部原盒、准确 K/h 区间、
两种 norm 的原 hmax 界、实际 rounded norm 到 raw h 的准确门
都必须保持，不能因 finite solver 成功而略过。

## 4. 全后缀的全部原约束

径向行由原已付 binary64 径向向量的准确有理值与 153/200 比较
得到，必须是原 21 行并含 ring 行 141。coarse384、fine768 的完整
角数组各自保持原字节和原顺序，分别使用自己的完整 Pi_N。
每点的两个原平滑 metric 行和四个原未平方 PSD 行全部保留：

\[
21(384+768)\,6=145152.
\]

加上 450 个原线性行，总计 145602 行。不使用 active-row 减行、
attainer-only 筛选、角向子网或环上多项式替代整个后缀的几何。

继续使用固定的 \(a,a_s,a_{ss},b,b_s\) 和完整位置二 jet：

\[
\begin{aligned}
X_s&=a_s\Pi T+a\Pi T_s+b e_3,&X_t&=aT,\\
X_{ss}&=a_{ss}\Pi T+2a_s\Pi T_s+a\Pi T_{ss}+b_s e_3,\\
X_{st}&=a_sT+aT_s,&X_{tt}&=aT_\theta.
\end{aligned}
\]

原 metric 是 \(e=|X_s|^2-1,\ f=X_s\cdot T\)，
\(\eta=(|e|+\operatorname{hypot}(e,2f))/2\)。
两个提议行保留原 epsilon；资格另外检查未平滑 eta 的严格预算
0.26600531463999305。外层从原 SOURCE_ETA 减去 1e-7，并与
request 的显式预算相等；模块再与 prefix MODEL 的准确 binary64
预算身份相等。

曲率保留实际第一基本形式 I、法向面积 q、分子二次形式 N，
不把 G 替换成 1。四个矩阵行分别来自

\[
H_\pm=(KqI\pm N)/c
\]

的 trace 与 determinant，c 为原 curvature scale。每个符号的
trace 门都在，没有用平方消去符号。全部后缀网还必须通过原未平滑
metric、返回 K 下四个未平方 PSD 门、独立直接主曲率在返回 K 与
hard cap 58 下的门，以及 area 严格大于原 floor。只使用原容差。

## 5. 已付输入、准确支持与必须新付的内容

三个 paid_* 参数都是原 stdout 的完整 JSON 字典。报告里的
shape/hash 元数据不能替代原数组。prefix 原 MODEL 的 JSON+LF
为 42,929,879 bytes，SHA256
64d1fdd63d339b102d0ce73f92e1f042110bc2fbe11ce95a92ec59d443663921。
外层固定原日志身份；模块核每个实际消费数组的 dtype、shape、
bytes、SHA 与已有 exact_binary64。

| 原记录 | 本次实际消费内容 |
|---|---|
| free36 MODEL | accepted58 的完整 q168/172、原目标、原已付 hmax、原末三样条准确支持身份 |
| free36 RING_SOLUTION | candidate_record 中完整 rounded q_R168 |
| prefix MODEL.new_paid_input | 原 radial/theta、固定 a/a_s/a_ss 与 b/b_s、q_R 的 u/v value/s/ss/theta、原角基/角导数 |
| prefix MODEL.fixed_suffix_full_arrays | q_R 后缀的 T、五个位置二 jet、e/f/eta、area、直接主曲率、K58 四 PSD 行 |
| closed whole34 的尾日志 | 外层闭账来源；模块不消费其缺失 MODEL/J/TRACE 内容 |

不读取 free36 的旧 P、float_P、raw36 或 z_R 来构造新坐标，
也不重做旧核、三 jet 逆或环单点多项式。新的准确 P 是 §2 的
显式注入。原末三径向 B9/B10/B11 的 value/s/ss 未存在 prefix
full input 内，因此从同一个原 quintic 对象中只评这三列，作为
明确新增工作。原 first6 径向与角基不重算。

逐行固定几何复用同时要求两个条件：仍是原已付径向 binary64 身份，
且其准确有理值不小于原准确支持右端 423/500 和原 BSpline 实际
binary64 右端。只要任一条件不满足，该行就进入新求值部分；
不以小量阈值或显示小数认定二 jet 为零。

新 value/J 只对真正可变的径向行计算。支持以外的 T、位置二 jet、
e/f/eta、area、直接主曲率和原 K58 PSD 直接拼入原已付数组。
完整 21 行仍全部进入约束。固定行的物理 51 列导数准确为零，
但当前 K 的 PSD 行和 K 导数必须重组；不能沿用 K58 的 PSD
作为其他 K 的结果。此前未存的实际 I/II 输入首次形成时单独计费，
随后缓存；已有 q_R 的 T/jets/e/f/eta/area/PSD/曲率数值不复算。

prefix 原 MODEL 未保存全 160 行的 frame/Pi/曲率派生数组。
这些缺失内容不是免费输入；旧 whole34 已丢失正文的数组同理。

## 6. 增量浮点语义和完整支持

先按 §2 得到真实一次舍入 q168，再用它相对 q_R 的实际系数差，
经原末三径向基和原角基形成标量 jet 增量，加到已付 q_R 标量场。
随后在可变行计算原完整 T/Pi/位置二 jet/metric/曲率链。

数学上仍是原标量场与同一固定 g，但浮点求和分组不等于 canonical
field.scalar_frame(q,...) 的逐项重建。definition/binding/summary
及 grid summary 明示这一差异。后缀合格只授权外部原 full-body
canonical prediction；最终 q168 的原 actual 十四门才有资格改变
接受索引。

末三原样条保持完整支持，不在 .765 人工截断。原源的支持为
B9 \([9/25,423/500]\)、B10 \([441/1000,423/500]\)、
B11 \([261/500,423/500]\)。因此原全域 eta 峰所在 .4725 落在
B9/B10 的内部，B11 在该处零；不能断言全 51 方向对该峰的二 jet
全零，也不能仅凭支持断言该峰已经下降。

支持依据：[原末径向支持记录](curvature-existing-terminal-row-support-20261114.md)
与 scripts/frame_collar_enriched.py::rational_knots。
即使后缀全部合格，原支持的重叠区域仍可能使全域预测失败；本次
可能仅为后续新的 prefix/联合问题提供实际候选坐标，而不产生 59。

## 7. 解析 J、缓存所有权和真实重复计费

新增完整 53 列 J 使用原 angular_kernels、virtual_selected_jets、
原 metric 导数、实际曲率 I/II 导数链。u 的 27 个与 v 的 24 个
物理方向最终乘对应 P 的 1/4，K 列按当前 K 的真实谱行导数形成，
h 在非线性行中为零，全部线性 J 为固定 -A。

导数含义是实际 once-rounded 场状态处连续原场的方向导数，不是
对离散 RN 映射求导。首次必要初始 J 在新 solver 内计费，固定
行尺度为 max(1,abs(initial value),max(abs(initial J row)))，
此后不更新。后续 J 只在真实后端请求时计算，迭代回调不增加科学调用。

缓存键与所有权如下：

| 层 | 键与内容 |
|---|---|
| 当前几何 | 实际 q168 字节；T/位置/metric/I/II 等已算数组 |
| 当前物理导数块 | q168、网格、径向块、u/v 族；K 无关 metric 与 I/II 导数 |
| 当前完整 J | q168 加 binary64 K；不能只按 q 复用 K 谱列 |
| backend 值表 | literal backend53 字节；该输入已有的完整约束向量与紧凑 summary |

同 q 新 K 可复用其 K 无关角核/位置/物理导数，只重新形成当前
K 的曲率行/J。h 只影响固定线性项。不同 q 淘汰当前几何、
物理导数块和完整 J，不把数百张完整 J 常驻或写盘。只另保初始/
最后实际完成的数组供绑定，backend 值表最多 960 项。全部数组
仅在该进程 RAM 内，临时磁盘读写为零，不上传 cache/artifact、
Release 或仓库。

淘汰后重访某个 q 若确实需要几何或 J，就真实重算并计入总钟。
new_geometry_counts、new_J_counts、
K_independent_derivative_input_counts 分别报告实际 started/
completed/failed/cache_hits，并区分 distinct 身份与 eviction
之后的重新执行。不能因为 unique-q 计数未增长就声称没有新科学。
组件事件另列角核、虚拟位置导数和当前 K 组装的实际耗时/状态。
process peak RSS 也进入原 scope 记录；不为报告重算已淘汰数据。

## 8. 唯一后端和两种输入上限

外层新总 scope 上限 900 秒。唯一 solver 上限 360 秒、maxiter 240、
ftol=1e-9，使用一次 scipy.optimize.minimize(method='SLSQP')。
solver 钟包含必要初始 value/J、导入和全部后端调用，不只记录
minimize 内部时间。大库调用的钟检查非抢占；实际超时和已做工作
照实记录，不虚称硬抢占保证。

最多 480 个需要新几何的不同实际 q168；literal 已付 q_R 命中另列，
不冒充新增点。另有最多 960 个不同 literal backend53 输入，
包括同 q 的不同 K/h，防止这类输入无限线搜索。每个回调输入都受
后者限制。实际重复几何/J 次数可高于 distinct-q 数，仍完整计费；
不能用 480 的 unique 语义隐去重复工作。两个上限只能缩小。

## 9. 原返回、紧凑输出与资格

后端一旦返回，先保完整真实 OptimizeResult 全字段、raw53、
status/success、message、nit/nfev/njev、后端耗时和原 multipliers，
再作任何资格、时限或外部判断。只要 raw53 有限，真实 q168/172
及完整准确候选记录也在下一次钟检查之前保存；status 9 等失败
不会抹掉实际返回向量。未返回字段不虚构。

若后端未返回，保存真实最后 callback53、实际已完成值/J 绑定、
迭代与组件成本及真正未完成部分。失败 callback 不冒充返回候选，
没有伪造 status0、伪造 0 cost 或修补后的 raw 向量。

模块内部 emit 只发送一次真实 NONLINEAR_RESULT。
caller 唯一拥有 SOLVE_TRACE/BODY_SOLUTION/MODEL 以及相应 partial
标签；已成功发送的 trace 不在后续预测异常时重复发送。

新输出采用完整而有界的紧凑记录：raw53、q168/172、全部后端字段
保留数值；科学 value/J/大 partial 只保 shape/hash/已填行列范围/
成本与组件状态。未完成 np.empty J 不对整张缓冲区哈希，只绑定
真正已经填完的块；不补零，不输出伪截断片段，不把哈希说成未来
免费数组。capture 只读已算结果，不运行重建。外层 stdout 目标/
限额为 96 MiB，不能分块绕限。

只有真实 status0 且 success 的返回，经过固定缩放残差门、原
未缩放线性门、§3 全部准确终门及 §4 全部后缀资格门后，才给出
candidate168。否则原返回与拒绝原因仍保存，candidate168 为 None。
合格也只授权外部至多一次 canonical full-body prediction，预测
通过才可运行至多一个原 actual pair；原十四门、全时全域 reach、
embedded、metric、端点/包络等主课题完成门都没有删减。

## 10. 固定 API 与外层边界

    build_full51_whole_suffix_model(
        field, accepted_state168, ring_candidate168,
        paid_free_model, paid_free_solution, paid_prefix_model,
        cfg, lower172, upper172, source_receipt, wall, capture=None,
        *, metric_budget, charge_prepare)

    solve_full51_whole_suffix_once(
        model, *, wall, charge_solve, emit=None, capture=None,
        solver_seconds=360., maxiter=240, max_evaluations=480,
        max_backend_evaluations=960)

    full51_whole_suffix_capture_record(capture, *, include_arrays=False)

    model.summary()
    model.full_record()

builder 成功路径的 charge_prepare 恰一次，包含新 P、新原末三
径向 jet、新线性模型和原盒 bounds；builder 不做初始几何/J。
solver 的 charge_solve 恰一次。外层 clock 从输入恢复到输出/
失败均持续计费。模块不依赖旧 scope 类或旧 ledger。

solution 字段为 status、report、qualified、qualified_candidate、
candidate168/candidate、candidate_record、actual_backend_raw53、
backend_success、backend_status。report 只作已有收据的紧凑输出。
capture 的 legacy include_arrays 参数不会启用大数组；full_record
也只提供新数组绑定和原已付来源引用，不构造后继免费输入。

后缀成功后若全域预测失败，原 q168/172 可作为新问题的真实候选
坐标来源；缺失的科学数组仍需在未来明确付费。是否启动后继问题
属于 root 的下一项工作，本 scope 不私自补跑 prefix102 或旧34。
