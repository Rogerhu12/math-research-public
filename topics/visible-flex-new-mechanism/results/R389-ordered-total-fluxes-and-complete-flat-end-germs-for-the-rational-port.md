# R389：同一有理端口圆的整包通量、有序自然缺陷与全部零端 germ

日期：2026-11-15。**完整原式纸面证明；没有执行新的 profile 积分、符号程序、秩计算、科学运行或人工测试。**

[R326](R326-one-global-second-gauge-pays-the-complete-rational-port-and-preserves-joint-cost.md) 已用同一个全局二阶规范支付指定有理端口，却保留两个实际第四 period。[R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md) 的十三行系统以这两个完整目标已有真特解为前提；它不能代替 period 像的检查。

本稿付清其中一个此前没有显式原式的环节：在实际 whole pure 为零时，**整个 mixed period 的每包总通量**准确由自然读出的单包值与有序 $3+2$ 系数决定。该表达保留右方全部二阶尾，不假设自然通量在整个 $U$ 上局部，也不把新 Q4 的局部公式扩展到静态或 Q2。

由此得到两个具体后果。第一，这些整包 mixed 通量在原响应子空间 $\mathcal R\cap\ker\pi$ 上全部为零；它们不能由已经用于内部点的局部 whole-$E$ 核方向改变。第二，在 R345 已安装的 whole-$E=0$ 背景上，所有解析零端的真实逆 germ 光滑，当且仅当下文两组整包标量为零。平台仿射值、内部 Laurent 条件、两个全局特解及十三行同规范兼容均不因此自动支付。

## 1. 同一个实际圆、路径、锚与代价

固定 R324/R326/R327 的有理端口分支。整个实际闭几何满足
$$
M_B=0,\qquad T_B=\tau\mathfrak H,\quad \tau\ne0,\qquad
\pi V_B=0.
\tag{1}
$$
最后一项是实际 universal whole-period pure 身份，不能用 pure 像等号代替。
$\tau$ 是整条路径的第三 hook 系数，不是指定端口的曲率参数。

令 $u_1,\ldots,u_n$ 为按从左至右排列、值支撑严格不交且有正间隙的真实紧包，
$$
f=\sum_{i=1}^n a_i u_i,\qquad
g=\sum_{i=1}^n b_i u_i,\qquad a_i\ne0.
$$
所有真实有限复制、宽度、中心和最后有限频率已经固定。本稿不重新选择母函数，不改变这些实际数据。置
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
c_i(\theta)=a_i\cos\theta+b_i\sin\theta,
$$
$$
d_i(\theta)=a_i^2-c_i(\theta)^2,\qquad
R_i=a_i^2-b_i^2,\qquad T_i=a_ib_i.
$$
于是
$$
d_i=R_i\sin^2\theta-2T_i\sin\theta\cos\theta.
\tag{2}
$$
整圆的三个真实二次矩、完整第三 range 及同一个指定端口均按原稿保持。

采用共同右 collar $r_*$、原起点 $s_0$ 及
$J F(x)=\int_x^{r_*}F$。记
$$
Z_i=\operatorname{Range}H(Y_{u_i},Y_{u_i}),\qquad
C_{ij}=\operatorname{Range}H(Y_{u_i},Z_j),
$$
$$
\mathsf Z_{ij}=\mathscr P H(Z_i,Z_j),\qquad
Q_{ij}=\mathscr P H(Y_{u_i},C_{ij}).
\tag{3}
$$
$\mathscr P$ 是原完整 characteristic 周期，包含所有 $s$ 导数、$x$ 右积分及真实累计 history；不是 ruling 配对。单项可以带真左尾，不称其为独立的双 collar 控制场。

在此不交值包空间上，$\mathfrak H$ 的全部三槽为零，来源是原 $P,R,S$ 的常数/仿射左尾及对角 $\mathfrak H(u;u,u)=0$，见 [R292 §1](R292-zero-platform-periods-and-ordered-second-history-matrix.md)。所以所用三阶分解仍服从同一真实周期；没有在包间重置初值。

## 2. 从零平台身份升级到整个输出函数

