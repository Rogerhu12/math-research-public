# R340：原三输入 Fourier 联合测度与真实碰撞域

日期：2026-11-13。**状态：原三变量 sigma 恒等式、完整辅助坐标投影、范数三链的全部联合测度、深度/环带/碰撞域运输均已证明。原 S 的中央零确实传播到下述明确域。R339 的独立原输入深度网格尚未由这些域覆盖，故主目标未完成。**

## 1. 原三变量恒等式的完整证明

沿用同一固定 $E:y^2=x^3+b$、$b=17$，$x'=2y$、$y' =3x^2$、
$\zeta'=-x$，$\omega=(-1+\delta)/2$、$\delta^2=-3$。
置
$$A(z)=\sigma(z)^3,\quad B(z)=\sigma(z)^3x(z)=\sigma(\delta z)/\delta,
\quad C(z)=\sigma(z)^3y(z).$$
原三变量式准确为
$$
\boxed{\begin{aligned}
&\sigma(u+v+w)\sigma(u+\omega v+\omega^2w)
                         \sigma(u+\omega^2v+\omega w)\\
={}&A(u)C(v)C(w)+C(u)A(v)C(w)+C(u)C(v)A(w)\\
&\quad-3B(u)B(v)B(w)-3bA(u)A(v)A(w).
\end{aligned}}\tag{1}
$$

**证明。** 左端除以 $A(u)A(v)A(w)$ 后，在每个变量中都是椭圆函数，
仅在原点有至多三阶极。对 $u$ 的周期性由 $1+\omega+\omega^2=0$ 直接消去交叉项；
对 $v,w$ 则使用原 CM 准周期式
$\eta(\omega\lambda)=\omega^{-1}\eta(\lambda)$。
所以原整个函数属于三个 $H^0(E,\mathcal O(3O))$ 的外积，
每个变量的实际基为 $A,B,C$。

左端对三变量置换对称。例如交换 $u,v$ 时，后两个因子分别乘
$\omega,\omega^2$ 并互换，原 sigma 相位乘积为一。
变换 $(v,w)\mapsto(\omega v,\omega^2w)$ 只轮换三个因子。
在 $\mu_3$ 下 $A,C$ 的型为零、$B$ 的型为一，故允许的基项要么没有 B，
要么三个变量全为 B。整体反号的奇性又排除含偶数个 A 的项。
因此只剩对称的三个 ACC、AAA、BBB。

$A(0)=B(0)=0,C(0)=-1$；令 $v=w=0$ 得 ACC 系数为一。
最低三次式是 $u^3+v^3+w^3-3uvw$，故 BBB 系数为 $-3$。
令 $u=v=w$，左端为零，右端剩
$A(u)^3\{3y(u)^2-3x(u)^3+c\}$，曲线方程迫 $c=-3b$。
这证明全部 (1)，不只证明有限 jet。$\square$

## 2. 同一原测度的三输入变换

固定普通 $p>7,p\ne17$，所有对象及周期 $\Omega=\Omega_p$ 均沿用 R316、R339。
令 $\nu=\nu_{\sigma,17}$，并定义
$$
F=\frac1\delta\begin{pmatrix}1&1&1\\1&\omega&\omega^2\\
1&\omega^2&\omega\end{pmatrix},\qquad
Q(X_1,X_2,X_3)=-\frac{(X_2-X_3)^2}{2\Omega^2},\qquad
\rho=\frac{x\nu}{\Omega}.
\tag{2}
$$
直接计算得
$$\boxed{\det F=1,\quad F^2=-P_{23},\quad Q\circ F=Q.}\tag{3}$$
$F$ 因而是原 $\mathbf Z_p^3$ 的整可逆变换。
$\rho$ 质量一，且原 core 准确给
$$\boxed{\rho|_{p\mathbf Z_p}=t_p[\kappa]_*\rho,\qquad
\rho(p^n\mathbf Z_p)=t_p^n.}\tag{4}$$
所有 $t_p,\lambda,\kappa$ 均为 R339 的原值。

