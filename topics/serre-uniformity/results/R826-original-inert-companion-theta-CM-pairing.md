# R826 — 原惰性 apolar 源的 Gaussian companion theta CM 值公式

**状态：已证明。** 对每个 $p\ge41$、$p\equiv11\pmod {12}$，原未筛交替卷积准确等于下文八个权 $p-5$ Gaussian companion theta 的指定 CM 线性组合，外因子为显式单位。本文不证明该组合非零，也不消去原 primitive/Legendre 筛。

来源与规范固定为 [R812](R812-original-apolar-source-and-Gaussian-Frobenius-low-moment.md)、[IH 原惰性 harmonic-seven 源](../notes/2026-11-15-sigma-inert-Gaussian-harmonic-seven-source.md)及 [GC 固定 Gaussian 射线类分解](../notes/2026-11-15-sigma-inert-Gaussian-rayclass-source.md)。GC 的全文 SHA256 为 c2855a43758242ad1dd2f1ff2f4375ada8a4e9bd36e3e72574b2854ee62a7e30。所有矩阵、积分常数和原微分均沿这些来源；没有将其他标准 theta 基代入原 $F,G$。

## 1. 四个原 Hecke 字符与八个输入

置 $\mathcal O=\mathbb Z[i]$、$\pi_2=1+i$、$\xi_8=(1+i)/\sqrt2$。在 $(\mathcal O/3)^\times$ 中取生成元 $g=1+i$，定义
$$
 \epsilon_b(g)=\xi_8^b.
 \tag{826.1}
$$
特别是 $g^6=i$，所以 $\epsilon_b(i)=i^{-b}$。置 $\delta(1)=1,\delta(i)=-1$ 为 $(\mathcal O/2)^\times$ 上的非平凡字符。使用四个有限字符
$$
 \epsilon_3,\quad\epsilon_7,\quad
 \delta\epsilon_1,\quad\delta\epsilon_5.
 \tag{826.2}
$$
前两个导子为 $3$，后两个导子为 $6$；以下分别记为 $\epsilon$，导子记为 $\mathfrak f_\epsilon$。对 Gaussian 单位 $u$，四者都满足
$$
 \epsilon(u)=u,\qquad \epsilon(u)u^7=1.
 \tag{826.3}
$$

令
$$
 f_\epsilon(t)=
 \sum_{\substack{\mathfrak a\subset\mathcal O,\ \mathfrak a\ne0\\
                  (\mathfrak a,\mathfrak f_\epsilon)=1}}
 \epsilon(w)w^7t^{N\mathfrak a},
 \qquad \mathfrak a=(w).
 \tag{826.4}
$$
这是对理想求和；每个理想只取一次。由 (826.3) 生成元选择无关。按 (826.2) 次序，它们正是 GC 的 $F_3,F_7,G_1,G_5$，不是额外乘四的元素和。

八个 oldform 标签 $(\epsilon,d)$ 固定为
$$
 (F_3,1),(F_3,2),(F_3,4),
 (F_7,1),(F_7,2),(F_7,4),(G_1,1),(G_5,1).
 \tag{826.5}
$$
写
$$
 f_\nu(t)=f_\epsilon(t^d),\qquad
 J_\epsilon(t)=\sum_{n\ge1}\frac{a_\epsilon(n)}n t^n,\qquad
 \mathscr J_\nu(t)=\frac1dJ_\epsilon(t^d).
 \tag{826.6}
$$
因此 $\theta_t\mathscr J_\nu=f_\nu$，其中 $\theta_t=t\,d/dt$。这里是原 IH 的一次原函数，不是权八形式的七次 Eichler 原函数。

固定 $p\equiv11\pmod {12}$ 及所有有限系数字段的一个 $p$ 上素点，以下横线表示该处约化。有限字符值是八次单位根，故均 $p$ 整。所有恒等式对每个这样的嵌入成立，不改变 $i$ 或 $\xi_8$ 的相位。

## 2. 原一次原函数的五次 companion 比较

定义
$$
 C_{\epsilon,p}(t)=
 \sum_{\substack{\mathfrak a=(w)\ne0\\
                  (\mathfrak a,\mathfrak f_\epsilon)=1}}
 \epsilon(w)\bar w^{\,p-6}t^{N\mathfrak a},
 \qquad
 C_{\nu,p}(t)=d^{p-7}C_{\epsilon,p}(t^d).
 \tag{826.7}
$$
这里的 $\bar w$ 只是 Gaussian 共轭，不是对 $t$ 或 $\tau$ 取共轭，也不对 $\epsilon(w)$ 另施 Frobenius。

