# R119 续篇：窄源图上的近似右逆、完整端口缺陷与低阶无平滑损失

2026-11-15，visible-exact / tail_connector。

**状态：解析证明，已独立核对。** 本篇使用已证明的 E 固定参考图、N 完整网络、J 三径源四径状态和 G 第一参数 Schur。几何、第二参数、$\zeta_{131}$、真实五盒点及所有 source 单位保持不变。新的结论是一个真正作用到 $E_s$ 的近似右逆；它同时控制状态和窄参考源，不把 $\mathscr X_s$ 偷换成 $E_s$。

body 图仍为 holonomy-one。一般有荷数据可用 N 的完整 proxy 解，但它与当前 nonlinear 第一参数值图的识别仍限于 G.30 的真正切空间。物理两端 height、flux、cap/long 原行与 $\nu$ 不由 body 近似逆自动消去。本篇给它们准确的差项，作为下一完整匹配 Schur 的明确输入。

## 1. 真实图、源和外行

全文使用：

* [E：固定参考图与准确角平滑](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md)；
* [N：二层完整网络 tame 逆](R119-supplement-two-level-full-network-tame-inverse-and-complete-sources.md)；
* [J：三径普通源与四径状态](R119-supplement-three-radial-source-jets-four-state-jets-and-1734-loss.md)；
* [G：第一参数的低方向与完整 projected Schur](R119-supplement-low-direction-first-Gamma-projected-metric-source-and-linear-Schur.md)；
* [M：holonomy 荷与真实高度图](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md)。

保 E.1--E.6 的固定径向参考 $\mathcal L_0$、非mean物理高度 $u$、图 norm $E_s$ 和三径 source norm $Z_s^{[3]}$。写
$$
 {\mathfrak f}(u)=P_\perp{\mathfrak F}(u)
       =\mathcal L_0u+\mathcal Q(u),\qquad
 {\mathfrak F}(u)=\Pi_{A_u}{\mathfrak f}(u),\quad
 A_u=JD^{-3/2}.                                          \tag{A.1}
$$
内部 $\mathfrak F$ 为 $N=c_{\rm ph}(K_t-F)$，有限 connector 为原 ordinary $e_o$，不替换其单位。$\Pi_A f=f-\langle Af\rangle/\langle A\rangle$，并不等于外 DN 的 density 投影。

固定
$$
 \|u\|_{E_{1856}}\le\rho_E/2,\qquad
 \rho_E=2^{-8192016},\qquad
 u\in E_{8192}.                                           \tag{A.2}
$$
高阶仅有限。E.22 给 N.1 的低球，N.1a/b 给同一第二参数间隙。外行先取 N 已付的同一个真实 linear long/$C_R$ 行。若更新外背景，N.2 的相对型、伴随、mean、Poisson 与全传播门均须另外满足。

定义同一外源的完整记号
$$
 d_\ell(f,b)=Z_{\ell+2}^{[3]}(f)+\mathfrak B_\ell^{[3]}(b).
 \tag{A.3}
$$
$\mathfrak B$ 保 N.4、K.21a 和 J 的全部独立端口：普通 Robin、两 mean、height/span、source 原子、给定 cap/source 列及其真实 physical 系数。screened 列保 $s_B\epsilon_L\mathcal D$，unscreened 两 mean 和 $a w(L)/165$ 不加 $\epsilon_L$。本篇不把一个未支付的实际 cap high 列放入已经成立的 $\mathfrak B$。

## 2. 三径 compatible 投影的同一低门

(A.2) 和 C.9a/M 的完整小根给
$$
 \langle A_u\rangle>3/4,\qquad
 \max_{1\le a\le3}\ell^a
       \|\partial_t^a(A_u-1)\|_{H^2}
       +\|A_u-1\|_{H^2}<2^{-20}.                         \tag{A.4}
