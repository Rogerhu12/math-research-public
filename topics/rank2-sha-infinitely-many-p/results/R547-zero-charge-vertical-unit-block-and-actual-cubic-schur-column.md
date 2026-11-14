# R547 — 零新增 charge 的原垂直单位块与保留 cube 的真实单列余项

日期：2026-11-14。**状态：已证明。** 本篇在同一原
\(t^rQH^0(3C)\) 子格内使用
\(F\mathcal EH-2(\mathcal EF)H\)。
它不增加 charge，且在显示深接触窗中给出
\(2\kappa+\chi\) 个真实单位 Smith 因子。

该单位像与整个承载 \(\xi\) 的高 \(\epsilon\) 尾空间相交为零。
再加入原 \(F^2\mathcal H_1\) 后，显示子格中仅剩原 \(F^3\)
一个非单位来源方向，其因子在显示子格内准确为 \(p\)；
全部 forcing 可作同一整 Schur 单列读取。
本篇不把这个显示子格当成整个 \(\mathcal W_D\)，
也不把 \(\xi\) 单项的非零当成完整 Bockstein 非零。

最后准确比较 R545：新的平衡切向像也单独不吸收该尾空间，
但两个单位像之和仍可能通过彼此抵消产生尾项。
这一联合交没有被免费置零。

## 1. 同一原低 ell 目标与真实来源

保 R495、R498、R502、R543、R545 的实际对象：
$$
P^{\rm fact}=d^{-C_D}t^rQF^3\in\mathcal W_D,\qquad
F(0,1)=0,\quad F_Y(0,1)Q(0,1)\ne0,
$$
$$
1\le\ell\le r<h,\qquad
k=2h+r-s,\quad0\le k<\ell,\quad
S=s-r=2h-k,\qquad p=6s-1>83.
\tag{1}
$$
\(C\subset X\) 是同一个十九次吹起后的整因子曲线，
\(\kappa=C^2,\chi=-K_XC\)，
\(\mathcal H_j=H^0(X,\mathcal O_X(jC))\)
仍使用原多项式平凡化及角/次数保持整格。

对没有额外 \(t\) 因子的原三倍来源，
相对 \(J\) 和整个原 \(M\) 的准确高双块长度分别为
$$
\boxed{T_J=s-r,\qquad T_M=s-r-13.}
\tag{2}
$$
原 \(M=c_*U_0m_{13}J\) 全部恢复后才得到第二个长度。
两种目标均由原低 \(\ell\) 使第三高块为零，
而原最初低行、第三块和十三行 carry 并未从整个矩阵中删除。

在已知高像中除去同一个 \(t^rQ/d^{C_D}\) 及原完整单位后，
记目标为
$$
\mathcal A_T=k[[t]][\epsilon]/(t^T,\epsilon^2).
$$
同一 normal 坐标满足
$$
\zeta=\log(Y/\psi),\qquad
\zeta_{\rm phys}=\eta+a\epsilon,\qquad
\operatorname{ord}\eta=h,\qquad
\eta^2=0\bmod t^T,\quad a\in k^\times.
\tag{3}
$$
这里三厚化只用于这个指定高像，
不在 raw \(\bar\Gamma\) 中抹掉 R502 的活 \(\zeta^3\)。

## 2. 整个原 H3 中的垂直列

令
$$
\mathcal E=Y\partial_Y,\qquad e=\mathcal EF,\qquad
\boxed{\mathcal W_F(H)=F\mathcal EH-2eH.}
\tag{4}
$$
所有十九角和次数帽都是逐 charge 的条件，
所以
$$
\mathcal E\mathcal H_j\subset\mathcal H_j\quad(j=1,2).
$$
特别 \(F,e\in\mathcal H_1\)、\(H,\mathcal EH\in\mathcal H_2\)，从而
$$
\boxed{\mathcal W_F(H)\in\mathcal H_3,\qquad
\mathcal V_{\rm vert}(H):=
d^{-C_D}t^rQ\,\mathcal W_F(H)\in\mathcal W_D.}
\tag{5}
$$
这是 R495 已付整个 \(t^rQ\mathcal H_3\) 的子来源，
不增加一个 charge，也不需要 R545 的两 charge 余量。

恒等式
$$
\mathcal W_F(FH_1)=F(F\mathcal EH_1-eH_1),\qquad
\boxed{\mathcal W_F(F^2)=0}
\tag{6}
$$
在整系数上准确成立。

