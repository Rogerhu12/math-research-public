# R138 补篇：根锚定与谱体预算组合的必要筛查

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

本篇只限定[RA 根锚定接收器](R138-supplement-root-anchored-local-drift-and-capacity.md)
与[SG 原未加权谱体预算](R138-supplement-complementary-Gram-spectral-body-energy.md)
的这一种组合。它使用已完成的[RS 径向权无关试探](R138-supplement-radial-weight-independent-root-budget-screen.md)、
同一真实96/97 signed型与同一原完整 high 压缩；不排实际正区边界问题、
最优体常数或利用额外可达迹方程的另一种能量法。

## 1. 单次局部 Jacobian 后仍存在的根费用

RS 的完整 Schur 必要性对真正 $D_H^{-1}$、其更紧正乘子压缩比较以及
任意保留源余量的 $0<\vartheta\le1$均适用：

$$
W^*W\succeq C^*(\vartheta D_H)^{-1}C-A_L
\quad\Longrightarrow\quad\|We_{96}\|^2>148.
\tag{RN.1}
$$

这里原 $e_{96}$ 配对真实全高输入；没有将高边界截断至97单模，
没有重新求旧三个 signed矩阵条目，也没有删除独立mean。

对任意局部径向权和自由外截段，RS 的同一个完整试探积分给
$C_{E,\alpha}N_W^2/\rho^2>148/T$。
RA 根初值为恒等，能量只付一次 $\sqrt{\Gamma_{loc}}$，故

$$
\bigl(\alpha_E^{root}(W)\bigr)^2
>\frac{148\Gamma_{loc}}{T}.
\tag{RN.2}
$$

完整source/physical-density项非负，只会增大左侧；没有为证明(RN.2)将它们
从原读出中删掉。原 RS run44758362539/1 的整个保存球严格给
$T<125$，而 $\Gamma_{loc}=\exp D_{loc}\ge1$。因此此组合的第一项必要条件是

$$
a_{EE,sp}+\bigl(\alpha_E^{root}(W)\bigr)^2<2
\quad\Longrightarrow\quad
\boxed{a_{EE,sp}<102/125.}
\tag{RN.3}
$$

进一步的 high/source 根费和完整二维交叉门仍须实际支付；(RN.3)通过并不保证它们。
它不使用尚未求值的 $\Gamma_{loc}$小于某个数的结论。

## 2. 只读旧有向标量得到两个更早的必要门

同一完整 Y 保存球直接给所选标量

$$
E_0>693/500000,\qquad E_1>2719/1000,
\qquad h_E>1869/10^6.
\tag{RN.4}
$$

它们是原算法已经选择并保存的上界数值；这里的lower比较只限制继续使用
这些数值的SG预算，绝不宣称实际残差或最优source常数有这些下界。

若 SG.14 的新 $w_{E,sp}\ge45/2$，SG.15 即给

$$
\begin{split}
a_{EE,sp}
&>\frac{693}{500000}\left(\frac{45}{2}\right)^2
 +\frac{2719}{1000}\frac{1869}{10^6}\frac{45}{2}\\
&=\frac{1632006495}{2000000000}
 =\frac{102}{125}+\frac{6495}{2000000000}.
\end{split}
\tag{RN.5}
$$

故完整门还必须满足

$$
\boxed{w_{E,sp}<45/2.}
\tag{RN.6}
$$

原 X 的完整所选标量又严格给

$$
\Gamma>11839/10000,\qquad
A_\Theta>(15794/10000)^2.
$$

因此保持原body辅助flow的 SG.14 满足

$$
\frac52\Gamma\sqrt{A_\Theta}
>\frac{186985166}{40000000}>\frac{467}{100},
\qquad
w_{E,sp}>\frac{467}{100}\sqrt{C_{sp}}.
\tag{RN.7}
$$

结合(RN.6)，必要地

$$
\boxed{C_{sp}<\left(\frac{2250}{467}\right)^2<24.}
\tag{RN.8}
$$

最后一个严格有理比较为
$2250^2=5062500<24\cdot467^2=5234136$。
三个简单比较 $C_{sp}<24$、$w_{E,sp}<45/2$、$a_{EE,sp}<102/125$
都是独立必要筛查；前一个通过不能省去后两个，更不能省去完整交叉或source门。

## 3. 新完整目标的使用范围

可对 SG.12 的完整4651片新最大值及 SG.14–SG.15 的4条新upper实际求值，
先逐球完整保存、读回，再作上述比较。原 $C_E,w_B,a_{BB}$与其他原
X/Y/GB成功/失败结果全部只读，不重求。
SG.16的两个对角与det三门若通过，SG.17条件性新allowance仍须向下保存；
它只给尚待实际根费用的预算，不将 RN 的必要筛查变成充分逆定理。

这条新组合使用 RA 的真实根初值，与已被 SE 排除的“SG.12 加原整因子
$\Gamma$根接收器”不同。原 SE 排除保持；本篇也没有宣布新组合能够通过。
若新谱upper已经不能通过本页简单门，便不应为同一SG/RA预算另造大型
接收器Gram来重复一个必要条件已经排除的工作。

