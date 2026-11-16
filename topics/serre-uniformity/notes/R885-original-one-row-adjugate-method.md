# R885 首producer：原多项式特征关系与一行伴随

本方法只执行 [R885](../results/R885-original-one-row-adjugate-and-whole-Artin-fibre-norms.md) §§2–4 的完整算术。结果名 R885-original-polynomial-one-row-adjugate；最终证书 p41-original-polynomial-one-row-adjugate-certificate.json。没有将后继整Artin代入或九范数预称已成。

## 实际来源

唯一数值源是原 R827 run43734420663/source400edecfeab313d1858cdb72bf18f8452ab9566a 的完整阶段。该run最终BudgetStop并不否定其已完成W、place audit、八点grid与各Krylov阶段。原完整manifest19902271字节/SHA2609de217bf1da048f7987ae7de09df38ac24fb63e82d45add1e7c6b9cdbea7e，完整数学configuration为7f86690b743e182580ce7ca25745afa3dd326364e76b4a1c65122f948b45bab0。

public wrapper使用真实Archive身份和Range读取完整manifest及上述必要小阶段，不下载3.6GB整ZIP或原Hermite操作历史。八个K节点从真实grid引用选择，不根据文件名猜它们的值。原run receipt必须为已结束exit124，原完整阶段complete=true且保旧configuration。新源包仅这些实际数值输入与必要元数据。程序不实例化旧数学Job，不重求原W、g/h、K或K逆。

## 273个节点

先核原全部矩阵条目的weighted次数界。使用grid实际八个不同节点作为列表前段，再追加最小尚未使用的非负整数，直到273个。每个已有K节点仅新增k272=Wk271和h=K^-1k272，全272项核Kh=k272，给T272−Σh_iT^i。原K、K逆和W(a)全部读取；没有新K求逆。

其余节点仅以原四个W系数块Horner评价W(a)，调用python-flint0.9.0公开的nmod_mat.charpoly。节点阶段完整保存单首一272次多项式。每个完成节点原子保存，同tag续算直接复用。

对c_k取前k+1节点作普通Newton差商插值，所有节点差须非零；原域大小大于全部节点。按R885真degree≤k界，再完整核全部273节点的所有特征多项式系数。这一步从未要求节点为Krylov好点。最高单首一项逐节点也核。

## 单行递推

保存b0=e0^T，再以b_k=b_(k−1)W+c_k e0^T计算至k272。按z幂排列系数矩阵，只用四个原Fp矩阵块右乘，幂数以行移位表示。实际全零的W系数行可以跳过；这只是原矩阵零项消除，没有换normal基或不同算术对象。

每层完整核所有degree>k+eps_j系数为零。第272层必须对整个多项式行全部系数核零，保存真正末行Cayley–Hamilton证书。最后将前272层按T^(271−k)索引，给出r=e0^T adj(TI−W)及完整多项式恒等式。没有物化整伴随矩阵，也没有调用扩域矩阵接口。

## 输出与恢复

数学阶段均在输出根目录，前缀R885-adjugate-，包括source-audit、273个charpoly-node、polynomial-characteristic-relation、row-level000至272、full-polynomial-adjugate-certificate及内容命名的stage-manifest。current明确complete=false，不混入完整阶段。所有已完成节点/插值/行层只读复用，预算仅在新原子阶段前检查，不能因预算已到丢弃刚完成的返回值。

tag绑定新coreSHA、固定python-flint0.9.0、正式证明与方法、原R827全身份/配置/实际选件、固定273节点选择规则、左行递推及weighted界。预算与物理目录不入tag。false FINAL是历史endpoint，不约束已推进current；true FINAL必须准确引用完整当前inventory。外timeout为预算加900秒，保留真实已完成文件；缺core receipt只记录null，不伪造。

## 边界与后继

成功仅声明原模p753特征多项式和完整单行伴随已认证。target_Artin_normal_coordinates_computed、nine_reference_norms_computed以及原Picard/nonp/height标志均false。独立后继将本producer作为真实外源，结合已成R88217列、R879参考v0、R807 theta/N692，执行R885 §§5–9。不会改本core/tag或重算完成节点和行。

所有新数学仅公开Actions，最长300分钟。一日artifact保留完整数值阶段与原来源载体；Git只放源码、参数、证明及简明运行/SHA登记。workflow sparse checkout、真实git pull/rebase与README差异检查保持原要求，pip命令用块标量。
