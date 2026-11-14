# Carrier 自有参考的完整曲率预算：111 叶与其余七段的接合

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）。
日期：2026-11-13。
状态：已证明的实际数据应用，真解存在和完整场误差仍为明确条件。

## 1. 结论与参考对象

将原 cell 0 / seg7 的第一 substage 换为已经完整执行的物理半径 carrier，
其余七段保持原 R48 高度。新第一段完整覆盖原物理求积的 111 叶；
它的非均值高度、实际一阶与二阶径向导数来自同一个函数，
两个端点的非均值两 jet 与原参考完全相同。
全段使用同一完整均值根及一次贯穿所有段的高度积分常数。
以下称该混合高度为 $\widehat h_C$。

本次直接在 carrier 自己的实际导数上重付 R95 第 3 节，得到

$$
 \sup_{\text{第一段},\theta}
 \left\|\frac{\operatorname{Hess}_g\widehat h_C}
 {\sqrt{1-|\nabla_g\widehat h_C|^2}}\right\|
 <8.143011140160913403.
$$

这只是非精确候选的形式矩阵范数，不称为候选实际曲面的主曲率。

**条件性实际曲率结论。** 设 $h$ 是同一真实背景
$g=(1+w^2)dr^2+r^2d\theta^2$ 上的实际 $C^2$ 等距浸入的高度，
满足完整、未投影的 Darboux 方程和同一个完整均值根分支。
若在整个 seg7 的每个径向位置有

$$
 \|P-\widehat P_C\|_{A_\tau^1}
 +\|\overline K-\widehat{\overline K}_C\|_{A_\tau^1}
 \le\varepsilon=\frac1{512},\qquad \tau\ge0,
 \tag{C1}
$$

这里 $P=h_\theta/(rw)$、$h_r=w(1+c+\overline K)$，
范数保留全部非零偶频，而不是只有保存的 20 个模式，则

$$
 \boxed{\sup_{\text{整个 seg7},\theta}|\kappa_i|
 <8.165888306896058136<\frac{33}{4}.}
 \tag{C2}
$$

到 $33/4$ 的余量严格大于 $0.084111693103941864$。
本应用没有支付 (C1)，没有证明外头真解存在，也不提供全曲面 reach、
held 或全时间域的证明。与 R102 第一段旧参考的失败预算没有矛盾：
这里使用一个实际重构并重新验证的新函数，不在两个候选之间逐点取小值。

## 2. 实际输入、执行及同背景

完整 carrier 原执行的 summary SHA256 为
`0ac4b1e14ec34a86035add63e6250660924537c54acc834e497c6ebdd396ae12`，
完整 resource 为
`dee1cef1a748f4459e00a5428dd4b6b1602c3eb442498091b29bd88e0ea1c865`。
两者记录该数学执行正式 child exitcode 0、signal null，全部 111 叶，
20 个非均值高度模式及完整 $J$ 的 $0,2,\ldots,80$ 共 41 个模式。
每叶原记录包括实际 $\widehat h^\perp_{rr}$、完整均值的实际径向导数、
完整 $J$ 与正分母下界。本次没有以 PDE 的二阶值替换候选导数。

脚本逐项核对原输入与数学源码 SHA，并流式消费原 gzip。
同背景 R31 账本 SHA 是
`27e9cac085dd4913cdf14526fec847613bede8fae5367ae72cc143f25b254083`；
它与候选的完整 ready SHA 相同，已付
$K_{\rm bg}\le8$、$0<w<3/25$、$r>1/20$。
其余七段只使用 R102 原实际有理账本
`d01b7310f9d76fa5d5d56f44805c67fedf7be776a78435803943edcda424bc6f`
中相同 $\varepsilon$ 的已付粗界，不重新积分或重算它们。

本次新消费者 [tail_carrier_conditional_curvature.py](../computations/tail_carrier_conditional_curvature.py)
正式 child exitcode 为 0、signal null，耗时 $0.8161814213$ 秒，
wait4 峰 RSS 为 18,000 KiB。九项结构门和 111 个曲率门全部通过。
计算仅为 Python 精确 Fraction 算术，没有 Arb、Node、新 ODE 或新积分。
原输入始终本地读取，没有通过工具传送编码或二进制数据。

