# R133：随解曲率角中的完整物理边界矩、变分与全部尾

**已证明。** 本文把已证的
[完整随解曲率角](R133-supplement-exact-moving-curvature-chart-and-mean-energy.md)
直接接到原物理角的全部边界行。公式包含真平均、所有非零模、参数列和
完整变角尾；不需要先在每个物理角点求逆角。本文不宣称实际非线性边界
方程已解，也不把角积分的浮点梯形值当作精确 Fourier 系数。

## 1. 坐标与全部物理矩

用 $P=\pi/2$ 表示四重周期，$\langle f\rangle=P^{-1}\int_0^P f$。
令 $u(\phi)$ 为实奇函数、$v(\phi)<0$ 为实偶函数，

$$m=\langle v\rangle<0,\qquad
 I=\partial_\phi^{-1}(1-\langle\cdot\rangle),\qquad
 \theta(\phi)=\phi+\frac{I(v-m)}m.                    \tag{B.1}$$

$I$ 取零平均 primitive；偶输入的 primitive 为奇函数，故
$\theta(0)=0$，且 $\theta_\phi=v/m>0$、
$\theta(\phi+P)=\theta(\phi)+P$。因此这是整个实角圆的度1微分同胚。
原物理场由

$$B(\theta(\phi))=u(\phi)/v(\phi),\qquad
 C(\theta(\phi))=1/v(\phi)                              \tag{B.2}$$

定义。对每个 $k\in4\mathbb Z$，以物理角定义复 Fourier 系数，真实换元给

$$\boxed{\widehat C_k^\theta=\frac1m
             \langle e^{-ik\theta(\phi)}\rangle_\phi,\qquad
 \widehat B_k^\theta=\frac1m
             \langle u(\phi)e^{-ik\theta(\phi)}\rangle_\phi.}
                                                               \tag{B.3}$$

证明是将 $d\theta=(v/m)d\phi$ 代入全部原物理积分，恰好抵消 (B.2)
中的分母。没有频率投影或近似。这也证明

$$\langle C\rangle_\theta=1/m,\qquad
 \langle B\rangle_\theta=\langle u\rangle_\phi/m=0.        \tag{B.4}$$

若暂不施加奇偶性，则第二个平均仍是 $\langle u\rangle/m$，不能删掉。
在当前反射类，$\theta$ 奇，故 $B$ 奇、$C$ 偶；对 $j\ge1$、$k=4j$，
实正弦、余弦系数分别为

$$B_j^{\sin}=\frac2m\langle u\sin(k\theta)\rangle,\qquad
 C_j^{\cos}=\frac2m\langle\cos(k\theta)\rangle.             \tag{B.5}$$

所以原帽的每一真实物理行 $B_j^{\sin}+q_{4j}C_j^{\cos}$ 都直接由
(B.5) 计算。$q_{4j}$ 仍是原物理角的实际帽系数，未将其替换成曲率角
上的 Fourier 乘子。非线性帽余项、独立 $f_B$、mean及所有未保留行仍按
原完整帽图消费。

## 2. 完整 Fréchet 变分及平均行

固定反射归一，令 $h=(h_1,h_2)=(\delta u,\delta v)$，
$z=\langle h_2\rangle=\delta m$。对 (B.1) 直接微分得

$$\delta\theta=\frac1m I\left(h_2-\frac zmv\right).
                                                               \tag{B.6}$$

括号的真平均恰为零。它含全部 $h_2$，不是只允许零平均变分的公式。
对 (B.3) 在同一个 $\phi$ 积分域微分，得到

$$\begin{aligned}
 \delta\widehat C_k^\theta
 &=-\frac zm\widehat C_k^\theta
       -\frac{ik}{m}\langle e^{-ik\theta}\delta\theta\rangle,\\
 \delta\widehat B_k^\theta
 &=-\frac zm\widehat B_k^\theta
       +\frac1m\langle e^{-ik\theta}(h_1-iku\delta\theta)\rangle.
\end{aligned}                                                   \tag{B.7}$$

