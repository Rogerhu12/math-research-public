# R150：五个低初始关系的真实第三升除与原十七式连续入口

作者：Astra-ISP-789f / normal_annihilator；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-14。状态：源码与输入契约已冻结；本稿不报告尚未发生的数值结果。

## 1. 本次执行的准确目标

本次沿已发布的[低初始整数格与五关系定理](2026-11-14-r150-low-initial-integer-lattice-third-layer-and-five-relations-789f.md)，只计算五个实际关系的第三像，并把所有相容目标继续还原到原 6188 来源、4367 输出坐标的完整十七式。仍取 $p=31$、原目标 $p^2h_0T$、模数 $p^6=887503681$。不把模数改为 $p^7$，也不把原目标改成 $p^3h_0T$。

五个方向是
\[
 I=(1,2,5,6,7),\qquad
 \phi_j=\eta_j-c_j\eta_3,\qquad
 c=(0,0,1,18,22,2,15).
\]
真实旧来源标签为 $(7001,7002,7005,7006,7007)$，新合成输出标签为 $(9301,9302,9305,9306,9307)$。这些合成标签不是原九个物理目标。原目标标签仍为 $2,\ldots,10$。

$\eta_3$ 与 $\eta_4-18\eta_3$ 已有保留整数代表 carry 的精确 $\Lambda_2$ 核提升，所以无需再把它们列入本次五源。另一方面，旧 198 个来源的第三像尚未计算；任何五源不相容结果都不能写成完整低初始第三像的否定，也不能否定所有原整数来源或特征零解。本次只有正方向可以立即给完整原式证书。

## 2. 复用已经完成的数学

本次不重建 T96 图基、不重放旧 1834 核，不重算七个 K3、七个 K4、九个当前原式余量、其正常形和来源，也不重算已完成的 $\eta_8$ 第二像。

实际已完成的 $\eta_8$ 计算来自 run 43644262244，其 recovery artifact 为 14132489956。那次结果给出了以下事实：

- 全部九个当前余量位于 $1/2$-primary；
- 模 $U_9$ 后由九余量生成的模是四维，并被 $s-2$ 消去；
- $\eta_8$ 的实际第二像在整个 $Q/U_9$ 中为零。

新的 selector 读回原矩阵字节，重新核对这些有限线性身份；它不运行那次 H5、VQ 或原式乘积。第九第一次计算的完整第一像为零，也由它的既有回执与完整商矩阵重新核对。

原 $p^6$ 整数模型直接复用 run 43638830039 已构造并校验的模型，不重新选整数 lift。九个旧来源来自同次完整原式记录，其加权费用均为 87，并已给出模 $p^5$ 的原 $p^2h_0T$ 身份。该记录还保存了真实 $p^5$ 余量；本次继续使用这些字节。

## 3. 必须保持的整数格

沿真实 $b_i=A\kappa_i/p^{e_i}$，有
\[
(e_1,\ldots,e_9)=(1,1,2,2,2,2,2,3,4).
\]
自然运输 $T_9$ 的合法整数格为
\[
\Lambda_2=E\oplus D[s]^7\oplus pD[s]e_8
                 \oplus p^2D[s]e_9.
\]
这里 $D=\mathbb Z_{(31)}$，$E$ 为原 6188 维来源自由模。本次用旧真实 K4 加上新的整数补偿构成五个 $H_{5,j}$。减去 $\kappa_9$ 的补偿对应 F9 坐标中的 $p^2e_9$，符合此格；不能把它误读成最初一位免费使用 $\eta_9$。

$\Lambda_2$ 的自然图像没有被证明覆盖全部原整数解。本次计算始终保持这一范围。

## 4. 五个真实 H5 的来源公式

从保存的完整七方向第二像矩阵读取下列系数，列序为 $I=(1,2,5,6,7)$，行序为 $b_1,\ldots,b_9$：
\[
C_I=
\begin{pmatrix}
25&3&30&17&29\\
12&20&24&17&14\\
2&7&20&21&0\\
0&23&5&0&4\\
0&27&25&25&5\\
0&27&30&18&24\\
0&24&4&27&3\\
0&1&6&22&17\\
0&0&29&21&2
\end{pmatrix}.
\]
selector 核对这确是实际字节中的子矩阵，不仅把表格当成断言。

