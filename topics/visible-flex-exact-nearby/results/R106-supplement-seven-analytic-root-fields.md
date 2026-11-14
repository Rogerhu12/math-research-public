# R106 补充：完整根首相位的七个解析输入与非均值 Fourier 误差

2026-11-13，constructive-route。

本文证明统一的有限输入合同，并保存两个实际计算入口。**两个新入口尚未运行；本文没有新增候选的七场系数、宽复盘通过报告或完整 $b-\beta$ 证书。** 已执行的根密度迁移、$q<28$ Chebyshev 门和全时真实射线管仍按各自原范围使用。

## 1. 对象、坐标和保留的端项

对象固定为 step5 exact affine 家族，中心

$$
p_5=-7789843107295549/4611686018427387904,\qquad
|p-p_5|\le10^{-9}.
$$

$t=t(p)$ 是径向输出度量的真实正根，与 $\theta$ 无关。设 $\rho=t-r=s^2$，$\theta$ 是周期 $\pi/2$ 的物理角。用 R106 原始高度 $\zeta$，不换成 grounded 算子。物理 $r$ 坐标的密度主系数
记为 $a,b,c$，其缩放量是 $a_0=\zeta^2a,b_0=\zeta^2b,c_0=\zeta^2c$。
因此 inward 特征漂移为 $q=-b_0/a_0$。

令

$$
Q(\rho,p)=\frac{-K_0(t-\rho,p)}{\rho},\qquad
\kappa=\sqrt Q,\qquad k_*=\kappa/a_0,
$$

并在实际正根分支取平方根。$K_0$ 只依赖径向与参数。定义

$$
\begin{aligned}
L_\theta&=-2(\log\zeta)_\theta,\\
L_{\rho,\mathrm{reg}}&=\frac{Q_\rho}{2Q}+2(\log\zeta)_r,\\
S_{\mathrm{reg}}&=\frac{\omega_0\ell}{\kappa},\\
U_0&=\frac {a_0}{2\kappa},\qquad
U_1=\frac{a_0L_{\rho,\mathrm{reg}}-b_0L_\theta}{\kappa}.
\end{aligned}
\tag{106RF.1}
$$

其中 $\ell$、$\omega_0=(K_{\rm actual}-K_0)/a_0$ 保留 R106 的完整几何定义。于是

$$
sS(s^2,\theta)=S_{\mathrm{reg}}(s^2,\theta),\qquad
V_\rho=s^{-3}U_0+s^{-1}U_1.
\tag{106RF.2}
$$

证明只需 $\mu=s\kappa/\zeta^2$，故
$L_\rho=(\log\mu)_\rho=(2\rho)^{-1}+Q_\rho/(2Q)+2(\log\zeta)_r$；
再代入 $V_\rho=(aL_\rho-bL_\theta)/\mu$，共同的 $\zeta^{-2}$ 因子准确抵消，
得到 (106RF.2)。具体程序直接沿用 R106 的 $a_0=-n/G,\ b_0=m/G$ 与
$\kappa$ 公式，不把 physical 与 inward mixed 系数混用。

加上 $G=\rho^{5/2}D_{\rm red}$，实际所需恰为七个根解析函数

$$
G,\quad q,\quad k_*,\quad S_{\mathrm{reg}},\quad L_\theta,\quad U_0,\quad U_1.
\tag{106RF.3}
$$

由准确 $\theta\mapsto-\theta$ 反射，$G,k_*,U_0,U_1$ 为偶函数，
$q,S_{\mathrm{reg}},L_\theta$ 为奇函数。这个结论先由真实几何得到，
有限 DFT 才可复用半周期节点。

R106 的 transport-counterterm 定理给
$B=-G_0/(3s^3)+B_1/s$ 与解析源 $\mathcal R_\sigma$。完整单根首相位为

$$
\begin{aligned}
h_\sigma={}&J_c\left[
 B(c,\Theta_c)-\frac{U_0(c^2,\Theta_c)}{4c^3}
             -\frac{U_1(c^2,\Theta_c)}{4c}
             -\frac{\sigma}{4}L_\theta(c^2,\Theta_c)\right]\\
&+\int_0^c(\mathcal R_\sigma\circ\Theta)J\,ds
 +\partial_x\int_0^c S_{\mathrm{reg}}(s^2,\Theta)\,ds
 +\frac{\sigma}{4}J_0L_\theta(0,\Theta_0).
\end{aligned}
\tag{106RF.4}
$$

这里 $c=c(p)>0$ 对应原固定物理 cut，$J=\Theta_x$ 是实际输入标签导数。
本式不把 $J_0$ 设为 $1$。物理角 Fourier 微分乘 $4ik$，标签 $x$ 的微分
按标签自己的频率计算；半程积分无额外因子 $4$。

## 2. 同一真实复盘上的曲率 deflation 与辅助场

若整个复盘内 $K_0$ 解析且 $K_0(t,p)=0$，准确有

