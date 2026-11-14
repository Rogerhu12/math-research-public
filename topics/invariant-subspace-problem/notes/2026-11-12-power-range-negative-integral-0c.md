# 幂指数扩至 $12/5$：八点严格区间证书与连续参数覆盖

日期：2026-11-12（UTC）。子任务：critical_kernel。

**状态：已证明的标量常数扩充，可并入 R61。** 在新区间 $[a,b]=[1/10,30]$ 上，对全部 $2\le p\le12/5$ 严格证明
$$
\boxed{J_p(a,b)<-\frac1{2000}.}
\tag{0.1}
$$
结合[复正则变差推广稿](2026-11-12-complex-regular-variation-critical-products-0c-agent.md)中已经证明的 $1<p\le2$，实际复参数乘积定理及两个 R16 乘积全线性组合循环性都可扩至
$$
\boxed{1<p\le12/5.}
\tag{0.2}
$$
本条保留独立证书，不把离散采样当成整个参数区间的证明。八个有理站点之间的连续覆盖用精确有理算术和解析 Lipschitz 界完成。

脚本：[2026-11-12-power-range-negative-integral-0c.py](2026-11-12-power-range-negative-integral-0c.py)。

## 1. 常数定义与两种区间的分工

对一般 $0<a<b$ 定义
$$
g_{a,b}=\log\frac{\sqrt b+\sqrt a}{\sqrt b-\sqrt a},
\qquad
d\nu_{a,b}(u)=
\frac{\sqrt{ab}}{\pi u\sqrt{(u-a)(b-u)}}\,du.
$$
它是区间外点 $0$ 的谐测，质量为 $1$；R60 §1 已证明对次数至多 $n$ 的复多项式 $P$，
$$
\log|P(0)|
\le n g_{a,b}+\int_a^b\log|P(u)|\,d\nu_{a,b}(u).
\tag{1.1}
$$
置
$$
h_p(u)=\frac12\int_1^\infty
\log\left(1-\frac{u}{x^p}+\frac{u^2}{2x^{2p}}\right)\,dx,
\qquad
J_p(a,b)=g_{a,b}+\int_a^b h_p(u)\,d\nu_{a,b}(u).
\tag{1.2}
$$

两个指数部分使用不同的固定区间：

- $1<p\le2$：使用已经认证的 $[a,b]=[1,20]$。先前推广稿 §4 的单符号变化比较给 $J_p(1,20)\le J_2(1,20)<-13/100$。
- $2\le p\le12/5$：使用本条的 $[a,b]=[1/10,30]$，并证明 (0.1)。

不要求同一个积分区间同时控制两部分；给定固定 $p$ 后，选其对应区间即可。重叠端点 $p=2$ 两者都可用。

## 2. 一致线性插值误差与精确权重

仍写
$$
P(q)=1-q+q^2/2=\frac{1+(q-1)^2}{2}.
$$
关于 $u$ 两次求导可在积分号下进行，且
$$
h_p''(u)=
\int_1^\infty
\frac{1-(u/x^p-1)^2}
{x^{2p}(1+(u/x^p-1)^2)^2}\,dx.
$$
故
$$
\boxed{|h_p''(u)|\le\frac1{2p-1}.}
\tag{2.1}
$$
在 $[a,b]=[1/10,30]$ 上使用精确网格
$$
u_i=\frac1{10}+\frac i{10},\qquad i=0,\ldots,299,
\qquad\Delta=\frac1{10}.
$$
令 $\ell_p$ 为 $h_p(u_i)$ 的分段线性插值。单位区间证明经缩放即给
$$
h_p(u)\le\ell_p(u)+\frac{\Delta^2}{8(2p-1)}.
$$
对概率测度积分，
$$
\boxed{
J_p(a,b)\le
U_p:=g_{a,b}+\int_a^b\ell_p\,d\nu_{a,b}
+\frac1{800(2p-1)}.
}
\tag{2.2}
$$

精确质量和第一矩原函数为
$$
F(u)=\frac2\pi\arctan
\sqrt{\frac{b(u-a)}{a(b-u)}},
$$
$$
M(u)=\frac{2\sqrt{ab}}{\pi}
\arcsin\sqrt{\frac{u-a}{b-a}},
\tag{2.3}
$$
端点取 $F(a)=M(a)=0$、$F(b)=1$、$M(b)=\sqrt{ab}$。

