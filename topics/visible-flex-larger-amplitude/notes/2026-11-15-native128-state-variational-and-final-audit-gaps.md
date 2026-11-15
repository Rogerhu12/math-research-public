# 113 之后：持续128状态、匹配变分与原最终物理消费者的最小缺口

AI 协作记录：amplitude 与 ChatGPT /root（GPT-6 Astra Pro），2026-11-15 UTC。

本稿仅为源码与代数接口分析。113 首跑在原 ready 输入缺失处停止；[历史输入修复](2026-11-15-native113-frozen-input-restoration-interface.md)已发布，第二run43688981685/source8d68a39e79eb1f0c976868d69f87d27fa3f2acbb/job132735373768已进入科学步骤，尚未读回高精度残差。以下衔接以未来实际113结果支持为条件，没有新请求、运行、接受锚、数值结果或额外数学门，也没有开始编写另一个完整求解器。

## 1. 先持续保存真正的128状态

现113 C++ `evaluate()` 每次从同一原64 base/delta 生成 `base+alpha*delta`，在128中完成全部226态 root、RHS、RK与129248残差行。这适于回答同一方向的实际下降问题，但没有多次接受之后的状态所有权。

后续最小变化应是让同一个128进程拥有完整577×224 shooting状态。真实接受时直接保留这份128向量，后续 root、四个RK中间状态、残差、下一试探都从它产生。JavaScript/Python只管理显式协议和临时生命周期；可用有明确端序/格式的128字节，或可往返的十六进制浮点字符串传递状态。普通JSON number、`Float64Array`、`numpy.float64`及旧checkpoint均不能充当该状态的唯一保存形式。

若仍需要原消费者的64投影，应单独标明它是四舍五入投影，并保留128 owner。把已接受128状态折回64，再在旧Node对象中评价或进行最终audit，会改变所评价的状态；不能将该路径称为持续128精化。

113仍提升原64几何、角表、far、scales及cut target字面输入。后续也须明确保留或显式改变该输入约定；它不等同重新高精度求几何、更高阶径向离散或连续ODE证明。

## 2. 旧64 J 可以先提供近似方向，但右端必须来自新完整残差

设新owner的完整残差为 $F_{128}(x)$。旧64 stage J与R273可以继续作为近似导数或预条件器，条件是：

- 方向的右端来自当前128状态的全部cut、576个stage及far残差，不复用旧64残差；
- 进入现有64求解器的缩放/舍入须明确记录，返回方向仅是候选；方向提升后在128状态上累计，所有实际回溯仍使用完整 $F_{128}$；
- 若旧J重新在 $\operatorname{RN}_{64}(x)$ 上形成，应如实标明其基点是当前128状态的64投影；
- 正阻尼R273模型、完整实际回溯与原最终容差各自负责其原作用，不能把近似线性解称为新128方程的精确Newton方向。

现 `exact_20261114_native_damped_chain_qr.py` 真正调用的是 `dgeqrf/dormqr/dtrtrs` 双精度LAPACK；`longdouble`仅用于部分系数形成和诊断，随后仍转回`<f8`。因此现QR可复用为候选/预条件组件，不能只换输入类型或名称就称128 QR。原dyadic全行消费者也只证明所保存64有限数组的仿射关系，不自动证明新128模型。

这是一条可先小改状态所有权、再由真实非线性下降判断用途的路径；它本身不提供匹配的新128敏感度或最终DN Jacobian。

## 3. 匹配新J的可复用结构与局部导数责任

已有 `geometry_20261114_noj_matched_variational_engine.mjs` 提供可直接复用的结构：先完成原no-J RK一步的四个真实root/RHS，捕获这些相同状态与root，再传播完整226×224切向；切向阶段不重解另一个root，不改变primal。这一结构适合迁入128 owner，但其中的数组与算术目前仍是64。

在固定几何/角样本下，记原有限角积分的非线性项为 $q(L,Q)$，momentum目标为 $t(\Pi)$。隐式方程是

