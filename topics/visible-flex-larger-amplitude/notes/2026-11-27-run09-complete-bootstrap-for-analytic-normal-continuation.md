# Run09：为完整解析 normal 入口实际重建输入

本请求启动新的公开 Actions 工作目录，先重建完整原 warm 与 R690 reference，以便完整解析局部 J3 入口取得真实输入后继续计算。07 的 cc0a 首场与08的95559分支仍各自保留；没有取消它们，没有把未知 final 或 typed 历史写成空报告。新运行的实际 run ID、输入字节与目标身份均须等真实返回登记，本条不预填。

## 1. 完整请求、控制器与实际边界

完整请求为 [resume-20261127-actions-request-09.json](../computations/resume-20261127-actions-request-09.json)，2817 bytes，SHA256 `852e8e0e73f8ad5ec91f4c26f57003b34c54a2a9c96bb3fe7857a72e68e111d5`。完整初始队列为 [resume-20261127-followups-09.json](../computations/resume-20261127-followups-09.json)，5817 bytes，SHA256 `e1b532445c4fe0e2657e10a24059ec9ed90a80dacf12931bd293f774cf2734ed`；只有原完整 reference 生产步骤，`finish_when_done=false`。新科学入口和纯读尚待完整 source/argv 与真实输入绑定，不能把准备请求算作已经准入完整新求解。

| 完整来源 | SHA256 |
|---|---|
| `public_actions_controller_parallel09_compact_metadata.py` | `e386755a591d9a519f16b674b69c4241246df5dad68ed2eab15da3a9bf29f130` |
| `public_actions_followups_compact_metadata.py` | `3cb1e706ab43dac6e952ce00b41e83055112d2ee65edb37682d1f05e94f2ee3f` |
| `rebuild_axisymmetric_so3_warm.py` | `561308ca74186ac8eeb302dc786b633f2f643a1f98896d0685691d06eec556a4` |
| `so3_axisymmetric_reference.py` | `4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3` |
| `.github/workflows/visible-larger-analytic-normal-20261127-09.yml` | `fa977985f600e6cb9bde664dcf14d7b0aebd5385fb73cd7dcdecab14881e26a0` |

09控制器19006 bytes，从已实际运行的08完整控制器仅改变自己的 HANDOFF 标记和显示编号；逆向替换逐字还原原体。科学命令生成、完整小卷、真实pull/README检查、非快进rebase重试、raw只留runner及完整队列消费函数不改。新控制器已作stdlib AST parse/compile；本机没有import任何科学模块。

工作流仍使用原固定checkout/setup-python提交、Python3.12.14、NumPy2.3.5、SciPy1.17.0、CPU Torch2.5.1与单BLAS线程。job上限350分钟、控制器预算20000秒，属于本次运行边界而非研究终点。不同并行组不会自动取消07或08。请求文件变更触发本工作流，科学child不会接收认证环境变量。

## 2. 原科学输入构造全部保留

warm完整委托原 `reproduce_and_solve.py`，真实重建五次已接受prefix与四个完整warm步骤；仍核原099历史输入、全部原来源、每个producer journal和所有已声明输出。它不是重放旧优化方向，也不是再次宣告已登记结论。不能用缺失旧scratch作为伪造当前输入的理由。

完整reference步骤从08第2步的完整原参数归档逐项复制，仅改变新步骤ID与用途说明。此次实际验证 `script`、`parent_bundle`、完整 `args`、全部 `outputs` 和完整 `summary` 五个对象与原条目相等。完整原参数继续是：2048角、8阶seed积分、128 panels、300秒scalar准入、`1e-18`积分请求和`1/8`尾截断；全部旧1845与新5532观测、M160/J923/N2048、原923准确节点和全部十一份历史输入均保。完整argv在队列原对象中，不用此段摘要替换。

原请求追溯到完整run05归档 `resume-20261126-run05-returned-steps-archive-001.json` 的第0对象；旧归档SHA `36399e5355fc5778d43092a316ffff6c05e256b02d16330124b581860d6e2829` 与原步骤ID继续保存在新对象内。旧参数上的历史作用域保留，不把这些输入解释成已经读取07/08新发现的地点。

## 3. 首场之前必须绑定真实固定目标

08完整生产器已经实际返回7c图与d469固定目标，但09不能直接冒用其warm/reference/whole-file SHA。09返回后须读取完整实际输入元数据，并由完整消费者核真实160字图、准确scalar/nodes、完整reference模型和NPZ、完整旧/新载体及固定目标；若字节或数学定义不同，应明确记为新固定输入，不能静默放宽08守卫或声称同g。

原全部 P0、两份完整 G、曲率分支、双号幅度、所有自由变量、32段normal链、H²坐标、原Phi、真实筛查与回溯判据保持。07未知来源为cc0a，08未知来源为95559；新接口须逐run绑定确切来源，保未来适用历史完整合入责任。数学目标一旦为新分支冻结，就不能在优化过程中随当前core/H改变。

解析局部J3和不可变根记录器的完整源、全参数及严格seed迁移另行公开后才可加入该队列。不存在“缩少32段”“删自由量”“只筛少数永久点”或把数值缓存身份冒作根支证明的许可。实际初始场、导数、QP、连续费用与几何证书都仍待真实运行。

## 4. 交接与保留

为给09独立槽留足空间，HANDOFF的重复说明缩写并指向已公开 `4815339aa6cde9296ba221edb380f30073b9a1e0` 的完整前交接。06已实际结束的自动槽移归该固定历史；当前H仍保06完整终态/父分支/未返责任段及其完整note。07/08活动槽原样保留，任何历史或未返步骤都没有删作已完成。

新请求读取的规则提交为 `b8cc8fe52d7bd121a088c1f8efc0405e3f5ac333`，双README整SHA仍为581402…/3c1c…。普通发布前后与控制器每次真实pull均继续核差异，改变即读取并遵新规。raw不进入Git/Release/artifact；最终仍须同一固定g、整面算子范数容差、全t闭面/握持/变形/非全等/reach、真实mesh与频率精化及可复现多t网格。启动或job预算结束均不构成课题完成。
