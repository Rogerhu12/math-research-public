# R366：七个独立自然总通量的真实联合控制与闭空间安装

日期：2026-11-15。**完整有限纸面证明；没有执行新的求积、秩计算、符号程序、几何试验或人工检查。**

[R363](R363-actual-two-sided-total-flux-control-with-zero-lower-history-and-spatial-closure.md) 已把一个非零自然总通量读出实现为真正的双向路径控制。本稿给出它的有限向量版本，并从完整 H 层构造七个固定、彼此独立的自然读出，证明其联合值在实际零矩阵、零第三历史路径上覆盖整个七维实空间。补桥、倒行、固定空间闭合桥的成本全部保留。

这不是只给七个有符号的线性空间元素：最终每个目标都对应有限正时长、同端芽、真实水平几何，并有紧目标集上的光滑截面。它也不是同一个固定度量的有限 flex；这里调的是构造几何的真实成本。

来源：R363 的完整局部密度与实际桥证明，以及
[R350](R350-total-flux-factorization-for-the-three-actual-acceleration-square-costs.md)、
[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)、
[R358](R358-nonzero-total-flux-class-of-a-true-velocity-acceleration-cost.md)、
[R362](R362-full-H2-C2-remainder-and-nonzero-weight-minus-six-pure-kernel-flux.md)、
[R365](R365-complete-H-layer-affine-orbits-and-exact-total-flux-functionals.md)。
有限真实空间、真权分解、原 history 及空间闭合继续使用原 R105、R109、R129、R130、R134、R203、R210、R354，未重算其已付结果。

## 1. 准确的向量控制命题

固定有限区间 \(I=[\ell,r_*]\)，其中0为内点，并预留共同右 collar。固定有限个真实紧 profile \(u_1,\ldots,u_m\)，以及它们在同一右锚上的自然泛函
\[
\mathcal L(V)=(\Lambda_{u_1}(V),\ldots,\Lambda_{u_m}(V)).
\]
每条 \(\Lambda_u\) 都保 R352 的完整 ordered \(2+2\) 真尾，且在原响应空间 \(R\) 上为零。

用真实水平坐标
\[
d=h\omega-k,\qquad \gamma=h_s,\qquad\delta=d_s,
\]
并以自然泛函的意义记
\[
\widetilde H_\gamma=-2(H_1+2\omega H_2),\qquad
\widetilde H_\delta=4H_2 .
\tag{1}
\]
这两个实际系数都来自原 \(U\)。原坐标变换所附加的加速度平方伙伴由 R350 在每个状态上被所有 \(\Lambda_u\) 准确消去。

假设实际 H 值满足
\[
\operatorname{span}\{\mathcal L(\widetilde H_\gamma(S)),
 \mathcal L(\widetilde H_\delta(S)):S\ {\rm admissible}\}
=\mathbb R^m.
\tag{2}
\]
则对任意预定 \(\Omega>\max(0,-\ell)+1\)，可在
\[
h>0,\qquad \omega>\Omega,\qquad x+\omega>1\quad(x\in I)
\tag{3}
\]
内取同一个常值基端芽，使实际有限 \(M=T=0\)、frame \(I\to I\) 路径的联合成本满足
\[
\boxed{\mathcal L(\mathcal S)=\mathbb R^m.}
\tag{4}
\]
每个紧目标集有同一有限拼接类型中的光滑实际截面。还可用固定 Klein 闭合词同时准确闭合空间位移。

命题仅假设(2)，不假设全部 \(U\) 由 H 层张成。以下先证明存在 \(m=7\) 的明确固定读出满足(2)，再完成实际构造。

## 2. 完整 H 原式给七个不同真权的非零泛函

在 \(S_*=(1,1,1)\) 置
\[
v=u',\quad r=u'',\quad t=u''',\quad
Q=1+x^2,\quad L=v-xr,\quad E=ur-\frac{v^2}{2}.
\]
这里 \(E\) 仅为该局部多项式。

