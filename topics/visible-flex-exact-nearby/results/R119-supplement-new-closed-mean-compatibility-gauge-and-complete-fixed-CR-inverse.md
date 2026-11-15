# R119 续篇：新闭网络的真实 mean 兼容、唯一高度 gauge 与完整固定-C_R逆

2026-11-15，visible-exact / tail_connector。

**状态：解析结论；真实通量兼容、物理高度规范及源空间逆已核。** 本篇接
[新外完整加权 mixed 消元](R119-supplement-new-outer-complete-mixed-weighted-Schur-and-closed-nonmean-inverse.md)
Y.1--Y.28。实际外侧未知高度列固定独立物理 $C_R$，帽内反馈仍另联立。
闭合后的物理常高度是准确一维核；本篇给它的真实 source 兼容泛函、
一个整体高度 gauge 和其余全部频率的同空间 inverse。
不把原开放 mean Robin 逆直接沿用，也不把弱端口 norm 的收敛
当作平端两迹条件已经闭合。

置
$$
 v_j=2^{-464800}(j+5)^{-4165}\delta_j^{1073/32},\quad
 \mathscr Y=\{g:\|v^{-1}g\|_{\ell^2L^2}<\infty\},\quad
 \eta=2^{-5800000}.
 \tag{Z.1}
$$
$A_a=I-S_{{\rm rem},a}$、$A_\circ=I-S_{{\rm rem},\circ}$，
$\Delta S=S_{{\rm rem},a}-S_{{\rm rem},\circ}$。
Y 已付 $\|v^{-1}\Delta S v^{-1}\|<\eta$。
下文的 root source 和 remaining source 均是原真实有序消元后的单位，
不是任意 ordinary 或 weak 体源的免费改名。

## 1. 真正自然 mean 边界和唯一平移

仍按原 mean 篇 M.2--M.3，写
$$
 \mu_j=\varepsilon_s m_j,\qquad
 m_j=\begin{cases}\delta_j^6,&j\le4096,\\
 \delta_{4096}^{3/2}\delta_j^{9/2},&j>4096,\end{cases}
 \qquad
 H=\sqrt{\varepsilon_s/\rho}\,h,\quad
 P=\sqrt{\rho/\varepsilon_s}\,\pi .
 \tag{Z.2}
$$
这里 $\pi$ 是 total physical flux，$\rho,\varepsilon_s$ 没有设为1。
径向 mean 在每个无源开段满足
$H_t=\mathfrak m^{-1}P,\ P_t=0$，
$\mathfrak m=m_jp_*/r^8$ 于原尾段。
跨新 finite connector 使用同一正 conductance 及真实定向 total flux；
相反的局部参数方向同时改变 flux 号，电阻为
$\int\mathfrak m^{-1}|dt|$。

平端条件明确为
$$
 P\longrightarrow0,\qquad H\longrightarrow\lambda .
 \tag{Z.3}
$$
另一端 Y.4 的径向 mean 条件是自然 $P=0$。
因此径向无源解只有 $P=0,H=\lambda$。
实际物理高度的常数也准确解原散度 Jacobi 方程；
新正区未知高度列杀死常数，未匹配界面 $E_B1=0$，
真实 holonomy 的齐次 mean 通量为零。
这给实际的一条物理常高度核，而非 canonical 纯零模。
任意 $\lambda$ 只有这一条整体高度自由度，不逐胞另添常数。

## 2. 新外根的完整 mean frame 与电阻重新收费

原所有根定义
$q_e=\alpha_{0,e}/(\varepsilon_s/\rho)$。
原 M.7 给
$2^{-16}m_j\delta_j^{-5/4}<q_e<
2^{176}Jm_j\delta_j^{-13/4}$，
根的真实层允许相差1。新根 $e_0$ 不直接套这条旧门。

