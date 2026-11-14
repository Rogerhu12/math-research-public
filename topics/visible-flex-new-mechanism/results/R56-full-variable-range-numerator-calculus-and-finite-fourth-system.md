# R56：完整二次forcing的分子演算、真实变系数range与有限第四系统

日期：2026-11-14。literature推导，repo_sources独立全文核，root全文复核。独立精确证明。没有执行新的数值研究计算。

本稿覆盖真实 s 变系数与光滑连接段，不限常曲率段。它把已给定低阶场产生的完整下一阶 forcing、两 collar 条件及整个周期函数准确写成有限个固定 profile 函数与 s 系数的组合。有限化本身不证明相容条件为零；本稿末尾说明同一全局 profile 和全部第三阶 gauge 应如何共同进入第四阶条件。

来源：[R46 完整恢复式](R46-eight-packet-complete-third-order-circle.md)、[R47 全部第三gauge](R47-fourth-order-range-and-third-gauge.md)、[R52 真正重叠完整三阶](R52-overlapping-profile-plane-complete-third-order-circle.md)、[R53 相位分段新profile](R53-overlapping-profile-fourth-leading-gate-existence.md)及 [R54 全局共同gauge限制](R54-constant-state-helicoid-transfer-and-first-ruling-gauge.md)。六个逐点准确身份的[脚本](../scripts/literature_range_numerator_certificate.py)和[开发证书](../notes/literature-range-numerator-certificate-20261114.json)不运行几何或profile积分。

## 1. 坐标、真正导数与二次 forcing

保持

$$z=\xi+\omega(s),\quad u=h(s)/z,\quad
 e=h z-k,\quad \gamma=h_s,\quad
 \nu=\omega_s=k_s/(2h),$$

$$u_\xi=-h/z^2,\qquad
c=u_s|_\xi=(\gamma z-h\nu)/z^2.$$

活动区间 $I=[\ell,r]$ 固定在 xi 坐标中，且全 s 有 $z\ne0$。所有本稿 s 导数都固定 xi；不把它们与固定 u 的导数混用。

令正交移动框架 $F=(T,N,B)$ 满足 $F_s=F\Omega(k)$。对框架分量 V 记

$$\nabla_sV=V_s+\Omega(k)V.$$

设已知场均写成

$$Z_i(s,\xi)=F(s)V_i(s,\xi)/z.$$

它们在 I 的两个开放 collar 恒为零，且在完整几何周期上周期。取一个与 s、xi 无关的对称常数矩阵 C（可依赖外参数 theta），定义

$$H_{ab}=\sum_{i,j}C_{ij}\,\partial_aZ_i\cdot\partial_bZ_j,
\qquad a,b\in\{s,\xi\}.$$

例如 $H=(dY)^2$ 对应一个对角系数 1；$H=-\mathcal S(Y,Z)$ 对应 $C_{12}=C_{21}=-1$。所有 Taylor 等距方程的已知 forcing 都是这种有限组合。实式可以作普通复双线性延拓；需要模平方的 Gram 判定另行注明共轭。

定义四个真实分子配对

$$J=\sum C_{ij}V_i\cdot V_j,$$

$$T_\xi=\sum C_{ij}(V_i)_\xi\cdot(V_j)_\xi,$$

$$T_s=\sum C_{ij}\nabla_sV_i\cdot\nabla_sV_j,$$

$$T_{s\xi}=\sum C_{ij}\nabla_sV_i\cdot(V_j)_\xi.$$

因 C 对称且 Omega 反对称，直接求导给

$$H_{\xi\xi}=\frac{T_\xi}{z^2}-\frac{J_\xi}{z^3}+\frac J{z^4},$$

$$H_{ss}=\frac{T_s}{z^2}-\frac{\nu J_s}{z^3}+\frac{\nu^2J}{z^4},$$

