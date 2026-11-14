# R133 补充：精确M32修复后的实际完整正区N97高模逆

**状态：已证明（给定全部193低head与独立源时的完整无穷高模逆）。**

公开 Actions [43601149891](https://github.com/Rogerhu12/math-research-public/actions/runs/43601149891)
第二子过程实际通过8项完整检查，两个角阶均成功。
新数学时间10.703320795秒，子过程墙钟15.000749307秒，退出码0。
原4650闭行从四个binary parts逐字恢复；新增的只是修复膨胀、新Riccati下比较和scalar Volterra sweeps。

## 1. 同一修复背景、完整区间和真实参考

对象为固定物理$\eta_0$、原$\nu$下的精确连续M32修复。
区间准确为
$$
[r_b,25/8],\qquad r_b=1192029371497/5000000000000.
$$
全部4650闭盒、3594个原右接口、完整65槽、独立even mean和原内在系数均保留。
新背景仍是M32，完整反应带64；未知响应的全部$|j|\ge97$都参加，未截断其Fourier尾。

新principal速率为$a=-\gamma m_{\rm repaired}$。
新全域参考准确使用
$$
g_M(r_*)=M^{-1/3},\qquad
p_M(25/8)=q_*/(-m_{\rm repaired}(25/8)).
$$
它与[已完成的repair正根collar](R133-supplement-actual-exact-repair-positive-root-collar.md)
和[已完成的repair regular外图](R133-supplement-actual-exact-repair-complete-regular-outer-graph.md)
属于同一参考。内切面取$g=0$只用于保守下比较，未改真正根初值。
所有实际非零模式满足$M=4|j|\ge4$，本高块为$M\ge388$。

## 2. 两个完整角阶的实际收缩

[完整修复转授定理](R133-supplement-exact-M32-repair-transfer-of-cached-positive-high-rows.md)
规定逐字段变化、新mean、完整primitive与源。
全部4650个闭行的两个方向Volterra supremum实际给出：

| 项目 | $s=0$ | $s=1$ |
|---|---:|---:|
| 内部Volterra范数 | $<0.303269478915$ | $<0.788277735610$ |
| 本阶闭合的真外反馈 | $<0.000022100488421$ | 保独立右高端口 |
| 完整本阶反馈$\chi_s$ | $<0.303291579403$ | $<0.788277735610$ |
| normalized高态sup逆常数 | $<1.435320674241$ | $<4.723168831015$ |

两阶的最坏闭盒均为原row 2943，完整两支的径向最大值均在native中保存。
$s=0$已合入本次真实新外图反射；$s=1$没有擅自闭合一个未付的物理$H^{7/6}$外图。
这里的$\chi_1$是完整内部高逆的收缩，右高端口仍为独立输入。

## 3. 全部普通源、端口和迹

令$F_s$为原合同的普通源范数
$L^2_rH^{s+1/3}_\phi$。
令$G_s$为全部实际incoming端口、完整低head/mean和affine jump费用之和，
其中每个跳按同一新参考的$C_i\|j_i\|_{H^{s+1/3}}$计量。
源没有径向导数要求。

实际原生完整算子上界可向外显示为：

| 输出和输入 | $s=0$ | $s=1$ |
|---|---:|---:|
| $F_s\to Z_H$的径向sup | $0.181051041563$ | $0.595779501877$ |
| $G_s\to Z_H$的径向sup | $1.435320674241$ | $4.723168831015$ |
| $F_s\to h_H$的径向$L^2$ | $0.455697343253$ | $1.499555238888$ |
| $G_s\to h_H$的径向$L^2$ | $3.612637697750$ | $11.888043382477$ |
| $F_s\to$两端raw迹 | $1.793273635474$ | $5.901094036760$ |
| $G_s\to$两端raw迹 | $14.216558498357$ | $46.782179204754$ |

每行都用对应角阶的规范；表中数值是严格上界。
完整head到high源最多到index160，这只是该已知背景乘完整193head的支撑，
未赋给任意unknown high或非线性修正。
high到head、mean-own signed rate、mean feedback及mean rank的逐闭盒行均保存。
它们是后续全Schur的输入，本结果没有假设这些全局反馈已经小。

修复中心自己的值与全部角导数跳由准确repair身份为零；
任意响应或trial的affine跳仍保，不能由中心连续性删除。

## 4. 完整原件和实际执行

| 对象 | SHA256 |
|---|---|
| 原完整4650系数native | ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d |
| exact repair native | 6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc |
| 本次完整外图native | 75e7c0e1447306a97971ee05dcb68b8d357cb4fffa5c1a37335a6fc29a473424 |
| 新主体数学source | 8c4c734d3bf23e44aff5c8ad15ac248da52b79d05de3b4512cda42cb3cafa64d |
| 新完整主体native | eefb94952a409473fed7f9c34afc9214a3346d8c3b19ed7e0a7fc6fd06f48a68 |
| 新完整摘要 | fde40b46beb474e10a92e6f6b92bc93beecb91da33eefc073a72dbc60964a9a5 |
| 实际过程 | 459745352095624995f1a4c0864eb1e6dec7de5eff87c54ec1f2e3fce5ea99f1 |

[完整小摘要及8门](../notes/repaired_positive_ci/run-43601149891-1-exact-M32-repaired-positive/evidence/repaired-complete-positive-N97-high-inverse-summary.json)
与[实际过程](../notes/repaired_positive_ci/run-43601149891-1-exact-M32-repaired-positive/process.json)
保存全部范围、源单位、最坏闭盒、真实退出和原输入身份。
新完整native为16909572字节，已按规则无损拆成9件；
[精确分片清单](../notes/repaired_positive_ci/run-43601149891-1-exact-M32-repaired-positive/native-repaired-complete-positive-N97-high-inverse.json.gz-eefb94952a409473-parts.json)
恢复后仍是上述同一个SHA，全部4650膨胀行及两阶比较行均未删除。

结合已成root collar可在同一修复参考上接正根和正主体，
但全低head逆、实际负返回、true参数Schur及非线性F=0仍需完成。
$\delta Z$的M96/带192与未知非线性背景不自动取得本篇M32数值。
