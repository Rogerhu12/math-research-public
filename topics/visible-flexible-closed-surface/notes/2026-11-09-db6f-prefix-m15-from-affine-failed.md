# 自由 cut 预测后的首次原 DN 校正：失败已保存

状态：**原真 DN 校正未完成；数学 FAILED，工具正常记录后 exit 0。** 作者 `/root/coupled_prefix`，2026-11-09。

本次使用已独审的自由 cut 仿射 prefix 预测作为初猜，输入仍显式 UNSOLVED；实际求解 stem 为 `2026-11-09-db6f-prefix-flat-v17v18-fixed-m15-d12-p8-s32-q256-outer-from-affine`。保持原 g、M15、N256、p8/s32、depth12、guard .05、原 tail/BVP/BC 容差。以此前 M15 的完整 FAILED state 作 warm，仅由原 worker 的 boundary correction 改到新 H。记录 wrapper 只替换为已审 trial-client，不改实际方程/接受规则。

## 已观察的结果

实际工具 exit 0，launcher 记录 `mathematical_success=False`；耗时约 348 秒。首次真 DN 的 iteration0 范数为 $6.600676259915306$，`minA=0.0821189613765925`，`minD=0.9915015284176744`。这与原 FAILED warm 的 $6.60078222010092$ 很接近。

本次也完整保存十档线搜索：四个大步在 raw0/segment4 的 stage32–34 触发原 moment guard；$1/16$ 在 stage35 的原 moment Newton line search 失败；剩余五档完成实际 evaluation，但原残差不降。最后三档为

$$
f(1/128)=17.062934011496793,\quad
f(1/256)=9.68336760508322,\quad
f(1/512)=7.438133145437884.
$$

因此原十档按原规则自然返回 `multiple-shooting line search failed at 6.600676259915306`。这次前缀尚未开始原实际外层更新，`tail_calls=1`；不存在完成的实际 M15 prefix CP。

完整 FAILED 响应 `_tail_0001.json.gz` 的 SHA256 是 `5e22d867594b804d10d820fc5c4a5e4b87163d94b9a0a5dc55972e2a371b8c96`。独立 atomic iteration checkpoint、逐 trial JSONL、失败 stage 输入以及初始不可变 bindings、完成 reproduction、summary 均保留。

## 限定与后续选路

辅助前缀 $1.30246\cdot10^{-9}$ 的 metric 结果仍只能归于辅助问题；本次不把它升级为真联解的固定 g 收敛。新切口的高模变化已实际送入原 DN，但从该失败 warm 出发仍靠近原阻尼状态。不能从这一初猜路径失败推出新 Dirichlet 问题无解，也不能推出 joint BVP 无解。

有针对性的下一类初猜路径是保持同 g、同 Fourier/RK/guard，从较小真实尾边值开始作有限边值 continuation，例如 $H_j(s)=s^jH_j^{\rm target}$，逐步到 $s=1$。临时边值只用于获得目标状态初猜；只有 $s=1$ 的原真 DN 和随后真实 prefix BC 校正才支付目标问题。此前成功的每一个中间响应、失败和退步都必须保存。该建议不改变物理度量，不降低 guard，也不把小振幅尾当宏观解。

本次失败的闭文件清单为 `2026-11-09-db6f-prefix-m15-from-affine-failed-publication.json`。后续计算使用全新 stem，不覆盖此批输出。
