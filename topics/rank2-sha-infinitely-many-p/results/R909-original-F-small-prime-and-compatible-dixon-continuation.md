# R909 — 原 F 的小素数精确矩阵、PARI 基与兼容 Dixon 续接

日期：2026-11-16。**状态：算法保持与精度续接已证明；§7的真实公开计算现已通过全部特征零认证，原F17映射确实存在。原P、RR及主目标仍开。**

本篇将 R906 已证明的精度续接用于同一个原 F 映射。本篇发布时R905的run43899744213/job133412821010仍运行。其随后N256全窗/QQ/短支已过，但在高Sage基6123扩展后exit137；完整记录见R905§7，本篇自身PARI任务继续。R899 首轮公开日志已经把主要耗时定位到大辅助素数下的底域消元、选行和求逆；本篇没有尚未测得的加速结论。

## 1. 同一原问题与完整空间

固定原曲线
$$
E:y^2=x^3+17,\qquad Q=q^6,
$$
原归一化 newform $f(q)=qf_0(Q)$、原 $\eta(Q)^{12}$ 和原 Newton 支 $U(Q)$ 都保持。令
$$
\mathcal E(Q)=\prod_{n\ge1}(1-Q^n)^{12},\qquad
V(Q)=\mathcal E(Q)U(Q)=-1+5Q+\cdots.
$$
仍在 $\Gamma_0(867)$ 上求
$$
V=A/B,\qquad A\in M_{10},\quad B\in M_4. \tag{1}
$$
其维数分别为936、324，完整低矩阵是
$$
\mathcal M z=([Q^j](A-VB))_{j=0}^{1428}, \tag{2}
$$
共1429行、1260列。R904 的权二分母排除不变；本篇只运行权四。

本篇从 R905 producer blob c03bb33f8da0e9f6f047259428ac461e4708ece2 派生，并使用 R892 的完整 PARI 有理 $M_2$ 基。R892 已证明：这只是同一有理空间的基变换，原坐标存在与最终恒等式不变。乘积基仍通过完整 Sturm 前缀的非零最大子式达到准确维数；同一 seed20261116 与 product prime1000037 保持。

这里没有把旧 Sage 基的坐标移到 PARI 基中。新候选只能消费本次实际 forms2、完整 recipes 和低/高前缀。

## 2. 合格辅助素数与精确矩阵

只在公开 Actions 中按递增素数搜索 $[1000000,1001000]$，选择首个满足：

1. $\ell>6\cdot1428+1$；
2. 原两组完整有理乘积基的全部低系数分母是 $\ell$-单位；
3. 原 $M_{10}$ 的1021项 Sturm 前缀模 $\ell$ 秩936，原 $M_4$ 的409项前缀秩324。

原 $f_0$ 和 $\mathcal E$ 系数为整数，原 Newton 支的必要分母由第一项保证为单位。有限搜索失败只记未认证。

沿 R906 已亲读的 Sage10.6 源码，强制使用精确有限域实现 linbox-double，并打印/断言实际类的模块为 matrix_modn_dense_double；上限94906266仍检查。这不是浮点容差秩。依据见 R906§1 及其中固定源码和官方文档。

在选定素数上构造(2)的全部行、全部列。完整消元选原 pivot 列 $J$，按原规则选首个 free 列 $f$；再从 $J$ 列中选独立行 $I$，令
$$
B_0=\mathcal M[I,J]\bmod\ell,\qquad
z_f=1,\quad z_j=0\quad(j\notin J\cup\{f\}). \tag{3}
$$
只求一次 $B_0^{-1}$。初始解必须通过全部1429行及原 $A,B$ 首阶/首项检查。

**命题1。** 改用上述合格辅助素数和完整 PARI 基，不改变任何被最终接受的原 F 映射。

**证明。** (2)是同一特征零线性关系的好约化；完整基与单位分母保证没有删行、删列或缩小输入空间。基变换仅改变表示。若模矩阵满列秩，其非零子式在特征零仍非零，只能排除(1)这两个指定空间中的表示。否则模核只是候选起点，最后仍须在 $\mathbf Q$ 检查第4节的同一完整恒等式及原首支。任何接受的候选因此仍是原问题的解。证毕。

$\ell$ 只是固定特征零映射的辅助重建素数，不是主目标里变化的算术素数 $p$。

## 3. 从已验证全窗的精度真正续接

