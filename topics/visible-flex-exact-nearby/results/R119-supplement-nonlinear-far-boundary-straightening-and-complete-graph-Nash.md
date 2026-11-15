# R119 续篇：真实 far 图的 collar straightening、完整 graph 右逆与保持匹配的 Nash 迭代

2026-11-15，visible-exact / tail_connector。

**状态：已完成分段独立核对的解析证明。** 固定同一个实际修补 M32 帽的真实内端输入 $\gamma$，本篇把它与同一个有限 long 的 nonlinear $B$ 图作为准确的值约束。一个固定正 collar 上的高度 lift 将该约束化为固定线性子空间。角平滑在这个子空间进行；每个实际重建成员的 far 高度、非mean slope 和 holonomy mean slope 都准确匹配。新 lift 造成的完整 ordinary 源及前三径向导仍计入 graph norm。

本篇不改变 metric 设计对象、第二参数、profile 或 source 单位；不重算任何数值。结论是固定 $\gamma$ 下的 exact tail--long--cap 外部解。它不选择 $\gamma$ 以完成 M32 core 的完整 $B,C$ 行及 waist/设计参数匹配。独立非零外荷不被当作 holonomy-one 方向。

使用已发表的完整原件：

* [E：固定参考 graph 与 smoothing](R119-supplement-reference-graph-scale-exact-residual-and-angular-smoothing.md)；
* [A：graph 近似右逆](R119-supplement-reference-graph-approximate-right-inverse-and-exact-port-defects.md)；
* [B：3500/400 finite Nash](R119-supplement-finite-Nash-iteration-in-reference-graph-with-port-conditions.md)；
* [G：新94真实 collar 种子](R119-supplement-new-94-B-collar-lift-and-actual-graph-seed.md)；
* [F：实际固定帽输入的外预算](R119-supplement-actual-cap-fixed-input-budget-and-body-Nash-entry.md)；
* [N：两层完整网络逆](R119-supplement-two-level-full-network-tame-inverse-and-complete-sources.md)；
* [J：三径source与loss1734](R119-supplement-three-radial-source-jets-four-state-jets-and-1734-loss.md)；
* [M：两输入零宽实际帽](R133-supplement-two-input-zero-width-cap-Phi-and-complete-inner-ports.md)；
* [O：实际帽--long tame与true DN](R133-supplement-actual-two-input-cap-long-tame-forms-and-physical-Poisson.md)；
* [HT：actual外行的完整high/source账](R119-supplement-actual-cap-outer-update-in-full-network-tame-and-source-windows.md)。

所有 $m\in4\mathbb Z$ 是实际物理角频率。$\Lambda=(1+D_\theta^2)^{1/2}$，$\langle\cdot\rangle$ 是同一物理角的归一平均。普通非mean投影 $P_\perp$、holonomy投影 $\Pi_A$ 和 conormal density投影 $P_\mu$ 从不混同。

## 1. 固定输入、准确残差和参考子空间

固定 F.2 的同一个 real-even、普通mean为0输入：
$$
 \|\gamma\|_{A_{\sigma_0}}\le r_\gamma/128,\qquad
 \sigma_0=2^{-13},\quad r_\gamma=10^{-9}.
 \tag{S.1}
$$
它不是第一参数 $\Gamma_1$。每轮保持同一 $\gamma$。
其 finite 高门也由完整 Fourier 矩得到：$k=0$ 直接用(S.1)；对 $1\le k\le8193$，用 $k!<2^{13k}$、$\sigma_0^{-k}=2^{13k}$ 和 Bessel 比，
$$
 \|\gamma/r_\gamma\|_{H^k}
 \le2^{27k+8}/128<2^{262144}.
 \tag{S.2}
$$
这里在8176以上没有继续使用不再适用的 $2^{12k}$ 阶乘界。

取 G 的同一 $B$，记 $t_B=0$、$s_B=a_Bw_B>0$。令实际 long 完整斜率值图为 $\mathscr K_\gamma(f)=\mathcal K(f,\Phi_\gamma(f))$，其 mean 保留在原 O/M 图内。置
$$
 \mathsf C_L=|D_\theta|\coth(L|D_\theta|)P_\perp,\qquad
 q_\gamma(f)=P_\perp\mathscr K_\gamma(f)+\mathsf C_L f .
 \tag{S.3}
$$
$\mathsf C_L$ 在本篇仅定义一个固定 Fourier 坐标；不把它当作原 true fixed-$C_R$ 网络外行。$q_\gamma(0)$ 一般非零，且 $Dq_\gamma(0)$ 一般非零。

给非mean高度 $u$，在同一真实 holonomy图中定义
$$
 f(u)=u(0)/s_B,\qquad k(u)=u_t(0)/s_B,\qquad
 b_\gamma(u)=k(u)-P_\perp\mathscr K_\gamma(f(u)).
 \tag{S.4}
$$
第一参数的 bump 在此 collar 及 B 外均为0，所以这里的 $s_B$、$q_{\rm phys}$ 和 profile 不随 $\Gamma_1^*(u)$ 变化。定义固定线性边界行及子空间
$$
 B_0u=k(u)+\mathsf C_L f(u),\qquad
 {\cal E}_{s,0}^+=\{u:B_0u=0\}.
 \tag{S.5}
$$
具体 norm 在第3节给出。这不是预设待解的实际 nonlinear 边界行。

## 2. 固定单 jet lift 与 nilpotent 坐标

沿用 G 的准确正 collar $-d\le t\le0$，$d=\ell_o=2^{-1024}$；全段 $Q<-3/4$，不碰任何 negative 输入、根邻域或两 $\Gamma$ bump。
取 G.15 的 $H_1$，即
$$
 H_1(s)=s(1-s)^6\sum_{\ell=0}^{4}\binom{5+\ell}{\ell}s^\ell .
$$
对普通mean为0的 $\xi$ 定义
$$
 ({\cal L}_\partial\xi)(t,\theta)
   =-d\,s_B\,\xi(\theta)H_1(-t/d),\qquad-d\le t\le0,
 \quad {\cal L}_\partial\xi=0\quad(t\le-d).
 \tag{S.6}
$$
它准确满足
$$
 f{\cal L}_\partial=0,\quad
 k{\cal L}_\partial=I,\quad
 B_0{\cal L}_\partial=I,\qquad
 \partial_t^a{\cal L}_\partial(-d)=0\quad(0\le a\le5).
 \tag{S.7}
