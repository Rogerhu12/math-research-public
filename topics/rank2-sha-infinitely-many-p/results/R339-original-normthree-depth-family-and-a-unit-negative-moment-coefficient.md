# R339：原范数三深度族与必为单位的移动负矩系数

日期：2026-11-13。**状态：以下原恒等式、多深度展开、指定单位系数和实际非零子域存在性均已证明。对每个普通好素数，在同一个固定原目标 S 的真实输入表示中，存在任意深处的非零中央导数子域；证明不假设固定负五次矩非零。尚未把原完整中央零传播到这些子域，因此没有据此宣称 Sha 的无穷素数结论。**

## 1. 固定目标与原测度

保持 R316、R333 的同一固定曲线
$$E:y^2=x^3+b,\qquad b=17,$$
原 reduced sigma、$\Theta=\sigma^2x$、$\delta^2=-3$、
$\gamma=(5+\delta)/2$，以及原普通测度 $\nu=\nu_{\sigma,17}$。
这里不改换曲线或原目标：
$$
S=-\frac1{84}\sigma(z)\sigma(2z)\sigma(\delta z)
               \sigma(2\delta z)\sigma(\gamma z)\sigma(\bar\gamma z).
\tag{1}
$$
固定普通 $p>7$、$p\ne17$，写 $p=6s+1$。所有测度均在同一个
$p$ 进系数环 $\mathcal O$ 上，周期 $\Omega=\Omega_p$ 为单位。
沿用原真实 core
$$
\nu|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu,\qquad
\lambda=\varepsilon^3/\bar\pi\in\mathcal O^\times,\qquad
\kappa=p/\bar\pi^2,\qquad t_p=\lambda\kappa\in p\mathcal O^\times.
\tag{2}
$$
所以任意 $n\ge0$ 都有
$$\nu|_{p^n\mathbf Z_p}=\lambda^n[\kappa^n]_*\nu.\tag{3}$$
记原正矩和单位负矩
$$
\mu_r=\int x^r\,d\nu(x),\qquad
I_{-R}=\int_{\mathbf Z_p^\times}x^{-R}\,d\nu(x).
$$
$\mu_r=0$ 除非 $r\equiv1\pmod6$，而
$$\boxed{\mu_1=\Omega,\qquad\mu_7=24b\Omega^7.}\tag{4}$$
第二式也可直接从原曲线核定：
$x=z^{-2}-(b/7)z^4+\cdots$、$\zeta'=-x$ 给
$\sigma=z+(b/210)z^7+\cdots$，再乘 $7!\Omega^7$。
因此这两个固定正矩对本节全部素数都是单位。

## 2. 在同一 S 内反复展开一个原范数三因子

原恒等式是
$$\sigma(\delta z)=\delta\sigma(z)\Theta(z).$$
反复使用它，任意 $m\ge0$ 都准确有
$$
\boxed{\sigma(2z)=\delta^m\sigma(2\delta^{-m}z)
                       \prod_{h=1}^m\Theta(2\delta^{-h}z).}
\tag{5}
$$
(5) 的完整乘积等于原因子 $\sigma(2z)$；没有给各个新因子添加中央条件。
$\delta^{-h}$ 在本节每个普通处都是单位。

用 $\zeta'= -x$ 得到
$$\Theta=\sigma'^2-\sigma\sigma''.$$
所以对任意单位尺度 $q$，其真实测度是
$$
\boxed{\nu_{\Theta(qz)}
=\frac1{\Omega^2}\{q(X+Y)\}_*
\left(\left[XY-\frac{X^2+Y^2}{2}\right]\nu(X)\nu(Y)\right).}
\tag{6}
$$
对称平均给出了平方项的 $1/2$；所有导数是对 sigma 的自身变量求导，
故 (6) 中没有遗漏一个 $q^2$。也可由生成函数逐项核对。

在 (1) 中只展开 $\sigma(2z)$。保留尺度一的 $\sigma(z)$ 为指定单位输入 $x_0$。
其余五个不带二次权的尺度为
$$\boldsymbol c=(\delta,2\delta,\gamma,\bar\gamma,2\delta^{-m}),$$
并另有 $m$ 对输入，成对尺度
$$q_h=2\delta^{-h}\qquad(1\le h\le m).$$
总计仍是原 S 的一个准确表示：共有 $6+2m$ 个同 sigma 输入，
其中 $5+2m$ 个是下面的深输入。设
$$N=5+2m,\qquad
Q_m(\boldsymbol X)=\Omega^{-2m}
\prod_{h=1}^m\left(X_{h,+}X_{h,-}
                   -\frac{X_{h,+}^2+X_{h,-}^2}{2}\right),\qquad
