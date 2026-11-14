# 有限前尾的 inverse-Q 构造：正系数、端口与真实曲率预算

2026-11-12，metric_closure。本文的代数结论是完整证明；末尾候选的数值范围是有限采样，
没有把它们提升成整个尾或非线性闭面的证书。

## 1. 当前目的与所用实际量

原 wc01 的真实单位 cut 高度线性解在首格有物理第二基本形式行和约
`565353.102849392`，而第二格的相对 canonical 量 `|L|` 达
`4936322.040405483`。两者不是同一几何量。参考输入是
`2026-11-12-fd2d-layered64-wc01-recovery02-config.json` 及其
`m2-n512-report.json`、`m2-n512-trajectory.jsonl.gz`；本构造不改这些输入。

这里反过来选一个明确的线性高度函数和正背景斜率，使低斜率谷中极集中的
二阶变化能重新分配到有限物理径向区间。新的有限背景允许不同的 cut 半径和
斜率，未改的更深 source 仍须由实际完整消费者接入。最终要比较同一个新 g
的 prefix 传递和完整 tail 响应之积，不能只比较单位 cut 的一个局部峰。

## 2. 从 canonical m2 系统到物理高度方程

在一个物理径向区间内，令 r>0、w(r)>0，μ>0 是该区间选取的 canonical
尺度。真实 m2 线性系统写成

\[
Q_r=\frac{\sqrt{12}\,\mu}{r^8w}Z,
\qquad Z_r=-\frac{\sqrt{12}\,r^6w}{\mu}Q.
\tag{1}
\]

定义实际高度系数 H=r⁴Q 及

\[
J=H_r-\frac{4H}{r}=r^4Q_r
 =\frac{\sqrt{12}\,\mu}{r^4w}Z=wL.
\tag{2}
\]

对 (1) 第一式求导并用第二式消去 Z_r，得到

\[
Q_{rr}=-\left(\frac8r+\frac{w_r}{w}\right)Q_r-\frac{12}{r^2}Q.
\]

将 H=r⁴Q 求两次导数，三项的 Q 项和 Q_r 的 8/r 项消去，故准确有

\[
\boxed{H_{rr}=-\frac{w_r}{w}J},\qquad
J_r=-\frac{12H}{r^2}-\left(\frac4r+\frac{w_r}{w}\right)J.
\tag{3}
\]

反过来，任一满足 (3) 的 H 和正 w，令 Q=H/r⁴，
Z=r⁴wJ/(√12 μ)，直接代入即得 (1)。因此这是等价的物理定义，
并不依赖选择 μ 的数值大小。

在本文所用法向约定下，m2 实高度扰动 H(r)cos(2u) 的三个线性化
正交第二基本形式幅度为

\[
\delta l=-\frac{H_{rr}}{\sqrt{1+w^2}},\qquad
\delta n=-\frac{\sqrt{1+w^2}}rJ,\qquad
\delta m=\frac{2H}{r^2}-\frac{2H_r}{r}.
\tag{4}
\]

可由 R117 的完整 height-jet 公式在旋转背景处直接求一阶导数验证：
法向分母的导数抵消 l 式中含 w w_r H_r 的项，留下 H_rr/√(1+w²)；
n 式的 H_r 项合成 √(1+w²)H_r/r，再与角二导的
−4√(1+w²)H/r² 合并；m 式使用 ∂u cos(2u)=−2sin(2u)。
整体法向反号只同时反号，不影响以下绝对值预算。

所以一个直接的全角线性行和上界是

\[
B_{II}=\max\{|\delta l|+|\delta m|,
                 |\delta n|+|\delta m|\}.
\tag{5}
\]

另须保留图坐标的线性系数

\[
\Gamma=\frac Jw-\frac{4Hw}{r}=L-\frac{4Hw}{r}.
\tag{6}
\]

实际幅度 h 下，|hΓ| 的控制与 |h|B_II 的控制用途不同。
这里只把它作为现有 root chart 的设计诊断；没有由线性 (6) 推出完整
非线性嵌入或一般几何不可能性。

## 3. 正 k 的准确 inverse-Q 引理

