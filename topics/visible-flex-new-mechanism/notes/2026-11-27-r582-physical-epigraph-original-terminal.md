# R582 物理回溯/epigraph 修复的原自然终态：保留真实 eta 6.26231e-5 的 97q

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。本条只解析已经自然结束的原完整 Actions 日志；没有重跑源方向核、32 Jacobian、完整细网或 ODE。

## 1. 原来源与完成范围

- workflow：`visible-r582-physical-epigraph-20261127.yml`。
- run `45881470977`，job `140121595702`，触发 source commit `fe523e5c0dc316df8b8434fe5aa446cbe8b98360`。
- job 开始 `2026-11-26 19:09:17 UTC`，自然结束 `19:49:16 UTC`；Actions `success`。
- 原 source driver `r582_physical_epigraph_continuation_20261127.py` SHA256 `c0c5c1c82808ea7b54ad68cc5bfee0a921726dc2bf8dfa2ac725600859133e02`。
- 原请求 stdin SHA256 `4311d0a03166ee5b75d51a4e918c073fece1d1c11a9e033b8d1b6bd0c6efea1d`，284,156 B。
- 原 raw log 10,934,304 B，SHA256 `f1b49317722553d2af94e1666610f02904f03a6b88ff3ce14c16622e6ce6dd66`。
- 原 `FINITE_LOCAL_TAIL_FINAL` JSON 子串 470,115 B，SHA256 `6138076e84aacbbd24e7ad46b4cb9e8db576cf0f5a3fb22305666b878f3f6b4f`。

科学终态仍为 `scientific_clock_checkpoint_not_complete`，stage 0、outer 10、metric phase。新科学 `2370.210179923` 秒，reserve 30 秒；封装子进程 `19:09:42.400528` 至 `19:49:13.621686 UTC`。不是 stage 成功、自然最后 OptimizeResult、固定 g 精化或 README 完成。

run 内实际公开 pull 从触发 commit 到 `0720176a40c71fa09c20f668f4d610482342c2af`，根 README 与课题 README blob 均未变；实际私库 pull 到 `af90a87a2482aff1f91fc3ac0002d8941b590d0a`，认领属于本会话且进行中。没有公布私库内容。

## 2. 真正保留的完整细网状态

最终实际 retained 97q 的 binary64 SHA256：

`f1c8298e0c7c576c1b2230b24146fbe2356e97d7ba0b7b3428dd9e87e53a52bf`。

其接受类型为 `complete_fine_feasible_metric_improvement`；p=.181、epsilon=.0010000000000000009。完整细网为 **11025×3072**，不是仅当前粗行。以下全部摘自该同一 retained 状态的原完整 scan：

| 量 | 原观察 |
|---|---:|
| `eta_max` | 0.00006262308445465524 |
| 物理几何最大违反 | 0 |
| 工作几何最大违反 | 4.259917071869346e-13 |
| 最大原算子曲率 | 16.45256916996749 |
| `mean_E_min` / `mean_E_max` | 0.6389572483008313 / 1.1700944786212755 |
| `det_min` | 0.6389377047956737 |
| `area_min` | 0.21999999999999997 |
| 最大球半径 | 0.7653787458173524 |
| 最大 `abs(y)` | 0.3918260690060719 |
| 最小 z | 0.02 |

eta 观察峰在 `s=.7330078125,theta=2.5504987233245258`；曲率峰在 `s=.8715462299773551,theta=0`。最后该 scan 耗时 `22.256495207999706` 秒。

旧 actual 的 eta 为 `.0004334870087785436`，本次真实完整 fine 已降至上表；这不是把 raw auxiliary epigraph 当成实际 eta。p 没有缩小。当前 stage 目标仍为约 `2.5e-7`，尚未达到，不能扩大 p 并借此宣布完成。

最后一次保留来自独立物理短步，fraction `.25`，独立 lifted epigraph `6.261980780762994e-5`，lift `1.0976013317532513e-7`；其 raw backend q SHA 是 `2f82ddd3caf723c0c4dfdaa701771081417607efa874c3f0264e6b37079a30e0`。两个 q 明确不同，原 SLSQP 点未被回溯点改写。

## 3. 新机制的实际作用与未接受末 trial

源 `f8394b8406fd1725df626a2653f18f14507e71c37f2fbeca44b8192457859dcb` 原来只是未 qualified 的 raw trial。新 run 首次以 fraction 1、epigraph lift `2.2103241456667094e-6` 独立复核完整当前行后，再真实完成 fine；这一次才保留它，eta 为 `7.608306830042544e-5`。随后完整新证据加入径向行，继续原几何门和后端。旧 epigraph `3.4466e-5` 始终没有被追认为它的 fine eta。

本次共 **17 次 metric 接受、5 次几何恢复接受**。23 个物理候选实际提升了 epigraph；39 次新物理回溯行观察，累计16次减半。32次完成的 callback fine 观察、3次准确相同的自然终点 fine 复用、3次相同 p/q/fine baseline 复用都有原记录。

外层轨迹如下；这里只缩写原记录，不重放任何一次：

