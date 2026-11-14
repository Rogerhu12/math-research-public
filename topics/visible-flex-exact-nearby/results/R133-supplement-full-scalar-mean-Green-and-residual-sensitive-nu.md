# R133 补篇：完整均值的标量 Green、真实 residual 与 ν 参考消去

2026-11-14。**准确全频恒等式和实际两端比例预算已证明，23 个精确有理门已执行。**
把 $m=\langle v\rangle_\phi<0$ 改为 $n=a^2/m^2$，使给定完整非mean场之后的
mean 方程成为一维线性方程。此变换不消去 mean，不要求 $K$ 保持某个符号，
也不除 $\sqrt{|K|}$。本篇完整保留近似中心的 residual、真实 PPoly 跳、
normalized 参数列和独立外帽 mean。

中心是同一完整 final moving ac1：
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413。
本篇没有执行尚未恢复的全径向积分或 mean 跳求和，
因此最后的指数因子仍是待付的明确量；不能把所列小端点比例当成已完成的
整体逆常数。

## 1. 全 nonlinear mean 的准确标量化

在实际四重反射空间令

$$
 m=\langle v\rangle,\quad \widetilde v=v-m,\quad
 \mathcal V=\langle u^2\rangle+K\langle\widetilde v^2\rangle,
 \qquad n=\frac{a^2}{m^2},\qquad \tau=-\frac{2a^2}{m^3}>0.          \tag{Q.1}
$$

$\mathcal V$ 是带符号的二次量，负曲率区不能把它误当非负。
准确 moving 方程的 mean 是

$$
 m'=\beta m(1-\langle u^2+Kv^2\rangle)
     =\beta m(1-\mathcal V-Km^2),\qquad \beta=a'/a .
$$

直接微分 (Q.1) 得

