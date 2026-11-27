# R1024 — 原三字的六种固定连接、完整 P10 伴随与同一 primitive 的加权身份

日期：2026-11-27 UTC。**已证明。** 本篇消费
[R1022 的整个39支返回](R1022-original-thirtynine-flat-trace-and-common-degree10-reader.md)
中的真实 $W_\delta$，给其全部三个字一个先于 $p$ 固定的连接。
原 $P_{10}$、$G$、小留数、第二 section、Miller 和原测试全部保留。
特别，三挠平移的首水平项是原三处 Gaussian 的 Fermat 商，
第一非水平项是实际单位 $-3$；原 $P_{10}$ 的运输初值另行保留，
不能只用这个单位宣布 canonical 中央非零。

源端的固定 CM36 Hermite 及其四槽完整 Cartier 返回引用
[R1025](R1025-original-delta-flat-weight-full-cartier-and-cm36-hermite.md)。
本篇负责将这些式子放回真实加权 primitive 和原 $P_{10}$ 连接，
并明确其与原两条新必要行共用哪些权。

## 1. 原权的完整导数

沿 R1018/R1022 固定
$$
p=6s-1>13^4,\qquad H=6q+5\le s,\qquad
r=s-H\in\{0,1,2,3,4,5\}.
\tag{1}
$$
所以 $6H=p+1-6r$。仍用原 source 曲线
$E:y^2=x^3+1$、$X=x^3$、$D_{\rm up}=d/dz$。
原三处权是
$$
v=\frac X{X+1}=1-y^{-2},\qquad
W_\delta=v^{2q+2}B_{2q+2,q}(v).
\tag{2}
$$
令
$$
c_H=12(q+1)\binom{3q+2}{q}\in\mathbf F_p^\times.
$$
其单位性由 $0<q+1$、$3q+2<p$ 直接给出。
整个有限多项式的导数准确为
$$
\boxed{D_{\rm up}W_\delta=c_H(x/y)^H.}
\tag{3}
$$
证明：若 $a=2q+2$，则
$W=(1-y^{-2})^a\sum_{j=0}^q\binom{a+j-1}{j}y^{-2j}$。
完整二项式导数给
$W_v'=(-1)^qa\binom{a+q}{q}v^{a-1}(v-1)^q$。
再代 $D_{\rm up}v=6x^2/y^3$，所有符号相消，
$x$ 与 $y$ 的指数同时成为 $6q+5=H$，即 (3)。

因此模 $p$ 的真实二阶式是
$$
\boxed{
D_{\rm up}^2W_\delta=
\left(\frac16-r\right)
D_{\rm up}\log(x/y)\,D_{\rm up}W_\delta.
}
\tag{4}
$$
没有删除 $W_\delta$ 的其它字，也没有把增长权改成一个自由解。

## 2. 三字的固定六种连接及绝对 δ 缩放

本节 $(x,y)$ 改记 $[\delta]$ 的 target 坐标。
其微分和导数为
$\omega_\delta=[\delta]^*\omega_E=\delta\omega_{\rm up}$、
$D_\delta=\delta^{-1}D_{\rm up}$。
沿 R1022 的原根
$$
\kappa^3=1-y,\quad
\kappa=-\frac{y_{\rm up}+\delta}{\delta x_{\rm up}},
\quad
x_{\rm up}=-\frac{2\kappa}{\kappa^2-x},\quad
y_{\rm up}=\delta\frac{\kappa^2+x}{\kappa^2-x}
$$
写
$$
W_\delta=g_0+g_1\kappa+g_2\kappa^2.
$$
原
$g_i$ 全由 R1022(46) 代入 (2) 得到。
特别它们的相位及全部初始资料已经固定。

