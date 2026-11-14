# R133 续篇：新互逆图的完整连续残差及紧支度量三阶系数

2026-11-13，visible-exact / root。

**状态：已证明。** 本文给出适用于实际完整 dyadic 三次 Fourier 候选的连续残差包络方法，覆盖闭径向单元与整个实角圆；保留原目标的无限角尾、紧支度量参数、全部三次乘积频率及候选接口跳量。文末严格实例仅覆盖新 $\alpha=.70$ 候选最前面的三个闭单元。没有据此断言整个主体已验证，亦没有断言无限维逆、精确非线性解或最终闭面存在。

## 1. 同一完整目标与稳定半径消去

原目标是对象
`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json`，SHA256 为
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。
固定原准确参数（本次半宽为零），并取新的公共度量

$$
 g_\nu=E_\nu\,dr^2+a^2\,d\theta^2,
 \qquad E_\nu=E\exp(\nu h),
 \qquad h=4096t^6(1-t)^6,
 \quad t=(r-1/20)/(13/100),
 \tag{C.1}
$$

其中 $h$ 在 $(1/20,9/50)$ 外为零。本实例
$\nu=-8203900476603349/288230376151711744$。
它是已经明确登记的新度量；旧固定 $g_0$ 的精确存在结论没有被转授。

令 $P$ 为原完整单位 primitive，在其原旋转正交基中写

$$
 L=a'/a,\quad H=z'/a^2,\quad u=LP+P_r,
 \quad e=2L\langle u_x\rangle+\langle u\cdot u\rangle.
$$

这里 $u$ 仅用于计算目标能量，与互逆曲率变量不同。
原 primitive 的竖直零模恒为零，因此准确地有

$$
 \bar E:=E/a^2=L^2+a^2H^2+e.
 \tag{C.2}
$$

把 $K=-a''/(aE)+a'E'/(2aE^2)$ 先作代数消去，得到

