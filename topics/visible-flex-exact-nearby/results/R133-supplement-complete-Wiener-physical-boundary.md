# R133：互逆候选的完整 Wiener 商与真实物理边界

**已证明（完整无限 Fourier 商和指定边界的有向包络）。** 对已保存的互逆
多项式候选，有限 Laurent 多项式 $W$ 的完整卷积残差 $1-vW$ 严格小于1，
因此物理 $B=\alpha U/v$、$C=1/v$ 的全部频率、均值及两次角导均有真实包络。
这个结论不要求粗估计 $\|\alpha V/s\|_{A_0}<1$。

已实际消费 $\alpha=.70$ 的完整128模新候选：腰和 $r=3/2$ 两处的严格残差分别
小于 $9.022\cdot10^{-15}$ 和 $4.209\cdot10^{-15}$。在 $r=3/2$，整个
真实物理 $\zeta=(C-C_r)_{\ne0}$ 满足

$$
\|\zeta\|_{A_0}<1.303458\cdot10^{-5}<2\cdot10^{-5},\qquad
\|\partial_\theta^2\zeta\|_{A_0}<.000208558.
\tag{W.1}
$$

这已经严格进入[真正小输入周期帽](R133-supplement-universal-small-inner-periodic-cap.md)
的完整输入域，包含无限高频，并非有限角网格上的小量。对独立
$\|f_B\|_{\dot A^2_\sigma}\le2^{-60}$，该真实帽与候选的另一物理迹、mean
失配分别有上界

$$
\|b_{\rm cand}-b_{\rm cap}\|_{A_0}<8.920725\cdot10^{-8},\qquad
|c_{0,\rm cand}-c_{0,\rm cap}|<4.786544\cdot10^{-9}.
\tag{W.2}
$$

这些是完整匹配残差，不是零等式；主体内部 PDE、整个主体逆及远端 label 方程
仍须独立闭合。

## 1. 有限多项式选择与严格无限逆

在指定真实径向点上，候选 $U,V$ 是以完整精确 dyadic 系数解释的有限 Fourier
多项式，物理频率为 $4j$。记

$$
v=s+\alpha V,\qquad s=1/C_r<0,
\qquad \|f\|_{A_0}=\sum_{j\in\mathbb Z}|\widehat f_{4j}|.
\tag{W.3}
$$

$s$ 使用真正目标的有向 primitive 和全部无限尾计算。选取任意有限 Laurent
多项式 $W$，定义

$$
e=1-vW,\qquad E_j=\|\partial_\theta^j e\|_{A_0}\ (j=0,1,2).
\tag{W.4}
$$

**引理。** 若 $E_0<1$，则 $v$ 在 Wiener 代数中可逆，且

$$
v^{-1}=W\sum_{n=0}^{\infty}e^n,\qquad
I_0:=\frac{\|W\|_{A_0}}{1-E_0}\ \ge\ \|v^{-1}\|_{A_0},
\tag{W.5}
$$

$$
I_1:=I_0^2\|v_\theta\|_{A_0}\ \ge\ \|(v^{-1})_\theta\|_{A_0},
$$
$$
I_2:=2I_0^3\|v_\theta\|_{A_0}^2+I_0^2\|v_{\theta\theta}\|_{A_0}
\ \ge\ \|(v^{-1})_{\theta\theta}\|_{A_0}.
\tag{W.6}
$$

若 $R=v^{-1}-W$，则

$$
\begin{aligned}
\|R\|_{A_0}&\le T_0:=I_0E_0,\\
\|R_\theta\|_{A_0}&\le T_1:=I_1E_0+I_0E_1,\\
\|R_{\theta\theta}\|_{A_0}&\le T_2:=I_2E_0+2I_1E_1+I_0E_2.
\end{aligned}
\tag{W.7}
$$

**证明。** $A_0$ 是含单位的交换 Banach 代数，故 $1-e=vW$ 由完整 Neumann
级数可逆。明确乘法 $v[W(1-e)^{-1}]=1$ 直接给 (W.5)，不需要另外假设
$W$ 没有零点。特别地 $v$ 在整个真实角圆上不为零。