$$
这里 $\ell$ 按真实胞元或 finite connector 取值。可直接用低阶192的同一次递推：局部费用小于 $2^{262144}C_j^\#\mathscr R_{1856}$，原 $\sup C_j^\#<2^{160020}$ 与 N.1 仍留超过七百万 bits；有限 connector 的原单位更小。$\ell^a$ 分配到每个径向 Leibniz因子，不求未付的第四源导。

对三个普通径向导分配分母和圆周配对，(A.4)于是给
$$
 Z_s^{[3]}(\Pi_{A_u}f)\le4Z_s^{[3]}(f),\qquad s\ge0 .
 \tag{A.5}
$$
修正的输出是角常数；其 $H^s$ norm不要求 $A_u$ 有 $s$ 个角导。仍保其完整前三径导。这个常数只使用低背景，不能因 high $E_s$ 增大而重选 small gate。

## 3. 先解完整 proxy，再保真正 Jacobi 缺陷

取普通 mean为0的 body 源 $f$。先令 $g=\Pi_{A_u}f$，用 N.26/J.15 解
$$
 c_{\rm ph}\mathcal J_u h-
       \mathcal B_{p,u}(P_\perp h)=g,\qquad
 {\cal B}^{\rm lin}_u h=b .                              \tag{A.6}
$$
有限部分用其真 ordinary 两行，不把 $c_{\rm ph}$ 移植过去。$\mathcal B^{\rm lin}_u$ 表示 N 的完整 prescribed linear 端行、实际 matching 和唯一常高度规范。它不意味着一个 nonlinear 行在邻态都被冻结。

在 nonlinear 图的识别中，$b$ 须满足 holonomy-one 切向的真实外荷兼容；特别 body channel 取 flat $\chi=0$，未另给的外 flux 荷不由此设为0。一般 charged $b$ 仍可按 N 解其 projected-feedback 系统，但本篇不把它称作 $D\gamma_1^*$ 在 $\chi\ne0$ 上的导数。

设
$$
 v=P_\perp h,\qquad {\cal R}_u(f,b)=v,\qquad
 {\cal E}_u[h]=\alpha N k-\beta N_\theta p-\gamma Np .
 \tag{A.7}
$$
G.30 与 $P_\perp\Pi_A=P_\perp$ 准确给
$$
 \boxed{\quad
 D{\mathfrak f}(u)[{\cal R}_u(f,b)]
       =f-P_\perp{\cal E}_u[h].
 \quad}                                                   \tag{A.8}
$$
$\mathcal B_p$ 已含完整 metric 的 $+\dot\psi\,N$。不得再对参考 lift $H_p$ 收一次 $\mathcal E_u[H_p]$，也没有对 (A.7) 的剩余缺陷作有损 Neumann。

完整 mean derivative 为
$$
 D{\mathfrak F}(u)[v]
   =D\Pi_{A_u}[v]\,{\mathfrak f}(u)
        +\Pi_{A_u}\{f-P_\perp{\cal E}_u[h]\}.             \tag{A.9}
$$
第一项是实际 residual-sensitive mean 行。它一般非零；(A.8) 只选择了一个非mean source 坐标。

## 4. 证明像确实属于窄源图域

N/J 先给 $h$ 的真实四态与四径 jets，因而 $X_s^0(v)<\infty$，但这一步本身不授予 $Z_s^{[3]}(\mathcal L_0v)$。

对 E.16 的准确式求一次方向导数：
$$
 e^\psi\mathcal L_0v
 =D{\mathfrak f}(u)[v]
      -e^\psi D\psi(u)[v]\,\mathcal L_0u
      -DQ_{\rm src}(u)[v].                              \tag{A.10}
