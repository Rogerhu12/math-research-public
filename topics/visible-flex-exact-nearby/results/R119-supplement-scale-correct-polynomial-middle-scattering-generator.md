# R119 续篇：实际尺度下的多项式中频正定散射导数

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 在第53束同一个受控尾、原来保留的 middle
频带、同一两个 phase 补偿图和原参数盒内，本篇给出完整二维
complex scattering generator 的统一下界
\[
             -iS_M^*D_{\theta_M}S_M
                  >2^{-2200000}M^{-30697}I_2.                 \tag{S.1}
\]
它适用于全部深层 \(j\ge8193\) 的实际保留频率，不只高振荡区。
没有改 \(\zeta_j,h_j,b_M\)、原标签、\(\mathsf K\) 或最终度量对象。

关键是把实际尺度 \(\Delta=aB\) 保留到二十一阶导数预算中。
有限次数的复根消元只作用于真正的多项式；真实未知解始终在实
区间估计。尤其缩放 \(Q\mapsto Q/B\) 后，根上首行除法也要支付
\(B^2\)，本篇没有略去这一项。

本篇没有将 (S.1) 当作完整非径向混模矩阵的下界，也未据此宣称
原 source 空间上的全 Green 或非线性 \(\mathcal F=0\) 已闭合。

## 1. 同一真实区间及保留的中频

沿用[全部 Sym2 多项式分离](R119-supplement-polynomial-all-Sym2-profile-separation-and-positive-control.md)
及[真实完整二维正定控制](R119-supplement-all-quadratic-phase-preserving-positive-scattering-control.md)。
记
\[
 \delta=(2/25)2^{-j},\quad J=j+5,\quad j\ge8193,\qquad
 a=\frac{\delta^{3/2}}{8\sqrt6},\quad B=\frac{\Delta}{a},
\]
\[
 80<\Delta<3J,\quad B>2^{190},\quad
 \delta^{3/2}/32<a<\delta^{3/2}/16,\quad
 K=2^{6000}J^8\delta^{-16}.                                  \tag{S.2}
\]
这里 \(a\) 是径向 ramp 的尺度，不是标签或 Jacobi 逆密度。

在原第 \(n\) 个未使用区间内，取与它同中心、长度为
\[
       \ell=\frac1{512(n+1)(n+2)}                            \tag{S.3}
\]
的闭子区间 \(I\)。这是原区间的中间一半；所有新方向仍严格
支持在原 \(I_n\) 内，原其它控制及两补偿 bump 位于其外。
该邻域中的当前 profile 准确为
\[
 Q(x)=7+Bf(x),\quad f(x)=30x^2(1-x)^2,\quad
 dt=a\,dx,\quad \mu_t/\mu=-1-Q,\quad I\subset[7/16,15/32].
                                                               \tag{S.4}
\]
固定 band \(M\in[U/2,U]\cap4\mathbb N\)，实际频率数
\(N_{\rm band}\le U\)。原 middle 定义给
\[
 M\ge2^{-40}\delta^{-1/8},\qquad n+1<2^{10}J,\qquad U\le2M.
                                                               \tag{S.5}
\]
这仍是原 \(T_j=2^{65536}J^{204}\delta^{-320}\) 以下的真实
保留频带，未重新分类或扩大低窗。

令 \(\lambda=M^2\)、\(k=\sqrt{7\lambda-16}\)。两条真实基本解
在区间中心使
\[
        Y=(\sqrt k\,\sqrt\mu h,\;(\sqrt\mu h)_t/\sqrt k)
                                                               \tag{S.6}
\]
的 fundamental matrix 为单位阵。对任意
\(A\in{\rm Sym}(2,\mathbb R)\)、\(\|A\|_F=1\)，
\(\mathcal K_A=Z-2\lambda Y_b+\lambda X\) 是前篇完整对称平方核。
不假定 \(A\) 正定或秩为一。

## 2. 真正按 \(\Delta=aB\) 缩放的有限 jet 消元

