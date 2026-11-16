# R411：正解析母可使完整零权自然通量的仿射轨道全零，以及增强实际锥的两个剩余权

日期：2026-11-16。**完整纸面证明；没有执行新的 profile、求积、符号消元、秩、人工检查、原根或科学运行。**

[R409](R409-eight-terminal-packet-fluxes-read-the-positive-canonical-character.md) 的非零第五曲率矩机制说明，不能把一组实际末包的总通量都当成可自由支付的目标。本稿处理其 $M_5=0$ 例外，但不从未知完整 $U_{-7}$ 像猜测下一个系数。

新的结果是一个明确的线性反例：存在真紧、严格正解析前因子的偶母 u，使 [R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md) 的整个零权函数 $n_2$ 在 u 的**全部正仿射像**上恒零。因此已有 $H_*\in\ker E$、$\lambda_+(H_*)=1$ 同时杀掉这个母的所有仿射自然查询。正字符不能经这个查询系统下降，即使同时加入 whole pure/self。

这不是把 signed $H_*$ 变成实际路径。对相应有限仿射查询商，本稿还准确关闭零权商缺口；实际闭锥证明则仍须检查增强权 $-6,-4$ 的完整正字符，不能用旧 $E$ 响应等像跳过它们。

来源：[R316](R316-complete-weight-zero-self-membership-and-positive-character-representative.md)、[R323](R323-full-pure-self-cone-and-complete-negative-weight-response-control.md)、[R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md)、[R356](R356-lowest-two-full-self-weights-and-universal-total-flux-cancellation.md)、[R365 独立协变节](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md)、[R393](R393-nine-dimensional-natural-Q4-affine-image-and-two-character-heads.md)、[R406](R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md) 与 [R408](R408-independent-second-gauge-invariant-fluxes-and-natural-character-extension.md)。

## 1. 所用完整原函数，不把最高项替代整式

沿 R406，记
$$
n_2(u)=\Lambda_u(H_*),\qquad
E(H_*)=0,\quad \lambda_+(H_*)=1,\quad H_*\in U_0 .
\tag{1}
$$
$\Lambda$ 仍是含原 pure、有序 $2+2$ Green 补偿的自然通量；因为 $H_*$ 的 whole pure 为零，其值也等于原裸 self 总通量。$E=(\pi,\mathcal Q)$ 中 $\mathcal Q$ 是完整 universal 左二次 self 读出，不是整个 self 输出函数。

R406 的已付完整密度为
$$
n_2(u)=\int\mathscr L(x,u,p,r),\qquad p=u',\quad r=u'',
$$
$$
\begin{aligned}
\mathscr L={}&u^2p^3-xup^4
+\frac32x^2u^2pr^2+\frac3{10}x^2p^5
-\frac12x^3u^2r^3-3x^3up^2r^2\\
&+\frac32x^4upr^3+\frac32x^4p^3r^2
-\frac14x^5ur^4-x^5p^2r^3
+\frac5{16}x^6pr^4-\frac3{80}x^7r^5 .
\end{aligned}
\tag{2}
$$
没有非局部余项。本文只对这个已经 paid 的明确函数作手工多项式展开和有限构造。

对 $C_{a,c}u(x)=u((x-c)/a)$，原协变为
$$
\Lambda_u(\mathsf P_{a,c}V)=a^2\Lambda_{C_{a,c}u}(V),\qquad a>0.
\tag{3}
$$
由于 $H_*\in U_0$，
$$
n_2(C_{a,0}u)=a^{-2}n_2(u).
\tag{4}
$$
所有式子先在共同右 collar 与实际支撑合法的开参数域中成立，再作为已有有限多项式身份使用；不重新锚定 primitive。

## 2. 偶母的四个真实系数

设 v 是实偶紧 profile，令
$$
p_v(c)=n_2(C_{1,c}v).
$$
在(2)中换元，显式 $x$ 变为 $x+c$；v、r 偶，p 奇。逐项奇偶给
$$
\boxed{p_v(c)=q_0(v)c^7+q_1(v)c^5+q_2(v)c^3+q_3(v)c.}
\tag{5}
$$
每个 $q_j$ 都是连续 $C^2$ 的五次齐次多项式泛函。这是完整函数的系数，不是 principal 观察。最高两项明确为
$$
q_0(v)=-\frac3{80}M_5(v),\qquad M_5(v)=\int(v'')^5,
\tag{6}
$$
$$
q_1(v)=
-\frac14\int v r^4-\int p^2r^3
+\frac{15}{8}\int xp r^4-\frac{63}{80}\int x^2r^5.
\tag{7}
$$
$q_2,q_3$ 准确由(2)、(5)定义；本文的构造不要求先把它们展成另一个新表。