设
$$
a=\frac{y+1}{x},\qquad h=1-y,\qquad
\nabla_i=D_\delta+ia.
$$
直接微分 $\kappa^3=h$ 给 $D_\delta\kappa=a\kappa$。
完整乘法函数是
$$
\boxed{
L=D_\delta\log(x_{\rm up}/y_{\rm up})
=-\frac{x^2}{y}-\frac{\kappa}{y}
 +\frac{x}{y(1-y)}\kappa^2.
}
\tag{5}
$$
例如先写
$L=(h-a\kappa^2)/(\kappa^2+x)$，再用
$(\kappa^2+x)^{-1}=(x^2-x\kappa^2+h\kappa)/(-2yh)$，
即得全部三个系数。
这里是 **target 导数**，准确等于
$\delta^{-1}D_{\rm up}\log(x_{\rm up}/y_{\rm up})$。

记 $\nabla g=(\nabla_0g_0,\nabla_1g_1,\nabla_2g_2)^t$。
(4) 因而完整等价于
$$
\boxed{
\nabla^2g=
\left(\frac16-r\right)
\begin{pmatrix}
-x^2/y&x/y&-(1-y)/y\\
-1/y&-x^2/y&x/y\\
x/[y(1-y)]&-1/y&-x^2/y
\end{pmatrix}
\nabla g.
}
\tag{6}
$$
(6) 只有六种固定有理连接。它保留三个实际 $g_i$；
特别 R1022 中旧行用 $g_0$、原正三支用 $g_2$ 的区别未被抹掉。
第一阶的绝对尺度仍是
$D_\delta W_\delta=(c_H/\delta)(x_{\rm up}/y_{\rm up})^H$。

## 3. 固定 CM36 曲线中的真实微分

在 source 曲线上取固定六次 cover
$$
t^6=x/y.
$$
其归一化曲线 $\mathcal C$ 满足
$$
t^{36}=\frac{X^2}{(X+1)^3},\qquad
\omega_E=\frac{t^6}{6X}\,dX.
\tag{7}
$$
这不是随 $p$ 增长的 cover。
$x/y$ 在 $O,(0,\pm1)$ 有一阶零，在三个非零二挠点有一阶极；
六处全部完全分歧。Riemann–Hurwitz 给 $g(\mathcal C)=16$。
在本篇所有好位，这个固定 tame cover 及全部常数扩张均可约化。

置
$$
\beta_r=t^{\,1-6r}\omega_E
       =\frac{t^{\,7-6r}}{6X}\,dX.
\tag{8}
$$
于是 (3) 的整个微分身份为
$$
\boxed{dW_\delta=c_H t^p\beta_r,\qquad
\mathcal C_{\rm art}(\beta_r)=0.}
\tag{9}
$$
第二式确由第一式和 Cartier 的 $p$ 次乘数规则推出，
因为 $c_H$ 是单位且 $t$ 为非零函数。
字符分别为 $7,1,31,25,19,13\bmod36$。
(9) 从未被用于删除 $P_{10}\beta_r$。

R1025 给了真实的非加权对照。若
$R_\Psi=x^2(X-8)$、$R_{00}=x^2(X+10)$，
$n=(H-1)/2$、$C_H=(-1)^n\binom{H/3}{n}\in\mathbf F_p^\times$，
则在整个原曲线上
$$
\begin{aligned}
\mathcal C_{\rm art}((x/y)^H R_\Psi\omega_E)
 &=6C_H\frac{13-H}{9-H}\frac{\omega_E}{y},\\
\mathcal C_{\rm art}((x/y)^H R_{00}\omega_E)
 &=12C_H\frac{H-7}{9-H}\frac{\omega_E}{y}.
\end{aligned}
\tag{10}
$$
两系数都非零。同时 $(X+1),\,y(X+4),\,xy$ 的对应返回为零。
这些是原完整源端的返回，不是对加权输入的自动结论。

## 4. 原 P10 的完整扭曲 p 曲率与整个 first-Cartier 伴随