$$
G(L,Q,\Pi)=L+q(L,Q)-t(\Pi)=0.
$$

113使用 $e=L-t(\Pi)$ 避免形成消去严重的旧减法。匹配的实表达式导数满足

$$
B=I+q_L,\qquad
B\,dL=t_\Pi\,d\Pi-q_Q\,dQ.
$$

在同一实际近似root处形成 $B$、右端和RHS导数，再按同一RK组合传播，得到的是该隐式方程在实际近似root处的线性化。这还不能称为有限停止算法所返回场的精确Jacobian；捕获同四个RK现场只是避免换基点的必要条件，不是消除root停止误差的充分条件。

具体地，令原有限停止程序返回 $\widetilde L(y)$，其中 $y=(Q,\Pi)$，并保留它的实际隐式残差

$$
\varepsilon(y)=G(\widetilde L(y),y).
$$

若在同一固定分支的实表达式上可微，则

$$
B\,D\widetilde L=t_y-q_Q Q_y+D\varepsilon.
$$

前述隐式公式省去了 $B^{-1}D\varepsilon$。仅有 $\|\varepsilon\|$ 很小，或达到 `8e-14` 等相对停止阈值，不能自动界定 $\|D\varepsilon\|$；不能据此把近似root的隐式J称为实际有限停止映射的exact J。

因此新接口须明确两种不同责任。第一种是 `implicit_root_linearization_at_actual_approx_root`：保原root策略、实际残差和线性化语义，作为近似导数使用。第二种若确实要对应有限迭代程序的实数延拓，则必须在固定实际执行分支下对整个root迭代、其中的矩阵形成/线性解、已选回溯系数及返回步骤求导，再接RHS/RK；停止或回溯分支改变的边界不能当作同一光滑公式。二进制舍入程序本身也不能不加语义地称为通常意义下光滑可微。额外严格root配置是独立算法配置，不能靠更严阈值的名称把这些区别抹去。

当前113没有实现上述第二种root程序变分。最小后继应先如实使用第一种近似语义，并保存实际完整残差/误差；若需要更强一致性，再依据真实结果支付相应变分，而不预设任何新root误差阈值已经获证。

这里有一个具体不能省略的区别。旧 `78718-tail-fourier-product-jacobian.mjs` 用六组Fourier矩及乘积和差公式构造局部J，并独立生成相应sin/cos表。113提升的是各自已有64角表字面值，以及各自已有64 `w/w2/E`。在这些独立冻结系数上，连续三角恒等式及诸如 $E=1+w^2$ 的精确实数关系不能未经说明就当成有限字面系数的逐项恒等式。最保守的匹配实现应直接对113实际 `root_evaluate` 中的角向quad表达式取偏导，再对实际split RHS取偏导；现乘积矩结构只在其与该有限表达式的关系被明确后复用。旧50/54的切向形成改善没有支付这一新primal+变分链。

完整J无需构造成129248平方稠密阵。可以继续使用逐stage224×224块，或在同一root/RK轨迹上实现完整方向作用。若用旧64因子作预条件器，原理上可对匹配128算子做完整线性残差修正；是否值得实现须依据113的真实费用与下降证据，而非在本稿中先假定成功。

## 4. 全行装配保持原方向与边界

原core从较深节点 $x_{n+1}$ 经过stage映射 $\Phi_n$ 向内得到节点 $n$，stage残差为

$$
F_n(x)=\Phi_n(x_{n+1})-x_n.
$$

所以匹配线性作用为

$$
DF_n(x)v=T_n v_{n+1}-v_n,
$$

其中 $T_n$ 已包括原momentum端口除ratio。原cut行为 $Q_0-t_H$，far行为 $\Pi_D-G_DQ_D$，不能删掉或将其改成软投影。全部原scales也参与原归一范数。

两条mean演化仍保在每stage的226态与切向中；它们不反向耦合shape的原结构可以复用，但不能因此丢掉最终物理读数所需的mean贡献。原17/31-prefix问题与此native内部状态维数不同，不应混用两边的坐标或验收。

