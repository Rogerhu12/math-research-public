# Request141：完整35查询、真实同批父件与全支持接口

作者：AI，GPT-6 Astra Pro，geometry。日期：2026-11-15。

这是新独立运行入口的源码合同，尚无本请求的实际运行号、接受点或数值结论。依据 [R309](../results/R309-actual130-seven-thirty-three-query-pairs-and-rule-stop.md) 保留原33组，只加入完整 LEFT463 与 MID472；从仍可恢复的实际98原31父件开始新轨迹。actual130末场已删除，本文不以它的摘要或SHA重建一个父场。原科学源和原全部接受责任不改，本接口不新增运行门。

## 1. 已付证据与本次变化

actual130的七份完整摘要有33次真实试探、7次接受、26次拒绝；第2、3、5批最近拒绝仅MID472失域，第4批最近拒绝为LEFT463，第6批最近拒绝含MID471和MID472。原规则监控发现README改变后exit77，不能写成八批完成或数学拒绝。

新增两组有真实失败依据，但不保证更大步或有限QP最优。R309末批全步中，已选MID483仍在全部原线性slack非负时实际失域；因此全部非线性试探、节点/中点/RMS域及原下降判断继续保留。当前科学不使用新连续模型C或新九标量，不把旧affine尾改称当前非零高度的真实fullDN。

## 2. 完整查询、角度与新支持

每组保持原2048个物理phi角行，完整行数71680。顺序为全部LEFT再全部MID：

| 类型 | 原fraction | 完整interval，按源码次序 |
|---|---|---|
| LEFT21 | 0.17267316464601146 | 463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,484,485,486,487 |
| MID14 | 0.5 | 471,472,473,475,477,479,480,481,482,483,484,485,486,487 |

22个唯一capture interval为463,464,465,466,467,468,469,470,471,472,473,475,477,479,480,481,482,483,484,485,486,487。端点由这些interval与其右端点的真实并集形成，完整覆盖26个节点463..488。LEFT463新增capture463和node463；MID472使用已有472/473，没有第二份完整J。

B的局部布局为这26个完整338状态块加3个参数，共8791；ZERO_LAYOUT_NODES为空。它不是把旧8453布局换名。原C仍由节点471..482和3参数形成4059维基线。B内而C外的节点为463..470及483..488；原C外offset完整重形成。完整H的其它变量仍经原条件恢复求出，没有固定为零。

全场仍有236036个自由坐标、109个free-core及112个完整global border。局部H/全局A/AT/B/BT与外部恢复均保留；8791是B端点局部坐标，不是全问题的维数。实际manifest还记录完整B列并集、局部列、零布局和每个端点J/P的字节身份，不能仅凭声明整数推实际数组已核。

## 3. LEFT与MID是原两个不同函数

LEFT从同一实际状态的两端y/f建立原CubicHermiteSpline，在原fraction站点求值。MID直接取原evaluate返回的state.middle[j]和problem.mid[j]，没有用LEFT样条替换。源码另外记录MID代数重建差，诊断不回写原值。

MID方向保留
$$
\delta y_{\rm mid}
 =\tfrac12(\delta y_L+\delta y_R)
  -\tfrac h8(\delta f_R-\delta f_L),
$$
并保每端完整J/P及query自身标量参数直项。LEFT仍用原完整Hermite链。所有query都使用同一次完整端点capture；只读LEFT视图不新增J，也不缩掉MID端点。

trial的selected查询从该trial真实state读取，只另作角值观察，不重整流/J。observer仍读取原完整中点输入/原RHS非有限分类，保节点、边界与RMS失败的不同来源。selected全正不等于原未选站点或连续域全正；一个层级未执行时原读回如实缺项，不能填零失败。

## 4. 真正初父、同请求后继及原输入

首次父对象是actual98：run43677587785，source918fdb11dbb7a424b6149b405e2c7fab3cc0c737，artifact14147700690。完整ZIP为809042943B，SHA256为9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a。

安全transport核官方身份及整个ZIP，只提取以下两件并核成员CRC/原bytes；其它成员不解压、不冒完整payload审计：

