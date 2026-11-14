# R37：真实闭合几何的全零二阶周期算子

日期：2026-11-14。独立完整存在证明。只作精确代数与有限维存在论证，不运行新的几何搜索。

**独立复核。** root 已全文核对，repo_sources 已独立核对整圈密度与真实长度、射影八维秩、完整扩展框架控制、连接成本独立 $N$、Klein 闭合、八维隐函数定理以及二阶 range 的适用范围；另以有理算术独立核得行列式 $63/2048$。这些审核没有把浸入或二阶可解扩大为嵌入的有限等距族。

**正向结论。** 存在 $C^\infty$、周期、正则的球面曲线 $B(s)$，以及周期正函数 $h(s)$ 和周期函数 $\omega(s)$，满足

$$\omega_s=\frac{k_s}{2h},\qquad \oint h^2T\,ds=0,$$

使实际八系数的完整二阶周期算子全部为零：

$$A_0=A_1=A_2=B_0=B_1=B_2\equiv0.$$

因此 R21 保留的“全算子为零”例外确能由真实闭合带几何实现。它不是任意指定八个形式系数，也不需要用数值小残差替代等式。

**仍未支付。** 构造给闭合正则中心曲线与周期浸入带，不保证嵌入、reach 或宏观握持位移。全零二阶算子允许完整二阶 profile 校正，但不等于已经存在某个固定非零参数下的精确有限等距族；三阶以后的相容性和收敛仍须解决。

## 1. 实际算子的点态矩阵密度

固定本题有向框架

$$T_s=kN,\qquad N_s=-kT-B,\qquad B_s=N,$$

并令

$$\alpha_s=h^2T,\qquad X(s,u)=\alpha(s)+uN(s),$$

$$z=\xi+\omega,\quad e=hz-k,\quad u=h/z,\quad
\mathscr K=kz^2-\frac{k^2+1}{h}z-\partial_s^2(z/h).$$

由 [R32](../results/R32-C3-phase-and-C2-second-correction-obstruction.md) 的完整积分身份，对任意二次多项式 $P$，

