# R133 补充：实际 sharp Bernstein 完整角流与相对腰间隙界

2026-11-16。此页记录首次公开 Actions 的完整新结论 WBFA；前驱证明为 [WBF](R133-supplement-sharp-Bernstein-and-integrated-finite-flow-jets.md)。本页中的数值全部逐字读取该次已保存的小科学结论，没有在代码模式求值新的科学目标。

## 1. 实际结论与作用域

公开仓库 Rogerhu12/math-research-public 的 run **43870348355/1** 成功完成五个自然结论，共 **83 个新标量记录**。31 个科学字段、16 个完成门与16个进度字段均完整；33 个原标量对象和12个原资格对象保持完整原字。旧科学调用、旧目标重算、旧指数重算、旧二进制恢复均为零；本次新指数、对数、平方根、分数幂、ODE 与求积均为零。

同一选定真实参考、同一 $\eta_0$、物理角周期 $\pi/2$、原3070个接口、两条物理mean坐标与真实根没有改变。严格实区间为
$$
0\le r\le c,\qquad
c=\frac{76285779072683}{320000000000000}.
$$
原根区间仍是
$$
\left[\frac{1191984371497}{5000000000000},
      \frac{2383968743003}{10000000000000}\right].
$$
全部结果是普通物理角导数的完整上界，适用于相同原资格中的所有较短区间、两个定向、两个特征流以及漂移流。它们不是Wiener $A_0$ 范数，也不是对复根盘的解析延拓。

| 自然结论 | 新标量数 | 完整对象 |
|---|---:|---|
| sharp flow | 14 | 普通流导数阶2至15 |
| sharp phase | 14 | 普通相位导数阶2至15 |
| relative bulk | 14 | 同一正 $x$ 的普通角导数比上界阶1至14 |
| transport relative | 27 | cut组合阶2至14和bulk组合阶1至14 |
| relative omega | 14 | 同一正 $\omega$ 的完整相对角导数界阶1至14 |

原 $F_1,P_1,K_1$ 保持原记录，不重复求值。WDG已完成的80个新量及其cut-relative界只读。此处没有宣称相对 $\omega$ 的15阶界，也没有宣称混合jet、全误差小量、真实物理逆、有限Schur逆或非线性族已完成。

## 2. 数学接线

前驱WBF证明直接针对同一完整、已知有限Fourier支持的真实参考。漂移标签次数192对应物理频宽 $\Lambda=768$。Riesz移位恒等式给sharp Bernstein界
$$
\|\partial_\phi^k d\|_\infty
 \le 768^{k-1}\|\partial_\phi d\|_\infty,\qquad k\ge1,
$$
因此没有旧的 $\sqrt{385}$ 系数转换损失。常数并非来自有限网格探测。

原WX完整正算法已经证明所有较短区间上的
$$
\exp\!\left(\int D\right)\le F_1,\qquad D=\|\partial_\phi d\|_\infty.
$$
本次仅使用这个已证明的正比较预算。没有由任意流导数的范数上界反推指数积分。

完整角变分比较的生成式可写成
$$
w_A=\frac{e^{768w}-1}{768},\qquad w(0,h)=h.
$$
其精确有限系数给
$$
G_1=F_1,\qquad
G_j=768^{j-1}\sum_{k=1}^{j}(k-1)!\,
   S(j,k)(F_1-1)^k,\quad 2\le j\le15.
$$
这里只对正系数多项式有向求值。推导中的指数与对数没有进入本次数值程序。

相位界使用全部普通Bell项与原cut相位导数阶1至15：
$$
P_j=\sum_{k=1}^{j}\Phi_{c,k}B_{j,k}(G_1,\ldots,G_{j-k+1}).
$$
只有 $j\ge2$ 是本次新目标；$P_1$ 原字复用。令原真正正下界为 $m_\Phi$，取
$$
X_b=P_{b+1}/m_\Phi,\qquad 1\le b\le14.
$$
这里是不同角色的有效上界与真正正下界相除，没有相减或相除两个独立上界来冒充真实函数的商。

