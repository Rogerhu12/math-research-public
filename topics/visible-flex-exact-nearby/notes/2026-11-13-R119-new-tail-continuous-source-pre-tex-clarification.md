# R119 续篇：新真尾的连续普通源、完整 mean 与仿射外端数据

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 固定新 $c=16\sqrt2$ 深 profile 的任一已选实
$\Gamma$ 和按新全频右线重新选出的共同好 bump。本文在这个真实
径向参考上构造连续有源强解、全频仿射两迹条件，并将尾源接到真正的
外 regular 切口。非mean grounded Robin 的有源列确有长段筛选；
mean 的通量原函数和独立高度常数另列，没有设为0。

本文使用新全标签 Green，而不将旧尾的源算子重新命名。这里是
**零标签参考处**的全频线性定理；非零标签处的相对网络逆仍需真实
Airy/相位接合。源也须满足下列明确的 $L^1$ 和点态合同。

## 1. 一个物理源的三种准确单位

符号取自
[新 profile](R119-supplement-new-deep-profile-and-actual-homogeneous-Robin.md)
和 [新全标签图](R119-supplement-new-deep-profile-full-label-chart.md)。
令物理 raw 高度为 $h=\rho H$，$a=\rho r$，$t=\log r$，
$y=\sqrt{12}t$。本节的相对源 $e$ 定义为
$$
 H_{tt}+(A-1)H_t+A H_{\theta\theta}=rw e,
 \qquad A=w_t/w.
 \tag{S.1}
$$
同一物理径向方程及 canonical 源是
$$
 H_{rr}+\frac{w_r}{w}H_r+
       \frac{w_r}{rw}H_{\theta\theta}=F,
 \qquad F=\frac wr e,
$$
$$
 N_{m,j}=\frac{p_*}{12r^2}F_{m,j}
       =\frac{\mu_jp_*^2}{12r^{10}}e_{m,j}.
 \tag{S.2}
$$
因此 R115 (115.25) 的材料密度源 $e_{\mathcal E}$ 在当前参考上是
$$
 e_{\mathcal E}=\frac{w}{\sqrt{12}}e,
 \qquad N=\frac{p_*}{\sqrt{12}r^3}e_{\mathcal E}.
 \tag{S.3}
$$
在非零标签背景的准确转换为
$e_{\mathcal E}=wJD^{-3/2}e/\sqrt{12}$；这条恒等式不把下文的
径向基本解转授给非径向背景。

对 $m\ne0$ 保留真正的两分量状态
$$
 W_1=\nu_mH/r^4,\qquad
 W_2=\frac{p_*}{\sqrt{12}r^4}(H_t-m^2H),\qquad
 W_y=\begin{pmatrix}k_m&\nu_m/p_*\\-p_*&-k_m\end{pmatrix}W
                   +\binom0N.
 \tag{S.4}
$$
每胞输出转换仍为 $D_j=\operatorname{diag}(1,c_j^{-1})$。
下文允许 $N_0$，但没有以 $\nu_0=0$ 伪造一个可逆高度状态。

## 2. 真内部连续流和完整源空间

原 R15 (3.3) 的内部正、逆流证明在新 profile 上须重新付末段费用。
新的 $c_j\in[16,64]$ 保留最低 $p_*\ge\delta_j/2$、最高
$p_*\le64/\delta_j$、三主剪切及全部导数包络。完整 log 常数由
旧值放宽到6；四坡的指数前因子可由 $e^6$ 放宽到 $e^{12}$。
新全标签图 §3 已支付这个改动及余量 $2^{16}$。同一个证明用于
任意内部子区间，因此全频、双方向有
$$
 \|\Phi_{m,j}(s,t)\|_\infty,
 \|\Phi_{m,j}(s,t)^{-1}\|_\infty
 \le2^{80}(1+|m|)^{312}e^{|m|\beta_j}.
 \tag{S.5}
$$
$\beta_j$ 是原实际九段流角费，并满足
$\beta_j<h_j/4$、$\sum(h_j+\beta_j)<358$。
这不是仅在两个端点已知的矩阵界。

固定 $\beta\ge0$，$\sigma=\tau_{128}-1$。定义包含零模的明确范数
$$
 \|N\|_{\mathcal S_{1,\beta}}
 =\sum_{m\in4\mathbb Z}(1+|m|)^{312}\sup_{j>128}
 \left[\zeta_{j-1}^{-1}
 e^{|m|(\tau_{j-1}+\beta+\beta_j)}
       \int_{I_j}|N_{m,j}(y)|dy\right],
 \tag{S.6}
