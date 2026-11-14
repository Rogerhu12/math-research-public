# R150 附录：齐次普通多项式的非零纤维、快 Bell 余项与二次深度近单位

日期：2026-11-13（UTC）。作者：normal_resume_1cf / Astra-ISP-1cf8c51d。
状态：已证明；Astra-ISP-1cf8c51d 与 boundary_resume_1cf 全文核对 Euler 恒等、真实快系数幂型、二次自然词域、完整填顶及原局部配对。
本稿使用原普通点态多项式的完整共振 Bell、实际合并矩池和真实正分量预解。新增近单位输入是自然域上的多项式，不将它假称为全空间有界交换子。普通复 Hilbert 不变子空间问题仍未完成。

## 1. 结论与准确范围

固定有限个不同复指数
$$
\rho_1,\ldots,\rho_q,\qquad \operatorname{Re}\rho_\nu>0,
$$
以及[合并矩稿](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)中的原实际模式
$$
u_{\rho_\nu}=-\kappa_{\rho_\nu}
+\sum_{p\ge0}\frac{\rho_\nu(\log(p+2))^{\rho_\nu-1}}{p+2}\chi_p.
\tag{1.1}
$$
全部复幂使用正实底，所有 $\kappa_{\rho_\nu}$ 保持原值。指数权为任意
$$
w=w_*+\sum_pw_p\chi_p,\qquad (w_p)\in\ell^2(\mathbb C).
$$

**定理。** 设 $F\ne0$ 是普通总次数 $D\ge1$ 的齐次标量多项式。则对任意 $\lambda\ne0$，
$$
\boxed{[F(u_{\rho_1},\ldots,u_{\rho_q})-\lambda]e^w
\text{ 非零且对原实际 }A\text{ 循环}.}
\tag{1.2}
$$
不要求最高曲线 $F(\rho_\nu t^{\rho_\nu})$ 非零，也不要求其梯度非零、实系数、矩形顶角或空谱线性组合。

可以对整个齐次多项式 $F^h$ 再应用定理，得到全部
$[F(u)^h-\lambda]e^w$，$h\ge1$、$\lambda\ne0$。
这不同于 $[F(u)-\lambda]^h e^w$：后者在 $h>1$ 时不是本定理自动覆盖的目标。
本稿不从循环向量的点态乘法推出任何额外结论，也不包括 $\lambda=0$。

## 2. 完整合并矩及真实快累积量

保留 $1\le|\omega|\le D$ 的全部原矩，按
$$
g=(d,s)=(|\omega|,\rho\cdot\omega-|\omega|)
$$
准确合并。记有限键表为 $\mathcal I_D$、其大小为 $K$。原物理行是
$$
m_g(p)=\frac{(\log(p+2))^s}{(p+2)^d},\qquad
\prod_\nu a_{\nu p}^{\omega_\nu}
=\left(\prod_\nu\rho_\nu^{\omega_\nu}\right)m_g(p).
\tag{2.1}
$$
对应变量记为 $W_g$，赋予权 $d_g=d$。
$d=1$ 时保留原中心的一阶模式；$d\ge2$ 时是实际有界的
$\sum_p m_g(p)(\chi_p-1)$。
倾斜后仍用同一合并比例。

普通到共振的有限逆为
$$
\mathcal Q_F(Y)=
\left.
F(\partial_z)
\exp\left[
\sum_{|\omega|=1}z^\omega Y_\omega+
\sum_{2\le|\omega|\le D}
\frac{(-2)^{|\omega|-1}}{\omega!}z^\omega Y_\omega
\right]\right|_{z=0}.
$$
作准确代入
$Y_\omega=(\prod_\nu\rho_\nu^{\omega_\nu})W_{g(\omega)}$，所得多项式记为 $Q(W)$。
因为原 $F$ 齐次 $D$，
$$
\mathscr E Q=DQ,\qquad
\mathscr E=\sum_{g\in\mathcal I_D}d_gW_g\partial_{W_g}.
\tag{2.2}
$$
这是一整张合并矩表中的权齐次等式；不拆开实际相同的矩行。

