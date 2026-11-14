# R119 续篇：新外两根的完整强散射、真实首相位及全源

2026-11-14，visible-exact / tail_connector。

**状态：解析证明。** 对新 fixed-stop simple-root 对象的完整外负片
$I_o=[e_X,e_0]$，本篇支付从两端真实 Airy 波到完整负散射的两个强窗口，
并识别包含新根和新增平台的完整首密度相位。强 Hilbert 算子界和酉性在实控制、实非径向背景上成立，Jacobi 数据可为复数；标量相位及其差另在明列复参数域延拓。全部低频、两个 mean、
两个 Fourier 锥和真实 root graph 都保留。新 $e_0$ 的输入逐条来自新根
A.1--A.28；不把旧 quartic 的形状或大斜率假设赋给新根。

记 $g=4/3$，固定有限尺度
$$
 \Lambda_o=2^{2048},\qquad L_o=2^{6000}\Lambda_o=2^{8048}.
 \tag{F.1}
$$
在原物理 $m\in4\mathbb Z$ Sobolev 权和原共同 Airy Wronskian 单位上，
真实双端散射 $S_o$ 与第6节的明确酉模型 $S_o^{(1)}$ 满足
$$
 \boxed{\quad
 S_o\text{ 满射且酉},\qquad
 \|S_o-S_o^{(1)}:H^0\to H^{g}\|,
 \ \|S_o-S_o^{(1)}:H^{-g}\to H^0\|<2^{12000}.
 \quad}
 \tag{F.2}
$$
这里每个 $H^s$ 都含两端波及其完整 mean。完整 Cauchy 传递和反向传递
另有明确正定 norm 界 $2^{32768}$，不是由 $J$-unitarity 猜得。

## 1. 实际对象、真实切口及已付前置

使用 [新外 principal 与无限联立 KAM](R119-supplement-new-outer-two-root-complete-principal-return-and-joint-KAM.md)
的同一个完整图、固定参数、两根和所有控制，记为 O。
使用 [新根解析图](R119-supplement-new-fixed-stop-simple-root-full-analytic-chart-and-sources.md)
记为 A；[新 positive DN](R119-supplement-new-simple-root-complete-positive-DN-Airy-return-and-sources.md)
记为 P。取
$$
 \mathcal X=16\|a\|_{224}\le2^{-262144},\qquad
 n=2^{-12}\mathcal X,\qquad n_0=2^{-447}\mathcal X .
 \tag{F.3}
$$
实际最终工作球更小，$\mathcal X\le2^{-8388608}$。
全部先前内部片保持原定理；本篇只重付新外片。

两根分别取自己的准确径向 Liouville 坐标 $\xi_{0,e}$，以
$\xi_{0,e}=H=1/64$ 定义原物理 $t$ 的 fixed strict cuts。
新根由 A.5--A.7 有 $Q>1/128$ 于该切口。
左根沿用其已付真切口。实际非径向 constant-$\xi$ 截面与这些 fixed-$t$
截面的差由第5节真实图连接，不能将二者视为同一截面。

## 2. 有限外 strict 片的真实径向账

在两 fixed cuts 之间，S 的新平台与 quintic、旧第129胞实际 profile
共同给
$$
 Q>2^{-7},\quad \sqrt Q>2^{-4},\quad
 Q<2^{220},\quad |Q_t|<2^{425},\quad
 |Q_{tt}|<2^{640},\quad |Q_{ttt}|<2^{850}.
 \tag{F.4}
$$
后三者按真实光滑片取值，$Q,Q_t$ 连续，$Q_{tt}$ 的有限跳全部保留。
旧段的前三门是受控全图 C.15 的
$2^{12}(j+4)\delta^{-3/2}$、$2^{18}(j+4)\delta^{-3}$、
$2^{26}(j+4)\delta^{-9/2}$，代 $j=129,\delta^{-1}<2^{133}$；
第三径向导用受控联立 N.4 的 $2^{40}(j+5)\delta^{-6}$。
新增 quintic 上 $\eta=2^{-24}$，$Q$ 是 $10S-3$，其前三导分别
小于 $2^{29},2^{54},2^{82}$，均在 (F.4) 内。常平台导数为0。

O.4--O.7 已支付完整
$$
 |I_*|<2,\qquad
 \int_{I_*}(1+Q)\,dt<282\log2,\qquad
 \int_{I_*}\sqrt Q\,dt<2^9 .
 \tag{F.5}
$$
第一门也可直接由旧 $t=\log r$ 段长 $\le\log2$、
新平台 $<1/12$ 和新过渡 $<2^{-24}$ 得到。

