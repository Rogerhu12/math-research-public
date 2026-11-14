# R119 续篇：真实 Airy 单位中的全部 DN 对角及网络通量 shear

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 实际径向正段的完整 DN 对角，在本题原 Airy
高度单位中统一小于 $2^9$，包括 mean。真实更新后的对角差因此是
同 Sobolev 空间中的有界小 shear，可以从正段两端关系中准确移出。
此前的半光学 cross 估计也直接成为同一个 Airy 空间的估计，不再
留一个未比较的 $D_\pm^{1/2}$ 边界 norm。

同时，本篇逐项把参考负段的完整两行传播换到这同一端口单位，并
另付真正 raw 高度/flux mean。全部新增 shear 的真实无限层条件数
和小于 $2^{240000}\|X\|$。这支付的是具体的网络归一化，不宣称
已经反演其最终全局分母。

## 1. 原真实根、原 Airy 高度权和完整正段 DN

沿用[真实 positive transmission](R119-supplement-actual-positive-transmission-and-weighted-affine-source.md)
及[完整 Airy Cayley](R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md)
的同一实际端角、径向参考和物理尺度。
对正段端点 $e$，令

$$
 b_e=|A_t(t_e)|,\qquad\mu_e=(w_{\rm ref}/a)(t_e),\qquad
 \alpha_e=b_e\mu_e,
$$
$$
 \kappa=M/b_e,\quad
 \sigma_{e,m}=(1+\kappa^{4/3})^{1/2},\quad
 W_e=\sigma_{e,m}^{1/2},\qquad M=|m|.
 \tag{N.1}
$$

$m=0$ 时 $\sigma=W=1$。完整 raw DN 为
$S_m=\beta_m^{-1}(\alpha_m,-1;-1,\delta_m)$，
$D_-=(\alpha_m/\beta_m)_m$、$D_+=(\delta_m/\beta_m)_m$。
这些系数仍是实际径向 ODE 的准确值。

在向负区的根坐标 $x$ 中，已经证明的准确 germ 是

$$
 Q(x)=x+(14d_0-1/28)x^2-d_0x^3-7d_0^2x^4,
 \qquad 0<d_0<2^{-10}.
 \tag{N.2}
$$

正侧令 $z=-x=b_e|t-t_e|\ge0$。于是 $A(z)=-Q(-z)$，在
$0\le z\le1/128$ 上直接有

$$
                    0\le A(z)<2z.
 \tag{N.3}
$$

这个真实区间位于同一个 quartic germ 内，距离最近径向接缝远大于
它的长度。又 $(\log\mu_0)_t=A-1$、$b_e>2^{200}$，所以在该区间
$\mu_0/\mu_e<2$。两端分别用自己的向内正侧方向，不把右端法向号数
改成左端号数。

## 2. 一个实际径向 trial 支付所有频率的 DN 对角

取准确的频率依赖长度和 trial

$$
 d_m=\frac1{128\sigma_{e,m}},\qquad
 h_m(z)=(1-z/d_m)_+.
 \tag{N.4}
$$

它在当前端点为1，在其它端点为0，并在 (N.3) 的真实根 collar 内
截断。这个连续分片线性函数属于原完整能量空间，足以作为变分
竞争者；不把它当成一个额外的 PDE 解。

原能量准确为

$$
 \int\mu_0(|h_t|^2+A M^2|h|^2)dt
 \le2\alpha_e\left(\frac1{d_m}+\kappa^2d_m^2\right).
 \tag{N.5}
$$

此处角项直接用了 $A\le2z$ 和完整区间积分。因为
$\sigma_{e,m}^3\ge\kappa^2$，(N.5) 小于
$2\alpha_e\sigma_{e,m}(128+1/128^2)<2^9\alpha_e\sigma_{e,m}$。
径向 harmonic lift 的最小能量性质因而给全部 $m\in4\mathbb Z$

$$
 \boxed{\quad D_{e,m}<2^9\alpha_e\sigma_{e,m}.\quad}
 \tag{N.6}
$$

mean 也使用同一个 trial。特别 $D_{e,0}=R_I^{-1}$ 被保留，没有以
非zero频率的 Airy 渐近式替代这一行。

用原完整 Airy 归一

$$
 L_e=\alpha_e^{-1/2}W_e^{-1},\qquad
 P_0=L^*N_0L,\qquad \mathcal D_e=L_e^2D_e,
 \tag{N.7}
$$

立即得到 $0<\mathcal D_e<2^9I$。完整两端 $P_0$ 非负；对角
Cauchy–Schwarz 保留其真实非对角后给

$$
                         0\le P_0<2^{10}I.
 \tag{N.8}
$$

所以原 selfadjoint realization 在这个准确 Airy 空间中事实上是
有界的。共同常高度的核仍在完整双端空间内。

