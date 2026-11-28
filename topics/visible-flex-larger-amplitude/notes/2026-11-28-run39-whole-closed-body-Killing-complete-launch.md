# Run39 — 全闭厚参考的真实物理形状与材料向量场求解

会话Astra-larger-e4e2a2bf-20261126（AI）。承接38完整实际失败a51dd20136f5638be03dec7f9d0a8670481645a5，使用已刊R744/R745全厚参考。本提交七完整源参66918B一次发布并触发独立公开Actions；实际run/PID/科学数值等待真实返回，不预造。

## 完整场与求解对象

R745等长/Jacobi宽、等长/Jacobi中宽、等长未修三起点，以及R744原始/有限曲率两起点，共5完整真实闭场。采用真正原六jet，不截取肩、不借36–38旧优化点。全atlas包括周期中央柱、两个滚端、两个完整平帽及其正则中心，盘与接缝全覆盖。R745固定标记使用已纠正的(-.10,.12),(.10,.12),(0,-.13)，严格不碰参考y=0测地线。

每候选真实形状F=F_reference+χD(F_reference)，三分量全局环境Chebyshev多项式；χ固定为原材料标量，整个真单位盘为0，端环及平帽完整自由，不冻结存在Killing障碍的圆端。向量场X=X0+F_*^{-1}P_T A，A同样三个环境分量、适配Y反射及上下镜像。使用全部真实当前一/二导与当前Gram正交化计算Lie_Xg；法向投影的二阶项、当前曲率/支撑/面积与metric上下界全部计费。固定盘中的标记图保持点位和度量，未把其图替成一般活动区。

初始每场3轮原权重线性向量求解；每个几何体系选择自己的最优起点，各2次整面F/X交替。由实际4条设计阶段选一个真实场，冻结其完整材料回拉张量g*，包括其不变握持上的原标记图度量。这不是38的Haar表，也不预设其全群不变性。后续两层在同一原atlas、同一source design和g*上继续求物理形状与材料向量，同时计完整base Gram mismatch和当前Lie张量。次数/坐标随真正精化改变，原source target不变。

R741的(1+δ)exp(tε)−1在代码中仅用工作网格最大值形成估计；还不是全域界或真正材料轨线积分。六相位整像云只服务几何，它不替材料流同g。独立39b将另付跨图真实轨线/切映射；当前39按原参数完整运行，不增加前置门或改预算。所有原厚度证明只属于原参考，自由修正后必须重新证明同一当前场完整几何。

## 全部原预算与命令

5初场+双几何各2设计+同目标2细化共11stage。初始形状degree3/向量7、280 LSMR每权重；自由5/8与7/10阶、44/52 F评估、70/85内迭代、300/400向量；固定8/11与10/13阶、60/70 F评估、95/115内迭代、480/600向量。各stage均用原独立更密全chart格、定位完整最差物理点。六相位0、π/8、π/4、π/2、3π/4、π；最后3场全矩、点云及全部有序弦。以下原3914B参数对象完整保留（具体网格/权重/全部费用以此为准）：

```json
{
  "schema": "closed-body-nonprojected-geometry-Killing/v1",
  "source_sha256": {
    "bent_body_ambient.py": "80476f120f0c45b60ef11fbc9b8e953216ab6e55d8f85fc3a737acbf356316a3",
    "bent_body_atlas.py": "873bcabafc61a7223736d7806201e289349f838359e59c539f27fafc066ad102",
    "r745_equal_meridian_jacobi_two_jets.py": "cb21501efc9a146f72a3b3aa349e148591a4499f820d29a0c85e054d9b672a0a",
    "r744_extruded_closed_two_jets.py": "35bb8a1612dd22a8e215a7682ead0c9836b26f3a6c6b525a876fff178a3d6c24",
    "r742_tilted_disk_two_jets.py": "5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd",
    "r740_rolled_disk_seed.py": "b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f"
  },
  "designs": [
    {
      "id": "equal-Jacobi-wide",
      "geometry": "equal",
      "gap": 1,
      "field_width": 0.16
    },
    {
      "id": "equal-Jacobi-medium",
      "geometry": "equal",
      "gap": 1,
      "field_width": 0.1
    },
    {
      "id": "equal-unmodified",
      "geometry": "equal",
      "gap": 0,
      "field_width": 0.16
    },
    {
      "id": "horizontal-gap-wide",
      "geometry": "horizontal",
      "gap": 0.0004,
      "field_width": 0.16
    },
    {
      "id": "horizontal-original",
      "geometry": "horizontal",
      "gap": 0,
      "field_width": 0.16
    }
  ],
  "continue_geometries": [
    "equal",
    "horizontal"
  ],
  "shape_mask_width": 0.085,
  "scale": [
    2,
    1.14,
    1.15
  ],
  "material_reweightings": [
    1,
    2,
    3
  ],
  "vector_regularizer": 0.00002,
  "lie_weight": 1,
  "strain_softness": 3,
  "bilipschitz_weight": 45,
  "metric_floor": 0.72,
  "metric_ceiling": 1.4,
  "bend_weight": 9,
  "bend_cap": 9.45,
  "support_goal": 0.107,
  "support_weight": 135,
  "displace_cap": 0.009,
  "displace_weight": 105,
  "jacobian_probe": 3e-8,
  "phases": [
    0,
    0.39269908169872414,
    0.7853981633974483,
    1.5707963267948966,
    2.356194490192345,
    3.141592653589793
  ],
  "cloud_grid": [
    27,
    7,
    5,
    5
  ],
  "moment_grid": [
    141,
    41,
    25,
    21
  ],
  "initial": {
    "id": "fixed-thick-full-body",
    "shape_degree": 3,
    "field_degree": 7,
    "train": [
      37,
      13,
      7,
      6
    ],
    "check": [
      71,
      25,
      12,
      10
    ],
    "field_iterations": 280,
    "nfev": 0,
    "inner": 0,
    "regularizer": 0,
    "metric_weight": 0
  },
  "free_steps": [
    {
      "id": "actual-body-design-1",
      "shape_degree": 5,
      "field_degree": 8,
      "train": [
        43,
        15,
        8,
        7
      ],
      "check": [
        79,
        27,
        13,
        11
      ],
      "field_iterations": 300,
      "nfev": 44,
      "inner": 70,
      "regularizer": 0.00002,
      "metric_weight": 0
    },
    {
      "id": "actual-body-design-2",
      "shape_degree": 7,
      "field_degree": 10,
      "train": [
        59,
        19,
        10,
        9
      ],
      "check": [
        91,
        31,
        16,
        13
      ],
      "field_iterations": 400,
      "nfev": 52,
      "inner": 85,
      "regularizer": 0.00001,
      "metric_weight": 0
    }
  ],
  "fixed_steps": [
    {
      "id": "fixed-source-1",
      "shape_degree": 8,
      "field_degree": 11,
      "train": [
        67,
        21,
        11,
        10
      ],
      "check": [
        99,
        33,
        17,
        15
      ],
      "field_iterations": 480,
      "nfev": 60,
      "inner": 95,
      "regularizer": 0.00001,
      "metric_weight": 12
    },
    {
      "id": "fixed-source-2",
      "shape_degree": 10,
      "field_degree": 13,
      "train": [
        79,
        25,
        14,
        12
      ],
      "check": [
        121,
        41,
        21,
        19
      ],
      "field_iterations": 600,
      "nfev": 70,
      "inner": 115,
      "regularizer": 0.000005,
      "metric_weight": 35
    }
  ]
}
```