旧下降坡两个 bump 与浅形状均留在原严格单调子段，峰点及其邻域未动。
旧 X.5 的三段单调变差门再加新根负翼 $7\to Q(t_{*,0})$，给
$$
 \operatorname{TV}_{I_*}(\log Q)<704\log2 .
 \tag{F.6}
$$
旧片少于32个真实光滑片，加新平台和 quintic 后仍少于64片。
新增 $C^4$ 零延拓不制造额外 $Q_{tt}$ 原子；原两个 $C^2$ bump 的原子照计。

完整径向 wave 势是
$$
 V_w={Q_t\over2Q}-{(1+Q)^2\over4Q}
             +{5Q_t^2\over16Q^3}-{Q_{tt}\over4Q^2}.
 \tag{F.7}
$$
这里允许直接使用有限外片的上确界乘真实长度，不声称仍有旧的
$|I|<4\delta_{129}$。代 (F.4)，四项分别小于
$2^{432},2^{449},2^{871},2^{654}$，因此
$$
 \|V_w\|_\infty<2^{873},\qquad
 I_1:=\int |V_w|\sqrt Q\,dt<2^{985}<\Lambda_o .
 \tag{F.8}
$$
完整光滑片导数准确为
$$
 (V_w)_t={Q_{tt}\over2Q}-{Q_t^2\over2Q^2}
 -{1-Q^{-2}\over4}Q_t+{9Q_tQ_{tt}\over8Q^3}
 -{15Q_t^3\over16Q^4}-{Q_{ttt}\over4Q^2}.
 \tag{F.9}
$$
其六项共同和小于 $2^{1306}$：最大项 $Q_t^3Q^{-4}$ 的 bits 是
$3\cdot425+4\cdot7=1303$，其余项严格更小。
乘长度 $<2$，再加每个实际 seam 两侧的 $-Q_{tt}/(4Q^2)$，
得到
$$
 I_2:=\|V_w\|_\infty+\operatorname{Var}V_w
                         <2^{1310}<\Lambda_o^2 .
 \tag{F.10}
$$
真实 optical 时间 $\int\sqrt Q\,dt$ 单调，所以不改变总变差。
(F.8)--(F.10) 是新外片自己的门；未转授旧短坡反应项的尺度。

## 3. 完整 strict 同空间比较：mean 也重付

使用 [准确 strict 密度系统](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)
S.5--S.21 的完全相同定义：
$$
 \Lambda=\mu\nu={w_{\rm ref}\over a}{\sqrt Q\over\mathfrak d},
 \quad w=\sqrt\Lambda\,h,\quad
 y_\sigma=(w_\theta+\sigma\zeta)/2,\quad
 X_\sigma=\mathcal D_{H_\sigma}y_\sigma,
$$
$$
 \alpha=\langle X_+\rangle=-\langle X_-\rangle,\quad
 Z_\sigma=X_\sigma-\sigma\alpha,\qquad
 w=c+\alpha(S_+-S_-)-i\sum_\sigma C_{S_\sigma}D_\theta^{-1}Z_\sigma .
 \tag{F.11}
$$
$D_\theta^{-1}$ 在 mean 上为0；独立的 $c,\alpha$ 留在状态中。
采用完整平衡空间
$$
 \mathcal W_r=\mathbb C^2\oplus(H^r_0)^2,\qquad
 Y=(c,\alpha,|D_\theta|^{-1/2}Z_+,
                         |D_\theta|^{-1/2}Z_-).
 \tag{F.12}
$$
原真实物理高度和通量 mean 一般不是 $c,2\alpha$。

把完整固定标签 generator 记为 $\mathcal A$，同参数径向参考记为
$\mathcal A_0$。严格密度 S.12 的准确势差和 S.21 的
$\mathcal A=L_HB_HR_H$ 不含“内部长度”假设，因而可逐项重用。
本篇重付其数值如下。置
$$
 W=1+(1+Q)^2/q+|Q_t|/q+Q_t^2/q^5+|Q_{tt}|/q^3,\qquad q=\sqrt Q .
$$
(F.4) 给 $W<2^{872}$；原准确展开逐项给
$$
 \|\kappa-\kappa_0\|_{\mathcal A_1}<2^{64}nW,\qquad
 \kappa_0=qV_w,\qquad
 \int\|\kappa-\kappa_0\|_{\mathcal A_1}<2^{937}n,\quad
 \int|\kappa_0|<2^{985}.
 \tag{F.13}
$$
原完整状态方程支付所需径向 jets，完全包括 true $K_0$ 和
$\mathfrak d_t-d\mathfrak d_\theta$；没有只比较非mean方程。

