# R14. 无有理基点时的规范平移：无需额外乘以除子次数

日期：2026-11-12。会话：serre-uniformity-astra-cont；global_geometry。

**状态：已证明。** 本结果加强 R12：R12 中特殊的 Picard 类不是任意有理类，而是自动有一个规范的、定义于基域的 $d$ 次除根。因此可以保持原对应 $f$，仅作平移使拉回的 Poincaré 线丛平凡。好约化整数模型上的平凡化也存在，不产生新的垂直分量障碍。

Hashimoto–Lido–Lombardo–Mascot–Parent (2026), Remark 3.8 已指出可用 $j_D$ 替代有理基点，并强调具体的刚性化计算还需修改。R14 的作用是在本仓库内给出规范平移和好约化平凡化的完整证明，不主张“无基点的存在性思路”是新的文献结论。

这不是 Serre 一致性的证明；没有证明 Mordell–Weil 积分满射、全部 QC 局部函数的非退化或非 CM 有理点排除。

## 1. 精确陈述

设 $k$ 为特征零域，$X/k$ 是光滑射影几何连通曲线，亏格 $g\ge1$，$J=\operatorname{Pic}^0_{X/k}$。设 $D$ 是定义于 $k$ 的除子，次数为 $d>0$，并令
$$
u=\iota_D:X\longrightarrow J,\qquad x\longmapsto[d x-D].
$$
$D$ 不必有效。令 $\mathcal P$ 为 $J\times J^\vee$ 上在两个零截面刚性化的 Poincaré 线丛，$f:J\to J^\vee$ 为定义于 $k$ 的**实际同态**。若初始对应只有有理系数，须先清除它本身的分母；本定理不取消这一步。

对几何基点 $b\in X(\bar k)$，写
$$
i_b(x)=[x-b],\qquad
 a=i_b^*:J^\vee\xrightarrow{\sim}J,
\qquad e_b=[d b-D].
$$
Jacobian 自对偶性给出同构 $a$，且 $a$ 与 $b$ 无关并定义于 $k$（见 R12 §2）。在规范双对偶识别 $J^{\vee\vee}=J$ 下，$f^\vee$ 也是从 $J$ 到 $J^\vee$ 的同态；置
$$
s=f+f^\vee.
$$
假设
$$
\deg\mathcal L_D=0,
\qquad \mathcal L_D=(u,fu)^*\mathcal P.
\tag{1.1}
$$
则 $\mathcal L_b=(i_b,fi_b)^*\mathcal P$ 也次数零，记 $\kappa_b=[\mathcal L_b]\in J(\bar k)$。

**定理 1。** 有以下结论。

1. 元素
   $$\eta_D=d\kappa_b+a\bigl(s(e_b)\bigr)\in J(\bar k)\tag{1.2}$$
   与 $b$ 无关，定义于 $k$；它事实上由一个实际的 $k$ 线丛 $\mathcal M_D$ 表示。
2. 在 $J(k)$ 中，
   $$[\mathcal L_D]=d\eta_D.\tag{1.3}$$
   更强地，实际线丛满足 $\mathcal L_D\simeq\mathcal M_D^{\otimes d}$。
3. 取
   $$c_D=-a^{-1}(\eta_D)\in J^\vee(k),
   \qquad h_D(z)=f(z)+c_D.\tag{1.4}$$
   则实际 $k$ 线丛
   $$\mathcal L_D'=(u,h_Du)^*\mathcal P\tag{1.5}$$
   平凡。因此存在 $k$ 态射 $\widetilde u:X\to\mathcal P^\times$，投影为 $(u,h_Du)$。各提升相差 $k^\times$ 标量，且几何纤维有限。

本定理无需 $f=f^\vee$，也无需 $X(k)\ne\varnothing$。$c_D$ 是公式 (1.2) 给出的规范选择；并不声称使 (1.5) 平凡的所有平移只有这一种，因为还可加入 $J^\vee(k)[d]$。

## 2. Poincaré 双线性给出的两个恒等式