令 \(V_\gamma=\widetilde H_\gamma(S_*)\)、\(V_\delta=\widetilde H_\delta(S_*)\)。
R365 的完整式给
\[
\Lambda_u(V_\gamma)
=-\frac1{480}\int xQ^2LEt^2+\mathcal R_\gamma(u),
\qquad
\Lambda_u(V_\delta)
=\frac1{480}\int xQ^2rEt^2+\mathcal R_\delta(u),
\tag{5}
\]
其中两个余项都是该稿明确给出的同锚、五次、连续 \(C^2\) 泛函；全部 \(j_A,j_B,A_L,B_L\) 与真矩尾均在内。没有删除非紧 primitive 的左值。

采用原 R203 的真权投影 \(\Pi_\sigma\)。对 \(u_a(x)=u(x/a)\) 有
\[
\Lambda_{u_a}(\Pi_\sigma V)
=a^{\sigma-2}\Lambda_u(\Pi_\sigma V).
\tag{6}
\]
真权由完整有限表达式的正伸缩插值提取，不是只看局部最高导数。由于有限个固定伸缩在 \(C^2\) 上连续，对(5)的余项作任一真权提取仍是连续 \(C^2\) 泛函。

定义七个实际 \(U\) 元素：
\[
W_\sigma=
\begin{cases}
\Pi_\sigma V_\gamma,&\sigma=-7,-5,-3,-1,\\
\Pi_\sigma V_\delta,&\sigma=-6,-4,-2.
\end{cases}
\tag{7}
\]
R358 已给其中一项的完整准确式
\[
\boxed{\Lambda_u(W_{-7})=-\frac1{57600}\int r^5.}
\tag{8}
\]
其余六项由(5)及 \(xQ^2=x+2x^3+x^5\) 给以下准确三阶平方部分，表中每行另外保有连续 \(C^2\) 余项：

| 真成本权 \(\sigma\) | \(\Lambda_u(W_\sigma)\) 的三阶平方项 |
| --- | --- |
| \(-6\) | \( \frac1{480}\int x\,rE\,t^2\) |
| \(-5\) | \(-\frac1{480}\int x\,LE\,t^2\) |
| \(-4\) | \( \frac1{240}\int x^3rE\,t^2\) |
| \(-3\) | \(-\frac1{240}\int x^3LE\,t^2\) |
| \(-2\) | \( \frac1{480}\int x^5rE\,t^2\) |
| \(-1\) | \(-\frac1{480}\int x^5LE\,t^2\) |

例如 \(LEt^2\,dx\) 的伸缩次数为 \(-8\)；三个 \(x\) 幂给泛函次数 \(-7,-5,-3\)，对应成本权 \(-5,-3,-1\)。\(rEt^2\,dx\) 的次数为 \(-9\)，相应成本权为 \(-6,-4,-2\)。表格的1/480来自 \(\widetilde H_\delta=4H_2\)，没有误用 R362 的 H2 单独系数1/1920。

## 3. 一个真正相同的紧 profile 同时检出七项

不分别选择七个彼此无关的见证再默认其兼容。下面直接给一个共同见证。

取非零偶函数 \(\eta\ge0\)，支撑在 \([-a,a]\)，且 \(\eta(0)>0\)。取 \(b>3a\)，定义
\[
\bar r(y)=\eta(y)-\frac12\eta(y-b)-\frac12\eta(y+b).
\]
它的质量和一阶矩均为零。令
\[
\bar u=-J^2\bar r.
\]
所以 \(\bar u\) 是真紧、光滑、偶函数，并且 \(\bar u''=-\bar r\)。记 \(m_\eta=\int\eta>0\)，则
\[
\bar u(0)=\frac{b m_\eta}{2}-\int_0^a y\eta(y)\,dy>0,\quad
\bar u'(0)=0,\quad
\bar u''(0)=-\eta(0)<0.
\tag{9}
\]
三个不交 bump 还准确给
\[
\int(\bar u'')^5=-\frac{15}{16}\int\eta^5\ne0.
\tag{10}
\]

