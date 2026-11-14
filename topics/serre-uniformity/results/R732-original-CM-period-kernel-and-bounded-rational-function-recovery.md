# R732：原曲线的代数周期核与有界有理函数恢复

日期：2026-11-14。状态：**下述精确周期公式、线性核识别、映射次数公式和有限有理函数恢复定理已证明。** 本篇给出可执行的精确输入和有限算法；尚未执行一组原 $q$ 的函数表，亦未输出原 $\beta$ 的坐标或高度系数。

本篇继续 R725/R728 的实际模型
$$
C/L:\ y^2=x^3+b,\qquad
A^{\mathrm{mod}}\subset B=\operatorname{Res}_{L^+/\mathbb Q}C.
$$
它解决构造中的一个具体规范障碍：不把归一 newform 的 Fourier 首系数冒作原 $q$ 的 Néron/Manin 比例。该比例由原曲线全部闭周期的一个精确代数线性核决定，并保留最终清分母整数。

## 1. 原模型、周期与输入数据

始终使用 R595/R717 的固定模型和正 CM 格
$$
E_0:y^2=x^3-1,\quad \omega_0=dx/(2y),\quad
\Lambda_0=\Omega_0\mathcal O_K,\quad \Omega_0>0,\quad
K=\mathbb Q(\zeta),\quad \operatorname{Im}\zeta>0.
\tag{732.1}
$$
这里 $\Omega_0$ 为原正实周期。R725 中 $r=r_0/\sqrt[3]4$；
取同一个 $u^6=-16$，置
$$
R=ur,\qquad R^6=-b.
$$
则 $D_R:E_0\to C$ 是坐标缩放，准确满足
$$
D_R^*\omega_C=R^{-1}\omega_0,\qquad
\Lambda_C=\frac{\Omega_0}{R}\mathcal O_K.
\tag{732.2}
$$
换 $R$ 的六次单位倍数不改变此格；实现时仍记录所取根。
不能把 $E_{27}:Y^2=X^3+16$ 的最小正实周期当作其 $\mathcal O_K$-格生成元；使用 (732.1) 避开该相位问题。

令 $X=X_1$ 为 R616 的原曲线，保留原 $c_0,c_1$。令
$$
V=q_1^*H^0(A_{\theta,1},\Omega^1)
   \subset H^0(X,\Omega^1),\qquad g=\dim A_{\theta,1}.
\tag{732.3}
$$
算法的输入是以下**准确代数或有限组合对象**：

1. 原 $X/\mathbb Q$ 的函数域、光滑射影模型的 Riemann–Roch 运算、原 $c_0,c_1$ 的 places，以及一个展开用的尖点 $P$ 和局部参数 $q_P$。允许在有限数域上表示该尖点，但不允许换成不同层的曲线。
2. $V$ 的一个有理基 $\omega_1,\ldots,\omega_g$，并给每项通过 $X_1\simeq X_4$ 的原扭曲同构所对应的有限 adelic translate 表：
   $2\pi i(f_\nu|_2\gamma)(z)\,dz$ 的代数系数、实际矩阵 $\gamma\in\mathrm{GL}_2^+(\mathbb Q)$ 和相应 CM 角色。
3. 原曲线的整数闭同调基及交配矩阵。它们由同一复曲线的有限 Manin cell complex 给出，取 compact homology，不能把相对 cusp chains 直接当闭周期。
4. R725/R728 的 $b,F_p,L,L^+,R$、$E_n$ 及精确数域运算。

第二项采用 R575/R592 的原 tame 向量、Cartan 平均和全部换参常数。若从标准 newform 表开始，必须先完成这些有限矩阵运输。本篇不把未运输的 $\Gamma_1(108p^2)$ 形式直接当作 $\omega_j$。

