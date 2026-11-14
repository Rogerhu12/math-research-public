# R150 附录：有限多正 first 的共同图域与辅助行完整系数分类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：已证明。根推导并逐节核验共同图、半占据权、joint kernel 的 Hahn–Banach 延拓及有限维消元。固定有限族正行，不将共同图域替换成正总行的单一自然域。

## 1. 设置、结论与旧范围扣除

固定有限整数 $q\ge1$ 及非负行
$$
a^\nu=(a^\nu_j)_{j\ge0}\in\ell^2,\qquad a^\nu_j\ge0,
\qquad1\le\nu\le q.
$$
允许零行和 $\ell^1$ 行，不要求每个 first 空谱。
记
$$
X_\nu=X_{\sum_j a^\nu_j\chi_j},\qquad
A_j=\sum_{\nu=1}^q a^\nu_j,\qquad
\mathcal D=\bigcap_{\nu=1}^q\operatorname{Dom}X_\nu.
\tag{1.1}
$$
这里 $A_j$ 是标量总权，和原模型算子 $A$ 区分。
总行 $(A_j)$ 仍在 $\ell^2$。

对任意复 $c\in\ell^2$，令 $Y_c=X_{\sum c_j\chi_j}$。
给共同图域范数
$$
\|f\|_{\mathcal D}
=\left(\|f\|^2+\sum_{\nu=1}^q\|X_\nu f\|^2\right)^{1/2}.
\tag{1.2}
$$

**定理。** 以下条件等价：

1. $\mathcal D\subseteq\operatorname{Dom}Y_c$。
2. 存在固定 $M<\infty$，对所有有限 Walsh 柱 $f$ 有
   $$
   \|Y_cf\|\le M\|f\|_{\mathcal D}.
   \tag{1.3}
   $$
3. 存在 $\gamma_1,\ldots,\gamma_q\in\mathbb C$、$e\in\ell^1(\mathbb C)$
   和复行 $d$，使
   $$
   \boxed{
   c_j=\sum_{\nu=1}^q\gamma_\nu a^\nu_j+e_j+d_j,\qquad
   d_j=0\ (A_j=0),\qquad
   \sum_{A_j>0}\frac{|d_j|^2}{A_j}<\infty.
   }
   \tag{1.4}
   $$

在条件3下，残差 $Y_c-\sum_\nu\gamma_\nu X_\nu$
对共同一阶图的相对界为零：对每个 $\epsilon>0$ 存在 $C_\epsilon$，使
$$
\left\|\left(Y_c-\sum_\nu\gamma_\nu X_\nu\right)f\right\|
\le\epsilon\left(\sum_\nu\|X_\nu f\|^2\right)^{1/2}
+C_\epsilon\|f\|,
\qquad f\in\mathcal D.
\tag{1.5}
$$
$\gamma$ 一般不唯一，精确歧义见 §6。

[R186](R186-multimode-common-domains-maximal-polynomial-graphs-gauge-cyclicity.md)
已给共同图完备性、正则器与有限柱共同图核心。
[R201](R201-positive-first-ratio-domain-obstruction-and-full-plane-spectrum.md)
在有限个不交支持正行中给正总锚不能控制独立分量的具体反例。
本稿新增固定任意有限正族的完整系数判据；
不把 R201 的单一总锚商结论改称共同域分类。

## 2. 完整共同图与核心上的估计

R186 §3 给 $(\mathcal D,\|\cdot\|_{\mathcal D})$ 完备，
§6 式 (6.5) 给有限 Walsh 柱是这个共同图的图核心。
若条件1成立，$Y_c:\mathcal D\to H$ 是闭算子：
共同图收敛特别给 $H$ 收敛，故 $Y_c$ 的原闭性识别极限。
闭图定理遂给条件2。

反过来，若条件2成立，取有限柱 $f_n$
在 (1.2) 的共同图范数下逼近 $f\in\mathcal D$。
对 $f_n-f_m$ 用 (1.3)，$Y_cf_n$ Cauchy。
$Y_c$ 闭性给 $f\in\operatorname{Dom}Y_c$。
所以条件1与2等价。
这里只用真实共同图核心，不把分别的单算子图核心自动拼成共同核心。

## 3. 加权残差的充分方向

置
$$
N_A\chi_E=\left(\sum_{j\in E}A_j\right)\chi_E,\qquad
K^2=\sum_{A_j>0}\frac{|d_j|^2}{A_j}.
$$
$K<\infty$ 也保证 $d\in\ell^2$，因为总权有界。

