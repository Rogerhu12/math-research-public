# R371：完整 H 层模 C² 恰十二维、十三个独立自然通量与真实闭路联合控制

> **2026-11-15 R378 更正。** 本稿“实际H模C²恰12维”撤回；修正后principal商为零。完整像至少13及相应实际13联合控制的旧证明不成立，须重新核完整C²值。详见[完整原式更正](R378-correction-of-the-third-history-term-in-the-complete-H-flux.md)。以下旧正文保留供追溯，不作为被撤回结论的当前证明。


日期：2026-11-15。**有限纸面证明；没有执行新的积分、符号程序、数值秩、人工测试或研究计算。**

[R366](R366-seven-independent-natural-fluxes-and-actual-joint-closed-path-control.md) 已证明：任意固定的有限自然通量向量，只要它在真实 H 状态值上满秩，就可由保真实全部 history、桥基准、物理下界及空间闭合的实际路径联合指定。该稿构造了七个固定读出。本稿从 [R365](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md) 的两个完整泛函和真实正仿射输运，补出整个 H 像的三阶平方部分，而不只看一个状态的七个权。

新结论分为三个不同层次：

1. 将 H 的全部自然通量泛函对连续 C² 泛函取商，所得像**恰为十二维**。
2. 完整 H 通量像至少还有一个非零连续 C² 方向，所以其维数**至少十三**；不宣称恰十三。
3. 可一次固定十三个真实紧 profile，使对应自然读出在 H 状态上满秩；沿用 R366 的一般向量定理，得到十三维实际双向联合控制、任意共同物理下界、空间闭合及紧目标集光滑截面。

这里 C² 指对 profile 的范数连续性，绝不是对成本算子先删去历史、左尾或低阶项。也不把十三个读出当作全 U、全 period 或固定度量的有限 flex。

来源：
[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)、
[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)、
[R358](R358-nonzero-total-flux-class-of-a-true-velocity-acceleration-cost.md)、
[R362](R362-full-H2-C2-remainder-and-nonzero-weight-minus-six-pure-kernel-flux.md)、
[R365](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md)、
[R366](R366-seven-independent-natural-fluxes-and-actual-joint-closed-path-control.md)。
真权提取、真实 U 成员和原几何采用已付 R105/R109/R129/R130/R134/R203，不重算旧表或旧秩。

## 1. 固定 profile 域、同锚尾与两个实际 H 系数

固定有限物理区间 \(I=[\ell,r_*]\)，取非空开子区间
\(I_0\Subset I\)，其右边预留三个原 R352 辅助包的共同 collar。
所有被比较的 profile 都在
\[
\mathcal D=C_c^\infty(I_0;\mathbb R)
\]
内。辅助包及其真实三矩基一次固定，右锚 \(r_*\) 不随 profile、目标或状态改变。

对实际成本 \(V\in U\)，记完整自然泛函
\[
F_V(u)=\Lambda_u(V)
=\Omega_u(V)-\frac{16}{5}L_u(\pi V)
-\frac{32}{15}\int u'''\,\mathscr G_{V,u}(\mu(u)).
\tag{1}
\]
\(\mathscr G\) 是原有序 \(2+2\) 的真实三矩尾映射，非自由的修正项。
由 R352，(1)在线性响应空间 \(R\) 上为零，且不依赖用于实现相同真实三矩读出的辅助方案。

用实际水平状态坐标
\[
d=h\omega-k,\qquad \gamma=h_s,\qquad\delta=d_s
\]
定义两个实际 U 元素
\[
\widetilde H_\gamma(S)=-2\{H_1(S)+2\omega H_2(S)\},
\qquad
\widetilde H_\delta(S)=4H_2(S).
\tag{2}
\]
坐标改变带来的加速度平方伙伴已由 R350 在每个实际状态上被所有自然 \(\Lambda\) 精确消去。

令
\[
\mathcal H=\operatorname{span}_{\mathbb R}
 \{F_{\widetilde H_\gamma(S)},F_{\widetilde H_\delta(S)}
 :S\text{ 为共同窗口上的合法实际状态}\}.
\tag{3}
\]
这里是完整泛函的线性像，不是实际正时长路径半群。

令 \(\mathcal C_2\) 为定义在 \(\mathcal D\) 上、对
\(\|u\|_{C^2(I)}\) 拓扑连续的实值泛函组成的实线性空间。
我们要计算的是
\[
\mathcal H/(\mathcal H\cap\mathcal C_2),
\]
等价于 \(\mathcal H\) 在所有实值泛函模 \(\mathcal C_2\) 中的像。
不要求这些泛函对 profile 本身线性；原 \(F_V\) 是五次泛函，对成本 \(V\) 才线性。

## 2. 从完整 R365 推到任意 \(h,d\)，不能漏掉 \(-dD_\delta\)

写
\[
v=u',\quad r=u'',\quad t=u''',\quad
E=ur-\frac{v^2}{2},\quad L=v-xr,\qquad
p(z)=z(1+z^2)^2=z+2z^3+z^5.
\tag{4}
\]
在基状态 \(S_*=(1,1,1)\)，R365 的完整公式为
\[
D_\delta(u)=\frac1{128}\int p(x)rEt^2+\mathcal R_\delta(u),
\quad
D_\gamma(u)=-\frac1{128}\int p(x)LEt^2+\mathcal R_\gamma(u),
\tag{5}
\]
其中 \(\mathcal R_\gamma,\mathcal R_\delta\in\mathcal C_2\) 是该稿明确给出的全部局部、同锚 primitive、\(j_A,j_B\) 与真实三矩尾的和。各项的 C² 连续性已经通过原式 IBP 证明；不是这里另作近似。

