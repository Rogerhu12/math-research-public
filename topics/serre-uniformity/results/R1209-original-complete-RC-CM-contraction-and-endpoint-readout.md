# R1209：原最高 packet 的全列 RC–CM 消去与准确端点读数

日期：2026-11-28。会话：Astra-serre-24b8836b-20261126；global_route / root / o2_high_coefficient。

**已证明。** 在 R1196–1208 的同一个最高整 packet、同一个 $P=(p-1)D_0$ 和同一个有限 Picard–Serre 配对中，任意首中心多项式 $S(b)=\mathsf S(b^3)$、$\deg\mathsf S\le n$ 的完整首对数，准确等于一个 good CM 周期系数。全部 SS 项、三个支持 CM 尾、静态节点单位及低次 log 与高 normal 的交叉项均在式中保留并计算：

$$
\boxed{\quad
\mathcal V_m(S)=-\frac{8\,2^m\nu}{A(1)}
 [t^m]\mathcal E_S(t),\qquad
\mathcal E_S(t)=-\frac{v^2F(v^3)^3}{A(1)}
 S\!\left((1-v^3)^{1/3}\right),\quad
t=v\,\frac{G(v^3)}{F(v^3)} .
\quad}
\tag{1209.1}
$$

$F,G$ 是下文从同一个 good CM 家族明确定义的有限周期，$\nu$ 是 R1200/R1208 已锁定的原 Igusa–Weil 单位。式 (1209.1) 不引入任意局部参数比较因子。

对实际 PS 返回 $\mathscr DT$，该式又化为
$$
\boxed{\quad
\mathcal V_m(\mathscr DT)=
\frac{8\,2^m\nu(m+1)(m+2)}{A(1)}
 [t^{m+1}]\frac{T(b(t))}{A(b(t))}.
\quad}
\tag{1209.2}
$$
原真正返回算子仍是 $\mathcal C(T)=-3\gamma^2\mathscr DT$，不得漏掉这个已付单位。本文先证明全部原来源及端点公式；不把它直接等同于任意指定半秩商上的两列楔或 whole-disc 排除。

## 1. 原对象、有限精度和各个常数

保持
$$
p=12g-1>37,\quad n=2g-1,\quad
m=3n+2=(p-1)/2,\quad p=6n+5,\quad
e_0=m(p+1),\quad\pi_0^{e_0}=p.
\tag{1209.3}
$$
$n,m$ 均为奇数。置
$$
r=1-b^3,\quad A(b)=bQ(b^3),\quad
h=r^{n+1}A,\quad u^m=h,\quad
Q_0=Q(0)=\binom mn,\quad A_1=A(1)=-Q_0.
$$
$Q$ 是原 monic Jacobi polynomial，次数 $n$。仍取
$$
L=(m-1)/2,\qquad
c_m=(-1)^L\binom{m-1}{L},\qquad
\nu=(-3)^L(2\gamma)^{m-1}.
\tag{1209.4}
$$

由 R1193/R1197，每个 $S(b)=\mathsf S(b^3)$、$\deg\mathsf S\le n$ 都是同一个负 deck 角色底空间的实际首中心输入。选保持原角色且被 $E_m$ 固定的整提升 $\Omega_S$：
$$
\overline{\pi_0^{-1}\Omega_S}|_I=\frac{S(b)\,db}{uA(b)}.
$$
R1196 定义的 $\mathcal V_m(S)$ 是
$\pi_0^{-m^2}\langle E_m\log P,\Omega_S\rangle$ 的约化；同底向量的提升不改变它。本文从这个定义计算，不另以端点式定义新泛函。

全部计算先在
$$
A_M=R/(\pi_0^{m^2+1}),\qquad I=(\pi_0^m)
$$
的原相对 Picard 复形中进行。此处 $p=0$，$I^{m+1}=0$，有限 log 只反除 $1,\ldots,m$。所需 good fine 周期到次数 $m+1<p$；相应有限 PD 厚化仍只除这些 $p$ 单位。文中的幂级数表示这些有限 jet，不假定一个无限水平解或一个任意的整 Cartan 提升。

