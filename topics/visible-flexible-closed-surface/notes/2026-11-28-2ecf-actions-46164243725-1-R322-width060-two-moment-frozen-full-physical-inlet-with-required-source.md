# R322-width060-two-moment-frozen-full-physical-inlet-with-required-source

**数值记录。** 2026-11-28 17:46:46 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `ef4bcb7f2b238e8a74792bac7b61e9e210268e44`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

恢复缺失真实源码后继续本项先前五秒退出的实际任务；不重跑任何已成功数学结果。R322自己的新两矩r/r_v/r_vv与.060真窗口，对冻结自己的g加N/k、真入口差、ez/k²三真实列和全带状Newton，完整六jets、四组不同真法角网与全span；新的状态profile身份不混R317。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R322-width060-two-moment-frozen-full-physical-inlet-with-required-source；实际源码逐文件摘要列于下方。开始 2026-11-28 17:45:31 UTC，结束 2026-11-28 17:46:46 UTC。退出码 0。

```json
{
  "entrySHA256": "0b37497cd3ee7cc8378aab0475e9ed06eee8e2315dcd73609b2050b8f3167629",
  "stateSHA256": "6eac8473f4d90c5e7ed160701278bbf421e82c30c4cd53557bde939275a218bc",
  "parentSHA256": "100f7c8b312cb8be95cb8a46db340345ee560e4ba0d1ad7bc13da05cd49d2a9a",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "physicalSourceSHA256": "e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e",
  "cutSHA256": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "actualPositionVariables": 1326,
  "initial": {
    "peak": 0.0026875572229063463,
    "rms": 0.0007333530689082676,
    "curvature": 7.935283472417243,
    "worstMetric": [
      0.46819999999999995,
      5.177810114249844,
      5.131503933532943
    ],
    "worstCurvature": [
      0.4726905973284028,
      4.30514548825268,
      4.213940116718384
    ],
    "minimumSupport": 0.5930352736729909,
    "minimumZs": 0.22548890503029706,
    "minimumArea": 0.11999999946243713
  },
  "initialSecondary": {
    "peak": 0.002702281529155193,
    "rms": 0.0007444649924568506,
    "curvature": 7.863058121116272,
    "worstMetric": [
      0.4641989136299813,
      5.177266397971964,
      5.130531914242564
    ],
    "worstCurvature": [
      0.4770940738969057,
      4.296446027806602,
      4.211810828305119
    ],
    "minimumSupport": 0.5931134671477107,
    "minimumZs": 0.22552643722182703,
    "minimumArea": 0.12020687651814196
  },
  "initialGuard": {
    "peak": 0.0026417866242872345,
    "curvature": 7.9361320302532725,
    "minimumSupport": 0.5931346097527358,
    "minimumArea": 0.12006358917684039,
    "minimumZs": 0.2254996016721212,
    "worstMetric": [
      0.4526666666666666,
      5.17087702741118,
      5.119119050263374
    ],
    "worstCurvature": [
      0.476,
      4.302733979787057,
      4.2133438405665835
    ],
    "rms": 0.0006854917792851495,
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
    7.466531537092722e-16,
    4.403851084402835e-16
  ],
  "finalAngularGuard": {
    "peak": 0.0021155590976804067,
    "curvature": 7.424680516730633,
    "minimumSupport": 0.597407369278854,
    "minimumArea": 0.12006358917684039,
    "minimumZs": 0.2244970189671659,
    "worstMetric": [
      0.476,
      5.17087702741118,
      5.119119050263374
    ],
    "worstCurvature": [
      0.49066666666666664,
      4.302733979787057,
      4.2133438405665835
    ],
    "rms": 0.0007845162608094609,
    "radialRows": 163,
    "angles": 789
  },
  "initialIndependent": {
    "peak": 0.002663797747695852,
    "curvature": 7.931243588605961,
    "minimumSupport": 0.5931521177070241,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.22560308038915627,
    "worstMetric": [
      0.4711333333333333,
      5.181634941907041,
      5.138345119398703
    ],
    "worstCurvature": [
      0.4711333333333333,
      4.30474287481508,
      4.213840236037056
    ],
    "rms": 0.000683602889344936,
    "radialRows": 163,
    "angles": 1161
  },
  "independent": {
    "peak": 0.0021546491048935685,
    "curvature": 7.428501890661854,
    "minimumSupport": 0.5977445730310793,
    "minimumArea": 0.11999999946243713,
    "minimumZs": 0.22449616133542802,
    "worstMetric": [
      0.4711333333333333,
      5.174387900030247,
      5.125388028607359
    ],
    "worstCurvature": [
      0.49326666666666663,
      4.30474287481508,
      4.213840236037056
    ],
    "rms": 0.0007847051067262437,
    "radialRows": 163,
    "angles": 1161
  },
  "twoMomentCoefficients": [
    -0.5190218744366847,
    -0.5511349532277711
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

- 2ecf-r322-two-moment-060-inlet-profiles-all-span-banded.py: SHA-256 `0b37497cd3ee7cc8378aab0475e9ed06eee8e2315dcd73609b2050b8f3167629` (14321 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `549d65009e9ef037a5d23c71577965aedd6ca7ec014883867e84cd12bfe3ec7e` (88830 bytes).
- 2ecf-r322-two-moment-060-inlet-profiles-all-span-banded.py: SHA-256 `0b37497cd3ee7cc8378aab0475e9ed06eee8e2315dcd73609b2050b8f3167629` (14321 bytes).
- 2ecf-r262-adjacent-low-ports-two-moment-060-physical-cut.py: SHA-256 `e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e` (13494 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py: SHA-256 `ffa687858a059ab60e14987d55acdd1a7d63c62855f7804f2d2ccc2966cebfd0` (14160 bytes).
- h1-physical-inlet.json: SHA-256 `93060921f752477d6ac041a15f5ddd7579abc8fd38ccdf84201c7ee93c5d01ab` (16378 bytes).
- h1-physical-inlet.npz: SHA-256 `6eac8473f4d90c5e7ed160701278bbf421e82c30c4cd53557bde939275a218bc` (18091 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
