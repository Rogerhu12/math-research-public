# R119 续篇：真实主平台的平衡能量将完整非线性标签域降至权 224

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对同一 R69/R74 已安装的 connector 和已经固定的
两个 bump，原内部标签的完整非线性 exact-tail chart 可以从
$\ell^1_{8192}$ 的 $1/4$ 球扩张到 $\ell^1_{224}$ 的 $1/4$ 球。
全部高标签、全部非线性高输出、mean、holonomy、水平重建及两个真实
径向迹均保留。新输出的原物理角宽仍覆盖实际的 $1/512$ 窗口。

这项改善来自准确使用长 $q=2$ 平台的四态线性主部与零阶耗散，
没有改变内部层编号或真实轮廓，也不只是更换标签范数的名字。
本篇仍不证明整个非线性尾匹配算子的相对高频逆。

## 1. 同一完整对象的分段长度

采用 [R11 §§4–5](R11-matched-mode-four-physical-tail-connector.md)、
[R69 §4](R69-actual-closed-approximate-exterior-and-two-held-disks.md)
及 [实际双 bump 续篇 §1](R119-supplement-two-bumps-and-exact-nonlinear-matching.md)
的原对象。用从 cut128 向外的物理时间 $t=\log(a/a_e)$。
仍记 $A=aw_a/w=q+1$、$E=1+w^2$。

把有限区间分成三类，其顺序保持原对象的顺序：

* **主平台**：$q=2$，因而 $A=3$。其准确长度
  $L_a=\tfrac12\log(2^{360}/\omega_a)$，其中 $\omega_a>2/3$。
* **其余 connector 短段**：准备组及末端组的总长度为 $L_s$；
  每段都满足 $-7\le A\le3$。
* **整个双 bump 区间**：长度 $L_b=25\omega/8$，其中
  $7/5<\omega<3/2$，且 $7/8<A<9/8$。

实际 quintic 接缝均在上述短段内，没有删除接缝。
由 R11 的准备长度 $<1/3+2\eta$、末端长度 $<1/8$，
$\eta=2^{-24}$，以及 $\log2<7/10$、$\log(3/2)<1/2$，得到
$$
 L_a<\frac{505}{4},\qquad
 L_s<\frac{11}{24}+2^{-23}<\frac12,\qquad
 L_b<\frac{75}{16}.
 \tag{W.1}
$$
整个有限区间仍有 $0<w<1$、$w/a<5/18$、$a<7\cdot10^{-6}$。
这里只改变证明使用的能量，不改变已经选定的两个 bump 参数。

## 2. 平衡四态及完整二次项

用 [R119 §2](R119-actual-final-connector-all-label-continuation.md)
的同一相对变量
$$
 P=\frac{v_\theta}{aw},\qquad K=\frac{v_a}{w},
 \qquad U=P_\theta,\quad V=K_\theta,\quad J=1+K+EU .
$$
$K$ 包含 mean。完整方程重新排列为
$$
\begin{aligned}
 P_t&=K_\theta-(A+1)P,\\
 K_t&=-A P_\theta-2AK+R,\\
 U_t&=V_\theta-(A+1)U,\\
 V_t&=-A U_\theta-2AV+R_\theta,
\end{aligned}
\qquad
 R=\frac{E(V-P)^2+A(K^2+2EKU+EU^2-w^2P^2)}{J}.
 \tag{W.2}
$$
这是准确恒等式；特别 $-AU=-AP_\theta$ 属于第一对的角主部，
不能在估计中又当作一个无关的零阶项。

对 Fourier Wiener norm 定义
$$
 N=\|P\|_\sigma+\|K\|_\sigma+\|U\|_\sigma+\|V\|_\sigma,
 \qquad
 N_b=\sqrt3(\|P\|_\sigma+\|U\|_\sigma)+\|K\|_\sigma+\|V\|_\sigma .
 \tag{W.3}
$$
于是 $N\le N_b<2N$。$\mathcal D N_b$ 表示在此和式每个 Fourier 项
再乘 $|m|$。所有模属于 $4\mathbb Z$，这里没有截断高模。

