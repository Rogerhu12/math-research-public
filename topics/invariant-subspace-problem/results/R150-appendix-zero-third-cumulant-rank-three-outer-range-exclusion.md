# R150 附录：第三累积量为零时的秩三外值域排除

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / literature；AI-assisted，GPT-6 Astra Pro。

**状态：以下整支排除已证明。** 在原六模式完整立方的任何完整临界点，不可能同时有
$$
V=0,\qquad \operatorname{rank}H=3,\qquad y\notin\operatorname{Ran}H.
\tag{0.1}
$$
这里 $V$ 是原第三累积量张量，不能与第三普通矩 $T_3$ 混同。证明不要求 mean catalecticant 的秩为三。

特别地，若 $V=0$ 且第三普通矩恰有四个本质变量，那么完整临界性迫
$$
\operatorname{rank}H=4,\qquad y\in\operatorname{Ran}H.
\tag{0.2}
$$
原 $y,H,V$ 因而确实有一个由 $H$ 唯一确定的准确长度四曲线 jet 公共支撑。此前不能从 $V$ 自己的低展平秩自动推出该公共支撑；本稿通过排除 (0.1) 支付了 $V=0$ 时的缺口。

## 1. 原对象、已核矩阵及完整梯度

沿用 [完整第三矩 Schur 稿](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md) 的六维原物理数据：
$$
K=
\begin{pmatrix}
0&0&0&0&5&-1\\
0&0&0&-32&5&-1\\
0&0&54&-4&5&0\\
0&-32&-4&-8&0&0\\
5&5&5&0&0&0\\
-1&-1&0&0&0&0
\end{pmatrix},
\qquad \det K=-25600,
$$
$$
v(z)=(1,z,z^2,z^3,z^4,z^5)^{\mathsf T},\qquad
F=\tfrac12y^{\mathsf T}Ky,\quad p=Ky.
\tag{1.1}
$$
所有向量、双线性配对和张量均在复数域上；转置不表示共轭转置。原二阶累积量为
$$
H=(H_{i+j})_{0\le i,j\le5},
$$
第三累积量为 $V_{ijk}=V_{i+j+k}$。第三普通矩是
$$
T_3(r)=(y^{\mathsf T}r)^3-6(y^{\mathsf T}r)H(r,r)+4V(r,r,r).
\tag{1.2}
$$

记
$$
b=p^{\mathsf T}Hp,\qquad h=Hp,\qquad
c=p^{\mathsf T}HKHp,\qquad
\tau_j=\operatorname{tr}((KH)^j).
\tag{1.3}
$$
原 Hankel 约束及 $K$ 的反对角线和为零给
$$
\tau_1=\operatorname{tr}(KH)=0.
\tag{1.4}
$$

在 $V=0$ 时，[完整低梯度稿](R150-appendix-four-jet-complete-low-gradients-and-projected-quadric.md) 的原 mean 梯度精确变为
$$
0=\frac13K^{-1}\nabla_y\mathcal Q_3
=Q_2\,y-4Fh+8HKh,
$$
$$
Q_2=F^2-2b+2\tau_2.
\tag{1.5}
$$
原十一个二阶梯度精确等价于
$$
v(z)^{\mathsf T}KNKv(z)\equiv0,
$$
$$
N=Fyy^{\mathsf T}-2FH
 -2(yh^{\mathsf T}+hy^{\mathsf T})+4HKH.
\tag{1.6}
$$
原十六个最高梯度精确给
$$
T_3(Kv(z))\equiv0.
\tag{1.7}
$$
本稿只使用这些完整梯度的必要推论；没有自由另选更高普通矩。

