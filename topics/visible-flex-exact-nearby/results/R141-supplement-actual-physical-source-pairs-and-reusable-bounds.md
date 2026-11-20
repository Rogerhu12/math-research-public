# R141 补篇：实际物理源对、原径向尾和已成大小的接线

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**状态：已证明（准确源对及其完整上界合同）；新四标量消费者尚未执行。**

本篇接[两条 WPN 行的准确提升](R141-supplement-both-WPN-rows-by-exact-WOB-source-lifting.md)。
那一篇给任意两行输入的未来响应合同；本篇确定具体物理输入应放入哪一行，
并分开已有完整源大小和仍未取得的实际端口。没有执行新科学计算，没有重跑
WOBSA、旧 residual 或旧观察生产器，也没有构造尚未产生的 224 或 32 球结果。

## 1. 保持唯一算子和两条右端

所有符号保持 [WOB.24--31](R133-supplement-complete-outer-rows-and-signed-root96-inverse-certificate.md)、
[WDS.2--3](R133-supplement-two-sided-tail-residuals-and-true-finite-Schur-certificate.md)
和前篇 L.24。区间为
$I=[r_*,R]$，$R=25/8$，角测度为原归一化 moving 圆周。
低空间 $E_L$ 有 odd96、even nonmean96 和 independent even mean1。
输入 endpoint193 使用 raw 正交坐标；它不是未知量中加权的 outer96。
只有原 WPN 未知的 outer96 坐标乘 $\Theta$。

令 $c_*$ 为指定的 root even96，$x\in X_{\rm fr}$ 为原冻结高输入，
$p=(\delta f_B,r_B,r_C)$ 为真实物理外端数据；独立低跳按右减左记为
$j_\alpha$ 并位于 $\tau_\alpha$。原 high particular solution 和观察为
$v_p,y_p$，其源对低空间的作用为
$$
 q_p=B_{LH}v_p+g_L .
 \tag{S.1}
$$
这里 $g_L$ 是真正 ordinary raw $L^2(dr;E_L)$ 源，含 even mean。
整个原零 IVP 的实际右端恰为
$$
 \boxed{\begin{split}
 F={}&C_*E_cc_*+V_0\Phi x+V_0q_p
                  +\sum_\alpha{\bf1}_{(\tau_\alpha,R]}j_\alpha,\\
 e={}&Q_L B_{R,p}p+B_R^Hy_p-V_Rq_p-\sum_\alpha j_\alpha
             -E_cc_*-(V_R\Phi-B_R^H\Upsilon)x .
 \end{split}}
 \tag{S.2}
$$
因此原两条 WPN 输入是
$$
 f_f=(E_N^*SF,e),\qquad g_t=Q_NSF,\qquad N=24480,
 \tag{S.3}
$$
并准确有
$$
 \|f_f\|^2+\|g_t\|^2=\|SF\|_{L^2}^2+|e|^2.
 \tag{S.4}
$$
式 (S.2) 先保 signed 函数和完整 endpoint，再按所需精度取范数。
不能把上端的 $-V_Rq_p$、$-j_\alpha$ 或 $-E_cc_*$ 删除。
不能从两个有限矩得到 $g_t$，也不把一般 $L^2$ 函数 $F$ 赋予端点值。
前篇的有迹提升 $w$ 仍是恢复独立 $d,b$ 的唯一对象。

原 $\Phi,\Upsilon$ 只观察同一个 genuine 高列；$N_i$ 已在共同右端一次。
若改从原 stable $H^{-3/2}$ 数据 $s$ 出发，使用 WOB.16 的完整
$\Phi_{\rm rough}s,\Upsilon_{\rm rough}s$。这是一种替代表示。
同一物理 incoming cause 不得既计为 $x$，又计为 $s$，又计为七端口 stable。
确实不同的独立 cause 可以先分别接线再相加。
rough 观察延拓不授予一个不存在的 whole high raw $L^2$ 基线。

## 2. 每种数据同时出现在哪两行