在原整个 \(\Gamma\) 中，若
\(\mathsf A_2\) 是 \(\mathcal H_2\) 的真实评价、
\(\mathcal E_2\) 是相同来源的 charge 对角矩阵，
并记 \(\rho=\operatorname{ev}(d^{-C_D}t^rQ)\)，则
$$
\boxed{
J\mathcal V_{\rm vert}
=\mathsf M_{\rho\,\operatorname{ev}(F)}
 \mathsf A_2\mathcal E_2
-2\mathsf M_{\rho\,\operatorname{ev}(e)}
 \mathsf A_2 .
}
\tag{7}
$$
这个矩阵等式保全部 \(w^s=p\epsilon\)、Gaussian 和高尾，
在模 \(p^2,p^3\) 都成立。
它没有把 \(\mathcal E\) 换成一个不保 carry 的自由 \(\partial_\epsilon\)。
原 \(M\) 仍经完整 \(c_*U_0m_{13}\) 运输；
转置时 (7) 的两项同时保留。

## 3. 真物理核只有 F²

假定相应 (2) 的长度满足
$$
\boxed{T>2\kappa,\qquad h>\kappa.}
\tag{8}
$$

**定理 1。** 在 (8) 下，
$$
\boxed{
\ker(\bar J\,\overline{\mathcal V_{\rm vert}})
\quad\text{或}\quad
\ker(\bar M\,\overline{\mathcal V_{\rm vert}})
=kF^2.
}
\tag{9}
$$
对应的真实整限制有准确
$$
\boxed{R_{\rm vert}=2\kappa+\chi}
\tag{10}
$$
个非零 Smith 因子，全部为单位。

**证明。** 令 \(G=\mathcal W_FH\)。
物理为零给同一个普通值和 Euler 导数
\(G(t,g),(\mathcal EG)(t,g)\) 均消到 \(T\)。
由 (3)，
$$
G|_C=G(t,g)-\eta(\mathcal EG)(t,g)=0\bmod t^T.
$$
但 (4) 在 \(C\) 上准确是
$$
G|_C=-2e\,H|_C .
$$
\(e(P)\ne0\)，所以 \(H|_C\) 有 \(T\) 阶零。
它是 \(N^2=\mathcal O_C(2C)\) 的截面，次数为 \(2\kappa\)；
由 (8) 必为零。因此
$$
H=F H_1,\qquad H_1\in\mathcal H_1.
$$

用 (6)，余下条件是
\(F G_1\) 物理为零，其中
\(G_1=F\mathcal EH_1-eH_1\)。
因 \(F/\zeta\) 是同一个单位，原高双块条件准确为正镜轴
$$
G_1(t,\psi e^{2\eta})=0\bmod t^T.
$$
于是
\[
G_1|_C=-eH_1|_C=0\bmod t^{\min(h,T)}.
\]
(8) 使 \(\min(h,T)>\kappa\)，
而 \(H_1|_C\) 是次数 \(\kappa\) 的截面，故它也为零。
从同一个限制核得 \(H_1=cF\)，证明 (9)；
反向由 (6) 成立。

整提升中 \(F^2\) 是真实且 primitive 的核向量。
\(\operatorname{rank}\mathcal H_2=1+2\kappa+\chi\)，
所以 (9) 的模 \(p\) 秩为 (10)。
整关系给特征零秩的同一上界，故全部非零 Smith 因子都是单位。
同时来源返回也饱和；这个来源结论是由真实模 \(p\) 秩证明，
没有被用作物理饱和的替代。证毕。

本定理不需要 R537 的不可分交数门；
它直接用真实两行、曲线次数和 (8)。
原使用中的 \(f_D<p\)、全部来源整提升和矩阵预算仍保持。

## 4. 与整个 xi 尾空间的实际交为零

在 (3) 的同一目标中，定义
$$
\boxed{\mathcal Z_T=\epsilon\eta\,k[[t]]/(t^T)
=\epsilon t^h k[[t]]/(t^T).}
\tag{11}
$$
其维数是 \(q_T=(T-h)_+\)。
完整单位 \(2ae^2\) 不改变这个子空间。
它恰是 \(F^2\) 乘任意局部低轴函数的目标像。

**定理 2。** 在 (8) 下，
$$
\boxed{
\operatorname{im}(\bar J\,\overline{\mathcal V_{\rm vert}})
\cap\mathcal Z_T=0,
}
\tag{12}
$$
对原 \(M\) 同样成立，使用 (2) 的对应长度和相同单位运输。

**证明。** 假定 \(G=\mathcal W_FH\) 的物理值在 \(\mathcal Z_T\) 中。
其普通值为零，Euler 值至少有 \(h\) 阶。
所以
\(G|_C=G(t,g)-\eta(\mathcal EG)(t,g)\)
在模 \(t^T\) 为零，因为 \(2h\ge S\ge T\)。
仍由 \(-2eH|_C\) 和 (8) 得 \(H=F H_1\)。

