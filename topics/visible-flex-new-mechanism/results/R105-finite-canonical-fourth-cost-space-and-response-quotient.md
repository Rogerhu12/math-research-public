# R105：完整 canonical 第四成本的有限函数空间与真实响应商

日期：2026-11-14。**已证明。** 纸面有限化，不运行新的 profile、几何或完整研究编译。依据 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md) 的逐点分子恢复式、[R70](R70-zero-matrix-bridges-and-affine-complete-fourth-period.md) 的真实零矩连接、[R83](R83-true-fourth-transfer-and-zero-lower-history-variations.md) 的完整输入历史及 [R89](R89-affine-covariance-and-positive-multiple-pair-P1.md) 的全场协变。

本稿把 R102 留下的一个具体问题付清：固定同一 canonical 目标、同一右锚规则和零传入历史后，不仅每条路径的第四周期分别有限，**所有真实路径的完整第四成本共同落在同一个有限 profile 模板空间**。其真实 span 仿射不变，可以由一个合法光滑三矩圆上的有限查询忠实表示。尚未证明这个空间等于已可调响应空间；剩余的商和完整 ruling 仍须处理。

## 1. 固定成本的定义和适用范围

固定两个实输入 profiles $f,g$，令

$$\phi_\theta=\cos\theta\,f+\sin\theta\,g,\qquad
F=f\odot f,\qquad D_\theta=F-\phi_\theta^2.$$

采用既有固定度量目标 $g_X+\varepsilon^2\,dY_f\cdot dY_f$。第二、第三场一律按 R56 的真实右 collar 锚和同一个 $s$ 起点、零 scalar 传入值恢复；第四成本 $V_B(F,\phi_\theta)$ 是整条路径上的完整第四 characteristic RHS 积分。

这是固定 canonical 选择。不额外加入依赖任意新 profile 的二、三阶齐次 gauge，不改变目标，不在路径中途重锚，也不先删除未付的左尾或 ruling 缺陷。

即使某条候选的低阶双 collar/range 尚未支付，R56 的 canonical 右锚代数和历史沿有限路径仍有定义。本稿此时只把它们当作相应必要方程的真实局部恢复及成本表达式，不把它们冒充已经全周期、双 collar 的校正场。

当 $\theta=0$ 时 $D_\theta=0$，零锚 canonical 第二、第三场和第四 forcing 都为零。加上实结构，全部相位由 $-4,-2$ 两个复模式决定；等价地可用四个实输出函数。下文的“第四算子”均指这个完整相位对象。

## 2. 移动的 xi 极点逐阶被消去

用 R56 的记号

$$z=\xi+\omega,\quad e=hz-k,\quad
\gamma=h_s,\quad \nu=k_s/(2h),\quad
\lambda=\frac{\gamma z-h\nu}{h^2},$$

$$K_0=kz^2-\frac{k^2+1}{h}z.$$

假设已知场写成 $Z_i=F_{\rm frame}V_i/z$。对任一常系数对称二次 forcing，记真实分子配对为

$$J=\sum C_{ij}V_i\cdot V_j,\quad
T_\xi=\sum C_{ij}(V_i)_\xi\cdot(V_j)_\xi,$$

以及包含真实协变导数 $\nabla_sV=V_s+\Omega(k)V$ 的 $T_s,T_{s\xi}$。forcing 张量本身确实会出现 $z^{-2},z^{-3},z^{-4}$。这些不能被默默当作固定 profile 系数。

关键是完整恢复式准确给

$$B=\frac{J}{2h},\qquad
P=-\frac1{2h}\int_r^\xi T_\xi(s,\eta)\,d\eta,\qquad
\rho=P+B/z,$$

$$\boxed{\mathcal R_H=
\frac{T_s}{2h^2}+K_0P-\lambda P_s+
\left(kz-\frac{k^2+1}{h}\right)B-\frac{\gamma}{h^2}B_s,}\tag{1}$$

$$\boxed{\eta_0=
-\frac{T_{s\xi}}{2h}
+\frac{\gamma z-h\nu}{2h}P_\xi
+\frac{\gamma}{2h}B_\xi-\frac12P_s.}\tag{2}$$

