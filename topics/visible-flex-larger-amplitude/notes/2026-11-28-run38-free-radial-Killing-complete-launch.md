# Run38 — 完整自由径向 Killing 与同一冻结 Haar 度量求解

会话 Astra-larger-e4e2a2bf-20261126（AI）。承接R741/R742与36–37的实际失败，未达到README。本提交完整发布并触发独立公开Actions；run/job/source/PID及返回值只由随后实际记录填入，不预造。

## 数学输入与不变责任

十个完整闭参考：horizontal、tilt32、tilt44、soft32、soft44、Native及两端物理柄的32-18/32-30/32-42/44-30。全部直接使用原实际位置、两一阶及三二阶导数，未使用36/37优化点或截断投影作为输入。右柄窗口为S7((x−.65)/.30)，不得与独立R742右柄扫描的.70/.30窗口互借数值或证明。

真实向量场X=U∂s+W∂θ，U奇、W偶；左右完整兼容二jet。先固定真实F求线性Lie_X(g_F)，再对两条候选各作两层F/X交替求解。W的正下界通过全部非负样条控制及全角绝对和保留，圆作用/周期归一与Haar目标定义用R741；现有浮点流、采样Lie张量及积分差不是连续证书。

一次选择后记录实际cache内部正化后的fixed.cx，原始基和实际冻结向量SHA明确保留。两精化一直使用这一原始作用与同一Haar目标。非嵌套换基后的X只作诊断，不替换冻结作用；独立更密cache另存其实际向量SHA并报告是否完全相同。若两cache正化向量不同，差值包括该差，不冒同作用纯积分误差。轮廓修正后必须支付完整同g/嵌入/reach/held/grip/含反射δE与全时精化，原参考几何证明不自动转移。

## 原完整预算

初始10场：spans[3,8,2]/m10，径向[13,31,9]×96角，独立[26,73,19]×320，340 LSMR。保留最佳两场，各交替层的X迭代480/580、F评估72/85、F线性子步110/150；第二层spans[4,12,3]/m14、[16,43,11]×128、独立[30,99,23]×448。所有预算来自原完整6379B参数。

Haar原cache [22,59,17]/112半步/rtol2e−9，独立[35,94,25]/176/4e−10；比较[27,77,21]×194位移角。原7个U尺度[1,.8,.55,.3,.14,.05,0]逐一保留实际失败/成功，不补入新准入门。

同一目标两精化：[5,14,4]/m15，[17,49,13]×144、独立[31,109,27]×480、82 F评估/155 LSMR；[7,18,5]/m20，[21,61,15]×176、独立[39,137,31]×576、98/180。三最终完整场均计算整个上/下盘与肩的体积矩，并记录0、π/2、π整像点云和全部有序弦费用；这些有限点不代连续证明。

## 可执行入口、环境和实际观测

科学命令及全部依赖身份保[完整request](../computations/run38-bent-disk-killing-request.json)和[完整manifest](../computations/run38-complete-bent-disk-killing-source-and-launch-delivery.json)。入口为bent_disk_killing.py --params bent-disk-killing-design-v1.json --jet-source r742_tilted_disk_two_jets.py --out <runner>/field；所有路径绑定触发提交的不可变科学worktree。

公开ubuntu-latest、4 CPU/16 GB、Python3.12.14、numpy2.3.5/scipy1.17.0；BLAS/OMP/MKL各一线程。job360分钟，控制器不加科学子进程wall cutoff。每8秒观察、至少20秒重试发布、180秒发布实际进度、至多2700秒真实pull/rebase核两README。有变保存差异并遵守。日志/原NPZ仅runner；每个whole NPZ/summary实际字节和SHA保留。小型完整报告notes/run38-bent-disk-killing-<run>-<attempt>.json，所有异常和未返字段原样保留。

## 本次完整交付身份