$M_5=0$ 单独只删除(5)的七次项。若要用余项继续恢复 $\lambda_+$，必须同时处理其他真权成本的同次数贡献；不能仅因(7)非零便称它仍是正字符。下面直接把四个完整系数一同清零，避免依赖未付的 $U_{-7}$ 局部性。

## 3. 两个真非负偶母的 $M_5$ 异号

先给一个不依赖 profile 数值的存在证明。取 $0<a<b$，定义偶的紧、分段二次非负函数
$$
v_{a,b}(x)=
\begin{cases}
(ab-x^2)/2,& |x|\le a,\\
\dfrac{a}{2(b-a)}(b-|x|)^2,&a\le |x|\le b,\\
0,&|x|\ge b .
\end{cases}
\tag{8}
$$
它及一阶导数在接点连续，弱二阶导数为
$$
v_{a,b}''=
\begin{cases}
-1,&|x|<a,\\
a/(b-a),&a<|x|<b,\\
0,&|x|>b .
\end{cases}
$$
所以普通积分准确给
$$
M_5(v_{a,b})
=2a\left\{\left(\frac a{b-a}\right)^4-1\right\}.
\tag{9}
$$
取 $b-a<a$ 得正号，取 $b-a>a$ 得负号。

式(8)不被称为光滑母。把它与一个非负、偶、真紧 $C^\infty$ mollifier 卷积，得到非负偶真紧光滑函数。二阶导在 $L^5$ 收敛，且具有共同有限支撑和一致有界幅，所以(9)的两个严格号在足够小的**固定正** mollifier 宽下保持。此时即冻结两个真正的 $C_c^\infty$ 母 $v_+,v_-$，按
$$
q_0(v_+)>0,\qquad q_0(v_-)<0
\tag{10}
$$
命名。不是执行了 mollifier 或取非光滑极限作为最终输入。

## 4. 四个实际半径、十六个真包和严格正第五幅权

选择四个不同正数
$$
0<z_1<z_2<z_3<z_4.
$$
再固定两个相差足够大的 offset $d_+,d_-$，使同一半径处两种母的支撑也严格分离。对有限大 L 取
$$
t_{j,\pm}=Lz_j+d_\pm>0,\qquad
\phi_{j,\pm}(x)=v_\pm(x-t_{j,\pm})+v_\pm(x+t_{j,\pm}).
\tag{11}
$$
L 足够大时，全部十六个实际支撑互不交。每个 $\phi_{j,\pm}$ 是偶、非负、真紧光滑函数。

记 $\mathbf b_\pm(t)\in\mathbb R^4$ 为(5)中四个 odd 系数，对双镜像包有完整精确式
$$
\boxed{
b_{\pm,j}(t)=
2\sum_{\ell=0}^{j}
\binom{7-2\ell}{2j-2\ell}\,
q_\ell(v_\pm)t^{2j-2\ell},
\qquad j=0,1,2,3 .
}
\tag{12}
$$
这只是 $p_{v_\pm}(c+t)+p_{v_\pm}(c-t)$，不省略任何较低系数。

对每一行按 $2\binom7{2j}L^{2j}$ 归一后，由(11)—(12)，
$$
\mathbf b_\pm(t_{k,\pm})
\longrightarrow
q_0(v_\pm)(1,z_k^2,z_k^4,z_k^6)^{\mathsf T}.
\tag{13}
$$
固定 offset 的误差为 $O(L^{-1})$，原低系数的误差至多 $O(L^{-2})$；只需它们趋零。

四个 Vandermonde 列严格独立。极限八列有严格正核：
$$
w_{k,+}^{\,0}=\frac1{q_0(v_+)},\qquad
w_{k,-}^{\,0}=-\frac1{q_0(v_-)} .
\tag{14}
$$
固定后四个正权 $w_{k,-}=w_{k,-}^{\,0}$，对真实有限 L 的四个正号列解四个原线性方程。由(13)及可逆 minor，解 $w_{k,+}(L)$ 收敛到(14)，故在足够大的一个固定有限 L 处仍全严格正。

取真正幅度 $a_{k,\pm}=w_{k,\pm}^{1/5}>0$，定义
$$
u_*=\sum_{k=1}^4
\{a_{k,+}\phi_{k,+}+a_{k,-}\phi_{k,-}\}.
\tag{15}
$$
(2)是局部五次密度，原十六支撑不交，所以
$q(u_*)=\sum w_{k,\pm}\mathbf b_\pm(t_{k,\pm})$，没有跨包 primitive 或 mixed 项。于是
$$
\boxed{q_0(u_*)=q_1(u_*)=q_2(u_*)=q_3(u_*)=0.}
\tag{16}
$$
这里四个 $w_{k,+}$ 的真实 Jacobian 就是(13)对应的有限可逆矩阵。不能只从极限 span 宣称正核；(14)的正余量和有限 L 逆矩阵共同支付了它。