对第 $i$ 个坐标，记 $\mathsf P_{0,i}$ 为三个单位根推送的平均：
$$\mathsf P_{0,i}=\frac13\sum_{k=0}^2[D_{i,k}]_*,$$
其中 $D_{i,k}$ 将第 $i$ 个坐标乘 $\omega^k$。
**完整联合测度恒等式**是
$$
\boxed{\mathsf P_{0,2}\mathsf P_{0,3}
          F_*(Q\nu^{\otimes3})
             =\delta^{-1}\nu\otimes\rho\otimes\rho.}\tag{5}
$$

**证明。** 用原规范 Laplace 变换
$\mathcal L_\mu(\boldsymbol z)=\int\exp(\sum z_iX_i/\Omega)d\mu$，
有 $\mathcal L_\nu(z)=\sigma(z)$。
$F$ 对称，所以 $F_*\nu^{\otimes3}$ 的变换就是 (1) 左端在
$(u,v,w)=(z_1,z_2,z_3)/\delta$ 的值。
由 $Q\circ F=Q$，乘 Q 对应准确微分算子
$$\partial_2\partial_3-(\partial_2^2+\partial_3^2)/2.$$
在 $\mu_3$ 下，$A(z/\delta),C(z/\delta)$ 的型为零，$B(z/\delta)$ 的型为一。
导数将型减一。因此 ACC 和 AAA 经任一上述二阶单项式微分后，
至少一个辅助变量的型非零，被 (5) 的两个平均杀掉。
BBB 部分在 (1) 中准确为
$$-3\prod_i B(z_i/\delta)=\delta^{-1}\prod_i\sigma(z_i).$$
它的两个平方导数项也被杀掉，只留下
$\delta^{-1}\sigma(z_1)\sigma'(z_2)\sigma'(z_3)$，
这正是 (5) 右端的变换。

所有测度都有界，F 整可逆，Q 为整有界权。变换相等给所有多项式矩相等，
再由各坐标的 Mahler 多项式逼近得到测度本身相等。
所以 (5) 可以测试局部常数域及一般有界连续函数，不只是形式矩等式。$\square$

## 3. 原 sigma 因子的真实域运输

原范数三公式在尺度 $c\in\mathbf Z_p^\times$ 上写为
$$\sigma(cz)=\delta\sigma(cz/\delta)\Theta(cz/\delta).$$
将 Theta 写成原两 sigma 平方差权，三输入输出正是
$$cR_1,\qquad (R_1,R_2,R_3)=F\boldsymbol X.$$
因此对任意有界连续的 $f$，以及满足
$$\Phi(\omega R_2,R_3)=\Phi(R_2,\omega R_3)=\Phi(R_2,R_3)$$
的有界连续 $\Phi$，(5) 直接给
$$
\boxed{\delta\int f(cR_1)\Phi(R_2,R_3)
                        \,dF_*(Q\nu^{\otimes3})
 =\left(\int f(cx)\,d\nu(x)\right)
  \left(\int\Phi\,d\rho^{\otimes2}\right).}\tag{6}
$$
这里 (6) 作用于未平均的实际输入测度，因为测试函数已被两个平均固定。
没有要求 f 具有某个额外 tame 型。

把同一个变换用在原 S 的任意一个 sigma 因子，其他所有原因子保持全域，
并令 $y$ 为真正的完整相加输出。则 (6) 给
$$
\boxed{J_{S,\Phi}(u)=\left(\int\Phi\,d\rho^{\otimes2}\right)J_S(u).}\tag{7}
$$
(7) 保留 $y\in\mathbf Z_p^\times$、全部 tame 分支和所有 u；
原 $J'_S(0)=0$ 因而确实传播到这些域的中央导数。
如果另外限制其他原因子，右端变成那些限制下的原函数，不能再直接替成 $J_S$。

