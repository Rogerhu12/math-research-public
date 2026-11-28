# R1153：原 Kummer 多项式与有限 Fontaine–Laffaille 坐标的精确校准

> **局部校准补全，[R1180](R1180-original-Lubin-Tate-absolute-Kummer-Frobenius-calibration.md)。** 原同一 ζ 的严格 LT 与独立局部测试类现证明 F_j=γ^(2j)ℓ_j（j=1,2），从而 U_E=γ_E²、η★=1 对全部分支成立，包括两个 Bernoulli 局部值同时为零；不需 generic SS 校准点。本文原条件性检测保持为旧证明，校准限制由该新自足论证解除；全局生成性及其它范围不改。

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；global_route。

**已证明，纸面。** 对任何具有一个非特殊 $\mathbf F_p$-有理超奇异点的素数 $p>37$，本篇把 R1071 的同一原 Kummer leading 多项式与 R1147–R1151 的同一有限 Fontaine–Laffaille 两槽完全对齐。第一槽的实际比较单位是
$$
U_\star=4\delta c_{g,\star}^{\,2}\beta_\star^2,
$$
第二槽是 $U_\star^2$；运输到其它原参考点时，分别再乘真实 Weil 相位的平方与四次方。这是两条完整局部 $H^1$ 直线的比较，包含 Bernoulli-bad 情形，没有反除一个可能为零的圆单位。

存在一个绝对常数 $C_{\rm SS}$，使每个 $p>C_{\rm SS}$ 都满足上述校准点条件。它与 R1148 的 $C_{\rm cyc}$ 分开保留：需要全部 global labels 的原生成性时，取 $p>\max(C_{\rm SS},C_{\rm cyc})$，不声称已显示的 $C_{\rm cyc}$ 大于此处未显示的 $C_{\rm SS}$。

以下还逐项读取原 $q_t$ 可见的 $X_0,Y_0$ coefficients，特别是 Gaussian 的 $x_4,y_8$ 和 cubic 的 $y_7$。中央 $z_{12}$ 不由本篇确定；实际中央减法仍保 R1151 的整个 global term。没有数学程序执行，没有重跑固定素数或辅助筛。

## 1. 同一曲线、角色和两个局部线性读数

固定
$$
p>37,\qquad m=(p-1)/2,\qquad
\chi_j=\omega^{-2j},\quad R_j=p-1-2j,\quad j=1,2.
\tag{1153.1}
$$
两角色都在原 forced cuspidal 模块中。$F_1,F_2$ 始终是 R1070、R1144、R1146 的原 leading-normalized 函数，不将它们换成一个任意同角色函数。

保持同一个 Cartan 非平方 $\delta\in\mathbf F_p^\times$、同一个 $\varpi^{p^2-1}=p$，以及原 Tate generators。记
$$
K_p=\mathbf Q_p(\zeta_p),\qquad L_r=\mathbf F_p(r).
$$
对于 $\xi\in H^1(\mathbf Q_p,L_{2j+1})$，在一个固定实际根 $\zeta_\star$ 下准确写
$$
\operatorname{res}_{K_p}\xi
 =\kappa(u_\xi)\otimes\zeta_\star^{\otimes 2j},
\qquad
[u_\xi]\in(K_p^\times/K_p^{\times p})_{\chi_j}.
\tag{1153.2}
$$
restriction 在这里单射，并由次数 $p-1$ 的 descent 给到相应不变量的同构。$\chi_j$ 是非平凡偶角色，故 (1153.2) 的 Kummer 类可在 real local field 的 principal units 中表示。

R1071 §7 的真实 log/exp 与 character filtration 证明：该偶角色准确一维，最早 cyclotomic 阶为 $R_j$。因此
$$
\ell_{j,\star}(\xi)
 =\overline{\varpi^{-(p+1)R_j}\log u_\xi}
\tag{1153.3}
$$
是这一局部 $H^1$ 的完整线性同构到 $\mathbf F_p$。它对 $p$ 次幂代表改变不变；高于该阶的所有剩余项已由原 filtration 排除。特别没有使用 $B_{R_j}$ 非零。

