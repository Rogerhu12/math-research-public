# R53 补充：真实旧控制盒内的圆化步长有多大

维护：Astra-held10-1b6d88ec-20261120 / geometry_advance。
日期：2026-11-20。

这是 R53 同伦的核心层定量推论，不是新的前缀 BVP 终态。以下严格界不使用后来运行的核接口测试来代替证明。特别地，2026-11-20 的 Actions 序列在旧 H8 入口处失败，尚未运行材料圆化参数 lambda 的任何 BVP；不能将该旧入口失败归于本条的 lambda 方向。

## 1. 任意真实旧核心的相位与位置变化界

沿用 R53 的周期 T=2pi/n、半周期 L、固定材料窗 chi=1-W，以及同伦曲率

    kappa_lambda = kappa_old + lambda [chi (k-kappa_old) + beta W].

在以材料中心为原点的右半周期 x∈[0,L]，设

$$
A_{\rm abs}=\int_0^L \chi(L+x)\,|\kappa_0(L+x)-k|\,dx.
$$

该积分实际只到 S+b。令

$$f(x)=\chi(L+x)(k-\kappa_0(L+x))+\beta W(L+x).$$

反射性和整周期的零曲率增量给 int_0^L f=0。又有

$$
\int_0^L|f|
\le A_{\rm abs}+|\beta|\int_0^L W
=A_{\rm abs}+\left|\int_0^L\chi(k-\kappa_0)\right|
\le2A_{\rm abs}.
$$

对任意 x，一方面 primitive 是 int_0^x f，另一方面它等于 -int_x^L f，所以

$$
\left|\int_0^x f\right|
\le\min\!\left(\int_0^x|f|,\int_x^L|f|\right)
\le A_{\rm abs}.
$$

用反射扩展到全周期，得到

$$
\boxed{\|\phi_\lambda-\phi_0\|_\infty\le\lambda A_{\rm abs}.}
\tag{A}
$$

这个绝对值版本不要求旧中心是全局曲率最小点，因而也适用于真实 raw provider。需要的仍是 R53 的真实材料坐标、反射/旋转规范与曲率均值，不能用有限投影的系数替代这些对象。

记

$$K_n=\frac{\pi}{n\sin(\pi/n)},\qquad
\eta=\min(\lambda A_{\rm abs},\pi).$$

两条曲线的切线差满足 norm(Delta Gamma_u)≤2 sin(eta/2)。而二者同心 n 重旋转给

$$(e^{iT}-1)\Delta\Gamma(u)
=\int_u^{u+T}\Delta\Gamma_u(v)\,dv.$$

因此

$$
\boxed{\|\Gamma_\lambda-\Gamma_0\|_\infty
\le2K_n\sin(\eta/2)
\le K_n\min(\lambda A_{\rm abs},2).}
\tag{B}
$$

这是同一材料配对的 C0 距离上界，也给两个核心像的 Hausdorff 上界；它不是完整曲面的 held Hausdorff 下界。其方向和 R52 的可见运动见证相反，不能混用。

若 k≤min kappa_old，则 integrand 不变号，A_abs=A:=int chi(kappa_old-k)，并有 beta=A/(L-S-b/2)。这是下面三重控制盒的情况。

## 2. R53 三重控制盒的严格局部曲率界

这里固定 R53 §4 所声明的整个 support 参数盒，取 S=21/100、b=1/4，先令 curvature_blend=tau=0，即 k=kappa_old(L)。所有控制均仍在该盒内；本节不假定任何 Newton 迭代自动守盒。

令旧法向角 phi=L+v、旧材料角 u=L+x。R53 已证明 rho 在中心最大。由其精确系数和，

$$
\rho(L)\ge1+8(.0599)-.019454851275
=1.459745148725>\frac{729}{500}=:B,
$$

$$
\|\rho_{\phi\phi}\|_\infty
\le9[8(.0601)+.0959179744]
=5.1904617696<\frac{26}{5}=:D.
$$

rho_phi(L)=0，故 Taylor 积分余项给

$$\rho(L+v)\ge B-\frac D2v^2,\qquad
x=\int_0^v\rho(L+t)\,dt\ge Bv-\frac D6v^3.$$

在 v=17/50=.34 处，

$$Bv-\frac D6v^3
=\frac{432803}{937500}
=.461656533\ldots > S+b=.46.$$

因为真实 x(v) 严格增加，所以整个材料窗口 0≤x≤.46 对应 0≤v<.34。于是该窗口内

$$
\rho(L+v)>B-\frac D2(.34)^2
=\frac{3617}{3125}=1.15744>\frac{23}{20}=:r,
$$

并有 x≥rv。另一方面 rho(L)-rho(L+v)≤Dv^2/2，因此

$$
0\le\kappa_0(L+x)-\kappa_0(L)
\le\frac{D v^2}{2rB}
\le\frac{D x^2}{2r^3B}
=\frac{10400000}{8869743}x^2
<\frac65x^2.
\tag{C}
$$

这一段使用完整系数盒和真实材料逆图，未以“纯 q 曲线近似”替代控制的影响。

## 3. 精确材料窗矩和 C2 步长

R52 窗的 P'(t)=630t^4(1-t)^4。分部积分给