在 $J$ 上记
$$Q_f=(\mathrm{id},f)^*\mathcal P.$$
对几何点 $e\in J(\bar k)$，双线性展开得到
$$
t_e^*Q_f\simeq Q_f\otimes\mathcal P_{f(e)}
 \otimes f^*\mathcal P^{\mathrm{right}}_e\otimes V_e.
\tag{2.1}
$$
这里 $\mathcal P_{f(e)}=\mathcal P|_{J\times\{f(e)\}}$，$\mathcal P^{\mathrm{right}}_e=\mathcal P|_{\{e\}\times J^\vee}$，而 $V_e$ 是来自基域的一维向量空间。按对偶同态的定义，$f^*\mathcal P^{\mathrm{right}}_e$ 在 $J^\vee$ 中的类为 $f^\vee(e)$。因此 (2.1) 中两个非常数的交叉因子合为类 $s(e)$ 的代数平凡线丛：
$$
[t_e^*Q_f]=[Q_f]+[\mathcal P_{s(e)}]
\quad\text{于 }\operatorname{Pic}(J_{\bar k}).
\tag{2.2}
$$
这也直接证明了 $Q_f$ 的 Mumford 同态是 $f+f^\vee$，无需把该公式另作黑箱。

又因 $(z,fz)$ 同时乘以 $d$，Poincaré 双线性给出
$$[d]^*Q_f\simeq Q_f^{\otimes d^2}.
\tag{2.3}
$$
对 $\alpha\in J^\vee(\bar k)$，同理 $[d]^*\mathcal P_\alpha\simeq\mathcal P_\alpha^{\otimes d}$。

由 $u=t_{e_b}\circ[d]\circ i_b$，先用 (2.1)，再用 (2.3)，得到
$$
[\mathcal L_D]=d^2[i_b^*Q_f]+d\,a\bigl(s(e_b)\bigr).
\tag{2.4}
$$
交叉因子在 $X$ 上次数零，故同时有
$$\deg\mathcal L_D=d^2\deg(i_b^*Q_f).\tag{2.5}$$
由 (1.1) 和 $d>0$，$\deg\mathcal L_b=0$，所以 (2.4) 确实是 $J(\bar k)$ 中的等式，并立即给出 (1.3)。这个次数零假设不可删除：若 $f$ 给出正极化，通常有正次数，平移不会改变次数，因而不能平凡化。

## 3. 基点变换、Galois 下降与规范除根

换取几何基点 $b'$，令 $t=[b'-b]\in J(\bar k)$。则
$$i_{b'}=t_{-t}\circ i_b,\qquad e_{b'}=e_b+d t.$$
由 (2.2)，
$$\kappa_{b'}=\kappa_b-a\bigl(s(t)\bigr).\tag{3.1}$$
因此
$$
\begin{aligned}
d\kappa_{b'}+a(s(e_{b'}))
 &=d\kappa_b-d\,a(s(t))+a(s(e_b))+d\,a(s(t))\\
 &=d\kappa_b+a(s(e_b)).
\end{aligned}
$$
这证明 (1.2) 与 $b$ 无关。

对任意 $\sigma\in\operatorname{Gal}(\bar k/k)$，$D,f,a$ 均定义于 $k$，所以 $\sigma(\eta_D)$ 正是使用基点 $\sigma b$ 所得到的同一公式。基点独立性说明 $\sigma(\eta_D)=\eta_D$，从而 $\eta_D\in J(k)$。

这里证明的是**这个特殊类的显式可除性**。一般 $J(k)$ 中的点当然未必可被 $d$ 整除；但 R12 的 $\kappa_D$ 来自二次 Poincaré 拉回，必须使用 (2.4) 中额外的结构。直接把它当作任意类而为此再乘一次 $d$，虽能构造提升，却并非必要。

## 4. 用范数线丛得到实际的有理除根

Galois 不变的 Picard scheme 点不总是实际的 $k$ 线丛。下面显式构造 $\mathcal M_D$，避免这一障碍。

