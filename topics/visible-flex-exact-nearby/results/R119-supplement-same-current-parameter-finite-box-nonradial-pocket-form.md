# R119 续篇：同一当前参数的全盒实际负窗控制型

2026-11-14，visible-exact / tail_connector。

**状态：已证明。** 本篇把第71束的 fresh-support 结论推进到
第68束已经启用的完整有限参数盒。没有把非零径向补偿导数删掉，
也没有把当前非径向参数换回径向原点。对一个低缩放 band
$M\in[U/2,U]$、$U^2\le B$，在当前真实
$\Gamma^*(\mathbf a,\Omega)$ 上，沿原独立坐标 $\theta_M$ 的
整负窗 crossing form 满足
$$
 \mathfrak G_{I_i,\theta_M}(Y_c)
       >\frac{r_Ud_U}{16N_{\rm band}}\|Z_M(c)\|_2^2,
 \qquad Y_c\in\mathcal E_M .                         \tag{F.1}
$$
这里输入是当前中心的 $m=\pm M$ 完整两迹，输出包含全部
Fourier 模、相反锥及两个 mean。普通、weak 源和它们的参数列
仍是完整仿射输入，没有由齐次型删去。

本篇没有将 (F.1) 改写成整个混频矩阵的 PSD。不同 $M$ 的
中心数据之间仍有交叉项；实际 physical principal 端图和
incoming Hilbert 归一也仍须共同处理。当前真正输入进入所用
小球，但完整外方程 $\mathcal F=0$ 尚未由此解决。

## 1. 同一原对象、全盒和当前中心

消费[第68束](R119-supplement-all-scaled-five-function-finite-box-generator.md)
的原允许族、原独立模式坐标及实际半径。记
$$
 \delta=\delta_j,\quad J=j+5,\quad j\ge8193,\quad
 a=\Delta/B,\quad 80<\Delta<3J,\quad
 K=2^{6000}J^8\delta^{-16}.
$$
一个尚未使用的区间 $I$ 上生成全部第68束候选方向
$\psi_M$ 后，开启这个 band 的全部参数：
$$
 \Xi^{(n)}=\frac{r_U}{N_{\rm band}}\sum_M\theta_M\psi_M,\quad
 |\theta_M|\le1,\quad N_{\rm band}\le U,
$$
$$
 d_U=2^{-22050}U^{50}B^{-39}\Delta^{-103}
                      (1+U^2/B)^{-96},\qquad
 r_U=\frac{d_U}{2^{36}K^6(U+B)^2}.                   \tag{F.2}
$$
其它区间和其它负分量的全部原允许控制可以已经非零；在求这个
局部 $\theta_M$ 导数时将它们固定。全部区间的 $C^4_x$ 总和
仍小于 $2^{-79}$。各方向在生成时属于同一个实际径向两相位
annihilator 空间，且
$$
 \|\partial_x^\ell\psi_M\|_\infty\le\rho_M^{4-\ell},\quad
 \|\partial_x^\ell\psi_M\|_{L^1(dx)}\le2\rho_M^{5-\ell},
 \quad 0\le\ell\le4,
$$
$$
 \rho_M=2^{-2204}M^5B^{-4}\Delta^{-11}(1+M^2/B)^{-10}.
                                                               \tag{F.3}
$$
开启盒后不再声称其径向 phase 导数为0。

本篇限制到真实
$$
 2^{-40}\delta^{-1/8}\le M\le U\le\sqrt B,\qquad
 \mathcal X\le2^{-1048576}.                         \tag{F.4}
$$
这是第70/71束已经由 fixed-stop incoming
$\|\mathbf a^{\rm inc}\|_{224}<2^{-60000000}10^{-8}$ 实际进入的
邻域，未假设外部残余已经清零。

当前 $Q$ 在本区间准确为
$Q=7+Bf-\Xi^{(n)}_t$，$f=30x^2(1-x)^2$。
其它控制及原两个 bump 离开 $I$。因
$\|\Xi^{(n)}\|_{C_x^4}\le r_U<2^{-80}$、$aB=\Delta>80$，
仍有
$$
 B<Q<2B,\quad |Q_t|<B^2,\quad |Q_{tt}|<B^3,\quad
 |Q_{ttt}|<B^4 .                                   \tag{F.5}
