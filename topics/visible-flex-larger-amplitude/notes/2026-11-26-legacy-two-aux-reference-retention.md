# 第22次容量操作：两份旧辅助线性参考的逐胞数组

2026-11-26，Astra-larger-e4e2a2bf-20261126。主会话在同一普通提交移出以下两件原raw并保全部恢复资料；几何子代理只准备小记录，没有改引用。全程未运行科学计算。

## 1. 准确范围与可释放容量

依根 README 第15条和前21次 raw 保留记录，仅从当前树普通移出下列两份旧可重算输出，共 **1,133,547 B**。每份生成器的唯一大数组是 `cell_rows`，胞号为12至224；保留记录复制全部其他字段，包括所有原有理外包界、公式、八输入 SHA、源码 SHA、时间、限制及原资源记录。没有把仅有表格或参数的未知 JSON 当成 raw。

| 原相对路径 | 字节数 | SHA256 | Git blob |
|---|---:|---|---|
| `notes/2026-11-12-closure-variable-reference-farball.json` | 566768 | `592f43f17fb6c05fe32e4e6c3acda00e7c0b3d18fc8c4393d2d9f981034937ad` | `993e9ce14b49c8c909eb5b10f797f7bbd956a1ff` |
| `notes/2026-11-12-closure-wide12-reference.json` | 566779 | `3574206df53b69b41876ca07950a5d6cd3d2f98203c5591875d9b87e0a499dd5` | `edb40535935fb603d347a3bea0a520fcc9c6162f` |

两份原输出的固定恢复提交均为 `a93699427718235cb07d70c8f0971e5981dbfbe1`。本次已用 Git 树元数据核对该提交的路径、blob、字节数与工作树大小。variable 参考的 SHA 复制自仍保留的 `closure-anisotropic-low46-box.json` 尾部 `input_hashes`；wide12 的 SHA 来自完整小清单 `notes/2026-11-12-closure-strip-reweight-stable-manifest.json`。本次没有为摘要而整读任何大报告。

对应完整紧凑对象为 `computations/resume-20261126-legacy-two-aux-reference-retention.json`。本次把该文件与本说明加入当前树，并由主会话普通删除上述两件 raw；不重写历史，不压缩编码另塞，不移动到 release 或另一仓库。

## 2. 已有结论照保

variable 与 wide12 都记录：原真实线性参考在远端的完整46参数校正球门、R23小球门通过；校正球半径 `1/500` 是条件域，不能冒已经构造了完整频率非线性校正。原远端角宽为38、目标为 `2^-2200`；原参考只有所登记的8个非零浅端高度，全部46个可能的低深参数仍进入最坏模转换。两件的完整有理界均逐字段保留，未取显示约数重算。

两者区别也原样保留：variable 使用 `tau_n = 1 + (n-12) log(2)/4`；wide12 只在首胞取 `tau_12=2`，其余胞使用原公式。不能把宽首胞的条件参考表当成后续 Green 充分主界已成功：旧 `closure-strip-reweight-stable-manifest.json` 明记 isolated-wide12 充分主界失败。R34、R35、R36 与 strip-reweight 笔记完整保留；不新增数学结果，不把旧辅助低46结论转移到当前 SO3/normal/supported-seed 场。

## 3. 全部源码与直接输入

以下完整源码继续留在当前树。三件原报告登记源均与当前字节 SHA 相等；Green 模块实际导入的 `closure_projective_interval_column.py` 也明确保留，未用接口占位。第六件是原资源包装器，不改变科学算法。

| 完整相对源码 | 字节数 | SHA256 |
|---|---:|---|
| `computations/closure_far_ball_and_variable_reference.py` | 6758 | `a14800e650f5a7780e415edaa84ee675b3ed80a7d88fa055d7b790bed74a7ae8` |
| `computations/closure_wide12_reference.py` | 6879 | `1168c10e23304b85563de9830867f4dc02a4ccbbec6ecdeae25d54977f08e3ee` |
| `computations/closure_real_head_green_enclosure.py` | 11896 | `4b2e74d07f678e11631c51cf01831a4c1e588e8d207c144e2f1dace8413022e0` |
| `computations/closure_real_head_source_enclosure.py` | 20321 | `97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47` |
| `computations/closure_projective_interval_column.py` | 3594 | `45997a1d5be6326a1ebbe85ac4240ea7d9dde1c2fb6acdf832460dade89e4f97` |
| `computations/strong_resource_run.py` | 1658 | `bbf6c8ac8cb32cbc0f5c1e1c1c1e110ca1744c7839de0f272c172837a4ba3f59` |