写 $D=\sum_P n_P P$，其中 $P$ 遍历有限个闭点，$k(P)/k$ 为有限可分扩张。将 $P$ 看成 $X(k(P))$ 的基点，可在 $X_{k(P)}$ 上定义实际线丛
$$\mathcal L_P=(i_P,fi_P)^*\mathcal P.$$
令 $\pi_P:X_{k(P)}\to X$ 为基扩张，并取有限平坦映射的范数线丛
$$
\operatorname{Nm}_{\pi_P}(\mathcal L_P)
 =\det((\pi_P)_*\mathcal L_P)\otimes
 \det((\pi_P)_*\mathcal O_{X_{k(P)}})^{-1}.
$$
它定义于 $k$；扩到 $\bar k$ 后成为所有共轭线丛的张量积。定义
$$\mathcal M_D=
 \bigotimes_P\operatorname{Nm}_{\pi_P}(\mathcal L_P)^{\otimes n_P}.
\tag{4.1}$$
负的 $n_P$ 解释为对偶张量幂。所有因子均次数零，所以 $\mathcal M_D$ 次数零。

在 $\bar k$ 上把 $D$ 写成 $\sum_x n_x x$。由 (3.1)，
$$\kappa_x=\kappa_b-a\bigl(s([x-b])\bigr).$$
故
$$
\begin{aligned}
[\mathcal M_D]
 &=\sum_x n_x\kappa_x\\
 &=d\kappa_b-a\Bigl(s\Bigl(\sum_x n_x[x-b]\Bigr)\Bigr)\\
 &=d\kappa_b+a\bigl(s([d b-D])\bigr)
 =\eta_D.
\end{aligned}
\tag{4.2}
$$
这同时给出一个无需在 $J(k)$ 中解乘 $d$ 方程的构造：逐闭点形成 Poincaré 拉回，再取范数。

(1.3)、(4.2) 说明实际 $k$ 线丛 $\mathcal L_D\otimes\mathcal M_D^{-d}$ 在 $\bar k$ 上平凡。一个实际 $k$ 线丛若在 $\bar k$ 上平凡，则由域扩张的上同调基变换，其全局截面空间是一维 $k$ 向量空间；任一非零截面在 $\bar k$ 上是非零常数，因而处处不消失。因此该线丛在 $k$ 上已平凡，证明定理 1(2) 的加强版。

## 5. 平移消去及实际提升