## 2. 同一个 good CM target 的有限周期

先取 Igusa 标记 $b=1$。在 R1208 §9 的同一 good 六层模型上写
$$
r=v^3,\qquad b=(1-v^3)^{1/3},\qquad
E_{\rm good}:Y^2=X^3+3bvX+(1-2b^3).
$$
若 $q^2=v$，则原 $\omega_b=q^{-1}\omega_{\rm good}$。

把 R1198.4 的原 Picard–Fuchs 方程逐项代入 $b^3=1-v^3$、$y=q^{-1}f$，得到
$$
f''-\frac{2v^2}{1-v^3}f'
       -\frac{v}{4(1-v^3)}f=0.
\tag{1209.5}
$$
原 CM $\mu_3$ 两条晶体线不同，故其实际 opposite 线给 $f_0'(0)=0$。取
$$
f_0(v)=F(v^3),\qquad f_1(v)=vG(v^3),
$$
初值为 $f_0(0)=1,f_0'(0)=0,f_1(0)=0,f_1'(0)=1$。直接递推 (1209.5)：
$$
F(X)=\sum_j\frac{(1/6)_j^2}{(2/3)_j\,j!}X^j,\qquad
G(X)=\sum_j\frac{(1/2)_j^2}{(4/3)_j\,j!}X^j
\tag{1209.6}
$$
到本篇所需阶为止；全部分母为单位。原 Hasse 解又给
$$
f_1(v)=\frac{vA(b)}{A_1},\qquad
G(X)=(1-X)^{1/3}\frac{Q(X)}{Q_0},
\quad X=v^3.
\tag{1209.7}
$$
第二式使用原反射 $Q(1-X)=-Q(X)$。可直接把首式代入 (1209.5) 核准：原 $h=v^{m+1}A$ 与 $q^{-1}f_1$ 只差常数乘 $q^p$，在所需特征 $p$ 有限微分中不改变方程。

置
$$
t=f_1/f_0=vG/F.
$$
Wronskian 的初值为一，故
$$
\frac{dt}{dv}=\frac1{b^2F^2},\qquad
\frac{dt}{db}=-\frac1{v^2F^2}.
\tag{1209.8}
$$

对另外两个标记，写 $b_\xi=\xi(1-v^3)^{1/3}$，$\xi^3=1$。good 方程、$F,G,t$ 相同，
$$
A(b_\xi)=\xi A_1\,tF/v,\qquad
\frac{db_\xi}{dt}=-\xi v^2F^2.
\tag{1209.9}
$$
标记是 Igusa 的 $b=\xi$；原 coarse 标记为 $\xi^p$，后两个 divisor 系数相同，仍用 $a_1=2,a_\zeta=a_{\zeta^2}=-1$。这里不增加一次算术 Frobenius。

### 2.1 周期与原 quotient/node 参数确是同一比较

R1198 §2.1 的有限 Messing 比较同样适用于这个 good fine target，且可由 $m$ 延至 $m+1<p$。若 $\eta\in\mu_{p^2-1}$ 是原 full framing 的本原根，其 target 角色为 $\eta^{p-1}$，阶 $p+1$（此 $\eta$ 不是 CM 的三次根 $\zeta$）；有限周期比与实际 target 参数 $u'$ 角色相同。故在本篇精度内，二者只差其原一次单位。

保持 R1021 的同一个
$u'=\pi_0^m(c_Q\psi+pR_Q)$，
$\psi=\beta_Q^{p-1}$。在中心 connected line 上 $x_{\rm good}=0$，而
$$
W=\pi_0V=y_{\rm good}^2+3x_{\rm good}^2,\qquad
\pi_0^m\psi=y_{\rm good}^{p-1}=W^m .
$$
因此存在这里始终保留的原单位 $c_\xi$，使
$$
t=c_\xi W^m
\tag{1209.10}
$$
在所需中心 finite jet 中成立；在同一个尾图上则为
$t=c_\xi\pi_0^m\psi$。这来自实际 quotient 参数及同 target 的晶体比较，不是仅按 Hasse 的 $m$ 次方式任选根。

