# R119 续篇：实际度量参数盒上的统一全标签尾图与普通源

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 前篇的每层两个实际下降段参数可同时加入源
R72/R115 的完整无限尾构造。全部内部标签、真实九段矩阵、所有
高频、holonomy mean 和连续普通源均保留，原已付局部常数不必
放大。所得图对整个参数序列和所有标签联合全纯；在实参数乘积
盒上，它还有到真实 $C^2$ 尾的连续依赖。

这给出的仍是内部标签图及其已付角宽的有限 connector 延拓。
它没有把共同 cut 的高 Dirichlet 值变成自由标签，也没有证明
固定任意 $\Gamma$ 时旧 R74 的 regular 逆仍成立。

## 1. 同一实际参数、同一状态及同一标签层

沿用
[实际负段度量参数](R119-supplement-actual-negative-band-metric-parameters.md)
的 $\psi_{j,k}$ 和 $w_\Gamma$。为支付参数微分，先作明确复化：
$$
 \mathbb D_\Gamma=\{\Gamma\in\ell^\infty(\{j>128\}\times\{1,2\};\mathbb C):
                  \|\Gamma\|_\infty<r_C\},\qquad r_C=2^{-15}.
 \tag{U.1}
$$
几何实盒仍为 $|\gamma_{j,k}|\le r_R=2^{-16}$。复化只用于真实
解析方程及 Cauchy 估计；复 $w_\Gamma$ 不称为实度量。

源 R72 的 $\delta_j,\eta_j,h_j,\tau_j,\zeta_j,E_m,b_m$ 全部
不变。仍使用
$$
 X_{m,j}=(-1)^j\zeta_j^{-1}e^{|m|\tau_j}V_{m,j},\quad
 \zeta_j=\epsilon\delta_j^{39/4},\quad
 V_m=(\nu_m C_m/r^4,\xi_m),
