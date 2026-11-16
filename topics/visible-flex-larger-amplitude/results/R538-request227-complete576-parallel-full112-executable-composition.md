# R538 — request227：完整 576 段真实并行与原 full112 全链执行接口

作者：ChatGPT / amplitude（AI-assisted）  
日期：2026-11-16  
可信度：**已证明，限本文来源组合与控制流条件；本入口尚未实际运行。** request227 / actual R539 是明确预留，本文不填未来 run、数值、完成、native/full-DN 接受、耗时或加速结果。

## 1. 明确的新操作

本入口实际调用 [R531 的完整并行 cellFlow](R531-complete-current576-parallel-cellflow-source-and-conditional-equivalence.md)，从原 request224 字节子合同在新 job 中恢复所有真实数学输入、原数值政策和源。每次实际 withJ current576 求值，用 **2 个真实工作线程，每线程 old-generation heap ceiling 3072 MiB**；原主 Node 的 6144 MiB 另保。所有576段、226状态、224方向、两mean、112频率、原R273及完整FD/full-DN/末审计均保持。

source plan 允许2–4线程；本入口实际选择2，不能把允许范围写成“本次用了4”。额外线程的heap ceiling合计6144不包含原主Node，不是进程RSS/ArrayBuffer总上限。新增传输、线程、cache隔离和内存竞争构成真实资源差异。本文不以条件等价证明推定速度提升或剩余原钟足够。

原224正在运行的实际输入/输出不被修改或继承。其发表source498c03a7753a6f6caf66b563b2319cd42a447aaf、官方实际source23176ac678ea92882fa38ec6ddcc09e98742ac89，仅作为真实来源记录；新run必须在根端实际发布与dispatch后绑定。本文也没有将R531源组件发布等同于request227已经运行。

## 2. 本次三个发布文件

| 角色 | repo-relative 路径 | bytes | SHA256 |
|---|---|---:|---|
| 新外层请求 | topics/visible-flex-larger-amplitude/computations/public-complete576-parallel-cellflow-full112-request.json | 19994 | 56c985a5513e9c403fb9a31f03e1a5982267684293e4b925c181d1f8d5246504 |
| 真实执行 workflow | .github/workflows/visible-larger-public-complete576-parallel-cellflow-full112.yml | 53746 | 3305b7ec7fb77437e16d9bfb5d5993afaaa7eb6ad32370bb372fbeb6df822609 |
| 本文 | results/R538-request227-complete576-parallel-full112-executable-composition.md | 以发布身份为准 | 不自引自身SHA |

本次只增加小外层请求、workflow及本来源/操作结论。原R531四helper、source plan、八生成视图、原224 recipe和完整入口文件均不复制为新的同义版本。临时交付manifest与展开diff不是Git发布件。

新请求 schema 为 public-complete576-parallel-cellflow-full112-request-v1，request_number=227，lanes=[parallelComplete576Original112]。其193源集合通过完整祖先request及新12源明确构成，不在新请求再抄整份181旧map。

## 3. 祖先与当前来源的分界

原224全文必须保留：

| 对象 | bytes | SHA256 |
|---|---:|---|
| 原 request | 88551 | 6aa2f23f2e92f326ea2bf17b58f084c28580f5a44420c8cf47816597e9e5b980 |
| 原 recipe | 21539 | 0c9fa04642835dd37f9da5aeb03a35abae4be4e75283c3e2203a73dcec6544ea |
| 原生成器 | 23213 | 7b83c7c69b155bb99d402f9d03e24dbb11bf0d57ab239c1d23c9839d2e583f1f |
| 原 source plan | 36611 | 9a184000c0b8e81dc3d247e39b873a2c66cc7be4a42cfa01090df8ebf2fd7326 |
| 原 workflow | 42646 | 599f32c8a238dfd7bee7affacabcc1a3aeb51cb185619e509a477136e9320a41 |

新R531计划63026 B / 499616558f05865726aefa63c10842fa1a8a73172da557a18dbf7b8d574e61b7，逐literal生成8份真正新basename。它绑定4个新公开helper、8个真实旧base、93项before/after/count、8个完整输出bytes/SHA。原181源保150公开+31生成，新增加4公开+8生成，实际总数193=154公开+39生成。原78数学source-topic、四原输入、两份frozen native ready另依原责任恢复，不由这个计数替代。

