# R26：真实浅头源函数的严格区间求值与端口规范

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**结论。** R22/R23使用的固定新实背景，在 $n\ge12$ 的相关域现在具有实际可执行的区间求值器。它从同一个实函数定义同时产生半径、径向导数、slope和slope导数，保留完整warp积分。当前physical node12的真实半径已包在宽度小于 $2^{-96}$ 的区间中；第11–13节又完整支付0至11层真实积分，证明真实外半径与名义二进制 `.3` 严格不同。保存的双精度值与这些实量的差均明确保留。

这是一项**已支付的源函数接口**，不是线性 ODE 的基本解、全频 Green 逆或非线性浅头匹配证明。它没有把 source fingerprint、有限 RK 加密或独立浮点 `r`/`drdx` 识别成实积分认证。

## 1. 固定的实对象和有限参数来源

使用 [R15](R15-rational-deep-tail-and-46-parameter-trace.md) 的新固定源：全部浅层参数冻结，$n\ge160$ 的源 calibration 参数为准确 $65/64$。$d_0,c_0,r_c,\epsilon_{\rm phys}$ 与全局warp系数，均按其保存 dyadic 存数定义为准确实数。有限 $R_n,\alpha_n$ 也按新ready参数表的二进制存数固定，不再重新校准。

由 [R22](R22-wide-strip-linear-head-envelope.md) 的 paid-source 账本，所有本结果需要的范围和配置已实际核销：$12\le n<160$ 的 $\alpha_n\in[1/2,2]$、$R_n\in[2,64]$、$n\ge16$ 时 $R_n=64$、零valley controls、单位warp weights、没有相关层的custom cap或flat override，且全局warp系数 $2<\alpha_{\rm w}<162$、曲率预算为8。

精确配方为

$$
\delta_n=d_0 2^{-n},\quad c_n=c_0 2^{-n/2},\quad
\mu_n=\epsilon_{\rm phys}\delta_n^{11/4}.
\tag{1.1}
$$

令

$$
\mathcal A_n=3d_0 2^{-n}
+\frac{6c_0d_0\,2^{-3(n+1)/2}}{1-2^{-3/2}}.
\tag{1.2}
$$

这是严格位于cell $n$ 以内的全部未warp源log长度之和，所以该cell的内端源半径是
$r_c\exp(\mathcal A_n/\sqrt{12})$。此前的有限 $R_n,\alpha_n$ 改变profile层值，不改变这个长度配方。

在一个长为 $\ell$、前置log长度为 $s_0$ 的segment上，记

$$
\sigma(x)=10x^3-15x^4+6x^5,
\quad
r_o(x)=r_c\exp\left(\frac{\mathcal A_n+s_0+\ell x}{\sqrt{12}}\right),
$$
$$
w(x)=\frac{\mu_n}{r_o(x)^7}\exp(\ell_0+b\sigma(x)).
\tag{1.3}
$$

转接以外取 $b=0$。五个 $p_*$ 层值为

$$1,\quad R_n/\delta_n,\quad\delta_n/\alpha_n,
\quad1/\delta_n,\quad\rho=2^{11/4}.$$

九段长为六次 $c_n\delta_n$ 和三次 $\delta_n$。所有指数、对数、根式和积分在此都是真实函数；浮点计算只是它们的一个近似求值方式。

## 2. 真实warp的准确积分分解

R22已证明在 $n\ge12$ 的所有相关profile上，$w<2^{-12}$，因此原来的slope cap不触发。对 $12\le n\le158$，又有 $\chi=1$，故真实半径的导数为

$$
\boxed{
r_x=\frac{|w_x|}{8(1+w^2)^{3/2}}
+\alpha_{\rm w}\frac{(r_o)_x}{1+w^2}.
}
\tag{2.1}
$$

本文有限计算在 $n=95$ 截断，因此没有把保护层 $n=159$ 的 $\chi$ collar错用为1；其全部贡献进入有证明的深层宽度界。

