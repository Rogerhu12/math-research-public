# R119 续篇：真实平端平均模 Green、物理通量域与完整开放内部逆

2026-11-14，visible-exact / tail_connector。

**状态：解析证明，已由 root 与 tail_connector 独立核对。** 本篇接
[开放非零模逆](R119-supplement-open-radial-network-fractional-moment-and-actual-nonmean-inverse.md)
的同一公共参数、同一实际背景及同一权
$$
 \nu_j=2^{-432064}(j+5)^{-4166}\delta_j^{671/20},
 \qquad \delta_j=(2/25)2^{-j}.
 \tag{M.1}
$$
先在真实平端通量为零、平均高度有有限极限的端口域上反演
径向平均模，再以原完整 mixed 差反演全部 remaining 内部未知。
物理 mean 使用完整根乘子恢复，不被 canonical 零模代替。
外侧尚未覆盖的负分量、connector 和 regular 返回均保留为真实外条件。

本篇的平端条件是明确的物理两迹条件；它不由弱状态权自动推出。
这里所得仍是开放内部算子。最后的原强标签/source 映射、完整
$C^2$ 重建、外边界和联合参数行须继续消费，不能从本篇的
弱端口逆免费取得。

## 1. 真实开口在哪个根

[原实际胞元枚举](R119-supplement-actual-negative-band-metric-parameters.md)
(M.1)--(M.4) 的五个平台按 $t=\log r$ 增方向依次为
$$
 1,\quad K_j/\delta_j,\quad\delta_j/(65/64),
       \quad1/\delta_j,\quad c_j .
$$
第一、第三个过渡是两条上升坡，各含一个完整 positive 元件。
[原内部指标](R119-supplement-joint-actual-negative-band-return-kam.md)
(K.3) 规定 $(j,1)$ 在胞元 $j$ 内，$(j,2)$ 跨过 $j,j-1$ 接缝；
$(129,2)$ 在 cut128 截断，未作为完整两根内部元件。

定义 $e_X$ 为第129胞元第二个完整 positive 元件的**外侧真根**。
若在该胞元临时按 $t$ 增方向枚举四根，它是第四根；本篇不改变
原有根符号。整个相邻 positive 元件保在内部接线 $P$ 中，
$e_X$ 的输入、输出就是开放篇的 $X$ 端口。
从 $e_X$ 向外的未完整 $(129,2)$、cut128 后的实际 connector、
固定停止点 $25/8$ 及 regular 条件另保。

因此 $e_X$ 不是 cut128 的 physical-height 截面，也不是远端 $B$。
它的密度、斜率和根框架都由第129胞元的原根门支付。
这一编号不添加物理反射。

## 2. 去掉共同尺度的准确平均模两态

