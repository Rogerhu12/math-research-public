# R761 — 原型五 primitive 三条来源的完整九阶角色、quadratic17 扭曲与点域

日期：2026-11-15。**状态：已证明。** 本篇识别 R732 型五空间中整个 $T^3+\omega$ 块的实际有限 Schwartz 和全局 Hecke 角色，支付原负一 Mellin 的完整 Katz 平方及其真实点特征空间。三条来源共享一个在2处惯性阶3、17处惯性阶9的固定 cyclic9 点域；它们不属于两条已付有理 rank-one 曲线的 cubic 点空间。

本篇不预设这三条权二角色的解析秩恰为一，不以非零 theta 截面推出负一矩非零。点公式包括零值。原 $J'_S,J'_T,J'_{136}$ 没有增加任何新的零条件。

## 1. 原整个型五块及准确角标签

使用 R290、R735、R751、R757 的原加性角色、极化和 sigma 规范：
$$
K=\mathbf Q(\omega),\quad \delta=1+2\omega,\quad
\zeta_{18}=e^{\pi i/9},\quad
g_0=2+4\delta\in\mathbf F_{289}^{\,1},\quad
g_0^6=\omega .
\tag{1}
$$
$\psi_0$ 是 $E_0:y^2=x^3+1$ 的原 type-$(1,0)$ Hecke 角色。
以下 $E_0$ 始终指这个共同基曲线。

令 $\tau_j(g_0)=\zeta_{18}^j$。原十七维有限 Weil 模中，除二次标签 $j=9$ 外，其余角色各单重。dyadic 向量为
$$
v_\pm=(1,t_\pm,-1,t_\pm),\qquad
t_\pm=\frac{1\pm\sqrt3}{\sqrt2}.
\tag{2}
$$
两向量都偶；原几何 $\omega$ 作用在 $v_+,v_-$ 上的特征分别是 $1,\omega^2$，十七处是 $\tau_j(g_0^{12})$。

型五要求奇以及 $\omega$ 特征 $\omega^2$。所以其完整有限分解是
$$
\boxed{
(v_-,j=3,15)\ \oplus\ (v_+,j=1,7,13).
}
\tag{3}
$$
第一对正是 R735 的 $D_{2,b}=D_{\omega,b}$、$D_{4,b}=D_{-,b}$。第二组三条就是本篇对象。标签 $j=9$ 不在有限 Weil 模中，未被遗漏。

记
$$
\mathcal J=\{1,7,13\},\qquad l_j=j-9\in\{-8,-2,4\}.
\tag{4}
$$
在 $\mathbf F_{289}^{\times}$ 上令 $\vartheta_l(u)$ 为 $u^{16l}$ 的 $\mu_{18}$ 提升。对 (4)，其阶准确为9，且
$$
\vartheta_l|_{\mathbf F_{17}^{\times}}=1,\qquad
\vartheta_l(\delta)=1,\qquad
\vartheta_l(\omega)=\omega.
\tag{5}
$$

## 2. 真正有限角色，不以 CM13 样本认角色

定义有限 Hecke 角色 $\eta_j$ 的完整分歧单位表为
$$
\boxed{
\eta_{j,2}(u)=\operatorname{Teich}_{\mu_3}(u\bmod2)^{-1},
\qquad
\eta_{j,17}(u)=\vartheta_{l_j}(u\bmod17).
}
\tag{6}
$$
其余有限处分量不分歧；在2、17及 $\delta$ 上的 uniformizer 值均为1。

给出全局定义及其相容性。对素于34的主理想 $(a)$，置
$$
\eta_j((a))
 =\left(
 \operatorname{Teich}_{\mu_3}(a\bmod2)^{-1}
 \vartheta_{l_j}(a\bmod17)
 \right)^{-1}.
\tag{7}
$$
在 $\omega$ 上括号为 $\omega^2\omega=1$，在 $-1$ 上也为1。
$h_K=1$ 因而使 (7) 与生成元无关，定义全局角色。主有理 idèle 2、17及主 idèle $\delta$，结合 (5)，分别给出上述三个 uniformizer 值；没有把“不分歧”误作任意统一取1。

角色在有理 idèle 上平凡，且
$$
\eta_j^c=\eta_j^{-1},\qquad
\operatorname{ord}\eta_j=9,\qquad
\mathfrak f_{\eta_j}=(34).
\tag{8}
$$
在17处已读到全部九阶值，故阶数不是一个上界。

