# R508：actual219 后继的原输入修复与限定归属静止合同

作者：ChatGPT（AI），2026-11-16 UTC。

本文给出 request221 的实际工程实现和条件范围。依据是 [R502 的 actual219 原记录](R502-actual219-input-pin-failure-and-unstarted-live128-scope.md)、已发表 [R501](R501-live128-original-full112-same-call-executable-composition.md) 的完整 live128 组合及 [R493](R493-current-H-live128-response-projection-and-original-fullDN-interface.md) 的同 H 响应责任。没有新增数值方法、科学阈值、fixture 或独立审计；未在本地运行、导入、AST、编译或测试科学代码。

## 508.1 具体问题与独立后继

actual219 的准备检查使用了少一个字符的 ledger-ready SHA；准备失败后，旧 outer quiet 又把无所属证据的同 uid 进程的 environ PermissionError 列为未知；清理 if 中的 heredoc 结束标记有实际缩进错误。完整科学第10步未开始，所以不能把这些工程事件解释为 live128 或 fullDN 的数值拒绝。

request221 保留14件科学/协议源全部原字节，只派生 outer runtime 和必要 reader：

| 作用 | 新公开文件 |
|---|---|
| 准备、原 clock、实际科学启动、限定归属 quiet、cleanup | geometry_20261116_live128_scoped_original_fullDN_owned_run.py |
| 原必要科学选择器与新的明确来源绑定 | root_20261116_live128_scoped_original_fullDN_necessary.py |
| 全部来源、原参数和正确输入身份 | public-live128-scoped-original-full112-FD-fullDN-request.json |
| 真实调用与单必要对象报告 | visible-larger-public-live128-scoped-original-fullDN.yml |

原219 request/workflow/16源历史不修改。旧334个 source pin 逐值保留，加入两件新工程源后是336个显式 pin；旧 outer/reader 作为历史来源保留，不作为221的实际调用入口。

## 508.2 原数据身份的唯一校正

同一原输入仍是 historical commit 8bd267107cc8710d371f3b62c02986655ac965b0 下的：

~~~text
topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json
Git blob: 4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3
bytes: 109004
SHA256: 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6
~~~

完整64字符值来自原204和原208的 frozen_geometry_inputs.files；219误写成63字符，遗漏 eda 后面的 e。新请求只更正该字面身份。原 exact_git_input 的历史 commit/path/blob 检查、原 git show 取字节、长度与 SHA 检查以及新建写入方式保留。没有放宽输入检查、重算 ready、重新选 root、改动原数据或以旧 SHA 恢复不存在的内容。

accepted、actual63 warm/status、original112 config、stored-ready、public78 source restoration、actual91完整 artifact 与 seed 的实际准备顺序不变。actual63只是当前 prefix 初猜；actual91只是当前尾场初猜；二者均不移植本次未求的 J、native、原响应缓存或 fullDN 接受。

## 508.3 什么构成本请求的进程归属

新 quiet 保留原1516306f来源的登记合同。登记包含实际 run、原 process source、namespace、pid、start_ticks、uid、pgid、sid。这里 pid/start_ticks 是一对身份；数字 pid 相同不够。

令一次观察中的已登记身份集为
$R=\{(p,s_p,g_p,\sigma_p,u_p,N_p)\}$，
分别表示实际 pid、起始时钟 tick、进程组、session、uid 和 namespace。观察的权限范围由以下真实证据形成：

1. 同一 run 的原登记 pid/start_ticks；
2. 与已登记 pgid 或 sid 的关系，仍须后续核完整身份；
3. /proc 同次 stat 观察可追溯的真实父子链，且父起始 tick 不晚于子；
4. 已经观察到的同一 namespace/owned 身份；
5. 可读命令参数中等于本 namespace 或其子路径的明确路径；
6. 可读 R493_OWNED_NAMESPACE 环境值等于本 namespace 或其子路径。

第5类是可疑归属证据，不单凭命令文本给予发信号权限。第6类亦不能替代登记、组/session和 start-time 的完整信号绑定。原始 environ 或任意其它环境变量不输出；仅保匹配与权限错误的必要元数据。