## 3. 实际更新的全部对角，及同一窗口中的 cross

前篇的真实 relative form 误差为 $\epsilon_I$，在复角条带 $1/8$
上也逐项支付。完整 Dirichlet lift 的准确 resolvent 比较给

$$
 \|P_a(z)-P_0\|_{L^2\to L^2}<2^{12}\epsilon_I,
                  \qquad |\operatorname{Im}z|\le1/16.
 \tag{N.9}
$$

这里先用原 form-dual 两侧半幂，再用 (N.8)，不是只比对角主符号。
实背景有 $P_a\ge0$、$\|P_a\|<2^{11}$。加上原 normal shear
$\|T_0\|<1/64$，完整 $R_a=P_a+T_0$ 的 norm 小于 $2^{12}$。

真角平移的有限差商与 Cauchy 给完整 commutator
$\operatorname{ad}_{\partial_\theta}^k(P_a-P_0)$；其 norm 小于
$2^{12}k!16^k\epsilon_I$。整数导数链、伴随和插值因而给安全的
共同窗口

$$
 \|P_a-P_0\|_{H^s\to H^s}<2^{60}\epsilon_I,
                                  \qquad -4\le s\le4.
 \tag{N.10}
$$

全部 mean/非mean 交叉项仍在这个完整算子内。

前篇 cross 估计使用 $\mathcal D_\pm^{1/2}$ 单位。由 (N.6)，两侧
半幂的乘积 norm 小于 $2^9$。因此对 $0\le r\le1/16$，实际有

$$
 \|e^{(r+\ell/2)|D|}P_{+-}(a)e^{-r|D|}\|_{2\to2}<2^{14},
$$
$$
 \|e^{(r+\ell/2)|D|}[P_{+-}(a)-P_{+-,0}]e^{-r|D|}\|
                                  <2^{25}\epsilon_I,
 \tag{N.11}
$$

以及反方向的同一估计。这里 $\ell$ 是每个实际正段自己的光学长度。
完整端角和真 normal 单位未改变。

为支付负 Sobolev 窗，输入侧指数权也须保留。取前篇准确变权形式
中的 $\rho(t)=-\ell/2+\tau(t)/2\le0$。其强制性完全相同。
对原 Dirichlet 解直接乘这个有界收缩权，准确弱恒等式给

$$
 \|[P_{-+}(a)-P_{-+,0}]e^{\ell|D|/2}\|_{2\to2}
                                      <2^{25}\epsilon_I.
 \tag{N.12}
$$

没有从输出增益直接断言输入增益。先在有限边界 Fourier 数据上用
真实弱解证明，再闭延拓该有界算子即可。

对复角平移 $|\operatorname{Im}z|\le1/32$，(N.11)–(N.12) 同样成立：
真实系数仍有足够条带支付全部卷积。因 $|D|$ 与角平移可交换，
四阶 Cauchy/伴随链现在给

$$
 \|e^{\ell|D|/2}[P_{+-}(a)-P_{+-,0}]\|_{H^s\to H^s}
                         <2^{64}\epsilon_I,\quad |s|\le4,
 \tag{N.13}
$$

并保留反方向及需要的输入权版本。各层两方向求和小于
$2^{385}\|X\|$。这已经是原 Airy 空间的真正指数传输合同；未倒除
尚未支付的另一半参考指数。

## 4. 原参考负段在同一完整 Airy 端口中的条件数

必须把负段的现有传播 norm 和 (N.7) 放在同一两个端口中。
原[完整全频参考定理](R119-supplement-uniform-frequency-reference-Airy-Cauchy.md)
在梯度两态

$$
 X_m=\sqrt\mu\operatorname{diag}(\sqrt\omega,\omega^{-1/2})
                      (im h,h_t)^T,
 \quad\omega_e=\varrho_j(1+M)^{-1/3},
 \quad\varrho_j=32(j+4)/\delta_j
 \tag{N.14}
$$

给 $K_j^{\rm grad}=2^{5000}(j+4)^5\delta_j^{-10}$。
对 $M\ge4$ 先乘共同标量 $M^{-1/2}$；径向参考逐模独立，所以这个
共同标量不改变其传播 norm。

从 $M^{-1/2}X_m$ 到本篇 $(Y_h,Y_p)$ 的准确变换，是一个对角矩阵
（另有模长1的 $i\operatorname{sgn}m$ 及法向方向号）和原完整 normal
shear。对角模长为 $r_{e,m},r_{e,m}^{-1}$，其中

$$
 r_{e,m}^2=\frac{b_e\sigma_{e,m}}{M\omega_e},\qquad
 \frac{b_e^{1/3}}{\varrho_j}
 \le r_{e,m}^2\le\frac{4b_e}{\varrho_j}.
 \tag{N.15}
