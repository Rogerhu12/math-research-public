# 五位同一 Ward 费用的五次伴随与 Newton 矩压缩

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127 / stable_kernel_return。

**状态：以下有限代数表示和来源身份已证明；平方迹的正性尚未由此得到。** 本输入保持同一个五位 S2 的全部四维低源，只把全层五维运算改写到初等对称变量，避开五个原权变量中巨大矩阵条目的提前展开。它接续 [同一完整投影说明](2026-11-28-odd-hard-top-s2-one-projection-source-8542.md)；不重跑超时的旧输入或提高资源界。

## 1. 真实物理相似及其准确边界

仍令 $z_i=a_i^2>0$，并写
$$
S=e_1(z),\quad Z=e_2(z),\quad W=e_3(z),\quad U=e_4(z),\quad V=e_5(z),
\qquad m_j=\sum_i z_i^j.
$$
在原一孔坐标 $f_i=a_i u_i$ 中，物理内积为 $\sum_i z_i\overline u_i v_i$。暂取五个 $z_i$ 两两不同，将 $u_i=p(z_i)$ 表为次数至多四的多项式值。评价矩阵 $J_{ij}=z_i^{j-1}$ 可逆。

乘以变量的真实算子在系数列中的矩阵为
$$
\mathsf T=
\begin{pmatrix}
0&0&0&0&V\\
1&0&0&0&-U\\
0&1&0&0&W\\
0&0&1&0&-Z\\
0&0&0&1&S
\end{pmatrix},
\tag{1.1}
$$
即多项式 $t^5-St^4+Zt^3-Wt^2+Ut-V$ 的伴随矩阵。原算子 $\mathbf1(z_1,\ldots,z_5)$ 准确变为
$$
\mathsf Q=e_0(m_1,m_2,m_3,m_4,m_5).
\tag{1.2}
$$
前五个 $m_j$ 用 Newton 身份在 $S,Z,W,U,V$ 中表达。真实度量是 $J^*\operatorname{diag}(z_i)J$，所以 $\mathsf T,\mathsf Q$ 是物理自伴，而其普通矩阵转置通常不代表物理伴随。

primitive 正交投影是
$$
\Pi=I-\mathsf Q/S.
$$
下文的每个星号都按原物理伴随生成，代码逐项使用所列反序式。特别最后计算的是
$$
\operatorname{Tr}(K_A^2)=\sum_{i,j}(K_A)_{ij}(K_A)_{ji},
$$
不是伴随矩阵坐标的欧氏 Frobenius 平方。

## 2. 同一完整低层 Gram 与顶精度

[R288 的全层系数式](../results/R288-appendix-birth-one-precision-coefficients-and-common-source-s2-congruences.md)在本坐标给
$$
F_1=SI-2\mathsf T+\mathsf Q,
$$
$$
F_2=ZI-2S\mathsf T+3\mathsf T^2
+S\mathsf Q-\mathsf T\mathsf Q-\mathsf Q\mathsf T,
\tag{2.1}
$$
$$
\begin{aligned}
F_3={}&WI-2Z\mathsf T+3S\mathsf T^2-4\mathsf T^3+Z\mathsf Q\\
&-S(\mathsf T\mathsf Q+\mathsf Q\mathsf T)
+\mathsf T^2\mathsf Q+\mathsf T\mathsf Q\mathsf T+\mathsf Q\mathsf T^2.
\end{aligned}
$$
因此
$$
L_1=\Pi F_1^{-1}\Pi,\qquad L_2=\Pi F_2^{-1}\Pi,
\qquad
E:=L_3^{-1}=F_3-\frac{F_3\mathsf QF_3}{16U}.
\tag{2.2}
$$
所有式子均以零延拓表示低源算子。最后一式是真正完整 Schur：原 $F_3a$ 的真空系数四与 $a^*F_3a=16U$ 产生该分母，不是先压缩后取逆。

完整行列式为
$$
\det F_1=4\delta,\quad \delta=S^2W-4SU+12V,
$$
$$
\det F_2=9\epsilon,\quad \epsilon=U^2Z-4SUV+12V^2.
\tag{2.3}
$$
二者在原全正权域严格正。另由 (1.1) 的特征多项式，
$$
\mathsf T^{-1}
=\frac{\mathsf T^4-S\mathsf T^3+Z\mathsf T^2-W\mathsf T+UI}{V}.
\tag{2.4}
$$

## 3. 完整层联合块的显式生成式

记 $R=d:\mathcal H_2\to\mathcal H_1$，$d_+=d:\mathcal H_3\to\mathcal H_2$，
$R_2=d^2/2$，$F_{\rm mid}=d_+d_+^*$，完整三次下降 $C=\sum a_i^3E_i$ 及倒数权上升 $e=\sum a_i^{-1}E_i^*$。全部都与前述 Ward 来源相同。

下面各矩阵是这些原完整算子在同一伴随坐标中的表达。置
$$
H=CR^*=m_2I-2\mathsf T^2+\mathsf Q\mathsf T,\quad
H^*=m_2I-2\mathsf T^2+\mathsf T\mathsf Q,
$$
$$
Q_c=Ce=SI-2\mathsf T+\mathsf T^{-1}\mathsf Q\mathsf T,\quad
Q_c^*=SI-2\mathsf T+\mathsf T\mathsf Q\mathsf T^{-1}.
\tag{3.1}
$$
令
$$
D_X=(Sm_2-m_3)I-2m_2\mathsf T-2S\mathsf T^2+6\mathsf T^3.
$$
则
$$
X=(Cd_+)R_2^*
=D_X+m_2\mathsf Q+S\mathsf Q\mathsf T
-\mathsf T\mathsf Q\mathsf T-\mathsf T^2\mathsf Q-2\mathsf Q\mathsf T^2.
\tag{3.2}
$$
$X^*$ 为该式中每项按物理星号反序的式子。

