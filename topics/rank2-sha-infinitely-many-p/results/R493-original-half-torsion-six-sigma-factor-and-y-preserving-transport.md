# R493 — 原二挠态的六 sigma 因式、保 Y 三阶变换与真实 W 深管

日期：2026-11-14。**状态：已证明。** R488 的真实二挠态
$h=e_1+e_2$ 可完全改写成原六个独立 sigma 的一次 Hadamard
推前。经原 $\mu_6$ 相位及输入置换归一，所得实际三阶变换
$\mathcal T$ 严格固定 $Y_s$，只变换其五个完整伴随，故与第一
$Y$ 算术投影严格交换。本篇还给保持 $W$ 的真实反射、原来源的
新 scalar $W'$ 核，以及五深一单位独立网格到 $h$ 的 $W$ 深管
的准确运输。该管上一个六次正矩加权的 $Y$ 中央非零，赋值恰为
$5n$；其测试并非纯 $Y$ 伴随，不能因此宣布原完整中央非零。
主目标未完成。

## 1. 原六输入与真实二挠态

固定 R465 的同一 $b=17$、sigma、普通周期 $\Omega=\Omega_p$：
$$
\delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
\gamma=(5+\delta)/2,\quad\gamma\bar\gamma=7,
$$
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1.
\tag{1}
$$
用六个**未缩放**的独立原 sigma 变量
$$
\boldsymbol\xi=(\xi_1,\xi_2,\xi_3,\xi_4,c,d_0),\qquad
\rho_0=-\frac1{84}\nu_\sigma^{\otimes6}.
\tag{2}
$$
原两个实际输出为
$$
\begin{aligned}
Y_s&=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma\xi_4+c+2d_0,\\
W&=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma\xi_4+3\delta c+4d_0.
\end{aligned}
\tag{3}
$$
边际为 $S,6\delta T$，degree 分别为 $34,72$。
R488 的三态满足
$$
e_0=\rho_0,\quad e_1=K_W\rho_0,\quad
e_2=-\frac14\sum_{t\in E[4]}\mathsf T_{t,W}\rho_0,
$$
$$
\boxed{h=e_1+e_2=-\frac12\sum_{t\in E[2]}\mathsf T_{t,W}\rho_0,
\qquad K_Wh=-h.}
\tag{4}
$$
每个平移保原其余五个 $W$ 伴随，不是只作用一个边际。

## 2. 全部半周期相位与四 sigma 的准确和

canonical lift 为
$$
\mathsf T_t^{(N)}F(z)=e^{-N\eta_t(z+t/2)}F(z+t).
\tag{5}
$$
按原物理周期先令 $\Omega_\infty=1$。
取 $t=(s+r\omega)/2$，$s,r\in\{0,1\}$。在六个原生成变量中，
$W$ 平移的参数依次是
$$
(\delta,2\delta,\gamma,\bar\gamma,3\delta,4)t.
\tag{6}
$$
其 Gaussian 次数和为 $72$；原正交恒等式使 (6) 的乘积正是
(4) 的完整 $W$ 平移。

选中 $I=(\xi_1,\xi_3,\xi_4,c)$，取 CM 单位
$\boldsymbol\eta=(1,\omega^2,\omega,1)$。这四个系数除以
$\eta_i$ 后准确为
$$
\delta,\ -1+2\omega,\ -3-2\omega,\ 3\delta=1+2k_i,\qquad
(k_i)=(\omega,-1+\omega,-2-\omega,1+3\omega).
\tag{7}
$$
$\prod\eta_i=1$。由 $\sigma(\eta z)=\eta\sigma(z)$，四个新的
生成变量是
$$
\boldsymbol z=(x_1,\omega x_3,\omega^2x_4,x_c).
\tag{8}
$$
必须保留 (7) 多出的格周期。若
$k_i(s+r\omega)=m_i+n_i\omega$，其相位为
$$
(-1)^{m_i+n_i+m_in_i}
\exp\!\left(\frac{\pi i}{2}(m_ir-n_is)\right).
\tag{9}
$$
附脚本对四个 $t$ 逐项列出：四项 (9) 的乘积全部为 $1$。
未选中的第二个 sigma 给
$\mathsf T_{2\delta t}^{(1)}\sigma=\sigma$（$t=0$）、
$-\sigma$（$t\ne0$），因为 $\delta(s+r\omega)$ 的非零模二类
有奇 sigma 特征 $-1$。最后一个因子
$\mathsf T_{4t}^{(1)}\sigma=\sigma$，因 $4t\in2\Lambda$。
所以总权重准确是 $(+,-,-,-)$。

