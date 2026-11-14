# R119 续篇：同一个高频方向的第三相位与完整两端口正定性

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 在当前第53束实际允许的未使用 quartic
区间中，本篇构造一个与 Fourier 频率无关的真实 compact 方向。
它准确消去原两个 phase 的一阶变化，而使完整二维径向散射
对所有足够高的频率同时具有正定导数。这里的“足够高”有明确
的实际尺度门；不以形式 WKB 级数代替完整两行传播。

该方向仍在原 \(C^4\) profile 盒内，不改变
\(\zeta,h_j,\mathsf K\)、原标签或外部 fixed-stop 对象。
它可替换同一 unused 区间中高频 band 的控制方向选择。
没有把其径向正定性转授给非径向混合频率矩阵。

## 1. 同一个实际 ramp、两个 phase 与真正的光学变分

采用[实际多项式中频导数](R119-supplement-scale-correct-polynomial-middle-scattering-generator.md)
的 \(j\ge8193,a,\Delta,B,K,J,\delta,I,\ell\)，特别
\[
 Q=7+Bf(x),\quad f=30x^2(1-x)^2,\quad dt=a\,dx,\quad
 B=\Delta/a,\quad 80<\Delta<3J,\quad
 I\subset[7/16,15/32].
 \tag{H.1}
\]
取 \(c\) 为 \(I\) 中心、\(\rho=\ell/4\)，新支集为
\([c-\rho,c+\rho]\)，严格位于 \(I\) 内。

真实径向方程及准确密度变换为
\[
 (\mu h_t)_t+M^2\mu Qh=0,\quad \mu_t/\mu=-1-Q,\quad
 u=\sqrt\mu h,\quad s_t=\sqrt Q,\quad y=Q^{1/4}u,
\]
\[
 y_{ss}+(M^2+V)y=0,\qquad
 V=\frac{Q_t}{2Q}-\frac{(1+Q)^2}{4Q}
       -\frac{Q_{tt}}{4Q^2}+\frac{5Q_t^2}{16Q^3}.
 \tag{H.2}
\]
实际 compact profile 方向是
\(\dot{\log p_*}=\psi\)，所以 \(p:=\dot Q=-\psi_t\)。
若 \(\chi(t)=\dot s(t)=\int p/(2\sqrt Q)\,dt\)，固定光学坐标的
势变分为
\[
 v:=\dot V\big|_s=\dot V\big|_t-\chi V_s,
 \tag{H.3}
\]
\[
 \dot V\big|_t
 =-\frac{p_{tt}}{4Q^2}
  +\left(\frac1{2Q}+\frac{5Q_t}{8Q^3}\right)p_t
  +\left[-\frac{Q_t}{2Q^2}-\frac{1-Q^{-2}}4
       +\frac{Q_{tt}}{2Q^3}-\frac{15Q_t^2}{16Q^4}\right]p.
 \tag{H.4}
\]
这保留真实 \(ds\) 的变化，不把固定 \(t\) 与固定 \(s\) 的
变分混同。

两个原 phase 的变分核仍是
\[
 \phi_S=-\frac{Q_t}{4Q^{3/2}},\qquad
 256Q^{9/2}\phi_\beta
 =(12Q^4-8Q^3+12Q^2)Q_t
        +40QQ_tQ_{tt}-35Q_t^3-8Q^2Q_{ttt}.
 \tag{H.5}
\]
它们的方向约定来自原完整主旋转与首密度 phase。

## 2. 一个准确的共同第三密度方向

