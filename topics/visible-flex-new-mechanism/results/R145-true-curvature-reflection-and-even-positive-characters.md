# R145：保持右锚的真实曲率反号、负缩放代数延拓与奇权正字符排除

日期：2026-11-15。**已证明。** 本稿只作纸面推导；不运行新的 profile、几何或完整原式计算。

依据 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R127](R127-positive-affine-character-of-the-fourth-cost-cone.md) 与 [R141](R141-affine-character-acceleration-covariance-and-J-positivity.md)。

本稿证明：把真实路径的 $k,\omega$ 同时反号、保持 $h>0$，其完整 canonical 第四成本等于有限 Laurent 缩放表示在 $H=-1$ 的**代数延拓**。这一身份逐步来自 R56 的分子恢复，始终保持同一右锚。它不把实际 profile 镜像后出现的左锚误认成右锚，也不声称物理几何允许 $h<0$。

由此，真实成本闭凸锥在真权奇偶 involution 下不变。任何非零正仿射字符的整权必须是偶数。特别，R141 的权 $-2$ 门仍然保留，新方向 $J$ 没有因此被迫成为双向可调成本。

## 1. 负缩放的准确代数含义

对一个正次数右 Volterra 模板，沿用

$$
I_rF(\xi)=\int_r^\xi F(\eta)\,d\eta.
$$

所有节点仍使用同一个实际右端 $r$。R105 给完整成本的共同有限模板空间；正缩放作用为

$$
(\mathsf P_{H,0}V)(f,g)(\xi)
=V(C_{H,0}f,C_{H,0}g)(H\xi),\qquad
C_{H,0}f(x)=f(x/H),\quad H>0.
\tag{1}
$$

在原表达式上，(1) 的规则是

$$
\xi\mapsto H\xi,\qquad
q^{(j)}\mapsto H^{-j}q^{(j)},\qquad
I(F)\mapsto H I(\mathsf P_{H,0}F).
\tag{2}
$$

$r$ 与支撑在正缩放的真实输运中同时变换，因此 (2) 保留准确的原函数常数。每个节点有正 profile 次数，故将右锚移到更右的空区也不改变模板。

固定有限模板后，(2) 是 $H$ 的有限 Laurent 多项式。定义

$$
\boxed{\mathsf S=\mathsf P_{-1,0}^{\mathrm{alg}}}
\tag{3}
$$

为这个 Laurent 表示在 $H=-1$ 的代数取值。等价的递归规则为

$$
\mathsf S\xi=-\xi,\qquad
\mathsf S q^{(j)}=(-1)^j q^{(j)},\qquad
\mathsf S I(F)=-I(\mathsf SF).
\tag{4}
$$

颜色 $q,\bar q$、所有实输入槽以及常数均保持；与复共轭交换。

**(3) 下降到真实函数空间，而不只是语法树。** 若一个有限模板线性组合是真算子零式，对每个 $H>0$，其真实输运 (1) 仍为零。固定任意输入与查询，乘适当 $H$ 正幂后得到一个在全部正 $H$ 上为零的普通多项式；因此各系数为零，在 $H=-1$ 也为零。这对所有输入与查询成立，故 (3) 不依赖原模板表示。

所以在 $U=\mathcal U_4$ 及相应有限低阶算子空间上，$\mathsf S$ 是准确的实线性 involution，并在真权 $\sigma$ 上作用为

$$
\mathsf S|_{U_\sigma}=(-1)^\sigma\operatorname{id}.
\tag{5}
$$

这里没有通过不完备的正规形判等。也没有将 (3) 定义为“实际把 profile 支撑镜像到另一侧并重置锚”。后者会交换端点，具有不同的边界问题。

## 2. 一条始终满足 h 正的真实路径

设真实标量路径满足

$$
h>0,\qquad \omega_s=\frac{k_s}{2h},
$$

标架 $F=(T,N,B)$ 满足

$$
F_s=F\Omega(k),\qquad
\Omega(k)=
\begin{pmatrix}0&-k&0\\k&0&1\\0&-1&0\end{pmatrix},
\qquad \alpha_s=h^2T.
$$

置

$$
E=\operatorname{diag}(-1,1,1),\qquad
h^\sharp=h,\quad k^\sharp=-k,\quad\omega^\sharp=-\omega,
$$

$$
F^\sharp=E F E,\qquad \alpha^\sharp=-E\alpha
\tag{6}
$$

（中心线的起点可另加常向量）。虽然 $\det E=-1$，$F^\sharp$ 仍为正定向正交标架，且

$$
\Omega(-k)=E\Omega(k)E,
\qquad (\alpha^\sharp)_s=h^2T^\sharp,
\qquad (\omega^\sharp)_s=\frac{(k^\sharp)_s}{2h}.
\tag{7}
$$

