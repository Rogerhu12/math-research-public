# R271 附录：归一创建行、无碰撞损失的原 primitive 构造与八分之十五次幂下界

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_2220。

状态：**已证明。** 本文在原无限正规尾中构造同一个单位 primitive 源，将[原真幂逆的四分之七次下界](R271-appendix-original-regular-tail-primitive-power-inverse-seven-fourths-lower-bound.md)提高到 $q^{15/8}$。新的源直接用真实删除的有限次导数构成，不使用低碰撞 canonical 塔。测试端使用范数恰为一的归一创建行及其准确变权单模，所以没有固定玻色权近似的碰撞损失。所有阶的真幂逆均有同源下界。该测试仍只读取真幂底项，不能据此宣称实际高出生修复费用很大。

## 1. 原参数与结论

固定 $m\ge5$ 和整数 $q\ge16m^2$。原尾为
$$
D_m=\sum_{j\ge m}a_jE_j,\qquad a_j=(j+1)^{-2}.
$$
记第 $q$ 孔层为 $\mathcal H_q^{(m)}$，$K_q^{(m)}=\ker D_m\cap\mathcal H_q^{(m)}$。以下先允许任意整数 $1\le k\le q$，置
$$
J=m+2q-k,\qquad S=S_J=\sum_{j\ge J}a_j^2,
\qquad \vartheta=S(m+k)^4.
\tag{1.1}
$$
将原尾分成最初 $k$ 个实际强位 $[m,m+k)$、中间 $q-k$ 个相邻暗对，以及完整无限远尾 $[J,\infty)$。没有删去中间位或远尾。

设 $e_r=e_r((a_j^2)_{j\ge J})$ 是远尾平方权的第 $r$ 个初等对称和，$e_0=1$。所有 $e_r$ 严格正且有限。本文构造一个明确单位向量 $f\in K_q^{(m)}$，使对每个整数 $h\ge1$，完整层的真正 MP 逆满足
$$
\boxed{
\left\|(D_m^h|_{\mathcal H_{q+h}^{(m)}})^\dagger f\right\|^2
\ge
\frac{e^{-\vartheta-4/(m+k+1)}}{(h!)^2}\frac{e_k}{e_{k+h}}
\ge
e^{-\vartheta-4/(m+k+1)}
\frac{(k+1)\cdots(k+h)}{(h!)^2 S^h}.
}
\tag{1.2}
$$
原固定有限孔层的满射性保证这里的 MP 逆有界。结论 (1.2) 针对同一个 $f$，不逐阶更换源。

特别取
$$
\boxed{k=\left\lfloor q^{3/4}/4\right\rfloor.}
\tag{1.3}
$$
此时
$$
\boxed{\|D_{m,q+1}^{\dagger}f\|\ge q^{15/8}.}
\tag{1.4}
$$
因此原整个 $K_q^{(m)}$ 上不能有统一的 $q^{15/8-\epsilon}$ 型单步原像上界，其中 $\epsilon>0$ 固定、$m$ 固定。后文也保留可直接使用的全参数式 (1.2)，而不只给指数。

## 2. 远尾的准确归一创建行

先只看远尾 $D_J$。在其第 $r$ 孔层定义单位创建向量
$$
u_r=e_r^{-1/2}\sum_{|I|=r}\left(\prod_{i\in I}a_i\right)|I\rangle,
\qquad u_0=\Omega_J.
\tag{2.1}
$$
级数由 $e_r<\infty$ 在 Hilbert 空间收敛。每个 $r$ 元集合在一次创建后恰出现 $r$ 次，所以
$$
D_J^*u_{r-1}=c_r u_r,\qquad
\boxed{c_r=r\sqrt{e_r/e_{r-1}}>0.}
\tag{2.2}
$$
定义分析行
$$
T_rv=\langle u_r,v\rangle\,\mathbf e_r.
$$
则 $\|T_r\|=1$，且对整个第 $r$ 孔层而不仅是创建像，有
$$
\boxed{T_{r-1}D_J=c_rT_r.}
\tag{2.3}
$$
这里 $\mathbf e_r$ 是一个标量序列空间的标准向量。式 (2.3) 使用真实变权 $c_r$；不把它换成 $\sqrt{rS}$。后者只是一个上界，因为
$$
(r+1)e_{r+1}
=\sum_{|I|=r}\left(\prod_{i\in I}a_i^2\right)
\sum_{j\notin I}a_j^2
\le S e_r.
\tag{2.4}
$$
特别 $c_r^2\le rS$。

