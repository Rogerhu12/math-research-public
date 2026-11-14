# R150 附录：正主行上一阶有界比率的完整系数分类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf；AI 辅助：GPT-6 Astra Pro。
状态：已证明。根完整核验两态必要性、稠密核延拓和自然域等价。[加权相对域稿](R150-appendix-weighted-first-relative-domains-local-ratios-and-leading-homogeneous-cyclicity.md)给充分方向；本稿新增反向必要性、准确自然域等价以及唯一的相对主斜率。
只处理一阶比率，不将它直接代替一般剪切核或普通 ISP。

## 1. 定理及自然域约定

取
$$
a_j\ge0,\qquad a\in\ell^2\setminus\ell^1,\qquad
X=X_{\sum_j a_j\chi_j},\qquad L=X^{-1}\in A'.
$$
$X$ 取 R125/R128 的实际闭实现。它空谱，$L$ 全域有界且拟幂零。
给任意复 $c\in\ell^2$，令 $Y=Y_c=X_{\sum_jc_j\chi_j}$。
所有一阶算子的共同有限 Walsh 柱记为 $\mathcal C$；它是各自的图核心。

首先按准确的自然域定义
$$
T_c=YL,\qquad
\operatorname{Dom}T_c=\{h\in H:Lh\in\operatorname{Dom}Y\}.
\tag{1.1}
$$
不预设这个域等于 $H$。

**定理。** 以下条件等价：

1. $\operatorname{Dom}X\subseteq\operatorname{Dom}Y$。
2. (1.1) 的自然域为全 $H$，且 $T_c$ 有界。
3. 存在有限 $M$，使
   $$
   \|Yf\|\le M\|Xf\|\qquad(f\in\mathcal C).
   \tag{1.2}
   $$
4. 存在 $\gamma\in\mathbb C$、$e\in\ell^1(\mathbb C)$ 和复行 $d$，使
   $$
   \boxed{
   c=\gamma a+e+d,\qquad
   d_j=0\ (a_j=0),\qquad
   \sum_{a_j>0}\frac{|d_j|^2}{a_j}<\infty.
   }
   \tag{1.3}
   $$

条件4中的 $\gamma$ 唯一。$e,d$ 的分解不要求唯一。
零 $a_j$ 的全部辅助系数必须进入真正可和的 $e$，没有隐藏除零约定。

此外，令
$$
\mathcal B=\overline{\operatorname{alg}}(I,\mathcal A,L).
$$
当上述条件成立时，
$$
T_c\in\mathcal B,\qquad
\sigma_{B(H)}(T_c)=\{\gamma\}.
\tag{1.4}
$$
这里 $\mathcal B$ 的唯一字符将 $T_c$ 送到 $\gamma$。
$Y$ 对 $X$ 的最小相对界准确为 $|\gamma|$。

## 2. 先支付自然域与核心界的等价

$T_c$ 总是闭的：若 $h_n\to h$ 且 $YLh_n\to k$，则
$Lh_n\to Lh$；$Y$ 闭给 $Lh\in\operatorname{Dom}Y$ 和 $YLh=k$。

它的自然域也稠密。对 $f\in\mathcal C$，
$L(Xf)=f\in\operatorname{Dom}Y$，故 $X\mathcal C\subseteq\operatorname{Dom}T_c$。
又因 $X$ 满射且 $\mathcal C$ 是 $X$ 图核心，$X\mathcal C$ 在 $H$ 中稠密：
给 $h\in H$，以有限柱在 $X$ 图范数下逼近 $Lh$ 即可。

因为 $LH=\operatorname{Dom}X$，条件1等价于 (1.1) 全域。
结合闭图定理，得到条件1与2等价。条件2立即给条件3。

反过来，若 (1.2) 成立，给 $f\in\operatorname{Dom}X$，
取 $f_n\in\mathcal C$ 使 $f_n\to f$、$Xf_n\to Xf$。
对 $f_n-f_m$ 使用 (1.2)，$Yf_n$ 为 Cauchy。
$Y$ 的闭性于是给 $f\in\operatorname{Dom}Y$，并保留同一界。
所以条件3也等价。

同样，若仅知道 $T_c$ 的自然图具有一个全域有界延拓，
闭性及 $X\mathcal C$ 的稠密性也迫其自然域已经全域。
本稿的“有界比率”没有把一个未闭的初始商擅自当作全域算子。

