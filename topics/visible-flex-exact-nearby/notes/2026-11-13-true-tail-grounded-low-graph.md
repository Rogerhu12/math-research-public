# R115 补充：真实 cut128 的低172高度图、全高输出与 grounded 两迹

2026-11-13，independent_audit。依赖 R115 全文，源 R72/R25 的对象和 blob 同 R115 §1。本篇只在实际 cut128 付 Cauchy 图及其真实 normal/ground-state 转换，**没有**把它改称 regular $r=25/8$ 端口的全频 Robin 更新。所有高输出和 mean 都保留。

## 1. 低输入图及全频输出

令 $\mathcal L=\{m\in4\mathbb Z:0<|m|\le172\}$，
$I_L:\ell^1(\mathcal L)\to\ell^1$ 为零延拓，
$E_{128}:\mathcal X\to\ell^1(\mathbb Z;\mathbb C^2)$ 为真实状态读取。
在 $\|a\|\le1/12$ 上，
$$
 B_a=\Pi_L E_{128}^{(1)}DX(a)I_L .
$$
源 R72 的低标签层都等于128，且基态的第一分量满足
$$
 \|B_0-I\|\le\frac{3q_G}{1-q_G}<\frac1{85}.
$$
由 R115 的 $\kappa<2^{-60}$，
$$
 \|B_a-I\|<\frac1{85}+2\kappa<\frac1{64},\qquad
 \|B_a^{-1}\|\le64/63 .                                    \tag{L.1}
$$
这里任意已选高标签保持固定，不将它们产生的高高度设为0。
物理图采用 R115 已固定的真实二面体对称子空间：反射相容的标签方向也保持反射关系。用全部正负 $4\mathbb Z$ 写 norm 并不解除该条件。其整体角平移后的共轭对称族具有同一估计；没有另外授予一个未固定的径向旋转规范。

低高度变化 $y_L$ 对应的**全部**规范两迹为
$$
 S_a y_L=E_{128}DX(a)I_L B_a^{-1}y_L .
$$
于是
$$
 \|S_a\|<4,\qquad
 \|S_a-S_0\|<16\kappa<2^{-56},\qquad
 \|DS_a[b]\|<512\kappa\|b\|.                               \tag{L.2}
$$
证明用
$$
 S_a-S_0
 =E_{128}(DX(a)-\mathcal H)I_L B_a^{-1}
  +E_{128}\mathcal H I_L(B_a^{-1}-B_0^{-1}),
$$
以及 $\|DX-\mathcal H\|<2\kappa$；未放宽的差常数小于 $9\kappa$。
微分 $B_a^{-1}$ 后，$\|D^2X\|<64\kappa$ 给最后一式。
$S_0$ 的高输出准确为0，故非零背景的所有 $|m|\ge176$ 输出都在
(L.2) 的同一个 norm 内。它们没有被删掉或截断。

## 2. 物理两迹及准确基态 shear

以下 $b$ 为参考 cut128 半径，$\rho_*$ 为实际等比尺度，
$\zeta=\epsilon\delta_{128}^{39/4}$，$w_c=\epsilon\delta_{128}^6/b^7$。
北帽物理高度记 $Z$，$Z>17/20$；参考正向高度是 $-Z/\rho_*$ 加常数。
改变这个整体符号同时改变两项 raw 高度状态，不改变任何 norm。

对一个北帽物理高度 Jacobi 场，令其参考高度为
$C=\dot Z/\rho_*$。非零模输入 norm 是
$$
 \|(C,C_r)\|_{\mathfrak C_\tau}
 =\sum_{m\ne0}e^{\tau|m|}
  \max\left\{
    \left|\frac{\nu_m C_m}{b^4\zeta}\right|,
    \left|\frac{C_{r,m}/b^3-m^2C_m/b^4}{\sqrt{12}\zeta}\right|
  \right\},\qquad \tau=\tau_{128}.                         \tag{L.3}
