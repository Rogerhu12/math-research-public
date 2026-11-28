# R321-actual-full-half-same-g-curvature-constrained-refinement-v2

**数值记录。** 2026-11-28 18:08:11 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `be78d5b4275c3fdef82d483f6ffc937a61cdfe78`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

同一R321固定g全半场真实Boehm/42模精化，用当前实际六jet的两主方向曲率仿射约束和1.915球切平面，在同一带状Gram Hessian解非负对偶投影。原整网真实Gram/κ验步，独立1109角+每过渡57真角；没有把事后挡曲率的停滞视为数学障碍。 原5ee后继已实际因迭代记录覆盖grid变量在末网KeyError退出；本不同源只改该实现冲突和每接受步临时checkpoint，不重跑已成f18f全尾，直接从原已有seed继续未登记的约束后继。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R321-actual-full-half-same-g-curvature-constrained-refinement-v2；实际源码逐文件摘要列于下方。开始 2026-11-28 18:03:06 UTC，结束 2026-11-28 18:08:11 UTC。退出码 0。

```json
{
  "schema": "actual-full-half-same-metric-curvature-constrained-GN-v1",
  "sourceSHA": "86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841",
  "parentSHA": "a02d19c65ad08eafae0ec350f5053b26d1b0f84bf90f70d3d978c04147d5b593",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "02ce0e028afabf5a4652e9b6fd86888c279b91868d7eb7ebb9e26f5e02c7b1ca",
  "exactTailQueryReportSHA": "8888e19e0ed7a52b5cf389b5c218bfa5b3158d7740f1c6917b2e2380e65cbf7b",
  "exactTailQueryCacheSHA": "9ccf0d1eec413cb6e60533207c360cefc9f73143519f763a19b012219ca40d0a",
  "seedSHA": "f18f1fe6df153b7a77911143118df9e4b7a86006ec019818f2a2d2c2d3b33c18",
  "radialUnitSpans": 104,
  "positionVariables": 4429,
  "metricVariables": 0,
  "physicalCommonCut": 2.021775895105453,
  "physicalCuffCoordinate": 2.4717758951054534,
  "grids": [
    {
      "angular": {
        "fullUniform": 401,
        "additionalMaterialTargets": 114,
        "perTransitionInterior": 17,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "actualAngles": 87,
      "prefixRows": 654,
      "exactTailRadiusQueries": 3949,
      "originalGauss": 12,
      "tailSplit": "all original training rule",
      "trueCuff": 0.14999999999999997,
      "minimumTailH": 0.8732778474409361,
      "maximumTailH": 1.171949217293111,
      "minimumTailRadius": 0.14999999999999997,
      "maximumTailRadius": 0.5999948998639338,
      "baseSixJetTraceDifference": [
        0.0,
        5.551115123125783e-17,
        1.5700924586837752e-16,
        0.0,
        2.482534153247273e-16,
        3.3306690738754696e-16
      ],
      "baseAngularRadiusTraceDifference": 2.220446049250313e-16,
      "commonCutTraceMapRank": 3,
      "positiveInteriorSupportColumns": 5
    },
    {
      "angular": {
        "fullUniform": 607,
        "additionalMaterialTargets": 186,
        "perTransitionInterior": 29,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "actualAngles": 134,
      "prefixRows": 774,
      "exactTailRadiusQueries": 2304,
      "originalGauss": 12,
      "tailSplit": "even local indices in original higher rule",
      "trueCuff": 0.14999999999999997,
      "minimumTailH": 0.8732804832893022,
      "maximumTailH": 1.1719492071098017,
      "minimumTailRadius": 0.14999999999999997,
      "maximumTailRadius": 0.5999962062388967,
      "baseSixJetTraceDifference": [
        0.0,
        5.551115123125783e-17,
        1.5700924586837752e-16,
        0.0,
        3.1401849173675503e-16,
        3.140376573195942e-16
      ],
      "baseAngularRadiusTraceDifference": 2.220446049250313e-16,
      "commonCutTraceMapRank": 3,
      "positiveInteriorSupportColumns": 5
    },
    {
      "angular": {
        "fullUniform": 1109,
        "additionalMaterialTargets": 354,
        "perTransitionInterior": 57,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "actualAngles": 245,
      "prefixRows": 874,
      "exactTailRadiusQueries": 2304,
      "originalGauss": 12,
      "tailSplit": "odd local indices in original higher rule",
      "trueCuff": 0.14999999999999997,
      "minimumTailH": 0.8732788773552393,
      "maximumTailH": 1.1719492181925415,
      "minimumTailRadius": 0.14999999999999997,
      "maximumTailRadius": 0.5999802061751804,
      "baseSixJetTraceDifference": [
        2.220446049250313e-16,
        5.551115123125783e-17,
        1.5700984480997602e-16,
        0.0,
        3.1401849173675503e-16,
        3.140376573195942e-16
      ],
      "baseAngularRadiusTraceDifference": 2.220446049250313e-16,
      "commonCutTraceMapRank": 3,
      "positiveInteriorSupportColumns": 5
    }
  ],
  "actualMeanAndFullFrequencyCommonCutCoefficientTraceMax": [
    0.00030839685280992246,
    0.0003871198709465024,
    0.016864553980449906
  ],
  "actualTwoEndpointBasisZeroJets": [
    0.0,
    0.0,
    0.0
  ],
  "initial": {
    "peak": 0.002616382242823387,
    "rms": 0.00022073241315152838,
    "curvature": 8.116091449760217,
    "worstMetric": [
      0.46271575201715054,
      0.9714650599629285,
      0.9113989516559136
    ],
    "worstCurvature": [
      1.3671853608599993,
      0.0,
      0.0
    ],
    "minimumSupport": 0.5900301451462945,
    "minimumZs": 0.0,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.002616382242823387,
    "tailPeak": 5.313466571044145e-05,
    "prefixCurvature": 8.116091449760217,
    "tailCurvature": 6.394676303894627,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "initialSecondary": {
    "peak": 0.002616988416651402,
    "rms": 0.0002959404089281098,
    "curvature": 8.124339784166365,
    "worstMetric": [
      0.4623666666666666,
      0.9678382639559989,
      0.9049488926044827
    ],
    "worstCurvature": [
      1.364866240110101,
      0.0,
      0.0
    ],
    "minimumSupport": 0.590033003068352,
    "minimumZs": 0.0,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.002616988416651402,
    "tailPeak": 5.3016031208219516e-05,
    "prefixCurvature": 8.124339784166365,
    "tailCurvature": 6.398827598847363,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "accepted": {
    "actualCompletedSteps": 4
  },
  "initialIndependent": {
    "peak": 0.002616319083949236,
    "rms": 0.00031165948476353974,
    "curvature": 8.119933984668462,
    "worstMetric": [
      0.46480006146646885,
      0.9688229824415773,
      0.9066994384810332
    ],
    "worstCurvature": [
      1.3637778177988618,
      0.0,
      0.0
    ],
    "minimumSupport": 0.5900331378962456,
    "minimumZs": 0.0,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.002616319083949236,
    "tailPeak": 5.3412466923807855e-05,
    "prefixCurvature": 8.119933984668462,
    "tailCurvature": 6.36942368568637,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "independent": {
    "peak": 0.00215865904230137,
    "rms": 0.0002685069888119599,
    "curvature": 8.695557736321877,
    "worstMetric": [
      0.4855666666666666,
      0.9744886139178438,
      0.9167816267862975
    ],
    "worstCurvature": [
      0.524302368325308,
      0.07931884066773148,
      0.01646091434222414
    ],
    "minimumSupport": 0.5552750898370683,
    "minimumZs": 0.0,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.00215865904230137,
    "tailPeak": 4.04543561929569e-05,
    "prefixCurvature": 8.695557736321877,
    "tailCurvature": 6.450335546328873,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null,
    "maximumNorm": 1.8928164210370744
  },
  "scope": "The common cut is interior to a single additional XYZ field. Original tail queries are evaluated at their exact saved binary radii and derived from the exact physical source; physical derivatives use the signed radial-arclength factor and its derivative. The true cuff and sleeve keep their prescribed two-jets. Any nonzero new addition on the tail requires its own continuous metric and thickness bounds.",
  "solverSHA": "e96cfe23be5717d847c3bc3d9decf6329a29c5eafef8ffcc274572de7524c99e",
  "wallSHA": "38c9316f48501ab087caa88f86538a3003d184f6ac37ec37b9e3968fa5938994",
  "directionProjections": [
    [
      {
        "rows": 45,
        "dualIterations": 10,
        "active": 11,
        "maximumAffineViolation": 0.008678182413944533,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 1,
        "normalStep": 5.3071957117285676e-05
      },
      {
        "rows": 79,
        "dualIterations": 10,
        "active": 21,
        "maximumAffineViolation": 0.007835112770540276,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 2,
        "normalStep": 9.89380432653394e-07
      },
      {
        "rows": 113,
        "dualIterations": 8,
        "active": 31,
        "maximumAffineViolation": -0.023405443725742395,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 3,
        "normalStep": 6.150319675719378e-06
      },
      {
        "rows": 44,
        "dualIterations": 10,
        "active": 11,
        "maximumAffineViolation": 0.004852808750595009,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 1,
        "normalStep": 4.947208193897023e-05
      },
      {
        "rows": 77,
        "dualIterations": 9,
        "active": 22,
        "maximumAffineViolation": -0.0067238349568149915,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 2,
        "normalStep": 1.925424928493475e-06
      },
      {
        "rows": 110,
        "dualIterations": 9,
        "active": 31,
        "maximumAffineViolation": -0.005413713100663495,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 3,
        "normalStep": 1.9196342627032312e-07
      },
      {
        "rows": 31,
        "dualIterations": 10,
        "active": 6,
        "maximumAffineViolation": 0.014225291154299853,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 1,
        "normalStep": 2.2447609270674396e-05
      },
      {
        "rows": 48,
        "dualIterations": 10,
        "active": 13,
        "maximumAffineViolation": 0.01580905152805431,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 2,
        "normalStep": 3.393052352338073e-07
      },
      {
        "rows": 65,
        "dualIterations": 9,
        "active": 20,
        "maximumAffineViolation": 0.01965494229936245,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 3,
        "normalStep": 2.0956153331453997e-07
      }
    ],
    [
      {
        "rows": 68,
        "dualIterations": 20,
        "active": 32,
        "maximumAffineViolation": 0.08247256148464788,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 1,
        "normalStep": 0.00028823120334892105
      },
      {
        "rows": 133,
        "dualIterations": 20,
        "active": 51,
        "maximumAffineViolation": 0.03739925244286604,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 2,
        "normalStep": 1.8231446532505323e-05
      },
      {
        "rows": 198,
        "dualIterations": 22,
        "active": 76,
        "maximumAffineViolation": 0.025631409080080315,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 3,
        "normalStep": 4.469001742258111e-06
      },
      {
        "rows": 70,
        "dualIterations": 21,
        "active": 25,
        "maximumAffineViolation": 0.006026648639143967,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 1,
        "normalStep": 0.00025910030638211283
      },
      {
        "rows": 135,
        "dualIterations": 20,
        "active": 56,
        "maximumAffineViolation": 0.0367844964912752,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 2,
        "normalStep": 5.8516775441658635e-06
      },
      {
        "rows": 199,
        "dualIterations": 31,
        "active": 62,
        "maximumAffineViolation": 0.022096082129776283,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 3,
        "normalStep": 5.187700528845003e-06
      },
      {
        "rows": 72,
        "dualIterations": 16,
        "active": 37,
        "maximumAffineViolation": -0.012050325171122877,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 1,
        "normalStep": 0.00014965401831613093
      },
      {
        "rows": 140,
        "dualIterations": 28,
        "active": 44,
        "maximumAffineViolation": 0.00812089443743901,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 2,
        "normalStep": 6.238735989766946e-06
      },
      {
        "rows": 211,
        "dualIterations": 19,
        "active": 99,
        "maximumAffineViolation": 0.026569649633502602,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 3,
        "normalStep": 4.355470544979072e-06
      }
    ],
    [
      {
        "rows": 80,
        "dualIterations": 18,
        "active": 28,
        "maximumAffineViolation": 0.060968719865310245,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 1,
        "normalStep": 0.0002731383818790416
      },
      {
        "rows": 159,
        "dualIterations": 31,
        "active": 53,
        "maximumAffineViolation": 0.04784679600358988,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 2,
        "normalStep": 0.0001170129552382242
      },
      {
        "rows": 245,
        "dualIterations": 22,
        "active": 102,
        "maximumAffineViolation": 0.01303899915481957,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 3,
        "normalStep": 8.557858502629876e-06
      },
      {
        "rows": 80,
        "dualIterations": 22,
        "active": 23,
        "maximumAffineViolation": 0.014966270485837261,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 1,
        "normalStep": 0.0002562797390386595
      },
      {
        "rows": 159,
        "dualIterations": 23,
        "active": 64,
        "maximumAffineViolation": 0.009667125581658697,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 2,
        "normalStep": 9.792457792552708e-05
      },
      {
        "rows": 244,
        "dualIterations": 37,
        "active": 68,
        "maximumAffineViolation": 0.017733061707675725,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 3,
        "normalStep": 6.599625946446286e-06
      },
      {
        "rows": 77,
        "dualIterations": 12,
        "active": 40,
        "maximumAffineViolation": 0.03736186269621678,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 1,
        "normalStep": 0.00021519829752052793
      },
      {
        "rows": 158,
        "dualIterations": 43,
        "active": 49,
        "maximumAffineViolation": 0.03260582139863538,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 2,
        "normalStep": 2.9899811934949127e-05
      },
      {
        "rows": 245,
        "dualIterations": 35,
        "active": 79,
        "maximumAffineViolation": 0.03874376141564944,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 3,
        "normalStep": 7.392700547651432e-06
      }
    ],
    [
      {
        "rows": 72,
        "dualIterations": 26,
        "active": 26,
        "maximumAffineViolation": 0.04455412280770041,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 1,
        "normalStep": 0.0002899328456116387
      },
      {
        "rows": 152,
        "dualIterations": 12,
        "active": 113,
        "maximumAffineViolation": 0.06820049648186287,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 2,
        "normalStep": 0.00013376062032555773
      },
      {
        "rows": 234,
        "dualIterations": 17,
        "active": 117,
        "maximumAffineViolation": 0.02398798585909347,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 3,
        "normalStep": 1.1249704539433875e-05
      },
      {
        "rows": 73,
        "dualIterations": 23,
        "active": 22,
        "maximumAffineViolation": 0.04908202617137025,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 1,
        "normalStep": 0.0002688144379127102
      },
      {
        "rows": 152,
        "dualIterations": 22,
        "active": 64,
        "maximumAffineViolation": 0.012595709207752338,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 2,
        "normalStep": 0.00012616658937107293
      },
      {
        "rows": 241,
        "dualIterations": 23,
        "active": 102,
        "maximumAffineViolation": 0.011698421809686546,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 3,
        "normalStep": 3.832367333834676e-06
      },
      {
        "rows": 82,
        "dualIterations": 14,
        "active": 34,
        "maximumAffineViolation": 0.01352721557964909,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 1,
        "normalStep": 0.00016715399500941006
      },
      {
        "rows": 157,
        "dualIterations": 30,
        "active": 44,
        "maximumAffineViolation": 0.008173158831896435,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 2,
        "normalStep": 2.5565189769395852e-05
      },
      {
        "rows": 250,
        "dualIterations": 31,
        "active": 99,
        "maximumAffineViolation": 0.07679269958588524,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 3,
        "normalStep": 4.3821733190737355e-06
      }
    ]
  ],
  "independent.maximumNorm": 1.8928164210370744
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-full-half-curvature-constrained-newton-v2.py: SHA-256 `e96cfe23be5717d847c3bc3d9decf6329a29c5eafef8ffcc274572de7524c99e` (10883 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `c20429e2ce897d7c7239b0ee1ce85f48f1ad5ec558e41720fd967248d614f05a` (105935 bytes).
- 2ecf-physical-curvature-walls-and-banded-projection.py: SHA-256 `38c9316f48501ab087caa88f86538a3003d184f6ac37ec37b9e3968fa5938994` (6658 bytes).
- 2ecf-r262-full-half-cut-through-infinite-tail-xyz.py: SHA-256 `86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841` (13912 bytes).
- 2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py: SHA-256 `29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902` (13494 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r321-two-moment-inlet-profiles-all-span-banded.py: SHA-256 `05caa4008bfbf50fb7e2182445c4fced635d533c65510277d5f830ee4a3f32b1` (14321 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-full-half-curvature-constrained-newton-v2.py: SHA-256 `e96cfe23be5717d847c3bc3d9decf6329a29c5eafef8ffcc274572de7524c99e` (10883 bytes).
- h1-whole-true-tail-constrained-h2-v2.json: SHA-256 `c0fe80c2abd848e8d33c03ff417182988878b97430052f3377f750f9a239609f` (23765 bytes).
- h1-whole-true-tail-constrained-h2-v2.npz: SHA-256 `02ce0e028afabf5a4652e9b6fd86888c279b91868d7eb7ebb9e26f5e02c7b1ca` (46821 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
