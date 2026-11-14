# R115：实际无限混合尾的全纯相对邻域、连续强源与完整向量零延拓

2026-11-13，independent_audit。

**状态：已证明。** 本文针对本题 R69/R74 实际调用的 quantitative-newton-twist-flex **R72 内侧无限尾**，包括全部内部标签、真实 mean 和连续普通源。它把既有完整非线性尾变成可微的 Newton 模块，证明其一、二阶变化的完整物理向量场在平盘上仅为轴向平移。源 R72 的充分条件已经支付；本篇另给明确的强源空间和算子常数。没有把普通 $C^2$ 球当作退化尾的相对邻域。

本篇没有将更新后的全部高模两迹直接改成 R74 零标签基态的 Robin 乘子。其准确反馈在 §9；有限正帽与无限混合尾始终区分。实际当前非线性零解、完整强反馈逆及其数值收敛门仍须由全局联立问题完成。

## 1. 使用的真实对象及尺度

以下“源 R72/R21/R25”均指 quantitative-newton-twist-flex 的：

- [R72 完整内尾](../../quantitative-newton-twist-flex/results/R72-large-width-inner-tail-to-cut128.md)，本次读取 Git blob a7c78793ba18724a4f0553b6ccd55259b8f4df92；
- [R21 六次幂四重周期尾](../../quantitative-newton-twist-flex/results/R21-a6-quarter-period-all-mode-tail.md)，blob a3b55246f416d73a4c4fe2b0b1545f0bfee0863d；
- [R25 完整相对 mean 球](../../quantitative-newton-twist-flex/results/R25-relative-material-ball-and-early-gates.md)，blob be20257721fed270c59a4024427042fc76ee0073。

这些读取没有改动源文件。源 R72 是实际全频九段流，非理想剪切或有限 count20+e1 原型。2026-11-13 提交 f735ddf58ed5149f65299cffd01b4f4c9a3076ed 的另一组八行使用 $\alpha_*=81/20$、末因子6；本篇不使用那八个数。本篇的 $\alpha=65/64$、末因子64，且所有 $rC'/C$ 始终是无量纲比值，不是 $C'/C$。

参考半径 $1\le r\le2$，胞元 $j>128$，实际数据为
$$
 \delta_j=\frac2{25}2^{-j},\qquad
 \eta_j=\frac{\delta_j^{3/2}}{4\sqrt2},\qquad
 w=\epsilon\delta_j^6p_*/r^7,\qquad 0<\epsilon\le1,
$$
$$
 p_*:\quad1,\quad64/\delta_j,\quad\delta_j/(65/64),
       \quad1/\delta_j,\quad64,\qquad E=1+w^2.
 \tag{115.1}
$$
三个平台长 $\delta_j$，四个 log-quintic 过渡及两个端平台长 $\eta_j$；$y=\sqrt{12}\log r$。真实背景在深端接开平盘，半径极限 $r_f>1$。它有多次型别变化；不是从某有限切口一直保持正曲率的帽。

源 R72 的角宽和状态为
$$
 h_j=\begin{cases}9/100,&129\le j\le4096,\\
                  8\delta_j^{1/256},&j>4096,\end{cases}
 \quad \tau_{128}=5177/400,\quad \tau_j-\tau_{j-1}=h_j,
$$
$$
 \zeta_j=\epsilon\delta_j^{39/4},\qquad
 X_{m,j}=(-1)^j\zeta_j^{-1}e^{|m|\tau_j}V_{m,j},\qquad
 V_m=(\nu_m C_m/r^4,\xi_m),
