# R190：准确半径样条的 C² 区间层与浮点网格敏感界

本组消费 [R190](../results/R190-positive-radius-design-and-exact-fixing-of-the-metric.md) 的完整半径函数。源码是 [fd2d_R190_radius_spline_interval.cjs](../scripts/fd2d_R190_radius_spline_interval.cjs)，SHA256 c7fdbc32b297dd196b6277f673c8fe879fe5f99da33c5c7d955fe9d4422c3c27。它不求新的 BVP，也不把一个有限求积的指标改称连续证书。

## 1. 准确定义与当前尚未消费的基础输入

固定 $c=13/128$，令 $S$ 是 R181 的 B32 准确总长，$J\ge1$，

$$
h=\frac{S-c}{J+3},\qquad
q_j(s)=\frac{s-c}{h}-(j+2),\qquad
b_j(s)=B(q_j(s)),\qquad
d(s)=\sum_{j=0}^{J-1}\rho_jb_j(s).
$$

$B$ 是 R190 的中心三次 cardinal spline，$\rho_j$ 是保存的 binary64 系数作为准确 dyadic 有理数。准确半径是 $a=a_B+d$，基础高度 $Z_B$ 不随 $\rho$ 改变。

这里固定的是准确 $S$，不是 evaluator 的浮点 end。使用准确 $h$ 后，所有新增样条在准确 $c,S$ 的零至二阶 jet 都为零。若把浮点中心固化为另一组几何常数，这个端点结论不能自动沿用。

准确 B32 来源为：

- candidate：notes/2026-11-12-fd2d-r136-shorter-phase-design-01-B_standard_cut-cyl13over128-candidate.json，SHA256 9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d；
- 已保存的恢复入口：scripts/fd2d_gc_r181_b_arb_profile_recovery.py；
- 准确 $S$ 由该 candidate 的真实 phase 积分、各段长度和末 coast-to 半径匹配定义。

恢复入口截至本组写入尚未在恢复后的实际 OS 环境执行。会话中只有旧准确包的部分身份和 $S-S_{\rm float}$ 的显示值，没有完整严格有理端点。因此本组不据该显示值补造准确长度区间，不借旧 7c3f/δ7 包，也不声称已支付完整 $a_B,a_{B,s},a_{B,ss}$。

输入 schema 为 fd2d-R190-accurate-radius-spline-input-v1。它显式要求准确 base 定义、准确 cut 定义及其有理区间、全部实际 $\rho$ 与参数身份。$S$ 的区间是 caller 已证明的输入条件；该样条层不替 caller 重新证明它。

## 2. 有理 Bernstein 点盒消费者

在四个真实片 $[-2,-1],[-1,0],[0,1],[1,2]$ 上，$B$ 分别为

$$
\frac43+2t+t^2+\frac{t^3}{6},\quad
\frac23-t^2-\frac{t^3}{2},\quad
\frac23-t^2+\frac{t^3}{2},\quad
\frac43-2t+t^2-\frac{t^3}{6}.
$$

外部恒零。其前两阶导数在所有接点共同，源码逐片准确微分，只导出 $k=0,1,2$。

对任一准确有理子区间 $[l,r]$，先代入 $t=l+(r-l)x$。若得到 $p(x)=\sum_{k=0}^n a_kx^k$，则其 Bernstein 系数为

$$
\beta_j=\sum_{k=0}^j\frac{\binom jk}{\binom nk}a_k,\qquad 0\le j\le n.
$$

证明是将 $x^k$ 写成次数 $n$ 的 Bernstein 基的上述非负组合；展开二项式即可核定。Bernstein 基在 $[0,1]$ 非负且和为 1，所以

$$
\min_j\beta_j\le p(x)\le\max_j\beta_j.
$$

源码先在所有真实接点处分片，然后取各片这些有理 hull；因此完整跨接点查询同样有效。区间中的每个乘法、除法、仿射换元和 Bernstein 系数都由 BigInt 约分有理数准确计算，没有将 Number 舍入结果当区间端点。Number 仅用于展示。

物理导数为

$$
b_j^{(k)}=h^{-k}B^{(k)}(q_j),\qquad
d^{(k)}=\sum_j\rho_jb_j^{(k)}.
$$

准确 $S$ 的区间造成的相关性丢失只扩大包围。normalizedBox 使用 $t=(s-c)/(S-c)$，使 $q_j=(J+3)t-(j+2)$ 准确消去 $S$；输出导数仍为物理 $s$ 导数，绝不误报为 $t$ 导数。physicalBox 则直接消费物理 $s$ 区间。

所有半径参数列也完整给出：

