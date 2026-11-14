# R150：七个增广第二方向的连续数值接口

作者：normal_annihilator / 789f。2026-11-14 UTC。

**冻结状态：仅源码与接口。** 本次没有执行新数学、Python AST 或本机编译。原执行环境仍不可用；真正的 AST、六个有界编译和数学结果由新的本库 Actions 回执给出。不得把本文件的公式或预期分支写作已经完成的数值身份。

本接口落实[完整相关第二像的七方向归约](2026-11-14-r150-seven-augmented-second-kernel-and-primary-completeness-789f.md)，并使用实际 pair run43632271378 的完整 $J_8$、$c_i$、九个原余最小 ann，以及 $j=6,9$ 的原式成功。它不重算旧1834核、七关系第一像、198个旧第二方向或已经完成的两列 VQ。

## 1. 不变的真实输入与新目标

仍使用原17个整数方程、6188原来源、4367输出坐标，以及已证3333常预基和2195原来源的全图。35个输入逐一按 contract 的 SHA256 验证：

| 恢复范围 | 文件数 | 实际来源 |
| --- | ---: | --- |
| T96 | 5 | run43597823809 / artifact14114364261 |
| 旧198 | 15 | run43619888599 / artifact14124017685 |
| 原七关系 | 8 | run43630666145 / artifact14127663630 |
| 两正列及完整八维后处理 | 4 | run43632271378 / artifact14128781519 |
| 仓库固定原模型、精确整数JSON、完整torsion状态 | 3 | contract中的原路径及SHA |

原精确整数JSON只做模 $p^5=28629151$ 的转换，$p=31$；4433个原方程系数及18个行单位数据降至模 $p^4$ 时必须逐项等于实际旧模型。目标改为

$$
p^2h_0t_j,\qquad AX_j\equiv p^2h_0t_j\pmod {p^5}.
$$

所以新目标除以 $p$ 后的26个模系数必须严格等于旧 $ph_0$ 模 $p^4$ 目标。旧 $ph_0$ 的来源不能误称新目标。原 $h_0$ 的真实整数多项式仍从已经保存的完整整数JSON及固定 $s^3(s-2)F_+^2F_-^2E_8$ 双向核对。

两列 $j=6,9$ 已有原式模 $p^4$ 证书，直接把其保存的标准原来源乘 $p$，再对原17式核新目标模 $p^5$。无需重新求这两列的正常形或 VQ。

## 2. 只新增七个真实第二方向

实际

$$
c=(0,0,1,18,22,2,15),
$$

故 $L$ 的第3列为 $(s-2)e_3$，其它第 $i$ 列为 $e_i-c_i e_3$。使用旧实际原16来源束的前七列 $K_{3,i}$，先算 $K'_i=(K_3L)_i$。

旧全315矩阵中，对同一 $L$ 求 $d_i=AK'_i/p^3\bmod p$。其类必须完整落在旧七维 $U$ 中；通过实际七基解唯一常数 $C_i$，不只比较主部分。由旧 NF/Q/rem/trace 直接构造

$$
\bar A q_i=d_i-\sum_{\nu=1}^7\bar b_\nu(C_i)_\nu.
$$

新七列的完整余必须为零，随后用已成 T96 图恢复真2195来源，再按同一个3333 DAG运输至全部6188原行。该步骤的右源费用是88，原来源费用至多184，实际费用另由乘回读取。

固定 $e=(1,1,2,2,2,2,2)$，构造

$$
K_{4,i}=K'_i-p^3q_i-\sum_{\nu=1}^7p^{3-e_\nu}\kappa_\nu(C_i)_\nu.
$$

使用原 $A$ 模 $p^5$ 全部乘回，逐系数核 $p^4$ 整除，再保存真正的

$$
D_i=\frac{AK_{4,i}}{p^4}\bmod p.
$$

