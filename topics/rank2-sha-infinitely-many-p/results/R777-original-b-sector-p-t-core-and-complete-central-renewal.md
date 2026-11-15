# R777 — 原 B 分量的 P/t 整核、完整中央更新式及四单位余域

日期：2026-11-15。**状态：已证明。**

本文保持 R734 的同一个最终测试 $q_N^*$。先从 R767 的四核中分离一个真正的原来源，再把它的 $P$-deep/$t$-unit 行、相反行、两单位行和共同深行放进同一完整中央等式。新的整核只留下一个明确的绝对符号 $\epsilon_P^2=1$；不猜该符号，不把负二、负五矩赋非零。

实质返回是：$P,t$ 的共同深核与原 W 两态核，支付另一正交伴随 $V_t$ 的同源两态。因而全部真正 $W$ 近相消环带、以及全部 $W/V_t$ 深度矩形，都有原 $J_T$ 的完整返回。剩下的四单位行仍在同一个精确式中。新增帽门不是这些返回的不变门，最后逐项列出其移动。

## 1. 原来源、观察与两个真实投影

沿 R764、R767 的规范，置
$$
\omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad N\in4\mathbf Z_{>0}.
\tag{1}
$$
所有旧 ray、固定坏集、原逆矩阵和周期 $\Omega=\Omega_p$ 都保持。
特别 $p>163$，且 $p\nmid 2\cdot3\cdot7\cdot17\cdot29$。

用原六输入
$(\xi_1,\xi_2,\xi_3,x,c,d)$，记
$$
e_0=-\nu_\sigma^{\boxtimes6}/84,\qquad
h_W=\omega^2\mathcal T_*e_0,\qquad q=q_N^*.
$$
R764 的实际行是
$$
\begin{aligned}
r&=(\xi_1-\omega^2\xi_3+\omega x)/\delta,&
s&=r+c,&t&=r-c,\\
B&=-\xi_1+\omega\xi_3-\omega^2x,&
A_0&=2\delta\xi_2-4\delta B/3,&Y&=A_0+s+2d .
\end{aligned}
$$
置
$$
a=1+3\omega,\qquad
P=A_0+(2+3\omega)s+4d,\qquad
W=P-at,\qquad W_j=P-a\omega^{2j}t.
\tag{2}
$$
这里 $N(P)=58,\ N(t)=2,\ P\perp t$；
Y 与 P 不正交。原 t 同时垂直于 Y、P。

分离同一个原两态的 $\mathcal T_*$ 特征分量：
$$
e_A=\frac{\omega h_W-\omega^2e_0}{1-\omega^2},
\qquad
e_B=\frac{e_0-\omega h_W}{1-\omega^2}.
\tag{3}
$$
则 $e_0=e_A+e_B$，且
$\mathcal T_*e_A=e_A,\ \mathcal T_*e_B=\omega^2e_B$。
q、Y、P 都被 $\mathcal T$ 固定。因此
$$
Y_*(q e_B)=0,\qquad
W_*(q e_B)=\beta^N\frac{6\delta}{1-\omega^2}\nu_T.
\tag{4}
$$
这是原整来源的投影，不是给一个新辅助来源添加中央零。

下文的测试均与纯 C 六角平均相容；记
$\bar e_B=\mathscr P_Ce_B$，其中
$C=(\xi_1-\xi_3+x)/\delta$。
R767 已逐项支付 q 的六支不变性，P、t、Y 以及本文实际帽门不含 C。
写
$$
\rho_0=q\bar e_B,\qquad
Z_B(w)=\int f_w(W)\,d\rho_0
=\beta^N\frac{6\delta}{1-\omega^2}J_T(w),\quad
f_w(z)=1_{z\ {\rm unit}}\langle z\rangle^{d_pw},\quad d_p=p-1.
\tag{5}
$$
$Z_B(0)=0$。已知原 $J_T'(0)=0$ 只使 (5) 的完整导数为零。

## 2. 全五伙伴不丢的两核与实际 P/t 边际

