# restart8000-02 的同一实际会话监控接管

日期：2026-11-10，root。不是重新启动候选，也不是数学出口。

旧监控 functions cell32 自07:27最后已见内部轮询后，后续 wait 只返回cell运行中，
没有新的内部回执；其原因未知。08:10:00实际b097bc只读确认此stem没有
CP、summary、guard-completion、root-observed-exit或unavailable文件。
root随后调用functions.wait终止的是监控cell32，工具返回Script terminated。
没有向主guard进程发信号，也没有调用新的solver启动命令。

新的functions cell77只调用原session72917的write_stdin。其首个实际返回c2ddac
为同session72917活动、没有exit_code；随后第12次a47b46、第24次97d29d仍为活动返回。
这些实际返回证明此时原工具会话可访问，不能据此说BVP成功或已完成。
原ef2882启动身份、原start观察和所有数学/资源/输入/输出命名保持原字节。

cell77现在是这个session的唯一观察者；不要同时消费72917。它在真正
返回无活动session且有整数exit_code/chunk_id时，才调用原冻结root recorder
写同stem的root-observed-exit并散列全部自有关闭文件。未知工具错误只记unavailable。
完整原final仍须另行执行，监控状态和guard元数据不代替它。

独立seed8000仍未启动；其真实全链由指定独立者在资源允许后另行执行。
