# R317：四个原 CM 轨道的完整 Taylor 运输与第一次 Frobenius 缺项

日期：2026-11-13。**状态：以下四个指定原轨道的完整 Taylor 等式、两层统一尾界、准确 elliptic Fermat 商及固定 $p=59$ 的非零实际缺项均已证明。有限证书验证的是完整同源运输的缺项，不是无穷素数非消失的推断。**

R315 已排除对所有单极来源免费使用一个标量交织。本篇不再停在该一般性结论，而将 R310 的四个实际 CM 轨道逐一保留，并算出原中央行在 R313 同源迹下第一次真正改变的量。

## 1. 四个固定轨道及原中央行

沿 R310、R313，固定 $b=17$、
$$
D(r)=(r+4b)(r^3-204br^2-384b^2r+64b^3),
\qquad A_r=\frac{N(r)}{D'(r)}.
$$
对每个根 $r$ 选
$$
P_r=(a_r,y_r),\quad a_r^3=r,\quad y_r^2=r+b,\qquad
\Gamma_r=\frac{A_r}{2a_r^2y_r}.
$$
$\Gamma_r$ 是三条实际 CM 分式的合计留数系数 $3\varrho_r$。

固定 R313 的正密度惰性素数族中的一个 $p$；全部原极及留数在
$K_p=\mathbb Q_{p^2}$，且所有有关坐标与留数为单位。置
$$
\phi=[-p],\qquad P_{r,n}=\phi^nP_r,
\qquad r_n=x(P_{r,n})^3,\qquad
B_{r,n}=A_r\frac{x(P_{r,n})^2y(P_{r,n})}{a_r^2y_r}.
$$
R313 的实际来源是
$$
g_n(X)=\sum_{D(r)=0}\frac{B_{r,n}}{X-r_n},\qquad
L_n=\mathcal L_H(Hg_n).
$$
特别 $g_0=S/H$，所以
$$
L_0=\mathcal J_S'(0)
$$
是原目标的同一个中央导数。

用 R315 的完整单极核
$$
\mathfrak F_p(P)=2y(P)x(P)^2\mathfrak A_p(x(P)^3),
\qquad
\mathfrak A_p(R)=\sum_{j\ge1}\mathcal L_H(Hx^{-3j})R^{j-1},
$$
准确有
$$
\boxed{
L_n=\sum_{D(r)=0}\Gamma_r\mathfrak F_p(P_{r,n})
   =\sum_{D(r)=0}B_{r,n}\mathfrak A_p(r_n).}               \tag{1}
$$
这里没有删除任何一个原轨道，也没有给新极重新指定留数。$Hg_n$ 一般是亚纯来源；其原点 Newton 输入合法且仍使用原 $H_3$ 乘子。

## 2. 同一个原点对数与完整 Taylor 系列

令 $T_r$ 是 $P_r$ 约化的唯一 $(p+1)$ 挠点提升。R313 给
$$
\phi T_r=T_r,\qquad P_r-T_r\in\widehat E(p\mathcal O_p).
$$
用原微分 $dz=dx/(2y)$ 定义
$$
w_r=\log_E(P_r)=\log_E(P_r-T_r)\in p\mathcal O_p.
$$
于是实际群点等式是
$$
P_{r,n}=T_r+\exp_E((-p)^nw_r).                            \tag{2}
$$
不是将非挠点本身当作挠点，也没有丢掉它与 $T_r$ 的形式群差。

在点变量中写
$$
\partial_P=2y\,\partial_x+3x^2\,\partial_y.
$$
R315 证明 $\mathfrak F_p$ 在 $|x|=|y|=1$ 的整解析函数环中属于
$p\mathcal O_p$。该向量场保持整解析环，所以对每个 $m\ge0$
$$
\partial_P^m\mathfrak F_p\in p\mathcal O_p.                \tag{3}
$$
原形式指数在 $|w|\le p^{-1}$ 上收敛，并解这个原不变向量场的微分方程。因此其唯一 Taylor 展开给
$$
\mathfrak F_p(T_r+\exp_Ew)
=\sum_{m\ge0}\frac{\partial_P^m\mathfrak F_p(T_r)}{m!}w^m.
$$
定义
$$
\boxed{
D_{m,p}=\sum_{D(r)=0}\Gamma_r
      \frac{\partial_P^m\mathfrak F_p(T_r)}{m!}w_r^m.}     \tag{4}
$$
由 (3) 及原 $\Gamma_r$ 为单位，
$$
\boxed{v_p(D_{m,p})\ge1+m-v_p(m!).}                       \tag{5}
$$
于是 (1) 得到完整实际运输：
$$
\boxed{L_n=\sum_{m\ge0}(-p)^{nm}D_{m,p}.}                 \tag{6}
$$
其中
$$
D_{0,p}=L_\infty=\mathcal L_H(Hg_\infty).
$$
对于原 $r=-4b$ 的三挠轨道，$P_r=T_r$、$w_r=0$，所以它只贡献 $m=0$ 项。所有 $m\ge1$ 的项准确来自另外三个非挠轨道。

## 3. 两种展开的全部尾项

### 3.1 Taylor 尾项

对 $m\ge1$，Legendre 公式给
$v_p(m!)\le(m-1)/(p-1)$。因此对任意 $n,M\ge0$，
$$
\boxed{
v_p\left(L_n-\sum_{m=0}^{M}(-p)^{nm}D_{m,p}\right)
\ge
\left\lceil1+(n+1)(M+1)-\frac{M}{p-1}\right\rceil.}        \tag{7}
$$
这个界随 $M$ 趋于无穷；$M=0$ 直接回收 R313 的
$L_n-L_\infty\in p^{n+2}\mathcal O_p$。

### 3.2 每个 Taylor 系数仍保留完整 Newton 行

(4) 中的导数不能替换成其首多项式。准确地，
$$
\boxed{
\begin{aligned}
\partial_P^m\mathfrak F_p(T)
={}&\sum_{h\ge1}(-1)^{h-1}(h-1)!\,\kappa^{-h}\\
&\cdot[z^{dh}]
\left[
\widehat H(z)\,
\partial_P^m\left(
\frac{2y(P)x(P)^2}{x(z)^3-x(P)^3}
\right)_{P=T}
\right].
\end{aligned}}                                                   \tag{8}
$$
这是原 $\mu_3$ 投影后的同一完整 Newton 展开。点变量的导数保持六次起项、原整系数及一致 Gauss 界，故截断 $h\le A$ 的余项赋值至少
$$
\boxed{
M_{p,A}=
\left\lceil\frac{(A+1)(p-1)+6}{2p}\right\rceil+v_p(A!).}  \tag{9}
$$
乘上 $w_r^m/m!$ 以后，还增加至少 $m-v_p(m!)$。

因而若在 (6) 中同时截断 $m\le M$、并在 (8) 中截断 $h\le A$，总误差至少为
$$
\min\left\{
\left\lceil1+(n+1)(M+1)-\frac M{p-1}\right\rceil,\,
M_{p,A}
\right\}.                                                \tag{10}
$$
这给一个两层都有限、误差可任意加深的实际证书。原 Gaussian、所有 tame 进位以及点的全部 Taylor 系数都在 (8) 中；没有把其中任一层的形式展开当作有限维算子。

## 4. 第一次完整缺项是指定的 elliptic Fermat 行

(6) 给
$$
L_{n+1}-L_n
=\sum_{m\ge1}(-p)^{nm}\bigl((-p)^m-1\bigr)D_{m,p}.         \tag{11}
$$
对于 $m\ge2$，$v_p(m!)\le m-2$；故 (5) 使这些项的赋值至少为 $nm+3\ge2n+3$。所以
$$
\boxed{
L_{n+1}-L_n
\equiv(-p)^n(-p-1)D_{1,p}\pmod{p^{2n+3}}.}               \tag{12}
$$

定义原形式对数的准确剩余商
$$
q_p(P_r)=w_r/p\bmod p.
$$
如果 $e_r$ 是 $P_r$ 在 $E(\mathbb F_{p^2})$ 中的阶，则 $e_r\mid p+1$，且
$$
\boxed{
q_p(P_r)=\frac{t([e_r]P_r)}{e_rp}\pmod p,\qquad
t=-x/y.}                                                 \tag{13}
$$
因为 $[e_r]P_r$ 在形式群中，$\log_E(t)=t+O(t^7)$。这个公式保留原点和实际整数乘法；不是以一个任意数域单位的 Fermat 商代替。

沿 R315 的同一个首一多项式，令
$$
K_p(R)=\sum_{j=1}^{(p+1)/6}
[z^{p+1}](Hx^{-3j})R^{j-1},
$$
$$
G_p(R)=(7R+4b)\overline K_p(R)
             +6R(R+b)\overline K_p'(R),
\qquad c_p=\kappa^{-1}/p\bmod p.
$$
R315 的完整导数首层及 (4) 准确给
$$
\boxed{
W_p:=D_{1,p}/p^2\bmod p
=c_p\sum_{C_3(r)=0}
     \frac{\overline A_r\,G_p(\bar r)}
          {\bar a_r\bar y_r}\,q_p(P_r).}                 \tag{14}
$$
这里求和恰为三个原非挠轨道；原三挠轨道的 $q_p$ 为零。改变立方根 $a_r$ 或 $y_r$ 的符号时，分子中的真实对数标签同步改变，(14) 不变。整个原来源在 $\mathbb Q$ 上，故 $W_p\in\mathbb F_p$。

将 (12) 除以原精度，得到
$$
\boxed{
\frac{L_{n+1}-L_n}{p^{n+2}}
\equiv(-1)^{n+1}W_p\pmod p\qquad(n\ge0).}                 \tag{15}
$$
因此 $W_p\ne0$ 时，所有这些实际相邻缺项都准确具有赋值 $n+2$。

(14) 不是一个免费的跨素数非消失定理。它的系数是指定原 $H_3$ 的真实首多项式，$q_p$ 是三个固定非挠点的实际 elliptic Fermat 商；两者都不能删掉。完整 $D_{1,p}$ 的系数
$\partial_P\mathfrak F_p(T_r)$ 一般仍是 $p$ 进解析量，本文不把它们冒充代数系数以直接调用解析子群定理。

## 5. 原 $p=59$ 四轨道的完整证书

以下只用一个固定素数验证新缺项；正密度族及原目标的无穷素数要求不由有限数据推断。取
$$
p=59,\qquad \delta^2=-3,\qquad K_p=\mathbb Q_{59}(\delta).
$$
三个 $u=r/b$ 根模 $59$ 为 $45,47,53$，并逐一 Hensel 提升为原多项式
$u^3-204u^2-384u+64=0$ 的真代数点。脚本使用精度 $59^{12}$。

R315 的实际 $H_3$ 首核是
$$
\begin{aligned}
K_{59}(R)\equiv{}&
8+31R+27R^2+19R^3+39R^4+57R^5\\
&+29R^6+19R^7+8R^8+R^9\pmod{59},
\end{aligned}
$$
并且 $c_p=19$。完整点标签及第一次缺项如下。

| 原轨道 | $r\bmod59$ | $a\bmod59$ | $y\bmod59$ | 剩余阶 $e_r$ | $q_{59}(P_r)$ | (14) 的该轨道贡献 |
|---|---:|---:|---|---:|---|---:|
| $r=-4b$ | $50$ | $18$ | $28\delta$ | $3$ | $0$ | $0$ |
| $u\equiv45$ | $57$ | $21$ | $29$ | $20$ | $14$ | $24$ |
| $u\equiv47$ | $32$ | $56$ | $7$ | $30$ | $22$ | $1$ |
| $u\equiv53$ | $16$ | $17$ | $15\delta$ | $20$ | $38\delta$ | $55$ |

原 $A_r$ 依次为 $19,49,26,25$，原 $K_{59}(r)$ 依次为 $28,16,2,29$。于是
$$
L_0/59\equiv19\sum_r A_rK_{59}(r)\equiv1\pmod{59},
$$
而完整第一次缺项是
$$
\boxed{W_{59}=24+1+55\equiv21\pmod{59}.}                  \tag{16}
$$

### 5.1 对数商由完整椭圆群加法计算

对每个原点，脚本在 $\mathbb Z/59^{12}\mathbb Z[\delta]$ 中使用 Jacobian 坐标
$x=X/Z^2,\ y=Y/Z^3$，计算真正的 $[e_r]P_r$。所有中间群加法均保留，不用一个局部猜测阶替代。最后的原整参数为
$$
t([e_r]P_r)=-XZ/Y.
$$
末点的 $Y$ 是单位、$Z$ 被 $59$ 整除，所以 (13) 给表中的准确对数商。三挠轨道得到的参数准确为零；另外三条得到的 $q_{59}$ 都为单位。

### 5.2 不使用核的 Taylor 公式，直接核对移动点

脚本另以椭圆群加法计算
$$
[-59]P_r=P_r-[60]P_r
$$
到模 $59^2$，并重新取
$$
r_1=x([-59]P_r)^3,\qquad
B_{r,1}=A_r\frac{x([-59]P_r)^2y([-59]P_r)}{a_r^2y_r}.
$$
这里的移动点坐标完整保存于 JSON。

具体计算精度是可核定的。若 $t=t([e_r]P_r)\in59\mathcal O_p$，
则 $[60/e_r]$ 的形式参数是 $(60/e_r)t+O(t^7)$。
在 Jacobian 正式规范中，该形式点可写成
$(1+O(t^6),-1+O(t^6),(60/e_r)t+O(t^7))$。
将它与原 $P_r$ 做实际群加法，再规范化成仿射坐标时，此例只损失至多三个 $59$；
省掉的 $O(t^6)$ 项因此仍至少为 $59^3$，足以得到准确模 $59^2$ 坐标。脚本逐个核定移动点的原曲线方程。

用这些独立的移动点，计算
$$
\frac{B_{r,1}K_{59}(r_1)-A_rK_{59}(r)}{59}\pmod{59}.
$$
这里任取 $\overline K_{59}$ 系数的整提升都给同一结果：改变提升所加的 $59Q$，因 $B_{r,1}\equiv A_r$、$r_1\equiv r\pmod{59}$，对分子只改变一个 $59^2$ 的倍数。
四个值依次是
$$
0,\qquad36,\qquad31,\qquad53.
$$
因此由原 Newton 首层和 R313 的额外一层尾界，
$$
\boxed{
\frac{L_1-L_0}{59^2}
\equiv19(0+36+31+53)
\equiv38\equiv-21\pmod{59}.}                              \tag{17}
$$
这个计算直接使用原 theta 首核和实际移动极，独立核对了 (14)–(15) 的符号、原留数、尺度和全第一次缺项。所有 $h\ge2$ 的 Newton 差项由 R313 的 (23) 至少被 $59^3$ 整除，故没有用截断值冒充完整中央差。

## 6. 当前实际接口

(6)、(8) 给四原轨道的完整解析运输；(7)、(9) 允许同时控制两个无限展开。原 trace 常数已按 R312–313 的真实参考投影消去，留下的非恒定差项在 (14) 中有准确算术含义。

这证明了原四轨道的一个具体事实：即使保持同一个 $H_3$ 和同一个中央观察，真实 $[-p]$ trace 也不能直接替换成恒等行；$p=59$ 的完整缺项已由 (17) 确认非零。进一步使这些真实差项与原算术来源发生一个可用闭环，或证明原 $L_0$ 跨素数非零，仍需要新的原输入。

生产文件
[check-jzero-four-original-orbits-frobenius-defect.py](../scripts/check-jzero-four-original-orbits-frobenius-defect.py)
及其 JSON 有 **25 项精确检查全部 PASS**。脚本使用旁列 R315 JSON 的已证明原首核，独立重做全部原点提升、剩余阶、完整群加法、对数商及移动点差项。

直接依赖：
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R310](R310-jzero-actual-rankzero-frame-third-kind-and-central-transpose.md)、
[R312](R312-original-central-projection-fixed-poles-and-complete-kernels.md)、
[R313](R313-jzero-frobenius-square-actual-trace-and-central-first-layer.md)、
[R315](R315-original-pole-kernel-first-polynomial-and-actual-trace-orbits.md)。

