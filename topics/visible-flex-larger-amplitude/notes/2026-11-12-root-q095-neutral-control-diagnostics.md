# q095实际完整响应的neutral几何方向诊断

2026-11-12。root36072（r1，520.2621秒）与38671（r2，175.5696秒）均已在正式工具返回exit0；九个子进程的wait4资源记录均exit0。

这是同一已验收q095/M24实际参考处的完整一阶响应暖态，不是九个新BVP解。完整24core与全部状态场参与；三个低阶核心系数固定，外部vu或first descending curvature的变化含δ/LB/vp的同一真实Jac补偿。全部原配点RMS点与有限定义域被检查；尾部只用参考处完整真实切线，未启动Node、未求新的H尾。

| 轮次 | 方向 | 原RMS | 2max径向距离样本 | κ样本 | 两者乘积 |
|---|---|---:|---:|---:|---:|
| r1 | baseline | 9.976296746e-08 | 3.90094642152 | 8.43932619263 | 32.9213593112 |
| r1 | vu-plus | 0.007491451338 | 3.90623533681 | 8.41346754691 | 32.8649842369 |
| r1 | vu-minus | 0.008114283376 | 3.89557616411 | 8.8671725622 | 34.5427460764 |
| r1 | firstk-plus | 0.002045344662 | 3.90253123451 | 8.52465824998 | 33.2677450841 |
| r1 | firstk-minus | 0.002186033417 | 3.89937864845 | 8.48222690201 | 33.075414473 |
| r2 | vu-plus | 7.860738405e-05 | 3.90147894291 | 8.37980414997 | 32.6936294368 |
| r2 | vu-minus | 7.90805037e-05 | 3.90041308694 | 8.4954523084 | 33.1357733631 |
| r2 | firstk-plus | 2.121814231e-05 | 3.90110413583 | 8.44610218769 | 32.949124176 |
| r2 | firstk-minus | 2.14007473e-05 | 3.90078887763 | 8.4286005194 | 32.8781911601 |

r1使用vu±.002、firstK±.025；r2精确缩小十倍，保留r1已算出的相同baseline。所有候选均通过有限定义域。r2的vu正向明显降低当前峰，firstK负向同时小幅降低半径与曲率；r1表明较大步长会换到新的峰，不能据局部改善外推任意大步。

几何使用所有状态节点的物理s三次C²插值、原production完整高度mean与6阶积分、原角基及全部24模；它是暖态诊断，不是最终实际物理五次包。baseline的κ样本8.439326与完整实际审计8.444020不是同一个采样/插值审计。上述2max径向距离仅为镜像前缀的直径代理样本，不是加入无限尾/帽后的D上界；指标不构成reach、held或完整闭面证书。

基准主包/完整raw/true-tail/导数场的SHA由两份plan及每个screen内的source_sha256锁定。r1原驱动源码逐字保存在 `2026-11-12-root-q095-actual-neutral-geometry-r1-source.py.gz`，其解压SHA与r1 plan一致；来源代码已随main2b0b981a保全。r2只新增显式step-scale与省略重复baseline的命令参数，production入口、factory、暖态公式均未改变。

## 可复现命令

在课题目录内、恢复固定source依赖后运行；每次使用全新out-prefix。r1若重现须使用其已存源码快照或main2b0b981a版本，不能把后改源码SHA冒充旧版。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python computations/root_actual_neutral_geometry.py --baseline-command notes/2026-11-12-strong-q095-actual-augmented-local-r1-command.json --response notes/2026-11-12-strong-q095-actual-fixed-control-response.json --out-prefix notes/rebuilt-root-neutral-r2 --step-scale 0.1 --only-perturbations
```

r1对应原始版无最后两个选项。完整五/四条实际子命令、目标、方向补偿预期值及资源文件名在各自-plan.json；每个resource记录真实exitcode/峰值RSS/耗时。日志内的显式“warm inspection complete”异常只是生产适配器结束检查的哨兵，外层检查finished后正式返回0，不是新解收敛标记。

下一步是在新接受实际态更新完整控制响应（可再加入vd），构造同时限制D增长与峰曲率的组合方向，并以新的真实BVP/真尾验证。正在恢复的q105固定目标不因此改动。
