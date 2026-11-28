# R1171：原中央 Frobenius 的参考提升仿射化与有限 Brandt 方程

日期：2026-11-28  
会话：Astra-serre-24b8836b-20261126  
状态：下述同源 Taylor 仿射化、商曲线首位修正及有限格中的唯一性接口已证明。相关项在足够多辅助素数上的独立读取仍须支付；不宣称原中央数值或主目标已经完成。无数学程序执行。

## 1. 结论：固定原 abelian 槽后的真实有限未知量

保持 [R1147](R1147-original-canonical-moment-Heisenberg-lift.md)、[R1149](R1149-original-relative-Hodge-section-and-central-connection.md) 的原 rank-$43$ tower、Hodge section、Weil 规范及有序群律。本文具体使用 R1149 §§11–14 和 [R1150](R1150-original-relative-log-Frobenius-and-crystalline-identification.md) 已付的相对同源比较；以下并不另选一个具有相同 connection 的未知格。

对每个几何超奇异同构类选一个未分歧好约化参考提升，并固定其原 abelian Frobenius 槽
$$
(X_i,Y_i,T_i).
\tag{1171.1}
$$
它们是原 $\mathsf M_4,\mathsf M_8,\gamma_5$ 的实际读取；这里“固定”是把这些值作为输入，不声称本文新算出了所有超奇异参考点上的值。对最高和第二中央槽，写
$$
Z_{\rho,i},\qquad \rho=0,2,\qquad d_\rho=12-2\rho.
$$
于是有以下结论。

**定理。** 原中央值在同一超奇异提升盘内的变化，是一个由原 coefficient crystal、已知 connection、(1171.1) 和提升的第一 $p$ 位决定的显式平移。这个平移不含 $Z_{\rho,i}$。特别，保持同一原 abelian 槽、connection 和原格的两个候选，其中央差在该盘上模 $p$ 是常数。

对任一已经有原同源功能方程的素数 $\ell\ne p$，把每个实际商曲线与所选参考提升之间的平移移到右端，得到
$$
\boxed{\quad
\bigl((\ell^4+\ell^{-11})-\ell^{\,2-\rho}T_\ell^{(d_\rho)}\bigr)
\mathbf Z_\rho=\mathbf R_{\ell,\rho}.
\quad}
\tag{1171.2}
$$
左端是 [R1170](R1170-original-supersingular-Brandt-common-kernel.md) 的原有限格算子，右端为 §6 的明确式；没有把原绝对中央函数假定为只依赖约化。

若这些实际右端在一个余有限素数族上已经独立读出，R1170 的单位理想使 $\mathbf Z_\rho$ 唯一且能以有限 Hecke 线性组合恢复。此最后一句保留右端的真实来源要求，不通过把未求的 $\mathbf Z_\rho$ 代回功能方程来“定义已知右端”。

## 2. 参考提升、系数格与同构等变性

沿用 R1170 §2，取有限域 $k/\mathbb F_p$，使全部超奇异代表 $E_i$ 以及它们两两之间的全部几何同态定义在 $k$ 上。有限性由有限多个代表及有限生成的 $\operatorname{Hom}(E_i,E_j)$ 给出。令
$$
W=W(k),\qquad K=W[1/p],\qquad \sigma:W\longrightarrow W
$$
为 Witt Frobenius。必要时再扩大 $k$，不进入有分歧基域。

每个 $E_i$ 选好约化提升 $\mathcal E_i/W$，并要求其全部特殊纤维自同构延伸：

- 若 $j(E_i)\ne0,1728$，自同构只有 $\{\pm1\}$，任一短 Weierstrass 提升都满足；
- 若 $j(E_i)=0$ 或 $1728$，分别取 $A=0$ 或 $B=0$ 的原 CM 型提升，相关 $6$ 次或 $4$ 次单位根取其 Teichmüller 提升。

$p>37$ 时这些自同构的阶与 $p$ 互素。取
$$
D_i=H^1_{\mathrm{crys}}(E_i/W),\qquad
\mathcal B_{d}=\bigoplus_i(\operatorname{Sym}^{d}D_i)^{\operatorname{Aut}(E_i)}.
\tag{1171.3}
$$
通过所选提升的 crystalline–de Rham 比较及原 pointed polarization，所有外部 Tate 因子沿 R1159、R1169 的同一规范读取。特别 $\rho=2$ 时原额外 $\ell^{-2}$ 不被吸收进一个新的系数 convention。

原 torsor、唯一 Hodge section 和 Frobenius 对实际自同构自然。设一个自同构在原整 frame 上的矩阵为 $A$，全 Frobenius、纯 coefficient Frobenius 分别为 $\Phi,\Phi^{\mathrm c}$。两者均满足
$$
A\Phi=\Phi\sigma(A),\qquad
A\Phi^{\mathrm c}=\Phi^{\mathrm c}\sigma(A).
$$
若 $\Phi=R(F)\Phi^{\mathrm c}$，消去可逆的 $\Phi^{\mathrm c}$ 得
$AR(F)=R(F)A$。因此参考点的 $X_i,Y_i,Z_{\rho,i}$ 确属于相应自同构不变量；这不是把可能未延伸的特殊纤维自同构强加给任意邻近提升。

