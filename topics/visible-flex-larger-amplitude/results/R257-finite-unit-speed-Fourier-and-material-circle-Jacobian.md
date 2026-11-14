# R257. 有限单位速平面 Fourier 的圆障碍与材料角圆参考 Jacobian

日期：2026-11-14。

**状态。** 本文证明两个独立而相关的有限表示结论：

1. 正速度恒定的闭合平面曲线若为有限 Cartesian Fourier，必为圆的非零整数覆盖；
2. 固定 scalar 的精确圆参考若直接用均匀材料角 Fourier 表示，原 Frenet RHS 的物理有限 Jacobian 在精确算术及解析投影或充分解混叠的 DFT 下，确实保留 R255 的全部模态块。

本文不声称当前非圆 warm、某个新的材料角离散、native 尾解或完整 BVP 已成功。不改变本课题原有数值近似与精确存在的区分，也不增加“每个有限近似必须字面精确等距”的完成门。

## 1. 定理 R257-A：有限 Fourier、闭合与恒速强制圆

把有向平面正交识别为复平面。设闭合参数曲线
$$
\gamma:\mathbb R/(2\pi\mathbb Z)\longrightarrow\mathbb C
$$
是有限 Laurent/Fourier 多项式
$$
\gamma(\theta)=\sum_{j=j_-}^{j_+}a_j e^{ij\theta},
$$
并且
$$
|\gamma'(\theta)|\equiv v>0.
\tag{257.1}
$$

**结论。** 存在整数 $\ell\ne0$、复数 $\gamma_0,b$，使
$$
|b|=v,\qquad
\gamma'(\theta)=b e^{i\ell\theta},\qquad
\gamma(\theta)=\gamma_0+\frac{b}{i\ell}e^{i\ell\theta}.
\tag{257.2}
$$
因此像是半径 $v/|\ell|$ 的圆，参数化覆盖次数为 $|\ell|$，有向单位切向的转角 degree 为 $\ell$。

**证明。** 记 $w=\gamma'$。它仍是有限 Laurent 多项式，且非零，因为 $v>0$。令 p、q 分别为 w 的最低、最高非零频率：
$$
w(\theta)=\sum_{j=p}^q b_j e^{ij\theta},\qquad b_p b_q\ne0.
$$
若 $p<q$，则 $|w|^2$ 的频率 $q-p$ 系数只有一项
$$
b_q\overline{b_p}.
$$
原因是 j、k 均在 $[p,q]$ 中，$j-k=q-p$ 只可能取 $j=q,k=p$。此项非零，与 $|w|^2\equiv v^2$ 的所有非零频率系数为零矛盾。所以 $p=q=\ell$，w 只能是单频，且 $|b_\ell|=v$。

由于 $\gamma$ 闭合，
$$
0=\int_0^{2\pi}\gamma'(\theta)\,d\theta.
$$
如果 $\ell=0$，该积分为 $2\pi b_\ell\ne0$；故 $\ell\ne0$。积分该单频函数得到 (257.2)。

最后，
$$
\frac{\gamma'}{|\gamma'|}
=\frac b{|b|}e^{i\ell\theta}
$$
的 degree 为 $\ell$；(257.2) 在一个参数周期内恰绕该圆 $|\ell|$ 次。证毕。

这个证明不预先假设曲线简单或凸，也允许自交的候选参数化。恒速有限 Fourier 的条件本身已经把它限制为圆的整数覆盖。degree=0 不能出现；其单频零频率情形已由闭合排除，而不是靠“默认简单”排除。

### 1.1 简单性与 turning-one 的确切作用

若 $\gamma$ 是圆周的单射参数化，$|\ell|\ge2$ 时
$\gamma(\theta+2\pi/|\ell|)=\gamma(\theta)$，与单射矛盾，所以 $|\ell|=1$。若进一步指定有向切向 degree 为 1，则 $\ell=1$；degree 为 -1 对应相反方向。