这些输入并不要求已知 $q_1$ 的坐标。原函数域也有直接有限构造：在 $j=6912a^3(1-a^3)$ 上取
$$
k=\frac{j}{1728-j},\qquad E_j:\ y^2=x^3+3kx+2k.
$$
用原 $p$-除法多项式和 Weil pairing 表示一个完整有序 $p$-基，再取同一非分裂 Cartan 正规化子的固定域，并作光滑射影规范化。换这个通用椭圆模型的标量扭曲不会改变项链固定域；原六层由显示的 $a$ 和 R616 的 CM places 固定。实际计算可用等价的项链 resolvent，毋须展开整个 Galois 闭包。本篇尚未声称已将这些输入在某个新 $p$ 上全部展开。

## 2. 权一格点和的完整正则化

令 $\Lambda=\Omega_0\mathcal O_K$，$A_\Lambda=\operatorname{area}(\mathbb C/\Lambda)/\pi$，并定义
$$
\mathcal E(z)=\zeta_\Lambda(z)-\bar z/A_\Lambda.
\tag{732.4}
$$
等边 CM 格的 $e_2^*$ 为零：旋转 $\zeta$ 使其乘 $\zeta^{-2}\ne1$。
所以 (732.4) 是完整的周期完成化 zeta，不缺一个 holomorphic 线性项。

需要的求和规范是
$$
\mathcal E(z)=
\lim_{\epsilon\downarrow0}
 \sum_{\lambda\in\Lambda}
 \frac{e^{-\epsilon|z+\lambda|^2}}{z+\lambda}
\qquad(z\notin\Lambda).
\tag{732.5}
$$
说明其收敛和常数。将右边写成
$$
\int_\epsilon^\infty
 \sum_{\lambda\in\Lambda}
  \overline{z+\lambda}\,
  e^{-t|z+\lambda|^2}\,dt.
$$
对内部和作 Poisson。零频项是平面上一个线性函数乘径向 Gaussian 的积分，**精确等于零**；其余频率在 $t\downarrow0$ 指数衰减。大 $t$ 端在避开格点的紧集上也指数衰减。这给收敛及局部逐次微分的合法性。

极限周期、奇，格点处留数为一，且
$\partial_{\bar z}\mathcal E=-1/A_\Lambda$，因为
$\epsilon\sum_\lambda e^{-\epsilon|z+\lambda|^2}\to1/A_\Lambda$。
与 $\zeta_\Lambda(z)-\bar z/A_\Lambda$ 的差是一个至多线性的整函数；
奇性消掉常数，三次旋转消掉线性项。这证明 (732.5) 及准确规范。
相同结论也见 Bannai–Kobayashi–Tsuji §2.1 的 harmonic-degree-one Poisson 表达式。

特别地，对任意有限周期权 $W$，在对应分班格点和里不需假定
$\sum W=0$ 才能消掉一个虚构的权零极点：本例零频消失来自线性分子。
但完成化中的 $-\bar z/A_\Lambda$ 不能被删除，后面用除法多项式将它整体保留。

## 3. 任意有理尖点的精确有限代数和

考虑原 CM 形式的任一系数共轭
$$
f_\nu(z)=
 \sum_{\substack{\mathfrak a\subset\mathcal O_K\\
                 (\mathfrak a,\mathfrak f)=1}}
  \psi_0(\mathfrak a)\nu(\mathfrak a)
     e^{2\pi iN\mathfrak a\,z}.
\tag{732.6}
$$
每个理想唯一写成 $(\alpha)$，$\alpha\equiv1\bmod3$；
$\psi_0((\alpha))=\alpha$。$\mathfrak f$ 始终为该形式的真实导子。
未扭曲形式的 $2$-Euler 因子不能因选择一个含 $6$ 的辅助模数而删掉。

给 $t=A/c\in\mathbb Q$，$c>0$，取正整数 $M$ 使 $3\mid M$、真实有限角色在 primary 元素上模 $M$ 有定义且 $c\mid M$。例如取一个合适的原角色模数与 $c$ 的乘积；不要求二者互素。对 $v\bmod M\mathcal O_K$ 定义
$$
W_t(v)=
 \mathbf1_{v\equiv1\ (3)}
 \mathbf1_{((v),\mathfrak f)=1}
 \nu((v))\,e^{2\pi iA\,Nv/c}.
