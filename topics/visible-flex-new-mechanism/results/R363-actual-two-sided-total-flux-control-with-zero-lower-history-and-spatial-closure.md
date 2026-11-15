# R363：非零总通量读出的真实双向控制、零低阶历史与空间闭合

> **2026-11-15 R378 更正。** 依赖旧H非零值或秩给出的具体实际通量控制证明已撤回；小环/桥/有限参数论证仅保为“真实完整H确实非零或满秩”前提下的条件结论，不能省去该前提。详见[完整原式更正](R378-correction-of-the-third-history-term-in-the-complete-H-flux.md)。以下旧正文保留供追溯，不作为被撤回结论的当前证明。


日期：2026-11-15。**有限纸面建设性证明；没有运行几何、优化、profile 积分、符号程序或人工测试。**

[R358](R358-nonzero-total-flux-class-of-a-true-velocity-acceleration-cost.md) 已证明一个实际速度—加速度成本的自然总通量读出非零，但没有把该线性空间元素直接当成实际路径。本稿支付这一实际门：选定一个真实紧 profile 后，其同一个自然读出 \(\Lambda\) 在真实有限 \(M=T=0\)、同 scalar germ、frame \(I\to I\) 的路径上可取任意实值，并有紧目标集上的光滑实际截面。可以同时保预定的严格 \(\omega\) 下界，再用原 Klein 词准确闭合空间位移。

关键尺度兼顾两件事：快速小幅段的真实矩阵趋零，而所需第四商读出按两号无界增长。端点／矩阵桥只需一个固定光滑小邻域，全部真实桥成本有界。其完整第三历史不被假设小；先得到真实 \(M=0\)，再用整块真倒行准确消第三，第四成本是同号两倍。

来源：[R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md)、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R134](R134-acceleration-layer-from-complete-local-v4.md)、[R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md)、[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)、[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)、[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md)及 R358。

## 1. 精确目标与固定物理域

固定一个有 \(0\) 内点的有限 profile 区间 \(I=[\ell,r]\)，同一右 collar 和右锚。取
\[
\Omega>\max(0,-\ell)+1,\qquad B>\Omega+2,\qquad
S_B=(h,k,\omega)=(1,B,B).
\tag{1}
\]
因此 \(d=h\omega-k=0\)。本稿所有几何均要求
\[
h>0,\qquad \omega>\Omega,\qquad x+\omega>1\quad(x\in I).
\tag{2}
\]
辅助 profile 可以放在 \(I\) 内固定的右侧小区间；不会随着几何路径逐段改锚。

R352 给实际成本空间 \(U\) 上的线性泛函
\[
\Lambda_u(V)=\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)),
\qquad \Lambda_u(R)=0.
\tag{3}
\]
这里整个有序尾映射 \(\mathscr G\) 保留。先在第2节选定一个真实 \(u\)，以后固定这个同一个 \(\Lambda=\Lambda_u\)。不允许随着目标值或路径另换 profile 读出。

结论是单个明确标量观察的实际满射。它没有同时规定完整 pure、whole self 或全部其它通量值，亦不把一个观察满射称为整个 \(U\) 成本可控。

## 2. 在任意预定 ω 下界上取得同一非零 H 系数

以真实速度
\(\gamma=h_s,\delta=d_s\) 为坐标，则
\[
k_s=2\omega\gamma-2\delta,\qquad
\omega_s=\frac{\omega\gamma-\delta}{h}.
\tag{4}
\]
R129 正规式中的第四导数权部分，在施加 \(\Lambda\) 后可写成
\[
\Lambda(\widetilde H_\gamma)\gamma
(\gamma\delta_s-\delta\gamma_s)
+\Lambda(\widetilde H_\delta)\delta
(\gamma\delta_s-\delta\gamma_s)
+\text{速度四次式}.
\tag{5}
\]
原加速度平方系数在每个实际状态都由 R350 被 \(\Lambda\) 准确消去。因而坐标变化从它们产生的附加线性加速度项也为零；不是只在一个基点删其 leading 值。
原 H 系数满足
\[
\Lambda(\widetilde H_\gamma)
=-2\Lambda(H_1+2\omega H_2),\qquad
\Lambda(\widetilde H_\delta)=4\Lambda(H_2).
\tag{6}
\]