| 原物理输入 | $F$ 的准确增量 | $e$ 的准确增量 | 不能省略的部分 |
|---|---|---|---|
| root even96 $c_*$ | $C_*E_cc_*$ | $-E_cc_*$ | root mean 属于另一独立 97 维未知，并未设零 |
| 冻结 incoming $x$ | $V_0\Phi x$ | $-V_R\Phi x+B_R^H\Upsilon x$ | 原反射子空间、$D_+$、$N_i$ 的次序 |
| ordinary $g_L$ | $V_0g_L$ | $-V_Rg_L$ | 全低 mean、原径向尾 |
| 独立 high particular $v_p$ | $V_0B_{LH}v_p$ | $B_R^Hy_p-V_RB_{LH}v_p$ | 真外迹和 97..288 接收壳 |
| low jump $j$ 于 $\tau$ | ${\bf1}_{(\tau,R]}j$ | $-j$ | 同源两项，非 $L^2$ Dirac |
| 外 height / Robin / scalar mean | 经其 actual high affine 列进入上述 $v_p$ | 另加 $Q_LB_{R,p}p$ | high 和 low 两路径同时保留 |

外端三项使用原单位
$$
 F_B=\||D|^2\delta f_B\|_{H^{-5/6}},\qquad
 R_B=\|r_B\|_{H^{-5/6}},\qquad R_C=|r_C|.
 \tag{S.5}
$$
$r_C$ 是正则外图的独立物理 mean residual，进入原完整 chart 后才成为
moving endpoint mean；它不是可直接从 $r_B$ 删掉或合并的常数槽。
WOB.7 的完整 raw193 外列已经包含这一 chart 和 $\mu_F,\mu_C$。
normalized nonmean height $f_B$ 也不是任意 physical height：
若 $y_B=s_Bf_B$ 同时变动，准确方向是
$\delta f_B=(\delta y_B-f_B\delta s_B)/s_B$。
整体 height gauge、height span、腰幅度和两物理 mean 的其它全局方程
仍是各自原端口，不能用 (S.5) 三项取代。

## 3. 原 fine mesh 的普通源尾与真实低跳尾

在原第 $i$ 个 fine cell $I_i=(l_i,r_i)$ 上，$h_i=r_i-l_i$，
$S=S_i$ 为原精确常数矩阵。这里始终是 WVC/WPN 的 **24480** 格；
155 comparison panels 或 R141 的 1424 certification cuts 不改变这个投影。
定义 $\Lambda_h|_{I_i}=h_i/\pi$。对 ordinary raw 源 $g$，
逐格去均值的 Neumann--Poincaré 不等式给
$$
 \boxed{\quad
 \|Q_NSV_0g\|_{L^2}\le\|\Lambda_h Sg\|_{L^2}.
 \quad}
 \tag{S.6}
$$
证明是每格 $(SV_0g)'=S_i g$，并按真正普通 $dr$ 将各格平方相加。
不对源求径向导数。若源准确写为 $g=S^{-1}f$，则 (S.6) 右侧
准确为 $\|\Lambda_h f\|$，不能先粗乘一个额外 $\|S\|\|S^{-1}\|$。
若只知道 raw 源范数，才可用
$\|\Lambda_h S\|_\infty\|g\|$。

若某个 $\tau$ 在一格内部，置 $a=\tau-l_i$、$b=r_i-\tau$。
该阶跃在其它格均为常数，故准确有
$$
 \boxed{\quad
 \|Q_NS{\bf1}_{(\tau,R]}j\|^2
       ={ab\over a+b}|S_i j|^2 .
 \quad}
 \tag{S.7}
$$
这是两个常值 $-b/(a+b)$、$a/(a+b)$ 的直接平方积分。
若 $\tau$ 是原 fine cell 边界，尾准确为零。
若真根不确定性导致所在 cell 未被确定，消费者须保所有可能所在格并取完整
上界，不能从一个中点格号宣称尾零。保守备选为
$\tfrac12\sup_i\sqrt{h_i}\|S_i\|\,|j|$。

