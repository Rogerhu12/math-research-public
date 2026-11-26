# 旧固定 g 的活动面入口修复后实际方向

2026-11-26，Astra-larger-e4e2a2bf-20261126。真实公开 [run45762076394/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45762076394) stage61，完整逐字命令与读数见[第6卷](2026-11-26-public-actions-45762076394-1-part-006.md)。独立物理 base 修复后的完整活动面方向已成功返回；不把这次成功冒充先前 stage43 内层 traceback 已被读取。

## 实际源与父

checkout `f5c74ec8742d6370602cd51c73c261667c28be39`，launcher `618e5a988b733430dfe706897f4f695702b743e7f4a9953b651b5955ac89f36d`，独立物理 base adapter `8c3d11bb55c029ffcae23b126d566108947e9a92523574a53bfda7a4556f487f`。原完整 body/roles 核验后的物理 base 实际读为 `b1b0725acffde7958d9a4ad245057ea243d4319bde15bd9a7778ade3b0f844e8`，模型 R671；原父实际 driver 为 `1e709d869b3b2ef5e4d818ee8b8737c9bfcfe2f4f21ed9ad7b7dd4f06f495dd3`。本次完整实际 driver 为 `f6f9e8d4d6bd2e054a8a5f7c1612c6c1ead61dd02194c85025686ada0b903a7d`，原 v5 QP 源 `76b27520a433d85a52c3037ed5d519860b1002b0fb137378c855dad2993855e8` 未替换。

真正父场为 `d4bc3506e6aeef1180c9f7ede70f2aa6552d6505db80b00a0842f98c79d9704e`。新场为

`954fd4358441f6781396a316083a0f66519af74c0e2663077c7fd23b7012aa9f`。

完整修复语义见[原发布说明](2026-11-26-face-PCG-verified-physical-base-launcher-repair.md)：不改 parent 声明谱系，不把 derived driver SHA 当物理 base，原 literal DRIVER_SHA 比较和所有旧 source 守卫仍执行。当前计划报告确认 `raw_positions_read=true`，未以旧地点摘要代替实际输入。

## 实际单方向结果

| 项 | 实际返回 |
|---|---|
| 原/末 μ | `.012063248414946114`，未改变 |
| 原同固定 g Phi | `1.2412028206171362e-7` |
| 末同固定 g Phi | `1.221419986194176e-7` |
| 末 max relative Gram | `.013183911186764208` |
| 最终接受 | 原 ray，alpha `.5` |
| QP | `fullspace-feasible-active-set-face-metric-PCG-v5` |
| 内层状态 | `iteration_limit`，明确256预算 |
| 最后 Pg / 实际容差 | `3.4548154751235747e-8` / `1.1153055834258866e-12` |
| 原 J / J* 调用 | `265 / 266` |
| 完整旧行 SOC | 实际 attempted=true、accepted=false |
| 最终必要曲率筛 | true |
| 子进程退出码 / 实际控制器秒数 | `0 / 707.650064464` |

这是一次真实下降，但远未达到 README 的全域误差或求解驻点。此旧目标的谱参数和单位不可与新 physical-mean 或深谷目标的 Phi 互相相减。本次摘要没有给出 SOC 的完整真实拒绝类别或预条件耗时；已经排的独立纯报告归因继续读取，不预猜。

report 为19474080 B / `bc5621ce0957211b6cf29def235f9b95b93ae0ec2fd4189682d5176043f4d2b3`；final 为10377496 B / 上述954f。reference JSON/NPZ 分别为 `63f24fbcaaccc177ea7d02e5e79f4a457eb50344e1a1f9537ab7e91a9eb3d4ed` / `3d5063c868245c155b6258f47d0ed5059ee48ae98da520f930a7e08153332cc8`；实际 continuation plan 123895 B / `7f7621c0ba8e4f8830b86a7ed1938827a047789ba2847f286c96ec85b49ca70c`。全量 report/plan 和数组留 runner。

没有缺失输出。成功 report 不含 `source_commit` 键，控制器只对该摘要路径记一项缺失；实际源码 checkout 已在控制器的步骤记录中完整返回，不能把摘要键缺失当成科学方向失败。

该场尚无自己的连续 first/完整K/四标记证书，不迁入父场证书。后继先读这条真实方向归因，同时继续已排的幅度保护多轮分离与新固定深谷目标的完整求解；当前全部未付完成标准保持。
