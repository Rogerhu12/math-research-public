# R150 附录：固定正时间半群分母的一阶行完整分类

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / normal_resume_1cf；AI 辅助：GPT-6 Astra Pro。根提出并逐节核验正时间接口；kernel 另全文核验。

状态：已证明。固定正时间半群与固定逆幂的行分类不同。本文不把正向整级数当成全空间的有界算子。

## 1. 结论与实际实现

设
$$
a_j\ge0,\qquad a\in\ell^2,\qquad
X=X_{\sum_j a_j\chi_j},
\qquad S(t)=e^{-tX}\quad(t\ge0).
$$
$X$ 是 R125/R128 的实际最大增生第一阶闭乘子，$S$ 是其收缩 $C_0$ 半群。
给定任意复 $c\in\ell^2$，记
$$
Y=Y_c=X_{\sum_j c_j\chi_j}.
$$
固定任意一个 $t>0$。下列条件等价：

1. $S(t)H\subseteq\operatorname{Dom}Y$。
2. 自然算子 $YS(t)$ 的域为全 $H$，且有界。
3. 存在 $e\in\ell^1(\mathbb C)$ 和复行 $d$，满足
   $$
   \boxed{
   c=e+d,\qquad d_j=0\quad(a_j=0),\qquad
   \sum_{a_j>0}\frac{|d_j|^2}{a_j}<\infty.
   }
   \tag{1.1}
   $$
4. 对每个 $s>0$，自然 $YS(s)$ 都全域有界。

因此“某一个正时间”已经等价于“全部正时间”。自然 $YS(t)$ 总是闭且稠密定义；若声称它有全域有界延拓，则也恰好等价于上述条件。

条件 (1.1) 还等价于完全按原系数计算的条件
$$
\boxed{
\sum_{a_j=0}|c_j|
+
\sum_{a_j>0}
\min\!\left(|c_j|,\frac{|c_j|^2}{a_j}\right)<\infty.
}
\tag{1.2}
$$

在 $a\notin\ell^1$ 时，与[一阶有界比率分类](R150-appendix-positive-anchor-first-ratio-complete-coefficient-classification.md)及其固定逆幂推广比较：那些分类允许另加 $\gamma a$；这里必须没有这一非零斜率分量。特别，在这个不可和情形，
$$
\boxed{
XS(t)\text{ 对每个 }t>0\text{ 都不是全域有界算子。}
}
\tag{1.3}
$$
这不声称 $S(t)$ 缺少稠密的光滑像向量。

## 2. 纯第一阶、占据算子与真实有界 carry

在每位的 Walsh 基 $(1,\chi_j)$ 下，纯算子及占据投影是
$$
S_j^0=
\begin{pmatrix}0&-1\\1&2\end{pmatrix},
\qquad
n_j=\begin{pmatrix}0&0\\0&1\end{pmatrix}.
$$
所以 $\operatorname{Re}S_j^0=2n_j$。实际局部算子为
$$
V_j=(I-N_j)(I+N_j)^{-1},
\qquad \|V_j-S_j^0\|\le8\eta_j.
$$
令
$$
E_b=\sum_j b_j(V_j-S_j^0),\qquad
\kappa=8\|\eta\|_2.
$$
对任意 $b\in\ell^2$，级数在算子范数中绝对收敛，且
$$
\|E_b\|\le\kappa\|b\|_2.
\tag{2.1}
$$
不将 $E_b$ 自动列入 $\mathcal A$。

取
$$
X^0=X-E_a,\qquad
\operatorname{Dom}X^0=\operatorname{Dom}X.
$$
有限 Walsh 柱是该闭算子的图核心；其在该核心上恰为 $\sum_j a_jS_j^0$。
该算子增生，因为在有限柱上
$$
\operatorname{Re}\langle X^0f,f\rangle
=2\sum_j a_j\|n_jf\|^2\ge0,
$$
再按图闭包延拓。
对实 $\lambda>\|E_a\|$，
$$
X^0+\lambda I
=\bigl[I-E_a(X+\lambda I)^{-1}\bigr](X+\lambda I)
$$
满射，因为 $\|(X+\lambda I)^{-1}\|\le1/\lambda$。
所以 $X^0$ 也最大增生。