多个 jump 在同一格的 tail 可以相关。最小实现使用
$$
 J_T=\sum_\alpha
  \sqrt{a_\alpha b_\alpha/h_{i(\alpha)}}\,|S_{i(\alpha)}j_\alpha|;
 \quad
 J_E=\sum_\alpha|j_\alpha|;
 \quad
 J_B=\sum_\alpha
 \left(\int_{\tau_\alpha}^R|S(r)j_\alpha|^2dr\right)^{1/2}.
 \tag{S.8}
$$
这些分别界 tail、endpoint 和 weighted body；允许先完整 signed 合并再取更紧界。
没有声称不同 jump 的输出正交。一般的安全 body 上界是
$J_B\le\|S\|_\infty\sum_\alpha\sqrt{R-\tau_\alpha}|j_\alpha|$。
原七端口中的 high weighted jumps 与 (S.8) 的 raw low jumps 是不同分量；
二者先按真实投影和原 frame 分开，不能只付其中一项。

## 4. 可直接复用的完整 WOBSA 球

已只读核对原 [run 43844596176/1 完整结论](R133-supplement-actual-complete-outer-rows-and-rough-positive-observations.md)：
science 为 60416 B，SHA256
ba8e647cc4572333407b8979f98315e94dbab53ff2ff0086fe1d1dcdb0f17b79；
execution 为 15866 B，SHA256
b9022fe012e2e0f5db8186dda91a5ec1f2eb3222eb7af4ea02a9dd5ec41fdb57。
路径为 notes/outer_rows_and_rough_positive_observations_ci/run-43844596176-1/。
原 10 pins 的 bytes/SHA/gitblob 当前逐一相符；完整 42 旧 records 和 73-path
qualification projection 的原 canonical SHA 相符；18 门、6 图、37 新球、
4 条完整 README 链均相符。没有解释为新 inverse 证书。
这些整体观察的资格仍是原 selected member；个别外图和 high receiver 的
full-real-$\delta$ 资格不自动把整张 $\Phi,\Upsilon$ 表改称 uniform。

下表所有键以前缀 complete_new_graphs.[graph].complete_new_records 读取完整
保存对象。显示量只作定位，实际消费解析整个原 ball 后取有向 upper。

| 记号 | graph / record | 已有数学资格 |
|---|---|---|
| $K_{RH}$ | complete_outer_low_and_affine_rows / complete_high_outer_row_upper | 全 high 外迹到 raw193，含独立 mean |
| $k_F,k_R,k_C$ | 同图 / complete_affine_fB_low_pair_upper, complete_affine_rB_low_pair_upper, complete_affine_rC_low_pair_upper | 三个物理输入的完整 raw193 affine 列 |
| $K_\Phi,K_\Upsilon$ | complete_genuine_and_rough_observations / complete_Phi_upper, complete_Upsilon_upper | 原 $X_{\rm fr}$ 到 raw low ordinary / actual outer high 观察 |
| $K_{\Phi r},K_{\Upsilon r}$ | 同图 / complete_rough_head_observation_upper, complete_rough_outer_observation_upper | 原 stable $H^{-3/2}$ 的兼容观察，非 whole body 逆 |
| $B_x,D_x$ | complete_zero_IVP_rows / complete_B0_high_body_row_upper, complete_D0_high_endpoint_row_upper | $\|V_0\Phi\|$、$\|V_R\Phi-B_R^H\Upsilon\|$，保整行 |

原 copied_original_scalar_records 的 C_V0、C_R0、L_star 分别记为
$v_0,t_0,L_*$。不重新算其旧目标。
原 high 结果的 response_rows.entire_positive_raw_L2r_Hminus1、
response_rows.body_Y_sup 是完整七项 $\mathbf c,\mathbf y$，
exterior_affine_Y_output_coefficients 的索引 1、2、3 是
$\beta_F,\beta_R,\beta_C$。该 whole negative-window 结果正是 WOBSA
accepted_old_inputs.originals.negative 所绑定的原对象。

