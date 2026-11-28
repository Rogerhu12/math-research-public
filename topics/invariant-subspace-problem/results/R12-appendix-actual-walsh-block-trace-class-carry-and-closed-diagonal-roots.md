# 原 Haar Walsh 旗的全块秩一 carry、迹类双侧来源与闭块根

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。

本文只用原 Haar 各尾；$A^{(m)}$ 的上标是尾位编号，不是整数幂，也不是负整数边界表示。它给出新的实际全块表示及其精确来源费用。闭稳定根与原普通不变旗的接口见 [原旗/闭根定理](R12-appendix-all-ordinary-invariant-common-coordinate-flags-and-stable-closed-roots.md)。本文构造的是块对角压缩 $D$ 的闭根，尚未构造原 $A^{(m)}$ 的闭根。

## 1. 固定正交分解与全部原矩阵元

固定 $m_0\ge0$，写 $C=A^{(m_0)}$、$a_j=\alpha_{m_0+j}$，其中

$$
\alpha_j=\exp\!\left(-\frac{280}{3}16^j+90\,8^j-300\,2^j+\frac{850}{3}\right).
$$

在原 Haar 无穷张量积中，低位标准基为 $e_0,e_1$，令 $\Omega=(e_0+e_1)/\sqrt2$、$\chi=(e_0-e_1)/\sqrt2$。原尾满足

$$
A^{(k)}=\begin{pmatrix}0&A^{(k+1)}\\ \alpha_k I&0\end{pmatrix}.
\tag{1.1}
$$

$P_m$ 是依赖前 $m$ 位的柱函数空间投影；$P_0$ 是常数线投影。置 $Q_{-1}=P_0$、$Q_m=P_{m+1}-P_m$。在 $Q_mH$ 上使用真实正交基

$$
q_{m,k}=e_k^{(m)}\otimes\chi_m\otimes\Omega_{>m},
\qquad 0\le k<2^m,
$$

其中 $e_k^{(m)}$ 是按低位整数编号的归一柱指标。记 $u_m=q_{m,0}$、$v_m=q_{m,2^m-1}$；$u_{-1}=v_{-1}=\Omega$。

定义实际尾均值及其差

$$
\mu_j=\langle A^{(m_0+j)}\Omega,\Omega\rangle
=\sum_{\ell\ge0}2^{-\ell-1}a_{j+\ell},
\qquad
\delta_j=\frac{a_j-\mu_{j+1}}2.
$$

于是

$$
\mu_j=\frac{a_j+\mu_{j+1}}2,\quad
0<\delta_j<\mu_j,\quad
\frac{a_j}{2}\le\mu_j<a_j,\quad
\mu_j^2-\delta_j^2=a_j\mu_{j+1}.
\tag{1.2}
$$

令 $D_m=Q_mCQ_m$、$D=\bigoplus_{m\ge-1}D_m$。$D_{-1}=\mu_0$；$m\ge0$ 时，$D_m$ 是长度 $N=2^m$ 的完整加权循环块：

$$
D_mq_{m,k}=a_{v_2(k+1)}q_{m,k+1}\quad(k<N-1),
\qquad
D_mv_m=-\mu_m u_m.
\tag{1.3}
$$

全部非对角块 $K=C-D$ 恰为

$$
K_{mn}=2^{-|m-n|/2}\delta_{\max(m,n)}\,u_m v_n^*,
\qquad m,n\ge0,\ m\ne n,
\tag{1.4}
$$

以及

$$
K_{m,-1}=-2^{-m/2}\delta_m\,u_m\Omega^*,
\qquad
K_{-1,m}=+2^{-m/2}\delta_m\,\Omega v_m^*.
\tag{1.5}
$$

这里 $uv^*$ 表示 $x\mapsto u\langle x,v\rangle$；内积约定与此秩一记号一致。

