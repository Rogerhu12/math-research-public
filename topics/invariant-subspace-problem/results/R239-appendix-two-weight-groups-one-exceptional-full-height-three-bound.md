# R239 附录：两组任意重数加一异常位的整个高度三 primitive 严格系数 1

- 日期：2026-11-13。
- 作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
- 状态：整个高度三的完整相邻比较已证明。更高高度、任意多个不同权及普通 ISP 不由本稿完成。
- 输入：[全高度二维 shear 与高度二](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)；[两组全高度严格比较](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)；[任意头饱和固定线](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md) §8；[真实倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)。
- 精确整数证书：[完整 BigInt 程序](../notes/2026-11-13-two-weight-groups-one-exceptional-height-three-certificate-0c.mjs) / [全部逐区输出](../notes/2026-11-13-two-weight-groups-one-exceptional-height-three-certificate-0c.json)。两支合计 26929 个严格正 Newton 系数，零个负系数；先验次数和全系数覆盖在 §5 证明。

## 1. 整个问题准确只剩两类二维块

分别对两个共同权组作完整正交升降串分解，保留全部组内出生和重数。对每个三串块，记较短普通串长度为 $m$，较长普通串长度为 $L\ge m$，异常串长度为一。归一化长串权为一，短串和异常位权平方分别为 $z,w>0$。

二维 primitive 的参数是
$$
t=m-\delta,\qquad L=m+h-1-2\delta,
\qquad 0\le\delta\le m-1,\quad h\ge2\delta+1.
$$
因此 $h=3$ 时恰好有
$$
(\delta,L,t)=(0,m+2,m),\quad m\ge1;
\qquad
(\delta,L,t)=(1,m,m-1),\quad m\ge2.
\tag{1.1}
$$
我们只需证明相邻阶 $n=1$。已付真实倒数权对偶把 $n=2$ 与倒数权模型的 $n=1$ 作同一个源空间合同，倒数权仍属于 (1.1) 的相同组长族。它保留完整逆和源 Gram，不是仅比较行列式。

以下一直使用完整层
$$
F_n=D^n(D^*)^n/(n!)^2
$$
先取逆后压缩。源坐标为旧全高度稿的首一坐标 $\alpha,\beta$；真实源 Gram 是 $H_0$，并未置为单位矩阵。需证明
$$
K=H_0-H_1H_2^{-1}H_1\succ0.
\tag{1.2}
$$
源归一化的公共合同再给原 $\Gamma$ 不等式。

## 2. 端点相邻比较的通用四次恒等式

旧全高度 shear 公式给
$$
H_j[\alpha,\beta]=A_j|\alpha|^2+B_j|\beta-k_j\alpha|^2,
$$
$$
A_j=a_j+w a_{j+1},\qquad
B_0=w b_0,\quad
B_1=\frac{w b_0b_1}{b_0+w b_1},\quad
B_2=\frac{w b_1b_2}{b_1+w b_2}.
\tag{2.1}
$$
这里 $a_0,\ldots,a_4$ 是同一两串的高次首一最小范数，高度为四；$b_0,b_1,b_2$ 是低次问题的范数，高度为二。全部真实强制根已包含在这些范数中。

本节临时记
$$
a=a_0,\ b=a_1,\ c=a_2,\ d=a_3,
\qquad p=b_0,\ q=b_1,\ r=b_2,
$$
$$
x=k_0-k_1,\qquad y=k_2-k_1.
$$
这里的 $q$ 只是 $b_1$ 的代号，不是串长。对源共同剪切使 $k_1=0$ 后，二乘二展开准确给
$$
\boxed{
\det K=\frac{w\,P(w)}{(p+wq)^2(c+wd)r}.
}
\tag{2.2}
$$
其中
$$
\Lambda=(ac-b^2)+w(ad-bc)+w^2(bd-c^2),
$$
$$
F=p(pr-q^2)+wpqr+w^2q^2r,
$$
$$
\begin{aligned}
P(w)={}&p\Lambda F
-wp^3q(c+wd)(q+wr)x^2
-wp^2q^2r(a+wb)y^2\\
&-2wp^2qr(b+wc)(p+wq)xy
-w^2p^3q^2r x^2y^2.
\end{aligned}
\tag{2.3}
$$
这一恒等式可直接把 (2.1) 代入 $K$ 后清分母验证，没有端点无穷 Gram。若写 $P=\sum_{i=0}^4P_iw^i$，两端系数为
$$
P_0=p^2(pr-q^2)(ac-b^2)>0,
\quad
P_4=prq^2(bd-c^2)>0.
\tag{2.4}
$$
严格性由已经证明的两个旧两权范数序列的严格 log 凸性给出。

