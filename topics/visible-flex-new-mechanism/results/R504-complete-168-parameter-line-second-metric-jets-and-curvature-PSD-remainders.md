# R504 — 完整 168 场的真实参数线、二阶度量与原曲率 PSD 余项

## 0. 本稿实际证明了什么

在同一个真实第 $56$ 点、同一完整 $168$ 维参数化中，本稿给出任意固定方向 $\delta$ 的**完整非线性参数线恒等式**。它保持原 $g$、$b_0$、真实角相位、原全角周期原函数以及旧五个 null-height 与新增 $\gamma$ 高度列；没有把参数线替换成位置向量的仿射线。

结论分三层：

1. 只用已付的当前 $U=X_s,T$、当前 scalar fields、一个方向的 scalar fields 和固定 $a,a_s$，便有真实线上的完整 $U_\alpha,T_\alpha$，不需要位置 $X$、center 的前缀积分或全参数 Jacobian。
2. 由此得到 $e=|U|^2-1$、$f=U\cdot T$ 的完整方向二阶式和有明确常数的 Taylor 余项。原先的 $\phi(e_0+\alpha e_1,f_0+\alpha f_1)$ 保留 spectral 非线性，但**没有包含几何的二阶项**，因而不能作实际度量上界。
3. 对原四条曲率 PSD 行给出真实方向导数、二阶余项界及其必要输入。这里明确保留正常面积下界、原行尺度和直接曲率验收；不会从 U/T 缓存补造缺失的基点第二基本形式。

全文只作原式推导，没有运行数值、符号程序、方向查询、旧检查或新开发。它没有证明第 $56$ 点存在可行下降，也不宣布新的标量搜索已经完成。下面的上界只有在其常数得到真实有向估计后才成为数值证书；普通 binary64 代入不自动成为严格区间界。

## 1. 原来源与真实方向

本稿使用以下冻结源的实际公式，不使用旧有限主问题的求解状态作为数学前提：

- [完整 168 场](../scripts/frame_complete_body_extension168.py) 的 scalar_frame、height_jets、geometry；
- [原 frame 和周期算子](../scripts/frame_collar_bvp.py) 的 target_frame、periodic_operator；
- [当前 168 一阶方向](../scripts/frame_complete_body_extension168_joint_selected.py) 的 current_168_metric_direction 与 bind_current_168_first_jets；
- [固定高度与原参考](../scripts/frame_five_height_field.py)、[原 null-height 坐标](../scripts/frame_height_null_coordinates.py) 以及 [直接参考组装](../scripts/frame_direct_reference_geometry159.py)；
- [原 metric 两分支](../scripts/frame_metric_affine_spectral_model.py) 的 phi、phi_gradient，与 [原实际 metric 值](../scripts/frame_metric_epigraph.py) 的 geometry_values；
- [原实际曲率](../scripts/frame_curvature_psd.py) 的 curvature_values 和 [原 11 行接口](../scripts/frame_metric_budget_restoration_rows.py) 的 row_values；
- [R497](R497-complete-angular-primitive-and-axis-metric-curvature-response.md) 的完整角原函数范围，以及 [R501](R501-exact-full-column-rank-and-nonfixed-curvature-peak-in-the-current-168-family.md) 的精确物理映射。

上述实际代码按 source commit
$\mathtt{a9da16278c336ec5d6ce3be88502263d04429324}$
只读。原 frame、curvature、metric 源 blob 分别为
$\mathtt{586074c9bfba5b64246c015ae9a8303f5076df54}$、
$\mathtt{6540008651dad78b7885898c69b98e6cf7aa6835}$、
$\mathtt{9f34694cfbcbadd86a93944e5e8e342b7b315f63}$。

令真实独立坐标为

$$
q_\alpha=q_0+\alpha\delta,\qquad q_0=q_{56}\in\mathbb R^{168}.
\tag{1}
$$

这里首先是实数意义的参数线。实际程序生成的舍入坐标与此线的区别留在第 9 节，不把浮点加法解释成精确实数加法。

当前 scalar fields 和它们的方向满足

$$
u_\alpha=u+\alpha\xi,\qquad
v_\alpha=v+\alpha\nu,
\tag{2}
$$

包括全部旧 $154$ 个 tangent 坐标及新增八个 body tangent 坐标。原 normalized-Q 列仍属于 $v$；它的真实角函数没有替换成一个有限正弦近似。所有径向、角向导数都沿原固定基函数取。例如
$u_{\alpha,s}=u_s+\alpha\xi_s$、
$v_{\alpha,ss}=v_{ss}+\alpha\nu_{ss}$。

