# R1032 — 饱和三挠权 β、无 Fp 的完整三十九支返回与新增两点主部

日期：2026-11-27 UTC。**已证明。**
本篇另构造一枚真正的特征零平坦权；
它保持原三十九支和完整中央精度，
而在末两窗的模 $p$ 返回中给一个没有共同 $F_p$ 因子的读者。
原权没有被无代价替换。新权的全部增长极位于原二挠点和
两个实际三挠点；原点留数、两个 exact 层和完整 affine 项均保留。

## 1. 同一个原来源与一枚新的显示权

保持 R1022/R1026 的全部规范：
$$
E:y^2=x^3+1,\quad X=x^3,\quad
\delta^2=-3,\quad\pi=(7+\delta)/2,\quad\alpha=\delta\pi,
$$
$$
p=6s-1>13^4,\qquad q\in\{s-3,s-2\},\qquad
H=6q+5\in\{p-12,p-6\},
$$
$$
n=H(p+1),\quad k=n/6,\quad a=n+1,\quad
e=a+k=7n/6+1,\qquad K=5s-2.
\tag{1}
$$
原来源为完整
$f=\sigma^{390}R_f\in\mathcal V_{390,\mathcal O}$；
其实际两条 canonical 是 R981/R983 的 $\Psi_{35},\Psi_{53}$。
若用原 degree130 来源，先取其真实 $D_\delta$ 拉回；
所有 $[\delta]$、$[\pi]$ 尺度都保留。

置
$$
\boxed{
\beta=\frac{X}{X+4},\qquad
B_{a,k}(T)=\sum_{j=0}^k(-1)^j\binom{a+j-1}{j}(T-1)^j,
\qquad
V_{\beta,n}=\beta^{n+1}B_{n+1,n/6}(\beta).
}
\tag{2}
$$
这是特征零有理函数，尚未取任何 $p$ 次幂。
原点 $1-\beta=4/(X+4)=O(z^6)$；
在 $\ker\delta\setminus O=\{S,-S\}$，其中 $S=(0,1)$，
$X$ 各有三阶零。
$X+4$ 的六个零都是单零；它们恰为
$E[3]\setminus E[\delta]$。
原 $\delta$ 映射在这六点的像为 $S$ 或 $-S$。
所以完整除子信息是
$$
\boxed{
\begin{aligned}
V_{\beta,n}&=1+O(z^{n+6}) &&\text{at }O,\\
\operatorname{ord}_{\pm S}V_{\beta,n}&=3(n+1),\\
\operatorname{pole}_{E[3]\setminus E[\delta]}V_{\beta,n}&=e.
\end{aligned}}
\tag{3}
$$
后两行在特征零是准确阶：
$B_{a,k}(0)=\binom{a+k}{k}\ne0$，
且其最高系数也非零。
这些整数约化后可能消失，只会提高核零阶或降低极阶。

十三处仍取原
$$
v_\pi=\frac{R_\pi(X)}{(X+1)^2},\qquad
V_{\pi,n}=v_\pi^{n+1}B_{n+1,n/6}(v_\pi).
$$
本篇固定反次序的完整原权
$$
\boxed{V_{\alpha,\beta}(P)=V_{\beta,n}(P)V_{\pi,n}(\delta P).}
\tag{4}
$$
其三挠极与 $\delta^{-1}(E[2]\setminus O)$ 不相交；
不能把两个因子移过实际源字的 torsion translation。

## 2. 单一特征零 trace 及完整中央精度

沿原 sigma division 写
$$
\sigma(\alpha z)=\alpha\sigma(z)^{39}R_\alpha(P),
\qquad R_\alpha=xA_\pi R_\pi.
$$
定义未平均的全部39支 trace
$$
\boxed{
A_{\beta,n}(f)=\alpha^{-10}\operatorname{Tr}_{[\alpha]}
 \left(V_{\alpha,\beta}\frac{R_f}{R_\alpha^{10}}\right),
\qquad h_{\beta,n}(f)=\sigma^{10}A_{\beta,n}(f).
}
\tag{5}
$$
每一支都采用 R1021 的真实 Miller lift。
与 R1016/R1022 完全同样的逐支 sigma 消去给
$$
h_{\beta,n}(f)(\alpha z)
=\sum_{T\in E[\alpha]}
 V_{\alpha,\beta}(P(z)+T)\,T_Tf(z).
