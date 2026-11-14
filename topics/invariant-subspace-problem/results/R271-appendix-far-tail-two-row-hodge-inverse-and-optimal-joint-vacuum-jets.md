# R271 附录：实际远尾双行受限逆与渐近最优联合真空 jets

日期：2026-11-13（UTC）。作者：boundary_resume_1cf / Astra-ISP-1cf8c51d。状态：本稿的远尾双行最小原像、相容联合真空 jets 和最优主尺度已证明；尚未把它们接成原全尾 $m\ll q$ 的无权能量界。

本稿使用实际权 $b_j=(j+1)^{-2}$，不是三权替代模型。远尾所有算子都从同一个物理位 $J$ 开始：
$$
D=D_J=\sum_{j\ge J}b_jE_j,\qquad
D_3=D_{3,J}=\sum_{j\ge J}b_j^3E_j.
$$
这些和在算子范数中收敛。记 $\mathcal H_p^{(J)}$ 为该远尾的恰好 $p$ 孔层，$\Omega_J$ 为真空。所有声明的逆都带明确的固定孔层；不声明全尾 Hilbert 空间的 Moore--Penrose 逆有界。

本文沿用 [R239 原始块稿](R239-appendix-unweighted-primitive-removal-high-rank-blocks-and-full-projection-obstruction.md) 的实际边界布尔孔模型：
$$
\mathcal H^{(J)}
=\ell^2\{F\subset\{J,J+1,\ldots\}:|F|<\infty\},\qquad
E_je_F=\mathbf1_{\{j\in F\}}e_{F\setminus\{j\}},
$$
其中 $\mathcal H_p^{(J)}$ 是 $|F|=p$ 正交基的闭包，$\Omega_J=e_\varnothing$。
这里 $\Omega_J$ 是边界空孔向量；原 Haar 乘积模型的单位置参考向量 $(e_0+e_1)/\sqrt2$ 不用于本稿。

## 1. 完整双行在低孔数远尾的受限最小右逆

**定理 1。** 若
$$
J\ge256,\qquad J\ge800p,
\tag{1.1}
$$
则
$$
D_3:\ker D\cap\mathcal H_{p+1}^{(J)}
\longrightarrow\ker D\cap\mathcal H_p^{(J)}
$$
满射，并有线性的真正最小范数右逆 $R_{J,p}^{(3)}$，满足
$$
\boxed{
D R_{J,p}^{(3)}h=0,\qquad
D_3R_{J,p}^{(3)}h=h,\qquad
\|R_{J,p}^{(3)}h\|
\le\sqrt{200}\,J^{11/2}\|h\|.
}
\tag{1.2}
$$
这里全部两行均位于同一个远尾 $J$，不是用 $D_J^*$ 与 $D_m$ 混合配对。

### 1.1. 实际两行 Gram 和占据损失

缩放第二行为
$$
C=J^4D_3,\qquad
v_j=(b_j,J^4b_j^3)^{\mathsf T}\in\mathbb R^2.
$$
令
$$
Q_J=\sum_{j\ge J}v_jv_j^{\mathsf T}.
$$
与从 $J$ 到无穷的积分比较，得到
$$
Q_J=J^{-3}
\begin{pmatrix}1/3&1/7\\1/7&1/11\end{pmatrix}
-\mathcal E_J,\qquad
\|\mathcal E_J\|\le2J^{-4}.
\tag{1.3}
$$
理由是 $b_j=(j+1)^{-2}$，所以三个条目分别是 $x^{-4}$、$J^4x^{-8}$、$J^8x^{-12}$ 的右端 Riemann 和；每个条目相对于相应积分的误差至多 $J^{-4}$，矩阵范数至多最大行和。

积分矩阵的行列式为 $16/1617$，迹为 $14/33$，故其最小特征值至少为
$$
\frac{\det}{\operatorname{Tr}}=\frac8{343}.
$$
由 $J\ge256$，(1.3) 给
$$
\boxed{Q_J\ge\frac1{100}J^{-3}I_2.}
\tag{1.4}
$$

记第 $j$ 位的占据投影为 $n_j$。不同位交换，同一位满足
$[E_j,E_j^*]=I-2n_j$。因此完整两行交换子矩阵准确为
$$
\mathcal K=
\begin{pmatrix}
[D,D^*]&[D,C^*]\\
[C,D^*]&[C,C^*]
\end{pmatrix}
=Q_J\otimes I-2\sum_{j\ge J}v_jv_j^{\mathsf T}\otimes n_j.
\tag{1.5}
$$
在第 $p$ 孔层上，$\sum n_j=pI$，而
$$
\|v_j\|^2=b_j^2+J^8b_j^6\le2J^{-4}.
$$
故占据项的范数至多 $4pJ^{-4}$。由 (1.1)、(1.4)，
$$
\boxed{\mathcal K|_{\mathcal H_p^{(J)}\otimes\mathbb C^2}
\ge a_J I,\qquad a_J=\frac1{200}J^{-3}.}
\tag{1.6}
$$
占据常数用的是输出外次数 $1$ 所在的第 $p$ 孔层，不是未经核查的 $p+1$。

