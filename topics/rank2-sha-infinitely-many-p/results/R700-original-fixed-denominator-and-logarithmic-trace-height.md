# R700 — 原全迹的固定分母、全部复共轭及对数高度上界

日期：2026-11-15。**状态：已证明。** 主目标仍未完成。

本篇保 [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)
的同一个绝对根、同一个全 $H$ 迹以及原完整边界。
固定倍点循环同时给全部有限位的准确归一；原 Klein 模则控制全部
复共轭。两者把 R696 的 $O(p)$ 迹高度改进为
$\log(p+1)+O(1)$。

因此非零原边界的 $p$ 进赋值至多 $1+O(1/\log p)$。
这是一个“非零时”的上界，不证明该迹非零，
也不预支原中央 $j_m=0$ 对边界的任何下界。

## 1. 同一个原数、全部根及固定多项式

固定
$$
p=6s-1>101,\quad q=p^2,\quad d=p+1,\quad
K_0=\mathbf Q(\omega),\quad E:y^2=x^3+b,\quad b=17.
\tag{1}
$$
沿 R696 记
$$
F=K_0(E[p]),\qquad F_2=K_0(E[p^2]),\qquad
H=\ker(\mathbf F_q^\times\longrightarrow\mathbf F_p^\times).
$$
原归一为
$$
\alpha=\omega^2+p\omega,\quad
a_T=\frac{\psi_\alpha(T)^{2s}}{\psi_{p+1}(T)^{2s-1}},\quad
w^p=a_T,\qquad T\in E[p]\setminus0.
\tag{2}
$$
$w$ 可取任意一个根，但一旦选定就始终用这个根。
R696 已付全部根在 $F_2$，其共同域 $W=F(w)$ 与非零 $T$ 无关，
$[W:F]\le p$。令 $\widetilde H$ 为
$\operatorname{Gal}(W/F^H)$ 中阶 $d$ 的唯一 Hall 子群，置
$$
E_W=W^{\widetilde H},\qquad
Z_{m,T}=w^{-m}\phi_m(T),\qquad
\mathcal T_{m,T}=\operatorname{Tr}_{W/E_W}Z_{m,T}.
\tag{3}
$$
这里的 $\widetilde H$ 限制到 $F$ 正是 $H$。
$E_W$ 在 $p$ 处只有一个位，其局部度等于绝对数域次数。
这些是原全除点域的事实，未重新指定有限根。

令 $X=x^3$，原两个多项式可写为
$$
\begin{split}
\phi_{34}
 &=\frac{x^2}{7}(X+b)(X-8b)(7X^2-4bX+16b^2),\\
\phi_{72}
 &=x\,\phi_{34}(X+4b)
       (X^3-96bX^2+48b^2X+64b^3)
       (X^2+20bX-8b^2).
\end{split}
\tag{4}
$$
所以 $7\phi_m\in\mathbf Z[x]$，只有 $O$ 极点，
极阶准确为 $m-6$，最高项系数为 1。
这是原 $S=\sigma^{34}\phi_{34}$、
$T=\sigma^{72}\phi_{72}$；没有改来源或微分尺度。

为以后所有素数同时使用，明确取
$$
\boxed{
D_m=7\cdot2^{\lceil m/3\rceil}
       3^{\lceil m/4\rceil}17^{\lceil m/6\rceil},
\qquad m=34,72.
}
\tag{5}
$$
也可对两来源统一使用 $D=7\cdot2^{24}3^{18}17^{12}$。
这些整数与 $p,T,w$ 无关，且对 (1) 的所有 $p$ 都是 $p$ 单位。

## 2. 原倍点函数及其完整循环

暂选原代数不变微分对应的复周期格 $\Lambda$。
保持 R694/R696 的
$$
\mathfrak k(z)=e^{-\eta_z z/2}\sigma(z).
\tag{6}
$$
R696 已证明每个 $p$ 挠点代表 $z_T$ 的 $\mathfrak k(z_T)$ 是代数数，
且
$$
a_T=\xi_T\mathfrak k(z_T)^{-p},\quad \xi_T\in\mu_{6p},
\qquad
w=\rho_T/\mathfrak k(z_T),\quad \rho_T\in\mu_{6p^2}.
\tag{7}
$$
这些根单位的 $p$ 部分也保留；它们在每个有限位的赋值均为零。