写 $J=j+5$，按[当前全标签合同](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
(C.2),(C.40),(C.46)，令
$$
 \mu_j=\epsilon m_j,\qquad
 m_j=\begin{cases}
       \delta_j^6,&j\le4096,\\
       \delta_{4096}^{3/2}\delta_j^{9/2},&j>4096,
      \end{cases}
 \qquad \mu_0={\epsilon\over\rho}\,\mathfrak m,
 \quad\mathfrak m={m_jp_*\over r^8}.
 \tag{M.2}
$$
这里 $\rho$ 是同一真实物理缩放。先处理已经送到根端口的 affine
源；普通/weak 体源的准确入口在第9节保留。
以 $\pi$ 表示总物理通量，归一为
$$
 H=\sqrt{\epsilon/\rho}\,h,\qquad
 P=\sqrt{\rho/\epsilon}\,\pi .
$$
在径向 mean 的齐次开段，准确有
$$
                  H_t=\mathfrak m^{-1}P,\qquad P_t=0 .
 \tag{M.3}
$$
这个 determinant-one 变换保 Green pairing。
没有把 $\epsilon$、$\rho$ 当成1；最后恢复物理高度和通量时
分别乘 $\sqrt{\rho/\epsilon}$、$\sqrt{\epsilon/\rho}$。

真实 $m_j$ 满足
$$
 \delta_j^6\le m_j\le\delta_j^{9/2},\qquad
 {m_j\over m_k}\le2^{-(9/2)(j-k)}\quad(j\ge k).
 \tag{M.4}
$$
两处规范切换均包含在此式：第一段相邻比为 $2^{-6}$，
后段为 $2^{-9/2}$。

胞元的真实 $t$ 长度小于 $8\delta_j$。
由 $1\le r\le2$、$p_*\ge\delta_j/2$，
$$
 \int_{\text{胞元 }j}\mathfrak m^{-1}\,dt
                       <2^{12}m_j^{-1}.
$$
逐层使用 (M.4)，从任一第 $j$ 胞元根到 $e_X$ 的电阻因此满足
$$
 \int_t^{t_X}\mathfrak m^{-1}\,ds<2^{13}m_j^{-1}.
 \tag{M.5}
$$
它不跨过 $e_X$ 去使用未知外返回。

## 3. 平均模原 Airy 框架与开放端 Robin 行

在根 $e$，置
$$
 q_e={\alpha_{0,e}\over\epsilon/\rho}
       ={b_em_{\ell(e)}p_*(t_e)\over r_e^8}.
 \tag{M.6}
$$
$\ell(e)$ 是根真正所在的胞元。
[原联合根图](R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md)
(J.22)--(J.25),(J.39) 给
$\alpha_0=b\mu_0$ 于根、$|\ell_{0,\xi}|<8$。
所有新增控制只在下降坡，根 germ 准确不变。
一个内部窗记作第 $j$ 层时，其根属于 $j$ 或 $j-1$；
将这个真实邻胞比计入，足够的共同门是
$$
 2^{-16}m_j\delta_j^{-5/4}<q_e
      <2^{176}J\,m_j\delta_j^{-13/4}.
 \tag{M.7}
$$
确实原根斜率为
$\delta_j^{-9/4}<b_e<2^{32}\sqrt J\,\delta_j^{-9/4}$，
$1\le r\le2$、$\delta_j/2\le p_*\le2^{128}/\delta_j$；
相邻 $m$ 比至多64。显示的16、176 bits 已覆盖这些因素。
特别
$$
 q_e^{-1/2}<2^8\delta_j^{-19/8},\qquad
 q_e^{1/2}<2^{88}\sqrt J\,\delta_j^{5/8}.
 \tag{M.8}
$$

[R39 的完整 mean 框架](R39-finite-component-airy-transfer-input.md)
(3.1)--(3.4) 准确是
$$
 D_{\sigma,0}(\xi)=c(1+i\sigma\xi/\pi),\qquad
 \det F_0=-2ic^2/\pi,\qquad c=c_A^{-1/2}.
$$
其初值证明也给 $c,c^{-1}<4$：
$\Gamma(1/3)<4$、$\Gamma(2/3)<2$，
$\Gamma(1/3)>9/4$、$\Gamma(2/3)>9/10$，
故 $9/40<c_A<16/9$。

由原物理恢复式，在根
$$
 u=\sqrt q\,H,\qquad
 u_\xi={\ell_{0,\xi}\over2}\sqrt q\,H+
                                  {\varsigma P\over\sqrt q}.
$$
因此原两个波幅准确为
$$
 z_\sigma=\gamma_{e,\sigma}H+\chi_{e,\sigma}P,
$$
$$
 \gamma_{e,\sigma}={\sqrt q\over2c}
                  (1-i\sigma\pi\ell_{0,\xi}/2),\qquad
 \chi_{e,\sigma}={-i\sigma\pi\varsigma\over2c\sqrt q}.
 \tag{M.9}
$$
真实右根的 $\varsigma=-1$ 保留。
在 $e_X$ 取其实际 incoming 槽 $\sigma_X$，记
$\gamma_X,\chi_X$。由于全部参考系数为实，
$$
 |\gamma_X|\ge\sqrt{q_X}/8,\qquad
 \kappa_X:=-\chi_X/\gamma_X,\qquad
 |\kappa_X|\le4/q_X<2^{18}m_{129}^{-1}.
 \tag{M.10}
$$
零外输入准确是 $H(t_X)=\kappa_XP(t_X)$。
这只是开放逆的边界行，尚未施加外部 regular 返回。

## 4. 根源是完整两态跳量

径向 mean 的网络式为 $x=P_0S_0x+g$。
在每个根令 negative 元件的 outgoing 与相邻 positive 的
incoming 相同，另一波槽相差 $g_e$。
这与原网络方程双向等价；没有对 transmission 作除法。

固定源的真实有向物理跳量
$(a_e,b_e)=[(H,P)]_{t_e-}^{t_e+}$ 等于某个准确符号乘
$$
 \begin{pmatrix}
  c/\sqrt{q_e}\\
  \varsigma_e c\sqrt{q_e}
          (i\sigma_e/\pi-\ell_{0,\xi}/2)
 \end{pmatrix}g_e .
 \tag{M.11}
$$
它保两行及法向号。因而
$$
 |a_e|\le2^3q_e^{-1/2}|g_e|,\qquad
 |b_e|\le2^7q_e^{1/2}|g_e|,
$$
$$
 |z_e|\le2^7(\sqrt{q_e}|H|+q_e^{-1/2}|P|).
 \tag{M.12}
$$
这些是原波源到物理 jump 的费用，未把 weak 体源范数称作
一个单位端口 jump。

## 5. 真平端 Green 核及其收敛域

设 $t_f$ 为平端，明定
$$
               P(t)\longrightarrow0,\qquad
               H(t)\longrightarrow\Lambda\in\mathbb C
                      \quad(t\downarrow t_f).
 \tag{M.13}
$$
$\Lambda$ 是唯一整体高度输出，不是逐胞的独立常数。
先对有限个根源证明。一个源 $(a_k,b_k)$ 在 $t_k$ 的准确解为
$$
 \begin{split}
 P^{(k)}(t)&=b_k\,\mathbf1_{\{t>t_k\}},\\
 H^{(k)}(t)&=-a_k\,\mathbf1_{\{t<t_k\}}+
 b_k\left[\kappa_X-
       \int_{\max(t,t_k)}^{t_X}\mathfrak m^{-1}(s)\,ds\right].
 \end{split}
 \tag{M.14}
$$
它的两跳恰为 $(a_k,b_k)$，开段满足 (M.3)，外端满足 (M.10)，
内端满足 (M.13)。根两侧任一真实迹均可使用，源点自身的
particular 值也包含在 (M.14)。

若 $\|\nu^{-1}g_Z\|_{\ell^2}<\infty$，则
$$
 \sum_k\left[|a_k|+
 |b_k|\left(|\kappa_X|+
       \int_{t_k}^{t_X}\mathfrak m^{-1}\right)\right]<\infty .
 \tag{M.15}
$$
例如 (M.7),(M.4) 使方括号小于
$2^{128}J_k\delta_k^{-37/8}|g_k|$。
代入 $g_k=\nu_k(\nu_k^{-1}g_k)$ 后，剩下正幂
$671/20-37/8=1157/40$，Cauchy--Schwarz 的几何和收敛。
所以 (M.14) 可以绝对求和，给准确高度
$$
 \Lambda=-\sum_k a_k+
       \sum_kb_k\left[\kappa_X-
                \int_{t_k}^{t_X}\mathfrak m^{-1}\right],
 \tag{M.16}
$$
并在整个径向区间具有 (M.13) 的极限。

唯一性不能由弱权代替：齐次差的 $P$ 是一个全局常数；
(M.13) 迫使它为0，随后 $H$ 是常数，(M.10) 迫使 $H=0$。
若不施加 (M.13)，非零常通量产生的奇异解仍可能落在弱
$\nu$ 状态空间。本篇明确排除它，而不把它当作已经消失的核。

## 6. 完整根块的定量核与新权

记 $d=|j-k|$，$l=\min(j,k)$。
由 (M.7),(M.4)，当 $j\ge k$，
$$
 \sqrt{q_j/q_k}
 \le2^{96}\sqrt{J_j}\,\delta_k^{-1}2^{-5(j-k)/8},
$$
$$
 {\sqrt{q_jq_k}\over m_k}
 \le2^{176}\sqrt{J_jJ_k}\,
                   \delta_k^{-13/4}2^{-5(j-k)/8}.
 \tag{M.17}
$$
另一个方向交换 $j,k$。
(M.14) 的 height-jump 项只向内传播；
flux 项的电阻在更外的一层停止，因此分母正是 $m_l$。
常数 $\kappa_X$ 也由 (M.10) 和 $m_{129}\ge m_l$ 控制。
(M.12) 的反向 flux 输出同样由第一式控制。

合并源自身、两向传播、真实一层编号差和每胞至多四个
incoming 根槽，得到安全的逐块界
$$
 \boxed{\quad
 |(R_{Z,0})_{jk}|
 \le2^{512}J_jJ_k\,\delta_{\min(j,k)}^{-4}
                              2^{-|j-k|/2}.
 \quad}                                                     \tag{M.18}
$$
这里 $R_{Z,0}$ 是原开放 canonical-mean 网络在 (M.13) 域上的
真正 inverse。512 bits 的来源可直接核：
两次 (M.12) 至多14，电阻及 $\kappa_X$ 取20，
(M.17) 至多176；三项求和、相邻根重编号和四槽矩阵 norm
再宽放128，总数小于338。

由于
$\nu_j\nu_k\delta_{\min(j,k)}^{-4}
 \le2^{-864128}J_j^{-4166}J_k^{-4166}$，
(M.18) 的完整行列几何和给
$$
 \boxed{\qquad
       \|\nu R_{Z,0}\nu\|<2^{-860000}.
 \qquad}                                                     \tag{M.19}
$$
例如至多8个槽的
$8[1+2\sum_{d\ge1}2^{-d/2}]<64$，
所以未粗化的指数小于 $-863600$。
没有用有限层实验替代此无限和。

在实际非零外 mean 输入 $u_X$ 下，径向无源补解准确为
$$
       P=0,\qquad H=u_X/\gamma_X,\qquad
       y_X=(\gamma_{X,\rm out}/\gamma_X)u_X .
 \tag{M.20}
$$
最后的系数模长为1，但不是预先添加的外反射。
它是内部平端问题产生的实际径向响应。
整体高度读数由 $u_X/\gamma_X$ 及 (M.16) 给出。

## 7. canonical 平端域与实际物理 mean 两迹

这里先说根端口域，随后说明体源范围。
令 $x=x_R+x_D+x_H$ 是原有序 H/D 重建出的全部根 incoming，
且
$$
 \mathfrak X(x):=
 \|\nu x_R\|+
 \|\nu F^{-1}x_D\|+
 \|\nu F^{-1}x_H\|<\infty,\qquad
 F_j=2^{4096}J^4\delta_j^{-5}.
 \tag{M.21}
$$
完整 high/low Poisson 已在开放篇 (B.26)--(B.31) 对这些权重付。
于是每个真实窗口的完整 $L^2$ input 小于
$F_j\nu_j^{-1}\mathfrak X(x)$，邻胞因素可收一个固定 $2^{92}$。
不假定未知量本来有 $\nu^{-1}$ 强状态权。

实际共同 unitary $H_a$ 按原
[root-wave 完整比较](R119-supplement-complete-root-wave-network-and-high-Schur-difference.md)
(V.16)--(V.17) 准确保持 canonical mean。
在每个 negative 元件，用 $x_Z$ 和参考 mean scattering
$S_{-,0,00}x_Z$ 恢复一对径向 mean 根迹
$(H_{Z,0},P_{Z,0})$。
实际根迹则用原完整两振幅和 (J.39)--(J.40)：
$$
 \langle h\rangle
  =\langle\alpha^{-1/2}u\rangle,\qquad
 \langle p\rangle
  =\varsigma\langle\sqrt\alpha
                   (u_\xi-\ell_\xi u/2)\rangle .
 \tag{M.22}
$$
右边所有非零模都保留，尤其 $u=\sqrt\alpha\,h_{\rm const}$
不是 canonical 常数。

给出域比较的完整费用。原 (J.24)--(J.25) 的真实角条带使
$e^{\pm l/2}-1$、$l_\xi$ 的所需 $H^{1/3}$ Fourier norm
小于 $2^{36}n_e$，其中 $n_e\le4\mathcal N_j\mathcal X$。
[完整自由两行端架](R119-supplement-complete-free-Airy-two-row-frame-and-low-frequency-erratum.md)
(A.2)--(A.4) 在真实根 $\xi=0$ 精确给非零模
$D_{\sigma,M}(0)=c(M/b)^{-1/3}[\operatorname{Bi}(0)+i\sigma\operatorname{Ai}(0)]$，
$D'_{\sigma,M}(0)=-c(M/b)^{1/3}[\operatorname{Bi}'(0)+i\sigma\operatorname{Ai}'(0)]$；
mean 是 $c,i\sigma c/\pi$。四个 Airy 初值绝对值小于1、$c<4$，
且 $M\ge4$，所以这是完整根初值而不是远场渐近式。
这些原准确初值给
$$
 \|u\|_{H^{1/3}}+\|u_\xi\|_{H^{-1/3}}
                  <2^8b_e^{1/3}\|(z_+,z_-)\|_{L^2}.
$$
因此由密度恢复产生的 mean 差小于
$2^{48}(q_e^{-1/2}+q_e^{1/2})b_e^{1/3}
               \mathcal N_j\mathcal X\,\|x_i\|$。
这是对 $H^{-1/3}$ 第二迹的解析对偶，不要求未付的
$L^2$ 法向高频迹。

还必须保实际 outgoing 的差。
(V.14) 的真正 adjoint 一阶门以常数作为输出测试，给
$$
 \|\Pi_0(S_{-,a}-S_{-,0}):L^2\to\mathbb C^2\|
 \le2^{20200}J^{33}\delta_j^{-47}\mathcal N_j\mathcal X .
 \tag{M.23}
$$
径向 $S_{-,0}$ Fourier 对角且 $H_a$ 保 mean，
故没有另一个免费的 cross 项。
两次实际 source/trace 变换不在这里被删除。

将 (M.8),(M.12),(M.21),(M.23) 合并，足够的共同门为
$$
 \begin{split}
 &|\sqrt{\epsilon/\rho}\langle h\rangle-H_{Z,0}|
  +|\sqrt{\rho/\epsilon}\langle p\rangle-P_{Z,0}|\\
 &\hspace{12mm}
 <2^{460000}J^{4220}\delta_j^{-91}
              \mathcal N_j\mathcal X\,\mathfrak X(x).
 \end{split}
 \tag{M.24}
$$
可逐项检查其余量：两根迹的未粗化 $\delta$ 幂小于51，
而 $F\nu^{-1}$ 的幂是 $771/20=38.55$；
总幂小于90。其 bits 小于
$20500+436160+1000<460000$，$J$ 次方小于4220。
所有邻胞与两槽因子在显示的1000 bits内。

真正深层
$\mathcal N_j$ 的幂仍为 $31867/256$，
所以 (M.24) 的深端剩余幂是
$$
                  31867/256-91=8571/256>33.
 \tag{M.25}
$$
原 $\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}$ 只是固定常数，
没有从本式消去。全部有限前缀也有限。
因此沿任一趋向平端的真实根序列，(M.24) 趋0。

