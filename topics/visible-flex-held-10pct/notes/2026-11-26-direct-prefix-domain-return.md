# 公共原 M24 冷初猜的实际域失败

**数值执行记录，非不可能性结论。** 公共run45763361623的首原命令已实际结束，worker于06:13:44 UTC发布finished。原portable driver捕获内部异常，故进程码0与solver成功不同；此处solver_success=false、无raw_return、无prefix_audit。真实错误为 `Adaptive Frenet domain failure: -2.8750805252178435e-10`。不截断负值、不放宽Frenet域或接受门。

原M24/λ.002的旧成功输入来自M16完整lift场；本次是从记录控制和线性cold场再生，不能把二者混同。当前结论只排除这一实际冷恢复尝试，不能推翻旧631点accepted场，也不排除原问题。完整可复现命令在首ci请求的历史提交及recovery setup，执行hash/实际run hash见同名小JSON。

后续三路parent在06:21:20 UTC真实拒绝未接受源并exit2；没有启动任何fullH、fixed-g或λ设计子进程。这正确保留了各自门。原公共runner仍在线，源和native都在；接下来从较低维M16求解得到实际场、以原完整lift升M24，再原门求解。M16即使仅solver收敛而metric未门，也只能当升谱初猜，不作为合格场。

原runner保存的真实traceback现已读取：`solve_bvp → f6curve_domain_newton.solve_newton → analytic_adaptive_core_jac.py:26`，失败发生在δ参数列的中心差分 `self.fun(t,y,plus)-self.fun(t,y,minus)`，其中原步长为 `2e-6*max(.1,cfg.delta+p0)`。扰动点离开原Frenet域不等于未扰动基点非法；负数也不被解释成可忽略舍入。原日志同时给出首418点RMS3.62、BC4.01e−3，次1252点RMS5.21、BC4.00e−3，再增2502点；1796.135177604秒抛异常，故不能把一次差分修正说成已解决初猜收敛。

新增独立入口 `tail_domain_safe_prefix_driver.py` 只在原δ差分行先验证原基点，再将步长逐次减半，直至两侧原RHS通过全部原域检查。记录真实步长、失败侧和减半次数；基点非法、其他异常、不可分辨的扰动或40次预算耗尽即明确失败。没有clip、改单边导数、换残差或放宽门。仍由原streamed-release入口求解；目前只通过编译、帮助及5个针对性synthetic守卫检查，尚未在BVP执行。当前M16源码/目录不被替换。

M16冷输入尚在原自适应求解；并行准备前会话已成功的新g q=.006→.06 checkpoint路径，必要再生旧场后再升谱，不把恢复旧结果登记成新几何。此记录时第二runner尚未启动。