$$
$$
 \|N\|_{\mathcal S_{2,\beta}}
 =\sum_{m\in4\mathbb Z}\sup_{j>128}
 \left[\delta_j^4\zeta_j^{-1}e^{|m|(\sigma+\beta)}
                         \sup_{I_j}|N_{m,j}|\right].
 \tag{S.7}
$$
源各胞连续，且 (S.2) 的同一物理 $F$ 在接缝连续。范数未包含未知
解、未知基本解或未知 DN。只有径向 $L^1$ 源不足以控制二阶尖峰，
所以不能删除 (S.7)。

由真实 Duhamel 公式，非mean端口源准确为
$$
 f_{m,j-1}=(-1)^{j-1}\zeta_{j-1}^{-1}e^{|m|\tau_{j-1}}D_j
       \int_{I_j}\Phi_{m,j}(y_+,s)\binom0{N_{m,j}(s)}ds.
 \tag{S.8}
$$
它同时含两个端口分量。先逐模取径向上确界再求和，(S.5) 给
$$
 \|f\|_{\mathcal F_\beta}\le2^{80}\|N\|_{\mathcal S_{1,\beta}},
 \qquad X=\mathcal H_\Gamma^\dagger a+\mathcal G_\Gamma^\dagger f,
$$
$$
 \boxed{\quad\|X\|_{\mathcal X_\beta}
 <9\|a\|_\beta+2^{96}\|N\|_{\mathcal S_{1,\beta}}.\quad}
 \tag{S.9}
$$
每个内部场由同一连续 Duhamel 公式重建。这里的 source 没有先被
误认为任意端点跳量，也没有把真实高区块删去。

## 3. Mean 通量、完整高度与平盘

真实 raw conormal 的常数槽是
$$
 p_0=\frac wr(H_t)_0,\qquad
 (p_0)_t=\langle w^2e\rangle,
 (p_0)_y=\sqrt{12}\,\mu_jr^{-4}N_0.
 \tag{S.10}
$$
平端的通量必须为0。因而唯一的通量及带一个独立常数的高度为
$$
 p_0(y)=\int_{y_f}^y\sqrt{12}\,\mu(s)r(s)^{-4}N_0(s)ds,
 \qquad
 H_0(t)=\lambda+\int_{t_f}^t\frac rwp_0(s)ds.
 \tag{S.11}
$$
分段出现的 $\mu$ 只是 (S.2) 的 canonical 归一；积分密度
$w^2e$ 是同一个连续物理源。cut128 的 $p_0$ 是真实 holonomy
负荷，不能另设为0。$\lambda$ 是平盘上的唯一高度自由常数。

对所有深浅层，$\mu_{j+1}/\mu_j\le2^{-9/2}$，而
$\zeta_{j+1}/\zeta_j=2^{-39/4}$。由 (S.6) 逐项积分得到
$$
 |p_0|_{I_j}<2^{13}\mu_j\zeta_j\|N\|_{\mathcal S_{1,0}},
 \quad |(H_0)_t|<2^{22}\zeta_j\delta_j^{-1}
                                      \|N\|_{\mathcal S_{1,0}},
$$
$$
 |H_0-\lambda|<2^{25}\zeta_j\|N\|_{\mathcal S_{1,0}}.
 \tag{S.12}
$$
其中 $w_{\min}\ge\mu_j\delta_j/256$、每胞 $t$ 长小于
$4\delta_j$。准确二阶方程是
$$
 (H_0)_{tt}=(1-A)(H_0)_t+\frac{12r^4}{p_*}N_0.
$$
用 $|1-A|<2^9\delta_j^{-5/2}$ 和 (S.7)，完整 mean 二 jet
小于 $2^{34}\zeta_j\delta_j^{-5}
(\|N\|_{\mathcal S_{1,0}}+\|N\|_{\mathcal S_{2,0}})$。

