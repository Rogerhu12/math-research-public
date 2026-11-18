# q060 圆弧 M8 五点域版本：真实返回 max-nodes，完整状态已保存

状态：**没有得到接受的联立解。**
本次原 `solve_bvp` 真实返回 `status=1`，2431 个节点上的最大原 RMS 为
$1.3860615692460996$。完整返回参数、节点状态、原 cubic 和全部 RMS 数组已经保存。
随后原控制流保存了失败的物理 C2 checkpoint，再在 prefix 审计的均值高度积分处越过原 Frenet 域。
两个阶段必须分开：后处理异常不是原 max-nodes 判断的原因。
没有新实际尾请求，也没有完整 metric 结果。

## 1. 唯一已冻结方法的执行

运行严格使用上一条 `2026-11-18-m3-original-lobatto-domain-guard-entry.md`
的唯一 `lobatto-launch-command.json`：

- guard 源 `8a15397acf3f0007ef5341373266e25bd8e383fb0a0cb32dc15a9f53adf68c31`；
- runner 源 `fc979b5bf136f1feda855bbb6d5249cad758a50e561daa749410141f5b548fd1`；
- plan `da2c3d945ac45fcb04dc456c7e00283fb1c8b9bdbe4d2fe5fb5d3c8687c2374b`。

新 $q=0.05210565550627671$、M8/25 状态、$B_2,\ldots,B_6,T,U$ 空间、
$\lambda=1$、$a=.21,b_p=.32,b_c=.4$、原 profile、七项尺度和全部原门保持。
原初猜 $y,p,H$ 的完整哈希在必要重建时再次相同，未重做 RMS 探针。
没有启动同目录的普通 parent command，也没有并行另一种 BVP。

真实工具 session 为 `82557`，启动 chunk `5cda97`，终态 chunk `ae3122`。
2026-11-18 02:11:57 UTC 开始，02:19:00 UTC 独立 observer 观察到 child exit 0，
原 worker exit 0，用时约 422.71 秒。
退出码只记录异常处理后的进程终止，不能当成 BVP 接受。

中途一次只读查询曾返回 `exec-server transport disconnected`。
既有 session 随后继续返回 running，文件读取也恢复；没有因此重启进程、修改源或推断 OOM。

## 2. 新域覆盖的实际作用和原返回结果

原 Newton 试步额外检查了原 RMS 的两个 Lobatto 点，
共记录 **32 次**由这些点触发的原 Frenet 域拒绝。
因此本次确实跨过旧 `12897` 的“Newton 返回后首次 RMS 立即抛错”阶段，
并让原 RMS/mesh 逻辑继续运行。
这只证明该有限取点缺口获得了实际覆盖，不是连续域证书或求解成功。

| 项目 | 实际终态 |
|---|---:|
| 原 SciPy/网格轮数 | 3 |
| 三轮节点数 | 271、811、2431 |
| 原 BVP status | 1：节点上限 |
| 原 max_nodes 设置 | 6000 |
| 最大原 RMS | $1.3860615692460996$ |
| 接受的 Newton 步 | 17 |
| 全部原域拒绝 | 238 |
| 其中新增两点引出的拒绝 | 32 |
| 原 merit 拒绝 | 4 |
| no_step | 2 |
| 最小接受 alpha | $1/524288$ |
| 新实际尾请求 | 0 |

实际返回消息是 `The maximum number of mesh nodes is exceeded.`。
它表示原逻辑认为下一轮所需加点会超出 6000，不能写成“已计算到 6000 节点”。
原 RMS 仍远高于 $10^{-6}$ 门；没有把补齐取点或增加网格本身记作完成标准。

## 3. 完整返回态与来源

`inner-00-returned.json.gz` 的 SHA-256 为
`6961706a8a9f7c50decf735b2e75f88f51c89a9138ba6830a11e86958044a4f0`。
它包含原归一化 chart 的 2431 个节点、$25\times2431$ 状态、八项参数、
$4\times2430\times25$ 原 cubic、完整 RMS、status/message/niter 及候选完整 $H$。
对应实际 DN 锚 sidecar 为
`85390a6ac5080fa0ffcf2a8c182c720dfb9838c2b5a080f70f9eec1a5b32bb82`。

