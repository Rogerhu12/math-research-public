# R136 准确物理 profile 的闭包与接入

完整数学定义、Taylor 余项、共享两 jet、当前 C4 bumps、单侧三导、准确 cut 和删柱平移的证明已登记为 [R171](../results/R171-accurate-radial-profile-and-one-sided-Arb-jets.md)。本文件给出实际文件及最短消费路径。没有执行 F/J、BVP、frame 或 body。

## 1. 已闭实际对象

生成器 `scripts/fd2d-metric-r136-profile-packet.py` 使用最新不可变第 27 轮 accepted 数组：

```
notes/2026-11-12-fd2d-raw-bump-grouped27-trial-back00-a01-accepted.npz
SHA256 2b65810c5c09985d54544e6ca697ee609f066a17ecbce4b83e89adad0b52ae6f
```

参数布局逐键读取为中央 31、尾 16、径向 7，总计 54；网格 131 节点。目标基准为候选 `7c3f31de…888bfd1`。七个实际径向参数分别为

```
[-0.0012866756042280987,
 -0.012106596139651038,
 -0.01782976399578991,
 -0.01829985883174857,
  0.013983173056804694,
  0.030146008628793613,
  0.013044667972955068]
```

显示小数只便于定位；准确值为 NPZ 中原 binary64 字节，包内同时保存有理分子分母。输入文件字节未改。

真实执行命令：

```bash
python scripts/fd2d-metric-r136-profile-packet.py \
  --field notes/2026-11-12-fd2d-raw-bump-grouped27-trial-back00-a01-accepted.npz \
  --out-prefix notes/2026-11-12-fd2d-metric-r136-arb-profile-01 \
  --precision 256 --order 24
```

进程 `87589`，初 chunk `3ee9be`，完成 chunk `f951e0`，真实退出 0。已存在的闭输出不得覆盖；需要重做时另给输出 stem。

## 2. 不重算即可读取

在本题目录执行，或自行把本题 `scripts` 加入 Python 搜索路径：

```python
from fractions import Fraction
import sys
sys.path.insert(0, "scripts")
from fd2d_gc_r136_arb_profile import R136ArbProfile
from fd2d_gc_current_native_interval import ProfileBox

target = R136ArbProfile.from_packet(
    "notes/2026-11-12-fd2d-metric-r136-arb-profile-01-packet.json.gz",
    expected_sha256="7bedd394db9ab0fc3b1d3186c49225ae8f7765ca6d28a80560aeb8842a26ee7c",
)
box = target.physical_box(Fraction(3,5), Fraction(61,100))
radial = ProfileBox(box["a"], box["a_s"], box["a_ss"], box["a_sss"])
cut = target.endpoint_jets()
shorter = target.shifted(Fraction(7,50))
shorter_cut = shorter.endpoint_jets()
```

`physical_box` 的物理端点是准确有理输入；如果传入 Python float，则明确解释为那个 float 的准确 dyadic 数。`piece_box(i,t0,t1)` 用准确物理片的归一参数查询。`interface_jets(i)` 同时返回左右片 jet；不会暗选不同的浮点分片。

接口均返回 Arb 球，适合直接参与后续区间运算。所有数学输入及分段多项式/原函数系数已在 packet 中保存，读包不再次求相位积分或 BVP。文件末尾的 `input_binding_sha256` 为

```
174ce735894c493f545295fe9f32c25de8b5e8aced2b4142df8e92fa08462794
```

读取时需提供闭包 SHA，校验源及精度、输入和确切参数；不能拿另一输入的包换名消费。`from_packet` 不用原绝对路径重新读取源数组。manifest 同时保留生成输入身份以便重做。

## 3. 连续信息与有限比较分开

[完整报告](2026-11-12-fd2d-metric-r136-arb-profile-01-report.json) 中：

- `piece_rows` 和 `continuous_whole_profile_ranges` 是全部准确片的连续外包。宽盒导数外包较松，不能当作实际极值。
- `one_sided_interfaces` 保存 60 个共享两 jet 恒等及两侧第三导；没有全局三导相等要求。
- `accurate_cut` 是准确半径 cut；`R155_second_form_radial_jet_inferred=false`。
- `finite_same_point_runtime_error_maxima` 仅比较保存网格前 130 点的旧数值输出。
- `last_saved_endpoint_label_comparison` 明示末点不是与准确 cut 相同的物理坐标；没有重新定义有限场或延拓它。
- `runtime_scope` 明示本链无 profile ODE/dense 插值；旧半径来自 40 点浮点 Gauss，旧导数是独立的解析公式求值。
- `exact_cylinder_shift` 是父物理 profile 的准确限制/平移；父准确 cut 标签继承。
- `whole_surface_certificate=false`。

准确总长区间宽小于 `2.617e-31`，比旧保存 endpoint label 大约 `1.1873403225247745e-15`。本包支付准确标量目标；它不自动把原 P1 场的最后一小段、atlas 或旧浮点 body 结果搬到该准确端点。后续有限曲面定义应明示这项极小端点衔接，再用同一后验消费。

## 4. 文件、证明与依赖

闭存清单为 [closed manifest](2026-11-12-fd2d-metric-r136-arb-profile-closed-manifest-01.json)。运行使用 python-flint 0.9.0、NumPy 2.3.5、SciPy 1.17.0；其中 SciPy 只用于捕获既有 Candidate 数值输出，不用于区间判定。

准确数学依赖是 R136 原始候选、已发布 a0 矩包、半径 v2 证书及保存七个物理 δ 的输入字节。原 `fd2d_frozen_ellipse_candidate.py` 和 `fd2d_gc_radial_bump_profile.py` 的身份也列入 manifest，用于再现有限 runtime 比较。

本轮没有修改原 target、旧 reader、已有场、R165 积分规则或运行中的数值求解器。按 root 的本轮明确授权，仅在结果索引追加 R171 条目；其他公共状态由 root 维护。完整 affine/reference/atlas 连续消费者及 R119/R125 的全场余项仍单独支付；这里已提供其中准确一维 `ProfileBox` 的实算来源。
