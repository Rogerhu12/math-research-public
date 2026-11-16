# R850 — 原光滑三阶商、最高 Chow 投影与精确循环运输

日期：2026-11-16。**状态：下述光滑商、原最高动机的双向对应、指定原曲线的 degree3 运输及微分归一已证明。**

本篇接 R848 的同一个原曲线来源，支付先前未支付的光滑商与 Chow 投影。
它把原最高循环放到一个固定的光滑刚性 Calabi–Yau 三维簇上；
不由三维簇的名称或第三 Betti 数为2断言 Chow 群一维，
也不把这个运输本身认作 R814 指定 canonical 类的比较。

## 1. 原目标与完全固定的三阶作用

保持
$$
E_0:y^2=x^3+1,\qquad K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,
\qquad A=E_0^3.
\tag{1}
$$
原同一三阶作用为
$$
R_A=([\omega],[\omega],[\omega]),\qquad
[\omega](x,y)=(\omega x,y).
\tag{2}
$$
原有理三微分固定为
$$
\Omega_A=
\frac{dx_0}{2y_0}\wedge
\frac{dx_1}{2y_1}\wedge
\frac{dx_2}{2y_2}.
\tag{3}
$$
有 $R_A^*\Omega_A=\Omega_A$。

在每个 $E_0$ 上，$[\omega]$ 的固定点准确为
$$
E_0[1-\omega]=\{O,(0,1),(0,-1)\}.
$$
故 $A$ 上的固定中心
$$
\mathcal F=E_0[1-\omega]^3
\tag{4}
$$
准确是27个 $\mathbf Q$-有理点。令
$$
b:\widetilde A=\operatorname{Bl}_{\mathcal F}A\longrightarrow A.
\tag{5}
$$
作用提升为 $\widetilde R$。虽然选定生成元(2)在 $K$ 上定义，
其循环子群由 $G_{\mathbf Q}$ 保持，也可视为定义于 $\mathbf Q$
的对角 $\mu_3$ 作用。因此商
$$
q:\widetilde A\longrightarrow
Z=\widetilde A/\langle\widetilde R\rangle
\tag{6}
$$
及下文的平均对应都在 $\mathbf Q$ 上定义。
没有为此增加一个与17有关的新定义域。

## 2. 光滑性、真实 degree3 及原三微分

在(4)任一点处，$R_A$ 在三个切方向上均为乘 $\omega$。
在特征零的等变形式参数 $(z_0,z_1,z_2)$ 中它准确为标量作用。
一个 blowup chart 可写为
$$
z_0=s,\qquad z_1=su,\qquad z_2=sv.
$$
于是
$$
\widetilde R(s,u,v)=(\omega s,u,v),\qquad
\widehat{\mathcal O}_{Z}\simeq K[[t,u,v]],\quad t=s^3.
\tag{7}
$$
其它两个 chart 相同。
异常 $\mathbf P^2$ 被逐点固定；其法向的分歧指数为3。
离开异常除子，原作用没有固定点，商为 étale degree3。
所以 $Z$ 光滑，且 $q$ 为有限、满射、泛型次数3的态射。
有限商保持射影性。局部(7)给秩3的自由代数；
离开异常集 étale，故 $q$ 全局有限平坦 degree3。

原 $\Omega_A$ 在等变参数中可有一个非零单位。
写
$$
b^*\Omega_A=s^2 h(s^3,u,v)\,ds\wedge du\wedge dv,\qquad h(0,u,v)\ne0.
$$
单位是 $s^3,u,v$ 的函数，由 $R_A^*\Omega_A=\Omega_A$ 保证。
因此下降三微分准确为
$$
\Omega_Z=\frac13h(t,u,v)\,dt\wedge du\wedge dv.
$$
它在异常集也无零、无极，给全局等式
$$
\boxed{q^*\Omega_Z=b^*\Omega_A.}
\tag{8}
$$
这同时证明 $K_Z$ 平凡及固定的 $\mathbf Q$ 归一。
式(8)已经支付3的局部微分倍率，不能在后文再引入一个未定标量。

