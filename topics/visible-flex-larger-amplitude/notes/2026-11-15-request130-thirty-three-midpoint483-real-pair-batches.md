# Request130：原32查询只增 MID483，从真实98另起33查询轨迹

作者：ChatGPT（amplitude 子任务）。日期：2026-11-15。

**类型：源码接口／有原数值依据的未执行实验设计。** 本项仅准备独立源码、配方和一次Actions请求；没有本地科学运算、数值fixture或派发。下面用作选点依据的数值直接来自[R289实际118结果](../results/R289-actual118-eight-thirty-two-query-pairs-and-midpoint483-barrier.md)，不能读作Request130的结果。

## 1. 为什么只增 MID483，为什么从98重新开始

实际118 run `43693006085`、source `bb1d75675dc639f3f1ab74749798a5c11b2ac3a5`、compute job `132747387808` 完成了八个原32查询模型及各自新warm的FD。后四批最近拒绝均只有未建模MID483失域。末批接受 $\alpha=1/256$；最近拒绝 $\alpha=1/128$ 的MID483给出原 $\beta^2_{\min}=-0.0008413561364628563$，站点 `1.2367303492381132`，最坏角 `2.8440003807399785`、角下标927，4个负角、0个非有限beta角。该点原middle输入有限而原RHS非有限，32个已选查询在同一步均无负角。

选择只补MID483的全部2048原角点。它不是LEFT483，也不是把邻节点域当作中点域。R289同时保留早先最近拒绝中的MID472及更大试步LEFT463等限制，本次不宣称它们已消失，也不据增一组线性约束保证更大实际步长或完整QP最优。

原118末warm/status已按规则删除，不能由SHA恢复场。本请求**不重演118八批然后改名接续**，而是从仍可精确恢复的实际98原31 pair直接开始新的33-query轨迹。对比口径分两层：

- 相对已冻结32查询算法，唯一新增为MID483，原MID471保留。
- 相对第一批实际输入98的31查询producer，当前查询定义增加MID471和MID483。helper的 `query_changes_since_this_model_input` 首批准确列这两项；后续自己的33-schema输入列空。

真实118末warm SHA `46adc694ff2d989e16924c3469ba1d208630406a6e4cb5f338484bd055a540f6` 和status SHA `dd24bfeff587a9b73677fffb398ca494ccd6889bfc38361580cf197893011b3f` 仅作为原结果出处，不会被当作可读取的本次父文件。末原摘要43258B／`d996ed38e592b491b95f6e31bb01fd55ff0cbdc820ca45b8c4deac2564bea7c6` 同样只定位证据。

## 2. 冻结文件

全部新源位于课题 `computations/`，workflow位于根 `.github/workflows/`。旧32、旧31及其工作流不修改。

| 新文件 | 字节数 | SHA-256 |
|---|---:|---|
| `geometry_20261115_thirty_three_query_domain_operator.py` | 34843 | `3c06f9c59b91d39b6a7db86e7017ca50dcf5549764f3aed143102c9913fb93d5` |
| `geometry_20261115_thirty_three_query_condensed_warm.py` | 48548 | `18827b3f4bcc67d96875a25f86c71ded459e4a9b505d071b2d0dfda208ce31e7` |
| `geometry_20261115_thirty_three_query_condensed_response.py` | 2625 | `cbb533db27892d6918de7d81c9053db5750a7954c3ef74a07235c5511b911289` |
| `geometry_20261115_thirty_three_query_collocation_observer_warm.py` | 16736 | `c2bfbddc3e680c00627c0a33d16efd1cccf1ee7fd9971a12012ef6322b45d244` |
| `root_20261115_thirty_three_temporary_readout.py` | 16743 | `9415e05990f64b02287bcf37bf1a870c756f4864ac72a867fa269c453bd8b743` |
| `geometry_20261115_thirty_three_temporary_batches.py` | 26878 | `63dc6829f4ea022af369129f0d5f67e334c02c0edbd65f1b78ad50c03a7703f9` |
| `public-thirty-three-model-recipe.json` | 23213 | `6fc6cac93c4d205a3bf829014c76621f4123f257f62aec0a8e7de21a35c1ae68` |
| `public-thirty-three-batch-request.json` | 5878 | `53d4e417947997bdb7506202a2d3e450305ee566e3e7f621ec455c65551df82d` |
| `visible-larger-public-thirty-three-batches.yml` | 7985 | `25d81c4d02240dd0d5543fd1a0432ada72e95da500acd4a42d324cdc9d423050` |

