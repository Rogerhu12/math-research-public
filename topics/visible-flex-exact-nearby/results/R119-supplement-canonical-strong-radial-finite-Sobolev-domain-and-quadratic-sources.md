# R119 续篇：真实 canonical 深尾的有限角强径向域及实际二次源

2026-11-15，visible-exact / tail_connector。

**状态：已证明的固定既知背景结论，保留2050阶真实导数损失。** 本篇不改 $p_*$、$\mathsf K=2^{128}$、
$\mu_j$、$\zeta_j$、五盒参数点、实际 $\Gamma^*$ 或任何物理切口。
新的辅助空间保留原 $\zeta_j$ 径向尺度，却只取有限角 Sobolev norm。
它不是原指数 Fourier 标签 $\ell^1_{224}$。

背景始终是已经构造的同一个真实非线性强尾成员，且
$\mathcal X\le2^{-8388608}$。
全闭线性解使用原真实 mean 兼容、固定高度 gauge、完整外 returned 条件
以及同一物理帽 Schur。本文不把这套背景逆自动延拓给任意有限 Sobolev
近邻背景；最后明确该后续量词。

本文的核心是：原宽松 $q_M=2^{-100}M^{-4}$ 不是低尾真实衰减率。
在真正 $p_*=1$ 接缝直接使用 canonical 两行，可以保住
$\Lambda_4>2^{132}$ 与 $\zeta_j/\zeta_{j-1}=2^{-131}$ 之间的余量。
根架的 $\delta$ 条件数只在首次输入/最后读取时收费，不每层重复相乘。

## 1. 原单位、有限角空间与输入

仍令
$$
 \delta_j=(2/25)2^{-j},\quad J=j+5,\quad
 h_j=.09\ (j\le4096),\quad h_j=8\delta_j^{1/256}\ (j>4096),
$$
$$
 m_j=\mu_j/\varepsilon_s,\qquad
 z_j^{\,*}=\zeta_j/\varepsilon_s,\qquad
 C_j=2^{200}h_j^{-5}\frac{\zeta_j}{\mu_j\delta_j^2}.
 \tag{R.1}
$$
这里 $z_j^{\,*}$ 是径向尺度，下面的特征坐标用 $Z_j$，二者不同。
完整三段 $\mu_j,\zeta_j$ 均用控制 profile 篇 C.2；尤其深尾
$$
 \mu_j=\varepsilon_s\delta_{4096}^{3/2}\delta_j^{9/2},
 \quad
 \zeta_j=\varepsilon_s\delta_{8192}^{-485/4}\delta_j^{131}.
 \tag{R.2}
$$
两个大常数因子未被丢掉。

物理高度写 $h=\rho H$，原 fixed-$t$ 普通源仍为
$$
 N=\frac{\mu_jp_*^2}{12r^{10}}e,\qquad
 f=w^2JD^{-3/2}e,\qquad w=\mu_jp_*/r^7 .
 \tag{R.3}
$$
为完整核对总体单位，定义
$$
 \bar H=H/\varepsilon_s,\quad
 \bar N=N/\varepsilon_s,\quad
 s_{\rm tail}=\varepsilon_s\sqrt{\rho\varepsilon_s}.
 \tag{R.4}
$$
每个原 density-Airy incoming 除以同一个 $s_{\rm tail}$。
这只是线性状态/源的整体改单位，实际 $w,E,D$ 不改变。
例如原深接缝的准确公式 L.5 变为
$$
 \frac{Y_j}{s_{\rm tail}}=\sqrt{m_j}\,C_M
                                  \frac{W_j}{\varepsilon_s}.
 \tag{R.5}
