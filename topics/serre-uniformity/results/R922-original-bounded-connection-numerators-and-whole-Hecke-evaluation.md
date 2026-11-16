# R922：七个原联络的有界分子、低权迹对偶与完整 Hecke 目标求值

日期：2026-11-16。状态：**本文为真实已成来源上的纸面证明与下一算术消费者契约。R905 的七个联络、R885 的完整源纤维及目标正规基、R919 的九个导数系数和八维微分迹行已经实际完成；本文新增的七个分母/分子、低权迹对偶矩阵、八个导数系数与七个目标联络值尚未运行。**

本篇不改已冻结 R919，也不以源纤维上 272 个函数值代替目标函数求值。核心缩减是：每个 R905 联络只需一个次数至多 272 的标量分母与 272 个次数至多 273 的分子；共同的正规迹对偶可改用一个次数至多 3 的矩阵，避免在目标纤维反演可能因分歧而非单位的特征多项式导数。所有实际接受仍在整个秩 8、底长 272 的 Artin 代数中进行。

## 1. 不变的原来源与方向

令 $k$ 为原 $K$ 或 $L$ 系数字段，保留原 $Y_k$、$\tau,\sigma,w_0$ 与正规基

$$
z=\sigma/\tau,\quad w=w_0/\tau,\quad
R_\tau=\bigoplus_{i=0}^{271}k[z]\beta_i,
\qquad \epsilon=(0,1^{144},2^{127}),\quad\beta_0=1.
\tag{922.1}
$$

原 $e_i$ 已含 $82^2$ 尺度；本篇不再次乘除。R806 的准确 $W=M_w$、R813 的准确 $g=\delta z,h=\delta w$ 及 R860 的

$$
\delta=\tau^{-1}q_Y\partial_{q_Y}/82,\qquad
\nu=dz/g,\qquad\operatorname{div}\nu=H-\mathcal C_{\rm cusp},
\qquad c_Y\nu=\nu
\tag{922.2}
$$

全部保留。$H=(\tau)$，$\deg H=272$，$\deg\mathcal C_{\rm cusp}=20$。

对七个已成有效除子 $D\in\{D_1,\ldots,D_5,X,D_N\}$，R905 已给同一原 $D$ 的完整 $U_D=H^0(2H-D)$、$W_D=H^0(3H-D)$，维数分别 146、418；已成单位图证明 $h^0(H-D)=0$。R905 的每个联络 $\alpha_D$ 是原有理截面 $1$ 中、全对数主部 $H-D$ 的准确 unit-solve 表达式，不能换成任意同主部联络。

记 R885/R919 已成的完整源纤维为

$$
A_0=\mathbf F_\ell[X]/(\chi_0(X)),\quad\dim A_0=272,
\qquad E=A_0[U]/(p(U)),\quad p=P/a_8,\quad\operatorname{rank}_{A_0}E=8,
\tag{922.3}
$$

其中 $\ell=1000000753$，$U=\pi_t^*z$，$V=K(U)/P_U(U)=\pi_t^*w$。$P$ 的九个系数及分子 $K$ 的八个系数来自同一 17 列准确函数表达式；后八列不是已经除过 $P_U$ 的目标坐标多项式。$a_8$ 与 $P_U$ 的整个代数单位证书、全部 272 个 $\beta_i(U,V)$、全部原 272 方程及 $U^0,\ldots,U^{273}$ 表均沿原已成来源。

这里的直接方向始终是 $\operatorname{Tr}_{\pi_s}\pi_t^*$。与原冻结 Hecke 方向的连接使用 R873/R915 的实际 canonical dual-isogeny 7，保留 scalar 7、diamond、原 $-3$ twist 和两端行列式帧；不以自伴随性删掉方向或刚性化。

## 2. R905 的 670 个系数只组成一个小次数向量

R905 为每个 $D$ 保存 $272\times272$ 多项式矩阵 $F_D(z)$。前 146 列来自 $U_D$，列权 $n_j=2$；其余 126 列为原 $W_D$ 的已选列，列权 $n_j=3$。因此