设WDG原cut相对界为 $C_b$。完整两个非负贡献为
$$
K_b=\sum_{k=1}^{b} C_k B_{b,k}(G),\qquad
B_b=\sum_{k=1}^{b} X_k B_{b,k}(G).
$$
$K_1$ 已经存在，故只读。全cut原子与普通 $dr$ 积分的同一正概率比较给
$$
\frac{|\partial_\phi^b\omega|}{\omega}
 \le R_b:=\max(K_b,B_b),\qquad 1\le b\le14.
$$
各贡献均先保存并回读，再形成最终max；没有从两份独立上界作差。所有普通Bell系数、非零cut与完整普通径向积分均在同一证明中保留。

## 3. 实际完整相对界

下表逐字保留该次科学JSON的14个最终ball字符串。使用它们时必须取程序已经规定的有向上端。表格只是便于阅读；后续消费者必须连同完整科学JSON的参数、原输入、scope、门与源身份一起核验。

| 阶 $b$ | 完整原ball |
|---:|---|
| 1 | `[383257932.783812447923633013960482061232966233735175682670668252716033619133 +/- 4.27e-67]` |
| 2 | `[423538287407127.642170543188891588037751034295526236209290716385219340416136 +/- 2.16e-61]` |
| 3 | `[702078031113152715769.376458661094283440915811491092752412216777388915502165 +/- 1.52e-55]` |
| 4 | `[1551747774053253609886303445.44233084521726372965047687857310507804259323454 +/- 1.86e-48]` |
| 5 | `[4287175593240246554280066180419026.03199365849550300231293940814516809022400 +/- 3.56e-42]` |
| 6 | `[14213677063338540076121219752977470381769.6547145009188015877729756360182906 +/- 1.15e-35]` |
| 7 | `[54978330756379124361723434776257954189192543802.0826332841242536951559017920 +/- 4.13e-29]` |
| 8 | `[243036325331939345958050619220603443698009745404377018.031100905838839412174 +/- 3.25e-22]` |
| 9 | `[1208663718280589956552627313279195439197846736156003286518180.69283151145053 +/- 9.27e-16]` |
| 10 | `[6678809214288788128052072795086582135558921664024115945187804714574.57686917 +/- 4.66e-11]` |
| 11 | `[40596327302071847302274157053598778212077351034800043578815110676662841996.9 +/- 1.14e-3]` |
| 12 | `[2.69193299049754419705578013986401265393180408657694677385195439657822082253e+80 +/- 2.67e+4]` |
| 13 | `[1.93377030405332824215678075136740853279948574421938848585868159632648740732e+87 +/- 2.26e+12]` |
| 14 | `[1.49599825598193029062256171513009572448582346132172608969056696769825200021e+94 +/- 8.50e+18]` |

旧WDG第14阶候选约为 $6.8453\times10^{105}$，本次第14阶约为 $1.4960\times10^{94}$。这是完整候选上界的降低，仍不构成后续全算子小量结论。旧候选及全部原始完成记录继续有效且不重算。

## 4. 后续混合jet消费者的准确接口

全部路径相对于完整科学JSON。阶1的流与相位必须使用原拷贝，不能重新运行前驱。

| 对象 | 完整字段路径 |
|---|---|
| 原 $F_1$ | copied_original_scalar_records.flow_1 |
| flow阶2至15 | complete_new_graphs.complete_new_sharp_flow_conclusion.new_records.ordinary_flow_orders_2_through_15 |
| 原 $P_1$ | copied_original_scalar_records.phase_1 |
| phase阶2至15 | complete_new_graphs.complete_new_sharp_phase_conclusion.new_records.ordinary_phase_orders_2_through_15 |
| 原真正正相位下界 | copied_original_scalar_records.strict_phase_lower |
| 原 $K_1$ | copied_original_scalar_records.cut_composition_1 |
| cut组合阶2至14 | complete_new_graphs.complete_new_sharp_transport_relative_conclusion.new_records.ordinary_cut_contribution_orders_2_through_14 |
| bulk组合阶1至14 | complete_new_graphs.complete_new_sharp_transport_relative_conclusion.new_records.ordinary_bulk_contribution_orders_1_through_14 |
| 完整 $R_b$ 阶1至14 | complete_new_graphs.complete_new_sharp_relative_omega_conclusion.new_records.complete_strict_relative_omega_angular_orders_1_through_14 |

