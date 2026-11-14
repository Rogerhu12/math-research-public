# R239 附录：两组任意重数加一异常位的高度四完整相邻比较

- 日期：2026-11-13。
- 作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。
- 状态：整个高度四的全部完整相邻比较已证明；更高高度和任意有限权仍需继续，普通 ISP 未完成。
- 精确整数证书：[独立整数证书](../notes/2026-11-13-two-weight-groups-one-exceptional-height-four-certificate-0c.mjs)（[完整输出](../notes/2026-11-13-two-weight-groups-one-exceptional-height-four-certificate-0c.json)）；完整物理 MP 核验：[独立满层 MP 核验](../notes/2026-11-13-two-weight-groups-one-exceptional-height-four-full-mp-check-0c.py)。
- 输入：[全高度二维 shear](R239-appendix-two-weight-groups-one-exceptional-full-shear-and-height-two-bound.md)、[高度三全重数证书](R239-appendix-two-weight-groups-one-exceptional-full-height-three-bound.md)、[两权全高度严格比较](R239-appendix-two-weight-groups-all-heights-strict-primitive-gram-bound.md)、[真实倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)、[任意头饱和固定线](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md) §8。

## 1. 真实完整逆与四个必要比较

对两个共同权组分别作完整正交升降串分解，保留全部出生和重数。在每个三串块上，较短普通串长度记为 $m$，较长长度 $L\ge m$，异常串长度为一；较长串权归一化为一，其余两个权平方记为 $z,w>0$。

二维 primitive 的一般参数为 $t=m-\delta$、$L=m+h-1-2\delta$、$0\le\delta\le m-1$、$h\ge2\delta+1$。因此高度四恰有两族：
$$
\delta=0:\quad L=m+3,\ t=m,\ m\ge1;
\qquad
\delta=1:\quad L=m+1,\ t=m-1,\ m\ge2.
\tag{1.1}
$$
相邻阶 $n=1$ 和 $n=2$ 各需证明；$n=3$ 由真实倒数权对偶归入同族的 $n=1$，不另外丢弃最高逆。

始终定义 $F_n=D^n(D^*)^n/(n!)^2$，在整个出生层取逆，再压缩到 primitive。固定首一源坐标的真实 MP 矩阵为
$$
H_j[\alpha,\beta]=(a_j+w a_{j+1})|\alpha|^2+B_j|\beta-k_j\alpha|^2,
\tag{1.2}
$$
其中
$$
B_0=w b_0,\quad B_j=\frac{w b_{j-1}b_j}{b_{j-1}+wb_j}\ (1\le j<4),\quad B_4=b_3.
$$
$a_j$ 是同一个两串的高次首一最小范数，高度五；$b_j$ 是低次问题的范数，高度三；$k_j$ 是相邻高次最小多项式的次高系数之差。全部强制根、完整逆和真实源 Gram $H_0$ 由已有全高度 shear 定理支付。

对任何中阶 $n$，共同剪切使 $k_n=0$。令 $A_j=a_j+w a_{j+1}$，则
$$
K=H_{n-1}-H_nH_{n+1}^{-1}H_n
$$
满足
$$
K_{11}=A_{n-1}-A_n^2/A_{n+1}+B_{n-1}(k_{n-1}-k_n)^2>0.
\tag{1.3}
$$
严格性由旧两权全高度定理给 $a_j$ 的严格 log 凸性，再给正线性和 $A_j$ 的严格 log 凸性。因此所有新费用都准确集中在 $\det K>0$。

## 2. 两套通用四次式

### 2.1 硬端点 $n=1$