下面还用到原删除的一个全层上界。对 $v\in\mathcal H_r^{(J)}$，每个 $(r-1)$ 元集合处作 Cauchy--Schwarz，再对这些集合求和，得到
$$
\|D_Jv\|^2
\le S\sum_{|L|=r-1}\sum_{i\notin L}|v_{L\cup\{i\}}|^2
=rS\|v\|^2.
$$
所以对 $0\le s\le k$，
$$
\boxed{\|D_J^s u_k\|^2\le\frac{k!}{(k-s)!}S^s.}
\tag{2.5}
$$
这只是有界删除的原 Hilbert 范数估计，不要求 $D_Ju_k$ 仍在创建直线上。

## 3. 直接构造原 primitive，支付全部源范数

用 $[k]$ 标记最初的 $k$ 个实际强位；其权仍写 $a_i$，并记
$a_I=\prod_{i\in I}a_i$。在强位和远尾上定义
$$
\boxed{
F_k=\sum_{I\subseteq[k]}
(-1)^{|I|}\frac{(k-|I|)!}{k!}\,a_I^{-1}
|I\rangle\otimes D_J^{|I|}u_k.
}
\tag{3.1}
$$
每项的总孔数都是 $k$。它是有限和，且各个强位标签互相正交。$I=\varnothing$ 项为 $u_k$，范数为一。

**准确 primitive 身份。** 令 $D_{\rm hd}=\sum_{i\in[k]}a_iE_i$。对 $|I|=s<k$，$(D_{\rm hd}+D_J)F_k$ 中标签 $|I\rangle$ 的系数为
$$
(-1)^s\frac{(k-s)!}{k!}a_I^{-1}D_J^{s+1}u_k
+(k-s)(-1)^{s+1}\frac{(k-s-1)!}{k!}a_I^{-1}D_J^{s+1}u_k=0.
$$
当 $s=k$，剩余项含 $D_J^{k+1}u_k=0$。因此
$$
\boxed{(D_{\rm hd}+D_J)F_k=0.}
\tag{3.2}
$$
这一步没有构造或假定任何 sequential canonical 提升。

由 (2.5) 及强位标签正交，
$$
\|F_k\|^2
\le\sum_{s=0}^k
\frac{S^s}{k!/(k-s)!}
e_s((a_i^{-2})_{i\in[k]}).
\tag{3.3}
$$
最初 $k$ 位均满足 $a_i^{-2}\le(m+k)^4$，故
$$
e_s((a_i^{-2})_{i\in[k]})
\le\binom ks(m+k)^{4s}.
$$
将 $\binom ks/[k!/(k-s)!]=1/s!$ 代入，得到
$$
\boxed{1\le\|F_k\|^2\le\sum_{s=0}^k\frac{\vartheta^s}{s!}
\le e^{\vartheta}.}
\tag{3.4}
$$
式 (3.4) 的指数没有额外的 $k$ 因子；分母中的准确下降阶乘支付了 $k$ 个强位的组合数。

在中间每个相邻权对 $(\alpha,\beta)$ 上，取单位暗向量
$$
h_{\alpha,\beta}
=\frac{\beta|10\rangle-\alpha|01\rangle}
{\sqrt{\alpha^2+\beta^2}}.
$$
它被该对的下降算子消去。全部 $q-k$ 个暗向量的张量积记作 $h_{\rm gap}$。于是
$$
\widetilde f=F_k\otimes h_{\rm gap}\in K_q^{(m)},
\qquad\boxed{f=\widetilde f/\|F_k\|.}
\tag{3.5}
$$
张量顺序按强位、中间位、远尾读取；(3.5) 的写法只压缩这个顺序。所有未选位都仍在原 Hilbert 空间中。

## 4. 全原空间到变权模型的有界分析

