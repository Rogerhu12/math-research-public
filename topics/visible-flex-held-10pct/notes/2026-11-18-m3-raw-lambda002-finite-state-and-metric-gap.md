# m3 raw 路径 λ=.02：首个有限真联立态及完整 metric 缺口

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
可信度：有限 actual-coupled 接受，不是完整等距、圆弧或10%完成。

采用已登记 raw mean/primary projected compact 同伦，仍从旧
β₀=4.625/q=.040 metric 良好的 cosine 接受态出发；没有从上一
canonical metric 失败态接续。a=.21、b=.08、补弧转接 .16，
λ=.02、M8/N128/depth8、parts16/steps16，所有原守门保持。

终态 solver_success=true，δ=.06105141410261685。第3次实际
尾验证和最后第4次 audit 均接受，尾射击残差1.375444292097049e-9，
minA=.7420033682728756、minD=.9994281510655263。原真实
外层边界残差6.758123119154146e-10，通过原 bc_tol=1e-7。

| 完整物理量 | 实际诊断 |
|---|---:|
| prefix metric FFT-l1 | 8.30077505696214e-5 |
| prefix Darboux FFT-l1 | .04793199864238629 |
| mean 一阶接缝差 | −5.4724665451977295e-8 |
| mean 二阶接缝差 | 1.278609890409399e-6 |

完整 metric 仍超过 README 的1e-6，不能用有限 solvertrue 或
较小的 mean seam 代替这个门。λ也只有.02，尚无λ1精确圆弧。
因此下一步没有机械增大λ，而是固定此态的完整物理 profile、
圆化λ/几何参数、raw控制定义和材料角图，升M8→M16，同时
angular256→512、tailN128→256（保留parts16/steps16）。新实际
worker端口的物理参数及五个cut浮点jet逐项保持原样。

raw控制每列只依赖原2×2低Gram，因此追加零系数精确保留输入
完整核心；有限BVP在新模式下仍须重新求解并通过实际尾验证。
本次只建立了这个可检验的同g精化起点，尚不宣称加密成功或误差
必定下降。后续完整metric及q/control变化必须由实际终态报告。

完整命令、源/输入/输出hash、全部真实尾response标量、core与
inlet诊断保存在 `scripts/resume_m3/raw_round_lambda_0p02_record.json`。
脚本为 `continue_round_core_raw.py` 与 `couple_m3_round_core_raw.py`。
checkpoint留在计算目录，没有将场数组写入仓库。
