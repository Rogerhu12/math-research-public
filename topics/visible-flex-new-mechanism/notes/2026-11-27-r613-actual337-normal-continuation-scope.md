# R613 实际337的正常续算：原完整 S 方法与全部状态、费用连续继承

日期：2026-11-27；会话 `Astra-new-mechanism-1f4a61a4-20261127`。

## 为什么继续原方法

原 run45891036836/job140153472856 在 60 次迭代上限自然返回；
最后一次方向仍有可分辨且被接受的下降，终态不是驻点。
原始证据和全部费用在
`2026-11-27-r613-full-position-sixty-step-terminal.md`。
本 scope 从它的**实际 iteration337** 接着求解同一个完整位置目标；
本地只准备和核对源、JSON、AST、hash，不执行科学。

实际 q 为 1130 个参数，JSON `22696 B`，SHA-256
`238d786c6134bcbd356958c5fcf263916feb5bf1004af7e93722a30ed591e1c7`；
保持 `amp=1e-5`、`H=.5188903591561069` 和真实下一 damping `1e-14`。
高频增长后的原系数全部继承，没有换回中途较小 η 的 q，
也没有降低 amplitude、移动径向节点或重拟合种子。

## 新入口只读实际新输入，数值流程直接调用原源

新入口 `scripts/r613_full_position_resume_337_20261127.py`
以 SHA-256
`6850c9e7f561aadfbc749536b181e1e5e32ff6fddfa6ea3b2de9d08d91b2cfb0`
绑定原 `r613_full_position_height_20261127.py`。
它只替换实际 checkpoint 的输入读取函数和本次 receipt schema；
`driver.__file__` 指向新入口，使原 main 打印的新 source identity 诚实对应入口。
原 module 的 `HERE` 及所有依赖在此之前已绑定同一 scripts 目录。

`FullPositionHeight`、完整解析 Jacobian、checkpoint、solve、
完整行 QR/SVD、全部方向、函数空间 step limit、line search、damping 更新、
原 fine_readout 和所有原计数器，均直接使用原驱动中的函数。
没有复制后重写这些数值函数，也没有把旧计算结果伪装成新缓存。
原 solve 已经从 input_state 读 `first_iteration`，因此新轮首个 checkpoint337，
实际下一接受态338，最多正常推进到397；它没有硬编码277的续算编号错误。

原运行没有保存 QR 因子、BFGS 矩阵或其他线性内部态。
此处恢复的是实际 q、amplitude、下一 damping 及费用，
下一轮必要的 J/QR/SVD 正常重新形成并计费；不声称恢复不存在的内部状态。

## 绑定和输入传输

新 request 为
`computations/request-r613-full-position-resume337-20261127.json`，
新 workflow 为
`.github/workflows/visible-r613-full-position-resume337-20261127.yml`。
共24项 source/workflow 字节身份绑定。

完整 stdin 为 `108233 B`，SHA-256
`0d8e87ebab7135065c153c6c285b9d64fdff693dcd49a4c0bc20bdd9869fde22`。
它带原337 q 的完整原 JSON、原 run/job/source/raw-log/FINAL 身份，
以及前一 scope 的完整 `67172 B` 输入原 JSON，后者 SHA-256
`b21486214dbec1ddd6033a2a90218a91150d6e0b271a12b104aa6ed3203694c4`。
从该原输入读取同一个 `31425 B` reconstruction，SHA-256
`14970496aa117e859d0605fe8a36414ed9f037be3b846ec10cf3d20708c9f7ee`。
因此旧 pre-tanh/canonical512、post force、67 knots、
全部 true mouths 和原 core 链不是另行猜造的一份输入。

新入口 `5880 B`，SHA-256
`be14efea5d19f5b787ff4190d24e2d50b7de67989b2e0c23096e022b3b7e8cec`；
新 workflow `4465 B`，SHA-256
`51ae23aebc846479fb290d37787f9bda8ee90ff9f91e32ad50f5d4f11ce0db81`。
request 的规则已读 commit 由发布者用真实 pull 后的已读身份登记，
完整科学 stdin 不因该元数据更新而改变。

## 原范围和终读出完整保留

- 工作仍是 `950 × 256`、全部奇频 `1…127` 的128个位置坐标/半径；
  完整 J 为 `121600 × 1130`，4096行完整增广 QR 和小 R 全 SVD。
- 原 1130q、所有原径向点及每段 compact span 保留，
  fixed512 old-tanh mean、原 force、core 全部六 jets 和全部参数链保留。
- 全部已付内口复用，新增 inner Riccati RHS=0；必要的旧 dense
  connector/core/height 重建仍如实计本轮新费用。
- 以前付过的 fine、R606/R615 或方向诊断不作为入场门重跑。
  新实际末态只按原驱动做一次 fine `1728 × 512`、两种真实位置差分步长、
  全 D 偶频0…128、原 At/M 全正谱同步读出，以及共享一次系数遍历的
  R606/R615（fine 全奇频1…255）。
- 新60次迭代、5400科学秒、240秒终读出 reserve，job100分钟；
  仍用同一高度串行 concurrency group，不 cancel 原运行。
  Python/NumPy/SciPy、原容差和所有物理参数不变。

“原末态没有通过2e−9”不是本轮预设重放一个旧门的理由。
本轮的终态判据仍由新实际 q 的原 fine_readout 执行；
没有把新的同场 R615 条件界升级为连续、全时间或固定 g 的证书。

## 费用和结论限度

本次输入逐项继承前一原运行的 `2961.020285526` 科学秒、
60个 J/67800列、60个QR/SVD、226 trial、60接受/166拒绝、
原全部必要重建和位置差分计数。它们在
`source_cost_ledger` 中明确是前次费用。
更早 compact/full682q/eleven-mode/paid receipts 在 `prior_cost_ledgers`
和完整前次输入中保留；嵌套账有重叠，不重复加总。
本轮所有新尝试、失败、拒步、实际接受态和未接受 pending trial
由原完整 receipt 路径分别保留。

该续算并不声称已经固定一个连续 E，也不变更 R617 有限角带严格零缺陷障碍。
真正固定 E 的 growing-post 完整高度/Jacobian/core-τ 实现继续并行推进。
只有原续算自然末态到达后，才据真实新 q 和原日志决定下一输入；
本 scope 不用预想的后续数值替代实际终态。
