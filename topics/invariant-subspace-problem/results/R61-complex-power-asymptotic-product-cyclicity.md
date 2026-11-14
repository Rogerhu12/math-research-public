# R61：复幂次渐近尾的临界乘积与两乘积全线性组合循环

日期：2026-11-12（UTC）。子任务：critical_kernel。

**状态：已证明的中间结论。** 本条将 R60 的双尺度估计推广到有界复底参数、非零复主系数、一个明确的幂指数区间，以及通常全纯演算意义下的解析单位前因子。随后完整归约两个不同 R16 乘积及任意有限前缀的临界线性组合。它不处理任意衰减率的两个乘积，也不证明一般 $L^2$ 向量循环。

依赖：R9/R12/R44 的真实有限链与归一化幂估计；R16 的乘积循环性和精确尾分解；R24 的复对称性；R32 的解析代数、单点谱；[R60](../results/R60-critical-multiplier-injective-dense-and-cyclic.md) §1 的加权多项式估计；[严格负积分证书](../notes/2026-11-12-critical-negative-integral-certificate-0c.md)。全部新增的复参数、对数、截断、指数变化及两乘积归约在下文证明。

## 1. 精确的参数及结论

沿用实际 odometer $A$、权 $a_j$ 和
$$
N_j=A^{2^j}/W_{2^j},\qquad
\eta_j=a_{j+1}/a_j,\qquad E_j=e_{10}^{(j)}.
$$
所需事实为
$$
\|N_j\|=1,\quad N_j^2=\eta_jN_{j+1},\quad
\|N_j-E_j\|=\eta_j,\quad
\eta_j\le e^{-770\,16^j}.
\tag{1.1}
$$
有限链截断 $A_k$ 满足
$$
A_k^{2^k}=0,\qquad \|A-A_k\|=a_k,
$$
$$
N_j^{[k]}=A_k^{2^j}/W_{2^j},\qquad
\|N_j-N_j^{[k]}\|=a_k/a_j\quad(j<k).
\tag{1.2}
$$
它们都是正权路径的删减，故对每个 $n$，
$$
\|(N_j^{[k]})^n\|\le\|N_j^n\|,
\qquad \|A_k^n\|\le\|A^n\|.
\tag{1.3}
$$

取两个有界复数列 $(s_j),(t_j)$，置
$$
\delta_j=s_j-t_j.
$$
假设存在 $c\in\mathbb C\setminus\{0\}$ 及
$$
\boxed{1<p\le\frac{12}{5}}
\tag{1.4}
$$
使
$$
\boxed{
\delta_j=c(j+2)^{-p}(1+\varepsilon_j),
\qquad\varepsilon_j\longrightarrow0.
}
\tag{1.5}
$$
因此 $\delta\in\ell^1$。有限多个 $s_j,t_j$ 可以是任意复数，不要求实数、非零或有序；只要求这两个完整数列有界。

令 $R$ 是某个含 $0$ 的复邻域上解析的标量函数，满足 $R(0)=1$。$R(A)$ 使用通常全纯演算，等价地使用在 $0$ 展开的 Taylor 级数：$A$ 拟幂零使其算子级数收敛。定义
$$
Q=R(A)\prod_{j\ge0}(I+t_jN_j)(I+s_jN_j)^{-1},
\qquad D=I-Q.
\tag{1.6}
$$

**定理 1.1。** (1.6) 的乘积按算子范数收敛，$Q$ 有界可逆且 $\sigma(Q)=\{1\}$。存在下文明确的拟幂零对数 $L$，使 $Q=e^{-L}$，并且
$$
\boxed{
\ker L=\ker D=\{0\},\qquad
\overline{LH}=\overline{DH}=H.
}
\tag{1.7}
$$

**关于解析前因子的范围。** 这里的 $R$ 必须是一个实际标量全纯函数的芽，且 $R(0)=1$。不把任意 $\mathcal A=\overline{\mathbb C[I,A]}$ 中常数系数为 $1$ 的单位，都当作这种 $R(A)$；R32 已说明这种偷换可能丢失有界除法与系数增长问题。第 8 节产生的 $R$ 是明确的有理函数芽，满足本假设。

