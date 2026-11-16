# R428：共同合法窗口内完整 J 的条件性真实有限 C1 截面

日期：2026-11-16。**条件定理及原式接口证明；不执行新的 profile、求积、符号程序、原根、秩或科学计算。**

本稿把 R414 的高自然商控制升级为整个共同映射
$$
J=(E,\mathcal A),\qquad E=(\pi,\mathcal Q),
$$
所需的最后前提精确隔离出来：在同一个从起点构造、随后冻结的实际母库上，R427 的两个剩余完整 $kk$ 权负四自然系数须落在已经支付的真实平移像中。**本稿不宣称这两个新原函数已经求出或满足该前提。**

在这个前提下，以下三个结论完整成立：

1. $J$ 的实际闭成本锥是整个真实联合像 $J(U)$；
2. 每个紧相容目标集都由同一个固定有限真实词族给出 $C^1$ 截面，全部原型、桥与后校正基准保留；
3. 对零目标，原 R394 所使用的有限 total 条件可以实际同时支付，不需要不可能实际实现的 universal $\Lambda_{\rm all}=0$。内部 $A_f$ 部分通量与同一十三行规范仍不由此消失。

物理实施沿 R414 的明确共同合法窗口前提。不同初选母库、不相容的目标空间或分开取得的控制截面不在证明中拼接。

直接来源：[R414](R414-common-high-natural-quotient-and-actual-finite-C1-sections.md)、[R413](R413-common-mother-Q4-chain-and-exact-low-layer-character-reduction.md)、[R206](R206-full-pure-cone-equivalent-to-actual-finite-pure-controllability.md)、[R212](R212-C1-sections-for-complete-real-pure-cost-control.md)、[R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)、[R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md)、[R389](R389-ordered-total-fluxes-and-complete-flat-end-germs-for-the-rational-port.md)、[R394](R394-conditional-complete-period-and-finite-same-gauge-interface.md)、[R407](R407-connected-moment-fibers-fix-self-caps-and-retain-the-actual-total-fluxes.md)、[R412](R412-complete-weight-zero-natural-null-mothers-and-nineteen-common-targets.md)、[R421](R421-all-curvature-kk-minus6-natural-identity-and-common-character-cancellation.md)、[R425](R425-complete-hh-minus4-natural-identity-and-PSD-cross-cancellation.md)、[R426](R426-complete-zero-curvature-kk-minus4-natural-anchor-and-common-query-reduction.md)、[R427](R427-even-quartic-curvature-support-of-the-complete-kk-minus4-natural-function.md)。逐权证明另使用原 R130、R145、R188、R190、R356、R406、R416、R419、R420 与 R424。本文引用的 R427 结论只涉及完整自然函数；不将其冒作原成本的三项恒等式。

## 1. 一次冻结的实际库、最小查询和两种初选分支

固定原共同右锚与同一有限真实库
$$
u_i(x)=\rho_i U_i((x-\xi_i)/w_i),\qquad w_i>0.
\tag{1}
$$
全部实际宽度、幅度、中心、八/十二副本及最终块均包含在(1)中。每个中心偶母来自同一次 R412 有限十九量构造，并满足
$$
n_2(C_{H,c}U_i)=0,\qquad C_{H,c}u(x)=u((x-c)/H).
\tag{2}
$$
从起点保留共同 $D,E_5$，且 $D_0-E_0>0$。以下写 $p=u',r=u''$，并使用 R413/R424 的原规范
$$
D=-\frac12\int p^2r^3+\frac12\int xpr^4-\frac3{20}\int x^2r^5,\qquad
E_5=-\frac12\int xpr^4+\frac7{20}\int x^2r^5,
\qquad M_{25}=\int x^2r^5.
$$
若使用下文第二种分支，须在这同一次初选中再将 $M_{25}$ 放入 $F^\star$；这些共同值取自新初选的母包，不是任意外指定的数。不能在一个旧冻结库上免费添值。

