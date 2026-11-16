# 原 μ3 补空间的椭圆 sigma 求值与指定 Poincaré 周期输入

日期：2026-11-16。状态：**新的准确纸面求值公式及全尾界，尚无本篇新数值计算。** 本文接原 [RF 具体帧与 Poincaré 纤维](2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md)，将其中对称项的求值降到原六个椭圆点及其真实共轭上的形式群计算。原 $Y$-Picard 因子、全局线性校正、非 $p$ 项及指定 theta 的比较全部保留。

新的缩小不是再给一个一般的 universal-extension 算法：在本实际正 CM 型中，R724 使用的相容补空间已被特征分解唯一固定；原椭圆方程给一个没有未知第二类系数的 sigma 递推。原点值、主函数和帧则已经由 R841/R844/R846/R848/R849 给出。本篇明确这些真实来源如何进入 RF.30/31，且给对称项的值和同一 $c_1$ 参数下一阶项。

## 1. 原来源、地方与补空间

记
$$
K=\mathbf Q(\zeta),\qquad s=1+2\zeta,\qquad
C_b:y^2=x^3+b,\qquad
\omega=\frac{dx}{2y},\qquad \xi=-\frac{x}{y}.
\tag{SP.1}
$$
$b$、$L/K$ 的七个共轭、$\rho$、原 Hom 字及全部目标缩放均取 R791 的原数据。原六个 Hom 为 $f=f_4$ 和 $g_j=(1+T^j)f$；实际对称源使用
$$
f_R=[1-\zeta^2]f,\qquad g_{R,j}=[1-\zeta^2]g_j.
\tag{SP.2}
$$
点的准确表达式来自 [R841](../results/R841-certified-original-CM-point-and-descent-DAG.md)、[R844](../results/R844-certified-original-five-Hom-word-points-and-comparison-values.md)；
原切向和坐标一阶式来自 [R846](../results/R846-certified-original-Hom-coordinate-and-comparison-first-jets.md)。
R843 保证这些点及非零整数倍均非挠，因而以下真正使用的除法函数和小盘参数不会因点落入其有限核而等于零。

RF 的 $\nu_j,\kappa_j,v_j,v_j^R,z_j^{(3)}$ 继续使用
[R848 的 c0 输出](../results/R848-certified-original-c0-Hodge-jets-and-comparison-leading-coefficients.md)
和 [R849 的全局理想表达式](../results/R849-certified-original-global-function-and-five-polar-ideal-DAGs.md)。
本篇不再计算这两组源，不将 $\xi$ 与原 $Y$ 参数 $t=a^3$ 混用。

### 1.1 本实际补空间无需再求未知的第二类系数

在 $C_b$ 上，$[\zeta](x,y)=(\zeta x,y)$，所以
$$
[\zeta]^*\omega=\zeta\omega,\qquad
[\zeta]^*(x\omega)=\zeta^2x\omega.
\tag{SP.3}
$$
$[\omega],[x\omega]$ 是原 Weierstrass 曲线的 de Rham 基。因此唯一与 $\mu_3$ 相容的 Hodge 补空间是
$$
W_b=\langle[x\omega]\rangle.
\tag{SP.4}
$$
这里没有增加一个任意的 $c\omega$；那将混合两个不同特征。

R728 的原 $B=\operatorname{Res}_{L^+/\mathbf Q}C$ 在 $L$ 上是七个原分量的乘积。取 (SP.4) 的直和；原 $T$ 的同构和缩放保持其第二类特征子空间。原正 CM 型使 $A$ 的 Hodge 子空间全部为 $\zeta$ 特征，商全部为 $\zeta^2$ 特征。故 R699.27a 所取的 $F$、$\mu_3$ 相容补空间在 $A$ 上同样唯一，就是后一个特征子空间。原 $v:A\to B$ 与 CM 作用交换，故这个直和在 $A$ 上诱导的正是 R724 §2 已使用的相容补空间。

因此可以用这七个分量计算 RF 的对称源，而非对七个分量各选一种无关高度。原 $v^\dagger v$、$q q^\dagger$ 和 theta 幂始终留在 RF.17–18 的真实源同态中。R634/R724 的 $A$、$Y$ 正交分裂保证该操作不额外加入跨块曲率。