令 $t_p=e^{-2w_p}$、$R_p=V(t_pN_p)$。
完整实际共振累积量为
$$
G_\beta=(-1)^{|\beta|-1}(|\beta|-1)!
\sum_p\left(\prod_gm_g(p)^{\beta_g}\right)(R_p-I)^{|\beta|},
\qquad 2\le|\beta|\le D.
\tag{2.3}
$$
每条 $m_g$ 都属于 $\ell^2$，所以以上级数绝对范数收敛。

更强地，真实局部至少二阶消去给
$$
\boxed{G_\beta\in\mathcal G,\qquad \chi(G_\beta)=0.}
\tag{2.4}
$$
这里 $\mathcal G$ 是 R151 的四次型解析逼近代数。
具体依据是 R270C §10.1 的实际 $G_n$ 及 R270B 的统一二阶消去；对有限线性组合行作固定次数的有限参数插值即可提取 (2.3)，只使用 $\mathcal G$ 的有限加法封闭。
也可直接对 (2.3) 的每位有理函数使用同一个统一小圆解析预算。
没有将普通慢 Bell 系数误认作 (2.3)，没有把 $\mathcal G$ 当成整个 $\mathcal A$ 的范数闭理想。

定义有限微分算子
$$
\mathscr L=\sum_{2\le|\beta|\le D}\frac{G_\beta}{\beta!}\partial_W^\beta,
\qquad P_0(W)=e^{\mathscr L}Q(W),\qquad P(W)=P_0(W)-\lambda I.
\tag{2.5}
$$
指数在有限多项式上截断，所以所有显示式均为有限和。
R186 和合并矩稿的完整生成恒等式、共同自然域及图核心给原规范最大实现 $\mathsf P$：
$$
\mathsf P^*=C\mathsf PC,\qquad
\mathsf P e^w=[F(u_\rho)-\lambda]e^w.
\tag{2.6}
$$
以下 $M=\ker\mathsf P$。不先假设 $M$ 属于任意一阶自然域。

## 3. 加权 Euler 恒等式与快余项

记
$$
\operatorname{wt}(\beta)=\sum_gd_g\beta_g,\qquad
\mathscr L_1=\sum_{2\le|\beta|\le D}
\frac{\operatorname{wt}(\beta)G_\beta}{\beta!}\partial_W^\beta.
$$
真正的多项式微分交换子是
$$
[\mathscr E,\mathscr L]=-\mathscr L_1.
$$
所有常系数微分算子互相交换，故
$$
\mathscr E P_0
=e^{\mathscr L}(\mathscr E-\mathscr L_1)Q
=DP_0-\mathscr L_1P_0.
\tag{3.1}
$$
取
$$
E(W)=\frac{1}{D\lambda}\mathscr L_1P_0(W).
\tag{3.2}
$$
由 (3.1)，得到整个有限多项式恒等式
$$
\boxed{
\sum_g\frac{d_gW_g}{D\lambda}\partial_{W_g}P
=I-E(W)+\frac{1}{\lambda}P(W).
}
\tag{3.3}
$$

将 $E$ 写成显示变量的有限单项式和
$$
E(W)=\sum_{\alpha\in\mathcal J}E_\alpha W^\alpha.
\tag{3.4}
$$
零系数删除。每个系数至少含一个 (2.3)，其余系数也是有限个 $G_\beta$ 的多项式；因此 R151 的有限和积封闭给
$$
E_\alpha\in\mathcal G,\qquad\chi(E_\alpha)=0.
\tag{3.5}
$$
$E$ 的普通显示次数不超过 $D-2$；以下只用较粗的固定上界 $D$。
若 $E=0$，之后所有快余项估计直接省去，近单位就是精确单位。

### 3.1 固定有限系数的联合四次幂界