C_m=-\delta^m/84.$$
将五个不带权变量和各对变量统一编号为 $X_1,\ldots,X_N$，对应尺度记为 $a_i$。
则完整原测度为
$$
\boxed{\nu_S=C_m\left(x_0+\sum_{i=1}^N a_iX_i\right)_*
            \bigl(Q_m(\boldsymbol X)\,\nu(x_0)\nu^{\otimes N}(\boldsymbol X)\bigr).}
\tag{7}
$$
其中各对的两个 $a_i$ 同为 $q_h$。整个目标的次数和首项仍由 (1) 固定。

## 3. 独立深度是实际输入子域

取任意整数向量 $\boldsymbol n=(n_1,\ldots,n_N)$、$n_i\ge1$，
在 (7) 的原输入空间中限制
$$\mathcal D_{m,\boldsymbol n}
 =\{x_0\in\mathbf Z_p^\times,\ X_i\in p^{n_i}\mathbf Z_p\text{ 对全部 }i\}.$$
其真实输出必为单位。令 $J_{m,\boldsymbol n}(u)$ 是 (7) 在该域上
测试 $\langle y\rangle^{du}$ 所得的整条函数，其中 $d=p-1$。
所有相位、权和输入尺度都照 (7) 保留。

在 $\boldsymbol T\in(p\mathcal O)^N$ 上定义
$$
\mathcal F_m(\boldsymbol T)=C_md
\int_{x_0\in\mathbf Z_p^\times}\int_{\mathbf Z_p^N}
 Q_m(T_1X_1,\ldots,T_NX_N)
 \log_p\left\langle x_0+\sum_i a_iT_iX_i\right\rangle
 \,d\nu^{\otimes N}\,d\nu(x_0).
\tag{8}
$$
由 (3) 得到准确式
$$
\boxed{J'_{m,\boldsymbol n}(0)
       =\lambda^{\sum_i n_i}\,
          \mathcal F_m(\kappa^{n_1},\ldots,\kappa^{n_N}).}
\tag{9}
$$
各个 $T_i$ 在权多项式中也必须缩放；这正是 (8) 中的写法。
不能只缩放相加输出而漏掉二次权。

(8) 是收敛的多变量解析函数。具体地，展开
$\log\langle x_0+Z\rangle=\log\langle x_0\rangle+
\sum_{R\ge1}(-1)^{R-1}Z^R/(Rx_0^R)$。
前一个常数项被五个不带权深输入的零质量消掉。
第 $R$ 个齐次部分的总次数为 $R+2m$，其系数赋值下界为
$-v_p(R)$ 加一个与 $m,p$ 固定的常数；因此在 $(p\mathcal O)^N$ 上一致收敛。
同一估计允许逐项积分、取系数及原中央求导。
本篇不声称 (8) 的所有幂级数系数均整。

## 4. 完整多深度系数的准确因子

对一个多重指数 $\boldsymbol r$，假定每个 $r_i\ge1$、$r_i\equiv1\pmod6$，
并置
$$R=|\boldsymbol r|-2m.$$
在以下应用中 $R\ge5$。定义
$$B(r,t)=rt-\frac{r(r-1)+t(t-1)}2
       =\frac{r+t-(r-t)^2}{2}.$$
则 (8) 的准确系数为
$$
\boxed{\begin{aligned}
[\boldsymbol T^{\boldsymbol r}]\mathcal F_m
={}&C_md\,(-1)^{R-1}(R-1)!\,I_{-R}\,\Omega^{-2m}\\
&\quad\times\prod_{i=1}^N\frac{a_i^{r_i}\mu_{r_i}}{r_i!}
       \prod_{h=1}^m q_h^{-2}B(r_{h,+},r_{h,-}).
\end{aligned}}\tag{10}
$$

**证明。** 将 $Q_m=\Omega^{-2m}\sum_{\boldsymbol e}q_{\boldsymbol e}
\boldsymbol X^{\boldsymbol e}$ 展开，其中 $|\boldsymbol e|=2m$。
对该单项式，log 部分的指数只能为 $r_i-e_i\ge0$，总数是 $R$。
其系数准确为
$$C_md(-1)^{R-1}(R-1)!I_{-R}\Omega^{-2m}
 q_{\boldsymbol e}\prod_i\frac{a_i^{r_i-e_i}\mu_{r_i}}{(r_i-e_i)!}.$$
对每个互不相交的变量对分别求和。由于两尺度同为 $q_h$，
从共同因子提出 $a_i^{r_i}/r_i!$ 后，三个单项式的和就是
$q_h^{-2}B(r_{h,+},r_{h,-})$。若某个 $e_i>r_i$，
相应下降阶乘为零，公式仍准确。相乘即 (10)。$\square$

