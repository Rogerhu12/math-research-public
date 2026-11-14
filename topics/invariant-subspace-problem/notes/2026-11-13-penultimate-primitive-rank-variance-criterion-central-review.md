# 任意出生的算子方差判据与整个 primitive 中段系数一

日期：2026-11-13  
作者：AI 协作研究，central_review  
状态：已证明；root 已独立全文核验完整 MP、两均值逆、端点纤维、严格性及全部窗口因子。本文不声称一般权、一般出生的全区间系数一。

## 1. 范围、完整逆与主结论

取 q 个正头权 a_i，以及 L 个权为一的弱池位，满足 q≥1、L≥q。有限 Boolean 删除算子为
$$
D=\sum_{i=1}^q a_iE_i+D_{\rm w}.
$$
在弱池置换固定部分，取相对出生
$$
s=q-1,\qquad h=L-q+2\ge2.
$$
这里的 primitive 源空间维数为 q。始终先在完整孔层取
$$
F_n=\frac{D^n(D^*)^n}{(n!)^2}
$$
的逆，再压到 primitive 源；不得换成先压缩后的逆。

使用 [一般头一参数完整 MP 公式](../results/R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md) 的坐标变换 f_i=a_i x_i。记
$$
A_i=a_i^2,\quad A_R=\prod_{i\in R}A_i,\quad
s_R(x)=\sum_{i\in R}x_i.
$$
源向量准确为
$$
g(x)=\sum_{\varnothing\ne R\subseteq[q]}
\frac{(-1)^{|R|-1}a_R}{\binom L{|R|-1}}
s_R(x)\,e_{[q]\setminus R}w_{|R|-1}.
\tag{1.1}
$$
令 H_n 为完整 MP 平方范数在此源坐标中的正 Gram：
$$
\langle H_nx,x\rangle
=\left\|\left(\frac{D^n}{n!}\right)^\dagger g(x)\right\|^2.
\tag{1.2}
$$
该引用已逐式支付：所有池固定解的一参数描述、两端的强制参数、对全 Hilbert 原像的群平均、以及真实完整最小范数。这里不重新假定一个受限右逆等于完整 MP。

本文证明一个依实际权的方差判据，并从它推出以下权无关结论。

**定理 1（任意头数的中段系数一）。** 对任意
$$
1\le n<h
$$
满足
$$
\boxed{4n(h-n)\ge(q-1)^2(h+q),}
\tag{1.3}
$$
都有严格算子不等式
$$
\boxed{H_nH_{n+1}^{-1}H_n<H_{n-1}.}
\tag{1.4}
$$
对应真正 primitive 算子同样满足
$$
\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n<\Gamma_{n-1}.}
\tag{1.5}
$$
严格性指两边之差正定。

对 q=1、2，(1.3) 覆盖全部合法 n；这是已有小头范围的另一种证明。对 q≥3，(1.3) 自动排除 n=1 和 n=h-1；这些端点没有被中段结论冒充为已闭。新一般范围从 q≥4 开始有独立意义，q≤3 的完整系数一范围已有更强结果。

实数中段窗口非空的准确条件为
$$
h\ge q(q-1),\quad\text{等价于}\quad L\ge q^2-2.
\tag{1.6}
$$
此时可将 (1.3) 写成
$$
|2n-h|
\le\sqrt{(h-q(q-1))(h+q-1)}.
\tag{1.7}
$$
最短窗口 h=q(q-1) 的中心 n=h/2 为整数。这里只讨论属于该窗口的合法整数阶。

## 2. 三个相邻 Gram 的同一概率空间

对固定内部阶 1≤n<h，全部子集 R 都合法，定义
$$
\omega_R(n)=\frac{A_R}{\binom L{n+|R|-1}},
\quad W_n=\sum_R\omega_R(n),
\quad \mu(R)=\frac{\omega_R(n)}{W_n}.
\tag{2.1}
$$
每个子集的概率都严格为正。令随机秩与移位秩为
$$
r=|R|,\qquad k=n+r-1,\qquad 0\le k\le L.
$$
内部完整 MP 公式为
$$
\langle H_nx,x\rangle
=W_n\min_z\mathbb E_\mu|s_R(x)-z|^2
=W_n\operatorname{Var}_\mu(s_R(x)).
\tag{2.2}
$$
因此双线性形式为相同概率下的协方差。

若 0<k<L，定义
$$
\alpha(k)=\frac{L-k+1}{k},\qquad
\beta(k)=\frac{k+1}{L-k}.
\tag{2.3}
$$
准确的相邻权比是
$$
\omega_R(n-1)=\alpha(k)\omega_R(n),\qquad
\omega_R(n+1)=\beta(k)\omega_R(n).
\tag{2.4}
$$

端点必须保留一参数公式中的原约束：

- n=1 时，H_0 的参数固定为 z=0；唯一的 k=0 状态是 R=∅，且 s_∅(x)=0。因此这一状态的左函数 u 必须为零，不引入无穷权乘非零值。
- n=h-1 时，H_h 的参数固定为 z=s_[q](y)；唯一的 k=L 状态是 R=[q]，故右函数 v 必须为零。
- 其余情况下两个相邻参数独立作普通最小化。

所以相邻费用准确地分别是
$$
W_n\mathbb E_\mu\bigl[\alpha(k)|u|^2\bigr],
\qquad
W_n\mathbb E_\mu\bigl[\beta(k)|v|^2\bigr],
\tag{2.5}
$$
其中 u=s_R(x)-z_-、v=s_R(y)-z_+，并遵守上述端点约束。非法分母对应的项完全删去，因为相应函数已被强制为零；不靠形式极限定义 H_0 或 H_h。

## 3. 一个完整的两均值变分引理

考虑任意有限概率空间上取值于 {0,…,L} 的 k。对 k=0 强制 u=0，对 k=L 强制 v=0；其他状态的 u、v 任意。

在 0<k<L 处，点态正矩阵
$$
C(k)=
\begin{pmatrix}\alpha(k)&1\\1&\beta(k)\end{pmatrix}
$$
满足
$$
\det C(k)=\frac{L+1}{k(L-k)}>0,
$$
且
$$
C(k)^{-1}=
\frac1{L+1}
\begin{pmatrix}
k(k+1)&-k(L-k)\\
-k(L-k)&(L-k)(L-k+1)
\end{pmatrix}.
\tag{3.1}
$$
将右侧记为 B(k)。在 k=0 时，
$$
B(0)=\operatorname{diag}(0,L),
$$
它恰是仅允许 v 的费用 |v|²/L 的逆；在 k=L 时
$$
B(L)=\operatorname{diag}(L,0)
$$
作同样解释。因此 (3.1) 是所有合法点态纤维的准确逆，端点不需要额外误差。

置
$$
K=\mathbb E B(k),\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{3.2}
$$
在本文 (2.1) 的分布下 K 严格正定：若 L≥2，支持包含一个内部秩，其 B(k) 正定；L=1 时两个端点均有正质量，和仍正定。

固定两个均值
$$
m_u=\mathbb E u,\qquad m_v=\mathbb E v.
$$
点态费用的准确最小值为
$$
\min_{\mathbb E(u,v)=(m_u,m_v)}
\mathbb E\left[
\alpha|u|^2+2\operatorname{Re}(\overline uv)+\beta|v|^2
\right]
=
\begin{pmatrix}m_u\\m_v\end{pmatrix}^*
K^{-1}
\begin{pmatrix}m_u\\m_v\end{pmatrix}.
\tag{3.3}
$$
确切极小函数是
$$
\begin{pmatrix}u(k)\\v(k)\end{pmatrix}
=B(k)K^{-1}
\begin{pmatrix}m_u\\m_v\end{pmatrix}.
$$
它自动满足端点零约束。证明只需将任意函数减去这个极小函数，按点态 C 内积展开；交叉项是残差均值，准确为零。