证明：非末列原移位只改变低 $m$ 位，故没有跨块项。末列按 (1.1) 变成 $e_0^{(m)}\otimes A^{(m_0+m)}\chi$。其 $\chi$ 均值为 $-\mu_m$，$\Omega$ 均值为 $+\delta_m$。投到较低 $Q_n$ 时，每个夹层常数位给 $2^{-1/2}$，得到 (1.4) 的 $n<m$ 项。投到较高 $Q_n$ 时，输入 $\chi_m$ 的 wrap 系数为负，后面首个 $\chi_n$ 的均值系数也为负，两负相消，给同一正号。常数输入仅有后一个负号，常数输出仅有前述正均值，故得 (1.5)。这些计算也证明没有遗漏其余矩阵元。

## 2. 真实迹类 carry 与临界反馈

置 $t=2^{-1/2}$。每项 (1.4)–(1.5) 的迹范数就是其标量系数绝对值。因此整个秩一和绝对收敛，且

$$
\begin{aligned}
\|K\|_1
&\le
2\sum_{n\ge0}\delta_n
\left(t^n+\sum_{j=1}^n t^j\right)\\
&\le 2(1+\sqrt2)\sum_{n\ge0}\delta_n
\le(1+\sqrt2)\sum_{n\ge0}a_n<\infty.
\end{aligned}
\tag{2.1}
$$

这确是原 $C-D$，因为有限柱函数稠密，且所有矩阵元已经逐项同一化。特别 $D$ 有界、$\|D\|\le\|C\|$。

在每个实际尾的常数/首 Walsh 字符二维压缩中，矩阵准确为

$$
\begin{pmatrix}\mu_j&\delta_j\\-\delta_j&-\mu_j\end{pmatrix},
\qquad
\begin{pmatrix}\mu_j&\delta_j\\-\delta_j&-\mu_j\end{pmatrix}^{\!2}
=a_j\mu_{j+1}I.
\tag{2.2}
$$

由于 $\mu_{j+1}/a_j\to0$，

$$
\delta_j/\mu_j\longrightarrow1.
\tag{2.3}
$$

所以原跨块反馈相对于该层闭合均值不是小参数。迹类性本身不提供根方程所需的相对小量。

## 3. 循环平衡的准确费用

记

$$
\beta_{m,k}=\prod_{\ell=1}^k a_{v_2(\ell)},\quad
\beta_m=\beta_{m,2^m-1},\quad
p_m=\mu_m\beta_m,\quad r_m=p_m^{1/2^m}.
\tag{3.1}
$$

空积取 $1$。由 (1.3)，$D_m^{2^m}=-p_mI$。取对角矩阵

$$
Z_mq_{m,k}=\frac{\beta_{m,k}}{r_m^k}\,q_{m,k}.
$$

则 $D_m=r_m Z_m U_m Z_m^{-1}$，其中 $U_m$ 为末闭合 $-1$ 的酉循环移位。其条件数不是仅由低头乘积给出的较小指数，而恰为

$$
\boxed{\ \|Z_m\|\|Z_m^{-1}\|=\frac{r_m}{\mu_m}\ }.
\tag{3.2}
$$

证明这一等号需保前缀。令 $\ell_j=-\log a_j$。对 $1\le k<2^m$，

$$
-\frac1k\log\beta_{m,k}
=\ell_0+\sum_{j=1}^{m-1}\frac{\lfloor k/2^j\rfloor}{k}
(\ell_j-\ell_{j-1})
\le\ell_0+\sum_{j=1}^{m-1}2^{-j}(\ell_j-\ell_{j-1})
<-\log r_m.
$$

所以所有对角元至少 $1$。又 $v_2(2^m-\ell)=v_2(\ell)$，同一前缀估计应用于末段给全部对角元不超过最后一个；最后一个是 $\beta_m/r_m^{2^m-1}=r_m/\mu_m$。首、末元达到两端，证毕。

由原权的确切式及每级出现次数，