将整个函数平移到一个 \(x_0>0\)，并从一开始选小的 \(a,b,x_0\)，使其全部支撑位于 \(I\) 的正半部、右 collar 之前。记此函数为 \(u_0\)。在 \(x_0\) 有
\[
L_0=-x_0r_0>0,\qquad E_0=u_0r_0<0,\qquad r_0E_0>0.
\]
因此存在一个固定小窗口，使表中六个 \(t^2\) 系数全部严格为正。

选非零实 \(\chi\in C_c^\infty\) 支撑于该窗口，令
\[
u_N=u_0+N^{-5/2}\chi(x)\cos N(x-x_0).
\tag{11}
\]
则 \(u_N\to u_0\) 于 \(C^2\)，并且
\[
u_N'''=N^{1/2}\chi\sin N(x-x_0)+O(1).
\]
对表中任一正系数 \(a_\sigma(x,u,u',u'')\)，有限积分的标准振荡平均给
\[
\frac{\Lambda_{u_N}(W_\sigma)}{N}
\longrightarrow \frac12\int a_\sigma(x,u_0,u_0',u_0'')\chi^2>0,
\quad \sigma=-6,\ldots,-1.
\tag{12}
\]
所有连续 \(C^2\) 余项在(11)下有界，除以 \(N\) 后为零。与此同时，(8)、(10)及 \(C^2\) 收敛给
\[
\Lambda_{u_N}(W_{-7})\longrightarrow
-\frac1{57600}\int(u_0'')^5\ne0.
\tag{13}
\]
所以可以一次选定足够大但有限的整数 \(N\)，使同一个真实 \(u=u_N\) 满足
\[
B_\sigma:=\Lambda_u(W_\sigma)\ne0
\qquad(-7\le\sigma\le-1).
\tag{14}
\]
此后 \(N,u\) 全部固定；没有执行数值见证或取极限曲面。

## 4. 七个正缩放给准确 Vandermonde，且列来自 H 的真实像

取七个互异的 \(a_i\in(1/2,1)\)，固定
\[
u_i(x)=u(x/a_i),\qquad i=1,\ldots,7.
\tag{15}
\]
原支撑在正半部，故全部缩放仍位于 \(I\)；右侧可一次固定 R352 的三辅助包基，定义所有读出的同锚尾映射。辅助方案不随目标或几何路径更换。

对按 \(\sigma=-7,-6,\ldots,-1\) 排列的七列，(6)给
\[
\bigl(\Lambda_{u_i}(W_\sigma)\bigr)_{i,\sigma}
=\operatorname{diag}(a_i^{-9})
\,(a_i^{\,j})_{i=1,\ldots,7;\,j=0,\ldots,6}
\,\operatorname{diag}(B_{-7},\ldots,B_{-1}).
\tag{16}
\]
其行列式为
\[
\left(\prod_i a_i^{-9}\right)
\left(\prod_{\sigma=-7}^{-1}B_\sigma\right)
\prod_{i<j}(a_j-a_i)\ne0 .
\tag{17}
\]
这是真实七维秩的证明，不是把七个函数位置叫作秩。

还需证明(17)能由 H 状态实现，不能仅知道 \(W_\sigma\in U\)。R365 的完整正仿射协变给，在所有自然 \(\Lambda\) 的意义下，
\[
P_{H,0}\widetilde H_\delta(S)
\sim_\Lambda H\widetilde H_\delta(\widetilde S),\qquad
P_{H,0}\widetilde H_\gamma(S)
\sim_\Lambda H^2\widetilde H_\gamma(\widetilde S).
\tag{18}
\]
原有限真权投影 \(\Pi_\sigma\) 是有限个互异正 \(H\) 的该完整共轭的准确线性组合。因此每个 \(\mathcal L(W_\sigma)\) 都属于真实 H 值的线性 span。只需这一像空间结论；没有把 signed 投影本身称作实际正时长路径。

(17)、(18)遂证明(2)在 \(m=7\) 时成立。可以从全部实际 H 值中选出七个真实状态及速度方向 \(v_j=(v_{j1},v_{j2})\ne0\)，使
\[
c_j=\mathcal L\bigl(v_{j1}\widetilde H_\gamma(S_j)
+v_{j2}\widetilde H_\delta(S_j)\bigr),\qquad
A=(c_1,\ldots,c_7)
\tag{19}
\]
可逆。事实上可仅选单个 \(\gamma\) 或 \(\delta\) 方向；一般 \(v_j\) 的写法便于统一构造。

R365 还证明两个 H 读出在固定 \((h,d)\) 时不依赖独立的 \(k\)。因此对有限个(19)中的状态，可以重新取
\(\omega_j>\Omega+2,\ k_j=h_j\omega_j-d_j\)，而不改变 \(c_j\)。这个操作只用来从起点选择合法实际状态，不宣任意已冻结曲面的免费变换。由此(2)在(3)的共同物理域内真实成立。

## 5. 对一般满秩 m 选择实际快速段

以下对任意满足(2)的有限 \(m\) 证明(4)。选状态、\(v_j\) 使(19)的 \(m\times m\) 矩阵 \(A\) 可逆。取 \(w_j\in\mathbb R^2\) 使
\[
\det(v_j,w_j)=1.
\tag{20}
\]
固定同一个非零非负偶 \(\psi\in C_c^\infty((-1,1))\)，并记
\[
A_\psi=\int\psi(\psi')^2>0,\qquad
K_\psi=\psi\psi''-(\psi')^2 .
\]
真实 IBP 和奇偶性给
\[
\int\psi K_\psi=-3A_\psi,\qquad
\int\psi'K_\psi=0.
\tag{21}
\]

取参数 \(\sigma=(\sigma_1,\ldots,\sigma_m)\) 于一个固定小闭盒，取
\[
\tau=\epsilon^{3/2},\qquad s=\tau t,
\]
并从真实状态 \(S_j\) 指定
\[
\binom{\gamma}{\delta}
=\frac{\epsilon}{\tau}
\{v_j\psi(t)+\sigma_j w_j\psi'(t)\},
\qquad -1\le t\le1 .
\tag{22}
\]
积分 \(h,d\)，再真实解
\[
\omega_s=\frac{\omega\gamma-\delta}{h},\qquad k=h\omega-d,
\tag{23}
\]
以及原 frame 方程。由此所有 jets 来自同一实际水平路径，不是分别指定不相容导数。

状态变化、末 frame 和矩阵有一致含参数一导的界
\[
S-S_j=O_{C^1}(\epsilon),\qquad
F_{\rm out}-I=O_{C^1}(\tau),\qquad
M_{\rm micro}=O_{C^1}(\tau+\epsilon^2/\tau)
=O_{C^1}(\epsilon^{1/2}).
\tag{24}
\]
有限个初始状态均在(3)严格内部，所以一个共同的有限小 \(\epsilon>0\) 保整个段合法。第三历史可能很大，没有在(24)中被当作小量。

## 6. 完整局部密度的向量估计：全状态平方项恰为零

沿 R363，取原 R105/R130 的固定有限环境，逐分量将 \(\Lambda_{u_i}\) 线性延拓为 \(\ell_i\)，记向量 \(\ell\)。原实际 H 和加速度平方系数属于 \(U\)，故这些系数上的值不依赖延拓。

R350 的全状态结论给
\[
\ell(\overline A_{hh})=\ell(\overline A_{hk})
=\ell(\overline A_{kk})=0 .
\tag{25}
\]
原 R109、R129 在常值端 germs 之间的完整局部积分，准确为
\[
I_\ell=\int\{\ell(L_0)+Q_2^\ell
+[\lambda_\gamma(S)\gamma+\lambda_\delta(S)\delta]
(\gamma\delta_s-\delta\gamma_s)+Q_4^\ell\}\,ds.
\tag{26}
\]
其中 \(\lambda_{\gamma,\delta}=\mathcal L(\widetilde H_{\gamma,\delta})\)，两个 \(Q\) 为完整的速度二次、四次向量式。全部 \(N_0,N_2\)、原历史导数及 IBP 伙伴仍在(26)中。单个局部模板不被假设属于 \(U\)。

由(20)、(22)，面积准确为
\[
\gamma\delta_s-\delta\gamma_s
=\frac{\epsilon^2}{\tau^3}\sigma_jK_\psi .
\]
再用(21)、(24)，该快速段的 H 积分是
\[
\frac{\epsilon^3}{\tau^3}
\{-3A_\psi c_j\sigma_j+O_{C^1}(\epsilon)\}.
\tag{27}
\]
其它完整项分别为
\[
\int Q_4^\ell=O_{C^1}(\epsilon^4/\tau^3),\quad
\int Q_2^\ell=O_{C^1}(\epsilon^2/\tau),\quad
\int\ell(L_0)=O_{C^1}(\tau).
\]
因此
\[
I_\ell({\rm micro}_j)
=\epsilon^{-3/2}
\{-3A_\psi c_j\sigma_j+O_{C^1}(\epsilon)\}
+O_{C^1}(\epsilon^{1/2}).
\tag{28}
\]
所有常数均对固定参数盒一致。若只在基点消去(25)而非全状态精确消去，就可能留下更大的加速度平方项；本证明不用这种无效近似。

## 7. 回到同一基点，准确消 M/T，并保全部补桥成本

固定一个公共基端芽 \(S_B=(1,B,B)\)，\(B>\Omega+2\)。对每个 \(j\)，用 R354 加强的 R70 选择一条固定真实桥 \(B_j:S_B\to S_j\)，frame \(I\to I\)、\(M_{B_j}=0\)，始终保(3)。其真实第三与第四成本不设为零。

在 \(B_j\) 后接(22)。其实际末状态、frame 与矩阵由(24)趋于固定数据。再用同一个固定光滑桥族
\[
C_{j,\epsilon,\sigma_j}:
(S_{\rm out},F_{\rm out})\longrightarrow(S_B,I),\qquad
M_C=-M_{\rm micro}.
\tag{29}
\]
有限个桥族的辅助整数、拼接类型和紧参数盒先冻结；真实长度、状态及所需 jets 一致有界。它们的完整局部积分及参数一导为 \(O(1)\)。这包括 \(B_j\) 与所有返回桥基准，绝不把传入历史成本另设为零。

于是
\[
D_j=B_j\,{\rm micro}_j\,C_{j,\epsilon,\sigma_j}
\]
已有同一 scalar germ、frame I、总 \(M=0\)。现在才使用 R109：
\[
V_{D_j}-\int_{D_j}(v-\mathcal B_mN)\,ds\in R.
\tag{30}
\]
原累计的两份 response/history 项只是因 \(\ell(R)=0\) 在这些读出中消失，没有在非零 M 的短段上提前删除。因而
\[
\mathcal L(V_{D_j})
=\epsilon^{-3/2}
\{-3A_\psi c_j\sigma_j+O_{C^1}(\epsilon)\}
+O_{C^1}(1).
\tag{31}
\]

再接整块真倒行
\[
P_j=D_jD_j^{\rm rev}.
\]
原 R83 给
\[
M_{P_j}=T_{P_j}=0,\qquad V_{P_j}=2V_{D_j}.
\tag{32}
\]
第四成本同号加倍，第三准确相消；没有拿倒行当第四逆元。特别 \(2V_{D_j}\in U\)，所以(31)中的自然读出合法。所有物理下界和端芽保持。

依次连接有限个 \(P_j\)，令
\[
P_{\epsilon,\sigma}=P_1\cdots P_m .
\]
每块 M0/T0，所以完整成本准确相加。由(31)、(32)，
\[
\boxed{
\Phi_\epsilon(\sigma):=\mathcal L(V_{P_{\epsilon,\sigma}})
=\epsilon^{-3/2}\{-6A_\psi A\sigma+O_{C^1}(\epsilon)\}
+O_{C^1}(1).}
\tag{33}
\]
每个固定桥、真实累计 history 与完整局部低权项都在余项里；它们并不需要落在 H 的像中。

## 8. 有限参数同时解全部 m 个真实读出

设 \(K\subset\mathbb R^m\) 为任意紧目标集。把(33)乘 \(\epsilon^{3/2}\)，得到
\[
G_\epsilon(\sigma)=C\sigma+E_\epsilon(\sigma),
\quad C=-6A_\psi A,\quad
\|E_\epsilon\|_{C^1}\longrightarrow0 .
\tag{34}
\]
矩阵 \(C\) 可逆。取一次固定的小闭参数球。充分小但有限的 \(\epsilon>0\) 上，
\[
\sigma\longmapsto C^{-1}
\{\epsilon^{3/2}z-E_\epsilon(\sigma)\}
\tag{35}
\]
对全部 \(z\in K\) 都将该球严格映入内部，且导数范数小于1/2。因此它有唯一内点不动点 \(\sigma(z)\)，准确满足
\[
\Phi_\epsilon(\sigma(z))=z.
\tag{36}
\]
或者可用同一个非退化零稳定性表述。此处只用实际正 \(\epsilon\) 的一致 \(C^1\) 收敛，不要求把 \(\epsilon=0\) 加成光滑几何。

真实目标映射在每个正 \(\epsilon\) 上光滑；\(D_\sigma G_\epsilon\) 可逆，故隐函数定理给紧目标集邻域上的光滑 \(\sigma(z)\)。同一有限 \(\epsilon,\tau\)、同一有限桥整数与同一拼接类型同时适用于整个 \(K\)。

这一步说明为何 H 的满秩足够：所有其它坐标的实际误差都在这同一个 m 维观测目标中被有限 IFT 同时修正。它并没有推出观测以外的完整成本为零，也不要求余项分别落在 H 的线性像中。

## 9. 空间闭合与固定基准向量

frame I 不意味着位移零。按 R363/R210，在同一基端芽和物理下界内先固定两条 \(M=T=0\) frame 桥 \(C_1,C_2\)，其末 frame 为两个 Klein 半转 \(g_1,g_2\)。

使用 prototype 1 为 \(P_{\epsilon,\sigma}C_1\)、prototype 2 为 \(C_2\)，并采用原八边词
\[
1,2,1,2,2,1,2,1 .
\]
每种完整 prototype 在 \(\{I,g_1,g_2,g_1g_2\}\) 四个 ambient 左旋位置各出现一次；四矩阵之和为零，故各完整实际位移准确相消。scalar/frame germs 也闭合。

完整第四成本为
\[
V_X=4V_P+4V_{C_1}+4V_{C_2}.
\]
固定向量
\[
b=\mathcal L(4V_{C_1}+4V_{C_2})
\]
保留全部桥基准。对目标 \(z\) 在(36)取 \((z-b)/4\)，就有
\[
\boxed{
M_X=T_X=0,\quad X\ {\rm 空间/frame/scalar闭合},\quad
\mathcal L(V_X)=z,\quad h>0,\ \omega>\Omega.}
\tag{37}
\]
紧目标集仍有同一个有限光滑截面。所得为闭正则浸入数据；没有证明嵌入或 reach。

## 10. 本稿准确增加的结论与仍未支付的门

第2—4节给七个一次固定的真实 profile，且(17)证明它们的自然读出独立，并在实际 H 状态值上满秩。第5—9节遂给
\[
\boxed{(\Lambda_{u_1},\ldots,\Lambda_{u_7})(\mathcal S)=\mathbb R^7}
\]
以及含空间闭合、物理下界、完整桥成本的紧集光滑实际截面。

这排除了这七个读出的任何非零线性组合在整个实际成本集上必为单号。它不把其它可能的正性泛函排除，也不声称自然总通量商只有七维。

本稿没有使用全权 \(E(U)=E(R)\)——原 R333 只付其明确的零权等像。没有要求或宣称本模块免费保持 whole pure/whole self、当前 Gaussian 弱圆的完整第四门、其它 profile 通量或两条完整 period。若插入已有 hook 原型，M/T 可以保持，但其全部未列出成本需重新联合支付。

同一个 \(\sigma\) 家族中的构造几何可以改变度量；它不是主 README 所需的同一固定 g 的有限嵌入族。高阶收敛、全时间 C² 嵌入、连续全域 reach、宏观握持幅度仍未由此完成。后续继续完整 Q2/Q4 层、同规范 joint 与剩余 Gaussian 函数条件。