R151 定理3.1 给每个非零零字符 $E_\alpha$ 一个严格正的四次型。
固定有限列表后，可以取共同 $c>0$、$C\ge1$，使
$$
\|E_\alpha^n\|\le C^n e^{-cn^4}\qquad(n\ge0).
\tag{3.6}
$$
系数在原 $A'$ 中实际交换。设 $L=|\mathcal J|$，则对任意 $n_\alpha\ge0$、$\sum_\alpha n_\alpha=k$，
$$
\boxed{
\left\|\prod_\alpha E_\alpha^{n_\alpha}\right\|
\le C^k\exp\left(-\frac{c}{L^3}k^4\right).
}
\tag{3.7}
$$
这里只用了 $\sum_\alpha n_\alpha^4\ge k^4/L^3$。

本稿需要的是实际幂范数 (3.6)，不是从系数的范数尾快就直接宣称 (3.7)。
也不使用 $G_\beta=A B_\beta$ 这样的全域有界除法。

## 4. 二次增长的共同自然词与强单位

把全部原复一阶行拆成实、虚的正负部，取其中非零的有限个实际最大增生 first
$T_1,\ldots,T_J$。
原 $d=1$ first 在这些正分量的共同域上是固定复线性组合，加原常数和固定有界倾斜；$d\ge2$ 的模式本来有界。
不声称原共同域等于这些正分量的共同域。

对整数 $r\ge2$，取
$$
q_r=(8D+8)(r+1)^2,\qquad \epsilon_r=r^{-3},
$$
$$
\boxed{
\mathcal R_r=
\left[\prod_{\nu=1}^J(I+\epsilon_rT_\nu)^{-1}\right]^{q_r}.
}
\tag{4.1}
$$
全部因子是真正交换的收缩，属于 $A'$。
R186 的逐因子域计算给全部长度至多 $q_r$ 的正分量词域。
特别每个原显示模式词满足
$$
\boxed{
\|W^\gamma\mathcal R_r\|
\le(C+Cr^3)^{|\gamma|}
\qquad(|\gamma|\le q_r).
}
\tag{4.2}
$$
包含有界高矩模式不会增加无界域要求。

在稠密正分量共同一阶域上，
$$
\|(\mathcal R_r-I)f\|
\le q_r\epsilon_r\sum_\nu\|T_\nu f\|\longrightarrow0,
$$
因为 $q_r\epsilon_r=O(r^{-1})$。
收缩性将此延到全部 $H$。
R186 的有界核方程又给
$$
\boxed{\mathcal R_r\to I\text{ 强},\qquad \mathcal R_rM\subset M.}
\tag{4.3}
$$
每个 $A'$ 系数保持全部这些共同词域，原 first 在合法域内保持 $M$。

把 (3.7)、有限多项式展开及 (4.2) 合并，对 $k\le r^2$ 得
$$
\boxed{
\|E(W)^k\mathcal R_r\|
\le \exp[-c_0k^4+C_0k\log(r+2)].
}
\tag{4.4}
$$
每项的 first 词长不超过 $Dk\le Dr^2$，故定义域由 (4.1) 支付。
指数中的有限单项式数及多项式组合数只增加 $C^k$。
本式的 $E^k$ 是已付自然词上的实际乘积；没有把未正则化的 $E$ 当作有界算子。

## 5. 多项式块证书与准确的近单位

定义有限 Neumann 多项式
$$
H_r(W)=\sum_{k=0}^{r-1}E(W)^k,\qquad
B_{g,r}(W)=\frac{d_gW_g}{D\lambda}H_r(W).
\tag{5.1}
$$
乘 (3.3)，得到全多项式等式
$$
\boxed{
\sum_gB_{g,r}\partial_{W_g}P
=I-E^r+\lambda^{-1}H_rP.
}
\tag{5.2}
$$
所以在 $M$ 内的已付深域上，右侧准确等于 $I-E^r$。
这里使用原完整 $P$，不是只在尾多项式的核上成立的证书。

各 $B_{g,r}$ 的显示次数至多 $1+D(r-1)$。
它们一般不是全空间有界算子；只在 (4.1) 支付的有限深域上使用。
所有 $r$ 个块的乘积最多消耗
$$
r[1+D(r-1)]\le Dr^2+r
\tag{5.3}
$$
个 first 字。
再加 $P^r$、反射后的词和固定低头交换子所需 $O(Dr)$ 层，仍严格小于 $q_r$。

