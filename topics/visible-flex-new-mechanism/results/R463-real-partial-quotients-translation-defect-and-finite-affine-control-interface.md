# R463：同宽全角色 partial 的真实二项商、平移放大的缺口与有限仿射控制接口

日期：2026-11-16。**已发表原式的只读消费与完整纸面证明。没有执行新科学、旧秩、profile、积分、符号程序或人工检查。**

[R459](R459-one-common-signed-witness-for-all-internal-fluxes-of-the-equal-width-library.md) 已给同一个实际宽度、全部角色及全部对应副本的 signed 成本 $V_\#$，它满足原共同 $J^+=0$、全部内部 partial 零及 $\lambda_+(V_\#)=1$。其最后响应 $W$ 可以混合真权。本稿不将这个 signed 见证提升成已经支付的 actual 路径。

本稿的三个具体结论是：

1. 当前全角色 partial 确能从原有限位置读取 $D_5,D_6$。它们杀整个响应空间，而 $H_*,J_4,J_6\in\ker J^+$ 的 $D_5$ 已非零。因此，**当前整个 partial 的 vertical response-cover 不成立**，不是仅有一个未查的满秩前提。
2. R206/R333/R428/R433 的纯缩放商截面不能只把 $D$ 换成真实平移 $N$。放大主微分只到 $NQ$，真实桥仍保留但仅为 $O(1)$；准确余商是 $Q/NQ$。当前新映射已有非零的 $D_6$ 读出落在这个余商中。补正伸缩闭包以后，$D_5$ 又给一个非零零权类，故旧“$D$ 单独可逆”的证明也不能原样照搬。
3. 这些事实**不证明 actual 增强不可能**。同一完整商上的较弱条件
   $DQ+NQ=Q$ 已足以重作真实两参数放大、两次商校正与最后有限响应根。另给一个最多十三个近一正伸缩的有限闭包合同；它不是无限物理宽度要求，也不是新秩结果。

主要来源为 [R127](R127-positive-affine-character-of-the-fourth-cost-cone.md)、[R145](R145-true-curvature-reflection-and-even-positive-characters.md)、[R206](R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md)、[R212](R212-C1-sections-for-complete-real-pure-cost-control.md)、[R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)、[R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md)、[R428](R428-conditional-complete-joint-cost-cone-and-finite-actual-C1-sections.md)、[R429](R429-complete-kk-minus4-values-and-actual-common-joint-sections.md)、[R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md)、[R456](R456-two-highest-ordered-current-invariants-on-real-mirror-copy-families.md)、[R457](R457-natural-seven-current-quotient-complete-normalization-and-weight-zero-witness.md)、R459 和 [R462](R462-five-dimensional-complete-weight-zero-current-kernel-and-all-width-self-interface.md)。所有成本、原型、真实倒行与积分均保持原共同锚。

## 1. 固定映射、原式延拓及“固定宽度”的两种含义

沿原真实空间记
$$
\mathcal S=\{V_B:B\text{ 有限真实同 scalar/frame 端口},\
M_B=\mathbf T_B=0\},\qquad
U=\operatorname{span}_{\mathbb R}\mathcal S,
$$
并记完整响应空间为 $\mathcal R$。固定 R459 从起点构造的同宽库，置
$$
J_0=J^+=(E,\mathcal A,\mathcal O_{\rm all}),\qquad
E=(\pi,\mathcal Q).
\tag{1}
$$
这里 $\mathcal A$ 已是 R429/R433 的共同有限正仿射查询闭包；它不是 universal self 自然函数。R433 已给同一个 $J_0$ 的实际有限 $C^1$ 截面。

令 $F$ 是该库全部原角色、全部真实镜点的两通道内部累计量。每一行必须在整个 $U$ 上先有一个确定的真实线性延拓，不能只在 $\ker J_0$ 中写局部 current，再把它用于非零 prototype 基准。

一种直接延拓使用原第四算子的固定相位查询。对每个实际圆的固定 $f,g$，置
$$
D_V^\circ=V(f^2,g),\qquad
E_V^\circ=V\!\left(f^2,\frac{f+g}{\sqrt2}\right)
-\frac12V(f^2,g).
\tag{2}
$$
在 $\pi V=0$ 时，R333/R159 的完整相位式给
$D_V^\circ=D_V$、$E_V^\circ=-G_V$。因此原左锚到每个活动包退化点的
$\int f'(D_V^\circ)''$ 与 $\int f'(E_V^\circ)''$，按 R459 原角色规范取行，正是 $H_d,H_e$。式(2)在 $\pi V\ne0$ 时仍是有限真实原式查询。它不删真左尾、不改变 incoming history，也不在离开核后继续套用 pure-zero 极化身份。

