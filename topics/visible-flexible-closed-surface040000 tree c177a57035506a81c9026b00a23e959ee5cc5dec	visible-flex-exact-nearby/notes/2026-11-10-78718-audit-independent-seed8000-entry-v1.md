# independent-seed8000 原公开 M14 入口：完整独立启动审查

2026-11-10；审者 /root/independent_audit；会话 Astra-visible-flex-78718bd0。

## 1. 结论与执行状态

**冻结 independent-seed8000 v1 入口通过完整源码、输入身份、原数学保持、真实出口及资源接线审查。** 可以按 root 的后续明确排程，由指定独立执行者实际启动这份已冻命令。该结论是启动入口通过，不是数值成功、最终独跑完成或 README 完成。

本文完成时，本审者没有启动这次主 solver，没有创建候选、调用 RHS/BVP/DN，没有选择初猜/节点预算/优化参数，没有写正向独立工具观察。只实际执行来源/输入闭包检查、十函数小运行时检查和负出口/记录器检查。所有这些实际范围和回执列于第 9 节。

这是作者预先选定的另名路线：从已发表真 M14/N512 seed 与它自己的 tail_0002，按同 g/M14/N512/W14 和原 tol/BC，以 max_nodes8000 重新求完整 nonlinear-DN 联解。它不是 root 当前“失败 run02 CP→restart8000”的仅 I/O 重放。真实数值结果未知，可能产生不同的同 g 有限图；需要对自己的图完整认证，不能借用 root 图证书。

前置完整审查为 [restart8000 全文审稿](2026-11-10-78718-audit-restart8000-entry.md)。本次两件 canonical 实现字节未变，其前置全字段语义审查和实际检查保留；本次全文检查全部八件新源及七对完整差异，不以来源改名摘要代替程序审查。

## 2. 全文阅读与逐字派生证据

实际全文读取：八件新源，包括输入、准备器、driver、auditor、小 runtime checker、guard preparer、独立 actor recorder 和生成器；两件 canonical 源复核原实物 SHA，没有当作新实现重审；15,754 B 的完整设计、8,091 B 冻结清单、4,383 B 生成账本及 **46,451 B 全 unified diff**。各分段输出均完整；未把大 launch 或 runtime JSON 的内部 code/数组字段输出到对话。

本人真实 **89dbf4，exit 0** 做了以下检查：

- 冻结清单中的全部 22 项源码、文档、报告及已准备元数据均逐文件按 path/bytes/SHA 核对。
- 七件旧源保持指定 SHA；以已全文读的 stdlib-only builder.derive 在内存重新派生七件新输出，逐字等于实物，source compile 成功；未调用 builder.main 或写任何源。
- 独立直接从七对实际旧/新文件用 difflib 重建整个 46,451 B diff，逐字等于冻结 diff。此核对不依赖作者声称“差异只有这些”。
- 独立重新作完整函数 AST 比较，只规范四种已逐字读过的文件名/status/exit-scope 字符串。driver 的全部 15 个顶层函数均相同；auditor 的 10 个函数相同，只有 final_audit 增加固定 actor 与真实完成返回约束。main 内的 selected 包装整体包含在比较中。
- 真正调用新输入门 validate 对预先冻结主 launch 检查全部165项输入；逐件重算 guard 的167项绑定，核同一数学 command、固定 executor 和 recorder 来源。

证据 [source/input 独立检查](2026-11-10-78718-audit-independent-seed8000-source-inputs-01.json)，5,820 B，SHA256 **bbca94a7701725d8480867317d14875e08d82c64e0a9b50d5419c6c79b32911f**。这是 source/input 执行，不是求解，不调用候选初始化或 CSC factory。

源码变换的每一类已对正文核语义。生成器的 rename_references 限于另名入口文件和 importlib alias；原 solver 模块名未替换。失败输入函数明确被公开 seed 校验函数替代，旧 failed-CP 入口自身保持冻结。生成器在写前检查全部输出冲突并在结束重新核原源字节，没有覆盖不同内容旧源。本文不把 AST 的“相同”数量单独当作改变输入函数或新观察门正确性的证明。

## 3. 原始来源、seed 和全部数据闭包

### 3.1 三层原来源仍按原门实际校验

