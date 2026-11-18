# q060 parts16：原 warmup 失败与外部初值程序堆上限

**数值失败与工程终态分别记录，未产生新 prefix。**

session33116 的原联立入口对 $H_{\rm old}$ 真实求解。
原 worker 在 iteration3 以
$3.671459625080514\times10^{-9}$ 线搜索失败，原门仍为严格小于
$2\times10^{-9}$；minA $.529333104523161$，minD
$.9991344478556847$。
该 $H_{\rm old}$ 与 initializer 的已接受 $H_{\rm new}$ 不同，不能互借响应。

完整 1153×16 native 失败态已保留：
`closed_work/q060-coupled-parts16-v1/seed_tail_0001.json.gz`，
SHA `adf477252c1dc707ce4fe8975aa9c911aca2f9d4c5113ba300d11b82023c4535`。
请求是原 warmup 的 `jacobian=false,audit=true`；原 solve 失败，不能把
这些请求标志称作已返回审计。

IO-v2 自动恢复确实进入了它的唯一外部候选分支，但外部 Node 程序没有
显式获得原 worker 的 heap3072 资源配置。
约 10.18 秒后返回码为 −6；实际 stderr 明确写出：
`FATAL ERROR: Reached heap limit Allocation failed - JavaScript heap out of memory`。
最后 GC 记录约 383.3→383.1 MB。这里有明确的 V8 诊断，不是从无返回码
或 namespace RSS 推测 OOM。

该程序没有生成 candidate 或 candidate-summary 文件，原生重试没有执行。
这不能写成同一预声明候选算法的数学失败或无改善结果。
原 worker 自身没有报告 OOM；它此前的线搜索失败与外部程序的堆错误是
两件不同事件。

原 coupler 捕获异常并保存 `solver_success=false` 后正常返回，所以
observer 的真实 child exit0 **不表示联立接受**。
observer 于 2026-11-18 00:03:26 UTC 记录终态，耗时 204.252 秒。
此次还未进入 prefix inner，因而没有 raw-inner dump；并未丢失一个新的
已完成 inner cubic。

独立 `recovering_tail_client_v3.py` 相对 v2 只把外部命令改成
`node --max-old-space-size=<同一node_heap> ...`。
候选脚本、列表、16 轮上限、全 replay、原 worker、物理参数和门全部不改。
`prepare_recovering_tail_source_v3.py` 只换到这个 owned adapter。
旧源、旧 overlay 和旧日志不修改；后续从已保存的失败状态补完因工程
中断而未得到结果的候选，应另列运行记录。

来源与紧凑终态见
`scripts/resume_transfer/q060_coupled_parts16_warmup_terminal.json`。
完整状态和日志只留 scratch；本条没有 accepted 新尾、前缀或闭曲面。
