# 真 QR 固定度量后继的独立完整尾生成入口

新文件 `scripts/resume_20261128/tail/qr_fixed_complete_tail_geometry_chunks.py`，SHA256 `8cb073f0f30e37fbe7926c5fd0f51d6a9b8c0c238a51bdeca1da7c42eddbefb3`。本条补齐实际 fixed-QR reader 与完整 tail bundle 之间的来源缺口；不是新的数值场或几何证书。

已发布 `qr_complete_tail_geometry_chunks.py` 接受的是原 QR/native4/chord3/8outer anchor。新 fixed-g 返回不能换成该 schema。新入口先调用 `qr_fixed_actual_cartesian_prefix.accepted_fixed`，保留 own KIND、完整 `fixed_problem`、实际固定 profile、最终 saved physical endpoint-H、各自真实 runtime/baseline/port/native manifest；之后才加载几何 provider。

程序直接复用已冻结 chunk factory（SHA `0bc3a31e348a5885b45ae082486aa470d39693684d3960bcd3ead61cc35fd5ee`）和原 `seam_run_tail_geometry_v2`（SHA `c165678d912761163ef29cfca1eb9c4dfc4bbf3102de6a00b228ca537f727615`），没有复制或覆写其数学算法。真实 native record 目录取自本次已接受 runtime 的 `traceFile` 所在目录下的 `native-runs`，不借 anchor 的旧 H 或旧 state。

跨 frozen tree 时，chunk 源、原 pipeline、Node exporter 和 Python/Node guard 都必须存在于该真实原树、与已审当前源码逐字同，并且实际导入路径一致。新独立入口自身在当前树。这保留实际执行路径和来源合同，避免用当前树的 exporter 却在汇总中记录另一棵树。

原流程依次完成新 stage0、全 mean 链、全谱、全部剩余段、小批共同两阶 jet 拼接、完整 index、原全部逐段证书与深 collar。保留默认每批 8 段、允许 1–16 段、Node heap 至少 256MiB、逐次写入至少 128MiB 的原资源门；resume 只接受本次完整 source contract 未变和真实已落盘内容。原 stage0 已完成后可从同目录继续，不重算它。原 K<10 或 metric 分配失败仍是原来的真实失败门，不由新入口改成通过。

所有引用和 metadata 明示 own fixed source。底层 chunk factory 保留的 `actual_QR_physical_height_source` 状态键内装的是这次新的完整 fixed contract，其 schema 和 source_kind 明确区分实际 own 返回与设计 anchor；没有修改原数值 run 或伪造原 coupling summary。

## 真返回后的执行

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/qr_fixed_complete_tail_geometry_chunks.py \
  --source-run "$ACTUAL_ACCEPTED_QR_FIXED_RUN" \
  --outdir "$NEW_FIXED_TAIL_GEOMETRY_DIRECTORY" \
  --phase all --chunk-stages 8 --node-heap-mib 512 --disk-reserve-mib 128
```

若需先付实际 cut 的 stage0，可用同命令的 `--phase stage0`，随后同目录加 `--phase all --resume`。`--background-summary` 只能引用其原完整物理定义验证实际接受的背景结果，不会将旧低 λ 场的扰动或证书带入新场。

## 实际检查

当前源 `py_compile` 与 `--help` 均真实 exit0；静态核查确认 own accepted gate 在几何导入之前、直接调用原 chunk factory，且没有新增或覆写任何数学 class。最终小记录 SHA256 `6693d6e7d2713047b1cbc6e2e171bfd579c5c3046a96f2d780bfcb131637beb7`，本 note 同名 JSON 保存实际检查结果。

尚无真实已接受 fixed-QR 输入，因此没有执行正向 source gate、native/几何导出或区间计算。既有真 QR anchor 仍使用其自己的已发布入口；此新入口只供真正 own fixed 返回使用。原证据、全谱、均值和全部两阶 jet 门不变。
