# R257：Bell 分支核的统一通常伴随解析半径与真实局部流

日期：2026-11-12（UTC）。作者：kernel。
状态：完整证明。接 R236 全固定阶通常伴随域附录，将其逐阶有限常数加强为同一个未知核上的统一阶乘界。以下只给固定第一阶方向的真实解析流；不据此取得任意 chaos 方向的矩、点乘指数域、中央零阶逆界或原核消失。

## 1. 设置与所用固定阶接口

令
$$
X=X_{a_*+\sum_{j\ge0}a_j\chi_j},\qquad a\in\ell^2,
\qquad B_2=\sum_j a_j^2(I-V_j^2),
$$
$$
Y=\phi(B_2)\in\mathcal A,\qquad T=X-Y,\qquad M=\ker T.
\tag{1.1}
$$
$\phi$ 在0邻域解析，代入为实际全纯演算。置 $g=\|a\|_2$、
$s_m=\sum_{j\le m}|a_j|$。记 $\delta_XB=[X,B]$，$\delta_TB=[T,B]$。

R236 全固定阶附录已在完整自然域证明
$$
\operatorname{Dom}T^n=\operatorname{Dom}(T^*)^n
\quad(n\ge1),
\tag{1.2}
$$
以及有界自伴 $C_T$ 满足
$$
T^*T-TT^*=C_T
\tag{1.3}
$$
于共同二阶域上成立。其每个固定 $\delta_T$、$\delta_{T^*}$ 导数有界并保持完整域。
所以 $M$ 中向量的下述每个有限有序运算已有真实定义域。

本稿不重新证明这些固定阶域，而从该附录的显式估计取得统一的阶数预算。
最终应用于原危险点态平方时，仍保留 $a_*=0$；解析半径结论本身适用于 (1.1) 的一般常数项。

## 2. 原自交换子和 Bell 通常伴随的整导数预算

记 $C_a=[X^*,X]$ 为实际完整图形式给出的有界算子。
R236 附录 (2.2) 在 $r=n+1$ 时给
$$
\|\delta_X^nC_a\|
\le12^n\left[
72\sum_i|a_i|^{n+2}
+648\sum_{m\ge1}\eta_{m-1}s_m^{n+2}
\right].
\tag{2.1}
$$
故对任意有限 $R\ge0$，
$$
\sum_{n\ge0}\frac{R^n}{n!}\|\delta_X^nC_a\|
\le72\sum_i|a_i|^2e^{12R|a_i|}
+648\sum_{m\ge1}\eta_{m-1}s_m^2e^{12Rs_m}<\infty.
\tag{2.2}
$$
第一和由 $72g^2e^{12Rg}$ 控制。第二和有限，因为
$s_m\le g\sqrt{m+1}$、$\eta_{m-1}\le e^{-770\,16^{m-1}}$。

因此
$$
\mathcal C(z)=\sum_{n\ge0}\frac{z^n}{n!}\delta_X^nC_a
\tag{2.3}
$$
是实际 $B(H)$ 值整函数，且在每个参数紧集上按算子范数绝对一致收敛。

R236 附录 (3.1) 同样给
$$
\|\delta_X^rB_2^*\|
\le12^{r-1}\left[
864\sum_i|a_i|^{r+2}
+7776\sum_{m\ge1}\eta_{m-1}
\left(\sum_{i\le m}|a_i|^2\right)s_m^r
\right]\quad(r\ge1).
\tag{2.4}
$$
于是
$$
\begin{aligned}
\sum_{r\ge1}\frac{R^r}{r!}\|\delta_X^rB_2^*\|
\le{}&
72\sum_i|a_i|^2(e^{12R|a_i|}-1)\\
&+648\sum_{m\ge1}\eta_{m-1}
\left(\sum_{i\le m}|a_i|^2\right)(e^{12Rs_m}-1)<\infty.
\end{aligned}
\tag{2.5}
$$
所以
$$
\mathcal B(z)=\sum_{r\ge0}\frac{z^r}{r!}\delta_X^rB_2^*
\tag{2.6}
$$
也是 $B(H)$ 值整函数。

这里的“整”是这些有界导数系数的范数级数结论；
没有使用未经定义的全空间 $e^{zX}$，也没有宣称它们来自全 $B(H)$ 上的有界自同构。

## 3. Bell 全纯轮廓给分支自交换子的正解析半径

设 $\psi(\lambda)=\overline{\phi(\overline\lambda)}$，则 $Y^*=\psi(B_2^*)$。
取固定围住0、位于 $\psi$ 解析域内的轮廓 $\Gamma$。
因为 $\mathcal B(0)=B_2^*$、$\sigma(B_2^*)=\{0\}$，范数连续性给 $\rho>0$，
使所有 $|z|<\rho$、$\lambda\in\Gamma$ 的 $\lambda I-\mathcal B(z)$ 都可逆。
例如将
$$
\sup_{\lambda\in\Gamma}\|(\lambda I-B_2^*)^{-1}\|
\,\|\mathcal B(z)-B_2^*\|<1/2
$$
作为充分条件即可。因此
$$
\mathcal Y(z)=\frac1{2\pi i}\int_\Gamma
\psi(\lambda)(\lambda I-\mathcal B(z))^{-1}\,d\lambda
\tag{3.1}
$$
是该小盘上的真正范数解析函数。

