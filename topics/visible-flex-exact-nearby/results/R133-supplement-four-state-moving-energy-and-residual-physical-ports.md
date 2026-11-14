# R133：四态 moving 强能量、无逆根权的物理端口与真实残差费用

**已证明（完整算子与条件预算；新中心的数值传播尚未执行）。**
本篇补上同一近似中心的一个实际接口：在 moving 能量中保留第二分量的
普通 $L^2$ 范数，便可把完整 mean、强源和两个物理端口相接，而不在中间
以 $(-K)^{-1/2}$ 恢复第二分量。近似中心的物理残差仍完整计入，不能因
候选残差小就把两种 Jacobi 算子等同。

新的四态 producer 适用于已指定的 fullR moving 中心
`ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`。
但平台 environment unavailable 前没有执行这个 producer，所以本篇
不列任何新 moving 增益，不沿用旧 $.75$ 中心的增益，也不宣称全 BVP 逆
或非线性解已闭合。

## 1. 完整 moving 线性化和四个状态

所有角平均与 $L^2$ 用归一化测度 $2\,d\phi/\pi$，完整频率为
$k\in4\mathbb Z$。$I=\partial_\phi^{-1}P_0$，$P_0=1-\langle\cdot\rangle$；
准确有 $\|I\|_{L^2\to L^2}=1/4$。在一个严格负区间令

$$
 q=\sqrt{-K}>0,\quad H=\operatorname{diag}(1,q^2),\quad
 Q=(u,v),\quad m=\langle v\rangle<0,
$$
$$
 S=u^2+Kv^2,\qquad
 d=-\beta I S,\qquad d_\phi=-\beta(S-\langle S\rangle).
 \tag{Y.1}
$$

这是实际径向 $K,\gamma,\beta$ 和实际中心 $Q$，没有假设 $Q$ 满足方程。
[完整 moving 系统](R133-supplement-exact-moving-curvature-chart-and-mean-energy.md)
的线性化对 $h=(\xi,\zeta)$、$z=\langle\zeta\rangle$ 为

$$
 h_r=d h_\phi+\gamma m J(K)h_\phi+L_0h
       +\delta d\,Q_\phi+\gamma zJ(K)Q_\phi+f,
 \qquad J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},
$$
$$
 L_0=\beta
 \begin{pmatrix}
 -1-3u^2-Kv^2&-2Kuv\\
 -2uv&1-u^2-3Kv^2
 \end{pmatrix},
 \quad
 \delta d=-\beta I(2u\xi+2Kv\zeta).
 \tag{Y.2}
$$

取四个真实状态

$$
 E_0=\|H^{1/2}h\|_2,\quad M=|z|,\quad
 E_1=\|H^{1/2}h_\phi\|_2,\quad Y=\|\zeta\|_2.
 \tag{Y.3}
$$

$Y$ 是一个额外受控输出；不以 $Y\le E_0/q$ 将它消掉。所有频率及
$z$ 都保留。几何应用采用原反射类 $\xi$ 奇、$\zeta$ 偶；能量估计本身
亦对 (Y.2) 的完整周期线性系统成立。

记已经在整条连续角圆和真实径向盒上付清的量

$$
 R=\|H^{1/2}Q\|_\infty,\quad
 L=\|H^{1/2}Q_\phi\|_\infty,\quad
 L_2=\|H^{1/2}Q_{\phi\phi}\|_\infty,
$$
$$
 U_1=\|u_\phi\|_\infty,\quad V_1=\|v_\phi\|_\infty.
 \tag{Y.4}
$$

令

$$
 A_1=-\beta(1+3u^2+Kv^2),\qquad
 A_2=\beta(1-u^2-3Kv^2)+K'/(2K),
$$
$$
 g_0=\max_{\phi,i}(A_i-d_\phi/2)+|\beta|RL/2,\qquad
 g_1=\max_{\phi,i}(A_i+d_\phi/2),
$$
$$
 c=\beta(1-\langle S\rangle),\qquad
 g_Y=\sup_\phi\{\beta(1-u^2-3Kv^2)-d_\phi/2\}.
 \tag{Y.5}
$$

这些对角数可以为负，不应未经说明全部改成绝对值。

## 2. 四态全 Fourier 比较

以 $\preceq$ 表示逐分量不等式，有

$$
 D^+
 \begin{pmatrix}E_0\\M\\E_1\\Y\end{pmatrix}
 \preceq
 \mathcal A
 \begin{pmatrix}E_0\\M\\E_1\\Y\end{pmatrix}
 +
 \begin{pmatrix}
 \|H^{1/2}f\|_2\\|\langle f_2\rangle|\\
 \|H^{1/2}f_\phi\|_2\\\|f_2\|_2
 \end{pmatrix},                                         \tag{Y.6}