为避免先验正则循环，先用角平移：$v$ 是有限多项式，平移轨道在 $A_0$ 中
是 $C^\infty$；Banach 代数可逆映射在可逆元开集中光滑。因此 $v^{-1}$ 的
平移轨道也具有两次强导，逐 Fourier 坐标识别出真实角导。对
$v^{-1}v=1$ 求导得

$$
(v^{-1})_\theta=-v^{-2}v_\theta,\qquad
(v^{-1})_{\theta\theta}=2v^{-3}v_\theta^2-v^{-2}v_{\theta\theta},
$$

由 Banach 代数不等式得到 (W.6)。最后 $R=v^{-1}e$，逐次使用 Leibniz 公式
得到 (W.7)。以上每个和都保留无限频率。证毕。

这里完整 $A_2$ 权若取 $(1+|m|)^2$，则

$$\|v^{-1}\|_{A_2}\le I_0+2I_1+I_2.
\tag{W.8}$$

故本篇没有混淆齐次 $m^2$ 权和非齐次 $(1+|m|)^2$ 权。

## 2. 全物理场、均值和未保留 Fourier 尾

令

$$
B^p=\alpha UW,\qquad C^p=W,\qquad c^p=W-C_r,
\quad b^p=i\operatorname{sgn}(D)B^p.
\tag{W.9}
$$

这些都是准确有限 Laurent 多项式；但真实 $B,C$ 并未被声明有限。
由 (W.7)，

$$
\|B-B^p\|_{A_0}\le T_B:=|\alpha|\|U\|_{A_0}T_0,
\qquad \|C-C^p\|_{A_0}\le T_C:=T_0.
\tag{W.10}
$$

例如对保留 $|m|\le4M$ 的投影，完整尾满足

$$
\|(I-P_M)B\|_{A_0}\le\|(I-P_M)B^p\|_{A_0}+T_B,
$$
$$
\|(I-P_M)(C-C_r)\|_{A_0}
\le\|(I-P_M)c^p\|_{A_0}+T_C.
\tag{W.11}
$$

$C$ mean 的整个误差至多 $T_C$。由原候选 $U$ 实奇、$V$ 实偶，$v^{-1}$ 实偶，
所以 $B_0=0$ 准确成立。该反射恒等式不等于 $B(0,\theta)=0$；有限候选腰的
每个非零 $U$ 系数仍被保留在实际边界残差中。

角二导的全部物理误差由 (W.7) 和乘积公式直接给出；程序同时保存

$$
\begin{aligned}
\|B\|_{A_0}&\le |\alpha|U_0I_0,\\
\|B_\theta\|_{A_0}&\le |\alpha|(U_1I_0+U_0I_1),\\
\|B_{\theta\theta}\|_{A_0}&\le |\alpha|(U_2I_0+2U_1I_1+U_0I_2),
\end{aligned}
\tag{W.12}
$$

其中 $U_j=\|\partial_\theta^jU\|_{A_0}$。没有有限角差分或微分截断。

最后，$|1/v|\le I_0$ 给整个实角圆上的严格分母下界 $|v|\ge1/I_0$。
实际用完整有限多项式在一个角点验证 $v<0$；连续性和无零点就给全角 $v<0$。
因此负 $C$ 图也已严格验证，而非仅采样验证。

## 3. 真 q、有限近似 q 和真正非线性帽同时消费

取[真实帽 q 向量](R133-supplement-actual-cap-cut-q-vector-and-full-frequency-budget.md)
中的 $\widetilde q_m,\epsilon_m$ 和完整上界 $Q=53/50$。对所有保留正负模定义

$$
\begin{aligned}
E_{\rm nom}&=\sum_{0<|m|\le4M}|b^p_m+\widetilde q_m c^p_m|,\\
E_q&=\sum_{0<|m|\le4M}\epsilon_m|c^p_m|,\\
E_{\rm tail}&=\sum_{|m|>4M}(|B^p_m|+Q|c^p_m|).
\end{aligned}
\tag{W.13}
$$