## 3. 真实一位均值及有限乘积向量

使用 R130 的实际/纯分解
$$
V_j=S_j+K_j,\qquad
S_j=c_j^+-c_j^-+2n_j,\qquad
\|K_j\|\le8\eta_j,
$$
其中 $c_j^+,c_j^-,n_j$ 是 Walsh 创建、删除、占据矩阵。
在基 $(1,\chi_j)$ 中，
$$
S_j1=\chi_j,\qquad S_j\chi_j=-1+2\chi_j.
\tag{3.1}
$$
并且 $\|S_j\|\le3$。

给实数 $\theta\in[-1,1]$，取
$$
\beta=-\tfrac12\arcsin\theta,\qquad
\xi_\theta=\cos\beta\,1+i\sin\beta\,\chi_j.
$$
它是单位向量，$\xi_0=1$。内积对第一变量线性。
直接用 (3.1) 算得
$$
\boxed{
\langle S_j\xi_\theta,\xi_\theta\rangle
=1-\sqrt{1-\theta^2}+i\theta.
}
\tag{3.2}
$$
记 $v(\theta)=1-\sqrt{1-\theta^2}$，则
$$
0\le v(\theta)\le\theta^2.
\tag{3.3}
$$

对任意实有限支撑列 $\theta=(\theta_j)$、$|\theta_j|\le1$，
令
$$
\xi(\theta)=\bigotimes_j\xi_{\theta_j}.
$$
只有有限个因子不为参考常向量，所以
$\xi(\theta)\in\mathcal C$ 且 $\|\xi(\theta)\|=1$。

对任意 $b\in\ell^2$，记纯一阶为 $Y_b^0=\sum_jb_jS_j$。
在这个有限乘积向量上，
$$
\mu_b(\theta):=\langle Y_b^0\xi(\theta),\xi(\theta)\rangle
=\sum_jb_j\bigl(v(\theta_j)+i\theta_j\bigr).
\tag{3.4}
$$
右端只有有限个非零项。
各个单坐标作用减去其均值后的向量两两正交，且都与
$\xi(\theta)$ 正交。因此实际的方差计算给
$$
\begin{aligned}
\|Y_b^0\xi(\theta)\|^2
&=|\mu_b(\theta)|^2+
\sum_j|b_j|^2\left(
\|S_j\xi_{\theta_j}\|^2
-|\langle S_j\xi_{\theta_j},\xi_{\theta_j}\rangle|^2
\right)\\
&\le |\mu_b(\theta)|^2+9\|b\|_2^2.
\end{aligned}
\tag{3.5}
$$
无限的零参数尾仍是正交的 $\ell^2$ 和，故 (3.4)—(3.5) 的极限合法。

全部实际 carry 已保留：下面的差首先在共同有限柱上成立，右端给它的全域有界延拓。
$$
E_b:=Y_b-Y_b^0=\sum_jb_jK_j\in B(H),\qquad
\|E_b\|\le\kappa\|b\|_2,\quad
\kappa=8\|\eta\|_2.
\tag{3.6}
$$
级数按算子范数绝对收敛。这些 $E_b$ 不被宣称为 $\mathcal A$ 元素。

## 4. 核上的真实线性泛函界

假设条件3成立。令 $\theta$ 为实有限支撑列，满足
$$
\sum_ja_j\theta_j=0,\qquad
\sum_ja_j\theta_j^2\le1,\qquad
\|\theta\|_\infty\le1.
\tag{4.1}
$$
因为 $a_j\ge0$，(3.3)—(3.4) 给
$$
\mu_a(\theta)=\sum_ja_jv(\theta_j)\in[0,1].
$$
对 $\theta$ 和 $-\theta$ 都如此。由 (3.5)—(3.6)，
$$
\|X\xi(\pm\theta)\|
\le \sqrt{1+9\|a\|_2^2}+\|E_a\|=:K_a<\infty.
\tag{4.2}
$$
于是 (1.2) 给 $\|Y\xi(\pm\theta)\|\le MK_a$。

(3.4) 的两个纯均值满足准确等式
$$
\mu_c(\theta)-\mu_c(-\theta)
=2i\sum_jc_j\theta_j.
\tag{4.3}
$$
实际 carry 的两次均值之差不被省略：分别用
$|\mu_c(\pm\theta)|\le MK_a+\|E_c\|$ 控制即可。
因此
$$
\boxed{
\left|\sum_jc_j\theta_j\right|
\le MK_a+\|E_c\|=:K_c
}
\tag{4.4}
$$
对全部 (4.1) 成立。这个常数与支撑的位置、大小及 $\theta$ 无关。

