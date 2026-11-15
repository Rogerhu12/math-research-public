# R119 续篇：4384角窗、1730阶全尾逆损失与固定窄域的有限 tame 预算

2026-11-15，visible-exact / tail_connector。

**状态：解析证明已逐段独立核对。** 本篇不改变原对象、$\zeta_j$、
公共五盒、第一真实参数、冻结第二参数、两 mean、fixed stop、
同一个外行和源单位。它重新收费 I 的完整角窗，并把最终
strong 读出的两个有限频率余量逐式重新计算。所得更高阶逆
仍是同一真实算子的 inverse；既有低阶结论全部保留。

本篇的1730不是把2050改名：此前2048角阶缓冲由高部层权和
首次低切口两处消耗，下文逐一改为1728并重新支付真正的正余量。
它也不是已经完成 nonlinear smoothing。尤其目前 inverse
背景仍处于原 $H^{8196}$ / residual-4420 窄球；
任意新低阶输出不会自动进入该背景域。

## 1. 原背景与新的有限角范围

使用 [附近完整逆](R119-supplement-nearby-finite-Sobolev-full-tail-proxy-inverse-and-complete-sources.md)
I.1 的相同背景，仍取
$$
 R=\mathscr R\le2^{-8192000}.
 \tag{T.1}
$$
C 的四态及三阶 scaled residual 输入到4420，P 的真实 principal
共轭有8188阶。整个外行使用 I.38 的真物理表示；
如改为新 nonlinear 外图，必须同时满足
[true long 有限 jet](R133-supplement-finite-angular-jet-true-long-DN-Poisson-and-energy.md)
J 的全部实际输入、mean 和源接口。

该外行所需的高 commutator 已由
[完整4480窗](R133-supplement-extended-finite-jet-outer-commutator-window.md)
E.1--E.10 证明。其真实 DN 差、独立曲率 Poisson 列、
未匹配 $\mathcal E_B$ 在 $q\le4480$ 统一取 $2^{131072}$；
原 $q\le2176$ 的 $2^{65536}$ 更尖界仍保留。

本篇置
$$
 q_*=4384,\qquad r_*=4416,\qquad
 B_{\rm fin}^{+}=2^{319488}.
 \tag{T.2}
$$
正、负、half-order 窗和 integer ceiling 仍在 $|q|\le4388$ 内。
跨符号分部取 $r=|q|+24\le4412$；
常数计算用4416作共同上界。
C.9 付 root 角阶最多4416所需的四个附加角导，
所以实际四态/源输入至多4420。
principal 图8188足够，不从低阶输出制造新输入。

窄普通源 norm 保原定义，但现在明确允许
$$
 \mathfrak N_a(g)=\sup_j
  (\zeta_j\delta_j^{16})^{-1}\sup_{I_j}\|g_j\|_{H^a},
                    \qquad 0\le a\le4386 .
 \tag{T.3}
$$
定义更高源 norm 不宣称原64阶非线性结论已被自动扩张；
第8节另给所用的有限乘积估计。

## 2. 所有有限角操作的真实共同费用

I.3 的全 signed Fourier 和、I.4 的 paired transport commutator、
I.5 的跨符号非驻相式、两个 mean 有限边和 I.6 的完整 resolvent
公式逐字保持。只增加有限导数阶数，不假设整个余核有解析 lag。

这里使用比 $r!<2^{13r}$ 更尖且直接的有限阶门：
对 $1\le r\le4416$，AM--GM 给
$r!\le((r+1)/2)^r<2^{12r}$，因为 $4417/2<4096$。
所以三个阶乘只占 $36r_*$；
I.4--I.6 中其余完整二项式/有序分拆、物理四倍角和有限 mean
仍由原 $4r_*+8192$ 支付，合计 $40r_*+8192$。
C.9a 的系数门与新的外 E commutator 共同取最大值131072，
不在同一个 coefficient 处将两个最高阶粗界相乘。
于是
$$
 131072+40\cdot4416+8192=315904<319488 .
 \tag{T.4}
$$
若采用两个整数偶阶权的插值，额外阶数已在 (T.2) 的4阶
ceiling 余量中；负阶使用真正 adjoint。

外 $\mathcal E_B$ 的总阶尤其不能重复算。E.8 的准确式为
$$
 \mathcal E_B=P_{\mu_T}
   \{-M_a\mathsf C_L+M_aT_{Z,f}P_\perp+M_b\partial_\theta\},