尤其
$$\boxed{B(1,1)=1,\qquad B(7,1)=B(1,7)=-14,\qquad B(7,7)=7.}\tag{11}$$
这些是完整平方项与交叉项聚合后的系数，不是只留下交叉单项式。

## 5. 每个普通好 p 的一个明确单位系数

现在取
$$\boxed{K=s-1,\qquad m=\lceil K/2\rceil.}\tag{12}$$
在 $2m$ 个成对深变量中任选 $K$ 个令 $r_i=7$，其余成对变量令 $r_i=1$；
五个不带权深变量都令 $r_i=1$。于是
$$|\boldsymbol r|=5+2m+6K,\qquad R=5+6K=p-2.$$
由 Fermat 同余及原 core，
$$
\boxed{I_{-(p-2)}\equiv\int_{\mathbf Z_p^\times}x\,d\nu(x)
 =(1-t_p)\Omega\not\equiv0\pmod p.}\tag{13}
$$
这里负矩指数可以随 $p$ 改变；(13) 只用于证明同一个 S 的指定系数，
未把它当作某个固定负权在无穷 p 上的单位定理。

将这些实际数据代入 (10)：$C_m,d,a_i,q_h,\Omega$ 全为单位；
正矩仅为 (4) 的两个单位；$r_i!$ 仅为 $1$ 或 $7!$，
而 $(R-1)!=(p-3)!$ 也是单位；全部 (11) 都是单位。
所以
$$\boxed{[\boldsymbol T^{\boldsymbol r}]\mathcal F_m\in\mathcal O^\times.}\tag{14}$$
这是一条对全部 $p>7,p\ne17,p\equiv1\pmod6$ 的证明，
不是有限素数扫描，也不要求猜测 sigma 的所有 Taylor 系数非零。
展开次数 $m$ 和输入数随 $p$ 增长，但 (5)、(7) 的原目标始终严格等于固定的 (1)。

## 6. 任意深处都有真实非零域

**定理。** 对第5节的每个普通好 $p$ 和指定 $m$，任意给定 $n_0\ge1$，
都存在一组整数 $n_i\ge n_0$，使
$$\boxed{J'_{m,\boldsymbol n}(0)\ne0.}\tag{15}$$

**证明。** 若所有这些网格点的值均为零，由 (9) 及 $\lambda\ne0$，
$\mathcal F_m$ 在整个笛卡尔网格
$\{\kappa^n:n\ge n_0\}^N$ 上为零。
先固定后 $N-1$ 个网格坐标。第一个坐标上的零趋于盘内点零，
一变量解析恒等定理使该坐标上的函数恒为零。
再依次对第二至第 $N$ 个坐标使用同一论证，
得到 $\mathcal F_m$ 在整个小多圆盘恒为零，与 (14) 矛盾。$\square$

这没有给出一个事先固定的公共深度，亦没有声称所有深度选择都非零。
定理给出的域均是 (7) 中明确的原输入域，输出单位条件自动满足。
各域自己的中央质量为零：至少五个零质量深变量不在 $Q_m$ 中。
所以 (15) 确实是这些实际域的第一中央导数，而非未扣除的尺度质量项。

## 7. 与主问题之间还须支付的接口

(14)、(15) 支付了一个新的真实非零输入，且避开固定 $I_{-5}$ 或 $I_{-6}$ 的单位猜测。
要用它否定原完整中央失败，仍必须从 $J'_S(0)=0$ 推出同一 (7) 中
足够多 $\mathcal D_{m,\boldsymbol n}$ 的中央导数为零，或证明其完整补域不能相消。

原 S 是所有输入域的总和。单独非零的 (15) 不排除补域贡献的抵消。
R337 的实际 Riemann/Hadamard 条件域可以提供合法的零传播，
但没有在本篇被假定覆盖上述独立深度网格。
尤其 (5) 引入的各个 Theta 对不是可自由加入的中央零条件。

本篇新增的具体问题是：能否通过原范数三与四 sigma 的完整 joint 域恒等式，
将原中央零运输到上述一整族多深度域；任何运输都须保留原权、全部相加输出和交叠。

## 精确证书与依赖

- `scripts/check-jzero-normthree-multidepth-unit-coefficient.py/.json` 核对固定原 jet、成对平方权的完整下降阶乘聚合、三个非零系数和全部剩余类的计数。
- R316：同一原 sigma 的测度、普通周期与完整 core。
- R333：固定六 sigma 原 S、原单位输出及负矩规范。
- R337：仅用于指出后续域运输接口；本篇证明不假设其域已覆盖 (15)。