取合并矩稿的 $K$ 个分离物理池，每池 $N$ 位，$r=\lfloor\sqrt N\rfloor$。
任意跨池块 $B=(p_1,\ldots,p_K)$ 的真实矩阵
$$
\Xi_B=(m_g(p_i))_{g,i}
$$
可逆，且统一
$$
\log^+\Delta_N^{-1}=O(\log N).
\tag{5.4}
$$
真实一次反射系数为
$$
L_{p_i}=4\sum_gm_g(p_i)\partial_{W_g}P.
\tag{5.5}
$$
固定所有 $G_\beta$ 为系数；它们的同位符号差至少含 $N_p^2$，所以没有漏掉任何平方零一次项。

定义多项式系数列及块输入
$$
b_{B,i}^{[r]}=\frac14\sum_g(\Xi_B^{-1})_{ig}B_{g,r}(W),
\qquad
Q_B^{[r]}=\sum_{i=1}^K b_{B,i}^{[r]}
\prod_{\ell\ne i}t_{p_\ell}N_{p_\ell}.
\tag{5.6}
$$
在足够深的 $M$ 域中，矩阵乘法与 (5.2) 给
$$
\sum_i b_{B,i}^{[r]}L_{p_i}=I-E^r.
\tag{5.7}
$$
故该块平方零顶部是
$$
\left(\sum_i t_{p_i}N_{p_i}L_{p_i}\right)Q_B^{[r]}
\equiv (I-E^r)\prod_i t_{p_i}N_{p_i}.
\tag{5.8}
$$

$r$ 个块按各池排序后的固定匹配组成。
其输入已有 $(K-1)r$ 个显式位因子。
原提升取高于一次的增量，或同一块收到两次提升，都会造成重复位。
因此原相同的顶部计数给
$$
r!\,t_E N_E(I-E^r)^r\mathcal R_rf.
\tag{5.9}
$$
多项式系数虽然也依赖实际模式，但与这些位因子交换；显式重复位不会被系数消掉。
没有增加任何未计的匹配因子。

最后，(4.4) 给
$$
\begin{aligned}
\|[(I-E^r)^r-I]\mathcal R_r\|
&\le\sum_{j=1}^r\binom rj
\|E^{rj}\mathcal R_r\|\\
&\le \sum_{j=1}^r\binom rj
e^{-c_0r^4j^4+C_0rj\log(r+2)}
\longrightarrow0.
\end{aligned}
\tag{5.10}
$$
例如充分大 $r$ 时上界不超过 $e^{-c_1r^4}$。
这里最大幂为 $r^2$，已经包含在 (4.4) 和 (5.3) 的域预算内。

## 6. 反射、carry 和局部四次费用仍全部支付

把 (5.6) 的系数与显示词真正展开。
每个固定 $E_\alpha$ 先仅用其有界范数作粗估计，$H_r$ 的次数为 $O(r)$，$r$ 个块的总次数为 $O(r^2)$。
结合 (5.4)、(4.2)，全部输入绝对费用至多
$$
\boxed{
A_N\le \exp[Cr\log N+Cr^2\log(r+2)]
=\exp[o(r^4)].
}
\tag{6.1}
$$
此处不以可能消去后的输入范数替代实际展开费用。

原正预解工作引理中，真实高位反射误差的联合导数满足
$$
\|\partial^\gamma\mathcal E_E\|
\le C^{|\gamma|}\gamma!\,
e^{-c16^{\min E-1}}.
\tag{6.2}
$$
有限正分量扩展与有界倾斜 $\operatorname{ad}_H$ 已由合并矩稿 §6 完整支付。
这里反射的仍是固定次数 $D$ 的原 $P$，其局部系数是 (2.3) 的明确实际 Bell 系数。
多项式 $Q_B^{[r]}$ 只放在最右的原核输入中，不要求它本身有任意 $A'$ 系数的反射估计。

