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

## 本次已实际返回的恢复链

从公开结果版本 `c9c5e7da2fc690e9d046fc7297cecde2d0412150`（07:20:57 UTC）读取：七档小幅度及 λ0 exact-lift 已实际通过原 solver/raw/physical/metric 门。下表是此次新chart上的实际返回，不登记为新的存在性结论。

| 实际阶段 | 节点 | RMS | 原有限 metric | 身份 |
|---|---:|---:|---:|---|
| q006_linear_m8 | 598 | 9.980240988e-07 | 5.590336282e-09 | 原门通过 |
| q012_linear_m8 | 603 | 9.79328084e-07 | 1.133183395e-08 | 原门通过 |
| q020_linear_m8 | 606 | 9.902730133e-07 | 1.922357551e-08 | 原门通过 |
| q030_linear_m8 | 610 | 9.984644272e-07 | 2.94708925e-08 | 原门通过 |
| q040_linear_m8 | 850 | 9.841842431e-07 | 4.015882858e-08 | 原门通过 |
| q050_linear_m8 | 903 | 9.973606919e-07 | 7.91015673e-08 | 原门通过 |
| q060_linear_m8 | 622 | 9.912228426e-07 | 4.091571675e-07 | 原门通过 |
| lambda0_exact_lift_m8 | 622 | 9.912230563e-07 | 5.455217033e-07 | 原门通过 |
| lambda002_m8_transfer_initializer | 622 | 9.927135478e-07 | 3.193207023e-05 | metric 未门；只作完整升谱初猜 |
| lambda002_m16 | 628 | 9.927099303e-07 | 4.272493001e-06 | metric 未门；只作完整升谱初猜 |

对应 run/raw/physical/checkpoint SHA 与 M8/M16 原export实际返回保存在 [lowq-accepted-recovery.json](2026-11-26-lowq-accepted-recovery.json)。端口物理 parameters/cut 逐项相同，完整包 SHA 不同历史值；不把包差解释成数值坡率相等。q/delta/warp 仍为设计变量，不计固定g精化或10%新成果。

该可见版本正求 λ.002/M24。07:21:58 起原worker因组合诊断超过64KiB而返回 omitted；从此不能推断M24终态或子路线已启动。原计算保留，等待实际可读返回。独立warm通道为本身runner必要再生同一链；其源/输出hash按实际文件记录，不能借另一runner的接受标签替代。
