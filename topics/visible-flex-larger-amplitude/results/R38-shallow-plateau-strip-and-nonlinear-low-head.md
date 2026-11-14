# R38：浅层平顶角宽下的强46模盒与真实低深图反馈

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

**已证明。** 对 R26 的同一真实固定源、R35 的同一46个浅高度和
R18 的同一完整真实深图，把证明空间的角宽改为

$$\widetilde\tau_n=\max\{2,1+(n-12)\log2/4\},\qquad12\le n\le224,
\tag{38.1}$$

则 R36 的辅助低46联合边值问题在下面明确的更强空间内有唯一
小解。全部213个胞元、全部46个低深参数均保留；完整点态mean
根仍参加源和深图计算。所得盒满足

$$\max_n U_n<1.005608,\qquad L_{\rm total}<0.021864,$$
$$|z|_{38}<2^{-2231.2349}<2^{-2231}.
\tag{38.2}$$

真实非线性低深图反馈消耗的不变性余量比例小于 $2^{-242}$，
新增Lipschitz常数小于 $2^{-245}$。度量、微分方程、浅高度和
深图均未改变；变动的是实际重算的范数权、Green界和盒。

**范围。** 这仍是完整源在输出处投影到物理 $m=2,4,\ldots,92$
的辅助问题。完整深图的高频两分量尚未装入头部，头部自产高频、
其与低窗的反馈及完整mean接缝尚须联合处理。外0..11胞元、实际
强前缀H向量以及闭面的全时几何条件不由本结果推出。

## 1. 固定的问题和真正改变的空间

令 $Y^0$ 为 R35 的真实线性参考，node12 的前八个高度取已有
q003包中准确的binary实数，其余38个参考高度为0。46个真实
浅高度增益都非零，且都已计算；参考中的零不限制校正后的深端
低参数。令 $\mathcal L$ 为真实线性算子，$N$ 为 R23 在完整
mean小根上计算的点态非线性源。

本结果的辅助方程及浅端条件是

$$\mathcal L Y=\Pi_{46}N(Y),\qquad
Q_m(b)=Q_m^0(b),\quad m=2,4,\ldots,92,
\tag{38.3}$$

其中 $b=r(\mathrm{node12})$。far为 physical node225，即数学
F224；其低高度参数为

$$S_F=\epsilon\delta_{224}^{11/2}/r_c^3,\qquad
z_j=e^{38(2j)}Q_{2j}(a)/S_F,\quad a=r(F224).$$

far低斜率等于 R18 **完整真实图** $\Gamma(z)$ 的低斜率投影。
该图本身保留高频和mean；这里只取其低斜率作为辅助边界条件。

在cell n定义

$$\widetilde X_n(Y)=\sum_{m\ne0}e^{\widetilde\tau_n|m|}
\left[(1+|m|)^3\sup_n|Q_m|+(1+|m|)\sup_n|\Xi_m|\right].
\tag{38.4}$$

两个分量的sup分别取。对有限46模空间这是完整范数。
(38.1) 只在cells12..17取常数2；cell18起严格沿用旧角宽。
因此far角宽及其与38的最后一次转换完全不变。

R23的源界与半径对任意固定非负角宽成立，其代数常数不依赖
角宽值。故在每个新空间中仍有

$$\|N(Y)\|_{L^1\mathcal W_{\widetilde\tau_n}}
\le B_n\widetilde X_n(Y)^2,$$
$$\|N(Y)-N(\widetilde Y)\|
\le2B_n\{\widetilde X_n(Y)+\widetilde X_n(\widetilde Y)\}
\widetilde X_n(Y-\widetilde Y),$$
$$B_n=2^{12}r_c^3/(\epsilon\delta_n^{19/4}),\qquad
r_n=2^{-23}\epsilon\delta_n^{19/4}/r_c^3.
\tag{38.5}$$

以下逐层核销整个盒内 $\widetilde X_n<r_n$。

## 2. 从真实46列重新计算权与参考

记原角宽 $\tau_n=1+(n-12)\log2/4$，并令

$$\beta_n=(2-\tau_n)_+.$$

R35每对胞元、每个物理模的准确Green核包络保持不变；只有
源和目标范数的转换因子改为

$$e^{m(\widetilde\tau_k-\widetilde\tau_n)}
=2^{m(k-n)/4}e^{m(\beta_k-\beta_n)}.
\tag{38.6}$$

程序逐一读入六个真实有符号列组、同cell有序核和cells12/13
真实分量sup，核对所有输入SHA，再对全部46模计算 (38.6)。
指数因子的Arb包围向上取dyadic界；原半整数二进制指数再向上
取整，最多额外损半比特。逐块取最大值给正数
$\widetilde\gamma_{kn}=2^{g_{kn}}$，满足