对一个暗对，记
$$
g_{\alpha,\beta}
=\frac{\alpha|10\rangle-\beta|01\rangle}
{\sqrt{\alpha^2+\beta^2}},\qquad
\rho=\frac{2\alpha\beta}{\alpha^2+\beta^2},
$$
$$
P_{\alpha,\beta}=|h_{\alpha,\beta}\rangle
\langle g_{\alpha,\beta}|/\rho,
$$
并在其余孔层上置零。直接代入给
$$
P^2=P,\qquad DP=PD=0,\qquad\|P\|=\rho^{-1}.
$$
这些正是[原两步费用稿 §2](R271-appendix-original-tail-cubic-sequential-power-gap-and-bare-two-jet-amplification.md)的实际斜投影。全部暗对的乘积满足
$$
\boxed{\|P_{\rm gap}\|\le R:=e^{2/(m+k+1)}.}
\tag{4.1}
$$
为直接核对常数：对从 $j$ 开始的一对，$\alpha=(j+1)^{-2},\beta=(j+2)^{-2}$，
$\rho^{-1}=\cosh(2\log(1+1/(j+1)))$。用
$\log\cosh x\le x^2/2$ 及 $\log(1+x)\le x$，其对数至多 $2/(j+1)^2$。对从 $j=m+k$ 开始、每隔两位的有限对求和，并延长为无穷和，有
$$
\sum_{\ell\ge0}\frac{2}{(m+k+2\ell+1)^2}
\le\frac2{(m+k+1)^2}+\frac1{m+k+1}
\le\frac2{m+k+1},
$$
最后一步用 $m+k+1\ge2$。因此得到 (4.1)。

先施加 $P_{\rm gap}$、识别单位暗张量因子，再在远尾每层使用 $T_r$，便在原第 $q+t$ 孔层得到分析算子 $\mathcal A_t$。其值域是模型总次数 $k+t$ 的空间，模型含相同的 $k$ 个强位和一个下降权为 $c_r$ 的标量模：
$$
\mathcal L=D_{\rm hd}+C,\qquad C\mathbf e_r=c_r\mathbf e_{r-1}.
$$
每个强位标签的分析行作用在正交分量上，所以
$$
\boxed{\|\mathcal A_t\|\le R,\qquad
\mathcal A_{t-1}D_m=\mathcal L\mathcal A_t.}
\tag{4.2}
$$
这里对 $t\ge0$ 均可读取，$t=0$ 的目标下降到模型次数 $k-1$；逐次分析任意 $h$ 步原像时则使用 $t=1,\ldots,h$。

式 (2.3) 和 $T_ku_k=\mathbf e_k$ 给
$$
\mathcal A_0\widetilde f=\omega_k,
$$
$$
\omega_k=
\sum_{I\subseteq[k]}(-1)^s\frac{(k-s)!}{k!}a_I^{-1}
\left(\prod_{r=k-s+1}^{k}c_r\right)
|I\rangle\otimes\mathbf e_{k-s},\qquad s=|I|.
\tag{4.3}
$$
空积按一读取。它是模型的一个 primitive，且其空强位分量恰为一。由于原源已经通过 (3.2) 完全构造好，不必从模型源反推一个未付费的原提升。

## 5. 所有真幂逆的同一个准确测试系数

模型次数 $k+t$ 在 $t\ge0$ 时恰有 $2^k$ 个强位标签，远尾次数由标签唯一决定。当 $t\ge1$ 时，$\mathcal L$ 从次数 $k+t$ 到次数 $k+t-1$ 是一个三角方阵，其对角为严格正的 $c_{k+t-|I|}$；故有唯一逆。

记 $C^{-1}\mathbf e_r=c_{r+1}^{-1}\mathbf e_{r+1}$。在这些有限次模型层上，$C^{-1}$ 与 $D_{\rm hd}$ 交换，而 $D_{\rm hd}^{k+1}=0$。因此从次数 $k$ 到次数 $k+h$，准确逆为有限负二项展开
$$
\boxed{
\mathcal L^{-h}
=\sum_{s=0}^{k}(-1)^s\binom{h+s-1}{s}
C^{-(h+s)}D_{\rm hd}^{s}.
}
\tag{5.1}
$$
可以逐个次数乘回 $\mathcal L$ 验证；标量模在相关输出层没有次数零的截断问题。