以下所有关于 $F$ 的核、商和 prototype 成本均使用这个同一个延拓。换成另一个在 $\ker J_0$ 上相同的线性延拓，只相差经 $J_0$ 因子化的行；联合映射的核和下面的 vertical 商不变。

“最终 profiles 始终是固定宽度”不等于“实际控制块不使用正伸缩”。R428 的实际截面在整个目标邻域中不移动最终 profiles，却确实使用随参数变化的 $B_i^{e^{t_i}}$。由原共轭协变，考察这些成本等价于在原成本上查询共同伸缩后的 profiles。新增 $F$ 是否允许这个有限闭包，是另外一项数学条件。

## 2. 从原全角色 partial 直接读出 D5、D6

这一节只用 R456 已付原式，不重新评价任何响应列。

令 $K=\ker J_0$。对 $V\in K$，R433/R457 给
$$
\mathfrak d(V)=D_V,\qquad
\mathfrak d:\ U\longrightarrow\operatorname{Pol}_{\le6},
\qquad \mathfrak d(\mathcal R)=0.
\tag{3}
$$
$\mathfrak d$ 是原 raw 有序局部 $ur$ 系数减 whole-self 主系数迹的自然读出，不能与旧 $\Lambda$ 混同。

在 R456 的最后 low/high 真实角色中，
$$
n_0=\epsilon B^2(4\sqrt2+3/2)\,\mu_{{\rm high},0}\ne0.
\tag{4}
$$
更右完整 cell 的原 $R/T$ 三矩闭合，使该 suffix 没有遗漏其它贡献。取其十二个已有不同中心中的任意八个；不移动或新造包。对每个真中心 $t_j$ 和两个镜点，先由全 partial 取
$$
\mathcal C_{j,\varepsilon}
=R_{ij}H_{e,j,\varepsilon}+T_{ij}H_{d,j,\varepsilon}.
$$
R456(35)给原归一
$$
E_\varepsilon(t_j)=
\frac{\mathcal C_{j,\varepsilon}}
{4\delta_j\gamma_j^7a_i^3r^3}.
\tag{5}
$$
全部分母非零，$\gamma^7$ 不改成别的幅次数。两个 $E_\varepsilon$ 都是次数至多七的完整多项式；八个真实位置的唯一插值因此是确定的实线性操作。

先按 R456(21)读
$$
D_6(V)=\frac{3}{4sn_0}[t^7](E_+-E_-).
\tag{6}
$$
再减去 $D_6$ 乘原完整形式代表 $F_6$ 的两个评价多项式。记余下为 $\widetilde E_\pm$，则
$$
D_5(V)=
-\frac{[t^5](\widetilde E_++\widetilde E_-)}
{2n_0(h/6+2s^2+10bs/3)}.
\tag{7}
$$
$h,s,b>0$ 保第二个分母非零。$F_6$ 只定义读出中的确定减项，不被称为实际可控成本。

所以存在两个已明确的有限真实行组合 $\chi_5,\chi_6$，使
$$
\boxed{\chi_jF(V)=[x^j]\mathfrak d(V)\quad(V\in K),\quad j=5,6.}
\tag{8}
$$
式(5)—(7)使用同一个成本的原两通道；没有独立指定三分量 $n$，没有丢 self 后再另换响应，也不依赖新数值秩。

## 3. 当前全 F 的 vertical response-cover 确实不成立

R333、R406、R457 已给
$$
H_*,J_4,J_6\in U_0\cap K,
$$
$$
\mathfrak d(H_*)=-\frac3{128}x^5,\qquad
\mathfrak d(J_4)=\mathfrak d(J_6)=\frac3{128}x^5.
\tag{9}
$$
这里 $H_*,J_4,J_6$ 是三个完整原成本，不是仅 self 的投影列。

对任一 $R\in\mathcal R\cap K$，由(3)(8)
$\chi_5F(R)=0$。但
$$
\chi_5F(H_*)=-3/128\ne0.
$$
立即得到
$$
\boxed{F(K)\ne F(\mathcal R\cap K).}
\tag{10}
$$
而且这是当前实际同宽全角色库中的真实额外商，不是形式39行中未被物理 suffix 检测的方向。单独选择十九个 self 行的已付实际截面不与(10)矛盾：那不是全部两通道的 $F$。

