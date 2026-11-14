# R22：宽 strip 真实深尾的高频端迹经过精确线性浅头的包络

2026-11-12，exact_closure，GPT-6 Astra Pro，AI-assisted。

状态：**已证明的条件线性传播引理**。它支付 R18 真正非线性深尾所带的高频端迹，经过实际浅头的**精确线性方程**后有多大；不是浅头非线性存在或匹配证明。浅头自身的非线性 forcing 另需控制。它允许所有高频浅 cut 高度相应改变，绝不提供任意全 Dirichlet 无限 DN。

## 1. 精确定义和命题

取 R15/R17/R18 的固定新实背景：深部 $n\ge160$ 使用有理 $\alpha_n=65/64$；其前面的实际 cap/valley/warp 参数固定一次。源函数的指数、对数和径向积分按其明确实函数定义。本引理处理这些实函数，不把求积得到的 `r` 与独立计算的 `drdx` 当成已经认证的同一函数。

使用当前参数范围

$$
3/500\le d_0<1/128,\quad c_0\le1/16,\quad
c_\eta=c_0/\sqrt{d_0}\le2/3,\quad
3/64<r_c<1/16,
$$
$$
0<\epsilon_{\rm norm}<2^{15},\quad
2<\alpha_{\rm warp}<162,\quad \kappa_{\rm cap}=8.
\tag{1.1}
$$

对有限源 $12\le n<160$ 再假设：

- 保存后固定的源 $\alpha_n\in[1/2,2]$；它们无需为精确校准根。
- $2\le R_n\le64$；$n\ge16$ 时 $R_n=64$。
- 长度采用同一 $\delta_n=d_0 2^{-n}$、$\eta_n=c_\eta\delta_n^{3/2}$ 九段配方。
- valley control 为0，warp weights 为1，无 custom pulse/valley cap；普通 slope cap 为当前的 $0.02$，过渡宽度为2。

这些都是有限数据或固定配方的条件。实际 depth12/far225 endpoint worker 的 `shallowSourceParameters` 已保存全部160个源 cell 参数；附属脚本对所需148个 $\alpha_n$ 作了逐项精确有理范围比较，当前范围为

$$
\frac{571647791199689}{562949953421312}
\le\alpha_n\le
\frac{148727001379739}{140737488355328}.
$$

同一核销还覆盖后16层的 $R=64$、dyadic $\delta$ 配方、零 valley controls、单位 warp weights、相关层没有 custom caps/flat override、固定 cap/warp/radius/epsilon 参数。保存于
`notes/2026-11-12-closure-wide-strip-head-ledger-paid-source.json`；输入是 `notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json`，其完整 hash 同时保存。这支付的是当前固定参数的范围条件，不是源实积分误差；旧包本身没有这个完整参数表。

记数学 F224 对应 physical node225。对任意 R18 真实低46高度输入，假设它在绝对角宽 $\tau_F=128$ 上满足

$$|z^{128}|_1\le2^{-1947}.$$

取其**完整真实深 trace**在 $j>46$ 的部分，用当前实背景的准确线性方程从 physical node225 传播到 physical node12。令物理 raw 线性坐标为 $(Q_m,\Xi_m)$，$m=2j$，$\nu_m=m^2(m^2-1)/12$。则有

$$
\boxed{
\sum_{j>46} e^{2j}
\left(|Q_{2j}(12)|+|\Xi_{2j}(12)|/\nu_{2j}\right)
<2^{-872}.
}
\tag{1.2}
$$

这个界使用真实线性积分，不依赖某个 RK4 输出。它是一个确定的误差项：完整深尾的高频端迹没有被设成零，但在同一线性头下其输出极小。它不包含头内低频之间的非线性相互作用所新生成的高频。

## 2. 两个 strip 确实给同一条深尾

R18 的常数不依赖绝对角宽 $\tau_F$，只依赖固定增量 $h=\log2/4$。同一物理低高度输入在不同宽度下的坐标满足

$$z_m^{\tau_2}=e^{m(\tau_2-\tau_1)}z_m^{\tau_1}.$$

