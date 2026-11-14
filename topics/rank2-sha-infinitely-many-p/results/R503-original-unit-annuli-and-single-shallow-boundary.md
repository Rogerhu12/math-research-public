# R503 — 原三输入的全部浅环带、正交 18/2466 核与唯一单位边界

日期：2026-11-14。**状态：已证明。** 本篇继续 R497、R500 的同一个原
六 sigma 来源和同一个纯 $T_c$ 算术测试，不增加曲线，也不把辅助来源
的中央赋零。

本文付清三件具体事情：

1. $W'/2$ 有一个显示的 degree2466 真正正交伴随；在压缩后的整个
   两变量来源上，两轴 core 分别为 $\beta,\chi_V\lambda$，保第三个独立
   sigma。
2. R500 的每条正深浅环带都准确等于一个固定解析函数的 Euler 差；
   所有这些环带的质量和中央导数均有非零首项。原完整浅支只剩一个
   $Z$ 单位边界。
3. 同一正次数算术测试的真实质量五阶系数也显示算出。它不能在
   后续尺度运输中省略。

$\chi_V$ 专指 R500 的 degree3699 符号，$\chi_V^2=1$；
不将它认作 R488 的 degree29 符号。主目标仍未完成。

## 1. 来源、物理坐标与全部既有核心

保留 R500 的
$$
\delta^2=-3,\quad \gamma=(5+\delta)/2,\quad
\lambda=-\bar\pi_0^{-1},\quad
\beta=-\lambda,\quad \kappa=p\lambda^2,\quad d=p-1,
\tag{1}
$$
以及 $b=17$、原周期 $\Omega$ 和固定 ray。令
$$
\alpha=37+3\delta,\qquad
Z=z\boldsymbol u,\quad V=v\boldsymbol u,\quad
Y=Z+\bar\gamma x,\quad T_c=\gamma Z-27x,
\tag{2}
$$
其中五个原输入按
$\boldsymbol u=(\xi_1,\xi_2,\xi_3,c,d_0)$ 排列，
$x=\xi_4$ 是第六个独立 sigma 输入。系数是
$$
z=(\delta,2\delta,\gamma,1,2),
$$
$$
v=\left((63+17\delta)/2,\ 9-10\delta,\ -17+14\delta,\
22+12\delta,\ 17-3\delta\right).
\tag{3}
$$

R500 已合法约去三个共同伴随深度，留下显示的整个来源
$$
\mathcal L(s,t)=-\frac1{84}
 \prod_{j=1}^5\sigma(z_js+v_jt),\qquad
\nu=\nu_{\mathcal L}\otimes\nu_\sigma .
\tag{4}
$$
它是原联合的推前，不是把五个独立深事件先改成两个输出深事件。
其 $Z$ 边际为
$$
B_{27}(s)=-\frac1{84}\sigma(\delta s)\sigma(2\delta s)
 \sigma(\gamma s)\sigma(s)\sigma(2s)
=\bar\gamma^{-1}s^5+O(s^{11}).
\tag{5}
$$
在整个 (4) 上，$Z,V,x$ 的 cores 分别为
$$
\beta,\qquad \chi_V\lambda,\qquad\beta.
\tag{6}
$$
$W'=(\alpha Z+2V)/27$ 的 core 是 $\beta$，并固定独立输入 $x$。
这些完整身份和 R500 的三伴随压缩均继续使用。

记 R497 的实际测试为
$$
h(t)=\mathfrak h_{b,p}^{\times}(t)
=\sum_{k=1}^6
 \frac{c_kb^{-k}}{1-\lambda\kappa^{6k}}t^{6k},
\tag{7}
$$
其中六个显示的有理数 $c_k$ 正是 R497(16)–(18)。
该同一个测试满足整个第一来源身份
$$
Y_*\{{\bf1}_{T_c\ {\rm unit}}h(T_c/\Omega)\nu\}=\nu_S.
\tag{8}
$$
所以在 $V$ 深 $n$ 时，完整 Mellin 行是
$(\chi_V\lambda)^nJ_S(u)$，不是一条新的辅助中央。

## 2. 真正正交的 degree18/2466 两轴