数组严格按阶递增。全部都是普通物理角导数；进入WSJ冻结 $t_0$ 的双索引归一jet时仅除一次角阶乘。不会把标量sup改名为背景 $A_0$；径向导数还须独立使用完整方程与真实正因子，不能由这14个纯角量补造。

## 5. 源、参数与完整输入身份

运行参数全部在固定manifest与科学JSON中保留：Arb320bits、Python3.12.14、python-flint0.9.0、75位打印、5自然图、83新记录、33原拷贝、12scope、0history。程序只调用一个新的科学入口，旧producer不导入。

| 文件 | Git blob | 字节 | SHA256 |
|---|---|---:|---|
| topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/actual-scientific-conclusion.json | 32ff92c516fcc5c43f3619930d4845d294289270 | 72251 | 8af3af0a2dc08a6611189178099c63b0e2ac5ae8e9d767c0e211861c6d63de1e |
| topics/visible-flex-exact-nearby/notes/global_fold_free_transport_finite_jets_ci/run-43820816332-1/complete-original-inputs.json | d6d13860e322d82ce354c8c0d0eb0f279ca63b3c | 31632 | 3c5588f13de4dc544f519b2fb99f372bba3200ccee79def665ce5bd1d3c3dd66 |
| topics/visible-flex-exact-nearby/notes/positive_drift_relative_omega_ci/run-43865837250-1/actual-scientific-conclusion.json | 67c7070e6678223b5de63635d4b18f110500a742 | 47714 | 04b757433390715acd5e2bca3cd29afef0ccf3e3cea35d5855a96eb28bf89395 |
| topics/visible-flex-exact-nearby/results/R133-supplement-sharp-Bernstein-and-integrated-finite-flow-jets.md | 0c1a3593617a4134ea875697a268b7b6eea3bb3b | 16027 | 2dd1cdc598fde3ca47ca1cf0d787fdc60b9ced5601654865cfc3736cdba6c323 |
| topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_sharp_Bernstein_finite_flow.py | 2cf08c631a2ab45dca147ec480729393ef69ba68 | 78191 | 7534760ac0e6867425c773598438c7909a502b6d84e05cc5c7c430637eee2ac7 |
| topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_small_frozen_public_worker.py | f966a6a05b18794927c3674956fb617e7dbaa244 | 25584 | 7abb8783fc3ffc9f3194bb9cab8e1d8c12d28395b9e4b0981c682c879aa39d18 |
| topics/visible-flex-exact-nearby/notes/2026-11-15-1133-R133-reviewed-public-CI-rules-cleanup-history.json | 5c5d020913d717bb5bc8ce891297e00eaa8944f7 | 2461 | 65503a41254348a301fd71657ea61e5c32aa2d0bf7c980967b9ae35022a6b1d1 |
| topics/visible-flex-exact-nearby/notes/2026-11-16-R133-sharp-Bernstein-finite-flow-current-inputs.json | 03166ea9714818f997f27f5a80e4c55ceaecb7b8 | 19449 | f3a9f5205bf8a91c1edf3e1fdb89787c0392bb047f07d7396f235e49300b27a3 |

完整原拷贝身份使用排序紧凑JSON加一个换行：

| 原对象 | 数量 | 字节 | SHA256 |
|---|---:|---:|---|
| 全标量记录 | 33 | 3847 | bc53ed42da3d2c81c70903c0517e9d4d39fd49ed99de590044b35d09bb62e65e |
| 全资格对象 | 12 | 21153 | e5d8a593d9a29998d4c1bb96165b1098225f3f7d145b44489f8d7d4857d00d2a |
| 全原接纳回执 | 完整嵌套对象 | 15709 | 4ef523df6fd6f1a275fcf0399ae90ee51da2d4b23f1a0d7ad4a8f278a525a558 |

原WGS的437槽与24门、WDG的80槽与16门、原源/manifest/run/companion绑定都在只读预检中完整检查。预检不导入flint，不计算新的科学目标。