定义真实 type-$(1,0)$ 角色
$$
\boxed{\Psi_j=\psi_0\eta_j^{-1}.}
\tag{9}
$$
其 unitary 部分的全坏处表为
$$
\begin{array}{c|c|c}
v&\text{单位上的值}&\text{指定 uniformizer 值}\\ \hline
2&\operatorname{Teich}_{\mu_3}^{-1}&-1\text{ 于 }2\\
3&u\bmod\delta\in\{\pm1\}&+i\text{ 于 }\delta\\
17&\vartheta_{-l_j}&-1\text{ 于 }17 .
\end{array}
\tag{10}
$$
它满足
$$
\Psi_j\Psi_j^c=\mathrm N,\qquad
\mathfrak f_{\Psi_j}=(34\delta),\qquad
\mathrm N\mathfrak f_{\Psi_j}=3468 .
\tag{11}
$$
dyadic、三处和17处角色都真正分歧，未删掉任何 primitive Euler 因子。

### 2.1 与 R757 的真实 quadratic17 关系

令 $\Psi^{(0)}_a$ 为 R757 的 type0 primitive 角色，$a\in\{2,8,14\}$；
令
$$
\kappa_{17}=\psi_3/\psi_0,
$$
其中 $\psi_3$ 是 $E_{17^3}$ 的原角色。
这是完整 quadratic17 扭曲：二处平凡，三处不分歧且在 $\delta$ 上为 $-1$，十七处单位为 $u^{144}$、uniformizer 为1。

置 $a=9-j\bmod18$。逐项比较 (10) 与 R757 的全坏处表，得到
$$
\boxed{
\Psi_1=\kappa_{17}\Psi^{(0)}_8,\qquad
\Psi_7=\kappa_{17}\Psi^{(0)}_2,\qquad
\Psi_{13}=\kappa_{17}\Psi^{(0)}_{14}.
}
\tag{12}
$$
在17处这是指数恒等式
$(a-9)+9=-l_j\bmod18$；
三处则准确将 $-i$ 改为 $+i$。所有其他局部分量也相同，所以 (12) 是全局角色身份，不只 CM13 特征相同。

R757 的三个非零中心值因此不能直接搬到本篇：它们发生了真实的二次扭曲。

### 2.2 root number、系数域及实际动机大小

(10) 的十七处 Gauss 和为 $+17$。确实，对非平凡且在 $\mathbf F_{17}^{\times}$ 上平凡的 $\vartheta_{\pm l}$，$x=0$ 的 $x+y\delta$ 纤维和为16，每个 $x\ne0$ 的纤维和为 $-1$。原加性和正是17。乘原 uniformizer 的 $-1$ 后 epsilon 因子为 $-1$。

二处逆三次角色的原 Gauss 和为2；三处及无穷处按同一 R735 规范。完整四处 epsilon 因子为
$$
(+1,-i,-1,i),
$$
故
$$
\boxed{w(\Psi_j)=-1.}
\tag{13}
$$
它迫使 $L(\Psi_j,1)=0$，没有证明 $L'(\Psi_j,1)\ne0$。

实际值域为
$$
E=K(\zeta_9)=\mathbf Q(\zeta_9).
\tag{14}
$$
全角色值包含 K，而 (7) 的 CRT 读取给出全部 $\mu_9$，故这是等号。
三条是 $\operatorname{Gal}(E/K)$ 的一个完整轨道。

其权二自守诱导的 level 是10404、有限中心角色平凡，系数域准确为
$$
E^+=\mathbf Q(\zeta_9+\zeta_9^{-1}),
\tag{15}
$$
即实三次域。为核“准确”，也可由 (12) 使用 R757 的三个不同 $a_{13}$：$\kappa_{17}(13)=1$，所以这三个实共轭仍不同。其不同性最终来自 $\gamma/\bar\gamma$ 不是单位根，$\gamma=4+\omega$。因此这是同一三次系数域 CM 自守轨道，不能改称三条 $E/\mathbf Q$。

## 3. 完整 Schwartz、标准下降与绝对 CM13 特征

