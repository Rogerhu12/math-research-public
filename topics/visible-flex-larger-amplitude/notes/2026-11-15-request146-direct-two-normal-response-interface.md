# Request146：在原完整九方向搜索内直接形成两条物理法向响应

作者：ChatGPT / amplitude。分类：独立候选算法及可执行源码接口；本稿不报告第146轮的未来数值结果。

本次从真实第142轮末九参数和真实末半径开始，只把每个原法向模型中的两列响应改为沿固定物理列 $P_1,P_2$ 的原 complex-step 调用。第142轮的完整九轴 Jacobian、完整九方向外模型、实际所选方向响应、12×20 法向试探、R299 有限候选选择、20 档外回溯及全部原最终责任保留。新法向轨迹会变化，不能声称与第142轮同轨迹或由新形成方式自动获得更准导数。

本次只计划一个原8方向批次。未增加科学接受门，原阈值和域规则保留，也没有执行任何本地科学计算。源码、短配方和原输出身份可核对；公开 Actions 才会实际形成新响应和候选。

## 1. 实际依据与起点

[第142轮完整原读回 R316](../results/R316-actual142-complete-nine-directional-response-and-normal-precision.md) 记录8个外方向均有原 Armijo 接受，14次外候选调用中有4次法向模型最终20档全拒。部分后档的参数词和三项方程词与当前点完全重复，R299 选择也没有直接救回一次原工作返回的外 Armijo 失败。另一方面，保存的2×2 QR 读数没有证明该小解本身病态；第142轮也没有沿两条实际 $P$ 列的直接响应，因而不能先宣布旧 $J P$ 已被测出错误。

新实验沿用原 R310 已公布的完整两列接口，只替换最终法向响应的形成路径。它检验一个实际可用的求解变化，不增设独立的导数验证任务，不声称会修复内部传递/边界消去或 binary64 参数分辨率。

原始起点来自：

- run `43713410623`，source `08752b3d96a153f9ebedcad9faf8b4134d5e129e`；
- compute `132809696991` / report `132809901399`；
- 实际 producer `geometry_20261115_small_core_nine_control_directional_response_recipe.py`，SHA256 `5acf5b029a756a356a3de3d598211eaa89df4a7670fc703f2d3567488e09bae4`；
- 原 status：2006738 B，SHA256 `2b92a0af0ea7aa7cd67540e428674230ca91fdcecd3bcdcc6c709c009d88ee3c`；
- 原完整 primary：70189 B，SHA256 `50b63e5d58f266a0643e69958adff4361d969222c763f29d39b2d37520504d4e`；
- 原完整 scalar view：991133 B，SHA256 `431aed4912c0271eac77c4640aee71196bc8ba38c4443351415fbb0da59e6e72`。

九参数依原顺序 $[p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3]$：

```json
[0.3055213800232409,0.21645015247953373,0.3427004414286296,-0.06322332433837356,-0.017474514984195083,0.9376116108116533,1.075130597804341,0.6886901265899157,0.9385439808625842]
```

初始相对半径为实际 `final_relative_trust_radius = 1.9073486328125e-7`，完整保留该 binary64 值，没有重置、夹取或放大。配方只消费这些字面参数、半径和真实来源，不读取或伪造已经清理的旧 status，不复用父 J、merit、FD、域或圆结果。原状态和 primary 的 SHA 是来源声明；本轮重新作初始 evaluate、description 和全部后续读回。

此起点是第142轮末点，**不是第142轮初点的同点对照**。它也不是已接受的非零 native/112场。原真实父 source 闭包31项，新 producer 闭包33项；后续若本独立 schema 产生真实完整结果，原 own-schema 配方入口仍可显式消费，但本请求上限只有一个批次。

## 2. 唯一科学变化

沿用原有限模型 $f:\mathbb R^9\to\mathbb R^3$ 的真实求值、原约束 $c=(f_2,f_3)$、当前外方向 $d$ 和直接动作 $a$。每个外候选仍使用同一固定法向平面：

$$
q(\alpha,w)=p+\alpha d+P w,\qquad
c_{\rm target}=c(p)+\alpha a_{2:3},\qquad P=S N\in\mathbb R^{9\times2}.
$$