定义非负自伴占据算子
$$
\mathcal N_a=\sum_j a_j n_j.
$$
具体在 Walsh 基 $\chi_F$（$F$ 有限）上，
$\mathcal N_a\chi_F=(\sum_{j\in F}a_j)\chi_F$。
其形式域由
$$
\|\mathcal N_a^{1/2}f\|^2=\sum_j a_j\|n_jf\|^2<\infty
\tag{2.2}
$$
准确给定；零 $a_j$ 位不施加形式约束。

## 3. 正时间的真实占据形式平滑

### 3.1 单比特端点不等式

置 $B(x)=e^{-xS_j^0}$，$x\ge0$。因 $(S_j^0-I)^2=0$，
$$
B(x)=e^{-x}
\begin{pmatrix}1+x&x\\-x&1-x\end{pmatrix}.
$$
给列向量 $z=(u,v)$，令 $q(s)=-su+(1-s)v$。则
$$
\|n_jB(s)z\|^2=e^{-2s}|q(s)|^2,
$$
以及由增生能量恒等式，
$$
\|z\|^2-\|B(x)z\|^2
=4\int_0^x e^{-2s}|q(s)|^2\,ds.
\tag{3.1}
$$

对任意一次复多项式 $q$ 及 $x>0$，
$$
|q(x)|^2\le\frac4x\int_0^x|q(s)|^2\,ds.
\tag{3.2}
$$
例如写成 $q(s)=\alpha+\beta(2s/x-1)$，右侧积分除以 $x$ 为
$|\alpha|^2+|\beta|^2/3$，再用 Cauchy–Schwarz。
由 $e^{-2x}\le e^{-2s}$，(3.1)—(3.2) 给
$$
\boxed{
xB(x)^*n_jB(x)\le I-B(x)^*B(x).
}
\tag{3.3}
$$
$x=0$ 时亦成立。

### 3.2 有限张量与无穷极限

令
$$
S_N^0(t)=\prod_{j<N}B(ta_j),
\qquad
K_j=B(ta_j)^*B(ta_j).
$$
各 $K_j$ 作用不同位，互相交换，且 $0\le K_j\le I$。
(3.3) 给
$$
t\,S_N^0(t)^*
\Bigl(\sum_{j<N}a_jn_j\Bigr)S_N^0(t)
\le
\sum_{j<N}(I-K_j)\prod_{\substack{k<N\\k\ne j}}K_k
\le I.
\tag{3.4}
$$
最后一个不等式可在这些交换正收缩的共同标量谱上逐点验证：
标量和是独立 Bernoulli 变量中“恰有一次失败”的概率。

这里的无穷张量极限也可直接支付。在原真空 $\Omega=1$ 上，
$$
\langle B(x)\Omega,\Omega\rangle=e^{-x}(1+x)\in[0,1],
\qquad
1-e^{-x}(1+x)\le x^2/2.
$$
所以对 $f$ 只依赖前 $m$ 位、$M>N\ge m$，
$$
\|(S_M^0(t)-S_N^0(t))f\|
\le t\|a_{[N,M)}\|_2\,\|f\|.
\tag{3.5}
$$
证明是将高位乘积向量与真空比较：其范数平方至多1，内积为上述正数的乘积，再用
$1-\prod r_j\le\sum(1-r_j)$。
于是 $S_N^0(t)$ 在有界时间区间强一致收敛到收缩 $C_0$ 半群。

这个极限的生成元确实是 $-X^0$。
对固定有限柱，先固定 $N$ 取 $t\downarrow0$，再用 (3.5) 除以 $t$ 并让 $N\to\infty$，
得到其生成元在有限柱上为 $-\sum_j a_jS_j^0$。
有限柱是 $X^0$ 图核心，而 $X^0$ 最大增生，故该生成元的闭延拓只能是 $-X^0$。
记此半群为 $S^0(t)$。

