# R138 补篇：真实齐次核由原 96 个低频根数据唯一确定

2026-11-20，visible-exact-astra-ac637-20261120 / joint_kernel。

本篇只消费已成的原 high 下界 `44750653724/1`、实际 mean 分母、
X/Y 完整结果和 GB `44745355257/1`；没有新的科学计算。结论是同一
真实齐次问题的核向原 low96 根空间的读出为单射，因而其实维数至多 96。
不据此授予满射、定量逆、参数族或加入未知参数后的增广算子。

## 1. 原问题与读出

固定 [V 第 9 节](R138-supplement-Volterra-Grushin-energy-and-root-defect-trace.md)
的同一 Qrepair、原实际参数和真实线性算子 $DF_0$。记其原实对称
齐次核为 $\mathcal K_0$：普通、affine、外端独立源和 prescribed
high-stable 根输入全部为零；原 finite low/mean 边界行及原 transmission
全部保留。有限 head 到完整 high 的作用仍在原方程中。
本篇没有令未知的有限 head 或 mean 为零，也没有使用 WVC hybrid 代替
真实 $DF_0$。

对 $h=(h_1,h_2)\in\mathcal K_0$，在真正 $r_*$ 取

\[
 f=h_1(r_*,\phi),\qquad \mu=\langle h_2(r_*,\cdot)\rangle,
 \quad P_L=P_{1\le j\le96},\quad P_H=P_{j\ge97},
 \quad S=P_LN+P_HN^{1/3},\quad z=S^{-1}f,
 \tag{KI.1}
\]

其中角变量是原 moving $\phi$，$N=|D_\phi|$ 的标量非零频率为
$4j$。原实 odd-fourfold 空间的 low 部分有恰好 96 个实维度。
按 [U.1](R138-supplement-complete-root-angular-form-and-two-scalar-geometry.md)，
原根行准确为

\[
 h_2(r_*)=\mu+P_HN^{1/3}Jf .
 \tag{KI.2}
\]

因此这里只把原 low nonmean even 根行置于其本来规定的齐次值，完整
high even 和独立 mean 均保留。以归一基 $\sqrt2\sin(4j\phi)$ 表示，定义

\[
 \mathscr L:\mathcal K_0\longrightarrow\mathbb R^{96},
 \qquad \mathscr Lh=P_Lz .
 \tag{KI.3}
\]

这里右侧指其 96 个实 Fourier 坐标；选择另一固定归一基不改变单射性。

**命题。** $\mathscr L$ 为单射，故

\[
 \boxed{\dim_{\mathbb R}\mathcal K_0\le96.}
 \tag{KI.4}
\]

## 2. 已成常数与完整根源

所有本节角范数使用完整 $2\pi$ 圈的归一平均。记

\[
 E=\mathcal E/(2\pi),\qquad B=\mathcal B/(2\pi),\qquad
 \mathsf H(\phi)=\vartheta(\phi)
 H(r_*,\Theta(\phi)),\qquad \vartheta=\Theta_\phi .
 \tag{KI.5}
\]

$H$ 是原辅助旋转的真实角缺陷，不是原方向 $h$。即使原 BVP 的
独立源均为零，它也不能在证明开始时设为零。

原 high 全角消费者的[完整 actual](../notes/original_high_root_lower_bound_ci/run-44750653724-1/original-high-root-lower-bound.json)及[独立后验核验](R138-supplement-actual-original-high-root-lower-bound.md)均已公开。
其保存后完整十进制球给以下有向有理后果：

\[
 \lambda_H>7/10,\qquad C_H^\times<4,\qquad C_q<19.
 \tag{KI.6}
\]

具体字段依次是 `complete_actual_high_lower_bound` 的 lower、
`complete_nonhomogeneous_source_coefficients.C_H_cross_upper` 的 upper 和
`C_quad_upper` 的 upper。该下界覆盖原**全部** $j\ge97$，并保留
完整 mean rank、六个局部项和两个环境 primitive 项；不是有限截断
或只对一个高频的下界。

同 actual 内只读嵌入的完整 X 结果给 $A_\Theta<5/2$。
实际 mean 结果给 $\mathcal D>17/20$，所以 U.10 的完整消元合法。
[F.1--F.7](R138-supplement-root-source-elimination-and-concave-finite-gate.md)
已经在同一真实 frame 上证明

\[
 \widetilde{\mathcal B}_L/(2\pi)
 \ge \mathfrak b_*(Sz)/(2\pi)
       -C_H^\times\|z_H\|_2\|\mathsf H\|_{H^{-1/3}_\phi}
       -C_q\|\mathsf H\|_{H^{-1/3}_\phi}^2
 \quad\text{当 }z_L=0.
 \tag{KI.7}
\]

这里 $C_H^\times$ 是 HC/relative R.26 的完整 high 列源交叉费用。
式 (KI.7) 中已保留 F.2 的两份 mean 交叉项与两个纯源项；
$\|\mathsf H\|_{H^{-1/3}}$ 使用非齐次 Sobolev 权，包含环境零模。
不把仅在 $z_L=0$ 成立的 (KI.7) 延伸到任意 low 数据。

## 3. 零 low 读出下的完整根费用

设 $h\in\mathcal K_0$ 且 $\mathscr Lh=0$，即 $z_L=0$。由真实
high 压缩下界，直接有

\[
 \mathfrak b_*(Sz)/(2\pi)\ge\lambda_H\|z_H\|_2^2 .
 \tag{KI.8}
\]