把一个 first 词移过最左反射时，每个字只留在右侧或变成一次系数导数。
再把右侧词与 (5.6) 的多项式输入相乘，所需总原词仍为 $O(r^2)$。
粗计数、联合阶乘和 (4.2) 至多增加
$\exp[Cr^2\log(r+2)]$，已包含于 (6.1)。
所有选位至少为 $\mu N$，真实
$N_j^2=\eta_jN_{j+1}$ 及 (6.2) 的双指数费用压过 (6.1)。
原反射顺序准确是
$$
\mathsf P^rJ_EQ_E^{[r]}\mathcal R_rf
=J_E(\gamma_EP)^rQ_E^{[r]}\mathcal R_rf.
\tag{6.3}
$$
先在原 $M$ 内形成全部输入，再作用最左 $J_E$。

对固定前 $h$ 位的局部全矩阵 $D_0$，只对明确有限物理头提出一个 $A$：
$$
P=P_{\mathrm{tail},h}+A\,U_h(W),\qquad \deg U_h\le D.
\tag{6.4}
$$
高尾与 $D_0$ 完整域交换。
展开 $\operatorname{ad}_P^rD_0$ 时，两侧因子
$A^j$ 与 $A^{r-j}$ 保留。
把 $U_h$ 的 first 字移过固定 $D_0$ 和反射，只使用已经支付的词；不需将 (5.6) 的系数移过 $D_0$。
R109 的实际四次幂界遂给
$$
\boxed{
\|(\operatorname{ad}_P^rD_0)\mathcal V_N^{[r]}\mathcal R_rf\|
\le
e^{-5r^4/6+105r^3+Cr^2\log(r+2)+Cr\log N}\|f\|
\longrightarrow0.
}
\tag{6.5}
$$
常数可依赖固定目标、权和 $D_0$，不依赖 $N$。
(6.4) 的有限头除法与未使用的全累积量除法是不同步骤。

## 7. 原池平均、完整 C 配对与排核

沿原固定匹配定义
$$
\mathcal V_N^{[r]}\mathcal R_r
=(-1)^{Kr}(r!)^{K-1}(2/N)^{Kr}
\sum_{\substack{J_\ell\subset I_{\ell,N}\\|J_\ell|=r}}
t_E^{-1}J_EQ_E^{[r]}\mathcal R_r.
\tag{7.1}
$$
这个带右正则器的整体是真正全域有界算子；不把单独的
$\mathcal V_N^{[r]}$ 宣称为全空间有界。
前因子、顶部 $r!$ 和 $K$ 个组合数与原合并矩稿完全相同。

设 $\mathcal C_N$ 为原 $K$ 池纯平均的乘积。
它一致有界，且
$$
\mathcal C_N\rightharpoonup e^{-K/2}I.
$$
(5.9)、真实 carry 及 §6 给
$$
\mathsf P^r\mathcal V_N^{[r]}\mathcal R_rf
-\mathcal C_N(I-E^r)^r\mathcal R_rf\longrightarrow0
\qquad(f\in M).
\tag{7.2}
$$
由 (4.3)、(5.10) 和 $\sup_N\|\mathcal C_N\|<\infty$，
$$
\boxed{
\mathsf P^r\mathcal V_N^{[r]}\mathcal R_rf
\rightharpoonup e^{-K/2}f.
}
\tag{7.3}
$$
近单位误差没有乘上增长的绝对输入费用；它位于已经归一后的顶部纯池平均之后。

对 $f,g\in M$，全部实际中间自然词由 §4–6 支付。
原全 $H$ 上的完整 $C$ 对称给
$$
B(D_0\mathsf P^r\mathcal V_N^{[r]}\mathcal R_rf,g)
=(-1)^r B((\operatorname{ad}_P^rD_0)
\mathcal V_N^{[r]}\mathcal R_rf,g).
\tag{7.4}
$$
只把左侧正次 $\mathsf P$ 移到 $g$ 后用 $\mathsf Pg=0$；
不要求 $CM=M$，不把 $\mathcal R_r^*$ 当作保核算子。
用 (6.5)、(7.3)，得
$$
B(D_0f,g)=0
$$
对全部有限局部全矩阵成立。其不可约性迫 $M=0$。