这证明：在 (M.21) 中，**明定的** radial mean 平端两迹域
与实际物理 mean 根两迹域等价。
若 ordinary/weak 原源有实际 particular，先按其原真实端口
加入该 particular；它的两条极限和 total/bare 端荷仍须按
原源合同提供。体源的 $L^2$ norm 本身不授予裸 $F^t$ 根迹。

对真正物理解，total mean flux 在开段满足原精确守恒式
$\partial_t\langle\pi\rangle=\langle f\rangle$；
因此可积原源下的通量平端条件与这些共尾根迹条件一致。
本篇不把仅有平均根迹极限称为整个高度场已 $C^2$ 延拓，
也不从该域比较推断原标签强范数。

## 8. 完整 remaining 内部逆及准确 mean 商

记 $\mathcal R_0$ 为径向非零逆与 (M.19) 的直和。
开放篇 (B.21)--(B.22) 及 (M.19) 给
$$
 \|\nu\mathcal R_0\nu\|\le1,\qquad
 \|\nu^{-1}\Delta S_{\rm rem}\nu^{-1}\|
                           <\eta=2^{-6000000}.
$$
在第7节明定的平端 mean 域上，真实 Neumann 级数于是定义
$$
 \boxed{\quad
 \mathcal R_a=(I-S_{\rm rem,a})^{-1}
        =(I-\mathcal R_0\Delta S_{\rm rem})^{-1}\mathcal R_0,
 \qquad \|\nu\mathcal R_a\nu\|<(1-\eta)^{-1}<2 .
 \quad}                                                     \tag{M.26}
