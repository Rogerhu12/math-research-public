# R828 增补 — 实际一标量四位系统与同一修正的第二、第三页

日期：2026-11-16。**状态：下列实际一标量整展开、完整四位中央检验、同一个修正的逐页公式及其真实尾行旗标已证明。指定页类的非零或可解性仍未判定。**

本注接 [完整 $d$ 参考运输](2026-11-15-r828-complete-d-reference-transport.md)。它在同一个原 $M_4$ 中使用实际 $H_p$，不是把四高轴再当自由输入。第二页保原低卷积 $\mathcal R_p$、第一修正的全部低行和高尾；第三页另外保同一第二修正与真正末端四次 carry。没有增加长窗、原来源列或中央条件。

## 1. 固定实际参考及唯一标量族

保 R821/R828 的
$$
p=6s-1>211,\quad a=a_p=p\kappa\in\mathcal O^\times,\quad
1\le\ell<s-13,\quad L=3s+\ell,
$$
$$
\Gamma=\mathcal O[w,\epsilon]/
 (w^s-p\epsilon,\epsilon^4,w^{\ell+13}\epsilon^3).
\tag{1}
$$
仍删除 R821 固定 Jacobian 分子坏集。$\Gamma$ 是按原标准基的有限自由
$\mathcal O$-模；本注的除以 $p$ 均在该真实整模中进行。

使用已经支付的参考
$$
g_{\Theta,\circ}=g\exp(-h_\Theta),\qquad
h_\Theta(t)=\sum_{r=1}^4\ell_{s-r}t^{s-r}.
\tag{2}
$$
原 $d$、公共 $P_{134}/U_0$ 和其全部高精度均在此参考内；没有删除
$8^s$ 的 Fermat 商。记同一参考矩阵为 $M_0$。

设
$$
\mathsf P_r(p)=\prod_{j=1}^{r-1}\frac{p-6j}{p-6j-3},
\qquad \mathsf P_1=1,\qquad T_0(w)=-t(w)/w,
$$
并定义这个**完整的实际整级数**
$$
\boxed{
B(w)=\sum_{r=1}^4
 \frac{(-1)^r\mathsf P_r(p)}{s-r}\,
 w^{4-r}T_0(w)^{s-r}.
}
\tag{3}
$$
只读取原窗口内已经支付整性的系数。设
$$
b=(b_0,b_1,b_2,b_3)^t,\quad b_i=[w^i]B,\qquad
B_{<4}=\sum_{i=0}^3b_iw^i.
$$
这里 $b$ 不指中央截距，后者一律写成 $b_\Theta$。原反射式准确给
$$
\boxed{h_\Theta=H_p w^{s-4}B(w),\qquad u_\Theta=H_p b.}
\tag{4}
$$
特别
$$
b_0=\mathsf P_4(p)/(s-4)\in\mathcal O^\times,\qquad
\bar b=-18v
\tag{5}
$$
其中 $v$ 是 R828 的固定有理列。$B-B_{<4}$ 是原确定的高尾，
不能在第二、第三页预先删除。

原完整低卷积为 R828(20) 的
$$
\mathcal R_p=\Delta+
 \sum_{n=1}^{s-1}\ell_n[w^s]t(w)^n
 -17[w^s]\log W_0(w)\in\mathcal O.
\tag{6}
$$
全精度等式是
$$
H_p=\frac{p+1}{6(p-3)}(a-p\mathcal R_p).
\tag{7}
$$
定义以下整系数：
$$
\begin{aligned}
h_0&=-a/18,\\
h_1&=\mathcal R_p/18-2a/27,\\
h_2&=2\mathcal R_p/27-2a/81,\\
h_3&=2\mathcal R_p/81-2a/243.
\end{aligned}
\tag{8}
$$
于是
$$
\boxed{H_p=h_0+ph_1+p^2h_2+p^3h_3\pmod{p^4}.}
\tag{9}
$$
证明只需将
$$
\frac{p+1}{6(p-3)}
=-\frac1{18}-\frac{2p}{27}
 -\frac{2p^2}{81}-\frac{2p^3}{243}\pmod{p^4}
$$
代入 (7)。式 (8) 中保完整 $a,\mathcal R_p$，不是给它们另选
Teichmüller 数字，也不把 $\mathcal R_p$ 当作可以自由调节的第二参数。

## 2. 完整四位中央在同一标量线上的必要条件

