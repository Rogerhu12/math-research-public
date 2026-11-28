# R262-recover-actual-low35-frozen-h1

**数值记录。** 2026-11-28 17:28:29 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `418dffcd9c0b81b375cbd47d7d427c4747353595`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

仅恢复已登记同g实际h1父场，旧观察不当作新成果；上次父场a405277f3c7b1d6ce22c2edc490be177d9f6c3f74d9fba0505bfa5acae30b586。其过渡门仅13共同径行，旧.010603不能当独立全门径向或连续上界。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-recover-actual-low35-frozen-h1；实际源码逐文件摘要列于下方。开始 2026-11-28 17:27:54 UTC，结束 2026-11-28 17:28:29 UTC。退出码 0。

```json
{
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA256": "a405277f3c7b1d6ce22c2edc490be177d9f6c3f74d9fba0505bfa5acae30b586",
  "independent": {
    "peak": 0.010603353774122486,
    "rms": 0.0010689757419913898,
    "curvature": 7.5503286161470955,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.992612052586979,
    "worstPhysicalRadialAndNativeTheta": [
      0.9800000000000001,
      4.959803786436633
    ],
    "radialRows": 384,
    "angles": 273
  },
  "accepted": {
    "actualCompletedSteps": 4
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-three-arcs-fixed-metric-refinement.py: SHA-256 `0ac91cf431ec69f6246d490931dac97d37004d84b9d5438b633f2a302256640f` (7551 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- low35-h1.json: SHA-256 `b31ffc1008184747f18ea1f45f4a4fe224f9720be75e768a8f8bbb097cf27917` (7283 bytes).
- low35-h1.npz: SHA-256 `a405277f3c7b1d6ce22c2edc490be177d9f6c3f74d9fba0505bfa5acae30b586` (25990 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
