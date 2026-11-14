# 第一格常斜率 buffer：实际失败记录

## 准确改动范围

fd2d_flat_outer_tail_design.py 以闭存 wc01 配置为输入，另名设置
flatOuterThroughCell=0、flatOuterStartSegment=2、flatSlope=.1。
用现有 closing_weighted_tail / closing_recalibrated_tail 公式，在第0格内峰
plateau 上把 log-slope 平滑过渡到常数 log(.1)，此后到 cut 恢复段保持常斜率。
cut 的两 jet 恢复公式和准确无限 source 定义不变。

配置 SHA256：
ece7db50c71562a457cd305ce2eb22efdb3d727fcde99725756c5fd426e9db58。

配置内 changed_finite_cells=[0] 指改变了 log-slope 参数的格子；
它不表示所有其他物理径向位置保持不变。全局自由伸缩参数重新求取，因此
全部前160格的物理径向 warp 随之变化。旧 beta 表只是固定定义常数，
没有把原每格校准性质转移到新物理度量。

## 真实结果

全160格、浅层256步的 canonical-momentum 运算自然 exit 0。
没有重置任何内节点的 momentum，也未仅计算前12格。
新 \(\lambda=11.564513707902838\)，原值约13.15597617；
背景 meridian 长 .18185209462477，背景高差 .02096899071000。
实际 \(D_2=2.4522925450591115\)，不能继续用原来的 \(D_2\simeq8\)。

常 \(w\) 区间的准确线性方程给 \(H_{rr}=0\)，因此第一格的真实线性
形算子绝对 row bound 从原来的约565353降至364.895。
但是该格原来的 height gain 一并消失。以 cut 的实 cosine 高度系数1归一，
第0格深侧的高度从原 \(-.0470740\) 变为 \(+.4453294\)。
下一格的真实绝对 row bound 由此上升到
\[
 5\,860\,795.012910559,
\]
峰在 raw1 / segment3 / x=.84375：
\[
 r=.37072276050754,\quad
 w=4.0437873607167\cdot10^{-6},\quad
 H=-.00216899046525,\quad H_r=79.3276951821.
\]
该点 \(w_r=-.29864839522444\)，
\(\delta l=-5\,860\,367.018979023\)。
这不是把相对 \(L\) 误读成物理曲率；物理二基本形式系数已经单独恢复。

全域最大相对 \(|L|\approx5.34193\cdot10^7\)，最大
\(|H_r|\approx131.69276\)。它们只是同一次有限线性计算的额外诊断。
不将这些线性结果升级为非线性不存在结论。

## 可复现文件

数据 stem：
2026-11-12-fd2d-layered64-wc01-flatouter0-p01。

* config.json 固定新物理参数；
* m2-n256-report.json 保存全部分格完成记录、端口、各量最坏点和源绑定；
* m2-n256-checkpoint.json 保存自然结束状态；
* 完整轨道/原 momentum 的 gzip 哈希保存在 report 中，由已闭
  fd2d-layered-tail-m2-audit.mjs 可重做。

此输入没有送入主非线性求解器。下一设计保留有限格的实际衰减，同时把
自由径向宽分配到低 \(w\) 的过渡区，而不是只移除第一格的谷。
