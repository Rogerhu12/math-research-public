# Request163：原151/157日志的完整字段读回与有界元数据传输

作者：ChatGPT /root/amplitude。日期：2026-11-15。状态：独立源文本与唯一请求草稿；尚无163运行结果。本文不会把已有151或157的科学结论改写成一次新计算。

## 1. 本次只补原始读回

[R340](../results/R340-actual157-residual-quadratic-square-chain-and-readback-scope.md)已明确157报告链可读、巨量compute正文未由连接工具返回的范围。R341原结论已由主控发布，完整证明/结果文本Git blob为d81b517dfa96116781c4557208d14d184e4bd9f9，发布提交67ef92e5f72de4e469cc239fa696d4b808e8e089；其中151完整节点表和frontier仍不能冒称已逐值读过。

163分别下载这两个已经结束的compute日志，每个原job一次，放在该次Actions的独占RUNNER_TEMP。它解析原日志文本，重建原JSON字段、分段、字节身份、记录顺序和覆盖计数。它不导入任何科学模块，不恢复78源，不下载四大科学输入，不调用原模型、J、Hessian、FD、Arb、native、优化器或任何区间计算。所有原科学门和原科学退出码保持原记录。

原始连接工具对巨量compute日志返回Transport closed，不能从这个传输错误推断151包围错误或157优化失败。本次工程失败也仍属于读回/传输层，不能反向改变原科学状态。

## 2. 四件可直接发布的文件

| 路径 | UTF-8字节 | SHA256 |
|---|---:|---|
| computations/root_20261115_existing151_157_log_readback.py | 77301 | ecb77c7e4aae0b7888c58c753ca74d49f0528db3f743443582c3bc4503853250 |
| computations/public-existing151-157-log-readback-request.json | 17848 | 4ae311d844e7f25adf6fe65e0d246ad26d2deb7e236dfe6a3599a7672c40ec63 |
| .github/workflows/visible-larger-public-existing151-157-log-readback.yml | 13974 | 1413450a6c0c8263c276c863dbbb6a4da9e7b3f88b7486a48f8166e33bc49893 |
| notes/2026-11-15-request163-original151-157-log-readback-interface.md | 本文最终身份在交付清单中 | 不在正文自引用 |

除workflow外，路径均相对本课题目录。本次只新增四份小文本。原151/157科学源、规则runner及原workflow均不修改；没有源码身份重标。请求中的两组protocol_sources只负责这次原日志协议，不声称其小文件数量等于科学闭包数量。

## 3. 固定的两条原来源

| 原项 | 151 | 157 |
|---|---|---|
| run | 43724306509 | 43729310294 |
| source commit | 618a9369d2bd45210767e294726cec10be1cd2df | c71cbeac7fd13c65cf50c7eb39842e9949737b25 |
| attempt | 1 | 1 |
| compute job | 132842781513，failure | 132858021333，success |
| 已读report job | 132859348081，success | 132861152631，success |
| 新的原compute日志下载次数 | 1 | 1 |
| 本次重新下载原report | 否 | 否 |

新helper先从官方REST读取原run、compute job和report job元数据，逐项核run ID、source commit、attempt、终态和实际conclusion；随后从明确原commit的Contents API读取协议小源码，对请求硬锁的size/SHA做字节核对。151核原consumer及原workflow；157核原search、producer、reader、wrapper、request及workflow六件。原完整科学闭包的其余源由保存报告中的SHA声明保持，不冒成163又独立下载审完。

