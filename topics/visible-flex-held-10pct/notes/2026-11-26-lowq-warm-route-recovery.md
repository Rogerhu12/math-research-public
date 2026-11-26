# 原成功小幅度路径的必要再生

当前原M24冷输入已真实失败；截M24控制的M16冷输入到1954节点仍大残差，尚无终态。旧完整场丢失后，为得到其所在的真实分支，使用前会话已成功的新g小幅度路径再生，既有数学结果不重登记。

独立公开 workflow `.github/workflows/held10-live-lowq.yml` 只由一次start请求启动；沿用原live worker的来源/规则差异检查、诊断白名单、路径范围和每小时pull，增加独立 `--channel lowq` 分隔command/result/state，不影响现有material进程。只在runner保存完整场，公开回传源/命令/hash/小结果。

入口：`scripts/resume_20261126/lowq_prefix_recovery.py --repo REPO --work WORK --outdir WORK/lowq-prefix-recovery`。bootstrap仍是已验证的tail_recovery_setup，恢复70源/native/完整物理port/chart。随后按原shared exporter取M8/N128和M16/N256，物理parameters/cut必须与M24完全相同；实际SHA另记，不凭参数猜逐字匹配。

1. 原portable BVP：q及warp同步为.006,.012,.02,.03,.04,.05,.06，M8/256，原tol1e−6、BC1e−7、physicalBC2e−9/maxnodes6000。每一步必须真正solver+完整physical+原metric门通过，使用前一步完整checkpoint。
2. λ0/tau1/S.5/b.2/k.2的完整lift重求；raw仅作初猜，lift系数1，仍须原门。
3. λ.002 M8原BVP；M16和M24按R48完整两jet lift。M8/M16只有真实solver成功及完整物理场才可作升谱初猜，其原metric未门身份保留；M24必须所有原有限前缀门通过。
4. 只有实际M24通过才启动已声明的fullH、固定g诊断及λ设计三路；各路结果不能拼成同一个合格场。

新runner使用原driver、原域和原解析参数列，没有应用未实跑的δ域内差分适配，也没有截静态controls冷开；observer只记录真实Jac/LU及保存未接受初猜。准备脚本通过编译和CLI检查；本note初次提交时尚无第二runner数值结果。新小结果随后即记即推。

## 实际首返回及不同数值坐标表的明确处理

run45772029917首命令已真正exit2，尚未导port或求BVP：再生chart SHA为69a3e8eb38463644119f22beec88824429ec8c480e812e7fc97a9fdbdcdde3f5，不是历史dc85dda524e03896b4afa552bd1f859b73cf96f88033565ff910e227034f2f93。原generator只存scope、reference_profile、65knots/values及末导数，没有时间/路径字段，不能称元数据差。完整旧65值已丢失，不能虚报差为零或给未计算的最大差。实测绑定见同日lowq-chart-precondition-return.json。

新请求held10-lowq-current-chart-20261126-02在同一存活runner续做，输出另用lowq-prefix-recovery-current-chart。明确使用本次再生的数值坐标函数，先核setup manifest实际SHA、有限65节点/值、[0,1]递增节点和原clamped spline两jet，再检查q≤.06对应原角图的基础采样域。该采样不是连续证书；每一实际原BVP仍检查域与全部物理/metric门。全链固定这同一chart并逐阶段重核SHA，保物理profile、尾背景、核心圆化输入的硬绑定。

这是本次恢复的数值坐标输入变化，不冒充历史chart逐字重现，也不把它当已证的同g精化。原物理多段g不由参考chart的reference_profile替换，后续固定g序列仍必须明确冻结实际chart。初次本地恢复记录中的历史chart同SHA结论只对应当时本地文件，不能外推为所有公共环境再生结果。
