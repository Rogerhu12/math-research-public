# R71：多尺度 Newton 权与超快横向尾

日期：2026-11-12（UTC）。经主会话逐段核验。

**状态：本条两个充分条件均已证明。一般不规则独立次主尾的所有临界组合仍未解决。**

依赖：R60–R61 的实际 BW 机制及 $1<p\le12/5$ 的负积分证书；R67 的真实正支配构造；[R69](R69-higher-critical-combinations-and-gevrey-bounds.md)的单变量幂界及一般 BW 搬运引理。下面把新增的多尺度幂估计、解析理想分解和超快尾全部证明写出。

为避免与归一化幂的范数记号混淆，主尾统一记为
$$
\theta_j=(j+2)^{-p},\qquad 1<p\le12/5.
$$
基准对数取
$$
L=\sum_j[\log(I+N_j)-\log(I+(1-\theta_j)N_j)].
\tag{0.1}
$$

## 1. 真实多尺度变量的幂界

### 1.1 可验证的局部表示

考虑有限个交换算子 $Y_\ell\in\mathcal A$，其常数项为零。以下具体条件足以赋予 $Y_\ell$ 一个指数 $p_\ell\in(1,4)$：
$$
Y_\ell=\psi_\ell(A)+\sum_{j\ge J}f_{\ell,j}(N_j),
$$
$$
f_{\ell,j}(z)=\xi_{\ell,j}z+\sum_{n\ge2}a_{\ell,j,n}z^n,
\tag{1.1}
$$
其中 $\psi_\ell$ 是实际零常数标量解析芽，
$$
|\xi_{\ell,j}|\le C_\ell(j+2)^{-p_\ell},\qquad
|a_{\ell,j,n}|\le\gamma_{\ell,j}S_\ell^{n-1},
\qquad
\sum_j\gamma_{\ell,j}<\infty.
\tag{1.2}
$$
所有有限初始位可并入 $\psi_\ell(A)$。取充分大的 $J$，使
$S_\ell^2\eta_j<1/2$。