O.17--O.19 的流以及一次角域 Cauchy 给真实流、逆流相对其径向
平移的完整 $C^8$ 差小于 $2^{64}n$。
现在 $|S_+-S_-|<2^{11}$，替代旧 strict 证明中的 $<2$。
原 $R_H,L_H$ 的上界 $2^{22}$ 仍足够，径向参考二者取 $2^{12}$。
故原 S.20 的真实一次积分消导数和 S.22 的有序三项展开，
包括此处参考两算子的额外因子后，安全地给
$$
 \|\mathcal A-\mathcal A_0\|
 <2^{128}\bigl(\|\kappa-\kappa_0\|_{\mathcal A_1}
                                  +2^{64}n|\kappa_0|\bigr).
$$
半阶平衡以及 mean 的完整解析入列、出列再付 $2^{40}$，
于是对于所需 $|r|\le3$，
$$
 \int\|\mathcal A-\mathcal A_0\|_{\mathcal W_r\to\mathcal W_r}
                                  <E_o:=2^{1280}n .
 \tag{F.14}
$$
这是完整 generator 差；没有把裸 $C_H-C_{H_0}$ 误作同阶小算子。

径向参考条件数也重新计。非mean先用
$(\sqrt{\mu_0q}\,h_\theta,p/\sqrt{\mu_0q})$ 的对称 principal 能量；
其双向 norm 至多
$$
 \exp\left(\frac12\int(1+Q)dt
               +\frac14\operatorname{TV}\log Q\right)<2^{317}.
$$
准确 density shear 为 $\ell_{0,t}/(2q)$，且
$|\ell_{0,t}|<2^{432}$，所以每端转换及逆小于 $2^{436}$。
角实平移不改变 Sobolev norm。因此完整非zero模参考界小于 $2^{1200}$。

mean 使用准确三角矩阵
$$
 \begin{pmatrix}
  \sqrt{\Lambda_0(t)/\Lambda_0(s)}&
  \sqrt{\Lambda_0(t)\Lambda_0(s)}
                     \displaystyle\int_s^t\mu_0^{-1}d\tau\\
  0&\sqrt{\Lambda_0(s)/\Lambda_0(t)}
 \end{pmatrix}
 \tag{F.15}
$$
作用于 $(\sqrt{\Lambda_0}h,p/\sqrt{\Lambda_0})$。
由 (F.4)--(F.5)，$\mu_0$ 双向比例 $<2^{282}$、
$q$ 比例 $<2^{114}$，所以两对角项 $<2^{198}$，
非对角项 $<2^{394}$。每端同一个 density shear 至多 $2^{436}$；
再从 $w,\zeta$ 到 $c,\alpha$ 的两端费用各小于 $2^{12}$，
因为真实 optical 长度 $<512$。所有 mean 的双向费用小于 $2^{1300}$。
于是所有频率共同可取
$$
 \|U_0(t,s)\|<2^{1400},\qquad
 \eta_o\le2^{2800}E_o<2^{4080}n,\qquad
 \|U_{\rm st}(t,s)^{\pm1}\|<G_o:=2^{1536}.
 \tag{F.16}
$$
实际 $\eta_o\ll1$。这一次先付完整径向条件数，再以准确 interaction
积分得到实际界，不指数化一个含大径向势的绝对粗界。

## 4. strict 的真正高输出、二阶余项与全部低输入

以下消费 [strict 高输出证明](R119-supplement-complete-strict-high-output-in-root-slope-units.md)
的准确有序恒等式，重新列出每个数值输入。

由 (F.8)--(F.10)，径向高频波能量在 $M\ge2^{1024}\Lambda_o$
小于 $4/3$。用同一个完整 (F.14)、(F.16) 作 Duhamel，
新增项至多 $(4/3)E_oG_o<2^{2817}n<1/16$，所以
$$
 \|P_{\ge M}U_{\rm st}(t,s):\mathcal W_r\to\mathcal W_r\|<2,
       \quad M\ge2^{1024}\Lambda_o,\quad |r|\le3 .
 \tag{F.17}
$$
输入为全空间，包含 mean。

跨支原函数仍为 strict 原证明的
$K_{\rm cross}=\partial_t\mathcal L-\mathcal Z$，
其系数 $R=\kappa/\nu$ 的径向值准确是 $V_w$。
非径向的有限系数和 BV 差可以在本片直接支付：
$$
 \begin{array}{c|c}
 \text{量，未额外取角导}&\text{上界}\\ \hline
 |\ell_{0,t}|,\ |\ell_{0,tt}|,\ |\ell_{0,ttt}|
                         &2^{432},\ 2^{865},\ 2^{1298}\\
 \text{前三阶状态差的原全商式}
                         &2^{920}n\\
 |\kappa-\kappa_0|&2^{936}n\\
 |\partial_t(\kappa-\kappa_0)|,\
             |R-V_w|+|\partial_t(R-V_w)|&2^{2400}n
 \end{array}
 \tag{F.18}
