# R159 实际 node/cell normal-system 接口与闭存记录

完整证明见 [R159](../results/R159-local-normal-equations-with-exact-field-elimination.md)。这里保存实际接口、输入身份、运行结果和适用范围。没有运行新的 BVP 或 body，也没有给未收敛场补一个虚假连续证书。

## 1. 冻结源码与入口

| 源码 | SHA256 |
|---|---|
| `scripts/fd2d_gc_local_normal_system.py` | `2773a28192620749bb227b33e7ebdbb42deacca9370b34c392ba9d3edfa95bcf` |
| `scripts/fd2d_gc_positive_trace_stream_normal.py` | `3199493acdd0818e68655f80c39cdf4a10a9f5d7f0426bb9517b758387a4ab36` |
| `scripts/fd2d-metric-local-normal-check.py` | `105d23335203a16c159486548ccba442587881ed1040fcf90fef3318ec9d7467` |

生产使用：

```python
from fd2d_gc_positive_trace_stream_normal import stream_positive_trace_normal
from fd2d_gc_local_normal_system import bounded_normal_direction

normal, assembly_info = stream_positive_trace_normal(
    problem, vector,
    curvature_cap=7.2,
    curvature_weight=1.,
    high_gauss_weight=1.,
    high_codazzi_weight=1.,
    order=2,
    block_cells=8,
)
direction, direction_info = bounded_normal_direction(
    problem, vector, normal,
    damping=1e-5,              # 或同原调用选择 .001 / .1
    central_floor=.1,
    central_cap=1/.136,
    profile_box=.08,
    preserve_gap=True,
)
```

需要另一阻尼时复用同一 `normal`，不重新产生全场 Jacobian。原 line search 的完整实际残差评价仍必须执行；不能用 normal 模型预测取代非线性接受判断。

`normal` 保存未缩放的 `diagonal, upper, Hfp, Hpp, gf, gp` 和准确消元之后累计的 `field_norm_squared, parameter_norm_squared`。`normal.hff()` 才生成字段 normal 稀疏矩阵；整个路径不保存全 tall J。所有 source/实体身份继续由调用 driver 绑定，本 helper 不更改旧 source、场或公共索引。

`normal.mapping` 明示 free/fixed 索引、中央参数映射和末端 `trace_gauge_pairs`。中央 `Jp += Jcentral @ core_coefficients`、coast 原始 l 列删除、terminal `Jn−Jl` 均发生在列平方范数之前。

## 2. 新格内行的直接接口

一个新实际格内 Gauss/曲率包若依赖两个端点，给出其**完整实际**局部 Jacobian：

```python
# local_J 的列：[left_raw_q, right_raw_q, all_explicit_parameters_P]
normal.add(residual, local_J, nodes=(cell, cell+1), label='actual_cell_G')
```

这会保留所有非线性链式参数列，自动做同一消元、列范数和 normal 累加。它不限制新包的行数。新的有限目标必须在调用方明确标识，原 16 目标和新增格内目标不能混写；追加后实际统计从 `normal.rows / normal.row_groups` 读取，旧 `assembly_info` 的初始整数统计须由调用方更新。`LocalNormalSystem` 的数值内容即时更新。

即使 cut-material tail lifting 换成另一个已明示函数，只要残差仍依赖同一节点/相邻节点与全局参数，R159 的代数与核心累加器都适用。具体实际字段 evaluation 则必须调用新 provider，不能因 normal 结构相同而把旧字段当作新字段。

R158 独立 tail degree 用真实 `parameter_count` 和 `tail_parameter_slice/profile_parameter_slice`。核心没有假定 tail 参数个数等于 `K+1`。本次实际方向夹具是 K15；K31 的全运行改善和峰值没有在此冒称已实测。

## 3. 局部 view 的实际含义

`radial_view` 复制当前 problem 的小视图，只切出实际保存的 x 节点和其已有完整 atlas coordinates；不重造网格，不改 chart、物理 g 或固定 reference。每个节点的 no-J 包仍由完整 R153/R155 provider 求值，因此曲率和 Gauss 不会漏掉这两个非线性场变换。