因此在本题正向、turning-one、单位速的平面入口类中，纯有限 Cartesian Fourier 的精确入口只能是半径 1 的圆。不是任意一种有限参数化，而是这个严格的有限 Fourier 与恒速组合导致该限制。

## 2. 旋转材料角 Fourier 也在定理范围内

假设平面入口写为
$$
\gamma(\theta)
=\bigl(R(\theta)\cos\theta-T(\theta)\sin\theta,\;
       R(\theta)\sin\theta+T(\theta)\cos\theta\bigr),
$$
其中 R、T 均为有限 Fourier 函数。复数形式为
$$
\gamma(\theta)=e^{i\theta}\bigl(R(\theta)+iT(\theta)\bigr),
$$
仍是有限 Laurent 多项式。因此换成旋转材料角的有限 R/T 系数并不绕过定理。

尤其，当前常用的反射对称类
$$
R=r_0+\sum_{j=1}^M r_j\cos(2j\theta),\qquad
T=\sum_{j=1}^M t_j\sin(2j\theta)
$$
也受同一限制。不能同时要求：

- 精确保留一个指定的非圆平面入口像；
- 该入口在共同材料角 theta 中严格单位速，即入口角度量为 $d\theta^2$；
- 整个入口位置是上述纯有限 Fourier 函数。

三者不能同时成立。放弃字面恒速、保留并计量截断误差，是一种可能的近似离散；把完整非多项式入口作为已知解析 lift 保留，再加有限未知量，是另一种表示。它们各有额外的对象身份和验证成本，不能以“只是换坐标”掩盖。

## 3. 原 support core 的真实材料入口及其导数

令当前归一化 support core 为
$$
r_c(\phi)=1+\sum_{j=1}^M c_j\cos(\omega_j\phi),
\qquad \omega_j=2j,
$$
$$
\Gamma_c(\phi)=r_c(\phi)e_r(\phi)+r_c'(\phi)e_\phi(\phi).
$$
定义
$$
\rho_c(\phi)=r_c+r_c''
=1+\sum_{j=1}^M(1-\omega_j^2)c_j\cos(\omega_j\phi).
$$
假设全圆 $\rho_c>0$。直接求导得到
$$
\Gamma_c'(\phi)=\rho_c(\phi)e_\phi(\phi).
\tag{257.3}
$$
原材料图为
$$
\Theta_c(\phi)=\phi+
\sum_{j=1}^M\frac{1-\omega_j^2}{\omega_j}
c_j\sin(\omega_j\phi),\qquad
\Theta_c'=\rho_c>0.
\tag{257.4}
$$
它是 degree-one 圆微分同胚。取逆 $\phi=\Phi_c(\theta)$，则
$$
G_c(\theta)=\Gamma_c(\Phi_c(\theta)),\qquad
\partial_\theta G_c=e_\phi(\Phi_c(\theta)),
\qquad |\partial_\theta G_c|=1.
\tag{257.5}
$$
它精确保留原入口像，但一般有无限 theta Fourier 谱。若有非零高 support 模式且入口非圆，定理 R257-A 已排除有限 theta 位置表示。

这里的“rho=1”是材料坐标中的单位速事实，不是把原 support 密度 $\rho_c(\phi)$ 擅自改成 1。保留原 $\Gamma_c(\theta)$ 而不做真实逆图，就没有得到 (257.5)。

### 3.1 完整位置的 core 导数存在有用的抵消

在固定 theta 下，
$$
\partial_{c_j}\Phi_c(\theta)
=-\frac{(1-\omega_j^2)\sin(\omega_j\phi)}
       {\omega_j\rho_c(\phi)}.