数学四源分别薄改自原32四源：domain `a55edba9bf4dde9c909ceb6aa47aee5957ed4d26fa13dd40f8bf38d9ce74df0f`、warm `3f4162b9594acb5c7607f3329e757dad3e18311a1544ea20a081f5c4689cafb8`、FD `47f420ad7dcddee0192ac6eb02aec4caedbfb66e3100d5fe879261cc33251e73`、observer `845af95d9481ef2c30bf76d8169f91c5a3640980400b0b69828cf6c7cadb3f5d`。原helper `a05af3878e1f93c66a8f0b253be0936ddc4342438f4dbd13d4ed178ed6f4955d` 和worker `336fc52205446977ed936035e06818abc2aebb732d1b41c8d8f2fb49eb2266b0` 的输入恢复、真实pair生命周期及原读回算法也保留。

每一新文件都有相对原118文件的完整 `.diff`，仅作本地交付依据；不新归档可重算data。本文未填写未来run或输出SHA。

## 3. 完整typed查询、capture与局部支持

本次顺序仍先LEFT、后MID，每组原角下标 `0..2047`。LEFT分数是原 `0.17267316464601146`；MID是原collocation构造，不与LEFT共用一个fraction。

```text
LEFT20:
464,465,466,467,468,469,470,471,472,473,
475,477,479,480,481,482,484,485,486,487

MID13:
471,473,475,477,479,480,481,482,483,484,485,486,487
```

共33组、67584行。新MID483位于typed group28，排在MID482之后、MID484之前；旧MID484及后续MID组号相应顺移。当前模型、真实trial、verify及导出均使用同一 `QUERY_SPECS` 循环，不能沿用旧组号标注。

`CAPTURE_INTERVALS` 按全部typed区间union自动形成：

```text
464,465,466,467,468,469,470,471,472,473,
475,477,479,480,481,482,483,484,485,486,487
```

因此**捕获区间从20增到21，新增483**。两端点483／484此前已在端点并集中，实际端点仍是464至488的25个物理节点；完整B局部坐标仍为8453，全部三项global p保留，zero-layout仍空。这里不能沿原118笼统说“捕获区间不变”。源码／recipe／worker明确记录 `added_capture_intervals=[483]`；同时分别记录端点并集不变和没有新增局部坐标。

原C基线只修正节点471至482及global p，共4059维。完整B在C之外的节点仍为：

```text
464,465,466,467,468,469,470,483,484,485,486,487,488
```

新增MID483的两端点都在这个C外部集合中；它们的实际贡献仍进入原有效offset `c+B_out*z0_out`。这不表示最终方向把外部固定：完整R270条件恢复保所有外部响应，之后原全向量radial／backup／同f选择仍可改变外部坐标。全部236036原坐标、free-core109及原边框／pure-global行保留。

## 4. 新MID483的实际基点与导数链

基点直接读同次原evaluate已返回的 `state.middle[483]` 和 `problem.mid[483]`。新query不以RMS样条、半节点线性平均或另一次whole flow替代。其原构造及变分沿冻结32公式：

$$
Y_{\mathrm{mid},j}=\tfrac12(Y_j+Y_{j+1})-\frac{h_j}{8}(f_{j+1}-f_j),
\qquad
\delta Y_{\mathrm{mid},j}=\tfrac12(\delta Y_j+\delta Y_{j+1})-\frac{h_j}{8}(\delta f_{j+1}-\delta f_j).
$$

Gamma作用到两端原J/P，加上query处直接scalar Pi，形成原left／right／p三块，再按原chart.scale除一次。483号capture记录是这条新完整链所需的真实区间记录；即使两端点已有，也不能省略该记录而冒成旧20区间合同。

全J仍由原 `CompleteLinearization` 唯一构造，capture只截同次原A中的既有端点J/P。源guard、同方向完整complex链、adjoint及local/full检查保原阈值，未增加科学门。所有B／B转置用同一冻结块scatter，新增query仍完整2048行。新的A／weights／B／C／H／g均从本批真实parent重新形成；这里不预称不同运行的浮点因子或权重逐字相同。

## 5. source闭包、首父与后续own-schema

新domain schema为：

```text
captured-thirty-three-query-original-RMS-and-collocation-midpoint-domain-v1
```

新warm及FD使用：

```text
exact-constraint-thirty-three-query-condensed-complete-H-warm-v1
```

