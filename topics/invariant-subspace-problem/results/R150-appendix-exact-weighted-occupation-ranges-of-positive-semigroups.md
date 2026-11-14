# R150 附录：正 first 半群的准确占据权值域与有界移动权单位

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。根代理已全文核验逆张量极限、真实carry双向Volterra和全部自然域。

状态：完整证明。这是[精确占据指数增益](R150-appendix-sharp-weighted-occupation-exponential-gain-of-positive-semigroups.md)的加强：移动权演化不只有界，而且是有界单位。因此得到准确值域、双向图范数及全部自然域。原稿已付的临界上界和越临界测试不重新计作本稿新结论。

## 1. 准确值域定理

保持原实际非负 $\ell^2$ 行 $a$、最大增生 first $X_a$ 及
$$
S(t)=e^{-tX_a},\qquad
\mathcal N_a\chi_F=\left(\sum_{j\in F}a_j\right)\chi_F,
$$
$$
W_\sigma=e^{\sigma\mathcal N_a},\qquad
H_{a,\sigma}=\operatorname{Dom}W_\sigma,\qquad
\|f\|_{a,\sigma}=\|W_\sigma f\|.
$$
允许 $a$ 是零行或可和行。

**定理。** 对每个 $t>0$、$\delta\ge0$，
$$
\boxed{
U_\delta(t):=W_{\delta+2t}S(t)W_{-\delta}
\in B(H)^\times.
}
\tag{1.1}
$$
所以
$$
\boxed{
S(t)H_{a,\delta}=H_{a,\delta+2t},
\qquad
\operatorname{Ran}S(t)=H_{a,2t}.
}
\tag{1.2}
$$
$S(t)$ 是从第一个加权 Hilbert 空间到第二个加权 Hilbert 空间的有界同构。特别，实际逆的准确域为
$$
\boxed{
\operatorname{Dom}S(t)^{-1}=H_{a,2t},\qquad
S(t)^{-1}f=U_0(t)^{-1}W_{2t}f.
}
\tag{1.3}
$$
这里 $S(t)^{-1}$ 只在其真实值域上定义，没有全空间有界反半群的断言。

令前稿的
$$
b_\delta(r)=\sum_j a_j\sinh((\delta+2r)a_j),\qquad
K_a(\sigma)=18\sum_j a_j\eta_j
\sum_{L\ge1}e^{\sigma\|a\|_2\sqrt{L+1}}\eta_*^{L-1}.
$$
可取同一个有限常数
$$
M_{\delta,t}
=\exp\!\left(\int_0^t
[b_\delta(r)+K_a(\delta+2r)]\,dr\right)
$$
同时控制
$$
\boxed{\|U_\delta(t)\|\le M_{\delta,t},\qquad
\|U_\delta(t)^{-1}\|\le M_{\delta,t}.}
\tag{1.4}
$$
因此对每个 $f\in H_{a,\delta}$，
$$
M_{\delta,t}^{-1}\|f\|_{a,\delta}
\le\|S(t)f\|_{a,\delta+2t}
\le M_{\delta,t}\|f\|_{a,\delta}.
\tag{1.5}
$$

证明必须补出无限极限的逆；统一有界下界本身只给闭像，不能代替下面的满射论证。

## 2. 有限纯移动权的逆也有相同预算

前稿对 $0\le s\le t\le T$ 构造
$$
U^0_{\delta,n}(t,s)=
e^{(\delta+2t)\mathcal N_{a,n}}
e^{-(t-s)X^0_n}
e^{-(\delta+2s)\mathcal N_{a,n}},
$$
其中
$$
X^0_n=\sum_{j<n}a_jS_j^0,\qquad
\mathcal N_{a,n}=\sum_{j<n}a_jn_j,\qquad
S_j^0=\begin{pmatrix}0&-1\\1&2\end{pmatrix}.
$$
前稿给其强极限 $U^0_\delta(t,s)$ 以及准确反权关系
$$
W_{-(\delta+2t)}U^0_\delta(t,s)
=S^0(t-s)W_{-(\delta+2s)}.
\tag{2.1}
$$

