# 第 419 段的有限左端 cap 覆盖

同一准确对象与完整时间外域的定义见
`2026-11-12-full-time-correlated-outer-gate.md`。本文件只增加准确有限
分段的径向覆盖证书，未改动已经冻结的外域源、报告或证明。

独立小入口 `fourfold_phase_reference_germ_partition.py` 对同一个准确
对象、同一个第 419 段和细化真根，认证了准确划分

\[
 [0,1/1024]\ \cup\ [1/1024,1]
\]

的全部实际 common-span 覆盖。左端 cap 需要原来的三个 germ，
余下整个区间只需要第三个 germ。共享物理时间端点为

\[
 \tau_*=1143496157753710521/2305843009213693952.
\]

这是径向轨迹与准确 knot 的有向覆盖证书，没有新求解任何 knot
预像，也没有依据浮点近重合合并 knots。余段径向像离第三个 span
的左端大于 \(1.2605\times10^{-6}\)，离右端大于 0.00027494。
若把同一个有限参考及同一个全段修正多项式准确限制到两段，新增
接缝跳跃准确为零；若分别重新校正两段，则必须重新支付实际跳跃。
此小证书尚未对校正后的残差作任何结论。

输入身份、每段准确时间端点、实际径向区间、全部 common spans、
连续性及真根收缩轨迹保存在
`type_fixed_step02_d5_exact_affine_step3_reference419_germ_partition.json`，
SHA256 为 `32d1e3743c8461d98c30ed92a23dc4eb2d8f6054b498db97d35905aba792b9b1`。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_reference_germ_partition.py \
  --manifest data/phase_ring_continuation/r61_step3_shared_forward/manifest.json \
  --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json \
  --segment 419 --cuts 0,1/1024,1 \
  --out /workspace/scratch/f6a2c7886477/newton-experiments/reference419_germ_partition_replay.json
```
