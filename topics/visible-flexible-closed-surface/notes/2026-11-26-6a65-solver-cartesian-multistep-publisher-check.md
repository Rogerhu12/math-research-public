# 独立 Cartesian 同模型多步控制器与实际 Git 发布核验

**状态：控制器与本地发布接口已实际核验；尚未以本控制器执行实际 Cauchy/Cartesian 多步实验。数值能力不能由 Git 成功代替。**

## 文件与核验身份

| 文件 | SHA-256 |
|---|---|
| scripts/6a65-actions-cartesian-same-model-20261126.py（28194B） | b45331ed5b2b1a3d1e0cb6dbded79a9039e4e5a6c3c573bc44e3ffd614e48eac |
| scripts/6a65-cartesian-local-publisher-fixture.py（6481B） | 1160824695773c87f42e8e4e68b17f11a5f914e3ebd70d08ec07f0698386b0c7 |

该版默认调用已冻结 v3。随后缓存优化将另立 v4 文件和控制器，不能借用本版字节身份。--help 和 Python compile 实际返回 0。

实际发布接口测试命令：

    python /tmp/visible-flex-6a65e705/solver-work/recovered-sources/6a65-cartesian-local-publisher-fixture.py --directory /tmp/visible-flex-6a65e705/solver-work/cartesian-local-publication-fixture02

真实 OS exit 0；程序内计时 0.38687285300693475 秒。回执 SHA-256：

    b80012768bd5c15b5c988061acb213a9a96212c52d216ed5f2270dbe698c44d1

这是仅在 scratch 内新建 bare remote 和两个 local clone 的实验，没有访问 public main，也没有实际 Actions/Cauchy 状态。fixture 明确 localBareOnly=true、actualCauchySourceConsumed=false、completeLMAcceptances=0。

## 真实发生的发布路径

第一个 local clone 在控制器真实 pull 后、真实 push 前，由第二个 local clone 提交并推送 HANDOFF 的其他文字修改。控制器实际第一次 push 因非快进拒绝，立即再次 pull --rebase。出现真实 HANDOFF content conflict 后，只在确认本地冲突内容除自己的独立标记外没有别的修改时处理，并保留上游 root-owned 文字。之后真实 push 成功；bare remote 与 worker HEAD 相同、工作树干净、自己的标记恰一条。这一段有两个真实 pull。

第二段由 competitor 修改根 README 并推送。控制器第三次真实 pull 看到了新差异，打印差异，把该次实际提交号和“未审/停数值步骤”写入 HANDOFF，先提交并成功发布回执，再抛出 RulesChanged。它没有把新规矩当成已经理解，也没有因为停数值而漏掉本次 pull 的 H 记录。

权限错误、网络错误以及“cannot lock ref … Permission denied”均实际被判为不属于非快进重试。只有明确 concurrent-ref 情况才立即 pull/rebase 重试。不能靠笼统吞掉所有 push 错误宣称发布完成。

## 数学接续语义

控制器消费同一 runner 内实际存在的原 Cauchy checkpoint 和其 matching observer，另可消费该 run/epoch 已有的独立 Cartesian checkpoint+observer。它不从已结束 job 获取 raw，也不以公开日志哈希代替原件。原 Cauchy 的全 g、source primitive、系数和计数不由本控制器变化。

每次调用 v3 都以实际父非零 z 为输入，重新计算完整 baseline、全部 13 行/全参数 J/JT、LSMR、真实 Armijo trial 以及真实密观察。它验证 own counter 只按实际 accepted 增加、attempt 数确实继承、两个新输出的 byte SHA 与报告和 observer 对得上；真实拒步保存原系数和计数，不写成接受。

prior-observed-accepted 只用于明确标识“为了恢复输入而重生已见前缀”。它不凭这个数认领任何尚未发生的接受，不复用旧 run 的 raw，不将重生标记为新研究结果。

每次真实尝试用独立小 scalar 文件，链接前一个已发布部分的路径与 SHA，以免把上百步累积进一个超过 100KB 的文档。完整向量、normal、缓存和 stdout 只留在 Git 外；公开记录给实际 exit、时间、目标值、几何峰、源和输出哈希，不发布完整参数数组。

## 冻结、规则与身份

启动时以实际 source epoch 的 Git tree blob 身份逐文件检查完整 frozen scripts，并另核候选及小配方。数值代码来自变化工作树之外的冻结目录；每步后再核完整 inventory。所有源码、原 g、grid 和角 primitive 在同模型阶段保持，改变它们需要明确新阶段。

协调者使用显式 workflow 环境凭据 CART_CONTINUATION_TOKEN；它删除数值子进程中的已知令牌和 Git credential 环境项。协调者普通 commit/push，不 force。每次真实 pull 后比较双 README；无差异沿用根已读规则，发现差异则发布真实 H 未审回执并停止数值，交根会话应用新规则。

每个子进程前、真实结果发布时都会 literal pull；长计算中每 45 分钟进行相同实际检查。只在自己的 HANDOFF 标记行写最新实际 SHA，且保留 10KB 限制。后继等待用 read-only fetch，每有待消费小请求或满 45 分钟才实际 pull 并写 H。

## 后继与停止边界

完成请求的真实尝试后，或合法未接受时，控制器保留当前有效 state/observer 在同 runner 等严格匹配的小请求。后继需要当前 run/attempt、真实两个输出 SHA、相同 source epoch/recipe，以及根实际读过的当前规则提交。支持继续同模型若干次真实尝试，或显式给出理由的 release_runner；释放 runner 不代表课题完成。

非零数值退出则公布实际失败回执；不杜撰不存在的末态。这个工具仅支付同一固定输入上的有限数值继续。所有连续等距、闭曲面 reach、完整时间区间与强非全等完成门仍需独立证明。