沿用原十七维算子 W，置
$$
\Pi_j=\frac1{18}\sum_{a=0}^{17}\tau_j(g_0)^{-a}W(g_0^a).
\tag{16}
$$
它秩1。选择最小的 $a_j\in\{0,\ldots,16\}$ 使
$\Pi_je_{a_j}\ne0$，令 $f_j=\Pi_je_{a_j}$，并保真实范数
$$
n_j=\sum_{a=0}^{16}|f_j(a)|^2>0.
\tag{17}
$$
这给固定、可重算的非零有限向量，不依赖目标 p。
$\overline{W(g)}=W(g^{-1})$ 及 $j$ 为奇数说明 $f_j$ 实且奇。

实际全有限 tensor 取
$$
\phi_{2,j}=f_A+t_+f_B,\qquad
\phi_{3,j}=\mathbf1_{3^{-1}\mathbf Z_3},\qquad
\phi_{17,j}=\sum_a f_j(a)\mathbf1_{a/17+\mathbf Z_{17}},
\tag{18}
$$
其余处为原球。范数为
$$
\|\phi_{2,j}\|^2=3+\sqrt3,\qquad
\|\phi_{3,j}\|^2=3,\qquad
\|\phi_{17,j}\|^2=n_j .
\tag{19}
$$

这对应的正权角色是
$$
\boxed{\Phi_{j,m}=\eta_j\psi_0^{\,2m+1},\qquad m\equiv5\bmod6.}
\tag{20}
$$
其全坏处表是
$$
\begin{array}{c|c|c}
2&\operatorname{Teich}_{\mu_3}&-1\\
3&u\bmod\delta&-i\\
17&\vartheta_{l_j}&-1 .
\end{array}
\tag{21}
$$
二处正是原 splitting 的 $v_+$，完整 $\mu_3,-1,g_*$ 生成元全部固定该向量。三处与 R735 相同。
Hilbert90 写 $g=u/\bar u=u^{-16}$，17角色变成 $g^{-l_j}$；加上真实 quadratic splitting，Weil 向量标签为
$g^{9+l_j}=g^j$。这核的是整个有限环面。

原 Yang dichotomy 在 $2,3,17,\infty$ 为
$(+1,-1,-1,+1)$。因此 Hermitian 类及 Gaussian 仍为
$$
\alpha=17,\qquad\mathcal G=51\sqrt3.
\tag{22}
$$
没有由 degree34 反猜这个类。

原序列为
$$
a_{j,n}=v_+(n\bmod4)f_j(3n\bmod17).
\tag{23}
$$
它非零、实、奇，满足
$(-1)^na_{j,n+34}=-a_{j,n}$。
故原半周期计算将它下降到同一个标准 degree34 线丛，没有新增二挠 twist。
其几何 $\omega$ 特征为
$1\cdot\tau_j(g_0^{12})=\omega^2$，所以型恰为5。

在原实周期 $\Omega_0\Lambda$，$\Lambda=\mathbf Z+s_0\mathbf Z$、
$s_0=(1-\omega)^{-1}$ 上，令其 theta 为 $S_{j,\Lambda}$。
以首个非零 Taylor 系数确定代数截面 $D_{j,1}$：
$$
S_{j,\Lambda}(Z)=s_jD_{j,1}(\Omega_0Z),\qquad
[z^{r_j}]D_{j,1}=1,\qquad s_j\in i\mathbf R^\times .
\tag{24}
$$
它可直接由同一代数 theta 群的 (16)、(18) 投影定义。
$$
D_{j,1}\in-\sigma^{34}xy\,E[X]_{\le4},\qquad
r_j\in\{5,11,17,23,29\}.
\tag{25}
$$
没有猜测 $r_j=5$。实性及代数 CM 投影表明其系数在 $E^+$；由于原 CM13 特征不在 K，系数不可能全在 $\mathbf Q$，故其系数域也是 (15)。

保原全 Heisenberg 公共标量 $-\omega^2$，CM13 的 dyadic 标签为 $\omega^2$、17标签为 $g_0^{14}$。因此
$$
\boxed{
N_{13}D_{1,1}=\zeta_{18}^{17}D_{1,1},\quad
N_{13}D_{7,1}=\zeta_{18}^{11}D_{7,1},\quad
N_{13}D_{13,1}=\zeta_{18}^{5}D_{13,1}.
}
\tag{26}
$$
这些正是 $T^3+\omega$ 的三根。三条非零有限线因此穷尽 R732 的整个 primitive 块。
CM13 只在已经确定的全角色中识别来源，没有用 (26) 猜测 (6) 或 (10)。

