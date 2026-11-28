# R321-two-moment-two-free-scalars-all-full-rings

**数值记录。** 2026-11-28 17:25:46 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46164243725](https://github.com/Rogerhu12/math-research-public/actions/runs/46164243725), attempt 1；计算源码提交 `b49836a1b133a301ddd67b71d5b08a0a456a83d3`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

R321新两矩母线自己的冻结g上真正自由的逐环高度Z与水平切角β，由全D3中心化角原函数重建三维闭环，目标角速度进入完整E/F及所有交块带状求解；每span不同径行、16/27/49真法角。母场、投影初值、优化场在三网分别报；CubicSpline角积分及Pqq角导是有限求值，准确连续定义的G恒等式不冒作当前有限插值场证书。新专用状态需自身全几何。

本次命令参数见 scripts/2ecf-r262-live-work-orders.json 的 R321-two-moment-two-free-scalars-all-full-rings；实际源码逐文件摘要列于下方。开始 2026-11-28 17:25:11 UTC，结束 2026-11-28 17:25:46 UTC。退出码 0。

```json
{
  "schema": "R317-full-D3-rings-open-height-and-horizontal-angle-with-fixed-angular-speed-v1",
  "entrySHA": "6f84c4d84a940aa34f7236b39e5c5fbbd33164b1ce5c0c1c62c62091e8a8dcd3",
  "twoScalarSHA": "6d18eff6ca9268fe29e2dd6194643d807362729c2792e988b2cde9d579a52195",
  "parentSHA": "a02d19c65ad08eafae0ec350f5053b26d1b0f84bf90f70d3d978c04147d5b593",
  "stateSHA": "9b2a60e7a4ca70f0972e74822ef09d32a4a02d6f57f477394e2fedf7d14279dd",
  "fieldSHA": "e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a",
  "angularStrength": 1.0,
  "freePhysicalScalars": 975,
  "frozenMetricVariables": 0,
  "radialSpans": 40,
  "grid": [
    {
      "actualRadial": 399,
      "sectorNodes": 125,
      "materialTargets": {
        "fullUniform": 264,
        "additionalMaterialTargets": 108,
        "perTransitionInterior": 16,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "original": {
        "peak": 0.002708060630093323,
        "rms": 0.0007260749632149641,
        "curvature": 5.798353138996124
      }
    },
    {
      "actualRadial": 503,
      "sectorNodes": 189,
      "materialTargets": {
        "fullUniform": 387,
        "additionalMaterialTargets": 174,
        "perTransitionInterior": 27,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "original": {
        "peak": 0.0027031168673704586,
        "rms": 0.0007395615056890449,
        "curvature": 5.790467483276214
      }
    },
    {
      "actualRadial": 615,
      "sectorNodes": 324,
      "materialTargets": {
        "fullUniform": 663,
        "additionalMaterialTargets": 306,
        "perTransitionInterior": 49,
        "originalMaterialInverseError": 8.881784197001252e-16
      },
      "original": {
        "peak": 0.0027091992317963337,
        "rms": 0.0007486821494168822,
        "curvature": 5.797618549207374
      }
    }
  ],
  "initial": {
    "peak": 0.009169287772858957,
    "rms": 0.0012233413872153205,
    "curvature": 5.7984983651743365,
    "minimumHorizontalAngularSpeed": 0.11999999946289142,
    "minimumSupport": 0.5933305653181713,
    "minimumArea": 0.11999999946243714,
    "minimumZs": 0.22627487035093571,
    "angularComponent": 0.00020718224463678325,
    "worstMetric": [
      0.5273978277146436,
      1.3089969389957472,
      1.4975587473085354
    ],
    "worstCurvature": [
      0.4534088182539455,
      0.09519977738150888,
      0.02007109557109383
    ]
  },
  "initialSecondary": {
    "peak": 0.009184279016035638,
    "rms": 0.0012357762259410348,
    "curvature": 5.790669301866611,
    "minimumHorizontalAngularSpeed": 0.11999999946289142,
    "minimumSupport": 0.5932766158163394,
    "minimumArea": 0.11999999946243714,
    "minimumZs": 0.22627637605588868,
    "angularComponent": 0.00020713628762258907,
    "worstMetric": [
      0.5247333333333334,
      1.306967486377149,
      1.4943777752127267
    ],
    "worstCurvature": [
      0.4580666666666666,
      0.08929591521831452,
      0.018710551518575466
    ]
  },
  "accepted": {
    "actualCompletedSteps": 5
  },
  "physicalJacobianCheck": [
    2.5738743321439416e-12,
    2.7130341079543176e-12
  ],
  "projectedInitialHoldout": {
    "peak": 0.00917724230453681,
    "rms": 0.0012520766890680142,
    "curvature": 5.797765666596395,
    "minimumHorizontalAngularSpeed": 0.11999999946289142,
    "minimumSupport": 0.5932854373509575,
    "minimumArea": 0.11999999946243714,
    "minimumZs": 0.2262994749546218,
    "angularComponent": 0.00020714426105483685,
    "worstMetric": [
      0.5236445079730752,
      1.3078123263812713,
      1.4957028272704551
    ],
    "worstCurvature": [
      0.4560150567627848,
      0.09476900915806315,
      0.01997104525666018
    ]
  },
  "independent": {
    "peak": 0.003248647193673053,
    "rms": 0.0012457219986687636,
    "curvature": 6.1346036371854105,
    "minimumHorizontalAngularSpeed": 0.11999999946289142,
    "minimumSupport": 0.6165849666550878,
    "minimumArea": 0.11999999946243714,
    "minimumZs": 0.22614130124345033,
    "angularComponent": 0.00020714426105483685,
    "worstMetric": [
      0.4211333333333333,
      0.8718748842541808,
      0.7379947765157484
    ],
    "worstCurvature": [
      0.4665594774084987,
      0.08529210824225683,
      0.017800561864557998
    ]
  },
  "scope": "The continuous curve definition uses its D3-centered angular primitive. At unit angular strength the exact target G is prescribed on the part q<=liftEnd before blending back to the actual boundary speed. Reported E,F, curvature and support are finite quadrature observations from independent material-angle grids."
}
```
 数值观察与连续证明分别登记；不将旧输入的证书转移到新位置。

## 可重算输出的身份

- 2ecf-r262-adjacent-two-open-scalars-full-angular-target.py: SHA-256 `6f84c4d84a940aa34f7236b39e5c5fbbd33164b1ce5c0c1c62c62091e8a8dcd3` (9630 bytes).
- 2ecf-r262-live-work-orders.json: SHA-256 `6117c8cc4eb66114d151249ca0ebdf845cd0be10e81329db7162c7e36c0d7fa5` (75912 bytes).
- 2ecf-r262-adjacent-two-open-scalars-full-angular-target.py: SHA-256 `6f84c4d84a940aa34f7236b39e5c5fbbd33164b1ce5c0c1c62c62091e8a8dcd3` (9630 bytes).
- 2ecf-r262-centred-full-ring-height-and-angle.py: SHA-256 `6d18eff6ca9268fe29e2dd6194643d807362729c2792e988b2cde9d579a52195` (7471 bytes).
- h1-two-open-scalars.json: SHA-256 `5931bd0721e37e54375879908be391fb19e2e837f3aec6f211f8a313ae27e297` (11655 bytes).
- h1-two-open-scalars.npz: SHA-256 `9b2a60e7a4ca70f0972e74822ef09d32a4a02d6f57f477394e2fedf7d14279dd` (9580 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
