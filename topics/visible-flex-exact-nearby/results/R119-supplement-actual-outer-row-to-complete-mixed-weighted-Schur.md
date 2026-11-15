# R119 续篇：真实 B 边界行到完整 mixed 剩余算子的定量外端传输

2026-11-15，visible-exact / tail_connector。

**状态：解析证明，已分段独立核对。** 本篇保持同一实际短 connector、
两个负根、完整负分量、公共参数、物理角和背景。只把真实正外区的
$B$ 边界行从 $\mathcal T_0$ 换成 $\mathcal T_1$。
这里的 $\mathcal T$ 是高度到 total conormal density 的 order-one
行，包含真实未匹配修正；不是帽曲率的 order-two 行。

目标是补
[N：完整两层网络](R119-supplement-two-level-full-network-tame-inverse-and-complete-sources.md)
(N.2) 的**第二个独立门**。从局部有界型小量出发，必须实际付清
原正区、有限外行、共同表示、两个 high/deep Poisson 与双逆层权。
本篇不将第一门 $\mathcal A_{1824}$ 的名字直接替换成第二门。

所用原件为：

* [P：新完整正区与全源](R119-supplement-new-simple-root-complete-positive-DN-Airy-return-and-sources.md)，
  特别 P.13--P.32；
* [L：物理帽尾 Schur](R119-supplement-complete-physical-cap-tail-Sobolev-Schur-with-all-mean-charges.md)，
  特别 L.14--L.23；
* [I：附近全尾 proxy](R119-supplement-nearby-finite-Sobolev-full-tail-proxy-inverse-and-complete-sources.md)，
  I.3--I.7、I.14--I.25；
* [Y：同表示 mixed 差](R119-supplement-new-outer-complete-mixed-weighted-Schur-and-closed-nonmean-inverse.md)，
  Y.14--Y.28；
* [H：高外 Poisson](R119-supplement-unitary-high-exterior-Poisson-and-buffered-angular-projections.md)，
  H.12、H.18--H.21；
* [D：真正 deep-low 消元](R119-supplement-complete-deep-low-Green-Poisson-and-mixed-elimination.md)，
  D 篇正文 L.15--L.28；
* [Z：完整 mean 商](R119-supplement-new-closed-mean-compatibility-gauge-and-complete-fixed-CR-inverse.md)。

以下所有 $H^s$ 都是完整 $4\mathbb Z$ 物理 Fourier 空间；
$\Lambda=(1+D_\theta^2)^{1/2}$。负阶、真正 adjoint、两个 mean、
相反 Fourier 锥和全部高模都保留。

## 1. 局部输入必须是哪一个算子

在同一个当前短侧背景上，记
$$
 \mathcal T_i=\mathcal N_{B,i}-\mathcal E_{B,i},\qquad
 \Delta\mathcal T=\mathcal T_1-\mathcal T_0 .
 \tag{D.1}
$$
$\mathcal N_{B,i}$ 使用真实 long 加其真正远端反馈。
$\mathcal E_{B,i}$ 是原 P.7/I.6a 的完整未匹配项：
$$
 \mathcal E_{B,i}
 =P_{\mu_T}\{-M_{\mu_T/\mu_{L,i}-1}\mathcal N_{B,i}P_\perp
           +M_{\mu_T(d_{L,i}-d_T)}\partial_\theta\}.
 \tag{D.2}
$$
这里 $P_{\mu_T}z=z-\mu_T\langle z\rangle/\langle\mu_T\rangle$；
其 rank-one 行不能提前换成 $P_\perp$。
$\mu_T,d_T$ 在两次比较中相同，long 端的真实系数可以不同。
必须先将另一实角中的 DN 按 scalar 输入、density 输出的真
Piola 变换送到此同一角；不能以裸 composition 的小差替代这一步。

令
$$
 q_0=1792,\qquad
 d_{1792}=\max_{|s|\le1796}
 \|\Lambda^s\Delta\mathcal T\Lambda^{-s}:
                              H^{1/2}\longrightarrow H^{-1/2}\|.
 \tag{D.3}
