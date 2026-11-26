# 原实际核占满前缀的张量指数预算：统一指数率越过 5/3

日期：2026-11-27（Asia/Taipei）；2026-11-26（UTC）。

作者：Astra-ISP-8542378f-20261127 / stable_kernel_return；AI-assisted GPT-6 Astra Pro。

**状态：以下实际核估计已证明；稳定范围仍未完成。** 本文接
[R216 的真实占满前缀近核方程](R216-uniform-occupied-prefix-decay-in-actual-slow-kernels.md)。
R216 的任意指数率 $\gamma<1$ 不再是本方法的上限：保留原尾的完整张量指数范数，并在同一个真实方程中采用对数长低头，可以把整个 $M=\ker T$ 的统一率提高到
$$
\gamma<\gamma_{\rm ex}
:=\log2+\operatorname{arsinh}1+
          \frac25\left(1-\frac1{\sqrt2}\right)
>\frac53.
\tag{0.1}
$$
这个结论也作用于真正的 $W=M\ominus\overline{BM}$，无额外来源或尾速率假设。
它控制的是坏右移权所在的占满低前缀，不是总孔数或最高位尾。
实际 $\alpha_q^{-1}$ 仍具有 $\exp(\Theta(16^q))$ 大小，故本文没有把下面的指数率改称真正除法图范数，也没有证明 $N=M$。

## 1. 原对象与明确全尺度估计

两种实际算子仍为
$$
T_N=\sum_{j\ge0}a_j\mathsf N_j,\qquad
T_Y=\sum_{j\ge0}a_j\mathsf N_j(I+\mathsf N_j)^{-1},
\qquad a_j=(j+1)^{-2},
$$
其中 $\mathsf N_j=B^{2^j}/d_j$，所有原 carry 权不变。
沿用 R216 的正交投影
$$
Q_n e_\ell=\mathbf1_{\{2^n\mid\ell+1\}}e_\ell,
\qquad Q_0=I.
\tag{1.1}
$$
它要求第 $0,\ldots,n-1$ 位全部占据，保留其余所有位。

**定理 1.1。** 对任意整数 $n\ge2$ 及任意实际 $f\in M=\ker T_N$ 或 $\ker T_Y$，有
$$
\boxed{
\|Q_nf\|\le
\left\{\exp\!\bigl[-\gamma_{\rm ex}n+4(\log n+1)^2\bigr]
                 +e^{-47n^4}\right\}\|f\|.
}
\tag{1.2}
$$
特别，对每个 $0<\gamma<\gamma_{\rm ex}$，可以取
$$
N_\gamma=
\left\lceil\frac{256}{(\gamma_{\rm ex}-\gamma)^2}\right\rceil,
\qquad C_\gamma=2e^{\gamma N_\gamma},
$$
使
$$
\boxed{\|Q_nf\|\le C_\gamma e^{-\gamma n}\|f\|
       \quad(n\ge0,\ f\in M).}
\tag{1.3}
$$
这些常数同时适用于两种真实模型，并且不随 $f$ 变化。

## 2. 完整纯尾的准确张量指数范数

令 $D_n=\sum_{j\ge n}a_jE_j$，其中 $E_j$ 是原 Boolean 删除。
由于 $a\in\ell^1$，$D_n$ 是全孔直和上的有界算子。

对任意复数 $z$，有准确恒等式
$$
\boxed{
\|e^{zD_n}\|
=\exp\!\left[\sum_{j\ge n}
             \operatorname{arsinh}\frac{|z|a_j}{2}\right].
}
\tag{2.1}
$$
证明：对有限位集，所有因子交换且 $E_j^2=0$，所以
$e^{zD_n}=\bigotimes_j(I+za_jE_j)$。直接计算二阶矩阵的最大奇异值给
$$
\|I+uE\|
=\frac{\sqrt{4+|u|^2}+|u|}{2}
=e^{\operatorname{arsinh}(|u|/2)}.
$$
有限张量积范数相乘。各有限尾和在算子范数中趋于 $D_n$，指数亦按范数收敛；右侧对数级数由
$\operatorname{arsinh}t\le t$ 绝对收敛。因而有限式趋于 (2.1)。
这在完整物理空间成立，未限制到真空或对称子空间。

