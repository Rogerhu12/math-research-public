# R484：有理保护芽的真实延拓锁定与有限加速度判别集

日期：2026-11-16。**完整纸面证明；没有执行符号程序、原根恢复、profile 求积、秩计算、人工检查或新的数值研究。**

本稿继续 [R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md) 的同一个真实十三状态系统。得到的不是另一组一般相容条件，而是一条可以首先阻断现成拼接方案的延拓结论：

> 如果已付有理保护芽上的两条相位 ruling 方程独立确定两个真实加速度，那么在同一个最终规范和同一个真实前缀下，任何全段 ruling 解都被局部初值唯一性锁在这条有理芽的抛物线延拓上。离开它只能发生在全部相位加速度行真正降秩处；在固定 $\kappa,\omega$ 上，这些候选高度属于一个次数至多十二的非零多项式的根集。

这个结论有明确前提：**本稿没有证明当前实际母库的该 minor 非零。** 如果从起点另选库使两加速度行全零，或它们沿整个芽始终只有一维，本稿的非退化锁定不适用。即使出现判别根，也没有证明存在可通过的光滑分支。

本稿同时保留 R482 的完整常 scalar 平方门。加速度两行属于有限 $C^2$ 资料，并不使无加速度项 $\mathcal F$ 也自动为零。全词的第三入值、端点势、第二累计、一般 $w_\theta,\chi_\theta$、所有桥内第四成本和两个 collars 均不删去。

## 1. 同一个固定规范及真实状态

固定 R480 从起点选定的严格不交 rank-one profile 库，原全相位圆为
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
\tag{1}
$$
它保持原三矩和同一右锚，且已付完整第三空间 $W$ 的三个 outer 矩
$$
I_j\{\phi_\theta,\tau(\phi_\theta;D_\theta)\}=0,
\qquad \tau\in W,\quad j=0,1,2.
\tag{2}
$$
不把(2)扩大成 $\tau(\phi_\theta;D_\theta)$ 的整函数为零。

固定最终采用的同一个 $w_\theta,\chi_\theta$，以及真实全词起点的低阶入值。几何状态记为
$$
X=(h,k,\omega,\mathsf m,\gamma,\upsilon),\qquad
h>0,\quad \gamma=h_s,\quad \upsilon=k_s.
$$
这里 $\mathsf m$ 是原八维第二累计，不是可单独选择的控制。真实动力学为
$$
\begin{aligned}
h_s&=\gamma,& k_s&=\upsilon,&
\omega_s&=\upsilon/(2h),\\
\mathsf m_s&=M_{\rm raw}(h,k,\omega,\gamma,\upsilon),&
\gamma_s&=u_h,&\upsilon_s&=u_k .
\end{aligned}
\tag{3}
$$
frame、位置仍由原 $F_s=F\Omega(k)$、$\alpha_s=h^2T$ 恢复。

沿用 R482 的完整 ruling：
$$
\boxed{
\mathscr K(X,u;\theta)
=\mathcal F(X;\theta)
+\mathcal C_h(h,k,\omega;\theta)u_h
+\mathcal C_k(h,k,\omega;\theta)u_k .
}
\tag{4}
$$
$\mathcal F$ 指 R482(22)(25)(27)–(33) 所定义的**全部**无加速度项。它保留真实 $\Phi_{\mathsf m}D$、其平方、变化-profile chain、端点势差和一般规范，不只一个 principal。

为准确比较两条路径，除同一个 $X$ 外还须固定 R482 的端点类
$$
P_s^{\rm end}=\Theta_0+\Pi(j^1S_s)-\Pi(j^1S_{s_0}).
\tag{5}
$$
下面一律从同一个真实前缀切出，故 $\Theta_0$ 与初端势都相同。不能在新桥入口重新置 $\mathsf m=0$ 或更换 $\Theta_0$，再引用本稿的唯一性。

## 2. 两加速度系数的有限多项式结构