$$H_{s\xi}=\frac{T_{s\xi}}{z^2}
-\frac{J_s+\nu J_\xi}{2z^3}+\frac{\nu J}{z^4}.
\tag{1}$$

这里的 ss、sxi 都是适应坐标的完整分量，已经包含 c 引起的混合项。

## 2. 右 collar 锚定的 normal 分量没有未知尾

完整 range 的 normal 分量 rho 满足

$$\rho_\xi=\frac{H_{\xi\xi}}{2u_\xi},\qquad \rho(s,r)=0.$$

置

$$\boxed{B=\frac J{2h},\qquad
P(s,\xi)=-\frac1{2h(s)}\int_r^\xi T_\xi(s,\eta)\,d\eta.}\tag{2}$$

则 (1) 直接给

$$\boxed{\rho=P+B/z.}\tag{3}$$

在右 collar，Vi、J、Txi 都为零，所以 B=P=rho=0，确实采用了同一个真实右锚。左 collar 中 B=0 而 P 是其真实累计积分，不得自行重置。

由于 physical u 从右 xi 端对应的下端增至左 xi 端对应的上端，完整 ruling 积分准确为

$$\boxed{\int H_{uu}\,du=2\rho(s,\ell)
=\frac1{h(s)}\int_\ell^rT_\xi(s,\xi)\,d\xi.}\tag{4}$$

因此两 collar 可同时为零的第一条件，恰为 (4) 对全部 s 为零。这个结论保留了跨 packet 的全部尾积分。

## 3. 整个 characteristic RHS 的有理项准确相消

记

$$K_0=kz^2-\frac{k^2+1}{h}z,\qquad
\lambda=\frac c{u^2}=\frac{\gamma z-h\nu}{h^2}.$$

完整 characteristic 方程使用

$$W_s=\mathcal R_H
=\frac{H_{ss}}{2u^2}+K_0\rho-\lambda\rho_s.$$

代入 (1)、(3)，使用 $J=2hB$ 与 $J_s=2\gamma B+2hB_s$，所有 1/z 和 1/z² 项逐对消去。准确剩下

$$\boxed{\mathcal R_H=
\frac{T_s}{2h^2}+K_0P-\lambda P_s
+\left(kz-\frac{k^2+1}{h}\right)B
-\frac\gamma{h^2}B_s.}\tag{5}$$

这里没有丢掉只在全周期积分后为零的 s 总导数，也没有假设 h、k 或 omega 为常数。连接段上的 gamma、nu 及真实 W 段首值都保留。

例如待消去的有理部分正是

$$-\frac\nu{2h^2z}J_s+\frac{\nu^2}{2h^2z^2}J
+\frac\nu{hz}B_s+\frac{\gamma\nu}{h^2z}B
-\frac{\nu^2}{hz^2}B=0.$$

## 4. 恢复中的 eta0 同样没有隐藏分母

适应坐标的完整定义是

$$\eta_0=\frac{H_{s\xi}-c\rho_\xi}{2u_\xi}-\frac12\rho_s.$$

继续代 (1)–(3)，用同一 J 与 B 关系，准确得到

$$\boxed{\eta_0=-\frac{T_{s\xi}}{2h}
+\frac{\gamma z-h\nu}{2h}P_\xi
+\frac\gamma{2h}B_\xi-\frac12P_s.}\tag{6}$$

1/z 与 1/z² 项在这里也是逐点相消，而不是依靠周期积分。固定 u 与固定 xi 的转换已体现在 eta0 的定义中。

解 (5) 后，置

$$A=\frac12W_\xi+\frac{\eta_0}{h}.$$

整个恢复场可以直接用一个新分子写为

$$\boxed{V_{\rm new}=(A,\ zP+B,\ eA-hW),\qquad
Z_{\rm new}=F V_{\rm new}/z.}\tag{7}$$

这与原恢复式 $\zeta=u^2W$、$\eta=\eta_0-uW+hW_\xi/2$、
$p=(\zeta+u\eta)/h^2$、$q=\eta-kp$ 完全相同。