$$
finite connector用 E.17。$Q_{\rm src}$ 是 E.20 的两项，不含径向 multiplier 乘 $\mathcal L_0u$。L 的低方向 functional 给 $D\psi[v]$ 全部原 profile及四个 broken径导；$DQ_{\rm src}$ 只用已得的四态 jets。背景 $\mathcal L_0u$ 则是 (A.2) 的真正 graph输入。右侧各项均在 $Z_s^{[3]}$，由 (A.8)、J.23 和低正下界可解回 $\mathcal L_0v$。所以 $v\in E_s$，不是先假设其 graph正则再套 tame不等式。

为估计该 norm，可在已经证明的域上改用 E.25：
$$
 \|v\|_{E_s}\le
 2\{X_s^0(v)+Z_s^{[3]}(f)
       +Z_s^{[3]}(P_\perp{\cal E}_u[h])
       +K_E\|u\|_{E_s}\|v\|_{E_{20}}\},
 \quad K_E=2^{2097152}.                                  \tag{A.11}
$$
其中 $K_E\|u\|_{E_{20}}\|v\|_{E_s}$ 已由 (A.2) 吸收。径向 $e^{\pm\psi}$ 与当前/参考四态的转换小于2；这没有把 high背景放入分母。

## 5. 低 graph读出没有平滑频率损失

在 $s=20$，J.23 只用背景 $N_{21}$、$N_{17}$ 和 $\mathscr R_{28}$，全在低球；因此 (A.11)宽化为
$$
            \|v\|_{E_{20}}\le
                4\{X_{20}(h)+Z_{20}^{[3]}(f)\}.          \tag{A.12}
$$
J.11 的同一低阶两行递推从已证 $\mathscr Y_{64}$ 读取 $X_{20}$；所需源是1794阶、背景在1856内。没有调用一个尚未独立授予的 $s=8$ 网络尖窗。连同 (A.5)，可取
$$
 \boxed{\quad
 \|{\cal R}_u(f,b)\|_{E_{20}}
       +X_{20}(h)
       \le 2^{10485768}\,d_{1792}(f,b).
 \quad}                                                   \tag{A.13}
$$
这是真正包含 $\mathcal L_0v$ 的低图 norm。若 $f=S_TF$ 且 $F$ 在1794阶，则 (A.13) 不出现 $T^{1734}$。相反，完整 $E_{1856}$ 或更高读出仍使用下一节的有损估计；不能把 (A.13) 误说成整个迭代 norm 无损。

## 6. 完整高阶 graph tame界

令
$$
 {\cal H}^{E}_s
 =1+\|u\|_{E_{s+1796}}
      +\mathcal A_{s+1748}
      +\epsilon_L\mathcal D_{s+1748},
       \qquad64\le s\le6396 .                            \tag{A.14}
$$
固定外行的对应数值是已知有限常数。最高 source角阶8130、背景8192、外调用8144/其 state8176及 height8178都在 N/J 原窗口内。

J.15、(A.11)--(A.13)及 E.22 给
$$
 \boxed{\quad
 \|{\cal R}_u(f,b)\|_{E_s}+X_s(h)
 \le C_p\,d_{s+1732}(f,b)
        +C_h\,{\cal H}^{E}_s d_{1792}(f,b),
 \quad}
 \tag{A.15}
$$
其中明确固定
$$
                  C_p=2^{10485768},\qquad
                  C_h=2^{41943040}.                      \tag{A.16}
$$
为核余量，pure项至多是 J 的10485760加 source投影、graph吸收、参考态读回与最后状态和的8 bits。高项从37748736出发；E.22的16、一次 $K_E$、J.23的1572864以及低读出的组合只加在各对应项，不能将整个高常数反复相乘。最大的新增项为 $K_E\|u\|_{E_s}$ 乘 (A.13)，费用低于12600000 bits，故均严格小于41943040。high背景始终只乘低 source。

若保指定外源，(A.15)中的 $d$ 必须保其完整 $\mathfrak B$。特别独立 mean-height、cap 两 mean、实际 $f_*^{\rm src}$、原子及 $\nu$ 不能因其不是 ordinary body源而从估计中消失。

