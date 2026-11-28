# M12 / N256 / 半幅原尾真实接受；资源屏障后续 M16

日期：2026-11-28。小记录：[2026-11-28-tail-m12-halfheight-accepted.json](2026-11-28-tail-m12-halfheight-accepted.json)。

在修正原 audit 的 radix-2 前提后，**真实 M12 / N256 / f=.5 请求已完整通过原非线性残差与 audit 门**：

- residual：`4.737446564795518e-10`；原第三次 Newton 更新后的 fresh-final-J 返回。
- 原 sampled audit actualMetric：`7.549521606768208e-14`；normalizedFullDefect：`2.0785510546490448e-8`；formalCurvature：`8.148045697296691`。
- 原 audit minLeading：`.8200817837254577`；minD：`.9995941334989237`。
- 接受包 SHA：`ccba27ff6af8686f24197591e9314fedf96f15ebfdb431971a5616ad573f296c`；native manifest SHA 与完整状态行数保存在小记录。请求包含原 M24 源 H 的前 12 个分量，逐项乘 `.5^j`；不是完整源 H，也没有请求最终完整 height Jacobian。

随后段 b 的 summary 为 `original_tail_route_failed`，具体原因是父会话预先要求的 **M16 输出目录资源交接屏障**。它在 M16 `mkdir` 时触发 `FileExistsError`，发生在任何 M16 native source 构造或方程执行之前；不是 M12 数学失败，也没有使上述真接受包失效。

段 c 已实际从此包续接 M16 / N256 / f=.5，使用 2 个原 native workers，为同时进行的原前缀计算保留内存。M12 的接受请求没有重算，原方程、Frenet、残差、audit 与后续完整 M24 / N512 的 full-H/J 要求没有修改。M16 与完整 M24 的结果仍待其各自真实返回，公共 Cartesian 接缝与闭图仍未由本条证明。
