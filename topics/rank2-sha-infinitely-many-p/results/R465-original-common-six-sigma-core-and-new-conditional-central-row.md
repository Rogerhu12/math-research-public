# R465 — 原共同六 sigma 的真实 T 核、新谱线及完整五伴随中央行

日期：2026-11-14。**状态：已证明。** 本篇在原六个独立 sigma 输入中，
保留全部伴随，施加原 $T$ 输出的真实 core。原第一态的完整投影为零；
第二态的同一固定投影准确为 $S_{\mathrm{new}}\otimes\Lambda$，
其中 $\Lambda$ 的质量为 $52/3$，在当前普通素数类上是单位。
因此第三条真实曲线的中央零给任意五伴随测试的条件中央零。
这里没有把新行解释成整个第二态的中央零，也没有把混合第一输出的
$T$ 管穿过 CM 投影。主目标尚未完成。

## 1. 同一个原六 sigma 联合

使用 R398、R414、R457 的同一 $E_b$ 模型、reduced sigma、微分和
普通周期，$\delta^2=-3$、$\omega=(-1+\delta)/2$、
$\gamma=(5+\delta)/2$。置
$$
\mathcal C(z)=
\sigma(\delta z)\sigma(2\delta z)
\sigma(\gamma z)\sigma(\bar\gamma z)\in\mathcal S_{29}.
\tag{1}
$$
它保原奇 degree 的半特征；函数本身为偶函数。

令六个原独立 sigma 输入为 $\xi_1,\ldots,\xi_4,c,d$，并写
$$
t_1=\delta\xi_1,\quad t_2=2\delta\xi_2,\quad
t_3=\gamma\xi_3,\quad t_4=\bar\gamma\xi_4,\quad
A=t_1+t_2+t_3+t_4.
$$
在完整六变量上固定
$$
\rho_0=-\frac1{84}
([\delta]_*\nu_\sigma)\otimes([2\delta]_*\nu_\sigma)
\otimes([\gamma]_*\nu_\sigma)\otimes([\bar\gamma]_*\nu_\sigma)
\otimes\nu_\sigma\otimes\nu_\sigma.
\tag{2}
$$
本篇没有先忘掉四个 $\mathcal C$ 输入的独立事件。

两个原目标输出为
$$
Y_s=A+c+2d,\qquad W=Y_t=A+3\delta c+4d.
\tag{3}
$$
原首项规范逐字给
$$
(Y_s)_*\rho_0=\nu_S,\qquad
W_*\rho_0=6\delta\,\nu_T.
\tag{4}
$$
这里 $6\delta$ 来自原
$S=-\mathcal C\,\sigma\,\sigma(2\cdot)/84$、
$T=-\mathcal C\,\sigma(3\delta\cdot)\sigma(4\cdot)/(504\delta)$。
没有把实际 $E_{24}$ 来源另换一个周期。

## 2. 保全部输入的真实 W 核及两态返回

取另外五个物理输出
$$
\begin{aligned}
Q&=3\delta A+29c,& U&=A+3\delta c-14d,\\
R_1&=4t_1-t_2,&
R_2&=7(t_1+t_2)-15t_3,&
R_3&=7(t_1+t_2+t_3)-22t_4.
\end{aligned}
\tag{5}
$$
从 $(t_1,t_2,t_3,t_4,c,d)$ 到 $(W,Q,U,R_1,R_2,R_3)$ 的矩阵为
$$
M=\begin{pmatrix}
1&1&1&1&3\delta&4\\
3\delta&3\delta&3\delta&3\delta&29&0\\
1&1&1&1&3\delta&-14\\
4&-1&0&0&0&0\\
7&7&-15&0&0&0\\
7&7&7&-22&0&0
\end{pmatrix}.
\tag{6}
$$
完整计算给
$$
\det M=3215520=1008\cdot3190,
$$
$$
M\operatorname{diag}(3,12,7,7,1,1)\bar M^{\,t}
=\operatorname{diag}(72,1624,252,60,2310,4466).
\tag{7}
$$
这些固定整数的全部素因子在 $2,3,5,7,11,29$ 中。
当前普通 $p>19$ 不等于惰性的 $29$，故 $M$ 是完整的
$\mathbf Z_p^6$ 整坐标；这里不需要新增模 $29$ 或 $263$ 的 ray。