再写 \(G=FG_1\)。除同一单位 \(F/\zeta\) 后，
目标仍是纯 \(\epsilon\eta\) 尾。
\(\zeta G_1\) 的 \(\epsilon\) 系数说明
\(G_1|_C+2\eta(\mathcal EG_1)|_C\) 至少有
\(\min(h,T)\) 阶，因此 \(G_1|_C\) 也有这一阶。
由 \(G_1|_C=-eH_1|_C\) 和 (8)，得 \(H_1=cF\)。
于是 \(G=0\)，原尾亦为零。证毕。

这比“垂直块是单位像”更具体：
其整消元不能单独抹掉某个非零 \(\xi\) 尾。
它仍不排除与其他原列相加后发生消去。

## 5. 加原 F²H1 后，接触余核保持为真子商

同一原 \(F^2\mathcal H_1\subset\mathcal H_3\) 的高目标准确为
$$
\operatorname{ev}(F^2H_1)
=2ae^2\eta\epsilon\,(H_1|_C)\pmod{t^T}.
\tag{13}
$$
因此它的像是 \(\mathcal Z_T\) 中的真实接触像
$$
E_{q_T}:\mathcal H_1\longrightarrow k[t]/t^{q_T},
\qquad H_1\longmapsto H_1|_C .
\tag{14}
$$
因为 \(q_T\le h\)，这里也等于同一原轴 \(g\) 的该长度评价，
没有另选接触参数。

由 (12)，准确有单射
$$
\boxed{
\operatorname{coker}E_{q_T}
\simeq
\mathcal Z_T/\operatorname{im}(F^2\mathcal H_1)
\hookrightarrow
\mathcal A_T/
\bigl(\operatorname{im}\mathcal W_F+
      \operatorname{im}(F^2\mathcal H_1)\bigr).
}
\tag{15}
$$
证明是：若一个 \(\mathcal Z_T\) 向量落在右侧两像之和，
减去其中的 \(F^2\mathcal H_1\) 像后仍在 \(\mathcal Z_T\)，
(12) 迫其垂直像部分为零。
(15) 只对显示的实际两族来源成立，
不把它提升为整个原 \(\mathcal W_D\) 的余核单射。

R502 的实际 \(\xi\) 项在同一高框中是
$$
6ae^3\eta\xi\epsilon.
$$
所以 (15) 准确将它识别为
$$
\boxed{[\,3e\xi\,]\in\operatorname{coker}E_{q_T}.}
\tag{16}
$$
对相对 \(J\)，\(q_T=h-k\)；
对原 \(M\)，\(q_T=(h-k-13)_+\)。
这保了原十三行的真实缩短。
\(\xi\) 由原 Hensel/forcing 决定，未被当成可任意规范为零的函数。

(16) 仍只是完整首 Bockstein 的一个项。
R502 的两项 carry、活 \(V_1\) 及低行右逆的全部高尾
必须和它一起通过同一整消元；不能单用 (16) 宣称非零。

## 6. 同预算联合块中，仅剩原 cube 一条非单位方向

再假设
$$
\boxed{q_T=T-h>\kappa.}
\tag{17}
$$
于是 (14) 的核准确为 \(kF\)：
其在 \(C\) 上的次数是 \(\kappa\)，消到 \(q_T>\kappa\) 只能为零；
原限制核正是 \(kF\)。

考虑同一个真实整来源呈示
$$
\boxed{
\mathcal A:\mathcal H_2\oplus\mathcal H_1\to\mathcal W_D,\qquad
(H,K)\longmapsto
d^{-C_D}t^rQ\bigl(\mathcal W_FH+F^2K\bigr).
}
\tag{18}
$$
所有列都在原 \(t^rQ\mathcal H_3\) 中，仍为零新增 charge。

它的多项式来源核准确是
$$
\boxed{\ker\mathcal A=\mathcal O(F^2,0).}
\tag{19}
$$
为见此，若 \(\mathcal W_FH=-F^2K\)，先限制到 \(C\) 得
\(-2eH|_C=0\)，所以 \(H=FH_1\)。
再除一个 \(F\) 并限制到 \(C\)，得
\(-eH_1|_C=0\)，所以 \(H_1=aF\)，
从而 \(\mathcal W_FH=0\)、\(K=0\)。
这个论证在约化和角保持整提升上都成立。
故 (18) 的来源像饱和，且其秩为
$$
1+\frac{5\kappa+3\chi}{2}.
$$