令 $F_\nu^\Theta(u)$ 为 R821 的实际归一中央多项式，使用参考 (2)；
四来源仍为 $S,T,U,V$。定义
$$
\mathfrak F_\nu(H)=F_\nu^\Theta(Hb)\pmod{p^4}.
\tag{10}
$$
每个 $h_A$ 都使用 (4) 的整个 $B(w)$。R821 已付的 Hurwitz 四权化给
$$
\mathfrak F_\nu(H)=
\sum_{j=1}^4
 \frac{(-1)^{j-1}(j-1)!\,p^{j-1}}{q_\nu^ja^{j-1}}
 [w^{js}]\,A_{\nu,\Theta}
 \sum_{m=0}^j\frac{q_\nu^m}{m!}
       \bigl(Hw^{s-4}B(w)\bigr)^m
 \pmod{p^4}.
\tag{11}
$$
其中 $A_{\nu,\Theta}=(g_{\Theta,\circ}/d)^{q_\nu}f_\nu(t)$
是原参考来源，不是共同的自由余项。

所有 (11) 的多项式系数整。一个直接可用的加强是：
$$
\boxed{
[H^m]\mathfrak F_\nu\in p^{m-1}\mathcal O\quad(1\le m\le4),
\qquad
\mathfrak F_\nu^{(j)}\in p^{j-1}\mathcal O[H]\quad(2\le j\le4).
}
\tag{12}
$$
事实上，第 $j$ 个 Newton 权的参数次数不超过 $j$，并带 $p^{j-1}$。
在这里 $js-1<p$；R821 的实际 Hurwitz 整性
$(js-1)!\,C_{\nu,j}\in\mathcal O[H]$ 因而直接给
$C_{\nu,j}\in\mathcal O[H]$，不需要把更长窗口的裸系数认整。