\tag{6}
$$
这里没有平均 $1/39$，没有另外选逐字相位。

在 $T=0$，(3)和原 $V_{\pi,n}$ 均平坦到 $n+6$。
若 $T\ne0$ 且 $\delta T=0$，第一因子零阶为 $3(n+1)$。
若 $\delta T\ne0$，则 $\delta T\in E[\pi]\setminus O$，
第二因子零阶为 $n+1$；
第一因子在那里正则，因为其全部极不在 $E[\alpha]$。
每个 $T_Tf$ 全纯，故特征零准确有
$$
\boxed{h_{\beta,n}(f)(\alpha z)-f(z)=O(z^{n+1}).}
\tag{7}
$$
全部低项、非 diagonal 系数和质量都在此保留。

原 theta frame 的两个 Gaussian 给
$$
q_\alpha=\alpha^{p+1}/39\in1+p\mathcal O,\qquad
\gamma_\alpha=10c(\alpha^{p+1}-39)\in\mathcal O,
$$
$$
e^{-390cz^{p+1}}h_{\beta,n}(f)(\alpha z)
=e^{\gamma_\alpha z^{p+1}}
 \bigl(e^{-10cz^{p+1}}h_{\beta,n}(f)\bigr)(\alpha z).
\tag{8}
$$
下节支付与增长极无关的完整 Hurwitz 界。
因此 R1026 的相同整窗及无限尾逐项给
$$
\boxed{
j_{390,f}-j_{10,h_{\beta,n}(f)}
-m_0(f)\log_p q_\alpha\in p^K\mathcal O.
}
\tag{9}
$$
本篇的两个 $H$ 都有
$K=\min(H+1,5s-2)=5s-2$。
这是一条完整特征零中央比较，不是从 $\bar V=\beta^{p^2}$
直接把有限系数同余升到 $p^K$。

对原 $V_{\alpha}^{\mathrm{alt}}
=V_{\delta,n}(P)V_{\pi,n}(\delta P)$ 的真实来源记作
$h_{\delta,n}(f)$。
两边分别应用已付全精度定理，质量项相同，得到
$$
\boxed{
j_{10,h_{\beta,n}(f)}
-j_{10,h_{\delta,n}(f)}\in p^K\mathcal O.
}
\tag{10}
$$
在联合坏 canonical 假设下，两条原 rank 至少二来源
分别使 (9) 的 target 导数为零模 $p^K$；
(10) 不增加独立的算术零假设。

## 3. 全部增长极、整基及统一 Hurwitz 输入

记 $\mathcal D_2=E[2]\setminus O$。
(4)在 $\delta^{-1}\mathcal D_2$ 的极阶至多 $4e$，
在 $E[3]\setminus E[\delta]$ 的极阶至多 $e$。
这两组分别被 $[\alpha]$ 送到
$\mathcal D_2$ 和 $\{S,-S\}$，因为 $\pi S=-S$。
在所有非零 $\alpha$ 核，(3)和原十三零阶
都消去 $R_\alpha^{10}$ 的原十阶分母。
在 $O$，该比的极阶至多10。

有限 étale trace 不增加逐点极帽，因而
$$
\boxed{
\operatorname{div}_\infty A_{\beta,n}
\le10O+4e\mathcal D_2+e(S)+e(-S).
}
\tag{11}
$$
全部函数及 trace 在原好约化模型上整，
没有垂直极。新的分母只来自原 $2,3,13$ 和固定来源分母。

原 principal 型使 $A_{\beta,n}/x^2$ 是 $X$ 的有理函数。
令
$$
J=\left\lfloor\frac{e+2}{3}\right\rfloor,\qquad M=2e.
$$
三挠两点处的允许极阶须与 $x^2$ 的角色相容，
最大值为 $3J-2\le e$。由 (11) 及 $O$ 的帽，准确有
$$
\boxed{
A_{\beta,n}(f)=
\frac{x^2P_{\beta,n,f}(X)}{X^J(X+1)^M},
\quad
\deg P_{\beta,n,f}\le J+M+1,\quad
P_{\beta,n,f}\in\mathcal O[X].
}
\tag{12}
$$
整性可先乘显示的两个分母，再用原 $\mu_6$ 不变量环；
不需要一个含未知 $p$ 分母的线性求解。