$$
源到波幅的相同单位也可直接核对。这里的密度是
$\mu_{\rm density}=(\mu_jp_*/(\rho r^8))JD^{-3/2}$，
不同于胞元尺度 $\mu_j$。
$f=12\mu_jr^{-4}JD^{-3/2}N$，所以
$f/\sqrt{\mu_{\rm density}}=12\sqrt{\rho\varepsilon_s}\sqrt{m_j/p_*}
(JD^{-3/2})^{1/2}N$；代 $N=\varepsilon_s\bar N$ 恰得
$s_{\rm tail}$。涉及 $f/\mu_{\rm density}$ 的项在恢复波幅时乘同一个
$\sqrt{\mu_{\rm density}}$，也得这个单位，并未保留虚假的 $\rho/\varepsilon_s$ 比。
实际总通量除以 $\varepsilon_s^2$，物理高度恢复为
$h=\rho\varepsilon_s\bar H$。因此不能把 $\rho,\varepsilon_s$ 设为1
来改变背景，却可以从显示单位准确消去它们对下文算子常数的影响。

对整数 $0\le s\le2114$ 定义窄普通源域
$$
 \mathfrak N_s(N)=
 \sup_{j\ge129}\frac1{\zeta_j\delta_j^{16}}
                  \sup_{t\in I_j}\|N(t,\cdot)\|_{H^s}.
 \tag{R.6}
$$
它含真正 mean。源在原接缝连续；若有独立原子或 weak 源，
仍按原端荷合同另列，不能用 (R.6) 给 bare 端迹。

高度空间 (R.7) 只取 $0\le s\le64$；第9节的非线性估计
也只在这个范围内成立，不因 (R.6) 的源 norm 定义扩大而扩张。
对高度变分，四个准确相对量是
$$
 p=\frac{h_\theta}{\rho rw},\quad
 k=\frac{h_t}{\rho rw},\quad U=p_\theta,\quad V=k_\theta .
$$
记
$$
 \mathfrak Y_s(h)=
 \sup_{j\ge129}C_j^{-1}
          \sup_{t\in I_j}\|(p,k,U,V)(t,\cdot)\|_{H^s}.
 \tag{R.7}
$$
高度 gauge 不计入 (R.7)，但始终由原平端高度单独指定。
不把两个 mean 都当成这个 gauge。

## 2. 所用有限角窗：重新收费至2112阶

下面需要原 U/K 的同一背景逆至 $q=s+2048\le2112$。
这里给完整替换账，不把原1024阶结论换名字。

U.4 的实际角宽仍为 $\sigma_0=2^{-20}$。
U.6 的 transport commutator、原 signed-lag kernel 和跨锥非驻相
展开现至多取2176阶。
用 $p!<2^{12p}$、相同 $c=2^{-18}$ 的完整几何和及全部二项式计数，
每组有限角操作可取
$$
 B_\#=2^{131072}.
 \tag{R.8}
$$
三个真实输入/系数/输出组至多收 $B_\#^3=2^{393216}$。
真实 radial Fourier multiplier 仍准确交换，真正角复合仍用 transport
commutator，未把裸 $C_\Phi-I$ 当同阶小量。

重做 U.9--U.14，辅助单片 cutoff 取
$L_i^\flat=2^{262144}\lambda_i$。
root 的 $2^{2217}B_\#(b/M)^{2/3}$、strict 的一次项与全部双 buffer
在这个 cutoff 下均小于原允许门。
完整高输出强费、低输出的
$4(2^{262144}\lambda_i)^{4/3}$、两侧真正反向 word 和全部 mean，
合计可取
$$
 \|\mathcal R_i:H^s\to H^{s+4/3}\|,
 \quad\|\mathcal R_i^*:H^s\to H^{s+4/3}\|
                 <2^{524288}\lambda_i^{4/3}.
 \tag{R.9}
$$
原同阶完整 Duhamel 的每行则以
$2^{524288}J^{128}\delta^{-96}\mathcal N_j\mathcal X$ 支付。
U.8 的三段求和只比原增加262144 bits，仍小于
$2^{1362144}\mathcal X<2^{-7026464}$。

