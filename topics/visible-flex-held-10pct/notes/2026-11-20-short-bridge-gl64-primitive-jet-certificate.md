# 短桥有限求积的 primitive jet 证书与末端解析延拓

维护：Astra-held10-1b6d88ec-20261120 / n4_continue。2026-11-20 UTC。

## 已支付的量与对象

本条处理当前 port、curvature=4、peak_fraction=.2 的 ShortBridge。固定实际程序返回的 binary64 节点、权重、peak、eps 和段长；对末段明确采用相位 $p-eu^2$ 的**解析延拓**到实际物理 end，不用上端 clip。用真实三角函数解释这个有限规则，和真实 primitive 比较。已实际执行精确有理矩及外向区间计算，归一化域为

$$0\le u\le U=1+10^{-12}.$$

当前已过原有限 metric 门的 M24 linear 场满足：

| 比较 | 0 阶界 | 物理 1 阶界 | 物理 2 阶界 |
|---|---:|---:|---:|
| 字面参数的有限规则与真 primitive，sin | $2.445\,10^{-13}$ | $7.987\,10^{-12}$ | $2.778\,10^{-10}$ |
| 同上，cos | $2.454\,10^{-13}$ | $8.003\,10^{-12}$ | $2.777\,10^{-10}$ |
| 端点拉回后与 R59 真参考，两 trig 均可用 | $7.451\,10^{-12}$ | $8.005\,10^{-12}$ | $2.779\,10^{-10}$ |

表中都是严格上界；最后一行是各解析段及接头单侧 jet 的比较。**有限 GL 曲段和平台之间的小 jet 跳跃仍需共享 jet 重建，不能自动称全局 $C^2$。** 若改用真正 primitive，则各曲段本身已是解析函数；其接头及字段重建仍必须使用明确共享 jet。

本文也付了源的字面 clip 与所选解析延拓之间的半径**值**差、以及源手填 geo jet 与解析相位之间的差。没有宣称字面 clipped 位置函数的真实导数在末端与延拓导数很接近。

可执行源为
[certify_short_bridge_quadrature_jet_gap.py](../scripts/resume_n4/certify_short_bridge_quadrature_jet_gap.py)。
完整可再生输出留在 scratch；源、本文和
[紧凑执行记录](2026-11-20-short-bridge-gl64-jet-execution.json)
保存输入/源/输出绑定。没有运行新 BVP 或尾 Newton。

## 1. 冻结参数、真实函数和有限规则

实际恢复的 [root_short_bridge.py](../../visible-flex-larger-amplitude/computations/root_short_bridge.py) SHA256 为
7e00a3336a302ba94c751c09e6f75749d6973c86605269538c8f0b44c60779b4。

记字面参数 $p=\mathrm{peak}$、$e=\mathrm{eps}$。初始和末段相位分别为

$$
\phi_0(u)=p(3u^2-2u^3),\qquad
\phi_2(u)=p-eu^2.
$$

原程序产生 64 个 binary64 数 $g_i,\omega_i$。把实际计算的
$t_i=\mathrm{fl}((1+g_i)/2)$ 和 $w_i=\omega_i/2$ 视为精确有理数，定义

$$
Q_f(u)=u\sum_{i=1}^{64}w_i f(\phi(ut_i)),
\qquad
I_f(u)=\int_0^u f(\phi(v))\,dv,\qquad f=\sin,\cos.
\tag{1}
$$

这是有限规则的连续实函数解释，不是随输入离散舍入的浮点映射。平台的 math.sin(p)、math.cos(p) 返回数也作为字面常数，分别与真实三角值作外向比较。实际 libm/numpy 点值的舍入误差没有被假定为零；本文的证书可以用作它们所近似的连续对象之定义与误差预算，真正点值 oracle 另用外向求值。

R59 参考使用同一组字面 cut 数据，之后用真实 elementary operations、curvature=4 和精确 $1/5$ 定义相位及真积分段长。没有修改 cut、谷参数或目标物理参数来增大比例。

## 2. 精确矩与 Taylor 余项

逐项精确计算

$$
\mu_j=\sum_iw_it_i^j-\frac1{j+1},\qquad0\le j\le84.
$$

将 $\sin\phi$、$\cos\phi$ 关于 $\phi$ 的 28 阶 Taylor 多项式再展开为
$P(u)=\sum_{j=0}^{84}a_j u^j$。字面相位系数为有理数，所以所有 $a_j,\mu_j$ 均以 Fraction 精确计算。直接有

$$
Q_P(u)-I_P(u)=\sum_j a_j\mu_j u^{j+1}.
$$

因而对 $r=0,1,2$，