### 2.1 完整张量格与半特征

把 (2) 的六个原生成变量按 $M^t$ 代换，(7) 消掉全部 Gaussian
交叉项。沿每个显示输出，原奇 sigma 的半特征之积均为一：
前面三个输出各有四个奇 CM 系数，$R_1$ 有零个，$R_2,R_3$
各有两个。模 $2$ 的非零 CM 单位置换原奇半特征，故这些计数
支付了原 lift，而不只是各 degree 为偶。

所得完整联合来源 $\mathcal H_0$ 因此属于
$$
\mathcal S_{72}\otimes\mathcal S_{1624}\otimes\mathcal S_{252}
\otimes\mathcal S_{60}\otimes\mathcal S_{2310}\otimes\mathcal S_{4466}.
\tag{8}
$$
整性用 R413 的原首阶单位基论证：原六 sigma 测度整有界，
$M$ 是普通整自同构，各 theta 基的首阶互异且首系数为单位。
在完整张量基中逐阶消元得到整系数；没有通过除大阶乘推断整性。

只在第一因子施加 R413/R416 已付的真实 $K_{72}$，定义
$$
\mathcal H_1=(K_{72}\otimes I^{\otimes5})\mathcal H_0,\qquad
\rho_1=(M^{-1})_*\nu_{\mathcal H_1}.
\tag{9}
$$
保持当前 $\lambda=-1/\bar\pi_0$、
$\kappa=p/\bar\pi_0^2$。令
$$
v=(3,12,7,7,-3\delta,4)^t,\qquad
w=(1,1,1,1,3\delta,4),
$$
$$
\boxed{\mathcal A_W=I+\frac{\kappa-1}{72}vw.}
\tag{10}
$$
它把 $W$ 乘 $\kappa$，逐个固定 (5) 的五个输出。
完整测度式为
$$
\boxed{
\rho_0|_{W\in p\mathbf Z_p}=\lambda(\mathcal A_W)_*\rho_1,\qquad
\rho_1|_{W\in p\mathbf Z_p}=\lambda(\mathcal A_W)_*\rho_0.
}
\tag{11}
$$
第二式使用整个 $\mathcal S_{72}$ 上的 $K_{72}^2=I$，
不把一个原边际的 core 免费延伸到新联合。
两式对任意六输入事件和测试都成立，须按 (10) 同时运输。
特别
$$
Y_s\longmapsto
Y_s+\frac{\kappa-1}{72}(37-3\delta)W.
\tag{12}
$$
这是真正改变原 $Y_s$ 的操作。

两态的完整 $W$ 边际相同：
$$
W_*\rho_0=W_*\rho_1=6\delta\,\nu_T.
\tag{13}
$$
因为原 $K_{72}T=T$。这不表示两态的每个隐藏区域边际相同。

## 3. 原四挠公式及第二态的完整 Y_s 边际

原对称 lift 记为
$$
(\mathsf T_t^{(N)}F)(z)=e^{-N\eta_t(z+t/2)}F(z+t).
$$
R416 的完整绝对式是
$$
K_{72}=\frac14\sum_{t\in E[4]}\mathsf T_t^{(72)}
       -\frac12\sum_{t\in E[2]}\mathsf T_t^{(72)}.
\tag{14}
$$
它作用于 (8) 的第一轴；每次平移均保另外五个生成变量。

令 $\Xi$ 是 $(Y_s)_*\rho_1$ 的 Amice 来源。置
$$
\Phi_t(z)=
(\mathsf T_t^{(29)}\mathcal C)(z)
(\mathsf T_{3\delta t}^{(1)}\sigma)(z)
(\mathsf T_{4t}^{(1)}\sigma)(2z).
\tag{15}
$$
准确的总 Gaussian 是
$$
\Phi_t(z)=
e^{-\eta_t((37-3\delta)z+36t)}
\mathcal C(z+t)\sigma(z+3\delta t)\sigma(2z+4t).
\tag{16}
$$
其中 $29+27+16=72$，线性项为 $29-3\delta+8$。
于是完整函数为
$$
\boxed{\Xi(z)=-\frac1{336}
 \left(\sum_{t\in E[4]\setminus E[2]}\Phi_t(z)
             -\sum_{t\in E[2]}\Phi_t(z)\right).}