$$
例如归一改变量分别为
$r_U/\Delta,r_U/\Delta^2,r_U/\Delta^3,r_U/\Delta^4$；
原 $f>7/4$、$|f'|<2,|f''|<30,|f'''|\le45$ 留有严格余量。
这里真正只用到四阶形状导数。

当前中心仍取
$$
 k=\sqrt{7M^2-16},\quad u=\sqrt{\mu_0}h,\quad v_J=\pi/\sqrt{\mu_0},
 \quad
 Z_M=\left(\sqrt k\,u,\
     \frac{v_J-(1+Q(c))u/2}{\sqrt k}\right),\quad \mu_0=w/r .
                                                               \tag{F.6}
$$
所有参数变化时，都把当前这个中心数值向量作为型的输入单位。
实际 $\mu_0$、当前 $Q(c)$ 和物理两迹的变换没有被固定成另一
个参数点。固定腰尺度 $\rho_{\rm waist}$ 与 (F.3) 的支集宽
仍为不同量；整段 divergence 密度和全部源保持第70束的同一规范。

## 2. 径向中心矩阵的完整 Hessian：不重复损失端口条件数

先在一个径向补偿路径上工作。对任意方向 $\psi$，令
$$
 \Psi=\psi+\sum_{s=1}^2v_s^{\,0}\varphi_s
$$
为其完整径向 phase-preserving 方向。真实径向标量方程是
$$
 u_{tt}+T_Mu=0,\qquad
 T_M=M^2Q+\frac{Q_t}{2}-\frac{(1+Q)^2}{4}.
$$
因此
$$
 \dot T_M=\left(\frac{1+Q}{2}-M^2\right)\Psi_t
                                 -\frac12\Psi_{tt}. \tag{F.7}
$$
两端 $\Psi,\Psi_t$ 为0。两次分部积分和真实方程准确给
$$
 \int\dot T_Mu^2dt=-\int\Psi\mathcal K_{\rm rad}(u)\,dt,
$$
$$
 \mathcal K_{\rm rad}
 =u_t^2+(1+Q-2M^2)uu_t
                   +\left(\frac{(1+Q)^2}{4}-M^2Q\right)u^2 .
                                                               \tag{F.8}
$$
这是原物理型 $\mu_0(h_t^2-2M^2hh_t+M^2h^2)$ 的准确同一形式。
所有边界项在完整两端消失；未使用一条特殊 Robin 解。

令 $\mathcal U_M(t,c)$ 为当前 wave 状态
$(\sqrt k\,u,u_t/\sqrt k)$ 的真实双向流。于是完整中心矩阵
$$
 L_\psi^0
 =-\int\mathcal U_M(t,c)^T
       \begin{pmatrix}\dot T_M/k&0\\0&0\end{pmatrix}
                                      \mathcal U_M(t,c)\,dt
                                                               \tag{F.9}
$$
对所有实中心向量同时表示 (F.8)。这先在中心单位直接求导，
不先从 scattering PSD 反推中心矩阵而多损失一个 $K^4$。

[第54束](R119-supplement-radial-phase-compensation-and-full-Wronskian-Hessian.md)
(H.18)--(H.20) 对整个当前允许盒已付
$$
 \|\mathcal U_M(t,s)\|\le K,\quad
 \|D\mathcal U_M(t,c)\|\le2K^2R,\quad
 \int\|D\mathsf A_M\|dt<2R,\quad
 \int\|D^2\mathsf A_M\|dt<2^{20}R,\quad R=M+B/M .
                                                               \tag{F.10}
$$
最后一式包含两个补偿 bump 的二阶响应。
在 (F.9) 的左右流和中间真实方向矩阵上逐项求导，得到
$$
 \|D_\Xi L_\psi^0\|
 <8K^3R^2+2^{20}K^2R<2^{22}K^3R^2 .               \tag{F.11}
$$
这里 $R,K>1$。没有 individual eigenphase 或其它谱隙进入此估计。

在本区间尚未开启时，第68束的完整 Sym2 构造准确给
$L_{\psi_M}^0=d(M)I/4$，且 $d(M)\ge d_U$。
沿长度至多 $r_U$ 的真实补偿路径，由 $R<U+B$，
$$
 \|L_{\psi_M}^0-L_{\psi_M}^0|_{\Xi^{(n)}=0}\|
 <2^{22}K^3(U+B)^2r_U
   =\frac{d_U}{2^{14}K^3}<\frac{d_U}{64}.