注意协方差交叉项比 (3.3) 的点态交叉项少
$$
2\operatorname{Re}(\overline{m_u}m_v).
$$
故对所有合法 u,v 有
$$
\mathbb E[\alpha|u|^2+\beta|v|^2]
+2\operatorname{Re}\operatorname{Cov}(u,v)\ge0
\tag{3.4}
$$
当且仅当
$$
K^{-1}-J\succeq0.
\tag{3.5}
$$
这里是均值约束后的完整逆 K^{-1}，没有逐状态取逆后再错误地交换最小化次序。

## 4. 准确方差判据

设
$$
m=\mathbb E k,\qquad
v=\operatorname{Var}(k),\qquad
d=\frac{\mathbb E[k(L-k)]}{L+1}
=\frac{m(L-m)-v}{L+1}.
$$
由 (3.1)，
$$
K=
\begin{pmatrix}m-d&-d\\-d&L-m-d\end{pmatrix}.
\tag{4.1}
$$
矩阵 K^(1/2) J K^(1/2) 与 JK 相似，其两个特征值为
$$
-d\pm\sqrt{(m-d)(L-m-d)}.
$$
负号分支严格小于一。正号分支不大于一，等价于
$$
m(L-m)\le1+(L+2)d.
$$
代入 d 得到以下完全等价的判据：
$$
\boxed{
K^{-1}-J\succeq0
\iff
(L+2)v\le(m+1)(L-m+1).
}
\tag{4.2}
$$
两侧不等式严格时，(3.4) 对任意非零合法函数对严格为正。

**定理 2（依实际秩分布的判据）。** 若 (2.1) 的真实概率满足
$$
\boxed{
\operatorname{Var}_\mu(k)
\le\frac{(\mathbb E_\mu k+1)(L-\mathbb E_\mu k+1)}{L+2},
}
\tag{4.3}
$$
则
$$
\begin{pmatrix}H_{n-1}&H_n\\H_n&H_{n+1}\end{pmatrix}\succeq0.
\tag{4.4}
$$
若 (4.3) 严格，则 (4.4) 正定，并给出 (1.4)。

证明：给定 x,y，分别取 H_(n−1)、H_(n+1) 的实际极小参数 z_-、z_+。它们满足 §2 的端点约束。协方差对减去任何常数不变，故 (3.4) 乘 W_n 正是 (4.4) 在 (x,y) 上的二次型。若 (x,y) 非零，至少一个 s_R 非常数，因为全部子集都有正概率，且空集值为零；所以该函数对不可能全零。严格性因此保留。最后对 H_(n+1)>0 取 Schur 补即得 (1.4)。

## 5. 只用秩范围的权无关窗口

写
$$
\bar r=\mathbb E r,\qquad v=\operatorname{Var}(r).
$$
由于 0≤r≤q，
$$
v\le\bar r(q-\bar r).
\tag{5.1}
$$
这是将 r(q-r)≥0 取期望。q≥2 且全部子集概率正时，(5.1) 严格，因为存在正概率的 1≤r≤q-1 状态。

令
$$
H=h+q=L+2,\quad
\delta=2n-h,\quad
x=\bar r-\frac q2.
$$
方差判据左移后的余量为
$$
\mathcal D=(n+\bar r)(h+q-n-\bar r)-Hv.
$$
使用 (5.1) 并完成平方：
$$
\begin{aligned}
\mathcal D
&\ge(n+\bar r)(h+q-n-\bar r)-H\bar r(q-\bar r)\\
&=(H-1)\left(x-\frac{\delta}{2(H-1)}\right)^2\\
&\quad+
\frac{H}{4(H-1)}
\left[4n(h-n)-(q-1)^2(h+q)\right].
\end{aligned}
\tag{5.2}
$$
这证明 (1.3) 蕴含 (4.3)。

严格性也没有遗漏：

- q≥2 时，(5.1) 已严格，故即使 (1.3) 等号，仍有 𝒟>0。
- q=1 时，(5.1) 可以等号，但 (5.2) 方括号为 4n(h-n)>0。

所以定理 1 的矩阵差确实正定。

对 q=2，合法区间上
$$
4n(h-n)-(h+2)\ge4(h-1)-(h+2)=3(h-2)\ge0.
$$
q=1 更直接。因此这两个头数包括首尾。q≥3 时若 n=1，则
$$
4(h-1)<(q-1)^2(h+q),
$$
对另一端相同；故新一般窗口自动只在真正内部，没有遗漏非法二项式端点。

最后，
$$
h^2-(q-1)^2(h+q)
=(h-q(q-1))(h+q-1),
$$
给出 (1.6)—(1.7)。

## 6. 真正算子坐标、归属和未闭范围

源基通常不正交。若其 Gram 是 H_0，真正 Γ_n 的坐标矩阵是
$$
H_0^{-1}H_n.
$$
于是 Γ_n Γ_(n+1)^(-1) Γ_n 的坐标为
$$
H_0^{-1}H_nH_{n+1}^{-1}H_n.
$$
用源内积 H_0 比较，正好是 (1.4)；没有把 Gram form 与坐标算子混同。上述推导也始终保留完整逆后压缩。

本判据用的是未加出生阶乘归一的相邻三项，所以只给系数一；没有推出
$$
\frac{n+q-1}{n+q}
$$
这一更小系数，也没有证明完整的矩阵 Hankel 或 Stieltjes 正性。

它是充分判据，不是原 primitive 不等式的必要条件。例如 q=4、L=4、h=2、所有 A_i=1、n=1 时，r 在 {0,1,2,3,4} 上均匀，
$$
\mathbb E r=2,\qquad\operatorname{Var}(r)=2,
$$
而 (4.3) 的右侧为 3/2。此时两均值的“所有函数”扩张不满足判据，但原等权 primitive 不等式仍有既有 sl(2) 证明；不能据此宣称原 Γ 反例。

q≤3 的全区间结论已有三头完整结果；本文的新统一范围是任意 q 的实际方差准则及 (1.3) 中段窗口。窗口外、其他相对出生层、任意不规则实际尾，以及 ISP 主目标，均不由本文结论自动关闭。

## 7. 任意出生的多项式商与非交换方差判据

本节在 §1—6 的两均值方法上，保留整个低次多项式商。它不是把标量判据直接逐特征值套到两个未必交换的压缩算子。

### 7.1 真实完整 MP 的共同商空间

取 q≥3、L≥q。设相对出生为
$$
s=q-\delta,\qquad 0\le\delta\le q,
$$
并记
$$
h_\delta=L-q+2\delta,\qquad h_0^\flat=L-q+2.
\tag{7.1}
$$
这里 h_0^\flat 只是下文窗口参数，不是出生零的谱串长度。