[R288](R288-cross-packet-third-locality-and-automatic-canonical-first-end-layers.md) 的原 R56 恢复给
$$
i\ne j:\quad C_{ij}\text{ 的整个场局域于第 }i\text{ 包},\qquad
i>j:\quad C_{ij}=0.
\tag{4}
$$
这里 $i<j$ 时，$Z_j$ 在 outer 包上是真实仿射分子；局域性来自完整 $P,B,T_s$ 及原初值的共同消去，并没有把这个尾置零。

若 $k\ne i$ 且 $i\ne j$，(4) 给
$$
\mathscr P H(Y_{u_k},C_{ij})=0
\tag{5}
$$
作为全函数。对尚可能带尾的 $C_{ii}$，不能由(4)直接作同样推断。所缺一项由实际 pure 身份准确支付。

令 $q=\sum z_i u_i$，其中 $z_i$ 为原 universal 输入的实参数。
这些输入只用于原函数极化，不称为新的合法首阶圆或更换固定目标。
不同包的第一 forcing 交叉为零，故
$$
Z(q,q)=\sum_i z_i^2Z_i,\qquad
C(q;q,q)=\sum_{i,j}z_i z_j^2 C_{ij}.
$$
原 raw pure 是
$$
16\pi V_B(q)
=-\sum_{i,j}z_i^2z_j^2\mathsf Z_{ij}
-4\sum_{k,i,j}z_kz_i z_j^2
  \mathscr P H(Y_{u_k},C_{ij}).
\tag{6}
$$
由(1)，这是整个 $x$ 函数恒零。

对 $i\ne j$ 比较 $z_i z_j^3$：另一候选项
$\mathscr P H(Y_{u_j},C_{ij})$ 已由(4)为零，平方项也没有这种次数。因此
$$
\boxed{\mathscr P H(Y_{u_i},C_{jj})=0\quad(i\ne j).}
\tag{7}
$$
这比只在零平台比较更强；其原第三尾仍先保留，再由完整 pure 的一个真实系数消掉。

对角 $z_i^4$ 与有序 $z_i^2z_j^2$ 给
$$
\boxed{
\mathsf Z_{ii}=-4Q_{ii},\qquad
\mathsf Z_{ij}=-2Q_{ij}\quad(i<j).
}
\tag{8}
$$
第二式使用 $C_{ji}=0$。这两个式子同样是**整个输出**，不是只取左二次系数。

原 canonical mixed period 为
$$
V^0_\theta=-\mathscr P H(Z_D,Z_D)
+4\mathscr P H(Y_{\phi_\theta},C(\phi_\theta;D_\theta)).
\tag{9}
$$
把(5)、(7)、(8)逐项代入：对角系数为
$4(d_i^2+c_i^2d_i)=4a_i^2d_i$；
$i<j$ 的系数为
$4(d_i d_j+c_i^2d_j)=4a_i^2d_j$。
定义原 self 和有序交叉函数
$$
S_i=V_B(u_i^2,0)=-\mathsf Z_{ii}=4Q_{ii},
\qquad
U_{ij}=-2\mathsf Z_{ij}=4Q_{ij}\quad(i<j).
\tag{10}
$$
得到本稿的完整分解
$$
\boxed{
V^0_\theta(x)=
\sum_i a_i^2\left[
d_i(\theta)S_i(x)+\sum_{j>i}d_j(\theta)U_{ij}(x)
\right].
}
\tag{11}
$$
它保留了每一个实际右包、原顺序和全部自 history。

式(10)的两个函数是原成本本身的查询：
$S_i$ 是 self，
$U_{ij}=[a^2b^2]V_B((au_i+bu_j)^2,0)$。
因此不依赖把 $V_B$ 写成哪些路径生成元。上面的证明也可对实际路径作有限实线性组合后应用；pure 零只要求于最终组合，而不是要求每个组成路径各自 pure 零。

## 3. 真左尾为何不会在别的包的总通量中留下项

