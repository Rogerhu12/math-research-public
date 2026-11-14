# 原 PM/PA 恢复后的首个完整 carrier 结果

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）
日期：2026-11-13
可信度：111 个连续叶上的实际区间计算与有理数比较；新候选，不是已存在的精确外头解。

## 恢复与身份

旧 PM、PA 两个正式成功的 111 叶包以及全部原依赖已恢复，未重算。新 `tail_outer_legacy_schema_reader.py` 只显式补旧 schema 别名；原五正积分、完整均值、各逆域门、端点两 jet、有限 $J$ 的所有系数和候选场界均保持。新增 $w_r=w(\log w)_r$、物理 primitive 位置及均值高度的包围来自同一旧数据的精确有理数运算。原资源仍是原 producer 的 exit 0 记录。

执行入口 `tail_outer_legacy_carrier_stage.py` 调用冻结数学模块，只替换其 JSON reader。每个阶段另存 executor、reader、数学组件、旧输入、派生 view 和完整 argv 的身份。原模块 SHA 只是组件身份，不冒作本次完整 executor。未改原 MJS、原源函数或任何数学参数。

## 正积分与完整 carrier

在原全部 111 叶上新付 $A(r)=\int_{r_L}^r dt/w(t)$：108 叶同分支 Taylor，3 叶完整分支/符号并集；224 bit、order 16、余项门 $2^{-48}$。十二门全部通过，正式 wall 2.531564712524414 秒、峰值 38292 KiB。原五矩没有重算。

逐模 carrier 为

$$
f_{c,m}(r)=H_{L,m}+a_m(r-r_L)+b_m A(r),\quad
a_m=\frac{m^2H_{L,m}}{r_L},\quad
b_m=w_L(H_{r,L,m}-a_m).
$$

将两端真实非均值 $H,H_r,H_{rr}$ 减去此 carrier 后，用原五个物理 $r$ 正积分作 R48 残余插值。因此完整新候选保留两端非均值两 jet，但其内部函数不同于原 source-$x$ 和旧 physical-$r$ 候选。只有一个完整均值积分常数；尚未宣称两端均值高度同时保持。

192 bit 的真实自身导数、完整 R64 mean、完整 $J$ 的 0 到 80 偶频及 R77 全部在 111 叶通过。核心线性项使用与直接展开区间相交的恒等式

$$
K_r+\ell(2K+P_\theta)
=\kappa_r+\ell\left(2\kappa+
\frac{a_m(1-m^2)(r-r_L)-m^2b_m A(r)-m^2G_m(r)}{r w}\right)
$$

逐模求值，其中 $K=a_m/w+b_m/w^2+\kappa$、$G$ 为实际残余高度。没有把 PDE 二阶导数代入候选。八门全部通过，正式 wall 5.442119598388672 秒、峰值 38800 KiB。

## 实际比较

同覆盖的纯 Fraction 比较正式 exit 0。旧 physical-$r$ 候选 Darboux 上界为 $0.01094933049029123$；新 carrier 上界为

$$
150196937323\,2^{-54}<8.337604902208807\times10^{-6}.
$$

两上界之比为 $150196937323/197245602864128<0.000761471664$。这里比较的是两个已付上界，不是两精确残差函数的逐点序关系。没有跨候选取最小值，没有修改原 8594 叶选定候选。

新完整 $J$ 最坏叶为 part0/panel29、源区间 $[17/256,35/512]$。完整均值/位置偏移与原 R48 到新 carrier 的误差桥仍继续通过 mean v3 与 frame 消费。载体缺陷下降并不单独支付外头存在性、全时 reach 或握持幅度。

## 本地复现

所有原输入来自已恢复原课题目录；完整命令逐字保存在各 `-resource.json`。`math-modules` 是从原 computations 及已发布重建 computations 建立的只读 `.py` 链接目录，不改变源。主线包含这些组件后可直接以该 computations 为 `--math-directory`。两个派生 view 是原 PM/PA 的可重建 schema 视图，SHA 和原件身份在 reader 报告中；无需重复提交它们。新正积分及完整 carrier primary 则随本清单保存。