$$
故内部不产生新状态跳或 source原子；在 B 不假装修好了所有高 jets。

现在定义
$$
 {\cal U}_\gamma(w)
       =w+{\cal L}_\partial q_\gamma(f(w)),
                       \qquad w\in{\cal E}_{s,0}^+ .
 \tag{S.8}
$$
因 $f{\cal L}_\partial=0$，
$$
 f({\cal U}_\gamma w)=f(w),\quad
 k({\cal U}_\gamma w)
  =-\mathsf C_L f(w)+q_\gamma(f(w))
  =P_\perp\mathscr K_\gamma(f(w)).
 \tag{S.9}
$$
所以 $b_\gamma({\cal U}_\gamma w)=0$ 准确成立，不是小量估计。

lift 在实际全部 negative 输入域上为0，故 L 的唯一 principal 值图给 $\Gamma_1^*({\cal U}_\gamma w)=\Gamma_1^*(w)$。这个等式用整个实际输入域，不仅用 B 处的零值。第二参数仍为 G 先固定的同一个值。

记 $F_Bw=f(w)$，并令
$$
 J_w=D{\cal U}_\gamma(w)
    =I+{\cal L}_\partial Dq_\gamma(f(w))F_B .
$$
由 $F_B{\cal L}_\partial=0$，准确有
$$
 J_w^{-1}=I-{\cal L}_\partial Dq_\gamma(f(w))F_B .
 \tag{S.10}
$$
这不是一个有损 Neumann 展开。对于已经满足 $b_\gamma(u)=0$ 的 $u$，反坐标是 $w=u-{\cal L}_\partial q_\gamma(f(u))$。

## 3. 真正多付一个端角导的固定 graph

采用 E 的同一 $\|\cdot\|_{E_s}$，另定义
$$
 \|w\|_{E_s^+}
    =\|w\|_{E_s}+2^{440}\|f(w)\|_{H^{s+3}},
                  \qquad20\le s\le8192 .
 \tag{S.11}
$$
这是新的固定线性 graph norm；没有从 $E_s$ 自动取得这额外一导。它保所有原层权、四个 scaled 径向 state jets、三个 source jets、内部 traces，并将 (S.5)作为闭线性条件。

G.19--G.20 的真实 $s_B/(aw)$ ratio及单侧 polynomial界给
$$
 \|{\cal L}_\partial\xi\|_{E_s^+}
     =\|{\cal L}_\partial\xi\|_{E_s}
     \le2^{2048}\|\xi\|_{H^{s+2}} .
 \tag{S.12}
$$
核费用只需：poly/Leibniz $64$ bits、ordinary source多一径导 $d^{-1}=2^{1024}$、finite权 $2^{440}$；总计1528 bits。角二导用于 $U$ 和参考 source；不是从有限 Fourier支持省掉。额外端项为0，因 $f{\cal L}_\partial=0$。

$S_T=\mathbf1_{\Lambda\le T}$ 与所有径向参考项、$F_B$、$ {\cal L}_\partial$、$\mathsf C_L$ 和 $B_0$ 准确交换。因此 $E_{s,0}^+$ 完备，且
$$
 \|S_Tw\|_{E_b^+}\le T^{b-a}\|w\|_{E_a^+},\qquad
 \|(I-S_T)w\|_{E_a^+}\le T^{a-b}\|w\|_{E_b^+}.
 \tag{S.13}
$$
没有以 $\Gamma$ 或 nonlinear mean 的变动坐标进行平滑。

## 4. 只重收实际 slope 值图所需的8193角窗

本节不扩大 N 的 $q\le8128$ 网络窗。需要的是 normalized slope 值图 $|D|q_\gamma$ 的有限 Sobolev窗，因为 (S.12)在 $s=8192$ 要求 $q_\gamma(f)\in H^{8194}$。

M.16/O.12 的已证完整 mixed Taylor核在零宽输入 $(G,U)=(\gamma/r_\gamma,|D|^2f/r_B)$ 上直接适用，$r_B=2^{-60}$。long 的原 $A^2\to A^1$ 值界先对输出乘 $|D|$。其 Taylor核仍满足完整 signed-lag 列和；未知 $f$ 没有复角取值。全部非mean输入、所有 mean输出以及 cap--long反射项在推核时保留，只在最终 (S.3) 选择非mean slope。

将这个同一个核的 one-high 证明重收到 $0\le r\le8193$。first/second difference只增至多四个 Taylor次数因子；所需矩可取 $p\le r+4\le8197$。此时 $p!<2^{13p}$，而 $h=2^{-15}$，所以完整 lag矩和次数矩分别由 $2^{p+3}p!h^{-p-1}$ 与 $p!2^{p+1}$ 控制。六次 scalar/Young组合、两次有限差及完整 signed/mean因子的费用小于
$$
                 C_r^\partial=2^{512(r+32)+262144}.
 \tag{S.14}
$$
最高指数为4473344。相比 O 原 $48(r+32)+8192$ 的单组账，这里每个阶乘多付一bit/阶、至多四个次数因子以及全部 normalization；每组可用 $64(r+32)+8192$，六组加固定费用仍严格在(S.14)内。这是一次完整核求和，不按每个 Taylor项反复乘整个高常数。

O.5 的二次零点给纯 $f$ 子族的一高界；O.6--O.9给其它子族准确的 $\epsilon=e^{-7L/4}<2^{-57000000}$。恢复真实 $f$ 时至多保 $r_B^{-2}\epsilon=2^{120}\epsilon$；不能把这项记成一份不存在的 $f$。更明确地，令 $F_r=\|f\|_{H^{r+2}}$、$G_r=1+\|\gamma/r_\gamma\|_{H^r}$，则(S.14)包含
$$
 \|q_\gamma(f)\|_{H^{r+1}}
 \le C_r^\partial\{F_1F_r+2^{120}\epsilon(G_r+F_r)\}.
$$
一阶差和二次余项按同一核保一份 highest norm；纯 $f$ 项至少保两个真实 $f$ 或方向因子，pure $\gamma$ 部分仍带 $\epsilon$。

(S.2)、(S.12)、(S.14)及有限固定和可统一收进
$$
                         K_\partial=2^{6291456}.
 \tag{S.15}
