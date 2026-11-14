# R119 续篇：实际非径向完整余项与真两端口网络高块

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇在第50束的同一个实际双参数选择后，支付
第49束尚未量化的完整非径向返回余项。对 \(|s|\le1\)，每个完整内部
负分量的实际两端口行有
\[
 \|\mathcal E_i:H^s(\text{相邻全部端口})\to H^{s+4/3}\|
 <C_i,\qquad C_i=2^{20000}(j+5)^{64}\delta_j^{-100}.         \tag{H.1}
\]
两个正型 cross、全部 Fourier lag、跨锥、低模和 mean 列包含在此界中。
它由全空间 Duhamel 和完整输出 Sobolev 界证明，**没有**把低频输入的
截断误当作输出已平滑。

由固定的真实 \(\omega_i,\beta_i^0\)，在
\[
 T_i=2^{65536}(j+5)^{204}\delta_j^{-320},\qquad
 P_{H,i}=\mathbf1_{\{|m|\ge T_i\}},                         \tag{H.2}
\]
上，真正非径向全网络高块的反馈 norm 小于 \(2^{-1024}\)。
其它全部模式、两个 mean、最外截断分量及 source 是完整外输入。
本篇不称这个高块为全网络 inverse；移动中频 Schur 和最终外方程
\(\mathcal F_c=0\) 仍是继续任务。

## 1. 同一个背景、固定主模型与函数空间

使用
[真实联合参数选择](R119-supplement-joint-actual-principal-and-beta-selection.md)
的 \(\Gamma^*(a)\)，
\[
 \|a\|_{224}<2^{-262148},\qquad
 \mathcal X(a)=16\|a\|_{224}\le2^{-262144}.
\]
该背景已经准确满足真实 principal return 的 \(\omega_i\) 和
[首密度相位](R119-supplement-actual-nonradial-first-density-phase.md)
的 \(\beta_i^0\)，两者就是原第46束的固定目标。
不更换 profile、有限 connector、外 \(t_0\) 或最外分量。

物理角为 \(\theta\in\mathbb T_{\pi/2}\)，\(m=4n\)。
\(H^s\) 使用 \(\langle m\rangle^s=(1+m^2)^{s/2}\)；
端口是原完整 Airy incoming/outgoing 两行。
mean 使用原固定 mean Airy 两列，权为1，从不代入 \(1/m\)。
每条返回行的相邻端口数至多8。下文的范数包括这些全部输入列。

取较深胞元号 \(j\)、\(J=j+5\)，仍记
\[
 N_j=2^{184}h_j^{-5}{\zeta_j\over\mu_j\delta_j^2},\qquad
 N_j^\#=N_j+\mathbf1_{j\ge130}N_{j-1}.
\]
已有真实
\[
 \sum_{j\ge129}(K_j^{\rm ref})^2N_j<2^{160000},\qquad
 K_j^{\rm ref}=2^{5000}(j+4)^5\delta_j^{-10}                 \tag{H.3}
\]
包含两个全局 inverse 因子及全部129--8192前缀。

以下同时使用全部完整 Cauchy 窗 \(|r|\le4\)，只在最后声称
\(|s|\le1\) 的 \(4/3\) 阶余项。所需输出最高是
\(s+3\le4\)。严格密度态的指数相差 \(-1/2\)，仍准确位于原
\([-9/2,7/2]\) 窗中。没有从径向逐模门推导非径向输出增益。

本篇所用完整窗口与实际源变换分别见
[严格密度 Cauchy](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)、
[联合解析根](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)、
[根图到原径向两端口](R119-supplement-actual-root-graph-to-fixed-radial-two-port.md)、
[正型 DN 到完整 Airy Cayley](R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md)
及[同一参考的全频 Cauchy](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)。
这里重新支付新的有限算子复合费用，不调用其它度量的数值常数。

## 2. 一个全层实际角费用，含两个真实参数的改变

