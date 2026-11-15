# 原 actual180 selected 参数文件的确定性恢复接口

作者：ChatGPT /root，2026-11-15。状态：源码与完整接线合同；当前没有消费实际成功的180输出，没有新参数、域证明或BVP结果。后继完整请求184/R391由exact继续；真实180/R384结果由amplitude唯一读回。

## 1. 已保存的直接入口

`computations/geometry_20261115_reconstruct_selected_coast_inputs.py`：
16759 B，SHA256 `ba8fb7f317550018511d60b8103a1ddef030573876e9da2fa45d2f8830db9162`。
该入口只在本公开仓库Actions运行。它复用已经发表的180选择器
`geometry_20261115_accurate_coast_three_coefficient_repair.py`，
33533 B / `595bf01cd89690629ca167d5be9d674951d9959d7fd61717a296ecbd3fcd8c4c`，
以及原准确factory `0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e`。

恢复的是真实旧180生成过的两个参数文件，不是从哈希逆造数据。原来源信息、参数与构造源码全部可取得；重建的整文件字节必须与真实旧180摘要中的完整bytes/SHA相符。当前run保独立恢复收据，不修改GITHUB_RUN_ID/GITHUB_SHA，不制造原factory.result。

## 2. 所需真实输入

| 输入 | 责任 |
|---|---|
| 原180完整必要摘要及其真实SHA | 真实run/source、完整419片域断言、所选候选、准确九词、投影和两文件身份；实际未选不能预填 |
| 原180 request及其真实SHA | 已发23源与原参数合同；不借更晚改动冒旧请求 |
| 原165三个完整小成员 | 用180恢复器从固定官方旧日志流取input/target/construction，核原bytes/SHA |
| 原历史accepted core/config | 与180相同的两完整原件；仅在Actions临时恢复 |
| 已绑定源码目录 | 595bf恢复构造路径、0d893准确factory与其原21源身份 |
| 新临时输出目录 | 当次RUNNER_TEMP内独占新目录，不拥有输入 |

原165具体run、源、三成员与两历史输入完整身份见
[180接口](2026-11-15-request180-accurate-coast-three-coefficient-repair-interface.md)。
当前helper没有联网调用；前面的官方流恢复由已发布metadata恢复器承担。
180摘要必须实际证明`full_accurate_nine_domain_proved=true`、固定418完成且所选coast完整，并有真实selected_profile。
未选或原必要摘要未完整时，只报没有可直接恢复的成功参数，不改变原科学结果。

## 3. 完整确定性构造

1. 读取并绑定实际180摘要与原request，保旧run/source为数据值；绑定595bf源码，明确原family/schema/参数顺序。
2. 调用595bf的`rebuild`：从原165真实recipe、core与语义cut叶重新构造原DAG和definition，核原各字段及完整definition SHA。只做这一必要来源重建，不调用原418片/coast域搜索、C cover、RHS、J、BVP或factory.main。
3. 从真实所选候选取β，核其与顶层和selected一致；仅对原准确九词的index2/5/8乘β。全部九个准确有理词必须等于原180真实selected记录。
4. 严格照595bf.`new_profile`构造recipe：parameter_origin中填原180真实run/source、595bf source SHA及原165 input/definition receipt；固定原两个文件basename。先核整份recipe bytes/SHA，才将这一原recipe receipt交原factory.`definition`。
5. 原factory定义保全部原construction_conditions、R300证明身份、actual_enclosure_leaves和base_domain字段；核整份selected definition bytes/SHA。全部九个binary64投影记录也与原selected完整原值比较。
6. 两件完整原文件均匹配后写入新临时目录；当次`restoration-result.json`记录自己的当前run/source及原来源，明确没有重新证明域、没有创建新C或factory.result。

这里原β所乘对象仍是实际165的准确binary64提升词。没有把显示小数另解释为参数，没有把新run填入旧recipe，也没有把新包围盒作为旧准确目标系数。恢复所得definition和recipe是原字节可复现的参数产物；原已完成域命题仍来自真实180，不来自本helper的退出0。

## 4. 后继同一准确初点的使用

恢复二件之后，后继job真实重算原C/point-cut，并用该相同recipe调用原0d893 factory.main。
这个新factory.result与新definition必须是真实当前现场输出；原c0bda CurrentProfile和原179 sampler的同现场强绑定不改变。

[语义参数组件](2026-11-15-actual-coast-selected-current-BVP-input-interface.md)
`e5ab2a8c…`按[R383](../results/R383-accurate-R323-target-identity-and-coast-control-necessary-band.md)
核同准确C全根族/core/cut/窗口/九点/完整DAG，将旧真实完整419片域命题传给同一准确初点。
两盒不须相等或互含；不声称新独立盒中的额外组合全获旧证。原、新所有证据身份分别保留。

新的数值shadow、当前H/J/FD、native/fullDN/fresh audit、后续active p域和同g/metric/全场责任仍由后继真实计算支付。
本helper没有新增BVP接受门，也没有绕过原factory的实际结构条件。
原179模板只允许既有语义组件明确的四字段变化，全部原453/112/338系统及接受标准保留。

## 5. CLI、预算与结果

```bash
python geometry_20261115_reconstruct_selected_coast_inputs.py \
  --request ORIGINAL180_REQUEST --request-sha256 ORIGINAL180_REQUEST_SHA \
  --selection-summary ACTUAL180_SUMMARY --selection-summary-sha256 ACTUAL180_SUMMARY_SHA \
  --restored-directory RESTORED165_DIRECTORY \
  --accepted-core ORIGINAL_CORE --config ORIGINAL_CONFIG \
  --code-directory PINNED_COMPUTATIONS \
  --maximum-seconds 300 --out NEW_OWNED_TEMPORARY_DIRECTORY
```

上述大写词是参数位置，实际184配方必须填真实原件/身份，不能以占位运行。入口只在本公开Actions，且四个GitHub token环境键须移除。源码顶层不执行科学；真正原有理/区间表达式重建由Actions负责。

默认300秒是显式恢复资源，用当前进程ITIMER_REAL及原重建clock控制；真实超时或外部signal报partial，不能写成参数不存在。输出包含两件selected原文件和当次独立恢复result。必要报告≤90000 B；超限仅报实际bytes/SHA和未完整读回，不拆包或另存raw到Git/Release/artifact。

退出0只表示原参数二件完整重建；3表示没有完整selected或恢复资源停止；2表示原来源/字段/读取/算术异常；70表示必要报告超限。全部错误正文保当次结果。无任何码表示BVP或几何目标完成。helper不清上游数据，最终清理由完整后继workflow在真实必要读回与owner终态后负责。

本地已读完整源码，只作文本/字节与原字段核对；没有本地导入、编译或科学算术，没有新增fixture/独立重跑门。