沿用高度三稿 §2 的完整恒等式。临时记
$$
a=a_0,\ b=a_1,\ c=a_2,\ d=a_3,
\quad p=b_0,\ q=b_1,\ r=b_2,
\quad x=k_0-k_1,\ y=k_2-k_1.
$$
则
$$
\det K=\frac{wP^{\rm b}(w)}{(p+wq)^2(c+wd)r},
\tag{2.1}
$$
$$
\begin{aligned}
P^{\rm b}={}&p\Lambda\{p(pr-q^2)+wpqr+w^2q^2r\}\\
&-wp^3q(c+wd)(q+wr)x^2-wp^2q^2r(a+wb)y^2\\
&-2wp^2qr(b+wc)(p+wq)xy-w^2p^3q^2r x^2y^2,
\end{aligned}
$$
$$
\Lambda=(ac-b^2)+w(ad-bc)+w^2(bd-c^2).
$$
若代入 $a=A,b=T_0/p,c=T_1/q,d=T_2/r$ 及 $x=X/(pq),y=Y/(pqr)$，三个中间系数为
$$
P^{\rm b}_1=N^{\rm b}_1/(qr),\quad
P^{\rm b}_2=N^{\rm b}_2/(pq^2r),\quad
P^{\rm b}_3=N^{\rm b}_3/q,
\tag{2.2}
$$
其中 $N^{\rm b}_i$ 正是高度三稿 (2.7)–(2.9) 的 9、14、6 项固定整数多项式，证书完整嵌入这些单项式。端系数
$$
P^{\rm b}_0=p^2(pr-q^2)(ac-b^2)>0,
\quad P^{\rm b}_4=prq^2(bd-c^2)>0
$$
由旧两权严格比较给出。

### 2.2 中央 $n=2$

现在记
$$
a=a_1,\ b=a_2,\ c=a_3,\ d=a_4,
\quad p=b_0,\ q=b_1,\ r=b_2,\ t=b_3,
\quad x=k_1-k_2,\ y=k_3-k_2.
$$
有限正 Gram 的直接二乘二展开给
$$
\boxed{\det K=\frac{wP^{\rm c}(w)}{(p+wq)(q+wr)^2(c+wd)t}.}
\tag{2.3}
$$
置
$$
F=pq(qt-r^2)+wqr(pt-qr)+w^2rt(pr-q^2).
$$
则准确四次多项式为
$$
\begin{aligned}
P^{\rm c}={}&q\Lambda F
-wpq^3r(c+wd)(r+wt)x^2
-wq^2r^2t(a+wb)(p+wq)y^2\\
&-2wpq^2rt(b+wc)(q+wr)xy-w^2pq^3r^2t x^2y^2.
\end{aligned}
\tag{2.4}
$$
端系数严格正：
$$
P^{\rm c}_0=pq^2(ac-b^2)(qt-r^2)>0,
\quad
P^{\rm c}_4=qrt(bd-c^2)(pr-q^2)>0.
\tag{2.5}
$$
用如下统一形式编码其余三项：
$$
a=A/p,\quad b=B/q,\quad c=C/r,\quad d=D/t,
\quad x=X/(pqr),\quad y=Y/(qrt).
\tag{2.6}
$$
清分母后
$$
N^{\rm c}_1=prt\,P^{\rm c}_1,\qquad
N^{\rm c}_2=pqr^2t\,P^{\rm c}_2,\qquad
N^{\rm c}_3=prt\,P^{\rm c}_3
\tag{2.7}
$$
都是固定的整数多项式，分别有 11、19、11 项。其完整定义是 (2.4)、(2.6)、(2.7) 的有限展开；证书逐单项式原样嵌入。例如
$$
\begin{aligned}
N^{\rm c}_1={}&ACpq^2rt^2-ACq^3r^2t+ADpq^3rt-ADpq^2r^3-AY^2pr\\
&-B^2p^2r^2t^2+B^2pqr^3t-BCp^2q^2t^2+BCp^2qr^2t
-2BXYpt-CX^2qt.
\end{aligned}
$$
这些是实际相邻矩阵式的恒等展开；不从全 Hankel 正性推导。

## 3. $\delta=0$ 的实际范数与两套代入

