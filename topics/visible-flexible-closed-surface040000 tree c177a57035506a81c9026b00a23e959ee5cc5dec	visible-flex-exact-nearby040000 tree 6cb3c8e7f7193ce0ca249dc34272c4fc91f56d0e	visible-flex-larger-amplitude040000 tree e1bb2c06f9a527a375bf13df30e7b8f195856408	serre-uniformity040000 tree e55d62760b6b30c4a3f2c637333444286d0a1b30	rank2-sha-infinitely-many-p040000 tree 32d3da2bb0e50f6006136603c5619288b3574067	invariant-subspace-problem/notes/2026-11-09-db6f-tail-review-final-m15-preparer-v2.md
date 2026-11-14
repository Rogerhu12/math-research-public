# 最终 M15 前缀接续准备器 v2 独审

审查者 `/root/tail_theory`，2026-11-09。**PASS，条件式输入准备 / 来源与旗标门 / cut-jet 数据门。** 目标 $s=1$ 的已审成功分支尚未执行；本审查没有启动数值 solver，没有生成伪 $s=1$ 记录，也没有把小振幅真尾当作完整前缀解。

正式受审源 `scripts/db6f-prefix-prepare-final-m15-coupling-v2.py` 的 SHA256 为 `8b235dfd97d558fc16e446b65bff2412642b041b9bbe6efb193fc88147426b81`。旧版 `22e43581c929145483b704673eb767cabfc1961eb41400595f1a289caf59855e` 保留不改。作者为 `coupled_prefix`，审查者没有参与准备器实现；审查者指出了旧数值叶谓词的缺陷，以下独审核修正版完整含义。

## 1. 只接受真实已闭的最终目标尾

准备器将 continuation02 的 progress、reproduction、input bindings、config 和最终 response 串接：闭合记录必须逐字段一致，状态必须明确为目标尾已收敛并已 audit、前缀仍未解，目标 scale 必须恰为 1，worker 自然 exit code 必须为 0，且无 terminal exception。最终请求必须等于原保存的 affine `predicted_cut_height`，同时请求原 Jacobian 和 audit。

真实 response 必须收敛，原残差严格小于 $2\times10^{-9}$，705 个原 DN Jacobian 元素有限，完整有限 source audit 的原键齐全且数值有限。最后 history 的 norm 与 response、进度摘要一致。最终 shooting states 的维数、有限值、rawNode 和 rawStates 全部核对；参数与真实已闭 warm 只允许指定运行路径 / 迭代上限元数据差异，resolved guard 仍为 $.05$。

来源方面，旧 original command、restart-only 检查和 resume launch 的所有绑定在写出前重新读取核大小 / SHA。最终 response 的直接来源集合必须等于原 eight-file 集合并逐一核 SHA；完整绑定另支付其传递依赖。还必须提供 root 实际观察自然退出的记录，绑定最终 progress、reproduction、config、response，不能以进程不存在代替自然完成。

这些门只允许为一个真实最终 DN 准备下一步。它们不证明该候选已达到原前缀的 outer BC，更不证明完整闭图的连续 metric。

## 2. 原配置与 warm 接口

新配置复制原 `from-affine` 配置，只替换 `initialCheckpoint` 及四个输出路径。最终启动 argv 只改 `--tail-config` 与 `--out-prefix`；原 profile、chart、port、affine restart、物理固定参数、前缀自由参数、所有求解容差和网格选项保持原值。准备器明确拒绝 `correctInitialBoundary` 键，保留原 worker 的缺省真；零态对照配置的 false 不能进入该路线。

审查者独立重读原 argv：`--warmup-scales` 后直接接 `--lagged-tail`，所以尺度列表为空。原 `sharedEngines=True` 经 trial wrapper 只改用已审的诊断 client；该 fresh client 的缓存为空，checkpoint 的参数不覆盖本次 config flags。

真实保存的 affine 高度与 `preserve_restart` 重新求值存在原报告中约 $1.7\times10^{-21}$ 的微差。原 worker 从最终 response 取得初猜后，使用本次实际请求高度，为全部模加原有限线性边界修正，再请求原 nonlinear DN。它不会重贴旧 response 的标签来冒充新边值的解。高模非零也不会触发只适用于纯一模请求的 harmonic predictor 分支。

原配置本身未显式写 `projectionFloor`；审查者从 `db6f-prefix-tail-trial-core.mjs` 的默认值和真实已闭 checkpoint 的 resolved `.05` 双重核实此项。没有将缺省键误认成物理参数缺失。

## 3. v2 修补完整性

旧 `finite_tree` 会接受 `None`、字符串和 bool；JavaScript 序列化非有限数可能产生 `null`，因此旧谓词不能作为实际 cut jets 数值门。旧版此前只走过真实未闭合的拒绝路径，没有据它放行目标或启动最终前缀。

源码差分表明 v2 只用 `valid_cut_jets` 替换该谓词及其唯一调用 / 错误信息。其键集合已与 trial core 的实际 `cutJets` 返回式逐项核对：14 个标量与 `height/slope/second` 三列表。标量必须为有限 int/float 且非 bool，三列表长度必须等于正整数 $M$，元素满足相同数值条件；缺键、额外键和 null 都拒绝。

其余 source / closed-state / argv / 配置门保持旧版原样。输出的 `preparation_script_sha256` 来自实际运行文件，能区分 v2 与保留的历史 v1。

## 4. 实际独立重放与限制

审查者重放 `db6f-prefix-final-m15-cut-jets-fixture.py` 到自有新输出，实际 exit 0；文件逐字节等于作者输出，SHA256 `ebaa95d264e4a46bf22862d0fd520db14d4d9f16298cf5c03d894d303388e140`。真实已闭 $s=.25$ 的 jets 被接受，86 个只存在于内存的错误副本全部拒绝，原 response 文件前后散列相同。没有构造假的成功 metadata，没有调用完整正分支、root、RK 或 solver。

审查者同时对原 command / restart / resume 的 91 个不同文件引用独立核大小及 SHA，并分别运行旧版与 v2 的 `--check-current-gate`。两次实际 exit 0，输出均为 `ready=false`，原因是 continuation02 尚缺闭合 reproduction；写文件数和 solver 次数均为 0。该观察只记录当时状态，不推断稍后的 continuation 进展。

自有重放结果为 `2026-11-09-db6f-tail-review-final-m15-cut-jets-fixture.json`；完整绑定和审查记录为 `2026-11-09-db6f-tail-review-final-m15-preparer-v2.json`，SHA256 `a4ae48242965bd098ccae1d530b7c6bc993d984d4eaae62a2047429c640d89f1`。正式接续仍须真实最终 $s=1$ 审计与 root 自然退出记录到齐，之后执行原前缀联解、原 outer BC 验收、最终 seam audit，再为实际新图重新完成连续证书和独立全流程。