$$

这里使用 $(1+M)/M\le5/4$ 和
$\max(1,x^{2/3})\le\sqrt{1+x^{4/3}}\le1+x^{2/3}$。
原真实根界给
$\delta_j^{-9/4}<b_e<2^{16}\sqrt{j+4}\delta_j^{-9/4}$，并有
$1<\varrho_j<b_e$。normal shear 的准确系数是
$\ell_{0,\xi}/(2\sigma_{e,m})$，其模小于 $1/64$。
所以每个变换及其逆的 norm 小于 $4\sqrt{b_e}$。

两个端点共同收费后，所有非zero模在本篇的完整 Airy 两态中满足

$$
 \|U_{0,I}\|_{H^s\to H^s},\ \|U_{0,I}^{-1}\|_{H^s\to H^s}
 <\mathcal K_j:=2^{5100}(j+4)^6\delta_j^{-13}.
 \tag{N.16}
$$

不能把原梯度框架的 mean 槽当成 raw 高度 mean。真正 mean 单独是
$p_t=0,h_t=p/\mu$。去掉两端已付 normal shear 后，它在
$(\sqrt{b_e\mu_e}h,p/\sqrt{b_e\mu_e})$ 中的对角为
$\sqrt{b_+\mu_+/(b_-\mu_-)}$ 及其倒数，交叉项为
$\sqrt{b_+b_-\mu_+\mu_-}\int_I\mu^{-1}dt$。
消费实际

$$
 \mu_{\max}/\mu_{\min}<2^{272}\delta_j^{-2},\qquad |I|<4\delta_j
$$

后，其完整两行 norm 小于 $2^{160}(j+4)\delta_j^{-3}$，严格落在
(N.16) 内。因此 (N.16) 包括真正 mean 高度和通量，不只包括人工
梯度常数槽。

## 5. 精确移出 DN 对角差：真实网络的新两行

记完整对角差 $\Delta_e=(P_a-P_0)_{ee}$。在每个正段端点采用
准确变换

$$
 \widetilde Y_h=Y_h,\qquad
 \widetilde Y_p=Y_p-\Delta_eY_h,
 \qquad
 \mathsf S_e=\begin{pmatrix}I&0\\-\Delta_e&I\end{pmatrix}.
 \tag{N.17}
$$

实背景下 $\Delta_e$ 自伴，所以这是完整 symplectic shear。
其逆准确把负号改成正号；不是一个只到一阶的坐标替代。
(N.10) 给 $\|\mathsf S_e-I\|_{H^s}<2^{60}\epsilon_I$。

原真实正段关系因此准确成为

$$
 \begin{aligned}
 \widetilde Y_{p,-}&=(P_{0,--}+T_{0,-})Y_{h,-}
                         +P_{a,-+}Y_{h,+}+q_-,\\
 \widetilde Y_{p,+}&=P_{a,+-}Y_{h,-}
                         +(P_{0,++}+T_{0,+})Y_{h,+}+q_+.
 \end{aligned}                                            \tag{N.18}
$$

两端参考对角现在完全相同，实际全部 cross 和 sourced flux 仍原样存在。
整个推导没有使用 $P_{0,+-}^{-1}$。

若负段使用共同向 $t$ 增大的 flux 方向，在相应端先用准确
$J_e=\operatorname{diag}(1,\varsigma_e)$ 转换 (N.17)。这些符号矩阵
norm 为1。对任何真实完整负段关系 $Y_+=U_aY_-+s$，准确有

$$
 \widetilde Y_+=\mathsf S_+U_a\mathsf S_-^{-1}\widetilde Y_-
                                      +\mathsf S_+s.
 \tag{N.19}
$$

特别，比较时必须保留

$$
 \mathsf S_+U_a\mathsf S_-^{-1}-U_0
 =\mathsf S_+(U_a-U_0)\mathsf S_-^{-1}
      +[\mathsf S_+U_0\mathsf S_-^{-1}-U_0].
 \tag{N.20}
$$

第一项仍是原先要支付的实际两支传播及其相位误差。本篇并未把它删除。
第二项是真正新增的 DN 对角 shear，在参考 interaction picture 中
至多为 $3\mathcal K_j^2$ 乘两端的 (N.10) 误差和。

## 6. 新增 shear 的实际全层账

真实 $N_j$ 的三段准确式为

$$
 N_j=\begin{cases}
 2^{184}(9/100)^{-5}\delta_j^{7/4},&129\le j\le4096,\\
 2^{169}\delta_{4096}^{-3/2}\delta_j^{827/256},&4096<j\le8192,\\
 2^{169}\delta_{4096}^{-3/2}\delta_{8192}^{-485/4}
                     \delta_j^{31867/256},&j>8192.
 \end{cases}                                              \tag{N.21}
