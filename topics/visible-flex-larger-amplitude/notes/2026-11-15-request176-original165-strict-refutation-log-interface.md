# Request176：actual165原38条严格反例的只读日志定位

这是独立的Actions元数据读回任务，补R356中尚未亲读的38个具体u区间。它只读取已经完成的actual165日志；不重跑C、cut、R323、factory、区间包围、profile、导数、FD或native，不计算新的有理数/浮点差、范数、多项式或域不等式。175及其他求解不以它为前置门。首跑真实限制已记录为R374；本修订只改必要metadata布局/输入格式诊断，不预填仍未返回的38条位置或bounds。

## 1. 唯一原来源

固定原run43736208020，source1f2ec637430e5c6b27b1a93720e106539281a156，compute job132879253906。该job原target返回exit4；其reported source是94125B / 61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205 的 root_20261115_continuous_nine_shared_target_enclosures.py。

已完成的report job132897872239原日志417817B / 82b5a074e953159c069d8a7886319be97e0b37a81aeab7b9d14a7c2d3e6cf64d已被读取，176不再次下载它。报告中的原完整target result为105512B / e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619，canonical ASCII包含最后LF，原compute以complete-target-result标签的9个片段保存。新reader必须从原compute日志恢复这一实际原对象并核全部原bytes/SHA、run/source/schema/source-file身份，不能用重新序列化的猜测结果替换它。

原report只给出全范围、计数和原界；不含38条全部位置。R356已明确没有读取巨compute。176对巨compute只做一次官方流式下载和顺序扫描，实际总bytes/SHA在本次读回中形成；事先未知的完整log hash不会伪造。

## 2. 冻结四件

| 文件 | UTF-8字节数 | SHA256 | 小文本blob |
|---|---:|---|---|
| root_20261115_read_actual165_strict_refutations.py | 32670 | `2e5717de6c1d00059e995f398384bd5758f9e2c8f2657484bd651d66cf950371` | `fc17fe82d7e24365c31898f29bac37abc711cfc6` |
| public-actual165-strict-refutations-readback-request.json | 7083 | `3ba3e2a207476c7596a06f42df8e46dd11255d13ba5140a72780bbe4605a2b7b` | `9d87a6b05e902ccea0f7d4586e76c152caada03e` |
| visible-larger-public-actual165-strict-refutations-readback.yml | 6477 | `41fe2cdf8bce4dbcd2577c2a2566fb14a4538ff0a6f710caad99fe50321140f6` | `b75fe165e07ed6e92d337ce46434fa006a3b3585` |

接口另给自身最终身份。只有新reader和原165 emitter源码参与源码字节核；旧94125B源码仅read_bytes/hash，绝不import。其余C/数学闭包不被重新执行，也不把旧科学source hash冒成本次科学计算。

## 3. 原源确已保存哪些定位

原61b98的最终cover循环逐叶输出：

~~~
event = request165_final_complete_cover_leaf
record = 当前完整原叶
~~~

对每个未决或严格反例，原循环继续输出：

~~~
event = request165_full_pending_or_refuted_interval
record = {
  numeric_piece, closed_public_u, depth, node_id, reasons,
  retained_complete_enclosure,
  classification, terminal_reason
}
~~~

因此原38条各有实际u两个准确字符串端点、原数值piece、深度、node_id、原因和完整原包围。完整原对象与原final-cover的逐字联结只在Actions内部处理；新摘要只返回38条位置、classification/reasons、必要原accurate_a与accurate_as两界及原radius/speed反证布尔，附完整pending/enclosure与原事件bytes/SHA。ass、差值、目标和其余大包围不重新输出。

它同时找同一个node的原final-cover对象，要求canonical原数字词法完全相同于pending的retained_complete_enclosure；保两处原事件SHA、日志行号、原raw行byte offset、原raw行SHA。键是完整(node_id,numeric_piece,lo原串,hi原串,depth)，不解析lo/hi为有理数、不比较区间端点，不按近似站点合并。

相同节点若重复出现，保每次出现的原位置和字节身份，必要反例行只输出一次；不重复发送完整enclosure。相同身份但完整字节不同是读回错误，不能悄选其中一份。最终唯一反例节点集合必须等于原最终cover中的反例集合；这是原记录联结，不是新的数学判定。

## 4. 原科学数值不经本地或Actions再算

reader使用LiteralNumber保存每个JSON number的原token。canonical编码把该token逐字放回，原大整数界本来是字符串的仍保字符串。所选闭区间、a/as包围与理由的原token全部原样保留；完整其余字段仅在Actions内部字节核对，不构造成新的科学输出表。

