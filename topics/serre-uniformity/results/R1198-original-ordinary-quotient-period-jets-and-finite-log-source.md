# R1198：原 ordinary 商的全部小阶周期 jet 与指定有限对数源

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明。** 对原 $p=12g-1>37$ 模型，R1196 所需原 $G(b_{\rm lift})^2$ 在每个无支撑 supersingular 尾的全部 $1\le a\le m=(p-1)/2$ 次有限对数输入，由同一个有理 Gauss–Manin 方程、原 framing 的一条 opposite line 和原一次单位 $\theta_s$ 明确给出。不再把 $B_s$ 的各个高 Taylor 系数作为独立未知输入。在原 $b=0$ CM 支，第五和第七槽分别为 $-13\theta_0^5/40$ 与 $-149\theta_0^7/1680$，均为当前素数范围内的单位；最高第 $m$ 槽也化为原 $Q_p$ 的一个明确有限系数。

这些是同一个原普通节点及同一 Čech 来源的系数。本文不把某个节点输入的单位性等同于整个 Jacobian 的首列单位性，也不删 R1196 中低次数与高 normal 微分的交叉项、三条支持尾或指定 $C$ 的投影。

## 1. 固定原来源和有限精度

保持 R1014、R1018、R1021、R1023、R1196 的全部对象：
$$
p=12g-1>37,\qquad m=(p-1)/2,\qquad e_0=m(p+1),
\qquad \pi_0^{e_0}=p,\qquad\varepsilon=\pi_0^m,
$$
$$
P=(p-1)D_0,\qquad
G(b)=\frac{(b-1)^2}{b^2+b+1},\qquad
r(b)=1-b^3,\qquad
\lambda(b)=2G'(b)/G(b)=-\frac{6(b+1)}{r(b)}.
\tag{1198.1}
$$
这里的 $r(b)$ 是多项式，不是惯性类型的指标。原 fine 家族为
$$
E_b:\ y^2=x^3+3br(b)x+r(b)(1-2b^3),
\qquad \omega=dx/(2y),\quad\eta=x\omega.
$$
全部无支撑 $e=1$ supersingular 点构成 $S=\{A_p=0\}$，且 $r(s)\ne0$。在每个 $s\in S$，取原 ordinary connected line 和同一个 trace-zero Cartan 方向 $Q=\sqrt{-3}P_{\rm level}$；$b_{\rm lift}$ 是实际 $E/\langle Q\rangle$、连同原六标记运输给出的参数。其约化是原 Igusa 参数 $b$，而原 source 遗忘参数满足 $a=b^p$。这两个参数不互换。