$$

其中完整 Metzler 矩阵为

$$
 \boxed{
 \mathcal A=
 \begin{pmatrix}
 g_0&\gamma qL&0&0\\
 2|\beta m|R&c&0&0\\
 |\beta|R(10L+L_2/2)&\gamma qL_2&g_1&0\\
 a_{Y0}&\gamma U_1&\gamma|m|&g_Y
 \end{pmatrix},\quad
 a_{Y0}=2|\beta|\|uv\|_\infty+|\beta|RV_1/2.}
 \tag{Y.7}
$$

前三行是已证明的完整 moving mean/强能量；这里再次说明其关键消去。
$HJ(K)$ 对称且 $\gamma m$ 只依 $r$，故角主部积分为零。
$H^{1/2}L_0H^{-1/2}$ 的非对角 Hermitian 部分准确相消。
径向权导数给第二对角的 $K'/(2K)$，共同输运分部积分给
$-d_\phi/2$。$\|\delta d\|_2\le|\beta|RE_0/2$ 给第一行的原函数费用，
$\|H^{1/2}J(K)Q_\phi\|_2\le qL$ 给完整 mean 列。

真实平均准确满足

$$z_r=cz-2\beta m\langle u\xi+Kv\zeta\rangle+\langle f_2\rangle.$$

这是第二行，不把 $z$ 预置为零。对第一角导线性化，局部矩阵导数的
完整 $H$ 算子范数不超过 $8|\beta|RL$；
$\|(\delta d)_\phi\|_2\le2|\beta|RE_0$ 再付 $2|\beta|RL$。
剩下 $\delta d\,Q_{\phi\phi}$ 和 mean 列分别给
$|\beta|RL_2/2$、$\gamma qL_2M$。因此第三行的系数10包含全部
局部/非局部交换项，且 $g_1$ 中的输运符号确为 $+d_\phi/2$。

第四行由 (Y.2) 的完整第二分量直接得出：

$$
 \zeta_r=d\zeta_\phi-\gamma m\xi_\phi
 -2\beta uv\,\xi+\beta(1-u^2-3Kv^2)\zeta
 +\delta d\,v_\phi-\gamma z u_\phi+f_2.
$$

分别在 $L^2$ 中取上界，使用 $\|\xi_\phi\|_2\le E_1$、
$\|\xi\|_2\le E_0$ 和原函数界，即得 (Y.7) 的最后一行。
此推导没有任何 $1/q$。第四列前三行准确为零，因此新增状态不扩大
原来三态的齐次增益。

对逆向传播，将所有对角中的真实生成元取反后重新取上确界；
非对角绝对上界保持。具体为
$g_0^-=\max_{\phi,i}(-A_i+d_\phi/2)+|\beta|RL/2$、
$g_1^-=\max_{\phi,i}(-A_i-d_\phi/2)$、$c^-=-c$、
$g_Y^-=-\inf_\phi[\beta(1-u^2-3Kv^2)-d_\phi/2]$。
不把前向的耗散未经变号沿用到反向。

## 3. 真实连续计算、强源和准确分片跳

对实际有限 moving 中心 $u=\alpha\sum U_j\sin4j\phi$、
$v=s+\alpha(V_0+\sum V_j\cos4j\phi)$，mean 可用准确正交公式

$$
 m=s+\alpha V_0,\qquad
 \langle S\rangle=
 \frac{\alpha^2}2\sum U_j^2
 +K\left(m^2+\frac{\alpha^2}2\sum V_j^2\right).          \tag{Y.8}
$$

这里不需要原物理角的逆角积分，亦不把 $V_0$ 删除。
$R,L,L_2$ 用完整有限三角和及闭角 Taylor 余项计算；所有 dyadic
径向三次系数和真实目标盒同时保留。原无限 primitive 属于目标，
仍通过原目标 native 保留，不能因中心有限就把目标尾删去。

在每个完整闭径向盒上用非负上界矩阵 $\overline{\mathcal A}_j$；
其对角仍可有符号。矩阵指数和顺序乘积给准确的比较演化。
为了同时包围任意子区间及 $L^1_r$ 源，可以只将对角换成
$\max(0,\overline A_{ii})$，保其余真实上界，再求完整正矩阵乘积。
这一步增加的是显式费用，不是重新初始化 mean。

