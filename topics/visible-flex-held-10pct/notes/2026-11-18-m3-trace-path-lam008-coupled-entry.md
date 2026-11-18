# 有限圆弧路径：从完整 λ=.04 状态续接 λ=.08

## 本次单步

λ=.04 的原内解、原 BC、实际尾和接缝已完成，完整物理审计也已保存。其 prefix metric 为 $8.069276022575717\times10^{-6}$，仍高于最终目标；本次将它作为明确的有限 continuation 锚，不记作全题完成。已有内解只用一层 mesh、3 次全步 Newton，接缝原尾又以一次原 Newton 修正接受，因此下一步预先选择 **λ=.08**，没有扫描 λ 或增加 M。

本次继续使用已经审阅的 [同一通用 runner](../scripts/resume_m3/run_m3_trace_path_continuation.py)，源 SHA-256 仍为 `4e8e4548536a0f0091910180247c1240ab49d045acbdf08a892f2809993eac57`。原方程、参数 Jacobian、五点域检查、Newton/BC/RMS 门、8 次 outer 总预算、原尾 $2\times10^{-9}$ 门和完整即时保存均不变。

## 实际来源与参数语义

旧完整物理 checkpoint：

`closed_work/m3-trace-path-lam004-resume-v1/seed.json.gz`

SHA-256：`fca57af1457d3c3b27aea7d3477e5888aca951454e876421532aec9c247f59f2`。

旧原内解仍是 `7ca5ea61…`，没有再次求解。新入口使用旧物理 quintic 在原 chart 映射后节点的全部 25 个状态值；它不把原 raw 节点值误当成逐位相同的物理 quintic 端点值。

- M8、原 7 控制列、gauge/warp=.06、原 7 个 `pscale` 保持。
- 新定义核幅值由唯一主矩匹配给出 $q_{.08}=0.05928147775446849$。
- 原 base profile 与全部 8 参数一并保留，`p0` 仍只修正原 base 的 δ；没有将旧 frozen δ 再叠加一次旧 `p0`。
- 原完整 7 个物理控制保留，没有 `ratio**j` 重启或按名义高频幂次放大。
- 使用同基下的参考差回投与原共享 C² 入口修补；232 个参考差为零的节点保留字面旧值。
- 最大投影参考修正为 $3.100481721405235\times10^{-16}$。该数只描述有限投影系数的修正，不能当作完整未投影参考曲线的差界。
- 数值 core guard 给出 lower=$0.5074553121566229$、sample=$0.5075506363722274$；这不是严格连续证书。
- 入口残差为 $8.470329472543003\times10^{-22}$。没有为记录身份再次计算初始 RMS。

新完整 8 项 H 与旧物理 quintic H 逐位相同，因而起始实际响应准确复用旧真实 seam 响应 `e87e1fcbf2ecd8e1767fbb470393e75019fcd78c0faf136aa05da8157dcbf7f3`。它与旧 raw 节点 H 分开保存。之后任何 H 改变仍调用原实际 worker/Jacobian/audit；不以相近 H 的旧响应代替。

旧均值高度不复制到新模型；完整图后处理按新实际 flow 调用原 `height_integral` 和 audit。中间部分 lift 的入口仍不等于定义积分核的精确曲线，不能借 λ=1 的圆弧几何结论。

## 实际启动

119 个来源通过 metadata 绑定：工具块 `443781`，真实 exit 0。新 continuation plan SHA-256：

`304d73208181bacad9bec089bb4385484a003fae389cce8bb4f1c0aad078ce5d`。

唯一 observer 启动为 session **92146**，工具块 `a169db`；2026-11-18 04:14:33 UTC 已观察到实际 running。执行目录为 `m3_work/trace-path-lam008-coupled-v1`，该启动记录没有虚构终态 exit 或新解成功。

完整命令、全部必要初始参数、7 个物理控制、8 项 H、数组 SHA 与运行身份见 [紧凑入口记录](../scripts/resume_m3/trace_path_lam008_coupled_entry.json)。后续原内解、实际尾及完整后处理的真实终态独立登记；不在本入口记录里预认任何接受结论。
