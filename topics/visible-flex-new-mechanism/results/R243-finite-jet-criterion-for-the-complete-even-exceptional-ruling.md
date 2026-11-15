# R243：例外端芽完整 ruling 偶部的有限字、线性 ODE 与准确有限 jet 判据

日期：2026-11-15。**完整纸面证明；没有新的符号目标、profile 积分、几何计算或研究运行。**

本稿把例外端芽的整个 ruling 偶部一次化为有限判据，不再逐次添加大参数渐近的必要层。所保留的函数包括真实两重 s history、全部局部恢复、链式项及共同右锚 profile 尾。有限表示允许冗余；判据不要求它们逐个线性独立，也不把所有表示系数分别置零。

来源：[R56 原分子恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 八矩与真实第三 history](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R221 完整 gauge ruling](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R224 偶部商](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)、[R227 例外端芽](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)、[R231 完整领先项](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)及 [R241 完整下一层](R241-complete-sigma-four-layer-and-resonant-exceptional-germs.md)。

## 1. 固定对象与主结论

固定

$$
h=h_eH,\qquad H(\sigma)=e^{\varepsilon\sigma^2},\qquad
k=k_e(1-2\varepsilon\sigma^2),\qquad
\omega=k_e/h,
\quad h_e>0,\ \varepsilon>0,\ k_e\ne0.
\tag{1}
$$

取同一个正 profile 区间 $I=[\ell,r]$，使 $x+k_e/h_e>0$，以及已付低阶 range 的同锚三矩圆

$$
\phi_\theta=\cos\theta f+\sin\theta g,\qquad
D_\theta=f^2-\phi_\theta^2.
$$

所有 profile 均有固定双零 collar。原二、三阶传入场取自实际完整路径，不先置零。按 R224、R227、R231 的中心比较，原 ruling 偶部与同中心、同右锚的中心化模型 $\widehat{\mathscr K}_\theta$ 满足

$$
[\operatorname{Ev}\mathscr K^0_\theta]
=[\widehat{\mathscr K}_\theta]\pmod{\mathcal W_e},\qquad
\mathcal W_e=\operatorname{span}\left\{
h_eH,\ \sigma^2,\ \frac{1+4\varepsilon^2k_e^2\sigma^4}{h_eH}
\right\}.
\tag{2}
$$

这里引用的是已证的完整比较：二阶中心初值、相应第三初值及二阶初值的平方项一起处理；不是分别删除其中任意一项。任意合法二阶 gauge 的偶部响应亦在 $\mathcal W_e$，第三 gauge 的像就是原三矩像在该 germ 上的限制。

**完整有限判据。** 从 R56 的二、三阶原始递推及第四 ruling 公式，可以构造一个有限的整数对角矩阵 D、常数严格三角矩阵 N、一个固定初值向量 $X_0$ 和有限维系统

$$
X'=(N+2\varepsilon\sigma D)X,\qquad X(0)=X_0,
\qquad n:=\dim X,
\tag{3}
$$

使整个中心 ruling 及 (2) 的三列都是 X 的常行输出。ruling 输出行的条目是原 profile 的真实四次泛函；它们保留所有跨包尾和嵌套右原函数。

对每个实际相位谐波，先用其 Taylor 系数 $y_0,y_2,y_4$ 唯一减去 (2) 的一个元素，得到余函数 F。令

$$
\boxed{B_n=\frac{n(n+1)}2-1.}
\tag{4}
$$

则准确有

$$
\boxed{
F\equiv0
\quad\Longleftrightarrow\quad
F^{(j)}(0)=0\quad(0\le j\le B_n).
}
\tag{5}
$$

F 为偶函数，故实际只需其中的偶阶；0、2、4 阶已经由唯一三列校正支付。若按一个通用程序构造 n，(4) 是显式上界，不要求寻找最小系统维数或证明生成函数独立。

结论是**整个偶部在 $\mathcal W_e$ 中的充要判据**。它不是整个闭路径第四 ruling、第四 period 或同一个二阶 gauge 的 joint 可解性定理。原始 forcing 仍须保留所有 0、2、4 相位谐波；R231、R237、R241 某些领先层只有两个谐波，不将此性质外推到整个 ruling。

