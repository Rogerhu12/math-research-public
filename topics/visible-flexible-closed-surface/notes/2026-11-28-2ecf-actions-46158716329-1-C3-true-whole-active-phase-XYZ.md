# C3-true-whole-active-phase-XYZ

**数值记录。** 2026-11-28 15:15:02 UTC；会话 Astra-visible-flex-2ecfcd69-20261128。

公开 Actions run [46158716329](https://github.com/Rogerhu12/math-research-public/actions/runs/46158716329), attempt 1；计算源码提交 `6990e09ba612942b90a99536b684990959f56165`。命令与参数由本提交中的 `2ecf-public-actions-research-runner.py` 明列。

一次样条跨过整个真 .06 ramp 出口，使全部真实中间端迹参与空间求解；中央及帽端的两 jets 保持。固定同一初相真实诱导 g，所有实际相位与插值相位均单独观察。

```json
{
  "parameters": {
    "seed_state": null,
    "deltas": [
      0.0009765625,
      0.00390625,
      0.015625,
      0.0625,
      0.125,
      0.25,
      0.375,
      0.5
    ],
    "ramp_spans": 4,
    "phase_interior": 1,
    "c": 0.78,
    "length": 0.58,
    "gate": 0.1,
    "cap_radius": 0.94,
    "cap_height": 0.32,
    "spans": 8,
    "modes": 6,
    "angles": 64,
    "radial": 25,
    "independent": 192,
    "test_radial": 63,
    "steps": 18
  },
  "results": [
    {
      "delta": 0.0009765625,
      "eta": 0.4990234375,
      "variables": 435,
      "zeroCorrectionIndependent": {
        "peak": 0.0034502737665965213,
        "rms": 0.0008017517455276155,
        "curvature": 5.489931686394778,
        "minAreaSquared": 0.8590233480506331,
        "minimumPolarAngularDeterminant": 0.6301235631193541,
        "minimumHeightRateAtFixedPolarAngle": 0.999549898704409,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          5.595961914206819
        ]
      },
      "warmTraining": {
        "peak": 0.0034501208403218647,
        "rms": 0.0012075414339737423,
        "curvature": 5.440706808840641,
        "minAreaSquared": 0.8591689325701328,
        "minimumPolarAngularDeterminant": 0.6301235631193541,
        "minimumHeightRateAtFixedPolarAngle": 0.9995498987044102,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.0952000000000002,
          2.454369260617026
        ]
      },
      "finalTraining": {
        "peak": 0.0005043487084056904,
        "rms": 0.0001938847255788627,
        "curvature": 5.443127584395214,
        "minAreaSquared": 0.8588882810448941,
        "minimumPolarAngularDeterminant": 0.6301235631193541,
        "minimumHeightRateAtFixedPolarAngle": 0.9977838464522725,
        "capHeightAnalyticSupportLower": 1.4199993786176415,
        "minimumActiveHeight": 0.78,
        "point": [
          0.9096000000000001,
          0.7853981633974483
        ]
      },
      "finalIndependent": {
        "peak": 0.0005094424785942364,
        "rms": 0.0001558113561837254,
        "curvature": 5.492486646355761,
        "minAreaSquared": 0.8587510304973891,
        "minimumPolarAngularDeterminant": 0.6301235631193541,
        "minimumHeightRateAtFixedPolarAngle": 0.9977872355609301,
        "capHeightAnalyticSupportLower": 1.4199993786176415,
        "minimumActiveHeight": 0.78,
        "point": [
          0.9101431746031747,
          0.818123086872342
        ]
      },
      "unmodifiedNativeRampMismatchForComparison": 3.1063960641877513e-12,
      "completeObservedPeak": 0.0005094424785942364,
      "stateSHA256": "468aece98feb73d0457c306f7fb8d505e66d37b73af9bb451577cd1e3193524e",
      "acceptedSteps": 4
    },
    {
      "delta": 0.00390625,
      "eta": 0.49609375,
      "variables": 435,
      "zeroCorrectionIndependent": {
        "peak": 0.013872096336589791,
        "rms": 0.0032070742699345364,
        "curvature": 5.489868691939039,
        "minAreaSquared": 0.858988033320664,
        "minimumPolarAngularDeterminant": 0.6301248133509875,
        "minimumHeightRateAtFixedPolarAngle": 0.9995498987044108,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          5.595961914206819
        ]
      },
      "warmTraining": {
        "peak": 0.0020221014811865144,
        "rms": 0.0007761785198226518,
        "curvature": 5.492408656716107,
        "minAreaSquared": 0.8580671782697868,
        "minimumPolarAngularDeterminant": 0.6301248133509875,
        "minimumHeightRateAtFixedPolarAngle": 0.9911357617295558,
        "capHeightAnalyticSupportLower": 1.419997514470566,
        "minimumActiveHeight": 0.78,
        "point": [
          0.8944504000000001,
          2.356194490192345
        ]
      },
      "finalTraining": {
        "peak": 0.0020188303135015655,
        "rms": 0.0007755399913715964,
        "curvature": 5.500898913281974,
        "minAreaSquared": 0.858048983783148,
        "minimumPolarAngularDeterminant": 0.6301248133509875,
        "minimumHeightRateAtFixedPolarAngle": 0.9911341071224989,
        "capHeightAnalyticSupportLower": 1.4199957220514545,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3504,
          3.043417883165112
        ]
      },
      "finalIndependent": {
        "peak": 0.0020358521734440806,
        "rms": 0.0006221880381801789,
        "curvature": 5.533219756179767,
        "minAreaSquared": 0.8579312722177175,
        "minimumPolarAngularDeterminant": 0.6301248133509875,
        "minimumHeightRateAtFixedPolarAngle": 0.9911467592099725,
        "capHeightAnalyticSupportLower": 1.4199957220514545,
        "minimumActiveHeight": 0.78,
        "point": [
          0.9136507936507937,
          0.818123086872342
        ]
      },
      "unmodifiedNativeRampMismatchForComparison": 3.290524044674084e-12,
      "completeObservedPeak": 0.0020358521734440806,
      "stateSHA256": "82081aeea6cf679022424e4561574f2b6ffb49525da9893ff22db7ca327af83c",
      "acceptedSteps": 1
    },
    {
      "delta": 0.015625,
      "eta": 0.484375,
      "variables": 435,
      "zeroCorrectionIndependent": {
        "peak": 0.056635512580562,
        "rms": 0.012832602671979195,
        "curvature": 5.488860705263957,
        "minAreaSquared": 0.8588981107040214,
        "minimumPolarAngularDeterminant": 0.6301448170409063,
        "minimumHeightRateAtFixedPolarAngle": 0.9995498987044104,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          5.595961914206819
        ]
      },
      "warmTraining": {
        "peak": 0.009595042235699259,
        "rms": 0.0031599374991991822,
        "curvature": 6.7689947859360355,
        "minAreaSquared": 0.8553808865380439,
        "minimumPolarAngularDeterminant": 0.6301448170409063,
        "minimumHeightRateAtFixedPolarAngle": 0.9645445759202061,
        "capHeightAnalyticSupportLower": 1.4199828882058183,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3504,
          5.890486225480862
        ]
      },
      "finalTraining": {
        "peak": 0.007449381772949898,
        "rms": 0.0032058534800214916,
        "curvature": 7.596742451082179,
        "minAreaSquared": 0.8539862225284368,
        "minimumPolarAngularDeterminant": 0.6301448170409063,
        "minimumHeightRateAtFixedPolarAngle": 0.9613153917726417,
        "capHeightAnalyticSupportLower": 1.4198202083430114,
        "minimumActiveHeight": 0.78,
        "point": [
          1.2888504,
          0.5890486225480862
        ]
      },
      "finalIndependent": {
        "peak": 0.0074499053964466105,
        "rms": 0.0028848478396595145,
        "curvature": 7.8142826596026564,
        "minAreaSquared": 0.8538728714563629,
        "minimumPolarAngularDeterminant": 0.6301448170409063,
        "minimumHeightRateAtFixedPolarAngle": 0.9612104403203311,
        "capHeightAnalyticSupportLower": 1.4198202083430114,
        "minimumActiveHeight": 0.78,
        "point": [
          1.287603492063492,
          0.5890486225480862
        ]
      },
      "unmodifiedNativeRampMismatchForComparison": 3.670228210278945e-12,
      "completeObservedPeak": 0.0074499053964466105,
      "stateSHA256": "3d9eb0319ae272e280c9d1e5ab3cb7c69da3d89285c2d1743933749a044842df",
      "acceptedSteps": 6
    },
    {
      "delta": 0.0625,
      "eta": 0.4375,
      "variables": 435,
      "zeroCorrectionIndependent": {
        "peak": 0.24595720868450155,
        "rms": 0.051605124564893384,
        "curvature": 5.489846365379706,
        "minAreaSquared": 0.8590465327491141,
        "minimumPolarAngularDeterminant": 0.6301242402686429,
        "minimumHeightRateAtFixedPolarAngle": 0.9995498987044108,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.0942701587301589,
          2.421644337142132
        ]
      },
      "warmTraining": {
        "peak": 0.06452943571370379,
        "rms": 0.014927374400612443,
        "curvature": 26.924777855297926,
        "minAreaSquared": 0.8470237347102267,
        "minimumPolarAngularDeterminant": 0.6302347091956774,
        "minimumHeightRateAtFixedPolarAngle": 0.8448505382732219,
        "capHeightAnalyticSupportLower": 1.4192808333720457,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3504,
          2.552544031041707
        ]
      },
      "finalTraining": {
        "peak": 0.03142844830643295,
        "rms": 0.01270643308030981,
        "curvature": 23.140068466842802,
        "minAreaSquared": 0.8407533804412797,
        "minimumPolarAngularDeterminant": 0.6285381331835506,
        "minimumHeightRateAtFixedPolarAngle": 0.8692458575138082,
        "capHeightAnalyticSupportLower": 1.4173763300259543,
        "minimumActiveHeight": 0.78,
        "point": [
          1.2888504,
          3.6324665057131984
        ]
      },
      "finalIndependent": {
        "peak": 0.03146145754369735,
        "rms": 0.011356652681507233,
        "curvature": 24.461290185134274,
        "minAreaSquared": 0.8407735594560983,
        "minimumPolarAngularDeterminant": 0.6284201353637793,
        "minimumHeightRateAtFixedPolarAngle": 0.8678942718515951,
        "capHeightAnalyticSupportLower": 1.4173763300259543,
        "minimumActiveHeight": 0.78,
        "point": [
          1.291111111111111,
          3.665191429188092
        ]
      },
      "unmodifiedNativeRampMismatchForComparison": 4.011910064507575e-12,
      "completeObservedPeak": 0.03146145754369735,
      "stateSHA256": "8f1e9e57d6b64362354acfafec0777daee8214da2b05803909ff385191957b64",
      "acceptedSteps": 6
    },
    {
      "delta": 0.125,
      "eta": 0.375,
      "variables": 435,
      "zeroCorrectionIndependent": {
        "peak": 0.548632196321462,
        "rms": 0.10494755736450806,
        "curvature": 5.489577796784976,
        "minAreaSquared": 0.8589576739700704,
        "minimumPolarAngularDeterminant": 0.6301265217625399,
        "minimumHeightRateAtFixedPolarAngle": 0.9995498987044111,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          5.563236990731926
        ]
      },
      "warmTraining": {
        "peak": 0.14812294431562267,
        "rms": 0.03154512763962063,
        "curvature": 47.43311896962229,
        "minAreaSquared": 0.8299088753838968,
        "minimumPolarAngularDeterminant": 0.6263679498417277,
        "minimumHeightRateAtFixedPolarAngle": 0.7386682383782666,
        "capHeightAnalyticSupportLower": 1.414752660051909,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3504,
          5.6941366846315
        ]
      },
      "finalTraining": {
        "peak": 0.06819188737699802,
        "rms": 0.02474413375954899,
        "curvature": 34.04139783110411,
        "minAreaSquared": 0.811531836496503,
        "minimumPolarAngularDeterminant": 0.6262981148725776,
        "minimumHeightRateAtFixedPolarAngle": 0.7652840101200349,
        "capHeightAnalyticSupportLower": 1.4096462228873812,
        "minimumActiveHeight": 0.78,
        "point": [
          0.9176504000000001,
          4.908738521234052
        ]
      },
      "finalIndependent": {
        "peak": 0.06896430315336108,
        "rms": 0.019613333566900846,
        "curvature": 36.68595032897242,
        "minAreaSquared": 0.8115358842683202,
        "minimumPolarAngularDeterminant": 0.6263043034496216,
        "minimumHeightRateAtFixedPolarAngle": 0.7614286117658823,
        "capHeightAnalyticSupportLower": 1.4096462228873812,
        "minimumActiveHeight": 0.78,
        "point": [
          0.9136507936507937,
          4.941463444708945
        ]
      },
      "unmodifiedNativeRampMismatchForComparison": 3.5824476416231123e-12,
      "completeObservedPeak": 0.06896430315336108,
      "stateSHA256": "31c49fb5e8083c6dbd3b2df08c2373f7ea92f77a5318e2a303d2978b221c31d9",
      "acceptedSteps": 2
    },
    {
      "delta": 0.25,
      "eta": 0.25,
      "variables": 435,
      "zeroCorrectionIndependent": {
        "peak": 1.3525291535781592,
        "rms": 0.22321154066544135,
        "curvature": 5.488882015962842,
        "minAreaSquared": 0.8588717053033567,
        "minimumPolarAngularDeterminant": 0.6301356477343794,
        "minimumHeightRateAtFixedPolarAngle": 0.9995498987044111,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          2.3889194136672383
        ]
      },
      "warmTraining": {
        "peak": 0.5994458063908807,
        "rms": 0.08480729022519336,
        "curvature": 69.11589843607499,
        "minAreaSquared": 0.8120199712085191,
        "minimumPolarAngularDeterminant": 0.6238129720776536,
        "minimumHeightRateAtFixedPolarAngle": 0.5273565150945159,
        "capHeightAnalyticSupportLower": 1.3992924457747784,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3504,
          3.5342917352885173
        ]
      },
      "finalTraining": {
        "peak": 0.13785817924532606,
        "rms": 0.04704491879542188,
        "curvature": 78.59403027614579,
        "minAreaSquared": 0.7652870675739554,
        "minimumPolarAngularDeterminant": 0.6238093403596979,
        "minimumHeightRateAtFixedPolarAngle": 0.11007922094838057,
        "capHeightAnalyticSupportLower": 1.3827850655766833,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3968,
          3.5342917352885173
        ]
      },
      "finalIndependent": {
        "peak": 0.14162549780506584,
        "rms": 0.044265740214873985,
        "curvature": 78.82469710751931,
        "minAreaSquared": 0.7640714930931637,
        "minimumPolarAngularDeterminant": 0.6237289660048697,
        "minimumHeightRateAtFixedPolarAngle": 0.11237001833438304,
        "capHeightAnalyticSupportLower": 1.3827850655766833,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3923809523809523,
          3.5670166587634107
        ]
      },
      "unmodifiedNativeRampMismatchForComparison": 3.7354763520292615e-12,
      "completeObservedPeak": 0.14162549780506584,
      "stateSHA256": "91b1c61a04af38dd5c661e69220b1a9626ac0cc49a538e33eafb508dbbf5f892",
      "acceptedSteps": 6
    },
    {
      "delta": 0.375,
      "eta": 0.125,
      "variables": 435,
      "zeroCorrectionIndependent": {
        "peak": 2.46071374390145,
        "rms": 0.36550437544864156,
        "curvature": 5.489752574773891,
        "minAreaSquared": 0.8588583132802837,
        "minimumPolarAngularDeterminant": 0.6301432120136514,
        "minimumHeightRateAtFixedPolarAngle": 0.99954989870441,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          2.3889194136672383
        ]
      },
      "warmTraining": {
        "peak": 1.553878443256726,
        "rms": 0.1407010086315639,
        "curvature": 117.8629610708318,
        "minAreaSquared": 0.7680175240784828,
        "minimumPolarAngularDeterminant": 0.6139329114304823,
        "minimumHeightRateAtFixedPolarAngle": -0.3348102421064072,
        "capHeightAnalyticSupportLower": 1.3641775983656332,
        "minimumActiveHeight": 0.78,
        "point": [
          0.8480504000000001,
          5.105088062083414
        ]
      },
      "finalTraining": {
        "peak": 0.21600983407067856,
        "rms": 0.0706714965259463,
        "curvature": 106.95032569004385,
        "minAreaSquared": 0.6969423283738349,
        "minimumPolarAngularDeterminant": 0.6297124791935246,
        "minimumHeightRateAtFixedPolarAngle": -0.4195637789490849,
        "capHeightAnalyticSupportLower": 1.36085445999446,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3968,
          3.5342917352885173
        ]
      },
      "finalIndependent": {
        "peak": 0.22058290851767853,
        "rms": 0.0674772813503187,
        "curvature": 107.33722598619099,
        "minAreaSquared": 0.6955117488331645,
        "minimumPolarAngularDeterminant": 0.6296190372277705,
        "minimumHeightRateAtFixedPolarAngle": -0.41631295901324766,
        "capHeightAnalyticSupportLower": 1.36085445999446,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3923809523809523,
          3.5015668118136234
        ]
      },
      "unmodifiedNativeRampMismatchForComparison": 4.722256977504783e-12,
      "completeObservedPeak": 0.22058290851767853,
      "stateSHA256": "b49d0921ef3f38dea06156c953ab196aefc06a0d9a54f3a57182d351e7f26ef7",
      "acceptedSteps": 6
    },
    {
      "delta": 0.5,
      "eta": 0.0,
      "variables": 435,
      "zeroCorrectionIndependent": {
        "peak": 3.9135929187633964,
        "rms": 0.5390145019867568,
        "curvature": 5.489906900130778,
        "minAreaSquared": 0.8589104674425001,
        "minimumPolarAngularDeterminant": 0.6301307588095139,
        "minimumHeightRateAtFixedPolarAngle": 0.9995498987044115,
        "capHeightAnalyticSupportLower": 1.42,
        "minimumActiveHeight": 0.78,
        "point": [
          1.097777777777778,
          5.497787143782138
        ]
      },
      "warmTraining": {
        "peak": 1.6259272690573914,
        "rms": 0.16330269932799676,
        "curvature": 143.43411641453554,
        "minAreaSquared": 0.6931008701399592,
        "minimumPolarAngularDeterminant": 0.6271741054567511,
        "minimumHeightRateAtFixedPolarAngle": -0.8903532530477487,
        "capHeightAnalyticSupportLower": 1.3411392799927735,
        "minimumActiveHeight": 0.78,
        "point": [
          0.8480504000000001,
          5.006913291658733
        ]
      },
      "finalTraining": {
        "peak": 0.2375863856160358,
        "rms": 0.09574322299495996,
        "curvature": 141.455728771562,
        "minAreaSquared": 0.6779830175957005,
        "minimumPolarAngularDeterminant": 0.6301307588095301,
        "minimumHeightRateAtFixedPolarAngle": -0.6424830577222299,
        "capHeightAnalyticSupportLower": 1.3414543656175688,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3968,
          3.436116964863836
        ]
      },
      "finalIndependent": {
        "peak": 0.24083466274531842,
        "rms": 0.090778868833661,
        "curvature": 141.8705603819114,
        "minAreaSquared": 0.6779183136522622,
        "minimumPolarAngularDeterminant": 0.6301302950334671,
        "minimumHeightRateAtFixedPolarAngle": -0.6570103912561333,
        "capHeightAnalyticSupportLower": 1.3414543656175688,
        "minimumActiveHeight": 0.78,
        "point": [
          1.3923809523809523,
          3.370667117914049
        ]
      },
      "unmodifiedNativeRampMismatchForComparison": 3.3173670455794478e-12,
      "completeObservedPeak": 0.24083466274531842,
      "stateSHA256": "b7ca60739ad2997b2ce4792f570926359c35510699292958995eee9295411f6d",
      "acceptedSteps": 13
    }
  ],
  "definedFamily": {
    "phaseSpan": [
      0.0,
      0.5
    ],
    "coefficientInterpolation": "affine in actual physical coefficients and cap displacement, shortest SO3 arc between proper cap rotations",
    "independentInteriorPhases": [
      {
        "delta": 0.00048828125,
        "interval": [
          0.0,
          0.0009765625
        ],
        "completeMaterial": {
          "peak": 0.00025460575967531124,
          "rms": 7.792718674464793e-05,
          "curvature": 5.49038477857029,
          "minAreaSquared": 0.8588939129338494,
          "minimumPolarAngularDeterminant": 0.6301235006077692,
          "minimumHeightRateAtFixedPolarAngle": 0.9988921901903636,
          "capHeightAnalyticSupportLower": 1.4199996893088207,
          "minimumActiveHeight": 0.78,
          "point": [
            0.9087990476190477,
            0.818123086872342
          ]
        }
      },
      {
        "delta": 0.00244140625,
        "interval": [
          0.0009765625,
          0.00390625
        ],
        "completeMaterial": {
          "peak": 0.0012720347115467963,
          "rms": 0.0003889920751473517,
          "curvature": 5.508429724000268,
          "minAreaSquared": 0.8583344171682152,
          "minimumPolarAngularDeterminant": 0.6301240007004394,
          "minimumHeightRateAtFixedPolarAngle": 0.9944600176471863,
          "capHeightAnalyticSupportLower": 1.4199975503345479,
          "minimumActiveHeight": 0.78,
          "point": [
            0.9136507936507937,
            0.818123086872342
          ]
        }
      },
      {
        "delta": 0.009765625,
        "interval": [
          0.00390625,
          0.015625
        ],
        "completeMaterial": {
          "peak": 0.004709034682694155,
          "rms": 0.001747197810061853,
          "curvature": 5.83789497000253,
          "minAreaSquared": 0.8557266638791473,
          "minimumPolarAngularDeterminant": 0.6301318146459312,
          "minimumHeightRateAtFixedPolarAngle": 0.9763304088588219,
          "capHeightAnalyticSupportLower": 1.4199079651972355,
          "minimumActiveHeight": 0.78,
          "point": [
            1.3555555555555556,
            0.09817477042468103
          ]
        }
      },
      {
        "delta": 0.0390625,
        "interval": [
          0.015625,
          0.0625
        ],
        "completeMaterial": {
          "peak": 0.020329866991661748,
          "rms": 0.007227539458198375,
          "curvature": 14.816736681885438,
          "minAreaSquared": 0.8452645205847327,
          "minimumPolarAngularDeterminant": 0.6299573988586569,
          "minimumHeightRateAtFixedPolarAngle": 0.9169026375842001,
          "capHeightAnalyticSupportLower": 1.4185982691844916,
          "minimumActiveHeight": 0.78,
          "point": [
            0.8768253968253968,
            5.07236313860852
          ]
        }
      },
      {
        "delta": 0.09375,
        "interval": [
          0.0625,
          0.125
        ],
        "completeMaterial": {
          "peak": 0.0526278749157626,
          "rms": 0.015562034616390587,
          "curvature": 28.8501055231942,
          "minAreaSquared": 0.8237919768355427,
          "minimumPolarAngularDeterminant": 0.6274005775872955,
          "minimumHeightRateAtFixedPolarAngle": 0.8156191942908408,
          "capHeightAnalyticSupportLower": 1.4135112764566684,
          "minimumActiveHeight": 0.78,
          "point": [
            0.8860317460317462,
            5.006913291658733
          ]
        }
      },
      {
        "delta": 0.1875,
        "interval": [
          0.125,
          0.25
        ],
        "completeMaterial": {
          "peak": 0.28019436176551243,
          "rms": 0.04570887560184968,
          "curvature": 46.261157433459495,
          "minAreaSquared": 0.7227402371117106,
          "minimumPolarAngularDeterminant": 0.6248437770499499,
          "minimumHeightRateAtFixedPolarAngle": 0.5034905708549416,
          "capHeightAnalyticSupportLower": 1.396215644232002,
          "minimumActiveHeight": 0.78,
          "point": [
            0.8367187500000001,
            5.006913291658733
          ]
        }
      },
      {
        "delta": 0.3125,
        "interval": [
          0.25,
          0.375
        ],
        "completeMaterial": {
          "peak": 0.1886705289974891,
          "rms": 0.05630308190056941,
          "curvature": 90.81471085413406,
          "minAreaSquared": 0.7272665065680317,
          "minimumPolarAngularDeterminant": 0.6288246545356577,
          "minimumHeightRateAtFixedPolarAngle": -0.1451134364880225,
          "capHeightAnalyticSupportLower": 1.3718197627915056,
          "minimumActiveHeight": 0.78,
          "point": [
            0.8360518829386829,
            1.5707963267948966
          ]
        }
      },
      {
        "delta": 0.4375,
        "interval": [
          0.375,
          0.5
        ],
        "completeMaterial": {
          "peak": 0.27465982178952536,
          "rms": 0.08192236490215414,
          "curvature": 113.8768345491753,
          "minAreaSquared": 0.6869168739997815,
          "minimumPolarAngularDeterminant": 0.6300507309673785,
          "minimumHeightRateAtFixedPolarAngle": -0.526587306025179,
          "capHeightAnalyticSupportLower": 1.3511544128063537,
          "minimumActiveHeight": 0.78,
          "point": [
            0.8088643829386829,
            4.810563750809371
          ]
        }
      }
    ],
    "scope": "finite observations along a defined C2-continuous family, not a continuous error or reach bound"
  }
}
```


## 可重算输出的身份

- C3-joint-phases.json: SHA-256 `0e2e7bc481032d0afe66ffe7f505f27da63561b14eace03241a7faff5526de7a` (53468 bytes).
- C3-joint-phases-phase1.npz: SHA-256 `468aece98feb73d0457c306f7fb8d505e66d37b73af9bb451577cd1e3193524e` (4713 bytes).
- C3-joint-phases-phase3.npz: SHA-256 `3d9eb0319ae272e280c9d1e5ab3cb7c69da3d89285c2d1743933749a044842df` (4719 bytes).
- C3-joint-phases-phase6.npz: SHA-256 `91b1c61a04af38dd5c661e69220b1a9626ac0cc49a538e33eafb508dbbf5f892` (4689 bytes).
- C3-joint-phases-phase5.npz: SHA-256 `31c49fb5e8083c6dbd3b2df08c2373f7ea92f77a5318e2a303d2978b221c31d9` (4684 bytes).
- C3-joint-phases-phase7.npz: SHA-256 `b49d0921ef3f38dea06156c953ab196aefc06a0d9a54f3a57182d351e7f26ef7` (4687 bytes).
- C3-joint-phases-phase4.npz: SHA-256 `8f1e9e57d6b64362354acfafec0777daee8214da2b05803909ff385191957b64` (4696 bytes).
- C3-joint-phases-phase8.npz: SHA-256 `b7ca60739ad2997b2ce4792f570926359c35510699292958995eee9295411f6d` (4688 bytes).
- C3-joint-phases-phase2.npz: SHA-256 `82081aeea6cf679022424e4561574f2b6ffb49525da9893ff22db7ca327af83c` (4716 bytes).

数组、完整输出和网格仅在 RUNNER_TEMP 生成，没有保存至 Git、Release 或 artifact。