ancestor_context 首先钉旧真实 direct-CSC run02 launch（b935a586…），从其 bindings 唯一找到并核原 entry 源，再真正运行它原来的 validate_inputs。原97项 reference、141项 launch、W14、固定物理定义与全部已审 prerequisite 因而都由原入口自己付清。ancestor.settings 必须精确等于本次 settings 仅将 max_nodes 改回6500。

随后 published_seed_inputs 钉公开 prefix 与配对末尾：

| 输入 | SHA256 |
| --- | --- |
| 原公开 M14 prefix | 3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0 |
| 该 seed 自己的 tail_0002 | 009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762 |
| 原97项 reference launch | e45c553ea6832525c6a2719a197dbcc49a7ee5dd77badfb4b363e19a4b974a83 |
| 原141项 source launch | b935a5863a88e6c4541357a558c6b3874ed3ba89174b65032b0494425681c671 |
| 原152项 runtime source guard | c5a9bb2d5bba1099db7b489d52b423b0fff135be339a8ea435989f235d3b8063 |

公开 CP/末包必须与原141 launch 原本声明的 source_checkpoint/own_actual_tail_warm 精确相同。这不是仅凭文件名寻找一个方便 seed。

152项旧 guard 在这里用作已冻结的启动前代码/运行时来源集合：它的 command 必须等于原141 command，全部文件实物逐一 verify、禁止重复路径，并逐项包含原141闭包。它没有在此用作任何自然退出证据。该旧主计算后来失败不会使原启动前源码和公开 seed 变成新的失败输出。

### 3.2 公开 seed 的实际范围

公开 CP 必须是已审2633节点、有限 solver_success=true；tail_seam.tail_record 必须是配对0002。原 auditor.check_packet 实际读取它自己的 warm，核完整原17 jet、616 Jacobian、八 audit、参数/八源、有限865×28状态及raw布局、真实 residual门等。所有 PP chunk 的实物大小/SHA 再核且必须在原152闭包中。

这里使用已审公开有限解作为输入，不声称其旧整图已达最终 G5，也不重新求它。完整97来源和 CP/PP/末尾共同构成输入，不能只凭一个CP头。原 source ancestor 的结局仍按原失败保存；当前入口没有把它改为成功。

新165闭包中的四个被排除旧失败对象也实际检查过：不含失败 CP b04af907…、失败0003 b26fff3d…、旧失败观察 c32d439b…、6599诊断 fb758032…。不是只有顶层 failed_CP_warm_input_used=false 而实物仍暗含旧失败输入。

## 4. 本次实际改变的数值政策和 I/O

新 settings 明确为 M14、angular512、audit1024、nodes1601、max_nodes8000、tol2e−9、bc_tol1e−8、physical_bc_tol2e−11、Node heap1536。与原141 source ancestor 唯一数值差异是 max_nodes6500→8000；这个预算由作者/root 预先指定，本审者没有选择它或把另一条失败初猜的6599诊断挪给公开 seed。

expected_argv 从原 delegated_parser_argv 复制，仅允许明确更新 tail-config、out-prefix、restart 和 max-nodes 四个选项，每个选项要求恰好一次。实际165主 launch 与原141相比，**只发生三个 argv 值变化：tail-config、out-prefix、max-nodes**；restart 的真实值原本就是同一个公开 seed，故实际不变。

expected_config 复制原真实 config，initialCheckpoint 指向同一个公开0002，trace 与存在的 iteration/trial I/O 改到新命名空间；去除 I/O 后必须与原物理/离散config完全相同。实际主 config 相对原 config 只有 iterationCheckpointFile 和 traceFile 两项变化；initialCheckpoint 未改。fixed、lagged-tail、preserve-restart-mesh、显式空 warmup 和所有其它 parser 值都保留。

nodes1601 是原命令选项，并没有覆盖 preserve-restart-mesh 保留的2633节点；实际重启或以后适配的节点数仍由真正原算法产生，并受 max8000/原门约束。本审不预言这条新路线的初始增点数或收敛。

所有 launch 的 frozen_physical_fields、source_root、weights、callbacks、newton_lifetime_definitions、csc_selection_definitions/prerequisites 都逐字段等于原 source ancestor。新 launch 必须明确 executor=/root/independent_audit、固定 recorder，禁止失败输入那四个旧顶层字段，并明确本路线不是 failed-CP restart exact replay。

## 5. 准备层和主计算保持原数学

### 5.1 纯准备和资源文件