如果某个较早的记录尚使用另一个 $A$ splitting，须保留 R634 的原差
$$
\lambda^\mu_{p,h}(x)-\lambda^{\mathrm{old}}_{p,h}(x)
=\Delta_h(\log q[x-c_0]),\qquad
Q^\mu_h-Q^{\mathrm{old}}_h=\Delta_h.
\tag{SP.5}
$$
于是原局部函数为本篇求值减去同一个 $\Delta_h$，原外积保持不变。本文不把这项记为零。$Y$ 的 splitting 和与它相配的 $\ell_h$ 在本篇中完全不变；R724 的原精确运输仍适用。

### 1.2 真正的计算地方

以下 $p$ 是所求高度的地方。选一个有限扩张 $E/\mathbf Q_p$，包含本次全部原系数、点值及目标共轭，并保持原嵌入。令 $\log_E:E^\times\to E$ 延拓原对数分支。

若需要从 $E$ 上的分量值回到原有理纤维，可用规范化扩张角色
$$
\chi_E=\frac1{[E:\mathbf Q_p]}\chi_p\circ N_{E/\mathbf Q_p}
      =\operatorname{tr}_{\chi,E}\circ\log_E.
\tag{SP.6}
$$
它在 $\mathbf Q_p^\times$ 上仍等于 $\chi_p$。先在 $E$ 上取同一分支的 $E$ 值线丛对数，再施加 $\operatorname{tr}_{\chi,E}$。RF 已经给出的 $\mathbf Q$ 三次纤维保证最终 tensor 值就是原 $\mathbf Q_p$ 地方值，不是任选扩域的一个地方代原全局和。

R843 等成功输出中的 $518$ 位球位于辅助
$\ell=1000000753$，**不能充当原 $p=41$ 的输入精度**。
在 $41$ 地方使用本篇公式，必须对完整、已接受的 U.1 单位解表达式在真实 $41$ 进扩域求值，或以后使用已准确接受的 A.1；并另行绑定原代数嵌入。任何现有短候选或辅助 $\ell$ 的模球都不替代这一步。

## 2. 原椭圆方程给出的形式 sigma

本节仅令 $u=\xi^2x$、$v=b\xi^6$ 表示形式单位与单变量。原方程和参数给
$$
u^2(1-u)=v,\qquad u(0)=1,\qquad
x=\xi^{-2}u,\quad y=-\xi^{-3}u.
\tag{SP.7}
$$
因隐函数在 $u=1$ 的导数为 $-1$，有唯一
$u\in1+v\mathbf Z[[v]]$。只使用原方程的这一根，不选另一个局部分支。