\tag{17}
$$
所有项保留 (16) 的中心相位。单项可能带平坦 twist；
双覆盖后 $\Xi(2z)\in\mathcal S_{136}$。

### 3.1 奇 sigma 的四挠常数

以下先取 $b=1$，$X=x^3$。原全函数式为
$$
\mathcal C=6\sigma^{29}x^2y(X-8)P_2(X),\qquad
P_2(X)=7X^2-4X+16.
\tag{18}
$$
对 $t\in E[4]\setminus E[2]$ 置
$e=x(t)$、$f=y(t)$、$h=x(2t)$，
$c_t=e^{-\eta_t t/2}\sigma(t)$。R419(10) 的原常数是
$$
\boxed{c_t^8=\frac{e-h}{12h^2f^2}.}
\tag{19}
$$
这里必须是 $e-h$；在下面的奇次幂 $c_t^{56}=(c_t^8)^7$ 中反号
会改变整个四挠和。本篇采用 (19)，不从未定平方根读常数。

令
$$
m=(1+3\delta)/2=-\omega^2\gamma,\qquad
n=(1-3\delta)/2=-\omega\bar\gamma.
$$
原 sigma 加法公式，包括 reduced 指数，给
$$
(\mathsf T_t\sigma)(z)(\mathsf T_{3\delta t}\sigma)(z)
=(\mathsf T_{mt}\sigma)(z)^2c_{nt}^2
       \{x(nt)-x(z+mt)\}.
\tag{20}
$$
又因 $r_m(t)r_n(t)=P_2(e^3)$，严格有
$$
c_{mt}^2c_{nt}^2=P_2(e^3)^2c_t^{28}.
\tag{21}
$$
这把 (18) 中的奇幂 $29+1$ 化成 $28+2$，没有另选两个半相位。

为给全多项式计算明确输入，置
$$
g_t(z)=
\frac{y+f+\frac{3e^2}{2f}(x-e)}{x-h}.
$$
由完整除子和原点首项得到
$$
(\mathsf T_t\sigma)^2
=-c_t^2\sigma^2\sqrt{x-h}\,g_t,\qquad
\sqrt{x-h}\sim z^{-1}.
\tag{22}
$$
对四挠点 $\mathsf T_{4t}^{(1)}\sigma=-\sigma$。
(18)–(22) 因而给下面完全确定的有理函数式：
$$
\begin{aligned}
\Phi_t(z)={}&6c_t^{56}P_2(e^3)^2\sigma(z)^{30}\sigma(2z)
(x-h)^7\sqrt{x-h_m}\,g_t^{14}g_{mt}\\
&\quad\cdot(e_n-x_{mt})\,x_t^2y_t(X_t-8)P_2(X_t),
\end{aligned}
\tag{23}
$$
其中下标表示实际平移后的坐标，$h_m=x(2mt)$、$e_n=x(nt)$。

在 $h=-1$ 纤维，可取
$$
e=-1-\sqrt3,\quad f^2=e^3+1,\quad
e_m=\omega(2h-e),\quad e_n=\omega^2(2h-e),\quad
f_m=-3\delta/f,\quad h_m=\omega h.
\tag{24}
$$
剩下两点由 $e\mapsto2h-e$ 和 $f\mapsto-f$ 得出。
平移坐标使用原加法式
$$
x_t=\frac{ex^2+e^2x+2-2fy}{(x-e)^2},
\quad
fy_t=-fy+\frac{fy-f^2}{x-e}(x-x_t).
\tag{25}
$$
双覆盖中的最后一个根也有确定首项：
$$
\sqrt{x(2z)-h_m}
=-\frac{x(z)^2-2h_mx(z)-2h_m^2}{2y(z)}.
\tag{26}
$$

将 (19)、(23)–(26) 代入，
旁列脚本在
$$
\mathbf Q(\sqrt3,\delta)[x,\tau]/(\tau^2-f^2(x^3+1))
$$
中做完整乘法及多项式整除，余数严格为零。
先对两种 $f$ 求和，再取固定 $\delta$ 的 $e$ 共轭和，最后对三个
$h$ 作真实 $\mu_3$ 旋转。后一步在 $\sigma^{136}x^j$ 中准确保留
$j\equiv2\pmod3$。没有插值点或截断尾。