宽 strip 解限制到窄 strip 后仍在其原来的状态球内；其46个参数标签逐模乘以不超过1的因子，也仍在原标签球内。它具有同一窄 strip 低高度。R18 的固定点和低高度反函数的唯一性因此说明两者是同一解，而不是两个不同的远端边界。

所以低模 Robin 误差可以继续使用窄 strip 的精细界，高模则使用宽 strip 的指数衰减。这里绝不据此把第47模起的高度设0，也不把浅 cut 上一个任意有限多项式识别成这条真 trace。

R18 (9.5) 在宽 strip 给

$$
\sum_{j>46}e^{128(2j)}
\big(|U_{Q,2j}|+|U_{\Xi,2j}|\big)
\le\epsilon_{\rm norm}\delta_{224}^{11/2}
 2^{1967}|z^{128}|_1^2.
$$

乘回物理 raw 坐标的因子 $r_c^{-3}<2^{15}$，并用 $\delta_{224}<2^{-231}$，得

$$
\sum_{j>46}e^{128(2j)}
\left(|Q_{2j}(225)|+|\Xi_{2j}(225)|/\nu_{2j}\right)
<2^{15+15-231\cdot11/2+1967-3894}
<2^{-3167}.
\tag{2.1}
$$

这里宽 strip 只要求图半径 $2^{-1947}$，没有误用较小的实用 Robin 球 $2^{-2048}$。

## 3. 当前 warp 的实几何宽度与 log 变化量

用 $r_o$ 表示未 warp 的源半径，$r$ 表示实际半径，$\mu=\epsilon_{\rm phys}\delta^{11/4}$。在 $n\ge12$，原始 slope 上界为

$$
W_n:=2^{21}\delta_n^{7/4}.
\tag{3.1}
$$

原因是 $p_*$ 的最大层值为 $R_n/\delta_n\le64/\delta_n$，而 $r_o\ge r_c$。此时 $W_n<2^{-12}$。又 $0.02>1/64$、$e^{-2}>1/8$，所以普通 cap 的非平凡过渡尚未开始；整个 $n\ge12$ 实源均未触发该 cap。最后一个不等式可由 $e<11/4$ 立即得到。

源总 log 长度小于 $33/640$，$\sqrt{12}>24/7$，从而

$$
\log(r_o/r_c)<77/5120<1/65,
\qquad r_o/r_c<65/64.
$$

每个源 cell 的径向长度满足

$$
\Delta r_o
\le r_c\frac{65}{64}\frac{27}{8}\frac7{24}\delta_n
<r_c\delta_n.
\tag{3.2}
$$

其五个 log 层值按两峰交替。profile 本身的总变化量不超过 $3W_n$，乘上 $r_o^{-7}$ 所增加的变化量不超过 $7\delta_nW_n$。故

$$\operatorname{TV}(w_n)<4W_n.$$

实际 warp 的导数由源定义给出（内端的 $\chi$ collar 也适用）

$$
0<r_x\le(1+\alpha_{\rm warp})(r_o)_x+
 \frac{|w_x|}{8}.
$$

因此实际 cell 宽度 $L_n$ 满足

$$
\boxed{\frac{L_n}{r_c}
\le\overline L_n:=163\delta_n+11W_n.}
\tag{3.3}
$$

由于 $\alpha_{\rm warp}/(1+w^2)>1$，还直接有 $r_x\ge(r_o)_x$，从内端逐 cell 得 $r\ge r_o$。

把 (3.3) 从12起相加，使用 $2^{-1/4}<27/32$ 和 $2^{-7/4}<3/10$，得到精确有理界

$$
\sum_{n\ge12}\overline L_n
<163\,2^{-18}
 +11\,2^{-12}\frac{27/32}{1-3/10}
<1/256.
\tag{3.4}
$$

所以全部相关半径满足

$$1\le r_o/r_c\le r/r_c<257/256.$$

令 $V_n=\operatorname{TV}(\log w_n)$。直接对五层 log 值求变化量，并加上 $7\Delta\log r_o<7\delta_n$，有

$$
V_n\le2\log128+6|\log\delta_n|+7\delta_n
<\overline V_n:=5(n+9).
\tag{3.5}
$$

这里用了 $d_0>2^{-8}$ 和 $\log2<7/10$。只取下降变差则更精确：