本节恢复原共同 target 的 $D,Z,G$，并记
$r_0=x^2/y$、$\mathcal H=G+r_0$。
R887 原式为
$$
D^p=0,\quad D^{p-1}G=r_0^p,\quad
P_{10}=-(D-10G)^{p-1}Z^{p+9},
$$
$$
DP_{10}=10GP_{10}+10(\mathcal H Z)^pZ^9.
\tag{11}
$$
它们在任一固定可分函数域扩张上仍成立。
对整数 $a$，在包含 $t$ 的域上置
$$
\mathscr L_a=D+10G+aD\log t.
$$
由 $t^{-a}(D+10G)t^a=\mathscr L_a$，完整地有
$$
\boxed{\mathscr L_a^p=10\mathcal H^p,\qquad
\mathscr L_a^{-1}=
\frac{\mathscr L_a^{p-1}}{10\mathcal H^p}.}
\tag{12}
$$
这里是函数域中的实际可逆算子；
$\mathcal H\ne0$ 由原点首项 $3Z^5/5$ 给出。
不把 $aD\log t$ 当作另一个可删的连接常数。

对任意完整有理输入 $u$，令
$Q=(D+10G)^{p-1}u/(10\mathcal H^p)$。
直接对 $P_{10}Q$ 微分，再用 Cartier 杀掉整个 exact，得到
$$
\boxed{
\mathcal C_{\rm art}(P_{10}u\omega_E)
=-Z\,\mathcal C_{\rm art}
 \left(Z^9(D+10G)^{p-1}u\,\omega_E\right).
}
\tag{13}
$$
所以同样有
$$
\boxed{
\mathcal C_{\rm art}(P_{10}t^af\omega_E)
=-Z\,\mathcal C_{\rm art}
 \left(Z^9t^a\mathscr L_a^{p-1}f\,\omega_E\right).
}
\tag{14}
$$
这两个式子是完整微分身份，不只一个最高 $p$-基系数。
所有实际 $Z^{-b-1}$、$h^e/h_i$、原测试或有限字因子
都可以包含在 $u$ 中；没有先删非 diagonal 项。

一阶版本尤其准确：
$$
\boxed{
\mathcal C_{\rm art}(P_{10}(D+10G)u\,\omega_E)
=-10\,\mathcal H Z\,\mathcal C_{\rm art}(Z^9u\,\omega_E).
}
\tag{15}
$$
对固定低层 $u$，内核有固定的二挠极帽；
外面的原 $\mathcal H$ 仍然保留。
不能把内核的小帽传播为整个 (15) 的小帽。

### 4.1 完整 CM36 Hermite 的真正加权残项

记
$$
A=4R_\Psi+5R_{00},\quad B=65R_\Psi+61R_{00},\quad
k=\frac{19-6r}{36},\quad
\lambda=\frac{19k-10}{2(k-1)}.
$$
R1025 的原函数证书准确化为
$$
\boxed{
\beta_r(B-\lambda A)=dV,\qquad
V=\frac{27}{4(1-k)}\,t^{1-6r}x^2U_B,\qquad U_B=xy.
}
\tag{16}
$$
因此乘上真实 $P_{10}$ 后，整个返回是
$$
\boxed{
\mathcal C_{\rm art}(P_{10}\beta_r(B-\lambda A))
=-10\,\mathcal C_{\rm art}(GP_{10}V\omega_E)
 -10\mathcal H Z\,\mathcal C_{\rm art}(Z^9V\omega_E).
}
\tag{17}
$$
第二项在 R1025 §7.1 已给四个原有限多项式系数槽；
第一项没有被赋零。
(12)–(14) 可直接作用于这个实际 $GP_{10}V$，
不需要添加一个自由的高权来源。

(16) 的 $x^2$ 与原 mode2 Miller 的关系也是精确的。
取 $S=(0,1)$、$R_2=-S$，有
$$
h_2(P-S)=\frac{x^2(y-1)^2}{64},\qquad
h(P-S)=\frac{2(y+1)}{y-1}.
\tag{18}
$$
所以 $x^2/h_2(P-S)=64/(y-1)^2$；
剩余 $h^e,g_2^p$、十三字符及这个两阶分母都保留。
此外 $x^2U_B=(U_A+2U_C)/3$。
故这里不是把一个乘法或 dyadic 投影免费传播为中央零。

## 5. 同一个原 section 的完整加权 primitive 恒等