此时 low/high 交叉完全为零，无需为相对 Schur 预算另付一个
$(1-\theta)$ 损失。令 $t=\|\mathsf H\|_{H^{-1/3}_\phi}$，
对 (KI.7) 的非负标量 $\|z_H\|_2$ 完成平方，得到

\[
 \widetilde{\mathcal B}_L/(2\pi)
 \ge -Q_{\rm src,H} t^2,
 \qquad Q_{\rm src,H}=C_q+\frac{(C_H^\times)^2}{4\lambda_H}
 <19+\frac{40}{7}=\frac{173}{7}<25 .
 \tag{KI.9}
\]

这是对完整源 $\mathsf H$ 的下界，尚未把它设零。其真正物理角到
moving 角的 density 拉回由 F.8 及原完整 X 资格给

\[
 \|\mathsf H\|_{H^{-1/3}_\phi}^2
 \le A_\Theta\|H(r_*)\|_{H^{-1/3}_\theta}^2,
 \qquad A_\Theta<5/2 .
 \tag{KI.10}
\]

这里两边范数均为归一范数；把 (KI.9) 乘以 $2\pi$ 时，右侧范数
平方也乘以 $2\pi$。因此在 V 的原非归一物理圈记号下，准确得到

\[
 \widetilde{\mathcal B}_L
 \ge-C_*\|H(r_*)\|_{H^{-1/3}_\theta,\,d\theta}^2,
 \qquad 0\le C_*=A_\Theta Q_{\rm src,H}<125/2<367 .
 \tag{KI.11}
\]

没有额外或遗漏的 $2\pi$，也没有把 $\phi$ 当作物理 $\theta$。
唯一角密度费用是 (KI.10)。

## 4. GB 严格余量与原方向归零

[GB 实际结论](R138-supplement-actual-capped-Hhalf-body-absorption-and-root-allowance.md)
`44745355257/1` 已用完整保存球支付三个 body 门及
$C_{\rm allow}>367$。取其非负向上端点构成

\[
 M=\begin{pmatrix}
 2-a_{EE}&-a_{EB}/2\\-a_{EB}/2&1-a_{BB}
 \end{pmatrix}>0,\qquad r=(r_E,r_B)^T .
 \tag{KI.12}
\]

$r_E,r_B$ 仍是原完整 Y/V.21--22 的 $H^{2/3}\to H^{-1/3}$
根缺陷估计；本篇没有把已成的 $H^{1/2}$ 体估计冒作新根迹。
由 GB.23--24 和 (KI.11)，

\[
 M-C_*rr^T\succeq\tfrac12M>0 .
 \tag{KI.13}
\]

原真实修正能量恒等式 T.18 与完整体误差预算，则对
$x=(\sqrt E,\sqrt B)^T$ 给

\[
 x^T(M-C_*rr^T)x\le0.
 \tag{KI.14}
\]

(KI.13) 迫使 $E=B=0$。随后旧 V.8 及 V.21 的完整有界估计分别给
$H=0$ 于体内和 $H(r_*)=0$ 于原 $H^{-1/3}$ 根迹空间，故
$\mathsf H=0$。这一步在吸收之后才合法。

又因 $ea\sigma>0$、(K>0) 于开正区，

\[
 \mathcal E=\int ea\sigma\bigl[(b-uc)^2+Kv^2c^2\bigr]=0
 \quad\Longrightarrow\quad b=c=0\quad\text{几乎处处}.
 \tag{KI.15}
\]

V.28 所用的同一完整 $D\Psi$ 可逆，真实 $v,m$ gap 和逆角资格均已付，
所以原方向 $h=0$。原 weak 图/一阶方程辨认其原边界迹与 transmission，
因而不是只让内开区间的一个代表为零而留下独立端点态。
特别，原 mean $\mu$ 同样为零；也可在 $f=0,\mathsf H=0$ 后由
完整 U.9 和 $\mathcal D>17/20$ 直接读出。

## 5. 弱域、实维数与资格边界

上述积分先对原同域光滑方向成立。V 第 9 节已由**同一个实际 full-real-delta
七列高图**辨认原弱齐次解，并给全态 $L^2$、有限体能量、真实根缺陷迹
和分片积分恒等式的合法极限。原 stable 输入为零时，准确根矩阵还给
所需的 $z_H\in L^2$，所以 (KI.7)--(KI.9) 的有界根型及源对偶可沿
该同域逼近传到原弱核。原连续 Qrepair 与齐次 transmission 没有新造的
接口原子；原分片系数、原接口和所有 mean 行均按已有合同保留。

因此 $\ker\mathscr L=\{0\}$。由于原问题、根迹和固定 $S^{-1}$ 均为实线性，
对任意两个核元素的差应用此结论即证 (KI.3) 单射。
一个向 $\mathbb R^{96}$ 的线性单射直接给 (KI.4)，不需要预先假定
Fredholm 性、closed range 或存在任何逆。

此结论没有证明这 96 个自由读出全部可达，也没有证明核恰好为零。
它不适用于添加 $\nu$ 或其他未知参数后的增广核，不能替代 finite-rho、
七端口、两条独立 RHS、负区连接或非线性族的原任务。
已成负 96/97 根型和被排除的全域接收器比较预算继续按原范围保留；
这里利用的是原齐次核在 **low 根读出为零** 的限制，不否认那些结论。