## 3. Carrier 自己的连续参考界

对一个叶记其真实范围为 $r\in[r_-,r_+]$、$w\in[w_-,w_+]$，
令 $z_*=w_+^2$、$E_*=1+z_*$、$e_*=1+z_*/2$。
由同背景曲率界，可用

$$
 C_g=8w_+e_*\ge |E'/(2E)|,\qquad
 v=\min\{w_+|\log w|_{r,*},\,8E_*e_*\}\ge |w_r|.
$$

以原保存的完整有限 cosine 系数及其连续区间取

$$
 k_0\ge|\widehat c|+\sum_m|\widehat K_m|,
 \qquad
 p_0\ge\frac{\sum_m m|\widehat H_m|}{r_-w_-}.
$$

$t_0$ 和 $u_0$ 分别围住
$\widehat T=\widehat P_\theta$ 和
$\widehat U=\widehat{\overline K}_\theta-\widehat P$：
直接完整有限质量界与原保存的 $A_\tau^1$ 界除以 3 可以取小，
因为这里比较的是同一个函数、同一叶和同一种物理量。
最小非零频率为 2，故除以 3 合法。

记实际非均值径向二阶质量上界为 $H_*$，
完整均值二阶偏离背景的上界为 $M_*$。取

$$
\begin{aligned}
 d_0&=w_+k_0,&e_0&=w_+p_0,\\
 A_0&=H_*+M_*+C_gd_0,&
 B_0&=\frac{w_+}{r_-}u_0,&
 C_0&=\frac{w_+}{r_-}(k_0+t_0).
\end{aligned}
\tag{C3}
$$

R95 的背景扰动矩阵证明逐叶适用。
其证明不要求参考自身满足 Darboux 方程，只要求参考导数为同一个高度的真实导数。
所以 (C3) 直接支付 carrier 自有参考界，完全不借用旧 R48 的内部两 jet。

## 4. 完整均值根的连续域与 R99 四场矩阵

由 (C1)，四个 $A^0$ 场误差可取

$$
 (e_K,e_P,e_T,e_\theta)
 \le\varepsilon(1/3,1/3,1,1).
$$

先允许 $|c-\widehat c|\le\varepsilon$，在共同盒上取

$$
 p=p_0+\varepsilon/3,\quad k=k_0+4\varepsilon/3,
 \quad t=t_0+\varepsilon,\quad u=u_0+4\varepsilon/3.
$$

定义

$$
 v_D=z_*(2k+k^2+E_*p^2),\quad
 a=1-z_*p^2,\quad d=1-v_D,\quad l=1-k-E_*t.
$$

本次全部叶严格有 $a,d,l,1-k>0$ 以及
$1-z_*(1+k)t/a>0$。
沿非均值输入的实线段，完整均值方程严格单调。
R99 (99.16–17) 给三个正系数 $a_K,a_P,a_T$，并实际验证

$$
 C_m=(a_K+a_P)/3+a_T<1,\qquad
 |c-\widehat c|\le C_m\varepsilon.
 \tag{C4}
$$

为避免用待证均值域循环论证，在候选完整均值根处开始连续。
只要根在允许的 $\varepsilon$ 盒内，R99 的积分差式给出 (C4)。
若有首次触及盒边界，就与 $C_m<1$ 矛盾。
盒内的严格正均值导数又保证局部连续延拓；紧参数区间上其下界一致为正，
故整个非均值输入线段上都存在同一分支。
这保留完整角平均，不将实正性当成未支付的复条带逆。

R99 的五物理导数矩阵 (99.20) 在本次每叶完整输出。
列顺序是 $(\overline K,P,P_\theta,\overline K_\theta)$；
行顺序是 $(h_r,h_\theta,h_{rr},h_{r\theta},h_{\theta\theta})$。
矩阵已经包含 (C4) 的完整均值响应，二阶径向行另加下一节的真实候选缺陷。

## 5. 同叶完整 $J$ 与实际二阶缺陷

本次 carrier 审计直接使用物理 $r$，逐叶强制检查 $r_x=1$。
因此 R99 的准确残差项是

$$
 \widehat R_H=\frac{w\widehat J}{\widehat L}.