### 2.1 半周期四项和的完整证明

记 $\sigma_t=\mathsf T_t^{(1)}\sigma$，$q=\frac12\sum z_i$。
整个函数身份为
$$
\boxed{\sum_{t\in E[2]}\prod_{i=1}^4\sigma_t(z_i)
=2\prod_{i=1}^4\sigma(q-z_i).}
\tag{10}
$$
为给出完整证明，置
$(z_1,z_2,z_3,z_4)=(a+b_1,a-b_1,c+e,c-e)$，记
$A=\wp(a),B=\wp(b_1),C=\wp(c),D=\wp(e)$。
对非零二挠点，$h_t=\wp(t)$、$c_t=\sigma_t(0)$ 满足
$c_t^4=(3h_t^2)^{-1}$、$h_t^3=-b$，并由原 sigma 加法得到
$$
\sigma_t(a+b_1)\sigma_t(a-b_1)
=c_t^2\sigma(a)^2\sigma(b_1)^2
 \{AB-h_t(A+B)-2h_t^2\}.
$$
故 (10) 左边除以
$\sigma(a)^2\sigma(b_1)^2\sigma(c)^2\sigma(e)^2$ 后是
$$
(B-A)(D-C)+
\sum_{h^3=-b}\frac{
 (AB-h(A+B)-2h^2)(CD-h(C+D)-2h^2)}{3h^2}.
$$
三根的 $h^{\pm1},h^{\pm2}$ 之和全零，显示式恰为
$2(A-D)(C-B)$。再次用原 sigma 加法即得 (10) 右边。
证明在无极开集成立后延拓到全域，未靠有限 Taylor 项。

令
$$
H=\begin{pmatrix}
1&1&1&1\\1&1&-1&-1\\1&-1&1&-1\\1&-1&-1&1
\end{pmatrix},\quad C_+=H/2,\quad C_-=(\mathbf1\mathbf1^t-2I)/2.
\tag{11}
$$
R337(9)–(10) 已由原两变量加法证明
$$
\prod_i\sigma(z_i)=
\prod_i\sigma((C_+\boldsymbol z)_i)+
\prod_i\sigma((C_-\boldsymbol z)_i).
\tag{12}
$$
$C_-$ 与 R337 的矩阵只差输出置换，乘积相同。
由 (10)、(12)，真实带权和为
$$
\prod_i\sigma(z_i)-\sum_{t\ne0}\prod_i\sigma_t(z_i)
=2\prod_i\sigma((C_+\boldsymbol z)_i).
\tag{13}
$$

## 3. 真六 sigma 因式与固定 Y 的三阶变换

在选中四维中置
$$
E=\operatorname{diag}(1,\omega,\omega^2,1),\qquad A=EC_+,
$$
并在其余两维取恒等。(4)、(7)–(13) 的准确常数给
$$
\boxed{h=-A_*\rho_0.}
\tag{14}
$$
其整个生成函数是
$$
\frac1{84}\sigma(x_2)\sigma(x_d)
 \prod_{i=1}^4\sigma((C_+E\boldsymbol x_I)_i).
\tag{15}
$$
输入仍全为同一原 sigma。$A$ 的分母只有二且是 Hermitian
等距，Gaussian 交叉项全消，故 (14) 是真实整有界测度身份。
所有隐藏条件都按 $A$ 的完整逆像运输。

