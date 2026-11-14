# 原仿射恢复的首次请求守卫：r3真实失败与r4修正

`physical-merit-r3`（session20793）正式exit1，wall21.0590739s、peak138972KiB；Jacobian callback、矩阵、因子和线性求解计数均为0，未启动新Node。实际拒绝信息为 `Tail recovery complete H does not match the first live actual request`。这是包装器的身份守卫不适配显式仿射恢复，不是数学不收敛，也不是环境signal9。

原因是原a84入口会把 `--initial-audited-tail-packet` 同时设为 `tail_warm_checkpoint`。原上层 `coupled` 函数在调用 Actual 的 `solve_coupled` 前，以当前raw的H检查这个暖包。原先普通重启的首次请求就是当前H，因此该守卫正确；显式续算旧仿射问题时，首次实际请求改为旧H0，而当前raw H仍有差别。此前五项协议夹具只覆盖下层Actual方法，未覆盖这一层。因此保留该检查的有效结论，同时明确它未捕获此次完整启动中的守卫冲突。

旧 `strong_physical_merit_actual_bvp.py`（11f3e91e…）、`strong_physical_merit_and_affine_resume.py`（e330336d…）和全部失败数据保持原样。新独立 `strong_physical_merit_actual_bvp_v2.py` 只在既有显式变换之后增加四个可重建替换：加入自身源身份、把自身SHA加入运行记录、将首次请求比较的左端明确设为Runtime冻结H0、在该身份记录中另存当前raw H并标为未审计。

原完整向量比较本身未删除。随后Runtime仍要求：原入口末端的实际H逐位等于H0，最新x/y/p逐位等于所选完整raw，原source/ready/160层指纹正确，旧完整K0/74×24 J0逐位相同。当前H从未被标为已有真实审计。原Hnew真实复核、最终audit和所有原始RMS/BC门均未动。

## 新增的实际两层协议核对

`strong_physical_merit_first_request_check.py` 使用同一完整raw及已审计包，分别从真正源码中提取上层 `coupled` 与下层 `solve_coupled`，按实际调用关系连起来。它是明确的协议夹具，在第一处 `solve_bvp` 入口以专用哨兵停止，未执行物理RHS、Jacobian、BVP、Node或新审计。

session32433正式exit0，wall12.6350353s、内部计时4.5203554s、peak71620KiB，四项全部通过：

1. 旧上层代码准确复现r3的守卫拒绝。
2. 新上层仍拒绝H0中一个binary64位的改动。
3. 当前raw参数中一个位的改动经两层仍被Runtime完整状态校验拒绝。
4. 未改动的原始输入经两层真实源码恢复同一H0/K0/J0，并在BVP之前停止；0新Node请求，current raw H明确不同且未审计。

标准库prepare session70381也正式exit0，确认27参数/100BC及原coupling='outer'身份。两层核对读取的draft-plan SHA与完成时文件逐字核对一致。

## 新运行身份

r4使用原已保全0003继续；新入口SHA256为 `4e452c8c969d85a5ffbea2d6f954f84926f7fb53e934833daffdc6b6470ca30b`，不可变命令计划SHA256为 `0a387ef8562443bc6687ce0f22844c387999038584ac6e97b0543d29fb307924`。它保留前一记录中的固定S选择、完整原始方程/目标、磁盘原Jac/QR后向核验、全部最终验收和资源配置。正式session98541已在真实生产链中通过两层身份守卫，并记录原H0、当前不同H、完整raw、K0/J0逐位恢复，首次响应来自严格已审计H0缓存，未启动Node。

这里仅登记恢复入口正确进入实际BVP；后续收敛、新H真实尾部、最终物理审计与题目完成仍需另付。活动日志和恢复点不纳入本静态源码/核对清单。