首先 (826.7) 生成元选择无关。因为 $p-6\equiv1\pmod4$，对单位 $u$，
$$
 \epsilon(u)\bar u^{\,p-6}
 =u\,u^{-(p-6)}=1.
 \tag{826.8}
$$
将理想用共轭重指标，又有
$$
 C_{\epsilon,p}(t)
 =\sum_{\mathfrak a=(w)}
       \epsilon(\bar w)w^{p-6}t^{N\mathfrak a},
 \tag{826.9}
$$
同样限制为与导子互素。因此它是普通的、全纯的 Hecke theta 形式，权为 $p-5$；导子仍是 $3$ 或 $6$，level 仍为 $36$ 或 $144$，nebentype 仍为 $\chi_{12}$。所谓反全纯的无穷型 $(0,p-6)$ 只表示选择了 Gaussian 的另一嵌入；(826.9) 明确给出全纯 $q$ 级数，不产生 $\bar q$。所用一般 Hecke theta 定理见 GC 所引 Schütt, *CM newforms with rational coefficients*, arXiv:math/0511228v5, Theorem 1.4；这里并不假设 Fourier 系数是实数。

**逐项模 $p$ 比较。** 因 $p\equiv3\pmod4$，
$$
 w^p=\bar w\quad\text{in }\mathcal O/p\mathcal O.
 \tag{826.10}
$$
若 $p\nmid Nw$，则
$$
 (Nw)^{p-7}w^7
 =w^p\bar w^{\,p-7}
 =\bar w^{\,p-6}\pmod p.
 \tag{826.11}
$$
若 $p\mid Nw$，Gaussian 惰性给出 $p\mid w$；于是两端分别含正次 $p$ 因子，也都为零。对每个范数只有有限个理想，故逐项相加合法，并得到
$$
 \boxed{\ \theta_t^{p-7}\overline{f_\epsilon}
              =\overline{C_{\epsilon,p}},\qquad
 \theta_t^{p-7}\overline{f_\nu}
              =\overline{C_{\nu,p}}.\ }
 \tag{826.12}
$$
第二式的 $d^{p-7}$ 正来自 oldform 求导，不能删去。

还必须先核 (826.6) 在 $p\mid n$ 时的分母。写 $w=p^a v$、$p\nmid Nv$；则
$$
 \frac{\epsilon(w)w^7}{Nw}
 =\epsilon(p)^a p^{5a}\frac{\epsilon(v)v^7}{Nv}.
 \tag{826.13}
$$
若 $p\mid Nw$，必 $a\ge1$，所以此项在约化后为零；若 $p\nmid Nw$，分母是单位。由此每个 $J_\epsilon$ 均 $p$ 整，且
$$
 \overline{J_\epsilon}=\theta_t^{p-2}\overline{f_\epsilon}.
 \tag{826.14}
$$
oldform 的 $d\in\{1,2,4\}$ 是单位，且 $d^{p-2}=d^{-1}\pmod p$。结合 (826.12)--(826.14)：
$$
 \boxed{\ \overline{\mathscr J_\nu}
           =\theta_t^5\overline{C_{\nu,p}}.\ }
 \tag{826.15}
$$
这对所有 $p\mid n$ 项已经先约去原分母后证明，不使用形式的 $0/0$。

## 3. 同一个 tame 标架上的几何对象

保留 R812 原辅助曲线、导子与点：
$$
 Y^2=X^3+16,\quad DX=2Y,\quad DY=3X^2,\quad
 P_0=(0,4),
$$
$$
 A(P_0)=0,\quad DA(P_0)=B\ne0,\quad D^2A=-XA/4.
 \tag{826.16}
$$
原 Tate 标架严格为
$$
 \lambda=d_0\eta^{-2},\quad d_0^{12}=-432,\quad
 D=\lambda^2\theta_q,\quad
 D\lambda=-\lambda^3E_2/12,\quad q_*=q^{1/12}.
 \tag{826.17}
$$
R812 已在模 $p$ 原 $q$ 字段证明
$$
 A=\lambda^{p-1},\qquad
 DA=A\lambda^2E_2/12,\qquad \eta^2=d_0/\lambda.
 \tag{826.18}
$$
这些是组合的 $q$ 展开恒等；从来不先在 supersingular 点给 $\lambda$ 指派单独的值。

令 $k=p-5$。定义
$$
 \mathscr C_{\nu,p}
  =\bigl[\lambda^k\overline{C_{\nu,p}}(q_*)\bigr]_{\rm alg}.
 \tag{826.19}