设

$$F(w)=\frac{w}{\sqrt{1+w^2}}.$$

因为 $F'(w)=(1+w^2)^{-3/2}>0$，(2.1) 的曲率部分在任意segment上的准确积分为

$$
\frac18\operatorname{TV}_{[0,1]}F(w(x)).
\tag{2.2}
$$

自由warp部分则写为

$$
B=\int_0^1\frac{(r_o)_x}{1+w^2}\,dx
=\Delta r_o-J,
\qquad
J=\int_0^1(r_o)_x\frac{w^2}{1+w^2}\,dx.
\tag{2.3}
$$

于是segment的准确实际宽度是

$$\Delta r=\tfrac18\operatorname{TV}F(w)+\alpha_{\rm w}B.$$

这个分解先把近乎等于常数的自由项抽出，再严格积分小的 $J$；它没有用两个数值积分器相差很小来估计误差。

## 3. 全部内部极值是显式根式

由 (1.3)，

$$
(\log w)_x=30b x^2(1-x)^2-7\ell/\sqrt{12}.
\tag{3.1}
$$

若 $b\le0$，则 $w$ 严格下降。若 $b>0$，令

$$
t=\sqrt{\frac{7\ell}{30\sqrt{12}b}}.
$$

当前所有正转接均严格满足 $0<t<1/4$，脚本逐段以区间比较检查。两个临界点准确为

$$
x_- =\frac{2t}{1+\sqrt{1-4t}},\qquad x_+=1-x_-.
\tag{3.2}
$$

第一个式子与 $(1-\sqrt{1-4t})/2$ 相等，数值求值避免相减抵消。将端点及这两个点按顺序插入，(2.2) 就是相邻 $F(w)$ 值之差的绝对值之和。没有采样找极值，也没有未经包络的浮点critical root。

相同公式适用于任意有理中间坐标 $x$ 的部分积分，只保留位于 $[0,x]$ 的临界点。若工作精度不能严格判断某个查询点与临界点区间的顺序，接口会要求提高精度而不猜测其顺序。

## 4. 自由warp积分的三种严格算法

### 4.1 浅层log转接

对 $12\le n\le23$ 的四个log转接，用 Arb/Acb 的严格积分计算 (2.3) 的 $J$。被积函数在复变量 $x$ 上是指数多项式除以 $1+w(x)^2$，因此是亚纯函数。若一个复球包含分母零点，普通区间除法就返回非有限球；它没有需要被忽略的log或sqrt分支切口，因为那些运算只作用在已固定的正常数上。

实际调用 `acb.integral` 的结果是包含真实积分的复球；脚本要求结果有限且虚部包含0，再取实部区间。相对和绝对tolerance只作为算法工作目标，正确性依赖返回的区间本身，不把tolerance参数当成已达到的误差声明。

为了使极小的部分segment也可求值，实际实现先抽出正因子 $\ell r_o(0)w(0)^2/\sqrt{12}$，把积分中的函数归一到左端约为1，再乘回。这个准确恒等变换避免绝对tolerance把一个极小正材料积分的区间放宽到包含0；它不改变任何实源参数。

### 4.2 常层平台与端口

在 $b=0$ 的segment上，$w=w_0(r_o/r_{o,0})^{-7}$。令 $q=\ell/\sqrt{12}$，则

$$
J_k=\int(r_o)_xw^{2k}dx
=w_0^{2k}r_{o,0}
\frac{1-e^{-(14k-1)q}}{14k-1}.
\tag{4.1}
$$

由准确几何恒等式

$$\frac{w^2}{1+w^2}=w^2-w^4+w^6-\frac{w^8}{1+w^2},$$

得

$$
J_1-J_2+J_3-w_0^8\Delta r_o
\le J\le J_1-J_2+J_3.
\tag{4.2}
$$