每个 $Q_{ij}$ 的 forcing $H(Y_{u_i},C_{ij})$ 局域于 outer 包 $i$。原 R56 在其左外域给
$B_H=T_s=0$、$P_H$ 为真实常数，其完整周期为
$$
\int_B(K_0+\lambda_s)P_H\,ds,
$$
所以是一个真实二次多项式；右外域为零。这包括 $i=j$，不要求 $C_{ii}$ 左紧。

因此(10)的 $S_i,U_{ij}$ 均满足
$$
\boxed{\text{outer 包右方为零；其左方为原二次多项式。}}
\tag{12}
$$
对任何真紧 $u$ 和二次多项式 $p$，
$$
\int u'''p=0.
\tag{13}
$$
三次分部积分的所有边项由 $u,u',u''$ 的真实零 jets 支付，而不是将 $p$ 改成零。

定义
$$
\omega_i(V)=\int u_i'''S_i,\qquad
\omega_{ij}(V)=\int u_i'''U_{ij}\quad(i<j).
\tag{14}
$$
由(12)—(13)，在第 $i$ 包上对(11)作总通量收缩时，其他 outer 包的全部项准确为零。因此
$$
\boxed{
\int u_i'''V^0_\theta
=a_i^2\left[d_i\omega_i+\sum_{j>i}d_j\omega_{ij}\right].
}
\tag{15}
$$
这里 $\int$ 可写为整个 $I$ 或 $u_i$ 所在闭包；紧 outer 使二者相同。不能把(15)中的右方和略去后直接写成 $a_i^2d_i\omega_i$。

## 4. 有序 $3+2$ 缺陷是同一个自然读出的实际系数