再令
$$
D_C=(Sm_3+m_2^2-2m_4)I-2m_3\mathsf T-4m_2\mathsf T^2
-2S\mathsf T^3+12\mathsf T^4.
$$
则
$$
\begin{aligned}
F_C:=(Cd_+)(Cd_+)^*={}&D_C+m_3\mathsf Q
+m_2(\mathsf T\mathsf Q+\mathsf Q\mathsf T)+S\mathsf T\mathsf Q\mathsf T\\
&-2(\mathsf T^3\mathsf Q+\mathsf Q\mathsf T^3
+\mathsf T^2\mathsf Q\mathsf T+\mathsf T\mathsf Q\mathsf T^2).
\end{aligned}
\tag{3.3}
$$
这两式可以直接逐三元子集核对。例如在原 log 坐标中，对 $x=z_i,y=z_j$，
$$
X_{ij}=y[m_2+Sy-xy-x^2-2y^2]\quad(i\ne j),
$$
$$
(F_C)_{ij}=y[m_3+m_2(x+y)+Sxy-2(x^3+y^3+x^2y+xy^2)].
$$
其对角分别为
$$
Sm_2-m_3-xm_2-Sx^2+2x^3,
$$
$$
Sm_3+m_2^2-2m_4-xm_3-2m_2x^2-Sx^3+4x^4.
$$
将对应秩项的对角扣除即得 $D_X,D_C$，所以没有由几个样本拟合公式。

这里的 $e$ 始终指同一个全局倒数权 creation 在所列层的限制。五位完整交换关系为
$
d_+\,e|_{\mathcal H_2}=e|_{\mathcal H_1}R+I_{\mathcal H_2},\qquad
R\,e|_{\mathcal H_1}=e|_{\mathcal H_0}\,d|_{\mathcal H_1}+3I_{\mathcal H_1}.
$
因此
$$
F_{\rm mid}e=eF_1+R^*,
\qquad
Y:=\tfrac12 R F_{\rm mid}e
=2F_1+\mathsf T^{-1}\mathsf Q(SI-\mathsf T).
\tag{3.4}
$$
另有
$$
E_1:=e^*e=\frac UV I-2\mathsf T^{-1}
+\mathsf T^{-1}\mathsf Q\mathsf T^{-1},
$$
$$
CF_{\rm mid}e=Q_cF_1+H,\qquad
e^*F_{\rm mid}e=E_1F_1+3I+\mathsf Q\mathsf T^{-1}.
\tag{3.5}
$$
(3.4)–(3.5) 中的常数一和三使用了当前五位层次，未直接推广到别的位数。

## 4. 保留一个完整 Schur 的四个共同块

上源精度的准确零延拓为
$$
\widetilde C_u
=F_{\rm mid}-F_{\rm mid}R^*(4F_2)^{-1}RF_{\rm mid}.
$$
因此在同一个低源上定义
$$
K_{cc}=\Pi(F_C-XF_2^{-1}X^*)\Pi,
$$
$$
K_{ce}=\Pi(Q_cF_1+H-XF_2^{-1}Y)\Pi,\qquad K_{ec}=K_{ce}^*,
$$
$$
K_{ee}=\Pi(E_1F_1+3I+\mathsf Q\mathsf T^{-1}-Y^*F_2^{-1}Y)\Pi.
\tag{4.1}
$$
它们分别就是 $C\widetilde C_uC^*$、$C\widetilde C_ue$、$e^*\widetilde C_uC^*$、$e^*\widetilde C_ue$ 的完整低源压缩，故来自同一个正的二行二列 Schur 块，而不是四个独立估计。

设 $\Theta=L_1E$，则原 Ward 费用准确为
$$
\boxed{
K_A=L_2\left[
K_{cc}+K_{ce}\Theta+\Theta^*K_{ec}
+\Theta^*K_{ee}\Theta
\right]L_2.
}
\tag{4.2}
$$
两个交叉项完整保留；此式与一次完整投影 $V^*PV$ 是同一个物理算子。整个五维矩阵延零的平方迹等于原四维 $L$ 上的平方迹。

## 5. 标量的范围、连续延拓及可续算输入

所有分母只使用 $2,3,S,U,V,\delta,\epsilon$ 的非负整数幂，均在原正权域严格非零。对互异权，§1 的评价相似证明 (2.1)–(4.2) 的全部算子身份；互异正权稠密，而这些真实完整 Gram 与分母在全部正权域连续且非奇异。因此最终标量
$$
\operatorname{Tr}_L(K_A^2)=N(S,Z,W,U,V)/D(S,Z,W,U,V)
$$
准确延拓到相等权。没有在评价矩阵奇异时假装它仍是可逆相似，也没有在伴随坐标中直接比较普通欧氏范数。

[新精确源](2026-11-28-five-bit-s2-companion-moment-cost-square-8542.py)保留 180 秒和 4 GiB 原资源界。它在形成真正 $K_A$ 后先以原子替换写入完整分子矩阵与分母因子的 checkpoint；后续若超时，继续的是这个已经付出的同一原来源。平方迹成功形成后，完整初等对称变量系数仍全部保留，不把非正系数删掉。

若报告仅为 EXACT_COST_READY 或 EXACT_SCALAR_READY，不得据此称 S2 成立。只有实际标量正性门通过，或在保留标量上另有完整证明，才能接已刊同一低源 $I/2$ 预算。若 $D-4N$ 的全部初等对称变量系数非负且非零，则因 $S,Z,W,U,V>0$，这本身是有效但可能过强的充分证书；失败时仍可在原正根域继续，不能将它视为 S2 的反例。
