# 冻结原坐标的v2同图入口

会话：Astra-held10-06bbeb39-20261126。状态：首执行的记录序列化故障已由真实日志定位并最小修复；真实重验与后续λ解排同runner。

原631节点场的只读probe已经实际通过，证据见[执行记录](2026-11-26-warm-handoff-equivalence-execution.json)。新独立provider/model/入口均有v2版本；原v1源保留，可以重放其已登记失败。

- 新provider沿用同一R65几何核，以实际legacy floor1e−9反解控制，恢复明确的d_j=phase_scale·p_(j−1)合同；在d=0完整核心不变。
- model_v2明确冻结原chart_join、chart_reference_prefix和chart_breaks，不把冻结δ顺带导致的默认坐标变化混入此交接。
- qaux域guard在扩大一个单位的log区间之外先拒试探，原边界仍由原exp后范围检查决定，所有实际有效值和几何/metric域门不改。
- 首入口绑定真实原run/raw/physical及已完成probe，自己再实算原RMS所有节点和取样点的坐标、f/fm、collocation与两种BC逐位相等；没有调用BVP。
- raw的x/y/cubic与physical的x/c保持原值，只把参数坐标改为全零，再以同mean1168在原角floor和两倍floor重新审完整相对metric。任一实际门不通过都不给accepted。

通过后的来源类型是 `same_cartesian_map_verified_reexpression`；`solver_invoked=false`、`solver_success=null`、`raw_return.success=null`，原真实求解来源单独保在source_solver_provenance。后续真实暖BVP将使用另一来源类型 `actual_warm_bvp_return`。统一accepted_input检查对应身份、所有实际原门和raw/physical/metric报告SHA；不能用新文件名或一个布尔标签替代验收。

本步骤只把已有λ=.002场表达在明确的新控制坐标中，不算λ前进，不算新BVP成功，也不算闭面、fullH或固定问题收敛。λ变化仍需真实求解，λ1后的完整固定问题和几何标准仍待完成。

命令（所有大输出在checkout外）：

```bash
python scripts/resume_20261126/warm_zero_control_reexpression_v2.py \
  --source-run WORK/warm-prefix-recovery/lambda002_m24/run.json \
  --probe-summary WORK/warm-handoff-probe-01/summary.json \
  --outdir WORK/warm-v2-anchor
```

## 实际入口故障与后继执行

首进程在literal_raw_equations_verified事件保存时发生NumPy bool不可JSON序列化，未到完整metric审计；[实际日志证据](2026-11-26-warm-v2-entry-failure.json)保留命令/源码/log SHA和完整错误位置。只把4个比较转成内置bool，不改变几何、方程、误差门或已有场。旧失败目录保留，新父入口使用新目录；原恢复与只读probe均不重做。

v2 step/continue已由root与actual_tail独立审阅：每步从实际accepted源作完整lift并调用solve_bvp；保原raw网格，只有明确refine才新增径向节点。只有真实BVP通过且实际metric报告超门才升M，其他失败从最后accepted二分λ，失败场永不晋源。RHS每8点、Jac分批与释放已失效LU只减少峰值内存，记录原/运行Newton函数SHA；原阻尼、RMS/BC/physicalBC和完整双角metric门不改，不称逐位同。

执行命令：

```bash
python scripts/resume_20261126/warm_fixed_m3_continue_v2.py \
  --repo REPO --work WORK \
  --source-run WORK/warm-prefix-recovery/lambda002_m24/run.json \
  --probe-summary WORK/warm-handoff-probe-01/summary.json \
  --outdir WORK/warm-v2-design
```

该命令先真实验证同图重表达，只有accepted_input接受后才开始λ>.002设计；任何实际结果另行登记，当前不预认λ前进。

## 实际同图验收已通过

[实际小记录](2026-11-26-warm-v2-anchor-actual.json)绑定原source、实际新run/raw和全部原方程逐位等式。双角1168/2336完整相对metric最大分别为6.482415781989006e−7与6.482415812048341e−7，sample operator均为5.449318613117554e−7；原631点RMS9.927150345213775e−7。身份仍是重表达、solver_invoked=false/solver_success=null，不新增BVP成功。父入口已经开始原631点上的λ.004真实求解；当前尚无该步accepted，不把同图审计算λ前进。