先取得 stat 身份图，后筛归属，避免一个真正后代或登记组成员改变 uid 后被初步“同 uid”过滤悄悄排除。若所属候选的实际 uid 与登记不同，它仍是未知并阻止读删。原程序不因此被授权改变 uid。

### 508.3.1 权限错误的两种不同结果

如果某进程已有上述真实或可疑归属证据，读取其 cmdline/environ、stat 或身份复核失败，仍返回 unknown。真实 owned 或可疑 owned 不可读时，禁止把 quiet 写成 true，禁止读取科学文件并禁止删除 namespace。

如果某外部同 uid 进程既没有登记组/session、实际后代和先前 owned 身份，也没有可读 namespace 证据，则仅 environ 不可读不构成所有权。该错误记录在 outside_scope_unreadable，注明没有宣称 owned、没有发信号，也没有声称全 runner 同 uid 进程均可读。此分类不是普遍忽略 PermissionError：同一个错误一旦发生在归属候选上，仍进入 unknown。

这给出的结论只覆盖本请求的实际所有权范围。它不宣称有权终止、读取或证明整个 runner 上所有同 uid 进程的状态，也不从缺少权限推出某个外部进程绝不可能运行。

### 508.3.2 pid 复用和观察变化

真实祖先链只以存活的准确登记 pid/start_ticks 或以前同起始 tick 的身份为锚。仅复用数字 pid 不建立祖先锚。对每个 owned/可疑 owned 候选，读取必要元数据后再次读 stat；pid、ppid、pgid、sid、start_ticks、uid 任一变化，返回 identity-changed-during-observation 未知。

登记 pid 的 start_ticks 不同也返回原身份不符。没有通过“现在同名进程”替代已登记进程。僵尸只按其明确 state=Z 记录为 zombie_nonwriting，不把它当仍在执行写入的进程；这不授予其它未知进程静止状态。

## 508.4 停止与最后静止条件

新 outer 不再调用旧 outer 的全 uid environ 判据。原登记 producer 1516306f 不变，新 outer 消费它的真实记录，实际观察、停止并保留结果。

registry 固定来自本请求原 rules-process、science-process 和真实 live128 worker-process 路径。每件先核 namespace 内路径、原 schema/source、同 run 和完整登记字段。出错不构造一个合格登记，也不清理。

停止次序维持原 launcher/science 在先，随后重新读取实际 registry 集，包含此时已经出现的独立 Node session。原每组 SIGTERM 后15秒、必要时 SIGKILL 后15秒的上限保留。发信号前必须再次实际观察；任一未知归属或无效登记阻止信号。一个可疑 namespace 进程若不属于已登记的原 session，只记录尚未付清的范围，不凭字符串匹配直接 kill。

对一个允许发信号的非僵尸成员，必须同时有：

- 实际 pgid/sid 等于同一个登记；
- 实际 uid 相同，start_ticks 不早于登记；
- 若它就是原 leader，start_ticks 必须准确相同；
- 可读 namespace 环境准确等于该登记 namespace；
- 观察期间身份不变。

终止对象因此只可能是原实际登记组；不是外部所有同 uid 进程，也不是未登记的“看起来相关”进程。

最终重新读取 registry 和 scoped observation。只有没有剩余执行者、没有 unknown，并且各已处理登记组的实际结尾均静止，才返回 quiescent=true。此前的信号尝试本身不证明静止。源中保留 actual groups、original workers、信号、前后观察、真实权限错误以及外部权限范围，失败或未完成均如实返回。

这是对本次真实源合同、继承 namespace/session 的实际进程及观察时刻的条件结论，不是任意敌对进程或无限未来的系统定理。新源没有降低原真实 owned 不可读时的禁止读删条件。

## 508.5 必要 reader 与 cleanup 的行为

reader 的数学/结果选择器逐字来自原a585f94b；只改新 runtime basename/SHA、request221、明确 R508 schema/namespace 和 report frame。原所有实际调用、iteration/trial、方向/未访范围、原 FD 方向层、338/112/means、fullDN 域与错误、原 stderr 和 raw receipt 的选择规则保留。

