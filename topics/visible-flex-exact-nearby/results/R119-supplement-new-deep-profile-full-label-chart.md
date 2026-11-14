# R119 续篇：新深 profile 的真全标签 Green、完整 mean 与非线性尾图

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对前篇已经明确构造的 $J_*=4096$ 后
$c=16\sqrt2$ 新 profile，重新证明全部内部标签的强离散 Green
和零 residual 非线性尾图。包括原高模真实块、唯一特征基接缝、
完整 mean 小根和连续全角 PDE 修正。可取
$$
 \|\mathcal G^\dagger_\Gamma\|\le2^{16},\qquad
 \|X^\dagger_\Gamma(a)\|_{\mathcal X_\beta}
          <16\|a\|_{\ell^1_\beta},\qquad \|a\|_\beta<1/64.
 \tag{L.1}
$$
新相对状态在深端的估计明确带
$\delta_{4096}^{-3/2}$，没有将它略去。这里的强离散 source
是全部非mean canonical 端口残差；它不等于尚未付出的任意物理
普通源与 mean 负荷的完整 affine 外 DN。

## 1. 新对象、未改的规范和实际完整方程

完全采用
[新深 profile 与齐次 Robin](R119-supplement-new-deep-profile-and-actual-homogeneous-Robin.md)
的 $\delta_j,\eta_j,c_j,\mu_j,p^\dagger_\Gamma$。参数复盒取
$\|\Gamma\|_\infty<2^{-15}$，实盒取 $2^{-16}$。
令
$$
 \zeta_j=\epsilon\delta_j^{39/4},\quad
 h_j=9/100\ (129\le j\le4096),\quad
 h_j=8\delta_j^{1/256}\ (j>4096),
$$
$$
 \tau_{128}=5177/400,\qquad \tau_j-\tau_{j-1}=h_j,\qquad
 X_{m,j}=(-1)^j\zeta_j^{-1}e^{|m|\tau_j}V_{m,j}.
 \tag{L.2}
$$
$V$ 仍为每个截面的真实两分量 canonical 状态；新胞元输出
第二分量必须除以 $c_j$，已在前篇准确证明。
规范 $\zeta_{j-1}/\zeta_j=2^{39/4}$ 没有改成 $c_j$。

在每个单胞元内，R72 (2.4)--(2.7) 的完整向量场以这个实际
$w=\mu_jp_\Gamma^\dagger/r^7$ 重新代入。其 mean 方程仍是
$$
 M=\left\langle
   \frac{1+K_{\rm tot}p_\theta/(1-p^2)}{\sqrt D}
                 \right\rangle=1,\qquad
 D=1-2w\kappa-\kappa^2-(1+w^2)p^2.
 \tag{L.3}
$$
Galerkin 方程使用完整
$\Pi[ D^{-3/2}(1+(\kappa+Ep_\theta)/w)]\Pi$ 的压缩逆；
常数模始终包含在投影内，不把压缩逆换成逐点倒数。
源 R25 的材料证明只要求 $|w|\le1$。浅层保持原界；深层有
$$
 |w|\le64\epsilon\delta_{4096}^{3/2}\delta_j^{7/2}<1.
$$
因此该全纯 mean 小根及其 $|K_0|\le12\mathcal R^2$、
$\|B^{-1}\|\le8/7$ 在新对象上确有已付前提。

## 2. 新单胞元的完整局部 map

先列出真正更改的局部门。两个端平台及最后下降段的
$\int|p|^{-1}$ 上界由 $\eta/64$ 改为至多 $\eta/16$；所有主
平台、最低 $|p|\ge\delta/2$ 和最高 $|p|\le64/\delta$ 保持。
完整 log 变差是
$$
 6|\log\delta|+c(c)+4r_C,\qquad
 c(c)=2\log65-\log c<6,\quad r_C=2^{-15}.
 \tag{L.4}
$$
四个坡的点态一、二阶 log 导数仍由
$15\Delta/8$、$6\Delta$ 控制。于是实际材料积分变成
$$
 \begin{split}
 \int(1+|\lambda|)(1+|p|^{-2})dy
 &\le16\delta(1+\alpha^2\delta^{-2})+6|\log\delta|+6\\
 &\quad+e^{2r_C}(\alpha^2\delta^{-2}+1/2+1/512)
             +4r_C(1+\alpha^2\delta^{-2})
 <64\delta^{-2}.
 \end{split}                                                 \tag{L.5}