$$
\|(Q_P-I_P)^{(r)}\|_{[0,U]}
\le\sum_{j+1\ge r}|a_j\mu_j|(j+1)_r U^{j+1-r}.
\tag{2}
$$

这实际计算了每个浮点节点的矩缺陷，没有以理想 Gauss 精确度替代。

在 $0\le u\le U$ 上，两个显式相位均满足

$$|\phi|\le1.51,\quad|\phi'|\le6,\quad|\phi''|\le10.$$

于是 $R=f(\phi)-P$ 满足

$$
\|R\|\le r_0=\frac{1.51^{29}}{29!},\qquad
\|R'\|\le r_1=6\frac{1.51^{28}}{28!},
$$

$$
\|R''\|\le r_2=
36\frac{1.51^{27}}{27!}+10\frac{1.51^{28}}{28!}.
$$

设 $W=\sum_iw_i$；所有节点在 $(0,1)$、权重正。由 (1) 的真实求导及
$I_R'=R(u),\,I_R''=R'(u)$，

$$
\begin{split}
\|Q_R-I_R\|&\le(W+1)U r_0,\\
\|Q_R'-I_R'\|&\le(W+1)(r_0+U r_1),\\
\|Q_R''-I_R''\|&\le(W+1)(2r_1+U r_2).
\end{split}
\tag{3}
$$

(2)+(3) 给每个归一化曲段的三项界。物理段长为 $L$ 时乘子依次为
$L,1,L^{-1}$。位置误差累计两曲段；一二阶取所在曲段的上界。平台字面常数差分别小于 $1.867\,10^{-17}$ 和 $3.598\,10^{-18}$，也已计入。

这里使用的是**已知解析背景公式**的 Taylor 余项，不给非旋转 $C^2$ 场增加第三阶正则性假设。

## 3. 实际端点比例与 R59 参数误差

字面参数为

$$
p_s=1.5069323382251065,\qquad e_s=0.015965997142447508,
$$

$$
(L_{1,s},L_{2,s},L_{3,s})
=(0.565099626834415,\ 0.34832173342948536,\ 0.017270909669753535).
$$

真参考的 $L_2$ 通过真三角函数的上述多项式积分及余项包围，不复用粗分箱中点。例如

$$
-1.078040041819375\,10^{-16}
<L_{2,s}-L_{2,\rm ref}
<-1.078040041614771\,10^{-16}.
$$

M24 actual linear 场的端点数为

$$
s_0=0.49457743382696573,\qquad
s_1=1.4252697037606197.
$$

先各自 float-to-Fraction，再精确相减：

$$
L_s=\frac{4191465360069805}{4503599627370496}.
\tag{4}
$$

没有把 (4) 替换成 bridge.L。$c=L_s/L_{\rm ref}$ 的实算界为

$$
-2.466669742346956\,10^{-17}
<c-1<
-2.466669740148577\,10^{-17}.
\tag{5}
$$

此前 M8 场的端点为 .4945773692800001 和 1.425269639213654；
其精确差为 $16765861440279217/18014398509481984$，对应
$|c_8-1|<2.037\,10^{-16}$。两者都严格在 $10^{-12}$ 预算内；
它们是不同的端点输入，未混用。

在参考坐标 $\tau\in[0,L_{\rm ref}]$ 中用 $s=c\tau$。初始曲段的归一化变量用 clip，末段仅用正部、不作上端 clip。两相位都可写为

$$
p_s C(\operatorname{clip}(s/L_{1,s},0,1))
-e_s\left(\frac{(s-L_{1,s}-L_{2,s})_+}{L_{3,s}}\right)^2,
\quad C(u)=3u^2-2u^3.
$$

由正部和 clip 的 1-Lipschitz 性、$\|C'\|\le3/2$、
$\|C''\|\le6$ 及参数区间，得到 M24 的

