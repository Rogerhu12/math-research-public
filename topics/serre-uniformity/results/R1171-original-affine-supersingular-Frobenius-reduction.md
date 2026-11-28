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
