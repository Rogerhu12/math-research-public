# R590：完整第三历史的最高平方势与 C² 更新

日期：2026-11-26。**已证明以下完整原式身份与可逆状态变换**。原式纸证；没有执行新的符号程序、求积、ODE、优化或秩计算。

本稿承接 R581、R584、R586，并回应完整十九态首跑中真实的巨大第三历史读出。完整中心化第三导数的最高空间三阶平方项并不恒为零。新的准确结论是：它恰为一个显式当前状态势的全时间导数。用这个势作可逆坐标变换后，全部六个第三更新都可按原空间分部积分化为 C² 表达；相应非负平方必须完整回付原 ruling，不能因它大而丢掉。

本稿没有把新坐标称作已经温和或已经求根；原物理输入、固定规范、真实历史、加速度方程和端点义务全部保留。

## 1. 固定原块、原尾与最高空间变量

沿 R586 的同一个实际 R578 库。一个未旋转微包内令
\[
u=\rho,\quad p=\rho',\quad r=\rho'',\quad \mathsf t=\rho''',
\qquad f=\alpha u,\quad g=\beta u,\quad \alpha\beta=0.
\]
令
\[
D=\alpha^2-\beta^2,\qquad C=\alpha\sin\vartheta+\beta\cos\vartheta.
\]
D 为该微包的原差系数；C 是旋转后 g 的系数。整块二尾仍是 R586 的
\(J_0,J_1,J_2\)，不按微包重置。所有形式恒等在微包上计算，原全平支撑端保证各次分部积分可以按真实整块拼合。

原八维算子作用在缺陷上的 profile 写为
\[
q_A=a_0Du^2+a_1Dup+a_2Dp^2+b_0J_0+b_1J_1+b_2J_2.
\tag{1}
\]
这里 \(a_i=a_i(A;y),b_i=b_i(A;y)\) 是原 E8 固定坐标的多项式，全部对 A 一次。定义
\[
C_A(y)=b_0+yb_1+y^2b_2,\qquad
\boxed{H_A=a_1u+2a_2p-2C_A r.}
\tag{2}
\]
原尾微分给
\[
(q_A)_{yy}=DH_A\mathsf t+\text{不含 }\mathsf t\text{ 的项}.
\tag{3}
\]
因为固定 y 坐标中的 E8 基不随几何移动，真实 \(A_s=M\) 直接给
\[
\boxed{(H_A)_s=H_M.}
\tag{4}
\]
这里的 \(D_s\) 始终保真实 \(A_s=M\)，不是只微分几何系数。

几何记号为
\[
z=y+\eta,\quad e=hz-k,\quad Q=1+e^2,\quad
e_s=\gamma z-\upsilon/2,\quad q_g=1+(h\eta-k)^2,
\]
\[
Z=\gamma p-e_s r,\qquad
\boxed{F_0=\frac{QZ}{8h^3}.}
\tag{5}
\]
F0 对真实速度一次，H_A 对 A 一次；两者都不含加速度和 \(\mathsf t\)。

下文 \([P]_2\) 表示关于 \(\mathsf t\) 的二次系数。R586 的所有转置后完整读出至多二次依赖 \(\mathsf t\)：每个一阶分子至多一次，\((q_A)_{yy}\) 至多一次，第三测试原函数也至多一次。不存在未保留的更高幂。

## 2. 有序 B、Gram 与 L 的最高项

R586 的准确六元平均在本记号下为
\[
\overline{D^2}=\tfrac12D^2,\qquad
\overline{C^2D}=-\tfrac14D^2.
\tag{6}
\]
左边 D 指旋转时相应二次槽的系数；右边 D 为未旋转块的固定原差。下文所有横线都指该精确平均，不是浮点三角求和。

### 2.1 原有序 B 和 G/2

R586 的原转置式给
\[
[B_j[M,A]]_2
=-\tfrac12 y^j C^2D\,H_MH_A.
\tag{7}
\]
为核对次序与系数：局部部分的最高项是
\(-y^j C^2D(a_1(M)u/2+a_2(M)p)H_A\)；三条真尾给
\(y^j C^2D C_M rH_A\)。两者之和即 (7)，没有先把 M/A 对称化。

同一原 Gram 为
\[
[G_j[M,A]]_2=y^jD^2H_MH_A.
\tag{8}
\]
\(j=2\) 时额外的一阶项不含 \(\mathsf t^2\)，但在后续低阶部分完整保留。由 (6)，
\[
\boxed{\left[-\overline B_j+\tfrac12\overline G_j\right]_2
=\frac18D^2y^jH_MH_A
=D_s\!\left(\frac1{16}D^2y^jH_A^2\right).}
\tag{9}
\]

