# run02 实际成功后的同图生产链

2026-11-10，Astra-visible-flex-78718bd0 / numerical_recovery。
**状态：按现存源码逐项核对的条件执行清单；当前尚无 run02 成功 CP，
以下导出和连续后端均未执行。** 本文不增加数学验收门，也不把首 DN
或参数预检称为成功候选。

## 1. 真实入口与固定输入

当前主运行是新环境的 `2026-11-10-78718-numerical-m14-direct-csc-02`。
root 持有 session 44394，开始回执 00aa17；仍须取得它自己的自然退出、
完整 reproduction/CP/PP/末次 DN/outer/seam，并运行冻结 final auditor。
必须先由真实 root 退出观察支付原 `--observed-execution`，再采用该次
`PASS_ROOT_OBSERVED_TRUE_M14_W14_DIRECT_CSC_FINITE_COUPLED_CLOSE`。
下列路径中的 `-02` 不能被另一次成功首包替代。

```sh
VF_REPO=/workspace/scratch/78718bd0c4a9/math-research
VF_T="$VF_REPO/topics/visible-flexible-closed-surface"
VF_S="$VF_T/scripts"
VF_N="$VF_T/notes"
VF_PY=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
VF_SRC="$VF_T/repro/source-root"
VF_OLD=/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface
VF_PCP="$VF_OLD/notes/2026-11-10-78718-numerical-m14-direct-csc-02.json.gz"
VF_PORT="$VF_OLD/notes/2026-11-09-950f-prefix-weighted-k6-port96-cusp1024.json"
VF_RUN="$VF_N/2026-11-10-78718-numerical-closed-m14-01"
VF_OLD_TAIL="$VF_N/2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json"
VF_BG_K="$VF_N/2026-11-09-db6f-audit-tail-tight-final-packet.json"
VF_BG_E="$VF_N/2026-11-09-db6f-audit-tail-lowmetric-final-packet.json"
VF_BG_H="$VF_N/2026-11-09-db6f-tail-background-height-rigorous.json"
VF_BG_A="$VF_N/2026-11-09-db6f-audit-positive-radial-alpha.json"
VF_CAL="$VF_N/2026-11-09-db6f-tail-finite-source-calibrations.json"
VF_ALPHA="$VF_N/2026-11-09-db6f-tail-tight-alpha.json"
cd "$VF_REPO"
```

生产链使用当前仓库已核过的原通用源码与 source-root；原求解身份仍明确
属于新环境重建的旧绝对目录。当前源码不能伪记为旧求解的运行路径。
原 CP 和其分片闭合后可逐字另存当前 checkout，以便 git 提交；不改写其
嵌入的旧路径或声称它属于另一次执行。

`VF_TCP` 应从真实 `VF_PCP` 的 `tail_seam.tail_record` 解析：若为相对
文件名，以 CP 所在目录为基准；先核该文件真实存在及末审绑定。
它不是 prefix CP，也不是本轮首 `tail_0001` 的预填别名。
输出目录须全新且不存在。下列 `node` 指当前已核 Node v24.22.1；正式
运行记录仍保存实际 `command -v node` 的绝对解释器位置。

固定背景已实际取齐并核原散列：

| 变量 | `$VF_N/` 下文件 |
|---|---|
| `VF_OLD_TAIL` | `2026-11-09-db6f-tail-int2-flat17-m8-q10-n8-s32-manifest.json` |
| `VF_BG_K` | `2026-11-09-db6f-audit-tail-tight-final-packet.json` |
| `VF_BG_E` | `2026-11-09-db6f-audit-tail-lowmetric-final-packet.json` |
| `VF_BG_H` | `2026-11-09-db6f-tail-background-height-rigorous.json` |
| `VF_BG_A` | `2026-11-09-db6f-audit-positive-radial-alpha.json` |
| `VF_CAL` | `2026-11-09-db6f-tail-finite-source-calibrations.json` |
| `VF_ALPHA` | `2026-11-09-db6f-tail-tight-alpha.json` |