对非零二挠点，(19) 的替代是
$c_t^4=(3h^2)^{-1}$。
真实 division 函数给
$r_{3\delta}(t)c_t^{56}=\delta/6561$。
在 $h=-1$ 处，完整的 $\Phi_t/\sigma^{34}$ 因而是
$$
\begin{aligned}
\frac{4\delta}{729}(X+1)(x+1)^2(x-2)^2
\{- (x-2)^3-8(x+1)^3\}\\
\cdot\{7(x-2)^6+4(x-2)^3(x+1)^3+16(x+1)^6\}.
\end{aligned}
\tag{27}
$$
其双覆盖与三个二挠点的旋转和也由脚本逐项给出。
最后 $t=0$ 项准确是 $\Phi_0=-84S$。

### 3.2 完整边际与实际新谱线

写
$$
H_9(X)=(X+1)(X^2+20X-8)(7X^2-4X+16)
       (X^4+40X^3+2112X^2+3136X+1792).
$$
(17) 的完整结果是
$$
\boxed{\Xi(2z)=-\frac17\sigma^{136}x^2H_9(X)
                        \{A_{12}(X)+\delta B_{12}(X)\},}
\tag{28}
$$
其中
$$
\begin{aligned}
A_{12}={}&17X^{12}-38136X^{11}-2117568X^{10}+23348480X^9\\
&+248235264X^8+868082688X^7-518148096X^6
 +2393505792X^5\\
&+8501723136X^4+6635651072X^3+2686451712X^2
 +591396864X-16777216,\\
B_{12}={}&31X^{12}-27000X^{11}-359904X^{10}+9361408X^9\\
&-218937600X^8-1178698752X^7-3474518016X^6
 -2798419968X^5\\
&+1462763520X^4+2889613312X^3+962592768X^2
 +213909504X+16777216.
\end{aligned}
\tag{29}
$$
式 (28) 包含全部 $23$ 个 principal 坐标，而不只原点首项。
一般 $b$ 按 $b^{-1}F_1(b^{1/6}z)$ 恢复，与 R470 的新来源相同。

使用 R470 同一个完整十八项投影
$$
\mathcal Q=\frac{I-\omega N_{19}}{36}
                  \sum_{j=0}^{17}\omega^jN_7^j
$$
后，全部坐标准确给
$$
\boxed{\mathcal Q\Xi(2z)=\frac{52}{3}S_{\mathrm{new}}.}
\tag{30}
$$
此外完整负块为
$$
\boxed{\frac{I-N_7^9}{2}\Xi(2z)
       =-\frac{1+\delta}{4}S(2z).}
\tag{31}
$$
正块的余部并未消失；$\Xi(2z)$ 的 CM7 循环维数准确为 $10$。
所以 (30) 不能被简化为“$\Xi$ 就是新曲线来源”。

## 4. 同一完整联合上的固定覆盖与秩一分解

为了在保其余五个输出时施加 (30)，取
$$
Q_s=A-29c,\qquad U_s=A+c-15d
$$
和完整固定坐标
$$
\boxed{L=(2Y_s,\,2Q_s,\,2U_s,\,R_1,R_2,R_3).}
\tag{32}
$$
记第一坐标为 $Y$，其余五个为 $\mathbf Z=(Z,V,R_1,R_2,R_3)$。
直接计算
$$
\det L=-13015200,\qquad
\operatorname{Gram}(L)
=\operatorname{diag}(136,3480,1020,60,2310,4466).
\tag{33}
$$
它同样是当前普通 $\mathbf Z_p^6$ 的整自同构。
在原态中，先用未加倍的 $(Y_s,Q_s,U_s,R_1,R_2,R_3)$，
其 Gram 为 $(34,870,255,60,2310,4466)$；
第一因子正是原 $\mathcal S_{34}$，再作 $[2]$ 拉回。
$255$ 轴保原奇 sigma 半特征；(32) 的双覆盖将它同时拉回为
$1020$ 的偶 degree，未将这个奇半特征预先删去。

第二态的各四挠项在 (32) 下也确实无平坦 twist。它们的前三个
完整交叉数为
$$
2(37+3\delta),\qquad 2(29-87\delta),\qquad2(-31+3\delta),
\tag{34}
$$
分别等于 $4(20+3\omega)$、$4(-29-87\omega)$、
$4(-14+3\omega)$；后三个交叉数为零。
因此对每个 $t\in E[4]$，全部 twist 都在同一个固定覆盖中消失。
相位仍由 (16) 保留，而不作逐项重新定标。

