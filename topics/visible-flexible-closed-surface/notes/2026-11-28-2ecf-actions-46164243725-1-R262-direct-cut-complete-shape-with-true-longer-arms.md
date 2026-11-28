# R262-direct-cut-complete-shape-with-true-longer-arms

**数值记录。** 2026-11-28 17:31:41 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `5d4cbf5c5fedbcfc37f059da84d79a65d40dc2ec`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

真实直接Newton末态与新低/高末直长度.98/.46的两厚臂组成全闭空间像；所有原尾与平盘、两真端口都来自同一输入，整D与双向握持是有限观察，连续R315条件另行支付。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-direct-cut-complete-shape-with-true-longer-arms；实际源码逐文件摘要列于下方。开始 2026-11-28 17:31:26 UTC，结束 2026-11-28 17:31:41 UTC。退出码 0。

```json
{
  "stateSHA256": "8e4d090c855f1a5de8f4698ada7cf212c636dc7741480b807c50b33a5ff6cdce",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "definitionSHA256": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "beltSHA256": "7dc3c36f3bad1eaf8e9137f5557df863e3467bc805f03d6c54f4148b9cd68a8d",
  "low": 0.35,
  "sleeve": 0.78,
  "geometry": {
    "positionsInPrefix": 26208,
    "positiveArea": 0.014399999870984911,
    "observedPrefixMetricPeak": 0.009710469351342448,
    "curvatureMax": 8.632690914746375,
    "supportMinimum": 0.36946086662431743,
    "exteriorHeightMinimum": 0.78,
    "exteriorHeightMaximum": 1.772114288708474,
    "supportIndex": [
      6,
      123
    ],
    "curvatureIndex": [
      8,
      48
    ],
    "sourceRowsKept": [
      0.78,
      2.021775895105453
    ],
    "radiusMaximum": 1.0920838539556232,
    "observedPrefixShapeSufficientMargins": {
      "planarRadius": 0.4679161460443768,
      "originRadius": 0.021408009304897835,
      "armMixedSquared": 0.9872709387115126,
      "minimumExternalZForArmNormalBalls": 0.43200000000000005,
      "maximumMixedLocation": [
        93,
        0
      ]
    },
    "originalCapHeight": 1.8205859521647094,
    "trueCuffPositionMismatch": 0.0,
    "trueCutPositionMismatch": 8.673617379884035e-19,
    "sleevePositionMismatch": 0.0,
    "numericOldTailRadii": 62
  },
  "initialDiameter": {
    "value": 3.7775383055193394,
    "points": 112252,
    "hull": 24029,
    "pair": [
      {
        "part": "prefix+",
        "parameter": [
          1.7640621963622756,
          2.6616271092913526
        ],
        "xyz": [
          -0.7979780765534237,
          0.2776393531368694,
          1.692397967305551
        ]
      },
      {
        "part": "prefix-",
        "parameter": [
          1.771247354895497,
          5.45415391248228
        ],
        "xyz": [
          0.8097552024400801,
          -0.21205314430727512,
          -1.6906761689246372
        ]
      }
    ]
  },
  "otherDiameter": {
    "value": 4.249811906785206,
    "points": 112252,
    "hull": 23109,
    "pair": [
      {
        "part": "arm0",
        "parameter": [
          149.0,
          3.141592653589793
        ],
        "xyz": [
          1.736044059117064,
          -1.38712595609516,
          1.3189411513663584e-17
        ]
      },
      {
        "part": "arm1",
        "parameter": [
          146.0,
          0.0
        ],
        "xyz": [
          -0.615921425264488,
          2.152529338327047,
          0.0
        ]
      }
    ]
  },
  "initialToOtherHeld": {
    "value": 1.0273317136049112,
    "source": {
      "part": "arm0",
      "parameter": [
        162.0,
        0.0
      ],
      "xyz": [
        2.056115478316428,
        -0.21046681542705048,
        0.0
      ]
    },
    "nearest": {
      "part": "arm0",
      "parameter": [
        151.0,
        0.0
      ],
      "xyz": [
        1.7099492463836623,
        -1.1777203445743336,
        0.0
      ]
    }
  },
  "otherToInitialHeld": {
    "value": 0.6033688278192735,
    "source": {
      "part": "arm0",
      "parameter": [
        91.0,
        3.141592653589793
      ],
      "xyz": [
        0.4933302871276507,
        -1.5488983795908635,
        1.4362343378027565e-17
      ]
    },
    "nearest": {
      "part": "belt",
      "parameter": [
        0.0,
        4.974188368183839
      ],
      "xyz": [
        0.24278682962797019,
        -1.0000068435948073,
        0.0
      ]
    }
  },
  "sampledHeldRatio": 0.2719579870583662,
  "sampledHalfDiameterDifferenceRatio": 0.06251076270700294,
  "sampledRequiredReach": 0.11332614916558018,
  "scope": "Finite independent shape diagnostics on real parts of the same surface. Reach and continuous diameter, Hausdorff and full-domain metric inequalities require continuous arguments."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-three-arcs-actual-high-caps-complete-observer.py: SHA-256 `e58aa45f369e3b89bca9db10c59ff7c65300bfd539cafd0595ad5573f234e7fe` (11912 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-three-arcs-actual-high-caps-complete-observer.py: SHA-256 `e58aa45f369e3b89bca9db10c59ff7c65300bfd539cafd0595ad5573f234e7fe` (11912 bytes).
- 2ecf-threefold-035-longer-end-arm-belt.py: SHA-256 `7dc3c36f3bad1eaf8e9137f5557df863e3467bc805f03d6c54f4148b9cd68a8d` (5437 bytes).
- direct-whole-long-arms.json: SHA-256 `45020e0419c04be7af9b129c5c22e7ddcac8cc0a572e9fb1191f6d3f81877606` (4814 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