取 a>0、ℓ>0、b=a+ℓ，r=a+ℓt，0≤t≤1。选取一个在闭区间上严格正的
多项式 k(t)，记 k0=k(0)>0、k1=k(1)>0，并要求

\[
\int_0^1t(1-t)k(t)\,dt
 =\frac{a^2k_0+b^2k_1}{12\ell^2}.
\tag{7}
\]

准确地定义

\[
Q(t)=-\frac{a^2k_0}{12\ell^2}
          +\int_0^t v(1-v)k(v)\,dv,
\quad H(t)=r(t)^4Q(t).
\tag{8}
\]

由 (7)，Q(1)=b²k1/(12ℓ²)。Qt=t(1−t)k，因而

\[
J=\frac{r^4}{\ell}t(1-t)k>0\quad(0<t<1),
\quad J(0)=J(1)=0.
\tag{9}
\]

令

\[
F=r^2Q_{tt}+8\ell rQ_t+12\ell^2Q.
\tag{10}
\]

在 t=0 有 Qtt=k0，故 F(0)=a²k0+12ℓ²Q(0)=0；
在 t=1 有 Qtt=−k1，故 F(1)=−b²k1+12ℓ²Q(1)=0。
因此存在唯一多项式 P 使

\[
F=t(1-t)P.
\tag{11}
\]

给定 w0>0，定义

\[
\boxed{\displaystyle
w_{\rm raw}(t)=w_0\exp\!\left[-\int_0^t
 \frac{P(v)}{r(v)^2k(v)}\,dv\right].}
\tag{12}
\]

分母在闭区间上严格正，故 (12) 为光滑正函数，包含两端的准确有限值。
它没有使用端点处的 0/0 商。另一方面

\[
H_{rr}=\frac{r^2F}{\ell^2},\quad
\frac{(w_{\rm raw})_r}{w_{\rm raw}}
 =-\frac{P}{\ell r^2k}.
\]

再代 (9)、(11)，立即得到

\[
H_{rr}+\frac{(w_{\rm raw})_r}{w_{\rm raw}}J=0.
\]

这证明 (8)、(12) 给出准确的 m2 线性解和正背景。其端点满足

\[
H(0)=-\frac{a^6k_0}{12\ell^2},\qquad
H(1)=\frac{b^6k_1}{12\ell^2},\qquad H_{rr}(0)=H_{rr}(1)=0.
\tag{13}
\]

所以向外高度增益和向内衰减恰为

\[
\frac{H(1)}{H(0)}=-\frac{k_1}{k_0}\left(\frac ba\right)^6,
\qquad \gamma=\left|\frac{H(0)}{H(1)}\right|
 =\frac{k_0}{k_1}\left(\frac ab\right)^6.
\tag{14}
\]

除以 H(1) 就得到 cut 处 H=1 的单位参考解。因为 k>0，Q 严格递增，
它恰有一个零点；本引理构造一段变号传递。多次变号须按实际端口拼接多段，
不能把这个单段结论当成任意整个有限尾的传递定理。

## 4. 端口斜率与 C² 表面的准确接合

给定两端所需的物理 logarithmic 斜率
s0=(w_r/w)(a)、s1=(w_r/w)(b)，要求

\[
k'_0=k_0\left[1-\frac\ell2\left(\frac{10}a+s_0\right)\right],
\quad
k'_1=-k_1\left[1+\frac\ell2\left(\frac{10}b+s_1\right)\right].
\tag{15}
\]

证明只需求 P 的端值。由 (10)，

\[
F'(0)=10a\ell k_0+2a^2(k'_0-k_0),
\quad
F'(1)=-10b\ell k_1-2b^2(k_1+k'_1).
\]

由 F=t(1−t)P 得 P(0)=F′(0)、P(1)=−F′(1)。将 (15) 代入
(12) 的导数，得到 (log wraw)t(0)=ℓs0、(log wraw)t(1)=ℓs1。