设 $\omega=w(\xi)d\xi$。直接微分 (SP.7) 得
$$
w=1-\frac{\xi u'}{2u}
 =\frac1{3u-2}\in1+v\mathbf Z[[v]].
\tag{SP.8}
$$
这里中间的 $1/2$ 已在 $\xi u'=6v\,du/dv$ 中消去；(SP.8) 的整系数结论也适用于剩余特征 $2$、$3$。

定义原导子 $D_\omega=w^{-1}d/d\xi$，并置
$$
H(\xi)
=-xw-\frac d{d\xi}\left(\frac1{\xi w}\right)
=b\xi^4\,\frac{9u+4}{u^2(3u-2)}
=\sum_{n\ge1}H_n b^n\xi^{6n-2},
\quad H_n\in\mathbf Z.
\tag{SP.9}
$$
令
$$
F(\xi)=\int_0^\xi w(v)\left(\int_0^vH(u)\,du\right)dv,
\qquad
\mathcal Z_b(\xi)=\frac1{\xi w(\xi)}+\int_0^\xi H(u)\,du.
\tag{SP.10}
$$
积分中的哑变量与 (SP.7) 的形式单位无关。两次形式积分均取零常数。则
$$
D_\omega(\log\xi+F)=\mathcal Z_b,\qquad
D_\omega\mathcal Z_b=-x.
\tag{SP.11}
$$
定义形式级数
$$
\sigma_b(\xi)=\xi\exp F(\xi).
\tag{SP.12}
$$
其含义首先是特征零形式级数；数值求对数只需
$\log_E\xi+F(\xi)$，无需先对一个大数作指数。它满足
$$
D_\omega^2\log\sigma_b=-x,\qquad
\sigma_b/\xi\longrightarrow1,\qquad
\sigma_b(-P)=-\sigma_b(P),\qquad
\sigma_b([\zeta]P)=\zeta\sigma_b(P).
\tag{SP.13}
$$
最后两式也直接由 $F\in b\xi^6\mathbf Q[[b\xi^6]]$ 得出。

这些条件唯一确定 $\sigma_b$。确实，换到原椭圆 Abel 参数
$\mathfrak z=\int_0^\xi w(v)dv$ 后，两解的对数差为 $a\mathfrak z+c$；首系数给 $c=0$，oddness 给 $a=0$。$\mathfrak z$ 不是后文原 $c_1$ 粗参数 $z=a-1$。这不是将一个全局第二类积分的常数任意置零：下面通过原线丛的刚性化及 cubical 比较识别其准确规范。

## 3. 规范除法函数、曲率及正号匹配

原 theta 是
$$
\Theta_b=\mathcal O_{C_b}(O),\qquad e_0=\xi^{-1}\in(\Theta_b)_O,
\tag{SP.14}
$$
并以 $e_0(O)$ 为给定原点刚性化。它的原有理截面是 $1$，在原点附近等于 $\xi e_0$。

对正整数 $n$，定义唯一规范除法函数 $\psi_n$：
$$
\operatorname{div}\psi_n=[n]^*[O]-n^2[O],
\qquad
\lim_{P\to O}\psi_n(P)\xi(P)^{n^2-1}=n.
\tag{SP.15}
$$
特别地
$$
\psi_1=1,\qquad \boxed{\psi_2=-2y}.
\tag{SP.16}
$$
标准表中出现的 $+2y$ 在本 $\xi=-x/y$ 规范下首常数为 $-2$，不能未经记录就用于原帧。

**引理 SP.1。** 原刚性化 cubical 同构
$[n]^*\Theta_b\to\Theta_b^{\otimes n^2}$ 是正乘 $\psi_n$。

证明。两个 Cartier 除子的差正是 (SP.15)，所以正乘 $\psi_n$ 给所需同构。源帧近原点为
$\xi([n]P)^{-1}\sim(n\xi)^{-1}$；乘 $\psi_n\sim n\xi^{1-n^2}$ 后为
$\xi^{-n^2}$，恰是目标帧。故其刚性化常数为 $1$。$\square$

### 3.1 原二阶方程没有遗漏一个 Eisenstein 常数

有准确的有理函数恒等式
$$
D_\omega^2\log\psi_n
=n^2\bigl(x-x\circ[n]\bigr).
\tag{SP.17}
$$
可在原曲线上直接证明。两边的极部仅在 $n$ 挠点；用平移的 Abel 参数逐点比较，所有二阶极部相消，且没有一阶极部。因此两边之差为常数。原 $\mu_3$ 作用保持 $C_b[n]$，由 (SP.15) 得
$\psi_n([\zeta]P)=\zeta^{1-n^2}\psi_n(P)$。
这使上述差按 $\zeta$ 特征变换；常数只能为零。

由 (SP.11)、(SP.17)，形式比值
$\sigma_b([n]P)/(\psi_n(P)\sigma_b(P)^{n^2})$
的对数二阶导为零。比值为偶函数，原点首常数为 $1$，遂得
$$
\boxed{\sigma_b([n]P)=\psi_n(P)\sigma_b(P)^{n^2}.}
\tag{SP.18}
$$
本证明在特征零成立，不要求 $n$ 为 $p$ 单位。

### 3.2 与原 Poincaré splitting 的实际识别

先取 $E$ 值原对数分支。令 $\mathcal L_b(P)$ 为
$1(P)\in\Theta_b(P)$ 的原规范 line-log，采用 (SP.4) 的补空间及 (SP.14) 的刚性化。它在小盘具有形式
$\log_E\xi+G(\xi)$，其中 $G$ 正则且 $G(0)=0$。
原 Poincaré 双线性、canonical square 及引理 SP.1 给
$$
\mathcal L_b([n]P)
=n^2\mathcal L_b(P)+\log_E\psi_n(P).
\tag{SP.19}
$$
这里 line-log 的标量规则是
$\log_\Theta(cu)=\log_Ec+\log_\Theta(u)$，不是负号。

(SP.18) 说明 $\log_E\xi+F$ 满足相同的 cubical 恒等式。
两者之差在 Abel 参数 $\mathfrak z$ 中由 $n=2$ 迫为 $c\mathfrak z^2$。
原补空间 (SP.4) 与 $\mu_3$ 相容；保持原点帧的 $\mu_3$ 线丛同构只乘一个三次单位根，其对数为零。因此 $\mathcal L_b$ 不变，而 (SP.13) 也使 $\log_E\sigma_b$ 不变。由于 $\zeta^2\ne1$，只能 $c=0$。所以
$$
\boxed{\mathcal L_b(P)=\log_E\xi(P)+F(\xi(P))}
\tag{SP.20}
$$
在充分小的原形式盘内成立。

此唯一性先在 $E$ 值、$E$ 解析函数中证明，再施加 (SP.6)；不能将一个一般 $\mathbf Q_p$ 解析函数的特征分解误当作单一 $E$ 解析变量。
这同时匹配了原曲率和补空间：若加一个 $c\omega$ 的第二类代表，积分将增加一个 $\mathfrak z^2$ 项；本实际 $\mu_3$ 规范已经将它严格排除。没有从实高度或普通约化推断。

文献中的 sigma 确有相同形式方程，例如 Balakrishnan–Besser 的
[Theorem 4.1 与 §4](https://arxiv.org/pdf/1201.6016)。
但其切向自配对函数使用 $-2\log\sigma$；本文没有直接搬用该符号。
(SP.20) 的正号由原 $\mathcal O(O)$ 帧、正乘 $\psi_n$ 及 RF 的 line-log 约定独立确定。该文 Corollary 4.2 的 ordinary/unit-root 假设也未被用于这里的形式和 cubical 证明。

## 4. 一般原点值及一阶周期的恢复

取一个正整数 $n$，使本次有限个点 $[n]P$ 全落在后述收敛小盘中。这样的 $n$ 存在：$C_b(E)$ 为紧致 $p$ 进群，充分深的原形式群邻域为开子群，故商有限；再乘充分大的 $p$ 幂即可任意深入。允许 $p\mid n$，精度损失须按实际 $v_p(n)$ 记录。

对本次原非挠点，$\psi_n(P)\ne0$、$[n]P\ne O$。由 (SP.19) 和 (SP.20)，
$$
\boxed{
\mathcal L_b(P)
=\frac{\log_E\xi([n]P)+F(\xi([n]P))
       -\log_E\psi_n(P)}{n^2}.}
\tag{SP.21}
$$
右边每一个代数点、函数和参数均使用原方程；若实现改模型，必须把原 $\xi^{-1}$ 帧和 $\psi_n$ 的归一标量一并运输。

同时定义 $d\mathcal L_b=\mathcal Z_b\,\omega$。微分 (SP.19) 给
$$
\boxed{
\mathcal Z_b(P)
=\frac{\mathcal Z_b([n]P)}n
-\frac{D_\omega\log\psi_n(P)}{n^2},\qquad
d\mathcal Z_b=-x\omega.}
\tag{SP.22}
$$
式中代数导数为
$$
D_\omega=2y\,\frac{\partial}{\partial x}
          +3x^2\,\frac{\partial}{\partial y}
\quad\text{于 }E(C_b).
\tag{SP.23}
$$
所以已成原点 DAG 可通过准确整数乘法及除法函数的自动微分扩充；不需要先生成一个大维 Jacobian 的 universal-extension 坐标图。

为增深收敛盘，不必重算已经完成的倍点及除法函数。规范恒等式为
$$
\psi_{mn}(P)=\psi_m([n]P)\psi_n(P)^{m^2},
\quad
D_\omega\log\psi_{mn}(P)
=nD_\omega\log\psi_m([n]P)+m^2D_\omega\log\psi_n(P).
\tag{SP.24}
$$
它由 (SP.15) 的除子与原点首常数，或由 (SP.18)，准确确定。新的实际消费者应保留原已成节点并只增加新倍率。

公式与可用 $n$ 无关，因为它们恢复的都是同一个原 line-log 及其微分；任取一个收敛倍点不改变原积分路径、原分支或规范常数。

## 5. 全尾界及有限精度出口

写
$$
w=\sum_{k\ge0}w_k b^k\xi^{6k},\quad w_0=1,\quad w_k\in\mathbf Z,
\qquad
F=\sum_{m\ge1}F_m b^m\xi^{6m}.
$$
由 (SP.9)–(SP.10) 有准确系数公式
$$
F_m=\frac1{6m}\sum_{n=1}^m
       \frac{H_nw_{m-n}}{6n-1}.
\tag{SP.25}
$$
归一赋值满足 $v_p(p)=1$。在给定倍点必须同时认证所选为原点分支，并令
$$
A=v_p(b)+6v_p(\xi)>0,\qquad
v_p(\xi^2x-1)>0.
\tag{SP.26}
$$
第二个条件使实际 $u=\xi^2x$ 是 (SP.7) 的 $u(0)=1$ 分支；不能仅从 $A>0$ 将其余两个局部根排除。整个形式输入 $u,w,H$ 于是收敛，并有
$$
\begin{aligned}
v_p(F_m b^m\xi^{6m})
&\ge mA-v_p(6m)-\max_{1\le n\le m}v_p(6n-1),\\
v_p\!\left(\frac{H_n b^n\xi^{6n-1}}{6n-1}\right)
&\ge nA-v_p(\xi)-v_p(6n-1).
\end{aligned}
\tag{SP.27}
$$
第一式控制 $F$ 的全尾，第二式控制 $\mathcal Z_b$ 中积分部分的全尾。
其有理项 $(\xi w)^{-1}=(3u-2)/\xi$ 可直接用原点坐标求值，不必另截断。

例如可将第一式下界进一步放弱为
$$
mA-v_p(6)-\lfloor\log_p m\rfloor
           -\lfloor\log_p(6m-1)\rfloor.
\tag{SP.28}
$$
这随 $m$ 线性趋于无穷。给定目标精度，可以找一个有限起点，使相应连续放弱函数以后单调，再逐项检查此前的有限区间，得到对所有 $m>N$ 的严格下界。不能只检查“最后一个可见系数”。

这里不要求 $b$ 为整元，也不要求模型有好约化；只需通过原倍点使 (SP.26) 的两个条件真实成立。原分支的 $\log_E\xi$ 和 $\log_E\psi_n$ 另按其实际单位、均匀化元和角色值计算。以 (SP.21) 除以 $n^2$ 时，尾精度须再扣除 $2v_p(n)$；(SP.22) 的两项也分别按 $v_p(n)$、$2v_p(n)$ 运输。有限扩域的 $\operatorname{tr}_{\chi,E}$ 依其实际线性算子赋值界运输，不能假设其不损失精度。

这些是完整计算所需的确定尾规则；没有在本文生成任何具体 $p$ 的新截断值、倍率或误差数字。

## 6. 直接代入 RF 的原六点、五个对称周期

令 $\tau$ 遍历原七个目标分量。在一个共同 $E$ 中定义
$$
\begin{aligned}
\mathcal A_h
&=\sum_\tau
 \operatorname{tr}_{\chi,E}
 \bigl(\mathcal L_{\tau(b)}(h_{R,\tau}(c_1))\bigr),\\
\mathcal B_h
&=\sum_\tau
 \operatorname{tr}_{\chi,E}
 \bigl(\mathcal Z_{\tau(b)}(h_{R,\tau}(c_1))
               h^{\rm tan}_{R,\tau}(c_1)\bigr),
\end{aligned}
\tag{SP.29}
$$
其中 $h=f,g_1,\ldots,g_5$；
$h^{\rm tan}_{R,\tau}$ 明确由
$h_{R,\tau}^*\omega_{\tau(b)}=h^{\rm tan}_{R,\tau}(z)\,dz$
定义，$z=a-1$ 是原 $c_1$ 粗参数。这个上标防止把 Hom 映射和微分系数混为一项。原同源给切向乘 $1-\zeta^2$，所有 $\rho$ 及共轭均按原 DAG 作用于整个表达式。

RF 的真实 $S_j^{\otimes3}$ 及其 canonical square 给
$$
\boxed{\frac12\tau_{J,p}(z_j^{(3)})
=3\bigl(q_j\mathcal A_{g_j}-p_j\mathcal A_f\bigr).}
\tag{SP.30}
$$
原因是每个 $u_j$ 是原 $\Theta_b$ 的截面 $1$ 的 tensor，平方同构给每个分量的两倍 line-log，而第二 Picard 槽的第三次 tensor 再给因子 $3$。并非把原 $\beta$ 乘三，也未丢去 theta 的二挠比较；后者仍由 RF 的完整 Corr 同构和平方处理。

因此 RF.30/31 的确切地方表达式为
$$
\boxed{
\lambda_{p,h_j}(c_1)
=\mathcal A_{g_j}-\frac{p_j}{q_j}\mathcal A_f
+\frac1{3q_j}
 \left[\chi_p(\nu_j)+\tau_{Y,p}(v_j^R)\right],}
\tag{SP.31}
$$
或
$$
\boxed{
\lambda_{p,h_j}(c_1)
=\mathcal A_{g_j}-\frac{p_j}{q_j}\mathcal A_f
+\frac1{3q_j}\chi_p\!\left(
 \frac{\nu_j\kappa_j}{\mathcal R_j(P_1)}\right)
+\frac1{q_j}\tau_{Y,p}(v_j).}
\tag{SP.32}
$$
若使用 (SP.5) 中未运输的旧 splitting，则两式右侧须减去所记的同一个 $\Delta_h(\log\beta)$。

同一原参数下，一阶项为
$$
\boxed{
\lambda'_{p,h_j}(c_1)
=\mathcal B_{g_j}-\frac{p_j}{q_j}\mathcal B_f
+\frac1{q_j}\left.\frac d{dz}\tau_{Y,p}(v_j(P_Y(z)))\right|_{z=0}
-\frac1{3q_j}\operatorname{tr}_{\chi,E}
 \left(\frac{\mathcal R_j'}{\mathcal R_j}(c_1)\right).}
\tag{SP.33}
$$
最后一项的负号就是 RF.12 的 $\kappa/\mathcal R$，$\nu,\kappa$ 均为常数。原比较对数导数来自 R846/R847，未重算；$Y$ 项的变量只在第一个 Poincaré 槽，第二个实际 Picard 点固定。任何较早 splitting 的差也须对 (SP.5) 求导后同样运输。

原真实函数仍是
$$
\Lambda_{h_j}
=\lambda_{p,h_j}-2\ell_{h_j}(\log P_Y).
\tag{SP.34}
$$
(SP.31)–(SP.33) 没有删除其 $2\ell_{h_j}$，也没有用 $\mathcal R_j'\ne0$ 推断整式非零。所有非 $p$ 项按 RF/R724 同一有理纤维及模型保留；不能用乘积公式在一个地方删去 $\chi_p(\nu_j\kappa_j/\mathcal R_j(P_1))$。

## 7. 新的实际消费规模与未执行部分

| 输入或输出 | 真实来源与处理 |
|---|---|
| 六个原椭圆点及其共轭 | R841/R844 的准确表达式；目标 $p$ 另绑定真实嵌入，不使用辅助 $\ell$ 球替代 |
| 六个原切向 | R846 原 Hom 线性组合，实同源只加准确已知标量 |
| theta 原点帧 | RF 的 $\xi^{-1}$ 与 $\mathbf Q$ 三次下降，保留 $\nu_j$、二挠比较及 $v^\dagger v$ |
| 对称周期值与一阶 | (SP.21)–(SP.22) 对六组点的七个分量；共用同一原方程的普适整系数递推 |
| 原 $Y$ 具体纤维 | RF 已成 $v_j,v_j^R$，完整 GP 理想和 $c_0$ 帧，不换成点值或空 Picard 类 |
| 原高度与首项 | (SP.31)–(SP.34)，仍需同一 $Y$ 周期及全局 $\ell_h$；原非 $p$ 数据不变 |

与一般 R724 接口相比，本次确定了本实际对称部分的所有第二类系数及帧常数，并给出原坐标上的有限倍率公式、一次周期及可验证的全尾界。后继无需为该部分构造 $J_X$ 的高维 universal extension，也不需求一套未知 Eisenstein/单位根补空间。

本文没有实施上述目标地方的点值、sigma 或周期算术。原 $Y$-Picard 周期与其全局线性校正仍按已登记的原接口求值；故没有宣称原指定 $\mathscr T_p$ 非零、原高度已出或全 $p$ 主目标完成。

## 来源定位

- R699 §5.1、R634 §§3–4、R724 §2：原 $F,\mu_3$ 相容补空间及保持原外积的准确运输。
- R728 原 Weil restriction 和原极化；R791 原 Hom、真实目标相位及实三同源。
- RF.14–31：完整 Picard correction、真实 $\mathbf Q$ 三次帧、原 $C_h$、canonical square 和主函数标量。
- R841/R843/R844/R846/R848/R849：已经完成的准确点、非挠、原切向、c0 及全局理想来源。
- Balakrishnan–Besser, *Coleman–Gross height pairings and the p-adic sigma function*, [arXiv:1201.6016](https://arxiv.org/abs/1201.6016), §4：形式方程的文献定位。本篇采用自己的原帧与 cubical 符号证明，不以 ordinary 的专门比较替代本实际规范。

