# R119 续篇：新外两根分量与全部 principal 返回的同一无限联立 KAM

2026-11-14，visible-exact / tail_connector。

**状态：解析证明，提交独立核对。** 本篇针对新的 fixed-stop simple-root 对象，将原来在 cut128 截断的 $(129,2)$ 分量加入真正两根返回的指标集。新根为 $e_0$，原另一根为 $e_X$。真实路径是 $e_X\to\mathrm{cut128}\to e_0$；其新增径向相位完整计入新的固定目标，不取旧未覆盖分量的相位值。

全部内部行与新增的一行在同一个无限参数方程内求解。完整平均行、所有角 Fourier 模、第二 $\Gamma$ 参数以及原始标签依赖均保留。所得是实际 principal 返回的共轭和第一参数反项；完整 $1/M$ 密度相位、有限频段的五盒选择及闭 PDE 逆仍须继续。

## 1. 同一新对象、全部控制和实际枚举

使用已经证明的

- [新固定 stop 对象及完整转移门](../notes/2026-11-14-R119-simple-root-fixed-stop-new-object-and-transfer-gates.md)，记为 S；
- [新 simple 根的完整解析图和源](R119-supplement-new-fixed-stop-simple-root-full-analytic-chart-and-sources.md)，记为 A；
- [新根的完整正区 DN、Airy 返回和源](R119-supplement-new-simple-root-complete-positive-DN-Airy-return-and-sources.md)，记为 P；
- [受控全标签的实际联立双相位](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)，记为 N；
- [浅前缀五盒重建](R119-supplement-shallow-five-cube-family-and-all-frequency-radial-selection.md)，其实际文本的第2--4节和 (P.5)--(P.9)；
- [强首剪切实际 KAM](R119-supplement-stronger-tail-joint-actual-return-KAM.md)，记为 K。

新完整集合为
$$
 \mathcal I_+=\{(j,k):j\ge129,\ k=1,2\},\qquad o=(129,2).
 \tag{O.1}
$$
除 $o$ 外，区间及两端 root germ 与原集合完全相同。对 $o$，区间 $I_o$ 的两端是 $e_X,e_0$，而 cut128 是其严格负型内部截面。新的 $\ell^0,\rho,H_e,\omega_e$ 固定；对所有控制参数 $D\ell^0=0$。

每个下降坡的两个原 bump 仍为
$$
 \psi_1=64z_1^3(1-z_1)^3,\quad z_1=8(x-1/4),\qquad
 \psi_2=64z_2^3(1-z_2)^3,\quad z_2=32(x-3/16),
 \tag{O.2}
$$
分别零延拓于 $[1/4,3/8]$、$[3/16,7/32]$ 外。复半径仍为 $2^{-15},2^{-29}$。新增外侧浅形状 $\Xi_o\in C^4_0(7/16,15/32)$ 的复半径为 $2^{-79}$；其实际五坐标子族也在此球内。其余已安装形状与平移控制保持原来已付的域。

S.20、S.25 已重新构造包含 $o$ 两 bump 和形状的完整图，且所有 root germ、平台和两阶接缝 jets 未变。这里不是把原“完整内部集合”的量词直接扩大。

继续用原标签与真实状态
$$
 A_*=2^{-262148},\qquad \|a\|_{224}<A_*,
 \quad \bar a=\|a\|_{224}/A_*,\quad
 \mathcal X=16\|a\|_{224}.
 \tag{O.3}
$$
最终反演使用的更小域 $\mathcal X\le2^{-8388608}$ 是此域的子域。全部结论首先是所显示图上的结论，不把未解决的 nonlinear 匹配余项设为零。

## 2. 外两根之间的完整积分，不沿用短胞元长度

令 $t=\log a_{\rm phys}$，$Q=-A_{\rm metric}\ge0$ 于 $I_o$。在 $e_X$ 至 cut128，原实际密度恒等式为
$$
 (\log\mu_0)_t=-1-Q,\qquad
 \mu_0=C_{\rm phys}\delta_{129}^{6}p_*(r)r^{-8}.