$$
Q(\rho,p)=\int_0^1K_{0,r}(t-z\rho,p)\,dz,\qquad
Q_\rho=-\int_0^1zK_{0,rr}(t-z\rho,p)\,dz.
\tag{106RF.5}
$$

所以包含整个 $K_{0,r}$ 值集的复矩形同时包含 $Q$；包含
$-K_{0,rr}/2$ 值集的凸矩形同时包含 $Q_\rho$。第二个因子 $1/2$
来自 $\int_0^1z\,dz$，不能遗漏。若所用 Taylor 系数是 $K_{[2]}=K_{rr}/2$，
直接用 $-K_{[2]}$ 的全盘包围即可。

目标曲率是

$$
K_0=(a'E'-2a''E)/(2aE^2).
$$

支付 $K_{0,r},K_{0,rr}$ 的全复盘只需要真正的 $a$ 到四阶、$E$ 到三阶。
代码先给每阶 $E$ 加完整无限原函数误差和径向 Taylor 尾，再形成商，
保留复值；没有把复径向求值投影到实轴。全盘 $\Re Q>0$ 固定平方根支。

几何辅助场用 $C=F_\theta\times F_r$、$G=C\cdot C$、
$H=C\cdot F$ 和 $R^2=F\cdot F$。准确公式为

$$
(\log\zeta)_r=\frac{C_r\cdot F}{H}
             -\frac{C\cdot C_r}{G}-\frac{F\cdot F_r}{R^2},\qquad
(\log\zeta)_\theta=\frac{C_\theta\cdot F}{H}
             -\frac{C\cdot C_\theta}{G}-\frac{F\cdot F_\theta}{R^2}.
\tag{106RF.6}
$$

$C\cdot F_r=C\cdot F_\theta=0$ 是完整真实叉积恒等式。$F_z,H,R^2,G,a_0$
的复分母分别付清后，(106RF.1) 的四个辅助量可直接由同一六 jet 计算。
$q,k_*$ 与这些辅助量的界因此属于同一个 germ、参数盒及复域。

新源 scripts/fourfold_subprincipal_root_bidisk_domain.py 对每个闭角单元执行
这些运算，另调用冻结的完整 $G$ 域函数。只有全部闭单元及所有分母通过，
才输出 complete=true。默认尝试物理角宽 $1/64$ 不是一个已经通过的事实；
若失败，必须保留失败报告，再以新输出路径缩域重跑。

## 3. 完整双变量近似：无均值替换、无未知系数填零

设任一七场函数 $f$ 在 $|\rho|\le R$、$|\Im\theta|\le S$ 上解析并有
$|f|\le M$。真实 Taylor 展开记为

$$
f(\rho,\theta)=\sum_{n\ge0}f_n(\theta)(\rho/d)^n,
\qquad d>0
$$

其中 $d$ 是保存的准确 dyadic scale。于是 $|f_n|_S\le M(d/R)^n$。
对每个 $n\le m$，在实际等距 $N$ 节点给出真 $f_n$ 的球，选择它们的
准确 dyadic 中点作 DFT；只保留 $|k|\le K<N/2$，并完整保存
$e^{4ik\theta}$ 的正负频率。

令 $r<R,\ s<S$，$S_x=4S,\ s_x=4s$。完整角 alias 系数费是

$$
A_{N,K}(S_x,s_x)=
 \sum_{|k|\le K}e^{s_x|k|}
 \frac{e^{-S_x(N-|k|)}+e^{-S_x(N+|k|)}}{1-e^{-S_xN}},
\tag{106RF.7}
$$

未留角频费是

$$
T_K(S_x-s_x)=\frac{2e^{-(S_x-s_x)(K+1)}}{1-e^{-(S_x-s_x)}}.
\tag{106RF.8}
$$

证明对保留 $k$ 显式求和所有 $k+\ell N,\ell\ne0$，对未保留真实频率
求完整几何级数；Nyquist 及更高频率都在补集中。

若 $e_{jn}$ 是真节点球到所选节点中点的模误差，记
$\epsilon_n=(N^{-1}\sum_j e_{jn}^2)^{1/2}$。归一 DFT 的 Parseval 恒等式
与加权 Cauchy–Schwarz 给保留模式误差

$$
\left(1+2\sum_{k=1}^K e^{2s_xk}\right)^{1/2}\epsilon_n.
\tag{106RF.9}
$$

这已经包含真正无限原函数和整个参数盒在节点的球宽。实际 Arb DFT 运算
以及最终 dyadic 系数选择的加权 $l^1$ 误差另加，不能用节点 RMS 代替它们。

令 $\varepsilon_n$ 表示 (106RF.9) 加 DFT/选择费，则完整函数差为

$$
\begin{aligned}
|f-\widehat f|_{r,s}\le{}&
\sum_{n=0}^m(r/d)^n\left[
 \varepsilon_n+M(d/R)^n(A_{N,K}+T_K)\right]\\
&+\frac{M(r/R)^{m+1}}{1-r/R}.
\end{aligned}
\tag{106RF.10}
$$

