# R133 续篇：旧径向 Taylor 消费的双分支代数对称与完整角尾

2026-11-14，phase_inverse。

**解析消费引理。** 接
[旧径向完整 Fourier 递推](R133-supplement-old-radial-first-Airy-Taylor-and-complete-Fourier-root-recurrence.md)
(P.1)--(P.25)。
下面两点允许同一次新 finite algebra 消费完整两分支，并直接给出
Taylor 尾的 Wiener 费用。它们不改变修正或原参数，不代替实际
域门、旧 $I/J$、even mean 或全局 strong 验证。

## C.1 全复参数盘上的准确 $\epsilon$ 对称

固定任意同一允许的复 $\delta$。
背景 $u,v,K,\beta,\gamma,\eta,d$，
fold $T,X,A$ 和 $G,Q,\mu$ 全都不依赖 $\epsilon$。
这里没有对 $\delta$、$\rho$、$\phi$ 取共轭。

令 $w_0^\epsilon=(a_0^\epsilon,b_0^\epsilon)$。
由原 (P.9)，
$$
 a_0^-=a_0^+,\qquad b_0^-=-b_0^+.
 \tag{C.1}
$$
局部 scalar 微分部分不依赖 $\epsilon$；
完整 cross term 是
$i\epsilon\vartheta Q(Tb_0^\epsilon,a_0^\epsilon)$。
所以原完整 degree-zero 第一强迫满足
$$
 F_b^-=F_b^+,\qquad F_a^-=-F_a^+ .
 \tag{C.2}
$$
这里仍包括 $r_Q$、$V_0$、$T_0$、径向导数与全部 mean。

leading determinant $\Delta=a_0^2-Tb_0^2$ 不变，
因而原 (P.14) 归一化强迫满足
$$
 f_b^-=f_b^+,\qquad f_a^-=-f_a^+ .
 \tag{C.3}
$$
将此代入旧径向三角递推 (P.18)--(P.19)，根值
$\mathcal A_0=0,\mathcal B_0=f_{b,0}$ 起始给出逐阶准确恒等
$$
 \mathcal A_p^-=-\mathcal A_p^+,\qquad
 \mathcal B_p^-=\mathcal B_p^+ .
 \tag{C.4}
$$
每个 $i\epsilon$ 角向交叉项也按该规律变换。
例如 $\mathcal A$ 方程中的 $i\epsilon\mathcal B_\phi$ 随号变，
而 $\mathcal B$ 方程中的 $i\epsilon\mathcal A_\phi$ 不变；
不存在漏掉一个角项才成立的对称。

再代入完整重构 (P.20)，得到
$$
 \boxed{\qquad
       (a_1)_p^-=-(a_1)_p^+,\qquad
       (b_1)_p^-=(b_1)_p^+ .
       \qquad}
 \tag{C.5}
$$
这对完整角函数和同一复参数逐点成立。
故可只实际计算 $\epsilon=+1$ 的新 finite algebra，
把 $\epsilon=-1$ 记录为 (C.1)--(C.5) 的准确符号映射。
全部相应导数、Fourier 系数和所用范数的两分支绝对上界相同。
这不使用“实基点的数值结果看来共轭”；
也不将真正带 $e^{i\epsilon nX}$ 的两个 Airy 传播分支合成一个。

## C.2 根 series 的支持与数组完整性

每个新 series 系数的 Fourier 支持由 (P.21)--(P.22) 确定。
输出采用 $e^{4ij\phi}$ 的 Laurent 系数；
shift 后完整 ordinary polynomial 乘法再 shift 回来，
因此不发生有限周期卷积 alias。
代码只能删数学上准确为零的边端系数。

带区间的函数恒等式，例如
$X_\phi(0)=1$、$T_\phi(0)=T_{\rho\phi}(0)=0$、
$\mathcal J(0)=\mathcal J_*$
及 $TX_\phi-\mathcal J_*\rho=O(\rho^2)$，
可以先核每个原球包含所声明的准确值，
再使用已证明恒等式建立消费视图。
仅凭“球很小”或“舍入中心为零”不能删项。
这些视图必须记录对应恒等式，原 source/prefix 字节不变。

以最高修正阶 $p=6$ 为例，leading 到8阶、强迫到6阶、
修正两列到6阶的全部系数都保存。
$b_1$ 的完整支持上界是 $|j|\le1536$，
$a_1$ 至多 $|j|\le1344$。
它们是准确有限根 Taylor 系数的支持，
不是原未知高模的角截断；最终 Airy 输入频率仍为全部 $|j|\ge97$。

## C.3 原 canonical 上界到旧 product 圆

