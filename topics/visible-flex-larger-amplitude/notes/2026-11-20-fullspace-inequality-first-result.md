# 完整余量不等式 QP：首方向的真实结果与后继依据

## 1. 来源、执行范围及规范纠正

以下是已经启动并自然结束的一次本地数值诊断及其已启动后验读的事实记录。它没有公开 GitHub Actions run/artifact，不能冒充已经通过题 README 的公开科学计算要求。根在复核题 README「计算用本仓库的 GitHub Actions」后已纠正后续路径；本支没有再启动新的本地场读取、求解或科学测试。后继复现和新算法的必要测试均安排到公开 Actions。

本地首方向 session51104 自然 exit0；后验 session84914 也自然 exit0，没有未结束的本地科学进程。记录已经发生的结果不意味着以本地诊断替代公开Actions执行要求。

真实父为 `curvature-qp-spectral-hessian-r22-restore-three.npz`，SHA-256 `35f74961a297775f7e38c01cee7f9ed5516e98c48964f758f1795b76d2061ebf`。同一 g、原923节点/922胞、M160、7377径向观察、2048完整角行及513精确轨道代表不变。

原1,332,245自由变量、全部 DI A/E/D 和端口保留。增量采用已刊物理高度映射与 νc24 正角向范数，另有 m≤12/r22 的2534个冗余粗列在同范数中白化。实际目标是 p8 正谱 Φ，p=8、ε=.001、scale=.05，固定于整条回溯；原 Jw 仅同步报告。

## 2. 真实初态、完整位置集合与二次模型

本轮纯位置清单 `fullqp-35f-all-known-locations.json`，37552B，SHA-256 `7c0edba0b9c502c6409cbfeccdfc1f3d649c1e3ae6135d03143d72c26517bf34`，包含973个 κ 位置、165个半径位置和14个 protected 位置。它合并 geometry 的921/150历史位置与完整方向支线的新拒绝峰、后验局部点；所有值在35f父上重新读出。

初态 Φ=1.1923035857631737e-7，max relative Gram=.013343526276563303，Jw=.19654005323887383。全部 Gauss 加1138个永久位置给 K=8.070936772955928、Dlb=4.096558331489566，点乘积 .03 Dlb K=.9918918984053982<.992。这个父在本轮实际并集下可从 z=0 开始；不是套用旧标签。

二次模型使用 exact residual-Hessian 桥和真正半梯度。A 与虚拟右端 v 同乘 sqrt(1600/C0)，C0=4856.422137302683；v 使用 B^{-T}Traw* h(E)，不是 B*r。正则 µ=.012063248414946114 已在平均 Φ 单位。虚拟右端平方不是实际 Φ，报告不作该等同。

选出的192条线性条件都是实际余量不等式

$$
C_i z\le(.992-.03D_i|\kappa_i|)/\|g_i\|,
\quad
C_i=g_i/\|g_i\|,
\quad
g_i=.03\{D_i\operatorname{sgn}(\kappa_i)d\kappa_i+|\kappa_i|dD_i\}T.
$$

没有额外减 .0002，也没有把192行先变成同次等式。所有永久位置仍参加每次真实非线性几何筛选。C 的 scratch 缓存为2,051,701,248B；半径余向量惰性生成，实际仅生成1个完整百万维半径余向量，避免预存165份。

## 3. 内迭代与真实回溯

一般可行 active-set CG 前进256次，线性阶段596.836868077s；整方向和回溯641.8410853140012s。真实进程 peak RSS=1,687,676KiB。最终活动行8条，活动Q内存85,487,552B；literal 线性可行性误差约1e-20，最大的已选原产品线性预测为.992。

内迭代状态是 `iteration_limit`，不是 QP 最优证书。初始梯度范数8.636482352520271e-6；面内停止阈值9.636482352520271e-12；最终面内投影梯度4.232443743733279e-11。程序当时只在达到面内阈值后释放负乘子，所以本次没有发生释放；最终乘子中有负值，最小为-.0034062583954612194。

这个原始乘子幅度不能直接等同于物理下降大小：活动行最小新增正交分量仅3.2017543014246326e-7，具有明显近相关性。后继释放判据应看单位可行释放方向的实际负方向导数，不凭 raw λ 大小宣称主要失效机制。

