# R454：完整响应空间的 self 主系数与七项对角不变量

日期：2026-11-16。**完整原式纸面证明；没有执行新的原式编译、符号消元、profile 评价、秩、人工测试或科学运行。**

[R434](R434-complete-self-kernel-and-three-tail-current-image-on-144-original-responses.md) 只计算了原 $144=\mathcal B(E_8,Z)$ 列的 whole-self 核，其三个真实尾矩的完整退化点 current 像为三十九维规范空间中的三十二维。此前尚不能排除 [R247](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md) 的额外入口 $\Theta_{71}(\ker\Pi_{71})$ 改变剩余七项。

本文从完整 self 的原左二次系数证明一个统一恒等。七项对角量是其三阶导数平方主系数的固定 jet 收缩。因此，**整个原响应空间中保持 whole-self 的响应都杀这七项**。结合 R434 的既有反向包含，整个 $\mathcal R\cap\ker(\pi,\mathcal Q)$ 的 universal 三尾 current 像准确仍是原三十二维核。

这不是完整响应空间等于 $144+K_{0,\ldots,10}$ 的结论，也不决定完整 self 像、实际冻结母的评价秩或一般 actual 成本的对角余量。本文没有把响应身份移给一般 canonical 成本。

直接来源：R247、[R254](R254-eight-exact-third-diagonal-lifts-and-eighteen-dimensional-image.md)、[R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)、[R316](R316-complete-weight-zero-self-membership-and-positive-character-representative.md)、[R344](R344-general-pure-factorization-of-total-response-flux-with-ordered-Green-tails.md)、[R352](R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)、[R405](R405-common-exterior-packets-and-local-ordered-currents-at-all-internal-degeneracies.md)、[R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md)、R434，以及 R439 的六次对角表达。全部 primitives 仍使用同一个原右 collar。

## 1. 完整空间、原 self 与对角读出

沿 R247 记
$$
C(A,B)(a;b,c)=\Phi_A(a,\Phi_B(b,c))-\Phi_B(a,\Phi_A(b,c)),
$$
$$
\mathcal B_E(\tau)(F,\phi)
=2\tau(\Phi_ED;D)-4\tau(\phi;\phi,\Phi_ED)
+4\Phi_E(\phi,\tau(\phi;D)),\qquad D=F-\phi^2 .
\tag{1}
$$
令
$$
\Sigma_V(u)=V(u^2,0),\qquad
\widehat{\mathcal Q}_V(u)=[x^2]_{\rm left}\Sigma_V(u).
\tag{2}
$$
这里直接使用原 self 左多项式的二次系数，避免与文献中乘固定常数的 $\mathcal Q$ 规范混淆；两者的核相同。原 self 并不被假设左紧。

