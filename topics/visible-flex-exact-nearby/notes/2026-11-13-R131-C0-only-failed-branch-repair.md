# R131：保留真实失败门的 v2 序列化修复

2026-11-13。原 R131 的 `.005` 成功脚本、证明、报告和 manifest 保持原样。

## 实际异常及修复

将原消费者用于 root 的完整 `[0,1/20]` compact 残差报告时，零阶管门
确实失败。原脚本在失败行把未认证的角导数上界设为 `arb.pos_inf()`；
`record` 随后生成浮点 infinity，最终被 `allow_nan=False` 的严格 JSON
编码拒绝。因此原运行没有写出失败报告。这是失败分支的报告代码错误，
不改变已成功的 `[0,1/200]` 数学证书。

独立原样重跑复现了 `ValueError: Out of range float values are not JSON compliant`，
退出码为 1，预定输出不存在。完整异常和输入 SHA 保存于：

- `2026-11-13-R131-v1-failure-serialization-raw.txt`；
- `2026-11-13-R131-v1-failure-serialization-audit.json`。

新脚本 `scripts/fourfold_codazzi_linear_degeneracy_v2.py` 只将失败行的
`actual_first_angular_derivative_upper` 改为 `null`，并增加明确的
`actual_first_angular_derivative_certified=false`。所有有限输入、误差屏障、
余量及失败 gate 保留；顶层 `continuation_certified=false`。
它没有删除失败盒、扩大管宽或把失败回写成成功。

## 完整 compact 输入上的真实失败

完整请求区间为 `[0,1/20]`，producer 已包含全部 150 个闭盒。
R131 v2 在从 0 开始的第 112 个盒（零起算索引 111）遇到首个失败：

\[
\left[
\frac{5476377146882523}{144115188075855872},
\frac{5548434740920451}{144115188075855872}
\right]
\approx[0.038,0.0385].
\]

通过前缀的末零阶屏障为 `0.060569266514237409...`。
下一盒尝试的终值为 `0.063170238466659468...`，超过预定管宽
$1/16=0.0625$，所以 `C0_inside_tube=false`。
该尝试的仿射微分余量仍为正，约 $5.5273\times10^{-14}$；
尝试的 gap 余量约 `0.11995044779` 也为正，但这些**失败盒中的尝试值**
不能称为整个失败盒的真实解界，因为用于零阶 Lipschitz 常数的预定管
已经没有闭合。保存这些数值只是为了说明失败发生在哪里。

报告 `2026-11-13-R131-C0-only-r005-compact-failed-native.json.gz`
保存全部通过盒及完整首失败盒，`covered_interval` 只到上述左端。
文件名的 `r005` 沿用 compact producer 命名，表示 `.05`，不是 `.005`。
这不是曲面不存在的证明，也不是 `K=0` 或实际 `C=0` 的诊断。

## 固定文件及输入

| 文件/输入 | SHA-256 |
|---|---|
| v2 consumer | `3a179c671c4b2ab7f237875d8da64e8f7c7fa7599c0038ba326c3cecd8c630fa` |
| v2 真实失败报告 | `d3b6070ed5ac4d49ff0a009f1c45545cb82492012fbfbaaba9a02d7dca097f57` |
| 原异常 audit | `89df5c7434a1f8c1005797fac2a4dfa68679e7e960896be11294fe5878fbb327` |
| 原异常全文 | `996d32be9184bad91f0b81344e7ee184a08f9579480d9a31108d15486083f2ba` |
| compact producer | `51e454ad8aa1209d3199169d52cf8cf3df49d8728da8914db251ebddc363f6d0` |
| high target jets provider | `ea71aefd62bf0c16c9e9c9fe4a5da5ce95a973cf913825bd875a4ba59fc14168` |
| 完整 `.05` 有限候选 | `1fdb86b3f959cd3137cf06bdbb37637643a1a56143152c7e26b622d7b353dd81` |

完整输入 native 报告的 SHA、原消费者 SHA 和原始对象 SHA 均在 audit
及 v2 报告中保存。两次 native 运行读取同一输入，旧异常与修复后的
真实失败因此可以逐项对应。
