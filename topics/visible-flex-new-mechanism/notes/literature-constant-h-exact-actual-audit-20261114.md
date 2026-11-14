# R31 准确矩式与 Klein 闭合恒等的公开 Actions 审计

2026-11-14。实际运行 [43601439290](https://github.com/Rogerhu12/math-research-public/actions/runs/43601439290)，源提交 `b43250b608f9844a22d52ce66a3f7a2cd15d675e`，lane `constant_h_exact`。工作流成功只表示这次准确代数检查完成；不是主课题通过。

输出为 [constant-h-moments-and-klein-exact.json](actions-43601439290-1-constant_h_exact/constant-h-moments-and-klein-exact.json)，SHA256 `990834647c6987ebc0f067f48827058c5c9552fb943c68674149206557565f96`。运行脚本 SHA256 为 `58b997fc49d1ffcd496866ccec49ef1f4976048a20fc074d74eea809d6f09563`。逐项从源提交读取并核对 receipt 的 58 个源文件及唯一输出，字节数和 SHA256 全部一致。publisher 在 rebase 后重新核根/本题 README，记录差异为空。

## 实际检查结果

Python `Fraction` 稀疏多项式与 Laurent 多项式准确核验：矩阵迹为零；中央矩行列式八项恒等成立；`det M=-32 det B` 成立。两频函数的四个平均值分别为 `5/8, 3/8, 1, 3/8`，行列式的首项系数为 `3/4096`。

极限参数 `a=20,e=1/3,D_energy=20740/27,xi=31/3` 给 `C=0`、`C'=679/36`、`W=-1037/27`，比值准确为 `-4148/2037`，严格落在 R26 的开区间中。输出同时保留：**该极限本身的 Kjet 为零**。有限高频微扰修复非退化性的论证在 R31 正文，不能把极限数据直接叫作非退化有限几何。

Klein 四旋转矩阵和为零、所给 Euler 词准确遍历八条有向边、半转把第一轴送到负第三轴，均为准确恒等。

## 证据范围

本次没有评价真实几何、调用优化器、运行研究 ODE、选择有限 `n/N` 或认证任何闭曲面。平滑框架连接及“先取有限 n、再取有限 N”的存在性由 [R31](../results/R31-closed-geometry-negative-physical-root-and-local-phase.md) 的证明承担；嵌入、reach、完整外尾和有限等距族仍未得到。
