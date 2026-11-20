# R138 补篇：真根全角比较的实际小费用与无导数 mean 读出

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**已证明的同对象结论。** 在真根，用同一 Qrepair、准确 $\eta_0,\nu_0$ 和同一物理径向模型的轴初值，解 (U.22) 的完整 $0\le\phi\le2\pi$ 角 ODE。它和真正周期物理径向 frame 的差已有明确小界
$$
\boxed{\quad
\|\bar O-O^{P,c}\circ\Theta_c\|_\infty<11/10^7,\qquad
|\bar G-G^{P,c}\circ\Theta_c|_\infty<1/25000.
\quad}
\tag{W.1}
$$
所以新的根圈 ODE 消费者可以直接使用 (W.1) 支付实际 frame/位置转移。这里没有计算那条新角 ODE，没有证明根 mean 分母或完整根型为正，也没有把角比较模型的端点直接拼成周期 frame。

根 mean 分母可从角旋转源的平均直接读出，不需对 frame 求导。因此 (W.1) 足够支付这个实际分母和有限角矩阵的几何输入；完整高尾仍须其真正所需的导数/乘子费用。

## 1. 全部规范与已经完成的输入

使用[同物理角 support 补篇](R138-supplement-actual-positive-support-for-repaired-physical-frame.md)的原 moving 模型 $(O^M,F^M)$、原物理径向模型 $(O^P,F^P)$ 和同外锚修补模型 $(O^{P,c},F^{P,c})$。平移仍为 $p=\tfrac12e_z$，故 $G=F-p$；同一点的差不因这个共同平移改变。

令 $\epsilon_c=4/10^{18}$。该补篇已经证明
$$
\|O^P-O^M\circ\Phi\|<4\,10^{-7},\quad
|F^P-F^M\circ\Phi|<3\,10^{-6},
$$
$$
\|O^{P,c}-O^P\|<2\,10^{-8},\quad
|F^{P,c}-F^P|<4\,10^{-8},\quad
|\Phi\circ\Theta_c-\mathrm{id}|<41000\epsilon_c.
\tag{W.2}
$$
这里 $\Phi$ 是原 lift 的真实逆，$\Theta_c$ 是 Qrepair 的真实 lift。它们没有被认成同一个角。完整 mean 和所有原接口已经包含于这些已付比较中。

原[完整角缺陷实际记录](../notes/2026-11-14-R133-final-complete-angular-defect.md)给
$$
\|E\|<1/30000000,\quad |P_M|<1/20000000,\quad
\|O^M_{\phi\phi}\|<4.646383.
\tag{W.3}
$$
这些是全径向、全环境 $2\pi$ 圈的界。周期性使 $O^M_\phi$ 的平均为零；按圆周最短距离积分，
$$
\|O^M_\phi\|\le(\pi/2)\|O^M_{\phi\phi}\|<8.
$$
原 support 证明 (S.6) 又给 $|f_\phi|<10$，故
$|F^M_\phi|\le|f_\phi|+|P_M|<11$。因此 (W.2) 在同一个 moving 点上变成
$$
\boxed{\quad
\|O^{P,c}\circ\Theta_c-O^M\|<a_0,\quad
|G^{P,c}\circ\Theta_c-(F^M-p)|<f_0,
\quad}
\tag{W.4}
$$
其中准确可取
$$
a_0=421/10^9,\qquad f_0=3041/10^9.
\tag{W.5}
$$
例如额外 frame 角图费为 $8\cdot41000\epsilon_c$，位置费为
$11\cdot41000\epsilon_c$；它们严格包含在 (W.5) 的放宽里。

## 2. 修补后的角连接与速度差已付

在原 moving 角，
$$
\Omega_\phi=\Omega(b_0v/m,au/m,a/m),\qquad
f_\phi=(0,av/m,0)^t,\qquad m=\langle v\rangle.
\tag{W.6}
$$
原 $\Omega(x,y,z)$ 是 skew 矩阵，其 operator 范数为
$\sqrt{x^2+y^2+z^2}$。由于
$O^M_\phi=O^M\Omega_\phi+E$，(W.3) 也给
$\|\Omega_\phi\|<8$。

原实际 $|v|,|m|>1/12$；修补后 $|v_c|,|m_c|>1/13$，
且完整 $|\Delta u|,|\Delta v|,|\Delta m|\le\epsilon_c$。
因此 $|m/m_c|<101/100$。对 (W.6) 作准确商差，三个连接分量分别不超过
$$
202\epsilon_c,\qquad113\epsilon_c,\qquad104\epsilon_c.
$$
例如第一分量的两项为
$$
\left|\frac{b_0}{m_c}\Delta v\right|
\le8\frac{101}{100}\,12\epsilon_c<98\epsilon_c,\qquad
\left|\frac{b_0v}{m}\frac{\Delta m}{m_c}\right|
<104\epsilon_c.
$$
第二分量的第一项用原 (W.6) 第三连接分量
$|a/m|<8$，故
$|a/m_c|\le|a/m|\,|m/m_c|<8\cdot101/100<9$；
第二项用 $|au/m|<8$ 与 $1/|m_c|<13$，小于 $104\epsilon_c$。
第三分量同样小于 $104\epsilon_c$。因此
$$
\|\Omega_{\phi,c}-\Omega_\phi\|<300\epsilon_c.
\tag{W.7}
$$
同样用 $|av/m|<10$，速度差的两项小于
$122\epsilon_c$ 与 $130\epsilon_c$，从而
$$
|f_{\phi,c}-f_\phi|<300\epsilon_c.
\tag{W.8}
$$
全部 intrinsic 系数没有改变；这是同一个原中心到 Qrepair 的比较，不是不同参数模型之间的替换。