在参考点取带约化标记的整 versal chart，参数 $u=0$ 对应 $\mathcal E_i$。可以先取与 $p$ 互素的 fine level，最后作上述有限自同构下降。也可直接使用短 Weierstrass chart：$B_i$ 为单位时固定 $B_i$、变化 $A$；$A_i$ 为单位时固定 $A_i$、变化 $B$。同余于一的缩放因 $4,6$ 为单位而唯一解出。Kodaira–Spencer 的相应系数是单位，故这是真正的整一维参数。

特别在 $j=0,1728$ 处使用 fine 参数，不把有分歧的 coarse $j$ 坐标当作整 uniformizer。这里也不把完整 heat 时间当作一个已知整 power series 参数。

## 3. 未分歧底上的半线性有限 Taylor 式

在上述 chart 取 R1149 §12 的原适配 Hodge frame。写
$$
M=\bigoplus_a W[[u]]e_a,\qquad
\operatorname{wt}(e_a)=-r_a,\quad 0\le r_a\le14,
\qquad D=\operatorname{diag}(p^{r_a}).
$$
基 $e$ 为行向量，连接矩阵满足
$$
\nabla e=eN(u)\,du,\qquad
N_{ab}=0\ \text{若 }r_a>r_b+1.
\tag{1171.4}
$$
纯 coefficient 对象在同一分裂旗标上有矩阵 $N^{\mathrm c}(u)$。原完整矩阵为
$$
N=N^{\mathrm c}+R_*(\alpha,0),\qquad
\alpha=(v_4^\infty E_6\nu^4\tau_1\,KS,\
        v_8^\infty E_{10}\nu^8\tau_1\,KS,\ 0),
\tag{1171.5}
$$
其中
$$
v_4^\infty=\frac{1-p^4}{252},\qquad
v_8^\infty=\frac{1-p^8}{132}.
$$
原 $\Pi_\rho$ 和最低槽的 $+\lambda_\infty x t'$ 均保留在 $R_*$ 中。式 (1171.5) 不含参考点的未知中央 Frobenius 条目。

令
$$
T'=TN,\quad T(0)=1,\qquad
(T^{\mathrm c})'=T^{\mathrm c}N^{\mathrm c},\quad T^{\mathrm c}(0)=1.
$$
参考点原 semilinear Frobenius 的 divided matrices 为
$$
C_i=\Phi_iD=R(F_i)C_i^{\mathrm c},\qquad
C_i^{\mathrm c}=\Phi_i^{\mathrm c}D\in\operatorname{GL}_{43}(W).
\tag{1171.6}
$$
在实际点 $u=pt$，$t\in W$，原水平比较给
$$
\Phi_i(t)=T(pt)^{-1}\Phi_i\,\sigma\!\left(T(pt)\right).
\tag{1171.7}
$$
右端的 $\sigma$ 同时作用于 Taylor 系数及 $t$。因此这不是把 $\mathbb Z_p$ 情形的 $t^p=t$ 简写搬到 $W(k)$。

记 $\xi=t\bmod p$，并把 $N(0)$、$N^{\mathrm c}(0)$ 中降低过滤恰好一阶的部分记作
$$
L_i=N_-(0),\qquad L_i^{\mathrm c}=N^{\mathrm c}_-(0)
\quad\text{于 }k.
$$
则
$$
\begin{aligned}
C_i(t)\bmod p&=\bar C_i\exp\bigl(\sigma(\xi L_i)\bigr),\\
C_i^{\mathrm c}(t)\bmod p
 &=\bar C_i^{\mathrm c}\exp\bigl(\sigma(\xi L_i^{\mathrm c})\bigr).
\end{aligned}
\tag{1171.8}
$$
这里 $\sigma(\xi L)=\xi^p\sigma(L)$；只在 $k=\mathbb F_p$ 且相应系数固定时才能再写成 $\xi L$。

为核整性，写 $T(u)=\sum_nT_nu^n$。原递推给 $n!T_n$ 整，且
$(T_n)_{ab}=0$ 若 $r_a-r_b>n$。在
$D^{-1}\sigma(T(pt))D$ 中，第 $n$ 项估值至少
$$
n-v_p(n!)-(r_a-r_b).
\tag{1171.9}
$$
若 $n\ge15$，这在 $p>37$ 时严格正；$n\le14$ 时分母是单位。模 $p$ 只剩 $n=r_a-r_b$ 的项，其全部因子都必须是 $N(0)$ 的降一阶部分，故系数正是 $L_i^n/n!$。同时 $T(pt)\equiv1\bmod p$。这证明 (1171.8)，也证明只读取 $\xi$ 而不读取 $t$ 的更高 $p$ 位。

原相对 associatedness 由 R1150 支付；R1149 §12 的参考 fibre 原格及小权全忠实性识别，保证这里计算的是原有限 tower。没有通过有理同构任意改变 lattice。纯 coefficient 矩阵 $C_i^{\mathrm c}$ 可由该参考好约化曲线的实际 crystalline cohomology 读取，属于几何系数输入，不是尚未知的中央 $F_i$。

## 4. 不含参考中央常数的群增量

用 (1171.6)–(1171.8) 相除，得到
$$
\boxed{\quad
R(\Delta_i(\xi))
=\bar C_i^{\mathrm c}
 \exp\bigl(\sigma(\xi L_i)\bigr)
 \exp\bigl(-\sigma(\xi L_i^{\mathrm c})\bigr)
 (\bar C_i^{\mathrm c})^{-1}.
\quad}
\tag{1171.10}
$$
并且
$$
\boxed{\qquad F_i(t)=F_i\,\Delta_i(\xi)\pmod p.\qquad}
\tag{1171.11}
$$
两个 exponentials 的次序不能交换。各单项严格降低总过滤次数，超过 $14$ 次便为零，因此 (1171.10) 是有限矩阵式；其中所有分母均与 $p$ 互素。