$$
$C_r$ 是参考半径导数，故物理 $\dot Z_{r_{\rm phys}}=C_r$。
以物理 grounded 变量 $v=F\cdot V/Z$ 和 tail 的 outward 正半径
conormal $p=(Y_z^2A\nabla v)\cdot dr_{\rm phys}$ 定义对应输出：
将 (L.3) 中 $C$ 换为 $v/\rho_*$、$C_r$ 换为 $p/w_c$。
零模用 $v_0/(\rho_*b^4\zeta)$ 和
$p_0/(\sqrt{12}w_c b^3\zeta)$ 单列。另一侧域的 outward conormal
方向相反，应在 matching 行准确翻号。

零标签基态上，R115 (115.39) 逐项给以下准确矩阵，而非只给主阶：
$$
 \eta=\frac{\rho_*b w_c}{Z},\qquad
 T_m(\eta)=
 \begin{pmatrix}
  1&-\eta m^2/\sqrt{12}\\
  -\sqrt{12}\eta/((m^2-1)(1+\eta))&
  1+\eta^2m^2/((m^2-1)(1+\eta))
 \end{pmatrix}.                                           \tag{L.4}
$$
直接有 $\det T_m=1$。这是实际高度、水平位移、normal scalar、
ground state 和动量 shear 的联合换元；不是将高度微分改名为通量。

因 $\rho_*<1$、$\epsilon\le1$、$b>1$、
$\delta_{128}<2^{-131}$、$Z>17/20$，
$$
 0<\eta<2^{-785}.                                          \tag{L.5}
$$
在 $|m|\le172$ 上 $T_m-I$ 的 norm 小于 $2^{-771}$。
对全频付任何明确正角宽损失也可界它，但没有同宽零阶结论：
其第一行确含 $m^2$。这保留了真实两迹的导阶。

## 3. 非零标签的准确物理转换

记源尾的 $k=w+\kappa$、$p_s=z_\theta/r$、
$t=1-p_s^2$、$D=E-k^2-Ep_s^2$。用 $p_s$ 与 conormal $p$ 区分。
在 cut128 的 R115 coframe 中，
$$
 l=r\sqrt t,\quad a_1=-k p_s/\sqrt t,\quad b_1=\sqrt{D/t},
 \qquad \alpha=\theta+\pi/2+\gamma .
$$
给北帽 $C,C_r$ 时，源高度的变化是
$\dot k=-C_r,\ \dot p_s=-C_\theta/r$。准确有
$$
 \dot l=-r p_s\dot p_s/\sqrt t,\qquad
 \dot a_1=-p_s\dot k/\sqrt t-k\dot p_s/t^{3/2},
$$
$$
 \dot b_1=-k\dot k/(b_1t)-k^2p_s\dot p_s/(b_1t^2),
$$
$$
 \dot G=D^{-1/2}\left[
 \frac{\dot k(p_s)_\theta+k(\dot p_s)_\theta}{t}
 +\frac{2k(p_s)_\theta p_s\dot p_s}{t^2}\right]
 +(1+k(p_s)_\theta/t)D^{-3/2}(k\dot k+Ep_s\dot p_s),
 \quad G=\alpha_\theta .
 \tag{L.6}
$$
对真实 homogeneous tail Jacobi 数据，$\langle\dot G\rangle=0$；
这由完整 mean 导数决定 $C_{r,0}$，不是任意将 mean slope 置零。
令 $\dot\gamma=\partial_\theta^{-1}\dot G$，则旋转坐标中的完整水平
位移及其径向导数为
$$
 (\partial_\theta+i)V_h=e^{i\gamma}(i\dot l-l\dot\gamma),
 \quad
 (V_h)_r=e^{i\gamma}
       [\dot b_1+i\dot a_1+i(b_1+i a_1)\dot\gamma].
 \tag{L.7}
$$
这里 $V_h$ 是物理水平位移除以 $\rho_*$，旋转基的准确导数已经保留。
没有逐 Fourier 列假定其为对角乘子。

若 $R_h$ 是背景的同一旋转水平坐标，设
$$
 c_v=C+\frac{\rho_*}{Z}R_h\cdot V_h,\qquad
 S=F\cdot\nu,\qquad c=\frac{Z^2}{S^2}.