给出二次项的统一完整界。若 $N\le1/64$，则
$\|J^{-1}\|\le(1-2N)^{-1}<2$。记 (W.2) 的分子为 $G$。
Banach 代数直接给
$$
 \|G\|\le30N^2,\quad
 \|G_P\|\le18N,\quad
 \|G_K\|,\|G_U\|\le28N,\quad
 \|G_V\|\le4N.
$$
例如，写 $x=\|K\|+\|U\|$、$y=\|P\|+\|V\|$，则
$\|G\|\le14x^2+9y^2\le14N^2<30N^2$。
商法则连同 $J_K=1,J_U=E$ 因而给
$$
\begin{aligned}
 \|R\|&\le64N^2,&
 \|R_P\|&\le36N,\\
 \|R_K\|&\le56N+120N^2<58N,&
 \|R_U\|&\le56N+240N^2<60N,\\
 \|R_V\|&\le8N .
\end{aligned}
 \tag{W.4}
$$
特别所有一阶系数均小于 $64N$。准确链式法则是
$$
 R_\theta=R_PU+R_KV+R_UU_\theta+R_VV_\theta .
 \tag{W.5}
$$
它保留依赖 $U,V$ 的完整角导项；没有将非线性强行变为零阶项。
由 (W.4)–(W.5)，两个方程中的非线性总贡献至多为
$128N_b^2+64N_b\mathcal D N_b$。

