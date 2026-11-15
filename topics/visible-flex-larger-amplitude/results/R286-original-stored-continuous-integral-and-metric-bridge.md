# R286：原冻结数据的连续实积分提升、cusp 消去与同场 metric 包络桥

2026-11-15，geometry，GPT-6 Astra Pro，AI-assisted。

**状态：已证明的连续模型与误差接口结论；源码只读，未执行科学计算。** 本文不把旧有限 selector、旧 stored 响应或某个已保存 BVP 改称连续背景的认证解，也不宣布当前已产生原连续 $g$ 的数值包络或已接受完整闭场。

本文完成三项具体责任：明确哪些数据已由旧 ready 固定、哪些实函数解释仍是模型约定；证明原正径向 warp 在 $|w_s|$ cusp 处仍给一致的连续二阶 metric；给出从完整原表达直接产生 $E_*(r)$ 包络以及比较原有限求值器的可计算路径。直接包围 $E_*$ 可以供同场有限 $F$ 的 R251 比较使用，不必先穷举 R285 的非平坦48层选择树。

## 286.1 原定义的证据和不能混同的三个对象

原 closed 题 [R15](../../visible-flexible-closed-surface/results/R15-weighted-inner-background-and-collar-bounds.md) §1 明确采用固定正 warp 系数与真实积分构造径向坐标，同时说明浮点 quadrature 偏差仍须另外控制。该文的固定数值曲率结论有自己的参数范围，不能移植到本题另一组参数。

原 large-amplitude 题 R28，Git blob cf9881e3ae2c2797a61213ab099dbec239be5f0d，明确把深层准确校准定义为真实线性 ODE 的根，证明根存在于 $[1/2,2]$；它不证明唯一性，并允许按一个固定规则选择该区间中的根。原程序的有限 RK/Newton 校准被该证明明确称为准确定义根的近似。

本题 [R26](R26-real-head-source-interval-and-port-coordinates.md) 则另行选择从 $n=160$ 起准确等于 $65/64$ 的新深背景。其真实积分工具与有限头表达可以在严格相同的数据范围内复用，但其无限对象、现成数值证书和 new metric 身份不能被换标签给原校准根背景。

因此必须区分：

1. 原已固定 binary 参数和原数值求值器；
2. 采用明确实函数解释后得到的连续模型；
3. 当前有限场是否已经对该同一个连续模型满足原 metric、接缝及全部完成标准。

[R285](R285-original-finite-selector-closed-cover.md) 只支付第1项中有限 selector 的闭区间覆盖。本文支付第2项的明确构造与接线定理。第3项必须仍由真实同场输入及实际包络结论承担。

### 286.1.1 本文实际读取的来源

| 原件 | SHA256 |
|---|---|
| tail_frozen_geometry.mjs | db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3 |
| strong_frozen_calibration_factory.mjs | 77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247 |
| closure_bounded_point_cache.mjs | 35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043 |
| closing_weighted_tail.mjs | 740e672edee58cff7a15f89d75e181577dd439c1c62777c57d0d0ab1af32141e |
| closing_recalibrated_tail.mjs | 4a109f26b0e6c9741dfff678c0fe42da4935bfda9c605e55688e97848aef0dd6 |
| tailnext_balanced_tail.mjs | 928567418f411b70c4040be9ee08be2a78b65e147b8d0c5728f4cf6766a28888 |
| general_root_smooth_tail_cells.cjs | d074799099e27401456449343c8f490ec60cdec7eb0d02758f024f541d409575 |
| f6tail_cusp_grid.mjs | b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f |
| 原 closed R15 | 268da9dd07a1009825a62636c039f6f4c847eca6b723959eb75822530cd5904a |
| 原 large-amplitude R28 | ff37c93014ddae437add50e6bed7c495df099ce3a6883fd0a14e6666163b2163 |
| closure_real_head_source_enclosure.py | 97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47 |
| closure_real_outer_radius.py | bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe |

原 JS 和 R26 工具均只读，未改写、导入或执行。原 public source 固定参考为 ce9807e19bb2ea638987e18c6ba5402bf4adc595；相邻大幅题的三个小依赖由原 loader 清单所列 Git blobs 读取。原 R28 由上述确切 blob 从原仓库读取，不由标题推定内容。

## 286.2 唯一已固定的数据与额外实模型约定

旧 ready 唯一固定了160行校准存数、保存的 global warp alpha、完整 physicalParameters、有限 controls/caps/weights、source revision/hash和历史指纹。它还固定实际数值算法和原运行的有限输出。单凭这些字节，不会自动指定“每一个程序中间量都应当作独立准确实常数”，也不会自动指定一个准确无限深根的唯一选择规则。

以下给出一个与原设计公式一致、但须明确登记的连续解释，记为约定 $\mathcal C$。这是一个明确的模型层补充，不是宣称旧 ready 已独自选定该解释。

### 286.2.1 冻结量

将原保存的下列数按其准确 binary64 dyadic 值保留：

- $d_0,c_0,r_c,\epsilon_{\mathrm{phys}}$；
- 全局正 warp 系数 $\lambda$；
- 原曲率再分配参数 $K>0$；
- 名义 $r_{\mathrm{cut,bin}}$ 与工厂捕获的 $r_{\mathrm{old,bin}}$；
- 浅160层的 $R_n,\alpha_n$；
- 所有有限 valley controls、cap层值、cap transition、flat参数和正warp层权；
- 原 orientation、protect index、prefix和rejoin选择。