$$
点积按真实二维双线性表达延拓。实际 grounded 两迹准确是
$$
 \frac v{\rho_*}=c_v,\qquad
 \frac p{w_c}=\frac c{\sqrt D}
 \left[\frac{k+E(p_s)_\theta}{Ew_c}(c_v)_r
       -\frac{\kappa_\theta-p_s}{r w_c}(c_v)_\theta\right].
 \tag{L.8}
$$
$(c_v)_r$ 保留 $Z_r=-\rho_*k$、
$(R_h)_r$ 及 (L.7)，不以 $C_r$ 直接替代。
本式来自
$$
 Y_z^2A^{rr}=\frac{Z^2(k+E(p_s)_\theta)}
                 {\rho_* S^2 E\sqrt D},\qquad
 Y_z^2A^{r\theta}
    =-\frac{Z^2(\kappa_\theta-p_s)}
                  {\rho_* S^2 r\sqrt D}
$$
在参考 material $(r,\theta)$ 密度中的表达。因 $v=\rho_*c_v$，
尺度 $\rho_*$ 准确相消，和 (L.4) 一致。

整体物理竖直平移另为准确列 $v=\lambda_{\rm phys},p=0$。
因此可把 cut128 的平均高度作为一个独立有限坐标：通过调整整体
高度常数使 label 方向 $C_0=0$，而平帽的最终高度仍由完整 mean
积分输出。没有同时固定 cut mean 和 flat mean。

## 4. 一个实际可消费的转换常数

取
$$
 d=9/400,\quad \sigma=\tau-d,\quad
 \sigma_0=\tau-d/4 .
$$
源 R72 (11.9) 对完整标签球给
$$
 R_c:=\mathcal R_{128,\sigma_0}
 \le12b^{10}\delta_{128}^{15/4}(ed/4)^{-1}\|X(a)\|
 <2^{-469}.                                                \tag{L.9}
$$
其中五项相对 norm 与源 R25 (2.1) 相同。
这用的是 whole Fourier/真实 mean，不是最低模样本。

为说明以下粗常数是有限运算所得，令
$\|f\|_{\sigma,k}=\sum_m e^{\sigma|m|}(1+|m|)^k|f_m|$。
它是乘法 norm 常数1的代数。由于
$1+8/(\sigma_0-\sigma)<512$，
$$
 \|f\|_{\sigma,8}\le2^{72}\|f\|_{\sigma_0}.
$$
所有非constant相对背景量可因此统一记为
$R_d=2^{72}R_c<2^{-397}$。完整 mean 逆小于2。
由 (L.3)、$\nu_m\ge m^4/16$、$b\le2$ 得
$$
 \|C_\perp/\zeta\|_{\tau,4}\le625\|X_{128}\|,\qquad
 \|(C_r)_\perp/\zeta\|_{\tau,0}\le64\|X_{128}\|.
$$
支付 $d$ 后，可宽松取
$$
 I:=\|C/\zeta\|_{\sigma,6}
          +\|C_r/\zeta\|_{\sigma,4}
 \le2^{48}\|X_{128}\|                                      \tag{L.10}
$$
于 $C_0=0$ 的 compatible 数据；由 $\langle\dot G\rangle=0$ 解得
$|C_{r,0}|/\zeta\le128R_d I$，其自映系数小于 $1/2$，
已包含在 (L.10)。

下面把转换常数的有限运算列出，以免只凭“足够小”授予 (L.11)。
全部 planar 向量以两个旋转分量
$H_\pm=e^{\mp i\theta}(H_x\pm iH_y)$ 的最大 Wiener norm 衡量。
真实双线性点积是 $(H_+V_-+H_-V_+)/2$，乘法 norm 仍为1。
(L.7) 写出加号分量，减号分量把所有 $i,\gamma$ 同时改号；两者界相同。