保 R767 的整数输出
$$
S=\delta s,\quad T_0=\delta t,\quad C_0=\delta C,\quad B,\xi_2,d.
$$
为避免混淆，$T_0$ 是物理轴，$\nu_T$ 仍是原 degree72 曲线来源。
写
$$
P_3=\sigma^3,\quad B_3=-y_b\sigma^3,\quad
f_1=-x_by_b\sigma^6,\quad f_3=-y_b\sigma^6,\quad
f_4=x_b\sigma^6,\quad H=(x_b^3-2b)\sigma^6.
$$
R767 的完整四核及 $h_W$ 的四个乘数给出
$$
\boxed{
\bar e_B=\frac{\delta}{84}\,
\nu_{B_3}(C_0)\boxtimes\nu_\sigma(\xi_2)\boxtimes\nu_\sigma(d)
\boxtimes\left(f_{1,T_0}\otimes U_1+f_{4,T_0}\otimes U_4\right),
}
\tag{6}
$$
其中
$$
U_1=2f_3(S)B_3(B)+H(S)P_3(B),\qquad
U_4=6b f_3(S)P_3(B)-H(S)B_3(B).
\tag{7}
$$
原 H、$f_3$ 两个 t 来源在 (3) 中整条消去；
(6) 保完整五个伙伴，并允许任意原相容混合切集。
它不是对边际质量的运算。

