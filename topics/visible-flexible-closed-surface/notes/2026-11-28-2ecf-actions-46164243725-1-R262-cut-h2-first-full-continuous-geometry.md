# R262-cut-h2-first-full-continuous-geometry

**数值记录。** 2026-11-28 18:23:49 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `d7d539f3f337b02995dab9ab9ea64fc4851a2e16`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

直接消费真实cut后首个原W单元及其全部物理交格，准确原Hermite/原W/新XYZ/真中央/全部六jets进入同一个连续区间核。这是新场局部几何计算；其输出仅覆盖明列区间，不作整闭证书。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-cut-h2-first-full-continuous-geometry；实际源码逐文件摘要列于下方。开始 2026-11-28 18:23:34 UTC，结束 2026-11-28 18:23:49 UTC。退出码 0。

```json
{
  "completed": true,
  "allSelectedPassed": true,
  "originalFieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA256": "9a3958fa2f008855599a34e01cb96090dbffeaf741502c34e714152ad140332e",
  "selected": [
    56
  ],
  "commonRefinedRows": 4,
  "acceptedBoxes": 384,
  "unresolvedBoxes": 0,
  "firstUnresolved": [],
  "acceptedDirectedMinima": {
    "height": 0.7799999996427767,
    "support": 0.8675812716854633,
    "area2": 0.03999422411363363,
    "curvatureFormMin": 0.05695590455872806
  },
  "limits": {
    "curvature": "200/23",
    "support": "23/200",
    "height": "87/250"
  },
  "geometryFamily": "true-cut-and-sleeve",
  "seconds": 11.798013206000178
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-true-three-arcs-cut-or-height-directed-geometry.py: SHA-256 `686f35574755f303355e07ff06b778865917fb7410ec674337fd0eeeabaa8cc5` (13282 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r262-true-three-arcs-cut-directed-position-kernel.py: SHA-256 `ce0593ff10e6b0b07d2d4cae0eceaf649bc44d42785fd25f9cc161350a0a87d1` (9241 bytes).
- 2ecf-r262-true-three-arcs-cut-or-height-directed-geometry.py: SHA-256 `686f35574755f303355e07ff06b778865917fb7410ec674337fd0eeeabaa8cc5` (13282 bytes).
- h2-first-geometry.json: SHA-256 `e651c2abf73561665ffee01317a40c61cadc14cb9e470122e46ac35497cd0356` (2668 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