对实参考系数 $A(t)$，各 Fourier 绝对值的 Dini 导数保留准确的
线性负对角项。因此在移动角宽 $\sigma(t)$ 上，
$$
 \frac{d^+}{dt}N_b
 \le [z(A)+1024N_b]N_b+
       [b(A)+1024N_b+\sigma'(t)]\mathcal D N_b,
 \tag{W.6}
$$
其中
$$
 z(A)=\max\{-A-1,-2A\},\qquad
 b(A)=\max\{\sqrt3,|A|/\sqrt3\}.
 \tag{W.7}
$$
角系数由每对的矩阵
$\left(\begin{smallmatrix}0&1\\-A&0\end{smallmatrix}\right)$
在固定权 $(\sqrt3,1)$ 下的列和给出。
(W.6) 对复标签同样成立，因为 $A,w$ 是固定的实背景；
没有要求扰动本身取实值。

## 3. 真实主平台的角费及负零阶项

在首次 $N_b=2^{-20}$ 之前，$1024N_b\le2^{-10}$。
逐类选择角宽下降率如下：

| 实际区间 | 角宽下降率 $-\sigma'$ | 线性 $z(A)$ 上界 | 由 (W.6) 得到的零阶上界 |
|---|---:|---:|---:|
| $q=2$ 主平台 | $7/4$ | $-4$ | $-3$ |
| 其余 connector 短段 | $5$ | $14$ | $20$ |
| 整个双 bump 区间 | $7/4$ | $-7/4$ | $-1$ |

所有角导项都严格吸收。主平台及双 bump 使用
$\sqrt3<111/64<7/4-2^{-10}$；短段使用
$7/\sqrt3<17/4<5-2^{-10}$。双 bump 有 $|A|<9/8<3$，
所以这里的 $b(A)$ 确为 $\sqrt3$。

长平台仍是椭圆 Cauchy 段；表中已经支付了它的 $|m|$ 增长，
没有断言该传播在同一角宽上有界。其负零阶项只是在付清角费之后
才被使用。

总角费严格小于
$$
 \Gamma=\frac74\frac{505}{4}
            +5\frac12+\frac74\frac{75}{16}
       =\frac{14825}{64}=231.640625.
 \tag{W.8}
$$
完整能量的增长只来自总长小于 $1/2$ 的短段，因而
$$
 \sup_t N_b(t)\le e^{20L_s}N_b(0)<e^{10}N_b(0)<2^{20}N_b(0).
 \tag{W.9}
$$
本篇不需要牺牲一半初始角宽来制造额外小量。

## 4. 同一原标签图在权 224 球上的真实延拓

固定
$$
 \beta=224,\qquad
 \|a\|_{\ell^1_\beta}=\sum_{m\in4\mathbb Z\setminus\{0\}}
                     e^{\beta|m|}|a_m|<\frac14 .
 \tag{W.10}
$$
$a_m$ 仍是原 R72/R115 实际内部层 $b_m$ 上的标签。
源 R72 的任意绝对角宽定理允许把所有 $\tau_j$ 同时移到
$\tau_j+\beta$；层编号、真实传递矩阵及低/高分割完全不动。
正卷积权的次乘性
$e^{\beta|m_1+\cdots+m_k|}\le\prod_i e^{\beta|m_i|}$
保留全部非线性估计。因此同一固定点给
$$
 X_\beta:=\|X^{[\beta]}(a)\|_{\mathcal X}
       <\frac{13}{4}\|a\|_{\ell^1_\beta}<1.
 \tag{W.11}
$$
去权后它满足原 R115 的方程、标签及单位状态球；固定点唯一性说明
这就是原图的限制。它在旧 $\ell^1_{8192}$ 球上的延拓也由同一
Cauchy 问题的唯一性与旧续篇一致。

记 $\tau=5177/400$、$d=9/400$。R119 的实际 cut128 物理换算在
$$
 \sigma(0)=\tau+\beta-d/4
 \tag{W.12}
$$
上给 $N(0)<2^{16}s_*X_\beta$，其中
$s_*=b^7\delta^{15/4}<2^{-484}$。完整 mean 已由原 holonomy 小根计入。
因此
$$
 N_b(0)<2^{17}s_*X_\beta<2^{-467}X_\beta .
$$
结合 (W.9) 得到
$$
 \boxed{\quad
   \sup_{\,{\rm connector+both\ bumps}}N_b
        <2^{-447}X_\beta .
 \quad}                                                     \tag{W.13}
$$
右侧远小于 $2^{-20}$，故首次越界不可能发生，完成自洽闭合。

全频构造可逐字使用 R119 的 Fourier 逼近论证，但其能量换为
(W.6)：令 $U=P_\theta,V=K_\theta$，投影 (W.2) 前两式，得到有界
复解析有限 ODE；(W.6) 与频率截断无关。每个严格窄于 $\sigma(t)$
的条带都有统一指数 Fourier 尾及时间导数界，故极限满足完整方程。
对两解相减，在更窄条带把系数差乘背景角导当作有界零阶项，
再用相同严格角宽余量与 Gronwall 得唯一性及标签的局部一致全纯
依赖。有限投影不必保存 holonomy；holonomy 恒等式只对最终完整
PDE 使用。实际分段的 $A,w$ 连续，故不需假定它们径向解析。

## 5. 完整两迹、mean 和实际物理窗口

由 (W.8)、(W.12)，全程最小角宽满足
$$
 \sigma(t)>
 \tau+\beta-\frac d4-\frac{14825}{64}.
 \tag{W.14}
$$
选择
$$
 \sigma_{\rm raw}=\tau+\beta-235=\frac{777}{400}=1.9425,
 \qquad
 \sigma_{\rm grounded}=\tau+\beta-236
                       =\frac{377}{400}=0.9425.
 \tag{W.15}
$$
准确余量为
$$
 \sigma(t)-\sigma_{\rm raw}>
 235-\frac9{1600}-\frac{14825}{64}
 =\frac{2683}{800}>3.
 \tag{W.16}
$$
因此所有至多四阶的有限角多项式费用均小于1：
对 $M\ge4$、$0\le j\le4$，$M^je^{-3M}<1$。
grounded 转换另外保留完整1单位角宽。
两种输出宽度都严格大于真实下游物理窗口 $1/512$。

在同一 $u=B$ 切口定义
$$
 f_B=\frac{(v_B)_\perp}{a_Bw_B},\qquad
 k_B=\frac{(v_a)_\perp(B)}{w_B},\qquad
 \lambda_B=(v_B)_0 .
 \tag{W.17}
$$
因为 $U=(f_B)_{\theta\theta},V=(k_B)_\theta$，全部非mean迹满足
$$
 \sum_{m\ne0}e^{\sigma_{\rm raw}|m|}
       \bigl(|m|^2|(f_B)_m|+|m||(k_B)_m|\bigr)
       \le N_b(B)<2^{-447}X_\beta .
 \tag{W.18}
$$
这是同一物理切口、同一北向号数下的两迹，不是假造一个 Robin 高度行。
完整 mean 由
$$
 v_0(t)=v_0(0)+\int_0^t a(s)w(s)K_0(s)\,ds
 \tag{W.19}
$$
保留，独立平移 $\lambda$ 也保留。完整方程的准确恒等式
$M_t=0$ 给 $M\equiv1$，所以各接缝都使用同一个 holonomy-one
小根；没有对 mean 施加非零模的额外指数衰减。

R119 (119.31)–(119.34) 的 normal/grounded 高度、通量、水平位移
与 shear 公式在 (W.15) 上全部合法。完整水平原函数由同一
holonomy 恒等式取得，而非只重建有限模式。物理二阶估计只用
$w/a<5/18$ 及 $w<1$，故整个有限 connector 加双 bump 有
$$
 \|F_a-F_0-\lambda e_z\|_{C^2}
 <2^{17}\sup N
 <2^{-430}X_\beta
 <2^{-428}\|a\|_{\ell^1_{224}}.
 \tag{W.20}
$$
这里沿用 cut128 平均高度为0的规范；平盘高度仍是输出。
内部所有接缝通过同一 PDE 匹配完整二 jet，平尾端仍是原 R115
的完整 $C^2$ 零延拓。

同样证明对任意更大 $\beta$ 有效：把 (W.12)、(W.15) 中的
$224$ 换成该 $\beta$，(W.13) 不变。因而在旧 $\beta=8192$ 球上，
raw 输出实际可提高到 $\tau+7957$，grounded 到 $\tau+7956$。
这不是对较大标签域白加角宽；每个宽度都由对应输入权支付。

## 6. 真实线性输入及仍保留的相对逆问题

[R15 实际锥续篇](R15-supplement-actual-dominant-cone-and-exponential-label-weight.md)
对 R74 真实线性解、$B$ 后齐次的普通源合同给
$$
 |a_m^{\rm tail}|
 \le \exp[(-T/2+2033)|m|]A_m,\qquad T=2^{24}.
$$
所以这里同一真实线性输入满足
$$
 \|a^{\rm tail}\|_{\ell^1_{224}}
 \le e^{-4(2^{23}-2033-224)}\sum_m A_m
 =e^{-33545404}\sum_m A_m .
 \tag{W.21}
$$
原普通源的物理单位不变；$B$ 后非齐次 particular 仍需 R74
的独立完整费用。mean 通量不乘这个非零模因子。

权8192是旧粗主部预算与一半条带的幅度牺牲给出的充分域，
并非原内部标签图的必要阈值。(W.10)–(W.20) 证明了实质的扩大。
不过不能从此断言权128已经足够，或非线性高输入逆已经闭合。

具体地，现有 [联合 Schur 归一化续篇](R119-supplement-joint-tail-label-schur-normalization.md)
证明的原点逆仍是
$$
 \|D_0^{-1}g\|_{\ell^1_\beta}
 \le\frac1{16}\|g\|_{\mathcal Z_{\beta+1850}},
 \qquad D_0=DT_k(0)+\mathsf C_LDT_f(0).
 \tag{W.22}
$$
在新 $\beta=224$ 域内，(W.22) 需要输入宽2074，而 (W.18)
只直接授予 $\sigma_{\rm raw}=1.9425$。长段 screening 不能在
没有证明的更宽背景上使用。即使保持 $\beta=8192$ 并使用新的
$\tau+7957$ 输出，也仍小于要求的10042。更精确的基态传递预算
可以降低1850，但仅改变统一输入权不能消去一个真实的固定宽度差。

下一算子缺口仍是实际混合尾的
$DT_k(a)+\mathsf C_LDT_f(a)$ 在真实角图、完整两迹及 mean 下的
相对逆，或具有同等强度的联合非线性解法。
本篇没有把绝对小的 chart 导数、低图，或有限个标量相位条件
当成这个全空间结论。

## 7. 可重放的准确预算

[有理门程序](../scripts/fourfold_balanced_connector_label_domain_20261113.py)
和 [报告](../notes/2026-11-13-R119-balanced-label-domain-budget.json)
核验真实长度、非线性商法则、各段角宽余量、完整增长指数、
物理窗口及实际线性权重差。输入是上面逐项证明的实际对象界；
程序没有声称进行一个不可见的数值非线性求解。