$$
\int_0^{S+b}\chi(L+x)x^2\,dx
=\frac13\int_0^1(S+bt)^3P'(t)\,dt.
$$

用该多项式的前三个矩 1/2、3/11、7/44 得

$$
J_2=\frac13\left[S^3+\frac32S^2b+\frac9{11}Sb^2+
\frac7{44}b^3\right]
=\frac{1717009}{132000000}<\frac1{75}.
$$

由 (C)，

$$
0\le A<\frac65J_2
=\frac{1717009}{110000000}
=.0156091727\ldots<\frac2{125}=.016.
\tag{D}
$$

此外，pi>3 给 L>1，故 beta=A/(L-.335)<16/665。旧盒给 kappa_old<201/100；所以整个 tau=0、lambda∈[0,1] 的核心还满足

$$
\kappa_\lambda<\frac{201}{100}+\frac{16}{665}<2.035.
$$

为控制二阶位置导数，先利用窗的对称性：x≤.335 时 chi≤1；x≥.335 时 chi≤1/2。于是

$$
\chi x^2\le\max(.335^2,\tfrac12(.46)^2)=.112225.
$$

结合 (C) 和 beta<16/665，

$$
|\chi(k-\kappa_0)+\beta W|
\le\max(\chi(\kappa_0-k),\beta)<.13467.
\tag{E}
$$

这里左端是两个非负项的差，因此用 max，不能无故换成一个更小的有符号平均。由 Gamma_uu=-kappa nu、(A)、(D)、(E)，

$$
\|\Gamma_{\lambda,uu}-\Gamma_{0,uu}\|_\infty
\le\lambda(.13467)+\frac{201}{100}(.016\lambda)
<.16683\lambda.
$$

最后 K_3=2pi/(3sqrt3)<1.21；可直接使用 R52 已给的 pi<22/7、sqrt3>433/250 验证。由 (A)、(B)：

$$
\boxed{
\begin{aligned}
\|\Gamma_\lambda-\Gamma_0\|_\infty&<.01936\lambda,\\
\|\Gamma_{\lambda,u}-\Gamma_{0,u}\|_\infty&<.016\lambda,\\
\|\Gamma_{\lambda,uu}-\Gamma_{0,uu}\|_\infty&<.16683\lambda.
\end{aligned}}
\tag{F}
$$

特别地，在计划的第一步 lambda=.02 上，三个严格上界依次为

    .0003872, .00032, .0033366.

这些是连续、全材料角、完整旧控制盒上的核心变化预算，不是采样误差，也不是 BVP Newton 残差。它们不提供前缀 BVP Jacobian 的逆界；一个很小的真实核心改变也可能不沿边值解集。因此未来若材料 lambda 的实际联立求解失败，应按其真实门、残差和尾来记录，不能由 (F) 宣称本来必应成功。

## 4. 整个 lambda/tau 方形的核心曲率上界

R53 给 min kappa_old>.5、max kappa_old<201/100，以及 k=(1-tau)kappa_old(L)+tau/5≤min kappa_old。故核心曲率下界为 1/5。

又 J=2S+b=.67、T>2，所以 J/(T-J)<67/133，因而

$$
0\le\beta
<\frac{67}{133}\left(\frac{201}{100}-\frac15\right)
=\frac{12127}{13300}.
$$

R53 的曲率混合公式随即给整个设计方形

$$
\boxed{\frac15\le\kappa_\lambda<\frac{1943}{665}<3.}
\tag{G}
$$

这支付的是平面核心以及它的直柱部分的局部主曲率；过渡区、完整嵌入、全像直径和 reach 均仍须分别证明。不能把 (G) 直接当整曲面曲率证书。

## 5. 仅作设计诊断的独立浮点数

另用当前可执行的 JavaScript 进行纯 q support 曲线的材料反演与 20000 小段 Simpson 积分，得到下面数值。这部分不声称 outward 区间包围，也不代替上面的精确有理证明；所用控制均为零，不是待恢复 BVP 的实际系数。

| n | q | S,b | tau | A | beta | lambda=.02 的核心 C0 上界估计 |
|---:|---:|---|---:|---:|---:|---:|
| 3 | .06 | .21,.25 | 0 | .00620960264358 | .00871893287635 | .000150172977598 |
| 3 | .06 | .21,.25 | 1 | .16556095399494 | .23246493015424 | .00400392287882 |
| 4 | .03 | .20,.25 | 0 | .01070129978884 | .02324357619037 | .000237723110786 |
| 4 | .03 | .20,.25 | 1 | .16983923082332 | .36889641255302 | .00377287729044 |

tau=0 先圆化再降目标曲率有较小的核心扰动，但这里没有证明相应过渡区解能跟随。真实 raw 核可用第1节的 A_abs；除非先核实，不应声称其中心仍为全局曲率最小值。

## 状态边界

上面严格十进制和分数已用 BigInt 精确四则算术复核；证明不依赖 Python 环境。R53 两个实际实现及其四项核接口检查后来已在独立 Actions 运行通过，相关实测与哈希由主记录另列，不在这里制造新的 BVP 终态。本补充没有更改正在使用的源文件或物理模型参数。
