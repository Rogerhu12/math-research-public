# R916 — 原特殊零纤维的稳定核至多一维与唯一同源前缀测试

日期：2026-11-16。**状态：以下六系数限制、真实稳定核至多一维、全部十九角下的唯一候选和指定留数读取已证明。未判定剩余候选是否通过其真实前缀，也未判定指定 forcing；主目标仍未完成。**

本篇在 R907/R914 的同一个四块核中，处理准确的特殊零纤维
$F(0,Y)=\lambda Y^2(Y-1)$。
另保原常数 charge $F(t,0)$ 的零点阶为一或二。
这正包含 R797 移动常数因子次数至多二且零纤维如此的子类，
但不将该特殊形式赋给其它实际因子。

六维纤维算子的谱在此为 $0,1,\ldots,5$。
关键新增是同一个完整 $F^3$ 的这六个全局系数至多有一个恒零；
因此真正可无限续接的原核至多一维。
剩余方向的全十九角、完整值前缀和指定 GRes 都由同一个明确候选读取，
不能另选法向修正或任意给纯 charge 的系数。

## 1. 同一原格、实际窗口与特殊零纤维

保持 [R907](R907-original-two-step-successor-and-six-dimensional-fiber-feedback.md)、
[R914](R914-original-nonstable-kernel-eight-nine-step-cutoff-and-joint-rank.md)
的原十九角曲面、几何整曲线 $C=(F=0)$、$P=(0,1)$，及
$$
\mathcal H_j=H^0(X,\mathcal O_X(jC)),\quad
N=\mathcal O_C(C),\quad \kappa=C^2,\quad
\mathcal E=Y\partial_Y,\quad e=\mathcal EF,\quad
\gamma=e(P)\ne0.
\tag{1}
$$
只用已经支付同预算返回的
$$
q_{\rm src}t^r\mathcal H_3\subset\overline{\mathcal W_D}.
\tag{2}
$$
保持原 $r=2,\ C.f_0=3,\ b=\deg_YF\ge5,\ 3b<p,\ p>211$。
所有 charge 四十、原 $P_{134}/U_0$ 及物理 Euler 项仍按原完整单位运输；
$\mathcal E$ 是该运输后的相对算子。

令 $g=\psi\exp\eta$、$\operatorname{ord}\eta=h$，本篇取实际短窗
$$
\boxed{
h<T\le2h,\qquad T-h>\kappa,\qquad T-h\le L\le h,
\qquad T=s-r-13,\quad L=\max(\ell-r,0).
}
\tag{3}
$$
不扩大原读取长度。
实际四块核为
$$
K=\{G\in\mathcal H_3:
\mathcal E^jG(t,g)\in(t^T)\ (0\le j\le2),\
\mathcal E^3G(t,g)\in(t^L)\}.
\tag{4}
$$
记
$$
V_T=H^0(C,N^3(-TP)),\quad n_T=\dim_kV_T,\quad
R_C=3(e_++\mu_{0,1}),\quad e_+=C.H_+.
$$
R907 的原逐 charge 帽给 $R_C<T$；原 $b\ge5$、$T>2\kappa$
按 R819 的准确交数已保证此门。

本篇另有两个明确假设：
$$
\boxed{
F(0,Y)=\lambda Y^2(Y-1),\quad \lambda\in k^\times,
\qquad 1\le m:=\operatorname{ord}_tF(t,0)\le2.
}
\tag{5}
$$
$F(t,0)\ne0$ 是整个原函数域中的条件。
将 $F$ 除以常数 $\lambda$ 不改曲线、原角帽或反馈算子，
因为 $F^3$ 与 $\gamma^3$ 同时缩放；以下取 $\lambda=1$。

(5) 的第二个条件在下述已付子类中自动成立：
R792§6、R797§1 给同一个原因子
$$
F(t,0)=\lambda_0 d^{c_d}H(t),\qquad
d=1+8t,\quad 0\ne H,\quad \deg H\le2.
$$
若这个因子又满足 (5) 的零纤维，则 $H(0)=0$，而 $d(0)=1$，
故 $m=1$ 或 $2$。
这里只引用该来源分类已经适用的同一个 $F$；
不将旧 cube 的分类或新 quartic 的假设彼此偷换。
其余 profile、一般三次 $F(0,Y)$ 或 $m>2$ 不在本篇加强范围。

