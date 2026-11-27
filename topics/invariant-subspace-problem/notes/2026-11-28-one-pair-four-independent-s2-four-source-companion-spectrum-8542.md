# 一对等权加四独立权：原完整四维低来源 S2 的谱输入

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

状态：以下同源形式、全部物理度量及碰撞延拓已证明；四个谱系数的全域正性尚待唯一首次执行。
它不重放任何 S1 正性门，也不再使用一般六位已经失败的平方迹充分条件。

唯一新源为
[完整四维低来源 S2](2026-11-28-one-pair-four-independent-s2-four-source-companion-spectrum-8542.py)，
Git blob e527e3836b5266104dee584dc938044555fd8110。
固定内层 180 秒、4 GiB，只打印普通小摘要，不输出扩展参数或编码数据。

## 1. 原范围和实际目标

继续取六位权
$$
(\sqrt{x_1},\sqrt{x_2},\sqrt{x_3},\sqrt{x_4},1,1),\qquad x_i>0.
$$
[完整九维 S1](../results/R271-appendix-one-pair-four-independent-full-nine-dimensional-strengthened-s1.md)
已支付原上来源的 S1；本输入只处理另一个原联合条件。

用 [R275 §4](../results/R275-appendix-first-edge-three-block-equivalence-and-parameter-free-sos.md)
的真实记号，旧上来源 $U=K_2$、下来源 $L=K_1$，
$C_1=G_1^{-1}$，并令
$$
A_{\rm op}=\frac12(C_1B^*L_2+B^*L_2L_3^{-1}L_2).
$$
新目标是完整原 S2
$$
\boxed{
I_L-A_{\rm op}^*G_1A_{\rm op}-L_1L_2^{-1}L_1>0.
}
\tag{1}
$$
这里不是单独证明一个列费用或先丢掉任一 mixed term。

只交换等权 pair 的约化依旧给上来源 $9=6+3$、下来源 $5=4+1$。
反对称 singlet 的上出生变为原四位出生一，下来源是真空；
[R288 任意权出生一 S2](../results/R288-appendix-birth-one-s2-contraction-and-weighted-coordinate-lift.md)
已给整个该部分费用至多 $2/3$。
因此本次唯一未付目标是 pair 对称部分的整个四维低来源。
全来源中的各块正交，完整物理逆和原桥同时约化，不丢重数。

## 2. 完整原物理 Gram 与上精度

全部源、叶矩坐标和实际层取自
[三叶原来源稿](2026-11-28-one-pair-four-independent-s1-three-leaf-companion-schur-8542.md)，
但本次不形成其 S1 矩阵。

具体说，低源
$$
E_1=(X_i-J)_{i=1}^4
$$
以及上源
$$
E_2=((X_i-J)(X_j-J))_{i<j}
$$
张满同一个四维、六维 pair 对称 primitive 空间。
原系数物理度量仍是
$$
\|g\|^2=\sum_I\frac{|g_I|^2}
{\binom2{j_I}\prod_{\nu=1}^4x_\nu^{i_\nu}}.
$$
记全部二次型矩阵
$$
U_1=E_1^{\mathsf t}W_1E_1,\qquad
U_0=E_2^{\mathsf t}W_2E_2,
$$
$$
\Lambda_j=E_1^{\mathsf t}\mathcal F_{1,j}^{-1}E_1,\quad j=1,2,3.
\tag{2}
$$
每个 $\mathcal F_{1,j}$ 都在整个五维物理一孔层取逆；
然后才压到四个 primitive 源。
特别新增的 $\Lambda_1$ 也不采用压缩逆代替完整逆。

令 $K_B$ 为原 cubic 桥 $B$ 的四行六列来源矩阵。
使用原占据形式 $\widehat H$ 及 R275 的完整两带身份
$H_0=C_1+B^*L_2B$，得
$$
\boxed{
\widehat C_1=\widehat H-K_B^{\mathsf t}\Lambda_2K_B>0.
}
\tag{3}
$$
(3) 是原完整上精度的二次型矩阵。上来源的算子及 Gram 形式分别为
$$
(C_1)_{\rm coord}=U_0^{-1}\widehat C_1,\qquad
(G_1)_{\rm coord}=\widehat C_1^{-1}U_0,\qquad
\widehat G_1=U_0\widehat C_1^{-1}U_0.
\tag{4}
$$
因此源码对整个六维 $\widehat C_1$ 取逆。
这是由已付两带等式识别真正完整 MP 精度，不是先把某个物理 Gram
压到试探六列再未经证明地取逆。

两组 source 的 primitive 身份、原删除和两次 cubic 桥都由原完整层乘回。
全部实际物理层维数仍是 $1,5,11,14,11,5,1$。

## 3. 同一低来源上的四项费用

