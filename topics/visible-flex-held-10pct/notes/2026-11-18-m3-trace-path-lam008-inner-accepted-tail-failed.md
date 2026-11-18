# λ=.08：原内解接受，实际新 H 尾仍未过原门

## 真实终态

[λ=.08 唯一续接入口](2026-11-18-m3-trace-path-lam008-coupled-entry.md) 的原 BVP 内解已真实接受：493 个节点、1 次 mesh 迭代，最大 RMS 为 $9.87469885365366\times10^{-7}$。原 Newton 统计为 **3 次接受步，全部 α=1，域拒绝和 merit 拒绝均为 0**。快照的 `state-004` 是保存序号，不是 4 次接受步。

原随后提交全部 8 项新 H 的实际尾请求，在迭代 2 的原 line search 处失败：完整归一化残差 $3.6678627560762796\times10^{-9}$，高于未改变的严格 $2\times10^{-9}$ 门。本轮没有取得完整物理前缀、mean-height 积分或 metric；不能以进程 exit 0 或原内解接受替代整个联立流程接受。

## 已保存的实际状态

执行目录：`m3_work/trace-path-lam008-coupled-v1`。

- 原真实 `solve_bvp` 返回保存为 `inner-00-returned.json.gz`，SHA-256 `936f8bdd0615c7905b560a1942a67d4830721573d07c3fa930ced3f9ce66a310`。
- 同一实际 DN 仿射锚侧文件 SHA-256 `04b605175a4fbd4066ae08de9330da4ac3212ab2654ce803bed51d27eb2bbd4f`。
- 原返回状态含 normalized x、全部 $25\times493$ 节点状态、完整 8 参数、RMS 向量和原 $4\times492\times25$ cubic。未用物理 quintic 反推原 cubic。
- 全部 7 个物理控制仍由原 `pscale*p[1:]` 得到。两个末槽的实际值为 $t=-4.947790658605629\times10^{-6}$、$u=3.1867573949775895\times10^{-6}$；参数数值因原尺度较小而较大，不能与物理控制混淆。
- 本轮支撑幅值 $q=.05928147775446849$、数值 gauge/warp=.06；原 base profile 保持，返回 `p0=-4.293530940936157e-9` 只修正 δ。
- 另有全部 8 个实际 Newton/返回快照及侧锚；清单只存 scratch，Git 保留 hash 与必要标量。

实际失败尾为 `seed_tail_0001.json.gz`，SHA-256：

`c0b60dd59c64f76f34e76dce9722a50e97336d0ebf6805adc3fbef5b16f08b3b`。

它保存完整失败 tail state。末次原全量读数 minA=$0.5218915388038644$、minD=$0.9991195150963185$；这次停点是原残差/line-search 门，不能仅凭这些正值称全尾接受。该失败响应未返回完整接受 audit。

## 过程身份与下一接口边界

真实 session **92146**，启动工具块 `a169db`，终态工具块 `6e4515`；observer 于 **2026-11-18 04:17:44 UTC** 记录 child=0，实际 worker 也为 0。原 main 如实把数学异常写入 summary，`solver_success=false`。耗时约 194.244 秒。

[同一只读 collector](../scripts/resume_m3/collect_trace_path_coupled_terminal.py) 本次工具块 `9bb0fa`、exit 0，只读取 119 个已执行来源、8 个原快照、真实返回状态和一个实际失败尾，没有构造模型或重算 BVP/flow/audit。完整参数、全部新 H、原失败来源和命令见 [紧凑终态记录](../scripts/resume_m3/trace_path_lam008_coupled_terminal.json)。

原内解已保存，后续应接它的原 post-tail 位置，无需再次求解。当前只对这个新的实际失败尾进行一次完整行定位，再由真实原门判定是否有合适的新初值；不会因残差数值接近上一 λ 的停点而预认同一 ULP 原因，更不放宽停止门。本条登记的是原失败及可恢复的原内解，不预先合并后续修复结果。
