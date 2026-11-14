# R228 附录：点态实化、反射偶奇实配对与预解商的带权实结构

日期：2026-11-13（UTC）。作者：normal_resume_1cf；Astra-ISP-1cf8c51d 已核查泛函变换、实偶奇配对、带权商投影和无限正负指数。

状态：已证明，正有限秩见证的精确实化及秩约束。C 实化保同一泛函是 [R228](R228-positive-finite-rank-realification-and-minimal-support.md) 已证结论；这里单独处理实际模型的点态共轭 J_0，并区分不变泛函、实化后改变的泛函、原最小域及商坐标。没有降任意正见证为秩一，也没有从 Krein 对称性推出共同图核心。

## 1. 三种不同的实际对称

在 $H=L^2(\mathbb Z_2)$ 上记
$
 (J_0f)(y)=\overline{f(y)},\qquad
 (\mathcal Rf)(y)=f(-1-y),\qquad C=\mathcal R J_0=J_0\mathcal R.
$
J_0、C 是反线性等距对合，$\mathcal R$ 是线性自伴酉对合。

实际权及慢系数为实，故
$
 J_0A=AJ_0,\qquad J_0S=SJ_0
$
对本题的 S_N、S_Y 均成立。因而
$
 \overline F:=J_0FJ_0\in\mathfrak C=A'\qquad(F\in\mathfrak C).
$
R24/R88 的另一个恒等式是 $F^*=CFC$；这不说 $F$ 与 C 交换，也不说所有 F 都是 J_0 实的。

[R176 的实结构稿](R176-appendix-real-structure-affine-lines-and-odd-power-cyclicity.md)已使用点态共轭与实 first 乘子。以下不将这一事实重新登记为新结论。

## 2. J_0 平均保持真湮灭，但一般改变整个泛函

设
$
 \rho=\sum_{i=1}^r f_i\otimes f_i\ge0,\qquad
 \tau=\operatorname{Tr}\rho>0,\qquad
 \phi_\rho(S\mathfrak C)=0.
$
有限秩向量展开直接给
$
 \phi_{J_0\rho J_0}(F)
 =\overline{\phi_\rho(\overline F)}. \tag{2.1}
$
因为 S 实，$\overline{SF}=S\overline F$，故 $J_0\rho J_0$ 仍湮灭 $S\mathfrak C$。所以
$
 \rho_0=\tfrac12(\rho+J_0\rho J_0) \tag{2.2}
$
正、同迹、秩至多 $2r$，满足 $J_0\rho_0J_0=\rho_0$ 并保持原真湮灭条件。

必须保留 (2.1) 的共轭；一般没有 $\phi_{\rho_0}(F)=\phi_\rho(F)$。对 J_0 实的 F，新的值是原值的实部。

相反，R228 §1 已证明
$
 \phi_{C\rho C}(F)=\phi_\rho(F)\qquad(F\in\mathfrak C). \tag{2.3}
$
(2.3) 合法；此前不能作的步骤是把 C 不经核验施于未知子商、假定普通 $T\rho T^*$ 保湮灭，或把可能增秩的 C 平均迭代当成降秩。

由于两个共轭交换，可进一步取
$
 \sigma=\tfrac14(\rho+J_0\rho J_0+C\rho C+
                         \mathcal R\rho\mathcal R). \tag{2.4}
$
它正、同迹、秩至多 $4r$，仍湮灭 $S\mathfrak C$，且
$
 J_0\sigma J_0=C\sigma C=\mathcal R\sigma\mathcal R=\sigma,
 \qquad \phi_\sigma|_{\mathfrak C}=\phi_{\rho_0}|_{\mathfrak C}. \tag{2.5}
$
每个非零有限维谱空间同时被 J_0 和 $\mathcal R$ 保持。先分反射的 ± 空间，再选实正交基，得到
$
 \sigma=\sum_j h_j\otimes h_j,\qquad
 J_0h_j=h_j,\quad \mathcal Rh_j=\varepsilon_jh_j,\quad
 Ch_j=\varepsilon_jh_j,\quad \varepsilon_j\in\{1,-1\}. \tag{2.6}
$
没有声称这样的双重对称表示仍达到原最小秩。