若 $u$ 完全在 $v$ 左侧，定义其普通系数
$$
U_V(u;n)
=[a^2b^2]\Sigma_V(au+bv),\qquad n=\mu(v),
$$
$$
\mu(v)=\left(\int(v'')^2,\ \int x(v'')^2,\
\int\{x^2(v'')^2+2(v')^2\}\right).
\tag{3}
$$
先对真实右包成立，再用三个同宽不同中心的真实矩基线性延拓到任意 $n$。没有把单个物理矩向量任意赋值。

在 $\pi V=0$ 时，R389 的完整 pure 极化识别
$$
U_V(u;n)=4Q_{V,n}(u).
\tag{4}
$$
对本稿的各响应生成元，(3)本身也有局部二次式加原 primitives 的表达。因此可以先定义
$$
\widetilde D_V(x)
=[ur]_{\rm loc}\frac{U_V(u;n)}4\bigg|_{n=(1,x,x^2)},
\qquad p=u',\ r=u'',\ t=u'''.
\tag{5}
$$
在 (5) 中，先提局部 $ur$ 系数，再作显示的代数代入；不是把 $n$ 当成随 $x$ 变化的物理输入而微分。

**与 raw pure 的定义域核对。** 对任意原响应先记
$P_{{\rm raw},V}(u)=V(0,u)=16\pi V(u)$，并令
$$
U_V^{\,S-P}(u;n)
=[a^2b^2]\{\Sigma_V-P_{{\rm raw},V}\}(au+bv).
\tag{5a}
$$
这里仍先取真实右包 $n=\mu(v)$，随后才按(3)线性延拓。
对每个 $\mathcal B_EC(B,C)$，R344 第 3 节(20)—(21)的完整三槽展开给
$$
[a^2b^2]P_{{\rm raw},V}(au+bv)
=2q_{\mathcal J_{E;B,C}(n)}(u),\qquad
\mathcal J_{E;B,C}(n)\in E_8 .
\tag{5b}
$$
原八个 $q_A$ 的局部部分均无 $ur$ 项；它们的真实 primitives 和左尾仍保留在(5b)，没有被置零。因此，对整个 $W_{71}$ 的各单原列，**即使其 $\pi V$ 非零**，用 $U_V^{\,S-P}/4$ 或 $U_V/4$ 提取局部 $ur$，再代 $n=(1,x,x^2)$，均得到同一个 $\widetilde D_V$。八个 $\chi$ 的原 pure 恒零，故(7)把这个结论延拓到全部 $\mathcal R$。这只识别本稿所用的对角系数；不声称两个完整有序函数相等，也不把(5b)外推到一般 $U$ 成本。下文的 self 主系数证明仍直接使用 $\Sigma_V$，未增添 pure-zero 假设。

若 $E(V)=(\pi V,\mathcal QV)=0$，再由 R344/R352 的 $\Lambda(\mathcal R)=0$ 得全部 ordered 自然系数为零。此时 (5) 正是 R433/R439 的真实 current 对角量
$$
D_V(x)=c_V(x;(1,x,x^2)).
\tag{6}
$$
其次数至多六，七个系数分别是既有的七项余量。

R247/R254 给完整来源覆盖
$$
W=W_{71}\oplus\operatorname{span}
\{\chi_{30},\chi_{32},\chi_{34},\chi_{37},
\chi_{40},\chi_{100},\chi_{104},\chi_{109}\},
\quad W_{71}=C(\Lambda^2E_8),
\tag{7}
$$
且八个 $\chi$ 全属于 $Z=\ker\Delta$。下面先证整个 $W_{71}$，再证整个 $Z$；这覆盖全部 $\mathcal R$，而不把 $Z$ 误当整个第三空间。

## 2. 八个原二次式的真实尾与主系数

采用
$$
P=r_0,\quad R=r_1,\quad S=s_0,\quad L=p_0,\quad
U=s_1,\quad V=p_1,\quad T=t_1,\quad Y=p_2 .
$$
写
$$
q_E=\Phi_E(u,u),\qquad
q_E''=\alpha_E(x,u,p,r)t+\beta_E,
\quad
\alpha_E=f_Eu+g_Ep+h_Er .
\tag{8}
$$
$\beta_E$ 只含二阶 jets 及原 $J_0,J_1,J_2$。由 R255 的完整八式直接求导得到：

| $E$ | $f_E$ | $g_E$ | $h_E$ | 真左尾 $p_E(n)(y)$ |
|---|---:|---:|---:|---|
| $P$ | $0$ | $0$ | $-2$ | $n_0$ |
| $R$ | $0$ | $2$ | $-2x$ | $yn_0$ |
| $S$ | $0$ | $0$ | $-2x$ | $n_1$ |
| $L$ | $1$ | $-x$ | $0$ | $(n_2-y^2n_0)/4$ |
| $U$ | $0$ | $2x$ | $-3x^2$ | $yn_1+n_2/2$ |
| $V$ | $x$ | $-x^2$ | $x^3/2$ | $-y^2n_1/4$ |
| $T$ | $0$ | $2x^2$ | $-2x^3$ | $yn_2$ |
| $Y$ | $x^2$ | $-x^3$ | $x^4/2$ | $-y^2n_2/4$ |

$y$ 只表示尾多项式的变量，评价点随后为 $y=x$。所以
$$
\boxed{
\left(p_E,p_E',p_E''\right)
\big|_{\,y=x,\ n=(1,x,x^2)}
=\left(-\frac{h_E}{2},\frac{g_E}{2},-\frac{f_E}{2}\right).
}
\tag{9}
$$

对任意二次多项式 $p_*=Ay^2+By+C$，R255/R344 的完整同锚作用为
$$
\Phi_E(p_*,w)=L_E(p_*)w,\qquad
L_E(p_*)=\ell_E(p_*)D_y-\ell_E(p_*)',
\tag{10}
$$
其中
$$
\begin{array}{c|cccccccc}
E&P&R&S&L&U&V&T&Y\\ \hline
\ell_E&
-2A&B&-2Ay&(C-Ay^2)/2&
By-Ay^2&Cy/2&By^2&Cy^2/2 .
\end{array}
$$
式(10)适用于右零、可有真实左二次尾的 $w$；原右 collar 的边项已在同锚公式内，不另删左尾。等价地
$$
\ell_E(p_*)=\frac12\alpha_E(y,p_*,p_*',p_*'').
\tag{11}
$$
令
$$
M_{AB}(x)=\ell_A(p_B(n))(x)\big|_{n=(1,x,x^2)} .
$$
由(9)—(11)，
$$
\boxed{
M_{AB}
=\frac{g_Ag_B-f_Ah_B-h_Af_B}{4}=M_{BA}.
}
\tag{12}
$$
这个对称性由真实八尾推出，不把 primitive 视作独立变量。

## 3. 全部交换子响应的原有序公式

先取 $V=\mathcal B_E C(B,C)$。由(1)直接得
$$
\Sigma_V(u)=2\{\Phi_B(q_E,q_C)-\Phi_C(q_E,q_B)\}.
\tag{13}
$$
对 (3) 作完整双包展开。右包处左包的 $q_E$ 准确为零；左包处右包的 $q_E$ 是原 $p_E(n)$。保留这两个方向后，准确得到
$$
\begin{aligned}
U_V(u;n)=2\{&
L_B(p_E)q_C-L_C(p_E)q_B\\
&+[L_B(p_C)-L_C(p_B)]q_E\}.
\end{aligned}
\tag{14}
$$
没有假设 $\Delta C(B,C)=0$，也没有假设单包 $q_E$ 左紧。

原 $q_A$ 的局部部分无 $ur$ 项，而 $q_A'$ 的该项系数为 $f_A$。由(10)，
$$
[ur]_{\rm loc}\frac{U_V}{4}
=\frac12\{f_C\ell_B(p_E)-f_B\ell_C(p_E)
+f_E[\ell_B(p_C)-\ell_C(p_B)]\}.
$$
用(12)仅消最后一项，得到
$$
\boxed{\widetilde D_V
=\frac12(M_{BE}f_C-M_{CE}f_B).}
\tag{15}
$$
这是全部原 Jacobi 呈示的直接读出。它也遵守完整 Jacobi，因为(12)使循环和逐项抵消。

### 3.1. 原 self 二次尾的三导平方项

在一个固定原左 collar 点 $\ell$ 与共同右 collar 之间积分。若 $a,b$ 都右零、左侧为
$A_ax^2+B_ax+C_a$ 与 $A_bx^2+B_bx+C_b$，原八式给
$$
[x^2]_{\rm left}\Phi_E(a,b)
=-\frac14\int_\ell^{r_*}f_Ea''b''
-\frac12\mathbf1_{E=Y}\int_\ell^{r_*}a'b'
+\mathfrak b_E(p_a,p_b;\ell).
\tag{16}
$$
$\mathfrak b_E$ 是原左多项式系数的准确双线性边项。这里没有把它置零。

例如 $L$ 的边项为 $-A_aA_b\ell$；$V$ 的边项为
$(A_aC_b+A_bC_a)/2-A_aA_b\ell^2/2$；$Y$ 的边项为
$$
-\frac{B_aC_b+C_aB_b}{2}
-A_aA_b\ell^3
-\frac{A_aB_b+A_bB_a}{2}\ell^2
-\frac{B_aB_b}{2}\ell .
$$
$P,R$ 的二次系数为零，$S,U,T$ 的全二次系数分别为
$-2A_aA_b,\ A_aB_b+A_bB_a,\ -B_aB_b$。
这给(16)全部八行，并保原有限积分下端。

把(8)代入(13)、(16)，所有原左边项均为真实 $\mu(u)$ 的四次组合，连续依赖 $C^2$。两个 $q'$ 的乘积也为 $C^2$。其余三阶导数的一次项可以对 $r$ 取原函数，再作一次保端项分部。因此
$$
\widehat{\mathcal Q}_V(u)
=\int F_V(x,u,p,r)t^2+\mathcal B_V(u),
\qquad \mathcal B_V\text{ 连续于共同支撑的 }C^2,
\tag{17}
$$
其中完整主系数为
$$
\boxed{F_V=-\frac12\alpha_E(f_B\alpha_C-f_C\alpha_B).}
\tag{18}
$$
(17)只是精确分裂，未删掉 $\mathcal B_V$ 或声称它为零。

定义只作用于自由 jet 变量的收缩
$$
\mathfrak T=\partial_p^2-2\partial_u\partial_r .
\tag{19}
$$
由(12)，$\mathfrak T(\alpha_A\alpha_B)=8M_{AB}$，所以
$$
\boxed{\mathfrak T F_V=8\widetilde D_V}
\qquad(V\in\mathcal R_{71}).
\tag{20}
$$

## 4. 全部十八个第三对角核的同一恒等

现在取任意 $\tau\in Z$，记
$$
K(w)=\tau(w;u,u),\qquad
K(w)'''=\mathscr A_uw,\qquad
\mathscr A_u=D^2(aD^2)+D(bD)+c,\qquad \mathscr A_uu=0.
\tag{21}
$$
这是 R258/R261 的完整算子与三个真实右常数，不仅是对角式。

置
$$
A=K(1),\qquad B=K(x)-xA,\qquad
C=\frac{K(x^2)-x^2A-2xB}{2}.
\tag{22}
$$
这里对多项式输入使用右归一的 $-J^3(\mathscr A_uw)$：其 source 支撑于 $u$，无需把该多项式输入本身假设为右紧。真实右包的 $p_E(n)$ 在 source 上与此延拓相同，因此
$$
K(p_*)=p_*A+p_*'B+p_*''C
\tag{23}
$$
对每个二次多项式准确成立。

### 4.1. 本步骤未循环使用 whole-self 零

$A,B,C$ 均有“局部二次 $C^2$ 多项式 + 显式系数乘原二次 primitives”的完整表达。

可直接从 R405 §4—6 的 raw 分子式读取这个事实：该段的局部加三个 $J$ 身份不使用 whole-$\mathcal Q=0$；whole-self 仅在其 §7 把 primitive 系数的二阶导数置零。对 $\mathcal B_P\tau,\mathcal B_R\tau,\mathcal B_L\tau$，$\Delta\tau=0$ 已给 $\pi=0$，故完整 ordered self 正是 $2K(p_E(n))$。依次用其常、一次、二次尾和三个真实矩基，得到(22)所需的表达。

这段 raw 恒等不使用 $\tau_{\rm hook}\ne0$ 的除法或 period 右逆；对原 $M=0$、同端口闭 frame 响应成本的有限 signed 延拓成立。不能把 R405 后来用于 current 的 whole-$E$ 假设提前作为本步骤前提。

因而可写
$$
A_{\rm loc}=a_Au^2+b_Aup+c_Aur+d_Ap^2+e_Apr+f_Ar^2
\tag{24}
$$
及 $B_{\rm loc},C_{\rm loc}$ 的同样六项。各 bare primitive 的三阶导数最高只到 $u^{(4)}$，不会贡献下一步的 $u^{(5)}$ 系数。

### 4.2. 一个最高 jet 恒等，而非重新求十八列

对(23)求三阶导，与(21)比较 $p_*,p_*',p_*''$，并用共同右端常数，得
$$
\boxed{c=A''',\qquad b=3A'+B'',\qquad a=2B+C'.}
\tag{25}
$$
例如 $b'=3A''+B'''$ 的积分常数由右 collar 全零固定；$a$ 的两常数也同样固定。

把(25)代入
$$
(ar)''+(bp)'+cu=0 .
$$
其 $u^{(5)}$ 系数准确为
$$
u(A_{\rm loc})_r+p(B_{\rm loc})_r+r(C_{\rm loc})_r=0.
\tag{26}
$$
这只是一个原 universal jet 恒等的系数比较；没有对 primitive 内部作退化点代入。

比较(26)的六个二次单项，特别得到
$$
\boxed{c_A=0,\qquad c_B=-e_A,\qquad c_C=-2f_A.}
\tag{27}
$$
另三式为 $e_B=0,\ e_C=-2f_B,\ f_C=0$，本稿不需要它们。

由(23)、(27)，对任意 $p_*$，
$$
[ur]_{\rm loc}K(p_*)=-e_Ap_*'-2f_Ap_*'' .
\tag{28}
$$
对 $V=\mathcal B_E\tau$，真实 ordered 输出为 $U_V=2K(p_E(n))$：另一项 $K_v(q_E(u,u))$ 的 source 处 $q_E(u,u)$ 准确为零，原三个右常数也为零。这一步没有删除 $K_u(p_E)$ 的左尾。

利用(9)，
$$
\boxed{\widetilde D_V=\frac{f_Ef_A}{2}-\frac{g_Ee_A}{4}.}
\tag{29}
$$

### 4.3. 完整 self 主系数与真实左边项

由(21)，
$$
\widehat{\mathcal Q}_{\mathcal B_E\tau}(u)
=-\int_\ell^{r_*}c\,q_E .
$$
这里 self 为 $2K(q_E)$；其左 $x^2$ 系数正是 $K(q_E)''_{\rm left}$。$a,b$ 含紧 $u$ 的 jets，所以从 $\mathscr A_uq_E$ 积分到 $cq_E$ 的两边界为零，而 $q_E$ 本身仍可有左二次尾。

用 $c=A'''$，完整分部积分是
$$
\boxed{
-\int A'''q_E
=A''(\ell)q_E(\ell)-A'(\ell)q_E'(\ell)
-\int A'q_E''.
}
\tag{30}
$$
这是保留真实下端的公式，不是沿非紧方向套一个仅紧域的变分。

由 §4.1，$A'(\ell),A''(\ell)$ 都是原二次矩的确定线性组合；$q_E(\ell),q_E'(\ell)$ 也由真尾表给定。因此显示边项是连续 $C^2$ 的完整四次量。余积分用(8)、(24)、(27)分裂：
$$
F_V=-\alpha_E(A_{\rm loc})_r
=-\alpha_E(e_Ap+2f_Ar).
\tag{31}
$$
其他项至多一次 $t$，仍按原锚降为连续 $C^2$ 余量。于是(17)继续成立，并且
$$
\mathfrak T F_V=4f_Ef_A-2g_Ee_A
=8\widetilde D_V.
\tag{32}
$$

作为直接源校验，R261 的八个 $\bar c_j=256c_j$ 之 $u^{(5)}$ 系数依次给
$$
\begin{array}{c|l}
j&256(A_{\rm loc})_r\\ \hline
30&3r\\
32&-2p-6xr\\
34&2p-18xr\\
37&-16xp+36x^2r\\
40&8x^2p-12x^3r\\
100&-32xp-48x^2r\\
104&-160x^2p+192x^3r\\
109&192x^3p-192x^4r .
\end{array}
\tag{33}
$$
这只是已发表表的系数读取，不执行八个算子的新恢复或新消元。主证明由(25)—(32)统一完成。

## 5. whole-self 零迫七项对角量零

由(7)、(20)、(32)，整个响应空间都有同一准确身份
$$
\boxed{\mathfrak T F_R=8\widetilde D_R,\qquad R\in\mathcal R.}
\tag{34}
$$
它没有声称 $F_R$ 或 $\widetilde D_R$ 对任意响应为零。

若 $\widehat{\mathcal Q}_R$ 对全部真实紧 $u$ 为零，(17)迫
$$
F_R(x,u,p,r)\equiv0 .
\tag{35}
$$
这里不能只由“主系数”的名称推得(35)。一个直接纸面验证如下：固定任意紧基准 $u_0$ 和内部小窗，加入
$N^{-5/2}\chi(x)\cos Nx$。二阶范数趋零，三阶平方除以 $N$ 弱趋 $\chi^2/2$；原连续 $C^2$ 余量除以 $N$ 趋零。将恒零的(17)除以 $N$，得到
$\int F_R(x,u_0,u_0',u_0'')\chi^2=0$。
任意缩小小窗，再自由指定基准的二阶 jets，得(35)。这里只证明 universal 身份，不构造新的研究母或运行任何高频计算。

因此
$$
\boxed{\widetilde D(\mathcal R\cap\ker\mathcal Q)=0.}
\tag{36}
$$
在本课题完整 period 所用的范围内，
$$
\boxed{D(\mathcal R\cap\ker(\pi,\mathcal Q))=0.}
\tag{37}
$$

whole-self 条件不可省。R255 的
$$
J_0=4C(L,R)-4C(L,S)-3C(P,T)+2C(R,U)+4C(S,U)
$$
属于 $Z$，但(15)直接给
$$
\widetilde D_{\mathcal B_RJ_0}=-2.
\tag{38}
$$
同时 $K_{J_0}(1)=4pr+2P(u,u)$，其中 $P(u,u)=\int_x^{r_*}r^2$ 是原 primitive；故(31)的主系数是
$-8p^2+8xpr\ne0$。
这个 pure 零响应确有非零 whole-self。式(38)只作规范和必要假设的纸面校验。

## 6. 整个响应空间的 ordered current 像已经闭合

令 $\mathscr C_{39}$ 为 R433/R439 的完整十三列、三尾矩 current 空间，记
$$
D:\mathscr C_{39}\longrightarrow\operatorname{Pol}_{\le6}.
$$
R434 已付原 $144$ 列的 whole-self 核像
$$
\operatorname{im}\bigl(\mathcal B(E_8,Z)\cap\ker\mathcal Q
\longrightarrow\mathscr C_{39}\bigr)
=\ker D,\qquad\dim\ker D=32.
\tag{39}
$$
本文不重算该秩、三十九行、八十五核、五十三 current 核或 R443 self 像。

另一方面，全 $\mathcal R\cap\ker E$ 的 current 也落在 $\mathscr C_{39}$：
whole pure 给原有序识别，whole self 给仿射 primitive 系数，R344/R352 的完整 $\Lambda(\mathcal R)=0$ 给 R433 的六条 Euler ODE。由(37)，其像包含于 $\ker D$。反向包含由(39)及 $Z\subset W$ 已有，故
$$
\boxed{
\operatorname{im}\bigl(\mathcal R\cap\ker E
\longrightarrow\mathscr C_{39}\bigr)=\ker D,\qquad
\dim=32 .
}
\tag{40}
$$

所以 $\Theta_{71}(\ker\Pi_{71})$ 的确是完整 pure 核不可删除的来源，但在**最终仍保 whole self** 的 ordered current 问题中，它不新增第33个方向。若先用一个响应改变 $E$，再用另一个响应恢复 $E$，净响应仍属于(37)，也不能留下新的 $D$ 改变量。不能把中途(38)的非零值当成免费的最终控制。

对实际冻结的所有退化点、真实 suffix 和两通道组合，仍须应用原评价映射。其具体像为
$$
\operatorname{Eval}_{\rm actual}(\ker D).
\tag{41}
$$
(40)不把它的秩固定为32，不把七个 formal 系数都宣布为实际独立障碍，也不允许逐点选不同成本。它准确排除了“转到未算的完整响应就能补七项”这一未经支付的可能；一般 actual 路径改变 $D$ 的能力仍是另一个问题。

## 7. H* 的六个 R126 原来源及所走的外入口

R316 的正特征代表为
$$
H_*=C_2+\frac{649}{768}R_2-\frac{73}{3072}R_3
+\frac{649}{1536}R_4-\frac{821}{768}R_5
+\frac1{64}R_7+\frac{187}{1024}R_9.
\tag{42}
$$
这里的 $R_j$ 始终是 **R126 old-column 编号**，不是其他权块的同名编号。

本次只消费 R406 已付原日志的
$\texttt{needed_original_input_restore.six_mixed_responses}$ 标签。run 为
$43775998866$，job 为 $133002325378$；原日志为123807字节，
SHA256为
$\texttt{fffe1b37deb54839af548cd50b155b956c4338744490f02668f8967f239ceda2}$。
原 main 为31231字节，
SHA256为
$\texttt{776e3f3fbe1872c877018a5b22a792203eac09265d589391d59223b7c11f758c}$。
这是旧来源只读，不是新的数学运算。

原 retained $W$ 的前28项按 R247 的 pair 字典序，位置35为原 $\tau_{109}$。因此：

| R126 标签 | quadratic | retained W | 完整来源 |
|---|---|---:|---|
| $R_2$ | $p_1=V$ | 1 | $\mathcal B_V C(L,Y)$ |
| $R_3$ | $p_1=V$ | 12 | $\mathcal B_V C(V,T)$ |
| $R_4$ | $p_1=V$ | 16 | $\mathcal B_V C(Y,U)$ |
| $R_5$ | $p_1=V$ | 35 | $\mathcal B_V\tau_{109}$ |
| $R_7$ | $p_2=Y$ | 6 | $\mathcal B_Y C(L,T)$ |
| $R_9$ | $p_2=Y$ | 14 | $\mathcal B_Y C(Y,R)$ |

R254 给 $\gamma_{109}=-C_{12}/4$，故完整身份是
$$
\boxed{R_5+\frac14R_3=\mathcal B_V\chi_{109}.}
\tag{43}
$$
右边确是144个原标签之一；其余五条属于原 $W_{71}$ 交换子来源。不能因它们出现在 H* 就把它们改称第三对角核标签，也不从标签不同推出完整成本线性独立于144列。

由(15)、(33)，在(5)的完整 self-ordered 扩展下，
$$
\widetilde D(R_2)=\frac{x^5}{16},\qquad
\widetilde D(R_4)=-\frac{x^5}{8},\qquad
\widetilde D(R_3)=\widetilde D(R_5)
=\widetilde D(R_7)=\widetilde D(R_9)=0.
\tag{44}
$$
于是(42)的六响应总修正的 $\widetilde D$ 恰为零。H* 的七项因此完全来自 $C_2$ 的**原 self-cross**，而不是由这六条修正制造。

需要保留这句话的定义域：$C_2$ 单独未被假定 pure 零，故不能把它的一个单独 $YC$ 路径系数直接等同于(5)。只有对最终 pure 零的 H*，(4)才把 self-cross 与 R439 的真实 $D$ 识别。本文不计算 $C_2$ 的该完整值，不替代原路径方向的独立证明。

六个旧 mixed 根 SHA256 依原标签依次为：

- $R_2$：$\texttt{d0fffba432e8a26a063f1d7d618f1b352a0d3c661af236e08c7b71323a057120}$；
- $R_3$：$\texttt{1cbdd945922696c4ce47c50e0c67894ef8ed673b8b195d7c1a08387b89207b4b}$；
- $R_4$：$\texttt{f62bfd17fb145469826fb310b8c33ef8aceb9ff3e275d93e024c750f0b8b454c}$；
- $R_5$：$\texttt{95e7338cd3754b8dbde7568a7db44d50842b885399fda5adb1024c5ea6ee36a6}$；
- $R_7$：$\texttt{29f01b9237e9fba535fd35070d32f6b08b8698028cb82819dad7aed5a3d628ee}$；
- $R_9$：$\texttt{1b4fe2068891586de835bfa89cdd43f37a28062269ece6728f9950190bc4977a}$。

## 8. 本稿关闭与保留的范围

已关闭的是整个原响应空间的三尾 current 外入口：(40)给出完整像，不再只是144列的生成上界。R126 的全部已付 pure-kernel 关系、或任何以后选出的 $\Theta_{71}(\ker\Pi_{71})$ 代表，只要净响应保持 whole $E$，都不能改变七项系数表中的 $D$。

仍然分别保留：

- 一般 canonical actual 成本的 $D$，以及该路径量能否在原几何约束内归零；
- (41)在同一冻结母、全部真实幅宽、suffix 与副本位置上的具体评价商；
- 完整 self 的实际所有根目标。R443/R448 的49模块和镜对19行不是全 $\mathcal R\cap\ker E$ 的 self 穷尽结论；
- 原 period 平台仿射常量、内部 range、端 germ、同一补偿与十三行 joint；
- 任何新增实际正锥或同点 $C^1$ 截面。本文是完整响应线性像定理，未把 signed 代表直接变成实际路径。

R453 的 canonical 原路径余量与本文没有冲突：本文的收缩恒等针对响应来源 (1)、(7)，没有把一般 $U$ 的 self 主系数当作唯一项。完整课题继续，未完成。
