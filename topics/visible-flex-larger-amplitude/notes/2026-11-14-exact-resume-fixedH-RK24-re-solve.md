# 同原 g、完整 32H 的 RK24 真 Newton/J/audit 重解

可信度：**启发式/数值证据**。2026-11-14。原 worker 已真实退出 0，耗时 1575.8113338069998 秒；`finished=true`、`success=true`，完整响应、DN Jacobian、finite audit、历史和源启动哈希均已保存。

## 固定问题

基点为原接受 A：`2026-11-13-strong-q126-m32-tail2-actual-r1`。保持 M32、spacing 2、physical depth 8、shootingParts 8、576 段/577 个节点、quadrature 512、linearFar 48、linearSteps 2048、全部 32 项物理 cut height $H$、原 160 层 calibrated background 及全部物理参数。唯一的离散变化是 RK4 每段步数及 audit 步数由 12 增至 24；另有私有运行输出路径和 warm 文件路径变化。

原 `tail_frozen_worker.mjs`、Newton、line search、maxIterations 32、solveTolerance $2\times10^{-9}$ 均未改变。原 RK12 响应仅作 warm start，不恢复旧 tangent。请求同时开启 `jacobian=true` 和 `audit=true`。

`exact_20261114_compare_RK.py` 已核对完整 $H$、全部非 RK/I/O config 和 checkpoint 参数、原 factory 参数、cut 几何的 binary64 位值相等。source revision 为 `869436630c99aa5a68afb55bd8877c826034d117`；frozenWarpAlpha 仍为 161.27721826272244；160 层 profile 前后指纹均为 `8a87255bf9e025190a1a98ff800859f05f95a94113045a60af9391fcace51d24`。

## 真实收敛与有限 audit

原 RK12 状态经原算法 warm 转换后，RK24 的首次归一化残差为 0.03500040514935115。两个原 Newton 全步分别把残差降到

$$7.703098286927356\times10^{-9},\qquad 8.361777892934857\times10^{-11}.$$

第二项随后由完整终态再次确认，原容差没有放松。

| 终态有限 audit 项 | RK24 数值 |
|---|---:|
| actualMetric | $7.994359035019858\times10^{-15}$ |
| fullD | $3.6140230122452866\times10^{-12}$ |
| normalizedFullDefect | $1.9441768344969496\times10^{-13}$ |
| minLeading | 0.8635125235436262 |
| minD | 0.9999284957696983 |
| formalCurvature | 7.994260716974354 |
| maxPhysicalPV | $5.651311493468282\times10^{-5}$ |
| holonomy | $7.263803831073157\times10^{-20}$ |

这些是原 audit 定义下的有限结果，不是完整重构曲面的连续最大值。

## 对原 RK12 的实际变化

完整 cut height 向量逐项差为零。其余 cut jet 的最大绝对差为：

| 项 | 最大绝对差 |
|---|---:|
| 非常数 slope，32 项 | $5.9669802736014854\times10^{-12}$ |
| 非常数 second，32 项 | $1.392364331470608\times10^{-10}$ |
| meanSlope | $1.4016565685892601\times10^{-15}$ |
| meanSecond | $3.5083047578154947\times10^{-13}$ |
| meanSlopeCorrection | $1.407203363844355\times10^{-15}$ |
| meanSecondCorrection | $3.5074762240678084\times10^{-13}$ |

完整 577×64 canonical 状态的最大绝对差为 $1.1502295978971233\times10^{-4}$，位置为第 10 个节点的第一个 momentum 分量；最大逐行相对差为 $1.1865646080732295\times10^{-5}$。它说明本次确实重解了 shooting 状态，没有只为旧端点补内点。

**基点 cut jet 很稳定，并不意味着整个 DN Jacobian 已到舍入精度。** 完整矩阵的行依次为 slope[32]、second[32]、meanSlopeCorrection、meanSecondCorrection、height[32]，列为物理 $H[0:32]$：

| Jacobian 块 | 最大绝对变化 | 除以旧块最大绝对值 |
|---|---:|---:|
| slope | 1.0621372059831629 | $6.10409899561724\times10^{-5}$ |
| second | 24.777027686301153 | $8.127128078343387\times10^{-5}$ |
| meanSlopeCorrection | $9.962294184040488\times10^{-11}$ | $4.333024161812661\times10^{-9}$ |
| meanSecondCorrection | $1.669178838197439\times10^{-7}$ | $1.9136278255169992\times10^{-7}$ |
| height | 0 | 0 |

slope 的最大变化位于零起点索引 [19,19]，即角频 40 的同频项，17400.392862988956 变为 17399.330725782973；second 块的最大变化也在该项。原 Jacobian 算法保持不变：slope 和 meanSlopeCorrection 是原 shooting tangent 加精确 cut 链式法则，其余是原对称差分，差分参数 $10^{-4}$。本条没有把后者升级为严格导数界。

## 后续实际重构与范围

新状态的全部端点及真实 RK24 1/2/4/8 内点已交 `exact_20261114_resolved_radial_readout.mjs` 重新计算。消费者明确验证同物理参数、同完整 $H$；禁止复制旧端点数据。完整比较、固定宽 $0.01$ 接缝和九相位闭组装由 `exact_20261114_resolved_tail_pipeline.py` 继续执行，其结果另记，不能预先把本条 audit 数值当成组装后误差。

原 prefix BVP 没有在新 DN 算子下重新求解或重新接受。后续有限闭组装将继续保留原 prefix 的完整 cut jet，并以既有固定宽补丁对齐。当前 A 的大幅度指标仍不足。本条不证明无限 nonlinear tail、精确等距闭曲面、连续嵌入或连续 reach，也不把单独尾部重解称为完成标准的解。

## 归档与复现

紧凑包 `notes/2026-11-14-exact-resume-fixedH-RK24-r1/` 含新 config/request、完整压缩 ready/response、真实 result、comparison、trace、intent、stdout、源启动哈希和工具退出记录。源为 `computations/exact_20261114_fixedH_RK24.py` 与 `exact_20261114_compare_RK.py`；原 91 个 pinned 依赖和冻结校准数据保持原恢复入口。

启动方式是 `exact_20261114_fixedH_RK24.py --topic TOPIC --source-topic SOURCE --out-dir FRESH_DIR --steps 24 --node-heap-mib 512`。完成后调用 `exact_20261114_compare_RK.py --topic TOPIC --new-dir FRESH_DIR --out comparison.json`。完整真实命令、文件身份和输出哈希均在包内，不依赖尚未结束的其它计算。