preparer 先做原来源、公开seed与共用代码前提，再要求完全未使用的 independent-命名空间。它只构造新config字节、launch和preparation，在实际写之前以 planned_config 调用完整 validate。预计config的字节/SHA也核，且拒已有config；所有其它绑定仍读实物。实际作者 d45c80 的完整三文件准备为165绑定，c0b05b的guard为167绑定；本审逐字读代码及逐文件重核这些已写对象，未把它们称为本人新执行的数值过程。

本次本人没有为了重复已充分验证的 metadata writer 再创建另一套纯prepare输出；本人实际调用的是完整新输入门对将来主launch的165项校验及guard167逐件hash。已作者真实执行的准备与本人实际输入验证范围分别记账。

guard preparer 保留原资源 wrapper SHA8260d9…和原 disk guard SHAcf1e23…，直接使用同一 launch.command；新字段是 executor_start_command、固定executor和recorder身份。政策仍为每进程 RLIMIT_DATA 6GiB、Node heap1536MiB、磁盘512/768MiB暂停恢复阈值。它不保证所有进程总内存，也不是数学成功门。

### 5.2 真正 driver 没有变成零更新验算

driver.main 仍载入原 db6f-prefix-flat-coupled 原 main/outer算法并核其 callback 身份；构造原 W14 坐标 solver；只把原 solve_bvp 挂到已审 selected 包装。main 真实执行 runner.main，不能靠读 CP 或复制记录完成。公开 seed 是原初猜，不是本次未产生的最终CP。

selected 仍要求原 tol/bc_tol/max_nodes 和完整kwargs集合、同一物理callback owner、固定M14/N512、fun/bc/jac、physical flow、chart、seam、save_checkpoint等来源；每次真实 BVP 前后都检查 Newton和CSC。首个真实DN关闭后才写 first-request-binding，且准确保持“一次DN，outer仍未完成”的范围。原所有外层重求、真 DN/J、BC、物理 PPoly保存、seam最终audited packet均继续由原程序执行。

source-only比较的15个driver函数在仅规范名字/status/退出说明后全AST相同，正文也逐段确认原 runner.main、math kernels、原十函数typed检查/闭包/alias约束均未删改。成功仍要求原 check_outputs 真正通过；捕获异常、恢复失败或未闭状态都保留失败/中断请求exit。程序自行请求的exit不替代工具观察。

## 6. 完整 runtime 与全部物理关闭门

canonical core/checker 两件保持797eb77…/f869c3…原字节。共同 canonical 小前提可以复用 root 当时真实检查及冻结观察；这是通用代码身份，不是本次独立主计算出口。其环境、24拒绝、6float位例、四个实际SciPy live/source、全部公共CodeType数据字段及源/report观察闭包，仍由 code_evidence 真正核验。本审过去对这套原canonical已经完整独审与实跑，本次没有冒称重新做24例。

每次 BVP 的 complete typed envelope 仍恰含十函数：四个SciPy、三个foundation、两个 selected closures和一个 selected Newton。raw记录保留，原factory provenance、defaults/closures、来源归一比较、原STATS alias、只换prepare属性、原exported函数保留、无旧global-COO闭包均保留。restoration同时核原raw与typed before/after。

新auditor的 check_packet、polynomial_endpoint、check_runtime_records、check_outputs 等十函数经声明字符串规范后与旧版相同；本次也全文读了其实际实现。以下门仍全在：

- 完整CP/summary一致，原固定物理定义与config不变，实际有限M14自由参数、原RMS门、真实outer inner success/BC/tail residual及编号完整。
- 所有PP chunk逐字hash/大小、全数组有限性、quintic形状、状态43槽完整分区、全物理mesh正跨度及max8000；以已保存物理PPoly算最终cut height，没有新ODE调用。
- 本次outer真response与记录残差一致；随后必须另有更晚的最后 Jac+audit 请求。最后tail文件名从本次tail_calls定义，实际request height等于保存PPoly端点，并有17jet/616Jacobian/8audit、完整有限raw状态与配置。
- 完整seam标量、原896 seam angular、源tail输出身份、prefix audit1024等有限诊断；首DN、全部运行时calls、成功加权/物理坐标回转、PP axis、原inner残差门相互对应。
- reproduction的运行状态、源/argv/定义、actual BVP记录、before/after/restoration以及closed_output_checks必须和独立重读输出完全一致。

没有以首DN、CP.solver_success单字段或guard子进程状态支付上述关闭门。它们仍是原有限求解门，不是continuous XYZ/metric/reach证书。