这些变量只指同一个冻结背景的证明输入。8 个 M8 raw 分片、两 NPZ、
六定义及 bookkeeping 的闭合来源在本轮 `numerical-m8-background-inputs`
和 `numerical-fixed-proof-preflight` 报告中。producer 和 consumer 的
首 DN 参数预检各两条均已实际退出 0；它们不生成正式转包。

## 2. 先看原成功对象的实际误差

读该 CP 的原物理 residual、BC、保存 PPoly 的 metric 诊断及自己最后
尾 audit。若新源诊断仍明显未达到原目标，先定位实际误差来源；不能期待
连续验证把真实超标图改小。RMS/normalized residual、source metric 和
最终有限 Hermite 图的全域 metric 是不同量。

本轮初档沿用已审入口：M14/N512/native P8×S32；尾导出 depth8、degree192；
prefix 保留已有 Cartesian M24、angular768、mean quadrature8、subdivide1。
保留 M24 不代表 source M14 有24个未知模。全部均为同一冻结物理 g 的
数值表示选择；后端须认证由它们定义的实际新图。

**文件大小的实际分支：** 原 prefix producer 在写 gzip 后才检查 5MB。
后续可用纯资源包装 `78718-run-file-cap.py --` 执行原命令，将该进程
RLIMIT_FSIZE 限为4,999,999字节；单件写入一旦超过就自然失败，不能记为
完整图。原参数、源码及数据运算不变。两例1KB合成写入已实际核过
（工具ccc85e退出0，报告 `numerical-file-cap-check`）；这不新增数学门，
也不限制总磁盘或预存文件，未用于运行中的主 solver。

仅当实际单容器超限，才启用无损字节分片：保留 M24、原节点和全部值，
优先保存该真实逻辑容器以避免重做数学计算，完整记录格式身份，并补齐
生产/消费者源码恢复及所需独审。本轮尚未恢复 A/B 原执行源，C 为已审
静态恢复文本，不能预称该分支已可执行或已生成新图。当前已有的尾
exporter 本来就分片，不应为了统一包装重复它的数学计算。

## 3. 本次尾和自己的 collar

```sh
node --max-old-space-size=1536 "$VF_S/db6f-prefix-endpoint-critical-increment-export.mjs" \
  "$VF_TCP" "$VF_RUN/tail" --source-root "$VF_SRC" \
  --depth 8 --steps 32 --flow-steps 32 --angular-nodes 512 --degree 192 \
  --grid critical --critical-cells 0 --critical-base-steps 64 \
  --critical-ratio .05 --endpoint-ratio .025 --difference-step .00005 \
  --audit-angular-nodes 128 --audit-fractions .25,.5,.75
"$VF_PY" "$VF_S/db6f-tail-collar-exact-check.py" \
  "$VF_RUN/tail-collar.json" "$VF_RUN/tail-collar-check.json"
"$VF_PY" "$VF_S/db6f-tail-first-bounds-stream.py" \
  "$VF_RUN/tail-manifest.json" "$VF_RUN/tail-first.json" --batch 128
```

先核 exporter 自然退出、manifest.finished、全部分片 SHA/尺寸/共享行、
完整 C3 模式、正增量和精确归一恒等式，以及它自己的 collar 已写完。
M14/degree192 为143系数、stride575；每片1000原始行4,600,000字节。
实际仍逐件核小于5MB，数据超过1MB gzip。表示节点改变局部重新积分路径，
不能叫严格纯插值，也不能把它计成原生 S64 联解。

## 4. 基础 prefix、自己的目标、桥和共同 cut

原单文件支路可用时，实际命令为：