## 3. 反射偶奇谱项可在实类内两两合并

记 $H_\pm=\ker(\mathcal R\mp I)$、$P_\pm=(I\pm\mathcal R)/2$。
若 u、v 均为 J_0 实，且 $u\in H_+$、$v\in H_-$，则对全部 $F\in\mathfrak C$，
$
 \langle Fu,v\rangle=-\langle Fv,u\rangle. \tag{3.1}
$
确实 C 对称性给
$\langle Fu,v\rangle=\langle FCv,Cu\rangle$，而 $Cu=u,Cv=-v$。

所以实向量 u+v 满足
$
 \langle F(u+v),u+v\rangle
 =\langle Fu,u\rangle+\langle Fv,v\rangle. \tag{3.2}
$
这与 R228 将两个 C 实谱向量用复系数 i 配对不同：这里直接在点态实向量类内合并相反反射奇偶。

更一般，设 $\rho\ge0$ 有限秩且 J_0 实，记
$
 p=\operatorname{rank}(P_+\rho P_+),\qquad
 q=\operatorname{rank}(P_-\rho P_-).
$
反射平均准确等于
$
 \tfrac12(\rho+\mathcal R\rho\mathcal R)
       =P_+\rho P_++P_-\rho P_- . \tag{3.3}
$
由于 $\mathcal R\rho\mathcal R=C\rho C$，(2.3) 表明 (3.3) 在整个 $\mathfrak C$ 上保同一泛函。

取两个正块的实谱分解 $\sum_{j=1}^p u_j\otimes u_j$、
$\sum_{j=1}^q v_j\otimes v_j$，把短的一列补零，再令 $w_j=u_j+v_j$。由 (3.2)，
$
 \widehat\rho=\sum_{j=1}^{\max(p,q)}w_j\otimes w_j
$
是 J_0 实正密度，同迹，且
$
 \boxed{\phi_{\widehat\rho}|_{\mathfrak C}
             =\phi_\rho|_{\mathfrak C},\qquad
         \operatorname{rank}\widehat\rho=\max(p,q).} \tag{3.4}
$
秩的等号也有直接理由：若 p≥q，P_+ 将这些向量送到线性无关的 p 个 u_j；反之用 P_-。

因此若存在真正见证，可以在 J_0 实见证中选最小秩 d 者。令 W 为其支撑，有限维正性给
$
 p=\dim P_+W=d-\dim(W\cap H_-),\quad
 q=\dim P_-W=d-\dim(W\cap H_+).
$
最小性及 (3.4) 迫
$
 \boxed{\max(p,q)=d,\qquad
  \min\{\dim(W\cap H_+),\dim(W\cap H_-)\}=0.} \tag{3.5}
$
特别，若这个最小实见证还恰好反射不变，则其支撑必须完全位于某一个反射奇偶空间。不能先作双重平均，再免费宣布所得见证仍为最小实秩。

R229 的九维实回文幂零例依旧不被排除。其最高空间有实偶维数2、实奇维数1，(3.4) 只给实秩二表示，恰与其已证最小正秩二一致。它不是实际慢理想的真湮灭见证。

## 4. 实最小乘子与 Krein 域等式的范围

若 h 为 J_0 实，原最小闭乘子 $X_h$ 也是 J_0 实。确实在规范核心上
$
 J_0\bigl(p(A)1,p(A)h\bigr)
   =\bigl(\overline p(A)1,\overline p(A)h\bigr),
$
再取图闭包即可；有限柱核心与该多项式核心的等价由 R176 §6 的实际范数逼近支付。

若见证谱向量 f_i 实，则 $Cf_i=\mathcal Rf_i$ 也实，因此 $M_i=X_{Cf_i}$ 满足
$
 J_0\operatorname{Dom}M_i=\operatorname{Dom}M_i,\qquad
 J_0M_i=M_iJ_0.
$
原最小乘子的 C 对称性给
$
 \mathcal R M_i\mathcal R\subseteq M_i^*. \tag{4.1}
$
这只是 Krein 对称性；不能从实化单独删去包含号。