$$
\deg(F_D)_{ij}\le n_j-\epsilon_i,\qquad
\sum_j n_j=670,\qquad\sum_i\epsilon_i=398.
\tag{922.4}
$$

R905 实际选择的辅助 $a$ 满足 $F_D(a)$ 可逆，并已保存这个逆。当前七项的实际 $a$ 均为 0；消费者仍须读各原阶段的 `auxiliary_z`，不能用默认值替代来源。

令 $\theta_j$ 是 $F_D$ 各函数列关于原 $k(Y)/k(z)$ 迹的对偶基。原 670 个微分基依次是 $(z-a)^m\theta_jdz$，其中 $0\le m\le n_j-1$。从已成 `differential_basis_indices` 与同一个 543 阶单位解，直接组合

$$
c_{D,j}(z)=\sum_{m=0}^{n_j-1}c_{jm}(z-a)^m,
\qquad \alpha_D=\sum_j c_{D,j}\theta_j\,dz.
\tag{922.5}
$$

这一步只组合已成系数，不重新求主部矩阵、目标或 543 阶解。设 $\beta_i^*$ 为原正规基的迹对偶。由于 $\theta=\beta^*F_D^{-t}$，有

$$
F_D(z)^t x_D(z)=c_D(z),\qquad
\alpha_D=\left(\sum_i x_{D,i}(z)\beta_i^*\right)dz.
\tag{922.6}
$$

转置在此不可省略。

## 3. 从已成整个 $\mathcal O_D$ 得到真正标量分母

记 $h_a=\sigma-a\tau$。R905 的实际单位图证明整个 $D$ 与 $H_a=(h_a)$ 不交，但没有假设 $D\cap H$ 为空。其已成商及整除模型是

$$
Q_D:V_2\longrightarrow V_2/U_D\simeq H^0(\mathcal O_D),
\quad q\longmapsto q/h_a^2,
\tag{922.7}
$$

以及 $L_a:V_3\to V_2$，满足对全部 690 个原列

$$
h_aL_a(r)=r-w_r,\qquad w_r\in W_D.
\tag{922.8}
$$

令 $E_D$ 为已成商自由行的 canonical lift，$T_\tau:V_2\to V_3$ 为同一原 normal 位置的乘 $\tau$ 嵌入。则

$$
Z_D=Q_DL_aT_\tau E_D
\tag{922.9}
$$

是 **整个** $\mathcal O_D$ 上乘 $u_D=\tau/h_a$ 的矩阵，含所有非约化和闭点重数。理由是 $r=\tau q$ 时，(922.8) 除以 $h_a^3$ 后在 $D$ 上给 $L_a(\tau q)/h_a^2=(\tau/h_a)(q/h_a^2)$。

**定理 922.1。**

$$
d_D(z):=\det\bigl(I-(z-a)Z_D\bigr)
=\frac{\det F_D(z)}{\det F_D(a)},
\qquad \deg d_D\le272,\quad d_D(a)=1.
\tag{922.10}
$$

证明。$F_D$ 是 $\pi_*\mathcal O(3H-D)\to\pi_*\mathcal O(3H)$ 的完整同秩矩阵；其行列式截面的零除子是 $\pi_*D$，总次数 272。另一方面，$1-(z-a)u_D=(\sigma-z\tau)/h_a$ 在完整 $D$ 上的范数给同一个零除子，且在 $z=a$ 取 1。两个原截面在同一平凡化及归一处相等，得到 (922.10)。这一论证使用有限局部代数的行列式范数，不按几何点去重。若 $D\cap H\ne\varnothing$，相应 $u_D$ 为零或幂零；它们正确地降低 $d_D$ 的实际多项式次数，不能删掉后重新计长。证毕。

还可复用 R905 已成 $\mathcal O_D$ 的 power-basis inverse 和其完整 272 次关系：$u_D$ 的 canonical 坐标直接是 $Q_D(\tau h_a)$；只解这一个旧逆右端后，在该旧完整幂代数中求 $\operatorname{Nm}(1-(z-a)u_D)$。此选项不重求旧 primitive element、Krylov 逆或旧关系。无论选择哪条实现，新的范数/乘回回执必须保存，不能将 (922.10) 的纸证当实际分母已算。