$$
$$
 \nu_m=m^2(m^2-1)/12,\quad
 \xi_m=(C'_m/r^3-m^2C_m/r^4)/\sqrt{12},\quad
 m\in4\mathbb Z\setminus\{0\}.
 \tag{115.2}
$$
采用强次序
$$
 \|X\|_{\mathcal X}=\sum_m\sup_j\|X_{m,j}\|_\infty,\qquad
 \|f\|_{\mathcal F}=\sum_m\sup_j\|f_{m,j-1}\|_\infty.
 \tag{115.3}
$$
每模标签是其实际内部层 $\ell_m(X)=(E_m^{-1}X_{m,b_m})_1$。不将这些标签替换为任意共同切口 Dirichlet 值。

本题的物理安装使用 R69/R74 的相同参数
$$
 \rho_*=(H_e b)^{-1},\qquad
 \epsilon=(4H_e\omega_e\bar W_b)^{-1},\qquad
 \frac{\epsilon}{\rho_*}=\frac b{4\omega_e\bar W_b}<2^{440}.
 \tag{115.4}
$$
最后一界只用 $b<2$、$\omega_e>(4/5)2^{360}$、$\bar W_b>2^{-799}$。先在此 $\epsilon$ 重新调用真实尾，再整体等比缩放 $\rho_*$；没有对一个既有非线性等距族作各向异性伸缩。

## 2. 完整固定点的一阶、二阶导数

源 R72 §§8–9 已付
$$
 X(a)=\mathcal H a+\mathcal G\mathcal R(X(a)),\qquad
 \|\mathcal H\|\le H_*:=256/85,\quad \|\mathcal G\|\le8192,
$$
$$
 \|\mathcal R(X)-\mathcal R(Y)\|
 \le K_*(\|X\|+\|Y\|)\|X-Y\|,\qquad
 \kappa:=8192K_*<2^{-60}.
 \tag{115.5}
$$
$\mathcal R$ 是单位复 $\mathcal X$ 球上的真实全纯 map。其局部入球门 $16e\,\zeta_j/R_j<1$ 对每层成立，所以使用整个单位球合法。

实际还可在 $\|a\|<1/4$ 解此同一固定点：$H_*/4+\kappa<1$ 且 $2\kappa<1$。这是扩大标签域的直接自映证明，没有改背景、标签或局部 PDE。原任务使用的 $\|a\|\le1/12$ 上，
$$
 \|X(a)\|\le\frac{H_*}{1-\kappa}\|a\|
 <\frac{13}{4}\|a\|\le\frac{13}{48}=:r_*.
 \tag{115.6}
$$
全纯参数定理也可由逐次收缩的局部一致收敛直接证明。微分准确给
$$
 DX(a)=(I-\mathcal G D\mathcal R(X(a)))^{-1}\mathcal H .
 \tag{115.7}
$$
由 $\|D\mathcal R(X)\|\le2K_*\|X\|$ 得
$$
 \boxed{\quad
 \|DX(a)\|<13/4,\qquad
 \|DX(a)-\mathcal H\|<2\kappa<2^{-59}.
 \quad}                                                     \tag{115.8}
$$
所有内部标签精确保持：$\ell(DX(a)b)=b$。

在 $\|X\|\le r_*<1/2$ 上，对算子值全纯函数 $D\mathcal R$ 作半径 $1/2$ 的 Cauchy 估计，得 $\|D^2\mathcal R(X)\|\le4K_*$。再次微分 (115.7) 因而有
$$
 \boxed{\quad \|D^2X(a)\|<64\kappa<2^{-54}.\quad}             \tag{115.9}
$$
例如未放宽的常数是 $4\kappa(13/4)^2/(1-2r_*\kappa)<43\kappa$。因此沿标签球内线段，
$$
 \|X(a+b)-X(a)-DX(a)b\|<2^{-55}\|b\|^2.
 \tag{115.10}
$$
该余项在完整强状态中成立，含所有高输出频率；不是固定有限模的 Taylor 公式。

## 3. 一致逐胞加权 $C^2$ 零延拓

固定角宽 $\sigma=\tau_{128}-1$，令
$$
 \beta=\frac{23}{4}-\frac5{256}=\frac{1467}{256}>0,\qquad
 \|v\|_{\mathcal J}
 =\sup_{j>128}\epsilon^{-1}\delta_j^{-\beta}
       \|v\|_{C^2_{r,\theta},\mathcal A_\sigma(I_j)} .
 \tag{115.11}
$$
这里先在一个胞元内取 Wiener 和，再取胞元上确界；没有将它误写成 (115.3) 的另一次 $\sum\sup$。对向量先用旋转柱坐标基，实际 $\theta$ 微分含该基的准确连接矩阵。转固定 Cartesian 实 $C^2$ norm 至多付下面已保留的 $2^6$；若另要求固定 Cartesian 复角 Wiener norm，还应付 $e^\sigma$，本篇的物理 $C^2$ 数字不需要它。

源 R72 (5.9) 给全部非mean高度、mean一二阶导
$$
 \|\mathcal J_j(U)\|_{C^2,\mathcal A_{\tau_{j-1}}}
 \le2^{52}\delta_j^{-4}h_j^{-5}\|U\|.
 \tag{115.12}
$$
$\|U_j\|\le\zeta_j\|X\|$，且 $h_j^{-5}\le2^{18}\delta_j^{-5/256}$。因此上述 jets 至多 $2^{70}\epsilon\delta_j^\beta\|X\|$。每胞物理参考径向长度小于 $3\delta_j$；将 mean 一阶导从 $r_f$ 积分后，
$$
 \left|\overline v(r)-\lambda\right|
 \le6\cdot2^{70}\epsilon\delta_j^{\beta+1}\|X\|.
$$
$\lambda$ 是唯一整体高度常数。以 $\lambda=0$ 定义规范高度 $v_a$，宽松统一界为
$$
 \boxed{\quad\|v_a\|_{\mathcal J}\le2^{74}\|X(a)\|.\quad}      \tag{115.13}
$$
这个论证包括角零模；没有仅从非mean高度趋零推断全部二阶平坦。

(115.12) 的复球及实际 PDE 给同样的全纯 $\mathcal J$ 值 map。在 $\|a\|<1/4$ 上的一致界和半径 $1/6$ 的 Cauchy 公式给一、二阶 Fréchet 导数的同一逐胞衰减。二阶混合导用两变量各半径 $1/12$，费用144；不把仅对角二阶界当成双线性 norm。

由于 $\delta_j^\beta\to0$，所有一二阶 jets 在真实累积圆 $r=r_f$ 一致趋零。真实源 R72 的端口、mean 及物理 PDE 已使每个有限接缝的二阶 jets 相同。因此延拓 $v_a=0$ 到整片平盘是真 $C^2$ 延拓，$Dv_a$ 和 $D^2v_a$ 同样成立。全部非零 $4\mathbb Z$ 高频都在同一个界内，未作截断。

## 4. 完整水平原函数及轴移是唯一平帽余项

本节先用源尾的正斜率方向 $z=h+v_a$，$h_r=w>0$。令
$$
 k=z_r=w+\kappa,\quad p=z_\theta/r,\quad t=1-p^2,\quad
 D=E-k^2-Ep^2,\quad
 l=r\sqrt t,\quad a_1=-kp/\sqrt t,\quad b_1=\sqrt{D/t}.
 \tag{115.14}
$$
源 R72 (5.8) 已在实际全角复球支付各胞物理相对量 $Y_{\rm true}<3\cdot10^{-6}w_{\min}/8$；实解特别满足
$$
 t>1-10^{-6},\quad D>1-10^{-6},\quad
 k+Ep_\theta>(1-10^{-6})w>0.
 \tag{115.15}
$$
同一复估计给 $t,D$ 在1附近的固定幂级数分支。没有要求曲率离零。

水平投影的准确度量为
$$
 H=g_0-dz^2,\qquad g_0=E\,dr^2+r^2d\theta^2.
$$
写其向量导数为
$$
 F_{h,\theta}=l e^{i\alpha},\qquad
 F_{h,r}=(a_1-i b_1)e^{i\alpha}.
 \tag{115.16}
$$
闭合所需的连接恰为
$$
 \alpha_\theta=\frac{l_r-(a_1)_\theta}{b_1}
 =\frac{1+kp_\theta/t}{\sqrt D},\qquad
 \alpha_r=\frac{a_1\alpha_\theta-(b_1)_\theta}{l}.
 \tag{115.17}
$$
等式只用 $rp_r=k_\theta-p$。$H$ 平坦的准确 Darboux 方程使此连接闭；源 R72 的完整 mean 方程给 $\langle\alpha_\theta\rangle=1$。

对实反射偶高度，$p$ 奇、$k$ 偶，故 $\alpha_\theta-1$ 偶、$\alpha_r$ 奇。固定
$$
 \alpha=\theta+\pi/2+\gamma,\qquad
 \gamma=\partial_\theta^{-1}(\alpha_\theta-1),\qquad
 \gamma(r,0)=0.
 \tag{115.18}
$$
$\gamma$ 是奇的 $\pi/2$ 周期函数，其径向导由 (115.17) 给出，没有漏掉径向旋转常数。现在令 $\widetilde F_h=e^{-i\theta}F_h$，准确解
$$
 (\partial_\theta+i)\widetilde F_h=i l e^{i\gamma}.           \tag{115.19}
$$
在 $4\mathbb Z$ 上 $|4k+1|\ge1$，故这是有界唯一角原函数。(115.17) 保证其径向导也等于 (115.16)。在真实角变量中，$\pi/2$ 旋转使向量乘 $i$，四段积分之和为0；水平平移规范由这个对称性准确固定。不存在另一个漏掉的平移周期。

式 (115.16) 的一次径向微分只用 $k_r,p_r,\gamma_r$；一次角微分只用 $k_\theta,p_\theta,\alpha_\theta$。所以完整 $F_h$ 的 $C^2$ 重建只需高度 $C^2$，不需高度三阶。在 $1\le r\le2$、$|w|,|w_r|\le1$ 及 (115.15) 下，逆/平方根、两条角原函数和 Leibniz 和给
$$
 \|F_h-r e^{i\theta}\|_{C^2,\mathcal A_\sigma;\mathrm{rot}}
 \le2^{16}\|v_a\|_{C^2,\mathcal A_\sigma}.                   \tag{115.20}
$$
一个可直接核的粗账为：若右侧未乘常数的 norm 为 $N\le2^{-10}$，则 $|D-1|\le5N$、$|D_r|\le16N$、$|D_\theta|\le8N$，$|\alpha_\theta-1|\le18N$、$|\gamma|\le5N$、$|\gamma_r|\le64N$；各零、一、二阶向量项分别小于 $64N,128N,1024N$，$2^{16}$ 包含全部分量及连接项。实际 (115.13) 与 $\delta_{129}<2^{-132}$ 远小于此 $N$ 门。这些是 Wiener 代数界，非仅实角采样。

于是完整参考尾
$$
 F_a=(F_{h,a},h+v_a+\lambda)
$$
有准确 $g(F_a)=g_0$，并在整片平盘上等于 $(r\cos\theta,r\sin\theta,h(r_f)+\lambda)$。其标签一、二阶变化在那里准确为0；只有 $\lambda$ 方向为 $e_z$。上帽的真实负斜率通过整体竖直反射得到，全部零延拓结论不变。

在本题物理缩放 (115.4) 后，包含极坐标到 Cartesian 的 $2^6$，
$$
 \|F_a-F_0-\lambda_{\rm phys}e_z\|_{C^2(I_j^{\rm phys})}
 \le2^{96}\frac{\epsilon}{\rho_*}\delta_j^\beta\|X(a)\|.
 \tag{115.21}
$$
因为 $132\beta-536>220$，全真实无限尾上可统一取
$$
 \|F_a-F_0-\lambda_{\rm phys}e_z\|_{C^2}<2^{-218}\|a\|,
$$
$$
 \boxed{\quad
 \|D_aF_a\|_{C^2}<2^{-217},\qquad
 \|D_a^2F_a\|_{C^2}<2^{-212}.
 \quad}                                                     \tag{115.22}
$$
物理半径很小，但 $\epsilon/\rho_*$ 的准确消去已付，没有把 $1/\rho_*$ 单独丢掉或当成免费常数。上界非常宽松，非新的几何数值运行。

## 5. 更新后 material 径向主系数的真实相对正性

在北帽实际高度 $Z=-z+\text{constant}$ 下，取外法向。从 $g_0$ 的 Christoffel 系数直接得
$$
 N:=II_{\theta\theta}
 =-\frac{r(k+Ep_\theta)}{\sqrt E\sqrt D},\qquad
 \frac{N}{N_0}=\frac{k+Ep_\theta}{w\sqrt D}>0,\qquad
 N_0=-rw/\sqrt E.
 \tag{115.23}
$$
R37 的 material 密度为 $A=-\operatorname{cof}(II)/(\zeta^2\sqrt{\det g_0})$，$\zeta=\nu\cdot F/|F|$。因此
$$
 A^{rr}=\frac{k+Ep_\theta}{\zeta^2 E\sqrt D}>0
 \qquad(r>r_f).                                             \tag{115.24}
$$
这是更新后的真实系数，不是从未更新背景推测。在实际尾 $Z>0.9$，且 (115.22) 保持支持正性；允许 $|\lambda_{\rm phys}|<1/20$ 亦有固定正支持余量。各平盘上 $w=0$，退化本身保留，未声称全域统一椭圆。

由于尾族准确保持同一 $g_0$，其 Gauss 曲率等于该目标 metric 的曲率，全部混合型别和转折集合也随之准确保留。因此 R37 $K_{g(F)}-K_{g_0}$ 的 residual 系数在这条尾上恒为0。有限正帽止于本题 regular 切口；本节没有将源尾的负曲率段改称正帽。

## 6. 真连续普通源：准确空间、mean 及 Jacobi Green

以下是实际更新后尾上的线性有源定理，不是把离散跳量称为普通源。固定 $\|a\|\le1/12$ 的真实 $z_a$。定义源 R72 的完整密度
$$
 {\cal E}(z)=D^{-3/2}[(1+n_{\rm ph})\kappa_y-\mathscr G_+],
 \qquad n_{\rm ph}=(\kappa+Ep_\theta)/w ,
 \tag{115.25}
$$
其中 $\mathscr G_+$ 按源 R72 (2.4)，包含完整 mean。给连续普通源 $e_j(y,\theta)$，求 $D{\cal E}(z_a)\dot z=e$。允许源有零模。

一个明确充分的源空间是
$$
 \boxed{\quad
 \|e\|_{\mathcal T}
 =2^{4200}\epsilon^{-1}
 \sum_{m\in4\mathbb Z}\sup_{j>128}
 \left[
  \delta_j^{-11607/4}h_j^{-2}
  e^{(\tau_{j-1}+h_j/2)|m|}
  \sup_{y\in I_j}|\widehat e_{m,j}(y)|
 \right]<\infty .
 \quad}                                                     \tag{115.26}
$$
源在实际接缝连续，或等价地其同一物理方程的 RHS 连续。这是刻意很强的显式空间，未声称等于 R15 较大的 $\mathcal S_1\cap\mathcal S_2$，也未声称当前任意全局 RHS 自动属于它。它不含未知解、未知基本解或未知 DN norm。

### 6.1 零模不是可以删掉的源

由源 R72 (2.6) 微分，
$$
 (\dot M)_y=w\langle e\rangle .
$$
$C^2$ 平坦实现要求深端 $\dot M(r_f)=0$，故准确取
$$
 \dot M(y)=\int_{y_f}^y w(s)\langle e(s)\rangle\,ds.          \tag{115.27}
$$
cut128 的这个数是一个真实输出负荷，不能另设为0。在每个切口，mean 小根的变化包含 $\dot M/(w F_{K_0})$；源 R25 给 $|F_{K_0}^{-1}|\le64/55<2$。非mean变化引起的 mean 导数仍由同一隐函数保留。

因 $w\le64\epsilon\delta_j^5$、$\ell_j<4\delta_j$、$h_j$ 非增，(115.26) 直接给
$$
 |\dot M|_{I_j}\le
 2^{-4191}\epsilon^2\delta_j^{11631/4}h_j^2\|e\|_{\mathcal T},
$$
$$
 |\dot\kappa_0^{\,M}|_{\text{deep},j}\le
 2^{-4182}\epsilon\delta_j^{11603/4}h_j^2\|e\|_{\mathcal T}.
 \tag{115.28}
$$
这里用了真实 $w_{\min}\ge\epsilon\delta_j^7/256$。这些界由实际积分获得，不是冻结 mean 后补一个自由常数。

### 6.2 连续局部 response 及强求和

实际背景处于源 R72 的物理复球 $Y_{\rm true}<3\cdot10^{-6}w_{\min}/8$。其 §5 的完整64-Lipschitz/移动角宽 Volterra 证明可在此背景处直接线性化。以零非mean初值、(115.28) 的 mean 初值解 Jacobi Cauchy 问题，外加 $(D^{-3/2}(1+n_{\rm ph}))^{-1}e$。该逆 norm 小于2；不交换 Fourier 投影与乘法逆。

相同九段估计给
$$
 \|\dot v\|_{\mathrm{physical},\#}
 \le2^{38}e^{2012}\delta_j^{-2890}
          (I_{0,j}+18\,E_j),
 \quad
 E_j=\sum_m e^{(\tau_{j-1}+h_j/2)|m|}
                     \sup_y|\widehat e_{m,j}|.
 \tag{115.29}
$$
这里的 physical norm 是源 R72 §5 对 $(p,\kappa)$ 的强 $\mathcal W^1$ norm，$\dot v$ 在此式表示这对梯度变化；高度本身随后按兼容关系恢复。角路径从 $\tau_{j-1}+h_j/2$ 出发，实际费用 $256\beta_j\le h_j/4$，故端点仍有 $h_j/4$ 的余宽。实际背景已有同一路径的复强控制，所以此线性化不是在未给出的更大条带上使用系数。

转 canonical 端点费 $2^6h_j^{-2}$；由方程控制二阶径向导再付 $2^{15}\delta_j^{-3}$。因 $e^{2012}<3^{2012}<2^{4024}$，以下同时包围真端点及内部高度 jets：
$$
 C_{\mathrm{port},j}=2^{4096}\delta_j^{-2890}h_j^{-2},\qquad
 C_{\mathrm{jet},j}=2^{4096}\delta_j^{-2893}h_j^{-2}.
 \tag{115.30}
$$
(115.29) 是 source 真实径向连续 Cauchy response；输入切口状态改变时另加 $D\Phi_j(U_j)\dot U_j$，不会把它误当独立跳量。线性方程的任意源大小由缩放恢复，不要求把大的线性响应当作一个新的非线性背景。

局部 response 对原初值 $U_j$ 全纯，在 $R_j/4$ 球有上述统一界。它和 mean 逆均与角平移交换。以源 R72 §9.1 相同的多线性极化方法，每个背景系数先取胞元上界，再与源系数卷积。$16e\zeta_j/R_j<1$ 使整个级数费用小于 $2^{10}$。准确说，含 $q$ 个背景输入的系数由 $(8e\zeta_j/R_j)^q$ 的几何和控制；源只出现一次，mean 积分是显式的零模线性算子。频率始终满足输出频率等于全部输入频率之和。

由 (115.28)–(115.30) 及 (115.26)，得到真实规范端点源 $f_a(e)$，满足
$$
 \|f_a(e)\|_{\mathcal F}\le\|e\|_{\mathcal T}.               \tag{115.31}
$$
具体剩余径向幂：直接源为 $11607/4-2890-39/4=2$；mean 初值为 $11603/4-2890-39/4=1$。用 (115.29) 原常数先计 mean 初值费用再作强提升，常数仍有超过 $2^{80}$ 的余量。因此本式没有不合法的 $\sup\sum\to\sum\sup$ 换序，也没有忽略零模诱发的非mean输出。

### 6.3 真更新后强解

给全部标签变化 $b\in\ell^1$，准确求解
$$
 \dot X=\mathcal H b+\mathcal G
       [D\mathcal R(X(a))\dot X+f_a(e)] .
$$
于是
$$
 \boxed{\quad
 \|\dot X\|_{\mathcal X}
 \le4\|b\|_{\ell^1}+2^{14}\|e\|_{\mathcal T}.
 \quad}                                                     \tag{115.32}
$$
每胞用刚才的真实 Jacobi Cauchy response 重建，端口和 mean 相同；连续物理源使二阶 jets 在接缝相同。用 (115.30) 后直接源留下 $\delta_j^{35/4}$，mean 初值留下 $\delta_j^{31/4}$，两者严格强于 $\delta_j^\beta$。因此
$$
 \|\dot z-\lambda\|_{\mathcal J}
 \le2^{80}\bigl(\|b\|+2^{14}\|e\|_{\mathcal T}\bigr).
 \tag{115.33}
$$
这是所有高模、mean、普通源的真实 $C^2$ 平坦延拓。

基态 $a=0$ 时，(115.25) 准确化为
$$
 C''+\frac{w'}w C'+\frac{w'}{rw}C_{\theta\theta}
   =\frac{\sqrt{12}}r e.
 \tag{115.34}
$$
故 R15 的 $F=\sqrt{12}e/r$、$N=p_*e/(\sqrt{12}r^3)$。由 $\beta_j<h_j/4$ 和 $(1+m)^{312}e^{-mh_j/4}\le(2048/h_j)^{312}$，(115.26) 蕴含 R15 的非mean $\mathcal S_1,\mathcal S_2$；其已证强解与本构造由标签和唯一性相同。零模由 (115.27) 单列，不将 R15 的非零模命题误称零模定理。一般 $a$ 使用真实 (115.25)，没有将基态 ODE 转授给非径向尾。

## 7. 有源全向量重建的准确合同

给定真实对称 metric source $T$，要求它在平盘为0，接缝至少有所需连续 jets，并令
$$
 {\cal P}(g,z)=\det(\nabla_g^2z)
              -K_g\det(g)(1-|\nabla z|_g^2).
$$
在 $g_0=E\,dr^2+r^2d\theta^2$ 上直接展开得到恒等式
$$
 {\cal P}(g_0,z)=\frac{\sqrt{12}w}{E D^{-3/2}}{\cal E}(z).
$$
为独立核此归一，乘 $E/r$ 后的左侧是
$$
 (k+Ep_\theta)k_r-\frac Er(k_\theta-p)^2
       -\frac{E'}2(1-p^2+kp_\theta).
$$
代 $k=w+\kappa$、$E'=2ww'$、$r_y=r/\sqrt{12}$，它准确等于 $(\sqrt{12}w/r)D^{3/2}{\cal E}(z)$。因背景 $\mathcal E(z_a)=0$，准确普通源是
$$
 \boxed{\quad
 e_T=-\frac{E D^{-3/2}}{\sqrt{12}w}\,D_g{\cal P}(g_0,z_a)[T].
 \quad}                                                     \tag{115.35}
$$
右侧只含已知背景和 $T$ 的二阶 jets，没有未知 $\dot z$。要求 $e_T\in\mathcal T$ 以及
$$
 \|T\|_{\mathcal Z}
 =\sup_j\epsilon^{-1}\delta_j^{-\beta}
          \|T\|_{C^1,\mathcal A_\sigma(I_j)}<\infty .         \tag{115.36}
$$
这是完整可检验的 tail source 合同；其中 $1/w$ 明确保留。并非所有普通 $C^2$ metric source 自动满足它。

以 §6 求 $\dot z$。则
$T-dz\otimes d\dot z-d\dot z\otimes dz$
是水平平坦度量 $H$ 的线性兼容应变。微分 (115.16)–(115.17)，连接变化 $\dot\omega$ 闭；其周期在半径间保持常数，又因 (115.33)、(115.36) 在平坦端趋零，故周期准确为0。四重旋转消去平移周期，反射固定旋转规范。因此存在完整水平变化 $\dot F_h$，且
$$
 Dg(F_a)[(\dot F_h,\dot z)]=T,\qquad
 \|\dot F_h\|_{\mathcal J}
 \le2^{20}\bigl(\|T\|_{\mathcal Z}+
                     \|\dot z-\lambda\|_{\mathcal J}\bigr).
 \tag{115.37}
$$
这里 $T$ 与源须保持实际二面体对称性；并非把任意非对称平移 period 隐藏为0。

为核导数阶数，可先变化 $l^2=H_{\theta\theta}$、$a_1=H_{r\theta}/l$、$b_1=\sqrt{\det H}/l$。它们的一阶 jets 只含 $T$ 的一阶与 $\dot z$ 的二阶；$\dot\alpha_\theta,\dot\alpha_r$ 仍由这三量的一阶 jets 给出。在 $l\in[1/2,3]$、$b_1\in[1/2,2]$ 的实际球，coframe、connection、两次角原函数及六个二阶项分别可用 $2^8,2^{12},2^{12},2^{18}$ 包围，$2^{20}$ 包含相加费用。本式不要求 $T$ 三阶，也没有用除以趋零 Gauss 曲率的重建。

零延拓后 $(\dot F_h,\dot z)=\lambda e_z$ 在整个平盘上，不是只在边界圆上为零。cut128 的 mean 高度、(115.27) 的 holonomy 负荷以及其实际 mean slope 都仍须与外部匹配。在本题的物理规范中 $w_{\rm radial}=V\cdot F/|F|$、$Y_z=F_z/|F|$，平帽上因而准确为 $w_{\rm radial}=\lambda Y_z$。这正是 R112/R114 所需的完整强尾实现。

## 8. Newton 中如何使用，何处仍须联立

可将当前曲面未知量分成有限主体及两份实际 $(a_\pm,\lambda_\pm)$ tail chart，在 cut128 施加它们的**全部实际 Cauchy 两迹和 metric germs**。每次更新标签后重新评价 $F_{a_\pm}$，而非在无限尾直接加一个任意普通 $C^2$ 位移。这样无限尾的 metric defect 恒为0；其 Newton source 精确为0，自动满足 (115.26)、(115.35)–(115.36)。主体求得的切口数据必须通过联立方程与这个 chart 匹配。

二阶展开由 (115.9)、(115.22) 给真实定量余项。在平盘上更新是轴向平移，$dV=0$，二次 metric defect 也准确为0。腰反射取 $\lambda_-=-\lambda_+$，与 R112 相同。最终角相位族可在这个选定闭面上生成；本篇不另要求每个最终相位重新选择内部标签或尾参数。

若 Newton 内部还调整使有限主体可逆的参数、connector 或 R74 好 bump 参数，则须对它们的实际变化另付定量控制；上述固定 chart 不自动解决那项选择问题。不能把最终只需一个参数值误作迭代中所有选择都免费连续。

## 9. 与实际 ground-state Cauchy frame 的精确接线

对任何真实标签方向构造的完整向量 $V$，R32/R74 的 scalar 和 ground-state 变量准确为
$$
 w_{\rm radial}=F\cdot V/|F|,\qquad
 v=\frac{w_{\rm radial}}{Y_z}=\frac{F\cdot V}{F_z},
$$
$$
 p=\bigl(Y_z^2A\nabla v\bigr)\cdot dr,\qquad
 A=-\frac{\operatorname{cof}II}{\zeta^2\sqrt{\det g_0}}.
 \tag{115.38}
$$
这是同一物理角、同一密度和真实 horizontal reconstruction。给外域 outward conormal 时再使用其对应方向符号。物理等比缩放保留，不能把 $(C,C')$ 直接称为 $(v,p)$。

在零标签北帽上，写 $F=(r e_r,Z(r))$、$W=-Z_r>0$，模式 $m\ne0$。若高度变化为 $C$、水平径向分量为 $U$，线性 metric 方程直接给
$$
 U=\frac{W(m^2C-rC')}{m^2-1},\qquad
 v=C+\frac rZ U,\qquad
 p=\frac{WZ}{Z+rW}C'+\frac W{Z+rW}U.
 \tag{115.39}
$$
$C'$ 是此处的**物理半径导数**。此式准确支付 normal/ground-state 与 momentum shear，不用维数不符的 $rC'/C$ 替代 $C'/C$。在非零标签使用 (115.38) 的实际变化；(115.39) 不是更新后公式。轴向平移方向则对每个真实 $a$ 都准确给 $v=\lambda_{\rm phys}$、$p=0$，不发生重新归一的误差。

(115.8) 是完整内部标签到规范强状态的微扰门。它没有提供所有高标签到共同切口高度的统一逆：源 R15 的实际切口方向可能为竖直，且标签权 $\mathfrak w_m$ 随频率增长。故不能仅乘一个常数就宣布 R74 的全部 regular Robin 形式在非零标签上同宽相对小变。正确下一步是保留 (115.38) 的完整两迹或在已支付的 trace 空间上证明其 graph 逆，并与 finite/body/connector 的真实 source 和 mean 行作 Schur 消去。已证明的 (115.8)–(115.10) 可直接用于这一增广算子；没有删去高输出列。

## 10. 本次有限核验的范围

相邻脚本 [fourfold_true_tail_chart_budget.mjs](../scripts/fourfold_true_tail_chart_budget.mjs) 用准确 BigInt 分数核 (115.5)–(115.10)、指数、物理缩放及源剩余幂。相邻小报告保存原始有理输入、全部门和本篇来源 blob。这是实际执行的有限常数核，不是重新运行源 R72 的 PDE 证书，也不是新宽 collar 原生运行。全无限层结论来自上面的证明和已读源 R72/R21/R25；本次未创建或补造任何丢失的大 JSON。