$$
所以同一中心规范的整盒结论为
$$
                     L_{\psi_M}^0>\frac{d_U}{8}I .
                                                               \tag{F.12}
$$

## 3. 辅助参考路径确实终止于当前真实参数

径向的两个 normalized phase 在每个负分量准确分解为
$$
 \mathsf F_i(\Gamma_i)+\mathsf C_{\rm old}
                          +\mathsf C_n(\Xi^{(n)}).
                                                               \tag{F.13}
$$
这是原支集分离的局部积分恒等式，不是整个非径向 PDE 图的解耦。
在 $\Xi^{(n)}$ 所属 annihilator 空间，
$\mathsf C_n(0)=D\mathsf C_n(0)=0$、
$\|D^2\mathsf C_n\|<2^{-10}$。
当前完整径向两行的逆小于 $2^{10}$，其真实局部逆盒保留着原
两个参数的严格余量。

现在固定一个实际当前
$\Gamma_i=\Gamma_i^*(\mathbf a,\Omega)$。仅作估计时，定义辅助
$\Gamma_i^{\rm base}$ 为
$$
 \mathsf F_i(\Gamma_i^{\rm base})
   =\mathsf F_i(\Gamma_i)+\mathsf C_n(\Xi^{(n)}).
                                                               \tag{F.14}
$$
第54束同一有限维逆在半径 $2r_U^2$ 内给唯一解，因为
$\|\mathsf C_n(\Xi^{(n)})\|\le2^{-11}r_U^2$。所需逆导数小于
$2^{10}$，因此
$\|\Gamma_i^{\rm base}-\Gamma_i\|_\infty<r_U^2$。
全路径
$$
 \mathsf F_i(\Gamma_i(s))+\mathsf C_n(s\Xi^{(n)})
       =\mathsf F_i(\Gamma_i)+\mathsf C_n(\Xi^{(n)}),
 \quad 0\le s\le1
$$
留在同一真实内盒，并准确满足 $\Gamma_i(1)=\Gamma_i$。
其它原控制保持不动。该路径只是为了将 (F.11) 用到同一个
当前参数点；它没有改变实际目标 $\omega_i,\beta_i^0$，没有把
实际解图换成 $\Gamma^{\rm base}$ 处的图。

本区间处的 $Q$、center wave 方程和两个 phase 核，在起点
不依赖区间外的这次微小补偿。因此原第68束方向在这个辅助
起点仍给完全相同的 $d(M)I/4$。这证明 (F.12) 对所有当前
$\Gamma^*(\mathbf a,\Omega)$ 一致成立，而不是只在某个预先固定
的径向目标上成立。

在终点记该径向约束方向为
$$
 v^0=-(A^0)^{-1}f^0,\qquad
 A_i^0=D_{\Gamma_i}\mathsf F_i,\qquad
 f_i^0=D_{\psi_M}\mathsf C_n(\Xi^{(n)}).
                                                               \tag{F.15}
$$
其它径向分量的 $v_i^0$ 为0。第54束的完整二阶界给
$$
 |v_1^0|+|v_2^0|\le2r_U,\qquad \|f^0\|_1<8r_U .
                                                               \tag{F.16}
$$
非零的 $v^0$ 将在后面实际加入，不再以 fresh-support 消去它。

## 4. 实际联立切向量减去同点径向切向量

沿当前联合选择支，真实导数满足 $A v=-f$；$A$ 是第71束
准确共轭平均行与完整首密度相位行。其参数列始终在当前
$h_i$ 处评价。置
$$
 e=v-v^0,\qquad A=A^0+E .
$$
准确的方程是
$$
                  Ae=-(f-f^0)-Ev^0 .              \tag{F.17}
$$
此处两边都是同一个当前 $\Gamma,\Xi$ 的量；没有把
$A^0(\Gamma)$ 替成 $A^0$ 在未扰点的值。

写
$$
 \chi=P_j\rho_M^5,\quad P_j=2^{-42}\delta^{-231/128},\qquad
 \mathcal W_i=J_i^4\delta_i^{-6}\mathcal N_i,\quad
                  \sum_i\mathcal W_i<2^{160024}.    \tag{F.18}