## 6. 实际执行、保存与README回执

workflow事件提交0465d714f7233c7787b0ab279f28df14994af882；consumer封包提交f8a9228d678147cf7e9d8acc109702a4015e6a4a。只读预检checkout为workflow事件提交；其后consumed marker普通提交6c7e71e0cd53bb15ebdfe024cc7f9574d27c0a84成为实际科学checkout。这两个阶段的提交不同，回执明确区分。

科学child于2026-11-16 12:51:47.523803 UTC启动，12:51:48.023237 UTC结束；child wall为0.499383617999996秒，数学段内部计时为0.22349473999999958秒。两种计时各自保留。一个child返回0，全部83新记录先原子写入、刷新、保存完整prefix，再输出并回读。没有失败目标、丢失已成记录或授权重试。

| 实际输出 | Git blob | 字节 | SHA256 |
|---|---|---:|---|
| topics/visible-flex-exact-nearby/notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/actual-scientific-conclusion.json | df5ea6fff610d70ad98fbebc9dd004d24388ce86 | 59417 | 87621adee76080dbbc14abdd7f8e5dce5d3e2742ba299fc941d13ff40f4410c0 |
| topics/visible-flex-exact-nearby/notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/execution.json | bd14fe2fe6ad17c91eb20a4b38f6caf9c093e5e6 | 25491 | 057250199c0624f7b69972dd032a5df1f173e624fcb02036e701a973ee26034b |
| topics/visible-flex-exact-nearby/notes/sharp_Bernstein_finite_flow_ci/run-43870348355-1/report.md | a0cf4b936a2f2d44d1a9139ca59fae3997844102 | 445 | 6301c1a6daeffa4b10c23b3bc6e02e3b80a2267b2bd375750d6d50e7e92d6f7f |

三个输出合计85353字节。科学JSON59417字节小于90000限制；执行JSON25491字节小于59000；报告445字节小于8000。完整child stdout为5166539字节，SHA256为43c8244f92a9150b6af16e146e3862ce210293f667988b9d3ac214f15c054241；正文不提交、不拆分、没有经connector读取。

worker在科学启动前实际topic容量199629980字节；consumed marker后、紧邻child之前为199630618字节。执行前与紧邻child前均支付完整157000出版预算和120000预留；marker另外检查。实际结果保存按实际容量上限检查，没有为了留空而截掉已完成结果。

四次真实git pull的完成时间为12:51:41.196142、12:51:43.250670、12:51:46.704453、12:51:48.256116 UTC。前两次after为workflow事件提交，后两次after为实际科学checkout。两份README的实际diff及相对于已读提交2f72b274f8647dbf6ce236ff2185cbe22153f8e1的diff每次均为空。执行JSON保存四份完整回执，链SHA256为7b03a7884a9c625dfb7573651c7cfc4b96f2487d200bded2b6734923930971c7。

root另按文本、schema与hash核对32组条件：完整31字段、5图的全部83个ball和形状、16门/16进度、33拷贝/12scope/全accepted、7输入、源AST/模块/参数/manifest、公开run和阶段checkout、完整只读预检stdout及四pull回执链，全部通过。实际执行JSON有43字段；只有超过四次pull需要压缩保留时worker才增加readme_retention字段。本次没有假称存在该字段。

## 7. 继续保持的全部独立义务

同一真实root、正侧响应、两条物理mean及mean ODE、四个腰端点、3070个接口jump、完整 $H^{-1},\mu^{-1},G$ 与forcing、全部source ports、真实96列的signed归一化、有限块的两rhs与全部四块仍须继续。原 $n=4|j|$、$\alpha$、$\sqrt2$、affine/height和有限因子均不因本次角界而省去。

当前仅提供下一完整严格实域混合jet与profile消费者的新角前驱。相对15阶、局部根盘、全误差小量、负侧head/$\nu$/两mean/$\Theta$/高门、所有阶tame及同一对象的非线性matching均未由本次计算闭合。本课题README的真实闭 $C^2$ 固定度量连续族完成标准仍未达到，继续处理open中的实际剩余问题。