另读已成 D-lift 的 reference_weighted_right97_body_upper 为 $d_B$。
前篇 L.17 已证明它也支配 $\|SC_*E_c\|$，利用同一独立 mean 的 constant
body $q(r)$，不重算 D 的旧目标，不加 $\sqrt{96}$。

## 5. 一个实际数据包的四个新标量

令 $\alpha$ 为七个已知 high particular 输入大小，在这里它的第 3 槽
**尚未**加入同一 $p$ 的 physical affine forcing。先置
$$
 \widehat\alpha=\alpha+
   (0,0,0,\beta_FF_B+\beta_RR_B+\beta_CR_C,0,0,0).
 \tag{S.9}
$$
未知 outer low $b$ 的 $\beta_b b$ 不进入此 RHS，它已经属于原 WOB 算子。
记 $s_*=\|S\|_\infty$、$m_h=\|\Lambda_hS\|_\infty$、
$\lambda_h=\|\Lambda_h\|_\infty$；这三个量须来自同一原精确 fine-mesh
descriptor。不能以 v3 的 binary64 balance 或认证新 cuts 代替。
raw low 源大小为 $G$，可选准确 transformed 源 $S^{-1}f_L$ 大小为 $G_S$。
它们是不同已知源时可以相加；同一源只能选择一种表示。
由原 $q\ge1/8$，$\|S^{-1}\|\le8$。置
$$
 C_p=\mathbf c\cdot\widehat\alpha,\qquad
 Y_p=\mathbf y\cdot\widehat\alpha,\qquad
 Q_p=1153L_*C_p+G+8G_S.
 \tag{S.10}
$$
$1153$ 只支付完整 high-to-low receiving shell97..288 的
$H^{-1}\to L^2$ 变换，不截断 $v_p$。

以 $X=\|x\|$、$U=\|s\|_{H^{-3/2}}$、$C=|c_*|$ 表示各自有资格的输入，
一个保持全部路径的完整预算为
$$
 \begin{split}
 B={}&d_B C+s_*\{B_xX+v_0K_{\Phi r}U+v_0Q_p\}+J_B,\\
 E={}&C+D_xX+(t_0K_{\Phi r}+K_{RH}K_{\Upsilon r})U\\
    &+k_FF_B+k_RR_B+k_CR_C+4K_{RH}Y_p+t_0Q_p+J_E,\\
 T={}&m_h\{K_\Phi X+K_{\Phi r}U+1153L_*C_p+G\}
                         +\lambda_hG_S+J_T .
 \end{split}
 \tag{S.11}
$$
这里 $B\ge\|SF\|$、$E\ge|e|$、$T\ge\|g_t\|$，而
$$
 \boxed{\quad
 P=\sqrt{B^2+E^2}\ \ge\
       (\|f_f\|^2+\|g_t\|^2)^{1/2},\qquad
 \|f_f\|\le P,\quad \|g_t\|\le T .
 \quad}
 \tag{S.12}
$$
这只用输入各块的正交性计算同一 body/endpoint 直和，不把不同 cause 的
输出说成正交。若取得完整 signed projected functions，可以直接计算
$\|E_N^*SF\|$ 改善 finite 行；(S.12) 是无需伪造这些数组的合法上界。
不能用 $\sqrt{P^2+T^2}$ 反称准确 pair 大小：$P$ 已包含整个 body。

配套纯模块只保存 $B,E,P,T$ 四个新记录。每个先 emit 完整球、验证保存
包含原 upper，回读 upper 后才进入后继式。旧 WOBSA 数字均只读。
只有每项输入真实存在且身份匹配时，才可执行本四标量目标；
缺少 $\alpha,c_*$ 或某个 independent residual 时返回缺项，不能填零。

如果未来两行 32 球已经完整成功，则其任一输出满足
$$
 \|O h\|\le U_{f,O}P+U_{t,O}T .
 \tag{S.13}
$$
同一 $F$ 的 finite 与 tail 不是独立产生的两个物理原因；(S.13) 用三角。
本篇不生成这些 future 球。还须另加已知 $v_p+\Psi_A N_i x$ 的合法
high 观察，才是完整 high 解；前篇返回的 zero-independent-high part
不自动包含这个 baseline。