本文当前构造采用 stored loader 实际支持的 orientation $+1$、protect index160、无 rejoin，以及 $a=11/4$、$\mathrm{etaPower}=3/2$。不是把不符这些条件的另一输入悄悄转换过来。

$\epsilon_{\mathrm{phys}}$ 和 $r_{\mathrm{old,bin}}$ 不从另一套实运算重新求值。尤其不重新选择 $\lambda$ 来强制真实 cut 等于名义 cut。浅层 $\alpha_n$ 也是保留原 binary 常数，不重新求一个更“准确”的校准根。

### 286.2.2 关系式的实解释

在约定 $\mathcal C$ 中定义

$$
\delta_n=d_0\,2^{-n},\qquad
c_n=c_0\,2^{-n/2},\qquad
\eta_n=c_n\delta_n,\qquad
\mu_n=\epsilon_{\mathrm{phys}}\delta_n^{11/4}.
\tag{286.1}
$$

指数、对数、根式、微分和积分在这里指实函数。原表中由浮点派生的 $\delta,c,\mu,r_o$ 等仍完整保存为比较对象，不被重写；不能同时将所有独立舍入的派生量当作准确常数，又无证明地使用它们原本只在实公式下成立的端口恒等式。

这个取舍是模型语义的一部分。它保留上述冻结输入，不宣称每个原浮点中间值都与本次实值相等。若选择另一种“所有派生词也独立冻结”的对象，必须另检其拼接；那种对象不自动继承下文的连续性。

对 $n\ge160$，保留原深源的准确校准根类别：$\alpha_n$ 是原 mode2准确胞元传递下左元为零的根，且 $\alpha_n\in[1/2,2]$。不将它设成 R26 的 $65/64$。

如果旧模型尚未固定选根规则，则约定 $\mathcal C$ 在此首先定义一个背景族。下面除明确的单个根数值求值外，所有结论对族内每一种固定选择同时成立。要把它变成唯一的 $g_*$，须再固定一个原允许的根选择规则；这是一项模型层声明，不是对旧 finite output 的新证明。第286.8节给出可计算的固定选择方式。

## 286.3 同一 raw profile 的实表达和端口

原未改 source 的每个胞元有九段：两个port、四个transition和三个plateau。六个短段长 $\eta_n$，三个plateau长 $\delta_n$。当前这条原factory调用的 lengthScale 为1；实际输入还须保原table该列的相同身份。有限 $R_n,\alpha_n$ 改变层值，不改变这些长度。其它 lengthScale 配方不在本文这个声明中悄悄归一为1。

记整个 source 从 cuff 向外的单调log-length坐标为 $s$。胞元 $n$ 内端前的准确总长是

$$
\mathcal A_n
 =3d_0\,2^{-n}
 +\frac{6c_0d_0\,2^{-3(n+1)/2}}{1-2^{-3/2}}.
\tag{286.2}
$$

一段长为 $\ell$、前置长度为 $s_0$ 时，$s=\mathcal A_n+s_0+\ell x$，$0\le x\le1$，并取

$$
r_o(s)=r_c e^{s/\sqrt{12}},\qquad
P_n=(1,\ R_n/\delta_n,\ \delta_n/\alpha_n,\ 1/\delta_n,\ 2^{11/4}).
\tag{286.3}
$$

相邻层值间用原quintic

$$
S(x)=10x^3-15x^4+6x^5
\tag{286.4}
$$

作对数插值；平台和port取常值。于是

$$
w_{\mathrm{raw}}(s)=
\mu_n\,P_n(x)\,r_o(s)^{-7}.
\tag{286.5}
$$

这与原 source 的 log-mu、log层值减log-delta及负7倍log-radius表达是相同实公式，只将原五个层值除以 $\delta_n$ 后写成 $P_n$。

$S'(0)=S'(1)=S''(0)=S''(1)=0$。胞元间又有

$$
\mu_{n+1}\,2^{11/4}=\mu_n,
\qquad
\mathcal A_{n+1}+\delta_{n+1}(3+6c_{n+1})=\mathcal A_n.
\tag{286.6}
$$

因此未改 raw profile 的值及前两阶 $s$ 导数在所有有限port相接。这个论证使用约定 $\mathcal C$ 的实关系，不使用“浮点端口看起来相同”。

浅层 calibration 数是否正好满足准确ODE校准不参与这里的几何拼接证明：只需它是固定正数。准确校准和非线性尾存在性是另一个责任。

## 286.4 完整 cap、valley、flat、cut-preserving 和 weights

在raw对数上先按原源加入 valley control：

$$
\log w_{\mathrm{raw}}+\beta_n v_j(x),\qquad
v_3=S,\quad v_4=1,\quad v_5=1-S,
\tag{286.7}
$$

其余 $v_j=0$。五个正cap层值与五个正warp权重均按原索引读取；偶数段取对应常值，奇数段按 $S$ 作对数插值。权重两个port层值仍等于1。

设待cap的log值为 $z$，局部cap的log值为 $c$，transition宽度为 $L>0$。原cap可准确写成

$$
C(z,c)=
\begin{cases}
z,&z-c\le-L,\\
z-2LJ\!\left(\frac{z-c+L}{2L}\right),
 &-L\le z-c\le0,\\
c-2LJ\!\left(\frac{c+L-z}{2L}\right),
 &0\le z-c\le L,\\
c,&z-c\ge L,
\end{cases}
\tag{286.8}
$$

其中

$$
J(t)=7t^5-14t^6+10t^7-\frac52t^8,\qquad
J'(t)=35t^4-84t^5+70t^6-20t^7.
\tag{286.9}
$$

