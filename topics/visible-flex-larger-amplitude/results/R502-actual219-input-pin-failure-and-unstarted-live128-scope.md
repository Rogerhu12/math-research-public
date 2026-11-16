# R502：actual219 的输入身份失败、静止判定范围与未启动的 live128 全责任

作者：ChatGPT（AI），2026-11-16 UTC。

可信度范围：本结论依据 actual219 两个官方终态 job 的唯一一次原日志读取、两份逐字相同的必要对象、已发表的原 request/source 控制流，以及原204/208中既有输入身份。这里没有执行新的数学计算，也没有把绿色 report、source syntax 或部分准备工作解释为科学成功。

## 502.1 真实运行及本次结论

actual219 没有进入 live128 科学步骤。准备阶段先在 frozen ledger-ready 的字节与 SHA 检查处失败；随后必要读回因过宽的进程归属扫描而未能证明 quiet；最后 cleanup 的 shell heredoc 存在实际语法错误。三件事分别记录，不能用后二者覆盖第一个输入错误，也不能把它们解释为原有限问题、binary128 方法或 fullDN 的数值拒绝。

| 项目 | 原记录 |
|---|---|
| 仓库 | Rogerhu12/math-research-public |
| 实际 source/main | f0c787340f29734e17c9428ba7588e2a58ae665e |
| run / attempt | 43832887523 / 1 |
| 触发 | workflow_dispatch，main |
| 创建 | 2026-11-16T08:38:35Z |
| workflow_id | 419898247 |
| compute | 133182240807，completed / failure |
| report | 133182459836，completed / success |
| request | public-live128-original-full112-FD-fullDN-request.json，52615 B / 1c9400110f65f5930f833142a85a48ce389df7f652c385fd2435676c369b251b |
| 原必要对象 | 2101 B / 074caaa8dfed72b2b3e304950829128711d34e8aa18e03b5ff8ad33b1b802dee，包含末尾一个 LF |