采用[一参数主稿 §10 的全部出生完整 MP 公式](../results/R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md)。源由齐次多重仿射多项式
$$
f(X)=\sum_{|I|=\delta}x_I X_I
$$
参数化，记其实际源嵌入为
$$
\mathcal E_\delta f=
\sum_{|R|\ge\delta}
(-1)^{|R|-\delta}
\frac{a_R}{\binom L{|R|-\delta}} f(R)\,
e_{[q]\setminus R}w_{|R|-\delta}.
\tag{7.2}
$$
令 H_n^δ 是此源的完整 MP Gram，先全层取逆再压缩。该文的群平均和有限差分已给出准确公式
$$
\langle H_n^\delta f,f\rangle
=\min_{\deg p\le\delta-1}
\sum_R \frac{A_R}{\binom L{n+|R|-\delta}}|f(R)+p(R)|^2
\tag{7.3}
$$
只要全部状态合法；δ=0 时没有 p 参数。

本文考虑
$$
\nu=n+1-\delta,\qquad
1\le\nu<h_0^\flat,
$$
满足
$$
\boxed{
4\nu(h_0^\flat-\nu)
\ge(q-1)^2(h_0^\flat+q).
}
\tag{7.4}
$$
由于 q≥3，§5 的端点检查自动给
$$
\nu\ge2,\qquad h_0^\flat-\nu\ge2.
$$
所以
$$
\delta+1\le n\le h_\delta-\delta-1.
\tag{7.5}
$$
在 n−1、n、n+1 三阶中，全部 2^q 个头状态都合法；三个最小化确实使用同一个低次多项式空间。本文没有将这个共同商假设搬到近端的改变维数区间。

固定 n，定义
$$
\omega_R=\frac{A_R}{\binom L{n+|R|-\delta}},\quad
W=\sum_R\omega_R,\quad \mu(R)=\omega_R/W,
$$
并在有限 Hilbert 空间
$$
\mathscr H=L^2(\{R\subseteq[q]\},\mu)
$$
中令 V 为次数至多 δ−1 的多重仿射函数空间，P 为其正交投影。δ=0 时 V={0}。令 M 为实函数
$$
k=n+|R|-\delta=\nu+|R|-1
$$
的乘法算子。由 (7.5)，所有 k 都严格介于 0 与 L 之间。

以 U=I−P 记正交余量，则
$$
H_n^\delta(f,g)=W\langle Uf,Ug\rangle_\mu.
\tag{7.6}
$$
前后两阶分别是在同一个 f+V 上，以乘法权
$$
\alpha(M)=\frac{L-M+I}{M},
\qquad
\beta(M)=\frac{M+I}{L-M}
$$
作最小化；这些分式都是真正的有限正单位。

### 7.2 两个多项式投影约束的准确最小化

暂取 δ≥1。压缩乘法及离开商空间的部分记为
$$
R=P M|_V,\qquad C=(I-P)M|_V.
$$
它们满足
$$
P M^2|_V=R^2+C^*C.
\tag{7.7}
$$
不假设 R 与 C* C 交换。

对任意 u,v∈𝓗，所需的跨项为
$$
\langle Uu,Uv\rangle
=\langle u,v\rangle-\langle Pu,Pv\rangle.
$$
点态正费用矩阵仍是 §3 的
$$
\mathcal C(k)=\begin{pmatrix}\alpha(k)&1\\1&\beta(k)\end{pmatrix}.
$$
固定整个多项式投影
$$
Pu=m_1,\qquad Pv=m_2,\qquad m_i\in V,
$$
后，完整最小点态费用为
$$
\left\langle K^{-1}
\begin{pmatrix}m_1\\m_2\end{pmatrix},
\begin{pmatrix}m_1\\m_2\end{pmatrix}\right\rangle,
$$
其中
$$
K=(P\oplus P)\mathcal C(M)^{-1}|_{V\oplus V}.
\tag{7.8}
$$
K 是严格正单位。证明与 (3.3) 完全相同：极小函数对为
$$
\mathcal C(M)^{-1}\iota K^{-1}(m_1,m_2),
$$
其中 ι 将 V⊕V 嵌入 𝓗⊕𝓗；减去它后的交叉项只读两个零投影。这里没有先在 V 上倒置乘法费用。

因此
$$
\mathbb E[\alpha|u|^2+\beta|v|^2]
+2\operatorname{Re}\langle Uu,Uv\rangle\ge0
\quad\text{对全部 }u,v
\tag{7.9}
$$
等价于
$$
K^{-1}-J\succeq0,\qquad
J=\begin{pmatrix}0&I_V\\I_V&0\end{pmatrix}.
\tag{7.10}
$$
严格正定版本也等价。

由 (3.1)、(7.7)，准确有
$$
K=
\begin{pmatrix}
R-\Delta&-\Delta\\
-\Delta&LI-R-\Delta
\end{pmatrix},
\qquad
\Delta=\frac{R(LI-R)-C^*C}{L+1}.
\tag{7.11}
$$

### 7.3 非交换 Schur 消元给出的算子方差式

用 Hadamard 酉矩阵把 J 化为 diag(I,−I)。变换后的 K 为
$$
\widetilde K=
\begin{pmatrix}
\frac L2 I-2\Delta&R-\frac L2I\\
R-\frac L2I&\frac L2I
\end{pmatrix}.
\tag{7.12}
$$
这一步没有交换 R 和 Δ 的乘法顺序。

令 Q_+ 为第一分量投影。因为
$$
\widetilde K^{-1}-\operatorname{diag}(I,-I)
=(\widetilde K^{-1}+I)-2Q_+,
$$
正性等价于
$$
2Q_+(\widetilde K^{-1}+I)^{-1}Q_+\preceq I_V.
$$
再用
$$
(\widetilde K^{-1}+I)^{-1}
=I-(I+\widetilde K)^{-1},
$$
它等价于 (I+K̃) 的左上逆块不小于 I/2。

右下块恰为 (L+2)I/2，故此左上逆块是以下真正 Schur 补的逆：
$$
S=I+\frac L2I-2\Delta
-\frac2{L+2}\left(R-\frac L2I\right)^2.
$$
因此条件正好是 S≤2I。直接整理可得
$$
2I-S=\frac{2}{(L+1)(L+2)}\Theta,
$$
其中
$$
\boxed{
\Theta=(R+I)((L+1)I-R)-(L+2)C^*C.
}
\tag{7.13}
$$
于是得到完整非交换等价式
$$
\boxed{
K^{-1}-J\succeq0
\iff
(L+2)C^*C\preceq(R+I)((L+1)I-R).
}
\tag{7.14}
$$
严格正定也等价。只在 (7.12) 的右下标量块上作 Schur 消元；没有把标量方差公式套到非交换矩阵的共同特征向量。

### 7.4 一条精确的正分拆与严格性

记 r=|R| 的乘法算子，令
$$
\widehat R=P r|_V,\qquad
G=P\,r(q-r)|_V,\qquad H=L+2=h_0^\flat+q.
$$
由于 M=(ν−1)I+r，
$$
R=(\nu-1)I+\widehat R.
$$
由 (7.7) 逐项相减，准确有
$$
C^*C=\widehat R(qI-\widehat R)-G.
\tag{7.15}
$$
这比只写算子 Bhatia–Davis 上界更强，保留了余量 G。

将 (7.15) 代入 (7.13)，使用与 (5.2) 相同的标量多项式恒等式，得到
$$
\boxed{
\begin{aligned}
\Theta={}&
(H-1)\left[
\widehat R-\left(\frac q2+
\frac{2\nu-h_0^\flat}{2(H-1)}\right)I
\right]^2\\
&+\frac{H}{4(H-1)}
\left[4\nu(h_0^\flat-\nu)
-(q-1)^2(h_0^\flat+q)\right]I
+HG.
\end{aligned}
}
\tag{7.16}
$$
这里是准确等式。即使 R 与 G 不交换，右侧每一项的正性仍可单独使用；没有出现不合法的乘积排序。