若 $f$ 仅以普通完整 $H^1$ 给出，取 $w=\max(1,\sup q)$，则源状态
由两个普通通道 $\|f\|_2,\|f_\phi\|_2$ 通过

$$
 \begin{pmatrix}w&0\\1&0\\0&w\\1&0\end{pmatrix}           \tag{Y.9}
$$

控制。因此输出 $(E_0,E_1,Y)$ 的全 $L^1_rH^1_\phi$ 费用可直接从
四态传播和 (Y.9) 得到，也不需要全区间的 $1/\inf q$。
若需要更紧预算，直接保留 (Y.6) 的四个源通道。普通标量/参数源的
mean 不得丢掉。

分片中心的每一个 dyadic PPoly 跳必须准确计算。设完整 moving
分量及第一角导的跳上界为 $J_u,J_v,J_{u1},J_{v1}$，
准确 mean 跳为 $J_m=|\alpha[V_0]|$，则该接口的四态点源为

$$
 \left(\sqrt{J_u^2+q^2J_v^2},\ J_m,\
       \sqrt{J_{u1}^2+q^2J_{v1}^2},\ J_v\right)^T.
 \tag{Y.10}
$$

这只适用于在共同 $\phi$ 圆上解 moving 方程时的真实仿射跳
$-[\widehat Q]$。若从已有物理方程转换其同一物理角接线，仍须使用
准确 $T_+\mathcal P T_-^{-1}$，不能把它默认为恒等。

全 Fourier Cauchy 存在性可由在每个光滑片上的对称双曲正则化、
(Y.6) 的一致能量界和唯一性得到，再按准确接口拼接。这个论证的
Galerkin 正则化只是构造完整极限，不把有限候选的 Jacobian 当作
全频逆。$H^0/H^1$ 在同一完整 Fourier 权尺度插值给中间阶；
所有允许 mean 同时保留。

## 4. 两个完整物理端口，不除以根权

固定一个实端口，$g\le|v|$、$m_g\le|m|$，
$V_2=\|v\|_2$，$j=\theta_\phi=v/m$，$0<j_-\le j\le j_+$。
[准确变分互逆](R133-supplement-residual-sensitive-moving-physical-Jacobi-bridge.md)
给，固定物理角变分拉回为 $k$，moving 变分为 $h$：

$$
 k=h-Q_\phi\chi,\qquad
 \chi=\frac1vI(h_2-zv/m),\qquad z=\langle h_2\rangle.
 \tag{Y.11}
$$

当前反射归一确保所用奇原函数唯一；这不是任意常数角漂移的遗漏。
定义

$$
 a_Y=\frac1{4g},\quad a_M=\frac{V_2}{4g m_g},\quad
 b_Y=\frac1g+\frac{V_1a_Y}g,\quad
 b_M=\frac1{m_g}+\frac{V_1a_M}g.
 \tag{Y.12}
$$

由完整原函数界和准确导数

$$
 \chi_\phi=\frac{h_2}v-\frac zm-\frac{v_\phi}v\chi
$$

得

$$\|\chi\|_2\le a_Y Y+a_M M=:C,\qquad
 \|\chi_\phi\|_2\le b_Y Y+b_M M=:C_1.                  \tag{Y.13}$$

于是拉回的三个完整量满足

$$
 K_0:=\|H^{1/2}k\|_2\le E_0+LC,\quad
 K_1:=\|H^{1/2}k_\phi\|_2\le E_1+L_2C+LC_1,
$$
$$Y_k:=\|k_2\|_2\le Y+V_1C.                            \tag{Y.14}$$

最后使用真实测度和导数换元：

$$
 \|H^{1/2}k^{\rm phys}\|_{L^2_\theta}\le\sqrt{j_+}\,K_0,\quad
 \|H^{1/2}k^{\rm phys}_\theta\|_{L^2_\theta}
                    \le j_-^{-1/2}K_1,\quad
 \|k_2^{\rm phys}\|_{L^2_\theta}\le\sqrt{j_+}\,Y_k.
 \tag{Y.15}
$$

这给显式 $3\times4$ 正矩阵，将 $(E_0,M,E_1,Y)$ 送到真正物理
$(E_0^{\rm phys},E_1^{\rm phys},Y_2^{\rm phys})$。没有 $1/q$。

反向准确公式为 $h=k+Q_\phi I(k_2/v)$、
$z=m\langle k_2/v\rangle$。在 $\phi$ 测度下