尤其 $\delta C_0=-z/m^2$；当前奇偶类 $\delta B_0=0$。若将 $z$ 删除，
(B.7) 的 prefactor 项和逆角变分都错误。这些式子在例如完整 $A_\sigma$
场的开集中逐项合法：实圆上 $v/m$ 有严格正下界、$m\ne0$，实逆角和
有限积分对场光滑依赖。下面的解析估计同时给全频导数的可求和界。

对于实际规范化 $u=\alpha U$、$v=s+\alpha V$、$s=1/C_{\rm ref}$，
固定 $\alpha>0$，有

$$m=s+\alpha V_0,\qquad
 b=B/\alpha,\quad c=(C-C_{\rm ref})/\alpha,$$
$$b_j^{\sin}=\frac2m\langle U\sin(4j\theta)\rangle,\qquad
 c_j^{\cos}=\frac{2}{\alpha m}\langle\cos(4j\theta)\rangle,
 \quad j\ge1,$$
$$\boxed{c_0=-\frac{C_{\rm ref}V_0}{m}.}                  \tag{B.8}$$

因此诊断边界条件 $c_0=0$ 与 $V_0=0$ **准确等价**，不是扔掉 mean。
实际真帽若给非零 mean 关系，则仍使用 (B.8) 联立该关系，不能把它
擅自改成零。全部规范化变分及度量参数列只需在 (B.6)–(B.7) 代入

$$h_1=\alpha\delta U,\qquad
 h_2=\alpha\delta V+s_\nu\delta\nu,\qquad
 z=\alpha\delta V_0+s_\nu\delta\nu.                      \tag{B.9}$$

$c$ 还需减去 $C_{{\rm ref},\nu}\delta\nu/\alpha$ 的零模。
例如 (B.8) 的两个独立实际导数为

$$\partial_{V_0}c_0=-m^{-2},\qquad
 \partial_\nu c_0=-\frac{C_{{\rm ref},\nu}V_0(2s+\alpha V_0)}{m^2}.
                                                               \tag{B.10}$$

全部腰 $B=0$ 与 $U=0$ 等价，因为 $v$ 从不为零。原物理第四频振幅行
$C_1^{\cos}=-\alpha$ 则准确使用 (B.5)，不把曲率角上的第一模误认作
物理第一模。故原有限边界行数、参数及全物理含义均可原样保留。

## 3. 变角的完整无限尾

设 $\psi=\theta-\phi=I(v-m)/m$ 在 $|\Im\phi|\le\sigma$ 解析，
实轴上实且奇，且已付

$$|\Im\psi(x\pm i\sigma)|\le P_\sigma<\sigma,
 \qquad \tau=\sigma-P_\sigma>0,\qquad
 U_\sigma\ge\sup_{|\Im\phi|\le\sigma}|u|.                \tag{B.11}$$

这些是假设的明确可检查门，不在本文中冒称某个实际完整中心已通过。
对有限实正弦 $\psi=\sum_{j\ge1}\psi_j\sin(4j\phi)$，可直接取完整有限和

$$P_\sigma=\sum_{j\ge1}|\psi_j|\sinh(4j\sigma),          \tag{B.12}$$

比用 $\sup|\psi|$ 更准确；若有无限尾，该尾必须同时计入。(B.11) 仅用
来估计精确矩的全部物理频率，不要求先构造复域中的逆角。

对 $k=4j>0$ 把 (B.3) 的积分移到 $\Im\phi=-\sigma$。周期性抵消两侧
边界，且 $\Im\theta\le-\tau$，从而

$$|\widehat C_k^\theta|\le |m|^{-1}e^{-|k|\tau},\qquad
 |\widehat B_k^\theta|\le U_\sigma|m|^{-1}e^{-|k|\tau}.  \tag{B.13}$$

负 $k$ 移到上边界。若只在开条带有界，先移到略窄条带再取极限；相同
不等式成立。因此 $M$ 模后的完整物理 $A_0$ 尾满足

