# 最终 M15 准备器 v1 初审的后续修正

2026-11-09，/root。历史root源审 root-review-final-m15-coupling-preparation.md（SHA703bc9d548060fcde97c37216766412ff2661b1ac4c84f31521344c615c781a7）保留，不改其当时字节。

tail_theory后续窄接口复核发现 v1 的 finite_tree 对 None、字符串和bool返回真，而原cutJets此处所有值应是有限数值标量或长度M数值数组。故“全jets有限”的通用门描述过强；该辅助门须修正后才能作为正式未来启动入口。当前continuation尚无闭合s=1结果，现有两次只读gate已因缺少reproduction提前返回未就绪；没有发生错误放行或solver启动。真实已闭quarter的jets经单独检查没有这种类型异常。

已要求保留v1，另存最小v2：显式完整字段集合、数值不接受bool/None/str、三数组长度M与全有限检查；只用现有真实quarter输入及内存坏类型副本测试该局部门，不制造伪s=1响应。v2另经全文独审和root差分复核后才供未来真正s=1接续。此修正不改变任何正在求解的方程、guard、容差、流程或数据。