令 $\varphi_H$ 是 R1020 的原平坦 section：
$\mathcal C_{\rm art}\varphi_H=\omega_E$，
在原点阶至少 $H+5$。
在任一上述固定可分扩域中仍用其实际拉回，定义
$$
S_H(f\omega_E)=f^p\varphi_H,\qquad
E_H=1-S_H\mathcal C_{\rm art},\qquad
\mathfrak P_H(\nu)=D^{-1}(E_H\nu)\pmod{F^p}.
\tag{19}
$$
Cartier 的核是 exact，故最后一式对全部有理微分有定义。
$E_H$ 及 $\mathfrak P_H$ 都是 $F^p$ 线性的；
不要求输入先是全纯或已删留数。

给任意实际 $\nu$，置
$$
U=\mathfrak P_H(\nu),\qquad
\mathcal C_{\rm art}\nu=\tau\omega_E.
$$
由 $\nu=dU+\tau^p\varphi_H$，完整分部积分给
$$
\boxed{
\mathfrak P_H(W\nu)
=WU+\tau^p\mathfrak P_H(W\varphi_H)
-\mathfrak P_H(U\,dW)\pmod{F^p}.
}
\tag{20}
$$
若把 $U$ 换成 $U+a^p$，右边增加
$a^pW-\mathfrak P_H(a^p\,dW)=0\bmod F^p$，
所以 (20) 不依赖 primitive 代表的选择。

在 R1022 的完整 $\alpha=\delta\pi$ frame 中，
取 $\omega_\alpha=\alpha\omega_{\rm up}$，
$\beta_{r,\alpha}=\alpha\beta_r$。
(9) 是
$dW_\delta=(c_H/\alpha)t^p\beta_{r,\alpha}$；
所以 (20) 准确变成
$$
\boxed{
\mathfrak P_H(W_\delta\nu)
=W_\delta U+
\tau^p\mathfrak P_H(W_\delta\varphi_H)
-\frac{c_H}{\alpha}t^p
 \mathfrak P_H(U\beta_{r,\alpha})\pmod{F^p}.
}
\tag{21}
$$
这是固定六种 CM 微分对实际第一 primitive 的配对。
它不是 $\beta_r$ 对原裸 $R_f$ 的配对；
二者之间的原 $P_{10}$ 扭曲由 (13)–(17) 完整保留。

### 5.1 原十三权、trace 与小留数

对于 R1022 的反次序权，把原
$W_\pi(\delta P)$ 和全部 $P_{10}/Z$/Miller 输入
先包含在 $\nu$ 中，再应用 (21)。
所有 section 都取自同一个最终 target，
故 Cartier、$E_H$ 及 exact 类与完整未平均 trace 交织。
常数 $\alpha^{-10}$ 经过第一次 Cartier 时准确变为
$\alpha^{-10/p}$；不能提前把它改成 $\alpha^{-10}$。
(21) 因而可逐字放入原39支 trace，未改变 cut 或高精度来源。

原 R1020 的留数修正也显式保留。
若 $\rho=\operatorname{Res}_O\eta$，记
$$
\Lambda_H=\mathfrak P_H(r_0\omega_E).
$$
由于 $r_0\omega_E=\frac13d\log y$ 被 Cartier 固定，
实际原 primitive 满足
$$
\boxed{
\mathfrak M_H(\eta)
=\mathfrak P_H(\mathcal C_{\rm art}\eta)
+\rho^{1/p}\Lambda_H.
}
\tag{22}
$$
这就是先把 $\eta$ 的原点留数按 R1020 去掉再取 primitive；
没有丢掉质量或某个 $b$ 的 affine 项。
所有 $b=0,\ldots,p-1$，包括最后四个非 diagonal 余数，
仍由 R1020 的同一读者回代。

在单独三处 cover 中，还有两个完全规范的小对数方向：
$$
\ell_1=\kappa\omega_\delta,\qquad
\ell_2=(x/\kappa)\omega_\delta.
\tag{23}
$$
两者只在三个 $\delta$ 核点有简单极，原点留数都是一；
其余两个留数是实际 deck 字符。
$C\ell_1=\ell_2$、$C\ell_2=\ell_1$。
证明：Cartier 保留相应留数并交换非平凡字符；
具有同样极和留数的差为全纯，而平移 deck 在全纯微分上平凡，
所以非平凡字符下差只能为零。
这些形式可支付单正分支的全部小留数，
不把非平凡字符的总迹零误认为原点读数零。

