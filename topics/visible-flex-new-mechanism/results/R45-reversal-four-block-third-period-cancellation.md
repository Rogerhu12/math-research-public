# R45：真实倒行四块与三阶周期相消

日期：2026-11-14。literature 推导，repo_sources 独立全文核对，root 全文复核。**独立完整构造与相容性结论；没有新研究数值。**

本稿给 R37–R39 的正向后续：可以选择另一种真实零算子闭带，使 R39 的两条三阶**周期函数**准确为零。它还明确给出没有被这项对称支付的每条 ruling 条件，并证明同 collar 齐次 gauge 不能掩盖该剩余条件。

**没有得到：** 三阶完整可解、精确有限等距族、嵌入、宏观位移或 reach。以下四块构造是一个新的几何设计；不能把此前 Klein 八块数值候选直接改称本构造。

## 1. 保持 u、xi 不翻号的合法倒行

仍用

$$F=(T,N,B),\quad F_s=F\Omega(k),\quad
\Omega(k)=\begin{pmatrix}0&-k&0\\k&0&1\\0&-1&0\end{pmatrix},$$

$$\alpha_s=h^2T,\quad X(s,u)=\alpha(s)+uN(s),\quad
\omega_s=k_s/(2h),\quad \xi=h/u-\omega.$$

取

$$D=\operatorname{diag}(-1,1,-1),\qquad D\Omega(k)D=-\Omega(k).\tag{1}$$

设路径 P 的长度为 $\ell$，初始框架 I、末框架 D，标量两端均为同一常值芽
$(k,h,\omega)=(0,1,0)$。记初始位置 0，末位置 $V$。

令反向标量控制为

$$k^R(s)=k(\ell-s),\quad h^R(s)=h(\ell-s),\quad
\omega^R(s)=\omega(\ell-s).\tag{2}$$

因为 k、omega 的导数同时变号，(2) 仍满足真实的
$\omega_s^R=k_s^R/(2h^R)$。以 I 为初始框架解倒行控制，准确得到

$$F^R(s)=F(\ell-s)D,\qquad
\alpha^R(s)=\alpha(\ell-s)-V.\tag{3}$$

验证：$(F^R)_s=-F(\ell-s)\Omega D=F^R\Omega$，
$F^R(0)=D^2=I$，且 $\alpha_s^R=-h^2T(\ell-s)=h_R^2T^R$。特别地

$$T^R=-T\circ R,\quad N^R=N\circ R,\quad B^R=-B\circ R,$$

$$F^R(\ell)=D,\qquad \Delta\alpha^R=-V,\qquad
X^R(s,u)=X(\ell-s,u)-V.\tag{4}$$

这里 u 和 xi 都保持原号，正物理半线仍是同一半线。它与另一个需要 $u\mapsto-u$ 的合法倒行不同，不能混用两套曲率、omega 变换。

## 2. 一条 I 到 D 的准确零算子路径确实存在

R37 的十二种完整常曲率圈、四个 $(h,d)$ 状态和八参数导数保持不变。把最终固定桥改成从 I 到 D，标量首末仍为 $(0,1,0)$；记整条未闭位置路径为 $P_N(p)$。所有连接仍可由 R37 的扩展框架控制引理真实实现，并保持常值端芽。

其矩阵为

$$M_P(p,N)=NF_{\rm bulk}(p)+G_D(p),\tag{5}$$

其中 $G_D$ 及其参数导数均与 N 无关。$F_{\rm bulk}(0)=0$，其八维导数就是 R37 已证明可逆的矩阵。实际 trace 恒为零。

因此对

$$F_{\rm bulk}(p)+\varepsilon G_D(p)=0$$

在 $(p,\varepsilon)=(0,0)$ 应用八维隐函数定理，再取充分大的有限整数 $N$、$\varepsilon=1/N$，得到

$$\boxed{M_P=0.}\tag{6}$$

这里不预先要求 $\alpha_P$ 闭合，故没有额外位置条件占用这八参数。

