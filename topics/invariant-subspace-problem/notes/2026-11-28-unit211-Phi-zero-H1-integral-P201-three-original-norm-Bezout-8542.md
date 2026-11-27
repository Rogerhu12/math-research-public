# H1：整首一 P201 与三个完整原范数的新 Bézout 输入

日期：2026-11-28（Asia/Taipei）；会话：Astra-ISP-8542378f-20261127。

唯一新源：[原范数 Bézout](2026-11-28-unit211-Phi-zero-H1-integral-P201-three-original-norm-Bezout-8542.py)，Git blob 9051857be180f334d1dec546248548e70e6f37b5，SHA256 b0bf3ee69af6e68bf305f422eddabe9de1f4c5d002092885028ef43ec4d74a64。首次内层120秒、1GiB；若未返回只保已完成目标，不增加时限重放。

## 同一个实际整输入

[P201 整性及完整约化](../results/R150-appendix-unit211-Phi-zero-H1-P201-integral-squarefree-complete-modular-reduction.md)已经证明旧定义的首一 $P_{201}$ 属于 $\mathbb Z_{(1009)}[u]$，完整模像保201次且平方自由。本次只在 runner 内从其固定原定义重建模系数，不传输或入库展开系数。

另外三个输入是[原 v 接口](../results/R150-appendix-unit211-Phi-zero-H1-polynomial-v-source-and-fixed-original-norm-interface.md)中的完整原范数。固定 $\lambda$ 次数组合为 $(6,6),(6,9),(6,10)$，完整四维正则范数对应48、60、64阶原 Sylvester 映射。原式全部系数在 $\mathbb Z_{(1009)}$ 中，完整固定行列式也整；每个原解的同一点必使这些必要多项式为零。不能删除任何首项零面。

本次不重做旧 QQ Dixon Gaussian、已闭 C55 值层、无穷赋值门或旧次数上界门，只重建新 Bézout 目标所需原系数。两份历史 JSON 仅由终端历史加载器读入临时目录。

## 允许的严格结论

设 $H$ 为 $P_{201}$ 与所有已完成原范数的首一 QQ gcd。由于 $H$ 是整首一 $P_{201}$ 的首一因子，$\mathbb Z_{(1009)}$ 整闭给 $H$ 及对应首一商均整。对每个整原范数以首一 $H$ 作长除，其准确商也整。因此完整约化满足
$$
\overline H\mid\gcd(\overline P_{201},\overline R_0,\ldots),
\qquad \deg H=\deg\overline H\le d,
$$
其中 $d$ 是本次实际模 gcd 的次数。

源码每轮乘回二项 Bézout，并把它合成为对 $\overline P_{201}$ 及全部已成原范数的真实组合再全乘回。模因子仅标签实际完备化整块，不识别为 QQ 因子。若某个新原范数尚未返回，只有此前已完成输入可用于结论。

由同一个剩余权曲线的首一 $Q$ 四次及已付原首一 $\lambda$ 六次、三均值生成和完整恢复，可给不同权对至多 $4d$、五坐标不同点至多 $72d$、完整规范不同点至多 $144d$。这些是不同点上界，不冒称全球 scheme 长度。只有实际 $d=0$ 才排空此 H1 范围；其余情况须继续完整同点原理想，不宣普通 ISP 完成。

## 运行依赖与输出边界

同一临时目录放本源、6226 的 P201 必要前缀源、ef9 的原 Dixon 构造源、0ea9 的原 v 源，以及旧两份历史输入；每个程序源用固定 SHA 核验。内嵌源保持相同1GiB硬限，不提高资源。重建前缀只供新输入，旧独立结论不再次登记。

输出只有实际阶段、次数、固定映射阶、乘回状态、因子次数、SHA、run 与小回执；不保存或传送可重算矩阵、多项式、编码或分片数据。