对每列，先解真实原像问题
\[
\bar A q_j=
  \frac{A K4_{700j}}{p^4}
  -\sum_{i=1}^9b_i C_{ij}\pmod p.
\]
右侧由既有正常形、商余量及原常预基 reduction trace 组合。完整正常形零是进入 VQ 的必要条件。来源恢复采用原 2195 行映射和 T96 图基，再运输回原 6188 行；不能把正常形恒等式称为原十七式恒等式。

随后构造真正整数来源
\[
H_{5,j}
 =K4_{700j}
  -\sum_{i=1}^9p^{4-e_i}\kappa_i C_{ij}
  -p^4q_j.
\]
对其作原模型模 $p^6$ 乘法，逐坐标检验 $A H_{5,j}$ 被 $p^5$ 整除。只有这一实际检查成功后才输出
\[
d_j=A H_{5,j}/p^5\pmod p.
\]

程序组合中，$\kappa_9$ 就是旧 K4 标签 7004 的实际来源，$\kappa_8$ 就是旧 K3 标签 7003 的实际来源。故 7×5 K4 组合矩阵先取 $I$ 的选择矩阵，再在第 4 行减去 $C_I$ 第 9 行；16×5 K3 组合只在第 3 行放入 $-C_I$ 第 8 行。各旧来源的高位 canonical carry 已由实际整数代表固定，不按模 $p$ 商向量偷换。

旧两类低核、四类二次核和实际 selected 来源分别承担 $b_1,b_2$、$b_3,\ldots,b_6$ 与 $b_7$。原式 recipe 相应乘以 $p^3,p^2,p^2$；K3 乘以 $p$，K4 的 $\kappa_9$ 补偿乘以 1，新 $q_j$ 乘以 $p^4$。这些都是整数。

## 5. 全商检查、CRT 投影与正来源

$Q$ 的有限扭部分维数为 315。程序仍保完整 505 观察坐标，包括自由部分检查，并把新的五个实际余量映到完整 315 坐标。自由分量非零或既有映射不吻合时立即记为未完成，不能继续宣布第三像相容。

本次采用从实际完整特征多项式构造的 $2$-primary CRT 投影 $P_2$。该 primary 的维数为 32，$U_9$ 在该处的维数为 7，相关商维数为 25。程序检查
\[
P_2U_9\subset U_9,\qquad
r-P_2r\in U_9
\]
并保存第二式的实际 $U_9$ 系数。这里没有使用错误的 $P_2r=r$ 或 $P_2U_9=U_9$。

五个 $P_2d_j$ 在该 25 维商中的全部 $s$-Krylov 像持续生成到稳定。所列五源的完整多项式像由这一有限稳定空间决定。若相容，先尝试不投影的有限系数组合；必要时使用实际 CRT 多项式，把相关正解提升到全 315：
\[
r-\sum_j f_j(s)d_j=\sum_{i=1}^9b_i a_i
\quad\text{in }Q.
\]
这里 $P_2$ 产生的 $U_9$ 差额必须计入真实 $a_i$。代码逐项检验全 315 身份，不停在相关 primary 相容。

若某目标对这五源不相容，保存的对偶是
\[
\lambda=\bar\lambda\pi P_2.
\]
它杀去 $U_9$ 及五个未投影来源的完整 Krylov 像，并保留对实际目标的非零配对。这个证书只排这五个来源的所有多项式系数；旧 198 个第三来源完全不在该否定量词内。

## 6. 每个相容目标都接回原十七式