程序没有import numpy、flint、fractions、任何科学源，也没有对a、as、P或delta做数值比较。严格反例选择只使用原classification和原accurate_domain_rigorously_refuted布尔。原已报告38条是否数学上正确仍依原165/R352来源，不由176重新证明；新的工作仅把其原字面证据定位出来。

对另外32488条原unresolved记录只做字符串和整数元数据计数：

- 原reason逐项计数及原完整reason-list组合计数；
- 原numeric_piece计数；
- 原depth计数；
- 原pending/refuted总数。

这些计数不产生新的科学界，也不把reason“宽度未决”改为真正域失败。65535个已评节点的大系数表不重新读成数学对象、不重新审计每个界；全log SHA仅表示完整运输的原byte范围。

## 5. 真实全流与认证边界

流程先用官方API核原run已经completed、head_sha确为固定source，再核job已经completed且run_id一致。API元数据本身保bytes/SHA与实际status/conclusion。

原job logs endpoint只打开一次。token只来自GH_TOKEN/GITHUB_TOKEN进程环境，只发给api.github.com；如果官方返回签名HTTPS redirect，后续请求不带原token，签名URL不写日志或文件。reader不使用用户PAT，也不建Git凭据文件。

HTTP原response要求identity编码，逐原字节更新SHA和bytes，检查实际Content-Length（存在时）。整个log不落盘。原timestamp前缀只在选取JSON事件时剥离；原行SHA与全流SHA仍覆盖timestamp和原换行。最终全流必须到EOF；预算只得到prefix时明确full_log.complete=false。

原metadata分段协议也按61b98真实格式复用：begin给label/bytes/SHA/segments；segment给index和完整ASCII data。相关label严格按原顺序拼接，核长度和SHA，不从hash反建文本；缺segment/错序/错hash均保明确错误，不能声称完整。无关大grid转换或科学表不重新打印。

原日志含完整当前cover32977叶和pending/refuted32526记录。reader将实际扫描计数与恢复的同一原fullresult字段、已读report计数相对照；38条必须完整，32488未决概要必须完整。不同结果不被“纠正”成预期数，而是读回未完成并保实际已见记录。

## 6. 唯一有界摘要，不搬大原对象

reader在扫描期间不输出逐条科学对象，也不建立任何新的begin/segment/reassemble输出协议。只在结束时输出一份真正不超过90000B的ASCII JSON摘要，包含：

- 原官方run/job、完整log或实际prefix身份；
- 原105512B target result身份、关键原flags与范围计数；
- 全38条node_id/numeric_piece/闭u两端/depth/classification/reasons及必要原a/as严格反证bound；
- 每条完整pending/enclosure、原事件与原日志位置的bytes/SHA，重复事件仅metadata；
- 原32488未决的reason组合、piece和depth计数；
- 未完原输入segment、malformed相关行及reader实际错误；
- 实际原科学exit4与独立reader状态，双方不互相重标。

原完整result及完整enclosure仍严格按原字节在Actions内部核对。输入旧165日志必须使用其已有分段协议才能恢复原对象；这不授权新输出再次分段发送科学见证。

若必要摘要实际超过90000B，原内部扫描结果可保为RUNNER_TEMP文件，但返回明确summary_complete=false、transport_complete=false、readback_complete=false、exit70以及未返回范围。不会用hash宣称38条已完整返回，更不会拆包绕过上限。original_internal_scan_complete单独保留实际扫描是否完成，不改原科学结论。

stdout摘要写完才记录对应bytes/SHA的summary-stdout-complete.json。always步骤只在摘要此前未完整打印时打印同一份有界对象；已有相同身份时只打印小receipt，避免重复。任何实际传输异常不会留下成功cleanup标志。

## 7. 预算、错误与临时文件

该纯读回预算1500秒、原log最多4294967296B；原单行最多1048576B、相关单语义record最多4194304B。单step30分钟、job35分钟。没有宣称原log一定小于某值或传输一定在预算内结束。若实际超过，resource_partial或错误明确保留实际prefix与已见38子集，不补剩余记录。

任务只用Python3.12.14标准库，无pip科学依赖。35分钟job短于45分钟规则周期；启动逐字核根21bd547f56590b7f2dd279d0297efb289a9b2783和课题bff8aea253a9e6a7a4fac28d810ac454c5499fec。contents/actions都只读，没有H写入、GitAPI提交或科学checkout修改。

临时目录仅有结果/摘要和stdout receipt；原巨log从不存文件。必要原位置、bound与错误只经最终有界摘要返回；always步骤只读已留的同一摘要，不重下载、不恢复输出大对象。cleanup要求原reader step真实success且readback_complete/transport_complete均true；失败保小对象到runner销毁，不能把清理成功冒科学成功。