同样，$A_j=a_j+w a_{j+1}$ 严格 log 凸，所以旧 shear 展开的第一对角元
$$
K_{11}=A_0-A_1^2/A_2+B_0(k_0-k_1)^2
$$
严格正。故只需证明 $P_1,P_2,P_3\ge0$，便得到 $P(w)>0$、$\det K>0$ 及全部矩阵严格序。

为同时编码两个分支，写
$$
a=A,\quad b=T_0/p,\quad c=T_1/q,\quad d=T_2/r,
\qquad x=X/(pq),\quad y=Y/(pqr).
\tag{2.5}
$$
直接展开 (2.3) 得
$$
P_1=N_1/(qr),\qquad P_2=N_2/(pq^2r),\qquad P_3=N_3/q,
\tag{2.6}
$$
其中以下三个有限多项式固定，不依赖分支：
$$
\begin{aligned}
N_1={}&AT_1p^2qr^2+AT_2p^3qr-AT_2p^2q^3-AY^2q\\
&-T_0^2q^2r^2-T_0T_1p^2r^2+T_0T_1pq^2r
-2T_0XYr-T_1X^2pr;
\end{aligned}
\tag{2.7}
$$
$$
\begin{aligned}
N_2={}&AT_1p^2q^3r^2+AT_2p^3q^3r-T_0^2q^4r^2
-T_0T_1p^2q^2r^2\\
&+T_0T_2p^3q^2r-T_0T_2p^2q^4-2T_0XYq^2r-T_0Y^2q^2\\
&-T_1^2p^4r^2+T_1^2p^3q^2r-T_1X^2p^2r^2
-2T_1XYp^2r-T_2X^2p^2q^2-X^2Y^2;
\end{aligned}
\tag{2.8}
$$
$$
N_3=AT_2pq^3-T_0T_1q^2r+T_0T_2pq^2-T_1^2p^2r-2T_1XY-T_2X^2p.
\tag{2.9}
$$

## 3. 相差二的普通串：$\delta=0,L=m+2$

令 $Q=m+1$、$\Theta=z\partial_z$、$W=\sum_{j=0}^m z^j=(1-z^Q)/(1-z)$。对任意有限正权多项式定义
$$
T(f)=f\Theta^2 f-(\Theta f)^2.
$$
在 (2.5) 中取
$$
p=(Q-\Theta)(Q+1-\Theta)W,
\quad q=(1+\Theta)(Q-\Theta)W,
\quad r=(1+\Theta)(2+\Theta)W,
$$
$$
A=\Theta(Q-\Theta)(Q+1-\Theta)(Q+2-\Theta)W,
\qquad T_0=T(p),\ T_1=T(q),\ T_2=T(r),
\tag{3.1}
$$
$$
X=p\Theta q-2q\Theta p,
\qquad Y=2pr\Theta q-qr\Theta p-pq\Theta r.
\tag{3.2}
$$
这些表达式都是 $z$ 的有限整数多项式。这里把所有原 Gram 同时乘以正标量 $Q(Q+1)$，不改变 (1.2) 的符号。直接消真实二项式分母，旧低次范数恰为 $p,q,r$，而旧高次范数为
$$
a_0=A,\quad a_1=T(p)/p,\quad a_2=T(q)/q,\quad a_3=T(r)/r.
$$
$a_0$ 的强制根为 $r_{\rm miss}=0$，其多项式固定为缺失数本身，所以有限权确为 $j(Q-j)(Q+1-j)(Q+2-j)$。其余三个高次最小多项式都是全合法支撑上的首一次正交多项式，次高系数分别为 $-\Theta\log p,-\Theta\log q,-\Theta\log r$。第零阶的次高系数为零。因此
$$
x=\Theta\log q-2\Theta\log p,
\qquad y=2\Theta\log q-\Theta\log p-\Theta\log r,
$$
准确恢复 (3.2)，包括真正的硬端点。

§5 将证明按 (3.1)–(3.2) 代入后的 $N_1,N_2,N_3$ 全部具有非负 $z$ 系数。

## 4. 等长普通串：$\delta=1,L=m$