四支在闭端点的值及所需导数相同。若未启用正cap，就保原raw分支，不能取非正cap的对数。

flat规则完整保持：满足原层/段条件的地方直接令log slope等于固定 $\log(\mathrm{flatSlope})$；唯一过渡段用原 $S$ 混合。随后仍按原顺序覆盖cut-preserving最后一段的raw值，并在倒数第二段用 $1-S$ 混合。不得因为先前进入flat分支，就漏掉这两个后续覆盖。

记全部操作后的slope为 $w(s)>0$。这些是有限个平滑实复合，因而在每个有限闭piece及其所有cap/flat边界上 $w$ 为 $C^2$；常cap区间的 $w_s$ 可整段为零。相邻piece的二阶端点匹配由原 $S$ 的二阶平端及相邻层值相同给出。

原权重记为 $\omega(s)>0$。原 $\chi$ 和 $j_0$ 保留：

- 普通piece上 $\chi=j_0=1$；
- 最深保护port上 $\chi=S(x),j_0=1$；
- 最外cutport上 $\chi=1-S(x)$，
  $j_0=1+(r_{\mathrm{cut,bin}}/r_{\mathrm{old,bin}}-1)S(x)$。

它们同样在有限joins有匹配的所需导数。全段有 $0\le\chi\le1$、$j_0>0$，后一正性来自两个正端值的凸组合。


## 286.5 六个共同 primitive 与严格正的真实径向坐标

以下导数先对统一的 $s$ 坐标取。令

$$
q=w_s,\qquad E_s=1+w^2,\qquad v=(r_o)_s=r_o/\sqrt{12}>0,
$$
$$
A=(1-\chi)j_0v+\frac{\chi|q|}{K E_s^{3/2}},
\qquad
B=\frac{\chi\omega v}{E_s}.
\tag{286.10}
$$

原weighted源码只将 $B,\sqrt{E_s}B,wB$ 乘正权 $\omega$，不改 $A$ 的曲率项和缓冲项。六个真实被积函数恰为

$$
(A,\ B,\ \sqrt{E_s}A,\ \sqrt{E_s}B,\ wA,\ wB).
\tag{286.11}
$$

在原每段 $x$ 坐标下，$ds=\ell\,dx$，所有六项同时乘 $\ell$。不能只对半径项换变量，而把长度、height的另外四项留在另一种定义中。

记 $s_{160}=\mathcal A_{159}$。在原深源保持未warp的 $0<s\le s_{160}$ 上，令 $R_*(s)=r_o(s)$。在有限头上定义

$$
R_*(s)
 =r_o(s_{160})+\int_{s_{160}}^sD(u)\,du,
\qquad D=A+\lambda B.
\tag{286.12}
$$

于是

$$
D=b+c|q|,\qquad
b=v\left((1-\chi)j_0+\frac{\lambda\chi\omega}{E_s}\right)>0,
\qquad c=\frac{\chi}{K E_s^{3/2}}\ge0.
\tag{286.13}
$$

正性来自 $j_0>0,\lambda>0,\omega>0,E_s>0$ 以及 $0\le\chi\le1$，不来自浮点profile的正drdx断言。在任何固定有限闭段，有可计算的正下界，例如

$$
D\ge b\ge v_{\min}
 \min\left((j_0)_{\min},
            \frac{\lambda\omega_{\min}}{(E_s)_{\max}}\right)>0.
\tag{286.14}
$$

因此 $R_*$ 连续严格递增、是 $C^1$ 的，且在每个有限开邻域有 $C^1$ 反函数。原point.r的adaptive表达不参与此证明。

所有有限piece的起点必须由同一真实累计积分确定。不能每到新piece就把真实累计值重设成原浮点rStart；后者会另定义一个可能有跳跃的对象。真实meridian length和height分别由同一六primitive给出

$$
L(s)-L(s_{160})=\int_{s_{160}}^s\sqrt{E_s}\,D\,du,
\qquad
H(s)-H(s_{160})=\int_{s_{160}}^swD\,du.
\tag{286.15}
$$

在 $r=R_*(s)$ 坐标下，$H_r=w$。这才是“slope”和原积分primitive属于一个共同函数的理由。

## 286.6 cusp 消去：不要求辅助半径自身二阶光滑

**定理286.1。** 设一个有限开区间上 $w\in C^2$，$b,c\in C^1$，$b>0,c\ge0$。令 $q=w_s$、$D=b+c|q|$、$R_s=D$。则真实径向slope

$$
w_*(r)=w(R^{-1}(r))
$$

属于 $C^2$，并且在包括 $q=0$ 的所有点上有

$$
\boxed{\ (w_*)_r=\frac qD,\qquad
(w_*)_{rr}=\frac{bq_s-qb_s-qc_s|q|}{D^3}.\ }
\tag{286.16}
$$

**证明。** $D$ 连续严格正，故 $R^{-1}$ 是 $C^1$。对 $b>0,c\ge0$ 定义

$$
\mathcal H(q,b,c)=\frac q{b+c|q|}.
$$

当 $q\ne0$ 时直接微分；当 $q=0$ 时用左右差商。三偏导统一为

$$
\mathcal H_q=\frac b{(b+c|q|)^2},\qquad
\mathcal H_b=-\frac q{(b+c|q|)^2},\qquad
\mathcal H_c=-\frac{q|q|}{(b+c|q|)^2}.
\tag{286.17}
$$

这些式子在 $q=0$ 处连续，因此 $\mathcal H$ 为 $C^1$。于是