$$
实际最大账小于 $4473344+262145+120+8192+32<6291456$。
于是，固定(S.1)后，对 $20\le s\le8192$ 有
$$
 \|{\cal U}_\gamma(w)-w\|_{E_s^+}
 \le K_\partial\{
       \|w\|_{E_{20}^+}\|w\|_{E_s^+}
                  +\epsilon(1+\|w\|_{E_s^+})\}.
 \tag{S.16}
$$
其一阶差、二次余项和导数差保相同的 one-high形式。例如 $J_w-I$ 的最高方向乘 $K_\partial(\|w\|_{E_{20}^+}+\epsilon)$，高背景只乘低方向；(S.10)有完全相同结构。证明只用 $r=s+1$ 的输入 $f\in H^{s+3}$，最高为8195，恰是 (S.11)的8192端项；没有要求整个 state有8195阶。

固定新的低球
$$
 \rho_+=2^{-33554432},\qquad
 \|w\|_{E_{1856}^+}\le\rho_+/2 .
 \tag{S.17}
$$
$K_\partial\rho_+=2^{-27262976}$，且 $K_\partial\epsilon<2^{-50708544}$。所以实际 $u={\cal U}_\gamma w$ 仍在 A/F/N 的原低球严格内部；高 norm只需有限。实际外图的 F.8及 O/HT全部低门继续成立。

## 5. 真实 far 切向行与同一个 complete proxy

先给不要求背景已经匹配的准确恒等式。写 $\mu_T,d_T$ 与 $\mu_L,d_L$ 为 B 两侧当前真实量，
$$
 \pi_T(h)=\mu_T(h_t-d_Th_\theta),\qquad
 {\cal N}_Bh=-\mu_L\{D_f\mathscr K_\gamma\,P_\perp h-d_Lh_\theta\}.
$$
原 P.7/I.6a 是
$$
 {\cal E}_B=P_{\mu_T}\{
     -(\mu_T/\mu_L-1){\cal N}_BP_\perp
                  +\mu_T(d_L-d_T)\partial_\theta\},
$$
$$
 P_{\mu_T}z=z-\frac{\mu_T}{\langle\mu_T\rangle}\langle z\rangle .
 \tag{S.18}
$$
在 holonomy-one切向，$\langle\pi_T(h)\rangle=0$、$\langle{\cal N}_Bh\rangle=0$。直接代入而不先删 $D_f\mathscr K$ 的mean，得
$$
 (\pi_T+{\cal N}_B-{\cal E}_B)h
 =P_{\mu_T}\{\mu_T(h_t-D_f\mathscr K_\gamma P_\perp h)\}
 =P_{\mu_T}\{\mu_Ts_B\,Db_\gamma(u)[P_\perp h]\}.
 \tag{S.19}
$$
对普通mean零的 slope源 $\xi$，映射 $\xi\mapsto P_{\mu_T}(\mu_Ts_B\xi)$ 是到普通mean零 density源的双射；其反向为 $s_B^{-1}P_\perp(\beta/\mu_T)$。这不是对独立非零通量荷的投影许可。

在(S.8)的实际背景上，四态 $P,U,K_\perp,V$ 已相同；同一 holonomy 小根给 $\kappa_T=\kappa_L$。因而 $\mu_T=\mu_L,d_T=d_L,{\cal E}_B=0$。一般未匹配成员仍必须使用(S.18)。这里不以仅非mean slope相同代替 mean小根唯一性。

令 $u={\cal U}_\gamma w$，$H$ 为 A 的 same-background complete body proxy解，$v_U={\cal R}_u(g,0)=P_\perp H$。其原真实 homogeneous B行与(S.19)给 $Db_\gamma(u)v_U=0$。参数 lift $H_p$ 在这个 collar角常数且 $(H_p)_t=0$，不改变这条 nonmean行；同截面的 mean-height仍用同一个连续积分。

定义
$$
 \widehat{\cal R}_w g=J_w^{-1}v_U .
 \tag{S.20}
$$
由 $Dq_\gamma=D(P_\perp\mathscr K_\gamma)+\mathsf C_L$，准确有 $B_0\widehat{\cal R}_wg=0$。故它是固定子空间的真正方向，而不是取一步后再投影产生新缺陷。

记
$$
 {\cal F}_\gamma(w)=\mathfrak f({\cal U}_\gamma w).
$$
同一个 $H$ 与原A缺陷给
$$
 \boxed{\quad
 D{\cal F}_\gamma(w)\widehat{\cal R}_wg
              =g-P_\perp{\cal E}_{u}[H].
 \quad}
 \tag{S.21}
$$
$\Gamma_1$的 derivative由负输入相同而准确识别。不对 $H_p$ 再收一次 $ {\cal E}$，也没有新增 far边界缺陷。完整 nonlinear mean仍为 $\Pi_{A_u}{\cal F}_\gamma$，其微分保 $D\Pi_{A_u}\,{\cal F}_\gamma$。

## 6. 额外端trace由实际两行恢复，不能从旧norm猜

这是(S.20)进入 $E_s^+$ 的新门。在严格正 collar，按 J.6 写同一个真实 proxy两行：
$$
 p_t=V+(Q-1)p,\qquad
 k_t=F_UU+F_VV+C_pp+C_kk+e,
$$
$$
 C_p=F_P+\beta\mathfrak r_\theta+\gamma_{\rm alg}\mathfrak r,\qquad
 C_k=F_K-\alpha\mathfrak r .
$$
$\gamma_{\rm alg}$ 是 J 的系数，不是帽输入；$e$ 是原有限 ordinary源。这里 $\Gamma$源在支集之外准确为0。

对第二行取 $\theta$ 导，再用 $V_\theta=U_t-(Q-1)U$，得
$$
 \begin{split}
 F_U p_{\theta\theta}={}&
 V_t-F_V[U_t-(Q-1)U]-F_{U,\theta}U-F_{V,\theta}V\\
 &-C_pU-C_{p,\theta}p-C_kV-C_{k,\theta}k-e_\theta .
 \end{split}
 \tag{S.22}
$$
所有右侧 $U_t,V_t$ 都是 J/E 已付的一侧普通 jets。scaled转回只付 $d^{-1}=2^{1024}$。source只要 $H^{s+1}$，不是给未知 $H$ 多索一角。