R459 用的是 $H_*+J_4$（或相应 $J_6$ 组合）先使 $\mathfrak d=0$，再付 current 和 self。一个 $\lambda_+=1$ 的核成员只排除 $\lambda_+$ 经该固定映射下降；它不使(9)的每个独立类都进入响应像。因此 R459 不能被改读成(10)的反面。

更精确地，因(8)在 $\ker J_0$ 成立，
$$
\ker(J_0,F)\subseteq\ker(\mathfrak d_5,\mathfrak d_6).
$$
有限维因子化遂给一个确定的线性映射，使
$(\mathfrak d_5,\mathfrak d_6)$ 经 $(J_0,F)$ 下降；它在 $\mathcal R$ 上零。R457 的完整
$\mathfrak d(U)=\operatorname{Pol}_{\le6}$
又说明这两个读出共同满到 $\mathbb R^2$。这是旧函数像定理的直接推论，不是新求秩。

## 4. 真实平移闭包与准确余商 Q/NQ

记真实成本平移为 $T_c=e^{cN}$。原真权支撑为 $[-9,3]$ 且 $N$ 降权，所以
$$
N^{13}=0.
\tag{11}
$$
把 $F$ 扩为其最小平移行闭包
$$
F_{\rm tr}=(FN^j)_{0\le j\le12},\qquad
J_{\rm tr}=(J_0,F_{\rm tr}).
\tag{12}
$$
这只保共同物理宽度和真平移；全部真实 suffix 随同一个平移输运。也可以用十三个足够小的不同 $c$ 的真实查询替代(12)，由有限多项式插值得到同一个核。

置
$$
P=J_{\rm tr}(U),\quad L=J_{\rm tr}(\mathcal R),\quad
Q=P/L,\quad q:P\to Q.
\tag{13}
$$
$N$ 在 $Q$ 上良定义且幂零。这里没有先假定 $D$ 能在这个仅平移稳定的商上下降。

**平移余商引理。** 对任意 $q_i\in Q$，共同平移的所有主微分都落在 $NQ$：
$$
\partial_c(e^{cN}q_i)=Ne^{cN}q_i\in NQ.
\tag{14}
$$
因此只用这些平移和原响应的放大变化，未触及的准确商是
$$
\boxed{Q/NQ\simeq P/(L+NP).}
\tag{15}
$$
若 $Q\ne0$，幂零性迫 $NQ\ne Q$。否则反复用 $Q=NQ$ 会给
$Q=N^{13}Q=0$。

在当前库中，(15)确有一个具体非零读出。R457(15)—(16)给
$$
\mathfrak d(NV)=\partial_x\mathfrak d(V),\qquad
\mathfrak d_6(NV)=0,\quad
\mathfrak d_5(NV)=6\mathfrak d_6(V).
\tag{16}
$$
由第3节的因子化，$\mathfrak d_6$ 下降到 $Q$，且杀 $NQ$；它在 $U$ 上非零。故它是(15)的非零对偶向量。

这不说当前实际成本的 $D_6$ 必然非零；它说整个目标空间的这个方向不能由平移主微分及响应任意指定。

## 5. 不能把原桥删掉，也不能用未付的桥导数补放大 minor

原 R89 真平移把一个零低阶块 $B_i$ 变成 $B_i^c$，其 scalar 端口通常改变。必须接原 $M=0$ 桥 $A_i(c)$ 及同一桥真倒行：
$$
W_i(c,n)=A_i(c)(B_i^c)^nA_i(c)^R .
$$
完整身份是
$$
M_{W_i}=\mathbf T_{W_i}=0,\qquad
V_{W_i}=2V_{A_i(c)}+nT_cV_{B_i}.
\tag{17}
$$
第四倒行同号。$2V_A$ 是实际 $AA^R$ 的成本，不是可删除的“连接误差”。