因此 (6) 是一条真实合法路径，$h$ 没有变号；时间方向及长度也没有改变。初、末 frame 都为 I 的路径仍具有这个性质。常值 scalar germs 与全部平坦端 jets 按 (6) 真实变换。

若原末 frame 为 A，新末 frame为 $EAE$。本证明不把它与 R45 的时间倒行 $D A^{-1}D$ 混用。

对任何所需的有限路径或紧小族，原路径与 (6) 的 $\omega$ 都有界，可以随后选择共同物理区间，使两者的 $\xi+\omega$ 都有正间隙。不存在预先固定任意窄区间的额外承诺。

## 3. 完整分子递推的联合奇偶

以 $\Gamma$ 表示只对几何数据作 (6) 的代换，令

$$
\mathcal J=\Gamma\mathsf S.
$$

$\Gamma$ 与 $\mathsf S$ 交换。记 R56 的

$$
z=\xi+\omega,\quad e=hz-k,\quad
\gamma=h_s,\quad\nu=k_s/(2h),
$$

$$
\lambda=\frac{\gamma z-h\nu}{h^2},\qquad
K_0=kz^2-\frac{k^2+1}{h}z.
$$

则

$$
\mathcal Jz=-z,\quad\mathcal Je=-e,\quad
\mathcal J\gamma=\gamma,\quad\mathcal J\nu=-\nu,
\quad\mathcal J\lambda=-\lambda,\quad\mathcal JK_0=-K_0.
\tag{8}
$$

与 $s$ 微分、真实 $s$ 积分交换；与 profile 微分和右原函数满足

$$
\mathcal JD_\xi=-D_\xi\mathcal J,\qquad
\mathcal JI=-I\mathcal J.
\tag{9}
$$

初始场分子为

$$
V_{Y_f}=(-f'/2,\ 0,\ hf-ef'/2).
$$

直接代 (4)、(8) 得

$$
\mathcal J V_{Y_f}=E V_{Y_f}.
\tag{10}
$$

任一输入槽均同样成立。

假设某一次恢复所用各场分子都满足 $\mathcal JV_i=EV_i$。由于 (7)，真实协变导数满足

$$
\mathcal J(\nabla_sV_i)=E\nabla_sV_i.
$$

因此对任意既定常系数对称二次 forcing，分子配对的奇偶为

| 分子量 | 联合奇偶 |
|---|---:|
| $J=\sum c_{ij}V_i\cdot V_j$ | 偶 |
| $T_\xi=\sum c_{ij}(V_i)_\xi\cdot(V_j)_\xi$ | 偶 |
| $T_s=\sum c_{ij}\nabla_sV_i\cdot\nabla_sV_j$ | 偶 |
| $T_{s\xi}$ | 奇 |

R56 的真实右锚恢复是

$$
P=-\frac1{2h}I(T_\xi),\qquad B=\frac{J}{2h},
$$

$$
\mathcal R_H=
\frac{T_s}{2h^2}+K_0P-\lambda P_s+
\frac{K_0}{z}B-\frac{\gamma}{h^2}B_s,
\tag{11}
$$

$$
\eta_0=-\frac{T_{s\xi}}{2h}
+\frac{\gamma z-h\nu}{2h}P_\xi
+\frac{\gamma}{2h}B_\xi-\frac12P_s.
\tag{12}
$$

由 (8)–(9)，$P$ 奇、$B$ 偶，$P_\xi$ 偶、$B_\xi$ 奇。逐项代入而非丢弃边项，得到

$$
\boxed{\mathcal J\mathcal R_H=\mathcal R_H,\qquad
\mathcal J\eta_0=-\eta_0.}
\tag{13}
$$

从同一个 $s$ 起点、零 scalar 传入值定义

$$
W(s,\xi)=\int_0^s\mathcal R_H(\sigma,\xi)\,d\sigma,
\qquad A=W_\xi/2+\eta_0/h.
$$

则 $W$ 偶、A 奇，故新分子

$$
V_{\mathrm{new}}=(A,\ zP+B,\ eA-hW)
$$

再次满足

$$
\boxed{\mathcal JV_{\mathrm{new}}=EV_{\mathrm{new}}.}
\tag{14}
$$

(14) 完成逐阶归纳。第二、第三场及完整第四 forcing 都适用；在模式分解中出现的实或复常系数不改变它。累计历史全程保留，未在接缝重锚，未将任何 $s$ 导数中的真实历史 RHS 先置零。

## 4. 完整实际成本的身份

由 (13)，标量 characteristic RHS 及其真实 $s$ 积分满足 $\Gamma\mathsf S R=R$。再用 $\mathsf S^2=1$，得到

