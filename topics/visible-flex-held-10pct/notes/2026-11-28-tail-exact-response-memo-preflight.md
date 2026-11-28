# 完整真实响应的严格复用入口与 coupled 图输入门

本条记录一项实际只读预检和尚未正向执行的新后继入口。完整数值记录见
[`2026-11-28-tail-exact-response-memo-preflight.json`](2026-11-28-tail-exact-response-memo-preflight.json)，
SHA256 `460d4e531f4f5be155dd8e0030b21e6236bb749e40d3355969ff12366db6db9a`。
观察时 E 的完整 H 请求仍在原 worker 中运行，未返回接受包。本条没有把这次请求、
复用或闭合图声称为成功；E 与旧 outer wrapper 均未修改。

## 已实际核验的兼容性

`m24-tail-settings.json` 的每个原配置值与 E attempt-001 的实际配置相同。
E 仅另外声明 `chordMaxCorrections=3`、trace 路径和初猜包路径；新后继同样明确
保留 chord3，仅改变两个执行路径。两侧 native manifest 的固定有限范围、
运行库和双 worker 设置相同，原 executable、CPP、header、parallel wrapper、
parallel plan 五项 SHA 逐项相同。owned source 的唯一字节差异是
`native_batch_adapter.mjs` 中完整 source-root 绝对路径的替换，且这项替换已逐字验证。
没有忽略任何数值配置差异，也没有用另一个内核冒充原来源。

以真实正在运行的 E summary 的原字节快照调用新严格门，实际返回
`ValueError('Only a genuinely returned complete original full-height response is reusable')`。
该观察没有启动新的 native 请求。五个源文件均通过 Python 语法编译；正向复用与
coupled 图加载尚未执行，必须等真实全 H 接受与原 outer 门返回。

## 新独立执行路径

`verified_tail_response_memo.py` 绑定完整请求的 canonical JSON、全部 H 的 binary64
字节、原完整数值/数学配置、全部 owned source、native 来源、原包 SHA、完整状态、
真实末次 fresh native J，以及完整 height J/audit。当前初猜必须就是该真实接受包。
`traceFile` 与 `initialCheckpoint` 是仅有的两个可不同配置项，且必须为字符串路径；
不会排除其他配置或任何数值项。每次复用前重新核验所有绑定。

只有字面相同的完整请求才按原字节复制先前真实 gzip 包。原 packet 中的 config、
history、来源和返回值都不改写；单独 sidecar 明示“先前完整响应复用”，不把它记成
新的 native 计算。请求有任何差别就委托原 client。原 client 为 BVP 边界计算已有的
非 audit 响应缓存继续保留，sidecar 分别记载其缓存命中和真正的新 worker 请求。

`prefix_resource_tail_memo_driver.py` 在独立加载的 client 类上安装此门，并原样使用
v2 的入口/内部径向分块与只读 Fourier 表缓存。它分别绑定真实外层 argv 和委托的
v2 argv。`couple_actual_prefix_memoized.py` 仍支付原完整前缀 BVP、全部未知、原
RMS/domain/边界门、八次 outer 预算和完整尾 H/J/audit。其最终 height binding
额外保存真实 packet 的 native record 目录与 manifest；若末包来自字面复用，后续
几何导出必须读取先前真正计算的目录，不能把新的逻辑 record 名当作新 native 来源。

## 真正 coupled source 的几何适配

`actual_cartesian_coupled_prefix.py` 单独验证真实 outer summary、run、原有限门、
所有 source/input/执行 sidecar、完整 raw/physical 场和末次完整 endpoint packet。
它保留 `actual_tail_requested` 和真实命令，未把 coupled run 改称 linear run。
最后一次 `seam_audit` 从 physical endpoint 求出的 H 单独成为尾部输入；raw collocation
candidate H 保留原样。二者即使只差舍入位，也不得强行混为同一字面数组。

新 adapter 继续使用原 `ActualR53CartesianPrefix`，保完整 exact-core lift、来源
angular count、GL6 和已声明的新共享 Hermite mean，没有改 root 当前使用的 prefix 类。
当前独立入口 `actual_closed_map_coupled_v3.py --coupling-summary ...` 显式选择这条输入门，并要求几何 bundle
同时绑定真实末 packet 与该 physical-endpoint H 文件。无此参数的原线性 source 路径不变。
此外 `ActualCutTarget` 文档明确：`ap=-1/sqrt(1+w²)` 等是唯一实数表达式；浮点缓存不是
独立定义常数。nearcut 只对有限扰动 V 重参数化，背景和度量仍用物理 R，其条带成本须另付。

这些来源门和入口既不构成完整 H 的正向返回，也不构成 C²/metric/reach/held/同题收敛
验收。后继仍由真实 E 的返回触发，随后执行原 coupling 与完整尾几何。

## 预检后的逐字节迁移

原 JSON 保留实际预检时的路径和 SHA，不倒改历史。当时带 coupled 选项的 v2 源随后由
root 逐字节保存为独立 `actual_closed_map_coupled_v3.py`，SHA 仍为
`ee5745c809c635fec21c2b2121daa2fdbcb5133b33896c53228c627dbcb3e764`。
已绑定 cut 合同的 `actual_closed_map_v2.py` 恢复为仅增定义说明的版本，SHA
`3742d3041daad388cc26d63fb7e4300732459f076327938a39ef92b7f3603ee5`，后续不修改。
逐字节相同已重新实核；迁移记录见
[`2026-11-28-tail-exact-response-memo-migration.json`](2026-11-28-tail-exact-response-memo-migration.json)。
历史 JSON 的 v2 路径是观察时路径，其所指源字节现由独立 v3 完整保存；不应把后来
恢复 v2 的哈希差异当作历史检查重新执行，也不应把历史检查谎称发生于 v3 路径。