两态 $\widehat\rho_i=L_*\rho_i$ 的完整生成来源遂都属于
$$
\mathcal S_{136}\otimes\mathcal S_{3480}\otimes\mathcal S_{1020}
\otimes\mathcal S_{60}\otimes\mathcal S_{2310}\otimes\mathcal S_{4466}.
\tag{35}
$$
由 (11)、(32) 和首阶单位基，它们都在原整张量格中。

令 $\Pi_0$ 是只旋转第一输出的真实 $\mu_6$ 平均，并置
$$
\mathcal P=\mathcal Q\Pi_0.
$$
R466/R470 的完整 CM7、CM19 矩阵给
$\mathcal P\mathcal S_{136}=K S_{\mathrm{new}}$，维数准确为一；
旁列证书也直接检查这个完整投影的秩和幂等性。
所以存在唯一的五变量实际 theta 来源 $\Lambda$，使
$$
\boxed{
(\mathcal P\otimes I^{\otimes5})\widehat\rho_1
   =\nu_{S_{\mathrm{new}}}\otimes\nu_\Lambda.
}
\tag{36}
$$
这一步使用完整第一轴的秩一像，不是由一个边际相等推断张量分解。

设置全部伴随生成变量为零，(30) 给
$$
\boxed{\Lambda(0)=52/3\in\mathcal O^\times.}
\tag{37}
$$
可完全具体地定义 $\Lambda$：对 (36) 左侧的完整生成来源取
第一变量的 $z^6$ 系数，因为 $S_{\mathrm{new}}=z^6+\cdots$。
在同一 Amice 测度中这也等于
$$
\nu_\Lambda=
\frac1{720\Omega_p^6}
\int Y^6\,d\bigl((\mathcal P\otimes I^{\otimes5})\widehat\rho_1\bigr),
\tag{38}
$$
且保留所有 $\mathbf Z$。在 $p>19$ 处，$720\Omega_p^6$ 是单位；
实际投影整性和 (38) 给 $\Lambda$ 的整有界测度。
由 (37) 它的五变量 Amice 级数是单位。这里未沿第一输出作反卷积。

### 4.1 原第一态的整个投影恰为零

这一点比第一边际为零更强。原 $\widehat\rho_0$ 的第一因子位于
$[2]^*\mathcal S_{34}$。R443 的整个 $K_{34}=R$ 与普通单位
$[2]$ 推前交换；在第一 principal 块中 $R=+I$。
R470 的整个 $K_{136}=-N_7^9$ 因而使该子空间满足
$N_7^9=-I$。投影 $\mathcal Q$ 的像则满足 $N_7^9=+I$。
故完整地
$$
\boxed{(\mathcal P\otimes I^{\otimes5})\widehat\rho_0=0.}
\tag{39}
$$
没有把 (4) 的单个原 $S$ 边际冒充整个第一轴的所有来源。
(39) 对完整六变量来源成立，故容许任意完整六变量测试。

## 5. 第三真实中央给任意五伴随测试的条件零

对任意整连续测试 $h(\mathbf Z)$，(36) 给完整函数恒等式
$$
\boxed{
\int_{Y\in\mathbf Z_p^\times}
\langle Y\rangle^{du}h(\mathbf Z)\,
d\bigl((\mathcal P\otimes I^{\otimes5})\widehat\rho_1\bigr)
=J_{S_{\mathrm{new}}}(u)\int h\,d\nu_\Lambda.
}
\tag{40}
$$
这里任意伴随区域、任意深度条件及其补域，都可包含在 $h$ 中；
五个坐标包括原 $\mathcal C$ 的全部三条隐藏伴随。

结合 R466 的实际曲线身份和 R469 的完整 Sha 桥，若以三条原曲线
中央同时失败作反证，则
$J'_S(0)=J'_T(0)=J'_{S_{\mathrm{new}}}(0)=0$。
第三个零准确使 (40) 的整个第一中央行对所有 $h$ 为零。
这条传播不需要把原 $A_{136}$、$\Xi$ 的余谱或某条 rank-zero
参考导数赋成零。