$$
\boxed{M_{P^\sharp}=\mathsf S M_P,\qquad
T_{P^\sharp}=\mathsf S T_P,\qquad
V_{P^\sharp}=\mathsf S V_P.}
\tag{15}
$$

前三者分别按各自输入槽理解同一个有限 Laurent 作用。它们是同一 canonical 右锚、零传入历史下的完整算子身份，不是只对 pure 模式或幂尾投影的身份。

特别，若 P 是实际同端口、frame I、$M=T=0$ 的成本路径，$P^\sharp$ 仍满足这些条件（端口改为 $g^\sharp$），其完整两模式成本正是 (3)。原始右锚没有换到左端，低阶 ruling 也没有被假定已经支付。

应区分两个不同操作：

- 实际将输入函数 $f(\xi)$ 镜像成 $f(-\xi)$，再尝试换端口，通常会涉及左右锚差；
- 本文 (15) 保持原输入函数和右锚，改真实几何，并由有限正缩放表示的负值代数延拓描述输出。

本稿只证明第二项。其合法性已由原恢复公式的全部符号和真实路径 (6) 共同支付。

## 5. 闭成本锥的基点无关与奇偶不变

固定常值 germ g，记 $\mathcal S_g$ 为实际同端口、frame I、$M=T=0$ 路径的完整第四成本集合，并置

$$
\mathcal C_g=\overline{\operatorname{cone}(\mathcal S_g)}\subset U.
$$

这是有限维真实函数空间中的闭凸锥，不是实际可取任意实倍的半群。

首先补清基点无关。若 B 是 $g_1$ 上的实际零矩零第三路径，取 R70 的实际 $M=0$、frame I 桥 $C:g\to g_1$。R83 的真实零矩传递与真倒行给，对任意正整数 n，

$$
M_{CB^nC^R}=T_{CB^nC^R}=0,
\qquad V_{CB^nC^R}=2V_C+nV_B.
$$

故

$$
V_B=\lim_{n\to\infty}\frac{V_{CB^nC^R}}n\in\mathcal C_g.
$$

反向连接同样成立，因而所有 $\mathcal C_g$ 相同，记作 $\mathcal C$。这里只取闭锥极限，没有把 $-2V_C$ 当作可实际减去的成本。

由 (15) 及 $\mathsf S^2=1$，

$$
\boxed{\mathsf S\mathcal C=\mathcal C.}
\tag{16}
$$

同时 R105 的定义给 $\operatorname{span}\mathcal C=U$。

## 6. 非零正仿射字符只能有偶整权

设实泛函 $\ell\in U^*$ 满足

$$
\ell(\mathcal C)\ge0,\qquad
\ell\circ\mathsf P_{H,d}=H^\sigma\ell
\quad(H>0),\qquad\sigma\in\mathbb Z.
\tag{17}
$$

由于真实作用为有限 Laurent 表示，(17) 在 $d=0$ 的恒等式同样可代数延拓到 $H=-1$。于是

$$
\ell\circ\mathsf S=(-1)^\sigma\ell.
\tag{18}
$$

若 $\sigma$ 为奇数，(16) 表明 $-\ell=\ell\circ\mathsf S$ 也是非负泛函。因此 $\ell$ 在 $\mathcal C$ 上同时非负、非正，只能为零；又 $\operatorname{span}\mathcal C=U$，遂

$$
\boxed{\sigma\text{ 为奇数且 (17) 成立}\ \Longrightarrow\ \ell=0.}
\tag{19}
$$

结合 R127：若 $\mathcal C\ne U$，必有一个非零正仿射字符，且其最终整权是偶数。R127 中最后的 $N^*$ 迭代可改变权；(19) 约束的是实际得到的最终字符，不声称迭代始终保持初始权。

另一个无需先取单权的推论是：若 $\ell\ne0$ 为任一正泛函，则

$$
\ell_{\mathrm{even}}=\frac12(\ell+\ell\circ\mathsf S)
$$

仍为非零正泛函。若其为零，则 $-\ell=\ell\circ\mathsf S$ 也正，与上述 span 论证矛盾。

## 7. 保留的真实边界

本稿使剩余 universal 闭锥正性问题只需寻找偶权正字符，但不排除任何偶权；特别 R141 的权 $-2$ 和 $\ell(J)\ge0$ 不受 (19) 否定。

$\mathsf S\mathcal C=\mathcal C$ 也不推出每个奇权成本分量属于锥的 lineality：两个实际成本的差仍不自动为实际成本或锥元素。本文没有由奇权字符不存在推出完整半群可取负。

同样没有证明 $\mathcal C=U$，没有支付完整第四周期的所有实际成本、逐 $s$ ruling、更高阶或有限等距族。这里新增的是一条保持真实几何和右锚的完整奇偶身份，以及据此严格排除奇整权正仿射字符。

