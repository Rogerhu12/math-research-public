# R1005 — 原单 P130 的全22返回、十三译像两 jet 修正与完整伴随

日期：2026-11-27 UTC。**已证明：R1003 的单 $P_{130}$ 模型可以准确扩至原全部22列，包括十三核上的非零质量轨道译像。代价只有两个明确的原低卷积标量；其中一个还有固定闭式。整个三次 Cartier 在全22上只留下首六阶系数的原对数线，真实第六读数仍完整保留两层 exact。**

下文把这两个修正代入 R987 的实际两个轨道，给出与完整 old 差相同的、两 jet 已准确消去的译像组合。同时给原有限 $p$ 基中的完整伴随与固定十三 Miller 运输；没有用两核零阶质量代替所有高 jet。

## 1. 同一个完整22维来源与两个首 jet

取 R1001/R1003 的同一个好惰性 $p=6s-1>211$、$E_1:y^2=x^3+1$、原 $Z,G,H,P_2,P_{130}$。记

$$
f=\sigma^{130}R_f,\qquad
R_f=x^2\sum_{i=0}^{21}u_iX^i,\qquad X=x^3,
$$

$$
m_0(f)=u_{21},\qquad
c_6(f)=u_{20}-\frac{26}{3}u_{21}.
\tag{1}
$$

这是完整来源的实际质量及首六阶系数。原两个第六读者分别是

$$
\mathcal T_6(f)=[Z^{6p+6}]P_2^{65}R_f,\qquad
\widetilde{\mathcal T}_6(f)=[Z^{6p+6}]P_{130}R_f.
\tag{2}
$$

原 $P_{130}$ 始终是

$$
P_{130}=-(D-130G)^{p-1}Z^{p+129},\qquad
(D-130G)P_{130}=130H^pZ^{p+129}.
\tag{3}
$$

没有重选一个局部水平解。R1003 已付 $m_0=c_6=0$ 时两读者相等；本篇支付其余两列的准确差。

## 2. 第一个完整乘法差只含严格低于 p 的输入

沿 R887 §19 的原首 Gaussian 规范置

$$
\mathcal F(w)=\frac{\sigma^\circ(z)}z,
\qquad f_0(w)=\mathcal F(w)^{-2},\qquad w=z^6,
\qquad \kappa_5=\frac{(3/5)^p}{c_p}.
$$

这里 $f_0$ 仅是本节的单位级数，不是 R992 的 degree10 来源。定义

$$
L_{65,p}=[w^p](f_{0,<p})^{65},\qquad
M_{k,p}=[w^s]f_0^k.
\tag{4}
$$

原有限式 R887(106)逐项给

$$
\boxed{A_p=L_{65,p}
       +\kappa_5\{-129M_{65,p}+65M_{1,p}\}.}
\tag{5}
$$

准确地，若 $e_{a,p}$ 表示该式中
$P_a/(\sigma^\circ)^a$ 的 $z^{6p}$ 系数，则

$$
e_{130,p}-65e_{2,p}
=[w^p]f_0^{65}-65[w^p]f_0
 +\kappa_5(-129M_{65,p}+65M_{1,p}).
$$

其中 $[w^p]f_0^{65}=65[w^p]f_0+L_{65,p}$。因此共同第 $p$ 个系数完整相消，而其余交叉卷积保留为(4)。式(5)只用 $f_{0,1},\ldots,f_{0,p-1}$，不是一个未指定的新高系数。

## 3. 下一项由原比值方程唯一固定

置 $C=P_{130}/P_2^{65}$。R887 的原完整比值方程为

$$
DC=\frac{130H^pZ^{p+1}}{P_2}
\left\{\left(\frac{Z^2}{P_2}\right)^{64}-C\right\}.
\tag{6}
$$

原型零及 R887(70)给

$$
C=1+A_pZ^{6p}+B_pZ^{6p+6}+O(Z^{6p+12}).
\tag{7}
$$

在所需低窗中

