# 有限 m=2 前缀与真实非线性尾的首个联立种子

会话：`true_a_analysis`。本包冻结 q=0.0002、M=8、tail depth=8 的已完成计算。继续增幅的运行写入其他目录，不覆盖这份记录。

## 已得到的结果

`coupling_completed_seed.json` 保留实际命令、求解参数、标量检查和原始产物的 SHA-256。原始数值数组只在 scratch。

| 项目 | 已完成数值 |
|---|---:|
| 前缀 q | 0.0002 |
| 前缀节点数 | 607 |
| 采样全度量 FFT l1 | 2.371462100615346e-11 |
| 外层真实 DN 重检的原始 BC 残差 | 2.050495712417276e-12 |
| 尾 shooting 归一残差 | 2.019421900908185e-9 |
| 非均值高度一阶接缝误差 | 4.1039065204862285e-14 |
| 非均值高度二阶接缝误差 | 9.701094248563116e-13 |
| 均值高度一阶接缝误差 | -1.4012402349550257e-13 |
| 均值高度二阶接缝误差 | 3.2640556923979602e-12 |
| 尾 audit 的最小 leading 系数 | 0.9183571218791513 |
| 尾 audit 的 actualMetric | 3.332227715474851e-15 |

这里的尾 `actualMetric` 是原引擎的有限尾审计。完整 Cartesian 刚体配准、共同 C2 表示、无限深尾闭合、全族 reach、非全等证据和 held 10% 均未支付。本包不是课题完成证书。原前缀 audit 自带的旧 scope 文案仍提线性端口；本次非线性联立的依据另存于 `actual_outer_checks` 和 `tail_seam`，不要把旧 scope 当作本次边界求解的方法。

## 复用与符号

原始联立器是提交 `46fe93d4bb708fdfb7935e91b8141ea77586f0d2` 的 `topics/visible-flexible-closed-surface/scripts/db6f-prefix-coupled.py`，SHA-256 为 `37defb33c031fd967ab0e06e086da56f2d67e30dd88bbbcb8e5e13201476511a`。`TailMixin`、`AffineTailForInnerBVP`、`solve_with_actual_tail` 和 `seam_audit` 的方程未改，只将模块加载指向已审过的 m=2 前缀，并选择新的物理尾 factory。

`coupling_sign_audit.md` 给出全部链式法则。本支线 `sigma=-1`；worker 输入是前缀完整非均值高度向量的负值。反射与 `r_s` 的负号在一阶导数中相消，不能再给 slope 额外翻号，也不能假定非线性 DN 为奇函数。Jacobian 对输入物理高度求导，不再乘除内部 r 的四次方。

内层 BVP 使用真实尾在当前点的仿射线性化；每个内层候选都再次调用原真实非线性尾，并检查原始 BC，才可能接受。`--actual-every-query` 可选择继承的直接方式。

## 从 partial clone 再生

以下假设本包保存于课题的 `scripts/coupling/`。`--dest` 必须是仓库外的新目录。

```bash
python topics/visible-flex-held-10pct/scripts/coupling/prepare_coupled_runtime.py \
  --repo /absolute/path/to/math-research-public \
  --dest /absolute/path/to/coupled-scratch
```

这一步按 `coupling_recovery_manifest.json` 逐文件 `git show` 并核 SHA-256，恢复原始方程和四个固定提交的小工具。它用冻结 beta8 factory 初始化真实 worker，读取其 ready 输出以再生本物理尾的线性端口；再调用已发布 `smallcut_prefix_sweep.prepare` 再生相同分支的 delta 根与角 chart。不会将 H、DN 数组或 checkpoint 写回仓库。

恢复清单共有 71 个文件，532270 字节；其中原始方程/依赖 67 文件，另四个本题辅助文件来自固定提交 `df901a6f2be972987cda2bbae48881e44feece8a`。清单包含历史 source-side 小端口 blob 的来源，仅为保留既有依赖闭包；本 beta8 端口仍从当前真实 factory 再生。

输出 `runtime-preparation.json` 中的 `commands.seed` 和 `commands.coupled` 是参数数组，可顺序执行：

```python
import json, subprocess
from pathlib import Path
runtime = Path('/absolute/path/to/coupled-scratch/runtime-preparation.json')
record = json.loads(runtime.read_text())
subprocess.run(record['commands']['seed'], check=True)
subprocess.run(record['commands']['coupled'], check=True)
```

也可在准备命令添加 `--run-seed`，让准备器执行第一条。新 seed 是同一线性端口分支在 q=.0002 的冷启动初值；历史实际运行则由已求出的 q=.002 线性端口初值缩小并在 q=.0002 再解。这个初值路径差异被显式记录，不能声称新数组会逐字复现历史文件 SHA。数学检查以实际 `solver_success`、原始 BC、真尾 residual 和接缝检查为准；路径及元数据不同也会改变完整文件 SHA。

本次已实际验证完整源闭包初始化 worker 成功，并核对其首八 DN 和五项物理 cut jet 与运行输入一致。准备器的端口/chart 再生检查另见源包中的 smoke 元数据。不会把一次初始化检查称为完整联立复跑。

## 后续延拓

`continue_smallcut_coupled.py` 从已经成功的一对 `prefix.json.gz` 与 `response_XXXX.json.gz` 启动，逐个 q 生成独立配置和目录。尾配置通过 `initialCheckpoint` 使用前一个成功真实尾状态；前缀也仅从前一个成功联立解重启。每个阶段仍要通过原联立器的真实外层检查。失败时保留最后成功的一对，不把失败响应当作已存在解。

增幅的每个阶段可以调整前缀 delta，因此属于新度量设计；只有随后显式冻结同一 profile、物理尾参数和角 chart 的多分辨率计算，才能叫固定度量精化。尾的第一圈 beta8 设计与其他 true-flat-valley 设计是不同物理度量，不可混用端口或 warm state。
