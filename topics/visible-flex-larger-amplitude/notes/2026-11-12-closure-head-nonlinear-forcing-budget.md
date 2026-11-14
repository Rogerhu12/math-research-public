# 浅头完整非线性源项预算

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

完整证明已按根规则13登记为
[R23](../results/R23-warped-head-complete-nonlinear-source-budget.md)。

对应可执行精确账本：

```sh
python computations/closure_head_forcing_ledger.py \
  --out notes/2026-11-12-closure-head-forcing-ledger.json
```

本账本不求解 ODE，不启动大数值进程。输入的全胞元强时空范数仍需从真实径向路径或严格包络核销，不能从旧 q003 小端点值推定。

当前大作业顺序由 root 统一安排：tail 完成旧 g 最后正式响应和短谱并释放 worker 后，exact_closure 接 depth12/far225 新 g 实际求解。新的 source 参数表与 canonical Xi 转换仅增添读取和输出，accepted-trial 回调仅存 recovery checkpoint；它们不修改原求解方程或 success gate。下一实际 ready/response 包将保存 worker/source/adapter 哈希。