这里每个原整数代表与旧保存来源一致。旧 $K_3$ 标准代表的模 $p^4$ 进位，在第二像中只增加原像；没有把某个模 $p$ 的除数结果随意提升成高精度原源。

仅对这七个新的4367坐标余量作正常形。生成的 forward/backward DAG 必须与旧两个完整哈希相同。完整 G 余保留全部505自由观察，并核820到315的完整重建；任一自由观察不消失都使本次入口失败，不准投影隐藏。

## 3. 相关第二像的完整性与真实投影费用

实际旧 raw 九列的全315最小 ann 均为

$$
(s-1)(s-2)^2.
$$

它们确实全在 $1/2$ 主部分。旧1632真提升核、四个精确增广 syzygy 以及198个旧方向的相关第二像已在前述定理中逐类支付。因此，在 $Q/U_8$ 的 $1/2$ 主部分，完整第二像只须这七个新 $D_i$。

入口使用完整315作用 $J$ 的真实特征多项式

$$
\chi_J=f_{1,2}g,\qquad (f_{1,2},g)=1,
$$

其中 $f_{1,2}$ 含1、2两点的全部特征多项式重数，次数须为已成的39。取真正 CRT 多项式

$$
P=g(g^{-1}\bmod f_{1,2}),\qquad \deg P\le314.
$$

代码逐项核模多项式投影身份，且核 $P(J)U_8=U_8$、$P(J)r=r$、$P(J)^2D=P(J)D$。由 Cayley–Hamilton，这给完整有限模上的谱投影。没有把对标量参数的抽样替代该身份。

在真实八维商中，对 $P(J)D$ 作完整 Krylov。相关商维数为 $39-8=31$；所选生成系数次数至多30。完整不变性 $JB=BH$ 必须成立，不以某个有限阶段秩未变的猜测代替。每个负目标保存完整315上的

$$
\lambda=\bar\lambda\,\pi\,P(J),
$$

并核它杀 $U_8$、杀全部相关 Krylov、与相应原余配对为1。这个负结论覆盖 $A^+$ 的所有模 $p$ 初始来源，排除相应 $h_0t_j$ 在 $A^+$ 中的模 $p^3$ 解；它不排除没有纳入该增广族的原有理来源，也不宣称其它 primary 的旧198第二像已经算全。

正方向先试同一已生成 Krylov 次数下未投影的七个真实 $D_i$。该试算仅用来降低正解费用，不宣称它已经给完整未投影像。若成功，则直接采用；否则采用 $P(s)$ 乘相关正解。每个正目标都必须在完整315中得到

$$
[r_j]=\sum_i f_{ij}(s)[D_i]+\sum_{\nu=1}^7 C_{\nu j}[b_\nu]+g_j[b_8].
$$

八个校正系数是实际 $U_8$ 基中的常数，八基都各自有已保存的真实原来源。实际解的次数记录在回执中，最坏至多 $314+30=344$。新右源费用至多 $184+344=528$，图给原来源费用至多624；不得在移动投影后仍引用费用88。

## 4. 每一个正目标都继续到原17式

七个剩余实际标签固定为

$$
(2,3,4,5,7,8,10).
$$

矩阵结果逐目标决定相容性。若只有部分相容，七槽中的其它槽强制全部来源为零，并在原目标掩码中排除；它们不会被写成已经完成。相容列继续真实 image/VQ/预基运输，恢复

$$
\bar A w_j=r_j-\sum_i f_{ij}D_i-\sum_{\nu=1}^7 C_{\nu j}b_\nu-g_jb_8.
$$

由旧实际 $AZ_j\equiv ph_0t_j\bmod p^3$ 及 $b_8=AK_{3,3}/p^3$，新来源取

$$
X_j=pZ_j+\sum_i f_{ij}K_{4,i}
+\sum_{\nu=1}^7p^{4-e_\nu}\kappa_\nu C_{\nu j}
+pK_{3,3}g_j+p^4w_j.
$$

