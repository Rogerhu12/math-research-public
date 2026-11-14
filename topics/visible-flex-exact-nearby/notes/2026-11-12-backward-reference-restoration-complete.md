# 后腿历史参考的完整恢复

本记录只证明保存的浮点参考及其有限二进制定义逐字恢复；不把该参考称为真实 ODE 解。

## 已恢复的对象

旧对象仍为准确仿射参数
`-7789866024620307/4611686018427387904` 的 δ4，原始 1032 条射线、
Q256、容差 `2e-12`、同一 knot-aligned 自适应积分器均未更换。
新参考的目标仍为 δ5，准确参数
`-7789843107295549/4611686018427387904`，retarget descriptor 的 SHA256 为
`097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052`。
这两个对象的身份未合并。

原后腿进程已完成积分但在保存大数组时退出 137，只留下前 20 个 raw 分块。
`fourfold_shared_trace_stream_recovery.py` 从该已保存前缀内准确 knot 步 319、
τ = `-0.09452111494777876` 重启；重叠步 319→320 的接受状态和 dense 系数逐字相同，
随后每块立即保存并释放。实际补完 230 步，耗时约 3525 秒。
所有 36 个 raw 文件（35 块及 manifest）均与历史哈希一致，末端角度、Jacobian、参数列也相同。

从该 raw 后腿重新生成的 550 段 U/L 参考（23 shards）和 Q（12 shards）全部逐字相同：

| 对象 | manifest SHA256 |
| --- | --- |
| 后腿 raw | `e59b287dd2eedcd4f80b80debf7f46f6b2f1a9dc3d40eb596e98082a681dd7ea` |
| 后腿 U/L | `0ad615a077a0c313d0700c3a6392f39250617257b93197ba1f5f766716191a07` |
| 后腿 Q | `6759d5c65842a32ad9c9f4ad7e8ccd51b264f6d5d9b7e29549ec409cd1554b5e` |

最后 `fourfold_retarget_reference_identity.py` 重新读取两腿全部 1100 段，检查每个
U/L 与 Q 分片的字节、尺寸、实均值、时间元数据以及所有内部准确接缝；以 Fraction
逐项重算 `U4f,start + a = h5/4`，并验证两腿的准确 symbolic product 接缝。
Q 仅为给定的有限 Bernstein/Fourier 多项式，未被称为真实 Jacobian。

## 小报告

- `2026-11-12-step4-backward-stream-recovery.json`：原退出 137、准确重启、重叠验证及后续块。
- `2026-11-12-step4-backward-raw-recovery-hash-check.json`：全部 36 个 raw 文件。
- `2026-11-12-step4-backward-reference-recovery-hash-check.json`：23 个 U/L 分片。
- `2026-11-12-step4-backward-Q-recovery-hash-check.json`：12 个 Q 分片。
- `2026-11-12-step5-restored-complete-retarget-identity.json`：两腿全部准确有限身份。

这些小报告可保存入库。大 raw、U/L 和 Q 可按已保存 manifest 重建，不新增为提交内容。
最后一份报告 SHA256 为
`9b2778a14ffc17eff7ea615110a76afbcf5de488470fa7fa7fd64e1576348e26`。

## 重放入口

在课题目录执行，统一限制 BLAS/OMP 为 1。保留准确已恢复前缀时，流式恢复命令为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python -u scripts/fourfold_shared_trace_stream_recovery.py \
  --hash-manifest notes/2026-11-12-D5-step4-shared1032-raw-trace-hashes.json \
  --old-report notes/2026-11-12-D5-exact-affine-step4-shared-knot-Hnodes1032.json \
  --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step4_root_tight.json \
  --trace-dir data/phase_ring_continuation/exact_affine_step4_shared_knot_dense1032 \
  --out notes/2026-11-12-step4-backward-stream-recovery-replay.json
```

如果整个 raw 目录丢失，须先用原冻结 `fourfold_phase_shared_grid_adaptive_chunks.py`
的历史参数恢复前腿及后腿前缀；不能凭空构造本流式入口要求的前缀。
完整原始命令和对象哈希已保存在历史 shared1032 报告中。

U/L 选择必须写入一个尚不存在的新目录：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python -u scripts/fourfold_shared_dense_reference.py \
  --trace-dir data/phase_ring_continuation/exact_affine_step4_shared_knot_dense1032 \
  --leg backward --rays 1032 --degree 516 --segments-per-file 24 \
  --previous-reference data/phase_ring_continuation/step4_shared1032_reference_forward/manifest.json \
  --out-dir data/phase_ring_continuation/step4_shared1032_reference_backward_replay
```

Q 使用冻结 `fourfold_shared_reference_retarget.construct_Q(reference, output, 128, 48,
sha(source))`；`reference` 为上述准确后腿 U/L manifest，`output` 为尚不存在目录。
该源 SHA256 必须仍为
`d6bcd4c3594151036108e7f6d154991b2ad7252d0afba4d5d795dfc45d64f583`。
先比对全部历史哈希，再将缺失 canonical 分片恢复；存在不同字节的文件必须另保对象。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_retarget_reference_identity.py \
  --descriptor data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --out notes/2026-11-12-step5-restored-complete-retarget-identity-replay.json
```

R77 的准确平方结构使当前真实场验证主线可只支付前腿；本后腿恢复用于完整兑现遗失输入的重做要求，
不据此额外宣称后腿真实流误差已经验证。