它还可直接写成原联合的一次真实 $W$ 深限制。由 (11)，
$$
\nu_{\Xi(2\cdot)}
=\lambda^{-1}
\left[\,2Y_s+\frac{2(\kappa^{-1}-1)}{72}(37-3\delta)W\,\right]_*
\left(\rho_0|_{W\in p\mathbf Z_p}\right).
\tag{41}
$$
逆缩放只在这个真实深域上使用。一般伴随也由
$L\mathcal A_W^{-1}$ 同时读取；(41) 没有删除任何原独立输入的限制。
随后施加 (36) 的真实 CM 投影，再作第一单位测试，才得到 (40)。

## 6. 实际新 CM 纤维与尚须控制的移动管

第一投影的全部纤维和单位域运输使用 R470(17)–(22)。
具体地，令 $a=\gamma_7^j\gamma_{19}^{\epsilon}$，
$0\le j\le17,\ \epsilon=0,1$，在第一轴取
$$
G_{a,t}(z,\mathbf z)
=(\mathsf T_{\bar at}^{(136)}F)(\bar az,\mathbf z),
\qquad t\in E[a].
$$
完整测度式为
$$
\nu_{N_a^{(1)}F}
=a^{-1}[a^{-1},I_5]_*\sum_{t\in E[a]}\nu_{G_{a,t}}.
\tag{42}
$$
每个新纤维的常数半相位、$1/a$、单位尺度
$\langle a\rangle^{-du}$ 及其导数质量项都保留。
$\Pi_0$ 再给六个真实单位旋转。独立的 $h(\mathbf Z)$ 在这整套
运输中不变，所以 (40) 对它们确实成立。

原 $W$ 却同时依赖第一坐标：
$$
\boxed{
W=\frac{37+3\delta}{68}Y
 +\frac{1-3\delta}{60}Z
 +\frac{-31+3\delta}{510}V.
}
\tag{43}
$$
因此额外的 $W\in p^n$ 条件不是 (40) 中允许任意加入的独立
伴随测试。在 (42) 的一个支和一个第一轴旋转 $\zeta$ 中，
相应测试必须改为
$$
\frac{37+3\delta}{68}\frac{\zeta}{a}Y
 +\frac{1-3\delta}{60}Z
 +\frac{-31+3\delta}{510}V\ \in p^n\mathbf Z_p,
\tag{44}
$$
并保该支的 theta 平移来源。原其他输入域也须一起运输。

所以 (39) 和 (36) 给出了一个真实不交换接口：
原完整 $\mathcal P$ 核经一次原 $W$ core 产生了质量单位的
$S_{\mathrm{new}}$ 张量分量。要继续逼中央非零，仍须把原非零
隐藏域及 (44) 的补域接到 (40)，不能直接令每个移动管中央为零。
本篇把剩余问题固定在同一六输入、两态及明确有限 CM 纤维内。

## 7. 证书与依赖

- [完整精确脚本](../scripts/check-r465-common-six-sigma-true-core-marginal.py)
  及[同名 JSON](../scripts/check-r465-common-six-sigma-true-core-marginal.json)：
  保存完整四挠多项式整除、非零二挠和、原点项、全部 $23$ 坐标、
  (30)、(31)、秩一投影、两个六变量 Gram 与行列式及所有 flat 交叉数。
  计算约五秒；没有目标素数扫描。
- [R398：两条实际来源的六 sigma 规范](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)。
- [R413：原全 theta 张量格与整个 W 核](R413-original-three-output-core-and-eight-source-central-return.md)。
- [R416：包含全部中心的四挠 K72 公式](R416-original-four-torsion-core-and-exact-second-state-marginals.md)。
- [R419：四挠常数与完整多项式计算规范](R419-original-opposite-quarter-translates-and-zero-new-total-marginal.md)。
- [R443：整个 K34 的真实反射](R443-original-residual-quarter-source-and-complete-central-return.md)。
- [R470：显式新谱线、完整 CM 投影与单位域运输](R470-original-riemann-negative-source-and-explicit-new-line.md)。
- R466 的新曲线完整身份、R469 的普通及惰性完整中央/Sha 桥；
  只有第 5 节的算术零传播使用它们，前四节是独立的完整来源恒等式。
