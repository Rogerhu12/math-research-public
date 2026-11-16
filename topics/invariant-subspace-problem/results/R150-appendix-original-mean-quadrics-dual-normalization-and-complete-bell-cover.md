# 原秩三均值曲面的四二次图、对偶正规化与完整 Bell 覆盖

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root；normal_annihilator 独立复核核心推导。AI-assisted: GPT-6 Astra Pro。

**状态：已证明。** 本稿复用已实际完成的原七次来源和35节点定理，不新增数值运行。原四个二次式在整个秩三均值曲面上没有公共零点，并给原六次面的对偶曲面的有限正规化；对偶次数恰80。将同一个七次来源乘回原 Bell 方程，还得到覆盖全部 Bell=1 参数的19个明确开集及可回填原来源的粘合公式。各开集上的完整临界理想是否为单位仍待证明。

## 1. 同一原对象与已付来源

系数域仍为
$$
E=\mathbb Q[d]/(3725d^3-43931504d^2+6080833024d+52565262336).
$$
保留原规范矩阵、参数和全部均值坐标：
$$
A(\mu)=\sum_{i=0}^3\mu_iT'_i,\qquad
F(\mu)=\det A(\mu),\qquad
\mathcal D=V(F)\subset\mathbb P^3_E,
$$
$$
M(y)=[T'_0y,T'_1y,T'_2y,T'_3y],\qquad
Y=V(I_4(M))\subset\mathbb P^5_E,
$$
$$
X=\{A(\mu)y=0\}\subset\mathbb P^3_E\times\mathbb P^5_E.
$$

[原完整关联定理](R150-appendix-original-rank-three-mean-incidence-and-complete-sextic-pencil.md)给
$$
I_3(M)=(y_0,\ldots,y_5)^3.
\tag{1.1}
$$
因此 $M$ 在整个 $Y$ 上秩恰3。其参数核为线丛，原常秩图给概形同构
$$
X\xrightarrow{\ \sim\ }Y.
\tag{1.2}
$$
这里不是只在一般点取一条参数核线。

[完整交几何](R150-appendix-original-mean-rank-three-integral-surface-and-complete-intersection-geometry.md)给 $X$ 上两个原超平面类
$$
u=c_1(\mathcal O_X(1,0)),\qquad
v=c_1(\mathcal O_X(0,1)),\qquad
u^2=6,\quad uv=15,\quad v^2=20.
\tag{1.3}
$$
由(1.2)，$v$ 是原 $Y\subset\mathbb P^5$ 的超平面类，故为很充足类。

[35个几何节点定理](R150-appendix-original-sextic-pencil-has-exactly-thirty-five-geometric-nodes.md)证明：$\mathcal D$ 几何整且正规，奇点恰为35个几何 $A_1$ 点；$X$ 光滑、几何整，投影
$$
\pi:X\longrightarrow\mathcal D
$$
是保全部核方向的极小解消。它在 rank5 开集上是同构。

写
$$
q_i(y)=y^{\mathsf T}T'_iy\quad(0\le i<4).
$$
以 $\delta_J(y)$ 表示 $M$ 的全部15个原4阶子式，$J$ 遍历原六行的4元子集；不换原列。该节点定理的实际完整792×1848来源给
$$
(y_0,\ldots,y_5)^7\subset(q_0,q_1,q_2,q_3,\delta_J).
\tag{1.4}
$$
所有系数在原 $E$ 中，只倒固定系数单位。

## 2. 四个原二次式定义整个 $X$ 上的有限映射

在 $Y$ 上全部 $\delta_J$ 为零。由(1.4)，四个 $q_i$ 不可能在任何几何点同时为零。更强地，它们在 $Y$ 上生成 $\mathcal O_Y(2)$：在原 $y_a\ne0$ 图，$y_a^7$ 的完整来源除以 $y_a^7$ 就给局部单位组合。