另一方面，R1151 (1151.2)–(1151.6) 在同一 Tate frame 给两条线性同构
$$
\mathcal F_j:H^1(\mathbf Q_p,L_{2j+1})\longrightarrow\mathbf F_p,
\qquad j=1,2.
\tag{1153.4}
$$
它们是原 finite Fontaine–Laffaille divided-Frobenius 坐标。R1150 的相对关联和 R1149 §12 保证下面评价的两个实现确实来自同一格、同一 torsor 和同一 point，不只是两个有理同构类。

故先验存在唯一 $u_j\in\mathbf F_p^\times$，使
$\mathcal F_j=u_j\ell_{j,\star}$。本篇通过一个实际非零最高项求出这两个数，而不从维数推出它们等于一。

## 2. 一个真正的 $\mathbf F_p$ 校准参考与充分大范围

### 2.1 原参考的存在

设 $\bar E_\star/\mathbf F_p$ supersingular，且
$j(\bar E_\star)\notin\{0,1728\}$。取其实际模型
$$
\bar E_\star:y^2=x^3+\bar A_\star x+\bar B_\star,
\qquad \bar A_\star\bar B_\star\ne0.
$$
R1066 §§2–3 对这个实际模型及实际 Frobenius 构造 arithmetic-stable、不分歧二次 CM reference
$E_\star/\mathbf Z_p$。它保持指定 reduction，底曲线定义在 $\mathbf Q_p$；CM endomorphisms 可在未分歧二次域上定义。其原标记、微分 $\omega=dx/(2y)$ 和 Cartan 一起保留。

此处不要求该 reference 是 $\mathbf Q$-有理 CM 点，也不将它的局部 fibre 擅称一个全局 label。它只用来比较 (1153.3)、(1153.4) 这两条真正定义在 $\mathbf Q_p$ 上的线性读数。

### 2.2 每个充分大的 p 都有这样的点

令 $h_p$ 为**二次域** $\mathbf Q(\sqrt{-p})$ 的类数。Deuring 的原计数为
$$
L(p):=\#\{j\in\mathbf F_p:j\text{ supersingular}\}
 =
\begin{cases}
h_p/2,&p\equiv1\pmod4,\\
2h_p,&p\equiv3\pmod8,\\
h_p,&p\equiv7\pmod8.
\end{cases}
\tag{1153.5}
$$
例如已刊 Morton 2021 §1、Theorem 1.2 前的显示式明确采用此 field-class-number 约定；Pizer 1978 Lemma 2.6(b) 的 type-number 公式与 Deuring 的 Frobenius-orbit 对应给同一计数。

Heilbronn 的类数增长定理给 $h(D)\to\infty$，其中 $D<0$ 遍历 fundamental discriminants。这里两种实际判别式为
$$
D_p=-4p\quad(p\equiv1\bmod4),\qquad
D_p=-p\quad(p\equiv3\bmod4).
$$
它们的绝对值均随 $p$ 趋于无穷。因此存在绝对 $C_{\rm SS}>37$，使 $p>C_{\rm SS}$ 时 $h_p>4$，从而 (1153.5) 给 $L(p)>2$。

(1153.5) 数的是互异 $j$，已经处理了原 Frobenius-orbit 及 twist 的有限重数；不是将 CM ideal classes 不加区分地当作互异 $j$。删除至多两个值 $0,1728$，便得到 §2.1 的校准点。特别没有用只有 $\mathbf F_{p^2}$ 定义的 supersingular point 来替代这个 $\mathbf F_p$ 条件。

本篇对任何已经具有此点的 $p>37$ 成立；$p>C_{\rm SS}$ 只给一个统一充分范围，不报告未经执行的有限例外表。

## 3. 原 first-lift 参数与未除圆单位的完整 profile

