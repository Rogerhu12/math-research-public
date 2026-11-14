# R80：准确 affine 族的全核心固定时间一、二阶参数源

2026-11-12，constructive-route。以下证明和有向有限证书共同给出同一准确
affine 族在完整闭核心、整个实际参数管、物理复角带上的参数源界：
\[\boxed{|f_\sigma|<4,\qquad |\partial_p f_\sigma|<20,\qquad
|\partial_p^2 f_\sigma|<200.}\]
其中两分支均包含，时间固定为真实转向坐标 \(\tau\in[-\pi/2,\pi/2]\)，
参数与角域在下文精确定义。167 个原始共同 span 经两次二分得到
169 个通过的闭叶，完整转折区另由真实 Q 消根控制。
这些是连续源界；没有使用差商或旧八条浮点射线，也没有据此声称实际
积分平均、非零 twist、完整流参数预算或 R31 门已完成。

## 1. 对象和固定时间

采用 R73/R75 的准确中心和参数管
\[
p_0=-7789843107295549/4611686018427387904,\qquad
I=[p_0-1/2000000,p_0+1/2000000].
\]
原点 0d17500a…、方向 8db5d57d…；先施加 affine 控制点/均值方向，
再施加固定 base 权重和准确偶奇对称化。角原函数是完整无限 R33 primitive。
径向 target 同步为 \(g_0(p)=E(r,p)dr^2+a(r,p)^2d\theta^2\)，
\(E=\langle F_r\cdot F_r\rangle\)。

正根 \(t(p)\) 属于 R57 的同一简单根分支。固定
\(\tau\in[-\pi/2,\pi/2]\)，令 \(s=\sin\tau,\ c=\cos\tau\ge0,\ r=t(p)s\)。
记 \(X=F_r,T=F_\theta/a\)。Cartesian 表达下
\[
D=(X\times T)\cdot T_\theta,\quad
M=(X\times T)\cdot T_r,\quad
W=(X\times T)\cdot(X\times T).                         \tag{1}
\]
这等于 R59 native moving-frame 的 D、M、W，其符号约定中
\(N_{\rm raw}=-a^2D,M_{\rm raw}=-a^2M,G=a^2W\)。
解析点积是双线性的；复 Euclidean 范数只用于上界。