仍用 $Q=m+1,W=\sum_{j=0}^m z^j$，现在 $m\ge2$。置
$$
V=\Theta(Q-\Theta)W,
\qquad R=(Q-1-\Theta)(1+\Theta)W,
$$
$$
A=\Theta(\Theta-1)(Q-\Theta)(Q+1-\Theta)W,
\qquad T=T(W).
\tag{4.1}
$$
令 $U$ 为三阶 Hankel 行列式
$$
U=\det[\Theta^{i+j}W]_{i,j=0}^2
=\sum_{0\le i<j<k\le m}(j-i)^2(k-i)^2(k-j)^2z^{i+j+k}>0.
\tag{4.2}
$$
真正旧范数为
$$
b_0=V,\quad b_1=T/W,\quad b_2=R,
$$
$$
a_0=A,\quad a_1=T(V)/V,\quad a_2=U/T,\quad a_3=T(R)/R.
\tag{4.3}
$$
这些公式保留全部强制根：$a_0$ 的首一多项式是 $j(j-1)$；$a_1$ 带强制根 $j=0$，除根后权为 $V$ 的系数；$a_2$ 是完整支撑上的首二次正交多项式；$a_3$ 带强制根 $j=m$，除根后权为 $R$ 的系数。四个次高系数依次为
$$
-1,\quad-\Theta\log V,\quad-\Theta\log T,\quad-m-\Theta\log R.
\tag{4.4}
$$
所以
$$
x=1-2\Theta\log V+\Theta\log T,
\qquad y=2\Theta\log T-\Theta\log V-\Theta\log R-m.
$$

为了使用固定多项式 (2.7)–(2.9)，取
$$
p=V,\quad q=T/W,\quad r=R,
\quad T_0=T(V),\quad T_1=U/W,\quad T_2=T(R),
$$
$$
X=X_0/W,\qquad Y=Y_0/W,
\tag{4.5}
$$
$$
X_0=VT-2T\Theta V+V\Theta T,
$$
$$
Y_0=2VR\Theta T-TR\Theta V-VT\Theta R-mVTR.
\tag{4.6}
$$
这里没有把 $T_1$ 误当成 $T(q)$：真实 $a_2b_1=U/W$ 来自完整 Hankel 商。

定义精确多项式
$$
\widetilde N_1=W^3N_1,\qquad
\widetilde N_2=W^4N_2,\qquad
\widetilde N_3=W^3N_3,
\tag{4.7}
$$
其中 $N_i$ 按 (4.5) 代入。每个单项式的 $W$ 分母次数不超过 (4.7) 的次数，故这些是有限整数多项式。相应系数准确为
$$
P_1=\frac{\widetilde N_1}{W^2TR},\quad
P_2=\frac{\widetilde N_2}{W^2VT^2R},\quad
P_3=\frac{\widetilde N_3}{W^2T}.
\tag{4.8}
$$
分母均严格正。§5 证明三个分子全部具有非负 $z$ 系数。

## 5. 六个全 $m$ 正性证书及完整覆盖

令 $D_i^{(0)}=N_i$ 表示 §3 的分子，$D_i^{(1)}=\widetilde N_i$ 表示 §4 的分子。证书从 $W=(1-z^Q)/(1-z)$、整数多项式乘法和 $\Theta$ 运算准确生成
$$
D_i^{(\delta)}(z)=
\frac{\sum_{\lambda,s}p_{\delta,i,\lambda,s}(Q)z^{\lambda Q+s}}{(1-z)^d},
\qquad p_{\delta,i,\lambda,s}\in\mathbb Z[Q].
\tag{5.1}
$$
所有非零项都有 $s\ge0$，且 $s\le d-1$。先验数据为

| $\delta$ | $i$ | 分母次 $d$ | 分子 $Q$ 次数 | Newton 先验总次数 | 系数分区数 $B$ |
|---|---:|---:|---:|---:|---:|
| 0 | 1 | 28 | 16 | 43 | 8 |
| 0 | 2 | 34 | 20 | 53 | 10 |
| 0 | 3 | 25 | 14 | 38 | 7 |
| 1 | 1 | 31 | 14 | 44 | 11 |
| 1 | 2 | 38 | 18 | 55 | 14 |
| 1 | 3 | 28 | 13 | 40 | 10 |

先说明这些区数确实覆盖全部 $z$ 系数。§3 的 $p,q,r,A$ 次数至多 $m$；$T(p),T(q),T(r)$ 次数至多 $2m-1$；$X$ 次数至多 $2m$，$Y$ 的最高 $3m$ 项由 $2-1-1=0$ 相消，故次数至多 $3m-1$。逐项检查 (2.7)–(2.9) 得
$$
\deg D_1^{(0)}\le8m-1,\quad
\deg D_2^{(0)}\le10m-1,\quad
\deg D_3^{(0)}\le7m-1.
\tag{5.2}
$$