其中 $w$ 随 $r_o$ 下降，所以 $w_0$ 确是全段最大值。计算使用 `expm1` 形成 (4.1) 的小差量；严格余项的符号和大小都保留。

### 4.3 较深的有限cell

对 $24\le n\le95$，无须昂贵精积分。R22的 $W_n=2^{21}\delta_n^{7/4}$ 是全段slope上界，直接有

$$0\le J\le W_n^2\Delta r_o.\tag{4.3}$$

曲率部分仍使用准确的极值公式 (2.2)–(3.2)；仅对已经十分小的自由warp修正使用 (4.3)。这给出有方向的实区间，而不是将它置零。

## 5. 无穷深处及保护collar的剩余半径

令有限计算起点为physical node $N=96$。从 $r_c$ 到该节点的全部真实半径增量，由R22的实际宽度界直接满足

$$
0\le r(N)-r_c\le T_N,
$$
$$
\boxed{
T_N=r_c\left(326\delta_N+
\frac{11\,2^{21}\delta_N^{7/4}}{1-2^{-7/4}}\right).
}
\tag{5.1}
$$

这个尾和包含 $96\le n<160$ 的warp层、$n=159$ 的真实collar及全部未warp有理深源，不存在未计的有限截断误差。

以区间 $r_c+[0,T_{96}]$ 为起点，依次加cell95到cell12的准确宽度区间，即得physical node12。每一段都满足 $r_x>0$，因此不需要推断径向顺序。

本次实际算得

$$T_{96}\approx1.234409544489839025278082\times10^{-30}<2^{-99}.$$

所有区间误差——包括(4.2)、(4.3)、(5.1)和Arb舍入——都包含在最终半径球里。

## 6. 可执行的整panel系数接口

代码实现于
`computations/closure_real_head_source_enclosure.py`。
其 `RealHead.physical_point(n,j,x)` 对有理 $x$ 计算同一实源的

$$r,\ r_x,\ \log w,\ (\log w)_x,\ w,\ w_r,\ E,\ E_r,$$

其中

$$w_r=\frac{w(\log w)_x}{r_x},\qquad E=1+w^2,\qquad E_r=2ww_r.$$

半径来自 (2.2)–(2.3) 的部分实积分，导数来自同一个被积函数 (2.1)。所以它们已经是一个共同函数及其导数，而不是独立数值字段的事后拼接。

`physical_interval(n,j,a,b)` 包含整个有理闭panel的值：半径利用严格单调性，取两端实积分区间的包络；其余表达式对整个 $x\in[a,b]$ 作Arb区间求值。若区间过宽以致不能证明分母正性，接口会要求细分。保存包已有cell12四个转接的整panel例子，范围为 $[127/256,129/256]$，并非中点采样。

对偶物理频率 $m\ge2$，定义

$$\nu_m=m^2(m^2-1)/12.$$

同一个接口返回 physical canonical 线性系统的严格系数矩阵

$$
\frac{d}{dx}\binom Q\Xi
=\begin{pmatrix}d&a\\b&-d\end{pmatrix}\binom Q\Xi,
$$
$$
d=(m^2-4)\frac{r_x}{r},\qquad
a=\frac{\sqrt{12}\mu_n r_x}{r^8w},\qquad
b=-\frac{\nu_m\sqrt{12}r_xr^6w}{\mu_n}.
\tag{6.1}
$$