定义真实严格区间的局部密度泛函
\[
                         C_3=\int V^2\,ds.
 \tag{H.6}
\]
其 compact 变分不需要在本区间外作任何积分。由 (H.3) 分部
积分，或直接变分 \(V^2\sqrt Q\,dt\)，得到
\[
 \dot C_3=2\int Vv\,ds=\int\phi_3(t)\psi(t)\,dt.
 \tag{H.7}
\]
令 \(q=Q,q_r=\partial_t^rQ\)。准确的 Euler 变分核为
\[
 \phi_3=\frac{\mathcal P(q,q_1,\ldots,q_5)}{1024q^{15/2}},
 \tag{H.8}
\]
\[
\begin{split}
\mathcal P={}&240q^8q_1+192q^7q_1-96q^6q_1-320q^6q_3\\
 &+960q^5q_1q_2+192q^5q_1-128q^5q_3
       -600q^4q_1^3+640q^4q_1q_2\\
 &+240q^4q_1-320q^4q_3+128q^4q_5
       -560q^3q_1^3+2240q^3q_1q_2\\
 &-1344q^3q_1q_4-2240q^3q_2q_3
       -2520q^2q_1^3+7728q^2q_1^2q_3\\
 &+10416q^2q_1q_2^2-29568q q_1^3q_2+15015q_1^5 .
\end{split} \tag{H.9}
\]
例如这是
\(\partial_t[\partial_Q(V^2\sqrt Q)
 -\partial_t\partial_{Q_t}(V^2\sqrt Q)
 +\partial_t^2\partial_{Q_{tt}}(V^2\sqrt Q)]\)，
而非仅对 \(V\) 平方忽略光学测度。

写 \(F=Q/B\)，取
\[
 b(z)=(1-z^2)_+^{42},\qquad f_0(x)=\rho^{36}b((x-c)/\rho),
 \qquad
                 \boxed{\ \psi=2^{-400}F^{15/2}f_0^{(32)}.\ }
 \tag{H.10}
\]
这是一个真正 \(C^9\) 紧支方向。完整导数预算给
\[
 \|\partial_x^r\psi\|_\infty\le\rho^{4-r}
       \quad(0\le r\le9),\qquad
                   \sum_{r=0}^4\|\partial_x^r\psi\|_\infty<1.
 \tag{H.11}
\]
具体地，显式 \(F^{15/2}\) 在每个实点的半径 \(1/8\) 盘中
模小于 \(2^{23}\)，前九 raw jet 小于 \(2^{70}\)；
\(b\) 前41导数小于 \(2^{42}84^{41}<2^{305}\)。
完整 Leibniz 和至多另付 \(2^9\)，严格被 \(2^{400}\) 支付。

将 (H.5) 乘 \(F^{15/2}\) 后，除去固定常数的两个分子，
在 \(x\) 中次数分别至多27和31。故32次分部积分准确给
\[
                           \dot S=\dot\beta=0.               \tag{H.12}
\]
所有支集端 jets 消失，原两个补偿 bump 的一阶变化因此准确为0。

将 (H.9) 代入真实 quartic，除
\(240Q^8Q_x/a\) 外的所有项次数至多31。于是
\[
 \partial_x^{32}\mathcal P
       =\frac{240}{9a}\partial_x^{33}(Q^9)
       =\frac{240}{9a}30^9B^9\,33!\,
                     [7140x^3-10710x^2+5202x-816].
 \tag{H.13}
\]
其最后的多项式准确为
\[
           51(x-\tfrac12)\,[140(x-\tfrac12)^2-3]>3
                  \quad(7/16\le x\le15/32).
 \tag{H.14}
\]
所以这个方向同时满足严格正的完整第三变分
\[
 \boxed{\qquad
          \dot C_3>2^{-430}B^{3/2}\rho^{37}>0.
       \qquad}                                                \tag{H.15}
\]
这里 \(dt=a\,dx\) 与 (H.13) 的 \(a^{-1}\) 准确抵消，
而 \(Q^{15/2}/B^{15/2}\) 留下 \(B^{9-15/2}=B^{3/2}\)。
\(\int_{-1}^1b>2^{-18}\)，完整未取粗费用已被430 bits覆盖。
方向 (H.10) 没有任何 \(M\) 依赖。

## 3. 真实固定光学端点与完整强源预算

(H.12) 的第一式使区间两端的光学坐标及其一阶变分固定；
\(\chi\) 在支集之前、之后均为0。因此 (H.3) 的 \(v\)
真正紧支于同一个内部光学区间。原首密度 phase 的第二式给
\[
                               \int v\,ds=0.                 \tag{H.16}
\]
端点密度、normal shear 和高度/flux 恢复矩阵也固定。
这里没有把一个移动端点的 source 省去。

