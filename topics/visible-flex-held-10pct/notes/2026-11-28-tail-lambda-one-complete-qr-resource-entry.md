# 真实 λ1 完整 DN 的高模 CSR/QR 接线，以及源码精确恢复

状态：**工程入口与来源合同已准备并实际检查；没有新的 λ1、完整尾、八轮耦合或闭曲面结论。** 本条是原 7a 协调器的高模前缀资源接线，不重复此前原 7a 几何 reader 准备结论。

## 1. 原数学问题与新增执行层

原 `resume_20261126/continue_original_actual_dn_chord.py` 的 SHA-256 为
`7a1ce40d5141c08f4d76b2bc201f3113b04d02f12f60c06809a9053ba03321cc`。
它已经负责真正 R53 的 λ=1、curvature_blend=1、完整 1≤M≤64 模输入，
native4、chord3、完整 H、fresh-final-J、完整高度 Jacobian、全部原 audit 和原 8 次 outer。
原先仅有 direct/旧 streamed SuperLU 的前缀执行选项。

新增 `continue_original_actual_dn_qr.py` 只给这个原流程接入本会话已经实际用于高模设计的完整 CSR/QR 资源链。
`prefix_actual_dn_qr_driver.py` 在同一 Python 进程内调用原
`prefix_block_qr_driver_v3.py`，base-driver 明确为
`design/prefix_chord_checkpoint_driver.py`，默认径向 RHS block 为 8。
完整矩阵、全部列、完整未知、原非线性残差、域门、merit、网格与验收均保留。
没有把 native 的完整 Jacobian 换成前缀 QR，也没有截取 H、只保入口或降低模数。

资源链包括 V5 的显式解析加性 δ 列、只读 Fourier/core 缓存、异常安全的 Flow 生命周期，
每个完整 J 前的全 nodal checkpoint 和已接受 Newton 步的全 nodal checkpoint。
V5 的 δ-Jacobian 算术改变明确记录；不声称整个新执行逐位等于旧有限差分 SuperLU。
完整 CSR 装配及 QR 解全系统、原 residual/所有验收门不变。

独立 coordinator schema 是
`original-lambda-one-native4-chord3-outer8-prefix-qr-v1`，
execution_backend 为 `complete_original_prefix_CSR_QR_V5_checkpoints`。
新 wrapper 在启动和实际返回时分别保存绑定的源码、真实 argv、in-process delegated argv、
原 portable 数学 argv、完整 CSR sidecar 与 factor/solve trace。
`run.json` 保留其真正的 portable 原数学命令；wrapper 来源写独立 sidecar，
没有冒充旧 streamed 源码身份。零次 factor 仅意味着原初猜已达原门，不能绕开原非线性验收。

## 2. 真源解析及后继完整图

`run_lambda_one_actual_dn_qr.py` 仅从真实设计 summary 的
`status=declared_finite_design_stages_passed`、
`result.accepted_lambda=1`、`result.run` 取源，不猜 attempt 目录。
原 R53 gate 再核完整 run/raw/physical/profile；
baseline 来自该真实 port 同目录的 `tail-M{M}.json`，
其完整 SHA 必须等于 port 的 `source.config_sha256`。
读取真实 `frozen_profile` 和最终 δ，不以 linear-root seed 代替。
R87 合法的新 q=.012/profile 可作为最终设计输入，不强制回到旧 q=.06。

新 `qr_actual_coupled_prefix.py` 保留旧 API：

```python
accepted_coupled(source_run, coupling_summary)
load_coupled_prefix(source_run, coupling_summary)
```

它以新 QR source_kind
`actual_lambda_one_qr_chord_final_physical_height` 独立识别新来源；
完整 physical-H 从最终 saved physical 的原 seam audit 及其 packet 绑定，
raw H 另列，不把前缀 raw H 贴作最终 physical H。
原完整 state/depth/native manifest/config/height-J/audit 门均保留。
mean 用真实 `prefix_audit.samples_psi`，并核
`max(audit-angular,16*(3M+1))`、原 GL6，不锁到旧 M24 的 1168。

`qr_coupled_prefix_continuous.py`、`qr_actual_closed_map.py`、
`qr_complete_tail_radius_identity.py` 只把既有完整有限图/连续证书/半径入口
接到这个明确的新来源。实际 finite tail、cut target、完整 Fourier 谱、
共同 mean 和 Cartesian 两jet的定义没有变化。
它们没有导入旧 λ=.002 数值上界来验收新 λ1。

`qr_export_actual_closed_mesh.py` 保留原完整 mesh 位置、环和拓扑生成，
使用已发布的 `analytic/material_circle_phase_contract.py`。
R87 必须显式传 `--phase-end 4/5 --held-width 27/50`；
握持扫窗按真实 S/k/b 与 λ1 准确核验，不继承旧 9/20、k=.2/S=.5 的硬编码窗。
每个实际 PLY 仍须严格小于 5,000,000 bytes；没有现在生成或发布网格。

## 3. 精确恢复及真实检查历史

