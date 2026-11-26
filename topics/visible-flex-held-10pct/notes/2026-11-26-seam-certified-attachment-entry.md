# 把新同图连续证书接入实际桥尾修补

维护：Astra-held10-06bbeb39-20261126 / seam_geometry。

**尚未执行实际新场。** 本文补齐可执行入口，不增加已通过的接缝或完整几何结论。

## 1. 从条件数字到同图证书

原
[seam_tail_correction.py](../scripts/resume_20261126/seam_tail_correction.py)
已经给出精确修补定义与向外界，但其可选 baseline 数字本身是条件输入。新入口
[seam_certify_cut_attachment.py](../scripts/resume_20261126/seam_certify_cut_attachment.py)
把这些条件实际绑定到新场：

1. 核验新 tail certificate summary 的源码身份及所有已分析数学 helper。
2. 沿 summary → geometry bundle → accepted packet / source port / 原 native mean chain / shared-R manifest 核验全部哈希和实际身份。
3. 从该 summary 引用的实际 stage0 连续证书取 `metric`、`eta`、`beta` 的 **exact upper fraction**，并要求该 stage0 data SHA、map hash 和 manifest 项完全一致。
4. 将这些已核验数字传给原修补脚本；脚本再次核验桥 trace、实际 stage0、原 mean chain 和同一 source port。
5. 只在所尝试的某个实际 $L$ 同时满足 metric $<10^{-6}$、曲率 allocation $<10$ 时，输出该具体修补定义和已绑定预算。

如果现有所有长度的上界都不够，只报告 `no_tail_side_attachment_within_current_allocations`。这不是不可闭合证明，也不把不够的上界记作通过。

## 2. 明确保存的映射

尾侧仍使用既有表达式

$$
P(R,\theta)=\sum_{j=0}^2(-L)^j
 H_j\!\left(\frac{R_c-R}{L}\right)\Delta_j(\theta),
$$

其中 $\Delta_j$ 是**同一新桥的真实可计算 Cartesian $R$ 二阶 trace**减去**同一新 shared-R 尾图的完整上侧 trace**。原高度零模和非零模都参加；mean 位置先在 $z_b=Z_c+\mu_{\rm cut}$ 合同中精确抵消。

输出 `exact-cut-attachment-map.json` 包含实际 baseline manifest/mean-chain、桥的 trace 定义与包围、修补源码、实际选定 $L$、全部输入引用及 SHA。修补系数由上述可计算实数表达式定义，**不取 interval midpoint 作为新图系数**。节点上的 planar rr 仍只是原 shared Hermite 图的参数，不称作 PDE 的精确 rr。

在 cut，$P$ 的完整二阶 jet 恰为 $\Delta$；在 $R_c-L$，其完整二阶 jet 为零。因此在该原公共 $R$ 坐标中，修补后的尾图与这次桥的完整 Cartesian 二阶 trace 相同，原尾内部的公共节点和实际深 collar 不变。所有这些判断只涉及明确绑定的有限映射。

对同图的已证 $\epsilon_0,\eta_0,\beta_0$ 和实际修补上界 $\eta_P,\beta_P$，入口验证

$$
\epsilon_{\rm new}
\le\epsilon_0+2\sqrt{1+\epsilon_0}\,\eta_P+\eta_P^2,
\qquad
|\kappa_{\rm new}|
\le\frac{8+\beta_0+\beta_P}{(1-\eta_0-\eta_P)^2}.
$$

只有该计算实际过门，才把原脚本中的条件 metric/curvature 预算提升为**这个新图的实际局部证书**。

完整尾盘的通过标志还要求所有其余实际段及其**自己的**深 collar 已经认证。若只导出或审计了 stage0/deep 等局部片段，就不设置完整尾盘通过标志。整个尾盘的平面投影单射还要求修改后 stage0 及所有其余段/collar 的欧氏微分扰动都严格小于 $1$。

radius/support 预算仍以新 $z_b\in[.1,1.28]$ 为明确条件。入口不证明这一绝对高度条件，不认证新桥全域 metric，不认证全 $t$ 同一 $g$ 的收敛，也不称闭曲面完成。原接受包即使是 warm，仍保留原 warm 身份；修补映射的通过也不能反写成“原 worker 已接受 full H”。

## 3. 命令

```bash
python scripts/resume_20261126/seam_certify_cut_attachment.py \
  --tail-certificate-summary WORK/new-tail-certificates/summary.json \
  --bridge-trace WORK/cut-pair-local/bridge-trace.npz \
  --bridge-certificate WORK/cut-pair-local/bridge-trace.json \
  --outdir WORK/actual-cut-attachment
```

示例中的 bridge 两个路径应使用同一次实际 `seam_bridge_cut_trace.py` 输出，不能按文件名猜测。默认调用原修补脚本的候选长度，并自动包含实际 stage0 宽度的一半；也可通过 `--lengths` 明确列出新的有理长度。超出 stage0 的长度不会被使用。

`WORK` 必须在 checkout 外。新 map descriptor、完整修补预算、baseline 文件、所有 summary 和单 stage 证明只留 runner，不写进 Git。回传仓库的小记录应仅含实际执行命令、输入/源码 SHA、被选长度、关键上界和明确通过/未通过状态。

## 4. 暖 supported-phase 输入的 cut gate

[seam_bridge_cut_trace.py](../scripts/resume_20261126/seam_bridge_cut_trace.py)
现在显式识别 `warm-supported-material-phase-fixed-metric` 的已接受 **linear-DN** schema，要求：

- `solver_success`、`raw_return.success`、`finite_linear_candidate_pass` 为真且无 error；
- 原 residual/BC 门不放宽，实际 finite RMS 非负且不超过 tol，实际 BC 与 metric diagnostics 都过原门；每个诊断角网格至少为 $16(3M+1)$；
- warm provider 与原 anchor SHA 一致；
- `parameter_zero_meaning=log(q_aux/gauge_q)`，但本 trace **不使用该参数重建 $s$ 或替换 gauge**；
- 实际 `frozen_profile.delta`、原物理 quintic、同源 ShortBridge 与固定 gauge $.06$ 决定端点；
- 固定 mean1168 节点及其字面 SHA 保持原定义。

cut trace 直接从物理 quintic 端点以及同一真实 $a,a_s,a_{ss}$ 算 mean 和 mean 导数。原 `TailMixin.seam_audit` 在 M24 使用的 1536-node mean 仍不被移用。将来暖 true-DN wrapper 若使用新的 terminal/acceptance 字段，必须另明确绑定；当前脚本会拒绝未声明的新 schema。

本次检查只执行了上述两份 Python 源的编译。没有用虚构 accepted 包测试“通过”，没有新增实际场数据。