(7.4) 使所有项半正。严格性分两种情况付清。

若 1≤δ≤q−1，则 V 中函数的次数至多 q−2。若 Gv=0，正概率迫使 v 只可能支持在 ∅ 与 [q]。这类函数的唯一多重仿射表示为
$$
\alpha\prod_i(1-X_i)+\beta\prod_iX_i.
$$
要使次数至多 q−2，所有 q−1 次系数先迫使 α=0，再由 q 次系数迫使 β=0。因此 G 在 V 上正定，进而 Θ>0。

若 δ=q，则 V 允许 q−1 次函数。此时 G 的核准确是一条两端支撑直线，且非零向量在两个端点的值都非零。仍不可能同时落在 (7.16) 的平方项之核。确实，若这样的 v 满足 Rv=λv，则因 1、k∈V，
$$
\langle(k-\lambda)v,1\rangle_\mu
=\langle(k-\lambda)v,k\rangle_\mu=0.
$$
写两个端点 k 值为 a=ν−1、b=a+q，并把带正概率的两个非零值记为 u_0,u_q，便有
$$
(a-\lambda)u_0+(b-\lambda)u_q=0,
$$
$$
a(a-\lambda)u_0+b(b-\lambda)u_q=0.
$$
相减先得 λ=b，再由第一式得 λ=a，矛盾。因此两个半正项无共同非零核，Θ仍正定。这里的真空出生也可由已有 Newton 不等式直接处理，但本证明并不需要跳过其严格性。

δ=0 时 V={0}，没有投影扣项，(7.9) 就是点态正矩阵 𝓒(k) 的费用，已严格为正。

### 7.5 全部相对出生的中段定理

**定理 3。** 对 q≥3、L≥q、0≤δ≤q，取完整池固定 primitive 块的真实 Gram H_n^δ。若 1≤ν=n+1−δ<h_0^flat 并满足 (7.4)，则
$$
\boxed{
H_n^\delta(H_{n+1}^\delta)^{-1}H_n^\delta
<H_{n-1}^\delta.
}
\tag{7.17}
$$
对应真实 Γ 的次序相同。

证明：分别取相邻两阶的实际最小低次修正，令 u=f+p_-、v=g+p_+。它们属于同一个共同商；(7.6) 保跨项不受修正影响。由 (7.9)—(7.16)，相邻二乘二块正定。非零齐次 δ 次源不属于 V，故不会被商掉；δ=0 的非零常数源同样非零。对 H_(n+1)>0 作真正 Schur 补，得 (7.17)。源非正交时依 §6 先保 H_0 合同，不改变结论。

本定理给任意出生的统一系数一窗口，不给窗口外的全区间系数一，也不证明更小出生因子或完整矩阵 Hankel 正性。

## 8. q 个异常头加等权池的整个 primitive 中段

上节是一个弱池固定块。下面明确支付整个 primitive 空间的拼合，不把固定块直接称为全空间。

设原模型有 q≥3 个任意正异常头及 M 个单位权池位，总位数 N=M+q。在总出生 s 的 primitive 空间 K_s 上令
$$
h=N-2s.
$$
假设
$$
h\ge q^2+q-4,
$$
并取 1≤n<h 满足
$$
\boxed{
4(n-q+2)(h-n-q+2)
\ge(q-1)^2(h-q+4).
}
\tag{8.1}
$$
则整个 K_s 上严格成立
$$
\boxed{
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n<\Gamma_{n-1}.
}
\tag{8.2}
$$

给出完整约化范围。弱池的标准正交 Lefschetz 分解将每个出生 j 的弱 primitive 及其字符串化为长度
$$
L_j=M-2j
$$
的对称弱池链；该分解同时约化弱 D 与 D*。与头张量以后，完整 F_n、其全层逆及 primitive 压缩都按这些子空间约化。

只有 j≤s 能贡献，置相对头出生
$$
t=s-j.
$$
由全局假设，
$$
L_j\ge M-2s=h-q\ge q^2-4\ge q.
\tag{8.3}
$$
若 t>q，则处于总中线以下的固定输入、输出均包含所有头状态，弱删除在每个头状态上给严格非零对角元，头删除只给三角项。因此该固定删除为可逆三角矩阵，没有 primitive。合法非零部分只需 t=0,…,q。

t=0 是真空线。其完整 Gram 为正倍数 1/e_n，其中 e_n 是该有限权平方的初等对称和；Newton 的准确有限因子严格小于一，故这条线全部合法相邻阶已满足 (8.2)。

对 t≥1，相关参数是
$$
\delta_t=q-t,\quad
L_t=h-q+2t,\quad
h_{0,t}^\flat=h-2q+2t+2,
$$
$$
\nu_t=n+1-q+t.
\tag{8.4}
$$
最紧的非真空窗口是 t=1：
$$
h_{0,1}^\flat=h-2q+4,\qquad
\nu_1=n-q+2.
$$
它正好由 (8.1) 给出，并且 h_(0,1)^flat≥q(q−1)。

令 a=t−1≥0。从 t=1 到 t，两边的距离参数都增加 a，而 h_0^flat 增加 2a。窗口余量的变化准确为
$$
a\bigl[4h_{0,1}^\flat-2(q-1)^2\bigr]+4a^2\ge0.
\tag{8.5}
$$
因此所有 t≥1 的块均满足定理 3。固定总源上的真实合法串长始终为
$$
L_t+q-2t=h,
$$
故所用 n 在各块的完整层上都合法，没有把某块短端越过后再求逆。

全部块有限且正交，真 F_n 先全层求逆后仍逐块，严格正差的有限直和仍正定。这证明 (8.2)。

(8.1) 也可写成
$$
|2n-h|\le
\sqrt{(h-q^2-q+4)(h-q+3)}.
\tag{8.6}
$$
最短 h=q²+q−4 是偶数，中心阶 n=h/2 合法。

此处是“有限 q 个异常权＋一个真正等权池”的整个 primitive 中段。若把一般连续尾或任意有限权模型补入一个小权池，还须独立支付极限及阶数范围；不能由本中段窗口宣称原早期返回费或全部无限尾已经闭合。

## 9. 真正线性源的准确 Schur 修正与全区间标量判据

本节仍只考虑 §§1–6 的相对出生 s=q−1 固定块：
$$
q\ge1,\qquad L\ge q,\qquad h=L-q+2,\qquad1\le n<h.
$$
它保留完整 MP 与真实一参数源，不把待证的一般相邻序当作结论。新增的是一个必要且充分的标量判据：旧全函数方差条件之外，原线性空间自动提供一个明确的非负修正。修正是否对任意权足够，仍须证明。

### 9.1 原源空间与全部端点纤维

继续使用 (2.1) 的严格正概率 μ，及
$$
r=|R|,\qquad k=n+r-1,\qquad
m=\mathbb E_\mu k,\qquad v=\operatorname{Var}_\mu k.
$$
在有限 Hilbert 空间
$$
\mathcal H=L^2(2^{[q]},\mu)
$$
中，定义真正的一次函数空间
$$
\mathcal W=\operatorname{span}\{1,X_1,\ldots,X_q\},
\qquad P=P_{\mathcal W},\qquad Q=I-P.
\tag{9.1}
$$
每个子集均有正质量，故此空间的维数为 q+1，且 1、k 都属于 W。所有投影均为当前 μ 内积下的正交投影。

