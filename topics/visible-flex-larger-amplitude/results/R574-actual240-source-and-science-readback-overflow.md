# R574：actual240 原准备完成、两份完整必要选择超限与尚未返回的科学终因

作者：ChatGPT（AI）；日期：2026-11-16。

**可信度：已证明，限本文所列实际 Actions 元数据、真实返回事件、完整返回的两份超限描述符及固定源码的控制流事实。350903 bytes 的源码必要正文与 221520 bytes 的科学必要正文均未返回；本文不补定 owner、重放、同次模型、FD、fullDN 或 audit 的内部结果。**

actual240 的源码生成、447 件实际源码绑定与原输入准备真实完成。科学外层返回 1，原 rules 和 science 返回码也均为 1；该外层记录 resource_stop=null、external_signal=null、owned_processes_quiescent=true。之后源码和科学两份必要选择分别超过原 90000 bytes 限制，均真实返回 70。compute 与 report 只逐字返回 1846 bytes 和 1163 bytes 的两个描述符。清理走保留分支，removed=false。

因此，本次结论是“准备已完成，科学外层失败，双必要读回不完整，具体科学终因没有传回”。准备成功不证明实际编译或数值接受，描述符的完整返回不等于所指正文已返回，report 成功也不改变 compute 的 failure。不得借旧 run 的 KeyError、残差、资源停点或接受结果填补本次未知值。

## 1. 唯一实际 run、官方终态与读取范围

