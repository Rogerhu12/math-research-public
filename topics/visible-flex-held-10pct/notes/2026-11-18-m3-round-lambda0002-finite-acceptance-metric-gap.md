# m3 圆化 λ=.0002：有限真联立接受，完整 metric 未过门

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
可信度：有限真联立接受及其明确的完整物理缺口。不是精确圆弧解、
同 g 收敛、闭面或课题完成。

## 实际接受了什么

保持 β₀=4.625/q=.040、a=.21/b=.08、补弧转接 .16、严格主频
与全部高矩 canonical 同伦。仅把尾射击 parts8→16，steps16、
M8/N128/depth8、物理尾及原 2e-9 射击门均保持。输入仍是旧
β4.625/q040 完整接受 prefix 与旧实际尾，原 worker 自行 warm
remesh。没有把上一失败尾标成接受。

完整终态 solver_success=true，936 径向节点，δ=.06104444009746941。
第3真实尾验证残差 6.883574338163801e-10，实际外层边界残差
1.112495615557887e-9（原 bc_tol=1e-7）；最终第4尾 audit 保持
同一已接受尾残差，physical nonmean BC=2.224991231115774e-11。
所有原局部 D/S/A、Frenet 与尾门仍生效。

## 没有接受的完整几何结论

| 实际完整诊断 | 数值 |
|---|---:|
| prefix metric FFT-l1 | 3.9703598722406656e-4 |
| prefix full flow defect | .010554889270813604 |
| prefix Darboux FFT-l1 | .3647606596413415 |
| prefix 最小采样 Frenet margin | .002957895446802694 |
| mean 一阶接缝差 | −9.83240147094111e-6 |
| mean 二阶接缝差 | .0002299332573019175 |
| nonmean 二阶接缝差 | 6.536999859036623e-6 |
| cut metric FFT-l1 | 1.861134864265817e-5 |

完整 metric 明显超过 README 的 1e-6；上表是实际完整场诊断，
不能被有限投影方程的 success 标签替代。补弧首控制 c6 约
2.03808e-4，但最高 c24 从旧接受态的 3.64010e-11 变成
1.9730760793443095e-5，显示这一步 M8 高模式的有限反馈很强。
λ 仍只有 .0002，保护区也尚不是 λ=1 的精确圆弧。因此不为
这一步重复建设闭图 metric 盒，也不按 solvertrue 机械增大 λ。

## 继续采用的新物理路径

下一步转向原始 compact 控制：在每个加权 cosine 上只扣除
均值/主频投影，而不乘近奇异的高矩 Gram 逆。λ=0 保留原 cosine，
λ=1 的自由控制空间与原 compact 空间相同，但中间高矩随 λ
改变；这是新物理同伦，不能说成同 g 精化或只改变存储坐标。
新运行仍从旧完整 metric 良好的 β4.625/q040 锚点出发，不从
本条 metric 失败的 canonical 状态接续。

源码 `continue_round_core_tail_resolution.py` 与完整标量、命令、
source/input/output hash 均在 `round_core_lambda_0p0002_parts16_record.json`。
第一次新 driver 在 worker 建立前误用了 `parts` 键并报 KeyError；
正确 schema 是 `shootingParts`。错误日志/hash保留，修正后使用
独立 v2 目录，原输入和 canonical source 均未改动。