由于真正 $q$ 的完整 multiplier 范数至多 $Q$，所有无限模式满足

$$
\|b+qc\|_{A_0,\ne0}\le
E_{\rm nom}+E_q+E_{\rm tail}+T_B+QT_C.
\tag{W.14}
$$

程序先计算完整有限卷积，再逐系数求 (W.13)，未交换角点 sup 和 Fourier 和。
$q$ 的有向区间及指数小 regular 费用均取同一对象的完整证书，$\widetilde q$
只当作精确 dyadic 近似中心。

若 $\zeta=c_{\ne0}$ 还满足整个 $A_0$ 小球门和 (W.8) 的 $A_2$ 正则，则真正
周期帽的图为 $b_{\rm cap}=-q\zeta+\mathcal N(\zeta,f_B)$、
$c_{0,\rm cap}=\mathcal M(\zeta,f_B)$，其中统一真界

$$
\|\mathcal N\|_{A_0}<1.663187\cdot10^{-8},\qquad
|\mathcal M|<4.636375\cdot10^{-9}
\tag{W.15}
$$

适用于独立 $\|f_B\|_{\dot A^2_\sigma}\le2^{-60}$。将 (W.15) 加到
(W.14) 和完整 mean 误差，才得到真正帽匹配残差。没有把 $\mathcal N$、
$\mathcal M$ 或独立 $f_B$ 当作零。

## 4. 本次实际完整算术

指定候选为
`notes/2026-11-13-R133-reciprocal-m128-alpha070-full-QR-candidate.json`，
全部3个无损分片先按原 SHA、精确节点接缝和完整形状读入。本次固定

$$
\alpha=\frac{3152519739159347}{4503599627370496},\qquad
\nu=-\frac{8203900476603349}{288230376151711744},\qquad \eta=0.
\tag{W.16}
$$

没有把十进制 `.70` 另作不同有理数，也没有声称这次候选在全部 $\eta$ 上
统一存在。$s$ 的真正 point provider 保留512节点表示以外的全部原 primitive
尾以及有向算术。在腰部另使用准确恒等式 $s=-a$，因为 $a'(0)=0$。

有限 PPoly 每个保存的 IEEE 系数和节点先转换为准确 Fraction，再在指定有理
$r$ 上用精确 Horner 求迹；内部接缝取报告标明的右片。此处只证明两个指定
径向点，不借此声称径向 piece 已连续。

每处先用8192点浮点 FFT **选择** degree1024 的实偶 $W$。选择后把所有系数
解释为精确 dyadic 数并保存在原生报告内。随后 $1-vW$ 的全部 degree1152
正负 Laurent 系数由320 bit Arb/acb 完整多项式乘法形成。FFT 的任何取整、
混叠或截断误差都无需假定：无论它选出什么 $W$，真正残差都会完整进入 (W.4)。
原生计算保留全部中间有向球，不把端点中点当上界。

向外舍入的主要结果如下：

| 完整量 | 腰 $r=0$ | 真帽切口 $r=3/2$ |
|---|---:|---:|
| $\|1-vW\|_{A_0}$ | $<9.022\cdot10^{-15}$ | $<4.209\cdot10^{-15}$ |
| $\|v^{-1}-W\|_{A_0}$ | $<4.679\cdot10^{-14}$ | $<8.207\cdot10^{-16}$ |
| 全角 $|v|$ 下界 | $>.1928416507809$ | $>5.1288860274301$ |
| 全 $\|(C-C_r)_{\ne0}\|_{A_0}$ | $<4.249914196$ | $<1.303458\cdot10^{-5}$ |
| 全 $|c_0|$ 上界 | $<4.174330\cdot10^{-10}$ | $<1.501690\cdot10^{-10}$ |
| $|m|>512$ 的完整 $c$ 尾 | $<3.671878\cdot10^{-5}$ | $<1.121467\cdot10^{-15}$ |

腰部表中大 $c$ 不是小帽输入；它说明互逆有限坐标的完整物理曲率谱确实含
未保留模。腰部另得全 $B$ 小于 $2.124402\cdot10^{-23}$、归一化第四 cosine
行误差小于 $1.344558\cdot10^{-13}$。实际腰 mean 并非零：