## 5. 最终cut、敏感度与audit是独立的实际缺口

现113 packet只导出残差用的 `r,drdx,w,w2,E` 及实际no-J/cusp步表。它尚未提供物理二阶jet需要的 `dlogwdx`，也没有导出原完整audit自己使用的所有查询/推进记录。保持原方程和最终门的后续实现必须补齐这些实际输入与消费者，不能只给root/RHS换精度。

| 现有消费者 | 可复用的公式/结构 | 真正128链仍须完成 |
|---|---|---|
| `cutJets`、`f6tail_momentum_physical_jets.mjs` | 原cut momentum乘ratio；隐式root的径向导数；slope/second/mean | 同一128状态、root、RHS和完整几何jet；不先投影到64 |
| `tangentGraphAtCut` | 原576段及完整far graph边界 | 在实际新状态形成的匹配变分；旧图病态不能仅凭更高精度宣称解决 |
| `actualSlopeJacobian` | 原物理height换算、第一斜率及mean-slope解析链 | 使用实际新graph/J与cut root，完整112列；原R273正阻尼逆不能冒充无阻尼物理解导数 |
| `heightJetJacobian` | 原沿实际graph的对称差分；原第二jet/mean-second行 | 所有扰动、cut评价和差分在128 owner内；若改为解析导数，须作为独立实际实现说明 |
| `audit` 与 `f6tail_actual_metric.mjs` | 原每stage/每profile物理jet、Darboux、metric、holonomy、曲率等 | 原查询范围与推进、完整128物理/角向消费者；只返回前几stage改善不够 |

`numerical-tail-slope-jacobian.mjs` 当前只替换第一斜率和mean-slope行。第二jet、mean-second仍沿原对称差分；它不是现成的完整解析高精度DN导数。对应原完整height边界变分可写成对同一完整全行J的112个物理输入右端求解，再经cut jet链求导；若借正阻尼因子加速，仍需区分预条件器与真正无阻尼线性问题。

末端对prefix的真实H请求也必须重新在新owner内形成目标并求解。113的旧target输入只是本轮诊断口径，不使失败base成为可复用成功锚。原actual-H完整FD、same-client责任及fresh最终audit保持；把round到64的对象喂旧audit只能得到那个64投影对象的读数。

## 6. 源码依据及当前可交接口

本稿所读的固定源为：

- `geometry_20261114_noj_matched_variational_engine.mjs`：`f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9`。
- `78718-tail-fourier-product-jacobian.mjs`：`205b28dbde3b43392ef8ad0a915e9f4265264f4663b5bc2a0ea34421516cfd25`。
- `78718-tail-tangent-core.mjs`：`ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`。
- `numerical-tail-slope-jacobian.mjs`：`206d82d3b41e6b9ce24b26447a2026c19c1c7126765107c23d58e55da25639e2`。
- `f6tail_momentum_physical_jets.mjs`：`2b96df25211c5d6ebfc7faf689ea7035704bf0bf7c1ea3aa50b1c137fbe39ea8`。
- `f6tail_actual_metric.mjs`：`36e4e642014d5afd733ed3fecc13267d23c40927e1bd2113e53abcdbb588dcb4`。
- `exact_20261114_native_damped_chain_qr.py`：`9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`。
- `exact_20261114_native_allrows_dyadic_residual.py`：`0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f`。
- 原113 CPP/bridge/probe继续为 `1b59cd10…` / `3655c81a…` / `ba3564ca…`，完整SHA见已发布113接口。

最小未来接口可明确分为 `state128`、`evaluate128(state,root_policy)`、`direction_from_fresh_complete_residual`、`accept_trial128`、`matched_variational128`、`cut_and_sensitivity128`、`audit128`。这些是责任边界，不是已经存在的可调用API。先等113实际评价回答旧完整方向在两种显式root配置下是否下降以及费用；再据结果选择是否先实现持久128状态与近似方向迭代，或者必须先支付匹配变分。当前没有把源码分析当成新的科学结果。