这些式子由真实线性Darboux方程
$(wC_m')'-m^2(w'/r)C_m=0$
和R23的canonical定义直接相减得到，对任意实际warp成立。选择balanced坐标 $(Q,\Xi/\nu_m)$ 时，将矩阵右上乘 $\nu_m$、左下除 $\nu_m$ 即可。

`linear_generator_interval` 返回的是 (6.1) 在整panel上的包含区间。它尚未求解矩阵ODE，也没有把一个系数矩阵区间当成基本解矩阵区间。

## 7. 当前真实端口与保存数的差

本次使用python-flint 0.9.0、192bit中点精度。所有输入float先转成精确有理数，再进入Arb；每个输出区间使用 `lower()/upper()` 的向外端点，并以准确整数mantissa乘 $2^{\text{exponent}}$ 保存。十进制display只供阅读。

完整数据保存在
`notes/2026-11-12-closure-real-head-source-enclosure.json`。
它同时记录ready、paid-source账本、实际非线性响应包和运行入口的SHA256。

physical node12的真实量为：

| 量 | 实值区间的十进制显示 |
| --- | --- |
| $r$ | $0.05002889966825685830298558258\ \pm6.08\times10^{-30}$ |
| $r_o$ | $0.05000012701266443146081066998169654\ldots$ |
| $w$ | $1.0072314093684093779549198695506700\ldots\times10^{-11}$ |
| $w_r$ | $-8.7434568021514911170589241700130\ldots\times10^{-12}$ |
| $E-1$ | $1.014515112018272274828420427\ldots\times10^{-22}$ |
| $E_r$ | $-1.7613368635165704221885175717551\ldots\times10^{-22}$ |

最终半径的完整区间宽度约为 $1.1175077387667045\times10^{-29}$，脚本以区间不等式检查它严格小于 $2^{-96}$；不是把表格的四舍五入显示当作证书。

与depth12实际响应中保存的double比较，得到以下**保存值减真实源值**的明确区间中心：

$$
\Delta r\approx+2.94097896799\times10^{-18},\qquad
\Delta w\approx-3.81327582435782549\times10^{-28},
$$
$$\Delta\mu_{11}\approx-7.46030119327316922\times10^{-37}.$$

每一个差都有包内的准确向外dyadic端点；它们不是“接近所以相等”的判断。特别地，实源的 $E=1+w^2$ 与浮点加法舍入到1具有不同算术意义；后续完整mean或Darboux误差必须沿用对应对象。

## 8. 跨cell的canonical端口规范

physical node $k$ 是cell $k-1$ 的内端，也是cell $k$ 的外端。worker最后的canonical转换使用 $\mu_{k-1}$；R23在cell $k$ 内使用 $\mu_k$。同一物理高度及其导数下，

$$
Q^{(k)}=Q^{(k-1)},\qquad
\boxed{\Xi^{(k)}=\frac{\mu_{k-1}}{\mu_k}\Xi^{(k-1)}
=2^{11/4}\Xi^{(k-1)}.}
\tag{8.1}
$$

本次node12的实际响应保存的是 $\mu_{11}$ 规范，故接入cell12的R23范数前必须乘此因子。该规范转换与非线性connection $\Pi$ 到canonical $\Xi$ 的转换是两件不同的事，均须保留。

node12端口本身不在保护collar；此时 $w=\mu_{11}/r_o^7$，且

$$
\frac{dr}{dr_o}=\frac{\alpha_{\rm w}}{1+w^2}
+\frac{7w}{8r_o(1+w^2)^{3/2}},
\qquad
w_r=\frac{-7w/r_o}{dr/dr_o}.
\tag{8.2}
$$

这解释了表中的准确 $w_r$ 来源，也给出一个不依赖额外径向差分的端口两jet接口。

## 9. 可复现命令与完成边界

```sh
python computations/closure_real_head_source_enclosure.py \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --source-ledger notes/2026-11-12-closure-wide-strip-head-ledger-paid-source.json \
  --response notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-response.json.gz \
  --out notes/2026-11-12-closure-real-head-source-enclosure.json
```

包含四个整panel例子的实际运行只用约30MiB内存，64次严格积分；所有正性和最终宽度门通过。若区间求积未给有限包络、极值分支不能严格判定或分母不能证明为正，脚本会失败，不产出成功声明。

本文已把原先独立欠缺的真实源积分、源导数一致性和端口规范做成可计算接口。它仍须与线性/线性化流误差、R23的全胞元非线性范数、全频Green估计及R18的真实低46匹配结合。有限q003端点仍不是最终全频浅trace，高频cut高度仍须作为输出交给前缀联解。

## 10. 真正outer cut不是一次隐含的重新归一

冻结二进制 $\alpha_{\rm w}$ 后，完整实背景的外cut半径定义为

$$
\boxed{R_{\rm out}=r_c+\sum_{n\ge0}\int_{\mathrm{cell}\ n}r_x\,dx.}
\tag{10.1}
$$

初次版本已包络其中 $n\ge12$ 的整个部分；第11–13节补齐 $0\le n\le11$ 的cap、非零valley control及正warp weights完整积分。**真实 $R_{\rm out}$ 严格不等于名义存数 `rCut=.3`**，也不能自动识别为旧响应的浮点cut半径。

为了把算术对象完全说明：源factory已捕获的辅助常数 `oldCut` 也按其二进制存数冻结。外collar使用的准确函数是
$j_0(x)=1+(r_{\rm cut,bin}/r_{\rm old,bin}-1)\sigma(x)$。
不能把分母静默换成重新求出的真实未warp外半径，正如不能把冻结 $\alpha_{\rm w}$ 静默换成使 (10.1) 恰等于 `.3` 的新implicit根。二者都会另定义一个背景。

真实外端的slope及其一阶导数还可以独立于 (10.1) 精确求值。令

$$
L_{\rm all}=6d_0+\frac{6c_0d_0}{1-2^{-3/2}},\qquad
r_{o,\rm out}=r_c e^{L_{\rm all}/\sqrt{12}},
$$
$$
j_{0,\rm out}=r_{\rm cut,bin}/r_{\rm old,bin},\qquad
w_{\rm out}=\epsilon_{\rm phys}(2d_0)^{11/4}/r_{o,\rm out}^7.
$$

cut-preserving模式在最外端恰取raw源，且 $\chi=0$，从同一真实函数可得

$$
(w_r)_{\rm out}=-\frac{7w_{\rm out}}{r_{o,\rm out}j_{0,\rm out}},
\qquad E_{\rm out}=1+w_{\rm out}^2,
\qquad (E_r)_{\rm out}=2w_{\rm out}(w_r)_{\rm out}.
\tag{10.2}
$$

代码和JSON包的 `outer_cut` 已保存这些完整实标量及它们与实际响应中背景slope、second、E、Ep的差区间。该历史包将真实 $R_{\rm out}$ 标为当时未完成，不回写历史输出；新的完整外半径见第13节独立证书。

最终前缀的径向metric与port两jet必须接到 (10.1)–(10.2) 这个同一实对象。当前前缀数值链若仍使用原存数cut，须保留并说明这段差；本文没有改动该链，也没有重新校准全局warp。

## 11. 完整外层cap、控制和权重

2026-11-12，root 补充。以下完整证明及 v4 程序在执行器切换后重新保存，数值证书已在新环境真实重算，不以失去访问的旧输出代替。

`computations/closure_real_outer_radius.py` 沿用同一 `RealHead` 和冻结输入；只接受当前实际配置：orientation $+1$、cut-preserving、cap transition $L=2$、曲率预算8、无flatten/rejoin。每个cell保留准确dyadic $R_n,\alpha_n,\beta_n$、正warp层权重，以及捕获的 `oldCut` 和全局 $\alpha_{\rm w}$，不重新校准。

在第1节原始对数profile上，准确地取

$$
g_0=\log\mu_n+\ell_0+b\sigma(x)-7\log r_o(x)+\beta_n v_j(x),
$$
$$
v_3=\sigma,\qquad v_4=1,\qquad v_5=1-\sigma,
\qquad v_j=0\ (j\notin\{3,4,5\}).
\tag{11.1}
$$

五个正cap层值依次为基本cap、左pulse cap、valley cap、右pulse cap、基本cap；偶数段取对应常数，奇数段用 $\sigma$ 在相邻对数层值间转接，得到 $c(x)$。令

$$
\mathcal S(t)=35t^4-84t^5+70t^6-20t^7,\qquad
J(t)=7t^5-14t^6+10t^7-\tfrac52t^8.
$$

有 $J'=\mathcal S$、$\mathcal S(1-t)=1-\mathcal S(t)$。cap的准确公式是

$$
g_c=\begin{cases}
g_0,&g_0-c\le-L,\\
c,&g_0-c\ge L,\\
g_0-2LJ(t),&-L\le g_0-c\le0,\quad t=(g_0-c+L)/(2L),\\
c-2LJ(u),&0\le g_0-c\le L,\quad u=(c+L-g_0)/(2L).
\end{cases}
\tag{11.2}
$$

这四式在交接处一致，是保存factory公式的多项式恒等变换。中间两式的完整导数为

$$
(g_c)_x=(g_0)_x-\mathcal S(t)((g_0)_x-c_x),\qquad
(g_c)_x=c_x+\mathcal S(u)((g_0)_x-c_x).
\tag{11.3}
$$

因此靠近常cap平台时无需计算两个近于1的量之差。相等dyadic层值的log跳跃准确为0；不把同一对数的两个区间球相减制造虚假导数宽度。不同层值直接用准确比值的log。权重转接也沿用这条规则。

在最外cell第8段取 $g=g_0$，第7段保留cut-preserving混合

$$g=g_0+(1-\sigma)(g_c-g_0),\tag{11.4}$$

并使用完整乘积导数；其它段取 $g=g_c$。五个正自由warp层权重记为 $W_0,\ldots,W_4$，偶数段常值，奇数段

$$W(x)=W_k\exp\bigl(\log(W_{k+1}/W_k)\sigma(x)\bigr).$$

除了最外cell第8段以外，$\chi=j_0=1$；该最外段则保留

$$
\chi=1-\sigma,\qquad
j_0=1+(r_{\rm cut,bin}/r_{\rm old,bin}-1)\sigma.
$$

于是所有12个外层cell的同一实径向导数为

$$
\boxed{
r_x=(r_o)_xj_0(1-\chi)
+\frac{\chi e^g|g_x|}{8(1+e^{2g})^{3/2}}
+\alpha_{\rm w}\frac{\chi(r_o)_xW}{1+e^{2g}}.
}
\tag{11.5}
$$

这是原weighted factory的准确实关系：$W$ 只乘自由warp项，不能错乘曲率项或外端基础项。$(r_o)_x,j_0,W,\alpha_{\rm w}>0$ 且 $0\le\chi\le1$，所以 $r_x>0$。各段半径由此式积分，源值与源导数属于同一个函数。

## 12. 分支、临界点与完整剩余积分

每个 $[0,1]$ 源段被完全覆盖的相邻dyadic闭panel划分。若整panel上 (11.2) 的分支以及最终 $g_x$ 的正、负或准确零都可严格判断，(11.5) 在该实panel上等于去掉绝对值后的一个解析表达式。

对该表达式调用 `acb.integral`。复球平方根使用积分器传入的 `analytic` 标志；若不能认证该复球上的解析分支，求值返回非有限球，不能作为成功积分接受。所有原double先转准确有理数；固定常数上的根、log和exp都由Arb包络。积分前提取一个严格正的缩放因子，最终乘回整个返回球，避免极小物理量被绝对工作容差吞没。工作tolerance不是误差结论，返回的包含球才是证书。

若分支或导数符号尚不明确，程序不丢弃该panel。将所有可能真实出现的分支代入整个panel的自然区间求值，保留 $|g_x|$，取其值域包络 $I$；准确长度为 $h$ 时，真实积分属于 $hI$。虽然某一候选分支公式在panel的其它部分可能不是实际公式，但其真正使用的子集仍包含在全panel求值中，所以并集包络有效。

此类panel继续二分，直到宽度不超过 $2^{-100}$，或者完整积分包络的宽度已经不超过 $2^{-100}$，然后把完整包络加进总和。后者适用于近乎平坦的平台；它不要求导数离零有距离，也未把临界点附近贡献置零。每个源段设30000次panel访问预算；耗尽则退出，不能产生完整半径成功声明。

成功运行覆盖108个源段和304个最终panel：204个解析严格积分、100个完整区间剩余界。源段端点严格相接覆盖 $[0,1]$。将12个cell宽度加到第7节node12严格半径，即为 (10.1)；所有 $n\ge96$ 无穷剩余仍由 (5.1) 包含。

## 13. 真实重算证书与闭式积分核对

新的完整输出为
`notes/2026-11-12-root-real-outer-radius-v4-recovered-full.json`。
执行会话39503已正式返回 `exit 0`：192bit，5.420717389秒，峰31256KiB。重建程序的SHA256与失联前已成功运行的版本逐字相同：
`bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe`。
输出记录ready、程序及原 `RealHead` 的SHA256，不把旧成功摘要冒充新数组。

全部准确向外dyadic端点的十进制显示为

$$
\boxed{R_{\rm out}=0.30000000000000715908123386
\ \pm6.70\times10^{-27}.}
\tag{13.1}
$$

减去准确的**二进制double** `.3` 后，另存的差区间为

$$
\boxed{R_{\rm out}-r_{\rm cut,bin}
=7.1701834641\times10^{-15}\ \pm9.97\times10^{-27}>0.}
\tag{13.2}
$$

十进制显示有各自的舍入位数；准确结论使用JSON中整数mantissa乘二的整数次幂端点。十进制有理数 $3/10$ 与二进制double `.3` 本身不同，(13.2) 比较的是后者。

`computations/root_real_outer_radius_check.py` 另用准确分数核对全部源hash、108段和304panel覆盖、外半径包含逐cell区间之和及差的严格正性，并与已推送的独立cell0、cell11结果比较，两组区间均相交。旧中断运行的未推文件已失去访问，因此新核对没有假借该文件。

还有不使用求积的解析核对。cell0第2段整个区间严格属于常cap分支，$w=C=\text{binary}(.4)$、$W=\text{binary}(.5)$、$\chi=1$、$g_x=0$。从 (11.5) 直接积分得到

$$
\Delta r_{0,2}=\frac{\alpha_{\rm w}W}{1+C^2}\,
 r_o(0)\operatorname{expm1}(\ell/\sqrt{12}).
\tag{13.3}
$$

该式的严格区间是

$$
0.0060596443902404577860370369230963374156574446778943572958
\ \pm3.61\times10^{-59},
$$

与保存的整段积分相容，包含关系及所有核对保存在
`notes/2026-11-12-root-real-outer-radius-v4-recovered-check.json`。
该核对也已正式 `exit 0`。因此平台处理并非通过宽泛容差掩盖分支或权重错误。

复现命令（输出须用新文件名保全已有结果）：

```sh
python computations/closure_real_outer_radius.py \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --out notes/root-real-outer-radius-fresh.json
python computations/root_real_outer_radius_check.py \
  --full notes/root-real-outer-radius-fresh.json \
  --previous notes/2026-11-12-root-real-outer-radius-cell0.json \
    notes/2026-11-12-root-real-outer-radius-cell11.json \
  --out notes/root-real-outer-radius-fresh-check.json
```

这补齐R26的真实外半径缺口。新实背景前缀必须接到 (13.1) 与 (10.2) 的共同对象；旧stored-g BVP仍保留原度量，不能因 (13.2) 小就把两者等同。全频非线性尾、浅头匹配、强幅闭面及全部reach/位移门继续按原标准核销。
