# 单次真实目标 DN：v2 严格类型身份的独立薄运行器

作者：/root/coupled_prefix，2026-11-09。

**状态：新运行器及启动方案，尚未启动任何求解。** 它与 continuation02 是不同运行。输入是仅供初猜的逐模放大状态；只有实际原方程响应、完整原 Jacobian／源审计、原容差和 worker 实际退出0全部满足时，本运行器才请求正常退出0。它不证明 prefix 联解，更不代替全 XYZ 或连续几何证书。

## 0. 独审发现的类型身份修补

v1 源 SHA e0c4792dc081bcd4c2082064f853d1b8a06e7ca03dba68742d3f066631cd43c7 及原方法 SHA c64baf2548eb18859944031ee666bb036ad5bd6e882fbe4a8e7c1d1e84fd0df0 保持历史原字节，均未启动。tail-theory 全文独审发现：Python 对象等号把 True 与1、False 与0视为相等；而原 JS 的 cuspAwareFlow===true 等分支严格区分 bool 与数字。因此 v1 的通用输入身份门不够严格。当前已绑 prepared config／warm 没有此类型问题，但 v1 不作新的正式入口。

v2 仅把声称精确身份的 config、参数签名、goal/cutHeight、request、record 和运行参数改为 canonical JSON 比较（固定 sort_keys、separators，禁止 NaN）；rawStates 另外要求13×30有限非 bool 数并严格对应新 states；history.iteration 必须为非 bool 整数。已有 rawNode 非 bool 整数门保留。数学调用、原 source、36轮/容差/guard、finally close 及最终 residual 可不同于 history 最后基点的语义全部不变。本轮不创建伪造成功响应、不运行 solver；独审只重核差分与真实已存输入的类型身份。

## 1. 为什么不直接使用旧单请求 runner

原 scripts/db6f-prefix-tail-trial-run.py 是 s=.25 recovery 和 zero pilot 的入口，但两处实际请求／reproduction 都写死 audit=False，没有改变该参数的 CLI。本次保留它的原字节。

新 scripts/db6f-prefix-single-audited-target-v2.py 直接使用已冻结的 db6f-prefix-tail-continuation-client.py。与旧 trial-client 全文比较，continuation-client 只改了自身来源名及响应的原子落盘步骤；worker、实际 solve、cache 和 close 的数学路径相同。采用该 client 使每份原始响应保留与 continuation02 相同的八源集合。

运行器新建 fresh port，仅调用一次：

    port.solve(goal.copy(), jacobian=True, audit=True)

goal 直接从原 affine prefix 的 predicted_cut_height 复制，没有再乘 s、没有额外除以 cut 半径的四次方。物理高度到 normalized Q 的唯一换算仍由原 DN 内部完成。audit=True 同时绕过任何缓存；fresh client 的 cache 本来也为空。初始化原 worker 所做的 cut／linear-port root 计算仍属原初始化，不把“一次请求”误写成只有一次 angular root。

## 2. 不变的原问题及输入身份

运行器以已审 resume02 launch 和 input-bindings 的固定 SHA 为权威，重新哈希其中66个闭来源／输入；当前八个实际 source 必须属于该集合。source-root 必须是该 launch 的冻结 bundle。这里不读取或修改活动 continuation02 的 progress、trace、trials 或 iteration 文件。

CLI 提供的 config 可以是已准备的逐模 warm config，但除以下五个 I/O 键外必须与原 continuation02 config 完全相同：

- initialCheckpoint；
- traceFile；
- iterationCheckpointFile；
- trialDiagnosticFile；
- trialStatePrefix。

运行器只把这五项指向独立输出 stem。原 M15、N256、depth12、parts8、steps32、maxIterations36、solveTolerance=2e-9、projectionFloor 默认0.05及 correctInitialBoundary 缺省真保持不变。没有新增 guard、放宽容差、替换 Jacobian、线搜索或方程。目标文件必须与原 input-bindings 里的目标 SHA 相同；其15个物理 H 值与已绑 target_height 逐值相同，物理 metric 参数还与原 config 核对。

warm checkpoint 必须提供865×30有限 shape 值、原13个 rawNode、对应逐值相同的 rawStates，以及精确目标 cutHeight 标签。该标签仅让原 loader 的统一 ratio 为1；它不是 warm 已满足原方程的声明。原 correctInitialBoundary 仍会按保存 Q0 实施完整线性初猜修正。