设在 $\ell^n$ 已取得通过全部(2)的归一化向量，其 pivot 部分取整数代表 $x_n$。新精度 $N>n$ 时，用原 Newton 支、同一有理基重新构造
$$
B_N=\mathcal M[I,J]\bmod\ell^N,\qquad
b_N=-\mathcal M[I,f]\bmod\ell^N.
$$
Newton 方程的逐阶唯一性和单位分母保证与旧矩阵模 $\ell^n$ 兼容。故
$$
e_n=(b_N-B_Nx_n)/\ell^n\in\mathbf Z^{|J|}. \tag{4}
$$
实现逐坐标检查此整除。以后只做新的数字：
$$
d_j=B_0^{-1}(e_j\bmod\ell),\qquad
x_{j+1}=x_j+\ell^j\widetilde d_j,\qquad
e_{j+1}=(e_j-B_N\widetilde d_j)/\ell. \tag{5}
$$

**命题2。** 每一步(5)为整除，且
$$
e_j=(b_N-B_Nx_j)/\ell^j.
$$
最后 $x_N$ 是该方阵唯一的模 $\ell^N$ 解，且 $x_N=x_n\bmod\ell^n$。

**证明。** 起点是(4)。模 $\ell$ 有 $B_N=B_0$，所以(5)的分子被 $\ell$ 整除。将 $x_{j+1}$ 代入即得归纳不变式。$B_0$ 可逆给终点唯一性；所有新加项都被 $\ell^n$ 整除，给兼容。初次取 $n=0,x_0=0,e_0=b_N$，恰为 R905。证毕。

所有 free 坐标和模 $\ell$、模旧 $\ell^n$ 的完整向量仍逐一检查。随后释放唯一高精度方阵，并重新形成实际 $A,B,V$，检查(2)的全部1429行。方阵满足不代替完整行满足；未选行失败只拒绝本 chart，不排除其它原表示。

本次精度表为512、1024。在512位失败于有理恢复、原短支或完整证书时，只有已通过全部模行的向量才进入续轮；1024位从这些旧向量开始。有限精度耗尽只记未认证，没有假定坐标高度界。模向量仅留在当前 Actions 进程内，不保存为输出文件。

## 4. 原完整特征零接受门逐字保持

producer 中 product_rows、initial_exact_check、strict_original_certificate、eta12_unit、e2_series 的函数正文相对 R905 均保持。每个候选的全部1260个坐标先返回 $\mathbf Q$，保(3)归一化；再检查原短支和 $B$ 的准确首阶。

最终使用同一实际 PARI 基扩到原精度，并逐项核对所有低前缀。令
$$
\Delta=Q\mathcal E^2,\quad H=Qf_0^3\mathcal E,\quad
C=(QA')B-A(QB')-\tfrac12 E_2 AB.
$$
接受仍要求准确检查第零项到第6120项的原恒等式
$$
8\Delta C^3-HB^2(A^2-17\Delta B^2)^2=0. \tag{6}
$$
原完整 Sturm 上界6120不缩短；还保 $V=-1+5Q+\cdots$、$C$ 首项、实际无穷点以及
$$
y=\frac{A}{\eta(Q)^{12}B},\qquad
x=\frac{f(q)(A^2-17\Delta B^2)}{2\eta(Q)^{12}C},
\qquad \frac{dx}{2y}=f(q)\frac{dq}{q}.
$$
只有(6)通过才设置 CERTIFIED_FIRST_FACTOR_SOLUTION。没有假定 Manin 常数为1，没有以模残差或矩阵核替代原完整映射证书。

## 5. 可重算执行与下一接受条件

新增源码与请求：

- scripts/original_f_small_prime_dixon_map.py；
- scripts/produce-r909-original-first-factor-map-small-prime-dixon.py；
- ci/original-F-small-prime-dixon-request.json；
- .github/workflows/rank2-sha-original-F-small-prime-dixon.yml。

仍用固定 Sage10.6 镜像、只读源码、无网具名容器、退出清理和 source/run/两README身份。数学只在公开 Actions 中执行。各阶段记录实际时间、矩阵类型、选定素数、完整 residual/坐标 hash 和完整最终接受门。

后续原 shadow 消费还要求另一原 P 映射、完整 RR 和全部绝对端点/边界输入都实际通过。本篇不把实现完备或一次辅助素数的模核记为这些门已经通过。


## 6. 实际公开执行