$$
 \boxed{n'=2\beta\mathcal V\,n+2\beta K a^2.}             \tag{Q.2}
$$

对给定的完整 $u,\widetilde v$，这是真线性 forced scalar 方程；
整个 coupled PDE 并未因此变为线性。选定真实 $m<0$ 分支后可准确恢复
$m=-a/\sqrt n$，没有丢失偶 mean 或新加另一个符号自由度。

真实旋转参考 $s=1/C_{\rm ref}$ 满足
$s'=\beta s(1-Ks^2)$。令

$$
 n_{\rm ref}=\frac{a^2}{s^2}
       =1-\frac{a'^2}{E_\nu},\qquad
 n_{\rm ref}'=2\beta K a^2.                             \tag{Q.3}
$$

因此 $e=n-n_{\rm ref}$ 的准确方程是
$e'=2\beta\mathcal V(e+n_{\rm ref})$。
这一等式保留全部非mean反馈；没有设置 $e=0$。

## 2. 任意近似中心：真实 mean residual 必须保留

现在令 $u,v$ 是任意实际保存的分片中心，其真实径向 jet 不一定满足 PDE。
定义

$$
 R_0=m'-\beta m(1-\mathcal V-Km^2),\qquad c=2\beta\mathcal V .
                                                               \tag{Q.4}
$$

每个真实片内准确有

$$
 n'-cn-2\beta Ka^2=\tau R_0.                            \tag{Q.5}
$$

故不能对近似中心直接使用无源 (Q.2)。
在 actual normalized 表示
$m=s+\alpha V_0$ 中，可避免大背景的无关区间减法：

$$
 \boxed{R_0=
 \alpha V_0'-\beta\alpha V_0
        [1-K(m^2+ms+s^2)]+\beta m\mathcal V.}            \tag{Q.6}
$$

这里 $V_0'$ 是保存的真实多项式导数；只对**精确旋转参考**使用 (Q.3)
中的恒等式，没有把有限中心的径向导数替换成 PDE。

对完整 $M$ 模 moving 中心，正交性给

$$
 \mathcal V=\frac{\alpha^2}{2}
       \sum_{j=1}^{M}(U_j^2+K V_j^2).                 \tag{Q.7}
$$

因此 $c,R_0$ 的真正闭盒计算只需要原完整径向系数、mean 和实际目标；
不需要角采样，也不需要反演物理角。未知方向仍有全部 Fourier 模；
(Q.7) 只计算当前有限中心的准确系数。

## 3. 完整线性 mean，含 residual 与参数源

写 $h=(\xi,\zeta)$、$z=\langle\zeta\rangle$、
$\widetilde\zeta=\zeta-z$。若完整线性化方程是

$$
 \mathcal D h=(\partial_\nu F)\delta\nu+f,
$$

则真实第二 mean 为

$$
 z'=\beta(1-\langle u^2+Kv^2\rangle)z
 -2\beta m\langle u\xi+Kv\zeta\rangle
 -\beta m\dot K\langle v^2\rangle\delta\nu+\langle f_2\rangle,
 \qquad \dot K=\partial_\nu K.                         \tag{Q.8}
$$

特别保留了原 nonlinear primitive 所产生的 mean。
设

$$
 y=\tau z,\qquad
 \widetilde c=c-\frac{3R_0}{m}.
$$

对 (Q.5) 真正线性化，等价地直接将 (Q.8) 代入 $y'$，得

$$
 \boxed{\begin{aligned}
 y'={}&\widetilde c\,y
   +4\beta n\langle u\xi+K\widetilde v\widetilde\zeta\rangle\\
 &+2\beta\dot K\bigl(n\langle\widetilde v^2\rangle+a^2\bigr)\delta\nu
   +\tau\langle f_2\rangle .
 \end{aligned}}                                                    \tag{Q.9}
$$

$-3R_0/m$ 是准确 residual-sensitive 修正，不能删除。
在真解中心 $R_0=0$ 时才剩下只含 nonmean 二次量的对角 $c$。

原直接 mean 对角
$c_m=\beta(1-\langle u^2+Kv^2\rangle-2Km^2)$ 与新对角的关系为

$$
 \widetilde c-c_m=\frac{\tau'}{\tau}
                  =2\beta-\frac{3m'}m .                \tag{Q.10}
$$

这个恒等式不要求 $R_0=0$，可独立核对 (Q.9) 的全部符号。

## 4. ν 的大径向 mean 源准确消去

原控制函数 $w$ 及目标仍为
$E_\nu=E e^{\nu w}$。定义

$$
 \rho=\frac{a'^2}{E_\nu}=1-n_{\rm ref}.
$$

因 $a,\beta$ 不随 $\nu$ 变化，

$$
 \partial_\nu n_{\rm ref}=\rho w,\qquad
 (\rho w)'=2\beta a^2\dot K,\qquad
 \dot K=-Kw+\frac{\beta}{2E_\nu}w'.                    \tag{Q.11}
$$

第二式也可直接由
$\rho'=-2\beta Ka^2$ 和
$2\beta a^2(\beta/(2E_\nu))=\rho$ 验证。

令 $\delta\nu$ 为固定标量，
$Y=y-\rho w\delta\nu$。则 (Q.9) 变为

$$
 \boxed{\begin{aligned}
 Y'={}&\widetilde c\,Y
   +4\beta n\langle u\xi+K\widetilde v\widetilde\zeta\rangle
   +\tau\langle f_2\rangle\\
 &+\left[\widetilde c\,\rho w
          +2\beta n\langle\widetilde v^2\rangle\dot K\right]\delta\nu .
 \end{aligned}}                                                    \tag{Q.12}
$$

单独的 $2\beta a^2\dot K$ 源准确消去。
除已明确保留的 $R_0$ 费用外，剩余参数源都含 nonmean 的二次背景。
这不是把整个 mean 源设零。

两个控制端点和腰、$R=25/8$ 处 $w=0$，所以那里 $Y=y$。
actual normalized $u=\alpha U,v=s+\alpha V$ 的显式参考列也可准确写成

$$
 \partial_\nu(n-n_{\rm ref})\big|_{U,V,\alpha}
       =\rho\bigl[(s/m)^3-1\bigr]w.                   \tag{Q.13}
$$

因为 $\partial_\nu s=-s(a')^2 w/[2(E_\nu-a'^2)]$。
只有 $m=s$ 时 (Q.13) 才为零；当前候选的真实 $V_0$ 没有被删除。

## 5. 所有 PPoly 接口：乘法跳和转换后的参数跳

记右值减左值为 $[m]_i$。真实 $a$ 在接缝连续，故中心的完整 nonlinear 跳为

$$
 [n]_i=-\frac{a_i^2[m]_i(m_i^++m_i^-)}
                         {(m_i^+)^2(m_i^-)^2}.         \tag{Q.14}
$$

若线性方向有实际 additive mean jump $[z]_i=j_i$，则

$$
 y_i^+=\frac{\tau_i^+}{\tau_i^-}y_i^-+\tau_i^+j_i,
 \qquad
 \frac{\tau_i^+}{\tau_i^-}
                  =\left(\frac{m_i^-}{m_i^+}\right)^3>0.          \tag{Q.15}
$$

即使当前 $\nu$ response 自身连续（$j_i=0$），有限中心的 mean 跳也会
在 $y$ 中产生乘法接口，不能默认这个比值为1。

$Y=y-\rho w\delta\nu$ 的接口为

$$
 Y_i^+=\frac{\tau_i^+}{\tau_i^-}Y_i^-
  +\left(\frac{\tau_i^+}{\tau_i^-}-1\right)
                           \rho_iw_i\delta\nu+\tau_i^+j_i .       \tag{Q.16}
$$

这条额外参数接口源必须保留。
$\rho,w$ 来自真连续目标，所以上式没有虚构的目标跳。
候选实际 $[m]_i=\alpha[V_0]_i$ 是准确 dyadic 差，可直接计算。

## 6. 后向 Green 与完整源/端口

对 $r<t$，原 mean 的 homogeneous 后向 Green 为

$$
 \boxed{H(r,t)=
 \left(\frac{a(t)}{a(r)}\right)^2
 \left(\frac{m(r)}{m(t)}\right)^3
 \exp\left(-\int_r^t\widetilde c(s)\,ds\right)
 \prod_{r<r_i<t}\left(\frac{m_i^+}{m_i^-}\right)^3.}     \tag{Q.17}
$$

端点在接缝时选一致单侧；完整表达式在原 $z$ 变量下不依赖这个选择。
(Q.10) 与 (Q.15) 证明它准确等于
$\exp(-\int_r^t c_m)$，并没有改变原方程。
改写的意义是把大背景放到可直接支付的端点比，
径向积分只保 nonmean 二次量、真实 residual 和准确接口。

若 $g$ 为 (Q.8) 除 $c_mz$ 外的全部项，则

$$
 z(r)=H(r,R)z(R)-\int_r^R H(r,t)g(t)\,dt
                           -\sum_{r<r_i<R}H(r,r_i)j_i.           \tag{Q.18}
$$

$g$ 包含全部 nonmean、$\nu$、普通 mean source。
也可直接使用 (Q.12)、(Q.16) 的较好参数源；两种形式完全等价。

每个接口都满足

$$
 \left|\log\left|\frac{m_i^+}{m_i^-}\right|\right|
 \le\frac{|[m]_i|}{\min(|m_i^+|,|m_i^-|)} .
$$

故定义实际待付的

$$
 I_-=\int_0^R(-\widetilde c)_+\,dr,\qquad
 J_m=3\sum_i\frac{|[m]_i|}
                    {\min(|m_i^+|,|m_i^-|)},\qquad
 \Gamma=\exp(I_-+J_m),                                 \tag{Q.19}
$$

便同时控制全部后向子区间的指数/乘法费用。
未完成这两个完整量之前，不把 $\Gamma$ 设为1。
原连续内蕴接缝和全部 candidate joins 都应在闭覆盖中核对。

外物理 mean 的准确微分是

$$
 \delta C_0(R)=-z(R)/m(R)^2,\qquad
 y(R)=\frac{2a(R)^2}{m(R)}\,\delta C_0(R).               \tag{Q.20}
$$

这是独立外帽 mean 行，仍须联立真 $D_Zc_0$ 和 $D_{f_B}c_0$。
整体高度平移另行保留；曲率 mean 不是高度常数。
腰 $z(0)=0$ 也不能在尚未完成周期帽/全迹匹配前免费设定。

## 7. 最终实际两端比例：可重算的23门预算

同一[完整腰坐标证书](R133-supplement-final-waist-amplitude-coordinate-and-mean-Schur.md)
给 whole-$\eta$ 上
$a(0)>1.06873282$、$|m(0)|<1.068733840999993869<1.07$。
[实际最终外端](R133-supplement-final-moving-centre-actual-regular-boundary.md)
与同一未改 long 入口给 $a(R)<7\cdot10^{-6}$、$|m(R)|>5.8$。
因此 (Q.17) 从 $R$ 到腰的端点比例严格小于

$$
 \left(\frac{7\,10^{-6}}{1.06873282}\right)^2
                  \left(\frac{1.07}{5.8}\right)^3
 <2.693551\,10^{-13}.                                 \tag{Q.21}
$$

将 (Q.20) 一次性代入后，外物理 $\delta C_0$ 到腰 $z$ 的比例是

$$
 \frac{a(R)^2|m(0)|^3}{a(0)^2|m(R)|}
 <9.061105\,10^{-12}.                                 \tag{Q.22}
$$

两个式子都还须乘 $\Gamma$。不能因外端 $a$ 小就漏掉 (Q.19)。

真实小球的 nonlinear 外 mean 导数已经给
$L_0<7.372818\,10^{-7}$、
$L_{0B}<8.1920198958\,10^{-8}$。所以其 homogeneous 外输入贡献有

$$
 |z(0)|_{\mathrm{outer}}
 <\Gamma\left(
 6.680588\,10^{-18}\|\delta Z\|_{L^2_\theta}
 +7.422875\,10^{-19}\|\delta f_B\|_{\dot H^2}
 +9.061105\,10^{-12}|g_{\rm mean,R}|\right).             \tag{Q.23}
$$

这不是完整 response 界；(Q.18) 的体源、参数项和 jumps 仍须加入。
$f_B$ 是独立数据，真实 far label 方程仍保留。

源
[scripts/fourfold_codazzi_scalar_mean_budget.mjs](../scripts/fourfold_codazzi_scalar_mean_budget.mjs)
与[23门精确报告](../notes/2026-11-14-R133-scalar-mean-green-rational.json)
使用 BigInt 有理数；同一函数已在可用 V8 实际执行。
人工一致 scalar jets 核对 (Q.5)、(Q.9)、(Q.10)–(Q.16)，非零
$R_0$ 和非零 mean 均保留；实际 endpoint 预算只消费上述同中心已付数据。
这些代数核对不是全径向 native，也不宣称完整 $\nu$ Schur 或主体逆已经完成。
