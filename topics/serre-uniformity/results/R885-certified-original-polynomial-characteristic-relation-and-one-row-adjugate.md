# R885. 已认证的原特征关系与完整单行伴随

## 1. 实际完成的结论

2026-11-16 的公开 Actions 已完成 [R885 原单行伴随证明](R885-original-one-row-adjugate-and-whole-Artin-fibre-norms.md) §§2–4 的独立 producer。实际数学运行时间为 **49.87897484799999 秒**，退出码0、error=null；随后冻结 stdlib verifier 完整通过原来源身份、输出字节与终点字段。

固定原 genus127 曲线 $Y$、level82、原 $-3$ 下降及原正规基，取
$$
 k=\mathbf F_{1000000753},\qquad
 \epsilon=(0,1^{144},2^{127}).
$$
令 $W(z)$ 为原 R827 已完成的同一素点乘法矩阵，方向不变。此次实际得到
$$
 \chi(z,T)=\det(TI-W(z))
 =T^{272}+c_1(z)T^{271}+\cdots+c_{272}(z)
 \quad\text{in }k[z,T],
 \qquad \deg c_i\le i.                              \tag{885C.1}
$$
还实际得到全部 $273$ 个多项式行 $b_0,\ldots,b_{272}$，满足
$$
 b_0=e_0^{\mathsf T},\qquad
 b_k=b_{k-1}W+c_ke_0^{\mathsf T},\qquad
 \deg b_{k,j}\le k+\epsilon_j,\qquad b_{272}=0.       \tag{885C.2}
$$
故
$$
 r(z,T)=\sum_{k=0}^{271}b_k(z)T^{271-k}
       =e_0^{\mathsf T}\operatorname{adj}(TI-W(z))    \tag{885C.3}
$$
是原指定的完整左伴随行，并且全部272个分量满足
$$
 r(z,T)(TI-W(z))=\chi(z,T)e_0^{\mathsf T}.            \tag{885C.4}
$$

这些是指定有限域上的完整多项式恒等式；不是少量测试点上的相合，也没有将它们改称已展开的特征零有理坐标。原 $W$ 的有理身份、约化位置与正规基来源仍沿既成 R806/R827，未另换曲线或基。

## 2. 原来源复用及实际认证链

本次只读取原 R827 的15件完成输入，包括完整 $W$、实际 place、八个原循环点及其既成 $K,K^{-1}$、原 manifest 和身份元数据。该历史 run 在后续 Hermite 阶段预算退出，不能因此否定已完整保存的这些输入；本次也没有重做其后续 Hermite。

原八点实际为 $0,1,\ldots,7$。本次在这些点只新增缺失的
$$
 k_{272}=W(a)k_{271},\qquad h=K_a^{-1}k_{272},
 \qquad K_ah=k_{272},
$$
由原已证循环性取得该点的特征关系。其余节点按冻结次序补最小未用非负整数，因此此次完整节点为 $0,\ldots,272$。新节点只计算原 $W(a)$ 的特征多项式，没有再求 Krylov 逆。

原加权界
$$
 \deg W_{ij}\le 1+\epsilon_j-\epsilon_i
$$
在全部矩阵条目上核过。主子式中权数相消给出 $\deg c_i\le i$，故逐 $c_i$ 插值后，在全部273节点准确代回就认证 (885C.1)。每个 $b_k$ 用原四个系数矩阵完整左乘递推并核加权支撑；最终 $b_{272}$ 的全部多项式分量实际为零。原 R885 §§2–4 随即给出 (885C.3)–(885C.4)。

冻结终验日志实际报告：

| 字段 | 实际值 |
|---|---:|
| complete | true |
| actual_complete_stage_count | 549 |
| actual_completed_node_count | 273 |
| actual_completed_row_level_count | 273 |
| actual_original_modular_characteristic_polynomial_certified | true |
| actual_original_complete_polynomial_adjugate_row_certified | true |
| selected_original_file_count | 15 |
| all_output_bytes_and_original_source_identities_verified | true |
| old_W_or_Krylov_arithmetic_recomputed | false |
| new_mathematics_executed_in_verifier | false |