O.4--O.6 已给整个 $e_X\to e_0$ 的
$\int(1+Q)|dt|<282\log2$，故其密度双向比例小于 $2^{282}$。
又 $2^{28}<b_0<2^{29}$、$1<b_X<2^{336}$，
根处 $q=b\mu_0/(\varepsilon_s/\rho)$，所以
$$
 2^{-600}<q_{e_0}/q_{e_X}<2^{600}.
$$
将 $e_0$ 标在第129层，全部旧根和这个新根共同满足
$$
 2^{-616}m_j\delta_j^{-5/4}<q_e
       <2^{776}Jm_j\delta_j^{-13/4},
$$
$$
 q_e^{-1/2}<2^{512}m_j^{-1/2}\delta_j^{5/8},\qquad
 q_e^{1/2}<2^{512}\sqrt J\,\sqrt{m_j}\delta_j^{-13/8}.
 \tag{Z.4}
$$
原实际 $m_j$ 在相邻深度的准确比介于
$2^{-6(j-k)}$ 和 $2^{-(9/2)(j-k)}$。
特别 $m_j\ge\delta_j^6$、$m_j\le\delta_j^{9/2}$，
故仍可用
$q_e^{-1/2}<2^{512}\delta_j^{-19/8}$、
$q_e^{1/2}<2^{512}\sqrt J\,\delta_j^{5/8}$。
新增根只增加固定费用，没有把深层的真 $\delta$ 幂改坏。

原 M.5 给任一第 $k$ 层根到 $e_X$ 的电阻
$<2^{13}m_k^{-1}$。
在 $e_X$，$\mathfrak m_X\ge m_{129}\delta_{129}/512$；
O.6 给外片长度 $<512$ 和密度比例 $<2^{282}$。
因 $\delta_{129}^{-1}<2^{133}$，整个新增负片电阻
$<2^{433}m_{129}^{-1}<2^{512}m_{129}^{-1}$。
所以从任一根向外、止于 $e_0$ 的任一子段准确有
$$
                  \int\mathfrak m^{-1}|dt|<2^{514}m_k^{-1}.
 \tag{Z.5}
$$
正片与长段的 mean 无源通量已经为零；不把其很长的电阻
无故乘入 (Z.5)。这些片有源时仍用 P/N 的真实 mean particular
与高度跨度，而不是把其源删除。

mean Airy 两列仍是
$D_{\sigma,0}=c(1+i\sigma\xi/\pi)$，$c,c^{-1}<4$。
在每个真根，原完整恢复给
$$
 z_\sigma=\gamma_{e,\sigma}H+\chi_{e,\sigma}P,\quad
 \gamma_{e,\sigma}={\sqrt q\over2c}(1-i\sigma\pi\ell_{0,\xi}/2),
 \quad
 \chi_{e,\sigma}={-i\sigma\pi\varsigma_e\over2c\sqrt q}.
 \tag{Z.6}
$$
$|\ell_{0,\xi}|<8$ 足够，新右根满足更强的 $1/8$ 门。
所有根均保真实 $\varsigma_e$ 和 outward 符号。

## 3. 原位 source 的两跳与一条完整通量泛函

准确网络 source 在每个根产生原 mean 篇 M.11 的一条 wave 差。
其有向物理跳量记为
$$
 (a_e,b_e)=(\alpha_e^{\,s},\beta_e^{\,s})\,g_e ,
$$
$$
 \binom{\alpha_e^{\,s}}{\beta_e^{\,s}}
  =\text{真实接线号}\,
  \binom{c/\sqrt{q_e}}
  {\varsigma_e c\sqrt{q_e}(i\sigma_e/\pi-\ell_{0,\xi}/2)} .
 \tag{Z.7}
$$
这里的 $\alpha_e^{\,s}$ 是 source 系数，不与根密度 $\alpha_e$ 混同。
准确有
$|a_e|\le2^3q_e^{-1/2}|g_e|$、
$|b_e|\le2^7q_e^{1/2}|g_e|$；
尤其 source 的 height 跳没有随着通量一起投掉。