(2.6) 的全 $C$ 自伴性给稠密值域。
R186 的原循环图核心遂证明 (1.2)，包括实际非零性。

## 8. 新范围例子与未覆盖边界

取正实指数 $1,2,3,4,5$，令
$$
g_1=x_1x_5-\frac58x_2x_4,\qquad
g_2=x_2x_5-\frac56x_3x_4,
$$
$$
F=g_1^2+g_2^2.
\tag{8.1}
$$
$F$ 是非零四次齐次多项式。
在原曲线 $x_\nu=\nu t^\nu$ 上，两个 $g_i$ 都为零，所以
$$
F(\nu t^\nu)=0,\qquad
\nabla F(\nu t^\nu)=0.
$$
本定理仍给任意 $\lambda\ne0$、任意复 $w$ 的
$$
\left[
\left(u_1u_5-\frac58u_2u_4\right)^2+
\left(u_2u_5-\frac56u_3u_4\right)^2-\lambda
\right]e^w
$$
非零且循环。
没有借助曲线上非零梯度，也没有将两个循环向量的平方或和视为自动循环。
这里只展示本定理的直接适用，不声称与任何可能的坐标变换类严格不交。

一般复指数、复系数和更高接触阶同样允许。
但 $\lambda=0$ 时 (3.3) 没有得到非零常数单位，不能沿本稿直接排核。
一般非齐次目标也未必满足 (2.2)。
对 $[F-\lambda]^h$ 或一般 $Q(F)$ 必须重新核完整普通矩逆及证书，不能用 (1.2) 替代。

## 9. 依据和撤回的错误捷径

- [R151](R151-quartic-analytic-approximation-gauge-stability.md) §§2–3：快类的有限和积、真实零字符幂型及联合四次预算的输入。
- [R270B](R270-appendix-local-quadratic-cancellation-and-fast-resonant-carry.md) §§1–3；[R270C](R270-appendix-closed-first-fast-polynomials-and-all-order-resonant-cyclicity.md) §10：至少二阶局部消去的真实共振累积量属于快类。
- [R236 多辅助矩阵](R236-appendix-multiple-summable-auxiliary-matrix-blocks-and-exact-pool-averages.md) §§3、5–9：混合系数有限插值、完整块顶部和原配对。
- [R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)：正分量共同域、规范核、自然词保持、完整图及全 $C$ 自伴。
- [增长正预解引理](../notes/2026-11-13-growing-positive-resolvent-powers-and-actual-multimode-kernel-jets-1cf.md)：原反射壳、倾斜导数和有限头两侧 $A$ 幂；本稿 §4 将所需词深度真实增为 $O(r^2)$，同步把参数改为 $r^{-3}$。
- [合并复对数矩稿](R150-appendix-merged-complex-logarithmic-moment-pools-and-all-resonant-zero-parameters.md)：全部合并比例、完整 Bell、跨池逆的对数费用和原平均常数。

工作中曾考虑从每个 $G_\beta$ 提出一个全域有界的 $A$ 因子；这一步已经撤回。
真实 dyadic 权在 $2^j$ 与 $2^{j+1}-1$ 间有不能忽略的跳跃，快类的强主理想性质也不推出这种有界除法。
本证明只使用独立已证的实际幂界 (3.6)–(3.7)，不需要也不宣称完整 $G_\beta$ 可除以 $A$。

上述全累积量有界除法路线已由[真实二阶快累积量反例](R270-appendix-fast-second-cumulant-has-no-bounded-A-quotient.md)严格排除：即使允许任意 B(H) 商，原正行 a_j=(j+2)^−1 的 G2 也不能除以 A。本文使用的联合四次幂界不受影响。

## 10. 后续独立扩展：有限兼容复权与非普通齐次目标

本节接 §§1–9 的一次非零纤维定理，单独记录后续新增的权范围；normal_resume_1cf 与 Astra-ISP-1cf8c51d 已核完整同键条件、普通矩逆及扩阶量词。
所有矩仍按原物理行准确合并，不能任意给未合并变量独立赋权。

### 10.1 最一般的有限兼容条件