有限移动权的时间生成元为
$$
G_{j,\delta}(r)=
-a_j\begin{pmatrix}
0&-e^{-(\delta+2r)a_j}\\
e^{(\delta+2r)a_j}&0
\end{pmatrix}.
$$
其实部上下界同时为
$$
-a_j\sinh((\delta+2r)a_j)I
\le\operatorname{Re}G_{j,\delta}(r)
\le a_j\sinh((\delta+2r)a_j)I.
$$
对有限维演化的范数平方同时使用两侧界，得到
$$
e^{-\int_s^t b_{\delta,n}(r)dr}\|h\|
\le\|U^0_{\delta,n}(t,s)h\|
\le e^{\int_s^t b_{\delta,n}(r)dr}\|h\|,
$$
$$
b_{\delta,n}(r)=\sum_{j<n}a_j\sinh((\delta+2r)a_j).
$$
因为有限头演化已是全空间有界单位，
其准确逆
$$
V^0_{\delta,n}(s,t)
=
e^{(\delta+2s)\mathcal N_{a,n}}
e^{+(t-s)X_n^0}
e^{-(\delta+2t)\mathcal N_{a,n}}
$$
满足
$$
\boxed{
\|V^0_{\delta,n}(s,t)\|
\le\exp\!\left(\int_s^t b_\delta(r)\,dr\right).
}
\tag{2.2}
$$
本式只对有限头正指数使用，不先定义全空间的无界正半群。

## 3. 逆移动权的无限强极限和真正双侧逆

令 $h=t-s\ge0$。
在每位原真空上，有限逆因子的准确公式是
$$
V_j^0(s,t)\Omega_j
=e^{ha_j}\left[(1-ha_j)\Omega_j
+ha_je^{(\delta+2s)a_j}\chi_j\right].
\tag{3.1}
$$
充分高的尾上 $T a_j\le1/2$。
其真空内积
$$
r_j=e^{ha_j}(1-ha_j)
$$
遂在 $[0,1]$ 中，而且
$$
1-r_j
=\int_0^{ha_j}u e^u\,du
\le\tfrac12 e^{T\|a\|_\infty}T^2a_j^2.
\tag{3.2}
$$
(2.2) 对任意尾区间的同一纯 tensor 也成立。
因此与前稿完全相同的尾向量范数计算给
$$
\left\|
\bigotimes_{j\in[n,N)}V_j^0(s,t)\Omega_j-\Omega_{[n,N)}
\right\|^2
\le C_{\delta,T,a}\sum_{j\ge n}a_j^2.
\tag{3.3}
$$
这里对充分大 $n$ 一致于 $N>n$ 及 $0\le s\le t\le T$；
有限低头无需满足 $Ta_j\le1/2$。

先对有限柱输入分开低头，再用 (2.2)、(3.3)，
得到 $V^0_{\delta,n}(s,t)$ 的强 Cauchy 性。
由统一范数界，极限
$$
V^0_\delta(s,t)=\operatorname*{SOT-lim}_{n\to\infty}
V^0_{\delta,n}(s,t)
$$
存在于全部 $H$，并对参数强连续。
有限头准确双侧乘积为 $I$；两列都强收敛且统一有界，故
$$
\boxed{
V^0_\delta(s,t)U^0_\delta(t,s)
=U^0_\delta(t,s)V^0_\delta(s,t)=I.
}
\tag{3.4}
$$
所以 $U^0_\delta(t,s)$ 真正满射且单射，
其逆就是 $V^0_\delta(s,t)$。

由此可把记号 $U^0_\delta(t,s)$ 扩到 $0\le s,t\le T$，
在 $t<s$ 时定义为上述逆。
它是强连续的双向演化族，满足全部参数次序的乘法关系。
其正反两向范数均由
$\exp(\int_{\min(s,t)}^{\max(s,t)}b_\delta(r)dr)$ 控制。

## 4. 实际 carry 的有界时间扰动仍给单位

前稿以真实局部级数证明
$$
E(r):=W_{\delta+2r}E_aW_{-(\delta+2r)}
\in B(H),\qquad
\|E(r)\|\le K_a(\delta+2r),
$$
并且 $E(r)$ 对 $r$ 范数连续。
原实际移动权解满足
$$
U_\delta(t,s)=U^0_\delta(t,s)
-\int_s^t U^0_\delta(t,r)E(r)U_\delta(r,s)\,dr
\quad(t\ge s).
\tag{4.1}
$$
前稿已通过左乘有界逆权，识别此解与原实际 $S$ 的关系；
这里不重新定义另一个实际半群。

为逐项证明可逆性，取
$$
B(r)=U^0_\delta(0,r)E(r)U^0_\delta(r,0).
$$
第3节保证这是真正全域有界、强连续、紧时间区间范数有界的系数。
常见的有界线性积分方程也可直接由 Picard 级数构造：
$$
V(t,s)=I-\int_s^t B(r)V(r,s)\,dr.
\tag{4.2}
$$
同样从终点往回积分可构造 $V(s,t)$。
在固定向量上使用强微分和乘积法则，
或将两边的 Picard 级数逐项相乘，得到
$$
V(t,s)V(s,t)=V(s,t)V(t,s)=I.
$$
所有积分和乘积均为有界算子作用于向量后的强积分；
不需要对原无界 first 作形式约分。