所有生成源都在本次真实 VISIBLE_COMPUTATIONS 下，原文件不覆写；旧31临时视图也在当前job按公开祖先计划真实重生，不把它们当成可从Git直接fetch的公共文件。新的193 map不意味着所有想象中的import都被证明；这里覆盖实际完整调用链及其明确源。

原224 request中的execution_entry、native_client等字段保存原字，表示**祖先子合同的实现**。实际227调用由新外层actual_entry明确决定；原recipe的旧native_correction implementation字段同样是祖先provenance，不能说它仍是当前科学producer。新runner/full112/client/reader如下：

| 角色 | 实际 basename | bytes | SHA256 |
|---|---|---:|---|
| runner | root_20261116_parallel_input_support_contracted_trace_r273_run.py | 15716 | 4c7e13df26c39ab881ac878429150b79e7536e55908d3ae69d097bba3c4afe19 |
| full112 | geometry_20261116_six_control_parallel_input_support_contracted_trace_r273_full112.py | 52339 | 525be2072fee4f53122d5802ef57d8b00f24e7b08408a3ed0441fd1872686311 |
| client | geometry_20261116_parallel_input_support_contracted_trace_r273_tail_client.py | 23870 | a8571e0c47c8f2e264c76ce3ee1554ca19cbcaa0366fbc6b7fdc2fe71e9856b2 |
| reader | root_20261116_six_control_parallel_input_support_contracted_trace_r273_scalar_readout.py | 50519 | fb8899e0da24ff8b6b7d5e728b3906c5096f57e0e93c0e511bfc506ddd32ea96 |

真正当前wrapper schema为R531-complete576-parallel-owned-process-wrapper-v1；full112 schema为R531-six-control-parallel-cellflow-three-active-nonzero112-physical-DN-v1；reader schema为R531-original64-parallel-complete576-necessary-readback-v1。原recipe schema不改。

## 4. 不变的数学初猜和门

原六参数按p1,p2,p3,theta1,theta2,theta3顺序：

~~~json
[0.41654476801167684,0.23884336093393582,0.5270922473095916,-0.13437878055563054,-0.005765450212224129,0.4141025261683763]
~~~

lambda=0.001；仅p1,p2,p3为活动坐标，三个theta冻结。实际新初猜仍由原fresh-circle/low-three路径形成；没有读入旧211、224或其它run的H、J、root或完整state。

workflow逐字段核新outer.execution与原224.execution完全相等，也继续核原195/208/210/211祖先的原约定。原参数包括：

| 项目 | 原值 |
|---|---|
| M / N / depth / state / directions | 112 / 2048 / 576 / 226 / 224 |
| native iterations / noJ trials / tolerance | 32 / 10 / 2e-9 |
| full-DN outer iterations / inner trials | 8 / 17 |
| RMS / boundary / FD tolerance | 1e-6 / 1e-11 / 5e-5 |
| max_nodes / material / physical angles | 1200 / 4096 / 4096 |
| original jac_workers / main Node heap | 2 / 6144 MiB |
| scientific wall clock | 18000 seconds |
| science step / compute job | 330 / 350 minutes |
| 原规则同步周期 | 2700 seconds |

原高度initial_positive_increment=0.015625，accepted multiplier=2，maximum_increment=0.25，maximum_bootstrap_requests=64。零/中间外层请求jacobian=false，末H请求true；求解器内部需要的全切向/predictor/mean照付。第一次被确认为原数学拒绝的正高度试算停止，不为本次并行重启递减height路线。

原R273 eta文字“1”、2因子workers、全部129248行/577 penalty blocks/224方向、2 GiB factor cap、原remaining-clock与transport reserve完全保留。线程pool不是R273因子worker；不能把两者计数混成一个资源总量。

原FD和338×112最终响应允许原合同中的实际混合列。完整解析J不是本入口新增接受门。原full-DN及末audit实际结果仍需由真实原consumer返回，不因所有cellFlow完成就补成native/full-DN接受。

## 5. 真正执行顺序与一次时钟

本workflow同时有workflow_dispatch和原样push触发形状，新的push path仅本请求文件；root负责实际发布后官方单次dispatch及run/source绑定。源文中的status是发布前文档状态，不是未来运行回执。

实际步骤顺序：