$$
 K=\frac{N}{\bar E^2},\qquad
 N=H^2(L^2-L')+LHH'+\frac{Le'-2L'e}{2a^2}.
 \tag{C.3}
$$

故新图的四个实际标量系数为

$$
 \gamma_\nu=\sqrt{G},\quad \beta=L,\quad
 K_\nu=\left(K+\frac{L\nu h'}{2a^2\bar E}\right)e^{-\nu h},
 \quad s_\nu=-\sqrt{G/R},
 \tag{C.4}
$$

$$
 G=\bar E e^{\nu h},\qquad
 R=H^2+e/a^2+(\bar E/a^2)\operatorname{expm1}(\nu h).
 \tag{C.5}
$$

确实 $\gamma_\nu=\sqrt{E_\nu}/a$，
$R=(E_\nu-a'^2)/a^4$，且
$s_\nu=1/C_{\rm ref,\nu}=-a\sqrt{E_\nu}/\sqrt{E_\nu-a'^2}$。
这在 $K_\nu$ 穿零时仍成立，只要求实际 $a,G,R$ 为正；没有使用
$\sqrt{-K_\nu}$。计算先消去半径幂，再取区间平方根，避免以两个近等的大数相减重建正帽缺口。

`fourfold_codazzi_reciprocal_compact_target_jets.py` 在每个原完整标量 germ 内形成上述 Taylor jet。
原 `CubicCodazziTarget.unit_finite_data` 给出六阶 primitive 数据；原
`unit_tail_errors` 给出的完整角尾在原复径向半径 $\rho$ 上有效，因此第 $j$ 个径向导数尾为
$j!\varepsilon/\rho^j$。若 $M_i$ 是有限 $u^{(i)}$ 的每个分量 $A^0$ 上界、
$\varepsilon_i$ 为每分量完整尾，则均值积的遗漏项由

$$
 3(M_i\varepsilon_j+M_j\varepsilon_i+\varepsilon_i\varepsilon_j)
 \tag{C.6}
$$

控制。零模线性项另付 $2|L^{(i)}|\varepsilon_j$，再按 Leibniz 二项式系数求和。
由此得到 $e^{(0)},\ldots,e^{(4)}$ 的完整包络。(C.2)–(C.5) 的截断幂级数运算遂给出
$\gamma_\nu,\beta,K_\nu,s_\nu$ 的实际零至三阶导数。所需每个导数都已由原六阶 primitive 及其 Cauchy 尾支付。

另用原未消去的完整 $a,E$ 及零至四阶能量 jet，直接在
$r=0,3/40,23/200,17/100,2/5,3/2$、$\nu=0$ 和上述准确 $\nu$ 处计算
$-a''/(aE_\nu)+a'E_\nu'/(2aE_\nu^2)$ 等原式。
12 组、每组 16 个实际系数包络全部相交，记录见
`notes/2026-11-13-R133-reciprocal-compact-target-direct-identity-v2.json.gz`。
这是对本次新半径消去实现及紧支变换的必要核对；数学恒等式由上面的代数证明。
首版因漏传旧构造器的 `angles` 参数在计算前退出，原源文件及失败记录也保留，没有算成任何系数验证。

## 2. 完整多项式方程与候选

采用[完整互逆多项式图](R133-supplement-polynomial-Codazzi-chart-and-complete-boundary.md)的变量

$$
 u=\alpha U,\quad v=s_\nu+\alpha V,\quad B=u/v,\quad C=1/v.
$$

实际归一化方程是

$$
 U_r=\gamma_\nu(\alpha UU_\theta+K_\nu vV_\theta)
      -\beta U(1+\alpha^2U^2+K_\nu v^2),
 \tag{C.7}
$$

$$
 V_r=\gamma_\nu(\alpha UV_\theta-vU_\theta)
 +\beta\{V-K_\nu(3s_\nu^2V+3\alpha s_\nu V^2+\alpha^2V^3)
                   -\alpha vU^2\}.
 \tag{C.8}
$$

输入候选使用全部保存的三次系数、全部 $M$ 个正频率及 $V$ 的均值。
每个 binary64 数解释为其准确 dyadic 实数，不能把候选自带的浮点误差界当作输入不确定性而丢掉。
径向划分同时包含原三次节点、原标量 germ 端点和紧支 bump 的两个端点；
任何闭单元都不跨过这些接口。

在单元 $I=[c-d,c+d]$ 上令 $x=(r-c)/d\in[-1,1]$。
候选本身及其实际径向、角向导数被准确平移为 $x$ 的多项式。
每个真实标量系数 $a(r)$ 则取

$$
 a(r)=a(c)+d a'(c)x+\tfrac12d^2a''(c)x^2+x^3\xi(r),
 \qquad \xi(r)\in\tfrac16d^3 a'''(I).
 \tag{C.9}
$$

$\xi(r)$ 可以随 $r$ 变化，下面的误差代数不要求它是常数。

## 3. $A^0$ 误差预算及全频残差

记 $\|f\|_{A^0}=\sum_k|\widehat f_k|$，物理角频率为 $4k$。
对一个有限参考多项式 $p(x,\theta)=\sum_jp_j(\theta)x^j$，保存三件数据：
其全部 dyadic 系数、$M_p\ge\sum_j\|p_j\|_{A^0}$、以及真实对象与它的统一误差
$\varepsilon_p\ge\sup_{x\in[-1,1]}\|f(x)-p(x)\|_{A^0}$。
候选的每个正弦/余弦系数及 (C.9) 的每个标量系数从其有向区间内选取一个 dyadic 中心；
完整偏差另计入 $\varepsilon_p$，没有忽略第三阶系数的不确定性。

$A^0$ 的乘法闭性给出准确的传播规则

$$
 M_{pq}\le M_pM_q,\qquad
 \varepsilon_{pq}\le M_p\varepsilon_q+M_q\varepsilon_p+
                         \varepsilon_p\varepsilon_q.
 \tag{C.10}
$$

加法则逐项相加。把 (C.7)–(C.8) 完整代入此代数，得到有限残差参考多项式
$P_U,P_V$ 及两个完整误差 $\varepsilon_U,\varepsilon_V$。
该规则直接证明即使 (C.9) 的余项随 $r$ 变化，所得误差仍在全部闭单元上成立。
它也避免把同一个标量区间误差经角点值 FFT 人为重复收取许多次。

有限参考残差的角频率准确支持于 $|k|\le3M$。
选择二幂角网格 $N>6M$，有向 FFT 因而准确包络其每个 Fourier 系数，且无三次乘积混叠。
只有在数学上确实不存在的 $|k|>3M$ 被设为零；程序另检查这些数值区间含零。
所有保留及未保留的 $M<|k|\le3M$ 项都求和。
若 $P_j$ 为各径向幂系数，则全单元残差满足

$$
 \sup_{r\in I}\|R_U(r)\|_{A^0}
 \le\sum_j\|(P_U)_j\|_{A^0}+\varepsilon_U,
 \qquad
 \sup_{r\in I}\|R_V(r)\|_{A^0}
 \le\sum_j\|(P_V)_j\|_{A^0}+\varepsilon_V.
 \tag{C.11}
$$

系数的平移、角 FFT、乘积、绝对值及归约求和使用现有有向 `Box/CBox` 运算，
标量级数与范数预算使用 192 位 Arb；每条最终上界取向上的端点。
上述证明的对象始终是完整真实目标与准确 dyadic 候选，网格只用于无混叠的有限系数运算。

## 4. 整个角圆的图缺口及实际接口

各有限角多项式在角网格中心取其有向函数值和一阶导数，
再用完整二阶 Fourier 范数 $\|\partial_\theta^2p_j\|_{A^0}$ 支付半格 Taylor 余项。
物理角半格为 $\pi/(4N)$。
在径向 $x\in[-1,1]$ 上作区间 Horner 后，得到完整闭角胞覆盖的 $v$ 上下界。
若 $v\le-g<0$，则整个单元上

$$
 |C|\le g^{-1},\qquad |B|\le|\alpha|\|U\|_\infty/g.
 \tag{C.12}
$$

原浮点 PPoly 相邻片的端值可能有小而非零的跳量。
程序用原准确 dyadic 节点差作有向 Horner，对所有频率及均值计算
$\|[U]\|_{A^0},\|[V]\|_{A^0}$ 并分别求和；没有把它们改写成零。
后续任何积分误差或 Newton 消费器仍须支付这些跳量。

## 5. 本次实际连续计算的范围

输入为完整已推候选
`notes/2026-11-13-R133-reciprocal-m128-alpha070-full-QR-candidate.json`，SHA256
`53b1fd54a20f6ab9edea521781ed8bece7d169949cf59a969b7c01e2370d2f71`。
其全部三 shards、$M=128$、准确
$\alpha=3152519739159347/4503599627370496$ 保留。
使用 $N=1024$、原 primitive 网格 512、192 位 Arb，运行
`fourfold_codazzi_reciprocal_continuous_residual_v3.py --first 0 --count 3`。

这三片准确覆盖

$$
 0\le r\le1080863910568919/576460752303423488,
$$

并给出严格宽松值

$$
 \sup\|R_U\|_{A^0}<3.645\cdot10^{-5},\qquad
 \sup\|R_V\|_{A^0}<2.330\cdot10^{-6},\qquad
 -v>0.1927131974.
 \tag{C.13}
$$

累计实际接口跳量分别小于 $1.462\cdot10^{-17}$、$1.069\cdot10^{-15}$。
原生完整记录为
`notes/2026-11-13-R133-reciprocal-alpha070-three-cell-continuous-residual-v3.json.gz`，其中保存每片的目标三阶 jet、完整径向幂残差、全误差费用、图缺口及全部依赖 SHA。

首版 v1 因 `Box` 构造器误用在第零片退出，零片通过；v2 修正类型后获得同三片的有效较宽包络。
v3 使用 (C.10) 支付共用标量误差，改进费用传播而不改变方程、候选、参数或验证范围。
三版源文件与原始 true/false 记录都保留。

总主体划分有 1613 片，本次只支付其中三片。
即便将来完成全部连续残差，仍必须有同一新度量的完整无限维逆和非线性误差闭合，
以及真实帽、尾、握持区和全像几何预算，才能满足题 README 的最终标准。
