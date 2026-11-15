# R806 — 原型四三条来源的十八阶角色、负二 Katz 值与准确临界锥

日期：2026-11-15。**状态：下述完整有限角色、原 Schwartz 来源、全权平方、负二特化及函数方程符号已证明。指定负二值与其实际三项线性组合的非消失未据此预付。**

本篇保持 R801 的同一个 $q_N^*$、全部58行、物理 E 深条件、
原 $Z^2/Y^2$ 观察和完整 W 外部。R798 的三维型四块不是
R761 的型五 primitive 块：二者虽有同一个 CM13 多项式，
其二处向量、十七处标签及合法整数权均不同。
这里给出这个实际型四块的完整算术身份，并先排除一个具体障碍：
原负二 Katz 支的自对偶函数方程乘子为 $+1$，并不被符号强制整零。

后续补充：[R804](R804-original-order-eighteen-soule-classes-and-negative-two-localization.md)已从原全 ray class 单位支付第8节保留的实际十八阶全局类及共同 Artin 周期；指定局部非零与原线性负二行仍未完成。

## 1. 原三维空间与全部有限标签

固定
$$
K=\mathbf Q(\omega),\quad \omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad \theta=17^{1/6}>0 .
\tag{1}
$$
$\psi_0$ 是 $E_0:y^2=x^3+1$、微分 $dx/(2y)$ 的原 type-$(1,0)$
Hecke 角色；$\Omega_{p,0}=\theta\Omega_p$，
$\varpi_0=s_0\Omega_0$，$s_0=(1-\omega)^{-1}$，
$\Omega_0>0$ 是 R735 的实周期。
原 $\lambda=-\bar\pi_0^{-1}$、$\kappa=p\lambda^2$ 和
$\beta=-\lambda$ 不变。

沿 R798 记
$$
V_4=\sigma^{34}K[X]_{\le5},\quad X=x^3,\qquad
\mathcal B_4=\operatorname{im}P_4
=\ker(\mathcal A_{13}^3+\omega),\qquad \dim_K\mathcal B_4=3 .
\tag{2}
$$
原整个 degree34 finite Weil 模为二处二维模与十七处十七维模的张量。
在 R735/R761 的同一极化、加性角色和绝对 splitting 下，
$$
v_\pm=(1,t_\pm,-1,t_\pm),\quad
t_\pm=(1\pm\sqrt3)/\sqrt2,
\quad
g_0=2+4\delta\in\mathbf F_{289}^{\,1},\quad
g_0^6=\omega,
\quad \tau_j(g_0)=\zeta_{18}^{\,j}.
\tag{3}
$$
十七维模除 quadratic 标签 $j=9$ 外，其余标签各单重。

几何 $\omega$ 的实际标签是 $g=\omega^2$。
它在 $v_+,v_-$ 上分别作用为 $1,\omega^2$，
在十七处作用为 $\tau_j(g_0^{12})=\omega^{2j}$。
型四要求偶性和几何 $\omega$ 特征 $\omega$，故整个型四是
$$
(v_+,j=2,8,14)\ \oplus\ (v_-,j=4,10,16).
\tag{4}
$$
这里不能将几何 $\omega$ 的标签换成 $g=\omega$。

原 $\mathcal H_Y$ 只在 dyadic 因子上作用：
它由完整 Y 二挠平移构成，与十七处有限群逐项交换。
R798 在 R735 的两个实际 $v_-$ 来源上付
$\mathcal H_Y=\omega$，在 $v_+$ 的三条型五来源上付
$\mathcal H_Y=\omega^2$，因此这已经确定它在整个二维 dyadic 因子上的作用。
所以原 $P_4=(I-\omega\mathcal H_Y)/(1-\omega^2)$ 恰选择
$$
\boxed{\mathcal B_4=(v_-,j=4,10,16).}
\tag{5}
$$
这用的是已付全 halfperiod 及完整 tensor；不是从 CM13 三次因子猜 dyadic 标签。