非mean内部转换与原 R15 (6.2)--(6.4) 相同；(S.5) 的额外
$2^{16}$ 连同 $|b|\le128\delta^{-5/2}$ 只增加固定二进制费。
包括 mean 的一个安全完整界是
$$
 \|H-\lambda\|_{C^2_{r,\theta},\mathcal A_{\sigma+\beta}(I_j)}
 <2^{108}626^{313}\epsilon\delta_j^{19/4}
       (\|X\|_{\mathcal X_\beta}+\|N\|_{\mathcal S_{1,\beta}}
                                  +\|N\|_{\mathcal S_{2,\beta}}).
 \tag{S.13}
$$
所有非mean和 mean二阶 jets 在平端趋0；物理 $F$ 连续给每个
接缝相同的二阶 jet。因此有真正全频 $C^2$ 平坦延拓。

## 4. 新对象的实际标签权仍由404支付

须重证新 cut128 允许线的权，不能引用旧线。令
$H_m^\dagger=\mathcal H_\Gamma^\dagger e_m^{\rm label}$，
$u_m^\dagger=H_m^\dagger(128)$，
$\mathfrak w_m^\dagger=\|u_m^\dagger\|_\infty^{-1}$。
有限真流可逆及标签为1给 $u_m^\dagger\ne0$。

新特征基 $E_{m,c}$ 满足 $\|E\|,\|E^{-1}\|<2$，
$\Lambda_{m,c}>4m^4$、$L_{m,c}<m^4$、
$\lambda_{m,c}/\Lambda_{m,c}<2^{-24}$。在真实窄窗
$m^4\sqrt{\delta_j}\le2^{-28}$，完整误差给
$$
 \|-E^{-1}B_{m,j}E-\operatorname{diag}(\Lambda,\lambda)\|
       <2^{-11}\Lambda.
 \tag{S.14}
$$
锥 $|v|\le|u|/2$ 经一个同基真胞元后进入
$|v|<|u|/1024$；其 Möbius 导数小于 $1/4$。这仍由真
$\det B=1/c_j$ 证明。唯一的基变换 $Q=E_{64}^{-1}E_C$ 满足
新全标签图 (L.13)。所以经过 $Q$ 后
$$
 |v/u|<\frac{1/8+2/1024}{1/2-2/1024}<1/2,
$$
$$
 |u_{j-1}|>\frac13 L_{m,C}e^{-mh_j}|u_j|.
 \tag{S.15}
$$
对需要跨接缝的 $m\ge176$，$L_{m,C}>3$；所以这一胞元也有
$|u_{j-1}|\ge e^{-mh_j}|u_j|$。没有把基变换的交叉行置0。
未来锥的存在按严格投影收缩取极限，再由新强 Green 的唯一性
识别为同一真允许线。

标签层的定义已在新全标签图固定。43个浅模仍有 $b_m=128$。
其余 $m\ge176$ 满足原准确推导
$b_m\ge j_0(m)=\max(129,\lceil56+8\log_2m\rceil)$；所需条件
只有 $L_{m,c}<m^4$、深段 $h_j=8\delta_j^{1/256}$ 和全部浅模门，
都已重证。故锥段不再重复支付大主特征值。

剩余坏前缀以 (S.5)、$D_j^{-1}\le64$ 及规范费得到
$\|\mathcal A_{m,j}^{-1}\|<2^{96}(1+m)^{312}e^{m(h_j+\beta_j)}$。
令 $x=\log m$；坏前缀若非空，$N_m^{bad}<12(x-6)$。
其每频率额外费用小于
$$
 e^{-6}\big[(121032/5)u+3744u^2\big]e^{-u},\qquad u=x-6>0.
$$
由 $e>8/3$，它严格小于
$$
 (3/8)^6(55917/5)<32.
$$
连同完整角和358和 $\|E^{-1}\|<2$，得到
$$
 \boxed{\quad 1/9<\mathfrak w_m^\dagger<e^{391m},\qquad
                   \tau_{128}+391<404.\quad}
 \tag{S.16}
$$
这个结果包括有限未改前缀、唯一新接缝和全部深层。

## 5. Cut128 的完整有源两迹图

令 $g_m(N)=(\mathcal G_\Gamma^\dagger f)_{m,128}$，
$\Lambda_m^\dagger=\operatorname{span}u_m^\dagger$。
给定规范切口迹 $v_m$ 可由 (S.9) 的同一全尾实现，当且仅当
$$
 v_m-g_m(N)\in\Lambda_m^\dagger,\qquad
 \sum_{m\ne0}e^{\beta|m|}\mathfrak w_m^\dagger
                       \|v_m-g_m(N)\|_\infty<\infty.
 \tag{S.17}