## 7. 精确缺陷的 tame窗

J.23 在同一个真实 $h$ 上给
$$
 \begin{split}
 Z_s^{[3]}(P_\perp{\cal E}_u[h])
 \le2^{1572864}\{&
 Z_{s+1}^{[3]}({\mathfrak F}(u))X_{16}(h)
 +Z_{17}^{[3]}({\mathfrak F}(u))X_s(h)\\
 &+(1+\mathscr R_{s+8})
       Z_{17}^{[3]}({\mathfrak F}(u))X_{16}(h)\}.
 \end{split}                                             \tag{A.17}
$$
$s+1$ 的角导数是真实损失。三个径向 source jets和完整 scalar mean均在该式，未知源仍给在 fixed-$t$。最高使用需 $s+8\le8192$，并另外满足 (A.15) 的6396上限。

(A.17)说明缺陷在零 body residual 的背景消失；不说明任意非零 residual 上可直接以 (A.15) 构造同域 Neumann。下一迭代必须同时利用低 source小量、高平滑和 (A.13)。

## 8. 不要求参数图 C∞ 的导数差

这里只使用 nonlinear residual map，不调用网络逆。E.15--E.21/E.25 的代数证明可在较大的 $\|u\|_{E_{20}}\le\rho_E$ 域重新实例：L 的值图只需低20阶，M小根的低分母只需对应四态，三个径向导数已有 $E_{20}$ 输入；$C_j^\#$ 和 E.19 的全 profile 不变。任意最高角阶仅作一次 one-high，完整 $k^s\|u\|_{E_{20}}^{k-1}$ 级数仍由同一个 $K_E$ 支付。这里不把 N 的 inverse或第二相位门扩张到这个大域。

因此 E.25 的统一二次 Fréchet余项在这个低20阶代数域足以给一次导数 Lipschitz估计。设 $u,\widetilde u$ 的 $E_{20}$ norm在该球四分之一内，$d=u-\widetilde u$，$v\ne0$。取
$t=\|d\|_{E_{20}}/\|v\|_{E_{20}}$。三次 Taylor展开分别在
$(\widetilde u,d+tv)$、$(\widetilde u,d)$、$(u,tv)$，
其低20阶 norm 均留在上述代数球；probe的1856阶不要求小，也不在probe处调用inverse。相减除 $t$，无需二阶参数导数，得到
$$
 \begin{split}
 Z_s^{[3]}((D{\mathfrak f}(u)-D{\mathfrak f}(\widetilde u))[v])
 \le16K_E\{&
 \|d\|_{E_{20}}\|v\|_{E_s}
       +\|d\|_{E_s}\|v\|_{E_{20}}\\
 &+(1+\|u\|_{E_s}+\|\widetilde u\|_{E_s})
       \|d\|_{E_{20}}\|v\|_{E_{20}}\}.
 \end{split}                                             \tag{A.18}
$$
$d=0$ 或 $v=0$ 的情形直接成立。完整 mean仍用 E.26，而不是把它的不同权投影交换。这里没有从第一参数的 $C^1$ 图推一个未证明的 $C^\infty$ tame图。

(E.21)、E.25和 (A.18)在某个有限 $E_b$ 上也成立，只要显示的阶数不超过 $b$。可先用 $S_T$、在较低 norm强收敛，并在每个固定片的高角 Hilbert norm用下半连续性传界；E的 closed graph识别同一分布极限。没有使用 Fourier多项式在 uniform全层最高 norm中必稠密的假设。

## 9. 实际高度方向与全部端口差

(A.7) 的 $v$ 是非mean高度方向。真正重建的总高度方向是
$$
                  \dot z=h+H_p+\dot\lambda .             \tag{A.19}