对固定 $m$，先在 (3.4) 中令 $N\to\infty$；有限和 $\sum_{j<m}a_jn_j$ 有界。
再令 $m\to\infty$，用 (2.2) 的单调形式和，得到
$$
\boxed{
S^0(t)H\subseteq\operatorname{Dom}\mathcal N_a^{1/2},
\qquad
\|\mathcal N_a^{1/2}S^0(t)\|\le t^{-1/2}.
}
\tag{3.6}
$$

### 3.3 实际 carry 的 Duhamel 处理

由于 $X=X^0+E_a$ 且两半群均收缩，在共同域 $\operatorname{Dom}X=\operatorname{Dom}X^0$ 上微分 $S^0(t-s)S(s)f$，积分后再以稠密性延拓，得到实际有界扰动恒等式
$$
S(t)=S^0(t)-\int_0^t S^0(t-s)E_aS(s)\,ds.
\tag{3.7}
$$
(3.6) 给被积向量在 $\mathcal N_a^{1/2}$ 图范数中的可积上界；
奇点 $(t-s)^{-1/2}$ 可积。
先在去掉右端点的区间积分，再用闭算子图的完备性取极限，得到
$$
\boxed{
S(t)H\subseteq\operatorname{Dom}\mathcal N_a^{1/2},
\qquad
\|\mathcal N_a^{1/2}S(t)\|
\le t^{-1/2}+2\|E_a\|\sqrt t.
}
\tag{3.8}
$$
图中强可测性可由有限占据截断的强可测性及 (3.6) 的逐向量极限得到。
此处没有在未付域的向量上直接作用 $\mathcal N_a^{1/2}$。

## 4. 充分方向及明确的算子界

设 $d$ 满足 (1.1) 的加权条件，记
$$
K_d=\Bigl(\sum_{a_j>0}|d_j|^2/a_j\Bigr)^{1/2},
\qquad g_d=\|d\|_2.
$$
纯第一阶由产生、消灭及两倍占据项组成。加权 Cauchy–Schwarz 给消灭项的界
$K_d\|\mathcal N_a^{1/2}f\|$；
产生项由一位交换子再多付 $g_d\|f\|$；
占据项的系数和也由加权 Cauchy–Schwarz控制。
因此在有限柱上
$$
\|Y_df\|
\le4K_d\|\mathcal N_a^{1/2}f\|
 +(1+\kappa)g_d\|f\|.
\tag{4.1}
$$
有限柱在 $\mathcal N_a^{1/2}$ 的图范数中稠密；
由 $Y_d$ 闭性，(4.1) 延到全部形式域，并同时证明该形式域包含于 $\operatorname{Dom}Y_d$。

若 $e\in\ell^1$，则
$$
Y_e=\sum_j e_jV_j\in\mathcal A,\qquad
\|Y_e\|\le6\|e\|_1.
$$
$Y_c=Y_d+Y_e$ 是准确的有界扰动等式：
有限柱为两边的图核心，故从核心等式可识别同一个闭实现。
(3.8)—(4.1) 于是给对全部 $t>0$，
$$
\boxed{
\|Y_cS(t)\|
\le
6\|e\|_1
+4K_d\bigl(t^{-1/2}+2\|E_a\|\sqrt t\bigr)
+(1+\kappa)g_d.
}
\tag{4.2}
$$
这同时付清全域，而非只给初始柱上的估计。

## 5. 任意有限乘积态上的统一真实整向量

本节结合 [R181](R181-bounded-coefficient-bell-polynomial-spectrum-trichotomy.md) 的任意乘积参考态与 [R251](R251-arbitrary-coordinate-heads-and-rearrangement-invariant-first-centers.md) §3 的指数次数尺度，得到下面的统一真实整向量估计，但只为正时间逆像提供所需的 Gaussian 型固定幂界。
它使用同一实际 carry 的局部绝对级数；不从有界 carry 自动推高次域。