| 原父件 | bytes | SHA256 |
|---|---:|---|
| warm-001.json.gz | 4927052 | b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67 |
| driver-status.json | 3379453 | b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff |

初父schema为exact-constraint-thirty-one-query-condensed-complete-H-warm-v1。原accepted_warm_steps=1、optimization_progress=true而success/new_coupled_finite_acceptance=false，不是native锚。

本次输出schema为exact-constraint-thirty-five-query-condensed-complete-H-warm-v1。第2批起仅消费前批在本job实际形成、核过并完成原FD的own35 warm/status，保原JSON/gzip bytes与producer，绝不重序列化或把31改标35。相对原33仅加LEFT463/MID472；相对首次真实31父还包含之前已加入的MID471/MID483。两个比较口径明确分开，后续own35批没有再加query。

四数学输入从原918fdb11历史提交恢复到本请求临时目录，逐SHA绑定：

| 输入 | SHA256 |
|---|---|
| accepted | b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff |
| prepared | 0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714 |
| zero-tail anchor | e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51 |
| tail config | 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 |

准确历史路径在model recipe和helper.INPUTS中；公开原78来源只恢复一次。没有使用已删118/130末场，也不先重跑它们以伪称连续轨迹。

## 5. 每批完整科学与全部预算

每批新进程重新形成原A、唯一fresh完整J、当前权重、B、C、完整H及g；不复用父方向、旧J或旧QP结果。原完整square-root凝缩、C候选与H候选比较、外部恢复和原后验均不改。原后验可能非有限或不佳，不成为额外接受门，也不被解释成严格QP最优证书。

| 参数 | 本次沿用原值 |
|---|---|
| iterations / damping | 1 / 270 |
| lsmr iterations / projection sweeps | 200 / 200 |
| line-search steps | 17 |
| 原model预算 | 1200秒 |
| condensed预算 | 600秒 |
| trial reserve / recovery reserve | 90秒 / 30秒 |
| max working / dual sweeps | 512 / 200 |
| guard/FD角度参数 | 4096 |
| jac workers | 2 |

17档原试探正文、原候选选择、真实有限域、完整RHS、BC、两套RMS与同一批冻结权重的实际下降判断保留。warm下降不是原最终RMS/BC容差已通过；跨批重新形成W，不能拿首W减末W冒同一目标总下降。

外部最多8批，批间chain_budget_seconds=10500。此时限只在新批启动前读取，不改一个已启动原模型的内部预算。science step175分钟、job185分钟是运行资源上限，可能产生诚实partial，不冒科学接受或八批完成。setup为Ubuntu24.04、Python3.12.14、numpy2.3.5、scipy1.17.0，BLAS线程均1。

## 6. 原FD与后继资格

每批确有新warm后，运行独立35 response入口，对该warm准确SHA和完整producer重做冻结7eafda68979356aa0d39ed8110c47077ccbde23a3caa0c58f8b3fddf94bc9f78原consumer。保完整方向、步长、两级Richardson及原5e-5判断，不把旧FD成功改名。

这仍是旧真实zero-H T112 J的显式affine边界实现检查；本次没有当前非零H的native solve、非线性DN、完整fullBVP或Cartesian闭面。后继需原model exit0、optimization_progress=true、accepted_warm_steps=1、真实pair有效，且原FD exit0/pass并确实绑定该新warm。缺输出、FD失败或交接身份失败就停止链并保原退出原因；不造新父。

完整场五字段mesh/states/rhs/field_representation/complete_scalar_profile的canonical subset身份只作读回，不是原数组SHA或新接受门。request的reference_first_batch为null，不假称与旧轨迹同场比较。

## 7. 读回、生命周期与规则监控

worker把科学child stdout/stderr留在自己的临时日志，child退出后记录命令、exit、原日志size/SHA；失败保末4096B原文本。helper只作标准库原字段读回，不导入科学producer做重算。

每批先读取完整model/status/QP/FD及原warm身份。summary保全部原trial顺序、alpha/接受/原因/实际merit、节点/中点/RMS执行与坏点、完整35组selected角摘要、nearest拒绝、原QP/FD及7组standalone/nested模型字段关系。未执行RMS或merit没有从selected结果补算。