## 2. 原始递推中的 s-history 长度最多为二

令 $\mathcal A=\mathbb R[\sigma,H,H^{-1}]$。系数可依赖固定的 $h_e,k_e,\varepsilon$；本节的整数幂只指 $\sigma,H$ 的幂。

沿 (1)，$h,k,\omega$ 及其任意指定有限阶 s 导数都在 $\mathcal A$。R56 的原分子式已准确消掉 $1/z$：其 $P,B,\mathcal R_H,\eta_0$ 与恢复分子，只使用这些 Laurent 多项式系数、profile 的有限乘积、x 导数以及同一个右锚原函数。frame 不需要另设无限维变量，因为全部 forcing 用真实正交分量内积，协变导数中的矩阵只含 k。

第一阶分子不含 s history。第二阶恢复为

$$
Z_2=K_2-Y_{W_2},\qquad
W_2(\sigma,x)=\Phi_{m(\sigma)}D_\theta,\qquad m'=M_{\rm raw},
\tag{6}
$$

其中 $K_2$ 是 R56 的完整局部恢复。R73 逐点八矩闭合说明每个 $M_{\rm raw}$ 坐标在 $\mathcal A$。因此 m 的非恒定部分只含一重 s 积分。

第三 forcing 是第一场与整个第二场的双线性配对。对第二 history 的真实 s 导数用 $m'=M_{\rm raw}$ 替换；局部恢复及 R73 的 $\Psi$ 链式项都必须保留。这样第三 characteristic 密度的每个几何系数具有准确形式

$$
a(\sigma,H)+\sum_i b_i(\sigma,H)m_i(\sigma),
\qquad a,b_i\in\mathcal A.
\tag{7}
$$

其真实积分 $W_3$ 最多含二重 s 积分。第三恢复分子又是 $W_3$、m 及局部系数的线性组合，不增加积分层数。

最后第四 **ruling** 由 R56(4) 给出，是第二场的二次配对及第一场与第三场的双线性配对。因此几何系数只需

$$
\mathcal A,\qquad \mathcal A m_i,\qquad
\mathcal A m_im_j,\qquad \mathcal A W_{3,a}.
\tag{8}
$$

没有在此再积分第四 characteristic 密度；那是另一个 period 问题。式 (7)、(8) 也没有假设局部三次密度是总导数或属于任何已知控制空间。

若保留实际中心初值，它们只添加更短 history 的项，长度上界不增加。为了使用原偶部比较，本文最终按 (2) 将这些完整组合收入同一个三矩空间；不是利用长度论证自行删去初值。

## 3. 有限指数字的准确表示

对整数 $r\in\mathbb Z$、$d\in\mathbb Z_{\ge0}$ 定义 letter

$$
\ell_{r,d}(\sigma)=\sigma^dH(\sigma)^r.
$$

对有限字 $w=(\ell_1,\ldots,\ell_L)$，采用外层在前的同中心积分