$$
$$
 \nu_m=\frac{m^2(m^2-1)}{12},\qquad
 \xi_m=(C'_m/r^3-m^2C_m/r^4)/\sqrt{12},
 \quad m\in4\mathbb Z\setminus\{0\}.
 \tag{U.2}
$$
强状态范数是 $\|X\|_{\mathcal X}=\sum_m\sup_j\|X_{m,j}\|_\infty$，
强端口源范数是相同次序的 $\mathcal F$。标签准确保持
$a_m=(E_m^{-1}X_{m,b_m})_1$。因为端点 profile 和理想平台均未变，
同一个理想 $E_m$ 及同一低/高分割仍可使用；真正的传递矩阵则随
$\Gamma$ 更新，不把它们冻结为原矩阵。

任意 $\beta\ge0$ 的标签 norm 定义为
$$
 \|a\|_\beta=\sum_m e^{\beta|m|}|a_m|.
$$
将全部绝对宽 $\tau_j$ 同时移到 $\tau_j+\beta$，记对应状态为
$X^{[\beta]}$。下面的图在 $\|a\|_\beta<1/4$ 成立。

## 2. 复参数盒上的实际 profile 门

在修改的下降段，
$$
 p_\Gamma=p_0e^{\gamma\psi},\qquad
 \partial_x\log p_\Gamma=-\Delta S'+\gamma\psi_x.
$$
$|p_\Gamma|=p_0e^{\operatorname{Re}\gamma\psi}$ 严格单调下降，
因为支集上 $S'>1$、$96r_C<1/32<\Delta$；支集外是原 profile。
它的端点模长仍为准确的正实端值。因此源 R72 §3 的逐段面积表
对 $|p_\Gamma|,|p_\Gamma|^{-1}$ **逐项保持原值**。特别
$$
 \delta/2\le|p_\Gamma|\le64/\delta,\qquad
 |w_\Gamma|\le64\epsilon\delta^5<1,\qquad
 \min|w_\Gamma|\ge\epsilon\delta^7/256.
 \tag{U.3}
$$
在 bump 支集，
$$
 |\partial_x\log p_\Gamma|
 \le\Delta\frac{3375}{2048}+96r_C
 <\frac{15}{8}\Delta,
$$
$$
 |\partial_x^2\log p_\Gamma|
 \le\Delta\frac{45}{8}+6144r_C<6\Delta.
 \tag{U.4}
$$
支集外仍是原来的 $15/8$ 和6上界。各段的
$m_*=1+\sup|\partial_y\log p_\Gamma|$ 因而不增。

复 log 导数的绝对积分不与实变差混同。准确保留新增项后有
$$
 \int_{\rm cell}|(\log p_\Gamma)_y|dy
 \le6|\log\delta|+c_R+4r_C
 <6|\log\delta|+2\log128,
 \quad c_R=\log64+2\log(65/64).
 \tag{U.5}
$$
每个 bump 的绝对变差为2，共有两个；这是 $4r_C$ 的来源。
最后严格余量可用 $c_R<5$、$2\log128>28/3$ 核对。

材料积分也需在复盒上重核。设 $\alpha_0=65/64$、
$\lambda_\Gamma=(\log p_\Gamma)_y-7/\sqrt{12}$。由
$\ell<4\delta$、$|\log p_\Gamma-\log p_0|\le r_C$ 和
两 bump 的总变差，
$$
 \begin{split}
 &\int(1+|\lambda_\Gamma|)(1+|p_\Gamma|^{-2})dy\\
 &\le16\delta(1+\alpha_0^2\delta^{-2})
       +6|\log\delta|+c_R\\
 &\quad+e^{2r_C}(\alpha_0^2\delta^{-2}+1/2+1/8192)
       +4r_C(1+\alpha_0^2\delta^{-2})
 <64\delta^{-2}.
 \end{split}                                                     \tag{U.6}
$$
最后一步甚至在 $\delta\le1/256$ 已有很大余量：乘 $\delta^2$，
用 $\alpha_0^2<2$、$e^{2r_C}<2$、$\delta|\log\delta|\le1$，
右侧小于10。实际所有层满足 $\delta<2^{-56}$。
因此 R72 (4.4) 的 $2^{24},2^{26}$ 完整材料常数仍可使用。

## 3. 完整低窗流：复 profile 不需要正面积符号

源 R38 的单调 Dyson/Gauss 论证在此只需以下明确扩展。设 $p$
非零而 $|p|$ 单调，$f=p e^{\pm2ky}$。在相应的偶阶 Dyson
integrand 中，每个按时间排序的 $p$ 比值的模不超过1。故原小
对角元 $d$ 满足 $|d-1|\le\varepsilon$，其中
$$
 \varepsilon=e^{2kh}(\cosh(\sqrt\nu h)-1)<1.
$$
两个奇阶和满足
$$
 |F_{12}|\le\nu(1+\varepsilon)\int|f|^{-1},\qquad
 |F_{21}|\le(1+\varepsilon)\int|f|.
$$
$\det F=1$ 仍给准确 Gauss 分解，面积这时允许为复数；它们的
模至多是上述绝对面积乘 $(1+\varepsilon)/(1-\varepsilon)$。
原所有对角共轭的模费保持不变。此处不声称复面积为正，也没有
除以可能相消的复面积积分。

R72 §3 的完整乘积只用这些面积**上界**及固定乘积次序，其
$P_-<128,P_+<3,C_*<4\nu,D<2$ 的账均不使用复面积的符号。
截短一个单调段后模长仍单调。因此原任意内部子区间结论保持：
$$
 \|\Psi_\Gamma(s,t)\|_\infty<3072\nu_m<256m^4
 \quad\text{若 } |m|\le2^{-5}\delta^{-3/8}.
 \tag{U.7}
$$
反向再付原来的固定因子2。这个扩展支付了真正有限 Galerkin
构造所需的内部流，而不只是整个胞元端口。

## 4. 全频强修正及真实高频矩阵没有遗漏

源 R72 §§4–6 的 mean 归一化、压缩 Galerkin 逆和完整 forced
Volterra 证明使用 $|w|,|w|^{-1},|E|\le2$、(U.6)、(U.7) 和
各段 $m_*$。这些条件现已逐项支付。平方根和逆始终在同一个
复 Wiener 球的幂级数分支；实参数时再恢复真实正分支。
完整 mean 恒等式保留 $E_y=2w_\Gamma(w_\Gamma)_y$，所以改变
profile 没有破坏 $M\equiv1$。

由 (U.4)，完整强修正的径向放大与角费仍是原数值：
$$
 2^{38}e^{480c_R}\delta^{-2890},\qquad
 256\beta(\delta),
$$
$$
 \beta(\delta)=3\delta+6\eta+
 \sqrt{\frac{15}{2}\eta(2\log128+6|\log\delta|)}.
 \tag{U.8}
$$
这里强放大使用各段 $\sup|b|$，由 (U.4) 保持原界；没有把
(U.5) 的额外变差藏进 $c_R$。
所以实际局部 map $\Phi_{j,\Gamma}$ 保持
$$
 R_j=2^{-64}\epsilon\delta_j^8h_j^5J_j^{-5},\qquad
 \|\Phi_{j,\Gamma}(U)\|\le2^{24}h_j^{-5}\|U\|,
$$
$$
 G_j=2^{98}(\epsilon\delta_j^8)^{-1}h_j^{-14}
 \tag{U.9}
$$
的存在球及二次余项常数，包含完整 mean 和全频残差修正。
原 $16e\zeta_j/R_j<1$ 的逐层入球门不变。

全频线性分析另外进行，不能从 (U.7) 推出。三个真实平台完全
不变；六个小段的 $L^1$ generator 上界由 (U.3) 保持。因此
$$
 \|B_{m,j,\Gamma}-B_{m,\infty}\|_\infty
 \le32768m^8\sqrt{\delta_j}
 \quad\text{若 } |m|\le M_j^\sharp=2^{-5/4}\delta_j^{-1/8}.
 \tag{U.10}
$$
在窗口外，原 coarse scalar 方程是
$Q''+bQ'+(d_m-k_mb)Q=0$。取
$Y=(|m|\sqrt{1+\sup|b|}\,Q,Q')$ 后，矩阵 norm 的界
$|b|+|m|\sqrt{1+\sup|b|}$ 对复 $b$ 也成立。(U.4) 保持全部
八次规范转换，(U.5) 支付完整 $\int|b|$。因而保留真正的
$$
 \|A_{m,j,\Gamma}\|_\infty
 \le C_H(1+|m|)^{312}e^{|m|(\beta_j-h_j)}<\frac14
 \quad (|m|>M_j^\sharp),
 \tag{U.11}
$$
其中 $C_H=2^{2-39/4}C_L^{(6)}$ 为源 R72 (7.5) 的同一明确
常数。原浅端高频上包络小于 $e^{-79.17}$；深段包络更小。
没有把复参数下的高频矩阵替换为理想谱。

## 5. 真全标签图及所有参数的联合全纯性

低区的参考特征基和标签层仍固定，高区参考块则使用 (U.11) 的
真实 $A_{m,j,\Gamma}$。同一强 Green 构造给
$$
 \|\mathcal G_{0,\Gamma}\|\le4096,\quad
 \|\mathcal H_{0,\Gamma}\|\le3,\quad
 q_G<.003124760<1/256.
$$
低区 (U.10) 的 Neumann 修正后，
$$
 \|\mathcal G_\Gamma\|\le8192,\qquad
 \|\mathcal H_\Gamma\|\le256/85.
 \tag{U.12}
$$
这些是真正的 $\sum_m\sup_j$ 算子界。全部理想中性层数、强
Taylor 卷积及两处分段单调包络均未改变。

完整余项 $\mathcal R_\Gamma$ 仍满足
$$
 \|\mathcal R_\Gamma(X)-\mathcal R_\Gamma(Y)\|_{\mathcal F}
 \le K_*(\|X\|+\|Y\|)\|X-Y\|,
 \quad \kappa_*:=8192K_*<2^{-60},
$$
$$
 K_*=2^{108}\sup_{j>128}\delta_j^{7/4}h_j^{-14}.
 \tag{U.13}
$$
因此
$$
 X_\Gamma(a)=\mathcal H_\Gamma a+
             \mathcal G_\Gamma\mathcal R_\Gamma(X_\Gamma(a))
 \tag{U.14}
$$
在 $\|a\|<1/4$、单位强状态球中自映并以小于 $2^{-59}$ 收缩。
同一个逐次迭代同时给出所有实、复参数的解。

每个局部有限流和全频 Volterra 固定点对两个本地参数及输入联合
全纯。高区 Green 的几何和在算子 norm 中局部一致收敛；低区的
Neumann 和也如此。频率求和使用已证明的强界，故对任意
$\ell^\infty$ 参数方向均可逐项作复线微分，并局部一致有界。
由 Banach 空间的 Cauchy 公式，或直接对上述一致收敛的幂级数
取系数，这给真正的 Fréchet 全纯性，而不只是逐坐标形式微分。
(U.14) 的统一收缩于是给 $\Gamma,a$ 的联合全纯图。

所有绝对宽同时平移后，准确有
$$
 \boxed{\quad
 X_{\Gamma,\beta}:=\|X_\Gamma^{[\beta]}(a)\|_{\mathcal X}
 <\frac{13}{4}\|a\|_\beta<1,\qquad
 \|X_\Gamma(a)\|_{\mathcal X}\le e^{-4\beta}X_{\Gamma,\beta}.
 \quad}                                                         \tag{U.15}
$$
这里的后式只先用于非零模强状态；完整 mean 仍由自己的二次小根
恢复。在实盒上，复参数余量至少 $2^{-16}$，所以
$$
 \boxed{\quad
 \|D_\Gamma X_\Gamma^{[\beta]}(a)\|_{\ell^\infty\to\mathcal X}
 <2^{18}\|a\|_\beta .
 \quad}                                                         \tag{U.16}
$$
原标签一阶界 $\|D_aX\|<13/4$ 和 $\|a\|\le1/12$ 上的
$\|D_a^2X\|<2^{-54}$ 也保持原常数；它们是内部标签空间的界，
不是共同 cut 的高输入逆。

## 6. 真实物理尾、两迹、mean 和有限 connector 的统一性

前述证明保持原局部 $C^2$ jet 界
$$
 \|\mathcal J_{j,\Gamma}(U)\|_{C^2,\mathcal A_{\tau_{j-1}}}
 \le2^{52}\delta_j^{-4}h_j^{-5}\|U\|.
 \tag{U.17}
$$
所以 R115 的实际高度、完整水平原函数和 $C^2$ 平坦延拓均可
逐项重建，只须把所有背景 $w,E$ 换成 $w_\Gamma,E_\Gamma$。
真实通量的 Euler 恒等式、反射和四重旋转对称完全保留。
一个整体高度常数可以固定；平盘与 cut128 的两个 mean 高度
不能独立指定。参数变化还包含前篇 (M.22) 的参考 mean 高度。

特别，完整四态 $P,K,U,V$ 在共同宽4及更宽的原允许条带满足
$$
 n_{j,\Gamma}\le2^{64}\delta_j^{443/256}
          e^{-4\beta}X_{\Gamma,\beta}.
 \tag{U.18}
$$
其证明是原真角图 (A.13) 的同一物理换算；分母 $|w_\Gamma|$
的下界、局部流和 $m_*$ 均已保持。mean 通过 R25 的完整小根
二次界计入，不另假设一个 mean 线性去权。
这也是联合全纯的逐胞物理 map。在实参数盒上，对固定
$\|a\|_\beta$，其参数方向的 Cauchy 费用至多另乘 $2^{16}$；
若要一个严格统一的宽松数，可取 $2^{17}$。

取 $\beta=224$。cut128 的背景 jet 和物理缩放完全未变，
(U.15) 使原 balanced connector 的初始球不增。所有有限段及
双 bump 的背景在本参数族中固定，故同一个已付流给
$$
 \sup N_b<2^{-447}X_{\Gamma,224},\qquad
 \sigma_{\rm raw}=777/400,\quad
 \sigma_{\rm grounded}=377/400.
 \tag{U.19}
$$
完整 $(f_B,k_B,\lambda_B)$、normal/shear 和 holonomy 仍按原
公式输出，并随 $\Gamma,a$ 联合全纯。这里仅使用实际 forward
延拓，不使用原 R74 regular 直线，也不声称新的第四标签方向
已与它匹配。

## 7. 普通连续源的同一个完整合同

对每个固定实 $\Gamma$，在其真实非径向尾上使用 R115 (115.25)
的完整密度 $\mathcal E_\Gamma$。同一强源空间可统一写为
$$
 \|e\|_{\mathcal T_\beta}
 =2^{4200}\epsilon^{-1}\sum_{m\in4\mathbb Z}\sup_{j>128}
 \left[
 \delta_j^{-11607/4}h_j^{-2}
 e^{(\tau_{j-1}+\beta+h_j/2)|m|}
 \sup_{y\in I_j}|\widehat e_{m,j}(y)|\right].
 \tag{U.20}
$$
源须在真实接缝给出同一连续物理 RHS。输入全部标签变化 $b$ 后，
真实 Jacobi 解存在并满足
$$
 \|\dot X\|_{\mathcal X_\beta}
 \le4\|b\|_\beta+2^{14}\|e\|_{\mathcal T_\beta}.
 \tag{U.21}
$$
理由是 R115 §6 中的 $2^{38}e^{2012}\delta^{-2890}$ 连续
response、$2^{4096}\delta^{-2890}h^{-2}$ 端口费和全部 mean
费只使用 §§2–4 已保留的门。强提升仍先逐频取胞元上界，然后
求卷积。原直接源留下的径向幂2、mean 初值留下的径向幂1及超过
$2^{80}$ 的常数余量不变。

零模准确为
$$
 \dot M(y)=\int_{y_f}^{y}w_\Gamma(s)\langle e(s)\rangle ds,
 \tag{U.22}
$$
不是设为0。完整 mean 斜率、两端高度及外端的 holonomy 负荷都
由同一方程给出。全向量源重建仍须检查 R115 (115.35)–(115.36)
的真实 $e_T\in\mathcal T_\beta$ 及 metric-source norm；不能
把任意普通源无条件放进此空间。

尤其，(M.22) 的度量参数列属于改变目标的方向，不因为已证明
(U.16) 就自动属于 (U.20)。它们的实际响应由联合图的参数微分
给出，含参考 profile 和 mean 的变化。若把它们改写为固定目标
方程的 ordinary source，仍须使用准确 metric-source 公式和
所选源空间，不能偷换为 $e=0$。

## 8. 无限参数乘积盒上的连续性

除 $\ell^\infty$ norm 全纯性外，还可给更适合无限参数选取的
连续性。设实盒内 $\Gamma^{(n)}$ 逐坐标趋于 $\Gamma$，标签在
$\ell^1_\beta$ 中收敛。则
$$
 X_{\Gamma^{(n)}}^{[\beta]}(a^{(n)})
       \longrightarrow X_\Gamma^{[\beta]}(a)
 \quad\text{于 }\mathcal X,
 \tag{U.23}
$$
相应完整物理尾也在 $C^2$ 中收敛。

证明不能只引用逐点 ODE 依赖，也不能把 (U.10) 的 raw 窗
误差直接作 $\sup_m$。准确低窗是 $|m|\le M_j^\sharp$；先
保留真实规范
$A_{m,j,\Gamma}=-2^{-39/4}e^{-|m|h_j}B_{m,j,\Gamma}$，
再对所有 $m$ 使用 $\sup_{x\ge0}x^8e^{-h_jx}=(8/(eh_j))^8$，
得到源 R72 (8.4) 的统一界
$$
 \|A_{m,j,\Gamma}-A^0_{m,j}\|\le\epsilon_j,
 \qquad
 \epsilon_j=32768\,2^{-39/4}\sqrt{\delta_j}
                 \left(\frac8{eh_j}\right)^8.
 \tag{U.24}
$$
深段 $h_j=8\delta_j^{1/256}$ 时，准确地
$\epsilon_j=32768\,2^{-39/4}e^{-8}\delta_j^{15/32}\to0$。
不需要另缩小到内部标签层 $b_m$ 的窗口；那些层始终由同一个
理想大分量首次越过1定义。对其余 $|m|>M_j^\sharp$，使用
(U.11) 的真正高频包络；它在 $j\to\infty$ 时也一致趋0。
因此任意
两个参数的**系数差**在这些层的 $\mathcal X\to\mathcal F$
norm 一致趋0。浅层只有有限多个参数，其全频算子依赖由复盒的
一致界连续。Green resolvent 恒等式和固定标签因此给
$\mathcal G_\Gamma,\mathcal H_\Gamma$ 的乘积拓扑连续性。

非线性余项的深层 operator 上包络是
$2^{108}\delta_j^{7/4}h_j^{-14}\to0$。浅层的完整局部 map
在单位强球上一致全纯，故 $\mathcal R_\Gamma$ 在该球上一致
连续。将这两项代入同一个严格收缩 (U.14) 得 (U.23)。最后用
(U.17) 的正衰减指数、参考 profile 前篇 (M.17) 及有限头的真实
依赖，得到完整 $C^2$ 结论；mean 高度由同一一次积分控制。

这项连续性支付任意无限参数选取和其有限近似极限。它没有改变
目标：每个选定 $\Gamma$ 对应一个明确的 $g_\Gamma$，最终相位
族仍须统一使用某一个最后选定的 $g_{\Gamma_\infty}$。

## 9. 来源和准确复核

使用的外课题完整文件及本次读取 blob 为：

| 来源 | 实际使用内容 | Git blob |
|---|---|---|
| quantitative-newton R72 | 完整局部 map、强 Green、全频固定点 | `a7c78793ba18724a4f0553b6ccd55259b8f4df92` |
| quantitative-newton R38 | 时间有序 Dyson/Gauss 上界 | `24cdd49839c024c84d8e5702a1567fbb8eba0e63` |
| quantitative-newton R21 | 真实 $C_L^{(6)}$ 和原 profile | `a3b55246f416d73a4c4fe2b0b1545f0bfee0863d` |
| large-amplitude coarse cell note | §3.3 的完整高频 scalar 能量 | `e02e594c8db2cb29ea71a86802104c87e5059906` |

本题 R115 和 balanced224 的原式在上文逐项标明。
`scripts/fourfold_uniform_metric_parameter_tail_chart_20261113.py` 核对
新复参数门、材料积分余量、原收缩余量和连续极限的正指数，输出
`notes/2026-11-13-R119-uniform-metric-parameter-tail-chart-budget.json`。
全频量词、参数全纯性和连续普通源结论由正文证明承担。
