# R457：全 U 的自然七余商、完整正规化及权零正字符核见证

日期：2026-11-16。**完整原式纸面证明；没有执行新的原根恢复、符号程序、profile、求积、成员、秩、人工测试或科学运行。**

[R453](R453-local-geometric-action-of-the-seven-ordered-current-remainders.md) 给出原实际路径七余量的完整局部 action；[R454](R454-complete-response-self-principal-trace-and-seven-ordered-current-invariants.md) 则证明整个原响应空间的七余量等于 whole-self 主系数的一个固定迹。本文合并这两条原式，先在全部真实成本空间 $U$ 上定义一个不要求 pure 或 self 为零的自然映射，再完整处理原八矩归一化 $\Gamma$。

准确结论是：

- 新自然映射 $\mathfrak d:U\to\operatorname{Pol}_{\le6}$ 杀整个 $\mathcal R$，其像恰为全部六次多项式；其真实仿射律为(15)。
- 完整正常族的读出由(26)给出。三个正规加速度平方、两个正规 H 族和五个正规四次速度族均被 $\mathfrak d$ 杀掉。这说的是本稿新映射，不能与旧总通量 $\Lambda$ 混淆。
- 原 $C_2,C_4,C_6$ 的值分别为 $-3x^5/128,3x^5/128,3x^5/128$。所以 $H_*+J_4$ 与 $H_*+J_6$ 是当前共同母库上保持 $J^+$、整个 $D$ 为零、但 $\lambda_+=1$ 的真实**有号成本成员**。
- R404 留下的唯一类系数由此确定为 $c_0=-1$。

没有由这些有号成员宣布实际联合截面、全根 period 或同一十三行规范已经支付。原型的完整非零基准仍保留。

直接来源为 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R109](R109-local-density-of-the-complete-fourth-quotient.md)、[R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)、[R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)、[R295](R295-final-grid-forces-zero-platform-matrix-and-exact-self-history-principal.md)、[R344](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md)、[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)、[R405](R405-common-exterior-packets-and-local-ordered-currents-at-all-internal-degeneracies.md)、[R439](R439-diagonal-current-quotient-and-exact-simultaneous-cap-criterion.md)及 R453—R454。所有 primitives 使用原共同右 collar 和同一个几何起点。

## 1. 不先假设 pure 零的真实有序输出