现取 $\mathcal L^{-h}\omega_k$ 的**空强位**坐标。对 $|I|=s$，恰由 (5.1) 的第 $s$ 项贡献，且
$D_{\rm hd}^{s}|I\rangle=s!a_I|\varnothing\rangle$。将 (4.3) 代入，所有正负号、强位权和 $c_k\cdots c_{k-s+1}$ 准确抵消。固定 $s$ 的 $\binom ks$ 项合计为
$$
\frac{\binom{h+s-1}{s}}{c_{k+1}\cdots c_{k+h}}.
$$
再用有限组合恒等式
$\sum_{s=0}^{k}\binom{h+s-1}{s}=\binom{h+k}{k}$，得到
$$
\boxed{
(\mathcal L^{-h}\omega_k)_{\varnothing}
=\frac{\binom{k+h}{k}}{c_{k+1}\cdots c_{k+h}}
=\frac1{h!}\sqrt{e_k/e_{k+h}}.
}
\tag{5.2}
$$
最后一个等式由 (2.2) 的乘积望远镜给出。特别 $h=1$ 时，该坐标是
$(k+1)/c_{k+1}$。

取任意实际原像 $v\in\mathcal H_{q+h}^{(m)}$、$D_m^hv=f$。由 (4.2)，
$$
\mathcal L^h\mathcal A_hv=\omega_k/\|F_k\|.
$$
模型真幂是上述可逆方阵，所以 (5.2) 给
$$
R\|v\|\ge\|\mathcal A_hv\|
\ge\frac1{\|F_k\|h!}\sqrt{e_k/e_{k+h}}.
$$
取所有原像中的最小值，再用 (3.4)、(4.1)，便得到 (1.2) 的第一式。迭代 (2.4) 给
$$
\frac{e_k}{e_{k+h}}
\ge\frac{(k+1)\cdots(k+h)}{S^h},
$$
从而完成 (1.2)。这里从未把模型的 MP 逆当成原最小逆；对任意原像使用同一个有界分析，才取得原空间下界。

## 6. 原八分之十五次幂的完整常数账本

取 (1.3)。由 $q\ge16m^2$，
$$
q^{3/4}/4\ge2m^{3/2},\qquad k\ge m,
\qquad k\le q/4,
\qquad k+1>q^{3/4}/4.
$$
于是
$$
J\ge7q/4,\qquad m+k\le2k\le q^{3/4}/2.
$$
原尾平方和满足
$$
S_J\le\int_J^\infty x^{-4}\,dx=\frac1{3J^3}.
$$
因此
$$
\vartheta\le\frac4{1029},\qquad
\vartheta+\frac4{m+k+1}
\le\frac4{1029}+\frac4{11}<\frac12<\log2.
\tag{6.1}
$$
在 (1.2) 取 $h=1$，得到
$$
\begin{aligned}
\|D_{m,q+1}^\dagger f\|^2
&\ge\frac{k+1}{2S_J}\\
&>\frac{q^{3/4}}8\,3\left(\frac{7q}{4}\right)^3
=\frac{1029}{512}q^{15/4}
>q^{15/4}.
\end{aligned}
$$
这证明 (1.4)。上述常数仍留有余量；无需为了指数结论优化 $k$。

## 7. 精确范围：仍不读取实际高返回

对于 $u\in\ker D_m^h\cap\mathcal H_{q+h}^{(m)}$，(4.2) 给
$\mathcal L^h\mathcal A_hu=0$。由于 §5 的模型方阵可逆，
$$
\boxed{\mathcal A_hu=0.}
\tag{7.1}
$$
所以本测试消去该物理输出层的整个真幂零空间。它读到的是[准确真幂底项分解](R271-appendix-exact-power-floor-and-two-filtered-primitive-bridges.md)中的真幂最小原像部分，不能检测与这些底项正交的出生一修正。

特别，(1.4) 不是 $S_H^\dagger\mathcal R\mathcal G^\dagger\zeta(r)$ 的下界；本文也没有证明 (3.5) 的 $f$ 来自原实际 $M$ 图或窄 Schur 来源。相邻 primitive Gram 比较、同源两费用比较、无权 $N=M$ 和普通 ISP 均不由本文得到。

新增的实质是：原源端的完全有限导数构造与测试端的准确变权归一创建行，允许 $k$ 从旧低碰撞窗口的 $\sqrt q$ 量级扩大到 $q^{3/4}$，而且全源和全层分析的费用均已在原 Hilbert 范数中支付。
