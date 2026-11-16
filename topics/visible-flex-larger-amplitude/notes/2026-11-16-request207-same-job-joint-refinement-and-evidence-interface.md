# Request207 / R458：同现场完整原205、五因子精化、M128 与固定目标误差读回接口

作者：ChatGPT /root/exact_refinement（AI）。日期：2026-11-16。  
状态：**独立源码与已发表合同的实际接线；尚未执行 request207。** 全部科学只在公开 GitHub Actions。主控唯一 Git 发布者。R458 条件证明由主控单独发表；本件是完整执行入口的参数、来源和生命周期接口，不用源码存在代替数值完成。

## 1. 正式文件与逐字基线

新运行源位于 `topics/visible-flex-larger-amplitude/computations/`：

| 文件 | 字节 | SHA256 |
|---|---:|---|
| geometry_20261116_request207_owned_roles.py | 17026 | 304eaa41b3b9c0e1eab4e71678720f336cbd1a5e7f47ceb9ef1b6e8d2b0ddc5f |
| geometry_20261116_request207_joint_refinement.py | 44927 | 76881ec3ad75c7d33ef2ea70cafbf12cf73dcb9273f137187f73a975368f4ea8 |
| root_20261116_request207_refinement_necessary.py | 33942 | 7902848f2aac3abb880ae604aa81f7f87bdd68b7b25f6a39dd0ffa92152dde24 |

新入口：

| 位置 | 字节 | SHA256 |
|---|---:|---|
| notes/current-C-actual202-joint-refinement207-request.json | 21956 | c798f376a63d552c12ff56b51fba8f11ed46bba4d858ec95df2838cfe3575015 |
| .github/workflows/visible-current-C-actual202-joint-refinement207.yml | 98422 | 37f426a26c97f637fae74cdcf185fb3ef5fc5025114a7b852613f9417673627e |

工作流基线为正式 request205 的 `visible-current-C-actual202-accurate-ten-closed-geometry205.yml`，95760 B / `726d97e1aada5d34ddfa949753ce59c6909122d3de8c39bd5a2160fdb8712c36`。原子子请求为正式 `notes/current-C-actual202-accurate-ten-closed-geometry205-request.json`，97406 B / `06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4`。不使用目录中的早期205草稿。

原子请求保持全部154 source pins；新外请求另列75 source pins，总229项，逐项不覆盖旧键的值。来源包括已发表 R441、R442、R448、R451、R456、R457、R459 及本件三个源。新请求自身为小普通 JSON，不把原97406 B对象换编码或拆包嵌入。它引用原对象的实际路径、字节数与SHA。原子请求在新作业内仍叫205，外层真实实验号为207；实际 `GITHUB_RUN_ID/GITHUB_SHA` 一律来自新作业，不能冒充旧205运行。

来源提交：R441 `f2c5653000abedf08622e5e703dffd314aac662a`；R442 `22a454e3a4705fef552a1938beef655a8bd1ac53`；R448 `4af72dc1cc28c5eb6485ac8f829b544630db3b31`；R451 `7a1a30ef879197237e063dae5380b047ba4de957`；R456 `49feeaf392e6c992ae91879c36423e24c652369e`；R457 `5064208b7a5c46d7b18c55f86c097a81192ba931`；R459 `1f8213c7bd64ed064f959eca10c0ab5d4c973a0c`。

## 2. 真正执行的有限顺序

工作流先逐字执行原205的完整来源恢复、准确C、cut、factory、完整112深尾、joint far采样、完整453→450、原FD/fullDN/final、首闭面R452五消费者及原独立held。原205的所有工作参数、理论目标、物理方程、试步与科学判据不改。它选择的参数来自该原请求明确绑定的 actual202 binary64投影有理词，不继承旧有限Gauss的J、状态接受或连续C域结论。

原必要读回后，清理前，新增实际调用：

