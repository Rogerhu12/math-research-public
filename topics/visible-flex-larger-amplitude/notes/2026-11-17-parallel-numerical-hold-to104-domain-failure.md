# 同一 hold 真IVP从1.02到1.04的单次有限失败

**负结论。** 从6529原始、未桥接的真实IVP在s=1.02的末态继续，目标固定1.04。M320/N4096、全部962个ODE、rtol1e−13、atol1e−16、first/max step=1/64000及原Q/W/H正性guard均未改变。启动前重新计算RHS/JVP，保存的初始0/1/2jet逐位差[0,0,0]。只执行这一目标，没有更换g、扫描参数或从几何修正场起算。

积分最后在4096角检查下接受s=1.0319816450141146；下一尝试s=1.031981746078114出现Hmin=−1.52234128218e−7，原`Frenet domain Q,W,H must be positive`异常结束。新段780个节点、9453次RHS，耗时47.29秒，目标1.04未达到。

|末积分接受态的检查|4096角|8192角|
|---|---:|---:|
|Qmin|.0385462866737|.0385462866737|
|Wmin|1.11462438591e−5|6.65569628451e−6|
|Hmin|6.32037256056e−7|−4.92442488571e−6|
|min sqrt(W/Q³)−abs(k)|.009311245332|−.083885951481|

该末态的8192角实际RHS相对Gram已为.266650305422；所以**末积分接受态也不是有效的新几何父**，不能把仅4096角的正性当全角定义域。失败发生在原曲率回升ramp中，标量κ约1.08205627358；这只是定位，不是证明失败原因或该g不存在其他解。原6529到1.02的成功IVP及其独立完整共同quintic/规范化结果保持原身份。

输出保留原1601节点，并追加新段去重后的779节点，共2380节点，状态明确`ivp_reached_end=false`、`bvp_accepted=false`。新增段的节点数、失败原因和初始jet核对以report的`continuation`及raw的`true_ivp_continuations`为准；raw中原始`integrator_accepted_nodes`等遗留字段仍描述最初段。后续入口拒绝此失败raw作为可续接父。

## 复现及身份

S为本题scripts目录：

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONPATH="$S" python "$S/parallel_20261117_hold_resume_ivp.py" --input parallel-negative-hold-ivp.json.gz --hold-source "$S/parallel_20261117_negative_hold_profile_ivp.py" --out parallel-negative-hold-to104.json --end 1.04
```

SHA256：

- 原成功输入：`6529073f7ad1c5f041e5f7be921a2dab6f509768622153a770556d0460a5a6be`。
- 本次真实执行源：`e773a7066045fb164894370b9f53e02bb2140b47e4cc23d4e053cca55f2b8c15`。
- 固定HoldProfile源：`ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1`。
- 失败raw：`10192e883b6fc41e80f266d1d1775bcce3bd0eb8be1095f5ae15f84d641459e4`。
- 实际report：`a04a5c153941b73297b3318fc9ab373ee8e43f71afe0f1d0fa476ff7a7b3972c`。

本项没有放宽域、删方程或将失败末态用于新求解。所有raw留scratch。