下文置
$$
\mathcal J=\{4,10,16\},\qquad l_j=j-9\in\{-5,1,7\}.
\tag{6}
$$
令 $\vartheta_l(u)$ 为 $(u\bmod17)^{16l}$ 的 $\mu_{18}$ 提升。
这三个角色均准确为十八阶，且
$$
\vartheta_l|_{\mathbf F_{17}^{\times}}=1,\qquad
\vartheta_l(\omega)=\omega,\qquad
\vartheta_l(\delta)=-1 .
\tag{7}
$$
最后的负号是与 R761 奇标签族的实质区别。

## 2. 实际有限 Hecke 角色和 uniformizer

对素于34的主理想 $(a)$ 定义
$$
\boxed{
\eta_j((a))
=\left[
 \operatorname{Teich}_{\mu_3}(a\bmod2)^{-1}
 \vartheta_{l_j}(a\bmod17)
 \right]^{-1}.
}
\tag{8}
$$
在更换生成元 $\omega$ 时，括号是 $\omega^2\omega=1$；
在 $-1$ 上也为1。由于 $h_K=1$，(8) 确实定义全局有限角色。
其 idèle 单位分量与括号一致，而与理想值互逆：
$$
\begin{array}{c|c|c}
v&\eta_{j,v}(u),\ u\text{ 为单位}&\text{指定 uniformizer 值}\\ \hline
2&\operatorname{Teich}_{\mu_3}(u)^{-1}&\eta_{j,2}(2)=1\\
3&1&\eta_{j,3}(\delta)=-1\\
17&\vartheta_{l_j}(u)&\eta_{j,17}(17)=1 .
\end{array}
\tag{9}
$$
三处**不分歧**不等于其 uniformizer 值为1。
确实 $\delta\bmod2=1$，而 (7) 给 $\eta_j((\delta))=-1$。
主有理 idèle 2、17 则给另外两个显示的值1。

因此
$$
\eta_j^c=\eta_j^{-1},\qquad
\operatorname{ord}\eta_j=18,\qquad
\mathfrak f_{\eta_j}=(34).
\tag{10}
$$
它在有理 idèle 上平凡。三个角色在
$E=K(\zeta_{18})=\mathbf Q(\zeta_9)$ 上构成一个完整的 $K$-Galois 轨道。

还可以逐坏位确定两个真实幂关系。令
$\psi_{17}$ 为原曲线 $y^2=x^3+17$ 的角色，
$\kappa_{17}=\psi_{17^3}/\psi_0$ 为 R761 的 quadratic17 角色，则
$$
\boxed{\eta_j^3=\psi_{17}/\psi_0,\qquad
       \eta_j^9=\kappa_{17}.}
\tag{11}
$$
第一式在2处平凡，17单位指数是 $48l_j\equiv48\bmod288$，
在 $\delta$ 上是 $-1$；这与原六次剩余公式完全相同。
第二式的17单位指数为144、三处 uniformizer 为 $-1$。
故三条有相同核，切出一个固定 cyclic18 扩张
$$
H/K,\qquad [H:K]=18,\quad e_2=3,\quad e_{17}=18,\quad e_3=1 .
\tag{12}
$$
其三处 Frobenius 值为 $-1$，且 $H^{I_2}=K(17^{1/6})$。
(12) 是有限角色域；本文没有把它冒称为已构造高权周期的点坐标域。

## 3. 合法正权、所有坏处和 Hermitian 类