§4 中 $W,V,A$ 次数至多 $m$，$R$ 次数至多 $m-1$，$T$ 次数至多 $2m-1$，$U$ 次数至多 $3m-3$，$T(V)$ 次数至多 $2m-1$，$T(R)$ 次数至多 $2m-3$，$X_0$ 次数至多 $3m-1$，$Y_0$ 次数至多 $4m-2$。将每一项乘以 (4.7) 所需的剩余 $W$ 幂后，直接给
$$
\deg D_1^{(1)}\le11m-1,\quad
\deg D_2^{(1)}\le14m-1,\quad
\deg D_3^{(1)}\le10m-1.
\tag{5.3}
$$
这些上界可以宽于真实次数，但绝不漏项。因为 $Q=m+1$，$0\le k\le Bm-1$ 的每个指数都落在某个
$$
k=jQ+u,\qquad 0\le j<B,\quad 0\le u<Q.
$$
置 $v=Q-u-1\ge0$，即 $Q=u+v+1$。在每个固定分区，准确系数为
$$
C_{\delta,i,j}(u,v)=
\sum_{\lambda\le j,s}p_{\delta,i,\lambda,s}(u+v+1)
\binom{(j-\lambda)(u+v+1)+u-s+d-1}{d-1}.
\tag{5.4}
$$
$\lambda>j$ 的项本来为零。$\lambda\le j$ 时，$s\le d-1$ 保证二项式上标非负；低于 $d-1$ 的上标使二项式多项式准确取零。因此每个 (5.4) 都是整个非负整数象限上的多项式，总次数预先不超过表中 $D=d-1+\deg_Qp$。

次数上界已知后，有限 Newton 恒等式为
$$
C(u,v)=\sum_{a,b=0}^{D}(\Delta_u^a\Delta_v^bC)(0,0)\binom ua\binom vb.
\tag{5.5}
$$
证书只用 BigInt 从 (5.4) 的 $(D+1)^2$ 网格算前向差分，逐项断言 Newton 系数非负。各区的正系数计数为

| 分支 | $i$ | 依次各区的正系数数目 |
|---|---:|---|
| $\delta=0$ | 1 | 231, 405, 405, 405, 403, 401, 390, 144 |
| $\delta=0$ | 2 | 338, 594, 594, 594, 594, 592, 591, 587, 570, 209 |
| $\delta=0$ | 3 | 171, 324, 324, 323, 321, 313, 126 |
| $\delta=1$ | 1 | 180, 484, 492, 493, 493, 493, 490, 487, 477, 440, 108 |
| $\delta=1$ | 2 | 225, 721, 734, 738, 738, 738, 738, 736, 735, 731, 724, 708, 641, 126 |
| $\delta=1$ | 3 | 111, 394, 402, 403, 403, 400, 397, 387, 350, 63 |

总数分别为 9949 和 16980，合计 26929；其余 Newton 系数为零。于是所有非负整数 $u,v$ 上的全部分区系数非负，证明全部合法 $m$ 的六个分子都有非负 $z$ 系数。证书也检查形式退化的更小 $m$ 点；这不把无 primitive 的退化点纳入物理定理。

为独立检查生成式，程序从有限权列表直接作稠密整数多项式运算，$T$ 用成对 Vandermonde 平方和，$U$ 用三元 Vandermonde 平方和；在 $\delta=0,m=1,2,5$ 及 $\delta=1,m=2,3,5$ 核对完整分子恒等式。全 $m$ 证明依靠 (5.1)–(5.5) 的先验次数及精确 Newton 表，这些独立有限核对只检验实现。

## 6. 严格性、倒数对偶与整个 $K_s$

由 §5，$P_1,P_2,P_3\ge0$。由 (2.4)，$P_0,P_4>0$。因此任意固定 $z,w>0$ 均有 $P(w)>0$，(2.2) 给 $\det K>0$。§2 已付 $K_{11}>0$，故整个二维 $K\succ0$。倒数权对偶支付同一高度三块的 $n=2$ 比较，且保留公共源合同。

回到原模型，两个普通组的所有正交串都保留。二维分支完全由 (1.1) 穷尽。其余分支也全部支付：

- 相对真空出生：剩余三个位的完整 scalar Gram 为 elementary symmetric 函数的倒数，严格 Newton 不等式给每个相邻阶系数小于一；允许三个权均不同。
- 某普通串长度为零：模型退化为一个共同权组加一个异常位，旧全两权定理直接给严格比较。
- 最高一维出生 $t=m+1$：高度三强制 $L=m+4$。把普通短串与异常位一起看成任意正权头，准确由旧任意头饱和固定线及双侧常数支付；它仍可能有三个不同权，不能误引两权定理。

故对任意两个共同权组的有限重数、任意一个正异常权，以及整个高度三 primitive 空间，
$$
\boxed{
\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\prec\Gamma_{n-1},\qquad n=1,2.
}
$$
这是原始 $F_n=D^n(D^*)^n/(n!)^2$ 归一化下的真实完整逆比较；全部短串、重数、硬端点和源 Gram 已付。

更高高度的同一族可继续从完整 shear 四次式出发。任意有限权、原连续尾的实际返回费用和普通 ISP 仍开。
