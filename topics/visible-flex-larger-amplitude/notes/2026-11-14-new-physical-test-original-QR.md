# 新物理角边界下恢复完整 QR 的实际检验

状态：**算法延续／尚未运行的新数值请求**。不改变 R252 新有限方程，不把原材料角 QR 的失败当作新方程的结果。

[request13 的真实测量](2026-11-14-actual-physical-test-failure-and-bridge-resolution.md)中，新物理角右边界乘**同一旧 Uend**的 112×112 小块条件数为 119589.80909759151。这个 Uend 来自原节点、原场、原 ODE 和原左边界的完整传播；旧材料角边界的小块约为 1.6e17。新切口改变已经实施且完整实际 J 的 FD 通过。它支持直接检验原 QR 在新边界下的真实线性精度，不支持预先宣称非线性解存在。

独立入口 geometry_20261114_physical_test_qr_full_dn.py 复用同一 PhysicalTestBoundary 与完整尾/切口审计，但最终调用 lifted_modes_full_dn.main，**不调用**安装带 LU 的 banded.main。因此使用原 separated QR、原 reduced 小块与原块残差诊断。完整模式不删、不截 SVD、不对材料 P 求逆；原 nonlinear RMS=1e−6、BC=1e−11、17 次回溯、max_nodes=1200、新 H 真尾及最终 fresh audit 全部保留。

request14 只选 coupling112physicalqr，原实际 699 warm 和自己的真实 T112 锚不变。响应 FD 重新运行约 17 秒的完整实际 J 仿射测试；既有真实零尾不重算。真实接受后仍同 run 消费完整 mean/唯一 SE2/自己的尾与闭合/R249；否则保存实际 QR、全部回溯和 checkpoint。源只在公开 Actions 编译/运行，本地执行环境仍 unavailable。

这项与末 bridge 原解析初猜加点是两个独立可比较的计算选择：一项保持旧网格换回原完整线性后端，另一项检验径向分辨率。两个都不改变最终验收门；下一决策依据各自实际结果。