$$
\frac d{ds}\left(\frac qD\right)
 =\frac{bq_s-qb_s-qc_s|q|}{D^2},
$$

再除以 $R_s=D$ 得(286.16)。$\square$

此证明既不假设零点孤立，也不假设过零为simple root。因此整段常cap、非横截cusp、多个临界点聚集以及piece端点上的零导数都不需要另选符号。直接对 $|q|$ 作两次微分会人为引入不存在的障碍；真正的径向导数是 $q/D$，它在零点消除了符号项。

对(286.13)，$w\in C^2$ 意味 $E_s\in C^2$；原 $\chi,j_0,\omega,v$ 有所需的匹配光滑性，所以 $b,c\in C^1$。可直接使用定理286.1。连续metric系数满足

$$
E_*(r)=1+w_*(r)^2,
\quad
(E_*)_r=2w_*(w_*)_r,
\quad
(E_*)_{rr}=2\bigl((w_*)_r^2+w_*(w_*)_{rr}\bigr).
\tag{286.18}
$$

因此有限头上的 $E_*$ 是 $C^2$。并未声称 $R(s)$ 在 $q$ 的每个simple zero处是 $C^2$；它可能只有 $C^1$。也没有把原point返回的独立drdx字段当作该连续原语的导数。

## 286.7 有限拼接、保护端和外cut的准确责任

### 286.7.1 有限头内部

对(286.4)的原quintic，每个相邻segment的cap层值、weight层值及raw端口值由同一源表相接；valley与flat过渡的前两阶端点项消失。$w,q,q_s,b,c,b_s,c_s$ 在有限join上相接时，(286.16)直接给径向两jet的相接。

这是一条实际表达式的结论，不是凭profile标签相同而推断。若输入扩展允许不同cap端值、不同weight端值或任意非法flat索引，则须对扩展后的实际表达重新核端点，不能引用当前源码已限制的port权重等于1。

### 286.7.2 内保护端

$\chi(0)=\chi_s(0)=0$、$j_0=1$ 保证径向再分配在内端退回raw速度。它**本身不保证被cap或flat修改的slope退回raw slope**。完整接缝还需要有限头内端的 $w,q,q_s$ 与未经修改的深源相同。

对于当前原设计中的深保护port，valley项准确为零。若flat不覆盖该port，且其整邻域满足

$$
\log w_{\rm raw}<\log c_{\rm cap}-L,
\tag{286.19}
$$

cap准确不激活，因而完整两jet相同。这可由本节原表达的严格区间比较或第286.9节深源上界直接证明；无需采样。原R15在其本身的冻结参数范围内已经支付同一条件，但不能把该文的数值直接转用于未经绑定的另一ready。

更一般地，准确相同的两jet也足够。若具体输入没有提供或证明这项源级兼容性，本文仍给有限头及深源各自的包络，**不把两者宣布为已经全域 $C^2$ 拼接**。这是原连续接缝责任的保留，不是新增BVP求解或试步验收门。

### 286.7.3 外cut

令

$$
s_{\rm out}=6d_0+\frac{6c_0d_0}{1-2^{-3/2}},
\quad
R_{\rm out}=R_*(s_{\rm out}),\quad
r_{o,\rm out}=r_c e^{s_{\rm out}/\sqrt{12}}.
\tag{286.20}
$$

冻结 $\lambda$ 后，$R_{\rm out}$ 由(286.12)唯一给出。即使原有限程序按同一个binary数据返回名义cut，也不能推出 $R_{\rm out}=r_{\rm cut,bin}$。

在原cut-preserving末port，

$$
w_{\rm out}
 =\epsilon_{\rm phys}(2d_0)^{11/4}r_{o,\rm out}^{-7},
\qquad
(j_0)_{\rm out}=\frac{r_{\rm cut,bin}}{r_{\rm old,bin}},
$$
$$
\boxed{\ ((w_*)_r)_{\rm out}
 =-\frac{7w_{\rm out}}{r_{o,\rm out}(j_0)_{\rm out}}.\ }
\tag{286.21}
$$

推导只用末port的raw表达、$\chi=0$和同一正径向速度。二阶量由(286.16)同样确定。不能把分母的旧捕获常数 $r_{\rm old,bin}$ 改为新实算 $r_{o,\rm out}$，也不能重选 $\lambda$、平移 $R_*$ 或缩放整个径向坐标来隐藏外cut差异。

若一个真实有限前缀/闭场仍以名义binary cut为其域端点，它与连续目标的域识别、metric和两jet拼接必须分别保留实际差项。本文未修改该场或原非线性求解器。

## 286.8 原深校准根：存在、非唯一与可计算选择

原R28的量化传递估计是

$$
\|T_n(\alpha)-S_3S_2S_1\|_\infty
 \le B(\delta_n,c_n)
 :=792e^{384c_n}(384c_n+36\delta_n^2).
\tag{286.22}
$$

理想下左元为 $64\alpha-65$。若 $B<33$，则真实下左元在 $\alpha=1/2$ 为负、在 $\alpha=2$ 为正。连续性给至少一个根，并且每个根满足

$$
\left|\alpha_n-\frac{65}{64}\right|\le\frac{B(\delta_n,c_n)}{64}.
\tag{286.23}
$$

它不是唯一根定理。本文不把原RK/Newton选择的binary值与某个准确根直接相等。

原实际参数所属的粗盒 $0<d_0\le1/10,\ 0<c_0\le1/16$ 已足保证所有 $n\ge160$ 的(286.22)严格小于33。只作解析有理估计即可：$c_n\le2^{-84}$、$\delta_n<2^{-163}$，故 $384c_n<2^{-75}$、$36\delta_n^2<2^{-320}$、$e^{384c_n}<2$，进而

