# R133：固定第四 connector 的真实控制误差、全频好角重建与完整外端口

**状态：已证明。** 固定第47束某个基准参数的完整 connector，
包括最后 $q=-1$ 段的停止长度；随后允许第53束的整个真实控制盒。
本篇把它产生的 cut128 第四物理斜率误差，经过**同一个不再重停的
connector**、真实双 bump 和未改长段，传到当前 $R=25/8$。
第四线无需精确等于 $-4\omega$。

还对这个新对象重新证明全频 good-angle 的非空与测度界。
旧 good parameter 和旧 retuned 尾的 $\mathsf D_0^{-1}$ 均不直接
转授：后者仍须以新 fixed-stop 的 raw 标签/完整源/两迹重新接入。
本篇不证明新的 nonlinear regular 方程或主体全 BVP 已解。

## 1. 实际新对象和准确切口误差

固定[第47束双参数实际尾](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
中任一实基点 $\Gamma^0=(\gamma_1^0,\gamma_2^0)$。用其真实第四线
按原构造选择一次 connector 的停止长度 $\ell^0$，之后固定完整
$q(v)$、所有短 quintic、$H_e,\omega_e$、$\rho$ 和
$\epsilon_{\rm tail}$。这里 $v=\log(H/H_{\rm start})$ 是 connector
坐标，不是主体的 reciprocal 未知函数。

安装
[第53束真实控制 profile](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
的完整参数 $\Pi=(\Gamma,s,\Xi)$：

\[
 \|\gamma_1\|_\infty<2^{-16},\quad
 \|\gamma_2\|_\infty<2^{-30},\quad
 |s_{j,k}|<1/16,\quad
 \|\Xi_{j,k}\|_{C^4}<2^{-21},\qquad j\ge8193.
 \tag{F.1}
\]

控制 $s,\Xi$ 不改前8192层。$\Gamma$ 可以改变浅层，但其费用必须
分别付。第53束 C.36 给的是 cut128 **物理高度**对数斜率，

\[
 |d_{4,\Pi}-d^{47}_4(\Gamma)|<2^{-193532},\qquad
 14<d_{4,\Pi}<15.                                      \tag{F.2}
\]

它不是 $\lambda_4/\omega$。第47束 U.17 给两条不同的真实导数界，

\[
 \|D_{\gamma_1}d^{47}_4\|<2^{-22},\qquad
 \|D_{\gamma_2}d^{47}_4\|<2^{-8}.                       \tag{F.3}
\]

故相对固定基点，

\[
 |d_{4,\Pi}-d^{47}_4(\Gamma^0)|\le\varepsilon_d,\quad
 \varepsilon_d=
 2^{-193532}
 +2^{-22}\|\gamma_1-\gamma_1^0\|_\infty
 +2^{-8}\|\gamma_2-\gamma_2^0\|_\infty
 <2^{-35}.                                            \tag{F.4}
\]

两个实盒的直径分别是 $2^{-15},2^{-29}$，所以两项都最多
$2^{-37}$。如果整个前缀 $\Gamma$ 固定，则可直接用
$\varepsilon_d=2^{-193532}$。不能将第55束
$\Gamma^*(a,\Omega)$ 的浅层变化塞进深层屏蔽指数。

所有 profile 参数在 cut128 的值和既有 jets 恒定。固定
$\rho=1/(H_e b)$、
$\epsilon_{\rm tail}=1/(4H_e\omega_e\bar W_b)$ 后，新实际背景在
切口仍与原 connector 完整 $C^2$ 相接。现在无需借重停的
$H_e\omega_e$ 抵消，因为这两个量根本没有变化。有限 body、
natural graft、$a_*,z_*,\omega$ 及 $[0,B]$ 都不变。

所有界同时覆盖真实
$\delta=-7789843107295549/4611686018427387904+\eta$、
$|\eta|\le10^{-9}$。该完整区间严格包含于 R74 (74.1) 的已付入口域；
有理程序核验两个准确中心之差加 $10^{-9}$ 小于 $1/2000000$。
主体 $\nu$ bump 在 $r\ge.18$ 为零，不改变这里的入口。
后文 uniform 常数不以单个 $\eta$ 点代替这个区间。

## 2. 固定 connector 的全程反向估计

沿用[R11 的实际变量](R11-matched-mode-four-physical-tail-connector.md)
和[原真实 connector](R119-supplement-retuned-fourth-connector-and-common-bumps.md)。
第四 Sturm 投影为

\[
 \mathcal R=\frac{y'}{16\omega y}
           =\frac{1-d_4}{16-d_4},\qquad
 \mathcal R_v=q(1-\mathcal R)+1-16\mathcal R^2.         \tag{F.5}
\]

两端 $d_4\in(14,15)$，所以

\[
 |\Delta\mathcal R_e|
 \le 15|\Delta d_4|.                                  \tag{F.6}
\]

基准全轨迹满足 $-14<\mathcal R^0\le-1/6$；
connector 始终有 $-8\le q\le2$。在共同管
$-15<\mathcal R<-1/8$ 内，两条同方程轨迹的差满足

\[
 (\Delta\mathcal R)_v
 =[-q-16(\mathcal R+\mathcal R^0)]\Delta\mathcal R,\qquad
 -q-16(\mathcal R+\mathcal R^0)\ge2.                   \tag{F.7}
\]

因此反向走时差不放大。以 $\varepsilon_d\le2^{-12}$ 作宽松 bootstrap，
$15\varepsilon_d<1/24$，且小于1，故扰动不会先碰到管的任一边界。
反向解在整个已固定有限 connector 存在；其 $y$ 不为零，因为
有限 $\mathcal R$ 给通常的标量指数方程。于是

\[
 |\mathcal R(T)-\mathcal R^0(T)|\le15\varepsilon_d,
 \qquad
 \frac{|\lambda_4(T)+4\omega|}{4\omega}
 \le60\varepsilon_d.                                  \tag{F.8}
\]

使用了 $\mathcal R^0(T)=-1/4$。
没有用一段理想常系数替代 preparation、放大段或最后短过渡；
(F.7) 支付全部同一真实 $q(v)$。

## 3. 同一个双 bump 曲线上的真实新第四线

保留基准第47/R74 的曲线 $s_0(\gamma_0 t)$，
$\gamma_0=2^{-17}$、$0\le t\le1$。它使**基准**第四线在
$B=2^{24}-25/8$ 回到 $(1,-\omega)$，并满足

\[
 s_0'=-K^0_{4,2}/K^0_{4,1},\qquad
 0<K^0_{4,2}/K^0_{4,1}<1/64.                          \tag{F.9}
\]

该已知曲线现在只是一个固定的真实背景参数曲线，
不声称它使新第四线精确不变。

R74 的实际 bump 给
$|\psi'|\le15/16384,\ |\psi''|\le3/16$、
$7/5<\omega<3/2$，故

\[
 (5/4)^2<\widetilde h''/\widetilde h
   =(\omega+\psi')^2+\psi''<(8/5)^2.                  \tag{F.10}
\]

令 $p=-y_4'/(4y_4)$，向左变量 $\tau=T-u$ 下

\[
 p_\tau=4(\widetilde h''/\widetilde h-p^2).
\]

(F.8) 和 $\varepsilon_d\le2^{-12}$ 使新旧初值都严格在
$[5/4,8/5]$；(F.10) 保持这个不变区间。两条轨迹的差满足
$\Delta p_\tau=-4(p+p^0)\Delta p$，再次不放大。因此对整个曲线，

\[
 p_{\rm new}(B)\in[5/4,8/5],\qquad
 \frac{|\lambda_4(B)+4\omega|}{4\omega}
 \le60\varepsilon_d.                                  \tag{F.11}
\]

新第四方向始终远离增长线：
\[
 \sin\angle((1,-p),(1,\omega))
 =\frac{p+\omega}{\sqrt{(1+p^2)(1+\omega^2)}}>1/2.
 \tag{F.12}
\]
这是实际方向的界，不是把新第四 mode 当成旧 exact-zero 方向。

## 4. 为新 fixed-stop 对象重新证明全模好角

新真实尾图在零标签处对每个 $m\in4\mathbb N$ 给非零齐次允许线。
经固定 connector 传至 $T$ 后仍非零；二阶唯一性排除零向量。
该线与外 bump 参数 $(s,t)$ 无关，因为两端完整 jet 固定，后方
只发生参考高度平移。

对每个新 $m\ge8$ 的线，在其左端归一化，R11 附录 A 的准确变分
仍是
\[
 D_m=(y_m'-\widetilde\omega y_m)^2+
       (m^2-1)(-\widetilde V)y_m^2,\quad
 K_{m,i}=2m\int\phi_iD_m,\quad \partial_i\theta_m=-K_{m,i}.
\]

当新线落在增长目标 $(1,\omega)$ 的坏角邻域内，同一真实正势盒
给该新解的正向 Riccati 锥，故原 A.10 前的估计重新成立：
$K_{m,1}/K_{m,2}<1/256$。沿**固定基准曲线** (F.9)，

\[
 \theta_m'(t)
 =-\gamma_0K_{m,2}
  +\gamma_0K_{m,1}K^0_{4,2}/K^0_{4,1}
 \le-\gamma_0m^3\ell_b/32,\qquad\ell_b=1/16.            \tag{F.13}
\]

这里使用的是基准第四曲线的已证导数比，以及**新解**自己的
$K_{m,i}$；没有将两者混成新第四匹配曲线。

每模参数角值域及坏区间穿越数仍按 R11 附录 A 的
$8m(25/8)$ 和 $3m(25/8)+2$ 支付，输入右线仅需非零且与 $t$ 独立。
全部 $m\ge8$ 的坏集之和不超过原对更大频率集的完整和
$1328\epsilon_*/(\gamma_0\ell_b)$。
新 $m=4$ 由 (F.12) 从来不坏。取 $\epsilon_*=2^{-39}$ 得新的闭好集

\[
 |G_\Pi^{\rm fixed}|\ge1-83/16384>0.                  \tag{F.14}
\]

这是真正对新允许线的重证。旧选中的 $t$ 不能直接沿用；必须为
新 $\Pi$ 选 $t\in G_\Pi^{\rm fixed}$。不声称这个选择随所有参数连续。
两帽若为同一对象的反射，可取同一个 $t$。
局部控制导数若要求固定外 bump 参数，也不能对这个尚无连续性定理的
选择函数擅自求导。

## 5. 未改长段的准确筛选及全模 regular 线

写 $\lambda=\lambda_4(B)$，
$e_B=(\lambda+4\omega)/(4\omega)$。在未改
$0\le u\le B$ 上，准确增长/衰减系数比为

\[
 \rho_B=\frac{e_B}{2-e_B},\qquad
 \rho_0=e^{-8L}\rho_B,\qquad
 \frac{\lambda_4(0)+4\omega}{4\omega}
       =\frac{2\rho_0}{1+\rho_0},\quad L=\omega B.
\]

由 $|e_B|\le60\varepsilon_d<1/8$，

\[
 \boxed{\frac{|\lambda_4(0)+4\omega|}{4\omega}
           \le240\varepsilon_d e^{-8L}.}             \tag{F.15}
\]

同 $\Gamma$ 时右端小于 $2^{-193524}e^{-8L}$；
整个真实两参数盒时小于 $2^{-27}e^{-8L}$。
这是当前 fixed-stop 候选的实际第四线费用。

对 (F.14) 的新好参数，其余每个模从自己的新线出发，在同一未改长段
重复 R74 的完整两指数换算，得到

\[
 |\lambda_m+m\omega|<2^{41}m\omega e^{-2mL}
 \quad(m\in4\mathbb N).                               \tag{F.16}
\]

(F.15) 比其中第四模的要求更强，但第四误差保持非零。
负频率用实共轭。定义真实曲率乘子
\[
 q_m=-\frac{\lambda_m}{m\omega\sqrt{1+w_R^2}},
 \quad q_*=(1+w_R^2)^{-1/2}.
\]
于是所有模，包括未保留物理高模，都满足
\[
 |q_m-q_*|<2^{-512}.                                  \tag{F.17}
\]
$L>(7/5)(2^{24}-25/8)>2^{24}$，用 $e>2$ 即支付
$(2^{42}+8)e^{-8L}<2^{-512}$；没有把指数下溢当作零。
当前 dyadic proposal 的原真费用加 (F.17) 仍小于 $10^{-17}$。

## 6. 真实完整两迹、普通源与参数变化

同一 $R=25/8$ 的真实 grounded 迹保持 R74 的完整矩阵：
\[
 v=A_0y-\frac4{m^2}y',\qquad p=-y+\frac4{A_0}y',
 \quad A_0=4\omega+a_*^2/z_*.
 \tag{F.18}
\]
对 $(y,y'/m)$ 的行列式为 $4m(1-m^{-2})$；第四模准确是15。

对 ordinary metric 源，必须使用
\[
 v=A_0\eta-\frac4{m^2}\eta'+\frac4{m^2}J,\qquad
 p=-\eta+\frac4{A_0}\eta'+\frac{8h^2}{A_0^2}R_m.       \tag{F.19}
\]
$J,R_m$ 两个端点项均保留。若 $\eta(0)=1$、同一 $J,R_m$，
第四齐次方向变化 $\Delta\lambda_4$ 给
\[
 \Delta v=-\Delta\lambda_4/4,\qquad
 \Delta p=4\Delta\lambda_4/A_0.
 \tag{F.20}
\]
将 $e_0=|\Delta\lambda_4|/(4\omega)$ 代入，
$|\Delta v|\le(3/2)e_0,\ |\Delta p|\le4e_0$。
这不是只付一个 slope 而丢掉另一迹。

真 DN
\[
 g_m=\frac{1-4\lambda_m/A_0}{A_0-4\lambda_m/m^2}
\]
满足同一正型界 $m/7<g_m<m/5$。两条负 $\lambda_4$ 之间，
\[
 |\Delta g_4|
 \le\frac{75}{112}\frac{|\Delta\lambda_4|}{4\omega}.
 \tag{F.21}
\]
这是从准确分式微分所得，而非把 grounded flux 当成 raw 高度导数。

完整有源边界应写成 $p+\Gamma_{\rm new}v=g_{\rm new}$。
可付的线性行变化是
$(\Gamma_{\rm new}-\Gamma_{\rm old})v$，其中 $v$ 必须含 (F.19)
的 $4J/m^2$。新尾产生的普通源/weak-source 仿射负荷
$g_{\rm new}$ 仍须按新真实两态求出；不能用齐次 (F.16) 将其设零。

固定 connector 后，控制的几何参数列在固定物理半径上为
\[
 \delta w^{\rm phys}(a)
       =D_\Pi\bar w_\Pi(a/\rho)[\delta\Pi],
 \quad \delta g_{aa}=2w^{\rm phys}\delta w^{\rm phys}.   \tag{F.22}
\]
因为 $\ell,\rho,a_e$ 固定，本方向没有旧 retune 的
$A\,\delta\ell$ 或 $w_e\delta a_e$ 项。真实 profile 微分、所有
nonmean/mean 源仍存在。若外 bump 参数 $t$ 也改变，必须另保其
真实 profile 源及高度平移；本篇没有给不连续选择的参数导数。

## 7. 同一个实际中心的 nonlinear long 行与独立 mean

当前完整最终中心的 SHA 为
ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413。
已证明全部物理频率上的
\[
 \|Z\|_{A_0}<2.532986\,10^{-13},\quad
 \|b+Q_{\rm old}Z\|_{A_0}<1.256750\,10^{-15},
\]
\[
 |C_0-C_{\rm ref}|<6.055\,10^{-43},\qquad B_0=0.
\]
这些是[原实际外端口证书](R133-supplement-final-moving-centre-actual-regular-boundary.md)
的结论；本篇不重建丢失的二进制报告，也不伪造其哈希。

(F.17) 给完整新旧乘子差至多 $2\epsilon$，$\epsilon=2^{-512}$。
取 $r_Z=10^{-12},r_B=2^{-60},r_f=10(r_Z+r_B),F=r_f+r_B$，
仍取当前实际反射类，独立 $f_B$ 的预算是物理角
$\dot A^2$ 范数（非零权 $|m|^2$，mean 另保留）。
真实未改 periodic-long 图满足
\[
 {\rm image}\le9r_Z+\epsilon r_B+9\,2^{12}F^2<r_f,
 \qquad {\rm Lip}\le36\,2^{12}F<1.
\]
它不依赖第四误差严格为零，且完整 $f_B$ 独立输入保留。按
[原第四容错端口预算](R133-supplement-regular-fourth-mode-robustness-budget.md)
的完整图表示，有
\[
 \|d_{\rm new}\|_{A_0}\le\epsilon(r_Z+r_B)+2^{14}F^2,
 \qquad |c_0|\le2^{11}F^2.
\]
因此同一个实际中心满足
\[
 \boxed{\|b+Q_{\rm new}Z-d_{\rm new}(Z,f_B)\|_{A_0}
             <1.258389\,10^{-15},}
\]
\[
 \boxed{|C_0-C_{\rm ref}-c_0(Z,f_B)|<2.048004\,10^{-19},
 \qquad B_0-B_0^{\rm long}=0.}                         \tag{F.23}
\]
归一化的主体行最后才除以原准确 $\alpha$。

在固定 $f_B$ 的同一未改 long 图中，若只是改变参考对角的表示，
准确有 $d_{\rm new}=d_{\rm old}+(Q_{\rm new}-Q_{\rm old})Z$；
故改变对角与其 remainder 必须一起处理。真实 tail 输出的
$f_B,k_B$、源负荷、mean 高度和标签响应不由这个代数抵消而消失。

固定尺度下的参考高度仍满足
\[
 Z_\Pi(a)=Z_e-\int_{a_e}^{a}w_\Pi^{\rm phys}(s)\,ds,
 \quad
 \Delta Z(a)=\Delta Z_e-\int_{a_e}^{a}\Delta w^{\rm phys}(s)\,ds.
 \tag{F.24}
\]
特别，固定外 bump/connector 高度时，平端 mean 变化是
$\rho\int_1^b\Delta\bar w_\Pi$，通常不为零。
ordinary mean 仍有 $p_0'=s_0$ 和独立高度积分常数；
weak source 应保总通量及其真实源修正。
(F.23) 的 curvature mean 不代替这些 height/flux 行。

## 8. 实际有理执行及尚未授予的接口

[新有理程序](../scripts/fourfold_regular_fixed_stop_connector_ports.mjs)
已在 functions 的 JavaScript 运行时执行，29 个门全部通过；
全部比较使用 BigInt 分数。新门覆盖两个不同的浅参数域、真实
反向管、双 bump 正势锥、第四角分离、新高模求和、真实长段、
两迹及完整实际 nonlinear 行。它不只是重跑旧19个容错门。

[完整文本报告](../notes/2026-11-14-R133-fixed-stop-connector-and-full-ports-rational.json)
记录第47、第53、R11、R74 和实际端口证明的字节身份。复现：

~~~sh
node scripts/fourfold_regular_fixed_stop_connector_ports.mjs
~~~

本篇已经为新 fixed-stop 对象支付 (F.14)–(F.17)。
新 raw404 标签列经固定 connector 形成的 $\mathsf D_{0,\Pi}$，
其完整普通/weak-source 仿射列、mean 和 nonlinear 参数依赖，
仍须在这个同一新对象重新接线；旧 retuned 的数值或标签逆不因
背景更接近而自动适用。最终
$k_B+\mathsf C_L f_B-\mathsf S_L f_*-\mathcal E_D=0$、
内部两相位条件、主体全逆、唯一公共度量和全族几何门也继续保留。
