# R119 续篇：相位控制新 profile 的完整全标签图、弱源两迹与真实 raw 入口

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 对第8193层以后新增的真实下降坡平移和
$C^4$ 紧支集形状控制，本文重建含完整 mean 的零 Darboux residual
全频尾图。低窗、内部标签、两个真正接缝和规范权都保持原定义：
$$
 \|\mathcal G_\Pi\|<2^{16},\qquad
 \|\mathcal H_\Pi\|<9,\qquad
 \|X_\Pi(a)\|_{\mathcal X_\beta}<16\|a\|_{\ell^1_\beta},
 \quad\|a\|_{\ell^1_\beta}<1/64,\quad\beta\ge0. \tag{C.1}
$$
这是真正新度量族的重建，不把原强尾的局部图直接转授给改变后的
系数。完整弱源使用总通量两态，无需对 $F^t$ 作径向微分。
原 raw404 权与逐点重新选择的 regular 线也在新对象上成立。

这些结论不等于完整非线性外接口 $\mathcal F_c=0$ 已经闭合。
尤其实际非径向相位参数选择、移动中频 Schur 的定量下界、
原同权内部 Green 及更新后 mixed 反馈仍须在同一最终参数上联立。
本篇没有把任意粗 Sobolev 外迹授予完整尾的 $C^2$ 重建权限。

## 1. 一个明确的新公共度量族