## 4. 274 个 Taylor 向量足够，且有全局准确出口

定义 $y_D=d_Dx_D$。Cramer 展开中，为求第 $i$ 个未知量，将 $F_D$ 的第 $i$ 行替换为 $c_D^t$。每个行列式项的次数至多

$$
\sum_jn_j-\sum_{r\ne i}\epsilon_r-1=271+\epsilon_i.
\tag{922.11}
$$

故

$$
\boxed{\deg y_{D,i}\le271+\epsilon_i\le273.}
\tag{922.12}
$$

把 $t=z-a$，写 $F_D(a+t)=\sum_{m=0}^3F_mt^m$。只用原已保存的 $F_0^{-1}$，递推

$$
x_r=F_0^{-t}\left(c_r-\sum_{m=1}^{\min(3,r)}F_m^t x_{r-m}\right)
\quad(0\le r\le273).
\tag{922.13}
$$

再由 $y_D=(d_Dx_D)\bmod t^{274}$ 得每列候选。严格接受是完整多项式等式

$$
F_D^t y_D=d_Dc_D,
\tag{922.14}
$$

全部 272 行和全部系数均须乘回，同时核 (922.12)。不能仅验 Taylor 前缀或随机点。准确特征零表达式由同一已成 $F_D,c_D$ 与 (922.10) 定义；辅助素点计算仅给此表达式的模 $\ell$ 数组，不宣称有理系数已展开。

每个完整递推块、范数阶段、完整乘回阶段独立原子保存。已完成 $x_0,\ldots,x_m$ 后续从 $m+1$ 开始；既有 R905 的低阶逆不重求。

## 5. 为什么不能直接把旧 272 个目标值代入迹对偶

R885 完成的是 $\beta_i(U,V)$，不是 $\beta_i^*(U,V)$。在原函数域，令

$$
\chi(z,T)=\det(TI-W(z)),\qquad C(z,T)=\operatorname{adj}(TI-W(z))e_0.
$$

则准确有

$$
\beta_i^*=\frac{C_i(z,w)}{\partial_T\chi(z,w)}.
\tag{922.15}
$$

这由可分谱投影或迹配对验证；R885 原左伴随行给 $\beta_i$，不能改标签成为 (922.15) 的右列。即使构造这一右列，也不能由已成 $a_8,P_U,r_0$ 单位推出 $\partial_T\chi(U,V)$ 单位。在 $z$ 的分歧处，微分 $\beta_i^*dz$ 可正则，而两个分式因子的普通数值求值并不合法。

本篇下一节给实际更小的替代：先在原正规环中消去这项分歧分母，再进入目标整个代数。

## 6. 共同低权矩阵：迹对偶乘原 $g$ 后已经正则

令 $G(z)$ 为原正规基迹 Gram 矩阵，$G_{ij}=\operatorname{Tr}_{k(Y)/k(z)}(\beta_i\beta_j)$。原基的全局分裂是 $\pi_*\mathcal O_Y=\bigoplus_i\mathcal O(-\epsilon_i)$。有限相对对偶给

$$
\pi_*\Omega_Y=\bigoplus_i\mathcal O(\epsilon_i-2),
\qquad \beta_i^*dz\in H^0\bigl(\Omega_Y((2-\epsilon_i)H)\bigr).
\tag{922.16}
$$