实际调用次序仍是：

1. 校验 request/source/run/ownership；
2. 调用新 scoped quiet；
3. quiet 未证明时，返回必要对象的完整失败和 unknown，scientific_files_read_after_unproved_quiet=false；
4. quiet 证明后，才读取原 preparation/execution/call/FD/fullDN/rules 及错误；
5. 输出一个至多90000 B的 ASCII JSON，包含末尾 LF。

大小超过90000 B时仍保原70及本地原完整对象身份；不能切包、编码大树、截断为成功或把传输失败改成数学失败。不存在“新工程修复保证全部调用摘要一定够小”的承诺。

cleanup 继续要求同 request/run/source 的完整必要摘要、原 ownership，且再次实际 quiet。必要读回可以完整描述科学失败；因此清理不要求科学成功，但始终要求原错误/未决已如实返回且进程静止。真正删除只针对本次 RUNNER_TEMP 独占 namespace。

workflow 在 necessary_complete!=true 时，改用一个明确单行 Python -c 命令返回 removed=false。它没有嵌套 heredoc，因而不存在219的结束标记缩进问题。输出属于未来实际执行；发布源码不提前宣称清理已经发生。其它错误分支仍如实保留原退出码。

## 508.6 原数学和资源不变量

14件原科学/协议源保持原 SHA；新的两个工程源没有进入其数值正文。固定内容包括：

| 原责任 | 221的合同 |
|---|---|
| 当前完整 H、原 noJ primal、实际选中有限 root trace | 原样 |
| 当前完整 J / R273 / 576 stage / 224方向 | 原样 |
| 226局部状态及两个 mean | 原样 |
| 577节点的224状态资料 | 原样，不与226局部布局混用 |
| 完整112 boundary、合法混合338×112 response | 原样 |
| 持续128状态、原32×10、tolerance2e-9、独立 replay | 原样 |
| 同 call scalar13/audit9、实际投影字值 | 原样 |
| 原全部 FD group/方向/层/适用收缩判据、5e-5阈值 | 原样 |
| 原 prefix17 trial、RMS1e-6、boundary1e-11与最终 fresh audit | 原样 |
| 8次outer、Jacobian workers2、max_nodes1200、材料/物理4096 | 原样 |

原 clock schema R493-original-full112-live128-job-deadline-v1 保持：输入恢复之后、第一次 rule sync 和 native factory之前建立一次19200秒科学钟。每个新 H 的调用只裁剩余时间，不重启时钟。job350分钟、science step320分钟、readback/cleanup reserve120秒仍原值。原 owner/stage/boundary/endpoint/audit各cap、2 GiB因子限制和盘空间参数均相同。

新静止条件是读删的工程权限条件，不是新增 native、FD 或 fullDN 的数值接受门。没有由实际219未启动的范围推出任何数值结果，没有把历史 actual91尾初猜冒作 actual63 prefix，也没有套用连续 C /18900秒另一条链。

## 508.7 来源及执行边界

四个实际运行入口身份为：

| 文件角色 | bytes | SHA256 |
|---|---:|---|
| 新 outer | 38924 | 6f211144ec8411f60981d699841e18c75d7f3f8000ee8ba8fe5d500322ad8dde |
| 新 necessary reader | 35283 | 687168ef5ec3414c79667deda4df40c233e60265c1b12605c40a891964f709a7 |
| 新 request | 54884 | 0fa9fe29153913252fd569cb2b99711c85b0afe72d8bc576adf629bd3e3f789e |
| 新 workflow | 13301 | 83849e83d91baffa78ee2cde101a11e8474ce808d191f9dc44cf8c321ebd90ef |

发布只说明该独立完整调用链已具备可复核源码。workflow保 push和workflow_dispatch；实际由主控真实 pull/rebase/push后使用官方同仓库 dispatch，并另记真实 head/run/job。R509预留给未来 actual221，尚无本次新数值、运行完成或接受声明。

具体CLI、source闭包、输出和错误分责见 [request221接口](../notes/2026-11-16-request221-live128-scoped-original-full112-interface.md)。完整差异只作文本交接，不作为额外运行或审核门。
