# R613：真实457保留全部原行，并加入已付fine最坏半径

日期：2026-11-27；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

## 1. 实际证据与唯一新增工作半径

原normal397 run45909455678/job140214007842在60次声明上限结束，
真实接受态为457，最后一步仍接受；完整终态见
`2026-11-27-r613-normal397-sixty-step-terminal.md`。
原工作merit由`3.4819798214204096e-7`降至`3.470337723851457e-7`，
工作η由`2.216116622493101e-7`降至`2.2088199539082962e-7`。
但同一实际457的fineη升为`2.2449537902118403e-7`；
两种原直接位置η为`2.245094994315899e-7`、`2.2450665803951752e-7`。

这三个实际最坏读数的共同半径是
**`.32708333333333334`**。它未包含在原950工作库：

- 在compact span `[.327,.328]`中，它是fine的第1/12点；工作只取k/6。
- 旧pre-tanh knot所在span为`[.326875,.32796875]`，工作步长为$7/38400$；
  该点距左端为$8/38400$，非整数步。最近原span点与它的间隔量级为$1/38400$，
  不是浮点舍入会改变的同一点问题。
- 粗compact span `[.31,.34]`工作步为`.005`；body从`.30`到`.82`步为`.52/64`，均不含此点。
- 原相位尾半径都不大于`.30`，core半径都不小于`.82`；其他声明特殊点及patch区间也不含此点。

以上是对已发布 `compact.radial_grid`、`knot.radial_grid`、原`radial_nodes`及
准确67knot文字的纸面/源码核查，没有在本地执行网格或科学探针。
原full-S main只在开始构造一次density1 data，solve不自适应加点，
末fine也没有自动回灌机制。因此不能假定前轮已经消化这个真实新峰。

本scope将工作半径准确改为

$$
\mathcal R_{\rm new}=\mathcal R_{\rm old,950}
                   \cup\{.32708333333333334\}. 
$$

只加这一个已付峰，预期951点；运行记录实际unique并验证原950全部保留、
真实新增项就是该原FINAL中的半径。没有另作峰值搜索或旧fine资格门。

## 2. 从同一个真实457继续，原参考身份全部继承

输入是原最后接受1130q，JSON `22777 B`，SHA-256
`a05c4374fe966df1982ae2f3fc5a92129aba03da562670fc848d4a666600b539`。
`H=.5188904014900897`、`amp=1e-5`、真实下一damping`1e-14`，
迭代标号从457继续；最多60次新接受后到517。

原source `12e47b06d7003b2df0a3c77be6d481b30cf226e9`，
原wrapper SHA
`bc4cf1bce2f62a67eac633deedf12a3fa9ba75b1758042b32c9354c87d802ff3`。
原log `2465022 B`/SHA
`6bfe702c7eabfed835ac19125364ad1c2328f8009770f37e97551fbbe08842ae`；
原FINAL `106832 B`/SHA
`da0c9caaea414b6cfd392e2bed4d0665a3837b5d54c922fa5faacc05c14fefad`。

新stdin逐字继承上一完整input `157609 B`/SHA
`79e6d6ce708687decd47fb8eb7a9668f8ca2ebf2351b2f3109fd571c6d692f9c`，
再递归取得原重建文字`31425 B`/SHA
`14970496aa117e859d0605fe8a36414ed9f037be3b846ec10cf3d20708c9f7ee`。
所有原嘴口、67knots、canonical512、force、core和六jets定义不变。
本轮4768.702256165秒、60J/60接受/102trial/42拒绝及全部其他真实费用
进入单独source ledger；4520.668522229001秒及更早费用继续逐层继承，未删或改算新增。

实际fine/direct最坏半径、原η及attainer直接来自这份已绑定原FINAL。
新源同时保存其旧工作merit供追踪，不把它当作新网的初始merit。
FINAL没有保存内部QR/BFGS，后继只恢复真实q、振幅、下一damping和编号，
不伪造线性内部态。

## 3. 完整原算子与新径向权的明确区别

新driver通过准确SHA直接载入原
`r613_full_position_height_20261127.py`，SHA仍为
`6850c9e7f561aadfbc749536b181e1e5e32ff6fddfa6ea3b2de9d08d91b2cfb0`。
原model、complete Jacobian、完整QR/SVD、函数步长、阻尼/回溯、接受条件、
checkpoint与fine函数全部直接调用；不改旧函数、类或已加载模块全局。
新main只有实际输入入口、显式工作并集、来源和成本receipt。

每个工作半径仍为N256、全部奇频1…127的128行；951点合计121728行，
完整J为`121728×1130`，原全部1130列和每个奇异方向保留。
4096行分块的完整增广QR和小R全SVD照旧，不形成normal equations。
额外128行只消费这一实际新峰，不删除任何旧观测或core参数链。

原prepare使用径向邻点距离构造dr权。**它会在并集上按同一原公式重新组装权**，
不保留过时的950网权后再悄悄混入一个无权点。
所以新的初始merit是新951网的有限Parseval/径向求积目标，
不能与旧950网的`3.470337723851457e-7`直接作同一目标的增减比较。
后继内部每个trial仍与同一新951工作目标比较，实际接受才更新checkpoint。

实际开始还会输出真实原/并集点数、新增半径、保留检查、全J形状与按形状计算的字节数。
这些是本次必要模型数据准备的receipt，不是对旧科学结论追加验证门。

## 4. 原fine不缩减，原完整费用仍记

原末态fine保持density2的全部1728半径、N512、双原直接位置步长、
全部D偶频0…128和完整At/M同步观察；同一系数/root/rho pass继续共享R606/R615，
R615保全部fine奇频1…255及其条件观察边界。
那个新增工作半径本来就在原fine内，末fine没有删改、降密度或选择性回避。

仍为60次/5400科学秒/240秒末态reserve，job100分钟；
同一串行height concurrency group，不取消其他原运行。
必要dense/connector/core/height重建、所有新J/QR/位置/line trial/拒绝和末fine均累计计费，
没有新inner Riccati或旧方向门。

驱动 `scripts/r613_paid_fine_peak_exchange457_20261127.py`；
request `computations/request-r613-fine-peak-exchange457-20261127.json`；
workflow `.github/workflows/visible-r613-fine-peak-exchange457-20261127.yml`。
完整新stdin `220270 B`，SHA-256
`9dfae1cd3e908c32ffa23c455b6f9e7df463a43de5a97e119d1cce9e54bf10f1`。
28项source/workflow绑定及全部sparse覆盖已静态核对；本地仅文本、AST、JSON/hash和原log解析。
发布者按真实pull更新规则metadata即可，科学stdin不变。

## 5. 目标量词保持

这个exchange只针对当前实际已付fine暴露的一个工作覆盖缺口，
不能预先保证下一fine下降，也不等于整个径向区间的连续覆盖。
后继若仍有新峰或真自然停滞，应据新的真实终态继续推进。

普通设计链的H/q继续按原求解器变化，**不改R618独立冻结的实际397连续E**。
本有限幅度设计仍未满足固定最终度量的全时间宏观族、持帽位移与reach等README标准。