source135b50ff04a12c51dd1b9de583a20b2bed19cbed 触发 [run43906594646](https://github.com/Rogerhu12/math-research-public/actions/runs/43906594646)，job133436977753，2026-11-16 16:21:34 UTC创建。16:21:56 UTC已亲读数学步骤运行；尚无结果，不先记PASS。选定素数、精度历史及最终hash依实际完整日志登记。

## 7. 已完成的原完整 F 映射证书

**已证明（公开精确特征零计算与 R878 的全局认证定理）。**
source135b50ff04a12c51dd1b9de583a20b2bed19cbed 的
[run43906594646](https://github.com/Rogerhu12/math-research-public/actions/runs/43906594646)、
job133436977753，于2026-11-16 16:33:13 UTC完成全部数学步骤，任务最终success。
参数就是本篇已提交request；固定Sage10.6、PARI2.17.1、seed20261116及同一镜像。
实际执行642.035482068秒。

完整结果SHA-256：
5193c929a0369e957a0495f12c5af244243f2b4ed444ba305bba963dfdc4831f。

程序选定的首个合格辅助素数为1000003；实际矩阵类型确为
sage.matrix.matrix_modn_dense_double.Matrix_modn_dense_double。
原完整1429×1260矩阵秩1116，首free列1005、原$B$首阶1。
在512位、10205bits即完成，未使用1024位续轮。全部1429行、全部1260个有理坐标恢复、
原精确短支、同一PARI基的6123项扩展与完整低前缀重现均通过。

最关键的实际接受字段为
$$
\text{full\_0\_through\_bound\_identity}=\mathrm{true},
\qquad \text{sturm\_bound}=6120,
$$
并且最终
$$
\boxed{\text{certified\_original\_first\_factor}=\mathrm{true}.} \tag{7}
$$
它来自完整特征零(6)，不是模素数或模素数幂残差的替代。

| 身份 | SHA-256 |
|---|---|
| producer | 347f7a2cac422808f2d1c48f879cf80f5a37da3dc6ace6b436d14f4a7586949d |
| 精确小素数/续接helper | 3ad1e0e6f610fed59c0893b8b1eb36c115fb94d650e0aae7015138b359340610 |
| 完整有理坐标 | 4543c651797de77545ee53d7f72428a3ae1a0bc05a563a966014a966103495e4 |
| 同一高精度M2基 | 961501516f83237c4b624151cb94abd77b7fc00159e6744362700378f174eb2b |
| 权10 recipes | 567b8fcaa45c523f003b8500eeec0d89a1fde592a2d53e3db172d60078bd7db8 |
| 权4 recipes | 93e884ba0f5f4c932106f5030a7b8372672ad4ad29156722d68d7cb728560d71 |
| 完整1429行零residual | fd5792a67901bd6c2302435071819bdf1e5f212da6a7760abe65792962eb2fd6 |
| 完整原newform输入 | 1e35bdedc13a4c9467563093e3635544dd1c786c3995f1cb7bfe910546c04015 |

**定理3（原第一映射确实存在）。** 同一原曲线上存在已由本次确定性producer构造的
$$
F_{17}:X_0(10404)\longrightarrow E_{17}:y^2=x^3+17
$$
满足
$$
F_{17}(\infty)=O,\qquad
F_{17}^{*}\frac{dx}{2y}=f(q)\frac{dq}{q},\qquad
x=q^{-2}+O(q^4),\quad y=-q^{-3}+O(q^3).
\tag{8}
$$
特别这一归一化是实际态射，不再只是形式支；其次数$d_F\ge1080$。

**证明。** 取同一进程中经(7)认证的完整有理坐标及实际PARI基/recipes，按§4定义$A,B,C$。
程序逐项检查第0项至第6120项的(6)，且所有高精度基完整重现低前缀。
$A,B$分别为权10、4的真实全局模形式；$C$为权16的Serre导数差。
故(6)两边都是权60全纯模形式。完整Sturm界6120使该恒等式全局成立。
原首项和$B$首阶已逐项验证，因此§4的坐标式定义非恒定有理函数，
由 R878§§2、5的全部有限角色下降得到原$X_0(10404)$上的实际有理映射。
同一恒等式给$y^2=x^3+17$和原微分；已核首支固定无穷点为$O$。
源和目标光滑射影，使其自动处处延拓。最后 R904附录A的条件下界现适用，
给$d_F\ge1080$。证毕。

本定理没有预设Manin常数，没有改变原$F$因子的CM尺度
$\theta_{17}$、Artin/旧副本倍率或原交点公式。
后续消费者须在本进程接收实际坐标/基，或按同一已提交producer重算。
仅有hash不是可求值的坐标对象；本篇依根规则15不另存可重算系数。

实际计时也已分开：底域chart/逆在约199.62秒完成，
完整512位残差约496.19秒，PARI高基扩展约566.25秒，
完整最终证书约642.04秒。它支付当前F计算；不同基、prime和实现同时变化，
不把与R905的总时差归因于某个未经隔离测量的单一原因。

原P映射、完整RR与全部shadow消费者仍需各自实际证书；
本定理不赋原AJ、ordinary localization或无穷目标素数的非零。