置
$$
X=\Lambda_2\Lambda_3^{-1}\Lambda_2.
$$
注意 $X$ 是 bilinear form，而不是省略来源度量后的原物理算子。
原伴随方向是
$$
(B^*)_{\rm coord}=U_0^{-1}K_B^{\mathsf t}U_1,\qquad
(L_j)_{\rm coord}=U_1^{-1}\Lambda_j.
$$
代入 $A_{\rm op}$ 得它的上对偶来源矩阵
$$
\widehat A=U_0(A_{\rm op})_{\rm coord}
=\frac12\left(
\widehat C_1U_0^{-1}K_B^{\mathsf t}\Lambda_2+K_B^{\mathsf t}X
\right).
\tag{5}
$$
由 (4)，其完整费用恰为
$$
\widehat K
=\widehat A^{\mathsf t}\widehat C_1^{-1}\widehat A.
\tag{6}
$$
为避免把大的原有理列不必要地平方，源码在同一式中使用准确展开：
$$
K_{bb}=K_BU_0^{-1}K_B^{\mathsf t},
$$
$$
K_{bc}=K_BU_0^{-1}\widehat C_1U_0^{-1}K_B^{\mathsf t},
\qquad
K_{bg}=K_B\widehat C_1^{-1}K_B^{\mathsf t},
$$
$$
\boxed{
4\widehat K
=\Lambda_2K_{bc}\Lambda_2
+\Lambda_2K_{bb}X+XK_{bb}\Lambda_2
+XK_{bg}X.
}
\tag{7}
$$
这是 (6) 的整个平方展开，两个 cross 都在。
所有中间 $K$ 是双对偶形式，故 (7) 不应另外插入或删除一个 $U_1$。

低来源原费用的二次型恰是
$$
\widehat{L_1L_2^{-1}L_1}=\Lambda_1\Lambda_2^{-1}\Lambda_1.
$$
所以 (1) 的原四维形式就是
$$
\boxed{
Z=U_1-\widehat K-\Lambda_1\Lambda_2^{-1}\Lambda_1.
}
\tag{8}
$$
源码完整形成 (8)，核对原对称性，并以 $U_1$ 为实际参考度量。
这不是 $\operatorname{Tr}(\widehat K^2)$，也不是 companion 的 Frobenius 范数。

## 4. 四个原谱系数和重复权

将最大单组权平方记为 $a=x_1$，其余三个叶权的初等和记为 $s,p,q$。
在互异叶权上，旧物理来源到矩坐标的变换为
$$
Q=\operatorname{diag}(1,V),\qquad V_{ik}=z_i^k.
$$
原低形式和度量同时变化：
$$
\widetilde Z=Q^{\mathsf t}ZQ,\qquad
\widetilde U_1=Q^{\mathsf t}U_1Q.
$$
新目标严格定义在原连续四维空间上：
$$
\boxed{
\frac{\det(tU_1+Z)}{\det U_1}
=t^4+c_1t^3+c_2t^2+c_3t+c_4.
}
\tag{9}
$$
在矩坐标中计算 $\widetilde U_1^{-1}\widetilde Z$ 的四个初等谱系数，
等于 (9)，因为分子、分母中的 $(\det Q)^2=(\det V)^2$ 完整相消。

原 $U_1,U_0,\widehat C_1,\Lambda_2,\Lambda_3$ 均严格正，
且 (2) 的全部原完整物理 Gram 严格正。
因此 (8)–(9) 在正权碰撞处连续、没有原正域极点。
对三个叶权的六个置换取原正分母的乘积，
就得到在整个原域仍严格正的对称共同分母；
故在 $a,s,p,q$ 中约简后的原系数分母也无零。
不能把退化的 Hankel 或 $V$ 当成重复权处的真基底。

五个闭权序仍用 $v_0=1,v_1=1+A,\ldots,v_4=1+A+B+C+D$，
$A,B,C,D\ge0$，并依 pair 的五个位置取 $\tau=v_k$。
其余四组降序为 $s_1,s_2,s_3,s_4$，
准确代换
$$
a=s_1/\tau,\quad
s=(s_2+s_3+s_4)/\tau,\quad
p=(s_2s_3+s_2s_4+s_3s_4)/\tau^2,\quad
q=s_2s_3s_4/\tau^3.
$$
因此同向分子须以权 $(1,1,2,3)$ 齐次化，不能改用普通总次数。
逐域只用精确系数非负及固定的半径二、至多 32 项平方来源；
完整返回和严格正常数是必需部分。
第一个未付系数或域即停止并准确报 INCONCLUSIVE，不将后面系数当作已算。

## 5. 若唯一首次输入完整成功，准确能得到什么

因为原 $U_1>0$、$Z=Z^{\mathsf t}$，
$U_1^{-1}Z$ 的四个特征值都为实数。
若 (9) 四个系数在全部闭权序域严格正，
则其多项式在 $t\ge0$ 严格正，排除任一非正原广义特征值；
这才给整个四维 $Z>0$，并经已付 singlet 给整个五维原 S2。

结合已经完整证明的同模型九维 S1，
以及[已付六独立正权出生一的内部第二边](../results/R271-appendix-six-site-internal-half-complete-ordered-difference-certificate.md)，
R275 才能对新增任意正权的一位递推给真实七位出生二首边。
倒数权对偶保持“一对等权加五个任意独立权”的族，
故也可支付其合法末边。此条件收尾需等待本输入四系数完整成功。

任何部分返回、零抽样、单系数或单域均不支付全 S2。
本文不预先声明新增七位结论、统一全出生常数或原 $N=M$。