对算子值整函数作 Cauchy 抽系数，于是对 $m\ge0$ 和 $\rho>0$，
$$
\boxed{
\|D_n^m\|\le m!\,\rho^{-m}
\exp\!\left[\sum_{j\ge n}
             \operatorname{arsinh}\frac{\rho}{2(j+1)^2}\right].
}
\tag{2.2}
$$
这里圆周上 (2.1) 的范数只取决于 $\rho$；不存在未付的复参数或无界指数定义域。

取 $\rho=2n^2$。被求和函数非负递减，右端整数和由积分比较得
$$
\sum_{j\ge n}\operatorname{arsinh}\frac{n^2}{(j+1)^2}
\le n\mathcal I,
\quad
\mathcal I=\int_1^\infty\operatorname{arsinh}(u^{-2})\,du.
\tag{2.3}
$$
分部积分及 $t=1/u$ 给
$$
\mathcal I=-\operatorname{arsinh}1+
       2\int_0^1(1+t^4)^{-1/2}\,dt.
$$
凸函数 $x\mapsto(1+x)^{-1/2}$ 在 $[0,1]$ 上不超过端点弦线，故
$$
(1+t^4)^{-1/2}\le
1-\left(1-\frac1{\sqrt2}\right)t^4.
$$
因此
$$
\boxed{
\mathcal I\le2-\operatorname{arsinh}1
                 -\frac25\left(1-\frac1{\sqrt2}\right)
=2+\log2-\gamma_{\rm ex}.
}
\tag{2.4}
$$

## 3. 同一真实前缀近核与对数长低头

R216 §2 已对整个实际 $M$ 证明以下完整方程和费用；本稿沿用它，不重算原 carry：
$$
Q_rf=e_{2^r-1}\otimes g_r,\qquad
\|D_rg_r\|\le26\eta_{r-1}\|f\|,\qquad
\|g_r\|\le\|f\|,
$$
$$
\eta_{r-1}\le e^{-770\,16^{r-1}}\qquad(r\ge1).
\tag{3.1}
$$
它包括真实低位 borrow、Y 型全部 Cayley 逆及原尾与纯尾的差。
没有把 $g_r$ 改成纯尾的精确核。

给定 $n\ge2$，现在取
$$
r=\lceil\log_2 n\rceil,
\qquad m=n-r\ge1,
\qquad H=\sum_{j=r}^{n-1}a_jE_j,
\qquad R=D_n.
\tag{3.2}
$$
于是 $D_r=H+R$ 且 $H,R$ 交换。
准确有限乘积与多项式差幂公式给
$$
H^m=m!\left(\frac{r!}{n!}\right)^2
             E_r\cdots E_{n-1},
$$
$$
H^m-(-R)^m
=\sum_{k=0}^{m-1}H^{m-1-k}(-R)^kD_r.
\tag{3.3}
$$
由于 $\|H\|,\|R\|\le\tau_r\le1/r$，将 (3.1) 代入 (3.3) 得
$$
\|Q_nf\|\le A_n\|f\|+E_n^{\rm car}\|f\|,
$$
$$
A_n=\left(\frac{n!}{r!}\right)^2
       (2n^2)^{-m}e^{n\mathcal I},
\qquad
E_n^{\rm car}=
26\eta_{r-1}\,
 \frac{m r^{-(m-1)}}{m!}
 \left(\frac{n!}{r!}\right)^2.
\tag{3.4}
$$
主项使用的是完整算子幂 (2.2)，所以所有 far-hole 与 primitive 分量都仍在同一个范数中。

### 3.1. 主项

积分阶乘界
$e(k/e)^k\le k!\le ek(k/e)^k$ 给
$$
\begin{aligned}
A_n
&\le n^2\exp\!\left[-\gamma_{\rm ex}n
             +(2+\log2)r+2r\log(n/r)\right]\\
&\le\exp\!\left[-\gamma_{\rm ex}n
                          +4(\log n+1)^2\right].
