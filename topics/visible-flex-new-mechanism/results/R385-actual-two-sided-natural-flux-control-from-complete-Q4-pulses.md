# R385：由完整 Q4 成本实现一个自然总通量的真实双向控制

日期：2026-11-15。**有限纸面构造；没有执行新的 profile 积分、几何运行、符号程序、旧根恢复、秩计算或人工检查。**

[R382](R382-universal-cancellation-of-the-corrected-H-total-flux-and-independent-Q4.md)
证明全部真实 H 系数被自然总通量消去；旧 H 非零值不能用于实际控制。
本稿使用 [R370](R370-complete-quartic-velocity-cost-and-exact-C2-total-flux.md)
独立给出的完整 Q4 值，构造一个不同的实际入口。

固定同一个真实紧 profile $u$，其自然读出为
$$
\Lambda_u(V)=\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\tag{1}
$$
$\mathscr G$ 始终是 [R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 的原 pure 有序 $2+2$ 真实三矩尾映射。
本稿证明：可以预先固定一个常值端口、共同物理窗口和严格 $\omega$ 下界，使
$\Lambda_u$ 在实际有限 $M=T=0$、frame 恒等闭合路径上取任意实值，
并在每个紧目标集上有同一有限拼接类型中的光滑截面。
进一步用原固定 Klein 词同时闭合空间位移。

这是一个固定标量读出的实际控制；不把 Q4 的两个独立函数方向自动当作两个实际自由度，也不保持另一个旧几何的度量或未列出的高阶观察。

## 1. 一次固定 profile、右锚与物理域

取一个非零非负偶的紧光滑 bump $\eta$，使下列三个支撑互不交：
$$
r(x)=\eta(x-x_0)
-\frac12\eta(x-x_0-b)
-\frac12\eta(x-x_0+b).
$$
准确有 $\int r=\int xr=0$。按同一个右锚置 $u=J^2r$，则
$u\in C_c^\infty(I)$、$u''=r$。定义
$$
M_5=\int r^5=\frac{15}{16}\int\eta^5>0,\qquad
X_5=\int xr^5=x_0M_5,\qquad
d_*=-\frac{X_5}{M_5}.
\tag{2}
$$
也可以从一开始固定任何满足 $M_5\ne0$ 的真实紧 profile；
后文只使用这个非零条件。

先取一个有限共同窗口 $I=[\ell,r_*]$，包含全部支撑及所需实际右辅助包，
两侧保开 collar。固定
$$
\Omega>\max(0,-\ell)+1.
\tag{3}
$$
取小正参数宽度 $a>0$，再取足够大的有限 $K$，使
$$
K+d_*-a>\Omega+2.
\tag{4}
$$
共同端口为常值 germ
$$
S_0=(h,k,\omega)=(1,K,K+d_*).
$$
另定义固定小区间中的中心状态
$$
S_\sigma=(1,K,K+d_*+\sigma),
\qquad -a\le\sigma\le a.
\tag{5}
$$
如果下面的光滑桥邻域需要，可以一次缩小 $a$。
所有之后的目标都使用同一个 $u$、右锚、自然读出和端口 $S_0$。

## 2. 原完整密度在纯 δ 方向的准确值

令
$$
d=h\omega-k,\qquad\gamma=h_s,\qquad\delta=d_s.
$$
原水平关系等价于
$$
k_s=2\omega\gamma-2\delta,\qquad
\omega_s=\frac{\omega\gamma-\delta}{h}.
\tag{6}
$$
沿 $h=1,\gamma=0$ 的方向，$k_s=-2\delta$、$\omega_s=-\delta$。

[R109](R109-local-density-of-the-complete-fourth-quotient.md) 的完整局部密度为
$$
L=v-\mathcal B_mN=L_0+L_2+L_4.
$$
按原 [R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md) 的真实 $s$ 分部积分正规化，$L_4$ 包含加速度平方、
速度—加速度 H 项以及完整速度四次项；$N_0,N_2$ 校正全保。

固定一个含全部所用局部模板及 $U,\mathcal R$ 的有限真实环境，
将 (1) 线性延拓为 $\ell$，并要求它在 $U$ 上与原自然读出一致、在 $\mathcal R$ 上为零。这是处理尚未总 $M=0$ 的短段所需的有限局部记号；
以后只有在原 R109 的总矩阵假设已满足时，才把局部积分等同于真实
canonical 成本的自然值。

[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md) 的三个加速度平方系数在每个实际状态上的 $\Lambda$ 值均为零。
R382 又给两个 H 系数在每个实际状态上的 $\Lambda$ 值均为零。
纯 $\delta$ 方向本身也没有速度面积；但本稿保持这两个全状态原结论，
不通过只在基点置零来删除大项。

原完整正规 Q4 系数属于 $U$，R370 给
$$
\boxed{
\Lambda_u(\mathcal Q_\delta(1,k,k+d))
=\frac{X_5+dM_5}{80}.}
\tag{7}
$$
因此短段的完整局部积分准确具有
$$
\int\ell(L)\,ds
=\int\left\{
\frac{X_5+dM_5}{80}\delta^4
+q_2(S)\delta^2+q_0(S)
\right\}\,ds .
\tag{8}
$$
$q_2,q_0$ 保留原 $N_0,N_2$、静态项和全部正常化余项。
它们在后面固定的 compact 状态盒上光滑有界。

(8) 所用显式正导数权端势在常值 germs 为零；短段的 scalar 首末也完全相同。
没有留下一个被省去的快速端点成本。
桥段中的全部真实局部成本则另行保留，不能由 (8) 假称为零。

## 3. 一个真实、首末 scalar 相同的快速小幅脉冲

固定非零
$\psi\in C_c^\infty((-1,1))$，可取偶且非负。
定义
$$
c_4=\int_{-1}^1(\psi')^4>0.
$$
对小正 $\varepsilon$ 取
$$
\tau=\varepsilon^{3/2},\qquad s=\tau t,\quad -1\le t\le1,
$$
并准确设
$$
\begin{aligned}
h(s)&=1,\\
d(s)&=d_*+\sigma+\varepsilon\psi(t),\\
k(s)&=K-2\varepsilon\psi(t),\\
\omega(s)&=K+d_*+\sigma-\varepsilon\psi(t).
\end{aligned}
\tag{9}
$$
这些量逐点满足 $d=h\omega-k$ 及 (6)。
本稿的 $\varepsilon$ 只缩短几何脉冲、缩小其状态幅度；不缩放固定的 profile $u$。

两端有开常值 germs，并都等于 $S_\sigma$。
充分小的有限 $\varepsilon>0$ 保
$\omega>\Omega+1$；$h$ 恒为1。
真实 frame 方程照原式积分，不以重参数化的旧 frame 解代替。
因为 $k$ 在固定盒内有界，末 frame 满足
$$
F_{\varepsilon,\sigma}=I+O_{C^1(\sigma)}(\tau).
\tag{10}
$$
这里 frame 甚至不依赖 $\sigma$，但不需要利用这一加强。

R73 的真实矩阵密度只有导数权零与二，故短段 $B_{\varepsilon,\sigma}$ 的矩阵满足
$$
M_{B_{\varepsilon,\sigma}}
=O_{C^1(\sigma)}(\tau+\varepsilon^2/\tau)
=O_{C^1(\sigma)}(\varepsilon^{1/2}).
\tag{11}
$$
第三历史与第四成本没有由 (11) 被假定为小量。

## 4. 完整 Q4 给严格的线性双号领先项

在 (9) 上
$$
\delta=\frac{\varepsilon}{\tau}\psi'(t),\qquad
X_5+d(s)M_5=M_5\{\sigma+\varepsilon\psi(t)\}.
$$
所以 (8) 的 Q4 积分可直接准确写为
$$
\frac{\varepsilon^4M_5}{80\tau^3}
\left\{
c_4\sigma+\varepsilon\int\psi(\psi')^4
\right\}.
\tag{12}
$$
另两项满足
$$
\int q_2(S)\delta^2\,ds=O_{C^1(\sigma)}(\varepsilon^2/\tau),\qquad
\int q_0(S)\,ds=O_{C^1(\sigma)}(\tau).
$$
所有余项及其一次 $\sigma$ 导数在固定参数盒上统一有界。

置
$$
c_*=\frac{M_5c_4}{80}>0.
$$
由 $\tau=\varepsilon^{3/2}$，
$$
\boxed{
I_\ell(B_{\varepsilon,\sigma})
:=\int_{B_{\varepsilon,\sigma}}\ell(L)\,ds
=c_*\varepsilon^{-1/2}\sigma
+O_{C^1(\sigma)}(\varepsilon^{1/2}).}
\tag{13}
$$
这是新机制的准确阶：第四读出变大，而真实矩阵 (11) 趋零。
双号来自中心状态 $\sigma$；所有脉冲时长、幅度与实际拼接次数都为正或有限，
没有使用负路径。

此时短段一般仍有非零矩阵。本节只得到局部积分 (13)，尚未称它为
$\Lambda(V_B)$。

## 5. 固定光滑桥族，先准确达到总 M0

[R354](R354-complete-reflection-and-positive-omega-bridges-pay-three-remaining-Gaussian-moments.md) §8–9 的受控 $\omega$ 版 R70 给光滑有限 frame/scalar/矩阵桥。
在固定小邻域内，端数据和矩阵目标均可同时光滑变化；辅助整数与拼接类型选定一次。

对 (10)、(11) 的实际端数据选择桥
$$
C_{\varepsilon,\sigma}:
(S_\sigma,F_{\varepsilon,\sigma})\longrightarrow(S_\sigma,I),
\qquad
M_C=-M_{B_{\varepsilon,\sigma}},
\tag{14}
$$
全程 $\omega>\Omega$。
其相对 frame 目标是短段实际末 frame 的逆。
因为所有目标都在同一个固定小邻域内，真实长度、状态及所需有限 jets
在整个闭参数盒上一致有界，并光滑依赖 $\sigma$。
包括真实变长成本在内，
$$
I_\ell(C_{\varepsilon,\sigma})=O_{C^1(\sigma)}(1).
\tag{15}
$$
不把桥当成空路径，不把它的第三或第四基准置零。

拼成
$$
D_{\varepsilon,\sigma}=B_{\varepsilon,\sigma}C_{\varepsilon,\sigma}.
$$
它真实满足同一 $S_\sigma$ 端口、frame $I\to I$ 和总矩阵 $M_D=0$。
现在才应用 R109 的完整历史公式：
$$
V_D-\int_D L\,ds\in\mathcal R.
\tag{16}
$$
该公式保留真实累计 second/third 字段；余下响应只是在 $\ell$ 下为零。
因此
$$
\Lambda(V_D)
=c_*\varepsilon^{-1/2}\sigma+O_{C^1(\sigma)}(1).
\tag{17}
$$
其 $U$ 成员资格也可由下一节的真实倒行立即取得，而非把非零矩短段冒作 $U$ 成本。

## 6. 原真倒行消第三，并保同号第四成本

这里使用 [R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md) 的完整向量场/历史公式，不能将形式时间反向当作成本取负。

对任一上述 $M_D=0$ 路径，设
$b=-2T_D(\phi;D_{\rm profile})$ 为其真实 third scalar 末值。
原真倒行的第三场是
$$
Z_3^{\rm rev}=-OZ_3\circ{\rm rev}+Y_b^{\rm rev}.
\tag{18}
$$
第二项是保持 canonical 零起点所需的真实端历史修正。
它在第四 forcing 中多出 $-2H(Y_\phi,Y_b)$，
其完整 scalar 成本为 $-2A_D(\phi,b)=0$，
因为整个矩阵 $A_D=\Phi_{M_D}$ 为零。
所以原完整结论是
$$
M_{D^{\rm rev}}=0,\qquad
T_{D^{\rm rev}}=-T_D,\qquad
V_{D^{\rm rev}}=+V_D.
\tag{19}
$$

令
$$
P_{\varepsilon,\sigma}
=D_{\varepsilon,\sigma}D_{\varepsilon,\sigma}^{\rm rev}.
$$
R83 的完整第四传递式在两段各 $M=0$ 时所有交叉项准确为零，
无论 $T_D$ 多大。因此
$$
M_P=T_P=0,\qquad V_P=2V_D.
\tag{20}
$$
全部 scalar/frame germs准确闭合，物理下界也保留。
特别 $2V_D\in U$，故 $V_D$ 的自然读出 (17) 有确切线性空间含义；
并没有实际执行“半条路径”。

## 7. 把不同中心运输到同一个固定端口

还不能把 $P_{\varepsilon,\sigma}$ 的变化中心端口当成共同端口。
再用 R354/R70，预先选定一个光滑有限桥族
$$
B_\sigma:S_0\longrightarrow S_\sigma,\qquad
M_{B_\sigma}=0,\qquad F_{B_\sigma}:I\to I,
\tag{21}
$$
始终 $\omega>\Omega$，两端为指定常值 germs。
$\sigma$ 只在一次固定的小区间 $[-a,a]$ 内变化。
其长度、全部有限 jets、真实 canonical 成本及一次参数导数有界。
$B_0$ 可以是非空路径；其成本完整保留。

用同一个真实逆字拼成
$$
Q_{\varepsilon,\sigma}
=B_\sigma P_{\varepsilon,\sigma}B_\sigma^{\rm rev}.
\tag{22}
$$
三段各 $M=0$，且 (19) 对 $B_\sigma$ 同样保真。
所以
$$
M_Q=T_Q=0,\qquad
F_Q=I,\qquad
V_Q=2V_{B_\sigma}+2V_D.
\tag{23}
$$
它们的共同首末 scalar germ 现在严格是固定的 $S_0$。
$B_\sigma$ 自己的第三量不需要为零，它由真正的反向桥准确相消。
$2V_{B_\sigma}$ 也由 $B_\sigma B_\sigma^{\rm rev}$ 给出实际 $U$ 资格。

定义这个固定端口族的实际读出
$$
\Phi_\varepsilon(\sigma)=\Lambda(V_{Q_{\varepsilon,\sigma}}).
$$
结合 (17)、(21) 的完整桥基准，
$$
\boxed{
\Phi_\varepsilon(\sigma)
=2c_*\varepsilon^{-1/2}\sigma+O_{C^1(\sigma)}(1).}
\tag{24}
$$
所有桥项都在余项中，包括其对中心的实际导数。

取充分小但有限的 $\varepsilon$，则
$\partial_\sigma\Phi_\varepsilon>0$ 在整个 $[-a,a]$ 成立。
两端值分别趋向负、正无穷。对任意固定紧目标集，
可一次选择同一个正 $\varepsilon$，使整个目标集严格位于两端像内。
中间值定理与非零导数给唯一的光滑逆
$\sigma=\sigma(z)$，从而准确支付
$$
\boxed{\Lambda(V_{Q_{\varepsilon,\sigma(z)}})=z.}
\tag{25}
$$
这是同一有限拼接类型、同一固定端口、同一 profile 读出的实际截面。

## 8. 固定 Klein 词准确闭合空间位移

frame 恒等不等于空间位移闭合。
取 [R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) 的两条固定真实 $M=T=0$ frame 桥，借 R354 的 $\omega$ 平移与真实
M0 夹心安装到端口 $S_0$，并保 $\omega>\Omega$：
$$
C_j:I\to g_j,\qquad
g_1=\operatorname{diag}(1,-1,-1),\quad
g_2=\operatorname{diag}(-1,1,-1).
\tag{26}
$$
这些桥不依赖 $\varepsilon,\sigma$，全部第四基准保留。

第一 prototype 取 $Q_{\varepsilon,\sigma}C_1$，第二取 $C_2$，
用原八边词
$$
1,2,1,2,2,1,2,1.
\tag{27}
$$
每种 prototype 在四个 ambient 左旋位置
$\{I,g_1,g_2,g_1g_2\}$ 各出现一次。
四个矩阵之和为零，所以两种 prototype 的整个真实位移分别准确相消。
这个论证使用变化后的完整 prototype 位移，没有将插入块的位移设零。

所有段均 M0/T0，原 R83 全函数传递给
$$
V_X=4V_Q+4V_{C_1}+4V_{C_2},\qquad M_X=T_X=0.
\tag{28}
$$
令固定基准
$$
b_*=\Lambda(4V_{C_1}+4V_{C_2}).
$$
该和本身由固定 Klein 闭合字给出实际 $U$ 成员，
故自然值无歧义；不要求每个非恒等 frame 桥单独属于指定闭路径集合。

在 (25) 中取目标 $(z-b_*)/4$，则
$$
\boxed{
\Lambda(V_X)=z,\quad
M_X=T_X=0,\quad
\text{scalar、frame 与空间位移全部闭合},\quad
\omega>\Omega.}
\tag{29}
$$
紧目标集上的光滑截面保持。
原 $\alpha_s=h^2T$ 与 $x+\omega>1$ 给真实闭正则浸入数据；
这里没有证明嵌入、reach 或宏观幅度。

## 9. 有限选择次序及实际范围

选择次序是：先固定 $u$、全部实际辅助包、$I$ 和 $\Omega$；
再固定 $K,a,\psi$、端口 $S_0$、光滑桥类型及其有限辅助整数；
随后对指定紧目标集一次选定正的有限 $\varepsilon$ 和
$\tau=\varepsilon^{3/2}$；最后只由实际逆函数选择 $\sigma(z)$。

没有取零时长路径、无穷复制或实数次拼接。
参数变化选择的是不同真实几何；本稿不把它们称为同一个冻结的 $g$，
也不把桥的可变时长重参数化后当成成本不变。

本稿支付的是一个固定自然通量的两号、任意实值及实际光滑截面。
它不从 [R384](R384-exact-two-dimensional-natural-image-and-positive-cone-of-Q4.md) 的线性像二维结论推出实际二维控制，
不保证 whole pure/self、其它通量、同一二阶 gauge 或全部 period 同时保持。
若将零低阶模块插入一个固定非零第三 hook 基准，原 M/T 可保持，
但其第四完整成本和其它观察仍须按同一传递式联合处理。

真正使用的领先项来自完整 Q4 的 (7)，而非已经撤回的 H 非零值。
R350 与 R382 的全状态零、原 M0 后的 R109、带 $Y_b$ 修正的真倒行、
以及全部固定桥成本都是 (29) 的必要组成部分。
