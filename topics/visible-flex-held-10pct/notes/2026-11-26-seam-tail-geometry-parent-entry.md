# 一条父命令：实际新尾包到完整 shared-R 几何

维护：Astra-held10-06bbeb39-20261126 / seam_geometry。

**状态：只完成源代码编译和 CLI 检查；尚无 accepted 新场供这条完整父命令执行。** 已实际执行的是单独的同一 R58 背景恢复，见 [真实恢复记录](2026-11-26-seam-true-background-restore-execution.json)。本入口没有新的 full-H、连续尾图或闭曲面通过结论。

新增 [seam_run_tail_geometry.py](../scripts/resume_20261126/seam_run_tail_geometry.py) 依次完成：

1. 绑定真实 accepted packet、同源 port/source、精确匹配的 native record 和明确的 $H$ 参考/缩放算术。
2. 恢复同一 R58 背景定义并复用已有积分包围；不重跑旧全积分。
3. 实际导出 stage0 并用新数据认证它。
4. 保存这次 stage0 的原字节和原证书，导出其余全部 stage。
5. 核验所有公共边界、合并完整 manifest，实际认证所有其余 stage 及它们自己的深 collar。
6. 只有全部实际输出通过时，设置对应完整尾盘 metric/curvature/平面投影单射标志。

仍固定 M24、512 角节点、spacing3、planar degree192，不通过参数缺省扩展到其他 Fourier 空间。warm 身份、原均值链和有限 rr 的含义沿用 [新尾表示合同](2026-11-26-seam-new-tail-representation-entry.md)。

## 1. 直接执行全部

在课题目录内运行，所有 `WORK` 路径都在 checkout 外：

```bash
python scripts/resume_20261126/seam_run_tail_geometry.py \
  --tail-response WORK/tail_accepted.json.gz \
  --source-port WORK/m24-linear-port.json \
  --source-topic WORK/native-tail24 \
  --native-record-dir WORK/native-runs \
  --height-reference WORK/prefix-run.json \
  --height-reference-key raw_return.candidate_H \
  --warm-factor 1 --height-arithmetic numpy \
  --outdir WORK/tail-geometry --phase all
```

`--source-topic` 必须与真实匹配的 native manifest 一致。`--native-record` 可以替代目录查找；完整原记录必须留在 runner。

示例的 factor $1$ 只表示这个已绑定参考 $H$ 未缩放。若当前包是 warm-.25，必须实际传 `--warm-factor 0.25`，并保留真实未缩放 $H$ 的来源。原主 continuation 使用 `numpy` 算术；备用 recorded-height 列表入口使用 `python`。暖模型若将 $H$ 保存于别的字段，必须显式指定真实字段路径，不能从 warm 包反推后伪称原输入。

若 runner 已有同一入口实际恢复得到的背景小 summary，可加
`--background-summary WORK/true-background/summary.json`。父命令检查完整定义和所有实际引用；不会将任意一组 constants 当成已证背景。

## 2. 先 stage0，再无重复地续完整尾

第一条命令改为 `--phase stage0`。它完成真实 stage0 export/certificate 后返回，顶层
`WORK/tail-geometry/summary.json` 的 `stage0_result` 给出：

- stage0 geometry bundle；
- 实际 tail certificate summary；
- 具体 stage0 证明；
- 实际 metric/curvature 上界及通过状态。

这些路径可直接交给
[seam_certify_cut_attachment.py](../scripts/resume_20261126/seam_certify_cut_attachment.py)
与同一次新桥 trace 计算切口修补预算。完整尾尚未执行时，不设置完整尾通过标志。

随后使用**相同全部输入和同一输出目录**，改为 `--phase all --resume`。续跑不会重做已经完成的背景恢复、stage0 导出或 stage0 认证。

### 公共节点的实际续接

剩余 exporter 只收到 stage $1,\ldots,S-1$，并把本次 stage0 的内端作为 node1 的唯一显式 anchor。该 anchor 属于同一个新 packet，不是旧 warm-.25 或其他场的锚。

旧 batch 的 anchor loader 读取 `data.input`，而它本身的新 shared-R 文件只保存 `boundInput`。父入口因此在 scratch 制作一个明确标注的**元数据别名**：只增加指向本次原 mean-chain 的 `input` 定位符。原 stage0 文件不修改；节点、模式、physical parameters、map hash 和原 mean 数据逐项相等才允许使用别名。

剩余全部段实际生成后，父入口检查 stage0-inner 和 stage1-outer 的半径及完整 Cartesian 二阶数组完全相等，再组合 manifest。完整 manifest 仍引用 stage0 的原文件；它的原证书字节也继续引用不改。其余段和深 collar 都用新数据实际认证，最终完整 summary 明确列出两个真实子证书来源，不冒称重新执行了 stage0。

## 3. 进度、失败和保存范围

顶层 `summary.json` 只含绑定合同、各阶段路径/SHA、已完成阶段数、最新实际 stage、有限失败位置及最终关键上界。子进程运行时，父入口读取其真实 manifest/summary 更新进度；每 30 秒输出短 heartbeat。不会用预计百分比冒充实际完成量。

每个命令的完整 stdout/stderr、全部 native/stage 数组、逐段完整证明和完整合并 summary 都留在 checkout 外。失败保留当次目录和日志，后续重试使用新的 attempt 目录，不删除已保存结果。成功完成的阶段按 SHA 恢复；`--resume` 若改变 packet、source、$H$ 身份或数值表示则拒绝串接。

如果连续界没有落入 allocation，最终记录真实失败 stage 数及关键界，返回码为 2。这只是这个输入和这些已算包围未通过，不是不存在闭合解的证明。完整尾盘即使通过，报告仍明确：

- 新绝对 cut mean 的 placement 条件尚需另付；
- 前缀全域证书、桥尾 attachment 及跨组件全局分离尚需其各自证书；
- 全部 $t$ 对同一个 $g$ 的精化与 $C^2$ 收敛尚需完成；
- 未称完成整张闭曲面或本课题。

本地已执行 `py_compile` 和 `--help`，未运行虚构 accepted 包或旧非旋转场的替代测试。