环境重置前实际检查 session **71238 返回 0**：
8 源编译，7 次 `--help` 调用返回 0；
其中 provider 文件没有独立 CLI，故其这一项准确地说仅检查 import。
原 7a 的四个完整块逐字核同：
source/baseline、native preparation/tail config、finite gate/saved return、
最终 physical-H packet/binding。
`ActualFiniteTailV2`/`ActualCutTarget` 和除入口/旧 held-frame 外的 mesh 代数函数
作过 AST 核同。

还实际使用真 R87 λ=.128/M24 run
`7f8bfa03ec380ef87d0a2dcdfd10b9fac7ad24e94a515f2b8cf271cdb149ed88`
做负向入口检查：coordinator 真返回 1，
明确报 `A real lambda-one source is required before any native preparation`，
`stages=[]`，未启动 native/BVP。
该输入没有改 λ 标签，也没有构造假阳性来源。

这次原 scratch 小报告 SHA 为
`54f898948e10c8c57e5921f7d2c5caec2da1e1d6474f3e42b38600df8ba42078`。
原尚未发布笔记 MD/JSON 的 SHA 分别为
`e36f2f1d301295971408d614b367a59ff37e3e20c279c58df46f1865d7451464`、
`e8d37a5d17298e8e156e48ef706207681db54fd7db55d0433a92d08ea0b778eb`。
环境重置后这些 scratch 报告的完整字节不在；
本条恢复记录没有编造其未保存的逐调用耗时，也不冒称复原了原报告全文。

8 个源码本体通过冻结原源及原实际替换**准确恢复**，
每个完整 SHA-256 与重置前已检查的源码相等。
GitHub create_blob 仅作小文本保存、没有自行更新 ref；
root 恢复 checkout `7b9c69332bafbfd4a234938709544ba9573e3c13` 后已原路径落盘，
再次完整核 SHA、8 源编译、上述 7 次调用均真返回 0。
原 λ.128 raw 已随 scratch 丢失，未伪称重做该原负向输入；
也未重算旧 1152 段数值证书。

所有源码均在 `scripts/resume_20261128/tail/`：

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `prefix_actual_dn_qr_driver.py` | 12962 | `a589e67328c456b85c08f00097f7b6e37327c0625f6d6b5e1085c36d3aad2333` |
| `continue_original_actual_dn_qr.py` | 33412 | `d716cbf3d6c82c1bbe83675218efc7016a6f42c3ec67adb63e03187cefa5fafa` |
| `qr_actual_coupled_prefix.py` | 18114 | `17cf2884fa337ef3a72d23064d2d68dc45973e97ff6722e09fa850fd317bc98a` |
| `run_lambda_one_actual_dn_qr.py` | 9089 | `91dfd5909432ed914b0d9e8a20181c56ca16dac205a308f4d5b468b61049469e` |
| `qr_coupled_prefix_continuous.py` | 21283 | `ef56ab160c7ebf2a16a8fe33901dad2da426d1d8ae71853b645300a53aee0b5c` |
| `qr_actual_closed_map.py` | 21015 | `57b39a97d9d5abcd3ae7dfb17697addb67a8094efba375996ea268a44068d92b` |
| `qr_complete_tail_radius_identity.py` | 16013 | `65513a57f2dcbfaed42c40c6c7a91cb87540f1b53a1fc7b89917f6becb8fb53b` |
| `qr_export_actual_closed_mesh.py` | 17955 | `6c050d032c65503c12ebd70c7c64d5d5f5dc7e7e40f9fa941cb218063c92d61c` |

独立 read-only 对照还核了真实 R87 `execution_provenance=None` 可合法通过
原 `source_streamed_block` 的直接源分支；没有为了接 QR 设计修改旧来源标签。
这里的源码检查不是新的数学解或模型验收。

## 4. 真 λ1 到来后的命令

在本会话 repo/work 路径下，用真实设计终态的 summary：

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/run_lambda_one_actual_dn_qr.py run \
  --repo /workspace/scratch/7c4e33ee17de/math-research-public \
  --work /workspace/scratch/7c4e33ee17de/held10-design-work \
  --design-summary /workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/positive-high-modes/summary.json \
  --outdir /workspace/scratch/7c4e33ee17de/held10-design-work/R87-lambda-one-actual-dn-qr \
  --rhs-block 8
```

若实际恢复工作目录改变，参数必须绑定那个真实目录，不将这个旧路径作为存在性证明。
仅解析真终态可把 `run` 换为 `resolve` 并用独立新 outdir。
原 warm factors 默认 .25/.5/.75/.9，随后 factor1 及原全部门。
本条未提前启动没有真实 λ1 的数值管线。
新的小 chunk 完整几何入口另有源码/检查记录，不混成这 8 源的原先执行结果。

## 5. 范围

仍没有真实 λ1 coupled-H 输出、全闭图比例或固定完整 g 的加密终态。
本条完成的是可执行、高模全系统资源接线和源码恢复；
native M>64 若被真实终态要求，须独立完整扩维，不能把高模输入截断成 ≤64。