1. 保存真实初始450 checkpoint作为 level0。若实际首共享场、首材料B均已返回，执行一次 R459 measurement；缺失时只记录本测量未付。
2. 以这个真实完整接受的450为父，执行 R456。五个因子 `radial_mesh / field_and_native_angles / native_steps / material_angles / physical_angles` 全部为2。原完整112 far族可按R456合同复用，实际新节点及新角/步数采样、完整H/J/FD/450/final全部重求。
3. R456真正返回自己的新接受checkpoint，才以它为父执行 R457 的 M128。四个角/步数因子全为1，意为保持父场真实已加密的计数；不是回旧2048/12。完整128 deep/far、新native及完整M维数BVP全部实际求解。旧高模零填充仅初猜，不能当新响应。
4. 每个新接受checkpoint分别执行自己的 radial replay、原cuff atlas、shared field、同C live-query metric、完整block reach；再独立执行本场的witness解析和held/rigidity。没有用旧场几何证书替新场。
5. 对实际可用的 level0、level1、level2 做R459测量和实际序列比较。只向compare传真的已返回 `result.json`；缺失成员不伪造。

有限计划只有这两个后继级。M128之后再做更高M的径向联合循环未注册，也不将独立分支说成连续求解父链。只要前一真实求解父未接受，后继求解标明未启动；这正是已有消费者的父场合同，不是新增数值门。metric、reach、held或R459 measurement的未付/失败不阻断仍可执行的下一求解。

## 3. 原时钟与实际资源分配

新作业仍360分钟。原namespace精确为 `visible-current-C-actual202-ten450-closed-geometry205`；这是本新job的独占临时目录，名字用于原子合同，不是旧run现场。

原startup记录与原BVP实际deadline均保 `request205-owned-job-science-deadline-v1`：从实际namespace创建时起18900秒science及2700秒读回reserve。原205早期阶段沿原工作流既有计时责任，本件不伪称它们因此获得新的统一硬终止机制。新增角色则全部由同一个原绝对science终点裁剩余量；metadata读回只用原读回终点，不新开时钟。

| 新角色 | 显式最大预算，秒 | 另有限制 |
|---|---:|---|
| R456采样及configure | 900 | 原owner将configure扣同一采样allowance |
| R456完整450 | 7200 | 原owner及外层均裁实际剩余 |
| M128 deep | 300 | 真完整128及适用性范围，未付不补 |
| M128完整far采样 | 12000 | 不是更长job，原linear/point14400/1800按实际available同比裁 |
| M128完整BVP | 7200 | 保完整原阶段/门 |
| 每级radial/cuff/shared/metric/reach | 600/120/300/600/600 | 每子阶段原owned过程，外层再裁 |
| 每级witness / held | 120 / 300 | 独立于metric/reach完成 |
| 每级R459measurement | 300 | 内外同钟，缺B只本角色未付 |
| R459compare | 120 | 原已返回结果的真实元数据/区间比较 |
| 末测量与关闭reserve | 900 | 已在18900内，从普通新science allowance扣除 |
| 每次child关闭reserve | 30 | 不超过实际原终点；外部中断时限更短 |

各上限不能相加解释为额外运行时长。M采样采用12000的上限，是避免主动设定一个已低于实际197局部完整far耗时的过短上限；没有据此预测M128能完成，也没有假定新M速度。所有现有C、首次BVP、首次闭面、安装、来源读取和规则同步都已经消费同一namespace时间。实际只可能完成0、1或2个新级；每个未起角色及原因完整记录。

`max_nodes=2400` 是显式资源容量。实际完整父节点、插值种子和全部knots的并集由原科学driver形成；没有写死实际节点数，没有截断种子，没有补伪节点。容量不足按原资源partial处理。新角色启动最低8GiB、资源停止线2GiB；原205最初32GiB等原条件不改。全部原大阵列/账本留RUNNER_TEMP。

## 4. 新运行源入口与真实所有权

`geometry_20261116_request207_joint_refinement.py` 的操作：