1. checkout原公共源与新request/R531文稿；建立本job全新子namespace。
2. setup原Python3.12.14、Node24.22.1和固定numpy/scipy/python-flint。
3. 原224生成器在本job恢复全部181 computations来源。
4. 真正校验新outer全文SHA/字节、原子合同/recipe、资源值；复制4新helper到同HERE，再执行R531生成器生成8新view。
5. 原全部source/recipe/README/数学输入审定不变，加核12新源及实际193集合；对**真实本workflow路径**做原bash-n/inlinePython/源语法步骤。
6. 原四字节输入、两frozen native inputs、78原source-topic分别真实恢复。
7. 原规则owner在原330分钟step内调用真正新runner；runner给整个原完整科学链一次18000秒deadline。
8. 实际科学完成或中断后，always执行新necessary reader和原rules-parent观察。
9. 只有完整原必要摘要marker、真实新来源receipt、完整读回及新鲜owned quiet共同成立，原范围内清理临时raw。
10. 独立report只复述一份原必要body及实际身份，不执行第二次数值计算。

固定的目录词visible-original64-input-support-contracted-trace224表示不可变祖先generator要求的子namespace，在每个新job的RUNNER_TEMP内真实新建。它不读旧run的目录，也不把实际request号伪装成224。新wrapper/status、sourcebinding、report均分列actual_request=227与immutable_source_request_ancestor=224。

源准备在原science owner起点之前，沿原step/job约束；科学deadline由新wrapper一次建立，内部沿原VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC及原R273UNIX投影继承。没有在worker、iteration、height或cell处重开。这里不额外把18000秒科学clock扩成另一份原钟；source准备与rule/cleanup overhead如实保原层次。

## 6. 两层源准备的实际receipt

第一层仍运行原224generator，其输出设置VISIBLE_COMPUTATIONS及VISIBLE_RUNTIME_SOURCE_VIEW_RECEIPT。新layer在同实际目录运行：

~~~bash
python "$VISIBLE_COMPUTATIONS/root_20261116_parallel_cellflow_source_views.py" \
  --computations "$VISIBLE_COMPUTATIONS" \
  --plan "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations/r531-complete576-parallel-cellflow-source-plan.json" \
  --plan-sha256 499616558f05865726aefa63c10842fa1a8a73172da557a18dbf7b8d574e61b7 \
  --out "$VISIBLE_BASE/parallel-source-views"
~~~

新helper本身的完整SHA先由新request/公开正文核，然后才被调用；不是在旧loader里动态换一个未绑定的工厂。生成器使用完整literal次数与输出SHA，保每个base和generated的真实绝对路径。

R531 source-views.json的schema为R531-complete576-parallel-actual-source-views-v1；新workflow另外写parallel-source-views/entry-binding.json，schema R538-actual227-immutable224-and-R531-entry-source-binding-v1，内容包括：

- 实际run/source/request227与新outer全文bytes/SHA/路径；
- 不变原224 request descriptor；
- 本次R531计划descriptor；
- 实际新source receipt文件bytes/SHA；
- 真正computations路径、193集合计数和请求的完整并行资源声明。

该binding在科学开始前形成，不含未来成功结果。两层生成任一失败，cleanup记录对应原step outcome并保raw；没有用缺失receipt虚构完整source或科学summary。

新workflow的PYPINS保原181source核与所有数值政策检查，同时逐12新source核bytes/SHA、Python源语法和实际新MJS入口。原bash/Python检查读取的确切路径是.github/workflows/visible-larger-public-complete576-parallel-cellflow-full112.yml，覆盖新增shell段，不再仅检查祖先224workflow。

所有这些现成源检查只在公开Actions执行；本交付没有本地AST/import/compile/science/fixture/benchmark，也没有为优化增加新科学前门。

## 7. 真实owner argv与源选择

原规则runner的SHA和body保留。其真实command由新外层actual_entry.runner选择；原224.request.execution_entry只作为祖先值存在，没有被误用为科学caller：

