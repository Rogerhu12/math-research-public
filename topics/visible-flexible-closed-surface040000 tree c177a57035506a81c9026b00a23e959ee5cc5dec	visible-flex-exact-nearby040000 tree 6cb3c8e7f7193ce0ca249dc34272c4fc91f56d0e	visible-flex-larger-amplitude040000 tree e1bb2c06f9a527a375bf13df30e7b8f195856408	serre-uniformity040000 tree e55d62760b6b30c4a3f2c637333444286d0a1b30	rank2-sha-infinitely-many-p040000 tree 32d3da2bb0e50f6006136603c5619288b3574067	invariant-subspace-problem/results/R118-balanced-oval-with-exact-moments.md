# R118：准确矩补偿的均衡曲率卵形核与同度量端口

2026-11-12，constructive_geometry。

本结果给出一个与 R115 使用**同一准确周长**的中央凸曲线族，并证明其统一曲率半径窗口。
参考曲线的长短轴支持准确为 1.405、.495；参考曲线满足
\(.228<\rho<3.17\)，加权支撑参数球内满足
\(.216<\rho<3.182\)。它可直接替换 R116 的中央数据而不修改 a0 或 frozen a(s)。
这里的结论是完整中央曲线及圆柱段的构造，不声称下游活动核、非线性尾匹配或强目标闭曲面已经完成。

## 1. 参考半径与三个准确矩条件

令 \(L=\pi/2\)，固定原椭圆 \(A_E=7/5,B_E=1/2\)，定义

\[
\ell_E(\theta)=\sqrt{A_E^2\sin^2\theta+B_E^2\cos^2\theta},\qquad
a_0=\frac1L\int_0^L\ell_E(\theta)\,d\theta
=\frac{2A_E E(1-B_E^2/A_E^2)}\pi.
\tag{1}
\]

以下十进制常数均按其有限小数的准确有理数含义使用：

\[
\begin{aligned}
r&=.22921358484022447,&D&=2.9353699772701836,\\
c&=-.6589229731934492,&k&=6,\\
A_*&=1.405,&B_*&=.495.
\end{aligned}
\tag{2}
\]

定义整个实轴上的解析、π 周期、关于两坐标轴对称的函数

\[
H(\phi)=\frac1{1+\exp(2k(\cos2\phi-c))},\qquad
\rho_0(\phi)=r+D H(\phi).
\tag{3}
\]

这里的有限小数只选择一个参考形状，准确约束由以下矩补偿支付。
令

\[
I_0=\int_0^L\rho_0,\quad I_s=\int_0^L\rho_0\sin\phi,\quad
I_c=\int_0^L\rho_0\cos\phi,
\]

\[
\Delta a=a_0-I_0/L,\qquad \Delta A=A_*-I_s,
\qquad \Delta B=B_*-I_c,
\]

\[
u_0=\Delta a,\qquad u_2=\frac32(\Delta B-\Delta A),\qquad
u_4=-\frac{15}2(\Delta A+\Delta B-2\Delta a),
\]

\[
\rho_*(\phi)=\rho_0(\phi)+u_0+u_2\cos2\phi+u_4\cos4\phi.
\tag{4}
\]

所有积分与系数在 (4) 中按准确实数定义；不能用报告里近乎零的浮点 u 值替代这一准确定义。
直接积分给出

\[
\begin{array}{c|ccc}
 &1&\cos2\phi&\cos4\phi\\\hline
\int_0^L(\cdot)\,d\phi&L&0&0\\
\int_0^L(\cdot)\sin\phi\,d\phi&1&-1/3&-1/15\\
\int_0^L(\cdot)\cos\phi\,d\phi&1&1/3&-1/15
\end{array}
\]

因此，无论 (2) 的拟合有多少浮点误差，定义 (4) 总满足

\[
\int_0^L\rho_*\,d\phi=a_0L,\qquad
\int_0^L\rho_*\sin\phi\,d\phi=A_*,\qquad
\int_0^L\rho_*\cos\phi\,d\phi=B_*.
\tag{5}
\]

## 2. 全域曲率半径界的可复现证书

