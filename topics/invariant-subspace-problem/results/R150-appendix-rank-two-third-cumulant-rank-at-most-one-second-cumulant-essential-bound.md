# R150 附录：秩二第三累积量与秩至多一二阶累积量不产生本质四维临界点

日期：2026-11-26（UTC）。作者：Astra-ISP-347c-20261126 / prior_results_map；AI-assisted GPT-6 Astra Pro。

**状态：已证明。** 原完整临界点若 $\operatorname{rank}V=2$、$\operatorname{rank}H\le1$，则 $\dim\operatorname{ess}(T_3)\le3$。结论包括第三累积量的两个不同点和二重 jet、全部无穷远及任意原均值。没有预设 $y$ 或 $H$ 与 $V$ 共支撑。

## 1. 完整结论和原梯度

仍用原六模式非退化对称矩阵 $K$、曲线 $u(a,b)$、Hankel 累积量和
$$
T_3=y^{\otimes3}-2\operatorname{Sym}_{\Sigma}(y\otimes H)+4V.
$$
$K$、$J_2$、完整 $\mathcal Q_3$ 及全部偏导定义见[原完整矩公式](R150-appendix-six-mode-cubic-bell-third-moment-schur-reduction.md)。特别
$$
\det K=-25600,\qquad \det J_2=-64701092257700249600.
$$
不对这些对象作改变。

**定理。**
$$
\nabla\mathcal Q_3=0,\quad
\operatorname{rank}V=2,\quad
\operatorname{rank}H\le1
\quad\Longrightarrow\quad
\dim\operatorname{ess}(T_3)\le3.
\tag{1.1}
$$
因此由[本质维数至多三的完整 Bell 零性定理](R150-appendix-all-essential-cubic-dimensions-at-most-three-have-zero-matched-bell-values.md)，三个原匹配 Bell 值在整个范围均零。这不是统一自然幂或算子证书。

记
$$
p=Ky,\quad F=\tfrac12y^{\mathsf T}Ky,\quad
b_0=p^{\mathsf T}Hp,\quad \tau_2=\operatorname{tr}((KH)^2).
$$
完整原低梯度为
$$
\Gamma=(F^2-2b_0+2\tau_2)y-4FHp+8HKHp
       +4V(p,p,\cdot)-8V:(KHK),
\tag{1.2}
$$
$$
N=Fyy^{\mathsf T}-2FH-2\{y(Hp)^{\mathsf T}+(Hp)y^{\mathsf T}\}
 +4HKH+4V_p,
\tag{1.3}
$$
$$
\nabla_y\mathcal Q_3=3K\Gamma,\qquad
-\tfrac16\partial_{H_m}\mathcal Q_3
=[z^m]u(z)^{\mathsf T}KNKu(z).
\tag{1.4}
$$
这里 $V_p=V(p,\cdot,\cdot)$ 是一条对称二阶张量，$V:(KHK)$ 表示对两个指标的完整收缩。

任意 $p$ 下 $V_p$ 都是原 Hankel 矩阵，因为
$$(V_p)_{ij}=\sum_kp_kV_{i+j+k}$$
只依赖 $i+j$。但一般 $N$ 不为 Hankel；下面只在原方程已经将它化为 $4V_p$ 之后使用 $J_2$ 可逆性。

## 2. 一条所需的原极线根重数事实

对不同物理点 $s,t$，
$$
k_s(t)=0\quad\Longrightarrow\quad
1\le\operatorname{ord}_t k_s\le2.
\tag{2.1}
$$
这是异点断言，不限制原自接触阶数。

有限图中 $k_s(z)=-(z-s)^2q_s(z)$，所以异点根的重数就是原三次 $q_s$ 的重数。其判别式为 $s^2D(s)$，其中 $D$ 是已登记八次式。[秩一完整分类](R150-appendix-rank-one-third-cumulant-complete-critical-classification.md) §6 已在整个 $\mathbb Q[s]/(D)$ 准确核出
$q_s=a_3(z-\alpha)^2(z-\beta)$，并给 $a_3,\alpha-\beta$ 的逆；所以 $D$ 的任何复根都只有一个二重根和一个不同单根，没有三重根。$s=0$ 时 $q_0=z^2(z-5)$。$s=-1$ 时原齐次三次式是
$-a(6a^2+26ab+5b^2)$，其三个射影根各自简单。其余有限点没有重根。

