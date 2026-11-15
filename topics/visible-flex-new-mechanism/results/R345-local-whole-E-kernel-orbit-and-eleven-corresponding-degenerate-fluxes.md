# R345：局部 whole-E 核的完整十一维轨道与对应退化点通量

日期：2026-11-15。**完整纸面原式与有限实现证明。** 没有执行新符号计算、求积、数值秩、人工检查或科学运行。

[R340](R340-local-whole-pure-self-kernel-and-two-actual-degenerate-flux-controls.md) 给出完整 pure/self 核中的两条局部响应。本稿给出其整个有限代数轨道，证明前十一条成本真独立，且对当前实际圆上任意至多十一个同形对应退化点，通量矩阵准确可逆。真实增强控制由此可以在保持 whole pure 与 whole self 的同时支付这十一个必要门。

这是 R324/R340 的实际有理端口圆线路。它不将 R343 的弱 Gaussian 圆与这里的 profiles 或几何混为同一个对象，不授全部退化点、两个完整 period 或同一 gauge 的全部兼容。

来源：[R247 §6](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md) 的真实交换子 sl2 模、[R330](R330-two-actual-packet-degenerate-fluxes-and-twenty-observation-control.md) 的实际解析包和退化查询、R340 的完整局部原式、[R333](R333-complete-joint-pure-self-membership-and-real-finite-control.md) 的原 E 商截面与 [R302](R302-regular-chi-prototypes-shared-reversal-and-enhanced-Morse-control.md) 的真实全局增强接口。

## 1. 完整局部最低权成本

沿用共同右锚和原算子
\[
P(a,b)=J(a''b''),\quad
S(a,b)=J(xa''b''),\quad
\tau_S=[P,S]=-J(a''b''c'').
\]
定义
\[
K_0=\widetilde{\mathcal K}=\frac13\mathcal B_P(\tau_S),
\qquad K_n=\delta^nK_0,\qquad
\mathscr D=x^2\partial_x-2x.
\]
导子始终是
\[
\delta V=\mathscr D_{\rm out}V-D_{\rm inputs}V[\mathscr D\,\text{inputs}],
\]
并不是对实际几何免费作非仿射坐标变换。

R340 已从三条完整响应项证明：任意值支撑严格不交的实紧 profiles \(u_i\)，若
\[
f=\sum_i a_i u_i,\qquad \phi=\sum_i c_i u_i,
\]
则在整个原区间上
\[
\boxed{K_0(f^2,\phi)=-\frac13\sum_i a_i^2(a_i^2-c_i^2)(u_i'')^4.}
\tag{1}
\]
这是全部原输出，无跨包项、左尾或未付常数。共同零 collar 及所有导数都保持。

原 \(E=(\pi,\mathcal Q)\) 中，\(\pi\) 是完整 canonical pure 投影，\(\mathcal Q(V)(u)\) 是原 \(V(u^2,0)\) 的左二次系数除以4。已有 \(E(K_0)=0\)。

## 2. 每个后继仍是完整局部输出：一个有限生成式

