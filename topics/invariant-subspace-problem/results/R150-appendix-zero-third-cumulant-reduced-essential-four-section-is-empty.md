# R150 附录：第三累积量为零时，四个不同物理支撑点的本质四维临界支为空

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 对原六模式完整立方临界系统，若第三累积量 $V=0$，而第三普通矩 $T_3$ 的本质维数为四，则原 $H$ 的准确长度四公共曲线支撑不可能由四个不同点组成。结论包含一次矩系数为零以及原无穷远点；不要求一次矩的三阶 Hankel 矩阵满秩。

本稿仅关闭这一约化支撑分支。重节点的长度四支撑仍须继续；没有把一般 $V\ne0$ 或完整临界集宣布为空，也没有由此推出原普通 ISP。

## 1. 原完整梯度与已付支撑归约

保留 [原六模式 Schur 稿](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) 的非退化对称矩阵 $K$、物理曲线
$$
v(z)=(1,z,\ldots,z^5)^{\mathsf T},
\qquad F_0(x)=\tfrac12x^{\mathsf T}Kx,
$$
以及原全部 Hankel 累积量 $y,H,V$。物理核满足
$v(z)^{\mathsf T}Kv(z)=0$。

在 $V=0$ 时，普通矩泛函为形式 Gaussian 泛函
$$
\Lambda[f(x)]
=\left.\exp(-H(\partial,\partial))f(x)\right|_{x=y}.
\tag{1.1}
$$
这是复代数身份，不使用正性或概率分布。原第三普通矩为
$$
T_3(r)=(y^{\mathsf T}r)
\big[(y^{\mathsf T}r)^2-6H(r,r)\big].
\tag{1.2}
$$
完整临界性包含
$$
\Lambda[xF_0(x)^2]=0,
\tag{1.3}
$$
$$
\Lambda[F_0(x)(v(z)^{\mathsf T}Kx)^2]=0
\quad\text{对全部物理 }z,
\tag{1.4}
$$
$$
T_3(Kv(z))=0.
\tag{1.5}
$$
这些依次是原全部一次梯度、全部二阶物理梯度和全部最高梯度，准确系数见 [原完整低阶梯度稿](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md)。因本质维数为四，$y\ne0$，且 $K$ 可逆；由 (1.2)、(1.5) 在二元多项式整环中消去非零极线，得到
$$
(y^{\mathsf T}Kv(z))^2=6v(z)^{\mathsf T}KHKv(z).
\tag{1.6}
$$

[秩三外值域排除](R150-appendix-zero-third-cumulant-rank-three-outer-range-exclusion.md) 已给
$$
\operatorname{rank}H=4,\quad
y\in E=\operatorname{Ran}H=E_D,
\tag{1.7}
$$
其中 $D$ 是由原 $H$ 唯一确定的准确长度四 jet divisor。
[独立双二次关系与基点归约](R150-appendix-zero-third-cumulant-essential-four-independent-quadrics-and-basepoint-reduction.md) 又从原完整梯度证明：$E_D$ 的物理投影有唯一简单基点 $s_0$，且此点属于 $D$ 的支撑。

反设 $D=s_0+s_1+s_2+s_3$ 是四个不同点。取对应非零正规列 $u_i$，可包含 $u_i=v_{\rm hom}(\infty)$。它们线性独立，而且
$$
y=\sum_{i=0}^3a_i u_i,\qquad
H=\sum_{i=0}^3h_i u_i^{\otimes2},\qquad h_i\ne0.
\tag{1.8}
$$
最后的非零性由原 $H$ 秩四得到。基点身份准确是
$$
u_0^{\mathsf T}Ku_i=0\quad(0\le i\le3).
\tag{1.9}
$$
记
$$
k_{ij}=u_i^{\mathsf T}Ku_j,\qquad
p_i(z)=u_i^{\mathsf T}Kv_{\rm hom}(z).
\tag{1.10}
$$
四个 $p_i$ 线性独立。

在独立节点坐标 $x=\sum_i u_iX_i$ 中，(1.1) 分解为四个一变量泛函。置
$$
b_i=\Lambda[X_i^2]=a_i^2-2h_i,\qquad
c_i=\Lambda[X_i^3]=a_i^3-6a_ih_i
=3a_ib_i-2a_i^3.
\tag{1.11}
$$
即使当前点 $V=0$，完整临界性仍包括原全部 $V$ 方向的导数。特别，沿四个节点的 $v_i u_i^{\otimes3}$ 变化不能删去。一般节点换元
$$
(a_i,h_i,v_i)\longleftrightarrow
(a_i,b_i,c_i),\qquad
c_i=a_i^3-6a_ih_i+4v_i
\tag{1.12}
$$
为 Jacobian 非零常数的三角换元，故完整临界性给全部这些节点普通矩的梯度。

## 2. 活跃三点的三个交叉配对不能全部非零