保留原不同复指数 $\rho_\nu$。取非零多项式
$F=\sum_\omega f_\omega x^\omega$，记其普通总次数为 $D\ge1$。
本次完整矩表是全部 $1\le|\omega|\le D$，键为
$$
g(\omega)=(|\omega|,\rho\cdot\omega-|\omega|).
$$

任选有限复权 $\vartheta_1,\ldots,\vartheta_q$，要求两个准确条件：

1. 对本次完整矩表内每一对同键指标，
$$
g(\omega)=g(\omega')
\quad\Longrightarrow\quad
\omega\cdot\vartheta=\omega'\cdot\vartheta.
\tag{10.1}
$$

2. 存在一个固定 $\delta\in\mathbb C\setminus\{0\}$，使
$$
\boxed{f_\omega\ne0\quad\Longrightarrow\quad
\omega\cdot\vartheta=\delta.}
\tag{10.2}
$$

由 (10.1)，每个真实合并变量有良定义的权
$$
\boxed{\vartheta_g=\omega\cdot\vartheta
\quad\text{其中 }g=g(\omega).}
\tag{10.3}
$$
这仅是有限线性方程与一个非零检查；不要求先对无限矩表赋权。
不过 (10.1) 必须检查本次全部 $1\le|\omega|\le D$，不能只检查原 $F$ 支撑上已经出现的指标。

权可以非实、为零或有负实部；证明不需要从它们定义无界缩放流。
因为 $\delta\ne0$，$F$ 的常数项必为零。
以后所有域深度仍按普通整数 $D$ 计算。

**扩展定理。** 在 (10.1)–(10.2) 下，任意 $\lambda\ne0$ 和任意复平方可和指数权 $w$ 都有
$$
\boxed{[F(u_{\rho_1},\ldots,u_{\rho_q})-\lambda]e^w
\text{ 非零且对实际 }A\text{ 循环}.}
\tag{10.4}
$$
$\kappa_\rho$、原物理行和全部 Bell 项均不改变。

### 10.2 自动兼容的一个显式族

给任意固定 $a,b\in\mathbb C$，取
$$
\vartheta_\nu=a+b(\rho_\nu-1).
\tag{10.5}
$$
则所有矩阶上都准确有
$$
\sum_\nu\omega_\nu\vartheta_\nu
=a|\omega|+b(\rho\cdot\omega-|\omega|).
$$
所以这个族自动满足 (10.1)，而
$$
\boxed{\vartheta_{d,s}=ad+bs.}
\tag{10.6}
$$
它是一般有限兼容条件的显式子类，不声称所有有限兼容权都必须具有 (10.5) 的形式。

$a=1,b=0$ 恰回到普通齐次主定理。
$a=b=1$ 给 $\vartheta_\nu=\rho_\nu$，允许对原对数指数齐次、但普通次数不同的目标。
例如 $\rho=(1,2)$、$F=x_1^2+x_2$ 满足 $\delta=2$；这只是展示权条件，双模式的该例已在原全多项式定理范围内，不另计新例。
在这个显式族内，(10.2) 恰为原有限支撑的键落在
$ad+bs=\delta\ne0$ 上。

### 10.3 完整普通矩逆确实保该权

普通矩逆 $\mathcal Q_F(Y)$ 的每一项，来自把原 $x^\omega$ 的有限多重指标拆成若干块。
对应矩变量 $Y_{\beta_1}\cdots Y_{\beta_\ell}$ 满足
$\beta_1+\cdots+\beta_\ell=\omega$，所以其总复权恰为
$\omega\cdot\vartheta=\delta$。
所有块的普通总阶都不超过 $D$，属于 (10.1) 已完整检查的表。
常数系数与全部阶乘不影响权。

由 (10.1)、(10.3)，代入
$Y_\omega=(\prod_\nu\rho_\nu^{\omega_\nu})W_{g(\omega)}$
后，准确合并的 $Q(W)$ 仍满足
$$
\mathscr E_\vartheta Q=\delta Q,\qquad
\mathscr E_\vartheta=\sum_g\vartheta_gW_g\partial_{W_g}.
\tag{10.7}
$$
这证明的是完整普通到共振有限逆的恒等式，不能只检查原 $F$ 后跳过矩合并。

原物理行的实际累积量 $G_\beta$ 与 §§2–3 完全相同。
令
$$
\vartheta(\beta)=\sum_g\beta_g\vartheta_g,\qquad
\mathscr L_\vartheta=
\sum_{2\le|\beta|\le D}
\frac{\vartheta(\beta)G_\beta}{\beta!}\partial_W^\beta.
$$
真正的有限微分交换子给
$$
[\mathscr E_\vartheta,\mathscr L]=-\mathscr L_\vartheta,\qquad
\mathscr E_\vartheta P_0=\delta P_0-\mathscr L_\vartheta P_0.
\tag{10.8}
$$
对 $P=P_0-\lambda I$，定义
$$
E_\vartheta(W)=(\delta\lambda)^{-1}\mathscr L_\vartheta P_0(W).
$$
便有全多项式恒等式
$$
\boxed{
\sum_g\frac{\vartheta_gW_g}{\delta\lambda}\partial_{W_g}P
=I-E_\vartheta+\lambda^{-1}P.
}
\tag{10.9}
$$
$\delta$ 和 $\lambda$ 都要求非零；本节没有在其为零时强行使用该式。

### 10.4 复权不改变真实定义域和费用

$E_\vartheta$ 的每个非零单项式系数仍是有限个 $G_\beta$ 的多项式，且每项至少含一个 $G_\beta$。
因此它们属于 $\mathcal G$，字符为零。
R151 的真实幂型给同样的有限联合四次预算。
复权只进入固定标量系数，不改变该估计。

具体地，在 §§4–7 中替换
$$
E\mapsto E_\vartheta,\qquad
\frac{d_gW_g}{D\lambda}\mapsto
\frac{\vartheta_gW_g}{\delta\lambda}.
$$
取
$$
H_r=\sum_{k<r}E_\vartheta^k,\qquad
B_{g,r}=\frac{\vartheta_gW_g}{\delta\lambda}H_r.
$$
原完整 $P$ 上的块证书仍是
$$
\sum_gB_{g,r}\partial_gP
=I-E_\vartheta^r+\lambda^{-1}H_rP.
\tag{10.10}
$$
因此在同一个原规范核内，$r$ 个实际矩块的顶部准确为
$(I-E_\vartheta^r)^r$。

所有次数上界按普通 $D$，而不是按 $|\delta|$ 或 $\operatorname{Re}\vartheta_g$。
完整多项式仍只有有限项，
$q_r=(8D+8)(r+1)^2$、$\epsilon_r=r^{-3}$
支付全部 $O(r^2)$ 原自然词，强趋 $I$ 的证明不变。
全部新固定标量最多改变 $C$，所以
$$
\|[(I-E_\vartheta^r)^r-I]\mathcal R_r\|
\le e^{-cr^4},\qquad
A_N\le e^{Cr^2\log(r+2)+Cr\log N}
$$
对充分大 $r$ 成立。
原合并池的完整逆、反射壳、真实 carry、两侧 $A$ 四次预算和原 $C$ 配对均保持同一顺序。
遂由 §§6–7 的已付证明得到 (10.4)。

### 10.5 点态幂及一般外层复合的边界

若再考虑整个 $F^h$，它按原权确有总权 $h\delta\ne0$。
但其完整矩表扩大到普通阶 $hD$。
所以对于一般仅满足有限 (10.1) 的权，必须在这个扩大的表上重新检查同键兼容，才可以推出 $[F(u)^h-\lambda]e^w$ 循环。
不把对阶 $D$ 的有限兼容免费延到所有阶。

对于自动兼容族 (10.5)，这一额外检查始终成立；
因而该族的全部 $F(u)^h-\lambda$，$h\ge1$、$\lambda\ne0$，都可对整个目标重做证明。

一般 $[F(u)-\lambda]^h$ 或一般 $Q(F(u))$ 是不同总权的和，本节不据此声称已经覆盖。
总权为零、零纤维及未满足完整同键兼容的目标，也仍不由本节排核。