$$
另一方面，
$$
\partial_{c_j}\Gamma_c(\phi)
=\cos(\omega_j\phi)e_r-\omega_j\sin(\omega_j\phi)e_\phi.
$$
结合 (257.3)，复合函数的两个项相加，得到
$$
\boxed{
\partial_{c_j}G_c(\theta)
=\cos(\omega_j\phi)e_r(\phi)
-\frac{\sin(\omega_j\phi)}{\omega_j}e_\phi(\phi),
\qquad \phi=\Phi_c(\theta).
}
\tag{257.6}
$$
因此完整**位置**的这个一阶 core 导数不需要保留两个各自很大的 $1/\rho$ 项作相减。角导、二阶 core 导以及有限 theta 投影仍有自己的条件数问题；(257.6) 不消除它们。

例如用归一化连续 $L^2(d\theta)$ 范数，并令
$0<\rho_*\le\rho_c\le\rho^*$，对任意系数方向 d，有
$$
\frac{\rho_*}{2}\sum_j
\left(1+\frac1{\omega_j^2}\right)d_j^2
\le
\left\|\sum_j d_j\partial_{c_j}G_c\right\|_{L^2(d\theta)}^2
\le
\frac{\rho^*}{2}\sum_j
\left(1+\frac1{\omega_j^2}\right)d_j^2.
\tag{257.7}
$$
证明是令
$A(\phi)=\sum_jd_j\cos(\omega_j\phi)$、
$B(\phi)=-\sum_jd_j\sin(\omega_j\phi)/\omega_j$；
正交的 $e_r,e_\phi$ 给出位置平方范数 $A^2+B^2$，再用
$d\theta=\rho_c\,d\phi$ 和三角正交性即可。

这个连续下界不自动传给截频后的 $P_M^\theta G_c$；投影可能丢掉导数的高频部分。不得据此宣布新有限入口 Jacobian 已良态。

## 4. 另一个问题：理想材料圆上的原 Frenet 微分

现在固定一个位置 s 及固定 scalar 值
$$
a>0,\qquad \nu\in(-1,1),\qquad w=\sqrt{1-\nu^2}.
$$
这里 nu 是同一个原 RHS 使用的 scalar 第二分量；本节只研究对物理场的微分，固定 a、nu，不把 active scalar 或 core 变化混入物理 Jacobian。

对任意正则角曲线 F，原 Frenet 公式为
$$
T=\frac{F_\theta}{|F_\theta|},\qquad
N=\frac{F_{\theta\theta}-
 (F_{\theta\theta}\cdot T)T}
 {\left|F_{\theta\theta}-(F_{\theta\theta}\cdot T)T\right|},
\qquad B=T\times N,
$$
$$
\kappa=
\frac{\left|F_{\theta\theta}-
 (F_{\theta\theta}\cdot T)T\right|}{|F_\theta|^2},
$$
$$
\mathcal V(F)
=\alpha N+\beta B,\qquad
\alpha=-\frac{\nu}{a\kappa},\qquad
\beta=\sqrt{1-\alpha^2}>0.
\tag{257.8}
$$
在精确材料圆
$$
F_\circ(\theta)=a e_r(\theta)+z e_z
$$
上，
$$
T=e_\theta,\quad N=-e_r,\quad B=e_z,\quad
\kappa=1/a,\quad \alpha=-\nu,\quad \beta=w.
$$
故 $\mathcal V(F_\circ)=\nu e_r+w e_z$。

取任意平滑周期变分
$$
V=u e_r+v e_\theta+h e_z.
$$
记 $\delta$ 为物理场方向导数。由
$$
V_\theta=(u_\theta-v)e_r+(u+v_\theta)e_\theta+h_\theta e_z
$$
及再求一次角导，可直接得到
$$
\delta|F_\theta|=u+v_\theta,
$$
$$
\delta\kappa=-\frac{u+u_{\theta\theta}}{a^2},
$$
$$
\delta N=\frac{u_\theta-v}{a}e_\theta+
\frac{h_{\theta\theta}}a e_z,\qquad
\delta B=\frac{h_{\theta\theta}}a e_r-
\frac{h_\theta}a e_\theta.
\tag{257.9}
$$
为核曲率式，可先记法向未归一化向量的模为 nn。在该圆上
$\mathrm{nn}=a$，其一阶变化为
$-u_{\theta\theta}+u+2v_\theta$。把它除以
$|F_\theta|^2$ 的变化代入，正好消去 $v_\theta$，得上述曲率变化。