原 $\sigma(z)\sim z$、$Dx=2y$ 的规范给
$$
\Psi_2(P(z))=\frac{\sigma(2z)}{\sigma(z)^4}=-2y(P(z)).
$$
实线性准周期满足 $\eta_{2z}\,2z=4\eta_z z$，所以准确有
$$
\boxed{
\mathfrak k(2z)=\Psi_2(P(z))\mathfrak k(z)^4.
}
\tag{8}
$$
特别没有为不同 $T$ 各选一份可变非单位归一。

令 $r$ 为 $2$ 在 $(\mathbf Z/p)^\times$ 中的阶。
$2^rT=T$，而 $\mathfrak k(2^rz_T)/\mathfrak k(z_T)$
是原准周期的根单位，见 R694(9)–(10)。
因此对任意有限位 $v$，若
$$
v(\Psi_2(2^jT))=a_v\quad(0\le j<r),
$$
则迭代 (8) 严格给
$$
(1-4^r)v(\mathfrak k(z_T))
=a_v\sum_{j=0}^{r-1}4^j,\qquad
\boxed{v(\mathfrak k(z_T))=-a_v/3.}
\tag{9}
$$
下节在同一潜好模型上证明整个循环有相同的 $a_v$。
此处不需要控制 $r$ 的大小。

## 3. 每个非 p 有限位的准确赋值

本节所有 $\ell$ 进赋值归一为 $v_\ell(\ell)=1$；
可先到一个有限扩张上作潜好变换，最后按该归一下降。
取 R691 的同一个固定模型：

| 剩余特征 | 原坐标与好模型 | 缩放 $c$ 的赋值 |
|---|---|---|
| $2$ | $x=c^2X,\ y=c^3(Y+1/2)$，$c^6=68$；$Y^2+Y=X^3$ | $v_2(c)=1/3$ |
| $3$ | $x=r+c^2X,\ y=c^3Y$，$r^3=-17,\ c^4=3r^2$；$Y^2=X^3+(3r/c^2)X^2+X$ | $v_3(c)=1/4$ |
| $17$ | $x=c^2X,\ y=c^3Y$，$c^6=17$；$Y^2=X^3+1$ | $v_{17}(c)=1/6$ |
| $\ell\ne2,3,17$ | 原模型已好，取 $c=1$ | $v_\ell(c)=0$ |

三个新模型的判别式分别为 $-27,-16,-432$，
在各自剩余特征下均为单位。第三行只用于 $\ell=17$。

现设 $\ell\ne p$。好模型的 $\mathcal E[p]$ 有限 étale，
故任何非零 $p$ 挠截面的约化仍是阶 $p$ 的非零点。
因此其坐标 $X,Y$ 整，且约化不在 $[2]$ 的核中。
原循环的每个 $2^jT$ 都满足这一性质。

在 $2$ 处，
$$
\Psi_2(T)=-c^3(2Y(T)+1),
$$
括号恒为单位。在其余各行，
$$
\Psi_2(T)=-c^3\,2Y(T).
$$
此时 $2$ 可逆，$2Y(T)$ 约化为零准确表示一个二挠点，
与点的阶为 $p>2$ 矛盾。
所以每一行、循环中每一个点都准确满足
$$
v_\ell(\Psi_2(2^jT))=3v_\ell(c).
\tag{10}
$$
(9)、(7) 因而给
$$
\boxed{
v_\ell(w)=
\begin{cases}
1/3,&\ell=2,\\
1/4,&\ell=3,\\
1/6,&\ell=17,\\
0,&\ell\notin\{2,3,17,p\}.
\end{cases}}
\tag{11}
$$

(11) 对所涉及数域的每一个有限位都成立，不仅对一个选定嵌入。
换 $\mathfrak k$ 的格代表、换 $w$ 的 $p$ 次单位根，
都不改变 (9) 或 (11)。

这也付清了可能由 $\ell\mid N\alpha$、$\ell\mid(p+1)$ 引起的疑问：
本证明使用固定倍点函数和真实潜好模型，不把高次
$\psi_\alpha$、$\psi_{p+1}$ 的两个垂直常数分别忽略。
它们组合后的原根已经由 (7)–(11) 精确控制。

## 4. 固定整数倍的原 Z 和迹全整

