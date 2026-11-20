# 新 g：λ=.004/M32 原 linear-DN 前缀实际过门

维护会话：Astra-held10-1b6d88ec-20261120。观察日期：2026-11-20 UTC。

本条接续[λ=.004/M24 的实际 metric 未门及补空间诊断](2026-11-20-m3-newg-lambda0004-m24-return.md)，
没有重算该诊断。完整参考 lift 转到 M32 后，原 BVP 和原完整前缀审计均
已真实返回；`metric_l1=7.60467686690455e-7`，通过原 `1e-6` 门。

## 1. 实际转移与求解

M24→M32 使用已发布的

\[
Y_{32}=\operatorname{embed}Y_{24}
       +a\chi(I_{32}-\operatorname{embed}I_{24}),
\]

系数为 `1`，不是材料同伦 `lambda=.004`。实际 transfer 进程返回
`exit0`；103 个径向检查点、3104 个角点上，完整参考六个二jet 分量的
最大差分别为
`[3.3437e-16,4.3467e-16,1.5544e-15,4.0854e-16,
2.0241e-15,7.5699e-15]`。这是连续参考转移的有限检查；保存的 nodal
初猜或随后新 cubic/physical quintic 不凭此被宣称逐字同图。
原 transfer 报告的这六项省略双方按同一规则共用的 mean-height 项；
它不能证明把原 mean1168 换成后续审计 mean1552 后仍是逐字同一张图。

新增八个控制仅在转移初猜中设为零。随后原 M32 设计求解仍释放
`delta` 和全部 31 个 support 控制；没有把设计延拓称为固定全部
物理参数的精化。

实际求解进程 `78016` 已观察 `exit0`。起始 635 点，最终 860 点，
五次 Newton 网格调用，共 11 个接受步；全部 `alpha=1`，域拒绝、merit
拒绝和 `no_step` 均为零。原记录在累计 `1057.169803282` 秒写出
`inner_return`，累计 `1108.137581373` 秒写出 `prefix_audit`；后两者
之差为 `50.967778091` 秒，不能把累计 1108 秒误写成额外审计耗时。

## 2. 原门与完整有限诊断

| 量 | 实际值 |
|---|---:|
| `solver_success` | true |
| 最终节点数 | 860 |
| collocation RMS max | 9.941928786103374e-7 |
| 32 条原 linear-DN physical BC max | 2.8434549427822667e-12 |
| 原完整 `metric_l1` | **7.60467686690455e-7** |
| 全未投影 `flow_defect` | 9.793278046322416e-6 |
| `darboux_l1` | .007812914610033857 |
| 原 `kappa_sample` | 8.913011526459478 |
| 原 `root_min` | .0025277796488304416 |
| 实际 `delta` | .06413456255056799 |
| 原审计角数／径向数 | 1552／1868 |

`tol=1e-6, bc_tol=1e-7, physical_bc_tol=2e-9, max_nodes=6000`
均保持。这里接受的是原有限前缀审计，未把未投影 flow defect 或 Darboux
量冒称为更强的接受结论。

同一物理输入仍为新多段 profile、原 bridge 曲率 `4`、`q=.06`、
`warp=.06`、`tau=1, S=.5, b=.2, target k=.2`；核心 `lambda=.004`。
实际 support 参数的前六项为
`[.000540145937742259,-3.6355164642353374e-5,
-5.56292600775879e-6,2.2797105865269463e-7,
2.224821088435334e-6,-3.0282193836901244e-7]`。
全部 31 项、归一参数及其缩放、最终完整 32 项 `H`、原尾物理参数和
完整 profile 均保存在随附小记录中，未以归一化大数冒充物理控制。

M32 的原审计按 `max(512,16*(3*M+1))` 使用 **mean1552**，原 GL6
高度重建不变。这个均值定义不能静默换成 M24 的 mean1168。BVP angular
为 1024；尾线性端口使用原 M32、N512（仍满足原 `N>4*M*3`）、
depth8、steps16、parts16，其物理尾参数不变。原 M24 场及 R60/R61 等
连续几何结论不自动转给这个新的场和参数。