沿原 $w=z^6,W_0=z^2x,U_\sigma=\sigma^\circ/z$，
(12)每个整基的完整 Gaussian 是
$$
\boxed{
(\sigma^\circ)^{10}
 \frac{x^2X^j}{X^J(X+1)^M}
=w^{J+M+1-j}U_\sigma^{10}
 W_0^{\,2+3j-3J-3M}
 (1+wW_0^{-3})^{-M}.
}
\tag{13}
$$
全部 $w$ 幂非负，$W_0$ 是原指定单位；
最后一个负整数幂有整二项式系数。
所以原完整 Hurwitz 代数与 $w<s(p-1)$ 整窗逐项保持，
严格内盘范数均至多一，常数不随 $e,J,M$ 增长。
这给 (9) 的真实 Tate 函数和其所有尾。

(11)–(13)是随 $p$ 增长的亚纯输入，
并非新的固定低高度 canonical 来源。
本篇没有把新增的 $S,-S$ 主部成本藏入旧二挠帽。

## 4. 末两窗的完整 β 饱和

(2)采用与 R1026 十三权相同的整数 $a=n+1,k=n/6$。
该篇的 Lucas 分解只依赖这些整数和
$T^aB_{a,k}(T)$ 这个完整多项式，故可在 $T=\beta$ 逐式使用。
在 (1) 的末两窗，$7q+6\ge p$，准确得到
$$
\boxed{\overline{V_{\beta,n}}=\beta^{p^2},\qquad
\overline{V_{\pi,n}}=v_\pi^{p^2}.}
\tag{14}
$$
所有被删的项都由原整数二项式的真实约化证明；
没有使用一个核上点值去冒充全函数。

因此本篇完整39权在特征 $p$ 为
$$
\boxed{
\overline{V_{\alpha,\beta}}
=(\beta\cdot v_\pi\circ\delta)^{p^2}.
}
\tag{15}
$$
第一 Cartier 后保
$(\beta\,v_\pi\circ\delta)^p$，第二次后保
$\beta\,v_\pi\circ\delta$。
它们的位置始终是原 source 点；
与全部 trace 的交织只按完整有限 étale 恒等使用。

## 5. 实际 δ 三字与没有 Fp 的两条返回

在本节的 $\delta$ target 上记坐标仍为 $x,y$，
取 R1022 的真实 Kummer 规范
$$
h=1-y,\qquad\kappa^3=h,\qquad
x_{\rm up}=-\frac{2\kappa}{\kappa^2-x},\qquad
y_{\rm up}=\delta\frac{\kappa^2+x}{\kappa^2-x}.
$$
整个原函数逐式化为
$$
\boxed{
\beta=\frac13+\frac{x}{3h}\kappa+\frac1{3x}\kappa^2.
}
\tag{16}
$$
例如令 $a_0=\kappa^2/x$，
则 $\beta=(1+a_0+a_0^{-1})/3$；
用 $\kappa^3=h$ 即得 (16)。
三个分量的表面 $x,h$ 分母在完整函数中按原式相消。

对 degree130 的实际下层 full13 来源 $G_A,G_B$，
仍取 R1021/R1028 的正三挠支和全部原 $\chi_6,\chi_{10}$。
它在本规范是 mode2，而不是 mode1。
由于
$$
\kappa^{p^2}=h^{(p^2-1)/3}\kappa,\qquad p^2\equiv1\pmod3,
$$
这个源字准确与 (16) 的第1系数
$\beta_1=x/(3h)$ 配对。
保持原
$$
h_{2,130}=\frac{x^2}{(1+y)^{44}},
\quad
\Phi_+=x/\kappa,\quad r_S=x/\kappa^2,
$$
以及 $Q_2=\delta^{130}C_S^{130}G$，
完整 Miller 返回中的比率是
$$
\frac{3\beta_1^{p^2}h^{(p^2+2)/3}}{h_{2,130}}
=r_S^{p^2}\Phi_+^{130}.
\tag{17}
$$
两边相除，剩下
$x^{-132}\{(1+y)(1-y)\}^{44}=1$，
因为 $(1+y)(1-y)=-x^3$、44为偶数。
故没有额外 $\delta$ 或三次根常数。