取
$$
 T_j^\#=\max(2^{2097280}J^2\delta_j^{-9},\,2^{2105344}),
 \qquad
 v_j^\#=2^{-1200000}J^{-4165}\delta_j^{1073/32}.
 \tag{R.10}
$$
高反馈不超过
$2^{524288+12+256+32-2097152/3}<2^{-174000}$，
所以原全部 high inverse、双 Poisson、独立外 source 和 adjoint
按相同有序式成立。原 high 中新恢复的频段也须付：
$2^{14}(v_j^\#)^2(1+T_j^\#)<2^{-294000}$。
这仍是在同一已选径向 full inverse 中恢复行，不重新选参数。

与 Y 的直接项相比，新增费用为
$393216+2031616+1470400=3895232$ bits，
所以原 $-5868864$ 变成 $-1973632$。
含 deep Poisson 的三项仍只收 $A_j$，得到
$-5934500+393216+1470400=-4070884$。
有限新行保其129--131真实支持，费用至多
$$
 2\cdot1238200+524288+393216+2105345+20=5499269.
$$
与 $\mathcal X$ 及 $\epsilon_L$ 相乘后小于 $2^{-2889000}$。
全部相加得
$$
 \|(v^\#)^{-1}\Delta S_{\rm rem}^\#(v^\#)^{-1}\|_{H^s}
                                      <2^{-1900000},
                  \qquad 0\le s\le2112 .
 \tag{R.11}
$$
径向 mean Green、真实兼容泛函和同一高度 gauge 不改变。
原 U.24 的真正同空间 Neumann 因而给完整 weak inverse。

原物理帽反馈也保留。原 U.27 有限两端收费在这里变为
$2\cdot1238200+2\cdot131072+14000+10000+1024
=2763568<3000000$。
原物理角负阶共轭用 shifted-Sobolev 篇的同一个 $M=2^{256}$；
$|s|\le2114$ 只把原 commutator 差的 $2^{-166}$ 放宽为 $2^{-164}$，
仍小于原小量余地。usual Sobolev 等价费至多 $2^{541185}$，
完整 $C_f$ 可放宽为 $2^{800000}$。
因此同一个固定 $\eta_0,\delta=0$ 已证物理帽反馈仍小于
$2^{-29000000}$。独立 $B_R,C_R$、两个 mean、真实相位恢复与
所需兼容仍为原实际行；本段不扩到未经转授的 full-$\delta$ 帽。

## 3. 一条完整 weak 读出界

令 $\mathfrak B_q$ 是 R.11 完整有序 source norm，
全部 root source 先除以 $s_{\rm tail}$，再按 U.25 依次消 high/deep；
包括 $v^{-1}$ remaining、$v^{-1}F$ deep 与 high 一角 source 窗。
所有独立外 source、$\nu$、两 $\Gamma$ 及 mean 荷均先由原真实 map
进入。取零高度 gauge；一般情形减去同一个真实常高度核。

原 D.19--D.28 的局部物理读出、K.24--K.30 的 fixed-$t$ 普通
particular 与本篇有限角收费给
$$
 \left(\sum_{j\ge129}\delta_j^{160}
 \left[
 \left\|\frac{W_\perp}{\varepsilon_s}\right\|_{C_tH^{q-12}}^2
 +\|\bar H\|_{C_t^2H^{q-12}}^2
 \right]\right)^{1/2}
 \le 2^{2097152}
        \{\mathfrak B_q+\mathfrak N_{q+2}(N)\}.
 \tag{R.12}
$$
这里 $W_\perp$ 使用下一节的原 physical Fourier 定义；
不要求 actual 根角的低频与这个投影相同。

说明这条宽界的费用：完整同阶 word 和物理二 jet 仍只需原
$\delta^{-32}$；$v^{-1}$ 给 $\delta^{-1073/32}$；
完整 deep 反向 Poisson 只授 $vF^{-1}x_D$，故还收一份
$F_j$ 的 $\delta^{-5}$ 与4096 bits，不能把它当作裸 $vx_D$。
canonical $\nu(D)$ 与第二行最多再收4角导，不收额外径向阶。
所有所需 $J$ 多项式可由
$\sup_{j\ge129}J^{5000}\delta_j^2<2^{65536}$ 支付。
这些指数连多项式吸收之和小于78，故显示的80有余。
例如 $j\le4096$ 时 $J^{5000}<2^{65000}$；
$j>4096$ 时 $J^{5000}\delta_j^2$ 已单调递减，故65536门有效。
本式保原根状态的全层 $\ell^2$；局部重建只有有限邻层，普通
particular 的额外径向下降另给绝对可和平方和。
固定 bits 可收在
$1200000+524288+65536+2^{14}<2097152$。
普通 particular 的 K.30 在本源域多得 $\delta^{20}$，
不比该宽界更大。完整 source 到 root 的 K.31 在新窗可宽放为
$2^{524288}J^{16}\delta^{-32}$，单位由 R.5 准确给出。

同一 K/P 全浅前缀与深尾求和还给
$$
 \mathfrak B_q^{\,\rm body}
             \le2^{3145728}\mathfrak N_{q+2}(N).
 \tag{R.13}
$$
相对原1600000 bits，$v^{-1}$ 增600000，
source 角费增加至多262144，其余有限前缀、mean 和相邻缓冲
仍在余下683584 bits中；$\delta^{20}$ 只改善所有深幂。
这不是先证明根源紧支再删除其胞内 particular。

## 4. 真 canonical 低递推及较尖的指数二分

以下 $M=|m|\ge4$，深低起点
$n(M)=\min\{j\ge8193:M\le A_j\}$，
$A_j=2^{-40}\delta_j^{-1/8}$。
在真正 $p_*=1$ 接缝使用
$$
 W_1=\nu_MH_m/r^4,\quad
 W_2=\frac{p_*}{\sqrt{12}r^4}(H_{m,t}-M^2H_m),
 \quad \nu_M=M^2(M^2-1)/12 .
 \tag{R.14}
$$
原准确基 $E_M=(1,t_M;s_M,1)$、$(-1)^j$ 交替标记给
$Z_j=(-1)^jE_M^{-1}W_j$。
原 C.34/L.9 是
$$
 Z_{j-1}=\mathcal D_jZ_j,\quad \det\mathcal D_j=1/C,
 \quad
 \|\mathcal D_j-\operatorname{diag}(\Lambda_M,(C\Lambda_M)^{-1})\|
                                  <2^{-11}\Lambda_M ,
$$
$$
 C=16\sqrt2,\qquad \Lambda_M>2^{124}M^4 .
 \tag{R.15}
$$
这是原 canonical 归一，未把 $\sqrt{\mu_j}$ 的变化再重复记入矩阵。

令 $\epsilon=2^{-11}$。真正向外允许线取第一分量1，
$u_j=(1,s_j)$，一次真 cone 压窄给 $|s_j|<2^{-10}$。
其准确标量增益
$$
 a_j=(\mathcal D_j)_{11}+(\mathcal D_j)_{12}s_j
                  >\Lambda_M(1-2^{-10}).
 \tag{R.16}
$$
互补线从首切口 $v_{n-1}=(0,1)$ 向内传播；其第二分量归一，
$|v_{j,1}|<1/8$。在这两个实际移动基中，第二标量增益由
真实 determinant 准确等于
$(C a_j)^{-1}$ 乘相邻基行列式之比。
这个比在任意整段乘积中望远镜相消，只有两端的固定因子小于4。
不能每步重新乘一个基 norm8。

深段 $\zeta_{j-1}/\zeta_j=2^{131}$，故第一行向内的加权比严格小于
$$
 r_M=\frac{2^{131}}{(1-2^{-10})\Lambda_M}
       <\frac{2^7M^{-4}}{1-2^{-10}}\le\frac{512}{1023}<\frac34 .
 \tag{R.17}
$$
第二行向外的加权比更小：
$2^{-131}/(C\Lambda_M(1-2^{-10}))$。
因此在
$\sup_j\|\zeta_j^{-1}W_j\|_{H^a}$ 上，完整两行 reference Green
和其首切口 Poisson 都小于 $2^{16}$，对每个有限 $a$ 均成立。
首切口指定的是 $(E_M^{-1}W_{n-1})_1$，非两条任意 Cauchy 值。
另一条由所有未来源及真实平端允许条件给出。
此构造同时保正负频率；在逐频读出后才作完整 Fourier平方和。

同一核在辅助弱层权 $\delta_j^{100}$ 上也有界。
其最坏互补向外比小于 $2^{100}/(C\Lambda_4)<2^{-36}$；
第一行向内更小。真实弱解不含向内以 $(C\Lambda_M)^j$
增长的互补齐次列，因为这列不属于该辅助弱空间。

## 5. 实际 mixed 差只进入一个真实 canonical 源行

固定同一个非线性背景 $(P,K,U,V)$。
原固定度量 Jacobi 恒等式是
$$
 p_t=k_\theta-(A+1)p,\qquad
 k_t=F_Pp+F_Kk+F_Up_\theta+F_Vk_\theta+e .
 \tag{R.18}
$$
这里 $A=(\log w)_t$，$Q=-A$，而
$F_U=Q,F_K=2Q,F_P=F_V=0$ 是原径向参考。
因此实际与径向的差是准确的 ordinary source
$$
 e_{\rm diff}=F_Pp+(F_K-2Q)k+(F_U-Q)p_\theta+F_Vk_\theta .
 \tag{R.19}
$$
按 R.14 变换后，reference canonical 第一行完全不改，
第二行增加
$$
 N_{\rm diff}=\frac{\mu_jp_*^2}{12r^{10}}\,
                    P_\perp e_{\rm diff}.
 \tag{R.20}
$$
角 mean 单独按第7节处理，不代入不可逆的 $\nu_M$。

从已证连续 Jacobi S.5--S.8，
$$
 \|(F_P,F_K-2Q,F_U-Q,F_V)\|_{H^{a}}
 \le2^{4096}(1+|Q|)\,C_j\mathcal X,\qquad a\le72 .
$$
使用 $p_*\in[\delta/2,2^{128}/\delta]$、
$|Q|<2^{12}J\delta^{-3/2}$、
原 C.12 的完整 reference 子段流 $2^{141}M^4$，
以及低投影 $M\le A_j$ 后的一个角导数，得到每胞完整低反馈的宽界
$$
 \|\mathcal E_j^{\rm low}\|
 \le2^{8192}J^8\delta_j^{-16}C_j\mathcal X .
 \tag{R.21}
$$
具体最大参数幂可由下列直接链核对：
$Y\le2^{16}\mu_j^{-1}\delta^{-2}\|W\|_{H^{a+1}}$，
$N_{\rm diff}\le2^{4608}J\delta^{-11/2}C_j\mathcal X
\|W\|_{H^{a+1}}$；
一个 $A_j$、一次 $M^4$ 及长度 $<4\delta_j$ 的 Duhamel
合计再收小于 $\delta^{-1}$。
用于先控制胞内低状态的另一次 reference 子段流至多
$\delta^{-1/2}$。这些幂总和小于8，显示16包括全部邻层与
原首切口缓冲。所有角乘法保全部 signed Fourier lag，
没有将 actual 按模对角化。

在 R.17 的强层权及辅助 $\delta^{100}$ 弱层权中，
相邻 $\zeta$、$m$ 及参考基的固定费用均小于 $2^{256}$。
原深 $C_j$ 三段公式给
$$
 \sum_{j\ge8193}2^{8448}J^8\delta_j^{-16}C_j\mathcal X
                                      <2^{-8000000}.
 \tag{R.22}
$$
例如首端可收
$8448+8\cdot14+16\cdot8197-20010-8388608<-8260000$；
以后净下降大于108次幂。
8192仅是首边界，不擅用新 $K$ 替代其真实64。

故 reference 两行 Green 与 R.20 的完整低反馈有真正 Neumann inverse，
同时作用上述强、弱两个空间。它保全部未来源。
这证明的是实际 low 子系统，不是局部逐模正型。

## 6. 从整个 weak 解取得真实 boundary 与 high 强迫

物理 Fourier 高部使用 $P_{>A_j}$，不是把 actual 根角投影当成它。
R.12 给其完整强界；这一步只用 Fourier tail 不等式，
不需要全 FIO 的指数 lag。

令 $q=s+2048$，在 R.12 读 $H^{q-12}$。
对于目标 $H^{s+6}$，保留2030阶余量。因此
$$
 \sup_j\frac{\|P_{>A_j}W\|_{C_tH^{s+6}}}{\zeta_j}
 \le2^{2200000}
       \{\mathfrak B_q+\mathfrak N_{q+2}(N)\}.
 \tag{R.23}
$$
准确幂为 $2030/8-80-131=171/4>0$；
$A_j^{-2030}=2^{81200}\delta_j^{2030/8}$，
且深 $z_j^{\,*}\ge\delta_j^{131}$。
因此 R.23 包含原高到低的所有真正混频强迫，不把高解设零。

首切口值是同一个 weak 解的真实
$b_m=(E_M^{-1}W_{n(M)-1})_1$。
若 $n(M)>8193$，最小性给
$$
 2^{-321}M^{-8}<\delta_{n(M)}\le2^{-320}M^{-8}.
 \tag{R.24}
$$
所以从 R.12 回到 $\zeta^{-1}$ 首数据只需有限角导：
$\delta^{-211}<2^{321\cdot211}M^{1688}$。
$n(M)=8193$ 时真实固定 $\delta_{8192}>2^{-8196}$ 单独收费。
全部首数据的 $H^{s+5}$ norm 因而小于
$$
 2^{4000000}\{\mathfrak B_q+\mathfrak N_{q+2}(N)\}.
 \tag{R.25}
$$
可核的最大有限费为
$2097152+211\cdot8197<3828000$；
$q-12-(s+5+1688)=343>0$。
每个频率只选一个实际首切口，因此
$\sum_m|b_m|^2$ 由原 $\sum_j\|x_j\|^2$ 控制，
未交换一个未经授权的 $\sup_j$ 与 Fourier和。

现在给定 R.23 的整个 high 场、R.25 的真实首数据和原源，
在第5节强空间解低方程。
该解也属于 $\delta^{100}$ 弱空间。
原 weak 解的低部由 R.12 属于同一弱空间；
两者解的是完全相同的低投影方程和同一首数据。
第5节在弱空间的唯一性使二者准确相同。
这里没有用“只保低方程”偷调用一个尚未证明的全PDE唯一性。

## 7. 两个 mean 与真实高度

线性化原完整 holonomy，记 $\chi=\langle\pi\rangle$。
连续 Jacobi S.17 的准确恒等式给
$$
 \chi_t=w^2\langle JD^{-3/2}e\rangle
       =12\mu_j\langle r^{-4}JD^{-3/2}N\rangle ,
 \qquad \chi(t_{\rm flat})=0 .
 \tag{R.26}
$$
右边含给定源与固定实际背景，不含未知非mean。
使用 $N\le\zeta\delta^{16}\mathfrak N_0$ 及深几何和，
整个未来通量积分绝对收敛。
局部 mean 斜率准确为
$$
 k_0=Dk_0^{\rm hol}(p,k_\perp)
              +\langle JD^{-3/2}\rangle^{-1}\chi/w^2 .
 \tag{R.27}
$$
完整 holonomy 小根及其导数是在原真实背景处取值；
其非mean导数至少含一个背景非mean因子，norm可取
$2^{12}C_j\mathcal X$。这包括由 $\theta$ 依赖的 actual 系数
产生的 mean，不把它当成 canonical 零模。

源通量项的直接幂是
$\mu\zeta\delta^{17}/(\mu^2\delta^2)
 =(\zeta/\mu)\delta^{15}$，
比 $C_j$ 另有 $h_j^5\delta_j^{17}/2^{200}$ 余量。
R.27 及其反馈也因此包含在 R.22 的收缩中。
cut 的真实通量是 R.26 的输出；
不再另设为0。原外兼容必须与它准确相等。

mean 高度用同一个 $h_t=\rho rw\,k$ 从平端积分，
指定唯一 $\lambda$，绝不在每胞重置常数。
独立外平均高度仍为积分输出。
无源时的实际共同常高度核按原 Z 的物理定义减去，
不以一个假 canonical mean 常数代替。

## 8. 完整有限角强径向结论及实际物理二 jet

由 R.17--R.27，整个实际 weak 解满足
$$
 \sup_{j\ge8193}\zeta_j^{-1}\|W_{\perp,j}\|_{H^{s+5}}
 \le2^{4194304}\{\mathfrak B_q+\mathfrak N_{q+2}(N)\}.
 \tag{R.28}
$$
胞内读 $H^{s+1}$ 时，原 reference $M^4$ 子段流由这多4个角导
准确支付；不用再以 $M^4\le\delta^{-1/2}$ 损坏最终径向幂。
R.19 的实际修正已由 R.22 吸收。准确两态换算给
$$
 \sup_{I_j}\|(p,k,U,V)\|_{H^s}
 \le2^{180}\frac{\zeta_j}{\mu_j\delta_j^2}
       \{\text{R.28 的右端}\}
 \le C_j\,2^{4194304}
       \{\mathfrak B_q+\mathfrak N_{q+2}(N)\}.
 \tag{R.29}
$$
增加的固定因子可在 R.28 的宽松4194304 bits中统一保留；
首边界余量超过190000 bits。
有限129--8192段用 R.12、$C_j\ge\delta_j^4$ 单独收费。
原 C.2 给 $\mu_j/\varepsilon_s\ge\delta_j^6$；在4096以后，
这是由 $\delta_{4096}\ge\delta_j$ 直接得到的。
两态读出可粗取 $2^{16}\delta_j^{-92}$ 乘 R.12 的界，
且 $2097152+16+92\cdot8197<4194304$，故同一个4194304界仍成立。
所以本篇得到的是 R.7 的完整新辅助解空间，
不是只控制深负窗的 incoming。

物理 $h,h_t,h_\theta,h_{t\theta},h_{\theta\theta}$ 由 R.14准确恢复。
第二径向导数使用原 raw PDE D.22，保 ordinary 源：
$a_1,a_2<2^{100}J\delta^{-3/2}$，$p_*^{-1}\le2/\delta$。
因此对 $4\le s\le64$，深胞可取
$$
 \|h-\lambda\|_{C^2_{r,\theta}(I_j)}
 \le \rho\,2^{4400000}J^4\zeta_j\delta_j^{-5/2}
       \{\mathfrak B_q+\mathfrak N_{q+2}(N)\}.
 \tag{R.30}
$$
其中 mean 源的 R.26--R.27 给更深幂。
所有真实接缝按同一散度方程连续，故平端是实际 $C^2$ 延拓。
回 ambient Cartesian还要乘 $2^8\max(1,\rho^{-2})$；
不删除 $\rho\zeta_j$ 的真实高度单位。

R.2 使深径向幂为 $131-5/2=257/2$。
这不与泛 $\mathcal S_t$ 的 mean 紧支反例矛盾：
本篇 R.6 要求 $N=O(\zeta\delta^{16})$，
而该反例的允许源只有 $O(\zeta\delta^{-4})$。

## 9. 真二次余项与两条 Gamma 列的窄源入口

令 $Y=(p,k,p_\theta,k_\theta)$ 是任意真实高度变分，
背景仍为本文已知真实非线性成员。
Q.6 的准确固定度量余项为
$$
 e_2=\frac{N_2-j_YDF\,Y}{J+j_Y},
 \qquad
 N_2=-A(k^2+kp_\theta+w^2p^2)
                         +(1+w^2)(k_\theta-p)^2 .
 \tag{R.31}
$$
当 $\mathfrak Y_{64}(h)\le2^{-24}$ 时，分母有原严格半径余量。
完整 $H^s$ 乘积给，$0\le s\le64$，
$$
 \|N_2^{\rm physical}\|_{\mathfrak N_s}
 \le2^{393216}\mathfrak Y_{64}(h)\mathfrak Y_s(h).
 \tag{R.32}
$$
这里 $N_2^{\rm physical}=\mu p_*^2e_2/(12r^{10})$，
不是把商式的 $N_2$ 多项式误当原普通源。

显示径向账为
$$
 \frac{\mu p_*^2(1+|Q|)C_j^2}{\zeta_j\delta_j^{16}}
 \le2^{700}J h_j^{-10}\frac{\zeta_j}{\mu_j}
                                      \delta_j^{-47/2}.
 \tag{R.33}
$$
第一段负幂 $79/4$，第二段负幂 $73/4$；
第二段固定因子 $\delta_{4096}^{-3/2}$ 保留。
深段的净正幂是 $103-10/256>102$，
同时保 $\delta_{8192}^{-485/4}$。
全浅前缀最大bits小于200000，Sobolev乘积、64阶系数和
全部有限和均在393216之内。
由此实际二次源确实落进新的 R.6 域；并非任意普通源都被提升。

对已经给定的两条 $D\Gamma^*$，仍先使用 Q.19 的真实 reference
height lift：
$h_{\psi,t}=\rho rw\psi$、平端高度为0，
保所有跨胞高度常数、真实总通量与两个端列。
只对 Q.23 的余项使用本窄域。
若参数列满足原 Q.26 的准确六邻胞门，
同一 R.33 给
$$
 \mathfrak N_s(N_{\Gamma,\rm rem})
 \le2^{786432}\mathcal X\,\|b\|_{\ell^1_{224}},
                                      \qquad s\le64 .
 \tag{R.34}
$$
原 $\ell^1_{224}$ 输入到有限 $H^s$ 的准确嵌入在这一步收费；
径向 $\psi$ 的非zero端高度没有被包括在小余项中。
一般有限Sob标签的 $\Gamma$ 选择还没有由 R.34 定义。

## 10. 已证明的入口与尚须完成的非线性量词

合并 R.13/R.29，固定当前真实背景时，
普通窄源给一条明确有限导数损失的线性估计：
$$
 \mathfrak Y_s(h)
 <2^{7340034}\mathfrak N_{s+2050}(N)
       +2^{4194304}\mathfrak B_{s+2048}^{\,\rm ext},
                         \qquad 0\le s\le64 .
 \tag{R.35}
$$
所有实际 mean兼容、物理height gauge、真实外returned列与帽反馈仍保留。
非兼容输入仍输出原唯一辅助通量荷，不能称真实方程解。

R.32 是同一个原物理非线性算子的准确余项入口。
它与 R.35 给新的有限Sob/强径向 tame接口；
不是 Banach收缩结论，因为 R.35 的2050角导损失真实存在。
也没有从当前已知解析背景的逆，推断任意 R.7 球中背景都已有逆。

后续必须在这个新辅助空间中实际构造/转授参数选择与全背景逆，
支付全部 principal/首相位、五盒方向、两 $\Gamma$、外曲率图和
$\nu$ 行，或给等价的完整可迭代解图。
原 analytic $\Gamma^*(a)$ 不能只因 R.7 的径向尺度相同就免费延拓。
本篇只把真实低核、mean/height、高频回接及实际二次源在
一个明确的新有限角空间中接合；没有宣称原指数标签、非线性存在
或本课题完成。