对一个 profile 记
\[
u=u(x),\qquad v=u'(x),\qquad r=u''(x).
\]
设局部四次多项式为 \(P(x,u,v,r)\)。因为
\[
\mathscr Du=x^2v-2xu,\quad
(\mathscr Du)'=x^2r-2u,\quad
(\mathscr Du)''=x^2u'''+2xr-2v,
\]
对输出与所有输入求导后的最高 jets 准确相消，余下
\[
\boxed{
\mathcal L P
=x^2P_x+2xuP_u+2uP_v+(2v-2xr)P_r-2xP.
}
\tag{2}
\]
这里 \(P_x\) 只微分显式 \(x\)，不是再次对 profile 全微分。

置 \(P_n=\mathcal L^n(r^4)\)。对(1)沿所有实际输入槽共同求导；变化 \(\mathscr D u_i\) 不扩大支撑，也保持同一包内的比例 \(a_i,c_i\)。归纳得到完整全区间身份
\[
\boxed{
K_n(f^2,\phi)
=-\frac13\sum_i a_i^2(a_i^2-c_i^2)
P_n(x,u_i,u_i',u_i'').
}
\tag{3}
\]
它只含原局部二阶 jets；没有因多次 \(\delta\) 产生新的实际尾。

式(2)可以直接手解。其向量场流为
\[
x_z=\frac{x}{1-zx},\quad
u_z=\frac{u}{(1-zx)^2},\quad
v_z=v+\frac{2zu}{1-zx},
\]
\[
r_z=(1-zx)^2r+2z(1-zx)v+2z^2u,
\]
乘子满足 \(w_z=(1-zx)^2\)。于是
\[
\boxed{
\sum_{n\ge0}\frac{z^n}{n!}P_n
=(1-zx)^2
\bigl((1-zx)^2r+2z(1-zx)v+2z^2u\bigr)^4.
}
\tag{4}
\]
可在 \(z=0\) 邻域作普通微分验证这个流；它只是求原代数导子的有限系数，不声明这些流是允许的真实几何变化。

右侧是次数至多10的多项式。例如
\[
P_0=r^4,\qquad P_1=-10xr^4+8vr^3,
\]
准确恢复 R340 的两列。\(P_n\) 中 \(x^nr^4\) 的系数为
\[
(-1)^n\frac{10!}{(10-n)!}\quad(0\le n\le10).
\tag{5}
\]
式(4)不是由程序拟合或有限 profile 采样得到。

## 3. 轨道在真实响应空间内恰为十一维

必须区分局部 rank-one 身份与 universal 完整算子身份。仅凭(4)不能推出 \(K_{11}\) 在全部输入上为零；这需要原完整响应空间的表示结构。

R247 已证明 \(E_8\simeq V_4\oplus V_2\)，其 H 权最大为2；真实交换子空间 \(W_{71}\simeq2V_6\oplus V_4\oplus3V_2\)，最大 H 权为3。\(\mathcal R_{71}=\mathcal B(E_8,W_{71})\) 是其等变像，最大 H 权因此不超过5，且在 \(N,H,\delta\) 下闭合。

本稿只使用 \(\mathcal R_{71}\)。不假定额外八个第三方向或整个 \(\mathcal R\) 在 \(\delta\) 下闭合。

由原 \(NP=0,\ NS=P\) 有 \(N\tau_S=0\)，又 \(HP=-2P,\ HS=-S\)，故
\[
NK_0=0,\qquad HK_0=-5K_0.
\]
原关系 \([N,\delta]=2H,\ [H,\delta]=\delta\) 给
\[
\boxed{
HK_n=(-5+n)K_n,\qquad
NK_n=n(n-11)K_{n-1}.
}
\tag{6}
\]
\(K_{11}\) 若非零将有 H 权6，与上述真实响应权范围矛盾，所以
\[
K_{11}=0
\quad\text{作为完整 universal 成本。}
\]
另一方面，(1)表明 \(K_0\ne0\)。对 \(0\le n\le10\)，
\[
\boxed{
N^nK_n=(-1)^n n!\frac{10!}{(10-n)!}K_0\ne0.
}
\tag{7}
\]
这些非零向量的 H 权互异，因而真独立。定义
\[
\boxed{
\mathscr K=\operatorname{span}\{K_0,\ldots,K_{10}\}
\simeq V_{10},\qquad \dim\mathscr K=11.
}
\tag{8}
\]
这是真响应子空间的准确维数，不是整个 \(\mathcal R\cap\ker E\) 的维数或新数值秩。

H 权不能与真成本仿射权混同。四输入成本相差三个单位；这里 \(K_n\) 的真成本权为 \(-8+n\)。

## 4. 整条轨道属于 whole pure/self 核

pure 投影与原代数导子交换，故 \(\pi K_n=0\) 对全部 \(n\) 成立。

在(3)取单个任意实紧 \(u\)、\(f=u,\phi=0\)，所有 \(K_n(u^2,0)\) 都是紧支撑局部多项式。因此左二次系数、左一次系数和左常数全部准确为零。特别
\[
\boxed{
\mathscr K\subset\mathcal R_{71}\cap\ker\pi\cap\ker\mathcal Q
=\mathcal R_{71}\cap\ker E.
}
\tag{9}
\]
这对任意实紧 \(u\) 成立，不只对一个 even 母包或有限平移族。对不交的 rank-one 圆，(3)进一步保全部跨包和外 collar 输出为零。

整包总通量也准确为零。记
\[
\Omega_u(V)=\int u'''V(u^2,0).
\]
共同零 collar 下的分部积分给
\[
\Omega_u(\delta V)=-D_u\Omega_u(V)[\mathscr Du],
\tag{10}
\]
因为
\[
(\mathscr Du)'''=x^2u''''+4xu''',\qquad
\int u'''\mathscr D F=-\int(x^2u''''+4xu''')F.
\]
真实左尾不影响这个边项，外 profile 的 jets 平坦。由
\[
\Omega_u(K_0)=-\frac13\int u'''(u'')^4=0
\]
归纳得 \(\Omega_u(K_n)=0\)。因此本轨道可改变内部部分通量，却不改变整包总通量；不能用它修补任意非零整包 \(\Omega\)。

## 5. 当前实际圆中有十一个可用的对应查询

仍固定 R324/R330/R340 的最终有限频率、有限纠正后的真实 profiles，而不是原母包近似。选择其中一个最细解析包 \(u=\psi P\)、\(P>0\)，及真实点 \(x_*\)，满足
\[
A_u(x_*):=6u'(x_*)u'''(x_*)-2u''(x_*)^2=0,
\quad u'(x_*),u''(x_*)>0.
\tag{11}
\]
R330 的 \(z=(u')^{2/3}\) 内部极大点论证已给其存在，不要求简单零。

原八副本和十二副本在最终 block 中都仍是完整平移与非零共同幅度。选同一基本包在其中任意 \(m\le11\) 个不同副本，写为
\[
f=\rho_j a\,u(x-t_j),\qquad
g=\rho_j\epsilon_j b\,u(x-t_j),\qquad
\epsilon_j\in\{1,-1\},
\tag{12}
\]
\[
\rho_j\ne0,\quad t_i\ne t_j\ (i\ne j),\quad
a\ne0,\quad a^2-b^2\ne0.
\]
跨十二副本时 \(g\) 可能翻号。这里明确保留 \(\epsilon_j\)；(3)在 \(\phi=g\) 时只含 \(c_i^2\)，所以符号不会改变本轨道的输出或下面常数。无需假称十一个都来自只有八个成员的单一八副本。

令 \(\ell_j=\ell+t_j,\ x_j=x_*+t_j\)。这些点是同一实际 \(A_f\) 的零点。对全部 \(U\) 定义原完整读出
\[
\mathcal F_j(V)=\int_{\ell_j}^{x_j}f'V(f^2,g)''
-\{f(x_j)-f(\ell_j)\}V(f^2,g)''(\ell_j).
\tag{13}
\]
平台修正对一般 \(U\) 始终保留。对本轨道，由(3)它准确为零，且其他所有包无跨尾贡献。

原 \(L_f\) Green 身份仍给
\[
\mathcal F_j(L_fw)=0
\tag{14}
\]
对允许的任意全区间光滑 \(w\) 成立。故这些是同一实际 \(V_d\) period 的真实必要门。

## 6. 通量多项式和准确 Vandermonde

以基本包上的原读出 \(\mathcal F_*\) 记
\[
C_*=\mathcal F_*(K_0)
=-\frac8{45}a^3(a^2-b^2)u''(x_*)^5\ne0.
\tag{15}
\]
这是 R340 保上端 jets 的完整分部积分值。记 \(c_n=\mathcal F_*(K_n)\)，其中 \(c_0=C_*\)；不需要分别执行积分求所有 \(c_n\)。

对真实平移 \(T_tu(x)=u(x-t)\)，搬回输出点的代数作用是 \(e^{tN}\)。由(6)，
\[
p_n(t):=\mathcal F_*(e^{tN}K_n)
=\sum_{r=0}^n\frac{t^r}{r!}\mathcal F_*(N^rK_n).
\tag{16}
\]
这是准确次数 \(n\) 的多项式，且
\[
[t^n]p_n=(-1)^n\frac{10!}{(10-n)!}C_*\ne0.
\tag{17}
\]
共同右锚位于所有支撑右方；本轨道全局局部，因此上述平移无需额外尾或重锚假设。

四次输出和读出的一个 \(f'\) 给实际第五次幅度：
\[
\boxed{\mathcal F_j(K_n)=\rho_j^5p_n(t_j).}
\tag{18}
\]
\(\epsilon_j\) 已由(3)消去，不能把它误并到 \(\rho_j\) 的第五次符号里。

对 \(m\le11\)，取列 \(K_0,\ldots,K_{m-1}\)。由逐次多项式基变换，
\[
\boxed{
\det(\mathcal F_j(K_n))_{\substack{1\le j\le m\\0\le n<m}}
=
C_*^m\left(\prod_{j=1}^m\rho_j^5\right)
\left(\prod_{n=0}^{m-1}(-1)^n\frac{10!}{(10-n)!}\right)
\prod_{1\le i<j\le m}(t_j-t_i)\ne0.
}
\tag{19}
\]
因此
\[
\boxed{(\mathcal F_1,\ldots,\mathcal F_m)
(\mathcal R\cap\ker E)=\mathbb R^m\quad(m\le11).}
\tag{20}
\]
此结论来自已定实际 shape、非零退化点常数和完整无尾成本，不来自行数或 formal column 数量。

## 7. 更多对应点时，本模块的准确范围

对同一基本点的任意有限个不同对应副本，整个 \(\mathscr K\) 的通量像准确是
\[
\boxed{
\left\{(\rho_j^5p(t_j))_j:p\in\mathbb R[t],\ \deg p\le10\right\}.
}
\tag{21}
\]
若有至少十一个点，该模块的秩恰为11。十二个点上的目标 \(b_j\) 必须满足
\[
\boxed{
\sum_{j\in J}
\frac{b_j/\rho_j^5}{\prod_{i\in J,\ i\ne j}(t_j-t_i)}=0,
\qquad |J|=12.
}
\tag{22}
\]
对任意有限点集，这些十一阶差商条件也充分：先在任意十一个点插值为唯一次数至多10的多项式，再用每个新增点与这十一点的(22)迫其值一致。

(22)只描述这个明确十一维子模块，**不是全部 \(\mathcal R\cap\ker E\) 的限制**。其他响应可能给额外方向。也不能从 \(m\le11\) 的满射声称同一微包内任意十一个不同退化点都满射；(12)要求同一个实际基本点的对应平移副本。

## 8. 与 whole E 的同一个真实控制系统

固定上述 \(m\le11\) 个查询，令
\[
\widehat E=(E,\mathcal F_1,\ldots,\mathcal F_m),\qquad
\mathscr P=E(U),\quad \mathscr L=E(\mathcal R).
\]
由(9)、(19)，准确有
\[
\widehat E(U)=\mathscr P\times\mathbb R^m,\qquad
\widehat E(\mathcal R)=\mathscr L\times\mathbb R^m.
\tag{23}
\]
增广响应商仍是原 \(\mathscr P/\mathscr L\)。

实际有符号实现不能从线性满射自动获得。这里沿用 R340 §7 已支付的构造，但把两列换成(19)的 \(m\) 列：

1. 只沿 R333 原 E 商构造有限真实 \(C^1\) 截面。固定点通量不被假称仿射不变；所有额外通量是截面的实际成本，全部保留。
2. 取原 E 响应像的一组基列，再加 \(K_0,\ldots,K_{m-1}\)。未知的原基列通量保留为左下块，右下块是(19)，因此增广响应基准确可逆。
3. 各真实第三原型、原商修正、scalar/frame 桥及所有复制基准都进入同一有限成本方程，不免费添加 signed 零基准响应。
4. 在固定紧参数盒中，最后仍是
\[
F(p,t)+n(A+t)=p_{\rm resp}.
\]
选择最后一个有限整数 \(n\)，原收缩给准确根和 \(C^1\) 参数依赖。

故对真实 \(M=\mathbf T=0\) 成本半群 \(\mathcal S\)，
\[
\boxed{
\widehat E(\mathcal S)=E(U)\times\mathbb R^m,
}
\tag{24}
\]
并有紧目标集上的有限真实 \(C^1\) 截面。E 目标仍须相容地属于 \(E(U)\)，不是任意 \(\pi U\times\mathcal Q(U)\)。

所有查询是固定有限 profiles 与固定端点上的线性泛函；原 R56 恢复的几何参数依赖仍光滑。有限个查询不会引入几何变量中的分布型约束。R302 的增强 IFT、共享原型和真倒行可同时保已固定有理核心及全部实际基准。

## 9. 同一新闭几何和准确剩余门

按 R340 的顺序，先定原有限库与本十一列所需的有限交换子原型、指定有理芽及最终 profiles；再固定查询点，作上述同一增强实现。Klein 闭合的实际背景成本也作为完整 \(\widehat E\) 目标保留，准确得到一个新实际闭 hook，使
\[
\pi V_X=0,\quad\mathcal Q(V_X)=0,\quad
\mathcal F_1(V_X)=\cdots=\mathcal F_m(V_X)=0.
\tag{25}
\]
这通常选择新的全局几何与目标 metric；不冒称在旧冻结 \(g\) 上免费加列。

用该新几何真正的传入 \(m_*\) 重取 R326 的同一 \(w_c=-\Phi_{m_*}D_\theta\)。由(14)，所有(25)的通量均保持，whole self 同时保持当前全部二次平台，指定有理端口的已付 ruling 按原局部接口保持。

这并未支付其他基本形状或其他内部 \(A_f\) 零点、\(V_e\)、全部整包量、仿射平台/右锚常数、完整光滑除法与端 germ、两个 period 的实际像、R327 十三行的同一相位解，以及其它段 ruling、高阶收敛和有限等距族。

本稿完成的是：完整局部生成式(4)、真实十一维 whole-E 核(8)—(9)、同形对应点的准确满射(19)—(20)、更多对应点的精确模块边界(21)—(22)，以及保全部基准的同一实际实现(24)—(25)。这些结论完成即推，随后继续未付的完整 period 与其他原接口。