$$
-\log\beta_m
=\sum_{j=0}^{m-1}2^{m-1-j}(-\log a_j),
$$

故固定 $m_0$ 时

$$
-\log r_m=100\,16^{m_0}8^m+O_{m_0}(4^m+m+1),
\qquad
-\log\mu_m=\frac{280}{3}16^{m_0}16^m+O_{m_0}(8^m).
\tag{3.3}
$$

尤其任意固定 $\gamma>0$ 都有 $\sum_m r_m^\gamma<\infty$，而 (3.2) 的主损失仍是 $\exp((280/3)16^{m_0+m})$。

## 4. 真正闭稳定的块根及已付双侧来源

取 $R_{-1}=\sqrt{\mu_0}$、$R_0=i\sqrt{\mu_0}$。对 $m\ge1$，$N=2^m$ 为偶数，$D_m$ 的谱不在负实轴，令 $R_m$ 为其主平方根。它具有完整有限公式

$$
R_m=\sum_{j=0}^{N-1} h_{j,N}\,r_m^{1/2-j}D_m^j,
\qquad
h_{j,N}=\frac{(-1)^j}{N\sin(\pi(1/2-j)/N)}.
\tag{4.1}
$$

这是在 $\theta_k=(2k+1-N)\pi/N$ 上对 $e^{i\theta_k/2}$ 作离散 Fourier 插值；故确有 $R_m^2=D_m$，没有截掉末列。

定义

$$
R=\bigoplus_{m\ge-1}R_m,\qquad
\mathcal D(R)=
\left\{x:\sum_{m\ge-1}\|R_mQ_mx\|^2<\infty\right\}.
\tag{4.2}
$$

$R$ 稠密定义且闭，有限个整块构成图核心。并且

$$
R\mathcal D(R)\subset\mathcal D(R),\qquad
\mathcal D(R^2)=\mathcal D(R),\qquad
R^2x=Dx\quad(x\in\mathcal D(R)).
\tag{4.3}
$$

确因 $\sum_m\|R_m^2Q_mx\|^2=\sum_m\|D_mQ_mx\|^2\le\|C\|^2\|x\|^2$。

酉平衡与 (3.2) 给

$$
\|R_m\|\le r_m^{3/2}/\mu_m\qquad(m\ge0).
\tag{4.4}
$$

此损失确会出现：对 $m\ge1$，令 $N=2^m$，则

$$
\langle R_mu_m,v_m\rangle
=h_{N-1,N}\frac{r_m^{3/2}}{\mu_m},
\qquad
h_{N-1,N}=\frac1{N\sin(3\pi/(2N))}\ge\frac2{3\pi}.
\tag{4.5}
$$

由 (3.3)，这些矩阵元趋于无穷，故这里的 $R$ 确实无界。

尽管如此，原 carry 支付了两侧真实来源：

$$
\boxed{\ K H\subset\mathcal D(R),\quad RK\in\mathfrak S_1,\quad
KR|_{\mathcal D(R)}\text{ 有迹类的全域延拓}.\ }
\tag{4.6}
$$

一个共同迹范数上界为

$$
\sqrt{\mu_0}\sum_{m\ge0}\delta_m
+2(1+\sqrt2)\sum_{m\ge0}r_m^{3/2}.
\tag{4.7}
$$

证明：在第 $m\ge0$ 行，(1.4)–(1.5) 的系数绝对值和不超过 $2(1+\sqrt2)\mu_m$；因为 $\delta_n\le\mu_n\le\mu_m$ 对 $n>m$，而 $n<m$ 的系数全含 $\delta_m$。乘 (4.4) 后可和。常数行贡献不超过 (4.7) 第一项。列估计完全相同，使用 $\|R_n^*v_n\|\le\|R_n\|$。先对有限整块截断应用 $R$，再用 $R$ 闭性得到 $KH\subset\mathcal D(R)$ 与真实 $RK$；另一侧先在整块图核心同一化，再按图范数极限得到 (4.6)。这一步没有以形式矩阵代替实际定义域。