warm仍导入原31 producer作为父schema／来源验证基线，**没有改成把32输出作为首父**。`ACTUAL98_WARM_SHA`／`ACTUAL98_STATUS_SHA` 仍精确硬锁如下；以后只接真实同job own33 pair。父producer子树、原constant状态、scalar profile及来源记录保完整，不递归改写旧31身份。

新domain的 `source_identity` 显式读取并核原32domain的a55 SHA；新warm的 `SOURCE_NAMES` 与 `FROZEN` 同时包含这个实际被hash的原32文件。这消除了只写新文件名却遗漏原实现来源的情况。model recipe保原118的75个pin逐个不变，新增四科学薄源和helper共5项，成为80项；batchrequest再单独pin新worker一项，共81个显式source身份，另保原 `source-dependencies.json` 参数SHA。

旧32domain是实际哈希基线；旧32warm／FD／observer／helper及旧107入口仅留作来源，不执行旧32搜索或其main。完整原数学依赖仍由原guard／imports及78来源恢复负责；80项并非一个伪称列尽全部传递import的数量。新entry所有正在调用的组件、原transport、原selector和规则runner均有原pin。

## 6. 实际98原件恢复：原完整ZIP与仅两个成员

原父tuple完整保留：

| 项目 | 实际值 |
|---|---|
| run／source | `43677587785`／`918fdb11dbb7a424b6149b405e2c7fab3cc0c737` |
| artifact ID／name | `14147700690`／`visible-followup-condensedqp-43677587785-1` |
| 原ZIP bytes／SHA | `809042943`／`9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a` |
| 原warm bytes／SHA | `4927052`／`b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67` |
| 原status bytes／SHA | `3379453`／`b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff` |

原transport `exact_20261114_fetch_pinned_public_artifact.py` SHA `51224788078acff0a522b4850c8d971a29cbc6d3cecd1c7cd1a724aaa24aa859` 仍负责official metadata、完整ZIP size/SHA。原98selector `root_20261115_read_existing98_scalar_summary.py` SHA `e2e8ec32c30bbc9ff0e77709524ff09f100f0ff5f4decd23c43b6445562b7484` 提供原PIN绑定和安全ZIP目录读取。

完整ZIP核过后，仅选择原 `thirty-one-condensed-warm/warm-001.json.gz` 和 `driver-status.json`；成员大小、SHA、解压CRC及唯一安全路径按原函数检查。其他成员不解压、不重新审计；不能冒称全809MB各payload已逐个检查。原status是原JSON字节，不重序列化；warm gzip也不改header或内容。选择后立刻删除本请求ZIP副本。

原四数学输入从同 `918fdb11...` 历史精确恢复，SHA分别是accepted `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`、prepared `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`、zero tail anchor `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`、T112 config `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。本线仍是原affine-tail前缀优化；没有native或完整fullDN调用，也不借新九H请求的field或native状态。

## 7. 每批仍为原单模型加该新warm的原FD

每批模型CLI保持原值：

```text
--iterations 1 --damping 270 --lsmr-iterations 200
--projection-sweeps 200 --line-search-steps 17
--budget-seconds 1200 --angles 4096 --jac-workers 2
--condensed-budget-seconds 600 --condensed-trial-reserve-seconds 90
--condensed-recovery-reserve-seconds 30
--condensed-max-working 512 --condensed-dual-sweeps 200
--condensed-store-root
```

原完整C候选与R270完整H候选仍按同一原f比较，保原可行ray／radial修复、真实全A／AT／B／BT读回，有限QP预算后验仍只是原浮点读数。未用小局部KKT替代完整方向判据，也没有更改原17档试步、RMS、BC、节点／中点、材料域或接受阈值。

只有原模型实际exit0、原状态为 `optimization_progress=true`、`accepted_warm_steps=1` 且真实新文件齐全，才按原consumer对它运行完整FD。FD以实际新warm SHA绑定，所有方向／步长／Richardson及原阈值不变；它保原zero-H affine响应口径，不冒当前非线性native完整J。

进入下一批还须原新warm FD真实exit0、`implementation_check_passed=true`、prepared SHA正是此warm且 `complete_current_warm_boundary_FD_actually_recomputed=true`。这些是原已付续接合同，不新增科学验收门。缺新warm时不跑伪new-FD，不把98或先前FD改名成本批结果。

真实pair移动前后只核原文件字节；`optimization_warm`／status identity保持原子集关系。旧parent只有在真实新pair及FD已完成后才删除。每个模型是独立child，重新构造同一个完整模型；不会把同一entry的 `--iterations` 盲目扩大或复用旧方向。固定权重merit只在各自模型内解释，不能跨批相减作同一目标下降。

## 8. 批次、墙钟与唯一工作流

本请求最多8个完整model／FD pair。批间预算10500秒，只在开始下一批前检查；不会缩短活动中的原1200秒模型、FD或原试步预算。外层science step175分钟、job185分钟沿原118；step还包含原件恢复和规则初始化，因此不保证8批总能完成。平台或规则中断不是新数学拒绝，已有原输出仍保实际阶段，未完成的batch不制造新pair。

原worker停止值保持明确：达到批数是 `explicit_maximum_batch_count`；批间到时是 `explicit_between_batches_time_budget`；模型、FD或pair交接失败分别保原原因及原exit。科学最终 `success`／`new_coupled_finite_acceptance` 仍false，不把warm进度当最终BVP接受。

独立workflow `.github/workflows/visible-larger-public-thirty-three-batches.yml` 只响应main上的 `topics/visible-flex-larger-amplitude/computations/public-thirty-three-batch-request.json` push，新的concurrency group不取消已有运行，无第二dispatch。执行命令为：

```text
python -u topics/visible-flex-larger-amplitude/computations/geometry_20261115_thirty_three_temporary_batches.py
  --repo-root GITHUB_WORKSPACE
  --request topics/visible-flex-larger-amplitude/computations/public-thirty-three-batch-request.json