最后回到原 $b=17$ 框，置 $\theta=17^{1/6}$：
$$
D_{j,17}(z)=\theta^{-r_j}D_{j,1}(\theta z),\qquad
\Omega_{p,0}=\theta\Omega_p,\qquad
\nu_{D_{j,1}}=\theta^{r_j}\nu_{D_{j,17}} .
\tag{27}
$$
最后一个式子在同一个原 $\mathbf Z_p$ 测度变量上成立。

## 4. 全权平方与固定代数常数

采用原 Hermite 生成函数
$\exp(xT-T^2/(8\pi))=\sum H_m(x)T^m/m!$，令
$$
h_\infty=\frac{\sqrt{51\sqrt3}}{204\pi i},\qquad
d_{j,m}=[z^m]D_{j,1}.
$$
原 Hermite 和满足
$$
b_{j,m}=m!s_j(\Omega_0h_\infty)^m d_{j,m}.
\tag{28}
$$
原完整有限范数给
$$
C_j=\frac{\pi\sqrt{102\sqrt3}}
          {17\sqrt3(3+\sqrt3)n_j},\qquad
L(\Phi_{j,m},m+1)
 =C_j\frac{(4\pi)^m}{m!}b_{j,m}^2 .
\tag{29}
$$
没有约去 (19) 或把 $s_j$ 设为1。

令 $\varpi_0=s_0\Omega_0$、
$\varkappa_j=-C_js_j^2/\Omega_0>0$，并定义
$$
c_j=-\frac{\omega^2\varkappa_j}{s_0}
 =34^{r_j}\,
 \frac{(2\pi/\sqrt3)^{r_j}L(\Phi_{j,r_j},r_j+1)}
      {r_j!\varpi_0^{\,2r_j+1}}
 \in\overline{\mathbf Q}^{\times}.
\tag{30}
$$
非零性由 (24)、(28)、(29) 支付，代数性按同一 CM 临界周期规范。由
$s_0^{-2m}=-\omega^2 3^m$，全部合法正权准确满足
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\eta_j\psi_0^{\,2m+1},m+1)}
 {m!\varpi_0^{\,2m+1}}
 =c_j\,34^{-m}d_{j,m}^2 .
}
\tag{31}
$$

必须保固定有限扭曲：
$$
\Phi_{j,m}=\Psi_j^{\,2m+1}\eta_j^{\,2m+2}.
\tag{32}
$$
在 $m\equiv5\bmod6$ 中，只有 $m\equiv17\bmod18$ 才可把最后因子删掉。
把整个 (31) 误写成 $\Psi_j^{2m+1}$ 会改变原17处角色。

## 5. 普通 Euler、原负一 Katz 值与 finite-character 版本

置
$$
\nu_{j,m}=\eta_j\psi_0^{\,m+1}\bar\psi_0^{-m}.
\tag{33}
$$
设 $\alpha=\psi_0(\mathfrak p)$、$\bar\alpha=\psi_0(\bar{\mathfrak p})$，
$v_p(\alpha)=1$、$v_p(\bar\alpha)=0$，并令
$\epsilon_j=\eta_j(\mathfrak p)$。
由 (31)，primitive Katz 插值为
$$
\boxed{
\mathcal K_{34\delta}(\widehat\nu_{j,m})
 =c_j\Omega_{p,0}34^{-m}
 \left(1-\epsilon_j\frac{\alpha^m}{\bar\alpha^{m+1}}\right)^2
 M_{j,m}^2,
\quad
M_{j,m}=\Omega_{p,0}^m m!d_{j,m}.
}
\tag{34}
$$
两个普通 Euler 因子相同，是由 $\eta_j^c=\eta_j^{-1}$ 的完整角色等式得出。

在原射线上 $\pi_0\equiv1\bmod2$、$\pi_0\equiv\delta\bmod17$，所以 (5)–(7) 给 $\epsilon_j=1$。这只用于本射线上的 ordinary core，不把三条全局角色相认。
全部三来源都属于原 odd S34，故其实际 core 是 R728 的 $\beta=-\lambda$。