在 $s=\infty$，$k_\infty(a,b)=-a^4(a+b)$，唯一异点根为 $-1$，且简单。若 $t=\infty$、$s$ 有限，共同值为零只可能 $s=-1$，原无穷远根仍简单。这证明 (2.1)，包含全部射影边界；不重跑任何已付判别式门。

## 3. 完整原低梯度把假想本质四空间压到三个特殊条件

令 $U=\operatorname{Ran}V$，$\dim U=2$。若 $H=0$，$T_3$ 已由 $\mathbb Cy+U$ 支撑，维数至多三，结论立即成立。

现在 $\operatorname{rank}H=1$。原 Hankel 秩一表示给
$$
H=h\,zz^{\mathsf T},\qquad h\ne0,\qquad z=u(t)
$$
为某个物理点的非零代表，允许 $t=\infty$。该表示亦是[有限低秩 Hankel jet 引理](R150-appendix-length-three-common-jets-and-inside-mean-critical-dichotomy.md) §6 的秩一情形。

反设 $\operatorname{ess}(T_3)$ 至少四维。由于
$$
T_3\text{ 支持于 }E=\mathbb Cy+\mathbb Cz+U,\qquad \dim E\le4,
$$
必有 $\dim E=4$；尤其 $y,z$ 在模 $U$ 后线性无关。这一独立性是反设推出的，不是对原参数的新增要求。

置 $P_z=p^{\mathsf T}z$。物理自等向关系 $z^{\mathsf T}Kz=0$ 给
$$
HKH=0,\quad \tau_2=0,\quad Hp=hP_z z,\quad b_0=hP_z^2.
$$
(1.2) 的最后两项都在 $U$ 内。比较独立的 $y,z$ 系数得到
$$
F^2-2hP_z^2=0,\qquad FP_z=0.
$$
因为 $h\ne0$，准确推出
$$
\boxed{F=0,\qquad P_z=0.}
\tag{3.1}
$$

此时 (1.3) 化为 $N=4V_p$，它确为原 Hankel 矩阵。(1.4) 和原 $J_2$ 可逆性便给
$$
V_p=0.
$$
对称第三张量的展平核是其本质像的湮灭子，所以
$$
\boxed{p|_U=0.}
\tag{3.2}
$$
也可分别从两个原子或一个二jet的显示张量直接比较系数，得到同一结论。

在 (3.1)、(3.2) 上，完整 mean 式剩下
$$
\boxed{V(Kz,Kz,\cdot)=0.}
\tag{3.3}
$$
这里已保全部原三阶贡献，没有把仅投影为零的矩阵误作零矩阵。接下来分别处理秩二 $V$ 的全部两种物理类型。

## 4. 两个不同点：极大全等向空间矛盾

写
$$
V=c\,u^{\otimes3}+d\,v^{\otimes3},\qquad cd\ne0,
$$
其中 $u,v$ 是两个不同物理点。由 (3.2)，
$$
p^{\mathsf T}u=p^{\mathsf T}v=0.
$$
(3.3) 则是
$$
c(z^{\mathsf T}Ku)^2u+d(z^{\mathsf T}Kv)^2v=0.
$$
$u,v$ 独立，故
$$
z^{\mathsf T}Ku=z^{\mathsf T}Kv=0.
\tag{4.1}
$$

将原最高式
$$
P(x)^3-6P(x)G_H(x)+4V(Ku(x),Ku(x),Ku(x))=0
\tag{4.2}
$$
在 $x$ 为 $u$ 的物理源时评价。前两项因 $p^{\mathsf T}u=0$ 为零，$c$ 项因 $u^{\mathsf T}Ku=0$ 为零，留下
$$
4d(v^{\mathsf T}Ku)^3=0.
$$
所以 $u^{\mathsf T}Kv=0$。

由 $\dim E=4$，$z,u,v$ 三列独立。它们自配对及两两配对全为零，因此
$$
L=\operatorname{span}\{z,u,v\}
$$
是三维全等向空间。$K$ 在六维上非退化，故 $L^{\perp_K}=L$。而 (3.1)、(3.2) 给 $y\perp_K L$，所以 $y\in L$，与 $\dim E=4$ 矛盾。全部两点型被排除。

## 5. 一个二重点：原最高式的唯一最低阶矛盾