$$
乘 $\delta^2$ 后，用 $\alpha^2<2$、$e^{2r_C}<2$、
$\delta|\log\delta|\le1$ 即有严格余量。

实际单调 Gauss/Dyson 乘积按原顺序保留。$P_-<128$、
$C_*<4\nu_m$、对角积 $<2$ 不变；$P_+$ 的新增上剪切面积
不超过 $\nu_m\eta/16$，在真低窗
$|m|\le2^{-5}\delta^{-3/8}$ 内小于 $2^{-28}$。
将 $P_+<3$ 放宽到4即得到任意内部子区间的安全新界
$$
 \|\Psi^\dagger_\Gamma(s,t)\|_\infty<512m^4,\qquad
 \|\Psi^\dagger_\Gamma(t,s)\|_\infty<1024m^4.
 \tag{L.6}
$$
复盒中使用 $|p|$ 的真正单调性，Gauss 面积允许为复数；
上述全部费用都是绝对面积的界，不假定复面积为正。

取实际 Galerkin 数
$$
 J_j=4\left\lceil\frac{4096(1+|\log\delta_j|)}{h_j}\right\rceil,
 \quad\overline J_j=32768(1+|\log\delta_j|)/h_j.
$$
在相同的完整复 Wiener 代数中，有限积分方程可用
$Z_0=2^{26}h^{-5}\|U\|$。由 (L.5)--(L.6)，全部 nonlinear
Lipschitz 费至多
$2^{61}J^5h^{-5}\|U\|/(\mu\delta^2)$。因此选取
$$
 R_j^\dagger=2^{-76}\mu_j\delta_j^2h_j^5J_j^{-5}
 \tag{L.7}
$$
使其小于 $2^{-15}$，mean/压缩逆的相对量也小于 $2^{-32}J^{-5}$。
这一步同时包含 mean，不是先解一个删常数的 ODE 再补数值。

完整有限近解残差仍按准确压缩逆公式提取。真实强 Volterra
修正的角费是
$$
 256\beta(\delta),\qquad
 \beta=3\delta+6\eta+
  \sqrt{(15/2)\eta(2\log128+6|\log\delta|)}.
$$
新变差常数只将径向前因子改为 $e^{480c(c)}$；
$480c(c)<2880<4096$，所以实际 $e^{-Jh/4}$ 的已付4096门
仍吸收它。全部矩阵、近解和回到 canonical 状态的费用可安全取
$$
 L_{\rm corr}^\dagger
     =2^{104}\delta^{4807/4}h^{-5}
 \tag{L.8}
$$
作为完整高频修正 map 的线性 norm。这里是实际全角零 residual
修正，source 中的 $-e$ 没有删掉。

对有限 Duhamel 二次项，在输出保留的宽差内用
$512\sup m^4e^{-hm/4}<2^{20}h^{-4}$，而不以 $J^4$ 替代。
连同 (L.5) 和 $Z_0$，其二次系数至多 $2^{96}\mu^{-1}\delta^{-2}h^{-14}$。
完整修正的 Cauchy 余项相对于下式的额外比小于
$2^{57}\delta^{9599/8}<1$。故完整真实局部 map 满足
$$
 \boxed{\quad
 \Phi_{j,\Gamma}^\dagger:B_{\mathcal A_{\tau+h_j}}(R_j^\dagger)
               \longrightarrow\mathcal A_\tau,\quad
 \|\Phi(U)\|\le2^{26}h_j^{-5}\|U\|,\quad
 G_j^\dagger=2^{102}(\mu_j\delta_j^2)^{-1}h_j^{-14}.
 \quad}                                                     \tag{L.9}
$$
$G_j^\dagger$ 同时控制真实二次余项和其二次 Lipschitz 形式。
这些推导重新列明了新 profile、端因子和背景幅度的每个变动；
没有把旧 R72 的局部存在结论直接移到新背景。

## 3. 真高频块、两个理想谱及唯一接缝