$$
这里 $1\le r\le2$、$\delta_{129}/2<p_*<64/\delta_{129}$，故任意端点之比小于 $2^{15}\delta_{129}^{-2}$。这包括原根本身，不只包括根外的 strict 切口。因此
$$
 \int_{e_X}^{\mathrm{cut128}}(1+Q)\,|dt|
 <281\log2,\qquad \delta_{129}^{-1}<2^{133}.
 \tag{O.4}
$$
用绝对弧长定向书写不会改变该正积分；上述密度单调恒等式按从负片内端至外端的真实 $t$ 方向取值。

新对象的剩余负片由 $q=-8$ 平台和 $q(v)=2-10S(v/\eta)$ 的负型部分组成，$A_{\rm metric}=q+1$。S.6--S.10 给平台长 $\ell^0<1/12$、$\eta=2^{-24}$，在此段 $0\le Q\le7$。因此
$$
 \int_{\mathrm{cut128}}^{e_0}(1+Q)\,|dt|
 <8/12+8\,2^{-24}<\log2.
 \tag{O.5}
$$
最后一门可由
$\log2=2\sum_{r\ge0}(1/3)^{2r+1}/(2r+1)>2/3+2/81$
直接核对。于是完整新区间满足
$$
 \int_{I_o}(1+Q)\,|dt|<282\log2,\qquad
 \int_{I_o}(1+\sqrt Q)\,|dt|<423\log2<2^9.
 \tag{O.6}
$$
第二式使用 $1+\sqrt Q\le3(1+Q)/2$，并确实用了实负片上的 $Q\ge0$。

实 $\Gamma_1,\Gamma_2,\Xi_o$ 的支集均在下降坡严格内部。其对第一积分的改变量准确是
$-\int\partial_t(\gamma_1\psi_1+\gamma_2\psi_2+\Xi_o)\,dt=0$；
支集外的两个根及端值完全不变。实 $Q$ 在这些支集仍严格正，故 (O.6) 对整个实盒成立。

复参数不把该有符号恒等式冒作绝对值界。支集上实际
$Q_0\ge(\sqrt{12}\Delta/\eta)/2$，而变动的相对模小于 $1/32$。
用同一正根的解析延拓和
$$
 \sqrt{Q_\Pi}-\sqrt{Q_0}
   ={Q_\Pi-Q_0\over\sqrt{Q_\Pi}+\sqrt{Q_0}}
$$
逐支集积分。$\int|\psi_{s,x}|dx=2$，且
$\int|\Xi_x|dx\le\|\Xi\|_{C^1}/32$，给
$$
 \int_{I_o}|\sqrt{Q_\Pi}-\sqrt{Q_0}|\,|dt|
 <4\bigl(|\gamma_1|+|\gamma_2|+\|\Xi_o\|_{C^1}\bigr)
                         \sqrt{\eta_{129}/\Delta_o}<2^{-12}.
 \tag{O.7}
$$
支集外平方根准确未变，包括两个可积零点。这同时支付参考平移的虚部和复参数下的 $\int(1+|\sqrt{Q_\Pi}|)<2^9$，没有绕过复平方根分支或使用 $\int(1+Q)$ 控制任意复 $Q$。

## 3. 新基点相位、真实局部逆和第二参数域

定义新外分量自己的完整径向相位
$$
 \Theta_o(\gamma_1,\gamma_2,\Xi_o)
       =-2\int_{I_o}\sqrt{Q_\Pi}\,dt,\qquad
 \Omega_o^0=4\Theta_o(0,0,0).
 \tag{O.8}
$$
新平台和新根附近的积分均包含于此。旧截断分量的相位数不能代入 $\Omega_o^0$。

令
$$
 \Delta_o=|\log\delta_{129}|-\log64,\quad
 \kappa_o=2^{-25}\sqrt{\eta_{129}/\Delta_o}.
