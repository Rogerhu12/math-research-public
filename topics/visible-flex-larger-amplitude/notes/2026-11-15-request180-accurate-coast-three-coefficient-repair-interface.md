# Request180：同一准确 R323 九族的 coast 三系数实际修域

作者：ChatGPT（/root/amplitude），2026-11-15。全部科学求值只在本公开仓库 GitHub Actions。
这是一个独立实际参数选择计算，源与配方可复算；没有执行本地科学、导入数学模块或新增 fixture。
本接口不填写未来 run、选中 β 或成功。实际结论编号预留 R384。

## 1. 直接推进的对象与已有证据

实际165的严格速度反证由 [R381](../results/R381-actual176r2-complete-strict-refutation-locations-and-readback-recovery.md)
定位到原 numeric piece416；其准确目标身份与169/179初点的对应见
[R383](../results/R383-accurate-R323-target-identity-and-coast-control-necessary-band.md)。
原419片的最后四片是 first-velocity-transition、negative-speed-coast、
last-velocity-transition、canonical-cubic-cut-collar；准确 coast 是 index416。

本次不重算原C、不重跑差额网格，也不把旧有限Gauss族的参数/J当作准确连续族。
从实际165原定义来源恢复同一 R323 准确九族，显式调整 coast 的三个真实自由系数
$p_3,\theta_3,\eta_3$。其余六系数、core、原cut、两个过渡窗口、collar宽度、
$\kappa$、自然长度定义及全许可C根族均不变。support1 的新 $\xi$ 不在本实验中，
没有把它当成 coast 修复方向。

实际165初九数值来自实际146；原浮点词在准确模型中按 `Fraction.from_float` 精确提升，
不是把显示十进制字符串另解释成新的有理数。原顺序是
$[p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3]$，原词为：

```json
[0.3055213835477326,0.21645013203050154,0.34270051957744246,-0.06322334619266512,-0.01747451701873286,0.9376115689625685,1.0751306255033548,0.6886900390922872,0.9385431607625546]
```

以上只是实际输入，初点不宣称域合法。新结果也不借用178/实际157的十族状态或被删除的raw。

## 2. 原165恢复与来源责任

官方实际源 tuple：

| 项 | 固定实际值 |
|---|---|
| run | 43736208020 |
| source commit | 1f2ec637430e5c6b27b1a93720e106539281a156 |
| compute job | 132879253906 |
| 原完整log bytes | 1486048285 |
| 原完整log SHA256 | `4ab8c6d688a27869353bb428288d467502c7aed6ad8cd96140a6cfaea508aea2` |

恢复器用官方 `GET /repos/Rogerhu12/math-research-public/actions/runs/...`、
`actions/jobs/...` 和 `actions/jobs/.../logs`。
先核 completed/source/job-run tuple，原compute是否success不作前提：
原165有严格反证，不能因此拒绝读取真实原记录。日志只流式读一次，不写1.486 GB临时副本。

官方API只从环境继承token；日志API返回的HTTPS重定向另发无token请求，
不记录带签名URL。每物理行仅在解析视图去一个行首BOM与一个锚定GitHub时间戳；
完整原流SHA仍包括所有这些原bytes。全部所选原分段按原index重建，并核原group/成员完整bytes/SHA，
不是从哈希“恢复”正文。只保存下列3个完整必要原成员到当次RUNNER_TEMP：

| 原成员 | bytes（含原LF） | SHA256 |
|---|---:|---|
| original-input-binding.json | 62398 | `996593f3a615c3694596463c949990a4967cc5c5a1bf48b100fbc4e149e73e48` |
| original-target-result.json | 105512 | `e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619` |
| original-construction-summary.json | 27207 | `6ff7fb33455be8dbc4eef1eb819a8f7b90329c8575c442dc810c83db13117fb8` |