令 $Q=m+1$、$\Theta=z\partial_z$、$W=\sum_{j=0}^m z^j=(1-z^Q)/(1-z)$，并记
$$
T(f)=f\Theta^2f-(\Theta f)^2.
$$
定义
$$
\begin{aligned}
\Phi_0&=(Q-\Theta)(Q+1-\Theta)(Q+2-\Theta)W,\\
\Phi_1&=(1+\Theta)(Q-\Theta)(Q+1-\Theta)W,\\
\Phi_2&=(1+\Theta)(2+\Theta)(Q-\Theta)W,\\
\Phi_3&=(1+\Theta)(2+\Theta)(3+\Theta)W,
\end{aligned}
\tag{3.1}
$$
$$
A_0=\Theta(Q-\Theta)(Q+1-\Theta)(Q+2-\Theta)(Q+3-\Theta)W.
$$
将所有真实 Gram 同时乘正标量 $Q(Q+1)(Q+2)$ 后，准确有
$$
b_j=\Phi_j\ (0\le j\le3),\qquad
a_0=A_0,\quad a_j=T(\Phi_{j-1})/\Phi_{j-1}\ (1\le j\le4).
\tag{3.2}
$$
$a_0$ 带真实强制根 $j=0$；其后四个高次多项式是全支撑上的首一次最小多项式，次高系数分别为 $-\Theta\log\Phi_j$。最高 $a_5$ 带根 $j=m$，由原完整公式支付；在倒数对偶中完整保留。

边端代入为
$$
p=\Phi_0,\ q=\Phi_1,\ r=\Phi_2,\ A=A_0,
\quad T_0=T(p),\ T_1=T(q),\ T_2=T(r),
$$
$$
X=p\Theta q-2q\Theta p,
\qquad Y=2pr\Theta q-qr\Theta p-pq\Theta r.
\tag{3.3}
$$
中央代入为
$$
p=\Phi_0,\ q=\Phi_1,\ r=\Phi_2,\ t=\Phi_3,
\quad A=T(p),\ B=T(q),\ C=T(r),\ D=T(t),
$$
$$
X=qr\Theta p-2pr\Theta q+pq\Theta r,
\quad Y=2qt\Theta r-rt\Theta q-qr\Theta t.
\tag{3.4}
$$
两式均由真实次高系数差直接得到。

## 4. $\delta=1$ 的强制根与完整 Hankel 商

这里 $m\ge2$。定义
$$
F_0=(Q-\Theta)W,\qquad F_1=(1+\Theta)W,
$$
$$
V=\Theta(Q-\Theta)(Q+1-\Theta)W,
\qquad R=(Q-1-\Theta)(1+\Theta)(2+\Theta)W,
$$
$$
A_0=\Theta(\Theta-1)(Q-\Theta)(Q+1-\Theta)(Q+2-\Theta)W.
\tag{4.1}
$$
令 $T_i=T(F_i)$，$U_i=\det[\Theta^{a+b}F_i]_{a,b=0}^2$。$U_i$ 也是对应正离散权的三元 Vandermonde 平方和，故严格正。

将全 Gram 共同乘以 $Q$ 后，真实范数准确为
$$
b_0=V,\quad b_1=T_0/F_0,\quad b_2=T_1/F_1,\quad b_3=R,
$$
$$
a_0=A_0,\quad a_1=T(V)/V,\quad a_2=U_0/T_0,
\quad a_3=U_1/T_1,\quad a_4=T(R)/R.
\tag{4.2}
$$
真实强制根依次如下：$a_0$ 的多项式固定为 $j(j-1)$；$a_1$ 除去根 $j=0$ 后权为 $V$；$a_2,a_3$ 是完整支撑上的二次正交多项式；$a_4$ 除去根 $j=m$ 后权为 $R$。次高系数依次为
$$
-1,\ -\Theta\log V,\ -\Theta\log T_0,
\ -\Theta\log T_1,\ -m-\Theta\log R.
\tag{4.3}
$$
最高 $a_5$ 的两个强制根为 $m-1,m$，亦由完整原公式保留。这里的 $a_2,a_3$ 是 $U_i/T_i$，不能替换成一维试探费用。

### 4.1 边端代入及清分母

