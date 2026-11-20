# R53. 从真实旧核心出发的材料曲率圆化同伦与正性域

维护：Astra-held10-1b6d88ec-20261120 / geometry_advance。

**已证明的核心层结构结论。** 本条在每个同伦参数上构造单位速度、严格凸、旋转闭合的平面核心，并给出完整参数变分和一个保留大曲率正余量的显式控制盒。它不证明前缀 BVP、真实非线性尾或整曲面可沿此路径求出，也不宣称绕过 R20 的完整线性核障碍。support 同伦适配器的草稿已写入源文件，但首次执行检查在创建进程前因环境断连失败；没有新的数值终态。此后保存的最终 support/provider 适配源仍未执行。

## 1. 原对象和不能混用的坐标

固定整数 $n\ge3$，$T=2\pi/n$、$L=T/2$。给定一条以原点为旋转中心、反射对称、严格凸的闭曲线 $\Gamma_0(u;p)$；$u$ 是周长为 $2\pi$ 的材料弧长，参数 $p$ 变化时该材料坐标和周长保持不变。假设其切线为

$$\partial_u\Gamma_0=i e^{i\phi_0(u;p)},\qquad \phi_0(0;p)=0,$$

且 $\phi_0(u+T;p)=\phi_0(u;p)+T$、$\phi_0(-u;p)=-\phi_0(u;p)$。于是 $\phi_0(L;p)=L$，曲率 $\kappa_0=\partial_u\phi_0>0$ 为偶、$T$ 周期函数。以下积分都在材料 $u$ 上，不能将原法向角的同名矩或有限投影系数代入。

采用 R52 的固定材料窗口 $\chi=1-W$，在 $|u-L|\le S$ 上为1，在 $|u-L|\ge S+b$ 上为0，其中 $0<S<S+b<L$。记

$$J=\int_0^T\chi(u)\,du=2S+b,\qquad m=J/T<1.$$

选一个正的目标圆弧曲率 $k(p)>0$。它可以是固定常数，也可以由原核心参数光滑决定，例如

$$k(p,\tau)=(1-\tau)\kappa_0(L;p)+\tau k_*,\qquad 0\le\tau\le1.$$

$\tau$ 和下面的圆化参数 $\lambda$ 是不同设计参数；它们都不同于旧 raw 核已有的同名圆化参数。实际记录必须分别命名。

## 2. 同一均值和材料圆弧

定义

$$
\beta(p)=\frac{\int_0^T\chi(u)\,[\kappa_0(u;p)-k(p)]\,du}{T-J},
$$

$$
\boxed{\kappa_\lambda
=\kappa_0+\lambda\chi(k-\kappa_0)+\lambda\beta W,\qquad 0\le\lambda\le1.}
\tag{1}
$$

由 $\int\kappa_0=T$ 和 $\beta$ 的定义，$\int_0^T\kappa_\lambda=T$ 严格成立。对称性也逐项保持。令

$$\phi_\lambda(u)=\int_0^u\kappa_\lambda(v)\,dv.$$

则 $\phi_\lambda(u+T)=\phi_\lambda(u)+T$，且反射性给 $\phi_\lambda(L)=L$。在 $\lambda=1$ 的保护弧上，

$$\phi_1(L+x)=L+kx,\qquad |x|\le S.$$

再按 R52 的旋转中心公式定义

$$
\Gamma_\lambda(u)=\frac{\int_0^T i e^{i\phi_\lambda(v)}\,dv}{e^{iT}-1}
+\int_0^u i e^{i\phi_\lambda(v)}\,dv.
\tag{2}
$$

只要 $\kappa_\lambda>0$，同一已证投影单调性论证使它为严格凸闭嵌入，单位速度和周长 $2\pi$ 均精确保留；$n$ 重旋转与两条反射轴也保持。在 $\lambda=0$，$\phi_\lambda=\phi_0$，而旋转闭合条件唯一决定积分常量，所以 $\Gamma_\lambda$ 就是原完整核心，不只是与其某些低矩相同。

在 $\lambda=1$，式 (2) 的保护段准确为

$$\Gamma_1(L+x)=O+\frac1k e^{i(L+kx)}.$$

因此所有 R52 的核心周长、圆心和条件换握持预算可以对这个新端点应用，但完整图的假设仍须分别支付。对 $0<\lambda<1$，保护段曲率是 $(1-\lambda)\kappa_0+\lambda k$，通常不恒定，不能提前用圆弧握持公式。

## 3. 正曲率不需要很小的同伦步长