~~~bash
PYTHONPATH="$VISIBLE_COMPUTATIONS" \
python -u "$VISIBLE_COMPUTATIONS/root_20261116_parallel_input_support_contracted_trace_r273_run.py" \
  --request "$VISIBLE_COMPUTATIONS/public-six-control-input-support-contracted-trace-r273-request.json" \
  --recipe "$VISIBLE_COMPUTATIONS/actual119-batch3-input-support-contracted-trace224-lambda0p001-recipe.json" \
  --inputs-directory "$VISIBLE_MATH_INPUTS" \
  --source-topic "$VISIBLE_SOURCE_TOPIC" \
  --out "$VISIBLE_BASE/execution"
~~~

wrapper内部真实entry/client已经是R531独立source身份，真实完整原参数由同字recipe和原execution提供。execution根由wrapper建立，内部science/factors路径不额外再套一层。

job环境明确：

~~~text
VISIBLE_R531_ACTUAL_REQUEST=227
VISIBLE_R531_CELLFLOW_WORKERS=2
VISIBLE_R531_CELLFLOW_WORKER_HEAP_MB=3072
~~~

新source准备成功后设置VISIBLE_R531_SOURCE_VIEW_RECEIPT、VISIBLE_R531_SOURCE_PLAN_SHA256；本workflow也设置VISIBLE_R538_REQUEST及VISIBLE_R538_REQUEST_SHA256。实际runner和reader同时核原子合同source receipt与R531新receipt。新outer本体在prepare/preflight/science caller/readback及cleanup使用其真实19994字节和完整SHA绑定，未借原6aa2…冒新请求。

原rules-parent-receipt/readback schema继续其request224来源名，因为原consumer读取这些字段；新owner记录另外写actual_request、actual_outer_request_sha256、immutable_source_request_ancestor、实际newrunner及并行资源。这个旧schema名不代表原224run在此继续。

## 8. 原算术与新组织的条件结论

在R531明列的同实际有限输入词、原工厂/profile/cusp/options、原flow源和完整成功条件下：

- 主端真实profile调用按原顺序进行，cache的原完整成功序列保留；
- 每个worker使用原R523 flow、R471有限zero-dFlux与R466名义因子收缩路径，原fallback/完整root入口不动；
- 同一真实engine固定分配到一个worker，各worker内按原n序处理其阶段；
- 每阶段完整226×224及两mean行均由原源求得；
- 主端仍按n=0,…,575归并原完整残差/J/端口/mean，不把并行完成顺序当数值求和顺序。

因此这是原完整局部计算的并行组织，不省模式、不省列、不借旧J、不减line-search或endpoint gate。它不把名义线性化升级为IEEE舍入程序的导数，不自动支付原舍入误差、准确C²、branch稳定或全闭面责任。

失败路径区别同样保留：预capture可能比串行提前多读profile；高n可能在低n失败前已完成；资源deadline与内存竞争前沿会变。只有R531限定的五条真实原数值guard在更低n全部已完成等条件下才沿原n优先返回原数学错误；资源、协议、来源或未分类错误不重新跑科学、不升级为数学不可能。

每个worker的engine/counter/last_observation是实际独立序列，不与主engine累加混同。missing inflight记录保持未知，不能按完成stage数反推尚未收到的所有root次数。

## 9. 新单份必要读回

science step结束后always使用真实R531reader：

~~~bash
python "$VISIBLE_COMPUTATIONS/root_20261116_six_control_parallel_input_support_contracted_trace_r273_scalar_readout.py" \
  --directory "$VISIBLE_BASE/execution" \
  --request "$VISIBLE_COMPUTATIONS/public-six-control-input-support-contracted-trace-r273-request.json" \
  --recipe "$VISIBLE_COMPUTATIONS/actual119-batch3-input-support-contracted-trace224-lambda0p001-recipe.json" \
  --rules-directory "$VISIBLE_BASE/rule-sync" \
  --compute-outcome "$ACTUAL_STEP_OUTCOME" \
  --out "$VISIBLE_BASE/scalar-readout"
~~~

原scalar/native/H/R273/FD/fullDN/错误选择全部保留，新增parallel_cellflows段。新段包含所有576原stage/rawCell/rawSegment/engine/worker地址和实际状态，全部实际worker/engine的原统计、R523十四计数、R466/R471字典、scope/reasons/last_observation、真实准备/失败/未访范围、source/owner和各必要raw身份。

它使用固定语义columns/catalogues表达相同值，保缺键≠null、所有位/类型/负零、原数组行序、实际错误地址。没有压缩任意对象树、分包大型科学stdout，或把未返回数组当正文已读。完整成功state/J/RK tapes只在本次Actions临时保存；reader按既定范围返回身份。