$$
$h$ 的 mean由真实 holonomy 切向补回；若 $h$ 已含所选 global常高度，则不再重复加 $\dot\lambda$。$H_p$ 是 G.14/J.19 的有向积分：
$$
 (H_p)_t=a_{\rm ph}w\{\dot\psi(1+\kappa)+\dot\kappa_p\},
              \qquad H_p(t_f)=0 .                        \tag{A.20}
$$
$\dot\kappa_p$ 保 G.12 的完整 metric/mean微分，绝不以0替代。

对任一真实物理边界或 matching行 $\mathscr C_e$，其实际增量必须取
$$
 D\mathscr C_e[\,h+H_p+\dot\lambda,\ \dot\gamma_1,\
                    \dot f_B,\ \dot C_R,\ \dot\nu,\ldots\,].
 \tag{A.21}
$$
只在该行正好是 (A.6) 已给的 fixed-metric线性行时，其中的 $h$ 部分等于 $b_e$。剩余量定义为准确端口缺陷
$$
 {\cal P}_{u,e}(v)
 =D\mathscr C_e[\,h+H_p,\dot\gamma_1,0,\ldots\,]
                    -{\cal B}^{\rm lin}_{u,e}h .          \tag{A.22}
$$
这是可逐原公式评价的完整列，不预设为小或0。good/raw transport、同物理角/密度变换和原外图 source坐标须依其真实合同读入；不能以一个局部 $C_R$ inverse替代它。

若一个端口确在全部第一参数 bump支集之外，则在那里
$\dot\psi=\dot\kappa_p=0$，所以 $H_p$ 是角常数且 $(H_p)_t=0$。
固定 metric 的 curvature和非mean state行不由这个常数产生额外项；真实 height行仍产生 $H_p(t_e)$。两个接在同一物理截面的高度差使用同一个连续有向积分，因此共同常数准确相消。不同外端之间却留下
$$
                  \Delta H_p=H_p(t_R)-H_p(t_L),           \tag{A.23}
$$
一般非零。位于 bump内的任何端口仍必须使用 (A.20)--(A.22)全式。

## 10. 唯一 global高度规范与不可删的荷

整个连通几何只有一个 rigid height常数 $\lambda$。可以规范一个真实参考端的平均高度；不能对每个胞元或两个外端各重置一次。若用 $\dot\lambda=-H_p(t_L)$ 抵消左端参数常数，右端仍为 (A.23)。它与 M 的独立 height/span 列、G.29 的两端真实 flux及 cap/long 的实际 mean行一起保留。

对指定 $\chi\ne0$ 的外源，M的 Volterra荷和 $\chi/w^2$ 斜率继续是独立列。它们不满足当前 holonomy-one图的 $\chi=0$ 恒等式，也不能以 $\Pi_A$ 自动消成 compatible源。若希望把这样的数据纳入同一个 nonlinear值图，必须另证实际 principal参数对 charged方向的识别，或者把该变化作为独立 affine principal列。

因此完整 augmented derivative的输出可明确写为
$$
 \left(
 f-P_\perp{\cal E}_u[h],\
 b+{\cal P}_u(v),\
 \dot z(t_L),\dot z(t_R),\
 \dot\pi(t_L),\dot\pi(t_R),\
 \hbox{原独立 mean/charge/参数列}
 \right),                                                \tag{A.24}
$$
每个 flux用真实原公式的全微分；不得仅用 $H_{p,t}=0$ 擅删本来独立给定的外荷。重复出现同一个 prescribed端值时只按其原匹配关系计一次，不把它伪装成两个独立数据。

(A.8)、(A.13)、(A.15)、(A.17)现已给出完整 body graph近似右逆及真实端口缺陷表。要使它成为全 nonlinear BVP 的近似右逆，还须对 (A.22)--(A.24) 的真实外返回、height/span、$\nu$ 和剩余参数列作实际 Schur，并验证初 residual 在同一完整 source域。不能先把这些行留在正文外，再称一次 body平滑迭代已经完成全局存在性。
