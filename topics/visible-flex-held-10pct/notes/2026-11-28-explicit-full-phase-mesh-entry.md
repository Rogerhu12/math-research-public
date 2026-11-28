# 真实全闭图的显式时间范围及 R87 握持坐标入口

原 mesh exporter 和它的7a/fixed-actual入口均固定`alpha(t)=9t/20`，其握持框架还只接受旧`k=.2,S=.5,b=.2`。R87的完整设计范围却是`alpha(t)=4t/5`、`k=.5,S=.675,b=.3`。即使λ1求解正确，旧导出默认也不能覆盖R87的规定末端。本条解决这个具体接口缺口；没有新λ1场或网格返回。

原已执行源全部保持字节不变。新的`material_circle_phase_contract.py`直接用R54/R87同一个圆弧刚体公式：对真实λ1、curvature_blend=1、正短柱，读实际k/S/b并要求k等于实际target_curvature。显式给出相位末端a>0和材料宽w>0后，令握持角区间相对L为`[(a-w)/2,(a+w)/2]`，完整扫窗为`[-(a+w)/2,(a+w)/2]`，严格核它在实际字面S内。

R87取a=4/5、w=27/50，正好得到原证明中的`[13/100,67/100]`、完整扫窗`[-67/100,67/100]`。框架仍是`R_(-(1-k)*alpha)G_alpha+O-R_(k*alpha)O`。O按原核心真实求值器计算，输出只称数值求值，不将它的binary64值冒称新精确定义。这个结构检查不替代held比例、全metric或reach证明。

`explicit_phase_mesh_adapter.py`逐项核已发布两条原入口SHA，只替换CLI相位语义、圆弧参数框架及相应来源记录。原源接受门、最终physical-H、完整谱/mean、逐ring原reader对照、拓扑、全部double坐标和每文件严格5MB门均保留。新入口记录原main及实际执行main的SHA；没有改KIND或假扮7a。

在各自真正接受源和同源完整bundle到位后，使用：

```bash
python chord_export_explicit_phase_mesh.py --source-run TRUE_7A_RUN --coupling-summary TRUE_7A_SUMMARY --geometry-bundle TRUE_COMPLETE_BUNDLE --cut-width TRUE_CERTIFIED_WIDTH --phase-end 4/5 --held-width 27/50 --frame held --times 0 1/4 1/2 3/4 1 --outdir NEW_OUTPUT
python fixed_actual_export_explicit_phase_mesh.py --source-run TRUE_FIXED_ACTUAL_RUN --geometry-bundle TRUE_COMPLETE_BUNDLE --cut-width TRUE_CERTIFIED_WIDTH --phase-end 4/5 --held-width 27/50 --frame held --times 0 1/4 1/2 3/4 1 --outdir NEW_OUTPUT
```

两个来源入口仍各认自己的真实数值生产者；正在独立准备的QR full-DN生产者如有新source协议，必须用其真实reader接同一phase工具，不能重标为旧7a。

实际只编译四源、逐处核对声明的main替换并运行两个真实`--help`，均exit0，显示required `--phase-end`及`--held-width`。未代入假正向模型、未重算BVP/native/几何、未生成网格，也没有C²收敛或本题完成声明。来源与实际准备记录见[小JSON](2026-11-28-explicit-full-phase-mesh-entry.json)。