### 5.1 参考态和指数激发尺度

取任意有限位乘积单位态
$$
h=\bigotimes_j h_j,\qquad h_j=\Omega\text{ 于充分高位}.
$$
置
$$
s_j=\langle S_j^0h_j,h_j\rangle,\qquad
\beta_h=\sum_j a_js_j.
$$
后式为有限和。以 $h_j$ 为局部真空，令 $\mathcal N_h$ 计数激发位，并定义
$$
H_\tau(h)=\operatorname{Dom}e^{\tau\mathcal N_h},
\qquad \|f\|_{\tau,h}=\|e^{\tau\mathcal N_h}f\|,
\qquad 0\le\tau\le1.
$$
在该乘积基下，$S_j^0-s_jI$ 的真空对角元为0，其余三个矩阵元的模至多6。

对 $0<\delta\le\tau\le1$，纯中心化行在激发次数 $q$ 上的产生、消灭和占据块分别有
$6\|a\|_2\sqrt{q+1}$、$6\|a\|_2\sqrt q$、$6\|a\|_2\sqrt q$ 的界。
由于
$$
\sup_{q\ge0}\sqrt{q+1}\,e^{-\delta q}\le C\delta^{-1/2},
$$
以及改变一个激发位的指数权比至多 $e$，存在绝对常数 $C_0$ 使
$$
\Bigl\|\sum_j a_j(S_j^0-s_jI):
H_\tau(h)\longrightarrow H_{\tau-\delta}(h)\Bigr\|
\le C_0\|a\|_2\,\delta^{-1/2}.
\tag{5.1}
$$

### 5.2 全部真实 carry 在同一尺度上的界

R181 §3 的实际有限链展开为
$$
V_j-S_j^0=\sum_{L\ge1}B_{j,j+L},
\qquad
\|B_{j,j+L}\|
\le18\eta_j\eta_*^{L-1},
\tag{5.2}
$$
其中该项只作用 $L+1$ 位，$\eta_*<1/4$。
对作用于 $L+1$ 位的任意算子 $B$，按这些位外的激发次数分块，
$$
\|B:H_\tau(h)\to H_{\tau-\delta}(h)\|
\le e^{L+1}\|B\|.
\tag{5.3}
$$
这不依赖局部参考态，也不依赖这些位的物理位置。
由 $e\eta_*<1$，
$$
\|E_a:H_\tau(h)\to H_{\tau-\delta}(h)\|
\le
18\|\eta\|_2\|a\|_2
\sum_{L\ge1}e^{L+1}\eta_*^{L-1}.
\tag{5.4}
$$
级数在该加权算子范数中绝对收敛。

结合 (5.1)—(5.4)，有一个只依赖实际进位常数的 $C_*$，使
$$
\boxed{
\|(X-\beta_h I):
H_\tau(h)\longrightarrow H_{\tau-\delta}(h)\|
\le C_*\|a\|_2\,\delta^{-1/2}.
}
\tag{5.5}
$$
其域含义如下：有限柱在 $H_\tau(h)$ 中稠密；
先在有限柱上使用估计，再由 $X-\beta_h I$ 与指数权算子的闭性，
将同一实际闭算子延到全部 $H_\tau(h)$。
因此 (5.5) 不是形式重排所得的另一个算子。

在 $k$ 次迭代中取每步 $\delta=1/k$，从 $H_1(h)$ 逐步到 $H_0(h)$。
因 $h$ 是相对真空，$\|h\|_{1,h}=1$，得到
$$
\boxed{
h\in\bigcap_{k\ge1}\operatorname{Dom}X^k,\qquad
\|(X-\beta_h I)^kh\|
\le (C_*\|a\|_2\sqrt k)^k.
}
\tag{5.6}
$$
$k=0$ 时右侧约定为1。所有常数对全部有限乘积参考态统一。

### 5.3 在这些向量上构造正向整级数