它必须最终经原17/6188/4367全乘回验证 $AX_j=p^2h_0t_j\bmod p^5$，核每个原行单位、每个系数和实际加权费用。新原来源采用 uint32 系数流 R150P531，原式来源 R150O531；旧 R150P431 和 R150PS31 输入按真实模数及宽度区别读取。两正列复用流另外保存，不能把其标签混进固定七槽。

九个目标若全部完成，则本次给原 $h_0$ 模 $p^3$ 的原来源证书，分母指数至多二。它不证明两层分母必要，仍不是特征零等式。

## 5. 精确执行命令与时间规则

六个 native 编译各自有30秒、512 MiB上限。固定输入哈希和编译完成后，所有新数学共用一个300秒真实时钟，包括整数模型转换、准备矩阵、两正列乘法、新七列的全部运算、相关像和每个正目标的来源及原式乘回。

入口：

~~~sh
python3 topics/invariant-subspace-problem/notes/2026-11-14-r150-augmented-seven-second-runner-789f.py \
  --notes-root topics/invariant-subspace-problem/notes \
  --t96-recovery T96_RECOVERY \
  --all198-recovery ALL198_RECOVERY \
  --seven-recovery SEVEN_RECOVERY \
  --pair-recovery PAIR_RECOVERY \
  --out OUTPUT \
  --math-seconds 300 --memory-mib 512 --compile-seconds 30
~~~

真实恢复使用相同命令另加 --resume-recovery PREVIOUS_RECOVERY。VQ 的累计数组、下一图行，以及原式乘回的完整 product 数组、两原来源前缀、下一原行都绑定全部输入哈希保存。已完成阶段的 cache 含原源码及真实输入绑定和全部输出哈希，直接复用；不把退出0当完成。

正常形、image、transport 和小矩阵阶段只缓存已经完整完成的阶段。它们若中途退出，保留实际文件及失败位置，但没有虚构不存在的可续数组；只未完成部分可能重新执行。外层 timeout 给 SIGTERM 后最多10秒保存 checkpoint，随后才强制终止。压缩、分片和上传在数学时钟之后，不能把保存时间当新的数学计算。

## 6. 输出、成功字段与边界

主回执为 results/augmented-seven-second-pipeline-receipt.json。完整执行有三种 outcome：

| outcome | 准确含义 |
| --- | --- |
| all-nine-full-original31squaredh0-mod28629151-certificates | 两复用列和七新正列均完成原17式 |
| complete-related-second-obstruction-with-all-positive-original-certificates | 一部分剩余目标有完整相关初值障碍；所有相容目标均完成原17式 |
| complete-related-second-obstruction-with-reused-pair-certificates | 七个剩余目标均有完整相关初值障碍；两复用正列完成新目标原式 |

三者都必须同时具备：

- status == completed；
- allSevenNewDirectionsComputed == true；
- relevantPrimaryImageComplete == true；
- allCompletedCompatibleTargetsOriginalIdentityVerified == true。

只有第一种允许 fullOriginalAllNineMod28629151IdentityVerified == true。obstructedTargetLabels 与 completedOriginalTargetLabels 必须按实际列分别读取。Actions success、退出0、相关像相容均不替代这些字段。finite_budget_verified 只有九列全成才为true；各已成正列的真实有限费用另以 finitePositiveSourceBudgetsVerified 标明。

recovery/ 保全全部新真实来源、余量、正常形、trace、矩阵、原17式来源、stage-cache及实际checkpoint；results/ 包含数学日志、所有小回执、原恢复清单、文本恢复清单和完整证书分片。二进制统一 gzip，无损分片不超过4,500,000字节，保存整体与每片 SHA，不以只有临时路径或只有大文件哈希替代证书。超时/失败仍保全部真实已成内容，后继从具体未完成位置继续。

原6188来源与17式永不被补成其它矩阵方程。全流程不访问或修改 main、HANDOFF、open、results索引或log；这些由根代理处理。此冻结提交也不触发 Actions。