进一步取
$$
O=\begin{pmatrix}
-\omega&0&0&0\\0&0&\omega^2&0\\0&0&0&\omega\\0&1&0&0
\end{pmatrix},\qquad
\boxed{\mathcal T=AO=EC_+O.}
\tag{16}
$$
$O_*\rho_0=-\omega\rho_0$，所以
$$
\boxed{h=\omega^2\mathcal T_*\rho_0.}
\tag{17}
$$
各矩阵都固定 $\xi_2,d_0$。准确有
$$
\boxed{\mathcal T^3=I,\quad\mathcal T\bar{\mathcal T}^{\,t}=I,\quad
Y_s\circ\mathcal T=Y_s.}
\tag{18}
$$
这是物理六输入等式，不仅是有限来源空间中的形式关系。

第二次返回的系数也完全确定。置
$$
O_2=\begin{pmatrix}
\omega^2&0&0&0\\0&0&0&-\omega^2\\0&-\omega&0&0\\0&0&-1&0
\end{pmatrix}.
$$
有 $\mathcal T^2=EC_-O_2$、
$(O_2)_*\rho_0=-\omega^2\rho_0$；(12)、(14) 给
$$
\boxed{(\mathcal T^2)_*\rho_0=-\omega^2(\rho_0+h).}
\tag{19}
$$

### 3.1 同一来源的 W 保持反射

在四维中置
$$
v=(1,\omega,-\omega^2,-1)^t,\qquad
\boxed{\mathcal U=I-\frac12v\bar v^{\,t},}
\tag{20}
$$
在另外两维为恒等。准确有
$$
\mathcal U^2=I,\quad\mathcal U\bar{\mathcal U}^{\,t}=I,\quad
W\circ\mathcal U=W.
\tag{21}
$$
取
$$
P=\begin{pmatrix}
0&1&0&0\\0&0&0&-\omega^2\\0&0&-\omega&0\\-\omega&0&0&0
\end{pmatrix}.
$$
$\mathcal U=\mathcal T^2P$、$P_*\rho_0=-\omega\rho_0$，故
$$
\boxed{\mathcal U_*\rho_0=\rho_0+h.}
\tag{22}
$$
于是任意完整可积测试 $f$ 和实际紧开域 $D$ 都满足
$$
\boxed{
\int_D f\,dh=
\int_{\mathcal U^{-1}D}f\circ\mathcal U\,d\rho_0-\int_D f\,d\rho_0
=\omega^2\int_{\mathcal T^{-1}D}f\circ\mathcal T\,d\rho_0.}
\tag{23}
$$
两个域真正不同；$\mathcal T$ 保 $Y_s$，$\mathcal U$ 保 $W$，
不能将它们各自保持的输出互换使用。

## 4. 完整第一 Y 投影与五伴随的准确运输

为接 R483，令
$$
D_\alpha=\operatorname{diag}(\delta,2\delta,\gamma,\bar\gamma,1,1),
$$
$$
L_0=\begin{pmatrix}
2&2&2&2&2&4\\2&2&2&2&-58&0\\2&2&2&2&2&-30\\
4&-1&0&0&0&0\\7&7&-15&0&0&0\\7&7&7&-22&0&0
\end{pmatrix},\qquad L=L_0D_\alpha.
\tag{24}
$$
这是从本篇未缩放输入到 R483
$(Y,\mathbf Z)=(2Y_s,2Q_s,2U_s,R_1,R_2,R_3)$ 的整个矩阵。

五伴随算子由以下完整显示式指定：
$$
\boxed{L\mathcal T L^{-1}=\operatorname{diag}(1,D_5).}
\tag{25}
$$
第一行由 (18) 给出，第一列没有交叉项则由原正交及等距性给出。
脚本直接计算整个矩阵；JSON 列出 $D_5$ 的二十五个 $K$ 系数，
并验证
$$
D_5^3=I,\qquad
D_5\operatorname{diag}(3480,1020,60,2310,4466)\bar D_5^{\,t}
=\operatorname{diag}(3480,1020,60,2310,4466).
\tag{26}
$$
逆矩阵只涉及固定素数 $2,3,5,7,11,17,29$，当前 ray 的
$p\ge71$，故 $D_5$ 是原 $\mathbf Z_p^5$ 整自同构。
没有依赖 $p$ 或截断深度的系数。