于是
$$
\widetilde U_\delta(t,s)=
U^0_\delta(t,0)V(t,s)U^0_\delta(0,s)
$$
是有界单位。
将 (4.2) 代回，恰满足 (4.1)，故由其唯一性，
$$
\boxed{U_\delta(t,s)=\widetilde U_\delta(t,s)\in B(H)^\times.}
\tag{4.3}
$$

正向预算已由前稿得到。
其逆满足准确的反向 Volterra 方程
$$
U_\delta(s,t)=U^0_\delta(s,t)
+\int_s^t U^0_\delta(s,r)E(r)U_\delta(r,t)\,dr.
\tag{4.4}
$$
使用第3节的逆纯演化界以及同一个 Gronwall 论证，
$$
\boxed{
\|U_\delta(s,t)\|
\le\exp\!\left(\int_s^t
[b_\delta(r)+K_a(\delta+2r)]\,dr\right).
}
\tag{4.5}
$$
所以 (1.4) 的两向预算都已支付。

## 5. 从有界单位得到准确值域

前稿已证的实际恒等式是
$$
S(t)W_{-\delta}=W_{-(\delta+2t)}U_\delta(t,0).
\tag{5.1}
$$
第4节给右侧最后因子满射。
因而两侧的准确像为
$$
S(t)H_{a,\delta}=H_{a,\delta+2t}.
$$
$W_{-(\delta+2t)}$ 单射、$U_\delta(t,0)$ 为单位，
也再次给 $S(t)$ 单射。
取 $\delta=0$ 即得 (1.2)--(1.3)。

对 $f\in H_{a,\delta}$ 写 $f=W_{-\delta}h$。
(5.1) 给
$$
\|f\|_{a,\delta}=\|h\|,
\qquad
\|S(t)f\|_{a,\delta+2t}=\|U_\delta(t,0)h\|.
$$
正反两向预算证明 (1.5)。
这些都是原 Hilbert 范数和原实际加权域，没有通过抽象完备化迁移表示。

## 6. 全部超临界自然域的精确表达

固定 $\rho,\delta\ge0$、$t>0$，令
$$
\beta=\delta+2t,\qquad U=U_\delta(t,0).
$$
由 (5.1)，在各自完整自然域上，
$$
W_\rho S(t)W_{-\delta}
=W_\rho W_{-\beta}U.
$$
所以：

- 若 $\rho\le\beta$，该算子全域有界，准确等于
  $W_{-(\beta-\rho)}U$，其像为 $H_{a,\beta-\rho}$。
- 若 $\rho>\beta$，则
  $$
  \boxed{
  \operatorname{Dom}(W_\rho S(t)W_{-\delta})
  =U^{-1}H_{a,\rho-\beta},\qquad
  W_\rho S(t)W_{-\delta}=W_{\rho-\beta}U.
  }
  \tag{6.1}
  $$
  这个自然闭算子仍然满射到 $H$，其实际有界逆为
  $U^{-1}W_{-(\rho-\beta)}$。
  当 $a\notin\ell^1$ 时，其域真且算子无界。

最后一句只用 $\mathcal N_a$ 的实际对角谱：
$a\notin\ell^1$ 时有限集的质量 $\sum_Fa_j$ 无界，
所以每个 $W_\varepsilon$（$\varepsilon>0$）都是闭无界算子，
其稠密定义域是真子空间。
(6.1) 经有界单位拉回，给同一结论。
它与前稿保留全部 carry 的显式超临界测试一致。

## 7. 同一个临界输出没有任何额外正增益

还可把锐性放在同一个实际向量上。
假设 $a\notin\ell^1$，固定 $t>0,\delta\ge0$，令 $\beta=\delta+2t$。
选不同的有限集 $F_n$，使
$$
s_n=\sum_{j\in F_n}a_j\ge n^2.
$$
例如按物理次序取逐渐增长的前缀。
不同的 $\chi_{F_n}$ 彼此正交。
定义
$$
g=\sum_{n\ge1}2^{-n}e^{-\beta s_n}\chi_{F_n}.
$$
则
$$
\|W_\beta g\|^2=\sum_{n\ge1}4^{-n}<\infty,
$$
而对每个 $\varepsilon>0$，
$$
\|W_{\beta+\varepsilon}g\|^2
=\sum_{n\ge1}4^{-n}e^{2\varepsilon s_n}=\infty.
$$
由准确像定理，存在唯一 $f\in H_{a,\delta}$ 使 $S(t)f=g$，
而且可明确写成
$$
f=W_{-\delta}U_\delta(t,0)^{-1}W_\beta g.
$$
因此同一个输入达到临界权，却不获得任何额外正指数增益。

## 8. 范围与不能转移的结论

本稿的准确像识别严格增强前稿的像包含；
它只使用已付的移动权演化，再补其逆强极限和有界扰动可逆性。

