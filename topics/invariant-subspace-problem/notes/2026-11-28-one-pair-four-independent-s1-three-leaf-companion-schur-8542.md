# 一对等权加四独立权：剩余原三维 Schur 的三根矩坐标与谱系数新输入

日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

状态：本文完整证明新的实际坐标、原 Schur 谱身份和碰撞权延拓。
三个原谱系数的全域正性尚待唯一首次执行。
本稿不重跑原第四主子式资源门，也不宣布完整 S1 已证。

唯一源为
[三根矩坐标中的原剩余 Schur](2026-11-28-one-pair-four-independent-s1-three-leaf-companion-schur-8542.py)，
Git blob 7ed6dd024e44427cc3b117f39e81737342797b0b。
内层固定 180 秒、4 GiB，只输出小的普通摘要，不保存扩展参数或编码数据。

## 1. 新目标始终定义在原连续三维空间

记最大单组平方权为 $a=x_1$，另外三个为
$z_1=x_2,z_2=x_3,z_3=x_4$；容量二的组 $J$ 仍为平方权 $1$。
原六维来源分成
$$
S_i=(X_1-J)(X_i-J),\qquad
Q_i=(X_j-J)(X_k-J),\qquad \{i,j,k\}=\{2,3,4\}.
\tag{1}
$$
$Q_i$ 用缺失的叶指标标记，因此与原后三列只差一个固定排列。

[已付共同因子定理](../results/R271-appendix-one-pair-four-independent-common-factor-three-source-s1-block.md)
给原 S1 矩阵分块
$$
\mathcal E_{\rm orig}=
\begin{pmatrix}A&C\\C^{\mathsf t}&D\end{pmatrix},
\qquad A>0
\tag{2}
$$
在全部原有序正权域成立。
令 $G$ 是三列 $Q_i$ 的原物理 Gram，故 $G>0$。
新目标是原连续形式
$$
\mathcal S=D-C^{\mathsf t}A^{-1}C,\qquad
\boxed{
\frac{\det(tG+\mathcal S)}{\det G}
=t^3+c_1t^2+c_2t+c_3.
}
\tag{3}
$$
不将 (3) 定义成重权处退化的矩 Hankel 表示。

本次针对 $c_1,c_2,c_3$，而非原 $\Delta_4,\Delta_5,\Delta_6$ 的连续消元。
已付 $A>0$ 和前三主子式均不再次作正性测试。

## 2. 三个互异叶权上的完整矩坐标

先取互异正 $z_i$，置
$$
s=z_1+z_2+z_3,\quad p=z_1z_2+z_1z_3+z_2z_3,\quad q=z_1z_2z_3,
$$
$$
V_{ik}=z_i^k\quad(0\le k\le2),\qquad
T=\begin{pmatrix}0&0&q\\1&0&-p\\0&1&s\end{pmatrix},
\qquad VT=\operatorname{diag}(z_i)V.
\tag{4}
$$
令
$$
v^{\mathsf t}=(3,s,s^2-2p),\qquad e=(1,0,0)^{\mathsf t},
\qquad P=ev^{\mathsf t}-I_3.
$$
写 $m_k=\sum_i z_i^k$，其中
$$
m_{-1}=p/q,\quad m_0=3,\quad m_1=s,\quad m_2=s^2-2p,
$$
$$
m_k=sm_{k-1}-pm_{k-2}+qm_{k-3}\quad(k\ge3).
$$
定义 $H_\ell=(m_{i+j+\ell})_{0\le i,j\le2}$。

叶一孔系数以 $V\xi$ 表示。
叶二孔系数按缺失指标以 $V\eta$ 表示。
叶零孔、三孔仍是标量。
因此四个叶层的**真实系数范数矩阵**依次是
$$
W^{\rm leaf}_0=1,\qquad W^{\rm leaf}_1=H_{-1},\qquad
W^{\rm leaf}_2=H_1/q,\qquad W^{\rm leaf}_3=1/q.
\tag{5}
$$
二孔式来自 $1/(z_jz_k)=z_i/q$，不是普通欧氏系数范数。

每个完整物理层由 $(\epsilon,j,l)$ 标记：
头占据 $\epsilon=0,1$，pair 占据 $j=0,1,2$，
叶占据 $l=0,1,2,3$，且 $\epsilon+j+l=r$。
该块度量是
$$
W_{(\epsilon,j,l)}
=\frac{a^{-\epsilon}}{\binom2j}W_l^{\rm leaf}.
\tag{6}
$$
全层维数准确为 $1,5,11,14,11,5,1$。
本文保全部这些原物理层，没有把高层限制为某个试探源。

## 3. 原删除、cubic 桥和全部实际逆