记 R1208 的真实相位
$\tau_\xi=\lambda_\xi\rho_\xi^{n+1}$。写
$$
u=\tau_\xi W^{m+1}K(t),\qquad K(0)=1.
$$
由 $u^m=h$、(1209.7)、(1209.10) 得
$$
\tau_\xi^m=A(\xi)c_\xi^{m+1},\qquad
K^m=(v/t)^mF.
$$
于是，在所需有限精度内，
$$
K=(v/t)F^{-2}.
\tag{1209.11}
$$
这里 $m=-1/2$ 于 $k$；严格地 $(F^{-2})^m=F/F^p$，但
$F^p=1+O(t^{3p})$，超过本文所有读取次数。没有把这个有限等式扩大为无限幂级数恒等式。

## 3. 任意底向量的全部实际 CM normal

定义
$$
\mathcal E_S(t)=
\frac{S(b_\xi)\,db_\xi/dt}{A(b_\xi)K(t)}
=-\frac{v^2F^3S(b_\xi)}{A_1}
=\sum_{k\ge1}e_{k-1}(S)t^{3k-1}.
\tag{1209.12}
$$
因为 $S$ 是 $b^3$ 的多项式，右侧与 $\xi$ 无关。其 top coefficient 为 $e_n=[t^m]\mathcal E_S$。

沿同一个 $W=\pi_0V$，
$$
\frac{S\,db}{uA}
=\frac{mc_\xi}{\tau_\xi}W^{-2}
   \mathcal E_S(c_\xi W^m)\,dW.
$$
在 $z_D=V^{-3}$ 上，$W=\pi_0z_D^{-1/3}$。以下在 R1021 的同一个 constant affine 模 $p$ 帧中，逐 normal 取实际系数；记为 $\Omega_{S,\xi}^{[N]}$。此前非零层保留在同一展开中，不把尚未除尽低层的 $\Omega_S/\pi_0^N$ 直接约化。

因此第
$$
N_k=(3k-1)m,\qquad
d_k=km-(n+1)=\frac{N_k-1}{3}
$$
层的最高极部准确为
$$
-\frac{m c_\xi^{3k}}{3\tau_\xi}
 e_{k-1}(S)\,
 \pi_0^{N_k}z_D^{-d_k-1}dz_D .
\tag{1209.13}
$$

这个计算不假定此前的 $S$-jets 为零。任意更高中心层的阶至少为 $1+(p+1)$；真实厚度三 node 的全部 normal–pole 界为
$\operatorname{pole}\le(N-1)/3+1$。更高中心层在当前 $N_k$ 给严格较低的 pole；已有尾 polar 项返回后也不能提高当前最高 pole。真实 node 单位的重参数保此滤过。

R1197 的完整 polynomial representative、全部 Weil 分支上的 determinant 运输和一维 $E_m$ 图像，适用于这些实际全部低极及 holomorphic 项；$k=n+1$ 的终端 $\mathrm{St}^N=0$ 已由 R1208 §3 补齐。因此当前层的最高系数完全决定整层。保持同一
$$
F_{\rm tail}=UV^{m-2},\qquad
H_k=\frac{\Theta^{3k-3}F_{\rm tail}}
 {(-1)^{k-1}(3k)!/6},
$$
得到所有 $1\le k\le n+1$ 的原完整式
$$
\boxed{\quad
\Omega_{S,\xi}^{[N_k]}
=\gamma_{k,\xi}(S)\,dH_k,\qquad
\gamma_{k,\xi}(S)=
\frac{m c_\xi^{3k}}{3\tau_\xi d_k}\,e_{k-1}(S).
\quad}
\tag{1209.14}
$$
$d_k=-(3k+1)/6$ 于 $k$，全部为单位。对前层消失的情形，(1209.14) 还原 R1197 的旗标；此处没有把那些旗标公式直接用于混合层。

## 4. 一般 SS 积分项严格为零