(1171.10) 真正落在原 $R(G)(k)$ 中。可以直接由 (1171.11) 两个同一原 torsor 的 Frobenius 比值得到；也可在 coefficient automorphism 与原 unipotent 群的半直积内使用 (1171.5) 验证。faithful $43$ 维表示的首列直接给出 $\Delta$ 的各有序坐标，不引入一个新的非线性开方。原第三个 abelian 槽的 connection 为零，故
$$
\Delta_i(\xi)
=(\Delta X_i,\Delta Y_i,0;\
  \Delta Z_{0,i},\Delta Z_{2,i},\Delta Z_{4,i}).
\tag{1171.12}
$$

因此对 $\rho=0,2$，有序中央变化是
$$
c^{\rm ord}_{\rho,i}(\xi)
=\Pi_\rho(X_i,\Delta Y_i(\xi))+\Delta Z_{\rho,i}(\xi),
\qquad
Z_\rho(\mathcal E_i(pt))
=Z_{\rho,i}+c^{\rm ord}_{\rho,i}(\xi).
\tag{1171.13}
$$
这一步使用的是原 $F_i\Delta$ 的顺序，而非 $\Delta F_i$。

若改为 BCH 中央
$$
W_\rho=Z_\rho-\frac12\Pi_\rho(X,Y),
$$
相应平移为
$$
\begin{aligned}
c^{\rm BCH}_{\rho,i}(\xi)
={}&\Delta Z_{\rho,i}
-\frac12\Pi_\rho(\Delta X_i,\Delta Y_i)\\
&+\frac12\left(
 \Pi_\rho(X_i,\Delta Y_i)
-\Pi_\rho(\Delta X_i,Y_i)\right).
\end{aligned}
\tag{1171.14}
$$
其中 $1/2$ 是整单位。实际功能方程若用 BCH 坐标，后文始终同时换用 (1171.14)；不能在左端有序、右端 BCH。

两式只使用原 abelian 参考值及 (1171.10)。所以同一 abelian 槽下两个候选的中央差为
$$
Z_\rho^{(1)}(\mathcal E_i(pt))
-Z_\rho^{(2)}(\mathcal E_i(pt))
=Z_{\rho,i}^{(1)}-Z_{\rho,i}^{(2)}.
\tag{1171.15}
$$
这里是同一原 connection、同一格、同一 right-torsor 规范下的比较。它不声称任意有限 jet section 都有此性质，也不声称每一个有限格向量都由某个全局算术 torsor 实现。

## 5. 实际商曲线的第一 $p$ 位及 coefficient 运输

固定 $\ell\ne p$、$C\subset E_i[\ell]$。由于 $\ell$ 可逆，有限 étale 子群有唯一提升
$\mathcal C\subset\mathcal E_i[\ell]$。令
$$
\mathcal Q_{i,C}=\mathcal E_i/\mathcal C.
$$
取约化同构 $E_i/C\simeq E_j$，并连同该标记将 $\mathcal Q_{i,C}$ 写入 §2 的参考 versal chart。于是得到实际
$$
u_{i,C}\in pW,\qquad
\xi_{i,C}=\frac{u_{i,C}}p\bmod p\in k.
\tag{1171.16}
$$
只需商曲线模 $p^2$ 的数据即可求出 $\xi_{i,C}$。例如对短模型作实际 Vélu 商，再用同余于一的缩放固定 chart 的一个非零系数即可。这里不把商曲线任意替成同一约化的另一个提升。

曲线 $\mathcal E_j(u_{i,C})$ 与参考 $\mathcal E_j$ 之间的原 coefficient crystal Taylor 运输模 $p$ 是恒等。这由 §3 的未除过滤幂的矩阵
$T^{\mathrm c}(u_{i,C})\equiv1$ 给出。因此实际同源的底层系数运输模 $p$ 正是特殊纤维的
$$
\psi_C^{-1}=\ell^{-1}\phi_C^*:
H^1_{\rm dR}(E_i/C)\longrightarrow H^1_{\rm dR}(E_i).
\tag{1171.17}
$$
商曲线重新归一的实际 shear 和微分缩放包含在 $\phi_C^*$ 中。特别不能将二同源的
$\phi_C^*\eta_C=2\eta-e_C\omega-d(y/(x-e_C))$
改成一个对角同构。

**此处只比较 underlying coefficient cohomology 模 $p$。** 不把恒等 Taylor 约化宣称为不同提升间的 Fontaine–Laffaille 同构；原 divided Frobenius 的全部差已经在 (1171.10) 中保留。后者正是只看底层模 $p$ 晶体会遗漏的输入。

改换约化同构会同时改变 chart 标记、$\xi_{i,C}$、矩阵 (1171.10) 和 (1171.17)。原 functoriality 及 §2 的参考自同构不变量使其合成不变。也可先在 fine-level chart 证明，再沿实际自同构下降。没有除以一个含 $p$ 的辅助分裂域次数。

## 6. 真实仿射 Brandt 方程

在已经有原功能方程的辅助素数范围内，R1159 §5 和 R1169 给
$$
\begin{aligned}
Z_{{\rm corr},\ell,\rho}(\mathcal E_i)
={}&(\ell^4+\ell^{-11})Z_{\rho,i}\\
&-\ell^{\,2-\rho}
 \sum_{|C|=\ell}\operatorname{Sym}^{d_\rho}(\psi_C^{-1})
 Z_\rho(\mathcal Q_{i,C}),