$$
源域为 $\|\nu^{-1}k\|<\infty$，状态为 $\|\nu x_R\|<\infty$，
而 mean 另带 (M.13)/(M.22) 的真实平端条件。
(M.15) 保证每个 Neumann 修正都属于同一个 mean 域；
(M.24) 给它的物理解释。不能在没有该域的裸形式方程中
将 (M.26) 写成无条件 inverse。

也可按开放篇 (B.30)--(B.32) 先消非零块：
$$
 \begin{split}
 G_Z&=P_Zk+A_{ZN}R_{N,a}P_Nk,\\
 x_Z&=[I-R_{Z,0}(S_Z^{\rm eff}-S_{ZZ,0})]^{-1}R_{Z,0}G_Z,\\
 x_N&=R_{N,a}(P_Nk+A_{NZ}x_Z).
 \end{split}
 \tag{M.27}
$$
此处两个 cross、完整 mean source、真实外列均没有删除。
mean 逆的 Neumann 因子小于
$2^{-860000}\,2\eta$。
唯一整体平移由开放边界输入决定；闭合真实外问题后若保留
整体高度 gauge，只商去这一个真正物理常高度方向。

两侧唯一性在声明域内同样成立。对任一齐次解，径向非零块
逐频是真正有限 inverse，径向 mean 用第5节的物理唯一性。
右边 $\Delta S_{\rm rem}x$ 位于完整源域，所以
$\|\nu x\|\le\eta\|\nu x\|$ 迫使 $x=0$。
这没有假定弱状态自动满足平端条件。