若 M_i 已有 R244 的某个广义预解数据，则有界 C 对称逆
$R_i=(M_iU_i+B_i)^{-1}$ 使 $M_iU_i+B_i$ 本身 C 自伴。
利用有界单位 U_i 的双向域交换，再减去有界 B_i，得到
$M_i=CM_i^*C$。这时 (4.1) 才升级为
$
 \mathcal R M_i\mathcal R=M_i^*. \tag{4.2}
$
它仍是单独算子的整个伴随域等式，并非共同最小图等于各最大域交。

若 U_i、B_i 及 M_i 都实，则相应逆 R_i 实，并满足
$
 R_i^*=\mathcal R R_i\mathcal R.
$
若希望以实 U_i、实 F_i 和实标量 λ_i 来保证 B_i=F_i−λ_iI 实，仍须另外验证该实 λ_i 确在预解集；非空复预解集本身不保证存在实预解点。B_i 实本身也不要求任意已给的 F_i、λ_i 分别实。

## 5. 一般复参数下，商的实结构需要准确权

本节即使 R_i 不实也适用，但要求两个原 M_i 都实。令
$\overline R_i=J_0R_iJ_0$。它是同一 M_i 的共轭广义参数所给预解子。
R244 的参数单位结论给
$
 \overline R_i=R_iW_i,\qquad W_i\in\mathfrak C^\times. \tag{5.1}
$
共轭两次并利用 R_i 单射可得
$
 W_i\overline W_i=I. \tag{5.2}
$

在原分母链
$
 N=\overline{\{(R_2h,R_1h):h\in H\}},\qquad
 K=\{(y_1,y_2):R_1y_1=R_2y_2\},\qquad Q=K\ominus N
$
上，定义有界反线性算子
$
 \Theta(y_1,y_2)=(W_1J_0y_1,W_2J_0y_2). \tag{5.3}
$
(5.2) 给 $\Theta^2=I$。若 y 属于 K，共轭其等式并用 (5.1) 就得 $\Theta y\in K$。对边界则准确有
$
 \Theta(R_2h,R_1h)
   =(R_2W_1W_2J_0h,\ R_1W_1W_2J_0h),
$
所以 $\Theta N=N$。因此它真正诱导商对合
$
 \Theta_Q=P_Q\Theta|_Q,\qquad
 \Theta_Q^2=I,\qquad \Theta_QT=T\Theta_Q,
 \quad T=P_QA^{(2)}|_Q. \tag{5.4}
$
平方等式必须经商验证：第一次投影删去的项在 N，第二次 Θ 仍把它留在 N，因此投影后正好为恒等。一般 Θ 不等距，也未必把正交实现 Q 本身保持；不能删掉 (5.4) 的 P_Q。

这与此前无权的 $J(y_1,y_2)=(Cy_2,-Cy_1)$ 不冲突：J 是交替型的反线性等距，平方为 -I；Θ_Q 是点态实结构的有界反线性对合，平方为 I。它们的功能和类型不同。

## 6. 真正实参数只给无限正负指数的 Krein 型

如果两个 R_i 本身实，则 N、K、Q 都被 $J_0^{(2)}$ 保持。此时上述 Θ_Q 就是其无权限制，且与 J 交换。在 Q 上定义线性酉算子
$
 \mathcal I=J J_0^{(2)},\qquad
 \mathcal I(y_1,y_2)=(\mathcal Ry_2,-\mathcal Ry_1).
$
有 $\mathcal I^2=-I$、$\mathcal I^*=-\mathcal I$，并且
$
 \mathcal I T=T^*\mathcal I.
$
故 $K_{\rm cr}=i\mathcal I$ 是自伴酉对合，满足
$K_{\rm cr}T=T^*K_{\rm cr}$。

这个度量并不正定：J_0 交换 $\mathcal I$ 但反共轭 i，故把 $K_{\rm cr}$ 的正、负特征空间相互等距映射。若 Q 非零，实际多项式强单位已使 Q 无限维；两个特征空间因此都无限维。这不提供有限负指数假设，也不产生共同图核心或真空原像。

一般复参数只保证 §5 的带权有界实结构，不能沿用本节的无权酉公式。把 R_i 与其共轭相乘虽得到实有界交换子，却可能缩小其范围，因而不能自动继续声称范围恰为 $\operatorname{Dom}M_i$。