$$
可以只在所需整数端点给界，再用同一 Hilbert 插值；
负 $s$ 同时记录真正 adjoint 的相应窗。
这个范数作用于真实物理高度 $g$ 和 total conormal density，
没有除以 $s_B=a_Bw_B$。归一化 $f_B=P_\perp g/s_B$
只在最终高度读出时使用。

齐次输入还须保准确的
$$
 \Delta\mathcal T\,1=0,\qquad
 \langle\Delta\mathcal T g\rangle=0 .
 \tag{D.4}
$$
它们由完整 holonomy 和散度 Green 身份得到，不能从先删去
$D\kappa$ 或 mean 行后的假算子取得。
独立的 mean flux、曲率 mean、height span 和弱端荷不满足
“全部为零”的结论；这些是下文另外的仿射列。

本篇定量结论是
$$
 \boxed{\quad
 \|(v^\#)^{-1}\Delta S_{\rm rem,out}(v^\#)^{-1}
                       :H^{1792}\to H^{1792}\|
             <2^{3000000}d_{1792}.
 \quad}                                                   \tag{D.5}
$$
充分的小门为 $d_{1792}\le2^{-3500000}$，于是 (D.5) 严格小于
$2^{-500000}<2^{-400000}$。这里也给更宽的实际用途：
若新的局部定理给 $d_{1792}<2^{-6000000}$，所得全网门直接为
$2^{-3000000}$，不再需要猜测一个端口倍率。

(D.5) 只比较这两个相同短侧背景上的外行。
背景、根、第一参数或表示本身的变化仍由 I/N 原 body 差处理；
一般参数导数另有 $\dot H^*g$、$\dot s_B$ 等真实列。

为固定本次应用的参考身份，可以在原 I/Y 已证明的同一个 uniform
fixed-$C_R$ 家族中明确取 $Z^0=0,\ f_B^0=0$。这里重新实例化的是
已经证明的线性外行定理；短侧仍是当前实际背景，真实
$\mathcal E_{B,0}$ 和 affine mismatch 均不改为零。
原 N.6 的球包含该点，M.17 的径向解与唯一性给
$\Phi_R(0,0)=0$；但 $D_f\Phi_R(0,0)$ 的有限长反射仍保留。
因此旧行是 Y.4 的真正 fixed-$C_R$ Robin：
$v_{m,t}(L)=m^2v_m(L)$（$m\ne0$）、$v_{0,t}(L)=0$。
它不是 N 中远端 Dirichlet comparator
$\mu_0|D|\coth(L|D|)P_\perp$；两者之差仍由原完整
$\epsilon_L$ 门收费。原 I 没有钉死另一组数值 $(f_B^0,Z^0)$；
若选择保留另一旧成员，则必须使用它自己已付的参数域和局部差，
不能由原全 $z_a$ 球推断它位于较小 $z_a/16$ 球。

## 2. 原正片的三个完整物理端口

固定旧外行，定义三个准确映射：

1. $\mathcal P_0$：给定真实 root incoming $z$、无仿射源时，
   读取真实 $B$ 高度 $h_B$；
2. $\mathcal C_0$：root incoming 为零、$B$ 总通量源为 $\beta$ 时，
   读取原 Airy affine 输出；
3. $\mathcal K_0$：同一个 incoming-zero 解的真实 $B$ 高度。

root incoming 是 P.18--P.19 的完整两列初值，包括
mean 阻抗 $i/\pi$。不是一个有限头的归一化向量。
物理边界方程约定为
$$
                  \pi_B+\mathcal T_0h_B=\beta .
 \tag{D.6}
$$
该号与原能量型的 $+\langle\mathcal T_0h_B,V_B\rangle$ 一致。

L.14--L.18 已逐项证明
$\mathcal P_0:L^2\to H^{1/2}$ 的 $2^{256}$ 门及右 $4/3$ 强窗
$2^{6100}$，并用真正 adjoint Poisson、全 mean Wronskian
得到
$\mathcal C_0:H^{-1/2}\to H^1$ 的 $2^{14000}$ 门。
同一 particular 的 $\mathcal K_0:H^{-1/2}\to H^{1/2}$
有 $2^{15000}$ 门。只使用 P.32 的 $L^2$ 源界不能替代它们。

这些同一个算子在所需低角窗上重新按 I.3--I.7 收费。
一个 source 或 trace map 最多新增一份
$B_{\rm fin}=2^{229376}$：真实输入表示、零边界型的完整 resolvent、
输出表示在同一个有界型/Green 配对中计算，不将该数视为每一项
Volterra factor 的 norm。I 第7节与 U 第8节的两次 source/trace
角费用正是分别一份。实际展开的角阶不超过 $q+32$；
$q\le1796$ 时小于1829，均在 N 的1856低背景之内。
根普通/强窗、半阶对偶及 true mean 的原固定费用不超过15000 bits。

例如 L.17 的准确恒等式是
$$
 2\chi^2|\langle\mathcal C_0\beta,\mathcal R_{\rm adj}z\rangle|
       =|\langle\beta,\mathcal P_{0,\rm adj}z\rangle|,
 \quad \mathcal R_{\rm adj}=\mathcal R_0^{-*}.
 \tag{D.7}
$$
由右 $4/3$ 窗及 I 已付的相邻同阶窗，实际上可保
$\mathcal C_0:H^{q-1/2}\to H^{q+4/3}$；
后续高 source 只消费其中一阶。
负 $q$ 用真对偶，不用实际返回的假酉性。
为整个窗口统一取
$$
 C_{\rm ext}:=2^{245760}>2^{229376+15000}.
 \tag{D.8}
$$
则在 $|q|\le1796$ 的所需相邻窗上，所有
$$
 \mathcal P_0:H^q\to H^{q+1/2},\quad
 \mathcal P_0\Lambda^{4/3}:H^q\to H^{q+1/2},
$$
$$
 \mathcal C_0:H^{q-1/2}\to H^{q+1},\quad
 \mathcal K_0:H^{q-1/2}\to H^{q+1/2}
 \tag{D.9}
$$
均小于 $C_{\rm ext}$，相同门保真正 adjoint。
这组界包含 physical $B$ mean；没有把 mean 高度用
$\dot H^{1/2}$ 控制。其低频费用来自原 P.31 的径向 Poincare 和
正 root shear，已在15000 bits内。

## 3. 先独立闭合新的正片，不能先借待证全网逆

用旧正片解新边界条件
$\pi_B+\mathcal T_1h_B=\beta$。旧边界源准确为
$\beta-\Delta\mathcal T h_B$，所以
$$
 (I+\mathcal K_0\Delta\mathcal T)h_B
               =\mathcal P_0z+\mathcal K_0\beta .
 \tag{D.10}
$$
由 $C_{\rm ext}d_{1792}<1/4$，两个边界 Neumann 级数
$I+\mathcal K_0\Delta\mathcal T$、
$I+\Delta\mathcal T\mathcal K_0$ 在各自准确半阶空间同时可逆，
范数小于2。先在光滑数据上证明，再按这些真正 source norm 延拓。

于是
$$
 \mathcal C_1=\mathcal C_0
       (I+\Delta\mathcal T\mathcal K_0)^{-1},\qquad
 \mathcal K_1=\mathcal K_0
       (I+\Delta\mathcal T\mathcal K_0)^{-1},
$$
$$
 \mathcal P_1=(I+\mathcal K_0\Delta\mathcal T)^{-1}\mathcal P_0,
 \qquad
 \Delta\mathcal R_+
    =-\mathcal C_1\Delta\mathcal T\,\mathcal P_0 .
 \tag{D.11}
$$
这支付了实际两端 graph 的完整分母，不是单凭两片有界就假定
新的 Möbius 分母可逆。正区全部零平台、root collar、long 反射、
未匹配 mean 和 $C_R$ 或真实帽的反馈已经在 $\mathcal T_i$ 中。

特别
$$
 \|\Delta\mathcal R_+:H^{1792}\to H^{1792}\|
       <2C_{\rm ext}^2d_{1792}=2^{491521}d_{1792}.
 \tag{D.12}
$$
原右 $4/3$ 窗由 (D.11) 的 $\mathcal P_0$ 强窗保留；
左窗用 $\mathcal C_0$ 的真对偶强窗。所需角移位不超过 $4/3$，
(D.3) 的四阶缓冲足够。新增强余项比旧 P/I 的强常数小得多，
故原 high 投影无需变化。旧正片的同阶 norm 和逆小于2；
由 (D.12) 的极小同阶差及准确 inverse identity，新正片的
同阶 norm 和逆可安全取小于4。这里只需这个有明确余量的门，
不从旧严格小于2擅自推新者仍小于2。
原 H 的 $2^{-9499}$ Poisson 门与下文 $2^{-9000}$ 之间的
499 bits 余量吸收这些固定因子及新增强余项。
以上是正片自身的构造，未使用新的 remaining inverse。

## 4. 完整有限外行及同一个 unitary 表示

固定当前负分量和共同 $H_W$。原 Y 的准确接线是
$U=R_+S_-$，而不是一个另有未知分母的合成。
正返回变化的未消元差为
$$
 \Delta\widehat U
   =H_W^*(\Delta R_+)S_-H_W .
 \tag{D.13}
$$
N/I 已在本低窗付 $H_W,H_W^*,S_-$ 的同阶 norm 小于2；
全部真实两端、两 wave 和 mean 均参加。
因此
$$
                D_U:=\|\Delta\widehat U:H^{1792}\to H^{1792}\|
                         <8\|\Delta R_+\| .
 \tag{D.14}
$$
共同表示没有因换外行而重新构造；若比较问题另换了背景或
principal 图，其 $\Delta H$ 是 I/N 的另一项，不藏在 (D.13)。

令 $\Pi$ 为全部层 $129\le j\le131$ 的完整波投影。
原 Y.14--Y.15 的真实有限邻接给
$$
                \Delta\widehat U=\Pi\Delta\widehat U\Pi .
 \tag{D.15}
$$
这个投影不截角频，也包含所有 canonical mean。
这里只说消元前的支持；两个 Schur 之后的差一般具有长程尾。

保持 N 原来的
$$
 v_j^\#=2^{-1200000}J_j^{-4165}\delta_j^{1073/32},\quad
 F_j=2^{4096}J_j^4\delta_j^{-5},\quad J_j=j+5 .
 \tag{D.16}
$$
由 $J_j<2^8,\delta_j^{-1}<2^{135}$，在 $\Pi$ 上
$$
 0<v_j^\#<1,\qquad
 \|(v^\#)^{-1}\Pi\|<2^{1238200},\qquad
 \|F\Pi\|<2^{5000}.
 \tag{D.17}
$$
第二个界也等于 U 的 $2^{638200}$ 乘准确新权因子 $2^{600000}$。
$\Pi$ 内 $v^\#$ 及其逆的条件数小于 $2^{160}$；
以下宽取 $2^{256}$。所需 $w=v^\#,(v^\#)^{-1}$ 和
$wF^{\pm1}$ 在真实相邻块的比均满足原 H.12，不因全局常数
$2^{-1200000}$ 改变。

## 5. 两实际的 high/deep 映射必须先存在

旧完整外行在 I/N 下已有 high 和 deep 映射。
(D.12) 的两强窗保新 high feedback 小门，所以 H.18--H.21
在旧、新两系统及所有上述权中都给安全的
$$
 \|wE_{H,i}w^{-1}\|,\quad\|wF_{H,i}w^{-1}\|
                  <\varepsilon_H:=2^{-9000},\quad i=0,1 .
 \tag{D.18}
$$
这是沿原强余项和真 adjoint 得到的 Poisson 界，
没有把 high-feedback 的另一指数直接改名为 Poisson norm。

这里还须避免先假设待证的新 deep inverse。
$P_D$ 仍是 $j\ge8193$ 的真正低包，因而 $\Pi P_D=0$。
准确 high Schur 差
$$
 \Delta S_H=[I,F_{H,1}]\,\Delta\widehat U\,[I;E_{H,0}]
 \tag{D.19}
$$
在 deep-deep 两侧都必须经一个 high Poisson。
将左因子放在 $wF$、右因子放在 $wF^{-1}$，
中间有限投影各取 $F_\Pi<2^{5000}$，得到
$$
 \|wF\,P_D\Delta S_HP_D\,Fw^{-1}\|
 <\varepsilon_H^2F_\Pi^2\,2^{256}D_U
 <2^{-7744}D_U .
 \tag{D.20}
$$
旧 $R_{D,0}$ 的 typed inverse
（源 $wF$ 到状态 $wF^{-1}$）范数小于 $2^{66}$；
$D_U<1$ 已由 (D.12) 给出。于是这个真正的 deep Neumann
反馈小于 $2^{-7678}$，新 $R_{D,1}$ 独立存在，范数小于 $2^{67}$。

对交叉列，同样有
$\|wF P_D\Delta S_HP_{\rm rem}w^{-1}\|
 <2^{256}\varepsilon_HF_\Pi(1+\varepsilon_H)D_U$。
把它及 (D.20) 代入
$E_{D,1}=E_{D,0}+R_{D,1}(\Delta C+\Delta D E_{D,0})$，
实际增量小于1；真正 adjoint 给左 Poisson。
旧 $2^{130}$ 门因而可以统一宽为
$$
 \|wF^{-1}E_{D,i}w^{-1}\|,\quad
 \|wF_{D,i}F^{-1}w^{-1}\|<2^{132},\quad i=0,1 .
 \tag{D.21}
$$
这一步用强源/状态域的原 Neumann，而非在裸 $\ell^2$ 中猜逆。
canonical mean 不属于 $P_D$，始终保留。

## 6. 两 actual 的全部长程路径及双逆权

定义完整齐次恢复和源消元
$$
 \mathscr R_i=[I;E_{H,i}][I;E_{D,i}],\qquad
 \mathscr L_i=[I,F_{D,i}][I,F_{H,i}] .
 \tag{D.22}
$$
各矩阵按原 remaining/deep/high 直和理解。
对于任意上述权 $w$，有
$$
 \|w\Pi\mathscr R_iw^{-1}\|,\quad
 \|w\mathscr L_i\Pi w^{-1}\|
 \le1+\varepsilon_H+2^{132}F_\Pi\varepsilon_H<2 .
 \tag{D.23}
$$
证明中直接 remaining 路径是1，直接 high 路径是
$\varepsilon_H$。因为 $\Pi P_D=0$，唯一新增 deep 路径是
$\Pi E_HE_D$ 或 $F_DF_H\Pi$。
前者用 $wF^{-1}$ 的 $E_H$ 界，把 $F$ 移到左侧 $\Pi$；
后者用 $wF$ 的 $F_H$ 界，把 $F$ 移到右侧 $\Pi$。
所以恰付 $2^{132}F_\Pi\varepsilon_H<2^{-3868}$。
这些路径没有被设零，也没有假定消元后仍有限邻接。

两个 actual Schur 的准确差是
$$
 \Delta S_{\rm rem,out}
                  =\mathscr L_1\,\Delta\widehat U\,\mathscr R_0 .
 \tag{D.24}
$$
先在有限角/层和合法源上由消元矩阵恒等式证明；
(D.18)--(D.23) 的穷尽无关界再给真实闭包。
左边用 $w=(v^\#)^{-1}$，右边用 $w=v^\#$。
结合 (D.15)、(D.17)、(D.23)，得到
$$
 \|(v^\#)^{-1}\Delta S_{\rm rem,out}(v^\#)^{-1}\|
                      <2^{2476402}D_U
                      <2^{2476416}\|\Delta R_+\|.
 \tag{D.25}
$$
最后代 (D.12)：
$2476416+491521=2967937<3000000$，即证 (D.5)。

这次差在同阶 $H^{1792}$ 已有界，因此没有乘 $T_j^\#$。
若仅取得一角损失的 $\Delta\widehat U$，则必须回到 Y/I 的
cutoff/径向 Poisson 账；不能用本篇代替那个不同类型的输入。
独立外 source 更没有由此获得内部 cutoff 权限。

## 7. 所有仿射 B 源和反向读出

令 $\beta\in H^{q-1/2}$ 是已经按原 P.27--P.28、
真实 total flux、相同物理角整理的完整 $B$ 源。
新正片给 Airy source
$\mathcal C_1\beta\in H^{q+1}$，并保
$\|\mathcal C_1\beta\|_{H^{q+1}}<2C_{\rm ext}\|\beta\|$。
将其嵌入真正外根、再乘共同 $H_W^*$，
得到支持于 $\Pi$ 的 $\widehat g$。
(D.23) 于是给充分门
$$
 \|(v^\#)^{-1}k_{\rm ext}\|_{H^q}
   <2^{1500000}\|\beta\|_{H^{q-1/2}},
                   \qquad0\le q\le1792 .
 \tag{D.26}
$$
未粗化指数至多 $1238200+245760+3=1483963$。
高 source 所需的一角由 (D.7)--(D.9) 真正给出，
不是从 $\Pi$ 有限层支持或一个有限频 cutoff 推出。

如果已核其完整物理 charge 相容，指定零整体高度 gauge 后，
I/Z 的 remaining inverse和(D.18)--(D.21)恢复 high、deep。
完整有限端抽取按原 L.19--L.23/U.27 重做，两个
$(v^\#)^{-1}$、两个 finite 角组、两份有限 $F$、正片 source/trace
和全部 mean/Poisson 的预算严格小于
$$
 2\cdot1238200+2\cdot229376+15000+10000+2048
                  =2962200<3100000 .
$$
因此真实归一化非mean高度响应满足
$$
 \|\mathcal T_{B,\rm tail}:H^{q-1/2}\to H^{q+1/2}_\perp\|
                         <2^{3100000}/s_B .
 \tag{D.27}
$$
其 source particular 包含在15000 bits中。
这条读出不赋予原 analytic224 标签，也不把新的帽输入 $\gamma$
默认为已经与负主体匹配。

具体外输入先保持各自真实局部门。例如独立帽内曲率方向若已得
$\|\mathcal B_\gamma\dot\gamma\|_{H^{q-1/2}}
 \le s_B\epsilon_L C_{\gamma,q}\|\dot\gamma\|$，
便将这个完整源代入(D.26)--(D.27)，准确取消
$s_B^{-1}s_B$。$C_{\gamma,q}$ 必须由真实两输入帽图给出，
不能沿用旧 fixed-$C_R$ 的另一归一半径。
$B_R$ mean、$C_R$ mean、$f_*^{\rm src}$、Robin residual及
各原体/weak/原子源则用自己的真实列。
long 的 mean 高度跨度继续是
$\int aw\,D\kappa\,h$，原 $aw(L)/165$ 的未screen列不乘
$\epsilon_L$。

## 8. 兼容、gauge、参数和全族范围

(D.24)--(D.25) 是**完整** remaining 算子界，包含两个 canonical
mean 的行列及它们与非mean的耦合。
物理常高度的 root 波不是纯 canonical mean。
因为(D.4)，同一个物理常高度仍满足新齐次外行；
其对应真实根向量按原 Z 的域识别保留。

原 Z 的强 source 方程、准确辅助列 $\sigma_\circ$、
一条物理 height functional $\ell$ 和 total-flux functional
继续使用。真正可解仍须核
$\mathcal L_{\rm new}k=0$；否则增广解保留
$\tau=\mathcal L_{\rm new}k/(\mathcal L_{\rm new}\sigma_\circ)$。
最后根的 physical source 系数不因外行变化而重新归一，
$\mathcal L_{\rm new}\sigma_\circ\ne0$ 仍由原真根 density/mean式保证。
不把辅助 $\tau$ 当作已经解出的 $\nu$ 或曲率 mean。

只有一个整体物理高度常数可以规范。另一端 height span、
真实 flux、$\Gamma$ 的 $H_p$ 两端差、raw mean slope、
帽内两 mean 和 $\nu$ 都是必须联立的原数据。
每个 affine 方向还须微分真实角/源表示、$s_B$、$\mu_0$、
参数停止尺度和实际帽图；不能对它们套齐次(D.4)。

最后，本篇固定当前设计 metric 的参数，证明外行替换及其完整
传输。E/L/B 迭代中逐次重建 $\Gamma_1^*(u)$、冻结 $\Gamma_2$，
目前给的是最终设计 metric 的一个成员。
原 $\nu$ 是 intrinsic 设计列，不是保持 metric 不变的 extrinsic
flex 参数。现有 projected 反馈与本篇外门没有证明：
把最终 $\nu^*,\Gamma_1^*,\Gamma_2^*$ 全部冻结后，
真正 extrinsic 族仍有满足所有 mean、height、frame 和帽内端口的
增广非线性入口。这个固定 metric 全族接口继续保留，既不能用
body 收敛替代，也不据此声称它不可能。