所有 $1/z$、$1/z^2$ 余项在 (1)、(2) 中**逐点相消**，不需要先积分一个周期，不需要 $\gamma,\nu$ 为零，也不使用任何低阶 range 为零的假设。

令

$$W(s,\xi)=\int_0^s\mathcal R_H(\sigma,\xi)\,d\sigma,\qquad
A=\frac12W_\xi+\frac{\eta_0}{h}.$$

新分子为

$$\boxed{V_{\rm new}=(A,\ zP+B,\ eA-hW).}\tag{3}$$

所以虽然物理场仍为 $F_{\rm frame}V_{\rm new}/z$，下一步需要的分子 $V_{\rm new}$ 没有移动的 $\xi$ 分母。再次组成完整二次 forcing 后，同一恒等式继续适用。

这正是为何不能仅看到物理 $u=h/z$ 或 $1/u$ 就判断会出现随路径变化的无限维有理 profile 族。第四成本使用的是 (1)，它已经把这种移动极点准确消掉。$1/h$ 等分母只依赖 $s$，不依赖 $\xi$。

## 3. 一个共同有限模板空间，独立于路径取值

从两个初始场开始：

$$V_{Y_f}=(-f'/2,\ 0,\ hf-ef'/2),\qquad
V_{Y_g}=(-g'/2,\ 0,\ hg-eg'/2).$$

将 $h,k,\omega$ 及其 $s$ jets 暂视为形式的系数函数。第一阶的 profile 部分只含 $f,g$、一阶导数和有限次 $\xi$。

按 (1)–(3) 构造第二、第三场及第四 characteristic RHS。每步只作以下有限操作：

1. profile 微分、乘积、乘有限次 $\xi$；
2. 同一个右端锚的 Volterra 原函数；
3. 几何系数的加、乘、求 $s$ 导数，以及乘 $h$ 的整数幂；
4. 沿真实 $s$ 起点对几何系数积分。

$\nabla_s$ 中的 $\Omega(k)$ 只作用在三维分量并加入几何系数。正交框架在内积中消失，中心线位置不进入这些 scalar 分子。积分上下端 $0,L$ 对每条路径固定，与 $\xi$ 无关。

固定到第四阶、固定有限相位通道后，语法树的操作次数有限。可以在给几何系数任何实际值之前，先生成一个有限集合

$$\Psi_1(f,g)(\xi),\ldots,\Psi_N(f,g)(\xi)$$

作为完整四实模式向量的模板，使每条有限真实路径都满足

$$\boxed{V_B=\sum_{\alpha=1}^N c_\alpha(B)\Psi_\alpha.}\tag{4}$$

这里 $N$ 是一个有限上界，不先声称模板独立。$c_\alpha(B)$ 可以是真实非有理数，也可以含 $\log h$、有限 ODE 历史或其他非有理时间积分；这些全部只是几何系数。它们不会生成 $\xi$ 的对数、移动极点或依赖路径的新 profile 节点。

这个论证比“对每条路径分别选一组函数”更强：同一个有限递推先产生模板，再由不同路径给系数赋值。完整 compiler 的既有有限 DAG 是这种递推的一个实现，但本命题不依赖其计数，也没有把冗余原模板个数当作真实维数。

所有模板都对 $(f,g)$ 为四次齐次。每个右原函数节点有严格正的 profile 次数。对紧支撑输入，支撑右方的所有 jets 和所有递归原函数均为零，故把右锚移到更右的空区不改变 (4)。左尾全部保留；本稿没有将其重置为零。

## 4. universal 延拓与物理区间的区别

式 (4) 的有限 profile 模板可作用于任意紧支撑光滑实输入，右锚取在支撑右方。这给每条路径的完整成本一个无移动极点的 universal 算子表示。

这只是用于定义函数空间的准确延拓，并不把 $\xi+\omega=0$ 附近的物理曲面变成合法浸入。任何几何应用仍须先对所需有限路径和小参数族选共同物理区间 $I$，保持 $h>0$ 和 $\xi+\omega>0$ 的正间隙，随后才在 $I$ 内选 profiles。

右锚的独立性来自正 profile 次数和真实空区，不依赖丢弃常数；因此后面的仿射变换和路径比较可使用同一个 profile 代数。