- `rules --request ... --request-sha256 ... --base ... --computations ... --source-topic ... --proof-directory ...`：实际加载原 `root_20261114_current576_rules_runner.py`，SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde`。把原已读两README字节显式回填其baseline，保45分钟真实pull/rebase/规则变化终止语义。规则输出在独立 `refinement207-rules`，避免原205 `*rule-sync*` selector重复收取。
- `run`：必须是原rules runner真正创建的独占PID=PGID=SID；实际记录run-owner，再执行十二个有名角色。
- `witness --input ... --input-sha256 ... --computations ...`：在Actions中加载实际R441或R451准确cut/atlas源，从当前新field真正解析唯一左端0的正prefix piece，再形成原四物理方位点；不复用旧field的piece index。

工作流外层 `timeout` 依据原startup science绝对终点给rules调用实际剩余上限并保关闭20秒；它是原命令的资源终止，不是科学通过门。内部run又以原BVP返回的实际deadline与原recipeSHA绑定。规则父startup、return、science-run身份分列。新入口stdout/stderr完整保临时文件，不用错误哈希代替必要原错误字符串。

`owned_roles` 保实际PID、PPID、PGID、SID、`/proc` start ticks、uid及boot ID。每个新增外层角色单独新session；内层既有owners再创建的子session，经实际祖先观察和同run原owner记录收集。只有匹配实际PID/start-time的已观察进程才接受TERM/KILL；不以namespace字符串给未知进程发送信号。当前可疑或未知进程留为unknown并阻止清理。

所有已观察组停止、实际child返回后，才读取可变raw。原205的固定八role `observe()` 在新run开始先实际查询；它不把207自身冒成旧role。旧scope仍活或未知时，本件记录原scope未静止而不启动下游，不把这称数学拒绝。

内层owner正在写文件时的读失败可暂记retry；最终稳定读仍失败则保unknown。两套新scope停止后再一起观察quiet，避免第一次观察时第二scope尚在退出而留下过期判断。元数据reader也有自己的实际owned子过程；cleanup前再观察三处scope。源码条件是这套可观察所有权协议，不预付某次运行已经静止。

## 5. 两次真正求解输入

R456 owner正式 `1a1df513...`，schema `R456-current-C-frozen450-same-far-resolution-owned-launch-v1`；R457 owner正式 `23a3b218...`，schema `R457-current-C-actual202-capable-frozen-M-owned-launch-v1`。两者CLI都是 `--input JSON --input-sha256 SHA`，输入schema为各自schema加 `-input-v1`。

顶层original accepted/tail_config均来自原origin launch的 `actual_input_files` 真回执；`tail_source_root` 从实际原command唯一 `--tail-source-root` 读取。两者的origin仍是实际 `BVP-launch`；R456 parent是origin，M parent是实际 `refinement207/level1-solve`。

R456的 `original_config` 来自真实父checkpoint的native_configuration member，而非把初始配置按名字替换；`original_sampling_directory` 与其真实geometry result相合。C cover/deep/proof均是同job真实原件。七个采样工作键为precision、budget、free、cache、nodes、inverse-depth、value-bits，保原值，仅budget明确900并裁剩余。

M的三原C输入、R286/R312/R442证明与precision256全部明确给入。父R456的same-far来源仅作为原目标和原坐标provenance；新128深尾/完整far必须重算。M sampler工作参数精确14键，**不传原205的额外 `steps` 键**；R457实际从父 `actual_resolution.native_steps_per_stage` 导出steps，这是其真实API。原13工作量键加representative精度4096保留；linear/point预算根据实际allowance同比裁并把原值与实际值共同记录。没有更改R457的科学函数或把M112边界行补零为M128行。

M driver仍正式 `395da6c8d43c0d31e59c58a2089fb4b116900a9b3192fa8d76456fc680adde12`，checkpoint仍 `18399ec7d7ad44f03d491fdf60a54794decfe8854c8115d7ebd55ed014ed5e93`；没有为来源标签再复制一份driver。

## 6. 同一个完整闭目标与每个新场

本件保同准确C、原root族、准确scalar DAG和全部十有理词。场维数/分辨率变时numeric field metadata与checkpoint身份真实变化；准确目标相同不是这些文件SHA相同。

完整闭面目标还必须保首次construction的W、H、所有marker、材料及尾帽定义，不只是十词。原R452真实procedure中的A提供 `actual_construction`，first shared提供同源完整表达来源；两个新postsolve均显式传真实 `first_parameter_procedure` 回执。各新field的radial/cuff/SE2及共享表达各自重求，不能复制首场几何证书。

原B提供首材料transport、首plan/assembly和原deadline。R459实际调用R457公共材料helper `059d0df3...`，对当前Phi与首Phi形成准确共轭，保whole phase/cap责任。原始B缺失时，R459对应角色明确未付；R456/M求解仍可继续，既有新几何/独立held也不因此新增B通过门。

每个新5-stage producer分别为R456 `4770c16a...`、R457 `a177cd7a...`；各对应reader与held采用同套明确来源tuple。输出当前字段、all-angle、mean、whole-cut、完整cap、反射以及pair责任都沿已刊原消费者。完整场几何未完成时仍保存其原frontier/count/异常；没有让本编排把未付改true。

witness解析仅得到原四物理方位的当前场地址，不能独立支付whole-image held或O(3)刚性；这些仍由原完整R425派生consumer执行。独立held不是metric或reach的后置通过门。

## 7. R459真实测量与t网格

源 `geometry_20261116_fixed_target_complete_metric_evidence.py`，62091 B / `494fea70b97404af2be8ef0f3d685fadc2f59c6a30ea3af771de98a56b868b05`，已刊 `1f8213c7...`。

每一级measure给精确字段 `schema,label,namespace,computations,proof_directory,job_deadline,first_material_transport,first_plan,first_assembly,field,work,c_queries,time_grid,out`。四个首材料/时钟描述以及field的cuff/C描述均是真实文件、字节、SHA；不由旧哈希恢复数据。field.family分别是 `original112 / resolution112 / completeM`，对应真实loader。

work显式保持11键；interval_bits256、sqrt_bits128、initial_angular_depth2、max_depth20、max_cells100000、max_inverse_steps80、max_phase_query_cells100000；宽度工作目标 `1/100000000`，metric reference `1/1000000`，各300s。宽度和reference都不是新BVP接受门，也不把native2e-9、RMS1e-6或BC1e-11硬说成相对metric误差的机器底线。

原c_queries11键完全沿205 work choices。测量的time subdivisions实际为4、8、16，四个共同见证是prefix公共u=1/2、q=0或1/4、上下两side。每个实际k=0..n及全部闭piece membership由R459真实执行；预算时保 `next_unvisited_address`、未界定query和原complete_grid_plan身份。离散t点只给实际加密见证；whole t误差界依赖完整base闭域与准确共轭，不靠有限t采样推断。

compare只消费已返回measure result。严格真实sup下降的区间分离证据、仅上界改善、区间重叠/未付三者分列；原解父相邻关系与最终adaptive mesh逐word嵌套也由真实成员判断。输入种子并集包含不等于solver最终自适应mesh必逐字嵌套。没有把三个source标签当误差下降。

## 8. 必要读回的精确范围

新reader生成**一份**整个新增链的必要摘要，硬上限90000 B。各冻结metadata reader只在Actions内部生成原必要对象；这些中间对象、所有完整result、raw ledger仍临时，不上传、不语义拆包、不编码科学树。

保留：

- 十二角色实际启动/返回/退出、原绝对剩余和实际裁剪、原未访后缀；
- 两次原完整solve必要阶段、FD所选原误差与实际native调用、真实mesh/source/checkpoint及错误；
- 每场五stage原必要结论/待办范围、独立held原必要字段；
- 每measurement的 `actual_job_deadline`、`fixed_closed_target_signature`、实际CP/resolution/mesh、全域opnorm上下界和完整/未付、t query地址、必要coverage、原tolerance证据及 `members`；
- R459 `members.complete_coverage_and_pending` 等原完整账本身份。已退休未付叶的全部正文仍只在Actions，不冒已经从compact scope读回每个节点；
- series完整**原必要对象**，包括 `level_count,actual_common_target,actual_common_original_clock,fixed_closed_target_signature,levels,consecutive_comparisons,all_complete_upper_envelopes_strictly_decrease,all_real_sup_strict_decreases_proved` 与所有原限定字段；
- 原规则真实receipt必要时间/源/returncode/README改变/所有原错误，原stderr完整可逆字符串；相同实际错误字节只展示一次并列全部原路径，不以hash代正文。

R459的early bind异常可以不产result；外层保原exit/stderr、角色未付，不造compare成员。原冻结reader因自己的>90KB输出返回70时，如果其完整必要JSON仍在现场，本新reader可按既定selector读取它，但明确保child70；本链是否完整独立决定，不把child70改成科学成功。没有读取到原字段则不补零/null以伪造范围。

新摘要超过90000 B，存临时attempted对象并只返回小overflow身份和section bytes，退出70、complete/transport=false、不产生清理marker；不拆包、不加大上限。原科学退出、控制性过程结束、单摘要完整、PID静止和整体科学任务完成相互独立。

## 9. 输出目录、marker及清理

原基目录内新增：

| 路径 | 实际用途 |
|---|---|
| refinement207-request.json | 原新外请求完整字节 |
| refinement207-rule-owner/ | rules父启动和实际返回 |
| refinement207-run-owner/ | 实际独占run PID/session/start-time |
| refinement207-rules/ | 原3b8规则元数据 |
| request207-entry.stdout.log / stderr.log | 实际新entry完整原流 |
| refinement207/result.json | 十二角色与原来源的实际编排记录 |
| refinement207/levelN-solve/ | 真R456或M owner及新CP |
| refinement207/levelN-geometry/ | 本场5stage输出 |
| refinement207/levelN-witness/、levelN-held/ | 本场真实witness及独立held |
| refinement207/levelN-measurement/、comparison/ | 原R459结果和必要summary |
| refinement207-readback/ | metadata子读者、单attempted/body、原错误 |
| refinement207-readback-complete.json | 仅实际完整读回且quiet后写 |

原205清理正文被搬为新reader `cleanup` 正常CLI，保原C、cut、construction、far、BVP、rules、closed七个实际outcome/marker和原BVP静止；再加新读回outcome、同run/source的新marker、同一摘要身份以及三处新owner最终quiet。只删除该唯一临时namespace。任何缺件、未知scope、读回失败或溢出都明确skip，raw仅留到runner销毁，不冒可跨run续接。

report job仅复现各原205独立必要scope和新增这一份精确body，核原bytes/SHA；不再取大raw，也不由job颜色推数学完成。

## 10. 与正式205工作流的完整差异

完整 `workflow-relative-to-published205.diff` 随本地交付。变化仅：

1. 新workflow名称、push入口、concurrency与新增外request稀疏路径；
2. 原PYPINS之后追加新外合同/75新增source的正常语法与字节绑定；原154绑定及其原数学参数均不改；
3. 原全部科学步骤、原first-closed及其独立held、原必要读回块保持原正文；
4. 原cleanup前插实际207 rules/science与always单份读回；原cleanup改调同义原条件加新条件的独立CLI；
5. report加新增单body与实际outcome字段。

正常Actions AST/node --check属于原源解析责任；本地仅源码文本、JSON、元数据、字节/SHA工作。未import、AST、编译、fixture或运行任何科学，没有生成accepted/native/fullDN结果，没有创建run或移动Git ref。

三新源本身是全新增文本；另给相对主控已读draft的完整小diff（含真实R459字段、稳定owner读/quiet、M14键修正），不是再改已冻结R456/R457/R459。原205对象及所有既有数学源原字节保持。

## 11. 当前实际边界和后续判读

本件未宣称首次准确C非零场能接受；未宣称三个误差上界必降；未宣称现有6小时能付M128完整far；未支付仅由source没有实际执行的任何scope。若只得level0、R456partial或Mpartial，保它的真实有限责任、实际停止和未访范围，不能用上一场J或原hash填补。

R461显示生成器、R462旧112远端族与新增M模态联合均不在207调用闭包。README要求的多t网格交付和实际误差向机器/求解容差收敛，不因有限两级的存在自动付清。R459也明确有限序列不证明准确极限/统一C2收敛。此入口将已经付出的同目标数学与实际求解接口放到一条真正执行链上；实际R460仍需从原终态必要结果据实判定。

主题容量元数据由主控2026-11-16读取：R459发布树9177 blobs、196952564 B、truncated=false；本件单件均<100KB，新增完整包由主控入库前另计真实bytes。这个存储数字不作为科学门。

## 12. 暂存交付物

`publication-files.json`、`workflow-relative-to-published205.diff`、`request207-complete-addition.diff`、`final-runtime-relative-to-root-read.diff`、`runner-step-contract-final.diff` 及当前目录的 `baselines/` 只供主控读准确来源/完整修改；不需要将暂存索引和diff入Git。新request是新增文件，旧205请求原件没有删除或修改，因此其完整改动以新增文件全文和保留旧对象的明确引用交付。把两个不同请求强作同一路径替换的机械diff会达120957 B，无需另造该大暂存件；两个真实完整文本分别97406 B与21956 B均已可读。正式入库为三个运行源、新request、新workflow、本接口，以及主控另发R458条件证明。