### 2.2 速度线性项 L

R586 使用 R221 的完整
\(\mathscr L=2T(q_A;\Delta)-4T(g;g,q_A)\)。
设其中两个明确二次多项式为
\[
H_1=D\{Q^2(2\gamma pr-e_s r^2)-2h\gamma eQp^2\},
\]
\[
H_2=D\{(\gamma Q-2he e_s)r^2-2h^2\gamma p^2\}.
\]
有
\[
\partial_rH_1=2DQ^2Z.
\]
因此第一个配对的最高项来自
\(-(q_A)_{yy}D_yH_1/(32h^4)\)，第二个来自 R221 原三线性式的第一项。合并后准确是
\[
[\mathscr L]_2
=-\frac{(D^2+C^2D)Q^2ZH_A}{8h^4}.
\tag{10}
\]
平均得
\[
\boxed{[\overline{\mathscr L}]_2
=-\frac{D^2Q^2ZH_A}{32h^4}
=-\frac{D^2QF_0H_A}{4h}.}
\tag{11}
\]
特别这个最高项通常非零。因为 \(4w_0=q_g/h\)，
\[
\boxed{\left[\frac{\overline{\mathscr L}}{4w_0}\right]_2
=-\frac{D^2QF_0H_A}{4q_g}.}
\tag{12}
\]

## 3. 完整局部第三源 c：chain 恰好是必需的抵消

这里必须使用 R586 的全部局部 C 与 R73 原 chain；单独局部恢复项不满足下面的恒等式。

写
\[
\kappa=kz^2-\frac{k^2+1}{h}z,\quad
U_0=he\,u-\frac Q2p,\quad U_1=he\,p-Qr,\quad
Z_0=\gamma u-\frac{e_s}2p,\quad F=DF_0.
\tag{13}
\]
由 R581 的原 \(\eta_\Delta\) 公式直接微分，
\[
\partial_r\eta_\Delta=\frac{DQZ}{8h^2}=hF.
\tag{14}
\]
R586 中 \(\mathcal T=Y_1\cdot K_1\)、
\(\mathcal W=\nabla_sY_1\cdot K_1+Y_1\cdot\nabla_sK_1\) 的一次系数因此为
\[
[\mathcal T]_1=\frac C2FU_1,\qquad
[\mathcal W]_1=\frac C2D_s(FU_1).
\tag{15}
\]
第二式也直接来自点积的真实全导数；协变连接的两项因反对称性抵消，并未省去加速度。