$$
两个 bump 与 $\Xi_o$ 的支集两两相离，故准确有
$$
 \Theta_o=\Theta_o(0,0,0)
            +\theta_{1,o}(\gamma_1)
            +\theta_{2,o}(\gamma_2)+\theta_{\Xi,o}(\Xi_o).
 \tag{O.9}
$$
这不仅是线性化身份。每个积分在其自己的支集变化，其他积分准确固定。

第一导数仍是原完整度量参数证明的实际局部积分：
$$
 \theta_{1,o}'(\gamma_1)
  =-\frac12\int
      {\psi_1(A_t+\gamma_1\psi_{1,tt})\over
                 (-A-\gamma_1\psi_{1,t})^{3/2}}\,dt.
 \tag{O.10}
$$
原 (M.8)--(M.15)、K.9--K.12 的分母、积分面积和复差商在本支集逐字不变，因而
$$
 \theta_{1,o}'(0)>2^{-8}\sqrt{\eta/\Delta},\quad
 \left|\theta_{1,o}'(\gamma_1)/\theta_{1,o}'(0)-1\right|<1/8,
$$
$$
 \theta_{1,o}(G_o(\lambda))=\lambda,\quad
 |\lambda|<2\kappa_o,\quad
 |G_o'|<512\sqrt{\Delta_o/\eta_{129}}.
 \tag{O.11}
$$
这个逆由同一复盘收缩构造，不依赖区间其余部分长度。

固定一个 $|\bar\gamma_{2,o}|<2^{-85}$，保留全部第二参数增量
$|q_o|<2^{-34}$，令 $\gamma_{2,o}=\bar\gamma_{2,o}+q_o$。
用 (O.7) 的局部推导而不计第一支集，得到
$$
 |\theta_{2,o}(\gamma_{2,o})+\theta_{\Xi,o}(\Xi_o)|
 <4\bigl(|\gamma_{2,o}|+\|\Xi_o\|_{C^1}\bigr)
                                      \sqrt{\eta/\Delta}
 <\kappa_o/32.
 \tag{O.12}
$$
这里 $|\gamma_{2,o}|<2^{-33}$；常数余量还覆盖 $\Xi_o$ 的 $2^{-79}$。以后只要新的径向第二参数基点在显示盒内，这个同一结论即可消费；本篇尚未选择它的完整次相位目标。

在标签之前，一次选定
$$
 |\omega_o-\Omega_o^0|<\kappa_o/64,\qquad
 |e^{in\omega_o}-1|>{\kappa_o\over4096|n|}
                       \quad(n\ne0).
 \tag{O.13}
$$
例如直接使用原实际完整相位算术证明 Q.2--Q.6 的连分数构造，输入改为本篇的 $\Omega_o^0,\kappa_o$。这是一项明确的实数定义，不是有限采样；不需要为新目标执行旧数值源。

令主反项坐标 $\|p\|_{\mathcal P}=\sup_i|p_i|/\kappa_i<4$。
外行第一物理参数准确定义为
$$
 \gamma_{1,o}(p_o,q_o,\Xi_o)=
 G_o\!\left({\omega_o-\Omega_o^0+p_o\over4}
           -\theta_{2,o}(\bar\gamma_{2,o}+q_o)
           -\theta_{\Xi,o}(\Xi_o)\right).
 \tag{O.14}
$$
括号模小于 $(1+1/256+1/32)\kappa_o<2\kappa_o$。
因此整个原盘4仍合法；复第一参数在原 $2^{-15}$ 盒内。实 $p_o=0$ 时更有 $|\gamma_{1,o}|<2^{-19}$。原内部行继续用受控证明 N.5 的真实径向曲线和同一个 phase 坐标，不重置其已固定的目标。

## 4. 外行的完整状态、真两支流和角域

在原无限尾上统一采用已经支付的受控权
$$
 N_j^c=2^{200}h_j^{-5}{\zeta_j\over\mu_j\delta_j^2}
                         =2^{16}N_j,\qquad
 (N_j^c)^\#=N_j^c+\mathbf1_{j\ge130}N_{j-1}^c.
 \tag{O.15}