把旧五个 null-height 坐标的方向记为 $\delta\lambda_j$，其原密度和原锚原函数记为 $C_j(s),Z_j(s)$，$Z_j'=C_j$。新增高度坐标的方向为 $\delta\gamma$。令

$$
L=\frac{81}{100},\qquad
x=\frac{s-9/250}{L},\qquad
P_8(x)=x^8e^{-x/(1-x)}
\quad(0<x<1),
\tag{3}
$$

并在区间外沿原定义延为零。完整高度方向是

$$
Z_\delta(s)=\sum_{j=1}^5\delta\lambda_j Z_j(s)
             +L\,\delta\gamma P_8(x),
\qquad
b_\delta(s)=Z_\delta'(s)
 =\sum_{j=1}^5\delta\lambda_j C_j(s)
             +\delta\gamma P_8'(x).
\tag{4}
$$

特别地

$$
b_{\delta,s}
 =\sum_j\delta\lambda_j C_j'(s)
   +\frac{\delta\gamma}{L}P_8''(x).
\tag{5}
$$

原 $a(s)$、$b_0$ 和各高度原函数的锚不随 $\alpha$ 改动。旧 null-height 的零总积分及原端点 jet 关系由原基保持；新增 $Z_\delta$ 的 $P_8$ 项在两个真实接口为零，并保其已声明的端点正则性。这不是添加一个可自由调节的 center 常数。新增 $u$ 用 $P_5$、新增 $v$ 用 $P_8$；其左端和右端零延拓也始终使用原定义。

## 2. 沿真实线的完整 $T$ 与 $U$

记

$$
\psi_\alpha=\theta+u_\alpha,\quad
N_\alpha=(\cos\psi_\alpha,\sin\psi_\alpha,0),\quad
H_\alpha=(-\sin\psi_\alpha,\cos\psi_\alpha,0),\quad
c_\alpha=(1+v_\alpha^2)^{-1/2}.
\tag{6}
$$

原 target_frame 给出的实际切向量准确为

$$
T_\alpha=c_\alpha H_\alpha+v_\alpha c_\alpha e_3,
\qquad |T_\alpha|=1.
\tag{7}
$$

原辅助 $\beta$ 不进入式 (7)。它不能代替独立高度方向，也不能用来删去 $v_\alpha c_\alpha$。

令 $\Pi$ 为同一完整角圈上的原零均值周期原函数。固定参考下，

$$
U_\alpha=a_s\Pi T_\alpha+a\Pi T_{\alpha,s}
                 +b_\alpha e_3,
\qquad b_\alpha=b_0^{\rm current}+\alpha b_\delta.
\tag{8}
$$

其中 $b_0^{\rm current}$ 是第 $56$ 点的完整实际高度速度，已经包含其旧 null-height 和非零新增 $\gamma$，不是只取 immutable $b_0$。

因此有可直接消费已付 first jets 的恒等式：

$$
\boxed{
U_\alpha=U_0
 +a_s\Pi(T_\alpha-T_0)
 +a\Pi(T_{\alpha,s}-T_{0,s})
 +\alpha b_\delta e_3 .
}
\tag{9}
$$

式 (9) 没有任何 center 查询，也不需要 $X$ 的高度前缀积分。$T_{\alpha,s}$ 直接由真实 scalar fields 得到：

$$
T_{\alpha,s}
 =u_{\alpha,s}T_u(u_\alpha,v_\alpha)
  +v_{\alpha,s}T_v(u_\alpha,v_\alpha).
\tag{10}
$$

需要时，全部位置 jet 的相对式同样完整：

$$
\begin{aligned}
X_\alpha-X_0
 &=a\Pi(T_\alpha-T_0)+\alpha Z_\delta e_3,\\
X_{\alpha,ss}-X_{0,ss}
 &=a_{ss}\Pi\Delta T+2a_s\Pi\Delta T_s
      +a\Pi\Delta T_{ss}+\alpha b_{\delta,s}e_3,\\
X_{\alpha,s\theta}-X_{0,s\theta}
 &=a_s\Delta T+a\Delta T_s,\\
X_{\alpha,\theta\theta}-X_{0,\theta\theta}
 &=a\Delta T_\theta.
\end{aligned}
\tag{11}
$$

这里 $\Delta T=T_\alpha-T_0$，其余同义。式 (11) 给的是完整**增量**，不把未存的 $X_0,X_{0,ss}$ 宣成已经恢复。

