# R912：原八维端点格、九范数的相对坐标与完整单位帧

日期：2026-11-16。状态：**以下为有限准确算法及其证明，尚未执行新的端点代数、端点格或端点范数求值。** 本文接已冻结 R907，不修改它的主函数、无基点铅笔、两图范数理想或既成 R885 的整 Artin 纤维。R885 的源 \(z=0\) 纤维并非 \(P_0\) 或 \(P_1\)。

本文的新增对象是原循环七对应在两个指定点上的完整秩八局部代数、其上的两个截面格，以及原行列式纤维的实际首项。局部相消只消去九截面的共同因子，**不删除完整范数帧中的 \(\operatorname{Nm}(q^*\Phi)\)**。所有原 \(\kappa,\rho_j,\sigma(b),p_j,q_j\)、两投影、原 \(-3\) 下降和非 \(p\) 项保持其来源。本文不计算 Picard 活跃支持、Poincaré period 或指定高度。

依赖：

- [R873](../results/R873-original-cyclic-seven-correspondence-from-short-section-norms.md) §4、§6、§10：原八分支、两个固定支和两个长度三轨道、\(P(U)=0\)、\(q^*w=K(U)/P'(U)\) 与 dual-seven。
- [R876](../results/R876-original-nine-norm-generators-and-rigidified-Hecke-ideals.md)：原九范数引理、\(672\) 判据、原 \(M_j/M_0\) 及两端 determinant fibre。
- [R802](../results/R802-original-semilinear-parity-and-degree-seven-relations.md)、[R837](../results/R837-certified-original-P0-evaluation-and-fixed-branch-pencil.md)、[R853](../results/R853-certified-original-three-V1-conjugates-and-semilinear-generators.md)、[R860](../notes/R860-original-adjugate-semilinear-descent-and-rational-differential.md)：原几何反射、原 \(V_1\) 尺度及真正算术共轭的区别。
- [R872](../notes/R872-original-point-jets-and-bounded-two-weight-RR-kernels.md)、[R872 实际结果](../results/R872-certified-original-P0-jets-and-fixed-Picard-spaces.md)、R883：原 \(P_0\) 的已成273系数及 \(t/\rho\) 真首项。
- R885 完整 Artin 结果、R879 原参考函数、R901/R903 原 \(\Phi_j\) 和 R907 的实际输入/完成证书；尚未实际完成的消费者来源保持 null。
- [RF](../notes/2026-11-16-original-c0-rigidified-Poincare-fibres-and-theta-section-DAG.md)：原两点帧；本文不用任意新 CM 常数代替它们。

## 1. 固定原函数与端点对象

记
\[
p=\pi_s:C_7\longrightarrow Y,\qquad q=\pi_t:C_7\longrightarrow Y,
\qquad\deg p=\deg q=8.
\tag{912.1}
\]
方向保持 R873 的“源保留椭圆曲线、靶取循环七商”。原 Hecke 方向 \(\operatorname{Nm}_q p^*\) 经原 dual-seven 同构运输为 \(\operatorname{Nm}_p q^*\)；该同构同时运输 determinant 的分子和分母。

设 \(k\) 是特征零的原系数域，或本次实际合法辅助特征 \(1000000753\) 的原剩余域。若使用一般剩余特征，本篇另要求 \(\operatorname{char}k>16\) 并满足原好约化条件；仅避开 \(2,3,7,41\) 不能代替这个长度条件。有限域首消费仍用原 \(1000000753\)、\(\zeta=549966761\)、\(s=99932770\)，不能将另一嵌入的数组混入。原 \(L\) 系数及七共轭数据按其真实选择运输；不因输出有理数字便擅称整个基已作 \(\mathbf Q\) 下降。

对 \(j=1,\ldots,5\)，沿 R901/R903 原图取
\[
L_j=\mathcal O_Y(-Z_j),\qquad M_j=L_j(254P_0),\qquad
u_j=\Phi_j a_j,\quad v_j=\Phi_j b_j,
\quad \Phi_j=Q_{Z,j}/q_\chi.
\tag{912.2}
\]
\(a_j,b_j\) 是 R907 实际接受的、未再次缩放的原正常 \(V_3\) 列；\(u_j,v_j\) 的完整无基点性须来自真实 \(672\) 证书。参考为 R879 的
\[
M_0=\mathcal O_Y(254P_0),\qquad (u_0,v_0)=(1,v_0).
\tag{912.3}
\]
原 \(v_0\) 的准确比值、单位解及其唯一254阶极点全部原样消费，不重构它。

对 \(\epsilon\in\{0,1\}\)，令 \(P_\epsilon=\phi(c_\epsilon)\)，选下文指定的实际参数 \(\rho_\epsilon\)，并置
\[
R_\epsilon=k[[\rho_\epsilon]],\quad F_\epsilon=k((\rho_\epsilon)),\quad
E_\epsilon=k(C_7)\otimes_{k(Y)}F_\epsilon.
\]
若已作合法剩余域求值，\(E_\epsilon\) 可以是有限可分代数的乘积。令
\[
B_\epsilon=\overline{R_\epsilon}^{\,E_\epsilon},\qquad
A_\epsilon=B_\epsilon/\rho_\epsilon B_\epsilon.
\tag{912.4}
\]
\(B_\epsilon\) 是秩八有限自由 \(R_\epsilon\) 代数，\(A_\epsilon\) 总长度八。所有因子、剩余域和 nilpotent 均保留。

R873 §4 给原椭圆点稳定子在八个循环七子群上的两个固定支和两个长度三轨道。因此在几何剩余域上
\[
A_\epsilon\otimes\bar k
\simeq \bar k\oplus\bar k\oplus
\bar k[\pi]/(\pi^3)\oplus\bar k[\pi]/(\pi^3).
\tag{912.5}
\]
这是结构类型，不是待计算值或分裂标签。实际算法不需要拆出四个点，也不能以四个约化值替代秩八代数。原合法特征避开 \(2,3,7,41\)，这里的局部分歧是 tame；其 discriminant 的参数阶为
\[
v_{\rho_\epsilon}\operatorname{disc}(B_\epsilon/R_\epsilon)
=(3-1)+(3-1)=4.
\tag{912.6}
\]
非拆情形中各剩余次数按原 trace/determinant 自动计入。

## 2. 真正 P1 jets 可从原 P0 jets 运输，但必须先算完整 V1 作用

原几何 involution \(\iota=T^{41}\) 在 \(Y_K\) 上是 \(K\) 线性的，
\[
\iota^*t=1-t,\quad q_Y\longmapsto-q_Y,\quad
\iota^*\tau=\tau,\quad \iota^*w_0=w_0.
\tag{912.7}
\]
它不同于算术共轭 \(c_Y\)：后者还对 \(s\) 及额外系数施加原共轭。原偶权的 \(T^{41}\) automorphy factor 为1。R837 已准确证明 \(P_1=\iota(P_0)\)，但明确没有构造完整146阶反射矩阵；R853 只给三个指定截面。R866 的127维全纯基也不是此146维空间的替代品。

令 \(S\) 为 R837/R853 使用的原 \(560\times146\) Fourier 矩阵，行标为 \(q_Y^n\xi^r\)，\(0\le n\le13\)、\(0\le r<40\)。其列直接是已含整数尺度的
\[
e_i=82^2T_{1,i}.
\]
不得再乘 \(82^2\)。令 \(D\) 是在第 \(n\) 阶40行上取 \((-1)^n\) 的对角矩阵。用一个实际合法的146阶原行子式 \(S_J\) 定义
\[
C_\iota=S_J^{-1}D_JS_J.
\tag{912.8}
\]
实际消费者必须核
\[
SC_\iota=DS,\qquad C_\iota^2=I
\tag{912.9}
\]
及 R853 已成的三列；全560行乘回而非只检查选行。R837 的旧子式行号优先读取；若在当前原剩余处不为单位，另作明确选择，不能照搬另一素数的逆。

(912.8) 同时给原特征零的准确 unit-solve 定义与其合法模求值。反射已经是原几何作用，完整 Fourier 评价单射保证它就是整个 \(V_1\) 上的唯一作用，不是由模矩阵平方为1猜出的新 involution。

原 R872 实际参数是 \(\rho_0=z-z(P_0)\)。定义
\[
\rho_1=\iota^*\rho_0,\qquad
\iota^*z=z-2\beta_{72}.
\tag{912.10}
\]
这是真正 \(P_1\) 参数，不擅自换成 \(z-z(P_1)\)。对原 \(V_1/\tau\) 的行值作右乘 \(C_\iota\)，再按 R805 已成 degree \(0,1,2\) 自由基 recipe 相乘，就得到全部原正常函数在 \(P_1\)、参数 \(\rho_1\) 下的同阶 jets。常数 \(K\) 不共轭；余下 \(L\) 系数按原函数本身保留。

若原 \(P_0\) 数据给
\[
t=c_0\rho_0+O(\rho_0^2),
\]
则精确地
\[
t-1=-c_0\rho_1+O(\rho_1^2).
\tag{912.11}
\]
故 \(c_1=-c_0\)，不需要一个新的 CM 周期或猜测单位。现有 R883 已成 \(c_0=354813668\) 模原素数，准确表达式仍为其原 \(N_{692},N_{693}\) 比值导数。其旧已算首项只读，不能把这个模数当作展开的特征零常数。

R872 的273系数只支持对应的真实截断精度。下面若某个 Laurent 消去损失超出该精度，须沿同一 R872 固定子式追加尚未计算的阶；P1 同步用 (912.8) 运输，不重算已成前缀。

## 3. 从原 P,K 到端点的完整八维整代数

R873 的原准确函数为
\[
P(U)=0,\qquad q^*z=U,\qquad q^*w=K(U)/P'(U).
\tag{912.12}
\]
十七个系数用 R882 的同素点完整2058坐标以及原 R873 的准确单位解定义。其局部展开只消费：

1. 原2050个 \(V_8/\tau^8\) recipe；
2. 原八个 \((\widehat E_6/\tau^3)^2V_2/\tau^2\) 补列；
3. R807 的 \(\widehat E_6/\tau^3=N_{692}/\theta\)，保原各 rational scale；
4. 第2节的源正常 jets。

在两个端点，\(\theta\) 和某些系数可以有零或极。必须作有阶数的 Laurent 除法；R885 的 \(z=0\) 处 theta/P′ 单位记录不运输到这里。R873 的4阶主部界也不授权将 \(a_8=P\) 首项或 \(P'\) 在端点直接置为单位。

先在 \(F_\epsilon[U]\) 中将 \(P\) 除以实际非零首项。取整数 \(h\ge0\)，使 \(\Theta=\rho_\epsilon^hU\) 的全部首一关系系数整，得到
\[
O_\epsilon=R_\epsilon[\Theta]\subset E_\epsilon.
\tag{912.13}
\]
\(h\) 由实际已知系数阶选取，不能预填为0。若某必要首项在已有精度中仍未确定，只输出 NeedPrecision，不将零球/零截断解释为准确零。

下面给一个不拆分支、不先建2176维全局整基的有限正规化算法。设 \(O\) 是当前秩八整 order，已保其完整乘法及1。

### 3.1 trace radical 只需八维剩余代数

令
\[
J/\rho O=\ker\!\left(
O/\rho O\longrightarrow\operatorname{Hom}_k(O/\rho O,k),
\ x\longmapsto(y\mapsto\operatorname{Tr}(xy))\right).
\tag{912.14}
\]
在本篇明确规定的特征零或特征大于16中，每个局部因子的长度最多8且非零于 \(k\)，剩余域可分。因此 trace pairing 的核恰为 \(O/\rho O\) 的 nilradical；故
\[
J=\sqrt{\rho O}=O\cap\operatorname{rad}(\rho B).
\tag{912.15}
\]
不能用 trace 的秩直接丢掉 nilpotent；此处正是利用它确定应扩大 order 的格。

取
\[
O'=(J:J)=\{x\in E_\epsilon:xJ\subset J\}.
\tag{912.16}
\]
它仍是 \(R_\epsilon\) 上有限的整 order，并且
\[
O\subseteq O'\subseteq B_\epsilon,\qquad O'\subseteq\rho^{-1}O.
\tag{912.17}
\]
最后一个包含来自 \(\rho\in J\) 及 \(\rho x\in J\subset O\)。整性来自 \(x\) 在自由格 \(J\) 上的乘法特征多项式。

若 \(O\ne B_\epsilon\)，有限长模 \(B_\epsilon/O\) 有非零 \(J\)-socle。取其代表 \(x\in B_\epsilon\setminus O\)，使 \(xJ\subset O\)。又因 \(x\) 整、\(J\subset\operatorname{rad}(\rho B)\)，有 \(xJ\subset O\cap\operatorname{rad}(\rho B)=J\)。所以 \(x\in O'\setminus O\)。因此每个未正规阶段都严格扩大。

### 3.2 每次扩大是一个有限小核

按 (912.17)，只须找 \(v\in O/\rho O\)，使 \(\rho^{-1}vJ\subset J\)。用实际 trace-kernel 的常数列和补列写
\[
J=C\operatorname{diag}(1,\ldots,1,\rho,\ldots,\rho)R_\epsilon^8,
\quad C\in\mathrm{GL}_8(k).
\]
对 \(J\) 的八个生成元，条件是 \(vJ\subset\rho J\)。它只使用当前乘法表的第0、1阶系数，形成一个 \(k\)-线性核。任何两个 v 的 lift 相差 \(\rho O\)，而 O 保持 J，故条件与 lift 无关。

保存该核、真实选行/自由列、基变换及完整乘回。用其独立 r 个方向将格扩大 r 阶，则 trace discriminant 的阶降低 \(2r\)。从原首一 order 的实际 discriminant 阶 d 开始，结合 (912.6)，最多 \((d-4)/2\) 次单维扩大即到 \(B_\epsilon\)。当阶为4，order 与 \(B_\epsilon\) 的 index 长度为0，故相等。该停止证书以完整整乘法、1、来源关系及 discriminant 阶共同认证；不把一个猜测的8次剩余多项式称为正规化。

若某次所需第1阶因先前除 \(\rho\) 已超出实际精度，则保存当前格和全部损失并请求新尾。旧已成 order 变换可直接复用，不重复其核。这个算法在特征零给准确有限线性定义，在合法辅助剩余处给实际矩阵；两种字段保持区别。

## 4. 靶正常坐标不能从旧 z=0 数组挪来

端点中依然要评价原目标函数，不只是源函数。优先消费 R885 已完成的全局 adjugate 多项式行
\[
r(z,T)=e_0^{\mathsf T}\operatorname{adj}(TI-W(z)).
\]
代入 (912.12)，令
\[
\gamma_i=r_i(U,q^*w),\qquad
q^*\beta_i=\gamma_i/\gamma_0.
\tag{912.18}
\]
\(\gamma_0\) 在每个 generic 完成分支非零，故在 \(E_\epsilon\) 中可逆，但它在 \(A_\epsilon\) 中可以为零因子。应在有精度的 Laurent 八维代数中求逆，再作完整272关系与 \(\beta_0=1\) 乘回；不强制要求它在特殊纤维是单位。

这直接复用 R885 真 global row levels 与原 \(W\)，不重新算 charpoly、adjugate 或原整272 Krylov 逆。若首实现选择新的271 RHS 求解，则必须清楚记录其为新的端点求值，不能冒称旧 \(z=0\) 的目标行已给这两个点。

每个原正常函数按其既有 \(z\)-多项式和真实 \(\epsilon_i\) 权展开后代入 (912.18)。全局 \(\Phi_j\) 则严格沿 R907 已固定图求值；负幂在 \(E_\epsilon\) 求逆，精度/极点通过整图传播。没有新的 \(\rho_j\)、\(\sigma\) 次序或目标相位选择。

## 5. 两个截面格消去公共 Φ，保留完整极点

以下固定一个端点，略去 \(\epsilon\)。将 \(q^*a_j,q^*b_j\) 简记为 a,b。置
\[
J_j=aB+bB\subset E.
\tag{912.19}
\]
这是原两个函数生成的完整分式 \(B\)-理想。因为 B 是半局部 DVR 的乘积，它可逆且在 B 上自由秩一；作为 R 格则自由秩八。它允许零、极及二者在各分支的不同阶数。

选一个有完整来源的 R-基矩阵 \(U_j\)，其列在已成 B 基中表示 \(J_j\)。令 \(M_a,M_b\) 为在同一 B 基中的乘法矩阵。定义
\[
C_{j,0}=U_j^{-1}M_a,\qquad
C_{j,1}=U_j^{-1}M_b.
\tag{912.20}
\]
两矩阵全部属于 \(M_8(R)\)，因为 aB、bB 包含于 \(J_j\)。实际需要核完整 \(8\times16\) 格的双向包含以及 (912.20)，不只核某个选定子式。

对参考同样取
\[
J_0=B+q^*v_0B,\quad
C_{0,0}=U_0^{-1}I,\quad C_{0,1}=U_0^{-1}M_{q^*v_0}.
\tag{912.21}
\]
原 \(v_0\) 的极点不能先约成纤维里的无穷数；(912.21) 正是其完整局部格。

R 上的格计算可用 \(8\times16\) Laurent 矩阵的列 Hermite/Smith 消元：先乘一个实际足够的 \(\rho\) 幂清极，再只除已确定的参数幂或单位。必须保存八个基列的准确线性表达、全部16列在新基中的系数及反向表达。消去的只是格表示的公共极点，没有改变原函数的标量。

由于 \(u_j,v_j\) 对 \(M_j\) 无基点，
\[
q^*M_j=(q^*\Phi_j)J_j
\tag{912.22}
\]
是全部对应上的准确嵌入理想；这里不是只在某个稠密开集相等。实际672证书是使用这条等式及下文九单位选择的必需来源。

## 6. 九个实际相对坐标只需两矩阵模参数

定义
\[
c_{j,i}=\det(\overline C_{j,0}+i\,\overline C_{j,1})\in k,
\qquad i=0,\ldots,8.
\tag{912.23}
\]
它们是九个 norm sections 在基
\[
\det\bigl(M_{q^*\Phi_j}U_j\bigr)\otimes\det(B)^{-1}
\]
中的真实纤维坐标。若 \(c_{j,\lambda}\ne0\)，相对于该单位铅笔帧的九坐标为
\[
\boxed{\qquad c_{j,i}/c_{j,\lambda}.\qquad}
\tag{912.24}
\]
(912.24) 中 \(\Phi_j\) 相消，因而本阶段不需要其在特殊纤维可逆；它甚至可以在某些分支有极点。此相消不适用于完整范数帧。

九范数引理保证至少一个 \(i\in\{0,\ldots,8\}\) 的值非零。它依靠完整线丛无基点性，不要求 a,b 中某一个函数在 A 为单位。坐标 (912.23) 由整8阶矩阵给出，自动包含两个长度三轨道的重数、未拆剩余域和 nilpotent；不把四个闭点的未加权乘积当作行列式。

如改变 R 格基 \(U_j\mapsto U_jS\)，\(S\in\mathrm{GL}_8(R)\)，则全部 c 同乘 \(\det\bar S^{-1}\)，故 (912.24) 不变。实际输出仍保 U 的标量，以供完整帧比较。

可从同一个次数至多8的多项式
\[
c_j(T)=\det(\overline C_{j,0}+T\overline C_{j,1})
\tag{912.25}
\]
同时评价两个端点。每个端点最多排除8个参数；所以在原特征大于16时，\(\lambda=0,\ldots,16\) 中至少一个使两个端点的 \(c_j(\lambda)\) 都非零。这个共同单位帧仅是同一八次多项式的新标量评价，**不重算17个全局域范数**；R907 的原九生成元仍完整不变。参考 \(\lambda_0\) 同理。

## 7. 完整帧绝不能省去 Norm Φ 或参考

在同一 B 基内，原范数商线丛的局部理想为
\[
\operatorname{Nm}_p(q^*L_j)
=\Gamma_{j,\epsilon}R_\epsilon,
\]
其中
\[
\boxed{\quad
\Gamma_{j,\epsilon}
=\operatorname{Nm}_{E_\epsilon/F_\epsilon}(q^*\Phi_j)
  \frac{\det U_{j,\epsilon}}{\det U_{0,\epsilon}}.\quad}
\tag{912.26}
\]
此处参考 \(M_0\) 的移动因子按 R876 准确取消，不能删除 \(\det U_0\)；范数是 \(\Phi_j\) 的正乘，不取倒数。改变 B 的基对分子、分母同时作用并抵消；改变 \(J_j,J_0\) 的格基则与其纤维坐标相反作用，整体不变。

令
\[
m_{j,\epsilon}=v_{\rho_\epsilon}\Gamma_{j,\epsilon},\qquad
g_{j,\epsilon}=
[\rho_\epsilon^0](\rho_\epsilon^{-m_{j,\epsilon}}\Gamma_{j,\epsilon})\ne0.
\tag{912.27}
\]
这些是新的实际局部整数与未缩放单位，不由旧 \(Z_j(P_0)\) 系数猜出。Hecke 后的负、正支撑都可能经过两个端点或对应靶点；R901 的负支撑不只 \(P_0\)。

原参数记 \(t_\epsilon=t-\epsilon\)。由 (912.11)，\(\,t_\epsilon=c_\epsilon\rho_\epsilon+\cdots\)，故同一准确单位在原 \(t_\epsilon^{m_{j,\epsilon}}\) 帧中为
\[
\boxed{\quad g^{\,t}_{j,\epsilon}
=c_\epsilon^{-m_{j,\epsilon}}g_{j,\epsilon},
\qquad c_1=-c_0.\quad}
\tag{912.28}
\]
负阶时这是原 c 的正幂，不能倒置。

若在两端选出 §6 的共同参数 \(\lambda_j,\lambda_0\)，原同一全局函数
\[
G_j=
\frac{\operatorname{Nm}_p(q^*(u_j+\lambda_jv_j))}
     {\operatorname{Nm}_p(q^*(1+\lambda_0v_0))}
\tag{912.29}
\]
在两个端点均生成原范数商理想。其原帧首项为
\[
\operatorname{LC}_{t_\epsilon}(G_j)
=g^t_{j,\epsilon}
 \frac{c_{j,\epsilon}(\lambda_j)}
      {c_{0,\epsilon}(\lambda_0)}.
\tag{912.30}
\]
因此两端所选 determinant generators 的完整单位比较是
\[
\frac{\operatorname{LC}_{t_1}(G_j)}
     {\operatorname{LC}_{t_0}(G_j)}.
\tag{912.31}
\]
这条式子必须保 (912.26) 的全部原叶；仅 (912.24) 的九坐标不能确定它。

## 8. 原 RF 帧和 dual-seven 的实际运输边界

输入 \(L_j\) 原点帧是
\[
e_{j,0}=t^{-7(p_j-q_j)},\qquad e_{j,1}=1,
\]
而 \(M_j,M_0\) 的原帧分别为
\[
t^{-7(p_j-q_j)-254},\qquad t^{-254}.
\tag{912.32}
\]
P1 帧1的合法性沿 RF/R843 原 Hom 非挠，不能移作所有循环七靶点都避开极除子的证明。

(912.20)–(912.31) 计算的是原完整 fractional-ideal / determinant-fibre 的单位转移。若下游使用所选铅笔 generator 作帧，应同时保它与原输入 (912.32)、原全局 \(\Phi_j\) 和移动参考的同构。不能因为两端已得一个非零比值，就宣布它是未经运输的 RF 点，或设任一 \(\kappa_j,\rho_j\)、theta 二挠或非 \(p\) 常数为1。

原 dual-seven 的 determinant 自然同构同时作用于 \(\det(p_*q^*L)\) 和 \(\det(p_*\mathcal O)\)，故不存在额外基排列符号。标量 \(7I\)、原 \(-3\) 下降和两个端点的运输沿 R873/R876 的已证精确同构保留；本次不重新证明或重算它们。实际证书应保存原 transport 节点以及 (912.26)–(912.31) 的数值，不只写“自伴”。

本篇输出完整的原端点 fibre、chosen-generator 与原单项式帧的准确比较。后继若要与另一个指定 theta/Poincaré frame 比较，仍须消费那个真实同构；此处没有以范数线丛的某个新生成函数替代指定高度规范。

## 9. 精度：没有把零截断当零函数的出口

所有局部运算保绝对 \(\rho_\epsilon\)-精度和实际可确定的最低阶。若 \(f\) 的非零首项在阶 v、已知到绝对精度 N，则 \(f^{-1}\) 只保证到 \(N-2v\)；加法取精度最小值，乘法按双方真实最低阶传递。准确结构零与未确定的零截断必须分开。

原 \(P,K\) 首项、primitive 分母、格 pivot、trace discriminant、\(\Phi_j\) 的每个负幂及 (912.27) 的单位，都只有在当前精度实际足够时才能消费。停止条件包括：

- 全八维整乘法及 discrim 阶4已认证；
- \(J_j,J_0\) 的全 \(8\times16\) 双向格等式；
- (912.20) 的两矩阵至少准确到第0阶；
- 选定 determinant 单位真实非零；
- \(\Gamma\) 的实际阶及其单位首项已经确定；
- 原 \(t/\rho\) 单位及全部 source/SHA 对齐。

若缺任何一项，保存当前实际对象、发生损失的节点和需要的绝对精度，返回 NeedPrecision；不标 false 的数学结论，不据此排除原支持或高度。新尾仅由同一准确 R872 解追加；已成273项、已有正常函数/多项式和旧范数运算都不重复。

特征零准确对象来自已认证原函数域与 unit-solve 叶；辅助素点上的数值只是它们在合法处的实际求值。端点 determinant 为零并不能推出特征零 Picard inactive，非零单位也不等于高度非零。

## 10. 最小来源闭包与可执行阶段

| 阶段 | 直接旧源 | 真正新增 |
|---|---|---|
| P0 基础 | R872 273正常 jets、旧点/子式；R883 原 c | 不重原 jets 或 c |
| P1 运输 | R837/R853 原560×146行、R805 degree≤2自由基、R802作用 | 完整146 RHS及全560乘回；同阶P1 jets |
| 17局部系数 | R882 2058×17同素点坐标；R873完整recipes；R807 theta/N692 | 两端的 Laurent 系数，原scale一次 |
| 八维正规 order | 原P/K关系及真实2+3+3来源 | trace-radical/idealizer小核、完整乘法及阶4证书 |
| 靶正常值 | R885既成global adjugate row levels、原W | 两端代入及全272关系；不搬z0数值 |
| 相对九坐标 | R907接受的两真实列及672证书；R879参考原比值 | 两个8维格、两矩阵、九实际坐标 |
| 完整单位帧 | R907原Φ全source closure、原参考/dual7/RF | NmΦ、det格比、原t首项和两端比值 |

R907 当前公共 consumer 的 endpoint_P0_values_computed 与 endpoint_P1_values_computed 均为 false。本篇不会因为 (912.26) 已写为准确表达式便修改它们。R903/R907 未完成的源仍为 null；几何前半段可以先在独立 scope 完成，但只能声明实际已计算的端点代数，不能声明五个端点范数已成。

建议每个端点单独保存原子阶段：source-jets、V1-involution、seventeen-Laurent-coefficients、order-000...、normal-order、target-normal-row；每方向/参考再保存 pencil-lattice、two-fibre-matrices、nine-coordinates、marked-frame-Laurent-leading。未完成 current 与完成阶段分开。最终字段逐项给 actual 精度、实际阶、原 unit-solve/source、完整乘回及真实 unit；不以一个 complete 总旗标掩盖未求值的端点。

以上仅代码/证明与简明来源可入 Git。全部新矩阵、形式系数、局部格、完整剩余代数及机器回执只在公开 Actions 的一日 artifact 中续传。本地不执行任何新数学。

