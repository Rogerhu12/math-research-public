# 原 g 的 T96 零高度真实尾响应与可复用锚点

2026-11-14，exact_refinement，AI 辅助研究。**状态：真实有限尾求解及完整响应已经完成；新大核的非零尾、完整联解和闭曲面尚未完成。**

## 1. 原始执行与输入

本公开仓库 Actions run `43582043166` 的 `tailzero` 数值步骤已成功。执行源提交为 `8fa6b3f3b5365bfffd674cdc04f7d77519fa0d76`，完整输出保存在 artifact `14109122474`，归档于 `public-actions-43582043166-1-tailzero/zero-H-T96/`。其后 publisher 因读取到新的根 README 而拒绝直接发布，不是数值步骤失败；root 已读取规则差异并另行保全实际输出。

入口是 `computations/exact_20261114_true_tail_client.py`，使用原冻结物理度量、原 Fourier-root/tangent worker 和明确记录的三处构造器容量扩展。全部 96 个材料高度系数准确为 0，未把小的非零输入截成 0。有限设置是 T96、角网格 1024、spacing 2、物理深度 8、每物理段 shootingParts 8；实际有 576 个 shooting stages、577 个完整状态。原 RK/audit 步数均 12，原接受容差为 `2e-9`。

关键原文件 SHA-256：

| 文件 | SHA-256 |
| --- | --- |
| `result.json` | `7548f90cf7a8da13e88a292cafbc22dd25613b934b4d03bb6597f2b16d6e35a1` |
| `tail_0001.json.gz` | `08d1e4865cb00d7d48ab169ce387a60119f304bc4dc4953eb8fd029fdbff1160` |
| `tail_ready.json.gz` | `c6b6e53b276ae9fde93c5d149cbd80cf2f2ea0e680cc08d0977c619eb14b1905` |
| `tail_intent.json` | `7f939b098dfbca2ed0e67474e50ab7e501cc0f60f58d469171263a49850e6be8` |
| `config.json` | `456d55c7f4a6cf3df8788c465a67b0774e53fa2fdc26f0d385b0556666cd6f53` |

## 2. 实际结果与完整审计

原 worker 正常退出 0，总用时 `805.484174514 s`，实际请求到响应为 `783.520987888 s`。即使初始状态恰为零，原程序仍先做完整 variational shooting pass，再报告第 0 轮 `norm=0`，随后执行完整 audit、J 和 tangent predictor；没有用零解的形式代数代替这条实际执行链。

| 原始记录字段 | 实际值 |
| --- | ---: |
| 非线性 normalized residual | 0 |
| audit `fullD` / `normalizedFullDefect` | 0 / 0 |
| audit `minLeading` / `minD` | 1 / 1 |
| audit `actualMetric` | `9.992007221626409e-16` |
| audit `holonomy` | 0 |
| audit `formalCurvature` | `7.994254693518797` |
| cut radius | `0.30000000000000004` |
| cut background slope | `0.08000000000000027` |
| cut background second | `-1.866666666666673` |
| cut E / E′ | `1.0064` / `-0.2986666666666687` |

非均值 height、slope、second 均为零；mean slope/second 等于背景，两个 mean correction 为零。保存了完整 `577×192` shooting state、与其一致的 raw-node 副本，以及 `(3T+2)×T=290×96` 的全部 `27840` 个有限 J 条目。J 的 slope 和 mean-slope 行来自实际 shooting tangent 加准确 cut 链式法则；second、mean-second 和 height 行保留原源码的对称差分。没有以 ready 中的线性参考图替代实际 J。

## 3. 导数精度仍需区分

原 trace 中 `tangent_predictor_ready.maxChartCondition` 为 `139135731134629120`。这是真实记录的严重图条件数信号，不能因零态 residual 恰为 0 就宣称高模导数已经精确收敛。

直接抽取原保存值，mode 96 的实际有限 slope-J 对角为 `589.6396854938342`，ready 的独立线性参考 slope 为 `587.3799694613762`。两者本来就沿不同离散路径取得：前者来自实际 RK12 shooting variational flow，后者来自预计算线性稳定图。这次记录不把两者混作同一计算，也不从它们的差异单独判断哪一个已经达到精确极限。

`computations/exact_20261114_zero_tail_response_audit.py` 已准备好在本仓 Actions 中消费这份完成响应，独立检查零态线性化 Darboux 恒等式

$$J_{rr}=\frac{w_r}{w}\left(\operatorname{diag}\frac{(\mathrm{spacing}\,j)^2}{r}-J_r\right),$$

以及均值导数为零、height block 为单位阵、Fourier 模间解耦和与 ready 参考的差异。本条写作时只完成了原输出读取和结构/来源验证，没有在本地执行这些新的误差计算，也没有把尚未产生的消费者结果写为通过。

## 4. 作为完整 DN 联解的初始缓存

新增 `computations/exact_20261114_seeded_zero_tail_client.py`，当前 SHA-256 为 `a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776`。它在原 TailClient 外加入一个明确的初始缓存导入层，不改正在运行或已经完成的原求解器。

它要求完整成功退出结果、真实 full-J/full-audit 响应、ready、intent、输入/运行配置及容量 manifest 全部存在。逐项检查 M/N、全数值设置、全部消费数学源码和冻结输入的字节 SHA、原方法标签、完整 state/raw-node 对应、切口和度量 fingerprints。两个运行的提交号可以不同，但所消费的数学源字节必须相同。只有四个输出路径配置键与资源/路径诊断允许变化；初猜配置不属于被忽略的键。

本批实际 zero bundle 已通过该导入层的纯结构预检；与本批 coupling 已生成的真实 ready/config/intent/capacity 也通过完整语义和来源比较。JSON 中 `0.0` 与 `0` 按准确数值相等处理，不加容差，布尔值不充当数值。没有为这个预检启动新的 worker 或重新求尾。

实际联解使用新 client 模块并设置 `VISIBLE_FLEX_COMPLETED_ZERO_TAIL_DIR` 指向上述已完成目录。只有准确同零 H、`audit=False` 的初始请求可复用这份实际响应；进入任何新 H 或任何 `audit=True` 请求前，导入缓存即被清除，随后执行原真实 worker。新 H 不阈值化，最终审计不会被缓存跳过。导入发生在 client 侧，没有伪造 worker 内部的 tangent predictor；首次新 H 使用原初始化路径。

这是一个已完成的原 g 有限零高度尾锚点。它不能证明新大核在真正 cut 上 T96 足够，不能代替材料谱、同 g 频率/径向/深度精化、完整六 jet、闭嵌入、hold 幅度或全相位 reach。课题仍未完成。