令 \(b_0=\sqrt B/\Delta\)。从显式 (H.2)，
在本真实区间上可统一取
\[
       |\partial_s^r V|<2^{256}B b_0^r\quad(0\le r\le6),
 \tag{H.17}
\]
\[
       |\partial_s^r v|<2^{512}(B/\Delta)b_0^r\rho^{1-r}
                                      \quad(0\le r\le3),
 \qquad \|v\|_{L^1(ds)}<2^{515}\sqrt B\,\rho^2 .
 \tag{H.18}
\]
为说明这些是实际方向的费用：\(p=-B\psi_x/\Delta\)，
其前两 \(t\) 导数依次带 \(B/\Delta\)；
(H.4) 的三项于是被
\((B/\Delta)(\rho^3+\rho^2/\Delta+\rho/\Delta^2)\) 控制。
完整 \(\chi V_s\) 也在此界内，因为
\(|\chi|\le\rho^4/\sqrt B\)。
再作至三次 \(\partial_s=b_0F^{-1/2}\partial_x\)，用 (H.11)
到六阶即可。支集光学长度小于 \(4\Delta\rho/\sqrt B\)。

对 (H.17)，只估计显式 \(F\) 及其倒数：
半径 \(1/8\) 的盘上 \(1/4<|F|<8\)，
\[
 V/B=F'/(2\Delta F)-H^2/(4F)
          +5(F')^2/(16\Delta^2F^3)-F''/(4\Delta^2F^2),
 \quad H=F+1/B .
 \tag{H.19}
\]
它的盘上界小于 \(2^{32}\)；在依次缩小的盘上应用
\(F^{-1/2}\partial_x\) 六次，额外费用小于 \(2^{80}\)。
256和512的余量覆盖所有实际乘积和坐标导数。

## 4. 完整两行 WKB 比较，不只形式相位

本节采用明确的实际高频门
\[
               \boxed{\quad M\ge2^{4096}\rho^{-64}\sqrt B.\quad}
 \tag{H.20}
\]
置 \(k(s)=\sqrt{M^2+V(s)}\)，取正实支，\(\theta_s=k\)。
由 (H.17)、(H.20)，有 \(M/2<k<2M\)。
对真实 optical canonical 两行
\(Z=(\sqrt M\,y,y_s/\sqrt M)\)，定义完整实 WKB 矩阵
\[
 W(s)=
 \begin{pmatrix}
 \sqrt{M/k}\cos\theta&\sqrt{M/k}\sin\theta\\
 -\frac{k_s}{2k\sqrt{Mk}}\cos\theta-\sqrt{k/M}\sin\theta&
 -\frac{k_s}{2k\sqrt{Mk}}\sin\theta+\sqrt{k/M}\cos\theta
 \end{pmatrix}.
 \tag{H.21}
\]
\(\det W=1\)，且 \(\|W\|,\|W^{-1}\|<2\)。
令真实 fundamental matrix \(\mathcal U\) 在区间中心满足
\(\mathcal U(c)=W(c)\)。准确残差是
\[
 W_s-AW=(R/M)e_{21}W,\qquad
 A=\begin{pmatrix}0&M\\-M-V/M&0\end{pmatrix},
 \quad R=(k^{-1/2})_{ss}/k^{-1/2}.
 \tag{H.22}
\]
完整两行 Duhamel 在 \(W\) 框架中给
\[
 \int_I4|R|/M\,ds<2^{520}(\sqrt B/M)^3,\qquad
                \|\mathcal U-W\|_\infty
                       <2^{523}(\sqrt B/M)^3.
 \tag{H.23}
\]
例如 \(|R|<2^{512}B^2/(\Delta^2M^2)\)，
整个 \(I\) 的光学长度小于 \(8\Delta\rho/\sqrt B\)。
指数余项小于2；上下两行及其真实初值均被比较。

完整变分 Green identity 在固定光学端点给 profile 二次型
\[
                \mathcal L_\psi[\xi]=-\int_Iv(s)|y_\xi(s)|^2ds,
 \tag{H.24}
\]
其中 \(y_\xi\) 是 (H.23) 的真实解。它与原 raw kernel
\(\int\mathcal K_h\psi\,dt\) 准确相同；端点的 determinant-one
变换和它们的 profile 一阶变化都已在 §3 固定。

先用 (H.21) 的完整两行解代入。所得二次矩阵是
\[
 -\frac12\int v/k\,ds\, I
 -\frac12
 \begin{pmatrix}
 \Re I_{\rm osc}&\Im I_{\rm osc}\\
 \Im I_{\rm osc}&-\Re I_{\rm osc}
 \end{pmatrix},
 \qquad I_{\rm osc}=\int(v/k)e^{2i\theta}\,ds .
 \tag{H.25}
\]
由 (H.16)，真实 scalar 部分为
\[
             -\tfrac12\int v/k\,ds
             =\frac{\dot C_3}{8M^3}
                  +O(2^{1540}B^{5/2}\rho^2/M^5).
 \tag{H.26}
\]
这是 \(k^{-1}=M^{-1}-V/(2M^3)+O(V^2/M^5)\) 的真实 Taylor
余项，包含光学势的完整 material 变分 \(v\)。

因为 \(v\) 及所需端 jets 消失，可对 \(I_{\rm osc}\)
完整分部积分三次。每步用
\(e^{2i\theta}=(2ik)^{-1}\partial_s e^{2i\theta}\)，
将导数留在实际 \(v,k\) 上。由 (H.17)--(H.18)，
\[
                   |I_{\rm osc}|
                 <2^{2048}B^2/(M^4\rho).
 \tag{H.27}
\]
三个完整导数项的阶数由
\(\|v_{sss}\|_1/M^4\) 控制；其它项多一个
\(B/M^2\) 或已付的 \(k_s/k\)。没有把 oscillatory 积分
仅用其高度行估计，也没有丢弃其两个实矩阵分量。

(H.18)、(H.23) 把从 WKB 解换回真实解的费用控制为
\(2^{1044}B^2\rho^2/M^4\)。
连同 (H.26)--(H.27)，完整二次矩阵误差小于
\[
                       2^{2100}B^2/(M^4\rho).
 \tag{H.28}
\]
相对于 (H.15) 的主项，其比小于
\[
 2^{2533}(\sqrt B/M)\rho^{-38}
       \le2^{2533-4096}\rho^{26}<1/2.
 \tag{H.29}
\]
故对所有实或复杂两行初态 \(\xi\)，
\[
             \mathcal L_\psi[\xi]
                  >2^{-434}B^{3/2}\rho^{37}M^{-3}|\xi|^2.
 \tag{H.30}
\]
这已经是完整两行的严格不等式，而非形式第三 phase 系数。

## 5. 真原 wave 端口及两个 complex incoming

原区间中心 wave state 为
\(Y=(\sqrt{k_7}u,u_t/\sqrt{k_7})\)，
\(k_7=\sqrt{7M^2-16}\)。到真实 \(Z\) 的 determinant-one
转换是
\[
 Z_1=\sqrt{M/k_7}Q^{1/4}Y_1,\qquad
 Z_2=\sqrt{k_7/M}Q^{-1/4}Y_2
       +\frac{Q_t}{4Q^{5/4}\sqrt{Mk_7}}Y_1 .
 \tag{H.31}
\]
由 \(B<Q<2B,\ |Q_t|<2B^2/\Delta\) 及 (H.20)，该转换及其
逆的 norm 平方小于 \(16\sqrt B\)。再用
\(\xi=W(c)^{-1}Z(c)\)，得到
\[
              \mathcal L_\psi[Y(c)]
                 >2^{-440}B\rho^{37}M^{-3}|Y(c)|^2.
 \tag{H.32}
\]
真实完整窗的双向 Cauchy \(K\) 给 incoming
\(x=(a_L,b_R)\) 与中心状态之间
\(|x|^2\le2K^2|Y(c)|^2\)。原准确 scattering Green identity
遂给
\[
 \boxed{\quad
       -iS_M^*DS_M[\psi]
                >2^{-512}B\rho^{37}M^{-3}K^{-2}I_2 .
       \quad}                                                  \tag{H.33}
\]
实部、虚部分别消费 (H.30) 即得完整 complex 空间的式子。
它不要求特征相位简单，也不假设两个端口之一很小。
原两个 phase 的有限补偿仍使用真实两 bump 图；
它们的一阶项已因 (H.12) 准确为0。

## 6. 同一方向控制整个实际高频 band 盒

对一个 band \(M\in[U/2,U]\)，若其最小频率满足 (H.20)，
同一个 (H.10) 同时满足 (H.33)。无需给每个频率分配独立
方向或再除 \(N_{\rm band}\)。
定义
\[
 d_U=2^{-512}B\rho^{37}U^{-3},\quad
 r=\min\{2^{-n-80},d_U/[2^{36}K^6(U+B)^2]\},\quad
                         \Xi^{(n)}=r\theta_n\psi,\quad|\theta_n|\le1.
 \tag{H.34}
\]
用原真实 matrix Hessian
\(2^{30}K^4(U+B)^2\)，整个盒上有
\[
        -iS_M^*D_{\theta_n}S_M>D_{j,M}^{\rm com}I,\qquad
                     D_{j,M}^{\rm com}=\frac{r d_U}{16K^2}.
 \tag{H.35}
\]
旧的其它区间可以同时存在；这里只将当前 band 的一个
真实参数归零作比较。共同方向仍属于第53束相同的完整 profile
盒；这是一种新的允许方向选择，不把已选旧参数的数值自动移来。

原 dyadic band 按递增编号给 \(U\ge2^n\)。
(H.20) 又给 \(B/U^2<2^{-8192}\rho^{128}\)，故
\(d_U<2^{-n-80}\)，半径准确取第二支。
由于 \(U\ge\sqrt B\)，\(U+B\le2\sqrt B\,U\)，因此
\[
             D_{j,M}^{\rm com}>
                    2^{-1066}K^{-8}B\rho^{74}U^{-8}.
 \tag{H.36}
\]
真实 \(\rho=\ell/4>2^{-33}J^{-2}\)、
\(B>\delta^{-3/2}\) 给
\[
             D_{j,M}^{\rm com}>
                    2^{-51508}\delta^{127}J^{-212}U^{-8}.
 \tag{H.37}
\]
高频门还给比原 middle 更强的
\(\delta>U^{-4/3}\)，而原真实 \(J<U^{1/64}\) 仍成立。
所以完整费用的频率幂小于
\[
                  4\cdot127/3+8+212/64
                           =180+31/48<181 .
 \tag{H.38}
\]
最后用 \(U\le2M\)，得到共同的安全整数界
\[
 \boxed{\qquad
             D_{j,M}^{\rm com}>2^{-52000}M^{-182}.
       \qquad}                                                \tag{H.39}
\]
它仅用于明确满足 (H.20) 的 band；其余实际 middle 保留第64束
的全模下界，没有扩大此高频门的权限。

## 7. 两个 mean、全部源与非径向簇的真实剩余

本篇始终 \(M\ne0\)。零模仍携带两个真实 mean、独立高度、
mean 电阻与 holonomy 行。ordinary/weak 源仍使用第61束
总通量方程以及实际端点 \(F^t\) 的电荷；本篇 homogeneous
二次型没有消去任何 source 列。

原非径向 Jacobi 系统的 compact profile 变分还含
\(\widehat z\) 背景响应，以及两条 physical principal 端图。
即使 (H.10) 在径向参考准确消去原两 phase，其非径向裸
pullback 导数仍不能作为同阶小算子。
要在实际混合频率近共振簇上消费 (H.33)，仍须把这些图变化
以真实共轭及完整参数导数接入，并支付剩余的相位/振幅项。
本篇没有由径向实性宣称非径向 order \(-2\) residue 自动为0，
也未将 \(\dot C_3\) 单独称作完整两根网络的第三相位。

新增结论是一个与 \(M\) 无关、准确保持原两 phase 的实际
profile 方向，以及它在明确高频门下的完整两态、两端口
正定导数。它避免为每个高频再次构造极窄的 \(\rho_M\) 控制。

[必要准确代数及有理预算](../scripts/fourfold_common_third_phase_two_port_20261114.py)
与[实际执行记录](../notes/2026-11-14-R119-common-third-phase-two-port-budget.json)
保存完整 Euler 核、32次消去、真实端口和全部指数费用。