即使另已证明增强闭锥满，并选到
$\alpha_i>0,\ \sum_i\alpha_iq_i=0$、$q_i=qJ_{\rm tr}(V_{B_i})$，
取 $n_i=\lfloor M\alpha_i\rfloor$ 后，原商方程仍为
$$
Q_M(c)=\sum_i n_ie^{c_iN}q_i+E_Q(c),\qquad
E_Q(c)=2\sum_iqJ_{\rm tr}(V_{A_i(c_i)}).
\tag{18}
$$
固定全部小桥族后 $E_Q$ 及其导数为 $O(1)$，并不是零。除以 $M$，
$$
M^{-1}D Q_M(0)\longrightarrow
(\alpha_1Nq_1,\ldots,\alpha_mNq_m),
\tag{19}
$$
秩至多 $\dim NQ$。在(15)中更有精确公式
$$
[Q_M(c)]=\sum_i n_i[q_i]+[E_Q(c)].
\tag{20}
$$
bulk 的平移参数在这里完全不作用；只剩未被放大的真桥函数。

所以 R206(10)—(11)、R428(19)、R433(24)所用的统一近恒等 minor 不能由(19)代替。不能从“桥是光滑的”推出其在(15)中满射或其可支付域覆盖全部目标。如果另能证明这些桥或另一些真实族在(15)上有足够可放大的正则导数，那是一个新的明确接口；本稿不排除它。

准确失败的是**原证明的平移替换步骤**，不是任意固定宽度实际构造的不可能性。

## 6. 两次商校正为什么都不能省

R101 的完整复制恒等式在任意固定线性观测 $J$ 下都是
$$
J(V_{Z(t,n)})=
E_J(t)+n\left(2\sum_\ell J(v_\ell)
+\sum_\ell t_\ell J(K_\ell)\right).
\tag{21}
$$
它本身不要求 $J$ 仿射稳定。$v_\ell$ 是真实第三 prototype 的整个第四成本；它一般不在响应中，且不因选了 $K_\ell$ 的核而为零。

R333/R428/R433 先用**同一个完整商**截面使每个 prototype 的商成本为零。否则(21)中的
$2n\sum qJ(v_\ell)$ 会随最后 $n$ 增长，不能藏入固定的 $O(1)$ 基准。然后对 $qE_J(t)$ 再用第二个实际商截面；其全部响应坐标仍进入最后
$$
n(a+t)+G(t,y).
\tag{22}
$$
先冻结 $G$ 及其紧盒，最后才选有限 $n$ 收缩。两个校正的成本都要通过新增 $F$ 原式查询，不能只保旧 $J_0$ 值。

真实 Klein 闭合只把最终成本写成 $V_{\rm base}+4V_B$。它通过目标
$-J(V_{\rm base})/4$ 消基准，不生成(15)所缺的连续控制方向，也不把 mixed signed $W$ 变成负时间路径。

## 7. 只保平移时正锥证明还能得到什么

令 $C_J=\overline{\operatorname{cone}(J_{\rm tr}\mathcal S)}$。
若它不是整个 $P$，有限维分离给非零正泛函。
$C_J$ 对真平移不变、其对偶尖；沿 R127 §4 对最后一个非零 $N^*$ 导数作两向极限，仍能得到
$$
0\ne\lambda,\qquad
\lambda(\mathcal S)\ge0,\qquad
\lambda\mathcal R=0,\quad \lambda N=0,\quad
\lambda\ker J_{\rm tr}=0.
\tag{23}
$$
此步骤不需要正伸缩，但所得 $\lambda$ 可以混权。

R127 §3 的下一步使用
$H^{-m}\lambda P_{H,0}\to\lambda_m$。
要保证 $\lambda_m$ 仍杀新增核，需要该核对正伸缩、从而对真权投影稳定。仅有(12)不能保证这一点。即使在整个 $U$ 上提取出一个正单权泛函，它也可能已经不经 $J_{\rm tr}$ 下降，便不能使用该联合映射的核见证来排除它。

所以 R433 原来对六种单权字符的排除不能直接照搬到这个未证伸缩稳定的新核。R459 排除 $\lambda_+$ 经固定 $J_{\rm tr}$ 下降，与排除(23)的全部混权泛函，是不同结论。

## 8. 最小仿射行闭包与十三个近一 H 的有限合同

以下给出一个明确有限的替代，不要求在实际几何上同时放入无限宽度。

