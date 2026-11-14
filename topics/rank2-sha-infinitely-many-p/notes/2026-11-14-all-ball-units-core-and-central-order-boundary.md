# 2026-11-14：逐球单位、完整单轴 core 与中央零阶的准确边界

**状态：以下抽象反模型已证明。** 本文记录一条应排除的推理：
即使同时知道完整单轴 core、每个非原点加法小球的质量为单位、
原点质量为零、六阶首矩为单位和 Mellin 函数不恒零，
也不能仅由这些性质推出 principal 中央导数非零。

这不是原 $S$ 的反例，不否定 R376，也不对原 theta 的零点阶作判断。
原目标仍须利用实际联合测度、同源域关系或原 canonical 矩阵的额外结构。
下述构造说明不能把上述已证性质单独当成缺失的跨素数非零定理。

## 1. 同时保持的全部性质

设 $p>7$ 为普通素数，故 $p\equiv1\pmod6$。
取任意有限扩张的整数环 $\mathcal O$，
任意 $\lambda\in\mathcal O^\times$，
以及 $\kappa\in p\mathbf Z_p^\times$。
对任意整数 $r\ge2$，存在 $\mathcal O$ 值有界测度 $\nu$，满足：

1. $\nu$ 在 $\mu_6$ 缩放下不变，且
   $\nu|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu$。
2. 对全部 $n\ge1$，
   $\nu(p^n\mathbf Z_p)=0$；每个非零类
   $c\bmod p^n$ 的 $\nu(c+p^n\mathbf Z_p)$ 都是单位。
3. 零至五阶矩均为零，六阶矩是单位。
4. 真实 principal Mellin 函数
   $$
   J_\nu(u)=\int_{\mathbf Z_p^\times}
       \langle x\rangle^{(p-1)u}\,d\nu(x)
   $$
   不恒为零，其在 $u=0$ 的零阶准确为 $r$。

因而可以令 $J_\nu'(0)=0$，也可令其任意有限多条初始导数消失；
若另需奇零阶，可直接取任意奇数 $r\ge3$。

## 2. 每个球都为单位的对称有界测度

用平衡数字集
$$
\mathcal D=\{-(p-1)/2,\ldots,(p-1)/2\}
$$
表示 $\mathbf Z_p$ 的唯一展开 $t=\sum_{j\ge0}d_jp^j$。
令
$$
a_0=2-p,\qquad a_d=1\quad(d\ne0).
$$
它们全是 $p$ 进单位，且
$$\sum_{d\in\mathcal D}a_d=1.$$
给定前 $n$ 个数字的圆柱，其质量定义为
$$\eta(d_0,\ldots,d_{n-1})=\prod_{j=0}^{n-1}a_{d_j}.$$
上一层质量等于全部子层质量之和，且所有质量范数均为一。
因此它定义一个有界 $\mathbf Z_p$ 值测度 $\eta$，
总质量为一，每个加法小球的质量是单位。

平衡数字下，取负准确把每个 $d_j$ 换成 $-d_j$；
$a_d=a_{-d}$ 给
$$[-1]_*\eta=\eta,\qquad \int t\,d\eta(t)=0.$$
将其沿 $t\mapsto\exp(pt)$ 推到 $1+p\mathbf Z_p$。
该映射把模 $p^{n-1}$ 小球准确双射到模 $p^n$ 小球。
以下保留 $\eta$ 的 $t$ 坐标，以免混淆加法与乘法。

## 3. 单位部分：保持全小球单位并指定 Mellin 零阶

令 $h=(p-1)/6\ge2$，
取 $\mu_{p-1}/\mu_6$ 的代表 $\tau_1,\ldots,\tau_h$。
取
$$
w_i=1\quad(i<h),\qquad w_h=-(h-1).
$$
它们全是单位，且 $\sum_iw_i=0$。
定义单位群上的有界测度
$$
\nu_0^\times
=\sum_{i=1}^{h}w_i\sum_{\zeta\in\mu_6}
 [\,t\mapsto\zeta\tau_i\exp(pt)\,]_*\eta.
\tag{1}
$$
每个单位加法球落在唯一 Teichmüller 类，
故其质量是某个 $w_i$ 乘一个 $\eta$ 小球质量，仍为单位。
它是 $\mu_6$ 不变的，总质量为零。

所有 Teichmüller 类共享同一个 $\eta$，所以
$$
J_{\nu_0^\times}(u)
=6\left(\sum_iw_i\right)
  \int\exp(p(p-1)ut)\,d\eta(t)=0.
