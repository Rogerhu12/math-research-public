# RK48 源分区精化执行链（准备与运行状态）

2026-11-14 /root，根据 exact_closure 实际检查点归档。原 A、同 g、全 H 的 RK48 Newton 已接受归一残差 1.6723555785869715e−10；08:23:50 UTC 尚在最终 audit，未出现 result.json，不能记作完成求解。

v3 pipeline 仅在原 solver 真成功退出后消费结果，保留全部 source knots，分别比较 RK24→RK48 的共同八级、RK48 八→十六级。区域包装保留原 longdouble 六 jet 数组，只补 patch / exterior 各自最大值；原三窗口实际验证已通过。source partition background 已实际执行，全部原半径匹配差为 0、保留32个原源节点。v1/v2 等待进程的中断不构成 solver 失败；v3 不导入它们。

## 可恢复位置

工作根 B=/workspace/scratch/ffc1334c1988，W=B/exact-work/closed-local-r1。solver session 87946；流水线 session 13425。即时 supervisor 记录 B/exact-work/current-checkpoint.json。实际恢复包 W/A-RK48-solve-r1/ 中的 config、request、intent、ready.json.gz、iteration.json.gz、trace.jsonl 可重启；iteration 是 recovery-only，不能当 converged。v3 intent/lifecycle 位于 W/A-RK48-cusp-resolved-r3。未完成的大输出保留在该独立工作目录，完整结果另行归档。

## 本次冻结的新增源

| 文件 | SHA256 |
|---|---|
| exact_20261114_RK48_cusp_pipeline_v3.py | 8cccbce9e45f952ee5c73303dd2b3dcc324f84478be4ab2fac59090530fd973b |
| exact_20261114_source_partition_background.mjs | 8d72c76b9ea75e7cb969c871b075175ed5d8323f1114d06680601b4e8fb514c9 |
| exact_20261114_regional_common_grid.py | 21ef05291861b575ce436d146b5aa85a1836cdfb8175efe969eae321ed08ea20 |

## 后续真实完成记录

原RK48 solver随后已真退出0，完整J/audit和全部响应见[独立完成结论](2026-11-14-exact-resume-fixedH-RK48-re-solve.md)。v3在08:31:15 UTC实际启动真实16点读出；本准备记录没有替代后续各项真实终态。