上述模型还说明原 $x(T),y(T)$ 在每个 $\ell\ne p$ 都整。
在 $2$ 处尤其要保原平移项：
$$
y(T)=c^3Y(T)+c^3/2,
\qquad v_2(c^3/2)=0.
$$
在 $3$ 处 $r$ 为单位；其它项亦整。
故由 (4)
$$
v_\ell(\phi_m(T))\ge-v_\ell(7)\qquad(\ell\ne p).
\tag{12}
$$
结合 (11)，(5) 逐位支付
$$
v_\ell(D_m Z_{m,T})\ge0\qquad(\ell\ne p).
\tag{13}
$$

在唯一的 $p$ 位，保持 R696 的原局部值
$$
v_p(w)=-\frac1{q-1},\qquad
v_p(u_T)=\frac1{q-1}.
$$
(4) 的唯一最高极项系数为单位，故
$$
v_p(\phi_m(T))=-\frac{m-6}{q-1},\qquad
\boxed{v_p(Z_{m,T})=\frac6{q-1}>0.}
\tag{14}
$$
$D_m$ 为 $p$ 单位。因此 (13)–(14) 证明
$$
\boxed{
D_m Z_{m,T}\in\mathcal O_W,\qquad
D_m\mathcal T_{m,T}\in\mathcal O_{E_W}.
}
\tag{15}
$$
第二式是完整 $d$ 项场迹的整性，不是只在 $p$ 处的整性。

## 5. 全复环面上的固定界

R694 证明实线性准周期在本 $j=0$ 格上为
$$
\eta_z=B\bar z.
$$
还需说明 $B$ 是实数，才能把模下降到环面。
对一组周期基 $\lambda_1,\lambda_2$，Legendre 关系给
$$
B(\bar\lambda_1\lambda_2-\bar\lambda_2\lambda_1)=2\pi i
$$
（随基的定向可同时换号）。
括号为非零纯虚数，因此 $B\in\mathbf R$。
于是对所有 $z\in\mathbf C$ 和 $\lambda\in\Lambda$，
$$
\mathfrak k(z+\lambda)
=\chi(\lambda)
 e^{(\eta_\lambda z-\eta_z\lambda)/2}\mathfrak k(z),
\qquad
\left|e^{(\eta_\lambda z-\eta_z\lambda)/2}\right|=1.
\tag{16}
$$
这里是整个复平面上的模恒等，不只是挠点处的根单位关系。

所以
$$
f_m(P(z))=
|\mathfrak k(z)|^m|\phi_m(P(z))|
\tag{17}
$$
在 $E(\mathbf C)\setminus\{O\}$ 是良定的连续函数。
$\mathfrak k(z)=z(1+O(|z|^2))$，
而 $\phi_m(P(z))=z^{-(m-6)}(1+O(z))$；
故 $f_m(P(z))=|z|^6(1+o(1))$，在 $O$ 连续延伸为零。
紧性给固定的有限常数
$$
\boxed{
C_m=\max\!\left(1,\max_{P\in E(\mathbf C)}f_m(P)\right)<\infty.
}
\tag{18}
$$
它只依原固定曲线、原不变微分和 (4)，与 $p$ 无关。

## 6. 界确实覆盖全部绝对嵌入

不能只用 $\operatorname{Gal}(F/K_0)$ 而漏掉
$K_0$ 的复共轭。现令 $\iota:W\hookrightarrow\mathbf C$ 为任意嵌入。