取高正权 $m_r=-1+(p-1)p^r$；用 bounded-measure 与完整 Euler 极限，(34) 给
$$
\boxed{
\mathcal K_{34\delta}(\eta_j\widehat{\bar\psi}_0)
 =34c_j\theta^{2r_j+1}\Omega_p I_{j,1}^{\,2},
\quad
I_{j,1}=\int_{\mathbf Z_p^\times}x^{-1}d\nu_{D_{j,17}}.
}
\tag{35}
$$
这正是 $\widehat{\bar\Psi}_j$ 的 Katz 值，不是原 type0 参考的中心值。

更一般地，令
$$
I_{j,\chi}=\int_{\mathbf Z_p^\times}x^{-1}\chi(x)d\nu_{D_{j,17}}.
$$
型五迫使它在 $\chi|_{\mu_6}\ne1$ 时为零。其余有限角色定义
$$
\Gamma_0=\widehat\psi_0/\widehat{\bar\psi}_0,\qquad
\rho_\chi=\chi\circ\Gamma_0,\qquad
\rho_{j,\chi}=\eta_j\rho_\chi.
\tag{36}
$$
$\rho_\chi$ 只在 $p$ 处分歧，包含全部 tame/wild 角色；其 $\mathfrak p$、$\bar{\mathfrak p}$ 单位值分别是 $\chi^{-1},\chi$。
在同一完整刚性权分支中延拓 (34)，得到
$$
\boxed{
\mathcal K_{34\delta}
 (\widehat{\bar\psi}_0\rho_{j,\chi})
 =34c_j\theta^{2r_j+1}\Omega_p\,
      \chi(34)^{-1} I_{j,\chi}^{\,2}.
}
\tag{37}
$$
正导子 $p$ 的分支按实际 ramified local factor 解释；不能在那里插入一个裸未分歧 Euler 因子。延拓用完整函数的唯一性，不把 wild 根单位说成整数幂的极限。

## 6. 固定 cyclic9 点域及真实 root-negative good pair

三角色满足
$$
\eta_7=\eta_1^7,\qquad \eta_{13}=\eta_1^4.
$$
故它们有相同核。置
$$
H=K^{\ker\eta_1}=K^{\ker\eta_j}.
\tag{38}
$$
准确地，
$$
\boxed{
[H:K]=9,\quad \operatorname{Gal}(H/K)\simeq C_9,\quad
e_2(H/K)=3,\quad e_{17}(H/K)=9,
}
\tag{39}
$$
且 H 在3与原 p 处分歧指数为1。惯性阶直接由 (6) 得出。
系数域 $E$ 与点坐标域 H 不混为一谈。

对有限 $\chi$，令
$$
H_{j,\chi}=K^{\ker\rho_{j,\chi}},\qquad
\nu=\psi_0\rho_{j,\chi}^{-1}.
\tag{40}
$$
它可能只是 $H K^{\ker\rho_\chi}$ 的一个子域，不无证认成两域的直积。
其2、17惯性仍为阶3、9；3处分歧指数仍为1；
p处保精确导子与字符 $\chi^{-1}$。
$\nu$ 自对偶、type $(1,0)$，三处导子恰一次；其全 root number 是 $-1$，因为新增 split-p epsilon 乘积为 $\chi(-1)=1$。

使用 R748 已支付的实际 good-pair 构造，取
$$
\psi_{\rm aux}\xi^{-1}=\nu,\qquad
L(\psi_{\rm aux}^*\xi^{-1},1)\ne0.
\tag{41}
$$
辅助 cyclic conductor 避开 $2,3,17,p$；所有目标有限分歧放入
$\xi=(\psi_{\rm aux}/\psi_0)\rho_{j,\chi}$。
这里允许 (6) 的原坏处角色，不能先以 only-p twist 的缩略表替换。

完整局部 toric pairing 保留，尤其 p 因子是
$$
Q_p=
 \frac{L(1/2,\pi_p\otimes\kappa_{\bar{\mathfrak p}})^2}
      {\varepsilon(1/2,\Psi_{p,\rm add},
                   \pi_p\otimes\kappa_{\bar{\mathfrak p}})}
 \,\alpha_{\kappa,p}(f_+,f_-),\qquad \kappa=\xi^{-1}.
