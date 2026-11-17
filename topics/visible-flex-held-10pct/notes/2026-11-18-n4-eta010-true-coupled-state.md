# n4 eta=.1、q=.01 的完整实际前缀—尾联立

维护：Astra-held10-7322d0de-20261118。状态为有限系统实际接受；尚未圆化、闭合或达到10%。

## 实际输入与保留的门

从原 wCut=.08 的 q=.01/M16 接受前缀出发，保留原 eta=.1
双谐波角图、精确核心提升、全部 Frenet 方程与参数守卫。
同一个实际物理尾通过原 TailMixin 联立，delta、vd 仍重新求解。
这不是把线性 DN 前缀与一个单独通过的尾并排称作成功。

本轮 M16、spacing4、depth8、parts8、RK16、原 N512 不变。
采用 R30 已证明的有限求积周期恒等式，独立角行数为128，公开 N
和全部原正性、D/S/A、求积及最终 shooting residual≤2e-9 门不变。
新代码仅复用周期标量根/积分行，不复用 Cartesian 空间点。
前缀 tol3e-7、scaled BC tol1e-8、物理 BC tol1e-10 保持。

原非周期运行已接受 .2H，但随后在 .5H 继续时失去运行句柄；
最后记录 residual2.41005744e-9，没有最终 summary、returncode 或
数学终态，原因未明。新轮从该已接受的 .2H 记录初始化，重新完成
.5H、全H、实际外层及最终 audit。工程中断没有改写为求解失败，
也没有用中断前的某个局部响应替代本轮联合终态。

## 完整返回

五次实际 tail 调用全部接受；前两次 .5H 与全H 预热的 residual
均为8.03352480498e-10。外层使用实际 DN 校正，随后最后一次
完整 audit 重查最终 H；具体结果如下。

| 项目 | 联立终态 |
|---|---:|
| prefix 节点 | 724 |
| delta | .030027177128250468 |
| vd | .2483630655929876 |
| 最大 collocation RMS | 2.99299449252e-7 |
| scaled actual BC | 3.48020791732e-9 |
| 物理 actual BC | 3.48020791732e-11 |
| prefix sampled metric FFT l1 | 2.38461129695e-8 |
| prefix Cartesian Darboux tensor l1 | 1.62251014823e-5 |
| prefix sampled 最大主曲率 | 6.51156622614 |
| prefix Frenet root 最小余量 | .00394501921570 |
| 最终 tail shooting residual | 1.60670990544e-9 |
| tail flow 最小 A | .942544977079 |
| tail audit actualMetric | 5.78292969214e-12 |
| tail audit fullD | 1.49888036681e-7 |
| tail audit formalCurvature | 7.99489798517 |

完整 mean 一阶/二阶接缝误差分别为
−1.17318654791e-12、2.85373946696e-11；非mean二阶误差
4.76670364718e-8。cut metric FFT l1 为1.14074340117e-8，
metric C1 FFT l1 为6.35674933873e-7。这些是明确记录的有限
数值缺陷，尚未替代共同 Cartesian 两jet 的严格修复与全闭验收。

这仍是 lambda=0 的完整核心。线性初态和此终态的 delta、vd
虽仅微小变化，也属于不同的完整 g；下一步已从本轮最终
checkpoint 冻结其自身实际 physical_profile，继续真正 M20
非线性尾精化，不借此前线性端口 g 的 M20 结果计分。

## 来源与复现

入口仍为 `scripts/resume_n4_tail/couple_actual_tail.py`。完整命令、
五次实际响应、源/输入/输出哈希及各原门见
`scripts/resume_n4_tail/eta010_q010_coupled_execution.json`。
本轮以 `--quadrature 512 --steps 16 --scales .5 1 --tol 3e-7`
及原 parts8 运行。真实场保留在
`transfer_work/n4-coupled-eta010-q010-periodic-v2/`。

新 `record_actual_run.py` 只提取标量和哈希。它读取真正保存的
checkpoint 系数块清单并逐项核对，避免把输入摘要继承的旧块名
当成新输出；原始数组不进入 Git。周期模块的四个实际运行哈希
和三个 patched imports 另对照已发表安装清单逐一验证，补足
原 client sources 没有列出的可选模块。

本轮 coupler 另有一项纯记录修复：求解后将 core_summary 更新为
当前 obj._core.summary()。原字段可能来自输入摘要；数值方程、
已求 parameters 和场均未改变。后续固定 g 的 API 已直接由
parameters 与 central_correction_scales 定义完整核心，摘要仅作
差值诊断。既有 q001 检查点保持原样，不重写历史执行结果。