下面既给出计算误差公式，也记录实际通过的区间数据。
不以密集采样或求根器的收敛代替全域不等式。

设 \(f(x)=(1+e^{2kx})^{-1}\)。由
\(f'=-2kf(1-f)\)、\(f''=4k^2f(1-f)(1-2f)\)，
有 \(|f'|\le k/2\)、\(|f''|\le k^2\)。结合
\(|(\cos2\phi)'|\le2\)、\(|(\cos2\phi)''|\le4\)，得到

\[
|\rho_0'|\le Dk=:M_1,\qquad
|\rho_0''|\le D(2k+4k^2)=:M_2.
\tag{6}
\]

因为 \(0<H<1\)，\(r<\rho_0<r+D\)。乘积求导又给出

\[
|(\rho_0\sin\phi)''|,
|(\rho_0\cos\phi)''|\le M_2+2M_1+r+D=:M_{2m}.
\tag{7}
\]

记 \(d=A_E^2-B_E^2\)，由对 \(\ell_E\) 直接求导，

\[
|\ell_E''|\le d/B_E+d^2/(4B_E^3)=:M_{2E}=9.2682.
\tag{8}
\]

对长度 L 的区间使用 N 个等长中点单元，Taylor 积分余项给

\[
\left|\int_0^Lf(x)\,dx-\frac LN
\sum_{j=0}^{N-1}f\!\left(\frac{(j+1/2)L}N\right)\right|
\le\frac{\|f''\|_\infty L^3}{24N^2}.
\tag{9}
\]

证明是逐单元在中点展开一阶项；该项积分为零，二阶余项积分至多
\(\|f''\|_\infty(L/N)^3/24\)，再对 N 个单元求和。
脚本 `fd2d_balanced_oval_certificate.py` 对所有中点、π、指数、三角函数及求和使用
45 位十进制区间运算，并按 (6)–(9) 扩张四个积分。
在实际 \(N=2048\) 的运行中，得到以下向外放宽的区间：

\[
\begin{aligned}
a_0&\in[1.00408261084,\ 1.00408306520],\\
|u_0|&<.000011451394,\\
|u_2|&<.000057433246,\\
|u_4|&<.000459021410,\\
|u_0|+|u_2|+|u_4|&<.000527906049.
\end{aligned}
\tag{10}
\]

完整外包端点及各余项见
`notes/2026-11-12-fd2d-balanced-oval-moment-certificate.json`。
其原始未放宽结果还给

\[
\rho_*(\phi)>.22868567879>.228,\qquad
\rho_*(\phi)<3.16511146816<3.17
\quad(\phi\in\mathbb R).
\tag{11}
\]

这一步只使用 \(r<\rho_0<r+D\) 及 (10)，不需要定位 \(\rho_*\) 极值。
证书的四个比较项全部为 true，`passed=true`。

## 3. 准确闭曲线、支撑函数及其共同弧长

在第一象限定义

\[
\Gamma_*(\phi)=\left(A_*-\int_0^\phi\rho_*(t)\sin t\,dt,
\ \int_0^\phi\rho_*(t)\cos t\,dt,\ 0\right),
\quad0\le\phi\le L.
\tag{12}
\]

由 (5)，两端准确为 \((A_*,0,0)\)、\((0,B_*,0)\)。令
\(\nu=(\cos\phi,\sin\phi,0)\)、\(T=(-\sin\phi,\cos\phi,0)\)，则
\(\Gamma_*'=\rho_*T\)。将 (12) 按坐标轴反射延拓一周。
由于 \(\rho_*\) 是 \(\cos2\phi\) 的解析函数再加两个偶频模式，
它在两轴处的全部奇数阶导数为零；反射延拓与全局方程
\(\Gamma_*'=\rho_*T\) 一致，故曲线解析。
π 周期的 \(\rho_*\) 保证
\(\int_0^{2\pi}\rho_*T\,d\phi=0\)，所以曲线准确闭合。

为说明严格凸与嵌入，不另加隐含假设。固定 φ，如果
\(\psi\in[\phi,\phi+\pi]\)，则

\[
(\Gamma_*(\psi)-\Gamma_*(\phi))\cdot\nu(\phi)
=\int_\phi^\psi\rho_*(t)\sin(\phi-t)\,dt\le0,
\]

且两端以外严格小于零。另一半周从 \(\phi+2\pi\) 向后积分得到同样结论。
故每个 φ 的切线都是全曲线的唯一支撑切线，正曲率使参数正则，曲线是严格凸嵌入。
设其支撑函数为 \(h_*=\Gamma_*\cdot\nu\)。直接微分得到

\[
\Gamma_*=h_*\nu+h_*'T,\qquad h_*+h_*''=\rho_*.
\tag{13}
\]

再取任意有限 M，\(m_j=2j,c_j=1-m_j^2\)，定义

\[
h_q=h_*+\sum_{j=1}^Mq_j\cos(m_j\phi),\qquad
\rho_q=\rho_*+\sum_jc_jq_j\cos(m_j\phi),\qquad
\Gamma_q=h_q\nu+h_q'T.
\tag{14}
\]

在全参数域 \(\sum_j(m_j^2-1)|q_j|<.228\) 内，\(\rho_q>0\)，
上述支撑切线证明仍适用。全部修正项均为零均值，故

\[
\operatorname{length}(\Gamma_q)=\int_0^{2\pi}\rho_q\,d\phi=2\pi a_0.
\tag{15}
\]

定义 \(S_*(\phi)=\int_0^\phi\rho_*\)，以及

\[
S_q(\phi)=S_*(\phi)+\sum_j\frac{c_jq_j}{m_j}\sin(m_j\phi),\qquad
S_q(\phi_q(\sigma))=a_0\sigma.
\tag{16}
\]

其反函数光滑、严格单调并与周数相容。材料角为 σ；法向角 φ 会随 q 变化。
令 \(\gamma_q(\sigma)=\Gamma_q(\phi_q(\sigma))\)，则

\[
\gamma_{q,\sigma}=a_0T,\qquad
\gamma_{q,\sigma\sigma}=-a_0^2\nu/\rho_q.
\tag{17}
\]

因此中央柱段 \(X_q(s,\sigma)=\gamma_q(\sigma)+se_z\) 的完整两 jet 为

\[
X_s=e_z,\quad X_\sigma=a_0T,\quad
X_{ss}=X_{s\sigma}=0,\quad X_{\sigma\sigma}=-a_0^2\nu/\rho_q,
\tag{18}
\]

并且诱导度量准确为 \(ds^2+a_0^2d\sigma^2\)，对所有 q 相同。
在 R116 的法向约定 \(N=e_z\times T=-\nu\) 下，中央正交第二基本形式为
\(l=m=0,n=1/\rho_q\)。

## 4. 全部参数导数及固定参考角

在固定 σ 下，(16) 给

\[
\partial_{q_j}\phi_q=-\frac{c_j\sin(m_j\phi_q)}{m_j\rho_q}.
\tag{19}
\]

按 R115 的相同直接微分过程，完整位置导数为

\[
J_j=\partial_{q_j}\gamma_q
=\cos(m_j\phi_q)\nu-\frac{\sin(m_j\phi_q)}{m_j}T,
\]

\[
J_{j,\sigma}=\frac{c_ja_0\sin(m_j\phi_q)}{m_j\rho_q}\nu,
\]

\[
J_{j,\sigma\sigma}=\frac{c_ja_0^2}{m_j}
\left[\left(\frac{m_j\cos(m_j\phi_q)}{\rho_q^2}
-\frac{\rho_q'\sin(m_j\phi_q)}{\rho_q^3}\right)\nu
+\frac{\sin(m_j\phi_q)}{\rho_q^2}T\right],
\tag{20}
\]

\[
\partial_{q_k}J_j=-\frac{c_jc_k\sin(m_j\phi_q)\sin(m_k\phi_q)}
{m_jm_k\rho_q}\nu.
\tag{21}
\]

这些公式只依赖 (14)、(16)，不需要基准是椭圆。
中央 (18) 中三个含 s 的参数导数仍全为零。
若直接需要 \(n=1/\rho_q\) 的固定材料角 JVP，令
\(\dot\phi=\sum_j\dot q_j\partial_{q_j}\phi_q\)，则

\[
\dot n=-\rho_q^{-2}\left(\rho_q'\dot\phi+
\sum_jc_j\dot q_j\cos(m_j\phi_q)\right).
\tag{22}
\]

为了保持既有偏心角 GC 网格，取**原** (1.4,.5) 椭圆的固定映射
\(\sigma=r_E(\theta)=S_E^{\mathrm{ecc}}(\theta)/a_0\)，
其中 \(r_E'=\ell_E/a_0\)、\(r_E''=\ell_E'/a_0\)。
全部曲线、两 jet、参数导数按该同一映射复合，
一阶角导数乘 \(r_E'\)，二阶按
\(D_\theta^2=D_\sigma^2(r_E')^2+D_\sigma r_E''\) 转换。
整个潜在活动核目标度量仍为
\(ds^2+(a(s)/a_0)^2\ell_E(\theta)^2d\theta^2\)。
不能把 A*=1.405、B*=.495 代入这条基准角映射，也不能用随 q 变化的法向角替代材料角。
尾 DN 的 Fourier 材料角仍是 σ。

## 5. 统一强中央窗口与可继承的固定帽条件

取

\[
\sum_j(m_j^2-1)|q_j|\le .012.
\tag{23}
\]

由 (11)，整个参数球满足

\[
\frac{27}{125}=.216<\rho_q<3.182=\frac{1591}{500},\qquad
\frac{500}{1591}<n<\frac{125}{27}<4.630.
\tag{24}
\]

因 \(m_j^2-1\ge3\)，有 \(\sum|q_j|\le.004\)。两轴支持为

\[
A_q=1.405+\sum_jq_j\ge1.401,\qquad
B_q=.495+\sum_j(-1)^jq_j\le.499,
\]

\[
A_q-B_q=.91+2\sum_{j\ {m odd}}q_j\ge.902.
\tag{25}
\]

因此 π/2 相位中央轴见证对原中央柱段的距离至少 .902。
参考曲线在矩形 \([-A_*,A_*]\times[-B_*,B_*]\) 内，故其支撑值不超过
\(\sqrt{A_*^2+B_*^2}\)，加支撑扰动后整个中央平面曲线在半径
\(\sqrt{A_*^2+B_*^2}+.004<1.494\) 的圆盘内。

令 \(r_c=.216\)。由 (24)，\(h_q-r_c\) 的曲率半径仍严格正，且π周期使其定义
一个中心对称凸体。因此 \(h_q\) 对应的凸体是该凸体与半径 \(r_c\) 圆盘的 Minkowski 和。
每个边界点均有半径 \(r_c\) 的内滚圆；外滚圆由凸性成立。
故这条平面闭曲线的 reach 至少 \(r_c\)。与闭区间的正交直积最近点投影逐因子分解，
所以任意有限中央柱段作为闭子集也有 reach≥.216。

这个 reach 结论限于中央柱段。与其他活动片或固定帽相接后的全局法球仍须另验。
R113 的固定帽和 cut/cuff 参数完全保留：cuff=.32、cut=.4，
\(w=.1,w_r=-7/4\)。下列继承关系可准确使用：

- 同一 a0 保持原全部 frozen 径向候选的内蕴度量入口；不需要重缩放或改变尾模型。
- 新真实中央点 \((\pm A_q,0,0)\) 的连线包含原 \((\pm1.4,0,0)\)，
  所以原六个固定帽点加中央两点的凸包包含关系、标记近点误差及标记内接球下界不减。
- 中央柱段满足原 held 保护式 \(y\le .5+(5/9)z^2\)，也满足中央窄板 \(|y|\le.499\)。

但是**整个活动核**的 \(|y|\le.75\)、held 保护曲线、球半径 2.25、高度窗口
\(z_c=1.2886410585615193\)、准确共同 cut/cuff 两 jet、真实主曲率和所有全局法球
均仍需实际解验证。只有这些全核条件通过，才可把 R113 的强 held、欧氏商及 reach
嫁接结论应用到新的完整曲面。R116 §6 的额外中央曲率参数若围绕此 seed 使用，
也须用 (24) 重新支付其变分窗口常数，不能抄用旧椭圆的 \(n_{\min},n_{\max}\)。

## 6. 稳定可调用实现与实际运行记录

实现 `scripts/fd2d_balanced_oval_core.py` 的当前 SHA256 为

`1df75241ec76ae9a28042b72cbb721de61e7283378d82e7dea5ff05c3f84b692`。

`BalancedOvalCore(coefficients=(0,...,0))` 使用 (4) 的积分定义。
常规浮点评估用 Gauss 积分计算这些准确对象；定义与证明不依赖其近似误差恰为零。
参考曲线的弧长逆采用带中央括区保护的 Newton 迭代，防止陡峭曲率半径过渡处
两个端点间交替而无收缩。它提供：

- `evaluate(sigma)`、`evaluate_reference_angle(theta)`：位置、两阶角导数、中央 s 两 jet、ρ 与 ρ′；
- R115 相同签名的 `parameter_derivatives`、`parameter_hessian` 及参考角参数导数；
- `gauss_codazzi_initial(coordinate, reference_angle=False/True)`：
  `X, X_u, X_uu, e1, e2, N, n, m, l, a0`；
  `X_u/X_uu` **始终**表示材料 σ 的一、二阶导数，即使取样点由 θ 输入。
  当 `reference_angle=True` 时，额外返回 `X_theta/X_thetatheta` 表示 θ 两 jet，
  `material_sigma` 给相应材料角；`X_coordinate/X_coordinatecoordinate` 给当前输入坐标的两 jet；
- `inlet`、`inlet_jacobian`：与 R115 相同的实际材料角 Fourier 投影接口，
  仍须读取其实际投影误差，不能把精确曲线度量等同于截断坐标曲线的度量。

实际有限检查文件 `notes/2026-11-12-fd2d-balanced-oval-core-check.json` 在 1024 个点给出：
弧长逆残差 \(1.69\times10^{-14}\)，材料角速度误差 \(2.23\times10^{-16}\)，
参考角速度误差 \(4.45\times10^{-16}\)。所采样的曲率半径范围为
\([.22921359148,3.11639547387]\)，对应曲率约 \([.32088353625,4.36274303607]\)。
这些更紧数值仅作实现诊断，统一结论采用 (11)、(24) 的已证界。

区间证书脚本 SHA256 为
`2187415dba61ab47cffd07c8e835d897e137e12f44b58e9528892af61a123a66`；
其报告同时记录上述 core 源哈希，两份输出与当前源一一对应。

旧接口源已按原字节内容闭存于 `scripts/fd2d_balanced_oval_core_aa56_snapshot.py`，
SHA256 `aa56c7d69b0d7a855ab8617f68657f25912a6a094704f3c619d22c3834a49c7b`。
它用于复现先前绑定该哈希的入口谱报告。新版只澄清材料 jet/参考角 jet 的字段、
修正投影诊断的 core 名称并增加接口检查，没有改变曲线、准确积分矩或角映射。
新版两套坐标的各一、二阶接口检查均为零误差。

## 7. 对强目标推进的具体作用

原准确椭圆曲率最大值为 5.6、最小值约 .2551；新的参考曲线在已证区间内
最大曲率低于 4.386，最小曲率高于 .3154。两端的余量同时改善，
而 a0、强中央轴支持窗口、固定帽及真实尾 DN 接口保持同一组定义。
这给正曲率段的 Gauss 方程 \(l=(m^2+K)/n\) 更多中央 n 余量，并降低中央最大曲率。
它不证明该余量会沿完整活动核保留；后续仍以真实 XYZ 的 E、F、G、主曲率、全局距离
和非线性尾残差判断。下一个实际任务是把这个稳定中央输入用于完整共同 g 的 BVP，
并继续选择能在原高度窗口内回到既定 cut 的活动母线。