\qquad \rho=0,2.
\end{aligned}
\tag{1171.18}
$$
这里 $\rho=2$ 的外部因子是 $1$，因为两次 Weil 收缩所带的 $\ell^{-2}$ 已与原外部 $\ell^2$ 抵消。使用 BCH 时同一原群态射给完全相同的式子，只需所有中央符号一同解释为 BCH。

将 (1171.13) 或 (1171.14) 代入实际商曲线，定义
$$
\begin{aligned}
R_{\ell,\rho,i}
={}&Z_{{\rm corr},\ell,\rho}(\mathcal E_i)\\
&+\ell^{\,2-\rho}
 \sum_{|C|=\ell}\operatorname{Sym}^{d_\rho}(\psi_C^{-1})
 c_{\rho,j(C)}(\xi_{i,C}).
\end{aligned}
\tag{1171.19}
$$
则 (1171.18) 精确化为 (1171.2)，其中
$$
\mathbf Z_\rho=(Z_{\rho,i})_i\in\mathcal B_{d_\rho}/p,
\qquad
T_\ell^{(d_\rho)}
=\sum_{|C|=\ell}\operatorname{Sym}^{d_\rho}(\psi_C^{-1}).
\tag{1171.20}
$$
未知量现在只有每个参考提升上的中央常数，维数正是原有限 Brandt 格的维数。原绝对中央函数在同一约化盘上的非平凡变化被实际读取并放进右端，并非被删去。

此构造允许更换参考提升：先以原 (1171.13)–(1171.14) 计算参考值的平移，再在各商曲线项中作同一改变，方程 (1171.18) 不变。因而参考提升是有限记录的坐标选择，不是一个新增算术假设。

## 7. 共同核定理现在可作用于真实差；读取范围仍独立

若 $\mathbf Z_\rho^{(1)},\mathbf Z_\rho^{(2)}$ 保持同一原 abelian 参考输入，并有相同的实际相关项，那么 (1171.19) 的右端相同；其差满足
$$
V_{\ell,\rho}\bigl(\mathbf Z_\rho^{(1)}-\mathbf Z_\rho^{(2)}\bigr)=0,
\quad
V_{\ell,\rho}=(\ell^4+\ell^{-11})
-\ell^{\,2-\rho}T_\ell^{(d_\rho)}.
\tag{1171.21}
$$
若该等式已在一个余有限素数族成立，R1170 给差为零。其更强的整 Hecke 单位理想给有限个 $\ell_a$ 和同一有限 Hecke order 中的 $A_a$，使
$$
\sum_a A_aV_{\ell_a,\rho}=1.
$$
于是
$$
\boxed{\qquad
\mathbf Z_\rho=\sum_a A_a\mathbf R_{\ell_a,\rho}.
\qquad}
\tag{1171.22}
$$

(1171.22) 是准确的有限重建公式，但没有声称已实际选择并读取所有这些 $\ell_a$。R1157–R1158 的原 raw 构造先限制 $3<n<p$，$n=2$ 后来另付；若对 $\ell\ge p$ 使用相同的相关项来源，必须另付其整下降与完整余链，不能在辅助域次数含 $p$ 时沿用旧的反除次数。

同样，本文没有把定义于全模叠的 canonical product correlation 与“已经独立算出其中央数值”混同。若把 (1171.18) 右边尚未知的 $Z_\rho$ 用来定义左侧相关项，所得恒等式本身不能作重建输入。在 R1168 已证明的参考点与原 frame 范围内，现有 $n=2$ 相关项、原高 Hurwitz 系数及两条 abelian 矩可直接代入 (1171.19)。这不宣称所有一般超奇异参考点上的 (1171.1) 和相关项都已读取；这些实际输入与足够的辅助范围分别保留。

本文关闭的是 R1170 §8 第一处接口的准确仿射版本：不需要也不主张原绝对 $Z_\rho$ 约化不变，只需要已在 §§3–5 证明的同一原 abelian quotient 下的差值约化不变。

## 8. 为什么绝对约化不变性不能替代上述平移

R1149 (1149.38)–(1149.40) 的最高过滤计算也说明绝对约化不变性一般不能默认。在 $\mathbb Q_p$ 上的好超奇异参考点，沿 [R1153 §5](R1153-original-Kummer-to-Fontaine-Laffaille-calibration.md) 的整 opposite-basis 论证，取 $\mu=\varphi\nu=\lambda(\mu_g+d\nu)$，其中 $\lambda$ 为单位、$d\in\mathbb Z_p$。$\nabla\nu$ 的降一阶部分仍是 $\lambda^{-1}\mu$；额外 $\nu$ 项不进入 §3 的最高过滤项。因此同一有限计算适用，不需要把 generic 参考点称为 CM 点。若该参考点两个 Hodge source 标量 $A_*,B_*$ 都非零，则
$$
[\nu^{12}s^{14}]\Delta Z_0
=\frac{\lambda^2A_*B_*}{70},
\qquad
[\nu^{12}s^{14}]
\left(\Delta Z_0-\frac12\Pi_0(\Delta X,\Delta Y)\right)
=\frac{\lambda^2A_*B_*}{315}.
\tag{1171.23}
$$
第一式来自 $\int_0^s(v^5/5)v^8\,dv$；第二式再减
$s^5s^9/(2\cdot5\cdot9)$。参考 $F_i$ 与增量的中央 cross term 次数至多 $9$，不能消去这个 $14$ 次项。$p>37$ 时显示分母为单位。