官方科学 run 为 [43887312387](https://github.com/Rogerhu12/math-research-public/actions/runs/43887312387)，仓库 Rogerhu12/math-research-public，workflow ID 420227793，attempt 1，事件 workflow_dispatch，分支 main。实际 head、checkout 和返回 body 中的 GITHUB_SHA 均为：

bce880e0037870ce0977abc5d54d0cf2bd24d2cd。

官方 created_at 与 run_started_at 均为 2026-11-16T14:35:27Z，updated_at 为 16:32:32Z，终态 conclusion=failure。发布源 commit、行政 publisher 和另一科学 run 均不作为本次实际来源。

| 实际 job | 官方名称 | 终态 |
|---|---|---|
| 133368868125 | Actual240 synthesis-product-owner same-DN model and original FD fullDN | completed/failure |
| 133444086994 | Actual source scope and one necessary240 original scientific conclusion | completed/success |

本结论作者在 16:34:05 UTC 的自然 jobs 元数据轮询确认终态，随后两原 job 日志各取一次并完整阅读；运行中未取日志，完成后也没有再次下载。本文没有获取原临时科学数组或所指 overflow 文件。

连接器返回的是**解码文本**，以下身份为其重新 UTF-8 编码的身份，包含返回文本中的时间戳、命令回显、换行及初始 BOM；不是 HTTP raw 日志的原字节身份：

| 完整连接器返回文本 | UTF-8 bytes | SHA-256 |
|---|---:|---|
| compute 133368868125 | 76669 | f8bd0e0f0a696b2cfdb9311270c4d9f544222ea74f9aefd2e8345c498cd9aa0a |
| report 133444086994 | 17856 | d4106dc2477d11c58e8ffca71225b7a0f336052d05efdd3b857e534ac58a11e4 |

两份必要帧按各自唯一 BEGIN/END 边界提取，去掉外部日志时间戳，保留原 JSON body 末尾 LF。compute 与 report 的源码 body 逐字相等，科学 body 也逐字相等，并分别匹配原 identity 事件。这个比对只涉及实际返回的 1846/1163 bytes，不涉及尚未返回的 350903/221520 bytes。

原日志及可再生必要输出只在当前会话临时缓存中阅读，未创建 Git blob、主树 raw 文件或 artifact。本文为作者结论，记录实际来源、值、完整范围与未付责任。

## 2. 本次冻结来源和未改变的原合同

实际 workflow 为 .github/workflows/visible-larger-public-live128-root-synthesis-product-projected-model-original-fullDN.yml，24295 bytes，SHA-256 722ef48081d5d6e4ee58c9a77cf376832682ab050c4e04fb4e71596d4fafeca6。

请求为 computations/public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request.json，97177 bytes，SHA-256 e4ad6178a06d2cf270f3469c4cbcce4747c8876e7c95c50f829be58c9f6c437a；schema 为 public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request-v1。

R573 source 生成及必要读回使用 root_20261116_live128_synthesis_product_projected_source_views.py，38611 bytes，SHA-256 3bb1084dfb44d675db8f186b138c5fb68ac6da9a1978f25c013e2bc5609f9cf2。实际完整计划 notes/r573-live128-synthesis-product-projected-model-complete-source-plan.json 为 82812 bytes，SHA-256 85fdec3e86821a8a6f85828bbf399347fbd7c3d57e97ab2ad1404561945974ed。

| 当前角色 | 实际 basename | bytes / SHA-256 |
|---|---|---|
| owned runner | geometry_20261116_live128_synthesis_product_projected_owned_run.py | 39422 / 13c3de46ba8f4bcadf82856d72bf330bdf9088d9b06a7f4afd7dfdf658cf3658 |
| 原 fullDN 入口 | geometry_20261116_live128_synthesis_product_projected_original_full_dn.py | 46439 / 721aaa94d4bd70fed644aed0ee62e0d19ba526aadd1e6793645636a90f445b63 |
| 科学必要 reader | root_20261116_live128_synthesis_product_projected_necessary.py | 63394 / e48c769418ffac56a2e931cbee4bc4474ad2067007e561c2aaa49f9a4291701b |
| 同次 owner caller | geometry_20261116_live128_synthesis_product_projected_same_call_owner.py | 26666 / 2af373696034e49f61e6dcc49707e668ed60d600b5a4f9dbf0d71d85cd24ad17 |

447=360 public+87 generated，保原237的432件，再明确加入当前 R572 两公共执行源、两生成 include、新生成器和十个 caller view。完整地图在请求与计划内；该数量不被扩张为任意未来动态导入的普遍闭包命题。旧237全文及 R565 源作为本 job 的明确祖先，不能把旧237执行结果迁来。

本次 R572 的五个合成乘积接点为 fixed_fallback_P、fixed_fallback_Pt、L、evaluation_u_words、evaluation_u_fallback。它们复用原 R564 的完整整数乘积资格与 RN128 核，保持实际左表达式、原右因子字及每次 += 顺序；不声称每次仍字面执行旧 binary128 首乘法，也不声称 fenv flags 或资源前沿完全相同。R564 原三个角向乘积、R561 第二乘法、R550 接受后的完整 RootEval 复用、R535 固定及 U 有限词机制继续保留。source prepare 只生成/绑定，原 owner_scope 规定直接安装 R572 一次，其余四祖先是 source-only。

这些源码条件仍由 [R572](R572-exact-root-synthesis-products-and-original-sum-order.md) 及所引祖先承担。本次准备成功不能补成该 hook 实际安装、g++ 实际编译或任一分支实际使用的证据。

| 原责任 | 冻结实际请求值 |
|---|---|
| field/tail modes；spacing | 112/112；2 |
| depth；节点数；每节点 shooting state | 576；577；224 |
| 含两 mean 的局部 RK 状态；完整方向 | 226；224 |
| 原物理输出顺序 | slope112, second112, meanSlopeCorrection1, meanSecondCorrection1, height112 |
| 物理 J | 338×112；保持原混合导数合同，不宣称全部解析 |
| nonlinear 最大迭代 / trial / tolerance | 32 / 10 / 2e-9 |
| FD 原两组 | direct_boundary、separated_boundary 各10方向；3步长层；2 Richardson 层；relative threshold 0.00005；全部适用 contraction |
| prefix inner trial / RMS / boundary tolerance | 17 / 1e-6 / 1e-11 |
| 原 runtime | node_heap6144、jac_workers2、max_nodes1200、material_angles4096、physical_angles4096、outer_iterations8、extension_step0.005、taper_fraction0.4 |
| native 参数 | eta="1"、exact workers2、max_factor_bytes2147483648 |
| 原总钟 | 19200 scientific seconds；新 H 不重启；readback/cleanup reserve120 |
| job / science step caps | 350 / 320分钟 |
| 同次 call 上限 | owner6000、replay reserve1200、stage8000、boundary600、endpoint600、audit1800、threads4；全部按实际剩余原钟裁切 |
| 磁盘 startup / resource-stop 界 | 68719476736 / 2147483648 bytes |
| 最大未缓存 protocol calls | 18；不构成全部可完成的容量证明 |

actual63 prefix 与 actual91 failed73 tail 仅是原输入/初猜来源，不继承旧接受。权威值及 fresh replay 为原128，当前完整 stage model 在同次真实 owner 状态一次 RN64 后由同一加载 DN engine 形成，再逐有限字准确 lift 到128；原 model 不是被认证的128程序导数，也不宣称投影点已收敛。旧全128误导性 required 字段未被填 true，真实契约仍是 same_call_complete128_value_components_and_explicit64_linear_model_required。

本次不是后来 R594 的 owner12000 来源，仍保原 owner6000。也不能把本次 source 计划中的所有 requested 阶段表写成已实际执行到的阶段。

## 3. 已返回的准备和容量事实

compute 使用固定 head 的 blob:none partial/sparse checkout。日志实际环境为 Python3.12.14、Node24.22.1、numpy2.3.5、scipy1.17.0、g++15.2.0。安装输出不等于本次 scientific C++ 已编译。

14:35:59.6445740Z，R573_source_preparation_return 真实返回：

- complete=true；
- actual_exit=0；
- science_success_inferred=false；
- actual_source_receipt.file=/home/runner/work/_temp/request240-source-preparation/source-views.json；
- bytes=152567；
- sha256=e95f32e1f87520a36c4b89ad5a55f78793441967b00291f0052db33ed4d33753。

14:36:02.5308753Z，request240_source_binding 返回 sources=447、§2的 request SHA 及§1的同一 head；Python_compiled_not_imported=true，Node_syntax_checked_not_executed=true，no_CXX_scientific_compilation_or_scientific_evaluation_yet=true。原绑定块按完整 public/generated map 逐件核实际文件及 README 来源，真实到达返回点。这个事件本身没有认证后面的科学调用。

14:36:02.7011853Z 的 declared_capacity 事件，before 与 after 完全相同：

| 原字段 | 实际值 |
|---|---:|
| total | 154993672192 |
| used | 62962356224 |
| free | 92014538752 |
| minimum_free_bytes_at_start | 68719476736 |
| unused_ephemeral_runner_SDKs_removed | [] |

scientific_payload_deleted=false，maximum_uncached_protocol_calls=18，all_possible_calls_fit_not_proved=true，original320_minute_clock_not_started_yet=true。实际 startup 容量要求在这个时间点已满足；不由此推整个运行始终充足，也不借其它 run 的32GiB或64GiB不足解释本次。

14:36:27.9945494Z，request240_preparation_return 返回 complete=true、phase="complete"、error=null。其 receipt 为：

/home/runner/work/_temp/visible-live128-root-synthesis-product-projected-model240/preparation.json，

84297 bytes，SHA-256 e87ddd3a88f32541e27cf213f2b4b990c2ee8fa701cd9a181163d3691bf8f7f3。

以上原 receipt 正文没有由本文另取；已知的是原事件确实返回的字段与身份。后面的 transport fallback 将 source_preparation_complete 置 false，不会反向取消这里真实 prepare.complete=true，见§5。

## 4. 科学外层的真实返回

14:36:28.0182290Z 出现原 owned runner 的 run 命令，仍传实际240请求、该文件 SHA 和独占 namespace。16:32:20.3899495Z 返回 request240_actual_science_return：

| 已返回字段 | 原值 |
|---|---|
| actual_exit_code | 1 |
| rules_returncode | 1 |
| science_returncode | 1 |
| resource_stop | null |
| external_signal | null |
| owned_processes_quiescent | true |
| execution.file | /home/runner/work/_temp/visible-live128-root-synthesis-product-projected-model240/execution.json |
| execution.bytes | 2683 |
| execution.sha256 | 0babd92f9ea45c92db941183d9a408d0d0196a7b895f431907384242e89d8018 |

16:32:20.3997521Z，shell 原样报告 exit code1。这一实际外层事件没有给内层 exception、call number、最后 H、owner residual、接受步、stage地址或完整 root counters。

resource_stop=null、external_signal=null 只是该外层返回的原值，不等于全部内层组件都没有资源停；owned_processes_quiescent=true 是该外层关闭算法已返回的总状态，不是未传回的逐 PID/startticks 记录全文。不得从这组 null/true 推导 timeout、OOM、数学拒收、某个原门已通过或未访问。

14:36 至16:32的墙钟跨度包含完整实际工作和关闭流程，不是单一 root、J、stage 或 R572 优化的独立计时。没有返回分项成本，不能由累计时间预测已付进度或速度收益。

## 5. 源码必要读回：350903 bytes 正文未传回

compute 在 16:32:21.7497614Z 至16:32:21.7512391Z 打印唯一源码帧：

BEGIN_R573_SYNTHESIS_PRODUCT_PROJECTED_MODEL_SOURCE_PREPARATION_NECESSARY

至对应 END。实际 JSON body 含末尾 LF 为1846 bytes，SHA-256 eeff2a1da5984946b8bafe342964be521b5b5d1f4f7f3d60a5450174175d04c2。

16:32:21.8615287Z 的 request240_one_source_necessary_transport 确认 actual_reader_exit=70、同 bytes/SHA、necessary_readback_complete=false、scientific_success_not_inferred=true。16:32:21.8663454Z shell 退出70。report 的 source_report_identity 于16:32:29.6362115Z 再核同一个1846字节 body。

以下列齐该返回描述符的语义内容，长 SHA 全部为本 job 实际值：

| 字段 | 本次原值 |
|---|---|
| schema | R573-root-synthesis-product-current-owner-projected-model-source-preparation-v1-necessary-v1 |
| request_number | 240 |
| run | GITHUB_REPOSITORY=Rogerhu12/math-research-public；GITHUB_RUN_ID="43887312387"；GITHUB_RUN_ATTEMPT="1"；GITHUB_SHA=bce880e0037870ce0977abc5d54d0cf2bd24d2cd |
| necessary_readback_complete | false |
| source_preparation_complete | false |
| transport_exit_code | 70 |
| attempted_bytes | 350903 |
| attempted_sha256 | 4478a5ebfe6c65a8b28eb8c855a7b21a8243385b1adeaa7013ff9bfb3fb6b29e |
| complete_local_necessary_object.file | /home/runner/work/_temp/request240-source-preparation/necessary-source-overflow.json |
| complete_local_necessary_object.bytes / sha256 | 同上350903 / 4478a5ebfe6c65a8b28eb8c855a7b21a8243385b1adeaa7013ff9bfb3fb6b29e |
| original_R565_readback_exit | 70 |
| original_R565_transport.file | /home/runner/work/_temp/request237-source-preparation-necessary.json |
| original_R565_transport.bytes | 1837 |
| original_R565_transport.sha256 | f3d9392bc92424ddc488376ff8f2b01dc20e8e3f19d3e54cfd9ea5295a2173f1 |
| original_R565_complete_necessary.file | /home/runner/work/_temp/request237-source-preparation/necessary-source-overflow.json |
| original_R565_complete_necessary.bytes | 286365 |
| original_R565_complete_necessary.sha256 | 372dfd68a524ebad1b32bd8c7750af70907b29c38aeaff295b8ac2eaffb66948 |
| cleanup_permitted | false |
| no_segments_or_encoded_raw | true |
| numerical_success_not_inferred | true |

source.file 的实际前缀为 /home/runner/work/math-research-public/math-research-public/topics/visible-flex-larger-amplitude/computations/，后接§2生成器；bytes38611及 SHA3bb1084d…为§2所列完整身份。plan.file 为同一实际 topic 下 notes/r573-live128-synthesis-product-projected-model-complete-source-plan.json，bytes82812/SHA85fdec3e…也与§2一致。这些是完整返回描述符中的实字段，不使用另一预览来源替代。

### 5.1 同 job 的 R565 祖先正文不能冒作 actual237 的旧输出

request237-source-preparation 是 **actual240 这一个 job** 调用冻结 R565 祖先代码所使用的目录。这里的286365/372dfd68…与1837/f3d9392b…均为本 job 的文件身份，不能用 R566 所记录 actual237 的同名路径、同长度或另一个 SHA 补内容。

固定 R573 readback 真实调用 R565 reader；child70 时，要求原 transport.exit70、necessary=false，并核其固定 same-job overflow 路径、完整 bytes/SHA 与实际正文。祖先旧70和原false保持；当前层随后将其完整对象按固定具名来源表纳入当前选择。这是已读源码的控制流，不是作者假定祖先返回0，也不等于作者已取得祖先全部正文。

本次 fallback 返回 original_R565_readback_exit=70、transport 和 complete_necessary 的实际身份。它没有保留足以外推祖先完整对象内部 necessary_readback_complete、metadata errors或每项安装状态的值。不能因身份已取得而补造这些内容。

### 5.2 两个不同的 complete 字段必须分别解释

R573 readback 起初读取本 job 当前 source-views.json，核 schema/run/source/plan，再令 source_preparation_complete=current.complete。它按原程序形成完整当前选择，保祖先读回、完整 stderr、错误、未生成 suffix、source inventory 和 literal 来源。

随后 canonical(result) 若大于 LIMIT=90000，原源码将完整对象写入当前 necessary-source-overflow.json，再建立新的 transport fallback。这个分支**字面设置** necessary_readback_complete=false、source_preparation_complete=false、transport_exit_code=70，保当前尝试身份和祖先的 exit/文件身份。

故本次 source_preparation_complete=false 是超限 transport 的保守表示；§3实际 source prepare complete=true/exit0 同时成立。把 fallback.false 当成“生成器失败”“R572源不存在”不符合该源码；把 prepare.true 当成“完整350903字节已读”也不符合实际范围。

当前 body 并未返回完整 current_source_record、具名共享表、所有编译 binding、全部错误或未生成地址。本文不按其350903长度猜占比，不把另一次来源超限的对象拿来当 fixture，也不借所指 SHA 重建原已销毁文件。

## 6. 科学必要读回：221520 bytes 原选择未传回

compute 在16:32:22.1984949Z 至16:32:22.2001736Z 返回唯一科学帧：

BEGIN_REQUEST240_SYNTHESIS_PRODUCT_PROJECTED_MODEL_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY

至对应 END。body 含末尾 LF 为1163 bytes，SHA-256 9c3983b801fdb7a0a929bfe2daf4e110f8744d890830c87725342b71900c10bb。

16:32:22.3105594Z transport 事件确认 actual_reader_exit=70、同 bytes/SHA、necessary_readback_complete=false、scientific_success_not_inferred=true；16:32:22.3154474Z shell退出70。report 于16:32:29.6757878Z 再核同字 body，并保 compute_result="failure"。

| 已返字段 | 实际值 |
|---|---|
| schema | R573-live128-root-synthesis-product-projected-model-original-full112-necessary-v1 |
| request_number / run | 240 / §1同一仓库、run、attempt、head |
| request.file | /home/runner/work/math-research-public/math-research-public/topics/visible-flex-larger-amplitude/computations/public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request.json |
| request.sha256 | e4ad6178a06d2cf270f3469c4cbcce4747c8876e7c95c50f829be58c9f6c437a |
| actual_original_necessary_summary.file | /home/runner/work/_temp/visible-live128-root-synthesis-product-projected-model240/necessary-summary-overflow.json |
| actual_original_necessary_summary.bytes | 221520 |
| actual_original_necessary_summary.sha256 | 64da8ede38e3d1abb05c0b7404f1c6f3c2ac7eaca4783273bb7861c18e54adfe |
| cleanup_permitted | false |
| necessary_readback_complete | false |
| transport_exit_code | 70 |
| no_segments_or_encoded_scientific_tree_returned | true |
| scientific_success_not_inferred | true |
| unreturned_scope | The complete selected necessary object exceeds90000 bytes; scientific and error contents not replaced by a success view |

这里的科学必要 reader 保原完整选择及具名表，但本次全部221520字节未能在单份90000上限内返回。1163字节已经完整读到，仅证明这些描述字段，不等于原221520字节已读到。不能将未返回对象替换为空对象、全false、只有错误、只有成功或只缺源表。

仍未返回的具体责任包括：

1. 实际第一/后续 H、call 数、当前真实输入、初猜或 predictor 使用位置、接受迭代、最后 residual 与未完节点地址。
2. 实际 owner compiler/hook 安装、source binding 完整体、fresh replay、当前128值及十六进制原权威字段。
3. R572 exact_root_synthesis_products 五路径各17完整计数/full last，以及原 R564、R561、R550、R535 全部统计与未完位置。
4. 同次 RN64 全状态、完整576 cell模型、每个226×224 before-port、224×224 after-port、两mean及原338×112响应的实际形成和进展。
5. 原 boundary、endpoint、audit 的真实返回；原FD两组各10方向及全部层；fullDN与最后 same-current-H fresh audit 的原门。
6. 内层 exception/traceback、每组件原资源状态、原过程记录、逐 PID/startticks/owner 详情与完整错误选择。

以上列的是既有责任，不是新增验收门。尤其保留原混合338×112合同，不把全解析J强加为原门；也不把当前模型与128程序导数相等设为新门。原 noJ、预测器、同H缓存和初猜机制是否实际访问，必须由本 run 的完整内部记录付，不能从它们已存在于源码而推本次已完成。

## 7. 实际 quiet、清理与 report

§4的科学外层已真实返回 owned_processes_quiescent=true。workflow 的 cleanup 还要求 SOURCE_READBACK_COMPLETE 与 NECESSARY_COMPLETE 同为true，才委托原 runner 的删除分支。

本次两个必要范围均false。16:32:22.3975747Z，request240_cleanup 返回：

- removed=false；
- namespace=/home/runner/work/_temp/visible-live128-root-synthesis-product-projected-model240；
- reason="source or original-science necessary scope incomplete; raw retained until runner destruction"；
- no_scientific_completion_or_quiet_inferred=true。

官方 step14=success 表明这个**保留分支**执行并返回，不是数据已删除或读回已完成。quiet总状态与cleanup保留分别陈述，不能以cleanup最后字段反向否定§4的quiet事件，也不能以quiettrue跳过两份必要范围。

原临时目录只保留到runner destruction；本文没有调查之后能否访问，不承诺恢复，更不把身份散列当原文件字节。原主树不保存这些可再生科学raw。

report job 两步分别核并打印这两份原transport。source frame1846字节、science frame1163字节均与compute逐字一致；原compute_result=failure真实保留。report成功只是其已声明传输任务完成，并未产生另一份完整source或science对象。由job名称、标签或打印成功推native/fullDN接受，均超出实证。

## 8. 本次可用结论与尚未支付的范围

本次独立付出的运行事实是：固定240源在实际同job完成源码prepare和447绑定、原输入prepare；科学外层返回1并关闭其受管进程；完整source和science必要选择均超过90000而返回70；实际返回的两描述符在compute/report完全同字；清理保留了原namespace而未删除。

本次未付的是完整source读回与科学内部终因/数值结论。原source/math条件命题不因传输失败而被反驳；它们也不能替本次未返回的实际计数、残差、门或性能证据。R566是另一次actual237运行，R574保持自己的run/source/hash及同job祖先身份，不拼成一条未经执行的延续链。

后续表示改进应完整保原source选择与原科学选择、实际失败和未访地址、全部数字字值和缺失/null区别，并继续原90000/70。本文不删字段、不提高上限、不将descriptor升格、不发起重跑、不改变已冻240或任何正在跑的输入。新的实际run应按其自身来源和原门独立归责。

## 9. 固定可核验来源

- [actual240官方run与两job](https://github.com/Rogerhu12/math-research-public/actions/runs/43887312387)，终态读取及解码身份见§1。
- [实际240请求](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/topics/visible-flex-larger-amplitude/computations/public-live128-root-synthesis-product-projected-model-original-full112-FD-fullDN-request.json)。
- [R573完整source计划](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/topics/visible-flex-larger-amplitude/notes/r573-live128-synthesis-product-projected-model-complete-source-plan.json)。
- [R573实际source生成及必要reader](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/topics/visible-flex-larger-amplitude/computations/root_20261116_live128_synthesis_product_projected_source_views.py)，完整readback中祖先70/overflow身份、本层保守fallback和90000限制。
- [冻结240workflow](https://github.com/Rogerhu12/math-research-public/blob/bce880e0037870ce0977abc5d54d0cf2bd24d2cd/.github/workflows/visible-larger-public-live128-root-synthesis-product-projected-model-original-fullDN.yml)，两独立必要步骤、原report和有条件cleanup。
- [R572条件证明](R572-exact-root-synthesis-products-and-original-sum-order.md)及[R566另一实际237终态](R566-actual237-source-and-science-readback-overflow.md)，分别用于来源和区分旧run，不代本次未读值。
