# R321-frozen-profile-new-metric-whole-half-h2-M54-true-curvature

**数值记录。** 2026-11-28 18:14:50 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `e3b870a198bb01f5440853541ae9d56ca6144df2`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

冻结 c857ec53 三剖面设计的同一 a294… 径向g，接实际49c15998…全半场；一次Boehm插入每个全径span的中点，并把真实D3原生位置频率M42升M54。以完整物理曲率有符号二次型和球包约束作五次GN尝试。四组亲本、真切口六jets、新尾误差、加密后独立峰与非零退出分别登记。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R321-frozen-profile-new-metric-whole-half-h2-M54-true-curvature；实际源码逐文件摘要列于下方。开始 2026-11-28 18:08:45 UTC，结束 2026-11-28 18:14:50 UTC。退出码 0。

```json
{
  "schema": "actual-full-half-same-metric-curvature-constrained-GN-v1",
  "sourceSHA": "86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841",
  "parentSHA": "c857ec536a45196154b1d5bfa6670fed39f9851079a25ebc2268a7a163a521a0",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "a5f0b093126d18154f659e208af44dc0783d570e0f194721fa9c43845dee74d1",
  "exactTailQueryReportSHA": "8888e19e0ed7a52b5cf389b5c218bfa5b3158d7740f1c6917b2e2380e65cbf7b",
  "exactTailQueryCacheSHA": "9ccf0d1eec413cb6e60533207c360cefc9f73143519f763a19b012219ca40d0a",
  "seedSHA": "49c159980375fc0bf8761678405f7d49e9a6005f6ff1077e63e6d01fe2d50197",
  "radialUnitSpans": 104,
  "positionVariables": 5665,
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
    0.00205692235808747,
    0.0011901411881849178,
    0.07256291047009815
  ],
  "actualTwoEndpointBasisZeroJets": [
    0.0,
    0.0,
    0.0
  ],
  "initial": {
    "peak": 0.0016748168197599242,
    "rms": 0.00015846187939614118,
    "curvature": 8.466533195495117,
    "worstMetric": [
      0.4757666666666666,
      0.6267516515889862,
      0.3727520301156961
    ],
    "worstCurvature": [
      0.4898990999050441,
      0.1410191216075219,
      0.031539071229176985
    ],
    "minimumSupport": 0.5645904525120484,
    "minimumZs": 0.0,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.0016748168197599242,
    "tailPeak": 0.00024059740569591103,
    "prefixCurvature": 8.466533195495117,
    "tailCurvature": 6.578281252000667,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "initialSecondary": {
    "peak": 0.0016750938193133278,
    "rms": 0.00020970576371545147,
    "curvature": 8.459007656891776,
    "worstMetric": [
      0.4749812350870913,
      0.626248288442117,
      0.37212632003377305
    ],
    "worstCurvature": [
      0.48703333333333326,
      0.13974135361931533,
      0.03119419924780875
    ],
    "minimumSupport": 0.56437792876757,
    "minimumZs": 0.0,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.0016750938193133278,
    "tailPeak": 0.00024066406109486744,
    "prefixCurvature": 8.459007656891776,
    "tailCurvature": 6.5483227408040605,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "accepted": {
    "actualCompletedSteps": 5
  },
  "initialIndependent": {
    "peak": 0.001674452752364376,
    "rms": 0.0002201093219467322,
    "curvature": 8.465052319286515,
    "worstMetric": [
      0.4757666666666666,
      0.6288850938655853,
      0.3754104512403692
    ],
    "worstCurvature": [
      0.4884273491170365,
      0.14164078690666335,
      0.031707440752463234
    ],
    "minimumSupport": 0.5644666288883342,
    "minimumZs": 0.0,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.001674452752364376,
    "tailPeak": 0.0002406711538012198,
    "prefixCurvature": 8.465052319286515,
    "tailCurvature": 6.580475200066989,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "independent": {
    "peak": 0.0013303880283733935,
    "rms": 0.00018152792366787324,
    "curvature": 8.688127888314586,
    "worstMetric": [
      0.3787000153666172,
      0.3512691515285251,
      0.119452774769483
    ],
    "worstCurvature": [
      0.5293750960413576,
      0.15863768133546297,
      0.036464289378088724
    ],
    "minimumSupport": 0.5468557658517952,
    "minimumZs": 0.0,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.0013303880283733935,
    "tailPeak": 0.000159404355827222,
    "prefixCurvature": 8.688127888314586,
    "tailCurvature": 6.481180160425602,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null,
    "maximumNorm": 1.890966014820989
  },
  "scope": "The common cut is interior to a single additional XYZ field. Original tail queries are evaluated at their exact saved binary radii and derived from the exact physical source; physical derivatives use the signed radial-arclength factor and its derivative. The true cuff and sleeve keep their prescribed two-jets. Any nonzero new addition on the tail requires its own continuous metric and thickness bounds.",
  "solverSHA": "e96cfe23be5717d847c3bc3d9decf6329a29c5eafef8ffcc274572de7524c99e",
  "wallSHA": "38c9316f48501ab087caa88f86538a3003d184f6ac37ec37b9e3968fa5938994",
  "directionProjections": [
    [
      {
        "rows": 12,
        "dualIterations": 2,
        "active": 5,
        "maximumAffineViolation": 0.013737021824615286,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 1,
        "normalStep": 1.8011947187166205e-05
      },
      {
        "rows": 22,
        "dualIterations": 2,
        "active": 12,
        "maximumAffineViolation": 0.015653273562577424,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 2,
        "normalStep": 4.829473925567951e-07
      },
      {
        "rows": 32,
        "dualIterations": 2,
        "active": 19,
        "maximumAffineViolation": 0.015967966717282206,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 3,
        "normalStep": 1.5622062765410026e-07
      },
      {
        "rows": 25,
        "dualIterations": 8,
        "active": 7,
        "maximumAffineViolation": -0.03307013131123822,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 1,
        "normalStep": 0.00011334991002086871
      },
      {
        "rows": 38,
        "dualIterations": 7,
        "active": 16,
        "maximumAffineViolation": -0.011401815326092947,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 2,
        "normalStep": 5.735354935585857e-06
      },
      {
        "rows": 51,
        "dualIterations": 6,
        "active": 24,
        "maximumAffineViolation": 0.005483745747933948,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 3,
        "normalStep": 3.8061301420853404e-06
      },
      {
        "rows": 14,
        "dualIterations": 4,
        "active": 5,
        "maximumAffineViolation": 0.00659608033357054,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 1,
        "normalStep": 2.3855095364830752e-05
      },
      {
        "rows": 25,
        "dualIterations": 4,
        "active": 10,
        "maximumAffineViolation": 0.000887323069454446,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 2,
        "normalStep": 7.630688294419039e-07
      },
      {
        "rows": 36,
        "dualIterations": 4,
        "active": 15,
        "maximumAffineViolation": 0.00020960439291896384,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 3,
        "normalStep": 1.646855399155464e-07
      }
    ],
    [
      {
        "rows": 47,
        "dualIterations": 8,
        "active": 22,
        "maximumAffineViolation": -0.009165448641197785,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 1,
        "normalStep": 0.0002099577155495804
      },
      {
        "rows": 73,
        "dualIterations": 9,
        "active": 30,
        "maximumAffineViolation": -0.012025899490148328,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 2,
        "normalStep": 9.052445316787916e-06
      },
      {
        "rows": 100,
        "dualIterations": 12,
        "active": 24,
        "maximumAffineViolation": -0.038077798697618105,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 3,
        "normalStep": 6.576581303214219e-06
      },
      {
        "rows": 47,
        "dualIterations": 8,
        "active": 22,
        "maximumAffineViolation": -0.010220425657252737,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 1,
        "normalStep": 0.0002003394489654187
      },
      {
        "rows": 73,
        "dualIterations": 12,
        "active": 18,
        "maximumAffineViolation": -0.01801419571791589,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 2,
        "normalStep": 9.50842679018376e-06
      },
      {
        "rows": 100,
        "dualIterations": 13,
        "active": 22,
        "maximumAffineViolation": 0.014851612141433651,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 3,
        "normalStep": 8.657989691678332e-06
      },
      {
        "rows": 47,
        "dualIterations": 15,
        "active": 14,
        "maximumAffineViolation": 0.007907819946052259,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 1,
        "normalStep": 9.494981347492432e-05
      },
      {
        "rows": 76,
        "dualIterations": 12,
        "active": 22,
        "maximumAffineViolation": -0.006177872658836594,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 2,
        "normalStep": 1.6283870281405652e-06
      },
      {
        "rows": 104,
        "dualIterations": 17,
        "active": 36,
        "maximumAffineViolation": -0.0017406665197726603,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 3,
        "normalStep": 5.374389912905295e-07
      }
    ],
    [
      {
        "rows": 60,
        "dualIterations": 13,
        "active": 27,
        "maximumAffineViolation": 0.08322144590050727,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 1,
        "normalStep": 0.000248031344810846
      },
      {
        "rows": 100,
        "dualIterations": 12,
        "active": 38,
        "maximumAffineViolation": 0.027409876132396496,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 2,
        "normalStep": 9.238478521427581e-06
      },
      {
        "rows": 140,
        "dualIterations": 13,
        "active": 67,
        "maximumAffineViolation": 0.06399892588729998,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 3,
        "normalStep": 4.00992959364929e-06
      },
      {
        "rows": 60,
        "dualIterations": 13,
        "active": 27,
        "maximumAffineViolation": 0.08711631184718471,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 1,
        "normalStep": 0.0002373598596155922
      },
      {
        "rows": 101,
        "dualIterations": 10,
        "active": 38,
        "maximumAffineViolation": 0.05581894163971245,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 2,
        "normalStep": 8.692360113792338e-06
      },
      {
        "rows": 141,
        "dualIterations": 12,
        "active": 65,
        "maximumAffineViolation": 0.10346118408975462,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 3,
        "normalStep": 1.2610257687204551e-05
      },
      {
        "rows": 28,
        "dualIterations": 0,
        "maximumAffineViolation": 0.0,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 1,
        "normalStep": 0.0
      }
    ],
    [
      {
        "rows": 64,
        "dualIterations": 11,
        "active": 36,
        "maximumAffineViolation": 0.03682974088028627,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 1,
        "normalStep": 0.00028724150675093715
      },
      {
        "rows": 113,
        "dualIterations": 16,
        "active": 70,
        "maximumAffineViolation": 0.07140951671717904,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 2,
        "normalStep": 6.468321573928384e-06
      },
      {
        "rows": 163,
        "dualIterations": 14,
        "active": 111,
        "maximumAffineViolation": 0.04806606086245008,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 3,
        "normalStep": 7.703565391361893e-06
      },
      {
        "rows": 63,
        "dualIterations": 21,
        "active": 26,
        "maximumAffineViolation": 0.05723321666010285,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 1,
        "normalStep": 0.00028109149023090223
      },
      {
        "rows": 113,
        "dualIterations": 11,
        "active": 63,
        "maximumAffineViolation": 0.02480417736133542,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 2,
        "normalStep": 1.1492769092488837e-05
      },
      {
        "rows": 151,
        "dualIterations": 12,
        "active": 100,
        "maximumAffineViolation": 0.04004942394054191,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 3,
        "normalStep": 7.968104832379308e-06
      },
      {
        "rows": 62,
        "dualIterations": 9,
        "active": 37,
        "maximumAffineViolation": 0.008305638414274988,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 1,
        "normalStep": 0.0001385928132401725
      },
      {
        "rows": 99,
        "dualIterations": 20,
        "active": 46,
        "maximumAffineViolation": 0.011759828077009937,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 2,
        "normalStep": 4.721284077988266e-06
      },
      {
        "rows": 147,
        "dualIterations": 28,
        "active": 64,
        "maximumAffineViolation": -0.00024867743613648965,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 3,
        "normalStep": 5.11344919873121e-06
      }
    ],
    [
      {
        "rows": 72,
        "dualIterations": 21,
        "active": 29,
        "maximumAffineViolation": 0.012815380266218108,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 1,
        "normalStep": 0.00026399004637951814
      },
      {
        "rows": 133,
        "dualIterations": 16,
        "active": 81,
        "maximumAffineViolation": 0.04630898190321179,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 2,
        "normalStep": 4.715783743487223e-06
      },
      {
        "rows": 196,
        "dualIterations": 21,
        "active": 103,
        "maximumAffineViolation": 0.017706343124214593,
        "power": 0.72,
        "damping": 1e-09,
        "sweep": 3,
        "normalStep": 2.559067575412866e-06
      },
      {
        "rows": 72,
        "dualIterations": 16,
        "active": 38,
        "maximumAffineViolation": 0.03953301936217088,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 1,
        "normalStep": 0.0002645540581474028
      },
      {
        "rows": 133,
        "dualIterations": 11,
        "active": 91,
        "maximumAffineViolation": 0.08306461360263157,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 2,
        "normalStep": 1.0151648507747687e-05
      },
      {
        "rows": 198,
        "dualIterations": 15,
        "active": 129,
        "maximumAffineViolation": -0.0011891797749038959,
        "power": 0.72,
        "damping": 1e-06,
        "sweep": 3,
        "normalStep": 5.2901648735668486e-06
      },
      {
        "rows": 65,
        "dualIterations": 15,
        "active": 32,
        "maximumAffineViolation": 0.0458022066366031,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 1,
        "normalStep": 0.0002061471609279114
      },
      {
        "rows": 124,
        "dualIterations": 10,
        "active": 82,
        "maximumAffineViolation": -0.00359245632403802,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 2,
        "normalStep": 6.732181882334308e-06
      },
      {
        "rows": 173,
        "dualIterations": 11,
        "active": 124,
        "maximumAffineViolation": 0.011699339734765082,
        "power": 0.72,
        "damping": 0.0003,
        "sweep": 3,
        "normalStep": 5.949689681710152e-06
      }
    ]
  ],
  "independent.maximumNorm": 1.890966014820989
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-full-half-curvature-constrained-newton-v2.py: SHA-256 `e96cfe23be5717d847c3bc3d9decf6329a29c5eafef8ffcc274572de7524c99e` (10883 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `91b0653ff3423fec27402e6f4b25cab1ebaefd4681794857c2c450b7354575ee` (111563 bytes).
- 2ecf-r262-full-half-curvature-constrained-newton-v2.py: SHA-256 `e96cfe23be5717d847c3bc3d9decf6329a29c5eafef8ffcc274572de7524c99e` (10883 bytes).
- 2ecf-physical-curvature-walls-and-banded-projection.py: SHA-256 `38c9316f48501ab087caa88f86538a3003d184f6ac37ec37b9e3968fa5938994` (6658 bytes).
- 2ecf-r262-full-half-cut-through-infinite-tail-xyz.py: SHA-256 `86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841` (13912 bytes).
- 2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py: SHA-256 `29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902` (13494 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r321-two-moment-inlet-profiles-all-span-banded.py: SHA-256 `05caa4008bfbf50fb7e2182445c4fced635d533c65510277d5f830ee4a3f32b1` (14321 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-small-input-full-xyz-positive-metric-v2.py: SHA-256 `152b08a6e60a2aced9ef3aca61543bbc7050471c68614fe1235d4a9e8fa363dc` (20817 bytes).
- 2ecf-r262-minkowski-physical-continuation.py: SHA-256 `87da8b2607d5cf22f7f71bbc3f63ccc21d4c0a2b10f47235b1300560f979f1b3` (11326 bytes).
- 2ecf-m12-h2-cached-direct-lm-v2.py: SHA-256 `b69d67754d935a4e4342c934f80e5272d520f86164804c710350cf412a805745` (5741 bytes).
- 6a65-m12-global-common-cut-position-recovered.py: SHA-256 `89d3f03e752dce04007166a8e540e3e49f1621ed725cd8e6b43475ea8101776a` (21022 bytes).
- 6a65-m12-entire-half-cartesian-bvp.py: SHA-256 `7214054f65bfbd1055122dddf235074bc812c88cdf5d418b630877bf8b21880b` (18390 bytes).
- 6a65-m12-original-tail-background.py: SHA-256 `cab284d7506523dbe56a2711a654764084ef0a5d253187bafcec965ca06da1dd` (15717 bytes).
- profile-fine-g-whole-h2-m54.json: SHA-256 `efd8fdeb68fc5b550604ae9270a6371568589b6d193ab0ad2976af82c0303e05` (27538 bytes).
- profile-fine-g-whole-h2-m54.npz: SHA-256 `a5f0b093126d18154f659e208af44dc0783d570e0f194721fa9c43845dee74d1` (59081 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