八件总92568B；下列每一件已逐字读取并核字节、SHA256及Git blob，request/manifest中的同件引用已一致。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_disk_killing.py",
    "bytes": 22050,
    "git_blob_sha": "d3b8055dfc579c5af75cdebf7b5f387a39b6d8c4",
    "sha256": "963dc71f97d70c0a5bf80ad33da22a1ea4e3600347c8e26c2023772a111b6f6e"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_disk_killing_fields.py",
    "bytes": 10779,
    "git_blob_sha": "b66bae3ab3aace5e990c858c630bd9c0d1a993e2",
    "sha256": "cddef04056578a3e2b14f4506c3484b8ed0ee9e0de98757a0572617924805469"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_disk_killing_target.py",
    "bytes": 4055,
    "git_blob_sha": "3fdd92c129db20f41376dab916a4e6dbb9607164",
    "sha256": "030b617ad9fa9d5e8ec626dd9732fc751eb2670935867294f882a3c27c2cf2f2"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/bent-disk-killing-design-v1.json",
    "bytes": 6379,
    "git_blob_sha": "941e52186d2c5880e2a7238b86c407d7340fed67",
    "sha256": "49d65de32d08824e6721f8a9163fb13c209118b483645b668520da9baa8af087"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/observe_bent_disk_search.py",
    "bytes": 14863,
    "git_blob_sha": "c47dde7a91a32216afdb5f41ef2952fa3cb4b22c",
    "sha256": "72e7af7195e1087fa96f3a93b6f1963e60ae8d1ee13d4036f647673f8c25b450"
  },
  {
    "path": ".github/workflows/visible-larger-run38-bent-disk-killing.yml",
    "bytes": 3243,
    "git_blob_sha": "1e4e83bb485b65036a5ccab9d2d79b7507875690",
    "sha256": "e28beec77f44d3f0db79409c190e19e21c10b929d54139c2a9c1aa8e31c92dfd"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run38-bent-disk-killing-request.json",
    "bytes": 12337,
    "git_blob_sha": "19758fd6ad47d091b7ca50d53465d009578a4e6c",
    "sha256": "fde46166e4a63fd8743091d2e6d5a9692f958cee15a79adc12bf797fcf2818cb"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run38-complete-bent-disk-killing-source-and-launch-delivery.json",
    "bytes": 18862,
    "git_blob_sha": "5a4e0fd38857610f28925c82a258dbccd8ed1827",
    "sha256": "88ebbe53c71c68139c4c13e2d9780b4c929bd1093abe9dd8f3833acce444f3fa"
  }
]
```

此发布不等于已执行或已解。真实run由公开Actions返回后立即续记；不干预33–35尚在运行的科学子进程，不把36/37旧失败当新求解。

## 2026-11-28 12:43:16 UTC — 38 十六完整阶段自然返回与同Haar目标实际恶化

官方run46145189191/1、job140979589435全success；trigger/source 975d03650f7ad4c9641523e6018b7060427292a2，PID2553于2026-11-28T12:33:02Z进入真正科学入口，2026-11-28T12:40:13Z自然RC0。全部10初始+4交替+2固定阶段返回，用时418.36027598699997秒。源码与原参数预算全部执行；两固定层69/38次评估为原solver自然退出，不是预算削减。

stage13 tilt44被选择，一次冻结真实shape84350e3bf3b8c2573ddfc99ea7fbd8534f90d6648f00ef85d03bd858f9743561、X efc19d83394fecb4d2cd2bc68c178db385196bc807b2c51cb070c2f96387b65b及原基；两cache使用相同原向量，positive scale=1。两个实际表在独立共同格相对张量差max2.4072370923562953/RMS.1417033282879381，原目标求值误差尚很大。

两固定层原cache独立格Gram4.6303873878771675→9.607780255855785，密cache4.734943041299708→9.64107391752367；曲率工作最大22134636.41700951→18951840837.03279。没有同g精化收敛。负支撑只排除当前星形支撑证，约−1e−16的镜缝高度只是舍入量；这里不由此宣称自交。末完整点ac718a4b36763898980660b666133fb8794ebe5dabb16522e14d5e0e4f1131af。迁移到两层的X（f435e693…/2eb0a612…）只用于局部Killing诊断，不取代冻结原作用。

全部16原科学阶段/未知/费用、两表、源依赖、完整目标及三场三相与有向矩如下逐项保留。未证明闭嵌入时有向通量不作为R743实体体积/Cx或δE证明；有限点D/held/逆球不当连续证书。整个README目标仍未完成，改用R744/R745已付全几何的闭atlas，让两个端和盖也真可变。

```json
{
  "scientific_summary_file": {
    "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/summary.json",
    "bytes": 39564,
    "sha256": "fbf438fbd31c3ef1f1a08ea8f229e5dc69b8639b3767911adf924de71ce5748a"
  },
  "complete_scientific_summary": {
    "elapsed_seconds": 418.36027598699997,
    "frozen_source_npz_sha256": "89d69811a64d3b2a7ff560d5d06b8dd59b3ee45403662d6e4bb0dfc3382d81a3",
    "frozen_target": {
      "action": "Both fixed stages use the circle action of this same original shape basis and recorded preperiod vector. A transferred stage vector is used only for reporting the material Killing residual.",
      "cache": {
        "min_label_spacing": 0.00003896473829390068,
        "min_variational_derivative": 0.21257306504899126,
        "ode_calls": 1019,
        "period_range": [
          6.278303584208219,
          7.69135299392192
        ],
        "positive_clock_control_lower": 0.18000000000000016,
        "positive_clock_scale": 1,
        "radial_E_interval": [
          0.016607589274015747,
          54.968710287731454
        ],
        "radial_P2_interval": [
          0.8304442167480701,
          1.2012874287569135
        ],
        "samples": [
          96,
          224
        ]
      },
      "cache_table_sha256": "00787f3307b056326cec86b9747a4abc4e38781101a395862da8b2d21253ed26",
      "definition": "R741 (12)-(13) of the selected source shape and normalized material vector field, unchanged through both fixed steps. One cached rounded evaluator and one independent denser quadrature are retained.",
      "denser_table_sha256": "c29127aa7b09ee09a24af638d5383b73a69b8b8b0e9116da7a6eca0885960e4c",
      "identical_frozen_preperiod_vector": true,
      "independent": {
        "min_label_spacing": 0.000017363464182240662,
        "min_variational_derivative": 0.21232205134323026,
        "ode_calls": 1142,
        "period_range": [
          6.278512419378235,
          7.691802607950426
        ],
        "positive_clock_control_lower": 0.18000000000000016,
        "positive_clock_scale": 1,
        "radial_E_interval": [
          0.016788775641746818,
          55.53585901798346
        ],
        "radial_P2_interval": [
          0.8298597974158518,
          1.201306787852045
        ],
        "samples": [
          152,
          352
        ]
      },
      "independent_source_field_sha256": "efc19d83394fecb4d2cd2bc68c178db385196bc807b2c51cb070c2f96387b65b",
      "relative_cache_discrepancy_max": 2.4072370923562953,
      "relative_cache_discrepancy_rms": 0.1417033282879381,
      "source_field_before_cache_rescale_sha256": "efc19d83394fecb4d2cd2bc68c178db385196bc807b2c51cb070c2f96387b65b",
      "source_field_sha256": "efc19d83394fecb4d2cd2bc68c178db385196bc807b2c51cb070c2f96387b65b",
      "source_shape_sha256": "84350e3bf3b8c2573ddfc99ea7fbd8534f90d6648f00ef85d03bd858f9743561"
    },
    "numpy": "2.3.5",
    "orbit_integration_attempts": [
      {
        "radial_scale": 1,
        "status": "complete"
      }
    ],
    "params_sha256": "49d65de32d08824e6721f8a9163fb13c209118b483645b668520da9baa8af087",
    "schema": "finite-disk-killing-haar/v1",
    "science_sha256": "963dc71f97d70c0a5bf80ad33da22a1ea4e3600347c8e26c2023772a111b6f6e",
    "scipy": "1.17.0",
    "scope": "Actual full-circle shape and material field solve. Haar cache, independent integration, principal curvatures, ordered chord and volume moments are numerical. Exact symmetry, same-g path, reach and geometry certificates require continuum estimates.",
    "selected_source_stage": 13,
    "sources": {
      "bent_disk_arclength.py": "ee7793190ab74956e9df346b7c02e79386ef94c07db997279a7e76158fa0e3a6",
      "bent_disk_killing_fields.py": "cddef04056578a3e2b14f4506c3484b8ed0ee9e0de98757a0572617924805469",
      "bent_disk_killing_target.py": "030b617ad9fa9d5e8ec626dd9732fc751eb2670935867294f882a3c27c2cf2f2",
      "bent_disk_shoulder.py": "f77b38db6b58367c72463e4c6ed0234e7db7b1e61095f754792238eb34fa3c8e",
      "r740_rolled_disk_seed.py": "b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f",
      "r742_tilted_disk_two_jets.py": "5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd"
    },
    "stages": [
      {
        "angular_speed_control_lower": 0.17999999999999994,
        "check": {
          "Killing_op_max": 37.029874566052,
          "Killing_rms": 2.6608409955379435,
          "area_min": 0.08135055352897401,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.3861155736620723,
          "max_abs_principal": 397.4281083962778,
          "opposite_witness_to_upper": 0.803597729491887,
          "origin_radius": 1.2216651024540441,
          "support_min": 0.1187907860455484,
          "upper_height_min": 1.3877787807814457e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "extra": 0.54,
          "id": "horizontal",
          "parameters": {
            "end_height": 0.025,
            "gamma": 0,
            "height": 0.17,
            "join": 0.025,
            "left_handle": 0,
            "shift": 0.12
          }
        },
        "field_count": 284,
        "field_rescale": 0.7077130620166574,
        "field_sha256": "0fb2565d392e44ed33c89cb8e5b91e28a24714504c332395462855cf209e1363",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 18.30782963522747,
          "iterations": 340,
          "linear_norm": 2.425448829699055,
          "status": 7
        },
        "npz_bytes": 6238,
        "npz_sha256": "ad94fd242ac2c511b755f26b3b5e6826a9b99489984a70ef5224d01c7106b626",
        "point_sha256": "c2908bcc4d36eb732962746e7e2576716f0b370e66927e79cd6b7875e2759a35",
        "raw_polar_field": {
          "Killing_op_max": 80.85856029845513,
          "Killing_rms": 5.496451717932057,
          "area_min": 0.08135055352897401,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 397.4281083962778,
          "opposite_witness_to_upper": 0.803597729491887,
          "origin_radius": 1.2216651024540441,
          "support_min": 0.1187907860455484,
          "upper_height_min": 1.3877787807814457e-17
        },
        "score": 9.809711134972135,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 0,
        "train": {
          "Killing_op_max": 21.607501756305563,
          "Killing_rms": 2.5954491194572085,
          "area_min": 0.08134428169182947,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.38752767685069445,
          "max_abs_principal": 293.74988122744963,
          "opposite_witness_to_upper": 0.8035925198331335,
          "origin_radius": 1.2216610263024366,
          "support_min": 0.11879078604554841,
          "upper_height_min": 1.3877787807814457e-17
        }
      },
      {
        "angular_speed_control_lower": 0.17999999999999994,
        "check": {
          "Killing_op_max": 33.38931258952375,
          "Killing_rms": 2.978110932771448,
          "area_min": 0.16649870851238963,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.3969775564664185,
          "max_abs_principal": 1360.2349741753974,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.2614180298536035,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "extra": 0.58,
          "id": "tilt32",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.32,
            "height": 0.32,
            "join": 0.006,
            "left_handle": 0,
            "shift": 0.16
          }
        },
        "field_count": 284,
        "field_rescale": 0.7178122574805248,
        "field_sha256": "e65afa65abace964f799dc3666cec8fd1be62cf1cbc47c8498e8f26df1d908ed",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 24.881840770198668,
          "iterations": 340,
          "linear_norm": 2.415700524347241,
          "status": 7
        },
        "npz_bytes": 6238,
        "npz_sha256": "6f9e120d1ba26ce6d90e54ca5c600483bd704880694ab5145372e5b0395804ee",
        "point_sha256": "5ff482b501a1cc85d4938931e5ae3dc1983f60327d5bc3777d827a25a321bfa4",
        "raw_polar_field": {
          "Killing_op_max": 71.60880497636869,
          "Killing_rms": 4.763398459873465,
          "area_min": 0.16649870851238963,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 1360.2349741753974,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.2614180298536035,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "score": 11.453237331071017,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 1,
        "train": {
          "Killing_op_max": 21.352214020937225,
          "Killing_rms": 2.464821820768888,
          "area_min": 0.17497683546651618,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.3976625841448429,
          "max_abs_principal": 281.52983030999553,
          "opposite_witness_to_upper": 0.8035925198331334,
          "origin_radius": 1.2614194699646717,
          "support_min": 0.11879078604554834,
          "upper_height_min": -5.716372348916537e-17
        }
      },
      {
        "angular_speed_control_lower": 0.17999999999999994,
        "check": {
          "Killing_op_max": 34.69585014330228,
          "Killing_rms": 3.1635651056808785,
          "area_min": 0.14637638679543327,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.40135461079699364,
          "max_abs_principal": 1223.2325299460686,
          "opposite_witness_to_upper": 0.8035977294918869,
          "origin_radius": 1.2914174995711192,
          "support_min": 0.09694729417897913,
          "upper_height_min": -7.660457096012447e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "extra": 0.58,
          "id": "tilt44",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.44,
            "height": 0.37,
            "join": 0.006,
            "left_handle": 0,
            "shift": 0.19
          }
        },
        "field_count": 284,
        "field_rescale": 0.7081027758295275,
        "field_sha256": "4e761ce4484b3c3a205a70cd7b6b76b1c61a29066fc74915464c59cb0ea07483",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 11.854148243326932,
          "iterations": 340,
          "linear_norm": 2.4497789637432485,
          "status": 7
        },
        "npz_bytes": 6238,
        "npz_sha256": "f207066a9894acefeb3cb850daf26b4a6ebc9be6f14346d239eaaaa8b9e626b0",
        "point_sha256": "118a3af844bf53948d3ffbb212feb2da9894487aef33677909d47241082d9300",
        "raw_polar_field": {
          "Killing_op_max": 77.28205965291022,
          "Killing_rms": 5.056998776813273,
          "area_min": 0.14637638679543327,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 1223.2325299460686,
          "opposite_witness_to_upper": 0.8035977294918869,
          "origin_radius": 1.2914174995711192,
          "support_min": 0.09694729417897913,
          "upper_height_min": -7.660457096012447e-17
        },
        "score": 11.39277391002419,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 2,
        "train": {
          "Killing_op_max": 21.25951654964086,
          "Killing_rms": 2.5595711703141486,
          "area_min": 0.15758665110967132,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.4028610119590591,
          "max_abs_principal": 342.27645088925254,
          "opposite_witness_to_upper": 0.8035925198331333,
          "origin_radius": 1.2914191384754505,
          "support_min": 0.09694729417897906,
          "upper_height_min": -6.293169492056803e-17
        }
      },
      {
        "angular_speed_control_lower": 0.17999999999999994,
        "check": {
          "Killing_op_max": 41.04736645445183,
          "Killing_rms": 4.155424868674841,
          "area_min": 0.02381856582382575,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.44585285948334585,
          "max_abs_principal": 1360.2349741753976,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.2614180298536035,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "extra": 0.58,
          "id": "soft32",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.32,
            "height": 0.32,
            "join": 0.006,
            "left_handle": 0.09,
            "shift": 0.16
          }
        },
        "field_count": 284,
        "field_rescale": 0.7261899281651628,
        "field_sha256": "4de2db9f807c42fd2e4b3e34450fca4f935568b6d2e78ea54b7044702b1e276b",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 138.6142814165978,
          "iterations": 340,
          "linear_norm": 3.662874139282779,
          "status": 7
        },
        "npz_bytes": 6238,
        "npz_sha256": "3fd5815135e256365645397381116b67b1aa9c1e699c304c917eeae0cbc99133",
        "point_sha256": "261b35c415faad7fe49c67099782eca5698ddb0a68c9594b58d18fa406bd45e9",
        "raw_polar_field": {
          "Killing_op_max": 71.6088049763687,
          "Killing_rms": 7.565353450557148,
          "area_min": 0.02381856582382575,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 1360.2349741753976,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.2614180298536035,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "score": 11.91353071726478,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 3,
        "train": {
          "Killing_op_max": 27.546524185186772,
          "Killing_rms": 3.8909005098931324,
          "area_min": 0.023848503128847377,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.4507366352884833,
          "max_abs_principal": 281.5298303099953,
          "opposite_witness_to_upper": 0.8035925198331334,
          "origin_radius": 1.2614194699646717,
          "support_min": 0.11879078604554834,
          "upper_height_min": -5.716372348916537e-17
        }
      },
      {
        "angular_speed_control_lower": 0.17999999999999994,
        "check": {
          "Killing_op_max": 43.94720999061511,
          "Killing_rms": 4.2584038987131025,
          "area_min": 0.023854671581946374,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.44231686492499545,
          "max_abs_principal": 1223.232529946069,
          "opposite_witness_to_upper": 0.8035977294918869,
          "origin_radius": 1.2914174995711192,
          "support_min": 0.09694729417897913,
          "upper_height_min": -7.660457096012447e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "extra": 0.58,
          "id": "soft44",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.44,
            "height": 0.37,
            "join": 0.006,
            "left_handle": 0.09,
            "shift": 0.19
          }
        },
        "field_count": 284,
        "field_rescale": 0.7367380298741504,
        "field_sha256": "96d3099a5031197975df0fbcee8f007ebdbb561aee6e2972c5c19f111a197c40",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 15.51906829181405,
          "iterations": 340,
          "linear_norm": 3.58210145785589,
          "status": 7
        },
        "npz_bytes": 6238,
        "npz_sha256": "04f1d6d2b0d7c4921683e6411f8f5aeb138b4e75cee7e5d5dea806c152533c79",
        "point_sha256": "2b5c94b67b18930dbf01797428b004d5225f4277baa13153e567ad762cd6a0c7",
        "raw_polar_field": {
          "Killing_op_max": 77.28205965291023,
          "Killing_rms": 7.964229322283992,
          "area_min": 0.023854671581946374,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 1223.232529946069,
          "opposite_witness_to_upper": 0.8035977294918869,
          "origin_radius": 1.2914174995711192,
          "support_min": 0.09694729417897913,
          "upper_height_min": -7.660457096012447e-17
        },
        "score": 11.85668399587026,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 4,
        "train": {
          "Killing_op_max": 27.654540692791052,
          "Killing_rms": 3.860593644423556,
          "area_min": 0.023888154056295907,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.44451191797867606,
          "max_abs_principal": 342.2764508892522,
          "opposite_witness_to_upper": 0.8035925198331333,
          "origin_radius": 1.2914191384754505,
          "support_min": 0.09694729417897906,
          "upper_height_min": -6.293169492056803e-17
        }
      },
      {
        "angular_speed_control_lower": 0.4729960318300265,
        "check": {
          "Killing_op_max": 96.44117221414996,
          "Killing_rms": 1.992854746692528,
          "area_min": 0.008162473753326042,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.6035973024121581,
          "max_abs_principal": 45108.00632746887,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.200602835070457,
          "support_min": -1.0058745695149587,
          "upper_height_min": -6.01414998046007e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "id": "native"
        },
        "field_count": 284,
        "field_rescale": 1,
        "field_sha256": "1212e1d6026e0c7c4afc469bafb76bb0b51346dab3a85d00741a669bab915e00",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 39.98678836413921,
          "iterations": 160,
          "linear_norm": 1.8739226772962492,
          "status": 2
        },
        "npz_bytes": 6238,
        "npz_sha256": "3ba1f2430fa3236ee5a3cfd9d6ef3be22b96be17ea4d0c540eba550274b9992c",
        "point_sha256": "d8b2d01cd670289f5d7f5f1790ea009216efa598496d99152a4433961aea8e4e",
        "raw_polar_field": {
          "Killing_op_max": 100.33158803468132,
          "Killing_rms": 3.3310949437563155,
          "area_min": 0.008162473753326042,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 45108.00632746887,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.200602835070457,
          "support_min": -1.0058745695149587,
          "upper_height_min": -6.01414998046007e-17
        },
        "score": 21.300552335466705,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 5,
        "train": {
          "Killing_op_max": 22.66436351063786,
          "Killing_rms": 1.737772305544492,
          "area_min": 0.004637196686278658,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.6035968875607476,
          "max_abs_principal": 145116.5213558211,
          "opposite_witness_to_upper": 0.8035925198331334,
          "origin_radius": 1.2002122508112991,
          "support_min": -1.005775936875951,
          "upper_height_min": -4.311188974507386e-17
        }
      },
      {
        "angular_speed_control_lower": 0.17999999999999994,
        "check": {
          "Killing_op_max": 66.55834861935064,
          "Killing_rms": 6.960561531895626,
          "area_min": 0.02378856394711016,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.4749954182155618,
          "max_abs_principal": 1298.6987839816456,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.2614500573552854,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "extra": 0.58,
          "id": "two-handle32-18",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.32,
            "height": 0.32,
            "join": 0.006,
            "left_handle": 0.14,
            "shift": 0.16
          },
          "right_handle": 0.18
        },
        "field_count": 284,
        "field_rescale": 0.5481568732447533,
        "field_sha256": "a74860d530f3889b7b24187058b897578ed47ffda9847796b9ef210a94f2e8c6",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 19.487707068938615,
          "iterations": 340,
          "linear_norm": 4.399526340106141,
          "status": 7
        },
        "npz_bytes": 6238,
        "npz_sha256": "8d3e64979035ad8e5dd487c65efe3ee8abb0f4c864514f543552af85fa52b5ed",
        "point_sha256": "841b181b6a6c847d65cda93fd9c05ee23e0843f30c79c1fe77dee11f54d11a95",
        "raw_polar_field": {
          "Killing_op_max": 134.51488867473807,
          "Killing_rms": 12.579564928310496,
          "area_min": 0.02378856394711016,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 1298.6987839816456,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.2614500573552854,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "score": 12.759677865525042,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 6,
        "train": {
          "Killing_op_max": 64.3410715650489,
          "Killing_rms": 6.84166234318007,
          "area_min": 0.023815101033582805,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.4775704897402745,
          "max_abs_principal": 344.27251697891404,
          "opposite_witness_to_upper": 0.8035925198331334,
          "origin_radius": 1.2614509479735907,
          "support_min": 0.11879078604554834,
          "upper_height_min": -5.716372348916537e-17
        }
      },
      {
        "angular_speed_control_lower": 0.18000000000000005,
        "check": {
          "Killing_op_max": 80.29772053622402,
          "Killing_rms": 7.42827122044629,
          "area_min": 0.02378856394711016,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.47624700935573594,
          "max_abs_principal": 1296.607978230406,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.26153032688076,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "extra": 0.58,
          "id": "two-handle32-30",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.32,
            "height": 0.32,
            "join": 0.006,
            "left_handle": 0.14,
            "shift": 0.16
          },
          "right_handle": 0.3
        },
        "field_count": 284,
        "field_rescale": 0.5453304526891593,
        "field_sha256": "dc8f22c5db622f6cb207df23bac406768355b73d1fb6c1356782cc192ca80551",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 11.663560992462543,
          "iterations": 340,
          "linear_norm": 4.42755146936961,
          "status": 7
        },
        "npz_bytes": 6238,
        "npz_sha256": "402f7e145c6b21ff30d7b4e0a49918fae402520cf7eb463a2fa6ad9a625196df",
        "point_sha256": "c9141abb28e8bee7b649048d47ca2d772451874b3cf40b64efa43363aff37d8b",
        "raw_polar_field": {
          "Killing_op_max": 162.02591690677997,
          "Killing_rms": 13.546760275213106,
          "area_min": 0.02378856394711016,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 1296.607978230406,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.26153032688076,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "score": 12.999721182089923,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 7,
        "train": {
          "Killing_op_max": 69.70025881429639,
          "Killing_rms": 7.065976731636884,
          "area_min": 0.023815101033582805,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.47879706983853965,
          "max_abs_principal": 281.5298303099953,
          "opposite_witness_to_upper": 0.8035925198331334,
          "origin_radius": 1.2615167557796425,
          "support_min": 0.11879078604554834,
          "upper_height_min": -5.716372348916537e-17
        }
      },
      {
        "angular_speed_control_lower": 0.17999999999999994,
        "check": {
          "Killing_op_max": 89.2213143102106,
          "Killing_rms": 7.762919447562576,
          "area_min": 0.02378856394711016,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.47663388531874196,
          "max_abs_principal": 1295.470111286874,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.2617640741637968,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "extra": 0.58,
          "id": "two-handle32-42",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.32,
            "height": 0.32,
            "join": 0.006,
            "left_handle": 0.14,
            "shift": 0.16
          },
          "right_handle": 0.42
        },
        "field_count": 284,
        "field_rescale": 0.5473859654177872,
        "field_sha256": "717f1610518535f0b857bd24588a440d837b8b5342b9982bff34ae7ce6854510",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 12.235633157868856,
          "iterations": 340,
          "linear_norm": 4.43240406973325,
          "status": 7
        },
        "npz_bytes": 6238,
        "npz_sha256": "50e520d344febb2edb74a923415b03d120797b3071bd8be69c32e81a2d18e9aa",
        "point_sha256": "2dcd14c00bac74adb4bb28ce70aeff4e89295c57448ef56a6ca4cea2f5066379",
        "raw_polar_field": {
          "Killing_op_max": 178.6000155412437,
          "Killing_rms": 14.244498901116618,
          "area_min": 0.02378856394711016,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 1295.470111286874,
          "opposite_witness_to_upper": 0.8035977294918868,
          "origin_radius": 1.2617640741637968,
          "support_min": 0.1187907860455483,
          "upper_height_min": -5.909433344116524e-17
        },
        "score": 13.141621104283217,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 8,
        "train": {
          "Killing_op_max": 70.82172020721205,
          "Killing_rms": 6.980239355948274,
          "area_min": 0.023815101033582805,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.4784457739135404,
          "max_abs_principal": 281.5298303099953,
          "opposite_witness_to_upper": 0.8035925198331334,
          "origin_radius": 1.2617095043408628,
          "support_min": 0.11879078604554834,
          "upper_height_min": -5.716372348916537e-17
        }
      },
      {
        "angular_speed_control_lower": 0.18000000000000005,
        "check": {
          "Killing_op_max": 77.01017484739714,
          "Killing_rms": 7.344797004332266,
          "area_min": 0.023791200641750877,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.4807359817273963,
          "max_abs_principal": 1121.1040243362881,
          "opposite_witness_to_upper": 0.8035977294918869,
          "origin_radius": 1.291559114071865,
          "support_min": 0.09694729417897913,
          "upper_height_min": -7.660457096012447e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 340,
          "id": "linear-on-original-geometry",
          "lsmr": 0,
          "max_feval": 0,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0,
          "spans": [
            3,
            8,
            2
          ]
        },
        "design": {
          "extra": 0.58,
          "id": "two-handle44-30",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.44,
            "height": 0.37,
            "join": 0.006,
            "left_handle": 0.14,
            "shift": 0.19
          },
          "right_handle": 0.3
        },
        "field_count": 284,
        "field_rescale": 0.5494126188437718,
        "field_sha256": "cc0af876ea2a021fbb15bc6d1a82a59078bb2290eee48873cd5d6f793d9be905",
        "kind": "fixed_actual_shape_killing",
        "linear_solve": {
          "condition_estimate": 11.129880595017946,
          "iterations": 340,
          "linear_norm": 4.457475582956222,
          "status": 7
        },
        "npz_bytes": 6238,
        "npz_sha256": "df8f74f12bfc37e4ae29d7a777e30a7d0a9e14353df194af9643a4df4565125d",
        "point_sha256": "139bccc842ff64d2de9292593b9d06e6538378d0cbb6afec50c3720ff4feb15c",
        "raw_polar_field": {
          "Killing_op_max": 155.28035347465607,
          "Killing_rms": 13.345065147293418,
          "area_min": 0.023791200641750877,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 1,
          "max_abs_principal": 1121.1040243362881,
          "opposite_witness_to_upper": 0.8035977294918869,
          "origin_radius": 1.291559114071865,
          "support_min": 0.09694729417897913,
          "upper_height_min": -7.660457096012447e-17
        },
        "score": 12.752148167622309,
        "shape_count": 426,
        "shape_sha256": "b14366c44ff17f7eb4cb7b06bcea230765a6368ea3faed76c41c419cbcb3c83d",
        "stage": 9,
        "train": {
          "Killing_op_max": 66.63898936677357,
          "Killing_rms": 6.988951944575827,
          "area_min": 0.023826164786634702,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.4834543601787894,
          "max_abs_principal": 342.2764508892522,
          "opposite_witness_to_upper": 0.8035925198331333,
          "origin_radius": 1.291534275265443,
          "support_min": 0.09694729417897906,
          "upper_height_min": -6.293169492056803e-17
        }
      },
      {
        "adjoint_abs": 1.5265566588595902e-16,
        "angular_speed_control_lower": 0.17999999999999994,
        "check": {
          "Killing_op_max": 1012.8243522626879,
          "Killing_rms": 14.850799340025608,
          "area_min": 0.00035918394208088445,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.5503032001045589,
          "max_abs_principal": 10229726.202662598,
          "opposite_witness_to_upper": 0.803597729491887,
          "origin_radius": 1.2214992444265012,
          "support_min": -1.0805948852464615,
          "upper_height_min": 1.3877787807814457e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 480,
          "id": "alternating-physical-1",
          "lsmr": 110,
          "max_feval": 72,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0.00001,
          "spans": [
            3,
            8,
            2
          ]
        },
        "cost": 1.4742416206689755,
        "design": {
          "extra": 0.54,
          "id": "horizontal",
          "parameters": {
            "end_height": 0.025,
            "gamma": 0,
            "height": 0.17,
            "join": 0.025,
            "left_handle": 0,
            "shift": 0.12
          }
        },
        "directional_fd_relative": 2.2297973831525407e-10,
        "field_count": 284,
        "field_rescale": 0.4691008717049709,
        "field_sha256": "3fa85243d9f1183ffe83c0403342dfc187c133444170e2ffb37f75b4cda9e2e5",
        "kind": "alternate_shape_and_material",
        "linear_solve": {
          "condition_estimate": 4573.505852222387,
          "iterations": 480,
          "linear_norm": 4.536037948814065,
          "status": 7
        },
        "nfev": 72,
        "njev": 49,
        "npz_bytes": 6238,
        "npz_sha256": "16a112bb702d89acf5b54b378d2a30e7a06767d1ba8e1dcad2355d77ea4bd7e7",
        "optimality": 3.1855803610513007,
        "point_sha256": "4b568977634a02749a628a364e5d911710ec470e7ce6add0e026079140274249",
        "score": 32.93105295354172,
        "shape_count": 426,
        "shape_sha256": "2740d4c988144a0080a6165fce35636761458bad1cd80d10a9b61b432b269f4d",
        "solver_status": 0,
        "stage": 10,
        "train": {
          "Killing_op_max": 36885.232407218806,
          "Killing_rms": 745.5533656660803,
          "area_min": 0.000009718351527734255,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.5503601428336429,
          "max_abs_principal": 2355076059.8354816,
          "opposite_witness_to_upper": 0.8035925198331335,
          "origin_radius": 1.221500354292163,
          "support_min": -0.7615932381751911,
          "upper_height_min": 1.3877787807814457e-17
        }
      },
      {
        "adjoint_abs": 5.9396931817445875e-15,
        "angular_speed_control_lower": 0.18000000000000005,
        "check": {
          "Killing_op_max": 451.1261985284906,
          "Killing_rms": 7.926070198373935,
          "area_min": 0.00008623594444697919,
          "check_shape": [
            150,
            448
          ],
          "clock_min_sample": 0.43681988592526444,
          "max_abs_principal": 133100968.27340028,
          "opposite_witness_to_upper": 0.8035951778284829,
          "origin_radius": 1.2215035855203664,
          "support_min": -0.8987852717158792,
          "upper_height_min": 1.3877787807814457e-17
        },
        "configuration": {
          "angular": 128,
          "check_angular": 448,
          "check_radial": [
            30,
            99,
            23
          ],
          "field_iterations": 580,
          "id": "alternating-physical-2",
          "lsmr": 150,
          "max_feval": 85,
          "mode": 14,
          "radial": [
            16,
            43,
            11
          ],
          "regularizer": 0.000004,
          "spans": [
            4,
            12,
            3
          ]
        },
        "cost": 2.758594588119648,
        "design": {
          "extra": 0.54,
          "id": "horizontal",
          "parameters": {
            "end_height": 0.025,
            "gamma": 0,
            "height": 0.17,
            "join": 0.025,
            "left_handle": 0,
            "shift": 0.12
          }
        },
        "directional_fd_relative": 9.47352070853448e-8,
        "field_count": 566,
        "field_rescale": 0.5776947212645449,
        "field_sha256": "99a4365cbe80760490aac9cd5d56dd1c4ea6a70ec84a8e37e275772aaf059bcd",
        "kind": "alternate_shape_and_material",
        "linear_solve": {
          "condition_estimate": 285.8470470291391,
          "iterations": 580,
          "linear_norm": 4.776414040793008,
          "status": 7
        },
        "nfev": 85,
        "njev": 63,
        "npz_bytes": 11886,
        "npz_sha256": "eed1eac56bbd4815fed432dc07f3c0fed8e80d491d6034e23fdc5e70181137e6",
        "optimality": 115.13564582742546,
        "point_sha256": "6a95c8ea1b302df77f7b8ef67330d01a2fe368459b03ebec4b40357710b47cd9",
        "score": 34.28589094345776,
        "shape_count": 850,
        "shape_sha256": "4d8320486aebad84f27866fb386b9cd107e5fa1eb2f0d21b7ab7b9679c46b1e3",
        "solver_status": 0,
        "stage": 11,
        "train": {
          "Killing_op_max": 2222.9767826881753,
          "Killing_rms": 39.2849665044133,
          "area_min": 0.00003876382430831883,
          "check_shape": [
            68,
            128
          ],
          "clock_min_sample": 0.4374045833542566,
          "max_abs_principal": 218718824.88723844,
          "opposite_witness_to_upper": 0.8035925198331335,
          "origin_radius": 1.2215041541668432,
          "support_min": -0.757173942869598,
          "upper_height_min": 1.3877787807814457e-17
        }
      },
      {
        "adjoint_abs": 4.440892098500626e-16,
        "angular_speed_control_lower": 0.18000000000000005,
        "check": {
          "Killing_op_max": 116.63540502636587,
          "Killing_rms": 4.649588227857307,
          "area_min": 0.0026535362688383793,
          "check_shape": [
            116,
            320
          ],
          "clock_min_sample": 0.49920587982297193,
          "max_abs_principal": 406962.032221928,
          "opposite_witness_to_upper": 0.8035977294918869,
          "origin_radius": 1.2914357295285464,
          "support_min": -0.47120716268014096,
          "upper_height_min": -7.660457096012447e-17
        },
        "configuration": {
          "angular": 96,
          "check_angular": 320,
          "check_radial": [
            26,
            73,
            19
          ],
          "field_iterations": 480,
          "id": "alternating-physical-1",
          "lsmr": 110,
          "max_feval": 72,
          "mode": 10,
          "radial": [
            13,
            31,
            9
          ],
          "regularizer": 0.00001,
          "spans": [
            3,
            8,
            2
          ]
        },
        "cost": 0.9375284175384049,
        "design": {
          "extra": 0.58,
          "id": "tilt44",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.44,
            "height": 0.37,
            "join": 0.006,
            "left_handle": 0,
            "shift": 0.19
          }
        },
        "directional_fd_relative": 5.546225533130834e-10,
        "field_count": 284,
        "field_rescale": 0.5416377194982529,
        "field_sha256": "cfb040db6bb4fb60fc4553d9d264d7a13c1dbd86d86c0d63d16c1dfad1e35c07",
        "kind": "alternate_shape_and_material",
        "linear_solve": {
          "condition_estimate": 125.2921123410541,
          "iterations": 480,
          "linear_norm": 2.6594566869426215,
          "status": 7
        },
        "nfev": 72,
        "njev": 59,
        "npz_bytes": 6238,
        "npz_sha256": "218c71b99cccfa6a208a371ee0587bfd84ccfd078127bdd3322b538073bf6c5d",
        "optimality": 6.845093955984303,
        "point_sha256": "657225511153688b2f49cf9111dc98ba155f8749ed3dcfd9b1f2da81f4401ed5",
        "score": 22.95512008157826,
        "shape_count": 426,
        "shape_sha256": "d065485f1113e615ecbf5ad28df6a9cf1d95650eae72356b1fb15e0a26c8cd52",
        "solver_status": 0,
        "stage": 12,
        "train": {
          "Killing_op_max": 771.7892134261203,
          "Killing_rms": 16.24167703678859,
          "area_min": 0.0027848757779521463,
          "check_shape": [
            51,
            96
          ],
          "clock_min_sample": 0.4999119975909557,
          "max_abs_principal": 549280.9469991272,
          "opposite_witness_to_upper": 0.8035925198331333,
          "origin_radius": 1.2914373887090551,
          "support_min": -0.18113470317728253,
          "upper_height_min": -6.293169492056803e-17
        }
      },
      {
        "adjoint_abs": 1.7763568394002505e-14,
        "angular_speed_control_lower": 0.17999999999999994,
        "check": {
          "Killing_op_max": 1883.942037507727,
          "Killing_rms": 16.14776059137151,
          "area_min": 0.0002954223453726699,
          "check_shape": [
            150,
            448
          ],
          "clock_min_sample": 0.5028586780125325,
          "max_abs_principal": 10224032.570169672,
          "opposite_witness_to_upper": 0.8035951778284828,
          "origin_radius": 1.2914014822405608,
          "support_min": -1.019840242417692,
          "upper_height_min": -1.0465897170063843e-16
        },
        "configuration": {
          "angular": 128,
          "check_angular": 448,
          "check_radial": [
            30,
            99,
            23
          ],
          "field_iterations": 580,
          "id": "alternating-physical-2",
          "lsmr": 150,
          "max_feval": 85,
          "mode": 14,
          "radial": [
            16,
            43,
            11
          ],
          "regularizer": 0.000004,
          "spans": [
            4,
            12,
            3
          ]
        },
        "cost": 1.4387882721184353,
        "design": {
          "extra": 0.58,
          "id": "tilt44",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.44,
            "height": 0.37,
            "join": 0.006,
            "left_handle": 0,
            "shift": 0.19
          }
        },
        "directional_fd_relative": 2.0829123888416585e-10,
        "field_count": 566,
        "field_rescale": 0.4902064329439376,
        "field_sha256": "efc19d83394fecb4d2cd2bc68c178db385196bc807b2c51cb070c2f96387b65b",
        "kind": "alternate_shape_and_material",
        "linear_solve": {
          "condition_estimate": 27267.813983921766,
          "iterations": 580,
          "linear_norm": 9.15451497271738,
          "status": 7
        },
        "nfev": 85,
        "njev": 64,
        "npz_bytes": 11886,
        "npz_sha256": "89d69811a64d3b2a7ff560d5d06b8dd59b3ee45403662d6e4bb0dfc3382d81a3",
        "optimality": 22.632199905005237,
        "point_sha256": "33e446cd02c76409f10b9b5911ffacbb358bd2f390e4aed4fe97019b18959171",
        "sampled_entire_phases": [
          {
            "center_witness": 0.004999999999999893,
            "diameter": 2.202837768173485,
            "held": 0,
            "ordered_inverse_ball": 9042.978489917818,
            "phase": 0,
            "point_count": 2534
          },
          {
            "center_witness": 0.4704414073164541,
            "diameter": 2.202837768173485,
            "held": 0.6556422451277139,
            "ordered_inverse_ball": 9042.978489917818,
            "phase": 1.5707963267948966,
            "point_count": 2534
          },
          {
            "center_witness": 0.5974697916097655,
            "diameter": 2.202837768173485,
            "held": 0.6164800941550517,
            "ordered_inverse_ball": 9042.978489917818,
            "phase": 3.141592653589793,
            "point_count": 2534
          }
        ],
        "score": 33.38609785408723,
        "shape_count": 850,
        "shape_sha256": "84350e3bf3b8c2573ddfc99ea7fbd8534f90d6648f00ef85d03bd858f9743561",
        "solver_status": 0,
        "stage": 13,
        "train": {
          "Killing_op_max": 101184.05967550137,
          "Killing_rms": 1533.8764934474098,
          "area_min": 5.878842322531003e-7,
          "check_shape": [
            68,
            128
          ],
          "clock_min_sample": 0.5040543007349502,
          "max_abs_principal": 1758319594732.644,
          "opposite_witness_to_upper": 0.8035925198331333,
          "origin_radius": 1.2914022951855175,
          "support_min": -0.5557595217932655,
          "upper_height_min": -6.293169492056803e-17
        },
        "volume_moments": {
          "fixed_marker_first_moment_x": -4.1783182292744206e-10,
          "marked_central_second_moment_pi_difference": 1.4399683410802832e-11,
          "signed_unmarked_first_moment_x": -0.0212472198768775,
          "signed_unmarked_volume": 2.466099849136752
        }
      },
      {
        "adjoint_abs": 1.354472090042691e-14,
        "check": {
          "Killing_op_max": 7770.524401537529,
          "Killing_rms": 52.06379250301435,
          "area_min": 0.0003543507687211725,
          "check_shape": [
            165,
            480
          ],
          "clock_min_sample": 0.5032589630400411,
          "frozen_gram_max": 4.6303873878771675,
          "frozen_gram_rms": 0.5267159542943542,
          "max_abs_principal": 22134636.41700951,
          "opposite_witness_to_upper": 0.8035948352431393,
          "origin_radius": 1.2914019360096793,
          "support_min": -0.9420234882584296,
          "upper_height_min": -9.935874544866068e-17
        },
        "configuration": {
          "angular": 144,
          "check_angular": 480,
          "check_radial": [
            31,
            109,
            27
          ],
          "field_iterations": 0,
          "id": "fixed-Haar-1",
          "lsmr": 155,
          "max_feval": 82,
          "mode": 15,
          "radial": [
            17,
            49,
            13
          ],
          "regularizer": 0.000002,
          "spans": [
            5,
            14,
            4
          ]
        },
        "cost": 0.16936903120819807,
        "design": {
          "extra": 0.58,
          "id": "tilt44",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.44,
            "height": 0.37,
            "join": 0.006,
            "left_handle": 0,
            "shift": 0.19
          }
        },
        "directional_fd_relative": 0.00025064596051589157,
        "field_count": 729,
        "field_sha256": "f435e693f134d4d8e5674b34cb8556d1b1379f65d0279f1295f6229c81439c11",
        "frozen_action_source_field_sha256": "efc19d83394fecb4d2cd2bc68c178db385196bc807b2c51cb070c2f96387b65b",
        "independent_same_target": {
          "Killing_op_max": 7770.524401537529,
          "Killing_rms": 52.06379250301435,
          "area_min": 0.0003543507687211725,
          "check_shape": [
            165,
            480
          ],
          "clock_min_sample": 0.5032589630400411,
          "frozen_gram_max": 4.734943041299708,
          "frozen_gram_rms": 0.5354968970901659,
          "max_abs_principal": 22134636.41700951,
          "opposite_witness_to_upper": 0.8035948352431393,
          "origin_radius": 1.2914019360096793,
          "support_min": -0.9420234882584296,
          "upper_height_min": -9.935874544866068e-17
        },
        "kind": "same_frozen_Haar_shape",
        "nfev": 69,
        "njev": 45,
        "npz_bytes": 15158,
        "npz_sha256": "be3348eef87731d3939a067898ed71a10a7f1bfcdddc1fb57833b0db9a62d2d2",
        "optimality": 15.261179057331933,
        "point_sha256": "1865f1dd31607063944bcf16b3331508dc0a54015c8c225b672f4ea1d4166dc6",
        "sampled_entire_phases": [
          {
            "center_witness": 0.004999999999999893,
            "diameter": 2.220128784473113,
            "held": 0,
            "ordered_inverse_ball": 33591.47395206963,
            "phase": 0,
            "point_count": 2534
          },
          {
            "center_witness": 0.47069391183428566,
            "diameter": 2.220128784473113,
            "held": 0.6551203074997326,
            "ordered_inverse_ball": 33591.47395206963,
            "phase": 1.5707963267948966,
            "point_count": 2534
          },
          {
            "center_witness": 0.5974697916097655,
            "diameter": 2.220128784473113,
            "held": 0.6170133293190968,
            "ordered_inverse_ball": 33591.47395206963,
            "phase": 3.141592653589793,
            "point_count": 2534
          }
        ],
        "score": 36.663770788768,
        "shape_count": 1096,
        "shape_sha256": "af5c23a370c1603321b8deb11f77980954349fcedc9e4594d21f923286165c69",
        "solver_status": 4,
        "stage": 14,
        "train": {
          "Killing_op_max": 1410611.0558687625,
          "Killing_rms": 13396.19598062629,
          "area_min": 0.0000015652669592813432,
          "check_shape": [
            77,
            144
          ],
          "clock_min_sample": 0.5037754627668396,
          "frozen_gram_max": 4.9575686832522,
          "frozen_gram_rms": 0.527682035944209,
          "max_abs_principal": 22147706227.788506,
          "opposite_witness_to_upper": 0.8035925198331333,
          "origin_radius": 1.2914026650836825,
          "support_min": -0.24891595418833368,
          "upper_height_min": -8.11121345477864e-17
        },
        "transferred_diagnostic_field_sha256": "f435e693f134d4d8e5674b34cb8556d1b1379f65d0279f1295f6229c81439c11",
        "volume_moments": {
          "fixed_marker_first_moment_x": -4.1783182292744206e-10,
          "marked_central_second_moment_pi_difference": -8.62447503730372e-11,
          "signed_unmarked_first_moment_x": 0.12824501313809444,
          "signed_unmarked_volume": 2.4852455526130064
        }
      },
      {
        "adjoint_abs": 3.552713678800501e-15,
        "check": {
          "Killing_op_max": 85001.16825742641,
          "Killing_rms": 303.2193967886608,
          "area_min": 0.00013148639553890655,
          "check_shape": [
            205,
            576
          ],
          "clock_min_sample": 0.5033365762726365,
          "frozen_gram_max": 9.607780255855785,
          "frozen_gram_rms": 0.5611082405971355,
          "max_abs_principal": 18951840837.03279,
          "opposite_witness_to_upper": 0.8035941277577867,
          "origin_radius": 1.2914052739599309,
          "support_min": -0.9726544515609259,
          "upper_height_min": -1.0275498299328488e-16
        },
        "configuration": {
          "angular": 176,
          "check_angular": 576,
          "check_radial": [
            39,
            137,
            31
          ],
          "field_iterations": 0,
          "id": "fixed-Haar-2",
          "lsmr": 180,
          "max_feval": 98,
          "mode": 20,
          "radial": [
            21,
            61,
            15
          ],
          "regularizer": 9e-7,
          "spans": [
            7,
            18,
            5
          ]
        },
        "cost": 0.23779781548223256,
        "design": {
          "extra": 0.58,
          "id": "tilt44",
          "parameters": {
            "end_height": 0.006,
            "gamma": 0.44,
            "height": 0.37,
            "join": 0.006,
            "left_handle": 0,
            "shift": 0.19
          }
        },
        "directional_fd_relative": 1.222179812128246e-10,
        "field_count": 1251,
        "field_sha256": "2eb0a612e97d028e78f962f68b65206abeed8278e7e3dd9071284b415c2bd3cd",
        "frozen_action_source_field_sha256": "efc19d83394fecb4d2cd2bc68c178db385196bc807b2c51cb070c2f96387b65b",
        "independent_same_target": {
          "Killing_op_max": 85001.16825742641,
          "Killing_rms": 303.2193967886608,
          "area_min": 0.00013148639553890655,
          "check_shape": [
            205,
            576
          ],
          "clock_min_sample": 0.5033365762726365,
          "frozen_gram_max": 9.64107391752367,
          "frozen_gram_rms": 0.5620308205317127,
          "max_abs_principal": 18951840837.03279,
          "opposite_witness_to_upper": 0.8035941277577867,
          "origin_radius": 1.2914052739599309,
          "support_min": -0.9726544515609259,
          "upper_height_min": -1.0275498299328488e-16
        },
        "kind": "same_frozen_Haar_shape",
        "nfev": 38,
        "njev": 19,
        "npz_bytes": 25606,
        "npz_sha256": "e44566d57fa438a23bb76704aadb3fe6422f31fa7a1223cb412c3f0187818901",
        "optimality": 77.49361324279116,
        "point_sha256": "ac718a4b36763898980660b666133fb8794ebe5dabb16522e14d5e0e4f1131af",
        "sampled_entire_phases": [
          {
            "center_witness": 0.004999999999999893,
            "diameter": 2.219498727364315,
            "held": 0,
            "ordered_inverse_ball": 429448.04619797954,
            "phase": 0,
            "point_count": 2534
          },
          {
            "center_witness": 0.4707309741211738,
            "diameter": 2.2194987273643156,
            "held": 0.6549415799481877,
            "ordered_inverse_ball": 429448.04619797954,
            "phase": 1.5707963267948966,
            "point_count": 2534
          },
          {
            "center_witness": 0.5974697916097655,
            "diameter": 2.219498727364315,
            "held": 0.6168336320454637,
            "ordered_inverse_ball": 429448.04619797954,
            "phase": 3.141592653589793,
            "point_count": 2534
          }
        ],
        "score": 50.04065154519229,
        "shape_count": 1880,
        "shape_sha256": "b577db5c39d2fcbd727cc5c4f46fa5adb9846b850d70ca8f2eece0459246bea8",
        "solver_status": 3,
        "stage": 15,
        "train": {
          "Killing_op_max": 2996457.413779499,
          "Killing_rms": 32775.29453381792,
          "area_min": 0.000001038209312203329,
          "check_shape": [
            95,
            176
          ],
          "clock_min_sample": 0.5033925043043155,
          "frozen_gram_max": 8.438092175626856,
          "frozen_gram_rms": 0.5583642689989924,
          "max_abs_principal": 29585795382.2134,
          "opposite_witness_to_upper": 0.8035925198331333,
          "origin_radius": 1.2914057840731517,
          "support_min": -0.9363593970690769,
          "upper_height_min": -8.311563731929959e-17
        },
        "transferred_diagnostic_field_sha256": "2eb0a612e97d028e78f962f68b65206abeed8278e7e3dd9071284b415c2bd3cd",
        "volume_moments": {
          "fixed_marker_first_moment_x": -4.1783182292744206e-10,
          "marked_central_second_moment_pi_difference": -8.288574953726026e-11,
          "signed_unmarked_first_moment_x": 0.12277163756170746,
          "signed_unmarked_volume": 2.4755954043543267
        }
      }
    ],
    "status": "completed_full_finite_Killing_Haar_and_two_fixed_refinements"
  },
  "whole_runner_field_files": {
    "complete_inventory": {
      "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/complete-field-file-inventory.json",
      "bytes": 3703,
      "sha256": "f85afdbd40b45208d11184c5f14ae04be57d9f4ae6d66e32d0ea1d1df5560ea7"
    },
    "original_file_count": 18,
    "complete_file_records": [
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/current.npz",
        "bytes": 25606,
        "sha256": "0b22aa404fb51fa6b178d014388267e153052058cdb011aab210c2ee3ea86222"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/frozen-source.npz",
        "bytes": 11886,
        "sha256": "89d69811a64d3b2a7ff560d5d06b8dd59b3ee45403662d6e4bb0dfc3382d81a3"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-00.npz",
        "bytes": 6238,
        "sha256": "ad94fd242ac2c511b755f26b3b5e6826a9b99489984a70ef5224d01c7106b626"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-01.npz",
        "bytes": 6238,
        "sha256": "6f9e120d1ba26ce6d90e54ca5c600483bd704880694ab5145372e5b0395804ee"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-02.npz",
        "bytes": 6238,
        "sha256": "f207066a9894acefeb3cb850daf26b4a6ebc9be6f14346d239eaaaa8b9e626b0"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-03.npz",
        "bytes": 6238,
        "sha256": "3fd5815135e256365645397381116b67b1aa9c1e699c304c917eeae0cbc99133"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-04.npz",
        "bytes": 6238,
        "sha256": "04f1d6d2b0d7c4921683e6411f8f5aeb138b4e75cee7e5d5dea806c152533c79"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-05.npz",
        "bytes": 6238,
        "sha256": "3ba1f2430fa3236ee5a3cfd9d6ef3be22b96be17ea4d0c540eba550274b9992c"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-06.npz",
        "bytes": 6238,
        "sha256": "8d3e64979035ad8e5dd487c65efe3ee8abb0f4c864514f543552af85fa52b5ed"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-07.npz",
        "bytes": 6238,
        "sha256": "402f7e145c6b21ff30d7b4e0a49918fae402520cf7eb463a2fa6ad9a625196df"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-08.npz",
        "bytes": 6238,
        "sha256": "50e520d344febb2edb74a923415b03d120797b3071bd8be69c32e81a2d18e9aa"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-09.npz",
        "bytes": 6238,
        "sha256": "df8f74f12bfc37e4ae29d7a777e30a7d0a9e14353df194af9643a4df4565125d"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-10.npz",
        "bytes": 6238,
        "sha256": "16a112bb702d89acf5b54b378d2a30e7a06767d1ba8e1dcad2355d77ea4bd7e7"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-11.npz",
        "bytes": 11886,
        "sha256": "eed1eac56bbd4815fed432dc07f3c0fed8e80d491d6034e23fdc5e70181137e6"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-12.npz",
        "bytes": 6238,
        "sha256": "218c71b99cccfa6a208a371ee0587bfd84ccfd078127bdd3322b538073bf6c5d"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-13.npz",
        "bytes": 11886,
        "sha256": "89d69811a64d3b2a7ff560d5d06b8dd59b3ee45403662d6e4bb0dfc3382d81a3"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-14.npz",
        "bytes": 15158,
        "sha256": "be3348eef87731d3939a067898ed71a10a7f1bfcdddc1fb57833b0db9a62d2d2"
      },
      {
        "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/field/stage-15.npz",
        "bytes": 25606,
        "sha256": "e44566d57fa438a23bb76704aadb3fe6422f31fa7a1223cb412c3f0187818901"
      }
    ],
    "best_field_records": []
  },
  "stdout_stderr": {
    "path": "/home/runner/work/_temp/run38-bent-disk-killing-46145189191-1/complete-scientific-stdout-stderr.log",
    "bytes": 3489,
    "sha256": "c0af77de7d3ea5aad9a209d08e5e028ed7eaa712b3537d94a9a19930779bdbba"
  }
}
```


原索引/分卷已逐字核取；以下 whole-file 固定身份保全部原字段与失败/未知，不复制科学raw，不把统计进度当完整报告。

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/notes/run38-bent-disk-killing-46145189191-1.json",
    "bytes": 79140,
    "sha256": "d2cb112cb9cbebb42296e21c01c93765e8af130354ed7a372038edac648dee9f",
    "git_blob_sha": "ab199e8b47714f681b0b3bfad5a965061f8e412b",
    "fixed_commit": "0d1e56320416c0655ca3989fc26f4a3c400a4fb5",
    "scope": "Complete immutable original file; every command, input/output identity, returned value, missing field and error is preserved at this exact commit."
  }
]
```