对原 $\delta$-old 的 $D_\delta g$，
未平均 trace 给 $3(1/3)^{p^2}=1$。
对原正三挠支，
(17)和 $T_S^{130}$ 的固定相位给
$$
\boxed{
\begin{array}{c|c}
\text{原完整来源方向}&\text{本篇 β 模型的实际 δ 返回}\\
\hline
D_\delta g & R_g\\
T_{u_3}^{390}D_\delta G &
r_S^{p^2}R_{T_S^{130}G}.
\end{array}}
\tag{18}
$$
这是 complete source 和全部十二个十三字之和上的身份。
反次序中的 $\pi S=-S$ 继续使第 $i$ 字为
$$
C_S^{130}\Phi_+^{130}M_i(P+S)
 U(\pi P+B_i-S).
\tag{19}
$$
不能把它改成另一顺序的 $U(P+S)$。

正支在 (18) 中是原完整非偶来源。
对 canonical 的 diagonal 读者，沿 R1021 的原 parity 恒等
最后取整个函数的偶 principal 部分；
(4) 两个权都为偶函数，故这一操作与完整 trace 交换。
(12) 和第7节的 principal 极帽应用于这个完整结果，
不提前投影 (18) 中的某一个来源因子。

十三权 $V_{\pi,n}$ 是 $\delta$ target 上的原 base 因子，
故必须再在 (18) 的完整每一行上按原序乘上并作其全 trace。
(18)不使各个十三字分别具有 canonical 零值。

## 6. 固定整来源与剩余三挠权的准确分离

R1021/R1030 已付 $G_A,G_B$ 为奇函数，且
$G(0)=G(S)=G(-S)=0$。
定义带原相位的固定完整来源
$$
H_G=r_S T_S^{130}G.
$$
由于 $r_S$ 只在 $S$ 有一阶极，而
$T_SG$ 在该点读取 $G(-S)=0$，该极确实消去；
其线束相位与原 $T_S^{130}$ 相消。
所以 $H_G$ 是原整 degree130 截面，而非剩一个抽象三次根来源。

更明确地，原 full13 类型给
$$
G=\sigma^{130}yP(X),\quad \deg P\le21,\quad P(0)=0.
$$
写 $P=XQ,\deg Q\le20$。用实际加法
$x(P+S)=-2x/(y+1)$、$y(P+S)=(y-3)/(y+1)$，得到
$$
\boxed{
H_G=-8C_S^{130}\sigma^{130}x^2
 (y+1)^{40}(y-3)
 Q\!\left(-\frac{8(y-1)}{(y+1)^2}\right).
}
\tag{20}
$$
括号为次数至多41的真 $y$ 多项式。
其偶、奇部分分别为
$$
\sigma^{130}x^2P_{\rm e}(X),\qquad
\sigma^{130}x^2yP_{\rm o}(X),
\quad \deg P_{\rm e},\deg P_{\rm o}\le20.
\tag{21}
$$
偶部分质量零、从至少 $z^6$ 起，
奇部分从至少 $z^3$ 起。
它们一般都存在，不将 $H_G$ 认作纯 odd 或纯 principal。

这里还有一个完整源图的刚性，说明不能通过一个固定标量
把实际两条 odd 伴线消去。
令
$$
R_Q(y)=(y+1)^{40}(y-3)
 Q\!\left(-\frac{8(y-1)}{(y+1)^2}\right).
$$
变换 $j(y)=(y+3)/(y-1)$ 保持 $Q$ 的自变量，且
$$
R_Q(j(y))=-2^{41}(y-1)^{-41}R_Q(y).
\tag{21a}
$$
若 $R_Q$ 为偶，则对 $k(y)=j(-y)=(y-3)/(y+1)$，
$$
R_Q(k(y))=2^{41}(y+1)^{-41}R_Q(y).
$$
原 $k^3=1$，三个分母的乘积准确为 $-8$。
三次迭代因此给 $R_Q=-R_Q$，故 $R_Q=0$，再得 $Q=0$。
所以 (20) 的 odd 投影在整个21维 $Q$ 空间上单射。
特别实际两个独立来源的 odd 部分也独立；
不能在后面的非偶权之前用一个常数关系删去它们。
这没有给任何 $H_G$ 新的算术零。

(18)的第二行准确为
$$
\boxed{
r_S^{p^2}R_{T_S^{130}G}
=\left(\frac{y+1}{y-1}\right)^{(p^2-1)/3}R_{H_G}.
}
\tag{22}
$$
右边完全下降到原 target 函数域；
剩余权有实际 $S,-S$ 零极。
该权不是偶函数，所以几何 principal 投影必须作用于完整乘积，
不能先删掉 (21) 的奇部分。
本篇没有把 $H_G$ 自身另赋 canonical 中央零。