按 R907 定义
$$
a(G)=\frac{(\mathcal E^4G)(P)}{6\gamma^3},\qquad
\mathcal TG=\mathcal EG-a(G)F^3,
$$
$$
K_\infty=\{G\in K:\mathcal T^jG\in K\text{ 对所有 }j\ge0\}.
\tag{6}
$$
这是原真正稳定部分，未假设它等于整个 $K$。

## 2. 原 F³ 的六个全局系数至多一个恒零

写
$$
F=\sum_{j=0}^b A_j(t)Y^j,\qquad
a=A_0,\quad u=A_1,\quad v=A_2,\quad w=A_3.
$$
注意这里的 $a(t)$ 是常数 charge 系数，不是 (6) 的线性泛函 $a(G)$。
由 (5)，
$$
a(0)=u(0)=0,\quad v(0)=-1,\quad w(0)=1,\quad
A_4,A_5\in(t).
\tag{7}
$$
缺项按零处理。令
$$
C_n(t)=[Y^n]F^3.
$$
这与零纤维系数 $[Y^n]F(0,Y)^3$ 不同：
本节考察的是 $k[t]$ 中是否恒等于零。

精确展开给
$$
\begin{aligned}
C_0&=a^3,& C_1&=3a^2u,\\
C_2&=3a(av+u^2),&
C_3&=u^3+6auv+3a^2w,\\
C_4&=3a^2A_4+6auw+3av^2+3u^2v,\\
C_5&=3a^2A_5+6auA_4+6avw+3u^2w+3uv^2.
\end{aligned}
\tag{8}
$$

