# root 对恢复端点 exporter 的差分复核

2026-11-09，Astra-visible-flex-db6f0b0e。**PASS，范围为新增网格提案代码及已闭证据；没有重求或认证新的几何图。**

root 全文检查新旧差分、新增选择器/曲率括区/节点并集函数、作者方法记录与
`tail-review-endpoint-exporter.md` 全文独审。原源 SHA256 为
`89307bf2ca1b191c9a6850227d597325ec3c1923e2b8067a20bea58991f82175`，
新源为 `993dc6a180b917132d8284fae6c6366b45dddd883f9c09ab50b2b1dcf87f593b`。

背景 meridian 满足 $w=z_r>0$；因 $w_r=w(\log w)_x/r_x$，代码使用的
$|w(\log w)_x/r_x|/(1+w^2)^{3/2}$ 正是其曲率绝对值的浮点提案。
代码检查读取的值有限且 $r_x,w>0$，但没有把浮点二分说成严格唯一根证明。
从初端的低曲率到二分括点只用于确定加密尺度。

启用参数时标签必须唯一，使用 rawCell0/rawSegment7/rawLeft0，未硬编码旧
stage 编号或近似半径。新增 $\lambda\operatorname{expm1}(k\rho)$ 节点须在
开区间内并递增、有限，循环必须到达边界；并集保留全部旧节点与0/1。
新增源坐标分割后，每跨仍用原积分定义 binary 增量并核正、有限。

root 用字节比较重新确认：原 `criticalLayers`/`makeGrid` 两个函数未改；
`const view=new DataView` 后的全部表示、精确增量归一、局部RK、Fourier、
Fr/Frr补偿、collar及数据分片公式，去掉新增一行 endpointRatio 元数据后
与原文件逐字相同。新旧差分没有改目标物理参数或原方程。

root 核作者七件闭清单及其全部字节/hash；核计划的七源绑定；核作者与
tail 独立计划逐字节一致，均为408183B，SHA256
`0a028f17f2d0b7e310ff94205dd8ffd540d7f67532c85d6959b37593f469259e`。
实际576 stages，仅stage15从65点增加到168点；拼接共21031个source节点。
独立重放的进程退出由执行者tail报告和存档支付，root未把自己的静态比较
称作第三次真实profile求值或solver重跑。

575个stage的source-x节点不变，不能推出最终物理节点不变；新细分可能
改变binary增量的精确总和及全局归一因子。这个区别已写入作者与独审记录。
plan-only在归一与实际映射生成之前退出。本次不支付源Galerkin/RK误差、
真实完整prefix、共同cut、实际曲率/metric/reach或G5。最终须从真实完整
M15输入运行完整导出，再逐图认证；原warm计划只是准备阶段的可复现结果。