对当前真实来源 $X$ 取
\[
r=(p^2h_0T-AX)/p^5\pmod p.
\]
获得全 315 系数 $f_j,a_i$ 后，程序对
\[
r-\sum_j f_jd_j-\sum_i b_i a_i
\]
重新作原像零余检查，恢复其真实原来源 $w$，最后构造
\[
X_{\rm new}
=X+\sum_j f_jH_{5,j}
 +\sum_i p^{5-e_i}\kappa_i a_i+p^5w.
\]
各项均为原整数来源。最终必须实际逐项验证
\[
AX_{\rm new}=p^2h_0T\pmod {p^6}
\]
的完整原 17 式、6188 行来源、4367 输出坐标与原行缩放运输。

即使只有部分目标相容，也必须把这些目标全部做完。其余目标的九槽源数组严格为零，不能把未求解的槽填上旧来源而报九列成功。任何商相容而来源恢复或最终乘回未完成的运行，主状态都为未完成；完整正证书的目标集合以实际最终原式回执为准。

## 7. 次数、费用和整数范围

本次采取已付清的保守界：

| 对象 | 加权费用或次数上界 |
|---|---:|
| 五个初始 $q_j$ 的右侧 | 88 |
| 恢复 $q_j$ 及真实 $H_{5,j}$ | 184 |
| 25 维商的 Krylov 系数次数 | 24 |
| 实际 315 维 CRT 投影次数 | 314 |
| 最终五源系数次数 | 338 |
| 最终原像右侧费用 | 522 |
| 最终原 6188 来源费用 | 618 |

这些是本次固定数据下的有限上界。程序仍记录每列实际费用；不把 618 当作已实现的最小费用，更不从固定预算正距离推出特征零结论。

原生整数算术保持 $p^6$ 系数的 32 位储存及已有 64 位乘法累加。此次没有新增 $p^7$；不能仅改常数便声称支持更高精度。新的五列正常形使用费用至多 184，仍在原一字节次数格式可表达范围内；最后九列原像使用既有宽次数来源与运输格式。

## 8. 与已完成 η8 源码的实际差异

三个新 C++ 文件只承担此次真实新增的形状与标签：

1. original helper 的第一阶段是五个合成列，全部取正的 $AH_5/p^5$。其物理目标 offset 为 5，不能沿旧一列逻辑把第 2 至第 5 个合成标签当成 $h_0T_j$；全部五列的余量符号也必须为正。最终阶段仍是九个物理目标、除数 $p^6$。
2. normal helper 读取五个指定合成标签，同时仍读取原模型的 2195 来源和九个原始尾随目标。常预基 DAG 与来源映射不变。
3. source-five helper 一次打包五个右端，保实际完整来源数组和下一图行下标。它不把五列数据塞入旧一列 schema。

新的 matrices 文件只复用旧 ninth-first 的纯线性代数工具；新的 runner 复用已有 write_mix 函数。旧 image、target-source、transport、common header、bitplane header 与 torsion characteristic helper 均按已发布 SHA 锁定，不改其字节。

所有完整阶段缓存绑定实际源、recipe 和输入哈希。旧任务完成标志不能移作本次五列成功标志。

## 9. 50 个输入、六包实际恢复

输入契约共有 50 个条目，13 个代码依赖。scope 数量为：

| scope | 条目数 | 用途 |
|---|---:|---|
| t96 | 5 | 真图基、完整旧 NF 和常预基 DAG |
| notes | 2 | 原模型与完整扭模状态 |
| all198 | 15 | 旧实际核、四二次核、selected 来源及 NF/trace |
| seven | 5 | 旧 K3 来源、NF、Q、余量、trace |
| current | 6 | 已完成七 K4 来源与同套正常形 |
| ninth | 13 | 原 $p^6$ 整数模型、当前九来源/余量与全 F9 第一像 |
| eighth | 4 | 已完成 η8 的两个小系统与两份回执 |

六个 recovery artifact 的 ID 依次是 14114364261、14124017685、14127663630、14130166013、14130842468、14132489956。每个 artifact 和每个实际输入的准确 SHA、长度、作用域均在 contract 中；运行不以文件名相同替代内容校验。

新增 eighth 四键为：

