# 完整 actual DN 的 CSR-before-QR／factor mmap 来源入口

## 结论范围

旧 `prefix_actual_dn_qr_driver.py` 的 BASE 是匿名 CSR 的 checkpoint driver。
R87 的真实 $\lambda=.032,M=24$ 续算已经使用完整 CSR-before-QR 与全部 QR
因子的映射存储返回。这里将这条已有真实返回的资源链接到独立的完整 actual DN
入口。它保留原 native4、chord3、最多八轮 outer、全部未知、原完整残差与验收门。

这条记录是**新入口准备与真实旧执行日志核验**。没有执行新的 BVP、native
请求、Jacobian 分解或 $\lambda=1$ actual DN；没有拿旧 design 返回冒充新
wrapper 的正向返回，也没有重做旧 R90 的完整尾证书。

四个旧 QR 文件逐字节保持原 SHA。旧 schema、旧 reader、旧 source kind
均未改写。新 reader 不允许用新标签接纳旧匿名 CSR 执行。

## 四个独立入口

| 文件 | 职责 |
|---|---|
| `tail/prefix_actual_dn_mapped_qr_driver.py` | 真实执行完整 mapped prefix stack，绑定原 portable argv、外层 mapped argv、原 QR argv、所有实际返回与资源 sidecar |
| `tail/continue_original_actual_dn_mapped_qr.py` | 从真正接受的 R53 $\lambda=1$ design 输入调用原 native4/chord3/8outer；保留最终 physical-endpoint H 包与 raw H 的区别 |
| `tail/mapped_qr_actual_coupled_prefix.py` | 严格读取新真实来源；核完整数学门、实际映射执行和最终 physical H；提供与旧 reader 相同的四元组 API |
| `tail/run_lambda_one_actual_dn_mapped_qr.py` | 只从终态 controller summary 的真实 `result.run` 解析最终 design，再启动上述 coordinator |

这里 `tail/` 均指 `scripts/resume_20261128/tail/`。

新字面身份为：

```text
coordinator schema:
original-lambda-one-native4-chord3-outer8-prefix-mapped-qr-v1

prefix execution schema:
original-actual-dn-complete-prefix-mapped-qr-execution-v1

source kind:
actual_lambda_one_mapped_qr_chord_final_physical_height

execution backend:
complete_original_prefix_CSR_before_QR_and_all_factors_mmap_V5_checkpoints
```

reader 的 API 保持：

```python
accepted_coupled(source_run, coupling_summary)
# -> record, physical, binding, provenance

load_coupled_prefix(source_run, coupling_summary, *,
                    side_modes=None, center_width=.04)
# -> record, prefix, binding
```

它还显式导出 `SCHEMA` 与 `SOURCE_KIND`，供独立固定度量入口按真实来源选择
provider。新 mapped anchor 不能直接套旧 anchor 连续几何表的 source kind；
同一最终度量的后继可由实际 own-fixed 返回进入已有 own-fixed 证书链。

## 实际资源链和未改变的科学门

调用链为：

```text
prefix_actual_dn_mapped_qr_driver
  -> design/prefix_csr_prefactor_qr_driver
  -> prefix_block_qr_driver_v3
  -> design/prefix_mapped_chord_checkpoint_driver
  -> design/prefix_csr_prefactor_budget_driver
  -> 原完整 CSR assembly / V5 / portable / original domain Newton
```

仅替换 BASE 并不足以得到完整 CSR 映射，因此新入口同时选择外层
`prefix_csr_prefactor_qr_driver` 和 mapped checkpoint BASE。原完整 CSR 数值
及原 QR／求解／残差过程仍由原实现完成。新的默认径向 block 为 8；RAM 与
映射磁盘各留 512 MiB 外部余量。完整 CSR 的组装峰、全部 warm-solve
CSR／factor 驻留仍计入预算，映射逻辑字节不作为额外 RSS 抵扣。

实际 trace 必须表明每个完整 factor 有自己的预组装 RAM／disk 许可、映射
后递归 QR RAM 许可、完整 factor 返回及完整 solve 返回；两份干净映射
store 在原 solve 返回后都付页释放条件。分解计数、原 QR solve 计数与 mapped
solve 计数必须一致。资源日志不是数学验收；最终仍由原完整非线性、physical
boundary、metric、full-H fresh J、height J 和 audit 门决定。

未将 prefix QR 冒充 native full J，也未把 native 矩阵改成这个 prefix
映射实现。全部原 worker/native/config/source hash 与原完整 H 包仍独立绑定。
记录保留原 portable command，并另存真实 wrapper argv；保留历史参数名
`--streamed-rhs-block` 只是 CLI 相容，不声称执行过旧 streamed/SuperLU。

## 本次实际核验

小记录见同名 JSON，亦保存在 scratch：
`held10-tail-preparation/mapped-qr-actual-dn-entry-20261128/preparation.json`。
两处 JSON 字节相同，SHA256 为
`31aec6712f7bc0c7ad9c1de25606f364d2ed4aaf05e15bee65964faec6503bf3`。

- 四个新源实际 `py_compile` 通过。
- 三个有 CLI 的新源实际 `--help` 返回 0；reader 通过实际导入及 API／coordinator
  SHA 核验。没有伪造 reader 正向输入。
- 新 `check_mapped_trace` 与 `check_prefactor_trace` 实际只读核验了
  `R87-strict-lambda032-M24-mapped-recovery-20261128` 的真实终态日志：
  2 次完整 factor、4 次完整 solve、2 个完整预组装许可均匹配。
  mapped trace SHA256 为
  `919991376d2d0772bc34f6c232b9e7d4dfe5d32c64dfba50ff942d4bd4d2ee4d`。
- 原 coordinator 的 native4／完整 scope／chord3／warmup／原 portable 参数块，
  最终 physical-H 绑定／原 accepted 结果块，以及 reader 的全部 native/config/
  数学门／完整 raw、physical、H、J、mean、packet 块和实际 Cartesian 构造块，
  都与冻结旧 QR 源逐字节相同。JSON 保存每个块的边界、字节数及 SHA。

真实日志仅证明已返回的 design 链使用了这些资源与执行记录；它不证明尚未
执行的新 DN wrapper 已成功，也不把前缀收敛等同完整闭图完成。

## 最终真实来源到达后的调用

`ACTUAL_DESIGN_SUMMARY` 必须是当前唯一 controller 真正返回的 summary，且
`status=declared_finite_design_stages_passed`、`result.accepted_lambda=1`。
launcher 从该文件读取实际 `result.run`，核全部原接受门和完整 port/config
身份；不猜 attempt 编号、不改 q、不降模。

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/run_lambda_one_actual_dn_mapped_qr.py run \
  --repo /workspace/scratch/7c4e33ee17de/math-research-public \
  --work /workspace/scratch/7c4e33ee17de/held10-design-work \
  --design-summary "$ACTUAL_DESIGN_SUMMARY" \
  --outdir "$NEW_ACTUAL_DN_DIRECTORY" \
  --rhs-block 8
```

输出目录须全新且位于该 work 内。真实 $\lambda=1$、完整 original DN、同一
最终 $g$ 的精化、连续全域几何／metric 与完成标准仍须继续实付。