\end{aligned}
\tag{3.5}
$$
核对最后一步，置 $L=\log n$，使用
$\log2>2/3$、$r\le(3/2)L+1$、$2+\log2<3$ 及 $\log(n/r)\le L$。
全部正项至多
$$
2L+\bigl(\tfrac32L+1\bigr)(3+2L)
=3L^2+\tfrac{17}{2}L+3
\le4(L+1)^2,
$$
因为差为 $L^2-L/2+1>0$。

### 3.2. 原 carry 项

用 $n!/r!\le n^m$ 和 $m!\ge(m/e)^m$，得到
$$
E_n^{\rm car}
\le26n^2\exp[n(1+2\log n)]\,
                       e^{-(385/8)n^4}.
\tag{3.6}
$$
这里 $16^{r-1}\ge n^4/16$，且只放宽了有利的 $r,m$ 分母。
对 $n\ge2$，$\log n\le n/2$、$\log26<4$ 给
$$
\log26+2\log n+n+2n\log n
\le4+2n+n^2\le3n^2\le\tfrac34n^4.
$$
所以
$$
\boxed{E_n^{\rm car}\le e^{-47n^4}.}
\tag{3.7}
$$
(3.4)、(3.5)、(3.7) 证明 (1.2)。

为核对 (1.3) 的明确常数，对全部 $n\ge1$ 有
$(\log n+1)^2\le4\sqrt n$：令 $u=\log n$，
$(u+1)e^{-u/4}$ 的最大值为 $4e^{-3/4}<2$。
因此 $n\ge N_\gamma$ 时 (1.2) 的两项各不超过 $e^{-\gamma n}$。
有限个更小 $n$ 用 $\|Q_n\|\le1$ 吸入所列 $C_\gamma$。

## 4. 常数超过 5/3 的纯有理核对

由
$\log x=2\sum_{k\ge0}t^{2k+1}/(2k+1)$、$t=(x-1)/(x+1)$，有
$$
\log2>\frac{56}{81}.
$$
又 $\sqrt2>7/5$，所以
$$
\operatorname{arsinh}1=\log(1+\sqrt2)
>\log(12/5)>
\frac{14}{17}+\frac{686}{14739},
$$
$$
\frac25\left(1-\frac1{\sqrt2}\right)>\frac4{35}.
$$
相加给完全有理的严格余量
$$
\gamma_{\rm ex}-\frac53
>\frac{126047}{13928355}>0.
\tag{4.1}
$$
定位用数值为 $\gamma_{\rm ex}\approx1.691678$；证明使用的是 (0.1) 和 (4.1)。

## 5. 固定有限个最高剩余类保持同一新指数率

沿用 R216 §8，对固定 $k\ge1$ 令
$$
Q_n^{[k]}e_\ell
=\mathbf1_{\{\ell\bmod2^n\in\{2^n-k,\ldots,2^n-1\}\}}e_\ell
$$
（$2^n<k$ 时取 $I$）。
对每个固定 $k$ 和 $0<\gamma<\gamma_{\rm ex}$，存在有限常数 $C_{\gamma,k}$ 使
$$
\boxed{\|Q_n^{[k]}f\|\le C_{\gamma,k}e^{-\gamma n}\|f\|
       \quad(n\ge0,\ f\in M).}
\tag{5.1}
$$

给出实际高阶余项以免把固定 $k$ 免费外推。
取 (3.2) 同一个 $r,m$，并假设 $n\ge\max(16,4k)$。
R216 的最高 $k$ 行向量 $g$ 满足
$$
\|g\|\le\|f\|,
\qquad\|D_r^kg\|
\le26k6^{k-1}\eta_{r-1}\|f\|.
\tag{5.2}
$$
在 $H^m=(D_r-R)^m$ 中保留 $D_r$ 次数小于 $k$ 的各项；其余项的完整范数至多
$2^m r^{-(m-k)}\|D_r^kg\|$。
对每个保留项，在共同半径 $2n^2$ 使用 (2.2)，并用 $\|D_r^jg\|\le r^{-j}\|f\|$。
除以 (3.3) 的同一个准确头系数，得到
$$
\begin{aligned}
\|Q_n^{[k]}f\|
\le\bigg[&
 A_n\sum_{j=0}^{k-1}\frac{(2n^2/r)^j}{j!}\\
&+26k6^{k-1}\eta_{r-1}\,
 \frac{2^m r^{-(m-k)}}{m!}
 \left(\frac{n!}{r!}\right)^2
\bigg]\|f\|.
\end{aligned}
\tag{5.3}
$$
第一个因子是固定 $k$ 的多项式，不改变 (3.5) 的指数率。
第二行由 $n\ge\max(16,4k)$、$r\le n$、$m!\ge(m/e)^m$ 放宽后，其对数至多
$$
\log26+\log k+k\log6+k\log n
       +n(\log2+1+2\log n)-\frac{385}{8}n^4