$$L[P](\xi)=\oint \frac{1+e^2}{4h}
\{-2kP+\mathscr K_\xi P'-\mathscr KP''\}\,ds.\tag{1}$$

花括号对 $\xi$ 恒常，因为 $\mathscr K_{\xi\xi}=2k$ 和 $P'''=0$。令 $M$ 为 $L$ 在基 $\{1,\xi,\xi^2\}$ 上的矩阵。

若某一段的 $k,h,\omega$ 都为常数，记 $d=h\omega-k$。则

$$\mathscr K=k\xi^2+\frac{k^2+2kd-1}{h}\xi
+\frac{(d+k)(kd-1)}{h^2}.$$

定义列向量

$$\mathbf w(h,d)=
\begin{pmatrix}(d^2+1)/(4h)\\ d/2\\ h/4\end{pmatrix},$$

$$\mathbf A(h,d)=
\begin{pmatrix}0\\1/h\\-2d/h^2\end{pmatrix},\qquad
\mathbf B(h,d)=
\begin{pmatrix}-2\\2d/h\\-2(d^2-1)/h^2\end{pmatrix}.$$

由 (1)，这一常值段的矩阵密度严格等于

$$\boxed{\quad
\mathbf w(h,d)\,\boldsymbol\ell(k,h,d)^T,\qquad
\boldsymbol\ell=(k^2-1)\mathbf A+k\mathbf B.
\quad}\tag{2}$$

具体地，

$$\boldsymbol\ell=
\begin{pmatrix}
-2k\\
(k^2+2kd-1)/h\\
-2(d+k)(kd-1)/h^2
\end{pmatrix}.$$

$\mathbf A,\mathbf B$ 线性无关，且
$\mathbf A^T\mathbf w=\mathbf B^T\mathbf w=0$。所以 (2) 的迹逐点为零。

这里把 $d$ 固定而改变 $k$，意味着相应常值 $\omega=(d+k)/h$ 也改变。后面会用真实的变 $h$ 连接准确实现这些 $\omega$ 端值，绝不在各段独立重置 $\omega$。

## 2. 三个完整球面圆周严格抵消

当 $k$ 为常数，框架 ODE 为

$$F_s=F\Omega(k),\qquad
\Omega(k)=
\begin{pmatrix}0&-k&0\\k&0&1\\0&-1&0\end{pmatrix}.$$

它是角速度 $\sqrt{1+k^2}$ 的旋转，因此在真实弧长

$$T(k)=\frac{2\pi}{\sqrt{1+k^2}}$$

后框架准确回到起点。$B_s=N$ 始终为单位向量，故这个闭球面圆周正则，包含 $k=0$ 的大圆。

选择

$$a^2=\frac{9+\sqrt{33}}8,\qquad a>1.\tag{3}$$

它满足

$$2(a^2-1)=\sqrt{1+a^2}.$$

固定任意 $(h,d)$，分别取 $k=0,+a,-a$ 的一个完整圆周，各段保持该 $(h,d)$。其三个真实积分矩阵相加为

$$\mathbf w\{
T(0)\boldsymbol\ell(0)+T(a)\boldsymbol\ell(a)
+T(-a)\boldsymbol\ell(-a)\}^T=0.\tag{4}$$

证明只是

$$T(0)\boldsymbol\ell(0)=-2\pi\mathbf A,\qquad
T(a)\{\boldsymbol\ell(a)+\boldsymbol\ell(-a)\}
=\frac{4\pi(a^2-1)}{\sqrt{1+a^2}}\mathbf A
=2\pi\mathbf A.$$

$\mathbf B$ 项因正负 $k$ 准确抵消。这里使用的是各圆周的真实不同长度，不是把三段错误地取成等长。

每个圆周可重复任意正整数 $N$ 次。对所有邻近参数，每次都按其实际周期 $T(k)$ 走完整圈，因而改变参数也不会产生一个随 $N$ 高速变化的末端框架角。

## 3. 四个状态提供准确的八维可逆修正

取四个固定状态

$$ (h_i,d_i)=(1,0),(1,1),(1,-1),(2,0).\tag{5}$$

第 $i$ 组三圈中保持 $k=0$ 不动，将另外两个曲率参数化为

$$k_{i,+}=a+\alpha_i+\beta_i,\qquad
k_{i,-}=-a-\alpha_i+\beta_i.$$

记八参数向量为 $\mathbf p=(\alpha_1,\beta_1,\ldots,\alpha_4,\beta_4)$，并令 $F_{\rm bulk}(\mathbf p)$ 为这十二个完整圆周各走一次的矩阵和。由 (4)，

$$F_{\rm bulk}(0)=0.$$

设

$$f_A(k)=\frac{2\pi(k^2-1)}{\sqrt{1+k^2}},\qquad
f_B(k)=\frac{2\pi k}{\sqrt{1+k^2}}.$$

$f_A$ 为偶函数、$f_B$ 为奇函数，因此

$$\partial_{\alpha_i}F_{\rm bulk}(0)
=c_A\,\mathbf w_i\mathbf A_i^T,\qquad
c_A=\frac{4\pi a(a^2+3)}{(1+a^2)^{3/2}}>0,$$

$$\partial_{\beta_i}F_{\rm bulk}(0)
=c_B\,\mathbf w_i\mathbf B_i^T,\qquad
c_B=\frac{4\pi}{(1+a^2)^{3/2}}>0.\tag{6}$$

这八个方向准确张成 $\mathfrak{sl}_3(\mathbb R)$。一个不依赖数值行列式的证明如下：若矩阵 $Y$ 在迹配对下消去所有八个方向，则 $Y\mathbf w_i$ 必须与 $\mathbf w_i$ 平行，因为 $\mathbf A_i,\mathbf B_i$ 张成 $\mathbf w_i$ 的零化平面。

四条 $\mathbf w_i$ 的射影代表可取

$$(1,0,1),\quad(2,2,1),\quad(2,-2,1),\quad(1,0,4).$$

前三个线性无关，第四个等于前三个的

$$7\mathbf w_1-\tfrac32\mathbf w_2-\tfrac32\mathbf w_3$$

（此式使用上述射影代表）。三个系数均不为零。因此一个同时保持这四条本征线的线性映射只能为标量矩阵。八个方向的正交补只有标量矩阵，故它们张成整个八维无迹空间。

另一个精确核验是：按矩阵逐行坐标删去 $(3,3)$ 项，把八列依次取为
$\mathbf w_1\mathbf A_1^T,\mathbf w_1\mathbf B_1^T,\ldots,
\mathbf w_4\mathbf A_4^T,\mathbf w_4\mathbf B_4^T$，所得有理 $8\times8$ 矩阵的行列式为

$$\frac{63}{2048}\ne0.\tag{7}$$

因此 (6) 的真实导数行列式是 (7) 乘上 $c_A^4c_B^4$，严格非零。

## 4. 同时匹配 frame、h、k、omega 的有限平滑连接

**连接引理。** 给定两个端点框架 $F_0,F_1\in SO(3)$，以及两端常值状态
$(k_0,h_0,\omega_0)$、$(k_1,h_1,\omega_1)$，其中 $h_0,h_1>0$，存在有限长度的光滑连接，满足

$$F_s=F\Omega(k),\qquad h>0,\qquad
\omega_s=\frac{k_s}{2h},$$

并在两端开放邻域与相应常值状态一致。对于任一固定的端点数据，这种连接可在其一个邻域内按数据光滑选择。连接的长度、全部有限阶几何积分及其参数导数均有限。

**证明。** 先忽略 $h,\omega$。R31 §5 的框架控制证明只用 $k=0,1$ 的正时长平台，任意目标均可由完整周期、Euler 词和一个满秩恒等词实现；平滑过渡后，有限维隐函数定理恢复准确端点。若这里的端值 $k_0,k_1$ 为负数，可先后用固定长度的光滑端帽接到 $0$，再把中间框架目标按这些端帽的实际增量调整。中间控制不受影响。

在中间另插一段固定的非恒定光滑 $k$，使其中有两个互不相交的开放子段 $I_+,I_-$，分别满足 $k_s>0$、$k_s<0$。它产生的固定框架增量同样由后面的框架词准确补偿。满秩端点词确保整个 $k$ 路径及其端帽可在给定数据附近光滑选择；预留的 $I_\pm$ 保持固定。

现在处理 $h,\omega$。选择一个光滑正函数 $b_0(s)$，在两端分别等于 $1/(2h_0)$ 和 $1/(2h_1)$。在 $I_\pm$ 内选择非负、不恒零、紧支撑的光滑函数 $\chi_\pm$，令

$$\frac1{2h}=b_0+\eta_+\chi_++\eta_-\chi_-,\qquad
\eta_+,\eta_->0.$$

框架路径完全不依赖 $h$，而 $\omega$ 的准确增量是

$$\omega_1-\omega_0
=I_0+\eta_+A_++\eta_-A_-,$$

$$I_0=\int k_sb_0\,ds,\qquad
A_\pm=\int k_s\chi_\pm\,ds,\qquad A_+>0,\quad A_-<0.$$

先取足够大的固定 $\eta_->0$，即可解出严格正的 $\eta_+$ 来匹配任意指定增量。之后在端点数据的小邻域内，用同一条线性公式光滑选择 $\eta_+$；严格正性保持。$h$ 因而始终光滑且正。

最后定义
$\omega(s)=\omega_0+\int_0^s k_\sigma/(2h)\,d\sigma$。它的右端值准确为 $\omega_1$，并因两端 $k$ 为常数而在两端开放邻域恒定。$h,k,\omega$ 的全部端点 jet 都与指定常值芽匹配。有限个平台的长度和形状依赖参数光滑；变长度积分可缩放回固定区间，因此所需积分及参数导数也光滑有限。证毕。

该引理不是给每一段任意选择新的 $\omega$ 规范。它以同一条真实微分方程，从上一段的实际端值连续到达下一段的指定端值。全局的变 $h$ 连接正是克服“恒 $h$ 时 $\omega=k/(2h)+$常数”限制的必要自由度。

## 5. 连接成本与整圈重复次数真正分离

取固定起始框架 $F_*=(T_*,N_*,B_*)$，起始标量状态为

$$(k,h,\omega)=(0,1,0).$$

对八参数 $\mathbf p$ 在零点附近，按固定顺序安排 §3 的十二个常值圆周状态，每个状态重复 $N$ 个完整周期。其常值 $\omega$ 始终取

$$\omega_{i,j}=\frac{d_i+k_{i,j}}{h_i}.$$

每个圆周从 $F_*$ 开始，并准确返回 $F_*$。在相邻状态间应用 §4，使用从 $F_*$ 到 $F_*$ 的连接；第一段、最后一段也用连接匹配上述起始标量状态。

这些连接仅依赖八参数和相邻状态，**不依赖 $N$**。所有长段的末框架对每个参数都已是准确的 $F_*$，因此没有一个被隐藏的、导数大小随 $N$ 增长的端角纠正。

先让最后一条连接准确回到 $F_*$ 及起始标量状态，形成一个共同闭框架块。然后分别接上两条固定的扩展框架桥，从 $F_*$ 到 $g_1F_*$ 或 $g_2F_*$，其中 $g_1,g_2$ 为绕两个垂直固定空间轴的半周旋转；这两桥的标量起终状态都为 $(0,1,0)$。得到两条路径 $P_1^{(N)}(\mathbf p),P_2^{(N)}(\mathbf p)$。它们的标量状态均准确从 $(0,1,0)$ 回到同一状态，全部端点 jet 一致。

用 $G_j(\mathbf p)$ 记第 $j$ 条路径中所有连接段的矩阵密度积分之和，则路径的总矩阵为

$$N F_{\rm bulk}(\mathbf p)+G_j(\mathbf p).\tag{8}$$

$G_j$ 及其参数导数光滑、有界，且与 $N$ 无关。这比仅声称某种连接误差在数值上较小更强。

## 6. Klein 四元群给精确空间闭合

取

$$\mathcal G=\{I,g_1,g_2,g_3=g_1g_2\},\qquad
\sum_{g\in\mathcal G}g=0.$$

与 R31 相同，使用 Cayley 图的八边 Euler 词

$$g_1,g_2,g_1,g_2,g_2,g_1,g_2,g_1.$$

在顶点 $g$ 取第 $j$ 类边时，放入旋转后的整条路径
$gP_j^{(N)}(\mathbf p)$。每一类路径恰在四个群顶点各出现一次。端点框架与标量状态完全相接，因此 $B,h,\omega$ 得到真正的光滑周期数据；特别地 $\omega$ 回到同一值，$\oint k_s/(2h)\,ds=0$ 准确成立。

记未旋转第 $j$ 条路径的中心线位移为

$$V_j(\mathbf p,N)=\int_{P_j^{(N)}} h^2T\,ds.$$

完整曲线的位移严格等于

$$\sum_{g\in\mathcal G}gV_1+\sum_{g\in\mathcal G}gV_2=0.$$

故 $\alpha_s=h^2T$ 给一条 $C^\infty$ 闭合正则曲线。这个闭合等式对所有邻近八参数和每个正整数 $N$ 都成立，不需要与后面的八个算子方程争用参数。

矩阵密度只依赖标量 $k,h,\omega$ 及其导数，故在空间旋转下不变。全周期的实际矩阵于是准确为

$$M_{\rm total}(\mathbf p,N)
=8N F_{\rm bulk}(\mathbf p)+4\{G_1(\mathbf p)+G_2(\mathbf p)\}.\tag{9}$$

实际几何的 $D=0$ 恒等式给
$\operatorname{tr}M_{\rm total}=p_0+2s_1-4t_0=2D=0$。$F_{\rm bulk}$ 本来逐点无迹，因此 $G_1+G_2$ 也为无迹矩阵；下面确实是八个方程，不是遗漏了第九个标量条件。

## 7. 八维隐函数定理给有限 N 的精确零算子

定义光滑映射到 $\mathfrak{sl}_3(\mathbb R)$：

$$\Phi(\mathbf p,\varepsilon)
=F_{\rm bulk}(\mathbf p)
+\frac{\varepsilon}{2}\{G_1(\mathbf p)+G_2(\mathbf p)\}.$$

由 §2–3，

$$\Phi(0,0)=0,\qquad
D_{\mathbf p}\Phi(0,0)=D F_{\rm bulk}(0)
$$

为可逆的八维线性映射。普通有限维隐函数定理给某个 $\varepsilon_*>0$ 以及光滑参数
$\mathbf p(\varepsilon)=O(\varepsilon)$，使

$$\Phi(\mathbf p(\varepsilon),\varepsilon)=0
\qquad (|\varepsilon|<\varepsilon_*).$$

现在选择任意充分大的**有限整数** $N$，使 $\varepsilon=1/N<\varepsilon_*$，并把上述实际几何参数取为 $\mathbf p(1/N)$。(9) 便给

$$M_{\rm total}(\mathbf p(1/N),N)=0.$$

这不是把一个 $N\to\infty$ 的退化极限当成真解：每个充分大的有限 $N$ 都有一组准确修正后的参数。连接的严格正 $h$ 条件在小参数邻域内保持，所以最终几何仍光滑正则。

由 R31 的矩阵对应，

$$M=\begin{pmatrix}
p_0&2r_1&-4r_0\\
p_1&2s_1&-4s_0\\
p_2&2t_1&-4t_0
\end{pmatrix}.
$$

因此 $M=0$ 迫全部实际八个自由系数以及相应的第九个相关坐标为零。R7 的其余恒等式给

$$A_0=A_1=A_2=B_0=B_1=B_2\equiv0,$$

完整二阶周期表达式 $\mathcal O_\phi$ 对每个光滑 profile 都恒等为零，证明了开头的正向结论。

## 8. 真实物理带及已支付的二阶校正

最终 $h,\omega$ 周期连续，且 $h>0$。选一个共同的有限区间 $[\ell,r]$，使 $\xi+\omega(s)>0$ 对全部 $s,\xi$ 成立；例如在所有 $-\omega(s)$ 的上界之上再留正余量。于是

$$u=\frac{h}{\xi+\omega}>0$$

给真实光滑的周期物理带。对 $X=\alpha+uN$，

$$X_s=(h^2-ku)T-uB,\qquad X_u=N,$$

所以

$$|X_s|^2=(h^2-ku)^2+u^2>0,\qquad X_s\cdot X_u=0.$$

这准确给周期浸入带，不需要用采样验证秩。

按既有 [三矩与完整 range 证明](../notes/literature-second-order-moments-20261114.md)，在任意更小的活动区间可选择非零 $C^\infty$ 紧支撑 profile $f,g$，使其三矩相同且交叉三矩为零；于是
$\phi_\theta=\cos\theta\,f+\sin\theta\,g$ 保持三矩。

现在对 forcing $H_\theta=dY_f^2-dY_{\phi_\theta}^2$，每条 ruling 的全积分由这三个矩相同而为零，所以从一侧 collar 锚定的法向坐标分量在另一侧 collar 也准确为零。剩余的整个沿 $s$ 周期函数条件则由本稿的全零算子自动支付。因此可用既有完整 range 公式恢复对 $\theta$ 光滑的 $C^\infty$ 二阶校正，并选择齐次 gauge 使两侧 collar 都为零。这里 $B_j$ 全部退化，三总矩是另外显式支付的，绝不是从 $O=0$ 自动推出的。这是真实线性方程的解，已不只是把非零周期残差投影掉。

仍须区分：这是二阶等距路径的可解性。它没有自动支付三阶以后的周期障碍，没有证明形式级数收敛，也没有把两个离散等距像或有限精度 Newton 切片冒称为连续有限族。

## 9. 对后续构造的边界

本证明给实际曲线上的零算子，保留并实现了 R21 的例外；因此不能再把此前有限设计未搜到零算子当成该分支不存在的证据。

证明没有提供最小可用 $N$、数值曲线、嵌入或 reach 证书。连接中为控制 $\omega$ 可能需要较小 $h$，重复整圈也可能产生自交或很差的尺度比例。这些都不影响本稿所声明的周期浸入与二阶相容存在，但它们是完成本课题前还必须实际解决的不同问题。

下一步的数学任务是检查这个全零基底上的第三及更高阶 range 条件，或寻找能把该相容结构提升为真正有限族的精确参数化；闭面嵌入、固定握持区、宏观位移和统一 reach 仍未完成。

## 10. 精确代数附件的范围

脚本 [literature_zero_operator_certificate.py](../scripts/literature_zero_operator_certificate.py) 仅使用 Python 的有理数算术，核对四状态的无迹方向、(7) 的准确有理行列式、四本征线关系，以及数域 $\mathbb Q(\sqrt{33})$ 中的圆长抵消恒等式。小型输出为 [literature-zero-operator-exact-certificate-20261114.json](../notes/literature-zero-operator-exact-certificate-20261114.json)。

该附件没有求一个实际数值的 $N$ 或修正参数，没有运行曲线 ODE、几何优化、嵌入或 reach 计算。§4–7 的真实连接和有限 $N$ 存在结论来自正文证明，而不是从附件外推。

