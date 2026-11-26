# 真实 λ=.002/M24 高度的低模原 DN 升阶入口

维护会话：Astra-held10-06bbeb39-20261126。

**范围：已执行轻量源码检查的数值入口；尚未启动这条新尾路线。** 输入只能是当前 runner 上通过原完整有限门的 R53 λ=.002/M24 前缀，带它自己的 run/raw/physical、原 port、配置与源码身份。它不是准确圆弧端点，也不是前缀与尾已联立的解。

## 路线与旧记录的区别

检索 HANDOFF、open、旧日志及 2026-11-20 新 g 的 M8/M16/M24、原 warm025/chord-warm050 与 full-harmonic probe 记录，没有找到对这份真实 M24 高度先求完整低模尾、再升 16/24 的已登记执行。旧 M8/M16 升阶记录明确只求 linear-DN 前缀；该背景已登记的真实尾是 M24 的 .25/.5 暖响应及未取得终态的 .75。旧 full-harmonic 初猜 probe 的已知劣化路线不重试。本入口也不重复历史 λ=.004/M24 的 .25/.5 链。

从实际 run.raw_return.candidate_H 读取全部 24 个物理高度系数，绑定实际 raw 与 physical SHA。请求顺序固定为：

| M | N | 高度请求 | 原 audit | 请求最终 height J |
|---|---:|---|---|---|
| 8 | 128 | 所有 $H_1,\ldots,H_8$，逐次 $H_j f^j$，$f=.25,.5,.75,.9,1$ | 每次 true | false |
| 16 | 256 | 同一来源全部 $H_1,\ldots,H_{16}$，无缩幅 | true | false |
| 24 | 512 | 同一来源完整 $H_1,\ldots,H_{24}$，无缩幅 | true | true |

所有 M8 低模都保留；没有只留第一模或按大小筛模。M8/M16 的未保留高模属于粗表示，只有最后 M24 请求才标 original_m24_full_height。暖幂运算使用 NumPy；$f=1$ 直接复制对应来源分量。三档均满足原 $N>4M\cdot3$ 条件。

每次由原 WeightedTailPort.solve 运行；原成功状态、原 residual 与 solveTolerance、原 audit 返回仍必须成立。最终 M24 的原 heightJetJacobian 必须有 $(3M+2)M=1776$ 个有限项。这里复用已发布 tail_solve_recorded_height 的检查，不定义新残差或较松接受器。任何失败立即保留该次实际包并返回失败；没有自动把失败包升为接受锚。

## 跨 M 初猜与源绑定

原 34a036028256ad59c702a3fc8088275dad7c2948 的 950f-tail-warm-remesh.mjs，SHA256 为 91686f1c9e70c36ea53357101b619830015288354d1045116a75b5a9ce47667b。原函数分别复制每个节点的高度块和动量块，共同低模逐项保持，新增模态先为零。同 physicalDepth/shootingParts 下保原射击节点；原 worker 继续检查完整物理配置，并用 dn.tail.initial(delta) 补新 Dirichlet 高度。该状态仅是初猜，随后重新经过原完整非线性 Newton、域门、线搜索与停止门。

各 M 使用已发布 prepare_recovered_native 生成独立 native4 manifest，共用本 runner 已恢复的原二进制与 chord-source，保原 fresh-original final-J 路径。复用 continue_original_actual_dn_chord.py 的 source/native 校验函数与已审 bootstrap/chord 绑定；不调用它的 λ1-only 求解入口，不改源模型身份。每个保存包与它自己的 native source/manifest 核验；不会用下一 M 的源 SHA 错拒前一 M 的合法 checkpoint。

baseline 必须与实际原 port 的 config_sha256 完全一致。除模式数、角求积数、chord 执行元数据、trace 路径与 initialCheckpoint 外，其余配置逐项保持，包括完整背景、depth、shootingParts、RK/audit steps、calibration 与所有原容差。旧来源的 literal mean 只记录身份，本入口不另重定义前缀图，也不宣称共同 Cartesian 均值接缝通过。

## 复现

文件：scripts/resume_20261126/seam_tail_low_modes_to_full.py。

```bash
python "$REPO/topics/visible-flex-held-10pct/scripts/resume_20261126/seam_tail_low_modes_to_full.py" \
  --repo "$REPO" --work "$WORK" \
  --source-run "$WORK/fresh-one-direction/lambda002_m24/run.json" \
  --tail-config "$WORK/m24-tail-settings.json" \
  --outdir "$WORK/lambda002-lowm-tail"
```

若使用新的最短恢复 runner，仅将 source-run 指向该 runner 实际恢复并接受的 λ=.002/M24 run；不宣称与旧场逐位相同。必须已有 recovery-setup.json、chord-source/chord-install.json、native-tail24 的完整 manifest/源码和 frozen_flow_batch。原 prepare、source helper、gate、二进制以及每档实际配置/packet 全保 SHA。

完整 H、状态包、Jacobian、native 文件与日志仅留 runner。summary.json 的输入/阶段/结果只含必要标量、count/L1/linf 与 SHA，不发布方向/高度/状态向量或日志字符串。轻量检查只执行 py_compile、--help 和来源/路线字面核对，未执行本题 DN 求解，没有速度承诺。即使最终有限尾通过，前缀联立、λ1、同 g 精化、全尾连续几何和闭面仍须实际支付。

