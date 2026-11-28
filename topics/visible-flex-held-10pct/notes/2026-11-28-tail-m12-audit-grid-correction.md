# M12 中间尾的原 audit FFT 前提：真实失败原因与续接修正

日期：2026-11-28。执行：`tail_closure`。实际小记录见 [2026-11-28-tail-m12-audit-grid-correction.json](2026-11-28-tail-m12-audit-grid-correction.json)。

**本次 M12 / N192 / f=.5 没有通过原有限尾门。** 保存的原 worker 失败文本为 `Error: power-of-two angular grid required`；其 `lastIteration` 保留了 `fresh-final-J` 前的 iteration 2 residual `9.474893129591036e-10`、minA `.8200817826294743`、minD `.9995941251715881`。残差已到阈值并不等于 audit 返回，失败包的 `converged` / `residual` 为空，不能升格为接受。

原因已实际定位到同源 `f6tail_actual_metric.mjs` 的 radix-2 FFT 入口：原 audit 要求其角节点数为 2 的幂。我新增 M12 中间阶时采用 `N=16M=192`，满足原基本过采样不等式，却不满足这条实际 audit 前提。原 audit 没有修改，失败包、完整 checkpoint、失败文本、最后迭代与原控制器字节都保留在工作目录。这个新工程错误**不能解释或替代**历史 M16 / N256 的未知 worker 失败原因。

本次新 879 节点 λ=.002 / M24 源所诱导的 M8 子尾已先实际接受：

| 实际有限请求 | 原 residual | 原 audit |
|---|---:|---|
| M8 / N128 / f=.25 | `3.157564301931084e-10` | 完整返回 |
| M8 / N128 / f=.5 | `3.1311279019737547e-10` | 完整返回 |

修正后的控制器规定中间 N 为不小于 16M 的最小 2 的幂，最终维数仍使用真实源 port 绑定的原 N。当前实际计划因此是 `(M,N)=(8,128),(12,256),(16,256),(24,512)`；所有残差、Frenet、audit 门和最终 full-H/J 要求原样保留，没有因失败放宽门。

新的 `tail-mild-modes-20261128-b` 已实际启动，从上一段**真正接受**的 M8 / f=.5 包续接，SHA 为 `107204057a828d019ab7694c006163b6f658bfe398d6e456dc3c2d5add10aa94`。没有重算 M8 接受请求，也没有再次执行失败的 N192 请求。新段用原相互独立的 4 个 native workers，仅改变执行并发；最初段用 2 个。记录时新 M12 / N256 / f=.5 仍在原计算中，没有预写成功。

这次完成的是原工程前提的定位、保留真实失败证据，以及真实续接的启动。M16、完整 M24 full-H、原前缀 outer coupling 与公共 Cartesian 闭图仍由后续实际返回决定。