$$
前三阶状态行由原 strict S.9 的完整方程逐次微分：
第三阶的宽界为
$2^{256}[(1+Q)^3+(1+Q)|Q_t|+|Q_{tt}|]n$。
对 S.12 的准确差式微分只再用 $Q_{ttt}$。
最大的径向参考乘积是
$Q_t^3Q^{-3}$、$Q_tQ_{tt}Q^{-2}$ 和
$(Q^{-1/2})_{tt}\ell_{0,t}$，其 bits 分别小于
$1296,1079,1302$。分母 $J_0,\mathfrak d,v$ 及所需导数由同一
状态商式支付；$q^{-1}<16$。把有限乘积及其和统一放宽到
$2^{2400}n$ 有超过九百位余量，不依赖未给的第五径向导。

再取至多8阶角导，其一次 Cauchy 费小于
$8!256^8<2^{80}$；两轮有限乘积和逆函数链式的系数和各小于
$2^{64}$。真实流 Jacobian/逆的差已由 $2^{64}n$ 给出。
乘 $|I_*|<2$ 和全部少于64片的两侧 seam 迹，仍小于
$2^{4096}n$。这支付 $\mathcal L,\mathcal Z$ 的全部非径向系数，
而非两个不同 FIO 的裸同阶差。径向部分由 (F.8)--(F.10) 支付。

因此在所需两个输出阶窗可沿原证明取
$$
 \int\|K_{\rm all,nonmean}:H^r\to H^{r+1}\|<2^{512}\Lambda_o,
$$
$$
 \sup\|\mathcal L:H^r\to H^{r+2}\|
       +\int\|\mathcal Z:H^r\to H^{r+2}\|<2^{768}\Lambda_o^2 .
 \tag{F.19}
$$
两个 mean 的全部有限行列保留在 $K_{\rm sm}$，没有用
$D^{-1}$ 作用于零模。其角非mean部分带上述 $n$；
mean-only块可以大于1，但在高输出下准确为0。

两支角图是实平移加已付解析小量，导数离1小于 $1/4$。
所以原 strict S.22--S.24 的真实 contour 和双 Schur 和继续给
四倍隔带门
$2^{1024}C_T e^{-M/2^{14}}$。
这里大的实 optical 平移只乘模长1的 Fourier 因子，
不会使隔带估计多付 $e^{512M}$。
真实同支 phase 的径向大平均也先准确移走；
余下角非mean及其所需 commutator 由 (F.18) 的小量给出，
其复角演化 norm 小于2。

在完整有序 Duhamel 中插固定 cuts
$L_{\rm st}/4,L_{\rm st}/16,L_{\rm st}/64,L_{\rm st}/256$，
$L_{\rm st}=2^{4200}\Lambda_o$，按原 S.25 的真实次序消费。
所有高输入演化都由 (F.17) 付2；每个低输入项必有一个已付隔带。
同时 $G_o<2^{1024}\Lambda_o^6$，
$e^{-L_{\rm st}/2^{20}}\le32!(2^{20}/L_{\rm st})^{32}$。
原端项、$\mathcal Z$、三个 $\mathcal LK$、同支二次项及低输入项
于是分别落在原显示预算，给
$$
 \|P_{\ge L_{\rm st}}(U_{\rm st}-e^{B_{\rm st}}):
                 \mathcal W_s\to\mathcal W_{s+2}\|
                              <2^{2048}\Lambda_o^2 .
$$
与同阶差 $<4$ 在输出 Hilbert 标度插值：
$$
 \boxed{\quad
 \|P_{\ge L_{\rm st}}(U_{\rm st}-e^{B_{\rm st}}):
              \mathcal W_s\to\mathcal W_{s+g}\|
                         <2^{1400}\Lambda_o^g,\quad |s|\le1 .
 \quad}
 \tag{F.20}
$$
反向同样成立。这保留整个输出频带，未用 shell supremum 代替强范数。

## 5. 新 simple 根及其真实 graph，逐项核入口

左根仍是原完整实际根。右根 A 给
$b_0\in(2^{28},2^{29})$、$|V_0|<1$ 于 $|\xi|\le1/4$，
以及实际 $|V-V_0|<2^{36}n_0$ 于
$|\xi|\le1/32,|\operatorname{Im}\phi|\le1/2$。
所以在 $0\le\xi\le H$ 所需复邻域，
$$
 |V|<17,\quad |V_\xi|<129,\quad
 b_0>1,\quad \|M_{V-V_0}:H^r\to H^r\|<2^{52}n_{e,0},
 \qquad n_{e,0}:=2^{64}n_0 .
 \tag{F.21}