对每个非负
$$
m\equiv4\bmod6,\qquad
\Phi_{j,m}=\eta_j\psi_0^{\,2m+1},\qquad
\chi_{j,m}=\Phi_{j,m}\mathrm N^{-m-1/2},
\tag{13}
$$
原完整有限表恒为
$$
\begin{array}{c|c|c}
v&\chi_{j,m,v}(u)&\text{uniformizer}\\ \hline
2&\operatorname{Teich}_{\mu_3}(u)^{-1}&-1\text{ 于 }2\\
3&u\bmod\delta\in\{\pm1\}&-i\text{ 于 }\delta\\
17&\vartheta_{l_j}(u)&-1\text{ 于 }17 .
\end{array}
\tag{14}
$$
这里 $2m+1=9+12r$。
三处的 $-i$ 是基角色 $i^{2m+1}=i$ 乘 (9) 的 $-1$；
若省掉 (9) 就会写错整个来源。
原导子准确为 $(34\delta)$，其范数为3468。

十七处的完整 Gauss 和可以直接求出，无须数值样本。
若 $\vartheta$ 是 (7) 的任一角色，写
$S_x=\sum_y\vartheta(x+y\delta)$，零点项取零。
由其在 $\mathbf F_{17}^{\times}$ 上平凡，
$$
S_0=16\vartheta(\delta)=-16,\qquad
S_x=-\vartheta(\delta)=1\quad(x\ne0).
$$
原非平凡 trace 加性角色因此给
$$
\sum_{z\in\mathbf F_{289}^{\times}}\vartheta(z)\psi_{\rm tr}(z)
=17\vartheta(\delta)=-17.
\tag{15}
$$
乘原 uniformizer 的 $-1$ 后，十七处 epsilon 为 $+1$；
再乘 $\chi_{17}(\delta)=-1$，Yang dichotomy 仍为 $-1$。
二、三处使用与 R735 完全相同的两个局部角色，dichotomy 分别为 $+1,-1$。
正无穷 Hermite 部分的 dichotomy 为 $+1$。
所以原代表和 Gaussian 正是
$$
\boxed{\alpha=17,\qquad \mathcal G=51\sqrt3.}
\tag{16}
$$

还要单独核 root，而非仅记 (16)。
正 $m\equiv4\bmod6$ 时，四处 epsilon 依次为
$$
\epsilon_{2,3,17,\infty}=(+1,-i,+1,i^{\,2m+1})
                       =(+1,-i,+1,i).
$$
因而
$$
\boxed{W(\Phi_{j,m})=+1\quad(m\ge0,\ m\equiv4\bmod6).}
\tag{17}
$$
这是整个合法正整数支的符号；不声称该支每个复中心值都非零。

## 4. 完整 Schwartz 与准确标准 theta 来源

沿 R735 原17维 Weil 算子 $W(g)$ 定义
$$
\Pi_j=\frac1{18}\sum_{r=0}^{17}\zeta_{18}^{-jr}W(g_0^r).
\tag{18}
$$
原全环面 character trace 给 $\operatorname{rank}\Pi_j=1$。
选择最小 $a_j\in\{0,\ldots,16\}$ 使
$\Pi_je_{a_j}\ne0$，置 $f_j=\Pi_je_{a_j}$ 并保
$n_j=\sum_a|f_j(a)|^2>0$。
因为 $\overline{W(g)}=W(g^{-1})$，$\Pi_j$ 为实矩阵；
$j$ 为偶数使 $f_j(-a)=f_j(a)$。

完整 finite tensor 为
$$
\phi_{2,j}=f_A+t_-f_B,\qquad
\phi_{3,j}=\mathbf1_{3^{-1}\mathbf Z_3},\qquad
\phi_{17,j}=\sum_a f_j(a)\mathbf1_{a/17+\mathbf Z_{17}},
\tag{19}
$$
其余处取原球。范数分别为 $3-\sqrt3,3,n_j$。
二处全部 $\mu_3,-1,g_*$ 生成元和三处全部主单位已经由 R735
对 (14) 的同一局部角色付清。
十七处 Hilbert90 为 $g=u/\bar u=u^{-16}$；
加上原 quadratic splitting，(14) 的不变标签为
$g^{9+l_j}=g^j$。因此 (19) 核定的是完整本地环面。