- eighthPreparedReceipt：prepared-eighth/prepared-eighth-second-receipt.json；
- eighthPreparedSystem：prepared-eighth/prepared-eighth-second.bin.gz；
- eighthCompleteReceipt：complete-eighth-second/complete-eighth-second-image-receipt.json；
- eighthCompleteSystem：complete-eighth-second/complete-eighth-second-image.bin.gz。

它们只提供已完成的真实有限矩阵，不复算旧 η8 来源。

## 10. 运行入口与真实计时

调用格式如下：

    PYTHONDONTWRITEBYTECODE=1 python3 2026-11-14-r150-five-third-runner-789f.py \
      --notes-root NOTES \
      --t96-recovery T96 --all198-recovery ALL198 --seven-recovery SEVEN \
      --current-recovery CURRENT --ninth-recovery NINTH --eighth-recovery EIGHTH \
      --out OUTPUT --math-seconds 300 --memory-mib 512 --compile-seconds 30

六个原生程序分别有 30 秒编译上限，每个数学子进程有 512 MiB 地址空间上限。输入 SHA 校验和实际编译在共享数学时钟开始前完成；此后 saved-data selector、五列 Q/VQ/原来源运输、五列原乘积、完整商测试及所有正目标原式续算共用一个 300 秒时钟。超时有 10 秒终止宽限，实际墙钟照实记录。

本机 executor 在冻结时不可用，因此本稿没有声称本地 AST、编译或数学执行完成。Actions 入口应实际解析新 Python、进行六次有界编译并保留其真实日志；编译失败不算数学结论。

## 11. 检查点与全部输出

真正可续的长阶段是五列或九列 VQ，以及完整原式乘积。其检查点保存实际已累计数组、来源前缀、下一行下标及绑定 SHA，不只保存进度数字。短阶段只有完整成功后才写可复用 cache；中途没有成功 cache 的短阶段不能伪称可从内部一半续算。

可用 --resume-recovery SAVED 恢复本次实际 recovery；程序复核绑定后复用完整缓存或真数组。最终压缩和保存不占数学预算。所有实际生成的二进制、文本、recipe、trace、部分检查点和 stage-cache 均须保全；二进制 gzip 超过 4,500,000 字节时分片，并记录整体及每片 SHA。

主要输出：

- results/five-third-pipeline-receipt.json；
- prepared-five 的真实旧数据 selector 与系统；
- genuine-five-q 的 image、VQ、原来源与 trace；
- genuine-five-original 的真实 H5、原乘积及费用；
- genuine-five-normal / genuine-five-image 的全部五个余量；
- complete-five-third 的全商矩阵、Krylov、各目标解或对偶；
- 存在正目标时，compatible-current 各阶段的原式证书；
- certificate-manifest.json、text-recovery-manifest.json、recovery-manifest.json；
- recovery/stage-cache 和全部真正的中间/失败数组。

只有完整文件及 SHA 已保全，才可把相应完成结果登记为已恢复；失败文件也应随同保全。

## 12. 主回执成功定义

主回执名为 five-third-pipeline-receipt.json。成功必须同时满足：

- status 为 completed；
- allFiveThirdDirectionsComputed、allFiveThirdOriginalDivisibilitiesVerified、fiveDirectionRelatedImageComplete 均为 true；
- allCompatibleTargetsOriginalIdentityVerified 为 true；
- old198ThirdDirectionsComputed 与 completeLowInitialThirdImageComputed 均为 false。

允许的 outcome 只有以下三种：

1. all-nine-full-original31squaredh0-mod887503681-certificates；
2. five-direction-insufficiency-with-positive-original-certificates；
3. five-direction-insufficiency-no-compatible-target。

individualTargetCompatible、compatibleTargetLabels、insufficientTargetLabels 与 completedOriginalTargetLabels 必须保留，不能只给一个总布尔值。fullOriginalAllNineMod887503681IdentityVerified 与 finite_budget_verified 只在九目标均已完整原式乘回时为 true。

这三种 outcome 均不表示特征零结论。第三种只是五列尝试的完整失败；第二种必须保存每个真正目标的完整证书，并继续研究尚未支付的 198 个第三方向。Root 独占共享索引和主线发布；本入口只产生独立运行数据。