\tag{732.7}
$$
这里 $\nu((v))$ 只在第一、第二个条件成立时按 primary 角色求值。
权确实模 $M$ 周期，且 $W_t(0)=0$。

在 $\operatorname{Re}s>3/2$，
$$
L(f_\nu,t,s)
 =\sum_{\alpha\equiv1(3)}
 \frac{\alpha\,\nu((\alpha))
      e^{2\pi itN\alpha}}{(N\alpha)^s}
\tag{732.8}
$$
按 $v\bmod M$ 分班为有限个绝对收敛格点和。每班的 harmonic-degree-one Poisson 零频消失，故可合法延拓到 $s=1$。使用 (732.5) 及 $\Omega_0$ 为实数，得到
$$
\boxed{
\frac{L(f_\nu,t,1)}{\Omega_0}
 =\frac1M\sum_{v\bmod M\mathcal O_K}
    W_t(v)\,
    \overline{\mathcal E(\Omega_0v/M)}.
}
\tag{732.9}
$$
无一个额外的 $1/6$：primary 条件已经对每个理想恰选一个生成元。
$1/M$ 来自 $\alpha=M(\lambda+v/M)$ 的次数一分子和次数二分母。
若 $c$ 含 $2,3,p$，仍用同一分班；没有引入互素 CRT 的遗漏项。

记
$$
\mathcal A_\nu(t)=2\pi i\int_\infty^t f_\nu(z)\,dz,\qquad
\mathcal A_\nu(\infty)=0.
$$
尖点处 cusp 条件使积分收敛；Mellin/Abel 极限给
$\mathcal A_\nu(t)=L(f_\nu,t,1)$，所以从尖点 $t_1$ 到 $t_2$ 的周期为
$\mathcal A_\nu(t_2)-\mathcal A_\nu(t_1)$。
对 weight-two slash 使用
$(f|_2\gamma)(z)\,dz=f(\gamma z)\,d(\gamma z)$；
因此 §1 的全部 translate 的周期都由 (732.9) 求得，determinant 因子按实际 slash 约定保留。

## 4. 每个 torsion 值由原除法多项式给出

令 $P_v$ 是 $\Omega_0v/M\bmod\Lambda_0$ 对应的 $E_0[M]$ 点。
在 $E_0$ 上使用
$$
D=2y\,\partial_x+3x^2\,\partial_y.
$$
对原除法函数 $\psi_M$ 有准确恒等式
$$
D\log\psi_M(z)=M\mathcal E(Mz)-M^2\mathcal E(z).
\tag{732.10}
$$
它由 $\psi_M$ 的 sigma 乘法式导出；完成化的两个线性项在差中精确相消。

若 $P_v\ne O$，它是 $\psi_M$ 的简单零，故
$$
\boxed{
\mathcal E(P_v)
 =-\frac{D^2\psi_M(P_v)}{2M^2D\psi_M(P_v)}.
}
\tag{732.11}
$$
证明不能略掉常数项：在 $z=P_v+u$，
$D\log\psi_M=1/u+D^2\psi_M(P_v)/(2D\psi_M(P_v))+O(u)$，
而 (732.10) 右边常数为 $-M^2\mathcal E(P_v)$。
公式适用于合数 $M$、偶数 $M$ 和低阶非零挠点；特征零的 $[M]$ 可分，分母 $D\psi_M(P_v)$ 非零。$v=0$ 的项权为零，不求其极点值。

标签同样是有限代数输入：取原实周期上的
$P_1=\Omega_0/M$，即正向靠近原点的实 $M$-挠点，再用
$P_{a+b\zeta}=[a]P_1+[b][\zeta]P_1$。$M\ge3p>2$ 时可用实根隔离选定最靠近原点的一支，并保持原 $y<0$ 方向；不是任取一个未知的基。复共轭按同一 $E_0/\mathbb Q$ 的坐标作用求值。因此 (732.9) 是明确代数数的有限和，不使用浮点识别一个猜测周期。