有理共同支撑及完整 Fourier 系数为
$$
a_{j,n}=v_-(n\bmod4)f_j(3n\bmod17),\qquad n/102 .
\tag{20}
$$
它是非零实偶序列，周期68，且
$(-1)^na_{j,n+34}=-a_{j,n}$。
于是
$$
S_{j,\Lambda}(Z)
=e^{34\sqrt3\pi Z^2}
 \sum_{n\in\mathbf Z}a_{j,n}
 \exp\!\left(\frac{\pi i(\delta/3)n^2}{68}+2\pi inZ\right)
\tag{21}
$$
下降到原标准 $S_{34}$，没有额外平坦二挠 twist。
(4) 给其准确角型4，实轴上为实数。

仍保 R735 的完整 CM13 公共标量 $-\omega^2$、
dyadic 标签 $\omega^2$、17标签 $g_0^{14}$。
其作用是
$$
\mu_j=-\omega\,\zeta_{18}^{14j},\qquad
(\mu_4,\mu_{10},\mu_{16})
=(\zeta_{18}^{17},\zeta_{18}^{11},\zeta_{18}^{5}).
\tag{22}
$$
三根恰满足 $T^3+\omega$，所以非零 (21) 穷尽 (5)。
这里先核完整角色和 Schwartz，再由全 trace 的已付单重性认截面，
不是从 (22) 猜全角色。

这三条的首阶均准确为4。首 $z^4$ 是 K 上的线性行，
在 R798 的 $P_4(\sigma^{34})$ 上取值 $136/13122\ne0$。
若它杀一条特征线，$T^3+\omega$ 的 K-不可约性和完整 Galois 轨道
会迫它杀全部三条，与上述值矛盾。
因此唯一规范
$$
S_{j,\Lambda}(Z)=s_jD_{j,1}(\Omega_0Z),\quad
[z^4]D_{j,1}=1,\quad s_j\in\mathbf R^\times
\tag{23}
$$
已定义固定代数 theta 来源 $D_{j,1}\in\mathcal B_4\otimes_K E$。
也可在 (2) 上用
$(\mathcal A_{13}^2+\mu_j\mathcal A_{13}+\mu_j^2)/(3\mu_j^2)$
实际抽取该线，再按 $z^4$ 规范。

返回原 b=17：
$$
D_{j,17}(z)=\theta^{-4}D_{j,1}(\theta z),\qquad
\nu_{D_{j,1}}=\theta^4\nu_{D_{j,17}} .
\tag{24}
$$
最后一式用 $\Omega_{p,0}=\theta\Omega_p$，
保持同一个原 $\mathbf Z_p$ 测度变量和单位域。

## 5. 全权平方、范数和固定代数常数

令 $d_{j,m}=[z^m]D_{j,1}$，
$h_\infty=\sqrt{51\sqrt3}/(204\pi i)$。
原 Hermite 生成函数给
$$
b_{j,m}=m!s_j(\Omega_0h_\infty)^m d_{j,m}\in\mathbf R .
\tag{25}
$$
同一 Yang Theorem1.11 的 $S_1=\{2,17\}$、
$c(0)=17/27$、体积比6和完整范数给
$$
\mathcal N_{j,m}
=\frac{3(3-\sqrt3)n_j}{\sqrt{102\sqrt3}}
                    \frac{m!}{(4\pi)^m},
\qquad
C_j=\frac{\pi\sqrt{102\sqrt3}}
          {17\sqrt3(3-\sqrt3)n_j},
$$
$$
\boxed{L(\eta_j\psi_0^{2m+1},m+1)
       =C_j\frac{(4\pi)^m}{m!}\,b_{j,m}^2.}
\tag{26}
$$
上述常数沿 R735 原 Haar 规范；(15) 改变的是所选标签，
不是允许把 $n_j$ 或坏位体积省掉。