设原核心的全角界为 $0<a\le\kappa_0\le b$。式 (1) 可写成

$$\kappa_\lambda=(1-\lambda)\kappa_0
+\lambda[\chi k+W(\kappa_0+\beta)].$$

因此对整个 $[0,1]$ 有

$$
(1-\lambda)a+\lambda\min(k,a+\beta)
\le\kappa_\lambda\le
(1-\lambda)b+\lambda\max(k,b+\beta).
\tag{3}
$$

特别地，若

$$0<k\le \frac{\int_0^T\chi\kappa_0}{J},$$

则 $\beta\ge0$，故 $\kappa_\lambda\ge\min(a,k)>0$。一个更易核验的充分条件是 $0<k\le\min\kappa_0$；此时

$$
\boxed{\kappa_\lambda\ge k,\qquad
\kappa_\lambda\le b+(b-k)\frac{m}{1-m}.}
\tag{4}
$$

上界使用 $0\le\beta\le(b-k)m/(1-m)$。这是核心的全材料角结论，不依赖有限采样或 BVP 参数步长。实际 Newton 参数离开已付正性条件时，仍须检查新的完整曲率，不能把 (4) 当成全参数空间的许可。

若原参数族和窗口具有所需连续导数且在一个紧参数集上保持上述正下界，则 (1)、(2) 连续依赖所有参数于相应 $C^2$ 拓扑；求积是在有限区间上的固定定义。这不推出解过渡区边值问题的连续族存在。

## 4. 一个明确的三重 support 控制盒

这里是一个独立声明的参数盒；它不声称已恢复丢失的任何大数组或重新得到旧 BVP。取原支撑函数

$$h(\phi)=1+q\cos(3\phi)+\sum_{j=2}^8c_j\cos(3j\phi),\qquad q\in[.0599,.0601],$$

并要求相应系数满足精确十进制上界：

| j | $|c_j|$ 的上界 |
|---:|---:|
| 2 | .000465 |
| 3 | .0000377 |
| 4 | .000000645 |
| 5 | .000000173 |
| 6 | .0000000923 |
| 7 | .00000000593 |
| 8 | .000000000769 |

令 $\rho=h+h''$。精确有理相加给

$$\sum_{j=2}^8(9j^2-1)|c_j|\le.019454851275,$$

所以

$$.499745148725\le\rho\le1.500254851275.$$

又在 $0<\phi<\pi/3$，令 $x=3\phi\in(0,\pi)$。恒等式
$\sin(jx)/\sin x=\sum_{r=0}^{j-1}e^{i(j-1-2r)x}$ 给
$|\sin(jx)|\le j\sin x$。因此

$$
\rho'(\phi)\ge3\sin(3\phi)
\left[8q-\sum_{j=2}^8j^2(9j^2-1)|c_j|\right]>0,
$$

因为右端系数上界的精确和为 $.0959179744<.096$，而 $8q\ge.4792$。故 $\rho$ 在该半扇区严格上升，最大值在 $\phi=L$。材料角的反射和均值给对应材料点也为 $u=L$，于是

$$\kappa_0(L)=\min\kappa_0\ge1/1.500254851275>.2.$$

现在取

$$k=(1-\tau)\kappa_0(L)+\tau/5,\qquad (\lambda,\tau)\in[0,1]^2.$$

对盒内每个原核心及整个设计方形，(4) 给

$$\boxed{\kappa_\lambda\ge1/5.}\tag{5}$$

此盒可以在未来真实保存的 scalar 参数上直接核验，但在没有实际终态前，不把“盒中的核心存在”升级成“盒中的 BVP 已求出”。固定旧控制所得的正性也不允许未来联立求解不经检查地越盒。

## 5. 完整材料参数变分

令下标 $j$ 表示对实际参数 $p_j$ 的导数，窗口保持固定。由定义直接得到

$$
\beta_j=\frac{\int_0^T\chi(\kappa_{0,j}-k_j)}{T-J},\qquad
\kappa_{\lambda,j}=(1-\lambda\chi)\kappa_{0,j}
+\lambda\chi k_j+\lambda W\beta_j,
$$

$$
\phi_{\lambda,j}(u)=\phi_{0,j}(u)
+\lambda\int_0^u[\chi(k_j-\kappa_{0,j})+W\beta_j]\,dv.
\tag{6}
$$

固定 $k_*$ 的混合路径中 $k_j=(1-\tau)\kappa_{0,j}(L)$。式 (6) 的全周期积分为零，所以参数变分没有引入扭转或改变材料总长。