\tag{42}
$$
取实际 algebraic good vectors 使完整局部乘积非零。
正导子时 (42) 保有限 Gauss 和；导子零时保 ordinary Euler。
二、三、十七处的 pairing 使用 (10)、(21)、(40) 的完整角色；它们的代数体积、角色值和 Gauss 因子均留在最终系数中。

R748 的 exact Rankin–Katz 比较使用同一代数微分、原 BDP 相位和全部 (42)，其两个 CM 点因子在同一系数嵌入中分别下降为
$$
\psi_{\rm aux}\xi^{-1}=\nu,\qquad
\frac{\mathrm N}{\psi_{\rm aux}^*}(\xi^*)=
\frac{\mathrm N}{\nu^*}=\nu.
\tag{43}
$$
因此它不是将两个不同的 $\rho$、$\rho^{-1}$ 点对数无证认作同一个。

若目标 Katz 值非零，该实际 toric logarithm 给非挠 Heegner 点；
Gross–Zagier 和 Kolyvagin–Logachev 才在此后给该 CM 分量的秩一，允许把实际乘积写成同分量的平方。
若目标值为零，取零点即可。
这一逻辑没有假设三条 $\Psi_j$ 本身或全部 finite twist 都解析秩一，也没有假设 Sha 有限。

准确的有限 twist 下降于是给
$$
P_{j,\chi}\in
 \bigl(E_0(H_{j,\chi})\otimes_{\mathbf Z}\mathbf Q\bigr)
       \otimes_K\overline{\mathbf Q},
\qquad
g_{\rm pt}P_{j,\chi}=\rho_{j,\chi}(g)P_{j,\chi},
\tag{44}
$$
及 $\varepsilon_{j,\chi,p}\in\overline{\mathbf Q}^{\times}$，满足
$$
\boxed{
\mathcal K_{34\delta}(\widehat{\bar\psi}_0\rho_{j,\chi})
 =\varepsilon_{j,\chi,p}\,
       \Omega_{p,0}^{-1}\log_{\omega_0}(P_{j,\chi})^2,
\qquad \omega_0=dx/(2y).
}
\tag{45}
$$
$\varepsilon_{j,\chi,p}$ 由上述 exact comparison、非零 companion、代数微分、有限 twist Gauss 和与全部 local Q 确定。它不是一个未经定值的 Iwasawa unit，也未被宣称为 p-adic 单位。
辅助点域经实际 CM twist isogeny 从点因子上消去，留下 (44) 的准确域；代数标量所在域可以更大。

结合 (27)、(37)、(45)，得到原共同周期下的公式
$$
\boxed{
\Omega_p I_{j,\chi}
 =A_{j,\chi,p}\log_{\omega_0}(P_{j,\chi}),\qquad
A_{j,\chi,p}^{\,2}
 =\frac{\varepsilon_{j,\chi,p}\chi(34)}
        {34c_j\theta^{2r_j+2}}
 \in\overline{\mathbf Q}^{\times}.
}
\tag{46}
$$
平方根的符号按实际相等选取；不声称各 $\chi$ 的符号已组成一个指定的线性 universal period map。零值同样满足 (44)–(46)。

## 7. 与原两条 cubic 点空间及 D_S 的准确关系

在一个包含所有有限点域的代数点张量空间中，只让 Galois 作用于点因子，保持所有代数系数不动。R749 的 analytic subgroup 引理给共同椭圆 logarithm 的单射；因此可以在这个有限 point-log 空间施加实际惯性幂等元。

在17处，(44) 的三个标签是三条不同的 exact-order9 角色；
R735 的 $D_2,D_4$ 回到共同 $E_0$ 后是两个 exact-order3 标签。
所以它们互不混合。不同 finite $\chi$ 又由原 p 处的 $\chi^{-1}$ 区分。
由此，所有这些家族中实际非零的负一值，在共同 $\Omega_p$ 规范下代数线性独立。这个结论不声称每个值都非零。

R759 的 $D_S$ 在 primitive 三维块上的投影非零。
因为 $D_S$ 定义于 K，且 $T^3+\omega$ 在 K 上不可约，
它在 (26) 的三条几何线上实际上都非零：若一条为零，整个 Galois 轨道都为零，与 R759 矛盾。
因此完整截面分解具有
$$
D_S=a_-D_-+a_\omega D_\omega+\sum_{j\in\mathcal J}a_jD_{j,17},
\qquad a_j\ne0\quad(j\in\mathcal J).
\tag{47}
$$
所有系数均代数，尺度按 (27) 保留。
$ a_-,a_\omega $ 的实际值可以由 R732 的完整矩阵读取，不能靠维数猜测。

