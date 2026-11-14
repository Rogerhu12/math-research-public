# R54：全常状态的螺旋面迁移、准确相位矩与第一段常数gauge

日期：2026-11-14。literature推导，repo_sources独立全文核，root全文复核。独立精确推导。研究计算未在本地运行。

本稿继续真正重叠 profile 的四阶入口。它把所有常 k/h/omega 段准确转成同一个标准螺旋面问题，给共享相位参数的有限方程，并说明第一常段可额外支付的较低项。**它没有把各段可分别求解误作同一全局 profile 已经共同通过，也没有支付第四周期函数。**

来源：[R47 完整第四range和gauge](R47-fourth-order-range-and-third-gauge.md)、[R49 常段最高次](R49-fourth-ruling-leading-coefficient-and-narrow-packets.md)、[R50 局部平方式](R50-disjoint-profile-circle-fourth-order-positive-obstruction.md)及 [R53 真正重叠最高次门](R53-overlapping-profile-fourth-leading-gate-existence.md)。本稿没有为不同常状态另选彼此无关的profile，也没有改变指定目标度量。

## 1. 任一常状态就是平移、缩放后的标准螺旋面

固定常数 k、h>0、omega，记

$$a=\sqrt{1+k^2},\qquad H=h^2/a^2,$$

$$T_0=(T-kB)/a,\qquad B_0=(kT+B)/a,\qquad N_0=N.$$

由 $T_s=kN,N_s=-kT-B,B_s=N$，T0 固定且

$$N_{\tau}=-B_0,\qquad(B_0)_{\tau}=N,
\quad\tau=as.$$

又因 $\alpha_s=h^2T$，积分给（允许一次固定平移）

$$\alpha=H\tau T_0-HkN.$$

因此

$$\boxed{\widehat X=X/H=\tau T_0+vN,\qquad
v=u/H-k.}\tag{1}$$

这正是标准 $(k,h,\omega)=(0,1,0)$ 螺旋面，不只是内在度量相似。

## 2. 同一个原始 profile 的准确 Möbius 迁移

令原坐标 $\xi=h/u-\omega$、$e=h(\xi+\omega)-k$。标准 profile 坐标为 $x=1/v$，所以

$$\boxed{x=\frac{e+k}{1-ke},\qquad
\xi=\frac{a^2x}{h(1+kx)}-\omega.}\tag{2}$$

在 profile 支撑邻域要求 $1-ke\ne0$，使该图坐标有限；原物理带还已要求 $\xi+\omega\ne0$。面对有限多个常状态，可先选一个共同物理区间避开全部有限个极点，再把 packet 放入其中。

原 infinitesimal field 为

$$Y_\phi=P T+Q_BB,\quad
P=-\frac{u}{2h}\phi_\xi,\quad
Q_B=u\phi-\frac{h^2-ku}{2h}\phi_\xi.$$

缩放后对 T0、B0 的分量为

$$\widehat P=(P-kQ_B)/(aH),\qquad
\widehat Q=(kP+Q_B)/(aH).$$

准确定义

$$\boxed{\psi(x)=\frac{(1+kx)^2}{a}
\phi\left(\frac{a^2x}{h(1+kx)}-\omega\right).}\tag{3}$$

则

$$\widehat P=-\psi_x/(2x),\qquad
\widehat Q=\psi/x-\psi_x/2.$$

例如 $\psi_x=2k(1+kx)\phi/a+a\phi_\xi/h$，代入即逐项核对。没有在不同常状态独立换一个新 profile：所有 psi 都是同一个 phi 经 (3) 得到。

对真正重叠复 profile $q=f+ig$，(3) 同样复线性；实幅权 $(1+kx)^2/a$ 保留个体 bump 的实形状和原来的复相位系数。

## 3. 第四最高次门的准确尺度与共同约束

若 $\widehat H_4$ 是缩放并换坐标后的第四 forcing，则

$$\int (H_4)_{uu}\,du=H\int(\widehat H_4)_{vv}\,dv.$$

由于 $\tau-\tau_0=a(s-s_0)$，原 ruling 的 sigma² 系数等于标准系数乘

$$Ha^2=h^2>0.$$

所以某个常状态的全相位最高次门等价于把其迁移 profile psi 代入标准的

$$\mathcal F(\psi)=0,\qquad K_2(\psi)=0.\tag{4}$$

原三矩圆保证该状态 $E_{\rm orig}(q,q)=0$，而
$E_{\rm orig}=H E_{\rm standard}$。这恰保证标准复尾 J 的总值为零，足够用于下节局部化；不需要错误地宣称迁移后另外两个标准矩也各自为零。

若实际设计包含 m 个常状态，必须用同一原始 q 同时满足 m 组 (4)，且保持同一个全局目标 $g_X+\varepsilon^2(dY_f)^2$。分别对每段应用单状态隐函数定理，并不能自行给出共同解。

## 4. 相位分段 profile 的准确有限方程

设原始复 profile 为

$$q=\sum_j\alpha_j\phi_j,$$

其中各 phi_j 实、紧支撑且彼此支撑不交。允许复方向至少三个，因此 f、g 本身可真正重叠。原三复总矩必须同时为零。

先在标准状态定义，对任意实 phi，

$$Q=1+x^2,\quad L_\phi=xQ\phi''^2-2Q\phi'\phi'',$$