其中input保存原cut完整E/E_r/E_rr球、原C实际binding、全部定义字段SHA；
construction的 `actual_recipe` 保存原完整recipe。definition正文没有假定存在于旧小摘要中。

另从公开历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 精准取两个原输入：
完整accepted M96 core 2614352 B / `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`，
T112-config 2161 B / `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。
不恢复旧tail状态，不把原core叫作新目标的已接受场。

科学源实际调用原 `0d89370d…` factory 与 `a9a25d96…` 精确core constructor，
从完整core geometry、原recipe及cut语义叶重新 `build_expression`。
以原256-bit sqrt外包形成原 construction_conditions，并按原input中每个字段canonical SHA、
完整definition bytes/SHA核回实际来源。此项是来源绑定，不是新增数学接受门。

原21源全部字节仍核同，另加恢复/科学2源共23。
原165/151/147科学入口、numeric shadow、fullDN和C solver均不在本次执行；
3b8规则runner只是metadata。没有为“重建绑定”偷偷再付旧C或旧大差额网格。

## 3. 实际参数算法

候选的共同缩放是准确有理运算：

$$
(p_3,\theta_3,\eta_3)_\beta
=\beta(p_3,\theta_3,\eta_3),\qquad
\beta\in\{1,2^{-1},\ldots,2^{-16},0\}.
$$

这18档顺序明确，先大后小；0是显式原coast基底候选，不是隐藏重置。
每档都保原输入参数、三条准确新系数、实际证明/反证/未决/资源结果。
只选声明顺序中第一个完整419片域均已证明的候选，不宣称连续最大β或全局最优。
若有限计划全失败、未决或预算未付，就记录真实范围与全部未访后缀，不宣称不可行。

令 $t=(s-S_1)/L_C$，$P(t)=p_3B_0(t)+\theta_3B_1(t)+\eta_3B_2(t)$，
其中 $B_j=64t^3(1-t)^3(2t-1)^j$。
由于原真实校准使 $S_1,L_C,L$ 与九系数无关，本次在准确目标上使用：

$$
a_\beta(t)=R_A+I_A-\kappa L_Ct+\beta L_C^2P(t),\qquad
(a_\beta)_s=-\kappa+\beta L_CP'(t),\qquad
(a_\beta)_{ss}=\beta P''(t).
$$

这是原准确表达式的恒等形式；不把这些约简施加于另一个binary64数值程序。
区间系数由原完整语义叶外包得到，未用中点。根族中每一许可选择都被这些外包覆盖；
各叶间可能有相关性，使用乘积外包只会扩大范围，不把独立box当作新精确定义。

[ R386 ](../results/R386-accurate-coast-uniform-feasible-scaling-and-C2-bounds.md)
给出显式充分缩放界，但本实现直接沿全coast有理区间Bernstein计算，
不把中心必要带、该充分界或任何新阈值加作另一求解门。
中心速度 $-\kappa+2\beta L_C\theta_3$ 只作为必要诊断保存，不能代替全域。

## 4. 全部419片的准确域责任

先且只先计算一次其余418片；每个β复用这个真实不变部分的域结果。
零二阶jet保证缩放coast控制不会改变相邻片连接的半径、一阶或二阶导数。

- 原415个core片各沿其准确有理局部坐标；support0端点若落在一片内，按准确端点分开闭区间。
  相应完整三阶组控制合并后再与原半径多项式相加，支撑外原式保留。
- first-transition415含完整support1三控制，真实共同anchor/width显式核同。
- last-transition417与collar418保原完整表达式；coast控制在其连接端点为零二阶jet。
- coast416每档覆盖准确闭区间 $[0,1]$，三控制先准确合并，系数次数至多8；
  用同一半径的准确导数形成速度和加速度，不能拿互不一致的表替代。

对每个闭子区间，全系数Bernstein区间外包检查严格
$a_{\rm lower}>0$、$-1<(a_s)_{\rm lower}$ 及 $(a_s)_{\rm upper}<1$。
若 $a_{\rm upper}\le0$ 或速度包围完全在允许区间之外，明确记严格反证；
宽包围而未能判定时二分，深度/预算用尽记未决，不能当反证。
coast已出现一个足够严格反证可停止该候选，但把尚未访问的完整区间栈保留。

全部节点、终叶及准确Q端点只在当次临时ledger；小摘要返回完整片计数行、
所有实际反证/未决/未访记录和原ledger bytes/SHA。通过的巨量叶表只identity。
返回端点可用向外128bit dyadic summary网格并绑定原准确Q区间identity；
**证明谓词始终用原准确Q端点**，不用summary网格判定。

固定418若未付完整，则任何coast通过只叫 `coast-proved-fixed-part-unpaid`，
不会被选成完整目标。真实算术异常、严格反证、宽包围未决、资源停止各字段分开。

## 5. 实际输出与后继参数合同

顶层schema：
`request180-accurate-R323-coast-three-coefficient-repair-v1`。

`all418_unchanged_piece_domain.complete` 与实际候选的
`complete_coast_domain.complete` 均true，且 `new_profile` 实际生成成功后，
才设 `full_accurate_nine_domain_proved=true` 和非空 `selected_profile`。
该顶层字段始终bool。提前异常或部分覆盖保持false；没有未来selected数值占位。

selected保存：

| 字段 | 实际含义 |
|---|---|
| nine_parameters_exact | 完整九个准确有理词，非仅coast三项 |
| beta_exact | 本次实际选中共同缩放 |
| recipe / accurate_definition | 两个实际新文件的basename、bytes、SHA |
| factory_source_sha256 / new_selection_source_sha256 | 原定义函数与当前选择器身份 |
| continuous_model_schema | 原准确R323 family schema |
| semantic_C_remains_original_all_root_family | 原全部许可C根族责任 |
| full_length_expression_unchanged | 长度表达式没有以新参数重定义 |
| binary64_projection | 每项准确词、真实double词及是否逐词精确可表 |

输出文件为
`selected-accurate-nine-recipe.json` 和 `selected-accurate-nine-definition.json`。
后者由原factory的真实 `definition` 调用生成。
本次没有调用原factory.main，也**不制造**它的 `result.json` schema；
本次独立 `result.json` 是180自己的科学报告。

`binary64_projection.parameters[i].exact_projection_difference` 的符号严格是
$Q(\operatorname{binary64}(p_i))-p_i$；`binary64_word` 为小端double的16个hex字符。
`all_nine_exactly_representable` 只有实际九项全部准确相等时true。
即使全true，也没有支付numeric shadow/J、IEEE舍入域、BVP或metric误差；
后继必须真实形成自己的数值对象与原门。

不同C包围宽度/run/result SHA并不自动改变原准确函数：
同C根族、core、cut、窗口、$\kappa$及九个准确参数的语义同一性依R383。
本次保留原165包围与provenance作为实际证明来源，不伪装成未来新C的原文件。
后继薄适配可据这份准确函数身份与全部419片证明交接；
不得要求无关provenance字节相等而加域重算门，也不得省掉新数值shadow/J/实际活动参数点责任。

## 6. 资源、真实规则与失败读回

| 阶段 | 明确资源 |
|---|---|
| 官方旧log流式恢复 | 600 s，完整1486048285 B；workflow15 min |
| 新科学总clock | 900 s，从源/定义重建开始 |
| 其余418片 | 最多300 s、65536节点 |
| 每个coast候选 | 最多8192节点；共用科学剩余clock |
| 二分深度 | 28 |
| sqrt外包 | 原256bits |
| science workflow step / job | 25 min / 55 min |
| always必要读回 / report | 8 min / 10 min |

clock在受控节点/阶段检查，不能保证单次大有理运算恰在截止瞬间中断。
workflow还有独立墙钟上限；外部取消或规则停止后只按实际留存progress返回partial，
不能将预算未付写成数学否定。600s网络预算与900s新科学预算分开。

原3b8规则runner不改。startup从固定checkout核真实已读README blobs及完整正文，
只将其BASELINES换成当前已读版；原2700s真实pull、唯一HANDOFF规则行、
普通rebase/push和规则变动停止原进程组均保留。
metadata父保token；新science child移除四个GitHub token键及GITHUB_OUTPUT，
不接网络、不碰Git。新科学结果由always metadata读回独立导出。

未安装numpy/flint/其它包；原factory/core所调用路径是标准库精确有理/区间表达式。
原21源身份范围不等于这21件全被执行。

恢复、rule runner与science的stdout/stderr直接继承到原compute日志；
startup/导入/源码错误不会先只hash再删。已有进度、result与summary都属同一run/source。
必要报告重新选择/JSON编码不执行新的界/科学量。一个报告硬上限90000 B；
超限返回显式错误与未读身份，不把大表编码/分片塞工具，不假称complete。
真实错误与异常可能使报告超限，未实际运行前不保证字节结果。

## 7. 清理与公布

只有必要摘要complete、实际rule child.wait返回收据存在，且摘要/原source-summary/
runner-result的实际bytes/SHA重新核同，才清本次owned临时树。
必要读回失败或owner状态未确认时明确skip，不主动删除该现场；
runner结束后的销毁不等于仍有可恢复raw。

无artifact/Release上传，无raw入Git；只公布源、请求、说明、实际run及必要原值/输出SHA。
history对象的Git临时缓存仍是Actions checkout自己的原仓对象，未新归档科学数据。
本地只作文本、原字段接线及字节工作，未执行科学，也未为本次增加额外本地测试。

## 8. CLI 与完整冻结

恢复：

```bash
python root_20261115_restore_actual165_coast_inputs.py \
  --request public-accurate-coast-three-coefficient-repair-request.json \
  --out "$RUNNER_TEMP/visible-accurate-coast-repair180/restored165"