故有在整个原曲面上定义的态射
$$
\phi:X\cong Y\longrightarrow(\mathbb P^3_E)^\vee,\qquad
([\,\mu\,],[\,y\,])\longmapsto[q_0(y):q_1(y):q_2(y):q_3(y)],
\tag{2.1}
$$
并且
$$
\phi^*\mathcal O(1)=\mathcal O_X(0,2),\qquad
c_1(\phi^*\mathcal O(1))=2v.
\tag{2.2}
$$
这里 $\vee$ 表示原 $\mu$ 参数空间的对偶；没有更换四个原坐标。

由于 $X$ 射影，$\phi$ 适当。若某几何纤维正维，则它包含一条完整曲线 $C$；(2.2)在该曲线上次数为零，但 $2v$ 充足，限制到任何完整曲线次数严格正，矛盾。因此所有纤维均有限。由[适当有限纤维判准，Stacks Tag 02LS](https://stacks.math.columbia.edu/tag/02LS)，
$$
\boxed{\phi\text{ 是到其概形像的有限态射。}}
\tag{2.3}
$$

像取由 $X$ 定义的约化整概形，记为 $\Sigma$。有限性及 $\dim X=2$ 使 $\Sigma$ 是对偶 $\mathbb P^3$ 中的整曲面。以上同样在代数闭包上成立。

## 3. 与原 Gauss 映射一致，并有明确有理逆

在 $\mathcal D$ 的 rank5 光滑开集，原核向量为 $y$，且
$$
\operatorname{adj}A(\mu)=c\,yy^{\mathsf T},\qquad c\ne0.
$$
所以
$$
\partial_{\mu_i}F=c\,q_i(y).
\tag{3.1}
$$
(2.1)在该开集恰为原六次面的 Gauss 映射。其像的闭包因此就是原射影对偶：
$$
\Sigma=\mathcal D^\vee.
\tag{3.2}
$$

下面直接证明其双有理性，不预先假定 Gauss 映射的次数。

在原 incidence 上
$$
\mu^{\mathsf T}q(y)=y^{\mathsf T}A(\mu)y=0.
\tag{3.3}
$$
特征零中有限函数域扩张可分，所以在一个稠密开集上 $d\phi$ 的秩为2。还可同时要求 $\pi$ 落在 rank5 光滑开集、$\phi$ 落在 $\Sigma$ 的光滑开集。

取这个开集中的切向量。由(3.1)，原切面条件为
$$
q^{\mathsf T}d\mu=0.
$$
微分(3.3)得到
$$
\mu^{\mathsf T}dq+q^{\mathsf T}d\mu=0,
\qquad\text{故}\qquad
\mu^{\mathsf T}dq=0.
\tag{3.4}
$$
对 $q$ 的射影提升所作标量改变只加入 $q$ 的倍数，由(3.3)仍被 $\mu$ 杀掉。因此(3.4)是内在的射影切面关系。

由于 $d\phi$ 满秩，$q$ 及这些 $dq$ 张成 $\Sigma$ 在 $[q]$ 的完整三维仿射切空间，其零化子恰为一条线。(3.3)–(3.4)说明该唯一线就是 $[\mu]$。于是 $\Sigma$ 的 Gauss 映射在这个开集恢复原参数 $[\mu]$；再取原 rank5 矩阵 $A(\mu)$ 的唯一核点便恢复 $[y]$。

这给出定义在 $E$ 上的有理逆
$$
\Sigma\dashrightarrow X,\qquad
[q]\longmapsto\bigl(\operatorname{Gauss}_{\Sigma}([q]),
 \ker A(\operatorname{Gauss}_{\Sigma}([q]))\bigr).
$$
所以
$$
\boxed{\phi:X\longrightarrow\mathcal D^\vee
\text{ 有限且双有理。}}
\tag{3.5}
$$
该结论在代数闭包上仍成立。

## 4. 对偶的完整正规化及次数80

$X$ 光滑，因而正规。有限双有理映射(3.5)就是 $\Sigma$ 的正规化。也可逐仿射验证：若 $A\subset B\subset K$ 是对应的有限整扩张，$A,B$ 有同一个函数域且 $B$ 整闭，则任何对 $A$ 整的 $K$ 中元素也对 $B$ 整，从而属于 $B$；反向包含由有限性给出。因此 $B$ 恰为 $A$ 在 $K$ 中的整闭包。参见[Stacks 的正规化构造](https://stacks.math.columbia.edu/tag/035E)。

由有限映射的交数投影公式及 $\deg\phi=1$，
$$
\deg(\Sigma)
=(\phi^*\mathcal O(1))^2
=(2v)^2
=4\cdot20.
$$
得到
$$
\boxed{\deg\mathcal D^\vee=80,\qquad
X\cong(\mathcal D^\vee)^\nu.}
\tag{4.1}
$$
没有称 $\mathcal D^\vee$ 本身光滑或正规，也没有从其次数断言任何临界理想已空。

## 5. 全部原核线的像是完整二次圆锥曲线

在任一几何 rank4 参数 $\mu_*$，记
$$
K=\ker A(\mu_*),\qquad \dim K=2.
$$
前稿的原对称消元给
$$
A\sim\operatorname{diag}(U,S),\qquad
S=\begin{pmatrix}a&b\\b&c\end{pmatrix},
$$
其中 $a,b,c$ 是参数 $\mathbb P^3$ 在 $\mu_*$ 的完整局部参数。由于在该点 $S=0$，对消元矩阵求导所增加的项在核上均为零。因此
$$
dA|_K=dS:T_{\mu_*}\mathbb P^3
 \xrightarrow{\ \sim\ }\operatorname{Sym}^2(K^*).
\tag{5.1}
$$
对 $y\in K$，四个原二次值组成的线性泛函为
$$
q(y)(d\mu)=y^{\mathsf T}dA(d\mu)y.
\tag{5.2}
$$
它消去径向 $\mu_*$，故 $[q(y)]$ 落在对偶平面
$$
\mu_*^\perp=\{[q]:\mu_*^{\mathsf T}q=0\}.
$$
(5.1)的对偶把(5.2)识别为整个 $\operatorname{Sym}^2K$ 中的平方向量 $y^2$。故
$$
\boxed{\phi|_{\mathbb P(K)}:
\mathbb P^1\longrightarrow\mu_*^\perp
\text{ 是完整二次 Veronese 嵌入。}}
\tag{5.3}
$$
每条原例外核线因此映为一条光滑平面二次曲线，完整保留全部核方向。不同例外曲线像之间的相交情形不由本稿判定。

## 6. 原七次来源给全部 Bell=1 参数的19图覆盖

现在回到原仿射变量，并保全部自由 moment 参数：
$$
b=y^{\mathsf T}w,\qquad
R_0=E[y_0,\ldots,y_5,w_0,\ldots,w_5]/(b-1),
\qquad S_0=R_0[u_0,\ldots,u_4].
$$
不在此处令 $I_4(M)=0$。

(1.4)的每条原七次来源可写成
$$
y^\alpha=\sum_{i=0}^3 a_{\alpha i}(y)q_i(y)
 +\sum_J c_{\alpha J}(y)\delta_J(y),
\qquad |\alpha|=7,
\tag{6.1}
$$
其中 $a_{\alpha i}$ 齐次次数5，$c_{\alpha J}$ 齐次次数3。它们由同一个原792列单位及其伴随定义；没有重新解源或选另一个子式。

令
$$
A_i(y,w)=\sum_{|\alpha|=7}\binom7\alpha w^\alpha a_{\alpha i}(y),
\quad
C_J(y,w)=\sum_{|\alpha|=7}\binom7\alpha w^\alpha c_{\alpha J}(y).
$$
逐条乘回(6.1)和原多项式恒等式，得到
$$
b^7=\sum_i A_iq_i+\sum_J C_J\delta_J.
$$
因此在未归一的原多项式环中就有完整身份
$$
\boxed{
1=\sum_i A_iq_i+\sum_J C_J\delta_J
 -(b-1)(1+b+\cdots+b^6).
}
\tag{6.2}
$$
$A_i$ 的 $(y,w)$ 双次数是 $(5,7)$，$C_J$ 为 $(3,7)$；全部系数仍在原 $E$ 中。最后一个原 Bell 来源没有省掉。

故在整个 $S_0$ 中，四个 $q_i$ 与十五个 $\delta_J$ 生成单位理想。它们的19个主开集覆盖全部 Bell=1 参数，包括所有非约化基变换：

- $\delta_J\ne0$ 的15图覆盖 rank4 均值支路；
- 在闭支路 $I_4(M)=0$ 上，四个 $q_i\ne0$ 图覆盖全部 rank3 均值，包括原35条核线；
- 由(1.1)及 $b=1$，不存在被遗漏的非零均值 rank≤2 支路。

这些 $q_i$ 开集也可能包含 rank4 点，覆盖不要求各图互不相交。不把某个二次值设为1，不作未经证明的重新缩放。

## 7. 局部判空回填原17梯度的精确粘合规则

令 $J\subset S_0$ 是原全部17个运输后梯度理想，保持原完整9×56 presentation。依次记
$$
(g_1,\ldots,g_{19})=(q_0,q_1,q_2,q_3,\delta_J).
$$
由(6.2)，在 $S_0$ 有固定原源组合
$$
1=\sum_{i=1}^{19}a_i g_i.
\tag{7.1}
$$

以下给一个严格条件式接口：假如后续对每一图实际取得
$$
g_i^{N_i}=\sum_{\ell=1}^{17}b_{i\ell}G_\ell,\qquad
N_i\ge1,\quad b_{i\ell}\in S_0,
\tag{7.2}
$$
则令
$$
N=1+\sum_{i=1}^{19}(N_i-1).
$$
(7.1)的 $N$ 次幂每个展开项至少含某个 $g_i^{N_i}$。按第一个满足该条件的原编号分配每个多重指标，明确得到
$$
1=\sum_{i=1}^{19}B_i g_i^{N_i}.
$$
将(7.2)代入，就得到完整原来源
$$
1=\sum_{\ell=1}^{17}
 \left(\sum_i B_i b_{i\ell}\right)G_\ell
\quad\text{于 }S_0.
\tag{7.3}
$$
提升回 $E[y,w,u]$ 时，差额仍由同一个 $b-1$ 生成，故保持原18来源。

局部单位身份若先写在 $S_0[g_i^{-1}]$，必须先清出一个真实有限幂得到(7.2)，然后才可使用此粘合。某图上数值满秩、一般点空或有限域负判定都不能替代它。若只处理闭支路 $I_4(M)=0$，同样的四图公式须保这些子式作为额外原来源，并且不能据此宣布 rank4 支路已闭。

本稿没有实际提供(7.2)，因此没有声称原 Bell 临界商为零。它给出了完整覆盖和可逐原多项式回填的拼接式，供下一条实质判空使用。

## 8. 证明身份与后续范围

本稿没有新调用数值矩阵程序。唯一计算输入为已独立核验的 run43836278134 / job133193599424 的原七次来源；其数学时间2.981291404秒，binding：
~~~text
b2760f962db8cdca270eb353a64f421d02c6cd4e30de5b4203ac6fd26e65f8af
~~~
完整执行身份、原源码、所有输出SHA均见[35节点稿](R150-appendix-original-sextic-pencil-has-exactly-thirty-five-geometric-nodes.md) §§8–9。次数80由原交数及已证明双有理性推出，未用另一组参数点计数。

下一步仍是原所有临界关系的实际判空、其自然幂来源及完整算子桥。本稿的对偶正规化和19图覆盖不改动原 mean/moment 参数，也不替代普通复可分无限维 Hilbert ISP 的完成标准。
