# n4 eta=.1 的一笔同物理度量精化

维护：n4_round_core；2026-11-18。本条严格固定输入 checkpoint 的整段 physical_profile 与原 wCut=.08 真实线性端口，不把增幅设计列叫作同 g 收敛。

## 固定参数与完整核心嵌入

输入为 q=.01/M16 的已接受前缀，固定 delta=.030027177128287334、vd=.24836306559053845、vu=.35，所有 ramp、桥段和 tail 物理参数保持。原设计中的 delta/vd 不再作为未知量，改用 $\log(q/q_{gauge})$、自由 c8 和其余高阶核心控制。

在 lambda=0，换 canonical 矩基时保留原完整有限 support 模式。若 $f_o,f_n$ 是旧/新基的 fundamental leakage，$b_8=15\eta/63$，先把旧 c 补零，然后令

$$
\Delta q=\frac{f_o\cdot c_o-f_n\cdot c_o}{1+\eta+b_8(f_n)_0},\qquad c_8\leftarrow c_8+b_8\Delta q.
$$

这同时保持 fundamental 和 mode8，其余低矩原样保留。q 的数值坐标因基改变而微调，不是任意缩小物理输入场。正 lambda 的 API 则冻结同一个 $P_J$，使用已存在的 compact 嵌入公式，不重新定义随 M 改变的圆化核心。

本输入的 seed q=.009999932480233472；完整核心 F、Ft、Ftt 的数值恒等误差至多2.068e-15，材料图投影误差2.276e-15，入口修正4.326e-15。参数 Jacobian 的适当尺度差分检查呈二次下降至约5.08e-9（被检查导数尺度约1.70e-5）；BC Jacobian 最大误差2.90e-10（尺度约.593）。没有靠该差分检查替代最终方程审计。

## 实际精化终态

使用 M20/angular1280、tol1e-8、BC tol1e-8、maxnodes3200。6轮后在 **1920 节点**接受，RMS **9.99604638486e-9**、scaled BC **4.53050140806e-15**。最终 q=.00999989899089613；delta/vd 和全部 g 参数仍为输入值。

| 完整保存 C² 图的采样指标 | 输入 M16 | 同 g M20 |
|---|---:|---:|
| metric FFT l1 | 2.38461152777e-8 | **1.95002728087e-9** |
| Cartesian Darboux tensor l1 | 1.62252668286e-5 | **3.51077655113e-6** |
| flow defect | 1.06290240288e-7 | 3.34188553544e-8 |
| 最大主曲率样本 | 6.51156622613 | 6.51156288930 |
| Frenet root margin 最小值 | .00394505223 | .00394473806 |

metric约降低12.2倍，二阶张量缺陷约降低4.62倍。这是一笔实际的固定 g 数值改进，仍不足以证明可达任意 epsilon。两者均未圆化、未接真正非线性尾、未闭合；不能用这笔线性端口 g 代替主会话真正 coupled checkpoint 的细微不同 g。

## 可复用 seed 的修订与来源边界

首次运行使用已冻结的 `refine_fixed_large_radius_pre_parameter_truth.py`，SHA8496e0f160eb8a8bbad67f375b20bc33a45ba814223969783958108264c6decf。本次输入 core_summary 与 solved parameters 完全一致，差值都为0；新 API 一律从 parameters 和 central_correction_scales 重建，摘要仅用于一致性报告。

同时复查发现，原 mesh helper 只在归一化 [0,1] 上工作。首次 seed 把 physical s 直接传入，造成初始点数降至662；原物理端点仍在，后续 BVP 已重新求解到1920节点并对完整区间审计，故不改变上述终态含义。新可导入 API 已改为先除以 end 合并再乘回 end，保留全部输入物理节点；原 reference lift 的 initial 也从完整已求核心重新投影，而不借入口残差近似的 pp(0)。

源码、命令、参数、检查、终态和系数块 hash 在 `scripts/resume_n4/fixed_metric_runs.json`。主会话将从真正 actual-tail checkpoint 调用修正后的 build_seed，重新解其自身整段 g；这里不预先替它计为通过。
