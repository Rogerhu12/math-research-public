# Run41：延迟转弯固定初g、空间中央和双独立fan帽的真实全相位求解

会话 Astra-larger-e4e2a2bf-20261126。六件完整入口、物理场、参数、workflow、request、delivery已全文读取并同次入main。**实际run/job/点/度量费用此刻尚未知；课题未完成。**

## 固定目标与实际自由

本任务使用[R752新完整初度量](../results/R752-cap-shortcut-and-delayed-turn-central-chord-compatibility.md)：Y=.37、额外低角肩长.81、角度1/1024。它与40的旧初g不同，是独立新输入；本任务所有设计和后续三层都保持同一个新初g、同一个完整材料球和全相位0…π/2。R753已证明全部允许中央幅度|a|≤2^-21的所有中央点对均通过原闭面任意路径距离必要条件，不能把该条件冒称全端填充。

[R753真实物理接口](../results/R753-spatial-rectifying-cylinder-and-independent-ruled-cap-fans.md)给一条可动闭空间rectifying中央柱、两个完整独立直纹fan端帽；三块各自对初g精确等距。每个正时间结实际联合优化19个边界形状/位姿坐标：1中央控制，双帽各3纬度控制与6刚体位姿；另有两个完整圆端的三分量场。帽中正cubic项保证最终真实非C³法向germ，但只有实际整像嵌入等条件另付后才能推正商距。较大优化control不自动承继命名微量场的厚度界。

圆端包含真实v和逆原v0两套严格嵌套径向多项式、完整角向Fourier及真实切向量列、两端各v^(5/2) C²项；所有物理分量保留。逐层凭完整字典名把原系数精确直拷，新列零，不用近似投影偷换旧解空间。全部四接缝六jet残差和各图的正式R753六jet直接比较均由原任务返回。中央/两个帽面没有因求解只覆盖端部而从全闭检查中排除。

## 原完整任务与预算

原五设计 legacy-free-pose、omega-free-pose、plateau-free-pose、omega-shortened-cap、plateau-shortened-cap 全跑各2个正时间结；据原完整评分选支后依次4/8/16个正时间结，全部进行独立空间与时间检查。自然三次样条定义整个时间区间的物理系数，不以端点或Lie估计代全时。最细独立65时间样本，另有七个完整像/体矩相位；所有独立检查仍是有限工作值，不是区间证书。

以下为原参数完整全文（与实际冻结参数文件逐字一致）：