$$

各段起点和段内单调性给全部 $N_j<1$。保留真实
$\mathcal M_j=\sum_{|r-j|\le2}N_r$、(N.16) 与
$\epsilon_I=2^{104}(j+5)^2\mathcal M_j\delta_j^{-3/2}\|X\|$。
端点可属于相邻一层；用邻层的 $\delta$、$j$ 比及全部至多四次计数，
一个安全共同包络是

$$
 2^{10400}(j+5)^{14}\delta_j^{-55/2}\mathcal M_j\|X\|.
 \tag{N.22}
$$

对于 $j\le8195$，$j+5\le8200<2^{14}$、
$\delta_j>2^{-(j+4)}$、$\mathcal M_j<5$，每项的二进制对数小于
$10400+196+3+(55/2)8199<236100$。
整个有限前缀少于 $2^{14}$ 项。

从 $j=8195$ 起，$\mathcal M_{j+1}/\mathcal M_j=2^{-31867/256}$
是准确值，所有五个相邻层都已在同一真深规范内。故 (N.22) 的后续
比小于 $1/2$，真实整个无限尾小于首项的两倍。于是

$$
 \boxed{\quad
 \sum_{\rm negative\ components}
 \|\text{新增 DN diagonal shear 的完整 interaction 误差}\|
 <2^{240000}\|X\|\le2^{-22144}.
 \quad}                                                   \tag{N.23}
$$

这同时保留有限前缀与两个全局规范因子。实际 incoming/Newton 链的
$X$ 远更小，但 (N.23) 已在原 $2^{-262144}$ 工作球中成立。

## 7. 源、mean 和随标签变动的 frame 项

正段的完整 affine $q$ 在 (N.18) 中保留；负段 source 两行按
(N.19) 整体乘 $\mathsf S_+$。其中新 flux 项
$-\Delta_+s_h$ 不能删去。
前篇的加权源量 $\mathcal S_\rho$ 和 (N.6) 还直接给同一 Airy 单位
中的两端输出界 $\|W_\partial q\|<2^9\mathcal S_\rho$。
ordinary 密度、两 weak 分量、真实 source 支集和两个 bare weak flux
端迹仍采用前篇的完整合同。

当前 shear 也依赖标签及实际参数。微分时准确有

$$
 \delta\widetilde Y=\mathsf S_e\delta Y
                         +(0,-(\delta\Delta_e)Y_h)^T.
 \tag{N.24}
$$

由 (N.10) 的算子值全纯性、$\sum\epsilon_I<2^{320}\|X\|$ 和
$\|X\|<16\|a_{\rm lab}\|$，在 $\|a_{\rm lab}\|<A_*/2$ 上可安全取
$\sum_e\|D\Delta_e\|<2^{386}$：先对两端之和取
$2^{385}\|a_{\rm lab}\|$ 的界，再用半径 $A_*/2$ 的 Cauchy 圆盘。
因此 (N.24) 是一个已明确有界的端口 source 列；若以更强网络 norm
消费，仍须把真实 $Y_h$ 的对应 norm 一起输入。

mean 并不在 shear 后自动保持原来的数值。原 raw 总 outward flux
准确由

$$
 p_e^{\rm tot}=L_e^{-1}
       (\widetilde Y_{p,e}+\Delta_eY_{h,e}-T_{0,e}Y_{h,e})
 \tag{N.25}
$$

恢复。这里 $Y_p$ 按前篇使用 total flux；若需要 bare flux，则另减
真实的 weak endpoint charge。完整积分 mean
条件必须对 (N.25) 使用。实际 $\Delta_e$ 可混合 mean 与非mean，
不能把 $\widetilde Y_{p,e}$ 的 mean 单独设为0。
共同常高度解也由同一个准确 shear 变换，而非在新端口中假装仍有
零 flux。

## 8. 仍需继续的全局消元

本篇给同一实际 Airy 空间中的全部正段对角、真实 cross、负段完整
参考传播、新增 shear 的无限层费用，以及所有 mean/source 变换。
这使全网络可以使用 (N.18) 的参考对角作稳定消元，而不用在局部
反演指数小 cross。

最后仍须证明这个 paired-port 网络的整体参考逆与真实内部标签
$\mathcal X_{224}$ 及外部 Schur 行的准确关系，并消费 (N.20) 中
尚未合并的真实传播项。局部和 (N.23) 小，不自动支付全局最终
分母或恢复已经用掉的角宽。本文不以此把94步有限链称为完整解。

`scripts/fourfold_Airy_DN_diagonal_network_20261113.py` 与
`notes/2026-11-13-R119-Airy-DN-diagonal-network-budget.json`
记录以上实际根 trial、完整 mean、两端变换和无限层预算。
