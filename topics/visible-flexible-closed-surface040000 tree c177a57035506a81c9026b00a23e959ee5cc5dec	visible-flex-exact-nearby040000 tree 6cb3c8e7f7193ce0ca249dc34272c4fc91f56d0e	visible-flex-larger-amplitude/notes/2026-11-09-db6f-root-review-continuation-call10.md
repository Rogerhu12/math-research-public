# continuation02 call10 关闭失败：root 复核

2026-11-09，Astra-visible-flex-db6f0b0e。已完整读取 `prefix-continuation-call10-diagnosis.md` 及其元数据核查源码，独立执行同一核查自然 exit 0。排除明确标为活动观察的 `controller_observation` 后，关闭诊断 payload 与作者逐字段完全相同，canonical SHA256 为 `87bdd7cfe5b832f9e274af3618f913a9b0606a0e5ea3734cd82b5675b69f3315`。

66 项原启动绑定、实际8源码、原物理配置/15模目标、关闭响应/旋转日志和28个失败stage输入均已重核。root 在同一活动控制器中实际观察到回退至最后成功s=.8125并请求s=.84375；没有修改控制器或将失败状态作为warm。

原call10响应只含 failed、lastIteration、checkpoint。其末基点norm4892.887571107566/minA.05038380907076433不是完整成功residual；不补造converged或audit字段。失败是iteration3原十档线搜索耗尽，不是36轮耗尽或worker自然退出。主控制器仍在继续；本次元数据检查的exit0只属于检查器。

root同意窄诊断：call8/9已各从类似的大初残差全步成功；call10初minA约.31588健康，后续接受方向才把minA压至原guard附近。28次拒绝均为root或D/S/A组合guard，不能将全部组合guard改标为A单项失败，也不能据此证明该边值无正分支。三次warm规则未切换，较高模的相对倍率反而递减，不把倍率本身当成失败因果。

原方程、guard和容差保持。新步长的实际结果另行验收；任何备用初猜也须明确UNSOLVED，不能改变物理目标或替代原求解验收。root的复跑报告和实际执行记录分别为 `root-call10-diagnosis-replay.json`、`root-call10-diagnosis-replay-execution.json`；本次没有新root/RK/BVP/连续后端运算。