按照已推
[加权相对域稿](R150-appendix-weighted-first-relative-domains-local-ratios-and-leading-homogeneous-cyclicity.md)
的实际创建、删除和占据估计，
对有限柱 $f$ 有
$$
\|Y_d^0f\|\le4K\sqrt{\langle N_Af,f\rangle}
+\|d\|_2\|f\|.
\tag{3.1}
$$
该纯估计只使用非负权 $(A_j)$，
不要求这个总行的单一 first 域等于 $\mathcal D$。

记真实 carry
$$
E_\nu=X_\nu-X_\nu^0,\qquad
\|E_\nu\|\le\kappa\|a^\nu\|_2,\qquad
\kappa=8\|\eta\|_2,
$$
以及 $E_\Sigma=\sum_\nu E_\nu$。
有限柱上逐项相加二次型给
$$
2\langle N_Af,f\rangle
=\sum_\nu\operatorname{Re}\langle X_\nu f,f\rangle
-\operatorname{Re}\langle E_\Sigma f,f\rangle.
\tag{3.2}
$$
令 $Q(f)=(\sum_\nu\|X_\nu f\|^2)^{1/2}$。
由 Cauchy–Schwarz，
$$
\langle N_Af,f\rangle
\le\tfrac12\sqrt q\,Q(f)\|f\|
+\tfrac12\|E_\Sigma\|\|f\|^2.
\tag{3.3}
$$
加上 $Y_d$ 自身的有界 carry，
(3.1)—(3.3) 给
$$
\|Y_df\|
\le2\sqrt2Kq^{1/4}\sqrt{Q(f)\|f\|}
+\left[2\sqrt2K\sqrt{\|E_\Sigma\|}
+(1+\kappa)\|d\|_2\right]\|f\|.
\tag{3.4}
$$
Young 不等式使第一项被
$\epsilon Q(f)+2K^2\sqrt q\,\epsilon^{-1}\|f\|$
控制。

有限柱共同图核心和 $Y_d$ 闭性将这个估计延到全部 $\mathcal D$；
所以 $\mathcal D\subseteq\operatorname{Dom}Y_d$，残差相对界为零。
$Y_e=\sum e_jV_j$ 全域有界；
在共同有限柱上有
$$
Y_c=\sum_\nu\gamma_\nu X_\nu+Y_e+Y_d.
$$
同一个共同图逼近和 $Y_c$ 闭性把等式与估计延到 $\mathcal D$。
因此条件3推出条件1，并得到 (1.5)。
没有使用任何无界算子自然和预先闭的假设。

## 4. 必要性中的同一组有限乘积态

假设条件2。取实有限支撑列 $\theta$，满足
$$
\sum_j a^\nu_j\theta_j=0\quad(1\le\nu\le q),\qquad
\sum_j A_j\theta_j^2\le1,\qquad
\|\theta\|_\infty\le1.
\tag{4.1}
$$
使用
[单锚完整分类](R150-appendix-positive-anchor-first-ratio-complete-coefficient-classification.md)
§3 的实际单比特态
$$
\xi_{\theta_j}=\cos\beta_j\,1+i\sin\beta_j\,\chi_j,\qquad
\beta_j=-\tfrac12\arcsin\theta_j,
$$
并令 $\xi(\theta)=\bigotimes_j\xi_{\theta_j}$。
它是单位有限柱。

纯一位均值为
$$
\langle S_j\xi_{\theta_j},\xi_{\theta_j}\rangle
=v(\theta_j)+i\theta_j,\qquad
v(t)=1-\sqrt{1-t^2}\in[0,t^2].
\tag{4.2}
$$
对每条主行，
$$
\mu_\nu(\theta)
=\sum_j a^\nu_jv(\theta_j)\in[0,1],
\tag{4.3}
$$
因为 (4.1) 使虚部为零且 $a^\nu_j\le A_j$。
对 $\theta$ 和 $-\theta$ 同样成立。
不同位的纯中心余项正交，故
$$
\|X_\nu\xi(\pm\theta)\|
\le\sqrt{1+9\|a^\nu\|_2^2}+\|E_\nu\|
=:K_\nu.
\tag{4.4}
$$
常数不依赖支撑大小和位置。

所以条件2给
$$
\|Y_c\xi(\pm\theta)\|
\le M\left(1+\sum_\nu K_\nu^2\right)^{1/2}
=:M_0.
$$
两个纯辅助均值的差准确为
$2i\sum_jc_j\theta_j$。
实际 carry $E_c=Y_c-Y_c^0$ 分别以其范数付两次误差，
得到
$$
\boxed{\left|\sum_jc_j\theta_j\right|\le M_0+\|E_c\|.}
\tag{4.5}
$$

## 5. 直接 Hahn–Banach 延拓与有限维消元