```sh
"$VF_PY" "$VF_S/78718-run-file-cap.py" -- \
  "$VF_PY" "$VF_S/db6f-root-mirror-hermite.py" \
  --source-root "$VF_SRC" --checkpoint "$VF_PCP" --linear-port "$VF_PORT" \
  --out-prefix "$VF_RUN/prefix-base" --modes 24 --angular 768 \
  --quadrature 8 --subdivide 1 --ell 0
"$VF_PY" "$VF_S/db6f-audit-metric-supplier.py" \
  --geometry "$VF_RUN/prefix-base.json" --source-root "$VF_SRC" \
  --out-prefix "$VF_RUN/prefix-target"
"$VF_PY" "$VF_S/db6f-audit-metric-polynomial.py" \
  --geometry "$VF_RUN/prefix-base.json" --target "$VF_RUN/prefix-target.json" \
  --out "$VF_RUN/prefix-base-metric.json"
"$VF_PY" "$VF_S/db6f-root-exact-bridge.py" \
  --geometry "$VF_RUN/prefix-base.json" --target "$VF_RUN/prefix-target.json" \
  --tail-manifest "$VF_RUN/tail-manifest.json" \
  --metric-certificate "$VF_RUN/prefix-base-metric.json" --out "$VF_RUN/bridge.json"
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" make \
  --geometry "$VF_RUN/prefix-base.json" --tail "$VF_RUN/tail-manifest.json" \
  --bridge "$VF_RUN/bridge.json" --width .15 --out "$VF_RUN/closed-map.json"
```

桥的当前 CLI 必须消费基础图 metric 报告；共同图报告不能冒充它。
common-cut 会从实际尾所有 signed modes 扩充柱模，degree192 至少要64，
不能省掉新增槽。镜像两 jet、共享 mean increments、自己的 cut 修正和
实际宽度全部保留。旧 M12 的 eta 可供风险判断，不能代替本次桥身份。

## 5. 新共同图连续前缀证书

```sh
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" geometry \
  --geometry "$VF_RUN/closed-map.json" --angular 256 --radial 1 \
  --out "$VF_RUN/prefix-geometry.json"
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" metric \
  --geometry "$VF_RUN/closed-map.json" --target "$VF_RUN/prefix-target.json" \
  --out "$VF_RUN/prefix-baseline-metric.json"
"$VF_PY" "$VF_S/db6f-root-common-cut-v2.py" moment \
  --geometry "$VF_RUN/closed-map.json" --angular 512 --radial 1 \
  --out "$VF_RUN/prefix-moment.json"
```

用精确 Fraction 比较本次 baseline 的 `epsilon*(1+eta)+eta` 与
`1/500000000`。若已经通过，`VF_PREFIX_METRIC` 即该 baseline，停止额外
角细分；若未过，先按新报告自己的 worst_interval 做原128弧/depth4
局部诊断。确认是可改善的角过估计后再完整运行：

```sh
"$VF_PY" "$VF_S/db6f-audit-prefix-angular-metric.py" \
  --geometry "$VF_RUN/closed-map.json" --target "$VF_RUN/prefix-target.json" \
  --baseline "$VF_RUN/prefix-baseline-metric.json" --bridge "$VF_RUN/bridge.json" \
  --budget 2e-9 --initial-arcs 128 --max-depth 4 \
  --out "$VF_RUN/prefix-angular-metric.json"
```

最终必须完整覆盖；不得拿 `--intervals` 输出作 `VF_PREFIX_METRIC`。
该变量选本次实际通过的 baseline 或完整 angular 输出。common-cut 的
`metric` 分支不消费 `--angular/--radial`，调这两旗标不能收紧 metric。
closed-budget 读取源目标上界后转移一次，不重转已转移字段。

## 6. 固定背景换到新网格，新扰动自己的全尾界

```sh
"$VF_PY" "$VF_S/db6f-tail-transfer-background-v3.py" \
  --old-manifest "$VF_OLD_TAIL" --packet "$VF_BG_K" \
  --new-manifest "$VF_RUN/tail-manifest.json" --out-prefix "$VF_RUN/background-k"
"$VF_PY" "$VF_S/db6f-tail-transfer-background-v3.py" \
  --old-manifest "$VF_OLD_TAIL" --packet "$VF_BG_E" \
  --new-manifest "$VF_RUN/tail-manifest.json" --out-prefix "$VF_RUN/background-e"
"$VF_PY" "$VF_S/db6f-audit-tail-stream.py" \
  --manifest "$VF_RUN/tail-manifest.json" --packet "$VF_RUN/background-k.json" \
  --angular 128 --radial 1 --background-curvature 6 --direct-threshold 8.5 \
  --block-size 128 --out "$VF_RUN/tail-full.json"
"$VF_PY" "$VF_S/db6f-audit-tail-metric-only.py" \
  --manifest "$VF_RUN/tail-manifest.json" --packet "$VF_RUN/background-e.json" \
  --radial 1 --block-size 128 --out "$VF_RUN/tail-metric.json"
"$VF_PY" "$VF_S/db6f-audit-complete-metric-report.py" \
  --report "$VF_RUN/tail-metric.json" --curvature-report "$VF_RUN/tail-full.json" \
  --out "$VF_RUN/tail-completeness.json"
```