## 3. 完整复现与来源

[精简实际执行记录](2026-11-20-m3-newg-lambda0004-m32-execution.json)
（16404 字节；SHA256
`858601a23da67204444a6ef07df247d1aa2e3d6d248e372a80b9c4dcdec93a13`）
保留实际两条完整 argv/env、全部数学参数、门、实际返回和来源哈希。
核心设置文件已经是已发布的
`scripts/resume_m3/multistage_wide_circle_lambda0p004.json`；它与本次
scratch 配置逐字相同。`W=/workspace/scratch/1b6d88ecddf3/m3-work`，
`T=/workspace/scratch/1b6d88ecddf3/math-research-public/topics/visible-flex-held-10pct`。
两条原调用为：

```bash
python -u "$T/scripts/resume_m3/prepare_lifted_mode_restart.py" \
  --source-run "$W/newg-wide-lambda0p004-m24-linear/run.json" \
  --port "$W/newg-wide-m32-port/linear-port.json" \
  --modes 32 --angular 1024 --check-angular 2048 \
  --outdir "$W/newg-wide-lambda0p004-m32-transfer"

python "$T/scripts/resume_m3/portable_prefix_continue.py" \
  --source-topic "$W/multistage-source-v2" \
  --short-bridge "$W/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --profile "$W/multistage-linear-root-profile.json" \
  --chart "$W/bootstrap/reference/chart.json" \
  --port "$W/newg-wide-m32-port/linear-port.json" \
  --raw-restart "$W/newg-wide-lambda0p004-m32-transfer/initial.npz" \
  --core-module "$T/scripts/resume_m3/material_support_factory.py" \
  --core-config "$W/newg-wide-lambda0p004-m24-config.json" \
  --amplitude .06 --warp-reference .06 --modes 32 --angular 1024 \
  --audit-angular 512 --nodes 401 --max-nodes 6000 \
  --tol 1e-6 --bc-tol 1e-7 --physical-bc-tol 2e-9 \
  --outdir "$W/newg-wide-lambda0p004-m32-linear"
```

实际 Python 是 `/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python`；
两调用均清除 `LD_PRELOAD/LD_LIBRARY_PATH`，
`OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=MKL_NUM_THREADS=1`。
已有目录不能直接覆盖重演。

| 实际对象 | SHA256 |
|---|---|
| `newg-wide-lambda0p004-m32-linear/run.json` | `5c35c60c8f7926441638c416e248a14778ac61dd816d65fd78b33e17a186f093` |
| 完整 raw `inner-00.npz` | `ca2785ae119ef755e02f6e8081ee9f793ca35f7e184eff398276d95a9df238f2` |
| 完整 physical quintic | `8bae0a53a1a6dd10b51681cde549cfca2616b415b227d766563cc4438c7d6545` |
| 本次 M32 端口 | `2be7db12b977a95afe9ad4fa127faf3e92dddd6f2487a9978630e489a69684c6` |
| 初始 M24→32 raw | `15100cdcc9702edc37e093c015d4768dfa2a56173e128f2350b011cb13df3c98` |
| `lambda=.004` 配置 | `07b43ea561bdc6bff5fdb0eae93f0333408a59564307ed2c507f964e45364b0c` |

## 4. 继续范围

本条 `actual_tail_requested=false`，没有为 λ=.004 新接真 DN，也没有
支付它的完整 seam、连续 metric/reach、所有 `t` 或 fixed-g 精化。
原 λ=.002/M24 的真尾 `54314` 独立继续。

下一实际设计从本条完整 860 点 raw 进入 `lambda=.008/M32`，仅更换
核心 homotopy 配置和 fresh 输出目录，保原 base profile、端口、角图、
初始参数缩放及所有原门；后续仍是允许 delta/c 联立变化的设计步。
本条不预记下一步已通过，也不把未达到任务完整标准的前缀结论当作收尾。