**为何单条 P 可用全系数恒等式。** 矩阵 $M_P=L|_{\mathcal P_2}$ 与六个周期系数之间的 R7、R20、R37 身份，只依赖 k、h、omega 的标量积分、分部积分和相同端 jet，不依赖 P 的末空间框架已经等于初始框架。P 的标量首末为同一常值芽，所以这些边界项准确为零。故 (6) 仍迫使 P 上的全部六系数

$$A_0,A_1,A_2,B_0,B_1,B_2$$

为零。特别是对任意 profile $\phi$，

$$\int_P \mathcal R_{(dY_\phi)^2}(s,\xi)\,ds=0\quad\text{对全部 }\xi,\tag{7}$$

其中 $\mathcal R_H$ 是同一右 collar 锚定的完整 range 密度。此处“全部系数为零”是准确有限维存在论证，不是从有限采样的小矩阵推断。

## 3. 四块给真正闭合的框架和中心线

顺序执行标量控制

$$\boxed{P,\ P,\ P^R,\ P^R.}\tag{8}$$

每段始末框架增量都是 D，实际全局框架依次为

$$I\longrightarrow D\longrightarrow I\longrightarrow D\longrightarrow I.$$

因此四段的空间位移依次为

$$V,\quad DV,\quad -V,\quad -DV,$$

总和准确为零。每个段落的标量端芽相同，框架连续解同一 ODE，故在所有接缝处全部 jet 相接；不是只检查位置。

倒行不改变标量积分密度的值：$k,h,\omega$ 沿原路反向，$k_s,h_s$ 同时取负，而低导数密度中的导数项是二次的。因此全四块矩阵是 $4M_P=0$。

取一个紧区间使 $\xi+\omega>0$，即可得到真实的周期正则浸入带；$h>0$，且 $|X_s|^2=(h^2-ku)^2+u^2>0$。没有由此得到嵌入性。

四块中心线的具体形状可依次写为

$$\alpha(s),\quad V+D\alpha(s),\quad
DV+\alpha(\ell-s),\quad D\alpha(\ell-s).\tag{9}$$

这说明相反方向的两块分别是平移或旋转后的副本，不必等于同一位置上的简单回溯；但 (9) 也没有排除自交。

设全周期长度 $4\ell$，令 $\tau(s,u)=(4\ell-s,u)$。由 (9) 和框架式可得全局准确对称

$$X\circ\tau=DX,\qquad
F(4\ell-s)=DF(s)D.\tag{10}$$

## 4. 二阶恢复的完整锚与倒行关系

对任意 profile，使用 R39 的真实无穷小场

$$Y_\phi=U\phi+V_0\phi',\qquad
U=uB,\quad V_0=-\frac{uT+wB}{2h},\quad w=h^2-ku.$$

(3) 中 T、B 都取负，u、h、w、xi 均不变，因此逐点有

$$\boxed{Y_\phi^R(s,u)=-Y_\phi(\ell-s,u).}\tag{11}$$

取 R39 的显式三矩配平 f、g（也允许任意满足其三矩和交叉条件的 profile），令
$H_d=(dY_f)^2-(dY_g)^2$。沿每条 ruling 从同一个下 u collar，也即上 xi collar，积分

$$2\rho_u=(H_d)_{uu},\qquad \rho=0\quad\text{在该 collar}.$$

三矩平衡使另一 collar 也为零。记

$$c=\partial_su|_\xi,\quad
\mathcal R_H=
\frac{H(D_s,D_s)/2+(wk-u)\rho-cD_s\rho}{u^2},\quad
D_s=\partial_s|_\xi.$$

由 (7)，P 上 $\int_P\mathcal R_{H_d}\,ds=0$。因此可在每一 P 段取

$$W_s=\mathcal R_{H_d},\qquad W(0,\xi)=0,$$

并准确得到 $W(\ell,\xi)=0$，包括全部 xi 导数。令 $\zeta=u^2W$，恢复