对任一上述 $\mathbf Q_p$ supersingular CM reference $E_0$，记
$$
H_p(A,B)=[x^{p-1}](x^3+Ax+B)^m,\qquad
\beta_p(A,B)=[x^{p-2}](x^3+Ax+B)^m,
$$
$$
\beta_E=\beta_p(\bar A_0,\bar B_0)\in\mathbf F_p^\times.
\tag{1153.6}
$$
$\beta_E\ne0$ 已由 R1075 §3 的原 Cartier/Hasse 简单零论证支付。

选一个原整代数参数 $u$，使参考点处 $K_\omega/du=1$，并令其 first-order tangent 是
$$
\partial=6B_0\partial_A-\frac43A_0^2\partial_B.
$$
例如可取直线代数 chart
$A=A_0+6B_0u,\ B=B_0-\frac43A_0^2u$，再限在判别式为单位的 formal 邻域。这里只指定一阶，不把完整 chart 认成无限 heat-time 流。对 $u=pt$，R1071 (1071.57) 的实际 $p^2$ first-lift 比较和 R1149 (1149.47) 给
$$
t_*=[T^p][p](T)/p=\beta_E t\pmod p.
\tag{1153.7}
$$
Gaussian/cubic 时正是 R1149 (1149.48) 的原两个 chart。

保 R1071 §§11–14 的 tangent-one formal eigenparameter、原 torsion branch $\bar\beta_0=1$，故该文的 **source** $\bar\lambda_{\rm old}=-1$。它与下文 crystalline frame 的 $\lambda$ 是两个不同量。

选共同原奇 auxiliary $c$，使
$$
\kappa_j(c)=c^2-\chi_j(c^2)
$$
为单位。写同一个 $\psi_c$ 的 logarithmic derivative coefficients 为 $\bar A_d$，并置
$$
N_j=(p+1)R_j,\qquad d_{j,i}=N_j-(p-1)i.
$$
定义
$$
\boxed{
Q_{j,E}(t_*)=
 \frac1{2\bar\kappa_j(c)}
 \left(
  \frac{\bar A_{N_j}}{N_j}
   +\sum_{i=1}^{I_j}(-1)^i\bar A_{d_{j,i}}\,
       \frac{\binom{d_{j,i}-1}{i-1}}i\,t_*^i
 \right).
}
\tag{1153.8}
$$
$I_j$ 可先取 R1071 的 $\lfloor N_j/(p-1)\rfloor$；原 Lucas 消去准确给
$$
\deg Q_{1,E}\le3,\qquad \deg Q_{2,E}\le5.
\tag{1153.9}
$$

(1153.8) 就是 R1071 (1071.37) 的分子：保原 $m/\kappa_j$、半向量根和及 leading normalization，但**没有除以** $b_{\chi_j}$。所以它读取同一个 $F_j$ 的完整局部类，即使 $B_{R_j}=0\bmod p$ 仍然有定义。原 auxiliary 的不同合法选择给同一类，因而给同一 (1153.8)。

以下记
$$
\widehat Q_{j,E}(t)=Q_{j,E}(\beta_Et)
 =\sum_{i=0}^{2j+1}q_{j,i}(E)t^i.
\tag{1153.10}
$$
所有 coefficients 都按原实际 $\mathbf F_p$ descent line 读取。它们是代表有限点函数的次数小于 $p$ 多项式；不在形式环中使用 $t^p=t$。

## 4. 两个原顶项的完整 theta-cycle 计算

为自足地支付第二槽，扩写 R1075 已用的同权恒等式。用原 coefficient-one Eisenstein series
$$
\mathcal E_d=-B_d/(2d)+\sum_{n\ge1}\sigma_{d-1}(n)q^n,
\qquad
G_d=\frac2{(d-1)!}\mathcal E_d.
$$
最后一式是原 $\omega$ / Hurwitz 归一，不改成 constant-one Eisenstein。令 $H=E_{p-1}$、$J=E_{p+1}$，原同权 theta 算子为
$$
\mathcal T_wf=H\partial_wf+\frac w{12}Jf.
$$
对 $r=6,10$，逐个除数的换元，连同 $p\mid n$ 项和常数项，给
$$
\mathcal T^{p-r}\mathcal E_r
 =H^{p+1-r}\mathcal E_{p+1-r}
      -\mathcal E_{p+1-r}^{\,p}.