由 R12 的 $u^*=d a$ 与 Poincaré 双线性，
$$
\mathcal L_D'\simeq\mathcal L_D\otimes u^*\mathcal P_{c_D},
$$
而其 Picard 类为
$$
[\mathcal L_D']=d\eta_D+d a(c_D)=0.
$$
它已经是一个实际 $k$ 线丛，故用上一节同样的截面论证得到真正的 $k$ 平凡化，而不只是几何平凡化。

处处非零截面给出到 $\mathcal P^\times$ 的提升。由于 $H^0(X,\mathcal O_X^\times)=k^\times$，全部提升的歧义恰为一个 $k^\times$ 标量。又 $u=t_{e_b}\circ[d]\circ i_b$ 是 Abel–Jacobi 闭嵌入与有限同源及平移的复合，几何纤维有限；提升的纤维包含于 $u$ 的纤维，所以也有限。定理 1 得证。

## 6. 好约化整数模型上自动存在平凡化

**定理 2。** 令 $R$ 为特征零分式域 $K$ 的离散赋值环，$\mathcal X/R$ 为光滑射影曲线，所有几何纤维连通，且泛纤维 $X/K$ 的数据满足定理 1。则定理 1 中的 $u,f,c_D$ 延拓到相应的相对 Jacobian/对偶阿贝尔概形，且 (1.5) 的 Poincaré 拉回在整个 $\mathcal X$ 上平凡。

**证明。** $\mathcal J=\operatorname{Pic}^0_{\mathcal X/R}$ 是阿贝尔概形，其对偶亦然；阿贝尔概形是泛纤维的 Néron 模型。Néron 映射性质分别对光滑 $R$ 概形 $\mathcal X$、$\mathcal J$ 应用，延拓 $u$ 和 $f$。$c_D$ 由对偶阿贝尔概形的真性延拓为 $R$ 截面。于是 $h_D=f+c_D$ 及归一化相对 Poincaré 线丛都可定义，给出 $\mathcal X$ 上的实际线丛 $\mathscr L_D'$。

其泛纤维由定理 1 平凡。选择泛纤维的处处非零截面，将它看作 $\mathscr L_D'$ 的有理截面。因 $\mathcal X$ 正则，其除子只含垂直分量。光滑而几何连通的特纤维是几何不可约的：光滑曲线的不同不可约分量不相交，若有多个就不连通。因此这里只有一个垂直素除子 $\mathcal X_s$，而且特纤维约化。所以该除子为
$$n\mathcal X_s=n\operatorname{div}(\pi)$$
其中 $\pi$ 为 $R$ 的一致化参数。将截面乘以 $\pi^{-n}$ 后，其除子为零，得到整个正则概形上处处非零的截面。故 $\mathscr L_D'$ 平凡。

任何两个积分平凡化的比是 $H^0(\mathcal X,\mathcal O_{\mathcal X}^\times)=R^\times$；选择了泛纤维截面后，需要消去的整数 $n$ 唯一。证毕。

本证明没有要求剩余特征不整除 $d$。所以“$\ell\mid d$ 导致提升本身不存在”是错误的；它只可能影响后续坐标、微分或所用 Mordell–Weil 子群的积分指数。

**同时归一化。** 同一证明适用于 $R=\mathbb Z[S^{-1}]$ 上的光滑射影几何连通模型：泛纤维平凡截面的垂直除子为有限和 $\sum_{q\notin S}n_q\mathcal X_q$，而 $\mathcal X_q=\operatorname{div}(q)$。乘以有限乘积 $\prod_{q\notin S}q^{-n_q}$ 后，可使它在全部好素数处同时积分且处处非零；歧义变为 $\mathbb Z[S^{-1}]^\times$。这不是逐素数作相互不相容的标定。

## 7. 对本课题的作用与剩余边界

对 $X=X_{\rm ns}^+(p)$ 可取全部尖点之和，$d=(p-1)/2$。在适用的光滑好约化模型上，R14 得到：

- 使用 $h=f+c_D$ 即可，不必使用 R12 的 $h=d f+c$；
- $c_D$ 可由范数线丛公式 (4.1) 得到，而不是假设任意有理点可以被 $d$ 整除；
- 好素数处的平凡化存在且可同时归一化。

但 $u=[d]\circ i_b+e_b$ 本身仍含乘 $d$。若辅助素数 $\ell\mid d$，则其特纤维上的微分可为零；R14 没有把这一步变为积分可逆。即使 $\ell\nmid d$，Mordell–Weil 群到一阶形式群商的满射也不是由本定理推出。坏约化素数处多个垂直分量的处理、生成点/范数截面的有效表示、局部高度分支以及最终 QC 共同零点排除仍须分别完成。

R12 作为充分构造仍正确，但其 §3 所述“一般不能除以 $d$”不应被继续解释为这个特殊 $\kappa_D$ 的障碍；§6 中的好约化平凡化存在问题也已由本结果解决。

## 8. 标准输入及出处

证明中的新恒等式和下降、范数、垂直除子步骤均已在上文展开。使用的标准背景是 Jacobian 自对偶性、Poincaré 双线性、相对 Jacobian 的阿贝尔概形性质及 Néron 映射性质。

- J. S. Milne, *Jacobian Varieties*, in *Arithmetic Geometry* (1986), §6；[作者修订版](https://jmilne.org/math/xnotes/JVs.pdf)。R12 已固定自对偶映射及符号。
- J. S. Milne, *Abelian Varieties*, course notes v2.00 (2008), Part I §§8, 16–17, Part III §6：[作者版本](https://jmilne.org/math/CourseNotes/AV.pdf)。
- S. Hashimoto, G. M. Lido, D. Lombardo, N. Mascot, P. Parent, *Equationless quadratic Chabauty for non-split Cartan modular curves* (2026), Remark 3.8：[arXiv:2608.10919](https://arxiv.org/abs/2608.10919)。这里只用于说明无有理基点问题的背景；上述证明不以该预印本的未公认结论为前提。