$F_U=Q+O(P,U,K,V)$，低球和 $Q<-3/4$ 给 $F_U<-1/2$。其 inverse 的高乘法界由 C.9a/N.5 的完整几何级数及 J.10 的 same-collar finite coefficients取得：最高方向用低 multiplier，高系数只乘低方向。对 $s\le6396$，全部 $C_p,C_k$ 的 $\mathfrak r_{\theta\theta}$、$F_U^{-1}$、一次角导及乘法费用可宽取 $2^{524288}$。具体为 J 的262144、N近远乘法少于131072、有限径向1024以及至多4096的固定读出，仍留125000以上bits。所需背景至 $s+8$，source至 $s+1$，未超过原 A/J窗口。

在 B，$aw=s_B$，故 $p_{\theta\theta}=f_B(H)_{\theta\theta\theta}$。非mean物理频率的 $\langle m\rangle^3/|m|^3<2$ 给
$$
 \begin{split}
 2^{440}\|f_B(H)\|_{H^{s+3}}
 \le2^{524288}\{&
 X_s(H)+Z_{s+1}^{[3]}(g)\\
 &+(1+\|u\|_{E_{s+8}})X_{16}(H)\}.
 \end{split}
 \tag{S.23}
$$
普通mean高度不由此式控制；它仍是原独立规范/输出。本式使用 $2^{440}$ 同时乘 state和ordinary source；没有遗留一个裸 $s_B^{-1}$。

将(S.23)、(S.10)代入 A.13/A.15及 F.12，可用以下确定的完整常数：
$$
 \|\widehat{\cal R}_wg\|_{E_{20}^+}+X_{20}(H)
          \le2^{16777216}|g|_{1794},
$$
$$
 \|\widehat{\cal R}_wg\|_{E_s^+}+X_s(H)
 \le2^{16777216}|g|_{s+1734}
  +2^{67108864}(1+\overline B_\gamma)^2
          (1+\|w\|_{E_{s+1796}^+})|g|_{1794},
 \quad64\le s\le6396 .
 \tag{S.24}
$$
$\overline B_\gamma<2^{2097152}$ 是 F 的同一固定数据。trace新费、$J_w^{-1}$ 的一次高插入及 $ {\cal U}_\gamma$ 的一次高背景都只乘低source。即使将 A高常数41943040、trace524288、两份6291456及有限和全部相加，仍小于(S.24)的67108864；pure项只用低 $J_w^{-1}<2$，实际10485768+524288加固定读出小于16777216。source loss1734、背景1796和最高8192完全不变。


## 7. 固定 affine、固定线性和真正二次项分别记账

在同一个固定坐标空间内定义
$$
 c_\gamma={\cal F}_\gamma(0),\qquad
 {\cal B}_\gamma=D{\cal F}_\gamma(0)-{\cal L}_0,\qquad
 {\cal N}_\gamma(w)
  ={\cal F}_\gamma(w)-c_\gamma-({\cal L}_0+{\cal B}_\gamma)w .
 \tag{S.25}
$$
所以 $ {\cal N}_\gamma(0)=D{\cal N}_\gamma(0)=0$。
其中 $c_\gamma$ 和 $ {\cal B}_\gamma$ 是固定 $\gamma$ 下的真实量；
$ {\cal B}_\gamma$ 一般非径向，不与 $S_T$ 交换。
取
$$
 K_+=2^{25165824}.
$$
(S.16)、E.21/E.25与A.18的三次Taylor恒等，给
$$
 \|c_\gamma\|_{Z_s^{[3]}}
   +\|{\cal B}_\gamma:E_s^+\longrightarrow Z_s^{[3]}\|
      \le K_+\epsilon,\qquad
 \|{\cal N}_\gamma(w)\|_{Z_s^{[3]}}
      \le K_+\|w\|_{E_{20}^+}\|w\|_{E_s^+},
 \quad20\le s\le8192 .
 \tag{S.26}
$$
这里 $D{\mathfrak f}(0)={\cal L}_0$ 是原E.21的准确二次零点；
新基点为 $ {\cal U}_\gamma(0)={\cal L}_\partial q_\gamma(0)$。
把A.18在这两个真实基点相减即得(S.26)的线性部分。
它使用完整 $q_\gamma(0),Dq_\gamma(0)$ 的 $\epsilon$ 界，
没有把两者设为0，也没有将其norm要求为 $T_0^{-3000}$。

为核完整常数，可先保E/A的 $K_E=2^{2097152}$，
再最多三次使用(S.15)；实际指数
$$
 2097152+3\cdot6291456=20971520<25165824
$$
仍留4194304 bits支付有限和、16倍三Taylor及 mean投影。
最高阶只分给一个因子，没有产生两个最高背景norm。
特别地，同一次E.25/A.18计算给出需要用于平滑差的真实导数界
$$
 \|D{\cal N}_\gamma(w)h\|_{Z_s^{[3]}}
 \le K_+\{\|w\|_{E_{20}^+}\|h\|_{E_s^+}
                 +\|w\|_{E_s^+}\|h\|_{E_{20}^+}\}.
 \tag{S.26a}
$$
A.18额外的低低项由 $\|w\|_{E_{20}^+}\le1$、
$\|w\|_{E_s^+}\ge\|w\|_{E_{20}^+}$ 吸入这两项，
全部固定因子使用刚列的4194304-bit储备。
这不是仅由(S.26)的值界猜测导数界。
同样，若 $w,w+h$ 在低球内，
$$
 \begin{split}
 \|{\cal N}_\gamma(w+h)-{\cal N}_\gamma(w)
           -D{\cal N}_\gamma(w)h\|_{Z_s^{[3]}}
 \le K_+\{&
 \|h\|_{E_{20}^+}\|h\|_{E_s^+}\\
 &+(1+\|w\|_{E_s^+})\|h\|_{E_{20}^+}^2\}.
 \end{split}
 \tag{S.27}
$$
一次导数差使用A.18的同一三Taylor方法，费用至多 $16K_+$；
高背景仍只乘两个低方向。不声称第一参数图具有未付的二阶或无限阶导数。

现在真正计算平滑交换。准确有
$$
 \begin{split}
 {\cal F}_\gamma(S_Tw)-S_T{\cal F}_\gamma(w)
   ={}&(I-S_T)c_\gamma
       +[{\cal B}_\gamma,S_T]w\\
      &+{\cal N}_\gamma(S_Tw)-S_T{\cal N}_\gamma(w),\\
 [ {\cal B}_\gamma,S_T]w
   ={}&{\cal B}_\gamma(S_T-I)w
                  +(I-S_T){\cal B}_\gamma w .
 \end{split}
 \tag{S.28}