$$
B(\delta_n,c_n)<2^{11}2^{-74}=2^{-63}<33.
\tag{286.24}
$$

这不是一次本地科学计算；也不借用原R28另一套半径、曲率或有限保护参数的数值证书。

### 可固定一个不依赖浮点猜测的选择规则

对于某个固定 $n$，准确下左元 $f_n(\alpha)$ 是 $\alpha>0$ 上的实解析函数。理由是各段长度固定、正层值及log插值对 $\alpha$ 解析，有限区间线性ODE的解对参数解析。端点异号还保证它不恒为零。

从准确异号闭区间 $[a_0,b_0]=[1/2,2]$ 出发，在每一轮的中间三分之一内，按事先固定的次序交错枚举有理点与严格求值精度，直到某点的包含区间严格在零的一侧。这样的点一定存在：非零解析函数的零点在内部不能占满区间；有理点稠密；准确ODE的收敛严格包围最终判出一个非零值的符号。取与相应端点同号的候选点替换该端点。

每轮保持两端严格异号，并将区间长度至多乘 $2/3$。闭区间嵌套且直径趋零，故唯一交点是一个根，并可按区间直径计算到任意给定绝对精度。整个枚举/精度调度必须在模型定义中固定，不能随一次预期数值结果改变。

这是一个可计算的**选根约定**，并非原ready已包含的额外数据。若不采用它或另一个明确规则，下面的深尾包络仍对所有允许根同时有效，但输出身份必须称根族，而不能虚称唯一无限背景。

## 286.9 原非理想深尾的全域平圆领与 $C^2$ metric

这里处理原 $\alpha_n\in[1/2,2]$，不将深源换成 $65/64$。对 $n\ge160$ 有 $R_n=64$、没有有限cap/valley/flat/warp修改。令 $R=64$。因为 $0<\delta_n\le1/10$，全部五个规范层值满足

$$
0<P_n\le R/\delta_n,\qquad
\frac{\max P_n}{\min P_n}\le\frac{2R}{\delta_n^2}.
$$

因此定义

$$
W_n=\frac{\epsilon_{\rm phys}R}{r_c^7}\delta_n^{7/4},
\qquad
H_n=\log\frac{2R}{\delta_n^2},
$$
$$
L_n=\frac{15H_n}{8\eta_n}+\frac7{\sqrt{12}},
\qquad
M_n=\frac{15H_n}{\eta_n^2},
\tag{286.25}
$$

可得整cell而非有限采样的界

$$
0<w\le W_n,\qquad
|(\log w)_s|\le L_n,\qquad
|(\log w)_{ss}|\le M_n.
\tag{286.26}
$$

这里使用 $\|S'\|_\infty=15/8$ 及粗但充分的 $\|S''\|_\infty\le15$。port/plateau上的log层导数为零，仍在该界内。所有估计对允许的每一个准确根选择同时成立。

记 $Z=w^2$。直接微分得

$$
|Z_s|\le2W_n^2L_n,\qquad
|Z_{ss}|\le W_n^2(4L_n^2+2M_n).
\tag{286.27}
$$

未warp深域有 $r=r_o(s)$，所以

$$
(E_*)_r=\frac{\sqrt{12}}rZ_s,\qquad
(E_*)_{rr}=\frac{12Z_{ss}-\sqrt{12}Z_s}{r^2}.
$$

因而全cell严格上界可以取

$$
|E_*-1|\le W_n^2,\qquad
|(E_*)_r|\le\frac{2\sqrt{12}}{r_c}W_n^2L_n,
$$
$$
|(E_*)_{rr}|
\le\frac{W_n^2}{r_c^2}
 \left(48L_n^2+24M_n+2\sqrt{12}L_n\right).
\tag{286.28}
$$

这些表达不依赖准确校准根的某一浮点近似。

由 $\delta_n=d_0 2^{-n}$、$\eta_n=c_0d_0 2^{-3n/2}$ 可知
$W_n=O(2^{-7n/4})$、
$L_n=O((n+1)2^{3n/2})$、
$M_n=O((n+1)2^{3n})$。
于是(286.28)右端依次趋零，最后一项至多为
$O((n+1)^2 2^{-n/2})$。同时

$$
|(w_*)_r|\le\frac{\sqrt{12}}{r_c}W_nL_n
 =O((n+1)2^{-n/4})\longrightarrow0.
\tag{286.29}
$$

因此在 $r=r_c$ 赋值 $w_*=0,E_*=1$，并在平圆领侧取相同常值，得到 $w_*\in C^1$、$E_*\in C^2$ 的延拓；若以 $h_r=w_*$ 定义旋转母线，则 $h$ 是 $C^2$ 并与平圆领匹配。这里**没有声称 $w_*$ 在 cuff 是 $C^2$**，因为 $w_{rr}$ 的粗界不必趋零；所需的metric二阶结论由 $w^2$ 的额外小量独立支付。

证明闭端点延拓时，可在每个有限开深域使用已证导数，然后由(286.28)–(286.29)的统一趋零及一维中值定理得到端点导数。不是仅凭函数值趋零而跳过端点导数存在性。

还有一个无需枚举无限cell的完整值域界。若 $N\ge160$，整个
$[r_c,r_o(\mathcal A_{N-1})]$ 由 $n\ge N$ 的cell和 cuff组成，而 $W_n\le W_N$，故