$$
径向导门可直接用 $V_0$ 的半径 $1/4$ 和实际差的余宽 $1/64$；
没有使用旧根多项式。
A.21--A.22 的全频、含 mean 根能量给同一 $K_R=2^{2184}$。
原自由 Airy 到 balanced $Y$ 的两个 $2^{16}b^{1/3}$ 门于是给
完整 interaction $\|U_e^{\pm1}\|<2^{2217}b_e^{2/3}$。

[根高输出 Volterra](R119-supplement-root-high-output-Volterra-without-low-frequency-condition-number.md)
V.3--V.7 的全部输入因此重获：原完整 Wronskian、
$|V_l|\le17e^{-|l|/128}$、全 lag/mean kernel 和同空间 interaction 门。
其双 buffer 与频带双 Schur 证明只要求 $b>1$，
所以在新右根同样给全输入高输出门2。
[完整 root first phase](R119-supplement-complete-root-first-phase-in-slope-units.md)
F.3--F.16 只再用 $V_\xi$，给
$$
 \|P_{\ge2^{4200}b_e}(U_e-e^{B_e}):
                      H^s\to H^{s+g}\|<2^{4098}b_e^g .
 \tag{F.22}
$$
其两个 mean 始终使用原 $c(1\pm i\xi/\pi)$，未代入 $m^{-1}$。

新 fixed-$t$ graph 准确定义为
$g(\phi)=\xi(x_*,H^{-1}(\phi))$、$H(\theta)=\phi(x_*,\theta)$。
A.15--A.16 给
$|g-H|<2^{14}n_0$ 于角宽1，
$|H-\mathrm{id}|<2^{10}n_0/b_0$ 及其真逆。
这些门、(F.21) 及 $b_0^2n_{e,0}\le2^{-512}$，逐条强于
[完整二阶根图](R119-supplement-complete-root-graph-two-order-slope-budget.md)
G.2、G.14 的输入；$g_s$ 始终在 $H/2<g_s<2H$。
特别右根所用八阶角费由实际宽1及宽1/2分别支付，
$n_{e,0}=2^{64}n_0$ 显式覆盖 A 的缩域损失。
故该篇 G.5--G.21 的准确完整两 mean 方程、跨支原函数、
有序 Duhamel 和插值给新根 graph 的强门
$2^{700}b_0^g$ 与完整同阶正逆门4。

左根取其原受控状态界，安全宽放为 $n$；$b_X<2^{336}$。
两根都有 $b_e<\Lambda_o$，且当前球使各自 $b_e^2n_e$
远小于 $2^{-512}$。自由两行端架在两根均严格使用
[完整 free frame 勘误](R119-supplement-complete-free-Airy-two-row-frame-and-low-frequency-erratum.md)
的 $2^{64}b_e$ 同阶门和 $2^{64}b_e^g$ 强余项，
不恢复旧的低非mean $b_e^{1/2}$ 错界。

## 6. 完整 ordered word，而非相乘局部高输出界

从左至右依次取左 root interaction、自由端架、真 graph、
完整 strict、右 graph inverse、右自由端架 inverse、
右 root interaction inverse 和真方向交换。
将 principal 恢复另列，因素总数不超过12。
真实乘积记为 $T=A_N\cdots A_1$。

模型 $M=M_N\cdots M_1$ 与
[完整负 scattering 的有序证明](R119-supplement-complete-negative-scattering-and-network-word-in-slope-units.md)
W.4--W.6 一样定义：root/graph/strict 用准确同支首 phase exponent，
自由架保两 $\pi/4$ 及 $-5b_e/(48H^{3/2}M)$，
角图用真实 signed-density 的 polar unitary。
模型的两个 mean 取独立恒等块，右根仍作交换；
实际 mean-only变化完整留在误差。于是
$$
 M=\begin{pmatrix}0&M_B\\M_C&0\end{pmatrix},\qquad
 S_o^{(1)}=\begin{pmatrix}0&M_B^*\\M_C&0\end{pmatrix}
 \tag{F.23}
$$
都按原波 Green 单位定义，$M_B,M_C$ 满射且酉。

为明确旧 word 证明的每个入口，这里列出新有限外片的对应账：

| 实际输入 | 本片已经证明的门 |
|---|---:|
| 两根全频 interaction | $2^{2217}\Lambda_o^{2/3}$ |
| 每个真实自由架及逆 | $2^{64}\Lambda_o$ |
| 每个 graph 与恢复 | 原非mean门4；新增 mean-only因子小于 $2^{12}$ |
| strict 完整双向 | $G_o=2^{1536}$ |
| strict 完整 generator 差 | $E_o=2^{1280}n$ |
| strict 与同参数径向之绝对差 | $\epsilon_{\rm st}<2^{4356}n$ |
| 实际单根 incoming 前缀 | $2^{2300}\Lambda_o^{5/3}$ |
| 任意完整实际连续子乘积及逆 | $G_{\rm all}=2^{8192}\Lambda_o^{12}=2^{32768}$ |