设 $\ast$ 为新最后根 $e_0$ 的那个 mean incoming 源槽。
它是新完整负窗的右端槽，外侧已接 Y.4 的自然 mean 线。
令 $\beta_\ast=\beta_\ast^{\,s}$，则
$$
 |\beta_\ast|\ge\sqrt{q_\ast}/16>0,\qquad
 \sigma_\circ=\beta_\ast^{-1}e_\ast,\qquad
 \mathcal L_\circ g=\sum_e b_e,\qquad
 \mathcal L_\circ\sigma_\circ=1 .
 \tag{Z.8}
$$
非zero Fourier source 的径向 $\mathcal L_\circ$ 为零。
$\sigma_\circ$ 仅是反演时的一个准确辅助列，不是新增可自由调整的
物理参数，更不是把一个未解 mean 条件交给 $\nu$ 而不收费。

由 (Z.4)、原每胞至多四根及 Cauchy--Schwarz，
$$
 \|\mathcal L_\circ v\|<2^{-460000}.
 \tag{Z.9}
$$
例如每个 $b_e$ 系数不超过
$2^{519}\sqrt J\,\delta^{5/8}$，
乘 $v$ 后有正幂 $1073/32+5/8=1093/32$，
完整平方几何和小于显示余量。
新根的 (Z.4) 还给 $q_\ast^{-1/2}<2^{624}$，
而 $v_{129}^{-1}<2^{503000}$，所以
$$
                    \|v^{-1}\sigma_\circ\|<2^{504000}.
 \tag{Z.10}
$$
这些量均在原波/通量单位中，未把非零的物理缩放舍去。

## 4. 径向闭 mean 的真正右解，不借开放 Robin

先取有限个根源，令
$\widetilde g=g-\sigma_\circ\mathcal L_\circ g$。
其全部物理 flux 跳和准确为零。
在从平端向外的真实次序中，定义
$$
 P(t)=\sum_{t_e<t} \widetilde b_e,\qquad
 H(t)=\sum_{t_e<t}
       \left(\widetilde a_e+
                \widetilde b_e\int_{t_e}^{t}\mathfrak m^{-1}|ds|\right).
 \tag{Z.11}
$$
源点按所需的单侧迹读取。它准确满足每个开段、两个 jump，
平端 $(H,P)\to(0,0)$ 和外侧自然 $P=0$。
最后正片的常高度由此确定，不另指定一个 mean Dirichlet 条件。

注意最后根的负窗状态取该根的内侧迹。辅助 source
$\sigma_\circ$ 只改变该点外侧的自由常高度和 flux，
所以 (Z.11) 恢复出的所有负窗 incoming 对它准确为零。
这不是把它的 height 跳设零，而是最后正片没有额外 height 约束。
把所有这些 incoming 记为 $R_{Z,\circ}g$，于是
$$
 R_{Z,\circ}\sigma_\circ=0,\qquad
 A_{ZZ,\circ}R_{Z,\circ}=I-\sigma_\circ\mathcal L_\circ .
 \tag{Z.12}
$$
如果反而使用原开放 mean 的 $\kappa_X$，
就会固定错误的外 Robin；本篇完全未使用它。

(Z.4)--(Z.5) 还给绝对收敛门
$$
 |a_e|+|b_e|\int_{t_e}^{e_0}\mathfrak m^{-1}|ds|
          <2^{2048}J_e\delta_e^{-5}|g_e| .
 \tag{Z.13}
$$
因为最强的真实幂是 $37/8<5$。
对 $g\in\mathscr Y$，剩余幂为
$1073/32-5=913/32>0$，故完整绝对和收敛。
在 (Z.11) 向平端取极限，只剩这个绝对可和级数的深尾，
因此真正 $H\to0,P\to0$。这一结论对强 source 范数的收敛连续。