## 6. 真正 $\nu$ 列：可以置零的只有已证那一项

在固定物理 $Q=(u,v)$ 下，
$$
 F_\nu=w'A_\nu+wB_\nu,\qquad
 \operatorname{supp}w=[1/20,9/50],
 \tag{S.14}
$$
其中 $A_\nu,B_\nu$ 采用[原完整物理参数源](R133-supplement-actual-signed-nu-pairing-and-all-product-jumps.md)
的 mean 和 primitive 定义。
由于 $r_*>9/50$，在整个 $I$ 上
$F_\nu|_I=0$ 是准确恒等，非数值小量。

exterior 的参数结论还使用完整 metric 定义
$E_\nu=E\exp(\nu w)$、$a_\nu=a$，而非只用局部源等于零。
[原正帽定理第 1 节](R133-supplement-A0-contraction-and-translation-regularity.md)
明确证明其整个帽区间的 $g_\nu=g_0$。
其外侧采用 [R119 的完整长径向段 D.1--D.11](R119-supplement-actual-long-radial-nonlinear-dirichlet-problem.md)
和[真实帽—长段匹配 M.1--M.3](R133-supplement-actual-positive-cap-and-periodic-long-tail-matching.md)：
在固定 $\eta_0$ 下，实际 $a_*e^{-\omega u}$、$w=a/(4\omega)$、
整段度量与两端原坐标均未被这个内侧紧支 $\nu$ 控制改变。
[完整 nonlinear 外图 S.2、S.36--S.38](R133-supplement-final-regular-Hs-and-Riccati-outer-graph.md)
于是是在同一整个 exterior 上、以同一物理曲率和同一 height 输入定义的唯一图。
固定这些输入时其显式 $\nu$ 导数为零；state 变化仍由该图的全微分支付。
故纯物理参数响应取 $\delta f_B=0$ 时没有**显式** exterior mean source。
真实 mean **输出**仍由 $\mu_R y$ 给出，通常非零。
原 [mean-completed-body 定理 D.2](R133-supplement-mean-completed-head-and-adjoint-body-consumer.md)
已明确这个区别。

因此直接 $\nu$ 正区列的 (S.2) 仍必须接入由负区、germ 和真正匹配取得的
$c_\nu,x_\nu$ 或对应 stable 数据，以及任何真接口/外部独立输入。
紧支撑恒等不证明这些数据为零，也不提供其大小。
若使用 normalized $U,V$，参数方向还含 $s_\nu$ 链式列；
先转到原物理方向，不能将其另外再加到 (S.14)。

有一种已明确的 alternative：以 **连续** $Z$ 为全域已知 proposal，
写 $q_\nu=Z+z$。在 $\delta=0$ 的同 Qrepair 上
$$
 (\partial_r-A_0)z=s_0,\qquad
 s_0=F_{\nu,0}-(\partial_r-A_0)Z .
 \tag{S.15}
$$
完整 [run 43613560173/1](R133-supplement-actual-complete7721-continuous-Z-source-cover.md)
已付 $s_0$ 的 full、low193 和 high97..160
三种普通源，包含 raw even mean 与两 repairs。不得改用
$q^\sharp=q_{\rm raw}+e_{\rm mean}(r)e_2$ 的旧上界并忘记 raw mean；
三对象的区别见已发表 [MC](R133-supplement-raw-response-mean-identity-and-corrected-collar-source.md)
和 [RF](R133-supplement-complete-core-residual-reuse-for-the-selected-centre.md)。
本篇不重复 RF 的 source 证明。

原 whole small summary 的确切字段是
complete_source_bounds.full_body.[species].L2_L2_radial：

| species | 原完整 upper 的外放显示 | 可复用范围 |
|---|---:|---|
| full_through160 | $2.725862\,10^{-6}$ | 全 $[0,25/8]$，含独立 mean |
| low193 | $2.723698\,10^{-6}$ | 同一 $Z,Q_0,\eta_0,\nu_0$ 的低源 |
| high97_through160 | $1.961163\,10^{-6}$ | 同一已知高输出，非未知 high 截断 |