绝对差行由准确全空间 Duhamel 的 $G_o^2E_o$、
同支 exponent 的同一差及固定有限因子取得。
新增较长 optical mean 恢复只在表中收费，未沿用旧 $<1/8$ optical 长度。

root 远带由实际复角势族和完整两行 kernel 得
$2^{2300}\Lambda_o e^{-M/2^{12}}$；
graph 的全路径求和仍给 $2^{1024}e^{-M/2^{14}}$。
principal 角图及首相位同调所需的26阶角门可统一记为
$$
                     \epsilon_o^c=2^{32768}\mathcal X .
 \tag{F.24}
$$
这里是有限外片的显式宽放：原流 $C^8$ 门为 $2^{64}n$，
继续取26阶只增加 $26!256^{26}<2^{300}$；
O.24--O.28 的 KAM 共轭取同一角余宽后小于 $2^{768}\mathcal X$。
有限密度系数与其径向首相位至多由 (F.18)--(F.19) 收
$2^{4096}\Lambda_o^2$，二十阶 signed/polar 与有限链式法则再收
$2^{4096}$。这些指数的和严格小于32768。
由完整 signed-Green 恒等式，跨锥及 polar 差有
$H^0\to H^{20}$ 与 adjoint 的 $2^{4096}\epsilon_o^c$ 门。
mean--nonmean列使用同一解析 Fourier 尾；mean-only块单独保留。
并且
$$
 \Lambda_o\epsilon_o^c<2^{34816}\mathcal X\ll1 .
 \tag{F.25}
$$
所以大径向首相位先移走后，真正复角同支族的 norm 小于2。
没有把“角图很小”当成裸同宽 pullback 差。

唯一 strict 因素前只乘真实单根前缀。上述表给
$$
 \epsilon_{\rm st}\|A_{\rm in}\|<2^{10080}\mathcal X
                                                    <2^{-252064}.
 \tag{F.26}
$$
对 $M\le L_o$，再付低输入 $\langle M/4\rangle^{g}$，
仍小于 $2^{21000}\mathcal X<2^{-241144}$。
这支付完整 mean 输入和全部低输入进入 strict 后的高输出，
不是把它们删掉。

因此可逐字执行原 W.27--W.34 的有限 buffered telescoping：
所有阈值在 $[2^{-100}L_o,L_o]$ 内，均超过每个根/strict 的
$2^{4200}\Lambda_o$；实际高输出前缀每步只收16及已付泄漏，
总门 $2^{64}$。准确恒等式
$$
 T-M=\sum_{k=1}^N M_N\cdots M_{k+1}(A_k-M_k)A_{k-1}\cdots A_1
 \tag{F.27}
$$
始终左模型、右实际前缀。各局部 strong 项由
(F.20)、(F.22) 和 graph/free 门支付；所有低频穿越左模型的项
由真隔带支付。最坏多项式泄漏仍小于
$2^{20000}\Lambda_o^{12}(2^{-100}L_o)^{g-20}$。
于是正反两方向均有
$$
 \|P_{\ge L_o}(T-M):H^0\to H^g\|,
 \ \|P_{\ge L_o}(T^{-1}-M^{-1}):H^0\to H^g\|
                                 <2^{6000}\Lambda_o^g .
 \tag{F.28}
$$
没有用单个高输出门相乘来取代全输入证明。

## 7. 准确全空间散射与所有中间频率

原物理 Green 配对、两个共同 Wronskian 和右根法向给
$$
 T^*\mathsf JT=-\mathsf J,\quad T\mathsf JT^*=-\mathsf J,
 \quad T^*=-\mathsf JT^{-1}\mathsf J .
 \tag{F.29}
$$
完整 onto 性来自已付 Cauchy inverse，包括 mean。
若 $T=(A,B;C,D)$，则 $B^{-1},C^{-1}$ 为全空间 contraction；
$$
 S_o=\begin{pmatrix}
 -B^{-1}A&B^{-1}\\
 C-DB^{-1}A&DB^{-1}
 \end{pmatrix}.
 \tag{F.30}
$$
正反解均存在，故 $S_o$ 满射且酉。

原 W.38 的四个准确块恒等式，配合 (F.28) 和其 adjoint，
只在最右乘 contraction 或真实散射块，
给高输出误差及其 adjoint $<3\cdot2^{6000}\Lambda_o^g$。
最后才用真正酉性支付全部低输出：
$$
 \|P_{<L_o}(S_o-S_o^{(1)}):H^0\to H^g\|
                \le2\langle L_o\rangle^g<4L_o^g .
