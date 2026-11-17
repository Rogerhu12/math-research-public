# 新 wCut=.16 的两个完整有限前缀

维护：Astra-held10-7322d0de-20261118。可信度：原门下的实际有限 BVP 数值证据。

此前新 cut 的真实24模端口与双根只给线性设计；本条登记在该物理
设计上真正求得的 q=.01、.0125 前缀。两行仍使用有限线性 DN，
lambda=0，未安装精确圆弧、非线性尾或全闭图。

## 一致的定义与实际求解

共同 rCut=.3、wCut=.16、vu=.35、ramp=.45、ramp_eta=.05，
ShortBridge K4/peak=.2、cycles1。原 worker 重建的端口 SHA 为
`b7f572c5dcb04b355c1dec7da5908bb0a30a5ac8e0b89c0919990438c399abb5`。
该物理设计与原 wCut=.08 的整段 g 不同，不能互换端口或误差结论。

核心 eta=.1、轴 pi/4、半宽 .147、transition .08、control
transition .16；保留完整精确 reference lift 与双谐波材料角图。
两行 M16/angular1024，初始241节点，maxnodes3200，tol3e-7、
BC tol1e-8 及原正根/核心正性门均不变。q=.01 从真实双模
BackwardLine 冷启动；q=.0125 用完整已求材料映射暖启动。

| 项目 | q=.01 | q=.0125 |
|---|---:|---:|
| 迭代次数 / 最终节点 | 5 / 731 | 2 / 748 |
| 实际 delta | .030154764799030766 | .03015813595363715 |
| 实际 vd | .2501491579635462 | .25018861537216824 |
| 最大 collocation RMS | 2.97663907310e-7 | 2.98075972845e-7 |
| scaled BC | 2.72004641033e-15 | 1.16239964008e-13 |
| 完整图 sampled metric FFT l1 | 2.48503837443e-8 | 5.97569413959e-7 |
| Cartesian Darboux tensor l1 | 1.32801541744e-5 | 2.12364202269e-4 |
| 采样最大主曲率 | 6.48302966713 | 6.72287144138 |
| 采样最小 Frenet root 余量 | .0156278664556 | .0152963919781 |
| terminal height 最大系数 | 7.52448999147e-6 | 9.41093615659e-6 |
| 实际求解秒数 | 229.56 | 161.26 |

两行均通过原有限 BVP 及1e-6的采样 metric 门，但第二行完整
二阶缺陷已经显著上升。较大的 root 余量不等于完整非线性存在
或收敛证书。delta、vd 均重新求解，故这两行也不是固定 g 精化。

## 已继续的任务及复现

已以两张接受映射作完整材料角 secant，继续 q=.015/M20；
该轮随后已给终态：虽通过原 BVP，完整 metric 未过，另条登记。
上述 q=.0125 接受态继续作为新 cut 精确圆化入口；后续结果独立登记。

先按 `scripts/resume_n4/README.md` 准备源，再用已发表
`scripts/resume_transfer/n4_thicker_cut_design.py` 重建端口及
物理双根。依次运行 `run_large_radius_circle.py`，完整参数、
材料初值路径、源转换、真实输入/输出/系数块哈希见
`scripts/resume_transfer/n4_w016_prefix_execution.json`。
`record_w016_prefixes.py` 已逐项核对实际 runtime 的相关依赖和
真正 checkpoint 的系数块；不把运行目录中未导入文件的 hash
误称为执行依赖。原始求解结果及证书界表只留在 scratch。