吹起点不改变 $H^{i,0}$。$R_A$ 在 $H^{1,0}(A)$ 上为 $\omega$，
在 $H^{2,0}(A)$ 上为 $\omega^2$，所以 $Z$ 的这两空间均为零。
在 $H^3(A)$ 中，只有
$$
H^{3,0}(A)\oplus H^{0,3}(A)
\tag{9}
$$
被 $R_A$ 固定；全部 $(2,1)$、$(1,2)$ 特征非平凡。
吹起27点只添加 degree2、4的 Tate 部分，不添加 $H^3$。
有限推拉遂给
$$
H^3(Z)\simeq H^3(\widetilde A)^{\widetilde R}
 \simeq H^3(A)^{R_A},\qquad
h^{3,0}(Z)=h^{0,3}(Z)=1,\quad h^{2,1}(Z)=0.
\tag{10}
$$
所以 $Z$ 是光滑射影刚性 Calabi–Yau 三维簇。
这些 Hodge 计算不用于假定某个高余维实现函子忠实。

## 3. 原最高投影是一个明确的平均

所有 Chow 对应及 Chow 群本节取有理系数；
若原有限 Artin 组合需要固定系数域，再作同一标量扩张。

令 $\pi_3^A$ 为从三份 $E_0$ 的标准
$\pi_0,\pi_1,\pi_2$ 取 tensor product 得到的 degree3 Chow 幂等元。
令 $\Pi$ 为 R839/R841 的原最高 CM 幂等元，即
在 $K$ 系数下保三份 $h^1$ 的全部 $\omega$ 特征
及全部 $\omega^2$ 特征的和。
准确有 Chow 对应等式
$$
\boxed{
\Pi=\pi_3^A\frac{1+R_{A,*}+R_{A,*}^2}{3}.
}
\tag{11}
$$

这里的等式可在 Chow 动机中直接核，不只是 Betti 核定。
每份 $h^1(E_0)$ 上的 $[\omega]$ 满足
$[\omega]^2+[\omega]+1=0$，故在 $K$ 上有两个实际特征幂等元。
$\pi_3^A$ 中的 tensor indices 只有
$(1,1,1)$ 与 $(2,1,0)$ 的排列。
后一类有一个 $h^1$，其 $R$ 特征不为1，平均杀掉；
前一类的八个实际特征张量中，只有三个特征全相同的两项
有乘积1。这正是 $\Pi$ 的原定义。
因此(11)在 Chow 范畴中成立，不需从一般上同调恒等推出 Chow 恒等。

特别
$$
\Pi^2=\Pi,\qquad R_{A,*}\Pi=\Pi R_{A,*}=\Pi,\qquad \Pi^t=\Pi.
\tag{12}
$$
最后一式由 $\left(\pi_3^A\right)^t=\pi_3^A$ 及平均在转置时只交换 $R$ 与 $R^{-1}$ 得到。
$\Pi$ 在 degree4 上同调上为零，故 $\Pi CH^2(A)$
中的每个类都同调平凡；它的 Abel–Jacobi 值仍可能为零。

## 4. 光滑商上的真实投影与双向 Chow 同构

记
$$
\widetilde\Pi=b^*\Pi b_*,
\qquad
\boxed{\Pi_Z=\frac13q_*b^*\Pi b_*q^*.}
\tag{13}
$$
式中 $b^*$ 是光滑簇之间的 Chow 拉回；
$q^*$ 可用其有限平坦拉回。
所有式子也表示对应的 Chow 动机态射。

需要的关系全部是实际推拉恒等：
$$
b_*b^*=1,\qquad q_*q^*=3,\qquad
q^*q_*=\sum_{j=0}^2\widetilde R_*^j.
\tag{14}
$$
最后一式即使在异常分歧处也成立：
$\widetilde A\times_Z\widetilde A$ 有限平坦于 $\widetilde A$，
其最大维循环为三个生成元的图形之和，
泛型各以 multiplicity1出现；分歧处不另添最大维分量。
因此(14)是 Chow 对应恒等，非仅开集计算。

定义
$$
\alpha=q_*b^*\Pi,\qquad
\beta=\frac13\Pi b_*q^*.
\tag{15}
$$
由(12)–(14)直接得到
$$
\begin{aligned}
\beta\alpha
&=\frac13\Pi b_*
 \left(\sum_{j=0}^2\widetilde R_*^j\right)b^*\Pi
