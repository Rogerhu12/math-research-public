# 延拓实际报告的短根记录合同：独立完整 pure reader v2

## 范围与当前事实

本条是完整读取入口的静态接口修复，不是端点求解结论。公开 run `45820592817/1` 的 actual28 已产生真实 `9649ed99...` 报告，字节 SHA256 为 `a2442ccad906f5fbc473376c5bd1644328235ae484ba8bebfcd8e4fa3019d335`。其数值延拓没有到达参数一，初场读数失败；旧 `a0c927aa...` 纯读取步骤 actual29 另以 returncode 1 返回，没有产生 readout。actual29 的真实最后异常由另一个已刊 `ef017af52...` 纯日志入口读取；在该日志返回前，不将下述静态差异冒充已经读取的实际异常。

## 完整源码中的确定差异

绑定的科学 driver `fullclosed_zero_moment_continuation_so3_qp.py` 的 `endpoint_readout(q)` 只保存当前点摘要。它逐项保存当前整点摘要、根政策、缓存数量、实际根误差与修正量、当前成功根上的奇异值统计、根计数、最后失败记录以及四项明确为假的连续认证标记；它没有保存 `endpoint_continuation_policy`、`endpoint_continuation_counts` 或 `endpoint_continuation_last_summary`。

旧完整 reader 的 `endpoint_roots(value)` 对以上三个未产出的名字执行 `value[key]`。因此，只要先前完整源/模型/固定目标/18 字输入检查通过，读取这种合法短记录就必然报缺键。这不是 `None` 数值应当补零的问题。完整 `latest_operator_metadata` 是另一份记录，它实际包含这三项，并由 `endpoint_metadata` 单独核验和返回。

## 修复的全部边界

新完整源 `read_zero_moment_continuation_so3_report_v2.py` 从旧 `a0c927aa9d7608a16ad7c051861903ebb533be3602325c2aada60ed6b1ccae61` 全体派生，只作三处文本修改：文档说明；在 `endpoint_roots` 的必取名字列表移除上述三项；把本次独立 readout schema 从 `...-v1` 改为 `...-v2`。它仍完整保留全部原函数，全部科学 driver/来源角色/三层模型/固定标量定义/同一 Q 字/范数/初场失败/完整终态守卫。

`endpoint_metadata` 全函数 AST 与旧源完全相同，仍要求真实的延拓政策与模型和工作政策一致，仍从完整实际元数据返回政策、计数、最后摘要及完整最后批次。新源没有给短记录缺项补零、没有从另一点记录填值，也没有把失败当作完整场。`verify-final-bundle` 的原条件语义保留：只有科学报告实际 complete 时才验证最终 bundle；初场失败不要求不存在的最终场。

新 readout 保留完整历史和真实报告；新增 fresh 参数把同批八个角的字面角度、最终辅助参数、初始端点缺陷、实际 stage/accept/reject/Newton 数，以及真实失败记录作为标量返回。源未记录中间 stage 的 `C_z` 奇异值，所以本次不创造这种数，也不重新求任何 Jacobian 或奇异值。完整 stage 表与科学报告继续留在 runner。

## 字节、参数和实际静态检查

- 新完整源：31936 bytes，SHA256 `75f4e9abd41972add063d3881cb4140aa6e259f09c2f9832c58c69be3c856e00`。
- 新完整 fresh step：15174 bytes，SHA256 `6867087a35e851acae9be88095d955ba1bbeebb0ba1e22664a3daf7467d3286f`。
- 新输出：`postprocess/zero-closure-frozen-moment-Q-continuation-first-readout-v2.json`，不覆盖旧缺失路径。
- 科学输入：原 `zero-closure-frozen-moment-Q-continuation-first/report.json`；parent 仍是实际存在的 `axisymmetric-R690-reference-v2-first/reference.npz`。

本地只实际运行 Python 标准库的源码 SHA、JSON、AST、`compile`、重复字面 dict key 和尾空白检查，没有 import 或运行科学模块。把两处代码替换与文档恢复后，新旧完整模块 AST 相等；只有 `endpoint_roots` 与 `read_report` 两个既有函数 AST 改变，后一项只改 readout schema。完整差异在 `read_zero_moment_continuation_so3_report_v2.diff`，核对记录在 `reader-v2-source-derivation.json`。

本次 source 尚未在 Actions 执行，不能填实际读取成功，更不能填数学完成。原 9649 科学源及 actual28/29 原始返回状态均不改。

## root实际发布

2026-11-26 17:29:59 UTC：root亲读全部三处diff及9649.endpoint_readout真实名字列表，核全部函数保留/仅两函数AST变，完整endpoint_metadata AST相同；未运行科学函数。完整31936B新源与15174B参数按上表原字发布，追加03b原ef017 trace之后，其余完整步骤逐值不改，运行child不打断。实际trace及v2返回仍待Actions，不提前宣布29的真实异常或v2成功。