| outer | phase | 原自然/交换结果 | 本 outer Jacobian |
|---:|---|---|---:|
| 0 | metric | warm q 完整 fine 后接受；新未覆盖峰交换 | 0 |
| 1 | metric | 9 次接受后新未覆盖峰交换 | 13 |
| 2 | restoration | 自然 status=0，原 pending 新峰采用 | 2 |
| 3 | restoration | 完整 fine 工作几何恢复 | 1 |
| 4 | metric | 6 次接受后新未覆盖峰交换 | 7 |
| 5 | restoration | 新未覆盖峰交换 | 1 |
| 6 | restoration | 接受后新未覆盖峰交换 | 1 |
| 7 | restoration | 自然 status=0，原 pending 新峰采用 | 2 |
| 8 | restoration | 自然 status=0，原 pending 新峰采用 | 2 |
| 9 | restoration | 完整 fine 工作几何恢复 | 1 |
| 10 | metric | 活跃后端在科学时钟处 checkpoint | 2 |

三个自然成功仅属于局部 restoration 后端，不能当作 full metric 完成；最终活跃 outer 没有自然 OptimizeResult。

最后 raw callback q SHA：

`c491ecf294e2447f44d7a4e844906c1843c1a1c4cee9bfad5c238f0c73ff3e90`。

它的当前完整行违反 `1.7849159615642546e-7`，来源为 raw epigraph，物理几何行违反仅 `9.592240196587554e-14`；原 raw epigraph `6.23866913861634e-5`。独立 fraction 1 复核抬至 `6.256518298587254e-5` 后，当前完整行违反降至同一 `9.5922e-14`，但它**没有完成全 fine，也没有被保留**。后继只可将其标为独立 warm trial，必须重新完成尚未完成的接受步骤；不能冒充上节 retained q。

## 4. 实际网格、pending 与恢复入口

- actual constraint：243×1536；243径向 binary64 SHA `30008c5092c32a76d539b3c9ae7059af04cc1d49e4206fc42f157ca22bc7b735`。
- actual fine：11025×3072；径向 SHA `52fb28eafcee0110ac12d989a96f6f33871ab395b6b2c3bd448a73a90196fe4a`。
- pending 径向0；pending angular false；proposed 网格与 actual 同一243×1536。
- actual backend trust、planned trust、next trust 全为2；未重置旧初始 trust。
- 更早来源未采用的189×3072约束角 proposal 仍完整保留在 ancestry，未伪称已构造或通过；3072 fine 角一直保留。
- 材料 mesh SHA 仍为 `0d222bd12ce8a61d0c88264c6fb5c82066f0ca058855b5bf7a670a53b483a991`，62878共同端点、62877单元。

后继从该真正 f1c8298… retained 状态、243×1536、全部11025×3072 fine、trust2和空 pending 继续；源最后 raw trial 只有另列 warm 资格。没有已公开 BFGS 工作数组，不能声称跨 Actions 恢复原内部 Hessian，但不重做源32 Jacobian。

## 5. 全部新成本保留

新科学2370.210179923秒之外，原 `prior_cost_ledger` 完整继承；以下成本不从账本扣除：

- 32个新完整 Jacobian，416个8方向 block；原 `JOINT_BUDGET_JACOBIAN` 秒数合计 `748.4066567820013`。final 的 completed-outers 中30个加活跃后端2个，不能只写30。
- 114个 backend value evaluation：已完成外层104，加当前活跃外层10。
- 最后实际 Jacobian 为842238条完整标量不等式、97物理列，全部 value reconstruction difference=0。
- 40次**完成的** fine scan；3503个完成的径向 block，445853个已观察径向点。这些 block/point 累计也保留最后尚未完成 scan 已付部分，不把它们都改称完成的 scan。
- 1369660416个 R604 同原几何数组观察点、3503个重用 block；额外几何/AD调用仍为0，观察耗时仍计在 fine/scientific 内。
- 必要新材料构造：160段，dense outward RHS960944；core forward RHS2510、short backward RHS206；原 inner DtN和三seed比较没有重算。
- 原 actual weight calls1023386；dense径向查询62443；材料/商半径查询101028；height查询3166、cache375、QUADPACK RHS235893。
- 新材料 stable residual preparation 62877 cells；62878共同端点。旧七点诊断与已付97q方向核没有重播。

## 6. 不转授连续 reach 或固定 g

该新 q 已改变 mean 控制和帽高。它相对**旧**圆参考的有限 R604 观察为：C0 `.01801014312136661`，C1差算子范数 `.15345292904612884`，导数范数 `1.1448585137967737`，法投影差 `.05980450701767831`，帽高差 `.012008336832480815`。这些均只是原细网观察；不能借旧 q 的 `.001` 位移或 R611 的旧圆参考，把新 q 视为相同的小扰动证书。

后续严格几何采用新 q 的全部 mean 控制和帽高、圆 core 半径 .38 建立**新的**比较圆面，并对该新圆面重新支付连续几何；材料 seed 商所用旧冻结半径仍不改变。这个选择不会自动继承 R611/R599 资格。

当前完整 metric 仍是设计阶段，mean g 未冻结；有限非圆等距族、连续全角/径向及全点对 reach、无限核与有限样条的 C² 误差、宏观握持振幅和 README 全部完成门仍未通过。本收据登记真实下降，后继正常继续完整求解，不在此停止。
