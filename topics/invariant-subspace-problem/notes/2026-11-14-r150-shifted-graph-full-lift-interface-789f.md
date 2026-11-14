# R150 continuation：全图模结束后的自动九目标 lift 接口

作者：normal_annihilator / 789f。2026-11-14 UTC。

状态：实现及有界编译已完成；**尚未执行完整图模或此后处理**。只有此前 672 来源前缀真实完成。本文件给唯一全量请求的准确入口，不预写成功结果。

## 1. 一条完整入口

使用[完整 wrapper](2026-11-14-r150-shifted-graph-full-lift-runner-789f.py)：

```text
python3 topics/invariant-subspace-problem/notes/2026-11-14-r150-shifted-graph-full-lift-runner-789f.py
  --input <完整原生正常形二进制>
  --mapping <原normal-form-mapping.json>
  --nf-receipt <原完整正常形回执>
  --ann-receipt topics/invariant-subspace-problem/notes/2026-11-14-r150-target-minimum-annihilators-receipt-789f.json
  --work /tmp/r150-shifted-graph-full-789f
  --out <本次小输出目录>
  --seconds 1800
  --memory-mib 4096
```

这里 1800 秒是**图模阶段的硬界**，其软界为 1740 秒。图模确实返回全部 2195 来源、1021/1174 消元条件后，后处理有另一个 60 秒硬界。两个 C++ 编译各自受 30 秒、512 MiB 上限约束。完整 wrapper 不调用旧 `Singular std`，不重跑已停的原大 DAG 反向展开。

`--work` 放大图基、执行文件、完整原始候选和临时 checkpoint；`--out` 只放小回执、完整来源字典、日志和目标系数 gzip。工作流可另以相应整体作业上限包含上述顺序阶段，但不能把 1800 秒解释成已经包括后处理的时间承诺。

## 2. 九个目标如何直接恢复原正常形来源

[后处理 C++](2026-11-14-r150-shifted-graph-target-lift-789f.cpp)读取全图基二进制及完整来源字典。它逐行确认 1021 个输出主元、1174 个来源主元及后者的零输出；对输出行只除其非零域常数首项系数，同时对保存的来源列作同一归一。

随后从同一原正常形输入读取全部九个 \(T\)，形成 \(h_{31}T\)。每次正常形消去

\[
v\longleftarrow v-a s^uG_i
\]

时，同时在原 2195 个来源坐标上累加 \(a s^uV_i\)。所以没有再展开旧 GB DAG，也没有仅保存抽象商空间关系。

结果系数的源编号是完整字典中的原第 1 至 2195 列，并各自保留原 6188 行号。代码逐项检查

\[
\deg C_j\le114-\delta_j.
\]

最末再重新读取完整原正常形矩阵 \(R\)，用九目标并行位平面核对所有 1034 个分量、参数次数 0 至 114 上的准确多项式身份

\[
RC=h_{31}T.
\]

这一步是**原正常形来源身份**。仍须后续复合 \(B(hJ-HC)\) 和常预基前后 DAG，才可称已经回到原 6188 行及十七式的完整恒等式。因此成功字段准确命名为 `fullNormalFormSourceIdentity`，不命名为原十七式身份。

## 3. 成功和失败字段

[后处理 runner](2026-11-14-r150-shifted-graph-target-lift-runner-789f.py)只有在下列条件全部成立时把回执状态写为 `completed`：

```text
exitCode == 0
nativeStatistics.status == "original-nine-targets-low-degree-lift-complete"
nativeStatistics.fullNormalFormSourceIdentity == true
nativeStatistics.allDegreeBoundsVerified == true
```

单纯返回码 0、图模成功、所有目标约化为零，均不能替代最后的完整 \(RC=h_{31}T\) 核对。图模前缀、全图但消元条件失败、后处理超时或残差非零都给明确未完成状态。

全 wrapper 的 `completed` 还要求图模阶段及后处理阶段都真实完成。它的 `sourceIdentity` 再次标明特征零提升和常预基回代尚未由这个计算阶段完成。

## 4. 小输出和 checkpoint

正常成功时小输出为：

- `full-lift-receipt.json`；
- `graph-receipt.json`、`graph-metadata.json`、`graph.log`；
- `target-lift/target-lift-receipt.json`、`target-lift/target-lift.log`；
- `target-lift/original-coefficients.json`；
- `target-lift/original-coefficients.bin.gz`。

目标二进制头 `R150TC31` 保存来源数、九目标数、24 次共同多项式及其全部系数。每条来源记录保存原来源编号 `u32`、原 6188 行号 `u32`、实际 \(\delta_j\) `u16`，然后保存九个系数多项式的准确 `u16` 长度和升幂规范域字节。小回执保未压缩与 gzip 哈希，且拒绝写入超过 5000000 字节的压缩证书。

九个系数全部算成以后、最后的全 \(RC=hT\) 检查以前，还会原子保存一个约 1 MB 的 `R150LC31` checkpoint。它含全部 2195 来源的九目标系数位平面、完整来源字典、移位组和 \(h_{31}\)；它不是旧反向表达式的 55 MB 中间态。

若 60 秒上限到达验证阶段，后处理回执仍为失败/未完成，但会保存 `lift-checkpoint.bin.gz` 并明确标记 `all-nine-coefficients-computed-full-polynomial-verification-incomplete`。因此可从这些已经计算的原来源系数继续完整核对及常预基回代，不必重算全图模。当前代码尚未实际产出该 checkpoint；只有真实运行到该阶段才会有此文件。