令 $R=R_d$。完整相对变量满足
$\|K\|_{\sigma,8}\le2R$、
$\|\mathsf P\|_{\sigma,8},\|\mathsf P_\theta\|_{\sigma,8},
\|K_\theta-\mathsf P\|_{\sigma,8}\le R$。
因而
$$
 \|D-1\|_{\sigma,8}\le w_c^2(4R+6R^2),\qquad
 \|t-1\|_{\sigma,8}\le w_c^2R^2 .
$$
对 $|z|\le1/16$，幂级数给
$|(1+z)^{-3/2}-1|\le2|z|$、
$|(1+z)^{-2}-1|\le3|z|$。在同一 Banach 代数逐项使用这些式子，
得到 $\|\gamma\|_{\sigma,4}\le15w_c^2R$、
$\|R_h/b-1\|_{\sigma,4}\le32w_c^2R$。
准确
$$
 \frac{(\nu_h)_{\rm rot}}{\nu_z}
 =e^{i\gamma}\left(\frac{k}{\sqrt{tD}}+
                             \frac{i p_s}{\sqrt t}\right)
$$
和
$\|(Z-\overline Z)/\overline Z\|_{\sigma,4}\le\eta R/4$
故给
$$
 \frac S Z=\sqrt{D/E}(1+\chi),\qquad
 \|\chi\|_{\sigma,4}<8\eta .
$$
这里 $R_h/b-1$ 的“1”表示实轴径向基态；双 planar 分量均用该式。

均值方程的费用也可直接从 (L.6) 看出。将 $\dot G/w_c$
写成 $A_k\dot k+A_\theta(\dot p_s)_\theta+A_p\dot p_s$，
则
$$
 \|A_k-1\|_{\sigma,4}\le16R,\quad
 \|A_\theta-1\|_{\sigma,4}\le8R,\quad
 \|A_p\|_{\sigma,4}\le8R .
$$
零阶两项的角平均只剩 $\dot k_0=-C_{r,0}$。
这证明 (L.10) 中已用的
$|C_{r,0}|/\zeta\le128R I$；$128R<1/2$ 使它真正闭合。

(L.6)–(L.7) 及
$\|\partial_\theta^{-1}\Pi_{\ne0}:\mathcal A_{\sigma,3}
 \to\mathcal A_{\sigma,4}\|\le5/4$、
$\|(\partial_\theta\pm i)^{-1}\|_{4\mathbb Z}\le1$
进一步给下表。每行均除去所显示的共同尺度：

| 实际量 | norm | 上界 |
|---|---|---:|
| $\dot G/(w_c\zeta I)$ | $\mathcal A_{\sigma,3}$ | $64$ |
| $\dot\gamma/(w_c\zeta I)$ | $\mathcal A_{\sigma,4}$ | $128$ |
| $\dot l/(w_c\zeta I)$ | $\mathcal A_{\sigma,4}$ | $4R$ |
| $\dot a_1/(w_c\zeta I)$、$\dot b_1/(w_c\zeta I)$ | $\mathcal A_{\sigma,4}$ | 各 $8$ |
| $V_h/(w_c\zeta I)$ | $\mathcal A_{\sigma,4}$ | $2^{10}$ |
| $(V_h)_r/(w_c\zeta I)$ | $\mathcal A_{\sigma,4}$ | $2^{12}$ |
| $(c_v-C)/(\zeta I)$ | $\mathcal A_{\sigma,4}$ | $2^{13}\eta$ |
| $((c_v)_r-C_r)/(\zeta I)$ | $\mathcal A_{\sigma,4}$ | $2^{18}\eta$ |

例如最后一行准确保留
$(\rho_*/Z)(R_{h,r}\cdot V_h+R_h\cdot V_{h,r})
+\rho_*^2 k Z^{-2}R_h\cdot V_h$；
它的三个费用分别小于 $2^{13}\eta$、$2^{15}\eta$、$2^{15}\eta^2$，
总和严格小于所列 $2^{18}\eta$。

(L.8) 的两个系数因此满足
$$
 \left\|D^{-3/2}(1+\chi)^{-2}
           (1+K+E\mathsf P_\theta)-1\right\|_{\sigma,4}
       \le32(R+\eta),
