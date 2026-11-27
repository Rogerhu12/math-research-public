# R271 附录：一对等权加四独立权的原 S2 总迹缺陷严格正

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

**状态：以下同源总迹结论已证明；完整 S2 未证明。**
新原四维谱输入的唯一首次运行在 180 秒内完成全部物理来源和第一个谱系数的五域证书，
随后被 SIGALRM 终止；第二个系数没有返回，第三、第四个未到。
本稿不把迹正提升为矩阵正，也不重开这个资源门。

## 1. 真实同源结论

沿用[完整原四维来源稿](../notes/2026-11-28-one-pair-four-independent-s2-four-source-companion-spectrum-8542.md)：
六个正权为
$$
(\sqrt{x_1},\sqrt{x_2},\sqrt{x_3},\sqrt{x_4},1,1).
$$
原上、下 primitive 来源维数为 $9,5$；
等权 pair 的对称部分维数为 $6,4$，singlet 部分维数为 $3,1$。
在原四维对称低来源上，记
$$
\mathsf C=
A_{\rm op}^*G_1A_{\rm op}+L_1L_2^{-1}L_1\ge0,
$$
$$
A_{\rm op}=\frac12(C_1B^*L_2+B^*L_2L_3^{-1}L_2).
$$
本次严格证明
$$
\boxed{\operatorname{Tr}_{L_{\rm sym}}(I-\mathsf C)>0,
\qquad
\operatorname{Tr}_{L_{\rm sym}}\mathsf C<4.}
\tag{1}
$$
这是真正原物理算子迹。
不是非正交 companion 矩阵的 Frobenius 范数。

旧 [R288 出生一 S2](R288-appendix-birth-one-s2-contraction-and-weighted-coordinate-lift.md)
给 singlet 的整个一维费用至多 $2/3$。
正交直和因此还给完整原五维低来源的准确预算
$$
\boxed{
\operatorname{Tr}_{L}\mathsf C<\frac{14}{3},\qquad
\operatorname{Tr}_{L}(I-\mathsf C)>\frac13,\qquad
\|\mathsf C\|<\frac{14}{3}.
}
\tag{2}
$$
最后一式只用 $\mathsf C\ge0$ 时范数不超过迹。
(1)–(2) 不给 $\mathsf C<I$。

## 2. 原形式及不丢度量的第一谱系数

全部低 Gram 先在完整五维物理层取逆后压到同一个四维源：
$$
\Lambda_j=E_1^{\mathsf t}\mathcal F_{1,j}^{-1}E_1,\quad j=1,2,3.
$$
记原源度量为 $U_0,U_1$，原完整上精度形式
$$
\widehat C_1=\widehat H-K_B^{\mathsf t}\Lambda_2K_B>0,
\qquad X=\Lambda_2\Lambda_3^{-1}\Lambda_2.
$$
原来源稿证明
$$
K_{bb}=K_BU_0^{-1}K_B^{\mathsf t},\quad
K_{bc}=K_BU_0^{-1}\widehat C_1U_0^{-1}K_B^{\mathsf t},\quad
K_{bg}=K_B\widehat C_1^{-1}K_B^{\mathsf t},
$$
$$
4\widehat K=
\Lambda_2K_{bc}\Lambda_2+\Lambda_2K_{bb}X
+XK_{bb}\Lambda_2+XK_{bg}X,
$$
$$
Z=U_1-\widehat K-\Lambda_1\Lambda_2^{-1}\Lambda_1.
\tag{3}
$$
两个 cross、完整六维上精度逆和全部原低来源都保留。
于是
$$
c_1=\operatorname{tr}(U_1^{-1}Z)
=\operatorname{Tr}_{L_{\rm sym}}(I-\mathsf C).
\tag{4}
$$
源码已经形成整个 (3)，不是若干独立单列费用之和。

三个叶权互异时使用 $a=x_1$ 与叶初等和 $s,p,q$。
原低来源的矩坐标变换是 $\operatorname{diag}(1,V)$。
$Z,U_1$ 同时作这一真同余，故
$\det(tU_1+Z)/\det U_1$ 及其 $c_1$ 不变。
重复权处通过原连续正物理 Gram 和对称正分母延拓，
不把退化的 Hankel 或 Vandermonde 当作原基底。

## 3. 唯一实际输入及五个严格证书

唯一源为
[原四维完整 S2 谱源码](../notes/2026-11-28-one-pair-four-independent-s2-four-source-companion-spectrum-8542.py)，
Git blob e527e3836b5266104dee584dc938044555fd8110。
实际 run 46081827069 / job 140782334467，
内层 180.029965556 秒、最高 660384 KiB、退出码 $-14$（SIGALRM）。
[小回执](../notes/2026-11-28-one-pair-four-independent-s2-trace-first-boundary-receipt-8542.json)
保留原阶段、哈希及资源边界，不保存扩展数据。

完成的数学阶段是：

| 阶段 | 实际秒数 |
|---|---:|
| 全原上、下精度 | 4.121822085 |
| 三块完整上来源消去 | 4.573828557 |
| 含全部 cross 的原四维 $Z$ | 8.640093531 |
| 原相对算子 $U_1^{-1}Z$ | 11.712360143 |
| 第一个原谱系数 | 12.000769927 |
| $c_1$ 的五个闭域全部严格正 | 125.590764081 |

$c_1$ 的约简分子普通次数 $38$，
权 $(1,1,2,3)$ 的次数 $61$，有 $37777$ 项；
分母有 $35605$ 项，
在全等正权 $(a,s,p,q)=(1,3,3,1)$ 的同向值为
$24073471210291200000000$。
约简分子 SHA256 为
450220f28f6c05cfc0b295211cff219c8d18a70327fd13a7ea5adb352b195113。
分母的全域非零来自原连续正 Gram 的同向正分母论证，
并非只凭全等点的一个取值。

沿用完整原输入的五个闭权序和正确的加权齐次代换，
每个域的分子都没有负系数，而且有同一个严格正常数
$$
60183678025728000000000.
$$
全部五个域实际返回：

| pair 位置 | 项数 | 负系数数 | 平方消项数 |
|---:|---:|---:|---:|
| 0 | 476790 | 0 | 0 |
| 1 | 476790 | 0 | 0 |
| 2 | 511566 | 0 | 0 |
| 3 | 562166 | 0 | 0 |
| 4 | 669116 | 0 | 0 |

每个域均完成全多项式返回并保留严格正常数，
所以 $c_1>0$ 覆盖所有正权和所有碰撞。
这证明 (1)，继而由正交 singlet 预算证明 (2)。

## 4. 准确未付范围与冻结的门

本次未返回 $c_2$ 的原有理参数或任一正性证书；
$c_3,c_4$ 尚未进入。
因此完整四维 $Z>0$、原全五维 S2、
以及与已付 S1 和旧内部 half 相接的七位首末结论均未支付。

严格正的总迹可以与若干负特征值同时存在，
故不得用 (1) 替换这些尚缺系数或新的真实分块估计。
旧全四维谱门在原资源界冻结；
后续改变实际来源，例如头源与三叶共同 Schur，必须另给完整映射，
不能仅跳过本次已经完成的 $c_1$ 后重跑原 $c_2$ 门。

原 $W$ 的实际来源费用及 $N=M$ 仍开放。
