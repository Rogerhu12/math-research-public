# 跨 cap 四阶 Taylor 方法的独立审查

审查者：Astra-visible-flex-db6f0b0e（root）；作者：tail_theory。

**结论：条件证明、实现差异与实际跨 cap pilot 的独立复跑全部 PASS。**
完整绑定及精确检查见 `db6f-root-review-cap-c4.json`。新 producer 为
`scripts/db6f-tail-background-packet-c4.py`，SHA256
`2c8e3c30cd7a23ee2d4c74fca9833b3454085889a28ac5fcf044029b66a4bdf3`。

## 数学证明核对

已逐节阅读 `db6f-tail-cap-c4-taylor.md`，并对照冻结的 stable source
实现。中支与低支之差具有 $t^5$ 因子；中支与高支之差具有
$(1-t)^5$ 因子。独立脚本在有理多项式环中重算后一个恒等式，并核对
两个接缝的 0 至 4 阶导数差恰为零。复合任意光滑 $t(x)$ 保持这些
匹配，不需要接缝横截或 $t'(x)$ 非零。光滑恢复权重与指数保持 $C^4$。

stable source 的 uncertain 分支对 normalized jets 逐系数取 hull。
中支只收紧 $t$ 的常数项，保留所有高阶导数区间；真实属于中支的点
仍包含在这个乘积区间内。低支、高支分别加入，接缝处的四阶匹配
确保不存在遗漏的导数。因此整个单 profile 盒上，第四 jet 系数确实
包住每点的 $w^{(4)}(x)/4!$。这不是解析性断言。

Taylor 积分余项因 normalized jet 已含阶乘，恰被
$\sup|w^{(p)}|h^p/p!$ 包住。二进中心取精确有理中点的最近双精度数，
仍在原盒中。已审有序 Bezier 控制点保证反解近似留在该 profile 的
原 source 区间。精确物理半径的额外误差仍由原函数残差乘已证的
全域 Lipschitz 常数 24 支付。该部分没有使用径向原函数的四阶导数。

这些论证只用于固定 profile 内的 $w(x)$。不能推出 $|w_x|$、含它的
径向速度项或不同 profile 接口也为 $C^4$；新脚本并未作这些推论。

## 实现与独立复跑

与已审 totalwidth producer 的 diff 只在原 cap 值域 fallback 处改用
不超过四阶的 Taylor 包，并增加诊断计数。其余包含性计算、物理网格、
哈希检查、余项输出与 $w_r$ 路线保持不变。原工作阶数必须为至少 2
的偶数，因此降阶后只有 2 或 4；不会索引一个未计算的 jet。

独立复跑真实跨 cap 的原 M8 span 3115，实际进程 exit0。全部 3 个
输出盒的每个数组逐字节相同，跨 cap Taylor 确实被调用 3 次，最大
工作不确定度为 $2.1779972011414653\cdot10^{-7}$，未达工作阈值数为 0。
这次回归验证了新分支，而另一个 raw0 pilot 的调用计数为零，不能
作为它的替代测试。

新方法只供应同一冻结背景的区间包。实际有限图的 metric 仍需后端
独立计算；它不支付源 ODE、无限非线性尾存在或 README 完成门。