## 5. 从稠密核延拓得到精确系数分解

定义复 Banach 空间
$$
\mathscr E=
\left\{z\in c_0:\sum_ja_j|z_j|^2<\infty\right\},
\qquad
\|z\|_{\mathscr E}
=\max\left(\|z\|_\infty,
\left(\sum_ja_j|z_j|^2\right)^{1/2}\right).
\tag{5.1}
$$
$c_{00}$ 在 $\mathscr E$ 中稠密。
只在 $c_{00}$ 上定义线性泛函
$$
A_0(z)=\sum_ja_jz_j,\qquad C_0(z)=\sum_jc_jz_j.
$$
这里 $A_0$ 是一个标量泛函，不是原算子 $A$。

由 (4.4) 及齐次性，$C_0$ 在实的 $\ker A_0$ 上有界。
若复 $z\in\ker A_0$，因为 $a$ 实，
$\operatorname{Re}z,\operatorname{Im}z$ 都在实核内。
故
$$
|C_0(z)|\le2K_c\|z\|_{\mathscr E}
\qquad(z\in c_{00}\cap\ker A_0).
\tag{5.2}
$$

这个核在整个 $\mathscr E$ 中稠密。
事实上，取有限集 $F$ 使 $s_F=\sum_{j\in F}a_j\to\infty$，并置
$$
h_F=\frac{1_F}{s_F}.
$$
则
$$
A_0(h_F)=1,\qquad
\|h_F\|_{\mathscr E}
=\max(s_F^{-1},s_F^{-1/2})\longrightarrow0.
\tag{5.3}
$$
对每个固定 $z\in c_{00}$，
$z-A_0(z)h_F\in\ker A_0$ 且趋于 $z$。
再用 $c_{00}$ 的稠密性即可。

所以 (5.2) 唯一延拓为某个连续复线性泛函
$\ell\in\mathscr E^*$。
$C_0-\ell$ 在 $c_{00}\cap\ker A_0$ 上为零。
取一个 $z_0\in c_{00}$ 使 $A_0(z_0)=1$，置
$$
\gamma=C_0(z_0)-\ell(z_0).
$$
对任意 $z\in c_{00}$，将
$z-A_0(z)z_0$ 代入核上的等式，得到
$$
\boxed{C_0(z)-\ell(z)=\gamma A_0(z).}
\tag{5.4}
$$
这一步没有把不连续的 $A_0$ 延拓成 $\mathscr E^*$ 元素。

为识别 $\ell$，把 $\mathscr E$ 等距嵌入
$$
c_0\oplus_\infty\ell^2,
\qquad z\longmapsto (z,(\sqrt{a_j}z_j)_j).
$$
像是闭的。由复 Hahn–Banach 及
$(c_0\oplus_\infty\ell^2)^*=\ell^1\oplus_1\ell^2$，
存在 $e\in\ell^1$、$b\in\ell^2$，使
$$
\ell(z)=\sum_je_jz_j+\sum_jb_j\sqrt{a_j}z_j.
\tag{5.5}
$$
令 $d_j=\sqrt{a_j}b_j$。
它在零 $a_j$ 位为零，且 $\sum_{a_j>0}|d_j|^2/a_j\le\|b\|_2^2<\infty$。
对 (5.4) 取各坐标向量，即得
$c_j=\gamma a_j+e_j+d_j$。必要方向证明完成。

## 6. 充分方向和真实有界比率

简述已核加权相对域估计，使本分类的方向完整。
若 $K^2=\sum |d_j|^2/a_j<\infty$，有限柱上的创建、删除、占据估计给
$$
\|Y_d^0f\|\le4K\sqrt{\langle N_af,f\rangle}
+\|d\|_2\|f\|.
$$
真实主行的二次型为
$$
\operatorname{Re}\langle Xf,f\rangle
=2\langle N_af,f\rangle+
\operatorname{Re}\langle E_af,f\rangle.
$$
加上 $E_d$，并用 Young 不等式，得到每个 $\epsilon>0$ 上
$$
\|Y_df\|\le\epsilon\|Xf\|+C_{\epsilon,d,a}\|f\|
\qquad(f\in\mathcal C).
\tag{6.1}
$$
相同柱图核心闭性给 $\operatorname{Dom}X\subseteq\operatorname{Dom}Y_d$。
$Y_e=\sum e_jV_j\in\mathcal A$ 全域有界。
在共同有限柱上，
$$
Y_c=\gamma X+Y_d+Y_e.
$$
于是 (6.1) 及 $\|f\|\le\|L\|\|Xf\|$ 给条件3。
由 §2，完整自然域包含与全域 $Y_cL$ 随后成立；
并非仅从形式行相加直接赠送域。

