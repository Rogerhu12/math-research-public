# 强分支实际 H 的新有理深 g 作业准备

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**仅已准备，未启动Node。** 当前团队大作业窗口依root调度，本文件不改变队列。

输入为成功的旧g实际响应
`notes/2026-11-12-root-vu032-q085-actual-resumable-m16-tail-response_0003.json.gz`，
保留全部16个H系数，包括
$H_2=-2.1668389630452756\times10^{-5}$。

准备器已逐项比较全部30个相关几何/求积输入，与q003新有理深模型所冻结的浅头配置一致。新作业保留浅头的二进制global warp alpha及其source fingerprint，另明确把 $n\ge160$ 的真实源改为 $\alpha_n=65/64$。因此旧响应只是warm start，不是被重命名为同g加密结果。

已经落盘：

- `notes/2026-11-12-closure-newg-strong-vu032-q085-m16-d12-f225-plan.json`
- `notes/2026-11-12-closure-newg-strong-vu032-q085-m16-d12-f225-config.json`

从原M16、角quadrature512、depth8、steps12、parts8、linearFar48、linearSteps2048，改为同M16/512/12/parts8，nonlinear depth12和linearFar225。原success tolerance、maxIterations、完整实际H和源参数都保留。请求省略外层高度Jacobian，仅要求真实尾响应及完整audit。

计划记录旧输入、配置、参考ready、source实现和10个本地入口的SHA256，执行前逐项核对。仅在root明确交付大Node窗口后运行：

```sh
python computations/closure_new_metric_endpoint_job.py run \
  --plan notes/2026-11-12-closure-newg-strong-vu032-q085-m16-d12-f225-plan.json \
  --node-heap 768
```

worker会在已接受trial后即时保存 `iteration-recovery-only`。如果进程中断，保留所有原输出，并以新的prefix准备恢复作业：

```sh
python computations/closure_new_metric_endpoint_job.py recover \
  --plan notes/2026-11-12-closure-newg-strong-vu032-q085-m16-d12-f225-plan.json \
  --out-prefix notes/2026-11-12-closure-newg-strong-vu032-q085-m16-d12-f225-resume1
```

`recover`只读原计划指定的recovery文件，原完整H和求解门不变；它不把checkpoint标记为已收敛。之后仍需在获分配的窗口运行新的plan。

准备器也可对以后成功的M20或M32完整实际响应重新准备一个独立新prefix，并重新核对所有几何输入。未成功的outer worker输出不能冒作成功响应输入。

真实source outer cut的 $R_{\rm out},E,E_r$ 与保存port的区别仍按R26保留。有限新g响应完成后，还必须核对全胞元源/Green预算、未表示频率及真实R18 trace；计划不预先宣告这些条件已经支付。