```json
{
  "schema": "delayed-hard-central-disk-roll/v1",
  "source_sha256": {
    "r748_developable_axial_caps.py": "947245856229ddeb95b83c763403e86bdd867c63b63b6013929d2e2a13a87b46",
    "r747_offset_arclength_closed_two_jets.py": "09b29cd06eec6887bf8f103f104cdd9ca598b691c3e7503fa2220dbafc71e3ac",
    "r746_axial_translation_closed_two_jets.py": "e5ab4d4a0921cb83c7eefc485147883d6dcea92ff9df6f3f3da8604440f174ef",
    "r744_extruded_closed_two_jets.py": "35bb8a1612dd22a8e215a7682ead0c9836b26f3a6c6b525a876fff178a3d6c24",
    "r742_tilted_disk_two_jets.py": "5088d1e5183b91f78d8fd1af056bd774ce6ef54b5c578277c3dc7ef04fe183bd",
    "r740_rolled_disk_seed.py": "b812afa381e2775433710edb9cfa9bd54f0b1b892935c21f2f785675bb4d866f",
    "bent_end_phase_fields.py": "5305a955f3f5a0f37a3097388b025889584ce2033fe82bcab0140ab8330b31ba",
    "bent_body_atlas.py": "873bcabafc61a7223736d7806201e289349f838359e59c539f27fafc066ad102",
    "r753_rectifying_cylinder_and_cap_fans.py": "8115dea654acb925db30357e675db07879dcedfecfe3c4f4fb0c5d0539217a81",
    "r752_delayed_turn_closed_two_jets.py": "762717cc9bd895893b9538683a588217d2f8fc4f236f997a3120880acbe161c6",
    "bent_end_phase.py": "0b2ce5d260bdc4160b972d7b36cc0567660c6bbc18d56eb722265e6f0b04b701",
    "bent_hard_end_fields.py": "af0422bc6ed3e8823594b955550ef980c665d1b24e5330a46a595c19c5b333ba"
  },
  "designs": [
    {
      "id": "legacy-free-pose",
      "method": "legacy",
      "middle": 0,
      "upper_cubic": 0.000001,
      "lower_cubic": 0,
      "cap_y": 0
    },
    {
      "id": "omega-free-pose",
      "method": "arc",
      "middle": 0,
      "upper_cubic": 0.000001,
      "lower_cubic": 0,
      "cap_y": 0
    },
    {
      "id": "plateau-free-pose",
      "method": "plateau",
      "middle": 0,
      "upper_cubic": 0.000001,
      "lower_cubic": 0,
      "cap_y": 0
    },
    {
      "id": "omega-shortened-cap",
      "method": "arc",
      "middle": 5.960464477539063e-8,
      "upper_cubic": 0.006,
      "lower_cubic": 0.003,
      "cap_y": -0.15
    },
    {
      "id": "plateau-shortened-cap",
      "method": "plateau",
      "middle": -5.960464477539063e-8,
      "upper_cubic": 0.008,
      "lower_cubic": -0.005,
      "cap_y": -0.22
    }
  ],
  "metric_loss_scale": 1.5,
  "curvature_cap": 9.5,
  "bend_weight": 0.9,
  "support_goal": 0.103,
  "support_weight": 8,
  "normal_displace_goal": 0.15,
  "normal_displace_weight": 1.5,
  "travel_goal": 0.55,
  "travel_weight": 0.6,
  "jacobian_probe": 5e-8,
  "dense_jacobian_entries": 32000000,
  "coarse": {
    "id": "all-five-coarse",
    "roll_modes": 3,
    "intervals": 2,
    "mesh": [
      27,
      11,
      8,
      7
    ],
    "check": [
      69,
      21,
      15,
      13
    ],
    "max_nfev": 52,
    "inner": 85,
    "regularizer": 0.000007,
    "extra_check": false,
    "radial_degree": 2,
    "turn_degree": 2
  },
  "refinements": [
    {
      "id": "fixed-target-space-time-1",
      "roll_modes": 5,
      "intervals": 4,
      "mesh": [
        35,
        13,
        10,
        9
      ],
      "check": [
        77,
        25,
        17,
        15
      ],
      "max_nfev": 60,
      "inner": 95,
      "regularizer": 0.000004,
      "extra_check": true,
      "radial_degree": 4,
      "turn_degree": 3
    },
    {
      "id": "fixed-target-space-time-2",
      "roll_modes": 7,
      "intervals": 8,
      "mesh": [
        49,
        17,
        12,
        11
      ],
      "check": [
        103,
        33,
        21,
        19
      ],
      "max_nfev": 68,
      "inner": 105,
      "regularizer": 0.000002,
      "extra_check": true,
      "radial_degree": 6,
      "turn_degree": 5
    },
    {
      "id": "fixed-target-space-time-3",
      "roll_modes": 9,
      "intervals": 16,
      "mesh": [
        65,
        21,
        16,
        14
      ],
      "check": [
        127,
        41,
        27,
        23
      ],
      "max_nfev": 76,
      "inner": 125,
      "regularizer": 0.000001,
      "extra_check": true,
      "radial_degree": 9,
      "turn_degree": 7
    }
  ],
  "cloud_grid": [
    27,
    9,
    5,
    5
  ],
  "moment_grid": [
    125,
    33,
    25,
    19
  ],
  "geometry_phases": [
    0,
    0.2617993877991494,
    0.5235987755982988,
    0.7853981633974483,
    1.0471975511965976,
    1.3089969389957472,
    1.5707963267948966
  ],
  "immersion_weight": 4,
  "minimum_eigenvalue": 0.73,
  "hard_parameter_difference": 0.00004,
  "geometry_source": "r753_rectifying_cylinder_and_cap_fans.py",
  "target": "One exact initial phase-zero R752 delayed-turn metric, both finite material ends and all t, Y=.37/extra=.81/small angle=1/1024, independently from run40."
}
```