$$
后一个和准确等于标签范数。mean 则须等于 (S.11) 的高度和通量，
允许同一个整体 $\lambda$；不是额外任意指定的两个数。
这给出了真实连续 source 的仿射两迹条件。

## 6. 从真尾源到外 regular 切口的全频仿射列

本节源只支持于 mixed tail，有限 connector、双 bump 和
$0\le u\le B=2^{24}-25/8$ 的长段上无源。
取具体的充分合同
$$
 S_*:=\|N\|_{\mathcal S_{1,2304}}+
                         \|N\|_{\mathcal S_{2,2304}}<\infty.
 \tag{S.18}
$$
先取零内部标签的真实 particular $X^p=\mathcal G^\dagger f$。
新参考的 cut128 和 retuned connector 仍满足完整 R119 平衡能量
所用的全部长度、$A,w/a$ 及尺度门；新 bump 也在同一允许盒内。
线性化该真传播（不是把一个大 particular 当非线性小背景）给
$$
 \|(f_B^p,k_B^p)\|_{\mathfrak C_{\sigma_B}}
 <2^{-447}\|X^p\|_{\mathcal X_{2304}}<2^{-351}S_* ,
 \quad \sigma_B=\tau_{128}+2304-235>2074.
 \tag{S.19}
$$
$f_B=h_\perp/(a_Bw_B)$、$k_B=(h_a)_\perp/w_B$，
$\mathfrak C_s$ 可用较强的和
$\sum_{m\ne0}e^{sM}(M^2|f_m|+M|k_m|)$。

新实际主方向、同一第四保持 connector 及重新选择的全模好集
重新满足原联合 Schur 证明的每个输入；(S.16) 仍为404。因此
准确同一个1850角费可用于新对象：
$$
 \|\mathsf D_0^{\dagger,-1}g\|_{\ell^1_\beta}
 \le\frac1{16}\|g\|_{\mathfrak Z_{\beta+1850}},
 \quad\mathsf D_0^\dagger a=k_B^{lin}+M\coth(ML)f_B^{lin}.
 \tag{S.20}
$$
特别令外端非mean raw Dirichlet 值为0，准确取
$$
 a^N=-\mathsf D_0^{\dagger,-1}(k_B^p+M\coth(ML)f_B^p),
 \qquad \|a^N\|_{224}<2^{-354}S_*.
 \tag{S.21}
$$
因为 $M\coth(ML)<2M$，且 $224+1850=2074<\sigma_B$。
尾中 $X^p+\mathcal H^\dagger a^N$、完整有限 connector 与长段
Dirichlet 解因此确实连成全频场。两条非mean迹都匹配；没有把
source 的 particular 删掉。其总尾状态可取 $\|X\|_{224}<2^{97}S_*$。

为计算真实 grounded 外 affine 列，不需要对这个整个场作极大
反向 Cauchy 估计。记同一 R74 状态 $Y=(y,y_u/M)$，
$$
 v=A_0y-4y_u/M^2,\qquad p=-y+4y_u/A_0,
 \qquad A_0=4\omega+a_*^2/z_* .
 \tag{S.22}
$$
其矩阵行列式是 $4(1-M^{-2})$。令真实齐次 regular 解 $q_m$
满足 $v(q_m;0)=1$，$p(q_m;0)=-\gamma_m^\dagger$。
新好集及同一增长直线的 Wronskian 给
$$
 \|Y(q_m;B)\|_2<2^{42}e^{-ML},\qquad L=\omega B.
 \tag{S.23}
$$
这里 $\|Y(q_m;0)\|_2<1$：由新实际
$\lambda_m=-M\omega+O(2^{41}M\omega e^{-2ML})$、
$A_0>4\omega>28/5$ 直接可核。夹角下界是实际新好集的 $2^{-39}$。

对任一同源 particular，完整有源 Robin 列准确为
$$
 r_m(N)=p_m(0)+\gamma_m^\dagger v_m(0)
       =4(1-M^{-2})M\det(Y(q_m;B),Y^p_m(B)).
 \tag{S.24}