## 5. 两个完整 range 条件及全周期的含义

若 (4) 对全部 s 为零，则 P、B、rho 在两 collar 都为零，(5)、(6) 也在两 collar 为零。第二个完整条件是

$$\boxed{\int_0^L\mathcal R_H(s,\xi)\,ds=0
\quad\text{作为整个 xi 函数成立。}}\tag{8}$$

在 (8) 下，以同一个 s0 和同一个初值 W0(xi) 积分 (5)，W 为周期函数；若 W0 在两 collar 为零，恢复 (7) 亦保持双 collar。反之，任何周期双 collar 解都必须满足 (4)、(8)。这正是完整 range，没有把单 P、常段或有限 xi 节点当作完整周期。

四块模型的完整周期 L 覆盖全部四块及光滑连接。单 P 的某条高阶周期函数可以非零，即使四块总和为零；段首 W 必须由上一段真正积分而来。公式 (2)、(5) 全程只用一套锚，不能为了让不同 packet 看似局部而分段重置。

## 6. 任意固定有限阶的分离变量空间准确闭合

假设已有分子均是有限和

$$V_i(s,\xi)=\sum_{a=1}^{M_i}c_{ia}(s)\psi_{ia}(\xi),$$

其中 c 为三维向量系数，psi 是固定光滑 profile 函数。第一阶 $Y_f,Y_g$ 已有这种形式，因为其分子是
$(-f'/2,0,hf-ef'/2)$ 及 g 的同式。

在 (1)–(7) 中，只会产生以下有限操作：

1. 对已有 profile 函数求 xi 导数、相乘，以及乘有限次 xi；
2. 对有限个固定 profile 乘积取同一个右端 r 锚的 Volterra 原函数；
3. 对有限个 s 系数求导、相乘，乘 h、1/h、k、omega、gamma、nu；
4. 对有限个真实 s 系数沿同一全局 s 起点积分。

例如 P 由固定函数 $\int_r^\xi\psi_a'(\eta)\psi_b'(\eta)d\eta$ 的有限组合得到；R 中 z、K0、lambda 只是 xi 的低次多项式。然后 W 按这些固定 profile 的真实 s 系数积分。因此新分子 (7) 仍属于一个有限生成的分离变量空间。

**归纳结论。** 从有限个初始 profile 出发，只要前面各阶的完整相容条件已经支付，每一个指定有限 Taylor 阶的完整 forcing、rho、R、eta0、W 和恢复场都可用这种有限表示准确构造。空间维数可随阶数增长；本稿不提供统一维数界或收敛定理。

这不要求不同 packet 的高阶场各自局部化：跨 packet 的尾和 s 积分常数会作为实际固定 profile 原函数与实际系数继续保留。两 collar 失败时的常尾也必须保留，直到 (4) 真正被支付。

## 7. 有限表示如何等价检验整个函数，而非采样

把 (5) 写成 $\mathcal R_H=\sum_a r_a(s)\psi_a(\xi)$，则整个周期函数是

$$\mathscr P_H(\xi)=\sum_a\mu_a\psi_a(\xi),\qquad
\mu_a=\int_0^Lr_a(s)\,ds.$$

若已选真正线性无关的 profile 基，(8) 等价于全部相应系数为零；若保留了冗余生成元，就必须取它们的准确函数关系，而不能把“每个生成元系数分别为零”误称必要条件。

一种不依赖预先独立性声明的精确写法是 Gram 矩阵

$$G_{ab}=\int_I\overline{\psi_a}\psi_b,$$

则 $\mathscr P_H\equiv0$ 当且仅当 $\mu^*G\mu=0$，亦即 $\mu\in\ker G$。连续性保证积分零与整个函数零等价。

同样，(4) 可写成有限组合 $K_H(s)=\sum_bm_b\kappa_b(s)$；对真实全周期的几何函数取 Gram 矩阵，就能准确表示其为零的条件。这些是有限个真实积分/代数条件，不是有限网格的点值替代。