$$
I_\varnothing=1,\qquad
I_{(\ell_1,w')}(\sigma)=\int_0^\sigma\ell_1(t)I_{w'}(t)\,dt.
\tag{9}
$$

所有这些函数都是整函数。这里只整理真实中心积分，未更换 profile 的右锚 r。

一重积分的乘积满足原积分恒等式

$$
I_{(\ell_a)}I_{(\ell_b)}
=I_{(\ell_a,\ell_b)}+I_{(\ell_b,\ell_a)}.
\tag{10}
$$

证明只需微分两边并核共同零初值；因此适用于本稿真实积分，不是用形式 shuffle 代替实际 history。

由 (6)–(10)，整个 ruling 可以写为有限和

$$
\widehat{\mathscr K}_\theta(\sigma)
=\sum_\alpha c_{\alpha,\theta}\,
\sigma^{a_\alpha}H^{r_\alpha}I_{w_\alpha}(\sigma),
\quad a_\alpha\ge0,\quad r_\alpha\in\mathbb Z,\quad |w_\alpha|\le2.
\tag{11}
$$

这里 $c_{\alpha,\theta}$ 来自完整 R56 原式，包括最后真实 x 积分。它们一般是**带右 Volterra 尾的非局部四次泛函**，不能未经新证明换成逐微包局部 bulk。不同微包之间的二阶尾与第三嵌套交叉仍包含在这些系数中。

相位依赖按原四次齐次结构收集到

$$
1,\quad\cos2\theta,\quad\sin2\theta,\quad
\cos4\theta,\quad\sin4\theta.
\tag{12}
$$

种子处可有已知线性关系，但保留全部五项始终 sound。若某项已由完整原式消掉，可在之后引用该身份；不能只因其领先渐近项消掉就删去。

此外

$$
I_w(-\sigma)=(-1)^{\sum_{i=1}^{|w|}(d_i+1)}I_w(\sigma).
\tag{13}
$$

故 (11) 的偶部可以按每一单项的准确奇偶性选取。该操作不删除任何尾或初值影响。对于已用 (2) 中心化的偶模型，仍可显式取此投影以避免依赖未经登记的进一步对称性。

## 4. 一次有限微分闭包给线性系数系统

把 (11) 的每个单项标记为三元组 $(a,r,w)$，对应

$$
X_{a,r,w}=\sigma^aH^rI_w.
$$

其导数准确为

$$
\begin{aligned}
X_{a,r,w}'={}&2\varepsilon r\sigma X_{a,r,w}
+aX_{a-1,r,w}\\
&+X_{a+d_1,r+r_1,w'}
\quad\text{若 }w=(\ell_{r_1,d_1},w').
\end{aligned}
\tag{14}
$$

第二项在 $a=0$ 时省略，最后一项在空字时省略。

从原有限单项清单开始，加入 (14) 需要的三元组，直到闭合。此过程必有限：导数边若不缩短 word，就严格降低 a；缩短 word 最多发生两次，其间 a 只会增加该有限字已有的 d。一个完全显式的保守清单是：对起始 $(a,r,w)$、$|w|=L$，加入每个后缀 $w_j$ 及

$$
\left(b,r+\sum_{i=1}^j r_i,w_j\right),
\qquad 0\le b\le a+\sum_{i=1}^j d_i,\quad 0\le j\le L.
\tag{15}
$$

重复三元组合并即可。一个起始项贡献的状态数不超过

$$
\sum_{j=0}^L\left(a+\sum_{i=1}^j d_i+1\right).
\tag{16}
$$

再加入三矩空间所需的

$$
(0,1,\varnothing),\quad(2,0,\varnothing),\quad
(0,-1,\varnothing),\quad(4,-1,\varnothing)
\tag{17}
$$

及其闭包；(17) 最多增加九个不同状态。因此 n 可由原有限清单及 (15) 直接计数，本稿没有虚构已运行的 n 或秩。

将状态按 word 长度、再按多项式次数作兼容排序。式 (14) 的非对角边都严格下降，因此得到 (3)：D 的对角元是各 r，N 是常数严格三角矩阵，其非零条目来自 a 与 1。D、N 的构造不依赖 profile 数值。H 的归一化令初值特别简单：空字且 $a=0$ 的分量为 1，其余分量为 0。

本系统不宣称 X 的各分量作为函数独立。原函数、shuffle、重复指数或其他关系均可以使某个非零常行 c 满足 $cX\equiv0$；下节正是允许这种情况的准确零判据。

## 5. 多项式线性系统的消失阶引理

**引理。** 设

$$
Y'=A(\sigma)Y,\qquad A(\sigma)=A_0+\sigma A_1,
$$

是 n 维实解析系统，c 是常行。对任意一个解析解 Y，若 $cY$ 不是零函数，则

$$
\operatorname{ord}_0(cY)\le \frac{n(n+1)}2-1.
\tag{18}
$$

证明分四步，特别不以系统分量独立为前提。

**第一步：有理行秩与有限首段。** 定义多项式行

$$
R_0=c,\qquad R_{j+1}=R_j'+R_jA.
\tag{19}
$$

则 $\deg R_j\le j$。c 为零时结论平凡；否则令 r 为这些行在 $\mathbb R(\sigma)$ 上张成的秩。必有 $1\le r\le n$，且首 r 行 $R_0,\ldots,R_{r-1}$ 独立。

后一事实不能只假定：若首次依赖发生在第 k 行，则 $R_k$ 是前 k 行的有理组合。对该关系微分，再加右乘 A，表明 $R_{k+1}$ 仍在前 k 行的有理 span；归纳给全部后继。因此首次依赖时所得秩就是最终秩。

置

$$
\Omega=R_0\wedge\cdots\wedge R_{r-1}\ne0.
$$

每个非零 r 阶 minor 的次数不超过

$$
d_r=0+1+\cdots+(r-1)=r(r-1)/2.
\tag{20}
$$

令 $\nu$ 为这些 minor 在 0 点消失阶的最小值，则 $0\le\nu\le d_r$。

**第二步：实际输出解空间恰为 r 维。** 取满足 $\Phi(0)=I_n$ 的解析基本解矩阵。所有输出解组成

$$
\mathcal F=\{\sigma\mapsto c\Phi(\sigma)v:\ v\in\mathbb R^n\}.
$$

其维数恰为 r。确切地，在某个避开非零 minor 零点及有理关系分母零点的邻近点 $\sigma_*$，首 r 行给秩 r 的初始导数映射。由 (19) 的依赖关系，输出满足一个首项系数为 1、系数在 $\sigma_*$ 附近解析的 r 阶标量 ODE；故前 r 个初始值为零当且仅当整个局部输出为零，再由解析性延回 0。于是零输出初值空间恰有维数 $n-r$，所述输出空间维数正是 r。

这也说明不能用一个形式行秩直接略过真实输出空间的论证。

**第三步：Wronskian 的共同消失阶。** 所有 r 阶输出 Wronskian 是

$$
\Omega\,\bigwedge^r\Phi
\tag{21}
$$

的各坐标。$\bigwedge^r\Phi$ 在 0 点解析可逆，故乘它不改变这些坐标的共同最小消失阶：若每个原坐标被 $\sigma^\nu$ 整除，乘积亦然；用其解析逆反推，不能多一个共同因子。因此 (21) 的共同消失阶仍为 $\nu$。

任意 r 个独立输出函数都是 $\mathcal F$ 的实常系数基。两组这样的基之间由常数可逆矩阵联系，非零 Wronskian 只差一个非零常数。故它们的消失阶都恰为 $\nu$，并非仅存在一组特别的取值基。

**第四步：适配消失阶的函数基。** 在 r 维解析函数空间 $\mathcal F$ 中，可按 Taylor 首个非零系数逐次消元，选出消失阶严格递增的基

$$
0\le m_0<m_1<\cdots<m_{r-1}.
$$

过程有限，因为一个解析函数全部 jets 为零就恒为零。任一非零 $F\in\mathcal F$ 的消失阶不超过 $m_{r-1}$。这些不同整数给出的 falling-factorial 行列式是非零 Vandermonde，故该基 Wronskian 的准确阶数为

$$
\nu=\sum_{i=0}^{r-1}m_i-r(r-1)/2.
\tag{22}
$$

用 $m_i\ge i$，得到

$$
m_{r-1}\le\nu+r-1
\le r(r-1)/2+r-1
\le n(n+1)/2-1.
$$

这证明 (18)。整个论证也适用于实际解落在更小子空间的情况；上界只会偏大，不会漏掉真实关系。

## 6. 完整 jet 只需一个准确递推

对 (3) 定义 $v_j=X^{(j)}(0)$。则

$$
v_0=X_0,\qquad v_1=Nv_0,\qquad
\boxed{v_{j+1}=Nv_j+2\varepsilon jDv_{j-1}\quad(j\ge1).}
\tag{23}
$$

这从对 (3) 作 j 次导数直接得到，不需要再次求真实 profile 积分或逐点 s 求解。若 $F=c_FX$，则 $F^{(j)}(0)=c_Fv_j$。由引理，检查至 (4) 就准确判定整个 F 是否为零。

这是零函数证书，不是数值小残差判定。将来若作实际消费，必须保留原 profile 泛函的准确值或可复核的原函数恒等式；浮点有限 jet 小值不授 (5)。

## 7. 三矩系数的显式唯一消元

对任一偶谐波输出写 Taylor 展开

$$
Y(\sigma)=y_0+y_2\sigma^2+y_4\sigma^4+\cdots,
\qquad y_{2j}=Y^{(2j)}(0)/(2j)!.
$$

欲减去

$$
a h_eH+b\sigma^2+
c\frac{1+4\varepsilon^2k_e^2\sigma^4}{h_eH},
$$

令 $A=a h_e$、$C=c/h_e$。前三个 Taylor 方程恰为

$$
y_0=A+C,\qquad
y_2=\varepsilon(A-C)+b,\qquad
y_4=\frac{\varepsilon^2}{2}(A+C)+4\varepsilon^2k_e^2C.
$$

由于 $\varepsilon>0,k_e\ne0$，准确唯一解是

$$
\boxed{
C=\frac{y_4-\varepsilon^2y_0/2}{4\varepsilon^2k_e^2},\quad
A=y_0-C,\quad
b=y_2-\varepsilon(A-C),\quad
a=A/h_e,\quad c=h_eC.
}
\tag{24}
$$

三个 Taylor 行的行列式为 $4\varepsilon^2k_e^2$。这里用的是 Taylor 系数；若改用实际 0、2、4 阶导数，须相应乘阶乘，不能混用两个规范。

减去 (24) 后，F 的 0、2、4 阶 jet 自动为零。故实际尚需的有限线性条件只有

$$
\boxed{F^{(2j)}(0)=0,\qquad 6\le2j\le B_n.}
\tag{25}
$$

状态清单已经包含 (17)，所以该残差仍是同一个系统的常行输出。若某一谐波全零，(24) 给三个系数全零；若不同相位有种子关系，线性公式保持该关系。

## 8. 完整 profile 条件的含义与可复用接口

式 (11) 的每个 $c_{\alpha,\theta}$ 都是完整原 forcing 导出的四次 profile 泛函。结合 (23)、(24)，(25) 因而是一组有限、准确的四次条件。它们可按五个原相位谐波分别收集，也可作为同一个四次张量呈示保存。

这比仅给“存在某个有限 Gram 空间”更具体：

- s 函数仅需真实长度不超过二的指数字；
- 微分系统只有常数项和 $\sigma$ 一次项；
- 初值与所有待检 jets 有统一准确递推；
- 校正三矩列有显式逆；
- 判零阶数由有限状态清单 n 直接给出，不依赖猜测何时渐近层已穷尽。

同时，这并不使原 profile 条件自动独立，也不证明它们都是对角微包能量。若某些 R239 参数恰好使其中若干条件消失，只能按原条件的真实身份登记；不能因有限性就宣称剩余条件可由幅度或旋转任意支付。

一个后继实际源可以只消费原 R56/R73 公式和固定 profile 构造，输出 (11) 的有限清单、闭包 (15)、N/D/初值、原四次泛函定义以及 (25) 的最终残差。所有冗余必须通过真实输出关系处理。这里没有运行该目标，没有给未计算的 n、秩、零值或可解结论。

## 9. 真实范围

所有中心积分、局部恢复及 profile 右尾均保留；原传入 histories 的处理只用已证 (2)。解析性发生在指定偶 germ 的有限 s 系数上，不要求 C∞ profile 在 x 上解析，也不把局部解析公式延长为一条新的实际闭路径。

有限判据精确解决的是：**这个固定 germ 上，原第四 ruling 的整个偶部能否落在同一个三矩空间。** 若任一 (25) 非零，则任意合法全局二、三 gauge 都不能消掉该偶部障碍。若全部为零，则只得到此偶部 membership；奇部、其他 s 段、完整 period、同一个 w 的 joint 条件以及最终第四恢复仍须分别支付。

共振 $\varepsilon=k_e^2/4$ 可直接代入全部有限系统，并使 R241 已证层消去，但它不降低本稿需要保留的真实 history 层数，也不预先保证 (25) 的其他条件为零。