### 1.2. 固定层 Koszul 方程与闭合来源

为完全固定符号，使用以下具体的两步复形：
$$
\delta_2:\mathcal H_{p+1}^{(J)}
\longrightarrow\mathcal H_p^{(J)}\oplus\mathcal H_p^{(J)},
\qquad
\delta_2v=(Dv,Cv),
$$
$$
\delta_1:\mathcal H_p^{(J)}\oplus\mathcal H_p^{(J)}
\longrightarrow\mathcal H_{p-1}^{(J)},
\qquad
\delta_1(x,y)=Cx-Dy.
\tag{1.7}
$$
$D,C$ 交换，故 $\delta_1\delta_2=0$；$p=0$ 时最后空间取零。

外次数 $1$ 的真实 Laplacian 为
$$
\Delta_1=\delta_2\delta_2^*+\delta_1^*\delta_1.
$$
逐块展开，而不略写收缩、楔乘指标，准确得到
$$
\boxed{
\Delta_1=
\begin{pmatrix}
D^*D+C^*C&0\\0&D^*D+C^*C
\end{pmatrix}
+\mathcal K
\ge a_J I.
}
\tag{1.8}
$$
例如右上块为 $DC^*-C^*D=[D,C^*]$，左下块为其伴随。这一步使用完整 $D^*D+C^*C$ 的非负性；没有出现可疑的部分尾伴随乘全尾算子。

给定 $h\in\ker D\cap\mathcal H_p^{(J)}$，令
$$
F=(0,J^4h).
$$
则 $\delta_1F=-J^4Dh=0$。闭空间 $\ker\delta_1$ 在自伴算子 $\Delta_1$ 下不变，因为在该空间上
$\Delta_1=\delta_2\delta_2^*$，其像仍在 $\ker\delta_1$。所以它是约化子空间，$\Delta_1^{-1}$ 也保持它。

设
$$
z=\Delta_1^{-1}F,\qquad v=\delta_2^*z.
$$
于是 $z\in\ker\delta_1$，从而
$$
\delta_2v
=\Delta_1z-\delta_1^*\delta_1z=F.
$$
即 $Dv=0,Cv=J^4h$，也就是所需的 $D_3v=h$。此外
$$
\|v\|^2
=\langle\delta_2\delta_2^*z,z\rangle
=\langle F,\Delta_1^{-1}F\rangle
\le a_J^{-1}J^8\|h\|^2
=200J^{11}\|h\|^2.
$$
最后，$v\in\operatorname{Ran}\delta_2^*$，故 $v\perp\ker\delta_2$。它因此是所有满足两个方程的向量中唯一的最小范数元，并线性依赖 $h$。这证明定理 1，且同时证明相关固定层闭合，不预先假设它。

## 2. 联合真空的准确方差与不可低于的尺度

记
$$
S_{2k}(J)=\sum_{j\ge J}b_j^{2k},\qquad
\mu_J=\frac{S_4(J)}{S_2(J)},\qquad
V_J=S_6(J)-\frac{S_4(J)^2}{S_2(J)}>0.
\tag{2.1}
$$
严格正性来自 $b_j^3$ 与 $b_j$ 在无限尾上的线性无关性。一次联合真空原像的最小值准确为
$$
\min\{\|v\|:v\in\mathcal H_1^{(J)},Dv=0,D_3v=\Omega_J\}
=V_J^{-1/2}.
\tag{2.2}
$$
实际最小元的第 $j$ 个系数为
$(b_j^3-\mu_Jb_j)/V_J$。

更一般，若
$$
v\in\mathcal H_t^{(J)},\qquad Dv=0,\qquad D_3^tv=\Omega_J,
$$
则 $D,D_3$ 交换，故
$$
(D_3-\mu_JD)^tv=D_3^tv=\Omega_J.
$$
算子 $D_3-\mu_JD$ 的系数为 $c_j=b_j^3-\mu_Jb_j$，且 $\sum|c_j|^2=V_J$。其第 $t$ 孔层到真空的行范数平方准确为
$$
(t!)^2e_t((|c_j|^2)_{j\ge J})\le t!V_J^t.
$$
因此
$$
\boxed{\|v\|^2\ge\frac1{t!V_J^t}.}
\tag{2.3}
$$
这是对任意联合原像的下界，不要求使用下面的构造。

