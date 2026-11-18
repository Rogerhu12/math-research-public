# λ=.64：明确 native 算术来源后的真实原 DN 接受

**状态：完整有限尾的真实接受；不是连续误差证书、完整闭图或最终持握结论。**

原 λ=.64 前缀 inner 已成功返回，真实节点 H 的原 V8 尾在 $3.667517320458417\times10^{-9}$ 停止。其唯一反向局部候选未改善，保留 λ=.32 尾内部的另一个初值也失败。这里回到完整原近解 `753aa9ec…`，全部 checkpoint 状态、边界和参数原样作为未接受初值，只把原完整 DN 中 shooting flow 和对应字面隐式 Jacobian 的计算来源换成明确绑定的 native provider。

这次仍执行原 worker 的 Newton、归一残差、`.05` 域门、线搜索和 $2\times10^{-9}$ 停止门，切口响应、最终 208 项 Jacobian 与有限 audit 仍通过原接口请求和返回。初值没有局部修改、幅值扫描或额外全态预先探针；第一次必需的全 Jacobian 求值就是第一次完整 native 批计算。此前两次 ready 前打包错误见 [独立工程记录](2026-11-18-m3-native-provider-bootstrap-missing-input.md)，均未执行数学求解。

真实单次求解的残差演化为：

| 原 Newton 迭代 | 新 provider 下的完整归一残差 |
|---:|---:|
| 0 | $1.4670069281833668\times10^{-8}$ |
| 1 | $3.667517320458417\times10^{-9}$ |
| 2 | $9.168793301146043\times10^{-10}$ |

最后一次严格低于原门，完整响应 `converged=true`，208 个 Jacobian 元素有限，原有限尾 audit 返回。旧 V8 对同一初始 checkpoint 的残差与新 provider 的首残差不同；不把更换算术误写成逐位相同的计算，也不把此次数值接受解释为真 ODE 或无限尾的严格误差界。

执行入口为 [solve_bound_native_tail_v2.py](../scripts/resume_m3/solve_bound_native_tail_v2.py)，SHA `2629f3d9b25e1342c410156154bc8c0a8ae8d0ba4f26fe6efdc575b8879366f8`。其 [provider helper](../scripts/resume_m3/m3_literal_tail_provider_v2.py) 逐值验证两项明确的来源注记，再核原所有物理与 I/O 参数；它不把 provenance 字段变成新的物理配置。实际 provider manifest 为 `m3_work/native-literal-adapter-v3/manifest.json`，SHA：

`abb2a44fd55d91af60f9f86834ec70e5d40ec73fd8f412eec5ecaaba6bd300be`。

实际 session **92035**，启动块 `7466ef`、终态块 `6599cb`；observer 于 **2026-11-18 05:36:51 UTC** 记录 child=0，worker=0，历时约 78.36 秒。真接受尾为 `m3_work/trace-path-lam064-native-literal-v3/seed_tail_0001.json.gz`，SHA：

`7682be890f21d5c687a978b8480ebc70e0e3f2aad183ff8cb63177fec1b7c4be`。

实际全 H、原配置、来源与运行库清单、三次迭代和 audit 标量见 [紧凑接受记录](../scripts/resume_m3/trace_path_lam064_native_tail_acceptance.json)。本条没有运行前缀 BVP、重做原 inner、mean-height 积分、prefix metric 或物理 seam 审计。后续直接将该同 H 的真实响应接入已保存 raw inner 的原 post-tail 流程；旧 V8 affine 锚保留为历史来源，不能伪装为新 provider 的实际响应。