$P$ 仍由原外层 fresh nine-axis J 和原完整 QR 形成；本轮没有在法向迭代内重排或重新选择 $P$。目标值不清零，当前真实残差不覆盖。

在每个原来需要法向模型的迭代处，新 helper 依次完成：

1. 原 `model.jacobian(current['parameters'])`，保留完整3×9矩阵；保存旧 `derivative[1:, :] @ physical_normal`，供原位比较。
2. 调用冻结 R310 的 `normal_directional_response`，对同一点、同固定两列分别调用原模型：
   $f(q+i h P_1)$、$f(q+i h P_2)$，其中 $h=10^{-25}$ 是原已用步长。
3. 保留全部3×2响应 $B$，只把末两行 $D=B_{2:3,:}$ 送入原2×2完整行尺度 QR。
4. 原法向位移求解和模型斜率现在使用这个 $D$；原行尺度、当前误差、12次迭代/每次20档回溯、实数求值和接受式不变。

以真实目标误差 $e=c(q)-c_{\rm target}$、原固定正行尺度 $s$ 表示，内部模型仍是：

$$
D\,\Delta w=-e,\qquad
m=\tfrac12\|e/s\|^2,\qquad
\ell=(e/s)^T(D\Delta w/s).
$$

每个真实内部候选仍由原 `q = seed + physical_normal @ trial_w` 形成，只有原真实 scaled-constraint Armijo 可以改变工作状态。原正常返回、全部失败、目标未到、参数词未变等分支保持。原 $10^{-8}$ 只是法向停止目标，始终不是外层额外接受门。

这两条 complex probe 不进入实数候选全集，不成为可采用的状态。R299 继续只在新工作轨迹中已经完成的有限实数状态间比较原完整三项 merit；完整工作返回在相同保存 merit 时优先。工作调用未完成时不从 shadow 假造成功，法向模型正常失败后的真实工作返回也按原规则保留。

### 2.1 外层、半径与最终检查

第142轮外层完整九列 reformation、12×9 正则 QR、所选实际方向的原 complex 动作均原样。外层仍以原真实三项未加权 merit

$$
W(q)=\tfrac12 f(q)^T f(q)
$$

与原 $W(p)+0.2\alpha f(p)^Ta$ 比较。模型 action、真实实数残差、pilot $Jd$、完整基底 $Kw$ 和曲线原点 $q'$ 的读数继续区别记录，不能互换名称。

原 `next_radius` 字节未动。接受回溯后的 halve、满足原条件的 double、保持半径、整方向全拒后的 quarter 都保留；包括最后一方向全拒后的真实末半径。参数未获原外接受时不采用内部工作点。没有降低容差、改写损失、删掉第3残差或转为 p3 消元。

初末完整九列三档实 FD、原 Arb 域、固定实际六shape的453维圆检查、完整112右残差、原 low/full/native/final 字段全部走原主体。R299 选择和当前 normal 变化均不增加 `inner_target_tolerance_met` 为门。原最终失败、例外、未完成和预算停止保留原含义。

## 3. 源码最小差异与调用合同

新 normal helper 的入口为：

```python
curved_candidate(
    np, qr, solve_triangular, model, baseline, trace,
    parameters, state, direction, action, frame, alpha, args,
    record, label, *, response_helper
)
```

producer 在原独立 source 检查之后加载 helper 及原 R310 模块，并使用：

```python
curved_candidate = partial(selector.curved_candidate,
                           response_helper=response_helper)
```

从原外层 `slope = float(residual@action)` 开始至所有外试探、接受、半径更新、末端检查、`except/finally` 的源码段逐字保留。原 `norm`、`next_radius`、2×2 `full_column_qr_solve`、R310 loader 也逐字保留。

helper 从正常模型完成后的原斜率判别开始，整个20档实回溯、工作更新、末返回及 R299 选择尾段逐字保留。仅模型形成处增两P probe、旧投影与新响应并列读数；helper身份和元数据明确是新独立算法。未执行旧142 producer main或旧 helper；旧源码仍逐字保留并进入来源闭包。