## 2. 复对数和统一预解式常数

令
$$
S\ge\sup_j\max(|s_j|,|t_j|,1).
$$
每个 $N_j$ 拟幂零，故 $I+zN_j$ 对所有复 $z$ 可逆。截断 $N_j^{[k]}$ 幂零，亦如此。

存在只依赖 $S$ 的有限常数 $C_S$，同时满足
$$
\|(I+zN_j)^{-1}\|\le C_S,\qquad
\|(I+zN_j^{[k]})^{-1}\|\le C_S
\tag{2.1}
$$
对所有 $|z|\le S$、所有相应 $j,k$ 成立。证明如下。对充分大的 $j$，$S^2\eta_j\le1/2$，利用
$$
(I+zT)^{-1}=(I-zT)(I-z^2T^2)^{-1}
$$
可将范数控制为 $2(1+S)$。余下有限多个 $j$ 则由
$$
\sum_{n\ge0}S^n\|N_j^n\|<\infty
$$
及 (1.3) 共同控制，故可取最大值。

定义
$$
\ell_j(T)=\log(I+s_jT)-\log(I+t_jT)
=\int_{t_j}^{s_j}T(I+zT)^{-1}\,dz,
\tag{2.2}
$$
积分沿直线段。两个对数均指围绕谱点 $1$ 的通常解析支；也可用在 $z=0$ 出发的整个算子函数
$$
\log(I+zT)=\sum_{n\ge1}\frac{(-1)^{n+1}z^nT^n}{n}.
$$
当 $T=N_j$ 时，该级数因拟幂零性对每个固定 $z$ 按范数绝对收敛；截断时是有限和。因此没有通过复参数穿过标量主值割线的含糊选支。

由 (2.1)，
$$
\|\ell_j(N_j)\|\le C_S|\delta_j|,
\tag{2.3}
$$
所以对数总和按算子范数绝对收敛。

在 $0$ 邻域内取唯一满足 $\psi(0)=0$ 的解析芽
$$
\psi=-\log R.
$$
置
$$
L=\psi(A)+\sum_{j\ge0}\ell_j(N_j).
\tag{2.4}
$$
它属于 $\mathcal A$ 且常数系数为零，因此由 R32 拟幂零。各项彼此交换，而 (2.2) 的指数是对应可逆因子，故
$$
e^{-L}=R(A)\prod_j(I+t_jN_j)(I+s_jN_j)^{-1}=Q.
\tag{2.5}
$$
特别 $Q$ 可逆、$\sigma(Q)=\{1\}$。也可直接用
$$
(I+t_jN_j)(I+s_jN_j)^{-1}-I
=-\delta_jN_j(I+s_jN_j)^{-1}
$$
及 (2.1)、$\delta\in\ell^1$ 检查范数乘积收敛。

最后
$$
D=L\Psi(L),\qquad
\Psi(z)=\frac{1-e^{-z}}z,\quad\Psi(0)=1,
\tag{2.6}
$$
$\Psi(L)$ 可逆。因此只需证明 $L$ 单射稠密。

## 3. 真实进位与解析前因子的截断误差

### 3.1 对数差的统一控制

对任意两个相应的原幂或截断幂 $T,U$，预解式恒等式给
$$
T(I+zT)^{-1}-U(I+zU)^{-1}
=(I+zT)^{-1}(T-U)(I+zU)^{-1}.
$$
不要求 $T,U$ 相互交换。将此式沿 (2.2) 的线段积分，得到
$$
\boxed{
\|\ell_j(T)-\ell_j(U)\|
\le C_S^2|\delta_j|\,\|T-U\|.
}
\tag{3.1}
$$

又
$$
N_j(I+zN_j)^{-1}-N_j
=-zN_j^2(I+zN_j)^{-1}.
$$
由 (1.1)、(2.1)，
$$
\|\ell_j(N_j)-\delta_jN_j\|
\le SC_S|\delta_j|\eta_j.
$$
再替换 $N_j$ 为 $E_j$：
$$
\boxed{
\|\ell_j(N_j)-\delta_jE_j\|
\le (1+SC_S)|\delta_j|\eta_j.
}
\tag{3.2}
$$