## 4. 只收紧旧试探系数，不重算T，得到更强门

[实际high41](R138-supplement-actual-original-high-root-lower-bound.md)的完整保存球
还严格给出

$$
b_0<49/50,\quad b_1<101/100,\quad b_2<103/100,
\quad (g_m)_0<201/100,\qquad D>17/20.
\tag{RN.9}
$$

保持RS的同一个真实根代数方向 $z=e_{96}$、$\mathsf H=0$。
令 $R=\sqrt2\cos384\phi$、$b=\rho Y$；完整mean消元后准确有

$$
\omega_{96}=-bR+I(b'R-g_m\ell_{96}),\qquad
\omega_{96}'=384b e_{96}-g_m\ell_{96},
$$
$$
|\ell_{96}|\le\frac{20}{17}\frac{b_2}{384}.
\tag{RN.10}
$$

$\ell_{96}$是原独立mean读出；没有把它设为零。所有范数沿原归一化moving圆周。
沿RS的同一完整环境频率分解，near为 $|k|\ge192$，far为 $0<|k|<192$，
两输出正交；Sylvester gap给

$$
\|I(b'R)\|_2
\le\frac{\sqrt{b_1^2+2b_2^2}}{192}
<\frac{1773}{192000},\qquad
\|g_m\ell_{96}\|_2<\frac{20703}{3264000}.
\tag{RN.11}
$$

这里 $(101/100)^2+2(103/100)^2=31419/10000<(1773/1000)^2$。
环境primitive对mean rank仍用norm1，未错误改成四重scalar的 $1/4$。
于是

$$
\|\omega_{96}\|_2
<\frac{49}{50}+\frac{1773}{192000}+\frac{20703}{3264000}
=\frac{3249564}{3264000}<1,
$$
$$
\|\omega_{96}'\|_2
<384\frac{49}{50}+\frac{20703}{3264000}<377.
\tag{RN.12}
$$

对**同一个**旧 $f=(1-x/\ell)_+$、$\ell=1/100$、同 $h,\eta,K$，
把原RS integrand里的 $(26/25)^2$、$385^2$分别替成 $1$、$377^2$。
逐点已有

$$
1<\frac{24}{25}\left(\frac{26}{25}\right)^2
=\frac{16224}{15625},\qquad
377^2=142129<142296=\frac{24}{25}\,385^2.
\tag{RN.13}
$$

两个原权均非负，故此改进试探的整个能量直接被
$\widehat T=(24/25)T_{old}<120$控制。
这只用已成whole $T_{old}$乘一个正有理数；没有拆分未保存的两个积分分量，
没有求新积分，更没有改变RS旧target或它的保存结果。
因此(RN.2)可纯解析加强为

$$
\bigl(\alpha_E^{root}(W)\bigr)^2>
\frac{148\Gamma_{loc}}{\widehat T}>\frac{37}{30}.
\tag{RN.14}
$$

同一新组合更强的必要门是

$$
\boxed{a_{EE,sp}<23/30,\qquad w_{E,sp}<22,
\qquad C_{sp}<\left(\frac{2200}{467}\right)^2<23.}
\tag{RN.15}
$$

第二项由(RN.4)在 $w_E=22$时给
$a_{EE}>391311921/500000000>23/30$；最后一项用(RN.7)，且
$2200^2=4840000<23\cdot467^2=5016047$。
RN.1–RN.8较松的原门仍然正确，已按它们声明的科学消费者无需修改参数。
只需在其整个新4球实际完成以后直接比较(RN.15)，不重跑任何目标。

## 5. 已成统一lambda的Schur版本单独不能付根预算

作为进一步纯解析范围判断，若后继坚持把真正 $D_H^{-1}$换成已成统一标量
$\lambda_H^{-1}I$，使用原relative R.23的

$$
W^*W\succeq\frac{C^*C}{\vartheta\lambda_H}-A_L,
\qquad 0<\vartheta\le1,
\tag{RN.16}
$$

则原 `complete_actual_high_lower_bound`保存的所选 $\lambda_H<3/4$ 与
同一完整signed条目直接给

$$
\begin{split}
\|We_{96}\|^2
&\ge\frac{|\langle e_{97},Ce_{96}\rangle|^2}
                 {\vartheta\lambda_H}-M_{11}\\
&>\frac{(189/10)^2}{3/4}-\frac{457}{1000}
=\frac{475823}{1000}>475.
\end{split}
\tag{RN.17}
$$

连较松的旧 $T<125$已经强迫根E费用大于 $475/125=19/5>2$。
所以即令所有非负body/source费用为零，这个**特定统一lambda Schur预算**仍不能
通过原能量门。此结论不把已成算子lower当成实际最小谱值的上界；
它只排把这个已选lower拿来替代整个 $D_H$的算法。
真正 $C^*D_H^{-1}C$、保留角依赖的正乘子压缩逆或别的可达迹结构没有被(RN.17)排除。