第50束逐行逆 \(|\varphi_i'|<2^{10}\) 及其 (J.15)--(J.17)
同时给比全局 sup 更有用的真实逐行界：
\[
 |s_i^*(a)|+
 |\gamma_{1,i}^*(a)-\gamma_{1,i}^0|
 <2^{158}J^3\delta_j^{-17/4}N_j^\#\mathcal X(a).            \tag{H.4}
\]
这里第二项包含径向主角保持曲线的 \(|\chi_i'|<2\) 和实际第一 KAM
的完整逐行修正；不是把其余层固定后的偏导。

两 compact bump 的部分光学位移至多
\(2\sqrt{\eta/\Delta}(|\delta\gamma_1|+|\delta\gamma_2|)\)；
它只改变径向平移，不产生角导。完整 ray 的非径向位移、真实 KAM
端图和根图原有角域仍有至少固定正余宽。
在较窄宽 \(1/128\) 上，所有本篇所用至多26阶角导、root height 比、
normal shear、actual graph Jacobian，以及归一首符号的非mean部分，
可统一收费
\[
 \epsilon_i^*
 =2^{8192}J^{16}\delta_j^{-16}N_j^\#\mathcal X(a).          \tag{H.5}
\]
说明这一宽包络的组成如下：

* 原严格 \(\kappa\) 差是
  \(2^{130}J^2\delta^{-5}N_j^\#\mathcal X\) 的完整积分界；
  真实 flow 导数和端角的额外因子只需
  \(2^{128}J^4\delta^{-3/4}\)。
* root 势差为 \(2^{32}n_i\)，完整 root interaction 的相对费用小于
  \(2^{4496}n_i\)；\(n_i=4N_j^\#\mathcal X\)。
  graph 所需 \(b_e^2n_i\) 用
  \(b_e^2<2^{32}J\delta^{-9/2}\)。
* 单次26阶 Cauchy 费用小于 \(26!\,128^{26}<2^{280}\)；
  有限卷积、极化和有序两行复合再付 \(2^{512}\)。
  对首符号的 cohomological 逆还付
  \(\kappa_i^{-1}<2^{28}\sqrt j\,\delta^{-3/4}\) 和宽差的二阶 Fourier
  权，取 \(2^{64}\) 余量。最坏剩余 \(\delta\) 幂小于14。
* (H.4) 的径向改变带 \(\delta^{3/4}\) 的部分光学因子；
  正段及两个 root germ 不被 bump 改动。真实平均高度的积分另保，
  不用它冒充角小量。

这些因子都严格落在 (H.5)；26阶只用于角方向，未对 \(C^2\) 径向
接缝求26阶导。具体无限层核对可用
\[
 {2^{8192}J^{16}\delta_j^{-16}\over
                  (K_j^{\rm ref})^2}
 <2^{-1800}J^6\delta_j^4<1
\]
（对 \(j\ge129\)，\(J^6<2^{j/2}\)），邻胞与有限端口计数后得到
\[
                    \sum_i\epsilon_i^*
                  <2^{160032}\mathcal X(a)<2^{-102112}.   \tag{H.6}
\]
所以以下真正角乘子、full pullback 和参数图的有限常数有统一余量。
这里没有估计裸同宽 \(C_H-I\)；实际图始终准确保留。

## 3. 严格区的完整 order-two 跨支恒等式

采用真实密度篇的
\(\Lambda,\kappa,\nu=\sqrt Q\,v,d\)，以及真实
\(H_\sigma,S_\sigma=H_\sigma^{-1}\)。
先在物理角写 \(D=-i\partial_\theta\)，
\(\mathcal D_H=M_{H'}C_H\)，prime 仅表示角导。
两个 mean 的完整恢复仍是
\[
 w=c+\alpha(S_+-S_-)
       -i\sum_\sigma C_{S_\sigma}D^{-1}Z_\sigma,
 \qquad \langle Z_\sigma\rangle=0.                        \tag{H.7}
\]
所有投影固定在原位置。

对 \(\tau=-\sigma\)，跨支 generator 为
\[
 K_{\sigma\tau}
 ={i\sigma\over2}\Pi_0\mathcal D_{H_\sigma}
                  M_\kappa C_{S_\tau}D^{-1}\Pi_0.
\]
记 \(J_\tau=H_\tau'\)、\(R=\kappa/\nu\)，定义完整算子
\[
 L_{\sigma\tau}
 =-\frac14\Pi_0\mathcal D_{H_\sigma}M_R
                   C_{S_\tau}M_{J_\tau}D^{-2}\Pi_0 .
\]
准确求导，而不作符号近似，得
\[
 \boxed{\quad K_{\sigma\tau}=\partial_tL_{\sigma\tau}
                                      -Z_{\sigma\tau},\quad}       \tag{H.8}
\]
\[
\begin{split}
 Z_{\sigma\tau}={}&-\frac14\Pi_0\mathcal D_{H_\sigma}
 M_{R_t+(-d-\sigma\nu)R_\theta-2d_\theta R}
                      C_{S_\tau}M_{J_\tau}D^{-2}\Pi_0\\
 &+\frac{\sigma}{2}\Pi_0\mathcal D_{H_\sigma}M_\kappa
                    C_{S_\tau}M_{J_\tau'/J_\tau}D^{-2}\Pi_0 .
\end{split}                                                       \tag{H.9}
\]
核对关键因子：
\[
 (S_\tau\circ H_\sigma)_t
 =-{2\sigma\,\nu\circ H_\sigma\over
                       J_\tau\circ S_\tau\circ H_\sigma}.
\]
它微分 \(D^{-2}\) 的复合时给 \(iD^{-1}\)，恰产生
\(i\sigma/2\)。另外两项来自两个真实 Jacobian 的导数。
这也解释两个跨支的 \(L\) 都取同一个负号。

在每个光滑径向片，原 \(P,K\) 方程及角 Cauchy 给前三阶径向状态
导数的充分包络
\[
 C(1+Q)n_i,\quad
 C[(1+Q)^2+|Q_t|]n_i,\quad
 C[(1+Q)^3+(1+Q)|Q_t|+|Q_{tt}|]n_i,\qquad C=2^{256}.
\]
证明只需对原一阶方程求导三次，逐次把角宽4降至3、2、1：
真实分母 \(J,D\) 仍大于 \(1/2\)，每次 Fréchet 导数的商式费可取
\(2^{40}\)，最后的有限角导费用也在 \(2^{256}\) 内。
参考密度满足 \((\ell_0)_t=-1-Q+Q_t/(2Q)\)；
其后续导数最多用 \(Q_{ttt}\)。
把已付
\[
 q>1/16,\quad |Q|<2^{12}J\delta^{-3/2},\
 |Q_t|<2^{18}J\delta^{-3},\
 |Q_{tt}|<2^{26}J\delta^{-9/2},\
 |Q_{ttt}|<2^{40}J\delta^{-6}
\]
代入完整 \(\kappa\) 商式及 (H.9)，包括全部至多32片的真实跳幅，
足以取
\[
\begin{split}
 &\sup_t\|L(t):H^r\to H^{r+2}\|
       +\int\|Z(t):H^r\to H^{r+2}\|dt\\
 &\hspace{25mm}<2^{1024}J^{12}\delta^{-24},\\
 &\int\|K_{\rm all}(t):H^r\to H^{r+1}\|dt
       <2^{512}J^8\delta^{-16}                              \tag{H.10}
\end{split}
\]
对非mean块成立；完整 mean 块在下一段作为真正平滑有限维列保留。
这些界刻意宽放。最高代数分母只用 \(q^{-9}\)，最高径向乘积是
\(Q_t^3\)，给 \(\delta^{-9}\)；显示的24、16幂已涵盖所有复合与片长。

在每个固定正/负 \(\theta\)-锥中，令
\(\widetilde Z_\sigma=|D|^{-1/2}Z_\sigma\)。
同支 generator 准确为
\[
 {i\sigma\varepsilon\over2}
 |D|^{-1/2}\Pi_\varepsilon
 M_{H_\sigma'\kappa\circ H_\sigma}
 \Pi_\varepsilon|D|^{-1/2},\qquad \varepsilon=\operatorname{sign}m.
                                                                    \tag{H.11}
\]
实背景下它反自伴。其径向标量平均
\(\langle H_\sigma'\kappa\circ H_\sigma\rangle=\langle\kappa\rangle\)
可以准确酉移走，不把这真平均换成背景平均。
剩余角部分在各已付 \(H^r,\ |r|\le4\) 上的总费用小于 (H.6)，
故完整同支演化 \(U_d^{\pm1}\) 的这些 norm 小于2。
同支的跨 \(\theta\)-锥项由真实解析 Fourier lag 给平滑算子；
\(c,\alpha\) 的两个进出列用 (H.7) 原样保留，系数角解析，因此也是
有明确有限费用的平滑列 \(K_{\rm sm}\)，不等于被置0。

严格区完整真实演化 \(U\) 已在同一全部状态和输出空间上有
\[
                       \|U^{\pm1}\|_{H^r}<2^{1024}J^5\delta^{-10}.
                                                                    \tag{H.12}
\]
这是原真实密度 relative-Cauchy 定理在同一两参数盒的实例化：
基准仍取该 \(\Gamma^*(a)\) 的径向对象，所有 partial ray 准确拉回。
(H.6) 支付额外角费用；径向基准的同阶界本来与 Sobolev 指数无关。
mean 使用原增强空间，未对其乘 \(m^{-1}\)。

现在对完整 Duhamel
\[
 U(t,0)-U_d(t,0)=
 \int_0^tU_d(t,\tau)(K_{\rm cross}+K_{\rm sm})U(\tau,0)d\tau
\]
使用 (H.8) 真正分部积分，得到端项
\(U_dLU|_0^t\) 和
\[
 -\int U_d[Z+[L,K_d]+LK_{\rm cross}+LK_{\rm sm}]U
       +\int U_dK_{\rm sm}U .                              \tag{H.13}
\]
所以整个差降两阶；这里 \(U\) 必须且确实在输出 \(H^{s+2}\) 上有界。
同支演化减去它的首 Dyson 项，用
\[
 U_d-I-\int K_d=\int_{\tau_2<\tau_1}
                 K_d(\tau_1)K_d(\tau_2)U_d(\tau_2,0)
\]
同样降两阶；无须用一个巨大的绝对 \(e^{\int|\kappa|}\)。
含真实 principal density pullback 后，可统一取严格两行 remainder
\[
               \|R_{\rm st}:H^s\to H^{s+2}\|
                 <2^{4608}J^{32}\delta^{-56},
                    \qquad |s|\le1.                      \tag{H.14}
\]
其中最坏的 \(LK_{\rm all}U\) 直接为
\(2^{2562}J^{25}\delta^{-50}\)，端项为
\(2^{2049}J^{17}\delta^{-34}\)；同支二次项为
\(2^{1025}J^{16}\delta^{-32}\)。加全部径向片、两支、mean平滑列后，
都落在 (H.14) 内。
这是真正全输入、全输出的界，不需要任何低频截断假设。

## 4. 根区：完整两次 Volterra 直接给 \(4/3\) 阶

每根的 canonical 方程为
\[
 u_{\xi\xi}-{\xi\over b^2}u_{\phi\phi}+Vu=0,\quad
 0\le\xi\le H=1/64,\quad |V|<17,\quad |V_\xi|<129
\]
于已付较小复盘和固定角条带。后一个界由真实完整 \(V-V_0\) 的
盘界及 Cauchy 得到。没有假设跨原径向接缝解析。

令 \(F_m\) 是原完整 Airy 两行基，包括 mean 的
\(c(1\pm i\xi/\pi)\)。非mean列为
\(c\kappa_m^{-1/3}[\operatorname{Bi}(-\xi\kappa_m^{2/3})
 \pm i\operatorname{Ai}(-\xi\kappa_m^{2/3})]\)，
\(\kappa_m=|m|/b\)。
完整负轴 Airy 两行界直接给
\[
 |D_{\sigma,m}(\xi)|\le 2^6 b^{1/3}\langle m\rangle^{-1/3}.
\]
于是 interaction
\[
 K_{mn}=F_m^{-1}
       \begin{pmatrix}0&0\\-V_{m-n}&0\end{pmatrix}F_n
\]
满足真正全矩阵
\[
             \|K(\xi):H^r\to H^{r+2/3}\|<2^{128}b^{2/3}.
                                                                    \tag{H.15}
\]
例如核中的两个 height 因子各提供 \(1/3\)：
权比只剩 \(\langle m-n\rangle^{|r+1/3|}\)，
由整角条带的 Fourier 和支付；不是先看对角列。
mean及跨锥也在同一次卷积中。

原完整 root 平衡 \(Y=(\sqrt{s_m}u,s_m^{-1/2}u_\xi)\) 的真实演化
在所有所需 \(H^r,\ |r|\le4\) 上小于 \(2^{2185}\)。
\(F_m\) 与这个平衡及其逆的 norm 至多 \(2^{16}b^{1/3}\)。
所以完整 interaction 演化及其逆可取
\[
                             \|U_{\rm int}^{\pm1}\|<2^{2217}b^{2/3}.
                                                                    \tag{H.16}
\]
特别，它不是只有径向基准的 bound。

准确 Volterra 恒等式
\[
 U_{\rm int}-I-\int K
 =\int_{\xi_2<\xi_1}K(\xi_1)K(\xi_2)U_{\rm int}(\xi_2,0)
\]
和 (H.15)--(H.16) 立即给完整 \(4/3\) 阶余项小于
\(2^{2560}b^2\)。所有低输入产生的高输出都经过真正
\(H^r\to H^{r+2/3}\to H^{r+4/3}\) 链。

一次积分的首项和余项按第49束全部 Fourier lag 拆分支付：
\(|m-n|\le |n|/2\) 时使用可比频率的完整 Airy 两行与
\(\xi=(|n|/b)^{-2/3}\) 根层；另一部分使用真实
\(e^{-c|m-n|}\) 尾。系数替换
\((|m||n|)^{-1/2}-|n|^{-1}\) 多一个
\(|m-n||n|^{-2}\)；跨支和根层均给 \(4/3\) 阶。
\(|V|<17,|V_\xi|<129\) 和有理上界 \(50\pi+5<163\)
使全部加权卷积费用小于 \(2^{512}b^2\)。
mean进出列也由同一解析尾取得完整输出 bound。

同支首项可换为自伴降一阶的指数；反对称排序差降两阶，
二次余项用准确 unitary Duhamel 付 \(2^{256}b^2\)。
其角非mean部分由 (H.6) 很小，故这个完整同支模型在所需
\(H^r\) 上 norm 小于2。不能把径向大平均的绝对指数当作费用。

在 \(\xi=H\) 转为严格 wave 密度态，准确使用
\[
 w=\xi^{1/4}u/\sqrt b,\qquad
 \zeta=\sqrt b\,\xi^{-1/4}(u_\xi+u/(4\xi)).
\]
完整自由 Airy 两行给真 \(-5b/(48H^{3/2}m)\) 次首项。
当 \(|m|/b\ge2^{12}\) 时余项按原两行 Volterra 门；
其余 \(|m|\le2^{12}b\) 按完整 Airy函数界直接估。
两种合并的全矩阵余项小于 \(2^{64}b^2\)，该 frame 及逆的
全部所需 \(H^r\) norm 小于 \(2^{16}b^{1/2}\)，mean 同时保留。

constant canonical cut 到真实原 \(t\) cut 仍用原 graph 两迹。
其跨支分部积分是在真实 canonical \(\xi\) 中进行，速度差是
\(2\sqrt\xi/b\)，在图带 \(H/2<\xi<2H\) 不为0。
可变上限只给两张真实 graph 的端项，带
\(1\pm(\sqrt\xi/b)g'\) 的准确密度因子。
不除以可能为0的图高 \(g-H\)。
\(|\kappa|<2^{17}b\)、完整 graph 解析界及 \(b^2n_i\) 已付的余量
给 graph 的两阶余项 \(<2^{1024}b^4\)，完整正逆 norm 小于2。

组合以上真实因素，整条 root 到原固定 \(t\) 的正逆 map \(L_e\)
及所识别的主加首模型 \(L_e^{(1)}\) 可用以下共同门：
\[
 \|L_e^{\pm1}\|_{H^r}<2^{2500}b_e^2,\qquad
 \|L_e-L_e^{(1)}\|_{H^s\to H^{s+4/3}}<2^{3500}b_e^6,
\]
\[
 \|L_e^{-1}-(L_e^{(1)})^{-1}\|_{H^s\to H^{s+4/3}}
                                    <2^{6002}b_e^8.        \tag{H.17}
\]
最后一式用准确 inverse identity 和前两式；没有反解 tiny transmission。
模型正逆 norm 小于2。右根的完整两行交换矩阵仍原样保留。

## 5. 真正正型双端 reflection 的量化重实例化

原 positive-DN-to-Airy 篇已经给完整正型 form 的真实复角平移比较。
两参数的新 radial bump 不进入正区；(H.4)--(H.6) 支付实际端图和
背景变化。因此同一复 form、Poisson/source/resolvent 证明在实际对象上
继续成立。

在两端 canonical collar，真实
\(|\nabla\log\alpha^{-1/2}|_{\operatorname{diag}(1,y/b_e^2)}<5\)。
以 \(H=1/64\) 的两支互不相交 ramp 重做完整 Poisson 估计，可取
\[
 E_*<128,\quad T_*<32,\quad P_*<128 .                       \tag{H.18}
\]
这里 \(1-5H=59/64>0\) 吸收实际 height 梯度；
\(T_*\) 是全 gradient 增益，\(P_*\) 是
\(H^{1/3}_{\lambda_-}\oplus H^{1/3}_{\lambda_+}
 \to L^2H^{2/3}_{\lambda_e}\) 的两 collar 联合增益。
原完整 positive form 的共同常数、两端 mean差和 flux 荷均参加。

每个非mean根作实际截断 Ai trial。其 residual 准确为
\(-\chi VU_0-2\chi'U_{0,y}-\chi''U_0\)。
Parseval、\(\int\mathrm{Ai}^2=\mathrm{Ai}'(0)^2\) 和真实
\(y\lambda_e^{2/3}\) 尺度给右乘 \(\langle m\rangle^{4/3}\) 的
ordinary residual bound \(<2^{128}b_*^{4/3}\)；
其 full contact 到原 Airy wave 再付 \(2^{16}b_*^{1/3}\)。
两端 source 同时解，故 off-diagonal 也被支付。
完整 graph identity
\[
                    R_++I=E_B-R_+E_A
\]
无需反解 trial incoming 图。实角的真 \(R_+\) 酉；
由原正型复 form relative estimate 和 (H.6)，在宽 \(1/128\)
复角平移后的整个 graph norm 也有 uniform bound。
转换 regularized root balance 与原 Airy frame 的低频费
至多 \(2^{64}b_*^{4/3}\)，它乘真实相对 form 小量，仍小于 (H.5)。
所以该复族及 adjoint 的 Cauchy commutator给全部所需
\(|r|\le4\) 的真实同空间 bound，小于2。

得到完整双端算子
\[
 R_+=-I+E_+,\quad
 \|E_+:H^s\to H^{s+4/3}\|
 <2^{4096}J^{16}\delta_j^{-16},\qquad
 \|R_+\|_{H^r}<2.                                        \tag{H.19}
\]
mean列使用原完整 mean frame；trial 为0的 mean列在 \(E_A,E_B\)
分别是 \(-I,I\)，不是把真 reflection 规定为 \(-I\)。
原 Airy 端迹不是单独一个 principal DN根，weak端点负荷也仍保留。

## 6. 真实角图与首符号共轭怎样作用于物理两迹

先在原物理 root 角中的 Airy amplitudes 组装，使用 (H.19)。
之后的 KAM 和首符号共轭是**完整 wave 空间的表示变换**。
它不是在保持固定 Airy frame 时只把 raw 高度写成 \(f\circ K\)。

具体地，在每个 \(\theta\)-锥先用
\[
 V_K=|D|^{-1/2}\Pi_\varepsilon\mathcal D_K
                      \Pi_\varepsilon|D|^{1/2}.
\]
完整零均值算子
\(T_K=|D|^{-1/2}\mathcal D_K|D|^{1/2}\) 的准确逆是
\(T_{K^{-1}}\)。令 \(J_{\rm cone}=\operatorname{sgn}D\)。
signed primitive 的 Green pairing 给两个准确恒等式
\[
 T_K^*J_{\rm cone}T_K=J_{\rm cone},\qquad
 T_KJ_{\rm cone}T_K^*=J_{\rm cone}.
\]
第二式可由第一式及真实逆直接推出，未假定某个单锥块已满射。
若 \(T_K=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\)
按正负锥分块，则
\(A^*A-C^*C=I\)、\(AA^*-BB^*=I\)；
负锥有相同的两式。两个跨锥 kernel 均对相反符号频率作24次真实
角分部积分，相位导数至少为 \((|m|+|n|)/2\)。
(H.5) 支付两个完整 kernel 的系数与所需强范数，因此
\(V_K^*V_K-I\) 和 \(V_KV_K^*-I\) **双侧**都有该平滑小界。
特别 \(V_KV_K^*\ge I\)，所以 \(V_K\) 满射；第一式还给有界下方。
故实际 polar 校正
\(U_K=V_K(V_K^*V_K)^{-1/2}\) 是满射 unitary。
mean上取恒等；\(U_K-V_K\) 平滑且有 (H.5) 费用。
它们的群关系只差同样有界的平滑项，全部放入余项。

若 \(F_e\) 是原完整 Airy两行矩阵，物理两迹恢复必须用
\[
             \mathscr B_{K,e}
           =F_e\operatorname{diag}(U_K,U_K)F_e^{-1}.        \tag{H.20}
\]
它是完整 \(2\times2\) Green 变换，一般有非zero的两条交叉块。
不能把它偷换成 \(\operatorname{diag}(C_K,\mathcal D_K)\)，后者在固定
Airy频率单位中会产生未付的 principal混合。
真实 raw 高度/flux 还须在 (H.20) 外按原 \(\alpha\) 和 normal shear
转换，物理 constant height 因此仍是完整函数。

principal KAM 使真实返回角图共轭到固定平移。
第49束的首符号 \(B_i(x)\) 有真实平均 \(\beta_i^0\)，其非mean部分
与实际 cohomological 解
\[
 q_i-q_i\circ T_{-\omega_i}=\beta_i^0-B_i
\]
由 (H.5) 支付。取完整自伴 order-one-inverse 的 \(Q_i\)，首符号
\(q_i/n\)，mean上为0。\(e^{iQ_i}\) 和逆在全部需要的 \(H^r\) norm
小于2；由准确 Duhamel，所有排序差和二次项降两阶。
因此实际主加首返回模型是固定
\[
                     U_i=\exp(i\omega_iD_x)
                                  \exp(i\beta_i^0D_x^{-1})          \tag{H.21}
\]
于非mean，负锥取真实共轭。这里 \(D_x^{-1}\) 的 mean定义只用于表示，
真实 mean网络没有被 (H.21) 代替。

## 7. 组装全部两端口：明确的常数账

真实负区两根—严格区—两根的完整乘积，逐项 telescoping 后使用
\[
 b_e<2^{16}\sqrt J\,\delta^{-9/4}
\]
及 (H.12)、(H.14)、(H.17)，给
\[
 \|C_-^{\rm true}\|_{H^r}<2^{6200}J^8\delta^{-20},\qquad
 \|E_-:H^s\to H^{s+4/3}\|<2^{10000}J^{32}\delta^{-64}.     \tag{H.22}
\]
例如最贵 root-inverse 项是
\(2^{6002}b^8\cdot2^{1024}J^5\delta^{-10}
 \cdot2^{2500}b^2
 <2^{9686}J^{10}\delta^{-65/2}\)；
strict余项项小于
\(2\cdot2^{4608}J^{32}\delta^{-56}\cdot2^{2500}b^2
 <2^{7141}J^{33}\delta^{-121/2}\)。
第二项用 \(J\delta^{7/2}<1\) 降到显示的 \(J^{32}\delta^{-64}\)
包络；其余有限项仍有超过 \(2^{200}\) 的余量。
二者都落在 (H.22)，不是把两个强余项常数无理由相乘。
乘 positive defect 时使用完整负区的同空间第一界；
乘负区 defect 时使用 \(\|R_+\|_{H^r}<2\)。

保留一个负分量的两个独立 incoming unknown。仅反解前面明确构造的
同支主加首**模型**，其 norm 和逆小于2；不反解实际 Cauchy 的一个
可能有低核的非对角块。经第6节的表示变换，可将两个准确方程写成
\[
 \left[\begin{pmatrix}I&I\\-U_i&I\end{pmatrix}
                          +\mathcal R_i\right]z_i
       +\sum_{\ell\sim i}\mathcal R_{i\ell}z_\ell=g_i .     \tag{H.23}
\]
\(\mathcal R\) 含完整实际 negative remainder、两个 positive cross、
mean进出列和全部仿射 particular。每个系数都来自准确原两行代入。

现在用明确的、有界 Fourier 行矩阵
\[
 A_i^0=\begin{pmatrix}I&-I\\U_i&I\end{pmatrix},
 \qquad
 A_i^0\begin{pmatrix}I&I\\-U_i&I\end{pmatrix}
                    =\operatorname{diag}(I+U_i,I+U_i).     \tag{H.24}
\]
其 norm小于2。非mean处原目标保证 \(I+U_i\) 可逆；
此处尚未使用这个逆，也没有对 mean作 (H.24) 的谱除法。
有序 source同时乘 \(A_i^0\)。

两个相邻胞元的尺度差、最多8个端口、(H.20) 的完整端口表示及
所有前述剩余费用，给准确的非mean网络
\[
                 (\mathcal D+\mathcal E)z=g,\qquad
 (\mathcal D_i)_n=
      [1+e^{i(n\omega_i+\beta_i^0/n)}]I_2,                 \tag{H.25}
\]
并给 (H.1)。若选另一实wave约定，只将第二对角项换成其复共轭，
所有模和范数完全相同。
mean行仍是原完整两状态/正型 mean flux行，位于未消去的低系统。

## 8. 真正非径向无限网络高块

由原实际算术，
\[
 |(\mathcal D_i)_n^{-1}|
 <2^{165}J^3\delta^{-13/2}|m|.
\]
为同时包括 \(\langle m\rangle\) 与两行 norm，取
\(d_i=2^{167}J^3\delta^{-13/2}\)。
(H.1)--(H.2) 给对**全部**邻居输入的高输出 bound
\[
 \|P_{H,i}\mathcal D_i^{-1}\mathcal E_i z\|_{H^s}
 \le d_iT_i^{-1/3}C_i\|z_{\rm neighbors}\|_{H^s}
 <2^{-5035/3}J^{-1}\delta^{1/6}
                                  \|z_{\rm neighbors}\|_{H^s}.
                                                                    \tag{H.26}
\]
每个列也只进入至多8个行。所以在 \(\ell^2_i(H^s)^2\)、
\(\ell^1_i(H^s)^2\) 或 \(\ell^\infty_i(H^s)^2\) 上，完整
\[
           \|P_H\mathcal D^{-1}\mathcal E P_H\|<2^{-1024}. \tag{H.27}
\]
同样的输出估计也作用于 \(P_L=I-P_H\)，并未假设低历史为0。
所有 Fourier lag和跨正负锥早在 (H.1) 的全算子界中支付，
此处不能退回仅逐模对角的径向论证。

令 \(\mathcal Z_s\) 取上述任一具体完整序列空间，并给实际源一个
可直接读的充分 norm
\[
 \|g\|_{\mathcal Y_s}
 =\|(d_i\|g_i\|_{H^{s+1}})_i\|_{\ell^p},\quad
                    p\in\{1,2,\infty\}.                  \tag{H.28}
\]
则给定完整 \(z_L\in\mathcal Z_s\) 时，唯一高解为
\[
 z_H=
 [I+P_H\mathcal D^{-1}\mathcal E P_H]^{-1}
 P_H\mathcal D^{-1}(g-\mathcal E z_L),                     \tag{H.29}
\]
\[
 \|z_H\|_{\mathcal Z_s}
 <2\big(\|g\|_{\mathcal Y_s}+2^{-1024}\|z_L\|_{\mathcal Z_s}\big).
                                                                    \tag{H.30}
\]
这是真正非径向高网络的闭算子门，域、输出、两端口和全部低输入明确。
对每个固定 \(m\)，高分量集合有限；全部频率仍同时保留。

## 9. Ordinary、weak、mean 与 metric-source 的完整消费

\(g_i\) 是准确原方程 particular 的端口向量经 (H.20)、同支模型和
(H.24) **按顺序**变换后的向量。不是自由挑选的理想源。
其 (H.28) 是对这些实际端口的充分输入条件，没有把它授予原物理空间中
尚无该正则性的任意源。

原负区与 graph 的 source保持
\[
 F_d=\Lambda^{-1/2}F,\qquad
 f_d=\Lambda^{-1/2}(f-\tfrac12\nabla\log\Lambda\cdot F),
\]
以及真实 Piola 后的 root height转换。根上始终用 total状态
\[
 \partial_\xi\binom uP
 =\begin{pmatrix}0&1\\-(m^2\xi/b^2+V)&0\end{pmatrix}\binom uP
       +\binom{-F^\xi}{\,f_c-imF_c^\phi\,}.                \tag{H.31}
\]
不求 \(\partial_\xi F^\xi\)。第3、4节每一次有界 Duhamel、
角图及两行变换同时作用于此完整两分量。

正区的实际两端 Poisson 与 total-contact 保持原 source 号数。
在本文原 raw 约定 \(\operatorname{div}(G\nabla h)=f-\operatorname{div}F\)
下，零高度 particular 满足
\(\langle q,g\rangle=\int f\,Hg+\int F\cdot\nabla Hg\)。
若改用正算子 \(-\operatorname{div}(G\nabla h)\)，必须同时代入
\(f_{\rm ph}=-f,\ F_{\rm ph}=-F\)，这就是同一 Poisson 的负伴随式。
再按完整 source Cayley列恢复 incoming/outgoing。
source norm的 \(A^{-1}\) 权、真实 Jacobian和height因子保留。
若需要 bare通量，则继续提供并减去原合同要求的真实法向端点迹；
体源范数本身不授这个迹。

令 \(\pi=\mu(h_t-dh_\theta)+F^t\) 为原物理 total flux，
\(\pi_0=\langle\pi\rangle_\theta\)、\(h_0=\langle h\rangle_\theta\)。
两个实际 mean 行准确是
\[
 \pi_0(t)=\pi_0(t_f)+\int_{t_f}^t\langle f\rangle_\theta\,d\tau,
 \qquad
 h_0(t)=\rho\lambda+
 \int_{t_f}^t
 \left\langle d h_\theta+\mu^{-1}(\pi-F^t)\right\rangle_\theta d\tau.
                                                               \tag{H.32}
\]
第二式保留全部非mean通量经 \(\mu^{-1}\) 和 drift 回灌 mean 的项。
只有在真正径向参考中才可化为
\(\rho\lambda+\int(\pi_0-F^t_0)/\mu_0\)，不能把这个参考式移用于
当前非径向背景。它们、两个正端 mean contact及最外regular mean行
全属于 \(z_L\) 的未解
完整系统；不能在 (H.29) 中将其设为0。
\(\Gamma^*(a)\) 的导数带来的 ordinary/weak metric-source、固定物理半径
的 \(\dot t\)、第四停止列和完整 mean height移动端项也按同一合同作为源。
本篇并未把这些依赖未知方向的列自动当成已吸收的小反馈。

## 10. 当前真正剩余的部分

已付的是同一个实际背景的全余项 (H.1) 与真高网络 (H.29)。
剩余集合 \(P_L\) 随分量、频率移动，包含所有转向/中间频率、两mean、
外cut128及有限connector。它与原离散标签的低窗不同。
还须把这个实际 Schur 系统及完整高解恢复到原 \(\mathcal X_\beta\)、
连续普通/weak源和真实外 \(\mathcal F_c\) 的同权空间，支付
\(H D_0^{-1}E G\) 与实际参数源反馈。

第50束新的两参数 map 的旧94步数列必须重新定义/执行；
(H.29) 本身不会把有限步 residual变为0，也不会完成外边界闭合。

小严格预算程序为
\(\texttt{scripts/fourfold_actual_nonradial_full_remainder_high_network_20261114.js}\)，
报告为
\(\texttt{notes/2026-11-14-R119-actual-nonradial-full-remainder-high-network-budget.json}\)。
程序实际使用 BigInt 有理门核对全部显示费用和指数；
完整 Fourier、Duhamel、源域及低输出链的证明在正文给出。