记
$$
z=x+\omega,\quad e=hz-k,\quad Q=1+e^2,\qquad
F_\phi=Q\phi''-2he\phi'+2h^2\phi.
$$
R482 给
$$
\mathcal C_h=-\frac1{4h^4}\int F_\phi Q\phi'''a_h[D],
\qquad
\mathcal C_k=-\frac1{4h^4}\int F_\phi Q\phi'''a_k[D],
\tag{6}
$$
其中
$$
a_h[D]=\frac1{16h^2}
\left[
Q(D_{12}-zD_{22})-2heD_{11}
+J\{(Q-2hez)D_{22}-2h^2D_{11}\}
\right],
\tag{7}
$$
$$
a_k[D]=\frac1{32h^2}
\left[QD_{22}+2hJ(eD_{22})\right].
\tag{8}
$$
$Jv(x)=\int_x^r v$ 仍是原右积分。$D_{11},D_{12},D_{22}$ 是真实对称二次槽上的导数，不把 $D$ 先乘开再任意求导。

现在固定
$$
k=\kappa,\qquad \omega=\omega_c .
\tag{9}
$$
$z$ 因而与 $h$ 无关。$e$ 对 $h$ 一次，$Q$ 与 $F_\phi$ 对 $h$ 至多二次。(7)(8)的中括号也对 $h$ 至多二次，原 $x$ 积分不增加 $h$ 次数。因此
$$
\boxed{
h^6\mathcal C_\alpha(h,\kappa,\omega_c;\theta)
=\sum_{j=0}^{6}h^j c_{\alpha,j}(\theta),
\qquad \alpha=h,k .
}
\tag{10}
$$
这里 $c_{\alpha,j}(\theta)$ 是同一实际 profile 库的完整积分。常数 $1/64$、$1/128$ 已包含在这些系数内；没有忽略真实尾项或将其用未知自由参数替代。

R482 已证明(6)为 quartic $C^2$ polynomial 泛函：最高 profile 三导只线性出现，按 local $u''$ 的原函数作真实 IBP 后降阶，所有 $J$ 的左值保留。式(10)只进一步记录几何参数的准确次数，不执行新的 profile 评价或秩判定。

## 3. 固定规范下的系数实解析性

R73 的 $M_{\rm raw}$ 在 $h>0$ 上对真实状态实解析。R77 的速度势与 R79 的端点商势由有限 Laurent/log 几何表达及 $k,\omega$ 多项式组成，故可一次选择实解析 lift $\Pi$。此处只取固定有限维商的线性截面，不随路径或相位重新选 lift。

R482(25)中其余局部恢复、原 $J$、physical 配对及第二历史平方，都由有限次加法、乘法、真实 $x$ 积分和 $h>0$ 上的解析系数构成。因此对每个固定 $\theta$，
$$
X\longmapsto \mathcal F(X;\theta),\quad
\mathcal C_h(X;\theta),\quad\mathcal C_k(X;\theta)
\tag{11}
$$
在共同物理状态域上实解析。

profiles、$w_\theta,\chi_\theta$ 只需原允许的光滑性，不必在 $x$ 上全局解析。它们在(11)中是固定资料；$x$ 积分所得的真实矩是参数表达的固定系数。固定 $x$ 区间上的共同物理支与 $h>0$ 保证局部解析微分可以在这些有限原式中进行。

本节没有宣称待构造的整条实际几何本来解析。原允许类仍是 $C^\infty$；解析性仅用于下一节中一条明确的参照路径和本系统的状态系数。

## 4. 已付有理芽有一条唯一的参照解析延拓

设在某个非空开放保护芽上已经支付完整 ruling，且原 scalar 几何为
$$
\bar h(s)=H\{1+\varepsilon(s-s_e)^2\},\qquad
\bar k(s)=\kappa,\qquad
\bar\omega(s)=\omega_c,
\quad H>0,\quad\varepsilon>0 .
\tag{12}
$$
固定芽内一点 $s_a$ 和它的真实第二累计 $\mathsf m(s_a)$。在抛物线(12)上以这个初值积分
$$
\bar{\mathsf m}_s
=M_{\rm raw}(\bar h,\kappa,\omega_c,
2H\varepsilon(s-s_e),0).
\tag{13}
$$
这是真实水平几何的第二历史，不能用一个近似多项式替代。其右端在实 $s$ 上解析且 $\bar h>0$，故 $\bar{\mathsf m}$ 解析。

