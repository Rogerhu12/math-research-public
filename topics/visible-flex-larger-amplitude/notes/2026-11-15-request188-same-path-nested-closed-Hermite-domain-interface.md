# Request188：同一准确Hermite路径的嵌套闭段域继承——完整公开Actions接口

作者：ChatGPT /root/exact_refinement  
日期：2026-11-15  
状态：独立可执行源码与接线；只完成文本、身份和差异核对，未本地导入、AST、编译或科学执行。本接口不预报实际188结果。

## 1. 具体改变与原责任

188从真实actual98重新恢复原父warm/status，执行一次完整原37-query模型和原新点FD。原170准确端点/方向参考、原175所有629组完整453分量闭段Hermite差额先按原算法支付；随后完整声明37查询×2048角×17档闭段域责任。只改变最后这一阶段的重复证明方式：同一查询、同一角度的某个闭段已由原完整系数分类严格证明后，较小的嵌套闭段可直接使用R398集合包含推论。

继承不是对子档系数盒再次求值。它不要求各档余项盒互相包含，不把余项族当固定二次函数，不继承未决或反证。每档自己的原完整453差额若不可用，仍保原缺失依赖。旧175已停止的未提交角不被本次结果回填。

原模型/FD、全部非线性域、原17档真实试探、merit、原QP与完整外变量、native/fullDN/最终物理审计责任均不变。新诊断的部分结果、反证、传输失败均不能修改原模型及FD返回值；公开job的结论与具体科学字段须分开读取。

原actual175已经由R372正式记录：一次原模型接受α=1/8、FD通过；全部629组完整453差额已计算；在5400秒诊断预算后，43910个查询角事务、746470个角×档直接分类已提交，其中702379严格、44091未决、0反证。该事实只说明有明确重复分类工作可研究，不能保证188完整结束或严格通过。

## 2. 数学对象与包含证明

依据：

- R354，20501 B，SHA256 `b6e293c20ffb6584f316b3e38877b7e3d4fb61cbad1f008718ab034f605cb183`。
- R398，11337 B，SHA256 `be828511c22ec7fe6c0e9dcefa1637b2b2587d5e634407d8e25ddb9e7ca82ba7`，文件 `results/R398-same-Hermite-path-nested-closed-domain-inheritance.md`。
- 已发表原175设计，14877 B，SHA256 `b3094ad14bf332cfb6e891faf1d45eb4774075fe9cea7958788cc2f1474286a2`。该文件仍以175真实名称绑定，不改成188或伪称新设计字节。

固定查询q、原有限角n和实际捕获的两端点chunk身份，原准确路径为同一个函数：

$$
H(t)=\widehat q_0+t\widehat q_1+G(t),\qquad 0\leq t\leq 2^{-j}.
$$

原执行形成差、准确有限RHS与原返回词的差、准确一阶变化与原J/P字词动作的差，均来自同一次当前原模型现场。原代码在17档外形成相同的G0/G1/H0/H1；每个j只改变用于包围二阶余项的完整系数盒。真实G2(t)可以随t变化；它不因选择不同包围档而成为另一条准确路径。

如果直接分类已经证明同一q、n的全部t∈[0,2^{-k}]满足a>0、P>0、−1<ν<1，则j≥k时[0,2^{-j}]⊆[0,2^{-k}]给出同一真实路径的相同严格域结论。即使另算子档系数盒会较宽，也不改变这个集合包含命题。原查询a、ν、μ由实际单站缓存b/C和完整参数行形成；不由rounded scalar反解b，不混合不同chunk的J/P/cache词。

原完整338物理系数及115个零RHS分量保留，两个mean行为0、225。查询角jet使用原全部112模态；P完整最高14次、15个系数。原准确有限投影使用已发布84af的正sin约定。对真实IEEE程序的全闭段执行误差、连续角/连续站、全RMS及native接受，没有从这个证明获得新支付。

## 3. 实际可执行遍历

科学consumer主要新入口是 `inherited_closed_outcome` 以及 `visit_complete_query_angles` 的同角局部parent。

每个query/angle从j=0到16顺序遍历：

