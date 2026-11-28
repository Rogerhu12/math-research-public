# R321-selected-physical-profile-frozen-g-full-half-through-tail

**数值记录。** 2026-11-28 17:59:12 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `057297d023f4190e94f66dd85be49007faba24a0`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

在前置W040三剖面细g设计之后，若其真实未见峰得到改善，则固定该新g并将一个XYZ场跨公共切环延展至真实无限尾及平领。设计未生成或未改善时取原 f638dc99 三剖面父态的已冻结g。两组身份、完整原尾实际格、两端零迹和独立峰分别登记。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R321-selected-physical-profile-frozen-g-full-half-through-tail；实际源码逐文件摘要列于下方。开始 2026-11-28 17:57:37 UTC，结束 2026-11-28 17:59:12 UTC。退出码 0。

```json
{
  "schema": "actual-new-strong-half-same-metric-full-XYZ-across-r06-to-the-true-cuff-v1",
  "sourceSHA": "86833bbafd7715c924916f48f3c8b3325cb8a4008d7b7a95398b9e5546621841",
  "parentSHA": "c857ec536a45196154b1d5bfa6670fed39f9851079a25ebc2268a7a163a521a0",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "stateSHA": "49c159980375fc0bf8761678405f7d49e9a6005f6ff1077e63e6d01fe2d50197",
  "exactTailQueryReportSHA": "8888e19e0ed7a52b5cf389b5c218bfa5b3158d7740f1c6917b2e2380e65cbf7b",
  "exactTailQueryCacheSHA": "9ccf0d1eec413cb6e60533207c360cefc9f73143519f763a19b012219ca40d0a",
  "radialUnitSpans": 52,
  "positionVariables": 2193,
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
    0.0015818904279674135,
    0.0006893304523375166,
    0.10686284227154141
  ],
  "actualTwoEndpointBasisZeroJets": [
    0.0,
    0.0,
    0.0
  ],
  "initial": {
    "peak": 0.0018330593723224727,
    "rms": 0.00020271445579639542,
    "curvature": 6.590220145282828,
    "worstMetric": [
      0.8129635671286278,
      0.7068583470577035,
      0.4794876365605249
    ],
    "worstCurvature": [
      0.4726905973284028,
      0.10471975511965977,
      0.022315223304399126
    ],
    "minimumSupport": 0.5768046587976523,
    "minimumZs": -2.5776236057809258e-09,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.0018330593723224727,
    "tailPeak": 5.295414201997818e-10,
    "prefixCurvature": 6.590220145282828,
    "tailCurvature": 6.424492816892881,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "initialSecondary": {
    "peak": 0.0018340100357306115,
    "rms": 0.0002842508208184297,
    "curvature": 6.657469030817214,
    "worstMetric": [
      0.8138453350581604,
      0.7070821072182156,
      0.4798049794328505
    ],
    "worstCurvature": [
      0.47254213945567775,
      0.11635528346628865,
      0.02514991193199822
    ],
    "minimumSupport": 0.5768017673669068,
    "minimumZs": -2.576085426802553e-09,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.0018340100357306115,
    "tailPeak": 5.435508573314617e-10,
    "prefixCurvature": 6.657469030817214,
    "tailCurvature": 6.428917515304164,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "accepted": {
    "actualCompletedSteps": 5
  },
  "matrixAndRhsAgreement": [
    2.3097652374971235e-15,
    3.9108686356072893e-16
  ],
  "initialIndependent": {
    "peak": 0.0018325848490009977,
    "rms": 0.0003024967876673076,
    "curvature": 6.651703945661495,
    "worstMetric": [
      0.8156544730659023,
      0.7082495515339308,
      0.48146234151044615
    ],
    "worstCurvature": [
      0.4743755463879139,
      0.11129635809818912,
      0.023904412111025855
    ],
    "minimumSupport": 0.5768233203969866,
    "minimumZs": -2.5777622626167116e-09,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.0018325848490009977,
    "tailPeak": 5.429267074733872e-10,
    "prefixCurvature": 6.651703945661495,
    "tailCurvature": 6.394066119213662,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "independent": {
    "peak": 0.0016750072095737616,
    "rms": 0.00019454165224642165,
    "curvature": 8.466311178484975,
    "worstMetric": [
      0.4743755463879139,
      0.6273067456443387,
      0.3734427163179006
    ],
    "worstCurvature": [
      0.48964290616056644,
      0.14164991030678617,
      0.03170991454341853
    ],
    "minimumSupport": 0.564408678813174,
    "minimumZs": 0.0,
    "minimumArea": 0.029999999865732006,
    "prefixPeak": 0.0016750072095737616,
    "tailPeak": 0.0002406706188885907,
    "prefixCurvature": 8.466311178484975,
    "tailCurvature": 6.580475200066989,
    "worstMetricTailRadius": null,
    "worstCurvatureTailRadius": null
  },
  "scope": "The common cut is interior to a single additional XYZ field. Original tail queries are evaluated at their exact saved binary radii and derived from the exact physical source; physical derivatives use the signed radial-arclength factor and its derivative. The true cuff and sleeve keep their prescribed two-jets. Any nonzero new addition on the tail requires its own continuous metric and thickness bounds.",
  "parentSelection": {
    "reason": "successful fine positive design reduced the independent metric peak",
    "fallbackSHA": "f638dc99f7edd7a54dbbd3fff3614aa593812088004d642ae50ec1c8a0f1b95f",
    "chosenSHA": "c857ec536a45196154b1d5bfa6670fed39f9851079a25ebc2268a7a163a521a0",
    "newFrozenMetricSHA": "a294e03c6543dd925c3bbeaddb230962034e80e25a20d96da81de712386e2e68",
    "designReportSHA": "a7d5403efdc2edf3e7e8d7b26907fd828fe30da9e080895e538642634a0c26ed"
  }
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r321-selected-profile-design-whole-tail.py: SHA-256 `2b2d34d08e2123cfad7e95bc5a97c7b712c4c32e3c8090158950df5ea43bbce1` (2043 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `55ad15eaacdaa43682448dbbbbdaba54dde9c9db37b27be7bd052d90dc1306c5` (97522 bytes).
- 2ecf-r321-selected-profile-design-whole-tail.py: SHA-256 `2b2d34d08e2123cfad7e95bc5a97c7b712c4c32e3c8090158950df5ea43bbce1` (2043 bytes).
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
- profile-best-metric-whole-tail.json: SHA-256 `8bc4ee1db9788904e876b45397463f52a6372dd48322a105165e000649c13f10` (15969 bytes).
- profile-best-metric-whole-tail.npz: SHA-256 `49c159980375fc0bf8761678405f7d49e9a6005f6ff1077e63e6d01fe2d50197` (24022 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