## 9. 全部源与真实外返回的未删方程

严格沿开放篇 (B.31)，给定真实外输入 $x_X$ 后先形成
$$
 \widetilde g_H=g_H+C_Xx_X,\qquad
 k_L=g_L+A_{LX}x_X+F_H\widetilde g_H,\qquad
 k=k_R+F_Dk_D .
$$
现在全部 remaining 的解是
$$
 \begin{split}
 x_R&=\mathcal R_a k,\\
 x_D&=E_Dx_R+R_Dk_D,\\
 x_H&=E_H(x_R+x_D)+R_H\widetilde g_H.
 \end{split}
 \tag{M.28}
$$
高源仍须提供原 $H^1$ 窗，deep-low 源仍须提供
$\|\nu Fk_D\|$，remaining 源须提供 $\|\nu^{-1}k\|$。
这些真实输入同时使 (M.21) 有限；例如用权 $\nu F^{-1}$
读取高 Poisson，及原 low 双向门读取第二行即可。
不向任意裸 $L^2$ 外输入授予这些合同。

原外输出仍准确为
$$
 y_X=A_{XI}(x_R+x_D)+A_{XX}x_X+B_Xx_H+g_X .
 \tag{M.29}
$$
实际外问题若写成
$$
 x_X=\mathcal E_a y_X+f_X,\qquad
 \mathcal C_{\rm true}(x_X,y_X,\dot\Gamma,\lambda,\ldots)
                                      =f_{\rm true},
 \tag{M.30}
$$
必须保其真实 $\mathcal E_a$、有限约束、mean 与所有 affine 列。
(M.26) 不能把 (M.30) 换成辅助圆周平均中的 $x_X=z y_X$，
也没有证明 $I-\mathcal E_a\mathcal T_a$ 已可逆；
$\mathcal T_a$ 是 (M.28)--(M.29) 才定义的实际内部响应。

普通源仍按原 (C.42)--(C.43) 保留 $\mu_jp_*^2$；
weak 源保 $F^t,F^\theta$，原 Piola 和高度共轭中的
$-\frac12\nabla\ell\cdot\widetilde{\mathbf F}$ 保留。
两 mean total-DN 荷、negative particular、真实径向 jumps、
bare flux 需要的 $F^t$ 端迹也保留。
参数微分时，两列 $D\Gamma^*$、metric-source、端角导数和
$\dot H^*g$ 仍分别通过 (M.28)，不得由固定背景逆设为0。

本篇完成了此前剩下的平均模端口域和完整开放内部逆。
真实外部接合、原强源及标签权的最终连续映射、完整物理
平端正则与 nonlinear 全局方程继续作为下一实质步骤。
全文为解析推导，没有新增本地数值实验。