规范线性矩阵是
$A_{m,j}^\dagger=-2^{-39/4}e^{-|m|h_j}B_{m,j,\Gamma}^\dagger$。
在低窗 $|m|\le M_j^\sharp=2^{-5/4}\delta_j^{-1/8}$ 内，
前篇已经重证真矩阵误差 $32768m^8\sqrt\delta$。
窗口外仍使用真正的矩阵。按相同 scalar 能量的四坡转换，
点态 log 导数包络未改；完整变差常数可把旧 $e^6$ 放宽到
$e^{12}$。因 $e^6<2^{10}$、$c\le64$，安全的全频式是
$$
 \|A_{m,j}^\dagger\|_\infty
 \le2^{16}C_H(1+|m|)^{312}e^{|m|(\beta_j-h_j)}<1/4,
               \qquad |m|>M_j^\sharp.                       \tag{L.10}
$$
$C_H$ 是原已明确的 $2^{2-39/4}C_L^{(6)}$。native 在浅端128
重新给完整 log 包络 $<-68.0895$，在4097给 $<-10^{150}$；
原 $\beta/h$ 及频率/层单调性证明不含 $c$，故覆盖全部层。

对 $c=64$ 或 $C=16\sqrt2$ 定义
$$
 T_{m,c}=\alpha\nu_m(64+1/c)-(1+1/c),\qquad
 \Lambda_{m,c}=\frac{T_{m,c}+\sqrt{T_{m,c}^2-4/c}}2,
 \quad \lambda_{m,c}=1/(c\Lambda_{m,c}).
$$
准确特征基可取
$$
 E_{m,c}=\begin{pmatrix}1&t_{m,c}\\s_{m,c}&1\end{pmatrix},
 \quad t_{m,c}=\frac{\alpha\nu_m}{64\alpha\nu_m-1-\lambda_{m,c}},
 \quad s_{m,c}=\frac{64\alpha\nu_m-1-\Lambda_{m,c}}{\alpha\nu_m}.
 \tag{L.11}
$$
完整 $16\le c\le64$ 上
$$
 -1/16<s_{m,c}<0,\quad0<t_{m,c}<1/63,\quad
 \|E_{m,c}\|_\infty,\|E_{m,c}^{-1}\|_\infty<17/16<2.
 \tag{L.12}
$$
令 $L_{m,c}=2^{-39/4}\Lambda_{m,c}>\sqrt2$。
native 对43个 $m=4,\ldots,172$ 重核
$L_{m,c}e^{-.09m}>25/24$，并核 $m=176$ 时小于 $4/5$。
这里最小端取 $c=64$、最大端取 $c=16$；谱根对 $1/c$ 单调。
$\partial_m\log\Lambda<5/m$ 再给所有 $m\ge176$。
深段的 $h_j$ 几何递减，$L_{m,C}\ge L_{m,64}$；
中性层数仍不超过192。这来自准确
$256\log_2(5/3)+2<192$，并非只核两个频率。
因此不含基接缝的 scalar 强 Green 核和仍小于256。

若同一模的低区跨过4096，唯一的新基变化是
$$
 Q_m=E_{m,64}^{-1}E_{m,C},\qquad
 \|Q_m\|,\|Q_m^{-1}\|<2,\quad Q_{11}>1/2,\quad |Q_{21}|<1/8.
 \tag{L.13}
$$
若它首次进入低窗时已经位于4096之后，则从开始即用 $E_{m,C}$，
没有再人为插入一次 $Q$。高区始终保留 (L.10) 的真实块。

## 4. 接缝上的完整两分量 Green，不丢大倍率

在低区用 $z=(u,v)=E^{-1}X$，参考对角递推写为
$u_{j-1}=a_ju_j+f^u_{j-1}$、
$v_{j-1}=s_jv_j+f^v_{j-1}$，其中
$a_j=L_{m,c_j}e^{-|m|h_j}$、$0<s_j<1/1000$。
在接缝处准确是
$$
 \begin{pmatrix}u_{J_*}\\v_{J_*}\end{pmatrix}
 =Q_m\begin{pmatrix}a_{J_*+1}u_{J_*+1}\\
                         s_{J_*+1}v_{J_*+1}\end{pmatrix}
   +\begin{pmatrix}f^u_{J_*}\\f^v_{J_*}\end{pmatrix}.
 \tag{L.14}
$$
先由未来的完整强迫和确定 $v_{J_*+1}$，norm 至多 $2\|f\|$。
第一行只是 scalar $u$ 的一次 gain $Q_{11}a_{J_*+1}$ 和
额外 source $Q_{12}s_{J_*+1}v_{J_*+1}$。
$Q_{11}$ 与其倒数小于2；相对原 scalar kernel 的每条传播路径
至多经过这一因子一次。因此 large kernel 和至多512，齐次
标签列至多2。