任意实际 \(h>0,d=h\omega-k\) 上，令
\[
w(\xi)=u\!\left(\frac{\xi-d}{h}\right).
\]
R365 的**完整**状态公式准确给
\[
\Lambda_u(H_2(S))=\frac h{15}D_\delta(w),
\qquad
\Lambda_u(H_1(S))=-\frac2{15}\{D_\gamma(w)+kD_\delta(w)\}.
\tag{6}
\]
因此
\[
F_{\widetilde H_\delta(S)}=\frac{4h}{15}D_\delta(w),
\qquad
F_{\widetilde H_\gamma(S)}
=\frac4{15}\{D_\gamma(w)-dD_\delta(w)\}.
\tag{7}
\]
第二式的 \(-dD_\delta\) 是原 \(2\omega H_2\) 与 \(kD_\delta\) 合成的结果，不能用单独的 \(D_\gamma(w)\) 替代。

在 \(\xi=hx+d\) 下有
\[
w'=h^{-1}v,\quad w''=h^{-2}r,\quad
w'''=h^{-3}t,\quad
w w''-\frac{(w')^2}{2}=h^{-2}E,
\]
\[
(w'-\xi w'')+d w''=h^{-1}(v-xr)=h^{-1}L,\qquad d\xi=h\,dx.
\tag{8}
\]
故 (5)—(8) 给出全部状态的准确分裂
\[
\boxed{
F_{\widetilde H_\delta(S)}(u)
=\frac{h^{-8}}{480}\int p(hx+d)\,rEt^2
+\mathcal R_{\delta;h,d}(u),}
\tag{9}
\]
\[
\boxed{
F_{\widetilde H_\gamma(S)}(u)
=-\frac{h^{-8}}{480}\int p(hx+d)\,LEt^2
+\mathcal R_{\gamma;h,d}(u),}
\tag{10}
\]
其中每个固定 \(h,d\) 的余项仍属于 \(\mathcal C_2\)。

常数 \(h^{-8}\) 对两式相同：δ 式中 (7) 的外部 \(h\) 正好补偿其额外一个 \(w''\) 的缩放；γ 式中 (8) 的 \(+dw''\) 正好消去错误的额外平移项。所有变换后的右锚、左矩与 primitive 仍来自完整 (6)，没有在 (9)(10) 中重新锚定它们。

(7) 也表明两个完整泛函在固定 \(h,d\) 时与独立 \(k\) 无关。对任意给定 \(\Omega>\max(0,-\ell)+1\)，可从起点选择
\[
\omega>\Omega+2,\qquad k=h\omega-d
\tag{11}
\]
使共同窗口上 \(x+\omega>1\)，而不改变 (9)(10) 的完整值。

## 3. 六个真实状态平移给全部五次多项式

固定 \(h=1\)，取任意六个互异的实数 \(d_0,\ldots,d_5\)。
六个多项式
\[
p(x+d_j),\qquad j=0,\ldots,5
\tag{12}
\]
构成 \(\operatorname{Pol}_{\le5}\) 的一组基。

给出有限代数证明。若
\(\sum_j c_jp(x+d_j)=0\)，依次比较
\(x^5,x^4,\ldots,x^0\) 系数。因 \(p\) 首项为 \(x^5\)，已经求出的较低矩消去所有 \(2x^3+x\) 的贡献，依次得到
\[
\sum_j c_jd_j^m=0,\qquad m=0,\ldots,5.
\]
普通六点 Vandermonde 非零，所以每个 \(c_j=0\)。
这不要求执行矩阵秩计算，也不将六个形式参数直接称为独立方向。

对每个 \(d_j\) 按 (11) 取一个真实状态 \(S_j\)。
由 (9)(10)，这十二个真实 H 系数在模 C² 意义下恰张成
\[
\mathscr T_{P,Q}(u)
=\int\{P(x)r-Q(x)(v-xr)\}
       \left(ur-\frac{v^2}{2}\right)t^2,
\qquad P,Q\in\operatorname{Pol}_{\le5}.
\tag{13}
\]
共同非零系数 \(1/480\) 不影响张成性。

另一方面，对任意 \(h>0,d\)，\(p(hx+d)\) 的次数仍不超过5。
所以 (9)(10) 也证明全部 H 像的模 C² 维数至多12。
还必须证明 (13) 没有隐藏的 C² 或 IBP 关系；仅看两个五次多项式不能当作维数证明。

## 4. 完整 principal 商的忠实性

假设某个 (13) 对 C² 拓扑连续。
任取真实 \(u_0\in\mathcal D\) 和实 \(\chi\in C_c^\infty(I_0)\)，定义
\[
u_N=u_0+N^{-5/2}\chi(x)\cos Nx.
\tag{14}
\]
这是实际有限光滑函数序列，且
\[
u_N\longrightarrow u_0\quad\text{于 }C^2,\qquad
u_N'''=u_0'''+N^{1/2}\chi\sin Nx+O(N^{-1/2}).
\]
令
\[
A_0(x)=\{P r_0-Q(v_0-xr_0)\}
       \left(u_0r_0-\frac{v_0^2}{2}\right).
\]
系数只含二阶 jet，故在 (14) 下均匀趋于 \(A_0\)。
固定紧区间上对 \(\sin^2Nx\) 的一次振荡平均给
\[
\frac{\mathscr T_{P,Q}(u_N)}{N}
\longrightarrow \frac12\int A_0(x)\chi(x)^2\,dx.
\tag{15}
\]
具体地，三导中的旧项和交叉项除 \(N\) 后趋零，系数误差为
\(O(N^{-1/2})\)，\(\sin^2Nx=(1-\cos2Nx)/2\) 的振荡部分由一次普通 IBP 趋零。
没有对任何 profile 实际运行积分。

若 \(\mathscr T_{P,Q}\in\mathcal C_2\)，则左边因 (14) 的 C² 收敛而趋零。
因为 \(\chi\) 可任意局部化，
\[
\{P(x)r-Q(x)(v-xr)\}
       \left(ur-\frac{v^2}{2}\right)=0
\tag{16}
\]
在每个 \(x\in I_0\)、每个可由紧光滑函数实现的二阶 jet 上成立。
固定一点的 \((u,v,r)\) 可由乘上局部 cutoff 的二阶多项式任意指定。

先取 \((u,v,r)=(1,1,0)\)，(16) 给 \(Q(x)/2=0\)。
再取 \((u,v,r)=(1,0,1)\)，得到 \(P(x)+xQ(x)=P(x)=0\)。
所以 \(P,Q\) 在非空开区间上为零，作为多项式处处为零。

反过来 \(P=Q=0\) 显然给零泛函。于是 (13) 对模 C² 商是忠实的，得到准确等式
\[
\boxed{\dim\{\mathcal H/(\mathcal H\cap\mathcal C_2)\}=12.}
\tag{17}
\]
(15) 同时排除了由局部 IBP 或未标出的连续 C² 项导致的额外依赖。
真正的完整余项仍留在 \(\mathcal H\) 中；本节没有证明它们为零。

## 5. 一个非零 C² 元素确实属于完整 H 像

仅有 (17) 尚不能推出完整 H 像超过12。需要一个来自同一 H 像的非零连续 C² 泛函。

R358 已对完整实际真权元素
\[
W_{-7}=\Pi_{-7}\widetilde H_\gamma(S_*)
\]
证明
\[
\boxed{F_{W_{-7}}(u)=-\frac1{57600}\int (u'')^5.}
\tag{18}
\]
这个公式包含原 self、pure 与两份真实有序尾，不是局部猜测。

还须确认 \(F_{W_{-7}}\in\mathcal H\)，不能仅由 \(W_{-7}\in U\) 推断。
原有限真权投影 \(\Pi_{-7}\) 是有限个互异正缩放 \(H_j\) 的完整共轭
\(P_{H_j,0}\) 的准确线性组合；这是 R203 的有限整权 Vandermonde。
R365/R366 的原协变关系在**全部**自然泛函意义下给
\[
P_{H,0}\widetilde H_\gamma(S)
\sim_\Lambda H^2\widetilde H_\gamma(\widetilde S),
\qquad
P_{H,0}\widetilde H_\delta(S)
\sim_\Lambda H\widetilde H_\delta(\widetilde S).
\tag{19}
\]
因此 (18) 是有限个真实 H 状态泛函的线性组合，确实位于 \(\mathcal H\)。
若这些原共轭状态的 \(\omega\) 不满足预定下界，用 (11) 选择同一 \(h,d\) 的实际 \(k,\omega\) 即可，完整泛函不变。
这里使用 signed 线性组合只证明像空间成员，不称其为正时长路径。

(18) 对 C² 连续且在 \(\mathcal D\) 上非零。
例如在 \(I_0\) 中取三个不交的同形偶非负 bump，
\[
r(x)=-\eta(x-x_0)
+\frac12\eta(x-x_0-b)+\frac12\eta(x-x_0+b).
\]
其零、一阶矩皆为零，故 \(u=J^2r\in\mathcal D\)，并且
\[
\int r^5=-\frac{15}{16}\int\eta^5\ne0.
\tag{20}
\]
全部宽度与间隔一次选小即可装入任意非空 \(I_0\)。

取第3节十二个真实 H 泛函为 \(F_1,\ldots,F_{12}\)，再取
\(F_{13}=F_{W_{-7}}\)。
若
\(\sum_{j=1}^{13}c_jF_j=0\)，对 \(\mathcal C_2\) 取商后由 (17) 先得
\(c_1=\cdots=c_{12}=0\)，再由 (18)(20) 得 \(c_{13}=0\)。
因此
\[
\boxed{\dim\mathcal H\ge13.}
\tag{21}
\]
我们没有给 \(\mathcal H\cap\mathcal C_2\) 的维数上界。
特别刚完成的 R370 四次速度 C² 通量不能仅因其 C² 连续就宣称位于 H 像外；该问题仍须完整比较。

## 6. 一次固定十三个真实 profile，而非十三个形式符号

使用如下 elementary 有限求值引理：

> 若 \(F_1,\ldots,F_m\) 是同一集合 \(\mathcal D\) 上线性独立的实值函数，则存在 \(u_1,\ldots,u_m\in\mathcal D\)，使矩阵 \((F_j(u_i))\) 可逆。

证明：所有求值行 \((F_1(u),\ldots,F_m(u))\) 必须张成 \(\mathbb R^m\)；否则某个非零向量垂直于全部求值行，给这 \(m\) 个函数的恒等线性依赖。
逐次选一条不在此前行 span 中的真实求值行，有限 \(m\) 次即得所需矩阵。
不要求函数对 \(u\) 线性，也不执行数值寻找。

将此引理用于 (21) 的十三个函数，得到一次固定的
\(u_1,\ldots,u_{13}\in C_c^\infty(I_0)\)，使
\[
A_0=(\Lambda_{u_i}(V_j))_{i,j=1}^{13}
\quad\text{可逆},
\tag{22}
\]
其中前十二个 \(V_j\) 是真实 H 系数，第十三个为 \(W_{-7}\)。

由第5节，(22) 的第十三列是有限个真实 H 列的线性组合。
故这些十三个读出在全部实际 H 状态值上满秩：
\[
\boxed{
\operatorname{span}\left\{
  \bigl(\Lambda_{u_i}(\widetilde H_\gamma(S))\bigr)_{i=1}^{13},
  \bigl(\Lambda_{u_i}(\widetilde H_\delta(S))\bigr)_{i=1}^{13}
 \right\}=\mathbb R^{13}.}
\tag{23}
\]
可以从这个集合选出十三个真实 H 列构成另一可逆矩阵。
因此第十三个 signed 权投影不会作为待实现的假路径进入下一步。

全部 profiles 的支撑都在同一个 \(I_0\)，右侧三个辅助包基与锚从第1节已经固定。
所以 (22)(23) 真正给十三个在同一 U/R 上定义的独立线性读出，
不是分属十三个窗口、锚或几何的互不兼容见证。

这是有限存在性证明，没有提供数值 profiles 或显式行列式下界。
该不足不影响 (23) 的严格满秩，但不能把它当作已经计算的离散控制器或已交网格。

## 7. 真实十三维控制：全部桥、倒行和空间基准沿用原一般定理

令
\[
\mathcal L=(\Lambda_{u_1},\ldots,\Lambda_{u_{13}}).
\]
(23) 正好满足 R366 §1 的一般有限 \(m\) 假设。
而 R350 的三个加速度平方系数在每个实际状态上被这些自然读出同时消去。
因此可直接应用已完整证明的 R366 §5—9，取 \(m=13\)，无需重复运行或重算其七维特殊见证。

明确保留其真实范围：

- 对任意预设 \(\Omega>\max(0,-\ell)+1\)，全部路径保持 \(h>0,\omega>\Omega\)，共同窗口上 \(x+\omega>1\)。
- 十三个实际 H 状态先由 (11)(23) 固定，再选择有限正时长的快速段；不是先解一个虚拟投影再假定有原型。
- 每段的真实返回桥使同一个 scalar/frame germ 及总 \(M=0\)，所有非零桥成本与完整传入 history 保留。
- 仅在完整 \(M=0\) 块上使用原 response 商；整块真倒行令 \(T=0\)，第四成本同号加倍。
- 一个足够小但有限的 \(\epsilon\) 上的向量 IFT 同时修正全部十三个读出及完整余项，紧目标集有同一有限拼接类型的光滑截面。

因此实际 \(M=T=0\)、frame \(I\to I\) 路径成本集合满足
\[
\boxed{\mathcal L(\mathcal S)=\mathbb R^{13}.}
\tag{24}
\]
(24) 是双向实际可达性，超出了 (21) 的 signed span。
它依赖原快速段与有限 IFT，而非把第5节的负系数当作负时间。

空间闭合仍用原八边 Klein 词
\(1,2,1,2,2,1,2,1\)，两条固定闭合桥全部成本保留。
完整成本为
\[
V_X=4V_P+4V_{C_1}+4V_{C_2}.
\]
先固定
\(b=\mathcal L(4V_{C_1}+4V_{C_2})\)，对目标 \(z\) 在 (24) 取
\((z-b)/4\)，得到
\[
\boxed{
X\text{ 空间、frame、scalar 闭合},\quad
M_X=T_X=0,\quad \mathcal L(V_X)=z.}
\tag{25}
\]
紧集光滑截面与物理下界保持。
这些仍是闭正则浸入数据，不冒充闭嵌入或 reach 证书。

## 8. 对后续工作的准确含义

(17) 给完整 H 层三阶平方商的准确维数，不是整个自然通量商的维数。
(21) 仅是完整 H 像的下界；连续 C² 核的其它方向、完整 Q2/Q4、静态族都须继续分析。

(24)(25) 排除这十三个读出的非零线性组合在整个实际成本集上必为单号。
它不排除其它未识别的正性泛函，不证明实际成本半群等于全 U，也不免费保持 whole pure、whole self、Gaussian 弱圆的其余第四条件或两条 period。

本模块的参数族可改变构造几何与度量，不能把它当作 README 要求的同一固定 g 的有限形变。
完整高阶收敛、全时间 C² 嵌入、连续全域 reach、宏观握持幅度以及要求的数值收敛与网格仍未完成。
完成本子题后继续 open.md 的完整 C² 核、其余正常层、同规范 joint 和余下 Gaussian 条件。