$$\mathcal A=(H_d)_{su}-\rho_s|_u,\qquad
\eta=(\mathcal A-\zeta_u)/2,$$

$$p=(\zeta+u\eta)/h^2,\qquad q=\eta-kp,\qquad
Z_d=pT+\rho N+qB.\tag{12}$$

倒行下 $H_d^R=R^*H_d$，所以

$$\rho^R=\rho\circ R,\quad c^R=-c\circ R,
\quad\mathcal R_{H_d^R}=\mathcal R_{H_d}\circ R.$$

两个端点的 W 都为零，故同一锚真正给出

$$W^R(s,\xi)=-W(\ell-s,\xi).\tag{13}$$

接着 $\mathcal A^R=-\mathcal A\circ R$、
$\zeta^R=-\zeta\circ R$、$\eta^R=-\eta\circ R$，
$p^R=-p\circ R$、$q^R=-q\circ R$，而 rho 不变。结合框架 T、B 的负号，得到

$$\boxed{Z_d^R(s,u)=Z_d(\ell-s,u).}\tag{14}$$

这没有忽略 Z 的切向部分，也没有在反向段重新选择不同 gauge。

**接缝。** 在共同常值端芽上 $c=0$、$\rho_s=0$、$(H_d)_{su}=0$；在每段端点 $W=W_\xi=0$。所以 (12) 给 $p=q=0$，即端点 $Z_d=\rho N$。N 被 D 保持，因此四块端值匹配。更高 jet 由同一个光滑 W 方程与相同标量端芽自动相接；(13) 近端的导数也一致。于是构成真实的全局光滑周期解

$$\mathcal L_X Z_d=H_d,$$

并有 $Z_d\circ\tau=DZ_d$。

## 5. 两条三阶周期函数准确为零

仍定义 R39 的两条 forcing

$$H_\phi^{[3]}=-\mathcal S(Y_\phi,Z_d),\qquad \phi=f,g.$$

由 (11)、(14)，

$$\boxed{(H_\phi^{[3]})^R=-R^*H_\phi^{[3]}.}\tag{15}$$

沿每条 ruling 用同一 collar 锚定三阶 rho，即使尚未证明另一端为零，(15) 仍给

$$\rho_3^R=-\rho_3\circ R.$$

由于 c 取负、$D_s\rho_3^R=(D_s\rho_3)\circ R$，完整 range 密度逐点满足

$$\mathcal R_{(H_\phi^{[3]})^R}
=-\mathcal R_{H_\phi^{[3]}}\circ R.\tag{16}$$

第二个 P 与第一个只差空间刚体 D，点积和 range 密度不变；两个倒行块给相反的积分。所以对全部 xi，

$$\boxed{\mathscr P(H_f^{[3]})(\xi)
=\mathscr P(H_g^{[3]})(\xi)=0.}\tag{17}$$

它是整个函数的准确相消，不是只检查有限个 xi 或少数矩。

## 6. 完整三阶的剩余条件，以及 gauge 不能消除它

令 P 上的两条 ruling 函数为

$$K_\phi(s)=\int (H_\phi^{[3]})_{uu}(s,u)\,du
=-2\int (Y_\phi)_u\cdot(Z_d)_u\,du,
\qquad \phi=f,g.\tag{18}$$

四块中的它们依次是 $K_\phi,K_\phi,-K_\phi\circ R,-K_\phi\circ R$。因此 (18) **不能**靠全周期积分相消来通过每 s 的 ruling 条件。

对当前规范的 $Z_d$，由完整 range 定理和 (17)，三阶路径可解当且仅当

$$\boxed{K_f(s)=K_g(s)=0\quad\text{在整个 P 上}.}\tag{19}$$

这个条件也不能用另一二阶齐次 gauge 偷换。任意周期、同 collar 的二阶解都与当前解相差 $Y_\psi$。对其中一条通道，ruling 变化量为

