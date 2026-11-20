# 旧材料 λ=.02：M24 原前缀实际通过并接原真尾

维护会话：Astra-held10-1b6d88ec-20261120。

本条续 [M8/M12/M16实际记录](2026-11-20-material-m8-true-dn-and-m12-linear-return.md)。
旧短ramp的reach障碍没有消失；本分支用于真实尾和固定参数场接口实测，
没有以旧模型推进最终10%几何的声明。新宽多段g另行计算。

## 实际执行与门

Actions run44720589640/job136234983080 的命令
`held10-material-m24-stage-01` 已全部五阶段 exit0；原M16升M24
端口只装已付的共享分配修改，原Node heap=2048不变。
同原模型完整lift、原BVP和两个operator评价都真正执行。

| 指标 | 实际值 |
|---|---:|
| 原节点数 | 605 |
| DomainNewton完整接受步 | 1 |
| domain/merit拒绝/no_step | 0/0/0 |
| collocation RMS | 9.990839180580315e-7 |
| 原 metric_l1 | **2.950911661714551e-7** |
| physical linear DN BC | 1.761764479935745e-14 |
| flow_defect（另列） | 2.9893214255914183e-6 |
| Darboux l1（另列） | .0018886017514948995 |
| raw p0（δ增量） | -1.5881496901682128e-8 |
| 支撑幅度q | .06 |

原有限metric与边界门通过。完整c6,...,c72与原数值p、全部阶段argv在
[短执行记录](2026-11-20-material-m24-actual-return.json)。
δ及核心c仍是设计未知量；M12→M16→M24不是固定完整g的收敛证明。

原前缀audit使用**mean1168/GL6**。独立审计明确选择固定mean512，
N1024和N2048均得到sampled relative operator
**2.539100933951488e-7**，峰位s=.08820768573127918、ψ=θ=π。
相对矩阵(ss,st,tt)为
[-2.539100933951488e-7,-2.8094490856098124e-17,7.516908873128614e-9]，
共同节点分量差0。这是固定mean512 proxy的有限节点结论；
与原mean1168完整图的连续差量尚未支付，不能混成同一个严格证书。

M16→M24完整lift系数是1。2336角×103径向点的六jet差最大
8.662585850030506e-15；入口投影改变8.88378746274874e-8。
传递节点只是原BVP初猜，不声明新cubic与旧quintic恒等。

| 对象 | SHA256 |
|---|---|
| M24 raw | 8aee00ee6d6468a032e491833f570a8fcd360f493cce583a51d3d75e80e5e4d3 |
| M24 physical | 90750aa2d47bc57786ef5d86448dc0b79d0faa40c598b4c6adf022b6ae49255d |
| M24 run | 32f872e18640756fc64d7c8e08a436a8c03572b8300831e595fe7a8cc39a2bc1 |
| actual M24 port | 42369d1571413fd4ecccea43ccfef233f4b97506f71e28b86ed9735c28c2d93b |
| tail settings | 37bc9073d2dba1d110b165b5febbb054d1dd1a8ca09ec23b86e2d76c39f08f46 |
| lifted raw初猜 | 60d6e78b92798b070909d5a6bc6453488d85c2d5815ec4338e181f11b4d12f8e |

## 可复现入口与原真尾接续

REPO为仓库，WORK为同一live工作树；不需要重跑已完成M8恢复。
原M24入口如下，完整各阶段argv另在短记录。

~~~bash
python "$REPO/topics/visible-flex-held-10pct/scripts/resume_m3/extend_material_mode_stage.py" \
  --repo "$REPO" \
  --source-run "$WORK/material-lam002-m16-linear/run.json" \
  --tail-config "$WORK/material-lam002-m16-transfer/tail-settings.json" \
  --outdir "$WORK/material-lam002-m24-stage" \
  --modes 24 --mean-nodes 512 --angular 1024 2048
~~~

新的 `continue_actual_mode_true_tail.py` 从实际run读取完整argv、
物理raw/field身份和所有原输入。它保原profile/chart/core/port/
物理参数初值/角分辨率/原八轮预算和门；仅在独立source安装已有
shared/periodic/native接口，然后添加同物理tail-config与原warmup。
不调用硬码M8的旧bootstrap入口；不修改材料λ。native范围由实际
M24/spacing3/N512/steps16/2workers绑定，子环境清LD继承问题。
源仅已py_compile；本条提交时尚无此新M24真尾终态。

~~~bash
python "$REPO/topics/visible-flex-held-10pct/scripts/resume_m3/continue_actual_mode_true_tail.py" \
  --repo "$REPO" \
  --source-run "$WORK/material-lam002-m24-stage/linear/run.json" \
  --tail-config "$WORK/material-lam002-m24-stage/tail-settings.json" \
  --outdir "$WORK/material-lam002-m24-true-dn" --workers 2
~~~

新命令 `held10-material-m24-true-dn-01` 的返回另记。只有原BVP、
原trueDN、射击和原metric全通过才报有限接受；失败照原门记录。
随后需显式将最终δ并入冻结cfg、固定q/全部c与完整均值合同，才可
调用固定物理场精化接口。这里没有完整闭合、C²族、reach或held结论。

## 真实入口故障：未启动 M24 真尾

2026-11-20 12:36:12 UTC，Actions run44720589640 以 failure 终止。
worker 读新命令时发现诊断请求中的 input/native 两个顶层字段未获
既有白名单允许，抛出 ValueError: Diagnostic top key is not whitelisted。
这发生在 subprocess 启动之前；因此没有新的 M24 真尾或失败数学迭代。
上面的五阶段 M24 前缀已完成，其原结果不被此入口错误撤销。

请求已删掉两个不合规诊断键，保原白名单，没有放开数据导出。
原 runner 已结束，当前环境没有该旧 M24 原场副本，不能声称仍可直接
接续它。源、参数、命令及小结果均已发布；若以后确有数学需要，须按
记录必要再生，而不是伪造原 checkpoint 或称重算为新结论。

当前新g M24的原真尾在独立本地 session42787 持续，固定参数接口实测
转接该实际新g；没有为这个旧reach障碍模型重复整条计算链。