$$R_\phi''=\frac14(x\phi''-\phi')
\{x\phi''-\phi'+Q\phi'''\},$$

$$e_\phi=\frac14\int Q(R_\phi'')^2
+\frac1{128}\int\{L_\phi^2+2Q^2\phi'^2\phi''^2+4Q\phi'^4\},$$

$$t_\phi=T(\phi),\qquad s_\phi=e_\phi+2t_\phi.
\tag{5}$$

R50 的准确局部平方恒等给

$$s_\phi=\frac1{128}\int\mathcal Q(x,\phi,\phi',\phi'')>0$$

对非零 phi 成立；$e_\phi>0$ 也由 (5) 可见。t_phi 不在此处假定符号。

令 $V=R_0(q,q)$。它的 V' 含非局部复尾，但在总尾为零时，准确有

$$\int|V'|^2=\frac1{64}\int\{|L|^2
+2Q^2\operatorname{Re}(q''^2\bar q'^2)+4Q|q'|^4\},$$

以及不带共轭的对应恒等式。这正是复尾的积分分部，不是逐个未配平 bump 独立重置 J。

因此全部非局部交叉项消去后，

$$E(V,V)=\sum_j\alpha_j^4e_{\phi_j},\qquad
E(V,\bar V)=\sum_j|\alpha_j|^4e_{\phi_j}.$$

局部式 $\mathcal C(r)=\int B_qr''/32$ 及其极化另给

$$\mathcal C(V)=\sum_j\alpha_j^4t_{\phi_j},\qquad
\mathcal C(\bar V)=\sum_j|\alpha_j|^4t_{\phi_j},$$

$$\mathcal B(V)=2\sum_j\alpha_j^2|\alpha_j|^2t_{\phi_j}.$$

写 $w_j=|\alpha_j|^4$、$z_j=\alpha_j^2/|\alpha_j|^2$，得到两个准确有限式

$$\boxed{\mathcal F(q)=\sum_jw_jz_j^2s_{\phi_j},}\tag{6}$$

$$\boxed{4K_2(q)=\sum_jw_j
\{(z_j^2+1)s_{\phi_j}-(z_j+1)^2t_{\phi_j}\}.}\tag{7}$$

对于每个其他常状态，只需将所有 phi_j 用 (3) 迁移后重新计算两个实数 $s_{mj},t_{mj}$。原来的 alpha_j、z_j 必须保持相同。这样全常状态最高次的必要条件是一套有限相位/幅度方程，并保留独立的原三复矩方程。

(6)–(7) 仍不含连接段、第四周期函数或低次 sigma 系数，不能把这个有限系统的解称为全第四 range 解。

## 5. 第一常段的一次项确实自动消失

现只看四块几何中 P 起点的标准常段，采用已经固定的两个二阶 W 在 s=0 取零的共同规范。可把这个常状态形式地延伸到 sigma=0 的两侧，以考察局部代数对称，不改变实际 P。

在起点标架定义刚体旋转 $D_0=\operatorname{diag}(-1,1,-1)$。标准螺旋面有

$$X(-\sigma,u)=D_0X(\sigma,u),\qquad
Y_\phi(-\sigma,u)=-D_0Y_\phi(\sigma,u).$$

两个二阶 forcing 的 rho 与 sigma 无关，且 W= sigma R，所以

$$Z_d(-\sigma,u)=D_0Z_d(\sigma,u),\qquad
Z_c(-\sigma,u)=D_0Z_c(\sigma,u).$$

对每个相位，第三 forcing 于是反射奇：其 ss、uu 分量是奇函数，su 分量是偶函数。共同右端锚给 rho3 奇，标准 characteristic RHS 奇，故 W3 是偶函数加任意段首 profile 常数。恢复的第三场满足

$$W_\theta(-\sigma,u)=-D_0W_\theta(\sigma,u).$$

所有第三同 collar 齐次场 $Y_\psi$ 也具有同样奇性。第四 forcing 因而反射偶，其 ruling 在该常段是一个没有一次项的二次多项式。

在该段应用已准确支付 sigma² 门的新重叠设计后，第四 ruling 只剩一个与空间 sigma 无关的实函数 $k(\theta)$。

这一断言使用指定二阶零锚；任意额外二阶齐次改动不必保持本节的反射偶性。它也不自动覆盖 P 中间其他常段的真实段首 W。

## 6. 一个全局第三 gauge 能清除第一段的常数项

三矩圆使该标准状态

$$E(\phi_\theta,\phi_\theta)=E(f,f)=E_0>0$$

与 theta 无关。取真正的全局 profile

$$\psi_\theta=\frac{k(\theta)}{2E_0}\phi_\theta$$

并把第三场改为 $W_\theta+Y_{\psi_\theta}$。它不改变第三阶方程、周期或双 collar。对第四 forcing 的改变量是
$-\mathcal S(Y_{\phi_\theta},Y_{\psi_\theta})$，其在第一常段的 ruling 恰为 $-k(\theta)$，故该段完整 ruling 准确归零。

全零二阶周期算子的极化同时保证这个 gauge 对所有第四 characteristic 周期函数的改变量为零。它没有支付这些原有周期函数。

在 theta=0、pi 两准确种子处，原二、三阶通道均为零，故 k=0；这个 gauge 也为零，保留两准确种子。

**共同性限制。** 同一个 psi_theta 会在全 P 上改变第四 ruling；不能在每个常段另选一个独立 gauge。重复块的第三段首积分常数也可能不同。本节只证明第一完整常段的 ruling 可支付，后续联合求解须同时跟踪其他常段和连接段，不能各段清零后拼成全局结论。