## 5. 一个有限代数线性核恰给出原商的全部椭圆映射

令 $G_X$ 为 $X$ 的亏格，取输入中的闭整数同调基
$\gamma_1,\ldots,\gamma_{2G_X}$。由 §§2–4 及全部原 translate 表精确计算
$$
w_{ji}=\frac1{\Omega_0}\int_{\gamma_i}\omega_j\in\overline{\mathbb Q}.
\tag{732.12}
$$
取一个明确的有限数域 $\mathcal T$，包含 $L,R$、这些 $w_{ji}$、角色值及所需全部带标签挠点坐标。令
$\lambda_0=1,\lambda_1,\ldots,\lambda_{d_{\mathcal T}-1}$
为 $\mathcal T/K$ 的基。所有数域嵌入都按 §4 的原复标签记录。

把未知微分写成
$$
h_v=\sum_{j=1}^g v_j\omega_j,\qquad
v_j=\sum_{t=0}^{m-1}x_{jt}b^t,\qquad x_{jt}\in K.
$$
对每个 $i$ 展开 $R\sum_jv_jw_{ji}$，令其中所有 $\lambda_a$、
$a>0$ 的系数为零。于是得到一个**完全明确的有限 $K$-线性矩阵**
$\mathcal M$，其每列就是
$Rb^tw_{ji}$ 在 $\mathcal T/K$ 中的非恒定坐标。其核恰为
$$
\boxed{
\ker\mathcal M
 =\left\{v\in L^g:
 R\sum_jv_jw_{ji}\in K\ \text{对全部 }i\right\}
 \simeq \operatorname{Hom}_L(A_{\theta,1},C)\otimes_{\mathbb Z}\mathbb Q .
}
\tag{732.13}
$$
右边通过拉回 $\omega_C$ 放入左边；这是 $K$-向量空间同构，
且维数准确为 $g$。

证明如下。R725 的原正角色给
$A_{\theta,1,L}\sim C^g$，且 $\operatorname{End}_L^0C=K$。
任一 $L$-同态的拉回微分属于 $V_L$，其闭周期属于
$(\Omega_0/R)\mathcal O_K$；有理同态的周期属于
$(\Omega_0/R)K$，故给出核内元素。拉回微分在特征零对同态是单射。

反之，若 $v$ 在核内，记
$\kappa_i=R\sum_jv_jw_{ji}\in K$。
取正整数 $N$ 清除全部 $\kappa_i$ 在 $1,\zeta$ 基下的有理分母，
使 $N\kappa_i\in\mathcal O_K$。于是 $Nh_v$ 的全部闭周期属于
$\Lambda_C$。从原 $c_0$ 积分给出单值全纯映射
$$
f_v:X(\mathbb C)\longrightarrow\mathbb C/\Lambda_C=C(\mathbb C),
\qquad f_v(c_0)=O,\qquad f_v^*\omega_C=Nh_v.
\tag{732.14}
$$
它由 Jacobian 的复同态诱导，故代数。定义在 $\overline{\mathbb Q}$ 上的两个阿贝尔簇之间的复同态已定义在 $\overline{\mathbb Q}$ 上；这也可由 Hom scheme 的离散性和图的下降得到。对任意
$\tau\in G_L$，$f_v$ 与 $\,{}^\tau f_v$ 有相同拉回微分并都把 $c_0$ 送到 $O$，所以二者相等，故 $f_v/L$。

又因该微分属于 $V_L$，所得 Jacobian 同态在原 $q_1$ 的连通核上微分为零，因而在该连通核上为零。它在有理同态范畴中经原 $A_{\theta,1}$ 分解；可能的有限核只引入一个必须保留的整数分母。这证明 (732.13)。维数由
$\operatorname{Hom}_L^0(C^g,C)=K^g$ 得出。

这是有限线性代数和清分母计算，毋须识别任何未知超越周期。
可以取核的固定行简化基，再按预先固定的列顺序选择首个非零向量。
整数 $N$ 是显式计算的一部分，**不预先假定其为 $p$-单位**。
本节没有使用 $\beta$ 非挠或 R616 的秩假设。