这里必须走真实 `--new-manifest`，不用首 DN 参数预检充当转移。
正式区间计算不带 limit 或局部 span 选择，包含 collar(-1)和全部有限跨。
8.5是触发直接计算的算法阈值，不是提前给新图的曲率结论。
metric-only 不含曲率；只能与这份同 manifest 的实际 full 证书组合。
若 full 本身已到原 B，则不机械重复第二个后端，最终清单如实记实际支路。

## 7. 本次闭预算、原门与最终交付

```sh
"$VF_PY" "$VF_S/db6f-audit-closed-budget-transfer-v3.py" \
  --geometry "$VF_RUN/closed-map.json" --geometry-certificate "$VF_RUN/prefix-geometry.json" \
  --metric-certificate "$VF_PREFIX_METRIC" --moment-certificate "$VF_RUN/prefix-moment.json" \
  --tail-first "$VF_RUN/tail-first.json" --height "$VF_BG_H" --positive-alpha "$VF_BG_A" \
  --background-transfer "$VF_RUN/background-k.json" --out "$VF_RUN/closed-budget.json"
"$VF_PY" "$VF_S/db6f-root-whole-metric-reach-v2.py" \
  --closed-budget "$VF_RUN/closed-budget.json" --tail-certificate "$VF_RUN/tail-full.json" \
  --tail-metric-certificate "$VF_RUN/tail-metric.json" --out "$VF_RUN/whole.json"
"$VF_PY" "$VF_S/db6f-audit-terminal-error-gate.py" \
  --whole "$VF_RUN/whole.json" --prefix-target "$VF_RUN/prefix-target.json" \
  --out "$VF_RUN/terminal-error.json"
```

whole 原1e-6通过不等于末端2e-9通过。终门使用原正常候选入口，并须核
同 g 的 M12 真点下界。现已核9个固定 REFERENCE 的原散列，然而原
`reference()` 还要重哈希24份 M12 raw（合80,730,280字节）、它的原尾CP、
点包及数据。只在本次新图有望进入最后门时取回这组复核必需数据；
`numerical-final-gate-deferred-inputs.txt` 已列现有26项缺件，点包 NPZ
尚待按其真实头文件派生。不能把“无需 M12 中间转背景”说成终门完全
不读 M12 原数据。

终门通过后由同一 `closed-map.json` / `whole.json` 运行原 mesh
`plan -> db6f-tail-sample-background-height.mjs -> build`；初档沿用
angular144、prefix128、tail64、collar4、cap12。实际三个时刻
0、1/4、1/2的文件逐件运行 `db6f-audit-closed-mesh.py --batch 2048`。
独立者按原完整协议从原种子重跑候选、导出、全部实际后端与网格；
同plan字节对照不能替代这次全链重算。三网格共同面表、固定mask及
固定顶点位模式实际读回，单件小于5MB；数值高度样本不是严格顶点误差证。

完整归档以实际新产物为准；大而可重生的中间数据不自动提交。
旧 M8/M12 的数值界只作为已审固定 g 收敛对照，不能移给新图。
基础完成还需 README 其余所有门及统一 G5 账本，随后继续强目标。

## 来源

- `2026-11-09-db6f-root-final-m14-w14-entry-and-export.md`：本轮 M14 初档。
- `2026-11-09-db6f-audit-final-independent-pipeline.md`：全链实际命令与独跑边界。
- `2026-11-09-db6f-prefix-final-m15-metric-risk-order.md`：原图诊断顺序和 CLI 陷阱。
- 上述命令逐项对照当前原脚本 argparse 与输出名；这是静态接口核查，
  不是这些数学程序的新执行回执。