其 $n$ 阶导数在0恰为 $\delta_X^nY^*$。
可由逆恒等式逐阶核验：对 $(\lambda I-\mathcal B(z))R(z,\lambda)=I$ 微分，
与 R236 已付真实域的 Leibniz/逆导数递推比较，两者有相同的初值
$R(0,\lambda)=(\lambda I-B_2^*)^{-1}$ 和相同递推。
再作固定轮廓积分即可。因而没有把一般逆的域保持当作自动事实。

令 $K_Y=[X^*,Y]$。R236 的准确 Jacobi 式为
$$
\delta_X^nK_Y=-[\delta_X^{n-1}C_a,Y]\quad(n\ge1),
\qquad K_Y^*=-\delta_XY^*.
\tag{3.2}
$$
定义整函数
$$
\mathcal K(z)=K_Y-\int_0^z[\mathcal C(w),Y]\,dw.
$$
于是小盘内的解析函数
$$
\mathcal D(z)=
\mathcal C(z)-\mathcal K(z)+\mathcal Y'(z)
+\mathcal Y(z)Y-Y\mathcal Y(z)
\tag{3.3}
$$
满足
$$
\mathcal D^{(n)}(0)=\delta_X^nC_T.
$$
这里使用真实式 $C_T=C_a-K_Y-K_Y^*+Y^*Y-YY^*$，符号由
$K_Y^*=-\delta_XY^*$ 确定。

因为 $\delta_XY=0$，已付域的有限二项式给
$\delta_T=\delta_X-\operatorname{ad}_Y$，两导子交换。因此
$$
\mathcal E(z)=e^{-zY}\mathcal D(z)e^{zY}
\tag{3.4}
$$
在同一小盘解析，且 $\mathcal E^{(n)}(0)=\delta_T^nC_T$。
选择任意 $0<R<\rho$，并置
$$
M_C=\sup_{|z|=R}\|\mathcal E(z)\|<\infty.
$$
Cauchy 不等式给
$$
\boxed{\|\delta_T^rC_T\|\le M_C\,r!\,R^{-r}\quad(r\ge0).}
\tag{3.5}
$$
$C_T$ 自伴且真实通常伴随导数式为
$\delta_{T^*}^rC_T=(-1)^r(\delta_T^rC_T)^*$，所以同样有
$$
\boxed{\|\delta_{T^*}^rC_T\|\le M_C\,r!\,R^{-r}.}
\tag{3.6}
$$

常数可以很大，且依赖固定 $a,\phi$ 和轮廓；本稿只需一个严格正的 $R$。
没有将该局部解析性无证扩成全参数 Bell 逆演算。

## 4. 整个未知核上的统一阶乘界

**定理。** 取
$$
K=\max\{1,\ 2/R,\ \sqrt{2M_C}\}.
\tag{4.1}
$$
则对每个整数 $n\ge0$，
$$
\boxed{
\|(T^*)^nf\|\le K^n n!\,\|f\|
\qquad(f\in M).
}
\tag{4.2}
$$
同一个结论在交换 $T,T^*$ 后成立，即
$\|T^ng\|\le K^nn!\|g\|$ 对所有 $g\in\ker T^*$ 成立。

**证明。** 设 $g_n=(T^*)^nf$、$v_n=\|g_n\|$。由 (1.2)，所有这些向量以及下述有限运算在所需自然域中。
真实伸缩和并把 $C_T$ 移到各 $T^*$ 左侧，给
$$
\boxed{
T(T^*)^nf
=-\sum_{r=0}^{n-1}\binom n{r+1}
(\delta_{T^*}^rC_T)(T^*)^{n-1-r}f
\quad(n\ge1).
}
\tag{4.3}
$$
这是由
$[T,(T^*)^n]=-\sum_{k=0}^{n-1}(T^*)^kC_T(T^*)^{n-1-k}$
及 $\sum_{k=r}^{n-1}\binom kr=\binom n{r+1}$ 得到；右端没有遗漏原先的 $Tf$，因为 $Tf=0$。

完整一阶形式为
$$
\|Tg\|^2-\|T^*g\|^2=\langle C_Tg,g\rangle.
$$
应用于 $g_n$，得到
$$
v_{n+1}^2\le\|Tg_n\|^2+M_Cv_n^2.
\tag{4.4}
$$
$n=0$ 时 $Tf=0$，所以 $v_1\le\sqrt{M_C}v_0\le Kv_0$。

