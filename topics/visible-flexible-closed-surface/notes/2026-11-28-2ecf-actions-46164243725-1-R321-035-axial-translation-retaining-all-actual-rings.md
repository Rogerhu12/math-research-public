# R321-035-axial-translation-retaining-all-actual-rings

**数值记录。** 2026-11-28 17:59:52 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `05f8a44842036a32330e35970927530a2ee7b0e6`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

以R324已经实际e3逐系数支付的尾位置窗口内每侧δ=.035，保留所有原环、真实圆领和双平盘，另作完整物理前缀新g设计与固定该g的XYZ更新。真实高度速度的准确积分是.350-.035=.315，不删原尾或借旧新前缀几何。所选唯一位移与完整新状态分别登记。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R321-035-axial-translation-retaining-all-actual-rings；实际源码逐文件摘要列于下方。开始 2026-11-28 17:59:17 UTC，结束 2026-11-28 17:59:52 UTC。退出码 0。

```json
{
  "schema": "actual-R317-type-all-original-rings-with-outward-translated-infinite-tails-and-frozen-positive-metric-v1",
  "sourceSHA": "a24aefdcd21c344a997e60b97b6c04c9d097812d3cc6bf78bfcf3fe669adcacf",
  "physicalSHA": "29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902",
  "stateSHA": "66c203a2ef90cb8cf1b1df163546be968380c4651a8bb57847ecb8c4e72ca94c",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "originalS": 2.021775895105453,
  "originalT": 2.4717758951054534,
  "newS": 2.3717758951054533,
  "newT": 2.8217758951054535,
  "eachHalfTailOutwardTranslation": 0.035,
  "trueAxialIntegral": {
    "exactRawIntegral": "1226680132828852091238158113706177/3894222643901120721397872246915072",
    "exactRequiredIntegral": "11349071060973649/36028797018963968",
    "exactVelocityScale": "1226680132828852927800849985437696/1226680132828852091238158113706177",
    "endTranslation": 0.035
  },
  "designedMetricCoefficients": 62,
  "initialLPRayleighObjective": 0.010927841646171095,
  "initialLPGrid": {
    "fullUniform": 252,
    "additionalMaterialTargets": 138,
    "perTransitionInterior": 21,
    "originalMaterialInverseError": 8.881784197001252e-16
  },
  "frozenPositionVariables": 961,
  "grids": [
    {
      "actualRadialRows": 433,
      "actualAngularRows": 54,
      "angleDefinition": {
        "fullUniform": 228,
        "additionalMaterialTargets": 90,
        "perTransitionInterior": 13,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "minRadialMetric": 0.3885904481703598,
      "minAngularMultiplier": 0.9890428062594402
    },
    {
      "actualRadialRows": 529,
      "actualAngularRows": 84,
      "angleDefinition": {
        "fullUniform": 333,
        "additionalMaterialTargets": 162,
        "perTransitionInterior": 25,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "minRadialMetric": 0.388675927396644,
      "minAngularMultiplier": 0.9890426156415709
    },
    {
      "actualRadialRows": 637,
      "actualAngularRows": 151,
      "angleDefinition": {
        "fullUniform": 603,
        "additionalMaterialTargets": 294,
        "perTransitionInterior": 47,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "minRadialMetric": 0.3885904481703598,
      "minAngularMultiplier": 0.989045105820253
    }
  ],
  "fixedMetricInitial": {
    "peak": 0.01879094508761736,
    "rms": 0.010019353363079716,
    "curvature": 7.089917701486641,
    "worstMetric": [
      1.2555682640266688,
      0.0,
      0.0
    ],
    "worstCurvature": [
      1.6000133757179305,
      1.0471975511965976,
      1.047197551196597
    ],
    "minimumSupport": 0.7247517635975977,
    "minimumZs": 0.0915103835905699,
    "minimumArea": 0.1199999994624372
  },
  "fixedMetricInitialSecondary": {
    "peak": 0.018789046754180694,
    "rms": 0.010063544997984628,
    "curvature": 7.085159858276629,
    "worstMetric": [
      1.2543865042625073,
      0.0,
      0.0
    ],
    "worstCurvature": [
      1.5938087348276564,
      1.0471975511965976,
      1.047197551196597
    ],
    "minimumSupport": 0.7248465165133591,
    "minimumZs": 0.09149466331528977,
    "minimumArea": 0.1199999994624372
  },
  "fixedMetricAccepts": [
    {
      "step": 1,
      "alpha": 0.3535533905932738,
      "damping": 0.002,
      "irlsPower": 0.6,
      "training": {
        "peak": 0.012721912092810159,
        "rms": 0.0068803212355430495,
        "curvature": 6.917052641501208,
        "worstMetric": [
          1.7761886488971073,
          0.3031361332411204,
          0.0926986640724886
        ],
        "worstCurvature": [
          1.6786795786093174,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.7186113506411667,
        "minimumZs": 0.08868107326395505,
        "minimumArea": 0.1199999994624372
      },
      "shifted": {
        "peak": 0.01272692834035667,
        "rms": 0.006889651071718184,
        "curvature": 6.917551306000899,
        "worstMetric": [
          1.7782706728677353,
          0.29246057736121195,
          0.08737577561688799
        ],
        "worstCurvature": [
          1.6778231156366736,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.7185799102968172,
        "minimumZs": 0.08865517851778727,
        "minimumArea": 0.1199999994624372
      }
    },
    {
      "step": 2,
      "alpha": 0.25,
      "damping": 1e-11,
      "irlsPower": 0.6,
      "training": {
        "peak": 0.012371689958277832,
        "rms": 0.005489285672401442,
        "curvature": 7.630833967630609,
        "worstMetric": [
          1.7761886488971073,
          0.3031361332411204,
          0.0926986640724886
        ],
        "worstCurvature": [
          0.11140188360223396,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.68473424179044,
        "minimumZs": 0.08249037690057207,
        "minimumArea": 0.1199999994624372
      },
      "shifted": {
        "peak": 0.01238406594145927,
        "rms": 0.005487400677337095,
        "curvature": 7.6243339251013085,
        "worstMetric": [
          1.7782706728677353,
          0.29246057736121195,
          0.08737577561688799
        ],
        "worstCurvature": [
          0.11310792950909386,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.6847179237872073,
        "minimumZs": 0.0824523534551261,
        "minimumArea": 0.1199999994624372
      }
    },
    {
      "step": 3,
      "alpha": 0.125,
      "damping": 1e-11,
      "irlsPower": 0.6,
      "training": {
        "peak": 0.012076655348653532,
        "rms": 0.004984985066184647,
        "curvature": 8.117315008502722,
        "worstMetric": [
          1.7761886488971073,
          0.3031361332411204,
          0.0926986640724886
        ],
        "worstCurvature": [
          0.11140188360223396,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.6727232661066934,
        "minimumZs": 0.0686155988697642,
        "minimumArea": 0.1199999994624372
      },
      "shifted": {
        "peak": 0.01211941244734599,
        "rms": 0.004979563294568666,
        "curvature": 8.104003514571605,
        "worstMetric": [
          1.7718214766660334,
          0.29246057736121195,
          0.08737577561688799
        ],
        "worstCurvature": [
          0.11310792950909386,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.672786232317019,
        "minimumZs": 0.06860629095290494,
        "minimumArea": 0.1199999994624372
      }
    },
    {
      "step": 4,
      "alpha": 0.1767766952966369,
      "damping": 1e-11,
      "irlsPower": 0.6,
      "training": {
        "peak": 0.011943797606861433,
        "rms": 0.004326068853404843,
        "curvature": 8.66558019070888,
        "worstMetric": [
          1.7761886488971073,
          0.3031361332411204,
          0.0926986640724886
        ],
        "worstCurvature": [
          0.11140188360223396,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.6591619871637147,
        "minimumZs": 0.05636277287496713,
        "minimumArea": 0.1199999994624372
      },
      "shifted": {
        "peak": 0.011984863929861426,
        "rms": 0.004313464145844954,
        "curvature": 8.645655166120314,
        "worstMetric": [
          1.7718214766660334,
          0.29246057736121195,
          0.08737577561688799
        ],
        "worstCurvature": [
          0.1078233482854059,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.6592851984765176,
        "minimumZs": 0.05683926722541588,
        "minimumArea": 0.1199999994624372
      }
    },
    {
      "step": 5,
      "alpha": 0.011048543456039806,
      "damping": 1e-11,
      "irlsPower": 0.6,
      "training": {
        "peak": 0.011934124562746604,
        "rms": 0.004293053848956379,
        "curvature": 8.68938565637054,
        "worstMetric": [
          1.7761886488971073,
          0.3031361332411204,
          0.0926986640724886
        ],
        "worstCurvature": [
          0.11140188360223396,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.6585683340363473,
        "minimumZs": 0.05581659720656226,
        "minimumArea": 0.1199999994624372
      },
      "shifted": {
        "peak": 0.011975786476957925,
        "rms": 0.004280023328878563,
        "curvature": 8.67115578318904,
        "worstMetric": [
          1.7718214766660334,
          0.29246057736121195,
          0.08737577561688799
        ],
        "worstCurvature": [
          0.1078233482854059,
          1.0471975511965976,
          1.047197551196597
        ],
        "minimumSupport": 0.6586937920276523,
        "minimumZs": 0.056298885554217776,
        "minimumArea": 0.1199999994624372
      }
    }
  ],
  "actualMatrixAgreement": [
    8.323583280700031e-16,
    3.56498173005306e-16
  ],
  "originalFixedHoldout": {
    "peak": 0.018766482759450698,
    "rms": 0.01005097515847853,
    "curvature": 7.090450294848006,
    "worstMetric": [
      1.2519238580629166,
      0.0,
      0.0
    ],
    "worstCurvature": [
      1.5983673306854627,
      1.0471975511965976,
      1.047197551196597
    ],
    "minimumSupport": 0.7247779254315792,
    "minimumZs": 0.09149189960004611,
    "minimumArea": 0.1199999994624372
  },
  "independent": {
    "peak": 0.012039445888623832,
    "rms": 0.0042731388244945075,
    "curvature": 8.68938565637054,
    "worstMetric": [
      1.7761886488971073,
      0.29175653167666404,
      0.08703218931031168
    ],
    "worstCurvature": [
      0.11140188360223396,
      1.0471975511965976,
      1.047197551196597
    ],
    "minimumSupport": 0.6585683340363473,
    "minimumZs": 0.05581550533931573,
    "minimumArea": 0.1199999994624372
  },
  "scope": "The prescribed axial translation term equals delta for original s>=H. Beyond the last XYZ support S the whole original tail, actual cuff and capping flat disk move rigidly by that amount. Local tail metric/curvature are unchanged relative to that same input; complete new diameter, mixed distances and nonlocal reach require actual new bounds."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-adjacent-all-rings-outward-translated-tail.py: SHA-256 `a24aefdcd21c344a997e60b97b6c04c9d097812d3cc6bf78bfcf3fe669adcacf` (11892 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `55ad15eaacdaa43682448dbbbbdaba54dde9c9db37b27be7bd052d90dc1306c5` (97522 bytes).
- 2ecf-r262-adjacent-all-rings-outward-translated-tail.py: SHA-256 `a24aefdcd21c344a997e60b97b6c04c9d097812d3cc6bf78bfcf3fe669adcacf` (11892 bytes).
- 2ecf-r262-adjacent-low-ports-two-moment-physical-cut.py: SHA-256 `29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902` (13494 bytes).
- 2ecf-r262-adjacent-low-ports-support-physical-cut.py: SHA-256 `94e64a7ee9ead3e1683663dfef5c8bd0b8473b088a11f17f1effb8523fb467f6` (12244 bytes).
- 2ecf-r262-three-arcs-shortened-prefix-v2.py: SHA-256 `4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8` (13772 bytes).
- 2ecf-r262-three-circular-arcs-material-comparison.py: SHA-256 `a8894dc94dd10b54b1646169dffaae3cf85dbc1b5c370ca5810cedbfa84e7a9e` (6345 bytes).
- 2ecf-r321-two-moment-inlet-profiles-all-span-banded.py: SHA-256 `05caa4008bfbf50fb7e2182445c4fced635d533c65510277d5f830ee4a3f32b1` (14321 bytes).
- 2ecf-r262-cut-physical-cauchy-inlet-profile-refinement.py: SHA-256 `ffa687858a059ab60e14987d55acdd1a7d63c62855f7804f2d2ccc2966cebfd0` (14160 bytes).
- 2ecf-r262-adjacent-cut-true-normal-angle-cauchy-refinement.py: SHA-256 `4a04812dce749f7973e2431fac484e9fabeba194f5cc7a59b226b71cd8b9eafa` (14237 bytes).
- 2ecf-r262-cut-frozen-native-and-true-material-position.py: SHA-256 `d8058312f521405e845d76f95d03c69e8b0065c288991c8dbc54ca43551e287f` (10367 bytes).
- 2ecf-r262-cut-same-metric-banded-direct-newton.py: SHA-256 `dfdea60ec56ea6b685c20c7bf4143ba5c087c859648b0881f77ce71404cd61d2` (9818 bytes).
- 2ecf-r262-small-input-full-xyz-positive-metric-v2.py: SHA-256 `152b08a6e60a2aced9ef3aca61543bbc7050471c68614fe1235d4a9e8fa363dc` (20817 bytes).
- 2ecf-r262-minkowski-physical-continuation.py: SHA-256 `87da8b2607d5cf22f7f71bbc3f63ccc21d4c0a2b10f47235b1300560f979f1b3` (11326 bytes).
- 2ecf-m12-h2-cached-direct-lm-v2.py: SHA-256 `b69d67754d935a4e4342c934f80e5272d520f86164804c710350cf412a805745` (5741 bytes).
- 6a65-m12-global-common-cut-position-recovered.py: SHA-256 `89d3f03e752dce04007166a8e540e3e49f1621ed725cd8e6b43475ea8101776a` (21022 bytes).
- 6a65-m12-entire-half-cartesian-bvp.py: SHA-256 `7214054f65bfbd1055122dddf235074bc812c88cdf5d418b630877bf8b21880b` (18390 bytes).
- 6a65-m12-original-tail-background.py: SHA-256 `cab284d7506523dbe56a2711a654764084ef0a5d253187bafcec965ca06da1dd` (15717 bytes).
- design.json: SHA-256 `417b570cc5be2298d8fe1466387c2df1211cd9ee0f12315fe570aa3774d065ba` (10450 bytes).
- design.npz: SHA-256 `66c203a2ef90cb8cf1b1df163546be968380c4651a8bb57847ecb8c4e72ca94c` (14123 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