还使用原已经核验的矩阵
$$
(J_2)_{mn}=[z^m\zeta^n]\big(v(z)^{\mathsf T}Kv(\zeta)\big)^2,
\qquad 0\le m,n\le10.
\tag{1.8}
$$
上述 Schur 稿 §4 已记录
$$
\det J_2=-64701092257700249600\ne0.
\tag{1.9}
$$
这里没有重新启动矩阵计算或假设另一个映射可逆：对原 Hankel 坐标列 $\mathbf H=(H_0,\ldots,H_{10})^{\mathsf T}$，
$$
[z^m]\,v(z)^{\mathsf T}KHKv(z)
=(J_2\mathbf H)_m
\tag{1.10}
$$
直接由展开 (1.8) 成立。

## 2. 最高式唯一确定原 $H$，并固定二次迹

在 (0.1) 中 $y\ne0$。因为 $K$ 可逆且原曲线张成六维空间，
$$
P(z)=y^{\mathsf T}Kv(z)
$$
不是零多项式。令 $V=0$，(1.7) 因式分解为
$$
P(z)\left[P(z)^2-6v(z)^{\mathsf T}KHKv(z)\right]=0.
$$
复多项式环无零因子，故
$$
\boxed{\ P(z)^2=6v(z)^{\mathsf T}KHKv(z).\ }
\tag{2.1}
$$
记 $\mathbf d_2(y)$ 为 $P(z)^2$ 的十一维系数列，由 (1.9)–(1.10)，
$$
\boxed{\ \mathbf H=\frac16J_2^{-1}\mathbf d_2(y).\ }
\tag{2.2}
$$
因此这里的 $H$ 是同一个给定原 $y$ 的唯一二次函数，不是可以另调的低矩参数。

原合并键展开还给
$$
\mathbf d_2(y)^{\mathsf T}\mathbf H=b,\qquad
\mathbf H^{\mathsf T}J_2\mathbf H=\tau_2.
$$
将 (2.2) 代入，得到关键比例
$$
\boxed{\ \tau_2=\frac b6.\ }
\tag{2.3}
$$

## 3. 外值域 mean 与原二阶梯度强迫 $F=0$

置 $E=\operatorname{Ran}H$，当前 $\dim E=3$，且 $y\notin E$。取线性泛函 $\lambda$，使
$\lambda|_E=0,\lambda(y)=1$。因为 (1.5) 中除 $Q_2y$ 外的项都在 $E$，有
$$
Q_2=0.
\tag{3.1}
$$
由 (2.3)，
$$
\boxed{\ b=\frac35F^2,\qquad \tau_2=\frac1{10}F^2.\ }
\tag{3.2}
$$
剩余 mean 等式成为
$$
HKh=\frac F2h,\qquad
c=p^{\mathsf T}HKh=\frac F2b.
\tag{3.3}
$$

将原二阶梯度 (1.6) 与原 Hankel 坐标 $\mathbf H$ 收缩。由于该梯度的每个真实合并系数均为零，等价的张量收缩给
$$
0=\operatorname{tr}(KNKH)
=Fb-2F\tau_2-4c+4\tau_3.
\tag{3.4}
$$
(2.3)、(3.3) 因而给
$$
\boxed{\ \tau_3=\frac{Fb}{3}=\frac15F^3.\ }
\tag{3.5}
$$

反设 $F\ne0$。由 (3.2)，$b\ne0$，从而 $h\ne0$。因为 $H$ 是复对称秩三矩阵，可取满列秩的六乘三矩阵 $U$，使
$$
H=UU^{\mathsf T}.
\tag{3.6}
$$
令
$$
S=U^{\mathsf T}KU,\qquad a=U^{\mathsf T}p.
\tag{3.7}
$$
则 $h=Ua$，且循环迹给
$$
\operatorname{tr}S=0,\quad
\operatorname{tr}S^2=\tau_2,\quad
\operatorname{tr}S^3=\tau_3.
$$
由 (3.3)，$Sa=(F/2)a$，所以 $S$ 有特征值 $F/2$。记其余两个特征值为 $\sigma_1,\sigma_2$，只计代数重数，不假设 $S$ 可对角化。由迹和平方迹，
$$
\sigma_1+\sigma_2=-F/2,\qquad
\sigma_1^2+\sigma_2^2=-3F^2/20,
$$
故
$$
\sigma_1\sigma_2=F^2/5.
$$
于是
$$
\operatorname{tr}S^3
=\frac{F^3}{8}
 +(\sigma_1+\sigma_2)^3
 -3\sigma_1\sigma_2(\sigma_1+\sigma_2)