写全部非约化型为
$$
V=c u^{\otimes3}
+d(u\otimes u\otimes w+u\otimes w\otimes u+w\otimes u\otimes u),
\qquad d\ne0,
\tag{5.1}
$$
其中 $u=u(s)$、$w$ 是原非零切向代表，$c$ 可零。由 (3.2)，
$$
p^{\mathsf T}u=p^{\mathsf T}w=0.
$$
在 (3.3) 中比较 $w$ 系数，得到
$d(z^{\mathsf T}Ku)^2=0$，故
$$
z^{\mathsf T}Ku=0.
\tag{5.2}
$$
令 $\ell=z^{\mathsf T}Kw$。

在独立基 $(y,u,z,w)$ 中，(3.1)、(3.2)、(5.2) 及物理关系
$uKu=uKw=zKz=0$ 使原 Gram 矩阵为
$$
K|_E=
\begin{pmatrix}
0&0&0&0\\
0&0&0&0\\
0&0&0&\ell\\
0&0&\ell&w^{\mathsf T}Kw
\end{pmatrix}.
\tag{5.3}
$$
任何四维子空间在非退化六维型中的限制秩至少二，因为
$\operatorname{rad}(K|_E)\subset E^{\perp_K}$，后者只有二维。
若 $\ell=0$，(5.3) 的秩至多一，矛盾。因此
$$
\ell\ne0.
\tag{5.4}
$$

在 $z=u(t)$ 的物理源处选任意非零局部齐次平凡化，记
$$
A(x)=u^{\mathsf T}Ku(x),\quad
B(x)=w^{\mathsf T}Ku(x),\quad
C(x)=z^{\mathsf T}Ku(x),\quad
P(x)=y^{\mathsf T}Ku(x).
$$
由于四列独立，$t\ne s$。由 (5.2) 和 (2.1)，
$$
m=\operatorname{ord}_tA\in\{1,2\}.
$$
而 (5.4) 给 $B(t)=\ell\ne0$，物理自接触给
$$
r=\operatorname{ord}_tC\ge2.
$$
(3.1) 给 $P(t)=0$；$P$ 非零，因为 $y\ne0$ 且 $K$ 可逆，所以
$$
n=\operatorname{ord}_tP\ge1.
$$

原最高恒等式此时正是
$$
P^3-6hPC^2+4A^2(cA+3dB)=0.
\tag{5.5}
$$
三项在 $t$ 的准确阶数分别为
$$
3n,\qquad n+2r\ge n+4,\qquad 2m\in\{2,4\}.
\tag{5.6}
$$
第三项的阶数准确为 $2m$，因为其括号在 $t$ 为 $3d\ell\ne0$。

若 $n=1,m=1$，第三项是唯一二阶首项；若 $n=1,m=2$，第一项是唯一三阶首项。若 $n\ge2$，第三项阶数至多四，另两项均至少六，仍只有一个最低非零首项。这三种情况穷尽全部可能，与恒等式 (5.5) 矛盾。

该局部阶数证明直接适用于 $s$ 或 $t$ 为无穷远的情形，且 §2 已支付异点根重数，没有遗漏仿射降次或额外三重根。二jet型也全部排除。

## 6. 完成与下一层的准确范围

两个类型穷尽原 rankV2 Hankel 第三张量。因此 $\dim E=4$ 的反设不可能，必有 $\dim\operatorname{ess}(T_3)\le3$，定理证毕。然后用已登记的本质维数至多三定理取得三个原匹配 Bell 值为零。

本稿只用显示的完整原梯度、$J_2$ 的既有准确逆、原异点根重数及六维非退化型的维数恒等，没有新的计算执行或未验证数值证据。已有判别式与低本质维数门均不重跑。

结合[rankV2全部内均值分类](R150-appendix-rank-two-third-cumulant-all-inside-mean-complete-classification.md)，潜在非零原匹配 Bell 的 rankV2 临界点现在必须同时满足
$$
\boxed{
y\notin\operatorname{Ran}V,\qquad
\operatorname{rank}H\ge2,\qquad
\dim\operatorname{ess}(T_3)\ge4.
}
$$
这些是已证明的必要条件，未把剩余高二阶秩临界点当作空集。原全局自然幂、实际算子桥与普通 Hilbert ISP仍未完成。

