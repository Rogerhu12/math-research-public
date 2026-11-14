# 丢失的 rounded 第二步 129 节点结果已实际重做

状态：**浮点数值证据；恢复记录**。本节不是当前精确 affine $\delta_3$ 对象。保存它是为了完整恢复 executor 丢失前尚未推送的失败诊断。

固定旧 rounded 输入 `type_fixed_step02_d5_actual_Newton129_step2_probe.npz`，SHA256
`3453e5be05f8ada2dc333d3e2eab5bcbf58d668eea4817ec7cda85913ca77fa7`，以及旧 dyadic $H$，SHA256
`58375d24a99ba0f43b29143fe22f950a6e74e4fec2b94123d68b078fcf088260`。
这组旧射线程序仍忽略了约二进制舍入大小的径向镜像缺陷；其有限原函数也尚未认证。新对称 affine 对象采用另外的明确定义，不能把两者互换。

两次完整重新积分均已结束：

| 129 节点 | 采样 $\max|E|$ | 采样 $\max|E'|$ | 平均 $E/H'_\alpha$ |
|---|---:|---:|---:|
| 原网格 | $1.788679746539401\cdot10^{-6}$ | $0.005103154605687443$ | $-1.5173991260774357\cdot10^{-8}$ |
| 偏移半格 | $7.884658858214877\cdot10^{-5}$ | $0.0004626094978859019$ | $-2.1331525328910764\cdot10^{-8}$ |

这些标量与丢失前记录一致，是本次真实重跑的输出，未从聊天摘要拼出报告。整格看起来较小的误差漏掉了错位格上的明显振荡；因此后续已改用全实际射线的 Newton，而没有把旧 129 格插值误差当连续误差。

JSON 分别为：

- `2026-11-12-step02-d5-actual-Newton129-step2-Hnodes129.json`，SHA256 `78483c803ce2ad7ed8100c4cafe4a1eddd2bcf2d0f2b17829b4d2414aad1ab26`；
- `2026-11-12-step02-d5-actual-Newton129-step2-staggered129.json`，SHA256 `4bcf671b1f9f41dedcdcf7c7da811c4c52e97e6959945235a4b72ed1f5b70f86`。

从本课题目录重做：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_conjugacy_nodes.py \
  --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_probe.npz \
  --directions data/phase_ring_continuation/type_fixed_step02_schur_directions.npz \
  --parameter-map notes/2026-11-12-phase24-corrected-step02-parameter-map48.json \
  --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_dyadic_H.json \
  --out notes/2026-11-12-step02-d5-actual-Newton129-step2-Hnodes129.json \
  --branch-checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_Hnodes_branch.npz \
  --rays 129 --block-size 43 --tolerance 2e-9 --resume

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_conjugacy_validation.py \
  --checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_probe.npz \
  --dyadic-conjugacy data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_dyadic_H.json \
  --out notes/2026-11-12-step02-d5-actual-Newton129-step2-staggered129.json \
  --branch-checkpoint data/phase_ring_continuation/type_fixed_step02_d5_actual_Newton129_step2_staggered_branch.npz \
  --rays 129 --offset .5 --block-size 43 --tolerance 2e-9 --resume
```

同一 rounded 输入的完整区间源也已重新物化，SHA256 仍为
`1ef92be77cff11904b656c33b3e74994d6415428160319cd92b5df2717d36e14`；
数值代理已独立重跑其局部根和 R57 独立控制点盒包含证书。那些证书属于这个旧 rounded 点，不给当前精确族增加新的参数结论。
