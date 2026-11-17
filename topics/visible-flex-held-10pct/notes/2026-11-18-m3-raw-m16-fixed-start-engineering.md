# m3 raw λ=.02 同 g 的 M16 启动工程记录

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
可信度：原问题保持下的工程终态，不是数学失败或新接受态。

固定已登记 raw λ=.02/M8 的完整物理 profile（包括δ）、圆化
几何、补弧路径和材料角图，仅升 M8→M16、prefix角求积256→512、
tailN128→256，保留 depth8/parts16/steps16 和原全部门。
`refine_round_core_raw.py` 与 `couple_m3_round_core_raw_fixed.py`
使用原 fixed-g BVP；输出钩子逐项拒绝 profile、chart、warp或
物理port改变。原 raw 基 append0 精确保输入核心的数学定义。

第一次新worker端口只提供五个物理cut数值，未带prefix专用
`_prefix_bridge`选择器；构造器误走原Hermite分支并在worker前
拒绝。这是入口工程错误。修正为独立 `prefix-port.json`，保留
原已接受的桥段选择器，原worker五个cut数值逐项完全相同，没有
调整任何物理参数或cut数据。首次错误的命令、日志/hash保留。

v2成功进入M16实际warmup。首轮完整shoot给归一化残差
720.048666025166、minA=.7420107199374775、minD=.99942817624964。
随后worker停止，Python summary返回 `Weighted tail worker stopped`，
共1次尾调用，没有完整尾response，没有prefix内解。原client没有
保留worker退出码，stderr无额外说明；因此仅记工程中断，不宣称
D/S/A失效、求解不收敛、OOM或数学分支不存在。

下一入口会在当前sparse源的独立副本中，仅复用同一物理mu的
无状态计算engine，并保留被cutJets捕获的对象身份，减少每个
数值stage重复分配。所有原ODE、浮点求和顺序、sparseGlobalSolve、
残差/line search和原守门保持。完整同态残差/Jacobian逐值核验
与worker stderr/退出码诊断分别登记后再继续实际M16求解。

完整命令、两个失败的源/输入/hash、首轮trace摘要，位于
`scripts/resume_m3/raw_m16_fixed_start_failures.json`。该文件不含
checkpoint场数组。此笔仍没有把同g精化算作已完成。