保同一(5)与 $w_\theta,\chi_\theta$，将(12)(13)代入(4)。对每个固定 $\theta$，得到参照 ruling 的解析函数
$$
s\longmapsto
\overline{\mathscr K}(s;\theta)
=\mathcal F(\bar X(s);\theta)
+2H\varepsilon\,\mathcal C_h(\bar h,\kappa,\omega_c;\theta).
\tag{14}
$$
它在原开放芽上为零。实解析唯一延拓因而给
$$
\boxed{
\overline{\mathscr K}(s;\theta)=0
}
\tag{15}
$$
于包含该芽的共同物理连通域，且对全部 $\theta$ 同时成立。

逐个固定 $\theta$ 使用唯一延拓已经足够；不需要从有限相位采样猜全函数。实际 frame/位置可沿(12)恢复，但(15)不保证它们闭合，也不保证参照路径一直留在某个预先限制的紧状态盒。离开一个规定状态盒是参照可用域的终点，不是一个已经支付的拼接。

## 5. 正则点的局部锁定定理

设在参照路径一点 $s_a$，存在两个真实相位 $\theta_1,\theta_2$，使
$$
C_*(X)=
\begin{pmatrix}
\mathcal C_h(X;\theta_1)&\mathcal C_k(X;\theta_1)\\
\mathcal C_h(X;\theta_2)&\mathcal C_k(X;\theta_2)
\end{pmatrix},
\qquad
\det C_*(\bar X(s_a))\ne0 .
\tag{16}
$$
则附近任何完整 ruling 解必须满足
$$
\begin{pmatrix}u_h\\u_k\end{pmatrix}
=-C_*(X)^{-1}
\begin{pmatrix}
\mathcal F(X;\theta_1)\\
\mathcal F(X;\theta_2)
\end{pmatrix}.
\tag{17}
$$
将(17)代入真实状态方程(3)，得到一个光滑、局部 Lipschitz 的常微分方程。参照路径由(15)是它的一个解。

**锁定定理。** 在同一个真实前缀、同一个(5)及同一个 $w_\theta,\chi_\theta$ 下，若另一条 $C^\infty$ 全相位 ruling 路径与参照路径在 $s_a$ 有相同状态，则二者在该正则连通延拓区间完全相同。

证明就是(3)(17)的初值唯一性。这里确实保留了八个 $\mathsf m$ 分量和两个速度初值；只知道相同 $h,k,\omega$ 不足以调用唯一性。完整全相位方程比所取两行更强，但每个完整解必满足这两行，所以不会损害这个必要性结论。

若某一所选相位对的 determinant 在后面变零，而另一个相位对仍非零，可切换局部 ODE 图继续同一唯一性。切换图没有改变真实解、控制或规范。因此真正能够结束锁定的不是某一任选 minor 的零，而是
$$
\boxed{
\operatorname{rank}
\{\bigl(\mathcal C_h(\bar X;\theta),
\mathcal C_k(\bar X;\theta)\bigr):\theta\in\mathbb R\}<2 .
}
\tag{18}
$$

这与“在正则域任意选两个加速度控制一切”相反：两行一旦独立，完整 ruling 已经把这两个控制固定。剩余全相位方程只是额外相容性，不能提供第三个自由几何输入。

## 6. 真正离开抛物线只能到达有限候选高度

沿固定(9)，对第5节一个确实非零的相位对定义
$$
\boxed{
D_*(h)=h^{12}
\det
\begin{pmatrix}
\mathcal C_h(h,\kappa,\omega_c;\theta_1)&
\mathcal C_k(h,\kappa,\omega_c;\theta_1)\\
\mathcal C_h(h,\kappa,\omega_c;\theta_2)&
\mathcal C_k(h,\kappa,\omega_c;\theta_2)
\end{pmatrix}.
}
\tag{19}
$$
由(10)，$D_*$ 是次数至多十二的真实实多项式；由(16)，它不是零多项式。因此全部真降秩高度构成的集合 $\mathcal Z$ 满足
$$
\boxed{
\mathcal Z\subseteq\{h>0:D_*(h)=0\},
\qquad \#\mathcal Z\le12 .
}
\tag{20}
$$
重根只算一个候选高度。$(20)$是包含，不是等式：某个 $D_*$ 根可能只是这两个相位失去独立，全部相位仍然 rank $2$。

