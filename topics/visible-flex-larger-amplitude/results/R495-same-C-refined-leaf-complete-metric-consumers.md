# R495 — 同一准确 C 新叶包围进入完整闭域度量与实际精化误差消费者

**可信度：已证明（限下述条件命题）。** 本文给出 R489/R492 的真实新叶求值对象进入既有完整闭域消费者的来源与包含性证明，以及与之逐项对应的独立源码视图。没有实际接受父、R489 重算结果、全域误差数值或新 run；没有在本地执行科学、导入项目、AST、编译或 fixture。所有实际区间算术仍只允许本库公开 Actions。

本文不重新证明 R418 的四个 Loewner 判据、R459 的二维相对算子范数、R483 的完整 coast Bernstein 包围或 R443/R447 的共同材料相位共轭。新结论是这些已付公式对**同一准确函数的新包围求值状态**的可执行组合。原 checkpoint、准确 definition、参数、节点、材料映射、B 与接受条件均不修改。

## 495.1 条件与真实来源

设一次实际公开 job 中已经存在完整、真实、通过其原加载条件的冻结场。它必须来自下列明确登记的一个家族；登记家族名不替代加载器对完整父、原配置、全部数组、末端记录和 source closure 的实际检查。

| 家族 | 实际准确 cut 加载器 | 原 target 实现 |
|---|---|---|
| original112 | R416，`geometry_20261115_current_C_accurate_cut_patch.py`，28417b93 | R400，`geometry_20261115_continuous_ten_frozen450_prefix_metric.py`，011ca7db |
| resolution112 | R441，`geometry_20261116_current_C_resolution_accurate_cut_patch.py`，8811f89c | 同一 R400 target |
| completeM | R451，`geometry_20261116_current_C_M_accurate_cut_patch.py`，747b9d1f | `geometry_20261116_continuous_ten_M_prefix_metric.py`，56a3a9fe |
| incrementalM | R464 实际生成视图，`geometry_20261116_current_C_incremental_M_accurate_cut_patch.py`，8105c814 | R464 实际生成的 `geometry_20261116_continuous_ten_incremental_M_prefix_metric.py`，fd74b6ad |

另须有同 job 的真实 R489 result、原/新完整 C 与 cut 文件、实际完整输入绑定，以及 R492 所要求的原 clock/launcher/源身份。R495 调用 R492 `RefinedLeafProvider` 重新读取这些原件；不只信 result 中的一组布尔值。它保留 R489 当前实际支持的 `actual202205` 来源合同，不能因为上表出现四个场家族，就把尚未登记的历史 launcher 伪装成 R489 已支持的来源。

本证明的条件是：这些实际绑定确实成立，原/新包围均覆盖同一个原定义许可的准确 C 根族，原准确场与目标的定义满足各自原加载条件，并且所要求的正分母/宽度条件由相应实际区间求值支付。缺少任一实际输入时，消费者保持错误或 partial；它不生成接受父，也不把这项后置测量变成 BVP 前门。

主要已付来源是 [R489](R489-same-C-complete-head-recomputation-and-cut-enclosure-intersection.md)、[R492](R492-same-C-leaf-refinement-for-the-fixed-target-and-accurate-cut-field.md)、[R418](R418-current-C-complete-closed-relative-metric-source-interface.md)、[R459](R459-fixed-closed-target-relative-error-and-refinement-evidence.md)、[R483](R483-complete-coast-Bernstein-ranges-in-current-metric-consumers.md)、R416、R443/R447/R457/R464。正式文件名及完整 SHA 以本次接口和 `r495-same-C-refined-metric-source-plan.json` 的字面清单为准；本段短 SHA 只供定位。

## 495.2 相交保全原根族，不产生新的 C 选择

以 $\mathcal C$ 表示原 f12f 数学定义许可的完整准确 C 族，$R$ 为原物理 cut。对 $C\in\mathcal C$，令

