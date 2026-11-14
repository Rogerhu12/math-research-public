# strong 原全 shooting 切向的跨进程保存入口

**状态：实现与真实输入准备已完成；尚未执行新 worker 的数值求解或真实 flow-J 二进制回环。不是新解、几何证书或达到完成标准的声明。**

## 为什么保存这些已有数据

本轮 q098 的首个新完整 H 使用原比例暖态时，原归一残差为
933.0483780997954。三次原 Newton 全步后依次到
0.001005720225069174、3.607336772944774e-9、
7.442322326430711e-11，最后完整 J 响应才返回。
原严格容差仍为 2e-9。该首次尾包完整原件已经归档为
`2026-11-13-strong-q098-initial-tail-fullJ-recovery.json.gz`，
SHA256 `35823553df43fc8e643ca1e56ab4b6478e0e8057383143d0dc30675ae8e3f3ac`；
它没有 audit，不能代最终验收。

冻结的 `78718-tail-tangent-core.mjs` 已在完整 J 求解时保留
`sol.linearizedFlowJacobians`。冻结的
`78718-tail-tangent-predictor.mjs` 已提供
`createPhysicalHeightTangentPredictor`，能用全部物理 H 的增量生成每个
shooting 节点的全部 Q/pi 暖态。原 worker 在同一进程中一直使用它；
旧 JSON checkpoint 没有保存这些 flow-J，所以跨进程会失去这项已有计算。
不能从 cut 处的 `heightJetJacobian` 恢复全状态切向。

q098 当前 worker 没有被释放或修改。其第二次 true-H 请求已实际调用原
full-shooting predictor，最大相对暖态修正为
0.0011964762968233358。这只是下一真尾求解的初猜指标。

## 新增内容与保留的原门

六个 fresh 源文件见
`2026-11-13-strong-full-tangent-preparation-manifest.json`。
存储 helper 把已经收敛解的全部 stage flow-J 及完整基准 states/H 保存为
Float64LE gzip 侧车。M28/576 stages 的原 flow-J 共
14,450,688 个未压缩字节，按完整 stage 分块，每件严格小于 5 MB。
另存完整二进制基准以保留 JSON 不区分的正负零。

恢复严格核对完整原参数（只排除原有四个 I/O 路径键）、rawNode、实际
stage/分段/积分断点、farGraph、radius、物理 fingerprint、冻结源码和
全部基准 states/H。随后直接调用未改的原 predictor factory。
原 same-H exact-raw 分支仍优先；原 `dn.solve`、全 H、2e-9、positivity、
full J、RMS/BC 与请求的完整 audit 都继续决定接受。

每次保存后重新读取并逐 bit 检查全部 states、完整 H、farGraph、radius
与全部 flow-J。每个 worker 的第一份保存还会用未改的原 factory，比较
一个完整 H 探针下的所有 577×56 预测状态；该探针只检查存储等价，不运行
非线性求解，也不声称是新解。写侧车失败会保留原真尾响应并明确报告
`fullFlowTangentStorageError`；有问题的输入侧车不会被使用。

## 已实际完成的准备检查

1. 三层原 source transform 全部匹配，最终展开的实际 worker 通过语法检查；
   该 source-only 分支没有实例化 tail engine 或执行 ODE/Jacobian。
2. 完整原实际 BVP 的 Python 编译链与 fresh client 导入成功，原固定物理
   merit、disk QR、prefix cache 与所有最终门均保留。
3. 用真实已接受 q096 M28 的原 physical/raw/tail/config，完整复核原数组
   piece SHA、原 RMS、全 28H、完整 J/audit 和来源后，`--prepare-only`
   正式退出 0；没有启动 Node、Newton 或新的实际尾求解。

独立运行树保留原 626 件 computation 文件，再加入 fresh 源，共 636 件；
完整身份见 `2026-11-13-strong-full-tangent-runtime-source-manifest.json.gz`。
当前正在运行的 q098 使用原运行树，不受此准备影响。

## 继续执行

q098 通过原 true-H、RMS/BC 和最终物理审计后，先用原 adapter 生成真实
fixed-design view。新六控 full-J 响应加入 `start_acceleration`；同时在
唯一 Node 槽，用 `strong_full_tangent_accepted_audit.py` 对该接受点的同一
完整 H 再运行原 full-J/audit 并形成首份真实可用侧车。完成真实回环后，
`strong_full_tangent_actual_bvp.py` 可接原 control-response 或 secant-v2
初猜入口。全状态切向依然只是暖态，后续每个目标仍做原非线性求解与全门。
