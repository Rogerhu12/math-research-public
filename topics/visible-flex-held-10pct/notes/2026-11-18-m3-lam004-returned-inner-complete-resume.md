# λ=.04：从真实 returned inner 完成原尾与物理后处理

**类别：数值证据与已执行接口；不是连续误差证明或本课题完成。**

在 R45 的有限 M8 同伦上，原运行 `20514` 已接受的 493 点内解经字面恢复，完成原 outer 检查、物理 quintic、完整前缀审计和真实尾接缝。恢复运行 `96355` 没有重跑该内解；节点高度的原接受响应直接复用，真实 quintic 端点高度则由原 worker 作一次新请求并通过。前缀有限 FFT 度量误差为 $8.069276022575717\times10^{-6}$，仍高于最终 $10^{-6}$ 门。这是可继续同伦的完整有限状态，不是固定 $g$ 加密结果。

## 1. 已接受的原状态和接续位置

原运行目录为 `m3_work/trace-path-lam004-coupled-v2/`。真正返回的内解是
`inner-00-returned.json.gz`，SHA-256
`7ca5ea61dcabd581bb9541167b2b7c9086d184b5d336465f1e9b3f2479c9fe4e`。
对应的旧 DN 线性化锚为 `inner-00-returned-dn-anchor.json`，SHA-256
`4e6d365b9bc764bad9c03640d89996fe6611d6b1bc3ecf2cc8c128a0bdf86b7c`。
这份锚是在内解期间使用的真实旧高度响应，不冒充返回后新高度的响应。

原状态含 493 个归一化节点、25 个状态分量、完整八参数、492 个逐区间 RMS、真实 cubic 系数、原 `status=0`、`success=true`、`niter=1` 和返回消息。最大 RMS 为
$9.873653007345489\times10^{-7}$。恢复只在保存区间内建立原 cubic，禁止外推；没有保存的 `sol.yp` 不予补造。

原随后新高度尾请求的失败记录为 `a94402ea667b60d454ffe364a3e3b65a8f2b3572f6c1b86c01baf478de924510`。另一次已登记的唯一两邻数初值经原 DN/Jacobian/audit 真正接受，文件
`m3_work/trace-path-lam004-native-neighbors-v1/seed_tail_0001.json.gz` 的 SHA-256 为
`7c3af1e8d95445cacfc82fbb27f138c9c46d560d9eee5bedd401cb84b87e1e93`，残差
$1.8339314423524552\times10^{-9}$。本次恢复直接使用这份完整同高度响应，不重解它。

## 2. 通用 pending-inner 接口

新 `scripts/resume_closed/m3_trace_path_pending_inner.py` 从显式指定的原 raw、sidecar 和失败尾记录绑定原 runtime plan，逐项保留原来源、完整参数、当前同伦值、物理定义和真实返回诊断。它不需要尚未产生的 physical checkpoint。

新 `resume_m3_trace_path_pending_v2.py` 恢复原 outer 的当前位置。原函数只作三处接续变换：不再查询旧启动高度；读入真实此前 outer 历史；第一次循环使用保存的原返回解，其后继续原内解与 actual/affine 切换。原总预算始终是 outer 索引 $0,\ldots,7$，不因恢复重新获得八轮预算。本次恢复索引为 0，原 outer 的实际边界误差为
$3.5419522471783794\times10^{-12}$，因此不需进入 inner 1。

worker 仍按原入口初始化并返回 ready。同高度只查询既有真实响应；未知完整高度交原 worker，保持原方程、完整 Jacobian、audit 和 $2\times10^{-9}$ 门。真实尾记录的原配置与当前 worker 的 IO 路径配置分列，不能为了配置标签一致而重新计算或重写来源。

实际恢复后的数值身份为：

| 项 | 值或范围 |
|---|---|
| 同伦参数 | $\lambda=.04$ |
| 原数值 gauge / 材料 warp | 字面 binary64 `.06`，两者保持 |
| 定义核支撑幅度 | `.05963857477670898`，由既定主矩规则给出 |
| M / 状态 / 控制 | 8 / 25 / 全部 7 个控制 |
| partial lift 窗 | 原 prefix 长度的 `(.5,.9)` |
| 主平顶半宽、过渡宽、控制过渡宽 | `.21`, `.32`, `.4` |
| base $\delta$ | `.06104275721220832` |
| 原返回 $p_0$ | `-3.596950323757216e-10` |
| 实际 $\delta$ | `.06104275685251329`，只加一次 $p_0$ |
| 经线长度 | `1.3602524107476364` |
| 原尾离散 | M8 / parts16 / RK16 / N128 / depth8 |

完整八参数、七物理控制、原尺度、profile、chart/port/尾物理参数哈希在紧凑执行记录中。原 raw cubic 与后处理生成的物理 quintic 保持不同身份。既有 `resume_m3_trace_path_pending.py` v1 没有运行；v2 只修正两处元数据说明：恢复方法写为字面 returned inner，并如实说明 worker 初始化与同高度不发新 DN 请求的区别，数值控制流未改。

## 3. 真实运行与新接缝高度

