# Request176：actual165原38条严格反例的只读日志定位

这是独立的Actions元数据读回任务，补R356中尚未亲读的38个具体u区间。它只读取已经完成的actual165日志；不重跑C、cut、R323、factory、区间包围、profile、导数、FD或native，不计算新的有理数/浮点差、范数、多项式或域不等式。175及其他求解不以它为前置门。未来真实结论编号R374，当前不预填任何38条的位置或bounds。

## 1. 唯一原来源

固定原run43736208020，source1f2ec637430e5c6b27b1a93720e106539281a156，compute job132879253906。该job原target返回exit4；其reported source是94125B / 61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205 的 root_20261115_continuous_nine_shared_target_enclosures.py。

已完成的report job132897872239原日志417817B / 82b5a074e953159c069d8a7886319be97e0b37a81aeab7b9d14a7c2d3e6cf64d已被读取，176不再次下载它。报告中的原完整target result为105512B / e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619，canonical ASCII包含最后LF，原compute以complete-target-result标签的9个片段保存。新reader必须从原compute日志恢复这一实际原对象并核全部原bytes/SHA、run/source/schema/source-file身份，不能用重新序列化的猜测结果替换它。

原report只给出全范围、计数和原界；不含38条全部位置。R356已明确没有读取巨compute。176对巨compute只做一次官方流式下载和顺序扫描，实际总bytes/SHA在本次读回中形成；事先未知的完整log hash不会伪造。

## 2. 冻结四件

| 文件 | UTF-8字节数 | SHA256 | 小文本blob |
|---|---:|---|---|
| root_20261115_read_actual165_strict_refutations.py | 28097 | `07d3b2608bf4f9614ed74465ddb40f068f130f69f1e5208912bfc3ab6bddb631` | `f683958d69697e0ca5e38ca9723addf17fe56c76` |
| public-actual165-strict-refutations-readback-request.json | 5217 | `c0e938965b9f4824e58d7d302d7d66bd65e88c38cb055a5b73aa289ed81529ec` | `8359877fe39bc9dc76569563db3116ff3cecf4e6` |
| visible-larger-public-actual165-strict-refutations-readback.yml | 6477 | `3919128037850ae017676bb7e35f008aefec9e1bc44f51969fe8212a09ee23ad` | `bf2764be0dfd9e989db19c9e92fc5962112ffc2b` |

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

工作流独立trigger/concurrency，cancel-in-progress=false，不动原165或175。固定request SHA c0e938965b9f4824e58d7d302d7d66bd65e88c38cb055a5b73aa289ed81529ec，reader SHA07d3b2608bf4f9614ed74465ddb40f068f130f69f1e5208912bfc3ab6bddb631。新源码仅文本成文和SHA核；未本地AST、import、下载巨log或科学执行。公开Actions的正常ast.parse检查文本语法，绝不增加科学fixture门。

现在尚未取得这38个实际位置，不能据此选择某个新的形状/参数或局部细分。176实际读回后才可用原u/piece/support信息判断具体下一调整；它本身不调整九参数、不证明新域、不恢复已删场，也不是任何原模型或native接受条件。