$m\equiv4$ 为偶数，$s_j$ 为实。
置 $\varkappa_j=C_js_j^2/\Omega_0>0$。
由 $4\pi h_\infty^2=-\sqrt3/(204\pi)$ 和
$s_0^{-2m}=3^m\omega$，准确得到
$$
c_j=\frac{\omega\varkappa_j}{s_0}
=34^4\frac{(2\pi/\sqrt3)^4L(\eta_j\psi_0^9,5)}
                   {4!\varpi_0^9}\in\overline{\mathbf Q}^{\times},
\tag{27}
$$
以及全部合法正权的同一个公式
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\eta_j\psi_0^{2m+1},m+1)}
     {m!\varpi_0^{2m+1}}
=c_j\,34^{-m}d_{j,m}^2.}
\tag{28}
$$
非零 $c_j$ 来自已证 $d_{j,4}=1$ 和 (26)；
代数性用原 CM 临界周期。
$c_j$ 是固定代数常数，不随 p、N 或原 q 变化。
若要求它在研究素数为单位，删其固定有限支撑即可。

## 6. 同一 ordinary 单位域上的负二 Katz 值

记
$$
M_{j,m}=\Omega_{p,0}^m m!d_{j,m},\qquad
\nu_{j,m}=\eta_j\psi_0^{m+1}\bar\psi_0^{-m},\qquad
\nu_{j,m}\nu_{j,m}^c=\mathrm N .
\tag{29}
$$
设 $\alpha=\psi_0(\mathfrak p)=\pi_0$、
$\bar\alpha=\psi_0(\bar{\mathfrak p})=\bar\pi_0$，
$v_p(\alpha)=1$。由 (28) 的原 primitive Katz 插值，
$$
\boxed{
\mathcal K^{\rm prim}_{34\delta}(\widehat\nu_{j,m})
 =c_j\Omega_{p,0}\,34^{-m}
   \left(1-\epsilon_j
               \frac{\alpha^m}{\bar\alpha^{m+1}}\right)^2M_{j,m}^2,
\quad \epsilon_j=\eta_j(\mathfrak p).
}
\tag{30}
$$
两个 ordinary 因子相同，是由 (10) 而非样本得到；
2、3、17均真正分歧，未添加或删除 primitive 坏 Euler 因子。

旧射线 $\pi_0\equiv1\bmod2,\ \pi_0\equiv\delta\bmod17$ 给
$$
\boxed{\epsilon_j=-1\quad(j\in\mathcal J).}
\tag{31}
$$
这与 R798/R801 型四来源的深核 $\lambda[\kappa]_*$ 完全一致；
其正权单位矩因子是 $1-\lambda\kappa^m$。
也可不预用核心符号：全 p-trace 保存 (5) 的每个 CM13 单重线，
其整标量由首阶4矩和 (30) 的密集正权单位平方唯一确定，
正如 R540§7.1 的完整 Euler 定标。

定义本篇三个实际裸负二矩
$$
I_{j,-2,p}=\int_{\mathbf Z_p^\times}
                      x^{-2}\,d\nu_{D_{j,17}}(x).
\tag{32}
$$
取 $m_r=-2+(p-1)p^r$。它们为合法正权且趋于原负二点；
非单位高矩趋零，单位测试一致趋于 $x^{-2}$。
周期变指数已经包含在实际测度矩中，
没有对任意 $\mathbf C_p$ 单位定义未付的复幂。
(30) 的 ordinary 因子在这一高正权极限中趋1。
因此准确有
$$
\boxed{
\nu_{j,-2}=\eta_j\psi_0^{-1}\bar\psi_0^2,\qquad
\mathcal K^{\rm prim}_{34\delta}(\widehat\nu_{j,-2})
=34^2c_j\theta^9\Omega_p\,I_{j,-2,p}^{\,2}.
}
\tag{33}
$$
$\theta^9$ 是 (24) 的 $\theta^8$ 与
$\Omega_{p,0}=\theta\Omega_p$ 的乘积。
没有把 (32) 的 Y-unit 换成另一个输入的单位域。