固定 a、nu 时，
$$
\delta\alpha=-\frac{\nu}{a}(u+u_{\theta\theta}),
\qquad
\delta\beta=-\frac{\nu^2}{aw}(u+u_{\theta\theta}).
$$
故原完整 Frenet RHS 的线性化为
$$
\boxed{\begin{aligned}
(\delta\mathcal V)_r
&=\frac{\nu}{a}(u+u_{\theta\theta})
 +\frac wa h_{\theta\theta},\\
(\delta\mathcal V)_\theta
&=\frac{\nu}{a}(v-u_\theta)-\frac wa h_\theta,\\
(\delta\mathcal V)_z
&=-\frac{\nu}{a}h_{\theta\theta}
 -\frac{\nu^2}{aw}(u+u_{\theta\theta}).
\end{aligned}}
\tag{257.10}
$$
此推导没有先施加线性等距约束；它是完整物理状态空间上的微分。

## 5. 定理 R257-B：材料角有限投影保留全部圆参考模态块

取反射对称的有限旋转材料角空间
$$
u=U_0+\sum_{j=1}^M U_j\cos(2j\theta),\qquad
v=\sum_{j=1}^M V_j\sin(2j\theta),
$$
$$
h=H_0+\sum_{j=1}^M H_j\cos(2j\theta).
\tag{257.11}
$$
其维数恰为 $3M+2$，包含完整高度均值 H0。由 (257.10)，每个频率保持在自身三维空间中。对 k=2j，按 $(U_j,H_j,V_j)$ 排列，
$$
\begin{pmatrix}U_j\\H_j\\V_j\end{pmatrix}'
=\frac1a K_k
\begin{pmatrix}U_j\\H_j\\V_j\end{pmatrix},
$$
$$
\boxed{
K_k=
\begin{pmatrix}
\nu(1-k^2)&-wk^2&0\\
\nu^2(k^2-1)/w&\nu k^2&0\\
k\nu&kw&\nu
\end{pmatrix}.
}
\tag{257.12}
$$
零模态按 $(U_0,H_0)$ 排列为
$$
\frac1a K_0,\qquad
K_0=
\begin{pmatrix}
\nu&0\\
-\nu^2/w&0
\end{pmatrix}.
\tag{257.13}
$$
这里 V0 因指定的反射对称表示而不存在；若允许完整切向零模态，其导数另为 $\nu V_0/a$。

**投影结论。** 若用解析 Fourier 投影定义有限 RHS，则其在精确圆上的物理 Jacobian，经过固定状态排列，正好是上述块对角矩阵。若改用均匀 theta 网格
$$
\theta_\ell=2\pi\ell/N,\qquad N>4M,
$$
并使用原归一化 Fourier 合成/投影，则在精确算术中结论仍完全成立。

**证明。** 令 $S_M$ 为有限状态合成到 (257.11) 的线性映射，$Q_M$ 为相应 Fourier 投影。有限 RHS 为
$$
f_M(y)=Q_M\mathcal V(S_My).
$$
在圆状态 $y_\circ$，链式给出
$$
Df_M(y_\circ)=Q_M D\mathcal V(F_\circ)S_M.
$$
(257.10) 已证明 $D\mathcal V(F_\circ)$ 把每个保留模态映回同一模态；而 $Q_MS_M=I$，所以投影没有丢掉任何线性化分量，得到 (257.12)--(257.13)。