### 2.1 全角与浮点的准确范围

$\Pi$ 不能逐角点替换成一个局部系数。即使 $\xi,\nu$ 在某个反射轴取零，式 (9) 的角原函数仍含整个角圈。

连续模型中 $\Pi$ 与 $\partial_s,\partial_\alpha$ 交换。原有限完整角网的 periodic_operator 则是一个固定的实线性矩阵 $\Pi_N$；在实数运算意义下，上述交换及式 (9) 对该同一 $\Pi_N$ 也成立。粗、细网分别保持自己的原角点和算子，不把细网重新生成成不同舍入的角列。

但是，原 geometry 是先组装参考项，再依次添加旧 null-height、新 $\gamma$；式 (9) 是从已付 $U_0$ 添加差。两者代数等价，浮点加法次序不同。因此一个按式 (9) 实现的新 predictor 必须有自己的求值身份，不能声称已经逐位复现原 ordinary 数组。原 actual 14 门仍用原 ordinary 路径。

## 3. 完整方向二阶，而非局部 frame 的一部分

以下下标 $[k]$ 指 $\partial_\alpha^k$，在未另说明时取 $\alpha=0$。令 $c=(1+v^2)^{-1/2}$。由原 frame，

$$
T_{[1]}=-c\xi N+c^3\nu(e_3-vH),
\tag{12}
$$

$$
\boxed{
T_{[2]}
 =-c\xi^2 H+2vc^3\xi\nu N
   +(2v^2-1)c^5\nu^2H-3vc^5\nu^2e_3 .
}
\tag{13}
$$

该式包括相位、归一化和交叉项。尤其不能只保 $T_{uu}\xi^2$，也不能把 $v$ 方向当成 $e_3$ 的线性添加。

径向导数必须作用到背景及方向两者。例如

$$
\begin{aligned}
\partial_sT_{[1]}
={}&\xi_sT_u+\nu_sT_v\\
 &+\xi(u_sT_{uu}+v_sT_{uv})
  +\nu(u_sT_{uv}+v_sT_{vv}).
\end{aligned}
\tag{14}
$$

式 (13) 的 $\partial_s$ 同样保留
$\xi_s,\nu_s,u_s,v_s$，其 $\partial_s^2$ 保留原二阶 scalar jets。

沿式 (8)，

$$
U_{[1]}=a_s\Pi T_{[1]}+a\Pi\partial_sT_{[1]}+b_\delta e_3,
\tag{15}
$$

$$
\boxed{U_{[2]}=a_s\Pi T_{[2]}+a\Pi\partial_sT_{[2]}.}
\tag{16}
$$

高度的二阶方向导数为零，但它在 $U_{[1]}$ 中的贡献仍进入后面的平方和交叉项，不能因此在二阶 metric 中删除高度。

原实际两量为

$$
e_\alpha=|U_\alpha|^2-1,\qquad f_\alpha=U_\alpha\cdot T_\alpha.
\tag{17}
$$

它们的完整一阶和二阶是

$$
e_{[1]}=2U_0\cdot U_{[1]},\qquad
f_{[1]}=U_{[1]}\cdot T_0+U_0\cdot T_{[1]},
\tag{18}
$$

$$
\boxed{
\begin{aligned}
e_{[2]}&=2|U_{[1]}|^2+2U_0\cdot U_{[2]},\\
f_{[2]}&=U_{[2]}\cdot T_0
       +2U_{[1]}\cdot T_{[1]}+U_0\cdot T_{[2]}.
\end{aligned}}
\tag{19}
$$

这些只需要方向数组，最大参数轴可以保持为一个方向；没有完整网格 $\times168$ 张量的必要性。式 (13)、(16)、(19) 已由另一代理作窄纸面独核；该独核不扩展为余项或实际门的数值通过。

### 3.1 一个不能忽略的严格特例

若方向只有高度，即 $\xi=\nu=0$，则 $T_\alpha=T_0$，$U_\alpha=U_0+\alpha b_\delta e_3$，所以

$$
e_\alpha=e_0+2\alpha b_\delta U_{0,3}+\alpha^2b_\delta^2,
\qquad
f_\alpha=f_0+\alpha b_\delta T_{0,3}.
\tag{20}
$$

旧 affine-observable 线精确漏掉了 $\alpha^2b_\delta^2$。这已经证明“$T$ 不变”不足以使 $e,f$ 都沿真实参数线仿射。本稿不据此断言任何已观察方向的误差由高度主导。

## 4. 对旧两层预测的精确比较