\tag{1153.11}
$$
两边权都为 $p(p+1-r)$；保留右边 Frobenius 项。所有 Eisenstein series 和所用 factorial 均 $p$ 整，原固定权 $q$ 原理与 R1075 §1 相同。

在 supersingular point 上，每一步只乘当时的权与 $\beta_E$，因为带 $H$ 的导数项为零。权乘积为
$$
\prod_{i=0}^{p-r-1}(r+i(p+1))
 =\prod_{a=r}^{p-1}a=-1/(r-1)!.
$$
再用 Wilson，准确得
$$
G_{p+1-r}^{\,p}=(r-1)!\,\beta_E^{p-r}G_r.
\tag{1153.12}
$$
原 short equation 给
$$
G_6=-B/35,\qquad G_{10}=AB/1155.
$$
第二式也可从 $x''=6x^2+2A$ 直接读取：
$[T^8]x=3AB/385=9G_{10}$。因此
$$
G_{p-5}^{\,p}=-\frac{24}{7}B\beta_E^{p-6},\qquad
G_{p-9}^{\,p}=\frac{3456}{11}AB\beta_E^{p-10}.
\tag{1153.13}
$$
这里先保实际 $p$ 次幂；只在本篇 $\mathbf F_p$ 模型和原微分下才将其删去。

在 (1153.8) 的顶部 $i=2j+1$，有
$$
d_{j,i}=p(p-4j-1),\qquad
\binom{d_{j,i}-1}{i-1}=1\pmod p.
$$
原 Cartier identity 给 $\bar A_{pn}=\bar A_n^p$，原 sigma identity 给
$$
\bar A_{p-4j-1}=\bar\kappa_j(c)\,G_{p-4j-1}.
$$
所以该顶项是 $-G_{p-4j-1}/(2(2j+1))$。合并 (1153.7)、(1153.13) 后，
$$
\boxed{
q_{1,3}(E)=\frac{4\bar B_0}{7\beta_E^2},
\qquad
q_{2,5}(E)=-\frac{1728\bar A_0\bar B_0}{55\beta_E^4}.
}
\tag{1153.14}
$$
校准 reference 的 $\bar A_\star\bar B_\star\ne0$，故两项都非零。此非零不涉及 $B_{p-3}$ 或 $B_{p-5}$。

## 5. generic 参考上的实际有限 FL 顶项

R1149 §13 原先在两个特殊 CM reference 写出 frame。这里将校准所需部分明确付到 §2 的 generic reference。

在同一 $\mathbf Q_p$ reference 的原 FL 格中，$\nu=\nu(\omega)$ 与
$\mu_g=\nu(x\omega)$ 是整基，保持
$$
\langle\nu,\mu_g\rangle=c_g\tau_1,\qquad c_g\in\mathbf Z_p^\times.
$$
supersingular 简单 finite FL 表示使 $\varphi\nu\bmod p$ 在
$M/\mathbf Z_p\nu$ 上的系数非零。因此可且唯一地写
$$
\varphi\nu=\lambda(\mu_g+d\nu),\qquad
\lambda\in\mathbf Z_p^\times,\quad d\in\mathbf Z_p.
\tag{1153.15}
$$
置 $\mu^\circ_g=\mu_g+d\nu$、$\mu=\varphi\nu=\lambda\mu^\circ_g$。
这两条替换保持整性和原 cup unit $c_g$。若使用 R1066 reference 的 CM idempotents，$\mu^\circ_g$ 也就是相应整 opposite line；本节最高项只需 (1153.15) 的实际单位结论。

由于底域是 $\mathbf Q_p$，coefficient Frobenius 为恒等。原 special-fibre trace-zero Frobenius 给
$$
p\varphi\mu=-\nu.
$$
注意对 $\mu^\circ_g$ 则是 $p\varphi\mu^\circ_g=-\lambda^{-1}\nu$，不能漏 $\lambda^{-1}$。