## 6. 同一整数周期直接给出映射次数

令 $h=Nh_v\ne0$，并把整数交配矩阵化为一个定向辛基
$a_1,\ldots,a_{G_X},b_1,\ldots,b_{G_X}$，约定 $a_i\cdot b_i=1$。
精确记录
$$
\begin{aligned}
 \int_{a_i}h&=\frac{\Omega_0}{R}(u_i+v_i\zeta),\\
 \int_{b_i}h&=\frac{\Omega_0}{R}(s_i+t_i\zeta),
\end{aligned}
\qquad u_i,v_i,s_i,t_i\in\mathbb Z.
\tag{732.15}
$$
那么
$$
\boxed{\quad d=\deg f_v=\sum_{i=1}^{G_X}(u_it_i-v_is_i)>0.\quad}
\tag{732.16}
$$
这是精确整数等式。证明是将 Riemann 双线性关系应用于
$h=f_v^*\omega_C$：
$$
\frac i2\int_Xh\wedge\bar h
 =\sum_i\operatorname{Im}
       \left(\overline{\int_{a_i}h}\int_{b_i}h\right)
 =\left|\frac{\Omega_0}{R}\right|^2
    \operatorname{Im}\zeta\sum_i(u_it_i-v_is_i).
$$
左边也等于 $d$ 乘 $C$ 的同一面积
$|\Omega_0/R|^2\operatorname{Im}\zeta$。故 (732.16)。
该整数提供下一节的终止界；不需要另猜一个 modular degree，
也不通过浮点面积决定整数。

## 7. 有界 Riemann–Roch 线性系统输出真正有理函数

取 §1 的展开尖点 $P$，必要时在一个显式有限扩域上工作。
记其局部参数为 $q$，并以代数形式积分
$$
I(q)=\int_P^q h,\qquad I(0)=0,\qquad
e=\operatorname{ord}_q I\ge1.
$$
这给以 $P$ 为零点的映射 $f_P$，它与 (732.14) 只差常值平移，
所以其次数仍为 $d$，且局部分歧指数满足 $e\le d$。

在目标 $C:y^2=x^3+b$ 的**同一**微分 $\omega_C=dx/(2y)$ 下，
形式均匀化给
$$
\begin{aligned}
 x_\infty(q)&=\wp_C(I(q))
      =I(q)^{-2}-\frac b7 I(q)^4+\cdots,\\
 y_\infty(q)&=\frac12\wp_C'(I(q))
      =-I(q)^{-3}-\frac{2b}7 I(q)^3+\cdots.
\end{aligned}
\tag{732.17}
$$
所用不变量为 $g_2=0,g_3=-4b$。
全部系数由 $y^2=x^3+b$、$dx/(2y)=dI$ 递推得到，均为代数数。
实际函数 $x\circ f_P$ 的极点除子记为 $E_x$，
则 $\deg E_x=2d$，在 $P$ 的极点阶为 $2e$。

选一个显式有效除子 $D$，支撑避开 $P$ 且
$$
\deg D\ge2d+G_X,\qquad M_0=\deg D+2d.
\tag{732.18}
$$
例如取足够多个避开 $P$ 的有限映射纤维；可在同一表示数域内取一个有理有效除子。求$\mathcal L(D)$ 的一个精确基
$r_1,\ldots,r_s$。
对未知
$A=\sum a_ir_i$、$B=\sum b_ir_i$，解以下有限齐次线性系统：
$$
[q^k]\bigl(A(q)-B(q)x_\infty(q)\bigr)=0
\quad(-2e\le k\le M_0).
\tag{732.19}
$$
选择一个 $B\ne0$ 的解，并置
$$
\boxed{\quad x_P=A/B,\qquad y_P=\frac{dx_P}{2h}.\quad}
\tag{732.20}
$$
这两项就是 $f_P$ 的实际有理函数，并满足
$$
y_P^2=x_P^3+b,\qquad f_P^*\omega_C=h.
\tag{732.21}
$$