$$
4.1733858\cdot10^{-10}
<\langle C(0)\rangle+1/a(0)
<4.1743294\cdot10^{-10}.
\tag{W.17}
$$

因此这份 finite candidate 没有被宣称已经满足准确总转角/周期闭合。

在 $r=3/2$，(W.14) 的各项实际为

$$
\begin{aligned}
E_{\rm nom}&<1.005029\cdot10^{-10},\\
E_q&<7.247488\cdot10^{-8},\\
E_{\rm tail}&<3.188934\cdot10^{-16},\\
T_B+QT_C&<8.699332\cdot10^{-16}.
\end{aligned}
\tag{W.18}
$$

所以真实线性边界上界小于 $7.257538\cdot10^{-8}$，加上真正非线性帽得到
(W.2)。当前主费用是已经明确保留的 $q$ 向量有向宽度，不是无限 Fourier
商尾；若后续逆预算需要进一步缩小它，应重新细分真正 scalar 盒或作严格
径向高阶传播，不能用浮点 $q$ 代替。

## 5. 文件及适用范围

- `scripts/fourfold_codazzi_reciprocal_Wiener_boundary.py`：完整 Fraction 迹、有限
  $W$ 选择、全卷积有向逆、全角导和真帽边界消费；
- `notes/2026-11-13-R133-reciprocal-m128-alpha070-Wiener-boundary-native.json.gz`：
  两个真实径向点的完整报告、全部 $W$ 系数、输入及目标源 SHA。

在课题目录执行该脚本的 `--candidate`、`--out` 即可；`--radii` 可明确选择
其他已有候选覆盖内的指定点，目标 provider 当前限制 $0\le r\le3/2$。
任何新候选须重新支付自己的完整卷积和实际目标参数。本次只确认真实边界
对象及其完整差额，没有授予主体全频逆、跨型 Cauchy 存在、全域嵌入或最终闭面。

## 6. 实际 M256、alpha=.75 已接受检查点的同一完整切口消费

同一脚本还实际消费了
[137退出记录中无损恢复的首个完整检查点](../notes/2026-11-13-R133-reciprocal-m256-exit137-and-complete-resume.md)。
该候选没有原完整有限收敛结论，本篇不改变这个状态；仅把其指定物理边界作为
准确函数。完整恢复索引 SHA 为
`45923b3675d2789376361192c6e0841e82914e27605d362872d5ac1dcf7a628e`，
其原 accepted checkpoint SHA 为
`af0a3f5fabd4d8d1194f30ff942130040e62975c0963f127c9ae864f7bd9521a`。
使用全部256模、$\alpha=3/4$、
$\nu=-2443457753738987/72057594037927936$、$\eta=0$。

在 $r=3/2$，实际完整卷积给

$$
E_0<3.9350\cdot10^{-15},\quad T_C<7.672275\cdot10^{-16},\quad
|v|>5.1288552897771,
$$
$$
\|\zeta\|_{A_0}<1.420305\cdot10^{-5}<2\cdot10^{-5},\qquad
\|\partial_\theta^2\zeta\|_{A_0}<.000227253.
\tag{W.19}
$$

因此这个实际已接受状态的**完整物理内迹**也已真入统一周期帽域。对同一独立
$f_B$ 域，其完整另一迹和 mean 失配有界于

$$
\|b_{\rm cand}-b_{\rm cap}\|_{A_0}<9.571855\cdot10^{-8},\qquad
|c_{0,\rm cand}-c_{0,\rm cap}|<4.815042\cdot10^{-9}.
\tag{W.20}
$$

原生数据为
`notes/2026-11-13-R133-reciprocal-m256-alpha075-accepted000-Wiener-cut-native.json.gz`，
保存全部有限 $W$ 系数和真正无限商预算。原 accepted 状态的再生入口、参数和
哈希由上述过程记录给出；没有重复提交可再生的大候选，也没有把进程137改写
成数学成功。
