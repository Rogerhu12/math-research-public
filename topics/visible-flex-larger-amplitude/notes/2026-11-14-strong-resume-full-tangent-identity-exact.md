# 新旧完整尾工厂身份的逐位比较

**状态：数值记录与精确文件比较；不是新的闭曲面或全审计前缀解。**

margin325 实际 r3 的首个新 H 经原 576-stage 非线性尾求解，于 2026-11-14 06:53:29 UTC 返回 `converged=true`、残差 2.34189151390313e−10，低于原 2e−9 门。该次原外层请求是 `jacobian=true,audit=false`，故只表明当前 H 的完整数值响应与 J，不能替代最终 audit。原工厂已实际写出当前完整切线 snapshot；前缀继续在第一大 J 中运行。

将新 manifest 与真正 A 的原 manifest 内 `identityCanonical` 按原 typed-JSON/Float64LE 形式直接比较，八个顶层字段中只有 `sourceSha256` 不同。其余七个字段——`backendIdentity`、`farGraph`、`parameters`、`physicalIdentity`、`radius`、`rawNode`、`stageLayout`——完整逐位相同。这包括全部 stored-g 指纹、所有非 IO 参数、完整远端 graph 与每个 stage 的几何记录，并非只比较三个低模。

源散列表从 120 项变为 129 项：原 120 项全部存在且 SHA 不变，恰好多出前条已列的九个后来诊断 MJS。至此可确切判定 r2 原可选 snapshot 的失败由保守整目录源散列表增加导致；没有几何、参数、远端线性图或 stage 布局变化。原比较器并未修改。r3 采用原 raw 状态重新构建的响应，已经给出同一尾工厂的真实新 H 计算。

配套 JSON 给出两个 manifest 的 SHA、九项新增源 SHA 及全部比较项。这里仅归档新 identity manifest 供逐位比较，不归档这次运行的十个可重生 tangent sidecars，故不能把此小包称作可直接恢复的完整 snapshot。所有完整侧文件仍在运行中的稳定 RT，后续新接受态可按同树完整身份正常复用。较大的前缀与最终审计结果仍待本次真实 BVP 完成。
