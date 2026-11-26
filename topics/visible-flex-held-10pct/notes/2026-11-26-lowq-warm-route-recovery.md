# 原成功小幅度路径的必要再生

当前原M24冷输入已真实失败；截M24控制的M16冷输入到1954节点仍大残差，尚无终态。旧完整场丢失后，为得到其所在的真实分支，使用前会话已成功的新g小幅度路径再生，既有数学结果不重登记。

独立公开 workflow `.github/workflows/held10-live-lowq.yml` 只由一次start请求启动；沿用原live worker的来源/规则差异检查、诊断白名单、路径范围和每小时pull，增加独立 `--channel lowq` 分隔command/result/state，不影响现有material进程。只在runner保存完整场，公开回传源/命令/hash/小结果。

入口：`scripts/resume_20261126/lowq_prefix_recovery.py --repo REPO --work WORK --outdir WORK/lowq-prefix-recovery`。bootstrap仍是已验证的tail_recovery_setup，恢复70源/native/完整物理port/chart。随后按原shared exporter取M8/N128和M16/N256，物理parameters/cut必须与M24完全相同；实际SHA另记，不凭参数猜逐字匹配。

1. 原portable BVP：q及warp同步为.006,.012,.02,.03,.04,.05,.06，M8/256，原tol1e−6、BC1e−7、physicalBC2e−9/maxnodes6000。每一步必须真正solver+完整physical+原metric门通过，使用前一步完整checkpoint。
2. λ0/tau1/S.5/b.2/k.2的完整lift重求；raw仅作初猜，lift系数1，仍须原门。
3. λ.002 M8原BVP；M16和M24按R48完整两jet lift。M8/M16只有真实solver成功及完整物理场才可作升谱初猜，其原metric未门身份保留；M24必须所有原有限前缀门通过。
4. 只有实际M24通过才启动已声明的fullH、固定g诊断及λ设计三路；各路结果不能拼成同一个合格场。

新runner使用原driver、原域和原解析参数列，没有应用未实跑的δ域内差分适配，也没有截静态controls冷开；observer只记录真实Jac/LU及保存未接受初猜。准备脚本通过编译和CLI检查；本note初次提交时尚无第二runner数值结果。新小结果随后即记即推。