在叶层 $l\to l-1$，原删除的三块准确为
$$
d^{\rm leaf}_1=v^{\mathsf t},\qquad
d^{\rm leaf}_2=P,\qquad d^{\rm leaf}_3=e.
\tag{7}
$$
第二式是三点补集 incidence：
输出第 $i$ 项等于除第 $i$ 项外全部输入之和。

原 cubic 删除的三块准确为
$$
C^{\rm leaf}_1=v^{\mathsf t}T,\quad
C^{\rm leaf}_2=sP-TP-PT,\quad
C^{\rm leaf}_3=Te.
\tag{8}
$$
例如二孔输入缺失 $k$、输出占据 $i\ne k$ 时，
被删除的第三个叶权为 $s-z_i-z_k$，正好给 (8) 的中式。
头上的 $d,C$ 系数分别为 $1,a$，
pair 的两者系数都为 $j$。
这些块完整确定真实下降矩阵 $D_r:\mathcal H_r\to\mathcal H_{r-1}$。

若
$$
L_{j,r}=\frac{D_{r+1}\cdots D_{r+j}}{j!},
$$
则实际最小逆的完整源形式由
$$
\mathcal F_{j,r}=L_{j,r}W_{r+j}^{-1}L_{j,r}^{\mathsf t}
\tag{9}
$$
给出；对源列 $E$ 的最小范数平方是
$E^{\mathsf t}\mathcal F_{j,r}^{-1}E$。
这是在全部高层最小化所得，不是先压缩后取逆。
一般完整 creation Gram 的原源形式是
$$
E^{\mathsf t}W_r\mathcal F_{j,r}W_rE.
\tag{10}
$$
(9)–(10) 保留了两个物理伴随所需的全部度量。

低来源坐标是一个头系数和三个叶矩系数：
头块为 $\xi_0$，叶块为 $V\xi$，pair 块为 $-\xi_0-v^{\mathsf t}\xi$。
上来源 (1) 的坐标为 $(x,y)\in\mathbb C^3\oplus\mathbb C^3$。
在五种二孔块中的系数分别为
$$
\begin{array}{c|c}
\text{块}&\text{系数}\\ \hline
\text{头+叶}&x\\
\text{两叶，按缺失指标}&y\\
\text{pair+叶}&-x-Py\\
\text{头+pair}&-v^{\mathsf t}x\\
\text{pair两孔}&v^{\mathsf t}(x+y).
\end{array}
\tag{11}
$$
由 (7) 可直接核验两组源均 primitive，维数分别为 $4,6$。

记 $w^{\mathsf t}=v^{\mathsf t}(T-I)$。
原 cubic 桥的完整 $4\times6$ 坐标是
$$
K_B=
\begin{pmatrix}
w^{\mathsf t}&0\\
(a-1)I&(s-1)P-TP-PT
\end{pmatrix},
\qquad
K_Y=(a-1,\ w^{\mathsf t})K_B.
\tag{12}
$$
源码从 (7)–(11) 的完整物理矩阵实际乘回两次桥，
同时核验两组来源的原删除核身份。

源用 (9) 在整个五维低物理层取第二、第三阶逆，
再压到完整四维低来源。
上来源仍取完整六维物理度量 $U_0=E_2^{\mathsf t}W_2E_2$。
原第四阶真空量准确为
$$
e_4=as+(2a+1)p+(a+2)q,
$$
源码也用整个第四物理层的 (9) 乘回它。

最后按原 R288 三塔式形成
$$
\widetilde{\mathcal E}
=\widehat H U_0^{-1}\widehat H-\widehat F_2
-(K_B^{\mathsf t}\Lambda_2K_B)U_0^{-1}(K_B^{\mathsf t}\Lambda_2K_B)
+2K_B^{\mathsf t}\Lambda_2\Lambda_3^{-1}\Lambda_2K_B
+\frac{K_Y^{\mathsf t}K_Y}{4e_4}.
\tag{13}
$$
$\widehat H$ 使用真实占据乘法：
叶各层为 $0,T,sI-T,s$，头为 $\epsilon a$，pair 为 $j$，
故总 $H=(a+s+2)I-2W_{\rm occ}$。
(10) 给 $\widehat F_2$。
至此保了所有原 cross 和逆序，不是另一套 Euclidean Schur 模型。

## 4. 真实剩余谱及 Vandermonde 的完整消去