相邻两参数的函数恰为
$$
u(R)=\sum_i x_iX_i(R)-z_-,
\qquad
w(R)=\sum_i y_iX_i(R)-z_+.
$$
它们都属于 W。若 k=0，则强制 u=0；若 k=L，则强制 w=0。前者仅发生于 n=1 的空集，后者仅发生于 n=h−1 的全集。这正是原 H_0、H_h 的准确约束，没有增加或删除自由参数。

记点态费用为
$$
\mathfrak c(u,w)
=\mathbb E_\mu\left[
\alpha(k)|u|^2+2\operatorname{Re}(\overline u w)+\beta(k)|w|^2
\right],
\tag{9.2}
$$
其中 α、β 如 (2.3)，端点只取合法纤维上的项。每个合法纤维上的费用严格正；其零延拓逆为 (3.1) 的
$$
B(k)=\frac1{L+1}
\begin{pmatrix}
k(k+1)&-k(L-k)\\
-k(L-k)&(L-k)(L-k+1)
\end{pmatrix}.
\tag{9.3}
$$
B(0)=diag(0,L)、B(L)=diag(L,0)，并非在端点对奇异的整块形式作普通求逆。

因为协方差不受 z_-、z_+ 影响，原相邻块
$$
\begin{pmatrix}H_{n-1}&H_n\\H_n&H_{n+1}\end{pmatrix}
\tag{9.4}
$$
正半定，当且仅当对全部上述 u,w 都有
$$
\mathfrak c(u,w)
-2\operatorname{Re}\bigl(\overline{\mathbb E u}\,\mathbb E w\bigr)
\ge0.
\tag{9.5}
$$
确实，对给定 x,y，先分别最小化两个相邻参数，就精确恢复 (9.4) 的二次型。这里 u,w 只遍历 W；把它们放大到任意函数只是原 §3 的充分条件。

### 9.2 低次约束的真实逆与秩一修正

令 B 表示 (9.3) 在 H⊕H 上的乘法算子，令
$$
Q_2=Q\oplus Q,\qquad
B_Q=Q_2B|_{Q\mathcal H\oplus Q\mathcal H}.
$$
若 QH 非零，则 B_Q 严格正定。其证明不需要抹去端点：一个零费用向量必须在所有内部状态为零，第一分量只能支持 k=0，第二分量只能支持 k=L；但每个分量都正交于常数 1，故在单个正质量端点也必须为零。

定义
$$
t=Qk^2\in Q\mathcal H.
\tag{9.6}
$$
从 Q1=Qk=0 及 (9.3) 逐项得到
$$
Q_2B\binom{\xi\,1}{\eta\,1}
=\frac{\xi+\eta}{L+1}\binom t t.
\tag{9.7}
$$
这就是原一次空间带来的关键简化：全部高次约束只通过一个向量 t 和两个均值之和耦合。

令 K=E B 为 §3 的两均值 Gram。固定均值 b=(b_1,b_2)，并同时强制 Qu=Qw=0 时，准确最小费用为
$$
\min_{\substack{\mathbb E(u,w)=b\\u,w\in\mathcal W\\
\text{端点纤维约束}}}\mathfrak c(u,w)
=b^*K_{\mathcal W}^{-1}b,
\tag{9.8}
$$
其中
$$
\boxed{
K_{\mathcal W}
=K-\tau\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad
\tau=\frac1{(L+1)^2}
\left\langle\binom t t,B_Q^{-1}\binom t t\right\rangle\ge0.
}
\tag{9.9}
$$
当 QH 为零时，约定 τ=0。

为完整支付 (9.8)，可以直接用有限维严格凸最小化：在所有合法点态纤维上，均值与高次约束的联合 Gram 为
$$
\begin{pmatrix}
K&\mathcal F\\
\mathcal F^*&B_Q
\end{pmatrix},
\qquad
\mathcal F^*\binom{\xi}{\eta}
=\frac{\xi+\eta}{L+1}\binom t t.
$$
消去高次约束的乘子，得到其 Schur 补 K−F B_Q^{-1}F*，即 (9.9)。此联合约束具有满行秩：B_Q>0 已支付高次部分，而在 W 中可分别选 u=X_1（左端需要零时）或 u=1，以及 w=1−X_1（右端需要零时）或 w=1，实现任意两个均值。严格正质量保证这些测试的均值非零。因此 K_W 严格正定，(9.8) 使用普通逆，既不借闭值域假设，也没有将奇异端点当作可逆整块。

### 9.3 修正项的单算子正表示

把 k 视为 H 上的自伴乘法算子，置
$$
R_0=Qk|_{Q\mathcal H},\qquad
C_0=Pk|_{Q\mathcal H}.
$$
定义 QH 上的正算子
$$
\mathscr S
=R_0(LI-R_0)+L C_0^*C_0
=Qk(L-k)|_{Q\mathcal H}+(L+1)C_0^*C_0.
\tag{9.10}
$$
它严格正定。事实上，第一项的零空间只能由 k=0、L 的端点支持组成；但 QH 中的函数同时正交于 1 和 X_1，因此不能非零地只支持这两个端点。若只有一个端点，此结论更直接。q=1 时 QH=0，仍采用零空间约定。

对 B_Q 作常数 Hadamard 酉变换，准确得到
$$
\widetilde B_Q=
\begin{pmatrix}
\frac L2 I-\frac2{L+1}Qk(L-k)|_{Q\mathcal H}
&
R_0-\frac L2 I\\
R_0-\frac L2 I&\frac L2 I
\end{pmatrix}.
$$
左上角对右下角的 Schur 补为
$$
\frac{2}{L(L+1)}\mathscr S.
\tag{9.11}
$$
这里用了 Qk²Q=R_0²+C_0*C_0，不能把投影与 k 交换。

向量 (t,t) 经同一酉变换为 (sqrt(2)t,0)，所以 (9.9) 化为
$$
\boxed{
\tau=\frac L{L+1}\langle t,\mathscr S^{-1}t\rangle.
}
\tag{9.12}
$$
它仍是原有限概率空间和原一次函数投影产生的准确量；没有换成完整空间预解或标量平均的逆。

### 9.4 必要且充分的相邻标量判据

记
$$
d=\frac{\mathbb E[k(L-k)]}{L+1}
=\frac{m(L-m)-v}{L+1}.
$$
原 K 与修正后的 K_W 分别为
$$
K=\begin{pmatrix}m-d&-d\\-d&L-m-d\end{pmatrix},
$$
$$
K_{\mathcal W}
=\begin{pmatrix}
m-d-\tau&-d-\tau\\
-d-\tau&L-m-d-\tau
\end{pmatrix}.
\tag{9.13}
$$
因此修正只将 d 改为 d+τ；m 与 L 均保持原值。

由 (9.5)、(9.8)，原相邻块正半定恰等价于
$$
K_{\mathcal W}^{-1}
-\begin{pmatrix}0&1\\1&0\end{pmatrix}\succeq0.
$$
K_W>0，所以此二乘二矩阵的对角元严格正；其行列式的符号准确为
$$
1+(L+2)(d+\tau)-m(L-m).
$$
代入 d，得到以下完整等价式：
$$
\boxed{
H_nH_{n+1}^{-1}H_n\preceq H_{n-1}
\quad\Longleftrightarrow\quad
(L+2)v
\le (m+1)(L-m+1)+(L+1)(L+2)\tau.
}
\tag{9.14}
$$
严格不等式也等价。若标量取等号，(9.8) 的非零均值极小函数给原块的零向量；其两个一次部分不可能同时为零，因为非零常数对的协方差为零而合法点态费用严格正。反过来，标量严格则 (9.5) 对任何非零一次源对严格为正。