定义复 Banach 空间
$$
\mathscr E_A=
\left\{z\in c_0:\sum_jA_j|z_j|^2<\infty\right\},
\quad
\|z\|_{\mathscr E_A}
=\max(\|z\|_\infty,\sqrt{\sum_jA_j|z_j|^2}).
$$
在 $c_{00}$ 上定义
$$
T(z)=\left(\sum_j a^\nu_jz_j\right)_{\nu=1}^q,\qquad
C_0(z)=\sum_jc_jz_j,\qquad
\mathcal K=\ker T.
$$
由 (4.5)、齐次性及实虚分开，
$C_0|_{\mathcal K}$ 是 $\mathscr E_A$ 范数下的有界复线性泛函。

此处不要求 $\mathcal K$ 在 $\mathscr E_A$ 中稠密。
直接使用复 Hahn–Banach，将它延拓为
$\ell\in\mathscr E_A^*$。
于是 $C_0-\ell$ 在 $c_{00}$ 上消掉 $\ker T$，
因而降为有限维 $\operatorname{Ran}T\subseteq\mathbb C^q$ 上的线性泛函。
任意延拓这个有限维泛函到 $\mathbb C^q$，得到
$$
C_0(z)-\ell(z)=\sum_{\nu=1}^q\gamma_\nu\sum_j a^\nu_jz_j,
\qquad z\in c_{00}.
\tag{5.1}
$$
这是纯有限维代数步骤，不把可能不连续的 $T$ 当成全 $\mathscr E_A$ 上的连续映射。

将 $\mathscr E_A$ 等距嵌入
$$
c_0\oplus_\infty\ell^2,\qquad
z\mapsto(z,(\sqrt{A_j}z_j)_j).
$$
其像闭。再次使用复 Hahn–Banach 及直和对偶，
$$
\ell(z)=\sum_je_jz_j+\sum_jb_j\sqrt{A_j}z_j,
\qquad e\in\ell^1,\quad b\in\ell^2.
$$
令 $d_j=\sqrt{A_j}b_j$。
对 (5.1) 取坐标向量就得到 (1.4)，
包括零 $A_j$ 位的可和条件。
条件2推出条件3，主定理证明完毕。

## 6. 斜率歧义及逐系数判据

记
$$
\mathscr J_A=\ell^1+
\left\{d:d_j=0\ (A_j=0),\
\sum_{A_j>0}|d_j|^2/A_j<\infty\right\}.
$$
若 $\gamma^0$ 是一个可行向量，
全部可行系数向量准确为仿射空间
$$
\boxed{
\gamma^0+
\left\{\delta\in\mathbb C^q:
\sum_\nu\delta_\nu a^\nu\in\mathscr J_A\right\}.
}
\tag{6.1}
$$
例如两条主行相同时，$(1,-1)$ 属于歧义空间；
即使主行在普通序列意义上线性独立，也可能只差一个 $\mathscr J_A$ 行。
因此不能重复单锚稿的无条件唯一斜率结论。

对给定 $\gamma$，置
$z_j=c_j-\sum_\nu\gamma_\nu a^\nu_j$。
(1.4) 等价于可直接检查的条件
$$
\boxed{
\sum_{A_j=0}|z_j|
+\sum_{A_j>0}\min\left(|z_j|,\frac{|z_j|^2}{A_j}\right)<\infty.
}
\tag{6.2}
$$
证明与单锚稿相同：
正位上 $|z_j|>A_j$ 的部分给 $\ell^1$，其余给加权平方和；
反向若 $z=e+d$，
$\min(|z|,|z|^2/A)\le2|e|+4|d|^2/A$。
零位全部由 $\ell^1$ 承担。

## 7. 可和或零总行、共同图与总锚的区别

如果 $\sum_jA_j<\infty$，
所有主 first 都全域有界，所以 $\mathcal D=H$。
而加权行满足
$$
\sum_j|d_j|
\le\left(\sum_jA_j\right)^{1/2}
\left(\sum_{A_j>0}|d_j|^2/A_j\right)^{1/2}<\infty.
$$
因此 (1.4) 退化成准确的 $c\in\ell^1$，
与实际一阶有界性一致。
若总行完全为零，(1.4) 同样只允许 $c\in\ell^1$。

若总行不可和，不能将 $\mathcal D$ 换成
$\operatorname{Dom}X_{\sum A_j\chi_j}$。
例如两条不交支持、各自不可和的正行 $a^1,a^2$，
辅助 $c=a^1$ 显然满足 (1.4)，并在共同图上受控。
但 R201 已证
$\operatorname{Dom}X_{a^1+a^2}\not\subseteq\operatorname{Dom}X_{a^1}$。
本稿没有抹去这个实际域差。

所有判据均在原 $H$ 上。
它没有把共同域包含自动下传到未知子商，
也不据此判定一般剪切核或完整 ISP 已完成。