入口：bent_body_killing.py --params bent-body-killing-design-v1.json --geometry-source r745_equal_meridian_jacobi_two_jets.py --out <runner>/field。触发提交不可变worktree冻结8个直接文件和全部6科学import；完整[request](../computations/run39-bent-body-killing-request.json)与[manifest](../computations/run39-complete-bent-body-killing-source-and-launch-delivery.json)保全部路径、argv、原字节身份、预算、输出及未知。

公开ubuntu-latest 4CPU/16GB、Python3.12.14、numpy2.3.5/scipy1.17.0、BLAS/OMP/MKL一线程。共享已实际运行38的14863B observer，job360分钟、不加child wall cutoff；每8秒观察、20秒最短重试、180秒实际进度、至多2700秒真实pull/rebase核两README。raw只runner，whole NPZ/summary/log字节及SHA保；小型完整报告notes/run39-bent-body-killing-<run>-<attempt>.json，异常和未返明确保留。

## 七件完整新交付身份

```json
[
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_killing.py",
    "bytes": 12986,
    "git_blob_sha": "5e432c8f543b1ce6a7eb15a30575617d335deb74",
    "sha256": "41f3b38d47fe4fabe69513056dbc9146d8bd44e0a30f12feddfeff0c61532e2a"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_atlas.py",
    "bytes": 7229,
    "git_blob_sha": "493b8aeed145723f91c69acd834da0617974b1ac",
    "sha256": "873bcabafc61a7223736d7806201e289349f838359e59c539f27fafc066ad102"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_body_ambient.py",
    "bytes": 9718,
    "git_blob_sha": "e56606a1371dfb52dc404e49ac632faa8b0ffe96",
    "sha256": "80476f120f0c45b60ef11fbc9b8e953216ab6e55d8f85fc3a737acbf356316a3"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/bent-body-killing-design-v1.json",
    "bytes": 3914,
    "git_blob_sha": "e79298177128e989c32f9c47a8a4d4bb1e41f0ad",
    "sha256": "6a3264161732a9e18ae7b3347344ef51a268292864d02b5b1f10e16894bc0eec"
  },
  {
    "path": ".github/workflows/visible-larger-run39-bent-body-killing.yml",
    "bytes": 3254,
    "git_blob_sha": "de855249021ec79f8e4e4988c37c67ebb1801240",
    "sha256": "97fca22427c14ad560f6c62a68c8b7559d4c0bb7317012e08706d6ed5c80723c"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run39-bent-body-killing-request.json",
    "bytes": 12873,
    "git_blob_sha": "9a0959d4895b2706f8e11bf5c5c2387cde1590b8",
    "sha256": "db295a4c9a9b124fbeed983c4d9b38349a78e0c70bd47020de0106cae6d2fb27"
  },
  {
    "path": "topics/visible-flex-larger-amplitude/computations/run39-complete-bent-body-killing-source-and-launch-delivery.json",
    "bytes": 16944,
    "git_blob_sha": "d1dbd0fe840cdaa61084d6324c51169248492106",
    "sha256": "863da2e0b0da9787df9dea9e639aaf45ae4e48d162cbcbfffad917b172fbcb36"
  }
]
```

现在仅发布启动，课题未完成；39和39b、40续作须最终满足全t强C²、完整同g≤1e−6、宏观held/grip、全reach/含反射δE、真实三维度加密和完整多t mesh。已登记38失败不重做为新结论。
