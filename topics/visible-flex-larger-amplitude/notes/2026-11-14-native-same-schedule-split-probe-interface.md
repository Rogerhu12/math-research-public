# 两个原段、四个短块 J 的实际探针接线

2026-11-14。独立入口：

- `../computations/geometry_20261114_native_same_schedule_split_probe.py`
- `../computations/geometry_20261114_native_same_schedule_split_probe_hook.mjs`

它调用已冻结 [同 schedule 窗口模块](2026-11-14-native-same-schedule-windows-interface.md)，针对 [actual36](2026-11-14-actual-request36-native-equilibration-failed-direction.md) 已确证的原方程巨缺陷准备下一项小计算。本文写成时尚无本探针数值结果；本地只做 Python AST 与 Node 语法检查，没有科学执行。

## 1. 科学范围严格限定

仅 original stage43、stage58 的**同一 actual28 原入端**，每个段原12步按6+6分组，实际计算4个短块 withJac。两段分别另沿原 no-J 算式运行同样4个短窗，以清楚记录两种原调度差别。

不会：重算576段完整 J；重算两个完整12步参考 J；运行原 `dn.solve`、Newton、trial、endpoint J、fresh audit；重算零 H 求解；改变原 profile、g、H、far、graphs、gains、原 σ、`linearSteps` 或任何原容差。

withJac 的原 x 是 `n*(1/12)`；no-J 的原 x 是 `k/12`。两条路径都保持各自原字面 h/x、原 profile 对象和原 root/RHS；不将其数据混称同一浮点调度。两目标原 profile 均无 cusp，原 portRatio 均为1。原 source 固定，不能将本版拿去处理其他带 cusp 的段。

## 2. 完整原握手、seed 与 actual28 参考

Python 复用已冻结25入口的纯输入绑定：17/19/21/22/23 全历史、同一112项非零 H、完整577×224 seed与全部9546个负零、原 config/source/ready/capacity、原 graphs/gains/far/scales 和原 live stages。

实际28参考继续固定 result SHA：

`ff53d954de378571eac8d4b22e55c1b0a4595c0a0ab567d0760e1f3d427fded7`。

冻结 `CapturedArrays` 首先绑定原整个 artifact；随后只抽取原 bytes，保存两段的：

- 原 input state，224项；
- 原 withJac `stage-out`，224项；
- 原 `[minA,minD,meanHeight]`，3项；
- 原完整长段 J，224×224，只作旧 reference。

这些小参考都有单独文件、尺寸、形状和 SHA；没有用旧 residual+state 相加重建原输出，也没有重新求原长段 J。原原件仍只读。

Node 再读对应参考的真实 bytes，确认当前原入端与 restored seed、actual28 input逐位相同。它仍检查原完整 H/target/scales/far；对具体段另锁 `43=(raw0,seg3,part4,parts8,[.5,.625])`、`58=(raw0,seg1,part5,parts8,[.625,.75])`。

原请求 flags 仍为 `jacobian=true,audit=true`，但这是沿用协议身份。probe 在原 solve 之前执行，随后明确计划停机；**flags 不代表已经计算全 J 或 audit**。

## 3. 每个段的实际执行与即时保全

从原 `state[n+1]` 构造226项输入：前224项逐位复制，最后两个 mean 积分state按原 cellFlow 初值取正零。

1. 原 withJac k=0..5，保存全226中间 state、内短块224×224形状 J、额外2×224 mean tangent、原返回 minA/minD/maxRootRelative、每一步原 x/h 与四个 abscissae bits。
2. 把**完整226中间 state**传给原 k=6..11；不清零 mean。保存外短块同类输出；Pi及其J行只在原出口按原 portRatio 除一次。
3. 将两短块的最终旧坐标输出与 actual28 原 `stage-out` 逐位对照；原范数口径下的最大浮点输出差也记录。将组合的 minA、minD、原两 mean state 相加式与 actual28 guard-mean三项比较。
4. 另沿原 no-J 的 `k/12` 路径依次做0..5、6..11，同样保留完整中间 state与原出口。它与 actual28 withJac reference 的对照明确标记 reference种类，不能把可能差别称为新分组错误或自动通过。

每个短窗一完成就写其 state、J和窗口记录；若后一个窗 guard失败，前一个窗证据仍在。输出直接保存 typed-array `<f8` bytes，保留正负零和实际非有限位模式。原局部异常、发生段/窗口和已完成计数写入 partial summary；不编造缺失块。

