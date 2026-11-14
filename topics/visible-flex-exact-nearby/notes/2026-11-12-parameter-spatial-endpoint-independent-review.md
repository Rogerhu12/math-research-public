# 参数空间导数端点接口：独立源码复核

复核对象是 `scripts/fourfold_parameter_endpoint_spatial_v2.py`，SHA256
`0f652c9d397ea3e91f1c293bec09e4006e71bbef3c29bbff5fb06234ba5b32fe`。
同时逐式核对其调用的 `endpoint_parameter_budget`（`fourfold_parameter_ordered_defect.py`，
`c9998ab78eb93cb42e1b94b854f482d4a80840f57810f862fc17e940d0219e49`）以及
`fourfold_spatial_derivative_defect_budget.py` 的 `certify`、源误差与空间尾公式
（`ed2a43049c290aa95c74c5580bc6da3c432c374b24eb43203319ac5fb47fe4cc`）。
本记录不重复计算叶，不把当前有限前缀称为完整返回。

## 1. 参数变化与整盒转移

共同轨道带上的真实一、二阶参数变化满足

\[
 Z\le e^{A_1}B_0,\qquad
 W\le e^{A_1}(C_0+A_2Z^2+2B_1Z).
\]

这来自直接变化方程，使用普通参数导数，无额外二阶阶乘。
中心近似 `g0/g1` 与整盒近似 `g2` 的混合选择可以使用；源码逐个空间阶付

\[
B_j^{\rm box}\le B_j^{\rm c}+\eta C_j^{\rm box},\quad
A_j^{\rm box}\le A_j^{\rm c}+\eta B_j^{\rm box},
\]

且两条相同增量分别加进 `E1`、`E0`。此处没有把中心 `A`、`B` 直接转授整盒，
也不要求三个有限近似本身来自同一有限参数族；真实三源必须来自同一真实族。

## 2. 完整端点多项式与费用

物理端点为 `Y(x)=x/4+U(x)`。有限坐标近似分别为 `w0,w1,w2`。
源码保留的归一化端点三行准确为

\[
\begin{aligned}
 P_0&=4U+(1+4U')w_0+2U''w_0^2,\\
 P_1&=(1+4U'+4U''w_0)w_1,\\
 P_2&=(1+4U'+4U''w_0)w_2+4U''w_1^2.
\end{aligned}
\]

所有乘积频率保留；这解释为什么源 `g1/g2` 不再乘 4，而端点统一出现 4。
遗漏 Taylor 项依次是

\[
\tfrac23 M_3D_0^3,\quad 2M_3D_0^2D_1,\quad
2M_3D_0^2D_2+4M_3D_0D_1^2.
\]

半径 `sigma+max(A0,D0)` 同时包住真实与选定有限坐标，以及连接它们的线段。
由真实变化界与 `Dj+errorj` 取较小上界合法。系数中心选择费先以完整 Wiener 范数支付，
再用于同带 sup 误差，不存在反向转换。`endpoint_parameter_budget` 的
`Q2*b0*Z^2`、`Q1*b1*(Z+Zh)`、`Q1*b0*W` 与 `Q0*b2` 四项均来自完整二阶差分解。

## 3. 局部逆与实际调用合同

整盒逆门先以 `Ebox=Ecenter+eta*Pg` 验证，随后才推 `P/T`。
可选八次 `P=min(P,Pcenter+eta*T)` 及随后的 `T` 缩紧每步从已成立的整盒界出发，
没有循环假设有利二次根。位移上界的两条独立估计取较小值同样成立。

`certify` 仅需误差的空间阶 0、1；当前实际 CLI
`fourfold_actual_parameter_endpoint_kam.py` 明确从三阶保存记录取 `row[:2]`。
它另核实完整 550 段、准确 `[-pi/2,pi/2]`、descriptor、真实参数盒、所有交叉项和
每叶完整 `2J11`，因此不会把这次前缀输入误标为实际全返回。

## 4. 实际 hybrid 字段名的连接问题

读取完整前 20 段的实际冻结 hybrid 报告时发现：其字段为
`every_center_local_2J11_retained=True` 与 `uniform_local_2J11_not_used=True`；
当前实际 CLI 却对两个 scope 都要求中心报告的字段
`every_local_retained_2J11_included`。因此当前 CLI 将拒绝正确 hybrid 报告。
这是未连接的字段名，不是数学上的遗漏或错误接受。已直接告知该 CLI 所有者；
应在其新版本对 uniform scope 检查上述两个明确字段，保留冻结 hybrid 字节。

结论：空间端点接口与混合转移的数学及源码一致。实际最终 CLI 仍有上述明确
schema 修正待接。本复核不宣告完整前腿、实际 twist 定号、R31 接受或非线性/PDE 逆已经完成。