1. 子档自己的 `radius_by_step[j]` 为None时，照原记录 `not-computed-endpoint-bound-unavailable`。不以父证明补造其端点/629差额记录。
2. 还没有直接严格父档时，执行原 `projected_remainder_jet_envelope → query_polynomials → classify_closed_polynomial`。完整degree14 Bernstein与Horner相交、严格条件、两端反证分类逐字保持。
3. 首次出现 `strictly-proved-on-whole-closed-interval` 后，保存该实际直接结果的canonical字节数/SHA及q、angle、k。因原顺序从大段向小段，这是本角最大“已直接证明”的dyadic段；不是最大可行域或最优步长证明。
4. 后续有自己原依赖的j>k，记录 `strictly-proved-by-containing-closed-step`，引用同一个角事务中的直接父结果及R398。不再形成子档d2/e2、多项式或系数范围。
5. 每档仍检查原budget；完整17档结果作为一个原子角事务写入临时ledger。只有整条写入返回后，才更新全局及各query/step计数。

父缓存只存在于该q、angle的一次遍历中。没有跨query、跨角、跨chunk或跨run缓存。每个继承记录保源父k、父/子准确闭区间、父结果SHA及明确 `directly_classified_child_coefficient_family=False`。父完整系数/区间见证仍在同一Actions临时角ledger，不通过摘要搬运。

在当前角第j档中断时，可能已有局部计算但整17事务没有提交；全部计数维持上一已提交角，当前角及后缀明确“未完成提交”。不把已经做过的局部工作误称完整提交，也不以局部结果充当后继真实输入。

源级核到原84af的SIGTERM/SIGINT handler会立即抛ResourceStop，不只是置标志。为避免信号在ledger写完后、17项计数尚在更新时留下半提交，188在私有module main的原handler添加一条显式回调。只有“整角ledger.write＋全部计数和cursor更新”短段内，angle_commit_active=true，回调保留signum并返回；finally清标志，完整提交后立即按原ResourceStop语义退出。其它阶段原handler立即停止。它不依赖线程级signal mask，因而不遗漏由库线程送达、最终在Python主线程执行的handler。实际deferred信号表进入必要读回。预算检查和数学分类不变；byte-cap在写入前失败，不更新计数。这个工程原子性不宣称覆盖SIGKILL、机器丢失或I/O故障；发生此类情况仍按真实传输/文件状态标partial。

## 4. 完整保留的数值代码范围

原175基线：

- `exact_20261115_R354_thirty_seven_closed_query_domain.py`：36928 B / `cf4fa7b33bfcc13cd68193c3abc9b2da8edae4b90e64c16bcfbcce863a095d89`。
- `geometry_20261115_R354_thirty_seven_closed_query_same_job.py`：36809 B / `825caec6efc3fa7fca5daf9d70a9bed907bb0fe91b3fb39858b9d0da3a66d516`。
- 原发布commit：`81bf71ae214da94b01ebff4870fb4ee3ecd8782b`。

以下consumer函数经纯源码逐字比较，除读取 `query_domain_175`→`query_domain_188` 身份外不变：`interval_jet`、`projected_remainder_jet_envelope`、`coefficients_on_unit_interval`、`complete_range`、`query_polynomials`、`contradiction`、`classify_closed_polynomial`、`scalar_coefficients`、`full_coefficient_summary`、`endpoint_second_upper`、`prepare_complete_families`。

因此原全端点M闭界、全部453差额、三scalar完整关系、338角合成、P15项及直接严格/反证标准不变。新方法只省略已由集合包含支付的重复子档分类。

原endpoint模块仍是75046 B / `84af1e250b8a52d9b1691dd5dbeea4ff674ee79949fd72737e16c3f1b2fa018a`。新consumer在Actions内按14条完整old/new字符串、唯一次数生成独立私有模块。生成结果75536 B / `a2d2d09b521996f2201b5634aabe5ddc61218b24b7f3ee96e6501a00af12d1bc`；原数值函数正文全部不变，只改身份、main新增阶段、受控信号提交回调和最终scope/读回。公开checkout源不修改，旧99ef负sin草稿不参与。

原query scalar capture `geometry_20261115_R354_thirty_seven_query_scalar_capture.py` 26648 B / `0a8f4920d5f4c080c64f5e9ea6aedd203c90a475d99c4e73d5ddce6e7a9d5a90` 逐字复用，无新捕获源、RHS/J或scalar调用。

## 5. 科学结果字段与计数语义

新完整result的域字段为 `query_domain_188`；schema为 `R398-complete37-same-path-nested-closed-domain-v1`。原 `query_step_results` 仍有最多37×17个真实记录。