令 \(Q=-K_0(t(p)s,p)/(1-s^2)\)，端点按 R58 可去奇延拓。两实际分支为
\[
f_\sigma=-tc\{M+\sigma c\sqrt Q\,W\}/D,\qquad \sigma=\pm1. \tag{2}
\]
本文的参数导数固定 \(\tau,\theta\)。故 \(r_p=s t'\)、\(r_{pp}=s t''\)，
且 (2) 外面的 t 也必须微分。

## 2. 真无限图的两个参数导数

固定 r 时 \(\beta,\gamma,a,Z\) 对 p 都 affine。令角相位
\(b=\beta(\theta),g=\gamma(\theta),b_1=b_p,g_1=g_p\)。
旋转基中的 \(T=(-\cos g\sin b,\cos g\cos b,\sin g)\) 给
\[
T_p=(\sin g\,g_1\sin b-\cos g\cos b\,b_1,\
-\sin g\,g_1\cos b-\cos g\sin b\,b_1,\ \cos g\,g_1),       \tag{3}
\]
\[
\begin{aligned}
(T_{pp})_1&=\cos g\sin b(b_1^2+g_1^2)+2\sin g\cos b\,b_1g_1,\\
(T_{pp})_2&=-\cos g\cos b(b_1^2+g_1^2)+2\sin g\sin b\,b_1g_1,\\
(T_{pp})_3&=-\sin g\,g_1^2 .
\end{aligned}                                                   \tag{4}
\]
线性原函数与参数导数交换，所以
\[
F_p=a_p\mathcal PT+a\mathcal PT_p+Z_pe_z,\qquad
F_{pp}=2a_p\mathcal PT_p+a\mathcal PT_{pp}.                \tag{5}
\]
第二式的 \(a_{pp},Z_{pp}\) 因准确标量族 affine 而为零；非线性几何量
没有被当作 affine。令 \(X_p=\partial_rF_p,X_{pp}=\partial_rF_{pp}\)，则
\[
E_p=2\langle X\cdot X_p\rangle,\quad
E_{pp}=2\langle X_p\cdot X_p+X\cdot X_{pp}\rangle .         \tag{6}
\]

有限 Fourier 部分在完整保留模式上求准确系数均值。
若有限 \(X,X_p,X_{pp}\) 每个 Cartesian 分量的模界为 \(M,M_p,M_{pp}\)，
无限误差为 \(e,e_p,e_{pp}\)，则三个均值的完整误差界为
\[
3(2Me+e^2),\qquad 6(Me_p+M_pe+ee_p),
\]
\[
6(2M_pe_p+e_p^2+Me_{pp}+M_{pp}e+ee_{pp}).                 \tag{7}
\]
二阶的 \(X_p\cdot X_p\)、误差平方和两个误差交叉项均保留。

每个实际 scalar germ 的外径向圆取 \(R_0=.003\)、均值圆取
\(R_E=.0025\)，归一角外带 .32（物理角 .08）。
原始与方向多项式先完整展开，再求整圆 majorant。
若两个方向相位的界为 \(B_1,G_1\)，二阶 primitive 的半径因子可取
\[
A_2=2|a_p|(B_1+G_1)+|a|(B_1+G_1)^2,                    \tag{8}
\]
乘原相位的 \(e^{B+G}\)，代入同一线性 Fourier 尾预算。高度二阶项为零。
对三种 F 独立支付角 alias/tail，在 \(R_E\) 上用 Cauchy 支付径向导数，
再用 (7) 支付真实 E 的混合导数。复径向圆属于各自固定多项式的解析延拓，
没有把实际分片样条说成跨 knot 全纯。

## 3. 曲率和移动根链式

写 \(C=a_rE_r-2a_{rr}E,\ K=C/(2aE^2),\ L=a_p/a+2E_p/E\)，准确有
\[
\begin{aligned}
C_p&=a_{rp}E_r+a_rE_{rp}-2a_{rrp}E-2a_{rr}E_p,\\
C_{pp}&=2a_{rp}E_{rp}+a_rE_{rpp}-4a_{rrp}E_p-2a_{rr}E_{pp},\\
L_p&=-(a_p/a)^2+2E_{pp}/E-2(E_p/E)^2,\\
K_p&=C_p/(2aE^2)-KL,\\
K_{pp}&=C_{pp}/(2aE^2)-2K_pL-K(L^2+L_p).
\end{aligned}                                                   \tag{9}
\]
区间除法只在闭单元 \(a,E>0\) 后执行。所用阶数仅为
\(K,K_r,K_{rr},K_p,K_{rp},K_{pp}\)，不使用人为补零的更高阶。

在 \(0\le s\le999/1000\)，固定真实时间的链式为
\[
\dot K=K_p+s t'K_r,\quad
\ddot K=K_{pp}+2s t'K_{rp}+s^2(t')^2K_{rr}+s t''K_r.     \tag{10}
\]
于是 \(Q=-K/(1-s^2),Q_p=-\dot K/(1-s^2),Q_{pp}=-\ddot K/(1-s^2)\)。
若直接闭区间没有证明 \(Q>0\)，程序细分并保留失败记录。

在 \(999/1000\le s\le1\)，使用完整 R58 已付的 \(Q,Q_p,Q_{pp}\)：
\[
Q=\frac{t}{1+s}\int_0^1K_r(t(1-v(1-s)),p)\,dv.            \tag{11}
\]
R58 已对 (11) 作两次完整参数链式，且在更大
\(|p|\le\operatorname{binary64}(.01)\) 上支付。先使用 (11)，再对正 Q
开平方，端点因此不出现对近零 \(-K\) 求导后留下的伪奇项。

## 4. 全角、无限 primitive 的几何 majorant

令 \(\phi=\theta+\beta\)，则 \(T=R_z(\phi)R_x(\gamma)e_y\)。
复旋转范数至多 \(e^{|\Im\phi|},e^{|\Im\gamma|}\)，相位生成矩阵范数至多 1。
故每个 \(\partial_\beta^j\partial_\gamma^kT\) 的范数均不超过
\(e^{|\Im\phi|+|\Im\gamma|}\)。
若 B、G 是非恒定 r,p 增量的非负系数 majorant，归一化混合 jet 逐系数受
\[
e^I\exp(B+G),\quad
I=S+\sum_k|\beta_k|\sinh(4kS)+\sum_k|\gamma_k|\sinh(4kS)   \tag{12}
\]
控制。常数只计虚部，没有把实相位放入常数指数。