存在性和截断的充分性必须分别证明。由
$\deg(D-E_x)\ge G_X$，Riemann–Roch 给
$\mathcal L(D-E_x)\ne0$。任取其中非零 $B$，便有
$B\in\mathcal L(D)$ 及 $A=B(x\circ f_P)\in\mathcal L(D)$，
所以 (732.19) 确有 $B\ne0$ 的解。

反之，对任一这样的解，实际亚纯函数
$A-B(x\circ f_P)$ 的极点除子至多为 $D+E_x$，度数至多 $M_0$。
条件 (732.19) 使其在 $P$ 的零阶至少为 $M_0+1$。
非零主除子的零、极点度数相等，故该函数恒零，得到
$x_P=x\circ f_P$。于是 (732.20) 的 $y_P$ 也准确等于 $y\circ f_P$，
因为实际 pullback 微分是 $h$。这同时证明 (732.21)，不是仅在截断精度上拟合一个椭圆方程。

所需展开精度也是预先确定的。把每个 $r_i$ 展开到 $q^{M_0+2d}$，
把 $h/dq$ 展开到 $q^{M_0+3d}$，足以得到 (732.19) 全部系数：
$x_\infty$ 的最低阶是 $-2e$，计算它到 $q^{M_0}$ 至多需要
$I$ 到 $q^{M_0+3e}$，且 $e\le d$。故不存在依靠“多算若干项看起来稳定”的停机条件。按固定列顺序选择首个非零 $B$ 的主元解，还可将输出明确写成这些有限矩阵的有理 minors。

最后按原 place 求值
$P_0=f_P(c_0)$，用 $C$ 的群律定义
$$
f_0=f_P-P_0,\qquad f_0(c_0)=O,\qquad
\beta_C=f_0(c_1).
\tag{732.22}
$$
如果某个 place 的仿射坐标有极点，用光滑目标的射影延拓求值；
这只是精确 place 运算。即使展开尖点 $P$ 不在 $L$ 上，
唯一性仍使 $f_0$ 降到 $L$，正如 (732.14) 的证明。
所以原 CM 基点平移是由两个真实 place 的代数求值决定，
不是任意选一个 Fourier 积分常数。

## 8. 回到 $L^+$、原有理商与原 $\beta$

上节的非零 $f_0:X_L\to C$ 属于原 $V$ 的同态空间。
令 $c$ 为 $L/L^+$ 的复共轭，且作用于函数的所有系数。
两个映射
$$
F_+=f_0+c(f_0),\qquad
F_\zeta=[\zeta]f_0+c([\zeta]f_0)
\tag{732.23}
$$
都定义在 $L^+$，都把 $c_0$ 送到 $O$，且至少一个非零。
事实上，若 $F_+=0$，则 $c(f_0)=-f_0$，从而
$F_\zeta=[\zeta-\bar\zeta]f_0\ne0$。
是否为零可由准确拉回微分判断；特征零中不能有非零而零微分的群同态。

选其中非零者 $F$。R728 的 Weil adjunction 给实际有理同态
$$
Q_F:J_X\longrightarrow
B=\operatorname{Res}_{L^+/\mathbb Q}C,
\qquad
q^{\mathrm{mod}}=E_n\circ Q_F:J_X\longrightarrow A^{\mathrm{mod}}.
\tag{732.24}
$$
$F$ 的微分来自原 $V$，故 $Q_F$ 在有理同态范畴中经原
$A_{\theta,1}$ 分解。R728 的各简单因子互不同构，原 primitive
因子在 $B$ 中恰出现一次；因此非零 $Q_F$ 的像在该 primitive
因子内，$q^{\mathrm{mod}}\ne0$。它与原 $q_1$ 之间的非零有理同态
$A_{\theta,1}\to A^{\mathrm{mod}}$ 是一个同源，所有前述整数分母必须保留。

相应的实际点是
$$
\beta^{\mathrm{mod}}=q^{\mathrm{mod}}([c_1-c_0])
  =E_n\bigl(Q_F([c_1-c_0])\bigr),