两份输入集合逐键相同：原 `closure-real-linear-q003-low46-recovered.json.gz`、原 `closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json`，以及全部6个01–46列组。全部路径、SHA256、原字节数、Git blob、恢复提交已从第12次保留记录的 `verified_inputs` 完整复制，并与这两份尾部 `input_hashes` 逐值比较相等。该已有核验清单是 `computations/resume-20261126-legacy-plateau2-reference-retention.json`；原8件的固定恢复提交均为 `8ef38046e8b04adc6da1093c0730e1fc8747c2c9`。

本次没有重新下载或整读这些已移出的列数组，不冒称新做了其逐字核验；准确证据是现有公开第12次核验清单。全部原参数已在其原 ready 中；未把参数缩写成摘要。以后需要复算时，在公开 Actions 隔离 scratch 恢复上述原字节及相对路径；`load_json` 对原 `.gz` 字节做 SHA，解压仅用于 JSON 读取，不能用重新压缩后的不同字节冒原输入。

## 4. 原完整命令及准确默认参数

下面是原资源记录的完整 argv，只把排版转换为 shell；原解释器路径是历史事实，不声称当前存在。记录没有 Python/python-flint 版本，不补造。原资源 JSON 本身继续保留。

### `notes/2026-11-12-closure-variable-reference-farball.json`

```sh
/workspace/scratch/c0de65fac774/research-venv/bin/python \
  computations/closure_far_ball_and_variable_reference.py \
  --columns \
  notes/2026-11-12-closure-real-linear-q003-low46-recovered.json.gz \
  --ready \
  notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --out \
  notes/2026-11-12-closure-variable-reference-farball.json
```

原 resource：`notes/2026-11-12-closure-variable-reference-farball-resource.json`；exitcode `0`、wall `2.394235610961914` 秒、峰 RSS `82556` KiB。这是旧本地资源记录，未登记旧 Actions run，不虚构 run 编号。

### `notes/2026-11-12-closure-wide12-reference.json`

```sh
/workspace/scratch/c0de65fac774/research-venv/bin/python \
  computations/closure_wide12_reference.py \
  --columns \
  notes/2026-11-12-closure-real-linear-q003-low46-recovered.json.gz \
  --ready \
  notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --out \
  notes/2026-11-12-closure-wide12-reference.json
```

原 resource：`notes/2026-11-12-closure-wide12-reference-resource.json`；exitcode `0`、wall `2.26031494140625` 秒、峰 RSS `85320` KiB。这是旧本地资源记录，未登记旧 Actions run，不虚构 run 编号。

原完整生成器默认值且未被原 argv 覆盖的参数是：`--relative-radius 1/500 --far-strip 38 --far-log2-ball -2200 --precision 192`。全部46 modes及213胞由完整源核验，没有额外省略尾段开关。将来确需重新计算，只在公开 Actions 独立 scratch 执行；所有新 raw 留 runner，发布紧凑真实结果。浮点/Arb版本、计时及资源数据会使重新生成的字节不同，所以恢复原字节与重新计算明确分开。

## 5. 原字节恢复与旧消费者

```sh
git show a93699427718235cb07d70c8f0971e5981dbfbe1:topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-variable-reference-farball.json > /tmp/legacy-variable-reference.json
git show a93699427718235cb07d70c8f0971e5981dbfbe1:topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-wide12-reference.json > /tmp/legacy-wide12-reference.json
sha256sum /tmp/legacy-variable-reference.json /tmp/legacy-wide12-reference.json
```

旧 variable Green、anisotropic 盒、nonlinear-low-far 消费者，以及 wide12 Green 仍有这些路径引用；完整列表在 JSON 的 `historical_textual_references_preserved`。这次不修改其源码、resource 或历史文字，也不谎称所有旧消费者都没有引用。若它们需要 `cell_rows`，必须先恢复原完整字节并将隔离 scratch 布局保持为原相对 `notes/`/`computations/`；紧凑对象不能代替完整输入，尤其 Green 验证以相对路径作身份键。

本次针对课题文本的路径搜索只发现上述旧记录/旧证明，没有在当前执行脚本、当前输入队列或新入口参数里发现直接引用；主会话保留实际活跃队列和 runner 数据。当前05的全部永久位置、完整源、冻结参数、新场输入及待返结果均不在移出清单中。

## 6. 本次核查边界

对两件大报告各仅读取首12000和末12000字节，按完整源的 `result` 字典顺序提取 `cell_rows` 之前、`input_hashes` 之后的所有字段。没有整读或解析逐胞数组，也没有重新发布它们；首尾截段偶含首末行片段，保留对象仅提取其前后的元数据。其他读取均是完整小源码/小清单/小资源记录，做的是文本、JSON语法、SHA及Git树元数据检查；没有 import flint、数值积分、重新计算区间或重证旧结论。

主会话另实际核对两件原文件各首末12000字节：全部25个非cell_rows字段与小对象逐值相同；六份完整小源SHA及八件原输入恢复清单亦相同。删除前再次按当前HEAD与固定恢复commit的路径/blob/字节数守卫，不读取逐胞数组。
