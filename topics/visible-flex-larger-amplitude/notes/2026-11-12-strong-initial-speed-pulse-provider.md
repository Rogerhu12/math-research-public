# 可选 initial_speed_pulse provider 与实际响应入口

## 已实现及检查的范围

`computations/strong_initial_speed_pulse.py` 是独立 Python hook，
不编辑原 provider，也不编辑任何 MJS。接口为
`install(actual_loaded_provider)`；如果调用者只有实际模块的 globals，
也可用 `install_globals(namespace)`。

新物理 profile 字段为 `initial_speed_pulse`，默认 0。
缺省或精确 0 时，velocity、piece_jet、首段长度和所有段构造都走原函数和原算术。
非零时只替换第一段 Hermite 的长度、半径多项式与前两阶 jet，
保持 k0、delta 和末速度；其后仍由原 angle-boost/neck/bridge 构造。
这是新的物理度量参数，不是同 g 的精化开关。

真实原 provider 的小检查已执行，正式 exit 0：
12.185 秒，峰 64324 KiB，0 Flow/RHS/Jac/BVP/Node。
缺省与显式零两条路径的所有段数据、breaks、总长度/高度、
每段 515 个参数位置的全部三项 jet 与 velocity 均逐字节等于未安装前。
hook 重复安装不改变类。

在 `b=-.001,.001,.2,.35,.5,.6`，首尾半径/速度/加速度的最大误差
不超过检查门 `3e-15`；其后半径只出现不超过 `4e-15` 的浮点差，
后段速度和加速度逐值相等。所有样本速度在域内，段和图结点拓扑不变。
第一段二阶 jet 与真实 velocity 中央差分的最大差为
`7.918847799714968e-10`，这只是实现核对，不是连续误差证书。
NaN、infinity 和越过充分域的正负 pulse 被拒绝。

## 小负 pulse 的用途及充分域

小负 b 只为实际中央有限差分留出真实邻域，没有用单边差分冒充中央差分。
写 `h(t)=t²(3-2t)`、`p(t)=64t³(1-t)³`。

\[
 0\le p(t)/h(t)
   ={64t(1-t)^3\over3-2t}\le {27\over4},\quad 0<t\le1.
\]

最后一步用 `3-2t>=1` 和 `max t(1-t)^3=27/256`。
当 `k0*S<=3V`，未加 pulse 的 Hermite 速度单调从 0 到 V。
故 b<0 且 `V-(27/4)|b|>0` 保证完整速度非负，且不大于 V<1。
b>=0 时 `p<=1` 给出充分界 `v<=V+b<1`。
代码另外要求正长度、正 k0/delta，以及新长度上的 `k0*S<=3V`。
默认 b=0 没有增加原构造本来没有的拒绝门。

## 新的实际全场响应入口：仅准备，尚未算新列

`computations/strong_pulse_disk_control_response.py` 组合已冻结的
`strong_disk_actual_fixed_control_response.py`。
它只做四项明确源码变换：允许新的外字段；对缺省 b 读为 0；
在实际 root-dual 的 nested module loader 上安装上述 provider hook；
记录新 provenance。

完整变换源已 AST 编译，并把四项变换逆向消去，逐字得到原 disk response 源。
source-only 作业正式 exit 0，0.664 秒，14464 KiB，
**没有执行实际响应或加载物理场**。
默认只请求 `delta,boost_length,boost_speed,initial_speed_pulse` 四列；
可以显式加其它原本允许的 prefix-only 外控制。

以下原门全部保留：真实已接受 fixed-view 的 M 个核心参数布局；
完整原 raw/x/y/p 的恢复；baseline complete-H 与物理 BC 的复现；
完整固定 g Jacobian；两个扰动步长的全场外 forcing；
全矩阵及 streamed backward error；3×3 实际核心控制交换。
新的响应输出不是新 BVP 或新接受面。
M+3 的已接受设计端点仍必须通过真实固定视图转换后才能输入，
不能只改 metadata 标签。

该准备为后续直接测量 core-held b 方向提供入口，
不把背景包络的大幅降低当成完整实际控制响应的结果。
当前 q096 原目标尾部与前缀计算不加载这些新源码。
