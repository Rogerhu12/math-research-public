# R811 执行契约：低度原乘法、两图极理想及规范不变的函数入口

日期：2026-11-15。状态：**契约与可认证算法已具备；尚无 R811 实际算术输出。**
证明见 `results/R811-original-normal-polar-ideal-preimages-and-two-chart-certificates.md`。
本契约不填尚未成功的 R809 A/B producer、原极理想或五函数 DAG。

## 1. 分清首个实际任务与后继

首任务是原 $A/\tau^5,B/\tau^5$ 的两份准确乘法矩阵，
随后同一原函数 $A/B$ 的两个极理想前像。
R807 已实际 success，不把其清极自动算作 R811 结果；
R809 六个 C 组可以先独立完成，原 A/B 组须等待 R787 真正完成。

本 core 不做已成 R803/R807/R809 的有理短坐标求解。
只需要 R806 的原 $M_w$、cyclic 证书、正常基次序，
以及目标实际 normal-vector stage。R809 的112个有理右端不是112个新乘法算子：
每个 A/B 是一个 $L$ 函数、最多14个有理系数分量。
没有需求时不生成六个 C 的全乘法矩阵。

建议结果身份 `R811-original-regular-multipliers-and-polar-preimages`，
核心 CLI：
`--config --proof --method --retained --output --budget-minutes`。
请求须明示 `requested_stage`：
`base_regular_multipliers` 或 `base_polar_preimages`。
两者各自有真实完成字段，不用前一阶段冒充后一阶段。

## 2. 必需实际输入与不变字段

| 输入 | 必需消费内容 | 本阶段不重算 |
|---|---|---|
| R806 | 原272整基、$M_w$、成功候选与实际cyclic minor、各分组准确坐标 | 原S690短块、筛选、Dixon或Krylov秩 |
| R809 | 实际 A/B normal 向量、原S5标识、字段/尺度/目标生成证书 | 112个短右端及原Fourier行 |
| R787 | 由R809继承的原A/B来源和实际函数关系证书 | Laurent、Schur、原关系 |
| 原L定义 | 真实b的七次多项式、$s=1+2\zeta$和已冻结字段adapter | 原CM模型/period/Hom |
| 直接前一R811 | 已成目标分量、有限域272逆、当前CRT、完整极理想工作状态 | 任何已登记完成项 |

全局基标签固定 core/proof/method SHA、原 R806 producer、正常基、$z$、$\epsilon$、
矩阵输入/输出方向和原L字段描述。
每个目标标签另绑定其实际 R809 stage/file/bytes/SHA、原目标名、齐次度和来源链。
未提供的 A/B stage 不以占位 SHA 进入一次实际计算。

R809 统一字段为
`b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b`。
A/B 的 r=5。六个 C 若将来实际消费，必须读取 r=4 的最高项全零证书；
不能只由目标名字推断次数。

前缀数据已在旧 producer 完成，此 core 不需要再携带全部 R786 q 行。
正常基的原次数、行序和原完整生成证书必须保留，
不能只抄一个272维数字和一个辅助矩阵。

## 3. 有限域插值、CRT与准确终验

按目标、字段分量逐一处理。准确输入为零的分量直接保存零向量的来源证书；
不因一次模零判为特征零零。

每个新素数：

1. 核所有本轮原有理输入分母是单位；
2. 用原 $M_w$ 的准确约化，在整数点 $t=0,1,\ldots$ 找 r+3 个
   互异好剩余类；每个实际 $\mathcal K(t)$ 逆完整乘回；
3. 对当前目标分量形成 $\mathcal K_f(t)$，算
   $\mathcal K_f(t)\mathcal K(t)^{-1}$；
4. 插值次数至 r+2 的每项，再核更细的
   $r+\epsilon_a-\epsilon_b$ 支撑；超界项须真模零；
5. 将全部准确模系数合入当前 CRT，不保存每一历史大CRT向量。

不同目标/字段分量共用相同素数/点的原 $M_w(t)$ 与逆 stage。
这些 stage 一旦完成即读回，不重做相同小块。
不为这一步找 $L$ 的完全分裂素数，不在合数模环上重新求矩阵逆。
对一个坏素数只登记实际障碍；不改变原目标或相位。

采用固定对称重构界 $B=\lfloor\sqrt{(M-1)/2}\rfloor$，
保证 $2B^2<M$。一个完整分量接受前必须准确核：

- 所有 weighted degree bound；
- 原第一列完整相等；
- 所有系数上的 $NM_w-M_wN=0$。

这些是原 $L(z)$ 算子身份的充分证书，不能换成若干“随机特化通过”。
实施采用 R809 定理809.1已经证明的确定性准确点认证：
先逐项验证原 $M_w$ 的界 $1+\epsilon_a-\epsilon_b$ 与候选的
$r+\epsilon_a-\epsilon_b$，从而交换子的每项次数至多
$r+1+\epsilon_a-\epsilon_b\le r+3$。
然后在互异整数 $0,1,\ldots,r+3$ 的全部 $r+4$ 个点，
逐字段分量、逐行块准确验证完整交换子矩阵为零。
首 A/B 的 r=5，故每项次数至多8，必须使用全部9点 $0,\ldots,8$；
这由多项式注入性证明**全部系数**为零。
这些点只用于准确矩阵乘法，不要求它们是 Krylov 好点。
原第一列仍逐多项式系数检查，不改成点验。
证书保存逐项 weighted bound、`commutator_maximum_degree`、
全部 `exact_commutator_points`、每点每个行块的准确零证书及其矩阵源SHA。
由于全部输入按14个有理分量编码，清除已记录的公共正分母后
只需准确整数矩阵乘法。软件不生成特征零 $272\times272$ Krylov 逆。