$$
它保留原两个全局逆幂和真实规范接缝。对外尾片，完整四态 norm 小于
$4N_{129}^c\mathcal X$；原 X.1--X.7 已给 $N_{129}<2^{-30}$。
对新 connector，S.25 的完整 balanced 四态小于
$n_0=2^{-447}\mathcal X$。两者统一可取
$$
                         n_o=2^{-12}\mathcal X.
 \tag{O.16}
$$
这里没有拿原内部两胞元长度代替新 connector，也没有把 mean 状态投掉。

实际两支 principal 特征流仍是
$$
 \partial_tF_\sigma(t,\theta)
 =-d(t,F_\sigma)-\sigma\sqrt{Q_\Pi(t)}\,v(t,F_\sigma),
 \quad F_\sigma(t_-)=\mathrm{id},\qquad
 R_o=F_-^{-1}\circ F_+,
 \tag{O.17}
$$
其中 $d=E(V-P)/J_0$、$v=\sqrt{\mathfrak d}/J_0$，完整 $K$ 含原 holonomy mean。
原全标签图和新 S.25 的角余宽均超过3。
在物理宽3上，商式、平方根与一次角导的共同界可保守取
$$
 |d|+|v-1|+|d_\theta|+|v_\theta|<2^8n_o .
 \tag{O.18}
$$
尾片原 K.13--K.16 的对应界是 $32n$；新根 A 的原商式及 P.17 所用 drift 门在 connector 给相同的 $2^8n_0$ 宽界。这里仅角微分，不要求根处 $q_t$ 有界。

减去准确参考平移 $-\sigma\int\sqrt{Q_\Pi}\,dt$。由 (O.6)--(O.7)，余项积分及其角 Lipschitz 积分各小于 $2^{17}n_o$。在宽 $7/4$ 的位移球上 Picard 迭代给每支正反流的偏差小于 $2^{18}n_o$；其空间导数离1亦小于同一数。所有被评价系数仍在宽2内：参考虚平移小于 $2^{-12}$，未知位移与逆流复合总消费小于 $1/8$。

两支复合后，在宽 $3/2$ 上得到准确实际 map
$$
 R_o(\theta)=\theta+\Theta_o(\gamma_1,\gamma_2,\Xi_o)+E_o(\theta),
 \qquad \|E_o\|_{\mathcal A_{3/2}}<2^{20}n_o.
 \tag{O.19}
$$
它对全部标签、全部第一/第二参数和控制联合全纯。接缝用原固定段坐标；这不声称粗 Sobolev pullback 在移动接缝上同宽全纯。

## 5. 加入外行后的实际小除数平方费用

置标准圆 $x=4\theta$。全部真实 maps 为
$$
 \mathcal R_{i,p,a,q,\Omega}(x)
 =x+\omega_i+p_i+f_i(p,a,q,\Omega,x),\qquad
 \|f_i\|_{\mathcal A_6}<\varepsilon_i\bar a .
 \tag{O.20}
$$
内部已付的受控状态给
$$
 \varepsilon_i=2^{24}(j+4)(N_j^c)^\# A_*
                       \quad(i\ne o).
$$
外行从 (O.16)、(O.19) 和标准圆因子4得到
$$
 \|f_o\|_{\mathcal A_6}
 <2^{22}n_o=2^{10}\mathcal X
              =2^{14}A_*\bar a,\qquad
                         \varepsilon_o=2^{14}A_* .
 \tag{O.21}
$$
所有 $f_i$ 都可依赖全部 $p$；没有把外行当作一个独立的一维迭代。

统一取 $\gamma_i^{\rm D}=\kappa_i/4096$，并使用较弱但足够的
$|e^{in\omega_i}-1|\ge\gamma_i^{\rm D}|n|^{-2}$。
原 K.19 的真实求和预算乘 $2^{16}$ 后为
$$
 \sup_{j\ge129}j(j+4)(N_j^c)^\#\delta_j^{-3/2}<2^{201}.
