# R582：真实6e91与原完整390库的实际续接

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。

从 [原383自然终态](2026-11-28-r582-e781-to-6e91-natural-terminal.md)
的真实97q `6e91b58d61b2535ea4e262950d2177310a53ceb7fc50e87869d38e639949a334`
继续；同一p=.181、阶段0、metric phase、trust2，原模型和完整接受代码未改。

实际当前385coarse及5个pending全部并成390，原16290fine逐点保留，
原中点规则新增6点后需16296×3072完整资格。旧fine并不替新点；
求解器原baseline、全部当前行、物理回溯、epigraph提升、完整fine及阶段门照常。
原目标p=.8和最终η≤1e−7保持，当前mean仍是设计变量。

这次优化初值明确选择已接受的6e91物理q，epigraph取其原fine η加原1e−9。
该值只是新优化初值，仍须新行检验。旧driver的通用initializer槽名为
`unqualified_warm_backend_trial`；新对象在槽内明确标明
`scientific_source_kind=accepted_physical6e91_with_original_fine_metric_epigraph`、
`is_previous_raw_backend_point=false`，没有把它伪称为上一轮raw callback。
此前raw5cf6和独立半步a938的完整原数据、拒绝原因保留在输入来源中，
不作为新初值，不重做一个独立已拒fine。原完整优化代码直接复用，未重写接受逻辑。

必要输入330307 B，SHA256
`a21bc8e922a79c0831fc9f5f06adae95bc489c739a349993aec9193a2f8f4045`；
只含真实态、原库/拟定库/fine、拒绝来源、完整成本及来源身份。
原唯一FINAL/log仍以source/run/hash再生，不复制入库。
上一轮2515.759658948实际秒、11完整J/143方向块/60值/14fine及祖先成本全保留，
未存的SLSQP工作数组不伪称已恢复；新必需J、物质场和所有部分费用继续收费。

公开Actions入口 `scripts/r582_6e91_original390_resume_20261128.py`，
请求 `computations/request-r582-6e91-original390-20261128.json`，
仍是2400秒科学预算、30秒终态预留、50分钟job。时钟结束若未达门继续接真实态，
不把声明预算当实际收费上界或课题完成。