$$
方括号的含义是：把权 $k$ 模形式沿原固定判别式标架评价所得的代数截面/函数；其 $q$ 展开是所显示的乘积。它不是先把两个因子分别当作 $P_0$ 上的函数。

为明确其存在与正则性，可在原 level-six 标架上取一个共同的高层 tame 覆盖。$C_{\epsilon,p}$ 的 level 为 $36$ 或 $144$；$t^d=q^{d/12}$ 只加入 $2,3$ 次幂的 level。取主同余 level $1728$ 足够：对 $\gamma\in\Gamma(1728)$，由 $\tau\mapsto d\tau/12$ 共轭后的矩阵仍整且属于相应 $\Gamma_0(36)$ 或 $\Gamma_0(144)$。同层也包含原 eta 及 theta 的有限乘子核；若需要统一根的标记，再取只在 $2,3$ 分歧的常数扩张。沿这个覆盖，(826.19) 正是用原不变微分评价的权 $k$ 形式。

这些 theta 的积分性不随 $p-6$ 产生新分母：它们的 Fourier 系数是有限字符值与 Gaussian 整数的 $(p-6)$ 次幂之和；在其他尖点，Poisson 变换只出现该固定 lattice 的 Fourier 矩阵、单位根和 $2,3$ 的幂。对调和齐次多项式的 Fourier 变换不引入阶乘分母。因此 $p\ge41$ 时有通常的积分模形式模型，并在非尖点正则。固定判别式非零，故原微分标架在 $P_0$ 上正则。level 覆盖在此处是 tame 且具有光滑的好约化；$D$ 可提升为正则导子。

所以 $\mathscr C_{\nu,p}(P_0)$ 是良定义的代数模 $p$ CM 值。这里选择一个与原 level-six 点相容的高层点；下文与 GC 原 $e_{\nu,p}$ 的恒等保证实际所用的组合下降回原覆盖，不增加自由相位。

## 4. 原 Katz theta 的精确运输

对任意整数 $j$ 定义原标架上的正则算子
$$
 \mathcal T_j(v)=A\,Dv+j(DA)v.
 \tag{826.20}
$$
如果 $v$ 是权 $j$ 形式 $h(q)$ 的原标架表达 $v=\lambda^j h(q)$，则由 (826.17)--(826.18) 逐项得
$$
\begin{aligned}
 A D(\lambda^j h)+j(DA)\lambda^j h
 &=A\lambda^{j+2}
       \left(\theta_qh-\frac{jE_2}{12}h\right)
   +\frac{jA\lambda^{j+2}E_2}{12}h\\
 &=\lambda^{j+p+1}\theta_qh .
\end{aligned}
 \tag{826.21}
$$
因此 $\mathcal T_j$ 精确运输权 $j\mapsto j+p+1$ 的 Katz theta，符号为正；它不是固定权的裸 $D$。

因 $\theta_q h(q_*)=\theta_t h(t)|_{t=q_*}/12$，五次迭代 (826.21) 和 (826.15) 给出代数恒等
$$
 \bigl[\lambda^{6p}\overline{\mathscr J_\nu}(q_*)\bigr]_{\rm alg}
 =12^5\,
   \mathcal T_{5p-1}\mathcal T_{4p-2}
   \mathcal T_{3p-3}\mathcal T_{2p-4}
   \mathcal T_{p-5}(\mathscr C_{\nu,p}).
 \tag{826.22}
$$
五个输入权正是
$$
 p-5,\ 2p-4,\ 3p-3,\ 4p-2,\ 5p-1;
$$
输出权是 $6p$。这也由 $k+5(p+1)=6p$ 直接核对。

在 $P_0$，对每个正则 $v$，
$$
 \mathcal T_j(v)(P_0)=jB\,v(P_0).
 \tag{826.23}
$$
五个算子的中间结果仍正则，故可依次使用 (826.23)，无需把 $A Dv$ 的其他局部系数丢弃：
$$
 \left(
 \mathcal T_{5p-1}\mathcal T_{4p-2}
 \mathcal T_{3p-3}\mathcal T_{2p-4}
 \mathcal T_{p-5}v
 \right)(P_0)
 =-120B^5v(P_0).
 \tag{826.24}
$$
这里 $(-5)(-4)(-3)(-2)(-1)=-120$。

GC/IH 原尺度为
$$
 \mathcal P=A^5\lambda^{p+4}\eta^{-2}
           =\lambda^{6p}/d_0
 \tag{826.25}