## 7. 指定 actor 与真实自然工具出口

新 final_audit 对原完整关闭流程只增加明确独立身份要求：observer字面固定为 /root/independent_audit、同stem、正整数session id、非空字符串receipt、actual_exit_code为整数0；recorder_source必须与launch绑定的实际新recorder全等。

tool_return_metadata必须为dict，含整数exit_code，与顶层出口相等；chunk_id与顶层tool_receipt相等；不再带活动session id。之后才进行原reproduction/完整输出复核。最终observation.files每一行实物hash都重核、路径禁止重复，而且必须覆盖CP、summary、全部PP、first、outer、最后audit及launch/reproduction。

新recorder全文已核。它不读取guard来推断自然出口：

- start要求实际返回含整数session_id、没有exit_code，且匹配实际传入session，保留chunk；
- complete要求实际返回整数exit_code、非空chunk_id，且session_id为空；
- unavailable要求tool_error字符串、不能有exit_code；单独文件名记录未知出口；
- actor固定写成独立者，保存工具返回除output以外的原metadata与recorder实物身份；complete对同stem已关闭文件逐件hash，写前和exclusive create均拒覆盖。

记录器不会密码学验证调用者是谁，因此执行纪律仍是指定执行者必须把自己真正收到的工具返回传入。不能借root回执改actor，也不能用guard child exit生成一个工具返回。时间戳注明是记录时刻，不是假精确进程结束时刻。

完整设计要求单个持续orchestration cell持有实际exec会话，连续write_stdin取得真实返回；如果句柄不可用就保存unavailable，不能从mtime或/proc缺进程推断自然成功/失败。本审认可这个证据范围，但不宣称持续cell能根治执行器失效。

## 8. 独立路线与后链范围

原独跑协议允许已有已审warm/较粗解作为真实前置，不要求重搜所有失败或重做每段continuation；对一条精确冻结命令的replay则要求原seed/参数不变。当前作者明确冻结的是旧公开M14直接seed8000的新路线；审者不偷偷改变root failed-CP command或称两者逐字相同。

将来此计算若真得到不同的数学payload，按原协议需对本图独立重导出、完整认证、比较并明确最终交付对象，不能改系数凑hash。实际全链还包括自己的tail/prefix/target/bridge/common-cut、两侧连续界、closed-budget/whole/正常2e−9 terminal及网格。这些在本入口没有执行或预支。

已审 78718-plan-post-restart8000-v1.py 固定root的另一个schema/actor，不能直接消费新independent final。设计已经明确必须另名、另审success-only接线或按冻结原全链显式执行；不能静默改旧计划器。新无损存储家族同样保持已审新source身份，按实际需求接入，不改本次求解方程。

## 9. 本人实际执行及全部小证据

| 真实工具 | 真实退出 | 实际范围 |
| --- | ---: | --- |
| 89dbf4 | 0 | 全部22冻结对象、7源派生/全diff/AST，真正新input.validate165，逐件guard167，0 factory/solver。 |
| cadede | 0 | 冻结runtime checker：10个actual live函数、10个typed摘要改变拒绝、原before/after/restoration，1个无矩阵CSC函数factory，0 RHS/Newton/BVP/DN。 |
| 048223 | 2 | 使用真实新主launch，缺独立工具出口；完整final正确拒绝。 |
| f44627 | 2 | 新主launch配旧run02 root真实观察；固定独立actor/运行身份正确拒绝。 |
| 5e082f | 0 | recorder负测试外层检查通过；对真实旧guard完成元数据调用recorder的子程序实际exit1，拒缺自然工具出口/receipt，零观察文件。 |
| 51c38a | 0 | 比较本人runtime与作者报告，仅seconds不同；实核主165闭包没有四个失败输入SHA；打印自有小证据身份。 |

本人runtime报告为98,368 B，SHA256 **82c5bc8b57c1b1ec49d291195682b732e0446160eb9bd0f736672d49ca240a78**；没有把作者289aed回执算为本人执行。它的source、实际十函数字段、十拒绝名单及恢复结果都与作者报告相同，只有时长不同。

两负final文件分别577 B/SHA00514b5a8ecf407cbfaa31da3cdd18b66398d36233a823e24a0bb8f764b14388和547 B/SHA8723a327fbfec467304d791a51218b4310a14a8ac0998bad25e2e0cdbe6c395f。其字节虽与作者同类负例相同，真实执行回执各自保留。