设一条光滑全 ruling 路径已经在开放区间上等于(12)(13)，随后在有限点 $s_*$ 第一次离开，且该点仍在物理状态域内。若(18)不成立，某个局部图(17)仍存在，由唯一性可跨过 $s_*$，与第一次离开矛盾。所以
$$
\boxed{\bar h(s_*)\in\mathcal Z.}
\tag{21}
$$
因为 $\bar h$ 是抛物线，同一个高度在整个实参照线上至多出现两次；这给至多二十四个参照位置的粗上界。实际可达的候选仅取所在物理区间及相应方向，不把这些点全部当成可用控制口。

### 6.1 奇点仍须支付真正的光滑分支

若新路径在 $s<s_*$ 的一段恰等于参照且两者均 $C^\infty$，则它们在 $s_*$ 的全部 jets 相同。任何不同的后继分支必须以相对参照的平坦差开始。

这并不排除分支。奇异解析微分约束可以容许非零的 $C^\infty$ 平坦解；因此不能仅凭系数解析就把(21)升级成全局不可能。必须回到原(3)(4)，核真降秩点的相容性、消失阶和允许平坦延拓。也不能强迫实际全词属于解析类；原几何只要求光滑。

### 6.2 没有非零 minor 的分支

如果全部相位 minor 沿开放芽恒零，则(16)的前提没有支付，本稿不给有限判别根结论。特别若从起点扩大低阶纤维，使 $\mathcal C_h=\mathcal C_k=0$，两加速度不再由(4)直接确定。

这正是一条需要单独研究的真实设计分支，而不是一个例外可以忽略。其原无加速度约束仍为
$$
\mathcal F(X;\theta)=0\quad\text{对全部 }\theta,
\tag{22}
$$
并须沿真实(3)保持；并未得到任意可走的 R70 桥。

## 7. 对原常态拼接的后果及完整平方门

若在离开保护芽之前没有遇到真正降秩，则同一最终规范的路径不能任意转成 R70 使用的常 scalar collar。抛物线 $\bar h$ 的二阶导恒为 $2H\varepsilon>0$，不可能在一个开放区间变成常数；改变 $k,\omega$ 也会违反已锁定的同一 ODE。有限词中的复位桥即便末矩阵为零，也不能跳过这段内部限制。

即使成功通过某个真降秩点进入常态区间，该常段还必须支付 R482 的完整平方门。设其真实常 scalar 为 $S_c$，令
$$
M_c=M_{\rm raw}(S_c,0,0),\qquad
A_c=\Phi_{M_c},\qquad A(t)=A_*+tA_c .
$$
记 $q_*=A_*D_\theta+w_\theta$。R482 的完整式给
$$
\mathscr K(t;\theta)
=\mathscr K(0;\theta)+t\,\mathcal B_c(\theta)+t^2\mathcal Q_c(\theta),
\tag{23}
$$
其中
$$
\mathcal B_c=
-2\mathcal E_{S_c}(q_*,A_cD_\theta)
+4\mathcal E_{S_c}\{\phi_\theta,A_c(\phi_\theta,q_*)\},
\tag{24}
$$
$$
\boxed{
\mathcal Q_c=
-\mathcal E_{S_c}(A_cD_\theta,A_cD_\theta)
+2\mathcal E_{S_c}\{\phi_\theta,
A_c(\phi_\theta,A_cD_\theta)\}.
}
\tag{25}
$$
一个正长度常段全 ruling 为零，要求(23)的常数、一次、二次系数全部为零。(25)既不含 $A_*$，也不含 $w_\theta,\chi_\theta$；不能靠另选该段的规范消去它。