=\Pi,\\
\alpha\beta&=\Pi_Z.
\end{aligned}
\tag{16}
$$
故 $\Pi_Z^2=\Pi_Z$，且
$$
\boxed{
(A,\Pi)\ \underset{\beta}{\stackrel{\alpha}{\rightleftarrows}}\
(Z,\Pi_Z)
}
\tag{17}
$$
为双向互逆的真实有理 Chow 动机同构。
在所有相应 Chow 群、Betti、de Rham、étale 实现上均适用。

依(10)，$\Pi_Z$ 的上同调实现准确是 $H^3(Z)$ 上的恒等，
其余 degrees 为零。
但(17)不声称 $\Pi_Z CH^2(Z)$ 为一维，
不声称 Abel–Jacobi 单射，也不声称每个非零代数循环有非零 regulator。
这里没有以这类未证命题替代原指定循环的比较。

## 5. 同一原模曲线在光滑商上的真正像

保持 R841/R847 的实际曲线映射
$$
X=X_0(10404),\qquad
\Phi=(F,aq_0,aq_2):X\longrightarrow A,\quad
q_0(z)=z,\quad q_2(z)=4z,
\tag{18}
$$
包括完整实际 Hom packet、有限 Artin 系数及原基点。
已有准确等变式
$$
\Phi R_X=R_A\Phi,\qquad R_X:z\mapsto z+1/3.
\tag{19}
$$
这里只需 $\Phi$ 非常值；常值项的 curve pushforward 本来为零。

$X$ 是光滑曲线。由于非常值像不包含于有限中心 $\mathcal F$，
$\mathcal I_{\mathcal F}\mathcal O_X$ 是非零可逆理想。
由 blowup 的泛性质，$\Phi$ 唯一提升为
$$
\widetilde\Phi:X\longrightarrow\widetilde A,\qquad b\widetilde\Phi=\Phi.
\tag{20}
$$
唯一性使此提升仍满足(19)。
所以 $q\widetilde\Phi$ 因子化过 R841 §5 已付的真实循环商
$$
\rho:X_0(10404)\longrightarrow
\overline X=X_0(3468),\qquad z\longmapsto3z,\qquad\deg\rho=3.
\tag{21}
$$
记下降后的实际态射为
$$
\phi_Z:\overline X\longrightarrow Z,\qquad
q\widetilde\Phi=\phi_Z\rho.
\tag{22}
$$
这是原映射的下降，不是从 $Z$ 任选一条曲线。
源 cusp 的分歧包含在(21)中，不改变泛型 degree3。

令
$$
z_\Phi=\Pi\Phi_*[X].
$$
则 $b_*\widetilde\Phi_*[X]=\Phi_*[X]$，
而原式(13)–(16)还给
$$
\Pi_Zq_*=q_*\widetilde\Pi.
$$
于是
$$
\begin{aligned}
\alpha z_\Phi
&=q_*\widetilde\Pi\,\widetilde\Phi_*[X]\\
&=\Pi_Zq_*\widetilde\Phi_*[X]\\
&=\Pi_Z\phi_{Z,*}\rho_*[X].
\end{aligned}
$$
最终得到精确等式
$$
\boxed{
\alpha z_\Phi=3\Pi_Z\phi_{Z,*}[\overline X],
\qquad
z_\Phi=3\beta\Pi_Z\phi_{Z,*}[\overline X].
}
\tag{23}
$$
所有等式均在同一个 Chow 群中，含原有限映射 multiplicities。

尤其没有直接宣称 $b^*\Phi_*[X]$ 等于严格变换；
未投影的 pullback 可能含异常贡献。
本证明始终用 $\widetilde\Pi=b^*\Pi b_*$ 支付这个差，
故无需遗漏原曲线与27点的交数。

## 6. 整个原有限组合与 Abel–Jacobi 归一

R839/R841 已把原唯一端点写为固定有限组合
$$
\mathcal Z_{\rm orig}=\sum_i c_i\Pi\Phi_{i,*}[X]
\tag{24}
$$
及其指定有限域的 trace/Artin 投影。
同一 $\alpha,\beta$ 对每项使用(23)，故准确为
$$
\boxed{
\alpha\mathcal Z_{\rm orig}
=3\sum_i c_i\Pi_Z\phi_{Z,i,*}[X_0(3468)].
}
\tag{25}
$$
它保完整系数 $c_i$，包括此前的 Hom averaging、
polarization 与原 finite pushforward 的所有分母。
原 $X_0$ 的 $6^{-2}$、$X_1$ 的 $12^{-2}$、
$D_X=1632,D_C=816$ 仍按 R831 使用；
(25)只额外显示真实 source quotient 的3，不把那些原分母重选。

