# 平衡 star 共同矩阵的唯一负方向及显式正补偿

本稿证明平衡 star 的一个此前未支付的完整源结构：若小组总长度 \(Q>1\)，真实自伴矩阵
\[
\widehat K=Z^{1/2}(\mathsf G-nm^*)Z^{-1/2}
\]
恰有一个负特征值，其余全部严格为正。证明保留同一原积分 Gram、全部 binomial 噪声和明确的秩一补偿，不把 \(\widehat K\) 当作任意自伴矩阵。

结果不等于相位界；它把下一步的共同 Schur 明确限制到唯一的真实负方向。所有方差估计均在正文自足证明。

## 1. 原同源量和精确自伴化

沿用[平衡 star 完整概率稿](2026-11-14-balanced-star-full-source-beta-binomial-phase-transport-789f-next.md)的量：
\[
F(t)=\prod_i(1-t+z_it)^{q_i},\qquad
\rho=F/\int_0^1F,\qquad Q=\sum_iq_i,\qquad q_i\ge1,\ z_i>0,
\]
\[
p_i(t)=\frac{z_it}{1-t+z_it},\qquad
m=\mathbb E_\rho p,\qquad n=\mathbf1-m,\qquad
Z=\operatorname{diag}(z_i).
\]
实际归一第一 Gram 是
\[
\mathsf G=\operatorname{Cov}_\rho(p)
+\operatorname{diag}\!\left(
\frac{\mathbb E_\rho p_i(1-p_i)}{q_i}
\right)>0.
\]
这里全部期望属于同一实际测度。

记
\[
a(t)=t(1-t),\qquad
f_i(t)=\frac{\sqrt{z_i}}{1-t+z_it},
\]
\[
W=\mathbb E_\rho[a f f^*],\qquad
D=\operatorname{diag}(W_{ii}/q_i)>0. \tag{1.1}
\]
因 \(a f_i^2=p_i(1-p_i)\)，这个 \(D\) 正是原条件 binomial 噪声。

准确有
\[
\boxed{
\widehat K
:=Z^{1/2}(\mathsf G-nm^*)Z^{-1/2}
=D-W.
} \tag{1.2}
\]
对 \(i\ne j\)，左边的元为
\[
\sqrt{\frac{z_i}{z_j}}\,
\left(\mathbb E p_ip_j-m_im_j-(1-m_i)m_j\right)
=-\sqrt{\frac{z_i}{z_j}}\,
\mathbb E[(1-p_i)p_j]
=-W_{ij}.
\]
对角则为
\[
\operatorname{Var}(p_i)+W_{ii}/q_i-m_i(1-m_i)
=W_{ii}/q_i-W_{ii}.
\]
故 (1.2) 是完整自伴身份，不需额外假设。

同一 source 的两侧度量还准确为
\[
\mathsf H
=Z^{1/2}\left(\operatorname{diag}(n_i/q_i)-\widehat K\right)Z^{1/2},
\]
\[
\mathsf L
=Z^{-1/2}\left(\operatorname{diag}(m_i/q_i)-\widehat K\right)Z^{-1/2}. \tag{1.3}
\]
这些式子说明本稿控制的正是原非交换相位中的共同矩阵。

## 2. 一个自足的一维加权方差引理