令
$$
\Phi(r)=\sum_{k=0}^\infty\frac{r^k k^{k/2}}{k!},
$$
其中 $k=0$ 项为1。由 $k!\ge(k/e)^k$，该级数对所有有限 $r\ge0$ 收敛，并有明确界
$$
\Phi(r)\le\sum_{k\ge0}\frac{(er)^k}{\sqrt{k!}}
\le\sqrt2\exp(e^2r^2).
$$
上述级数界对所有有限参数有效。最后一步对权 $2^{-k/2}$ 使用 Cauchy–Schwarz。
对固定 $h$ 定义
$$
F_h(z)=e^{z\beta_h}
\sum_{k=0}^\infty\frac{z^k}{k!}(X-\beta_h I)^kh.
\tag{5.7}
$$
(5.6) 及同一估计的 $k+m$ 次版本，保证级数及其逐次 $X$ 作用在紧 $z$ 集上一致收敛。
闭性逐次给
$$
F_h(z)\in\bigcap_{m\ge1}\operatorname{Dom}X^m,\qquad
F_h'(z)=XF_h(z),\qquad F_h(0)=h.
\tag{5.8}
$$
对实 $t>0$，
$$
\|F_h(t)\|
\le e^{t\operatorname{Re}\beta_h}
\Phi(C_*t\|a\|_2).
\tag{5.9}
$$

在 $0\le s\le t$ 上，$F_h(s)$ 在 $X$ 图范数中连续；
实际半群在 $\operatorname{Dom}X$ 上可微并与 $X$ 域交换。
于是乘积法则给
$$
\frac{d}{ds}\bigl[S(s)F_h(s)\bigr]
=-XS(s)F_h(s)+S(s)XF_h(s)=0.
$$
因此有准确的真实逆像关系
$$
\boxed{S(t)F_h(t)=h.}
\tag{5.10}
$$
这里只在指定整向量上构造 $F_h$，没有断言全空间存在有界 $e^{tX}$。

## 6. 必要性：不再限制于一个线性核

取实有限支撑 $\theta$，仅假设
$$
\|\theta\|_\infty\le1,\qquad
\sum_j a_j\theta_j^2\le1.
\tag{6.1}
$$
本节没有 $\sum_j a_j\theta_j=0$ 的附加条件。

沿用一阶完整分类中的两态
$$
\xi_{\theta_j}=\cos b_j\,1+i\sin b_j\,\chi_j,
\qquad b_j=-\tfrac12\arcsin\theta_j,
\qquad
\xi(\theta)=\bigotimes_j\xi_{\theta_j}.
$$
纯局部期望准确为
$$
\langle S_j^0\xi_{\theta_j},\xi_{\theta_j}\rangle
=1-\sqrt{1-\theta_j^2}+i\theta_j.
$$
所以两态的主行均值 $\beta_\pm$ 满足
$$
\operatorname{Re}\beta_\pm
=\sum_j a_j(1-\sqrt{1-\theta_j^2})
\le1.
\tag{6.2}
$$
其虚部可以很大；(5.9) 只使用实部。

由 §5，存在实际向量 $f_\pm=F_{\xi(\pm\theta)}(t)$，使
$$
S(t)f_\pm=\xi(\pm\theta),\qquad
\|f_\pm\|\le
C_{t,a}:=e^t\Phi(C_*t\|a\|_2).
\tag{6.3}
$$
若自然 $YS(t)$ 全域有界，范数为 $M$，则
$$
\|Y\xi(\pm\theta)\|\le MC_{t,a}.
$$
对纯辅助行 $Y^0=\sum_jc_jS_j^0$，两次期望的准确差是
$$
\langle Y^0\xi(\theta),\xi(\theta)\rangle
-\langle Y^0\xi(-\theta),\xi(-\theta)\rangle
=2i\sum_jc_j\theta_j.
$$
真实 carry 两次分别付 $\|E_c\|$，从而
$$
\boxed{
\left|\sum_jc_j\theta_j\right|
\le MC_{t,a}+\|E_c\|.
}
\tag{6.4}
$$

