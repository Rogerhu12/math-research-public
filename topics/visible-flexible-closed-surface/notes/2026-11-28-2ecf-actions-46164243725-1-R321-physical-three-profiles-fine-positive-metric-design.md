# R321-physical-three-profiles-fine-positive-metric-design

**数值记录。** 2026-11-28 17:57:31 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `0e33dcf75625b3e323583881d853d8752c6fba35`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R321 W040 已实际提升的三剖面 f638dc99 场，与全部细径正度量和真实笛卡尔位置联合设计。逐个有理 Boehm 插结保持初始 g，两径向函数的最终二进系数另作冻结，未见网按最终值重算。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R321-physical-three-profiles-fine-positive-metric-design；实际源码逐文件摘要列于下方。开始 2026-11-28 17:57:06 UTC，结束 2026-11-28 17:57:31 UTC。退出码 0。

```json
{
  "schema": "R321-W040-three-physical-profiles-and-fine-positive-metric-v1",
  "entrySHA256": "060aeabd563d23cfccd9a84d5702943dec408c76eda408d83856db4d3bd34bac",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "parentSHA256": "f638dc99f7edd7a54dbbd3fff3614aa593812088004d642ae50ec1c8a0f1b95f",
  "stateSHA256": "c857ec536a45196154b1d5bfa6670fed39f9851079a25ebc2268a7a163a521a0",
  "chosenMetricSHA256": "a294e03c6543dd925c3bbeaddb230962034e80e25a20d96da81de712386e2e68",
  "physicalCurveSHA": "29a132a266968591d16e192635efda4415e2bb1366ea2a6b3c95ff9c82ad5902",
  "cutSHA": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "angularTargetSHA": "05caa4008bfbf50fb7e2182445c4fced635d533c65510277d5f830ee4a3f32b1",
  "parentFineDesignSHA": "292171ea82b3b39bbb15186f4f0e969015c9d515857224a82f15324e4c17d898",
  "trueGrids": [
    {
      "fullUniform": 481,
      "additionalMaterialTargets": 114,
      "perTransitionInterior": 17,
      "originalMaterialInverseError": 8.881784197001252e-16,
      "maximumProfileSecondDerivative": 8461.576419963763,
      "actualAngles": 101,
      "radialRows": 451
    },
    {
      "fullUniform": 691,
      "additionalMaterialTargets": 186,
      "perTransitionInterior": 29,
      "originalMaterialInverseError": 8.881784197001252e-16,
      "maximumProfileSecondDerivative": 8643.74948050143,
      "actualAngles": 148,
      "radialRows": 551
    },
    {
      "fullUniform": 1111,
      "additionalMaterialTargets": 330,
      "perTransitionInterior": 53,
      "originalMaterialInverseError": 8.881784197001252e-16,
      "maximumProfileSecondDerivative": 8662.531494943856,
      "actualAngles": 242,
      "radialRows": 671
    }
  ],
  "actualPositionVariables": 1560,
  "newMetricVariables": 78,
  "parentMetricCoefficients": 38,
  "exactBoehmInitialContainsOriginalMetric": true,
  "finalMetricRoundingBoundExact": "5248960855268163859109524736904062714902971265580606796737532679302545447171773800907826893/1880490490601111610390675327982759143101175597048550299024763762532765520989843036697224644454457144162385920",
  "positiveMetricControlMinimum": 0.9667449229305917,
  "initial": {
    "peak": 0.0021361195246209397,
    "rms": 0.0008229790003327206,
    "curvature": 6.8649680977623815,
    "worstMetric": [
      0.46819999999999995,
      0.6531377658190838,
      0.4063553693195066
    ],
    "worstCurvature": [
      0.46819999999999995,
      0.11756479784743508,
      0.025450771336456325
    ],
    "minimumSupport": 0.598289624117744,
    "minimumZs": 0.21998722614263047,
    "minimumArea": 0.1199999994624372
  },
  "initialSecondary": {
    "peak": 0.002134850932260882,
    "rms": 0.0008218022154543103,
    "curvature": 6.858016000221236,
    "worstMetric": [
      0.4659613337645401,
      0.650141460873141,
      0.4024607853897465
    ],
    "worstCurvature": [
      0.47254213945567775,
      0.11366109455824143,
      0.02448404763148551
    ],
    "minimumSupport": 0.5982487891860029,
    "minimumZs": 0.21998714135418268,
    "minimumArea": 0.1199999994624372
  },
  "initialIndependent": {
    "peak": 0.0021372664137639407,
    "rms": 0.0008209122298728532,
    "curvature": 6.862906522998239,
    "worstMetric": [
      0.46819999999999995,
      0.6503747167647637,
      0.40276325296482546
    ],
    "worstCurvature": [
      0.46819999999999995,
      0.11876407871356555,
      0.025750282635799635
    ],
    "minimumSupport": 0.5982506385319627,
    "minimumZs": 0.21997288563856124,
    "minimumArea": 0.1199999994624372
  },
  "accepted": {
    "actualCompletedSteps": 6
  },
  "completeDifferentialAgreement": [
    1.000210520568564e-15,
    4.290242700263622e-16
  ],
  "secondsPerStep": [
    0.9186362219998045,
    0.9531341120000434,
    0.8877587530005258,
    0.9048100480003995,
    0.9077663609996307,
    0.9489304610006002
  ],
  "finalFrozenCandidate": {
    "peak": 0.0018323684272073693,
    "rms": 0.0006663470725260557,
    "curvature": 6.657806139522172,
    "worstMetric": [
      0.8163193724124109,
      0.7125844722813932,
      0.48764070517238417
    ],
    "worstCurvature": [
      0.4740773414337279,
      0.11310864639387194,
      0.02434823509419929
    ],
    "minimumSupport": 0.5768028586428668,
    "minimumZs": 0.20106616163741947,
    "minimumArea": 0.1199999994624372,
    "maximumOriginNorm": 1.893065835389483,
    "relativeE_F_GatPeak": [
      0.0017998281770252866,
      -0.00029282138787549504,
      -0.0008026563411192011
    ]
  },
  "scope": "The exact radial Boehm lift represents the parent metric identically. Joint steps are a new metric design. The saved final dyadic functions define the metric for subsequent frozen spatial refinement; the cuff, true tail parent, and central rigid windows keep the same physical source."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r321-physical-profiles-and-fine-positive-metric.py: SHA-256 `060aeabd563d23cfccd9a84d5702943dec408c76eda408d83856db4d3bd34bac` (10975 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `859aee484ba170498a756dc98eeee8b7f901a285d9e551716c6850bbd5b7b917` (94890 bytes).
- 2ecf-r321-physical-profiles-and-fine-positive-metric.py: SHA-256 `060aeabd563d23cfccd9a84d5702943dec408c76eda408d83856db4d3bd34bac` (10975 bytes).
- 2ecf-r262-cut-fine-positive-metric-complete-banded-design.py: SHA-256 `292171ea82b3b39bbb15186f4f0e969015c9d515857224a82f15324e4c17d898` (12592 bytes).
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
- h1-physical-fine-metric.json: SHA-256 `a7d5403efdc2edf3e7e8d7b26907fd828fe30da9e080895e538642634a0c26ed` (11985 bytes).
- h1-physical-fine-metric.npz: SHA-256 `c857ec536a45196154b1d5bfa6670fed39f9851079a25ebc2268a7a163a521a0` (21547 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
