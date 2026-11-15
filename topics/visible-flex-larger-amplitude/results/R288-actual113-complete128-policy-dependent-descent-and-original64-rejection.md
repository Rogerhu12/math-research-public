# R288：actual113 完整128残差的策略相关下降，以及原64十档回溯仍拒绝

**可信度：启发式／数值证据。** 本文是本仓库公开 Actions 的原执行读回；不是新128精确Jacobian、严格误差界、native成功锚或非零完整场证明。

作者：ChatGPT（amplitude 子任务；主控读取并发布）。日期：2026-11-15。

## 1. 已经付出的完整实验与真正停止位置

[run 43688981685](https://github.com/Rogerhu12/math-research-public/actions/runs/43688981685) 的 source 为 `8d68a39e79eb1f0c976868d69f87d27fa3f2acbb`，job为 `132735373768`。步骤1–13成功，步骤14最终exit2，步骤15请求自有临时树清理成功。

这次不是准备阶段失败。实际完成了原当前场的一次 fresh J、一次完整R273方向、额外一次原64完整 noJ 基点控制，以及两种128 root-stop策略各自的完整基点和 alpha=1 评价。四次128评价都覆盖原全部129248行、576个stage，没有数学域失效。之后原stop策略的 alpha=1/2 评价因独立7200秒实验预算仅完成189个stage／42560行，未形成完整范数；更小步及 refined 半步没有完成。实验可执行程序正常exit0，并把原方向原样交回。

接着原64十档 noJ 回溯确实完整执行，全部拒绝。真正导致job的科学失败是原iteration0的

```text
Error: multiple-shooting line search failed at 0.000060618737006888706
```

`entry_error=null`、`bridge_failure=null`、worker进程exit0；没有达到最终native J、敏感度或审计。独立128预算耗尽是部分实验范围，不应伪写成数值发散或合法域不存在；原64线搜索失败也不能抹去此前已经完成的四次128全残差。

## 2. 同一真实当前方向、全部原方程与输入范围

本轮从真实 failed73 原场作为初猜，未把它或 failed95 认作已接受锚。实际 `same_complete_H=true`，使用原 `eta=1`、最多32次native迭代、原十档回溯、原 `2e-9` 容差。实际只达到iteration0。

原 fresh 场的64范数为 `6.0618737006888706e-5`。额外原 noJ 基点控制覆盖全部129248行，范数相同；其完整 stage-residual SHA与fresh记录相同为 `04ec3639e1a3ec4965ff4d7532bbe606e54aed895dd0523dc743702b0bd9e1f7`，far-residual SHA同为 `30939371bf346ff34a7534d70f1c42ff3b1dd35f708ba6a046b34dd30fef7f28`。这比单个最大值相等更具体，但仍不宣称原withJ与noJ所有中间浮点坐标或网格运算逐字相同。

实际新R273方向SHA为 `4bb396b069f5c32a3d77a08531ad2cdefbd3ece7fd8f63c56baed84f13976ce6`。原完整有限线性模型的精确dyadic回读最大缩放残差保存为

```text
9.685623139820915231844260456306540893890861679791289092058094119E-11
```

其最坏行是原global row2128，stage node9、Q mode1。这个数是原64有限矩阵加该方向的线性残差，不是128实际非线性残差。实际因子含129248行／列、258496增广行、576stage、577node、224宽度、577个罚块、1153次QR、1152次formation；因子及pure-constant临时字节数464891392，原factor报告耗时 `16.816937855000106` 秒。该factor所报 `float128` 实际significand为64位的longdouble；下面C++ primal才是113位有效尾数的IEEE binary128，二者不能只看类型名混为同一种精度。

128 packet从实际 noJ cell profiles 与 cusp splitter 导出，实际调度是 **6943个RK子步、20829次几何样本调用**，576个cell，而不是直接假设576×12。packet保留完整226态RHS／RK，包含224个形状态与两个原均值累积态；保持cut、全部stage及far行、原sigma归一化、端口ratio和完整112模式。角积分N=2048。

节点更新、root、RHS、RK、残差及范数在128中保持，不在更新后先折回64。几何 `w,w2,E`、角表／Gram、原far graph、scale及输入场仍分别提升自原64字面样本。该实验没有重新校准几何，也不把有限表的关系冒成精确连续ODE恒等式；原64J仅产生待检方向，不声称是新128 primal的精确导数。

## 3. 两个root-stop配置的四次完整读数

原stop配置使用原binary64常量提升后的 `8e-14`／fallback `5e-12`；refined配置明确改为binary128十进制 `1e-28`／fallback `5e-27`。两者是两个显式有限算法配置，后者不是前者同一原件的重命名。两份base先完成，再交错试同一alpha。

| 配置 | alpha | 原完整缩放范数（十进制字符串） | 同配置基点严格下降 | 达原2e-9 | 最坏原行 | 评价秒数 |
|---|---:|---|---|---|---:|---:|
| 原stop128 | 0 | 0.000122096054597410989492629881621789239 | 不适用 | false | 2791 | 873.703969032 |
| refined128 | 0 | 0.0278314932684405436812367265128199486 | 不适用 | false | 2782 | 2527.929873912 |
| 原stop128 | 1 | 0.000117187079879422633820220437067618538 | true | false | 2791 | 871.155691707 |
| refined128 | 1 | 0.027833507993481042641289769785034577 | false | false | 2782 | 2590.889588236 |

这些是原执行打印值，没有本地重做范数或相减。精确保存的128范数hex依次为：

```text
0x1.000dd1f7889da0c80213a1f62c65p-13
0x1.c7fdbe58c1453388429f47bd5204p-6
0x1.eb84ab3cf66ad3a5b0daad504e0bp-14
0x1.c80631a4283bc823a28a80e7d588p-6
```

范数沿原scale逐行计算。原stop基点的最坏未缩放残差是 `-6.32022287232257274964381733314263019e-19`；其全步为 `-6.06611298814502824458731353366609226e-19`。refined基点最坏未缩放残差是 `1.44067915139511457004338543307734789e-16`；其全步为 `1.4407834423267453170972985399943381e-16`。不能仅因这些未缩放数很小就宣布通过原缩放 `2e-9` 门。

每个完整评价均实际调用root27772次，最大成功Newton更新数为1，fallback返回数0；全部返回root通过所用策略的停止条件。两份原stop评价各904次Newton／回溯更新、29580次角评价；两份refined评价各27760次Newton／回溯更新、83292次角评价。

| 配置及评价 | 原保存的最大返回相对root残差 |
|---|---|
| 原stop基点 | 7.97942273584970872285222203689169507e-14 |
| 原stop全步 | 7.97942273584970749750995158741279345e-14 |
| refined基点 | 9.83114919311045868101932595752943758e-29 |
| refined全步 | 9.8311491931104540123382787819312751e-29 |

四次完整评价的 `failed_stage_count=0`。例如refined基点在全部合法root评价中记录的最小D、S、A分别为 `0.9999999999999857826630627151396472`、`0.999999999999999999999999999688946329`、`0.999999999975949816097646413730855503`。因此当前这四项差异不是由未记录的D/S/A拒绝造成。

这项同输入对照说明：在当前有限场及同一个旧方向上，改成完整128算术、以及进一步收紧有限root停止策略，会改变实际映射和步长效果。原stop128全步确实下降；refined128全步没有下降，且两者的基点范数不同。不能把“更严root残差”直接等同于“当前外部shooting残差更小”，也不能把同一个64方向视为两种新映射的Newton方向。

## 4. 半步只完成部分行；未完成值没有被补成成功

接下来原stop128的 alpha=0.5 记录：

- `rows_completed=42560`，`stages_completed=189`，`complete=false`；
- `experiment_budget_exhausted=true`，`norm_decimal=null`，下降判断为null；
- 本次评价耗时 `336.237611813` 秒；
- stage189–575共387个stage未完成，原错误文本为 `explicit-experiment-time-budget`；
- root calls9164、原stop已达9163次、Newton更新903次、fallback0。

原预算7200秒覆盖两份base及后续交错评价。最终 `evaluations_reported=5`、`all22_requested_evaluations_reported=false`；refined半步以及两种配置更小alpha没有得到完整评价。部分输出仍分配了2067968B，未完成行保持未完成状态；完整字节长度和SHA不能当成完整有效残差。

独立实验return保存 `status=0,signal=null,error=null`，`original_delta_returned_unchanged=true`。随后继续原64控制的责任确已履行，没有被128部分预算截断。

## 5. 原64十档回程及最终失败

原基点范数固定为 `6.0618737006888706e-5`。原十档完整noJ读数为：

| alpha | 原trialNorm | 原决定 |
|---:|---:|---|
| 1 | 0.00019266928302730032 | residual-not-decreasing |
| 1/2 | 0.00013090599247904327 | residual-not-decreasing |
| 1/4 | 0.00012144901300393549 | residual-not-decreasing |
| 1/8 | 0.00011814265821233656 | residual-not-decreasing |
| 1/16 | 0.00006569760416151993 | residual-not-decreasing |
| 1/32 | 0.00010632854139856965 | residual-not-decreasing |
| 1/64 | 0.00006848278937534994 | residual-not-decreasing |
| 1/128 | 0.000060618737006888706 | residual-not-decreasing |
| 1/256 | 0.000060618737006888706 | residual-not-decreasing |
| 1/512 | 0.000060618737006888706 | residual-not-decreasing |

最后三档保存范数与基点相同，未按相同范数放宽接受。原调用仍只返回失败：`native_accepted=false,success=false,accepted_prefix=false,task_completed=false`，`fresh_withJ_snapshots=1,current_R273_directions_returned=1,word_directions_returned=0`，`requested_complete_J_returned=false`。lastIteration仍为0，原minA=`0.9999999999759498`、minD=`0.9999999999999858`，residual和chartCondition未提供成功值。原调用耗时 `8431.179564694` 秒，外层总耗时 `8434.380945676` 秒；这些是实际报告，未以最初32步上限冒成执行32步。

当前保存的旧线性模型仍可极小，但真实64评价全拒，原stop128只提供一次严格下降、refined128一次不下降。仅继续邻词猜测、把最后相减换精度后马上折回64、或放宽原容差，都没有由本轮产生新的依据。

## 6. 下一求解算法得到的具体依据和未付责任

本轮支持推进**保留128状态、完整primal与明确root-stop策略相匹配的方向形成**。这是实现下一真正求解所需的数学责任，不是另加一个先验科学审批门。

1. 可以把现有64J视作近似导数或预条件来源；必须用所选128映射的完整129248残差重新承担方向、真实回溯和原缩放容差。原stop128的alpha1下降是可用证据，不能由此声称它已通过native或后续所有步。
2. 若选择refined root策略，必须重新形成与其实际root轨迹相匹配的变分。相同旧方向在该策略下全步上升，直接说明不能把它无条件当成refined Newton方向。小alpha是否下降本轮未付。
3. [R283](R283-finite-root-trace-differentiation-with-literal-tables.md) 已区分真实有限root过程中的F与更新矩阵C、各自独立字面表、Cholesky／代回算术、停止和回溯分支。后续变分须传播实际迭代程序；不能用精确隐式根公式代替有限停止轨迹，也不能把固定分支理想实表达导数冒成包含舍入的离散映射的经典导数。
4. 真正接受后的完整cut、far、敏感度、新J和最终审计仍需同一状态／精度／模型承担。当前128原件没有这些成果。本轮也没有证明原64表本身达到128连续精度。

两种策略各完整评价的实际耗时已经给出后继预算依据。单纯把同一昂贵22项实验重复跑完并不能替代一致方向；可以在已明确策略及有限轨迹变分接口上直接开展后续有界求解，资源部分结果继续如实区分。

## 7. 源、配置与原输出SHA

本轮请求SHA为 `ce294b5eb4136dd083cf0ad17912fda85d23630192fcc223c8bf37dbc8456136`。28个源的实际字节pin均由Actions在科学前验证。关键源是：

| 源／执行对象 | 字节数或范围 | SHA-256 |
|---|---|---|
| geometry_20261115_native_primal128.cpp | 23890B | 1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d |
| geometry_20261115_native_primal128_bridge.mjs | 12045B | 3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8 |
| geometry_20261115_native_primal128_probe.py | 10291B | ba3564ca6ef5329326861a66a948292280e2ab9e311eb8912c11d4e24d7d8409 |
| 本次编译evaluator | 真实可执行字节 | 91efd6f2984be486609928cc1c0112bbe5fa268ae8e7ebe3f37dc57c040b0196 |
| 实际生成probe hook | 原十档控制保留 | 96421af9f622a375f6e887de101b0261a193449b9c69bb05884a1427285a3a37 |
| 实际生成driver | 原native外壳 | 7c2d8cc80010dc259cda9b545f3e2f1c4c4c579105a0de194a00a92c338661a8 |
| 原R273因子源 | 42340B | 9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33 |

首轮113在历史ready路径缺失处失败后，本轮只修输入恢复及请求自有清理，三份科学源未变。两个原ready从历史commit `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复至原client支持的环境槽：109004B／`563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6`，29774B／`c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d`。原校准／几何检查保留，未把恢复输入写回main或Release。

实际原始输入和新中间对象：

| 对象 | 字节数或范围 | SHA-256 |
|---|---|---|
| fresh snapshot结果 | 本次current576 | 0d37c866014aac5a6357d6a741ab27917c9b4269e93f1d87fbbd05b6b47a9b97 |
| 完整base states | 577×224原64词 | f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6 |
| 完整delta | 129248原64词 | 4bb396b069f5c32a3d77a08531ad2cdefbd3ece7fd8f63c56baed84f13976ce6 |
| 原scale | 全部原节点 | ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc |
| 原physical H | 完整112分量 | c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f |
| complete-input.bin | 10348368B | 1c9df6b2aa203d526eee11fe443ebcb474584c677b76ed3901b6a0f6c1f37aa8 |
| 真实子步schedule JSON | 576cell／6943子步 | 3594f1f5da9327c4396350aea82a9086e18d27be96e3db3096c4f6bb00128c1c |
| 128评价原报告 | 11759B | 925bfe91a339820a2464c5ff9c05f7a3fd8031b69e1634eb6777676f8d8f85b5 |

每份128临时残差数组为2067968B；四个完整对象及一个部分对象的原SHA为：

| 配置／alpha | 完整性 | SHA-256 |
|---|---|---|
| 原stop／0 | complete | 7a2f785786ee1e60b63270925c9b1f6a9425ca5755cf50c64732f8aded520cf1 |
| refined／0 | complete | f50e435564138b3860cba2668925a3d2ba83d48bc933d92af6a289bf7c406865 |
| 原stop／1 | complete | f8aaf3244e9317d3ea3bf3fe5be176f99c232399f71824a2af65759ace01a542 |
| refined／1 | complete | 2ba56a423fe793fe5b2975f70a52b10273e50bca6762a95b0992b4d7226552c0 |
| 原stop／1/2 | partial，42560行完成 | 9ace4c5c1dea36b89a8ddff3a311ac05ebd02ff6e448e8b90c63e3c633be62de |

原native结果SHA `dfdc5c16f003d87bb7e6fff78bf0d8610b33455b0eee7b1062f1956040410273`；原response 1332003B／`5f27d0b89e0a0a71b8dd0d1436dcaba17fdea8c1da549fee9234dcfe17905ae3`；最终摘要SHA `f1c7bf72d94260191dbbbed8f13f9299b2dac17ee83d97093c9d9eab9f517623`。本次完整job日志113563B，SHA `255c07242b1fd609aca0b5dd1034c3754e801e15f2b311f5df1257615ebcc970`。

规则监控在07:14:13、07:59:16、08:44:18、09:29:21 UTC完成真实同步，固定科学checkout未变。清理实际成功删除本请求实验输出、临时91输入与78源恢复树；对只读91临时归档只恢复自有21个目录的用户权限，不跟随symlink，不改变文件内容或科学结果。原始数组、checkpoint和factor未上传Git、Release或新artifact。本文只读取原日志和源代码，局部做JSON／字节检查，没有本地数学重算。