读回含新 `direct_normal_response_probe_readback`：

- 当前真实参数和方程；
- 原3×9 J、固定9×2物理 $P$、原2×2投影；
- 两条实际 probe 的全部 real/imag 参数、返回 real/imag 三方程、真实异常；
- 完整3×2响应、用于求解的2×2响应、实际形成的新旧投影差；
- 原完整2×2 QR/回代读数、真实法向更新和原三项 merit。

`original_evaluation_attempts/returns` 继续只计原实候选，不把新增 complex 混入旧计数。新 `normal_complex_evaluation_attempts/returns/exceptions` 单列，全部数学调用还进入原 EvaluationTrace。每次probe在调用前登记；发生原数学异常则保留失败详情，既不转回旧投影冒正常使用，也不丢弃已发生的部分调用。原可处理数学异常进入原正常失败路径，未预期异常按原 producer 责任传播和保存。

`original_full3_merit_slope_of_normal_correction` 保留旧轴J的读回并显式标注来源；另存新完整3×2的 formed full3 斜率。内部接受只用原 scaled-target merit 及其当前新矩阵斜率。旧字段不重标为新的真实导数。

## 4. 精度边界

[R310](../results/R310-complete-nine-directional-response-basis-and-finite-error.md) 的线性换基/方向响应条件与误差范围仍适用。沿 $P_j$ 求响应可以避免**最后一步**由9个保存轴列形成该响应的相减路径；它不删掉 `model.evaluate` 内部传递矩阵、边界减法、复数运算或 branch 的有限误差。

第142轮真实 complex probe 的实部方程已与同点原 real evaluate 不逐字相同。本轮完整保留这一可读事实，不把直接 complex 动作自动称为 rounded real 程序的精确导数。微小更新是否形成新的参数词仍由原更新程序决定；直接响应不保证越过这种分辨率，也不能用相近的列FD误差认证微小奇向量。新旧投影差只是一项实际读数，没有同意阈值、rank cutoff 或替代科学门。

原始P和目标仍由外模型确定。曲线实际 $q'$ 等于 predictor $d$ 还需要相应的真实响应等式，当前数据未提供这种证书。本次初始位置也已前进到142末点，不能把后续差别全归因于法向形成方法。

因此本次应直接读取：新旧正常矩阵差和两probe来源、20档全拒是否仍有相同词、真实normal与外merit是否改善、完整选择轨迹和全部末端状态。若仍只极小下降且probe/实值或词分辨率问题保留，应据新原读数决定更一致的高精度方程/导数形成；本请求没有预设再次堆32批，也没有先承诺该下一算法有效。

## 5. 明确预算与单批语义

| 项目 | 本次值/责任 |
|---|---|
| 科学 child | 最多1个，每个原8方向 |
| 外回溯 | 每方向20档，原 $2^{-j}$ 顺序 |
| normal | 每外候选12次，每次20档 |
| normal 目标 | 原绝对 $10^{-8}$，不是外门 |
| 原 full3 candidate 阈值 | $10^{-8}$，不替原 BVP 接受 |
| 初半径 | 实际142末值 `1.9073486328125e-7` |
| 原外层新增complex上界 | 8×(9基底+1实际方向)=80 |
| 本次normal新增complex上界 | 8×20×12×2=3840 |
| 原fresh normal9J上界 | 1920次，原J自身complex调用不计入新增2P计数 |
| 原seed/normal实候选上界 | 38560，未删减 |
| 其它原工作 | 初末FD/description/域/圆/112等另按原程序 |
| wrapper资源预算 | 3600秒，只在完整批之间检查；不截一批的原科学预算 |
| Actions science / compute job | 原75 / 90分钟 |
| report job | 原10分钟 |

probe失败可能只完成第一列；实际调用数和未返回记录照实保存，不以预算上界代替实际。资源中断、规则变化、未完成readout、零接受、非budget数学停止各按原 wrapper 记录。原 `original_stop`、`science_argv` 与 `genuine_next_recipe` 源码逐字保留。单批上限不强迫其完成8方向，也不会把零接受改成成功继续。

## 6. 原输入、完整source与唯一请求