若原四个完整中央同时零，准确的必要条件仍是
$$
\boxed{\mathfrak F(H_p)=0\pmod{p^4}.}
\tag{13}
$$
令
$$
f=\mathfrak F(h_0),\qquad f'=\mathfrak F'(h_0),\qquad
f''_1=\mathfrak F''(h_0)/p\in\mathcal O^4.
$$
利用 (9)、(12)，(13) 等价于下面这个真正四位的向量条件：
$$
\boxed{
f+ph_1f'+p^2h_2f'
 +p^3\left(h_3f'+\frac{h_1^2}{2}f''_1\right)
 \in p^4\mathcal O^4.
}
\tag{14}
$$
余下 Taylor 项都在 $p^4$ 中：二次项的 $h_1h_2$ 部分已带
$p^3\mathfrak F''\subset p^4$，三次项更在
$p^3\mathfrak F'''\subset p^5$。因此 (14) 没有遗漏高位非线性。

这也给一个准确的一标量 Hensel 读取。令
$$
\eta_0=e_0^tB_4^{-1},
$$
其中 $B_4$ 是原固定四轴 Jacobian，$e_0$ 读第一个物理坐标。由
$$
\mathfrak F'(H)\equiv B_4b\pmod p
$$
知 $\eta_0\mathfrak F'(H)\equiv b_0$ 为单位。故
$\eta_0\mathfrak F(H)=0\bmod p^4$ 有唯一标量解。
另外三条原中央仍必须在这同一个解上检验，不能各自选解。

例如在 (13) 的假设下，$\mathfrak F(h_0)\in p\mathcal O^4$，并有
$$
\boxed{
h_1\equiv-\frac{\eta_0\mathfrak F(h_0)}{p\,b_0}\pmod p,
\qquad
h_1=\mathcal R_p/18-2a/27.
}
\tag{15}
$$
其它三条第二位条件仍是同一向量
$\mathfrak F(h_0)/p+h_1\mathfrak F'(h_0)$ 的剩余三分量。
式 (15) 把实际低卷积接到下一中央位，未赋其为零或证明条件不相容。

## 3. 同一个原矩阵的四个整算子

对同一实际 charge 列 $\Phi$，保总 charge $Q_\Phi$，包括原公共四十；
参考列写成
$$
w^{13}A_\Phi(w)
 \sum_{i=0}^3\frac{a^iQ_\Phi^i\epsilon^i}{i!}.
$$
$A_\Phi$ 包括完整公共单位、$P_{134}$ 与该列的全部固定角数据。
对原源向量 $X$ 定义实际整级数
$$
W_i(X)=\sum_\Phi X_\Phi Q_\Phi^iA_\Phi(w).
\tag{16}
$$
在整个 $\Gamma$ 中
$$
M_0(X)=w^{13}\sum_{i=0}^3\frac{a^i\epsilon^i}{i!}W_i(X).
$$

定义以下四个真正的整映射，不另加源列：
$$
\begin{aligned}
A_1(X)&=\epsilon w^9B
 \left(W_1+a\epsilon W_2+\frac{a^2\epsilon^2}{2}W_3\right),\\
A_2(X)&=\frac{\epsilon^2w^5B^2}{2}
                   (W_2+a\epsilon W_3),\\
A_3(X)&=\frac{\epsilon^3wB^3}{6}W_3,\\
A_4(X)&=\frac{\epsilon^3w^{s-3}B_{<4}^{\,4}}{24}W_4 .
\end{aligned}
\tag{17}
$$
右边的每个 $W_i$ 均作用于同一 $X$；所有乘法都在 (1) 中真实折回，
不是先把 $w^s$ 当零。

由 R821 的完整四次末端式，实际矩阵准确为
$$
\boxed{
M_{\rm act}=M_0+pH_pA_1+p^2H_p^2A_2+
 p^3(H_p^3A_3+H_p^4A_4)\pmod{p^4}.
}
\tag{18}
$$
第四项来自 $w^{4s-3}=p^3\epsilon^3w^{s-3}$；
$\epsilon^4=0$ 不能删它。

将实际 (9) 代入，定义
$$
\boxed{
\begin{aligned}
D_1&=h_0A_1,\\
D_2&=h_1A_1+h_0^2A_2,\\
D_3&=h_2A_1+2h_0h_1A_2+h_0^3A_3+h_0^4A_4.
\end{aligned}}
\tag{19}
$$
于是
$$
\boxed{M_{\rm act}=M_0+pD_1+p^2D_2+p^3D_3\pmod{p^4}.}
\tag{20}
$$
这些是完整整算子展开，$M_0,A_i,a,\mathcal R_p,B$ 自身的全部
$p$-进位仍保留。尤其第二页的新原项确切为
$$
\boxed{
D_2=(\mathcal R_p/18-2a/27)A_1+\frac{a^2}{324}A_2.
}
\tag{21}
$$
不能把它替换为四个自由的“第二高轴”。

## 4. 同一 $P,R,S$ 的逐页整商

令 $\bar P\in K_1=\ker\bar M_0$，选择一个真实整提升 $P$。
所有修正 $R,S,T$ 都取在同一个原来源格。置
$$
Y_0=M_0(P)/p+D_1(P).
\tag{22}
$$
它是实际目标整向量。第一提升可解，准确等价于存在同格 $R$ 使
$$
Y_1:=Y_0+M_0(R)\in p\Gamma.
\tag{23}
$$
对这个同一 $R$，第二页的实际候选类是
$$
\boxed{
\left[Y_1/p+D_1(R)+D_2(P)\right]\in C_1,
\quad C_1=\operatorname{coker}\bar M_0.
}
\tag{24}
$$
它为零，准确等价于存在同格 $S$ 使
$$
Y_2:=Y_1/p+D_1(R)+D_2(P)+M_0(S)\in p\Gamma.
\tag{25}
$$
继续使用这个同一 $R,S$，第三页为
$$
\boxed{
\left[Y_2/p+D_1(S)+D_2(R)+D_3(P)\right]\in C_1.
}
\tag{26}
$$
其为零等价于可再选择同格 $T$，使
$$
Y_3:=Y_2/p+D_1(S)+D_2(R)+D_3(P)+M_0(T)\in p\Gamma.
\tag{27}
$$

直接展开 (20) 得到严格的等价：
$$
\boxed{
M_{\rm act}(P+pR+p^2S+p^3T)\in p^4\Gamma
\iff (23),(25),(27)\text{ 全部成立}.
}
\tag{28}
$$
每一商的整性都由前一条同一修正的条件支付。不能把
$Y_1/p$ 或 $Y_2/p$ 先作为任意目标向量，也不能为 (24) 的两项另选不同 $R$。

(24)、(26) 故意写成固定前面提升后的 $C_1$ 仿射类。
若取标准第二、第三 Bockstein 商，改变前面提升产生的像仍须一并商去；
本注没有把未固定提升的 $C_1$ 表达冒称一个与选择无关的新左行。
全部 native 来源项 $M_0(P)/p$、$M_0(R)$、$M_0(S)$ 均保留。

## 5. 首核上的真实 $12/16/12$ 尾行及其并集

现在只在模 $p$ 的原 $\Gamma$ 中读取 (17)，并令
$$
n_0=s-13.
$$
原完整首核给
$$
W_0(P),W_1(P),W_2(P)\in w^{n_0}k[[w]],\qquad
W_3(P)\in w^\ell k[[w]].
\tag{29}
$$
记
$$
D_{j,m}(P)=\sum_{i=0}^{m-1}
 [w^{n_0+i}]W_j(P)\,w^i\quad(j=1,2),
$$
$$
D_{3,m}(P)=\sum_{i=0}^{m-1}
 [w^{\ell+i}]W_3(P)\,w^i.
\tag{30}
$$
截断符号 $[\ ]_{<m}$ 始终先作实际乘积，再截断。

第一算子准确为 R821 的十二尾：
$$
\begin{aligned}
\bar A_1(P)={}&
 \epsilon w^{s-4}[BD_{1,4}]_{<4}
 +a\epsilon^2w^{s-4}[BD_{2,4}]_{<4}\\
 &+\frac{a^2}{2}\epsilon^3w^{\ell+9}
                         [BD_{3,4}]_{<4}.
\end{aligned}
\tag{31}
$$
第二算子的首核值则有新的完整十六尾式：
$$
\boxed{
\bar A_2(P)=
 \frac{\epsilon^2w^{s-8}}2[B^2D_{2,8}]_{<8}
 +\frac{a\epsilon^3w^{\ell+5}}2
                         [B^2D_{3,8}]_{<8}.
}
\tag{32}
$$
其目标位置是
$$
3s-8,\ldots,3s-1;\qquad L+5,\ldots,L+12.
\tag{33}
$$
第三算子的首核值为
$$
\boxed{
\bar A_3(P)=\frac{\epsilon^3w^{\ell+1}}6
                         [B^3D_{3,12}]_{<12},
}
\tag{34}
$$
位置 $L+1,\ldots,L+12$。

证明只用 (29) 后的准确首阶：
$$
5+n_0=s-8,\qquad5+\ell=\ell+5,\qquad1+\ell=\ell+1.
$$
达到块端点的项在约化目标中真正为零。这里没有把 $B$ 的高尾提前丢掉：
(32) 读取其前八阶，(34) 读取其前十二阶，而 (31) 只读前四阶。

因此 $D_2(P)$ 的三个源尾段长度是
$$
\boxed{(4,8,8)\quad\text{共 }20\text{ 个确定的同源系数},}
\tag{35}
$$
$D_3(P)$ 除真正末端四次项外，源尾段为
$$
\boxed{(4,8,12)\quad\text{共 }24\text{ 个确定的同源系数}.}
\tag{36}
$$
这些并集计数避免把重合的十二、十六、十二个目标位置重复计为独立余核行。
它们也绝不是二十或二十四个自由源参数。

## 6. 修正 $R$ 的全高尾如何由同一低行与十二尾读取

$R$ 通常不是首核，故不能对它套 (29) 或直接删除 $B-B_{<4}$。
令
$$
V_j(R)=[W_j(R)]_{<n_0}\ (j=1,2),\qquad
V_3(R)=[W_3(R)]_{<\ell}.
\tag{37}
$$
式 (23) 的同一 $\bar M_0R=-\bar Y_0$ 唯一指定这些低段：
第 $j$ 块先除其真实 $w^{13}$，再除原单位 $a^j/j!$。
该陈述只在第一修正确已存在时使用；最前十三个自由目标行仍必须通过。

定义读取已指定低段的完整卷积
$$
K_1^{\rm low}(R)=
 \epsilon w^9B
 \left(V_1(R)+a\epsilon V_2(R)+\frac{a^2\epsilon^2}{2}V_3(R)\right)
 \quad\text{于 }\bar\Gamma.
\tag{38}
$$
则逐项准确有
$$
\boxed{
\bar A_1(R)=K_1^{\rm low}(R)+
 \mathcal T_1(D_{1,4}(R),D_{2,4}(R),D_{3,4}(R)),
}
\tag{39}
$$
其中 $\mathcal T_1$ 就是 (31) 显示的三个尾乘积。
所以第二页 (24) 的 $R$ 端，是**第一修正指定的整个低卷积，加同一个 $R$ 的十二尾**。
式 (38) 可能读取 $B$ 的很长一段；它不等于只保 $B_{<4}$。

第三页的 $A_2(R)$ 同样准确分解为
$$
K_2^{\rm low}(R)=
 \frac{\epsilon^2w^5B^2}{2}\bigl(V_2(R)+a\epsilon V_3(R)\bigr)
\tag{40}
$$
加 (32) 形式的两个八尾。
对第二修正 $S$，(25) 指定其低段，$A_1(S)$ 再按 (38)–(39) 读取。
因此第三页的 $R$ 端读 $(4,8,8)$，$S$ 端读 $(4,4,4)$；
它们都服从各自前一步的同一个源向量，不是可以逐尾挑选的解。

此外，(24)、(26) 中的 $Y_1/p,Y_2/p$ 仍含真实 native 更高位。
上述有限尾旗标没有删除这些整商，也没有把整个第二或第三页缩成一个只依赖模 $p$ 尾表的自由矩阵。

## 7. 两个末窗在真正 canonical 首核上的读取

对一般来源，仍按 R821 保 (17) 的 $A_4$：

- $\ell\le s-16$ 时它为零；
- $\ell=s-15$ 时读取 $B_{<4}^4W_4(P)$ 的常数；
- $\ell=s-14$ 时读取其常数和一次项。

在本注的**原 canonical 单部分**中，可对真正首核再准确收紧一次。
只有相对 charge $0,1,2$ 的原列在 $w=0$ 非零，总 charge 为 $40,41,42$。
(29) 的三条常数行是这些 charge 上的单位 Vandermonde，因此逐个相对 charge 的常数系数组合为零。这严格给
$$
\boxed{W_i(P)(0)=0\quad\text{对全部 }i\ge0.}
\tag{41}
$$
故首核上的末端四次项准确为
$$
\boxed{
\bar A_4(P)=
\begin{cases}
0,&\ell\le s-15,\\[1mm]
\dfrac{b_0^4}{24}\epsilon^3w^{s-2}[w]W_4(P),
 &\ell=s-14 .
\end{cases}}
\tag{42}
$$
这不是利用 $\epsilon^4$ 删除原 carry，而是使用原三个常数行后真正留下的读取。
最后这一 $[w]W_4(P)$ 不受四个低阶矩全部强迫为零，必须保。
若来源格已经通过有成本的导子加入其它实际低 charge 项，
则必须先核其常数支撑；不能无条件把 (41)–(42) 搬到扩大的格。

## 8. 本次实际接合完成了什么

第一首余核仍准确为
$$
\beta_1^{\rm act}=
 \beta_{\Theta,\circ}+a_p\sum_{j=0}^3v_j\mathcal L_j,
$$
因为 $\bar h_0\bar b=a_pv$。没有把 $v$ 当作可删的 gauge。

新支付的是原实际标量的下一位如何进入同一个第二、第三修正：
$\mathcal R_p$ 通过 (21) 进入第二页，通过 (19) 进入第三页；
(31)–(40) 同时保其全部已指定低卷积与真正高尾。
四个完整中央在同一个标量上的额外限制则由 (14)–(15) 读取。

$h_3$ 确实出现在完整四位中央 (14) 中，但不出现在
$M_{\rm act}\bmod p^4$ 的 (20) 中：矩阵的一次高轴项本来已有一个 $p$。
因此不能把这一额外中央位直接计成一个新深核或第五长行。

仍未支付的是：对一个实际候选 $P$ 和同源修正 $R,S$，
(24) 或 (26) 中的指定 native 类是否非零；或者四个原卷积是否违反 (14)。
本注没有从中央条件构造任意 $F^4$ 核，也没有证明全部首核为四次幂。
原四位、三条十三行带、总 charge 四十、十九角、完整公共单位、
同一整提升和全部 source 成本均保留。

依赖：[R821](../results/R821-original-four-central-axes-and-complete-four-block-carries.md)、
[R828](../results/R828-original-four-high-axis-reflection-and-native-central-compatibility.md)、
[完整参考运输](2026-11-15-r828-complete-d-reference-transport.md)及
[R824](../results/R824-original-quartic-first-correctors-and-native-central-schur.md)。
本注为原式的整符号推导，无新增数学数值运行。
