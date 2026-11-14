# 完整 signed Green 端口的实际公开代数门

2026-11-14，visible-exact-astra-0df9。

公开 [run43596517945](https://github.com/Rogerhu12/math-research-public/actions/runs/43596517945)
已实际成功。原事件提交为 d69ad0dc7720f439c1e1f24b67b1ffa191281094，
固定 93 输入 manifest 为
`da3e142168cb2a92d08548efe71ed4505e2e82d82cda965b128582e1acb22764`。
[原过程](regular_cut_green_ci/run-43596517945-1-public-signed-Green-algebra/process.json)
记录全部输入核实、一个实际数学子进程退出 0、七门完成。
数学子进程墙时 5.000564212 秒；公开实际 arithmetic 为 python-flint 0.9.0。

完成的原 native 为
[public-signed-Green-algebra-gates.json.gz](regular_cut_green_ci/run-43596517945-1-public-signed-Green-algebra/native/public-signed-Green-algebra-gates.json.gz)，
3381 bytes，SHA256
`60e69d61435b76232016fb49e9f3390d2f0b7c8a6e4b3184e777d50a404e08f3`。
原 artifact 为
`visible-exact-complete-cut-Green-algebra-43596517945-1`
（id14114876534，归档 digest
`sha256:b664a8239777f47447e90a6f5a112c435661e57efb60e1cf96735bd4e06f1b96`）。

完整实际源码给出七个检查：

1. 无耦合负 signed rates 的完整 suffix 无 pole 门；
2. 两个负 rate 在真实指数与端口中保留符号；
3. 无耦合源保留右端反馈和 $q$ 方程的真实负源号数；
4. 耦合系统四个源系数与原双状态 transfer 精确相容；
5. 整片 $p,q$ 上界包含两侧实际端点；
6. 真 sec/tan 投影跳及两个独立接口源的系数；
7. 完整 suffix 门失败的例子必须拒绝，不能被端点采样放行。

[core](../scripts/fourfold_codazzi_signed_positive_Green_ports.py)
SHA256 为
`c8f288fd76cd6da753a5e3a615e3518227bb7c75c9a70c2fcfd1d6e852ff9930`；
[代数消费者](../scripts/fourfold_codazzi_signed_Green_public_algebra_gates.py)
SHA256 为
`fa9e78fe396113cbf3e57688e4eecc11532b91807f36d054372e041d3a396cda`。
真实子进程退出 0，结合源码中逐门拒绝、完成时恰好七门的逻辑，
证明该次执行完成了所列门。这里按可读过程及源码核对结果；未经
connector 传输或展开二进制 native。原完整 binary 保持在仓库和原
Actions artifact，后继实际消费者将按完整 SHA 读取并核其七项布尔值。

这七个显式比较系统检查支付实现约定；实际数学比较定理仍见
[signed Riccati 正 Green](../results/R133-supplement-signed-Riccati-positive-Green-with-full-interface-sources.md)
与[完整源合同](2026-11-14-R133-complete-signed-Green-distributed-source-contract.md)。
它们不代替原 5970 格，不授全区间有限逆或未知 high 反馈。
后继 full5970 成功事件按相同 core/source/worker/manifest SHA 和原退出码
直接复用本次 native，不重跑成功代数门。