因此，在内端准确取原物理 source 的 a,w0,s0 时，新的背景高度原函数
z_r=w 与原背景的两阶空间 jet 一致（位置允许作所需常数竖直平移）。
这里匹配的是 w 和 w_r，不是擅自要求 w_rr 也匹配。径向弧长坐标下
a_s=1/√(1+w²)、a_ss=−w w_r/(1+w²)²，故同样给准确 C² 的 a 和目标
度量 ds²+a(s)²du²。w_rr 是更高阶数据，未设为本题额外完成门。

对线性非圆参考高度，(13) 还给 H、H_r=4H/r、H_rr=0 的端两 jet。
实际深处的 bounded line 必须使用完整消费者算出的端值；若原 finite
calibration 只数值地接近 J=0，这个小偏差不会被本文自动删除。

## 5. 正 Bernstein 系数给可计算的准确定义

令 k=Σ bi B_i^d，d≥4，B_i^d=binom(d,i)t^i(1−t)^(d−i)。
取 k0=1、k1=κ>0。先由 (15) 固定

\[
b_0=1,\quad b_1=1+k'_0/d,\quad
b_d=\kappa,\quad b_{d-1}=\kappa-k'_1/d.
\tag{16}
\]

加权矩的准确系数是

\[
\omega_i=\int_0^1t(1-t)B_i^d(t)dt
 =\frac{(i+1)(d-i+1)}{(d+1)(d+2)(d+3)}.
\tag{17}
\]

给任意严格正的内部权重 vi，2≤i≤d−2。设

\[
C=\frac{a^2+b^2\kappa}{12\ell^2}
       -\sum_{i\in\{0,1,d-1,d\}}\omega_i b_i.
\]

只要 C>0、b1>0、b_(d−1)>0，定义

\[
b_i=\frac{C v_i}{\sum_{j=2}^{d-2}\omega_jv_j}
 \quad(2\le i\le d-2).
\tag{18}
\]

则所有 bi>0，故 k>0，且 (7) 准确成立。这里 (18) 是定义的一部分，
不是把优化器浮点矩残差当成零。候选 JSON 的有限浮点 vi 可按其二进制字节
作准确正有理数；真实内端几何常数则由所绑定的旧 source 定义取得。

无需用病态幂基相除：Qt 的 degree d+2 Bernstein 系数满足

\[
(Q_t)_{i+1}=b_i\frac{(i+1)(d-i+1)}{(d+1)(d+2)},
\]

两端系数为零。逐项积分得到 Q；由 Bernstein 乘法得到 degree D=d+3 的 F。
若 F 的系数为 fj，(11) 的 P 系数恰为

\[
P_{j-1}=f_j\frac{D(D-1)}{j(D-j)},\quad1\le j\le D-1.
\tag{19}
\]

原因是 t(1−t)B_(j−1)^(D−2)=j(D−j)B_j^D/[D(D−1)]。
这也证明代码消去端点零因子的算法与 (11) 相同。

## 6. 端值校准与准确新对象

不必把优化器的最后一个 log 端值残差变成独立等待门。给所需 w1>0，取

\[
S_5(t)=10t^3-15t^4+6t^5,\quad
c=\log\frac{w_1}{w_{\rm raw}(1)},\quad
w(t)=w_{\rm raw}(t)\exp(cS_5(t)).
\tag{20}
\]

则 w>0，w(0)=w0、w(1)=w1，且因为 S5′ 和 S5″ 在两端均为零，
两端的 logarithmic 一、二导数保持不变。特别地 (15) 所需的 w_r/w
保持，故 §4 的背景 C² 接合保持。

校准后的 (20) 是一个明确的新 g。原 H 多项式此时满足的准确方程是

\[
H_{rr}+\frac{w_r}{w}J=\frac c\ell S'_5(t)J.
\tag{21}
\]

若 c≠0，不能称原 H 已经是新 g 的真线性解；实际全线性尾和非线性尾必须
消费 (20)。即使 c 在浮点试算中很小，也保留这一对象区别。

`fd2d-metric-inverse-q-buffer.mjs` 是 (7)–(20) 的浮点求值器，使用固定有限
1024 格累积积分和每格 16 点 Gauss，再在查询格内积分余段；没有无界点缓存。
积分定义本身是准确的，浮点评估及网格比较不冒充积分余项证书。