这里使用 trace-normalized 的相对对偶，和 R905/R909 相同；有限映射的 Hom 描述见 [Stacks 0FKW](https://stacks.math.columbia.edu/tag/0FKW)，与绝对 dualizing sheaf 的运输见 [0C18](https://stacks.math.columbia.edu/tag/0C18)。

用原 (922.2) 除以 $\nu$，得到

$$
r_i:=g\beta_i^*\in H^0\bigl((3-\epsilon_i)H-\mathcal C_{\rm cusp}\bigr).
\tag{922.17}
$$

在原 normal 基写 $r_j=\sum_iR_{ij}(z)\beta_i$。于是

$$
\boxed{R=M_gG^{-1},\quad
\deg R_{ij}\le3-\epsilon_i-\epsilon_j,\quad
RG=M_g.}
\tag{922.18}
$$

负次数上界的条目必须恒零；尤其最后 $127\times127$ 块恒零。还可核 $R^t=R$，因为原乘法对迹配对自伴随。这是真正的原正规环结论：在整个 $\tau$ 图上 $gR_\tau^*=\mathcal C_\tau$，没有假设 $z$ 不分歧或 cusp 理想平凡。

因此 (922.6) 改写成

$$
\alpha_D=B_D\nu,\qquad
B_D=\frac{\boldsymbol\beta R(z)y_D(z)}{d_D(z)}.
\tag{922.19}
$$

其 numerator 的第 $i$ 个 normal 坐标次数至多 $274-\epsilon_i$；实际目标求值可保分解 $\boldsymbol\beta(U,V)R(U)y_D(U)$，不必先展开更大多项式。

## 7. 低权矩阵的最小新算术与严格出口

$\deg G_{ij}\le\epsilon_i+\epsilon_j\le4$：迹保持原 $mH$ 的有限推前整性。故五个不同已成 cyclic 纤维足够构造 $G$ 的候选，四个足够构造 $R$ 的候选。只复用旧 $W(a),K_a,K_a^{-1}$、旧 $\chi(a,T)$ 和旧 $M_g$；不重算旧 273 个 characteristic-polynomial 节点、旧 Krylov 或完整 $M_g$。

在一条旧 cyclic 纤维，设 $\chi_a(T)=T^{272}+c_1T^{271}+\cdots+c_{272}$，$H_a$ 是幂基的迹 Hankel 矩阵。其所有条目可由这一个旧完整关系的 Newton traces 得到，非约化纤维同样成立。由于 $K_a$ 的列是幂基在 normal 基中的坐标，

$$
G(a)=K_a^{-t}H_aK_a^{-1}.
\tag{922.20}
$$

只有用于构造 $R$ 的节点还需要实证 $\chi_a'$ 在整个该幂代数中可逆；不得从 cyclic 推出可分。若它确为单位，令 $Q_a$ 的第 $j$ 列为

$$
q_j(T)=\sum_{r=0}^{271-j}c_rT^{271-j-r},\qquad c_0=1
\quad(0\le j\le271).
\tag{922.21}
$$

则 $q_j(T)/\chi_a'(T)$ 是幂基 $T^j$ 的迹对偶。一次完整 polynomial xgcd 给 $\chi_a'^{-1}$，从而

$$
H_a^{-1}=M_{\chi_a'^{-1}}Q_a,
\qquad
R(a)=M_g(a)K_aM_{\chi_a'^{-1}}Q_aK_a^t.
\tag{922.22}
$$

这里没有新的 $272\times272$ 矩阵逆。每条点证书均保存整个多项式 Bézout 恒等式、完整迹乘回以及原点来源。已有节点中若不足四个满足条件，首scope诚实停止或另登记需要的新节点；不将失败节点删掉后声称其纤维已经计算。

按 (922.18)、(922.20) 的逐项次数界插值后，严格接受是完整多项式 $RG=M_g$、全部权界与 $R^t=R$，而非所选点上的相等。原 $G$ 在函数域可逆，故这个出口唯一确定原矩阵。$M_g$ 的全部原 17 块直接读取，最后一块是行 $256,\ldots,271$，不能误写块宽 17。

该矩阵为七个 $D$ 共同计算一次。它不重新选择 R905 的 holomorphic gauge，也不改原 $\nu$ 的尺度或真 $c_Y$。

## 8. 进入整个目标 $E$：真正分母及必要停止边界

沿原已成 $U^0,\ldots,U^{273}$ 表形成 $y_D(U)$，沿前四幂形成 $R(U)$；以原 272 个 **目标** $\beta_i(U,V)$ 收缩。必须分别实证

$$
d_D(U)\in E^\times.
\tag{922.23}
$$

单位证书是在完整 $E/A_0$ 上求范数并在完整 $A_0$ 上作 Bézout，随后完整 $E$ 乘回为 1；所有底因子及其幂零重数保留。$F_D(0)$ 的已成单位只描述源图的一个取值，不推出 $F_D(U)$ 或 (922.23)。

若 (922.23) 失败，不能把某个非零几何点数值当整个目标值。该失败也不证明原联络或精确目标不存在：标量 $d_D$ 可能含一个与实际目标支撑不相交的同 $z$ 纤维因子，或者联络在目标确有极点。下一步须用原完整局部模块消去真实可消因子，或单独登记另一个合法完整源纤维。不得只保单位分量，更不能从辅助素点失败推出特征零高度结论。

## 9. 在分歧处运输原 $\nu$：只新增八个 $\delta K$ 系数

R919 已准确完成整个 $E$ 中

$$
\dot U:=\delta_sU=-\delta P(U)/P_U(U),
\qquad\mathcal L(e)=\operatorname{Tr}_{E/A_0}(e\dot U),
\tag{922.24}
$$

并保存八个基元素的完整乘法迹及全部 272 个目标 normal 迹。这里 $\delta P$ 作用在原源系数后才specialize；$\delta_s$ 不是凭空加在底有限代数上的导子。

R919 还已保存全部 2058 个原基函数的导数。现在只用同一 R882 17 列矩阵的最后八列做新的线性收缩，得到分子导数 $\delta K$；九个 $\delta P$ 不再计算。必须保持原式 $V=K(U)/P_U(U)$。令 $\mathscr D=P_U(U)$，其整个 $E$ 中的逆直接复用 R885 已成证书。准确商法则给

$$
\dot V=\mathscr D^{-1}
\left[
\delta K(U)+K_U(U)\dot U
-V\left(\delta P_U(U)+P_{UU}(U)\dot U\right)
\right].
\tag{922.25}
$$

这里 $\delta P_U=(\delta P)_U$，直接对原已成九个 $\delta P$ 系数关于独立变量 $U$ 求导；$P_{UU}$ 同理由原九个 $P$ 系数取得。两者均不需要新的 $\Gamma$、$P$ 或其重构。为后面的迹公式，记

$$
\Delta_K=\delta K(U)-V\,\delta P_U(U),\qquad
\mathcal H_K=K_U(U)-V\,P_{UU}(U),
\qquad \dot V=\mathscr D^{-1}(\Delta_K+\mathcal H_K\dot U).
\tag{922.25a}
$$

实际阶段保留原分子标记，并完整乘回
$\mathscr D\dot V+V(\delta P_U+P_{UU}\dot U)=\delta K+K_U\dot U$。
不能只把 $K/P_U$ 重命名为 $K$ 而漏掉分母导数。

原目标 $g_t=\pi_t^*g,h_t=\pi_t^*h$ 由原已成正规向量和全 272 个目标 $\beta_i(U,V)$ 取得，绝不是源点 $z_s=0$ 上的 $g_s,h_s$。

对确定的整数 $t$，若

$$
\ell_t=g_t+t h_t\in E^\times,
\tag{922.26}
$$

则

$$
\boxed{J=\frac{\dot U+t\dot V}{g_t+t h_t}
=\frac{\pi_t^*\nu}{\pi_s^*\nu}.}
\tag{922.27}
$$

证明。在原对应函数域上，源导子的唯一可分延拓与目标导子相差同一标量 $J$，因 $z,w$ 生成目标函数域而分别有 $\dot U=Jg_t,\dot V=Jh_t$。对这两个等式作准确线性组合并在允许处除以 $\ell_t$，得 (922.27)。实际有限代数中，必须同时乘回 $Jg_t=\dot U$、$Jh_t=\dot V$ 的全部 $8\times272$ 坐标。整个单位条件使该 specialization 合法，不要求 $g_t$ 单独为单位；所以 $z$-分歧并未被排除。证毕。

若理想 $(g_t,h_t)=E$，存在某个 $t\in\{0,\ldots,2176\}$ 使 (922.26) 成立：每个极大理想至多排除一个常数，极大理想数至多 $\dim_{\mathbf F_\ell}E=2176<\ell$。这是一个条件性有限停止界，不先断言该理想已是单位理想。首scope可只试固定短前缀；失败如实保存，不丢因子。若两函数有共同零或所选原平面参数不能分离该处，须原正规局部模块处理，不能任选普通数值分母。

## 10. 七个联络的迹怎样复用 R919，且保帧

在 (922.23)、(922.26) 均通过后，

$$
\operatorname{Tr}_{\pi_s}\pi_t^*\alpha_D
=\operatorname{Tr}_{E/A_0}(B_D(U,V)J)\,\nu_s.
\tag{922.28}
$$

若 $g_t$ 自身为单位，可直接取 $t=0$，用已成 $\mathcal L$ 得 $\mathcal L(B_D/g_t)$；这只是一个真单位分支，不是假设所有纤维皆如此。

一般 $t$ 下，令 $\mathcal T(e)=\operatorname{Tr}_{E/A_0}(e)$。由 (922.25)，还可完全复用旧 $\mathcal L$：

$$
\operatorname{Tr}_{E/A_0}(B_DJ)
=\mathcal L\left(\frac{B_D(1+t\mathscr D^{-1}\mathcal H_K)}{\ell_t}\right)
+t\,\mathcal T\left(\frac{B_D\mathscr D^{-1}\Delta_K}{\ell_t}\right).
\tag{922.29}
$$

$\mathcal T$ 的八维行只需原已成 $a_8^{-1},P_U$ 与 Euler 恒等式

$$
\mathcal T(e)=a_8^{-1}[U^7]\bigl(eP_U(U)\bmod p(U)\bigr).
\tag{922.30}
$$

该恒等式对任意交换底环、首一关系成立，保留 nilpotents。可另按整个 rank8 乘法矩阵对八个基元素逐项乘回；这属于本次新普通迹行的准确接受，不重做 R919 已成的微分迹行。

准确特征零输出仍是原来源限定的表达式；实际 $8\times272$ 数值与七个 $272$ 向量明确是同一个 $\ell=1000000753$ 地方的像。本篇不把它们当 41-adic period 或高度。

## 11. 七个真实源、共同阶段和恢复顺序

每个 $D$ 必需原 R905 的 `complete-bundle-unit-graph`、`complete-quotient-and-h-division-models`、`complete-principal-parts-544-by670` 的基索引、`complete-full-principal-parts-solution`、`exact-regular-connection-DAG`。如果使用旧 $\mathcal O_D$ 幂基 norm 方案，再取其 `parameter-00000001-whole-Artin-algebra`。所有原 source refs、543 阶 gauge 和 $a$ 保持，不取模糊同类替代。

共同来源是原 R827 的 $W,g,h$、$M_g$ 17 个块与实际旧 Krylov 点；R885 的原 $\chi$、完整目标 17 个块与 $U$ 幂表；R919 的原 2058 导数索引、九 $\delta P$、$\dot U$、完整 $\mathcal L$。R882 旧17坐标只为新增八个分子 $\delta K$ 再读取，不重求2058逆或旧准确 Fourier 系数。原 R873 的第9至16列字段是分子 $K$；R885 已成字段 original_K_coefficients、Pprime_at_U、Pprime_unit_certificate 与 target_w 必须同时保留，后者满足整个 $E$ 中 $P_UV=K$。

最小阶段依赖为：

1. 五旧节点的完整迹 $G$ 与四个实证可分旧节点的低权 $R$，最终完整 $RG=M_g$；所有七项共享。
2. 每个 $D$ 的 $u_D$ 整乘法/norm、274 个递推向量及完整 $F_D^ty_D=d_Dc_D$。
3. 七个整个 $E$ 的 $d_D(U)$ 单位与 $B_D(U,V)$；失败只保该项真实结果。
4. 新八个分子 $\delta K$、原 $\dot U$、由旧九 $\delta P$ 导出的 $\delta P_U$、原 $P_{UU}$ 与旧 $\mathscr D^{-1}$，按完整商法则取得新 $\dot V$；再核真 $\ell_t$ 单位、商法则和两运输等式的全部坐标。
5. 普通迹八维行和七个原联络迹，分别保所有 272 坐标。

每个完成阶段不可变，current 单独记录下一未成节点、Taylor 下标或输入块。一次失败不能将旧成功阶段换标签重算；不同数学来源或选择规则必须新 tag。

## 12. 与五个原 Picard 输入、Hecke 校准和高度的边界

七个未平均 $\alpha_D$ 的直接目标迹并不自动等于五个原 $\mathcal I_{Z_j}$ 的规范连接。仍须严格沿 R905 已成 DAG：先校正 $\alpha_{D_N}-d\log Q_N$ 再作七共轭平均，保每个 $q_j\sum\sigma\alpha_{D_j}$、$7q_j(n_j-2)\alpha_X$、$-p_j\beta_N$ 和 $-q_jd\log\operatorname{Nm}Q_j$，最后作真正 $c_Y$ 平均。原 $c_Y(z)=z-2\beta_{72}$、$c_Y\nu=\nu$ 不可改为仅系数共轭。

完整 Hecke/YP 主函数的 $P_0,P_1$ 数值刚性化仍未由一个 $z_s=0$ 纤维计算；R917/R907 的端点 order 与原 $\kappa,\nu_j$、非 $p$ 项继续独立保留。本文不给 `height_computed`、`Poincare_period_computed`、`non_p_terms_computed`、`active_Hecke_support_determined` 或 `endpoint_numeric_calibration_computed` 真旗标。

## 13. 已实际来源登记

原标记的准确源码位置如下，均按实际 source 读取：

- R873 的 topics/serre-uniformity/scripts/R873_original_cyclic_seven_correspondence.py，在 source 2ee14751d7b2cb4403931886b587ca6f64138c73 的 function_program() 中，P_over_tau8_coefficients 取列0至8、K_over_tau8_coefficients 取列9至16；correspondence_function_field.target_w 明确是 K(U)/P'(U)。
- R885 的 topics/serre-uniformity/scripts/R885_original_whole_Artin_norms.py，在 source a22acdb019714f55bf182feb958425f8954da2ca 的 correspondence() 中，原代码先取 p=coefficients[:9]、k=coefficients[9:]，以原未首一化 P 的导数构造 Pprime_at_U，再作 V=K*derivative_inverse，并逐整个 E 核 Pprime*V=K。该冻结文件 Git blob 为 9f930082646f9539fae5b19a9dcd28bf47f40b5d。


- R905：run `43893738459` / source `f4589d2b0d8f5e2a914ca165a601351d09c303a9`；FINAL SHA256 `24045a35dcd878cad48d28aea20bce7077161b0eb9dc86113a54ba83bc71d4a4`；原 manifest `b11afeda52eb05af86a6fe162484854c29e0764acb26fb383f3f04d214b63fb0`。正式实际证明为 `results/R905-certified-original-seven-trace-dual-connections-and-five-Picard-inputs.md`，SHA256 `7fd90966e9b7713f1991be10840156b6b7138892e07f6f20f966e3e3082ade2a`。
- R885 整 Artin：run `43848870181` / source `a22acdb019714f55bf182feb958425f8954da2ca`；完整 manifest `8bbbe3d01fc4118dc3b1fc5238bfa906a50e850f1eea234302a1c1f7ea38f035`。原节点为 $z_s=0$，不是 $P_0$ 或 $P_1$。
- R919：run `43904104159` / source `1e0ecf187b6e282226833c6c45c5e94661a0a9b1`；实际 core `1.78416674` 秒、66 阶段；FINAL `c5b5a3a4f2a7b221d1b10bfbbc4a8f092690cbdeb30f83cc36135d23c91608ca`；configuration `cb2e457199bc9856e16fbebcfc1cfecbb0a94388bbee274e65047499ea0e3ede`。其九 $\delta P$、完整八维微分迹及 272 个目标像已成，七个联络尚未代入。
- 基础证明：R905 `137f5558857f0c67846fe0e7f32740e569f44c7f2dcb99b9c07b313d18229d7e`；R909 `60f74fbd4fd23e64c86df615ee661b874ed8ae900a2c146c26aa74ece28e9391`；R915 `b8ea2f3b8b11b0923e9192122d40dbd46224a5e54e4047c534748e9fabf1dc92`。

Git 只登记源码、参数、纸面证明及简明运行/SHA；机器矩阵、分子/分母、单位/Bézout回执与有限纤维值仅由一日活动 artifact/carrier 续传。