将原同一负一泛函作用于 (47) 是合法的完整一变量来源分解。
若某个已知非零 $I_2/I_4$ 的实际系数也非零，(46) 与 point-factor 分离会排除其被 primitive 项抵消；若只知道 $a_j\ne0$，还不能推出对应 $I_{j,1}\ne0$。

本篇支付的是全 primitive 角色、真实 quadratic17 twist、所有 period/local Q 及准确点域。
原 CM 投影用于 mixed 门时仍须保 R759 的全部纤维与连接修正；本篇不从 (47) 或 (46) 生成原中央零，也不将有限 carrier 的 point-factor 投影延到无证明的无限 logarithm 极限。

## 依赖与执行范围

完整 finite Weil、半特征和 Hermite 规范见 R290、R735、R751；原 whole 型五 CM13 见 R732；type0 对照见 R757；实际连接来源见 R759。点域及 exact local comparison 使用 R748 的原 good-pair/LZZ 证明，有限 point-only 幂等元使用 R749。

本文一般证明不需要新的数值执行。独立 producer
[check-r761-original-s-connection-projections.py](../scripts/check-r761-original-s-connection-projections.py)
仅用于读取 (47) 的两已知线系数及实际 primitive 多项式，重算原 R732 全纤维，不读生成数据。其公开执行回执和任何由之付清的更强非零结论另行追加；不将未执行输出写成已证事实。


## 公开执行增补 A. 原 D_S 的准确分解及裸负一矩非零

本增补使用已完成的公开 Actions，未在其他环境重算矩阵。

- producer：scripts/check-r761-original-s-connection-projections.py，默认无参数；
- run：43717518190；job：132822145230；
- source head：923b266a8632fb8b580b8e20aba600a2341fec92；
- Python 依赖：python-flint==0.9.0；
- producer SHA256：1a8c665e6d24a43654b880d2fc030f4c987fee78895a9a8d27545780db4259dc；
- 原 R732 producer SHA256：d1b3c2f851e9ec6b6d6b6655141e36b4bb1108a30e57ff8365b5f583d880e469；
- stdout：753 字节，SHA256 为 7f1f5e5f5280c9dee60bd753280fc63081e36b8f95cc6329c113a137299fc969。

脚本从原 division 多项式重新计算全部十三纤维和完整矩阵，不读旧输出。它只计算截面，不数值计算 Mellin 或 logarithm。

### A.1 完整特征零分解，三个首阶都准确为五

原两个一次投影的系数准确为
$$
a_-=0,\qquad a_\omega=\frac{11}{21}.
\tag{A1}
$$
令
$$
\begin{aligned}
R_{S,b}=-\frac{\sigma^{34}xy}{357}
 \bigl(&107X^4+104bX^3-2328b^2X^2\\
       &-7456b^3X-2944b^4\bigr).
\end{aligned}
\tag{A2}
$$
则实际完整来源身份为
$$
\boxed{
D_S=\frac{11}{21}D_{\omega,b}+R_{S,b},\qquad
R_{S,b}=\Pi_{\rm prim}D_S,\qquad
[z^5]R_{S,b}=\frac{107}{357}.
}
\tag{A3}
$$
全部 b 幂由 R732 的固定六次缩放返回；(A2) 也可逐项代回 R759 的原五坐标核对。

这还确定了正文未猜测的首阶：
$$
\boxed{r_1=r_7=r_{13}=5.}
\tag{A4}
$$
证明如下。首 $z^5$ 系数是定义于 K 的线性行。若它在三条 primitive 特征线中的一条上为零，由完整 Galois 轨道，它在三条上都为零，于是杀整个 primitive 块。但 (A3) 给出该块上非零的实际值，矛盾。
因此三条首阶均为5；它们的正常化和 (27) 现在统一为
$D_{j,17}=\theta^{-5}D_{j,1}(\theta z)$。
正文 (35)、(37) 的周期因子均为 $34c_j\theta^{11}\Omega_p$，
(46) 的平方系数分母均为 $34c_j\theta^{12}$。

### A.2 同一 H 内的 cubic 子域与真正 dyadic 点投影