$$
$$
 \left\|E D^{-3/2}(1+\chi)^{-2}
                  (K_\theta-\mathsf P)/b\right\|_{\sigma,4}
       \le8R.
$$
将上一表逐项相乘，保留 $C_{r,0}$，给
$$
 \|(p/w_c-C_r)/\zeta\|_\sigma
             \le2^{20}(R+\eta)I .
$$
再乘实际 $\nu_m/b^4$ 或 $m^2/b^4$、分别加入两个 mean 行，
总费用小于 $2^{24}(R+\eta)I$。所有这些正有理 majorant 在相邻
BigInt 程序中逐项检查；没有把程序当成对未知全局 PDE 的数值证明。

所以在自然规范两迹空间，真实转换 $\mathcal F_a$ 满足
$$
 \boxed{\quad
 \|\mathcal F_a-I_{\ne0,\,\text{zero mean flux}}\|
       _{\mathfrak C_\tau\to\mathfrak C_\sigma\oplus\mathbb C^2}
 \le2^{144}(R_c+\eta)<2^{-324}.
 \quad}                                                     \tag{L.11}
$$
这是有明确角宽损失的结论。上述费用中，$2^{72}$ 是背景8阶角权，
$2^{48}$ 是输入角权，$2^{24}$ 是上表之后已逐项保留的输出总和。
零高度/零通量的基态 mean 被保留；纯平移列本来就准确，不支付虚构
的高频权。

## 5. 真实低 grounded 图仍保全高输出

对 (L.2) 输出应用 (L.11)。在低高度投影上恢复 $\tau$ 的费用至多
$e^{172d}<64$，故其 grounded 低 Dirichlet 矩阵相对单位阵之差
小于 $2^{-316}$，有真逆 norm 小于2。竖直平移给平均高度准确单位列。
连同 mean 高度，其低 Dirichlet 矩阵准确是
$\begin{pmatrix}I+E_{LL}&0\\E_{0L}&1\end{pmatrix}$；
它的逆同时扣除 label 方向产生的 mean 高度，不同时强加 flat mean=0。
其余 mean 输出仍从 (L.8) 保留。

因此用**实际 grounded 低高度加平均高度**参数化后，完整两迹图
$\widetilde S_a$ 有
$$
 \|\widetilde S_a\|<8,\qquad
 \|\widetilde S_a-\widetilde S_0\|
       _{\ell^1(\mathcal L)\oplus\mathbb C
          \to\mathfrak C_\sigma\oplus\mathbb C^2}
 <2^{-55}.                                                  \tag{L.12}
$$
例如每个图因转换及低 Dirichlet 逆引入的误差小于
$8\cdot2^{-324}+4\cdot2^{-315}$；两个图相减，再加
$16\kappa<2^{-56}$，得 (L.12)。完整零模通量及所有
$|m|\ge176$ 行在输出中，未以“低图”之名忽略。

这给本题 finite augmented Schur 一个真实 tail-end 输入。
它仍不是全频 regular Robin perturbation：把该 finite incoming 图
及其全部高输出穿过实际 connector/长段，并在非零标签几何上证明
完整 high incoming 图的逆，需要额外强传播/反馈预算。
不能以 (L.12) 或 R74 的齐次标签小量代替该步骤。


## 6. 有限核验与范围

脚本 [fourfold_true_tail_grounded_low_graph.mjs](../scripts/fourfold_true_tail_grounded_low_graph.mjs)
只用本篇所列准确有理数和源 R115 的已证算子常数。它逐项核低图逆、
规范矩阵行列式、实际角宽/径向幂、mean 方程及上表的正有理包络；
完整小报告保存每个门。没有新原生尾 PDE 运行，也没有以摘要重建
任何丢失的原生大报告。

供 Schur 使用的仍是“有限低输入、完整高输出、真实 mean 两行”的
actual cut128 图。所有 high incoming 标签到 regular 端口的统一图逆、
实际有限 connector 传播和有源强反馈不在本篇的已付范围。
