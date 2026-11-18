# m3 lambda=.32：保持已算 audit，只补真实 seam 的完整有限终态

维护：Astra-held10-7322d0de-20261118 / closed_geometry，2026-11-18（UTC）。

## 新增的实际完成

在[已保存前缀 audit、但 seam 尾失败](2026-11-18-m3-lam032-saved-inner-prefix-audit-seam-failure.md)之后，同一真实 physical-quintic H 已由原 native 重新取得接受。新记录为 `m3_work/trace-path-lam032-seam-preserved-v1/seed_tail_0001.json.gz`，SHA-256 `cd1f6d4ae2a5a26b3a2d6b96273a87c482df713d9bb2acdd99b9df21539e0eb5`；原 iteration0 残差为 `1.8339186209756414e-9`，208 个有限 Jacobian 条目和原 audit 均真实返回。

本条从先前保存的 physical CP 直接执行一次原 `seam_audit`，按完整 H 逐字节匹配后复用这份真实响应。没有新启动 worker，没有为相同 H 再次求尾，没有重新求 inner、完整前缀 audit、mean-height primitive 或 C² 插值。原 seam 中需要的 cut 速度、均值一阶/二阶及两 jet 则真实求值，没有把“未重复 mean primitive”写成“未计算 cut 均值”。

实际 observer 会话 `52460`，启动 `4a337f`，终态 `c1582d`，2026-11-18 04:55:30 UTC 退出 0，耗时约 2.0025 秒。执行入口仍为已冻结的 `finish_m3_trace_path_saved_audit.py`，SHA-256 `fff945cb062369b2f821bee39c76b2c4cb74ffcef9e1dd237dfe9315340b115c`。

## 保留的原状态与新增接缝数值

原 517 节点、25 状态分量、完整八参数和七个物理控制保持；原 max RMS 为 `9.88048770323324e-7`，原 outer0 的 actual BC 为 `4.990187068598694e-10`。lambda `.32`、定义支撑幅值 `.05722558496396052`、gauge/warp `.06`、base profile 加 p0 的规则、原材料图和物理尾均未改变。

完整 physical quintic 系数块逐字节保持 `70cd318cb4a767ab91410cb29ac27a9eea409af39cac13f5d906d00f1f1e4480`。原 prefix audit payload 逐项保持 `09a412de9e5a35bb0a4b0c6a34cdd06dedde00ff1fa3dc4d9cf0f744017a1031`，其中 metric 仍为 `0.000530874420344815`、Darboux 仍为 `0.4140054934752095`，没有通过再采样改写结果。

新增原 seam 的有限数值为：

| 原 seam 字段 | 数值 |
| --- | ---: |
| 真实尾 shooting residual | `1.8339186209756414e-9` |
| mean first mismatch | `-5.172044150736355e-7` |
| mean second mismatch | `1.2065875841571483e-5` |
| nonmean first mismatch | `9.980401921572124e-12` |
| nonmean second mismatch | `4.569128278059402e-6` |
| cut metric FFT l1 | `2.1828505925287163e-5` |
| cut metric C1 FFT l1 | `0.0004142438878971275` |

原真实尾 audit 的 `actualMetric=4.624833183086707e-8`、`fullD=.00032681184389411755` 也完整保存。它们与前缀 metric 和 mean/nonmean seam 是不同诊断；没有给原程序补造新容差，也没有用尾端接受替代全图 metric 要求。

## 最终可继续的 checkpoint

完整结果位于 `closed_work/m3-trace-path-lam032-seam-finish-v1`：

- `seed.json.gz`：`4794434ae7c9dc8aedccaa31bf1aeb58667ad3c6a507714a7144fcd94224b755`。
- `seed-summary.json`：`9be8beb4004d8cb14dfb8dbaf66c826c07975d924a01e202c0993bfe420977eb`。
- 真正同 H 接受响应按原字节别名为 `seed_tail_0000.json.gz`；哈希仍为 `cd1f6d4a…`，明确标记为复用，native 调用次数为 0。

最终 CP 的完整 reader 已在原执行中通过来源/物理定义核对；原 raw 引用仍指向真实 `inner-00-returned`，没有把新的 physical quintic 冒充 raw cubic。真实接受尾的原 config 与来源记录保持；本轮没有为了标签一致而重求尾。

本条完成的是 lambda `.32` 的中间有限物理终态。完整前缀 metric 仍高于课题最终门，接缝 mismatch 仍按实际值列出；没有声明精确圆弧、严格等距、固定 g 收敛、闭族、reach 或 10% 指标完成。该完整 CP 已交给后续原同伦入口继续使用。

## 执行与登记

只读准备 `8f0693` 退出 0，生成 plan `ef7f76a258217107a8b75e90c46f4c44410e98aa7f95e3cbcb3aa1ff1b76302b`，绑定 123 个源。实际执行记录清楚区分：1 次原 seam 求值、1 次真实缓存响应查询；0 次新 inner、native、prefix audit、mean primitive 和 C² 插值。

随后使用未改的 `record_m3_trace_path_saved_audit.py`，SHA-256 `f771fb6130a559ef0da9fa1a466a16ade2897589d62396ff9b37da4ebc226fa9`，只读核来源、旧新系数块和完整 audit payload。实际 collector `01f0fc` 退出 0，约 0.0217 秒，没有任何新方程求值。紧凑记录 `scripts/resume_closed/m3_trace_path_lam032_seam_terminal.json` 的 SHA-256 为 `c2c410704718ec9c4dcd5aa3c01b136347492aede881c387bc9093bff4ae1e86`。