## 6. 原三挠平移的完整 G 水平项

取 $S=(0,1)$。原 addition 给
$$
x(P+S)=-\frac{2x}{y+1},\qquad
y(P+S)=\frac{y-3}{y+1},\qquad
j_S=\frac{y-1}{x}=\frac13D\log(1+y).
$$
原 $\lambda_S=0$，且 R887 的完整 $Z$ 差为
$$
Z_S=Z+h_S^p,\qquad
h_S=-3\rho_p\frac{x^2}{y(y-3)}
=-3\rho_pZ^2+O(Z^5),\qquad c_p\rho_p=1.
\tag{24}
$$
设
$$
\mathcal G_T(f)=
-\sum_{n=0}^{p-2}\frac{(-1)^nT^{n+1}D^nf}{(n+1)!},\qquad
\Pi_Tf=\sum_{n=0}^{p-1}\frac{(-T)^nD^nf}{n!}.
$$
原 $G$ 就是 $\mathcal G_Z(x)$，不是另一 primitive。
因 $x_S=x-Dj_S$，原全部运输严格为
$$
\boxed{
J_S=G_S-G-j_S
=\mathcal G_{Z+h_S^p}(x)-\mathcal G_Z(x)
-\Pi_{Z+h_S^p}j_S.
}
\tag{25}
$$
这已固定完整水平项，没有任意的 $k_S^p$。

等价地可写
$$
J_S=c_p\sum_{j=1}^{p-1}
 \frac{(-1)^{j-1}}j\,h_S^{pj}Z^{p-j}+k_S^p,
$$
$$
\boxed{
k_S^p=-\Pi_Zj_S+
\sum_{j=1}^{p-1}\frac{(-h_S^p)^j}{j!}
\,\Pi_ZD^{j-1}x_S.
}
\tag{26}
$$
这些都是原有限函数的完整式子，不是一个低 jet 拟合。

### 6.1 第一个 Gaussian 水平与真正的第三块单位

在 $S$ 固定的 CM3 作用下，$J_S$ 为型二。
因为 $p\equiv2\pmod3$，其水平项 $Z^{mp}$ 只允许
$m\equiv1\pmod3$；所以 $Z^{2p}$、$Z^{3p}$ 都不存在。

记原特征零
$q_\delta=\delta^{p+1}/3\in1+p\mathcal O$。
准确的最初展开是
$$
\boxed{
J_S=a_SZ^p-3Z^{3p-1}+O(Z^{4p}),\qquad
a_S=\frac{3c_p}{2}\,
 \overline{\frac{q_\delta-1}{p}}.
}
\tag{27}
$$
横线表示先在特征零真除 $p$ 再约化。

支付水平系数：$p$ 是奇数，故
$[z^p]j_S=[z^p](y/x)$。
原 $\sigma(\delta z)=\delta\sigma(z)^3x$ 给
$2y/x=\delta\zeta(\delta z)-3\zeta(z)$。
若 $\zeta_p=[z^p]\zeta$，则
$\zeta_p=-x_{p-1}/p$，且原规范给 $x_{p-1}\equiv c_p$。
再用 $Z=z+O(z^{5p})$，便得到
$[Z^p]j_S=-(c_p/2)\overline{(\delta^{p+1}-3)/p}$。
(25) 的坐标变化首阶是 $3p-1$，所以 $a_S$ 是其相反数。

支付非水平项：在 (26) 的 $j=1$ 项代入 (24)，得到
$c_p(-3\rho_p)Z^{3p-1}=-3Z^{3p-1}$。
$j=2$ 首阶至少 $5p-2$，$j=1$ 的下一项至少 $6p-1$；
下一可能的水平项是 $4p$。
所以 (27) 的余阶和单位都完整确定。

## 7. 实际 Miller／测试 connection 与 P10 初值