R586 的 \(C_{\rm loc}\) 不含 \(\mathsf t\)。按其全部原项微分，有
\[
\begin{aligned}
\partial_r C_{\rm loc}
=C\bigg\{&
\frac z2\left(u-\frac z2p\right)F
+\frac{Z_0}{2h^2}D_s(eF)
+\frac{\kappa}{2hz}U_0F\\
&-\frac{\gamma}{2h^3}D_s(U_0F)
+\frac{\gamma^2}{2h^4}U_0F
+\frac{\gamma QpD}{8h^3}H_M
\bigg\}.
\end{aligned}
\tag{16}
\]
其中最后一项来自完整 chain 中的
\(\gamma Qg'(q_M)'/(8h^3)\)；
另一个 \(-\mu g'q_M/4\) 项的 \(\partial_r\) 为零，因为 (1)本身不含 r，所有二尾作为原独立形式变量保留。这不表示其低阶导数被删掉。

为给出 (16)的直接向量核对，原分子满足
\[
\nabla_s(Y_0/C)=
\left(0,h(u-zp/2),Z_0\right).
\]
\(\partial_rK_0=(F,0,eF)\)，所以
\[
\partial_r(\nabla_sY_0\cdot\nabla_sK_0)
=C\{h^2z(u-zp/2)F+Z_0D_s(eF)\}.
\]
同时 \(\partial_r(Y_0\cdot K_0)=CU_0F\)。逐项代入 R586 的 \(C_{\rm loc}\) 即 (16)。

测试原函数 \(P_j[a]\) 的一次系数是 \(y^jaC\)。故 c 的最高项由
\[
-y^jC\,\partial_rC_{\rm loc}
+y^ja_TC[\mathcal T]_1
+y^ja_WC[\mathcal W]_1
+y^ja_JQC^2DrH_M
\tag{17}
\]
给出，其中
\[
a_T=\frac{\kappa}{2h}+\frac{\gamma e_s}{2h^4},\quad
a_W=-\frac{e_s}{2h^3},\quad a_J=\frac{e_s}{8h^3}.
\]
(16)最后一项与 (17)最后一项合成
\(-y^jC^2FH_M\)。

其余部分按 \(F_s,F\) 收集。\(F_s\) 的系数准确为
\[
\frac{-2heZ_0+2\gamma U_0-e_sU_1}{4h^3}
=-\frac{QZ}{4h^3}=-2F_0.
\tag{18}
\]
F 的系数准确为 \(H_M\)。这里可以不靠未展开的“直接计算”：由 R73(4)–(7)，
\[
\boxed{
H_M=\frac Q{4h}(-2ku+\kappa_y p-\kappa r)
+\frac{(\gamma Q-2he e_s)Z}{4h^4}.}
\tag{19}
\]
(17)中不含速度的 F 系数用
\[
z+e\kappa/z=kQ/h,\qquad
z^2+e\kappa+\kappa Q/(hz)=\kappa_yQ/h
\]
分别给 (19)的 u、p、r 系数；含速度部分的 u 系数抵消，p、r 系数分别为
\[
\frac{\gamma^2Q}{4h^4}-\frac{\gamma e e_s}{2h^3},
\qquad
-\frac{\gamma e_sQ}{4h^4}+\frac{e e_s^2}{2h^3},
\]
恰为 (19)后一项。

所以这个 \(+FH_M\) 与原 chain 的 \(-FH_M\) 正好相消，得到
\[
[c_j]_2=-2y^jC^2DF_0(F_0)_s
=-y^jC^2D\,D_s(F_0^2).
\]
精确平均后，
\[
\boxed{[\overline c_j]_2
=\frac14D^2y^jD_s(F_0^2).}
\tag{20}
\]
这是保全部 a/b 与原 M 的全导数恒等式，不是冻结状态或略去 chain 后的形式观察。

## 4. 整个最高项的状态势

R584 的完整中心化历史导数是
\[
\mathcal H_j
=c_j-B_j[M,A]+\tfrac12G_j[M,A]
-\delta_{j0}D_s(\mathscr L/(4w_0)).
\tag{21}
\]
由 (9)(12)(20)，精确平均后的被积式满足
\[
\boxed{[\overline{\mathcal H}_j]_2=D_s e_j,}
\]
\[
\boxed{
e_j=D^2\left\{
y^j\left(\frac{F_0^2}{4}+\frac{H_A^2}{16}\right)
+\delta_{j0}\frac{QF_0H_A}{4q_g}
\right\}.}
\tag{22}
\]

令 \(\mathfrak I\) 表示 R586 的完整参考积分：对六个参考位置的全部完整块作正权积分，再乘6；它准确等于同一36块物理库的精确角平均。定义真实三维状态势
\[
\boxed{\mathcal E_j(S,v,A)=\mathfrak I[e_j\,\mathsf t^2].}
\tag{23}
\]
所有 profiles、幅、位置、右锚均固定。因而
\[
D_s\mathcal E_j=\mathfrak I[(D_se_j)\mathsf t^2].
\]
这里没有新的任意第三 profile，也没有沿路径选择规范；\(\mathcal E\) 是明确的当前状态函数。

### 一个可供精确编译的无分母身份

设 R586 的完整形式分子是
\(\mathcal N_j=q_g^2\overline{\mathcal H}_j\)。令
\[
K_j=q_ge_j
=D^2\left\{
q_gy^j\left(\frac{F_0^2}{4}+\frac{H_A^2}{16}\right)
+\delta_{j0}\frac{QF_0H_A}{4}
\right\}.
\]
这是关于 h 的有限 Laurent 多项式。于是
\[
\boxed{[\mathcal N_j]_2
=q_gD_sK_j-(q_g)_sK_j.}
\tag{24}
\]
(24)可在公开 Actions 的原 Fraction 编译中逐系数核验，不需要除一个几何多项式，也不依赖数值拟合。

## 5. 支付状态势后，完整更新确可降到 C²

写
\[
\mathcal N_j=N_{j,2}\mathsf t^2+N_{j,1}\mathsf t+N_{j,0}.
\]
所有 \(N_{j,l}\) 都只读 \((y,u,p,r,J_0,J_1,J_2)\)、几何、原 A 与实际 a/b。由 (24)，
\[
\mathcal H_j-D_s\mathcal E_j
=\frac1{q_g^2}\mathfrak I[N_{j,0}+N_{j,1}\mathsf t].
\]
定义
\[
\mathcal P_j(y,u,p,r,J)=\int_0^rN_{j,1}(y,u,p,\xi,J)\,d\xi,
\]
以及保原尾的
\[
D_0=\partial_y+p\partial_u+r\partial_p
-Dr^2\partial_{J_0}-yDr^2\partial_{J_1}
-D(y^2r^2+2p^2)\partial_{J_2}.
\tag{25}
\]
于是 \(\partial_y\mathcal P_j=D_0\mathcal P_j+\mathsf tN_{j,1}\)。每个微包两端 r=0，\(\mathcal P_j=0\)，原全平 jets 使拼接合法；在间隙 r=p=u=0，该原函数同样为零。整个真块的边界项准确为零，不依赖把二尾重新置零。

因此
\[
\boxed{
\mathcal H_j^{(2)}
:=\mathcal H_j-D_s\mathcal E_j
=\frac1{q_g^2}\mathfrak I
\left[N_{j,0}-D_0\mathcal P_j\right].}
\tag{26}
\]
这是真正完整第三更新的 C² 表达。先对 r 取原函数，再用 D0，次序不可交换。\(j=2\) 的额外一阶项、全局历史 A、原有序 B 和全部 chain 仍在低阶部分中。

(26)没有把原完整物理方程都说成只需 C² profiles：下面 ruling 保留一个真实、通常非零的 C³ 能量平方。新结论是把这个最高项从历史导数准确转成可读的状态势，同时将余下全部更新稳定地转置到 C²。

## 6. 同一个十九态系统的可逆改写

对一条实际候选，R584 原共同中心为
\[
S_{\rm c}=(H,0,0),\quad v_{\rm c}=(0,v_0),\quad A_{\rm c}=A_{\rm o},
\]
并令
\[
\mathcal E_{\rm c}=\mathcal E(S_{\rm c},v_{\rm c},A_{\rm o}).
\tag{27}
\]
正负两侧在这个中心的实际状态完全相同，因此这个三向量是两侧共用的同一个值。它不含 a/b 或原 \(\nu\)。

定义
\[
\boxed{\rho_\pm=\sigma_\pm-\mathcal E(S_\pm,v_\pm,A_\pm)
+\mathcal E_{\rm c},\qquad
\widehat\nu=\bar\nu-2\mathcal E_{\rm c}.}
\tag{28}
\]
在原 \(r_{\rm c}\) 定义下，实际固定参数是
\[
\boxed{\nu=\widehat\nu-2r_{\rm c}+2\mathcal E_{\rm c}.}
\tag{29}
\]
对固定几何和 A，sigma 到 rho 是平移；其逆由 (28)直接给。中心射击参数的变换
\[
(v_0,A_{\rm o},\nu)\mapsto
(v_0,A_{\rm o},\widehat\nu
=\nu+2r_{\rm c}-2\mathcal E_{\rm c})
\]
仍为对角 \(I_5,I_3\) 的三角变换，行列式1。若 H 也自由，保它在前块即可。这个坐标行列式不是实际端图 rank。

原中心条件准确变成
\[
\rho_+(0)=\rho_-(0)=0.
\]
更新为
\[
\boxed{
(\rho_+)_s=\mathcal H^{(2)}(S_+,v_+,a,b,A),\qquad
(\rho_-)_s=-\mathcal H^{(2)}(S_-,v_-,a,-b,JA).}
\tag{30}
\]
负侧的整个号来自真实时间反向：
\((\mathcal E_-)_s=-(D_s\mathcal E)(S_-,v_-,a,-b,JA)\)。
不能只对原有序项或势中的某一项改号。

## 7. 原 ruling 必须回付的非负平方

R584 的完整 ruling 在 (28)后准确是
\[
\boxed{
\mathscr K_\pm=\mathscr R_\pm
-4w_\pm\cdot\rho_\pm
-4w_\pm\cdot\mathcal E(S_\pm,v_\pm,A_\pm)
-2w_\pm\cdot\widehat\nu.}
\tag{31}
\]
特别不能把它改成只剩 \(\mathscr R-4w\rho-2w\widehat\nu\)。

由于
\[
\sum_{j=0}^2w_jy^j=\frac Q{4h},\qquad w_0=\frac{q_g}{4h},
\]
(22)给出准确平方
\[
\boxed{
w(S)\cdot\mathcal E(S,v,A)
=\mathfrak I\left[
\frac{D^2\mathsf t^2Q}{64h}(H_A+2F_0)^2
\right]\ge0.}
\tag{32}
\]
这里所有实际副本权都为正。当前 ruling 中此项的贡献为该平方的 \(-4\) 倍。它不含加速度，所以原两侧 Ch/Ck 系数和正行列式仍完全不变；唯一 Cramer 输出必须以 (31)的新完整右侧求得。

若保 \(\bar\nu\) 而不使用 \(\widehat\nu\)，也可把 (31)等价地写为
\[
\mathscr R_\pm-4w_\pm\cdot\rho_\pm
-4w_\pm\cdot(\mathcal E_\pm-\mathcal E_{\rm c})
-2w_\pm\cdot\bar\nu.
\tag{33}
\]
这仅是同一固定中心常数的记法；任何数值预条件都必须保该差的全部读出。

在原微包幅按 \(\delta^{7/4}\) 选择时，\(\mathsf t^2r^2\) 的整包积分具有
\(\delta^7\delta^{-10}\delta=\delta^{-2}\) 尺度。F0 和 H_A 都一般含有 r 项，所以 (32)通常确有这个真实高尺度。这个判断来自显式非负原项，不是把首跑的大 probe 自动归因为求积误差。某些状态的相应系数可能消失；本稿不声称每一个状态或每条解都具有非零首项。

## 8. 真实末端、规范和反射条件

在任意末端，从新状态恢复
\[
\sigma_\pm=\rho_\pm+\mathcal E_\pm-\mathcal E_{\rm c},
\]
\[
t_\pm=\rho_\pm+\mathcal E_\pm-\mathcal E_{\rm c}
-r(S_\pm,v_\pm,A_\pm)+r_{\rm c}.
\tag{34}
\]
若原八矩目标 \(A_\pm(L)=0\) 成立，则 r 的末值为0。因此完整第三总响应的三个投影是
\[
\boxed{
t_+(L)-t_-(L)
=\rho_+(L)-\rho_-(L)+\mathcal E_+(L)-\mathcal E_-(L).}
\tag{35}
\]
最终从真实左端重锚后的第三 Gram 参数为
\[
\boxed{\nu+2t_-(L)
=\widehat\nu+2\rho_-(L)+2\mathcal E_-(L).}
\tag{36}
\]
只到八矩根时，不得漏掉这两个末势项。

若进一步满足 R589 的真实末速度
\(\gamma(L)=\upsilon(L)=0\)，则 \(F_0=0\)、\(H_A=0\)，故
\[
\mathcal E_\pm(L)=0.
\]
这时 (35)(36)才分别简化为
\(\rho_+(L)-\rho_-(L)\) 和
\(\widehat\nu+2\rho_-(L)\)。

(22)还表明 \(\mathcal E(S,-v,-A)=\mathcal E(S,v,A)\)。
因此 R589 的自主反射在新坐标中仍是
\[
(S,v,A,\rho_+,\rho_-)\mapsto(S,-v,-A,\rho_+,\rho_-).
\]
同一实际 A=0 和零速度端仍授全部偶 germs，不必另铺未结账尾段。R589 的13中心+10末端、19状态+4参数 \((\widehat\nu,L)\) 的有限边值问题可以逐字改用 (30)(31)，同时从新共同根按 (29)恢复其唯一原 \(\nu\)。

原真实左锚的最终 profile 仍是
\(\chi_\theta^\nu+2T_-(L)(\phi_\theta;\Delta_\theta)\)；
完整 T 在同一所得几何上由原 R73 恢复。不能用三个新 rho 坐标替代完整第三算子端值。pose、整个第四 period、同十三规范和主几何条件也没有由本变量替换消失。

## 9. 实现责任与新工作的具体范围

下一份源应先在公开 Actions 精确核 (24)，再用 (26)生成六个完整 C² 更新，以 (32)或其严格等价的有限积分评价必须回付的平方。允许为这个真实改写选择新的有限求解参数与 R589 的自由 H/L 末速度目标；不得原样重跑此前四个已失败初猜并把相同工作称为新验证。

该源须保：
一份固定物理母与原二尾、两侧同一个中心势、一个真正固定的 \(\nu\)、完整负侧反号、原 Ch/Ck 加速度系数、所有末势和真实左端重锚。尺度预条件不能改变等式或把 (32)吸收到未说明的残差阈值。

本稿严格减少的是历史更新的导数阶和其中独立大项读出；它没有证明新的实际有限根已经存在，也没有证明仅此预条件就足以使数值求解收敛。

### 原来源

- R73(3)–(10)、(15)–(17)：完整原二阶算子、原 M、变化-profile chain 和完整第三更新。
- R221(17)(18)：原有序三线性配对与全部真尾。
- R581：完整局部 R 的 C² 约化，原先的最高项身份只适用于其局部项。
- R584：真正十九态、共同中心 r、原 nu 的可逆平移和真实末重锚。
- R586：QQ/LLQ 平均、完整转置积分及 q_g² 分子。
- [R589](R589-autonomous-full-feedback-and-even-end-germs.md)：同一自主双反馈的全反射 germs 与真正自由 H/L 边界目标。

