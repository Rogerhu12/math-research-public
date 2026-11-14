# R131 续篇：完整正权闭盒的连续分片消费

2026-11-13，visible-exact-astra-ac0d。

**已证明并执行首盒复核。** 对同一个完整有限 BC 候选、同一个完整
有限正权和同一个真实目标，可以分别生成相邻径向区间的完整 native，
再连续传播同一个加权误差和同一个真实一阶导数界。本篇没有把尚在
运行的分片标记为完整，也没有将首盒通过扩大成整个 \([0,1/5]\) 的
存在结论。

## 1. 每片仍是原 producer 的完整证书

原完整比较定理是
[正权比较与清分母行](R131-supplement-positive-comparison-weights-and-cleared-tube-rows.md)。
它的 v2 producer 为
`scripts/fourfold_codazzi_positive_weight_cubic_native.py`。
每个实际闭盒已经包含完整 Fourier 乘积、全部 mean、闭角 cells、
真实 scalar germ、整个辅助参数盒、完整 Taylor 余项和非线性管费用。

新消费者
`scripts/fourfold_codazzi_positive_weight_piece_C0.py`
首先逐片核对原 kind、原 producer SHA、`complete=true`、
`failure=null`、实际覆盖与准确请求区间相等，以及所有完整范围门。
它再逐项读取并核查每片绑定的所有 input 和 dependency SHA。

各片的真实对象、准确中心参数、整个参数宽度、完整 BC 原字节、
完整正权原字节、原初始误差、原残差全区间和全部管列表必须相同。
角网格或算术精度可以不同：每份完整 native 本来就是同一精确有限
函数在相同真实参数族中的独立闭包围，结论只消费它已经证明的上界。
这种允许不改变任何输入函数，也不省略任何频率。

## 2. 完整径向和真实 germ 检查

第一片必须从原腰 \(r=0\) 开始。原 partition index 从0连续增加；
每行的实际左端必须等于上一行右端，且整个闭盒包含于记录的真实
scalar germ。每片实际行数必须等于其原计划行数，片末必须准确到达
该片请求右端。最终游标必须等于消费者请求的准确有理右端，并处于
原完整残差的区间内。

因此缺行、重复行、乱序、径向空隙、不完整分片和不同输入均被拒绝。
原 native 文件保持原字节；消费者只在内存中构造一个明确标为
`checked_contiguous_original_weight_rows` 的行视图，不写出冒充原
producer 的合并报告。

## 3. 同一个误差在接缝处连续携带

令原完整有限正权为 \(W_p,W_q\)，误差为
\(u=p-P,v=q-Q\)，并定义
\[
z(r)=\max\{\|u/W_p\|_\infty,\|v/W_q\|_\infty\}.
\]
每个闭盒上的原定理给
\[
D^+z\le L_i z+\rho_i/w_i.
\]
同一个有限权的相邻径向多项式使用同一份准确共享端点数组，故
\(W_p,W_q\) 在接缝处连续且严格为正。真实解和有限候选也连续，
从而接缝两侧的 \(z\) 是同一个量，不需重置、重新归一化或支付一个
虚构的跳跃因子。分段一阶系数在开盒内应用最大值不等式，再由连续性
将端点上界传入下一盒即可。

消费者只调用一次原 v2 `propagate`，使用完整拼接行表；每盒严格仿射
屏障的末值就是下一盒初值。独立真实腰的加权角导数也只初始化一次，
随后连续应用 R131 的真实梯度输运。

所有尝试的管及失败行完整保存。一个管通过的最终门仍是
\[
\max W\,z<T,\qquad q-p>0,\qquad k>0,
\]
以及严格仿射 margin 和有限真实一阶导数。小的加权误差不替代第一条
未加权门。只有全部闭盒通过且终点准确到达请求端点，才给该请求区间
同一 Cauchy 分支的延拓结论。

## 4. 已执行的独立消费

当前已完成的独立测试使用原 v2 的完整首盒：
\[
0\le r\le\frac{1152921504606847}{2305843009213693952}.
\]
原完整输入为
`notes/2026-11-13-Codazzi-positive-weight-cubic-s10-first-native.json.gz`。
本消费者的完整输出为
`notes/2026-11-13-R131-positive-weight-piece-first-C0-native.json.gz`。

五个原管 \(1/500,1/200,1/100,1/50,1/16\) 全部通过。root 将
`tube_results`、独立真初值、全部通过管及所选最优管与原单份 v2
消费者的完整 JSON 逐项比较，全部相同；最优未加权误差仍小于
\(3.470723\times10^{-8}\)。这验证了实际实现的输入和连续消费，
没有改变原首盒结论的范围。

newton_source 独立审查了完整输入身份、原 partition 连续性、真实
germ、准确右端、一次传播、独立初始梯度及不同有效网格的允许范围，
未发现需要改动的数学或输入门。

重现时在课题目录指定新的输出路径：

~~~sh
python scripts/fourfold_codazzi_positive_weight_piece_C0.py \
  --native-parts notes/2026-11-13-Codazzi-positive-weight-cubic-s10-first-native.json.gz \
  --right 1152921504606847/2305843009213693952 \
  --out /tmp/positive-weight-piece-first-reproduced.json.gz
~~~

整个 \([0,1/5]\) 的多个分片只有在各自真正完成后才能按本合同消费。
本篇不宣称其运行已结束，也不宣称嵌入、闭面、共同度量弯曲族或 reach。
