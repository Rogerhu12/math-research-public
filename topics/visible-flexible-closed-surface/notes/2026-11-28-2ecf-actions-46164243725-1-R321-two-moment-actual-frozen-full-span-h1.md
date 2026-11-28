# R321-two-moment-actual-frozen-full-span-h1

**数值记录。** 2026-11-28 17:24:41 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `0c6ab3b207ce9b64bbe1bbf73fe11f37a884edc9`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R321新.040两矩真实母线自己的g固定后做实际Boehm和角精化。每span独立径行、769加全六个真实法角窗观察，完整原X+C+W与全部新XYZ保持自己的源身份；不当作R317旧g的精化。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R321-two-moment-actual-frozen-full-span-h1；实际源码逐文件摘要列于下方。开始 2026-11-28 17:23:56 UTC，结束 2026-11-28 17:24:41 UTC。退出码 0。

```json
{
  "entrySHA256": "6111d3c9e256807258d56f95bdd0869100bf1ab42cb0aa30a3038da8f821a0e8",
  "physicalSourceSHA256": "29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "parentSHA256": "639df9782b3da6c064513f8d64e532a623c74817149caab1b71aa751fdaf6361",
  "stateSHA256": "a02d19c65ad08eafae0ec350f5053b26d1b0f84bf90f70d3d978c04147d5b593",
  "angularModes": 30,
  "radialSpans": 40,
  "actualPositionDOFs": 1209,
  "metricDOFs": 0,
  "knotTransferMaxActual0th1st2nd": [
    5.204170427930421e-18,
    4.5102810375396984e-17,
    1.2490009027033011e-15
  ],
  "initialTraining": {
    "peak": 0.007615607231132915,
    "rms": 0.0007755520984728173,
    "curvature": 6.337208551207148,
    "positiveMetricCoefficientLower": 0.9668205354346655,
    "areaRatioMinimum": 0.9964443523569305,
    "worstPhysicalRadialAndNativeTheta": [
      0.4752373555555555,
      3.5682286929661844
    ],
    "radialRows": 290,
    "angles": 162
  },
  "initialShifted": {
    "peak": 0.007613220812071585,
    "curvature": 6.34005418674836,
    "areaRatioMinimum": 0.9964232736506111,
    "worstPhysicalRadialAndNativeTheta": [
      0.47366467407407403,
      1.4747918698906572
    ],
    "positiveMetricCoefficientLower": 0.9668205354346655,
    "minimumOutwardSupport": 0.5980819784658709,
    "minimumRadialHeightDerivative": 0.2282991138014695,
    "heightRange": [
      0.0,
      1.7721142884249084
    ],
    "maximumOriginNorm": 1.8932261617219381,
    "minimumArea": 0.12000400497223701,
    "uniformPeak": 0.007613220812071585,
    "additionalTransitionPeak": 0.005339883539403477,
    "rms": 0.0007865692841595294,
    "radialRows": 413,
    "angles": 847,
    "uniformShiftedNativeAngles": 769,
    "actualMaterialTransitionAngles": 78,
    "maximumNativeAngleInversionError": 8.881784197001252e-16,
    "radialCoverage": {
      "interiorPerActualSpan": 9,
      "numberOfSpans": 41,
      "sampledActualSpans": [
        0.35,
        2.021775895105453
      ],
      "gateInteriorRows": 59
    }
  },
  "initialGeometry": {
    "minimumOutwardSupport": 0.5982275165291845,
    "at": [
      0.5641262444444445,
      3.141592653589793
    ],
    "minimumRadialHeightDerivative": 0.22829727156518564,
    "heightRange": [
      0.0,
      1.772114288708474
    ],
    "maximumOriginNorm": 1.8932212704328695,
    "minimumArea": 0.11999999946243713
  },
  "accepted": {
    "actualCompletedSteps": 3
  },
  "training": {
    "peak": 0.0027045839806770777,
    "rms": 0.0004348047895069872,
    "curvature": 5.725756913469505,
    "positiveMetricCoefficientLower": 0.9668205354346655,
    "areaRatioMinimum": 0.9982087972126535,
    "worstPhysicalRadialAndNativeTheta": [
      0.4641262444444444,
      1.0471975511965976
    ],
    "radialRows": 290,
    "angles": 162
  },
  "independent": {
    "peak": 0.0027091852277314477,
    "curvature": 5.796606209135277,
    "areaRatioMinimum": 0.9981965335722481,
    "worstPhysicalRadialAndNativeTheta": [
      0.4662572666666666,
      3.141592653589793
    ],
    "positiveMetricCoefficientLower": 0.9668205354346655,
    "minimumOutwardSupport": 0.5923607943781386,
    "minimumRadialHeightDerivative": 0.22633441008802027,
    "heightRange": [
      0.0,
      1.7721142884249084
    ],
    "maximumOriginNorm": 1.8931322380423687,
    "minimumArea": 0.12000400497223701,
    "uniformPeak": 0.0027091852277314477,
    "additionalTransitionPeak": 0.002677077388255992,
    "rms": 0.0004351196897515012,
    "radialRows": 413,
    "angles": 847,
    "uniformShiftedNativeAngles": 769,
    "actualMaterialTransitionAngles": 78,
    "maximumNativeAngleInversionError": 8.881784197001252e-16,
    "radialCoverage": {
      "interiorPerActualSpan": 9,
      "numberOfSpans": 41,
      "sampledActualSpans": [
        0.35,
        2.021775895105453
      ],
      "gateInteriorRows": 59
    }
  },
  "independentGeometry": {
    "minimumOutwardSupport": 0.5923607943781386,
    "minimumRadialHeightDerivative": 0.22633441008802027,
    "heightRange": [
      0.0,
      1.7721142884249084
    ],
    "maximumOriginNorm": 1.8931322380423687,
    "minimumArea": 0.12000400497223701
  },
  "trainingActualSpanCoverage": {
    "interiorPerActualSpan": 6,
    "numberOfSpans": 41,
    "sampledActualSpans": [
      0.35,
      2.021775895105453
    ],
    "gateInteriorRows": 41
  },
  "trueSpatialMomentCoefficients": [
    -0.3778248033946554,
    -0.376143427008282
  ],
  "trueNormalEndpointAngles": [
    0.536,
    0.576
  ],
  "R317SourceSHA": "94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6"
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-two-moment-frozen-metric-refinement.py: SHA-256 `6111d3c9e256807258d56f95bdd0869100bf1ab42cb0aa30a3038da8f821a0e8` (16735 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-r262-two-moment-frozen-metric-refinement.py: SHA-256 `6111d3c9e256807258d56f95bdd0869100bf1ab42cb0aa30a3038da8f821a0e8` (16735 bytes).
- fixed-h1.json: SHA-256 `7d79667762db9d1e4d189c8fc3aaa008b2d198586c69cc1d48d3a20b8d450bbe` (8750 bytes).
- fixed-h1.npz: SHA-256 `a02d19c65ad08eafae0ec350f5053b26d1b0f84bf90f70d3d978c04147d5b593` (26174 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