## 7. 新增两点处的完整有限读者及两个 exact 层

在原 target 上保持
$$
\eta_{\beta,b}=Z^{-b-1}P_{10}A_{\beta,n}(f)\omega_E,
\qquad0\le b<p,
$$
以及原 $P_{10}=-Z^p(D-10G)^{p-1}Z^9$。
$Z(S)=Z(-S)=0$，由 $\mu_3$ 类型与 $DZ=1$ 可知是单零。
原 $Z^p$ 因子保证 $P_{10}$ 在这两点至少 $p$ 阶零，
因为 $G$ 在两点正则。
故全部 $b<p$ 下 $Z^{-b-1}P_{10}$ 在两点正则。
结合 (11)，完整极帽是
$$
\boxed{
\begin{aligned}
\operatorname{pole}_O\eta_{\beta,b}&\le b+1\le p,\\
\operatorname{pole}_{\mathcal D_2}\eta_{\beta,b}
&\le d_{2,b}=p^3-p^2+(8-b)p+4e+1<2p^3,\\
\operatorname{pole}_{\pm S}\eta_{\beta,b}&\le e<p^3.
\end{aligned}}
\tag{23}
$$
不在这些集合内的其它 $Z=0$ 点仍由原 $Z^p$ 消去，
没有新增未列出的补极。
(23)的严格不等式由 $H\le p-6$、
$4e=14H(p+1)/3+4$、$p>13^4$ 直接给出。

原点留数保持准确值
$$
\rho_{\beta,b}=\operatorname{Res}_O\eta_{\beta,b}
=\alpha^{-b}c_b(f).
\tag{24}
$$
定义
$$
\eta_{\beta,b}^{\,0}
=\eta_{\beta,b}+\rho_{\beta,b}r_0\omega_E,\qquad r_0=x^2/y.
$$
令 $\nu_1=C\eta_{\beta,b}^{\,0}$、$\nu_2=C^2\eta_{\beta,b}^{\,0}$。
它们在 $O$ 正则。
在 $\mathcal D_2$ 的准确可用形式帽为
$$
d_{2,1}=\left\lfloor\frac{d_{2,b}-1}{p}\right\rfloor+1,\qquad
d_{2,2}=\left\lfloor\frac{d_{2,1}-1}{p}\right\rfloor+1;
$$
在 $S,-S$ 则为
$$
d_{3,1}=\left\lfloor\frac{e-1}{p}\right\rfloor+1,\qquad
d_{3,2}=\left\lfloor\frac{d_{3,1}-1}{p}\right\rfloor+1\le2.
\tag{25}
$$
这里没有用二挠帽代替三挠主部。

沿 R1020 取同一个 target 平坦截面
$\varphi_*=\varphi-dJ_{p-6}$，
$C\varphi_*=\omega_E$，
$\operatorname{ord}_O(\varphi_*/\omega_E)\ge p-1$，
并定义 $\mathfrak S_*(u\omega_E)=u^p\varphi_*$。
在 $S,-S$，原 $\varphi=-3x/(c_p(X+1))\omega_E$ 至少一阶零；
$Z=0$ 且 $dJ_{p-6}$ 从 $Z^4$ 起，所以 $\varphi_*$ 也至少一阶零。
因此完整 Cartier 零差
$\nu_1-\mathfrak S_*\nu_2$ 的逐点帽为
$$
\boxed{
\begin{aligned}
L_2&=\max\{d_{2,1},\,p(d_{2,2}+p-7)\}
 &&\text{at }\mathcal D_2,\\
L_3&=\max\{d_{3,1},\,pd_{3,2}-1\}\le2p-1
 &&\text{at }S,-S .
\end{aligned}}
\tag{26}
$$
原 $F/F^p$ primitive 类
$$
[K_{\beta,b}]
=D^{-1}\{\nu_1-\mathfrak S_*\nu_2\}
\tag{27}
$$
可按原 genus1 Mittag-Leffler 证明选成
$V_{\beta,b}+a_{\beta,b}Z$，
$V(O)=0$、二挠极至多 $L_2-1$、
三挠极至多 $L_3-1$，其它点无极。
全局障碍仍由
$\sum_T\operatorname{Res}_T(V_T\omega_E)
=-\sum_T\operatorname{Res}_T(Z\,dK)=0$ 支付；
这一次求和明确包括 $S,-S$。
原 affine $a_{\beta,b}Z$ 必须保留。