设
$$
\mathscr E=c_0\cap\ell^2(a),\qquad
\|z\|_{\mathscr E}
=\max\!\left(\|z\|_\infty,
\sqrt{\sum_j a_j|z_j|^2}\right).
$$
由齐次性，(6.4) 对全部实有限列给统一的 $\mathscr E$ 范数界。
复列分开实虚部，故 $z\mapsto\sum_jc_jz_j$ 在整个有限列空间上连续；
有限列在 $\mathscr E$ 中稠密，所以它连续延拓到 $\mathscr E$。

将 $\mathscr E$ 等距嵌入
$$
z\longmapsto(z,\sqrt a\,z)
\quad\text{于 }c_0\oplus_\infty\ell^2.
$$
复 Hahn–Banach 和该直和的对偶给
$$
\sum_jc_jz_j
=\sum_je_jz_j+\sum_j b_j\sqrt{a_j}\,z_j,
\qquad e\in\ell^1,\quad b\in\ell^2.
$$
逐坐标比较，得 $c=e+d$、$d_j=\sqrt{a_j}b_j$，即 (1.1)，包括全部零 $a_j$ 位。

这里的区别是 (6.4) 控制整个 $\mathscr E$，不只控制某个不连续线性泛函的核；
因此没有另加 $\gamma a$ 的自由度。

## 7. 自然闭图、有界延拓和系数形式

自然定义
$$
\operatorname{Dom}(YS(t))
=\{f:S(t)f\in\operatorname{Dom}Y\}.
$$
$S(t)$ 有界、$Y$ 闭，所以这个自然乘积闭。
它稠密定义：$S(t)\in A'$；
取 R186 给 $Y$ 的强收缩正则器 $R_\varepsilon$，其像在 $\operatorname{Dom}Y$ 且
$R_\varepsilon\to I$ 强。
实际第一阶的完整域被 $A'$ 保持，故
$S(t)R_\varepsilon H\subseteq\operatorname{Dom}Y$，
即 $R_\varepsilon H\subseteq\operatorname{Dom}(YS(t))$。

因此自然域若是全 $H$，闭图定理就给有界。
若闭的稠密自然图有一个全域有界延拓，则按该延拓的连续性逼近任意输入，
再用自然图闭性，也迫自然域全 $H$。
这完成条件1、2和有界延拓版本的等价。
§4 和 §6 完成其余方向。

最后证明 (1.2)。
若 (1.2) 成立，在 $a_j>0$ 位按 $|c_j|>a_j$ 分割：
大值部分放入 $e$，小值部分放入 $d$；零 $a_j$ 位全部放入 $e$。
反向若 $c=e+d$，则在 $a_j>0$ 位有
$$
\min(|c_j|,|c_j|^2/a_j)
\le2|e_j|+4|d_j|^2/a_j.
$$
证明：若 $|e_j|\ge|c_j|/2$，用第一个上界；否则 $|d_j|>|c_j|/2$，用第二个。
零位 $d_j=0$，故其绝对和也有限。

现在额外假设 $a\notin\ell^1$。由于 $a_j\to0$ 且 $\sum a_j=\infty$，
$$
\sum_j\min(a_j,a_j^2/a_j)=\sum_j a_j=\infty.
$$
所以 $c=a$ 不满足条件，给 (1.3)。
更一般，任意非零 $\gamma a$ 也不满足 (1.2)。
若在一阶完整分类中 $c=\gamma a+e+d$，则本稿条件等价于其中唯一斜率 $\gamma=0$。

若 $a\in\ell^1$（包括 $a=0$），则对每个加权余项，
$$
\sum_j|d_j|\le K_d\sqrt{\sum_j a_j}<\infty.
$$
所以 (1.1) 恰好是 $c\in\ell^1$。此时 $X$ 有界，$S(t)$ 是全空间有界单位，与该分类一致；$\gamma a$ 已能吸收到可和部分，不在这里声称斜率必须为零。

