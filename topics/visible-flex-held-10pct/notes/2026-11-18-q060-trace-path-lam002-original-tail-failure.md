# 有限迹路径 λ=.02：原内解接受，首次真尾仍未过门

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。

[唯一实际入口](2026-11-18-q060-trace-path-lam002-coupled-entry.md)会话 `94553` 已于 2026-11-18 03:20:37 UTC 真实终止；启动／终态工具块 `67ca61`、`38def1`。observer、child、worker 均返回 `0`，但原 main 的 `solver_success=false`：原内层 BVP 已接受，随后改变后的完整 $H$ 对应的实际尾在原线搜索门失败。程序退出码不能替代数学接受。

## 已完成的原内解

保留原完整 25 状态、八参数与所有原门。原 `solve_bvp` 五次网格迭代后返回 `status=0`、`success=true`，493 个节点，原 RMS 最大值 `9.873637694422844e−7`。七个 Newton 接受步全部取 $\alpha=1$，域拒绝、merit 拒绝和 no-step 均为零；五点 guard 没有额外域拒绝。

终态 $p_0=-1.3637752370752413\times10^{-10}$。完整七控制与八参数保存在紧凑记录；支撑 seed 仍为 `.059818741459951905`，表示 gauge／warp／参数尺度仍为原 `.06`。新控制是沿 λ=.02 七列实际联立求得，未借用旧失败 λ1 状态。

共 24 个完整 raw 快照及各自真实 DN 锚已保存，包含每个 Newton 接受状态和真正返回的 $4\times492\times25$ cubic。原返回文件为 `inner-00-returned.json.gz`，SHA-256 `bc2fee7117ba8d8d842ac3352290ce55e966813ebf8048494688ce6d46180cc0`。这使后续可以在原接受内解之后接续；不能为恢复而重跑这个已完成内解。

## 改变后的实际尾未接受

03:17:54.974 UTC，原外循环发出唯一一次改变后的八维完整 $H$，请求 `jacobian=true`、`audit=true`。其与初始实际锚的八维身份不同，确实执行了新尾计算。

原尾残差依次为 `1.752588698423556`、`4.0575733344065144e−8`、`3.667862901158431e−9`；随后原 multiple-shooting 线搜索失败。原门仍为 $2\times10^{-9}$。最后迭代 $A_{\min}=.5218915666495756$、$D_{\min}=.9991195413189724$，不能将正 $A,D$ 当成残差已过门。

完整失败有限尾状态保存在 `seed_tail_0001.json.gz`，SHA-256 `6f0cdfa7bdc27c330bd3320ba94417e1fb410430dfdcdd3bd685c2944d2411ac`。请求完整 Jacobian／audit 不表示失败响应已经返回一个被接受的完整审计；它仍是失败状态。

原外层在该真尾异常处终止，没有写 physical quintic CP，也未执行后续 mean-height、完整 metric 或接缝审计。故本条只领取原内解接受，不领取实际联立或任何完整几何门。内解实际 DN 锚仍是原旧 $H$ 的接受响应；新 $H$ 的失败状态不能冒充该锚。

## 可复查来源与接续边界

- [只读 collector](../scripts/resume_m3/collect_q060_trace_path_coupled_terminal.py)：核 103 项来源、24 个 raw／sidecar、完整有限数组、全参数／八高度和真实退出，不求值任何方程。
- [紧凑终态](../scripts/resume_m3/q060_trace_path_coupled_terminal.json)：源／日志 hash、原错误栈、完整必要参数及精确恢复位置。
- 所有 raw 场、逐次日志和失败尾留在 `m3_work/q060-circle-trace-path-coupled-lam002-v1/`，不将可再生大数组写入 Git。

接续须先定位这个新失败尾，并在同一完整新 $H$ 上取得原停止门、Jacobian 和审计真实接受；然后从已保存原内解接原 outer/BC 流程。原后处理与 README 完成标准仍全部适用。