$$
每个固定线性项都先使用(S.26)在同阶固定graph上的真实界，再用(S.13)。
这个阶段不需要把 $ {\cal B}_\gamma$ 当成Fourier对角；
其同阶界已在第4节由完整known-lag核、额外端迹与lift支付。
对 $20\le a<b\le8192$，所得全式为
$$
 \begin{split}
 \|{\cal F}_\gamma(S_Tw)-S_T{\cal F}_\gamma(w)\|_{Z_a^{[3]}}
 \le4K_+\{&
 T^{a-b}[\epsilon(1+\|w\|_{E_b^+})
                  +\|w\|_{E_{20}^+}\|w\|_{E_b^+}]\\
 &+T^{20-b}\|w\|_{E_a^+}\|w\|_{E_b^+}\}.
 \end{split}
 \tag{S.29}
$$
$a+1<b$ 时照同式代入 $a+1$。它完整保留固定affine tail和非径向线性交换子。
最高 $b+1$ 窗只对 $S_Tw$使用，不索取未给的 $w\in E_{b+1}^+$。
若某一步 $ {\cal F}_\gamma(w)=0$，本篇的校正源准确为0；
(S.28)是背景估计，不是另加一份固定forcing的迭代规则。

## 8. 同一实际种子的准确反坐标及确定的常数门

使用G已经构造的同一实际种子
$u_{\rm seed}=u^\dagger+\ell_B$。它在B满足(S.4)的真实值行。
定义
$$
 w_0=u_{\rm seed}
            -{\cal L}_\partial q_\gamma(f(u_{\rm seed})).
 \tag{S.30}
$$
由(S.7)--(S.9)，$B_0w_0=0$ 且
$ {\cal U}_\gamma(w_0)=u_{\rm seed}$ 准确成立。
第一参数输入逐点不变；其 holonomy mean和metric也是原种子的同一份，
不是两个近似对象之间作norm比较。

G.21的端点读数具有剩余角宽大于8198。
此处只把B端 $\Lambda^{8194}$ 换为 $\Lambda^{8195}$；
因物理 $m\ne0$ 时 $\Lambda_m\le e^{|m|}$，
仍由该同一完整解析norm控制，不提高全网络的角窗口。
包括 $2^{440}$ 的finite权后，可宽取
$2^{440}\|f(u_{\rm seed})\|_{H^{8195}}<2^{-54866000}$。
结合G.26、(S.16)、$\epsilon<2^{-57000000}$，得到
$$
 \|w_0\|_{E_{8192}^+}<2^{-50000000},\qquad
 \|{\cal F}_\gamma(w_0)\|_{Z_s^{[3]}}
 =\|\mathfrak f(u_{\rm seed})\|_{Z_s^{[3]}}
 <2^{-5275847456},\quad0\le s\le6396 .
 \tag{S.31}
$$
后一式是准确坐标恒等式后直接消费G.28，未把两个较粗绝对界相减。
$ {\cal U}_\gamma(w_0)$ 中的affine项自身只有(S.26)的 $\epsilon$ 尺度；
(S.31)的小残差依赖实际种子，而非该affine项单独极小。

固定
$$
 a=1856,\quad b=6396,\quad b-a=4540,\qquad
 C_+=2^{167772160}(1+\overline B_\gamma)^8,\qquad
 T_0=2^{1500000}.
 \tag{S.32}
$$
单步中至多出现两份(S.24)的高逆常数及一次(S.27)/(S.29)；
其最大指数
$2\cdot67108864+25165824=159383552<167772160$。
剩余8388608 bits包括source投影、参数/mean读出、有限和及所有16倍因子。
$\overline B_\gamma$只来自固定数据；变化的高背景继续明确保留。
由 $\overline B_\gamma<2^{2097152}$，
$$
 \begin{split}
 \log_2(16C_+)&<184549388<189000000
                         =\log_2 T_0^{126},\\
 \log_2(16C_+/\rho_+)&<218103820<1899000000
                         =\log_2 T_0^{1266}.
 \end{split}
 \tag{S.33}
$$
(S.31)同时给 $\|w_0\|_{E_a^+}<\rho_+/8$、
$1+\|w_0\|_{E_b^+}+\|{\cal F}_\gamma(w_0)\|_{Z_b^{[3]}}<T_0$
以及 $\|{\cal F}_\gamma(w_0)\|_{Z_a^{[3]}}<T_0^{-3000}$。
这里 $4500000000<5275847456$；所有数均为同一真实种子的单位。


## 9. 保持实际far图的3500/400归纳

令
$$
 \begin{split}
 T_n&=T_0^{(5/4)^n},\quad v_n=S_{T_n}w_n,\quad
 F_n={\cal F}_\gamma(w_n),\\
 h_n&=-\widehat{\cal R}_{v_n}(S_{T_n}F_n),\qquad
 w_{n+1}=w_n+h_n,\qquad
 u_n={\cal U}_\gamma(w_n).
 \end{split}
 \tag{S.34}
$$
不在 $h_n$ 外再加第二次 $S_{T_n}$。由(S.20)，
$B_0h_n=0$，故所有 $w_n,v_n$ 都在固定线性子空间；
由(S.9)，每一个 $u_n$ 和用于proxy的 $ {\cal U}_\gamma(v_n)$
都满足同一个完整nonlinear far值图。

B.14--B.25的归纳取(S.24)、(S.27)、(S.29)与 $C_+$ 重新实例。
这里逐项说明新增项没有被略过。若 $T=T_n$，
原归纳量给 $\|w_n\|_{E_b^+}\le T^{2800}$、
$|F_n|_b\le T^{320}$、$|F_n|_a\le T^{-3000}$。
(S.29)在20阶的固定affine/linear及二次项均不超过
$C_+T^{20-b+2800}=C_+T^{-3576}$；
在 $a+1$ 阶不超过 $C_+T^{a+1-b+2800}=C_+T^{-1739}$。
纯affine tail甚至不带 $T^{2800}$。
因此完整当前mean投影后仍有
$$
 |\mathfrak F({\cal U}_\gamma(v_n))|_{17}\le C_+T^{-3000},
 \quad
 |\mathfrak F({\cal U}_\gamma(v_n))|_{a+1}\le C_+T^{-1739},
 \quad
 |\mathfrak F({\cal U}_\gamma(v_n))|_{b+1}\le C_+T^{2801}.
 \tag{S.35}
