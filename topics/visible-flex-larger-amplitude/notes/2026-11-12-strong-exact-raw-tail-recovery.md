# 严格同离散的原始射击暖恢复入口

**当前状态：源码、语法与数据身份检查完成；尚未运行新的物理tail求解。**
这是两个正式−9之后的独立新入口，不编辑原frozen/resumable/数值源。

## 改变与保持

完整非IO参数必须逐项相等，包括M、N、物理depth、展开段数、steps、parts、所有
物理参数和原容差；rawNode、全部577×48状态、9个rawStates副本也核对。
只有这时才逐位复制原states，省去重新求Q/L的几何remesh。首次请求全部24H
逐位等于该恢复包cutHeight时，直接把该raw状态作为initial；明确跳过ratio1的
几何amplitude remap及warm-only边界补偿。它仍接受原完整非线性残差、Newton、
完整variational、positivity、line search、完整audit检查；不借旧norm宣布成功。

同离散但不同H的首次请求仍使用原几何amplitude warm和Dirichlet暖补偿；原
true-DN接受门不变。不同离散的旧包目前直接拒绝，这个入口不是M24→M28的
谱延拓器。为保持源身份严格，新client把三个新增warm/storage源hash加入正常
source集合；后续cached/release前缀使用对应的新production wrapper，不能以
旧client伪装同一完整来源集合。

另外在checkpoint读取前、ready之前、request暖变换之前显式global.gc()，记录
前后heap/RSS。原full-solve前的GC保留。GC只释放不可达对象，物理函数和操作顺序
不变；其内存收益尚须实际观察，不能因此推断前两次−9是OOM。

## 独立文件

- strong_exact_raw_tail_warm.mjs：完整参数/状态守卫、逐位复制、H相等和GC记录。
- strong_exact_raw_tail_worker.mjs：锁定frozen worker SHA并记录所有唯一文本替换；
  原数值core、物理构造、fullJac及audit保持。
- strong_exact_raw_tail_client.py：原协议和frozen profile守卫，追加新源及变换身份。
- strong_exact_raw_same_height_tail.py：锁定ef8独立runner，显式换新client并追加来源。
- strong_exact_raw_three_control_bvp.py：锁定a84实际生产入口，显式使用同一新client；
  前缀M+3方程、边界、原acceptance及7fc的严格audit缓存都不变。
- strong_exact_raw_tail_guard_check.mjs：真实旧恢复包与已接受ready的纯数据检查。
- strong_exact_raw_recorded_tail_check.py：原e009协议检查加显式主packet-ready输入。

## 已实际核对的范围

两个JS源及虚拟frozen/pinned worker层已通过node --check语法解析，不执行模块。
三个Python生产/检查wrapper及其虚拟源AST通过；独立--prepare-only exit0，
worker_started=false。真实记录数据检查9项全通过，fullStateFloat64LE SHA见
strong-exact-raw-tail-data-guards.json。该检查用的是metadata descriptor，
physicalFactoriesCreated、RHS、Jacobians、Newton、newResponses全为0。
因此不能把这些检查写成新实际解或物理factory已经运行通过。

## 实际重做与协议核对

fresh计划为strong-actual-q105-sameH-tail-audit-exactraw-r1-command-plan.json。
从已推原r1试步恢复（SHA9bfe4149…，旧norm5.560497e−11），仍heap256/cache2，
M24/N512/depth8/steps12/parts8/tol2e−9/fullJac+audit，原数学配置全部不变。
等待exact当前独占窗口正式退出之后运行。

新真包成功后，先用其准确ready做原协议的7项单packet检查；不可拿旧来源集合
不同的q095包伪装成第二个同源packet来强行通过3项optional release replay。
7fc release实现本身未修改。实际前缀产生下一个同源完整audited H之后，再用
两个真实同源包重做全部10项。新响应source集合及ready会完整保留，不制造
新H响应、不改标签绕过source守卫。当前没有新q105 prefix或完整闭面声明。