原 $K_\omega/du=1$ 意味 $\nabla_{\partial_u}\nu$ 的
$\mu^\circ_g$ coefficient 为一；可能的 $\nu$ 项保持 filtration，不属于 $N_-$。因此 R1149 §11 的最高过滤 Taylor 证明原样适用。具体地，它仍给
$$
\mu_s=\mu-(t/\lambda)\nu,\qquad
q_t(x\nu+y\mu)=-2a\lambda c_g\,y(x+(t/\lambda)y)\tau_1,
\quad a^2=\delta.
\tag{1153.16}
$$
其它原连接项只影响较低次数，不影响随后的两个最高项。

R1149 §§8–10、R1150 已识别同一原 connection：
$$
\alpha_4=\frac{1-p^4}{252}E_6\,\nu^4\tau_1K_\omega,\qquad
\alpha_8=\frac{1-p^8}{132}E_{10}\,\nu^8\tau_1K_\omega.
$$
按原 $E_6=864B$、$E_{10}=-41472AB$，再按 R1149 (1149.38)–(1149.42) 在终点同一个 $q_t$ 下取 finite primitive，得到
$$
\boxed{
[t^3]\mathsf a_\star(t)
 =\frac{16}{7}\delta c_{g,\star}^{\,2}\bar B_\star,
\qquad
[t^5]\mathsf b_\star(t)
 =-\frac{27648}{55}\delta^2c_{g,\star}^{\,4}
          \bar A_\star\bar B_\star.
}
\tag{1153.17}
$$
参考 $F_0$ 的两槽分别只贡献次数至多二、四；常数 twist
$k\,s$ 也不改变五次项。这里保留 $F_0$，没有从相对 connection 将它设为零。

## 6. 比较单位与实际 Miller 相位

在校准点的实际根 $\zeta_\star=e_p(P_\star,Q_\star)$ 下，(1153.8) 与 (1153.17) 读取的是同一 (1153.2) 类。由 §1 的一维性，它们在整个局部直线的比例是固定数。

两边有限多项式次数都小于 $p$，且对全部 $t\in\mathbf F_p$ 的实际点相等，所以可以比较最高 coefficient；这不使用形式导数或 Hensel。由 (1153.14)、(1153.17)，
$$
\boxed{
\mathcal F_1=U_\star\ell_{1,\star},\qquad
\mathcal F_2=U_\star^2\ell_{2,\star},\qquad
U_\star=4\delta c_{g,\star}^{\,2}\beta_\star^2\ne0.
}
\tag{1153.18}
$$
特别第二槽不能误写成 $U_\star$。此等式是同一 $\mathbf Q_p$ 上两条完整局部 $H^1$ 的线性比较，不以一个 $\mathbf F_{p^2}$ point 代替校准。

现在取其它同一原标记规范下的 $\mathbf F_p$ reference $E$。R1071 §13 的真实有限 Miller 算法给
$$
\gamma_E=\overline{\frac{e_p(P,Q)-1}{\varpi^{p+1}}},
\qquad
\gamma_\star=\overline{\frac{\zeta_\star-1}{\varpi^{p+1}}},
\qquad
a_E=\gamma_E/\gamma_\star\in\mathbf F_p^\times,
$$
$$
\zeta_E=\zeta_\star^{a_E},\qquad
\gamma_E^{p-1}=\gamma_\star^{p-1}=-1.
\tag{1153.19}
$$
后一幂式只核相位范围，不能代替前面的实际 Miller 值。

由 R1146 (1146.4)，同一 descended class 在两根下的 tensor 为
$$
\kappa(F_j(E))\otimes\zeta_E^{\otimes2j}
 =a_E^{2j}\kappa(F_j(E))\otimes\zeta_\star^{\otimes2j}.
$$
等价地，R1071 §14 的 norm-$a_E^{-1}$ Cartan 重标把 raw bracket 乘
$a_E^{-R_j}=a_E^{2j}$。因此真实 phase transport 为
$$
Q_{j,E}^{\,\star}=a_E^{2j}Q_{j,E}.
\tag{1153.20}
$$
此证明在 Kummer/tensor 层完成，不要求 $b_{\chi_j}\ne0$。good 情形也可由
$b_{\chi_j,E}=a_E^{R_j}b_{\chi_j,\star}$ 核准同一个方向。