$$
$$
 a=\mu_T-\mu_L,\qquad b=\mu_Ld_L-\mu_Td_T .
 \tag{T.5}
$$
$q$ 次 commutator、四次 signed-lag 和一次 multiplier 导数
至多是总阶 $q+5$，不是每个 factor 都取 $q+5$。
$P_{\mu_T}$ 的非零 commutator 为
$-|\partial_\theta^r c_T\rangle\langle1|$，
在负半阶输出只需 A0，所以没有再多一角导。
这些入口与 E 的4480范围相容；实际 homogeneous mean 为0
不影响任何 affine 荷。

## 3. 真全输入强余项及保持不变的 high cutoff

先按 I.15 已澄清的非循环次序构造传播：
true density flow 精确消去 strict 的 order-one transport，
真实 primitive 支付 composition 差的一角导；
radial interaction-picture Picard 给实际 Cauchy 演化。
根内先用径向 Airy 与有界零阶势差的 Picard 级数。
实际 Cauchy 子乘积先有 $2^{8192}\lambda_i^{12}$ 多项式界，
anti-J 及模型有序积随后才得到同阶 norm 小于2。
此链的角输入只把 $B_{\rm fin}$ 改成 (T.2)。

现在把单片低 cutoff 取为
$$
                  L_i^+=2^{491520}\lambda_i .
 \tag{T.6}
$$
其中内部 $\lambda_i=2^{32}\sqrt J\,\delta^{-9/4}$，
外行 $\lambda_o=2^{2048}$，都仍严格大于其真实 root slope。
root 完整双 buffer 的最坏指数为
$$
 2217+319488-\frac23\,491520=-5975 .
 \tag{T.7}
$$
原所有固定 buffer 因子小于 $2^{56}$，故仍有超过5900 bits余量。
strict 与 graph 的原完整二阶 remainder 同样按其真实生成子
及全部 seam 收费；其有限角部分只是两个 $B_{\rm fin}^+$。
mean 输入和反向必要项都保留。

低输出现在用 $8(L_i^+)^{4/3}$，包含 Bessel 权的端点因子。
高输出的预算为 $2^{4098}(B_{\rm fin}^+)^2\lambda_i^{4/3}$。
完整 word、相邻表示与真正两个反向窗再收2048 bits，得到
$$
 \boxed{\quad
 \|\mathcal R_i:H^q\to H^{q+4/3}\|,
 \quad\|\mathcal R_i^*:H^q\to H^{q+4/3}\|
        <2^{663552}\lambda_i^{4/3},\quad |q|\le4384 .
 \quad}                                                  \tag{T.8}
$$
高项是 $4098+2\cdot319488+2048=645122$；
低项是 $(4/3)491520+3+2048=657411$；
二者都严格小于663552。

保持 I.19 原有
$$
 T_j^\#=\max(2^{2097280}J_j^2\delta_j^{-9},2^{2105344}),
 \qquad
 v_j^\#=2^{-1200000}J_j^{-4165}\delta_j^{1073/32},
 \qquad F_j=2^{4096}J_j^4\delta_j^{-5}.
 \tag{T.9}
$$
不重新选择五盒，不改变 radial inverse 和层权。
完整 high feedback 的固定账至多
$$
 663552+12+256+32-\frac{2097152}{3}<-35000 .
 \tag{T.10}