式(33)保留原双向非零判据，但不自行证明任一侧非零。

## 7. 负二的复临界点、完整 root 和没有强制零的 Katz 符号

令
$$
\nu_j=\nu_{j,-2}
=\eta_j\bar\psi_0^3\mathrm N^{-1},\qquad
\Theta_j=\eta_j^{-1}\psi_0^3 .
$$
所选 Katz 实际插值约定比较的是 $L(\nu^{-1},0)$，故
$$
\boxed{L(\nu_j^{-1},0)=L(\Theta_j,2).}
\tag{34}
$$
$\Theta_j$ 是权四 CM modular form 的 type-$(3,0)$ Hecke 角色，
导子仍为 $(34\delta)$，level为10404。
2是其中心且是 Deligne 临界点，不是绝对收敛区。

其 unitary 坏位表为
$$
\begin{array}{c|c|c}
2&\operatorname{Teich}_{\mu_3}&-1\\
3&u\bmod\delta&+i\\
17&\vartheta_{-l_j}&-1 .
\end{array}
$$
三处 $+i$ 是基 $\psi_0^3$ 的 $-i$ 乘 $\eta_j^{-1}(\delta)=-1$。
由 (15) 及原2/3 Gauss 规范，全部 epsilon 为
$$
\epsilon_{2,3,17,\infty}(\Theta_j)
=(+1,-i,+1,i^3)=(+1,-i,+1,-i).
$$
于是
$$
\boxed{W(\Theta_j)=-1,\qquad L(\Theta_j,2)=0.}
\tag{35}
$$
正支(17)与(35)并不冲突：
$\eta_j\psi_0^{-3}$ 与 $\eta_j\psi_0^9$ 的有限数据相同，
无穷绝对角却为3与9，epsilon 的比是 $i^6=-1$。
不能只代 $m\bmod6$ 而忽略正负 Hermite 方向。

还要区分反射复零和 Katz 的自对偶符号。
de Shalit II.6.4(9)–(10)、II.6.5(18) 使用
$\varepsilon=\nu^{-1}$，其对偶为
$\widetilde\varepsilon=(\varepsilon^c)^{-1}\mathrm N^{-1}$。
对本篇 $\widetilde\varepsilon=\varepsilon$。
原完整 multiplier 为
$$
W_{\rm pad}(\varepsilon)\varepsilon(\sigma_{-1}),\qquad
W_{\rm pad}(\varepsilon)
=-i\prod_{v\nmid p,\infty}W_v(\varepsilon).
\tag{36}
$$
本篇 $\varepsilon$ 型为 $(1,-2)$，在 p 未分歧，
故其所选 LT 的 $-1$ 值为 $(-1)^1=-1$。
(35) 的有限 epsilon 乘积为 $-i$，所以
$$
\boxed{
W_{\rm pad}(\varepsilon)=-1,\qquad
W_{\rm pad}(\varepsilon)\varepsilon(\sigma_{-1})=+1 .
}
\tag{37}
$$
(36)适用的 away-p 模数恰为本篇真正分歧的 $34\delta$；
所有 ordinary Euler 因子非零，改写为 (30) 的 primitive 规范不改变这个符号。
因此 **(33) 不被函数方程符号强制为零**。
这不是值非零定理，也没有声称任意 Teich 分支非恒等零可由首权4免费推出。

若用同一未分歧自对偶一般式，
$\varepsilon$ 型为 $(k,-k-1)$ 时，
(36)是 $W(\varepsilon)$（$k<0$）或 $-W(\varepsilon)$（$k\ge0$）。
正权(29)的逆型为 $(-m-1,m)$，
故(17)给其 multiplier同为 $+1$。
本篇负点属于后一种情形；不能搬用另一个 root-positive
权一曲线的共轭支整零结论。

准确的区域表为：