$$
最后一式只在真实平滑成员上用(S.25)--(S.27)及(S.13)，
固定 $c_\gamma$ 的高阶值仍由(S.26)单独支付。
不把两种holonomy权投影交换。

低校正由1794阶源直接读出，故
$\|h_n\|_{E_{20}^+}+X_{20}(H_n)\le C_+T^{-3000}$。
其1856阶界仍为 $C_+T^{-1266}$；最高阶保留
$C_+T^{3274}$，background项为 $C_+T^{1596}$。
使用(S.21)的真实负源 $H_n$，
准确残差递推为
$$
 \begin{split}
 F_{n+1}={}&(I-S_T)F_n
 +[D{\cal F}_\gamma(w_n)-D{\cal F}_\gamma(v_n)]h_n\\
 &-P_\perp{\cal E}_{{\cal U}_\gamma(v_n)}[H_n]
 +{\cal F}_\gamma(w_n+h_n)-{\cal F}_\gamma(w_n)
                 -D{\cal F}_\gamma(w_n)h_n .
 \end{split}
 \tag{S.36}
$$
(S.25)中的 $c_\gamma$ 在这个等式中准确消去，固定
$ {\cal B}_\gamma$ 亦在导数差中消去；它们已经通过(S.29)进入了
(S.35)，没有被漏掉。

低阶六项的最坏幂仍为
$-4220,-4266,-4740,-4842,-4739,-4266$；
额外高背景低方向项仍小于 $C_+T^{-5994}$。
高阶保留原投影尾的准确系数1：
$|F_{n+1}|_b\le T^{320}+C_+T^{274}$。
最高校正的3274与目标3500之间留226幂，
高新余项274与400之间留126幂；
原tail320与400之间的80幂不带 $C_+$。
(S.33)分别支付这些门，因而归纳给
$$
 \begin{gathered}
 |F_n|_a\le T_n^{-3000},\qquad
 \|w_n\|_{E_b^+}\le T_{n-1}^{3500},\qquad
 |F_n|_b\le T_{n-1}^{400},\\
 \|w_n\|_{E_a^+}\le\rho_+/4,\qquad
 \sum_n\|h_n\|_{E_a^+}
       \le2C_+T_0^{-1266}\le\rho_+/8 .
 \end{gathered}
 \tag{S.37}
$$
最高background仍为 $b+1796=8192$，最高source为
$b+1734=8130$；第4节新增8193窗只用于端点值图及(S.11)，
不把它转授为整个网络的8193阶inverse。
每次先验证低球，再使用high有限界，次序与原B相同。

## 10. 极限、曲率mean及全几何范围

(S.37)与固定graph的完备性给
$w_n\to w_\infty$ 于 $E_{1856,0}^+$。
(S.16)及其一次差给同一真实
$u_\infty={\cal U}_\gamma(w_\infty)$，
并且
$$
 \mathfrak f(u_\infty)=0,\qquad
 \mathfrak F(u_\infty)=
          \Pi_{A_{u_\infty}}\mathfrak f(u_\infty)=0,\qquad
 b_\gamma(u_\infty)=0 .
 \tag{S.38}
$$
这里还取得相对于实际种子的确定强小量。
由(S.30)、(S.37)，以及(S.16)在1856低球上的 Lipschitz常数小于2，
$$
 \|u_\infty-u_{\rm seed}\|_{E_{1856}}
 \le4C_+T_0^{-1266}<2^{-1700000000}.
 \tag{S.39}
$$
因为 $\log_2(4C_+)<184549386$，
而 $1266\log_2T_0=1899000000$。
这里比较的是同一个 $\gamma$、同一个真实种子的重建高度；
不把(S.26)中的固定affine项单独当作这份小误差。

完整mean由实际holonomy重建保留，不是从普通mean为0推出。
B处 $f$ 和非mean slope相同，故 $P,U,K_\perp,V$相同；
同一holonomy小根再给完整mean slope相同。
这些是在同一个实际物理角上的值。

选择唯一整体高度常数 $\lambda$，使这个同一B截面的mean-height
与cap--long相同。其余mean-height由原一次有向积分决定，
没有每片重置。参数lift在该截面两侧使用同一个积分，
所以共同常数准确相消；跨端的实际span与 $H_p$ 仍保留为几何输出。
当两侧都满足原准确PDE后，真实一侧公式恢复所需 $C^2$ jets；
原 $Q^{(3)}$ 在B的跳以及高度五阶的broken口径没有被抹掉。
本次 graph 足以直接支付高度在无限深端的物理 $C^2$ 平延；
不需要将旧 D 的独立 root/source域条件冒充为本次输入。
准确原件是 [J](R119-supplement-three-radial-source-jets-four-state-jets-and-1734-loss.md)
J.13 的物理读出、
[有限Sobolev mean图](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md)
M.1--M.4、M.28--M.30、
[原controlled profile](R119-supplement-controlled-profile-full-label-and-raw-ports.md)
C.2、C.6--C.7，以及
[强深规范](R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md)
U.2。具体证明如下。

令 $R=16\|u_\infty\|_{E_{1856}}$，$J_j=j+5$。
E.22对当前实际 metric 给
$\|(P,K,U,V)\|_{H^2}\le C_jR$、
$\|\partial_tK\|_{H^2}\le\ell_j^{-1}C_jR$。
普通非mean投影的范数为1；所以同样控制 $K_\perp$ 及其径导。
由 $u_\infty=a_{\rm ph}wI_\theta P$ 和J.13，
$$
 \begin{split}
 (u_\infty)_\theta&=a_{\rm ph}wP,\qquad
 (u_\infty)_t=a_{\rm ph}wK_\perp,\\
 (u_\infty)_{tt}
 &=a_{\rm ph}w\{(K_\perp)_t+(A+1)K_\perp\},
 \qquad A=(\log w)_t=-Q .
 \end{split}
$$
同一单位下 $a_{\rm ph}w\le\rho2^{130}\mu_j\delta_j^{-1}$，
$\ell_j^{-1}=2^{64}J_j^2\delta_j^{-4}$ 吸收 $1+|Q|$；
$1\le r\le2$ 及 $H^2(S^1)\hookrightarrow C^0$ 的固定费用给
$$
 \begin{split}
 \|u_\infty\|_{C^2_{r,\theta}(I_j)}
 &\le \rho\,2^{256}J_j^2\mu_jC_j\delta_j^{-5}R\\
 &\le \rho\,2^{512}J_j^2h_j^{-5}\zeta_j\delta_j^{-7}R
 \longrightarrow0 .
 \end{split}
 \tag{S.40}