定义
$$
\boxed{
U=\frac{W'}2=\frac{\alpha Z+2V}{54},\qquad
P=\frac{-274Z+\bar\alpha V}{54}.
}
\tag{9}
$$
这里 $P$ 是新的单个物理伴随，不指 R500 的三个 $Q_i$。
从 $(Z,V)$ 到 $(U,P)$ 的矩阵和逆准确为
$$
M=\begin{pmatrix}
 \alpha/54&1/27\\ -137/27&\bar\alpha/54
\end{pmatrix},\qquad
M^{-1}=\begin{pmatrix}
 \bar\alpha/36&-1/18\\137/18&\alpha/36
\end{pmatrix},\qquad \det M=2/3.
\tag{10}
$$
因此
$$
Z=\frac{\bar\alpha U-2P}{36},\qquad
V=\frac{274U+\alpha P}{36}.
\tag{11}
$$

原 Gram 为 $\operatorname{diag}(27,3699)$。
直接相乘给
$$
\boxed{M\operatorname{diag}(27,3699)\bar M^{\,t}
=\operatorname{diag}(18,2466).}
\tag{12}
$$
两个输出在五个原 sigma 上的全部系数分别为
$$
u=(1+\delta,\delta,1+\delta,(3+\delta)/2,2),
$$
$$
p=(23-\delta,(9-35\delta)/2,-22+8\delta,12+7\delta,1-3\delta).
\tag{13}
$$
它们都在 $\mathcal O_K$。每行模二恰有两个单位系数，故第一、第二
轴都是标准偶 theta 线丛；交叉项严格为零。新的完整来源是
$$
\boxed{\widetilde{\mathcal L}(s,t)
=-\frac1{84}\prod_{j=1}^5\sigma(u_js+p_jt)
\in\mathcal S_{18}\boxtimes\mathcal S_{2466}.}
\tag{14}
$$
它与 (4) 仅相差显示的完整坐标推前，第三输入 $x$ 不变。
特别第一边际为
$$
\widetilde{\mathcal L}(s,0)
=\frac{\omega^2}{84}\sigma(2s)^3\sigma(\delta s)^2.
\tag{15}
$$
(15) 没有被赋算术 rank-two 身份。

$U$ 的整个来源 core 是 $\beta$，因为它是 R500 的 $W'$ 乘以
固定普通单位 $1/2$，物理投影不变。为确定第二轴，不猜 whole
$K_{2466}$ 的绝对相位：由 (10)，$Z,V$ 同时深与 $U,P$ 同时深
是同一个完整域，前者由 (6) 给
$-\chi_V\lambda^2[\kappa,\kappa]_*\nu_{\mathcal L}$。
用 $U$ 的 $\beta=-\lambda$ core 并取消其可逆推前，得到
$$
\boxed{
\nu_{\widetilde{\mathcal L}}|_{P\in p}
=\chi_V\lambda[1,\kappa]_*
 \nu_{\widetilde{\mathcal L}}.
}
\tag{16}
$$
这是真实来源的第二轴身份，不是对整个 $\mathcal S_{2466}$ 的
未经定标推断。因此对 $a,b\ge0$，
$$
\boxed{
\nu_{\widetilde{\mathcal L}}|_{U\in p^a,\ P\in p^b}
=\beta^a(\chi_V\lambda)^b[\kappa^a,\kappa^b]_*
 \nu_{\widetilde{\mathcal L}}.
}
\tag{17}
$$

将第一轴幂等矩阵搬回 $(Z,V)$，准确为
$$
M^{-1}\begin{pmatrix}1&0\\0&0\end{pmatrix}M
=\frac1{1944}
\begin{pmatrix}
1396&2\bar\alpha\\274\alpha&548
\end{pmatrix}.
\tag{18}
$$
故 (17) 仍是 R500 的同一个 $W'$ 核，未更换物理方向。

## 3. 一个固定解析函数包含全部正深度贡献

对 $T\in p\mathcal O$ 定义整个 Mellin 函数
$$
\boxed{
\mathcal A(u,T)=
 \int_{x\ {\rm unit}}
 \langle\bar\gamma x+TZ\rangle^{du}
 h((\gamma TZ-27x)/\Omega)
 \,d(\nu_{B_{27}}(Z)\otimes\nu_\sigma(x)).
}
\tag{19}
$$
积分中的 $Z$ 不受深度限制。
因为 $T$ 深且 $x$ 为单位，两个线性式都是单位，所有括号都在
其真实定义域。置
$$
\mathcal A_0(T)=\mathcal A(0,T),\qquad
A(T)=\partial_u\mathcal A(0,T).
\tag{20}
$$
(19) 是 R497 已付第五阶的同一个原五 sigma 函数，忘却四个
正交伴随后就是 (5)，没有改变周期或常数。

进一步限制 $Z$ 单位，记其 Mellin 函数为 $\mathcal F(u,T)$。
由 $B_{27}$ 的完整 core $\beta$，
$$
\boxed{
\mathcal F(u,T)=\mathcal A(u,T)-\beta\mathcal A(u,\kappa T).
}
\tag{21}
$$
这是全函数等式，含质量及中央；没有把尺度 $\kappa$ 从
$\bar\gamma x+TZ$ 中提出。

### 3.1 所有中央系数的准确规则

写 $h(t)=\sum_{m\in\{6,12,\ldots,36\}}h_mt^m$，并记
$$
\mu_k=\int Z^k\,d\nu_{B_{27}},\qquad
I_\ell=\int_{x\ {\rm unit}}x^\ell d\nu_\sigma,\qquad
I_{\ell,\log}=\int_{x\ {\rm unit}}x^\ell\log\langle x\rangle d\nu_\sigma.
$$
负的 $\ell$ 同样在单位域上有定义。令
$$
L_{mk}={\bf1}_{k\le m}\binom mk\gamma^k(-27)^{m-k},
$$
$$
C_{mk}=
\sum_{j=0}^{\min(m,k-1)}
 \frac{(-1)^{k-j-1}}{(k-j)\bar\gamma^{k-j}}
 \binom mj\gamma^j(-27)^{m-j}.
\tag{22}
$$
由两项有限二项展开和 $\log(1+t)$ 的整盘展开，逐项得到
$$
\boxed{
[T^k]A(T)=d\mu_k\sum_m h_m\Omega^{-m}
 \left\{C_{mk}I_{m-k}
 +L_{mk}\big(I_{m-k,\log}
       +\log\langle\bar\gamma\rangle I_{m-k}\big)\right\}.
}
\tag{23}
$$
全部真正 log 行和固定尺度 log 都保留在 (23)。

(5) 的型为五，且首零阶为五，故
$$
A(T)=\sum_{j\ge0}a_{6j+5}T^{6j+5}.
\tag{24}
$$
R497 的完整首项计算给 $a_5$ 为单位，删除的只是该篇显示的固定
有限坏素数集。R497 的全尾论证也直接由 (23) 读出：
$$
v_p(a_k)\ge-\lfloor\log_p k\rfloor.
\tag{25}
$$
因为 $h$ 整、所有正矩整、单位负矩有界，而显式分母只有
$1,\ldots,k$。因此对每个 $r\ge1$，
$$
\boxed{
v_p(A(\kappa^r))=5r,\qquad
v_p\big(A(\kappa^r)-\beta A(\kappa^{r+1})\big)=5r.
}
\tag{26}
$$
第二式也可逐系数读成乘单位 $1-\beta\kappa^k$。
所有高阶项的赋值严格超过 $5r$，不是只作有限截断判断。

## 4. 同一来源的质量是显示的六项多项式

质量不能用中央为零代替。写原规范
$$
\sigma_b(s)=s\sum_{i\ge0}a_i b^i s^{6i},\qquad
B_{27,b}(s)=\bar\gamma^{-1}s^5
 \sum_{j\ge0}H_jb^js^{6j}.
\tag{27}
$$
$a_i,H_j$ 完全由 R497(11)–(12) 的固定递推定义，$a_0=H_0=1$。
在 $u=0$ 时只有测试多项式，所以 (19) 的质量准确是
$$
\boxed{\mathcal A_0(T)=\sum_{j=0}^5M_jT^{6j+5},}
\tag{28}
$$
其中
$$
\boxed{
M_j=\frac{\gamma^{6j+5}H_j}{\bar\gamma b}
 \sum_{k=j+1}^{6}
 c_k(6k)!(-27)^{6(k-j)-5}a_{k-j-1}
 \frac{1-\beta\kappa^{6(k-j)-5}}
      {1-\lambda\kappa^{6k}}.
}
\tag{29}
$$
证明是将 $h$ 展开后使用实际单位正矩
$$
I_\ell=(1-\beta\kappa^\ell)\ell!\Omega^\ell[s^\ell]\sigma_b(s).
$$
$\Omega$ 的幂逐项完全抵消；$b$ 的剩余幂全部为 $b^{-1}$。
因此 (28) 是原质量的全公式，不是仅首项相合。

首项的固定有理和为
$$
R_0=\sum_{k=1}^6c_k(6k)!(-27)^{6k-5}a_{k-1}
=
\frac{
65697892675002405040626188558622031253105091375280933452405
}{
60965943523105331968822263375218291443315617960283253727910014976
}.
\tag{30}
$$
它模 $101$ 为 $79$，尤其严格非零。
附证书使用
$$
(a_0,\ldots,a_5)=
\left(
1,\frac1{210},-\frac1{1801800},
-\frac{23}{366648282000},
\frac{31}{77920092890640000},
-\frac{9103}{956184731893555164000000}
\right)
$$
和 R497 的全部六个 $c_k$ 在特征零中核 (30)。
又 $\gamma^6=-143+180\delta$，故
$$
M_0\equiv\frac{\gamma^6R_0}{7b}\pmod p.
\tag{31}
$$
除 (30) 分子、分母的固定有限素因子以及既有坏集后，$M_0$ 是单位。
这些删除不改变固定 ray 上的无穷性。于是每个 $r\ge1$ 都有
$$
\boxed{
v_p(\mathcal A_0(\kappa^r))=
v_p\big(\mathcal A_0(\kappa^r)
       -\beta\mathcal A_0(\kappa^{r+1})\big)=5r.
}
\tag{32}
$$
这项质量结论不以 $J'_S(0)=0$ 为假设。

## 5. 每条真实 W' 浅环带及其完整移动测试

在 R500 的三个真实输入中，对 $n\ge1$、$0\le r<n$ 令
$$
D_{n,r}=\{V\in p^n,\ v_p(U)=r,\ Y,T_c\ {\rm unit}\}.
\tag{33}
$$
排除 $349$ 后，$\alpha$ 是单位。由于 $V$ 深 $n$，
$U$ 与 $Z$ 的赋值在浅层相同。因此对 $1\le r<n$，
$$
D_{n,r}=\{V\in p^n,\ v_p(Z)=r,\ x\ {\rm unit}\}.
\tag{34}
$$
这一次域等价只在 $r\ge1$ 成立；$r=0$ 不得删 $Y,T_c$ 的单位条件。

先用 $V$ core，再用 $Z$ 的第 $r$ 层 core，得到完整 Mellin 式
$$
\boxed{
\int_{D_{n,r}}\langle Y\rangle^{du}h(T_c/\Omega)\,d\nu
=(\chi_V\lambda)^n\beta^r
 \left\{\mathcal A(u,\kappa^r)
       -\beta\mathcal A(u,\kappa^{r+1})\right\},
\quad 1\le r<n.
}
\tag{35}
$$
所以每条正深浅环带的质量及中央导数均恰有赋值 $5r$。
它们不是新的未定辅助中央。

也可完全从 $W'$ 方向读 (35)，从而核实其与物理 core 相容。
由 (11)，(33) 先推出 $v_p(P)=r$。使用 (17) 依次缩回 $U,P$
的第 $r$ 层，原域准确变成
$$
\boxed{
U\ {\rm unit},\qquad
274U+\alpha P\in p^{n-r},\qquad x\ {\rm unit}.
}
\tag{36}
$$
此时 $P$ 和 $Z_0=(\bar\alpha U-2P)/36$ 都是单位。
标量为 $\beta^r(\chi_V\lambda)^r$，而所有测试都必须写成
$$
\boxed{
\langle\kappa^r Z_0+\bar\gamma x\rangle^{du}
 h((\gamma\kappa^rZ_0-27x)/\Omega).
}
\tag{37}
$$
(36) 是实际 $W'$ 单位环带中的一条移动斜管；
$274U+\alpha P$ 的条件没有消失。再用 $V$ core 才回到 (35)。
这说明两种真实核比较给同一完整式；它们不额外给浅支赋零。

## 6. 全部浅层只有一个固定单位边界

定义保持全部单位条件的固定边界函数
$$
\boxed{
B_0(u)=
\int_{\substack{Z\ {\rm unit}\\Y=Z+\bar\gamma x\ {\rm unit}\\
                         T_c=\gamma Z-27x\ {\rm unit}}}
 \langle Y\rangle^{du}h(T_c/\Omega)
 \,d(\nu_{B_{27}}(Z)\otimes\nu_\sigma(x)).
}
\tag{38}
$$
$x$ 在 (38) 中允许单位和非单位，两个近相消支都按显示条件保留。
由 (8)，整个 $S$ Mellin 行严格分成
$$
\boxed{J_S(u)=B_0(u)+\beta\mathcal A(u,\kappa).}
\tag{39}
$$
第二项正是 $Z$ 深、$x$ 单位的完整支；没有漏掉其他深度。

在 (33) 的 $r=0$ 支使用 $V$ core，只因 $V$ 深才有
$U$ 单位等价 $Z$ 单位，故其值为
$(\chi_V\lambda)^nB_0(u)$。将它和 (35) 相加，所有中项望远镜消去：
$$
\boxed{
\begin{aligned}
&\int_{\substack{V\in p^n,\ U\notin p^n\\Y,T_c\ {\rm unit}}}
 \langle Y\rangle^{du}h(T_c/\Omega)\,d\nu\\
&\qquad=(\chi_V\lambda)^n
 \left\{B_0(u)+\beta\mathcal A(u,\kappa)
                  -\beta^n\mathcal A(u,\kappa^n)\right\}\\
&\qquad=(\chi_V\lambda)^n
 \left\{J_S(u)-\beta^n\mathcal A(u,\kappa^n)\right\}.
\end{aligned}}
\tag{40}
$$
这就是 R500 唯一浅支的完整求和，不是只列一串等价域。

令 $n\to\infty$ 也给收敛的确切环带和
$$
\sum_{r\ge1}\beta^r
 \{\mathcal A(u,\kappa^r)-\beta\mathcal A(u,\kappa^{r+1})\}
=\beta\mathcal A(u,\kappa).
\tag{41}
$$
收敛来自首阶五与全尾界，不需要对 $u$ 的形式截断。

原 $S$ 的质量为零，所以无条件有
$$
\boxed{B_0(0)=-\beta\mathcal A_0(\kappa),\qquad
       v_p(B_0(0))=5.}
\tag{42}
$$
若再使用反证输入 $J'_S(0)=0$，则准确为
$$
\boxed{B'_0(0)=-\beta A(\kappa),\qquad
       v_p(B'_0(0))=5.}
\tag{43}
$$
而整个第 $n$ 层浅支的中央在此输入下为
$-(\chi_V\lambda)^n\beta^nA(\kappa^n)$，赋值为 $5n$。
因此各正浅环带虽然都非零，仍与唯一的单位边界发生精确逐层抵消。
(39) 表明无穷多层并没有免费产生无穷多个新的独立算术零条件。

## 7. 后续使用时的实际接口

全部未知已集中为 (38) 这一个固定来源上的单位边界；
其中包括 $x$ 深支，以及 $x$ 单位时
$Z+\bar\gamma x$、$\gamma Z-27x$ 两条近相消支的真实删去。
(29)、(42) 给出其质量，不可以将它当作零质量辅助来源。
(23)、(35) 则给所有正深环带的完整中央和尺度 log。

如果以后把整个 $(Z,V,x)$ 同时缩深，原共同 core 是
$(\chi_V\lambda^3)^n$。对第 $m$ 个单项测试，实际第一 log
还增加
$$
n\,d\log\langle\lambda^2\rangle
$$
乘以同域质量，并有 $\kappa^{mn}$ 的多项式因子。
这里 $p$ 的 log 按原普通规范为零。
(28)–(32)、(42) 正是支付这类非齐次项的真实质量资料；
不能用 $J_S(0)=0$ 去抹掉 (38) 的非零质量。

本篇并未证明 (43) 不可能。要完成主目标，仍须用真正改变 $Y$
的来源身份控制 (38)，或得到该边界与原合格中央之间新的非齐次
关系；不能再将 (40) 中的浅支删去。

## 证书与依赖

- [精确有理/CM 证书程序](../scripts/check-r503-original-unit-annuli-and-boundary.mjs)；
  [全部有限数据](../scripts/check-r503-original-unit-annuli-and-boundary.json)。
  程序核整个 (10)–(18)、实际五输入系数、sigma 递推及 (30)，
  使用 BigInt 有理数。执行器失效后，同一程序的纯 JavaScript
  证书函数已在可用 V8 工具运行并通过；无目标素数数值扫描。
- [R497：同一个完整 S 测试、首五阶单位与全尾](R497-original-degree918-positive-companion-and-six-sigma-arithmetic-grid.md)。
- [R500：原 3699 轴、全部输入、三伴随压缩和唯一浅支](R500-original-pure-y-axis3699-and-complete-w-depth-complement.md)。
- [R493：真实六 sigma 几何、B27 和 W' 完整核心](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