本稿保留(25)的第二项，因而**没有从第一项的负平方单独推出定号**。R480 清掉完整第三 outer 矩，不等于清掉(25)。R482 两加速度行的低阶可支付性，也不等于(25)或(22)为零。

当前结论因而准确区分两道门：

- 正则延拓区间里，是否根本能离开已付抛物线；
- 通过真奇点后，候选常态桥是否满足完整(23)，包括历史平方和真实入口值。

若没有实际常态开区间，则不施加(23)的多项式系数条件。不能把不存在的旧常 collar 门继续强加于真正非平的实现。

## 8. 初选低阶增强能够改变哪一层

R482§7 证明(6)涉及有限个 quartic $C^2$ polynomial 系数。若在新的母库选择**起点**明确加入这些系数及其真实有限平移系数，原相同纤维、十次矩、十二副本和五个完整正 block 的机制可用于相应消去。这需要一个新的明确初选合同，不能在当前冻结库上免费补上。

这样改变的是两条 $\mathcal C$，以及本稿(16)是否成立。它不自动将完整 $\mathcal F$ 变成任意可指定的低阶资料。特别(25)有完整第二历史平方；判断其中能 IBP 降到 $C^2$ 的余项，与识别真正的三导平方，必须对完整两项一起做。

下一项精确任务由此分开：

1. 在同一个实际库上判(10)的相位 minor 是恒零，还是确有非零的一对；本稿没有进行该评价。
2. 若有非零 pair，只需研究(20)中的有限候选高度及其真全相位相容性，而非任意拼一条新 bridge。
3. 若从起点使加速度行退化，则对完整(22)(25)给低阶余表与不可降阶主项的准确分解，保全部原尾和累计，再判断约束状态族是否能产生真正返回路径。

前两项不把有限候选数量当成实际可控性；第三项不把有限低阶观察的保持当成能将其任意指定为零。

## 9. 全词与未付范围

本稿的唯一性只比较同一个最终 profile 圆、同一组规范、同一真实前缀和同一 quotient 端点势的路径。若重新选择 $w_\theta,\chi_\theta$，或改变母库，(17)的向量场可能改变；必须同时保原两个 period、十三规范行、相位种子与已付保护芽。若在最终词中换了前缀，真实 $\mathsf m$ 与(5)也须重新计入。

即使找到允许的新 scalar 分支，原 frame、位置、总 $M$、完整第三 $T$、第四 $V$、J-aff 成本及全部新增桥内 ruling 仍逐项保留。R468/R467 的实际成本截面可以支付其真实终值基准，但不替代(4)在桥内每一点的要求。

本稿完成的是：同规范下的正则锁定定理、真实系数的十二次判别上界、有限奇点的必要分支界，以及它与完整常态平方门的衔接。它没有证明当前库 rank $2$，没有排除退化库或可变 cap，也没有把已知冻结母的非零结论外推为全部实际构造不可能。

### 来源与独立窄核

- [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：真实分子恢复与八矩状态；
- [R77](R77-weight-three-local-operator-actual-finite-controllability.md)、[R79](R79-closed-horizontal-C1-control-and-endpoint-potential.md)：速度势、实解析系数与固定端点商；
- [R467](R467-conditional-actual-highest-gauge-control-and-one-complete-thirteen-row-normalization.md)、[R469](R469-global-gauge-locking-and-real-prefix-obstructions-between-rational-germs.md)、[R472](R472-two-level-prefix-reset-and-unavoidable-ruling-in-actual-return-bridges.md)：同一个规范、真实前缀及复位桥范围；
- [R480](R480-finite-full-third-outer-moments-and-zero-matrix-prototype-ruling.md)、[R482](R482-pointwise-third-memory-elimination-and-constrained-prototype-ruling-system.md)：本稿直接使用的完整 ruling 与系数。

literature 独立窄核了在给定解析性、仿射加速度式及次数前提下的解析延拓、局部 ODE 锁定与真 rank 降区别；没有替代本稿(6)–(10)的原式来源核对，也没有判当前实际 minor。全文没有新的科学执行。