官方入口：[run43832887523](https://github.com/Rogerhu12/math-research-public/actions/runs/43832887523)，[compute133182240807](https://github.com/Rogerhu12/math-research-public/actions/runs/43832887523/job/133182240807)，[report133182459836](https://github.com/Rogerhu12/math-research-public/actions/runs/43832887523/job/133182459836)。

compute 的 source binding、普通 Python/Node 语法及容量步骤已成功；第9步准备失败，第10步科学被跳过，第11步必要读回失败，第12步清理失败。report 仅成功转发已有的小必要对象。必要对象本身明确 necessary_readback_complete=false、fullDN_accepted=false、task_completed=false，故 report success 不提供另一种科学结论。

## 502.2 原日志和返回对象的证据身份

两份 job 日志各只通过官方 connector 获取一次。以下 SHA 适用于工具返回的完整已解码文本重新编码为 UTF-8 的字节；不冒称 GitHub HTTP 压缩流或重定向响应的原字节身份。

| 完整工具返回文本 | UTF-8 bytes | SHA256 |
|---|---:|---|
| compute133182240807 | 53633 | af8494a95d16967000e82d9695b8beb3ed5ed0805814c4fbdbc99c4b8d11be66 |
| report133182459836 | 9164 | 889a463e3d46c70cd02aa8b60548f658fe6eeba0587e15f5d8d7ce80260d1c11 |
| compute/report 中的同一必要 JSON，含一个 LF | 2101 | 074caaa8dfed72b2b3e304950829128711d34e8aa18e03b5ff8ad33b1b802dee |

解析视图只对每个物理行处理已识别的行首单个 BOM 和锚定的时间前缀；没有改变留存的原日志文本。两 job 的必要 JSON 按上述字节口径完全相同。未拆包、未从某个 SHA 还原不存在的科学正文，也未第二次下载日志。

compute 日志首末时间为 08:38:39.3086353Z 与 08:39:03.7816937Z；report 为 08:39:09.0519663Z 与 08:39:09.2597853Z。这些只是所读日志的首末时间，不是数学步骤计时或 runner 销毁时刻。

## 502.3 已完成的来源和容量准备

08:38:59.1819114Z 的 request219_source_binding 记录实际 request SHA、实际 source head 和334个 source 身份。该步骤进行普通 Python 编译检查而不导入，Node 语法检查而不执行科学；记录明确尚未进行 C++ 科学编译或科学求值。334项在这个阶段核同，不能由此称后续所有动态来源和所有运行输入均已取得。

08:38:59.3066710Z 的 request219_declared_capacity 记录：

| 字段 | 原值 |
|---|---:|
| total | 154993672192 |
| used | 62957744128 |
| free，before 和 after 相同 | 92019150848 |
| minimum_free_bytes_at_start | 68719476736 |
| maximum_uncached_protocol_calls | 18 |

unused_ephemeral_runner_SDKs_removed 为空；scientific_payload_deleted=false。原 all_possible_calls_fit_not_proved=true，original320_minute_clock_not_started_yet=true。故本次不是已到19200秒科学预算、磁盘阈值或二进制精度上限后停止；容量记录也没有保证最多18次调用都能完成。

## 502.4 第一实际失败：原 ledger-ready SHA 少一个字符

08:39:03.3028926Z 的 request219_preparation_return 原事件返回：

- complete=false，phase=source-binding；
- error.type=ValueError；
- error.message 为 “Original input bytes and SHA are unchanged: 2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json”；
- traceback 位于已发表 outer runtime 的 prepare → exact_git_input → require。

确切原检查是先核历史 path 的 Git blob，再取得 git show 原字节，然后要求长度与 hashlib.sha256(raw).hexdigest() 同时等于 request 中的原字段。失败消息来自后一个长度/SHA 联合检查。

### 502.4.1 对 R501 接口原表的明确勘误

actual219 request，以及 R501 原接口的 ledger-ready 表项，误写了以下63字符值：

~~~text
563a99973230a7f15d1c1ba8537eda34bc02158a0cfff90160d37f57e3ab2f6
~~~

原204和原208冻结合同中，针对同一路径、同一 Git blob、同一109004 B原输入，完整64字符 SHA256 均为：

~~~text
563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6
~~~

差异是前一个值在 eda 后遗漏了一个 e；正确片段是 edae34。不是另一个 ready 文件、另一个 root 选择、重新生成的数据或输入升级。

| 原输入身份 | 不变内容 |
|---|---|
| 环境键 | VISIBLE_FLEX_FROZEN_LEDGER_READY |
| 路径 | topics/visible-flex-larger-amplitude/notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json |
| historical commit | 8bd267107cc8710d371f3b62c02986655ac965b0 |
| Git blob | 4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3 |
| bytes | 109004 |
| 正确 SHA256 | 563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6 |

此处正确 SHA 的来源是原204及原208的 frozen_geometry_inputs.files 中既有完整记录，本次实际日志没有打印所取 raw 的 SHA。不能把原合同的正确值伪称此次 guard 输出的实测值；不过63字符字符串不可能等于 sha256.hexdigest() 的64字符输出，所以所示错误字段本身足以解释这次检查必然不能通过。

原始 R501 接口21110 B版本及 actual219 request/workflow/source 保留在 f0c787340f29734e17c9428ba7588e2a58ae665e 历史；本条是公开勘误，不追改219输入，也不把 [R501](R501-live128-original-full112-same-call-executable-composition.md) 的条件构造倒填为已执行。原接口入口为 [request219 interface](../notes/2026-11-16-request219-live128-original-full112-interface.md)。

### 502.4.2 本次取得与未取得的边界

准备事件保留 preparation.json 的原身份：55039 B / 235497c8e2096a27c61e512173e8e99edcea61b4ec0c8e2c1e7a6429148429ac。该文件完整正文没有在本次必要对象中返回；这里直接读取的是原 compute 事件所带的错误、traceback 和 receipt，不能声称已读其全部 source/input 子表。

按发表源中的顺序，accepted、warm、warm_status 和 tail_config 位于 ledger-ready 前；到达第五项的该检查，意味着前四次 exact_git_input 已返回。这是控制流推论，不能替代四个实际 receipt 的完整读回。ledger-ready 失败后，stored-ready、decoded warm-status 后处理、原 port 对象输出、public78 source restoration、actual91 artifact 及 seed binding 均未到达其后续代码。

特别是 actual91 尾场只拟作下一次当前 H 求解的初猜；本次连此尾初猜的恢复阶段都未开始，不能把它或 actual63 暂存输入称为一个新 live128 响应。

## 502.5 第二实际失败：quiet 扫描范围过宽

原必要对象中的 original_quiet 返回：

~~~json
{
  "registries": [],
  "groups": [],
  "remaining_owned_processes": [],
  "unknown": [
    {"pid":1165,"reason":"PermissionError: [Errno 13] Permission denied: '/proc/1165/environ'"},
    {"pid":1182,"reason":"PermissionError: [Errno 13] Permission denied: '/proc/1182/environ'"}
  ],
  "quiescent": false
}
~~~

本次没有已登记的 rules/science/worker 组。旧 outer quiet 在已知 registry 处理之外，对同 uid 的进程读取 environ；两次 PermissionError 被直接列入 unknown，而此前没有给这两个 pid 建立已登记 pid/start-time、pgid/sid、实际后代或可读 namespace 归属证据。此处证明的是旧扫描未能确认自己的静止条件，不能据此说两个进程属于219、仍在写科学文件，或原 native 泄漏。

必要 reader 因 quiescent=false 在读取科学文件前返回，原字段为：

~~~json
{
  "necessary_readback_complete": false,
  "scientific_files_read_after_unproved_quiet": false,
  "transport_error": "Actual owned processes are not proved quiescent",
  "fullDN_accepted": false,
  "task_completed": false
}
~~~

实际 reader exit 为3。2101 B没有超过90000 B；这次不是摘要超限70，也没有通过截断掩盖未读部分。外部 report 转发同一对象，仍保这个失败。

后继修复的边界应是“对本请求真实所有或有具体所有权证据的进程不能证明静止”，而不是“整个同 uid 的每个进程都必须能读 environ”。已登记或可疑 owned 进程不可读时仍须保 unknown、禁止读删；不允许普遍忽略 PermissionError。反之，一个没有所属组/真实后代/可读 namespace 证据的外部同 uid 进程，不可仅因其 environ 不可读而冒称本请求所有。

## 502.6 第三实际失败：cleanup shell 未被成功解析

08:39:03.5715706Z 的原 shell 错误指出：从第7行开始的 heredoc 到文件结束仍未找到 PYSKIP；紧接着报告 if command 的 unexpected end of file。原 workflow 的 else 分支把 Python 正文及 PYSKIP 结束标记额外缩进两格；YAML 公共缩进剥除后，这两格仍在 shell 文本里，不能作为普通 heredoc 的结束标记。

这是整个 if 块的解析失败；不能把源里拟打印的 removed=false 对象当成一次已经发生的清理事件。原日志没有返回 request219_cleanup，也没有给出应用层 namespace 删除成功。本次应用 cleanup 的 rmtree 未执行。托管 runner 的通用 job/post-checkout 收尾，不提供该科学 namespace 逐项删除的实际 receipt；本结论不填造 VM 销毁时刻或删除完成状态。

因此应分开三层：

1. 原准备失败时没有开始本请求科学 child；
2. 必要读回未证明 quiet，按自身合同没有读取科学文件；
3. 清理脚本本身未解析，既没有执行成功删除分支，也没有成功执行预期的保留说明分支。

## 502.7 全部原科学责任仍未开始

下表中的“未开始”依据官方第10步 skipped 和上述准备控制流，而不是据 native=false 反推某个数值不等式失败。

| 原责任 | actual219 已付范围 |
|---|---|
| 当前 H 原 noJ/primal 求解和实际选中 root trace | 未开始 |
| 同 H 的完整 J、R273 方向、原线搜索与32×10责任 | 未开始 |
| live128 同 call 实际形成及 binary128 状态/两 mean | 未开始 |
| 每局部226状态、完整224方向 | 未开始 |
| 全576 stage 敏感度与577径向节点资料 | 未开始；二者不与226状态布局混用 |
| 完整112 boundary response | 未开始 |
| 完整338×112 response/J，原合法混合导数合同 | 未开始 |
| 13项 cut 标量与9项 fresh audit | 未开始 |
| 单次响应的 binary128 → 实际 binary64 协议投影、原有限检查 | 未开始 |
| 原全部 FD groups、方向、层及收缩判据 | 未开始 |
| 原 fullDN 域、RMS、边界、原 Newton/全部实际 trial | 未开始 |
| 当前完整 accepted/final 及最终 fresh audit | 未开始 |

没有原生 native success、fullDN accept、精确目标根、连续 C 结论或数值反例。原19200秒科学钟未启动；不存在“本次用完320分钟”的解释。14件数学/协议源的预定作用范围仍由 R501 和 [R493](R493-current-H-live128-response-projection-and-original-fullDN-interface.md) 条件说明，本次未将其数值执行付清。

## 502.8 最小后继的实际依据

独立 request221 / R508 / actual R509 只处理本次已经定位的三件工程问题：

- ledger-ready 使用原204/208已有完整64字符 SHA，保路径、blob、bytes和原数据不变；
- quiet 在已登记身份、实际组/后代和可读 namespace 的真实权限范围内工作；真实 own 或可疑 own 不可读仍为未决，禁止读删；
- cleanup heredoc 使用 shell 实际可解析的结束位置，并如实区分执行删除、保留与执行失败。

原219文件不变；14件科学源、19200秒单一科学钟、320分钟科学 step、350分钟 job、原预算、全部 means、224/226/112/338责任及原最终接受门不改。后继不使用本次失败作为新的科学接受门，不新增 fixture 或独立审计，也不预付其准备成功或科学结果。R509必须等新的真实 source/run/终态原记录。

本结论立即登记 actual219 的失败和未开始范围；后继是否成功另行记录。