$$
（最后一式只先在原模 $p$ 的 $q$ 字段使用）。由 (826.22) 它的乘积已有正则的代数延拓。因此 GC 定义的原 CM 值恰为
$$
 \boxed{\quad
 e_{\nu,p}
 =-\frac{120\,12^5}{d_0}B^5\,
    \mathscr C_{\nu,p}(P_0).
 \quad}
 \tag{826.26}
$$
这一步保留了全部 oldform 因子、原 $q_*$ 的 $12^5$、Hasse 归一和 CM 标架；没有把 $q$ 或非整完整 sigma 当作点值。

## 5. 指定原 FG 矩阵元与最终常数

令 $M_\nu$ 为 GC 的八个固定 $6\times6$ harmonic 源矩阵，即
$$
 \mathcal E(q)=\sum_{\nu=1}^8 M_\nu\mathscr J_\nu(q_*).
 \tag{826.27}
$$
它们为原第一指标偶、第二指标奇的 $4\times2$ 矩阵空间的一组整基，唯一的分母素数为 $2$。仍取原 Miller/Heisenberg 归一
$$
 U(P_0)=c\,\widehat U,\qquad
 \kappa_\nu=(\widehat U M_\nu\widehat U^t)_{F,G}.
 \tag{826.28}
$$
$c$ 是原共同尺度，不能置为 $1$。GC 固定运输脚本只计算这些 $\kappa_\nu$ 及其余七行，不能用矩阵整体可逆替代下述指定组合的非零。

原函数与 critical 指标为
$$
 F=x\sigma^6=z^4f(z^6),\qquad
 G=-xy\sigma^6=z\,g(z^6),\qquad p=6N+5.
 \tag{826.29}
$$
R812/IH 已证明
$$
 Q_{FG}(P_0)
 =(6B)^5\sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j,
$$
$$
 Q-Q_{\rm poly}
 =\frac{\mathcal P}{32}U_e\overline{\mathcal E}U_o^t,
 \qquad Q_{\rm poly}(P_0)=0.
 \tag{826.30}
$$
代入 (826.26)--(826.28)，再除原单位 $(6B)^5$，得到本篇主公式：
$$
 \boxed{\displaystyle
 \sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j
 =-\frac{120c^2}{d_0}
       \sum_{\nu=1}^8
          \kappa_\nu\,\mathscr C_{\nu,p}(P_0).
 }\tag{826.31}
$$
常数核对为
$$
 \frac{-120\,12^5}{32\,6^5}=-120.
 \tag{826.32}
$$

对所有允许的 $p$，$120$ 与 $d_0$ 是单位。R812 已认证的 $\widehat U$ 分母和 determinant Norm，以及其 $c^6=-d_0^{-16}/\det\widehat U$ 的尺度式，给出 $c$ 为单位；其有限坏素数仅在 $2,3,11$ 中。因此 (826.31) 外因子为单位，没有隐藏的 $p$ 倍数。

还有原 CM 权所迫的六条精确关系。按
$$
 (S,J),(S,G),(F,J),(F,G),(H,J),(H,G),(R,J),(R,G)
$$
排列八个 EO 行，除 $(F,G),(H,J)$ 外，对每行 $(a,b)$ 有
$$
 \sum_{\nu=1}^8
  (\widehat U M_\nu\widehat U^t)_{a,b}
       \mathscr C_{\nu,p}(P_0)=0.
 \tag{826.33}
$$
这是把 GC 的六个原零行用 (826.26) 等价运输后的关系；不另算新的非零定理，也不把剩余两个坐标混为一个。

## 6. 这条比较尚未完成什么

(826.31) 将指定惰性原组合变成了明确的代数 CM 值，避免把标准七次 Eichler 原函数或某个 good mock lift 的全局修正常数冒充原对象。

每个 $C_{\epsilon,p}$ 作为全局模形式的首项为 $t$，故不为零；但这不迫使其在本篇固定的 Eisenstein CM 点上非零。八个源矩阵的整基性也不迫使 (826.31) 的指定线性组合非零。其权为 $p-5$，随 $p$ 改变；不能把它误说成一个固定非零代数数而只排除其有限多个素因子。

即使 (826.31) 的右端最终证明非零，它仍只给原未筛交替卷积。原目标需要同一 $h=6i+7$、$(h,p+1)=1$，满足
$$
 P_{6i+6}(1/s)\,f_i\,g_{N-1-i}\ne0,\qquad s^2=-3.
 \tag{826.34}
$$
本篇没有加入这个 primitive/Legendre 投影，也没有消除 DP/QS 已登记的非水平投影障碍。下一步必须继续分析 (826.31) 的指定 CM 组合，或直接建立保留 (826.34) 的配对。