先对保留径向行付全部角补集，再付所有 $n>m$ 的完整函数；
两个补集既无遗漏也不需要互相重复。该式是全复 bidisk 的 sup 误差，
不是自动得到同宽 Wiener 误差。

scripts/fourfold_subprincipal_root_fourier.py 实现此合同。每 32 个已算真实节点
写一个 gzip checkpoint，每若干径向行另写准确系数 shard。报告保存完整科学身份、
输入和源 SHA、所有费用及全部 shard SHA。三个主场可用已完成的窄域证明；
请求四个辅助场时必须提供新执行完成的共同 bidisk 报告，不能套用只给 $G/q/k_*$
的旧常数。尚没有实际生成的七场候选报告。

## 4. 完整有限 cut、正则源和误差接口

保存系数乘 $(\rho/d)^n$，所以真实 $\rho$ 系数移位要带尺度：

$$
\begin{aligned}
\widehat B_1&=-\widehat G_1/d-\tfrac23D_\theta(\widehat q_0\widehat G_0),\\
\widehat{\mathcal R}_{2n}^{(w)}
&=\widehat G_{n+2}/d^2+\tfrac{2}{3d}
 D_\theta(\widehat q_{n+1}\widehat G_0)
 -2D_\theta(\widehat q_n\widehat B_1),\\
\widehat{\mathcal R}_{2n+1}^{(w)}
&=-\tfrac{2\sigma}{3d}D_\theta(\widehat k_{n+1}\widehat G_0)
 +2\sigma D_\theta(\widehat k_n\widehat B_1).
\end{aligned}
\tag{106RF.11}
$$

有限输入的零延拓只定义所选多项式，不替未知真实 Taylor 系数填零。
有限 Laurent 乘法必须保留全部输出频率；若用 FFT 卷积，填充长度至少为
两段支持长度之和减一，逆 DFT 的完整误差留在系数球内。

由 (106RF.10) 得到的 $e_G,e_q,e_k$ 应作为 transport-counterterm 定理的
同一外域误差输入。这里该定理的“外域”是已经支付有限函数差的
$(r,s)$，不是原先只支付真实模数的 $(R,S)$。因此要在实际 cut 与该误差域
之间再留严格径向、角向裕量。

辅助场在同一误差域内有误差 $e_S,e_L,e_{U0},e_{U1}$。
固定真实 $c>0$ 的有限 cut 近似误差另加

$$
\frac{e_{U0}}{4c^3}+\frac{e_{U1}}{4c}+\frac{e_L}{4}.
\tag{106RF.12}
$$

两端 $L_\theta$ 费用均保留。若积分时以有限 $c$ 代替真实 $c(p)$，
还必须另付端点位置误差；本合同没有免费转移端点。

在同一真实射线 $\Theta$ 上，$\partial_x\int S_{\rm reg}(s^2,\Theta)\,ds$
等于 $\int (\partial_\theta S_{\rm reg})(s^2,\Theta)J\,ds$。
因而可和 $\mathcal R_\sigma$ 合成同一一形式密度
$\mathcal R_\sigma+\partial_\theta S_{\rm reg}$，再沿实际射线积分。
若有额外物理角损失 $\delta>0$，此项的有限函数误差增加 $e_S/\delta$。
这一步没有删除周期导数，保留其完整非零 Fourier 输出与零频。

真射线与参考 $Y,Q$ 之间，所有一形式沿用已证明的完整规则

$$
|H(\Theta)J-\widehat H(Y)Q|
\le \|H\|e_J+\|Q\|(\|H_\theta\|e_\theta+e_H).
\tag{106RF.13}
$$

使用哪个标签、哪个真实参数盒、哪个全时复管必须在实际积分报告中绑定；
端点主返回误差不能替代全时误差。当前尚欠实际七场系数、完整有限积分、
两根/严格区拼接，以及 R46/R104 的真实共轭与强余项费用。

## 5. 可复放的第一次运行

在课题目录，先执行共同复盘，只有真实通过才接第二步：

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python scripts/fourfold_subprincipal_root_bidisk_domain.py \
      --half-width 1/1000000000 --physical-strip 1/64 --radial-radius 1/2500 \
      --precision 40 --angles 2048 --nodes 512 \
      --out notes/2026-11-13-R106-root-seven-field-domain.json.gz

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python scripts/fourfold_subprincipal_root_fourier.py \
      --domain-report notes/2026-11-13-R106-root-seven-field-domain.json.gz \
      --include-root-aux --degree 6 --precision 16 --angles 512 --keep 200 \
      --working-radius 7/25000 --working-strip 1/400 \
      --out-dir data/R106/root_seven_field_first_layout

第二步的短布局只校准实际函数/符号/费用，不保证误差已足供 R104。
后续必须根据真实报告的径向与角尾分别选阶；例如不能看到很小的有限系数，
便略去 (106RF.10) 最后一项。当前执行器不可用、最新 Actions 仍在 runner 分配前
失败，所以以上两次实际运行均未发生。
