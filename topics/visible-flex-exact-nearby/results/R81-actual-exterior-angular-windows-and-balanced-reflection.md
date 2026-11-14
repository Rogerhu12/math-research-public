# R81：真实外区的有限高角窗口、完整源接触与有界反射

2026-11-12，independent-audit。

**状态：已证明并实际支付的正侧算子结论；主课题仍未完成。**
本篇对 R69/R74 的同一完整外区和准确参数盒，支付 signed 解析/direct-log
角权下的有限高 Sobolev 窗口、正负普通源/contact，以及含根零模的
onto 反射和其逆。物理 regular 平均值约束、平均通量输出和它们的
微分费用全部保留。

新预算使用完整边界能量核，而非先估其零阶差核；实际归一边界复平移
模从 R76 的 \(1.55\,10^{13}\) 粗上界降到 \(<435\)。由此同一真实
变分问题的充分 signed 角权可取 \(2^{-67}\)。本篇没有修改 R76 的
冻结结论，也未把有限高角正则当成未付的高径向正则。

## 1. 同一实际对象、空间与真正平均行

准确参数盒仍是
\[
 \delta_c=-7789866024620307/4611686018427387904,
 \qquad |\delta-\delta_c|\le1/2000000.
 \tag{81.1}
\]
采用 [R69](R69-actual-closed-approximate-exterior-and-two-held-disks.md)、
[R74](R74-actual-full-tail-robin-and-augmented-positive-cap.md) 的整个正区间，
它含真实主体、自然 graft，以及从同一实际无限尾回传的完整 Robin
算子。使用 R76 已付的物理 shear/ground-state 坐标
\((x,\varphi)\in[0,L]\times\mathbb R/(2\pi\mathbb Z)\)。
\[
 \|u\|_{\mathcal V}^2=
 \int(|u|^2+|u_x|^2+x|u_\varphi|^2),
 \qquad \mathcal V_k=\{u:\langle D_\varphi\rangle^ku\in\mathcal V\}.
 \tag{81.2}
\]
这里使用物理角 Fourier 频率 \(n\)；真实四重子空间为 \(n\in4\mathbb Z\)。
若另换归一角 \(4\varphi\)，必须同步转换 Sobolev 乘子和角权，不把
这项实际四倍因子省去。令 \(\phi_0\) 为单位 \(L^2\) 常数函数。
regular 物理平均值与真实全形式分别为
\[
 \ell(u)=\langle J u(L),\phi_0\rangle,
 \qquad
 b(u,v)=\int C\nabla_xu\cdot\overline{\nabla_xv}
       +\langle\Gamma_Hu(L),v(L)\rangle,
 \tag{81.3}
\]
\(\nabla_x=(\partial_x,\sqrt x\partial_\varphi)\)，
\(\Gamma_H=C_H^*\Gamma_{\rm ext}C_H\)，真实实测度伴随
\(C_H^*=J C_H^{-1}\)。\(mI\le C\le MI\) 及正 Robin 使本形式非负。

定义
\[
 X_t=H^{t+1/3}\oplus\mathbb C,
 \quad Y_t=H^{t-1/3}\oplus\mathbb C=X_{-t}^*.
 \tag{81.4}
\]
第一槽是转折 trace/contact，第二槽是 regular 的物理平均值/平均通量。
完整正侧问题给定 \((a,\xi)\in X_0\)，满足
\(u(0)=a,\ell(u)=\xi\)，其弱式是
\[
 b(u,v)-F(v)=\langle p,v(0)\rangle+
                    \lambda\overline{\ell(v)}.
 \tag{81.5}
\]
这里 \(F(v)=\langle f,v\rangle+\langle d,v(L)\rangle\) 包含整个普通
体源与已拉回的 regular 负荷。\(\lambda\) 并未设成零；最终它还须
满足真尾和中央系统的有限兼容行。

角权为 R76 的
\[
 W_\sigma=e^{\sigma\psi(|D|)},\quad
 \psi(t)=t\ \text{或}\ [\log(e+t)]^{3/2}-1,
 \qquad |\sigma|\le2^{-67}.
 \tag{81.6}
\]
两种 \(\psi\) 在零点为零、Lipschitz 常数至多 1。以下常数同时控制
正、负符号，负权解释为相应 Fourier Hilbert completion。