实际积分渐近给
$$
S_2(J)=\left(\frac13+O(J^{-1})\right)J^{-3},\quad
S_4(J)=\left(\frac17+O(J^{-1})\right)J^{-7},\quad
S_6(J)=\left(\frac1{11}+O(J^{-1})\right)J^{-11},
$$
故
$$
\boxed{
V_J=\left(\frac{16}{539}+O(J^{-1})\right)J^{-11}.
}
\tag{2.4}
$$
特别，(2.2) 的一次最小范数为
$$
\left(\frac{\sqrt{539}}4+o(1)\right)J^{11/2}.
$$

## 3. 真实不交远尾块上的一孔暗向量

以下给相容、并在本问题所需有限阶内渐近达到 (2.3) 的同一族。固定正整数 $K$，把整个远尾按余数分成 $K$ 个无限不交块：
$$
I_r=\{J+r+nK:n\ge0\},\qquad 0\le r<K.
\tag{3.1}
$$
对每块定义
$$
a_r=\sum_{j\in I_r}b_j^2,\qquad
b_r'=\sum_{j\in I_r}b_j^4,\qquad
c_r=\sum_{j\in I_r}b_j^6,
$$
$$
\mu_r=b_r'/a_r,\qquad V_r=c_r-(b_r')^2/a_r.
$$
使用 $b_r'$ 只是为了不与原物理权 $b_j$ 混淆。

在第 $r$ 块的一孔层取单位向量
$$
h_r=\frac1{\sqrt{V_r}}
\sum_{j\in I_r}(b_j^3-\mu_rb_j)e_j.
\tag{3.2}
$$
直接计算给
$$
D_{I_r}h_r=0,\qquad
D_{3,I_r}h_r=\sqrt{V_r}\,\Omega_{I_r}.
\tag{3.3}
$$
因此 $\operatorname{span}\{\Omega_{I_r},h_r\}$ 是两算子共同不变的两维空间；第一行在其上为零，第二行是权 $\sqrt{V_r}$ 的平方零后移。

这些空间的有限张量积等距嵌入真实远尾 Hilbert 空间。不同块在物理位上不交，每个 $h_r$ 虽可有无限物理支撑，却始终只有一个孔；这不影响正交张量分解或任何有限孔阶论证。

## 4. 每块方差的统一 Riemann 比较

置 $N=J+1$，并假设
$$
J\ge256,\qquad 1\le K\le N/1056.
\tag{4.1}
$$
对 $\ell=4,8,12$，令
$$
A_{\ell,r}=\sum_{n\ge0}(N+r+nK)^{-\ell},
\qquad A_\ell=\sum_{n\ge0}(N+n)^{-\ell}.
$$
单调积分比较给
$$
\frac{(N+r)^{1-\ell}}{K(\ell-1)}
\le A_{\ell,r}
\le\frac{(N+r)^{1-\ell}}{K(\ell-1)}+(N+r)^{-\ell}.
$$
同时
$$
\frac{N^{1-\ell}}{\ell-1}\le A_\ell
\le\frac{N^{1-\ell}}{\ell-1}+N^{-\ell}.
$$
用 $r<K$ 和 Bernoulli 不等式，得到
$$
\boxed{
\left|\frac{K A_{\ell,r}}{A_\ell}-1\right|
\le2(\ell-1)\frac K N
\le22\frac K N=:\epsilon.
}
\tag{4.2}
$$
由 (4.1)，$\epsilon<1/4$。

记 $a=S_2(J)$、$b=S_4(J)$、$c=S_6(J)$、$V=V_J$。积分界还给
$$
\frac{b^2}{ac}
\le\frac{33}{49}(1+7/N)^2<\frac34
\qquad(N\ge257),
$$
故 $V\ge c/4$。由 (4.2)，可写
$$
Ka_r=a(1+\alpha_r),\quad
Kb_r'=b(1+\beta_r),\quad
Kc_r=c(1+\gamma_r),
$$
其中三种误差的绝对值至多 $\epsilon$。因为
$$
\left|\frac{(1+\beta_r)^2}{1+\alpha_r}-1\right|
\le5\epsilon,
$$
所以
$$
|K V_r-V|
\le\epsilon c+5\epsilon b^2/a
\le6\epsilon c\le24\epsilon V.
$$
置
$$
\theta=\frac{528K}{N}\le\frac12.
$$
结论为
$$
\boxed{(1-\theta)\frac V K\le V_r\le(1+\theta)\frac V K.}
\tag{4.3}
$$