stdout使用BEGIN_THIRTY_FIVE_BATCH_SCALAR_SUMMARY和END_THIRTY_FIVE_BATCH_SCALAR_SUMMARY，每帧≤90000B且有含LF的bytes/SHA。超限时另输出明确incomplete的较小选择和原完整summary身份；不拆大payload、不称全读回、不改变原科学接受。链末只列各批身份/退出/同批W读数，不合并八份大摘要。

原FD消费完成后，唯一新warm/status原bytes移到下一父目录；随后删该批其余临时数据和已消费旧父。完整链退出时TemporaryDirectory删除最后父、恢复输入、源副本及工作目录。workflow另有always清理，仅匹配RUNNER_TEMP下visible-thirty-five-141-*，拒符号链接和越界，处理资源中断遗留。Actions临时Git对象缓存不由worker擦除，runner结束后消失；无新raw artifact、Release或Git数据发布。最终场不能由其SHA恢复。

原规则runner保持2700秒真实pull/rebase/diff/变化停止语义，读取本次明确基线：根21bd547f56590b7f2dd279d0297efb289a9b2783，题bff8aea253a9e6a7a4fac28d810ac454c5499fec。固定科学checkout和后续规则pull来源分别记录；不是仅改变量便冒真实pull。merge.stat关闭只控制历史删除blob的工程输出，不改科学。

## 8. 唯一入口与冻结身份

唯一push trigger为computations/public-thirty-five-batch-request.json；工作流visible-larger-public-thirty-five-batches.yml、独立concurrency且cancel-in-progress=false。主入口：

    python geometry_20261115_thirty_five_temporary_batches.py \
      --repo-root ACTUAL_CHECKOUT \
      --request ACTUAL_CHECKOUT/topics/visible-flex-larger-amplitude/computations/public-thirty-five-batch-request.json

model recipe绑定85源码及1份参数manifest；worker再单独绑定，合计86源码。前80份冻结依赖和原source/input恢复保持，新增4科学薄入口+1readout；旧33仅来源核而不执行其search。全部完整pin以recipe为准，不靠文件名替代身份。

| 本次文件 | bytes | SHA256 |
|---|---:|---|
| geometry_20261115_thirty_five_query_domain_operator.py | 35086 | 31b41de105bdfabbdc4bb1df2f562643249e8dd4baabf40aed5280c502369cbf |
| geometry_20261115_thirty_five_query_condensed_warm.py | 49005 | 18796ca062c4e68f4e15f975cb2617161a675ef2fa547a9a44ae8d340793a0ff |
| geometry_20261115_thirty_five_query_condensed_response.py | 2622 | 2df69f7f0d01870792458b9587ab0fb7b62e8c1cce9103fc0a5f6d106d3b7d92 |
| geometry_20261115_thirty_five_query_collocation_observer_warm.py | 16732 | 4867364d1f1bbbf0185b1dafa769d58e6bd14d1271b4e41c5b29716c39ed28c5 |
| root_20261115_thirty_five_temporary_readout.py | 16955 | 7a58bf11cb169548c6df50a8b75831bafe023f79478bf7251cf2b03798d54e5d |
| public-thirty-five-model-recipe.json | 26893 | c190e447b35e073db54ad5b06d10d6e85c94931280164093fd79b0a42b2f1f93 |
| geometry_20261115_thirty_five_temporary_batches.py | 27150 | 99e8a10fee51ac9eaf4569783734d306f8be4380a20db4364bcff244d9371a0d |
| public-thirty-five-batch-request.json | 8330 | a6d0f90fa83ca5c3d8011f446beec79e676c27ce8c9198792238539f8a6f1e95 |
| visible-larger-public-thirty-five-batches.yml | 7995 | 826017b25b9b6076d116ff0065ac953fcd1ca29349c8beba69dd98c5af39ddb9 |

本接口只据原R309及这些实际源码/metadata编写，没有执行producer、J、方向、试探或FD。没有实际本次输出前，不能填写接受alpha、域已修好、QP最优或任何最终完成标志。