$$-2\mathcal E_s(\phi,\psi),$$

$$\mathcal E_s(\phi,\psi)
=\frac{d^2+1}{4h}I_0(\phi,\psi)
+\frac d2I_1(\phi,\psi)+\frac h4I_2^*(\phi,\psi),
\qquad d=h\omega-k.\tag{20}$$

这在 P 与 $P^R$ 对应点上**同号且相等**，因为它只用同一 h、d 和固定 profile 交叉矩。若修改后两处都满足 ruling 条件，就须同时有

$$K_\phi-2\mathcal E_s(\phi,\psi)=0,\qquad
-K_\phi-2\mathcal E_s(\phi,\psi)=0.$$

相减迫 $K_\phi=0$。所以任何非零的 (18) 都不能由一个合法全局 profile gauge 消掉。

同样允许每个相位独立选 $Y_{\psi_\theta}$ 也无帮助：canonical 三阶 ruling 的倒行奇部是
$\sin^2\theta(\cos\theta K_f+\sin\theta K_g)$，gauge 只能加倒行偶部。若要求全圆相位均可解，仍迫 (19)。反之 (19) 与 (17) 已给完整 range，故无需 gauge 就有 $W_f,W_g$，再用 R39 的准确三角组合恢复完整三阶路径。

因此本稿并未把三阶问题宣布完成，而是把它准确缩为两条真实的逐 ruling 函数；高维周期函数在该几何上已由对称严格支付。

## 7. 更一般的奇数阶周期相消，及其明确界限

对全局反射 $\tau$，任意 collar forcing H 若满足

$$\tau^*H=-H,$$

则同一 collar 锚定的 rho 为奇函数，c 也为奇函数，其完整 range 密度为奇函数，故

$$\mathscr P(H)\equiv0.\tag{21}$$

此结论不预先假设 H 的另一 collar ruling 条件已成立。

假设形式递推已经解到某阶，并可取

$$Z_j\circ\tau=(-1)^j DZ_j.$$

目标度量 $g_\varepsilon=g_X+\varepsilon^2H_f$ 对 $\tau$ 不变；第 n 阶的双线性 forcing 满足
$\tau^*H_n=(-1)^nH_n$。所以所有奇数 $n\ge3$ 的周期函数都由 (21) 自动为零。若某阶完整 range 已成立，可将该阶的任意解与
$(-1)^nD Z_n\circ\tau$ 平均，获得上述所需奇偶性，故此选择与后续递推相容。

这只是一个逐阶的准确对称约简：奇数阶 ruling、偶数阶完整 range、无限阶收敛与固定非零 epsilon 下的精确解仍未支付。它不是全非线性 holonomy 恒等为 I 的证明，也不从 M=0 推出高阶所有障碍都消失。

## 8. 下一具体对象

现有 R39 分离 bump 的每个副本可独立改符号，而 $H_f,H_g$ 及规范 $Z_d$ 不变。因此 (18) 对这些符号是线性的。这给一个清楚的后续构造入口：证明这些 ruling 函数属于可控的有限函数空间，或找到准确的 profile/控制对称使两条函数恒零；不能只在有限 s 节点拟合。

若要计算，本稿应使用单 P 目标 $M_P=0$ 的独立有限 N 设计，不能沿用八块目标 $M_{\rm total}=0$ 但单 P 矩阵未零的旧数值输出。完整反向控制和所有接缝保持同一物理参数，随后才接三阶 ruling 诊断。巨大 N 的整圈本身距题目宏观 reach 要求很远，本稿的作用是研究有限等距机制的相容结构，而不是把这些圈当成已合格的实物闭面。

## 后续完整三阶

[R46](R46-eight-packet-complete-third-order-circle.md) 已用八个完整配平packet准确支付本篇留下的两条逐ruling函数，得到该真实几何上的完整三阶路径。其准确误差从四阶开始，四阶偶周期门、收敛与宏观几何仍未付。
