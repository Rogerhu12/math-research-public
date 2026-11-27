# 同一缺陷来源的指数 dyadic 图边界下界与弱核心预算

日期：2026-11-27（Asia/Taipei）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下两种实际模型的来源下界和弱核心充分条件已证明；没有证明真实 $W$ 的 $\Gamma$ 有限或边界费用上界，$N=M$ 仍未完成。**

本文接[实际除法闭关系](R271-appendix-actual-formal-division-closed-relation-and-two-range-cores.md)、[同一来源的两个准确 dyadic 边界](R271-appendix-exact-dyadic-division-graph-boundaries-and-cayley-cost.md)和[全实际核的占满前缀指数界](R271-appendix-full-tensor-exponential-bound-and-improved-occupied-prefix-decay.md)。旧 dyadic 稿给指定截断强收敛的准确判据；本文不改变该判据。新增的是：只要求一条子列的完整输出有界，便能用凸组合取得图核心；如果输出恰是真实缺陷向量，则其两笔同源边界费用必须具有显式正指数增长。

## 1. 同一个原最大图对

沿用原 $S=B^*$、$M=\ker T$、$N=\overline{BM}$、$W=M\ominus N$ 和 $G=G_0^*$。模型 $\bullet$ 可为 $N$ 或 $Y$；每处使用该模型自己的 $T,G$ 和边界行。

固定
$$
y\in\mathcal D(G),\qquad f=Gy\in\mathcal H.
$$
原域身份给 $T^*y=Sf$、$y_0=0$。令 $h$ 是唯一形式解 $Sh=y$，则 $T^*h=f$。不预设 $h\in\mathcal H$。

令 $Q_r$ 为占满低 $r$ 位的投影，$d=2^r$，并用旧稿同一记号
$$
h^{<r}=(I-Q_r)h,\qquad
SQ_rh=e_0\otimes y_r,\qquad
Q_rf=e_{d-1}\otimes f_r.
\tag{1.1}
$$
已经支付
$$
h^{<r}\in\mathcal H,\quad
\|h^{<r}\|\le\alpha_{r-1}^{-1}\|y\|,\quad
\|y_r\|\longrightarrow0,\quad \|f_r\|\longrightarrow0.
\tag{1.2}
$$
所有下文费用属于这个固定的 $h,y,f$。

记原真实有限头顶行为 $\mathcal H_r^{\bullet,[r]}(h)$，原完整低头向量为 $v_r^\bullet$，并置
$$
\lambda_r^\bullet=\|v_r^\bullet\|,\qquad
E_r^\bullet(h,f)=
\left[
(\lambda_r^\bullet)^2\|y_r\|^2+
\|\mathcal H_r^{\bullet,[r]}(h)-f_r\|^2
\right]^{1/2}.
\tag{1.3}
$$
旧稿的精确分解及全部 Y 逆费用给
$$
T_\bullet^*h^{<r}-f
=-v_r^\bullet\otimes y_r
+e_{d-1}\otimes
  [\mathcal H_r^{\bullet,[r]}(h)-f_r]
+\mathcal E_r^\bullet,
\tag{1.4}
$$
其中前两项正交，而且
$$
\mathcal E_r^N=0,\qquad
\|\mathcal E_r^Y\|
\le24e^{-760\,16^{r-1}}\|y\|.
\tag{1.5}
$$
这里的 $24$ 仅把旧稿 (4.3)、(4.4) 两个实际误差相加；没有删去任何 Cayley 逆或把它们换成纯尾。

## 2. 有界子列已足够给真正图核心

**命题 2.1。** 若同一最大图对满足
$$
\liminf_{r\to\infty}E_r^\bullet(h,f)<\infty,
\tag{2.1}
$$
则存在 $h_n\in\mathcal H$ 使
$$
Sh_n\longrightarrow y,\qquad
T_\bullet^*h_n\longrightarrow f.
\tag{2.2}
$$
特别，$y$ 属于 $S\mathcal H$ 生成的实际 $G$ 图核心，且 $f\in M^\perp$。

证明：取 $r_j\to\infty$ 使 (1.3) 一致有界。由 (1.4)--(1.5)，
$T^*h^{<r_j}$ 在 $\mathcal H$ 中一致有界。每个固定输出整数坐标的 $T^*$ 行只有有限前驱；当 $r_j$ 足够大时，$h^{<r_j}$ 与 $h$ 在全部这些前驱上一致。因此
$$
(T^*h^{<r_j})_n\longrightarrow f_n
\qquad(n\ge0).
$$
一致范数界与有限坐标向量的稠密性给
$$
T^*h^{<r_j}\rightharpoonup f.
\tag{2.3}
$$
同时 (1.2) 给 $Sh^{<r_j}\to y$ 强收敛。每个图对
$(Sh^{<r_j},T^*h^{<r_j})$ 均属于 $G|_{S\mathcal H}$ 的图。其图闭包是闭线性子空间，因而弱闭；故 $(y,f)$ 属于这个图闭包。

