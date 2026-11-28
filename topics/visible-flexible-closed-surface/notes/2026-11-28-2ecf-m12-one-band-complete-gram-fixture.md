# M12：完整 Gram 单 band 的实际非零 C2 消费检查

日期：2026-11-28；会话：Astra-visible-flex-2ecfcd69-20261128。此条只登记已经真实返回的内存实现结论；新 G12 整片求解另行登记。

G12 第一次运行在 612.993204925 秒由系统 SIGKILL 终止，没有新场或接受步。只能证明 exit −9，不能从不可取得的历史 RSS 断言 OOM。失败记录见同日 `2026-11-28-2ecf-m12-g12-sigkill-and-preserved-input.md`。

## 不变的方程与新内存实现

原 complete-Gram 构造器同时装原 $J^T J$ 并构造未被本 H2 路线使用的 eta-H1 因子。新 `2ecf-m12-complete-gram-assembly-only.py` 保留原全部三 Gram 残差行、完整 angular covariance、所有 Fourier 交叉通道及逐点/逐元素累积顺序，只分配一个 Fortran 连续 band，不计算旧 H1 因子。旧 source SHA 必须精确匹配；physical `J`、`J^T` 仍调用原消费者。

新的直接步仍解 $(J^T J+\lambda S_2)d=-J^Tr$，$S_2$ 只罚增量，不改变原 $g$ 或非线性能量。添加 H2 与对角均衡后，`cholesky_banded(overwrite_ab=True)` 原位消费该 band，且实际检查返回因子与原 band 的首地址相同。若要增加 lambda，必须重新装原完整 Gram；不能把已分解矩阵当原 normal。完成物理/正则 normal 检查后释放 band 才做候选场观察。原始 `J/J^T` 闭包也在独立观察前释放。

## 已执行的有限非零核

实际 fixture 有 121 个非零未知数、2304 个物理残差行、两个 quintic 内三重结点。它独立装 dense Cartesian Jacobian 和 dense H2 矩阵，并与 band 解比较。自然 exit 0；全部检查通过。

- `raw_complete_Gram_logical_bytes_equal`：`True`。
- `retry_direction_relative_error`：`3.0013573292227054e-15`。
- `H2_band_relative_error`：`1.2646915807764667e-15`。
- `H2_operator_relative_error`：`1.5132338075970495e-15`。
- `actual_regularized_normal_relative_error`：`1.677675409351502e-15`。
- `dense_to_banded_physical_direction_relative_error`：`1.3012170649462484e-14`。
- `minimum_H2_eigenvalue`：`6.174275655133393`。
- `nonzero_off_channel_Gram_fraction`：`0.789522012375087`。

第一次 lambda 为 0.0003，第二次真实重新装 Gram 后使用 0.003。第一次、重试两次均检查原位因子指针；没有靠抽掉 cross-channel 降低内存。此 fixture 只证明这组完整非零 C2 数据上的实现一致性，不当作 107456 列 M12 整片返回、实际内存峰值或收敛证明。

## 实际身份与复现

- `2ecf-m12-complete-gram-assembly-only.py` SHA256 `63e7e92d774919dbf4970ac7c1f27eec990fc5cf9b63237c2f6cd7574b05be86`。
- `2ecf-m12-h2-inplace-direct-lm.py` SHA256 `771daeed3f56303b87d79323c0d04fdb9627a32c72d1dfa43d739adf9cfb27a1`。
- `2ecf-m12-h2-c2-inplace-lm.py` SHA256 `87d91356ba848679c18f95fa66d9070213593c1618bd6e8f5a20e96ee94aa254`。
- `2ecf-m12-h2-inplace-cached-lm.py` SHA256 `df9ef82c58173ec84a2a425ea457218355420d16e4ccf4c66527518a7912d3da`。
- `2ecf-m12-h2-inplace-c2-fixture.py` SHA256 `148df1d97e1885a6cd305991655a5e7e8d9532cc8edc01e1f43b351aef7e8b09`。
- 实际回执 `h2-inplace-c2-fixture-final.json` SHA256 `dedf4decb44dd4f1cb1f51ac78a31fc38fd4503a2c7d76780a4aaf2c61e49330`；全程 0.553897342 秒，实际 exit 0。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python scripts/2ecf-m12-h2-inplace-c2-fixture.py --scripts scripts --out /tmp/m12-inplace-fixture.json
```

新的 C2 adapter 仍逐 SHA 绑定原 exact Boehm transfer、同源报告、同 grid 与场；缓存入口仍采用已实际验证的相同角值 trig cache 和只读 source packet 的逐字磁盘核，返还新数组。失败进程遗留的 244 个 packet 未被本次重试复用。G12 重试从完全相同 `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61` 暖场开始，原数学目标、空间、参数和时间范围不变；启动并不等于已成功或已收敛。