活动Q正交误差4.285460875053104e-14，互补性数值残差3.50154475137608e-23。完整坐标步范数.004319745031272853，端口误差2.4246318115154347e-20，满步 δH=-4.813647274450421e-5。

| α | 真 Φ | 最大 relative Gram | 真 Jw | .03 Dlb K | 接受 |
|---:|---:|---:|---:|---:|:---:|
| 1 | 1.1134243974967098e-7 | .013157790763715713 | .19477489747766882 | .9931045129444934 | 否 |
| 1/2 | 1.1472739795635903e-7 | .013250087886839354 | .19552657286390884 | .992138265241925 | 否 |
| 1/4 | 1.1683565831314446e-7 | .013296667337010631 | .19600059179855125 | .9918500157507475 | 是 |

满步实际 Φ 与模型预测1.1143299655471469e-7接近；满步和半步都由几何筛选拒绝。拒绝产品仍小于真正必要阈值1，不能把超内部余量.992写成已经证明真实 reach 失败。

接受态 all raw SSE=668.0017041658508、legacy raw SSE=167.10606201789628、H=1.877700394610227。接受时 max Gram 仍远高于1e-6，不能收尾。

方向数组 SHA-256 `60065d6cff2692c64479d922e56b33f609c41cd7003eeefa7a871a730c71a5d8`。接受/终态数组 SHA-256 `da08825437612ebbaba58f84d84d5118bf322b43bc6c9d05820fbfa052c25284`，路径 `work/fullclosed_solver/gauss-spectral-inequality-35f-first/final.npz`。完整报告、缓存与数组只保 scratch。

## 4. 已有选行文字揭示的直接覆盖问题

满步、半步的真正拒绝点都是已经在永久非线性清单中的胞821低φ点

$$
u=.557082202638,\qquad \phi=.01647875344.
$$

仅检索已经完成报告的 selected-row 位置记录可见：该实际拒绝点没有进入192条线性行。胞821共选了28条，其中第三正κ盆附近有大量几乎重合的位置，约 u=.13182、φ=.435912；低φ盆只保了较早的 protected 种子 u=.422249305974、φ=.016682618788。

因此本次问题包含一个明确的 working-set 覆盖缺口：大量同盆近重复行占去名额，而当前低φ峰没有线性化。它始终被真正非线性筛选读取，所以没有悄悄接受已知坏点。不能把所有拒步都归因于负乘子，或称负乘子修正本身已经解决覆盖问题。

后继编程方向是：保留所有永久非线性位置；为每个 protected 盆选其当前最强历史点；对同胞的近重复(u,φ)候选作参数明确的多样性选择；线性不等式仍保真正余量。该新选择尚未进行数值试验，须在 Actions 实际检查。

## 5. 已启动的后验读与较新父比较

在根纠正执行路径之前，本支已经启动了一次后验读，随后自然结束：将并行 a04 的全部1053个 κ/165个半径位置读取到本接受态，并对821低φ/第三盆、230/113峰及881半径作局部细化。由已有输出得到 K=8.070633084378212、Dlb=4.096539509741154，组合 .03 Dlb K=.9918500189633838<.992。

这仍只是实际点下界，不是连续最大或 reach 证书。该后验报告是 `work/fullclosed_solver/inequality-35f-final-a04-and-local.json`；未再启动额外场扫描。

并行 a04 的同目标 Φ=1.139371253e-7、max Gram=.01323315849，均优于本 da088；因此后继主线应继续使用真正通过新位置筛选的 a04 或更好父，不能因为本支使用了完整变量就把 da088叫作最佳。

本次试步新增的两个网格位置是 cell113,u=.16939530676686776,φ=.11351457830353745，以及 cell230,u=.8306046932331322,φ=.6350680461846554；它们已加入本轮永久记忆。后验局部点也应只以位置形式并入后继，不能继承旧数值。

## 6. 已执行的完整源身份