本人recorder负例仅使用真实已存在guard元数据，不伪造一个完成或running工具结果，不编造session id。子程序实际错误为 Natural tool exit code and receipt are required，输出stem下无任何观察文件。小报告1,079 B/SHA39f30f3e32ecdb44429be1abecfe2c221ffbb9bdbd1bfbd3a2f978ac498e21bc。作者另有真实running返回负例的历史记录，本审只读其来源，不冒称亲手取得那个旧工具返回。

所有本人报告为：

- [完整来源/输入检查](2026-11-10-78718-audit-independent-seed8000-source-inputs-01.json)
- [实际十函数runtime检查](2026-11-10-78718-audit-independent-seed8000-runtime-01.json)
- [缺独立出口负门](2026-11-10-78718-audit-independent-seed8000-missing-exit-01.json)
- [错观察者负门](2026-11-10-78718-audit-independent-seed8000-wrong-observer-01.json)
- [真实guard元数据拒绝](2026-11-10-78718-audit-independent-seed8000-recorder-rejection-01.json)

这已经覆盖本次新来源、输入路线、actor/出口变化的具体风险；没有因可用测试而再重做未改变的canonical/所有旧数学测试，也没有把小factory当成真实候选求解。

## 10. 冻结的新源与主准备身份

| 新源 | B | SHA256 |
| --- | ---: | --- |
| 78718-build-independent-seed8000-entry-v1.py | 27706 | 0bf553b59da21e48676dceae8046c062160210bbec059c6530ddb75ffd943b43 |
| 78718-prefix-independent-seed8000-inputs-v1.py | 16312 | 3508c37cb4d9ff48702143b00fa668b6938b40e1e85e97d6ac0ae74cc55397be |
| 78718-prefix-prepare-independent-seed8000-v1.py | 6324 | f06e3c4a4fc9dfdfea73ace6eceb7658493106ede5dfac88947f51ae722c31df |
| 78718-prefix-spectral-independent-seed8000-v1.py | 18858 | 2fec0b89aab9611677fef9c2eab70b78d9eef8e22b85dfcd5b46753e2d4517b5 |
| 78718-prefix-audit-independent-seed8000-v1.py | 32581 | 067f8944cb0d75ceffc846119b1ca2511f0e6e886799258e4659b023d8828578 |
| 78718-check-independent-seed8000-runtime-v1.py | 5014 | c9a9adfc03688740ee258fff6895d4b0a62aa25832a9ab133dd5b75c8aba3f52 |
| 78718-prepare-independent-seed8000-guard-v1.py | 2880 | f40f1157153a608c3744e772fffc5f8097195c25d2000c20ea9f7c7e7f8b9e4d |
| 78718-record-independent-tool-observation-v1.py | 3825 | 65daca0b3bc7b8512bab1fff4edf672c2d158a0b21198b2d0f5a23815a7f0a6b |

主输出stem为2026-11-10-78718-independent-m14-seed8000-01，当前只有已准备用的metadata身份：

| 文件 | B | SHA256 |
| --- | ---: | --- |
| tail-config | 2682 | 9b6540d8769c60873ab7e61892beed116bd45bb01b10fe0a34f99c92b402992e |
| launch | 100701 | a00359ad76c53e92890f5cd098878929838b6505923deaef92d5603bec421019 |
| preparation | 6749 | 846d3f2e8fb85b595d1a93460348714043af1a58f0f43ac14df102645faab3e5 |
| guard-launch | 49374 | 5dad81b17ce9e382933f10bf4e52c0c4cd6fee6bb86c8e54c93e4cc839a26e4b |

设计稿SHA9604311aed03c5f4b5cbd840df7db77180c50ee9628f7b1d1d076b9377699013；总冻结清单SHAe9ef5c9ecddc006e394fcc723e12bffac0ace3c6d0e9b10550b352d3a85d2125；完整diff SHA7746ccfbb3ffeb30ab1bce533155c7fcf16f5ca2f8b444a390369648e4a79a93；派生账本SHAcf8fac0eff1898278a610cec059ae93fc2ff90fc671f3ea359d4a4a3bd5fdf9f。

八件新源逐字冻结；两件canonical、七件原对照源、数学kernels、root recorder与root主运行入口没有被本审改动。本文不修改HANDOFF/open/results/git。主启动动作仍等root读完整审稿后的排程，由唯一指定执行者亲自运行实际命令并保留工具返回。