$$
由 $\kappa_i^2>2^{-55}\delta_j^{3/2}/j$，
$$
 \sup_{i\ne o}{\varepsilon_i\over(\gamma_i^{\rm D})^2}
 <2^{24+24+55+201}A_*=2^{304}A_* .
 \tag{O.22}
$$
外行的尺度单独核算，不以内部行常数替代：
$$
 \kappa_o^{-2}<2^{55}\,129\,\delta_{129}^{-3/2}<2^{263},
 \qquad
 {\varepsilon_o\over(\gamma_o^{\rm D})^2}<2^{14+24+263}A_*
                                                   =2^{301}A_* .
 \tag{O.23}
$$
因此整个新集合满足
$$
 \mu_+:=\sup_{i\in\mathcal I_+}
           {\varepsilon_i\over(\gamma_i^{\rm D})^2}
 <2^{305}A_*=2^{-261843}<2^{-64}.
 \tag{O.24}
$$
这里是加权 $\ell^\infty$ 行 norm，增加一行不会产生“窗口总数”因子。所有无限内部行的两个规范接缝和完整前缀都已包含于 (O.22)。

## 6. 同一个无限平均方程和所有 Fourier 行

为明确不是逐分量固定其他参数，逐步使用原 K.21--K.24 的完整 Newton 行。记当前标准角共轭为 $h_i$，
$H_i=h_i'\circ T_{\omega_i}$，误差为
$E_i=\mathcal R_i\circ h_i-h_i\circ T_{\omega_i}$。
令
$$
 C_i^h[\dot p]=(D_pf_i[\dot p])\circ h_i,\quad
 d_i^0=\langle H_i^{-1}\rangle,\quad
 B_i(\dot p)=\langle H_i^{-1}C_i^h[\dot p]\rangle .
$$
在整个 $\mathcal I_+$ 上一次求解
$$
 d_i^0\dot p_i+B_i(\dot p)=-\langle E_i/H_i\rangle .
 \tag{O.25}
$$
外行及它对所有旧参数的导数也在此矩阵中。
原盘4和角域6给完整 Banach 方向 Cauchy 界
$\|C_i^h[\dot p]\|\le\varepsilon_i\|\dot p\|_{\mathcal P}$，
故归一非对角平均行 norm 小于 $4\mu_+$，其 Neumann 逆小于2。代回每一行仍给逐行
$|\dot p_i|\le8e_n\varepsilon_i$，不把深层小尺度换成共同最大值。

随后对所有非零 Fourier 系数解
$$
 v_i-v_i\circ T_{\omega_i}
 =-E_i/H_i-(\dot p_i+C_i^h[\dot p])/H_i,\qquad
 \langle v_i\rangle=0 .
 \tag{O.26}