由 (9)、(12)、(17)，物理约化的核恰为
$$
\boxed{k(F^2,0)\oplus k(0,F).}
\tag{20}
$$
第一条是来源本身的零关系；
第二条准确对应原因子化来源
$$
\mathcal A(0,F)=P^{\rm fact}.
$$

**定理 3。** 显示联合子格的原 \(J\) 或原 \(M\) 矩阵，
具有准确
$$
\boxed{R_{\rm joint}=\frac{5\kappa+3\chi}{2}}
\tag{21}
$$
个单位 Smith 因子。除去它们和 (19) 的来源零列后，
仅剩以原 \(P^{\rm fact}\) 为代表的**一个**来源方向。
下面新增第6A节证明，在这个显示同前缀子格内，其因子**准确为 \(p\)**；
不把该结论赋给加入其余原低行列后的完整矩阵。

**整 Schur 读法。** 在 (18) 的来源商格中，
选原 \(F^3\) 为最后一列，其他列给 (20) 的约化补空间。
它们形成 (21) 的单位块。经整行操作并按同一单位来源消去最后一列的上部，
得到
$$
\begin{pmatrix}I_{R_{\rm joint}}&0\\0&b_{\rm cub}\end{pmatrix},
\qquad b_{\rm cub}\in p\,\Gamma_{\rm rem}.
\tag{22}
$$
因为原 cube 的约化为零，所减的单位来源系数均被 \(p\) 整除；
这是同一个首核的真正首次修正，没有改变约化候选。
\(b_{\rm cub}/p\bmod p\) 正是完整首 Bockstein 在此显示子格余核中的类，
后续除 \(p\) 同样保原高精度。

若还有原 \(\mathcal W_D\) 其他列，它们必须经这个相同 Schur 过程加入剩余矩阵。
因此 (22) 不是整个原矩阵只剩一列的声明，
更不是主目标的非零结论。

## 6A. 显示子格的最后 cube 因子准确为 p

本节是原第6节的完整增补，缩小在那里原先保留的“不排更深或为零”范围。
保持 (1)、(8)、(17)，并且只讨论 (18) 的显示同前缀子格。

R502 的完整原首 Bockstein 在第三块中准确为
$$
\boxed{
\beta_J(P^{\rm fact})^{(2)}
=3a\,b_s(t)t^k u(t)^2 V_0(t)\bmod t^\ell,
}
\tag{22a}
$$
其中
$$
b_s=(t/w)^s,\qquad
\eta=t^hu+p\xi,\qquad
V_0=(d^{-C_D}Q)|_C\,e^3 .
$$
\(a,b_s(0),u(0),V_0(0)\) 全为单位，
且 \(0\le k<\ell\)。
所以第三块第 \(k\) 条行是一个真实单位。

反之，整个
$$
d^{-C_D}t^rQ\,\mathcal H_3
$$
的模 \(p\) 相对评价，第三块恒为零：
每一项都有同一个 \(t^r\) 前缀，而 \(r\ge\ell\)。
特别 (18) 的全部垂直列、\(F^2\mathcal H_1\) 列和它们的任何
首次修正，都不能取消 (22a)。
因此 cube 的相对首 Bockstein在这个显示子格的余核中非零。

对整个原 \(M\)，只作合法的完整目标单位逆
\((c_*U_0)^{-1}\)，不逆 \(m_{13}\)。
此时
$$
M(P^{\rm fact})/p
\equiv w^{13}\beta_J(P^{\rm fact})\pmod p.
$$
所有前两块乘 \(w^{13}\) 的越界进位另含一个 \(p\)，
在这个约化中为零。
故 (22a) 的单位准确移到原第三块第 \(13+k\) 条行，
而
$$
13+k<13+\ell
$$
保证它仍可读。
它在 \(w\) 坐标的首系数还乘
\((t/w)(0)^k\)，仍为单位。
同一个显示来源的第三块却因
\(w^{13}t^r\) 前缀而全部为零：
其最小次数至少 \(13+r\ge13+\ell\)。
所以原 \(M\) 在此显示子格中也有同一个非零首 Bockstein。

第6节已证明其余 \(R_{\rm joint}\) 个来源方向都是单位因子。
(22a) 现在严格排除最后一列被 \(p^2\) 整除或为零。
因此两种显示矩阵的完整非零 Smith 因子准确为
$$
\boxed{
\underbrace{1,\ldots,1}_{(5\kappa+3\chi)/2\text{ 个}},
\quad p .
}
\tag{22b}
$$
所有目标自由行及 (19) 的来源零关系按原矩阵保留。

