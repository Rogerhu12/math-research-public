# 03b 首个完整 hDelta 场与首个零闭合根失败的实际返回

## 1. 本次独立来源

本记录只读 [run45820592817/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45820592817) 的[阶段1–5](2026-11-26-public-actions-45820592817-1-part-001.md)与[阶段6](2026-11-26-public-actions-45820592817-1-part-002.md)。旧03的stage7子进程结果仍未知，不用本次结果回填。完整report、向量、缓存和日志只在runner，本文仅保紧凑实际数值与来源。

本次warm真实248.22315183700002秒exit0；必要reference准备真实313.700224134秒exit0，source4e65577d、checkout `ddf97130a9fad1903c6983575689e6791bcbf328`。新输入如下：

| 对象 | 实际SHA256 |
|---|---|
| preparation report | `02ddd35fed7b9c021847b7b0aa5108161547cc8b39195bca14394f6bc138f90d` |
| reference bundle | `0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1` |
| observation carrier | `b0257d9e03da36a422eab4e424942d38ccf817ac40ceb3b42be4378b1260966f` |
| 固定scalar profile | `6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb` |
| reference model | `3f62a03da637495af340f8da6ac31f0d7993fa6e769f7bcab1ed45b8dc7f19b2` |

完整原M160/J923/N2048与7377观察、1250/208/18曲率/半径/保护地点及1782原始出现次数都保。准确无限尾包围有效，1448 leaves，仍未达到请求scalar tolerance；半径carrier为 `0x1.2124d67c6a7adp-1`，已返回半径误差上界 `2.3765777896593284e-13`。这只是准备，不是整场误差证书。

## 2. 完整 hDelta 实际方向

实际stage3运行606e完整driver，checkout `f306df2d3b1a8ceff7250111228e091b9cfbc058`，自然854.478205233秒exit0。父即上表reference；实际完整模型 `9d4ccb16efe9a0c0f5b077c0e8919e76d1d04b06e669588b32e2de78c92f0258`。

- 初场bundle：`81b3dd28c7c0398c1bf87a8d60e92b45d1c879e778bca96d617e4260a175bb83`。
- 末场bundle：`fbf2b38ca6b4557568d06b05f91589ac4d463f660c877a2cb39396ab0cfe0337`，10720288B。
- 完整report：`989740cd8408c317b4540c3efa82b6ab35de269dcb200932f4d1d19d370773d1`，12489973B。
- stage4纯6d54 reader真实6.004563884000163秒exit0，产物 `2e52feaa0142a87cee16ca12256c58a70a9c8a2f247777574a5debe1bb09c3e6`，21661B。

| 实际量 | 初场 | 末场 |
|---|---:|---:|
| max relative Gram | 0.5170375580125983 | 0.5154401838413587 |
| centered Phi | 213.89131075534186 | 212.14818770844644 |
| maximum physical g | -0.024430047350427198 | -0.024554299879619434 |

纯reader实际给出同目标Phi差 `-1.7431230468954197`。全部1333370自由量与45324288原完整行保；一个metric方向真实接受，零个restoration方向，末mu `.01`，终止原因仅 `declared_metric_direction_budget`。alpha、该QP状态/Pg/tolerance和试步详情还未从当前公开selector读到，不填猜测；继续纯归因再选充分内层预算。

末有限几何筛确实通过：necessary reach product `0.749220230610006`，完整1283曲率/262半径永久点、每点正负两支都读取。幅度五g分别为body `-0.024554299879619434`、plus `-0.1377800864577554`、minus `-3.309031309068155`、cap `-0.06729638441434593`、H `-1.040989220273277`。这不是连续reach、整像保持或完整D的证明。

实际J/J*调用18/19，residual11，point covectors33，reference求值11647次/14593431点，完整field point计数208152621，inverse图38781次；当前最大数值inverse残差 `4.440892098500626e-16`，最小读取rho `0.16599098272799284`。这些是本次工作读取，不直接充当真逆根误差盒。

当前约0.515的最大误差远大于本题阈值，不能称候选已近完成、已精化或粗层驻点。此场不因此被安排昂贵整域证书；同场完整费用组件继续完成，以便后继真正小误差场使用。

## 3. 零闭合首输入的真实根失败