## 5. 真实成本 span 与端口无关

固定一个 scalar 常值 germ $g$，frame 取 $I\to I$。定义

$$\mathcal S_g=\{V_B:\ B\text{ 是实际有限同端口路径， }M_B=T_B=0\},$$

$$\boxed{\mathcal U_4(g)=\operatorname{span}_{\mathbb R}\mathcal S_g.}\tag{5}$$

由 (4)，$\mathcal U_4(g)$ 有限维。这是**真实函数 span**，不是不完备正规形的代表空间，也不是把实际成本半群定义成可自由取负。

设另一个 germ 为 $g_1$。取 R70 的真实 $M=0$、frame $I\to I$ 桥 $C:g\to g_1$。对任一 $B\in\mathcal S_{g_1}$，全部三块 $C,B,C^R$ 均为零矩阵，故 R83 的传递准确给

$$M_{CBC^R}=T_{CBC^R}=0,\qquad
V_{CBC^R}=2V_C+V_B.$$

而另一条实际路径 $CC^R$ 满足

$$M_{CC^R}=T_{CC^R}=0,\qquad V_{CC^R}=2V_C.$$

所以

$$\boxed{V_B=V_{CBC^R}-V_{CC^R}\in\mathcal U_4(g).}\tag{6}$$

反向连接同理，得到 $\mathcal U_4(g_1)=\mathcal U_4(g)$。以后统一记作 $\mathcal U_4$。

(6) 只是在真实线性 span 中取两个实际成本的差。它没有给一个可用来实现 $-V_{CC^R}$ 的实际路径。

另有一个有用的生成简化：同端口、frame $I\to I$ 的任一实际零矩阵路径 $B$，即使 $T_B$ 未零，也有

$$M_{BB^R}=T_{BB^R}=0,\qquad V_{BB^R}=2V_B.$$

因此

$$\boxed{\mathcal U_4
=\operatorname{span}\{V_B:\ B\text{ 为同端口真实零矩阵路径}\}.}\tag{7}$$

寻找真实 span 的原料不必每次先消去完整第三算子；但实际半群和最终候选的第三条件仍然必须支付。

## 6. 完整仿射不变及有限 Laurent 表示

R89 的全场变换把任何真实路径变成另一个真实路径，并保零矩阵、零第三算子：

$$\widetilde h=Hh,\quad \widetilde k=k,\quad
\widetilde\omega=(\omega+d)/H,\qquad H>0.$$

第四输出准确为共同 profile pullback

$$(\mathsf P_{H,d}V)(f,g)(\xi)
=V(C_{H,d}f,C_{H,d}g)(H\xi+d),$$

其中 $C_{H,d}f(x)=f((x-d)/H)$，右锚同步变换。变换后的 germ 可能改变，但第 5 节已经证明真实 span 不依赖 germ。反变换同样成立，所以

$$\boxed{\mathsf P_{H,d}\mathcal U_4=\mathcal U_4.}\tag{8}$$

对固定有限模板，一个 $j$ 阶 profile jet 给 $H^{-j}$，一个右原函数给 $H$，一个坐标幂给 $(H\xi+d)^j$。故在 $\mathcal U_4$ 的任一固定有限真实基中，(8) 的矩阵关于 $H$ 是有限 Laurent 多项式、关于 $d$ 是有限多项式。

这里非有理的几何系数 $c_\alpha(B)$ 只是固定实数，不破坏这一表示性质。没有要求几何路径对 $s$ 解析，也没有对其真实时间积分作级数截断。

## 7. 可调响应包含于实际成本 span

记 R101/R102 的完整响应空间为

$$\mathcal R_8=\operatorname{span}
\{\mathcal B_P(\tau):P\in E_8,\ \tau\in W\}.$$

R101 的实际词对任意小非零 $t$、固定 $n=1$ 给

$$V_{Z(t,1)}-V_{Z(-t,1)}
=2t\,\mathcal B_P(\tau).$$

两项都是真实 $M=T=0$ 成本，故

$$\boxed{\mathcal R_8\subseteq\mathcal U_4.}\tag{9}$$

这里“子空间”不预先宣称严格包含。R98/R99 已证 $\dim\mathcal R_8\ge15$，而 R102 给上界 288；本稿没有计算 $\dim\mathcal U_4$ 或两者之差。