设 $\mathscr F_{\rm tr}\subset U^*$ 是(12)的行空间。其最小真仿射稳定扩张是
$$
\boxed{
\mathscr F_{\rm aff}
=\operatorname{span}\{FN^j\Pi_\sigma:
-9\le\sigma\le3,\ 0\le j\le\sigma+9\}.
}
\tag{24}
$$
这里 $F$ 逐行理解；不存在的权和零行直接不贡献。
右侧至多有 $1+\cdots+13=91$ 个形式位置每原行，**不是**真实秩或独立新目标数。它包含原行，且在右复合 $D$、$N$ 下封闭；任何仿射稳定行空间若含原行，必含全部有限真权投影和这些平移导数。因此“最小”指这个确定的行空间，不指91个标签全部必需。

等价的有限查询实现如下。取十三个不同
$H_\nu\in(1-\varepsilon,1+\varepsilon)$，$\varepsilon>0$ 足够小，再取十三个不同的小平移 $c_\mu$。
采用成本顺序 $T_cD_H$，由 R89 它仍是真正正仿射变换（相应原参数为 $(H,Hc)$）。对任意 $V=\sum V_\sigma$，
$$
F(T_cD_HV)
=\sum_{\sigma=-9}^{3}\sum_{j=0}^{\sigma+9}
H^\sigma\frac{c^j}{j!}\,FN^jV_\sigma.
\tag{25}
$$
$c$ 次数至多十二；乘 $H^9$ 后对 $H$ 次数至多十二。两次普通 Vandermonde 插值表明，$13\times13$ 个真实查询与(24)具有同一个核。若已采用完整平移行空间，只需再加十三个 $H_\nu$。可以在已知较小权支撑时删冗余，但本稿不为删行另求秩。

从起点把这些有限查询、其原锚和全部 prototype/桥小族放入共同窗口即可。每一固定 $H_\nu$ 下的库仍是共同宽度 $H_\nu w_0$。这些是辅助查询输运，不改变最后目标圆中已冻结的实际宽度。有限 Laurent 身份一旦成立，给代数上的全部正 $H$ 核稳定；不要求最终窗口物理容纳 $H\to0$ 或 $H\to\infty$ 的全部 profiles。

原反号 $\mathsf S=\sum_\sigma(-1)^\sigma\Pi_\sigma$ 也因此保持该核。它沿 R145 是同右锚的真实曲率反号，而不是擅自把 profile 镜像并换积分锚。

## 9. R459 的混权 W 对该有限合同究竟还缺什么

R459 已构造
$$
V_0=\widehat H_4-R_C\in U_0\cap\ker J_0\cap\ker\mathscr C,
\qquad \lambda_+(V_0)=1,
$$
并有同一个可能混权的响应 $W=\sum_\sigma W_\sigma$，使
$$
F_{\rm tr}(V_0)=F_{\rm tr}(W).
\tag{26}
$$
其同宽全中心匹配范围按 R459 保留。

对这些同一查询，完整正伸缩匹配要求
$$
F_{\rm tr}(V_0)=
\sum_\sigma H^\sigma F_{\rm tr}(W_\sigma).
\tag{27}
$$
十三个近一 $H$ 的准确匹配等价于
$$
\boxed{
F_{\rm tr}(W_0)=F_{\rm tr}(V_0),\qquad
F_{\rm tr}(W_\sigma)=0\quad(\sigma\ne0).
}
\tag{28}
$$
而(26)只给各权值的和。把原 $W$ 直接投到权零，必须先付(28)，不能由(26)自动推出。

R462 已将一种保持整个形式 current 的权零 self 补偿问题缩到
$$
\dim(\mathcal R_0\cap\ker E\cap\ker\mathscr C)=5.
$$
原49模块中只有 $K_8,V_{51},V_{52}$ 三条权零完整成本；其镜对像真为三维，另外两维完整成本的 self 像尚未付。这里的“五”是成本维数，不能冒成镜对秩。R462 给的是(28)的一个具体小入口，不是 actual 截面结论。

## 10. 补仿射闭包后，旧 D 单独可逆仍确实失效

置
$$
J_{\rm aff}=(J_0,F_{\rm aff}),\quad
P_{\rm aff}=J_{\rm aff}(U),\quad
L_{\rm aff}=J_{\rm aff}(\mathcal R),\quad
Q_{\rm aff}=P_{\rm aff}/L_{\rm aff}.
\tag{29}
$$
现在才有完整真权分解。第3节的 $H_*$ 证明
$$
[J_{\rm aff}(H_*)]\ne0\quad\text{于 }(Q_{\rm aff})_0.
\tag{30}
$$
因为若它等于某个响应像，取 $J_0$ 分量会迫该响应保持 $J_0$，再用(8)(9)矛盾。也可直接用经该联合映射下降、且杀全响应的 $\mathfrak d_5$ 读出。