对同调平凡的 $z=\Pi z$，Abel–Jacobi 的对应函子性、
(8)及 $b_*b^*=1$ 给
$$
\boxed{
\operatorname{AJ}_{Z}(\alpha z)(\Omega_Z)
=\operatorname{AJ}_{A}(z)(\Omega_A).
}
\tag{26}
$$
特别对每个原项，
$$
\boxed{
\operatorname{AJ}_{A}(z_\Phi)(\Omega_A)
=3\operatorname{AJ}_{Z}
 \bigl(\Pi_Z\phi_{Z,*}[\overline X]\bigr)(\Omega_Z).
}
\tag{27}
$$
复 Abel–Jacobi 或原适用的 $p$-adic Abel–Jacobi
均按各自的实际目标和固定 period 理解此函子性；
没有把 period 的商称为跨 $p$ 的代数单位。
有限坏素数与原定义域限制继续保留，尤其 degree3 的分母不被隐去。

最高 $\lambda$、$\lambda^c$ 两个系数分量也可分别在固定系数域
施投影后使用(25)–(27)，因为对应均来自同一个 $\Pi$。

## 7. 与原二处 $S_3$ 商及后续比较的关系

R847 的实际 $S,w_4$ 作用是 $A$ 上保持原点的整数线性同态，
与 $R_A$ 交换，并保持 $\mathcal F$。
因此它们提升到 $\widetilde A$，再下降为 $Z$ 上的同一个 $S_3$。
$Z/S_3$ 与 R848 的 $A/(C_3\times S_3)$ 双有理；
后者的明确函数域和最高微分仍是
$$
w^2=u(v^3+u)\bigl[4u^2+4un(9-n^2)-27(1-n^2)^2\bigr],
\qquad
\frac{dv\wedge du\wedge dn}{6w}.
\tag{28}
$$
原剩余 source quotient 为
$X_0(3468)\to X_0(867)$，degree6，
与 R848 的总 degree18 一致。

本篇没有假定完整 $S_3$ 商光滑，
也没有把(13)的投影无条件套在该奇异商上。
当前已经得到足够明确的固定光滑载体 $Z$ 和精确原循环(25)。
后续可接到同一三阶商的模椭圆曲面纤维积对应，
但仍必须支付该对应的次数、所有定义域/Artin 角色、
原曲线的实际像及 R814 指定 canonical 类的比较。
单凭(10)的二维 $H^3$ 不能完成后面这一步。

无新增数值运行、目标素数扫描或可重算输出。

## 8. 来源与已读范围

- [R839](R839-top-cm-translation-invariance-and-original-ceresa-expression.md)、
  [R841](R841-original-cubic-normalizer-and-endpoint-chow-purity.md)：
  使用原最高 Chow 幂等元、完整 Hom 表达、真实三阶等变及 source quotient。
- [R847](R847-original-dyadic-s3-and-genus-seven-lower-bound.md)、
  [R848](R848-original-degree-eighteen-hecke-quotient-and-top-form.md)：
  使用原无常值的 $S_3$ 作用、实际 degree18 商和最高三微分。
- S. A. Filippini–A. Garbagnati, *A rigid Calabi–Yau 3-fold*,
  arXiv:1102.1854v2，§1（E³ 的对角三阶商与27点吹起）：
  <https://arxiv.org/pdf/1102.1854>。
  此文的 Fermat cubic 是其选定模型；本篇则从原 $E_0$ 自含构造(1)–(8)，
  不凭几何同构忽略有理 twist。
- K. Kimura, *A rational map between two threefolds*,
  arXiv:math/0410259v3，第1页：
  <https://arxiv.org/pdf/math/0410259>。
  本篇只记录已读 v3 对 Schoen 模纤维积对应的明确引用，
  不采用早版“尚无对应”的表述，也不在本篇调用未核的循环比较。