原 branch 为

$$
\phi_\sigma(e,f)
 =\frac{\sigma e+\sqrt{e^2+4f^2+\varepsilon^2}}2,
\qquad \sigma\in\{+1,-1\},\quad \varepsilon=10^{-8}.
\tag{21}
$$

有三种不同对象：

| 对象 | 保留的信息 |
|---|---|
| 原一阶主问题 | $\phi_\sigma(e_0,f_0)+\alpha D\phi_\sigma(e_0,f_0)[e_{[1]},f_{[1]}]$ |
| 旧 affine-observable 线 | $\phi_\sigma(e_0+\alpha e_{[1]},f_0+\alpha f_{[1]})$ |
| 真实参数线 | $\phi_\sigma(e_\alpha,f_\alpha)$，$e_\alpha,f_\alpha$ 由式 (9)、(17) 给出 |

前两者之间的凸性比较不能延伸成第二、第三者之间的上界。

记 $r=(e^2+4f^2+\varepsilon^2)^{1/2}$。真实线上的二阶 branch 为

$$
\begin{aligned}
\frac{d^2}{d\alpha^2}\phi_\sigma(e_\alpha,f_\alpha)
={}&\phi_e e''+\phi_f f''\\
 &+\frac{e'^2+4f'^2}{2r}
 -\frac{(ee'+4ff')^2}{2r^3}.
\end{aligned}
\tag{22}
$$

第二行非负；第一行包含式 (19) 的完整几何二阶量，没有固定符号。这说明旧 affine-observable 的凸性证明不能用于新的真实参数线。本稿没有证明这条真实线的完整最大包络凸，因而不能免费沿用旧凸搜索的最小性结论。

同时，对任意两组 $(e,f)$，

$$
|\phi_\sigma(e+\Delta e,f+\Delta f)-\phi_\sigma(e,f)|
 \le \frac{|\Delta e|+\sqrt{\Delta e^2+4\Delta f^2}}2
 \le |\Delta e|+|\Delta f|.
\tag{23}
$$

此界没有 $1/\varepsilon$ 的巨大因子。原未平滑实际 norm
$\eta=(|e|+\sqrt{e^2+4f^2})/2$
也满足同一 Lipschitz 界，而

$$
0\le \max_\sigma\phi_\sigma(e,f)-\eta(e,f)\le\varepsilon/2.
\tag{24}
$$

## 5. 可实用的 Taylor 余项常数

本节在一个固定 $\alpha$ 区间 $[0,A]$ 上给出明确有限上界，未对当前实际数组求这些常数。

### 5.1 同一完整角算子的范数

连续零均值周期原函数可写为 sawtooth 核，其 $L^\infty$ 算子范数不超过 $\pi/2$。对于原 $N$ 点实 FFT 原函数，记其矩阵为 $\Pi_N$，则

$$
C_N=\max_i\sum_j|(\Pi_N)_{ij}|
 \le\left(2\sum_{k=1}^{N/2-1}\frac1{k^2}\right)^{1/2}
 \le\frac{\pi}{\sqrt3}.
\tag{25}
$$

证明是对每行作 Cauchy–Schwarz 和离散 Parseval；原实输出的 Nyquist 原函数系数为零。由此对三向量场也有
$\|\Pi_NF\|_{\infty,2}\le C_N\|F\|_{\infty,2}$。
它是固定算子的实数范数界，不是 FFT 浮点舍入的后验界。

### 5.2 一维归一化导数足以给完整常数

令 $c(v)=(1+v^2)^{-1/2}$，$d(v)=vc(v)$。写 $H^{(j)}$ 为相位的 $j$ 阶导数，其长度均为 $1$。对任意 $k\ge1$，

$$
T_{[k]}(\alpha)
=\sum_{j=0}^{k}\binom{k}{j}
 c^{(j)}(v_\alpha)\nu^j\xi^{k-j}H_\alpha^{(k-j)}
+d^{(k)}(v_\alpha)\nu^ke_3.
\tag{26}
$$

这是实际 $T_\alpha$ 的导数，不是新增 profile 近似。metric 三阶余项只需此式的 $k\le3$ 及其一次径向导数，因此归一化函数最多用到四阶：

$$
\begin{aligned}
c'&=-vc^3,&c''&=(2v^2-1)c^5,\\
c'''&=3v(3-2v^2)c^7,&
c''''&=3(3-24v^2+8v^4)c^9,\\
d'&=c^3,&d''&=-3vc^5,\\
d'''&=3(4v^2-1)c^7,&
d''''&=15v(3-4v^2)c^9.
\end{aligned}
\tag{27}
$$