对 $d$ 的加权尾重复 (6.1) 的更准确平方根界，
可得
$$
Y_dL=\lim_n\left(\sum_{j<n}d_jV_j\right)L
\quad\text{于算子范数}.
\tag{6.2}
$$
其证明是加权尾范数与普通 $\ell^2$ 尾范数均趋零。
故 $Y_dL\in\mathcal B$ 且唯一字符为0：
$\mathcal A$ 只有字符 $\chi$，$L$ 的谱半径为0，
因此 $\mathcal B$ 的任意字符在生成元上的值完全确定。
于是
$$
T_c=\gamma I+Y_dL+Y_eL\in\mathcal B,
\qquad \phi(T_c)=\gamma.
$$
交换有单位 Banach 代数的字符判据给 (1.4)。

## 7. 唯一斜率、相对界及可直接检查的系数条件

对任意有限集 $F$，记 $s_F=\sum_{j\in F}a_j$。
(1.3) 给
$$
\left|\sum_{j\in F}c_j-\gamma s_F\right|
\le\|e\|_1+\|d\|_a\sqrt{s_F}.
\tag{7.1}
$$
所以沿任何 $s_F\to\infty$ 的有限集序列，
$$
\boxed{\frac{\sum_{j\in F}c_j}{\sum_{j\in F}a_j}\longrightarrow\gamma.}
\tag{7.2}
$$
这证明 $\gamma$ 唯一，也给原物理前缀上的具体求值式。
不要求点比值 $c_j/a_j$ 收敛。

由 (6.1)，$Y_c-\gamma X$ 的相对界为0，故最小相对界至多 $|\gamma|$。
$X$ 非有界，存在单位 $f_n\in\operatorname{Dom}X$ 使 $\|Xf_n\|\to\infty$。
若某个相对界 $b<|\gamma|$ 成立，
用
$$
\|Y_cf_n\|\ge |\gamma|\|Xf_n\|
-\|(Y_c-\gamma X)f_n\|
$$
及相对界零，取任意 $\epsilon<|\gamma|-b$ 即矛盾。
所以最小相对界恰为 $|\gamma|$；不宣称这个下确界本身必然取到。

还有完全逐系数的等价表述。
对给定 $\gamma$ 记 $z_j=c_j-\gamma a_j$。
(1.3) 等价于
$$
\boxed{
\sum_{a_j=0}|z_j|
+\sum_{a_j>0}
\min\left\{|z_j|,\frac{|z_j|^2}{a_j}\right\}<\infty.
}
\tag{7.3}
$$
若 (7.3) 成立，在 $|z_j|>a_j$ 的位置将 $z_j$ 放入 $e$，
在 $|z_j|\le a_j$ 的位置放入 $d$；零位全部放入 $e$。
反过来，若 $z=e+d$，每个正位上至少有
$|e_j|\ge |z_j|/2$ 或 $|d_j|\ge |z_j|/2$，故
$$
\min\left\{|z_j|,|z_j|^2/a_j\right\}
\le2|e_j|+4|d_j|^2/a_j.
$$
求和即得 (7.3)。

## 8. 使用边界

本稿把实际一阶有界比率的充分条件补成充要分类。
它解释了为何单纯 $|c_j|\le C a_j$ 不足：
如果没有 (1.3) 的唯一仿射主斜率和可和/加权余项，
则 $\operatorname{Dom}X\not\subseteq\operatorname{Dom}Y_c$，
自然 $Y_cX^{-1}$ 没有全域有界延拓。

本稿没有声称同阶复辅助的剪切核因此非零，
也没有将这个一阶域分类当成一般正常见证的聚合预算上界。
完整 ISP 及不满足其它已核排核机制的范围继续开放。