准备调用 `f6925f` 退出 0，绑定 119 个运行/定义源；这里只读元数据。实际 observer 为 session `96355`，启动块 `f992af`，终态块 `256d07`：2026-11-18 04:13:09 UTC 真正退出 0，观察时间 150.18085606599925 秒；原 worker 退出 0。执行目录为
`closed_work/m3-trace-path-lam004-resume-v1/`，运行计划 SHA-256 为
`7767aed93dd6772139cf84541721f704dd243e7e8bffae2af9cf21a497753d54`。

原完整 prefix audit 返回后立即写回 physical checkpoint，再调用 seam audit。因此即使随后尾请求失败，也不会丢失已经计算的 metric/mean 审计。这里该新请求真正通过：原 quintic 端点的完整高度与恢复的节点高度仅有以下 binary64 差异，未作强制替换。

| 零基分量 | 按数值升序排列的 binary64 邻数步数 |
|---|---:|
| 0 | −1 |
| 3 | −3 |
| 7 | +1 |

其余五个高度分量逐位相同。原 worker 的新高度初始残差为
$2.7508971635286816\times10^{-9}$，原线搜索接受一步 $1/512$，随后残差为
$1.8339314423524544\times10^{-9}$，208 个 height-jet Jacobian 标量全部有限，完整原 audit 返回。新真实尾记录 SHA-256 为
`e87e1fcbf2ecd8e1767fbb470393e75019fcd78c0faf136aa05da8157dcbf7f3`。
不需要执行另外准备的“保持所有内部态、只更新 Dirichlet”初值源。

本次新增 inner 调用为 **0**，新增原 native 尾请求为 **1**。最终 checkpoint 与实际尾来源都指向此次真实结果。

## 4. 已保存的有限审计

| 项 | 原程序保存值 |
|---|---:|
| prefix metric，有限 FFT $\ell^1$ | $8.069276022575717\times10^{-6}$ |
| Cartesian Darboux 张量有限值 | $.006673992421676362$ |
| flow defect | $3.6586308002364395\times10^{-5}$ |
| physical BC | $3.987474091285978\times10^{-15}$ |
| mean 一阶接缝差 | $1.3467426063229482\times10^{-9}$ |
| mean 二阶接缝差 | $-3.1458990523702823\times10^{-8}$ |
| nonmean 一阶接缝最大差 | $4.016752208624297\times10^{-15}$ |
| nonmean 二阶接缝最大差 | $2.034940147811841\times10^{-7}$ |
| cut metric，有限 FFT $\ell^1$ | $2.7396763888365724\times10^{-7}$ |
| cut metric 一阶差，有限 FFT $\ell^1$ | $5.960986821617125\times10^{-6}$ |
| 实际尾 audit metric | $4.624395355534716\times10^{-8}$ |

prefix 审计使用原 1134 个径向样本和 512 个角样本；完整 mean 使用当前模型的原 `height_integral`，没有从上一同伦值复制。原 audit 未保存 metric 主导分量、最坏径向位置或全谱，不能由这个总量推断其位置或原因。记录里的 `inlet.unlifted_projection` 仅是未 lift 的有限投影诊断，不代表实际 partial-lift 入口的度量。

最终可继续使用的文件：

- `seed.json.gz`：`fca57af1457d3c3b27aea7d3477e5888aca951454e876421532aec9c247f59f2`。
- `seed_coeff_00.npy.gz`：`9a810b82991900c35b7a241c4e75ec2f0e95bf680c9ddf5c11f382425b2c0af9`。
- `seed-summary.json`：`fb1266e1f88a31b6ca43b286636955e336df907b5f6a8367031d50c32b7edaaf`。

这些可重算数组不入 Git。`record_m3_trace_path_pending_resume.py` 的调用 `af7201` 退出 0，耗时 .272671152 秒；它只核对已经保存的来源、原数组身份和标量，不构造模型或重算方程。全部完整审计的 payload 哈希保留，仓库仅保存紧凑字段。

## 5. 复现与适用边界

在同一 source tree 中，准备入口使用：

```sh
python scripts/resume_closed/resume_m3_trace_path_pending_v2.py \
  --prepare NEW_OUTPUT_DIRECTORY \
  --raw ORIGINAL_RUN/inner-00-returned.json.gz \
  --sidecar ORIGINAL_RUN/inner-00-returned-dn-anchor.json \
  --failed-tail ORIGINAL_RUN/seed_tail_0001.json.gz \
  --accepted-tail ACCEPTED_DN/seed_tail_0001.json.gz \
  --accepted-summary ACCEPTED_DN/seed-summary.json \
  --prior-log ORIGINAL_RUN/stdout.log
```

这里 `ORIGINAL_RUN` 和 `ACCEPTED_DN` 分别是第 1 节两目录；新的输出目录不能覆盖本次已执行文件。准备产生显式 observer 命令和原函数派生片段；执行入口为 `--run-plan NEW_OUTPUT_DIRECTORY/launch-plan.json`。只读收集入口为：

```sh
python scripts/resume_closed/record_m3_trace_path_pending_resume.py \
  --directory EXECUTION_DIRECTORY --out NEW_RECORD.json
```

这次结果允许从全部真实物理状态继续 R45 同伦。它不证明 $\lambda=1$ 的圆弧可解，不继承 R46 的 10% 条件窗，也没有支付全闭图、reach、全部相位或固定完整 $g$ 的精化。当前同伦值变化和 $\delta$/控制重新求解属于新设计；不能把相邻同伦的 metric 数值当作固定 $g$ 收敛。
