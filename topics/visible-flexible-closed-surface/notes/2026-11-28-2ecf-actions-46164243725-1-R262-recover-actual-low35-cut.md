# R262-recover-actual-low35-cut

**数值记录。** 2026-11-28 17:27:49 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `e749cc9c533ad238cf2647b0bb31e9153630ea94`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

仅恢复已登记 low=.35、lambda=1、c=.78 的真实cut粗态，以便后继用实际数组精化；旧结论不重登记。上次实际状态SHA为538a7ecc1c65ae01d070056eb7b7fdd5b495e1083bce6c038a34bef1ed01d49b；本次若不同则明确新身份。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-recover-actual-low35-cut；实际源码逐文件摘要列于下方。开始 2026-11-28 17:27:29 UTC，结束 2026-11-28 17:27:49 UTC。退出码 0。

```json
{
  "finalIndependent": {
    "peak": 0.02607781770335018,
    "rms": 0.0016966245190830872,
    "curvature": 6.69372807157824,
    "positiveMetricCoefficientLower": 0.9794880954510434,
    "areaRatioMinimum": 0.987439548302391,
    "worstPhysicalRadialAndNativeTheta": [
      0.9133333333333334,
      4.945994587959316
    ],
    "radialRows": 224,
    "angles": 195
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- low35.json: SHA-256 `6eb4be1404f4531d40d15e5c70ab37e184d1128599b19212b7513aaae9af5a4d` (9831 bytes).
- low35.npz: SHA-256 `538a7ecc1c65ae01d070056eb7b7fdd5b495e1083bce6c038a34bef1ed01d49b` (10895 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