沿 R1022 的最终 $S_{10}$ 三字规范，
$h=1-y$、$R_1=S,R_2=-S$、
$h_1=(1-y)^{-3}$、$h_2=x^2/(1+y)^4$。
直接对整个函数微分，准确有
$$
\frac i3D\log h-D\log h_i=10j_{-R_i}.
\tag{28}
$$
又 $j_{-R}(P+R)=-j_R(P)$。
因此标准返回后的原核心 connection 是
$$
D+10G+10J_R-\frac{b+1}{Z_R}.
$$
相对于旧 $D+10G-(b+1)/Z$，完整差为
$$
\boxed{
M_{R,b}=10J_R+
 (b+1)\frac{h_R^p}{Z\,Z_R}.
}
\tag{29}
$$
其它十三字的全部 shifted 权仍留在实际乘积中；
(29) 没有把几何投影或十三权提前穿过平移。
标准返回还含原外部 $\tau_{-R}^*$：若用上式的内部坐标，
原测试点是 $P=-R$。下式在 $P=O$ 的精确运输展开，
不能单独代替带回外部拉回后的某条 canonical 第三读数。

特别
$$
\begin{aligned}
M_{S,b}
&=10a_SZ^p-3(b+1)\rho_pZ^{2p-2}
 -30Z^{3p-1}+O(Z^{4p-3}),\\
M_{-S,b}
&=10a_SZ^p+3(b+1)\rho_pZ^{2p-2}
 +30Z^{3p-1}+O(Z^{4p-3}).
\end{aligned}
\tag{30}
$$
末余数 $b=p-1$ 的测试项确实为零，未以一般首项替代它。
两支共同的 Gaussian 水平和相反的两后项都已经付清。

### 7.1 P10 的真实运输仍是独立账本

整个原 translated 模型必须使用
$$
\boxed{
P_{10,S}
=-(D-10(G+j_S+J_S))^{p-1}
 (Z+h_S^p)^{p+9}.
}
\tag{31}
$$
(31) 是原 finite 定义的实际拉回；
不能把 (27) 当作已付其全部初值。

若用原 canonical theta lift 的代数乘子 $q_S$，
$D\log q_S=j_S$，令
$Q_S=q_S^{10}P_{10}$、
$\Xi_{10,S}=P_{10,S}-Q_S$，则其完整方程是
$$
\boxed{
(D-10G_S)\Xi_{10,S}
=10J_SQ_S+
10(\mathcal H_SZ_S)^p Z_S^9
-10q_S^{10}(\mathcal HZ)^pZ^9.
}
\tag{32}
$$
$q_S$ 的绝对相位仍是原 torsion lift 的相位，不另选立方根。

实际初值已经说明为什么 (32) 不能删：
$P_{10}=-Z^p(D-10G)^{p-1}Z^9$；
$Z(S)=0$ 且 $G$ 在 $S$ 正则，所以 $P_{10}(S)=0$。
另一方面，$q_S$ 在原点有一阶极，
$P_{10}$ 的原点首项为 $Z^{10}$，
故 $Q_S(O)$ 是原固定非零 theta 常数，
$\Xi_{10,S}(O)=-Q_S(O)$。
原完整 (31)–(32) 而非仅一个 $G$ 前缀进入最终读者。

## 8. 当前可直接联立的实际数据

原四条 canonical 必要行、R1022 的两个严格 flat 返回顺序、
R1020 的同一 $\mathfrak M_H$ 和全部原点质量继续保持。
新增数据使真实三处权、Miller 连接和首三个 block 的补项都由
明确有理函数、原 Gaussian 或固定 CM36 微分决定。
R1025 的 exact 差进一步使加权残项只含实际 $x^2U_B$，
其完整 $P_{10}$ 伴随是 (17)，其真实移位倍率是 (18)。

要从这些行推出旧对数项消失，必须在这个同一读者中联立
(17)、(21)、(29) 和原 (31)；
没有使用“裸 Cartier 为零”“同一个 $g_2$”
或“单位 $-3$”作为额外 canonical 零。
本篇所有公式为手证，未运行本地数学或新增素数扫描。