$$
\boxed{\quad
1\le E_*(r)\le1+W_N^2
\quad(r_c\le r\le r_o(\mathcal A_{N-1})).
\quad}
\tag{286.30}
$$

它包含全部无限深尾。不能把该区间近似为1后抹去 $W_N^2$，也不能据此声称有限场的全部闭合责任已付。

## 286.10 连续目标的准确结论与有限头的可复用性

在约定 $\mathcal C$、明确根规则（或明确根族）以及第286.7节真实保护端兼容性下，定义

$$
g_*=E_*(r)\,dr^2+r^2\,d\theta^2,
\qquad r_c\le r\le R_{\rm out}.
\tag{286.31}
$$

有限头由真实六primitive构造，深域由原准确根source构造。上文证明其正定性和径向 $C^2$ 系数，包括finite cusp与flat cuff。外cut连接到某个前缀或帽仍需要该相邻piece的实际同坐标两jet；本文没有从一个metric名字推出完整闭面的 $C^2$。

若与R26比较的两个模型具有**完全相同的有限冻结数据及实解释**，差别仅为 $n\ge160$ 的根值，则它们的有限头 $R_*,w_*$ 完全相同。理由是有限头内端的raw半径 $r_o(\mathcal A_{159})$ 只由源长度与 $r_c$ 决定，不依赖更深校准根；port slope也由(286.6)决定。有限头后续积分只用 $n<160$ 的原表达。

这条有限头一致性允许复用R26严格积分的代数工具，**不允许省略实际参数比对或沿用旧输出数值**。R26现有程序的某些constructor、深余项和场绑定明确带有 rational-deep 身份；不能实例化后只改标签来冒充本对象。深域仍是原根背景或其族，其全部范围由(286.28)–(286.30)另付。

## 286.11 直接产生同一个 $E_*(r)$ 的严格闭区间包围

本节给出实际原表达的生产路径，不是要求外部不明来源提供一个E区间的条件消费者。未在本地执行任何步骤，也未宣称当前已有该生产器的数值输出。

### 286.11.1 完整有限表达与分支

输入是原ready的完整冻结表、全部几何参数及源SHA，另有约定 $\mathcal C$ 和深根规则/根族身份。原每个cell、九段、全部cap/flat/cut覆盖均须保留。每个源段的 $[0,1]$ 用闭有理panel覆盖；每次二分同时保留两个闭子panel。

对一个panel：

1. 准确dyadic常数直接进入区间环，实log、exp、正根使用向外包围；相等层值的log差准确置零。
2. 若整panel可严格确认一个cap分支，就用该分支。若不能确认，保留所有可能分支在整个panel上的区间值域并取包络；不能因中点在某支就选择它。
3. 实际flat/cut规则按原固定索引及原覆盖次序处理；flat不是不经过后续cut覆盖的提前返回。
4. 用同一表达真正求 $w,w_s,w_{ss}$，再形成 $b,c,b_s,c_s$、$D$ 与(286.16)–(286.18)。不能把原独立drdx字段或renderer的jets标签替代真实导数。
5. 若区间关联丢失使(286.14)暂未显正，细分或提高精度；实际数学正性已由原正参数保证，不能强行用区间中点代分母。

cap的多支公式在真实分界处连到所需导数，flat也有明确C²连接，所以保留所有可能分支不会丢失边界。绝对值直接作区间绝对值，不需要枚举cusp根，也不要求cusp具有正间隔。

### 286.11.2 六primitive的完整严格积分

对六分量(286.11)统一处理。若一个panel的cap分支及 $w_s$ 的符号均已严格确定，可在该panel使用去掉绝对值后的解析表达，沿R26已有严格积分方法计算。使用复积分时必须认证所用复邻域的分母、log/正根分支，不能只凭实轴上连续便宣称复解析。

对分支或符号未定panel，计算六分量的全panel区间值域 $I_1,\ldots,I_6$。若准确panel长度为 $h$，则真实积分逐分量属于

$$
\int_{\rm panel}f_k(s)\,ds\ \in\ h I_k,\qquad k=1,\ldots,6.
\tag{286.32}
$$

完整贡献必须加入总和，不能将“不确定小段”删除或置零。该式对常cap、非孤立cusp和分支交点同样成立。有限头上的各被积函数连续，因而在不断细分且区间算术精度提高时，完整上下Darboux和差趋零。这里的收敛来自真实有限表达的连续性和向外区间扩张的一致性，不来自G8/G16差值。

对于闭panel覆盖，端点重复不造成积分重复：积分使用相邻端点的区间长度，每个正长度子区间只计一次；共享端点仅用于值域与拼接覆盖。源段累计、cell累计和全头累计都按同一真实原点形成，保存完整贡献表及剩余未访stack。

若预算用完，可以输出已经得到的包含界及完整未处理范围；没有完整范围的输出不得称全头包含，包含界宽于目标也不得称该目标已达成。预算停止不是原metric、BVP或几何失败。

### 286.11.3 对给定物理半径闭区间作真实逆像覆盖

设查询为一个准确闭区间 $J$，已识别为(286.31)的真实定义域内。对每个有限源piece先由严格primitive给出其真实径向像包围。只丢弃已被严格证明与 $J$ 不相交的piece或panel。其余panel均保留或细分；当多个候选的半径区间重叠时，不用旧first-match或浮点端点作任意选择。

对保留下来的每个panel，计算(286.18)的 $E_*$ 值域，取全部包络。由于 $R_*$ 严格递增，每个真实逆像点必在某个未丢弃panel内，故该包络覆盖整个 $J$。跨cell、cap边界及cuff的查询必须同时含两侧闭端点。深域用(286.30)完整覆盖；若需更紧，可取更深的 $N$，对新增有限cell用已明确根规则的严格根区间，不能把它们改成 $65/64$。