七项实际物理控制由原 `parameters[1:]*pscale` 给出：

| 控制 | 物理值 |
|---|---:|
| $c_2$ | $-0.03991209359147333$ |
| $c_3$ | $0.02905012062601912$ |
| $c_4$ | $-0.017340601383138365$ |
| $c_5$ | $0.00853655636803817$ |
| $c_6$ | $-0.0033067695153830034$ |
| $t$ | $-0.00014864479045309842$ |
| $u$ | $0.00016596340767297669$ |

这是失败返回态的真实完整控制，不是旧入口的控制，也不是一个已接受核心。
末 `p0=0.0012664867412684557`，故原物理导出记录的
$\delta=0.06230924395347678$、$L_{\rm binary}=1.369164727384046$。
新 $q$ 固定；没有将这个新的 profile 当成原初始同 $g$ 的精化。

返回态候选的高三项 cut height 为

$$
(H_6,H_7,H_8)=
(-2.2327118780731963\times10^{-6},
7.817918650810279\times10^{-7},
-4.1243171108970935\times10^{-6}).
$$

完整八项列在紧凑记录中。因为 inner 未成功，原外层控制流没有向实际尾发送这个新 $H$。
不能把入口真实尾在旧 $H$ 的接受状态移给该候选，也不能据未执行的尾计算宣称尾域失败。

此外，本次共保存 **28 份**完成的 raw 状态：
一个 inner 入口、三次 Newton 初始求值前、三次初始域通过后、17 次 accepted assignment、
三次 ordinary return 和一次原 BVP return。
有 RHS 的内部记录同时保留原节点 `ff` 和由原 `create_spline` 构造的 cubic。
每份都绑定实际 DN 锚；没有用日志中的少量标量合成任何状态。
accepted-step 记录仍不包含 LU/step/cost/refresh，不能称逐位 Newton 算法续接。

## 4. 后处理的独立失败

原 main 在得到失败 BVP 返回值后，仍按原流程完成物理 C2 表示并先保存：

- `seed.json.gz`：`5244dcd8636c586376aa1bc824593a87453933e3f006049d5f87edfa4e0a3a60`；
- `seed_coeff_00.npy.gz`：`48b32b88370aae54f7192fcd18f316171456e6905096e60784f62986d94b8b17`，
  shape 为 $6\times2430\times25$。

该 CP 明确为 `solver_success=false`，没有 `summary` 或 `tail_seam`。
随后 traceback 精确经过
`adaptive.audit -> height_integral -> integrate_intervals -> frame`，
在原每段六点均值积分、audit angular 512 的调用中抛出

```text
Adaptive Frenet domain failure: -8.824213515445933e-08
```

这与原五点、angular 256 的有限求解域不同；本条不先把差别单独归因于径向或角向。
没有完成均值高度积分、完整 prefix metric 或后续实际 seam 审计。
失败物理 CP 只是恢复和定位材料，不能交给生产闭图流程作 accepted anchor。

## 5. 只读收集

`collect_q060_lobatto_guard_terminal.py` 只读已完成输出，核 69 项冻结来源、
28 份完整 raw/锚、三轮网格、全部参数与物理控制、
原 cubic 的节点值/已有节点导数对应、失败 CP/chunk 和真实进程终态。
它没有重算 ODE、RMS、核心或尾。

```bash
python topics/visible-flex-held-10pct/scripts/resume_m3/collect_q060_lobatto_guard_terminal.py \
  --run-dir /workspace/scratch/7322d0dee069/m3_work/q060-circle-trace-lobatto-guard-v1 \
  --out /tmp/q060-lobatto-terminal-new.json
```

本次只读收集工具 session `21884`，启动 chunk `d5a5e7`，完成 chunk `aaa241`，真实 exit 0。
入库紧凑记录 `q060_circle_trace_lobatto_guard_terminal.json` 的 SHA-256 为
`b35c3a5e1194115fed6a7a019c55031d04aa1d71ce381312bceb97944a89e9d9`。
所有原数组和完整日志保留在 scratch，不把可再生数值数据入 Git。