$$
两个基础窗的共同门因此小于
$2^{9000}\Lambda_o^g<2^{12000}$，即 (F.2)。
全部 $|m|<L_o$ 都通过实际 full scattering 支付，
不要求它们落入某个低 incoming cone。

## 8. 新根确实进入完整首相位

定义真实密度
$$
 \kappa={P(\Lambda^{-1/2})\over\Lambda^{1/2}},
 \qquad
 \Lambda=\sqrt{-\det G},
$$
等价于严格密度 S.7 的完整式。令 $\Omega_\epsilon$ 删除两根的
$0<\xi_e<\epsilon$，定义
$$
 \mathfrak b_o(a,\Gamma,\Xi)=
 \lim_{\epsilon\downarrow0}
 \left[\frac12\int_{\Omega_\epsilon}
       \kappa\,dt\,{d\theta\over\pi/2}
          -\sum_{e=X,0}{5b_e\over48\epsilon^{3/2}}\right],
 \qquad \beta_o=-\mathfrak b_o/2 .
 \tag{F.31}
$$
该分母形式与 $\kappa=(P(m_0)/m_0)/\Lambda$、
$m_0=\Lambda^{-1/2}$ 完全相同。

[完整非径向首相位](R119-supplement-actual-nonradial-first-density-phase.md)
B.7--B.18 的识别是准确代数：
Piola 下 $\kappa\,dt\,d\theta$ 不变，height 共轭不改变 $\kappa$；
每个 canonical 根准确给
$$
 \kappa_c=b_e\left({5\over16\xi^{5/2}}+{V_e\over\sqrt\xi}\right).
$$
所以 (F.31) 存在；两端 finite part 与实际 graph 区域完全匹配。
同支真实密度流的 Jacobian 使首系数平均恰为
$\frac12\int\langle\kappa\rangle dt$。
跨支及反号锥余项已由本篇完整 strong 门支付，mean 与低模均为
保留的有限/平滑列，不会贡献一个隐藏的非zero频 $1/M$ 项。

特别径向时
$$
 \mathfrak b_o(0,\Gamma,\Xi)
  =\frac12\int_{I_*}V_w\sqrt Q\,dt
   +\sum_{e=X,0}b_e\left[
       \frac12\int_0^H{V_{0,e}(\xi)\over\sqrt\xi}\,d\xi
                      -{5\over48H^{3/2}}\right].
 \tag{F.32}
$$
右根 A 的新 $V_{0,0}$ 与新 $b_0$ 在此式中真实出现。
两根的 $\pi/4$ 及完整 normal shear 给标准角首相位
$$
 \omega_o=-8\int_{I_o}\sqrt Q\,dt,\qquad
 1+\exp i(n\omega_o+\beta_o/n),\quad m=4n .
 \tag{F.33}
$$
新增平台和右根的贡献不能设成旧值。新 P 的实际完整正返回满足
$R_++I$ 降 $4/3$ 阶，故它不改变这个 $1/n$ 系数；
它的独立外源、非mean耦合和两个 mean 方程仍保留。

由 (F.8)、$b_X<2^{336}$、$b_0<2^{29}$、
两根 $|V_0|<16$ 及 $5/(48H^{3/2})<64$，
$$
          |\beta_o(0,\Gamma,\Xi)|+1<2^{1024}.
 \tag{F.34}
$$
这是以后完整相位算术所需的新有限 $B_{*,o}$，不是旧短胞元的
$2^{62}J^2\delta^{-5}$ 上界。

## 9. 真实非径向差及加入第二参数行的精确入口

先在同一个实际径向参数 $\Gamma,\Xi$ 比较。
fixed-$t$ strict 内的差由 (F.13) 小于 $2^{937}n$。
每个 canonical root 的 finite part 差为
$(b_e/2)\int_0^H\langle V_e-V_{0,e}\rangle\xi^{-1/2}d\xi$，
其两根总费小于 $2^{512}n$。
constant-$\xi$ 与 fixed-$t$ cuts 之间的有向窄图区也必须相减：
由真正密度不变性，其绝对差至多
$2^{17}b_e\|g_e-H\|$，两根总费同样小于 $2^{512}n$。
因此在实域及所用复参数子域上，可统一取
$$
 |\beta_o(a,\Gamma,\Xi)-\beta_o(0,\Gamma,\Xi)|<2^{1024}n .
 \tag{F.35}
$$
复域用各真非零分母的同一 $1/2$ 邻域和实际角范数；
没有以固定物理 $t$ 的移动接缝高阶全纯性替代分段论证。