四数学输入仍是第142轮的原字节：

| 输入 | bytes | SHA256 |
|---|---:|---|
| accepted | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail_anchor | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail_config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

按原 workflow 从历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 精确取回到本请求 RUNNER_TEMP 并核原size/SHA，原78源恢复也保留。不向当前main、Release或新artifact保存这些可重算数据。

原93个运行/来源pins和5个support pins全部不变。新增 helper、producer、wrapper后为96项，新增reader后support为6项。31→33科学闭包仅新增新helper及新producer；R3105004、旧R299d4c9、旧1425acf均保留原身份。旧142 wrapper/reader只作历史来源，不执行。

新 producer `R259-nine-control-full-three-direct-normal-response-carried-radius-trust-recipe-v1`；status `nine-control-direct-normal-response-carried-radius-status.json`。
完整reader `nine-control-direct-normal-response-full3-curved-trust-segmented-scalar-readback-no-raw-retention-v1`。
wrapper `same-nine-control-direct-normal-response-eight-direction-single-temporary-batch-v1`。
request `public-nine-control-direct-normal-response-single-temporary-batch-request-v1`。

文件安装位置：

- 四Python源、配方和请求：`topics/visible-flex-larger-amplitude/computations/`；
- workflow：`.github/workflows/visible-larger-public-nine-control-direct-normal-response.yml`；
- 本接口：`topics/visible-flex-larger-amplitude/notes/2026-11-15-request146-direct-two-normal-response-interface.md`。

唯一push trigger只匹配 `computations/public-nine-control-direct-normal-response-request.json` 的完整topic路径，不修改旧142请求或workflow。保留原 Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0及单线程环境。原metadata runner每2700秒真实pull/read双README、遇新规则停科学；科学checkout固定。当前已读root/topic blob分别为 `21bd547f56590b7f2dd279d0297efb289a9b2783` / `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。规则更新必须按实际新内容处理，不能绕过原runner。

workflow保原H唯一规则记录行及原大小约束、git no-GC/merge.stat=false、原token隔离和进程组停止责任。新wrapper实际CLI为：

```text
python -u <computations>/geometry_20261115_nine_control_direct_normal_response_temporary_batch.py
  --request <computations>/public-nine-control-direct-normal-response-request.json
  --request-sha256 <该请求实际完整SHA256>
  --repository-directory <本次固定checkout>
  --original-input-paths <RUNNER_TEMP中原四输入路径JSON>
  --rules-directory <本请求rule-sync>
  --out <RUNNER_TEMP>/nine-control-direct-normal-response-temporary-batch