Cartesian T 及其 r,p 导数都零均值：水平 quarter-rotation 和竖向奇对称
分别使均值为零。唯一零均值原函数的卷积核为
\[
(\mathcal PT)(\theta)=\frac1{2\pi}
 \int_0^{2\pi}(\pi-v)T(\theta-v)\,dv .
\]
核的 \(L^1\) 范数为 \(\pi/2\)，同样适用于每一条复水平线。因此
\[
\|\mathcal PT\|_\infty\le(\pi/2)\|T\|_\infty .            \tag{13}
\]
这是完整无限原函数的界。

可取
\(\mathcal X=(\pi/2)\partial_r(\mathcal A\mathcal T)+\mathcal Z_r\)，
\(\mathcal T_r=\mathcal T(B_r+G_r)\)，
\(\mathcal T_\theta=\mathcal T(1+B_\theta+G_\theta)\)。
复向量 cross/dot 范数不等式再给
\[
\mathcal D=\mathcal X\mathcal T\mathcal T_\theta,\quad
\mathcal M=\mathcal X\mathcal T\mathcal T_r,\quad
\mathcal W=(\mathcal X\mathcal T)^2.                      \tag{14}
\]

jet 按 \(r^i p^j\) 的归一化系数存储。对任意 majorant V，沿 \(r=t(p)s\)
的归一化参数零、一、二阶界是
\[
V_{00},\quad V_{01}+|s t'|V_{10},\quad
V_{02}+|s t'|V_{11}+|s t'|^2V_{20}+|s t''|V_{10}/2.       \tag{15}
\]
最后的 1/2 及中间项没有额外的 2 都来自归一化约定。