自然函数保持原 self/pure/ordered 规范
$$
\Lambda_u(V)=\int u'''V(u^2,0)-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\tag{3}
$$
它在整个 $U$ 上定义，并杀原响应空间 $\mathcal R$。

对每个 $u_i$，取三个完全位于其右侧的实紧辅助包 $v_{i\alpha}$，其真实三矩为基。只加入
$$
\omega_i(V)=\Lambda_{u_i}(V),\qquad
O_{i\alpha}(V)=[s^3t^2]\Lambda_{su_i+tv_{i\alpha}}(V),
\tag{4}
$$
及所有这些行的共同正仿射输运。记所得有限维映射为 $\mathcal A$。辅助包的 self 读出不额外加入。需要时(4)可由有限次真实 profile 评价提取；这不等于将那些额外评价全部作为独立目标。

若 $n=\sum_\alpha b_{i\alpha}(n)\mu(v_{i\alpha})$，定义
$$
A_i(V;n)=\sum_\alpha b_{i\alpha}(n)O_{i\alpha}(V).
\tag{5}
$$
它是原有序三矩映射；其系数和实际 suffix 均不可任意重选。

### 1.1 唯一未付输入，写成共同商中的准确条件

R427 给完整自然函数身份
$$
\mathcal N([h^{-4}]\widehat Q_{kk}(h,k,0))
=\mathcal N(V_0)+k^2\mathcal N(V_2)+k^4\mathcal N(V_4).
\tag{6}
$$
每个 $V_j$ 是原真实有限系数；(6)不宣称三个成本本身张满该曲率族。对这些列可以取真实权 $-4$ 投影，因原自然读出与有限真权分解协变。

本稿的新增前提是
$$
\boxed{
\mathcal A(V_2),\ \mathcal A(V_4)
\in N\mathcal A(U_{-3}),
}
\tag{H}
$$
其中 $N$ 是原真实平移生成元。这是同一个共同查询商的条件，不是分别在各母上成立的数值比例。

可用的两个实施分支必须在最初选定其一：

- **原共同 $D/E_5$ 分支：**若两个完整新函数直接在该库的共同 Q4 平移像中，则(H)原样适用，不改变已选母库。
- **R424 从起点增强分支：**若两个新函数已被完整原式证明为权 $-4$ 的局部、二阶 jet、五次多项式泛函，则在同一 R412 起点采用 $F^\star=(F_{\rm rat},D,E_5,M_{25})$；R424 给(H)。这里要求真正的 locality，而不是仅 $C^2$ 连续或 principal 相消。

第二种分支的精确原因是：该类密度模分部积分可用
$$
p^3r^2,\quad upr^3,\quad xp^2r^3,\quad xur^4,\quad x^2pr^4,\quad x^3r^5
\tag{7}
$$
表示。偶母及 $M_5=0$ 使全部平移值仅线性依赖中心；$q_1=0$ 与共同 $D,E_5,M_{25}$ 准确固定
$$
\int xpr^4=\frac7{10}M_{25}-2E_5,\quad
\int p^2r^3=\frac25M_{25}-2D-2E_5,\quad
\int ur^4=\frac12M_{25}+8D-7E_5 .
\tag{8}
$$
这些查询因而与 Q4 的 $NH$ 行共线。真实副本的因子
$\rho_i^5(Hw_i)^{-7}(H\xi_i+c)$ 保留。这是 profile 输运值；转换成成本作用时还乘(10)的共同 $H^2$。所有不交 ordered $3+2$ 因完整局部性为零，辅助包无须具有共同的(8)。

本文不证明(6)的两个新函数满足第二分支条件，也不将第一分支与另一个新母库的第二分支拼接。

## 2. 原仿射核、零权和满锥所需的全部范围

令
$$
\mathscr P=J(U),\qquad \mathscr L=J(\mathcal R),\qquad
J=(E,\mathcal A).
\tag{9}
$$
目标空间是实际联合像 $\mathscr P$，不是未经证明的直积。

自然协变为
$$
\Lambda_u(\mathsf P_{H,c}V)=H^2\Lambda_{C_{H,c}u}(V).
\tag{10}
$$
有限 profile 五次系数提取与该式交换。共同仿射开邻域上的零关系由原有限 Laurent/平移多项式延拓为表示身份，所以 $\ker J$ 在正仿射作用、$N$ 和全部有限真权投影下稳定。

原成本权支撑为 $[-9,3]$。R145 的同右锚代数反号按真权作用为 $(-1)^\sigma$，并由真实曲率反号保实际闭锥；它不是把 profile 镜像换成左锚。故非零正仿射字符只可能有偶权
$$
-8,-6,-4,-2,0,2.
\tag{11}
$$

R406 给 $\mathcal N(V^{(0)})=\lambda_+(V^{(0)})n_2$。
(2)杀所有实际母的 self 行；$n_2$ 的完整局部五次性杀所有不交(4)行，无需辅助 self 零。因此
$$
\mathcal A(U_0)=0,\qquad \mathcal A(\mathcal R)=0.
\tag{12}
$$
R333 的整个权零等像给
$$
J(U_0)=J(\mathcal R_0),\qquad
(\mathscr P/\mathscr L)_0=0.
\tag{13}
$$
这是稍后实际缩放 IFT 所需的整个零权条件。

(12)仅是选定共同查询的零权零式。原实际成本的 $\lambda_+>0$ 与 universal 自然不全零仍保持，不能把本有限 $\mathcal A$ 偷换成 $\Lambda_{\rm all}$。

## 3. 条件(H)怎样排除最后正字符

令 $\mathcal S$ 为原同 scalar/frame 端口、$M=\mathbf T=0$ 的有限真实成本集合，$U=\operatorname{span}\mathcal S$。考虑
$$
C_J=\overline{\operatorname{cone}(J\mathcal S)}\subset\mathscr P.
$$
若此闭锥不是整个 $\mathscr P$，原 R127 单权提取给非零正仿射字符，其拉回 $\lambda$ 杀 $\mathcal R$、经同一个 $J$ 下降，并在全部实际成本上非负。

对(11)逐项处理：

| 真权 | 完整排除依据 |
|---|---|
| $-8$ | R356 给整个该权自然函数零，R323 给 $E(U_{-8})=E(\mathcal R_{-8})$。 |
| $0$ | (12)与 R333 给整个联合像等号(13)。 |
| $2$ | R190 给原完整 $U_2=\mathcal R_2$。 |
| $-2$ | R188 已排除整个真实 $U$ 上该权的非零正仿射字符。 |
| $-6,-4$ | 由下列同一个实际 action 与原乘子逐态排除。 |

对后两权，R323 同权 $E$ 响应等像的作用须说清。若
$\mathcal A(V)=\mathcal A(NZ)$，$V\in U_\sigma$、$Z\in U_{\sigma+1}$，
则取真实 $R_V\in\mathcal R_\sigma$ 满足
$E(R_V)=E(V-NZ)$。这样
$$
J(V-NZ-R_V)=0,\qquad
\lambda(V)=\lambda(NZ)+\lambda(R_V)=0.
$$
第一项用 $\lambda N=0$，第二项用 $\lambda\mathcal R=0$。这不把仅 $\mathcal A$ 相等冒作完整 $J$ 相等，也不把响应补偿本身当成一条任意 signed 实际路径。更一般地，若 $\mathcal A(V)=0$，同权补响应后 $\lambda(V)=0$。

R350/R382 的完整 Abar/H 自然零、以及 R413 的共同 Q4 四链先使这两权的整个最高几何导数层在 $\lambda$ 下为零。R140/R413 随后给同一个八矩乘子 $\mu$，使完整 action 等价于
$$
A_\lambda(S)=\lambda F_0(S)-\mu m_0(S)\ge0,\qquad
B_\lambda(S)=\lambda\widehat Q_2(S)-\mu m_2(S)\succeq0.
\tag{14}
$$
原 $N_0,N_2,\Gamma$、水平正规化与真边势都包含在这里。

### 3.1 权负六

R416 已给全部曲率静态 $a=\mu=0$。R419 的全部曲率 $hh$ 完整自然零，使 PSD 的 $hh$ 行为零，从而交叉行为零。R421 的真实 $kk$ 身份为
$$
\mathcal N([h^{-6}]\widehat Q_{kk}(h,k,0))
=\frac{(1+k^2)^2}{640}\int(5p r^4-3xr^5).
$$
偶母及 $M_5=0$ 杀其全部实际 affine self；完整局部性杀 ordered 行。故 $kk$ 也在 $\lambda$ 下为零。原状态协变保所有真实 $h,\omega$，没有只用一个锚替代全曲率。

于是本权的全部十四个正规族及响应均被 $\lambda$ 杀掉；R130 的完整生成定理迫 $\lambda=0$。

### 3.2 权负四

R420 已使静态 action 与同一个乘子均为零。它不声称全 static 自然函数为零；完整 static 自然像落在已付共同 Q4 平移像中。

R425 给全曲率
$$
\mathcal N([h^{-6}]\widehat Q_{hh}(h,k,0))
=-\frac3{16}(1+k^2)^2F_{Q4}.
$$
R413 的共同四链使其 $\lambda$ 值为零；PSD 再迫交叉项为零。

R426 的完整锚
$$
\mathcal N(V_0)=\frac3{128}F_{Q4}
+\frac1{64}\int(3p^3r^2-2upr^3)
$$
在同一共同映射中准确等于 $3F_{Q4}/128$，故 $\lambda(V_0)=0$。
对(6)余下两行，(H)与 $\lambda N=0$、同权 $E$ 补偿给
$\lambda(V_2)=\lambda(V_4)=0$。所以整个 $kk$ 曲率函数为零。

因此(14)完整剩余层也为零；再次由原十四族生成定理得 $\lambda=0$。

六种权全被排除，故条件(H)下
$$
\boxed{C_J=\mathscr P.}
\tag{15}
$$
这一步在同一个 $J$ 上完成；没有把旧高商的满锥与另一个母库的低商结论拼接。

## 4. 主定理：同一有限真实词的完整 J 截面

**物理实施前提。** 原共同母库、辅助矩基、固定右锚，与下面选取的有限真实原型及其紧参数包络须同处一个从起点冻结的合法窗口。可按 R414 先作一次共同正仿射坐标识别，目标随同一个可逆输运改变、零目标保持零。不得在目标求解后迁移 profiles，亦不承诺任意旧冻结窄窗口容纳所有控制。

**定理。** 在这一实施前提及(H)下，对每个紧集
$\mathcal K\subset\mathscr P$，存在其有界开邻域 $\mathcal O$ 和一个固定有限真实词族 $\mathscr D(y)$，使
$$
\boxed{
M_{\mathscr D(y)}=\mathbf T_{\mathscr D(y)}=0,\quad
F_{\mathscr D(y)}:I\to I,\quad
J(V_{\mathscr D(y)})=y\qquad(y\in\mathcal O).
}
\tag{16}
$$
所有整数、构件类型和词排列固定，仅有限几何参数按 $y$ 作 $C^1$ 变化。原 scalar/frame 端口、右锚和整个 profile 库在目标邻域内固定。

### 4.1 同一个响应商的严格正核和真实桥

令 $q:\mathscr P\to\mathscr Q=\mathscr P/\mathscr L$。
由(13)，真实缩放生成元 $D$ 在 $\mathscr Q$ 上可逆。由(15)，R206 的有限选择给实际 $M=\mathbf T=0$ 块 $B_i$，其
$$
q_i=qJ(V_{B_i})
$$
正张成 $\mathscr Q$，并有严格正实数
$$
\alpha_i>0,\qquad\sum_i\alpha_iq_i=0.
\tag{17}
$$
这些实数只用来选整数，不是带实数次重复的路径。

真实缩放 $B_i^{e^{t_i}}$ 改 scalar 端口；用原 $M=0$ 桥
$A_i(t_i)$ 接入并用**同一桥的真倒行**返回。对整数 $n_i$，
$$
W_i=A_i(t_i)(B_i^{e^{t_i}})^{n_i}A_i(t_i)^R
$$
满足
$$
M_{W_i}=\mathbf T_{W_i}=0,\qquad
V_{W_i}=2V_{A_i(t_i)}+n_i\mathsf P_{e^{t_i},0}V_{B_i}.
\tag{18}
$$
桥的第三可非零，倒行第三反号；第四则同号，所以 $2V_A$ 不删。
它本身是真实 $AA^R$ 的成本，在原 $U$ 中。

令 $n_i=\lfloor N\alpha_i\rfloor$。拼接后商方程为
$$
\mathcal Q_N(t)=\sum_i n_i e^{t_iD}q_i+E_Q(t),
\quad E_Q(t)=2\sum_iqJ(V_{A_i(t_i)}).
\tag{19}
$$
除以 $N$ 后，在固定小盒中真 $C^1$ 收敛到
$\sum_i\alpha_i e^{t_iD}q_i$。
(17)给零点，$D$ 可逆及 $q_i$ 张满给一个可逆参数 minor。
R206 的统一收缩因此在一个**固定有限** $N$ 上支付任意紧商目标集，并给 $C^1$ 截面 $C(y_Q)$。所有桥基准均留在(19)。

### 4.2 先清每个第三原型的完整商基准

取有限真实响应 $K_\ell$，使
$\kappa_\ell=J(K_\ell)$ 是 $\mathscr L$ 的基。
其原第三 prototype $L_\ell$ 有 $M=0$、$\mathbf T=\tau_\ell$。
完整成本 $v_\ell$ 在 $U$ 中，因为真字 $L_\ell L_\ell^R$ 有成本 $2v_\ell$、$M=\mathbf T=0$；这不是执行半条路径。

先用(19)的同一商截面付目标 $-qJ(v_\ell)$，接上实际 $M=\mathbf T=0$ 块，得到
$$
\widehat L_\ell,\qquad
\mathbf T_{\widehat L_\ell}=\tau_\ell,\qquad
qJ(\widehat v_\ell)=0.
\tag{20}
$$
它们的全部响应坐标可能很大，但保留在 $\widehat v_\ell$；不只清自然坐标而漏掉商中的 $E$。

### 4.3 真实复制、第二商校正与最后有限根

R101/R212 的共享原型/真倒行字给
$$
J(V_{Z(t,n)})=
E_0(t)+n\left(2\sum_\ell J(\widehat v_\ell)
+\sum_\ell t_\ell\kappa_\ell\right),
\quad M_Z=\mathbf T_Z=0.
\tag{21}
$$
$E_0(t)$ 是完整固定 $C^1$ 基准，最后整数 $n$ 尚未选。
由(20)，$qJ(V_Z)=qE_0(t)$ 与 $n$ 无关。

固定 $\mathscr P=\mathscr L\oplus\mathscr J_Q$，
令 $\ell$ 取响应基坐标，
$a=2\sum_\ell\ell J(\widehat v_\ell)$，
$t^0=-a$。先固定覆盖 $t^0+[-2,2]^r$ 的原二阶小族重复数，得到固定的 $E_0$。
对 $y\in\overline{\mathcal O}$、$t\in t^0+[-1,1]^r$，
商目标集合
$$
Y_Q=\{qy-qE_0(t)\}
$$
紧；此时才选其统一商截面 $C(qy-qE_0(t))$，然后冻结这第二批整数。

两个 $M=\mathbf T=0$ 块的完整第四成本严格相加。最后
$$
qJ(V_{\widetilde Z})=qy,\qquad
\ell J(V_{\widetilde Z})=n(a+t)+F(t,y),
$$
$$
F(t,y)=\ell E_0(t)+\ell J(V_{C(qy-qE_0(t))}).
\tag{22}
$$
第二项的所有响应成本保留，不用其商目标替代。
$F,D_tF$ 在固定紧盒上有界，而且与最后 $n$ 无关。
取一个有限整数使
$$
t\longmapsto-a+n^{-1}\{\ell y-F(t,y)\}
\tag{23}
$$
将该盒映入内部且收缩常数小于 $1/2$。
唯一根及 $nI+D_tF$ 的可逆性给同一个 $C^1$ 目标截面，证明(16)。
若商维或响应维为零，省去相应步骤；不以空路径冒充实际几何。

原成本的 $C^1$ 性来自固定词上的 R56 全恢复、真实积分和固定锚。
$E$ 与(4)在有限联合像上可取有限忠实真实查询为坐标；
有限幅度系数提取也是固定线性操作。故这里不把抽象有限维本身当作几何正则性证明。

## 5. 不循环的选择顺序与原基准

证明中只有一个共同库、一个 $J$ 和一个目标空间。
先固定有限满锥见证、近一缩放桥族、响应基、第三 prototypes、二阶小族及需要的固定背景；它们的紧 scalar 包络连同 profile 库满足第4节实施前提。
随后依次：

1. 以一个有限商整数清各 prototype 的完整商基准；
2. 根据真实新基准确定响应中心 $t^0$，用小族有限重复覆盖其盒；
3. 对紧目标集选第二个统一商截面，冻结(22)；
4. 最后选(23)的响应重复数。

重复只增加有限长度和真实位移，不扩大已选 scalar 包络。
整个目标邻域内不改变母、右锚、实际宽度或 profile 坐标。
因此该定理不由“每个母分别 actual”或“先 high、再另做 low”推得。

若将固定闭 hook 背景与 Klein 闭合从起点纳入同一包络，其完整成本为
$$
V_{\rm base}+4V_{\mathscr D}.
$$
背景归属 $U$ 由原 $M=0$ 真倒行双字确认。
取相容目标 $-J(V_{\rm base})/4$，便可同时支付 whole $E$ 与完整共同 $\mathcal A$ 的零值。Klein 的实际位移、桥和非零第四基准不删。

若从起点将原有理保护芽及 hook 背景保留为固定真实子字，控制接在其外部、并按同一端口与真倒行规则返回，那么该子字的 scalar germ 原样保留，$M=0$ 和同一第三 hook 也按加法保持。它的实际 incoming $m_*$、全 period 和其它 mixed 成本须按新路径重新取值，不能继承旧几何的结果。

这构造新的真实参考几何；不声称无代价装回一个旧冻结目标度量。Morse 或无常段若要同时保持，仍须有原结构词或完整低阶补偿证明。
在这些低阶条件已经精确保留的实际小扰动下，(16)给
$D_yJ(V_{\mathscr D(y)})=I$，R212 的全目标 IFT 可恢复全部 $J$。
它不能代替尚未证明的低阶结构保持。

## 6. 有限共同零值足够支付原整包 total

此节条件仍是**同一实际成本**已按(16)取 $E=0,\mathcal A=0$，
且同一圆与原 $M=0,\mathbf T=\tau\mathfrak H$ 背景及指定端口条件真实成立。
不假设 universal $\Lambda_{\rm all}=0$。

由 $\pi V=0$，R389/R407 的原全场极化给
$$
\Lambda_{su_i+tu_j}(V)
=s^5\omega_i+s^3t^2A_i(V;\mu_j)+t^5\omega_j
\quad(i<j).
\tag{24}
$$
(5)来自三个真实右包矩基，所以 $\mathcal A=0$ 使
$\omega_i=0$ 且 $A_i(V;n)=0$ 对每个真实或线性延拓的 $n$ 成立。
因此(24)准确支付 R394 实际使用的全部有限
$\Lambda_{u_i},\Lambda_{u_i+u_j}$ 零值；没有把辅助 self 增加进目标。

令 $R_i=a_i^2-b_i^2,T_i=a_ib_i$，保原真实 suffix
$$
n_{R,i}=\sum_{j>i}R_j\mu_j,\qquad
n_{T,i}=\sum_{j>i}T_j\mu_j.
$$
两个完整 period 的整包通量准确为
$$
a_i^3\{R_i\omega_i+A_i(V;n_{R,i})\},\qquad
-a_i^3\{T_i\omega_i+A_i(V;n_{T,i})\};
\tag{25}
$$
它们因同一个零目标全为零。没有假 suffix 本身为零，也没有改变包的真实次序。

whole $\mathcal Q=0$ 再按 R389 的原 self/有序极化使每个零平台上的真实 forcing 二阶导为零。这里用的是全部输入的原二次尾函数：先取 $u_i$，再取 $su_i+tu_j$，得到 $S_i,U_{ij}$ 的左尾只剩原仿射项。对 incoming $L_f$ 项使用不除 $p$ 的原式
$$
(L_fk)''=(A_fk'')'-V_fk',\qquad
A_f=6f'f'''-2(f'')^2,\quad V_f=6(f''f''')',
$$
在零平台上 $A_f=V_f=0$，故它也保留 $G''=0$，而不是从乘了 $p=0$ 的等式反推。

完整端部条件的使用清单如下；每项都作用于同一个新成本。

| 实际输入 | 原式付出的条件 | 没有付出的量 |
|---|---|---|
| universal $\pi V=0$ | R389 的完整有序展开(24)，以及 R288 的 rank-one 端一次指数层消去 | 内部 self/mixed 部分函数不置零 |
| universal $\mathcal QV=0$ | 所有原零平台的 $G''=0$ | 平台仿射值保留 |
| $\omega_i=0$ 与三个 $O_{i\alpha}=0$ | 真实三矩基给 $A_i(V;n)=0$ 对全部 $n$；因而所有实际 pair totals 及(25)为零 | 不要求 suffix 本身零，也不加入辅助 self 目标 |
| 原固定解析平端类别 | R276/R389 的 $G=P_e+p^2t^{-4}B(t)$，其中 $P_e''=0$ | 不取未证明的全区间紧逆 |
| 同一个累计通量在包右端为零 | 左右零端的真实光滑逆 germ | 内部 $A_f$ 点与 k 的值闭合仍欠 |

最后一行的右端分支使用
$F_i(x)=-\int_x^{r_i}f'G''$，它恰由原左端累计值加(25)得到；没有重置积分常数。加入已知 incoming $L_f$ 像不改变逆 germ 类。

R412 可使每包有有限多个简单 $p=f'$ 零点，而 R394 原陈述先使用每包一个简单 $p$ 零的子类。这里不偷换两者：R391(27)的证明逐点适用。对任一简单零 $x_0$，写 $s=x-x_0$，
$$
p=r_0s+t_0s^2/2+O(s^3),\quad
A_fp^2=-2r_0^4s^2+O(s^4),\quad
F_i(x)=F_i(x_0)+O(s^2),\qquad r_0\ne0.
$$
所以 $F_i/(A_fp^2)$ 没有 residue；原二阶方程在该点因 $A_f(x_0)=-2r_0^2\ne0$ 直接光滑穿过。有限多个点分别使用同一个原累计量，不新增常数或控制门。全部 $A_f$ 零仍为简单且与 p 零分离；它们的通量未在此支付。

因此，在原解析平端和实际简单退化范围内，R394 所使用的 universal 自然零前提可准确替换为这个**同一有限截面可实现的有限共同零目标**。它不与 R406 的 universal 自然全零障碍冲突：本库只看一个明确有限表示商，其他 profiles 上的自然值仍保留。

## 7. 真实内部条件和同一十三行仍然剩下

上述零目标不清内部部分函数。仍按原右锚定义
$$
S_i=V(u_i^2,0),\quad
U_{ij}=[s^2t^2]V((su_i+tu_j)^2,0),
$$
$$
s_i(x)=\int_{\ell_i}^x u_i'S_i'',\qquad
s_{ij}(x)=\int_{\ell_i}^x u_i'U_{ij}''.
$$
在第 $i$ 包的每个原简单 $A_f$ 点 $x_{i,\alpha}$，两条真正剩余门为
$$
R_i s_i(x_{i,\alpha})+\sum_{j>i}R_j s_{ij}(x_{i,\alpha})=0,
$$
$$
T_i s_i(x_{i,\alpha})+\sum_{j>i}T_j s_{ij}(x_{i,\alpha})=0.
\tag{26}
$$
外乘原 $\mp a_i^3/(2\tau)$ 才是 R394 的两 period forcing 通量。
(25)只付包的右端积分，不付(26)。
R395 的响应核例子已说明即便 whole $E$ 和全部自然函数都线性为零，这些内部读出仍可非零；不能由 total 零省略它们。

若(26)另被同一实际成本支付，原 R394 才给两条全 period 特解：
先在活动包解 $k'$，再保真实端 jets 于间隙延拓；
另用 gap 中 $k'$ 的积分修正支付 $\int k'=0$；
最后由右 collar 消掉 $L_fk-G$ 的仿射差。
第二步改变 k 的平台值，它的真实十三行代价不能删除。

完整核仍含活动包母函数列及平台列，间隙中 k 本身为零于全部活动包的方向才对十三行全盲。
同一个规范的最终相位方程仍为
$$
C_\theta\eta_\theta=-\mathcal A_\theta
(\sin\theta\,k_d+2\cos\theta\,k_e),
\tag{27}
$$
保 actual incoming $m_*$、两真特解及平台值。R394 的零行恒等与单位圆 Smith 可去极点条件仍须检查；十三不是已授秩。
允许 gauge 的 $L_f$ 像不改(25)和所有 $A_f$ 点的(26)，所以不能用(27)回避先付内部通量。

本稿没有给(26)全行的新 actual 满射，也没有把原十一指定对应点控制推广到全部不同母的所有点。其它路径段 ruling、高阶兼容、同一固定度量上的全曲面变形与嵌入同样不由(16)推出。

## 8. 条件定理的消费顺序

本稿的证明已经完成的逻辑是
$$
\text{同库(H)}
\Longrightarrow
C_J=J(U)
\Longrightarrow
\text{同一有限 }C^1\text{ 截面}
\Longrightarrow
\text{whole }E+\text{有限全部 totals/端 germ}.
$$
两个新完整 $\Omega$ 结果若满足原 $D/E_5$ 分支，则直接在旧共同库消费；
若只满足 R424 的 local C² 分支，须从起点使用增强 $F^\star$ 的同一次新母构造。
两者均不得拼成跨库结论。

直到(H)的实际原函数证据完成，(16)仍是条件结论。
其后需要支付的对象是同一成本的(26)及(27)，而不是再增加一套自然查询目录。