在固定径向位置，对所有角点及 $\alpha\in[0,A]$，取

$$
X=\|\xi\|_\infty,\quad V=\|\nu\|_\infty,\quad
X_s=\|\xi_s\|_\infty,\quad V_s=\|\nu_s\|_\infty,
$$

$$
S_u=\|u_s\|_\infty+A X_s,\qquad
S_v=\|v_s\|_\infty+A V_s.
\tag{28}
$$

令 $C_j,D_j$ 是 $c^{(j)},d^{(j)}$ 在真实区间
$v+\alpha\nu$ 上的绝对值上界。定义

$$
N_k=\sum_{j=0}^k\binom{k}{j}C_jV^jX^{k-j}+D_kV^k.
\tag{29}
$$

则 $\sup_{\alpha,\theta}|T_{[k]}|\le N_k$。将式 (26) 完整求一次 $s$ 导数，给出

$$
\begin{aligned}
S_k={}&
\sum_{j=0}^{k}\binom{k}{j}\big[
 C_{j+1}S_vV^jX^{k-j}
 +C_j S_uV^jX^{k-j}\\
&\hspace{29mm}
 +jC_jV^{j-1}V_sX^{k-j}
 +(k-j)C_jV^jX^{k-j-1}X_s\big]\\
&+D_{k+1}S_vV^k+kD_kV^{k-1}V_s .
\end{aligned}
\tag{30}
$$

系数为零的项直接省略，不使用 $0^{-1}$。式 (30) 同时保留背景导数和方向导数，并给
$\sup|\partial_sT_{[k]}|\le S_k$。

取

$$
M_k=C_N\big(|a_s|N_k+aS_k\big)
        +{\bf1}_{k=1}|b_\delta|,\qquad k=1,2,3.
\tag{31}
$$

于是 $\sup|U_{[k]}|\le M_k$。可取

$$
M_0=\|U_0\|_{\infty,2}+A M_1
\tag{32}
$$

作为整段的 $|U_\alpha|$ 上界。所有 $C_j,D_j$ 可由显式有理函数 (27) 在一个有限实区间有向包住；此处没有调用另一个参数搜索。

### 5.3 metric 二阶多项式与三阶余项

定义

$$
e_Q=e_0+\alpha e_{[1]}+\frac{\alpha^2}{2}e_{[2]},
\qquad
f_Q=f_0+\alpha f_{[1]}+\frac{\alpha^2}{2}f_{[2]}.
\tag{33}
$$

完整三阶乘积法则给

$$
e'''=6U'\cdot U''+2U\cdot U''',
\quad
f'''=U'''\cdot T+3U''\cdot T'
           +3U'\cdot T''+U\cdot T'''.
\tag{34}
$$

因此可用

$$
L_e^{(3)}=6M_1M_2+2M_0M_3,\quad
L_f^{(3)}=M_3+3M_2N_1+3M_1N_2+M_0N_3
\tag{35}
$$

得到逐点严格的实数 Taylor 界

$$
|e_\alpha-e_Q|\le\frac{\alpha^3}{6}L_e^{(3)},\qquad
|f_\alpha-f_Q|\le\frac{\alpha^3}{6}L_f^{(3)}.
\tag{36}
$$

如只需要评估旧一阶观测预测的误差，可用

$$
L_e^{(2)}=2M_1^2+2M_0M_2,\qquad
L_f^{(2)}=M_2+2M_1N_1+M_0N_2,
\tag{37}
$$

把式 (36) 换成
$\alpha^2L^{(2)}/2$。

把式 (23) 与 (36) 组合，对每个网、每个原角点、每个 branch 成立；再取**全部原点**的最大值仍成立。尤其记 $R_e,R_f$ 为相应余项上界，则

$$
\eta_\alpha
 \le \max_\sigma\phi_\sigma(e_Q,f_Q)+R_e+R_f,
\tag{38}
$$

$$
\eta_\alpha
 \ge \max_\sigma\phi_\sigma(e_Q,f_Q)-R_e-R_f-\varepsilon/2.
\tag{39}
$$

全网使用全网最大的余项，或者逐原点加其自己的余项后取最大。不能只在旧四个 attainer 上加界后称已经覆盖全网。

## 6. 原曲率 PSD 的完整方向式

为避免与前文 $U=X_s$ 混淆，设