在 $I$、collar/body 的限制可以先用原整个球；更紧限制只消费原 7721
完整行和真实交集，不重新生产源。$H^{-2/3}$ 输入范数可由同一 $L^2$
源收缩控制；不由此得到 stable/germ 端口。$Z$ 全局连续，所以它自身
没有 value-jump Dirac；若改变投影、frame 或切口，变换后的真实接口仍须付。
这些 source 球在 $\delta=0$，而 WOBSA 的共同高观察保原 selected-member
身份；列在同一复用表中不等于已完成共同准入。实际消费必须匹配同一 member，
或另付原已证 selected source/operator 差。不能由 $10^{-10}$ 很小省略这一步。

这些球不包括同一 $Z$ 的全部 waist/actual outer/$r_*$ 匹配。
原 [43599771405/1](R133-supplement-actual-complete-known-response-boundary-sources.md)
的已知 boundary 球属于 $q^\sharp$、
waist0 和 cap cut $9/10$。它不是 $Z$，也不是当前 $R=25/8$
的 (S.2) endpoint。只能在其原切帽方案中整包复用，不能把那一个
$g_R$ 填入这里的 $e$。

## 7. 真正 Newton 源和还可以复用哪些大小

令 $f_\delta=(Q_\delta)_r-\mathcal F(Q_\delta,\nu_\delta)$。
Newton 线性步的 ordinary 源为 **$-f_\delta$**。
若保完整 nonlinear equation，则
$$
 (\partial_r-A_\delta)h=-f_\delta+
 \{\mathcal F(Q_\delta+h)-\mathcal F(Q_\delta)-A_\delta h\}.
 \tag{S.16}
$$
外端则是同一真实 nonlinear boundary residual 的负值，加其完整
nonlinear remainder 的负值。它们必须在物理角、同 height、同 mean
规范下形成 $p$，不能拿 Robin derivative norm 冒充 boundary residual size。

已成[原 moving residual](../notes/2026-11-14-R133-final-complete-moving-residual.md)
覆盖 7296 全闭行和 6143 接口。
其 $R_U,R_V$ 是 **normalized** 源，物理 source 必须乘准确
$\alpha=6890507429876859/9007199254740992$。
Qrepair 的 ordinary residual 另含完整
$-\{\mathcal F(Q+e)-\mathcal F(Q)\}$，而 value jumps 已准确消去。
RF 给的 whole-core 转授和
[X.10--11a](R138-supplement-complete-physical-residual-multiplier-budget.md)
从 7722 角闭行恢复 residual 的方式
均是可用原证明；X 已成 feedback/transport 组合常数不是新的独立
$\|f_0\|_{L^2(I)}$ 源记录。

在 $\delta=0$，Qrepair degree32，完整 field degree96，故
$$
 Q_H f_0=0 .
 \tag{S.17}
$$
这是已登记 [R.20](R133-supplement-selected-centre-complete-residual-and-collar-source-bounds.md) /
MC.11 的准确支集，不必再计算一次。它只说明当前
Newton known forcing 没有直接 highordinary 源；未知 $h_L$ 对 high
的反馈仍完整保留。在 $Q_\delta=Q_0+\delta Z$ 下 degree96，正区的准确
展开为原 R.17
$$
 f_\delta=f_0-\delta s_0-\delta^2T_2-\delta^3T_3 ,
 \quad
 \deg(s_0,T_2,T_3)\le(160,224,288).
 \tag{S.18}
$$
不能把 (S.17) 赋给非零 $\delta$。若消费旧 scalar budgets 而非新的
signed source，必须保 MC 的 raw mean，或直接使用已完整付清 mean 的
43613560173 球，不能重复加同一 fee。