\tag{2}
$$
现在在一个固定 $\mu_6$ 轨道中加入有限点测度
$$
\Delta_r
=p\sum_{\zeta\in\mu_6}\sum_{j=0}^{r}
 (-1)^{r-j}\binom rj\,\delta_{\zeta\tau_1\exp(pj)} ,
\qquad
\nu^\times=\nu_0^\times+\Delta_r .
\tag{3}
$$
每个加法球的新增质量属于 $p\mathcal O$。
因此全部单位球质量仍是单位；$\mu_6$ 不变性和总质量零也保持。
其 Mellin 函数准确是
$$
\boxed{
J_{\nu^\times}(u)
=6p\bigl(\exp(p(p-1)u)-1\bigr)^r .
}
\tag{4}
$$
它不恒零，且首项为
$6p\{p(p-1)\}^r u^r$，所以零阶恰为 $r$。
这是特征零的精确式，不是仅有有限精度的零。

再核六阶矩。
$\tau_i^6$ 遍历 $\mu_h$，所以
$$
\sum_iw_i\tau_i^6=-h\tau_h^6 .
$$
因此 (1) 的六阶矩为
$$
-6h\tau_h^6\int\exp(6pt)\,d\eta(t)\in\mathcal O^\times,
\tag{5}
$$
其中积分模 $p$ 为一，$6h=p-1$ 是单位。
(3) 的六阶矩属于 $p\mathcal O$，不会消去 (5) 的单位性。
一至五阶矩因 $\mu_6$ 不变性为零，零阶矩已经为零。

## 4. 沿完整 core 延拓，含收敛与原点球

定义
$$
\boxed{
\nu=\sum_{n\ge0}\lambda^n[\kappa^n]_*\nu^\times .
}
\tag{6}
$$
这不是把一串单位质量当作收敛几何级数。
关键是每项的总质量准确为零。

对模 $p^N$ 局部常数测试 $f$，当 $n\ge N$ 时，
$f$ 在 $\kappa^n\mathbf Z_p^\times$ 上等于 $f(0)$，
所以相应积分准确为零；(6) 对这种测试只是有限和。
对一般连续 $f$，其第 $n$ 项积分范数至多
$$
\|\nu^\times\|\,
\sup_{x\in p^n\mathbf Z_p}|f(x)-f(0)|\longrightarrow0.
$$
非阿基米德完备性于是给收敛，且全测度范数有统一界。
这严格构造了有界测度 (6)。

各项分别支撑在精确赋值 $n$ 的环带。
因此直接移指标得到
$$\nu|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu.$$
对原点球 $p^N\mathbf Z_p$，
$n<N$ 的项没有支撑，$n\ge N$ 的项总质量均为零，
故其质量为零。

若 $c\ne0\bmod p^N$，令 $v_p(c)=k<N$，
则只有第 $k$ 环带贡献：
$$
\nu(c+p^N\mathbf Z_p)
=\lambda^k\nu^\times
   \bigl(\kappa^{-k}c+p^{N-k}\mathbf Z_p\bigr)\in\mathcal O^\times.
\tag{7}
$$
所有非原点球单位的量词因此包括非单位中心和任意深度。

对正整数 $m$，矩级数中的 $\kappa^{nm}$ 收敛；
六阶矩准确为
$$
\int x^6d\nu
=\frac{\int x^6d\nu^\times}{1-\lambda\kappa^6}
\in\mathcal O^\times .
\tag{8}
$$
零至五阶矩仍为零。
单位 Mellin 函数就是 (4)，所以全部断言成立。

## 5. 与原研究的关系

还可乘一个明确单位，使六阶矩准确等于任给的单位，
例如原周期规范下的 $6!\Omega_p^6$。
全部性质及中央零阶不变。

因此下列信息的合取仍不够：
原质量零、首六阶矩单位、完整单轴 core、全部非原点球单位、
Mellin 不恒零，甚至奇的指定中央零阶。
这个反模型没有原固定代数 theta 来源、真正多轴联合 core，
也没有 R338/R377 的实际 canonical 像和全部整连接。
后继应在这些真实结构中取得新的约束；
不能把 (4) 的可能性误排除后宣称 R376 已推出主目标。

依赖仅为有界 $p$ 进测度的圆柱构造、
$\mathbf Z_p^\times=\mu_{p-1}\times(1+p\mathbf Z_p)$
和原主目标的定义。没有素数扫描或外部未证假设。