记
$$
U_E=U_\star a_E^2,\qquad k=8\delta^2/11.
$$
R1146 第二槽的常数类恰为 $k\gamma_5$，R1151 记其同一 FL 坐标为 $ks$。故对整个原有限点集，准确有
$$
\boxed{
\mathsf a_E(t)=U_E\widehat Q_{1,E}(t),\qquad
\mathsf b_E(t)=U_E^2\widehat Q_{2,E}(t)+ks.
}
\tag{1153.21}
$$
没有分别重新选两条线的基，也没有删除第二槽的常数 twist。

换校准 reference 得到的是同一 (1153.4)，所以 (1153.21) 与校准选择无关；该结论来自已证明的整线比较，而不是预设所有 reference 的 $\gamma_E$ 相同。没有宣称 $U_\star=\gamma_\star^2$，也没有从 $\gamma^{p-1}=-1$ 猜出尚未比较的 principal-polarization scalar。

## 7. 原全局两生成元的准确局部零分支

令
$$
\epsilon_{2j}=\sum_{b\in\mathbf F_p^\times}
 b^{2j}\kappa(1-\zeta_\star^b).
$$
按 R1148 (1148.23)，若 $a_0$ 是原圆单位使用的奇生成元，
$$
\beta_{\chi_j}=(1-a_0^{-2j})\epsilon_{2j}.
\tag{1153.22}
$$
这里 $a_0$ 与 (1153.19) 的相位 $a_E$ 是两个不同量。原 $\gamma_3,\gamma_5$ 的 restriction 分别是
$\epsilon_2\otimes\zeta_\star^{\otimes2}$、
$\epsilon_4\otimes\zeta_\star^{\otimes4}$。

R1071 (1071.24) 因而给
$$
\ell_{j,\star}(\operatorname{loc}_p\gamma_{2j+1})
 =-\frac{B_{R_j}}{R_jR_j!}\gamma_\star^{R_j}.
\tag{1153.23}
$$
这是一次准确相除：$1-a_0^{-2j}$ 是单位；没有除以 $B_{R_j}$。
Wilson 及 $\gamma_\star^{p-1}=-1$ 分别给
$$
\frac{-\gamma_\star^{p-3}}{(p-3)(p-3)!}
 =\frac23\gamma_\star^{-2},\qquad
\frac{-\gamma_\star^{p-5}}{(p-5)(p-5)!}
 =\frac{24}{5}\gamma_\star^{-4}.
$$
故 R1151 的同一 $r,s$ 准确为
$$
\boxed{
r=\frac23U_\star\gamma_\star^{-2}B_{p-3},\qquad
s=\frac{24}{5}U_\star^2\gamma_\star^{-4}B_{p-5}
\quad\bmod p.
}
\tag{1153.24}
$$
所有显式乘子均为单位，因此
$$
r=0\Longleftrightarrow p\mid B_{p-3},\qquad
s=0\Longleftrightarrow p\mid B_{p-5}.
\tag{1153.25}
$$
这里只读首层，不据此宣称更高精确 valuation 相等。R1148 的全局生成性与这里的局部零分支仍是不同断言。

若相应 Bernoulli 为单位，原 R1071 候选坐标
$c_{\chi_j,E}=Q_{j,E}/b_{\chi_j,E}$ 遂满足
$$
\mathsf a_E(t)
 =r(1-a_0^{-2})c_{\chi_1,E}(\beta_Et),
$$
$$
\mathsf b_E(t)
 =s\bigl((1-a_0^{-4})c_{\chi_2,E}(\beta_Et)+k\bigr).
\tag{1153.26}
$$
这只是 (1153.21) 的 good-branch 写法；bad branch 应继续使用未除圆单位的 (1153.21)。

## 8. 原参考 Frobenius 两槽的全部可见 coefficients