从 H_n 到实际 Γ_n 的 H_0 同余仍按 §5 保留顺序。因此 (9.14) 也是当前固定 primitive 块真实相邻算子序的必要充分判据。

旧 §4 的方差条件就是舍去 τ≥0 后的充分条件。本节没有证明任意正权都使 (9.14) 的右边足够大；所余问题已集中在原一次函数空间产生的准确正修正，而非任意全函数的最坏情形。

### 9.5 等权最短串的精确校准

取 L=q、h=2、n=1、全部 A_i=1。于是 k=r，秩 r 在 0,…,q 上均匀，
$$
m=q/2,\qquad v=q(q+2)/12.
$$
旧不含修正的方差条件在且仅在 q≤3 时成立；q≥4 的失败只是放大函数空间造成的障碍。

现在对两个固定均值作头置换平均。由于点态费用只依赖 r，严格凸最小值落在 span{1,r}；端点约束唯一给
$$
u=\frac{2b_1}{q}r,\qquad
w=\frac{2b_2}{q}(q-r).
$$
计算一、二阶均匀秩矩，得到
$$
K_{\mathcal W}^{-1}
=\begin{pmatrix}
\frac{2(q+2)}{3q}&\frac{2(q-1)}{3q}\\
\frac{2(q-1)}{3q}&\frac{2(q+2)}{3q}
\end{pmatrix},
$$
以及
$$
d+\tau=\frac{q(q-1)}{2(2q+1)},\qquad
\boxed{\tau=\frac{q(q-1)(q+2)}{6(q+1)(2q+1)}.}
\tag{9.15}
$$
K_W^{-1}−J 的两个特征值恰为
$$
\frac{q+2}{3q},\qquad\frac{q+2}{q},
$$
均严格正。这重新给出已知等权模型的严格相邻序，目的在于校准修正项及其符号，不重计等权范围。

例如 q=4 时，v=2、m=2，旧方差测试给 12>9 而不适用；本节准确修正 τ=4/15，使右侧变为
$$
9+5\cdot6\cdot\frac4{15}=17>12.
$$
真正的一次函数空间修复了该例，且全部端点仍保留。一般异权时，τ 的同样表示仍然准确，但尚未被免费替换成这个等权值。

### 9.6 单个二次残差给出的六阶矩充分条件

仍保 (9.1)–(9.12) 的全部真实空间与端点。以下只是 τ 的一个可直接计算的下界，不假定它对任意外场自动足够。q=1 时 Q=0，原严格不等式已由旧判据直接成立；本小节取 q≥2。由于每个布尔点的 μ 都严格正，k² 的二次项不能由一次函数表示，所以
$$
T_2:=\|t\|^2=\|Qk^2\|^2>0.
$$
对严格正的 S 应用
$$
\langle t,S^{-1}t\rangle\,\langle t,St\rangle\ge\|t\|^4
$$
（对 S^{1/2}t 与 S^{-1/2}t 使用 Cauchy–Schwarz），得
$$
\boxed{
\tau\ge\tau_{\rm quad}
:=\frac L{L+1}
\frac{T_2^2}{
\mathbb E[k(L-k)|t|^2]+(L+1)\|P(kt)\|^2
}.
}
\tag{9.16}
$$
这里用了 (9.10) 第二式及 t∈QH；不是把真实逆换成其一个向量的等式。分母严格正，且保持原端点零因子。

因此一个足够的、只到六阶的真实源条件为
$$
\boxed{
L(L+2)T_2^2\ge
\big[(L+2)v-(m+1)(L-m+1)\big]
\big\{\mathbb E[k(L-k)|t|^2]+(L+1)\|P(kt)\|^2\big\}.
}
\tag{9.17}
$$
严格大于给严格相邻序。若方括号非正，旧判据已足够，不需要对此下界作额外论证。

(9.17) 只需一次维数 q+1 的线性回归和有限矩，不需在整个 QH 上求 S 的逆。准确地，令
$$
b(R)=(1,X_1(R),\ldots,X_q(R))^{\mathsf T},
\quad M=\mathbb E[bb^*]>0,
$$
$$
c=\mathbb E[k^2b],\qquad \beta=M^{-1}c.
$$
所有数据均为实数，因此
$$
t=k^2-b^{\mathsf T}\beta,\qquad
T_2=\mathbb E k^4-c^{\mathsf T}M^{-1}c.
\tag{9.18}
$$
再置
$$
d=\mathbb E[k^3b]-\mathbb E[kbb^*]\beta.
$$
则
$$
\|P(kt)\|^2=d^{\mathsf T}M^{-1}d,
\tag{9.19}
$$
且
$$
\begin{aligned}
\mathbb E[k(L-k)t^2]
={}&L\mathbb E k^5-\mathbb E k^6\\
&-2\beta^{\mathsf T}
\bigl(L\mathbb E[k^3b]-\mathbb E[k^4b]\bigr)\\
&+\beta^{\mathsf T}
\bigl(L\mathbb E[kbb^*]-\mathbb E[k^2bb^*]\bigr)\beta.
\end{aligned}
\tag{9.20}
$$
每个矩的最高秩次数为六；坐标函数至多成对出现。它们都按实际 μ 求值，不只使用秩边缘分布。后一点不能省略：k² 对全部 X_i 的回归通常不同于仅对 1、k 回归。

### 9.7 等权全 q 的精确单向量校准与外场命题

继续 (9.15) 的 L=q、h=2、n=1、A_i=1。头置换对称给
$$
t=r^2-qr+\frac{q(q-1)}6,\qquad
v=\frac{q(q+2)}{12}.
$$
直接对整数 r=0,…,q 作均匀求和，得到
$$
T_2=\frac{q(q-1)(q+2)(q+3)}{180},
\qquad
\frac{\mathbb E t^3}{T_2}=\frac{(q-3)(q+5)}{21},
$$
$$
\mathbb E[r(q-r)t^2]
=T_2\,\frac{5q^2-11q+30}{42},
\qquad
\|P(rt)\|^2=\frac{T_2^2}{v}.
\tag{9.21}
$$
最后一式也由 t⊥1,r 与 r²=t+qr−q(q−1)/6 直接推出；
对称一次函数只含 1、r，故没有遗漏其他坐标方向。

记
$$
D_q=14q^3+67q^2-69q+108>0.
$$
代回 (9.16) 得
$$
\tau_{\rm quad}
=\frac{7q^2(q-1)(q+2)(q+3)}{6(q+1)D_q}.
\tag{9.22}
$$
(9.14) 要求的最低修正为
$$
\tau_{\rm req}=\frac{(q-3)(q+2)}{12(q+1)}.
$$
两者之差准确为
$$
\boxed{
\tau_{\rm quad}-\tau_{\rm req}
=\frac{(q+2)(q^3+76q^2-105q+108)}
{4(q+1)D_q}>0.
}
\tag{9.23}
$$
令 x=q−1≥0，括号多项式化为
$$
x^3+79x^2+50x+80,
$$
所以严格符号由正系数直接证明；差值趋于 1/56。q=1 的零空间情形直接给 τ=0 和原严格条件，不使用 T_2 分母。

