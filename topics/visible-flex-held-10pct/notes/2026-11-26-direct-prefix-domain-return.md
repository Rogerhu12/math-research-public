# 公共原 M24 冷初猜的实际域失败

**数值执行记录，非不可能性结论。** 公共run45763361623的首原命令已实际结束，worker于06:13:44 UTC发布finished。原portable driver捕获内部异常，故进程码0与solver成功不同；此处solver_success=false、无raw_return、无prefix_audit。真实错误为 `Adaptive Frenet domain failure: -2.8750805252178435e-10`。不截断负值、不放宽Frenet域或接受门。

原M24/λ.002的旧成功输入来自M16完整lift场；本次是从记录控制和线性cold场再生，不能把二者混同。当前结论只排除这一实际冷恢复尝试，不能推翻旧631点accepted场，也不排除原问题。完整可复现命令在首ci请求的历史提交及recovery setup，执行hash/实际run hash见同名小JSON。

后续三路parent在06:21:20 UTC真实拒绝未接受源并exit2；没有启动任何fullH、fixed-g或λ设计子进程。这正确保留了各自门。原公共runner仍在线，源和native都在；接下来从较低维M16求解得到实际场、以原完整lift升M24，再原门求解。M16即使仅solver收敛而metric未门，也只能当升谱初猜，不作为合格场。

完整traceback及最后资源事件将从原runner保存的run/log读取，尚不能断言失败发生在RMS、Jacobian有限差分或真实Newton基点。没有因耗时而停止或重启原进程；准备的第二runner未启动，继续使用现有runner。