记 $\mu_i=F(u_{i+1})-F(u_i)$、$m_i=M(u_{i+1})-M(u_i)$。该段的左、右帽权重分别为
$$
L_i=\frac{u_{i+1}\mu_i-m_i}{\Delta},
\qquad
R_i=\frac{m_i-u_i\mu_i}{\Delta},
\tag{2.4}
$$
均严格正。合并相邻段得到 300 个正权重 $\omega_i$，其和为 $1$，并有
$$
\int_a^b\ell_p\,d\nu_{a,b}
=\sum_{i=0}^{299}\omega_i h_p(u_i).
\tag{2.5}
$$
因此每个 $U_p$ 是一个有限明确表达式加上已经解析控制的误差，不进行未经误差控制的数值积分。

## 3. 任意有理 $p>1$ 的端点闭式与分支

令
$$
z=\frac{1+\mathrm i}{2}u,\qquad
\beta=1-\frac1p>0.
$$
原积分等于 $\operatorname{Re}\int_1^\infty\operatorname{Log}(1-z/x^p)\,dx$。$z$ 位于严格上半平面，所以主值对数沿积分路径不遇割线。分部积分给
$$
\int_1^\infty\operatorname{Log}(1-z/x^p)\,dx
=-\operatorname{Log}(1-z)
-pz\int_1^\infty\frac{x^{-p}}{1-zx^{-p}}\,dx.
$$
令 $v=x^{-p}$，最后一个积分等于
$$
\frac1p\int_0^1\frac{v^{-1/p}}{1-zv}\,dv
=\frac1{p-1}\,
{}_2F_1(1,\beta;\beta+1;z).
$$
这里使用 Euler 积分恒等式
$$
{}_2F_1(1,\beta;\beta+1;z)
=\beta\int_0^1\frac{v^{\beta-1}}{1-zv}\,dv,
$$
先在 $|z|<1$ 由几何级数逐项积分成立，再在 $\mathbb C\setminus[1,\infty)$ 上解析延拓。我们的 $z$ 始终在严格上半平面。故
$$
\boxed{
h_p(u)=\operatorname{Re}\left[
-\operatorname{Log}(1-z)
-\frac{pz}{p-1}\,
{}_2F_1(1,\beta;\beta+1;z)
\right].
}
\tag{3.1}
$$
$p=2$ 时，该式化为原证书的平方根与反双曲正切表达式。

脚本使用 Acb 的标准复超几何函数。参数的精确恒等式是
$$
\beta-(\beta+1)=-1,\qquad
1+\beta-(\beta+1)=0.
$$
因此脚本的 bc=True、abc=True 标志有数学依据，不是用数值近似猜测参数差为整数。相关接口与这些标志的含义见 python-flint 官方 [acb.hypgeom_2f1](https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.hypgeom_2f1)，本轮已核读。

## 4. 八个经过严格球区间验证的站点

取以下有理 $p_i$。脚本对 (2.2) 的整个 Arb 球上端，逐项验证
$$
\boxed{U_{p_i}<-K_i/10^6.}
\tag{4.1}
$$

| $i$ | $p_i$ | $K_i$ | 本轮得到的 $U_{p_i}$ 中点近似，仅便于阅读 |
|---:|---:|---:|---:|
| 1 | $12/5$ | 2289 | $-0.00228938162441136689916891$ |
| 2 | $239/100$ | 3808 | $-0.00380862088680533636502604$ |
| 3 | $237/100$ | 6939 | $-0.00693950429946908877868665$ |
| 4 | $117/50$ | 11879 | $-0.0118796674694284957206454$ |
| 5 | $229/100$ | 20826 | $-0.0208261654556303529374158$ |
| 6 | $111/50$ | 35077 | $-0.0350777699895565672766529$ |
| 7 | $53/25$ | 59790 | $-0.0597900381828788151841991$ |
| 8 | $2$ | 98662 | $-0.0986620726886793477390831$ |

最后一列不承担证明功能；严格断言使用 (4.1) 的精确有理界，并比较球上端而不是中点。工作精度为 160 位；输入全部是整数或 fmpq 精确有理数，无 Python float 输入。

## 5. 用有理覆盖控制全部连续指数

这里补上离散站点与整个区间之间必不可少的一步。

同先前推广稿，对任意 $p>1$，
$$
\left|\frac{\partial h_p(u)}{\partial p}\right|
\le\frac{u}{2(p-1)^2}.
$$
当前谐测第一矩为 $\int u\,d\nu_{a,b}=\sqrt{ab}=\sqrt3$，所以
$$
\left|\frac{dJ_p(a,b)}{dp}\right|
\le\frac{\sqrt3}{2(p-1)^2}.
\tag{5.1}
$$
改用参数
$$
v=\frac1{p-1},\qquad
\mathcal J(v)=J_{1+1/v}(a,b).
$$
链式法则使分母完全消掉：
$$
\boxed{
|\mathcal J'(v)|\le\frac{\sqrt3}{2}<\frac78
\qquad(v>0).
}
\tag{5.2}
$$

