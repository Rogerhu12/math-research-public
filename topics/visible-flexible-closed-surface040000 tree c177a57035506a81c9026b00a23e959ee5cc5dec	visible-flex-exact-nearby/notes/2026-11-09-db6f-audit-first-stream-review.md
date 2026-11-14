# 一阶尾界分块后端的独立审查与 M12 全量重跑

2026-11-09，independent_geometry。**PASS。**

审查新 `scripts/db6f-tail-first-bounds-stream.py`，SHA256 `98686f818270191e413fa20b9388637bf85649bfa82b4f60b3cbde40dee0ad7d`。它调用原已审后端的 `inspect`、Fourier/Bernstein 与区间算术，不改变有限图定义。

逐行核查两个持续状态：在 normalized-increment 格式中，`radial_node` 跨 batch 携带，仍按原顺序逐节点加同一个长度区间，故每个 r_lower 不变；`value_node` 同样跨 batch 携带，仍按原顺序逐项加相同精确积分增量。长度、Fr 四次系数、其积分位置及 Frr 的每个标量运算表达式与原版相同。分块只减少同时常驻的跨数。

`inspect` 内部运算不跨径向 span 混合：每个跨度独立作 Bernstein 与 Fourier 界。`merge_summary` 对 span 数相加、布尔条件取 AND、Lower 后缀取最小值、其他数值取最大值，因此与一次处理全部跨度相同。标签受相等检查。最后不足128跨的批次被完整包含，collar 的三组系数及单独检查逐行沿用。

我使用 batch128 独立重跑 M12 uniform 的全部18,457有限跨度和 R6 collar，输出 `2026-11-09-db6f-audit-first-stream-m12.json`。与已保存原版 `2026-11-09-db6f-tail-first-flat17-m12-uniform.json` 比较，**所有原报告字段都相同，仅实现脚本 SHA 改变**；新报告额外记录了 reference/streaming 元数据。尤其 finite、collar、entireTail 全部字段逐值相同。

本次实测峰值 RSS 为331,972,608 bytes（约316.6MiB），低于0.5GiB。该值属于本次进程，不是整台机器的共享内存数。

通过范围仍是原有有限一阶位移、Jacobian 和截面简单性证书。分块等价性及重放不额外证明目标 metric、实际曲率/reach、源 ODE 或 G5。机器记录见 `2026-11-09-db6f-audit-first-stream-review.json`。