- `fullspace_feasible_active_cg.py`，15699B，SHA-256 `5d08f84eb787efc6a754b1d2f3e6974582b5bcb408e524bedfaaf9d01a0aacac`。
- `fullclosed_point_inequalities.py`，8858B，SHA-256 `5395db01e7c1553c626aafebec8f26cdbe54416b2a16fe58684ad650d823657f`。
- `fullclosed_gauss_inequality_qp.py`，38630B，SHA-256 `5ef7e26834b55d97d2c2dfc2d82f0113b2e072b2f46d3d54f04978177ce0629a`。
- `check_feasible_active_cg.py`，3019B，SHA-256 `fa70b072dc3e6a458e4ababb72b93f412f6f659c6509a60c8fcbb3bd76513a3a`，保存此前一次小凸QP检查的精确可复现输入；本次没有重复运行该检查。
- 沿用 `angular_h2_coordinates.py` SHA-256 `11fd0b8c3bc8139cbce19374cc81ba73b47bddecb007eed3cd296285951c298b`；`physical_height_coordinates.py` SHA-256 `f26738f9ee5a27ec861a9a9cbdc99b301edb6c6b3b271320e567a3892fab5f0e`；`fullclosed_point_cotangent_working.py` SHA-256 `fe8e926c3239d707d6af48efbc48c1755bbac84c3d5722bdbf40f7be7bb53cad`。
- 正谱目标 `positive_spectral_gram_weights.py` SHA-256 `e83742c6f4237eca9d1593199209725d5f898e333f963d88873d5aaf79b0db91`；exact E-Hessian `positive_spectral_gram_hessian.py` SHA-256 `29e2cf8cf7e558168bec6cc90df662638d69da188770c17862a511352a0fb8b4`。

## 7. 字面参数与执行命令

以下保留历史启动命令作为完整来源；后续不得在本地再次执行，应由公开 Actions 替换为其真实新父和真实输出路径。所有 raw 数据在仓库外。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
python math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_gauss_inequality_qp.py \
  --repo math-research-public \
  --bundle work/geometry_path/curvature-qp-spectral-hessian-r22-restore-three.npz \
  --implementation math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/gauss_observed_closed_gram.py \
  --observations work/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz \
  --scale-source math-research-public/topics/visible-flex-larger-amplitude/scripts/integrated_l2_scale_20261120.py \
  --coarse-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_physical_subspace_v3.py \
  --geometry-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp.py \
  --geometry-observed-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120_curvature_qp_v3.py \
  --point-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_cotangent_working.py \
  --height-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/physical_height_coordinates.py \
  --angular-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/angular_h2_coordinates.py --angular-transition 24 \
  --qp-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullspace_feasible_active_cg.py \
  --inequality-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/fullclosed_point_inequalities.py \
  --objective spectral \
  --spectral-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/positive_spectral_gram_weights.py \
  --spectral-hessian-source math-research-public/topics/visible-flex-larger-amplitude/scripts/resume_20261120/positive_spectral_gram_hessian.py \
  --spectral-p 8 --spectral-epsilon .001 --spectral-scale .05 \
  --witness-input math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-fullqp-35f-all-known-locations.json \
  --radius-witness-input math-research-public/topics/visible-flex-larger-amplitude/notes/2026-11-20-fullqp-35f-all-known-locations.json \
  --low-modes 12 \
  --coarse-centers .30,.60,.83,.99,.995,1.0,1.02,1.05,1.077134370991557,1.097,1.20,1.35,1.55,1.75,1.95,2.020292089293148,2.100560831276262,2.15,2.2410311297467116,2.26,2.301232686234047,2.321299871729826 \
  --reach-ratio .03 --reach-safety-factor .992 \
  --active-max-rows 192 --active-block-columns 32768 \
  --outdir work/fullclosed_solver/gauss-spectral-inequality-35f-first \
  --max-directions 1 --maxiter 256 --damping .012063248414946114
```

其余生效默认值为 angles2048、stage_block64、legacy_fraction.5、active_band.025、top_curvature16、top_radius2、QP atol1e-12/rtol1e-6、线性可行容差2e-11、活动行独立性阈值2e-12、梯度刷新32、面内进展输出16、line_trials15、target5e-7。原 operator、basis、coordinate/helper 和 batch 都由记录的 repo 路径读取，完整源哈希在本地 report 头。后继修正版须另给源身份，不能覆盖此次已经执行的源。

完整二次模型与必要小模型来源见[准备记录](2026-11-20-fullspace-inequality-qp-preparation.md)；后续执行遵循[公开Actions纠正记录](2026-11-20-public-actions-execution-correction.md)。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