齐次径向 mean 的真实平端域若还允许高度 $\lambda$，
则只增加物理常高度的根向量 $c_\circ\lambda$。
记其高度读数为 $\ell$，于是
$$
 \ell R_{Z,\circ}=0,\quad \ell c_\circ=1,\quad
 R_{Z,\circ}A_{ZZ,\circ}x=x-c_\circ\ell x .
 \tag{Z.14}
$$
该唯一性使用明定的平端零通量，不能由弱状态权推出。

## 5. 新权的完整核估计与全径向广义逆

与开放 mean 的衰减核不同，(Z.11) 中 height 跳主要向外传播，
不能沿用原 M.18 的 $2^{-|j-k|/2}$。
令 $d=|j-k|$，$l=\min(j,k)$。
用 (Z.4)、$m_j/m_k\le2^{6|j-k|}$ 和 (Z.5)：
height 跳项最多增长 $2^{19d/8}$，
flux 乘电阻项最多增长 $2^{37d/8}$，
反向 flux 迹项更小。
将真实一层根编号差、最后根和四槽计数一起放宽，得
$$
 |(R_{Z,\circ})_{jk}|
   \le2^{4096}J_jJ_k\,\delta_l^{-4}\,2^{5d}.
 \tag{Z.15}
$$
其显示常数覆盖两次 frame 的1024 bits、电阻514 bits、
source/output14 bits及不足128 bits的有限重编号；
没有把向外增长偷换成衰减。

两侧乘 $v$ 后，
$$
 v_jv_k\delta_l^{-4}2^{5d}
 \le2^{-929600}J_j^{-4165}J_k^{-4165}
       \delta_l^{1009/16}\,2^{-(913/32)d}.
$$
所以完整行列几何和给
$$
 \|vR_{Z,\circ}v\|<2^{-925000},\qquad
 \|vc_\circ\|<2^{-460000}.
 \tag{Z.16}
$$
前式未粗化的 bits 小于 $-925500$；
后式直接用 (Z.6)、(Z.4) 及其完整平方和。
这两个门没有截断无限 low 根。

与 C/Y 已付的径向非mean inverse 直和，得到
$R_\circ=R_{N,\circ}\oplus R_{Z,\circ}$，并有
$$
 \|vR_\circ v\|\le1,\quad
 A_\circ R_\circ=I-\sigma_\circ\mathcal L_\circ,\quad
 R_\circ A_\circ=I-c_\circ\ell,
$$
$$
 R_\circ\sigma_\circ=0,\quad
 \ell R_\circ=0,\quad
 A_\circ c_\circ=0 .
 \tag{Z.17}
$$
这些是完整径向 remaining 算子的准确 generalized inverse 恒等式。
非mean 的 high/deep 真源和两向重建仍按 Y.28；
canonical mean 从来不属于那两个消元块。

## 6. 在强 source 空间解完整实际均值联立

不能仅在 $\|vx\|$ 中说“零平端高度是闭子空间”。
例如截断常高度向量即可在这个弱 norm 中逼近完整常高度，
而其平端高度不同。
为避免这个错误，直接在 Banach 空间 $\mathscr Y$ 解
$$
 \mathfrak h
  =g+\Delta S\,[c_\circ\lambda+R_\circ\mathfrak h].
 \tag{Z.18}
$$
(Y.2)、(Z.17) 给
$\|v^{-1}\Delta S R_\circ v\|<\eta<1$，故此式有唯一强 source 解。
定义
$$
 x=c_\circ\lambda+R_\circ\mathfrak h,\qquad
 \tau=\mathcal L_\circ\mathfrak h .
$$
准确代回 (Z.17)，得到
$$
                    A_a x+\sigma_\circ\tau=g,\qquad \ell x=\lambda .
 \tag{Z.19}
$$
并有完整界
$$
             \|vx\|<2\|v^{-1}g\|+2^{-459999}|\lambda| .
 \tag{Z.20}
$$
每次修正都是同一个强 source 的真实 Green 解；
(Z.13) 确保其物理 mean 平端两迹而非只给弱端口极限。