=\frac3{10}F^3.
$$
这与 (3.5) 的 $F^3/5$ 矛盾。因此
$$
\boxed{\ F=b=\tau_2=\tau_3=0,\qquad HKh=0.\ }
\tag{3.8}
$$
在 (3.6)–(3.7) 中，这意味着
$$
\operatorname{tr}S=\operatorname{tr}S^2
=\operatorname{tr}S^3=0,\qquad
a^{\mathsf T}a=0,\qquad Sa=0.
\tag{3.9}
$$

## 4. 若 $Hp\ne0$，二阶梯度变成不可能的两个线性因子

先设 $a\ne0$，即 $h\ne0$。使用一个三维复双线性事实：

**引理。** 若 $S$ 为三阶对称矩阵，$a\ne0$，且
$a^{\mathsf T}a=0,Sa=0,\operatorname{tr}S=0$，则存在 $z\in\mathbb C^3$，使
$$
S=az^{\mathsf T}+za^{\mathsf T}.
\tag{4.1}
$$

**证明。** 由对称性及 $Sa=0$，$\operatorname{Ran}S\subset a^\perp$，因此其对称张量属于 $\operatorname{Sym}^2(a^\perp)$。三维非退化标准双线性型中，$a^\perp$ 的根空间是 $\mathbb Ca$，商空间 $a^\perp/\mathbb Ca$ 一维非退化。取 $e\in a^\perp$ 使 $e^{\mathsf T}e\ne0$，则
$$
S=Aaa^{\mathsf T}+B(ae^{\mathsf T}+ea^{\mathsf T})+Cee^{\mathsf T}.
$$
前两项的迹为零，故 $\operatorname{tr}S=0$ 迫 $C=0$。取
$z=(A/2)a+Be$ 即得 (4.1)。$\square$

令 $z_0=Uz\in E$。由 (3.6)、(4.1)，
$$
HKH=USU^{\mathsf T}=hz_0^{\mathsf T}+z_0h^{\mathsf T}.
$$
将其与 $F=0$ 代入原 (1.6)，
$$
N=2\left[h(2z_0-y)^{\mathsf T}+(2z_0-y)h^{\mathsf T}\right].
$$
所以原二阶梯度恒等式成为
$$
4\big(h^{\mathsf T}Kv(z)\big)
 \big((2z_0-y)^{\mathsf T}Kv(z)\big)\equiv0.
\tag{4.2}
$$
但 $h\ne0$，且 $2z_0-y\ne0$，因为 $z_0\in E$ 而 $y\notin E$。原 $K$ 可逆、曲线张成整个空间，使 (4.2) 的两个因子都不是零多项式。矛盾。

故必须
$$
h=0,\qquad a=0.
\tag{4.3}
$$

## 5. 若 $Hp=0$，剩余二次式秩至多二，仍不可能

由 (3.9) 的三个迹恒等式及三阶 Newton 恒等式，
$S$ 的特征多项式为 $t^3$。因此 $S$ nilpotent，尤其
$$
\operatorname{rank}S\le2.
\tag{5.1}
$$
现在 (1.6) 简化为
$$
N=4HKH=4USU^{\mathsf T},\qquad
v(z)^{\mathsf T}KNKv(z)\equiv0.
\tag{5.2}
$$
若 $S\ne0$，由 $U$ 满列秩，$USU^{\mathsf T}$ 是非零、秩至多二的复对称矩阵。非零复二次式秩一时为线性式的平方，秩二时为两个非零线性式之积。因此 (5.2) 又给两个非零向量对应的物理线性多项式之积恒零，与 $K$ 可逆及原曲线张成性矛盾。故
$$
S=0,\qquad HKH=0.
\tag{5.3}
$$