格 consumer 直接使用已冻结的 `gauss_cell_positive_trace`，包括 R152 affine known-lifting 的分片细求积、R153 非线性商项、R155 正 trace 及准确 n 端点项。小块返回的行先核查径向依赖确实只落在对应格两端，再累加。没有用旧 trapezoid 行替换现 Gauss2/endpoint 行。

本节点/cell 顺序与主 driver 的行拼接顺序不同，属于行排列。它不改变平方目标和准确 normal。浮点归约顺序会改变，不能声称逐位同；实际比较记录如下。

## 4. 一次实际小夹具

输入：

- `notes/2026-11-12-fd2d-raw-bump-trace16-b0004-accepted-0002.npz`，57,893 字节，SHA `520a3e333c54bcc18da5071d8534cf91f9e6f0de60a567a5cbb56abb5e697e28`。
- 同轮 `...trace16-b0004-report.json` 提供真实 candidate、reference、profile radius 包及全部有限权重；checker 核对 candidate SHA、实际 mesh/supports 和 seed/atlas/R153/R155 完整定义。
- 实际 candidate SHA `7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1`。
- 原 Schur 源 SHA `44b869e7ba5e69c4db60a3fdd8e597b1c2003ceb3ef64f5753fdd1144042fc57`，未修改。

实际 cells 为 `0,8,63,64,67,70,71,118,119,120,121`，其相邻端点共 17 个。这里消费的是原实体上的这些局部行，没有用跨越缺口的新长格定义一个新场。三个典型消元全部覆盖。

复现命令：

```bash
python scripts/fd2d-metric-local-normal-check.py \
  --field notes/2026-11-12-fd2d-raw-bump-trace16-b0004-accepted-0002.npz \
  --run-report notes/2026-11-12-fd2d-raw-bump-trace16-b0004-report.json \
  --out-prefix notes/NEW_UNIQUE_STEM \
  --damping .001
```

同 stem 不得已有文件；外部 console 文件应放在独立目录，不能先在输出 stem 下创建日志。

实际 `check-02`：执行器 session 10665，初次 chunk `6038c4`，末次 chunk `a9d9e9`，真实 exit 0；外 wrapper 7.54084 秒，内部数值 3.42725 秒，峰 RSS 108784 KiB。2012 行中包含 70 个活跃曲率行。

完整报告 `...metric-local-normal-check-02-report.json` 给出：

- `Hff,Hfp,Hpp,gf,gp` 的归一最大绝对差至多 `1.1806634939912965e-15`。
- 变换后列平方范数字段差 `2.759690750559319e-16`，参数差 `9.53805749299371e-17`。
- 原/新同 λ=.001 的 SLSQP 都 success、102 次迭代；LU nnz 都 58,532。
- 方向 L2 归一差 `7.311547908501665e-8`；方向的实际残差作用 `Jδ` 归一差 `7.469390097535407e-14`。前者不能抹掉，也不能用后者声称每个未充分观测分量逐位相同。
- 新方向直接线性残差范数 `1.063225477293313`；normal 二次式差 `1.021405182655144e-14`。
- cut、coast 删除方向及 terminal 成对方向约束误差 0；中央映射差 `8.470329472543003e-22`。
- 原输入向量变化 0；所有运行源码结束时 SHA 未变。

证据 NPZ 只保存选中索引、两方向、小残差向量、列范数及小 Schur 数据；不保存大型全域矩阵。报告中的 tall 夹具 1.775 MB 小于为全节点预分配的 normal 5.489 MB，这是刻意的小夹具，**没有据此声称实际主运行峰值降低**。

## 5. 真实失败与范围

`check-01` 真 exit 1：外 wrapper 先创建同 stem 的 console 后，checker 的 fresh-stem 保护正确拒绝；尚未构造实际场/矩阵。保留 `...check-01-console.txt` 和 `...check-01-exit-receipt.json`。第二次只换独立 console 路径，三份源码未改。

小对照不增加验收门。证明覆盖任何满足第 1 节局部性并正确完整求导的有限行集合，实际有限方程是否已足够约束格内 Gauss、能否收敛、后续连续真实 metric/geometry/reach 是否通过，都仍须由相应真实实体和消费者支付。当前 16 末态的格内大 Gauss 由主数值代理独立确认，本 helper 不掩盖它。