$$
\partial_{\rho_j}(d,d_s,d_{ss})=(b_j,b_j',b_j'').
$$

这里只固定原准确 B32 长度；不是对 $S,c$ 求参数导数。

## 3. 全域半径正性与端口

R190 已准确证明 $0\le\sum_jb_j\le1$。令
$\rho_-=\min(0,\min_j\rho_j)$、
$\rho_+=\max(0,\max_j\rho_j)$，则

$$
\rho_-\le d(s)\le\rho_+,\qquad
a(s)\ge \frac45-\max_j|\rho_j|.
$$

消费者将该独立值域与逐项 Bernstein 值域相交。若取准确 binary64 的 .4 系数盒，下界是

$$
\frac45-\operatorname{binary64}(.4)
=\frac{18014398509481983}{45035996273704960}
>\frac{399}{1000}.
$$

该有理值略小于数学实数 $2/5$；普通 Number 打印可能显示为 .4，不应倒过来当准确 $2/5$。

第一和最后样条的支撑端点恰为 $c,S$。外端的 $B,B',B''$ 均为零，所以所有 $\rho$ 的改变量在两个准确端口都是准确零。该论证只用 C²，不要求样条第三导数在内部结点连续。

## 4. 保存浮点网格与准确网格的连续敏感界

设实际有限程序使用已保存的正浮点步长 $h_f$ 和中心 $\gamma_{f,j}$，将这些 binary64 数分别作为准确 dyadic 常数。定义相应完整实函数

$$
b_{f,j}^{(k)}(s)=h_f^{-k}B^{(k)}
  \left(\frac{s-\gamma_{f,j}}{h_f}\right).
$$

这一步只分离网格参数舍入，不把整个浮点求值过程改称准确运算。

令 $q_{f,j}=(s-\gamma_{f,j})/h_f$。有准确恒等式

$$
q_{f,j}-q_j
=(s-c)(h_f^{-1}-h^{-1})
+\frac{c-\gamma_{f,j}}{h_f}+j+2.
$$

因此在任一物理盒可直接有理包围
$\varepsilon_j=\sup|q_{f,j}-q_j|$，同时包围
$\eta_k=\sup|h_f^{-k}-h^{-k}|$。

完整全局常数可取

$$
M_0=\|B\|_\infty=\frac23,\qquad
M_1=\|B'\|_\infty=\frac23,\qquad
M_2=\|B''\|_\infty=2,\qquad M_3=3.
$$

前两个极值直接由四片多项式求导得到，$B''$ 的片内斜率绝对值至多 3，且自身连续，所以 $B''$ 全局 3-Lipschitz。因而 $k=0,1,2$ 统一有

$$
|b_{f,j}^{(k)}-b_j^{(k)}|
\le M_k\eta_k+M_{k+1}h_f^{-k}\varepsilon_j.
$$

证明是准确加减 $h_f^{-k}B^{(k)}(q_j)$，分别用幅度界与 Lipschitz 界。该公式跨所有支撑边界和样条接点有效，没有假设全局 C³。

同一准确 $\rho$ 下，总改变量的网格误差至多

$$
E_k=\sum_j|\rho_j|
  \left(M_k\eta_k+M_{k+1}h_f^{-k}\varepsilon_j\right).
$$

floatingGridComparison 输出每一项及总有理上界，并明确：

- 这里只包括保存网格常数与准确 $S,c,h$ 的差；
- 尚不包括有限算术操作的累计舍入；
- 尚不包括基础 $a_B$ evaluator 的误差。

另一个接口 returnedPointComparison(s,returnedJets) 把 caller 实际返回的三个 Number 准确解码，与同点严格改变量区间比较。这个点值上界包括该实际返回数中所有误差来源，但不能扩充为全盒浮点程序误差。使用方必须绑定真正返回的数和其来源，不能填入意向值。

若以后将准确 $S$ 更紧区间接入，只需同一个数学定义和新的严格区间证据；当前函数、ρ与 profile 身份不得静默更换。

## 5. 与完整准确基础半径的组合接口

addBase(basePacket,increment) 要求同一准确 base 定义、相同查询和固定物理 $s$ 导数。basePacket 按三个区间给 $a_B,a_{B,s},a_{B,ss}$，并应完整保存其 packet/source 身份。返回逐项和及全部半径参数列。

这一步的数学是

$$
[a,a_s,a_{ss}]
=[a_B,a_{B,s},a_{B,ss}]+[d,d_s,d_{ss}].
$$

完整 B32 reader 尚未提供的基础 jet 不能用一个独立公式或旧数据文件代填。准确 position 的二 jet 仍按 R190 第3节和 R187/R188 的完整 $Y,Y_s,Y_{ss}$ 组合；本组不替这些 angular primitive 支付余项。

## 6. 已真实完成的独立算术 fixture

本次实际 functions JavaScript isolate 已完成调用 runR190RadiusIntervalFixture()，耗时显示 .111 秒，没有启动 Node/OS 子进程，因而不填 OS exit code。

固定 $J=12,c=13/128,S=177/200$，ρ按完整 binary64 序列 $(-.4,.2,.1)$ 周期给出。这个准确有理 $S$ 是独立算术例子，不是 B32 长度或主线候选。

独立点公式使用 truncated powers：

$$
B^{(k)}(t)=
\frac1{(3-k)!}
\sum_{i=0}^4(-1)^i\binom4i(t+2-i)_+^{3-k},
\qquad k=0,1,2.
$$

它与逐片 Bernstein 实现走不同代数路径。实际报告包含：

- 1209 次完整基函数/总和准确点值包围；
- 180 个有理点在连续 Bernstein 盒中的独立对照；
- 两个准确端口全部新增二 jet 为零；
- 三个物理点的真实 rounded-grid 实函数与准确 grid 的独立比较；
- 非零连续盒和所有真实半径参数列；
- 全段浮点网格敏感界：值约 $1.0873\cdot10^{-15}$、一导约 $6.2542\cdot10^{-14}$、二导约 $1.8038\cdot10^{-12}$。严格有理上界保存在报告中，显示小数只供阅读。

第一次模块加载调用在 functions 中没有给 CommonJS require shim，实际返回 ReferenceError，尚未进入任何数学 fixture。随后同源使用 module/require shim 正常加载并真实完成；没有修改数学源或伪造前次完成。

完整报告为 notes/2026-11-12-fd2d-metric-R190-radius-spline-interval-01-report.json，SHA256 814e3415dae1458169a107aa9b0712f692dcfb226d00693c51c2a7fbe78e290d。主线 B32 的准确累计积分、真实完整位置与最终几何证书仍须由对应消费者支付。