$$

先保留原 41 个完整 cosine 区间。
非零质量为 $J_\perp=\sum_{m=2}^{80}|J_m|$；
R77 以同一叶的完整 $D$ 非常数质量、真实 $D_{\min}$ 和 $E_*$
给零模上界。该界与原实际 $J_0$ 上界取小后，再与原完整 $J$ 上界取小。
所有比较都围住同一个完整分子，不删除标量均值或带外模式。

完整 111 叶给

$$
 \sup|\widehat R_H|<0.000117729748874029.
 \tag{C5}
$$

最大叶是 source $x\in[17/256,35/512]$，panel 29。
这与原物理 Darboux 上界 $8.33761\times10^{-6}$ 是不同单位；
本应用始终使用 (C5)，没有将 Darboux 显示数直接当成 $h_{rr}$ 误差。

由 R99，真解与候选的二阶差满足
$|\delta h_{rr}|\le F_K\Delta K+F_Pe_P+F_Te_T+F_\theta e_\theta+|\widehat R_H|$。
令 $\Delta K=\varepsilon/3+C_m\varepsilon$，
$\phi=F_K\Delta K+F_P\varepsilon/3+F_T\varepsilon+F_\theta\varepsilon$。
准确组合角向误差给

$$
\begin{aligned}
 d_1&=d_0+w_+\Delta K,&e_1&=e_0+w_+\varepsilon/3,\\
 A_1&=A_0+\phi+C_gw_+\Delta K+d_H,\\
 B_1&=B_0+\frac{w_+}{r_-}\frac{4\varepsilon}{3},\\
 C_1&=C_0+\frac{w_+}{r_-}(\varepsilon+\Delta K).
\end{aligned}
$$

这里使用 $h_{r\theta}-h_\theta/r=wU$，以及
$h_{\theta\theta}/r^2+(h_r-w)/(rE)$ 的准确同场组合。
因而没有把同一个 $r$ 在两项中分别取不利极值来增加一项无须的 $r_+/r_-$。

置 $\omega=2w_+d_1+d_1^2+E_*e_1^2$，全部叶都有 $\omega<1$。
R31/R95 的矩阵界给

$$
 |\kappa_i|\le
 \frac{8+e_*[\max(A_1,C_1)+B_1]}{1-\omega}.
$$

这得到 (C2)。条件曲率最大叶为 panel 13，
source $x\in[7/256,1/32]$。
同叶可容许的 $d_H$ 下界超过 $0.084144069523953921$；
实际缺陷远在该正余量内。
全部叶的真竖直法向平方下界大于 $0.999525175129636708$。

## 6. 完整接合、位置及尚待支付的门

新第一段与旧其余段的非均值 $H,H_r,H_{rr}$ 在共同端点相同。
完整均值根由同一 $P,\overline K,T$ 确定，因此两侧 $c$ 相同；
完整均值径向微分公式使用相同两 jet 和背景，故 $c_r$ 也相同。
取一个连续的 mean 高度积分常数，便得到实际 $C^2$ 混合高度。
不能在第一段右端重新将 mean 高度差设零。

已正式完成的 paired-mean v4 账本给旧 source-$x$ 参考到新 carrier 的
完整 mean 高度改变量小于 $2.298791\times10^{-10}$。
PA 到 carrier 的连续参考位置差小于 $4.280436\times10^{-7}$，
参考单位向量差小于 $7.600138\times10^{-6}$。
这两项参考 frame 数值不是旧 R48 到 carrier 的完整空间差，
参考单位向量也不是非等距候选的实际法向。

后续可以直接对混合参考使用本次自己的曲率预算，不必强行通过旧 R48 的
内部二阶差来获得 (C2)。但是位置、远点对和 held 若仍使用旧参考，
必须另付旧 R48→PA→carrier 的空间桥以及 (C1)→真解的位置/法向桥。
本应用保留这一独立缺口，不从小 $J$ 推断它已解决。

原始 111 叶计算使用精确 Fraction；输出非负上界向上舍入到 96 个二进制有效位，
正下界向下舍入，最终门在舍入前后都具有严格余量。
所有源码、实际输入与完整输出 SHA、正式资源和重做命令见随附 stable manifest。