特别，辅助深度条件和 exact 环带条件分别给
$$
\boxed{J_{S;R_2\in p^a,R_3\in p^b}(u)=t_p^{a+b}J_S(u),}\tag{8}
$$
$$
\boxed{J_{S;v_pR_2=a,v_pR_3=b}(u)
       =t_p^{a+b}(1-t_p)^2J_S(u).}\tag{9}
$$
对只有一个坐标取环带的情形，只乘一次 $1-t_p$。
这些比例因子都非零，故相应中央零条件与原条件等价。

## 4. 一个真正不同的域族：原三输入的碰撞

(6) 不限于分别的深度。直接计算原线性形式，得到
$$
\boxed{R_2^3-R_3^3
 =(X_1-X_2)(X_2-X_3)(X_3-X_1),}\tag{10}
$$
$$\boxed{R_2R_3=-\frac{X_1^2+X_2^2+X_3^2-X_1X_2-X_1X_3-X_2X_3}{3}.}\tag{11}$$
三次方差在两辅助坐标的独立 $\mu_3$ 作用下不变。
所以对任意 $n\ge0$，原域
$$\{v_p((X_1-X_2)(X_2-X_3)(X_3-X_1))\ge n\}$$
也给 (7) 的真实零传播；其比例因子就是
$\rho^{\otimes2}\{v_p(r^3-t^3)\ge n\}$。
该比例因子保留为实际测度值，没有被假定为单位。
还可同时要求 (11) 分子为单位。

后一要求等价于 $R_2,R_3$ 都是单位。当 $n\ge1$ 时，
三个因子 $R_2-\omega^kR_3$ 至多一个非单位。
因此相应域准确是“三个原输入中恰有一对同余到指定深度，第三个在不同剩余类”
的并；不是一个可以随意删去其他两支的单独碰撞域。
所有相加输出仍按原完整 y 测试。

## 5. R339 整条范数三链的联合坐标

保持 R339 的链长度 m、末端 sigma 变量 Z 和每层配对变量 $X_{h,+},X_{h,-}$。
从内向外定义一组真实整坐标：
$$U_m=Z,\qquad
(U_{h-1},V_h,W_h)=F(U_h,X_{h,+},X_{h,-})\quad(h=m,\ldots,1).\tag{12}$$
这是原 $2m+1$ 维输入空间的整可逆变换 $T_m$。
根输出准确为
$$\boxed{U_0=\delta^{-m}Z+\sum_{h=1}^m\delta^{-h}(X_{h,+}+X_{h,-}),}\tag{13}$$
所以原尺度二的整个输出是 $2U_0$，恰与 R339 的各个实际尺度一致。
置
$$Q_m=\Omega^{-2m}\prod_{h=1}^m
 \left(X_{h,+}X_{h,-}-(X_{h,+}^2+X_{h,-}^2)/2\right).$$
记 $\mathsf P_{\rm aux}$ 为所有 $2m$ 个辅助坐标上的独立 $\mu_3$ 平均。
完整的链式联合恒等式是
$$
\boxed{\mathsf P_{\rm aux}(T_m)_*
       (\delta^m Q_m\nu^{\otimes(2m+1)})
       =\nu(U_0)\otimes\rho^{\otimes2m}.}\tag{14}
$$

**证明。** 最内层用 (5)，乘回原范数三系数 $\delta$，
便把三个原 sigma 输入准确化为一个 sigma 主坐标和两份 rho。
下一层只作用于该主坐标及自己新加入的一对变量，不动已经产生的辅助坐标。
因此原平均与下一层变换交换，可再次用 (5)。逐层即得 (14)。
这同时证明全部原权和所有 $\delta$ 因子都被保留。$\square$

