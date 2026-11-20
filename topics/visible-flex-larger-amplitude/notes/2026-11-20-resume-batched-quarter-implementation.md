# 同一完整闭面方程的批量 FFT 与 R653 角向实现

2026-11-20 09:41 UTC，Astra-larger-resume-24b2ab87-20261120。**实现及有限数值证据；尚无新几何解。**

原 ClosedGram 的共享 quintic、准确 affine core/端口、完整解析 lift、core→ρ→Θ 的导数与转置全部保留。[R653](../results/R653-exact-quarter-angle-closed-Gram-reduction.md) 的重数作用于 residual/Jv，并在 vjp 输入上再次作用，保存原完整角网格目标。外部 Frobenius 和径向权仍须双向一致；不要再乘一遍重数。

## 实际实现

- [批量算子](../scripts/resume_20261120_batched_closed_gram.py)：19058 B，SHA256 `02a5e83a799d929a9d1426b5eaff9f65484a660932b0bf51634298a1a2284b4a`。
- [最小实现核对](../scripts/resume_20261120_check_batched_closed_gram.py)：4691 B，SHA256 `ea09c5fb5cbe28b4ad68bb48ebb76c275a9f84b2ab1723a4af18b8fa325f263d`。与实际核对源的数学输入/计算相同，只把旧 scratch 路径改成仓库相对路径和必填 `--out`。
- 原数学算子仍是 `notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py`，SHA256 `e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d`。

`create(dense_source, mesh, a, radius, fixed_core, M=160, N=2048, stage_block=64, quarter=True)` 中 N 始终指原完整角数；实例 `full_N=2048`、`N=513`。`residual`/`jvp` 返回带平方根重数的数组，`raw_residual`/`unweight` 给真实 Gram 分量，不能直接对加权分量读物理谱范数。每64个径向stage分块合成/转置；缓存只对同一个完整实向量复用。

对923节点模型，quarter 缓存约45.4 MB，残差约22.7 MB；这是数组尺寸计算，不是新求解的实测峰值或加速声明。`six_jets` 保持原实际物理导数接口。

## 已完成的必要实现检查

新实现以明确小输入作一次检查：M4/N64、9个非均匀节点、306自由变量、block3、固定seed20261120；节点在复算源码中完整给出。这不是闭面候选，不能移作科学误差或收敛证据。

|比较|相对差|
|---|---:|
|原逐点算子 vs batch 残差|1.14e−16|
|原逐点算子 vs batch Jv|2.13e−15|
|原逐点算子 vs batch 转置|3.32e−15|
|quarter complex-step Jv|2.90e−16|
|quarter 伴随内积|1.56e−16|
|full/quarter 梯度|1.93e−17|
|full/quarter 正常矩阵作用|5.39e−17|

两种完整平方和在此次浮点评价中相同；这不提升为逐位等价定理。缓存/无缓存对照相同，准确 affine 端口全部满足。原小报告 SHA256 `0970670eb9fd171747c477054e37bbea9d70dac4623bf47e86ac9c49b41796d8`，仅留 scratch，不保存可再生输出。

从仓库根运行：

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python \
 topics/visible-flex-larger-amplitude/scripts/resume_20261120_check_batched_closed_gram.py \
 --out /tmp/fullclosed-small-check.json
```

下一实际工作是读取新环境重建的真实 warm 并推进非线性方向。真实 warm 的比较、速度、收敛及几何结果尚未在本条发生。只完成必要新实现检查，不重跑旧开放片证书或旧 dense 全数组核对。