置
\[
 F=Q/B=f+7/B,\quad H=F+1/B,\quad \kappa=\lambda/B,\quad
 T=1+\Delta^2(1+\kappa),\quad g=F^{9/2}\mathcal K_A.
                                                               \tag{S.7}
\]
前篇 (P.5)--(P.7) 的真实三阶方程除去公共 \(B^4\) 后，成为
\(\widetilde{\mathscr D}g=0\)。其四个多项式系数是
\[
\begin{split}
 A_3={}&F'F^3,\\
 A_2={}&-\tfrac{27}{2}F^2(F')^2-F^3F'',\\
 A_1={}&\tfrac{297}{4}F(F')^3-\tfrac92F^2F'F''
                  +\Delta^2F'VF^3,\\
 A_0={}&-\tfrac{1287}{8}(F')^4+\tfrac{99}{2}F(F')^2F''
       -\tfrac92F^2F'F'''+\tfrac92F^2(F'')^2\\
 &+\Delta^2[-\tfrac92(F')^2VF^2
                 +3(2\kappa-H)(F')^2F^3-F''VF^3],
 \qquad V=4\kappa F-H^2 .
\end{split}                                                    \tag{S.8}
\]
前四项次数仍为 \(15,14,23,22\)，所以
\(\deg P\le19\) 时 \(\deg(\widetilde{\mathscr D}P)\le41\)。
实 \(I\) 上的完整系数和小于 \(2^{80}T\)，
\(|z|\le3\) 上每个系数小于 \(2^{128}T\)。
这些界跟随 \(F\) 的固定 quartic 系数及 \(\Delta^2(1+\kappa)\)，
没有把 \(\lambda\) 与 \(B\) 分别粗乘。

记 \(E_{20}=\sup_I|g^{(20)}|\)，以 \(g\) 在中心的十九阶 Taylor
多项式 \(P\) 及完整积分余项，得到真正多项式
\[
 H_P=\widetilde{\mathscr D}P,\quad
 \|H_P\|_I<2^{80}T E_{20},\quad \deg H_P\le41.
                                                               \tag{S.9}
\]
前篇42点完整 Lagrange 公式只作用于 \(H_P\)，从而在四个
\(F\) 根上的前四个归一 jet 满足
\[
      |(H_P)^{(l)}(z_i)/l!|
       <H_*:=2^{480}\ell^{-41}T E_{20}\quad(0\le l\le4).
                                                               \tag{S.10}
\]
四根仍满足
\[
 |z_i|<2,\quad |z_i-z_k|>2^{-4}B^{-1/2},\quad
                   |F'(z_i)|>16B^{-1/2}.                     \tag{S.11}
\]
在各根写 \(p_l=P^{(l)}(z_i)/l!\)。三角系统的第 \(l\) 个
对角准确是
\[
 (F'(z_i))^4(l-\tfrac92)(l-\tfrac{11}2)(l-\tfrac{13}2).
                                                               \tag{S.12}
\]
对 \(0\le l\le4\)，其模大于 \(2^{16}B^{-2}\)。
低三角系数小于 \(2^{138}T\)，所以真正的逐行除法是
\[
 |p_l|\le B^2H_*+2^{122}B^2T\sum_{q<l}|p_q|.
                                                               \tag{S.13}
\]
首项 \(B^2H_*\) 不能省去。由有限五行递推得到
\[
 \max_{i,0\le l\le4}|p_l|
       <2^{512}B^{10}T^4H_*
       =2^{992}\ell^{-41}B^{10}T^5E_{20}.                    \tag{S.14}
\]
完整20维 Hermite 公式的费用是
\[
 2^{64}(2^{-4}B^{-1/2})^{-19}
                         =2^{140}B^{19/2};
                                                               \tag{S.15}
\]
此处保留准确的半整数幂。中心前两 raw jet 因而满足
\[
       \max_{0\le r\le2}|g^{(r)}(c)|
        <2^{1133}\ell^{-41}B^{39/2}T^5E_{20}.                \tag{S.16}
\]

真实中心态的行列式为1；前篇 (P.17)--(P.19) 的代数可观测性
在 \(F\ge1,\ |F'/F|<2,\ |F''/F|<32\) 下给
\[
 \max_{0\le r\le2}|g^{(r)}(c)|
                         >2^{-50}aB^{-4}\lambda^{-2}.
                                                               \tag{S.17}
\]
于是完整所有 Sym2 都有
\[
 \boxed{\quad E_{20}>\epsilon_*:=
       2^{-1280}a\ell^{41}B^{-47/2}\lambda^{-2}T^{-5}.
       \quad}                                                  \tag{S.18}
\]
这里仅将 \(1183\) bits 放宽到 \(1280\)；\(47/2=39/2+4\)
准确包括缩放根上的首行 \(B^2\)。没有要求未知解的全复域延拓。

## 3. 完整实际两行的二十一阶上界

令 \(u=\sqrt\mu h\)、\(N=aM\sqrt B=\Delta\sqrt\kappa\)、
\(\gamma=1+\Delta+N\)。真实标量方程准确为
\[
 u_{xx}+
  [N^2F+\tfrac{\Delta}{2}f'-\tfrac{\Delta^2}{4}H^2]u=0.
                                                               \tag{S.19}
\]
采用实际平衡的两行
\[
       \mathcal Y=(\sqrt\gamma\,u,\;u_x/\sqrt\gamma).
                                                               \tag{S.20}
\]
\(\gamma\) 在该固定 mode、固定参数下不随 \(x\) 变。
其一阶系数是次数至多8的多项式，各阶归一系数小于
\(2^{40}\gamma\)：下左系数中 (S.19) 的方括号除以
\(\gamma\)，而其每个所需 jet 小于 \(2^{40}\gamma^2\)。

原完整双向 Cauchy 门 \(K\) 作用于 (S.6)，故在每个真实点
\[
 |\mathcal Y|^2
 \le K^2\bigl(\gamma/k+a^2k/\gamma\bigr)
                         <4\Delta K^2.                       \tag{S.21}
\]
例如 \(2M<k<3M\)、\(M\ge4\)、\(aB=\Delta>80\)，
\(\gamma/M=(1+\Delta)/M+a\sqrt B\)，而
\(a^2M/\gamma\le a/\sqrt B\)。这保留实际中心归一，
没有对一个 raw 高度另加未经授权的条件。

对该多项式系数系统作真实点的有限 Taylor 递推，
再乘 \(r!\)（\(r\le22\)），可逐阶得到
\[
       |\mathcal Y^{(r)}|
         <2^{1024}\gamma^r\sqrt\Delta K,\qquad0\le r\le22.
                                                               \tag{S.22}
\]
每阶仍使用它自身的 \(\gamma^r\)，不能把所有阶都先替换为
\(\gamma^{22}\) 再相乘。

核在这两行中准确为
\[
 \mathcal K=
 \frac{\gamma}{a^2}\mathcal Y_2^2+
 \frac{1+Q-2\lambda}{a}\mathcal Y_1\mathcal Y_2+
 \frac{(1+Q)^2/4-\lambda Q}{\gamma}\mathcal Y_1^2 .
                                                               \tag{S.23}
\]
一般 \(A\) 取两个实谱方向的完整和。系数及其所需 raw jet
小于 \(2^{40}\gamma^2/a^2\)，因为
\(\lambda=N^2/(a\Delta)\)、\(B=\Delta/a\)。
完整21阶 Leibniz 和由 (S.22) 给
\[
 \sup_I|\mathcal K_A^{(r)}|
       <2^{2200}a^{-2}\Delta\gamma^{r+2}K^2
                                    \quad(0\le r\le21).
                                                               \tag{S.24}
\]
每个实点半径 \(1/8\) 复盘上，显式 \(F^{9/2}\) 无零且
模小于 \(2^{20}\)。只对这个显式系数作 Cauchy，
前21阶 raw jet 小于 \(2^{153}\)。再作完整 Leibniz，
\[
 \boxed{\quad
     \sup_I|g^{(21)}|<G_*:=
            2^{2400}a^{-2}\Delta\gamma^{23}K^2 .
       \quad}                                                  \tag{S.25}
\]
\(2200+153+21=2374<2400\)，没有隐藏的 \(B^5\) 或
\(M^{128}\) 粗替换。

## 4. 实际 compact 方向与全部 Sym2 的共同多项式下界

统一取
\[
 \rho=\frac{\epsilon_*}{16G_*}
 =2^{-3684}a^3\ell^{41}B^{-47/2}\lambda^{-2}T^{-5}
                       \Delta^{-1}\gamma^{-23}K^{-2}<\ell/8.
                                                               \tag{S.26}
\]
在真实见证点附近向区间内移动至多 \(2\rho\)，取
\(f_0=\rho^{24}(1-((x-x_0)/\rho)^2)_+^{30}\)，并定义
\[
            \psi_A=\operatorname{sign}(g^{(20)}(x_0))
                              2^{-220}F^{9/2}f_0^{(20)} .
                                                               \tag{S.27}
\]
前篇的完整 bump 导数预算直接给 \(C^9\) 紧支、
\(\sum_{r=0}^4\|\psi_A^{(r)}\|_\infty<1\)，且
\[
 \|\psi_A^{(r)}\|_\infty\le\rho^{4-r},\qquad
 \|\psi_A^{(r)}\|_{L^1(dx)}\le2\rho^{5-r}\quad(0\le r\le4).
                                                               \tag{S.28}
\]
因为 \(F^{9/2}=B^{-9/2}Q^{9/2}\)，二十次分部积分仍准确
消去每个原 \(P/Q^{9/2}\)、\(\deg P\le19\)，尤其两个真实 phase。
同一积分连同真实 \(dt=a\,dx\) 给
\[
 \int_I\mathcal K_A\psi_A\,dt
                  >2^{-236}a\epsilon_*\rho^{25}>d_*,
\]
\[
 \boxed{\quad
 d_*=2^{-96000}a^{77}\ell^{1066}B^{-611}M^{-104}
                 T^{-130}\Delta^{-25}\gamma^{-575}K^{-50}.
       \quad}                                                  \tag{S.29}
\]
未取整 bits 为 \(236+1280+25\cdot3684=93616\)。
各幂准确为
\(a^{1+1+75}\)、\(\ell^{26\cdot41}\)、
\(B^{-(47/2)\cdot26}\)、
\(M^{-4\cdot26}\)、\(T^{-5\cdot26}\)。

完整有限凸包证明适用于所有 Frobenius 单位 \(A\)，给同一真实
方向 \(\psi_+\) 满足
\[
            \mathcal L\psi_+=(d_*/4)I,\qquad
              -iS_M^*DS_M[\psi_+]\ge d_*/(8K^2)I.
                                                               \tag{S.30}
\]
这保留两个 complex incoming 端口；没有用 rank-one 替代
完整二维正定性。该方向可依赖实际频率，但不依赖区间外解
选了哪条左/右边界线。

## 5. 同一个实际 band 盒及其半径

在 (S.29) 中用 \(M=U\) 的共同下界；它随 \(M\) 递减，因
\(T,\gamma\) 都递增。每个频率使用它自己的 (S.30) 方向。
真实 matrix Hessian 仍是
\[
 H_G=2^{30}K^4(U+B)^2.
                                                               \tag{S.31}
\]
它包含同一两个补偿 bump 的完整二阶项。原 band 的实际控制为
\[
 \Xi^{(n)}=\frac r{N_{\rm band}}\sum_{M\ {\rm in\ band}}
                   \theta_M\psi_M,\quad|\theta_M|\le1,\qquad
 r=\min\left\{2^{-n-80},
                 \frac{d_*}{2^{36}K^6(U+B)^2}\right\}.          \tag{S.32}
\]
完整 Hessian 比较给整个盒上的 generator
\[
       -iS_M^*D_{\theta_M}S_M
                 \ge D_{j,M}I,\qquad
       D_{j,M}=\frac{r d_*}{16N_{\rm band}K^2}.                \tag{S.33}
\]
所有其它保留区间的控制同时存在，且 (S.33) 对它们统一成立。

此处可以准确识别半径是哪一支。由
\(a^{77}B^{-611}=a^{688}\Delta^{-611}\)、
\(a<\delta^{3/2}\)、\(K^{-50}\le2^{-300000}\delta^{800}\)，
其余 (S.29) 因子均小于1，得到
\[
                     d_*<2^{-396000}\delta^{1832}.
                                                               \tag{S.34}
\]
\(\delta<2^{-j}\)、\(n+1<1024(j+5)\) 及 \(j\ge8193\)
于是给 \(d_*<2^{-n-80}\)。第二支还除以大于1的量，故
不是仅估计 min，而是准确有
\[
 \boxed{\quad
       r=\frac{d_*}{2^{36}K^6(U+B)^2},\qquad
       D_{j,M}=\frac{d_*^2}
                       {2^{40}N_{\rm band}K^8(U+B)^2}.
       \quad}                                                  \tag{S.35}
\]
完整共同参数半径、频率数及两端口归一都已计入。

## 6. 两个实际尺度区的全部层号费用

由 (S.3)、\(n+1<2^{10}J\)、\(n+2<2^{11}J\)，可取
\[
                   \ell>2^{-31}J^{-2}.                       \tag{S.36}
\]
以下从 (S.29) 出发，不改变 source 权或原中性层。

若 \(U\le\sqrt B\)，则
\(T\le3\Delta^2,\ \gamma\le3\Delta\)。于是
\[
 d_*>2^{-96000}3^{-705}
                a^{688}\ell^{1066}\Delta^{-1471}U^{-104}K^{-50}.
                                                               \tag{S.37}
\]
用 \(3^{705}<2^{1120}\)、\(3^{1471}<2^{2340}\)、
\(a>\delta^{3/2}/32\)、(S.36) 和 (S.2)，完整 bits 至多
\[
         96000+1120+3440+2340+33046+300000
                                    =435946<436000.
                                                               \tag{S.38}
\]
全部幂给
\[
             d_*>2^{-436000}\delta^{1832}J^{-4003}U^{-104}.
                                                               \tag{S.39}
\]
这里 \(1832=688\cdot3/2+800\)，
\(4003=1471+2132+400\)。

若 \(U\ge\sqrt B\)，记 \(\kappa_U=U^2/B\ge1\)。
有 \(T\le3\Delta^2\kappa_U\)、
\(\gamma\le3\Delta\sqrt{\kappa_U}\)。于是
\[
 d_*>2^{-96000}3^{-705}a^{541/2}\ell^{1066}
                    \Delta^{-2107/2}U^{-939}K^{-50}.           \tag{S.40}
\]
\(\kappa_U^{-835/2}\) 已准确吸收到 \(B\) 和 \(U\) 的幂。
用 \(3^{2107}<2^{3360}\)、\(5(541/2)<1353\)，
完整 bits 小于
\[
        96000+1120+1353+1680+33046+300000
                                     =433199<434000.
                                                               \tag{S.41}
\]
将半整数幂向安全侧放宽得到
\[
                d_*>2^{-434000}\delta^{1206}J^{-3586}U^{-939}.
                                                               \tag{S.42}
\]
\(M\) 在一个跨越 \(\sqrt B\) 的 band 内时仍用 \(U\) 对应的
第二种下界；没有对 band 内频率另加假设。

低区 \(U+B\le2B<2^8J\delta^{-3/2}\)，高区
\(U+B\le(1+B)U<2^7J\delta^{-3/2}U\)。
由 (S.35)、\(N_{\rm band}\le U\) 和 \(K^8=2^{48000}J^{64}\delta^{-128}\)：
\[
 \begin{array}{ll}
 U\le\sqrt B:&
 D_{j,M}>2^{-920056}\delta^{3795}J^{-8072}U^{-209},\\[2mm]
 U\ge\sqrt B:&
 D_{j,M}>2^{-916054}\delta^{2543}J^{-7238}U^{-1881}.
 \end{array}                                                   \tag{S.43}
\]
这已经是整个真实参数盒上完整 scattering 矩阵的导数，
并非仅未缩放局部核。

## 7. 原 middle 门将层号费变成固定频率幂

从 (S.5)，\(U\ge2^{-40}\delta^{-1/8}\)，故
\[
                       \delta\ge2^{-320}U^{-8}.               \tag{S.44}
\]
还可在全部 \(j\ge8193\) 上准确证明
\[
                              J<U^{1/64}.                    \tag{S.45}
\]
写 \(j=8193+512q+r,\ 0\le r\le511\)。则
\(J\le8709+512q\le8709\,2^q<2^{14+q}\)，而
\[
 U>2^{j/8-40}\ge2^{984+1/8+64q},
 \qquad (984+1/8)/64>14.
 \tag{S.46}
\]
没有用未经证明的“层号比频率慢”取代这笔费用。

将 (S.44)--(S.45) 代入 (S.43)，低区 bits 为
\[
 920056+320\cdot3795=2134456<2140000,
\]
频率幂为
\[
           8\cdot3795+209+8072/64
                           =30695+1/8<30696.                 \tag{S.47}
\]
高区 bits 为 \(916054+320\cdot2543=1729814\)，幂为
\[
              8\cdot2543+1881+7238/64
                        =22338+3/32<22339.                   \tag{S.48}
\]
所以两区共同有
\[
                       D_{j,M}>2^{-2140000}U^{-30696}.
                                                               \tag{S.49}
\]
最后用真实 \(U\le2M\)，
\(2140000+30696=2170696<2200000\)，便得到 (S.1)。
额外放宽一幂只提供安全余量，没有补偿遗漏的参数因子。

## 8. 原标签规范的确切比较与仍须继续的全空间消费

[原中性层规范](R119-supplement-original-neutral-label-common-analytic-normalization.md)
在原标签取值泛函上准确给
\[
 C_\zeta e^{-\tau_\infty M}M^{-33024}
      <N_M<C_\zeta e^{-\tau_\infty M}M^{-30960}.
                                                               \tag{S.50}
\]
因此本篇完整 generator 的逆费用在多项式阶数上低于
\(M^{30960}\)，差为
\[
                            30960-30697=263.                 \tag{S.51}
\]
这只是同一对象的两个已证数值阶数的比较。
generator 下界、谱平均所得 resolvent、输入 source 的原径向
规范与实际输出两迹是不同的算子陈述；没有将它们互换。
完整网络在全部 middle incoming 上组装时应直接使用
(S.33) 的矩阵不等式，不能再无故重复一次 rank-one 到端口的
\(K^3\) 费用。

零模不属于上述 scattering 控制。两个真实 mean、独立高度、
ordinary/weak source、bare/total flux 的端荷及当前
\(\Gamma^*\) 两列均保持第61束和原全网络的准确方程。
非径向背景的 profile generator 还包含实际
\(\widehat z\) 响应和两条 physical characteristic 图的变分。
尚未证明它在全部混合频率簇上继承 (S.1)，也未将
\(\rho^5\) 的绝对误差免费除以本篇 \(\rho^{25}\) 的 pairing。

[必要有限阶代数与有理预算](../scripts/fourfold_scale_correct_polynomial_middle_generator_20261114.py)
及[实际执行记录](../notes/2026-11-14-R119-scale-correct-polynomial-middle-generator-budget.json)
保存缩放恒等式、真实首行 \(B^2\)、全部幂及实际 middle 转换。
全频、全层和完整参数盒结论由上述证明给出，不由有限采样替代。