$$
(O.25) 使右边的 mean 准确为零。取
$d_n=2^{-n-4}$，准确线性化恒等式
$(\mathcal R_i'\circ h_i)h_i'=H_i+E_i'$
将余项归为 $E_i'v_i$ 与原复域控制的二阶 Taylor 项。
同一原证明给
$$
 e_{n+1}\le2^{14}\mu_+d_n^{-6}e_n^2,\qquad
 e_n\le\bar a\,2^{-8n}.
 \tag{O.27}
$$
于是所有行和全部非零角模同时收敛：
$$
 \mathcal R_{i,p^*,a,q,\Omega}\circ h_i
                  =h_i\circ T_{\omega_i},\qquad
 |p_i^*|<16\varepsilon_i\bar a,\qquad
 \|h_i'-1\|_{\mathcal A_{3/2}}<2^{18}\mu_+ .
 \tag{O.28}
$$
角宽极限和参数球余量与原证明相同。无限层极限由一致加权 norm 得到，不是“先做有限窗口再省略极限”。

由 (O.14) 或原内部径向逆回到真实第一参数。若
$\gamma_{1,i}^{\rm rad}$ 表示同一 $q,\Omega$ 下的径向曲线，则
$$
 |\gamma_{1,i}^*-\gamma_{1,i}^{\rm rad}|
       <2^{-14}{\varepsilon_i\over\kappa_i}\bar a .
 \tag{O.29}
$$
这是物理 $\gamma_1$ 的费用，不把它误认为 phase 坐标 $p$。
外行也完全按此式收费。实解严格留在原 $2^{-16}$ 参数盒。

## 7. 第二参数、两种 mean 和原物理源的身份

第二参数 $q$ 在整个构造中作为完整无限外变量保留。所得
$\gamma_1^*(a,q,\Omega)$ 对 $q$ 联合全纯，后续消去完整次相位时必须消费它的真实导数；不能把径向保持主角曲线的导数当成实际 $\Gamma^*$ 导数。所有真实参数圆盘的 Cauchy 费用都按其实际半径收取。

原物理角共轭是 $K_i(\eta)=h_i(4\eta)/4$。高度与 total 通量分别变为
$$
 H^{\rm new}=H\circ K_i,\qquad
 \pi^{\rm new}=K_i'(\pi\circ K_i),\qquad
 \int\pi^{\rm new}H^{\rm new}=\int\pi H .
 \tag{O.30}
$$
通量 mean 守恒；高度 mean 是真实的
$\langle H\circ K_i\rangle$，不删除两个 mean 后再恢复一个常数。
上式所用 $\pi=\mu(H_t-dH_\theta)+F^t$ 始终是 total 通量。

S.27--S.29 的完整源在新目标下保持同一身份。对任一真实参数方向，
$$
 \delta w=w\!\left(\sum_i\psi_{1,i}\delta\gamma_{1,i}^*
                 +\sum_i\psi_{2,i}\delta q_i+\delta\Xi\right),
 \quad
 \delta g_{aa}=2w\,\delta w,\qquad
 \delta Z_{\rm ref}(a)=-\int_{a_e}^{a}\delta w(s)\,ds .
 \tag{O.31}
$$
第二式的参考高度积分含 mean。$\ell^0$ 固定，所以没有旧重停的
$A\,\delta\ell$ 项；这来自准确 $D\ell^0=0$，不是删源。
$\Gamma^*$ 两列、原 $\nu$、ordinary/weak 两行及 bare weak 端迹仍在原各段 Duhamel/边界合同中。纯 principal 共轭没有新授“任意粗体源直接进入混合根图”的权限。

相邻 positive 组件以 (O.30) 的 dual pairing 搬运完整两端 DN 和两端源；非对角块保留。对外行使用已经证明的新 P 和实际长段 screening；独立的 $C_R$ 端口、mean $B_R$ 与实际 Robin 残差不因本篇 principal 共轭消失。

## 8. 相位轨道与此刻实际闭合的范围

标签角平移 $a_m\mapsto e^{im\varphi}a_m$ 使原完整图、两支流和每个误差仅按物理角平移共轭。径向控制、全部参数平均行及相同 Fourier 逆与该平移交换。从同一个初值归纳，
$$
 \gamma_1^*((e^{im\varphi}a_m)_m,q,\Omega)
                      =\gamma_1^*(a,q,\Omega).
 \tag{O.32}
$$
对原非零 Fourier 标签方向，零点的一阶不变泛函只能为0，故
$D_a\gamma_1^*(0)=0$。整体高度平移本来不改变 principal 系数；真实 flux/holonomy 行仍由原完整图决定。

至此，新两根分量 $o$ 的实际 principal 目标、完整物理角流、
第二参数外变量、第一参数真实反项和无限联立 KAM 已与全部旧行接在同一对象上。其新增有限桥费用已在 (O.4)--(O.24) 支付，未借用短胞元长度或旧三阶根。

下一项是新外分量完整密度首相位及两 $\Gamma$ 的联合消去。
新的径向 $\beta_o$ 必须包含两端 Airy connection 和新增 strict 段，
不能只借局部 Jacobian 就设成旧值；随后还须将真实五盒 generator、
完整 positive/negative/source 端口和原强标签权接入闭网络。
本篇不把一个 principal scalar 同调逆冒作这些尚未完成的逆。
