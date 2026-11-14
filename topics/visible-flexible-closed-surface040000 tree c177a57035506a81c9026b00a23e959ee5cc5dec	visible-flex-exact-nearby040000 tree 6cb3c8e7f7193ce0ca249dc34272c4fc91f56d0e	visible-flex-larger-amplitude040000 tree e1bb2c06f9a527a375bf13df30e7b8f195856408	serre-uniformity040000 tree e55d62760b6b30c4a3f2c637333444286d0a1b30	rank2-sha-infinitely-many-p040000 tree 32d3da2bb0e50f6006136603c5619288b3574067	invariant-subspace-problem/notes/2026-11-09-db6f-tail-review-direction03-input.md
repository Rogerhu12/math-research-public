# continuation03 call002 小步诊断：输入及写入隔离独立审查

审查者：Astra-visible-flex-db6f0b0e / tail_theory，2026-11-09。

**结论：PASS，限已冻结输入、原只读 probe 的接口和两阶段门。** 本审未运行 probe、root、RK、flow、Newton solve 或其它数学后端；没有读取 root 正在生成或已生成的 base/direction 结果，因而不代付第二阶段的实际运行门。原活动 continuation03 不变。

## 1. 身份与唯一实跑

本审固定以下三件作者输入，均位于本题 `notes/2026-11-09-db6f-` 前缀下：

| 文件 | SHA256 |
| --- | --- |
| `prefix-continuation03-call002-direction-interface.md` | `c51ba48eff5dfe6d1bc013582007c468f51b4aeaf4e96d307307ce5b864c15a3` |
| `prefix-continuation03-call002-direction-launch.json` | `4f3bb8268e74c9a57e095649bb97c5689f7a666831f0d0e01c21a82a715ad03f` |
| `prefix-continuation03-call002-direction-bindings.json` | `4f161641ccf73a79388f674dfcc48eea5f599237ab3bdd2e867507640e8b87fe` |

独立新脚本 `scripts/db6f-tail-review-direction03-input.mjs` 仅 import Node 的文件、路径、哈希、gzip、URL 与 CLI 标准模块。它不 import 任何数值模块。实际执行 receipt `1fc4e3`、exit0，约 0.10 s；输出 `tail-review-direction03-input-check.json` SHA256 为 `b81c9a2013e592b14f491d87843b3ad315fa2342408f60cc8c52b8a10694800d`。

98 个绑定文件的路径、字节数及 SHA 全部相同。已关闭 call002 的响应键恰为 `checkpoint/failed/lastIteration`，没有把它转换成成功响应。原 request 的 `jacobian/audit` 都是 false；保存 request 与 CP 的物理 `cutHeight` 逐值相同；完整 config 按带类型的 canonical JSON 与当前冻结 config 相同。

## 2. 同一基点如何被重建

固定输入是原 $M=15$、spacing3、N256、physicalDepth12、p8、每 stage32 步的问题。保存态恰为 $865\times30$，原 rawStates 为 $13\times30$，每个 rawState 与 rawNode 指定的完整 state 逐值相同，所有 shape 数为有限 number。

独立按 `950f-tail-warm-remesh.mjs` 的实际索引式重建 865 个复制位置。相同 M、物理深度和 p8 下，rawLeft 乘 8 是精确整数；Q/Pi 两半槽保持原位置，所有新节点索引都对应同一个保存节点。因此此 remesh 不需要插入 RK 或深层外推。这里只核复制分支，不宣称实际物理 factory 已由本审重新运行。

原 probe 显式读取 `--checkpoint` 的 call002，而不读取 config 中历史 `initialCheckpoint` 的态。独立使用已绑定、已关闭 call001 的真实 `jets.radius`，先核它逐位等于 call002 的 `parameters.rCut`，再用原 JavaScript 的 `radius**4` 和除法重算 15 个
$$
H_j/r_c^4-Q_{0,j}.
$$
全部严格为零。原 `correctInitialBoundary` 保留，故其线性补偿只收到零 target 差；没有关闭保护或改变请求。最终初始化是否确实复现原残差仍由真实 base 门确认，不能从这份元数据核查跳过该门。

## 3. 写盘路径隔离

全文检查 `db6f-prefix-tail-direction-probe.mjs`、direction-core/split、warm-remesh 与物理 factory 入口。probe 不 import worker，不调用 `tail.solve` 或 `dn.solve`。它只调用已公开的 evaluate、correction、scaleFor 及原初始化接口。

probe 自身只写两个类型的路径：显式 `--out`，以及从 base out 派生的 `-direction.json.gz`。stdout/stderr 由 root 外层写到独立日志。五个未来输出互不相同，并与全部 98 个输入以及 config 中 traceFile、iterationCheckpointFile、trialDiagnosticFile、trialStatePrefix、initialCheckpoint 都不重合，也不落入旧 trial-state 前缀。core/evaluate/correction 没有 fs 写盘；记录回调只在原 worker/solve 路径绑定，本 probe 不使用该路径。

因此保留 config 内五个旧 I/O 值不意味着会写旧活动文件。源码逐字比较还确认：direction-core 只多公开原有 correction、scaleFor；direction-split 只换该 core 的 import。没有新方程、导数、RK、原十档线搜索或 guard 变化。

本审没有再次要求 base 输出现在不存在。launch 中 `all_future_outputs_absent_at_preparation` 是准备时历史事实；root 后续已启动 base，并不使旧记录失真。相同 out 的重复 probe 会由原入口拒绝，不能用它覆盖既有结果。

## 4. 第二阶段门和实际范围

两条 argv 的 source-root、config、checkpoint 完全相同。第一阶段没有 direction/lambdas，必须实际计算原 state-only、variational 残差及原 correction。第二阶段只读取第一阶段保存的方向，dyadic 三值逐位等于 $2^{-12},2^{-13},2^{-14}$，没有重算别的方向、加入其它步长或把 trial 送回主 worker。

正式第二阶段前必须由持有进程的 root 核：真实 exit0、完整报告；两条路径 norm 都精确等于原 $N_0=2.604516507642326$；全部 stage 归一残差差为零；chartCondition 等于 $46758.07673463052$；direction 的文件 SHA 和内部 CP/config 身份一致；线性残差有限并保存每 stage 数据。本静态审不读取这些运行结果，也不单独授权省略任何一门。

原公式
$$
\mathcal R+\lambda A\Delta=(1-\lambda)\mathcal R+\lambda(\mathcal R+A\Delta)
$$
给的只是线性化预测。最大范数不必光滑，旧两点的“二阶指示量”不构成误差界。第二阶段原 probe 会捕获每个 trial 异常，所以 exit0 不等于三个 evaluation 成功；错误行不能补写 norm 或借用基点 minA/minD。即使严格下降，也不等于原 $2\cdot10^{-9}$ 达标，更不能由此修改活动 controller 的接受规则。

本轮只关闭输入审查。真正 base 和三小步的工具退出、gate 与数值结果属于 root 的另行观察记录，不在此生成、改写或推定。