stage5沿同一新reference使用完整b4d7/5b4c来源及原窄bubble参数，checkout `eb1065c65924ec222f2e8a454dd7680ba2bb3605`。真实11.00651035199985秒exit1，初场读取在第一角block抛 `EndpointRootFailure`：failed indices `[0,1,7]`，maximum actual residual `0.37016474660679566`，maximum actual correction `0.07228725875791846`；原因是全部原backtrack未降低同一完整端点方程。

完整report `00a00590f7b38a3067220d9addfeba7ea2ef8bcc8343d3b9806a20a9e0b2a6a5`，81746B，`complete=false`。没有initial或final场，未调用J/J*，没有完成方向。原root tolerance `2e-12`、24 iterations、18 backtracks、Armijo `.0001`、branch radius `.5` 保持；失败候选被拒，没有用零根代替。

stage6 b25纯reader真实6.000651554000115秒exit0，产物 `e5fe08d36905cf3c323fce70c3f4e4b56ca18c21749ce9f256d5f79881e45666`，20872B。它正确读到initial/final/Phi change为null、root grid未完整、root角成功数0、一次失败；source/model与同一reference全绑定。summary尝试读取不存在的初末指标而报告missing/NoneType，均为真实未产生，不把缺字段当零。

该失败不证明统一IFT不存在，也不证明全部输入不可解。下一输入扩大两支内部bubble支持，保完整物理/implicit J/J*/原变量/行/几何与root验收设置，并在新模型/新目录实际尝试；不迁旧hDelta场的数值或证书。R695、全域metric、全t几何和固定问题真实精化仍未完成。

## 4. 紧接的实际请求

已追加同一6d54完整reader的新fresh输出，请求第一个完整方向的alpha、QP状态/advances/Pg/tolerance、mu、原C/幅度行数、first/last真实试步与trial_count及实际预测量。它只读原report和source，不重复F/J。之后排[宽支撑完整尝试](2026-11-26-zero-closure-narrow-failure-wide-support.md)及其纯reader；新输入只改变六个精确bubble参数和输出目录，全部其余科学argv逐字符串相同，仍拒绝未解根。

## 5. 同一首方向的实际详细归因

公开03b阶段7由原完整6d54 reader正常返回，实际秒数 `6.014455128000009`；同一读出文件仍为 `2e52feaa0142a87cee16ca12256c58a70a9c8a2f247777574a5debe1bb09c3e6`、21661字节，实际source commit为 `e61c4cd60a8e623714afcda45ef920b4ba619c46`。本次只是增加原报告已有标量的公开投影，没有重算方向。

真实接受步长 `0.0078125`，共8次回溯；QP状态 `iteration_limit`、16 advances，末投影梯度 `2550.6296140330887`，原容差 `0.002450868590297488`，活动面0行、最大线性违约0。原选择器预算192，但该方向实际产生28条原几何行，加6条幅度行总计34；没有删除已生成的原约束。行缓存362676640字节、重复前缀缓存0。QP实际399.32366009399993秒、完整方向699.7715167929999秒；QP J/Jtranspose为17/18，完整方向为18/19。

首试alpha1实际Phi未下降，未做完整几何读取，也没有read error；末试alpha1/128实际Phi下降且完整真几何接受。中间6次的拒因不从这两个端点推断，已排[全部8次纯归因参数](../computations/resume-20261126-axisymmetric-all-eight-trials-step.json)。原half objective slope为 `-112.01558056689831`，全步预测Phi变化 `-112.01558083426353`，coordinate step norm `0.051707153464990455`。报告的 `actual_to_full_prediction_ratio=0.015561433810484962` 使用全步预测作分母，不能充作被接受缩步处的模型准确性。末mu仍 `.01`；尚不把更大内层预算选定为下一科学输入。

完整实际命令和所有身份见[阶段7原记录](2026-11-26-public-actions-45820592817-1-part-002.md)。此次有限下降不是QP驻点、固定参数精化或连续度量证书。

## 6. 全部8次实际试步：主要拒因是几何

公开03b阶段10于 `6.021842170999662` 秒正常返回，source commit `ac374c51fea548d19cf875edf79d6b53ed1b5f4b`；原完整6d reader、原989740cd报告、fbf2末bundle、固定6ffc目标及读出SHA/字节数均与§5相同，只公开投影增加了全部真实8次地址。summary errors为0。每个实际trial的domain均为true、read error均为null。