| 原输入 | type | 所选 $\mathfrak p$ 的经典 Katz 插值 | 真实复值及符号 |
| --- | --- | --- | --- |
| $\nu_{j,m}$，$m\ge0,\ m\equiv4\bmod6$ | $(m+1,-m)$ | 是 | (28)，root $+1$ |
| $\nu_j$ | $(-1,2)$ | 否；另一 Deligne 临界锥 | (34)，root $-1$；Katz multiplier $+1$ |
| $\nu_j^c$ | $(2,-1)$ | 是 | 同一 $L(\Theta_j,2)=0$ |

裸共轭交换普通 CM type，不能由最后一行给第二行赋零。
同 CM-type involution $\nu\mapsto\mathrm N(\nu^c)^{-1}$
则固定第二行，不把它送到第三行。

## 8. 当前精确的局部表示接口和未付非消失

负点的对偶表示准确为
$$
V_j=\overline{\mathbf Q}_p(1)\widehat\nu_j^{-1}
=\eta_j^{-1}\widehat\psi_0^{\,2}
                    \widehat{\bar\psi}_0^{-1}.
\tag{38}
$$
在原 $\mathfrak p$ 上，
$$
V_j=\overline{\mathbf Q}_p(2)
              \otimes(\eta_j^{-1}\bar\psi_0^{-3}),\qquad
\varphi_{\rm cris}=q_j=-\bar\pi_0/\pi_0^2 .
$$
原 rank-one epsilon 下降的另一个 Euler 值是
$a_j=-\pi_0/\bar\pi_0^2$，所以准确有
$$
\frac{1-a_j}{1-q_j}
=\frac{1+\pi_0/\bar\pi_0^2}{1+\bar\pi_0/\pi_0^2}
=p^2\frac{1+p/\bar\pi_0^3}{p^2+\bar\pi_0^3}
\in p^2\mathcal O_p^\times .
\tag{39}
$$
两个位置都是同一 $\mathfrak p$，分母不是一个换位后的 Euler 因子。
这排除了该局部比较中“分母恰零”的例外。

(38)的 Hodge 型差为3；
它不是椭圆曲线差一表示作共同 Tate twist。
因此 R735/R748 的一次 elliptic logarithm/point-factor AST
不能直接用于 (33)。
若要接真实全局类，应在模 $34\delta$ 的椭圆单位塔上
取本篇十八阶有限标签，再作 (38) 的实际 Soulé 特殊化。
辅助 $(5)$ 的平滑值确为
$25-\nu_j((5))=25-(-5)=30$。
但其 finite unramified Artin de Rham period、Coleman 符号与
完整局部化必须一并付清，不能只把局部对数的逆像命名为全局类。

现有文献的范围也准确保留：
Agboola 2026 的 $\phi_1^*$ 正是未加本篇有限扭曲的 $(-1,2)$ 型，
其精确阶数/leading 公式保 restricted-regulator 假设，
另一个 rank-zero 特例保相反经典 Katz 值非零的前提。
这里相反经典值由(35)为零。
Sano–Venjakob 2610.36607 Theorem2.4.1 给此型的本地 Soulé-log
框架；其 Corollary2.4.7 要求两指数均非正，不包括 $(-1,2)$。
其指定 p-primary equivariant 版也不能无证替代 (9) 的17分歧。
本篇不据这些范围说明给 (33) 追加非零结论。

## 9. 回到原指定二阶行及所有外部

沿 R801 写原同一个来源
$$
G_{2,N}=\sum_{j\in\mathcal J}\alpha_{j,N}D_{j,17}.
\tag{40}
$$
$\alpha_{j,N}$ 是真实代数系数，来自 R734 的同一
$\lambda,\kappa,\kappa^N$ 测试及固定谱投影。
在 R801 已付密度一子集上，$G_{2,N}$ 非零且定义于 K。
由 (2) 的不可约性，全部 $\alpha_{j,N}\ne0$；
不能从这个事实给任一 $I_{j,-2,p}$ 或其和赋非零。