$$\widetilde X_k(Gf)\le\sum_n\widetilde\gamma_{kn}
\|f\|_{L^1\mathcal W_{\widetilde\tau_n}(n)}.
\tag{38.7}$$

这里取对角Fourier算子的范数最大值，再乘源的总加权
$\ell^1$ 质量；无需额外乘46。同胞元继续使用有序核，不退回
两个整个胞元最大值的无序乘积。没有重新近似源几何或替换真实流。

参考上界也重新计算为 $x_n\ge\widetilde X_n(Y^0)$，而非保留
旧角宽的数。对同一个准确参考far幅度 $a_m$ 和已付真实列，取

$$x_n=\sum_m e^{\widetilde\tau_n m}|a_m|
\left[(1+m)^3\Phi_{Q,n,m}+(1+m)\Phi_{\Xi,n,m}\right]
\tag{38.8}$$

的外舍入上端。全213×213矩阵和逐层参考分别保存在
`closure-plateau2-green.json.gz` 与 `closure-plateau2-reference.json`。

直接统一相对球的检查已经给出

$$\eta=\max_k\sum_n\widetilde\gamma_{kn}B_nx_n^2/x_k
<0.005597545,$$
$$\eta(1+1/100)^2<0.005710056<1/100,$$
$$4\eta(1+1/100)<0.022614081<1.
\tag{38.9}$$

这支付了线性far辅助问题的一个统一球。下面另用更小的非等
半径盒，使far参数估计和后续高频源密度更强。

## 3. 实际非等盒与严格门

定义

$$\widetilde A_{kn}=\widetilde\gamma_{kn}B_nx_n^2/x_k,$$
$$\mathcal B=\{V:\widetilde X_n(V)\le(U_n-1)x_n\},\qquad
d(V,\widetilde V)=\max_n\frac{\widetilde X_n(V-\widetilde V)}{W_nx_n}.
\tag{38.10}$$

与 R35 相同，先以普通浮点迭代提议 u,w，再把输出binary值
$U=u+2^{-30}w,W=w$ 固定成准确dyadic输入。普通迭代不是证明。
所有最终门从真实 $B_n,r_n$、参考上端、dyadicGreen矩阵重新
用192位Arb向外计算。准确213行 $U,W$ 保存在
`closure-plateau2-box.json`。

所得严格不等式是

$$s_k=U_k-1-\sum_n\widetilde A_{kn}U_n^2>0,
\qquad\min_k s_k/W_k>9.2114159\cdot10^{-10},$$
$$L=\max_k\frac{\sum_n4\widetilde A_{kn}U_nW_n}{W_k}
<0.021863096,$$
$$U_nx_n<r_n\quad(12\le n\le224).
\tag{38.11}$$

部分盒数据如下，显示值仅用于阅读，证明使用JSON里的准确端点。

| cell | $U_n$ | $W_n$ |
| --- | ---: | ---: |
| 12 | 1.00090864854719 | 1.00486527749245 |
| 13 | 1.00560772079857 | 1.03002606762039 |
| 14 | 1.00004667328187 | 1.00024900516940 |
| 224 | 1.00000001797070 | 1.00000009123598 |

最大U在cell13且小于1.005608。整个参考的半径比小于
$2.162454\cdot10^{-10}$，全部盒半径门直接逐行核销。
这消除了旧角宽正majorant中 $U_{13}\approx282$、
$U_{14}\approx6692$ 的相对膨胀；没有据此声称两个不同充分盒
定义完全相同，也不需要预先比较二者的包含关系。

## 4. 全部46参数的far域

最后cell的角宽没有改变。R34已付准确转换常数

$$C_F=\max_{m=2,4,\ldots,92}
\frac{e^{(38-\tau_{224})m}}{(1+m)^3}<40804.559661132.$$

全部46模参加最大值，最坏是m92。参考仍满足
$\log_2Z_0<-2232.18975653$，所以整个新盒满足

$$|z|_{38}\le Z_0+(U_{224}-1)x_{224}C_F/S_F,$$
$$\log_2|z|_{38}<-2231.23499966455.
\tag{38.12}$$

因此可保守取 $Z_*=2^{-2231}$。相比先前同一$2^{-2200}$工作门，
现在还有超过31.2349比特的余量。这里没有用参考中为零的38项
来删去允许变化的参数，也没有省略far角宽差。

## 5. 完整真实深图的低反馈

沿用 R36 的准确Wronskian提升。设 $\phi$ 为far可容许列，
$\psi_Q(b)=0,\psi_{\Xi,12}(b)=1$，
$W_m=\mu_{12}\phi_Q(b)\ne0$。对深端物理canonical斜率差
$d_m^{\rm phys}$，

$$\mathcal B_m d_m^{\rm phys}(r)
=\frac{\mu_{224}}{W_m}\psi_m(r)d_m^{\rm phys}.
\tag{38.13}$$