## 5. 同一实际右端的线性 Sylvester 修正仍无有界解

考察这一个特定 $R$ 的线性化方程

$$
RX+XR=K.
\tag{5.1}
$$

即使只要求各有限块满足
$R_mX_{mn}+X_{mn}R_n=K_{mn}$，也不存在有界矩阵 $X$。因此 (4.6) 不能自动升级为有界线性修正。

给出实际右端的精确证据。取 $n\ge2$，$N=2^n$、$m=n+1$，所以两块长度为 $N$、$2N$。两根的谱均在开右半平面，有限 Sylvester 解唯一。写

$$
c_j^{(s)}=h_{j,2^s}r_s^{1/2-j},\qquad
k=\delta_m/\sqrt2.
$$

乘 (5.1) 两侧的根并相减得

$$
D_mX_{mn}-X_{mn}D_n=R_mK_{mn}-K_{mn}R_n.
$$

把这个等式望远镜至 $2N$ 次，保 $D_m^{2N}=-p_mI$、$D_n^{2N}=p_n^2I$。取真实矩阵元 $x_n=\langle X_{mn}u_n,v_m\rangle$，只剩三项：

$$
x_n=
\frac{k\beta_m\beta_n}{p_m+p_n^2}
\left(c_{N-1}^{(n)}-c_{N-1}^{(m)}
+p_n c_{2N-1}^{(m)}\right).
\tag{5.2}
$$

此三项分别来自左边末列一次、右边 $N-1$ 次和 $2N-1$ 次；最后一次 $D_n^{2N-1}u_n=-p_n\beta_n v_n$ 的符号已包括在式中。

置 $\rho=r_m/r_n$、$q=\rho^N$、$\theta=3\pi/(4N)$。由 $\beta_m=a_n\beta_n^2$ 及 (1.2)，

$$
q^2=\frac{p_m}{p_n^2}
=\frac{a_n\mu_{n+1}}{\mu_n^2}
=1-\left(\frac{\delta_n}{\mu_n}\right)^2
\longrightarrow0.
\tag{5.3}
$$

(5.2) 的完整重写为

$$
x_n=
\frac{\delta_m}{\sqrt2\,\mu_m}\,
\frac{r_m^{3/2}}{\mu_n}\,
\frac{1}{2N\sin\theta}\,
\frac{1-q\tan\theta+\rho^{\,2N-3/2}/\cos\theta}{1+q^2}.
\tag{5.4}
$$

全部来源均是 (1.4) 的实际相邻 carry；没有换成任意最坏输入。对充分大的 $n$，$q\le1/2$、$\delta_m/\mu_m\ge1/2$，且 $\tan\theta<1$。故

$$
x_n\ge\frac{1}{12\pi\sqrt2}\frac{r_{n+1}^{3/2}}{\mu_n}.
\tag{5.5}
$$

而 (3.3) 给

$$
\log\frac{r_{n+1}^{3/2}}{\mu_n}
=\frac{280}{3}16^{m_0}16^n-O_{m_0}(8^n)
\longrightarrow+\infty.
$$

于是实际相邻块的一个矩阵元已经无界，证明 (5.1) 没有有界解。

## 6. 已闭范围与继续接口

本文支付了原 $C=D+K$ 的全块表示、实际迹类 $K$、闭稳定块根 $R$，以及 $RK$ 和 $KR$ 的真实迹类来源。它还精确关闭了对这一个块根直接求有界线性 Sylvester 修正的入口。

原根仍要求完整非线性等式

$$
RX+XR+X^2=K
$$

与实际域保持，或另一套相容根来源。第 5 节不否定非线性等式可能出现的同源抵消，不否定其他块根分支或其他闭稳定域，更不证明原候选没有普通不变子空间。本文没有把 $D$ 的根移作 $C$ 的根，也没有把迹类扰动本身当作普通 ISP 的桥。