只有在真正忘掉其余伙伴时，才能作以下简化。
由 R764，
$$
t=\frac{W-W'}{1-4\omega},\qquad P=(W+W'+W_2)/3,
$$
且 $W_2$ 是原 $W,W'$ 的固定线性组合。因此 $(P,t)$ 通过
原 $\pi_4=(Y,W,W',G)$ 因子化。
q 的整个 $\pi_4$ 返回和 $\mathcal T$ 的准确转置给
$$
\boxed{(P,t)_*\rho_0=\beta^N(P,t)_*\bar e_B.}
\tag{8}
$$
故任何只看 P、t 的新分区仍使用同一个原 q，但其完整 q 作用只是
$\beta^N$。含 Y、帽、CD、U 或 E 的门一般不通过此边际。

令 $P_0=\delta P$，$c_7=2+3\omega$。
实际生成变量代入是
$$
(S,B,\xi_2,d)=(c_7 z,4z,-6z,4\delta z).
$$
于是 (6) 的整个二维来源准确为
$$
\boxed{
(P_0,T_0)_*\bar e_B
=\frac{\delta}{84}
\left(\nu_{\mathcal A_1}\boxtimes\nu_{f_1}
+\nu_{\mathcal A_4}\boxtimes\nu_{f_4}\right),
}
\tag{9}
$$
$$
\begin{aligned}
\mathcal A_1(z)
&=\sigma(-6z)\sigma(4\delta z)
 \{2f_3(c_7z)B_3(4z)+H(c_7z)P_3(4z)\},\\
\mathcal A_4(z)
&=\sigma(-6z)\sigma(4\delta z)
 \{6b f_3(c_7z)P_3(4z)-H(c_7z)B_3(4z)\}.
\end{aligned}
\tag{10}
$$
它们属于完整标准 $\mathcal S_{174}$，角型分别为5、2；
(9) 的另一轴是原标准 $\mathcal S_6$。
显示首项是
$$
\boxed{
\mathcal A_1=-48\delta(13-18\omega)z^5+O(z^{11}),
\qquad
\mathcal A_4=24\delta z^2+O(z^8).
}
\tag{11}
$$
确实 $c_7^3=-19-18\omega$，故
$2c_7^3+4^3=26-36\omega$。
(11) 只用于读真实正矩，不被代作负矩非零。

## 3. 完整 S174 标量、平方锚与 P/t 所有矩形

R772 已付原整行
$$
P_0=(-2+3\omega,-6,-1+6\omega,1+3\omega,-4+\omega,4\delta)\xi,
\quad N(P_0)=174.
\tag{12}
$$
它有四个非零模二系数，故是标准 even 半特征。
原 $\mathcal T$ 固定 P，并保持这个完整格，因而相同结论用于
$e_0,h_W,e_B$ 以及全部未忘伙伴。

当前 ray 的比值满足
$$
g_\pi\equiv-1\pmod4,\qquad
g_\pi\equiv1\pmod3,\qquad g_\pi\equiv1\pmod{29};
$$
所以完整中心为
$$
g_\pi\equiv175=1+174\pmod{348}.
\tag{13}
$$
同 R764 的标准 even Heisenberg 规范，(13) 在整个
$\mathcal S_{174}$ 上与所有 Heisenberg 标签交换。因此完整
normalized 算子为一个标量 $\epsilon_P I$，而非仅在一个边际上 scalar。

其绝对平方可以不用任何新的角色猜测来定。取
$$
a_0=7\delta,\qquad b_0=3\delta,\qquad
\mathcal F(z,v)=
\sigma(a_0z-\bar b_0v)\sigma(b_0z+\bar a_0v).
\tag{14}
$$
两列的范数均为 $147+27=174$，交叉为零，行列式174是 p-unit。
两列各有两个非零模二系数，故两轴都是同一个标准 even
$\mathcal S_{174}$，所有半特征和 rigidification 一致。
原两个独立 sigma 同时 p-deep 给外部标量 $\beta^2=\lambda^2$；
两轴 whole 标量给 $\lambda^2\epsilon_P^2$。
$\mathcal F\ne0$，整像推前单射，故
$$
\boxed{\epsilon_P^2=1.}
\tag{15}
$$
本文先保这个准确符号。它不使用尚未识别的负一值定标。

令
$$
\alpha=\epsilon_P\lambda,\qquad
\Delta=\alpha\beta=-\epsilon_P\lambda^2.
\tag{16}
$$
对行 L 写
$P_{L,z}=I+(z-1)\bar L^tL/N(L)$。
R772 支付 q 对 P 的逐项不变性，R764 支付它对 t 的逐项不变性；
两轴正交。故完整测度身份是
$$
\boxed{
\rho_0|_{\{P\in p^\ell,\ t\in p^m\}}
=\alpha^\ell\beta^m
 (P_{P,\kappa^\ell}P_{t,\kappa^m})_*\rho_0,
\qquad\ell,m\ge0.
}
\tag{17}
$$
同式适用于未加 q 的整个 $e_B$。
P0、T0 与 P、t 只差固定 p-unit，未改变事件或物理投影。

特别，若 $\mathcal D$ 是任意原附加域，f 为完整有界测试，
$$
\int_{\{P\in p^\ell,t\in p^m\}}1_{\mathcal D}f\,d\rho_0
=\alpha^\ell\beta^m\int
1_{\mathcal D\circ M}(f\circ M)\,d\rho_0,
\quad M=P_{P,\kappa^\ell}P_{t,\kappa^m}.
\tag{18}
$$
不能将 $\mathcal D\circ M$ 改回 $\mathcal D$。

## 4. 原 W 核与一个实际两态更新式

置
$$
\boxed{
V_t=\bar aP+29t,\qquad
t=(V_t-\bar aW)/36,\qquad
P=(29W+aV_t)/36 .
}
\tag{19}
$$
这里 $N(a)=7$，所以
$$
\operatorname{Gram}(W,V_t)=\operatorname{diag}(72,2088),\qquad
P\perp t,\quad W\perp V_t .
$$
$(P,t)\mapsto(W,V_t)$ 的行列式为36，是 p-unit。
清掉原三处分母后，
$(P_0,T_0)\mapsto(W,\delta V_t)$ 的行列式为 $36/\delta$；
没有忘记原四个正交伙伴。两套共同缩放是同一个整映射
$$
P_{\rm pl}=P_{P,\kappa}P_{t,\kappa}
=P_{W,\kappa}P_{V_t,\kappa}.
\tag{20}
$$

R692 的原 W 三态给 $K_W^2=I$。定义
$$
\rho_1=K_W\rho_0=qK_W\bar e_B,\qquad
c_V=\Delta/\lambda=-\epsilon_P\lambda .
$$
q 与 W 核交换，因为 C、F、G 都在 $(P,t)^\perp$。
因此
$$
\rho_i|_{W\in p}=\lambda(P_{W,\kappa})_*\rho_{1-i}.
\tag{21}
$$
两条完整 W 边际都等于 (5) 的那个原 T 倍数。

**完整 V 返回的证明。**
由 (17)，
$\rho_0|_{\{W,V_t\in p\}}=\Delta(P_{\rm pl})_*\rho_0$。
在 $\{W\in p^2,V_t\in p\}$ 上分别先用共同深核和 W 核，
再由 (21) 的整像单射约消，得到
$\rho_1|_{\{W,V_t\in p\}}=\Delta(P_{\rm pl})_*\rho_1$。
现在对这两个共同深等式各自先用 (21)，约掉
$\lambda(P_{W,\kappa})_*$，准确得到
$$
\boxed{
\rho_i|_{V_t\in p}=c_V(P_{V_t,\kappa})_*\rho_{1-i}.
}
\tag{22}
$$
这只是在同一个完整实际两态上的结论，不声称 whole
$\mathcal S_{6264}$ 是 scalar，也不把 $\rho_1$ 的独立 P/t 核
认成 (17)。

由 (21)、(22) 的正交交换，所有真实矩形为
$$
\boxed{
\rho_i|_{\{W\in p^n,V_t\in p^m\}}
=\lambda^n c_V^m
 (P_{W,\kappa^n}P_{V_t,\kappa^m})_*
 \rho_{i+n+m\pmod2}.
}
\tag{23}
$$
所有另外四个伙伴保持。附加测试仍照 (18) 完整转置。

因两个返回态的 W 边际相同，(23) 给完整 Mellin 式
$$
\boxed{
\begin{aligned}
\int_{\{v_p(W)=n,\ V_t\in p^m\}}
 f_w(W/\kappa^n)\,d\rho_i
 &=\lambda^n c_V^m Z_B(w),\\
\int_{\{v_p(W)=n,\ v_p(V_t)=m\}}
 f_w(W/\kappa^n)\,d\rho_i
 &=\lambda^n c_V^m(1-c_V)Z_B(w).
\end{aligned}}
\tag{24}
$$
原 $1-c_V=1+\epsilon_P\lambda$ 是已付的单位。也可直接核：
若 $\lambda\equiv\pm1\bmod p$，则原偶整数迹
$\pi_0+\bar\pi_0\equiv\mp1\bmod p$。
由 $|\pi_0+\bar\pi_0|\le2\sqrt p<p-1$，它只能等于奇数 $\mp1$，
与原射线的偶迹矛盾。所以 $1\pm\lambda\in\mathcal O^\times$。
(24) 因而把原 $J_T'(0)=0$ 合法传入这些完整真矩形/环带。

采用 $W/p^n$ 时，应另乘
$\langle\kappa/p\rangle^{nd_pw}$；本篇未附门的质量为零，所以
相应尺度 log 项在完整来源后才消去。附额外门时没有此免费消去。

## 5. 四种 P/t 区域及真正近相消环带

在 W-unit 上，四种 P/t 状态给以下精确分割：
$$
\begin{array}{c|c}
\text{原区域}&\text{实际 W 条件}\\ \hline
P\ {\rm unit},\ t\in p&W\ {\rm unit}\text{ 自动}\\
P\in p,\ t\ {\rm unit}&W\ {\rm unit}\text{ 自动}\\
P,t\ {\rm unit}&W\ {\rm unit}\text{ 仍须保留}\\
P,t\in p&W\ {\rm unit}\text{ 为空}.
\end{array}
\tag{25}
$$
定义
$$
A_m(w)=\int_{\{P\ {\rm unit},t\in p^m\}}f_w(W)d\rho_0,\qquad
B_\ell(w)=\int_{\{P\in p^\ell,t\ {\rm unit}\}}f_w(W)d\rho_0
\quad(m,\ell\ge1),
$$
$$
C_0(w)=\int_{\{P,t,W\ {\rm unit}\}}f_w(W)d\rho_0.
$$
则同一个原完整中央恒等式为
$$
\boxed{Z_B(w)=A_1(w)+B_1(w)+C_0(w).}
\tag{26}
$$

共同深块不能从未归一 W-unit 的空域推成“来源为零”。
它的真实归一返回由 (17) 给出：
$$
\int_{\{P,t\in p^r\}}f_w(W/\kappa^r)d\rho_0
=\Delta^r Z_B(w).
\tag{27}
$$

更强地，对 $n\ge1$，当 W 在第 n 环带时，
P、t 要么同时为单位，要么同时深一层。
所以令
$$
C_n(w)=\int_{\{P,t\ {\rm unit},\,v_p(W)=n\}}
 f_w(W/\kappa^n)d\rho_0 ,
$$
由 W 全核与 (27) 的一层整像，得到
$$
\boxed{
C_n(w)
=\lambda^nZ_B(w)-\Delta\lambda^{n-1}Z_B(w)
=\lambda^n(1+\epsilon_P\lambda)Z_B(w).
}
\tag{28}
$$
这不是一个未收敛的无限环带求和，而是两个真正整域的有限相减。
也可由 (19) 看出：W-deep 时
$\{P,t\ {\rm unit}\}=\{V_t\ {\rm unit}\}$，
所以 (28) 正是 (24) 的 $m=0$ 行。

(28) 支付的是完整近相消环带的原 T 返回。
原 $J_T'(0)=0$ 使每条 $C_n'(0)=0$，但没有使 $C_0'(0)$ 为零。
后者仍是 (26) 中完整的双单位余项。

若 R778 的全角色定标将 $\epsilon_P$ 定为 $-1$，则这些式子准确
简化为 $\alpha=\beta,\ \Delta=\lambda^2,\ c_V=\lambda$，
以及 $C_n=\lambda^n(1-\lambda)Z_B$。
本文的证明不依赖这个后续定号。

## 6. P-deep/t-unit 的完整 Mellin 级数：原负二、负五在同一行

用 (9) 的实际来源定义
$$
M_F(r)=\int x^r\,d\nu_F=\Omega^rF^{(r)}(0),\qquad
J_F^{(-r)}(w)=\int_{x\ {\rm unit}}x^{-r}\langle x\rangle^{d_pw}d\nu_F .
\tag{29}
$$
这些符号不为负矩添加任何非零假设。
特别 $I_4=J_{f_4}^{(-2)}(0)$、$I_1=J_{f_1}^{(-5)}(0)$
是 R533/R540 的那两个原负矩。

在 P-deep/t-unit 上，
$W=(-a/\delta)T_0(1-P_0/(aT_0))$。
使用真正 P 核后，对所有 $w\in\mathbf Z_p$ 有
$$
\boxed{
B_\ell(w)=
\frac{\delta}{84}\beta^N\alpha^\ell
\langle-a/\delta\rangle^{d_pw}
\sum_{i\in\{1,4\}}\sum_{r\ge1}
 {d_pw\choose r}
 \left(-\frac{\kappa^\ell}{a}\right)^r
 M_{\mathcal A_i}(r)J_{f_i}^{(-r)}(w).
}
\tag{30}
$$
第一项 $r=0$ 严格消失，因为 $\mathcal A_i(0)=0$；
它的 t 型也会给同样消去。
$f_1$ 只保 $r\equiv5\bmod6$，$f_4$ 只保 $r\equiv2\bmod6$。
这些是完整单位域上的角型等式。
级数在 w 上一致收敛；微分后的 $1/r$ 分母完整保留。

因为每个 $r\ge1$ 的二项式系数在 $w=0$ 为零，所有
$\log\langle-a/\delta\rangle$、t-log 的零阶质量项准确消去。
因此
$$
\boxed{
B_\ell'(0)=
-\frac{\delta d_p}{84}\beta^N\alpha^\ell
\sum_{i,r\ge1}\frac{\kappa^{r\ell}}{r a^r}
 M_{\mathcal A_i}(r)I_{i,-r}.
}
\tag{31}
$$
这里 $I_{i,-r}=J_{f_i}^{(-r)}(0)$。
由 (11)，准确前两项是
$$
\boxed{
\begin{aligned}
B_\ell'(0)
={}&\frac{6d_p}{7a^2}\,
 \beta^N\alpha^\ell\kappa^{2\ell}\Omega^2 I_4\\
&-\frac{288(13-18\omega)d_p}{7a^5}\,
 \beta^N\alpha^\ell\kappa^{5\ell}\Omega^5 I_1
+p^{8\ell}\mathcal O.
\end{aligned}}
\tag{32}
$$
原两个负矩都没有被替换成正矩或其它曲线的值。
余项是同一原来源的 $r=8,11,\ldots$ 全部矩，不赋零。
$p>163$ 使显示前阶分母为单位；一般项使用
$r\ell-v_p(r)$ 的准确下界，得到 (32) 的整尾。

(30)–(32) 用到了真正完整边际 (8)。
如再附帽、CD、E 或 U 门，必须在 (6) 中保它，
不能把其条件正矩换成 (29) 的裸 $M_{\mathcal A_i}(r)$。

## 7. 相反条带、原 t 首行及全部条件来源

同样，在 P-unit/t-deep 上
$W=\delta^{-1}P_0(1-aT_0/P_0)$，得到
$$
\boxed{
A_m(w)=
\frac{\delta}{84}\beta^{N+m}
\langle\delta^{-1}\rangle^{d_pw}
\sum_{i\in\{1,4\}}\sum_{r\ge1}
 {d_pw\choose r}(-a\kappa^m)^r
 M_{f_i}(r)J_{\mathcal A_i}^{(-r)}(w).
}
\tag{33}
$$
这里 $f_1$ 只保 $r\equiv1\bmod6$，
$f_4$ 只保 $r\equiv4\bmod6$。所以
$$
\begin{aligned}
A_m'(0)={}&-\frac{\delta a d_p}{84}\,
 \beta^{N+m}\kappa^m\Omega\,J_{\mathcal A_1}^{(-1)}(0)\\
&-\frac{\delta a^4d_p}{14}\,
 \beta^{N+m}\kappa^{4m}\Omega^4J_{\mathcal A_4}^{(-4)}(0)
+p^{7m}\mathcal O .
\end{aligned}
\tag{34}
$$
它不是原裸 $D_\omega$ 的负一行，而是明确的 degree174 来源。
R772/R778 的点公式必须按自己的完整有限来源范围使用；
本文不对 (33) 的无限和施点因子投影。

为了精确保住 R773 的实际帽，记五伙伴测度
$$
\mathcal V_i=\nu_{B_3}(C_0)\boxtimes\nu_\sigma(\xi_2)
 \boxtimes\nu_\sigma(d)\boxtimes\nu_{U_i}(S,B).
$$
若 $\mathcal D$ 是不含 t 的原完整域，定义
$$
L_{i,\mathcal D}^{(-r)}(w)
=\int_{\{P_0\ {\rm unit}\}}
 P_0^{-r}\langle P_0\rangle^{d_pw}
 1_{\mathcal D}q\,d\mathcal V_i .
\tag{35}
$$
则带同一门的整条式为
$$
\boxed{
A_m[\mathcal D](w)=
\frac{\delta}{84}\beta^m\langle\delta^{-1}\rangle^{d_pw}
\sum_{i,r\ge1}{d_pw\choose r}
 (-a\kappa^m)^r M_{f_i}(r)L_{i,\mathcal D}^{(-r)}(w).
}
\tag{36}
$$
这里 q 完整留在 (35)，没有另外抽一个 $\beta^N$。
$\mathcal D=1$ 时，(8) 才给
$L_{i,1}^{(-r)}=\beta^N J_{\mathcal A_i}^{(-r)}$。
R773 的真实 $\mathcal D^\infty_{n,N}$ 满足 (36) 的条件，
而原含 t 的 E-ring 或浅独占门未必满足。

首项由 R767 的完整五伙伴收缩准确等于
$$
-d_pa\beta^m\kappa^m
 \int_{\mathcal D}\frac{t}{P}q\,d\bar e_B
 +p^{4m}\mathcal O .
\tag{37}
$$
这是同一个条件来源，不从 (34) 倒换一个裸负矩。
若把 t-deep m 改为第 m 个精确环带，
每个正 r 矩另保 $(1-\beta\kappa^r)$；
特别首项为已付 $(1-\beta\kappa)$。

对任意 $\mathcal T$-不变原域，$e_A$ 在三个 W 观察上的积分相同。
因此三个原 $e_0$ 行的两两差，**整条**都等于 $e_B$ 的相应差；
这不只对首项成立。R773 的共同深帽就在此范围内。
相反，未合并的三个浅 CD/O 原子仍须分别运输，不能各自相认。

## 8. 两单位更新式确实可解；它没有删除四单位函数

(17) 在所有连续有界测试上给准确有限 depletion
$$
\boxed{
\rho_0|_{\{P,t\ {\rm unit}\}}
=\rho_0-\alpha(P_{P,\kappa})_*\rho_0
-\beta(P_{t,\kappa})_*\rho_0
+\Delta(P_{\rm pl})_*\rho_0 .
}
\tag{38}
$$
其连续测试逆也可直接支付。
若 $S_Lf=f\circ P_{L,\kappa}$、$\Pi_Lf=f\circ P_{L,0}$，
且 c 是 $\alpha$ 或 $\beta$，则 $1-c$ 是原已付单位，
$$
\boxed{
\mathscr R_{c,L}f
=\frac{\Pi_Lf}{1-c}
+\sum_{r\ge0}c^r(S_L^rf-\Pi_Lf),\qquad
(I-cS_L)\mathscr R_{c,L}f=f .
}
\tag{39}
$$
紧集上一致连续保证各被加项一致趋零；非 Archimedean 完备性给
一致收敛。移位一项即证明显示的 telescoping 等式。
这个逆的范数不超过一，保所有其余伙伴坐标。
两个正交轴的逆交换，因此 (38) 是真正可解的同源更新式。

对本文完整 P/t 边际，两条 unit 边际都为零：
$f_1,f_4$ 的单位质量为零，$\mathcal A_1,\mathcal A_4$
的单位质量也由角型为零。
所以把 (39) 用于 $f_w(W)$ 后，中央导数可以明确写成
$$
\begin{aligned}
Z_B'(0)=d_p\int_{\{P,t\ {\rm unit}\}}\bigg[
&1_{W\ {\rm unit}}\log\langle W\rangle\\
&+\sum_{m\ge1}\beta^m\log(1-a\kappa^m t/P)\\
&+\sum_{\ell\ge1}\alpha^\ell
       \log(1-\kappa^\ell P/(at))
\bigg]\,d\rho_0 .
\end{aligned}
\tag{40}
$$
所有因子和正负号与 (31)、(34) 相同。
沿单轴的常数项是在上述**完整单位边际**为零后消去，
不是把一个局部 log 质量扔掉。
(40) 对一般另附门不自动有这些消去。