在边端通用多项式中取
$$
p=V,\ q=T_0/F_0,\ r=T_1/F_1,\ A=A_0,
\quad T_0^{\rm gen}=T(V),\ T_1^{\rm gen}=U_0/F_0,\ T_2^{\rm gen}=U_1/F_1,
$$
$$
X=X_{\rm b}/F_0,\quad Y=Y_{\rm b}/(F_0F_1),
$$
$$
X_{\rm b}=VT_0-2T_0\Theta V+V\Theta T_0,
\quad
Y_{\rm b}=2VT_1\Theta T_0-T_0T_1\Theta V-VT_0\Theta T_1.
\tag{4.4}
$$
对应的三个整数多项式为
$$
Z^{\rm b}_1=F_0^3F_1^2N^{\rm b}_1,\quad
Z^{\rm b}_2=F_0^4F_1^2N^{\rm b}_2,\quad
Z^{\rm b}_3=F_0^3F_1N^{\rm b}_3.
\tag{4.5}
$$
逐单项式检查，所有剩余 $F_0,F_1$ 幂均为非负整数。三个 $P_i^{\rm b}$ 的符号分别等于这三个多项式的符号，因为余下分母严格正。

### 4.2 中央代入及清分母

在中央通用式中取
$$
p=V,\ q=T_0/F_0,\ r=T_1/F_1,\ t=R,
\quad A=T(V),\ B=U_0/F_0,\ C=U_1/F_1,\ D=T(R),
$$
$$
X=X_{\rm c}/(F_0F_1),\qquad Y=Y_{\rm c}/(F_0F_1),
$$
$$
X_{\rm c}=T_0T_1\Theta V-2VT_1\Theta T_0+VT_0\Theta T_1,
$$
$$
Y_{\rm c}=2T_0R\Theta T_1-T_1R\Theta T_0-T_0T_1\Theta R-mT_0T_1R.
\tag{4.6}
$$
清分母多项式为
$$
Z^{\rm c}_1=F_0^3F_1^3N^{\rm c}_1,\quad
Z^{\rm c}_2=F_0^4F_1^4N^{\rm c}_2,\quad
Z^{\rm c}_3=F_0^3F_1^3N^{\rm c}_3.
\tag{4.7}
$$
同样，每个单项式的剩余清分母幂非负，故是准确整数多项式，而不是数值近似。

## 5. 全参数 Newton 证明的范围与次数

四个分支各有三个多项式：$\delta=0$ 直接取 $N_i^{\rm b},N_i^{\rm c}$，$\delta=1$ 取 (4.5)、(4.7)。生成式只使用 $W=(1-z^Q)/(1-z)$、整数多项式加乘及 $\Theta$。每个多项式准确具有
$$
D_m(z)=\frac{\sum_{\lambda,s}p_{\lambda,s}(Q)z^{\lambda Q+s}}{(1-z)^d},
\quad p_{\lambda,s}\in\mathbb Z[Q],\quad 0\le s\le d-1.
\tag{5.1}
$$
先验 $z$ 次数界为

| 分支 | $i=1$ | $i=2$ | $i=3$ |
|---|---:|---:|---:|
| $\delta=0$ 边端 | $8m-1$ | $10m-1$ | $7m-1$ |
| $\delta=0$ 中央 | $10m-1$ | $12m-1$ | $10m-1$ |
| $\delta=1$ 边端 | $13m-1$ | $16m-1$ | $11m-1$ |
| $\delta=1$ 中央 | $16m-1$ | $20m-1$ | $16m-1$ |

这些不是从有限 $m$ 插值得到的界。$\Phi_j,F_i,V,A_0$ 次数至多 $m$，$R$ 次数至多 $m-1$；$T(\Phi_j),T_i,T(V)$ 次数至多 $2m-1$，$T(R)$ 次数至多 $2m-3$；$U_i$ 次数至多 $3m-3$。各 $X,Y$ 的次数由其明确公式给出：$\delta=0$ 边端为 $2m,3m-1$，中央均为 $3m-1$；$\delta=1$ 边端为 $3m-1,5m-2$，中央为 $5m-2,5m-3$。逐单项式加上 (4.5)、(4.7) 的剩余 $F_i$ 幂，便得到上表。证书也以这些符号仿射次数逐项核对上界。