这重新校准已知等权结果，未增加等权范围。它还说明：在这个完整的全 q 校准中，甚至只用一个真正二次残差的 Rayleigh 下界，就足以修复旧全函数判据。

**外场自动命题的后续状态。** 对 L=q、h=2、n=1 及任意 A_i>0，(9.17) 是否总成立，曾作为下一命题提出。下方 §9.8 已用真实100头两簇分布和精确整数证书否定它；这不否定完整修正 (9.14)，也不否定一般相邻系数一。有限浮点探针只用于选择方向，严格结论以 §9.8 的整数比较为准。

一般相邻序仍须使用本题完整的外场分布
$$
\mu(R)\ \propto\ \frac{A_R}{\binom q{|R|}},
$$
不能仅假设秩边缘对数凹，亦不能将回归空间换成任意全函数或只含秩的函数。式 (9.14) 的真实必要充分条件继续保持原状态。


### 9.8 单个二次残差判据并不对任意异权自动成立

本节精确回答 §9.7 末的待证命题：答案是否定的。反例针对 (9.17) 的单向量充分条件；它不否定 (9.14) 中保留完整逆的必要充分条件，也不声称 primitive Gram 相邻不等式失败。

取一个真正的 penultimate 固定块
$$
q=L=100,\qquad s=q-1=99,\qquad h=2,\qquad n=1.
$$
一百个头参数分成两组：
$$
A_1=\cdots=A_{50}=\frac54,\qquad
A_{51}=\cdots=A_{100}=\frac56.
\tag{9.24}
$$
这里实际删除权为正数 $a_i=\sqrt{A_i}$，另有一百个单位权池位。因此仍是本稿原来的有限加权布尔模型。

记两个头组的占据数为 $p,s_0\in\{0,\ldots,50\}$，并置
$$
r=p+s_0,\qquad d=p-s_0,\qquad b=(1,r,d)^{\mathsf T}.
$$
分布在组计数上的未归一权为
$$
\binom{50}{p}\binom{50}{s_0}
\frac{(5/4)^p(5/6)^{s_0}}{\binom{100}{r}}.
$$
乘以同一个正数 $4^{50}6^{50}100!$ 后，成为完全整数的权
$$
\boxed{
w_{p,s_0}=
\binom{50}{p}\binom{50}{s_0}
5^{p+s_0}4^{50-p}6^{50-s_0}
r!(100-r)!.
}
\tag{9.25}
$$
全部 $51^2=2601$ 个权都严格正。

分布与 $r^2$ 在两个组内的置换下不变。正交投影到原完整空间
$$
W=\operatorname{span}\{1,X_1,\ldots,X_{100}\}
$$
与这些置换交换。因此 $P_Wr^2$ 必在固定子空间
$$
W^{S_{50}\times S_{50}}=\operatorname{span}\{1,r,d\}.
$$
对 $rt$ 也是同样的论证。这是原完整投影的对称化，并没有把回归空间擅自缩为 $\operatorname{span}\{1,r\}$。

下面给出精确有理证书所用的全部公式。求和均遍历 (9.25) 的 2601 个状态。令
$$
Z_0=\sum w,\qquad
M=\sum w\,bb^{\mathsf T},\qquad
c=\sum w\,r^2b,\qquad
\Delta=\det M,\qquad J=\operatorname{adj}M.
$$
$M$ 严格正，因为 $1,r,d$ 在这些状态上线性无关。将 $M^{-1}c$ 写成具有正公共分母的有理向量
$$
M^{-1}c=\frac{B}{d_0},\qquad d_0>0,\qquad B\in\mathbb Z^3.
$$
定义
$$
T=d_0r^2-B^{\mathsf T}b,\quad
S_2=\sum wT^2,\quad
S_{\rm edge}=\sum wr(100-r)T^2,
$$
$$
v_0=\sum wrTb,\qquad
E=v_0^{\mathsf T}Jv_0,\qquad
A_1=\Delta S_{\rm edge}+101E.
\tag{9.26}
$$
由回归方程，准确有 $\sum wTb=0$。于是原残差是 $t=T/d_0$，而不是一个另外选取的测试函数。式 (9.16)、(9.19) 给
$$
\boxed{
\tau_{\rm quad}
=\frac{100\Delta S_2^2}
{101Z_0d_0^2A_1}.
}
\tag{9.27}
$$
这里 $S_2,S_{\rm edge},E,A_1$ 均严格正。

置
$$
m_1=M_{01},\qquad m_2=M_{11},
$$
$$
R_0=
102(Z_0m_2-m_1^2)
-(m_1+Z_0)(101Z_0-m_1).
$$
真实必要阈值等于
$$
\boxed{
\tau_{\rm req}
=\frac{102\,\operatorname{Var}(r)
-(\mathbb Er+1)(101-\mathbb Er)}
{101\cdot102}
=\frac{R_0}{101\cdot102\,Z_0^2}.
}
\tag{9.28}
$$
故差值的分子、正分母分别为
$$
N=
100\cdot102\,Z_0S_2^2\Delta-R_0d_0^2A_1,
$$
$$
D=
101\cdot102\,Z_0^2d_0^2A_1>0.
\tag{9.29}
$$

独立可执行的 BigInt 证书按以上整数式直接构造所有状态、回归矩阵、伴随矩阵和残差，不使用浮点数判符号。它核验：
$$
M J=\Delta I,\qquad
\sum wTb=0,\qquad
R_0>0,\qquad D>0,
$$
并得到
$$
\boxed{
40N+D>0,\qquad 50N+D<0.
}
$$
因此
$$
\boxed{
-\frac1{40}
<\tau_{\rm quad}-\tau_{\rm req}
<-\frac1{50}<0.
}
\tag{9.30}
$$
作为便于辨认的十进制显示，
$$
\tau_{\rm quad}\approx5.998068659520,\qquad
\tau_{\rm req}\approx6.022600722698.
$$
这些十进制数不参与证书的逻辑；严格符号完全来自 (9.30) 的整数比较。

完整的[独立 BigInt 证书](2026-11-13-six-moment-rayleigh-two-cluster-counterexample-central-review.mjs)只依赖标准 JavaScript，可用 node 直接运行。root 与 central_review 已分别实际执行并得到 PASS；严格符号由整数比较决定，十进制数仅供显示。原稿证书 blob 为 009a6a2a154269db24e2a0da51cefd92b8248b9d。

所以，§9.7 的异权自动成立命题现已被精确排除。§9.6 仍是正确的充分判据，但对一般异权必须保留完整的 $\tau$，或给出比单个 $t$ 的 Rayleigh 下界更强的修正。尤其不能把 (9.30) 换称为原相邻 Gram 序的反例：本节没有计算 $S^{-1}$ 在整个 $QH$ 上的二次型。


### 9.9 高度二的内部平衡变分与完整修正项

本节只取
$$
L=q\ge2,\qquad h=2,\qquad n=1,
\qquad
\mu_R=\frac{A_R}{Z\binom q{|R|}},
\quad A_i>0.
$$
沿用 §9 的真实空间
$$
W=\operatorname{span}\{1,X_1,\ldots,X_q\},\quad
P=P_W,\quad Q=I-P,\quad t=Qr^2,
$$
以及
$$
S=Qr(q-r)Q+(q+1)C^*C,\qquad C=PrQ.
$$
这里不以单个 $t$ 的 Rayleigh 值代替完整逆。准确有
$$
\tau=\frac q{q+1}\langle t,S^{-1}t\rangle.
$$