```

科学（真实workflow经原rules runner启动，token先移除）：

```bash
python geometry_20261115_accurate_coast_three_coefficient_repair.py \
  --request public-accurate-coast-three-coefficient-repair-request.json \
  --restored-directory "$RUNNER_TEMP/visible-accurate-coast-repair180/restored165" \
  --accepted-core "$RUNNER_TEMP/visible-accurate-coast-repair180/original-inputs/accepted.json.gz" \
  --config "$RUNNER_TEMP/visible-accurate-coast-repair180/original-inputs/tail-config.json" \
  --code-directory topics/visible-flex-larger-amplitude/computations \
  --out "$RUNNER_TEMP/visible-accurate-coast-repair180/science"
```

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| 恢复 | root_20261115_restore_actual165_coast_inputs.py | 12957 | `630c288e45efa1f1f6649e9a9588f2dc7d01aea64e7fc9544107c83925f69ee2` |
| 科学 | geometry_20261115_accurate_coast_three_coefficient_repair.py | 33533 | `595bf01cd89690629ca167d5be9d674951d9959d7fd61717a296ecbd3fcd8c4c` |
| 请求 | public-accurate-coast-three-coefficient-repair-request.json | 16925 | `3df438b87ecdd659b7796169d50f84d7daa9e0d02280d3ae5007fa45b212e954` |
| 工作流 | visible-larger-public-accurate-coast-three-coefficient-repair.yml | 20757 | `ee7044e4ab7181d46c92b8cdb1a70b0c8c692e6c017ecff0e47667b8a02d4c66` |

新两源均独立文件，旧21源完全不改。没有修改179、178或任何既有科学预算/接受标准。
工作流只监听新 `computations/public-accurate-coast-three-coefficient-repair-request.json`，未派发未来run。
全部交付在独立 `/tmp/visible-continuous-coast180/`，root唯一Git/ref/dispatch。