无upload-artifact、Release或Git raw输出。可公开的只有脚本、参数、run/source/SHA和R374紧凑结论。

## 8. CLI、源检查与未付范围

~~~
python -u root_20261115_read_actual165_strict_refutations.py \
  --request "$VISIBLE_COMPUTATIONS/public-actual165-strict-refutations-readback-request.json" \
  --code-directory "$VISIBLE_COMPUTATIONS" \
  --out "$RUNNER_TEMP/visible-actual165-refutations-176"
~~~

工作流独立trigger/concurrency，cancel-in-progress=false，不动原165或175。固定request SHA 3ba3e2a207476c7596a06f42df8e46dd11255d13ba5140a72780bbe4605a2b7b，reader SHA2e5717de6c1d00059e995f398384bd5758f9e2c8f2657484bd651d66cf950371。新源码仅文本成文和SHA核；未本地AST、import、下载巨log或科学执行。公开Actions的正常ast.parse检查文本语法，绝不增加科学fixture门。

现在尚未取得这38个实际位置，不能据此选择某个新的形状/参数或局部细分。176实际读回后才可用原u/piece/support信息判断具体下一调整；它本身不调整九参数、不证明新域、不恢复已删场，也不是任何原模型或native接受条件。

## 9. actual176 后的明确修订2

首跑实际run43746302206/source97a99672e779d4b1f4aadcdb6adb6c7198187378/job132910242777内部找到38唯一节点，但完整计数扫描为32667 cover、32480 pending、32442 unresolved，未达到绑定原32977/32526/32488。原reader保完整count检查并报ValueError；必要摘要95577B超界，最终只返2388B明确70。R374保留该真实失败，不能用本修订覆盖它。

新输出schema为 actual165-original-log-selected38-bounded-columns-readback-v2。所有原finish检查正文逐字保留，不更改原目标计数，不降低原字节核对范围。selected38_full_enclosure_links_observed/complete_necessary38_table_returned与readback_complete分开：若将来仍是计数不齐，允许真实已找到且逐原enclosure联结的38行出现在≤90000B失败摘要内，同时完整count状态仍false/reader非零。没有把此布局变化写成科学成功。

38行改为一次columns+原行数组，公共reasons和terminal_reason各只列一次，去除重复node_id和同一enclosure/row SHA副本。每行仍保原u两端、piece、depth、分类、原a/as准确上下整数和各自binary_exponent、原radius/speed反证布尔、pending/enclosure完整bytes/SHA及两处原log/event位置身份。没有删掉反证必要字段或重新评估不等式。

新输入观察仅把event冒号周围合法JSON空白纳入词法识别，记录原event和分段label分布，以及最多12条相关但非JSON-object前缀行的bytes/SHA/位置，不返回其科学正文。原emit_segments对大final-cover/pending仍使用同event字面label，当前白名单已覆盖；尚无证据将310/46差额归于某个未覆盖label。因此这些新计数只供定位真实输入格式，不自动补事件、不预判日志丢失。

原旧日志全字节在Actions再流式一次；先前1486048285B/4ab8c6d688a27869353bb428288d467502c7aed6ad8cd96140a6cfaea508aea2仅为actual176实测来源，新的下载仍独立记其完整或prefix身份。新请求仍1500秒/4GiB/35min，90000B上限和禁止输出分段完全不变。若必要表仍超界仍70/readbackfalse，不提供完成保证。没有本地AST、日志下载或科学执行，也不重跑165科学。

## 10. 官方拼接日志的行首 BOM 解析

实际170官方job132896377831的完整log为4443980B/SHA429a69f20aecbe99dbffe13c72168243bebc4b716da000c3300c03570fb4df71，内部直接观察到3个UTF8 BOM。某行以BOM再接timestamp和原JSON起始；仅先用timestamp正则会漏掉该行。去除每一原物理行开头的单个BOM用于解析后，原170全部8个语义document及1230个member的各自原bytes/SHA完全核回，包括原Hermite_transfer[364]。这是已观察的日志格式事实，不是165差额的预定解释。

176r2仅在解析副本先识别并剥去该3字节前缀，再执行原timestamp/JSON逻辑；原log_hash、total_bytes、raw行SHA和byte_offset均先按原行处理，保持BOM在完整原字节身份中。新utf8_bom_prefixed_raw_line_count只记录实际观察数。没有宽松吞任意前缀、没有改变任何原科学值或finish计数断言。若165还有其他缺口，仍原样返回计数未完成和已找到38条的独立状态。