$$
A_\alpha=U_\alpha,\quad
B_\alpha=X_{\alpha,ss},\quad
C_\alpha=X_{\alpha,s\theta}/a
       =\frac{a_s}{a}T_\alpha+T_{\alpha,s},\quad
D_\alpha=X_{\alpha,\theta\theta}/a^2=T_{\alpha,\theta}/a.
\tag{40}
$$

令

$$
w_\alpha=A_\alpha\times T_\alpha,\qquad q_\alpha=|w_\alpha|,
$$

$$
I_\alpha=
\begin{pmatrix}|A_\alpha|^2&A_\alpha\cdot T_\alpha\\
 A_\alpha\cdot T_\alpha&1\end{pmatrix},
\qquad
K_\alpha=
\begin{pmatrix}w_\alpha\cdot B_\alpha&w_\alpha\cdot C_\alpha\\
 w_\alpha\cdot C_\alpha&w_\alpha\cdot D_\alpha\end{pmatrix}.
\tag{41}
$$

这些就是原 curvature_values 在真实第一基本形式下的矩阵。对原固定曲率 cap $\kappa$，$\tau=1/\kappa$，原两 PSD 矩阵是

$$
H_\pm=qI\pm\tau K.
\tag{42}
$$

原四行是 $\operatorname{tr}H_+,\det H_+,
\operatorname{tr}H_-,\det H_-$，随后乘原 row scale。没有把 $I$ 换成单位阵，也没有把 $q$ 删除。

沿方向的新增二阶量准确为

$$
\begin{aligned}
B_{[k]}&=
 a_{ss}\Pi T_{[k]}+2a_s\Pi\partial_sT_{[k]}
 +a\Pi\partial_s^2T_{[k]}
 +{\bf1}_{k=1}b_{\delta,s}e_3,\\
C_{[k]}&=(a_s/a)T_{[k]}+\partial_sT_{[k]},\\
D_{[k]}&=(1/a)\partial_\theta T_{[k]},
\qquad k=1,2.
\end{aligned}
\tag{43}
$$

$\partial_\theta$ 中必须保 $\partial_\theta\psi_\alpha=1+u_{\alpha,\theta}$。式 (43) 需要当前及方向的 scalar 二阶径向 jet 与一阶角向 jet；不是一次局部 $T$ 值或 selected metric gradient 可以代替的。

进一步，

$$
w'=A'\times T+A\times T',\qquad
w''=A''\times T+2A'\times T'+A\times T'',
\tag{44}
$$

