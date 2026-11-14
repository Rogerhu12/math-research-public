# R103 后续：两个已用局部处的辛类型没有再提供排除

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明的边界。** 对 R99–R103 的辅助曲线同余，$2$ 与 $3$ 处确实固定了唯一参考扭曲，但这两个地方允许两种辛类型。不能再将其与原 $E[p]\simeq A[p]$ 的辛类型相比较，制造一个尚无共同配对接口的矛盾。这里不讨论 $p$ 处或新增乘法素数处的类型。

沿用
$$
K=\mathbb Q(\sqrt3),\qquad
B_0:y^2=x^3+4x^2+(2+\sqrt3)x,\qquad d\in\{\pm1,\pm2\}.
$$

## 1. $K_{\mathfrak p_2}$ 上的完整模三像为 $C_8$

先取 $d=\delta\in\{1,2\}$。[R103](../results/R103-unique-twist-from-complete-dyadic-models.md) 显式构造了
$$
L_\delta=K(P_\delta),\qquad P_\delta\in B_0^{(\delta)}[3]\setminus\{0\},
$$
并核验唯一二进完备化 $\mathscr L_\delta/K_{\mathfrak p_2}$ 的次数为八、分歧指数为四、剩余次数为二，且参考曲线在 $\mathscr L_\delta$ 好约化。

令 $G=G_{K_{\mathfrak p_2}}$、$I$ 为惯性群，$V=B_0^{(\delta)}[3]$。因为 $\mathscr L_\delta$ 是点域，
$$G_{\mathscr L_\delta}=\operatorname{Stab}_G(P_\delta).$$
好约化说明 $I\cap G_{\mathscr L_\delta}$ 对整个 $V$ 平凡；反之，$\ker(I\to\operatorname{GL}(V))$ 必固定 $P_\delta$。故
$$
\ker(I\to\operatorname{GL}(V))=I\cap G_{\mathscr L_\delta},
\qquad |\overline\rho_3(I)|=4.
$$
惯性行列式平凡，所以此阶四子群在 $\operatorname{SL}_2(\mathbb F_3)$ 中。该群只有一个阶二元素 $-I$，故惯性为循环 $C_4$。

将 $V$ 识别为 $\mathbb F_9$，这个 $C_4$ 恰为范数一群。其中心化子是 $\mathbb F_9^\times=C_8$，正规化子为
$$\mathbb F_9^\times\rtimes\langle x\mapsto x^3\rangle.$$
设 $M$ 是算术 Frobenius 的像，则 $\det M=2=-1\in\mathbb F_3^\times$。完整局部像由惯性和 $M$ 生成。

若 $M$ 不在中心化子中，可写 $M(x)=c x^3$。其行列式为 $-N(c)$，故 $N(c)=1$，并有 $M^2=1$。此时整个像为阶八的二面体群，保持非零向量范数的两个值 $1,-1$；它在 $V\setminus\{0\}$ 上的每个轨道只有四元。这与
$$[K_{\mathfrak p_2}(P_\delta):K_{\mathfrak p_2}]=8$$
矛盾。

所以 $M$ 必在中心化子中，而且其范数为 $-1$，从而阶为八。完整模三局部像就是循环 $C_8$。

对 $d=-\delta$，扭曲角色在模三矩阵上只乘标量 $\pm1$，原像中的 $-I$ 已属于惯性 $C_4$。因此惯性与 Frobenius 的中心化关系保持；同样得到循环 $C_8$ 的局部像。

## 2. 所有奇特征的局部表示都有两种辛自同构

参考曲线在点域好约化，故特征零有限惯性像的阶也为四。其模三约化忠实。第 1 节说明 Frobenius 与惯性的交换子模三平凡；交换子本身属于惯性，所以它在特征零已经平凡。

因此，对任意 $p>3$，完整局部 $G_{K_{\mathfrak p_2}}$ 像都中心化一个满足
$$J^2=-I$$
的阶四惯性元。若 $p\equiv3\pmod4$，其中心化子为
$$\mathbb F_{p^2}^{\times},$$
行列式为满射的域范数；若 $p\equiv1\pmod4$，其中心化子为分裂环面 $\mathbb F_p^\times\times\mathbb F_p^\times$，行列式同样满射。因为完整局部像已在该交换环面内，这个环面的每个元素都是 Galois 自同构。

二维 Weil 配对的倍率正是线性自同构的行列式。故总存在一个平方行列式和一个非平方行列式的局部 Galois 自同构。只要
$$B(a,h)[p]\simeq B_0^{(d)}[p]$$
在这个局部域成立，任一局部同构与上述自同构复合，就分别得到辛型与反辛型同构。

这不意味着这些自同构能够延拓到全局。结论仅为：这个地方无法判定全局同构的辛类型，因而不能在 R103 的惯性域选择之后再次添加一个二进辛排除。

## 3. $3$ 处也没有辛限制

在 $\mathfrak p_3=(\sqrt3)$，四条参考均好约化，Frobenius 迹为 $\pm2$、行列式为 $3$。对 $p>37$，特征多项式的判别式
$$4-12=-8$$
模 $p$ 非零。表示不分歧，其中心化子因此是一个分裂或非分裂二维环面，行列式仍满射。所以这里也允许两种辛类型。

$3$ 处的实际整数迹仍严格给出 R103 的 $d\equiv a\pmod3$；本节只说明该条件成立后，Weil 配对不再提供一个独立符号条件。

## 4. 保留的全局接口

原 $E/A$ 与辅助 $B/B_0^{(d)}$ 是不同的模 $p$ 同构问题。目前没有一个已证明的 $p$ 挠点同态，将两对曲线的 Weil 配对按同一倍率联系起来。即使两个问题分别有唯一的全局辛类型，也不能直接要求这两个类型相同。

新增乘法素数处或 $p$ 处仍可能给辅助同余的非冗余条件，需要对辅助曲线本身计算；本笔记没有证明所有局部条件均冗余。尤其当剩余 Frobenius 是非平凡幺幂元时，其中心化子行列式可能只有平方，不能把本笔记的环面论证直接搬过去。