$$
加上任意真实齐次尾线不会改变它。源在这整段为0，故这里使用的
Wronskian 常数性合法。完整两迹变换
$(f,k/M)=-16\omega h(B)^2\mathsf J_MY$ 以及
$\|\mathsf J_M^{-1}\|_\infty\le4/3$ 给
$\|Y^p(B)\|_2<h(B)^{-2}(|f|+|k|/M)/8$。
于是对实际物理窗口 $\sigma_o=1/512$，由 (S.19) 得
$$
 \boxed{\quad
   (p+\Gamma^\dagger v)_\perp=r(N),\qquad
   \|r(N)\|_{\mathcal A_{\sigma_o},1}
                      <2^{-300}e^{-4L}S_* .\quad}
 \tag{S.25}
$$
这里 $\|r\|_{\mathcal A_s,1}=\sum_{m\ne0}e^{s|m|}|m||r_m|$。
这是实际新尾源的 affine DN 列，不是旧齐次 $\Gamma$ 的形式转授。
它仍只在 (S.18) 的真实 source 空间上成立。

## 7. 外端 mean 行和实际线性输入半径

外部无源时，(S.11) 的 raw mean flux $p_0$ 保持常数。外端
平均 raw 高度准确为
$$
 h_0(0)=\rho\lambda+\rho\!int_{t_f}^{t_e}\frac rwp_0dt
                  +p_0\!\int_{t_e}^{t_B}\frac awdt+4\omega Lp_0.
 \tag{S.26}
$$
第二个积分使用真实有限 connector 加双 bump；其方向沿深端至
外端，不可更换成另一外法向的符号。$(h_0,p_0)$ 是两个输出，
只有 $\lambda$ 一个自由常数。

为给明确有限费，cut128 有
$|K_{0,e}|=|p_0|/w_e^2<2^{27}\delta_{128}^{15/4}S_*$。
有限短段的总负 $A$ 积分大于 $-7/2$，故全程
$w\ge2^{-6}w_e$，$|K_0|<2^{39}\delta_{128}^{15/4}S_*$。
总时间小于132、$aw<1$ 给有限平均高度变化
$<2^{47}\delta_{128}^{15/4}S_*$。连同 (S.12)、
$4\omega L<2^{30}$、$\rho<1$，安全地有
$$
 |h_0(0)-\rho\lambda|<2^{-400}S_* ,\qquad
 |p_0|<2^{-1200}\epsilon S_* .
 \tag{S.27}
$$
这些量没有被非mean的 $e^{-4L}$ 免费替代。

零尾源时，R74 允许的真实外数据和普通帽源（仍在 $B$ 后齐次）
也可在新对象重跑：全部有限几何、增长线夹角及 (S.16) 的 raw404
费用均已付。若其原完整输入量为
$A_m=h(0)^2|f_m|+M^{1/p_*}F_{m,p_*}$，则
$$
 \|a^{\rm lin}\|_{224}
 \le e^{-33545404}\sum_{m\ne0}A_m.
 \tag{S.28}
$$
所以例如同一真实线性合同 $\sum A_m\le1$ 产生的输入确实位于
$2^{-10000}$ 标签球；这不是任意选择一个抽象小球。但 (S.28)
不是更新后非线性 regular 解的可达性证明，不能取代尚未闭合的
实际 $D_a\mathcal F$ 相对逆。

## 8. 全向量与更新后问题的权限

若源来自给定 metric tensor $T$，必须用新实际 $w$ 计算
$$
 e_{\mathcal E,T}=-\frac{ED^{-3/2}}{\sqrt{12}w}
                         D_g\mathcal P(g_0,z)[T],
$$
再按 (S.3)、(S.6)--(S.7) 检查它，且保留 $T$ 的完整一阶 jets、
normal/shear 源端项和角周期条件。mean 的 (S.11)、(S.26) 是
必须与该 metric source 接合的真实 holonomy/高度行。任意 scalar
源的 existence 不自动授予一个全局单值水平重建。

本文完成新径向参考的连续源、平坦 realization、真仿射两迹、
筛选后的非mean外 affine DN 和全部 mean 输出。非零标签处的真
相位/Airy网络条件数、更新后的 source 算子及 nonlinear matching
仍是不同的待证合同。

[有理与符号核验程序](../scripts/fourfold_new_tail_continuous_source_20261113.py)
及 [报告](../notes/2026-11-13-R119-new-tail-continuous-source-budget.json)
记录实际归一、接缝锥、全部源和 mean 指数、外两迹行列式、
Wronskian 列及新线性输入半径。