(17) 在该坐标中准确成为
$$
\boxed{\nu_{h^L}=\omega^2[I_Y,D_5]_*\nu_{\mathcal F_0^L}.}
\tag{27}
$$
生成变量的拉回只动五伴随，所以与第一 $Y$ 轴全部 canonical
CM trace、反射及角投影逐项交换，包含中心相位；不需要先投到
principal 格才成立。

记 R483 的真实第一轴投影为 $P_S,P_{\rm new},P_H$。其完整
来源身份给
$$
\boxed{
P_Sh^L=\omega^2 S(2Y)\otimes(D_5)_*A_0,\qquad
P_{\rm new}h^L=P_Hh^L=0.}
\tag{28}
$$
$A_0$ 是 R483 的质量一五伴随。完整测试 $g_u$ 准确转置为
$g_u(D_5\mathbf Z)$；其 Mellin 导数也全部如此运输。
因此 $J'_S(0)=0$ 确实消掉 (28) 第一行全部完整伴随中央，
但不自动消掉未投影 $h$ 的任意混管中央。

作为全边际校验，
$$
\boxed{(Y_s)_*h=\omega^2\nu_S=-\frac{1+\delta}{2}\nu_S,\qquad W_*h=0.}
\tag{29}
$$
它与 R488 的完整二挠计算吻合；下一节还从真正独立输入解释
第二个零。

## 5. 原来源的新 W' scalar 核与独立零质量方向

将 (3) 的 $W$ 行乘 $\mathcal T$，得到
$$
\boxed{
W'=W\circ\mathcal T=
(2+2\delta)\xi_1+2\delta\xi_2+(2+2\delta)\xi_3
 +(3+\delta)c+4d_0.}
\tag{30}
$$
原独立输入 $\xi_4$ 完全不出现，系数的范数和恰为 $72$。
事实上全部系数可除以二，$W'/2$ 的 degree 为 $18$；本篇保
$W'$ 的原物理尺度。