所以 $D$ 在(29)上不是可逆算子。这与 $\lambda_+$ 是否经(29)下降无关：非零零权响应商不必给正泛函。

完整零权等像要求的是三个原头类全部支付：
$$
U_0=\mathcal R_0+
\operatorname{span}\{H_*,J_4,J_6\}.
\tag{31}
$$
只有一条 $\lambda_+=1$ 的核见证，不能替代(31)中全部类的联合成员门。当前(9)已经表明整个零权像等号不成立。因此不能在补完(24)后仍引用“整个零权商为零”来启动原 R206。

## 11. 真正可用的双参数替代引理：DQ+NQ=Q

下述加强完整保留 R206 的真实成本证明，并容许零权商非零。

**双参数商引理。** 设 $J$ 是同一真仿射稳定有限映射，$P=J(U)$、
$L=J(\mathcal R)$、$Q=P/L$。假设：

- 已证明同一增强映射的满闭锥
  $\overline{\operatorname{cone}(J\mathcal S)}=P$；
- 同一个实际共同窗口包含所用有限 profiles、近恒等仿射块、真实桥、原型及其紧参数包络；
- 在这个完整 $Q$ 上，
  $DQ+NQ=Q$。

则 R206/R212/R433 的两个商校正与最终响应收缩仍给 $J$ 的实际有限 $C^1$ 截面。

**证明。** 满闭锥给有限实际 $B_i$，使 $q_i=qJ(V_{B_i})$ 正张成 $Q$，并有严格正配平
$\sum_i\alpha_iq_i=0$。令每个块同时带两个小真实参数，成本主项取
$T_{c_i}D_{e^{t_i}}q_i$，用原 $M=0$ 桥及真倒行返回固定端口。桥全成本保留为 $E_Q(t,c)$。取固定整数
$n_i=\lfloor M\alpha_i\rfloor$，则
$$
M^{-1}\left\{
\sum_i n_iT_{c_i}D_{e^{t_i}}q_i+E_Q(t,c)
\right\}
\longrightarrow
\sum_i\alpha_iT_{c_i}D_{e^{t_i}}q_i
\tag{32}
$$
在固定小盒上为真 $C^1$ 收敛。右边在零参数为零；其导数列是
$$
\{\alpha_iDq_i,\ \alpha_iNq_i\}_i.
\tag{33}
$$
$q_i$ 张满 $Q$，故(33)的像恰为 $DQ+NQ=Q$。选一个可逆 minor、冻结其它参数，R206 的统一近恒等收缩给一个固定有限 $M$ 上的紧目标商截面。没有实数次复制，所有桥成本均留在(32)。

之后先清每个第三 prototype 的这个**完整商**基准，再对 $qE_0(t)$ 作第二次商校正。两批整数先冻结；全部响应代价进入固定的 $G(t,y)$。最后用(22)的有限 $n$ 收缩，得到同一个实际 $C^1$ 截面。证毕。

因 $D$ 在非零权上可逆，这个条件准确等价于
$$
\boxed{Q_0\subseteq NQ_1.}
\tag{34}
$$
它严格弱于 $Q_0=0$。不过必须是同一个完整增强 $Q$，不能只检查其自然投影。

在已付 $\mathfrak d$ 多项式像上，生成元为
$$
D(x^j)=(j-5)x^j,\qquad N(x^j)=jx^{j-1}.
\tag{35}
$$
因此其中的零权 $x^5$ 有 $x^6/6$ 这个平移前像；这个自然像满足 $DQ+NQ=Q$。它说明(30)本身不是 actual 不可能性的证据。

但是，取到某个 $Z\in U_1$ 使 $\mathfrak d(NZ)=\mathfrak d(H_*)$，并没有证明
$J(H_*-NZ)$ 是响应：全部 $E,\mathcal A,\mathcal O$、所有 self partial 和真实角色尾仍须由**同一个**原响应或同一个 $J$ 核付清。这个完整 lift 缺口不能以(35)替代。

## 12. 固定宽度的 vertical 引理，及它在当前 F 上的准确禁用范围

另一个无需给新 $F$ 增加仿射闭包的充分接口如下。