R358 的完整速度一形式及其 curl 只使用 \(h,d\)、
\(e=hx+d,Q=1+e^2\) 和 \(\gamma,\delta\)。
该稿的第二 history 导数、ZZ 的 \(P,B\) 项和两个有序尾都已包括在这个式中。
所以其 \(h=1,d=0\) 的同一系数计算适用于 \(S_B\)，不依赖另一个独立的 \(k=\omega=B\)。
R134 的 \(\mathcal B_{m_2}N_2\) 修正是速度四次式，也不改变(5)的 H 系数。

具体地，对任一紧光滑 \(u_0\)，令
\(u_\rho(x)=u_0(x/\rho)\)，R358 的完整有限 Laurent 式给
\[
\Lambda_{u_\rho}(\widetilde H_\gamma(S_B))
=-\frac{\rho^{-9}}{57600}\int(u_0'')^5+O(\rho^{-8}).
\tag{7}
\]
(7)是原真权系数身份，使用完整 primitive 与同锚缩放，不是执行新的窄包试验。
取 R358 的三个真实不交偶 bump，使
\(\int(u_0'')^5>0\)。
选择一次足够小但有限的 \(\rho>0\)，使 \(u=u_\rho\) 支撑在 \(I\) 内0附近，并有
\[
\boxed{\lambda_*:=\Lambda_u(\widetilde H_\gamma(S_B))\ne0.}
\tag{8}
\]
其原三矩匹配辅助包选在 \(u\) 右侧的三个固定小区间，全部仍在 \(I\) 内。
从现在起 \(\rho,u,\Lambda,\lambda_*\) 一律固定。

## 3. 在完整局部密度上使用 Λ

R109 的完整局部密度为
\[
L=v-\mathcal B_mN=L_0+L_2+L_4,
\qquad m=m_0+m_2,
\tag{9}
\]
其中 \(m_2\) 是真实速度二次式。
它保留原第二、第三 history 的真实导数；不把历史值置零的操作提前到微分以前。

取 R105/R130 的一个固定有限真实环境 \(E\)，含 \(U,R\) 及全部局部系数。
将(3)从 \(U\) 线性延拓到 \(E\)，记为 \(\ell\)。
等价地，可先固定上节的真实有序辅助方案，在所用有限原式上定义这个线性读出。
后文从不要求单个局部模板属于 \(U\)，也不把 \(\ell\) 在 \(U\) 外的数值称为自然不变量。

所有 \(\overline A,H\) 的实际状态值都属于 \(U\)，故其 \(\ell\) 值准确等于(3)。
尤其
\[
\ell(\overline A_{hh}(S))
=\ell(\overline A_{hk}(S))
=\ell(\overline A_{kk}(S))=0
\quad\text{对每个 }S.
\tag{10}
\]
真实路径两端为常值 germs 时，R129 的显式正导数权端势分别为零。
在 \((h,d)\) 速度坐标下，施加 \(\ell\) 后的积分因此精确具有
\[
\begin{aligned}
\int\ell(L)\,ds
=\int\bigl\{&
\ell(L_0(S))+Q_2^\ell(S;\gamma,\delta)\\
&+[\lambda_\gamma(S)\gamma+\lambda_\delta(S)\delta]
(\gamma\delta_s-\delta\gamma_s)
+Q_4^\ell(S;\gamma,\delta)\bigr\}\,ds ,
\end{aligned}
\tag{11}
\]
其中 \(Q_2^\ell,Q_4^\ell\) 分别速度二次、四次；
\(\lambda_\gamma=\Lambda(\widetilde H_\gamma)\)、\(\lambda_\delta=\Lambda(\widetilde H_\delta)\)。
一切状态导数与原 \(N_0,N_2\) 成本均留在这些有限光滑系数中。

**使用(11)的边界：**它是完整局部积分的身份。只有在整条路径总 \(M=0\) 后，才由 R109 推出它等于真正 canonical 成本的 \(\Lambda\) 值。下节的短段尚不满足 \(M=0\)，故不提前作这个等同。

## 4. 一族真实快速小幅段