沿 R105/R130，$U$ 是同 scalar 常值 germ、frame $I\to I$、$M=T=0$ 的全部实际完整成本的真实线性 span，$\mathcal R\subset U$ 是原完整响应空间。记
$$
\Sigma_V(u)=V(u^2,0),\qquad
P_V(u)=V(0,u)=16\pi V(u).
\tag{1}
$$
对两个不交实紧输入 $u<v$，先取普通多项式系数
$$
\mathcal U^\circ_{V,\mu(v)}(u)
=[a^2b^2](\Sigma_V-P_V)(au+bv),
$$
$$
\mu(v)=\left(\int(v'')^2,\ \int x(v'')^2,\
\int\{x^2(v'')^2+2(v')^2\}\right).
\tag{2}
$$
这里只固定支撑次序，不把每个包的二阶左尾置零。

对实际 canonical 路径，原完整第四式给
$$
\Sigma_V(u)=-\mathscr P H(Z_u,Z_u),\qquad
P_V(u)=\Sigma_V(u)-4\mathscr P H(Y_u,C(u;u^2)).
$$
二阶交叉 $Z(u,v)$ 为零，且 $C(v;u^2)=0$：在右包 source 上左包二阶场准确右零。故
$$
\boxed{\mathcal U^\circ_{V,\mu(v)}(u)
=4\mathscr P H(Y_u,C(u;v^2))
=4Q_{V,\mu(v)}(u).}
\tag{3}
$$
因子四来自整个 $\Sigma-P$，不是把 pure-zero 情形的有序 self 身份无条件外推。

R292 的实际右包二阶左尾只依赖 $\mu(v)$，R405 第4—6节的 raw 分子恢复因此给
$$
\frac{\mathcal U^\circ_{V,n}(u)}4
=L_{V,n}(x,u,p,r)+\sum_{j=0}^2m_{V,j}(x,n)J_j(u),
\quad p=u',\ r=u'',
$$
$$
J_j(u)(x)=\int_x^{r_*}
\{y^j(u''(y))^2+2\mathbf1_{j=2}(u'(y))^2\}\,dy .
\tag{4}
$$
$L$ 对 $(u,p,r)$ 齐次二次，系数对 $n$ 线性；$m_j$ 对 $x$ 至多二次、对 $n$ 线性。这里还没有使用 whole self 或 ordered 自然通量为零。

本步在实际 $M=T=0$ 常值端芽生成路径上合法：二、三阶 endpoint 数据回到原值；而 R56 的 s 分部边项
$-[\lambda P+\gamma B/h^2]$ 中
$\lambda=(\gamma z-h\nu)/h^2$，在两个常值端芽分别为零。R439(36)的剩余边项 $[\gamma e\alpha/(2h^2)]$ 也分别为零。没有为此要求非零 hook、除以 hook、或支付第四 period。

用右侧三个同形同宽不同中心的真实矩基，(2)—(4)线性延拓到任意 $n\in\mathbb R^3$。它只依赖完整 $V$，不依赖其实际路径线性表示。

此外，(4)的分裂唯一。若其差恒零，先把 $u$ 支撑选在评价点右侧，局部 jets 全零，而三矩像张成 $\mathbb R^3$，故三个 $m_j$ 的差均零；随后自由指定局部二阶 jets，得到 $L$ 的差零。因此不能通过把真 primitive 的常数挪入 $L$ 来改变以下读出。

定义
$$
\boxed{
d_{\rm raw}(V)(x)
=[ur]_{\rm loc}L_{V,n}(x,u,p,r)
\big|_{n=(1,x,x^2)} .
}
\tag{5}
$$
先提局部系数，再作三矩的代数代入；不把 $(1,x,x^2)$ 称为实际点质量包。

## 2. whole self 的唯一三导平方系数

直接采用原 self 左二次系数
$$
\widehat{\mathcal Q}_V(u)=[x^2]_{\rm left}\Sigma_V(u)
=4\mathcal Q(V)(u).
$$
R295 的完整原分子及其真左尾给所有实际生成路径、继而给全部 $U$ 的分裂
$$
\widehat{\mathcal Q}_V(u)
=\int \widehat F_V(x,u,p,r)(u''')^2dx+\mathcal B_V(u),
\qquad
\mathcal B_V\text{ 在固定共同支撑的 }C^2\text{ 拓扑连续}.
\tag{6}
$$
$\widehat F_V$ 对 $(u,p,r)$ 齐次二次。余项保留原左矩、端势及所有一次三导项；不假单包 $Z_u$ 左紧。

这个系数是整个泛函的内在量。若两个分裂相差一项 $F$，令
$u_N=u_0+N^{-5/2}\chi\cos Nx$，将差式除以 $N$ 后取纸面极限，得到
$\frac12\int F(x,u_0,u_0',u_0'')\chi^2=0$。任意小窗与自由二阶 jets 迫 $F=0$。所以 $\widehat F_V$ 不依赖原模板呈示；本稿未执行该高频序列。

令
$$
\mathfrak T=\partial_p^2-2\partial_u\partial_r .
$$
对二次式作用后不再含 profile jets。定义新的自然七余读出
$$
\boxed{
\mathfrak d(V)=d_{\rm raw}(V)-\frac18\mathfrak T\widehat F_V .
}
\tag{7}
$$
这不是旧自然总通量 $\Lambda_u(V)$，也不是单独的原 $\mathcal Q$。

若 $E(V)=(\pi V,\mathcal QV)=0$，则(6)的唯一性给
$\widehat F_V=0$，并且(2)就是原 self 的有序 $2+2$。再有
$O_{\rm all}(V)=0$ 时，R433 的 Euler current 合法，R439 的整个六次对角量正满足
$$
\boxed{\mathfrak d(V)=D_V.}
\tag{8}
$$
一般 $V$ 不满足这些零门时仍由(7)定义，不能提前把它称为实际退化点 current。

## 3. 全部原响应都被新自然映射湮没

R454 对整个原 $\mathcal R$ 证明
$$
\mathfrak T\widehat F_R=8\widetilde D_R.
\tag{9}
$$
其中 $\widetilde D_R$ 起初使用 $\Sigma_R$ 的有序 self。还需核对(5)的 $\Sigma-P$ 规范。

对每个原 $\mathcal B_E C(B,C)$，R344 的完整 $2+2$ pure 身份给
$$
[a^2b^2]P_R(au+bv)=2q_{\mathcal J(n)}(u),\qquad
\mathcal J(n)\in E_8 .
$$
原八个 $q_A=\Phi_A(u,u)$ 的局部部分都没有 $ur$ 项；其 primitives 与左尾原样保留。故 pure 的这一系数不改变(5)。八个 $\chi$ 的原 pure 本来为零。R247/R254 的完整来源覆盖遂给
$$
d_{\rm raw}(R)=\widetilde D_R
\quad(R\in\mathcal R),
$$
即
$$
\boxed{\mathfrak d(\mathcal R)=0.}
\tag{10}
$$
这里既不把 $144$ 列当整个 $\mathcal R$，也不要求单列响应先满足 $E=0$。若净响应保持 $E$，(8)(10)才回到原七项 current 不变性。

## 4. 原路径 action 及全部端项的适用域

对实际 $M=T=0$ 同常值端芽生成路径，记
$$
\gamma=h_s,\quad v_k=k_s,\quad A=\gamma/h,\quad
d=h\omega-k,\quad e=hx+d,\quad Q=1+e^2,
$$
$$
Z_x=A(e^2+2ke-1)-e v_k,\qquad
\omega_s=\frac{v_k}{2h}.
\tag{11}
$$
在 R453 中，$\mathscr F_B=\widehat F_V/4$，且原完整恒等是
$d_{\rm raw}=\frac12\mathfrak T\mathscr F_B+
4\int kp_{\rm tail}\mathscr R_{\rm loc}$，其中
$p_{\rm tail}=Q/(8h)$。所以(7)恰消其 trace，而不需要
$\mathcal QV=0$。

用于此处的两个边界均有明确来源：R442 的分部边项含累计首系数 $a_n$，由原 $m(s_0)=m(s_1)=0$ 逐端为零；R453 一阶化的边项为
$-2[kp_{\rm tail}^2(p_{\rm tail})_s/h^2]$，由常值端芽逐端为零。原(4)的 s 分部边界已在第1节单独核对。没有把 $p_n,t_n,q_n,\eta_n$ 的单端值设成零。

因此全部生成路径满足
$$
\boxed{
\mathfrak d(V_B)(x)=\int_B\rho(S,\dot S;x)\,ds ,
}
\tag{12}
$$
$$
\boxed{
\rho=\frac1{512h^5}
\left\{
-2k(1+k^2)Q^3+5kQZ_x^2+2v_kQ^2Z_x
-2kAQ^2Z_x+kA^2Q^3
\right\}.
}
\tag{13}
$$
这是完整值，仅含几何导数权 $0$ 和 $2$。式(12)先在上述原 $U$ 生成路径上成立，再按真实线性 span 使用；不把任一未闭静态段的密度当作实际成本。

$Q,Z_x$ 均对 $x$ 至多二次，故
$$
\mathfrak d(U)\subseteq\operatorname{Pol}_{\le6}.
\tag{14}
$$
对 R453 当前非零 hook 的实际背景，若满足其完整原周期/whole-$E/O$ 条件，(8)仍把(12)识别为该背景的实际 $D$。本稿不改变其 hook、端口、母库或原初值。

## 5. 真仿射协变与七个系数的真实权

用 R89 的完整 profile 共轭
$$
P_{H,c}V=C_{H,c}^{-1}V(C_{H,c}\cdot),\qquad
(C_{H,c}u)(x)=u((x-c)/H),\quad H>0 .
$$
所有输入、右锚、原历史与整个输出一起输运。

三矩的真实变换是
$$
\mu(C_{H,c}v)
=H^{-3}(n_0,\ c n_0+Hn_1,\
c^2n_0+2cHn_1+H^2n_2).
$$
在新 $n=(1,\xi,\xi^2)$ 处，这等于
$H^{-3}(1,H\xi+c,(H\xi+c)^2)$。
局部 $ur$ 另有 $H^{-2}$，所以
$d_{\rm raw}(P_{H,c}V)(\xi)=H^{-5}d_{\rm raw}(V)(H\xi+c)$。

whole self 左二次系数额外乘 $H^2$；再保积分 Jacobian 和三导平方，得到
$$
\widehat F_{P_{H,c}V}(\xi,u,p,r)
=H^{-3}\widehat F_V(H\xi+c,u,p/H,r/H^2).
$$
其 $\mathfrak T$ 收缩也准确乘 $H^{-5}$。综上，
$$
\boxed{
\mathfrak d(P_{H,c}V)(x)=H^{-5}\mathfrak d(V)(Hx+c).
}
\tag{15}
$$
因此其核对真实正仿射作用稳定，原平移导子满足
$$
\mathfrak d(NV)=\partial_x\mathfrak d(V).
\tag{16}
$$
若 $V\in U_\sigma$ 是原真实权 $\sigma$，则
$\mathfrak d(V)$ 只能是 $x^{\sigma+5}$ 的常数倍，指数不在
$\{0,\ldots,6\}$ 时为零。尤其真权零的像只能沿 $x^5$；不是根据 profile 表面导数次数猜测其真权。

所有仿射使用可先限于共同合法窗口内的有限小参数；多项式恒等随后给原函数身份。本文不据(15)安装任意预给几何域。

## 6. 完整 Γ 修正：不能以 raw 静态密度代替正规 F0

R109 的完整局部密度为
$$
\mathscr L=v-\mathcal B_mN=\mathscr L_0+\mathscr L_2+\mathscr L_4,
\qquad m=m_0+m_2.
\tag{17}
$$
这里 $N=N_0+N_2$ 含全部原静态势和加速度势。R130 在八个参考态
$$
S_i^*=(h,k,\omega)=(1,k,d+k),\qquad
k\in\{0,1\},\quad d\in\{0,1,-1,2\}
\tag{18}
$$
定义
$$
\Gamma(M)=\sum_i a_i(M)\mathscr L_0(S_i^*),
\qquad
F_0=\mathscr L_0-\Gamma(m_0).
\tag{19}
$$
$a_i$ 是 $m_0(S_i^*)$ 的真实基坐标。记
$$
\Gamma_\rho(M)(x)=\sum_i a_i(M)\rho_0(S_i^*;x),
\quad
\rho_0=-\frac{k(1+k^2)}{256h^5}
[1+(hx+d)^2]^3.
\tag{20}
$$

下面证明
$$
\boxed{\mathfrak d(F_0(S))
=\rho_0(S)-\Gamma_\rho(m_0(S)).}
\tag{21}
$$
这一步不假定每个 raw $\mathscr L_0(S)$ 已属于 $U$。

在 R130 的有限真实环境 $\mathscr E\supset U$ 中，任取
$\mathfrak d$ 的线性延拓
$\widetilde{\mathfrak d}:\mathscr E\to\operatorname{Pol}_{\le6}$。
定义多项式值的真局部密度
$$
I=\widetilde{\mathfrak d}(\mathscr L)-\rho.
\tag{22}
$$
对实际同 scalar germ、frame $I$、$M=T=0$ 路径，
R109(19)、(10)与(12)给 $\int I=0$。

这个零积分条件可以准确去掉 $T=0$。对任意同 scalar germ、
frame $I$、$M=0$ 的实际平端路径 $B$，真倒行 $B^R$ 有
$M=0,T_{B^R}=-T_B$；所以 $BB^R$ 是前一类路径。
$\mathscr L$ 的导数权是 $0,2,4$，$\rho$ 是 $0,2$，均在真倒行下逐点保持；局部积分可加。因此
$$
0=\int_{BB^R}I=2\int_BI.
\tag{23}
$$
没有在非零矩阵路径上把完整 $V$ 当作可加量。

现在逐 $x$ 系数应用 R130 第4—7节的原端点纤维证明：

1. 同 scalar germ 的两个路径若末 frame 与 $M$ 相同，接同一个 R70 实际补偿，(23)使其 $I$ 积分相同。
2. 得到 $SO(3)\times E_8$ 到实加法群的连续同态；$SO(3)$ 紧，故只余一个真实八矩乘子。
3. 用真倒行及 R70 零矩开桥，得到同一个乘子适用于全部开平端路径，不预设 scalar 首末相同。
4. 偶导数权保证上述反向局部积分同号；没有用负时间或免费负成本。

于是存在固定多项式值线性映射 $\mu:E_8\to\operatorname{Pol}_{\le6}$，使
$$
\int_B\{\widetilde{\mathfrak d}(\mathscr L)-\rho-\mu(m)\}\,ds=0
\quad\text{对所有真实开平端路径}.
\tag{24}
$$
这段原证明只使用局部性、旋转不变性、连续性、(23)与真倒行偶权，不要求残差 $I$ 本身先写成某个固定 $\ell(\mathscr L)$。

在任意常态取任意正时长，(24)给
$\widetilde{\mathfrak d}(\mathscr L_0(S))
=\rho_0(S)+\mu(m_0(S))$。
代八个参考态得到
$\widetilde{\mathfrak d}\Gamma=\Gamma_\rho+\mu$，再由(19)准确消去
$\mu$，即(21)。结果独立于任意延拓。特别，原 $N_0$ 与
$\Gamma$ 没有被删去，而是通过完整(17)—(24)进入此身份。

## 7. 同一论证给完整正规四层的零式

将(19)—(20)放回(24)，按真实时长缩放
$s=\delta\sigma$，得到导数权 $0,2,4$ 的三项独立分离。
此时允许 frame、$M$ 和末 scalar 随时长改变，因为(24)已对全部开平端路径成立。

完整 $\Gamma(m_2)$ 必须保留。R129/R130 的正规式给
$$
\mathscr L_2-\Gamma(m_2)=D_sP_1+\widehat Q_2,
$$
$$
\mathscr L_4=D_sP_3+\bar A_{hh}h_{ss}^2+
\bar A_{hk}h_{ss}k_{ss}+\bar A_{kk}k_{ss}^2
+(H_1h_s+H_2k_s)(h_sk_{ss}-k_sh_{ss})
+\widehat Q_4 .
\tag{25}
$$
$P_1,P_3$ 是原正导数权势，在两端常值 germs 分别为零。

$\rho=\rho_0+\rho_2$、$m=m_0+m_2$ 没有第四导数权。
所以(24)的第四层积分恒零。按 R130 第8节原次序作微幅路径：
先分离加速度平方的二次幅项；它在每个状态零后，才分离
H 的三次幅项；最后分离四次速度。原两个 H 微路径使用
$(U,W)=(\psi,\psi')$ 及交换，系数是
$\mp3\int\psi(\psi')^2$，不能把 H 当成全导数。

同样，第二层已是无加速度的真实速度二次式，用
$(h_s,k_s)=\varepsilon(\alpha\psi,\beta\psi)$ 分离即可。
所有正规族的值属于 $U$，由 R130 保证，故结果不再依赖
$\widetilde{\mathfrak d}$：
$$
\boxed{
\begin{aligned}
\mathfrak d(F_0)&=\rho_0-\Gamma_\rho(m_0),\\
\mathfrak d(\widehat Q_2)&=\rho_2-\Gamma_\rho(m_2),\\
\mathfrak d(\bar A_{hh})&=\mathfrak d(\bar A_{hk})
=\mathfrak d(\bar A_{kk})=0,\\
\mathfrak d(H_1)&=\mathfrak d(H_2)=0,\qquad
\mathfrak d(\widehat Q_4)=0 .
\end{aligned}}
\tag{26}
$$
最后一式表示全部五个速度系数、每个真实状态均为零。这不说这些原成本或旧自然函数 $\Lambda$ 为零；例如 R386 的非零 $\Lambda(\widehat Q_4)$ 与(26)没有冲突。

## 8. 八参考态准确给最高两项

设 $D_j(V)=[x^j]\mathfrak d(V)$。静态原密度的最高两项是
$$
[x^6]\rho_0=-\frac{hk(1+k^2)}{256},\qquad
[x^5]\rho_0=-\frac{3k(1+k^2)d}{128}.
\tag{27}
$$
用 $\mathsf p_1,\mathsf p_2$ 表示 R73 的八矩坐标，避免与 profile 导数 $p$ 混淆。在八参考态(18)上逐项有
$$
[x^6]\rho_0(S_i^*)=\mathsf p_2(m_0(S_i^*))/64,
$$
$$
[x^5]\rho_0(S_i^*)=3\mathsf p_1(m_0(S_i^*))/64.
\tag{28}
$$
因为 $k=0$ 时两边均零，$k=1$ 时
$\mathsf p_2=-1/2,\ \mathsf p_1=-d$。
八矩基的唯一性将(28)提升为对任意 $M$ 的准确线性式。

对一般静态状态，原
$\mathsf p_2(m_0)=-kh/2,\ \mathsf p_1(m_0)=k^2-hk\omega=-kd$。
故(21)给
$$
\boxed{D_6(F_0(S))=\frac{hk(1-k^2)}{256},}
\tag{29}
$$
$$
\boxed{
D_5(F_0(S))
=\frac3{128}\left(k^4-k^2+hk\omega-hk^3\omega\right).
}
\tag{30}
$$
例如 raw 的 $-3k(1+k^2)d/128$ 并非(30)；遗漏
$\Gamma_\rho(m_0)$ 会同时改变 $C_2,C_6$ 的所需系数。

(29)在如 $h=1,k=2$ 的合法状态非零。R130 保证该完整
$F_0(S)$ 属于 $U$，所以 $\mathfrak d(U)$ 含一个真正六次多项式。
由(15)的小真实平移，其七个 Taylor 系数张成
$\operatorname{Pol}_{\le6}$：六次多项式及连续求导到常数的首项构成严格三角系数表；可用七个不同且足够小的平移作有限 Vandermonde 插值。因此
$$
\boxed{\mathfrak d(U)=\operatorname{Pol}_{\le6}.}
\tag{31}
$$
这是七维真实函数商像，不是七个 actual 正向控制。此处不执行任何新矩阵求秩或 profile 采样。

## 9. 原权零类与 R404 的系数

R196 原记录的状态幂顺序始终是 $(h,k,\omega,\log h)$：
$$
C_2=[h^0k^2\omega^0]F_0,\qquad
C_4=[h^0k^4\omega^0]F_0,\qquad
C_6=[h^1k^1\omega^1]F_0.
$$
它们都是真实权零。由(15)，其整个 $\mathfrak d$ 只能沿
$x^5$，所以(30)已经给出完整值：
$$
\boxed{
\mathfrak d(C_2)=-\frac3{128}x^5,\qquad
\mathfrak d(C_4)=\mathfrak d(C_6)=\frac3{128}x^5 .
}
\tag{32}
$$
不需要重新读取原 pure 成员坐标或对旧三维商再求秩。

[R404](R404-natural-weight-zero-image-at-most-two-and-single-function-kernel-criterion.md)
已在原完整商中证明存在唯一 $c_0$，使
$$
C_{20}=C_4+c_0C_6+R_*,\qquad R_*\in\mathcal R_0,
$$
其中 $C_{20}$ 是原 $\bar A_{hh}$ 的状态键 $(-2,0,0,0)$。
由(26)，$\mathfrak d(C_{20})=0$；由(10)(32)，
$$
0=(1+c_0)\frac3{128}x^5.
$$
因此原未知类系数准确为
$$
\boxed{c_0=-1,\qquad C_{20}=C_4-C_6+R_* .}
\tag{33}
$$
R404 使用的旧自然加速度平方零式只能看见 $n_4=-c_0n_6$；
这里用的是新 $\mathfrak d$，所以即使旧 $n_4=n_6=0$ 仍能辨认该原类系数。没有给出 $R_*$ 的新响应展开，也不需要重付它的旧存在性。

## 10. 当前共同库上的 λ 正见证与准确边界

R333/R400 的同权零原代表满足
$$
H_*-C_2\in\mathcal R_0,\qquad
J_4-C_4\in\mathcal R_0,\qquad
J_6-C_6\in\mathcal R_0,
$$
$$
E(H_*)=E(J_4)=E(J_6)=0,\qquad
\lambda_+(H_*)=1,\quad\lambda_+(J_4)=\lambda_+(J_6)=0.
\tag{34}
$$
其准确来源见
[R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md)、
[R400](R400-weight-zero-natural-flux-kernel-and-three-static-function-criterion.md)；
本稿不重新计算六条旧响应或它们的 pure/self 收据。

由(10)(32)，
$$
\mathfrak d(H_*)=-3x^5/128,\qquad
\mathfrak d(J_4)=\mathfrak d(J_6)=3x^5/128.
$$
所以两个明确的原有号成员
$$
\boxed{\widehat H_4=H_*+J_4,\qquad
\widehat H_6=H_*+J_6}
\tag{35}
$$
均满足
$$
E(\widehat H_i)=0,\qquad
\mathfrak d(\widehat H_i)=0,\qquad
\lambda_+(\widehat H_i)=1.
\tag{36}
$$

现在固定当前从起点共同选择的实际母库及其完整正仿射查询闭包。
R411/R412/R431 的四式约束、后续同纤维改动所保留的准确条件是：
[R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md) 的局部五次函数 $n_2=\Lambda(H_*)$ 在每个实际母的全部允许正仿射输运上为零。所有所需不同母的 ordered $3+2$ 查询也为零，因为该完整五次函数局部、不交支撑不产生混合项。

R406 还给 $\Lambda(J_4)=\Lambda(J_6)=0$ 对全部紧输入成立。
故对同一个
$$
J^+=(E,A,O_{\rm all})
$$
——其中 $A$ 只取当前冻结的有限母/有序查询的共同仿射闭包——
(35)准确满足
$$
\boxed{\widehat H_i\in U_0\cap\ker J^+\cap\ker\mathfrak d,
\qquad \lambda_+(\widehat H_i)=1.}
\tag{37}
$$
这不是 universal $\Lambda_{\rm all}$ 核见证：
$\Lambda(\widehat H_i)=n_2$ 仍是非零的 universal 函数，只在上述实际查询空间被原母条件杀掉。它因而不违反 R406 的全自然函数障碍。

在(37)上，whole $E$ 与 $O_{\rm all}$ 已使 R433 的完整 current 有定义；由(8)，其整个对角 $D$ 为零。R454 的 $\ker D$ 像定理因此适用于后续**同一个**原响应补偿。但本稿尚未选择该补偿，也未将其新 self 值置零。

特别继续保留：

- 整个 formal current 的共同响应提升与它引入的同包 self；
- R455 当前唯一镜对、所有角色/宽度/位置的真实联合评价，以及原 suffix；
- 原型复制的完整基准、全 $J^+$ 与新 partial 的同一有限实际构造；
- 原 $L_f$ 全部 range、端 germ、两个特解及同一个十三行规范；
- 原最高 $d/e$ 基准与实际非线性任务。

(31)与(37)分别是自然商像定理和有号核见证。它们不把一个原正常系数当成可独立实现的正时间路径，也不把 $\lambda_+$ 在新增有号核上非零当成已经证明实际联合正锥满。下一步应先在该同权零代表上支付整个 $C$ 和同包 self，再单独处理实际成本与所有基准。