这个过程不需要把辅助 $R$ 假定为二阶光滑，也不需要原有限point.r的单调性。真实 $R_s$ 正下界可将径向宽度换算成参数逆像宽度；它来自(286.14)。

需要区分“区间真实变化”与“包围误差”。若 $E_*$ 在 $J$ 上本就变化，细分不会使其完整值域宽度趋零。有效收敛指：对细分后的各个物理cell，区间扩张的过宽量趋零；在确有严格余量的同场不等式上，最终可以作出严格判断。没有严格余量、查询越出真实cut或输入缺少域识别时，算法诚实保留未付范围。

### 286.11.4 与有限Gauss语义的关系

旧entry.integrate使用G8、G16六分量共同接受条件，原最大depth16及预先split的cusp节点。一个分量的判定可以改变全部六分量采用的子区间。不能把其中两个分量单独改用另一分支后仍称原有限返回。

上面的真实积分生产器不重演该接受条件，而是对准确六函数积分；这并不改变原有限程序。要比较旧程序，就完整保留原六分量的实际返回和树，再将其准确binary值与对应真实积分区间相减。所有六分量、partial、cumA/cumB、原累计括号和最后的浮点组合误差，都可通过“实际保存词减准确共同表达”的包含差显式承担。

旧G8/G16差小不必是真积分误差界；depth16强制返回也不提供这样的界。原drdx是integrand另算值，因此即使它一直为正，也不能据此推出自适应point.r是同一个可微或单调函数。这里给出的真实 $R_s=D$ 与point误差必须分开记。

## 286.12 一次实际有限返回到连续目标的可计算误差桥

本节不要求全48层树先被穷举。假设保存一个实际背景查询的准确binary词：

$$
\widehat r,\quad
\widehat x,\quad
\widehat w,\quad
\widehat E,
$$

以及它实际选择的原piece、完整来源和实际profile返回。$\widehat x$ 只被当作准确dyadic参数；不把它预称准确反函数值。

由第286.11节同一真实piece的primitive和slope包围，求出

$$
|R_*(\widehat x)-\widehat r|\le\varepsilon_r,\qquad
|\widehat w-w(\widehat x)|\le\varepsilon_w.
\tag{286.33}
$$

如果实际 $\widehat r$ 与 $R_*(\widehat x)$ 的连接径向区间都在同一连续目标的定义域内，并有完整真实导数界 $|(w_*)_r|\le L_w$，则

$$
|\widehat w-w_*(\widehat r)|
 \le \varepsilon_w+L_w\varepsilon_r=:\varepsilon.
\tag{286.34}
$$

这是三角不等式与中值定理。不要求原数值selector选择正确piece：若所需径向路径跨相邻piece，$L_w$ 必须覆盖完整跨piece路径及端点；若无法证明同域，就不能用该式越界延拓。

进一步，令

$$
\varepsilon_{\rm arith}
 :=\left|\widehat E-(1+\widehat w^2)\right|,
$$

其中右端把保存binary词视为准确有理数，乘加在证明中是准确实运算。则

$$
\boxed{\quad
|\widehat E-E_*(\widehat r)|
 \le\varepsilon_{\rm arith}
      +2|\widehat w|\varepsilon+\varepsilon^2.
\quad}
\tag{286.35}
$$

原background的 $\widehat w=\mathrm{Math.exp}(\widehat{\log w})$、$\widehat E=\mathrm{fl}(1+\mathrm{fl}(\widehat w^2))$ 两算式没有被改写；$\varepsilon_{\rm arith}$ 恰保留它们与准确多项式的差。若另一实际consumer保存的是另一条E算式，也可以对其原 $\widehat E$ 直接使用同一差定义，不把两个浮点口径混为一谈。

(286.33)中真实 $R_*(\widehat x)$ 的计算从唯一真实内端开始，完整包含之前所有primitive以及本piece partial。因而原adaptive、prefix sum、global $\lambda$ 乘法、旧captured起点和48步停止带来的偏差都没有被遗漏。可以逐项另外分解，但不能先假设某项为零再套用结论。

该桥比较的是一个明确连续模型与原真实有限返回；它不把原返回重标为连续模型的解。直接作同场metric区间比较时，可完全绕过这一步，只使用第286.11节的目标 $E_*(J)$。

## 286.13 可选的48步统一误差界及其准确前提

只在下列前提已由实际完整包围支付时，才可给一个简洁统一界：

- 对所选piece的全部相关参数点，有
  $|\widehat R(x)-R_*(x)|\le\eta_R$；
- 真函数满足 $0<(R_*)_x\le M$；
- 查询在原两个有限端值形成的正确数值bracket内，且有限返回无NaN/无穷；或直接给出初始真不等式
  $R_*(0)\le\widehat r+\eta_R$、
  $R_*(1)\ge\widehat r-\eta_R$。

这里的 $\widehat R$ 是原实际数值表达，不要求它连续或单调。原条件 $\widehat R(m)<\widehat r$ 成立时令lo=m，否则令hi=m。于是每次更新都保持

$$
R_*(\mathrm{lo})\le\widehat r+\eta_R,\qquad
R_*(\mathrm{hi})\ge\widehat r-\eta_R.
\tag{286.36}
$$

从0和1出发，48次原二分使用的dyadic中点在binary64中均准确可表示，最终宽度准确为 $2^{-48}$。取最终中点 $\widehat x$，由(286.36)及真导数上界得到