$$
 E_0\le K_0+\frac L{4g}Y_k,\quad
 M\le\frac{|m|}gY_k,\quad
 E_1\le K_1+\left(\frac{L_2}{4g}+\frac Lg\right)Y_k,\quad
 Y\le\left(1+\frac{V_1}{4g}\right)Y_k.                  \tag{Y.16}
$$

对原物理通道先付
$K_0\le j_-^{-1/2}E_0^{\rm phys}$、
$K_1\le\sqrt{j_+}E_1^{\rm phys}$、
$Y_k\le j_-^{-1/2}Y_2^{\rm phys}$，
即得到完整反向 $4\times3$ 正矩阵。同一矩阵也控制实际物理源
先拉回再经 $T_Q$ 的四态源通道，包含其真实平均。

## 5. 近似中心的完整残差扰动

令 $R=(R_1,R_2)$ 是**物理中心残差拉回 $\phi$**，不是未经转换的
normalized moving 残差。记 $b=R_2/v$、$e=Ib$。准确 Jacobi 接线为

$$
 \mathcal J_{\rm mov}h=T_Q\mathcal J_{\rm phys}k+
                  D^2\mathcal H[R,k],
$$
$$
 D^2\mathcal H[R,k]=e h_\phi+R_\phi\chi+Q_\phi t,\quad
 t=-b\chi+2I(b_\phi\chi)-\frac zm e,
$$
$$
 \left\langle(D^2\mathcal H[R,k])_2\right\rangle
                      =2m\langle b_\phi\chi\rangle.     \tag{Y.17}
$$

这些是前篇的准确恒等式；$R$ 不得设为零。将唯一的一阶项
$e h_\phi$ 吸收到共同实速度 $d+e$，其余项是完整有界算子。

设以下都是实际连续上界：

$$
 B=\|b\|_\infty,\ B_1=\|b_\phi\|_\infty,\ 
 \mathcal E=\frac\pi8B\ge\|e\|_\infty,\quad
 A=B+B_1/2,
$$
$$
 T_1=\|H^{1/2}R_\phi\|_\infty,\quad
 T_2=\|H^{1/2}R_{\phi\phi}\|_\infty,\quad
 T_v=\|(R_2)_\phi\|_\infty.
 \tag{Y.18}
$$

用 (Y.13) 的两个非负线性形式 $C,C_1$，完整附加费用可直接写为

$$
 \begin{aligned}
 (\Delta X)_0={}&BE_0+(T_1+LA)C+L\mathcal E M/m_g,\\
 (\Delta X)_M={}&2|m|B_1C,\\
 (\Delta X)_1={}&BE_1+(T_2+L_2A+LB_1)C
                 +(T_1+LB)C_1+(L_2\mathcal E+LB)M/m_g,\\
 (\Delta X)_Y={}&BY+(T_v+V_1A)C+V_1\mathcal E M/m_g .
 \end{aligned}                                         \tag{Y.19}
$$

右侧各项都是四态的明确非负线性组合，所以 (Y.19) 定义一个
完整 $4\times4$ 非负矩阵 $\Delta\mathcal A_R$。
它与 (Y.7) 相加即可控制同一近似中心的物理 Jacobi 在 moving 变量中的
准确接线；逆向用相同绝对残差费用。这里没有逆根权。

证明如下。周期 Green 核给 $\|e\|_\infty\le\pi B/8$，
$\|e_\phi\|_\infty=\|P_0b\|_\infty\le2B$。因此共同速度在
$E_0,E_1,Y$ 各只增加 $B$，mean 单独用 (Y.17) 的准确式，
不能把它也粗写为漂移平均零。由 $\|I\|_{2\to2}=1/4$，

$$\|t\|_2\le AC+\mathcal E M/m_g.$$

更紧的一阶式保留所有 mean：

$$
 t_\phi=(2P_0-I_{\rm id})(b_\phi\chi)-b\chi_\phi
                           -(z/m)P_0b,
$$

其中 $I_{\rm id}$ 是恒等算子。$2P_0-I_{\rm id}$ 在完整 $L^2$
上是等距算子：mean 特征值为 $-1$，其余频率为 $+1$。
故

$$\|t_\phi\|_2\le B_1C+BC_1+B M/m_g.$$

分别对 $R_\phi\chi+Q_\phi t$、它的一阶角导及其第二分量应用三角
不等式，恰好给 (Y.19)。这一步既没有丢 mean，也不需要残差的第三导。

## 6. 可从现有 moving 残差数据直接支付的系数

若原生 producer 给完整 unnormalized moving 残差
$\mathcal R=(\mathcal R_1,\mathcal R_2)$，则