最后，(5.3) 表示 $K$ 在 $E=\operatorname{Ran}H$ 上恒零；(4.3) 表示 $y$ 与 $E$ 正交；$F=0$ 表示 $y$ 自身等向。因此
$$
E+\mathbb Cy
$$
是四维 $K$ 全等向空间。非退化双线性型在六维空间中不可能有四维全等向子空间：若 $L\subset L^{\perp_K}$，则
$\dim L\le6-\dim L$。矛盾完成 (0.1) 的整支排除。

## 6. 对四个本质变量、第三累积量为零的精确后果

当 $V=0,y\ne0,\operatorname{rank}H\ge3$ 时，
$$
\operatorname{ess}(T_3)=\mathbb Cy+\operatorname{Ran}H.
\tag{6.1}
$$
为核对不会漏掉张量退化，若方向 $\ell$ 湮灭 $T_3$ 的一阶导数，记
$a_0=\ell(y)$、$u_0=H\ell$，则
$$
3a_0(y^{\mathsf T}r)^2-6a_0H(r,r)
-12(y^{\mathsf T}r)(u_0^{\mathsf T}r)=0.
$$
若 $a_0\ne0$，此式把 $H$ 写成含 $y$ 的两个对称乘积之和，秩至多二，矛盾。故 $a_0=0$，继而 $u_0=0$，正好证明 (6.1)。若 $\operatorname{rank}H\le2$，原显示式直接给本质维数至多三。

因此 $V=0,\dim\operatorname{ess}(T_3)=4$ 只有两种线性代数可能：
$$
\operatorname{rank}H=3,\ y\notin\operatorname{Ran}H;
\qquad
\operatorname{rank}H=4,\ y\in\operatorname{Ran}H.
$$
第一种已被完整临界性排除，只剩 (0.2)。

对后一种，原秩四 Hankel 矩阵定义二元十次矩泛函 $\Lambda:S_{10}\to\mathbb C$，其中 $S=\mathbb C[X_0,X_1]$。令
$
I_k=\{g\in S_k:\Lambda(gS_{10-k})=0\},\qquad
b_k=\dim(S_k/I_k).
$
原配对给 $b_k=b_{10-k}$，而 $b_5=4$。若 $a$ 是首次非零关系次数，则 $a\le5$，$b_{a-1}=a=b_{11-a}$。一旦 $I_k\ne0$，两移位不等式 $\dim(X_0I_k+X_1I_k)\ge\dim I_k+1$ 给 $b_{k+1}\le b_k$。由于 $a\le5\le11-a$，
$
a\ge b_5=4\ge b_{11-a}=a.
$
故 $a=4$，且 $b_4=4,\dim I_4=1$。这正是[原长度五归约](R150-appendix-essential-four-outer-mean-length-five-algebra-and-rank-defects.md) §2 的有限 apolar 论证在当前十次泛函上的直接应用，不添加矩延长假设。

唯一四次关系定义准确长度四的射影 divisor $D$。在避开支撑的坐标中，除法和局部中国剩余分解给原 $H$ 的完整曲线 jets 表示；每个最高局部 jet 系数均非零，否则关系次数会下降。长度四 jets 对二元五次式施加四个独立条件，故其曲线向量张成空间恰为 $\operatorname{Ran}H$。

由 $y\in\operatorname{Ran}H$，原一次矩也在同一个 $D$ 上；$V=0$ 无额外支撑。这包含全部重根类型及原无穷远点，没有正性或首主块非退化假设。

本稿尚未排除剩余秩四公共支撑支，也未处理一般 $V\ne0$ 的 inner-mean 退化。没有由这个局部排除宣称完整 Bell 幂证书或普通 Hilbert 不变子空间结论。