若 $\iota|_{K_0}$ 为恒等，则 $T'=\iota(T)\in E[p]\setminus0$，
$\iota(w)^p=a_{T'}$。用原 (7) 的复归一，
$$
|\iota(w)|=|\mathfrak k(z_{T'})|^{-1}.
$$

若 $\iota$ 在 $K_0$ 上是共轭，则
$\psi_\alpha$ 变成 $\psi_{\bar\alpha}$，
且 $[\bar\alpha]T'=[\omega]T'$，范数仍为 $p^2-p+1$。
R694 的准周期推导逐式给相同的绝对值关系；
等价地，可直接将 (7) 复共轭。
原 $b=17$ 及 (4) 为实有理系数，
原 sigma 的 Taylor 系数实，
$\sigma(\bar z)=\overline{\sigma(z)}$，
周期格及其准周期在共轭下对应，$B$ 为实。
所以共轭的 Klein 模仍是 (17) 的同一个模，
不出现随 $p$ 增长的周期倍率。

因此对所有绝对嵌入都有
$$
\boxed{
|\iota(Z_{m,T})|
=|\mathfrak k(z_{T'})|^m|\phi_m(T')|
\le C_m.
}
\tag{19}
$$
任意根单位的嵌入仍有模一，包含 (7) 的全部 $\mu_{6p^2}$ 相位。

每个 $E_W$ 的复嵌入下，场迹是 $d$ 个延拓嵌入之和；
从 (19) 得
$$
\boxed{
|\iota(\mathcal T_{m,T})|\le d C_m,\qquad
|\iota(D_m\mathcal T_{m,T})|\le dD_m C_m
}
\tag{20}
$$
对所有绝对嵌入同时成立。
不要求 $W$ 或 $E_W$ 在复共轭下被逐点固定。

## 7. 对数高度及实际边界的统一上界

$h$ 为绝对对数 Weil 高度。
由 (15)、(20)，固定整数倍的迹是代数整数，且全部复共轭有上述界，
所以
$$
\boxed{
h(D_m\mathcal T_{m,T})
 \le \log\max(1,dD_m C_m)=\log d+\log(D_mC_m).
}
\tag{21}
$$
若要直接写原迹的高度，可在每个有限位使用
$D_m\mathcal T$ 整，其有限部分总和至多 $\log D_m$；
复部分由 (20) 至多 $\log(dC_m)$。因此同样准确有
$$
\boxed{
h(\mathcal T_{m,T})\le\log d+\log(D_mC_m).
}
\tag{22}
$$
(22) 不由 $h(\mathcal T)\le h(D_m\mathcal T)+\log D_m$
再删掉额外常数；这里已经单独支付有限分母与复部分。

若 $\mathcal T_{m,T}\ne0$，则
$h((D_m\mathcal T)^{-1})=h(D_m\mathcal T)$。
在 $E_W$ 唯一的 $p$ 位，其归一高度权为一；
$D_m$ 为 $p$ 单位，故由 (21)
$$
v_p(\mathcal T_{m,T})\log p
\le\log d+\log(D_m C_m).
\tag{23}
$$
无需乘 $[E_W:\mathbf Q]$。

R696(17)、(23) 对原完整边界给
$$
v_p(\mathcal T_{m,T})
=\frac1{p-1}+v_p\bigl(\mathcal B_m(v_T^d)\bigr).
$$
于是得到本篇主结论：
$$
\boxed{
\mathcal B_m(v_T^d)=0
\quad\text{或}\quad
0\le v_p\bigl(\mathcal B_m(v_T^d)\bigr)
\le
\frac{\log(p+1)+\log(D_m C_m)}{\log p}
-\frac1{p-1}.
}
\tag{24}
$$
其中 $m=34,72$，适用于每个允许的 $p$、每个非零 $T$，
全部原根和全部 $H$ 轨道都保持不变。
右端为 $1+O_m(1/\log p)$。

特别，存在只依原两个固定来源的 $p_0$，使 $p>p_0$ 时，
任一另已付的真实下界
$$
v_p\bigl(\mathcal B_m(v_T^d)\bigr)\ge2
$$
都会迫该原边界为零。这里尚未赋原中央这样的下界。

## 8. 本结论保留的算术接口

(24) 显著加强 R696 的非零边界上界，但没有证明以下任一尚开命题：

- 原完整 $j_m=0$ 对同一 $\mathcal B_m$ 给超过 (24) 的估值下界；
- 全迹 $\mathcal T_{m,T}$ 在无穷多个 $p$ 非零；
- 第一边界零已经支付 R663 的全部较高 $Q^{d-m}$ 条件。

本篇也没有把零阶挠点值的固定分母与紧环面界免费延伸到
随 $p$ 增长的高阶导数或 Hermite 插值系数。
原方程、完整中央和全高 $Q$ 条件继续保留。

## 依赖

- [R691](R691-original-unit-kummer-field-and-stabilizer-trace-criterion.md)：
  三个实际潜好模型、原全相对根及完整 cocycle。
- [R694](R694-original-cm-kummer-descent-and-full-norm-one-trace.md)：
  原 Klein 归一、准周期相位、实线性准周期和代数域包含。
- [R696](R696-original-absolute-roots-p2-field-and-linear-height-trace.md)：
  同一绝对根的共同 $W$、唯一 $p$ 位、准确场迹及原边界等式。
- [R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)：
  原 $S/T$ 的固定全多项式；(4) 保其原首项和 $b=17$ 规范。
- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：
  原 $\mathcal B_m$、完整挠点边界和高 $Q$ 条件。

本篇为全部允许素数的一般证明，没有新增数值扫描、证书或数据文件。