这个结论的范围尤其重要：
R498 的实际低行右逆使用不带共同 \(t^r\) 前缀的原列，
它可以取消 (22a)，随后产生 R502 的完整 \(\ell_0,\ell_1\) 高尾。
本节的第三块行并不杀这些原低列，
因而不是整个原 \(\mathcal W_D\) 的真左行。
一旦加回它们，仍须判断同一个低行消元后的完整 forcing，
不能把 (22b) 宣称为原全矩阵的第二障碍非零。

## 7. 与 R545 平衡切向像的准确交界

R545 的实际返回多一个 \(t\) 因子。
在本篇公共高框中，若其值属于 \(\mathcal Z_T\)，
剥该 \(t\) 及完整单位后是长度 \(T-1\) 的纯
\(\epsilon t^{h-1}\) 尾。

若
$$
\boxed{T-1>2\kappa,\qquad h-1>\kappa,}
\tag{23}
$$
则准确有
$$
\boxed{\operatorname{im}\overline{\mathcal T_c}\cap\mathcal Z_T=0.}
\tag{24}
$$
这里 R545 的两个 charge 成本仍必须已付。

证明使用 R545 的同一个 \(F_c,H_c,\mathscr D_c\)。
纯尾使
\((\mathcal V_{F_c}H_c)|_C\)
至少消到
\(\min(T-1,2h-1)>2\kappa\)。
所以 \(H_c|_C\) 是常数。
剥这个真实常数后写成 \(F_cH_{1,c}\)；
镜轴的纯尾又使
\((\mathcal V_{F_c}H_{1,c})|_C\)
至少消到 \(\min(T-1,h-1)>\kappa\)。
于是 \(H_{1,c}|_C\) 也为常数，
原返回为零，证明 (24)。
所有系数在 \(P\) 的导数读取仍低于 \(p\)。

(12)、(24) 分别证明两种实际单位像不单独吸收这个尾。
它们**不证明**
$$
(\operatorname{im}\mathcal W_F+
 \operatorname{im}\mathcal T_c)\cap\mathcal Z_T=0.
$$
两族来源之间仍可能有不落入尾空间的分量互相抵消，
留下一个非零尾。
其准确交由同一原目标中的
$$
\mathcal W_F(H)+
\mathfrak m_2\mathcal L_c(K)\in\mathcal Z_T
$$
读取，并保全部前缀与预算。
没有将两个分别可消的单位块数目相加后冒称联合秩。

因此，与 R545 的剩余实质问题已准确集中为这个真实交，
以及它与 (16)、完整 carry 和原其余列的联合。
本篇 (21) 的联合单位数只来自已严格证明交为零的
垂直像与 \(F^2\mathcal H_1\)。

## 8. 满主阶低 ell 窗确实适用

对已经存在且满足 R545(24) 的实际候选，
$$
\kappa=\frac{47}{12}b^2+O(b),\quad
h=\frac{141}{32}b^2+O(b),\quad
T_M=\frac{141}{16}b^2+O(b).
$$
于是 (8)、(17)、(23) 都最终成立。
特别
$$
T_M-h-\kappa=\frac{47}{96}b^2+O(b)>0.
$$
本篇不再增加任何来源次数，就有
$$
R_{\rm vert}=\frac{47}{6}b^2+O(b),\qquad
\boxed{R_{\rm joint}=\frac{235}{24}b^2+O(b)}
\tag{25}
$$
个相应真实单位因子。
最后一个数约为显示三倍来源主维数 \(9\kappa/2\) 的五分之九，
余下的原来源方向与目标行并未消失。

若需要同时使用 R545 列，另付其固定两个 charge，
并按同一实际矩阵检第7节的交。
两个返回从未被赋予原 \(S,T,U\) 的额外中央零。

## 9. 原完整任务的边界

本篇提供一块无需新增 charge 的整可消来源，
并让原 cube 在显示联合格中的全部非单位信息集中到 (22)。
它还证明 \(\xi\) 接触类在这个消元中有 (15) 的真实单射，
所以不能以“新增大量单位列”为由直接令该项消失。

完整相对首 Bockstein仍是 R502 的四项剩余式；
原 \(M\) 的实际 \(13/26\) 行和 R479/R481 的同一修正第三精度
继续按 (2)、(7)、(22) 运输。
原其余 \(\mathcal W_D\) 列及 R524 两连接必须接到剩余矩阵，
才可判断真实 forcing 是否被吸收。

跨素数中央非零和 R418 全部饱和前缀的严格斜率预算仍未证明。
本篇的实际单位块、接触子商和单列余项没有被当成这些缺项的替代。