$u_*$ 尚有内部零间隙。下一节把它换成整个活动区间内严格正的解析前因子，保持(16)的精确值。

## 5. 正解析前因子的有限参数逼近和真实四根

固定对称区间 $(-R,R)$，使(15)的全部支撑严格位于内部。令
$$
\psi_3(x)=
\exp\!\left\{-\frac3{1-(x/R)^2}\right\}\quad(|x|<R),
$$
外面为零。把(15)的八个偶非负成分依次记为 $\phi_i$；每个
$$
r_i(x)=\phi_i(x)/\psi_3(x)
$$
在闭 $[-R,R]$ 上是光滑、偶、非负函数，因为 $\phi_i$ 在靠近两端的邻域已零。

给定小 $\eta>0$，先取 $\sqrt{r_i+\eta}$ 的偶多项式 $Q_i$ 作 $C^2$ 逼近。这个逼近可以直接由二阶导数的普通多项式逼近再积分两次、最后取偶部获得。由乘法连续性，$Q_i^2$ 在 $C^2$ 中任意接近 $r_i+\eta$，从而接近 $r_i$。没有要求非负函数的零点处存在一个光滑平方根。

把四个 $w_{k,+}$ 留在(16)根附近一个固定的紧正参数盒，其他权仍固定。写原八个幅度为 $a_i(w)>0$。定义真正的新家族
$$
u_{w,\eta}(x)
=\psi_3(x)\left\{\eta+\sum_{i=1}^{8}a_i(w)Q_i(x)^2\right\}.
\tag{17}
$$
其前因子是整个闭区间上严格正的偶多项式，至少为 $\eta$。对全部盒内 w，函数及其 w 导数都可在 $C^2$ 中一致逼近原
$\sum a_i(w)\phi_i$；这是有限和，$w^{1/5}$ 及其导数在该正盒上有统一界。

$q=(q_0,\ldots,q_3)$ 是连续 $C^2$ 五次多项式，所以相应四方程及其 w 导数一致收敛于第4节的真实四方程。原 Jacobian 可逆。于是先固定足够小的正 $\eta$ 和足够好的有限多项式，再用原有限维 IFT/收缩，在同一正盒内得到一个有限 w，准确满足
$$
q(u_{w,\eta})=0.
\tag{18}
$$
这一步没有以近似零代替零，也没有让幅度过零。最终 u 是一个固定、非零、真紧 $C^\infty$ profile，在整个活动区间内严格正，且具有真正正解析前因子。它满足
$$
\boxed{n_2(C_{1,c}u)=0\quad\text{作为 c 的整个多项式}.}
\tag{19}
$$
本构造不控制 $A_u$ 的具体零点数或其简单性，也不宣称(17)属于 R405 已冻结的十九目标纤维。

## 6. 整个正仿射轨道与一个真实核反例

由(4)，
$$
n_2(C_{a,c}u)
=a^{-2}n_2(C_{1,c/a}u)=0,\qquad a>0 .
\tag{20}
$$
因此可将最终母按一个固定正仿射变换压入任意给定合法开窗口；(19)—(20)保持，端芽仍是 $\psi_3$ 乘正解析前因子。不要求物理坐标 0 位于原几何域内。

记其全正仿射自然查询映射为
$$
\mathcal A_u(V):(a,c)\longmapsto\Lambda_{C_{a,c}u}(V),
$$
$$
J_u(V)=\bigl(E(V),\mathcal A_u(V)\bigr).
\tag{21}
$$
参数只须覆盖一个共同支持合法的开域；有限函数身份给相同线性核。因为 U 有限维，(21)具有有限维真实像，并可由有限个真实查询承载；没有声称这些查询线性独立。

由(1)、(20)，
$$
\boxed{H_*\in\ker J_u,\qquad \lambda_+(H_*)=1.}
\tag{22}
$$
所以不存在一个经 $J_u$ 因子化、等于 $\lambda_+$ 的线性泛函。这不仅排除某个八点插值公式，而是排除该母全部平移、全部正缩放加 whole-$E$ 后的任何这种线性恢复。

式(22)是原已付 $H_*$ 的 signed 线性空间结论。它不声称 $H_*$ 是一条真实路径成本，不声称当前母能够安装为原全部几何/profile 约束下的最终圆，也不从“$\lambda_+$ 不下降”直接推出实际控制。

