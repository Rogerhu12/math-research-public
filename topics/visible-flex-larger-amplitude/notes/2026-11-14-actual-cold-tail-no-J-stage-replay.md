# 实际冷初猜：原无 Jacobian 全 stage 重放

这是公开仓库 Actions 的实际回执，不是新的尾部解，也不是新接受父场。
本次只解释 [原 tiny-H 失败](2026-11-14-actual-tiny-H-native-tail-cold-start-failure.md)
的 iteration 0。没有重算零锚，没有 Newton，没有改 H、RK、远端边界或容差。

## 1. 来源与执行身份

- Run [43602823170](https://github.com/Rogerhu12/math-research-public/actions/runs/43602823170)，
  job `132471064124`，lane `coldtailprobe`；源提交
  `25d2dcb606fa42af4ad146eae8b2463490b3ecbc`。
- 原 no-J 重放、artifact 保全、普通 rebase/push publisher 都实际 success。
- Artifact `14117255967`，`visible-mainline-coldtailprobe-43602823170-1`，
  ZIP 4,092,244 B，SHA-256
  `edc1a588aa521ca6ab283fc284cf66aa878a8c5525862cbb778b5255319c2fbb`。
- 消费的是 run `43598917532` 的真实 `true-tail_0001.json.gz` 与
  `true-tail_iteration.json.gz`；前者 SHA
  `ebe8932a7ba1a995f49b365344e795714bc0fdfccc606765cc69944b56a6b7a0`，
  后者 SHA
  `e996f37aa4eb7cfb0bb8b5bb912f594af794d16146240ee6db114c22eb55de7d`。
- Python 探针 SHA
  `5baf4b5505da6e124420253996630f6ebe6ecbc019f26938fa5747b147598515`；
  Node hook SHA
  `ad64dbc9ac33bcb51d693445649bf15164df7742587087a50dfe4ddb5dc117bd`。
  具体协议见 [接口说明](2026-11-14-actual-cold-tail-residual-probe-interface.md)。

`launcher-result.json` 实际报告 `identity_verified_before_stage_pass=true`、
`worker_exit_code=0`、`original_native_solve_calls=0`。
原 native worker 文件 SHA、全部数学源 SHA、数值配置、完整 ready 语义及
capacity 均在 stage 计算之前严格匹配。Node hook 只替换请求循环，原 constructor、
`initial`、`evaluate` 与数学源保持不变。完整 evidence 在
`notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/`。

仍是 M=112、N=2048、spacing=2、原 RK steps=12、physicalDepth=8、
576 个实际射击 stage、原 solveTolerance=`2e-9`。完整 H 112 项逐项保留；
首项为 `4.1760413061806626e-17`，没有将非零输入当作零锚。

## 2. 保存状态就是原 cold initial

重新调用原 `dn.tail.initial(H/rCut^4)`，只用于与实际保留状态逐项比较，
没有用新初值替换输入状态。

| 实际比较字段 | 回执 |
|---|---:|
| 比较条目 | 129248 = 577 × 224 |
| 数值不相等条目 | 0 |
| 最大绝对差 | 0 |
| 数值逐项严格相等 | true |
| 仅正负零符号不同 | 10153 |

正负零差单列保留，因为 JSON 保存会丢掉 `-0`；不能把数值相等写成逐位
IEEE 相等。对本次实际保留的 JSON 状态，数值初猜身份已经完全核对。
因此这次失败不能解释成保存了另一份初猜、丢失部分模式，或误用了已接受
zero-response 的 shooting state。

## 3. 原无 J 流的完整实际残差

调用严格为

```text
dn.tail.evaluate(savedStates, exactOriginalTarget, false, originalScales)
```

原 576 个 stage 都完成，所有原 flow guard 都通过，所有返回 flow 的
`J` 都为 null。Stage pass 实际耗时 70.779 s；整个 launcher 为
90.335639894 s。无 J API 不返回有限的全程 minA/minD，故此回执没有另造
这两个下界。

| 指标 | 实际值 |
|---|---:|
| 原 iteration 0 的 with-J norm | 13414069.96827908 |
| 本次原 no-J norm | 13414069.968482966 |
| no-J 减原 with-J norm | 0.00020388513803482056 |
| 全局最坏 stage | 11（从 0 编号） |
| 最坏原始位置 | rawCell 0 / rawSegment 7 |
| 最坏列 | 215，Pi 第 104 模（角频率 208） |
| 该列实际绝对残差 | 6.943706093148329e-8 |
| 该 stage 原 scale | 5.176434974219545e-15 |
| 该列按原 scale 归一的残差 | 13414069.968482966 |

完整 576 × 224 残差的符号值、绝对值、原 scale 归一值均已保存；没有只留
最坏点。原 scalar norm 从这些实际 residual 与边界项精确重建，报告
`original_scalar_norm_reconstructed_exactly=true`。

从已保存的 stage 数值选出最大的几项如下；这里只读取并排序已有回执，
没有再次积分或重算残差。

| stage | rawCell / rawSegment | 列 | 已保存绝对残差 | 已保存归一残差 |
|---:|---|---:|---:|---:|
| 11 | 0 / 7 | 215 | 6.943706093148329e-8 | 13414069.968482966 |
| 12 | 0 / 7 | 158 | 8.650770447755117e-9 | 1668861.4374145134 |
| 9 | 0 / 7 | 215 | 3.230893829496791e-9 | 626014.8758162701 |
| 10 | 0 / 7 | 215 | 1.4059005284955276e-9 | 271931.4573490269 |
| 8 | 0 / 7 | 187 | 4.313412417162091e-11 | 8362.004210414681 |
| 13 | 0 / 7 | 158 | 1.808317873724097e-12 | 347.97207600925884 |

cut 的全部 112 个 height residual 和 far 的全部 112 个 Robin residual
均恰为 0。原初猜已经满足两端条件，巨大归一缺陷确实出现在内部 stage
匹配。原失败 line search 的 stage 13/14 分支拒绝，和这里原未修正初猜
的最大缺陷 stage 11，是两个不同的实际事件。

原 scale 仍是 `max(1e-250,maxabs(H/rCut^4))` 后逐段除以
`abs(gains[n][0])`。表里的 Pi 残差是 native 动量坐标，不是曲面位置误差；
不能把 `1.34e7` 读成同量纲的巨大空间位移，也不能因 H 很小就宣布残差
应被固定绝对容差吞掉。

## 4. 这条回执支付了什么

已经排除本次 checkpoint/冷初猜数值身份不一致，且直接定位了原实际流
对该冷初猜的内部不兼容。原 no-J 重放复现了 with-J 记录的主导残差量级
和原始位置，而没有触发另一种输入或接口错误。

下一项有明确对象的诊断是：仅以同一实际 RK12 与同一 cusp grid 生成
零点线性化的候选初值，保留原 graphs、gains、scale、far Robin 边界与
完整非零 H，再交原 `evaluate(false)`。本回执尚未执行该候选，也未证明
原初猜积分网格差异是唯一根因。不能全局改 `linearSteps` 冒作“只改初猜”，
因为原 graphs 的末端及 gains 同时参与真正边界和残差尺度。

尚无新的 nonlinear tail 解、真实非零 H Jacobian 或 audit；尚无新的完整
联解接受父场。本课题完成条件仍未满足。

## 5. 小报告校验值

- `summary.json`（10968 B）：
  `5c9203ce46b44de31d187c3dce43f94f30524cb25c9beaf31b9d893f05d640b1`。
- `launcher-result.json`（33927 B）：
  `7e29222e2c5d87ce49ccd71c7170b34c4e1b0662998f974551812c9368fdf728`。
- `verified-launch-intent.json`（33653 B）：
  `21c9ff63afa7e3faf87ce51956db00b8836ac594bc48500477300f9e5a68bc52`。
- 原 graphs/gains 全 577 行、节点幅度全 577 行、所有 stage、两端全部模式
  与初猜相等记录，分别在 summary 所列 gzip evidence 中逐件 SHA 绑定。