取一个非零、非负、偶的
\(\psi\in C_c^\infty((-1,1))\)，记
\[
A_\psi=\int\psi(\psi')^2>0.
\]
对 \(\sigma\in[-1,1]\)、小正幅 \(\varepsilon\)，取真实时长因子
\[
\tau=\varepsilon^{3/2},\qquad s=\tau t,\quad -1\le t\le1,
\]
并准确指定
\[
h_s=\frac{\varepsilon}{\tau}\psi(t),\qquad
d_s=\frac{\varepsilon}{\tau}\sigma\psi'(t).
\tag{12}
\]
从同一状态 \(S_B\) 积分 \(h,d\)，再解(4)的 \(\omega\)，置 \(k=h\omega-d\)，并积分真实 frame 方程。
这是一条实际水平几何，不是独立指定不相容 jets。
两端有开常值 germs；末 scalar 无需等于起点。

对全部 \(\sigma\in[-1,1]\)，包括一次 \(\sigma\) 导数，
\[
S_{\varepsilon,\sigma}=S_B+O_{C^1(\sigma)}(\varepsilon).
\tag{13}
\]
因此充分小的实际 \(\varepsilon>0\) 使该段始终有
\(h>1/2,\ \omega>\Omega+1\)。
frame 末值为
\[
F_{\varepsilon,\sigma}=I+O_{C^1(\sigma)}(\tau),
\tag{14}
\]
因为真实 \(k\) 在紧状态盒内有界；没有把 frame 方程按改变时长后的旧解复用。

R73 的真实矩阵密度只有导数权0、2，所以
\[
M_{\varepsilon,\sigma}
=O_{C^1(\sigma)}(\tau)
 +O_{C^1(\sigma)}(\varepsilon^2/\tau)
=O_{C^1(\sigma)}(\varepsilon^{1/2}).
\tag{15}
\]
端 scalar、frame 和矩阵目标都趋向一个固定有限端点数据。
第三历史可能很大，本稿不对它作小量假设。

## 5. 原 H 项给准确领先双号，所有低权成本有明确阶

记
\[
K_\psi=\psi\psi''-(\psi')^2 .
\]
真实一次分部积分和奇偶性给
\[
\int\psi K_\psi=-3A_\psi,\qquad
\int\psi'K_\psi=0.
\tag{16}
\]
将(12)代入(11)，H 项为
\[
\frac{\varepsilon^3}{\tau^3}
\int [\lambda_\gamma(S_{\varepsilon,\sigma})\psi
+\sigma\lambda_\delta(S_{\varepsilon,\sigma})\psi']
\,\sigma K_\psi\,dt.
\]
由(8)、(13)、(16)，这是
\[
\frac{\varepsilon^3}{\tau^3}
\{-3A_\psi\lambda_*\sigma+O_{C^1(\sigma)}(\varepsilon)\}.
\tag{17}
\]
两个其它真实阶数分别为
\[
\int Q_4^\ell\,ds=O_{C^1(\sigma)}(\varepsilon^4/\tau^3),\quad
\int Q_2^\ell\,ds=O_{C^1(\sigma)}(\varepsilon^2/\tau),\quad
\int\ell(L_0)\,ds=O_{C^1(\sigma)}(\tau).
\tag{18}
\]
这些界的常数由固定 compact 状态盒、固定 \(u,\psi\) 和完整有限局部系数决定。
含 \(N_0,N_2\) 的项没有删去；它们处于(18)的相应项中。

设 \(c_*=-3A_\psi\lambda_*\ne0\)。把 \(\tau=\varepsilon^{3/2}\) 代入，短段 \(B_{\varepsilon,\sigma}\) 的完整局部积分为
\[
\boxed{
I_\ell(B_{\varepsilon,\sigma})
=\varepsilon^{-3/2}
\{c_*\sigma+O_{C^1(\sigma)}(\varepsilon)\}
+O_{C^1(\sigma)}(\varepsilon^{1/2}).
}
\tag{19}
\]
省写的静态 \(O(\varepsilon^{3/2})\) 已收入最后一项。

(19)成立的决定性条件是(10)在每一个真实状态都准确为零。
若只在 \(S_B\) 把加速度平方项 leading 系数设零，其状态变化可能产生更大的项，论证便无效。本稿使用的是 R350 的全状态结论。

## 6. 一个固定光滑桥族准确支付 frame、scalar 与 M

由 R354 §8—9 的受控 \(\omega\) 桥加强版 R70，可在一个固定小端点邻域内选择光滑有限桥
\[
C_{\varepsilon,\sigma}:
(S_{\varepsilon,\sigma}^{\rm out},F_{\varepsilon,\sigma})
\longrightarrow(S_B,I)
\]
并准确指定矩阵
\[
M_C=-M_{\varepsilon,\sigma}.
\tag{20}
\]
桥从短段实际末 frame 起接，所需相对 frame 为其逆。
这里的 \(-M\) 是真实可达的八矩目标，不是给第四成本取负。

由(13)—(15)，所有目标都在同一个固定邻域内。
R70 的辅助整数与拼接方式因此只需选择一次并冻结；R354 的真实 boost 保
\(\omega>\Omega\)。
桥族的真实长度、状态以及所需有限几何 jets 在这个闭参数盒上有界，且光滑依赖目标。因此
\[
I_\ell(C_{\varepsilon,\sigma})=O_{C^1(\sigma)}(1).
\tag{21}
\]
这是实际局部积分的有界性，不宣桥的完整传入历史成本独立或为零。
其参数依赖包括真实段长；没有把变长桥任意重参数化以后继续沿用旧 frame/成本。

拼成
\[
D_{\varepsilon,\sigma}=B_{\varepsilon,\sigma}C_{\varepsilon,\sigma}.
\]
它已真实满足同一 scalar germ、frame \(I\to I\)、总 \(M_D=0\)。
完整第三 \(T_D\) 仍保真实值。
由于局部积分可加，(19)、(21)给
\[
I_\ell(D_{\varepsilon,\sigma})
=\varepsilon^{-3/2}\{c_*\sigma+O_{C^1}(\varepsilon)\}
+O_{C^1}(1).
\tag{22}
\]

现在才应用 R109：
\[
V_D-\int_D L\,ds\in R .
\tag{23}
\]
(23)中原 \(\mathcal B_mH\) 和
\(\mathcal B_A(\tau_{A,m})/6\) 两个真实累计 history 均保留，只由 \(\ell(R)=0\) 消去读出。
所以(22)准确等于完整 canonical 成本的 \(\Lambda(V_D)\)；不是以局部 forcing 替换一个非零矩路径的总成本。

## 7. 整块真倒行准确消第三，不用它取负第四

因 \(D\) 的总 M 为零、scalar 同端口且 frame I，R83 的原真倒行给
\[
M_{D^{\rm rev}}=0,\qquad
T_{D^{\rm rev}}=-T_D,\qquad
V_{D^{\rm rev}}=V_D.
\]
令
\[
P_{\varepsilon,\sigma}=D_{\varepsilon,\sigma}
D_{\varepsilon,\sigma}^{\rm rev}.
\tag{24}
\]
两段各 M0，完整第四传递交叉项准确为零。因此
\[
\boxed{
M_P=T_P=0,\qquad V_P=2V_D.
}
\tag{25}
\]
frame、scalar 和常值 germs 均准确闭合；(2)的 \(\omega\) 下界也保持。
特别 \(2V_D\) 是实际定义 \(U\) 的一个成本，因此上节 \(V_D\in U\)，其自然读出使用合法。
(24)没有把未知、可能很大的 \(T_D\) 当成小项。

定义同一个实际族的标量
\[
\Phi_\varepsilon(\sigma)=\Lambda(V_{P_{\varepsilon,\sigma}}).
\]
由(22)得到
\[
\Phi_\varepsilon(\sigma)
=2\varepsilon^{-3/2}
\{c_*\sigma+O_{C^1}(\varepsilon)\}+O_{C^1}(1).
\tag{26}
\]
所以充分小的有限 \(\varepsilon\) 上，
\(\partial_\sigma\Phi_\varepsilon\) 全区间不为零，符号为 \(c_*\)。
两端值在 \(\varepsilon\downarrow0\) 时分别趋于异号无穷。
这是实际完整成本的双号；不是形式 \(H\) 系数的正负幅组合。

给任意目标 \(z\in\mathbb R\)，选一次足够小但有限的 \(\varepsilon>0\)，使两端值夹住 z。
中间值定理给唯一的实际 \(\sigma\in(-1,1)\)，准确满足
\[
\boxed{\Lambda(V_P)=z.}
\tag{27}
\]
对任意固定紧目标集，可选同一个有限 \(\varepsilon\)，使整个目标集位于两端像的内部。
非零导数与有限维隐函数定理给一个光滑的 \(\sigma(z)\)，从而给同一有限拼接类型、真实正长度的实际路径截面。

(27)不保证该路径的完整成本为零，也不保持其它未列出的观察值。

## 8. 可在同一物理域中准确闭合空间位移

\(P_{\varepsilon,\sigma}\) 的空间末位移一般非零。
不能因 frame I 就把它称为空间闭环。

先固定两条同 \(S_B\) germ 的真实 frame 桥 \(C_1,C_2\)，使
\[
M_{C_j}=T_{C_j}=0,\qquad
F_{C_j}:I\to g_j,\quad
g_1=\operatorname{diag}(1,-1,-1),\
g_2=\operatorname{diag}(-1,1,-1).
\tag{28}
\]
它们可由 R210 的既有桥经 R354 的共同 \(\omega\) 平移与真实 M0 夹心安装到当前端口，并保 \(\omega>\Omega\)。
夹心中的第三 history 按原真倒行相消；其第四成本全部留作固定基准。
只需两条固定有限桥，不随 \(\varepsilon,\sigma\) 增长。

设第一 prototype 为 \(P_{\varepsilon,\sigma}C_1\)，第二为 \(C_2\)，使用 R210 的同一个 Klein 八边词
\[
1,2,1,2,2,1,2,1.
\tag{29}
\]
每种 prototype 在
\(\{I,g_1,g_2,g_1g_2\}\) 四个 ambient 左旋位置各出现一次。
这四个矩阵之和为零，故两种 prototype 的**整个实际位移**分别准确相消；不要求任何单段位移为零。
全部 scalar/frame germs 同时闭合。

所有段 M0，且(25)、(28)使总 T0。
原 R83 完整成本于是准确为
\[
V_X=4V_P+4V_{C_1}+4V_{C_2}.
\tag{30}
\]
设固定基准
\(b_*=\Lambda(4V_{C_1}+4V_{C_2})\)。
桥各自 frame 非 I 时，可先在同一个有限环境使用 \(\ell\)；(30)的固定总和与 \(V_X,V_P\) 属 U，所以 \(b_*\) 的自然值无歧义。
对指定目标 z，在(27)取
\(\Lambda(V_P)=(z-b_*)/4\)，则
\[
\boxed{
X\text{ 空间/frame/scalar准确闭合},\quad
M_X=T_X=0,\quad\Lambda(V_X)=z,\quad \omega>\Omega .
}
\tag{31}
\]
同样给紧目标集上的光滑有限截面。
真实带在(2)内正则；这只证明闭正则浸入数据，不证明嵌入或 reach。

若另有一个固定 M0、非零第三 hook 的基准 prototype，可把(25)的零低阶模块作为同一第一 prototype 的前缀。
它保持原 hook；完整成本只增加四份 \(V_P\)，基准仍全部保留。
这样可调这一读出，但任何同时已付 pure/self/其它通量条件都必须另作联合控制，不能据此宣称免费保持。

## 9. 准确结论及保留范围

本稿将 R358 的一个非零 \(U/R\) 类推进为真实路径上的标量控制：
\[
\Lambda(\mathcal S)=\mathbb R
\]
对同一固定 profile 的自然读出成立，其中 \(\mathcal S\) 是指定端口、严格物理下界内的实际有限 M0/T0/frame-I 路径成本集合。
紧目标集有同一有限参数族中的光滑截面；空间闭合也能用固定真实桥和原 Klein 词同时完成。

论证保留全部桥基准、全部 canonical history、真实第三成本、物理域和有限选择顺序。所有最终 \(\rho,\varepsilon,\tau\)、辅助圈数及段长都为严格正或有限的实际值；极限只用来证明某个有限选择满足严格不等式。

这排除了“该特定 \(\Lambda\) 在实际成本上必为单号”这一障碍。
它不排除别的正性泛函，不说明整个商为一维，不给全部成本的正锥，更不替代当前弱圆的所有第四 period、同一规范 joint、高阶收敛、固定 g 的有限嵌入族或主课题的 reach／幅度门。
