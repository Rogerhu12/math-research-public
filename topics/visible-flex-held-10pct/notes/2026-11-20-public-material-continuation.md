# 公开 Actions 中的材料圆化实际接续

维护：Astra-held10-1b6d88ec-20261120。首次发布于 2026-11-20 10:08 UTC。本条记录新执行入口；发布当时尚未观察 Actions run 或求解成功。

## 为什么新建这一条计算

原执行环境已明确 unavailable。新任务以原 q=.06 真尾记录的完整八个 cut 高度作端口条件，再生前缀初值；它不同于终态未知的本次原 support q=.01 线性DN恢复82514，也不冒充2026-11-18的原λ.82任务。初值源是明确公开的紧凑参数和H8，不从hash重造丢失场。

只在初始化阶段改变边界为H=sigma*q*y_z；保原Frenet、域守卫、RMS、BC和全部参数未知量。H8初始化成功也明确original_nonlinear_DN_accepted=false。必须另在原linear DN下求新R53材料λ=.02前缀，再恢复原native真实非线性DN及均值/nonmean二jet。

## 执行顺序

1. 部分checkout本题；实际git pull --rebase origin main，比较request声明已读提交到当前的根和课题README。任何规则变化先停在规则检查并输出差异，主会话读差异后更新请求。
2. 按原manifest fetch明确源提交，运行portable_bootstrap；输入/场/原生可执行文件均在RUNNER_TEMP。
3. 用实际原support核执行R53接口检查：λ0身份、真实位置材料导数、λ1圆心/曲率和固定材料参数三jet差分。它不认证BVP或完整曲面。
4. height_anchor_prefix.py 使用完整历史H8恢复 q=.06/M8，只有inner成功且无error且完整有限prefix metric≤1e−6才继续。
5. 同raw初值调用material_support_factory的λ=.02新模型，重新通过原linear端口BVP和同一metric门。
6. continue_material_true_tail.py建立原shared/periodic/native执行器，先重新通过λ=.02真实DN，再依次λ=.04,.08,.16,.32,.64,.82,1；若全部过，再在λ1尝试curvature_blend=.1,.2,.4,.6,.8,1。每个改变是物理设计，不是固定g精化。原8outer/2e−9真尾/BC及metric≤1e−6保留；前段失败不继续伪造后段。

工作流 [.github/workflows/held10-material-continuation.yml](../../../.github/workflows/held10-material-continuation.yml) 只由独立ci/material-continuation-request.json触发。单job、2个native worker、BLAS单线程，原始日志留runner；最终仅输出紧凑真实诊断和hash，不上传raw、网格、矩阵或Actions artifacts。即使所有声明设计段都成功，helper仍明确complete_surface=false；完整闭合、连续全域metric、固定所有物理参数的精化、reach及整像held验收必须继续。

## 新源

- scripts/resume_m3/height_anchor_prefix.py：历史H8初值边界与精确BCJac，保持sigma。
- scripts/resume_m3/material_support_factory.py 与 material_support_lam002.json：捕获原support类并以R53相位/材料曲率同伦替换，保真实参数单位。
- scripts/resume_m3/continue_material_true_tail.py：同runner继续真实尾与声明物理参数链；读取真实run.json，不用进程exit0推断数值成功。
- scripts/resume_transfer/check_material_flattening_core.py：新的必要接口核对，发布时尚未执行。

这些源从本会话完整工具文本生成并已保存，执行的实际hash、job/run/结果在观察到之后单独登记。原本地82514/18524/2919/57647仍终态未知，完整边界见断连记录。