```

wrapper再调用新producer的原四输入、显式recipe及其SHA、实际半径、`--candidate-steps 8 --backtracks 20 --normal-iterations 12 --normal-backtracks 20 --normal-target-tolerance 1e-8 --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14`。没有重跑第142轮轨迹、读取失联raw、native bridge或隐藏第二child。

## 7. 完整输出和临时生命周期

每一outer方向的完整normal scalar record仍直接进入 `complete_normal_traces`。新reader没有增加count-only替换、首末样本截取、inner-trial上限或删列。每组完整原JSON的canonical bytes/SHA与各结构段完整保留；大对象只按原声明JSON路径/范围切分日志，单段≤90000 B。新的段schema为 `nine-control-direct-normal-response-complete-direction-scalar-segment-v1`，stdout标签前缀 `VISIBLE_NINE_DIRECT_NORMAL_RESPONSE_`。

每批reader stdout在原 `VISIBLE_NINE_BATCH_001_ORIGINAL_READER_STDOUT` 外框原样转发；primary另在 `VISIBLE_NINE_BATCH_001_PRIMARY` 输出。primary过大时按原协议把完整具名字段搬入日志组，仍保整组hash/索引。report job只接一行批次链和结果索引，不合并所有原组。所有未开始/未完成字段、原失败文本和异常保留；链或最小索引超90000 B时诚实返回transport未完，不截字段冒complete。

先由reader完整消费status、trace和所有原文件身份，再产生真实restart recipe和链读回，最后只删除本请求owned、无逃逸symlink的临时payload。workflow always-chain步骤先于最终owned cleanup。原小数据不上传artifact或Release，不写回Git；源、参数、原run、结论和输出SHA由主控依实际结果登记。不存在预填的146 run/source或接受结论。

## 8. 冻结文件与完整差异

| role | 文件 | bytes | SHA256 |
|---|---|---:|---|
| helper | `geometry_20261115_nine_control_direct_normal_full_merit_candidate.py` | 24043 | `485e5fd8b71bce6365084cca518a2b42e2e58d302933bd868c38995b59ad6a55` |
| producer | `geometry_20261115_small_core_nine_control_direct_normal_response_recipe.py` | 51746 | `c717bafb95854bef7b60048a8194b9949a30fbff29bc5e1eee8a0dbb25cf233b` |
| reader | `root_20261115_small_core_nine_control_direct_normal_response_scalar_readout.py` | 33912 | `60b9fa8ba6b071f367ea89efb23add861a473957d26dce8476feda7841f9e95c` |
| wrapper | `geometry_20261115_nine_control_direct_normal_response_temporary_batch.py` | 59280 | `0824c5830d310eaf11d68567c535fa5d9b0c5f093466e3dc79bfabc1b82464a0` |
| recipe | `actual142-final-nine-control-direct-normal-response-recipe.json` | 2455 | `63e9ccc0e45c3b3e5a3c5f4a5cad1aa3ed6ddc682e3c98ca2155a80eb4665ebe` |
| request | `public-nine-control-direct-normal-response-request.json` | 58056 | `80f2fa09dd1e4a853d652d86754fe74394c1f5344c57325a127d38ff0f2d3ae0` |
| workflow | `visible-larger-public-nine-control-direct-normal-response.yml` | 23724 | `8e01c9d238d77df3b263be66d4e10ef2eb9ae326a5796acbbf1f6717d4736bb9` |

四源及三接线均只创建无ref的公开Git blob作文本保全，由主控统一发布；这里没有更新branch、commit、PR或触发Actions。旧来源无修改。

以下差异是每个新文件相对真实基线的**完整文本差异**：helper对R29919265B/d4c9，其他对第142轮冻结文件。既有93+5pins及全部4inputs的相等检查只比较原字符串/JSON身份。

| 差异 | bytes | SHA256 | 未引用Git blob |
|---|---:|---|---|
| helper | 9322 | `aa726b9093e73536e8dc795e3309b6003e0225a859a90ae46e88e8ec31e0fe39` | `f296d8f5f91b6b915a8498fc410548a54ab5ad9f` |
| producer | 14850 | `85e2cf1d1df2d04ce82d4389d47e70f9b842f45ee57df54fff569e058d25d661` | `dc8dc85901895022a013baf0b739531331dd9365` |
| reader | 9983 | `796b0a2e2712c1a8fa4ffb5e49547d603a2a6dfede202b042e08dfea98bb4765` | `dad57f9f62b49474cf95a126e97bf061cb4b9080` |
| wrapper | 14212 | `a7e786401b07062eae6842ed7f57e3127469db146de4cfb28114d8bf5e830f4d` | `26f977d2ed1f1202e25bd65ee161d2c70ac0332f` |
| recipe | 2421 | `c41dbfc51ea5e1997f219ce2689a38e07e750ef8015ecd668a18f3074dd5f056` | `b9970f2e17fda67eb58ef2c0dd745d55aa5a3bfe` |
| request | 46528 | `863ba5fb88c7cfdec6b6dca4ecf64817e500004cce3ad0a985650eaa3164ddfb` | `3de900b5e24016c29c67e37db3e663f7223dc2f5` |
| workflow | 26910 | `ce022f291a2b8af7ffb78cd0a2352ef64a17844508d0d9db5a4f0a54938ef203` | `ca875613024f601a066ccce290400b0fab897d6c` |

源码检查仅包含原文本读取、逐项替换的逆恢复、原数值块字节比较、完整差异、JSON字段及来源闭包/哈希。终端失联期间未声称本地Python AST、Bash或数值测试已运行；已保留原Actions setup对全部源的AST/compile步骤。没有生成科学fixture，也没有以独立审计作为新科学门。
