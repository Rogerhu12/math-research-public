# R150：已成七关系之后，只续真正相容的 j=6、9

状态：本入口尚未执行；本地环境仍失联，未声称已通过 AST 或新 C++ 编译。它复用实际 run 43630666145 的全部七来源、原16式、正常形、Q/rem/trace、完整315商，不重新运行它们。

## 输入与运行

三个固定恢复输入：

- T96：run43597823809 / artifact14114364261；
- all198：run43619888599 / artifact14124017685，只取已成15文件；
- 七关系：run43630666145 / artifact14127663630，只取 contract 中8个真实文件。

仓库仍提供原 model、完整315 state 与原 reader。每个输入的准确 SHA 固定在 contract；不从已知结论重算或猜测矩阵。

命令：

    PYTHONDONTWRITEBYTECODE=1 python \
      NOTES/2026-11-14-r150-seven-compatible-pair-runner-789f.py \
      --notes-root NOTES --t96-recovery T96 --all198-recovery ALL198 \
      --seven-recovery SEVEN --out OUTPUT \
      --math-seconds 120 --memory-mib 512 --compile-seconds 30

四个编译各30秒，编译及固定输入核对不计入数学时钟。保存矩阵分析和新 pair image、VQ、原预基运输、完整原式共用一个120秒时钟，每进程512 MiB。不是四个各120秒。真实 VQ 数组和原式乘积数组及来源前缀可恢复；其余阶段仅复用已完成的内容绑定缓存。

接续时提供 --resume-recovery PREVIOUS/recovery，不改原输入 SHA。压缩保存在数学时钟结束后执行，所有实际 JSON stage-cache 和原流均保存；gzip 每片至多4500000字节。

## 只对真相容的两列恢复原式

实际新β基是7003，两个真完整系数分别为30、18。使用源 run 的真实 C 矩阵相应两列。新的原像右端是

$$
r_{3,j}-f_j\beta_{7003}-B C_j,\qquad
(f_6,f_9)=(30,18).
$$

四个保存族直接混合：

1. 已成新16列的 NF/Q/rem/trace，系数为 $[-F;E_{\{6,9\}}]$；
2. 原两第一除源，系数为 $-C_{1:2}$；
3. 原四第二除源，系数为 $-C_{3:6}$；
4. 原 selected2 第二除源，系数为 $-C_7$。

完整像身份及零余先核清，再恢复这两列来源 $w$。来源 native 只将已成 source7 的 nt、真实标签和元数据改为2及[6,9]；原 R 的九个尾目标仍完整读取，不删成两个。真实来源字典和 kernel 标准约化保持原值。

原式最终来源为

$$
Z_j^{\rm next}
=Z_j+f_jK_{3,7003}
+p^2(\kappa_1 C_{1,j}+\kappa_2C_{2,j})
+p\sum_{i=3}^7\kappa_i C_{i,j}
+p^3w_j .
$$

使用已成 R150P431 原16来源束，只选择真实7003及原j6/j9。完整乘回原17/6188/4367，目标明确是31h0，不是H0，也不是两个重标号的t2/t3。新的原式 helper 将目标指数直接读自标签[6,9]。完整模923521核过之后才能报告两列完成。

## 保存矩阵的下一结构信息

同一任务在恢复 pair 之前读取已成119064B全局系统：

- 核并导出实际七个新第一像的标量 $c_i$；
- 取7003为真实第八列，核其商上作用确为s=2；
- 完整315坐标构造八维 U8，核 J8，导出 $(s-2)b_8$ 的旧七列修正；
- 在完整315、商U后308、商U8后307三个真实空间，分别求九个原余及其共同的准确最小ann，全部乘回核零；不先假定只在1/2；
- 保存对应完整矩阵、每个目标原余非零数和后继七核的明确系数。

这只是已成矩阵的精确后处理，没有重算七个原余。它不计算新的δ2；对后续全像，必须区分已覆盖的1/2 primary与其它主部分。

## 完成与范围

主回执：

    results/seven-compatible-pair-pipeline-receipt.json

只有以下条件全满足才是这两个目标的原式完成：

- status=completed；
- outcome=targets6-and9-full-original31h0-mod923521-certificate；
- actualTargetLabels=[6,9]；
- fullOriginalPairMod923521IdentityVerified=true；
- finite_budget_verified=true。

otherSevenOriginalTargetsNotRecomputed=true 和 wholeNineTargetIdentityClaimed=false 必须保留。七个不相容目标的旧固定初值障碍没有被本任务更改。实际来源费用从 actualFinalSourceCosts 读取；88+96仅是预先付清的图界。

保存矩阵分析另在 recovery/saved-matrix-analysis/ 中，明确 exactThirdSmithValuationClaimed=false、newSecondBocksteinComputed=false。即使两列全部通过，仍只证明相应固定精度原式，不声称特征零来源。