令 \(\omega(t)>0\) 是 \((0,1)\) 上概率密度，在两端按正倍数的一次幂消失，写
\[
\omega=e^{-V}/\int e^{-V},\qquad V''>0.
\]
对闭区间上光滑有界函数 \(\varphi\)，有
\[
\boxed{
\operatorname{Var}_\omega(\varphi)
\le
\mathbb E_\omega\frac{|\varphi'|^2}{V''}.
} \tag{2.1}
\]

证明如下。可先取实函数，令
\(g=\varphi-\mathbb E_\omega\varphi\)，定义
\[
u(t)=\frac1{\omega(t)}\int_0^t g(r)\omega(r)\,dr.
\]
由 \(\int g\omega=0\) 及端点的一次消失，\(u=O(t)\) 于 \(0\)，
\(u=O(1-t)\) 于 \(1\)。又
\[
g=u'-V'u.
\]
积分分部，所有边界项消失，给出完整平方
\[
\mathbb E_\omega g^2
=\mathbb E_\omega\bigl((u')^2+V''u^2\bigr). \tag{2.2}
\]
另一方面
\[
\mathbb E_\omega g^2
=\int\varphi(u\omega)'
=-\mathbb E_\omega[u\varphi'].
\]
用带权 Cauchy–Schwarz 和 (2.2)，
\[
(\mathbb E g^2)^2
\le\mathbb E(V''u^2)\,
\mathbb E\frac{(\varphi')^2}{V''}
\le\mathbb E g^2\,
\mathbb E\frac{(\varphi')^2}{V''}.
\]
约去非零方差即得 (2.1)；零方差显然成立。复函数分实虚部即可。本文只对以下明确光滑密度使用该引理，因此不需要其它端点正则性推广。

## 3. 同一加权测度中的严格矩阵预算

令
\[
A=\mathbb E_\rho a>0,\qquad
\omega(t)=\frac{a(t)\rho(t)}A.
\]
它在两端按一次幂消失。其势满足
\[
\boxed{
V''(t)=\frac1{t^2}+\frac1{(1-t)^2}+\kappa_F(t),
\qquad
\kappa_F(t)=\sum_i\frac{q_i(z_i-1)^2}{(1-t+z_it)^2}.
} \tag{3.1}
\]
定义明确的标量
\[
\boxed{
\theta=\max_{0\le t\le1}
\frac{\kappa_F(t)}
{\kappa_F(t)+t^{-2}+(1-t)^{-2}}
<1,
} \tag{3.2}
\]
在两端取连续值 \(0\)。严格小于 \(1\) 来自闭区间紧性、所有权严格正，以及分母中的两个严格正端点曲率项。若全部 \(z_i=1\)，则 \(\theta=0\)。

对任意系数列 \(c\)，令 \(\varphi=c^*f\)。因为
\[
f_i'=-\frac{z_i-1}{1-t+z_it}f_i,
\]
逐点 Cauchy–Schwarz 给
\[
|\varphi'|^2
\le
\kappa_F(t)\sum_i\frac{|c_i|^2f_i(t)^2}{q_i}.
\]
代入 (2.1) 得
\[
\operatorname{Cov}_\omega(f)
\preceq
\theta\,\operatorname{diag}
\left(\frac{\mathbb E_\omega f_i^2}{q_i}\right).
\]
令
\[
w=\mathbb E_\rho[a f].
\]
乘回 \(A\)，得到完整同源矩阵界
\[
\boxed{
W-\frac{ww^*}{A}\preceq\theta D.
} \tag{3.3}
\]
从而
\[
\boxed{
P:=D-W+\frac{ww^*}{A}
\succeq(1-\theta)D\succ0.
} \tag{3.4}
\]
这是实际积分 Gram 的明确正补偿；还可给一个与权值大小一致的显式 gap。
令
\[
Q_+=\sum_{z_i>1}q_i,\qquad Q_-=\sum_{z_i<1}q_i,\qquad
M_{\pm}=\max(Q_+,Q_-).
\]
当 \(z_i>1\) 时，
\[
\frac{(z_i-1)^2}{(1-t+z_it)^2}\le t^{-2};
\]
当 \(z_i<1\) 时，对应量不超过 \((1-t)^{-2}\)。
因此逐点有
\[
\kappa_F(t)\le \frac{Q_+}{t^2}+\frac{Q_-}{(1-t)^2}
\le M_{\pm}\left(t^{-2}+(1-t)^{-2}\right).
\]
代入 (3.2)–(3.4)，得到权值一致的完整矩阵预算
\[
\boxed{
\theta\le\frac{M_{\pm}}{M_{\pm}+1}\le\frac Q{Q+1},
\qquad
P\succeq\frac{D}{M_{\pm}+1}\succeq\frac{D}{Q+1}.
} \tag{3.5}
\]
全部 \(z_i=1\) 时 \(M_{\pm}=0\)、\(P=D\)，等号完全保留。
此 gap 允许依赖总有效组长 \(Q\)，不把它误称为相位所需的统一有限 \(\kappa\)。
负方向个数的结论则不依赖任何数值扫描。

## 4. 完整惯性：恰一个负方向

由
\[
\widehat K=P-\frac{ww^*}{A},\qquad P>0,
\]
\(\widehat K\) 至多有一个非正方向。

它在 \(Q>1\) 时确有负方向。令
\[
R=D^{-1/2}WD^{-1/2}.
\]
其对角为 \(R_{ii}=q_i\ge1\)，且所有非对角严格为正。
若有 \(q_i>1\)，则 \(\lambda_{\max}(R)\ge q_i>1\)。
若全部 \(q_i=1\) 且 \(Q>1\)，用全一列的 Rayleigh 商，严格正的非对角给
\(\lambda_{\max}(R)>1\)。因此 \(I-R\) 有负特征值，\(\widehat K\) 也有负方向。

最后用 (3.4) 的完整 rank-one 同余：
\[
P^{-1/2}\widehat K P^{-1/2}
=I-\frac{(P^{-1/2}w)(P^{-1/2}w)^*}{A}.
\]
既然存在负方向，唯一非平凡特征值严格小于零；其余全部等于 \(1\)。故
\[
\boxed{
Q>1\Longrightarrow
\operatorname{inertia}(\widehat K)=(m-1,\ 1,\ 0),
} \tag{4.1}
\]
按正、负、零特征数排列。

当 \(Q=1\) 时只有一个 \(q_1=1\)，直接由 (1.1) 得
\(\widehat K=D-W=0\)。这是真正边界，不应套用严格惯性结论。

## 5. 一个准确的混合逆标量后果

当 \(Q>1\) 时，\(\widehat K\) 与
\(\mathsf G-nm^*\) 相似，所以后者行列式为负，而 \(\det\mathsf G>0\)。
矩阵行列式引理给
\[
\det(\mathsf G-nm^*)=
\det\mathsf G\,(1-m^*\mathsf G^{-1}n).
\]
因此
\[
\boxed{m^*\mathsf G^{-1}n>1\quad(Q>1).} \tag{5.1}
\]
当 \(Q=1\) 时该标量为 \(1\)。

本稿不给 (5.1) 一个与 \(Q\) 无关的上界，也不把惯性代替原 Euclidean 相位范数。下一步必须仍在同一 \(\mathsf H,\mathsf L,\mathsf G\) 中控制唯一负方向及其与其余源的交叉。只有 (3.3)–(3.4) 的真实正补偿可以带入该共同 Schur；任意具有同样惯性的矩阵不享有这些积分约束。