对均匀 DFT 投影，最高保留角频率为 $2M$。任意两保留频率的和、差绝对值至多 $4M$。当 $N>4M$，
$$
\frac1N\sum_{\ell=0}^{N-1}e^{ij\theta_\ell}
=0\quad(0<|j|\le4M).
$$
因此离散 cosine/sine 正交性与零模态归一化在该空间中完全正确，$Q_{M,N}S_M=I$。又线性化结果不产生超出该空间的频率，故
$$
Q_{M,N}D\mathcal V(F_\circ)S_M
$$
仍为相同块矩阵。证毕。

该解混叠结论只用于**精确圆处的线性化**。非圆场上的平方根、归一化和其他非线性一般产生高频，不能由此说整个有限非线性 DFT 等于无限精度的解析 Galerkin 投影。

### 5.1 精确最小多项式和 coast 传播

对每个 k，
$$
K_k^2=\nu K_k,
\qquad K_0^2=\nu K_0.
\tag{257.14}
$$
一种直接核对是写 $K_k$ 的左上块为
$$
N_k=
\binom{1}{-\nu/w}
\begin{pmatrix}\nu(1-k^2)&-wk^2\end{pmatrix}.
$$
右行乘左列为 nu，故 $N_k^2=\nu N_k$；而
$(k\nu,kw)N_k=0$。按分块相乘即得 (257.14)，零块直接相乘亦成立。

因此整个材料角有限物理 Jacobian J 满足
$$
\boxed{J^2=\frac{\nu}{a}J,\qquad
\operatorname{spec}J\subset\{0,\nu/a\}.}
\tag{257.15}
$$
没有依赖 k 的大实特征值。这是当前明确理想参考、固定 scalar、同一原 Frenet 公式及指定投影规则下的代数结论。

若进一步沿实际 coast 有 $a'=\nu$ 且 nu 常数，a 为正仿射函数，则 R255 的直接微分证明给出每个模态的传播
$$
I+\frac{s-s_0}{a(s_0)}K_k.
$$
这保留大 $k^2$ 非正规剪切；小谱不意味着小传播范数或整个 BVP 良态。固定 theta 度量的等距子空间仍需
$U_j+kV_j=0$；(257.12) 的全空间物理 Jacobian并不把所有变分都变成等距变分，详见 [R255](R255-circle-reference-linear-isometry-and-coast-shear.md)。

## 6. 对当前换表示备选的严格边界

本结果证明：如果完整物理场直接用均匀材料 theta 的有限 R/T/Z 表示，在精确圆参考上，原有限 Fourier Jacobian 可以具有正确的圆模态结构，不必出现由另一种截频表示造成的参考态谱偏移。

它同时证明：指定非圆 support core 的真实材料入口一般不能也纯粹落在这个有限空间中并保持严格单位速。必须明确选择入口投影及其误差，或保留完整非多项式入口 lift 等不同有限表示。

这两项结论不能相互抵消。圆参考 Jacobian 的好性质不能证明新非圆联解存在；入口不能纯有限精确保留也不禁止满足原数值误差要求的近似方案。

此外：

- 把实际物理 phi 曲线直接改名为 theta 并令 rho=1，不是合法的材料重参数化；
- 真实连续重参数化保持像和同一 canonical metric；有限投影通常改变有限场，必须标为新离散；
- 在材料表示中消去右端高度的 P 投影，不自动消去入口逆图或新有限入口投影的条件数；
- 固定 scalar 的物理 Jacobian 结论不等同于完整 core/control/boundary 设计 Jacobian 的谱结论；
- binary64、FFT 与 complex-step 的实际结果仍会有舍入，本文不把它们声称为逐位满足 (257.14)；
- 实际新尾、cut jets、完整 metric、闭面幅度与 reach，均须由新表示自己的真实输出支付。

可行性和下游成本另见 [uniform 材料角备选说明](../notes/2026-11-14-uniform-material-angle-representation-option.md)。当前主线和当前 Actions 不因本文自动更换方程、表示或验收门。