## 7. 真正有限仿射商的零权缺口已经关闭

这里可以继续一步准确的实际接口，而不把(22)升级过度。

由(3)和正仿射组合，$\ker\mathcal A_u$ 在原正仿射作用下稳定；$\ker E$ 也由 R322/R323 的原协变稳定。于是 $\ker J_u$ 是 U 的真实仿射不变核。有限 Laurent 投影使它逐真权稳定，因此也在 R145 的原代数反号
$\mathsf S=\sum_\sigma(-1)^\sigma\Pi_\sigma$ 下稳定。这个论证不需要给负缩放的输入右积分另造规范。

所有自然查询杀原响应 $\mathcal R$，故
$$
J_u(\mathcal R)=\{(E(R),0):R\in\mathcal R\}.
\tag{23}
$$
R406 完整零权结论是
$$
\Lambda_\cdot(V_0)=\lambda_+(V_0)n_2,\qquad V_0\in U_0.
$$
结合(20)及 R333 的 $E(U_0)=E(\mathcal R_0)$，准确得到
$$
\boxed{J_u(U_0)=J_u(\mathcal R_0).}
\tag{24}
$$
因此商
$$
\mathscr C_u=J_u(U)/J_u(\mathcal R)
$$
的零权部分确为零；不只是单个 $H_*$ 见证，也不需要新增旧权零成员计算。

## 8. 实际闭锥仍只剩两个明确候选权，但尚未支付

令 $\mathcal S$ 为原同端口、frame 闭合、$M=T=0$ 的真实有限路径成本半群，取
$$
C_u=\overline{\operatorname{cone}\{J_u(V_B):V_B\in\mathcal S\}}.
$$
若该闭锥不是整个 $J_u(U)$，R127/R145 在这个真实有限仿射商上给一个非零单整权正字符。其拉回杀 $\mathcal R$ 和 $\ker J_u$。按 R190 的原权支撑，候选权仍为
$-8,-6,-4,-2,0,2$，其中：

- $-8$：R356 给全部自然通量零，R323 给 $E(U_{-8})=0$，故 $J_u(U_{-8})=0$。
- $+2$：R190 给完整 $U_2=\mathcal R_2$。
- $-2$：R188 已排除该权的全部非零完整正仿射字符。
- $0$：R196 的完整实际正字符只能是正倍 $\lambda_+$，但(22)使其不可能杀 $\ker J_u$。

因此剩余候选准确缩到
$$
\boxed{\sigma=-6,\,-4.}
\tag{25}
$$
这里不能再次照抄 R323 对旧 E 的排除：虽然
$E(U_\sigma)=E(\mathcal R_\sigma)$，新增的 $\mathcal A_u(U_\sigma)$ 仍可能非零。它杀响应，故旧响应的 self 等像并不支付它。

原正常层 $F_0$ 与三个完整 $\widehat Q_2$ 仍必须保其 $N_0,N_2,\Gamma$ 和全部尾。R393 的 Q4 表只是一部分函数像；本稿没有证明完整 $U_{-7}$ 自然像只有 $\int r^5$，也没有证明(25)的完整字符头或 action 为零。

若后继从原完整成本准确排除(25)两个增强正字符，则闭锥才成为全空间。此时(24)已经支付 R206/R212 从闭锥到真实有限截面的零权商条件；其余原证明可在这个有限 J 商上保全部原型、复制基准、真实倒行、端口桥和最终收缩，得到同一路径的 $E+\mathcal A_u$ 实际联合截面。这个句子是明确的条件结论，不是本稿已付 actual。

## 9. 与固定圆、二阶规范及前两稿的关系

R408 证明允许的同一二阶规范不能改变真实包总量及 $A_f=0$ 部分通量。R409 对非零 $M_5$ 的实际末包列恢复正字符；本稿没有改动该正确范围。

这里的母满足更强的四式(18)，因而确实展示一个不能通过同母仿射 natural 查询线性恢复 $\lambda_+$ 的例外。它没有改变原 canonical 正性，也没有让任意新 $w$ 越出十三行真实定义域。

最后仍分别未付：

- 该母在原 R405 全观察纤维、十九个有理端口目标及具体内部退化模式中的实现；
- (25)两个增强负权正字符的完整低层 action；
- 同一路径对所需 fixed-circle mixed 总量、内部通量及十三门的实际联合控制。

本文新完成的是(19)—(24)的真实母、完整仿射盲性、signed 核反例和零权商消失；不以“泛函非零”“有限维”或分开可达替代这些尚欠的实际问题。