实际与径向的域识别也不能省略。Y.28 重建全部 high/deep 后，
旧 M.22--M.25 的完整根初值和密度配对在未改深尾保持。
新 $v$ 与旧 $\nu_j=2^{-432064}J^{-4166}\delta^{671/20}$
之比只引入一个有限常数；
原深端差的余幂仍大于33。
因此实际平均高度/total flux 与所用径向 mean 两迹的差趋0。
新增有限根不改变这个极限，根处非zero模式的
$(M/b)^{-1/3},(M/b)^{1/3}$ 初值及两个 true mean 仍都保留。
所以 (Z.19) 的 $\ell$ 正是归一化实际物理平端高度。

更明确地，remaining 的算子域取所有 $\|vx\|<\infty$、
$A_ax\in\mathscr Y$ 的真实分布解迹，其 high/deep 按 Y.28 的
齐次 Poisson 重建，并另要求 (Z.3) 的物理两迹。
有独立 high/deep particular 时先减其已付真实解，再用此域。
不把这项域定义替换成裸加权序列空间。

唯一性也在这个声明域中证明。若 $A_ax+\sigma_\circ\tau=0$、
$\ell x=0$，则用 (Z.17) 得
$x=R_\circ\Delta Sx$，
故 $\|vx\|\le\eta\|vx\|$，$x=0$，继而 $\tau=0$。
不允许有非零平端恒定通量的奇异解混入这个域。

## 7. 真实兼容泛函和实际一维核

对实际同一个 rooted 网络，令 $\mathcal L_a g$ 为所有 source
在物理 mean total-flux 中产生的有向跳和。
先在有限角/有限根源上按真实 Piola、根 density、normal shear、
共同 $H_a$ 和 (Z.7) 的方向定义，再连续延拓。
这个定义保留全部非zero角模；实际 physical mean 不是 canonical mean。

延拓的数值门可直接核。每个根的准确
$\langle\sqrt\alpha(u_\xi-\ell_\xi u/2)\rangle$
使用原两个 Airy 初值。常数 Fourier 测试只作用 mean；
非constant 测试由根解析密度的 $H^{1/3}$ 范数支付，
其费用为 $2^{48}b_e^{1/3}n_e$。
全部真实根均已付 $b_e^2n_e<2^{-512}$；
共同 $H_a$ 在 $L^2$ 酉而保持 mean。
因此每个完整 flux source 行可用 $2^{1024}\sqrt{q_e}$ 收费。
(Z.4) 的平方和给
$$
                     \|\mathcal L_av\|<2^{-460000}.
 \tag{Z.21}
$$
没有要求一个未付的高频裸法向 $L^2$ 迹。

在最后根，对 $\sigma_\circ$ 使用 $H_a|_{\rm mean}=I$，
其 physical flux 系数准确是
$$
 \beta_{\ast,a}
 =\text{同一接线号}\,\varsigma_\ast c
 \left\langle
 \sqrt{\alpha_\ast/(\varepsilon_s/\rho)}
            (i\sigma_\ast/\pi-\ell_{\xi,\ast}/2)
 \right\rangle .
 \tag{Z.22}
$$
真实背景下其 imaginary 部分是非零的正密度平均乘固定号。
新 A.19--A.25 的完整相对密度及其一阶根导给
$|\beta_{\ast,a}/\beta_\ast-1|<2^{256}n_0<1/2$，
所以
$$
             \mathcal L_a\sigma_\circ
               =\beta_{\ast,a}/\beta_\ast\ne0 .
 \tag{Z.23}
$$
这明付最后根的实际单位；没有仅从“Fredholm 指数应为零”猜测分母。

对每个真实局部齐次段，平均 total flux 守恒。
相邻段的全部 jumps、最后自然 mean 线和平端零通量相加，给
$$
                         \mathcal L_a A_ax=0 .
 \tag{Z.24}