令 $\nu_\lambda=e^{i\phi_\lambda}$。完整三个位置参数 jet 为

$$
\Gamma_{\lambda,j}(u)=
\frac{-\int_0^T\nu_\lambda\phi_{\lambda,j}}{e^{iT}-1}
-\int_0^u\nu_\lambda\phi_{\lambda,j},
$$

$$
\partial_j\Gamma_\lambda'=-\nu_\lambda\phi_{\lambda,j},\qquad
\partial_j\Gamma_\lambda''
=-\nu_\lambda(\kappa_{\lambda,j}+i\kappa_\lambda\phi_{\lambda,j}).
\tag{7}
$$

### 5.1 原核确为有限 support Fourier 核时

若 $h=1+\sum a_j\cos(m_j\phi)$、$m_j=nj$，则

$$u=\phi+\sum_j\frac{1-m_j^2}{m_j}a_j\sin(m_j\phi),\qquad \rho=h+h''.$$

固定材料 $u$ 求导给

$$
\phi_{0,j}=-\frac{(1-m_j^2)\sin(m_j\phi)}{m_j\rho},\qquad
\kappa_{0,j}=-\frac{(1-m_j^2)\cos(m_j\phi)+\rho_\phi\phi_{0,j}}{\rho^2}.
\tag{8}
$$

这支付了 moving normal angle。原材料导数也有

$$\kappa_{0,u}=-\rho_\phi/\rho^3,\qquad
\kappa_{0,uu}=-\rho_{\phi\phi}/\rho^4+3\rho_\phi^2/\rho^5.$$

### 5.2 任意真实旧 core provider

不能把 raw core 的某个 coefficients/frequencies 标签当成 (8) 的 support 定义。若已有 provider 返回真实 $F_u=T$、$F_{uu}$ 以及参数三jet，置外法向 $\nu=(T_y,-T_x,0)$，则单位速度给

$$\phi_{0,j}=-\partial_jF_u\cdot\nu,\qquad
\kappa_{0,j}=-\partial_jF_{uu}\cdot\nu.$$

第二式中遗漏的潜在项为 $F_{uu}\cdot\partial_j\nu$；因 $F_{uu}=-\kappa_0\nu$ 且 $\nu\cdot\partial_j\nu=0$，它确实为零。若 provider 还给真实材料 $\rho,\rho_u,\rho_{uu}$，则

$$\kappa_{0,u}=-\rho_u/\rho^2,\qquad
\kappa_{0,uu}=2\rho_u^2/\rho^3-\rho_{uu}/\rho^2.$$

这才是 n4 旧 raw 核可用的通用接口。解析公式的身份不代表某个特定 provider、缓存、求积或链式缩放已经实际接通。

## 6. 源码与执行边界

scripts/resume_transfer/material_flattened_support_core.py 已实现 (1)、(2)、(6)–(8)，专门适配原 PlanarSupportCore。默认先取 $\tau=0$，使目标圆弧曲率等于旧核心中心曲率；$\lambda=1$ 后可独立增大 $\tau$，避免把圆化和大幅降曲率强行放在同一个参数内。

其 make_factory(reference, settings) 在 $\lambda=0$ 直接返回原 reference 实例，不重新积分近似它；$\lambda>0$ 是新材料曲率核心。目标正性用 (3)，必要时用全角二阶导数界与节点插值余项作数值域守卫。该守卫的浮点评价不等同 outward 区间证书。

原型中的 _support_fields 使用 (8)，不能直接接旧 raw 核；后者须采用第5.2节的真实 provider 适配。相应 material_flattened_generic_core.py 以实例级回调接入显式的 parameter-jets 与 rho-jets provider，不改运行中原模块的全局函数；若粗正性界不足而没有真实材料曲率导数上界，则拒绝，绝不假造 support 频率公式的界。

首次准备进行 lambda0身份、圆弧和三jet差分检查时，执行工具在创建进程之前报 exec-server transport disconnected；没有 session ID、退出码或数值输出。随后环境明确 unavailable。本条不声称这些实现检查完成，也不声称任何新 BVP 已运行。通用适配器的源码是在不可执行期间保存，仍须先实际验证它自己的参数身份、解析 jet 与正性域。

该同伦可在核心层保留旧较大幅度的真实形状和参数语义，但仍会改变真实核心与完整参考 lift，属于设计。它没有证明原精确等距问题的解集含有这条路径，没有给完整线性核或 Jacobian 逆界，也不使“有限接受”自动成为 README 所需固定全部物理参数的收敛链。