保存每个完整分量的共同正分母/整数多项式系数，或逐列共同分母，
并明确读取规则；不能把分母统一改成1。
矩阵分行块落盘，完整矩阵 index 按每块 SHA 固定行区间。
CRT只保当前完整残余、模数、已消费素数列表及前项 SHA；
成功分量落盘后删其旧 current，大向量历史只留小哈希记录。

实际矩阵系数高度和所需素数数量未知，不能保证一次300分钟完成。
目标/字段分量/行块与CRT的原子状态须允许准确续算。

## 4. 两图 regular 矩阵的生成和认证

对首两目标使用 r=5：
$$
M'_f(t)=t^5D(t)M_f(1/t)D(t)^{-1},\quad
D(t)=\operatorname{diag}(t^{-\epsilon_a}).
$$
逐项指数是 $5+\epsilon_a-\epsilon_b-k$；
其非负性须由已验 weighted bound 检查。
两矩阵共同的 $t^5$ 对原比值取消。
同时保存相同函数过渡（没有 $t^5$）与同截面平凡化的不同字段，
不能只写一个含糊的 `transported` 标志。

若以后处理 r4 的 $\theta U_j/\tau^4$，使用 r4，
不能因 R809 用 S5 求过坐标就误乘 $t^5$。
任何选择了 r5 表达的额外共同 $t$ 需在源数据中显式记录。

## 5. Polynomial-pair 前像阶段

输入每图的准确两矩阵 $M_p,M_q$。
初始矩阵为 `[M_p | -M_q]`；$q\ne0$ 由实际原函数/正常域输入保证。
以证明(811.14)的多项式 Euclidean 列操作做完整核。

实现必须提供：

- 原L系数的准确零、加减乘、逆；
- 原L[z]系数表、准确除法余式和xgcd；
- swap、非零常数缩放、shear、Bezout二列操作；
- 每步可逆性和完整列操作乘回；
- 当前矩阵的原子断点及完整可重放 transcript。

不假定 python-flint 0.9.0 有 `fmpq_poly_mat.hnf` 这个接口。
其已核官方文档提供数值域矩阵和 `fmpq_poly` 的准确多项式操作；
对原L[z]需消费冻结字段adapter并实现明确的多项式层，
不能调用名称相似但底环不同的整数 HNF。
所有新算术只在公开 Actions 中执行。

若 $P E_1\cdots E_m=[\Gamma,0]$，
先保存这一完整等式与每个 $E_i$ 可逆的 transcript。
从 $(0,I)^t$ 逆时间左乘 $E_i$ 本身，取得核基 $(J,W)^t$；
核 `M_p*J == M_q*W`，再将 J 作列 Hermite 化。
只保存若干满足该式的列不够，必须有完整 unimodular 核证书。

一份完整二维前像输出至少包括：
原两矩阵 SHA、图变量/正常基、原函数pair标签、
full-row-rank原因、transcript分块、
最终Gamma、投影J/W、J的三角化操作及正规整理想基。
首一化常数只属于理想基变换，原函数 DAG pair保持原值。

## 6. 两图终验与可供后继消费的极除子

逐图计算三角对角的次数和 $t=0$ 阶数，
准确输出
`degree_on_tau_chart`、
`degree_on_missing_boundary_from_sigma_chart`、
`global_degree`。
不把两图全维数相加，不预填1206。

按 `D(t)*H_tau(1/t)` 的函数过渡，
核两图在 `L[t,t^-1]` 上互相包含。
清约后的每个包含系数分母只能是非零常数乘 $t$ 的幂；
两边准确乘回。这个步骤不需要再拆剩余域。

只有矩阵身份、完整前像、两图相容性和实际全局度全部通过后，
才置 `original_base_map_polar_divisor_computed=true`。
这仍不表示 $\mathcal B+3D_f$ 的三重数提取、
V3两次flip、原$\eta$、刚性化或高度已算出。

## 7. 原五函数 DAG 与导数的真实后续依赖

本任务可保存原R804的八节点整数Hom DAG和每个原标量，
但未有实际 $\partial_z$、$\chi$ 或源绑定 Wronskian 时，
不激活初始 $R_j$ 和全局五函数阶段。
原R804 CM点消费者是另一种数据，不能替代全球函数。

已有全局 $Y_g$ 后，或给同一个原pair，或给经过原域准确认证的算子pair；
(811.10)都可直接取极理想。任何取消只在理想层实施，
原 norm/三同源函数继续带整个分子分母、$b$、$\rho$、原单位与刚性化来源。

所有结果明确区分：
`regular_multipliers_computed`、
`base_polar_preimages_computed`、
`five_original_function_DAG_computed`、
`eta_or_height_computed`。
本契约不预填任何一项的成功。

## 8. 保存边界

每次新增数学阶段完成即保留直接后继需要的数据与SHA。
原大矩阵/极理想/证书只放一日活跃artifact及必要续算bundle，
Git与Release仅存脚本、参数、证明、run及SHA。
静态review或一个模成功不能被登记为准确极除子结果。

软件能力核对来源（2026-11-15，仅文档阅读，无本地数学运行）：

- https://python-flint.readthedocs.io/en/stable/
- https://python-flint.readthedocs.io/en/latest/fmpq_poly.html
- https://python-flint.readthedocs.io/en/latest/fmpq_mat.html
