# 从完整 λ=.02 有限态接续 λ=.04

**分类：启发式／数值执行入口。** 这是同一明确有限路径上的下一物理设计，保留 $M=8$，不称固定 $g$ 加密，也不预认最终圆弧或本题完成。

前态使用 `closed_work/m3-trace-path-physical-finish-v1/seed.json.gz`，SHA `fd93d3f088038830f9291356acbd4ef997cb912cd345570a0f18c1b5fe574596`。其原内解、实际 BC、真实尾与接缝均已接受，完整有限前缀审计也已保存；metric 为 $1.9786688260610694\times10^{-6}$，仍高于课题最终 $10^{-6}$ 要求。本入口如实保留这项短缺，以此有限态作 continuation 锚，不把中间每个 $\lambda$ 的 metric 另设成禁止推进的门。最终完整图仍须满足原完成标准。

## 一次必要的初值构造

新增 `scripts/resume_m3/run_m3_trace_path_continuation.py`，本次唯一指定 $\lambda=.04$。使用已登记 $P_1$ 真积分区间及精确有理标量运算，得到

$$
q_{\rm support}=0.05963857477670898,
\qquad q_{\rm gauge}=q_{\rm warp}=.06.
$$

保留原 `path_base_profile`、全部八项参数（包含非零 $p_0$）、七个参数尺度和七个实际控制量；不把已含 $p_0$ 的 `frozen_profile` 再当基底加一次，也不调用旧 `ratio**j` restart。

原真实返回态的 493 个 normalized $x$ 只用于继承网格。新模型按完整原 $p_0$ 正向计算 `chart(x,p0)`，与保存的物理网格逐位核对。状态则明确取物理 quintic

$$
Y_{\rm old}=P_{\rm physical}(\operatorname{chart}(x,p_0)),
$$

不是原 raw `sol.y`。在同一有限角基底、同一材料角图上，构造

$$
Y_{\rm new}
=Y_{\rm old}
+\frac{\operatorname{Proj}(\operatorname{Geo}_{\rm old}
-\operatorname{Geo}_{\rm new})}{.06},
$$

再用既有 $[.5,.9]$ 倍 `prefix_end` 的共享 $C^2$ 窗修复新入口。投影只作用于参考差，完整旧有限 Fourier 场本身不重新投影；参考差严格为零的节点直接保留原数值。新旧模型分别捕获自己的核工厂和 partial lift，构造新对象不改变旧图。

这只转换 `Geo + .06 × 全部25项有限场` 的表示部分。均值高度并不在这 25 项里；旧均值轨迹未被复制，新原 `height_integral` 仍须在后处理中真正计算。

实际一次构造结果：

- 493 节点，原全部参数和七个物理控制量逐位保留。
- 原数值核心 guard 的下界 $0.5071598853272026$；这不是严格区间证书。
- 新完整八项 $H$ 逐位等于旧物理 quintic 的端点 $H$，故匹配真实审计响应 `24dd350f…`。
- 原 raw 节点 $H$ 对应另一个真实响应 `d65514e…`，二者分别记录，没有混作逐位相同。
- 所投影参考修正系数峰为 $1.8307943832037201\times10^{-16}$。这个小读数不界定有限带外参考差，也不说明完整两张物理图相同。
- 未额外计算初值 RMS，未重跑旧 $\lambda=.02$ 入口或内解。

实际初值数组与记录先落入 scratch，再生成带这些真实 SHA 的 runtime `launch-plan.json`。这是同一 observer 中的一次必要构造，随后立即进入原联立，不单独发起第二个诊断求解。

## 原联立与记录改动

原 RHS、解析参数 Jacobian、merit、核心/Frenet 门、五点有限域 guard、节点与停止容差、八次 outer 预算、物理 quintic 导出、均值积分和审计公式均保留。每次 Newton 接受与返回仍保存原 $x/y/p$、节点 RHS、真实 cubic 和实际 DN 锚。

完整 $H$ 的字节匹配可以复用已经真实接受、含完整 Jacobian 与审计的响应。任何未知 $H$ 必须进入原 worker，要求原 Jacobian 和完整审计；不以近似 $H$、仿射响应或高度四舍五入替代。本次没有修改原 worker 初值预测器或残差公式。

新增两个后处理记录钩子：原 `adaptive.audit` 返回后立即保存完整结果；最终接缝的文件名与配置明确指向实际使用的真实响应。这样后续接缝若失败，不会再丢失已计算的前缀 metric。成功的原返回态在 CP 中另存 `accepted_raw_inner` / `accepted_raw_sidecar`，失败时只保留 `returned_raw_*`，供以后准确接续。

## 实际启动

source SHA：

`4e8e4548536a0f0091910180247c1240ab49d045acbdf08a892f2809993eac57`。

本次目录 `m3_work/trace-path-lam004-coupled-v2/`，prepared plan SHA `11ce94e323b79d970afce92806c1af48ed8a54e1f7fb72a3e7d15c1d5b0a387a`，实际 runtime plan SHA `b5146523cfb7e67c32d530b968adbec056dc0afe565bc5a5b39fc14443e9abb0`。观察会话 **20514**，真实启动工具块 `3aa85e`，开始时间 **2026-11-18 03:57:56 UTC**。本文件只登记入口，完整真实终态另记。

紧凑记录 `scripts/resume_m3/trace_path_lam004_coupled_entry.json` 提供完整参数、来源、实际命令、初值数组与两层计划的 SHA。114 项来源均已核对；原 outer 与记录 Newton excerpt 逐字沿用。首次 metadata-only 预案在启动前只修正失败态的 `accepted_raw_*` 标签，未运行模型，旧预案与旧源码副本保留在 scratch；没有被当作数学失败或数值重试。