`fd2d-metric-inverse-q-bridge.mjs` 只作实际 factory 接口：
`createInverseQBridge(candidate,{left,w0,wr0})` 返回 `point(t)`，其 t 是整个
bridge 的 [0,1] 坐标。若调用方把 bridge 分成多个 profiles，须一并链式缩放
dr/dx、dlogw/dx 和二阶导数。调用方可传入同一旧 source 的实际端值求值，
并在新 manifest 记录；这里的候选小数未被假装成原解析端口的准确常数。

## 7. 已实际闭存的 raw0 候选与有限检查

候选为 `2026-11-12-fd2d-metric-inverse-q-raw0-candidate-01.json`。
它替换最外 raw0；深端是原 raw1 的外端，同一输入约为

\[
a=.3808860058501116,\quad
w_0=.003991159062404631,\quad w_{r,0}=-.0001047846233821564.
\]

外端 b=13/20、w1=1/10、s1=−7/b。degree32，κ约 .42191565308926765。
原优化实际 session97765 返回 exit0；这个样本的 SLSQP 正常收敛。

独立 MJS 求值实际 session19135 返回 exit0，运行 3.699 秒。
`2026-11-12-fd2d-metric-inverse-q-raw0-provider-check-01.json` 记录4097个
径向采样点及完整端值：

|量|实际有限求值|
|---|---:|
|γ=\|Hinner/Hcut\||.09595427342001057|
|端值校准 c|−7.549516567451064e−15|
|背景母线曲率最大绝对值|6.9523130715755075|
|单位参考 Γ 最大绝对值|972.0276845873278|
|单位参考 II 行和最大值|329.2636284594819|
|校准方程残差 (21) 最大值|4.917992229070451e−13|
|512/1024 积分格的 logw 最大差|7.993605777301127e−15|

这些值只说明局部设计方向可计算且有显著改善，尚未证明全连续范围。
尤其 γ 大于旧首格的 .04707402625：保持深 source 后，原 raw1 的单位
cut 振幅可能增加。因此全尾消费者必须重新计算完整 bounded line，不能把
局部 329 与旧整尾 565353 的比例当成新整尾的改善倍数。

## 8. 可直接使用的预算与下一类有限设计

背景两条主曲率为

\[
\kappa_r=\frac{w_r}{(1+w^2)^{3/2}},\qquad
\kappa_\theta=\frac{w}{r\sqrt{1+w^2}}.
\tag{22}
\]

写 y=w/√(1+w²)，便有 y_r=κr。故任一背景曲率上界 K 都给准确必要条件
ℓ≥|y1−y0|/K，并可用两端的 K-Lipschitz 锥限制中间可选峰高。
这比只限制源 cap 或 canonical L 更直接。

对任意 H∈C²([a,b])，若 |Hrr|≤M，写 v0=Hr(a)、v1=Hr(b)，
S=|H(b)−H(a)−(v0+v1)ℓ/2|，则

\[
M\ge\frac{2S+\sqrt{4S^2+\ell^2(v_1-v_0)^2}}{\ell^2}.
\tag{23}
\]

证明：令 v=Hr，|v′|≤M。端速度差要求 Mℓ≥|v1−v0|。
在这些端值与 Lipschitz 常数下，v 的积分上下极值由两条端点斜率 ±M
直线的上下包络取得。计算两块三角形面积，得到
S≤[M²ℓ²−(v1−v0)²]/(4M)；解二次不等式即得 (23)。
这一推导只给该固定端值线性函数的必要预算，未推出完整非线性面不存在。

旧 raw0 的实际端值给 (23) 约195.2224，而实际峰约565000，所以分配
物理宽度确有优化空间。放大到 h=.05 时，同样旧端值和旧宽度也不能直接
保证小曲率；cut 半径、cut 斜率、有限格的端增益以及 prefix 的相同 g
传递都可以共同重设。

本组后续实际工作由几何分支消费这一完整 bridge 与未改深 source；本分支
继续自由增益、cut 斜率和多段 inverse 构造。这里没有添加独立审查、C³
正则性或超出题目原完成标准的验收门。