$$
P_2/Z^2=1+Z^6/105+O(Z^{12}),\qquad
H=(3/5)Z^5+O(Z^{11}).
$$

所以(6)右边的 $Z^{6p+5}$ 系数恰为
$-130\cdot64(3/5)^p/105$。左边的 $A_pZ^{6p}$ 导数为零，而下一项的导数系数为 $6B_p$。因而

$$
\boxed{B_p=-\frac{832}{63}(3/5)^p.}
\tag{8}
$$

这里没有在下一个 Frobenius 位置引入新水平项；$6p+6$ 不是 $p$ 的倍数。把 $z$ 换成 $Z$ 也不改(5)的首项，因 $z-Z=O(Z^{5p})$，且第 $6p$ 次幂的首变化远高于当前窗口。

对完整 $f$，$P_2^{65}R_f=m_0(f)+c_6(f)Z^6+O(Z^{12})$。乘(7)直接得到完整二 jet 修正：

$$
\boxed{\widetilde{\mathcal T}_6(f)-\mathcal T_6(f)
       =A_pc_6(f)+B_pm_0(f).}
\tag{9}
$$

式(9)在全部22列上成立。它也准确解释 R1003 的二十维零修正；没有撤回那篇的适用边界，而是付出了当时未被删除的两行。

## 4. 单 P130 在全22上的整个三次返回

定义实际微分

$$
\widetilde\eta_6(f)=Z^{-7}P_{130}R_f\omega_E.
\tag{10}
$$

在 $O$，它的完整前两主部是
$\{m_0Z^{-7}+c_6Z^{-1}\}dZ$。所有其它 $Z$ 零点由(3)的 $Z^p$ 因子准确消去。其余极只在三个原非零二挠点，极帽为

$$
d_p=p^3-p^2+122p+1<p^3.
\tag{11}
$$

所以三次 Cartier 后，在这三个点只可能有简单极；在 $O$ 只留 $c_6^{1/p^3}\omega_E/Z$ 的简单极。原 $\mu_6$ 不变性及留数定理唯一确定全部留数；没有额外的不变正则微分。于是整个函数域身份为

$$
\boxed{\mathcal C^3\widetilde\eta_6(f)
       =-c_6(f)^{1/p^3}r\omega_E,
       \qquad r=x^2/y.}
\tag{12}
$$

该式包括质量非零的第21列：其 $Z^{-7}dZ$ 在第一次 Cartier 就被杀掉，而不是事先删掉输入列。

### 4.1 两个 exact 多项式的完整读回

令 $t=-x^{-3}$、$Y=(t-1)^{-1}$。同一 quotient 的完整主部分解为

$$
\widetilde\eta_6(f)=\left\{
-\frac{m_0(f)}{6t^2}+\frac{c_6(f)}{6t}
+\sum_{k=1}^{\widetilde L_p}
 \frac{\widetilde b_{k,p}(f)}{(t-1)^k}\right\}dt,
\qquad \widetilde b_{1,p}(f)=-c_6(f)/6,
$$

$$
\boxed{\widetilde L_p=(p^3-p^2+122p+2)/2.}
\tag{13}
$$

这由(10)唯一规定，不能拿旧 $P_2^{65}$ 的主部替代。设

$$
\widetilde M_0=p(p-1)/2+61,\qquad
\widetilde M_1=(p-1)/2.
\tag{14}
$$

定义归一在 $Y=-1$ 的两个完整原函数

$$
\widetilde H_0(f;Y)=
\sum_{\substack{1\le j\le\widetilde M_0\\p\nmid j}}
\frac{\widetilde b_{1+jp,p}(f)^{1/p}}{j}
\{Y^j-(-1)^j\},
$$

$$
\widetilde H_1(f;Y)=
\sum_{j=1}^{(p-1)/2}
\frac{\widetilde b_{1+jp^2,p}(f)^{1/p^2}}{j}
\{Y^j-(-1)^j\}.
\tag{15}
$$

