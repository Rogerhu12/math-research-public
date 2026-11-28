# R321-two-moment-actual-frozen-full-physical-inlet-with-required-source

**数值记录。** 2026-11-28 17:45:11 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `16f65fb97a8f6c6b515b02621f69ec8b61539b01`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

恢复缺失真实源码后继续本项先前五秒退出的实际任务；不重跑任何已成功数学结果。R321自己的新两矩r/r_v/r_vv与.040真窗口，对冻结自己的g加N/k、真入口差、ez/k²三真实列和全带状Newton，完整六jets、四组不同真法角网与全span；新的状态profile身份不混R317。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R321-two-moment-actual-frozen-full-physical-inlet-with-required-source；实际源码逐文件摘要列于下方。开始 2026-11-28 17:44:01 UTC，结束 2026-11-28 17:45:11 UTC。退出码 0。

```json
{
  "entrySHA256": "05caa4008bfbf50fb7e2182445c4fced635d533c65510277d5f830ee4a3f32b1",
  "stateSHA256": "f638dc99f7edd7a54dbbd3fff3614aa593812088004d642ae50ec1c8a0f1b95f",
  "parentSHA256": "a02d19c65ad08eafae0ec350f5053b26d1b0f84bf90f70d3d978c04147d5b593",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "physicalSourceSHA256": "29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902",
  "cutSHA256": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "actualPositionVariables": 1326,
  "initial": {
    "peak": 0.002708060630093434,
    "rms": 0.0007307490852572024,
    "curvature": 5.784611446058914,
    "worstMetric": [
      0.46819999999999995,
      1.0471975511965976,
      1.047197551196597
    ],
    "worstCurvature": [
      0.457896120380567,
      4.276056667386108,
      4.207038255367545
    ],
    "minimumSupport": 0.5923721409217885,
    "minimumZs": 0.22630577980495212,
    "minimumArea": 0.11999999946243713
  },
  "initialSecondary": {
    "peak": 0.0027092044701326756,
    "rms": 0.0007432025990166177,
    "curvature": 5.787489227017383,
    "worstMetric": [
      0.46731760667406685,
      3.141592653589793,
      3.1415926535897913
    ],
    "worstCurvature": [
      0.457541139451228,
      4.276872241802927,
      4.207223809487482
    ],
    "minimumSupport": 0.5924403194267286,
    "minimumZs": 0.2263070274766381,
    "minimumArea": 0.12020687651814196
  },
  "initialGuard": {
    "peak": 0.002676895791325961,
    "curvature": 5.7960846051416155,
    "minimumSupport": 0.5925019748874706,
    "minimumArea": 0.12006358917684039,
    "minimumZs": 0.22628744162512757,
    "worstMetric": [
      0.55,
      4.603120920243557,
      4.350653826318314
    ],
    "worstCurvature": [
      0.4526666666666666,
      4.281030403596454,
      4.208176409062597
    ],
    "rms": 0.0006825752925975256,
    "radialRows": 163,
    "angles": 789
  },
  "accepted": {
    "actualCompletedSteps": 5
  },
  "attempts": [
    {
      "step": 1,
      "accepted": true
    },
    {
      "step": 2,
      "accepted": true
    },
    {
      "step": 3,
      "accepted": true
    },
    {
      "step": 4,
      "accepted": true
    }
  ],
  "normalAndRhsAgreement": [
    8.147148050568813e-16,
    4.70439189478226e-16
  ],
  "finalAngularGuard": {
    "peak": 0.002115760021053394,
    "curvature": 6.8533860756599765,
    "minimumSupport": 0.5983450645773907,
    "minimumArea": 0.12006358917684039,
    "minimumZs": 0.21998721838017699,
    "worstMetric": [
      0.476,
      3.532257025020648,
      3.777997394434188
    ],
    "worstCurvature": [
      0.476,
      4.302733979787057,
      4.2133438405665835
    ],
    "rms": 0.0007711464478388037,
    "radialRows": 163,
    "angles": 789
  },
  "initialIndependent": {
    "peak": 0.0026964883360363527,
    "curvature": 5.780979094411693,
    "minimumSupport": 0.5925218521441986,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.22643909490451136,
    "worstMetric": [
      0.4711333333333333,
      3.1452161745281892,
      3.1481149341884263
    ],
    "worstCurvature": [
      0.4455333333333333,
      4.283001749184701,
      4.208631958514704
    ],
    "rms": 0.0006798651793424928,
    "radialRows": 163,
    "angles": 1161
  },
  "independent": {
    "peak": 0.0021340470552876486,
    "curvature": 6.86548997579979,
    "minimumSupport": 0.5983632724360224,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.21998718097124018,
    "worstMetric": [
      0.4711333333333333,
      3.5365564358750152,
      3.78361195047133
    ],
    "worstCurvature": [
      0.4711333333333333,
      4.30474287481508,
      4.213840236037056
    ],
    "rms": 0.0007728679425093764,
    "radialRows": 163,
    "angles": 1161
  },
  "twoMomentCoefficients": [
    -0.3778248033946554,
    -0.376143427008282
  ],
  "R317PreservedRadiusSourceSHA": "94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6",
  "trueTransitionAngleGrids": [
    {
      "fullUniform": 216,
      "additionalMaterialTargets": 90,
      "perTransitionInterior": 13,
      "originalMaterialInverseError": 8.881784197001252e-16
    },
    {
      "fullUniform": 321,
      "additionalMaterialTargets": 138,
      "perTransitionInterior": 21,
      "originalMaterialInverseError": 8.881784197001252e-16
    },
    {
      "fullUniform": 579,
      "additionalMaterialTargets": 210,
      "perTransitionInterior": 33,
      "originalMaterialInverseError": 8.881784197001252e-16
    },
    {
      "fullUniform": 867,
      "additionalMaterialTargets": 294,
      "perTransitionInterior": 47,
      "originalMaterialInverseError": 8.881784197001252e-16
    }
  ],
  "coordinateEvaluatorsAgreement": [
    0.0,
    0.0
  ]
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r321-two-moment-inlet-profiles-all-span-banded.py: SHA-256 `05caa4008bfbf50fb7e2182445c4fced635d533c65510277d5f830ee4a3f32b1` (14321 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `549d65009e9ef037a5d23c71577965aedd6ca7ec014883867e84cd12bfe3ec7e` (88830 bytes).
- 2ecf-r321-two-moment-inlet-profiles-all-span-banded.py: SHA-256 `05caa4008bfbf50fb7e2182445c4fced635d533c65510277d5f830ee4a3f32b1` (14321 bytes).
- 2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py: SHA-256 `29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902` (13494 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py: SHA-256 `ffa687858a059ab60e14987d55acdd1a7d63c62855f7804f2d2ccc2966cebfd0` (14160 bytes).
- h1-physical-inlet.json: SHA-256 `a8633f6eeb0381471cce325fdb151e42001e5c0d863c69d364662a114be45ae3` (16408 bytes).
- h1-physical-inlet.npz: SHA-256 `f638dc99f7edd7a54dbbd3fff3614aa593812088004d642ae50ec1c8a0f1b95f` (18092 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