由于 (1.9)，$F_0$ 与 $X_0$ 无关。若 $k_{12},k_{13},k_{23}$ 均非零，可对三个节点列作非零复缩放，使这三个配对都为一。此时
$$
F_0=X_1X_2+X_1X_3+X_2X_3.
$$
沿这三个节点的目标准确为
$$
\begin{aligned}
\Lambda[F_0^3]={}&c_1c_2+c_1c_3+c_2c_3\\
&+3[c_1(b_2a_3+a_2b_3)+c_2(b_1a_3+a_1b_3)
+c_3(b_1a_2+a_1b_2)]\\
&+6b_1b_2b_3.
\end{aligned}
\tag{2.1}
$$
由 (1.12)，对每个无序对 $\{j,k\}\subset\{1,2,3\}$ 都有
$$
c_jb_k+c_kb_j=0,
\tag{2.2}
$$
$$
c_ja_k+c_ka_j+2b_jb_k=0,
\tag{2.3}
$$
$$
c_j+c_k+3(b_ja_k+b_ka_j)=0.
\tag{2.4}
$$
这是 [三个不同物理点稿](R150-appendix-three-distinct-physical-support-complete-critical-classification.md) §4 的原节点系统；下面补全本稿所需的零均值系数情形，不把旧的全部 $a_i\ne0$ 条件移过来。

先设 $a_1a_2a_3\ne0$。若三个 $b_i$ 都非零，(2.2) 迫全部 $c_i=0$，随后 (2.3) 矛盾。若恰两个 $b_i$ 非零，(2.2) 先杀掉另一个 $c_i$，(2.3) 再利用全部 $a_i\ne0$ 杀掉余下两个 $c_i$，仍与非零的两个 $b$ 之积矛盾。若恰一个 $b_i\ne0$，(2.2)、(2.3) 先迫全部 $c_i=0$，(2.4) 再与某个非零 $b_i a_j$ 矛盾。若全部 $b_i=0$，(2.3) 迫全部 $c_i=0$；但由 (1.11)，$c_i=-2a_i^3\ne0$。故这一情况不可能。

若某个 $a_i=0$，可设 $a_1=0$。由 $h_1\ne0$，
$$
b_1=-2h_1\ne0,\qquad c_1=0.
$$
对节点对 $\{1,2\},\{1,3\}$，(2.2) 先给 $c_2=c_3=0$，(2.3) 再给 $b_2=b_3=0$，(2.4) 随后给 $a_2=a_3=0$。于是 $b_2=-2h_2\ne0$，矛盾。这也包括两个或三个 $a_i$ 为零的情况。

因此三个活跃配对中至少一个为零。

## 3. 准确只可能一个活跃配对为零

若至少两个活跃配对为零，则会有两个不同的全等向物理三点支撑，二者都包含 $s_0$。[全等向长度三曲线 jets 分类](R150-appendix-classification-of-isotropic-length-three-curve-jets.md) 说明这样的三点组必须分别是
$$
P_+(z)=z^3-5z^2+\tfrac{32}{5}z-\tfrac85,\qquad
P_-(z)=z^3+27z^2+\tfrac{864}{5}z+\tfrac{864}{5}
\tag{3.1}
$$
的完整根组。两多项式互素：令
$$
A=5P_+,\quad B=5P_-,\quad
Q=20z^2+104z+109.
$$
则 $B-A=8Q$，而 $A$ 除以 $Q$ 的余式为
$\frac{5399}{20}(z+1)$，且 $Q(-1)=25\ne0$。
所以两组根不相交；两个三点组不能分享 $s_0$。若它们是同一组根，则四个不同节点也无法全部容纳于该三点组。因此至少两个活跃零配对不可能。

重排后，唯一可能的模式为
$$
k_{23}=0,\qquad k_{12}=\alpha\ne0,\qquad
k_{13}=\beta\ne0,
\tag{3.2}
$$
并且
$$
\operatorname{span}\{u_0,u_2,u_3\}=W_+
\quad\text{或 }W_-.
\tag{3.3}
$$
特别 $s_0,s_2,s_3$ 均为原有限不同点。此时
$$
F_0=X_1L,\qquad L=\alpha X_2+\beta X_3.
\tag{3.4}
$$

需要一个已付极线重数事实。由 (3.3)，$p_0,p_2,p_3$ 都被相应 $P=P_\pm$ 整除。原 [任意长度四单基点定理](R150-appendix-length-four-physical-projections-have-at-most-one-basepoint.md) §§2–4 已证明：两个不同物理点的五次极线，其最大公因子次数至多三。由于 $p_2$ 在自己的点 $s_2$ 至少二重，若 $p_3$ 在 $s_2$ 也至少二重，则二者的共同因子含 $P(z)(z-s_2)$，违反该界。因此
$$
p_3'(s_2)\ne0,\qquad p_2'(s_3)\ne0.
\tag{3.5}
$$
这里使用原有限图中的导数；非零代表列的缩放不改变零点重数。

## 4. 最高式与完整均值梯度迫聚合均值为零