## 2. 完整边界能量的共同复平移界

R76 已针对实际角图付出同一个复带及 sector：
\[
 \rho>8.09977\,10^{-6},\quad r=\rho/2,
 \quad |H'|,|1/H'|\le M<4.96931,
 \quad \Re H'\ge\mu>0.197210,
 \quad |\Im H'|\le\tfrac14\Re H'.
 \tag{81.7}
\]
它们在下面所有共同平移 \(|\Im\tau|\le r\) 及所需实路径成立。
\(H(z+2\pi)=H(z)+2\pi\)。

对于实 \(x,y\)，令 \(d=d_{S^1}(x,y)\in(0,\pi]\)。选择
\(D=H(x+\tau)-H(y+\tau)-2\pi k=a+ib\)，使 \(a\in[-\pi,\pi]\)。
沿 \(\Re H\) 的相应短像弧积分 \(H'\)，得到
\[
 |a|\ge\mu d,\qquad |b|\le|a|/4.
\]
所选原像弧未必是原圆最短弧，但其长度至少为 \(d\)，所以第一式的
方向正确。由 \(\pi^2<10\)、\(\sinh(\pi/8)<1/2\)，
\[
 \Re\sin^2(D/2)
 =\sin^2(a/2)-\cos a\sinh^2(b/2)
 \ge\frac{a^2}{\pi^2}\bigl(1-\sinh^2(\pi/8)\bigr)
 >\frac{a^2}{16}.
 \tag{81.8}
\]
于是完整核满足
\[
 \left|H'(x+\tau)H'(y+\tau)
 \csc^2\frac{H(x+\tau)-H(y+\tau)}2\right|
 \le\frac{4M^2}{\mu^2}\csc^2\frac{x-y}2.
 \tag{81.9}
\]

实平移时，\(C_H^*|D|C_H\) 的准确 Gagliardo 形式为
\[
 \frac1{8\pi}\iint
 (u(x)-u(y))\overline{(v(x)-v(y))}
 H'(x)H'(y)\csc^2\frac{H(x)-H(y)}2\,dx\,dy.
 \tag{81.10}
\]
复平移定义同一个核式；(81.9) 和 Cauchy--Schwarz 保证它在
\(H^{1/2}\times H^{1/2}\) 上有界，模至多
\(4M^2/\mu^2\)。同一可积支配使其弱解析；局部一致界及 Cauchy
积分再给归一后 \(L^2\) 算子的解析性。因此无需先估零阶差核的
\(H'''\) 对角极限，便有真正的 operator-valued 共同复平移界。

R76 的准确稳定线拆分、pulled resolvent 和真无限尾误差仍原样保留：
\[
 \Gamma_{\rm ext}=c_0|D|+c_1-c_1b(|D|+b)^{-1}+E,
\]
其常数 \(c_{0,+},c_{1,+},M_R,M_E\) 全来自同一已付输入，且
\(0<b<1\)。所以
\[
 \boxed{\quad
 \|\langle D\rangle^{-1/2}\Gamma_{H,\tau}
                \langle D\rangle^{-1/2}\|
 \le M_\Gamma:=(4M^2/\mu^2)c_{0,+}
                 +c_{1,+}(M+M_R)+M_E<435.
 \quad}
 \tag{81.11}
\]
均值和全部 \(4\mathbb Z\) 真尾模式皆包含；\(E\) 在 Arb 中保留为
非零数，未用零替代极小量。

## 3. 重新支付同宽角权与实际 mean 运输

写
\[
 N(A,h)=\frac{2Ae^{-h/2}}{(1-e^{-h/2})^2},
\]
\[
 N_C=N(M_C,\rho),\quad N_\Gamma=N(M_\Gamma,r),\quad
 N_J=N(M,\rho),\quad
 T_0=\sqrt{C_eC_t}N_J,
\]
\[
 N_0=N_C+C_tN_\Gamma,\qquad N_*=2N_0+3M_*T_0.
 \tag{81.12}
\]
这里 \(M_C\) 是实际内部归一矩阵的复模，\(M_*\) 是 R74 的完整
无权形式 norm。对完整边界归一算子应用 R76 的 Fourier lag 论证
完全合法；它不要求先去掉 \(|D|\)。该主项本来与角权交换，只是
本式对它也给了一个多余但有效的上界。

令 \(\ell_\sigma=\ell W_{-\sigma}\)，\(e\) 为转折 trace 零、regular
trace 为 \(\phi_0\) 的角常数 lift，\(\|e\|\le\sqrt{C_e}\)、
\(\ell(e)=1\)。在原来的零 trace、零 mean 子空间上
\(T_\sigma v=v-e\ell_\sigma(v)\) 准确运输平均约束。
trial/test 分别使用 \(T_\sigma,T_{-\sigma}\)，且
\[
 \|T_\sigma-I\|\le|\sigma|T_0,\qquad
 \|b_\sigma^X-b\|\le|\sigma|N_*.
 \tag{81.13}
\]
这些是 R76 的同一真实恒等式；只把更强的 (81.11) 代入，重新验证
所有 Neumann 门，未把 R76 的旧权范围直接外推。

取 \(w=2^{-67}\)、\(t_*=1+wT_0\)、
\(M_\sigma=M_*+wN_0\)。实际有向计算给
\[
 wT_0<3.842\,10^{-8},\qquad gwN_*<0.115<1/2.
 \tag{81.14}
\]
故下列同一实际常数有效：
\[
 B=2gt_*^2,\quad A=\sqrt{C_e}(1+BM_\sigma),
 \quad L_D=\sqrt{C_e}M_\sigma A,
 \quad L_F=\sqrt{C_e}(M_\sigma B+1).
 \tag{81.15}
\]
即
\[
 \|U\|_{\mathcal V}\le A\|(W_\sigma a,\xi)\|_{X_0}+B\|F_\sigma\|,
\]
\[
 \|(W_\sigma p,\lambda)\|_{Y_0}
 \le L_D\|(W_\sigma a,\xi)\|_{X_0}+L_F\|F_\sigma\|,
 \quad U=W_\sigma u.
 \tag{81.16}
\]
\(F_\sigma(v)=F(W_\sigma v)\)。所有源先按 R76 的真实
\(-JY_z f_{\rm phys}\circ\Theta\) 和真实边界对偶换元形成，再加角权。
R74 的实际常数转折列及其 mean pivot 也未改变：该列的平均通量仍为
\(-E_*\)，且 \(E_*^{-1}<2056.883\)。角权在常数模上为 1，故同一个
有限兼容行可照原式求解；这不消去中央系统剩余的有限低块。

## 4. 有限角导数 form 及不能省去的两条 mean 费用

\(b_{\sigma,j}\) 表示完整形式对共同角平移求 \(j\) 次导数后，再作
同一角权共轭；不是对输入函数另外求 \(j\) 次导数。置
\[
 q_C=1+wN(1,\rho/2)<2,\qquad q_\Gamma=1+wN(1,r/2)<2.
\]
Cauchy 与 R76 的加权 lag 界给，对 \(j\ge1\)，
\[
 \boxed{\quad
 B_j=j!\left[q_CM_C(2/\rho)^j+
                C_tq_\Gamma M_\Gamma(2/r)^j\right],
 \qquad |b_{\sigma,j}(u,v)|\le B_j\|u\|_V\|v\|_V.
 \quad}
 \tag{81.17}
\]
取 \(B_0=M_\sigma\)。这里包含整个非局部 Robin 的真正微分，不把
\(C_H^*\Gamma C_H\) 当作原角 Fourier 乘子。

实际平均密度的正、负权同时有
\[
 \boxed{\quad
 \|W_{\pm\sigma}\partial_\varphi^j(J\phi_0)\|_2
 \le J_j:=2M j!(2/\rho)^j.\quad}
 \tag{81.18}
\]
证明：先用 Cauchy 在半带上控制 \(J^{(j)}\)，再把正、负 Fourier
半轴分别放到上下复带边界，Parseval 给至多 \(\sqrt2\) 倍 sup。
这里 \(|\sigma|\le\rho/4\)、\(\psi(|n|)\le|n|\)；取 2 为安全上界。

完整加权弱式准确为
\[
 b_\sigma(U,v)=F_\sigma(v)+\langle p_\sigma,v(0)\rangle
       +\lambda\langle W_\sigma J\phi_0,v(L)\rangle.
 \tag{81.19}
\]
因此在 \(v(0)=0\) 上，真实第 \(k\) 次角微分满足
\[
 \begin{split}
 b_\sigma(\partial^kU,v)={}&F_\sigma^{(k)}(v)
 -\sum_{j=1}^k\binom kj b_{\sigma,j}(\partial^{k-j}U,v)\\
 &+\lambda\langle W_\sigma\partial^k(J\phi_0),v(L)\rangle,
 \end{split}
 \tag{81.20}
\]
而其 prescribed mean 是
\[
 \ell_\sigma(\partial^kU)=(-1)^k
       \langle U(L),W_{-\sigma}\partial^k(J\phi_0)\rangle.
 \tag{81.21}
\]
最后两式各有一项 \(J_k\) 费用：一条来自未知量的 mean 行，另一条
来自原有 \(\lambda\) 的通量列。即使原输入 \(\xi=0\)，也不能删除它们。

## 5. 实际有限递推及正窗口

令 \(c_t=\sqrt{C_t}\)、\(c_e=\sqrt{C_e}\)、\(C_I\le2\) 为 R69 已付
的完整内部 \(L^2H^{2/3}\) 增益。对源定义
\[
 \mathcal N_k=C_I\|W_\sigma f\|_{L^2H^{k-2/3}}
                +c_t\|W_\sigma d\|_{H^{k-1/2}}.
 \tag{81.22}
\]
它控制所有 \(0\le j\le k\) 的 \(\|F_\sigma^{(j)}\|_{V^*}\)。

以下是准确可执行的非负常数递推。置 \(P_0=A,Q_0=B\)，对 \(k\ge1\)：
\[
 \begin{split}
 P_k={}&A+A c_tJ_kP_0+
 B\left[\sum_{j=1}^k\binom kjB_jP_{k-j}+c_tJ_kL_D\right],\\
 Q_k={}&A c_tJ_kQ_0+
 B\left[1+\sum_{j=1}^k\binom kjB_jQ_{k-j}+c_tJ_kL_F\right].
 \end{split}
 \tag{81.23}
\]
则 \(\|\partial^ku\|_V\) 对 Poisson 数据由 \(P_k\) 控制，对纯源由
\(Q_k\mathcal N_k\) 控制。证明把 (81.20)、(81.21) 逐阶送入同一个
实际低阶逆 (81.16)；mean 行用
\(|\ell_\sigma(\partial^kU)|\le c_tJ_k\|U\|_V\)，通量列用原始
\(|\lambda|\le L_D\|data\|+L_F\mathcal N_k\)。没有假设一条新的低块逆。

取只在转折端延拓的 \(E_-h\)，其 regular trace 为零。于 (81.19)
角积分分部后，\(\lambda\) 项在该 test 上准确为零，从而转折 contact
的导数费为
\[
 Z^P_0=L_D,\quad Z^Q_0=L_F,
\]
\[
 Z^P_k=c_e\sum_{j=0}^k\binom kj B_jP_{k-j},\qquad
 Z^Q_k=c_e\left[1+\sum_{j=0}^k\binom kjB_jQ_{k-j}\right]\quad(k\ge1).
 \tag{81.24}
\]
零阶项已包含完整 \((p,\lambda)\)，高阶项只对 \(p\) 求角导数；
有限标量 \(\lambda\) 不应重复当作一个角函数微分。

对任意非负列 \(a_j\)，记
\(\mathcal B_k(a)=(\sum_{j=0}^k\binom kj a_j^2)^{1/2}\)。Fourier 恒等式
\((1+n^2)^k=\sum_j\binom kj n^{2j}\) 给
\[
 \begin{split}
 \|\mathcal H_\sigma:X_k\to V_k\|&\le\mathcal B_k(P),\\
 \|\mathcal H_\sigma:X_k\to L^2H^{k+2/3}\|&\le C_I\mathcal B_k(P),\\
 \|\Lambda_\sigma:X_k\to Y_k\|&\le\mathcal B_k(Z^P),\\
 \|\mathcal K_\sigma(f,d)\|_{Y_k}&\le\mathcal B_k(Z^Q)\mathcal N_k.
 \end{split}
 \tag{81.25}
\]
所有这些等式可先用角差商和截断权建立，再由一致估计、Fourier
完备化取极限。系数只需所列有限角导数；没有对 C4 径向 knots
求第五阶径向导数，也没有假定退化椭圆算子的未付更大域。

## 6. 负窗口、普通源与 regular 负荷的真实对偶

同一个实际自伴变分问题给完整恒等式
\[
 \mathcal K_{\sigma,f}=-\mathcal H_{-\sigma}^*,\qquad
 \mathcal K_{\sigma,d}=-(\operatorname{Tr}_L\mathcal H_{-\sigma})^*.
 \tag{81.26}
\]
证明与 R45 的 Green 配对相同，使用的是全部 \((a,\xi)\) 数据和
全部 \((p,\lambda)\) contact。正、负权互换不可省去。
因此 (81.25) 的准确对偶为
\[
 \begin{split}
 \|\mathcal K_{\sigma,f}:L^2H^{-k-2/3}\to Y_{-k}\|
     &\le C_I\mathcal B_k(P),\\
 \|\mathcal K_{\sigma,d}:H^{-k-1/2}\to Y_{-k}\|
     &\le c_t\mathcal B_k(P).
 \end{split}
 \tag{81.27}
\]
正窗口的对应常数分别为 \(C_I\mathcal B_k(Z^Q)\) 与
\(c_t\mathcal B_k(Z^Q)\)。正窗口 source 的对偶又给 Poisson 的负
窗口：\(X_{-k}\to L^2H^{-k+2/3}\)，常数
\(C_I\mathcal B_k(Z^Q)\)。\(\Lambda_\sigma^*=\Lambda_{-\sigma}\)
同样给 DN 的负窗口。

相邻整数层插值得到整个有限实窗口。特别，对其中任意 \(t\)：
\[
 \boxed{\quad
 \mathcal K_{\sigma,f}:L^2H^t\longrightarrow
 H^{t+1/3}\oplus\mathbb C,
 \qquad
 \mathcal K_{\sigma,d}:H^t\longrightarrow
 H^{t+1/6}\oplus\mathbb C.
 \quad}
 \tag{81.28}
\]
标量槽取相应插值定义的普通 \(\mathbb C\) norm。两种不同增益分别
来自根 trace \(1/3\) 和 regular trace \(1/2\)，不能把 regular
源也写成根源的 \(1/3\)。输入源仍是实际物理密度拉回后的完整源。

## 7. 真正 onto 的平衡根反射与其全有限窗口

令 \(Q=\langle D_\varphi\rangle^{1/3}\)。先取 regular mean 为零，
保留其通量 \(\lambda\) 作为额外输出。根处平衡 Cauchy 槽为
\[
 x=Qa,\quad y=Q^{-1}p,\qquad
 z_{\rm in}=(x+iy)/\sqrt2,\quad
 z_{\rm out}=(x-iy)/\sqrt2.
 \tag{81.29}
\]
这是实际能量/trace 标架，还没有把它改名为 canonical Airy 标架。

给定 \(z_{\rm in}=h\)，解真实 Robin 形式
\[
 b(u,v)-i\langle Qu(0),Qv(0)\rangle
   =-i\sqrt2\langle h,Qv(0)\rangle+F(v)
 \tag{81.30}
\]
于 test \(\ell(v)=0\)，同时规定 \(\ell(u)=0\)。完整 mean 乘子
照 (81.5) 另行恢复。取相反符号即给定 outgoing 的同一问题。

不带边界条件也有
\[
 \|u\|_2^2\le2L\|u(0)\|_2^2+L^2\|u_x\|_2^2.
\]
所以若
\(c_R=\max\{2L,(1+L^2)/m\}\)，则
\[
 \|u\|_V^2\le c_R
       [b(u,u)+\|Qu(0)\|_2^2].
 \tag{81.31}
\]
将 (81.30) 的形式乘 \(e^{i\pi/4}\)，其实部强制性给实际逆
\(g_R=\sqrt2c_R<2273.762\)。相反符号使用 \(e^{-i\pi/4}\)。
regular mean 是闭子空间，故不破坏该强制性。

加权时仍使用 trial/test 分别 \(T_\sigma,T_{-\sigma}\)。由于
\(e(0)=0\)，新增的虚 Robin 形式在两个运输下**准确不变**，其加权
差仍是 (81.13) 的同一个 \(wN_*\)，没有额外边界小量假设。本次
实际门为
\[
 g_RwN_*<0.294<1/2.
\]
故令
\[
 B_R=2g_Rt_*^2<4547.525,\qquad
 A_R=c_e(1+B_RM_\sigma),\qquad q_R=\sqrt{2C_t}.
 \tag{81.32}
\]
对任意 prescribed regular mean \(\xi\)，有
\(\|U\|_V\le A_R|\xi|+B_R\|F_R\|_{V^*}\)，而 incoming 负荷
的 norm 至多 \(q_R\|h\|_2\)。这个带任意 \(\xi\) 的版本用于下面
真实角微分产生的 (81.21)。

置
\[
 P^R_0=B_Rq_R,\quad Q^R_0=B_R,
 \quad L^R_D=c_eM_\sigma P^R_0,
 \quad L^R_F=c_e(M_\sigma B_R+1).
\]
对 \(k\ge1\) 定义
\[
 \begin{split}
 P^R_k={}&B_Rq_R+A_Rc_tJ_kP^R_0+
 B_R\left[\sum_{j=1}^k\binom kjB_jP^R_{k-j}+c_tJ_kL^R_D\right],\\
 Q^R_k={}&A_Rc_tJ_kQ^R_0+
 B_R\left[1+\sum_{j=1}^k\binom kjB_jQ^R_{k-j}+c_tJ_kL^R_F\right].
 \end{split}
 \tag{81.33}
\]
证明仍是 (81.20)--(81.21)，虚 Robin 项与角微分准确交换。
由于 \(z_{\rm out}=\sqrt2Qu(0)-h\)，同一个实际反射及其相反符号
构造的逆有
\[
 \boxed{\quad
 \|R_\sigma\|_{H^{\pm k}\to H^{\pm k}},\quad
 \|R_\sigma^{-1}\|_{H^{\pm k}\to H^{\pm k}}
 \le1+q_R\mathcal B_k(P^R).
 \quad}
 \tag{81.34}
\]
正窗口直接来自 root trace；负窗口使用
\(R_\sigma^*=(R^{-1})_{-\sigma}\) 及相反符号的同一个正窗口界。
零权时 Green 通量守恒给 \(R^*R=RR^*=I\)，且 opposite Robin
确实给双向满射，因此没有用未经支付的 Fredholm index 或仅单向
范数下界猜测 onto。根常数模仍在 \(Q\) 的 \(n=0\) 槽中。

对于普通源，正窗口的 affine outgoing 为
\[
 \|z_{\rm out}^{,F}\|_{H^k}
 \le q_R\mathcal B_k(Q^R)\mathcal N_k.
 \tag{81.35}
\]
完整 source/contact 的正负窗口仍由第 6 节给出；没有从齐次 unitary
关系删除源。mean-flux \(\lambda\) 也继续由同一完整弱式携带。

## 8. Airy 二阶反射、实际 cutoff 与低块的接口

[R53](R53-corrected-airy-trial-and-common-root-shear.md) 的正侧试解若已
支付同一实际有限 normalizing jets、\(E=y^5e\)、height/Jacobian、
canonical 根迹变换 \(B_\partial\) 和完整 source 常数 \(K_s^+\)，
则其源确实属于 \(L^2H^{s+5/3}\)。本篇 (81.28) 现在给当前实际
whole 正区间上的 contact 增益，而不再把“存在一个高窗口 cap 逆”
留作假设。再乘 R53 的根动量归一化增益 \(1/3\)，得到 \(7/3\)
阶 contact 误差。

准确常数须按实际域复合：对 \(t=s+5/3\)，令 \(C_{\rm ct}(t)\)
为第 6 节相邻整数的插值常数，则该项费用至多
\[
 \|C_A^{-1}B_\partial^*\|_{H^{s+2}\to H^{s+7/3}}
       C_{\rm ct}(s+5/3)\,K_s^+,
 \tag{81.36}
\]
其中边界乘法、复合、周期归一和 shear 必须使用 R47 的真正变换。
(81.34) 是实际能量根标架的有限窗口反射；经过这同一已付边界标架
和 R53 的共同自伴 shear，方可放入
\(R_{\rm cap}^S+I=E_B-R_{\rm cap}^SE_A\)。本篇没有计算那些尚未
输入的 canonical jets，因而不把 (81.36) 的其它因子写成 1。

完整网络的二阶余项若在所有真坐标/源/消元费用之后为 \(K_{\rm tot}\)，
R34 的完整高频主分母为 \(c/|j|\)，累计损失 \(\eta<1\)，则须选
\[
 N\ge\left\lceil(2K_{\rm tot}/c)^{1/(1-\eta)}\right\rceil,
 \tag{81.37}
\]
再对这个**同一** \(N\) 的有限低块及均值行支付真正 Schur 逆。
本篇没有把一个较小的方便截断换入 (81.37)。完整低块仍欠；全局
非线性迭代也还需要相应范数和残差预算。

所列高阶常数保守且增长快；它们支付实际有限窗口存在与强界，不是
已经选定一个可计算低矩阵并证明可逆。下一次改善应针对实际边界/系数
的有限角导数或直接高频块，而不是忽略这些常数后使用同宽 Neumann。
默认 \(k\le12\) 的完整包至少覆盖 R53 中 \(-8\le s\le8\) 所需的
本节 source/contact 和输出反射窗口；其坐标及试解 finite-jet 因子
仍须使用同一个实际对象另付。

## 9. 本次实际运行与冻结

源 `scripts/fourfold_phase_exterior_sobolev_windows.py` 读取三份同一对象的
完整 R69/R74/R76 报告，核对参数盒和全部输入身份，在 256-bit Arb
中支付 (81.11)--(81.34)。默认实际窗口为所有整数 \(0\le k\le12\)
以及相应负窗口和插值层。报告逐阶保存 \(B_j,J_j,P_j,Q_j,Z_j,P^R_j,Q^R_j\)
与所有最终 norm；没有将巨大上界转为浮点无穷。

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_exterior_sobolev_windows.py \
  --out notes/2026-11-12-actual-exterior-sobolev-windows.json
```

实际完整边界模 \(M_\Gamma<434.545\)，Dirichlet 权 Neumann 比率
\(<0.115\)，complex-root Robin 比率 \(<0.294\)，后者的完整
\(V^*\) 逆 \(<4547.525\)。精确数值及 source SHA 均写入报告。
例如普通源正窗口 contact 常数，在 \(k=0,2,4,12\) 可分别安全取
\(9.663\,10^5,8.119\,10^{32},2.041\,10^{60},7.831\,10^{172}\)；
对应反射及其逆的正负窗口常数可取
\(3.430\,10^5,1.881\,10^{33},3.085\,10^{61},2.148\,10^{177}\)。
这些上界全部显示在预算中，不能在全反馈高低频拼接时隐去。
所有结论对 (81.1) 逐点一致，仍不声称 R74 远端好参数选择随参数连续。

本篇支付当前全正侧的高角/源/反射输入。实际返回共轭、Airy 根 jets、
中央完整反馈低块、固定 H 的非线性真尾模块、残差因子 Newton 和
同一精确族仍须继续完成。