R73 在整个 I、实核心、物理角带 S=1/56 上已付
\(|N_{\rm raw}|\ge n_*>0\)。令 \(d_*=n_*/a_{\max}^2\)，则 \(|D|\ge d_*\)。
如 \(v=A/D\)，归一化参数模界递推为
\[
v_0\le A_0/d_*,\quad
v_1\le(A_1+D_1v_0)/d_*,\quad
v_2\le(A_2+D_1v_1+D_2v_0)/d_*.                          \tag{16}
\]
零阶再与 R73 的 \(|M/D|,|W/D|\) 界相交。对正 Q，平方根的归一化界为
\[
\sqrt{Q_{\max}},\quad \frac{|Q_p|}{2\sqrt{Q_{\min}}},\quad
\frac{|Q_{pp}|}{4\sqrt{Q_{\min}}}
+\frac{|Q_p|^2}{8Q_{\min}^{3/2}}.                        \tag{17}
\]
将 (15)–(17)、\((t,|t'|,|t''|/2)\) 及两个 c 因子代入 (2)，得到
完整 \(f,f_p,f_{pp}\) 界。最终二阶系数乘 2。
零阶可以与同一 R75 的 \(|f|<5\) 相交；归档有限核查必须明确确认实际
existence 输入的 coarse_physical_time_field_bound 字段确为 5。

## 5. 闭覆盖与参数 forcing 接口

bulk 使用全部实际正负 scalar knots 的准确有理公共分区，终点为
\(t_{\max}\cdot999/1000\)。每个径向闭单元配合
\[
s\in[r_{\min}/t_{\max},r_{\max}/t_{\min}]\cap[0,999/1000].
\]
递归二分保留准确闭覆盖。turn 使用
\([t_{\min}\cdot999/1000,t_{\max}]\) 中同一个实际 root germ。
两部分在 s 坐标覆盖 [0,1]；准确径向反射覆盖负半面与两分支。

scalar 为 C4、height primitive 为 C5，K 对 r,p 联合 C2。
非根 knot 的左右场二阶 \((\tau,p)\) jet 相同；移动 crossing 没有
delta 型源。根处由 (11) 消去奇性。所以全闭覆盖给整个真实参数管的
连续源，而不是互不相接的局部样本。

任意较小物理角带 \(s_\theta<S\) 上，Cauchy 给
\[
\|\partial_\theta^j f_p\|_{s_\theta}
\le j!\|f_p\|_S/(S-s_\theta)^j
\]
以及相同的 \(f_{pp}\) 公式。

若完整有限参考 \(Y(u,x)\) 与 p 无关、\(q=Y_x\)，固定准确物理半段宽为 h，
则
\[
g_0=(h f(Y)-Y_u)/q,\quad g_1=h f_p(Y)/q,\quad
g_2=h f_{pp}(Y)/q.                                      \tag{18}
\]
没有额外乘 4；初始标签 x 的规范已经在 q 中。完整实时像落在 S、
\(|q|\ge m\) 时，参数源分别有 \(|h|\|f_{p^j}\|/m\) 界。
这些粗界支付 R82 高阶余项；非零平均仍要保留有符号有限 \(g_1\) 及连续误差。

fourfold_phase_real_parameter_forcing.py 将相同的真实 native
\(F,F_p,F_{pp}\) 接成固定实 \(\tau\)、任意有限复角数组的取值接口：
全部有限 primitive 模、r-chain 项和各自无限尾都保留。
其有限节点报告不能代替整个标签圆、时间积分或真实 twist 证书。


## 6. 已完成的有限证书与重放

源文件 `scripts/fourfold_phase_fixed_tau_parameter_bounds.py` 的 SHA256 为
`0f93dd40ca924fd22a5df1e00e800c0cc0d2db4ac6e5cad753f7e0f3042841b2`。
它以 192 bit、有向 Arb/Acb 运算、Q256 实际角 primitive 和七阶径向
series，完整运行 167 个原始共同闭 span；第 165、166 个初始闭单元的
Q 正性未由粗盒证明，报告保留这两个失败尝试，再各二分为通过叶。
最后没有遗漏单元，没有把初始失败当作通过。

实际主报告为
`data/phase_ring_continuation/type_fixed_step02_d5_step5_fixed_tau_parameter_source_full.json.gz`，
SHA256
`33c2bdddb0c4e1172275b961da0a2e5e23486299168efe80c4cb6870c30dd556`。
其字段 `complete_real_core_parameter_source_proved` 为真，所有 169 个 bulk
闭叶及完整 turn 区都通过。实际机器统计为 CPU 151.225 秒、wall 1389.709 秒；
耗时不是数学输入。

完整连续区域为
\[
p\in I,\quad -\pi/2\le\tau\le\pi/2,\quad
|\Im\theta|\le1/56,\quad \sigma\in\{-1,1\}.
\]
报告的全局有向上端点分别小于
\[
3.583152267975,\qquad19.100211799085,\qquad194.813024648167.
\]
故开头整数 4、20、200 留有明确有理余量。转折部分
\(999/1000\le|\sin\tau|\le1\) 单独有
\[
|f_p|<0.369864157134,\qquad |f_{pp}|<2.468478415449.
\]
这些小数仅是保守的可读摘录；可复核输出保存全部有向球。

同管实际根 jet 的独立输入为
`type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json`，SHA256
`d83fe1e7ab3eed8baaf2448f2f6076212936633c69f58950720f6d372b03d99c`。
它给出
\[
6.11079918\cdot10^{-5}<t'<6.11079982\cdot10^{-5},
\]
\[
-9.40286714\cdot10^{-7}<t''<-9.40286069\cdot10^{-7}.
\]
显示的小数端点不另作准确输入；真正根导数使用 JSON 有向区间。
其请求半径是向上取整的 binary64 值
`5.000000000000001e-7`，严格包含本结果的准确半径 \(1/2000000\)。

另外的有限核验器
`scripts/fourfold_phase_parameter_source_certificate.py`
从准确 frozen scalar knots 独立重建全部共同 span，不信任报告的全局
max 或 completed 标志。它逐叶按 Fraction 核对准确端点、每个 span 的
闭覆盖、所有 169 个 leaf 的通过标志、真实参数/源/依赖 SHA 身份，
重新取全部模界的向外上端点，逐个验证小于 4、20、200。它也显式核对
实际 R75 输入的 `coarse_physical_time_field_bound` 恰为准确整数 5。
结果保存为
`type_fixed_step02_d5_step5_fixed_tau_parameter_source_certificate.json`。
这项有限核验不代替每个 leaf 的解析证明；它确保有限叶确实组装成所称区域。

在课题目录执行：

```bash
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_phase_fixed_tau_parameter_bounds.py \
  --out data/phase_ring_continuation/type_fixed_step02_d5_step5_fixed_tau_parameter_source_full.json.gz
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
python scripts/fourfold_phase_parameter_source_certificate.py \
  --out data/phase_ring_continuation/type_fixed_step02_d5_step5_fixed_tau_parameter_source_certificate.json
```

主扫描支持同身份 `--resume`。在重放期间不替换源或输入；报告中失败的
粗尝试是正常自适应细分记录。参数源全核心证书、完整有符号时间密度和
真流参数导数属于不同结论：后两者仍须连接 R82 的有限积分及其误差。