原 SS 收缩仍使用
$$
\lambda_1=-6b/r,\qquad
w_a=\frac{2(-1)^{m-a}(m-1)!}{(a-1)!(m-a+2)!}.
$$
R1200 的完整三次对称消去，对任意 $S\in k[b^3]$ 都杀掉 $\lambda_0=-6/r$ 的总和。设
$$
\mathcal P_m^{\lambda_1}(S)(b)=\mathsf P(b^3),
\qquad \deg\mathsf P\le3n+1.
$$
SS 部分为
$$
\mathcal V_{\rm SS}(S)=-m c_m\nu\,\Sigma(S),\qquad
\Sigma(S)=\sum_{A(s)=0}
 \frac{\mathsf P(s^3)}{(1-s^3)^{n+2}A'(s)^2}.
\tag{1209.15}
$$

沿 R1201 的同一个有限 Rankin–Cohen 源，置
$$
\operatorname{RC}^{2,3}_N(K,E)=
\sum_{i+j=N}(-1)^j
 \binom{N+1}{j}\binom{N+2}{i}K^{(i)}E^{(j)}.
$$
其原低一阶 primitive
$$
\mathcal T(K,E)=\frac2{m(m-1)m!}
 \operatorname{RC}^{2,3}_{m-2}(K,E)
$$
满足
$$
\mathcal T'=
 \frac2{m(m+1)!}\operatorname{RC}^{2,3}_{m-1}(K,E).
\tag{1209.16}
$$
R1201 已逐系数证明，使用的是 $2m+1=p$，不是未付的模形式类比。

现在把其输入 $-r^n$ 换成原 $S$。同一个有理函数
$\mathcal J_S=3b^p r^{m-1}\mathcal T_b$
仍准确满足
$$
\mathcal J_S'=3b^p r^{n+1}\mathsf P(b^3).
\tag{1209.17}
$$
为保证有限积分没有 $p$ 次幂歧义，给出一般界。原 finite ODE 递推给
$$
K_b^{(i)}\in r^{-i-1}k[b]_{\le2i+1},
\qquad
E_{b,j}\in r^{n+2-j}k[b]_{\le3n+2j}.
$$
在 $i+j=m-2$ 中，
$$
\mathcal T_b\in r^{n+3-m}k[b]_{\le9n+1}.
$$
所以
$$
\mathcal J_S=b^p r^{n+2}R_S(b),\quad
R_S\in b\,k[b^3],\quad
\deg_b\mathcal J_S\le3p-3.
\tag{1209.18}
$$
$R_S$ 的三次角色与 R1201.28 相同；$S$ 角色为零。故
$\mathcal J_S=J_S(B)$，且
$$
J_S\in B^{2n+2}(1-B)^{n+2}k[B],\quad
\deg J_S\le p-1.
$$
由 (1209.17)，
$$
J_S'(B)=B^{2n+1}(1-B)^{n+1}\mathsf P(B).
$$
因此
$$
\boxed{\quad
\int_0^1 B^{2n+1}(1-B)^{n+1}\mathsf P(B)\,dB=0 .
\quad}
\tag{1209.19}
$$
积分中的全部次数至多 $p-2$。这已经把一般 SS 求和的积分部分真实消去，未删除端点的高阶极部。

## 5. 原 Gauss 误差恰是同一个 good CM 周期

令 $\alpha=2n+2$、$w(B)=B^\alpha(1-B)^\alpha$。R1201 已给原 monic $Q$ 的 exact quadrature
$$
\sum_{Q(s)=0}\frac{f(s)}{s(1-s)Q'(s)^2}
=\int_0^1w(B)f(B)\,dB,\qquad\deg f\le2n-1.
$$
对端点 $s=1$ 定义有限 Taylor 误差
$$
\Delta(s)=\frac1{Q(s)}
 \int_0^1\frac{w(B)Q(B)}{s-B}\,dB.
$$
这里只读到 $(s-1)^n$；每个系数都是原合法多项式积分。由
$(Q(s)-Q(B))/(s-B)$ 的插值，$\Delta$ 正是积分减离散求和的 Cauchy 误差。

用 R1201 的 Rodrigues 式分部积分 $n$ 次。对 $0\le j\le n$，
$$
I_j:=\int_0^1\frac{w(B)Q(B)}{(1-B)^{j+1}}\,dB
=-\binom{n+j}{n}\frac{m!(\alpha-j-1)!}{(5n+4-j)!}.
$$
置 $\mathcal B=-I_0$，已知 $Q_0\mathcal B=3$。逐项相除：
$$
\frac{I_j}{I_0}
=\frac{(n+1)_j^2}{(-2n-1)_j\,j!}
=\frac{(1/6)_j^2}{(2/3)_j\,j!}.
$$
因此准确得到
$$
\boxed{\quad
\Delta(1-X)=\frac{3F(X)}{Q_0Q(X)}
=\frac{3bF(X)}{Q_0^2G(X)}
\pmod{X^{n+1}} .
\quad}
\tag{1209.20}
$$
它是 §2 的原 good $F$，没有新的 period 比例。

对
$f(B)=\mathsf P(B)/(B(1-B)^{n+1})$
作部分分式。多项式部分次数至多 $2n-1$，$0$ 端仅简单极，$1$ 端至多 $n+1$ 阶。故 exact quadrature、(1209.19) 和端点 residue 给
$$
\Sigma(S)=\frac13\operatorname{Res}_{B=1}
 \frac{\mathsf P(B)\Delta(B)}{B(1-B)^{n+1}}\,dB.
\tag{1209.21}
$$
$0$ 端项准确为 $-\mathsf P(0)/Q_0^2$，与原 $s=0$ 项相消。这沿用同一个原节点，不是删除该节点。

换 $X=1-B=v^3$，(1209.20)–(1209.21) 成为
$$
\Sigma(S)=-
\frac1{Q_0^2}\operatorname{Res}_{X=0}
 \frac{\mathsf P(1-X)}{X^{n+1}}\,
 b^{-2}\frac FG\,dX .
\tag{1209.22}
$$

## 6. SS 全列在 good 周期中的准确 RC 表达

置
$$
K_1(t)=\frac{6bF^2}{v}=\frac6t+L_1'(t),
\qquad L_1(t)=\sum_{j\ge1}\ell_jt^{3j},
$$
$$
\widehat E_S(t)=v^2F^3S(b)=-A_1\mathcal E_S(t),
\qquad
\mathfrak C_m(K,E)=\frac2{m(m+1)!}\operatorname{RC}^{2,3}_{m-1}(K,E).
\tag{1209.23}
$$
这里 $K_1$ 有真实的 $6/t$；不得套仅对 regular 输入的公式把它省去。

用原 Picard–Fuchs 的有限 framing 恒等式，在普通计算基点取
$y_0=q^{-1}F$、$q^2=v$，其周期比就是 $t$。由 (1209.8)，
$t_b'=-1/(v^2F^2)$。同一归一运输给
$$
\mathsf P(b^3)=
r^{m-n-2}(t_b')^m y_0^{-3}
 \mathfrak C_m\!\left(K_1,r^{n+2}S\,y_0^3\right).
$$
$r^{n+2}S y_0^3=q^p\widehat E_S$，$q^p$ 的导数为零；全部半次幂消去后
$$
\mathsf P(b^3)=
-v^{m-2}F^{-p-2}\mathfrak C_m(K_1,\widehat E_S).
\tag{1209.24}
$$
此式只检验相同有限 ODE jets；没有假定特征 $p$ 连接在全局有两个无限水平解。

将 (1209.24) 代入 (1209.22)，并用
$dt=dv/(b^2F^2)$。$X=v^3$ 的 ramification 为三，给
$$
\Sigma(S)=\frac1{Q_0^2}
 \operatorname{Res}_{t=0}
 F^{-p}\mathfrak C_m(K_1,\widehat E_S)\,\frac{dt}{t}.
$$
$\mathfrak C_m$ 的极阶至多 $m-2$，
而 $F^{-p}=1+O(t^{3p})$，故
$$
\boxed{\quad
\mathcal V_{\rm SS}(S)=
-\frac{2c_m\nu}{(m+1)!Q_0^2}
 [t^0]\operatorname{RC}^{2,3}_{m-1}(K_1,-A_1\mathcal E_S).
\quad}
\tag{1209.25}
$$

### 6.1 regular 部分与 singular 部分分别计算

若 $j,k\ge1$、$j+k=n+1$，则
$3j-1+3k-1=m-1$。regular 单项式的 RC 常数项只有
$i=3j-1$、$l=3k-1$ 一项。置
$$
\mathcal A_S=
\sum_{\substack{j,k\ge1\\j+k=n+1}}
 \frac{(-1)^{k-1}\ell_j e_{k-1}(S)}
 {(3j-1)!(3k+1)!}.
\tag{1209.26}
$$
它在 (1209.25) 中贡献
$2c_m\nu m!\mathcal A_S/A_1$。

对 singular 项必须单独算。直接 Vandermonde 给
$$
[t^0]\operatorname{RC}^{2,3}_{m-1}(t^{-1},t^m)
=\frac{m!}{m+2}
 \left(\binom{2m+2}{m}-1\right)
=-\frac{m!}{m+2}.
\tag{1209.27}
$$
因为 $2m+2=p+1$ 且 $2\le m<p-1$。带入 $6/t$ 及
$-A_1e_nt^m$，得到
$$
\boxed{\quad
\mathcal V_{\rm SS}(S)=
-\frac{16c_m\nu}{A_1}e_n(S)
+\frac{2c_m\nu m!}{A_1}\mathcal A_S.
\quad}
\tag{1209.28}
$$

## 7. 同一有限 Čech 来源的全部 CM analytic 项

继续 R1208 §4–6 的原 frame，而非另选一个对数类。原 $e_D/e_I$ 精确由 $G(b_{\rm lift})^2$、尾主化 $x_D^{ma_\xi}$、同一 vertical twister 和厚度三 node 给出。其 static node unit $\sigma_\xi$ 的所需 jet 为
$$
\sigma_\xi(z_D)=(1+A_\xi^{\rm tail}z_D^{4g})^{-3a_\xi}.
$$
用完整 static unit 作节点 frame 修正 $e_N'=\sigma_\xi e_N$ 后：

- tail–node 过渡属于 $1+I$，其实际 analytic 部分是同一
  $G(b_\xi(t))^2/(C_\xi t^{6a_\xi})$，代入
  $t=c_\xi\pi_0^m\psi$；
- centre–node 过渡也属于 $1+I$，准确保留 $\sigma_\xi$。
  在此 overlap 上 $z_D=\rho_\xi\pi_0^3/w$，
  所以 $\sigma_\xi-1$ 从 $\pi_0^{p+1}$ 起。

不在全 node 上对非 $1+I$ 的 static unit 取 log。改变节点的实际整延伸只在两个接口添加互相抵消的有限 Čech coboundary。$1+p$ 的仿射 frame 差在 $A_M$ 为零。same quotient 的 $pR_Q$ 亦在该有限来源中消失；没有在一个非单位参数上先除 $p$ 再删去余项。

定义零常数的合法 analytic log
$$
L_\xi(t)=
 \log\frac{G(b_\xi(t))^2}{C_\xi t^{6a_\xi}}
=\sum_{j\ge1}\ell_{j,\xi}t^{3j}.
\tag{1209.29}
$$
这里 $\mu_3$ 及原 good target 使其只含 $t^3$ 的幂。由原
$\lambda=-6(b+1)/r$ 和 (1209.9)，
$$
\frac d{dt}\log G(b_\xi(t))^2
=\frac{6(\xi^2b+\xi)F^2}{v}.
$$
另定义 $6F^2/v=6/t+L_0'$，取 $L_0(0)=0$。所以
$$
L_\xi=\xi^2L_1+\xi L_0.
\tag{1209.30}
$$
这个等式同时保留了三个实际 divisor 系数，因为
$a_\xi=\xi^2+\xi$。

乘 $\Omega_S$ 的第 $N_k$ 层时，只有
$$
3mj+N_k=m^2
\iff j+k=n+1
$$
贡献目标 normal。所有 $j,k$ 都小于 $p$。完整极界亦排除
static 无限 log 的隐藏 $p$ 分母返回，证明沿 R1208 §6：
若 $s=v_p(j)\ge1$，有效阶至少
$1+(p+1)(j-ms)>m^2$。因此此处使用原 finite Picard log 已经读全，未遗漏较高项。

在 $U,V$ 模型上，
$$
\psi^{m-1}F_{\rm tail}\eta=
\frac12 V^{m^2-2}
 (1+A_\xi^{\rm tail}V^{-p-1})^{-L}\,dV.
$$
唯一 residue 指标为 $L$，
$\binom{-L}{L}=c_m/2$。$U,V$ 模型到实际 CM 尾
$x_D=V^6,y_D=UV^3$ 在此无穷分歧指数为三，故
$$
\operatorname{Res}_{D,\infty}
 \psi^{m-1}F_{\rm tail}\eta
=-\frac{c_m(A_\xi^{\rm tail})^L}{12}.
\tag{1209.31}
$$
这也可在全部 full 分支上计算后按原 trace 除以六；不可把 intermediate 模型的 residue 直接当粗尾 residue。

由 $\Theta\psi=-\psi^2$ 分部积分，两个符号相消，得到
$$
\operatorname{Res}_{D,\infty}\psi^{3j}\,dH_k
=-\frac{(-1)^{k-1}c_m(A_\xi^{\rm tail})^L(m-2)!}
 {2(3j-1)!(3k)!}.
\tag{1209.32}
$$

将 (1209.14)、实际 $c_\xi^{3j}\ell_{j,\xi}$ 代入。
R1208 的 canonical phase 与 (1209.11) 给
$$
\frac{c_\xi^{m+1}(A_\xi^{\rm tail})^L}{\tau_\xi}
=\frac{\tau_\xi^{m-1}(A_\xi^{\rm tail})^L}{A(\xi)}
=\frac{\nu\xi}{A_1}.
\tag{1209.33}
$$
又 $\sum_\xi\xi\ell_{j,\xi}=3\ell_j$，所以全部 CM analytic 项恰为
$$
\boxed{\quad
\mathcal V_{\rm CM,an}(S)=
\frac{3m c_m\nu(m-2)!}{A_1}\mathcal A_S.
\quad}
\tag{1209.34}
$$
由于
$2m!=2m(m-1)(m-2)!=-3m(m-2)!$，
(1209.34) 与 (1209.28) 的全部 regular 项逐项相消。

## 8. 保留的 static top 项及完整端点公式

static 单位没有正 normal 系数，因此本层只配 $\Omega_S$ 的
$N_{n+1}=m^2$ 层。R1208 已从原 $e_D/e_I$ 严格锁定其加号，并证明
$$
\operatorname{Res}_\infty
 \bigl[-3a_\xi\log(1+A_\xi^{\rm tail}z_D^{4g})\bigr]\,dH_{n+1}
=4a_\xi(2c_m-2^m)(A_\xi^{\rm tail})^L .
\tag{1209.35}
$$
这里只用其有限 centre-overlap log；$\Omega_S$ 的较早 CM 层不被默认删除，它们已全部进入 §7 的 analytic 求和。

置 $d=d_{n+1}=-1/4$。由 (1209.14)、(1209.33)，
$$
\gamma_{n+1,\xi}(S)(A_\xi^{\rm tail})^L
=\frac{m\nu\xi}{3dA_1}e_n(S).
$$
所以
$$
\mathcal V_{\rm CM,st}(S)
=\frac{8\nu}{A_1}(2c_m-2^m)e_n(S).
\tag{1209.36}
$$
这里使用原 $\sum_\xi a_\xi\xi=3$，没有换 CM 点或 divisor。

加总 (1209.28)、(1209.34)、(1209.36)，所有正次收缩和
$c_m$ 项都精确抵消，得到 (1209.1)。由
$H_{n+1}(Q_\xi)=-4\,2^m(A_\xi^{\rm tail})^L$，
还可等价写成
$$
\boxed{\quad
\mathcal V_m(S)
=\sum_{\xi^3=1}
 a_\xi\,\gamma_{n+1,\xi}(S)\,H_{n+1}(Q_\xi).
\quad}
\tag{1209.37}
$$
这是完成全部原节点计算后的等式，不是预先把全图配对替成三个点的评价。

对 $S=T_*=-r^n$，(1209.12) 给 $e_n=1/A_1$，所以 (1209.1) 准确还原 R1208 的
$-8\,2^m\nu/Q_0^2$。这也保留了已更正的 static 边界，未重新使用 R1199 §6 的旧删除论证。

## 9. 原 PS 返回的更短系数式

保持 R1204/R1206 的
$$
\mathscr DT=rT''-4b^2T'-\frac94bT,\qquad
T=b^2P(b^3),\quad\deg P\le n-1,
$$
以及同一个实际有理 primitive
$$
f_T=\frac r u(T/A)',\qquad df_T=\frac{\mathscr DT\,db}{uA}.
$$
只在 $\xi=1$ 记 $R(t)=T(b(t))/A(b(t))$。
沿 (1209.8)、(1209.11)，逐项化简得
$$
f_T=-\tau_1^{-1}W^{-m-1}\,tR'(t).
\tag{1209.38}
$$
这里的 $W$ 是原节点坐标；没有重新选 primitive 的常数或删除 SS 的 $p$ 阶极部。

由 $dt=mt\,dW/W$，比较 $df_T$ 与
$\tau_1^{-1}W^{-m-1}\mathcal E_{\mathscr DT}(t)\,dt$，得到
$$
\mathcal E_{\mathscr DT}
=\frac1mR'-tR''=-(tR)''.
\tag{1209.39}
$$
$R$ 只含 $t^3$ 的幂。因此
$$
\boxed{\quad
e_n(\mathscr DT)
=-(m+1)(m+2)[t^{m+1}]R(t).
\quad}
\tag{1209.40}
$$
这证明 (1209.2)。所有指数和微分均在 $<p$ 的实际有限 jet 内。

该结论现在可直接作用于 R1205 识别的实际纯尖点底空间
$\operatorname{im}\mathcal C=\ker\mathfrak c$；是否得到单位，须对所选同源 $T$ 计算 (1209.40)。本文没有由 packet 单位假定整个纯型上的非零，更没有跳过指定 $C$ 的真实整投影或全 MW 比较。

## 10. 来源与范围

- R1014、R1018 §5/(1018.19)、R1021、R1023：同一个 $G(b_{\rm lift})^2$、target ordinary quotient、full-$p$ 非约化坐标、原 $\psi$、全部 node 及 canonical 单位。
- R1196：原 $P=(p-1)D_0$ 的有限 Picard log、Serre 方向和同底提升独立性。
- R1197、R1208 §3：完整 CM normal 的 polynomial representative、同一 determinant 运输、一维 $E_m$ 图像和顶层终端因子。本文 §3 保留一般混合列，未把仅在前 jets 消失时成立的旗标公式误用。
- R1198 §2.1：同 target 的有限 PD/晶体比较；本文在同一合法范围延至 $m+1<p$。一手来源仍为 W. Messing, *The Crystals Associated to Barsotti–Tate Groups: with Applications to Abelian Schemes*, LNM 264, Springer, 1972，Chapter V §1 Theorems 1.6、1.10 和 §2 Theorem 2.1，[正式 DOI](https://doi.org/10.1007/BFb0058301)，[原书 PDF](https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/messing72.pdf)；有限环、角色和逐阶单位分母在本文明示。
- R1199–1201：原 generic normal、canonical 相位、exact quadrature、有限 RC 及其 framing 恒等式；本文把一般积分项、端点误差和全部 CM 项完整接上。
- R1204–1206：同一实际返回及完整 primitive；R1207–1208：整个非约化 CM 截面、原 static frame 修正、真实加号、最高 primitive 常数和 CM canonical 相位。

全文为纸面证明，没有运行数学程序，也没有重复有限窗口扫描。global_route 推导原全列消去与节点来源；root 独立核一般 RC 次数界、Gauss 端点误差及返回低 jet；o2_high_coefficient 独立核 (1209.31)–(1209.34) 的 ramification、factorials 和正负号。核验范围以实际逐式证明为准，不构成发布前额外审批。

