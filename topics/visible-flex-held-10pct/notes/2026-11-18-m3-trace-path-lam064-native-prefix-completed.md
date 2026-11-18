# λ=.64：新尾来源下精确恢复原 inner 并完成有限物理后处理

**状态：完整有限 continuation 锚；metric 和接缝误差仍未达到最终标准。**

在 [真实 native 尾接受](2026-11-18-m3-trace-path-lam064-native-tail-accepted.md) 后，本条直接恢复原已返回的 $518\times25$ raw 节点状态、原 cubic、全部八个参数、RMS 数组及历史 affine 锚。没有重做原 inner，也没有对同一节点 H 再发 DN 请求。

独立入口 [resume_m3_trace_path_native_pending_v2.py](../scripts/resume_m3/resume_m3_trace_path_native_pending_v2.py)，SHA `2f359060de3479f297823f7965c36ca2eb445987eff89bfbd76eb323e8190f36`，保留原 pending binder 和总共 outer 0 至 7 的预算。旧 V8 响应只作历史 inner-affine 来源；实际响应缓存只接 manifest `abb2a44f…` 绑定的 native 真接受。prefix 的原源码和 source-root 不迁移，仅 worker 使用独立 provider 包，避免把不同算术来源混作同一个响应。

原 outer 0 的实际边界检查为

$$
\|BC\|_{\max}=2.342244904990641\times10^{-10},
\qquad \mathrm{tail\ residual}=9.168793301146043\times10^{-10}.
$$

该行已经通过原门，所以剩余 inner 没有被调用。随后执行原物理 C² 导出、完整 prefix audit 和真实 seam。节点 H 缓存复用真实 `7682be89…`；物理 quintic 的实际接缝 H 另发一次原完整 native DN，得到自己的真实 208 项 Jacobian/audit 响应 `6074075c…`，没有把节点响应代替另一个 H。

完整有限审计保存为：

| 读数 | 实际结果 |
|---|---:|
| prefix metric FFT-$\ell^1$ | $8.726888545969053\times10^{-4}$ |
| Cartesian Darboux FFT-$\ell^1$ | $0.5517054705331152$ |
| 物理非均值 BC 最大值 | $4.684489809981282\times10^{-12}$ |
| seam 均值一阶差 | $-3.8002870760819873\times10^{-5}$ |
| seam 均值二阶差 | $8.881645419223094\times10^{-4}$ |
| seam 非均值二阶差 | $3.157826662289476\times10^{-5}$ |
| cut metric FFT-$\ell^1$ | $6.100434771523486\times10^{-5}$ |
| cut metric C¹ FFT-$\ell^1$ | $9.590409752665077\times10^{-4}$ |

这些读数明确不满足最终完整误差目标。原实际 partial Flow 的 mean-height 由本次 `height_integral` 重新计算，没有继承旧均值轨迹；本条也没有再追加第二遍 FFT 或最坏点定位审计。原 metric 在 seam 前已经即时保存，因此后处理观察没有遗失。

实际 session **46055**，启动块 `dd0c23`、终态块 `e7ac9f`；observer 于 **2026-11-18 05:38:36 UTC** 记录 child=0，worker=0，历时约 46.03 秒。新 inner 调用数为 0，新 actual tail 调用数为 1。完整 CP 为 `m3_work/trace-path-lam064-native-resume-v1/seed.json.gz`，SHA：

`f55b4fbb0a05483a7ac67dcd352bbc58cb8371a8db5f7a4a476c954a9ae7ea5b`。

其完整物理 quintic 分块 SHA 为 `e5148564e1847f07764ea9271bfb0fc5149240accfe6c70920edc5059084f4ce`；原七个物理控制和八个参数逐位保持，$q_g=0.06$、$q_{\rm seed}=0.054696409291371345$、$\lambda=0.64$。完整来源、参数、两组 H、原 raw 引用和真实终态见 [紧凑记录](../scripts/resume_m3/trace_path_lam064_native_prefix_completion.json)。该状态仅作为继续到 literal $\lambda=1$ 的有限锚；没有宣称全参数固定收敛、精确圆形入口、完整闭合或 10% 持握已经完成。