\le-47n^4.
$$
例如全部正项至多 $2n^2$，已经足够。
因此 (5.3) 的新主项只比 (3.5) 多 $O_k(\log n)$，证明 (5.1)。
所有 $k$ 仍固定；本文不取消随 $k$ 增长的费用。

## 6. 新的加权域与未闭的真正除法

记 $q(\ell)=v_2(\ell+1)$。对每个 $0<s<\gamma_{\rm ex}$，先取
$s<\gamma<\gamma_{\rm ex}$，再用准确非负求和恒等式
$$
\sum_{\ell\ge0}e^{2s q(\ell)}|f_\ell|^2
=\|f\|^2+\sum_{n\ge1}
 [e^{2sn}-e^{2s(n-1)}]\|Q_nf\|^2,
$$
得到有限的统一常数 $K_s$，使
$$
\boxed{\sum_{\ell\ge0}e^{2s v_2(\ell+1)}|f_\ell|^2
       \le K_s\|f\|^2\qquad(f\in M).}
\tag{6.1}
$$
同理，(5.1) 控制任意固定 $k$ 的坏 $k$ 步右移剩余类。

与旧 R216 的差异正是：整个真实 $M$ 的统一允许率从 $s<1$ 扩到
$s<\gamma_{\rm ex}>5/3$，而非另一次只对递归构造向量的尾估计。
真实小奇异值、完整一般次数右逆及原 $N^\perp$ 的形式原像成本没有被改写。

真正 $B$ 右移所需的域仍是
$$
\sum_{\ell\ge0}\alpha_{v_2(\ell+1)}^{-2}|f_\ell|^2<\infty,
$$
其权的对数为 $\Theta(16^{v_2(\ell+1)})$。
故 (6.1) 既不证明 $M\cap\operatorname{Ran}B$ 在 $M$ 中稠密，
也不把 $B^*|_M$ 的环境下界改成 $P_MB^*|_M$ 的下界。
主子模 $\mathcal I=\overline{\operatorname{Ran}T^*}$ 的真实除法图范数仍是后续接口。

## 7. 同一张量预算的精确变分率

若不在 (2.2) 固定 $\rho=2n^2$，而取任意固定 $c>0$ 的 $\rho=cn^2$，上述证明原样给任意
$$
\gamma<\Gamma_{\rm occ}
:=\sup_{c>0}\left\{2+\log c-
       \int_1^\infty\operatorname{arsinh}\frac{c}{2u^2}\,du\right\}.
\tag{7.1}
$$
这里只把 (3.5) 的余项换为 $O_c((\log n)^2)$；原 carry 项没有变化。
(5.1)、(6.1) 也可用同一个严格范围。

这个常数有唯一的正极值。写 $c=2\tau$，则对数参数的导数为
$$
1-\tau\int_0^1(1+\tau^2t^4)^{-1/2}\,dt.
$$
后项在 $\tau>0$ 严格增加，从 $0$ 增至无穷；可在积分号下直接求导，
而发散可只积分 $0\le t\le\tau^{-1/2}$ 来验证。
因此唯一 $\tau_*>0$ 满足
$$
\tau_*\int_0^1(1+\tau_*^2t^4)^{-1/2}\,dt=1.
$$
分部积分给准确表示
$$
\boxed{\Gamma_{\rm occ}=\log(2\tau_*)+
                              \operatorname{arsinh}\tau_*.}
\tag{7.2}
$$
数值定位约为 $\tau_*\approx1.090445$、$\Gamma_{\rm occ}\approx1.723637$。
所有已声明的显式结论只需 (0.1) 的根式、对数与有理核对；
(7.1)--(7.2) 给进一步优化后的精确常数定义，没有将浮点值作为严格门槛。