所有显示除数是单位。逐项 Cartier 给

$$
\mathcal C\widetilde\eta_6(f)
=-c_6(f)^{1/p}r\omega_E
-\{\widetilde H_0'(f;Y)
       +Y^{p-1}\widetilde H_1'(f;Y)^p\}\,dY.
\tag{16}
$$

使用原 $r=-z^{-1}+4z^5/7+\cdots$ 和
$dY/\omega_E=6z^5+\cdots$，再结合(9)，得到真正的原第六行：

$$
\boxed{\begin{aligned}
\mathcal T_6(f)={}&
-\left(\frac47+A_p\right)c_6(f)-B_pm_0(f)\\
&-6\{\widetilde H_0'(f;-1)^p
          +\widetilde H_1'(f;-1)^{p^2}\}.
\end{aligned}}
\tag{17}
$$

第三层已经准确删去，但两层(15)的导数没有被(12)赋零。对 $\mathcal B$ 用其两个二挠因子可再把第一上限降为 R1003 的 $p(p-1)/2+60$；第二上限不变。

## 5. 两个真实十三轨道的修正准确相消

保持 R987 的绝对两个 Weyl-dual 正轨道及其非零质量 $m_M,m_U$，写

$$
V=\frac{\mathcal U_+}{m_U}-\frac{\mathcal M_+}{m_M},
\qquad
C_{13}=\frac1{12}(m_M^{-1}-m_U^{-1}).
$$

该篇完整来源恒等式为

$$
V=\frac34\Delta_{125}+C_{13}\Phi_*,\qquad
m_0(V)=0,
\qquad c_6(V)=-16380\delta+C_{13}.
\tag{18}
$$

两个原质量归一在这里逐一保留，未把它们换成单位切域质量。减去真实首六阶项后得到

$$
\boxed{V-c_6(V)\Phi_*
       =\frac34\{\Delta_{125}+21840\delta\Phi_*\}
       =\frac34G_{\rm old}.}
\tag{19}
$$

因此，若记(9)的完整误差为
$\mathfrak d_p(f)=A_pc_6(f)+B_pm_0(f)$，则准确有

$$
\boxed{
\frac{\mathfrak d_p(\mathcal U_+)}{m_U}
-\frac{\mathfrak d_p(\mathcal M_+)}{m_M}
-c_6(V)\mathfrak d_p(\Phi_*)=0.}
\tag{20}
$$

质量修正 $B_p$ 先因 $1-1=0$ 相消，剩余的 $A_p$ 再由实际首六阶项相消。这是原两个译像的真实全修正，不需要假设它们各自中央为零。

令

$$
\mathscr E_p(f)=
\widetilde H_0'(f;-1)^p+
\widetilde H_1'(f;-1)^{p^2}.
\tag{21}
$$

该量对原 $K$ 系数线性，因为最后的 $p$、$p^2$ 次方恢复了 Cartier 的半线性。于是(17)–(20)给

$$
\boxed{
\frac{\mathscr E_p(\mathcal U_+)}{m_U}
-\frac{\mathscr E_p(\mathcal M_+)}{m_M}
-c_6(V)\mathscr E_p(\Phi_*)
=\frac34\mathscr E_p(G_{\rm old}),}
$$

$$
\boxed{\mathcal T_6(G_{\rm old})=-6\mathscr E_p(G_{\rm old}).}
\tag{22}
$$

这把两个实际轨道的所有共同高系数精确消去后，只留同一完整 old 来源的两个 exact 读数。R993 的原第六 Gaussian 仍给

$$
\overline{g_6(G_{\rm old})}
=-6\mathscr E_p(G_{\rm old})
 -7\kappa_5\overline{a^+(G_{\rm old})}.
\tag{23}
$$

低卷积不能随共同高系数一起删除。若原坏 canonical 假设给 $j_{\Phi_*}=0$，则 R978/R987 的完整中央仍准确为

$$
j_{G_{\rm old}}=(p+1)\log_p(\pi/\bar\pi)\ne0.
\tag{24}
$$

式(22)未把(24)赋零。将(23)插入六位中央时只替换其最后 $p^5$ 项，前五项保原六位精度，恰按 R1003 §6；原对数的全位检出深度继续用 R1000。

### 5.1 同一改善极帽中的真零行与十八阶非零对照

以下两个完整来源同时保持原 degree130、相同两个二挠因子与 $Q_2$，不用乘积传播中央零。置

$$
\boxed{\mathcal K=254\Phi_{260}-11\Phi_*-243\mathcal X_{130},}
$$

$$
\boxed{\mathcal C_{130}=90\mathcal B_{130}-43\mathcal K
=-122\Phi_{260}-517\Phi_*+729\mathcal X_{130}-90F_{10}.}
\tag{24a}
$$

两者的质量与首六阶项都为零。R999 已付的实际二挠首导数给

$$
P_{\mathcal K}'(-1)
=-11\frac{3\cdot3^{30}}{385}
 +243\frac{3^{30}}{2835}=0.
$$

每一项本来有 $X+1$ 与 $Q_2$ 因子，故

$$
(X+1)^2Q_2\mid P_{\mathcal K},P_{\mathcal C_{130}},
\qquad P_{\mathcal K},P_{\mathcal C_{130}}\in175^{-1}\mathbf Z[X].
\tag{24b}
$$

其准确原点阶不是仅由一个预计消去给出。原六 sigma 的轴
$(\delta,2\delta,\gamma_7,\bar\gamma_7,1,10)$ 给
$[z^{12}]F_{10}=99796/21$，因为六个六次幂之和为997960。
原 $\mathcal X$ 已付 $[z^{12}]\mathcal X=-2530/21$。
R992 实际 $\operatorname{Res}_\pi=A+\delta B$ 的最高项为
$A_{19}=-168799680/19$、$B_{19}=737190720/19$，而完整身份为

$$
A=-\frac{1612800}{19}(P_{260}-P_*)
       +90720(P_{\mathcal X}-P_*).
\tag{24c}
$$

与 R999 的 $[z^{12}]\mathcal B=24768$ 一起解这两条实际线性式，得

$$
[z^{12}]\Phi_*=-21164/21,\qquad
[z^{12}]\Phi_{260}=949/21,
\qquad [z^{12}]\mathcal K=51840.
\tag{24d}
$$

代回虚部也准确返回 $737190720/19$。因此(24a)的 $z^{12}$ 项恰消去。

再支付首个剩余项。原 $R_\pi=X^2+(2+6\delta)X+(40+24\delta)/13$ 的完整 $x$-map 在最高四列为

$$
A_\pi(X)=X^4+(-32-168\delta)X^3
 +(-1128-72\delta)X^2+(-1184-288\delta)X+\cdots.
$$

这些系数直接来自 R978 的完整式
$13R^2-6(7X+4)RR'-36X(X+1)(RR''-R'^2)$。
用 $P_{\Delta_{125}}=XA_\pi^5-8\pi^6A_\pi^2R_\pi^6-\text{共轭}$，以及
$\pi^6=253+1260\delta$，逐项读到

$$
[X^{18}]P_{\Delta_{125}}=1309869120\delta.
$$

R971 的全部 $P_S\mathcal J_5$ 同时给
$[X^{18}]P_F=-3948716/7$。代入
$F_{10}=-11\Phi_*/2+\delta\Delta_{125}/10080$，得

$$
[X^{18}]P_*=2439644/77.
\tag{24e}
$$

R992 原回执的下一列为
$A_{18}=-96254654400/19$、$B_{18}=-92910110400/19$；
其实际 $P_{\mathcal X}$ 在这一列是 $-1070858/21$。
从(24c)和 $P_{\mathcal B}=(B-5A)/3360$，完整得到

$$
[X^{18}]P_{\mathcal B}=42583680/7,\qquad
[X^{18}]P_{\mathcal K}=89641728/7.
$$

因此首个未消列准确为

$$
\boxed{\mathcal C_{130}
=-3151872z^{18}+O(z^{24})
=-2^{11}3^4\cdot19\,z^{18}+O(z^{24}),\qquad
\deg P_{\mathcal C_{130}}=18.}
\tag{24f}
$$

它在全部当前 $p>211$ 的好位都是单位首项。以上只是对既有原完整回执和原除法恒等式的纸笔消费，没有重新运行数学或保存生成多项式。

若两条 canonical 中央坏，则 $j_{\mathcal K}=0$，而

$$
\boxed{j_{\mathcal C_{130}}
=-\frac{\delta(p+1)}{112}\log_p(\pi/\bar\pi)\ne0.}
\tag{24g}
$$

原 ordinary ray 上相应准确值是
$-\delta(p-1)(1-\upsilon_p)\log_p(\pi/\bar\pi)/112$；返回 $b=17$ 后，来源的整体齐次因子仍为 $1/17$。
两来源都适用 R1003 的较低二挠帽与同一两层 exact，且(9)的两个修正均为零。
对 $\mathcal C_{130}$，第六输入在 $O$ 从 $z^{11}dz$ 起；
其 $a^+=[w^s](w^{-1}\mathcal C_{130}e^{-130cw^s})$ 因括号从 $w^2$ 起，只用原低输入至 $s-2$。
这个首阶改善没有把 $\mathscr E_p(\mathcal K)=0$ 当成 $j_{\mathcal K}=0$ 的直接后果；仍要保原前五项、低卷积及两个 exact。

## 6. 原 p 基的完整伴随与平移

本节显式记 $\mathscr F=k(E_1)$ 为特征 $p$ 函数域，区别于前面来源系数的 CM 数域。在 $\mathscr F/\mathscr F^p$ 的原基 $1,Z,\ldots,Z^{p-1}$ 上，置

$$
q=Z^p,\qquad \lambda(a)=[a]_{p-1}.
\tag{25}
$$

这里右边是完整 $p$ 基坐标，不能改成原点系数。配对
$(a,b)\mapsto\lambda(ab)$ 的原基矩阵是反对角单位阵，故完美；另有

$$
\lambda(Da)=0,\qquad
\lambda(aDb)=-\lambda((Da)b).
\tag{26}
$$

令 $P_{130}R_f=\sum\widetilde\beta_j(f)Z^j$。逐坐标有

$$
\widetilde\beta_6(f)=
\lambda(Z^{p-7}P_{130}R_f).
$$

将(3)完整转置 $p-1$ 次，并保全部 $Z^p=q$ 折回，得到

$$
\boxed{
\widetilde\beta_6(f)
=-q\,\lambda\!\left(
Z^{129}(D+130G)^{p-1}(Z^{p-7}R_f)\right).}
\tag{27}
$$

因为 $p-1$ 为偶数，这里没有额外的负号。式(27)不除以 $H$，也没有给 $R_f$ 另加一个有利的 primitive。

对于实际十三挠点 $T$，R887 已付
$Z\circ t_T=Z+h_T^p$。由于在原 $p$ 基中这只是以 $\mathscr F^p$ 元为参数的三角单位平移，最高坐标严格满足

$$
\boxed{\lambda(t_T^*a)=t_T^*\lambda(a).}
\tag{28}
$$

但是第六坐标不是最高坐标；它的真实平移是

$$
\boxed{[t_T^*a]_6=
\sum_{j=6}^{p-1}\binom j6
 h_T^{p(j-6)}\,t_T^*([a]_j).}
\tag{29}
$$

所以使用(28)时，必须保留(27)中的完整实际权；不能由最高坐标相容性把第六坐标直接视为一个平移不变量。

## 7. 原十三 Miller frame 中的单 P130 全运输

取 R993 的同一个二次 $R_\pi(X)$，并对非零 $T\in\ker\pi$ 定义

$$
a_T(P)=\frac{R_\pi(X(P))}{R_\pi(X(P+T))},\qquad
\operatorname{div}(a_T)=13(-T)-13(O).
$$

完整 canonical lift 是

$$
T_Tf=\sigma^{130}a_T^{10}(R_f\circ t_T),\qquad
D\log a_T=13(j_T+\lambda_T).
\tag{30}
$$

因为 $130=10\cdot13$，这份相位已在原曲线上下降，无须再选一个 cover 上的标量。令

$$
P_0=P_{130},\quad P_T=P_{130}\circ t_T,
\quad Z_T=Z\circ t_T,\quad H_T=H\circ t_T,
$$

$$
k_T=G\circ t_T-G-j_T-\lambda_T,\qquad
W_T=P_0a_T^{10}-P_T.
\tag{31}
$$

全部是原实际有限函数；特别 $k_T$ 仍保 R887(59) 的指定水平项：

$$
k_T=-c_p\sum_{j=1}^{p-1}\frac{(-1)^j}{j}
             h_T^{pj}Z^{p-j}+\kappa_T^p.
\tag{32}
$$

直接求导(31)，准确得到

$$
\boxed{\begin{aligned}
(D-130G\circ t_T)W_T
=130\{&a_T^{10}H^pZ^{p+129}
       -H_T^pZ_T^{p+129}\\
       &-k_Ta_T^{10}P_0\}.
\end{aligned}}
\tag{33}
$$

例如 $Z_T^{p+129}=(q+h_T^{p^2})(Z+h_T^p)^{129}$，其中129小于 $p$；这一有限二项式是合法的原输入，但(32)和(33)其它项仍完整存在。

在原点，$a_T(z)=z^{-13}/DR_\pi(T)+\cdots$，所以

$$
W_T(O)=(DR_\pi(T))^{-10}-P_{130}(T).
\tag{34}
$$

同一真实第六输入的整个运输必须写为

$$
\boxed{\begin{aligned}
&Z^{-7}P_{130}a_T^{10}(R_f\circ t_T)\omega_E
 -t_T^*(Z^{-7}P_{130}R_f\omega_E)\\
&=\{Z^{-7}P_{130}a_T^{10}
       -Z_T^{-7}P_T\}(R_f\circ t_T)\omega_E.
\end{aligned}}
\tag{35}
$$

原 $Z(T)$ 在两个核上的单位性由 R993 已付。其余全部移动 $Z$ 零点与二挠及其平移仍由(35)保留；这里没有令 $P_{130}(T)$ 等于1，也没有把 $Z_T^{-7}$ 改成 $Z^{-7}$。

式(30)–(35)先是每个 $T$ 的全函数身份。应用本篇全22的(12)、(17)时须按 R987 做同一个六点主型平均；单个 $T_Tf$ 不自动属于几何 $\mu_6$ 不变的22维子空间。

若使用 R993 的实际 $P_{260}-\varrho_\pi P_*=R_\pi Q_\pi$，只会把(35)的共同乘子乘上这个完整一次可除来源；该篇真实首商非零，故零阶消去本身仍不是高 jet 消去。现在所需的每一项可以通过(27)、(29)、(33)在同一个完整原算子中继续处理，无须另添未知的首乘法差。

## 依赖与范围

- R887 §§13–15、19：原 $Z/G$ cocycle、完整 $P_a$ 初始化及首乘法差。
- R987/R993：两个实际十三轨道、全部绝对质量、Miller frame 与真实首商。
- R1001/R1003：原第六坐标、整体 Cartier 返回及两层 exact 的有限部。
- R711/R989/R1000：原 Gaussian 低卷积、六位前五项和全位检出深度。

本篇没有数学执行或生成系数文件。新增的全22修正(9)、固定闭式(8)、全三次返回(12)、实际译像消去(20)及完整伴随(27)均由显示的原有限恒等式手证。继续中央 forcing 时须使用(17)、(23)、(35)的所有项；整个三次结果不替代第一次 Cartier 的实际读者。