```

Python3.12.14／numpy2.3.5／scipy1.17.0、原单线程设置及checkout／setup固定action SHA不变。恢复历史Git对象不切换科学checkout。原规则runner SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde` 代码不改，只以已读两README实际字节设当前BASELINES；2700秒真实pull／rebase／diff／规则改变停止保留。根README blob `74c08a36f6c997d0bc1e64a7956b42276f5fa5d7`，课题blob `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。`merge.stat=false` 只约束Git输出，不改科学门。

## 9. 紧凑原读回与可重生payload生命周期

新helper仅标准库，原恢复／选字段算法不改。每批在compute日志打印一份：

```text
BEGIN_THIRTY_THREE_BATCH_SCALAR_SUMMARY
<原JSON字段选择，compact编码，最后恰好一个LF>
END_THIRTY_THREE_BATCH_SCALAR_SUMMARY
```

对应 `thirty_three_batch_scalar_identity` 保bytes/SHA。原trial alpha／accept／merit／node-mid／两套RMS是否执行／实际坏点与33组beta minima、negative／nonfinite counts均按原顺序保留；typed定义只记录一次，不每组重复庞大来源树。最近失败有完整必要原坐标和角摘要；原collocation observer及原冻结W字段照旧读取，未增加RHS／J／weights调用。

90000B上限与原显式回退策略保留：若正常选择过大，先记录完整选中summary的bytes/SHA，再给标明 `scalar_summary_complete=false` 的小选择；仍过大则给诚实小失败记录，不冒完整读回。没有把大型原报告机械拆块进Git或新artifact。

worker在读取本批原输出、完成FD并选出真实下一pair后，删除本批可重生raw树，再打印已经保在内存的纯JSON标量。真实下一pair暂留到下一次消费；末次临时上下文退出时也删除。workflow的always cleanup只匹配 `visible-thirty-three-130-*` 自有路径并拒绝越界／symlink。原job临时Git对象缓存由Actions生命周期负责，wrapper不冒已擦除它。

零raw artifact／Release／Git data上传；只保公开源、参数、实际run和原标量／SHA。当前118末场已经不可恢复的事实不会因保存新checksum而改变。真正新33场也只能在本job仍存在的pair内续接，不能将结束后的hash当作外部checkpoint。

## 10. 本地静态范围与未付责任

本地只做源码／JSON／离散索引／SHA／AST。80个配方source及独立worker pin真实对应，原75项全部保留；首actual98原pair和全部原atomic flags逐值不变。静态确认新增区间483、21capture、25端点、8453／4059布局、33typed顺序及实际被hash的32domain进入当前来源闭包。

原domain构造／完整complex核／export的算法AST除列明的描述文字不变；原完整evidence、C/H selector、project、原唯一J捕获、read-only observer、恢复输入／原件及真实pair移动等核心AST均未变。5段shell和3段inline Python语法通过。没有导入科学源、求任何矩阵、运行fixture、修改旧源或Git。

新增MID483是一条有限算法约束，完整残差、域责任、物理行155819、有限512工作集精度及未选点仍由真实新运行决定。Request130不承诺更大接受步，不把原affine FD、暖步或局部QP完成当作非零native／fullDN／闭面完成。
