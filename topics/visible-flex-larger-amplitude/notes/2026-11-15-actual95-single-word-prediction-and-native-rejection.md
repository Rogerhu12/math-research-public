# actual95：单词线性下降未兑现为原非线性下降

类型：公开Actions数值证据；第4节是针对已记录表达式和浮点字的舍入推论。作者：ChatGPT（amplitude；root整理发布）。日期：2026-11-15。

## 实际执行与可复算来源

原[run43675377211](https://github.com/Rogerhu12/math-research-public/actions/runs/43675377211)，source commit `90da0e1195100053583134f2714aa3b43ff6282d`，job `132694243435`。科学步骤失败，原artifact与出版成功。artifact为 `14147191145`，263859705B，ZIP SHA256 `c53f3c0176cf5443a0f58171953d4946887eb4c8dcc04035d2b7f5598a184148`。

本次只读主控已取回47件小原件，未重下完整ZIP或另读完整J大数组。取件清单24100B，SHA256 `46ebc6a4b0fd2a8d5882909fa46fa2614766445f45cd755635b313c6293e0903`。

复算使用上述commit的 `public-native-word-first-request.json`，入口 `geometry_20261115_native_word_first_current576_solve.py`（SHA256 `69c9a8d5cccfcfdcdda35c475b089609c789747803a7b363a17fb67c5bae28d0`），hook `geometry_20261115_native_word_first_current576_solve_hook.mjs`（`932961ef9f267f95f5de6bb28791ed43ef2c66d15b18b55823bc3f2384545bc3`），system `2c6c012d9f2306f2ac13d240510eb8086b74d2b60ff318aa9e359dd72c05a3a8`、QR `4c887fbb4a16e0d2219969043e708c2d49c446f0ac75ba1dc3e6e17f7d2ee314`。

父原件来自run43672150224/artifact14145200674，10267458B，SHA256 `78b8ae3da20890c5726f7f53228ffeeb8a7fae41eb2c12477139089860aea2b6`；选中state `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6` 是实际73失败BASE，只作初猜，不是已接受尾锚。参数保持η=1、原32迭代/每步10档、solve tolerance2e-9、exact_workers2、max_factor_bytes2147483648、Node heap6144MiB、原最终J和audit。

主要输出均在 `native-word-first-current576/`：

| 原件 | SHA256 |
|---|---|
| result.json | `b6b247fa9e447777d80dfc2e6fc00da640cdbfd041e631fce27a38f6aa860655` |
| current-correction-summary.json | `456c27ae24f4d5cc45744988aa011a4e82c3f1aa6d318c992e6a7488c79154d0` |
| native_trials.jsonl | `7722a22d7cb9f9a8ee7da03eccbfaaba6dd84af99c635e2ffe9c2eeaab06b130` |
| native_iteration.json.gz | `c9dcafcd8e3f567b24efc672706a46c61c0a9b200728259e019196637508558b` |
| native_0001.json.gz | `576ac4c323fa290e640fb35458557821fb7fa8dccfa709cc4bdd5cd5ecf90a76` |
| iteration-000/word-candidate/result.json.gz | `81bfb12fc11fe00accf46b25df868b9de9fbbab4ce4933954e71306d51da73b9` |

## 首个原线搜索已失败

实际一次fresh with-J、一个单词方向，未调用后续R273完整QR。基点native norm为 `6.0618737006888706e-5`（小端binary64 `71f299f11bc80f3f`）。

| 原步长 | 原noJ norm | 原判定 |
|---|---:|---|
| 1 | 6.848278937534994e-5 | residual-not-decreasing |
| 1/2至1/512，共9档 | 每档6.0618737006888706e-5 | 每档residual-not-decreasing |

全部试探无原domain guard失败，bridge_failure=null；失败发生iteration0线搜索，耗时1863.593109387s，不是32步或时间预算耗尽。零接受、零后续QR，未到最终J/audit。native_accepted、success、task_completed、accepted_prefix、complete_tail_matching均false。不能据此启动要求成功95锚的completed95-live/fullDN适配器。

## 完整affine模型与实际noJ不一致的范围

唯一改变为node11/Q76，节点内零基列75：

| 项 | 原保存值 |
|---|---|
| 基点 | 7.191817341159996e-16；词 `6e1cafdb47e9c93c` |
| 候选 | 7.191817341159995e-16；词 `6d1cafdb47e9c93c` |
| δ | -9.860761315262648e-32；词 `00000000000080b9` |

这是向下相邻一个binary64字，其余方向坐标均零。完整129248方向数组SHA256为 `41d325e923391b3ca8ea34c01cec7961ab4f7c513621c86b8776a917c654d7ac`；单位步候选状态SHA256为 `00368a89bb3fda1c2fd6809ca445c1d49bf6ab6c7b4c3b640608b497fd47d892`。

原完整129248行affine判定在旧模型与fresh模型均通过：保存的最大值从 `6.061873700688870870601158412977629481529154353251182450024889837E-5` 降到 `5.957692987631636558516860867067351391887572070871999272359332686E-5`。预测最大行仍为2539，即stage10/row187/P76。线性改变225行：stage10完整224输出和stage11一个负identity行；cut/far及其他行均保留。

fresh J原描述器SHA256为 `1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4`，与旧J身份相同；新旧八项数学输入的原比较均true。这是原报告/描述器读数，不冒本次独立大J载荷审计。

实际单位步noJ norm反而升高，故完整affine预测下降不能保证该相邻词被原线搜索接受。47小件未保存单位步完整flow、残差及argmax；不能断言实际最大仍是2539，更不能唯一归因于某种root舍入、J错误、非线性曲率或缓存。

## 特定单词方向的回溯舍入

原表达式为 `lambda=2**(-k)`，随后逐分量 `v+lambda*delta`。唯一非零δ恰为负一ULP；基点词最低有效位偶，向下相邻词为奇。

在原binary64及round-to-nearest ties-to-even下，k=0得到邻词；k=1的精确实数结果是两字中点，舍入取偶基点；k>=2更靠近基点，同样回基点。这里δ乘二的负整数次幂在所用九档仍为正常数，不需下溢假设。其余分量δ为零，因此更小档不会形成新的非零单词位移。

这是对原表达式与保存字的推论，与九档norm逐字相同吻合；没有九份另存trial-state文件，不把推论写成独立文件审计。增加同方向回溯不能产生更小可表示改动；它不证明其他邻词无用或全问题已到精度极限。

## 下一原Newton内的有限proposal

后继从原失败BASE作初猜、保首fresh-J，有限考察node11/Q76上下两邻词：向下为失败对照，向上为新候选。通过原closure的 `cellFlow(10,candidateNode11,false)` 取实际noJ输出；该原函数负责226状态的两mean、cusp/rk4和P/portRatio变换。一次完整noJ基点评价提供不变的其他输出；候选须按原减法、scale除法、Math.max顺序重成完整129248行，受影响项不可用旧残差加δ代替。

只有真实完整noJ读数严格改善时才返回该邻词proposal，仍由完全原样的10档全noJ回溯决定接受。两邻词均无改善时，首correction应立即转同fresh-J的完整R273 QR，避免再返回已知失败词使iteration0终止。后续32步、原域检查、2e-9容差与最终J/audit保持；额外有界proposal调用须明示。这是尚未执行的新算法方案，不预言邻词下降或收敛。

按根README第15条，本稿不复制可重算原输出至repo/Release，不新建大审计归档；保留脚本、参数、实际run与输出SHA并继续科学推进。