$$
所以原 high inverse、左右 Poisson 及真 adjoint 都仍有统一因子2。
恢复的真实频带项 $2^{14}(v^\#)^2(1+T^\#)$ 未改变；
所有相邻比 $\le2^{256}$ 的原权继续合法。
未覆盖外源仍使用其真实源窗，不能套内部低输入 cutoff。

## 4. 全网络 remaining 比较不增加径向坏幂

I.10 的 principal/首同调输入仍可取
$2^{950272}J^{16}\delta^{-16}C_j^\#R$：
P 提供整个8188阶共轭，C 的131072系数门未变。
这里只消费其中至多4416阶，没有再乘一个 full 高阶传播 norm。

I.17 的三个 finite 角组每组增加
$319488-229376=90112$，总共
$$
                       3\cdot90112=270336 .
 \tag{T.11}
$$
新强常数 (T.8) 用于 (T.10) 和后面的局部读出，
不再乘入原直接一角 Duhamel 差：
该差由完整 Cauchy generator 插入及原真实子乘积直接支付，
正是 I.15--I.18 的有序证明。
两侧模型的同阶 norm 仍小于2。

因此 I.18 的每行一角差只将1738936改为2009272，
全部 $J^{40}\delta^{-47}C_j^\#R$ 次数不变。
原准确 high/deep Schur 恒等式 I.20--I.21 保留；
有 deep Poisson 的项仍只收 $A_j$，不收 $T_j^\#$。
从 I.22 前的三个已核指数直接得到
$$
 \begin{array}{c|c}
 \text{完整来源}&\text{新的二进制 exponent 上界}\\ \hline
 \text{内部直接项}&-466304+270336=-195968\\
 \text{三个 deep 项}&-2563556+270336=-2293220\\
 \text{有限外行}&-1381672+270336=-1111336 .
 \end{array}
 \tag{T.12}
$$
原 $\epsilon_L<2^{-33554432}$ 单列更小。
所有 polynomial 与几何求和、非局部 high 反馈及相邻权均照原
完整式；其深剩余 $75/256$ 未变。
各项相加后可安全取
$$
 \|(v^\#)^{-1}\Delta S_{\rm rem}(v^\#)^{-1}:H^q\to H^q\|
                       <2^{-190000},\quad0\le q\le4384 .
 \tag{T.13}
$$
原完整 mean compatibility functional、常高度核、
独立 $\sigma_\circ$ 与强源域上的 Neumann 逆因而保持。
这仍是实际 mixed 全网，不是只扩大逐模窗口。

## 5. 两端源与 whole weak 读出的重新收费

全部 sources 仍按 I.25 的同一有序公式进入。
fixed-$t$ ordinary 源、反向 root 端口、half-order 权、
mean、weak/原子及独立 $C_R/B_0/\nu/\Gamma$ 均未改。
使用到 $\mathfrak N_{q+2}$，故最高正好4386。

weak 读出不能原样沿用 I 的2097156常数。
R.12 的原固定账为
$1200000+524288+65536+2^{14}=1806208$。
本篇强余项增加139264 bits，
两次 source 角操作相对 R.8 共增加
$2(319488-131072)=376832$。
所以实际合计为
$$
       1806208+139264+376832=2322304<2359296 .
 \tag{T.14}
$$
原 $J^{5000}\delta^2$ 的65536费用不变：
角阶变化只进入 (T.4)，没有把实际 $J$ 幂提升到5000以上。
故可取
$$
 \left(\sum_{j\ge129}\delta_j^{160}
  [\|W_\perp/\varepsilon_s\|_{C_tH^{q-12}}^2+
      \|H/\varepsilon_s\|_{C_t^2H^{q-12}}^2]\right)^{1/2}
 \le2^{2359296}\{\mathfrak B_q^W+\mathfrak N_{q+2}(g)\}.
 \tag{T.15}
$$
这里 $W_\perp$ 和 $H$ 的准确物理归一仍为 R.3--R.5/I.26，
$\mu_{\rm density}$ 不与 $\mu_j$ 混名。

body source 到波映射的 R.13 原余量是683584 bits。
本次最多增加 $376832+139264=516096$，仍在该余量内，
所以可以保持
$$
          \mathfrak B_q^{W,\rm body}
                    \le2^{3145732}\mathfrak N_{q+2}(g).
 \tag{T.16}
$$
外源 norm 仍独立，不从此式推 bare weak 端点迹。

## 6. 真 canonical low 系统的高角范围

canonical 两行、两个实际锥、moving-basis determinant 及
$512/1023$ 的真实强层比，均为 R.14--R.17 的相同径向对象。
该 reference Fourier 对角，故其 $2^{16}$ Green 门对每个有限
角阶成立，不因这里提高角阶而乘一个层数。

实际差仍只有 I.30 的第二行 ordinary source：
$$
 e_{\rm diff}=F_Pp+(F_K-2Q)k+(F_U-Q)p_\theta+F_Vk_\theta
       -\alpha\mathfrak r\,k+\beta\mathfrak r_\theta p
                                      +\gamma\mathfrak r\,p .
 \tag{T.17}
$$
第一运动学行不改。source 是
$c_jP_\perp e_{\rm diff}$，真正 mean 另留。

此前 I.31 的 $2^{4096}$ 系数小门只写到72阶，不能原样借用。
本篇在所需 $a\le2664$ 用 C.9a 的完整有限 Sobolev 代数，
可以宽取 $2^{131072}(1+|Q|)C_j^\#R$。
将这个数代入 R.21 的原两态、$M^4$、长度、low cutoff 及完整
signed Fourier 乘法链，得到安全的
$$
       \|\mathcal E_j^{\rm low}\|
             <2^{196608}J_j^8\delta_j^{-16}C_j^\#R .
 \tag{T.18}
$$
相比 I.31 只增加163840 bits，$\delta^{-16}$ 没有改变。
新增 residual 项还保 C.7 的 $\delta^{16}$，无需扩大这个坏幂。

原全部深和因而仍小于
$2^{-7700000+163840}<2^{-7500000}$。
strong $\zeta^{-1}$ 与 weak $\delta^{100}$ 两个 canonical inverse
都由相同 Neumann 级数构造，未来源、首切口和两个真线全部保留。
该构造不要求 actual 逐模解耦；只 reference 是 Fourier 对角。

## 7. 两条实际频率余量允许1728缓冲

令目标输出为 $H^s$，现在取
$$
                  q=s+1728,\qquad0\le s\le2656 .
 \tag{T.19}
$$
则 $q\le4384$、源 $q+2=s+1730\le4386$。
这一步须重新核原两处几何读取，不能仅由提高角阶推出。

第一，(T.15) 给 whole 解的 $H^{q-12}$。
原 high-to-low 强迫需要 $H^{s+6}$，故实际 Fourier 余量为
$$
             q-12-(s+6)=1710 .
$$
在 $A_j=2^{-40}\delta_j^{-1/8}$ 的原 high 上，
$$
 A_j^{-1710}=2^{68400}\delta_j^{1710/8},\qquad
             1710/8-80-131=11/4>0 .                     \tag{T.20}
$$
这完整支付 weak $\delta^{80}$ 与强 $\zeta$ 两个尺度。
原 $J$ 因子与 source/输出的高阶常数已经在 (T.15) 中；
(T.20) 不再引入一个新的 $J$ 幂。
真正 high 场及其全混频作用因此具有所需的强径向输入。

第二，首切口还是同一个 whole weak 解的
$b_m=(E_M^{-1}W_{n(M)-1})_1$。
当 $n(M)>8193$，原准确式
$2^{-321}M^{-8}<\delta_{n(M)}\le2^{-320}M^{-8}$
给 $\delta^{-211}<2^{321\cdot211}M^{1688}$。
现在
$$
             q-12-(s+5+1688)=23>0 .                     \tag{T.21}
$$
仍足够从完整 Fourier 平方和读取 $H^{s+5}$ 首数据。
每个频率仍只选一个首切口，未交换 $\sup_j$ 与 $\sum_m$。
$n(M)=8193$ 的真实固定前缀继续单独收 $\delta_{8192}$，
不在8192偷用深 $K=2^{128}$。

首端最大显示固定账现为
$$
        2359296+211\cdot8197=4088863<4300000 .
 \tag{T.22}
$$
(T.20) 的68400 bits比原81200更小。
原两行 Green、胞内4角 $M^4$ 和相对物理态转换可统一宽放到
$2^{4500000}$；finite129--8192读取仍用
$\mu_j/\varepsilon_s\ge\delta_j^6$、$C_j\ge\delta_j^4$，
其 $2359296+16+92\cdot8197$ 也远小于4500000。

于是先用 whole high 场与同一首数据在 strong low 域解方程，
再由同一个 weak low inverse 的唯一性认同实际解。
该顺序保全空间解，未先假设近核只在 low 包内。
此前343导和 $171/4$ 径向余量现在分别为23导和 $11/4$；
本篇所有后续步骤只需这两项严格为正。
不得在下游继续引用原更大的余量数。

两 mean 按 I.32--I.33 的同一个准确 off-shell Green 恒等式恢复。
ordinary body channel 的平端荷为0，独立外荷照原有序式叠加。
$\chi/w^2$ 的源幂仍为 $(\zeta/\mu)\delta^{15}$，
真实 mean 高度仍从唯一平端积分。
不存在把 mean 当成 $m^{-1}$ 的步骤。

因此整个相同解满足
$$
 \boxed{\quad
 \mathfrak Y_s^W(h)
   \le2^{8000000}\mathfrak N_{s+1730}(g)
          +2^{4600000}\mathfrak B_{s+1728}^{W,\rm ext},
                     \qquad0\le s\le2656 .
 \quad}                                                  \tag{T.23}
$$
普通 body 的固定总账
$4500000+3145732=7645732<8000000$；
两 mean 和有序外源在余量内完整保留。
这是一项新证明的更尖损失，不修改已经冻结的 I.34。

对 $s\ge4$，使用同一 raw PDE 恢复两个径向导可取
$$
 \|h-\lambda\|_{C^2_{r,\theta}(I_j)}
 \le\rho\,2^{4900000}J_j^4\zeta_j\delta_j^{-5/2}
       \{\mathfrak B_{s+1728}^W+\mathfrak N_{s+1730}(g)\}.
 \tag{T.24}
$$
该式的物理单位、真实接缝、独立高度 gauge 和 Cartesian 转换
都保持。其深衰减来自原 $\zeta_{131}$，没有重定义径向未知权。

## 8. 同一个普通残差的有限阶 tame 乘积

这里只给真实已经有界的增量的 nonlinear 预算，不先制造更高阶增量。
令 $h$ 是物理高度增量，原四个相对态记 $Z_h$；
背景及增量保持实际小分母门。
对 $8\le s\le2656$，完整 Fourier convolution 给
$$
 \|fg\|_{H^s}
 \le2^{s+2}\{\|f\|_{H^1}\|g\|_{H^s}
                         +\|f\|_{H^s}\|g\|_{H^1}\}.
$$
C 的完整 reciprocal 级数用 M.23 将最高角阶分配给一个真实因子，
而不是把两个最高阶 norm 相乘。
于是原商式的二阶 source 可写为
$$
 \|e_2\|_{H^s}
 \le2^{131072}(1+|Q|)
     \{\|Z_h\|_{H^2}\|Z_h\|_{H^s}
                    +\|Z\|_{H^s}\|Z_h\|_{H^2}^2\}.
 \tag{T.25}
$$
源中的 $p_\theta,k_\theta$ 本来就是四态的第三、四行，
这里不新增一个未付角导。背景最高 norm由 (T.1) 控制。

将原准确 physical factor $c_j$ 和三段 $\mu,\zeta,h$ 代入，
R.33 的 profile为
$J h^{-10}(\zeta/\mu)\delta^{-47/2}$；
即使将六邻胞读成原完整和而加宽固定系数，
其全层 supremum 小于 $2^{200000}$。
于是字面高度线段的 $c_je_2$ 以
$2^{524288}\{\mathfrak Y_8(h)\mathfrak Y_s(h)+R\mathfrak Y_8(h)^2\}$
控制。下面固定完整 mean 重建后的常数，不再留下待选的 bit。

C.27--C.29 的 mean 重建按同一有限角乘积消费：
先由准确切向性得 scalar $\Delta\kappa_2=O(\|Z_h\|_{H^2}^2)$，
再先取 $P_\perp$ 消去 $\partial_t\Delta\kappa_2$，
最后以实际 $\Pi_{A_{0,\rm new}}$ 恢复 ordinary mean。
$F_K-2Q$ 含 nonmean 背景因子；
C.27 的4096 bits、完整六邻胞费用及投影 norm4，
连同上述131072和200000位 profile 账，
仍严格落在另一份524288位预算内。
令 $g_{\rm quad}$ 表示字面二次源与这次真 mean 重建产生的
完整 quadratic ordinary 源之和，则确定地有
$$
 \boxed{\quad
 \mathfrak N_s(g_{\rm quad})
       \le2^{524289}
       \{\mathfrak Y_8(h)\mathfrak Y_s(h)
                                  +R\,\mathfrak Y_8(h)^2\}.
 \quad}                                                   \tag{T.26}
$$
这里仍只消费 holonomy-one 切向增量及其准确 mean 重建；
背景 residual 相关的 $\mathcal E_N[h]$ 另由下式收费。
不是把 mean 本身或它的真实外端高度删去，
也不是以 $C^2$ 控制任意高频。

真实 off-shell 误差也保准确 high/low 次序：
$$
 \mathfrak N_s(\Pi_A\mathcal E_N[h])
 \le2^{196608}
     \{\mathfrak N_{s+1}(N)\mathfrak Y_8(h)
                           +\mathfrak N_9(N)\mathfrak Y_s(h)\}.
 \tag{T.27}
$$
这里使用 O.6/O.10 的准确系数
$$
 \alpha=J^{-1}+3q(1+K)/D,\qquad
 \beta=(1+q)/J,\qquad
 \gamma=3q(1+K)d/D,\qquad
 \mathcal E_N=\alpha Nk-\beta N_\theta p-\gamma Np .
$$
这些式子不含 $Q$、$c_j^{-1}$ 或额外的 $\mu_j^{-1}$。
在 $q<1/4$、$D,J>1/2$ 和 (T.1) 下，
C.9a 的完整 reciprocal 级数及二次分母乘积给
$\|\alpha\|_{H^s}+\|\beta\|_{H^s}+\|\gamma\|_{H^s}<2^{131072}$
（$s\le2656$），低阶乘法系数当然也在此界内。
其径向零态是 $\alpha=1+3q,\beta=1+q,\gamma=0$；
因此未把一个很大的径向 $Q$ 错装进该角 norm。

每胞先以两次上述 tame 乘积展开三因子，再除以
$\zeta_j\delta_j^{16}$。$N$ 的这份源权准确消去，
方向 $p,k$ 则还保一份 $C_j$。
M.4 已逐三段证明 $\sup_{j\ge129}C_j<2^{-12}$：
它包括129--8192浅前缀和规范接点，不是只对无限深尾成立。
因此不必在本处调用较粗的 $2^{160020}$ 六邻胞上界。
所有项的固定指数可宽收
$131072+2(s+2)+16<136408$；系数高阶乘低方向的项用
$\mathfrak Y_8\le\mathfrak Y_s$ 和背景 (T.1) 收入所示右边。
$N_\theta$ 的最高范数是真正的 $\mathfrak N_{s+1}$，
其低范数由 $\mathfrak N_9$ 支付。
最后 $\Pi_A g=g-\langle A_0g\rangle/\langle A_0\rangle$
只有 constant 输出，C.23 给每个 $H^s$ 上 norm小于4；
这个 rank 行不要求再对 $A_0$ 取 $s$ 个角导。
总账仍严格小于196608，证明 (T.27)。

(T.27) 所显示的 $\mathfrak N_s,\mathfrak Y_s$ 是 (T.3)/R.7
的全部内部胞元 norm。若另附 C 第1节的有限 connector ordinary
残差块，使用它自己的真实径向 scalar 源单位，不能代入内部
$c_j=\mu_jp_*^2/(12r^{10})$。同一 (O.9) 在该块先乘此 scalar，
三个 $N$ 因子仍按同一源单位消去；方向四态则由其实际
$2^{440}$ norm给 $2^{-440}\mathfrak Y_s^o$。
$D,J,q$ 的原同一小门成立，所以上述196608位账也覆盖这一
独立普通块。它转到真正 $\mathfrak B^{\rm ext}$ 的 source map
仍按 I.25，未由 ordinary norm 授 bare 外端、weak 或原子荷。

不能把 (T.27) 当成 $\mathcal K_W\mathcal E_N$ 的同域 Neumann 门。
第一 $\Gamma$ 的 G projected 源和低方向 Schur 目前仍只授
其原 $q\le2114$ 源窗；本篇没有把它提升到4386。
第二参数和其它外方向仍按原实际列保留。

(T.25)--(T.27) 只比较 ordinary 源的角 norm。
径向 residual 的三阶 scaled 增量必须逐式使用原 PDE、
真实 seam 和 mean 小根，不能从这些式子推出未付的径向导数。

## 9. 更高线性范围与实际 nonlinear 迭代仍不同

本篇已付清：同一附近背景族、固定真实外行下的4384角网络，
完整两侧 $4/3$、不变的高 cutoff/层权、全 high/deep/remaining、
真实 mean/compatibility 和原单位有序 sources。
新的输出到2656，普通源损失为1730；没有停在局部频包。

但 (T.23) 仍不能直接放入一般同空间 Picard。
例如低阶输出经 Fourier smoothing 提高到8196阶时，会出现
真实的截断幂；同时目前背景 inverse 假设 (T.1) 的
$H^{8196}$ 和 residual-4420 输入保持小。
这些项不因 (T.26) 是一个 tame 乘积就自动闭合。

一个可执行的后续 smoothing 证明必须明确完成以下事项：
在实际所需高阶范围内给背景依赖的 tame inverse或另一个
真正可保持的背景域；给同一真实高度 smoothing 的完整 mean
重建和第一参数更新；支付三阶径向 residual 和全部外部
height/flux/curvature traces；再逐步验证增量、高 norm 增长、
误差下降及收敛。一般 Y64 截断、单个高阶逆、或仅写
“使用 Nash--Moser”均不满足这些要求。

本篇不先宣称这些门已完成，也不将有限光滑所得重新命名为
原 analytic224 标签。保留的新、具体入口是 (T.23) 和
(T.25)--(T.27)：它们给出了后续构造可以实际消费的有限阶
数量、真正损失、全径向权及非零 residual 误差。