数值 Gram 的小特征值、小正残差或有限节点零值都不自动给准确独立性或准确 range；实际 Actions 计算必须保留这个证据边界，并对同一冻结设计作加密。

## 8. 第四阶及全部第三 gauge 的有限完整判据

对已经完整构造的重叠三阶圆，第四 forcing 是

$$H_{4,\theta}=-\{(dZ_\theta)^2+\mathcal S(Y_\theta,W_\theta)\}.$$

这里二、三阶通道均按真正重叠公式保留；它是 §1 的常系数二次组合。故 (1)–(8) 一次适用于整条变系数几何，包括连接段。theta 依赖只有有限个三角谐波，可逐个独立实谐波检验整个 ruling 与 period。

固定选定的二阶解。任意第三阶双 collar 周期齐次改动是 $Y_{\chi_\theta}$。它对第四 period 的改变量，由全零二阶算子的极化准确为零；对第四 ruling 的改变量落在固定空间

$$\mathcal W=\{s\mapsto w(s)\cdot v:\ v\in\mathbb R^3\},$$

其中

$$w=\left(\frac{(h\omega-k)^2+1}{4h},\frac{h\omega-k}{2},\frac h4\right).$$

因此，对每个原始第四相位谐波，必要条件是整个 period 为零，整个 ruling 落在 W。它们可用 §7 的有限表示与真实 Gram 商空间完整检验，不能逐常段单独挑一个不同 v。

对于本会话的相位分段重叠构造，这个条件也充分。理由如下：三个交叉矩密度为

$$L_0\phi=\phi'''',\quad
L_1\phi=\xi\phi''''+2\phi''',\quad
L_2\phi=\xi^2\phi''''+4\xi\phi'''.$$

对非零紧支撑单 profile，这三者线性无关。若六个密度 $L_if,L_ig$ 有常系数关系，把它限制到某个个体 bump，那里 $f=a_j\eta_j,g=b_j\eta_j$，单 profile 引理迫 $a_jA+b_jB=0$。选两条非平行的复幅实方向即迫 A=B=0。因此六个密度的真实 Gram 正定，可取固定六个双矩右逆 profile：分别支付 $m(f,\psi)$ 和 $m(g,\psi)$ 的任意三个值。

若第四 ruling 为 $2w\cdot v_\theta$，选择具有双矩 $(v_\theta,0)$ 的 profile $\psi_f(v_\theta)$ 和双矩 $(0,v_\theta)$ 的 profile $\psi_g(v_\theta)$，再取

$$\chi_\theta=\cos\theta\,\psi_f(v_\theta)
+\sin\theta\,\psi_g(v_\theta).$$

则 $m(\phi_\theta,\chi_\theta)=v_\theta$，整个第四 ruling 一次清零，period 保持零。v_theta 可从原有限谐波作固定线性右逆选择，所以这是同一全局有限 profile 空间中的真实 gauge，而非逐 s 更换 profile。

由完整 range 恢复第四场即给充分性。故对固定二阶解和当前真实重叠类，**全第四存在性的剩余问题已准确约为：有限表示中的各整个周期函数为零、各整个 ruling 函数在同一个 W 内。** 这些条件目前仍未共同支付。

## 9. 下一计算与尚欠边界

可据此编译真实有限 profile 基、右锚 Volterra 表、s 系数 ODE/积分和第四完整 Gram 条件。几何/幅度/相位/归一化必须一次冻结，所有段首值和全周期闭合原样保留；必要的研究计算只在本公开仓库 Actions 执行。

本稿只证明准确有限化及固定二阶解下全部第三 gauge 的用途，没有声称某个离散矩阵已给连续 range 解。下一目标是用同一个全局 profile 与几何共同支付这些第四条件，再继续更高阶或真正非线性求解。