| 字段 | 本次含义 |
| --- | --- |
| query_angle_step_responsibilities_committed | 已整角提交的直接分类与包含继承总数 |
| query_angle_step_direct_evaluations_committed | 实际执行原完整系数分类的角×档数，不是底层区间操作次数 |
| query_angle_step_inclusion_inheritances_committed | 使用同路径闭区间包含推论的角×档数 |
| query_angle_step_direct_strict_proofs | 直接分类得到严格证明的数量 |
| query_angle_step_inherited_strict_proofs | 继承得到严格证明的数量 |
| query_angle_step_strictly_proved | 上述两类严格证明之和 |
| first_direct_strict_parent_trial_histogram | 各k作为某已提交角首次直接严格父档的次数 |
| all_requested_query_angle_step_responsibilities_accounted_for | 所有629档均有原差额依赖，且每档2048角责任已直接或继承处理 |
| all_requested_direct_step_range_evaluations_performed | 所有责任确由直接分类支付且没有继承时才为true |
| complete_accurate_query_domain_on_all_closed_steps | 每个声明query/angle/闭段都实际获得严格域证明 |
| committed_method_counts_consistent | 只核已提交计数相加关系，不重算任何科学区间 |

每个query/step另存 `direct_angle_evaluations_committed`、`inherited_angle_proofs_committed`、两类strict计数及对应完整角连续范围。原rigorously_refuted/unresolved/未完成范围保留。

`scientific_completed` 改为全部声明计算或推论责任完成，不能读作每个子档都重新执行了Bernstein。它可以在仍有真正未决/反证时为true；只有全部严格域证明才令独立诊断数学exit=0，否则3。异常/资源/传输状态独立，不借此改原model/FD。

## 6. 来源、真实输入与完整闭包

父仍为actual98：

- run `43677587785`，artifact `14147700690`，809042943 B / ZIP SHA256 `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`。
- 原source `918fdb11dbb7a424b6149b405e2c7fab3cc0c737`。
- warm `warm-001.json.gz`：4927052 B / `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`。
- 原status：3379453 B / `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`，保原JSON bytes，不重序列化冒原件。

原配方仍叫 `public-thirty-seven-model-recipe.json`，request155、schema `actual98-thirty-seven-model-and-FD-recipe-v1`，SHA `f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea`。它没有伪改成188。原90源、原worker1、158/166/170各3来源、175原3来源全部105闭包中保留：旧103逐basename/完整SHA不变，加新consumer与samejob2个。旧175 capture执行复用；旧175consumer/runtime只作为来源保留，不再运行。

三个原参数文件完整字典逐值不变：`source-dependencies.json`、原37recipe、原35recipe。原selected37 typed顺序、75776角行、17实际trial槽、原完整capture/node/FD/所有参数也不变。

本次不使用actual141/155/170/175已经删掉的warm、array或ledger；没有由旧SHA恢复数据的说法。每次真正恢复actual98后新模型现场决定本次原返回和新诊断输入。

## 7. 文件清单与固定身份

| 相对路径 | bytes | SHA256 |
| --- | ---: | --- |
| computations/exact_20261115_R398_thirty_seven_nested_query_domain.py | 46107 | 51d12ef4f224f2b579bd4afbda0f9fd568b2c6eea61e13eec4a1bcbd89422365 |
| computations/geometry_20261115_R398_thirty_seven_nested_query_same_job.py | 38320 | e1f80243405667ba037d826e86004ae8a0fc61747a2b634cd8da0c10fe5a4627 |
| computations/public-thirty-seven-R398-nested-query-domain-request.json | 40401 | 658621725d67ad7642bb8e2f43224e9b38914b2826d7a173ae959e1e8e3f7641 |
| .github/workflows/visible-larger-public-thirty-seven-R398-nested-query-domain.yml | 10927 | c99d4a5dcf380c6dc55af33f8d6f55c7045a532b7459b123b2b8579f8984c074 |

以上computations路径均相对本topic；workflow相对仓库根。完整源码以本文件和明确published baseline提供，没有只给diff冒可执行源。14条私有module替换全部保存在新consumer源码中，逐条检查唯一次数并记录old/new字节SHA。

## 8. 资源与同job生命周期

原资源保持：

| 范围 | 预算 |
| --- | ---: |
| 全science，从恢复/transport前开始的单调时钟 | 10800秒 |
| 新诊断上限 | 5400秒 |
| 完整结果finalization margin | 60秒 |
| 读回/清理预留 | 300秒 |
| 未压缩临时ledger总上限 | 8589934592 B |
| workflow science step | 190分钟 |
| job含setup/必要读回/cleanup | 215分钟 |
| always必要读回 | 15分钟 |

同job runtime按全局剩余时间裁剪所有child启动和wait。诊断只得到 `min(5400, remaining−60)`；不足时明确未启动，不把剩余预算假定为5400。原子17档事务不因继承而取消预算检查。此优化没有测得加速或完成保证；仍可能被端点参考、全部629差额、原model/FD、ledger容量或域未决限制。