现归纳假设 $v_k\le K^kk!v_0$ 至 $k=n$，$n\ge1$。
由 (3.6)、(4.3)，
$$
\begin{aligned}
\|Tg_n\|
&\le M_C n!K^{n-1}v_0
\sum_{r=0}^{n-1}\frac{(KR)^{-r}}{r+1}\\
&\le2M_C n!K^{n-1}v_0,
\end{aligned}
\tag{4.5}
$$
其中 $KR\ge2$。将其代入 (4.4)，
$$
\frac{v_{n+1}^2}{K^{2n+2}((n+1)!)^2v_0^2}
\le\frac{4M_C^2/K^4+M_C/K^2}{(n+1)^2}
\le\frac{3/2}{(n+1)^2}\le1.
$$
若 $v_0=0$ 结论平凡；上述除法只用于 $v_0>0$。归纳完成。
交换 $T,T^*$ 时自交换子变为 $-C_T$，导数范数界不变，故反向同证。证毕。

## 5. 真正的局部通常伴随流

对 $|z|<1/K$ 定义有界映射
$$
U(z):M\to H,\qquad
U(z)f=\sum_{n\ge0}\frac{z^n}{n!}(T^*)^nf.
\tag{5.1}
$$
(4.2) 给算子范数绝对收敛，并有
$$
\|U(z)\|\le\frac1{1-K|z|},\qquad
\|U(z)-I_M\|\le\frac{K|z|}{1-K|z|}.
\tag{5.2}
$$
这里 $I_M$ 表示 $M$ 向 $H$ 的自然包含。

对任意固定 $p\ge0$，同一估计给
$$
\sum_{n\ge0}\frac{|z|^n}{n!}\|(T^*)^{n+p}f\|
\le\frac{K^pp!}{(1-K|z|)^{p+1}}\|f\|.
\tag{5.3}
$$
对各阶收敛的部分和逐次使用闭算子 $T^*$ 的闭性，得到 $U(z)M$ 属于 $T^*$ 的全部自然幂域；
由 (1.2) 也属于 $T$ 的全部自然幂域。
特别，$\partial_zU(z)f=T^*U(z)f$ 是真实 Hilbert 导数。

若 $|z|<1/(2K)$，(5.2) 给 $U(z)$ 在 $M$ 上有正下界，
所以
$$
M_z:=U(z)M
\tag{5.4}
$$
是闭子空间，$U(z):M\to M_z$ 为有界同构。
例如 $|z|\le1/(4K)$ 时，$\|U(z)f\|\ge(2/3)\|f\|$。

还可准确写出它满足的有界扰动核方程。定义
$$
\mathcal A_*(z)=\sum_{r\ge0}\frac{z^r}{r!}\delta_{T^*}^rC_T,
\qquad
G(z)=\int_0^z\mathcal A_*(w)\,dw
=\sum_{r\ge0}\frac{z^{r+1}}{(r+1)!}\delta_{T^*}^rC_T.
\tag{5.5}
$$
这些级数在 $|z|<R$ 按范数收敛。将 (4.3) 代入 (5.1)，全部双和由 (3.6)、(4.2) 绝对控制，
故可以重排，得到
$$
\boxed{T U(z)f=-G(z)U(z)f,\qquad
M_z\subseteq\ker(T+G(z)).}
\tag{5.6}
$$
$G(z)$ 是真实有界算子，不是形式扰动。
在 $|z|<1/K\le R/2$，例如 $\|G(z)\|\le2M_C|z|$。

局部逆也是真实级数，而非假设 $e^{zT^*}$ 在全空间存在。
若 $|z|+|w|<1/K$，则
$$
\sum_{m,n\ge0}
\frac{|w|^m|z|^n}{m!n!}\|(T^*)^{m+n}f\|
\le\frac{\|f\|}{1-K(|z|+|w|)}.
$$
于是
$$
\sum_{m\ge0}\frac{w^m}{m!}(T^*)^mU(z)f=U(z+w)f.
\tag{5.7}
$$
取 $w=-z$、$2|z|<1/K$，得到 $M_z$ 上实际定义的局部逆映回 $M$。

## 6. 用途与未付条件

新增结论是固定 $a,\phi$ 下，整个未知 $M$ 具有同一个通常伴随解析半径，
以及 (5.1)–(5.7) 的真实局部流和闭像，而非仅每个固定阶分别有界。

必须保留以下范围：

- $U(z)$ 目前仅在这些已付解析向量上定义；不声称 $e^{zT^*}\in B(H)$。
- (5.6) 是包含关系，不未经证明宣称 $M_z$ 等于扰动算子的完整核。
- $G(z)$ 不必属于 $\{A\}'$，$M_z$ 不因此自动对原 $A$ 不变。
- 这只控制一个固定 first 方向的伴随幂；不控制整个 $\ell^2$ 方向球，不推出 Walsh 次数指数矩。
- 它不把点乘 $e^{v}$、或 Möbius 倾斜所需的点乘域自动加入 $M$。
- R236 高位反射附录现已给规范分支的全部有限闭像 $N_r=M$ 及中央耦合逆域 $D_H=\{0\}$；它们不是本稿正阶预算推出的。中央有核分支的真实根链和原规范危险 $+1$ 核仍待处理，本稿没有给中央逆的零阶范数界。

因此本结果可以作为实际通常伴随流的合法域工具；后续若要把该流识别为所需点乘或头图变换，仍须给出那个具体识别。