**有限 vertical 增强引理。** 已有 $J_0$ 的实际有限 $C^1$ 截面。若一个固定真实有限映射 $G$ 满足
$$
G(\ker J_0)=G(\mathcal R\cap\ker J_0),
\tag{36}
$$
则 $(J_0,G)$ 也有同一共同窗口内的实际有限 $C^1$ 截面。

取 $J_0$ 的线性截面 $s$，定义
$\widetilde G=G-GsJ_0$。它的像恰为 $G(\ker J_0)$。
选有限原响应 $K_j\in\mathcal R\cap\ker J_0$，使
$\widetilde G(K_j)$ 为该像的一组基。若某个 $K_j$ 是多条原 primitive 响应的组合，先按其真实有限表达分开 prototypes，再把二阶参数按同一个系数绑定；不假定每条 primitive 都单独杀 $J_0$。

先用既有 $J_0$ 截面清每个 prototype 的全部 $J_0$ 基准，保其 $G$ 成本。R101 复制后 $J_0$ 分量仅为与最后 $n$ 无关的 $E_0(t)$；再用既有截面清目标与 $E_0(t)$ 的差。两个校正块的完整 $\widetilde G$ 值进入固定 $C^1$ 函数 $G_{\rm err}(t,y)$。最后方程为
$n(a+Mt)+G_{\rm err}(t,y)=y_{\rm vert}$，
其中 $M$ 可逆，故有限 $n$ 收缩证明结论。

这条引理不要求新增查询核伸缩稳定；最终 profiles 可以保持固定宽度。但它继承旧 $J_0$ 截面内部已经使用的正伸缩，因此不是一个全部控制词都禁用 $H$ 的构造。

**当前完整 $F$ 明确不满足(36)，由(10)已经否定。** 此引理可用于先处理实际额外商之后的真正剩余 vertical 坐标，或用于 R448 那类已经证明响应覆盖的有限 self 行；不能再拿来宣整个全角色 partial 已可实际增强。

## 13. 下一有限查询合同与具体未付门

无需重做 R443、旧响应秩、十九根或四个母约束。下一接口可准确写成以下有限问题。

首先保原最终库、全部原幅/角色/suffix和固定右锚。以(2)定义全角色 $F$，以(24)定义其最小仿射行闭包；实际可用十三个近一 $H$ 配原完整平移闭包承载，完整值只用于原式证明或以后单独授权的新观察。不得用各宽独立挑选的响应代替同一个成本。

在
$$
K_{\rm aff}=\ker J_{\rm aff}
$$
下，双参数引理的唯一线性零权条件是
$$
\boxed{
U_0\subseteq \mathcal R_0+(K_{\rm aff}\cap U_0)+NU_1.
}
\tag{37}
$$
等价地，对(31)的三个原头，每个都须有**完整原成本** $Z\in U_1$、
$R\in\mathcal R_0$，使
$$
J_{\rm aff}(H_*-NZ-R)=0,
\quad\text{或分别将 }H_*\text{ 换成 }J_4,J_6.
\tag{38}
$$
三个方程可以共享或不共享 $Z,R$；但每一个方程中的所有坐标必须由同一个组合支付。式(38)不要求单独实现这些 signed 成本为路径，只为建立正确的实际商导数条件。

另外仍须在同一个 $J_{\rm aff}$ 上证明满闭锥。有限闭包只使 R127/R145 的单权步骤合法，不自动消掉新增正字符。尤其 R433 的负权步骤原来只匹配 $E,\mathcal A,\mathcal O$；任何用到
$J(V-NZ-R)=0$ 的地方，都必须把(24)的新行一起核入，不能以旧三部分身份代替。原 whole-$U$ 的 $-2$ 排除及 $U_2=\mathcal R_2$ 可按其真实范围保留；其它新增核条件不预授。

最后按第11节一次固定整个新商、有限正配平、完整 prototypes、两次商基准和 Klein 背景，再取实际有限根。不得先各做一个 $D_5$、self 或 $J_0$ 截面后直接相加。

本稿已经给出了真实读出的反例(9)—(10)、平移余商(15)、有限闭包(24)和双参数 actual 引理。当前最有价值的后续是(37)的完整 lift 与同一增强锥，尤其 R462 五维权零 current 核中剩余两条完整 self 方向；不是继续增加已知同宽 signed 行数。全 period、两条特解、平台连接及同一个十三行规范仍保持原未付范围。