R18完整非线性差 $\mathcal D=\Gamma-\Gamma^{\rm lin}$ 满足

$$\|\mathcal D(z)\|\le2^{1967}|z|_1^2,\qquad
\|D\mathcal D(z)\|\le4\cdot2^{1967}Z_*
\quad(|z|\le Z_*).
\tag{38.14}$$

后一式来自已经建立的共同复球全纯估计。低斜率投影范数至多1。
归一低输入d对应 $d_m^{\rm phys}=S_Fe^{-38m}d_m$。
每个胞元的实际提升范数重新按新角宽计算：

$$K_k=\max_m\frac{\mu_{224}S_F}{\mu_{12}|\phi_Q(b)|}
e^{(\widetilde\tau_k-38)m}
\left[(1+m)^3\sup_k|\psi_Q|+(1+m)\sup_k|\psi_\Xi|\right].$$

令

$$b_D=\max_kK_k/(W_kx_k),\qquad
e_D=W_{224}x_{224}C_F/S_F.$$

独立新入口读取每一行实际角宽，完整重算得

$$\log_2b_D<2222.932207,\qquad
\log_2e_D<-2206.5519291,$$
$$\log_2\left(4b_D2^{1967}Z_*e_D\right)<-245.6197230,$$
$$\log_2\max_k\frac{K_k2^{1967}Z_*^2}{x_ks_k}<-242.0677935.
\tag{38.15}$$

所以真实低边界反馈严格小于每行现有余量，新增Lipschitz常数
小于 $2^{-245}$。同时记录的完整深尾mean界仍为

$$|\kappa_0(a)|\le2^{99}\epsilon\delta_{224}^{33/4}Z_*^2,$$
$$|\overline v(a)-\overline v(r_c)|
\le r_c2^{853}\epsilon\delta_{224}^{25/4}Z_*^2.
\tag{38.16}$$

它们不是0，也未被当成头部mean接缝已经满足。

## 6. Banach固定点和本结果的解

在满足物理接口连续性、齐次浅高度的有限46模连续场完整空间中
取 (38.10) 的闭盒，不预先向输入施加线性far条件。令

$$T(V)=G\Pi_{46}N(Y^0+V)
+\mathcal B\mathcal D_{\rm lo}(z^0+\mathcal EV),
\tag{38.17}$$

其中 $\mathcal E$ 为准确far低高度评估。
(38.11) 与 (38.15) 使T把盒映入自身，并给

$$\operatorname{Lip}(T)<0.021863096+2^{-245}<0.021864.$$

Banach定理给此盒内唯一固定点。第一项施加齐次真实线性深条件，
第二项准确补上完整深图的低斜率差，故固定点满足 (38.3) 和
实际非线性低边界条件。完整mean根在整个盒内有效；源连续，
真实一阶系统再给canonical变量可微及有限头部高度的两阶正则性。
这个正则性仍是辅助投影方程的正则性，不使未进入微分方程的
高频Darboux残差自动为零。

## 7. 可重算链、实际退出和后续接口

独立入口保留旧脚本及旧结果：

- `computations/closure_plateau2_reference.py`：逐cell新角宽参考与far转换。
- `computations/closure_plateau2_green.py`：同一真实核的全部46模重新加权。
- `computations/closure_anisotropic_low46_box.py`：未改动的严格盒检查。
- `computations/closure_plateau2_nonlinear_low_far_lift.py`：读取实际角宽并取
  $Z_*=2^{-2231}$ 的新低边界提升；原R36入口保持不动。

四次实际作业均经 `strong_resource_run.py` 记录退出码0，且会话
79956、22619、49062、80912均已正式poll到exit0。相应resource
保存完整命令、wait4退出状态和峰RSS；最大峰值小于94MiB。
所有数学结果保存准确dyadic端点及全部输入/源SHA。

最终反馈复算命令为：

```bash
python computations/strong_resource_run.py \
  --out notes/2026-11-12-closure-plateau2-nonlinear-low-far-lift-resource.json -- \
  python computations/closure_plateau2_nonlinear_low_far_lift.py \
  --columns notes/2026-11-12-closure-real-linear-q003-low46-recovered.json.gz \
  --ordered notes/2026-11-12-closure-ordered-green-low46-v2.json.gz \
  --reference notes/2026-11-12-closure-plateau2-reference.json \
  --box notes/2026-11-12-closure-plateau2-box.json \
  --ready notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json \
  --out notes/2026-11-12-closure-plateau2-nonlinear-low-far-lift.json
```

浅层平顶给R33的强条带源估计提供额外的真实解析余量，并使
所需物理幅度包络更小。中频及高频源必须仍用其正确的径向位置、
逐模密度和实际strip转换支付；(38.2) 本身没有免费补齐这些核。
实际强H向量可以另建同规范参考重做这些门，不能直接沿用q003
的小幅盒作为强分支的闭合结论。