置目标余量 $\mu=1/2000=500/10^6$。对第 $i$ 个站点定义
$$
v_i=\frac1{p_i-1},\qquad
r_i=\frac{K_i-500}{875000}
=\frac87\left(\frac{K_i}{10^6}-\mu\right)>0.
\tag{5.3}
$$
由 (4.1)—(5.2)，若 $|v-v_i|\le r_i$，则
$$
\mathcal J(v)
<
-\frac{K_i}{10^6}+\frac78r_i
=-\mu.
\tag{5.4}
$$

下述完全有理事实由脚本的 Fraction 算术逐项核实：
$$
[v_1-r_1,v_1+r_1]\cup\cdots\cup[v_8-r_8,v_8+r_8]
\supseteq[5/7,1].
\tag{5.5}
$$
按表中顺序，中心严格递增；第一段覆盖 $5/7$，最后一段覆盖 $1$，七对相邻区间严格重叠。为保留小型、可查证的覆盖数据，七个重叠长度分别为
$$
\frac{83483}{121625000},\quad
\frac{10612121}{16662625000},\quad
\frac{16150711}{4015812500},\quad
\frac{11055263}{1512525000},\quad
\frac{125781707}{6885375000},\quad
\frac{1819637}{53375000},\quad
\frac{31851}{437500},
$$
全部严格为正。

由于 $p\in[2,12/5]$ 恰对应 $v\in[5/7,1]$，(5.4)—(5.5) 证明整个连续参数区间上的 (0.1)。没有假设 $J_p$ 关于 $p$ 单调。

## 6. 实际复参数定理如何随之扩充

先前推广稿的全部算子推导保留。只需作以下明确替换：

1. 对 $1<p\le2$，仍取 $[a,b]=[1,20]$，负常数为 $-13/100$。
2. 对 $2\le p\le12/5$，取 $[a,b]=[1/10,30]$，负常数用 $-1/2000$。
3. 尾范数的一致误差中，将原来的 $u\le20$ 替换为 $u\le b$。例如
   $$
   |\log F_m(u)-Mh_p(u)|
   \le\frac b2+\frac b2 e_m\left(1+\frac M{p-1}\right)=o(M).
   $$
   固定 $p>1$ 已足够；不要求在 $p\downarrow1$ 时一致。
4. 复时间变为 $\tau=M^p u/c$，故 $|\tau|\le b|c|^{-1}M^p$。仍选 $k=\lfloor(3/4)\log_2M\rfloor$。由于现在的最大 $p=12/5<3$，
   $$
   \eta_{k-1}e^{C|\tau|}
   \le\exp(-c_0M^3+O(M^{12/5}))\longrightarrow0
   $$
   仍远小于尾范数的 $e^{-CM}$ 下界。
5. 头部多项式次数仍为 $M+O(M^{3/4})$，而对应的 $g_{a,b}$ 是固定有限常数。加权多项式估计最后给出
   $$
   \log|\langle f,1\rangle|
   \le O(1)+o(M)+g_{a,b}M^{3/4}
      -\frac1{2000}M\longrightarrow-\infty
   $$
   （$1<p\le2$ 部分有更强负常数）。

所以对任意有界复底参数 $s_j,t_j$，若
$$
s_j-t_j\sim c(j+2)^{-p},\qquad c\ne0,\quad1<p\le12/5,
$$
并允许一个在 $0$ 邻域解析、$R(0)=1$ 的通常全纯演算前因子，实际 $I-Q$ 仍单射稠密。两 R16 乘积的常数归一化、有限多项式首阶分解及唯一临界系数的归约不依赖原先的上端 $41/20$，因此对应全线性组合循环性同样扩充。

## 7. 复现与边界

从仓库根目录运行：

    python -u topics/invariant-subspace-problem/notes/2026-11-12-power-range-negative-integral-0c.py

脚本打印八个严格上界的球区间，并断言全部八个有理比较、七个相邻覆盖及两个端点覆盖。所用环境为 python-flint 0.9.0、FLINT 3.6.0、160 位精度。球包含及比较的语义见官方 [General concepts](https://python-flint.readthedocs.io/en/latest/general.html#inexact-numbers-and-numerical-evaluation)。

本条不认证 $p>12/5$，也不从探索性数值推断该范围之外常数的符号。新的真正尾类型仍需处理，例如没有固定复相位主项、没有渐近主系数或不能化为两个乘积差的有限多项组合。