#### 9.9.1 两个端点的唯一补齐

记内部状态集合
$$
\mathcal I=\{R:0<r=|R|<q\},
$$
并在其上定义未归一正测度及两个概率向量
$$
\nu_R=\mu_Rr(q-r),\qquad
u_i(R)=\frac{X_i(R)}r,\qquad
v_i(R)=\frac{1-X_i(R)}{q-r}.
\tag{9.31}
$$
因此 $\sum_i u_i=\sum_i v_i=1$。记 $\mu_0=\mu_\varnothing>0$、
$\mu_q=\mu_{\{1,\ldots,q\}}>0$。

给定内部复函数 $f_{\mathcal I}$，若要补成一个满足
$\mathbb E_\mu f=\mathbb E_\mu(rf)=0$ 的全函数，两个端点必且只可能取
$$
f(q)=-\frac{\sum_{\mathcal I}\mu_Rr f_{\mathcal I}(R)}
{q\mu_q},
\qquad
f(0)=-\frac{\sum_{\mathcal I}\mu_R(q-r)f_{\mathcal I}(R)}
{q\mu_0}.
\tag{9.32}
$$
把 (9.32) 代入其余 $q$ 个坐标正交条件，得到
$$
\mathbb E_\mu(X_i f)=
\sum_{\mathcal I}\mu_R\left(X_i-\frac rq\right)f_{\mathcal I}.
$$
又
$$
\nu_R(u_i-v_i)=q\mu_R\left(X_i-\frac rq\right).
$$
所以限制到内部与端点补齐，给出准确线性双射
$$
\boxed{
QH\ \longleftrightarrow\
\mathcal B:=
\{f_{\mathcal I}\in L^2(\nu):
\mathbb E_\nu[f_{\mathcal I}(u-v)]=0\}.
}
\tag{9.33}
$$
这不是等距识别；端点可能具有很大的函数值。下文只在准确的 $S$ 能量里使用此双射，没有删去原 Hilbert 空间的端点范数。

#### 9.9.2 源与全部一次投影在内部的准确表达式

令
$$
\Sigma=\operatorname{Cov}_\mu(X)>0.
$$
严格正性来自全部布尔状态有正概率，故任何非常数一次函数都有严格正方差。对 $f_{\mathcal I}\in\mathcal B$ 定义
$$
g=\mathbb E_\nu(f_{\mathcal I}v)
 =\mathbb E_\nu(f_{\mathcal I}u)\in\mathbb C^q.
$$
(9.32) 直接给
$$
\mathbb E_\mu(r^2f)
=-\mathbb E_\nu f_{\mathcal I}
=-\mathbf1^{\mathsf T}g,
$$
$$
\mathbb E_\mu(rf)=0,\qquad
\mathbb E_\mu(X_i r f)=-g_i.
\tag{9.34}
$$
因此 $P(rf)$ 的常数均值为零，其余部分在中心化坐标
$X_i-\mathbb E_\mu X_i$ 中的系数为 $-\Sigma^{-1}g$，准确有
$$
\|P(rf)\|_\mu^2=g^*\Sigma^{-1}g.
$$
另一方面 $r(q-r)$ 在两端为零。故
$$
\langle Sf,f\rangle_\mu
=\mathbb E_\nu|f_{\mathcal I}|^2
 +(q+1)g^*\Sigma^{-1}g.
$$
由正算子逆的变分公式，得到
$$
\boxed{
\tau=\frac q{q+1}
\sup_{\substack{f_{\mathcal I}\in\mathcal B\\f_{\mathcal I}\ne0}}
\frac{|\mathbf1^{\mathsf T}g|^2}
{\mathbb E_\nu|f_{\mathcal I}|^2
 +(q+1)g^*\Sigma^{-1}g},
\qquad
g=\mathbb E_\nu(f_{\mathcal I}v).
}
\tag{9.35}
$$
分母严格正。式中保留全部 $q-1$ 个独立平衡约束和真实的
$\Sigma^{-1}$；仅知道 $\sum_i u_i=\sum_i v_i=1$ 不足以删去这些条件。

#### 9.9.3 一个不使用端点小逆的有限特征公式

在 $L^2(\nu)$ 中令
$$
\mathcal A_0=\operatorname{span}\{u_i-v_i:1\le i\le q\},
\qquad
\Pi_0=P_{\mathcal A_0},
\qquad
\widetilde v_i=(I-\Pi_0)v_i.
$$
则 $\mathcal B=\mathcal A_0^\perp$。定义正半定矩阵
$$
K_{ij}=\mathbb E_\nu(\widetilde v_i\widetilde v_j).
$$
它可以直接由有限特征 Gram 求得。若
$$
A_0=\mathbb E_\nu[(u-v)(u-v)^{\mathsf T}],\quad
B_0=\mathbb E_\nu[v(u-v)^{\mathsf T}],\quad
V_0=\mathbb E_\nu[vv^{\mathsf T}],
$$
则
$$
K=V_0-B_0A_0^\dagger B_0^{\mathsf T}.
\tag{9.36}
$$
$A_0^\dagger$ 是真实正半定矩阵的 Moore–Penrose 逆。
$\ker A_0=\operatorname{span}\{\mathbf1\}$：一方面坐标和恒为零，另一方面只看所有单点状态，就已强制核向量的各坐标相等。故这里恰消去 $q-1$ 个独立约束。

变分式 (9.35) 中，函数正交于所有 $\widetilde v_i$ 的部分只增加分母，所以可完整删去。令算子 $V:\mathcal B\to\mathbb C^q$ 为
$Vf=\mathbb E_\nu(fv)$；则 $VV^*=K$。应用有限秩逆恒等式，得到
$$
\boxed{
\tau=\frac q{q+1}\,
\mathbf1^{\mathsf T}
\left[
K-K\left(K+\frac{\Sigma}{q+1}\right)^{-1}K
\right]\mathbf1.
}
\tag{9.37}
$$
中间逆始终存在，因为 $\Sigma>0$。不需要假设 $K$ 可逆；例如 $q=2$ 时 $K$ 可以秩亏。式 (9.37) 与 (9.35) 是同一个完整 $\tau$，而不是另一项充分下界。

#### 9.9.4 外场换位结构与尚未支付的比较

上述内部测度保留原模型的准确比率。若 $i\in R,j\notin R$，则
$$
\frac{\nu_{R-\{i\}+\{j\}}}{\nu_R}=\frac{A_j}{A_i},
\qquad
\frac{\nu_{R^c}}{\nu_R}=\frac{\prod_i A_i}{A_R^2}.
\tag{9.38}
$$
对一个平衡函数，可定义矩阵
$$
J_f=\mathbb E_\nu(f\,u v^{\mathsf T}).
$$
它的行和与列和都等于 $g$；这只是 (9.33) 的等价写法。
$f$ 可以是复函数，所以这里不能免费把 $J_f$ 当成非负流或概率耦合。

本节把完整修正转成有全部成本的内部平衡问题，并移除了原端点值的显式小分母。它没有证明
$\tau\ge\tau_{\rm req}$，也没有在 (9.37) 中交换不相容矩阵的顺序。下一步仍须利用 (9.38) 的外场结构，或者在 (9.35) 中构造满足全部平衡约束且费用足够的真实测试。