官方日志接口是GET /repos/OWNER/REPO/actions/jobs/JOB_ID/logs。GitHub官方文档说明其返回下载纯文本日志的302地址：[Workflow jobs REST API](https://docs.github.com/en/rest/actions/workflow-jobs#download-job-logs-for-a-workflow-run)。源明确请求2022-11-28 API版本。首次官方API请求使用Actions读token；重定向地址采用新的无Authorization/Cookie请求，不输出signed URL或token，不猜私有端点。本次不使用新发现的按step接口，也不把它冒成已调用事实。

请求分别给151日志2GiB、157日志1GiB的运输上限；这是读取原文本的资源上限，不是数学预算。达到上限会诚实报partial/error，不重试下载或把缺失后缀填零。

## 4. 精确文本方法，不在本地重算科学

所有原JSON数字用RawNumber保存原词法字符串。序列化仅按原排序键、compact分隔符和ASCII转义重建，保留负零、指数写法和原小数位，不经过float、Decimal或Fraction。仅字节长度、数组索引、节点ID、原Boolean计数等整数元数据参与运算。

原日志每行只剥除严格锚定的GitHub UTC timestamp前缀，可包括行首BOM及重复timestamp；其余文字不变。receipt单独保存完整下载日志SHA、逐行运输规范化SHA和全部异常前缀位置。规范化后的事件文本不冒原下载文件字节相同。

每个内容组给出label、完整字节数、SHA256和parts；每12000个ASCII字符一段。每段本身是完整JSON事件且不超过90000字节。重建按index连接解码后的data字符串，不能把JSON转义的源码字面直接拼接。UTF8原错误字节则采用内层ensure_ascii JSON字符串：json.loads(field).encode('utf-8','surrogateescape')，避免外层watcher再次UTF8编码lone surrogate失败。

这不把大科学raw拆块存入仓库或Release。新小源码通过连接器保存，运行中的原内容只临时存在Actions；选择后的原科学标量及明确范围在Actions日志中读回。

## 5. 151：完整结果、输入及节点覆盖责任

请求锁定原三组：

| label | 原字节 | 原SHA256 | 原段数 |
|---|---:|---|---:|
| complete-target-result | 101961 | 95fa1e1104cf5dcfbf154bbba1b55e27bd1afb685dd82a51cec255d67ba08f94 | 9 |
| complete-input-and-rebuilt-definition-binding | 62020 | 6ed65011f5235f923123ccbcc529b8011bb0389aa3a6c155388ee7373d21c4cb | 6 |
| complete-original-Q-node-outward-conversions | 1533021 | 12794fb7e461a421b20c29e1383f26c867242feecf2b2dc599872f71eb13c9fc | 128 |

三组都先按原段数/顺序/内容SHA重建，包含原final LF。前两组完整原字段输出；grid只保存完整身份、列表长度及范围，不另打印其全部可重算数值。原摘要5137B/7319fbe3dbbd5d11d9e802a285ba53f649bc49603805ab84a0427e0966bd6eb2也逐字核。

原节点记录逐条进入原规范JSONL的SHA账本，保node_id顺序、coarse提交和两子节点替父交易。子区间的左端、共享端、右端仅按原字符串相等比较；depth只计整数加一，不重新求有理中点。原cover最终成员按原node hash核回，允许原source已明确的max-depth终态注释及两个cover附加flag；pending必须指向同一原完整cover记录。

它重建以下五个原文件身份：

- evaluated_nodes；
- current_cover；
- complete_frontier；
- complete_cover_transactions；
- original_query_plan。

原当前cover每段的首尾/相邻端点字面必须精确接合原coarse片段；完整节点数、frontier/queue计数及原Boolean谓词计数与result保存值相符。这是存档覆盖账本核对。没有重新计算半径、速度、区间正性、目标误差、Q转grid外包或全域delta；不能把同一Boolean再次计数写成独立证明。原151未完成包围、65535节点预算停止及未付范围完全来自原字段。

## 6. 157：完整外试探与有范围的内部模型读回

请求锁定：

- 原status声明51842612B/931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0；
- 原primary89063B/7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2；
- 原最终chain29684B/9d8bf161d9b88c0c411d326b1717fd2d32332a49534041ebd495b673a35652bd。

primary和chain通过原帧/身份核对后即完整输出，不等额外内部覆盖完成才付原值。随后重建原reader stdout、所有结构part、完整group索引、所有移动的primary字段与原fullview；value/object/list/string几种原operation都按原路径、列表范围、字符范围和SHA核。重复/缺失/重叠/未知operation均明确失败，不补值。

完整输出的字段包括：

1. 原initial、final、各轴/各步FD、literal model binding、所有最终门及scope；不把完成flag当成逐项FD通过。
2. 八个原outer除内部巨大model_updates之外的全部字段，包含完整外模型J/H、原axis-vs-direct动作、两条路径状态、fallback模型/curve frame、原radius更新及未访后缀。
3. 每一个原实际physical trial的完整JSON，包含原normal_correction、全部已保normal轨迹、参数、三残差、完整112向量、实际merit、Armijo、预测、异常、接受flag及reason。没有减少试探数量或重算其接受。
4. 每个内部model update的原当前点、全三模型残差/merit、radius、选择记录、controller、终态原因/未访后缀，全部candidate槽的原flag/数量/异常行和完整身份。候选的巨大trial表、重复QR/shift矩阵和逐格数据不再次全文输出，明确标识canonical size/SHA及coverage。
5. 每个outer最后一个内部update的完整模型J、gradient、Hessian、GN/spectral/terminal shift字段；仅其候选全表和shift历史按明确descriptor覆盖。
6. 原outer所选模型点对应的完整原trial行。这里只做存档引用的index、flag、point、residual与merit原字相等核，不重新排序模型merit、不重新挑最小值、不重算多项式。

实际全表中保存的global eligible编号必须按原记录顺序连续；eligible和inner_accept只计原Boolean。原finite point数仅复制原计数，不能因为解析成功就冒重新验证数值finite。巨大内部表已经完整结构重建和hash，不等于root独立逐值审过，更不等于最优性、rank或高精度证书。

原status文件本身没有被下载：本次独立重建的是原fullview的canonical JSON字节，status原SHA仍来自原producer/reader声明。两者容器schema与字节不能混称。

literal binding比较以此前实际154已经完整读过的保存描述器为参照，逐项比较十个原数组descriptor及相关标量字面；输出相等/不等完整结果，绝不假设相等作为新科学门。不重取数组、不重新形成矩阵、不量化SHA差异的数值大小。157的41-source闭包与四输入声明按原request/完整view核，不能冒107源文件全部又由163独立取审。

## 7. 原误差和工程失败也完整保留

所有原producer/reader stderr字节依原identity/part协议重建，空文件同样有实际SHA；完整错误正文在清理前输出，不只保hash、不截32KB。源记录的failure/cleanup/control事件保持原JSON。163自己的异常给出failed_stage、完整错误类型/traceback、此前完成的metadata check数及hash；仅token和signed URL查询凭据被去除。

原151/157source字段或传输hash不匹配时，不继续造完整receipt。已经读出的primary/chain或151结果仍保留在此前日志块中。complete=false只陈述本次读回未完成，不改原优化/区间结果。

## 8. 可执行CLI与workflow责任

```bash
python -u topics/visible-flex-larger-amplitude/computations/root_20261115_existing151_157_log_readback.py \
  --request topics/visible-flex-larger-amplitude/computations/public-existing151-157-log-readback-request.json \
  --request-sha256 4ae311d844e7f25adf6fe65e0d246ad26d2deb7e236dfe6a3599a7672c40ec63 \
  --lane 151 \
  --out "$RUNNER_TEMP/visible-existing151157-151-$GITHUB_RUN_ID-$GITHUB_RUN_ATTEMPT"
```

157只把lane及独占目录中的151改成157。helper要求GITHUB_ACTIONS=true、同一repository，以及fresh的RUNNER_TEMP直接子目录。token只作为Actions的GH_TOKEN环境输入，不写请求、不传连接器、不进任何元数据。

workflow由唯一新request路径push触发，两个独立read job并行；固定checkout11d5960a、setup-python a26af69b及Python3.12.14。每job35min，读取step30min，没有pip安装、数值脚本或artifact upload。小源码/requestSHA与实际checkout双README Gitblob先核；root21bd547f…、题bff8aea…是当前已读版本。它不修改规则监控周期，任务上限本身小于2700秒周期，也不调用任何科学程序。

report只接两个各≤90KB的完整索引，逐字SHA核后分开打印，不合并大科学payload。索引缺失、过大、读回失败均明确标识；不会删字段伪造complete。完整语义输出在对应read job日志中，原内部表的未全文输出范围也在索引中。

源的finally在原字段输出后，只删除该次新建的日志目录；always step对超时遗留做同一目录的属主/普通文件检查、SHA记录后删除。原输入、源、其他job目录、旧科学产物不在清理范围。若清理失败，其完整错误与原读回完成情况分开记录。无artifact、Release、raw main文件，也没有分支/ref写入。

## 9. 实际范围和下一步

本交付完成的是源文本、原协议逐段对照和字段/身份接线。终端不可用，未执行Python AST、YAML解析、科学导入、测试fixture或本地metadata reader；不把这些未做事项写成通过。root在发布前按已授权规则全文读此小文本后统一入库即可，原151/157不重新科学运行。

163真正完成后，主控可先读两个小report索引，再按语义label读151完整result/input和157原FD/模型终态/真实试探。若任一原字段没有成功读出，后继结论保留这一具体边界。157的微小下降是否反映数值驻点、完整rank退化或尚有新方向，仍须据实际原响应/二阶/模型与试探字段作条件分析；本只读工程不预判，也不以新读回作为原数学额外验收门。