$$
先对有限源构造使用准确 Green 恒等式；
(Z.13)、(Z.21) 和 Y 的高/深域门使无穷端的 flux 项趋0。
这是同一声明域上的恒等式，不是对所有形式弱序列的断言。

将 (Z.24) 用于 (Z.19)，准确有
$$
 \tau={\mathcal L_ag\over\mathcal L_a\sigma_\circ},
 \qquad |\tau|<2^{-459999}\|v^{-1}g\|.
 \tag{Z.25}
$$
因此**真正可解条件恰为**
$$
                            \mathcal L_ag=0 .
 \tag{Z.26}
$$
满足它时，(Z.19) 给唯一指定物理高度 gauge 的完整解；
不满足时，辅助 $\tau$ 明确记录尚未闭合的真实通量荷，
不能把它宣称已由其它参数自动消去。

取 $g=0,\lambda=1$。实际物理常高度已是允许域中的一个解，
故由 (Z.19) 的唯一性，该解恰为所得 $c_a$，且 $\tau=0$。
任意真正齐次解减去 $c_a\ell x$ 后为零。因此
$$
 \ker A_a=\mathbb Cc_a,\qquad
 \operatorname{Ran}A_a=\ker\mathcal L_a
 \quad\text{于上述真实平端域与 }\mathscr Y\text{ 中}.
 \tag{Z.27}
$$
$u=\sqrt\alpha\,h_{\rm const}$ 的全部角模包含在 $c_a$，
没有把这个核替成一个纯 canonical mean 槽。

## 8. 全物理 source、独立 C_R 与剩余帽联立

令原数据沿准确有序 source map、两外消元成为 $k$。
在 (Z.26) 中应使用 $\mathcal L_a k$。
这条荷不是仅取 $k$ 的 canonical 零 Fourier 系数：
root 密度、mean shear 和 $\dot H_a^*g$ 等均参与真正物理平均。

对于含体源、两 weak 源及径向原子的实际解，原方程仍给
$$
 q_R-q_f=\int f_0(t)\,dt+\sum_{\rm atoms}[\pi]_0,
 \qquad \pi=\mu(h_t-dh_\theta)+F^t .
 \tag{Z.28}
$$
按真实正负方向将端荷移到同一边，这正是 (Z.26) 经完整原
source map 的表达。可先在紧支光滑源与有限原子上逐段核，
再在其原已付积分、端迹和本篇 source 范数中取极限。
角 weak 项的平均散度为零，但 $F^t$ 的 total/bare 端荷没有消失。
一般 $L^2$ 体源本身仍不赋予裸 $F^t$ 端点值。

实际求解次序完全明确：先用 Y.28 形成 $k$，再在
$\mathscr Y$ 解 (Z.18)，核 (Z.26)，最后按 Y.28 重建 high
及全部无限 deep-low，并依原两行 Piola/frame 恢复物理场。
这给 fixed-$C_R$ 的完整全频 Jacobi 解，商去唯一整体物理高度。
其两端高度差及新 long mean particular 仍用原 N.24--N.25，
没有以通量兼容替代真实高度跨度。

独立 $C_R$、两条曲率 mean、$\nu$、两 $D\Gamma^*$、
材料 source 与参数 Cauchy 仍逐列通过同一个逆。
尤其本篇不把 $\tau$ 当作一个可自由物理调参，
不把 N.23b 的帽内 $q_m(R)$ 图或只在共同偶反射类证明的帽解
提升为任意固定背景的 all-$4\mathbb Z$ full cap。

接下来的实质问题已缩成：在原强 ordinary/weak source 和标签权
中消费上述 inverse 的双向 map，写出实际帽侧 $C_R$ 响应、
两条曲率 mean 和 $\nu$/joint 行的完整 Schur，并闭合非线性剩余。
这些费用没有被 (Z.20) 的弱端口界自动支付。
本篇完成的是固定 $C_R$ 全频网络的真实核、range、兼容与 gauge，
不是课题最终完成声明。