$$\begin{aligned}
 \|P_{>M}C\|_{A_0}&\le\frac2{|m|}
        \frac{e^{-4(M+1)\tau}}{1-e^{-4\tau}},\\
 \|P_{>M}B\|_{A_0}&\le\frac{2U_\sigma}{|m|}
        \frac{e^{-4(M+1)\tau}}{1-e^{-4\tau}}.
\end{aligned}                                                   \tag{B.14}$$

所有 $\ell$ 阶角导数尾只需将对应和替换为
$\sum_{j>M}(4j)^\ell e^{-4j\tau}$。该和是完整几何级数的有限次
$4q\partial_q$ 导数，$q=e^{-4\tau}$，可严格计算。若 $|q_{4j}|\le Q$
为真实全模帽界，则 Robin 尾被 $B$ 尾加 $Q$ 倍 $C$ 尾控制；这不消掉
帽非线性余项或任何 mean。

令 $H_\sigma\ge\sup|h_1|$、$\Theta_\sigma\ge\sup|\delta\theta|$。
同一移线对全部 (B.7) 给

$$|\delta\widehat C_k^\theta|
 \le\left(\frac{|z|}{|m|^2}
             +\frac{|k|\Theta_\sigma}{|m|}\right)e^{-|k|\tau},$$
$$|\delta\widehat B_k^\theta|
 \le\left(\frac{|z|U_\sigma}{|m|^2}
       +\frac{H_\sigma+|k|U_\sigma\Theta_\sigma}{|m|}\right)
          e^{-|k|\tau}.                                    \tag{B.15}$$

例如完整四重 Wiener 范数上 $\|I\|\le1/4$，故

$$\Theta_\sigma\le\frac1{4|m|}
       \left(\|h_2\|_{A_\sigma}
              +\frac{|z|}{|m|}\|v\|_{A_\sigma}\right).     \tag{B.16}$$

(B.15) 的全部尾由上一几何级数及其一阶导数求和。没有只控制有限
Jacobian 后删除高频变分；实际 mean 与度量列通过 (B.9) 同时保留。

## 4. 完整角积分与梯形误差

矩中的指数一般不是有限 Fourier 多项式；即便内部方程三次支持3M，
也不能据 $N>6M$ 宣称边界梯形积分无混叠。

对任意 $P$ 周期函数 $f$，若在闭条带 $\sigma$ 解析且 $|f|\le M_f$，
其 $N$ 等分平均 $Q_Nf$ 满足

$$|Q_Nf-\langle f\rangle|
 \le\frac{2M_f}{e^{4N\sigma}-1}.                           \tag{B.17}$$

证明：完整 Fourier Cauchy 估计为 $|\widehat f_j|\le M_fe^{-4|j|\sigma}$，
而 $Q_Nf-\langle f\rangle=\sum_{\ell\ne0}\widehat f_{\ell N}$；绝对求和
就是 (B.17)。所有被混叠的频率都已计入。

在 (B.11) 下，(B.3) 的两个被积函数可分别取

$$M_f=e^{|k|(\sigma+P_\sigma)},\qquad
 M_f=U_\sigma e^{|k|(\sigma+P_\sigma)}.                   \tag{B.18}$$

再乘 $1/|m|$ 及实正弦/余弦的因子2，得到每条实际边界矩的完整离散误差。
对变分矩，用 (B.15) 中相同的 numerator 结构、将衰减指数换成
$e^{|k|(\sigma+P_\sigma)}$，即可对每条完整 Jacobian/参数行使用 (B.17)。
数值舍入误差仍须由实际有向运算另包围。均值 (B.4)、(B.8) 应直接用
准确恒等式，而非给它们不必要的梯形误差。

实际使用必须同时支付输入中心/目标身份、真实 $v,m$ 非零、(B.11) 的
全域门、(B.14)–(B.17) 的所有费用及真帽非线性关系。本文完成的是可
直接消费的完整边界算子公式；最终主体、全逆、非线性收敛和闭面几何
仍按 open.md 继续。
