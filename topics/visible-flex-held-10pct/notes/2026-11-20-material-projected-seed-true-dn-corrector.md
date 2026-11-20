# λ=.02 未合格投影场的独立 trueDN 校正入口

维护：Astra-held10-1b6d88ec-20261120；2026-11-20。

[第二次实际返回](2026-11-20-public-material-second-return.md)给出了一个真实收敛的λ=.02/M8原linearDN场，但原metric_l1约2.39e−5未门。已接受材料锚的旧 continue_material_true_tail.py 入口保持原样，不能把这一场伪装成已合格锚传进去。

新增 scripts/resume_m3/correct_projected_material_seed.py 明确仅把它作为数值初猜。要求原solver真实成功、无error、原raw及physical场与已记hash一致、q=.06/M8及当前材料配置不变。随后安装原shared/periodic/native算子，使用原tail warmup、真实尾审计、8outer联立、Frenet/BC/原metric门，仅校正当前lambda/tau；没有自动推进材料参数。

最终依然须solver成功、无error、原metric_l1≤1e−6、实际outer BC≤原bc_tol、真实tail_converged且tail residual≤2e−9。任一未过即明确失败；初始metric未门既不被抹掉，也不算完成验收。原component-l1仍只是有限入口筛选，README要求的连续relative operator norm、全部固定参数精化、闭合/全时reach/非全等还须另付。

命令在同一实际字段尚在的runner中执行：

```sh
python -u topics/visible-flex-held-10pct/scripts/resume_m3/correct_projected_material_seed.py \
  --repo /path/to/repository --workdir /path/to/runtime \
  --prefix-dir /path/to/runtime/material-lam002-linear \
  --core-config topics/visible-flex-held-10pct/scripts/resume_m3/material_support_lam002.json \
  --workers 2
```

其工作目录独立使用corrector-*，不覆盖原线性场、旧已接受锚或旧native记录。结果只在material-corrector-summary.json保存小标量，全部场留runtime。源截至发布尚未执行；不能提前填入真尾接受。

并列准备的 audit_full_relative_metric.py 与 actual_m3_metric_model.py 从同一run命令和physical.npz恢复完整真实图，不运行seed/Newton/tail。明确固定mean_nodes后再比较angular512/1024，直接评2×2relative矩阵算子范数与两种角谱。默认只是有限s/θ诊断，full_prefix_certified=false；不会把加密样本或调用方给的证书标签当作连续/向外舍入证明。