$$
E_\phi<2.152\,10^{-15},\qquad
E_{\phi'}<1.218\,10^{-13}.
\tag{6}
$$

第二项为对 $\tau$ 的导数差。结合 $|\phi_{\rm ref}'|\le4$，

$$
E_1^{\rm pull}\le |c-1|+E_\phi+cE_1,
$$

$$
E_2^{\rm pull}\le cE_{\phi'}+4(|c-1|+E_\phi)+c^2E_2.
$$

由共同入口值积分得到 0 阶界，正是开头表中的最后一行。

## 4. 末端 clip 与所选新连续对象

三个字面段长的精确和与 M24 物理跨度满足

$$
L_s-\sum_jL_{j,s}=\frac{31}{2^{58}}
=1.0755285551056204\ldots\,10^{-16}>0.
\tag{7}
$$

所以把 np.clip 字面解释成连续函数时，最后这段内位置已被截成常数，而程序手填的一阶值仍非零；其真实导数差不是“小区间所以小”。本文不作这种错误声称。

此次新对象明确采用 $\phi=p_s-e_su^2$ 的解析延拓到 (4)，且已验证
$u_{\rm end}\le1+10^{-12}$。有限规则也按同一解析公式延拓，因此 (2)–(3) 已覆盖它。

令 $d=(L_s-\sum L_{j,s})_+$，$\delta=d/L_{3,s}$。源 clipped 半径值与解析延拓有限规则之差由

$$d(1+E_{1,\rm last})$$

包围。源手填 geo 一二阶与解析相位的差由

$$
\Delta\phi=e_s(2\delta+\delta^2),\qquad
\Delta\phi_s=\frac{2e_s\delta}{L_{3,s}},
$$

$$
\Delta a'\le\Delta\phi,\qquad
\Delta a''\le
\frac{2e_s}{L_{3,s}}\Delta\phi+\Delta\phi_s
\tag{8}
$$

包围。证书直接输出这些实算值。它比较的是源**手填 geo jet oracle**，不是 clipped 半径函数的真实导数。

半径值加入有限规则的 primitive 差后，由 $a\ge.299$ 可付这一项相对目标度量传递：

$$
\eta_{g,\rm radius}\le
2\frac{\varepsilon_a}{.299}
+\left(\frac{\varepsilon_a}{.299}\right)^2.
\tag{9}
$$

这里保持同一个物理 $s$ 和材料角、径向度量系数为 1；只比较半径系数。它不是两目标 $g$ 严格相等的声明，也不是完整 field/mean/尾缝证书。

## 5. GL 接头的共享 jet 修补量

一般 $Q_f'(1)\ne f(\phi(1))$，
$Q_f''(1)\ne f'(\phi(1))\phi'(1)$，所以有限求积曲段和平台有极小 jet 跳。若需要保留该有限规则作为候选图的一部分，可以显式修补：长度 $\ell$ 曲段端点值保持不动，一二导数改为指定共享值。

标准 quintic Hermite 基为

$$
\begin{split}
h_{10}&=u-6u^3+8u^4-3u^5,&
h_{11}&=-4u^3+7u^4-3u^5,\\
h_{20}&=(u^2-3u^3+3u^4-u^5)/2,&
h_{21}&=(u^3-2u^4+u^5)/2.
\end{split}
$$

设需要消去的端点缺口为 $e_{1,0},e_{1,1},e_{2,0},e_{2,1}$。取

$$
H=-\ell(e_{1,0}h_{10}+e_{1,1}h_{11})
  -\ell^2(e_{2,0}h_{20}+e_{2,1}h_{21}).
$$

Bernstein 凸包给两类基的 $r=0,1,2$ 导数绝对值和分别不超过

$$A_r=(4/5,4,24),\qquad B_r=(1/10,1/2,4).$$

于是

$$
\|H^{(r)}\|\le
\ell^{1-r}E_1A_r+\ell^{2-r}E_2B_r.
\tag{10}
$$

当前计算连同平台字面三角常数差，两个 trig 均可取

$$
\|H\|<1.249\,10^{-11},\quad
\|H'\|<1.105\,10^{-10},\quad
\|H''\|<1.451\,10^{-9}.
$$

末段 $\ell$ 使用 (4) 减去前两个字面段长；其解析延拓误差已在 $U$ 中计入。这只是已有完整上界的可用构造，**尚未把 live map 换成它**。若改用真 primitive 而非有限规则，仍须对 Y、角图及 mean 的全部共享 jet 采用明确的同一个连续对象。任何目标 $g$ 或候选图变化都须显式付到原度量门。

## 6. 重现与保留范围

实际运行命令如下；WORK 为当前 scratch 根，source 按已登记恢复入口生成。

~~~bash
OPENBLAS_NUM_THREADS=1 python \
  topics/visible-flex-held-10pct/scripts/resume_n4/certify_short_bridge_quadrature_jet_gap.py \
  --run "$WORK/m3-work/newg-wide-lambda0p002-m24-linear/run.json" \
  --source "$WORK/m3-work/runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py" \
  --prefix-end 0.49457743382696573 \
  --end 1.4252697037606197 \
  --extension 1e-12 \
  --out "$WORK/n4-work/short-bridge-m24-gl64-extended-gap.json"
~~~

本次实际 exit 0。输出的 full-metric、非旋转 geometry 和 live shared-jet-repair 标志均未提升为通过。本文不以 sampled FFT、两次浮点求积的差或非定向舍入代替连续区间界；也不通过局部重定标或新增均值常数来改善握持比例。