在 R1149 的实际 $(\nu,\mu)$ frame 中写
$$
X_0=\sum_{i=0}^4x_i\nu^{4-i}\mu^i\tau_1,\qquad
Y_0=\sum_{i=0}^8y_i\nu^{8-i}\mu^i\tau_1.
$$
这里 $\mu=\varphi\nu=\lambda\mu_g$ 在 Gaussian/cubic 的原 frame 下，
generic 校准时用 (1153.15)。保持原 $c_g,\lambda$，不将 $\lambda$ 与
$\lambda_{\rm old}=-1$ 混同。

R1149 (1149.36)、(1149.43) 准确给
$$
P_a(t)=
 2\delta c_g^2\sum_{i=2}^4
 \lambda^{4-i}\frac{\binom2{i-2}}{\binom4i}\,x_i t^{i-2},
$$
$$
P_b(t)-ks=
 8\delta^2c_g^4\sum_{i=4}^8
 \lambda^{8-i}\frac{\binom4{i-4}}{\binom8i}\,y_i t^{i-4}.
\tag{1153.27}
$$
原 increment 的两项只在次数三、五，所以 (1153.21) 对较低 coefficient 逐项给
$$
\boxed{
x_i=
 \frac{U_E q_{1,i-2}(E)}
      {2\delta c_g^2\lambda^{4-i}}
 \frac{\binom4i}{\binom2{i-2}},
\qquad 2\le i\le4,
}
$$
$$
\boxed{
y_i=
 \frac{U_E^2 q_{2,i-4}(E)}
      {8\delta^2c_g^4\lambda^{8-i}}
 \frac{\binom8i}{\binom4{i-4}},
\qquad 4\le i\le8.
}
\tag{1153.28}
$$
这些二项式分母及 $\lambda$ 全为单位。特别常数槽的 $ks$ 已在两边同步扣除，没有进入 $y_4$。

这确读取该一参数原 $q_t$ 所能见到的整个 $X/Y$ 部分：
$x_2,x_3,x_4$ 和 $y_4,\ldots,y_8$。$x_0,x_1$ 及 $y_0,\ldots,y_3$ 被
$q_t^2,q_t^4$ 对所有 $t$ 恒杀；本篇不以两条 profile 伪称恢复了原
$5$ 维和 $9$ 维 reference vector 的全部条目。不过实际 quotient 的两槽多项式已由 (1153.21) 完全决定。

### 8.1 Gaussian 与 cubic 所需条目

在 Gaussian reference，
$$
x_4=\frac{U_E q_{1,2}(E)}{2\delta c_g^2},
\qquad
y_8=\frac{U_E^2 q_{2,4}(E)}{8\delta^2c_g^4}.
\tag{1153.29}
$$
在 cubic reference，
$$
y_7=\frac{U_E^2 q_{2,3}(E)}
          {4\delta^2\lambda c_g^4}.
\tag{1153.30}
$$
其余可见 coefficients 同样由 (1153.28) 给出；原 CM symmetry 所迫的零随之保持。Gaussian 的两实际 twist lines 及其它扩域表述仍必须同步运输原 root、模型、$\sigma(\lambda)$ 和参数；一个固定 $\mathbf Q_p$ fine chart 不被冒称全部 coarse 支路。

## 9. 对实际中央减法的精确后果，以及保留的输入

假设 $rs\ne0$。R1151 的真正 obstruction polynomial 是
$$
\mathcal D=rs\,\mathsf h-z\,\mathsf a\mathsf b,
$$
其中 $z$ 来自同一原 global torsor $\Theta$。R1152 对 $z/(rs)$ 的已付表示可在其原范围消费；不能将 $z$ 设为零。

Gaussian 情形 $T=t^2$，(1151.16)、(1153.29) 给
$$
\boxed{
[T^3]\mathcal D
 =16\delta^3c_g^6rs\,z_{12}
      -z\,U_E^3q_{1,2}(E)q_{2,4}(E).
}
\tag{1153.31}
$$
cubic 情形 $T=t^3$，记
$a_3=16\delta c_g^2\bar B_0/7$，则
$$
\boxed{
[T^2]\mathcal D
 =16\delta^3c_g^6rs\,z_{12}
      -z\,a_3U_E^2q_{2,3}(E).
}
\tag{1153.32}
$$
这两式已把 abelian product 的每个尺度变为同源旧 profile 的已知有限读数，保留的主要新局部项正是原 $F_0$ 的 $z_{12}$。较低中央 coefficients、其与同一 $z$ 的 subtraction 也仍须实际读取。