固定
[强首剪切局部图](R119-supplement-stronger-deep-first-shear-and-complete-local-map.md)
和[强全标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
的实际数据，并采用[第47束双参数重建](R119-supplement-two-parameter-full-tail-chart-reconstructed.md)
的同一两 bump 族及其复域。以下所有“未改前缀”均相对于固定同一 $\Gamma$
的这个双参数对象，而非去掉第二 bump 的更早对象。
$$
 \delta_j=(2/25)2^{-j},\quad \eta_j=\delta_j^{3/2}/(4\sqrt2),
 \quad\mathsf K=2^{128},\quad C=16\sqrt2,\quad\alpha=65/64,
$$
$$
 \mu_j=\begin{cases}\epsilon\delta_j^6,&j\le4096,\\
 \epsilon\delta_{4096}^{3/2}\delta_j^{9/2},&j>4096,\end{cases}
 \qquad w(r)=\mu_jp_*(r)/r^7,\quad y=\sqrt{12}\log r.
 \tag{C.2}
$$
第8192层以前完全不改。对每个 $j\ge8193$ 的两个下降坡，
采用[真实相位保持控制](R119-supplement-phase-preserving-actual-finite-Schur-controls.md)
§1 的两个固定端点窗口。令
$$
 \ell_{j,k}=\eta_js_{j,k}/\sqrt{12},\qquad
 |s_{j,k}|<1/16 \quad\hbox{（复扩张 }|s_{j,k}|<1/8\hbox{）}.
 \tag{C.3}
$$
将整条下降坡连同原两个 bump 一起平移 $\ell_{j,k}$；相邻的
常 $Q=7$ 平台分别增减同一长度。胞元总长、两端值以及两端全部
已有 germ 都准确不变。每条主平台长度在
$\delta_j-\eta_j/8$ 与 $\delta_j+\eta_j/8$ 之间；末端短平台
仍大于 $7\eta_j/8$。

此外在各下降坡的单位坐标 $x$ 内加入
$$
 J_x=(7/16,15/32),\qquad
 \Xi_{j,k}\in C^4_0(J_x),\quad
 \|\Xi_{j,k}\|_{C^4_x}<2^{-21}
 \quad\hbox{（复扩张 }2^{-20}\hbox{）},
$$
$$
 \log p_*=\log p_{\rm left}-\Delta S(x)
       +\gamma_1\psi_1(x)+\gamma_2\psi_2(x)+\Xi_{j,k}(x),
 \qquad S=10x^3-15x^4+6x^5. \tag{C.4}
$$
$C^4_0(J_x)$ 表示零延拓仍为 $C^4$；第52束实际构造的 $C^5$
测试方向属于此空间。原 $\gamma_1$ 实盒 $2^{-16}$、复盒 $2^{-15}$，
$\gamma_2$ 实盒 $2^{-30}$、复盒 $2^{-29}$ 保留。原两个 bump 支集与 $J_x$ 不交。
所有参数记为 $\Pi=(\Gamma,s,\Xi)$。

本文全图覆盖上述完整参数盒，并不要求每个 $\Pi$ 都已满足两个
相位方程。第52束选择的相位保持子族是其中的实际子族；其后若
随非零标签重新选择 $\Gamma$，必须使用新图的真实参数导数。

在 $J_x$ 上
$$
 S'>7/4,\qquad S''>7/8,\qquad \Delta>j/2.
 \tag{C.5}
$$
故 $\Xi$ 的前两导数不能改变下降坡的 $|p_*|$ 单调性，也不能
改变 $Q=7+\Delta S'/(\eta/\sqrt{12})-\cdots$ 在该支集上的
单调方向。$J_x$ 严格位于峰点 $1/2$ 的左边，且
$S'(1/2)-S'(15/32)>1/128$；峰值、两个真实上升根及根附近
完整 quartic germ 不变。实参数下每个负分量仍是一个单峰。
复盒中使用 $\partial_x\operatorname{Re}\log p_*$ 的符号；
不把复数面积当正实面积。

始终有
$$
 \delta_j/2\le |p_*|\le\mathsf K/\delta_j,\qquad
 |\mu_jp_*/r^7|\ge\mu_j\delta_j/256.
 \tag{C.6}
$$
相邻胞元仍满足 $c_j\mu_j=\mu_{j-1}$。径向零延拓在平盘处
仍有真正 $C^2$ 背景，因为同一宽界
$$
 |w|<2\mathsf K\mu_j\delta_j^{-1},\quad
 |w_r|<2^{10}\mathsf K\mu_j(j+5)\delta_j^{-5/2},\quad
 |w_{rr}|<2^{22}\mathsf K\mu_j(j+5)^2\delta_j^{-4}
 \tag{C.7}
$$
给正幂 $7/2,2,1/2$。这只支付新参考几何，未据此授予最终
非径向嵌入的 reach。

## 2. 固定端点全纯性与实际径向正则性

对每个径向段改用其固定 $x\in[0,1]$。坡长仍为 $\eta$，
平台长度是 $s$ 的仿射函数，$p_*$ 是 $\Gamma,\Xi$ 的整函数；
$r=\exp(t_{\rm start}+x\,\ell_{\rm segment})$ 也是参数整函数。
在复盒中，各段长度的实部为正且总长固定，所以仍有
$1\le|r|\le2$。因此完整有限投影方程及其有源强修正可在同一
固定段参数空间构造，端点 map 全纯依赖全部参数。
这里既不把有限投影当最终解，也不把复时间当真实物理半径。

固定物理 $t$ 的 profile 穿过平移接缝时只有已给的径向 $C^2$
正则性；本文不声称它作为 $C^2_t$ 值函数对 $s$ 全纯。
真实物理解的 $C^2$ 连续性由统一二 jet 包络和逐段重建得到。
这一区分同样适用于之后的 metric-source 和移动切口导数。

## 3. 真低窗误差：仍保原 $2^{272}$ 与原低窗

以下 canonical 两行估计只对 $m\in4\mathbb Z\setminus\{0\}$。
mean 在第6、9节另付。写 $M=|m|$，
$$
 A_p=\begin{pmatrix}k_m&\nu_m/p_*\\-p_*&-k_m\end{pmatrix},
 \quad k_m=(m^2-4)/\sqrt{12},\quad
 \nu_m=m^2(m^2-1)/12,
 \quad A_p^2=-(7m^2-16)I/12
 \tag{C.8}
$$
于常平台。新的理想矩阵准确仍为
$$
 B^\infty_{m,\mathsf K,C}=
 \begin{pmatrix}
 1-\mathsf K\alpha\nu&\alpha\nu\\
 (\mathsf K\alpha\nu-\mathsf K-1)/C&(1-\alpha\nu)/C
 \end{pmatrix},\qquad \det B_{m,j}=1/C. \tag{C.9}
$$
采用同一
$$
 M_j^{\rm new}=2^{-40}\delta_j^{-1/8}.
 \tag{C.10}
$$
在 $M\le M_j^{\rm new}$ 时，$M^4\sqrt\delta\le2^{-160}$。
六个短段的完整 generator 积分至多
$32\mathsf K M^4\sqrt\delta\le2^{-27}$。
三条真主平台的范数可取 $4\mathsf K,8\nu,6$；
其相对原三个理想剪切的差分别至多
$(5\mathsf K,5,5)M^4\sqrt\delta$。这里平台长度的真实变化
$\pm\eta s$ 已由精确 sin/cos 式中的
$|(\ell-\delta)/\delta|\le\eta/(8\delta)$ 支付。

有序望远镜展开中，每个平台只出现一次。三个平台之间的
乘积差小于 $2^5\mathsf K M^8\sqrt\delta$。
将全部短段插回其实际位置的费用至多
$$
 192\mathsf K\nu
   \big(e^{32\mathsf K M^4\sqrt\delta}-1\big)
 <2^{10}\mathsf K^2 M^8\sqrt\delta .
$$
末端 $\operatorname{diag}(1,1/C)$ 不放大范数，故
$$
 \boxed{\ \|B_{m,j}-B^\infty_{m,\mathsf K,C}\|_\infty
 <2^{267}M^8\sqrt\delta<2^{272}M^8\sqrt\delta.\ } \tag{C.11}
$$
所有面积证明同时覆盖完整复参数盒，$\Xi$ 只通过真实单调
端值界进入。没有把新真实矩阵换成理想矩阵。

较大的内部窗 $M\le2^{-5}\delta^{-3/8}$ 使用原单调 Gauss
分解。仍有 $\sqrt\delta+k_m\delta+\nu_m\eta<2^{-24}$。
在原有序 $D P_+C_*P_-$ 中可取
$$
 \|D\|<2,\quad\|P_-\|<4\mathsf K,\quad
 \|C_*\|<8\nu,\quad\|P_+\|<8.
$$
中央因子的两条反剪切均保留；新增形状没有改变单调段的
端值面积，平台变化只将原宽界放大不超过2。
每个截短子区间仍服从相同面积界，故
$$
 \|\Psi(s,t)\|_\infty<2^{140}M^4,\qquad
 \|\Psi(t,s)\|_\infty<2^{141}M^4. \tag{C.12}
$$
没有出现 $e^{\mathsf K}$。

## 4. 真高频与参考两根 Cauchy

令
$$
 \beta_j^c=\beta_{\mathsf K}(\delta_j)+2\eta_j,\quad
 \beta_{\mathsf K}(\delta)=3\delta+6\eta+
 \sqrt{(15/2)\eta[2\log(2\mathsf K)+6|\log\delta|]}.
 \tag{C.13}
$$
形状的总附加变差小于 $2^{-18}$，已在
$2\log(2\mathsf K)-[2\log(\mathsf K\alpha)-\log C]>1$ 的
原跳幅储备内。标量化全频能量中的四次过渡数不变；不必因
$\Xi$ 的支集端点另加径向状态转换。其 $C^4$ 零延拓至少给
原论证所需的 $b=(\log p_*)_y$ 连续和分段导数界。

实平移的 $Q=7$ 总长度准确不变。复平移时，平台复时间的
全部虚部至多给额外 $e^{2M\eta}$；这正是 (C.13) 的末项。
原小窗精确平台证明和大窗标量能量分别重新给
$$
 \boxed{\quad
 \|\Psi(s,t)\|_\infty,\ \|\Psi(t,s)\|_\infty
 <2^{482}(1+M)^{312}e^{M\beta_j^c}
 \quad} \tag{C.14}
$$
于全部内部子区间和所有非零模。常数账可使用原
$2^{440}$ 未取粗幂常数：四个内部能量变换各放宽2，两个
endpoint 换算各放宽2，平台及范数换算再付 $2^{10}$，
连同原 $2^{10}$ 余量仍小于 $2^{482}$。
所得312次频率幂未增加；没有对低窗外的模作理想化。

准确有 $1024\beta_j^c<h_j$。例如以
$j+3<-\log_2\delta_j<j+4$，
$\log_2(j+47)\le j/128$（$j\ge8193$）逐项估计，
$\beta_j^c<8\sqrt{j+47}\,\delta_j^{3/4}$，因此
$\log_2(\beta_j^c/h_j)<-6082$ 在首层成立且继续下降。

在真实参考 Airy 两态中，根、完整 quartic germ 和根处密度
端值不变。修改支集上的 $Q,Q_t,Q_{tt}$ 仍满足原
$2^{12}(j+4)\delta^{-3/2}$、
$2^{18}(j+4)\delta^{-3}$、
$2^{26}(j+4)\delta^{-9/2}$ 宽界；完整负段仍单峰，
密度比仍小于 $2^{132}\delta^{-2}$。
所以原两根、严格段、mean 与完整两迹证明在新系数上给
$$
 K_j^{\rm ref}=2^{5000}(j+4)^5\delta_j^{-10}. \tag{C.15}
$$
这只是新径向参考 Cauchy 界；它不授予更新后的全网络逆。

## 5. 完整非线性局部图与含 mean 的真实小球

实际内向 Darboux 方程始终是原 R72 (2.4)--(2.7)；
必须保留
$$
 \kappa_y=
 \big(\Pi_J[\rho_D(1+n_{\rm ph})]\Pi_J\big)^{-1}
       \Pi_J(\rho_D\mathscr G_+),\qquad M=1. \tag{C.16}
$$
没有交换压缩逆与投影，没有清零初始或全程 mean。
$|p_*|$ 的单调性和准确端值给
$$
 \int(1+|\lambda|)(1+|p_*|^{-2})dy<128\delta^{-2}. \tag{C.17}
$$
这是把原64放宽2以覆盖复形状的虚部变差。因此完整源的
二次范数和二次差分别仍由
$2^{25}Z^2/(\mu\delta^2)$、
$2^{27}Z_0\|\Delta W\|/(\mu\delta^2)$ 控制。

同一实际 Galerkin 角窗
$$
 J=4\left\lceil4096(1+|\log\delta|)/h\right\rceil
 \le2^{-5}\delta^{-3/8},\quad Jh/4\ge4096(1+|\log\delta|)
 \tag{C.18}
$$
仍合法。由 (C.12) 齐次强范数小于 $2^{157}h^{-5}B$。
取
$$
 Z_0=2^{158}h^{-5}B,\qquad
 R_j^c=2^{-352}\mu_j\delta_j^2h_j^5J_j^{-5}. \tag{C.19}
$$
有限积分方程的 Lipschitz 费用不超过
$2^{140+27+158-352}=2^{-27}$。
mean 小根与压缩 leading 逆的相对量小于
$2^{19+158-352}J^{-5}=2^{-175}J^{-5}$。
真实小球由此先得到支付。

完整强迫修正保留原残差：
$$
 V_y=\mathcal F(W_{\rm app}+V)-\mathcal F(W_{\rm app})-(0,e).
 \tag{C.20}
$$
仍是九段，只在四条 log 过渡支付 $\sup|b|$。
平移保持平台总长，形状附加变差在常数中另付。
完整强增益可取
$2^{48}e^{480c_{\mathsf K}}\delta^{-2890}$；
残差可取
$S_e<2^{184}\delta^{-7/2}h^{-5}B e^{-Jh/4}$。
$c_{\mathsf K}<175$ 且
$e^{480c_{\mathsf K}}<\delta_j^{-16}$ 对 $j\ge8193$ 真实成立：
以 $\log2>2/3$ 即有
$480\cdot175\cdot(3/2)=126000<16(8193+3)$。

所以全部 physical 强修正小于
$2^{240}\delta^{2373/2}h^{-5}B$。
剩余角宽换回 canonical 两迹后可取
$$
 L_{\rm corr}^c=2^{248}\delta^{4743/4}h^{-5}. \tag{C.21}
$$
以 (C.19) 与 $w_{\min}\ge\mu\delta/640$ 比较，
相对强修正小于
$640\,2^{-112}\delta^{2375/2}J^{-5}<10^{-6}/4$。
因此完整全角解始终留在真实正分支。

输出 Duhamel 的真实角宽使用
$2^{140}\sup M^4e^{-hM/4}<2^{153}h^{-4}$。
有限二次项和 Lipschitz 费分别小于
$2^{494},2^{496}$ 乘 $(\mu\delta^2)^{-1}h^{-14}$。
全纯强修正减去其真实一次项后，Cauchy 二次费与
$2^{500}(\mu\delta^2)^{-1}h^{-14}$ 的比至多
$2^{79}\delta^{9471/8}<1$。
故完整零 residual 局部 map 满足
$$
 \Phi_{j,\Pi}:B_{\mathcal A_{\tau+h}}(R_j^c)\longrightarrow
 \mathcal A_\tau,\qquad
 \|\Phi_{j,\Pi}(U)\|<2^{158}h^{-5}\|U\|,
$$
$$
 G_j^c=2^{512}(\mu_j\delta_j^2)^{-1}h_j^{-14}. \tag{C.22}
$$
$G_j^c$ 控制 $R_j^c/4$ 上的完整二次余项及二次差，常数与
绝对角宽 $\tau\ge0$ 无关。方程给完整物理二 jet 和相对四态
$(P,K,U,V)$ 的安全界
$$
 \|v\|_{C^2_{r,\theta},\mathcal A_\tau}
 <2^{200}\delta^{-4}h^{-5}\|U\|,\qquad
 \|(P,K,U,V)\|<2^{200}(\mu\delta^2)^{-1}h^{-5}\|U\|.
 \tag{C.23}
$$
这些包含完整 mean；独立高度常数只在最终统一积分时加入。

## 6. 同一全标签、全部高块与两个接缝

保持
$$
 \zeta_j=\epsilon\delta_j^{39/4}\ (j\le8192),\qquad
 \zeta_j=\epsilon\delta_{8192}^{-485/4}\delta_j^{131}\ (j>8192),
$$
$$
 h_j=9/100\ (129\le j\le4096),\qquad h_j=8\delta_j^{1/256}
 \ (j>4096),\qquad\tau_{128}=5177/400,
$$
$$
 X_{m,j}=(-1)^j\zeta_j^{-1}e^{M\tau_j}V_{m,j},\quad
 A_{m,j}=-d_je^{-Mh_j}B_{m,j},\quad
 d_j=2^{-39/4}\ \hbox{或 }2^{-131}. \tag{C.24}
$$
真正低窗仍是前篇 U.4：
$$
 \widehat M_j=\min(2^{-5/4}\delta_j^{-1/8},M_*)\ (j\le8192),
 \quad \widehat M_j=2^{-40}\delta_j^{-1/8}\ (j>8192),
 \quad M_*=2^{-40}\delta_{8193}^{-1/8}. \tag{C.25}
$$
这也给后来 moving-middle 使用 $M\ge\widehat M_j$ 的准确
分类；一个频率只进入低区一次。

未改有限前缀的所有真高块不变。新深段用 (C.14)；
在 $M=M_j^{\rm new}$ 处
$\log_2(Mh/2)>954$，正的多项式对数费小于 $2^{34}$。
频率导数及层导数仍由
$312/(1+M)<h/4$、$39/1024<1/16-1/256$ 给严格负号。
因此全部真实高区仍有 $\|A_{m,j}\|<1/4$。

低区仍用同一理想特征基和两个原接缝 $Q_1,Q_2$。
所有 scalar Green、future 小分量和两行接缝消元完全相同；
特别第二接缝须先用第一行消去 $a_{8193}u_{8193}$，不另乘
一个大主因子。参考 $\|\mathcal G_0\|\le2^{15}$、
$\|\mathcal H_0\|\le8$ 继续成立。

(C.11) 给新深段规范误差
$$
 e_j\le2^{141}\sqrt{\delta_j}\big(8/(eh_j)\big)^8 .
 \tag{C.26}
$$
首层 $2^{15}e_j<2^{-3600}$，以后按 $\delta^{15/32}$ 改善。
未改浅端仍为 $q_G<.024998080<1/32$。
因此实际 Neumann 反演给 (C.1) 的 $\mathcal G,\mathcal H$；
每个高模的真实两行都保留。

局部 Taylor 的强卷积提升仍为 $2^{10}$，因为完整局部 map、
mean 小根和压缩逆都与角平移交换。
这里不是以 $\sup\sum$ 替换 $\sum\sup$。
首新层的严格粗二进制上界为
$$
 \log_2(\zeta_j/R_j^c)<-19689,\qquad
 \log_2(2^{26}G_j^c\zeta_j)<-19542, \tag{C.27}
$$
其层导数为负。未改前缀仍占主导，故
$$
 16e\sup_j\zeta_j/R_j<1,\qquad
 K_*:=2^{10}\sup_jG_j\zeta_j,\qquad2^{16}K_*<2^{-52}.
 \tag{C.28}
$$
真正全角固定点
$X=\mathcal H_\Pi a+\mathcal G_\Pi\mathscr R_\Pi(X)$
于是给 (C.1)。各胞是完整零 residual 解，metric/germ 相同，
两阶高度迹由 PDE 匹配。没有遗漏所有 high labels，
也没有把每胞 mean 当作另一个可指定变量。

## 7. 平端、完整参数依赖及两个全局因子

新深段的物理二 jet 包络是
$$
 2^{200}\epsilon\delta_{8192}^{-485/4}
               \delta_j^{127}h_j^{-5}\|X\|_{\mathcal X_\beta}.
 \tag{C.29}
$$
它趋0，背景由 (C.7) 趋0，故真解 $C^2$ 接平盘。
只剩一个整体 mean 高度常数。实共轭、四重周期、偶反射和
相位平移均由完整解的唯一性保持。

在端点/强标签 Banach 空间中，对全部复参数统一收缩给全纯
依赖。实内盒距离复外盒的归一化方向范数可取
$$
 \|\dot\Pi\|_*=
 \max(2^{16}\|\dot\gamma_1\|_\infty,\,
      2^{30}\|\dot\gamma_2\|_\infty,\,16\|\dot s\|_\infty,\,
      2^{21}\|\dot\Xi\|_{\ell^\infty(C^4_x)}).
 \tag{C.30}
$$
Cauchy 给同一方向的完整参数导数
$$
 \|D_\Pi^qX[\dot\Pi^q]\|_{\mathcal X_\beta}
 \le16q!\|a\|_\beta\|\dot\Pi\|_*^q,\qquad q\ge1,
 \quad\|D_aX\|<10. \tag{C.31}
$$
一般多线性方向可再用极化。这些是整个真尾图的导数，含 mean
与所有端口反馈；并非只对理想低图求导。
在固定物理径向坐标的 $C^2$ 空间中仅作已证的连续性声明。

乘积拓扑连续性用 (C.26) 的规范误差趋0、真实高块的超指数
尾以及 $G_j\zeta_j\to0$；不从未归一的
$M^8\sqrt\delta$ 在整低窗推出 uniform 收敛。
各有限坐标 $\Xi_j$ 使用 $C^4$ norm 收敛，再由统一深端包络
得到全局物理 $C^2$ 收敛。

相对状态仍准确含
$$
 N_j^c=2^{200}h_j^{-5}
 \delta_{4096}^{-3/2}\delta_{8192}^{-485/4}
                         \delta_j^{249/2},\qquad j>8192.
 \tag{C.32}
$$
两个全局逆幂没有删除。由原全前缀分段求和账与 (C.15)，
$$
 \sum_{j\ge129}(K_j^{\rm ref})^2N_j^c<2^{160016}. \tag{C.33}
$$
深段只比原 $2^{160000}$ 多 $2^{16}$；前缀没有变。
这仍只是明定的参考平方乘状态账，不授予同宽相对逆。

## 8. 真第四允许线、raw404 与逐点 regular 重选择

(C.11) 除以真实大根 $\Lambda>\mathsf K M^4/16$，
连同完整基转换给
$$
 \|{-E^{-1}BE}-\operatorname{diag}(\Lambda,\lambda)\|/\Lambda
 <2^{149}M^4\sqrt\delta\le2^{-11}. \tag{C.34}
$$
所以原 raw 权证明的真实窄锥、两个接缝和向浅下界重获。
新深起点仍为 $\lceil320+8\log_2M\rceil$；
新增高块一律使用真矩阵。全模实际逆的安全粗数由原
$2^{600}$ 改为 $2^{640}$。

当 $M>M_*$ 时 $x=\log M>600$。所有新增坏前缀的每频
对数费用可被
$(100000x+300000)e^{-x}<1/1000$ 控制；
它在 $x\ge600$ 递减。原
$40763493/1310720$ 加此数仍小于32。
总角宽也不超原358：常宽总和为357.12，深宽和小于1/16，
且每个真实 $\beta_j$ 或 $\beta_j^c<h_j/1024$。
因此单位真标签列 $u_m=H_{m,\Pi}(128)$ 的实际 raw 权仍有
$$
 \boxed{\quad
 1/9<\mathfrak w_{m,\Pi}:=\|u_m\|_\infty^{-1}<e^{391M},
 \qquad \tau_{128}+391<404.\quad} \tag{C.35}
$$
这是新 profile 的全频权，含完整坏前缀。

深处真实 Möbius 管和第四线仍严格在 $|s|<1/16$。
前8064个胞元129--8192完全相同，逐胞导数小于 $2^{-24}$，
故新线相对固定同一 $\Gamma$ 的第47束双参数强尾的 cut128 物理斜率差仍小于
$$
 2^{-193532},\qquad14<d_{4,\Pi}<15. \tag{C.36}
$$
对每个固定实 $\Pi$，重新停止最后 $q=-1$ connector。
准确 $H_e\omega_e$ 不变量保留 $\epsilon_{\rm tail}$；
停止变化小于 $2^{-193537}$，尺度按真实指数缩放。
固定物理 $a$ 时仍须用
$$
 Z(a)=Z_e-\int_{a_e}^{a}w(s)\,ds,\qquad
 \delta Z=\delta Z_e+w_e\delta a_e-\int_{a_e}^{a}\delta w(s)\,ds .
 \tag{C.37}
$$
移动端项不删除。

随后用本篇新无限允许线重新应用 R11 全模坏集证明。
其真实好集测度仍至少 $1-83/16384$；选择一个实际好参数后，
同一 $a_*,z_*,\omega,B=2^{24}-25/8,L=\omega B$ 给
$$
 |\lambda_m+M\omega|<2^{41}M\omega e^{-2ML},\qquad
 \lambda_4=-4\omega,\qquad m/7<\gamma_m<m/5,\quad\gamma_0=0,
 \tag{C.38}
$$
其中最后的 $m/7,m/5$ 按正 $m=M$ 读取。
$\gamma_m$ 由完整 grounded 两迹的原有理公式定义。
这是每个固定 $\Pi$ 上的真实重选择；没有宣称该外好参数
具有尚未证明的全参数连续或解析选择。

新的 raw404、真实 good angle 和有限 connector 盒重新满足
原 Schur1850 的全部输入，所以对这个实际径向零标签对象，
$$
 \|(\mathsf D_{0,\Pi})^{-1}g\|_{\ell^1_\beta}
 \le \tfrac1{16}\|g\|_{\mathfrak Z_{\beta+1850}},\qquad
 \mathsf D_{0,\Pi}a=k_B^{\rm lin}+M\coth(ML)f_B^{\rm lin}.
 \tag{C.39}
$$
原 R74 合法线性外输入于是再次有
$\|a^{\rm lin}\|_{224}\le e^{-33545404}\sum A_m$。
这不把新非线性 $\mathcal F_c$ 的余项清零，也不把有限次
解析 Newton 迭代称为其收敛。

## 9. 完整 ordinary/weak 源的 canonical 总通量

固定本篇新径向参考，取 $t=\log r$、raw 高度 $h=\rho H$，
$$
 \mu_0=w/(\rho r)=\mu_jp_*/(\rho r^8),\qquad
 (\mu_0h_t)_t+\mu_0Qm^2h=f-(F^t)_t-imF^\theta .
 \tag{C.40}
$$
定义总通量 $\pi=\mu_0h_t+F^t$。完整两态使用
$$
 \widetilde W_1=\nu_mH/r^4,\qquad
 \widetilde W_2=
 \frac{p_*}{\sqrt{12}r^4}(H_t-m^2H)
                 +\frac{r^4}{\sqrt{12}\mu_j}F^t .
 \tag{C.41}
$$
直接代入，不对 $F^t$ 微分，得到
$$
 \widetilde W_y=A_p\widetilde W+\mathcal J_m,\qquad
 \boxed{\quad
 \mathcal J_m=
 \begin{pmatrix}
 -\nu_m r^4F^t/(\sqrt{12}\mu_jp_*)\\
 r^4(f-imF^\theta+m^2F^t)/(12\mu_j)
 \end{pmatrix}.\quad} \tag{C.42}
$$
准确变换矩阵的行列式为 $\nu_m/(\sqrt{12}\rho\mu_j)$，
所以没有漏掉第二条物理迹。胞元接缝仍把第二行除以 $c_j$；
总通量连续时这与真实物理拼接一致。

对 ordinary 源 $f=w^2e,F=0$，(C.42) 正好还原
$$
 \mathcal J_m=(0,N_m),\qquad
 N_m=\mu_jp_*^2e_m/(12r^{10}).
 \tag{C.43}
$$
两个 $p_*$ 因子都保留。

令 $\mathcal S_{1,\beta}^w$ 为
$$
 \sum_{m\ne0}(1+M)^{312}
 \sup_{j>128}\frac{e^{M(\tau_{j-1}+\beta+\beta_j^c)}}{\zeta_{j-1}}
                \int_{I_j}\|\mathcal J_m(y)\|_\infty\,dy ,
 \tag{C.44}
$$
未改层将 $\beta_j^c$ 换回原 $\beta_j$。
完整有源 endpoint 残差与强标签解满足
$$
 \|f_{\rm end}\|_{\mathcal F_\beta}\le2^{482}\mathcal S_{1,\beta}^w,
 \qquad
 \|X\|_{\mathcal X_\beta}
 <9\|a\|_\beta+2^{498}\mathcal S_{1,\beta}^w . \tag{C.45}
$$
这是 full vector 源；不是把 weak 源变成 $F^t_t$ 后隐藏其范数。

mean 必须另按原物理变量读取：
$$
 (\pi_0)_t=f_0,\qquad
 (H_0)_t=(r/w)(\pi_0-F^t_0),\qquad
 \pi_0(t)=\int_{t_f}^t f_0(s)ds . \tag{C.46}
$$
独立高度 $\lambda=H_0(t_f)$ 保留。
若这些积分收敛，它们定义真实 mean；若要 $C^2$ 平端，
还须这些输入积分及 $(r/w)F^t_0$ 的所需一阶径向范数满足
相应平端衰减。仅 $L^1$ weak 源不授予 bare flux 的端点迹
或整个 $C^2$ 重建。

对 ordinary 源，使用原完整
$\mathcal S_{1,\beta},\mathcal S_{2,\beta}$（含 $m=0$），后者
为 $\sum_m\sup_j\delta_j^4\zeta_j^{-1}
e^{M(\sigma+\beta)}\sup|N_m|$，$\sigma=\tau_{128}-1$。
mean 的绝对账不依赖新旧 $p_*$ 的逐点比较：
$\int|N_0|\le\zeta_{j-1}\mathcal S_1
\le2^{10}\epsilon\delta_j^{39/4}\mathcal S_1$，
(C.6) 与深向几何和直接给
$$
 |\pi_0|\le2^{13}\mu_j\epsilon\delta_j^{39/4}\mathcal S_1,\quad
 |H_{0,t}|\le2^{22}\epsilon\delta_j^{35/4}\mathcal S_1.
$$
用 (C.40) 再微分一次，直接源项由
$\sup|N_0|\le\epsilon\delta_j^{23/4}\mathcal S_2$ 支付，
因此 mean 的完整二 jet 小于
$2^{40}\epsilon\delta_j^{19/4}(\mathcal S_1+\mathcal S_2)$。
非mean 的原 source-to-physical 换算只用 (C.6)、(C.14) 和
实际 $Q$ 界，给包括 mean 的安全总界
$$
 \|H-\lambda\|_{C^2_{r,\theta},\mathcal A_{\sigma+\beta}(I_j)}
 <2^{512}626^{313}\epsilon\delta_j^{19/4}
       (\|X\|+\mathcal S_1+\mathcal S_2).
 \tag{C.47}
$$
连续 ordinary 源下，各接缝二阶迹按真实方程匹配。
(C.47) 不通过一条不存在的新旧 profile 点态单调比较取得。

给任一真正齐次测试解 $q_m$，实际 Wronskian 恒等式是
$$
 \partial_t[q_m\pi-\mu_0(q_m)_t h]
       =q_m f+(q_m)_tF^t-imq_mF^\theta . \tag{C.48}
$$
这完整保留 weak 法向项、角向项和两端总通量。
把它沿实际有向 connector 换元后才能读取外 affine Robin；
不能漏掉物理 Jacobian 或将内向、外向的号混用。
bare flux 等于 $\pi-F^t$，所以任何要求 bare Airy 两迹的
消费者须另给 $F^t$ 的真实端点迹。

## 10. 控制方向的真实源和不能删除的 mean 积分

在固定物理 $t$，写 $\psi=\delta\log p_*$。
形状方向是 $\delta\Xi$；下降坡平移方向准确是
$$
 \psi_{\rm slide}=(Q-7)\delta\ell
 \tag{C.49}
$$
于整个移动坡，窗口外为0，另加原两个 bump 的方向。
该式包括当前 $\Xi$，不是只在原 quintic 上使用。
这里先固定局部径向坐标和高度尺度 $\rho$，然后才作外 connector
的尺度重参数化。因此
$$
 \delta Q=-\psi_t,\qquad
 G=\mu_0\operatorname{diag}(1,-Q),\qquad
 \delta G=\mu_0\operatorname{diag}(\psi,\psi_t-Q\psi).
 \tag{C.50}
$$
径向参考 Jacobi 解的 metric 方向满足
$P\,\delta h=-\operatorname{div}(\delta G\nabla h)$，
可以直接作为 (C.42) 的 weak 源输入。
若同时改变外尺度或使用移动物理切口，须先取真实
$\chi=\delta\mu_0/\mu_0$、$\dot Q$，并使用一般式
$\delta G=\mu_0\operatorname{diag}(\chi,-Q\chi-\dot Q)$；
不得将含 $\delta\rho$ 的变分仍写成固定尺度的 (C.50)。
相应高度端项由 (C.37) 保留。
没有 $F^t_t$ 范数，也没有删掉改变的 mean 电阻
$$
 \delta\int\mu_0^{-1}dt=-\int\psi\mu_0^{-1}dt . \tag{C.51}
$$
在非零背景必须微分完整 Darboux 方程及其 mean 根；
(C.31) 是已付的全图导数，不能把 (C.50) 的径向系数直接
冒充非径向 Jacobi 系数。

最终几何高度仍按 (C.37) 及唯一 $\lambda$ 重建。
平移或形状控制保持两个 phase，并不使平均高度、总通量、
metric-source 或端口密度自动不变。本文将这些列保留为
后续全 Schur/非线性闭合的真实输入。

## 11. 证据与后续权限

原强尾、R72 完整局部方程、原九段强修正和第52束实际控制的
依赖身份列在新的程序与报告中：
[scripts/fourfold_controlled_profile_full_label_20261114.js](../scripts/fourfold_controlled_profile_full_label_20261114.js)
及[严格预算](../notes/2026-11-14-R119-controlled-profile-full-label-budget.json)。
程序是本次纯 JavaScript / BigInt 有理实现，实际执行；
不声称恢复了任何丢失的 Python native。
它核实际低窗余量、完整有序乘积费、局部球、两全局逆幂、
全深层单调门、raw 前缀余量和 weak 两态单位恒等式。
全频和全层量词由以上解析证明给出，不由有限模采样代替。

已得新实际全图、原 Mhat 分类、两迹/mean/source 合同和逐点
regular 径向入口。第52束的有限共振非恒零以及后续量化核
只能在其准确范围内消费；它们仍不自动解完整非径向
$\mathcal F_c$，也不替代原同权内部 Green 的 source 控制。