$$
 e(C)=(E_C(R),E'_C(R),E''_C(R)).
$$

原与新计算分别给出三个闭区间 $I_i,J_i$，且条件是

$$
 \forall C\in\mathcal C,\quad e_i(C)\in I_i\quad\text{且}\quad e_i(C)\in J_i.
$$

因此 $K_i=I_i\cap J_i$ 仍包含每个许可 C 的该分量。R492 用准确有理端点重算这三个交集，并逐项核对 R489 的实际交集原件；其输入绑定还要求同原参数、原物理 cut、同准确根族和仅允许的工作参数改变。它没有把 $\mathcal C$ 改成某个盒中心对应的对象，也没有把新 result 的来源身份写回旧 definition。

上述结论不说 $\prod_i K_i$ 的每个点都来自某个共同 C。区间传播可以保留额外不相关组合，这只能扩大包含。空交集不许可删除一个不方便的根、偷偷选另一个分支或填中点；实际消费者报错，不能凭该错误声明原几何无解。

## 495.3 四家族的真实对象桥

`geometry_20261116_same_C_refined_metric_family_bridge.py::bind_loaded` 的输入是**已经通过原加载器的对象**。它从 `type(obj).__module__` 取得该对象实际的模块，再核确切文件、完整 SHA 与实际类对象相等；不会取 `sys.modules` 中某个同路径旧实例来替代。这保留 R417 已明确的多模块类身份边界。

对 target，桥调用 R492 `RefinedTenTarget`：

- 原 `definition`、tree 节点、piece/support、roots、十个准确参数和所有控制项保留；
- 独立复制求值树，并仅把 `E0/E1/E2` 求值叶换成 $K_i$；
- 重新求值准确长度与完整表达式；数值前缀长度仍是原数值字词代表的准确有理数；
- 旧 definition 的 bytes/SHA 不变，新叶原件、R489 result 与求值身份另记；
- 原消费者需要的 `all10_frozen_exact_dyadics` 是从原绑定逐项复制，并与同十个准确有理参数核同；不由新盒生成参数。

对 cut，桥调用**该家族原 `AccurateCutModel` 与 `new_exact_field`**，并实际要求新旧 appended DAG 节点、root 索引、cut、数值长度全同。它还要求 field 的完整 pieces、节点坐标、radii、core、density、registration、原正密度下界与 M 全同。新的包围对象具有独立 R495 schema/source/loader；原 450 或 frozen-M checkpoint 字段的完整 descriptor 保留，不重标成新的接受证明。

对每个同一个 $C\in\mathcal C$，原与新求值都是同一个函数 DAG 在同一个准确 $e(C)$ 上的值。因此它们定义同一准确 target 和同一准确 cut field。区间端点变了，数学函数没有变。源码中的字节与对象关系检查是这个既有输入合同的实现，不是要求另一个数值实验通过的科学门。

## 495.4 完整前缀与 coast 的包含

令 $L_C$ 为同一准确 DAG 的总长，$L_n>0$ 为原数值长度字词，$s_n\in[0,L_n]$，$u=s_n/L_n$。在原共同物理角 $\Theta=\Phi(2\pi q)$ 下，准确前缀目标仍为

$$
 g_{s_ns_n}=(L_C/L_n)^2,\qquad
 g_{qq}=a_C(L_Cs_n/L_n;p_{10})^2\,\Phi_q^2.
$$

新叶只收紧 $L_C$ 和 $a_C$ 的包围；不把 $L_n$ 当准确 $L_C$，不删控制项，也不把数值编译器的 C² 描述当准确目标证明。

各 metric 视图把独立的 `CoastTargetRange(current.target)` 作为局部参数传给原 `Prefix.inspect`；evidence 在自身 `target` 中调用其 `closed_range`。原 target 对象与工厂模块都未被猴补。R483 遍历每个原 piece，计算真归属 local interval 与该 piece 原闭区间的交，并 hull 全部可能归属。所有共享端点和原十个控制项保留。

coast 符合原结构识别条件时，它在同一宽度 $\ell$ 与局部变量 $t$ 上使用

$$
 a=A-\kappa\ell t+\ell^2P(t),\quad
 a_s=-\kappa+\ell P'(t),\quad a_{ss}=P''(t),
$$

以及既有的 27 个半径双 Bernstein 系数、两个宽度端点各 8 个速度系数和 7 个二阶系数。所有这些系数由新叶求值状态形成，仍包含同一 $C$ 的实际 $A,\ell$。结构未选中的 piece 原样回原完整公式，不因此被省略或判失败。这里调用 R483 已付包含性，没有新拟合、取样或另立 global domain 门。

## 495.5 准确 cut patch 的完整作用与尾部界限

R416 及其 M/分辨率派生的准确 chart 系数全部由同一原 DAG 给出。以 $k=L_C/L_n$，原准确 $v,b,q$ 为例，物理 $s_n$ 的三阶匹配仍由 $kv,k^2b,k^3q$ 及原反函数三 jet 表达支付。R495 新 model 重新包围所有七个原系数，`RefinedCutBundle.evaluate` 委托原家族的完整 `AccurateCutBundle.evaluate`。因此新叶确实进入受影响的场六 jet，而不只是更新 target 的说明字段。

原 R409 定义用的完整节点值/一二阶数据、共同 B、prefix/native Hermite 片、cut 窗口、registration、所有均值和材料 Fourier 模式仍是原件。R492/R495 不声明这些节点是精确连续 ODE 解，也不支付原 RK 轨迹误差或全连续解收敛。

**范围边界：** `ActualCompleteCTarget` 仍读原 definition 所绑定的原 f12f C result，live 版本仍用原 R426 provider。故在 native/collar 的径向目标仍是原实际闭 query 的 $E_C(r)$，角目标仍是 $r^2\Phi_q^2$。不得把本次 R489 新 cut 叶当成整个尾域的 $E_C(r)$，也不得替换为 $1+B'(r)^2$。R495 未把新全头累计原件接到 R426 的尾查询链，空间细分不会自动消除其原累计包围宽度。

新场六 jet 与旧尾 query 一起使用是合法的：两者都包围同一 $C\in\mathcal C$ 的实际值。独立区间组合可以更宽，但不排除真实值。这里没有对它们任意盒中点共同实现的声明。

## 495.6 四 Loewner、完整闭 DFS 与两帽

五个 metric 视图保留原 root plan、原 `roots`、完整角圈、两反射片、全部 prefix/native/collar/patch、每个闭端点、原 `split_cell` 与原四个严格 Loewner 检查。变化仅在实际传入的求值对象和局部 coast range。

因此每个原检查的数值输入仍外包实际 Gram 与同一准确目标。若原检查证明该 cell 的相对误差不超过指定 $\eta$，同一个结论适用于新求值对象覆盖的全部真实函数值；若不能证明，原分裂与未决机制不变。没有以块数、已访问点数或某个旧布尔值替代完整闭覆盖。

帽仍由原 R413 attachment 与实际 R417/M/union 帽对象绑定完整 marker 列表、side、原 cuff 与高度定义。两帽图与目标完全一致时，原 `cap_metric_identity` 的准确零误差结论继续成立。R495 不新扫帽、不增数值帽门，也不凭 active Gram 冒帽曲率/reach 证书。新叶不修改帽的任何定义数据。

## 495.7 实际全域误差量与全部 t

证据视图逐字保留 R459/R464 的 `relative_norm`、完整 ancestor-bound 覆盖、真正 t 点查询、原误差上下界与比较逻辑。它测量实际完整闭面相对算子误差，不把多个同 $\eta$ pass 当误差下降。

令 $G>0$、$E=DF^TDF-G$。R459 的原相对算子范数量等于 $G^{-1/2}EG^{-1/2}$ 的最大绝对特征值；其区间实现继续保留正目标与实际判别式条件。R495 不改变该公式，也不把某个 Gram 盒中心当矩阵。新包围通过与原相同的公式产生实际下界/上界；不承诺新上界一定更小。

共同材料接口仍接**原已登记对象**，而不把 R495 新 schema 伪装成旧来源。由495.2–495.3，原材料对象与新 cut 视图是同一个准确函数的两种包围。因此原材料接口给出的实际有限 t 点六 jet 仍是有效包围，只是可以更宽；这些点的 field 区间没有被声称已经使用新叶。它们的 target range 则由新 target/coast 求值。

对原严格正材料密度所保证的角微分同胚，方向仍为

$$
 \psi_{j,t}=\Theta_j^{-1}\circ(\Theta_0-\alpha),\qquad
 \alpha=\pi t/2.
$$

相位场由原准确角换元与共同刚转给出；两帽固定。对误差矩阵与目标同时作可逆导数的同余变换，不改变广义谱。完整角圈经 $\psi_{j,t}$ 双射，所以完整基底角圈的统一上界适用于全部 $t\in[0,1]$。这里调用 R443/R447 的既有 atlas/gluing 责任，不声称某个材料表达中的 $g$ 自身平移对称，也不把非线性角换元延到帽中心。

同一证据源码的实际 `compare` 仍核同 fixed-target signature 与原 clock。$U_{j+1}<L_j$ 是证明真实 sup 严格下降的充分条件；仅 $U_{j+1}<U_j$ 是包围上界改善；重叠保持未判定，继续原预算内精化不被阻止。旧 R459/R483/R464 result 不能改 schema 后冒本源输出：若要进入本源的比较，需要对各真实场实际执行本源测量。原 solver/native 容差没有被换算成不存在的全域 metric floor。

## 495.8 原钟、完整未访与必要读回

metric 的原单调时钟从原 source/setup 前启动。绑定新叶时，局部检查沿原开始时间；绑定完成后只把总额度裁成原额度与实际 R489 绝对截止时间的剩余量，不能重启。该裁剪是否实际发生单独记录，绑定前异常不填“已裁剪”。每次 DFS pop 之前还检查 provider 的实际原绝对截止时间；若已取出 cell 后异常，原 `current_cell` 与其栈按原 coverage 函数完整保留。

evidence 原 Budget 已绑定 first-material 的原 deadline；新 provider 的 deadline receipt 必须与它逐 bytes/SHA 相同。R492 的真实资源异常独立识别为资源 partial，不推断数学失败；原 ArithmeticError/ValueError 单元处理与全部原接受条件不变。

这些是协作式检查。R495 没有新增 OwnedChild，也不声称一个区间运算能被内部异步硬杀；后继调用者仍须用原真实 owned process、绝对截止时间、TERM→KILL/wait/reap 与 quiet。没有新 request 或实际外层编排在本结论中被宣告完成。

必要摘要保持单份 90000 B 上限。当前根、完整 frontier 地址、原未访 rank 后缀、全部实际 error/resource 字段沿原程序保留；已经退出但未付的叶在原完整 ledger 保地址与身份，不能说每一行正文已回传。新增新叶/新系数/coast 身份可能使某次必要摘要超过90KB；其原70退出与 raw 保留不改，不承诺一定适配、不分块编码大原件、不删未读数据。

## 495.9 独立源码生成与未付范围

发布的是一个薄桥、一个标准库 source generator 和完整显式 replacement plan；六个生成视图只在实际同目录 computations 新 basename 中形成，不把约三十余万字未变数学核重复刊入仓库。generator 先完整核选中 baseline/helper/source 身份，再在内存核每项 literal replacement/count 与新全文 bytes/SHA，全部成功后以 `xb` 创建新文件。它不导入、编译、AST 或执行数学模块，不覆写原源。不同 role 可独立选择；未选择的角色明记未生成，不能冒其消费者已调用。

R464 incremental 源是原生成器的真实产物。后继调用须先取得原完整发布依赖并实际生成这组来源，再执行本 plan 对相应 baseline 的绑定；不得在尚未生成时把新文件当既有 Git 文件校验。

本结论完成了同语义新 cut 叶到四种实际场家族的前缀 target、准确 cut 六 jet、完整闭域 Loewner 与实际 opnorm/evidence 的调用链。它没有完成新 C 全尾 query 的替换，没有重算 field 或原 native/J/FD/fullDN，没有生成任何接受父，没有给出实测误差下降、reach、held、嵌入或机器精度终点。原 first A/B、共同材料、同一准确 $g$ 与全部末门仍分别由实际来源支付；新 consumer 不是这些原工作的新前门。