$$
\boxed{\quad
|R_*(\widehat x)-\widehat r|
 \le\eta_R+M\,2^{-49}.
\quad}
\tag{286.37}
$$

因此可将其代入(286.34)–(286.35)。这个推导使用的是每个原比较的真误差包围，而不是假装48次比较在准确反函数上执行。

当前并没有从保存的radialResidual或G8/G16差值得到 $\eta_R$；也没有对所有非flat分支实际生产统一 $\eta_R$。R285树预算停止不能被这里掩盖。对某个已保存查询，(286.33)通常更直接，因为它只需准确求值实际 $\widehat x$ 与所需完整primitive，不先枚举所有可能数值路径。

## 286.14 对 a601 / R251 的同场 metric 接口

对于一个真实已绑定的完整有限场 $F$，其actual fullprefix、shared-B、Hermite tail、两帽、mean和SE(2)注册仍取原精确有限表达。本文的目标对象只提供同一原来源下明确选择的 $g_*$，不把目标改成 $1+(B')^2$，也不把有限场本身重定义为连续旋转模型。

材料角记为 $\theta$。如果实际场使用参数 $u=(u_1,u_2)$，其真实材料坐标为

$$
\chi(u)=(r(u),\theta(u)),
$$

那么同坐标目标矩阵是

$$
G(u)
 =D\chi(u)^{\!T}
   \begin{pmatrix}E_*(r(u))&0\\0&r(u)^2\end{pmatrix}
   D\chi(u).
\tag{286.38}
$$

例如tail的物理角为 $\phi$、材料角为 $\theta=\Phi(\xi,\phi)$ 时，$\Phi_\xi,\Phi_\phi$ 和径向变换必须全部保留，特别是混合项。只有在实际公式证明其为零时才能删除；有限 $\theta$ Fourier带宽不自动成为有限 $\phi$ 带宽，反之亦然。

令实际有限场第一基本形式为 $Q=DF^{T}DF$。沿 [R251](R251-direct-relative-operator-metric-certificate.md) 对同一个正定 $G$ 作相对算子比较，即可将第286.11节产生的连续目标包络和原完整 $F$ 的真实一阶jet结合。闭格的全部边界、prefix/tail/cut/cuff/两帽以及所有未访空间和phase范围仍须完整保留。它不要求先完成一个不相干的全selector舍入证书，也不从有限点值自动推出全域结果。

当前 a601消费者中外部tail-target责任必须记录准确模型身份：冻结输入、约定 $\mathcal C$、深根规则或根族、自然 $R_{\rm out}$ 与实际域识别。若这些身份仍未选定，就不能仅凭一个数值E包络将标志改成“原连续g已支付”。

本证明不会自动支付以下各项：真实接受的full-native/field；当前场与该目标的连续两jet/seam；原README的全域相对metric阈值；强幅、held、非平面、完整reach或所有 $t$。这些责任保持原定义和原门，不增加新的求解验收标准。

## 286.15 最小真实生产接口与诚实的完成状态

一个可接的独立连续目标producer至少应绑定：

| 部分 | 必须保留的实际对象 |
|---|---|
| 来源 | 原ledger-ready、stored-ready、参数和全部源SHA；不借另一ready |
| 模型 | $\mathcal C$ 的准确语义、有限表、根规则/根族、protect/方向/rejoin |
| 表达 | 全160有限cells的九段、cap/flat/cut/weight顺序、六primitive |
| 闭域 | 自然 $R_{\rm out}$、深原点、全部闭panel、待访stack与query suffix |
| 输出 | $E_*,(E_*)_r,(E_*)_{rr}$ 的有理端点包围及完整覆盖范围 |
| 接缝 | 内保护端真实两jet、cut实际域匹配；缺项显式unpaid |
| 可选误差桥 | 实际原piece/x/r/w/E词和(286.33)或(286.37)的完整范围 |
| 同场接线 | 当前完整finite-field binding、材料坐标pullback与原g模型身份 |

有限真实积分可以复用旧严格算术kernel，但不得让旧R26构造器的 rational-deep 字段、历史包络或不适用的flat限制悄悄通过。应新建薄的输入/表达层，直接读实际完整参数，把每次返回的目标区间与本表身份绑定。

没有新数值输出时，诚实状态是：**连续模型构造与误差桥已证明；模型语义尚需按当前目标明确采用；独立实际包络执行、同场metric和接缝证书未生成。** 这比R285有实质推进——不再只有有限选择树，而有原根背景的连续 $E_*$ 及其可计算包围——但没有把未运行或未选定的责任写成成功。

### 与既有结论的准确差异

- R285覆盖原48层有限selector，不给它连续实函数身份；本结果明确构造连续对象并比较两者。
- 原R15证明其参数范围内旋转背景曲率及母线C²；本结果证明一般正weighted warp的cusp二阶metric消去，并保留实际保护端条件。
- 原R28给准确深根存在与统一背景界；本结果保留原根类别，明确可计算选择和全域 $E_*$ 二阶包络。
- R26完整支付另一个 rational-deep 的实积分对象；本结果只在完整有限数据相同时复用有限头工具，绝不继承其无限身份或数值证书。
- R251消费同场目标包络；本结果补的是明确原来源连续目标和真实生产路径，不是重复一个外部区间的充分条件。

本次只读源码与证明、撰写精确推导和接口；未导入数值模块、未执行区间积分/ODE/校准/selector、未计算实际E区间、未改原stored或非线性源、未创建或重标一个已接受场。