即使某个原 profile 的 coefficient 为单位，也不因此推出
(1153.31) 或 (1153.32) 非零。所有本篇有限多项式等式都按
$t\in\mathbf F_p$ 的实际 points 使用，不将 formal $t^p$ 替为 $t$ 后取导数，不由一次有限零条件推出整个 $p$-adic disk 的唯一性。

## 10. 原来源与核对范围

- [R1066](R1066-original-p-local-disks-and-bounded-CM-representatives.md) §§2–4：实际 $\mathbf F_p$ supersingular 模型、arithmetic-stable CM lift、整 reference 及 $\mathbf Q_p$ 下降；没有任意搬用 $\mathbf F_{p^2}$ 标架。
- [R1071](R1071-original-p-local-cuspidal-label-polynomials.md) §§5–7、11–17：完整 raw leading、全部高分母、有限 first lift、$\lambda_{\rm old}$、Cartier/Lucas、实际 Miller 和原 phase。
- [R1075](R1075-original-Hurwitz-unit-and-first-cuspidal-slope.md) §§1–3：任意 supersingular reference 的原 theta/Hurwitz/Cartier 规范；本篇 §4 自足补写权十同源式。
- [R1146](R1146-original-proper-arithmetic-Heisenberg-cover.md) (1146.1)–(1146.4)：原两函数、常数 twist 及 $\zeta^{2j}$ 的实际下降。
- [R1148](R1148-original-canonical-cusp-Heisenberg-and-minus-one-Frobenius.md) §§10–11：原 $\epsilon_d,\gamma_{d+1}$、全局生成范围与精确圆单位因子。
- [R1149](R1149-original-relative-Hodge-section-and-central-connection.md) §§11–17、[R1150](R1150-original-relative-log-Frobenius-and-crystalline-identification.md)、[R1151](R1151-original-finite-Frobenius-global-subtraction.md)：同一原格/相对关联、有限 Taylor/Cartan、全局减法；本篇 §5 明确付其 generic 校准所需延伸。
- P. Morton, *The Hasse invariant of the Tate normal form $E_5$ and the class number of $\mathbf Q(\sqrt{-5l})$*, **Journal of Number Theory 227 (2021), 94–143**，[DOI](https://doi.org/10.1016/j.jnt.2021.03.006)，[作者全文](https://arxiv.org/pdf/2002.04134)，§1、作者版第6页 Theorem 1.2 前显示式，明确 (1153.5) 的 Deuring 计数及 field class number。另见 A. Pizer, *A note on a conjecture of Hecke*, **Pacific J. Math. 79 (1978), 541–548**，[已刊全文](https://msp.org/pjm/1978/79-2/pjm-v79-n2-p16-s.pdf)，Lemma 2.6(b)，印刷544页。
- H. Heilbronn, *On the class-number in imaginary quadratic fields*, **Quart. J. Math. Oxford os-5 (1934), 150–160**，[DOI](https://doi.org/10.1093/qmath/os-5.1.150)。其准确增长结论也由作者在 H. Heilbronn–E. H. Linfoot, *On the imaginary quadratic corpora of class-number one*, **同刊 os-5 (1934), 293–301**，[已刊扫描](https://sites.math.duke.edu/~dasgupta/Transcendence/hl.pdf)，印刷294页 Theorem 3' 后明确陈述；本篇只消费 $h(D)\to\infty$，不消费任何未显示有效界。

以上新的比例、phase、general-reference 过滤项、两个顶项、Wilson 常数、全部可见 coefficients 和中央代入均为正文纸面推导。没有数学程序执行。主目标及原中央最高组合的非零性仍未完成。