定义剩余完整函数商

$$\boxed{\mathcal Q_4=\mathcal U_4/\mathcal R_8.}\tag{10}$$

它是一个真正有限维的实函数商。它不是有限节点余差，也不是对冗余模板逐项置零。若用原式模板计算，必须支付真实函数关系，或采用准确分离证书；不能把一个不完备正规化余项直接当作非零商类。

复制式在这个商中只剩

$$[V_{Z(t,n)}]=[E(t)]+2n[v],\tag{11}$$

因为 $nt\mathcal B_P(\tau)$ 已被商掉。这清楚标出 R102 尚未支付的部分：signed tangent 对查询的线性控制，不会自动移除这些真实基准商类。

## 8. 用同一个合法圆忠实表示完整成本空间

有限维真实 span $\mathcal U_4$ 的基可以从有限条实际 $M=T=0$ 路径的成本中选取。再固定一组生成 $\mathcal R_8$ 的有限实际控制小族，必要时加入预先指定的参考配置。对这有限集合及其紧小族选择共同物理区间 $I$。

因为基成本已经在该集合中，所有在这个 $I$ 合法的实际路径成本的 span 仍是整个 $\mathcal U_4$。这里不是宣称任意预给的窄区间自动具备此性质；顺序仍是先选有限实际集合，再选 $I$。

第 3、6 节逐项支付了 R96 的假设：有限、统一四次、正次数右 Volterra、完整有限 Laurent 仿射表示。因此可在这个 $I$ 内选同一个合法非退化、归一的 $C^\infty$ 三矩圆及有限个实查询，使

$$\boxed{\mathcal E:\mathcal U_4\longrightarrow\mathbb R^{m},
\quad m=\dim\mathcal U_4,\quad
\mathcal E\text{ 单射}.}\tag{12}$$

若还需要同时保持 R98 的正字符，可对有限仿射空间 $\mathcal U_4+V_{\rm ext}$ 作同一构造，再限制到 $\mathcal U_4$。

对这个特殊选定的圆和查询，任意两个 canonical 实际成本在全部查询上一致，当且仅当它们在真实 $\mathcal U_4$ 中是同一个完整 universal 算子。这个结论多用了 (12) 的准确单射，不能反推任意普通采样网格也有此性质。当前没有给该基、查询或 packet 参数的数值清单。

## 9. 整函数控制的一个准确充分门

若将来能证明

$$\mathcal U_4=\mathcal R_8,$$

则用 (12) 的 $m$ 个查询，并选择 $\mathcal R_8$ 的真实原生成基，R102 的查询矩阵满秩。其有限复制论证对每个目标 $U\in\mathcal U_4$ 产生真实 $M=T=0$ 路径 $B$，满足

$$\mathcal E(V_B)=\mathcal E(U).$$

由 (12) 的单射，准确得到整个函数身份 $V_B=U$。这时才可把有限查询控制升级为完整 canonical 第四周期控制；连 $U=0$ 也由一个实际有限词实现，不需要把成本倒行取负。

当前**没有证明**这个等号。若 $\mathcal Q_4\ne0$，还须研究其实际成本半群和可能的非负泛函；即使 $\mathcal Q_4\ne0$，也不能仅由维数差断言目标不可达。

对所选共同 $I$ 的实际成本闭凸锥，R102 的真实复制证明其 lineality 包含 $\mathcal R_8$，所以剩余非负成本门只可能位于 (10) 的对偶中。这个闭凸锥仍是松弛，不能代替实际有限路径可达性。

## 10. 保留的缺口

(4)–(12) 只处理固定 canonical 目标、同右锚和零传入历史的完整第四周期。它们不处理任意新增 profile gauge，不把逐 $s$ 的 ruling 变成同一个固定函数空间，也不证明低阶或第四阶的双 collar 条件已经支付。

尚须确定 $\mathcal Q_4$ 的实际内容、匹配目标在其中的成本、支付完整 ruling，再处理更高阶、收敛、闭嵌入曲面、reach 与宏观位移。本文提供了准确的有限函数问题和真实成本生成门，不把模板有限化当作主课题完成。