逐项取绝对系数，构造
$$
B_\ell=\psi_{\ell,\#}(A)+
\sum_{j\ge J}\left[
|\xi_{\ell,j}|N_j+
\gamma_{\ell,j}\sum_{n\ge2}S_\ell^{n-1}N_j^n\right].
\tag{1.3}
$$
这是函数格正算子，按范数收敛，并且
$|Y_\ell f|\le B_\ell|f|$。高次局部项范数为
$O_{S_\ell}(\gamma_{\ell,j}\eta_j)$。

用 $A_k,N_j^{[k]}$ 截断所有低位，得到零常数多项式
$B_{\ell,k}(A_k)$。其误差分三部分：

- 解析芽误差为 $O(a_k)$；
- 全部 $j<k$ 的局部截断误差总和不超过
  $$C\sum_{j<k}(|\xi_{\ell,j}|+\gamma_{\ell,j})a_k/a_j
  \le C'\eta_{k-1};$$
- $j\ge k$ 的一阶纯位替换及高次项总误差不超过
  $$C\sum_{j\ge k}(|\xi_{\ell,j}|+\gamma_{\ell,j})\eta_j
  \le C'\eta_{k-1}.$$

因此
$$
\left\|B_\ell-B_{\ell,k}(A_k)
-\sum_{j\ge k}|\xi_{\ell,j}|E_j\right\|
\le C\eta_{k-1},
\tag{1.4}
$$
且 $B_{\ell,k}^{2^k}=0$、$\sup_k\|B_{\ell,k}\|<\infty$。

R69 的真实 Gevrey 引理因而给
$$
\boxed{\|Y_\ell^n\|\le
C_\ell^n(n!)^{-(p_\ell-1)}\qquad(n\ge1).}
\tag{1.5}
$$
这里可以用不同的正算子 $B_\ell$；不需要一个同时保持全部不同指数的共同正支配。

对实际局部对数
$$
L_i=\psi_i(A)+\sum_j[
\log(I+s_{i,j}N_j)-\log(I+t_{i,j}N_j)]
$$
及 $R_i=L_i-c_iL$，若其一阶余项是 $O(j^{-q_i})$，而局部底参数有界、原差为 $O(j^{-p})$，则 (1.1)—(1.2) 成立，指数可取 $p_\ell=q_i<4$。高次系数仍仅需由 $O(j^{-p})$ 支配；不必也不能强迫它们随更快的一阶余项一起缩小。

$A$ 本身可以赋予任意固定的 $p_\ell<4$，因为其尾系数全为零、真实截断误差为 $a_k=O(e^{-c16^k})$。

## 2. 加权 Newton 最小次数给出精确增长指数

给每个变量 $y_\ell$ 赋正权
$$
\omega_\ell=p_\ell-1>0.
$$
对多重指标 $\nu$ 定义
$$
\operatorname{wt}(\nu)=\sum_\ell\omega_\ell\nu_\ell.
$$

**定理 2.1。** 设 $\Phi(y)$ 是非零零常数解析芽，其每个非零 Taylor 单项式都满足
$$
\operatorname{wt}(\nu)\ge\Lambda>0.
\tag{2.1}
$$
若实际交换变量满足 (1.5)，则对 $Z=\Phi(Y)$ 存在固定 $C$，使
$$
\boxed{\|Z^n\|\le C^n(n!)^{-\Lambda}\quad(n\ge1),}
\tag{2.2}
$$
以及
$$
\boxed{\|e^{tZ}\|
\le\exp\bigl(C'|t|^{1/(1+\Lambda)}\bigr)
\quad(t\in\mathbb C).}
\tag{2.3}
$$

**证明。** 先证明有限单项式理想的情况。设
$$
\Phi(y)=\sum_{a=1}^N y^{\nu^a}g_a(y),
\qquad \operatorname{wt}(\nu^a)\ge\Lambda,
\tag{2.4}
$$
各 $g_a$ 是解析芽。令 $Z_a=Y^{\nu^a}g_a(Y)$。交换性给
$$
\begin{aligned}
\|Z_a^n\|
&\le\|g_a(Y)\|^n\prod_\ell\|Y_\ell^{\nu_\ell^an}\|\\
&\le C_a^n
\prod_\ell[(\nu_\ell^an)!]^{-\omega_\ell}\\
&\le C_a^n(n!)^{-\operatorname{wt}(\nu^a)}
\le C_a^n(n!)^{-\Lambda}.
\end{aligned}
\tag{2.5}
$$
对 $\nu_\ell^a=0$ 的因子按一处理；其余用
$(kn)!\ge(n!)^k$。

由有限个 $Z_a$ 彼此交换，
$$
\|Z^n\|
\le\sum_{\substack{n_1+\cdots+n_N=n\\n_a\ge0}}
\frac{n!}{\prod_an_a!}
\prod_a\frac{C_a^{n_a}}{(n_a!)^\Lambda}.
$$
多项式系数界
$n!/\prod_an_a!\le N^n$
给
$$
(\prod_an_a!)^{-\Lambda}
\le N^{\Lambda n}(n!)^{-\Lambda}.
$$
再用多项式定理，得到
$$
\|Z^n\|
\le[N^\Lambda(C_1+\cdots+C_N)]^n(n!)^{-\Lambda},
$$
即 (2.2)。

为由 (2.1) 得到 (2.4)，取
$K_\ell=\lceil\Lambda/\omega_\ell\rceil$。任何满足 (2.1) 的单项式，或者被某个 $y_\ell^{K_\ell}$ 整除，或者其全部指数都处于有限盒子
$0\le\nu_\ell<K_\ell$。把轴向单项式及该盒子中满足 (2.1) 的单项式作为有限生成元。每个原项按固定次序分配给一个整除它的生成元，便得到 (2.4)。各商级数在一个稍小的多圆盘内绝对收敛，因此确是解析芽。所有生成元的权均至少为 $\Lambda$。

最后置 $s=1+\Lambda>1$：
$$
\|e^{tZ}\|
\le\sum_{n\ge0}\frac{(C|t|)^n}{(n!)^s}
\le
\left(\sum_{n\ge0}\frac{(C|t|)^{n/s}}{n!}\right)^s
=e^{s(C|t|)^{1/s}},
$$
证明 (2.3)。证毕。

可以取 $\Lambda$ 为 Newton 支撑关于正权向量 $\omega$ 的最小值。由于各权为正，这个最小值在一个有限集合中达到。结论不需要预先把解析芽截成有限多项式。

## 3. Newton 余项与任意已证负 BW 尾的组合

设实际 $S\in\mathcal A$ 具有 R69 §6 的条件：真实低位误差 $O(\eta_{k-1})$，复时间尺度 $\tau_m$，一个固定区间上的统一尾界
$$
\log\|e^{-\overline{\tau_mu}C_m^*}1\|
\le Mh(u)+o(M),\qquad
\|e^{-\overline{\tau_mu}C_m^*}1\|\ge e^{-CM},
$$
以及
$$
g_{a,b}+\int h\,d\nu_{a,b}<0,\qquad
|\tau_m|=o(M^3),\qquad M=m+2.
\tag{3.1}
$$
这些都是需验证的实际条件；不从“次主尾很小”自动推定。

**推论 3.1。** 若 $Z=\Phi(Y)$ 满足定理 2.1，$S$ 与它交换，并且
$$
\boxed{|\tau_m|^{1/(1+\Lambda)}=o(M),}
\tag{3.2}
$$
则 $S-Z$ 单射且值域稠密。

证明是把 (2.3) 代入 R69 的核上恒等式和实际 Duhamel 误差。核向量满足 $e^{tS}f=e^{tZ}f$；(3.2) 恰给边界所需的 $e^{o(M)}$ 因子。没有把 $Z$ 与近似头尾的交换性当作条件。

例如若 $S$ 的实际一阶尾满足
$\sigma_j\sim c(j+2)^{-q_0}$、$c\ne0$、$1<q_0\le12/5$，则 R61 的证书给 (3.1)，取 $\tau_m=M^{q_0}/c$；此时只需
$$
q_0<1+\Lambda.
\tag{3.3}
$$
R64 的移动复归一化或平均相位缺陷也可直接代入，仍需保留各自的已证假设。

## 4. 有限乘积和的多阶主矩消去

考虑
$$
X=\sum_i a_i(A)e^{-L_i},\qquad
\alpha_i=a_i(0),\qquad
L_i=c_iL+R_i,
\tag{4.1}
$$
其中 $a_i$ 是实际标量解析芽。假设某个整数 $d\ge2$ 满足
$$
\sum_i\alpha_i c_i^k=0\qquad(0\le k<d).
\tag{4.2}
$$
不要求横向算子之间有线性恒等式。

令
$$
S=\sum_i\alpha_iR_i-\sum_i(a_i(A)-\alpha_i).
\tag{4.3}
$$
由于 (4.2) 的 $k=1$ 式，它也等于
$\sum_i\alpha_iL_i-\sum_i(a_i(A)-\alpha_i)$。精确写
$$
X=-S+Z.
$$
以 $w$ 代表 $L$、$y$ 代表 $(A,R_1,\ldots,R_r)$。则：

- 所有 $y=0$ 的纯 $w$ 项在次数 $d$ 以下消失，来自 (4.2)；
- $Z$ 的全部总次数零和一次项消失，来自实际选择 (4.3)。

因此确有解析理想归属
$$
\boxed{Z\in(w^d,\ wy_\ell,\ y_\ell y_{\ell'}).}
\tag{4.4}
$$
这是逐个 Taylor 单项式的分类：无 $y$ 因子的项至少含 $w^d$；只含一个 $y$ 因子的项必须再含 $w$；其余至少含两个 $y$。用第 2 节的绝对收敛分组即可得到实际解析系数，而非只得到形式级数。

假设全部横向 $R_i$ 的一阶尾为 $O(j^{-q})$，其中
$$
p<q<4.
$$
由第 1 节，$L$ 的权为 $p-1$，横向变量及 $A$ 的权可取 $q-1$。于是
$$
\Lambda=
\min\{d(p-1),\,p+q-2,\,2q-2\}
=\min\{d(p-1),\,p+q-2\}.
\tag{4.5}
$$
得到完整指数估计
$$
\boxed{
\log\|e^{tZ}\|
=O\!\left(
|t|^{1/\min\{d(p-1)+1,\ p+q-1\}}
\right).}
\tag{4.6}
$$

若实际合成尾
$$
\sigma_j=\sum_i\alpha_i\epsilon_{i,j}
$$
有幂律指数 $q_0\le12/5$，则推论 3.1 的充分条件为
$$
\boxed{q_0<d(p-1)+1,\qquad q_0<p+q-1.}
\tag{4.7}
$$
尤其当 $\sigma_j\sim c(j+2)^{-q}$、$c\ne0$ 时，第二个不等式由 $p>1$ 自动成立，故只需
$$
\boxed{p<q\le12/5,\qquad q<d(p-1)+1.}
\tag{4.8}
$$
这在 $d\ge3$ 时严格扩大了二阶路线的 $q<2p-1$。

如果不同横向变量有不同可验证的 $q_i$，无需降到最小 $q$：直接用第 2 节对 (4.4) 中实际出现的每个生成元计算权，再取最小值即可。不存在的混合项不应加入最小值中。

### 4.1 一个四项、真正独立次主尾的具体参数例子

取
$$
p=\frac32,\qquad q=\frac{11}5,\qquad
(c_0,c_1,c_2,c_3)=(0,1,2,3),
$$
$$
(\alpha_0,\alpha_1,\alpha_2,\alpha_3)=(1,-3,3,-1).
$$
前三个主矩 $k=0,1,2$ 消失。取任意 bounded 局部底参数，使
$$
s_{i,j}-t_{i,j}=c_i(j+2)^{-3/2}+\epsilon_{i,j},
\qquad \epsilon_{i,j}=O((j+2)^{-11/5}),
$$
且
$$
\sum_i\alpha_i\epsilon_{i,j}
\sim c(j+2)^{-11/5},\qquad c\ne0.
$$
这些 $\epsilon_i$ 可彼此独立。例如仅第 3 项带有 $(j+2)^{-11/5}$ 一阶余项，其余余项置零；各真实高次局部差仍全部保留。

此时
$$
d(p-1)+1=\frac52,\qquad p+q-1=\frac{27}{10},
$$
而 $q=11/5<5/2$，所以该四项组合单射稠密。二阶界只给 $q<2$，不能处理这个例子。

任意有限前缀产生的 $a_i(A)$ 仍应按 (4.2)—(4.3) 实际计算。若满足这些条件，R61 的共同循环锚及有限 $A$ 次幂分解把结论转成对应有限乘积和的非零循环性。

## 5. 超快横向变量允许全部有限阶主取消

Newton 条件是有限权的增长比较。下面给一个不同的实际低位条件，在它成立时不需要控制 Weierstrass 系数的低总次数。

设 $Y_1,\ldots,Y_s\in\mathcal A$，常数项全为零。假设对每个 $k$ 有零常数多项式
$$
Y_{\ell,k}=p_{\ell,k}(A_k)
$$
及固定 $C,c,\alpha>0$，使
$$
\boxed{\|Y_\ell-Y_{\ell,k}\|
\le C e^{-c2^{\alpha k}}\quad(\ell=1,\ldots,s),\qquad \alpha>p.}
\tag{5.1}
$$
有限个变量可取共同常数；它们在各个 $k$ 内彼此交换。

**定理 5.1。** 若 $F(w,y)$ 是解析芽，且一元芽 $F(w,0)$ 非恒零，则
$$
\boxed{F(L,Y)\text{ 单射且值域稠密。}}
\tag{5.2}
$$
无需假设 $F$ 的低总次数消失，也无需假设每个 $Y_\ell$ 是 $A$ 的标量解析函数。

**证明。** 若 $F(0)\ne0$，结论由单位性直接成立。否则令 $r\ge1$ 为 $F(w,0)$ 的有限零点阶。Weierstrass 分解给
$$
F=U P,\qquad
P(w,y)=w^r+\sum_{j=0}^{r-1}b_j(y)w^j,\qquad U(0)\ne0.
$$
令 $C(Y)$ 为上对角 $I$、末行 $-b_j(Y)$ 的伴随矩阵。其常数矩阵 $C(0)$ 满足 $C(0)^r=0$。

先确认解析评价的误差：对每个固定解析芽 $b_j$，
$$
\|b_j(Y)-b_j(Y_k)\|\le C_b e^{-c2^{\alpha k}}.
\tag{5.3}
$$
证明可取各 $Y_\ell$ 谱点零周围的固定小圆，半径小于解析芽的收敛多圆盘。实际预解式在这些圆上有界；(5.1) 和 Neumann 级数使所有充分大的 $Y_{\ell,k}$ 预解式也共同有界。Cauchy 公式于是给一致几何幂界，再对绝对收敛多变量级数逐项望远镜。这里不要求实际 $Y_\ell$ 与 $Y_{\ell,k}$ 互相交换；只用每组内的交换性。有限初始 $k$ 不影响随后极限。

记 $G_k$ 为基准 $L$ 的真实低位近似，构造矩阵头
$$
D_k=G_kI_r-C(Y_k).
\tag{5.4}
$$
它是 $A_k$ 的矩阵多项式，常数矩阵为 $-C(0)$。因此 $D_k^r$ 的每个条目都是 $A_k$ 的倍数：
$$
D_k^r=A_kR_k(A_k).
$$
标量 $A_kI_r$ 与矩阵多项式交换，故
$$
\boxed{D_k^{r2^k}=0.}
\tag{5.5}
$$
这个论证不要求各矩阵系数互相交换；常数矩阵幂零加上中心变量 $A_k$ 已足够。

令
$$
\zeta=\min(\alpha,4)>p,
$$
并取固定
$$
p/\zeta<\beta<1,\qquad
k=\lfloor\beta\log_2M\rfloor.
\tag{5.6}
$$
R61 的 $L$ 误差与 (5.3) 合并后，实际矩阵算子
$$
T=LI_r-C(Y)
$$
与
$$
T_k=D_k+\sum_{j\ge k}\theta_jE_j I_r
$$
之差至多
$$
C e^{-c'2^{\zeta k}}.
\tag{5.7}
$$
所有 $T,T_k,D_k$ 范数一致有界。

若 $P(L,Y)f=0$，取
$\mathbf f=(f,Lf,\ldots,L^{r-1}f)$，则 $T\mathbf f=0$。把
$$
T_k=H_{k,m}+C_mI_r,\qquad
H_{k,m}=D_k+\sum_{k\le j<m}\theta_jE_jI_r,
\quad C_m=\sum_{j\ge m}\theta_jE_j.
$$
头尾交换。由 (5.5)，
$$
H_{k,m}^{\,r2^k+m-k}=0.
\tag{5.8}
$$
因此 $e^{tH_{k,m}}$ 是 $t$ 的次数至多
$$
m-k+r2^k-1=M+O(M^\beta)
$$
的矩阵多项式。

在 $t=uM^p$ 的负 BW 区间上，
$$
e^{tH_{k,m}}\mathbf f-e^{-tC_m}\mathbf f
=e^{-tC_m}(e^{tT_k}-e^{tT})\mathbf f.
$$
由 (5.7) 和 Duhamel，误差范数至多
$$
\exp[-cM^{\beta\zeta}+O(M^p+\log M)]\|\mathbf f\|.
\tag{5.9}
$$
因为 $\beta\zeta>p>1$，它比尾范数下界 $e^{-CM}$ 小得多。

各坐标与 $1$ 配对所得多项式，边界为
$$
\|\mathbf f\|\exp[Mh_p(u)+O(1)]
$$
加可吸收误差。BW 的主指数为 $MJ_p<0$，头部额外次数只贡献
$O(M^\beta)=o(M)$。故所有核向量的均值为零；用 $A$ 不变性和 $1$ 对 $A^*$ 的循环性，得到 $P(L,Y)$ 单射。乘上可逆 $U(L,Y)$ 并用复对称性，完成证明。证毕。

## 6. 从实际独立次主尾核实超快假设

在
$$
L_i=\psi_i(A)+\sum_j[
\log(I+s_{i,j}N_j)-\log(I+t_{i,j}N_j)]
$$
中假设底参数共同有界，并且
$$
s_{i,j}-t_{i,j}=c_i\theta_j+\epsilon_{i,j},
$$
$$
|\epsilon_{i,j}|\le C e^{-c2^{\alpha j}},
\qquad\alpha>p.
\tag{6.1}
$$
相位可以任意变化，各 $\epsilon_i$ 无须相关。令 $R_i=L_i-c_iL$。

局部函数的线性项为 $\epsilon_{i,j}N_j$，高次系数满足
$|a_{i,j,n}|\le C(j+2)^{-p}S^{n-1}$。以全部 $j<k$ 的实际截断值，加上 $\psi_i(A_k)$ 定义 $R_{i,k}$。它是 $A_k$ 的零常数多项式。误差完整分为：

1. 解析前因子：$O(a_k)=O(e^{-c_1 2^{4k}})$；
2. 全部 $j<k$ 的局部截断累计：
   $$C\sum_{j<k}(j+2)^{-p}a_k/a_j
   \le C'\eta_{k-1}
   =O(e^{-c_2 2^{4k}});$$
3. $j\ge k$ 的一次尾：
   $$C\sum_{j\ge k}|\epsilon_{i,j}|
   \le C'e^{-c'2^{\alpha k}};$$
4. $j\ge k$ 的高次尾：
   $$C\sum_{j\ge k}(j+2)^{-p}\eta_j
   \le C'e^{-c_3 2^{4k}}.$$

从而
$$
\boxed{
\|R_i-R_{i,k}\|
\le C e^{-c'2^{\min(\alpha,4)k}}.}
\tag{6.2}
$$
正是定理 5.1 所需的近似。没有把累计低位误差漏掉，也没有把高次尾错误地按更小的 $\epsilon_{i,j}$ 控制。

特别是 $\epsilon_{i,j}=0$ 时，(6.2) 仍成立，指数为 $4$；这并不表示 $R_i$ 是 $A$ 或 $L$ 的标量解析函数。它表示高次局部项被真实的 $N_j^2=\eta_jN_{j+1}$ 压低，足以取得超快低位近似。

## 7. 全部有限临界组合的一个完整新类

假设第 6 节成立，且 $c_1,\ldots,c_s$ 两两不同。对实际解析系数 $a_i(A)$，令 $\alpha_i=a_i(0)$，假设不全为零。取快变量
$$
Y=(A,R_1,\ldots,R_s)
$$
并定义
$$
F(w,y)=\sum_i a_i(y_0)e^{-c_iw-y_i}.
$$
则
$$
F(w,0)=\sum_i\alpha_i e^{-c_iw}
$$
非恒零。证明：若其所有 Taylor 系数都为零，则前 $s$ 个矩给 Vandermonde 系统
$\sum_i\alpha_i c_i^n=0$，$0\le n<s$，两两不同的 $c_i$ 迫全部 $\alpha_i=0$，矛盾。

因此，无论其零点阶是多少，定理 5.1 都给
$$
\boxed{\sum_i a_i(A)e^{-L_i}\text{ 单射且值域稠密。}}
\tag{7.1}
$$
这覆盖所有有限阶主常数取消，不要求独立横向低次项消失。

对有限个 R16 乘积，保留共同循环锚、各非零尾归一化常数和实际有限前缀多项式。先从有限多项式中合法提出共同最小 $A$ 次幂后，各剩余系数 $a_i(0)$ 不全为零。因此在两两不同的 $c_i$ 和 (6.1) 下，**每个非平凡有限线性组合均非零且循环**。这里没有对一般范数闭包元素作有界除以 $A$。

若若干 $c_i$ 相同，使限制芽 $F(w,0)$ 恰好恒零，本条不自动给结论；需要先辨认新的实际主尺度或进一步的非退化关系。不能把定理 5.1 擅自写成对任意多变量非零芽的结论。

## 8. 范围与未解点

Newton 定理适用于逐个实际验证过的幂界和有效负 BW 主尾。超快定理适用于明确的低位近似率 $\alpha>p$。两者都允许多个独立次主方向，没有把它们强行写成一个 $L$ 的解析函数。

仍未解决的是一般只知 $\epsilon_{i,j}=o(j^{-p})$ 的高阶临界组合：实际一次合成尾可能没有任何已证的负 BW 结构，也可能不满足超快低位近似。对这些尾，不能自行假设固定相位、幂律主项或更高的 Newton 权。

本条仅扩大明确算子类及有限乘积和的循环性；不是一般 Hilbert 不变子空间问题的完成证明。