$$
\int_{\text{cell }n}(-w_r/w)_+dr
\le\log(\alpha_nR_n)+3|\log\delta_n|+7\delta_n
<(3n+32)\log2.
\tag{3.6}
$$

这些是实源不等式；没有从浮点 profile fingerprint 推导积分误差。

## 4. 全模式线性角宽损失小于4

准确线性高度方程是

$$
(w C_m')'-m^2(w'/r)C_m=0.
\tag{4.1}
$$

令非均值物理一阶场为 $p=v_\theta/r$、$\kappa=v_r$。其线性系统为

$$p_r=(\kappa_\theta-p)/r,\qquad
\kappa_r=-(w_r/w)(\kappa+p_\theta).$$

在 cell n 上固定

$$b_n=\sqrt{\overline V_n/\overline L_n}>1.$$

对单频复系数使用 $|b_np_m|+|\kappa_m|$。矩阵的列和估计给

$$
\frac{d}{dr}\|W_m\|
\le\left[(-w_r/w)_+
+|m|\left(\frac{b_n}{r}+\frac{|w_r/w|}{b_n}\right)\right]\|W_m\|.
$$

故该 cell 的角指数损失至多

$$\beta_n=b_nL_n/r_c+V_n/b_n
\le2\sqrt{\overline L_n\overline V_n}.$$

因为 $b_n$ 随 n 递增，向外经过相邻 cell 时，改用较小的 $b_{n-1}$ 不增加范数。不存在逐 cell 乘一个巨大的规范转换常数的问题。

对上式拆开两项平方根，得到

$$
\beta_n\le\frac{21}{4}\sqrt{n+9}\,2^{-n/2}
+320\sqrt{n+9}\,2^{-7n/8}.
\tag{4.2}
$$

令 $r_1=91/128>2^{-1/2}$、$r_2=35/64>2^{-7/8}$。写 $n=12+k$，用
$\sqrt{21+k}\le(23/5)(1+k/42)$，可把无穷和直接算成有理数：

$$
\sum_{n\ge12}\beta_n
\le\frac{23}{5}\left[
\frac{21}{4}\,2^{-6}G(r_1)
+320\,2^{-10}r_1G(r_2)\right]
<3.703<4,
$$
$$G(r)=\frac1{1-r}+\frac{r}{42(1-r)^2}.
\tag{4.3}
$$

这支付所有角频的角宽损失，不仅是某个固定有限频带。

## 5. 能量块的零阶增益与端口规范

对连续 cell $12,\ldots,S$，由 (3.6) 和上一节有

$$
\|W_m(12)\|
\le2^{A_S}e^{4|m|}\|W_m(S+1)\|,
\quad A_S=\sum_{n=12}^S(3n+32).
\tag{5.1}
$$

这里只要在未由更精细传递界覆盖的有限浅块上使用 (5.1)，不把它粗乘到全部224层。

定义物理线性 canonical 坐标

$$
Q_m=C_m/r^4,\qquad
\Xi_m=\frac{r^7w}{\mu}
\frac{C_m'/r^3-m^2Q_m}{\sqrt{12}}.
\tag{5.2}
$$

在数学端口 n，$w=\mu_n/r_o^7$。于是

$$p_m=-m r^3Q_m,\qquad
\kappa_m=r^3\left(m^2Q_m+\sqrt{12}(r_o/r)^7\Xi_m\right).
$$

采用 raw 平衡范数 $|Q_m|+|\Xi_m|/\nu_m$。由 $r/r_c<257/256$、$(257/256)^7<2$ 和 $m\ge2$，上述来回转换至多付

$$4(b_S+1)m^4.$$

又 $\overline L_S\ge163\delta_S$、$\delta_S>2^{-S-8}$、$S\le224$，所以

$$b_S^2< (S+9)2^{S+3}<2^{S+11}.$$

能量块在平衡 raw 坐标中的算子范数因此不超过

$$
2^{A_S+\lceil(S+17)/2\rceil}m^4e^{4m}.
\tag{5.3}
$$

这里的 $\Xi$ 是高度两-jet 定义的 canonical 量。数值 worker 的 connection momentum $\Pi$ 在非线性阶不同，不能把 checkpoint 的第二半向量直接改名为 (5.2)。新 endpoint wrapper 会另外输出实际 root 上的 $\Xi=fL_{\ne0}$ 与 $\Pi-\Xi$。

## 6. 更深 cell 的平衡传递界

以下用精确矩阵 ODE，未作时间离散。设

$$n\ge64,\qquad m^4\sqrt{\delta_n}\le2^{-16}.$$

令 $\nu=m^2(m^2-1)/12$。在 $(Q,\Xi/\nu)$ 坐标中，cell 内 canonical 系统的生成元是

$$
\begin{pmatrix}d&a\nu\\b/\nu&-d\end{pmatrix},\quad
d=(m^2-4)r_x/r,
$$
$$a=\sqrt{12}\mu r_x/(r^8w),\qquad
b=-\nu\sqrt{12}r_xr^6w/\mu.
\tag{6.1}
$$

cell 末的 raw 归一再乘 $\operatorname{diag}(1,2^{-11/4})$，不增加此范数。

### 6.1 六个短段

先取自由 warp 部分 $r_x\le162(r_o)_x$。在每个短段上，用 $p_*\in[\delta/2,64/\delta]$、$\eta\le(2/3)\delta^{3/2}$ 和 $(r/r_o)^6<17/16$，上三角项积分至多 $216\nu\sqrt\delta$，下三角项至多 $7344\sqrt\delta$。对角项也可吸收到 $2^{13}\nu\sqrt\delta$ 的总界中。

曲率项 $|w_x|/8$ 在**整个 cell**的贡献可直接按变差积分，分别满足

$$
\int |a\nu|_{\rm curv}
\le2^{19}\nu\delta^{11/4}V_n,
\quad
\int |b/\nu|_{\rm curv}\le2^{33}\delta^{3/4},
$$
$$\int|d|_{\rm curv}\le2^{25}m^2\delta^{7/4}.
$$

这里例如第二式来自
$\int w|dw|\le W_n\operatorname{TV}(w_n)\le4W_n^2$，不是使用无法认证的导数采样最大值。由 $\nu<m^4/8$、上述 mode 条件及 $\delta<2^{-71}$，三项总和小于 $2^{-19}$。所以六个短段生成元范数积分之和小于

$$6\,2^{13}\nu\sqrt\delta+2^{-19}
\le1/16+2^{-19}<1/8.$$

它们的总指数因子小于2。

### 6.2 三个平台

每个平台保留一项 dominant shear：第一个高峰的下三角、谷值的上三角、第二个高峰的下三角。其绝对积分依次满足

$$S_1<2^{14},\qquad S_2<2^9\nu,\qquad S_3<2^8.$$

具体地，自由 warp 部分依次至多
$162(17/16)64=11016$、$324\nu$、$162(17/16)<173$；曲率项由上一小节及平台 $\operatorname{TV}(\log w)<3\delta$ 吸收。

把其他项记为 $E_i(x)$。对角项的积分至多 $55m^2\delta$。高平台的非 dominant 上三角项至多 $163\nu\delta^2$；谷平台的非 dominant 下三角项至多 $346\delta^2$。为明确曲率部分也已计入：它们分别可用
$2^{24}m^2\delta^{11/4}$、$3\,2^{19}\nu\delta^{15/4}$、$2^{23}\delta^{23/4}$ 控制；在 $n\ge64$ 分别小于已增加的 $m^2\delta$、$\nu\delta^2$ 和 $\delta^2$。

因此统一有

$$\int\|E_i(x)\|_1dx\le2^8m^4\delta.$$

单一 shear 的任意子区间传播范数不超过 $1+S_i$。直接对 variation of constants 用 Gronwall，实际平台传播范数至多

$$
(1+S_i)\exp\left((1+S_i)\int\|E_i\|\right).
$$

三项指数之和至多 $3\,2^{20}m^8\delta\le3\,2^{-12}<1/8$，所以额外因子小于2。又

$$
(1+S_1)(1+S_2)(1+S_3)
\le(16385)(513)(257)\nu<2^{32}\nu.
$$

连同短段得完整 warped cell 界

$$\boxed{\|T_{m,n}\|_{\rm bal}<2^{34}\nu.}
\tag{6.2}
$$

对 $n\ge160$ 的 unwarped source，上面的自由 warp 系数改为1且没有曲率项。三个 dominant shear 依次为 $64,\alpha_n\nu,1$；乘积至多 $390\nu<2^9\nu$。相同余项预算更小，故宽松地有

$$\boxed{\|T_{m,n}\|_{\rm bal}<2^{14}\nu\quad(n\ge160).}
\tag{6.3}
$$

这一步避免用每层的粗物理能量界叠出不可支付的 $\exp(O(n^2))$。

## 7. 全部未表示高模的有限账本

对 $m\in[2^k,2^{k+1})$，取

$$N_k=\min(225,8k+33),\qquad S_k=N_k-1.$$

对第一个区间只取 $94\le m<128$；$m\ge2^{24}$ 用同一个 $S=224$ 的全能量块。若 $N_k\le224$，则其后每个 cell 均满足
$m^4\sqrt\delta<2^{-16}$，故可以使用 (6.2)–(6.3)。

记 $u_k=\max(0,160-N_k)$、$v_k=225-\max(160,N_k)$、$p_k=4(1+u_k+v_k)$。由 $\nu<m^4/8$，总传播界为

$$
2^{B_k}m^{p_k}e^{4m},\quad
B_k=A_{S_k}+\lceil(S_k+17)/2\rceil+31u_k+11v_k.
$$

从输入角宽128到输出角宽1，尚有净指数 $e^{-123m}<2^{-175m}$。因此 (2.1) 的输出至多

$$2^{-3167+B_k-175m}m^{p_k}.$$

每个 bin 内这个量递减：$p_k\le580$、$m\ge94$、$175\log2>175/2$。只需比较19个左端点。第一个 bin 有

$$S=80,\quad u=79,\quad v=65,\quad
A_S=11730,\quad B=14943,\quad p=580,$$

且精确整数比较 $94^{580}<2^{3802}$ 给

$$-3167+14943-175\cdot94+3802=-872.$$

其他18项都更小；对最终无界 bin，单调性同样覆盖其整个余尾。这19项取的是对角 Fourier 算子的加权 $\ell^1$ 算子范数之 supremum，统一乘 (2.1) 的总输入 $\ell^1$ 质量，因此无需把19个最坏上界再累加。全部比较保存在
`computations/closure_wide_strip_head_ledger.py` 与
`notes/2026-11-12-closure-wide-strip-head-ledger.json`。该脚本只用整数/有理数认证这些常数，不运行 ODE。于是得到 (1.2)。

## 8. 当前实际接口及仍须支付的项

用旧的有限线性 ray 数据，仅作预算诊断时，同一 q003 低频标签在 $\tau_F=128$ 的 norm 对数约为 $-1972.50468$，比宽图门 $-1947$ 多25.5bit余量。它仍是旧 finite-linear 诊断；不能当成将来 depth12 的实际低46深参数，也不能据此把额外低模和高模浅高度强设为0。

depth12 的实际输出现已提供：实际 $Q$、非线性 connection $\Pi$、由完整 finite root 转出的 canonical $\Xi$、两者差量，以及160个固定源参数。有限源范围条件已按 §1 核销。实际端点接未认证线性延拓的保留 M8 标签在 $\tau_F=128$ 上为 $\log_2\ell^1\approx-1972.5047301080194$；这仍不覆盖未保留的低9–46模、头内非线性或真实源积分误差，不能据此单独断言完整 R18 图域条件已付。

本引理已经把“宽 strip 可能帮助高频”变成一个具体全频传递界。它尚未处理：

1. 线性头近解内部产生的完整非线性 forcing 及其反馈；这是下一个实际数学误差项。
2. 低46浅高度与深参数之间的实际非线性匹配及其反函数。高频浅 trace 必须作为输出进入前缀联解。
3. 实源求积、线性/非线性积分和有限角 root 的数值误差。上述 exact-linear 证明不把浮点一致性改称这些误差的界。

因此 (1.2) 不能单独成为固定 g 的完整非线性 DN 或闭合证明；它精确支付的是其中一项以前没有可用界的高频深端误差。