CP.parameters 同时含物理／数值定义和历史运行 I/O。用已闭 quarter CP 交叉核布局时，只排除五个 I/O 及 maxIterations：quarter recovery 的历史预算是32，当前真正执行 config 始终是36。其余 parameters（包括原容差、几何和离散布局）必须相同。实际新响应还必须把这六个运行参数匹配到本次真正 config，不能把旧 CP 内的 I/O 元数据当成新执行路径。此区分不改变任何物理或 shooting 方程。

## 3. 输出、关闭与数学接受

所有输出拒绝覆盖。只有预先由 shell 创建的独立 stem-run.log 可存在。新 config 和 reproduction 在 worker 启动前分别写成只读新文件。reproduction 只记录准备输入，不在运行结束后补改其原字节。

运行器保留原 client 的原子响应文件，不改、补或包装其 response 内字段。求解器抛出失败时，原 failed／lastIteration／checkpoint 等真实 schema 原样保留；作者的 summary 另记错误。失败包没有 residual 或 converged 时，不向失败包中补造这些字段。

关闭步骤在 finally 中调用原 port.close，随后直接读 proc.poll。运行器在调用构造函数之前保留 fresh 对象，以便原 __init__ 在 Popen 后失败时，仍能关闭并观察该真实进程。没有进程句柄、poll 为 None、或实际非0，都不得当作 worker 已正常退出。run summary 的 intended_runner_exit_code 只是该脚本即将返回的码，父会话仍须另保存工具实际退出记录；文件存在不作为退出证据。

成功响应必须同时满足：

1. 原 request 恰为 exact goal、jacobian=True、audit=True；实际 config 及八源 SHA 与本次绑定相同。
2. 原 successful response 恰有 converged、residual、jets、heightJetJacobian、history、audit、checkpoint 七个字段，converged 严格为 True，有限且非 bool 的 residual 在 [0,2e-9)。
3. 完整物理高度 Jacobian 含705个有限非 bool 数；完整 cutJets 有14个有限数值标量及 height／slope／second 三个长度15的有限非 bool 向量。
4. 原 audit 八字段全部有限非 bool，minLeading 和 minD 为正。它仍仅是原有限源 jet 审计，不是导出后 actualXYZMetric，也不是连续全域界。
5. history 非空且不超过36个基点；保存状态、raw 映射及精确目标标签有效；真正 response CP 的运行参数对应新 config。
6. 实际 worker 退出码为0，且 client／schema 验证没有异常。

原 core 可能在第36个被接受步之后再作一次完整评价，因此最终 residual 可能不同于 history 最后一个基点 norm。本包装保留该原算法语义，不人为要求二者相等，不用旧 history norm 替代真正最终 residual。

真正成功仅标为 TARGET_DN_CONVERGED_AND_AUDITED_PREFIX_UNSOLVED；其它情况为 SINGLE_TARGET_NOT_ACCEPTED_PREFIX_UNSOLVED。数值阶段返回后，前者请求 runner 退出0，后者请求退出2。启动前绑定／拒覆盖异常会直接报错并非0退出，不能伪造成功 summary。

## 4. 供 root 独立审查后使用的具体命令

下列是启动计划，**尚未执行**。tail-theory 的真实纯构造输入也须先通过独立全文审查。新 stem 与它的 prepared config 以及活动 continuation02 全部独立。

    cd /workspace/scratch/db6f0b0e7462/math-research
    /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
      topics/visible-flexible-closed-surface/scripts/db6f-prefix-single-audited-target-v2.py \
      --source-root topics/visible-flexible-closed-surface/repro/source-root \
      --config topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-harmonic-s1-from-call9-config.json \
      --target-prefix topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-flat-v17v18-m15-affine-cut-predictor-from14q512.json.gz \
      --checkpoint topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-tail-harmonic-s1-from-call9-input.json.gz \
      --out-prefix topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-harmonic-s1-audited-target-01 \
      --node-heap 1536 \
      > topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-prefix-harmonic-s1-audited-target-01-run.log 2>&1

预计实际响应只有独立 stem_tail_0001.json.gz。独立 summary 不创建 target_reached、target_audited 或 continuation02 worker_exit_code，也不调用或修改原 final-m15-coupling-v2 的 continuation 身份门。若未来单请求真的成功，root 将依据该实际运行另建明确命名的来源验证与 coupled launch；不得把它改称原 continuation02 已完成。

## 5. 本轮验证范围

本轮只作源文件静态阅读、client 全差分、现存冻结输入的只读元数据核对，以及新 Python 源的 AST 语法解析。没有运行新 wrapper、root、flow、DN、BVP、导出或几何后端；没有构造伪造的 positive response fixture。后续独立审稿和实际工具退出另列记录。
