# 原 δ 可变材料核心设计的独立接续

会话：Astra-held10-06bbeb39-20261126。日期：2026-11-26。

当前固定 δ 的暖 v2 十二次实际尝试均未推进 λ；v3 首 λ=.004 也真实返回 status1/RMS .124646。这里改用原来确实通过 λ=.004/M32、.008/M32 的 δ 可变设计方向，不把固定 δ 的失败当不存在结论。

## 已有成功来源与必要再生

原 warm workflow `held10-live-warm.yml` 的 run45775899674 从 07:31:04 UTC 开始：原 source/input bootstrap 为 07:31:17–07:31:50；原 M24 接受已于 07:47:40 的记录确认。因此 q=.006→.06、λ0、λ.002/M8/M16/M24 的整条必要恢复已在不超过 15分50秒内完成（包含观察等待，不声称精确 solver 耗时）。这条恢复不依赖先前失败的 cold M16，也不依赖后来失败的 warm v1。

新 `lowq_prefix_recovery_design.py` 只从已成功的 `lowq_prefix_recovery.py` 改最后调用；前面的物理输入、q/warp 同步、完整 R48 lift、真实源/场和全部原接受门保持原样。只有新的完整 M24 场真正通过原门后，才调用现有 `material_design_continue.py`：

```text
--targets .004 .008 .016 .032 .064 .128 .256 .512 .75 1
--mode-levels 24 32 40 48 64 80 96 128
```

这是恢复遗失数值场以继续计算，不把已登记的 .004/.008 结论再次算作新数学结果。原 lowq runner 的三路 parent 从 .016 起步且诊断被旧 worker 省略，终态仍未知；新任务不声称它已失败。

## 原设计语义与实际返回

原 BVP 使用 `fixed=False`：p0 是 δ 增量，q=.06 固定，剩余 M−1 个原 support 系数联立求解。后继命令沿用原 profile/chart/完整 port；不把 `frozen_profile.delta` 再加一次。升 M 使用完整初值投影差的 R48 lift，系数为 1。

δ、核心控制以及原 finite mean 随设计阶段可变化：原 M24 使用 mean1168，M32 使用 mean1552。**这不是固定 g 或同一 Cartesian 图的精化。** 最终选择 λ=1 后，必须冻结完整 g、物理参数、mean 规则和时间范围。若随后更改 mean，必须真实重新核对整张图和度量，不能用核心零控制相等来代替。

现有 controller 只作必要的小修正：真正 solver/status0/RMS/physical BC 和完整 raw/physical 身份都通过、而 metric>1e−6 单独失败时，才把它作为同 λ 的升 M 初猜；不会将其登记为已接受阶段。已有 Newton/domain 统计、实际 δ 和 mean 节点数加入小结果投影。方程、Jacobians、Newton、步长、metric 门和 mean 规则没有改变。

## 执行入口

新 workflow `held10-live-design.yml` 沿用已成功的 4CPU/16GB 原 source/input bootstrap，独立 `design` command/result 通道，不中断其他三条实际计算。请求 `held10-material-delta-design-20261126-01`：

```text
python -u topics/visible-flex-held-10pct/scripts/resume_20261126/lowq_prefix_recovery_design.py \
  --repo @REPO@ --work @WORK@ --outdir @WORK@/design-prefix-recovery
```

原 design 子链摘要位于 `@WORK@/design-prefix-recovery/material-delta-design/summary.json`。实际 run 编号与每个真实返回另记；本文不预报恢复或 λ=1 成功。

源 SHA256：恢复 parent `a69f5c6ca118221700b16f01645b87be94afba349ca576825c47993891c22223`；design controller `7f85c3b422416b867a8fd19155583c1e8758fb45729ced1445c290f628360d5d`。两源已有实际 compile/help 通过。数组只留本 runner，提交源、参数、run 编号、SHA 和必要小标量。

## 实际启动

[run45801006547](https://github.com/Rogerhu12/math-research-public/actions/runs/45801006547)已在10:24:19 UTC实际进入job139843898376，原bootstrap于10:25:02完成；worker已运行新请求，首观察处于原M16 port恢复。完整小启动记录见 [实际记录](2026-11-26-original-delta-design-started.json)。runner工作目录为 `/home/runner/work/_temp/held10-design`。没有据启动事件宣称前缀恢复或λ1成功。

## 已恢复的 M32 原接受输入

11:01 UTC实读：本次λ=.004/M24仅metric未门，经原完整lift升M32后，860点/RMS9.941928786103374e−7、metric7.60467686690455e−7、BC2.8434549427822667e−12全门通过；raw `ca2785ae119ef755e02f6e8081ee9f793ca35f7e184eff398276d95a9df238f2`，run `9f9dc6f30e0c3af639615f81b5d9c1009b2292ab42927bf5f024fefbec3d679b`，原mean1552。已续.008。此为丢失输入的必要再生，旧.004结论不重新计数；具体小记录见 [本次返回](2026-11-26-original-design-m32-recovered.json)。