## 8. 范围

1. 这是每一个固定正时间的自然全空间分母分类，包含真实 carry 与全部定义域。
2. (3.8) 是占据形式域的平滑；它不能被替换成 $S(t)H\subseteq\operatorname{Dom}X$，后者在 $a\notin\ell^1$ 时由 (1.3) 明确失败。
3. §5 的正向整级数只在指定有限乘积态及其线性张成上构造，不产生全空间有界反半群。
4. 结论没有自动传到未知闭不变子空间或旗子商上的限制，也没有付清正常见证的聚合成本。
5. 完整 Hilbert 不变子空间问题仍未解决。

依赖：R125/R128 的实际第一阶闭域与正行最大增生；R181 §§2—3 的任意乘积参考态和真实局部 carry 展开；R186 的共同强正则器；一阶完整系数分类的两态坐标。§§3、5—6 为本稿新增的正时间预算与分类证明。

## 9. 允许选择半群锚时的准确 $\ell^{4/3}$ 阈值

本节改变量词：辅助行 $c$ 已给定，允许选择非负 $a\in\ell^2$ 及固定 $t>0$。
由主定理，
$$
\boxed{
\exists\,a\in\ell^2_+,\ t>0:
Y_c e^{-tX_a}\text{ 自然全域有界}
\quad\Longleftrightarrow\quad
c\in\ell^{4/3}.
}
\tag{9.1}
$$

必要性：写 $c=e+d$ 为主定理的分解。$e\in\ell^1\subset\ell^{4/3}$；
对 $d$，Hölder 给
$$
\sum_j|d_j|^{4/3}
=
\sum_{a_j>0}
\left(\frac{|d_j|^2}{a_j}\right)^{2/3}
(a_j^2)^{1/3}
\le
\left(\sum_{a_j>0}\frac{|d_j|^2}{a_j}\right)^{2/3}
\left(\sum_ja_j^2\right)^{1/3}<\infty.
\tag{9.2}
$$
故 $c\in\ell^{4/3}$。

充分性：取 $a_j=|c_j|^{2/3}$。则
$$
\sum_ja_j^2=\sum_j|c_j|^{4/3}<\infty,\qquad
\sum_{a_j>0}|c_j|^2/a_j=\sum_j|c_j|^{4/3}<\infty.
$$
因此主定理直接适用，且不需要可和余项。
若另外要求所选 $a$ 不可和，可以给它再加任意固定
$r\ge0$、$r\in\ell^2\setminus\ell^1$；权增大只会减少加权平方和。
这没有要求原 $c$ 具有固定相位。

更一般，对有限族 $c^{(1)},\ldots,c^{(d)}\in\ell^2$，
存在同一个非负平方可和锚 $a$，使全部
$Y_{c^{(i)}}e^{-tX_a}$ 自然全域有界，当且仅当每个 $c^{(i)}\in\ell^{4/3}$。
充分性可统一取
$$
v_j=\left(\sum_{i=1}^d|c_j^{(i)}|^2\right)^{1/2},
\qquad a_j=v_j^{2/3};
$$
此时 $\sum_jv_j^{4/3}\le\sum_i\sum_j|c_j^{(i)}|^{4/3}$。

还有一个准确的参数代价等式。
在不先拆出可和项的情况下，对非零这样的有限族，
$$
\boxed{
\inf_{\substack{a\ge0\\\|a\|_2=1}}
\sum_{j:a_j>0}\frac{v_j^2}{a_j}
=\|v\|_{4/3}^2.
}
\tag{9.3}
$$
约定 $a_j=0,v_j\ne0$ 时成本为无穷。
下界由 (9.2) 得到；取
$$
a_j=\frac{v_j^{2/3}}
{\left(\sum_kv_k^{4/3}\right)^{1/2}}
$$
达到等号。此式优化的是加权行分解成本，不是声称已算出
$\|Y_ce^{-tX_a}\|$ 的精确最小值。