$H_{a,2t}$ 是系数加权占据域。
在 $a_j\to0$ 时，不能把它换成通常
$\operatorname{Dom}e^{\sigma\mathcal N}$。
因此准确像仍不自动给 R255 的统一次数指数矩、
R244 的指定配对域，或 R267 的聚合矩上界。

$W_\sigma$ 未被假定保持未知不变空间。
本稿不给未知限制或旗子商的无界逆域识别。
完整 Hilbert 不变子空间问题仍未解决。

后续[全部不变旗与闭图的准确热像](R150-appendix-exact-heat-ranges-on-invariant-flags-and-closed-graphs.md)另用同一组真实有界强单位支付逆向包含，已经识别这些特定半群在未知不变限制/有限旗上的准确加权值域。其商范数为实际加权商，不由形式共轭或通常正交压缩取得。

## 9. 实际热算子的输入负占据范数与双侧二次型比较

本节只使用 §1 的准确全空间值域及原完整第一阶的 $C$ 自伴性。
固定 $t>0$，记
$$
\beta=2t,\qquad W_{-\beta}=e^{-\beta\mathcal N_a},\qquad
U=U_0(t).
$$
已证
$$
S(t)=W_{-\beta}U,\qquad U\in B(H)^\times,
\qquad \|U\|,\|U^{-1}\|\le M_{0,t}.
\tag{9.1}
$$
这是输出正权等式 $W_\beta S(t)=U$ 的实际有界形式。

原共轭在 Walsh 基上满足
$$
C\chi_F=(-1)^{|F|}\chi_F.
$$
所以 $C$ 保持各占据加权域，并且
$$
CW_{-\beta}C=W_{-\beta}.
\tag{9.2}
$$
原 $X_a=CX_a^*C$ 的真实半群满足
$$
CS(t)^*C=S(t).
\tag{9.3}
$$
例如先在左半平面的实际预解上使用 $C$ 自伴性，
再由生成元的半群唯一性得到 (9.3)。

对有界算子写 $B^\tau=CB^*C$。
这是保范数的反乘法映射，且有界单位的 $\tau$ 仍为有界单位。
对 (9.1) 取 $\tau$，由 (9.2)--(9.3) 得
$$
\boxed{
S(t)=U^\tau W_{-\beta}.
}
\tag{9.4}
$$
另外，直接取 Hilbert 伴随给
$$
\boxed{S(t)^*=U^*W_{-\beta}.}
\tag{9.5}
$$
两式中的有界左因子及其逆，范数都不超过 $M_{0,t}$。

因此对每个 $h\in H$，
$$
\boxed{
M_{0,t}^{-1}\|e^{-2t\mathcal N_a}h\|
\le\|S(t)h\|
\le M_{0,t}\|e^{-2t\mathcal N_a}h\|,
}
\tag{9.6}
$$
且同一个预算满足
$$
\boxed{
M_{0,t}^{-1}\|e^{-2t\mathcal N_a}h\|
\le\|S(t)^*h\|
\le M_{0,t}\|e^{-2t\mathcal N_a}h\|.
}
\tag{9.7}
$$
这两条是输入的负占据范数比较。
它们不把 $U$ 或 $U^\tau$ 与 $W_{-\beta}$ 交换，
也不同于原来的输出正权范数 $\|W_\beta S(t)h\|\asymp\|h\|$。

按有界自伴算子的二次型序，等价地，
$$
\boxed{
M_{0,t}^{-2}e^{-4t\mathcal N_a}
\le S(t)^*S(t)
\le M_{0,t}^{2}e^{-4t\mathcal N_a},
}
\tag{9.8}
$$
$$
\boxed{
M_{0,t}^{-2}e^{-4t\mathcal N_a}
\le S(t)S(t)^*
\le M_{0,t}^{2}e^{-4t\mathcal N_a}.
}
\tag{9.9}
$$

所有等式和预算按有限对角放大原样成立。
特别，对任何闭不变空间中的实际向量，可以直接使用环境范数的 (9.6)--(9.7)；
无需先证明占据权保持该空间。
这并不把 $C$ 或通常伴随限制到未知空间，
也不对其压缩凭空赋予乘法同态。

对任何实际源序列 $(h_p)\subset H$，(9.6) 还给准确的预算接口：
$$
\sup_p\|S(t)h_p\|<\infty
\Longleftrightarrow
\sup_p\|e^{-2t\mathcal N_a}h_p\|<\infty,
\tag{9.10}
$$
并且两范数之一趋于无穷，当且仅当另一者也如此。
同样的结论对 $S(t)^*$ 成立。
应用于 R244 的指定聚合源时，仍须先以该源的真实矩恒等式支付
$S(t)h_p$ 的上界或发散；(9.10) 只把那项实际算子成本精确换成占据负权成本。