如果某列上界为 $Bm-1$，所有可能的 $z$ 指数均被
$$
k=jQ+u,\quad0\le j<B,\quad0\le u<Q
$$
覆盖。置 $v=Q-u-1\ge0$，每区的准确系数是
$$
\sum_{\lambda\le j,s}p_{\lambda,s}(u+v+1)
\binom{(j-\lambda)(u+v+1)+u-s+d-1}{d-1}.
\tag{5.2}
$$
$0\le s\le d-1$ 保证它在整个非负整数象限上是合法二项式多项式，先验总次数为 $d-1+\max\deg_Qp$。已知这个界后，对有限网格作精确二维前向差分给完整 Newton 恒等式。全部 Newton 系数非负，即证明所有整数 $m$ 的所有 $z$ 系数非负。

证书的实现缓存相同二项式值和 $p(Q)$ 值，并逐键累加稀疏乘积；这些仅改变重复运算次数，不改变 (5.1)、(5.2) 或任何整数系数。完整先验数据如下；$D=d-1+\deg_Qp$ 是计算有限网格前已经得到的界。

| 分支 | $i$ | $d$ | $\deg_Qp$ | $D$ | 区数 | 正 Newton 系数数 |
|---|---:|---:|---:|---:|---:|---:|
| $\delta=0$ 边端 | 1 | 36 | 22 | 57 | 8 | 4660 |
| $\delta=0$ 边端 | 2 | 44 | 26 | 69 | 10 | 8908 |
| $\delta=0$ 边端 | 3 | 32 | 18 | 49 | 7 | 3169 |
| $\delta=0$ 中央 | 1 | 44 | 27 | 70 | 10 | 8835 |
| $\delta=0$ 中央 | 2 | 52 | 32 | 83 | 12 | 15053 |
| $\delta=0$ 中央 | 3 | 44 | 27 | 70 | 10 | 8817 |
| $\delta=1$ 边端 | 1 | 46 | 24 | 69 | 13 | 12402 |
| $\delta=1$ 边端 | 2 | 56 | 30 | 85 | 16 | 22998 |
| $\delta=1$ 边端 | 3 | 40 | 21 | 60 | 11 | 7694 |
| $\delta=1$ 中央 | 1 | 56 | 29 | 84 | 16 | 23039 |
| $\delta=1$ 中央 | 2 | 68 | 36 | 103 | 20 | 43103 |
| $\delta=1$ 中央 | 3 | 56 | 29 | 84 | 16 | 23009 |

四支严格正系数总数依次为 16737、32705、43094、89151，合计 **181687**；全部其余 Newton 系数为零，负项总数为零。每一区的计数和完整生成过程均在独立证书中逐项断言。于是四支全部中间四次系数非负。

证书还从有限离散权列表独立作稠密整数多项式运算，用成对和三元 Vandermonde 平方和分别构造 $T$、$U$，核对完整稀疏分子恒等式；并逐单项式断言上面的符号次数界与清分母幂合法。另一个物理脚本直接构造完整三串 $D^n/n!$、输入范数和源 Gram，在两族各三个串长、$n=1,2$、$z=4,w=9$ 的共 12 个有理例上，核对真实满层逆的 $\det K$ 与两套四次式完全相等。这些独立检查校验实现；全参数证明仍由先验次数、完整分区及精确 Newton 恒等式支付。

## 6. 全 primitive 拼合

四个比较已经由 §5 支付，(2.1)–(2.7) 的端系数严格正和中间系数非负使每个实际 $z,w>0$ 上 $\det K>0$，与 (1.3) 合并给两个完整二维相邻矩阵严格序。真实倒数权对偶支付 $n=3$。

所有二维分支由 (1.1) 穷尽。相对真空分支以四个位的严格 Newton 不等式支付；某普通串为零时用旧两权全高度定理；最高一维出生 $t=m+1$ 强制长串长 $m+5$，准确用任意头饱和固定线，而不把含三个值的分支误称为两权。各组正交串、所有重数、短串、真实最高逆和源 Gram 都保留。因此整个高度四 $K_s$ 满足
$$
\boxed{\Gamma_n\Gamma_{n+1}^{-1}\Gamma_n\prec\Gamma_{n-1},\qquad n=1,2,3.}
$$
所有固定正权下均严格，未把有限族的结论外推到任意有限权、原连续尾或普通 ISP。