$$
q'=\frac{w\cdot w'}q,\qquad
q''=\frac{|w'|^2+w\cdot w''}q
       -\frac{(w\cdot w')^2}{q^3}.
\tag{45}
$$

$I'$、$I''$ 由式 (41) 直接完整求导。特别地其右下角均为零，因为真实 $|T_\alpha|^2=1$；这不是把 $T$ 冻结。对 $Z=B,C,D$，

$$
(w\cdot Z)''=w''\cdot Z+2w'\cdot Z'+w\cdot Z''.
\tag{46}
$$

故

$$
\boxed{
H_\pm''=q''I+2q'I'+qI''\pm\tau K'' .
}
\tag{47}
$$

式 (43)–(47) 是原 PSD 矩阵的完整方向二阶模型。旧高度方向通过 $A',B'$ 及乘积进入，不能因其参数二阶为零而省掉。

### 6.1 first-jet 付费边界

当前 U/T 缓存给 $A_0,T_0,w_0,q_0,I_0$。当前 scalar frame 给 $C_0,D_0$ 及式 (43) 的方向项。**一般还缺 $B_0$ 中的当前真实 $b_s$**，或等价的已绑定基点位置二阶数据。

在一般表面中，一个点的一阶 jet 不决定二阶基本形式；给 $X_{ss}$ 增加一个正常分量会保持该点 $X_s,X_\theta$ 而改变曲率。因此不能仅凭 U/T 缓存声称式 (42) 的全部基点输入已经恢复。原 paid scalar trace/determinant 或 selected J 也不应未经额外原式识别就冒作完整 $B_0$ 向量。

若下一模型需要曲率二阶预测，最小明确补输入是同点当前 $b_s(s)$ 或完整 $B_0$，连同固定 $a_{ss}$ 与当前 scalar 二阶 jets。可以研究直接固定高度密度路径，避免 center 的原函数；但这是必要新输入工作，须在实际任务中计时，不在本稿宣称已经付费。全部 actual 14 门仍保原普通几何，包括需要 $X$ 的高度、ball、strip、mirror 等条件。

## 7. 原 PSD 四行的严格线性模型余项界

以下给出不用假设 $H_\pm$ 已经 PSD 的界。所有范数除注明外为向量 Euclidean 或矩阵 Frobenius；取整段 $\alpha\in[0,A]$ 的上界。

设

$$
\|A\|\le M_0,\quad \|A^{(j)}\|\le M_j,\quad
\|T^{(j)}\|\le N_j\quad(j=1,2).
$$

可取

$$
W_1=M_1+M_0N_1,\qquad
W_2=M_2+2M_1N_1+M_0N_2,\qquad Q=M_0
\tag{48}
$$

分别控制 $|w'|,|w''|,q$。这里可以逐原点使用 $q_0$；若要同一全网常数，就用该网原 $q_0$ 的最小值。如果真实已知

$$
q_*=q_0-AW_1>\text{原 normal-area floor},
\tag{49}
$$

则整段独立面积门保持，且

$$
|q'|\le W_1,\qquad
|q''|\le W_2+\frac{W_1^2}{q_*}.
\tag{50}
$$

式 (49) 是一个可用的充分估计；若它不给正数，并不等于真实面积门失败，也不自动产生新的排除条件。

定义

$$
Z_j=\sup_\alpha
 \big(\|B^{(j)}\|^2+2\|C^{(j)}\|^2+\|D^{(j)}\|^2\big)^{1/2},
 \qquad j=0,1,2.
\tag{51}
$$

这些可由式 (26)、(43) 和必要基点二阶输入包住。再取

$$
\begin{aligned}
I_0^*&=M_0^2+1,\\
I_1^*&=2M_0M_1+\sqrt2(M_1+M_0N_1),\\
I_2^*&=2(M_1^2+M_0M_2)
       +\sqrt2(M_2+2M_1N_1+M_0N_2).
\end{aligned}
\tag{52}
$$

它们分别控制 $\|I\|_F,\|I'\|_F,\|I''\|_F$。例如非对角项是 $f$，不能由 $T$ 单位长度而删除。

原矩阵可共同使用

$$
\begin{aligned}
L_0={}&Q I_0^*+\tau QZ_0,\\
L_1={}&W_1I_0^*+QI_1^*
       +\tau(W_1Z_0+QZ_1),\\
L_2={}&\left(W_2+\frac{W_1^2}{q_*}\right)I_0^*
       +2W_1I_1^*+QI_2^*\\
      &+\tau(W_2Z_0+2W_1Z_1+QZ_2).
\end{aligned}
\tag{53}
$$

于是对两个符号均有 $\|H_\pm^{(j)}\|_F\le L_j$，$j=0,1,2$。

对任意实 $2\times2$ 矩阵函数，

$$
(\det H)''=\operatorname{cof}(H):H''+2\det H',
\quad
\|\operatorname{cof}(H)\|_F=\|H\|_F,\quad
2|\det H'|\le\|H'\|_F^2.
\tag{54}
$$

故

$$
|(\operatorname{tr}H_\pm)''|\le\sqrt2L_2,\qquad
|(\det H_\pm)''|\le L_0L_2+L_1^2.
\tag{55}
$$

记原 curvature scale 为 $s_c>0$，原代码的 trace、determinant 两类倍率分别为 $\kappa/s_c$、$(\kappa/s_c)^2$。相应原行 $r$ 的一阶模型余项严格满足

$$
\begin{aligned}
|r_{\rm tr}(\alpha)-r_{\rm tr}(0)-\alpha r_{\rm tr}'(0)|
 &\le\frac{\alpha^2}{2}\frac{\kappa}{s_c}\sqrt2L_2,\\
|r_{\rm det}(\alpha)-r_{\rm det}(0)-\alpha r_{\rm det}'(0)|
 &\le\frac{\alpha^2}{2}
       \left(\frac{\kappa}{s_c}\right)^2(L_0L_2+L_1^2).
\end{aligned}
\tag{56}
$$

这保留了原四行、原 cap、原 scale 和原容差。可将已付 $r(0),r'(0)$ 与真实有向的右侧结合成一个充分下界；不能把未经估计的 $L_j$ 当成已经认证的 guard，也不修改当前实际任务的验收门。

更直接的矩阵形式为

$$
\|H_\pm(\alpha)-H_\pm(0)-\alpha H_\pm'(0)\|_{\rm op}
 \le\frac{\alpha^2}{2}L_2.
\tag{57}
$$

若线性矩阵的最小特征值严格超过此界，便足以推出同点原 PSD；若不超过，只是此充分估计没有结论。原 direct principal-curvature 门和正常面积门仍各自保留。

## 8. 小物理域为何有数学意义，且仍不保证下降

由 R501 的真实映射

$$
M=\operatorname{diag}(I_{154},H_{9\times5},I_9)
\in\mathbb Q^{172\times168}
\tag{58}
$$

可选出一个对角为 $\pm1$ 的 $168$ 行方阵。因此对每个真实方向，

$$
\|\delta\|_\infty\le\|M\delta\|_\infty=h/4.
\tag{59}
$$

原 scalar basis 固定，所以例如

$$
|\xi(s,\theta)|
 \le \frac h4\sum_j|U_j(s,\theta)|,\qquad
|\xi_s(s,\theta)|
 \le \frac h4\sum_j|\partial_sU_j(s,\theta)|,
\tag{60}
$$

$v$、高度及必要空间导数同理。不存在因换成 $168$ 坐标就未被新物理范数控制的高度自由列。

在一个固定背景和固定有界方向盒上，式 (26)、(30)、(31) 的第 $k$ 个方向导数齐次为 $h^k$；因而真实一阶 metric 和 PSD 预测的二阶余项为 $O(h^2)$，metric 二阶模型的余项为 $O(h^3)$。常数含真实 scalar 空间导数、全角算子、固定 $a$、以及曲率中不可删的正常面积下界。

特别地，同一方向缩小 $128$ 倍，二阶主误差相应缩小 $128^2$ 倍，三阶主余项缩小 $128^3$ 倍；若比较不同方向，只能用共同盒上的统一上界，不能把这个比例直接写成实际观测误差比例。

作为精确数学约束，当前新小域 $h\le1/128$ 给全部 $172$ 物理位移
$\|M\delta\|_\infty\le1/512$。有限主问题的 norm/box 行仍保原数值容差，有限行通过不能自动授予精确不等式；当前 small168 的实际候选另按原有理坐标映射逐项判断精确172盒和 $h\le1/128$，没有给该精确判门添加容差。这使一阶模型的误差控制有明确的尺度意义；它不证明该域含严格下降，也不证明 curvature floor 与其它硬行可同时满足。狭窄可行域、不同 active 点及有限主问题未覆盖的行都仍是独立问题。

## 9. 可实施的下一预测层及不能越过的边界

式 (9) 给两种真正不同、均可只沿一个方向实现的层：

1. **真实非线性 first-jet 线。** 固定当前完整 scalar fields 与方向 fields，逐 $\alpha$ 用原 $c(v_\alpha)$、相位 $\theta+u_\alpha$ 及两次完整 $\Pi$ 计算 $U_\alpha,T_\alpha$，再取全部两网实际 metric 函数。这是新的非线性 scalar 会话；不能因没有 LP 后端而称作“零求解”，也不能沿用旧 affine-line 已付查询。
2. **方向二阶模型加余项。** 一次得到式 (13)–(19) 的方向数组，随后用式 (33) 做低成本标量查询。若要数值上界，还必须在同一次明确预算内给出式 (35) 的真实有向常数。二阶预测本身不等于误差证书。

两者都不需要旧 center 前缀或 dense 参数 Hessian，也不重算已付硬行 Jacobian。曲率二阶层则需第 6.1 节的额外基点输入，不能偷偷借 U/T 的名义恢复完整 ordinary。

实际候选必须沿原坐标应用规则取得：

$$
\widehat q_\alpha=\operatorname{Apply}_{\rm original}(q_0,\alpha\delta).
\tag{61}
$$

若其 binary64 坐标不等于式 (1) 的实数点，新 predictor 要么在这个实际坐标上重新形成真实 scalar fields，要么明确包住
$\widehat q_\alpha-q_\alpha$ 的影响。不能只给 $\alpha$ 很小的口头说明。原 exact172 物理盒、相同 $M$ 和真实端点关系仍按实际坐标检查。

对于连续物理族，精确参数线的物理系数由同一个仿射 $M$ 映射，所以两个端点在盒内足以保证两者间的实数线在盒内；该事实不代替式 (61) 的舍入点验收。原 null-height 约束和新增零总高度列仍逐个保持，不经重新拟合或投影。

最后，任何新 predictor 都只产生候选或已明确范围内的充分估计。原两网 14 门、direct curvature、strict metric improvement、全部真实新行学习和费用账没有因此被替换。本稿付的是完整公式与必要输入边界；没有对当前第 $56$ 点再做科学调用，也没有借数学等价恢复旧已闭任务。

