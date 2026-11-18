# 中间同伦路径：完整物理 CP 与原 returned inner 的通用绑定

## 1. 新接口的作用与边界

`scripts/resume_closed/m3_trace_path_returned_inner.py` 将已完整记录的
M8、$0<\lambda<1$ 物理 CP 与其**实际保存的原 returned inner** 绑定。
它复用现有通用 partial-path 物理 reader，不为每个新的中间
$\lambda$ 写一个固定输入 SHA 的恢复器。

新输出优先提供 `accepted_raw_inner` 和 `accepted_raw_sidecar` 两个
明确引用。首次 $\lambda=.02$ 的 CP 则使用已经存在的
`saved_inner_resume.raw_inner/raw_sidecar`。没有 filename glob、
“最近一次”推断或自行构造的原 solver 记录；缺少完整显式引用时拒绝。
这里的 `accepted_raw` 指原 inner 成功返回，不是完整 metric 或闭族
认证。

本接口当前明确覆盖中间路径；$\lambda=1$ 的 endpoint 核及其最终
几何门须按实际来源另行接入，不能将当前中间态升级为精确圆弧。

## 2. 元数据检查

绑定先通过原 `m3_trace_path_prefix.bind_checkpoint`，校验完整
物理 CP、全部系数块和真实 seam 响应，再逐项核对：

- 原 raw / sidecar / raw plan 的明确 SHA 及相互引用；
- 两 plan 的完整物理 design，实际核心种类、$\lambda$、窗口、
  gauge/support、base profile 与源定义；
- 原八参数、七尺度、七个实际控制与物理 CP 逐位相同；
- 原 normalized mesh、25个节点状态、完整四阶系数轴的 cubic、
  全部 RMS、原 `success/status/message/niter` 均实际保存；
- 该 inner 的原 actual 响应及完整 canonical payload 与 sidecar
  一致。它是 inner 使用的旧 affine 线性化锚，不能自动解释成
  returned node 高度或物理 seam 高度的响应。

这一步不构造模型，不求 chart、反函数、均值、metric、Jacobian、
尾或 BVP。保存的大数组只用完整 binary64 摘要，未复制入 Git。

## 3. 显式 restore 的约束

`restore()` 只在后续实际需要模型时由调用者显式使用。它在新进程中
调用原完整物理 reader 构造同一个核/flow，然后用正向 chart 核对

$$
\operatorname{chart}(x_{\rm raw},p_0)=x_{\rm physical}
$$

的全部 binary64 值，不反复逆求 normalized mesh。原 $p_0$ 从同一个
base profile 加一次，完整控制不缩放。

返回对象中，`original_solution` 保留真实原 raw `x/y/p/cubic/RMS`；
`physical_prefix` 保留已保存的物理 quintic。没有用物理多项式的
节点求值替换原 `y`。原 cubic 仅在保存区间内求值，关闭外推；
未保存的原 `sol.yp` 不制造。接口不附加旧 affine 或任何实际尾对象，
后续调用者须选择与其完整实际高度相符的真实响应。

以上恢复路径只是可执行接口；本条尚未调用 `restore()`，不声称已经
执行额外的原模型重建或正向 chart 检查。

## 4. 已执行的实际绑定

只读 CLI 对刚完成的实际 CP

`closed_work/m3-trace-path-physical-finish-v1/seed.json.gz`

（SHA `fd93d3f088038830f9291356acbd4ef997cb912cd345570a0f18c1b5fe574596`）
执行一次绑定。它准确连接493个 normalized 节点、25状态、八参数、
492个原 RMS 与 `bc2fee71…` 原 raw returned 记录，以及
`fcbe787e…` 的真实 sidecar。

实际执行 chunk `4d009b`，exit0，0.155904秒；结果为
`scripts/resume_closed/m3_trace_path_returned_inner_binding.json`。
记录含全部输入/源 SHA、数组摘要与原诊断，并明确
`native_model_constructed=false`、`forward_chart_evaluated=false`。

这一新增接口让后续实际同伦步显式继承完整原状态，不改变当前有限图，
不重复已完成的数值结论，也不把其 $1.9787\times10^{-6}$ 的 metric
改称已过更严门。
