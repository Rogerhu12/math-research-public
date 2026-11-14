# 同 RK12 候选 v2：完整 determinant 留证及非原生检查的最小调整

本接口接续[公开 request21 的真实工厂失败](2026-11-14-public-same-RK-candidate-probe-actual21.md)。v1 报告不足以区分 determinant 非有限与有限零值；v2 将在实际计算中完整记录分支所需数据，不回填未观察到的 v1 数值。

## 数学范围

设候选 stage 块为 $T=\begin{pmatrix}a&b\\c&d\end{pmatrix}$，已给定深侧私有图 $\pi_{n+1}=\gamma_{n+1}Q_{n+1}$。若

$$
u=a+b\gamma_{n+1}\ne0,
$$

则 $Q_{n+1}=Q_n/u$ 和 $\gamma_n=(c+d\gamma_{n+1})/u$ 在精确代数中给出 $T(Q_{n+1},\gamma_{n+1}Q_{n+1})=(Q_n,\gamma_nQ_n)$。这个公式无需除以 $\det T$，因此有限浮点 determinant 为零并不是构造一个供原求解器检查的初猜所必需排除的情况。

v2 仅移除“有限 rounded determinant 等于零就终止”的新增 veto，保留所有非有限量、零 $u$ 及非零传播下溢的失败。它不声明 $T$ 可逆，不声明线性块准确，不证明候选对应任何真尾解。原 `evaluate/solve/J/audit`、far Robin、graphs、gains、scales、RK 网格、branch guards 和容差全不改。旧 v1 初猜器、探针、全部原始回执保持独立固定身份。

## 三个独立源

| 文件 | SHA256 |
| --- | --- |
| `geometry_20261114_zero_rk_stage_initializer_v2.mjs` | `c6146b9566031ec636949f94bcbbe4b6fd051002bdb5949a6c70821e0d0c1879` |
| `geometry_20261114_zero_rk_native_probe_v2.py` | `f30fa10b8b5d2261163bc74bacd7f2cc8354efb73b9f68680f3db50457662f09` |
| `geometry_20261114_zero_rk_native_probe_v2_hook.mjs` | `612a6e995214e192f8eea2522eab12576a95e482f0efcef85c17685439b23cbd` |

独立 initializer 仍导出 `createZeroRKStageInitializer(dn, options)`。新增可选 `options.onConstructionEvent`，仅传出诊断副本，不向原 `dn` 或私有构造数组写回。成功返回时，原 `stageBlock` / `predict` API 保留；身份另列有限零 determinant 的总数、首例和最小尺度化消去量。

每个 stage 的全部模在判定拒绝前形成完整 $T,ad,bc,ad-bc$ 记录。对有限乘积，消去指标定义为

$$
\chi=\frac{|ad-bc|}{|ad|+|bc|},
$$

用最大乘积绝对值缩放计算，避免分母求和溢出；两乘积均零时单列标志并令指标为零。它只描述这次浮点行列式计算，不是矩阵条件数或严格误差界。非有限数用明确分类对象保留，不写 JSON NaN、不默换为零。

observer 保留完整 stage blocks、所有已完成私有图行及分母、任何拒绝位置和实际操作数。实际 v1 失败的 stage 12 / mode index 92 另记录每个原 RK 子步的块和 determinant，以定位本次浮点消去发生的位置。发生拒绝时立即刷出已记录证据；完整事件按批 gzip 分块，每件小于 5 MB。

`predict` 的非零下溢仍不放行。失败时记录真实 $Q$、graph 或分母、结果及是否为非零下溢，并保留已完成节点。若候选成功，完整状态分块附 `negative_zero_columns`，未来消费者先恢复这些 `-0` 再核 binary64 SHA，避免 JSON signed-zero 表示差被误认为场变化。

## 与原生 worker 的接线

Python 和 hook 继续执行 v1 的原 constructor/ready/source/capacity 校验，实际导入被锁的原 `integrationGrid`，只替换请求循环。新增必需的 `--first-candidate-summary`，固定绑定真实 request21 summary SHA `0c69d072f25c927e32322021e65b717ef6d68089d6332ed4c69c793fec87b481`；同时核完整 H、原配置、请求和原始源身份。没有零解重算，也不改原已有零缓存。

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261114_zero_rk_native_probe_v2.py" \
  --failed-directory "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43598917532-1-coupling112trust/full-DN112" \
  --cold-probe-summary "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43602823170-1-coldtailprobe/cold-tail-residual/summary.json" \
  --first-candidate-summary "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/public-actions-43603818345-1-zerorkprobe/same-RK-candidate-native-probe/summary.json" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --out "$VISIBLE_OUT/same-RK-candidate-native-probe-v2" \
  --node-heap 1536
```

只有候选完成才运行一次原 `evaluate(candidate,H/r^4,false,originalScales)`。归一化继续使用原 gain 的第零模，绝不改用候选图的分母。线性块残差和原生非线性残差独立完整输出。无 J API 未提供的 `minA/minD` 不伪造。无论残差大小，探针都不调用 Newton/J/audit，也不产生接受旗；exit0 仍只表示原无 J 遍历完成，构造或原域失败为 exit2。

最先读取 `summary.actual21_failed_block_observed_in_v2` 和 `actual21_block_current_determinant_branch`，即可看到本次实际同段矩阵的四项及判定分支；其余完整事件在 `initializer_construction_evidence.artifacts`。若后续出现另一个阻点，应据同一完整记录处理，不从本次源改动预设成功。

交付时只完成 Python AST、两个 Node 模块及 hook 所生成文本的语法检查，没有在本地执行任何数学函数。新候选的工厂结果、下溢/域状态、线性残差和原生残差均待本公开仓库 Actions 实际运行。