**定理 1。** 在 (5)、(7) 下，
$$
\boxed{\#\{n\in\{0,1,\ldots,5\}:C_n\equiv0\}\le1.}
\tag{9}
$$
$C_0$ 始终非零，因此可能的唯一缺项属于 $\{1,\ldots,5\}$。

**证明。** 所有下面使用的 $2,3,5,6$ 都是原域中的单位。

若 $u\equiv0$，则 $C_1=0$，而
$$
C_2=3a^2v,\quad C_3=3a^2w,\quad
C_4=3a(aA_4+v^2),\quad C_5=3a(aA_5+2vw)
$$
全部非零；后两括号的常数项分别为 $1$、$-2$。
连同 $C_0\ne0$，此时唯一缺项准确是 $n=1$。

以下设 $u\ne0$，置 $n_u=\operatorname{ord}_tu\ge1$。
若 $n_u>m$，在 $C_2,C_3,C_4,C_5$ 中的唯一最低阶项分别来自
$3a^2v,3a^2w,3av^2,6avw$，故六项全非零。

若 $n_u=m$，写
$a=a_mt^m+\cdots,\ u=u_mt^m+\cdots$，$a_mu_m\ne0$。
$C_0,C_1,C_2,C_4$ 全非零。
余下两项的首候选系数为
$$
[t^{2m}]C_3=3a_m(a_m-2u_m),\qquad
[t^m]C_5=3(u_m-2a_m).
\tag{10}
$$
因此 $C_3\equiv0$ 必须 $u_m=a_m/2$，
而 $C_5\equiv0$ 必须 $u_m=2a_m$；
二者同时成立将迫 $3a_m=0$，不可能。
这也说明仅有首候选系数为零不等于该全局系数恒零。

最后若 $n_u<m$，由 $m\le2$，只能 $m=2,n_u=1$。
写 $a=a_2t^2+\cdots,\ u=u_1t+\cdots$。
$C_0,C_1,C_5$ 非零，而
$$
\begin{aligned}
[t^4]C_2&=3a_2(u_1^2-a_2),\\
[t^3]C_3&=u_1(u_1^2-6a_2),\\
[t^2]C_4&=3(a_2-u_1^2),\\
[t]C_5&=3u_1.
\end{aligned}
\tag{11}
$$
若 $u_1^2\ne a_2$，则 $C_2,C_4$ 已非零，至多 $C_3$ 缺失。
若 $u_1^2=a_2$，则 $C_3$ 的首系数为 $-5a_2u_1\ne0$，
所以只需排 $C_2,C_4$ 同时恒零。
一旦 $C_2\equiv0$，整域中 $av+u^2=0$，
(8) 精确化为
$$
C_4=3a(aA_4+2uw).
\tag{12}
$$
$aA_4$ 的阶至少三，而 $uw$ 的阶为一；
故 (12) 的阶为三、首系数 $6a_2u_1\ne0$。
所以两者不能同时恒零。证毕。

这是同一个原 $F$ 的系数限制，没有给任何系数赋额外中央零，
也未用数值样本或环境 Hermite–Padé 正规性。

## 3. 真正稳定核至多一维

由 $f(Y)=Y^2(Y-1)$，R907 的实际纤维特征多项式精确成为
$$
\boxed{Q_f(Z)=\prod_{n=0}^5(Z-n).}
\tag{13}
$$
确实 $f^3=-Y^6+3Y^7-3Y^8+Y^9$、$\gamma=1$，且
$$
-\frac1{Z-6}+\frac3{Z-7}-\frac3{Z-8}+\frac1{Z-9}
=\frac6{(Z-6)(Z-7)(Z-8)(Z-9)}.
$$
代入 R907(23) 即得 (13)，没有另换来源格。

**定理 2。** 保 (1)–(5)，则
$$
\boxed{\dim K_\infty\le1.}
\tag{14}
$$
若 $C_0,\ldots,C_5$ 全非零，则 $K_\infty=0$。

**证明。** R907 已付 $Q_f(\mathcal T)K_\infty=0$。
(13) 在 $k$ 上分裂且平方自由，故 $\mathcal T|_{K_\infty}$
按特征值 $n=0,\ldots,5$ 分解。
一个特征向量满足全局原多项式身份
$$
(\mathcal E-n)G=\alpha F^3,\qquad \alpha=a(G)\in k.
\tag{15}
$$
在同一个原单项式框取 charge $n$，得到
$$
0=\alpha C_n(t).
\tag{16}
$$
若 $\alpha=0$，则 $G$ 是原纯 charge $n$。
R907 的每一条真实纯 charge 帽
$\operatorname{ord}_0[Y^n]G\le R_C<T$ 与 (4) 第一长行
迫 $G=0$。因此每个非零特征向量的 $\alpha$ 必非零，
其特征值必须是 (9) 中唯一可能的缺项。

在固定特征值上，$G\mapsto\alpha$ 也单射：
两个向量的 $\alpha$ 相同，其差是 $K$ 中的纯 charge，故差为零。
所以每个允许特征空间至多一维，(9) 给 (14)。
六项全非零时没有允许特征值。证毕。

这不把 $K$ 本身认成稳定。
它也没有把原 $(0,0)$ 当作额外吹起中心；
$f$ 的 $Y^2$ 因子只是这个原因子的零纤维性质，
未强加给整个 $\mathcal H_3$ 的最低 charge。

## 4. 剩余方向是一个明确来源加同一纯 charge

若六项全非零，以下不需再测试。
否则令 $n_*\in\{1,\ldots,5\}$ 为唯一满足 $C_{n_*}\equiv0$ 的指标。
定义同一完整多项式
$$
\boxed{
B_{n_*}(t,Y)=
\sum_{\substack{0\le j\le3b\\j\ne n_*}}
\frac{C_j(t)}{j-n_*}Y^j.
}
\tag{17}
$$
$3b<p$ 保全部分母为单位。
原十九角截面格按 charge 直和，$F^3\in\mathcal H_3$，
故各项投影和 (17) 都在真正的 $\mathcal H_3$ 中。
特别
$$
(\mathcal E-n_*)B_{n_*}=F^3.
\tag{18}
$$

令原纯 charge 系数空间为
$$
\mathcal A_{n_*}
=\{c(t)\in k[t]:c(t)Y^{n_*}\in\mathcal H_3\}.
\tag{19}
$$
任何归一为 $\alpha=1$ 的可能稳定向量都必须是
$$
G_{n_*}=B_{n_*}+c(t)Y^{n_*},\qquad c\in\mathcal A_{n_*}.
\tag{20}
$$
没有允许超出 (19) 的多项式插值，更没有在各个角分别选取系数。

**定理 3。** (20) 给非零稳定向量，当且仅当同一个 $c$ 满足
$$
\boxed{
c(t)\equiv
-g(t)^{-n_*}B_{n_*}(t,g(t))\pmod{t^T},
\qquad c\in\mathcal A_{n_*}.
}
\tag{21}
$$
这样的 $c$ 至多一个。
若存在，则 $K_\infty=kG_{n_*}$；
若不存在，则 $K_\infty=0$。

**证明。** 稳定向量的必要性已由 (15)–(20) 和第一长行给出。
反过来，设 (21) 成立。则
$$
\begin{aligned}
\mathcal EG_{n_*}
 &=n_*G_{n_*}+F^3,\\
\mathcal E^2G_{n_*}
 &=n_*^2G_{n_*}+n_*F^3+3F^2e,\\
\mathcal E^3G_{n_*}
 &=n_*^3G_{n_*}+n_*^2F^3+3n_*F^2e
   +6Fe^2+3F^2\mathcal E^2F.
\end{aligned}
\tag{22}
$$
在同一个轴 $Y=g$ 上，$F$ 的阶恰为 $h$，$e$ 为单位。
(21)、$T\le2h$ 使前三个长行成立；
$L\le h$ 使最后短行成立。
所以 $G_{n_*}\in K$。
在 $P$ 处，(21)、(22) 给前四个 Euler jet 为零；
再对 (18) 取三次 Euler 导数，得
$$
(\mathcal E^4G_{n_*})(P)=6\gamma^3.
$$
因此 $a(G_{n_*})=1$，准确有
$\mathcal TG_{n_*}=n_*G_{n_*}$。
所以它确在 $K_\infty$，且非零。

若两个 $c$ 都满足 (21)，其差乘 $Y^{n_*}$ 是
$\mathcal H_3$ 中消到 $T$ 的纯 charge。
仍由 $R_C<T$ 迫差为零。证毕。

原首常数也被固定，而非自由：
$$
B_{n_*}(0,1)
=-\frac6{(6-n_*)(7-n_*)(8-n_*)(9-n_*)},
$$
$$
\boxed{
c(0)=\frac6{(6-n_*)(7-n_*)(8-n_*)(9-n_*)}\ne0.
}
\tag{23}
$$
这是 $f^3$ 的四项分式直接相加；全部小分母在原 $p>211$ 下为单位。

## 5. 纯 charge 空间的完整十九角公式

为使 (21) 是真正来源测试，本节给 (19) 的全部原帽，而非只用上界 $R_C$。

写 R495 的原曲线类
$$
C=bS_0+(u_C+4b)f-\sum\mu_{i,j}E_{i,j}^*,
\qquad u_C=\max_i(\deg A_i-4i)\ge0.
$$
沿用 R495(5) 的累计值 $V_j^{(i)}=V_j^{(i)}(F)$。
有限负权底点为
$$
i=0,\ h_{7,1},h_{7,2},1,
\qquad l_i=4,4,4,3;
$$
有限正权点为 $d=-1/8$，长二；底无穷远正权链也长二。

对每个原 $0\le n\le3b$ 定义
$$
\alpha_i(n)=
\max\left(
0,\ \max_{1\le j\le l_i}
\left\lceil\frac{3V_j^{(i)}-3b+n}{j}\right\rceil
\right)\qquad(i\text{ 为有限负权点}),
$$
$$
\alpha_d(n)=
\max\left(
0,\ \max_{1\le j\le2}
\left\lceil\frac{3V_j^{(d)}-n}{j}\right\rceil
\right),
\tag{24}
$$
以及
$$
d_n=\min\left(
3u_C+4n,\
\min_{1\le j\le2}
\left\{3u_C+4n+
\left\lfloor\frac{n-3V_j^{(\infty)}}j\right\rfloor\right\}
\right).
\tag{25}
$$
令
$$
P_n(t)=
\prod_{i=0,h_{7,1},h_{7,2},1,d}(t-t_i)^{\alpha_i(n)},
\qquad M_n=d_n-\deg P_n.
\tag{26}
$$
在原域上按完整闭点乘积解释 (26)。
两个 $h_7$ 几何根的指数按原 Galois 不变类同时下降；
不得将剩余域次数删去。
所有指数均非负，取首一乘积。

**命题 4。** 准确有
$$
\boxed{\mathcal A_n=P_n(t)\,k[t]_{\le M_n},}
\tag{27}
$$
$M_n<0$ 时该空间为零。

**证明。** 原 $\mathbb F_4$ 上的全局截面帽先给
$c(t)\in k[t]$、$\deg c\le3u_C+4n$。
在有限负权图 $x=1/Y$，实际局部框是
$x^{3b-n}c(t)$。
第 $j$ 次累计赋值为
$3b-n+j\operatorname{ord}_{t_i}c$，
须至少为 $3V_j^{(i)}$。
这些逐项条件恰是 (24) 的第一行。
有限正权图的累计值为
$n+j\operatorname{ord}_dc$，给第二行。

底无穷远使用原实际框
$$
T^{3u_C+4n}c(T^{-1})Z^n,\qquad T=1/t,\quad Z=t^4Y.
$$
严格底纤维正则给原次数帽；
第 $j$ 步累计值为
$j(3u_C+4n-\deg c)+n$。
它至少为 $3V_j^{(\infty)}$，正是 (25)。
两个严格水平截面则由 $0\le n\le3b$ 保证。
有限角外不允许新增极，故剩余系数恰是 (26) 的乘积乘一个多项式。
这支付全部十九个累计角，不仅最后五种 Gauss 权。
反向同样逐项成立，故为等号。证毕。

在本篇可能留下的 $n_*\le5$ 上，
$A_3(0)=1$ 使零链的每个 $V_j^{(0)}\le b-3$。
所以
$$
\alpha_0(n_*)=0,\qquad P_{n_*}(0)\ne0.
\tag{28}
$$
若 $M_{n_*}\ge0$，则 $P_{n_*}t^{M_{n_*}}Y^{n_*}$
本身是实际纯 charge 截面；
R907 的帽遂给 $M_{n_*}\le R_C<T$。

因此 (21) 可完全写成一个确定的有限系数测试。
置
$$
\beta_{n_*}(t)=-g(t)^{-n_*}B_{n_*}(t,g(t)).
$$
若 $M_{n_*}<0$，须 $\beta_{n_*}\equiv0\bmod t^T$；
但 (23) 已排除此情形。
若 $M_{n_*}\ge0$，则准确需要
$$
\boxed{
[t^j]\frac{\beta_{n_*}(t)}{P_{n_*}(t)}=0
\qquad(M_{n_*}+1\le j<T).
}
\tag{29}
$$
通过时唯一系数为
$$
c(t)=P_{n_*}(t)
\left[\frac{\beta_{n_*}(t)}{P_{n_*}(t)}\right]_{\le M_{n_*}}.
\tag{30}
$$
(29) 只读同一个实际 $g$ 的原 $T$ 前缀，
不延长到 $s$，不假设目标素数上的环境子式为单位。
它也没有以模 $p$ 的候选通过替换下一除 $p$ 页。

## 6. 同来源联合秩的准确加强

定义
$$
\varepsilon_F=
\begin{cases}
1,&\text{恰有一个 }C_{n_*}\equiv0\text{ 且 (29) 在真帽中通过},\\
0,&\text{否则}.
\end{cases}
$$
以上定理给
$$
\boxed{\dim K_\infty=\varepsilon_F\le1.}
\tag{31}
$$
这是一个由完整 $F$ 和同一实际前缀决定的数，不是可选参数。

在 R914 的准确门
$$
\mathsf A_5:\ 13(T-R_C)>27\kappa+312b,
\qquad
\mathsf A_6:\ 16(T-R_C)>27\kappa+384b
$$
下，其同源链映射和真实核识别原样成立。
所以 R914 的联合界分别加强为
$$
\boxed{9\dim K\le8n_T+\varepsilon_F\le8n_T+1
\quad(\mathsf A_5),}
$$
$$
\boxed{10\dim K\le9n_T+\varepsilon_F\le9n_T+1
\quad(\mathsf A_6).}
\tag{32}
$$
同时保原 $\dim K\le n_T$。
没有假定 $V_T$ 非特殊，$n_T$ 仍是真实维数；
没有把这些单位增益与其它显示子格直接相加。

(14)、(21)、(31) 本身不需要 $\mathsf A_5$ 或 $\mathsf A_6$。
这两个门只用于从稳定部分的精确维数回到整个原核的 (32)。

## 7. 唯一可能稳定方向的原指定 GRes

若 $\varepsilon_F=1$，使用 (20)、(30) 得到唯一归一 $G_{n_*}$。
保 R907§8 的原定义
$$
W_s=t^{r+1-s}(1-t)^{3s},\qquad
c_s=\frac{3(-1)^s}{17},\qquad H_s=c_sW_sF_t^2,
$$
$$
\Lambda(G)=
\sum_{Z^\circ}\mathcal R_{F,e}
\bigl(H_s\mathcal E^2(q_{\rm src}t^rG)\bigr).
\tag{33}
$$
$Z^\circ$ 及其余局部因子上的补零仍与 R842 相同；
留数用有序 $(F,e)$ 和 $\Omega_{\log}=dt\wedge dY/Y$。
两个 $t^r$ 仍各有原来源：
$W_s$ 中的是 R822 的 weighted Cartier 外权，
(33) 中的是实际来源返回，不能约去其中之一。

由 (18)，在完整交商 $(F,e)$ 中，
$$
\mathcal EG_{n_*}=n_*G_{n_*},\qquad
\mathcal E^2G_{n_*}=n_*^2G_{n_*}.
$$
故得到固定的实际一行
$$
\boxed{
\Lambda(G_{n_*})=
\sum_{Z^\circ}\mathcal R_{F,e}
\left(
H_s t^rG_{n_*}(\mathcal E+n_*)^2q_{\rm src}
\right).
}
\tag{34}
$$
其中
$(\mathcal E+n_*)^2q_{\rm src}
=\mathcal E^2q_{\rm src}+2n_*\mathcal Eq_{\rm src}
+n_*^2q_{\rm src}$。
同一个余因子的全部导数、全部有限非约化交及剩余域迹都保留。
本篇没有判 (34) 为零或非零。

特别，不能再用 R907 的两个反馈迹 $m_4,m_5$
把 (34) 自动消掉。
对这个归一特征向量，原全恒等式准确给
$$
\Lambda(\mathcal E^jG_{n_*})=n_*^j\Lambda(G_{n_*})\quad(0\le j\le4),
$$
$$
\Lambda(\mathcal E^5G_{n_*})=n_*^5\Lambda(G_{n_*})+m_4,
$$
$$
\Lambda(\mathcal E^6G_{n_*})=n_*^6\Lambda(G_{n_*})+n_*m_4+m_5.
\tag{35}
$$
代入六次 $Q_f$ 后，$\Lambda(G_{n_*})$ 的系数恰是
$Q_f(n_*)=0$。
余下两项正与 R907(41) 的反馈相符；
这是一致性身份，不是 (34) 的额外零条件。

原固定边界补偿 $\mathfrak B_F$、原点短尾、
十九角和 conductor、同 $K_{\rm corr}/H_{\rm corr}$、
唯一第二法向值、完整 $R/S$、三个十三行带、
末端四次 carry 与下一精度均未因本篇而删除。
原全 $\mathcal W_D$ 的非 $\mathcal H_3$ 列也仍在。
(32) 是同一个真实子格与同源链的秩加强，
不是原主目标完成，也不是指定仿射 forcing 已不可解。

依赖：R495 的完整三倍截面与十九角，
R792§6/R797§1 的实际移动常数因子范围，
R907 的同源反馈和六维零纤维，
R911/R914 的真实长行能量及同链秩。
本篇为精确手证，没有新增数学运行或数据。
