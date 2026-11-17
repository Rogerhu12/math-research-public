# 同一C²初猜端点：单改二阶rho余量的实际入口

维护：Astra-held10-7322d0de-20261118。

在完整记录原C²初猜失败和单状态域拒因后，新增owned入口只使用已验证的二阶rho插值充分余量。原控制曲线的定义和逐点jets不变，原triangle/一阶余量保留，原rho>1e−5及32768格上限不变。共享C²初猜、材料回拉、原Newton/Jacobian、原Frenet/BC/merit、原实际尾及全部最终门均不改。验证和独立数学审查见 `m3-raw-core-second-order-guard`；通过core数值守卫仍不等于通过BVP或几何目标。

独立目录 `m3_work/beta4625-q039912-raw-lam1-b032-w040-m16-c2guard`，session14903已启动同H实际尾加载，尚无新prefix终态。配置仍q=.03991248545080898、λ1、a=.21、bp=.32、bc=.4、M16/N512、tail N256/parts16/steps16、maxnodes6000。原全部16维初始p、15个物理raw控制、初始H、profile、settings、原/新repair函数来源SHA均与已结束C²入口逐值相同；tail config只有trace输出路径改变。相等口径仍是两次λ1/C²入口，旧accepted λ.02到此入口的首c负1 ULP重编码已登记且原样保留。

新源为 `couple_m3_raw_circle_endpoint_c2_guard.py`、`continue_m3_raw_circle_endpoint_c2_guard.py`；它们独立派生，原C²入口和 `round_raw_lib` 都未覆盖。checkpoint增加数值guard种类标签，核心类型、物理settings和control path仍原定义。底层新界在 `raw_second_order_core.py`，原初猜窗安装器继续不变。

新run的bridge和sparse-helper使用当前会话可用副本，SHA与历史输入相同；原旧路径、当前路径和预期SHA均列入 `circle_endpoint_second_order_guard_entry_record.json`。只变存储位置，不据此改变物理来源。原prefix和tail checkpoint仍为先前相同完整输入，必要系数分块SHA一并记录。

这是一条算法续跑入口：同一参数向量下g和方程完全相同；求解时δ仍是原未知量，不能把后来若得到的另一个解自动叫固定g精化。必须取得原完整coupler、实际尾和全metric终态后才能继续判断。