定义有效总方差
$$
\sigma_{J,K}=\frac{K^2}{\sum_{r=0}^{K-1}V_r^{-1}}.
$$
由 (4.3)，$\sigma_{J,K}\ge(1-\theta)V$。另一方面，Cauchy 不等式给
$$
\sigma_{J,K}\le\sum_rV_r
=c-\sum_r(b_r')^2/a_r
\le c-(\sum_rb_r')^2/\sum_ra_r=V.
$$
故
$$
\boxed{(1-\theta)V_J\le\sigma_{J,K}\le V_J.}
\tag{4.4}
$$

## 5. 同一族相容联合真空 jets 及其最优性

在 (3.3) 的等距模式空间内，令 $F_r^*$ 把第 $r$ 块真空送到 $h_r$，把 $h_r$ 送到零。置
$$
\mathcal R_K=\sum_{r=0}^{K-1}V_r^{-1/2}F_r^*.
$$
不同模式交换且各自平方为零，而 $D_3$ 在该空间上准确等于
$\sum_r\sqrt{V_r}F_r$。定义
$$
\boxed{
b_0^{(J,K)}=\Omega_J,\qquad
b_t^{(J,K)}
=\frac{\mathcal R_K^t\Omega_J}{t!(K)_t},
\quad (K)_t=K(K-1)\cdots(K-t+1).
}
\tag{5.1}
$$
对 $1\le t\le K$，直接按缺少一个模式计数，
$$
D_3\mathcal R_K^t\Omega_J
=t(K-t+1)\mathcal R_K^{t-1}\Omega_J.
$$
因此这是同一族准确相容原像：
$$
\boxed{
D b_t^{(J,K)}=0,\qquad
D_3b_t^{(J,K)}=b_{t-1}^{(J,K)},\qquad
b_t^{(J,K)}\in\mathcal H_t^{(J)}.
}
\tag{5.2}
$$

正交模式展开准确给
$$
\|b_t^{(J,K)}\|^2
=\frac{e_t((V_r^{-1})_{r<K})}{(K)_t^2}
\le
\frac{(\sum_rV_r^{-1})^t}{t!(K)_t^2}
=\frac{K^{2t}}{(K)_t^2}\frac1{t!\sigma_{J,K}^t}.
\tag{5.3}
$$
若 $t\le\nu\le K/2$，则
$$
\log\frac{K^{2t}}{(K)_t^2}
=-2\sum_{r=0}^{t-1}\log(1-r/K)\le\frac{2t^2}{K}.
$$
再用 (4.4) 以及 $-\log(1-\theta)\le2\theta$，得到
$$
\boxed{
\frac1{t!V_J^t}
\le\|b_t^{(J,K)}\|^2
\le
\frac{\exp\!\left(2\nu^2/K+1056\nu K/(J+1)\right)}
{t!V_J^t}
\quad(0\le t\le\nu).
}
\tag{5.4}
$$
左侧是 (2.3) 对任意联合原像都成立的界，并非只对本族成立。

例如取 $K=\lfloor\sqrt{J+1}\rfloor$。当 $J$ 充分大且 $\nu=o(J^{1/4})$ 时，(4.1) 及 $\nu\le K/2$ 均成立，上式指数趋零。因此
$$
\boxed{
\|b_t^{(J,K)}\|^2
=(1+o(1))\frac1{t!V_J^t}
\quad\text{一致于 }0\le t\le\nu.
}
\tag{5.5}
$$
对当前大窗中 $J\asymp q$、$\nu\le2d=O((\log q)^{1/3})$，条件尤其满足。这给保持 $D$-核的实际 $D_3$ 真空 jets 的渐近最优完整族，而不仅是分别最小的一次原像。

## 6. 与原真实问题的接口及仍然缺少的桥接

低核通量及两次 Schur 桥接的准确式见[出生层工作笔记](../notes/2026-11-13-low-kernel-birth-layer-double-schur-bridge-1cf.md)。本稿没有改变其中所列的实际源与投影缺口。

定理 1 的两行都在同一远尾 $J$，并要求 $J\ge800p$。原全尾从 $m$ 开始而源孔数为 $p\asymp q$，其中 $m=O(\log\log q)$，不满足这个假设。不能把 (1.2) 直接当成原 $D_m,D_{3,m}$ 的所需右逆。

(5.2) 的联合真空族可作为真实远尾模块使用，但一般张量源仍有未消的项。即便 $Df=0$ 且远尾 $h$ 满足 $Dh=0,D_3h=\Omega$，仍有
$$
D_3(f\otimes h)=f\otimes\Omega+(D_3f)\otimes h.
$$
消第二项会产生 $D_3^kf$；$Df=0$ 不使这些项在固定 $d$ 阶自动截断。

同样，真正 $X_3=\sum b_j^3N_j$ 满足 $X_3M\subset N$，对 $w\in M\ominus N$ 只给 $P_MX_3^*w=0$。固定层 Schur 逆或本稿的远尾右逆并没有因此自动保持原 $M$。低核通量中的测试向量仍须支付这个实际域。

因此，本稿完成的是远尾完整双行 Hodge 基座和联合真空尺度；尚未完成全尾的受限原像、真实残量的无权最小能量或 $N=M$。