完整原负二值成为
$$
\boxed{
\mathcal I_{2,N}
=\int_{\substack{E\in p^N\\Y\ {\rm unit}}}
 Z^2Y^{-2}q_N^*\,dB_0
=\lambda^{2N}\Omega_p^2
       \sum_{j\in\mathcal J}\alpha_{j,N}I_{j,-2,p}.
}
\tag{41}
$$
(33)识别各项的**平方**，不把(41)改成 Katz 值的线性和，
也不选择互不相干的平方根去生成线性独立。

R801 的同一个完整 Mellin 仍满足
$$
\mathscr X_{N,r}(w)+\lambda^rG_N(\kappa^r,w)
=\lambda^{2N}\frac{6\delta}{c_B}J_T(w)\qquad(r\ge2\text{ 偶}),
\tag{42}
$$
其内项起于
$$
\partial_wG_N(z,0)
=-\frac{d_pz^2}{2b_Y^2}\mathcal I_{2,N}
+d_p\sum_{h\ge3}\frac{(-1)^{h+1}z^h}{hb_Y^h}
 \int_{\substack{E\in p^N\\Y\ {\rm unit}}}Z^hY^{-h}q_N^*\,dB_0 .
\tag{43}
$$
所有 higher h、J深浅及真实 W-unit 失败域保持。
即使后续证明(41)非零，原强中央条件仍只使(42)的两导数相反；
还需一条已付的独立原算术关系才能消去外部。

## 10. 依赖、文献与执行范围

本篇没有新数值运行。完整算子用 R798 的特征零全 CM13/halfperiod，
实际原 $G_{2,N}$ 用 R801 的公开返回；本篇的新有限角色、
Gauss 和、绝对规范、正/负 root 和 period 均在上文逐式证明。
不以辅助模1009结果识别 Hecke 角色。

- [R735](R735-two-type-five-schwartz-and-rank-one-negative-moments.md)：原2/3/17模型、Yang Haar/Hermite及 Katz 周期。
- [R761](R761-primitive-type-five-ninth-order-characters-and-point-fields.md)：完整17环面、quadratic splitting及有限角色域；本篇保不同的偶标签。
- [R798](R798-original-halfperiod-two-types-and-e-depth-second-source.md)：原 canonical H 与完整两型压缩。
- [R801](R801-original-nonzero-second-e-source-and-complete-negative-two-row.md)：同 q 的实际二阶系数、全部密度量词、正矩及外部。
- [R332](R332-fixed-negative-original-moments-actual-soule-classes-and-reflected-root-signs.md)、[R540](R540-original-degree-six-schwartz-full-weight-and-negative-two-katz.md)：原 negative-weight/local-Euler 范围；不同有限角色没有相认。
- T. Yang, *Theta liftings and Hecke L-functions*, J. reine angew. Math.485 (1997), Theorem1.11及原 local dichotomy：
  <https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>。
- M. Bertolini–H. Darmon–K. Prasanna, *p-adic Rankin L-series and rational points on CM elliptic curves*, Pacific J. Math.260 (2012), §3A、Theorem3.1、Proposition3.5：
  <https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP2.pdf>。
- E. de Shalit, *Iwasawa Theory of Elliptic Curves with Complex Multiplication*, 1987，
  II.6.4(9)–(10)、II.6.5(18)，书页93–95：
  <https://djvu.online/file/gQB4wIcHwcVza>。
- A. Agboola, *On values of the Katz two-variable p-adic L-function*, 2026，
  TheoremA/6.3、TheoremD/11.1的准确假设：
  <https://link.springer.com/article/10.1007/s40316-026-00273-2>。
- T. Sano–O. Venjakob, *On extended interpolation properties of the Katz p-adic L-function*, arXiv:2610.36607v1，Theorem2.4.1、Corollary2.4.7、§3.6：
  <https://arxiv.org/pdf/2610.36607>。
