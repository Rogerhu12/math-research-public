# R758　保持球面积的全深材料坐标、两刚帽相位与唯一法向相容行

取 R738 的真环带 \([a,b]=[.075,.22]\)，同一 \(g=E_\sharp dr^2+r^2d\phi^2\)，外帽不动，内帽绕 \(y\) 轴作 \(\sin\theta=.27,\ \cos\theta>0\) 的固有转动。已有 R738 末态的真实面积预算、R748 的单高度工作和 R755 的必要矩阵各有单独身份。此处构造另一组在全部半径上满足 Gauss 映射 Jacobian 和准确连接形式的真实试场。给出的 \(F_\chi\) 仍需以其实际六 jet 和三 Gram 求解。本文不假设中央有双核。

## 1　Gauss 映射所付的整圈质量

记 \(m=\sqrt E\)，\(\mu=1-1/m\)。对于有向真等距浸入，\(n\cdot(n_r\times n_\phi)=Kr m=\mu'\)。两刚帽 \(n\) 各自沿整条材料边常值；若全图 \(n\) 落在开半球，则对任一连续球面测函数 \(f\)
\[
 \int f(n)K\,dA_g=0 .
\]
对光滑 \(f\)，在半球内 \(f\,dA_{\mathbb S^2}\) 有原函数，边上拉回为零。再以一致逼近得连续情形。正负 \(K\) 区经 Gauss 映射推前的绝对曲率测度因此相同。正图情形亦可取 \(f=f(n\cdot e_z)=f(\sqrt{1-|\nabla_g u|^2})\)。

用带符号 \(\alpha_0\) 表示源纬度，\(\tan\alpha_0=w_*=2.01 M\,b_{\rm bump}-\eta'\)。此处 \(b_{\rm bump}\) 是原中央平滑鼓包，\(\eta'\) 是原两深帽的源坡，二者支撑内部不相交，故 \(1+w_*^2=E_\sharp,\ |\alpha_0|<\pi/2\)。计算 \(\mu=w_*^2/[m(m+1)]\) 保留深层微量。连续公式的该值与直接 \(1-1/m\) 相同。IEEE 中同时保留差和 \(1+w_*^2-E_{64}\)，不得用一次浮点减法截掉数十层真坡。原 Base64 角校准的真实二进制数是 10.879249615813897（原 NPZ 610 B/SHA bf12e73a…）。在 \(r_*=.1475\)，质量一平滑与三角鼓包给 \(b_{\rm bump}\ge .06-.0025\)，故 \(\alpha_0(r_*)>.88\)。R738 原始导数和正负胞完整费用保持。

## 2　一次角隐方程的保面积修正

在 \(\mu>0\) 处取真实周期、在角变量奇的生成函数 \(h(\mu,\Phi)\)，用未动的材料角解
\[
 \phi=\Phi+h_\mu(\mu,\Phi),\qquad U=\mu+h_\Phi(\mu,\Phi).       \tag{1}
\]
若 \(1+h_{\mu\Phi}>0,\ 0<U<1\)，第一式的实提升有唯一解，每圈 \(\Phi(\phi+2\pi)=\Phi(\phi)+2\pi\)。由 \(S=\mu\Phi+h\)，\(dS=\phi\,d\mu+U\,d\Phi\)，故 \(dU\wedge d\Phi=d\mu\wedge d\phi\)。其连接原函数也显式给出
\[
 (1-\mu)d\phi-(1-U)d\Phi=d[(1-\mu)(\phi-\Phi)+h].             \tag{2}
\]
前式允许 \(\mu'(r)=0\)，由连续性穿过转向纬圈，无需除以 \(\mu'\)。每个单调支可使用各自的 \(h\)，前提是相邻真缝两侧值及用于物理二 jet 的混合导数相合。初接口取左右共享项与独立低纬项；后者在中央峰附近的开带消失。

用 \(p=U/\mu\)，以无除零方式定义
\[
 \sin\alpha=\sin\alpha_0\sqrt{p(2-U)/(2-\mu)},\qquad
 \cos\alpha=1-U .
\]
此取号使真深帽导数经过源坡的每一次变号而不取绝对值。首个有限簇用
\(h=\mu\sum_j c_j b_j(\mu)\sin(\ell_j\Phi)\)，故 \(p=1+\sum_j\ell_j c_j b_j\cos(\ell_j\Phi)\) 可连续直读。用 \(\sum_j|\ell_jc_j|\sup|(\mu b_j)'|<1\) 和 \(\sum_j|\ell_jc_j|\sup|b_j|<1\) 支付完整角图与 \(p>0\)，并付 \(U<1\)。任意额外参数的更宽域需保留两真实正性条件。当前源码每个径幂 d≥1，所选 lip<.88 给出总振幅≤.44；原中央鼓包≤.06，两真实尾坡和截断的已给上界均小于 .001，支撑与中央不重，由实际 M<10.89 得全段 |w_*|<1.314，故 μ<.395、U<.569。此处的全段上限不依赖角样本最大值。

## 3　使两真法向不同的准确初图

内半材料取 \(\gamma(\alpha)=\theta [1-S_{11}((\alpha-.025)/.825)]\)，\(S_{11}(x)=2772\int_0^x t^5(1-t)^5dt\) 是两端常值延拓的十一阶多项式阶跃；外半取零。两支在真实中央峰附近须满足 \(\alpha>.85\)，此处同为恒零。若试参数不能保证该缝，则该参数的资格未成立。令 \(v=\gamma_\alpha\)，有 \(|v|<.90\)。在同一真材料圈再解
\[
 \Phi=\psi+v\sin\psi .
\]
记 \(Q=Q_y(\gamma)\)，取
\[
 n=Q(\sin\alpha\cos\psi,\sin\alpha\sin\psi,\cos\alpha),\quad
 X=Q(\cos\alpha\cos\psi,\cos\alpha\sin\psi,-\sin\alpha),\quad
 Y=Q(-\sin\psi,\cos\psi,0).
\]
\(X\times Y=n\)。在 \((\alpha,\psi)\) 坐标中，法向 Jacobian 是 \(\sin\alpha(1+v\cos\psi)\)，与 \(dU\wedge d\Phi\) 完全一致。因此全初图具有指定 \(\mu'(r)\)。球标架连接为 \(Y\cdot dX=(1-U)d\psi+\sin\alpha\sin\psi\,d\gamma\)。再设
\[
 \delta=(1-\mu)(\phi-\Phi)+h+(1-U)(\Phi-\psi),\qquad
 P=\cos\delta\,X+\sin\delta\,Y,\quad T=-\sin\delta\,X+\cos\delta\,Y .
\]
由 (2) 及 \(d[(1-U)(\Phi-\psi)]=(1-U)(d\Phi-d\psi)-\sin\alpha\sin\psi\,d\gamma\)，恰有
\[
 T\cdot dP=(1-\mu)d\phi,\qquad P\times T=n .                  \tag{3}
\]
该实原函数消去另一个沿径向的角度积分。周期相位没有丢失：两个隐角绕数为一，\(\delta\) 真周期。由反射，在 \(\phi=0,\pi\) 两轴处角差都为零。更强地，在两真 rim，\(h/\mu,h_\mu\to0,\gamma\to\theta,0\)，于是全部材料角 \(P=D_e e,\ T=D_e e_\phi,\ n=n_e\) 恰是刚件的有序标架。若姿态或材料绕向改变，必须另付这一层。

## 4　全部实体闭合等价为一个标量及真实自由平移

利用二基对称性的唯一缺口
\[
 c=r\,T\cdot n_r-m\,P\cdot n_\phi,\qquad
 \partial_\phi(mP)-\partial_r(rT)=c\,n .                      \tag{4}
\]
切向两分量由 (3) 精确消失。一旦 \(c=0\)，从外圈真实位置沿径积分 \(F^o_r=mP,\ F^o(b,\phi)=bD_o e\)，直接得到 \(F^o_\phi=rT\)；全场周期且同一 \(g\) 已实现。内圈切向的完整材料相位已固定，故 \(F^o(a,\phi)-aD_i e\) 为同一常向量 \(C_*\)。必须比较该实际中心与真实刚件的握持、净空、支持与包络。如果另指定 \(C\)，尚需 \(C=C_*\)；若内平移自由，只需读出 \(C_*\)，反射使其 \(y\) 分量为零。反之，真正以这些帧闭合的同度量场必须满足 (4)。本有限 \(h\) 簇的完备性未作为无条件的所有等距场刻画。

在未解阶段也可做真实两帽实体。设
\(\Delta=C+aD_i e-F^o(a,\phi)\)，\(F_\chi=F^o+\chi(r)\Delta\)，沿用 R748 的真 C² 拼带。两方向实体只差这条角函数，因此
\[
 F_r=mP+\chi'\Delta,\quad F_\phi=F^o_\phi+\chi\Delta_\phi,\quad
 F_{rr}=m'P+mP_r+\chi''\Delta,\quad F_{r\phi}=mP_\phi+\chi'\Delta_\phi,\quad
 F_{\phi\phi}=F^o_{\phi\phi}+\chi\Delta_{\phi\phi}.
\]
实际位置和这五导给全部 Gram 与形算子。所绘 \(n\) 是设计 Gauss 图；在未解阶段，实体真法向必须由两条实际导数叉积获得。实际端帽处 \(P_r=0,\ m'=0\)，两边六 jet 按原始导数 \((F,F_r,F_\phi,F_{rr},F_{r\phi},F_{\phi\phi})\) 均为 \((C_e+rD_e e,D_e e,rD_e e_\phi,0,D_e e_\phi,-rD_e e)\)。完成等距的 \(F\) 才有设计 \(n\) 及准确形算子。

## 5　全深延拓及真实非局部微分

取 \(t=\mu/U_0\) 和有限角模。可取 \(b=t^d(1-t)^k\) 或其乘 \(\cos(\kappa\log t),\sin(\kappa\log t)\)，\(d\ge1\)；可再乘在 \(\mu_s<\mu(r_*)\) 已恒零的高阶截断。此类试函数未在真深帽的开邻域锁死。源的正 dyadic 母胞满足 \(|w_*|\le8L_n^3,\ |w_*'|\le C(1+n)L_n/\rho\)。故
\[
 |\mu|\le C L_n^6,\quad |\mu'|\le C(1+n)L_n^4,\quad
 |\partial_\phi^j(\Phi-\phi)|+|\partial_\phi^j(p-1)|\le C_jL_n^{6d},
\]
且一径导的界为 \(C_j(1+n)L_n^{6d-2}\)。隐角正分母及有限角频允许逐阶求导。对 \(\alpha\) 使用有符号的 \(\sin\alpha_0\) 消去 \(\sqrt\mu\) 顶点的伪奇异。\(P,T,n\) 及其首径导、所需两角导均收敛到准确帽迹。对任一内部分支的 \(w_*=0\) 且 \(w_*'\ne0\) 的点，\(\mu=O(w_*^2)\)，\(\partial_r(\mu^d e^{i\kappa\log\mu})=O(|w_*|^{2d-1}|w_*'|)\to0\)，同样可延拓。于是所给 \(F_\chi\) 是 \(C^2\) 的真实材料试场。常数依有限列和正分母；这里不授连续 reach 或中央全角零 \(c\)。已付 R734/735/738 的原模两射线与这些新生成函数不同，不移植其零模资格。

在不变真材料 \((r,\phi)\) 上，对 \(h\mapsto h+\epsilon k\) 有
\[
 \dot\Phi=-k_\mu/(1+h_{\mu\Phi}),\quad
 \dot U=k_\Phi+h_{\Phi\Phi}\dot\Phi,\quad
 (1+v\cos\psi)\dot\psi=\dot\Phi-\dot v\sin\psi .
\]
\(\alpha,\gamma,\delta\) 用以上显式函数在同一正分母下微分；真极点用 \(p\) 的延拓。\(c\) 有四项
\(r\dot T\cdot n_r+rT\cdot\dot n_r-m\dot P\cdot n_\phi-mP\cdot\dot n_\phi\)。
\(\dot F^o(r,\phi)=\int_b^r m\dot P\,dr\)，\(\dot\Delta=\dot C-\dot F^o(a,\phi)\)；两次物质角导均作用于同一整段积分。每列可以影响其径向支撑之外的实际实体和两个拼头，不能借旧 R738/R748 工作 J。正图、真实两帽、有限 Gauss 列和最终全物理场需分别审验，离散角/径网和真连续积分之间的误差仍须付费。

## 6　从标量余项直接控制实物三 Gram 与二阶导

设 \(q(r)\) 是整个纬圈上 \(|c|\) 的上界，\(\epsilon=\int_a^b q\,dr\)，\(q_1(r)\) 上界 \(|\partial_\phi c|+|c|\,|\partial_\phi n|\)。由 (4)，\(L_o=F^o_\phi-rT=\int_b^r c n\,dr,\ L_i=L_o+\Delta_\phi=\int_a^r c n\,dr\)。因而 \(\|\Delta_\phi\|_\infty\le\epsilon\)。积分平均所用圆周最短距离的均值为 \(\pi/2\)，遂有
\[
 \|\Delta\|_\infty \le d_C+\pi\epsilon/2,\qquad
 d_C=|C-\overline{F^o(a,\cdot)}|.
\]
真实位置单位为长度；期望自由中心若取该平均，则第一项消失。\(F_{\chi,r}/m=P+\chi'\Delta/m\)，\(F_{\chi,\phi}/r=T+[(1-\chi)L_o+\chi L_i]/r\)。令 \(e^2\) 为后二切向误差界的平方和，则连续相对 Gram 算子误差至多 \(2e+e^2\)，最小切向奇异值至少 \(1-e\)。若
\(\kappa_0=e_r+e_\phi+e_re_\phi<1\)，真实法向与设计 \(n\) 的差至多 \(2\kappa_0/(1-\kappa_0)\)。实际 \(rr,r\phi,\phi\phi\) 导与设计 \((mP)_r,mP_\phi,rT_\phi\) 的原始（未归一化）差分别至多
\[
 |\chi''|(d_C+\pi\epsilon/2),\quad |\chi'|\epsilon,\quad
 (1-\chi)\int_r^b q_1\,dr+\chi\int_a^r q_1\,dr .
\]
除以 \(E,mr,r^2\) 后还须乘实际法向、给设计二导范数支付法向误差，才得到实物二基界。所有这些条件以全径胞、全角的真实上界为前提。离散 Gauss 原函数得到的导数/积分差与普通 \(c\) 样本不能充作该前提。