公开ubuntu-latest、4 vCPU/16GB、Python3.12.14、numpy2.3.5/scipy1.17.0、BLAS各单线程。原workflow总360分钟；未加科学子任务墙钟截断。主入口先设兄弟真实几何目录再import，按正式CLI直接运行，不依赖40返回或重放旧点。

```sh
python -u topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_hard_end_phase.py --params topics/visible-flex-larger-amplitude/computations/bent-hard-end-phase-design-v1.json --geometry-source topics/visible-flex-larger-amplitude/scripts/resume_20261126/r753_rectifying_cylinder_and_cap_fans.py --out "$RUNNER_TEMP/run41-field"
```

原完整observer每8秒观察、120秒发布、最多2700秒真pull/rebase比较双README；源由触发提交固定独立科学worktree。NFF立即真pull/rebase重推，失败/未返原样记录。完整NPZ仅runner，报告完整字节数、float64系数矩阵/时间/各结SHA与文件SHA，不上传raw；全部实际小报告单独入notes并记HANDOFF。

## 新刊六件与冻结原来源

|新文件|bytes|SHA256|Git blob|
|---|---:|---|---|
|topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_hard_end_phase.py|14837|0dc5bab5445f2a0eb0cfe1387c2accd42bdf5a9d99396f4b6421384cf786ab97|1b8d69a94c80aac6a989f942b755e6370aa4d1a2|
|topics/visible-flex-larger-amplitude/scripts/resume_20261128/bent_hard_end_fields.py|10678|af0422bc6ed3e8823594b955550ef980c665d1b24e5330a46a595c19c5b333ba|125e94b27ac85f964318e0280a84f4d1fd428514|
|topics/visible-flex-larger-amplitude/computations/bent-hard-end-phase-design-v1.json|4685|836cb24a757f7d4b494dd65f9358b916713da3e30c9efbc394d9e96f504a8aac|c4e067979b28a6bbbbfec52f38260b3e83fe6c06|
|.github/workflows/visible-larger-run41-bent-end-fan.yml|3871|e2acde78f982b781544dfd0627a9f17cbd7d0ff36f9721598b16ead41ed2573d|230b11ab47d4bb29af13e1ca00fbe66b7b2606bc|
|topics/visible-flex-larger-amplitude/computations/run41-bent-end-fan-request.json|18364|d57b3512f7ac2d6c58a49409e702ef1fc53eb2e46afb1bc2304697bc996d6549|0012caaefde888f2ce874cc180042f5090cbe792|
|topics/visible-flex-larger-amplitude/computations/run41-complete-bent-end-fan-source-and-launch-delivery.json|23064|5f6cf90c2844c36ad4055c50586dd02a5a2d350eedf708d5d4f7c555b45e7281|6bcecea3b894a0c9c2190210d8867e28c202d924|

14科学输入的完整身份均在[request](../computations/run41-bent-end-fan-request.json)及[delivery](../computations/run41-complete-bent-end-fan-source-and-launch-delivery.json)，其中新三件和11个完整parent；科学程序核对12 import实际字节SHA。原控制observer14863B/c47dde7a91a32216afdb5f41ef2952fa3cb4b22c、run36控制18649B/67d3e096ab4a6417860d8aa1a413984002bc4523不变。

## 未付标准

实际同g相对算子峰≤1e−6、同参数连续收敛、整个时间/空间嵌入与reach、完整D/握持/held/含反射商距及多张全闭mesh均须由这一真实分支自身支付。参考几何或有限粗样本不代成品。40、33–35保持原预算并行，本任务不取消旧活求解。
