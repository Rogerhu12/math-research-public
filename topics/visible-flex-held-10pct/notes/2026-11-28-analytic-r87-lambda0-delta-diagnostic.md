# 新 R87 严格 λ0 的真实未接受状态：七节点完整 δ 列诊断

2026-11-28；本记录只诊断新 R87 的当前有限方程，不重跑旧 profile，也不把未接受 nodal checkpoint 升成解。

## 实际触发与来源

新 R87 的严格 `tol=2e-7` λ0/M8 求解在765节点发生很小的原牛顿阻尼。读取其真实保存的 ordinal9 全量检查点 `unaccepted-nodal-before-jac-0009.npz`，SHA
`e13909bf4981deae02e0024de06e58c3923f37815cb704085e63ce7257ee01c1`。
完整坐标为765个原节点、25个 state、8个参数、7个实际高支持控制尺度；没有删方程、换归一化或重新网格化。

诊断只选原节点索引 `0,127,255,382,509,637,764`，保存并核同原 `x/y/p/pscale`、checkpoint metadata 及全部原来源哈希。在这些节点保全部25个分量和全部8个参数方向。其实际物理 δ 为 `0.06809573171284733`，q/warp reference 都是 `.012`。报告只保存来源元数据和标量；列数组仍在科学 scratch 中。

## 第一入口实际失败与源码分支事实

第一独立入口 `check_unaccepted_design_delta_nodes.py` 借用了旧 positive-λ 的 `build_model`。真实 TTY42974 返回 exit 1（片段 `33ddf5`）：它无条件读取 `factory.jet_parameter_derivatives`，但当前 λ0 的 factory 没有该属性。尚未评价任何 δ 列或 Jacobian。这是诊断构造器不适用于 λ0，不是当前原 BVP 的数学失败；原失败源保留。

原 `material_support_factory.make_factory` 仅在 `homotopy>0` 时设置该属性；原 portable 也仅在该属性存在时装 `analytic_adaptive_core_jac`。V5 的 δ 替换只拦截此安装入口。因此当前 λ0 实际仍使用原 `exact_core_lift` 的完整参数有限差分分支，**没有安装 V5 的解析 δ 列**。不能因当前命令带 V5 wrapper 就把微小阻尼归因于一个没有执行的解析列。

## 独立 v2 的实际返回

`check_unaccepted_design_delta_nodes_v2.py` 按原 portable 的真实 `hasattr` 分支构造同一方程，保 λ0 的原全参数有限差分；不伪造缺失属性。该新进程先计算实际原七节点完整 Jacobian，再以独立 `OriginalDeltaColumn` 作为数值比较对象。没有把它安装进当前或任何后继求解器。

真实 TTY94929 返回 exit 0（`b67a44`），用时4.791602747秒，最大 RSS 79340 KiB。完整 RHS 中心差分与独立解析 δ 列的比较是：

| δ 步长 | 最大绝对差 | 相对二范数差 |
|---:|---:|---:|
| $10^{-6}$ | $3.8047490612691966\times10^{-8}$ | $6.928985587931628\times10^{-10}$ |
| $2\times10^{-7}$ | $1.799069529392905\times10^{-7}$ | $3.3399286415337597\times10^{-9}$ |
| $5\times10^{-8}$ | $8.471738317440748\times10^{-7}$ | $1.6321856071931404\times10^{-8}$ |

原 λ0 生产 δ 列就是第二行步长的完整差分，逐位相同。所有原 state 列、所有原 support 列及原 RHS 重评逐位相同，最后 base RHS 也逐位恢复。

这些实数比较没有显示新 profile 的 δ 公式有宏观不一致；更小差分步长的误差上升符合舍入影响，但本记录不把这个观察升成严格导数误差界，也不据七节点排除全域问题。

原 λ0 支持列仍用 `2e-5*max(1,abs(p[j]))` 的参数差分。末几个物理系数尺度为 $10^{-9}$，故一些方向可能只移动核心系数约 $2\times10^{-14}$。这是进一步核查支持列的具体理由，尚不构成小阻尼原因的证明；后续独立核验另记。当前活 source、RHS、域门、BC、RMS 和 metric 门都没有修改。

实际完整小报告为
`held10-analytic-work/r87-real-unaccepted-delta-check-20261128-b/comparison.json`，SHA
`54527662425a2df6a4935db0e9a1dc8ee90bf2e852f910060b564adddcd955b1`。
完整执行来源、失败/成功区分和列文件 SHA 见同名 JSON。未组装全局 collocation J，未执行新 BVP 或 native，也没有给出新的接受场。