由 (4)、(17)，$h$ 的真实 $W$ scalar core $\beta=-\lambda$
严格拉回成
$$
\boxed{
\rho_0|_{W'\in p\mathbf Z_p}
=\beta(C_{W'})_*\rho_0,\qquad
C_{W'}=I+\frac{\kappa-1}{72}\bar w'^{\,t}w'.}
\tag{31}
$$
$w'$ 是 (30) 的完整六维行。所有与它正交的原伴随都保持，
特别 $\xi_4$ 原样保持。$W'$ 边际本身为零，(31) 来自整个
联合的可逆推前，绝非用零边际猜核心。

给其余五输入任意完整紧开条件和连续测试，再给 $\xi_4$ 一个
原点深度或环带条件，只要测试不依赖 $\xi_4$，积分严格为零：
原 $\nu_\sigma$ 的这些深度和环带质量全零。也可乘
$\xi_4^{6k}$，原 $\mu_6$ 角色使该独立径向积分仍为零。
可附任意 $W'$ 单位 Mellin 权，但 $Y_s$ 权依赖 $\xi_4$，
不在此项零传播范围内。

未积分掉的五 sigma 在 $W'$ 上的来源，连同 (2) 的常数，为
$$
\frac{\omega^2}{84}\sigma(4z)^3\sigma(2\delta z)^2.
\tag{32}
$$
所以缺一输入是实际全来源因式，不是首项偶然为零。

## 6. 真五 sigma Y 残余的 degree27 与完整原核

删去 $\xi_4$ 后，
$$
Z=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+c+2d_0,\qquad
Y_s=Z+\bar\gamma\xi_4.
\tag{33}
$$
其固定来源是
$$
\boxed{
B_{27}(z)=-\frac1{84}
 \sigma(\delta z)\sigma(2\delta z)\sigma(\gamma z)\sigma(z)\sigma(2z),
\quad B_{27}(z)=\frac{\gamma}{7}z^5+O(z^{11}).}
\tag{34}
$$
degree 恰为 $3+12+7+1+4=27$，并非旧 $33$。

保全部四个隐藏伴随：对五个物理输入
$(\delta\xi_1,2\delta\xi_2,\gamma\xi_3,c,2d_0)$ 取矩阵
$$
\begin{pmatrix}
1&1&1&1&1\\4&-1&0&0&0\\7&7&-15&0&0\\
1&1&1&-22&0\\4&4&4&4&-23
\end{pmatrix}.
\tag{35}
$$
其完整 Hermitian Gram 为
$$
\operatorname{diag}(27,60,2310,506,2484).
\tag{36}
$$
行列式和原 CM 输入尺度在当前普通处为单位。第一轴保原奇
半特征：三个奇 CM 系数各保 sigma 唯一的奇特征；其余轴及
Gaussian 交叉项由 (35)、(36) 直接支付。

当前原 ray 已有
$$
g_\pi=\pi_0/\bar\pi_0\equiv1\pmod{54}.
\tag{37}
$$
R370、R454 的完整 odd theta 交织给 whole $K_{27}$ 为标量。
真实锚 $\sigma(3\delta z)\in\mathcal S_{27}$ 保同一奇半特征，
其 ordinary core 是 $\beta=-\lambda$。因此
$$
\boxed{K_{27}=-I\quad\text{在整个原奇 }\mathcal S_{27}\text{ 上}.}
\tag{38}
$$
原五输入联合沿 $Z$ 的真实 core 是 $\beta$，保 (35) 另外四个
输出及独立 $\xi_4$；没有猜 odd 相位，也没有从零边际定标。

## 7. 真独立网格到 h 的 W 深管及非零带权中央

对 $n\ge1$ 取原独立网格
$$
\mathcal D_n=\{\xi_4\in\mathbf Z_p^\times,\
 \xi_1,\xi_2,\xi_3,c,d_0\in p^n\mathbf Z_p\}.
\tag{39}
$$
此域上 $Y_s$ 是单位。考虑准确指定的带权中央
$$
\mathcal I_n=
\int_{\mathcal D_n}\xi_4^6\,d\log\langle Y_s\rangle\,d\rho_0.
\tag{40}
$$
$I_{\sigma,1}=\int_{\mathbf Z_p^\times}x\,d\nu_\sigma
=\Omega(1-\beta\kappa)$ 是单位。五个原 sigma 各自的深度 core 给
$$
\mathcal I_n=\beta^{5n}\mathcal A(\kappa^n),
$$
$$
\mathcal A(T)=d\int_{x\in\mathbf Z_p^\times}
x^6\log\langle\bar\gamma x+TZ\rangle
\,d\nu_{B_{27}}(Z)d\nu_\sigma(x).
\tag{41}
$$
这里使用五个原输入同时深的限制，没有将它与只有 $Z$ 深混同。

(34) 给 $B_{27}$ 次数 $0,\ldots,4$ 的矩全零，第五矩为
$120\Omega^5\gamma/7$，故
$$
\boxed{[T^5]\mathcal A(T)
=24d\,\Omega^5\bar\gamma^{-6}I_{\sigma,1}\in\mathcal O^\times.}
\tag{42}
$$
更低系数全零。一般 $k\ge5$ 的完整系数是
$$
\frac{d(-1)^{k+1}}{k}\bar\gamma^{-k}
\left(\int Z^k\,d\nu_{B_{27}}\right)
\left(\int_{\mathbf Z_p^\times}x^{6-k}\,d\nu_\sigma\right),
\tag{43}
$$
赋值至少 $-v_p(k)$。对 $p\ge71,n\ge1$，
$kn-v_p(k)>5n$ 对全部 $k\ge6$ 成立，整个 log 展开在
$T\in p\mathbf Z_p$ 收敛。因此
$$
\boxed{v_p(\mathcal I_n)=5n,\qquad\mathcal I_n\ne0.}
\tag{44}
$$
这里没有未知负五矩，且全尾已支付。

置 $\mathcal E_n=\mathcal T\mathcal D_n$、
$\ell_4=(\mathcal T^{-1}\boldsymbol\xi)_4$。(17)、(18) 给
$$
\boxed{
\int_{\mathcal E_n}\ell_4^6\,d\log\langle Y_s\rangle\,dh
=\omega^2\mathcal I_n\ne0,}
\tag{45}
$$
并由 (30)、(39) 得
$$
\mathcal E_n\subset
\{W\in p^n\mathbf Z_p,\ Y_s\in\mathbf Z_p^\times\}.
\tag{46}
$$

### 7.1 全部 W 伴随条件也准确保留

按 $(\xi_1,\xi_2,\xi_3,c,d_0)$ 的顺序，记 (30) 的五个非零
系数为 $a_1,\ldots,a_5$，取
$$
q_j=x_j-\frac{\bar a_j}{\bar a_1}x_1,\qquad 2\le j\le5.
\tag{47}
$$
每个 $q_j$ 与 $W'$ 正交，变换 $(W',q_2,\ldots,q_5)$ 的
行列式为 $72/\bar a_1$，是单位。故 (39) 等价于
$\xi_4$ 为单位、$W'$ 及四个 $q_j$ 全在 $p^n\mathbf Z_p$。
在 $h$ 坐标中，准确成为
$$
\boxed{\mathcal E_n=
\{\ell_4\ {\rm unit},\ W\in p^n\mathbf Z_p,\
q_j\circ\mathcal T^{-1}\in p^n\mathbf Z_p,\ 2\le j\le5\}.}
\tag{48}
$$
这五个函数是 $W$ 的完整伴随。原 $W$ core 固定 $\ell_4$、
其单位条件及六次测试；另四个深条件也原样保持。

若沿 (4) 将 (45) 拉回 $n$ 层，所有伴随条件仍是 (48) 的那些
条件，$W$ 变为不受限，而 $Y_s$ 测试准确变为
$$
Y_s+\frac{\kappa^n-1}{72}(37-3\delta)W.
\tag{49}
$$
真实单位指示函数随该表达运输；父域中原未改变的 $Y_s$ 未必为
单位。这得到有完整补域说明的非零移动测试，并非新的条件零。

### 7.2 与第一 Y 算术条件行的区别

因为 $\mathcal T$ 固定 $Y_s$ 且等距，$\ell_4$ 的 $Y_s$ 正交
分解准确为
$$
\boxed{\ell_4=\frac{\gamma}{34}Y_s+\ell_4^\perp.}
\tag{50}
$$
所以 $\ell_4^6$ 产生真正的正 $Y_s$ 权，不能直接当成 (28) 中
不改变第一 Mellin 权的五伴随测试。合法的纯 $Y_s$ 伴随是
$$
\gamma Y_s-34\ell_4.
\tag{51}
$$
在 (33) 原两输入中，它是 $\gamma Z-27\xi_4$，真实极化为
$$
\begin{pmatrix}1&\bar\gamma\\\gamma&-27\end{pmatrix}
\operatorname{diag}(27,1)
\overline{\begin{pmatrix}1&\bar\gamma\\\gamma&-27\end{pmatrix}}^{\,t}
=\operatorname{diag}(34,918).
\tag{52}
$$
行列式为 $-34$。下一接口是以这条完整纯伴随的正次数测试抽回
原 $S$ 中央，并同时保 (45) 的非零首项；本篇没有省略 (50)
的移权项或 (48) 的真实补域。

## 证书与依赖

- [完整半周期相位、真实 T/U、五伴随、degree27 核与原网格证书](../scripts/check-r493-original-half-torsion-six-sigma-factor.py)；
  [精确数据](../scripts/check-r493-original-half-torsion-six-sigma-factor.json)。
- [R337：原 sigma 加法及完整 Hadamard 测度身份](R337-original-hadamard-domain-transport-and-depth-zero-propagation.md)。
- [R465：原共同六输入及两个物理输出](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R483：完整第一 Y 三曲线投影及五伴随](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)。
- [R488：真实三态与二挠态 h 的 W 核](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)。
- [R454：odd theta 完整中心、半特征与绝对定标](R454-original-odd33-core-and-exact-residual-slope-transport.md)。

