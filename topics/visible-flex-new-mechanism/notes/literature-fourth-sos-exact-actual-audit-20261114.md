# R50 完整平方恒等式的公开运行审计：43611706012

2026-11-14，root。实际运行：[public Actions 43611706012](https://github.com/Rogerhu12/math-research-public/actions/runs/43611706012)，源码提交 `13ba4296f09fb04ee82c2c6386c44fcd1ec69c1a`。没有几何 ODE、数值积分、设计或优化。

按 [原始回执](actions-43611706012-1-fourth_sos_exact/receipt.json) 逐件读取源提交，**71 个来源文件**的字节数与 SHA256 全部一致。唯一输出 `fourth-disjoint-sos-exact.json` 为 775 字节，SHA256 `a394c455dd52af6a923338842b2dcbed93142c13c14706ba764b7b98f2c1b372`，与已提交开发证书原字节完全相同。

脚本 `literature_fourth_disjoint_sos_certificate.py` 的 SHA256 是 `0479a6c635a3e999b5bf69c3b99fdb5be295c63d13550a4c54ca451660bf414a`。五个准确符号差均为零：真实非局部尾的总导数、消去三阶 jet 的分部积分、完整平方和的总导数、任意固定混合目标的相位多项式，以及其二次系数。正下界系数准确为 `1/4608`。runner 实际 pull 后两 README 无变化。

本结果复核 [R50](../results/R50-disjoint-profile-circle-fourth-order-positive-obstruction.md) 的代数。实 profile、支撑不交、能量相等、常状态 k=0/h=1/omega=0、全 range 与二/三阶 gauge 范围仍由该文完整证明负责。它不排除真正重叠的 profile 平面或一般有限族，不能当作主课题完成。该准确代数项已成，不重复运行。
