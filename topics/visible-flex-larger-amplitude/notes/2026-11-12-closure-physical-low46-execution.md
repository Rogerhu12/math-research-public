# 真实外两胞元完整低46物理流执行

详见完整证明 [R87](../results/R87-complete-low46-physical-trace-flow.md)。

- 会话4951：工具最终 exit 0，独立 wait4 也为0；wall 31.13652729988098秒，峰31020KiB。
- 256位、Taylor阶24、平衡余项 $2^{-100}$、临界条带160位，完整46真内头斜率及每模两基列。
- 两胞元18段全部完成；1260个Taylor片、8个真实临界条带，1052次局部门拒绝后原位置细分。
- node11/node10全部92个高度chart非零；m2/m4每段真列、两端完整矩阵与R67相交。
- 所有源码/主包输入hash已逐项核对；每段恢复点完整保存。没有Git操作，没有更改MJS。
- 本包是完整低窗的真实线性流；新增44模的whole-field有源核及高频仍须另付。

入口与完整命令在 `2026-11-12-closure-outer-physical-low46-r1-plan.json`；`-resource.json` 保留实际wait4状态。
