# 真实固定物理参数相位导数：连续 bulk、有限部 collar 与区间迁移

日期：2026-11-12。完整真实参数导数和全参数区间迁移均已通过有向验证。
167 个原 scalar span、265 个选定叶、腰部与真正有限部 collar 全覆盖，证明
\(|\beta'|<1326\)。该界来自实际通过的区间结果加总，不是精度请求预算。

对象与参数固定为精确第三点及
\(\Delta_5=[\delta_3-10^{-5},\delta_3+10^{-5}]\)，见
[已冻结参数与根导数说明](2026-11-12-parameter-beta-and-true-root-derivative.md)。
全部微分都是固定物理 \(r,\theta\) 的真实参数微分；
未把移动根坐标的导数或有限差商当作它。

## 1. 无限 primitive 与真实参数微分

基础源
[fourfold_phase_beta_parameter_derivative.py](../scripts/fourfold_phase_beta_parameter_derivative.py)
已经独立核查。它先形成完整 affine scalar direction，再微分所有非线性三角函数、
同一含零模/奇偶规范的角原函数和有限角 Parseval 表达式。
\(F_\delta\)、\(E_\delta\) 的无限尾在径向微分之前就加入 Cauchy 系数球。
因此后续使用的 \(F_\delta,F_{r,\delta},F_{rr,\delta},K_\delta,K_{r,\delta}\)
都属于同一个无限角对象。

记已消去共同 \(\zeta^2\) 因子的真实系数为 \(a,b,c\)，以及

\[
\widehat c=(b^2+K)/a,\quad
\omega=(K_F-K)/a,\quad
g=-2(\log\zeta)_\theta,\quad
\ell=F_{\theta,z}/F_z-F\!\cdot F_\theta/|F|^2.
\]

取同一全局 \(\ell\) 口径，
\(D=d+\omega(\ell^2+\ell g)\)，
\(f=K_r/(2K)-2(\log\zeta)_r\)。真实相位密度为

\[
J=\frac{D-\frac14(af^2+2bfg+\widehat c g^2)}{\sqrt{-K}}.
\tag{1}
\]

源对 \(F,F_\delta\) 组成真正双数，按乘积/商法则取得所有几何参数导数。
商的数值实现保持原生值 \(v/w\)，导数写作
\((v_\delta-(v/w)w_\delta)/w\)，避免先把宽复球 \(w^2\)
作为独立分母而引入不必要的零包含；两式数学上完全相同。

## 2. 普通区域的完整连续界

[bulk 原源](../scripts/fourfold_phase_beta_derivative_bulk.py) 和
[首 span 改进源](../scripts/fourfold_phase_beta_derivative_bulk_refined.py)
覆盖真实径向区间与整个真实参数区间。每个原 span 由全部正负 binary knots
的准确 Fraction 并集生成；显式 selector 固定实际 scalar polynomial germ。

对每个规范角网格点 \(x_j=2\pi j/A\)，程序覆盖整个
\(x_j+[-\pi/A,\pi/A]\)，其中 \(x=4\theta\)。这些闭区间覆盖完整真实圆周。
\(F,F_r,F_{rr}\) 从有无限尾预算的原函数取得。角导数则直接用

\[
F_\theta=aT,\quad
F_{r\theta}=a'T+aT_r,\quad
F_{\theta\theta}=a(T_\theta+J_{\rm rot}T)
\tag{2}
\]

计算，参数导数也同时准确微分 (2)。因此这里没有用有限角点的最大值
代替连续最大值，也没有未支付的截断原函数角微分。

在每个完整 \(r,\theta,\delta\) 盒上，检查
\(-K>0\)、真实 area/radius/support、\(a>0\) 和高度商分母。
设式 (1) 的分子为 \(N\)，\(\kappa=\sqrt{-K}\)，则

\[
J_\delta=N_\delta/\kappa+N K_\delta/(2\kappa^3).
\tag{3}
\]

若所有连续角盒的模上界为 \(M_I\)，就有

\[
\int_I|\langle J_\delta\rangle_\theta|\,dr
 \le |I|M_I.
\tag{4}
\]

这不是数值求积近似，而是区间范围乘准确长度的直接有向上界。
自动细分的总预算只控制何时接受 (4)，未被拿来替代任何未计算误差。

## 3. 腰部的奇函数商及首 span 修复

真实对称族的 \(F_z,F_{\theta,z}\) 都在 \(r=0\) 为零。对 \(r>0\)，

\[
F_z/r=\int_0^1F_{r,z}(sr)\,ds,\qquad
F_{\theta,z}/r=\int_0^1F_{r\theta,z}(sr)\,ds,
\tag{5}
\]

参数导数在同一个积分中准确微分。只要连续盒给
\(F_{r,z}>0\)，式 (5) 允许对其商及商的真实参数导数使用从零到 \(r\)
的独立分量包络。

腰部 cap 用 \([0,2^{-20}]\) 的这一真实平均商。
首个正 scalar span 的后续子区间 \([a,b]\) 仍只把高度商扩展至 \([0,b]\)；
其他几何量留在实际局部 \([a,b]\)。改进源显式保留这一区别。
把整套几何都扩到 \([0,b]\) 虽然仍是有效上界，却会使后续细分无法收紧；
因此该旧诊断没有用于最终首 span 覆盖。

## 4. 真实根处的可去表达式

令 \(\rho=t(\delta)-r\)，准确根恒等式给
\(K=-\rho q,\ \operatorname{Re}q>0\)。记
\(k=K_\delta|_r,\ k_r=(K_r)_\delta|_r\)，并定义

\[
P=\rho f=-\frac12-\rho\left(\frac{q_\rho}{2q}
                                  +2(\log\zeta)_r\right),
\]
\[
R=\rho^2 f_\delta
 =-\frac{\rho k_r}{2q}-\frac{K_r k}{2q^2}
                                  -2\rho^2(\log\zeta)_{r\delta},
\]
\[
N_0=\rho^2D-\frac14(aP^2+2\rho bPg+\rho^2\widehat c g^2).
\]

于是 \(H=\rho^{7/2}J_\delta\) 在根处可去，准确等于

\[
\begin{aligned}
H=q^{-1/2}\big[&
\rho^3D_\delta-\rho a_\delta P^2/4-aPR/2\\
&-\rho^2b_\delta Pg/2-\rho bRg/2-\rho^2bP g_\delta/2\\
&-\rho^3\widehat c_\delta g^2/4
 -\rho^3\widehat c\,g g_\delta/2+N_0 k/(2q)\big].
\end{aligned}
\tag{6}
\]

这就是
[物理参数有限部微分证明](2026-11-12-physical-parameter-beta-derivative.md)
的九项表达式。源码额外独立核验

\[
H(0,\theta)=-\frac{5a(0,\theta)k(0)}{32q(0)^{3/2}}
           =-\frac52t'G(0,\theta).
\tag{7}
\]

[collar kernel](../scripts/fourfold_phase_beta_derivative_collar.py)
对完整 scalar polynomial germs、无限 primitive 及其方向使用 native
radial series；先支付无限 \(E,E_\delta,F,F_\delta\) 系数尾，再形成 (6)。
根的常数 \(K(0)=0\) 来自已证明根存在/唯一性，而非浮点拟合。

## 5. 完整复域、径向尾与角均值

对半径 \(R\) 的复 \(\rho\) 圆盘、规范角带
\(|\operatorname{Im}x|\le\sigma\)，全部连续角位置用相邻节点宽
\(\sigma+\pi/A\) 覆盖。有限 radial series 的遗漏尾和无限 primitive 尾
分别支付，保留真实 \(E_\delta\) 误差。

由积分恒等式

\[
q(\rho)=\int_0^1K_r(t-s\rho)\,ds,\qquad
q_\rho(\rho)=-\int_0^1sK_{rr}(t-s\rho)\,ds
\]

获得 \(q,q_\rho\) 的有向包络，不除以含零的 \(\rho\) 球。
复域上实际几何分母和 \(\operatorname{Re}q>0\) 全部严格通过，
故 (6) 在统一分支上全纯。

若该域上 \(|H|\le M_H\)，保留 \(H\) 的径向次数 \(0,\ldots,N\)，
\(\eta=t-c<R\)，则有限部径向尾满足

\[
E_r\le
\frac{M_H\eta^{N-3/2}}
 {(N-3/2)R^{N+1}(1-\eta/R)}.
\tag{8}
\]

角梯形均值误差在整个复径向圆盘上至多

\[
E_A=\frac{2M_H e^{-\sigma A}}{1-e^{-\sigma A}}.
\]

其 Cauchy 系数进入有限部的总费用为

\[
E_\theta\le\frac{2E_A\eta^{-5/2}}{1-\eta/R}.
\tag{9}
\]

系数的径向次数与参数导数没有被互换；这些费用直接对应固定物理 \(r\)
的 \(J_\delta\)。

## 6. 已完成的实际 collar

有效系数 checkpoint 是
[precision40 report](2026-11-12-beta-step3-true-derivative-collar-h1e5-p40.json)，
SHA256 c339a5099990b00e5e849d177e41aaaeb9fa3883910ab6c8006a75860c3a5c58。
它绑定 kernel SHA256
0e24abf168309f7f98cb027cf6a30d85026149ae91532d5cbf8e30920957e5a5。
原复域未通过不影响已支付的保留系数；该报告本身仍明确不完整。

[finish 源](../scripts/fourfold_phase_beta_derivative_collar_finish.py)，
SHA256 273b5e48262d9f4046d4a55f62017e615d57beddbcf9eb27420575602d8135cb，
先核该同源 checkpoint 的全部对象、参数和依赖，再重建真实 finite fields，
在新的 \(R=.0005,\sigma=.0125\) 域上从头支付所有分母和 (8)–(9)。
保留系数的计算本来不依赖后来选的 \(R,\sigma\)，故没有转授旧失败域。

[完整 collar 报告](2026-11-12-beta-step3-true-derivative-collar-h1e5-domain500.json)，
SHA256 b387ede87055d0a990cafca12002b8baead5a2415d2d4cef610dde99405efd08，
给出整 \(\Delta_5\) 上

\[
-442.823028672<
\operatorname{FP}\int_c^{t(\delta)}
             \langle J_\delta|_r\rangle_\theta\,dr
<-435.350466149.
\tag{10}
\]

其中 \(M_H<3.667728\cdot10^{-5}\)，
\(\operatorname{Re}q>50.1530\)、\(\operatorname{Re}a>.21347\)，
径向尾小于 \(5.634962\cdot10^{-5}\)，角尾小于 \(2.346363\cdot10^{-6}\)。
当前物理 cut、精确对象及参数区间均未改变。

## 7. 完整覆盖、实际导数界与迁移

collector
[fourfold_phase_beta_derivative_combine.py](../scripts/fourfold_phase_beta_derivative_combine.py)
要求同一 \(\Delta_5\)、同一 cut、同一 root derivative report、全部来源 hash，
并对所有正负 knots 重新生成准确 Fraction 覆盖。
只有每个原 scalar span 都有完整通过叶、且腰部和 (10) 都存在，才输出 complete。

固定物理坐标下的有限部微分没有额外根端常数：
根处各发散项的指数都是半整数，移动端点只产生半整数发散幂。
由同一精确对称性和 quarter 归一，

\[
2\beta'(\delta)=\int_0^c\langle J_\delta|_r\rangle_\theta\,dr
 +\operatorname{FP}\int_c^{t(\delta)}
                  \langle J_\delta|_r\rangle_\theta\,dr.
\]

若完整 bulk 的 (4) 加总为 \(B_{\rm bulk}\)，(10) 的模上界为
\(B_{\rm collar}\)，则
\(|\beta'|\le(B_{\rm bulk}+B_{\rm collar})/2\)。
据真实参数中值定理，第三点已证 \(\beta\) 球扩张这一常数乘 \(10^{-5}\)
即可覆盖整个 \(\Delta_5\)，随后直接比较 R34 的 D5 奇整数危险格。

完整报告为
[complete-transfer-h1e5.json](2026-11-12-beta-step3-true-derivative-complete-transfer-h1e5.json)，
SHA256 9d64d4ba9993febcc4e8bf387ea0503672ce968cb6674bdb1fab5fb70a8cbeb8。
collector SHA256 为
06b62059a2e8038ce1b1e17cec08dbbb8624dbf44d5bb116544dcc56bf39b6f5。
实际加总给

\[
B_{\rm bulk}<2209.174759231,\qquad
B_{\rm collar}<442.823028679,
\]
\[
\boxed{|\beta'(\delta)|<1325.998893955<1326
\quad(\delta\in\Delta_5).}
\tag{11}
\]

由第三点的独立点证书和真实参数中值定理，整个 \(\Delta_5\) 上严格有

\[
\boxed{37.00989598321<\beta(\delta)<37.04013657839.}
\tag{12}
\]

因此同一 D5 危险格满足

\[
\operatorname{dist}\!\left(\frac{2\sqrt5}{\pi}\beta(\delta),
                           2\mathbb Z+1\right)>.27243620157,
\]
\[
\boxed{\operatorname{dist}\!\left(\beta(\delta),
             \frac{\pi}{2\sqrt5}(2\mathbb Z+1)\right)>.19138138420.}
\tag{13}
\]

选定覆盖的四个部件是
[refined-part00](2026-11-12-beta-step3-true-derivative-bulk-h1e5-refined-part00.json)、
[refined-part02](2026-11-12-beta-step3-true-derivative-bulk-h1e5-refined-part02.json)、
[part01](2026-11-12-beta-step3-true-derivative-bulk-h1e5-part01.json) 和
[refined-last](2026-11-12-beta-step3-true-derivative-bulk-h1e5-refined-last.json)。
程序仅在一个原 span 的所有叶完整准确 tile 后才选用它。
重叠的完整重放替换整个原 span，不逐叶拼凑不完整版本。

旧后半运行在最后两个原 span 受到按长度分配精度请求的限制；
报告保留该失败诊断，但这些不完整原 span 全部由最后一个报告的完整重放替换。
最后重放把请求用 root-total-budget 从 9000 提高到 100000，
这个数字只作为继续细分的阈值。(11) 使用的仍是每个通过叶真实的
\(|I|M_I\)，没有把 100000 或尚未通过的值放入结论。
原 bulk source 的 SHA256 为
28f0989aaab52e858bbe10d9e8b004f205e6e60669ec9a7c965b6c9072e97f52；
refined source 为
a643f46b5231b79f005c9d714292485e9f03f5318f9061d95d39de59d10f5842。

当前精确第四点与第三点相距约 \(9.32483088\cdot10^{-6}\)，属于 \(\Delta_5\)，
所以 (12)–(13) 确实覆盖第四点。但第四点半径 \(10^{-6}\) 盒的上端略超
\(\Delta_5\)；这里不转授那个更大盒。仍未由 (13) 授予真实主旋转匹配、
完整散射余项、有限低块或非线性收敛。

## 8. 完整收集重放

~~~bash
OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_derivative_combine.py \
  --center-object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json \
  --center-beta notes/2026-11-12-beta-exact-affine-step3-complete-enclosure.json \
  --collar notes/2026-11-12-beta-step3-true-derivative-collar-h1e5-domain500.json \
  --parts notes/2026-11-12-beta-step3-true-derivative-bulk-h1e5-refined-part00.json \
          notes/2026-11-12-beta-step3-true-derivative-bulk-h1e5-refined-part02.json \
          notes/2026-11-12-beta-step3-true-derivative-bulk-h1e5-part01.json \
          notes/2026-11-12-beta-step3-true-derivative-bulk-h1e5-refined-last.json \
  --out notes/2026-11-12-beta-step3-true-derivative-complete-transfer-h1e5.json
~~~