还有一个有限的四单位式。令
$$
\mathcal G=\{P,t,W,V_t\ {\rm unit}\}.
$$
四条线在 primitive $(P,t)$ 平面中两两不同；
它们的所有行列式只含既已排除的 $2,3,7,29$ 因子。
所以
$$
\boxed{
\rho_0|_{\mathcal G}
=\rho_0-\alpha(P_{P,\kappa})_*\rho_0
-\beta(P_{t,\kappa})_*\rho_0
-\lambda(P_{W,\kappa})_*\rho_1
-c_V(P_{V_t,\kappa})_*\rho_1
+3\Delta(P_{\rm pl})_*\rho_0 .
}
\tag{41}
$$
这是原六变量的完整测度式。若
$G(w)=\int_{\mathcal G}f_w(W)d\rho_0$，则
$$
\boxed{G(w)=(1-c_V)Z_B(w)-A_1(w)-B_1(w).}
\tag{42}
$$
V_t-deep/W-unit 的那一支准确为 $c_VZ_B$；
W-deep 的各近消环带准确为 (28)。
它们都没有被遗漏在 (42) 之外。

因此在原 $J_T'(0)=0$ 下，完整且精确的剩余条件是
$$
\boxed{G'(0)=-A_1'(0)-B_1'(0),}
\tag{43}
$$
并有每个 (28) 的中央导数零。
(31)、(34)、(40) 描述了 (43) 的所有实际系数。
这没有给 $G'$、$A_1'$、$B_1'$ 单独赋零，也没有把一个裸
$I_4$ 或 $I_1$ 代入整个四单位来源。

## 9. 原帽、CD、E 与 U 的全转置；相反外部仍在

以下明确说明为何 (24)、(28) 不能免费限制到 R773 的帽。
置
$$
\hat s=s-Y/17,\qquad\hat d=d-Y/17,\qquad
U=\hat s/2-3\hat d,\qquad
E_\perp=-(17+3\omega)\hat s-(68+99\omega)\hat d .
$$
对
$M=P_{P,z}P_{t,v}$，原各行准确变成
$$
\begin{aligned}
P\circ M&=zP,&t\circ M&=vt,\\
Y\circ M&=Y+\frac{17-3\omega}{29}(z-1)P,\\
s\circ M&=s-\frac a{29}(z-1)P,&
d\circ M&=d+\frac2{29}(z-1)P,\\
\hat s\circ M&=\hat s-\frac{2(17+24\omega)}{17\cdot29}(z-1)P,\\
\hat d\circ M&=\hat d+\frac{17+3\omega}{17\cdot29}(z-1)P,\\
U\circ M&=U-\frac{68+33\omega}{17\cdot29}(z-1)P,\\
E_\perp\circ M&=E_\perp-\frac{25+48\omega}{29}(z-1)P,\\
W_j\circ M&=zP-a\omega^{2j}vt .
\end{aligned}
\tag{44}
$$
C、F、G、q 不变。
原
$E_j=E_\perp+(17+3\omega)\omega^{2j}t$
的完整返回由 (44) 加上
$(17+3\omega)\omega^{2j}vt$，未删这个项。

特别原 CD 门始终是
$$
d\circ M\in p^N,\qquad
s-\frac a{29}(z-1)P-\omega^{2j}vt\in p^N,
\tag{45}
$$
原 O 门还保 $Y\circ M\in p^n$ 和
$$
\frac12\left(s-\frac a{29}(z-1)P-\omega^{2j}vt\right)
-3\left(d+\frac2{29}(z-1)P\right)\notin p^n .
\tag{46}
$$
所有真实 unit、Mellin 与尺度 log 同时按 (44) 运输。

例如在 R773 的
$\{Y\ {\rm unit},\hat s,\hat d\in p^N\}$ 上 P 是单位。
取 $z=\kappa^\ell,\ell\ge1$，(44) 中
$(17+3\omega)/(17\cdot29)$ 是 p-unit，
因为 $N(17+3\omega)=13\cdot19$。
故该帽经真实 P 收缩后，$\hat d$ 成为单位，而不再深 N。
同时
$$
Y\circ P_{P,z}
=\frac{144+349z}{493}Y
 +(z-1)\frac{17-3\omega}{29}(a\hat s+2\hat d),
\tag{47}
$$
所以 Y 仍是单位。这个新像是原 Y-unit 外部中的一个具体部分，
不与原帽相认。

由此，R773 已证的共同块非零确实可以运输到新的原像，
但其相反补偿必须一起按 (44)–(47) 搬运。
(43) 的 G 或其它三支，尚不能被原帽上的负一非零替代。
同样，原 cd 返回 $E$-unit 是归一后的事件，
不因 R773 原物理 $E_\perp$-shallow 空而消失。

## 10. 本篇完成的原中央接口及剩余的一条完整问题

新增的完整来源结论是 (6)、(9)、(17)、(22)；
新增的原中央零传播是 (24)、(28) 的实际 W/V_t 矩形及近消环带。
它们来自相同 q、相同原 T 来源和完整格，而非新赋一个来源中央零。

原 $S$ 中央在 $e_B$ 上的整条 Y 来源已为零；
这不会再迫 R773 的 $t/Y$ 或 $t/P$ 行为零。
对原 $T$ 中央，尚须处理的是同一 (43) 中 G 的真实条件来源，
或找到保持全部 (44)–(46) 门的额外原算术关系。
(8) 还准确说明：仅重排不附伙伴门的 P/t 分区，
所有 q_N 的原中央信息仍只是同一 $\beta^N J_T$。
新帽来源的信息在它与这些完整补项的联系中，不能由边际次数替代。

本文没有新的数值执行或可重算输出。所有常数由原显示 sigma 恒等式、
标准 Heisenberg 中心、两 sigma 联合锚与真实域单射直接证明。
负矩算术身份和全部无限和/点投影边界仍按原已付范围保持。

## 依赖

- R410 推论2、定理3及 R533 §3：原射线和整分母单位；本文第4节亦给所需 $1\pm\lambda$ 的直接证明。
- [R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)：原完整六度基、双变量核及指定负二/负五矩。
- [R692](R692-original-four-axis-three-state-and-arithmetic-unit-cuts.md)：原 W 三态、$K_W^2=I$ 与完整 T 边际。
- [R734](R734-joint-paid-tests-and-complete-type-five-arithmetic-plane.md)：同一个实际 $q_N^*$ 和全 $\pi_4$ 返回。
- [R764](R764-y-preserving-six-axis-and-three-cd-exterior-domains.md)：整框架、绝对 t 核、三个原 CD/O 域。
- [R767](R767-native-t-moment-and-complete-five-partner-boundary.md)：全四核及原首行。
- [R772](R772-original-p58-orthogonal-weight-and-full-finite-schwartz-source.md)：原 P 整格、半特征和 q 的逐项 P 正交性。
- [R773](R773-native-common-hat-domain-and-five-conditional-moment-return.md)：原帽、U 失败域和完整外部补偿。