因此全部真实低窗仍由同一个 primitive 读取：
$$
\boxed{
t^{10}_{rp+b}(A_{\beta,n})
=\left(
-\rho_{\beta,b}^{1/p}[Z^{r-1}]r_0
+r[Z^r]K_{\beta,b}
\right)^p
\quad(1\le r\le K,\ 0\le b<p).
}
\tag{28}
$$
$r=0$ 准确为 (24)。
同一个 $b\equiv5\pmod6$ 的第二层 scalar 被
$\mathfrak S_*$ 完整编码，未被设为零。
至多四阶真实连接仍只降低原点阶四，
$\varphi_*$ 的原点阶足以覆盖该整个窗口。
所有 $S,-S$ 主部和它们的真实留数都在 (27) 里，
不能凭低窗只写一个裸有理原函数。

显示 (23)–(26) 是未施额外四阶伴随的 $\eta_{\beta,b}$ 的帽。
若先在完整微分上施 R1021/R1028 的实际四阶伴随，
$S,-S$ 处先把 $e$ 改成 $e+4$；
当前严格余量仍给 $d_{3,2}\le2$、$L_3\le2p-1$。
二挠处则须按原 $G$ 和全部连接的真实极阶另加入四次费用，
不能宣称显示的 $L_2$ 逐项不变。
R887 已付原 $G$ 的二挠极阶为 $p^2-p-1$，故保守的完整
四阶帽为 $d_{2,b}+4(p^2-p-1)<2p^3$；第三 Cartier 的
double 范围仍不变。
本篇上述原点四阶兼容只说明平坦截面的低窗不被读到，
不替代这些其它点的完整极成本。原点处最后四个 $b$ 的第五块
补项仍按 R1018 保留；(24)、(28)不被直接冒用为已经施加四阶
伴随后的原点公式。

若显式保第三 Cartier 边界，
(23)给二挠至多 double、$S,-S,O$ 至多 simple。
在原六个二挠边界之外，
加入
$$
d\log y,\qquad d\log(y-1),\qquad d\log(y+1)
\tag{29}
$$
即可得到这整个九维边界空间。
它们分别支付二挠总留数与两个三挠留数，并在 $O$ 保持总留数零。
每个 (29) 都被 Cartier 固定；
不存在把新增留数放入 exact 核的步骤。
这份显式边界与 (27) 的完整 primitive 编码严格等价。

## 8. 两合法模型之差与当前可消费的范围

把 R1028 的真实
$K_p=-c_p(x/y)^{p^2}F_p^p$ 保留。
其共同低窗模型在 $\delta$-old/new 两方向是
$$
2R_g+K_pR_g,\qquad
-K_pr_S^{p^2}R_{T_S^{130}G}.
$$
与本篇 (18) 相减，准确余项分别为
$$
\boxed{
(1+K_p)R_g,\qquad
-(1+K_p)r_S^{p^2}R_{T_S^{130}G}.
}
\tag{30}
$$
这里指的是 R1028 已支付整个39支 primitive 的共同模 $p$ 模型；
原 $V_{\delta,n}-W_\infty^p$ 的全函数项仍依该篇保留，
并未被宣布为零。

在真正 native $O$，
$1+K_p=O(Z^{p^2+p})$；
这解释了两份完整平坦模型为何有相同低窗。
在其它十三纤维点不得使用该原点阶。
对应的全特征零关系已经由 (9)–(10)独立支付，
而不是通过 (30) 猜测。

现在两条新 canonical 的真实有限读者可在 (18)、
(22)、(27) 直接使用；
相较原 $F_p$ 共因子，固定 β 返回不再需要先消一个增长的
$F_p$ 槽。
但 $P_{10}$、原连接曲率、全部十三 profile、
(22)的三挠权、(24)的低项及 (27)两组主部仍在。
R1025 §12.4 的实际单位组合
$\lambda_1-(10/81)\lambda_2$
只有在这些完整同一测试中被迫出现，才能给出中央非零。
本篇未由 (30) 的表示法或裸 Cartier 单位宣称这一 forcing 已完成。

全文为原完整 sigma/trace、显示有理函数和实际 Cartier 证明。
无新增数学执行或素数扫描。
