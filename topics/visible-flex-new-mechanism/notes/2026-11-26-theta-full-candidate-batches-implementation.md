# 2026-11-26：从513末态完整分批定位角峰

## 已证瓶颈和这次改变

run45790610433 的原始收据分别为 theta-513-b030/b038-original-terminal-receipt。B030 的一个几何可行trial有733个待定位候选，B038保留q在新941细径向格上有518个，均被旧总上限512整批拒绝，目标求值数0。两者均非时钟、优化器backend、513径向cap或1024峰库cap触发。

新独立入口 scripts/inverse_r566_theta_peak_batched_20261126.py 将512改成**候选批大小**，完整处理原相同算法枚举的全部候选。每批按原确定顺序处理至多512项，随后继续下一批。没有按值删候选，没有缩窄near-band，没有改变局部角优化的区间、xatol、maxiter、边界点算法或回退原采样点的逻辑。每个字段/径向圈的原最大值及近活跃局部峰仍全部保留。

物理模型、1536均匀FFT、真实角oracle、分块参数AD、全细网接受门、working margin、覆盖当前实际违规的urgent判定及trust规则均不变。径向cap513和额外峰cap1024也保持；后者虽接近，尚未真实触发，不能假造一次已经发生的容量事件。若下一次真实产生超过1024的proposal，应准确保留后再界定下一范围。

## 真实来源，不换成更低eta的被拒trial

来源source48e3048105f2e4e83c537beddb4bdefb99ae6e21，run45790610433。新loader拒绝旧joint或首次theta schema；绑定前驱wrapper0093d8ce3b80600a6b4eb0d921208423ca390cbc957497b026d8ef230355aaa1、原物理driver6094c15ff2696d6b64e9eac09ce60b54a59a64c545cb88fb7734df8bb185f757及oracle46eea6c6da4a94c82106e8a57ff98e70bf8f85bd2d0ef35c26cb649a0ee2f0a7。

| lane | 源actual径向/峰 | 源最终proposal径向/总峰 | 本次采用 | 源actual / next trust |
|---|---:|---:|---:|---:|
| B030 | 443 / 1012 | 450 / 1021 | 450 / 1021 | 1.20135498046875 / 同值 |
| B038 | 470 / 508 | 470 / 508 | 470 / 508 | .9010162353515625 / 同值 |

两条完整actual_terminal_state和完整last_unapplied_constraint_proposal均与原FINAL逐项相等；81q完全继承。B030用保留真峰eta约.275005的q，绝不取未定位的.270897 trial；B038用先前500候选确实定位后接受的q，但承认它在最终新网格上的518候选尚未解决。本次先执行完整起始细扫和全部518候选，才能按新观察判断其资格，来源classification不会被强行改成可行。

所有原actual+pending径向和真实角峰轨道合并保留；不清历史峰库，不重置trust。B038前驱actual470网格已构造但未运行backend的身份也保留在来源收据。每个新actual只在本轮oracle构造成功后登记。

## 时钟中断和全部费用

每个候选开始前及其每次目标求值前检查合作时钟。中断时返回 clock_checkpoint，而非空的成功扫描；记录完整候选数、已完成数、未解决数、批数和全部目标求值数。未完成候选逐项保留字段、准确s、径向/角索引、区间两端及采样值。

THETA_PEAK_LOCALIZER_PARTIAL 还直接打印该q、完整观察径向格、FFT节点数、已完成峰列表及全部剩余区间。q的binary64 SHA和oracle identity一起绑定；发生中断的当前候选即使已付部分目标求值，也仍列为未完成，同时已付调用数保留。无须为了记账额外求任何几何值。最终状态和被拒trial分别沿用原口径，不把部分局部扫描当成完整门。

THETA_PEAK_LOCALIZER_BATCH 每批打印累积求值/完成/剩余及真实耗时。总wall、底层oracle totals和新候选/批计数共同覆盖成本。主循环仍先判断全细网及observed几何/eta；任何未解决扫描都不能接受。新时钟状态与普通localizer backend未收敛分开。最后reserve期间的partial也保留剩余manifest。

## 已付算子核不重复、源闭包与正式执行

原run45785004209的uniform parity和offgrid参数方向检查仍按原两job、driver、oracle及1536规则绑定，本次新接口检查数0。这里只改候选调度/来源/可恢复计数，不改算子；不另跑独立验证科学。

新请求 computations/request-inverse-theta-peak-batched-20261126.json，新workflow .github/workflows/visible-inverse-theta-peak-batched-20261126.yml。11个完整绑定均在sparse checkout，包括旧hard-resume和前驱theta-resume。两条source-state单参数UTF8长分别115014和70869 bytes，均低于131072字节单参数限制；这是对必要q/网格/峰坐标配置的静态检查，不是科学执行。没有把原日志或大几何数组加入仓库。

仍为公开Actions两lane/max2、50分钟job、2400秒科学段、真实公/私双pull和README核、固定Python3.12.14/numpy2.3.5/scipy1.17.0、固定两个action SHA、stdout-only无artifact/cache/Git写入。本地仅源码/AST/hash/import闭包和已有原日志的输入逐项核对，未执行模型。全程可变设计g，尚未付固定g精化、连续全域覆盖/reach或README全门。