也可明确取逼近来源：对每个 $n$，取 (2.3) 的一个充分远有限凸组合，使输出距 $f$ 小于 $1/n$；由于输入已经强收敛，同一个凸组合的输入也可距 $y$ 小于 $1/n$。将相应的有限多个 $h^{<r_j}$ 作这个凸组合便得到 $h_n\in\mathcal H$。随后对每个 $h_n$ 作普通有限坐标逼近，因 $S,T^*$ 有界，仍保持 (2.2)。证毕。

这只把“某条指定截断本身强收敛”放宽成“其子列可经凸组合强收敛”。它没有断言一切图核心来源的原边界费用必须有界。

## 3. 两模型低边界均由末列主导

对 $r\ge2$ 置
$$
c_r=\frac{a_{r-1}}{\alpha_{r-1}}
=\frac1{r^2\alpha_{r-1}},\qquad
\beta_r=6r^2\eta_{r-2},\qquad
\eta_j=\frac{\alpha_{j+1}}{\alpha_j}.
\tag{3.1}
$$

**引理 3.1。** 原 N/Y 两模型均有
$$
v_r^\bullet=c_r e_{2^{r-1}-1}+u_r^\bullet,\qquad
\|u_r^\bullet\|\le\beta_r c_r,\qquad
\lambda_r^\bullet\ge(1-\beta_r)c_r.
\tag{3.2}
$$
而且 $0<\beta_r<1/2$。

N 型直接使用
$v_r^N=\sum_{i<r}(a_i/\alpha_i)e_{2^i-1}$。
去掉 $i=r-1$ 后，利用 $\sum_i a_i<2$、$\alpha_i\ge\alpha_{r-2}$，余向量范数至多 $2/\alpha_{r-2}$，小于 (3.2) 的统一上界。

Y 型使用原完整有限头向量
$v_r^Y=\sum_{i<r}a_i\ell_{ri}$。对末项 $i=r-1$，旧稿的
$L_{r,r-1}=2$，所以准确地
$$
\ell_{r,r-1}=\alpha_{r-1}^{-1}e_{2^{r-1}-1}.
$$
其余项的原有限头逆界为 $\|\ell_{ri}\|\le3/\alpha_i$，故它们的总范数不超过 $6/\alpha_{r-2}=\beta_rc_r$。允许这些向量相互重叠；这里没有错误地加它们的范数平方。三角不等式给 $\lambda_r^\bullet$ 的下界。

最后，$\eta_{j+1}\le\eta_j/4$ 给
$\beta_{r+1}/\beta_r\le9/16$；而
$\beta_2=24\eta_0<24/64<1/2$。证毕。

## 4. 原核投影对两条边界的实际衰减

记
$$
\gamma_{\rm ex}=\log2+\operatorname{arsinh}1+
\frac25\left(1-\frac1{\sqrt2}\right)>\frac53,
$$
$$
\delta_n=
\min\left\{1,\ 
e^{-\gamma_{\rm ex}n+4(\log n+1)^2}+e^{-47n^4}
\right\}\quad(n\ge2).
\tag{4.1}
$$
已发布的全核前缀界及取伴随给
$$
\|Q_nP_M\|=\|P_MQ_n\|\le\delta_n.
\tag{4.2}
$$
对 $r\ge3$ 定义
$$
A_r=\frac{\delta_{r-1}+\beta_r}{1-\beta_r}.
\tag{4.3}
$$

由 (3.2)，末列 $e_{2^{r-1}-1}\otimes z$ 属于占满低 $r-1$ 位的空间；余列用普通算子范数即可。因此对每个真实尾向量 $z$，
$$
\boxed{
\|P_M(v_r^\bullet\otimes z)\|
\le A_r\lambda_r^\bullet\|z\|.
}
\tag{4.4}
$$
同样，
$$
\|P_M(e_{2^r-1}\otimes z)\|\le\delta_r\|z\|.
\tag{4.5}
$$
这两条保留全部尾向量和 primitive，不把一列或高孔来源缩成标量真空。

## 5. 真正缺陷输出迫使同源费用指数增长

现在额外要求 $f=w\in M$。原域身份同时给
$Sw=T^*y\in M^\perp$，故 $w\in N^\perp$，即 $w\in W$。反过来，对于已付 $\Gamma(u)<\infty$ 的 $w=Ju\in W$，规范来源正好给这个最大图对 $y=Sh(w)$、$Gy=w$。因此本节始终处理真正同一 $W$ 来源。

由于 $T^*h^{<r}\in M^\perp$，把 (1.4) 投到 $M$，再用 (4.4)--(4.5)，得到
$$
\boxed{
\begin{aligned}
\|w\|\le {}&
A_r\lambda_r^\bullet\|y_r\|
+\delta_r\|\mathcal H_r^{\bullet,[r]}(h)-w_r\|\\
&+24e^{-760\,16^{r-1}}\|y\|.
\end{aligned}
}
\tag{5.1}
$$
N 型的最后一项可以删除。这不是一般最大图来源的上界，而是利用 $w\in M$ 得到的同源下界。