$$
在 $j>8192$，完整 profile为
$h_j=8\delta_j^{1/256}$、
$\zeta_j=\varepsilon_s\delta_{8192}^{-485/4}\delta_j^{131}$；
(S.40)的净深幂是 $124-5/256>0$。
固定前缀和 $\delta_{8192}^{-485/4}$ 留在原常数中；
没有把它们重设为1。

完整mean也单独保留。因(S.38)给真实普通源 $N=0$，
M.11、M.28、M.30适用于本次已经解出的完整方程，得到
$$
 \begin{split}
 |\kappa|&\le2^{10}C_j^2R^2,\qquad
 z_{\rm mean}(t)-z_{\rm rad}(t)
       =\int_{t_f}^{t}a_{\rm ph}w\kappa\,ds,\\
 \|z_{\rm mean}-z_{\rm rad}\|_{C^2_r(I_j)}
 &\le\rho\,2^{512}J_j\mu_jC_j^2\delta_j^{-5/2}R^2
 \longrightarrow0 .
 \end{split}
 \tag{S.41}
$$
这里 $z_{\rm rad}=\lambda+\int_{t_f}^{t}a_{\rm ph}w\,ds$，
深幂为 $251-10/256>0$；没有删去 mean slope 或每层重置高度。
径向baseline本身满足
$(z_{\rm rad})_r=\rho w$、
$(z_{\rm rad})_{rr}=\rho w_r$；
原C.7使这两者趋于0，并由完整未来层积分得到
$z_{\rm rad}\to\lambda$。
因此总高度 $z=u_\infty+z_{\rm mean}$ 的一、二阶物理导数都趋于0。
这里 $\rho>0$ 是固定的实际安装尺度，$a_{\rm ph}=\rho r$，
故真正物理径向 jets准确为
$$
 z_a=\rho^{-1}z_r,\qquad z_{aa}=\rho^{-2}z_{rr},
 \qquad z_{a\theta}=\rho^{-1}z_{r\theta}.
$$
前三式连同未变的角二导 $z_{\theta\theta}$ 都趋于0；径向baseline更直接满足
$(z_{\rm rad})_a=w$、$(z_{\rm rad})_{aa}=\rho^{-1}w_r$。
实际平端半径 $a_{\rm flat}=\rho r_f\ge\rho>0$，
从这些 polar jets 到 Cartesian二jet只再付固定
$2^8\max\{1,\rho^{-2}\}$。不将安装 $r$ 的导数误记成物理 $a$ 的导数。
原线性trace约束、(S.38)的普通方程及真实系数连续性给有限接缝
两侧的相应二jet相等；broken高jet从未当作这个结论的替代。
于是本次 $E_{1856}^+$ 球和完整零 residual已经蕴含
**标量高度在真实平端的 $C^2$ 常数延拓**。

这个结论不单独证明整张空间 immersion 的 frame、axis、
无自交、reach或markers条件。那些结论还须用准确coframe重建及
全局几何门；尤其M32 core内端的完整曲率matching尚在本篇范围外。

[原完整物理迹匹配与waist反射](R133-supplement-full-physical-trace-matching-and-waist-reflection.md) M.3--M.11
允许从一个上半体的一次frame/位置积分，再按真实waist反射安放下半体。
在当前没有预先指定两个世界锚的构造中，
两条曲率mean是真matching数据；mean-height的同截面匹配只用一个初值，
总span/轴向相对位置是输出和几何预算。
本篇不把一般指定的两端height或非零flux荷自动转入这个holonomy-one图。

因此本篇对固定(S.1)输入完成了实际tail body与真实cap--long
far图的同时求解。尚未据此选择 $\gamma$ 使帽在内端与M32 core的
完整 $B,C$（包括两条曲率mean）匹配；
waist及intrinsic设计参数的真实行也未被本篇消去。
(S.1)是固定输入的正宽解析门，未证明一般core有限Sobolev trace
自动属于该门；不能仅凭M/O的零宽值图将这里的种子存在量词扩大。
有限97端口的成功不替代这些无限/mean行。
得到最终单个全闭几何后，intrinsic参数先全部冻结，
原几何圆作用与固定markers给同一metric的族；
这里不把 $\nu$ 的intrinsic变化误称为flex参数。


## 11. 独立域扩张：固定物理 $H^{8193}$ 输入，而不要求正解析宽

本节是第1--10节解析输入结论之外的一个新定理。
它消费已经独立发表的
[RG：粗内曲率与真实B端解析种子](R119-supplement-rough-inner-curvature-data-and-true-smoothed-B-seed.md)
RG.2--RG.31。
RG原正文blob为 aa7fb26396cba7d41ff602d8f2ca0b5727ab7f0f，
SHA256为90acb31ed42fcfc8b32a7a5d3a467630c578a786527469ed5d49585e6339305b。
以下只替换固定输入门和实际种子的来源；
原(S.1)结论仍保留自己的准确量词，不静默改写。

固定同一个真实物理角上的 real-even、普通mean为0函数 $\gamma$，
现在只要求
$$
 \|\gamma/r_\gamma\|_{A_0}\le1/128,\qquad
 \|\gamma/r_\gamma\|_{H^{8193}}\le2^{1048576},
 \qquad r_\gamma=10^{-9}.
 \tag{S.42}
$$
$A_0$ 是完整无指数权的Wiener范数。
第一条是实际帽值域的小门，第二条是新增的真实有限高门；
两者都不宣称 $\gamma$ 有任何正角解析宽。
尤其不能从RG.31/F.1仅有的 $H^{8176}$ 条件自动取得第二条。

$\gamma$ 始终是物理内端曲率输入，不是第一参数 $\Gamma_1$，
不是intrinsic设计 $\nu$，也不是一般 $H^{-3/2}$ 线性方向。
每个固定 $\gamma$ 使用RG给出的同一个真实种子，
再冻结与该种子对应的第二参数。
Nash过程中保持这两者不变，只使用既有唯一第一参数值图。

**同一实际种子由分离端平滑给出。**
M.3的零宽实际值图在完整product域
$\|\gamma\|_{A_0}<r_\gamma$、
$\||D|^2f_B\|_{A_0}<r_B$ 中存在。
固定(S.42)后，$f_B$半球Cauchy导数来自这个product域；
没有将未知 $\gamma$ 平移到复角。