在互异叶域上，(11) 对源两块都是同一个 $V$ 变换，因此
$$
\widetilde{\mathcal E}
=\operatorname{diag}(V,V)^{\mathsf t}
\mathcal E_{\rm orig}\operatorname{diag}(V,V).
$$
从而
$$
\widetilde{\mathcal S}=V^{\mathsf t}\mathcal S V,\qquad
\widetilde G=V^{\mathsf t}GV.
$$
准确的谱身份是
$$
\boxed{
\frac{\det(t\widetilde G+\widetilde{\mathcal S})}{\det\widetilde G}
=
\frac{(\det V)^2\det(tG+\mathcal S)}
     {(\det V)^2\det G}
=
\frac{\det(tG+\mathcal S)}{\det G}.
}
\tag{14}
$$
这里只在互异域进行矩坐标的矩阵求逆。
$z_i$ 碰撞时，$V,H_{-1},H_1$ 可以退化，
不得继续称这些矩坐标是原三维基底或正定度量。

(3) 的右端却是原连续三维形式：
已付 $A>0$，原 $G>0$，全部原低层 Gram 也严格正。
所以三个系数在全部正权碰撞处连续且没有原正域极点。
原表达式对三个叶权置换不变。
将其原正分母取全部六次置换的乘积，
可得到一个在整个原域严格正的对称共同分母；
分子分母于是均能表示为 $a,s,p,q$ 的多项式。
因此 (14) 在有理函数域约简后，坐标 Vandermonde 因子完整消去，
所得分母在原正域也无零。

源码的 $G$ 始终取 (11) 后三列的**原物理 Gram**，
不换任意参考度量。
在矩坐标中算
$$
R=\widetilde G^{-1}\widetilde{\mathcal S},\qquad
c_1=\operatorname{tr}R,\quad
c_2=\sum_{i<j}(R_{ii}R_{jj}-R_{ij}R_{ji}),\quad
c_3=\det R.
\tag{15}
$$
(15) 只是 (14) 三个原系数的精确计算。
全等正权点 $(a,s,p,q)=(1,3,3,1)$ 的约简分母必须非零；
源码保这一真实碰撞检查，不将有理坐标极点留给后续符号外推。

## 5. 五个闭权序中的加权齐次代换

继续使用已证明的五域：
$$
v_0=1,\ v_1=1+A,\ v_2=1+A+B,\ 
v_3=1+A+B+C,\ v_4=1+A+B+C+D,
\quad A,B,C,D\ge0.
$$
pair 位于 $k$，$\tau=v_k$。
另外四组按降序记为 $s_1,s_2,s_3,s_4$。
设
$$
P_a=s_1,\quad P_s=s_2+s_3+s_4,\quad
P_p=s_2s_3+s_2s_4+s_3s_4,\quad P_q=s_2s_3s_4.
$$
则
$$
a=P_a/\tau,\quad s=P_s/\tau,\quad
p=P_p/\tau^2,\quad q=P_q/\tau^3.
\tag{16}
$$
五个闭域覆盖 $a\ge\max(z_i)>0$ 的全部原输入，
包括所有叶碰撞、头与叶碰撞以及与 pair 的碰撞。

对每个原同向分子 $n(a,s,p,q)$，取权 $(1,1,2,3)$ 的最大次数 $d$，
以额外变量 $\tau$ 补到齐次，便有
$$
n^{\rm wh}(P_a,P_s,P_p,P_q,\tau)
=\tau^d n(P_a/\tau,P_s/\tau,P_p/\tau^2,P_q/\tau^3).
\tag{17}
$$
$\tau\ge1$，故保原系数的符号。
源码用精确系数非负和已付半径二有理平方配方检验每个域；
余式常数必须严格正，并必须完成全多项式乘回。
每域固定至多 32 个平方，只打印前三例及小摘要。

任何当前系数或域不通过就准确停止 INCONCLUSIVE，
不外推下一系数，不称作原 Schur 的反例。

## 6. 只有三个系数完整成功才允许的谱收尾

因为原 $G>0$、$\mathcal S=\mathcal S^{\mathsf t}$，
$G^{-1}\mathcal S$ 相似于真实 Hermitian 矩阵
$G^{-1/2}\mathcal S G^{-1/2}$。
若三个原系数在每个闭权序域都严格正，则
$$
t^3+c_1t^2+c_2t+c_3>0\qquad(t\ge0).
$$
任一非正特征值 $\lambda$ 会在 $t=-\lambda\ge0$ 给出零，
矛盾。因此原 $\mathcal S>0$。
这一步在碰撞权直接使用原连续形式与严格系数证书，
没有由坐标连续性只得到半正后再偷偷宣称正定。

合已付 $A>0$，才得到整个六维原 S1；
再加原 pair-singlet 的已付出生一 S1，才得到完整九维结论。
若只完成一个或两个谱系数，均不足以作此收尾。
S2、七位联合来源、原 $W$ 费用及 $N=M$ 仍不由本输入自动支付。