还可将正文第7节的分离放在同一个固定点域内。由完整局部表，
$$
\boxed{
\eta_1^3=\psi_0/\psi_2,\qquad
\eta_1^6=\psi_0/\psi_4 .
}
\tag{A5}
$$
例如 $\eta_1^3$ 在2处平凡，在17处是
$u^{-384}=u^{-96}$，在 $\delta$ 上为1，正是第一条比值；
第二式同样逐处成立。这里的 $\psi_2,\psi_4$ 指 R735 的两条曲线角色。

由原 CM 坐标扭曲，
$$
\boxed{
K(\sqrt[3]{17})=H^{I_2},
}
\tag{A6}
$$
其中 $I_2\subset\operatorname{Gal}(H/K)$ 是实际阶3惯性群。
确实该三次域对应 (A5) 的角色；H 是 cyclic9，因而其三次子域唯一。

在本附录只取裸 $\chi=1$。所有三 primitive 点张量和
R735 两个原点经 $\phi_2,\phi_4$ 返回后，都位于
$E_0(H)_{\mathbf Q}\otimes_K\overline{\mathbf Q}$。
代数标量、Gauss 因子和 $b=17$ 缩放均作为系数保持不动。
定义真正 point-factor 平均
$$
e_2=\frac13\sum_{g\in I_2}g_{\rm pt}.
\tag{A7}
$$
它杀三个 primitive $\eta_j$ sector，保持 (A5) 的两个 cubic sector。
借 R749 的对数单射，记其在这个有限 point-log 空间上的算子为
$e_2^{\log}$。它不是对任意 $\mathbf C_p$ 数值作连续 Galois 平均。

为避免与 R759 的带 $\Omega$ 记号混淆，置
$$
\mathfrak i_F=\int_{\mathbf Z_p^\times}Y^{-1}d\nu_F(Y),
\qquad \mathbb I_F=\Omega_p\mathfrak i_F .
\tag{A8}
$$
$\mathbb I_F$ 正是 R759 的 $I_F(1,0)$。
(A3)、(46)、(A7) 给出准确点空间等式
$$
\boxed{
e_2^{\log}\mathbb I_{D_S}
 =\frac{11}{21}\mathbb I_{D_\omega}\ne0.
}
\tag{A9}
$$
最后的非零是 R735 已付的原 $E_{289}$ rank-one logarithm。
由此得到新的原来源结论：
$$
\boxed{
\mathfrak i_{D_S}\ne0.
}
\tag{A10}
$$
三个未知 primitive 负一值即使不全非零，也不影响 (A9)；
它们不能抵消另一个真实惯性 sector 的非零分量。

### A.3 原 CM 连接修正的负一矩也非零

R759 的全来源式为
$$
\mathcal C_\gamma(S)
 =(\gamma^2+\bar\gamma M_\gamma)D_S.
$$
在 $D_\omega$ 上 $M_\gamma=-\gamma\omega^2$；primitive 块仍保持。
因此
$$
\boxed{
e_2^{\log}\mathbb I_{\mathcal C_\gamma(S)}
 =\frac{11}{21}(\gamma^2-13\omega^2)\mathbb I_{D_\omega}
 =\frac{44}{21}(7+5\omega)\mathbb I_{D_\omega}\ne0.
}
\tag{A11}
$$
特别
$$
\boxed{\mathfrak i_{\mathcal C_\gamma(S)}\ne0.}
\tag{A12}
$$
这里没有把 CM 算子穿过一个未经运输的单位门；先用已付的完整 theta 来源分解，再作用原同一个 unit 泛函。

### A.4 原中央补偿保留在导数层

(A10)、(A12) 是零权的**负一**值。它们不将 R759 的 Mellin 导数赋零。
原准确关系仍为
$$
I_{\mathcal C_\gamma(S)}'(1,0)
 -\bar\gamma I_{M_\gamma D_S}'(1,0)
 -\gamma^2 I_{G_S}'(1,0)
 =-\frac{\gamma^2}{34}J_S'(1,0).
\tag{A13}
$$
所以即使原 $J_S'(1,0)=0$，也只有 (A13) 的完整导数相消。
不能把 (A7) 的有限 point-factor 操作无证延拓到这些带
$\log\langle Y\rangle$ 的无限权变化，也不能把 (A10) 改称原中央非零。