$$
$\mathcal N_i$ 是第71束保完整邻胞的实际系数和。
第60束 gauged 场在当前全部 $C^4$ 允许盒仍满足
$\widehat n_i<2^{832}\mathcal N_i\mathcal X\chi$。
这是其完整 profile-ball 估计；没有重新加回局部 $\rho_M^4$
的裸场项。

第71束 action 差
$\mathscr A_\beta-\mathscr A_\beta|_{Z=0}$ 的两次分部积分依然
成立；(F.5) 是它所需的全部支集 radial 输入。因而其
actual-minus-radial 直接项和全根/strict 响应，仍带 $\chi$。
不必在当前盒重新假设 $D\beta_{\rm radial}[\psi_M]=0$。

principal 行同样先取差：
[实际两射线](R133-supplement-actual-compact-ray-endpoint-response.md)
(R.23)、(R.27) 在尚未使用 annihilator 前准确给
$$
 \|\dot{\mathcal R}-D\Theta[\psi_M]\|_{C_*^6}
                         \le6E_i+7r_i|D\Theta[\psi_M]| .
                                                               \tag{F.19}
$$
其中 $E_i$ 的完整 $\rho_M^5$ 界只用 (F.5)；
$r_i\le2^{34}J_i\mathcal N_i\mathcal X$。
后面一项现在用 (F.16) 支付，而不删掉。
真实共轭平均再乘 $(h_i'\circ T)^{-1}$，第71束
$\|h_i'-1\|<2^{96}J_i^2\delta_i^{-1}\mathcal N_i\mathcal X$
对这条非零径向常数行也产生一个实际 $O(\mathcal W_i\mathcal Xr_U)$
项。全部 raw-ray、mean-normalization 和 beta 项给
$$
 \|(f-f^0)_i\|_1
 <2^{1110}\mathcal W_i\mathcal X\chi
                  +2^{128}\mathcal W_i\mathcal Xr_U .           \tag{F.20}
$$
原系数完整复域内有充分余量，(F.5) 保持同一径向尺度；
新增的十个 bits 已包含局部参数盒的安全放宽。

第71束的完整参数矩阵行仍是
$$
 \|(Ew)_i\|_1<2^{256}\mathcal W_i\mathcal X\|w\|_\infty .
$$
由 (F.16)，(F.17) 的总 forcing 小于
$$
 2^{1110}\mathcal W_i\mathcal X\chi
                       +2^{260}\mathcal W_i\mathcal Xr_U .
                                                               \tag{F.21}
$$
同一个全部无限行逆范数小于 $2^{16}$，于是
$$
 \|e\|_\infty
 <2^{161150}\mathcal X\chi
                         +2^{160300}\mathcal Xr_U .             \tag{F.22}
$$
再逐行代回，保留每个真实深层 $\mathcal W_i$：
$$
 \boxed{\quad
 |e_{1,i}|+|e_{2,i}|
 <2^{1130}\mathcal W_i\mathcal X\chi
                      +2^{280}\mathcal W_i\mathcal Xr_U .
 \quad}                                                       \tag{F.23}
$$
两列反馈分别相对于其主项小于 $2^{160296}\mathcal X<1/2$。
这里同时保留 compact 的 $\rho_M^5$ 列和非零径向补偿的 $r_U$
列；没有为方便记号把后者免费挤入前者。

## 5. 整窗能量与完整两种小量

第70/71束的 strict、两根、constant-canonical-cut 到原 physical
cut 的全部能量证明对当前控制盒一致适用。根 germ 完全未动；
strict 输入和中心变换只使用 (F.5) 与原已付全盒 Cauchy。
特别对当前 $\mathcal E_M$ 输入，
$$
 \sup_{I_i}[\|u\|_{H^2}^2+(1+Q)\|u_\theta\|_{H^1}^2
                         +\|v_J\|_{H^1}^2]
 <2^{8400}J^{20}\delta^{-34}\|Z_M(c)\|^2,              \tag{F.24}
$$
较低的物理能量仍为 $2^{7800}J^{16}\delta^{-32}$。
这两式均含全部输出频率和 mean；变图迹已经使用径向基本定理及
真实 PDE 支付，没有以有限输入替代输出导数。

令 $\bar\rho=2^{-2204}M^5B^{-4}\Delta^{-11}$、
$d_*=2^{-22000}M^{50}B^{-39}\Delta^{-103}$。
在当前 band，
$$
 \rho_M\le\bar\rho,\qquad
 \frac{d_*}{d_U}
   =2^{50}(M/U)^{50}(1+U^2/B)^{96}\le2^{146}.        \tag{F.25}
$$
因此第69/70束的 compact actual-minus-current-radial 型与
固定 $\Gamma$ 的全部 hat 响应，可以直接在 $d_U$ 单位中支付。
此处径向场从同一个当前中心向量和同一个当前 $Q,\mu_0$ 出发。
局部短段 Cauchy 比较只需要 (F.5)，其原 norm 余量允许额外
$2^{16}$ 放宽。完整两项相对费用分别小于
$$
 2^{14200}\mathcal N_{i|j}\mathcal XJ^{70}
                         \delta^{-3655/128},\qquad
 2^{21200}\mathcal N_{i|j}\mathcal XJ^{84}\delta^{-60}.
                                                               \tag{F.26}
$$
其中 $\mathcal N_{i|j}$ 是第70束的完整六项邻胞和。

现在单独支付 $v^0$，而不是试图从一个绝对小的场差推相对正定。
实际和径向的完整 $\mathcal K$ 均由 $2^{40}$ 乘 (F.24) 控制，
两个原 bump 的幅度小于1，负窗长度小于1。由 (F.16)，两种场的
径向补偿积分绝对值之和除以 $d_U\|Z\|^2$ 小于
$$
 2^{8450}J^{20}\delta^{-34}\frac{r_U}{d_U}
 =2^{-27586}J^{-28}
                  \frac{\delta^{62}}{(U+B)^2}<2^{-27000}.
                                                               \tag{F.27}
$$
这使用的是已经支付的实际盒半径，恰含 $K^{-6}$；没有再损失
从 scattering 返回中心的 $K^4$。

真实参数场响应
$\widehat n_i^\Gamma<2^{64}\mathcal N_i\mathcal X\|v\|_\infty$
也保留。$v^0$ 这一部分的整窗型除以 $d_U$ 小于
$$
 2^{-28137}\mathcal N_{i|j}\mathcal XJ^{-32}
                  \frac{\delta^{64}}{(U+B)^2}<2^{-28000}.
                                                               \tag{F.28}
$$
所有其它层对该场的反馈已在真全参数方向导数中，不是只看
控制支集内的状态。

(F.23) 的 $\chi$ 列，逐项消费第71束的两参数 metric 型及全部
参数场响应；相对 $d_U$ 的安全界为
$$
 2^{22200}\mathcal N_{i|j}\mathcal XJ^{92}\delta^{-68},\qquad
 2^{182200}\mathcal N_{i|j}\mathcal X^2J^{84}\delta^{-60}.
                                                               \tag{F.29}
$$
这里已经支付 (F.25)、新十个 bits 和邻胞差，未改原 $\zeta$。

(F.23) 的 $r_U$ 列则用 $r_U/d_U$ 直接支付。其本窗 metric
贡献小于
$$
 2^{-27306}\mathcal N_{i|j}\mathcal XJ^{-24}
                     \frac{\delta^{56}}{(U+B)^2}<2^{-27000}.
                                                               \tag{F.30}
$$
(F.22) 的全部 $r_U$ 参数列进入实际背景后，还多一个
$\mathcal N_i\mathcal X$。其相对费用小于
$$
 2^{132162}\mathcal N_{i|j}\mathcal X^2J^{-32}
                      \frac{\delta^{64}}{(U+B)^2}<2^{-1900000}.
                                                               \tag{F.31}
$$
巨大但固定的全参数行和已经保留在132162这个指数中；
可达输入的真实百万 bit 余量支付它。

## 6. 真实全局规范和所有层

不去掉旧接缝的全局因子。第70束准确给
$$
 \mathcal N_{i|j}<2^{-20010}2^{-\alpha(j-8193)},\quad
 \alpha=31867/256,\quad j\ge8193 .                 \tag{F.32}
$$
在首层 $J=8198<2^{14}$、$\delta>2^{-8197}$，
(F.26) 两项的对数分别小于 $-810000,-550000$；
(F.29) 两项的对数分别小于 $-480000,-1400000$。
全部 $J$ 幂至多92。由
$(8199/8198)^{92}<65/64$、$(65/64)^{32}<2$，
最坏层比的衰减指数仍大于
$\alpha-68-1/32>56$。因而这些实际相对费用在整个无限深尾可和。

(F.27)、(F.28)、(F.30)、(F.31) 含有利的正 $\delta$ 幂；
其显示的小常数直接对每层成立。它们没有依赖无限个模式的
逐一“任选更小球”。所有模式使用共同实际可达的 (F.4)。

## 7. 真全盒结论与原坐标的比例

令 $v=D_{\psi_M}\Gamma^*(\mathbf a,\Omega)$，在每个实际负分量
写完整总 profile 方向
$$
 \Psi_{\rm tot}=\mathbf1_{\rm control}\psi_M
                      +v_{1,i}\varphi_{1,i}+v_{2,i}\varphi_{2,i},
$$
$$
 \widehat z_{\rm tot}
 =D_{\psi_M}(p,k)+D_\Gamma(p,k)[v]-\Psi_{\rm tot}F_1 .
                                                               \tag{F.33}
$$
完整第61束恒等式给
$$
 \mathfrak G_{I_i,\psi_M}(Y_c)
 =\int_{I_i}
    [\Psi_{\rm tot}\mathcal K_{\rm act}(Y)
                     -\mathcal H_{\widehat z_{\rm tot}}(Y)]dt .
                                                               \tag{F.34}
$$
用 (F.12) 作同点径向参考，(F.26) 付 compact 部分，
(F.27)--(F.31) 付真实非零径向补偿及实际补偿之差。
每个误差严格小于 $d_U/256$；全部八项之和小于 $d_U/16$。
由此在整个有限盒，
$$
                \mathfrak G_{I_i,\psi_M}>
                    \frac{d_U}{16}\|Z_M(c)\|^2 .     \tag{F.35}
$$
所有不等式均在同一个当前 $\Gamma^*$、当前 $\Xi$、固定原
physical 两端点上成立。

原真实独立参数方向是
$D_{\theta_M}\Xi=(r_U/N_{\rm band})\psi_M$。
完整参数方程及 crossing form 都对这个切向量线性，因此
严格乘上 $r_U/N_{\rm band}$，即得到 (F.1)。
没有把 $\theta_M$ 换成一个 band 公共参数，也没有删除会动的
外部反馈 $P'$。

## 8. 全源和下一真实量词

普通源 $g$、weak 源 $(F^t,F^\theta)$ 及其真实方向列仍是
$$
 s=(-a_{\rm Jac}F^t,\
              g-\partial_\theta(F^\theta+dF^t)),\qquad
 \widehat s_{\rm tot}=D_{\psi_M,\Gamma^*}s-\Psi_{\rm tot}\mathsf B s .
                                                               \tag{F.36}
$$
这里 $a_{\rm Jac}$ 是真实 Jacobi 首行系数，避免与 ramp 的
$a=\Delta/B$ 重名。没有 $F_t^t$。
全部列按原有序 Duhamel、根 Piola/height 换元和 physical
normal shear 合同传播。原 $L^2$ 弱源本身不授 bare-flux 端点迹；
后者仍须由 producer 单独给出。
两个物理 mean 完整为
$$
 \pi_{0,t}=g_0,\qquad
 h_{0,t}=\langle dh_\theta+a_{\rm Jac}\pi-a_{\rm Jac}F^t\rangle .
$$
真实两根附近 profile 方向及其 jets 为0，背景响应一般不为0，
已经在 (F.28)、(F.29)、(F.31) 中保留。

实际供给是同一个 fixed-stop incoming 已进入 (F.4)，以及
第53/55束定义的整个实际非径向解图和第68束允许参数盒。
条件边界是当前证明只对中心 $\mathcal E_M$ 压缩型作正定声称。
若任意中心输入同时含多个频率，$\psi_M$ 对其它频率的径向
块也可能不定，实际系数还产生交叉块；(F.1) 不控制这些块。
完整 near-kernel cluster、参数依赖的物理 principal 端图、
全部 source-to-label 同权网络仍须真实支付。
本篇没有用一个物理端口范数的微小绝对差去除以径向小谱隙。

必要新增代数和有理预算见
[源码](../scripts/fourfold_same_current_parameter_finite_box_20261114.py)、
[实际记录](../notes/2026-11-14-R119-same-current-parameter-finite-box-budget.json)。