R1021 的同一 framing 本征参数给
$$
b_{\rm lift}=B_s(u'),\qquad
u'=\varepsilon(c_{Q,s}\psi_s+pR_{Q,s}),\qquad
\psi_s=\beta_Q^{p-1},
$$
其中 $B_s\in W(k)[[u']]$，$B_s(0)$ 是原未分歧提升，约化为 $s$；$B_s'(0),c_{Q,s}\in W(k)^\times$ 都是单位。定义
$$
\theta_s=\overline{B_s'(0)c_{Q,s}}\in k^\times.
\tag{1198.2}
$$
它就是 R1018.15、R1023.4 的原单位，不作重新定标。$\psi_s$ 在所选普通节点的 full-$p$ 图上有该实际定义；不把它当作整个 normalizer 商尾上的全局正则函数。

本文读取 $R/(\pi_0^{m^2+1})$。此环中特征为 $p$，$I=(\pi_0^m)$ 满足 $I^{m+1}=0$，故使用 R1196 的有限群对数
$$
\ell_I(1+x)=\sum_{a=1}^m\frac{(-1)^{a+1}x^a}{a}.
$$
所有计算先在这个实际有限 Picard/Čech 来源中进行。不是把未截断的 $p$ 进对数随意约化模 $p$。

## 2. 原 framing 的两条晶体线

在 $E_s$ 的 $H^1_{\rm dR}$ 中，原 framing 的 $\mu_{p^2-1}$ 保持 Hodge 线并有另一条本征线。将后一条唯一写成
$$
\mu_s=\eta_s+\mathfrak s_s\omega_s.
$$
这只是原本征线相对已固定 $(\omega,\eta)$ 的坐标；不另选一条任意 opposite line。置
$$
a_{\rm GM}(b)=\frac{b^2}{2r(b)},\qquad
c_{\rm GM}(b)=\frac1{2r(b)},\qquad
\alpha_s=a_{\rm GM}(s)-c_{\rm GM}(s)\mathfrak s_s.
\tag{1198.3}
$$
$\alpha_s$ 是一个实际剩余域标量，不能擅设为零。

R1023.19 的同源 Gauss–Manin 方程为
$$
\nabla\omega=a_{\rm GM}\omega+c_{\rm GM}\eta,
\qquad
\nabla\eta=\frac b2\omega-a_{\rm GM}\eta.
$$
在以 $(\omega_s,\mu_s)$ 为初值的水平晶体标架内，$\omega_b$ 的两个坐标可写为 $f_0(b-s)$ 与 $c_{\rm GM}(s)f_1(b-s)$。于是
$$
f_0(0)=1,\quad f_0'(0)=\alpha_s,\qquad
f_1(0)=0,\quad f_1'(0)=1.
$$
消去 $\eta$，两个坐标均满足
$$
f''+P_0(s+t)f'+Q_0(s+t)f=0,
$$
$$
P_0(b)=-\frac{3b^2}{r(b)},\qquad
Q_0(b)=-\frac{b(5-4b^3)}{4r(b)^2}.
\tag{1198.4}
$$
全篇仅取其次数不超过 $m$ 的唯一解。定义归一的有限周期比
$$
\xi_s(t)=\frac{f_1(t)}{f_0(t)},\qquad \xi_s(0)=0,\quad\xi_s'(0)=1.
\tag{1198.5}
$$

### 2.1 整比较为何一直有效到 $m$

令 $A_s=k[t]/(t^{m+1})$。理想 $(t)$ 有明确的 nilpotent divided powers：次数不超过 $m$ 时为 $t^j/j!$，较高次数为零。因 $m<p$，其中没有反除 $p$。Messing 的实际晶体构造和 deformation theorem 给原 $p$-divisible group 与其特殊 framing 晶体之间的函子性比较；对原椭圆曲线，其晶体与原 de Rham 模块相容。这里只使用这个有限 PD 厚化，不引用无限盘上的 integral period map。

在这个比较中，水平 Taylor 标架也可直接由原连接递推构造：每一步只除以 $1,\ldots,m$，且其初值唯一。因此它与原晶体比较相同，并对 framing 自同态相容。原 framing 在特殊晶体上沿两条本征线作线性作用；相应周期比作一个特征乘法作用。Kodaira–Spencer 的 $c_{\rm GM}(s)$ 是单位，故其 tangent character 正是 R1021 已固定的 target 参数 $u'$ 的 character，阶为 $p+1$。

这里须保真实 Frobenius 方向：source 的 framing $\zeta$ 在特殊 quotient $E'=E/F$ 上成为 $\zeta^p$，故 target $u'$ 的 character 为
$(\zeta^p)^{1-p}=\zeta^{p-1}$。本篇的 Gauss–Manin 基、$\alpha_s$ 和周期比都在 target 参数 $b=s$ 的 $E_s$ 上定义，未把 source 参数 $a=s^p$ 的基无扭搬来。特殊 framing 自同态固定 $k$；不再对 $\alpha_s,\theta_s$ 多施一次算术 Frobenius。上述同 target 的 Kodaira–Spencer 等变性锁定周期比的方向，不任选其倒数。

写 $\xi_s(B_s(T)-s)$ 时，$B_s$ 先约化模 $p$，因此 $B_s(0)=s$。该级数与 $T$ 同 character；次数 $a$ 的非零项要求 $a\equiv1\pmod{p+1}$。在 $1\le a\le m$ 中只允许 $a=1$。比较一次项得
$$
\boxed{\quad
\xi_s(\overline{B_s}(T)-s)
 =\overline{B_s'(0)}\,T\pmod{T^{m+1}}.
\quad}
\tag{1198.6}
$$
这是同一个原 $B_s$ 的有限 jet 比较，不是仅由两个参数都不为零作任意坐标同构。全部 Weil 分支和标记换基沿晶体的函子性运输，$\alpha_s,\theta_s$ 随原分支一起保留。

## 3. 可直接执行的有限递推

写 $P_0(s+t)=\sum_jP_jt^j$、$Q_0(s+t)=\sum_jQ_jt^j$，$f(t)=\sum_nf_nt^n$。从给定 $f_0,f_1$ 起，原方程逐项给
$$
\boxed{\quad
f_{n+2}=-\frac1{(n+2)(n+1)}
 \sum_{j=0}^n\bigl(P_j(n-j+1)f_{n-j+1}+Q_jf_{n-j}\bigr),
\quad0\le n\le m-2.
\quad}
\tag{1198.7}
$$
所以 (1198.6) 所需的全部系数是实际 $s,\alpha_s$ 的有限有理表达式。分母只含 $2$ 和不超过 $m$ 的整数。$r(s)$ 只作为已经非零的单位出现。

此处没有把实际 $\mathfrak s_s$ 改成一个待选方便值；在一般 $s$，其原 framing 线仍是一个明确但必须保留的输入。

## 4. 同一 $G^2$ 的全部有限对数系数

对任意 $1\le a\le m$，定义
$$
\boxed{\quad
\mathcal D_a(s,\alpha_s)
 =\frac1a[t^{a-1}]
   \lambda(s+t)\left(\frac t{\xi_s(t)}\right)^a.
\quad}
\tag{1198.8}
$$
这里 $t/\xi_s(t)$ 的常数项为一，故该式是有限幂级数代数中的合法系数。

**定理 1198.1。** 在原无支撑尾的实际普通节点图上，按 R1018.21 的 $e_s/e_I$ 方向，有
$$
\boxed{\quad
\ell_I\!\left(
 \frac{G(b_{\rm lift})^2}{G(B_s(0))^2}\right)
 \equiv\sum_{a=1}^m
  \varepsilon^a\theta_s^a
  \mathcal D_a(s,\alpha_s)\psi_s^a
 \pmod{\pi_0^{m^2+1}}.
\quad}
\tag{1198.9}
$$
各剩余域系数可取 $W(k)$ 中任意整提升；这些提升的差含 $p$，超过本式精度。这里不将一般分歧环 $R$ 中只差 $\pi_0$ 的任意提升混同于未分歧提升。

**证明。** 设 $b=s+J_s(V)$ 为 $\xi_s$ 的有限逆级数。由 (1198.6)，原 $B_s(T)$ 的所需截断就是 $s+J_s(B_s'(0)T)$。对
$$
F_s(t)=\log\frac{G(s+t)^2}{G(s)^2},\qquad F_s'(t)=\lambda(s+t),
$$
使用次数不超过 $m$ 的 Lagrange 反演，得到
$$
[V^a]F_s(J_s(V))
 =\frac1a[t^{a-1}]\lambda(s+t)(t/\xi_s(t))^a.
$$
本处的 log 是有限截断；恒等式可先在特征零有理幂级数中证明，再因所有所用分母为 $p$ 单位而约化。代入原 $u'=\varepsilon(c_{Q,s}\psi_s+pR_{Q,s})$，保留一次单位的乘积 (1198.2)，即得 (1198.9)。含 $pR_{Q,s}$ 的项至少在 $\pi_0^{e_0+m}$；而 $a\ge m+1$ 的有限幂次至少在 $\pi_0^{m(m+1)}$，均超过 $m^2$。

这一步没有在同一个函数域中另选 $p$ 次根，也没有将原 $a=b^p$ 当作 target 参数。常数分母始终为同一 frame 上的 $G(B_s(0))^2$。所指仿射/节点重叠上的公式不把 $R_{Q,s}$ 宣称为紧化全局正则函数；后续全图运输仍按原模型的各图及过渡执行。

### 4.1 opposite line 的准确三角变换

先只作有限周期坐标的代数比较。把初始导数 $\alpha$ 换成 $\alpha+c$，则
$$
f_0^{\rm new}=f_0+cf_1,\qquad f_1^{\rm new}=f_1,
\qquad \xi^{\rm new}=\frac{\xi}{1+c\xi}.
$$
代入 (1198.8)，逐项二项展开给
$$
\boxed{\quad
\mathcal D_a(s,\alpha+c)
 =\sum_{b=1}^a\binom{a-1}{b-1}c^{a-b}\mathcal D_b(s,\alpha).
\quad}
\tag{1198.10}
$$
因此更换 opposite 并不只改变一个最高系数；它混入全部较低槽。若在实际几何中更换 framing 或比较标架，必须同时运输 $u'$、同一节点函数和 normal 数据。不能据此把原 $\alpha_s$ 置零而保留其余原源不动。

### 4.2 前三槽及 Schwarzian 的方向

置
$$
\mathfrak q_s=\alpha_s+P_0(s)/2,\qquad
\mathcal S=2Q_0-P_0'-P_0^2/2
 =\frac{b(b^3+7)}{2(1-b^3)^2}.
$$
这里 $\mathcal S=\{\xi_s,t\}$，是周期比的 Schwarzian。直接展开 (1198.8) 得
$$
\mathcal D_1=\lambda,\qquad
\mathcal D_2=\frac{\lambda'}2+\mathfrak q_s\lambda,
$$
$$
\boxed{\quad
\mathcal D_3=\frac{\lambda''}6+\mathfrak q_s\lambda'
                  +(\mathfrak q_s^2-\mathcal S(s)/6)\lambda.
\quad}
\tag{1198.11}
$$
右侧 $\lambda$ 及其导数均在 $s$ 评价。负的 Schwarzian 项来自使用周期比的逆级数，不能把 $B_s$ 与 $\xi_s$ 的 Schwarzian 同号代换。

## 5. 实际源的统一多项式次数界

把 $s,\alpha_s$ 暂写为独立变量 $S,H/(1-S^3)$，并给 $S,H$ 分别权 $1,2$。存在明确由 (1198.7)–(1198.8) 定义的多项式
$$
\mathcal P_a(S,H)\in\mathbf Z[1/2,1/a!][S,H]
$$
使
$$
\boxed{\quad
(1-s^3)^a\mathcal D_a(s,\alpha_s)
 =\mathcal P_a(s,(1-s^3)\alpha_s),
\qquad\deg_{(1,2)}\mathcal P_a\le2a-1.
\quad}
\tag{1198.12}
$$

**证明。** 在 $P_0(S+t)$ 的第 $j$ 系数乘 $(1-S^3)^{j+1}$ 后，分子次数至多 $2j+2$；$Q_0$ 的相应分母为 $(1-S^3)^{j+2}$，分子次数至多 $2j+4$；$\lambda$ 的相应界为分母 $(1-S^3)^{j+1}$、分子次数至多 $2j+1$。这些界由对三个已显示的有理函数直接展开获得。

对 (1198.7) 归纳，$f_{0,n}(1-S^3)^n$ 的权次数至多 $2n$；$f_{1,n}(1-S^3)^{n-1}$ 的权次数至多 $2n-2$。因此 $[t^j](t/\xi)$ 乘 $(1-S^3)^j$ 后的权次数至多 $2j$，取其任意固定正整数次幂仍保持这个界。最后在 (1198.8) 中，$j+(a-1-j)=a-1$，总分母恰为 $(1-S^3)^a$，分子权次数至多
$$
(2j+1)+2(a-1-j)=2a-1.
$$
每一步反除的整数不超过 $a$，另有固定的 $2$；故系数环如上。

由 (1198.10)，$H^{a-1}$ 的系数准确为 $-6(S+1)$，所以这些是非零的通用多项式。对 $a=5,7$，权次数分别不超过 $9,13$。

这不是沿 supersingular 集的单变量零点界：实际 $(1-s^3)\alpha_s$ 仍可随原 framing 变化。本文没有把它宣称为一个已知低次的 $s$ 多项式。

## 6. 原 $b=0$ CM 支的第五和第七槽是单位

原 $s=0$ 是无 $D_0$ 支撑的 $e=1$ fine 支。选原 CM $\sqrt{-3}$ 作用的未分歧局部整数环所给 framing；其 Teichmüller 群包含实际 $\mu_6$。这是与原 $Q=\sqrt{-3}P_{\rm level}$ 兼容的同一个来源，不以任意局部同型代换。

在 $E_0:y^2=x^3+1$ 上，实际 $\mu_3$ 对 $\omega,\eta$ 的角色不同。原 framing 的 opposite 本征线因而正是 $k\eta$。故 (1198.3) 给 $\alpha_0=0$。将原有理方程代入 (1198.7)，纸面递推得到
$$
f_0(t)=1+\frac5{24}t^3+\frac{349}{2880}t^6+O(t^9),
$$
$$
f_1(t)=t+\frac{17}{48}t^4+\frac{1765}{8064}t^7+O(t^{10}),
$$
$$
\xi_0(t)=t+\frac7{48}t^4+\frac{1357}{20160}t^7+O(t^{10}).
$$
这些显示式只表示所需有限 jet。其逆级数为
$$
J_0(V)=V-\frac7{48}V^4+\frac{179}{10080}V^7+O(V^{10}).
\tag{1198.13}
$$
因为 $G(b)^2=(1-b)^6/(1-b^3)^2$，直接将 (1198.13) 代入有限 log 即得
$$
\boxed{\quad
\mathcal D_5(0,0)=-\frac{13}{40},\qquad
\mathcal D_7(0,0)=-\frac{149}{1680}.
\quad}
\tag{1198.14}
$$
于是原 (1198.9) 的两个实际 scalar 槽为
$$
-\frac{13}{40}\theta_0^5,\qquad
-\frac{149}{1680}\theta_0^7.
$$
分母和 $13$ 在 $p>37$ 时均为单位；$149\equiv5\pmod{12}$，不是当前 $p\equiv11\pmod{12}$ 的素数，所以第二槽也为单位。这里仍是原 $\theta_0$，未通过一次未知缩放取得单位。

再消费 R1196.25 的原局部 gap 公式，在 $Y^2=X(X^{m+1}+A_0)$、$X=z^{-2}$ 上，第五、第七项各自的特殊尾 cohomology 类准确为
$$
\boxed{\quad
-\frac{39}{20}\varepsilon^5\theta_0^5 A_0^2
      [z^{-(m-4)}],\qquad
\frac{149}{84}\varepsilon^7\theta_0^7 A_0^3
      [z^{-(m-6)}].
\quad}
\tag{1198.15}
$$
$A_0$ 是原尾方程的单位。式 (1198.15) 指有限 Čech log 中这两个次数的单独输入；它们没有包含较低次数经实际 gluing 返回的部分。

在此原 CM 支，$B_0$ 的有限逆周期坐标具有 $J_0(\zeta V)=\zeta J_0(V)$；同时 $G(b)G(\zeta b)G(\zeta^2b)=1$。所以整个有限源还满足
$$
\mathcal D_a(0,0)=0\quad\text{若 }3\mid a.
\tag{1198.16}
$$
这是同一个 $D_0$ 的非平凡三次角色条件，不是额外删除某条原输入。

## 7. 最高第 $m$ 槽回到同一个原 Hasse 多项式

本节仍在原 $s=0$、$\alpha_0=0$ 支，不引入另一个模型。记 R1023 的同一 monic 分解
$$
h_p(b)=b(1-b^3)^{2g}Q_p(b^3),\qquad
\deg Q_p=2g-1,\qquad Q_p(0)\ne0.
$$
$h_p$ 满足 (1198.4)，在零点的初值为 $0,h_p'(0)$，故唯一有限解给
$$
f_1(b)=\frac{h_p(b)}{h_p'(0)}
 =b(1-b^3)^{2g}\frac{Q_p(b^3)}{Q_p(0)}
 \pmod{b^{m+1}}.
\tag{1198.17}
$$

设 $W=f_0f_1'-f_0'f_1$。方程给 $W'=-P_0W$，而 $W(0)=1$，所以在所需有限精度内 $W=1/(1-b^3)$。因此
$$
\left(\frac{f_0}{f_1}\right)'
 =-\frac1{(1-b^3)f_1^2}.
$$
置 $n_*=2g-1$，在 $k[x]/(x^{n_*+1})$ 中明确计算
$$
\mathcal C(x)=
 \frac{Q_p(0)^2}{(1-x)^{4g+1}Q_p(x)^2}
 =\sum_{j=0}^{n_*}c_jx^j,\qquad c_0=1,
$$
$$
\boxed{\quad
\mathcal A(x)=1-\sum_{j=1}^{n_*}\frac{c_j}{3j-1}x^j.
\quad}
\tag{1198.18}
$$
每个 $3j-1$ 满足 $1\le3j-1\le6g-4<p$，全为单位。由于 $f_0'(0)=0$，$f_0/f_1$ 的积分常数为零；逐项积分上式得到
$$
b/\xi_0(b)=\mathcal A(b^3)
 \pmod{b^{3n_*+1}}.
$$
这里只作有限积分，未跨过一个 $p$ 分母。

对 $a\le m$，若 $a=3q+1$ 或 $3q+2$，(1198.8) 因 $\lambda=-6(1+b)/(1-b^3)$ 化为
$$
\boxed{\quad
\mathcal D_a(0,0)
 =-\frac6a[x^q]\frac{\mathcal A(x)^a}{1-x}.
\quad}
\tag{1198.19}
$$
若 $3\mid a$ 则由同式直接得零，与 (1198.16) 一致。特别是 $m=6g-1=3(2g-1)+2$，所以原最高节点输入为
$$
\boxed{\quad
\theta_0^m\mathcal D_m(0,0)
 =-\frac{6\theta_0^m}{m}
 [x^{2g-1}]\frac{\mathcal A(x)^m}{1-x}.
\quad}
\tag{1198.20}
$$
式 (1198.18)–(1198.20) 的 $Q_p$、主化函数、CM 支、商同源及 $\theta_0$ 都是原对象。最高槽现在是这个指定有限系数，未被改名为任意同权 hypergeometric 输入。

本文没有证明 (1198.20) 对全部素数非零。它也不是 R1196 的完整最高列：真正全列仍包含其它 supersingular 节点、三个 CM 支持尾，以及较低对数次数与较高 normal 微分的全部配对。

## 8. 进入同一个半秩问题的准确范围

R1196 在原 $E_m$ packet 上先作整投影，已经排除了首层的 formal-log $p$ 次返回。因此 (1198.9) 确给该完整有限 Čech 来源在每个无支撑节点上的所有所需 scalar 系数；原 $B_s$ 的高 jet 不再作为额外未知数据。实际源仍须在同一节点过渡、同一 vertical twister 和全部支持上粘合。

若 $5$ 或 $7$ 与 $p+1$ 互素，则相应指标属于 R1191 中同一个 $C$ 的真实 primitive 槽。式 (1198.14)–(1198.15) 提供这些小类型可用的新原节点单位，但不能由它们单独推出 $e_5\log\beta$ 或 $e_7\log\beta$ 的首类单位。对应 $E_r=\tau_r+\mathrm{PS}_{r-1}$ 的 holomorphic 自由项和单 cuspidal 分割必须保留。

对 $r=m$，R1193 已付的 CM jet 与 (1198.20) 使用同一原 CM 数据，仍须经过 R1196 的全图 Serre 配对才成为同 $\beta$ 的两列。不能由有理非零、一个节点单位或一个有限系数条件跳到整个 $p$ 进圆盘的唯一零点。

## 9. 来源与核准范围

- [R1014](R1014-original-CM-divisor-reduction-and-Igusa-Frobenius-principalization.md)、[R1018](R1018-original-CM-divisor-exact-first-formal-layer.md) §§3–6：原 $G^2$、同一 ordinary quotient、$\overline{b_{\rm lift}}=b$、原 $\theta_s$ 和 $e_s/e_I$ 的 Čech 符号。
- [R1021](R1021-actual-full-p-affine-tail-rigidity-and-quotient-parameter.md) §§1、3–4：同一 framing、实际 nonreduced affine 模 $p$ 来源和 $u'=\varepsilon(c_Q\psi+pR)$，其中 $B_s,c_Q$ 的系数来自未分歧环。
- [R1023](R1023-original-CM-divisor-complete-first-log-vector.md) §§4–5：原有理 Gauss–Manin 矩阵、Hasse 方程、三阶同源 period 比较以及原 normal 单位。本文把其中有限晶体比较逐步扩到 $m<p$，并写出全部递推及反演。
- W. Messing, *The Crystals Associated to Barsotti–Tate Groups: with Applications to Abelian Schemes*, Lecture Notes in Mathematics **264**, Springer, 1972, [正式书籍 DOI](https://doi.org/10.1007/BFb0058301)，[原书全文](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/messing72.pdf)：Chapter V, §1, Theorem 1.6（printed p.151 起），Theorem 1.10，以及 §2, Theorem 2.1（printed p.159）。使用其 nilpotent-PD deformation functoriality 和 abelian/Barsotti–Tate 晶体相容；本文的 PD 环、有限水平递推及角色次数限制均另行明证。
- [R1191](R1191-original-half-rank-factor-all-primitive-inertia-slots.md)、[R1193](R1193-original-highest-primitive-packet-and-simple-Cauchy-CM-jet.md)、[R1196](R1196-original-highest-packet-Picard-log-and-finite-Cech-source.md)：同一实际 $C,\beta$、最高 packet、原有限 Picard log 与局部 gap 源。

全篇为纸面推导，无数学程序执行；不重做已登记有限窗口，不恢复未经证明的 PS 点类零性。root 亲读所引 Messing 原文，核准有限 PD 比较、target Frobenius 方向及未分歧系数范围；o2_high_coefficient 纸核反演、opposite 三角变换、次数界和两个 CM 节点常数。
