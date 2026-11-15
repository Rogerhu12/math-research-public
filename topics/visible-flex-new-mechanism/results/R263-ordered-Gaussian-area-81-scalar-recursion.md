# R263：全部 Gaussian 面积的 81 标量有序组合律

日期：2026-11-15。独立纸面接口；没有编写消费者、求积、消元或执行 profile 构造。本文只使用 [R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 已证的原式与三类跨包核。

## 1. 状态保存什么

固定同一个物理区间、同一个右锚、同一个例外端芽参数 $(h_e,\kappa,\varepsilon)$，以及 R259 的六对 Gaussian 算子 $(B_r,B_s)$。不能把不同端芽或不同锚的状态直接相加。

一个 partial block 是在某个紧包络内给定的实 pair $(f,g)$。它暂时可以不满足三矩圆，也可以不是一个单独合法第三阶构造。状态仅描述这个真实 profile 片段的原面积数据，不把它冒称为可独立执行的几何成本。

先保存九个二次矩：

$$
F=\mathbf I(f,f),\qquad K=\mathbf I(f,g),\qquad G=\mathbf I(g,g)
\quad\in\mathbb R^3.
\tag{1}
$$

这里 $\mathbf I=(I_0,I_1,I_2^*)$ 保留第三分量的 $2f'g'$。令

$$
O_M(\theta)=F\cos^2\theta+2K\cos\theta\sin\theta+G\sin^2\theta,
$$

$$
D_M(\theta)
=(F-G)\sin^2\theta-2K\cos\theta\sin\theta.
\tag{2}
$$

它们分别是 $\mathbf I(\phi_\theta,\phi_\theta)$ 及原 inner 槽
$f\odot f-\phi_\theta\odot\phi_\theta$ 的三矩。

对每个 $r>s$，保存真实三外矩向量

$$
T_{r,s}(\theta)
=2\mathbf I\{\phi_\theta,[B_r,B_s](\phi_\theta;D_\theta)\}.
\tag{3}
$$

按 R259，它准确写成

$$
T_{r,s}(\theta)
=T_{31}\cos^3\theta\sin\theta
+T_{22}\cos^2\theta\sin^2\theta
+T_{13}\cos\theta\sin^3\theta
+T_{04}\sin^4\theta,
\tag{4}
$$

每个 $T_{ab}\in\mathbb R^3$。六对各保存十二个实数，共 72 个。连同 (1)，一个已经固定实际放置的 block 需 **81 个实标量**。

支撑位置、左右先后、原母包与参数身份是必要的外部元数据，不包含在这 81 个数中。标量个数不是实际独立维数的宣称。

## 2. 原式给出的组合，而非形式截断

若 block $A$ 的整个包络在 block $B$ 左侧，令 $A\star B$ 表示原 profile 的不交并置：

$$
(f,g)=(f_A+f_B,\ g_A+g_B).
$$

二次矩当然相加。R259 的 local adjoint 恒等式及真实二次左尾进一步给

$$
\boxed{
T_{r,s}(A\star B;\theta)
=T_{r,s}(A;\theta)+T_{r,s}(B;\theta)
+\Gamma_{r,s}\{O_{M_A}(\theta),D_{M_B}(\theta)\}.
}
\tag{5}
$$

$\Gamma_{r,s}$ 是 R259 第 6 节已经明确列出的双线性三向量核；其中三对为零，另三对由 $\mathbf K_1,\mathbf K_2,\mathbf K_3$ 给出。

式 (5) 的方向不能互换。在 $A$ 的支撑上，$B$ 的 inner 二次场是其真实二次左尾；在 $B$ 的支撑上，$A$ 的二次场处于准确右零 collar。这正是只有 $O_{M_A}$ 与 $D_{M_B}$ 的原因。没有删除任何包内 history，也没有把任意左尾改成零。

特别，(5) 对 partial block 也成立，不需要先求其三矩闭合。所用是 R259 已支付的 cutoff/local adjoint 形式，不是只在 diagonal 才成立的 cubic 变分抵消。

## 3. 四个可直接使用的交叉系数

写 $F_A,K_A,G_A$ 和 $F_B,K_B,G_B$。式 (5) 的交叉增量准确为

$$
\boxed{
\begin{aligned}
C_{31}(A,B)&=-2\Gamma(F_A,K_B),\\
C_{22}(A,B)&=\Gamma(F_A,F_B-G_B)-4\Gamma(K_A,K_B),\\
C_{13}(A,B)&=2\Gamma(K_A,F_B-G_B)-2\Gamma(G_A,K_B),\\
C_{04}(A,B)&=\Gamma(G_A,F_B-G_B).
\end{aligned}}
\tag{6}
$$

每一行都是三向量；对六对 $(r,s)$ 分别使用自己的同一 $\Gamma_{r,s}$。这只是将 (2) 的两个真实二次三角多项式相乘：

$$
(F_Ac^2+2K_Acs+G_As^2)
\quad\text{配}\quad
((F_B-G_B)s^2-2K_Bcs).
$$

故 (6) 包含全部四次角项，不是若干角度的采样。

## 4. 结合律与递归聚合

二次矩映射 $M\mapsto O_M,D_M$ 都是线性的，$\Gamma$ 为双线性。置

$$
C(M,N;\theta)=\Gamma(O_M(\theta),D_N(\theta)).
$$

则逐个原函数恒等地有

$$
C(M,N)+C(M+N,P)=C(N,P)+C(M,N+P).
\tag{7}
$$

两边都恰为 $C(M,N)+C(M,P)+C(N,P)$。因此

$$
\boxed{(A\star B)\star C=A\star(B\star C)}
\tag{8}
$$

在全部 81 个原标量上成立。它来自真实有序并置，不是忽略高阶项的近似代数。

空 block 是零状态。一般不交换：$A\star B$ 与 $B\star A$ 的交叉项不同，实际次序改变必须按 (5) 重算。也没有由该结合律授予实际逆元、负成本或任意 signed block；真实二次矩特别含非负的 $I_0(f,f),I_0(g,g)$。

给定有 $N$ 个微包或完整子块的已选有序构造，可以依任意保持叶子先后顺序的二叉树聚合。只需每个节点应用 (1)、(6)，不必逐对枚举 $N(N-1)/2$ 个尾相互作用。若构造有准确重复/差分结构，可进一步在相同原参数身份下复用子状态。本文不执行这种聚合，也不预填任何研究数值。

## 5. 什么时候交叉项真的为零

若右方 inner block $B$ 已满足三矩圆，

$$
F_B=G_B,\qquad K_B=0,
$$

则 $D_{M_B}(\theta)=0$ 对所有 $\theta$，所以 (5) 的交叉项准确为零。两个完整三矩 block 并置时当然满足这一充分条件。

这是有方向的结论。只有左方 block 满足三矩圆，而右方尚未闭合时，一般不能清掉交叉项。某个特殊 $\Gamma$ 或特殊数据也可能偶然给零；本文不把上述充分条件说成所有零的必要条件。

因此，R259 十二副本的准确加法可使用完整子块的状态。但在一个完整子块内部，原微包通常没有零三矩，必须保留 (6)；这正是 R257 的累计 primitive 项不能逐微包删掉的原因。

## 6. 准确的幅度和符号作用

对整个 block 作共同实幅度 $\gamma$，

$$
(F,K,G)\mapsto\gamma^2(F,K,G),\qquad
T_{ab}\mapsto\gamma^4T_{ab}.
\tag{9}
$$

对 $g\mapsto-g$，

$$
K\mapsto-K,\qquad
(T_{31},T_{13})\mapsto-(T_{31},T_{13}),
$$

$$
F,G,T_{22},T_{04}\quad\text{不变}.
\tag{10}
$$

这两种作用与 (5) 相容，足以准确接入 R183 的完整幅度副本及 R259 的十二副本 odd 消去。第三阶张量的幅度因子仍需在其自身来源中按三次齐次保留；它不包含在本状态的 72 个第四量里。

本状态没有自动记录任意重新选 seed 的正交旋转所需的全部双二次张量。不能仅凭这 81 个值就对未授权的一般 $O(2)$ 换种子作状态变换。当前已证明且使用的是 (9)、(10)。

## 7. 平移、多宽度与同一母包常数

对一个已有状态，九个二次矩的共同平移有已知三角变换：

$$
(m_0,m_1,m_2)\mapsto
(m_0,m_1+dm_0,m_2+2dm_1+d^2m_0).
\tag{11}
$$

但这并不从单个位置的 72 个数恢复其任意平移值。R259 证明的是原各面积系数对共同平移为次数至多 10 的多项式；若要递归复用平移副本，应先从原来源取得这个**完整多项式呈示**，或从该副本的准确叶子参数组成状态。不能用一次数值替代全部平移系数。

对固定实母包 $u$ 的真实宽度族
$\eta_{w,\zeta}=w^{3/2}u((x-\zeta)/w)$，每个叶子的三个矩与六个原 self 三向量都必须由同一母包的原积分常数生成。R259 的 24 个 local cubic 密度、local adjoint 及原八二次式提供该完整定义。改变母包形状参数时，所有这些常数都随同一真实母包变化；不得只更新 $S/C$ 或若干局部四次矩而冻结其余 self 数据。

因此，多项式或 Laurent 呈示版本的 (5)—(7) 仍是同一准确结合律，可用于层级汇总大量已指定微包。它不要求恢复旧第四 forcing，也不把原积分常数视为任意可调的自由变量。若未来要取得新实际数值、秩或可行性结论，仍须在公开 Actions 中按被冻结的真实来源计算；本文没有做这一步。

## 8. 结论范围

本接口保留同一右锚、全部真实左右尾、整圆相位、三外矩及六个 Gaussian 面积。它使 R256 一类大有限构造的剩余 30 个 even 条件可以按原顺序递归评估，而无需重编原 forcing 或遗漏累计项。

它不证明这 30 条条件独立、可解或不可解，也不由它们清零推出完整第四 ruling/period。只有实际完整三矩子块才享有已经支付的跨项消失；内部 history 和真实母包常数始终存在。