\quad
Q_F([c_1-c_0])\ \longleftrightarrow\ F(c_1)\in C(L^+).
\tag{732.25}
$$
后一对应是 Weil restriction 的点函子，而 $E_n$ 是 R728 的有限
Ramanujan 和、已有明确的坐标缩放、共轭和椭圆群律。
所以一旦 (732.19) 执行完毕，(732.25) 没有另一个未知的积分常数。

如果要恢复全部同态，可对 (732.13) 的一组核基重复同一有限过程。
若要比较原 Néron/Hodge 规范，应将这些实际拉回微分，与 R728 的
$$
e_n^*\bigl(F_p'(b)^{-1}\mathbb Z_p[b]\,\omega_C\bigr)
$$
及 R575/R592 的原微分一起作准确代数基变换。
这给实际比较矩阵；清分母整数、$E_n$、原商同源和基变换都须显示记录。
本篇不宣称其中任何一个未计算行列式为 $p$-单位。

## 9. 结论的具体范围及下一份计算必须输出的对象

本篇形成一个有限的实际数据流：

1. 保留原曲线和原正 CM 角色，按 (732.7)–(732.11) 用带标签除法点计算每一个闭周期。
2. 解 (732.13) 的确切代数核，逐周期清分母，得到非零原同态微分 $h$。
3. 用 (732.16) 的整数周期计算映射次数 $d$，据此固定 (732.19) 的有限截断。
4. 解 Riemann–Roch 线性系统，输出 (732.20) 的两个函数，再在原
$c_0,c_1$ 求值并按 (732.23)–(732.25) 返回有理模型。

下一份执行证书必须保存实际 $p$、原模型/places、原 translate 表、
闭同调基、有限周期矩阵、核向量与整数 $N$、整数周期和 $d$、
Riemann–Roch 基及解、两个函数、原点求值和全部比较矩阵。
在它们实际出现之前，本篇的算法不能被登记为“原 $q$ 或 $\beta$ 已算出”。

同样，即使上述函数全部生成，也仍须执行 R724 的同一
Poincaré 刚性化、规范 de Rham 连接提升和分裂，以及 R593/R694/R696
的真实坏处比较，才可用来给 R703/R716 的原高度系数。
本篇不把 Abel 微分、任意第三类微分或任意 Picard 提升替换实际高度；
也没有由一个同源模型自动得到原 $\Lambda$ 的非零外积 jet。

### 原始来源与仓内接口

- Bannai–Kobayashi–Tsuji, *On the de Rham and p-adic realizations of the elliptic polylogarithm for CM elliptic curves*, Ann. Sci. Éc. Norm. Supér. 43 (2010), 185–234，
  [arXiv:0711.1701](https://arxiv.org/abs/0711.1701)，§1.1、§2.1。使用其完整 Eisenstein–Kronecker/Poisson 规范；本篇 §§2–4 独立写出所需 harmonic-degree-one 特例、完成化及除法多项式常数项。
- Mercuri–Schoof, *Modular forms invariant under non-split Cartan subgroups*，
  [作者原稿](https://reneschoof.github.io/mcom3503.pdf)，§§4、6。这里只用实际有限群作用及其构造方式，不能省略本题 R575/R592 的六层、扭曲和向量运输。
- [R725](R725-original-CM-elliptic-model-and-splitting-field.md)：正角色、$b$、$L$、$L^+$、$R$、原分裂模型。
- [R728](R728-original-Weil-restriction-primitive-projector-and-Neron-lattice.md)：Weil restriction、primitive 投影、Néron 逆不同及原商 adjunction。
- [R616](R616-original-CM-point-difference-and-explicit-height-basis.md)：原 $c_0,c_1$、$V$、原点差与正商；本篇构造同态不需要把其秩条件扩展成一个新的假设。
- [R724](R724-original-Chow-Heegner-height-matrices-and-canonical-jet-evaluation.md)：原高度连接和局部比较；本篇不更换该规范。