## 3. 真正全圈比较，不借未闭扇区 holonomy

现在固定真实 $r=r_*$，定义唯一角初值问题
$$
\bar O_\phi=\bar O\Omega_{\phi,c},\qquad
\bar G_\phi=\bar O f_{\phi,c},
$$
$$
\bar O(0)=O^{P,c}(r_*,0),\qquad
\bar G(0)=G^{P,c}(r_*,0).
\tag{W.9}
$$
这正是 (U.22)，整个区间为 $[0,2\pi]$。Qrepair 保原反射奇偶类，所以 $\Theta_c(r,0)=0$。因此这里的轴初值正是两标量径向入口的同一实际初值；没有另选 frame 或世界位置。

置
$e_*=1/30000000$、$p_*=1/20000000$、
$d_*=300\epsilon_c$。
用 (W.4) 的起点差比较 $\bar O$ 与 $O^M$：
$$
(\bar O-O^M)_\phi
=(\bar O-O^M)\Omega_{\phi,c}
 +O^M(\Omega_{\phi,c}-\Omega_\phi)-E.
$$
两个准确 frame 都正交，右侧齐次传播正交，故
$$
\|\bar O(\phi)-O^M(\phi)\|
\le a_0+\phi(e_*+d_*).
\tag{W.10}
$$
位置差的导数是
$(\bar O-O^M)f_\phi+\bar O(f_{\phi,c}-f_\phi)-P_M$，因此
$$
|\bar G-(F^M-p)|
\le f_0+10\phi a_0+5\phi^2(e_*+d_*)+\phi(p_*+d_*).
\tag{W.11}
$$
最后加回 (W.4)，得到实际完整差
$$
\|\bar O-O^{P,c}\circ\Theta_c\|
\le2a_0+\phi(e_*+d_*),
$$
$$
|\bar G-G^{P,c}\circ\Theta_c|
\le2f_0+10\phi a_0+5\phi^2(e_*+d_*)+\phi(p_*+d_*).
\tag{W.12}
$$
用 $0\le\phi\le2\pi<44/7$ 作有理放宽，第一式小于
$11/10^7$，第二式小于 $1/25000$，证明 (W.1)。

实际 $(O^{P,c},G^{P,c})$ 是同一全圈周期径向对象，故 (W.1) 也控制比较 ODE 的端点 holonomy/position 缺陷。但 $\bar O,\bar G$ 没有因此被定义为周期对象；后续积分仍保完整 $[0,2\pi]$，不能拼四个独立扇区来删去这些费用。

## 4. 根 mean 分母只需要这个 C0 费用

沿用[完整根型补篇](R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md)的
$\ell=X(r_*,0)$，所有向量都在第 3 节同一个固定环境坐标中。令
$$
q_0=-I_\phi(v-m)/m,\qquad
t_0=q_0/v,\qquad
A_0=(t_0)_\phi+1/m,\qquad
B_0=-uA_0-t_0u_\phi,\qquad \rho=a/m.
\tag{W.13}
$$
根旋转曲率源 (U.4) 对完整 mean 方向 $(f,\mu)=(0,1)$ 的输出准确为
$$
g_m=\rho(A_0X+B_0Y).
\tag{W.14}
$$
因此原完整相容分母就是
$$
\boxed{\quad\mathcal D=\langle g_m\rangle_\phi\cdot\ell.\quad}
\tag{W.15}
$$
(U.8) 的含 $\mathcal A=T_\phi+u_\phi Y$ 形式与 (W.15) 由周期分部积分准确等价；(W.15) 不含 frame 导数或一个被假设为零的 $Z$。实际 frame 的非零缺陷没有消失，而是被准确写回 $X,Y$ 的值中。

用同一实际系数 $A_0,B_0$ 与比较 $\bar X,\bar Y$ 得到
$\bar{\mathcal D}$。正交 frame 的 operator 差与 (W.1) 给
$$
\boxed{\quad
|\mathcal D-\bar{\mathcal D}|
\le\frac{11}{10^7}\,
 \left\langle|\rho|\sqrt{A_0^2+B_0^2}\right\rangle_\phi.
\quad}
\tag{W.16}
$$
右侧是明确的 root 系数积分，全部 mean 和 primitive 保留。新的 directed angular 消费者只需给 $\bar{\mathcal D}$ 的整个积分球并加 (W.16)，就得到真正 periodic frame 的分母球；这并非拿新角模型的未闭 holonomy 当成 mean 相容条件。

同理，有限个指定 Fourier 输入的 $g_f$、$g_m$ 以及 (U.12)--(U.14) 的积分，均可在整圈比较路径上以 (W.1) 支付完整 C0 差。实际分母必须先与零分离，才能执行 mean 消元。非零 mean、高 stable 行、实际位置 $G$ 与所有 cross 项仍是原完整公式的一部分。

本篇没有从 C0 差推出任意阶乘子小量。若高频余项消费 $O_\phi,G_\phi$ 或更高角导，仍须使用实际缺陷方程或其他已证导数包络；(W.1) 不替代那一步。