将 (1.8) 代入原最高式 (1.6)，得
$$
\left(\sum_{i=0}^3a_ip_i(z)\right)^2
=6\sum_{i=0}^3h_ip_i(z)^2.
\tag{4.1}
$$
在 $s_2$ 评价，只有 $p_1$ 非零，故
$$
a_1^2=6h_1,\qquad
a_1\ne0,\qquad b_1=\tfrac23a_1^2\ne0,\qquad c_1=0.
\tag{4.2}
$$
定义同一 $L$ 的均值、二阶累积量和普通矩
$$
\mu=\alpha a_2+\beta a_3,\qquad
H_L=\alpha^2h_2+\beta^2h_3,
$$
$$
b_L=\Lambda[L^2]=\mu^2-2H_L,\qquad
c_L=\Lambda[L^3]=\mu^3-6\mu H_L.
\tag{4.3}
$$
在 $s_1$ 评价 (4.1)，包括 $s_1=\infty$ 时的齐次评价，得到
$$
\mu^2=6H_L,\qquad b_L=\tfrac23\mu^2,\qquad c_L=0.
\tag{4.4}
$$

原完整均值梯度 (1.3) 为
$$
\Lambda[xX_1^2L^2]=0.
$$
节点列独立，且 $X_1$ 与其余节点形式独立。其 $u_2,u_3,u_0$ 分量，在除去非零 $b_1$ 后依次给
$$
\Lambda[X_iL^2]=a_i b_L-4h_iL_i\mu=0
\quad(i=2,3),
\tag{4.5}
$$
$$
a_0b_L=0,
\tag{4.6}
$$
其中 $L_2=\alpha,L_3=\beta$。式 (4.5) 由同一 Gaussian 泛函直接展开；没有引入新的矩变量。

反设 $\mu\ne0$。由 (4.4)、(4.6)，$a_0=0$。将 (4.2) 代回 (4.1)，$p_1^2$ 项全局相消。在有限点 $s_2$ 作一阶导数；因 $p_2$ 在自己的点至少二重、$p_0,p_3$ 在该点为零，而 $p_1(s_2)\ne0$，得到
$$
a_0p_0'(s_2)+a_3p_3'(s_2)=0.
$$
由 $a_0=0$ 和 (3.5)，$a_3=0$。同样在 $s_3$ 得 $a_2=0$。于是 $\mu=0$，矛盾。

故准确有
$$
\boxed{\ \mu=0,\qquad H_L=0,\qquad b_L=0.\ }
\tag{4.7}
$$
这并不声称随机变量或局部代数元素 $L$ 为零；下面保留它与其余原变量的非零混合二阶矩。

## 5. 完整二阶梯度排除最后的零聚合矩情形

写
$$
Y(z)=p_0(z)X_0+p_2(z)X_2+p_3(z)X_3,\qquad
m_Y(z)=a_0p_0(z)+a_2p_2(z)+a_3p_3(z),
$$
$$
D(z)=\alpha h_2p_2(z)+\beta h_3p_3(z).
\tag{5.1}
$$
因为 $\alpha,\beta,h_2,h_3\ne0$，且 $p_2,p_3$ 独立，
$$
D\ne0
\tag{5.2}
$$
是非零物理五次式。由 (4.7) 和同一 Gaussian 展开，
$$
\Lambda[LY]=-2D,\qquad
\Lambda[LY^2]=-4m_YD.
\tag{5.3}
$$
原二阶梯度 (1.4) 现在要求
$$
0=\Lambda[X_1L(p_1X_1+Y)^2].
$$
利用 $X_1$ 与其余节点独立，(4.2)、(4.7)、(5.3) 将其准确化为
$$
\begin{aligned}
0
&=c_1p_1^2\mu
+2b_1p_1\Lambda[LY]
+a_1\Lambda[LY^2]\\
&=-4D(z)\bigl[b_1p_1(z)+a_1m_Y(z)\bigr].
\end{aligned}
\tag{5.4}
$$
在物理二元多项式整环中，(5.2) 迫
$$
b_1p_1+a_1(a_0p_0+a_2p_2+a_3p_3)=0.
\tag{5.5}
$$
但四个 $p_i$ 独立，而 $p_1$ 的系数 $b_1\ne0$。矛盾。

因此，原 $V=0,\ \operatorname{essdim}T_3=4$ 的完整临界点没有任何四个不同物理节点的支撑。

## 6. 当前保留范围

结合已付归约，若这一 $V=0$、本质四维支仍存在，原 $H$ 必为秩四，$y\in\operatorname{Ran}H$，其唯一准确长度四支撑只能有重节点：
$$
4,\qquad 3+1,\qquad 2+2,\qquad 2+1+1.
$$
它仍须满足唯一简单基点、两条独立原二次关系和全部原梯度。这些条件只是后续必须同时使用的约束，不能把所有具有该重数型的支撑当作临界点。

本稿没有使用旧外均值支的归一化条件，也没有由物理支撑上的零式推断所有匹配方向自动为零。最终全局目标仍是原三个匹配 Bell 值的所需消失及相应幂归属；未闭合的重节点、其他本质维数与 $V\ne0$ 分支继续保留。
