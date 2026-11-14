# 实际非线性尾耦合的中间恢复

2026-11-12，visible-larger-20261112，GPT-6 Astra Pro，AI-assisted。

## 为什么增加这一记录

旧first675 q085实际尾尝试在恢复prefix期间失去worker，未得到新接合解。
随后入口已将worker延后到prefix恢复及释放不用内存之后启动。
本次进一步复用已在同H的M24/M32完整运行中验证的 `tail_resumable_client.py`，
并在外层算法中尽早保全已经计算出的内层状态。没有据此推断旧signal9的原因。

## 两种不同的恢复对象

显式 `--client stored-resumable` 仍使用原stored度量、完整表示的物理H、
同一fourier-root/tangent算法和原验收阈值。
它增加每个接受尾Newton trial的立即保存；这种trial必须经过正式完整切线和audit复核，
才是最终响应。默认客户端仍为 `stored-bounded`。

前缀外层每次对真实尾的仿射切线成功求出内层BVP后，
在请求新的真实非线性尾之前保存 `outer-NN-raw-collocation.json.gz` 及压缩数组块。
该包显式标记 `solver_success=false`、`physical_surface=false` 和
`actual_nonlinear_coupling_pending=true`。
内层成功只写入provenance，防止它被误读为整个耦合问题成功。
`root_raw_collocation.read` 可将其作为同配置重启，而 `--postprocess-only`
因其未验收标志而拒绝跳过Newton。

最终仍以重新求解原非线性尾后的physical slope边界最大残差不超过 `1e-10` 为门，
并保留最终audit及真实PPoly导数对尾二jet的独立seam检查。
任何中间包都不能替代完整响应、无限尾、全Cartesian接缝或闭曲面。

## 本次有限检查

`strong_actual_cache_check.py` 经真实嵌套加载入口、显式resumable选择及cache8，
在旧first675 q085的M16/N384、49个warm节点上核对三点J/PJ。
重复两次结果逐位相同，前四次miss后四次hit，guarded tail启动次数为0。
该检查没有启动tail worker或BVP；故不把检查输出中的预期inspection异常当求解失败。
资源记录为4.03秒、119716 KiB、exit0。
命令、实际选择的客户端、源hash与guard计数完整保存在
`2026-11-12-root-resumable-client-inspection.json` 及resource JSON。

## 下一实际解的选择

已准备vu032 q085成功态的M16/N384完整向量联解计划，
冻结profile取自成功包，delta/boost_length继续是物理设计未知。
因此它不是固定前缀g的加密。
尾部物理参数、原q040成功tail warm、sigma=-1的方向约定及真实验收均保留。
若正在运行的q090同图三控制得到几何更好的成功态，先从该态生成新的独立配置。
这里只记录已准备的具体恢复路线，未声称实际尾接合已经完成。