| 项目 | 真正字面 |
|---|---|
| body schema | R531-original64-parallel-complete576-necessary-readback-v1 |
| marker schema | R531-owned-complete-parallel576-necessary-readback-v1 |
| BEGIN/END | BEGIN_R531_PARALLEL_COMPLETE576_NECESSARY_SUMMARY / END_R531_PARALLEL_COMPLETE576_NECESSARY_SUMMARY |
| body cap / failure | 90000 bytes / exit70 |
| main output | scalar-readout/scalar-summary.json |
| marker | scalar-readout/readback-complete.json |

原ordinary error prefix1600、traceback2400选择继续，不说成完整异常全文。新source与每worker统计可能使摘要较大；不预保证90K。真实超限仍原70，不从未来容量反向删任何原必要值，也不让旧raw主动删除。

report验证原GITHUB_OUTPUT带出的同body字节/SHA、≤90K、新schema和actual_request字符串“227”，复述同一个frame；打印identity事件另外含实际outerrequestSHA及source-generation outcome。没有body时只给explicit-unavailable scope，不造科学结果。body打印hash不含分隔LF，marker所指文件hash含实际LF。

## 10. 真实静止、原文件身份与清理

协调child与主Node属于同owned进程组/会话，实际worker_threads属于协调child；原start_new_session outer owner、PID/startticks/PGID/SID及未知scope原则保留。新reader的quiet名称检查与真newrunner一致。

原rules-parent还单独从原receipt定位PID/startticks，并只观察相同process是否已不在；shared runner PGID不用整组为空。这条不能被用来替代真正独占科学child组的quiet。

cleanup使用以下真实来源：

- 原224 child request/recipe完整字节身份；
- 实际227 outer request完整SHA；
- R531新source receipt、真实newreader全SHA；
- 新R531 marker schema及run/source/request/recipe/execution路径；
- body文件的完整bytes/SHA；
- 新鲜原owned-group quiet与真实rules-parent absent。

marker.complete不等于数值接受，只证明规定范围已完整必要读回。cleanup只有scalar step成功、原child group静止及原rules-parent已退出等原条件全付才删除自有VISIBLE_BASE。源生成任一不完整、摘要70、owner未知或原证据缺失时保留至runner销毁，不把未生成账本冒空文件。

清理不是新数学门；也不能以compile/程序completed字段填native/fullDN接受。新所有必要状态继续走原scalar内容及原gate逻辑。

## 11. 原文件与参数边界的静态结论

本次对原workflow的实质差异限于：

1. 实际227触发path/并发组/名称与显式资源env；
2. 原224 source恢复之后，R531四helper复制、八view生成与新outer binding；
3. 原preflight加真新源/真当前workflow范围；所有原数值检查保留；
4. 原规则owner实际command改为新runner，附实际outer/source/resource记录；
5. 新reader及report/cleanup真实schema、SHA、marker和source失败分支。

原科学/参数政策不改，未加fixture或短跑。新请求中的count依实际集合构造：原181每一项原值保留，与新增12 basename无交集，实际193。已通过纯文本/JSON/字节方式保存完整祖先与当前diff，不执行新科学。可重建展开diff不作为额外Git文件或另一步发布前门。

R531数学源码本次全字不改。独立M/连续十族/128-bit链的优化不从这条有限固定112链自动继承，也没有被本文偷偷注册。其原schema/source/性能/接受责任仍分别处理。

## 12. 实际运行后的结论责任

只有root实际发布/dispatch后，才能填写R539的真实head、run、attempt、compute/report job、实际worker启动数与参数。源码预留不等于已注册或已运行。

终态必要读回应区分：源准备是否完成、真实H/bootstrap/正高度进展、每次完整J与原R273调用、所有原trial与拒因、每worker及全阶段实际partial、FD/最终338×112/audit、原native/fullDN字段、90K传输、quiet与cleanup。任何尚未开始、资源中断、摘要未返回或未知值保持原scope；不能由相同输入、所有stage完成或worker退出补数值接受。

原222/R511与224/R525的独占终态职责不受本入口替代；没有中断、取消或重复取它们的运行中日志。R539必须只对应实际227新run，不能把224正运行事实贴到本入口。