549个数学阶段由一份 source audit、273个节点、一个多项式特征关系、273个行层以及一个完整伴随证书组成。上传步骤另明确报告562个实际输出文件。后继纯 IO 已读取原 manifest 的560条记录及其 reference，二者与上述文件数相符；数学阶段数仍为549。

## 3. 已读取的实际身份

原始运行与日志入口：

- [run43842694142](https://github.com/Rogerhu12/math-research-public/actions/runs/43842694142)
- [数学及冻结终验 job133215160383](https://github.com/Rogerhu12/math-research-public/actions/runs/43842694142/job/133215160383)

本登记依据实际 job 日志中的 R885_INPUT_REVIEW、R885_CORE_RECEIPT、R885_VERIFY、上传回执及原 GitHub artifact 身份；没有在本地执行新的数学。

| 项目 | 实际值 |
|---|---|
| source commit | 0210f90f1ac7d2c89e948cae0cdc5f64f775dc07 |
| result | R885-original-polynomial-one-row-adjugate |
| core | R885_original_one_row_adjugate.py |
| core SHA256 | dd4ef0d445e7c90caf568d7aa87951166d6730cc86da0a44be11b664742d3035 |
| public wrapper SHA256 | 12790bfaecf685ec66e2d6a1dca9a9cd4f74ad39f70f48e172bf5c23ac652c17 |
| [执行契约](../notes/R885-original-one-row-adjugate-method.md) SHA256 | 8f9714e573a9f4c4da02447f8a8c7b35665e04aaf179d3cea68d0db9f2b6c188 |
| 原 R885 证明 SHA256 | 1c67eca3f9140f7cd67b77e86c85a1fac7fdc89634331de3bc1ed80579a978f7 |
| 实际 configuration SHA256 | f4a4973d93b328bd76f93d41b668e70a0817c1510012b9824370a18858ed634a |
| FINAL | p41-original-polynomial-one-row-adjugate-certificate.json |
| FINAL bytes / SHA256 | 7104 / fc323a7d1b74a03ff3c846c2dfa92e4cd7c5269b20b3eebd857439e727d73d30 |

实际 artifact 为：

| 项目 | 实际值 |
|---|---|
| ID | 14214590084 |
| 名称 | serre-global-R885-polynomial-one-row-adjugate-43842694142-1 |
| 平台 ZIP bytes | 64381078 |
| 平台 ZIP SHA256 | 42bebd740b7bf4535ac7af50f072bcac8d1b7fc3a29796c43ad218c5c140021b |
| expires_at | 2026-11-17T09:47:33Z |

该 ZIP 摘要来自真实上传与平台身份；本文没有声称已另行下载整64MB并重新哈希。

实际继承的 R827 数学身份为：

| 项目 | 实际值 |
|---|---|
| run/source | 43734420663 / 400edecfeab313d1858cdb72bf18f8452ab9566a |
| core SHA256 | d9cf773976f3beff7f44ff30f8b593665f481470cb52297239710e0ce6e062d2 |
| 原 manifest SHA256 | 2609de217bf1da048f7987ae7de09df38ac24fb63e82d45add1e7c6b9cdbea7e |
| 原 configuration SHA256 | 7f86690b743e182580ce7ca25745afa3dd326364e76b4a1c65122f948b45bab0 |
| 15件原选择指纹 | 68de6174297a2bd6ef06486329948451ba8b04151a03929780bfd87efdad3cd4 |
| 原 W 阶段 SHA256 | 5bcbadf437c2ac91431771b6d9818b99436008e9a5db4caa185dfac8aca5f841 |

W 阶段为 R827-original-W-g-h-reductions.json.gz，763994 bytes；真实 grid 为 R827-eight-original-unit-cyclic-nodes.json.gz，2531 bytes、SHA256 2c58c02cd89e36301cb30a9f2d2d2dc04ae6ca66b25819ff84b36ae50736c3f3。各原 Krylov 文件的完整引用已经在此次实际 configuration 中逐一保存。

## 4. 实际小 IO 与后继逐件来源

[纯 IO run43844748582](https://github.com/Rogerhu12/math-research-public/actions/runs/43844748582) 已于2026-11-16 10:15:35完成，job133230055036，source85049ecab0b62dd5e7a3983841844ddee52b3da4。实际 R885_ENDED_SMALL_IO 摘要已读取，核原 reference、manifest、meta、最终证书、source inventory、特征关系、完整伴随索引、阶段清单和首末行。此次只传输476711个HTTP Range字节、13次请求；没有下载原13MB载体或全272个伴随行 payload，也没有执行新数学。

实际重要成员如下，均为原 producer 的原字节：

| 成员 | bytes | SHA256 |
|---|---:|---|
| full-outputs-manifest.json，560项 | 77918 | 51dff64343665bf629603f42e43cc21ecc10aaf17912df5cc6f20bb7b8973154 |
| full-outputs-manifest-reference.json | 181 | 1d092090c3f79fc50fc603e7c34b190c65e7d7544d493c71e2841526294e2ac3 |
| R885-adjugate-polynomial-characteristic-relation.json.gz | 194378 | fb8dbdd0a97eef2cd10a08f61afc55865203267c157d7e64c78c9a311a73486b |
| R885-adjugate-full-polynomial-adjugate-certificate.json.gz | 17474 | b49becb6df241cdb0e075c810f7e25865255de1389d62475c3f6db082517a106 |
| 实际 stage manifest | 27932 | b5f1d748f76fe9b496bfa6806da6e720d39d4fdcc27ad49616287c09c2a4abcb |
| R885-adjugate-source-audit.json.gz | 2765 | 90bf9ac57e89910f4a9cd2da3852056479d124a8673494c24113e0a2cc62c5ad |
| R885-adjugate-row-level-000.json.gz | 2169 | b6f92cbcda282bd05872c97541e3c04d26dfe2b2bc683e1db22b2df8f14145d1 |
| R885-adjugate-row-level-272.json.gz | 2954 | f3daaadff095120d978d51c6c5ff12dd1639789e2ab0859697369f739e3f0781 |
| R885-original-source-inventory.json | 5704 | 18ebb9b23926f08780155a19ec0c24bacaa28d75d4adf9179f4f9322e608a1c0 |
| R885-retained-inputs-receipt.json | 1765 | 58f2043a78e1301e96d3666eea5a87be075c1ba83b8b150a249430d4d8d0bdad |
| 原15件 R827 载体 | 13461744 | 95e2c88502c73b285a37f26df0765abd8bb4830742c231ced6f64a066fafa26b |
| core-receipt.json | 4814 | 4663d8ff07e372f68312b98ec78e5a9906d12f32653e0dfbb64af2d71c9564ab |

实际阶段清单文件名为 R885-adjugate-stage-manifest-d20454558b966c2b8c9688c9bea0ed1bc41df52ffd4f3e70b264a314808922cd.json.gz。伴随索引引用的 $b_0,\ldots,b_{271}$ 共272件，原压缩 bytes 总计49435182；后继只有真正消费完整伴随行时才逐件读取，不把小 IO 的首末行读取冒称已再次下载全部行。

小 IO 自身 artifact 为14215552237，641829 bytes，平台 ZIP SHA256 528764e84f0ece979ec79c6f3efb496a4e51352af5e7786bd9da7aae5ece4c1d，到期2026-11-17T10:15:30Z。它运输已成小文件，未新增或替代原数学 producer。

## 5. 完成边界

原 R885 §§5–9 给出之后的合法接口：在完整272维 $A=k[X]/\chi(a,X)$ 上构造自由秩8的原对应代数，以 (885C.3) 评价目标行；只有实际认证所需整体单位、$\chi(U,V)=0$ 及全部272条目标正规方程后，才可称得到完整2176维对应纤维。九个参考范数还需真实 R882 十七系数、R807 准确清分母与 R879 参考函数等输入。这些算术不属于本文 producer 的完成结论。

因此本次终验明确保持以下字段为 false：目标 Artin 正规坐标、九参考范数、原 Picard 活跃支持、全局主元与非 $p$ 校准、原高度或周期计算。它的实际新产物正是可被后继直接复用的完整特征关系和单行伴随，不重复旧 $W$、旧逆或旧 Fourier 前缀。

源码、参数、纸面证明和本简明实际登记可进 Git；完整机器阶段与数值数组仍仅在一日 artifact/carrier 中续传。
