# R119 续篇：强首剪切新尾的实际全参数 return KAM

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 在第8193层改变首剪切并采用131幂规范的
同一个新公共度量族上，全部内部负型分量的真实非径向两射线
return 可以同时共轭到预先选定的 Diophantine 旋转。全频、
所有层之间的参数依赖、完整平均行都保留。取
$$
 A_*=2^{-262148},\qquad
 \|a\|_{\ell^1_{224}}<A_*,\qquad \bar a=\|a\|/A_*<1.
 \tag{K.1}
$$
这使同一个真实全标签解满足 $\|X\|<16A_*\bar a\le2^{-262144}$。
此次真正重算的小除数平方预算是
$$
 \boxed{\qquad
 \mu_{\rm KAM}:=\sup_i{\varepsilon_i\over(\gamma_i^{\rm D})^2}
       <2^{276}A_*=2^{-261872}.
 \qquad}                                                     \tag{K.2}
$$
新构造所得参数在标签的角平移轨道上准确不变。因此选定标签后，
整个相位轨道对应一个固定目标度量。这里仍没有把这一内部标签
球当作已经由外部 nonlinear regular 问题达到的球。

## 1. 同一个新 profile 与真实可调参数

严格使用
[强首剪切几何](R119-supplement-stronger-deep-first-shear-and-complete-local-map.md)
和[全标签图](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
的对象：
$$
 K_j=\begin{cases}64,&j\le8192,\\2^{128},&j>8192,\end{cases}
 \quad c_j=\begin{cases}64,&j\le4096,\\16\sqrt2,&j>4096,\end{cases}
 \quad \alpha=65/64,
$$
$$
 \delta_j=(2/25)2^{-j},\qquad \eta_j={\delta_j^{3/2}\over4\sqrt2}.
 \tag{K.3}
$$
两种下降 log-quintic 的实际落差为
$$
 \Delta_{j,1}=\log(K_j\alpha)+2|\log\delta_j|,\qquad
 \Delta_{j,2}=|\log\delta_j|-\log c_j.
 \tag{K.4}
$$
对全部 $j\ge129$，准确有
$$
                         j/2<\Delta_{j,k}<3j.              \tag{K.5}
$$
旧段由 $\log65<5$、$2<\log(25/2)<3$、
$2/3<\log2<3/4$ 得到。新首剪切段有
$\log(2^{128}\alpha)<97$，故
$\Delta_{j,1}<103+3j/2<3j$ 于 $j\ge8193$；
第二种的最坏下界仍是 $c_j=64$。这重新验证了新对象的门，
没有把旧 log65 留在新8193层。

在每个下降段上用同一个实际 $C^2$ bump
$$
 \psi(x)=64[8(x-1/4)]^3[1-8(x-1/4)]^3,\quad 1/4\le x\le3/8,
$$
在支集外延0，并写
$$
 \log p_{j,\Gamma}=\log p_j+\gamma_{j,k}\psi,\qquad
 A_\Gamma=A+\gamma_{j,k}\psi_t.
 \tag{K.6}
$$
实参数盒为 $|\gamma_i|<2^{-16}$，复盒为 $|\gamma_i|<2^{-15}$。
每点至多一个 bump；全部端二 jet、所有正型分量及转向 germ
准确不变。强首剪切几何篇已经逐项支付这组新参考面的 $C^2$
平端和无限参数连续性；其全标签图在整个复盒和完整复标签球
上由同一收缩给出。这里不要求把粗 Sobolev pullback 视为全纯算子。

指标集仍取
$$
 \mathcal I=\{(j,1):j\ge129\}\cup\{(j,2):j\ge130\}.
 \tag{K.7}
$$
每个分量的两端都是真实转向根。最外 $(129,2)$ 在 cut128
截断，其参数固定为0；它保留在全尾与最外 regular 方程中，
不被冒充本篇的完整两根 return。

## 2. 新实际零标签角窗，及全部复参数逆

设 $I_i$ 是完整负型分量。零标签的真实两射线角为
$$
 \Theta_i(\gamma_i)=-2\int_{I_i}\sqrt{-A_\Gamma(t)}\,dt.
 \tag{K.8}
$$
每个 $I_i$ 只含自己的一个下降 bump。因为支集与转向点分离，
参数微分均在严格内部进行，准确有
$$
 \Theta_i'(\gamma_i)
 =-\frac12\int{\psi(A_t+\gamma_i\psi_{tt})\over
                              (-A_\Gamma)^{3/2}}\,dt>0.
 \tag{K.9}
$$
[真实度量参数证明](R119-supplement-actual-negative-band-metric-parameters.md)
(M.6)--(M.12) 的积分常数只使用 (K.5)、同一个 $S,\psi,\eta$：
$\int\psi dt=2\eta/(35\sqrt{12})$、
$36\Delta/\eta^2<-A_t<72\Delta/\eta^2$、
$\sqrt{12}\Delta/\eta<-A<3\sqrt{12}\Delta/\eta$ 在支集成立。
因此其完整推导在新落差 (K.4) 上给
$$
 2^{-8}\sqrt{\eta_j/\Delta_i}<\Theta_i'(0),\qquad
 2^{-9}\sqrt{\eta_j/\Delta_i}<\Theta_i'(\gamma_i)
                    <\tfrac12\sqrt{\eta_j/\Delta_i}.
 \tag{K.10}
$$
前一式取中心的较强下界；没有由实盒较弱下界反推中心常数。

在复盒上，
$|\gamma\psi_t/A|<1/256$、$|\gamma\psi_{tt}/A_t|<1/16$。
故直接对 (K.9) 的被积函数比较给
$$
 \left|{\Theta_i'(\gamma)\over\Theta_i'(0)}-1\right|<1/8.
$$
定义实际角窗
$$
 \kappa_i=2^{-25}\sqrt{\eta_j/\Delta_i},\qquad
 \kappa_i^2>{2^{-55}\over j}\delta_j^{3/2}.                 \tag{K.11}
$$
用
$\gamma=\lambda/\Theta_i'(0)
 -[\Theta_i(\gamma)-\Theta_i(0)-\Theta_i'(0)\gamma]/\Theta_i'(0)$
在完整复盘收缩，得到全纯逆 $G_i$：
$$
 \Theta_i(G_i(\lambda))=\Theta_i(0)+\lambda,\quad
 |\lambda|<2\kappa_i,\quad |G_i'|<512\sqrt{\Delta_i/\eta_j}.
 \tag{K.12}
$$
全部 $G_i$ 组成从加权 $\ell^\infty$ 圆盘
$\sup|\lambda_i|/\kappa_i<2$ 到原复参数盒的联合全纯 map。
整个无限盒一起处理，不把较深层变小的相位尺度漏掉。

## 3. 不经过 hodograph 的真实非径向完整 return

这里直接保留原物理角。对同一个完整尾解，采用
$$
 d=E(V-P)/J,\qquad v=\sqrt D/J,\qquad q_\Gamma=\sqrt{-A_\Gamma}.
$$
两个真实特征流是
$$
 (F_\sigma)_t=-d(t,F_\sigma)-\sigma q_\Gamma(t)v(t,F_\sigma),
 \quad F_\sigma(t_-)=\mathrm{id},\qquad
 R_i=F_-^{-1}\circ F_+ .
 \tag{K.13}
$$
这是完整两根间的两支流；共同漂移 $d$、波速 $v$ 和实际端角
都没有删除。它只描述 principal return，不声称 Airy 的幅度
connection 是恒等。

令
$$
 N_j=2^{184}h_j^{-5}{\zeta_j\over\mu_j\delta_j^2},\qquad
 N_j^\#=N_j+\mathbf1_{j\ge130}N_{j-1}.
 \tag{K.14}
$$
全标签图给宽4上的完整四态
$n_i\le4N_j^\#\|X\|$。商式在宽3给
$|d|,|v-1|,|d_\theta|,|v_\theta|\le32n_i$。
真实两胞元的几何给 $\int_{I_i}(1+|Q_\Gamma|)dt<16(j+4)$；
特别对每一部分区间
$$
 \int (1+|q_\Gamma|)dt<32(j+4).
$$
复参数的参考相位虚部也已直接支付：
$$
 \int|q_\Gamma-q_0|dt
 \le2(2^{-15})\sqrt{\eta_j/\Delta_i}<2^{-14}.               \tag{K.15}
$$
因参数支集外 $q_\Gamma=q_0$，包括两个平方根端点，所以没有
复平方根绕零的隐性分支问题。

从 (K.13) 减去准确参考标量平移
$-\sigma\int q_\Gamma$。其余角位移的 Picard 积分和导数 Lipschitz
积分不超过 $2^{10}(j+4)n_i$。在宽 $7/4$ 的位移球内，
真实复相位虚部、未知位移和逆流的复合总共消费小于 $1/8$；
所有原系数仍在宽2内求值。故正反流相对于参考平移的差
可以统一取
$$
 D_i=2^{14}(j+4)N_j^\#\|X\|.
$$
两个流复合，在宽 $3/2$ 上准确得到
$$
 R_i(\theta)=\theta+\Theta_i(\gamma_i)+E_i(\Gamma,a,\theta),
 \qquad \|E_i\|_{\mathcal A_{3/2}}<4D_i.
 \tag{K.16}
$$
它对所有参数和全部标签联合全纯。实数据下是真实圆周微分同胚。
这里即使 $v-1$ 只按一阶小量支付，预算也足够；没有以 mean
二阶抵消掩盖某一未付的角流。

## 4. 固定 Diophantine 目标和实际小除数平方预算

写标准圆 $x=4\theta$、$\Omega_i^0=4\Theta_i(0)$。
在标签选择以前，一次固定
$$
 |\omega_i-\Omega_i^0|\le\kappa_i/2,\qquad
 |e^{in\omega_i}-1|\ge\gamma_i^{\rm D}|n|^{-2}
 \quad(n\ne0),\qquad \gamma_i^{\rm D}=\kappa_i/64.
 \tag{K.17}
$$
存在性的完整测度证明仍直接适用新 $\kappa_i$：第 $n$ 坏集在
标准圆上的长度小于 $4\gamma_i^{\rm D}/n^2$；总坏集小于
$8\gamma_i^{\rm D}=\kappa_i/8$，小于允许闭区间的长度。
可固定该区间闭好集的最小实 lift，故目标不随标签或迭代改变。

令
$$
 p_i=4\lambda_i-(\omega_i-\Omega_i^0),\qquad
 \|p\|_{\mathcal P}=\sup_i|p_i|/\kappa_i .
$$
由 (K.12)，$\|p\|_{\mathcal P}<4$ 仍在合法复逆盘内。
新真实 maps 化为
$$
 \mathcal R_{i,p,a}(x)=x+\omega_i+p_i+f_i(p,a,x),
 \qquad
 \|f_i\|_{\mathcal A_6}<\varepsilon_i\bar a,\quad
 \varepsilon_i=2^{24}(j+4)N_j^\# A_* .
 \tag{K.18}
$$
这里标准圆因子4、两流复合费用4以及 $\|X\|<16A_*\bar a$
总共需要 $2^{22}$，显示的 $2^{24}$ 保留余量。各 $f_i$ 依赖
全部 $p$；没有假定它们在参数中逐行对角。

保留真实两次规范接缝，$N_j$ 的三个幂为
$$
 7/4,\quad 827/256,\quad 31867/256,
$$
且中段和深段始终带
$\delta_{4096}^{-3/2}$，深段另带 $\delta_{8192}^{-485/4}$。
定向预算给
$$
 \boxed{\quad
 \sup_{j\ge129}j(j+4)N_j^\#\delta_j^{-3/2}<2^{185}.
 \quad}                                                     \tag{K.19}
$$
为避免只做有限扫描，完整全层论证如下。三个内部区间中的
真实相邻比由多项式 $j(j+4)$ 的递减相邻比乘
$2^{-(7/4-3/2)}$、$2^{-(827/256-3/2)}$、
$2^{-(31867/256-3/2)}$ 给出。连最弱第一种在 $j=129$ 已小于1，
以后更小。两处混合邻胞接缝单独精算。所需各点的
$\log_2[j(j+4)N_j^\#\delta_j^{-3/2}]$ 上界为

| 层 | 向外上界 |
|---:|---:|
|129|182.276|
|130|184.173|
|4096|−797.414|
|4097|−753.568|
|4098|−751.921|
|8192|−7834.462|
|8193|−7836.338|
|8194|−7959.318|

故真正上确界在129起的首个完整跨胞行附近，所有新深段都在
显示界内。结合 (K.11)、(K.18)，得到
$$
 \mu_{\rm KAM}
 <2^{24+12+55}A_*
          \sup_jj(j+4)N_j^\#\delta_j^{-3/2}
 <2^{276}A_*=2^{-261872}<2^{-64}.                           \tag{K.20}
$$
这是实际新对象的完整小除数平方费用，未转授旧 $443/256$
单幂表达式，也没有省略长有限前缀或全局逆幂。

## 5. 真无限联立 Newton：所有 mean 与所有角频

此处消费
[完整联立 KAM 引理](R119-supplement-joint-actual-negative-band-return-kam.md)
§7 的已经给出证明的函数空间定理，而非其旧 profile 常数。
为明确核对新消费者，把其关键有序行列如下。

初值 $p=0,h_i(x)=x$，误差
$E_i=\mathcal R_{i,p,a}\circ h_i-h_i\circ T_{\omega_i}$。
第 $n$ 步取
$$
 s_0=2,\quad d_n=2^{-n-4},\quad s_{n+1}=s_n-4d_n,\quad
 \|E_i\|_{s_n}\le e_n\varepsilon_i,\quad e_0\le\bar a.
$$
写 $H_i=h_i'\circ T_{\omega_i}$。参数导数在**当前真实点**
$h_i(x)$ 处评价：
$$
 \mathsf C_i^h[q]=(D_pf_i(p,a,\cdot)[q])\circ h_i,\qquad
 d_i^0=\langle H_i^{-1}\rangle,\quad
 B_i(q)=\langle H_i^{-1}\mathsf C_i^h[q]\rangle.
$$
全部参数一次联立解
$$
 d_i^0q_i+B_i(q)=-\langle E_i/H_i\rangle,\qquad i\in\mathcal I .
 \tag{K.21}
$$
原盘4和宽6的实际余量给
$\|\mathsf C_i^h[q]\|\le\varepsilon_i\|q\|_{\mathcal P}$；
weighted 平均行的非对角 norm 至多
$4\sup_i\varepsilon_i/\kappa_i\le4\mu_{\rm KAM}$。
其 Neumann 逆存在，且
$$
 \|q\|_{\mathcal P}\le8e_n\sup_i\varepsilon_i/\kappa_i,\qquad
                         |q_i|\le8e_n\varepsilon_i.        \tag{K.22}
$$
后一式从已解出的完整平均行代回取得，保留每一深层自己的误差。

然后解所有非零 Fourier 系数的 cohomological 方程
$$
 v_i-v_i\circ T_{\omega_i}
   =-E_i/H_i-(q_i+\mathsf C_i^h[q])/H_i,\qquad \langle v_i\rangle=0.
 \tag{K.23}
$$
(K.21) 使右侧 mean 准确为0。每个非零系数除以
$1-e^{in\omega_i}$，得到
$\|v_i\|_{s_n-d_n}\le20e_n\varepsilon_i
(\gamma_i^{\rm D})^{-1}d_n^{-2}$。更新
$p\leftarrow p+q$、$h_i\leftarrow h_i+h_i'v_i$。
准确关系
$(\mathcal R_i'\circ h_i)h_i'=H_i+E_i'$
把剩余线性误差变为 $E_i'v_i$；参数/空间的真实二阶 Taylor
余项受原盘和角域控制。因此
$$
 e_{n+1}\le2^{14}\mu_{\rm KAM}d_n^{-6}e_n^2,\qquad
 e_n\le\bar a\,2^{-8n}.                                   \tag{K.24}
$$
全部参数修正和角导修正收敛，得到
$$
 \mathcal R_{i,p^*,a}\circ h_i=h_i\circ T_{\omega_i},\quad
 |p_i^*|<16\varepsilon_i\bar a,\quad
 \|h_i'-1\|_{\mathcal A_{3/2}}<2^{18}\mu_{\rm KAM}<2^{-261854}.
 \tag{K.25}
$$
每步保留全部 Fourier 模、完整 mean 与全参数交叉列；没有把
某层冻结来解另一层。引理的证明只需要刚逐项验证的
(K.11)、(K.17)--(K.20)，所以本次是对新族的真正实例化。

## 6. 最终单一目标及真实相位轨道

定义
$$
 \Gamma_i^0=G_i((\omega_i-\Omega_i^0)/4),\qquad
 \Gamma_i^*(a)=G_i((\omega_i-\Omega_i^0+p_i^*(a))/4),
 \quad \Gamma_{129,2}^*=0 .
 \tag{K.26}
$$
全部实参数落在原 $2^{-16}$ 盒内，并有
$$
 |\Gamma_i^0|<2^{-19},\qquad
 |\Gamma_i^*(a)-\Gamma_i^0|
 <2^{-14}{\varepsilon_i\over\kappa_i}\bar a.                \tag{K.27}
$$
这一单位转换使用实际 $|G_i'|<512\sqrt{\Delta_i/\eta_j}$，
没有把 $\Gamma$ 当成相位参数 $p$。新参考面的 $C^2$ 参数连续性
与全标签图保证 (K.26) 已定义真实无限尾和真实单个目标
$g^\ddagger_{\Gamma^*(a)}$，无需以后猜一个有限截断极限。

整个 Newton 过程在辅助标签上局部全纯。实标签平移
$a_m\mapsto e^{im\varphi}a_m$ 时，实际 raw 方程、mean 分支和
(K.13) 的两射线 map 均只被同一物理角平移共轭。
参数平均、相同的 Fourier 逆与完整 (K.21) 都与该平移交换；
从 $h_i=\mathrm{id},p=0$ 归纳可得参数修正逐步不变。因此
$$
             \boxed{\Gamma^*((e^{im\varphi}a_m)_m)=\Gamma^*(a).}
 \tag{K.28}
$$
一个最终标签选定以后，其整个相位轨道严格共用同一个度量。
此结论允许构造期间联立选择度量；它不在一个声称固定原 $g_0$
的 Newton 迭代中更换目标。

## 7. 实际两迹、正确 mean 与正型/source 接口

本次直接使用物理角，故令
$$
 K_i(\eta)=h_i(4\eta)/4,\qquad
                  R_i\circ K_i=K_i\circ T_{\omega_i/4}.    \tag{K.29}
$$
所有图至少在物理角宽 $3/8$ 上有定义。它们作用于高度和通量
的准确方式不同：
$$
                     f^{\rm new}=f\circ K_i,\qquad
                     p^{\rm new}=K_i'p\circ K_i .
 \tag{K.30}
$$
于是 $\int p^{\rm new}f^{\rm new}=\int pf$，而通量 mean 准确
保留；高度 mean 必须按 $\langle f\circ K_i\rangle$ 实读。
normal/shear 仍由完整两迹恢复。任何度量参数源还须保留
$D_\Gamma w_\Gamma$ 和原完整 mean/holonomy 的参数变化。

对于标量 return 方程 $u\circ R_i-u=f$，实际平均条件为
$\langle f\circ K_i\rangle=0$。在该条件下完整 Fourier 逆给
$$
 \|u\|_{K_i,s-h}\le(\gamma_i^{\rm D})^{-1}h^{-2}\|f\|_{K_i,s},
 \quad \langle u\circ K_i\rangle=0,\quad 0<h<s<3/8,
 \tag{K.31}
$$
这里 $\|f\|_{K_i,s}=\|f\circ K_i\|_{\mathcal A_s}$。
该结论只反演显示的 scalar cohomological 因子，不是整个
两场混合系统的逆。

相邻正型分量必须同时保留它的两个真实端图，以 (K.30) 的
dual pairing 搬运完整双端 DN 和两端源列。参考矩阵中
非对角的 $-1/\beta_m$ 不删除；搬运后的参考不必仍对原 Fourier
基对角。弱源的端点法向负荷不能被体源 norm 代替。
真实体源在坐标变换下带整个 Jacobian；原 weighted mean
电荷亦原样保留。这里未新增任何全域粗源到根混合坐标的权限。

新
[严格段全空间相对传递](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
比较的是同一个实际 $\Gamma^*(a)$ 的径向参考，因而可消费本篇
输出。它没有把 $\Gamma^*(a)$ 的参考进一步替换为
$\Gamma^0$ 的参考；如需这一替换，须支付完整径向两态及其
真 phase 变化，不能由 (K.27) 的数值小就作同宽替换。

## 8. 此次闭合和尚未转授的范围

新对象的全标签图、完整负段 roots/strict 传递和实际全参数
return KAM 现在都有各自真实输入门。最终选定
$g^\ddagger_{\Gamma^*(a)}$ 后，第四线必须消费其真实
$d_4^\ddagger(\Gamma^*)$，有限 connector 的停止长度和整体尺度
必须随它重调；共同双 bump 的全模好集也需按新尾实际选择。
已有零标签新 Robin 与第四线结论提供这些构造的输入，并不
自动给非零标签的完整 regular 反解。

R133 新得到的正帽—长段接合有真正 $f_*$ 及独立物理 $f_B$
端口。它尚需与本篇实际尾解的完整两迹方程
$F(a,f_*)=0$ 联立；本篇不把 $a=0$、$f_B=0$ 代入就宣布
这个边界方程成立。正型双端 Green 与全部 Airy/source 端口的
统一比较、最外 cut128 分量及该真实边界可达性仍为下一对象。

[实际新参数、小除数平方和无限层预算程序](../scripts/fourfold_stronger_tail_actual_KAM_20261113.py)
及[定向报告](../notes/2026-11-13-R119-stronger-tail-actual-KAM-budget.json)
记录此次所有新对象门；旧 KAM 的数值报告没有移作本次证据。