### 3.2 实际解析芽的误差

对 $\psi$ 的 Taylor 系数取某个 $\rho>0$、$C<\infty$ 使
$$
\psi(z)=\sum_{n\ge1}b_nz^n,\qquad |b_n|\le C\rho^{-n}.
$$
$A$ 拟幂零，所以
$$
\sum_{r\ge0}\rho^{-r}\|A^r\|<\infty.
$$
幂差望远镜式及 (1.3) 给
$$
\|A^n-A_k^n\|
\le a_k\sum_{r=0}^{n-1}\|A^r\|\|A^{n-1-r}\|.
$$
从而
$$
\boxed{
\|\psi(A)-\psi(A_k)\|\le C_\psi a_k,
}
\tag{3.3}
$$
其中可取
$$
C_\psi=
\frac C\rho
\left(\sum_{r\ge0}\rho^{-r}\|A^r\|\right)^2<\infty.
$$
这一步正是需要真正全纯芽而不是任意 $\mathcal A$ 单位的地方。

### 3.3 两尺度所用的算子

定义
$$
G_k=\psi(A_k)+\sum_{j<k}\ell_j(N_j^{[k]}),
\qquad
T_k=G_k+\sum_{j\ge k}\delta_jE_j.
\tag{3.4}
$$
$G_k$ 是幂零 $A_k$ 的无常数项多项式，故
$$
G_k^{2^k}=0.
\tag{3.5}
$$
由 (1.2)、(3.1)—(3.3)，以及
$a_k/a_j\le\eta_{k-1}$（$j<k$）、$\eta_j\le\eta_k$（$j\ge k$），有一个与 $k$ 无关的常数 $C_0$，使
$$
\boxed{
\|L-T_k\|
\le C_0\eta_{k-1}\quad(k\ge1).
}
\tag{3.6}
$$
例如右边依次控制
$$
C_\psi a_k+
C_S^2\sum_{j<k}|\delta_j|\frac{a_k}{a_j}
+(1+SC_S)\sum_{j\ge k}|\delta_j|\eta_j.
$$
有限前缀和复参数只改变 $C_0$。同时 $\|G_k\|$ 一致有界，因为 (2.3)、(3.3) 和 $\sum|\delta_j|<\infty$ 给一致界。

## 4. 全部 $1<p\le12/5$ 的严格负常数

### 4.1 原区间的解析比较