先复用真实较大辅助 v2 的原 native
`84e2bd1b7637299e94428b22cc19aba290d0b661f9dbe18dae918bf752f10077`。
其中的 canonical 幅度域为
$$
 R_T=\frac{27}{32000},\qquad \Sigma_V=\frac3{256}.
$$
新消费可尝试选择
$$
 R_\rho=\frac1{6000},\qquad \Sigma_\phi=\frac1{128}.
 \tag{C.6}
$$
这些只是明确待核的新消费参数，不先作为成功门。
必须使用同一已成 native 的 $A_+$、$|X_\rho|$ 和原 old-product
有效域，公开严格核 (P.24)：
$$
 R_\rho<R_{\rm fold},\qquad
 R_\rho A_+^{2/3}<R_T,\qquad
 \Sigma_\phi+R_\rho|X_\rho|<\Sigma_V .
 \tag{C.7}
$$
不得把 $R_T$ 本身当旧径向半径。
(P.24) 的正向 inclusion 与唯一性将真实 canonical 幅度拉回该圆，
而物理认同只在原根 piece 的实际交集中使用。

真实 inner cover 是原 $h=9\cdot10^{-6}$ 的闭区间连同原根 bracket。
若 bracket 是 $[r_-,r_+]$，则对其中真正 $r_*$，
$$
 |\rho|\le h+(r_+-r_-)=:r_{\rm in}.
 \tag{C.8}
$$
接续消费者以此有理数为 $r$，并核 $r<R_\rho$。
不是把区间宽度当零，也不额外制造物理界面。

## C.4 直接完整 Fourier 求和的 Taylor 余项

设同一旧 product 圆给 $|w|\le M_w$，
角内宽为 $\sigma<\Sigma_\phi$，$\Delta=\Sigma_\phi-\sigma>0$。
对每个未计算的径向系数和全部 Fourier 模，
双重 Cauchy 给
$$
 |w_{k,j}|\le M_wR_\rho^{-k}e^{-4|j|\Sigma_\phi}.
 \tag{C.9}
$$
定义
$$
 L_q(\Delta)=\sum_{j\in\mathbb Z}
                    (4|j|)^qe^{-4|j|\Delta},
 \tag{C.10}
$$
其中 $q=0$ 时 mean 项为1，$q>0$ 时 mean 项准确为0。
若 $z=e^{-4\Delta}$，则所需四个完整和为
$$
 L_0=\frac{1+z}{1-z},\qquad
 L_1=\frac{8z}{(1-z)^2},
$$
$$
 L_2=\frac{32z(1+z)}{(1-z)^3},\qquad
 L_3=\frac{128z(1+4z+z^2)}{(1-z)^4}.
 \tag{C.11}
$$
因此在已成前 $p+1$ 个完整根 Fourier 系数之上，
$$
\begin{split}
 \|\partial_\rho^u\partial_\phi^q w\|_{A_\sigma}
 \le{}&\sum_{k=u}^{p}\frac{k!}{(k-u)!}
                  C_{k,q}(\sigma)r^{k-u}\\
 &+M_wR_\rho^{-u}L_q(\Delta)
                   \mathcal T_{p,u}(r/R_\rho),
          \qquad 0\le u\le2,\ 0\le q\le3 .
\end{split}
 \tag{C.12}
$$
所有 signed Fourier 模和 mean 都包含在 (C.10)。
(C.12) 直接付完整角尾，不需要再作一次 angular derivative Cauchy
后另嵌入 Wiener；也不能删除 $L_q$ 而误称同宽 Wiener 界。

若下游只需要 strip sup，则保原 (P.25) 的
$q!\Delta^{-q}$ 版本作为另一个合法界。
程序分别标记 sup 与 Wiener；可在同一函数空间内取多个合法
界的最小值，不在两种空间之间混取。

## C.5 第一修正的旧坐标源仍保两套完整接口

新结果必须保存两幅度的
$w,\partial_\phi^{1,2,3}w,w_\rho,
\partial_\phi^{1,2}w_\rho,w_{\rho\rho}$
及声明宽度，而非只输出一个最大数。
本地 $\mathcal L_0w_1$ 用原完整 (P.11)--(P.13)。
全 old-circle $I/J$ 与独立 even mean 消费用
[准确 mean 压缩及完整第一修正非局部预算](R133-supplement-exact-old-mean-compression-and-first-correction-nonlocal-budgets.md)。

本篇 C.1--C.12 没有删除那个独立 mean 方程，
没有识别有限头响应与真实全频响应，
也没有缩掉任何1079个真实 seam 或正区七源列。
真正全局 strong 费用和 cutoff97 仍必须在这些实际列齐备后核。