$$
 R=\mathcal R-Q_\phi\chi_{\mathcal R},\qquad
 \chi_{\mathcal R}=\frac1vI\left(
     \mathcal R_2-\frac{\langle\mathcal R_2\rangle}{m}v\right).
 \tag{Y.20}
$$

这是准确 $T_Q^{-1}$，不是把两种 residual 的第二分量直接等同。
在本题 $u=\alpha U,v=s+\alpha V$，实际
$\mathcal R=\alpha(\mathcal R_U,\mathcal R_V)$；
其中 $\mathcal R_V$ 已通过真实恒等式
$s'=\beta s(1-Ks^2)$ 保留全部 $s'$。若 producer 未包含这一项，
不能使用上述缩放。

中心有限 $M$ 模、真实目标只依 $r$，所以完整 moving residual 角支持
至多 $3M$，包括原目标区间/无限 primitive 余项；这些余项是径向标量
系数不确定性，不能生成更高角模。因此已付的完整 $A_0,A_1$ 残差界可给

$$
 \|\mathcal R_{\phi\phi}\|_\infty
 \le12M\,\|\mathcal R_\phi\|_{A_0},
 \qquad
 \|\mathcal R_{\phi\phi}\|_\infty
 \le(12M)^2\|\mathcal R\|_{A_0}.                         \tag{Y.21}
$$

取二者较小者合法。这是准确支持及全系数范数的界，不是物理角 Fourier
截断声明。

设 $z_{\mathcal R}=\langle\mathcal R_2\rangle$。对
$\chi_{\mathcal R}$ 连续求导：

$$
 (\chi_{\mathcal R})_\phi
 =\mathcal R_2/v-z_{\mathcal R}/m-(v_\phi/v)\chi_{\mathcal R},
$$
$$
 (\chi_{\mathcal R})_{\phi\phi}
 =(\mathcal R_2)_\phi/v-\mathcal R_2v_\phi/v^2
 -\left(v_{\phi\phi}/v-v_\phi^2/v^2\right)\chi_{\mathcal R}
 -(v_\phi/v)(\chi_{\mathcal R})_\phi.                    \tag{Y.22}
$$

其零阶 $L^\infty$ 可先以有限完整 $A_0$ 原函数界 $1/4$ 支付，再除以
真实 gap $g$。最后

$$
 R_\phi=\mathcal R_\phi-Q_{\phi\phi}\chi_{\mathcal R}
                            -Q_\phi(\chi_{\mathcal R})_\phi,
$$
$$
 R_{\phi\phi}=\mathcal R_{\phi\phi}
 -Q_{\phi\phi\phi}\chi_{\mathcal R}
 -2Q_{\phi\phi}(\chi_{\mathcal R})_\phi
 -Q_\phi(\chi_{\mathcal R})_{\phi\phi}.                  \tag{Y.23}
$$

因此 (Y.18) 只需已有的实际中心三阶有限角 jet、$g,m$ 和完整
moving residual 的 $A_0,A_1$，无需未知解更高导。
还可直接用

$$
 B\le\|R_2\|_\infty/g,\qquad
 B_1\le\|(R_2)_\phi\|_\infty/g+\|R_2\|_\infty V_1/g^2
$$

取得最后两个系数。所有范数都须在同一个连续径向盒支付。

## 7. 接口范围和程序状态

新的
[fourfold_codazzi_final_moving_strict_energy.py](../scripts/fourfold_codazzi_final_moving_strict_energy.py)
准备直接消费最终 fullR 中心和原完整 intrinsic 493盒/真实根邻域，
在 $[0,119/500]$ 保持实际新 $\nu$，计算 (Y.7)、全部 dyadic 跳和
(Y.15)–(Y.16) 的两个矩阵。它不会把旧候选常数转授新候选。
可以逐完整行保存前缀，只有完整连续 cover 才输出全域传播。
**该新程序尚未执行，没有本篇新 native 数字。**

最后的短 strict 段须另付到新共同 PPoly 片左端
$2147184947341121/9007199254740992$。共同片内的真实 physical
fold/Airy 端口由对应新证明消费；不能把变角曲线冒充恒定径向截面。
若在光滑片内把 moving Jacobi 接到 physical Jacobi，须付
(Y.19)。若跨实际 PPoly 接缝，还须付第3节指出的准确物理复合接线；
本篇没有把跳很小当作接线恒等。

所有源和参数列均从原完整物理含义转换，独立 mean 保留。
返回小除数、完整正帽/远端标签联立及非线性后验仍继续；
本篇完成的是可实际支付的全频强源和端口公式。