沿用 R60 的区间 $[1,20]$、常数 $g_0$ 和概率测度
$$
g_0=\log\frac{\sqrt{20}+1}{\sqrt{20}-1},\qquad
d\nu(u)=
\frac{\sqrt{20}}{\pi u\sqrt{(u-1)(20-u)}}\,du.
$$
对任意实 $p>1$ 置
$$
h_p(u)=\frac12\int_1^\infty
\log\left(1-\frac{u}{x^p}+\frac{u^2}{2x^{2p}}\right)\,dx,
$$
$$
J_p=g_0+\int_1^{20}h_p(u)\,d\nu(u).
\tag{4.1}
$$
记 $P(q)=1-q+q^2/2$。对 $q\ge0$，
$$
\left|\frac{P'(q)}{P(q)}\right|
=\frac{2|q-1|}{1+(q-1)^2}\le1.
$$
在任意紧的 $p>1$ 区间内可用可积函数控制参数导数，因而
$$
\left|\frac{\partial}{\partial p}h_p(u)\right|
\le\frac u2\int_1^\infty\frac{\log x}{x^p}\,dx
=\frac{u}{2(p-1)^2}.
\tag{4.2}
$$
该谐测的第一矩为 $\int u\,d\nu=\sqrt{20}$（负积分证书 §3），故
$$
|J_p-J_2|
\le\frac{\sqrt{20}}2
\left|1-\frac1{p-1}\right|.
\tag{4.3}
$$
严格负积分证书已经证明 $J_2<-13/100$。当 $2\le p\le41/20$ 时，
$$
\left|1-\frac1{p-1}\right|\le\frac1{21},
\qquad \sqrt{20}<\frac92.
$$
因此在这一部分区间内，
$$
J_p<-\frac{13}{100}+\frac3{28}
=-\frac4{175}<0.
\tag{4.4}
$$

还可以只用一个符号变化把结论延伸到全部 $1<p\le2$。负积分证书的 20 个端点上界均不超过 $-111374/10^6$，全区间线性插值上界另加 $1/24$，所以
$$
\boxed{
h_2(u)\le-\frac{111374}{10^6}+\frac1{24}
=-\frac{104561}{1500000}<0
\quad(1\le u\le20).
}
\tag{4.5}
$$
在 $h_p$ 的积分中令 $y=p\log x$（不同 $p$ 各用这个代换），得到
$$
h_p(u)=\frac1{2p}\int_0^\infty
e^{y/p}\log P(ue^{-y})\,dy.
\tag{4.6}
$$
当 $1<p\le2$ 时，$p$ 权与 $2$ 权的比为
$$
r_p(y)=\frac2p
e^{(1/p-1/2)y}\ge1,
$$
且关于 $y$ 不减。若 $1\le u\le2$，则 $\log P(ue^{-y})\le0$ 对全部 $y\ge0$ 成立，立即得到 $h_p(u)\le h_2(u)$。

若 $u>2$，置 $y_0=\log(u/2)>0$。函数 $\log P(ue^{-y})$ 在 $y<y_0$ 为正，在 $y>y_0$ 为负。前半段 $r_p(y)\le r_p(y_0)$，后半段不等号反向但被负号反转，所以逐段积分给
$$
h_p(u)\le r_p(y_0)h_2(u)\le h_2(u),
\tag{4.7}
$$
最后使用了 (4.5) 和 $r_p(y_0)\ge1$。这些积分均绝对收敛，因为固定 $p>1$ 时尾为 $O(e^{-(1-1/p)y})$。

故 $1<p\le2$ 上 $J_p\le J_2<-13/100$。与 (4.4) 合并，
$$
\boxed{J_p<-\frac4{175}\qquad(1<p\le41/20).}
\tag{4.8}
$$
本节没有为新的 $p$ 做额外数值拟合；整个扩展只使用已经认证的有理端点表、解析参数导数界及上述单符号变化比较。各后续误差常数可以依赖固定的 $p$；没有声称在 $p\downarrow1$ 时也一致控制 $\sum|\delta_j|$ 或 $1/(p-1)$。

### 4.2 换区间后覆盖至 $12/5$

独立的[八点严格区间证书](../notes/2026-11-12-power-range-negative-integral-0c.md)及[可执行证书](../notes/2026-11-12-power-range-negative-integral-0c.py)证明
$$
J_p(1/10,30)<-\frac1{2000}\qquad(2\le p\le12/5).
\tag{4.9}
$$
该证书使用 $|h_p''|\le1/(2p-1)$、步长 $1/10$ 的精确线性插值权重、Acb 超几何端点闭式，以及八个有理指数的严格球上界。令 $v=1/(p-1)$ 后有 $|dJ/dv|\le\sqrt3/2<7/8$，八个精确有理邻域连续覆盖整个 $v\in[5/7,1]$；因此并非仅验证离散指数。全部公式、误差界、分支及覆盖数据均在所链接证书中。

今后给定固定的 $p\in(1,12/5]$，作以下选择：若 $p\le2$，取 $(a,b)=(1,20)$；若 $p>2$，取 $(a,b)=(1/10,30)$。令
$$
g_0=\log\frac{\sqrt b+\sqrt a}{\sqrt b-\sqrt a},\qquad
d\nu(u)=\frac{\sqrt{ab}}{\pi u\sqrt{(u-a)(b-u)}}\,du.
$$
则两种情形都满足
$$
\boxed{g_0+\int_a^b h_p(u)\,d\nu(u)<-\frac1{2000}.}
\tag{4.10}
$$
以下统一使用此处对应于给定 $p$ 的 $a,b,g_0,\nu$。

## 5. 复时间下的尾范数及一致 Riemann 极限

令
$$
C_m=\sum_{j\ge m}\delta_jE_j,\qquad M=m+2,
\qquad \tau=\tau_M(u)=\frac{M^p}{c}u,\quada\le u\le b.
\tag{5.1}
$$
$c$ 可以是任意非零复数；时间 $\tau$ 不必为实数。定义
$$
F_m(u)=\|e^{-\overline\tau C_m^*}1\|.
$$
各 $E_j$ 交换且平方为零，故
$$
F_m(u)=\prod_{j\ge m}
P_{\mathbb C}(\tau\delta_j)^{1/2},
\qquad
P_{\mathbb C}(z)=1-\operatorname{Re}z+\frac{|z|^2}{2}
=\frac{1+|z-1|^2}{2}.
\tag{5.2}
$$
无限乘积合法，因为每个固定 $m,u$ 有 $\sum_{j\ge m}|\tau\delta_j|<\infty$。各因子严格正，其对数尾绝对可和。

作为 $\mathbb R^2$ 上函数，
$$
\Lambda(z)=\log P_{\mathbb C}(z),\qquad
\|\nabla\Lambda(z)\|
=\frac{2|z-1|}{1+|z-1|^2}\le1.
\tag{5.3}
$$
所以 $\Lambda$ 全局 Lipschitz 常数为 $1$，且 $\Lambda(0)=0$ 给 $|\Lambda(z)|\le|z|$。

写
$$
e_m=\sup_{j\ge m}|\varepsilon_j|\longrightarrow0.
$$
对 $j=m+l$，由 (1.5)，
$$
\tau\delta_j=u(1+l/M)^{-p}(1+\varepsilon_j).
$$
用 (5.3) 比较到正实系数，得到
$$
\left|
\log F_m(u)
-\frac12\sum_{l\ge0}
 \log P\bigl(u(1+l/M)^{-p}\bigr)
\right|
\le\frac u2 e_m\left(1+\frac M{p-1}\right).
\tag{5.4}
$$
使用了递减函数的和积分界
$$
\sum_{l\ge0}(1+l/M)^{-p}
\le1+\frac M{p-1}.
$$

令 $f_u(x)=\frac12\log P(u/x^p)$。有
$$
|f_u'(x)|\le\frac{pu}{2}x^{-p-1},\qquad
\int_1^\infty|f_u'(x)|\,dx\le\frac u2.
$$
逐个网格区间积分导数的绝对值，得到
$$
\left|
\frac1M\sum_{l\ge0}f_u(1+l/M)
-\int_1^\infty f_u(x)\,dx
\right|
\le\frac{u}{2M}.
\tag{5.5}
$$
所以对整个 $u\in[a,b]$，
$$
\boxed{
|\log F_m(u)-M h_p(u)|\le r_m,
\qquad
r_m=\frac b2+\frac b2e_m\left(1+\frac M{p-1}\right)=o(M).
}
\tag{5.6}
$$
同样由 $|\Lambda(z)|\le|z|$ 可得，存在固定常数 $C_1$，使充分大的 $m$ 满足
$$
\boxed{F_m(u)\ge e^{-C_1M}\qquad(a\le u\le b).}
\tag{5.7}
$$
例如直接估计 $\frac12\sum|\tau\delta_j|$ 即可。这里的常数可依赖参数序列，但不依赖 $m,u$。

## 6. 真正核向量的多项式边界界

令
$$
k=\left\lfloor\frac34\log_2M\right\rfloor,
\qquad
H_{k,m}=G_k+\sum_{k\le j<m}\delta_jE_j.
$$
对充分大的 $M$，$1\le k<m$。各低位、中间位、尾部算子作用于不相交的位，因此
$$
T_k=H_{k,m}+C_m,\qquad [H_{k,m},C_m]=0.
$$
由 (3.5) 和中间段平方零因子的计数，
$$
H_{k,m}^{2^k+m-k}=0.
\tag{6.1}
$$
所以 $e^{\tau H_{k,m}}$ 是 $\tau$ 的次数至多
$$
d_m=2^k+m-k-1\le M+M^{3/4}
\tag{6.2}
$$
的多项式。同时存在固定 $C_2$ 使
$$
\|H_{k,m}\|+\|C_m\|\le C_2.
\tag{6.3}
$$

取 $f\in\ker L$。由 (3.6)，$\|T_kf\|\le C_0\eta_{k-1}\|f\|$。对复 $\tau$ 同样有沿线段的精确恒等式
$$
e^{\tau H_{k,m}}f-e^{-\tau C_m}f
=\tau\int_0^1
 e^{(1-s)\tau H_{k,m}}e^{-s\tau C_m}T_kf\,ds.
\tag{6.4}
$$
它只用头尾交换，不要求 $T_k$ 与实际 $L$ 交换。因此
$$
\|e^{\tau H_{k,m}}f-e^{-\tau C_m}f\|
\le C_0|\tau|e^{C_2|\tau|}\eta_{k-1}\|f\|.
\tag{6.5}
$$
而
$$
16^{k-1}\ge M^3/256,\qquad
|\tau|\le b|c|^{-1}M^p.
$$
由 $p\le12/5<3$，(1.1) 使 (6.5) 除以 $\|f\|$ 后不超过
$$
\exp\left[-\frac{770}{256}M^3+O(M^p+\log M)\right]
\le e^{-M^2}
\tag{6.6}
$$
对充分大的 $M$ 成立。初始指标可依赖序列及 $c$，但不依赖 $u\in[a,b]$。

定义复多项式
$$
p_m(u)=\langle e^{(M^p/c)uH_{k,m}}f,1\rangle.
\tag{6.7}
$$
其次数不超过 $d_m$，且 $p_m(0)=\langle f,1\rangle$。另一方面，
$$
|\langle e^{-\tau C_m}f,1\rangle|
=|\langle f,e^{-\overline\tau C_m^*}1\rangle|
\le\|f\|F_m(u).
$$
由 (5.7)，$e^{-M^2}\le F_m(u)$ 对充分大的 $M$ 一致成立。故 (5.6)、(6.5)—(6.6) 给
$$
\boxed{
|p_m(u)|\le2\|f\|\exp(Mh_p(u)+r_m),
\qquada\le u\le b.
}
\tag{6.8}
$$

## 7. 加权多项式估计完成实际单射与稠密值域

R60 §1 自含证明：对次数至多 $d$ 的复多项式 $P$，
$$
\log|P(0)|
\le d g_0+\int_a^b\log|P(u)|\,d\nu(u).
\tag{7.1}
$$
零多项式直接处理，区间上的零点不妨碍可积的对数上界。将 (6.8) 代入，得
$$
\begin{aligned}
\log|\langle f,1\rangle|
&\le\log(2\|f\|)+r_m+d_mg_0
  +M\int h_p\,d\nu\\
&\le\log(2\|f\|)+r_m+g_0M^{3/4}
  -\frac1{2000}M.
\end{aligned}
\tag{7.2}
$$
因 $r_m=o(M)$，右边趋向 $-\infty$，所以 $\langle f,1\rangle=0$。

$L\in\mathcal A$ 与 $A$ 交换，故每个 $A^nf$ 也在 $\ker L$。再次应用刚证明的零均值：
$$
\langle f,(A^*)^n1\rangle
=\langle A^nf,1\rangle=0\qquad(n\ge0).
$$
R11/R24 证明 $1$ 对 $A^*$ 循环，所以 $f=0$。

所有 $\mathcal A$ 元素满足 $C L^*C=L$，其中
$$
Cf(y)=\overline{f(-1-y)}.
$$
因此 $\ker L^*=C(\ker L)=0$，即 $L$ 值域稠密。由 (2.6)，同样得到 $D$ 单射且值域稠密，完成定理 1.1。所有有限正整数幂 $D^r,L^r$ 也单射稠密。

## 8. 两个不同 R16 乘积的全线性组合

**定理 8.1。** 设 $g,h$ 是两个非零 R16 向量，各自允许任意有限非乘积前缀。对充分高的每一位，把归一化局部因子分别写为 $g_j,h_j$，令
$$
s_j=\frac{g_j(1)}{g_j(0)},\qquad
t_j=\frac{h_j(1)}{h_j(0)}.
$$
假设它们满足 (1.5)，其中 $c\ne0$、$p$ 满足 (1.4)。则对任意 $(\alpha,\beta)\ne(0,0)$，
$$
\boxed{\alpha g+\beta h\ne0,\qquad
\alpha g+\beta h\text{ 对 }A\text{ 循环}.}
\tag{8.1}
$$
不要求 $s_j,t_j$ 实数或有序；它们各自可来自任意慢收敛、非连续的收敛乘积。

### 8.1 尾部映射的常数归一化

选共同截点 $d$，吸收两个任意有限前缀及所有局部零因子，使 $j\ge d$ 上局部零坐标、局部均值都非零，且相应尾均值的无限乘积非零。后一个选择由 R16 的 $L^2$ 收敛保证：足够远的有限尾乘积一致趋近参考常数 $1$，其均值乘积因而一致接近 $1$。

写
$$
g=v\otimes g_{\rm tail},\qquad
h=w\otimes h_{\rm tail},
\qquad v,w\in\mathbb C^{2^d}\setminus\{0\},
$$
尾部局部因子都归一化为范数一。R16 给 $s_j,t_j\to1$，故有界。

令
$$
\kappa_N=\prod_{j=d}^{N-1}\frac{h_j(0)}{g_j(0)}.
$$
设 $\mu_j^g=(g_j(0)+g_j(1))/2$，$\mu_j^h$ 类似。恒等式
$$
\frac{h_j(0)}{g_j(0)}
=\frac{\mu_j^h}{\mu_j^g}\,
 \frac{1+s_j}{1+t_j}
\tag{8.2}
$$
说明 $\kappa_N$ 收敛到某个 $\kappa\ne0$：第一部分的有限乘积是两个已收敛到非零数的尾均值乘积之比；第二部分满足
$$
\frac{1+s_j}{1+t_j}-1=\frac{\delta_j}{1+t_j}\in\ell^1
$$
且各因子非零。因此没有要求相对局部相位逐项绝对可和。

定义
$$
Q_{\rm tail}=\prod_{j\ge d}
 (I+t_jN_j)(I+s_jN_j)^{-1},
\qquad Y=\kappa Q_{\rm tail}.
\tag{8.3}
$$
由第 2 节，$Y$ 是 $\mathcal A$ 中的有界可逆算子，其常数系数为 $\kappa$。

该算子确实逐位把 $g_{\rm tail}$ 送到 $h_{\rm tail}$。验证单个位时，将当前局部因子写为
$$
g_j(0)(1,s_j)\otimes u
=g_j(0)(I+s_jN_j)((1,0)\otimes u).
$$
这里 $N_j((1,0)\otimes u)=(0,1)\otimes u$ 是实际进位模型中的精确式，非 $E_j$ 近似。作用相应因子及标量 $h_j(0)/g_j(0)$ 后，恰变为 $h_j(0)(1,t_j)\otimes u$，其余位不变。有限乘积逐位切换，最后用两个精确尾向量都趋向 $1$ 及 (8.2) 的常数收敛，得
$$
Y(e_0\otimes g_{\rm tail})=e_0\otimes h_{\rm tail}.
\tag{8.4}
$$
$Y$ 在低 $d$ 位上为恒等作用乘尾算子。

### 8.2 有限前缀化成真正的多项式因子

令 $N=2^d$、$\xi=e_0\otimes g_{\rm tail}$。R16 保证 $\xi$ 循环。对 $0\le n<N$，
$$
A^n\xi=W_n e_n\otimes g_{\rm tail},
$$
因为从头坐标 $0$ 走到 $n$ 尚未跨过此低位块边界。因此存在明确非零多项式
$$
p_v(z)=\sum_{n=0}^{N-1}\frac{v_n}{W_n}z^n,\qquad
p_w(z)=\sum_{n=0}^{N-1}\frac{w_n}{W_n}z^n
$$
使
$$
g=p_v(A)\xi,\qquad h=p_w(A)Y\xi.
\tag{8.5}
$$
分解这些有限多项式：
$$
p_v(z)=z^r u_v(z),\qquad
p_w(z)=z^s u_w(z),\qquad
u_v(0)u_w(0)\ne0.
\tag{8.6}
$$
$u_v(A),u_w(A)$ 有界可逆。这是对实际有限多项式的因式分解，没有对一般 $\mathcal A$ 元素擅自有界除以 $A$。

### 8.3 不同首阶与唯一临界系数

若 $\alpha=0$ 或 $\beta=0$，(8.1) 已由 R16 成立。以下两系数都非零。

若 $r<s$，则
$$
\alpha g+\beta h
=A^r u_v(A)
\left[\alpha I+\beta A^{s-r}u_w(A)u_v(A)^{-1}Y\right]\xi.
$$
方括号中第二项除去标量后拟幂零，因为它是 $A$ 的正次幂乘一个与 $A$ 交换的有界算子。故方括号可逆。$r>s$ 时交换两个角色并使用 $Y^{-1}$ 得同样结论。$A$ 单射稠密，所以所得向量非零且循环。

若 $r=s$，置
$$
T=u_w(A)u_v(A)^{-1}Y,\qquad
q_0=\frac{u_w(0)}{u_v(0)}\kappa\ne0.
$$
$T\in\mathcal A$，$\sigma(T)=\{q_0\}$。当 $\alpha+\beta q_0\ne0$ 时，$\alpha I+\beta T$ 可逆，结论仍成立。

最后考虑唯一临界关系 $\alpha+\beta q_0=0$。此时
$$
\alpha I+\beta T=\alpha(I-\widetilde Q),
$$
其中
$$
\widetilde Q=T/q_0=R(A)Q_{\rm tail},
\qquad
R(z)=
\frac{u_w(z)/u_v(z)}{u_w(0)/u_v(0)}.
\tag{8.7}
$$
$R$ 是在 $0$ 邻域解析的具体有理单位，$R(0)=1$。将 $j<d$ 的底参数补成 $s_j=t_j=0$，尾部仍满足 (1.5)。定理 1.1 因而保证 $I-\widetilde Q$ 单射且值域稠密。

于是
$$
\alpha g+\beta h
=\alpha A^r u_v(A)(I-\widetilde Q)\xi
$$
非零。右边各有界算子都与 $A$ 交换，且它们的乘积值域稠密；作用于循环 $\xi$ 后仍循环，因为轨道闭包等于该乘积值域的闭包。这完成全部系数情形。

## 9. 确切的扩展范围与未解问题

本条严格覆盖：

1. 有界复底参数 $s_j,t_j$，差具有非零复主项 $c(j+2)^{-p}$；
2. 全部 $1<p\le12/5$，尾部允许任意无速率的相对 $o(1)$ 误差；
3. 任意有限复前缀，以及真正标量全纯芽提供的单位前因子；
4. 对应两个 R16 乘积的任意非平凡线性组合，包括各自任意有限非乘积前缀。

本条没有覆盖任意 $\ell^1$ 尾差、变换相位而无非零渐近主系数的尾差、任意 $\mathcal A$ 单位前因子，或任意三个乘积的线性组合。它也没有排除本模型的一般普通不变子空间。

更大的指数范围可沿同一机制继续：对任意 $1<p<4$，只要另证同类标量常数 $J_p<0$，可取 $p/4<\beta<1$、$k=\lfloor\beta\log_2M\rfloor$。此时 $16^k\asymp M^{4\beta}$ 压过复时间的 $M^p$，而头多项式次数 $2^k=O(M^\beta)=o(M)$。本条只认证 (1.4) 的负号；对其他指数不把这个条件性机制误写成已证结论。