将其附回 (1) 型原六 sigma S 的其余五因子，完整真实输出记为 Y。
对 $(Y,V_1,W_1,\ldots,V_m,W_m)$ 的推送再取辅助平均，得到
$$\boxed{\nu_S(Y)\otimes\rho^{\otimes2m}.}\tag{15}$$
因此任意在各辅助坐标上分别 $\mu_3$ 不变的测试函数 Phi，都准确满足
$$\boxed{J_{S,\Phi}(u)=\left(\int\Phi\,d\rho^{\otimes2m}\right)J_S(u).}\tag{16}$$
比如所有辅助坐标分别处于给定深度/环带时，比例因子是
$t_p^{\sum n_i}(1-t_p)^e$，e 是取 exact 环带的坐标数。
各层的碰撞测试同样可用，但须在 (12) 的真实坐标中书写。

(14) 的辅助变量与 R339 的原叶输入不是同一组变量。
R339 的非零域还限制原尺度一 sigma 为单位、其他原 sigma 为深输入。
这些条件不因 (14) 自动变成只依赖辅助变量的测试。
因此本篇没有从 (16) 推出 R339 的全部独立深度网格为零。

## 6. 原三因子的一项额外准确运输

未加 Q 时，(1) 同时给一个真实三项测度恒等式。
设 $D_k=\operatorname{diag}(\omega^k,1,1)$。对第一变量取型一投影，
ACC、AAA 全被消去，故
$$
\boxed{\nu^{\otimes3}=\frac\delta3\sum_{k=0}^2
                       \omega^{-k}(D_kF)_*\nu^{\otimes3}.}\tag{17}
$$
这仍是原同 sigma 测度，不是另造具有相同低矩的测度。

原 S 中确实含有尺度 $(1,2,\delta)$ 的三个因子。
对 $\boldsymbol c=(1,2,\delta)^t$，全部输出尺度是
$$
\begin{array}{c|c|c}
k&F D_k\boldsymbol c&\text{未限制输入的原三因子倍数}\\\hline
0&(-2\omega,-\omega,-\delta\omega^2)&-\omega\\
1&(\delta\omega^2,1,2\omega)&1\\
2&(-\omega,0,\delta-2)&0
\end{array}\tag{18}
$$
前两行只是三个原因子的置换和真实 CM 单位相位；第三行有一个
完全不进入输出的 sigma 输入，其总质量为零。
总式的系数准确为
$\delta(-\omega+\omega^2)/3=1$，与 (17) 一致。

对任意真实输入域 D，正确的条件式始终是
$$
\boxed{\int_D f(\boldsymbol c^t\boldsymbol x)\,d\nu^{\otimes3}
 =\frac\delta3\sum_{k=0}^2\omega^{-k}
 \int_{(D_kF)^{-1}D}
        f((F D_k\boldsymbol c)^t\boldsymbol x)\,d\nu^{\otimes3}.}\tag{19}
$$
可在 f 中保留其余原输入以及真正的输出单位条件。
(18) 的第三行只在未受相关限制时由零质量消失；
如果 $(D_2F)^{-1}D$ 耦合了那个被忽略的坐标，不能删除该项。
(19) 因而提供进一步处理交叠的完整原域关系，未凭 (18) 的未限制零偷加子域零。

## 7. 当前准确接口

本篇付出的正向输入是 (5)、(14)、(16)：原中央零可以真正传播到任意长范数三链的
辅助深度、环带与三次碰撞域；全部单项式、CM 相位、原周期和相加单位条件均保留。
R339 已另付某些原叶输入域必有非零中央导数。
要合并二者，还须用 (19) 或 R337 的真实四输入运输控制相应交叠，
而不是把两种坐标域直接认成同一域。

## 精确证书与依赖

- `scripts/check-jzero-ternary-fourier-joint-domains.py/.json` 核对 F、Q、两个碰撞恒等式、全部型投影、原三因子输出表和链坐标。
- R316：原 sigma/Theta 测度与 CM/周期规范。
- R333：同一固定 S 的六 sigma 表示。
- R339：原范数三链及其独立原输入深度的单位系数。