具体外端 Newton 数据也可直接从原 physical 图命名，避免把 source norm
和 derivative norm 混为一谈。令同一物理角中的
$(B_\delta,C_\delta)=\Psi(Q_\delta(R))$，
$\mathcal Z_\delta=P_{\ne0}(C_\delta-C_{\rm ref})$。
固定当前真实背景 $f_B$，外图 S.2 给
$$
 \begin{split}
 r_B^{\rm Newton}
   &=-\{\mathscr J_\theta B_\delta+Q_\theta\mathcal Z_\delta
                                -d(\mathcal Z_\delta,f_B)\},\\
 r_C^{\rm Newton}
   &=-\{m_\delta(R)^{-1}-C_{\rm ref}
                                -c_0(\mathcal Z_\delta,f_B)\}.
 \end{split}
 \tag{S.19}
$$
第二式使用准确 physical mean $\langle C_\delta\rangle_\theta=1/m_\delta$；
没有把它替成 moving $\langle C_\delta\rangle_\phi$。
这两项还未经过 WOBSA 的 onto chart；其大小应在 (S.5) 的原空间验证，
随后完整三列才作用一次。已成 graph derivative 只能在其真实同一凸球上
控制 $d,c_0$ 的差，不能直接被宣布是 (S.19) 的 residual 大小。
若非mean height 是待联立的另一个未知坐标，它的微分列属于增广算子。
允许的 background height radius 不等于一个已知 Newton height RHS；
整体 height gauge 与实际 tail-label 方程仍须独立接合。

| 已有完整证据 | 已付对象 | 当前接线可直接用什么 | 仍缺什么 |
|---|---|---|---|
| WOBSA 43844596176 | 原 selected-member 观察和外 affine 列 | 本篇 (S.11) 的 receiver 常数 | 各实际数据范数及整 positive inverse |
| mixed $Z$ 43613560173 | same $Q_0,Z$ 全 ordinary discrepancy | (S.15) low/high 已知源大小 | 同 $Z$ 的真边界、负区/germ/匹配与 inverse |
| 7296 moving residual native | original raw M32 nonlinear residual | 完整 normalized $R_U,R_V$，再付 physical amplitude/repair | 同 positive 修补源组合的新小 scalar，非零 $\delta$ 完整 remainder |
| RF + WL + D | 全 $[0,9/10]$ selected core source 的显式已证组合 | 在其原 interval/parameter 内直接复用合同及旧球 | 不能直接把 core 界延至 $25/8$ |
| 43597921732 | $q^\sharp$ 修补 residual；也给 RF/MC 的保守 nonmean fee | 其准确同对象 ordinary 源或 MC 指定正预算 | 不等同 continuous $Z$，不自动付 raw mean |
| 43599771405 | $q^\sharp$ waist0、true cap cut $9/10$ 已知源 | 原切帽方案的完整 96/97/high data | 非 $Z$，非本篇 $r_*,25/8$ 两端 |
| exact $Q_0,Z$ continuity repairs | 这些特定函数的完整 value interface | 它们自身的 raw value jump 恰零 | 无关 iterate / high-frame / 投影的独立 jumps |
| genuine exterior graph | DN/mean/chart 的导数和 affine receiver | 给定 $F_B,R_B,R_C$ 后完整三列 | 实际 nonlinear residual 的值及 whole height/gauge 荷 |

## 8. 下一可执行消费的边界

配套 fourfold_codazzi_physical_WPN_source_pair_math.py 是四标量的纯运算核心，
不导入数值库、不读文件、不调用任何旧 producer。owner 须先完整 admit
WOBSA/negative/D/mesh 和实际 data packet；成功保存每个新球后回读 upper。
没有实际 data packet 时它只能给出明确缺项，不运行一个零填充的“完整右端”。

本篇的正区 source-pair 接线并不构造负区解、germ 连接、真实 root 输入、
waist/metric/phase 方程或参数 Schur；也不把 actual $G_H$ 改名为 WJK 的
finite trial $F$。若后续继续原 finite-$\rho$ 方案，必须使用原已发表桥并
另付其 residual；本直接 WOB 路线的合同不能把那个未付门设为真。
最终实际 $\nu$ 或 Newton 两行通过的声明，须同时有真实数据身份和大小、
完整 signed/full-space inverse、原有限/径向尾的两次作用以及所有独立匹配项。
