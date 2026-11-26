# 已付真实尾口的核心返回：首个完整原终态收据（2026-11-26）

本条只登记已经自然结束的一次公开运行。没有重做原三次尾种子，没有在本地执行任何科学计算。

## 1. 原身份、原 stdout 和自然终止

- workflow：visible-flex paid actual mouth to undivided core return。
- run：[45805053770](https://github.com/Rogerhu12/math-research-public/actions/runs/45805053770)；job：[139857971246](https://github.com/Rogerhu12/math-research-public/actions/runs/45805053770/job/139857971246)；attempt 1。
- source commit：8bb42c049fbfaa52083fcfe73f5e37186ef5dcc3。
- entry：r582_paid_mouth_core_return_20261126.py，SHA256 4afa0f904acc14fb892ccbcddf38ea006af9c829f0451c23b0e7f654ce8671e4。
- 原被复用算子 r582_actual_circle_seed_and_return_20261126.py，SHA256 fd4bd864c3e9e96d741b7bc896a1bf6f9d50ba54eda0c02bd898f21bd42427a4。
- request：12546 B，SHA256 e198c94f773bc136cb9d6d279402723f97e1ba97b5677867a59a2113f0b0b6e1。
- 完整原 job stdout：362350 B，SHA256 6745776a6153dccc835040df25ec3302426239fd6ba9377564870819b21ccce7。
- 原 FINAL JSON：165647 B，SHA256 a616918bf26bbda7952aba7fd0dc3d997a9c187b290325edb3cafb4aa0b75847。

自然 job conclusion 是 success，子进程 returncode 0。原 termination 是 natural_control_backend_returned_without_new_fine_geometry_points；这不是完整等距返回、非线性族或 README 完成。

子进程开始/结束为 10:51:03.145261 / 10:51:04.383725 UTC。原科学计时器记录 **0.4446435769999937 s**，子进程墙钟约1.238464 s，两个时钟不互相替代。

完整原日志只在 scratch 保留，未入 Git、未作为 blob/Actions artifact。原 JSON 和本条全部数值均从自然终态原 stdout 读取。

## 2. 真实双仓 pull 与规则

本次公开仓 actual git pull 于10:50:47.834379开始、10:50:50.413359完成：
8bb42c049fbfaa52083fcfe73f5e37186ef5dcc3 → 4836315578e115863c648be59d48b12d12a20d6a，returncode0。

根 README blob 282e86b03385d3b6245ce7100ae2e2af7b103c2d、课题 README blob d0432faff569c8e9af7ed4809847e12880976c11，二者 diff 均为空。

私库 actual git pull 于10:50:53.269935开始、10:50:55.558979完成：
fccaabaee7246cdb80e711c3ac95bc992192ea9e → 4087b83abf785b9f2aaccbb4b7fe55c0660d94c7；根 blob 5ba164843b1f5802184178a82d786264404873a3 相同；QUEUE 唯一本课题行仍为本会话进行中。原 SOURCE 绑定六份实际源，科学前凭证已移除。运行版本为已声明 Python3.12.14/numpy2.3.5/scipy1.17.0。

## 3. 原种子完整复用，旧失败接口关闭

[此前原收据](2026-11-26-r582-paid-seed-json-failure-receipt.md) 的三次真实传递是 run45800483161/job139842104318：

| 原 M / 容差因子 | 已付 inner RHS | 已付 outer RHS |
| --- | ---: | ---: |
| 168 / 1 | 48582 | 600476 |
| 169 / 1 | 54068 | 600476 |
| 169 / 8 | 70172 | 773624 |

此次 new_inner_or_outer_seed_transfers_executed=0，actual_weight_calls=0，inner_RHS=0，outer_RHS=0。同一 s=.82 真实尾口和三份原六 jets 直接来自完整带摘要的小输入。原114.013392 s子进程墙钟与精确终末科学计时缺失均继续记账，未计成零，也未与新科学计时冒加成同类精确时间。更早原 circle 全探索2401.8924319029998 s及其中 stage0输入2.981966937 s也保留来源，不回放其失败的p试探。

原 numpy.bool 序列化错误已经在新入口关闭：两个 same_actual_mouth 都成功输出 true。M168→169的六jet最大观测差约2.38e-14；M169因子1→8最大约6.30e-12。这里新增的只是原数字的只读比较，不是新的 ODE 传递或误差证书；原 cell 理论截断界不自动包含数值 ODE 误差。

## 4. 真正新支付的两控制与自然后端

新输入保持同一实际圆核17均值系数，用
a=a_*exp(mu psi)，z=z_*+nu psi，psi支撑于(.06,.80)；
尾口.82、核心口.036均不变。mu范围±.04，nu范围±.06。

原控制记录共12条（初始评估、后端callback及最终自然点）；唯一候选11，linear_least_squares=13，包含两个后继固定均值增基。原自然 SLSQP nit10、nfev11、njev10、status0，消息 Optimization terminated successfully。不存在被隐去的后端失败或时间中断。

| 已完成控制 | fine保守线性上界eta | 几何V | 保留身份 |
| --- | ---: | ---: | --- |
| (0,0) | .26975598202157136 | 0 | 初始有限合格候选 |
| (-.04,-.05999999999999992) | .03563093910440156 | 0 | 改善 |
| (-.03859409445907816,-.052188428699312804) | .007184138260099953 | 0 | 改善 |
| (-.04,-.049196411435989094) | .0069545364217516985 | 0 | 改善 |
| (-.04,-.048938713783582645) | .006486999913866644 | 0 | 改善 |
| (-.04,-.04893431917441107) | .006479209331362881 | 0 | 最后保留 |

accepted_finite_linear_improvements=6，包括初始有限合格候选。其余已完成trial没有因为coarse均方下降而覆盖fine上界较好的保留态；最后重复callback和terminal自然点也没有额外计改善。

仅outer0，实际几何节点1214，完整fine节点2413，pending_geometry_nodes为空；next_geometry_node_proposal仍同1214个实际节点。原 last_trial 是最近完成整套细读的trial，不能解释为每个SLSQP内部候选都各有一份该字段。

## 5. 最后保留几何与完整局限

最后控制准确为
mu=-.04，nu=-.04893431917441107。
mu已在此次声明盒的边界；不能把该边界最优称作所有均值设计的最优。

2413点完整几何扫描：

| 项 | 原值 |
| --- | ---: |
| raw geometry violation | 0 |
| ball max | .7540922720626985 |
| radius/strip max | .38911424067400135 |
| curvature max | 16.429102288730302 |
| mean E min | .489815451419476 |
| height min | .02 |
| curvature plus最小余量 | .002424909028296063，s=.7470703125 |
| strip最小余量 | .018678549071003303，s=.6767578125 |
| mirror最小余量 | .10849168780084747，s=0 |

联合充分预算仍R=1.012、Y=.3928、tau=.06072，未放松任何实际门。该表只在有限网格成立，不支付全连续曲率或全pair reach。

在返回区间的独立513点线性读出，背景z_s最小.012730981051657458、最大1.0648659662042483。**当前实际观察没有发现穿零；这不是全区间连续正性证书。** 后继应针对这个实际正值输入继续，不能把条件性穿零引理写成该背景已经发生的障碍。

## 6. 同一最后均值上的24/48/96基线性比较

本次全部线性幅值eta明确是
.5*(abs(e_amp)+sqrt(e_amp^2+4*f_amp^2)) 的保守角谱上界；
true_continuous_angular_maximum_computed=false。
e*cos2theta、f*sin2theta不能在同一角度同时取两个绝对幅值。没有在收据中把这个上界改叫真实角峰。

| 每场基数 | 线性未知/秩 | 同均值fine上界eta | attainer s | 尾口比例lambda |
| --- | ---: | ---: | ---: | ---: |
| 24 | 49 / 49 | .006479209331362881 | .32693749999999994 | 7.141786872245636 |
| 48 | 97 / 97 | .00016333775648803825 | .58571875 | 7.132914276492906 |
| 96 | 193 / 193 | .00021887224033628264 | .81846875 | 7.131371662796238 |

三者fit用257径向节点，独立fine用513。48/96没有再优化mu、nu，确实固定同一完整均值背景。48→96的fine最大值没有继续下降，attainer还转到尾口邻域；不能宣线性收敛、完整返回或固定g的非线性细化。

48基fine分量max为|e|=7.879470908040948e-5、|f|=.00013858280265797724。
96基为|e|=.00015552582172801378、|f|=.00013611129975177382。

24/48/96归一设计矩阵最小奇异值分别.0050583392471234235、.0009975951952923658、.000313309235787098；此次没有触发rcond1e-13的秩截断。归一normal residual分别2.6092318003477846e-14、6.005110523025469e-14、1.0477936917809049e-13。这里只读实际满列秩，不把它外推成控制梯度的严格证书；源仍明确字段保持梯度的变量投影适用条件。

最后24基场的|A,C|峰.6560546942651941，一阶2.9082589526766736，二阶28.83567467740541；48/96对应二阶约28.8884。有限非圆使用前仍需承担非线性和几何增长，不能仅看一阶线性误差。

## 7. 实际新成本与直接后继

本次原COUNTS完整为：

- actual_weight_calls=0，inner_RHS=0，outer_RHS=0；
- background_grid_constructions=4，background_radial_points=4403；
- mean_control_candidates=11，linear_least_squares=13；
- 新科学0.4446435769999937 s。

这个结果使下一输入具体：最后mu/nu、同一完整原均值定义、同一已付尾口以及实际全线性系数均已在原FINAL。应从这些付费数据做真实的s向核心射击，并先实际检查z_s的正性/根。若它在整个返回区间连续正，可直接用
A_s=-3a_s A/a-4z_s C/a，
C_s=3a_s^2 A/(a z_s)+4a_s C/a，
a_s穿零无需除它；核心需C_core=0且A_core非零，再归一A_core=1/2。

若实际发现z_s零点，则必须用准确未除法穿零接口支付连接条件。不能先假定没有根，也不能因条件性零点风险而放弃这个已付输入。继续直接消真实核心失配比重复24基粗拟合更对准本次剩余量；其完整数值误差、连续几何门和后继有限非圆构造仍须实际完成。

本条关闭本次自然运行的收据，没有关闭课题。原FINAL的actual_complete_linear_return_proved、finite_isometric_family_constructed、README_completion_claim均为false。

