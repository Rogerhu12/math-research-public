# λ=.32：原内解接受，新 H 原尾线搜索未过门

**状态：已保存的数值终态；原内解接受与整个联立接受严格分开。**

[λ=.32 单一步续接](2026-11-18-m3-trace-path-lam032-coupled-entry.md) 的原内解已通过原门：517 个节点、2 次 mesh 迭代，最大 RMS 为 $9.88048770323324\times10^{-7}$。原 Newton 共 6 次接受步，只有一次 merit 拒绝、最小 α=.5，域拒绝为 0。

随后实际全部 8 项新 H 的原尾请求，在迭代 3 的原 line search 失败：

$$
\mathrm{norm}=3.667837241951283\times10^{-9}>2\times10^{-9}.
$$

最后原完整读数 minA=$.5218840911834862$、minD=$.9991191544931648$。停止门没有放宽；这些正值不能代替全残差门。本轮原尾失败响应有完整 checkpoint，但没有返回接受 audit。尚未进入完整物理前缀、mean-height、metric 或接缝审计。

## 实际恢复材料

执行目录：`m3_work/trace-path-lam032-coupled-v1`。

| 文件 | SHA-256 |
|---|---|
| 原 `inner-00-returned.json.gz` | `71a9f0a62945c67576fe55185f40387ac161fd7c606fa9640a523e58e58474f1` |
| 对应原 DN 锚侧文件 | `865b218cc650d0aa2ad91a057c45f1d67a6188234748dd29223eb1d30aacbc72` |
| 实际失败 `seed_tail_0001.json.gz` | `5177e5635e424920e7521151342441c6316fe127d66405ddf603a5eb67450813` |

原 normalized x、全部 $25\times517$ 节点状态、8 参数、7 物理控制、RMS 向量及原 $4\times516\times25$ cubic 都已直接保存。没有用物理 quintic 反造原内解，后续不需要再次求解这个已接受的内层。

原定义核 q=$.05722558496396052$，gauge/warp=.06，base profile 与完整 p0 沿入口语义保存；此同伦是新物理设计，未冒称固定 g 精化。完整参数和新 H 都在下面的紧凑记录中，不在正文复制大数组。

## 真实执行口径

session **7336**，启动块 `398386`，真实终态块 `045d59`；observer 于 **2026-11-18 04:40:28 UTC** 记录 child=0，worker=0。原 main 已如实保存数学异常与 `solver_success=false`；进程退出状态不等于整个联立流程成功。

[紧凑终态记录](../scripts/resume_m3/trace_path_lam032_coupled_terminal.json) 由已提交的同一只读 collector 产生，核对本次 121 个执行来源和全部实际快照，不重建模型、不执行 flow/BVP/mean/metric。

下一项只对这个新的实际失败尾作一次完整行定位；不会从与旧残差读数相近就推断相同邻数方向。任何新的候选仍是初值，必须再经原全 DN/Jacobian/audit 门。此条单独保留原失败，不预认后续修复成功。