例如 $c_j=(j+1)^{-p}$、$p>1/2$ 时，
存在这样的半群锚当且仅当 $p>3/4$；
临界 $p=3/4$ 仍不满足 (9.1)。
这与用 $X_c^{-1}$ 正则化正行 $c$ 的能力不同。

## 10. 同一固定半群的明确收缩强*主理想单位

本节记录固定半群分母自身的强主理想锚，避免只从单射稠密像推测该性质。
令
$$
X_{a,<m}=\sum_{j<m}a_jV_j\in\mathcal A,\qquad
a^{\ge m}=a\,\mathbf1_{j\ge m},
\qquad
U_m=e^{tX_{a,<m}}\in\mathcal A.
$$
每个 $U_m$ 为实际有界单位，不要求其范数一致有界。

[R240 可数正半群乘积](R240-appendix-countable-positive-first-semigroup-products.md)
的有限加法恒等式给
$$
\boxed{
S_a(t)U_m=e^{-tX_{a^{\ge m}}}=:Q_m,\qquad
\|Q_m\|\le1.
}
\tag{10.1}
$$
此处前缀生成元有界，因而取消它的指数不存在域问题。

实际一阶在真空上的准确值为
$$
1\in\operatorname{Dom}X_{a^{\ge m}},\qquad
X_{a^{\ge m}}1=\sum_{j\ge m}a_j\chi_j.
$$
在该真实域内积分半群微分式，得到
$$
\boxed{
\|(Q_m-I)1\|
\le t\|a^{\ge m}\|_2\longrightarrow0.
}
\tag{10.2}
$$
全部 $Q_m$ 与 $\mathcal A$ 交换，故对固定 $F\in\mathcal A$，
$$
\|(Q_m-I)F1\|\le t\|F\|\|a^{\ge m}\|_2.
$$
$\mathcal A1$ 稠密且 $Q_m$ 收缩，因此 $Q_m\to I$ 强。
又 $Q_m\in A'$ 均为 $C$ 对称，
$Q_m^*=CQ_mC$，所以同时 $Q_m^*\to I$ 强。
因此
$$
\boxed{
\|S_a(t)U_m\|\le1,\qquad
S_a(t)U_m\longrightarrow I\quad\mathrm{SOT}^*.
}
\tag{10.3}
$$
这给固定 $S_a(t)\mathcal A$ 内的明确收缩强*单位序列。

如 R230/R267 的一般强单位论证，在任意有限放大和实际闭 $A$ 不变旗的子商上，
同一序列诱导收缩强单位；由交换性消核、由像逼近恒等给稠密像。
所以每个 $S_a(t)$ 在这些真实子商上仍单射且稠密像。
这里的结论来自同一组有界强单位，而不是将环境中的单射稠密像直接下传。

主稿 §5 对 $h=1$ 也已给实际向量 $g=F_1(t)$，满足 $S_a(t)g=1$。
这个真空原像事实和 (10.3) 都不表示
$S_a(t)H\subseteq\operatorname{Dom}X_a$；不可和 $a$ 时主定理恰好排除了后者。

## 11. 可数正半群乘积的范围与未付接口

R240 的可数乘积分类已证明：
非负一阶半群因子的规范可数乘积，若有非零弱极限，则累计非负行属于 $\ell^2$，
而该极限就是单个实际 $e^{-X_a}$。
因此 (9.1) 也给完整量化结论：

> 对给定第一阶辅助行，允许选择任意有限或规范可数个正一阶半群因子，
> 并要求所得分母的极限非零，能够使自然辅助乘积全域有界的行类，
> 仍恰为 $\ell^{4/3}$。

零弱极限不能作为非零分母；不加入发散标量重标定、符号相消或复杂生成元。
既有 R240 的高阶循环向量配对障碍没有因此被取消。

上述全空间一阶分类、可选锚阈值和强单位共同说明了这类分母的准确能力，
但没有把一般有限秩正常见证的谱向量限制成一阶行，
也没有构造其指定的配对域或聚合范数上界。
