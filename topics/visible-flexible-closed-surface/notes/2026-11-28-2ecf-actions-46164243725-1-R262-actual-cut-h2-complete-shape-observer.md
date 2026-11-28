# R262-actual-cut-h2-complete-shape-observer

**数值记录。** 2026-11-28 17:31:22 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `2d20160ea7abef59f6ed47f64b3d8db80f9ab36f`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

本次真实h2整闭空间像观察：完整原前缀/原尾/平盘和真D3两厚臂，检查实际接缝及R312的三个充分形状量；这些有限观察不冒连续厚度或Hausdorff下界。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R262-actual-cut-h2-complete-shape-observer；实际源码逐文件摘要列于下方。开始 2026-11-28 17:31:07 UTC，结束 2026-11-28 17:31:22 UTC。退出码 0。

```json
{
  "stateSHA256": "9a3958fa2f008855599a34e01cb96090dbffeaf741502c34e714152ad140332e",
  "fieldSHA256": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "definitionSHA256": "4e57eec6a1e3a9617dac6ef8d57df1564c13ef55b23c35742e9e7075defde1e8",
  "low": 0.35,
  "sleeve": 0.78,
  "geometry": {
    "positionsInPrefix": 26208,
    "positiveArea": 0.014399999870984911,
    "observedPrefixMetricPeak": 0.010108820751057061,
    "curvatureMax": 7.4995277486129,
    "supportMinimum": 0.3729438915008738,
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
    "radiusMaximum": 1.0920913241304602,
    "observedPrefixShapeSufficientMargins": {
      "planarRadius": 0.41790867586953984,
      "originRadius": 0.00040268056295200694,
      "armMixedSquared": 1.2716914018052687,
      "minimumExternalZForArmNormalBalls": 0.43200000000000005,
      "maximumMixedLocation": [
        94,
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
    "value": 3.7775539177405926,
    "points": 112252,
    "hull": 24208,
    "pair": [
      {
        "part": "prefix+",
        "parameter": [
          1.7640621963622756,
          0.5672320068981571
        ],
        "xyz": [
          0.6394334457575346,
          0.5522504294898956,
          1.6924057995491038
        ]
      },
      {
        "part": "prefix-",
        "parameter": [
          1.771247354895497,
          3.3597588100890845
        ],
        "xyz": [
          -0.5885217751584253,
          -0.5952442952243249,
          -1.6906838288254635
        ]
      }
    ]
  },
  "otherDiameter": {
    "value": 4.170640579941827,
    "points": 112252,
    "hull": 23358,
    "pair": [
      {
        "part": "arm0",
        "parameter": [
          150.0,
          3.141592653589793
        ],
        "xyz": [
          1.6615681015304808,
          -1.3976245632585085,
          1.2921320840215478e-17
        ]
      },
      {
        "part": "arm1",
        "parameter": [
          145.0,
          0.0
        ],
        "xyz": [
          -0.7381822668230011,
          2.0134516623108967,
          0.0
        ]
      }
    ]
  },
  "initialToOtherHeld": {
    "value": 0.9994116238021413,
    "source": {
      "part": "arm0",
      "parameter": [
        163.0,
        0.0
      ],
      "xyz": [
        1.9979049733637377,
        -0.26137785252409973,
        0.0
      ]
    },
    "nearest": {
      "part": "arm0",
      "parameter": [
        152.0,
        0.0
      ],
      "xyz": [
        1.6360584815245387,
        -1.1929843736125352,
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
  "sampledHeldRatio": 0.26456581310688565,
  "sampledHalfDiameterDifferenceRatio": 0.052029258980947214,
  "sampledRequiredReach": 0.11332661753221777,
  "scope": "Finite independent shape diagnostics on real parts of the same surface. Reach and continuous diameter, Hausdorff and full-domain metric inequalities require continuous arguments."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-three-arcs-actual-high-caps-complete-observer.py: SHA-256 `e58aa45f369e3b89bca9db10c59ff7c65300bfd539cafd0595ad5573f234e7fe` (11912 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-three-arcs-actual-high-caps-complete-observer.py: SHA-256 `e58aa45f369e3b89bca9db10c59ff7c65300bfd539cafd0595ad5573f234e7fe` (11912 bytes).
- h2-whole-shape.json: SHA-256 `d75185cfc0130b16b25abd23c2c1aa2d3eeafe8e086c587b30cda74401c482a8` (4812 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