新独立namespace为 `RUNNER_TEMP/visible-R398-188`，rules镜像为 `visible-R398-188-rules`。每个namespace以当前run/source/attempt真实owner marker绑定。

所有临时原模型/FD/完整result/ledger保在Actions临时空间；先必要读回，只有实际readback step success及marker存在才删除本namespace。失败保未读范围和原错误，随runner销毁，不假称已完成清理。不使用upload-artifact、Release或Git保存可重算数据。

原规则runner源码/真实pull--rebase/2700秒周期/变化停机保持。root README pin `21bd547f56590b7f2dd279d0297efb289a9b2783`，topic `bff8aea253a9e6a7a4fac28d810ac454c5499fec`；固定科学checkout不随监控镜像移动。compute permissions沿原contents:write、actions:read，tokens只环境/git过程，不入科学输出。

## 9. 单份必要读回

新samejob的readback模式只读取真实原JSON/日志，不重新做科学算术。必要摘要保持一次不超过90000 B，无语义分段、base64或重组大科学表：

- 原完整实际17trial槽：已访/未访、原返回scalar、原拒绝原因及接受值；原新点FD字段。
- 全37 query typed身份，17档各自严格/反证/未决/未完成query集合。
- 全37×17的原已提交角数、两类strict数、direct/inherited数量、未提交角连续范围及原依赖缺失原因；相同元数据组只按query索引范围编码。
- 原全局counts/flags、实际角事务cursor、首次直接父k分布。
- 原端点参考/J/P/旧逐点transfer的完整未完成范围。
- 当前生成私有模块/准确source/proof/input/ledger/result bytes与SHA，必要原错误文本和位置。
- 不输出全453区间向量、629大系数见证或37×2048×17科学表。

若这份真正必要摘要仍超90000 B，读回明确 `summary_complete=false,transport_complete=false,process_exit_code=70`，保完整原文件身份/未读范围，不分包，不以exit0掩盖，cleanup不运行。独立child摘要上限88000 B同样只影响运输，本job必要读回从完整result恢复其必要字段。

帧为 `BEGIN_REQUEST188_NECESSARY_SCALAR_SUMMARY` / `END_REQUEST188_NECESSARY_SCALAR_SUMMARY`；另输出实际summary SHA/size及是否含JSON序列化末LF。正式读回只读必要摘要和必需原错误，不把大表搬出作新门。

## 10. 执行接口

同job CLI：

```bash
python -u "$VISIBLE_COMPUTATIONS/geometry_20261115_R398_thirty_seven_nested_query_same_job.py" \
  --repo-root "$GITHUB_WORKSPACE" \
  --request "$VISIBLE_COMPUTATIONS/public-thirty-seven-R398-nested-query-domain-request.json" \
  --work "$RUNNER_TEMP/visible-R398-188" --mode run
```

正式workflow把 `$VISIBLE_COMPUTATIONS` 绑定到实际固定checkout的完整绝对路径，不依赖cwd。运行由原rules runner外包；另外 `--mode readback` 和 `--mode cleanup` 用相同request/work绑定。

新consumer仍使用原完整capture/model/code路径和原budget参数：

```text
--capture <current original37 R354-query-domain-capture>
--model-directory <current original37 complete model output>
--code-directory <fixed topic computations>
--seconds <actual remaining clipped to5400>
--max-ledger-bytes 8589934592
--out <same owned namespace/post-model-diagnostic>
```

独立push trigger只看 `public-thirty-seven-R398-nested-query-domain-request.json`；独立concurrency `visible-larger-thirty-seven-R398-nested-query-domain`，cancel-in-progress:false。原175及其它在跑实例不修改、不取消。

## 11. 静态核范围与剩余边界

已完成纯字符串/JSON/SHA核：旧103源码逐项保留、三参数字典不变、原model flags与query specs不变、105计数、request→workflow SHA、consumer→samejob SHA、私有14替换计数/生成完整SHA、原数值函数文本比较、原预算与一次摘要/cleanup合同。samejob的原child生命周期、原17trial选择器、domain selector与error selector等函数除request标签外逐字相同。

未声称本地AST、Python导入、bash-n或科学执行。workflow使用原Actions AST语法检查，之后直接真实计算；没有添加fixture或数学验收门。R398是包含证明，不是新运行成功标签。188实际结果须由当次source/run及全部原范围独立读取，编号R399预留但此处无未来run、接受点或结论。
