# R319-actual-h1-one-XYZ-through-entire-true-tail

**数值记录。** 2026-11-28 17:38:25 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `d553728e658e66b7410cb810dd9029b0e6185cf3`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

以已成功的104a884…真实R319 h1作父态，固定同一g，把新XYZ真正延到全部原尾/真cuff，S为内部可变六jet缝，只有袖和真平领两端钳0/1/2阶。尾以原保存半径、真实有向弧长H/Hq求六jets，保全部角项与实际独立尾峰。新非零尾不继承旧局部metric/法管；本项只据真实结果登记。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R319-actual-h1-one-XYZ-through-entire-true-tail；实际源码逐文件摘要列于下方。开始 2026-11-28 17:36:30 UTC，结束 2026-11-28 17:38:25 UTC。退出码 0。

```json
{
  "schema": "actual-new-strong-half-same-metric-full-XYZ-across-r06-to-the-true-cuff-v1",
  "sourceSHA": "86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841",
  "parentSHA": "104a8843272816e31129ff8fabce2dbfad6ad98b41f16975496f91dc1b19181d",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "d54f3a0963ed834479631fed38d3a89968c1b8e133aa12817fb90715734239a9",
  "exactTailQueryReportSHA": "8888e19e0ed7a52b5cf389b5c218bfa5b3158d7740f1c6917b2e2380e65cbf7b",
  "exactTailQueryCacheSHA": "9ccf0d1eec413cb6e60533207c360cefc9f73143519f763a19b012219ca40d0a",
  "radialUnitSpans": 52,
  "positionVariables": 1887,
  "metricVariables": 0,
  "physicalCommonCut": 2.021775895105453,
  "physicalCuffCoordinate": 2.4717758951054534,
  "grids": [
    {
      "angular": {
        "fullUniform": 240,
        "additionalMaterialTargets": 102,
        "perTransitionInterior": 15,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "actualAngles": 58,
      "prefixRows": 434,
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
        3.140376573195942e-16,
        3.1402328324212615e-16
      ],
      "baseAngularRadiusTraceDifference": 2.220446049250313e-16,
      "commonCutTraceMapRank": 3,
      "positiveInteriorSupportColumns": 5
    },
    {
      "angular": {
        "fullUniform": 351,
        "additionalMaterialTargets": 162,
        "perTransitionInterior": 25,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "actualAngles": 87,
      "prefixRows": 554,
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
        2.2204502844110104e-16,
        3.1401849173675503e-16
      ],
      "baseAngularRadiusTraceDifference": 2.220446049250313e-16,
      "commonCutTraceMapRank": 3,
      "positiveInteriorSupportColumns": 5
    },
    {
      "angular": {
        "fullUniform": 621,
        "additionalMaterialTargets": 294,
        "perTransitionInterior": 47,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "actualAngles": 154,
      "prefixRows": 646,
      "exactTailRadiusQueries": 2304,
      "originalGauss": 12,
      "tailSplit": "odd local indices in original higher rule",
      "trueCuff": 0.14999999999999997,
      "minimumTailH": 0.8732788773552393,
      "maximumTailH": 1.1719492181925415,
      "minimumTailRadius": 0.14999999999999997,
      "maximumTailRadius": 0.5999802061751804,
      "baseSixJetTraceDifference": [
        0.0,
        5.594315114139762e-17,
        1.5700924645328253e-16,
        0.0,
        2.482594761251414e-16,
        3.140376573195942e-16
      ],
      "baseAngularRadiusTraceDifference": 2.220446049250313e-16,
      "commonCutTraceMapRank": 3,
      "positiveInteriorSupportColumns": 5
    }
  ],
  "actualMeanAndFullFrequencyCommonCutCoefficientTraceMax": [
    0.0004910423263149886,
    0.007982876531787676,
    0.12889323266086739
  ],
  "actualTwoEndpointBasisZeroJets": [
    0.0,
    0.0,
    0.0
  ],
  "initial": {
    "peak": 0.004991619276091132,
    "rms": 0.0003383400862299077,
    "curvature": 8.662159665447234,
    "worstMetric": [
      0.4726905973284028,
      0.6283185307179586,
      0.3747034597077537
    ],
    "worstCurvature": [
      0.4726905973284028,
      0.0,
      0.0
    ],
    "minimumSupport": 0.5953704531769622,
    "minimumZs": -2.5776236057809258e-09,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.004991619276091132,
    "tailPeak": 5.295414201997818e-10,
    "prefixCurvature": 8.662159665447234,
    "tailCurvature": 6.424492816892881,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "initialSecondary": {
    "peak": 0.00501753590774417,
    "rms": 0.0004860908871234202,
    "curvature": 8.667827757297609,
    "worstMetric": [
      0.47506666666666664,
      0.6354788558543456,
      0.38369228927776483
    ],
    "worstCurvature": [
      0.47562477824491844,
      0.0,
      0.0
    ],
    "minimumSupport": 0.5953769812340786,
    "minimumZs": -2.576085426802553e-09,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.00501753590774417,
    "tailPeak": 5.435508573314617e-10,
    "prefixCurvature": 8.667827757297609,
    "tailCurvature": 6.428917515304164,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "accepted": {
    "actualCompletedSteps": 5
  },
  "matrixAndRhsAgreement": [
    2.6595964637424495e-15,
    4.2099155457139016e-16
  ],
  "initialIndependent": {
    "peak": 0.005017673379195575,
    "rms": 0.0005248548774565647,
    "curvature": 8.666160435007434,
    "worstMetric": [
      0.4743755463879139,
      0.6374245963805377,
      0.3861550171477494
    ],
    "worstCurvature": [
      0.4743755463879139,
      0.0,
      0.0
    ],
    "minimumSupport": 0.5953723056131056,
    "minimumZs": -2.5777622626167116e-09,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.005017673379195575,
    "tailPeak": 5.429267074733872e-10,
    "prefixCurvature": 8.666160435007434,
    "tailCurvature": 6.394066119213662,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "independent": {
    "peak": 0.0020826516349473634,
    "rms": 0.00034398386252731874,
    "curvature": 8.680442812546952,
    "worstMetric": [
      0.464505198294894,
      1.0471975511965976,
      1.047197551196597
    ],
    "worstCurvature": [
      0.4743755463879139,
      0.10117850736199012,
      0.02147291647363173
    ],
    "minimumSupport": 0.5977046353545238,
    "minimumZs": -0.0008011765307702723,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.0020826516349473634,
    "tailPeak": 0.0005310394009414576,
    "prefixCurvature": 8.680442812546952,
    "tailCurvature": 6.413154593527533,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "scope": "The common cut is interior to a single additional XYZ field. Original tail queries are evaluated at their exact saved binary radii and derived from the exact physical source; physical derivatives use the signed radial-arclength factor and its derivative. The true cuff and sleeve keep their prescribed two-jets. Any nonzero new addition on the tail requires its own continuous metric and thickness bounds."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-full-half-cut-through-infinite-tail-xyz.py: SHA-256 `86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841` (13912 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `82a1e922cb947b8f7986d7b6a123c9bbed2ed878e85b1c0a2dedce3159e6ee97` (78638 bytes).
- 2ecf-r262-full-half-cut-through-infinite-tail-xyz.py: SHA-256 `86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841` (13912 bytes).
- 2ecf-r262-adjacent-low-ports-support-physical-cut.py: SHA-256 `94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6` (12244 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r262-three-arcs-full-cut-span-frozen-metric-refinement.py: SHA-256 `494059a37c8414119c4834db624193ea7dafb85ba62485cf1a5cb47030942bae` (10367 bytes).
- 2ecf-r262-adjacent-cut-true-normal-angle-cauchy-refinement.py: SHA-256 `4a04812dce749f7973e2431fac484e9fabeba194f5cc7a59b226b71cd8b9eafa` (14237 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- h1-whole-true-tail.json: SHA-256 `7cf212a961fb771aeeab447188664a500035baecbc99de9161fe9b3ccada5d25` (15587 bytes).
- h1-whole-true-tail.npz: SHA-256 `d54f3a0963ed834479631fed38d3a89968c1b8e133aa12817fb90715734239a9` (21007 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