两原 bump 与全部新平台、两根和形状支集分离。
所以径向 $\Theta_o,\mathfrak b_o$ 的两个参数导数准确仍是原局部积分；
完整 $\beta_o$ 的基点值不同，但 Jacobian 未变。
令 $\mathcal B_o=\sqrt{12}\Delta_o/\eta_{129}$，
在原实参数盒内，原实际参数积分给
$$
 .085<\sqrt{\mathcal B_o}\,\partial_{\gamma_1}\Theta_o<.087,\quad
 .058<\sqrt{\mathcal B_o}\,\partial_{\gamma_2}\Theta_o<.061,
$$
$$
 -.023<\mathcal B_o^{-1/2}\partial_{\gamma_1}\mathfrak b_o<-.021,\quad
 -.010<\mathcal B_o^{-1/2}\partial_{\gamma_2}\mathfrak b_o<-.008 .
 \tag{F.36}
$$
沿准确保持 $\Theta_o$ 的曲线，
$|\partial_{\gamma_2}\beta_o|>2^{-9}\sqrt{\mathcal B_o}$。
这些是原定向局部积分的同一科学对象；本篇不重跑该源。

用 O.29 的真实第一参数反项，
$|\gamma_{1,o}^*-\gamma_{1,o}^{\rm rad}|<\mathcal X/(16\kappa_o)$。
径向归一 first-phase 导数小于4，且 $\kappa_o^{-1}<2^{132}$。
结合 (F.35)，完整新增第二行误差
$$
 E_o(a,q,\Xi)=
 {\beta_o(a,\gamma_1^*,\bar\gamma_{2,o}+q_o,\Xi)
  -\beta_o(0,\gamma_{1,o}^{\rm rad},
                        \bar\gamma_{2,o}+q_o,\Xi)
       \over\sqrt{\mathcal B_o}}
$$
满足
$$
 |E_o|<2^{2048}\mathcal X,\qquad
 \|D_qE_o\|_{\ell^\infty\to\mathbb C}
                         <2^{2083}\mathcal X
                 \quad(\|q\|_\infty<2^{-35}).
 \tag{F.37}
$$
导数使用真实 $2^{-34}$ 外球的剩余半径 $2^{-35}$。
它包括第一 KAM 反项对所有第二参数的完整交叉响应，
不只包括本行 $q_o$。

## 10. ordinary、weak、两 mean 和实际仿射源

每个因素仍先消费其原准确 Piola、height 共轭和 total 通量。
strict 中
$$
 F_d=\Lambda^{-1/2}F,\qquad
 f_d=\Lambda^{-1/2}\left(f-\tfrac12\nabla\log\Lambda\cdot F\right),
$$
$$
 \mathcal S_\sigma={\sigma f_d\over2}
  -\tfrac12\partial_\theta[(\nu+\sigma d)F_d^t+\sigma F_d^\theta],
 \qquad (c')_{\rm weak}=-\langle\nu F_d^t\rangle .
 \tag{F.38}
$$
原 complete mean 行与 $L_H$ 恢复照加。
ordinary 时 $f=w_{\rm ref}^2J_0\mathfrak d^{-3/2}e$，
实际径向乘子仍是
$a^{1/2}w_{\rm ref}^{3/2}J_0/(\sqrt q\,\mathfrak d)$；
若以 $L^2_t$ 消费，必须对该真权作 Cauchy--Schwarz。

根内用 A.26--A.28 的完整源，左根用其原对应合同；
新 graph 用准确
$\widehat Y_\sigma=Y_\sigma-\frac12g'(cF_d^\xi+\sigma F_d^\phi)|_g$
及两个 endpoint 荷。
这些是联合路径源范数；一般粗 $L^2_tH^s_\theta$ 体源不被免费赋予
混合图上的 trace。所有实际 $\Gamma^*$、$\nu$ 列按其真实支集、
端角/密度微分和 incoming 数据参加同一方程。

若有序 Duhamel 后的完整波位移为 $(f_A,f_B)$，
$$
 (a_R,b_R)=T(a_L,b_L)+(f_A,f_B),
$$
则准确的负散射源是
$$
 q_o=\binom{-B^{-1}f_A}{f_B-DB^{-1}f_A},\qquad
                  \|q_o\|_{H^0}\le2\|(f_A,f_B)\|_{H^0}.
 \tag{F.39}
$$
$T$ 的已付任意前后缀门 $2^{32768}$ 可直接消费各因素真正组成后的
完整源积分；未把物理源转换费藏入一个自由端口。
BV 原子用真实单侧迹和同一 jump 映射；
bare weak 通量另保其端迹，不对 $F^t$ 求未给的径向导。

本篇因此给新外两根片的完整强算子、真实首相位及其新增参数行费用。
下一步可以用 (F.34)、(F.36)--(F.37) 在同一无限第二行系统中选择
实际 $\beta_o$，再把当前五盒和新的有限外行接入完整网络；
mean/外帽条件和原强标签恢复仍须在真实方程上联立。