这给原实际提升变化的具体来源，解释了为何不能把一个参考 $F_0$ 的数值不加修正地贴到所有同约化商曲线上。它与 (1171.15) 完全相容：该 $14$ 次项由共同 connection 决定，在保持相同 abelian quotient 的两个候选之差中恰相消。

此例不把 formal $\xi^p$ 当作 $\xi$；(1171.23) 按 R1149 的 $\mathbb F_p$ 实际点范围读取。也不从一般 jet 模块的 Hecke 分次推断原算术差自动属于该模块。本文的有限化使用原半线性 Taylor 与实际 quotient chart，而不是仅用一个次数上界。

## 9. 来源与本篇新增部分

- [R1149 §§11–15](R1149-original-relative-Hodge-section-and-central-connection.md)：原整小盘 Taylor 估值、幅度 $14$ 的同一格、left-cocycle/right-torsor 乘法次序及特殊参考点的完整式。本篇 §3 把其 $\mathbb Z_p$ 简写扩为 $W(k)$ 的真实 $\sigma$ 作用，证明同时给出。
- [R1150](R1150-original-relative-log-Frobenius-and-crystalline-identification.md)：同一完整 rank-$43$ tower 的 horizontal relative crystalline realization；用于排除“同 connection、不同算术 source”的替换。
- [R1159 §5](R1159-original-correlation-to-Hecke-cochain-comparison.md)、[R1169](R1169-original-second-central-correlation-and-Frobenius.md)：原 Norm trivialization、群态射、同源的 exact/shear 与两个实际功能方程。
- [R1168](R1168-original-unramified-PD-contraction-and-CM-moment-readout.md)：原 $n=2$ 相关项、完整 nonlinear gauge 和实际 abelian/Hurwitz 读取。本文不重算这些结论。
- [R1170](R1170-original-supersingular-Brandt-common-kernel.md)：有限整格、原同源归一及余有限算子族的单位理想；本篇不把它扩大为有限小素数已经足够。
- R1149 所用已刊小权 realization：Abhinandan，*Crystalline representations and Wach modules in the relative case*，Ann. Inst. Fourier **75** (2025), 379–474，Definition 5.1、Proposition 5.3、§5.3，[正式全文](https://aif.centre-mersenne.org/item/10.5802/aif.3670.pdf)。这里只沿既成原格与原 associatedness 使用，不调用未付的相对 essential-surjectivity。

新增已证内容是 (1171.10) 的半线性原增量、(1171.13)–(1171.15) 的同 abelian 仿射差、实际 mod-$p^2$ 商位置到 (1171.19) 的归一，以及它们使 R1170 真正作用于原候选差的接口。主目标、原中央非零性和全盘排除均未被提前宣告。

root 逐式核了整 Taylor 的幅度/阶乘界与半线性位置、两个 exponentials 的次序、右群增量的有序/BCH项、参考 Aut 延伸及实际 quotient 模 p² chart。对一般 SS 输入的范围已在 §7 明确保留；o2_high_coefficient 独立纸核核心矩阵与群律。无数学程序执行。


## 10. 可使用的无限辅助族：原三项整源不要求 $\ell<p$

本节将 §7 保留的辅助范围进一步缩到一个真正足够、且原 raw 下降仍能处理的素数族。对固定 $p>37$，定义
$$
\mathscr A_p=\{\ell:\ \ell>3\text{ 为素数},\
 \ell\ne p,\ \ell\bmod p\notin\{1,-1\}\}.
\tag{1171.24}
$$
可以从 $\mathscr A_p$ 再删去任意固定有限集合。

**原源延伸命题。** R1157 §§1–8、R1158 的完整 triangle、S/U、同根群态射和 correlation torsor 构造，对每个 $\ell\in\mathscr A_p$ 都成立；相应的 R1159、R1169 功能方程使用同一原规范。

证明须检查的是实际反除，而不只是符号的形式代入。R1157 §§2–5 的 trace-fixed theta、rank 表、三零边际与三函数 principalization，对任意辅助素数 $\ell\ne p$ 使用完全相同的有限和。所有分母只是 $24$、$\ell^2$、$\ell^6$ 或 $\ell^8$。三个 $p$-标记陪集不交只用 $(\ell,p)=1$。该处没有 $\ell!$，没有反除 $\ell-1$ 或 $\ell+1$。

R1157 §6 原先以 $3<\ell<p$ 保证 $\ell$-division splitting field 的次数与 $p$ 互素。其真正需要的条件正是
$$
p\nmid|\operatorname{GL}_2(\mathbb F_\ell)|
 =\ell(\ell-1)^2(\ell+1).
\tag{1171.25}
$$
对于素数 $\ell\ne p$，这等价于 $\ell\not\equiv\pm1\bmod p$，与大小无关。故在 (1171.24) 上，实际 $\ell$-division splitting field 的 Galois degree 仍是 $p$ 单位。四线分解再加入的只有实际二次、三次 splitting fields，其 Galois closure 的阶只含 $2,3$；与前域合成后次数仍是 $p$ 单位。原 R1156 Cor/res 上链同伦及其除次数因而逐字合法。

R1158 的多项式 $A,B,Q$ 总次数恒为 $12$，只除 $2,3$。 R1169 的第二槽 filling 总次数恒为八，只再反除 $7$；其 $1/28,1/42$ 与原 Weil-square 运输在 $p>37$ 下同样整。其原 S/U 重指标、rank-one 分支、全有序 even quotient 和共同交换商的群态射不受辅助素数大小影响。全 $p$-level descent 使用 induced product/Weil restriction，没有反除含 $p$ 的标记 cover degree。这些条件已在 R1158 §§5–6 写明。若作 all-vector $p^\infty$ extension，每层原 theta Norm 及标记过渡也只要求 $(\ell,p)=1$，故保持同一兼容根塔；没有在本节重新选各有限层 primitive。

原 quotient normalization 固定使用 R1147 §8 的同一个合法辅助素数 $c>3$、primitive modulo $p$，它使 $k_d(c)=c^2-c^{-d}$ 对 $d=4,8,12$ 均为单位。该篇未给 $c<p$，这里也不需要这个大小界。只须从 $\mathscr A_p$ 再删去至多一个素数 $\ell=c$，其余便有 $(c,\ell)=1$；下面的 Hecke 结论允许这一有限删除。原式从未反除 $k_d(\ell)$，所以它们为零时不产生新例外。

由此得到的 correlation 是原实际 torsor，不是一个只在 $K_2/p$ 中有相同边界的替代项。R1159 的指定 Norm quotient 点、唯一 Hodge section 和真实 coefficient 运输遂给 (1171.18)；$\Pi_2$ 保 R1169 的额外 $\ell^{-2}$。此命题扩展的是来源和功能方程，不声称它们在所有参考曲线上的中央数值已经读取。

## 11. 删去 $\ell\equiv\pm1$ 后，真实 Hecke 单位理想仍成立

以下补全不能仅靠“正密度素数很多”代替的 trace 步骤。

**二维 trace 引理。** 设 $\omega:G\to\mathbb F_p^\times$ 满射，$p>5$。设 $\rho,\rho_0:G\to\operatorname{GL}_2(\overline{\mathbb F}_p)$ 连续，具有相同 determinant。若
$$
\operatorname{tr}\rho(g)=\operatorname{tr}\rho_0(g)
\quad\text{对所有 }\omega(g)\notin\{1,-1\},
\tag{1171.26}
$$
则该等式对全部 $g\in G$ 成立。

取 $\omega(h)=a$，其中 $a$ 是 $\mathbb F_p^\times$ 的 primitive element；则 $a,a^2$ 都不在 $\{1,-1\}$。若 $\omega(g)=\pm1$，则 $h,gh,gh^2$ 的 $\omega$ 值都不在 $\{1,-1\}$。Cayley–Hamilton 对 $\rho(h)$ 给
$$
\operatorname{tr}\rho(gh^2)
-\operatorname{tr}\rho(h)\operatorname{tr}\rho(gh)
+\det\rho(h)\operatorname{tr}\rho(g)=0.
\tag{1171.27}
$$
对 $\rho_0$ 有同式。前三个已经已知的 trace 及相同的非零 determinant 唯一给出 $\operatorname{tr}\rho(g)$，证明引理。这里不要求 $g,h$ 交换，也不假定原残余表示已经半单。

在 R1170 §4 的具体有限无挠 Hecke order 中，只使用 $\ell\in\mathscr A_p\setminus\Sigma$ 的 Hecke operators，$\Sigma$ 为任意有限集。若对应 $V_{\ell,\rho}$ 生成真理想，仍从该 order 的极小素分支得到一个实际特征零新形式；子 order 不引入一个仅存在于特殊纤维的分支。

最高槽的假想系统给
$$
a_\ell(f)\equiv\ell^{14}+\ell^{-1}
\quad(\ell\in\mathscr A_p\setminus\Sigma).
$$
对包含 $\bar\rho_f$ 与 $\omega$ 的共同有限 Galois quotient，Chebotarev 将此等式推广到全部满足 $\omega(g)\ne\pm1$ 的元素：每个这样的 conjugacy class 有避开 $\Sigma$ 的 Frobenius 素数，其 cyclotomic 值自动满足 (1171.24)。然后应用 (1171.27)，得到全 $G_{\mathbb Q}$ 的 trace 等式及
$$
\bar\rho_f^{\,\rm ss}\simeq\omega^{14}\oplus\omega^{-1}.
$$
determinant 仍是原 $\omega^{13}$。于是 R1170 的 weight-$14$ 半稳定惯性矛盾原样成立。第二中央槽同理给
$\omega^{12}\oplus\omega^{-3}$、determinant $\omega^9$，违反 weight-$10$ 的界。

因此不只在余有限素数族，而在这个实际来源可用的族上已有
$$
\boxed{\quad
(V_{\ell,0}:\ell\in\mathscr A_p\setminus\Sigma)=1,\qquad
(V_{\ell,2}:\ell\in\mathscr A_p\setminus\Sigma)=1.
\quad}
\tag{1171.28}
$$
这里单位理想在 R1170 所用、由相同受限 prime set 生成的真实有限整 Hecke order 中解释。有限性、无挠性、characteristic-zero 分支和所有稳定格的惯性界均不改变；新增的完整步骤是 (1171.26)–(1171.27)，不是把一条密度结论直接当成 Chebotarev 的全特征判断。

## 12. 已关闭的辅助范围，以及现在剩下的实际读取

结合 §§6、10–11，原两个中央参考向量的精确有限重建可以使用全部来自 (1171.24) 的实际来源。存在有限个
$$
\ell_a\in\mathscr A_p,\qquad
A_a\in W[B_\ell:\ell\in\mathscr A_p],
$$
满足 (1171.22)。每个所用 raw tower 的辅助 splitting degree 都与 $p$ 互素；因此不需要先解决 $\ell\equiv\pm1\bmod p$ 的含 $p$ 分裂域下降。

这关闭的是两处结构接口：同一 abelian 槽下的实际仿射 Brandt membership，以及足够辅助 prime set 上的原功能方程来源。它没有给所需有限 $\ell_a$ 的统一大小界，没有证明只用 $2,5$ 已足够，也没有把已付 CM 参考点上的 raw readout 自动推广到所有超奇异参考提升。

下一数值／闭式输入准确为：同一组参考提升上全部实际 $(X_i,Y_i,T_i)$、所用 $\ell_a$ 的原 $Z_{{\rm corr},\ell_a,\rho}$，以及 mod-$p^2$ 商位置 (1171.16)。后者和系数 map 是有限曲线数据；前者须继续按原 theta/Miller/PD source 读取。没有把一般算术路径的未读值改名为“已知右端”，也没有把唯一性当成原中央非零性或全盘排除。

本三节只纸读并延伸 R1157–R1159 的精确来源，未执行新的数学计算。

root 新增逐读 R1157 §§1–6、R1158 §§5、7 及 R1147 §8，核全部实际反除、同根归一与标记下降；修正了不需要且原文未给的 c<p 小界。Cayley–Hamilton 的 h/gh/gh² 取值与行列式补全已逐式核准。


## 13. 最低槽的完整仿射化与三槽共同辅助素数族

### 13.1 最低 BCH 平移必须保留原 Tate-five 项

现在使用 [R1172](R1172-original-lowest-central-Tate-correlation-and-unsmoothing.md) 已付的完整最低群律
$$
\mathfrak b_4((X,Y,T),(X',Y',T'))
=\Pi_4(X,Y')+\lambda_\infty XT',
\qquad \lambda_\infty=\frac{21}{11}(1+p^4).
\tag{1171.29}
$$
本节的 $\lambda_\infty$ 沿同一整塔定义，读取模 $p$ 时才约化。参考点与增量仍是 (1171.10)–(1171.12)，特别 $\Delta T=0$。

从原右乘 $F_i\Delta_i(\xi)$ 直接得
$$
c^{\rm ord}_{4,i}(\xi)
 =\Pi_4(X_i,\Delta Y_i)+\Delta Z_{4,i}.
\tag{1171.30}
$$
这里没有 $\lambda_\infty X_i\Delta T$，因为 $\Delta T=0$。但最低 BCH 坐标的定义是
$$
W_4=Z_4-\frac12\{\Pi_4(X,Y)+\lambda_\infty XT\}.
$$
所以准确的平移为
$$
\boxed{\begin{aligned}
c^{\rm BCH}_{4,i}(\xi)
={}&\Delta Z_{4,i}
-\frac12\Pi_4(\Delta X_i,\Delta Y_i)\\
&+\frac12\{\Pi_4(X_i,\Delta Y_i)
             -\Pi_4(\Delta X_i,Y_i)\}
-\frac{\lambda_\infty}{2}\Delta X_i\,T_i .
\end{aligned}}
\tag{1171.31}
$$
最后一项来自改变后的 $X$ 与未改变的 $T_i$，不能由 $\Delta T=0$ 删去。两式均只含原 abelian 参考值、已知 coefficient crystal 及有限增量；没有 $Z_{4,i}$。因此 (1171.15) 的同 abelian 中央差论证对第三槽也成立。

参考自同构、实际 quotient 模 $p^2$ 标记及 underlying coefficient 运输完全沿 §§2、5。R1172 (1172.24) 使用的是已含 Tate 修正的 correlation，故其商曲线项前准确为 $\ell^{-2}$。于是
$$
\begin{aligned}
R_{\ell,4,i}
={}&Z_{{\rm corr},\ell,4}(\mathcal E_i)
+\ell^{-2}\sum_{|C|=\ell}
 \operatorname{Sym}^4(\psi_C^{-1})
 c_{4,j(C)}(\xi_{i,C}),\\
\bigl((\ell^4+\ell^{-11})-\ell^{-2}T_\ell^{(4)}\bigr)
 \mathbf Z_4
={}&\mathbf R_{\ell,4}.
\end{aligned}
\tag{1171.32}
$$
有序或 BCH 坐标须整式统一使用。这里的 $Z_{{\rm corr},\ell,4}$ 始终是 R1172 (1172.9)、(1172.18) 的完整 corrected 对象，不是裸 $\Pi_4$ 的 raw 双和。

### 13.2 一个同时满足全部整来源条件的无限族

令
$$
\boxed{\quad
\mathscr A_p^{(6)}
=\{\ell>3\text{ 为素数}:\ \ell\ne p,\ 
          \ell^6\not\equiv1\pmod p\}.
\quad}
\tag{1171.33}
$$
仍可删去任意固定有限集合 $\Sigma$，其中包含 §10 原辅助素数 $c$。这个族包含无穷多个素数；例如 primitive residue class 经 Dirichlet 定理给出。此处不要求 $\ell<p$，也不给最小可用素数界。

由于 $\{\pm1\}\subset\mu_6(\mathbb F_p)$，
$\mathscr A_p^{(6)}\subset\mathscr A_p$。所以 §10 的实际 division-field、四线 splitting、同根 Cor/res、完整 S/U、induced descent 和两个最高槽来源全部有效。此外
$$
k_4(\ell)=\ell^2-\ell^{-4}
         =\ell^{-4}(\ell^6-1)\in\mathbb Z_p^\times .
\tag{1171.34}
$$
故 R1172 (1172.8) 的
$\kappa_\ell=\lambda_\infty v_{\ell,4}/k_4(\ell)$ 是原整标量，其 product/Norm kernel 逆像和完整 Tate 群态射也有效。

为明确大辅助素数的范围，R1172 §§2–4 的其余步骤只用实际 prime-to-$p$ 同源、指定 theta Norm 点、原基域 $\gamma_5$ 的单位倍，以及原 $R,L,K,\eta_4$ 的有限陪集式。它们不要求 $\ell<p$；相关 splitting degree 的唯一反除已由 (1171.25) 支付。最低 corrected cup 的指定算术 primitive
$$
h_{{\rm corr},4}
=-\mathcal B_{4,6}(\Omega_{{\rm corr},4})
$$
沿 R1172 (1172.19)–(1172.20) 构造，不除 $v_{\ell,4}$。所以 $v_{\ell,4}$ 对某个 $\ell$ 约化为零也不影响该 torsor 和 (1171.32)。若另外使用除 $v_{\ell,4}$ 的未平滑公式，仍可按 R1172 取 $n=2$；本节没有把该反除强加到 (1171.33) 的所有素数。

相同地，本节不要求 $k_8(\ell)$ 为单位；原两个 raw 槽的群 map 使用它作乘数，并未反除。三槽因此确可共用 (1171.33)，无须为每槽另选互不相容的根规范。

### 13.3 去掉全部六次单位根仍足以补全 Galois 迹

把 §11 的 trace 引理中的 $\{\pm1\}$ 换成子群
$$
H=\mu_6(\mathbb F_p)=\{x\in\mathbb F_p^\times:x^6=1\}.
$$
设两连续二维残表示具有同一 determinant，且 trace 在所有 $\omega(g)\notin H$ 上相同。取 $\omega(h)=a$ 为 primitive element。因为 $p-1>12$，$a,a^2$ 都不在 $H$。若 $\omega(g)\in H$，则 $h,gh,gh^2$ 的 cyclotomic 值均不在 $H$；这是子群条件，而不是对三个无关素数同时作分布假设。对两表示同用 (1171.27)，相同且非零的 $\det(h)$ 唯一补回 $t(g)$。故全部 Galois 元素的 trace 相同。

在各自真实有限无挠 Hecke order 中，假设相应受限算子理想为真理想。沿 §11 的 characteristic-zero 分支和共同有限 Galois quotient，Chebotarev 先在 $\omega(g)\notin H$ 上给 trace，再由上一段补到全部 $G_{\mathbb Q}$。三个残余目标及其标准 determinant 是
$$
\begin{array}{c|c|c|c}
\rho&d_\rho&\text{假想残余半单表示}&\det\\ \hline
0&12&\omega^{14}\oplus\omega^{-1}&\omega^{13}\\
2&8&\omega^{12}\oplus\omega^{-3}&\omega^9\\
4&4&\omega^{10}\oplus\omega^{-5}&\omega^5 .
\end{array}
\tag{1171.35}
$$
前两行由 R1170 §§4–6 排除，第三行由其 §10 的 weight-$6$ 半稳定惯性界排除。所有比较使用同一 cyclotomic 约定及实际 $B_\ell=\ell^{d_\rho}T_\ell^{(d_\rho)}$，没有把最低 Tate 因子改进一个未知 twist。

因此，对任意固定有限 $\Sigma$，都有
$$
\boxed{\quad
\bigl(V_{\ell,\rho}:\ell\in\mathscr A_p^{(6)}\setminus\Sigma\bigr)=1,
\qquad
V_{\ell,\rho}=(\ell^4+\ell^{-11})
-\ell^{\,2-\rho}T_\ell^{(12-2\rho)},
\quad \rho=0,2,4 .
\quad}
\tag{1171.36}
$$
各单位理想均在对应的真实受限 Hecke order 中。各取一个有限证书，再取三个素数集合的并，便得到同一有限辅助集合同时支持三槽的重建。无需声称三个不同系数格的证书系数相同。

### 13.4 已得的三槽结构与仍须读取的最低输入

给定同一原 $(X_i,Y_i,T_i)$，三槽现在均满足 §§6、13.1 的实际仿射方程，并能在同一个原来源可用的辅助族中用单位理想比较候选差。所有第一 $p$ 位、$\sigma$、actual quotient shear、lowest Tate term 都保留。

这不把 R1172 已构造的 $h_{{\rm corr},4}$ 自动认作已读出的局部 Frobenius 值。其独立算术构造包含原 $\mathcal B_{4,6}$ 的实际共轭路径；在这些值或另一个同源局部读取尚未给出之前，(1171.32) 的最低右端仍是待读输入。特别不能把 R1168 对最高相关项的读取挪作这个含 $\lambda_\infty$ 的 corrected 对象，也不能由三槽共同核为零推出它们的值为零。

本节新增的是三槽共同来源、最低槽完整仿射修正及同一受限素数族的单位理想。未执行数学程序，未预支原中央非零性或一般 $p$ 的排点结论。