[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md) 定义了与辅助右包选择无关的自然读出
$$
\Lambda_u(V)=
\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)
-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\tag{16}
$$
其中 $\mathscr G$ 是原 pure 有序 $2+2$ 的完整三矩尾映射，不是任意补偿。
实际 $\pi V=0$ 先使所有真实右辅助包的 $2+2$ 输出为零；
三个真实矩向量张成后才得到 $\mathscr G_{V,u}=0$。
故在本稿范围
$$
\boxed{\Lambda_u(V)=\int u'''V(u^2,0).}
\tag{17}
$$
一般 $V$ 不能删除(16)后两项。

对 $i<j$，原 self 的准确展开是
$$
V((au_i+bu_j)^2,0)
=a^4S_i+a^2b^2U_{ij}+b^4S_j.
\tag{18}
$$
将 $au_i'''+bu_j'''$ 乘入(18)，再用(12)—(13)，只剩
$$
\boxed{
\Lambda_{au_i+bu_j}(V)
=a^5\omega_i+a^3b^2\omega_{ij}+b^5\omega_j.
}
\tag{19}
$$
特别
$$
\boxed{
\omega_i=\Lambda_{u_i}(V),\qquad
\omega_{ij}=[a^3b^2]\Lambda_{au_i+bu_j}(V).
}
\tag{20}
$$
没有额外的二倍极化因子。$a^2b^3$ 项为零，是因为 $U_{ij}$ 在右 outer 包上为零；不是因为交换了两个有序输入。

公式(19)也给可直接使用的准确缺陷
$$
\omega_{ij}=\Lambda_{u_i+u_j}(V)-\Lambda_{u_i}(V)-\Lambda_{u_j}(V).
\tag{21}
$$
但它不证明这个缺陷为零。本文不使用“自然读出局部”作为一般 $U$ 的未付假设。

### 4.1 右包依赖仍只经过原三矩

令
$$
\mu(u)=\left(\int(u'')^2,\int x(u'')^2,
\int[x^2(u'')^2+2(u')^2]\right).
$$
R352 的真实第二尾记为 $\mathscr T_n$；它的三条系数由同一 $m(s_0)=0$ 累积，并对 $n$ 线性。
对固定左包 $u$，
$$
\mathcal A_{V,u}(n)=
4\int u'''\,
\mathscr P H\!\left(Y_u,\operatorname{Range}H(Y_u,\mathscr T_n)\right)
\tag{22}
$$
按原实际路径线性组合解释。对真正位于 $u$ 右方的 $v$，
$$
\boxed{\omega^\to_{u,v}=\mathcal A_{V,u}(\mu(v)).}
\tag{23}
$$
该量对 $u$ 三次、对右矩 $n$ 一次。式(22)完整保留第三恢复的真实 $\beta$ 及其初值；可以直接使用 R292(17)—(22)，但不能只取其平台 $x^2$ 系数。

若换一种路径表示同一个 pure-zero 成本，(20)使(22)在三个真实右包矩基上相同，所以对全部 $n$ 相同。这个唯一性不宣称任意 $n$ 是单个实包的矩，也不作新数值秩。

所以本稿新通量与旧 $\mathcal T_B$ 平台矩阵不同：后者两槽都是二次矩，而(22)的左槽是一个真实三次 profile 泛函。whole self 零不能据此置它为零。

## 5. 两个实际 period 的整包条件：符号、幅度与真实规范

按 R326 的规范写
$$
V^0_\theta=\sin^2\theta\,V_d+
2\sin\theta\cos\theta\,V_e .
$$
由(11)，
$$
V_d=\sum_i a_i^2\left[R_iS_i+\sum_{j>i}R_jU_{ij}\right],
$$
$$
V_e=-\sum_i a_i^2\left[T_iS_i+\sum_{j>i}T_jU_{ij}\right].
\tag{24}
$$

设真实 incoming 矩阵给 $X=\Phi_{m_*}$。R326 使用唯一的
$w_c=-XD_\theta$，并保持原第三 Gram 规范。其实际周期为
$$
V_d^c=V_d-2\tau L_f(X\Delta),\qquad
V_e^c=V_e+2\tau L_f(X(f,g)).
\tag{25}
$$
R327 的两个目标准确是
$$
G_d=-V_d^c/(2\tau),\qquad G_e=-V_e^c/(2\tau).
\tag{26}
$$
不要混入 R225 采用 $(1-\cos2\theta,\sin2\theta)$ 时的另一组系数归一。

对第 $i$ 个活动包 $J_i=(\ell_i,r_i)$，置
$$
\mathcal F_i(G)=\int_{\ell_i}^{r_i} f'(x)G''(x)\,dx
=\int_{\ell_i}^{r_i}f'''(x)G(x)\,dx.
\tag{27}
$$
两次分部积分的端项由 $f',f''$ 全平消去；$G$ 可以有真实仿射平台。

原通量身份
$$
f'(L_fk)''=
\{A_f(f'k''-f''k')\}',\qquad
A_f=6f'f'''-2(f'')^2
\tag{28}
$$
给 $\mathcal F_i(L_fk)=0$，对任意全局光滑允许 $k$ 成立。
因此(25)不改变(27)。使用 $f'''=a_i u_i'''$，得到
$$
\boxed{
\begin{aligned}
\mathcal F_i(G_d)
&=-\frac{a_i^3}{2\tau}
 \left[R_i\omega_i+\sum_{j>i}R_j\omega_{ij}\right],\\
\mathcal F_i(G_e)
&=+\frac{a_i^3}{2\tau}
 \left[T_i\omega_i+\sum_{j>i}T_j\omega_{ij}\right].
\end{aligned}}
\tag{29}
$$
第三 Gram 不改第四 period。后续任意二阶 $k_\theta$，即使先不施十三行端口约束，也不能改变这些总通量。

故全部相位的每包总通量为零，准确等价于
$$
\boxed{
R_i\omega_i+\sum_{j>i}R_j\omega_{ij}=0,\qquad
T_i\omega_i+\sum_{j>i}T_j\omega_{ij}=0
\quad(1\le i\le n).
}
\tag{30}
$$
这是原实际成本的一组具体标量，不宣称其 $2n$ 个显示位置独立。

### 5.1 最右包与最右两包的明确门

因 $a_n\ne0$，$(R_n,T_n)$ 不可能同时为零。最右包没有右方尾，故(30)准确迫
$$
\boxed{\Lambda_{u_n}(V_B)=\omega_n=0.}
\tag{31}
$$
这不是 whole self 的尾读出，也不是一个内部退化点的部分积分。

若另有
$$
R_{n-1}T_n-T_{n-1}R_n\ne0,
$$
则倒数第二行的两式还迫
$$
\boxed{\omega_{n-1}=0,\qquad \omega_{n-1,n}=0.}
\tag{32}
$$
不满足这个实际非共线条件时，必须保留原两式，不能强行作此消元。

## 6. 整个纯零响应子空间对这些通量都不可见

[R344](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md) 严格证明
$$
\Lambda_u(K)=0\quad\text{对全部 }u,\ K\in\mathcal R .
\tag{33}
$$
现在取
$$
K\in\mathcal R\cap\ker\pi .
$$
它满足本稿从(6)开始的 whole pure 前提。由(20)、(33)，
$$
\omega_i(K)=\omega_{ij}(K)=0,
$$
继而(29)给
$$
\boxed{
\mathcal F_i(G_d[K])=\mathcal F_i(G_e[K])=0
\quad\text{对每个包 }i .
}
\tag{34}
$$
这里 $G[K]$ 指原固定 profiles 上的线性 period 读出；不为一个抽象响应重新安装几何。

因此，只要两条成本的差确实属于 $\mathcal R\cap\ker\pi$，它们的全部这些整包 mixed 通量相同。R345 的十一条局部 whole-$E$ 核列当然落在此子空间；其内部部分通量满射不能推出(30)可控。

**“纯零响应”在此严格指 $\mathcal R\cap\ker\pi$，不指任意 $V\in U\cap\ker\pi$。**
R370 的完整 Q4 已给真正的自然非零通道；按 R207 的已付 pure 像校正一个适当权 $-6$ 代表后，仍可有
$\Lambda_u(V)=\int x(u'')^5/80\ne0$ 而 $\pi V=0$。
这只是相应原成本空间的非零读出，不自动提供保持本稿固定圆所有门的实际几何。

同样，实际增强控制的 prototype、桥和有限复制都有完整基准成本。若重建实际路径时还改变了响应商部分，(34)不保证其总通量保持。不能把一条响应列的零导数当作整个实际联合实现的零成本。R385 目前的实际标量 $\Lambda$ 控制也没有声称保持 whole pure/self 或本稿所有行，故本文不借它宣布(31)已经可调为零。

## 7. whole self 支付平台后二次零端的准确 iff

现在再采用 R345 已实际安装的同一背景
$$
\mathcal Q(V_B)=0
\tag{35}
$$
作为 universal self 尾函数，而不是只在有限个母包上的查询。
此增强通常选定新几何；这里使用其真实 incoming $m_*$ 重取(25)，不继承另一个旧几何的成本。

由(10)、(18)，whole self 零使每个 $S_i$ 和 $U_{ij}$ 的真实左二次系数为零。配合(12)，它们的左尾至多仿射。因此(11)、(24)在每个共同零平台上给
$$
(V_d)''=(V_e)''=0.
\tag{36}
$$
原 R225(3) 的同一算子身份为
$$
(L_fk)''=(A_fk'')'-V_fk',\qquad
A_f=6f'f'''-2(f'')^2,\quad V_f=6(f''f''')'.
$$
在每个 $f=0$ 开平台上二者恒零，故 $(L_fk)''=0$；这不对 $p=f'$ 除法。于是(25)保留(36)。原共同右 collar 的零值和零导数一直按真实锚保持。

这没有将平台仿射值宣布为零。它准确支付的是原逆算子的 $G''=0$ 平台条件。

### 7.1 当前解析最细包的原端部类别

对 R327 的每个最细包，最终 profile 是 R281 的
$\psi$ 乘严格正解析 prefactor，包括有限 $N$ 的实际三角函数和有限修正。
靠每个零端，$p=f'$ 具有
$$
p(t)=t^{-2}a(t)e^{-c/t},\qquad c>0,\quad a(0)\ne0,
$$
方向号可以不同。$pA_f$ 在充分小单侧邻域不为零。

[R288](R288-cross-packet-third-locality-and-automatic-canonical-first-end-layers.md)
在这些逐包比例输入及(1)下已经由原 pure 身份消掉 canonical 第四 period 的一次指数层。
[R276](R276-canonical-fourth-periods-at-analytic-zero-ends-and-finite-first-layer-conditions.md)
的完整原恢复遂给每个端点
$$
G=P_e+p^2t^{-4}B(t),\qquad B\in C^\infty,
\tag{37}
$$
其中 $P_e$ 是真实平台多项式。由(36)，$P_e''=0$。
先对未加 $w_c$ 的 canonical 目标使用(37)，再由(25)加一个已知 $L_f$ 像；
这种加法不改变逆 germ 的光滑可延拓类。

### 7.2 左端分支与右端的真实累计常数

对任一目标 $G_d$ 或 $G_e$，记
$$
F_i(x)=\int_{\ell_i}^{x}p(t)G''(t)\,dt .
$$
原变参数式为
$$
k'(x)=p(x)\left(C+
\int^x\frac{F_i(t)}{A_f(t)p(t)^2}\,dt\right).
\tag{38}
$$
右端必须使用这个同一个 $F_i$，不能另扣 $F_i(r_i)$。

靠左端，定义本身给真实零通量分支。
式(37)与 R276 的加权原函数证明保证(38)可作 $C^\infty$ 延拓。
改变 $C$ 只加全平的 $p$，不影响该结论。

靠右端，若 $F_i(r_i)=0$，则
$$
F_i(x)=-\int_x^{r_i}p(t)G''(t)\,dt ,
$$
原右零分支同样由 R276 得到真正光滑延拓。
反之，若(38)有光滑延拓，原(28)在右零端的通量必须为零，
所以必有 $F_i(r_i)=0$。内部可能出现的 Laurent 失败不参与这一单侧必要性，也不被这里省略。

于是，在(1)、(35)及当前解析包范围内：
$$
\boxed{
\begin{gathered}
\text{两实际目标在全部零端的原逆 germ 均光滑}\\
\Longleftrightarrow
\mathcal F_i(G_d)=\mathcal F_i(G_e)=0\quad\forall i\\
\Longleftrightarrow \text{原有序标量系统(30)成立。}
\end{gathered}}
\tag{39}
$$
这是一条实际 canonical 目标的完整端部消元，不是“有限维所以可检”的存在性声明。它既没有假设 $\omega_{ij}=0$，也没有把未知端通量重新置零。

## 8. 接回 R327，仍须同一个 k

本稿已经把当前有理端口线路中的全部零端 germ 归到(30)的真实自然通量。任何一行不为零，都在施十三行端口约束之前阻断 period 像；特别(31)是最右包的明确门。

若(30)成立，whole self 已付平台二次条件，R276/R288 已付所有端 germ。
仍须对每个内部 $p$ 或 $A_f$ 零点支付 [R225](R225-complete-period-range-flat-end-germs-and-finite-observation-quotient.md) 的全部禁止 Laurent 项及 residue。
这些通过后，原全局平台连接和同右 collar 常数才构成真正的
$$
L_f k_d=G_d,\qquad L_f k_e=G_e.
$$
此处没有因平台只剩仿射就免费设定这些真特解。

得到特解后，还须对
$k_\theta^0=\sin^2\theta\,k_d+2\sin\theta\cos\theta\,k_e$
支付 R327 的实际十三行兼容：
三个第三合法矩、七个 $\sigma h^\ell$ 系数、三个 $Eh^j$ 系数，
并保相位光滑、种子及降秩点的准确整除。
其它全部几何段也仍使用同一个二阶 $k_\theta$ 和同一个第三规范。

本稿没有计算当前几何的 $\omega_i,\omega_{ij}$，没有证明整个系统(30)已有零解，
没有假设静态/Q2 的自然读出局部，也没有把实际 Q4 两号当成已完成的 whole-$E$ joint 控制。
新的实质结论是全函数有序分解(11)、真实 $3+2$ 通量接口(20)/(29)、
完整响应核的不可见性(34)，以及当前 analytic canonical 端 germ 的准确 iff(39)。