原 no-J 返回路径没有 minA/minD估计，因此只记录实际原 guards返回以及实际state，不虚构这两个最小值。对两个路径都没有任何新数值阈值，也没有以对照误差作为新科学接受门。非有限新J若原函数返回而未抛错，原数组和统计仍保留，不能因probe流程完成就冒可用J。

## 4. 停机与输出身份

4个 withJac短块及4个 no-J窗完成后，写 `split-probe-summary.json`、`split-probe-array-manifest.json` 和每段的完整 report，然后抛：

```text
VISIBLE_NATIVE_SAME_SCHEDULE_SPLIT_PROBE_COMPLETE_V1
```

原 worker catch 如实返回 failed；Python 仅在消息、1次协议请求、worker正常退出和完整计数全部一致时标 `probe_completed=true`。这表示 scoped诊断完整完成；`native_accepted=false,task_completed=false` 始终保持。原 worker 的 last、tangentPredictor和成功响应 cache 不填入这个结果。

没有把两个短块相乘生成新的长矩阵。新4个短J各自有独立 SHA，不冒 actual28 整体 J 的旧 SHA；旧长J的最大项统计只是对保存数组的读数，不是新长J计算或条件数。

`prospective-split-layout.json` 与新显式尺度是候选扩展系统的说明，没有安装进原 dn。旧节点 σ全部原样保留；新中间节点明确取原 parent stage σ。它不从新 gains递推，也不会用它替换原 σ下的最终readback。

## 5. Actions CLI

沿25/28的原参数，只新增 `--capture-directory` 指向统一已核下载的 actual28 `native-correction-capture`。此入口不需要actual36方向，也不运行坏方向的trial。

```bash
python "$C/geometry_20261114_native_same_schedule_split_probe.py" \
  --failed-directory "$TOPIC/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$TOPIC/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$TOPIC/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --v2-candidate-summary "$TOPIC/notes/public-actions-43604874829-1-zerorkprobev2/same-RK-candidate-native-probe-v2/summary.json" \
  --candidate-directory "$TOPIC/notes/public-actions-43605912092-1-zerorkprobev3/same-RK-candidate-native-probe-v3" \
  --capture-directory "$CAPTURE28" \
  --source-topic "$REPO/topics/visible-flexible-closed-surface" \
  --node-heap 6144 \
  --out "$OUT/native-same-schedule-split-probe"
```

依赖固定源除原25历史外，还包括：

| 功能 | 源 SHA256 |
|---|---|
| actual28 metadata纯绑定，`geometry_20261114_native_band_trial_replay.py` | `e357426aa6e81cbab526ea74f7f9fd3e1fd69d917000dd7f9847972745823b80` |
| 完整 capture数组绑定，`geometry_20261114_native_captured_band_correction.py` | `b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390` |
| 窗口模块，`geometry_20261114_native_same_schedule_windows.mjs` | `2973c14460de920ba2cc873ef9bcc137bdd264b70799ba9734122f3c610b946f` |

第一个 helper 不调用其trial主程序，也不需要band方向；第二个不调用其band主程序；仅调用已冻结的原输入绑定。原数学源继续由原TailClient窄恢复。

所有二进制小参考及新短块各文件小于1 MB；本probe不另保存整个231 MB J或LU。原artifact下载仍走已经钉住的统一fetcher。

## 6. 若实际短块证据支持扩展线性系统

后继的578stage矩阵可直接消费原actual28的574个未分组 J，以及本次四个新短块。不能提前声称这份新扩展矩阵已有效，需实际消费以下同一对象：

- 全旧节点取原state；两个插入中间形状state取本probe的真实inner full-state前224项。
- 外半块在shooting列表前、内半块后。内半块 residual按实际inner输出减对应中间state；外半块 residual按真实分组出口减旧out-node，不能偷用旧r覆盖实际出口差。
- 新完整cut/far仍为同原H/原farG和旧首末节点；原g/profile/root/模式不变。
- 完整增强A/r有独立producer、原矩阵来源、4块SHA、旧到新索引、完整新增σ规则及全state身份。
- 原未分组574块按旧节点输入完全不变才可复用；任何新base或新H都不能移植这些旧J。
- 之后方向仍限制回旧坐标，调用原完整flow、原σ与原trial/最终验收；新内部低残差不能替代原整体gate。mean/readout仍按原分组口径另付。

这条路径分开检验长传播矩阵表示和原RK步长问题。它不增加ODE步，不改变原连续metric，也不声称当前已经排除了其他stage、局部导数误差或全系统病态。