| 实际alpha | 同一Phi | 实际positive physical g | 完整几何读取 | 接受 |
|---|---|---|---|---|
| 1 | 228.42395861866115 | null | false | false |
| 0.5 | 139.25436301509788 | 31.90436616181289 | true | false |
| 0.25 | 165.55863915376247 | 15.500572782613311 | true | false |
| 0.125 | 187.7115637415427 | 7.27473500670862 | true | false |
| 0.0625 | 200.3423646934129 | 3.155814733918934 | true | false |
| 0.03125 | 207.00381415620961 | 1.0948541225127562 | true | false |
| 0.015625 | 210.41926124692344 | 0.06399761652393754 | true | false |
| 0.0078125 | 212.14818770844644 | 0 | true | true |

alpha1未达到真实Phi下降，故没有读取完整几何；其余7次都真实Phi下降，前6次因完整物理几何不满足被拒。alpha1/128才通过。因此不能把这次小步接受归因于中间6次Phi模型失败，也不据此直接排只增加内层64预算的草案。下一步先用[完整原报告纯归因](../computations/resume-20261126-axisymmetric-first-geometry-rejections-step.json)读取各物理约束族及实际最差地址，再接完整全C分离/必要校正；原已生成28+6条必须保留，新的地点与双符号也不能丢弃。

全部实际原值及未在此重复的minE/det/max来自[阶段10完整记录](2026-11-26-public-actions-45820592817-1-part-003.md)。这次追加只复制已有真实标量与解释拒因，没有本地计算或重跑方向。

## 7. 阶段13的实际完整几何归因：同一core胞内曲率触发六次拒绝

[03b实际阶段13](2026-11-26-public-actions-45820592817-1-part-003.md)纯读出在6.019553217000066秒exit0返回，source commit `453f89d785dd73570dd6abf9a4bd63f99d69b1ec`。完整6d54 reader、606e报告989740cd与fbf2末场、6ffc准确目标逐项保持；输出仍是21661字节的 `2e52feaa0142a87cee16ca12256c58a70a9c8a2f247777574a5debe1bb09c3e6`。summary errors及missing outputs均为空，没有重算F/J或新方向。

| alpha | 原reach物理g | 最大绝对主曲率 | 完整D点下界 |
|---|---|---|---|
| 0.5 | 31.90436616181289 | 265.489049262913 | 4.130285380024057 |
| 0.25 | 15.500572782613311 | 132.8445535364406 | 4.138313626356596 |
| 0.125 | 7.27473500670862 | 66.52230570866907 | 4.142337380242727 |
| 0.0625 | 3.155814733918934 | 33.361181803684474 | 4.1443523177395765 |
| 0.03125 | 1.0948541225127562 | 16.780619853421797 | 4.145365587885238 |
| 0.015625 | 0.06399761652393754 | 8.490338878848396 | 4.145879340398287 |
| 0.0078125 | -0.24277976938999402 | 6.023435406882225 | 4.146140200734207 |

前六条Phi下降试步的 `maximum_physical_g` 均恰为表中reach物理g，全部五幅度族g均严格负；每次全部永久曲率与半径地点均已读。六次最差曲率地址均为 `cell=0, u=0.5, phi=1.5707963267948966, branch=0`，phi是实际binary64字面，不能悄悄换为某个别的角点。故此次拒绝的具体原因已落实到同一个核心邻接胞内部的曲率，不能再当作未读归因或仅凭小步长猜测。

被接受的alpha1/128最差曲率地址改为 `cell=0,u=0,phi=0,branch=1`；完整maximum physical g仍为 `-0.024554299879619434`，主导族此时是body直径。必要reach product `0.749220230610006` 与接受一致，但这些有限点筛仍非连续reach或闭嵌入证明。

后继在实际fbf2末场上重新建立完整原选择器的全部前缀与幅度行，并在QP前补读上述已知胞内地址的两条主曲率分支及当前完整D的配对导数。之后冻结已生成的全部C，真实下降但几何失败的试步只追加完整自由空间的新分离行/二阶校正；不删除原行，不把历史34条缓存还存在作为假设，不把旧场上的row数或数值移到新场。若扩展地点使当前父已不满足物理筛，先如实进入恢复，不假定零步可行。