第二行不能直接用 $a_{J_*+1}\|u\|$ 来估计，因为 $a_j$ 可能
很大。必须准确使用第一行给出的
$$
 a_{J_*+1}u_{J_*+1}
 =\frac{u_{J_*}-Q_{12}s_{J_*+1}v_{J_*+1}-f^u_{J_*}}{Q_{11}}.
 \tag{L.15}
$$
由此 $|v_{J_*}|\le\|u\|/4+2\|f\|$，再向浅端用小分量
几何和延拓。两分量 source 完整保留，没有删除配对的 flux 行。
加入两次 $E,E^{-1}$ 和真实高区 $4/3$ 几何和，可安全统一取
$$
 \|\mathcal G_{0,\Gamma}^\dagger\|_{\mathcal F\to\mathcal X}
                  \le2^{15},\qquad
 \|\mathcal H_{0,\Gamma}^\dagger\|_{\ell^1\to\mathcal X}\le8.
 \tag{L.16}
$$
这里 $\mathcal X=\sum_{m\ne0}\sup_{j\ge128}|X_{m,j}|_\infty$，
$\mathcal F=\sum_{m\ne0}\sup_{j>128}|f_{m,j-1}|_\infty$。
明确令 $n_0(m)$ 为首次进入低窗的层，$j_m$ 为其后第一个
$a_{m,j}\ge1$ 的层，$b_m=j_m-1$，标签为该层 $E^{-1}X$ 的第一分量。
若 $n_0(m)>4096$，从其首个低区端点 $n_0(m)-1$ 起就用新 $E_C$；
否则在 $n\le4096$ 用 $E_{64}$、$n\ge4097$ 用 $E_C$，并付 (L.14)。
这些是明确的内部线性泛函，没有换成共同 cut 的高高度。
上述构造先逐模证明时间上确界，再求和，故 (L.16) 是全频强界。

## 5. 真矩阵和完整非线性图

低区真矩阵误差在原 $X$ norm 中仍至多
$$
 \varepsilon_j=32768\,2^{-39/4}\sqrt{\delta_j}
                         (8/(eh_j))^8.
$$
重跑全部分段门给
$$
 2^{15}\sup_j\varepsilon_j<.024998080<1/32.
$$
于是新的真 Green 与真齐次标签列确实满足
$$
 \mathcal G_\Gamma^\dagger
   =(I-\mathcal G_{0,\Gamma}^\dagger R_\Gamma)^{-1}
                                  \mathcal G_{0,\Gamma}^\dagger,
 \quad \|\mathcal G_\Gamma^\dagger\|<2^{16},\quad
 \|\mathcal H_\Gamma^\dagger\|<256/31<9.
 \tag{L.17}
$$
Neumann 只在已经带真实逐层角权的同一强离散空间进行；
没有重复使用一个连续 PDE 有宽差算子而不付费。

新局部 (L.7) 的真实 Taylor 入球门也重新核验。
$\zeta_j/R_j^\dagger$ 在浅端128的 $\log_2$ 上界小于 $-12$；
深端4097远小于 $-6000$。完整包络对每层递减，且
$16e\zeta_j/R_j^\dagger<1$。
角平移等变性仍强制所有 Taylor 频率满足
$m=m_1+\cdots+m_q$；包含 mean 的压缩逆与实际强残差修正都保持
该性质。因此完整卷积提升给
$$
 \|\mathcal R^\dagger(X)-\mathcal R^\dagger(Y)\|_{\mathcal F}
 \le K_*^\dagger(\|X\|+\|Y\|)\|X-Y\|,
$$
$$
 K_*^\dagger=2^{112}\sup_{j>128}
       \frac{\zeta_j}{\mu_j\delta_j^2}h_j^{-14}.
 \tag{L.18}
$$
逐层比例准确是前篇 (N.22)。深段相对于旧的 $\delta_j^{7/4}$
多了 $(\delta_j/\delta_{4096})^{3/2}\le1$，所以统一新门为
$$
 2^{16}K_*^\dagger<2^{-53}.
 \tag{L.19}
$$
于 $\|a\|_{\ell^1}<1/64$，方程
$$
 X=\mathcal H_\Gamma^\dagger a
          +\mathcal G_\Gamma^\dagger\mathcal R^\dagger(X)
 \tag{L.20}