由 Cauchy--Schwarz，
$$
\boxed{
E_r^\bullet(h,w)
\ge
\frac{\bigl(\|w\|-24e^{-760\,16^{r-1}}\|y\|\bigr)_+}
{\sqrt{A_r^2+\delta_r^2}}.
}
\tag{5.2}
$$

给一个明确的指数版本。对 $0<\gamma<\gamma_{\rm ex}$，沿用已发布
$$
C_\gamma=2e^{\gamma N_\gamma},\qquad
N_\gamma=\left\lceil\frac{256}{(\gamma_{\rm ex}-\gamma)^2}\right\rceil,
$$
于是 $\delta_n\le C_\gamma e^{-\gamma n}$。
又 $\eta_{r-2}\le e^{-770\cdot16^{r-2}}$、
$16^{r-2}\ge r-1$ 和 $6r^2\le24^{r-1}$ 给
$\beta_r\le e^{-2(r-1)}$。
因为 $\gamma<\gamma_{\rm ex}<2$，有
$$
\sqrt{A_r^2+\delta_r^2}
\le D_\gamma e^{-\gamma r},\qquad
D_\gamma=
\sqrt{4e^{2\gamma}(C_\gamma+1)^2+C_\gamma^2}.
\tag{5.3}
$$
这里使用 $1-\beta_r>1/2$。若 $w\ne0$，则对全部充分大的 $r$，
$$
\boxed{
E_r^\bullet(h,w)\ge
\frac{\|w\|}{2D_\gamma}e^{\gamma r}.
}
\tag{5.4}
$$
等价地，
$$
\boxed{
\liminf_{r\to\infty}\frac1r\log E_r^\bullet(h,w)
\ge\gamma_{\rm ex}>\frac53.
}
\tag{5.5}
$$
这个下界是对所有充分大的实际 $r$，而非只选出一个坏子列。精确形式 (5.2) 还保留了 $\gamma_{\rm ex}$ 处的 $O((\log r)^2)$ 修正。

由于 $w\perp T^*h^{<r}$，另有
$$
\|T^*h^{<r}-w\|^2
=\|T^*h^{<r}\|^2+\|w\|^2.
\tag{5.6}
$$
结合 (1.4)--(1.5)，同样的下指数率也适用于
$\|T^*h^{<r}\|$。因此这里不是允许两笔误差在最终输出中相消的粗费用下界；两个主边界本来正交，输出对 $w$ 的正交性也被保留。

## 5.1 同一个最大图来源的范围判据

前面的投影论证实际上还保留了一个稍强的范围版本。对 §1 的任意最大图对，域身份已给 $f\in N^\perp$，所以
$$
P_Mf=P_Wf.
$$
直接将 (1.4) 投到 $M$，得到
$$
\boxed{
\|P_Wf\|
\le A_r\lambda_r^\bullet\|y_r\|
+\delta_r\|\mathcal H_r^{\bullet,[r]}(h)-f_r\|
+24e^{-760\,16^{r-1}}\|y\|.
}
\tag{5.7}
$$
因此只要 $P_Wf\ne0$，(5.2)--(5.5) 的来源 $h,y,f$ 原样保留，只把分子中的 $\|w\|$ 换成 $\|P_Wf\|$；不把 $h$ 偷换成 $P_Wf$ 的规范原像。

特别，若同一个最大图对存在 $r_j\to\infty$ 和 $0<\gamma<\gamma_{\rm ex}$ 使
$$
e^{-\gamma r_j}E_{r_j}^\bullet(h,f)\longrightarrow0,
\tag{5.8}
$$
则 $P_Wf=0$，进而 $f\in M^\perp=\mathcal I$。这直接给第一道闭包范围核心的一个来源扇区。它只证明这个输出属于 $\mathcal I$，不把 (5.8) 擅自称为 $y$ 的图核心判据；§2 的有界子列才另行支付了输入和输出同时的图逼近。

## 6. 仍未支付的范围

对非零 $w=Ju\in W$，目前得到的是精确二分：

- 若 $\Gamma(u)=+\infty$，则规范 $Sh(w)$ 尚不在实际 Hilbert 图域。
- 若 $\Gamma(u)<\infty$，则同一个原 $h(w),Sh(w),w$ 的 (1.3) 必须满足 (5.2)--(5.5)。

特别，若以后对同一 $w$ 支付了 $\Gamma(u)<\infty$，并找到 $r_j\to\infty$ 和某个 $0<\gamma<\gamma_{\rm ex}$ 使
$e^{-\gamma r_j}E_{r_j}^\bullet(h,w)\to0$，则 (5.1) 立即推出 $w=0$。本文没有给出这个来源上界，也没有用普通 $Sh\in\mathcal H$ 代替原 $15/16$ 核心所需的输出逆权。两道闭包范围核心及 $N=M$ 仍开。