RG.9--RG.22将真实两端long Green的帽端宽设为0：
$f_B=0$的incoming图在B取 $7L/16$，
完整mixed图在B取真实 $s_\beta$，其斜率 $s_\beta/L<1/32$。
后者的完整双端module保两mean、真实反射、
$320$/$5/8$门以及 $44\epsilon$ 输出；
前者的incoming增益重新支付
$$
                 4(7L/16-262144-1850)>39194024 .
$$
因此同一个94步准备、五个真实一侧jets和原collar lift给
$$
 \|u_{\rm seed}\|_{E_{8192}}<2^{-54866996},\qquad
 Z_s^{[3]}(\mathfrak F(u_{\rm seed}))
       <2^{-5275847456},\quad0\le s\le6396 .
 \tag{S.43}
$$
B端剩余真实角宽大于8198，故同时支付(S.31)所需
$2^{440}\|f_B(u_{\rm seed})\|_{H^{8195}}<2^{-54866000}$。
这是B端分离平滑的结果，不是粗帽输入端的解析正则性。
该步骤完全不需要 $\gamma$ 的8193阶界。

固定同一 $\gamma$，collar仍在全部negative principal路径之外，
所以RG和T.3--T.4给它前后准确相同的第一参数。
这不比较两个不同 $\gamma$ 的完整种子；
$a_{94}(\gamma)$、整尾数据和设计参数可以随 $\gamma$ 变化。

**新高门仅用于第4节的端点值窗。**
S.14直接重收M.16/O.12已经证明的完整mixed Taylor核：
未知两个输入都保持零宽，复平移只用于已知背景系数。
先有完整signed-lag列和，再做one-high Young卷积；
不是由裸 $A_0$ 算子norm猜矩阵绝对和。
全部mean输出在推核时保留，只在(S.3)选择非mean slope。

对最高 $r=8193$，所需矩仍为 $p\le r+4\le8197$，
阶乘界 $p!\le2^{13p}$ 及所有known-only角域均未改变。
(S.42)给
$1+\|\gamma/r_\gamma\|_{H^r}<2^{1048577}$，
所以替代原(S.2)后，最大完整账为
$$
 4473344+1048577+120+8192+32
                       =5530265<6291456 .
 \tag{S.44}
$$
这里120 bits是原 $r_B^{-2}\epsilon$；
8192及32保原lift与有限和。
因此 $K_\partial=2^{6291456}$ 完全不变。
固定affine $q_\gamma(0)$ 与非径向 $Dq_\gamma(0)$
仍分别保 $\epsilon$，没有把它们当二次零项。

S.16的一次差、二次余项、导数差遂全部逐字保留。
新的固定graph仍是(S.11)；
在最高 $s=8192$ 只用 $r=s+1=8193$ 及其已经单付的
$f_B\in H^{8195}$。本节不扩大N的整体网络角窗，
也不把M原 $q\le8160$的全部输出一并免费扩大到8193。

**原full proxy和确定Nash常数不变。**
由(S.42)，旧F的 $H^{8176}$ 门成立，且
$$
 G_\gamma=1+\|\gamma/r_\gamma\|_{H^{8176}}<2^{1048577},
 \qquad \overline B_\gamma=2^{1024}G_\gamma<2^{2097152}.
 \tag{S.45}
$$
这是固定输入常数；变化的最高背景继续以
$\|w\|_{E_{s+1796}^+}$ 显式出现。
真实 $s_B$、bare flux、两个曲率mean和所有独立Poisson列
按F/O/HT的同一单位保留。

S.18--S.24的准确far切向行只需要这些实际值图与finite高门，
不使用未知 $\gamma$ 的复角值。
nilpotent $J_w^{-1}$、完整 $P_\mu$、同截面 $H_p$ 常数相消、
额外 $H^{s+3}$ 端迹和 $\mathcal E_u[H]$ 全部不变。
source loss1734、背景1796和输出 $s\le6396$ 也不变。
一般有荷方向仍不由本节自动进入holonomy-one值图。

S.25--S.29的固定affine/固定非径向线性/真正二次三分解保持，
特别是两个实际线性交换项仍都存在。
(S.44)保证同一个
$K_+=2^{25165824}$、$\rho_+=2^{-33554432}$、
$C_+=2^{167772160}(1+\overline B_\gamma)^8$、
$T_0=2^{1500000}$
支付全部余项。以(S.43)的同一个种子定义(S.30)，
仍准确有 $\mathcal U_\gamma(w_0)=u_{\rm seed}$，
不是以粗上界重估初始 residual。

现在逐字执行S.34--S.37，得到每个固定真实输入(S.42)下的解
$$
 \mathfrak F(u_\infty)=0,\qquad b_\gamma(u_\infty)=0,\qquad
 \|u_\infty-u_{\rm seed}\|_{E_{1856}}
                                     <2^{-1700000000}.
 \tag{S.46}
$$
完整mean由同一个真正holonomy小根恢复；
同截面高度只指定一次，跨端真实span不被screen。
S.40--S.41的物理层衰减也不使用正解析宽，因此原结论保持。
为明确mean深幂的完整profile，M.1给
$\mu_j=\varepsilon_s\delta_{4096}^{3/2}\delta_j^{9/2}$
于深段；代入S.41后净幂准确为
$-9/2+262-13/2-10/256=251-10/256$，
固定 $\varepsilon_s,\delta_{4096},\delta_{8192}$ 的因子全部保留。
若进一步调用T第10节的整盘结论，
仍须使用其中的真实物理 $a$-jets、零residual与同一次frame积分。

本节只声明：对每个固定(S.42)输入存在上述实际body--far解。
它不单凭这一存在性授予 $\gamma\mapsto u_\infty(\gamma)$
的未证明全参数可微图或增广右逆。
仍须选择 $\gamma$ 以完成M32 core的完整内端 $B,C$，
包括两条曲率mean、waist及intrinsic设计行，
并对最终单个完整面支付原全域几何门。

最后，(S.42)始终是物理角上的完整函数条件。
moving low97向量经真实角变换或帽Poisson输出通常具有无限物理Fourier尾，
不能用有限维数直接推出它。
真正物理 $P_{\le96}^{\theta}\gamma$ 的有限部分可以独立估计，
其余完整物理尾仍须另付。
本节解决固定输入的解析域障碍，不把未知core的实际高门宣布为已验证。