$$
在单位 $\mathcal X$ 球内自映，收缩常数小于 $2^{-52}$，且
$\|X\|<10\|a\|<16\|a\|$。每个胞元使用 (L.9) 的真正全角
零 residual 解，端口连接同时匹配完整高度和径向迹。
(L.3) 的唯一 mean 根一致，二阶 jet 由真实 PDE 匹配。
因此这是真正新尾 PDE 的解，不是离散近似或 Galerkin 尾。

对任意 $\beta\ge0$，同时给全部 Fourier 标签和状态乘
$e^{\beta|m|}$，所有系数卷积与上述强界保持；所以 (L.1)
在整个 $\ell^1_\beta$ 域成立，包括所需 $\beta=224$。

## 6. 新状态的实际层权、平坦性及全部参数

完整局部强解给
$$
 \mathcal R_j^{\rm rel}
 \le2^{47}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2}
                  e^{-4\beta}\|X\|_{\mathcal X_\beta}.
$$
这里 mean 的 $12\mathcal R^2$ 也已包含。用
$h_j^{-5}<2^{18}\delta_j^{-5/256}$，并为跨胞邻接及各完整相对
分量留固定余量，可取
$$
 \boxed{\quad n_j^\dagger<2^{72}e^{-4\beta}
       \|X\|_{\mathcal X_\beta}
 \begin{cases}
     \delta_j^{443/256},&j\le4096,\\
     \delta_{4096}^{-3/2}\delta_j^{827/256},&j>4096.
 \end{cases}\quad}                                         \tag{L.21}
$$
它是新真实解上的界。特别全局因子并没有被写进一个未指明的
常数再忘掉；切换处的新旧尺度严格相接。

把平盘 mean 高度固定为0作为唯一的加法规范后，绝对高度 jets
可由同一零 residual 方程恢复，安全界是
$2^{56}\delta_j^{-4}h_j^{-5}\zeta_j\|X\|$。
其深端指数仍为 $23/4-5/256>0$，所以完整非线性图 $C^2$ 接到
平盘。mean 高度由一次真实积分恢复，只保留一个整体加法规范。
实共轭、四重周期及整体相位平移由完整构造的唯一性保持。

局部 map、两段高频真块和低区 Neumann 都对 $\Gamma,a$ 联合
Fréchet 全纯。$Q_m$ 是固定的新实际两理想基变换，与 $\Gamma$
无关；没有逐层固定其它参数。完整复球的一致收缩给 (L.20)
的联合全纯性。参数的乘积拓扑连续性使用真正的低区包络
$\sqrt\delta\,h_j^{-8}=O(\delta_j^{15/32})$ 和高区的实际指数
衰减；局部 nonlinear 深端包络是
$\delta_{4096}^{-3/2}\delta_j^{13/4}h_j^{-14}\to0$。
这些准确尾界及绝对二 jet 衰减给物理 $C^2$ 连续性。

## 7. 强 source 范畴与下一个真实输入缺口

(L.17) 是任意完整**非mean canonical 端口残差**
$f\in\mathcal F$ 的真线性解，保留所有内部标签与两分量。
它没有把物理连续 source 只记成一个端点高度跳量。
要将一个给定物理 $e$ 放入这个空间，必须按前篇 (N.10) 的
$\mu_j(p_*^\dagger)^2e/(12r^{10})$ 和真连续 propagator 得到
两个 canonical 端口分量，再支付 (L.2) 的准确规范。
其 mean 还必须按 (N.11) 的通量原函数和独立高度行支付；
不能将有源 holonomy 负荷设为0后直接套 (L.3)。

本篇闭合了新零源全标签图和相应强离散 inverse。
下一项仍是完整连续普通/metric 源的实际归一、负段真实相位和
完整网络相对逆，以及从当前帽端 $f_*$ 经长段筛选后真正可达的
标签半径。尤其 (L.21) 的正深层幂本身不证明一个预选的极小球
已包含真实匹配数据。

[准确新 Green/入球预算程序](../scripts/fourfold_new_deep_full_label_chart_20261113.py)
及 [完整报告](../notes/2026-11-13-R119-new-deep-full-label-chart-budget-v2.json)
包含新端基、真实所有43个浅低频门、高频两端单调包络、完整
Neumann 和全部 Taylor/mean 入球费。
