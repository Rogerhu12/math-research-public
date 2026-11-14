# R271 附录：回文四头的显式源与全源两形式比较的非一致性

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_1cf。
状态：已证明；Astra-ISP-1cf8c51d 与 kernel_resume_1cf 全文核对真实最小链、全部物理系数及匹配上下界。以下是有限模型的解析渐近，不以数值作为证明。

本稿只排除“单凭头的回文 / $C$ 对称形状，便有只依头维数的全源两形式常数”这一更强入口。使用固定四维头、固定十一位 Boolean 尾和 $q=1$；它不是原 $m\ge5$ 的实际 $A_m$、不是原连续尾、也不是实际 $w\in W$ 产生的窄源。§§1–6 的基本源裸右能量发散；后续 §7 通过真实混合源取得左归一、裸费趋零且比例仍发散的加强。后续 §8 证明混合源规范差不趋零，§9 更证明整个有限规范来源类的左费≤24倍裸费；这仍不外推原实际 W 或高孔合法窗。

## 1. 有限真实 Hilbert 模型与结论

令 $0<t<1$，置
$$
\varepsilon=t^4,\qquad \beta=t^3,\qquad b=\frac14,
$$
$$
A_\varepsilon=
\begin{pmatrix}
0&1&b&0\\
0&0&\varepsilon&b\\
0&0&0&1\\
0&0&0&0
\end{pmatrix}.
\tag{1.1}
$$
它与四位 $N$ 头具有相同矩阵形状，严格为单链；反序共轭
$C_4e_i=e_{3-i}$ 给 $A_\varepsilon=C_4A_\varepsilon^*C_4$，且范数有统一上界。
此处自由改变 $\varepsilon$，没有把它认作原固定 carry。

尾是十一位标准 Boolean Hilbert 空间：三个位权为 $1$，八个位权为 $\beta$。
$D$ 是其真实删除，$E_{h,p}=\ker D^h\cap\mathcal H_p$。
取 $d=4,q=1$，保留原联合旗
$$
\mathscr C_t=\bigoplus_{i=0}^{4-t}e_iE_{4-i,1+t},
\quad 1\le t\le4,
$$
$$
\mathscr Y_t=\bigoplus_{i=0}^{3-t}e_iE_{3-i,1+t},
\quad1\le t\le3,
\qquad
Fc=Dc_1,\quad(Sc)_t=A_\varepsilon c_t+Dc_{t+1}.
\tag{1.2}
$$
这里段号 $t$ 在 (1.2) 中只作整数索引；渐近参数仍是 (1.1) 的正实 $t$。
为避免后文混淆，输入坐标写作 $c_{j,i}$，$j=1,\ldots,4$ 是段号。

按原相对出生数分低、高输入，令 $S_L$ 为低输出限制、
$Z=\ker S_L$、$\mathsf F=F|_Z$。
高输入在第 $j$ 段为
$$
\bigoplus_{i=0}^{4-j}e_iE_{j-1,1+j}.
\tag{1.3}
$$
所有投影均按原 Hilbert 内积。

在 $S_3\times S_8$ 固定块中，用
$x^a y^\ell$ 表示两个群中物理占据向量的均匀平均。
这些向量正交，且
$$
\|x^a y^\ell\|^2
=\frac1{\binom3a\binom8\ell},
\qquad
D=\partial_x+\beta\partial_y,
\qquad 0\le a\le3,\ 0\le\ell\le8.
\tag{1.4}
$$
令
$$
g_0=\beta x-y,\qquad
z_\beta=\|g_0\|^2=\frac{\beta^2}{3}+\frac18,
\qquad g=z_\beta^{-1/2}g_0.
$$
则 $Dg=0,\|g\|=1$。取显式首段源
$$
r=(e_2+b e_1)g=A_\varepsilon(e_3g).
\tag{1.5}
$$
记
$$
\lambda_t^2
=\min\{\|c\|^2:c\in\mathscr C,\ Fc=r,\ Sc=0\},
$$
$$
a_t=\mathsf F^\dagger r,\qquad
\alpha_t^2=\|a_t\|^2,\qquad
\mu_t^2=\|(E_1)^\dagger r\|^2,
\tag{1.6}
$$
其中 $E_1v=A_\varepsilon v_1$，$v$ 支持在尾孔层 $\le1$ 且满足其低输出方程。

**结论。**
$$
\boxed{
\mu_t^2=1,\qquad
\lambda_t^2\sim\frac{65}{12852}\,t^{-4},\qquad
\alpha_t^2\sim\frac4{8505}\,t^{-2}.
}
\tag{1.7}
$$
因此原有效正算子 $\mathscr L$ 与左状态形式 $\mathcal Q$ 在这个源上满足
$$
\boxed{
\frac{\langle\mathscr L a_t,a_t\rangle}
{\|a_t\|^2+\langle\mathcal Qa_t,a_t\rangle}
=
\frac{\lambda_t^2-\alpha_t^2}{\alpha_t^2+\mu_t^2}
\sim\frac{2925}{272}\,t^{-2}\longrightarrow\infty.
}
\tag{1.8}
$$
所以不存在只依 $d=4$ 的全源常数 $C$，使这整个回文头族都满足
$\mathscr L\le C(I+\mathcal Q)$。

## 2. 为何固定块给整个 Boolean 空间的真最小值

两个置换群均以酉作用保持 $D,D^*$、全部 $\ker D^h$、所有原正交出生投影，以及 (1.2) 的全部头和边界方程。源 (1.5) 固定。

把任意可行向量作群平均，仍可行且范数不增。最小范数元唯一，因此它属于固定块。相同论证分别适用于完整链、裸低链和左输入；没有把非正交代数链当作原最小原像。

$p=3,4,5$ 时，固定块 $\mathcal H_p$ 的维数为4，
$\mathcal H_2$ 的维数为3。$D^{p-2}:\mathcal H_p\to\mathcal H_2$
满射：按强占据数排序，取前三个源列，弱删除的三角对角均非零。
所以
$$
\boxed{
E_{p-2,p}^{\rm fixed}
=\mathbb C\chi_p,\qquad
\chi_p=y^{p-3}g_0^3.
}
\tag{2.1}
$$
$D^{p-2}\chi_p=0$ 来自 $Dg_0=0$；其物理强次数不超过3。
因此在第 $j=2,3,4$ 段，把完整输入投到低出生，恰是逐头作
$P_{\chi_{j+1}^\perp}$；第1段不改变。

固定高链 $S_H$ 也满射。因为
$D\chi_4=\beta\chi_3$、$D\chi_5=2\beta\chi_4$，
可从左到右用这些非零删除系数解三个高输出方程。
所以任意固定裸低可行链都有完整高补全。
反之，完整链的低投影是同源裸低可行链。由此
$$
\boxed{
\alpha_t^2
=\min_{Fc=r,\ Sc=0}\|P_{\mathscr X_L}c\|^2.
}
\tag{2.2}
$$
这是同一个真实低链最小值；没有以随意低截断代替低输出核。

左源则可直接解：$A_\varepsilon v_1=r$ 迫
$(v_1)_3=g,(v_1)_2=(v_1)_1=0$；其余第1层头分量只增加范数。
$Dg=0$ 允许第0层取零。故最小左输入正是 $e_3g$，
证明 $\mu_t^2=1$。

## 3. 完整右可行链的精确参数化

本节先用未归一化的 $g_0$，最后所有平方能量除以 $z_\beta$。
记 $g_0$ 暂为 $g$，仅为节省公式；本节中它的范数不是1。

取
$$
Z\in\mathcal H_4,\quad D^3Z=g,\qquad
W\in\mathcal H_5,\quad D^4W=0,\qquad
K\in\mathcal H_3,\quad D^2K=0.
$$
全部可行链恰由以下式子给出，另有可独立置零的
$c_{1,0}\in\ker D\cap\mathcal H_2$：
$$
\begin{array}{lll}
c_{1,1}=bD^2Z+DK,&c_{1,2}=D^2Z,&c_{1,3}=-D^3W,\\
c_{2,0}=-2bDZ-K,&c_{2,1}=bD^2W-\varepsilon DZ,&c_{2,2}=D^2W,\\
c_{3,0}=\varepsilon Z-2bDW,&c_{3,1}=-\varepsilon DW,&\\
c_{4,0}=\varepsilon W.&&
\end{array}
\tag{3.1}
$$
代入逐段验证 $Fc=(e_2+b e_1)g$、$Sc=0$，
每一项也满足相应逐头删除核。

反向，从任意完整可行链取
$$
W=\varepsilon^{-1}c_{4,0},\qquad
Z=\varepsilon^{-1}(c_{3,0}+2bDW),\qquad
K=-c_{2,0}-2bDZ.
$$
内部第3段、再第2段、再第1段逐头方程依次给 (3.1)，
首段源方程给 $D^3Z=g,D^2K=0$，而 $D^4W=0$ 是原旗。
故这是完整参数化，不只是一个候选族。

使用形式坐标 $(x,g)$，有 $Dx=1,Dg=0$。
为了保证物理强次数至多3，准确写为
$$
\begin{aligned}
Z={}&\frac{x^3g}{6}+u\,x^2g^2+v\,xg^3
-\left(\frac1{6\beta^3}+\frac u{\beta^2}+\frac v\beta\right)g^4,\\
W={}&\frac{\theta}{6}x^3g^2+\frac{\zeta}{2}x^2g^3
-\left(\frac{\theta}{2\beta^2}+\frac{\zeta}{\beta}\right)xg^4
+\left(\frac{\theta}{3\beta^3}+\frac{\zeta}{2\beta^2}\right)g^5,\\
K={}&k_1xg^2+k_0g^3.
\end{aligned}
\tag{3.2}
$$
六个参数任意为复数。
形式 $g^4,g^5$ 不单独被当成物理向量；(3.2) 的完整组合中
$x^4,x^5$ 系数准确相消，才得到合法向量。
反向由 $D=\partial_x$（保持 $g$）及上述强次数条件，
(3.2) 穷尽本节的 $Z,W,K$。

后面要读取的真实物理系数为
$$
\begin{array}{c|cc}
 & [y^p] &[xy^{p-1}]\\ \hline
Z\ (p=4)&-\frac1{6\beta^3}-\frac u{\beta^2}-\frac v\beta
&\frac2{3\beta^2}+\frac{4u}{\beta}+3v\\
DW\ (p=4)&-\frac{\theta}{2\beta^2}-\frac{\zeta}{\beta}
&\frac{2\theta}{\beta}+3\zeta\\
W\ (p=5)&-\frac{\theta}{3\beta^3}-\frac{\zeta}{2\beta^2}
&\frac{7\theta}{6\beta^2}+\frac{3\zeta}{2\beta}.
\end{array}
\tag{3.3}
$$
另外
$$
D^2Z=xg+2u g^2,\qquad DZ=\frac{x^2g}{2}+2u xg^2+vg^3,
$$
$$
D^2W=\theta xg^2+\zeta g^3,\qquad D^3W=\theta g^2.
\tag{3.4}
$$

## 4. 完整最小能量的准确主项

先说明存在 $O(t^{-4})$ 的上界。取任意固定复数 $A$，并设
$$
u=k_1=0,\quad
\theta=tA,\quad
\zeta=-\frac{2A}{3t^2},\quad
v=t^{-6}\Gamma,\quad
\Gamma=-\frac16-\frac{bA}{3},\quad
k_0=-2bv.
\tag{4.1}
$$
由 (3.1)–(3.3)，$c_{3,0}$ 的 $y^4$ 系数和 $c_{4,0}$ 的
$y^5$ 系数都准确为零。仅以下三个物理系数有 $t^{-2}$ 主项：
$$
\begin{array}{c|c}
\text{坐标/物理单项式}&t^2\text{乘该系数的极限}\\ \hline
c_{2,1}/y^3&-\frac16+\frac{bA}{3}\\
c_{2,2}/y^3&\frac{2A}{3}\\
c_{3,0}/xy^3&\frac16-bA .
\end{array}
\tag{4.2}
$$
其余系数均为 $O(t^{-1})$ 或更小。
由 (1.4)，$\|y^3\|^2=1/56$、$\|xy^3\|^2=1/168$。
故未归一化完整能量的 $\limsup$ 至多为
$$
\frac1{56}\min_{A\in\mathbb C}
\left\{
\left|-\frac16+\frac{bA}{3}\right|^2
+\left|\frac{2A}{3}\right|^2
+\frac13\left|\frac16-bA\right|^2
\right\}.
\tag{4.3}
$$

为给匹配下界，取真正最小链，使用刚付的 $O(t^{-4})$ 上界。
每个物理系数因正交范数均为 $O(t^{-2})$。
$c_{1,2}$ 的 $y^2$ 系数是 $2u$，$c_{2,2}$ 的 $y^3$ 系数是
$-\zeta$，所以
$$
u=O(t^{-2}),\qquad \zeta=O(t^{-2}).
$$
$c_{4,0}$ 的 $y^5$ 系数结合 (3.3) 给
$$
\frac{\theta}{3}+\frac{\beta\zeta}{2}=O(t^3).
$$
令 $A_t=\theta/t$、$B_t=t^2\zeta$，便有二者有界且
$$
A_t/3+B_t/2=O(t^2).
\tag{4.4}
$$
再读 $c_{3,0}$ 的 $y^4$ 系数并乘 $t^5$，得到
$$
t^6v=-\frac16+bA_t+2bB_t-t^3u+O(t^3)
=-\frac16-\frac{bA_t}{3}+o(1).
\tag{4.5}
$$
这里 $t^3u=O(t)$，没有忽略一个可能不小的参数。

将 (4.4)–(4.5) 代回三个 (4.2) 系数，
它们分别等于相应 $A_t$ 表达式加 $o(1)$。
丢去其余非负平方项，得到与 (4.3) 相同的 $\liminf$。
完整最小能量的主项因此恰为 (4.3)。

该复二次式的最小点为实数
$$
A_*=\frac{b}{4(1+b^2)},
$$
最小值为
$$
\frac{b^2+4}{108(1+b^2)}.
$$
最后除以 $z_\beta\to1/8$，代入 $b=1/4$，
证明
$$
\boxed{\lim_{t\downarrow0}t^4\lambda_t^2
=\frac8{56}\frac{b^2+4}{108(1+b^2)}
=\frac{65}{12852}.}
\tag{4.6}
$$

## 5. 裸低最小能量的准确主项

### 5.1 一个保原低可行性的上界

在 (3.2) 中取
$$
u=v=k_1=k_0=\zeta=0,\qquad
\theta=\frac{\varepsilon}{6b\beta}=\frac{t}{6b}.
\tag{5.1}
$$
其完整链可以非常昂贵；只取其真实低投影，(2.2) 保证同源裸可行性。

以下为这个低投影选择更容易估计的代表。
第2段保持 (3.1) 的原多项式；
第3、4段只加适当的 $\chi_4,\chi_5$ 倍数，以消去 $y^4,y^5$ 系数。
这些改变完全在高输入内，不改变低投影。调整后的第3、4段准确为
$$
\widetilde c_{3,0}=\frac{\varepsilon}{6\beta}x^2yg,\qquad
\widetilde c_{3,1}=-\frac{\varepsilon\theta}{2\beta}xyg^2,\qquad
\widetilde c_{4,0}=\frac{\varepsilon\theta}{6\beta^2}xy^2g^2.
\tag{5.2}
$$
第1段不变。除了最后一项，所有物理范数均为 $O(1)$。
而
$$
\widetilde c_{4,0}
=\frac{t^{-1}}{36b}xy^2g^2,\qquad
\|xy^2g^2\|^2\longrightarrow\|xy^4\|^2=\frac1{210}.
$$
所以未归一化裸能量的 $\limsup$ 满足
$$
\limsup_{t\downarrow0}t^2\alpha_{t,0}^2
\le\frac1{1296b^2\cdot210}.
\tag{5.3}
$$
下标0提醒本式暂用未归一化的 $g_0$。

### 5.2 只读取真实低分量的下界

给裸最小链选择任意完整高补全，按 (3.1)–(3.2) 记其参数。
(5.3) 给低能量 $O(t^{-2})$。
第一段没有高输入，故 $c_{1,2}$ 的 $y^2$ 系数迫
$$
u=O(t^{-1}).
\tag{5.4}
$$
对 $p=4,5$ 定义线性泛函
$$
\ell_p(f)=[xy^{p-1}]f+3\beta[y^p]f.
$$
由 (2.1)，$\ell_p(\chi_p)=0$，所以它只读取真实低投影。
其原 Hilbert 对偶范数准确为
$$
\|\ell_p\|^2
=\|xy^{p-1}\|^{-2}+9\beta^2\|y^p\|^{-2}.
\tag{5.5}
$$
特别该范数一致有界，且与完整高补全无关。

(3.3) 给
$$
\ell_4(c_{3,0})
=\frac{\varepsilon}{6\beta^2}
+\frac{\varepsilon u}{\beta}
-\frac{b\theta}{\beta}.
$$
低能量界使左边为 $O(t^{-1})$；结合 (5.4)，得到
$$
\boxed{\theta=\frac{t}{6b}+O(t^2).}
\tag{5.6}
$$
再由 (3.3)，另一个准确低泛函是
$$
\ell_5(c_{4,0})=\frac{\varepsilon\theta}{6\beta^2}
=\frac{t^{-1}}{36b}+O(1).
\tag{5.7}
$$
因此 Cauchy--Schwarz 在该原低分量上给
$$
\|P_{\chi_5^\perp}c_{4,0}\|^2
\ge
\frac{|\ell_5(c_{4,0})|^2}{\|\ell_5\|^2}.
$$
由 (5.5)，$\|\ell_5\|^2\to210$。
这给与 (5.3) 完全相同的 $\liminf$。
最后恢复 $g$ 的单位归一化：
$$
\boxed{
\lim_{t\downarrow0}t^2\alpha_t^2
=\frac8{1296b^2\cdot210}
=\frac4{8505}.
}
\tag{5.8}
$$
本证明没有把低投影换成一个非正交删系数操作：
上界只利用允许高向量改变后的范数，
下界则使用严格消灭该高子空间的有界泛函。

## 6. 所排入口与实际源边界

(4.6)、(5.8) 与 $\mu_t=1$ 给 (1.8)。
整个比较发生于原有限 Boolean Hilbert 范数，
两侧和裸链均为真正最小原像。
投影、头长跃迁、有限头回文性均未被删掉。

但
$$
\frac{\|a_t\|}{\mu_t}\longrightarrow\infty.
$$
所以本例不满足原 $w\in W$ 已付的
$\|a_{m,q}(w)\|\le\beta_q(w)+e^{-72d^4}\|w\|\to0$、
$\mu_{m,q}(w)\to\|w\|$。
它不排除只在真实 $a$、$a_{\rm two}$、$a^\sharp$ 上成立的更窄比较，
也没有给原连续尾合法窗中的反例。

此前有限定点探针只用于选定这条显式源和参数关系；
上述渐近已经由 (3.1)–(5.8) 的完整有限计算独立证明。
本稿不把浮点或定点读数当作已证结论，也不扩大原有限核 lift 窗。

## 7. 后续加强：左归一且裸源趋零的锥仍不产生形状统一常数

本节由 Astra-ISP-1cf8c51d 提出混合源，boundary_resume_1cf 核对全部旗与左最小像。继续使用同一个有限四头 / 十一尾模型，仍固定 $b=1/4$、$\varepsilon=t^4$、$\beta=t^3$，且 $g$ 始终是 (1.5) 的单位 primitive。

§§1–6 的基本坏源记为
$$
r_{\rm b}=(e_2+b e_1)g.
$$
它的裸右能量发散，确实不在原实际源的裸能量小锥中。不过可以加入另一个右费一致有界、左费很大的源，再对左费归一。这个有限模型中的混合严格表明：单独加上“左费为一、裸费趋零”还不足以从头的形状得到统一常数。

### 7.1 一个全右费一致有界的辅助源

令
$$
r_{\rm g}=e_1g.
$$
它有如下完整、合法的右链：
$$
c_1=e_1xg,\qquad
c_2=-\frac12e_0x^2g,\qquad
c_3=c_4=0.
\tag{7.1}
$$
因为 $Dg=0$，有 $D(xg)=g$、$D(x^2g)=2xg$；
而 $A_\varepsilon e_1=e_0$、$A_\varepsilon e_0=0$。
因此 $Fc=r_{\rm g}$、$Sc=0$。第一段的 $xg$ 在 $E_{3,2}$ 中，第二段的 $x^2g$ 在 $E_{4,3}$ 中；所有其余端点和旗也满足 (1.2)。

(1.4) 还给明确的统一范数预算
$$
\begin{aligned}
\|c\|^2
&=\|xg\|^2+\frac14\|x^2g\|^2\\
&=\frac{\frac7{12}\beta^2+\frac5{96}}
{\frac13\beta^2+\frac18}
\le\frac{61}{12}<6.
\end{aligned}
\tag{7.2}
$$
故真完整最小费和真裸最小费满足
$$
\lambda(r_{\rm g})\le\sqrt6,\qquad
\alpha(r_{\rm g})\le\lambda(r_{\rm g})\le\sqrt6.
\tag{7.3}
$$
第二个不等式来自 (2.2) 的真实低投影。

左最小像则准确为
$$
\boxed{
(E_1)^\dagger r_{\rm g}
=\varepsilon^{-1}(e_2-b e_1)g.
}
\tag{7.4}
$$
确实 $A_\varepsilon(e_2-b e_1)=\varepsilon e_1$。
源方程逐头固定这两个分量，其他第一层或零层分量都只增加正交范数；$Dg=0$ 允许零层取零。因此
$$
\mu(r_{\rm g})^2=(1+b^2)\varepsilon^{-2}.
$$
(7.4) 与基本坏源的左最小像 $e_3g$ 正交。

(7.1) 仅用于可行上界；没有声称它就是裸最小链，也没有据此断言 $a(r_{\rm g})\in\ker B_A$。

### 7.2 混合源保留两个右主项而放大左费

取
$$
R_t=r_{\rm b}+t^{5/2}r_{\rm g}.
\tag{7.5}
$$
对每个固定 $t$，完整右最小逆、裸最小逆和左最小逆都是真正的线性算子。三角不等式与 (7.3) 给
$$
|\lambda(R_t)-\lambda(r_{\rm b})|
\le\sqrt6\,t^{5/2},
\qquad
|\alpha(R_t)-\alpha(r_{\rm b})|
\le\sqrt6\,t^{5/2}.
\tag{7.6}
$$
因此 §§4–5 的两个精确主项不变：
$$
\lambda(R_t)^2\sim\frac{65}{12852}t^{-4},
\qquad
\alpha(R_t)^2\sim\frac4{8505}t^{-2}.
\tag{7.7}
$$
另一方面，两个左最小像的正交性给准确等式
$$
\boxed{
\mu(R_t)^2=1+t^5(1+b^2)t^{-8}
=1+\frac{17}{16}t^{-3}.
}
\tag{7.8}
$$
这里没有估计后再忽略左侧交叉项；它精确为零。

### 7.3 左归一后的真实裸锥与发散比例

定义
$$
\widehat r_t=\frac{R_t}{\mu(R_t)},\qquad
\widehat a_t=\mathsf F^\dagger\widehat r_t.
$$
由真实最小逆的齐次性，
$$
\boxed{
\mu(\widehat r_t)=1,\qquad
\|\widehat a_t\|^2
\sim\frac{64}{144585}t\longrightarrow0,
}
\tag{7.9}
$$
$$
\boxed{
\lambda(\widehat r_t)^2
\sim\frac{260}{54621}t^{-1}\longrightarrow\infty.
}
\tag{7.10}
$$
所以在完全相同的状态形式上，
$$
\boxed{
\frac{\langle\mathscr L\widehat a_t,\widehat a_t\rangle}
{\langle(I+\mathcal Q)\widehat a_t,\widehat a_t\rangle}
=
\frac{\lambda(\widehat r_t)^2-\|\widehat a_t\|^2}
{1+\|\widehat a_t\|^2}
\sim\frac{260}{54621}t^{-1}\longrightarrow\infty.
}
\tag{7.11}
$$

特别，对任意固定 $C>0$ 和任意固定 $\delta>0$，这个有限回文头族中都有某个参数和真实源满足左费为一、裸费小于 $\delta$，但 (7.11) 大于 $C$。
这是对“形状＋裸源小锥”的全源统一比较入口的反例。

本节仍没有构造原固定 $A_m$ / 连续尾合法窗中的源，更没有构造 $w\in W$。
原实际源还满足左、右的全部物理配对以及已付的同 $B_A$ 规范化；(7.5) 是否在
$$
P_{\ker B_A}(I+\mathcal Q)\widehat a_t=0
$$
的规范类中，没有在本节证明。
也没有证明投到该规范类后仍保留 (7.9)–(7.11) 的主项。
因此新的锥反例不关闭或否定原实际二形式求和目标。

## 8. 小裸锥混合源没有通过同返回源规范

本节仍用 §7 的
$$
R_t=r_b+t^{5/2}r_g,\qquad
r_b=(e_2+be_1)g,\qquad r_g=e_1g,\qquad b=\frac14,
$$
以及其真裸最小状态 $a_R=\mathsf F^\dagger R_t$。
记 $\mathcal D=I+\mathcal Q$，
其中 $\mathcal Q$ 是原左最小费用；令
$$
\widetilde a_t=\frac{a_R}{\mu(R_t)},\qquad
\widetilde a_t^\sharp
=\arg\min_{B_Aa=B_A\widetilde a_t}\|a\|_{\mathcal D}.
$$
这里 $B_A$、$\mathcal Q$ 与
[两侧真实源稿 §7](R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)
完全一致，全部投影仍按真实范数。

**结论。**
$$
\boxed{
\liminf_{t\downarrow0}
\|\widetilde a_t-\widetilde a_t^\sharp\|_{\mathcal D}^2
\ge\frac3{68}.
}
\tag{8.1}
$$
因此 §7 虽给左费用归一为 $1$、裸费用趋零的源，
其同返回源规范校正并不趋零。

证明只需要一个明确的零返回方向。
记 $D_2=D|_{\mathcal H_2}:\mathcal H_2\to\mathcal H_1$，置
$$
(k_t)_1=e_0D_2^\dagger g,\qquad
(k_t)_2=(k_t)_3=(k_t)_4=0.
\tag{8.2}
$$
这是源 $e_0g$ 的真裸最小链与真完整最小链：
任何同源向量第一段第零头都须满足 $Dv=g$，
而 (8.2) 达到其最小范数；它同时满足全部内部等式与旗。
所以
$$
k_t\in\ker B_A,\qquad E_1^\dagger(e_0g)=e_1g.
\tag{8.3}
$$

在原十一位空间的单孔标准正交基中，
$$
D_2D_2^*
=s^2I-2\operatorname{diag}(b_j^2)+\mathbf b\mathbf b^*,
\qquad s^2=3+8\beta^2.
$$
当 $\beta$ 充分小时，这个 Gram 至少为 $I$。
因此 $D_2^\dagger$ 在 $\beta=0$ 处连续，不存在未付的奇异极限。
此时 $g=-\sqrt8\,y$，真正最小原像为
$-\sqrt8\,xy$，其平方范数为 $1/3$。从而
$$
\boxed{
\|k_t\|_{\mathcal D}^2
=\|D_2^\dagger g\|^2+\|e_1g\|^2
\longrightarrow\frac43.
}
\tag{8.4}
$$

§7 的左最小链及正交性给
$$
E_1^\dagger R_t
=e_3g+t^{-3/2}(e_2-be_1)g,
\qquad
\mu(R_t)^2=1+(1+b^2)t^{-3}.
$$
又 $\|a_R\|=O(t^{-1})$、$\|k_t\|=O(1)$，所以
$$
\langle a_R,k_t\rangle_{\mathcal D}
=\langle a_R,k_t\rangle
+\langle E_1^\dagger R_t,e_1g\rangle
=-bt^{-3/2}+O(t^{-1}).
$$
除以 $\mu(R_t)$ 得
$$
\langle\widetilde a_t,k_t\rangle_{\mathcal D}
\longrightarrow-\frac b{\sqrt{1+b^2}}.
\tag{8.5}
$$

同返回源规范差是
$\ker B_A$ 上的 $\mathcal D$ 正交投影。
仅投到 (8.3) 的一维子空间便得到
$$
\|\widetilde a_t-\widetilde a_t^\sharp\|_{\mathcal D}^2
\ge
\frac{|\langle\widetilde a_t,k_t\rangle_{\mathcal D}|^2}
{\|k_t\|_{\mathcal D}^2}.
$$
结合 (8.4)、(8.5)，下极限至少为
$$
\frac{3b^2}{4(1+b^2)}=\frac3{68},
$$
证明 (8.1)。

本论证不需要、也没有声称
$\mathsf F^\dagger r_g\in\ker B_A$。
用于检测规范缺陷的准确零返回源是 $e_0g$。
原真实 $W$ 来源已付
$\|a-a^\sharp\|_{\mathcal D}\le e^{-72d^4}\|w\|$；
§7 的混合并未提供具有该额外来源性质的反例。

## 9. 同一四头族中，同返回源规范排除小裸能量锥

本节仍只处理本文的 $d=4,q=1$ 有限模型，但不再限于
$S_3\times S_8$ 固定向量。令
$$
0<\varepsilon\le1,\qquad 0<\beta\le\frac14,\qquad b=\frac14
$$
独立变化，尾仍为三个位权 $1$ 与八个位权 $\beta$。
以下结论适用于这个完整十一位 Boolean Hilbert 空间的所有首段源。

沿用真正低链
$$
U=Z\ominus\ker\mathsf F,\qquad \mathsf f=\mathsf F|_U,
\qquad
\mathcal Q=(E_1^\dagger\mathsf f)^*
             E_1^\dagger\mathsf f,\qquad
\mathcal D=I+\mathcal Q.
$$
$B_A$ 是同一低链到原高输出的映射，$\ker B_A=\ker\mathscr L$。
这里的 $a^\sharp$ 与
[两侧真实源稿 §7](R271-appendix-two-sided-actual-head-flux-gram-and-exact-energy-gap.md)
完全相同：它在固定 $B_Aa$ 的仿射集内最小化 $\|a\|_{\mathcal D}$。

**结论。** 若 $a\in U$ 满足
$$
a\perp_{\mathcal D}\ker B_A,
$$
则
$$
\boxed{
\mu(\mathsf f a)^2=\langle\mathcal Qa,a\rangle
\le576\|a\|^2.
}
\tag{9.1}
$$
常数不依赖 $\varepsilon,\beta$。实际上，只需对下面明确的首头零返回子空间满足
$\mathcal D$ 正交，便有 (9.1)；不需要识别整个 $\ker B_A$。

### 9.1 一个完整保留最小原像的零返回子空间

记
$$
D_1=D|_{\mathcal H_1}:\mathcal H_1\to\mathcal H_0,\qquad
D_2=D|_{\mathcal H_2}:\mathcal H_2\to\mathcal H_1,
$$
并把 $\mathcal H_0$ 的单位真空记为 $\Omega$。置
$$
s^2=3+8\beta^2,\qquad
u=s^{-1}D_1^*\Omega,\qquad
K=\ker D_1,
$$
于是 $\mathcal H_1=K\oplus\mathbb Cu$，$D_1u=s\Omega$。

在单孔的原标准正交基上，令权向量为 $\mathbf b$。
直接逐位计算给
$$
D_2D_2^*
=s^2I-2\operatorname{diag}(b_j^2)+\mathbf b\mathbf b^*.
$$
因最大位权为 $1$，且 $3\le s^2\le7/2$，
$$
\boxed{
I\le D_2D_2^*\le 7I,\qquad
\|D_2^\dagger\|\le1,\qquad
\|D_2\|\le\sqrt7<3.
}
\tag{9.2}
$$

对任意 $h\in\mathcal H_1$，定义低链 $k_h$ 为
$$
(k_h)_1=e_0D_2^\dagger h,\qquad
(k_h)_2=(k_h)_3=(k_h)_4=0.
\tag{9.3}
$$
它满足全部逐头旗，且
$$
Fk_h=e_0h,\qquad Sk_h=0.
$$
任何同源裸低链的第一段第零头分量都必须满足 $Dv=h$，
故其范数至少为 $\|D_2^\dagger h\|$。
(9.3) 达到该下界，所以它同时是该源的真正裸最小链与完整最小链。
特别
$$
k_h\in U,\qquad B_Ak_h=0,\qquad \|k_h\|\le\|h\|.
\tag{9.4}
$$
后面只使用 $a\perp_{\mathcal D}\{k_h:h\in\mathcal H_1\}$。

### 9.2 左最小链的完整五块坐标

设 $r=\mathsf f a$、$\alpha=\|a\|$，并令
$$
v=E_1^\dagger r=v_0+v_1,\qquad v_p\in\mathbb C^4\otimes\mathcal H_p.
$$
它满足
$$
A_\varepsilon v_0+D_1v_1=0,\qquad A_\varepsilon v_1=r.
$$
在这个左空间内，$\ker E_1$ 恰由以下向量张成：
$$
e_0\Omega,\qquad e_0h\ (h\in K),\qquad
e_0u-se_1\Omega.
$$
因此左最小条件就是对这三个正交类型的核方向正交。

解低输出方程并加上该正交条件，得到全部左最小链的唯一坐标：
存在 $\xi_1,\xi_2,\xi_3\in K$ 与 $x,y\in\mathbb C$，使
$$
\begin{array}{c|cc}
i &(v_0)_i\text{ 的 }\Omega\text{ 系数}&(v_1)_i\\ \hline
0&0&-\dfrac{bs}{1+s^2}yu\\
1&-\dfrac b{1+s^2}y&
  \xi_1+\left(bx-\dfrac{\varepsilon}{s}y\right)u\\
2&y&\xi_2+xu\\
3&-sx&\xi_3.
\end{array}
\tag{9.5}
$$
反向把 (9.5) 代入，也直接验证两项条件，所以没有删去一个左自由分量。
置
$$
c=1+s^2,\qquad k=1+\frac{b^2}{1+s^2}.
$$
原 Hilbert 范数准确为
$$
\boxed{
\|v\|^2=
\sum_{j=1}^3\|\xi_j\|^2
+c|x|^2+
\left|bx-\frac{\varepsilon}{s}y\right|^2+k|y|^2.
}
\tag{9.6}
$$
首段源的三个头坐标为
$$
\begin{aligned}
r_0&=\xi_1+b\xi_2+
       \left(2bx-\frac{\varepsilon}{s}y\right)u,\\
r_1&=\varepsilon\xi_2+b\xi_3+\varepsilon xu,\\
r_2&=\xi_3.
\end{aligned}
\tag{9.7}
$$
另一方面，$r=Fa=D_2a_1$，所以
$$
\|r\|\le3\alpha.
\tag{9.8}
$$

### 9.3 规范正交准确控制可能含小分母的左坐标

由 (9.4) 及 $\mathcal D$ 正交，
$$
\langle v,E_1^\dagger(e_0h)\rangle=-\langle a,k_h\rangle.
\tag{9.9}
$$
若 $h\in K$，则 $E_1^\dagger(e_0h)=e_1h$。
取全部单位 $h\in K$，(9.9) 给
$$
\|\xi_1\|\le\alpha.
\tag{9.10}
$$
再取 $h=u$。在 (9.5) 中，
$E_1^\dagger(e_0u)$ 恰对应 $x=0,y=-s/\varepsilon$、所有 $\xi_j=0$。
使用原范数 (9.6)，(9.9) 因而给准确的不等式
$$
\boxed{
\left|bx-\left(\frac{ks}{\varepsilon}
               +\frac{\varepsilon}{s}\right)y\right|
\le\alpha.
}
\tag{9.11}
$$
这里的小分母没有被一个头相似常数代替。

由 (9.7)、(9.8)、(9.10) 及 $b=1/4$，
$$
\|\xi_2\|\le16\alpha,\qquad
\|\xi_3\|\le3\alpha,
$$
从而
$$
\sum_{j=1}^3\|\xi_j\|^2\le266\alpha^2.
\tag{9.12}
$$
记 (9.11) 左边绝对值内部为 $\ell$，
并记 $r_0$ 的 $u$ 系数为 $r_{0,u}$。
两式准确相减给
$$
2\ell-r_{0,u}
=-\left(\frac{2ks}{\varepsilon}
         +\frac{\varepsilon}{s}\right)y.
$$
因为 $|\ell|\le\alpha$、$|r_{0,u}|\le3\alpha$，
$$
|y|\le\frac{5\varepsilon}{2ks}\alpha,
\qquad
\left|\frac{\varepsilon}{s}y\right|\le\frac56\alpha.
\tag{9.13}
$$
于是
$$
|x|\le\frac{23}{3}\alpha,\qquad
\left|bx-\frac{\varepsilon}{s}y\right|
=\frac12\left|r_{0,u}-\frac{\varepsilon}{s}y\right|
\le\frac{23}{12}\alpha.
\tag{9.14}
$$
最后 $c\le9/2$ 且
$k|y|^2\le25\alpha^2/12$。
将这些界代入 (9.6)，得到
$$
\begin{aligned}
\mu(r)^2
&\le
\left(266+\frac92\frac{529}{9}
           +\frac{529}{144}+\frac{25}{12}\right)\alpha^2\\
&=\frac{77221}{144}\alpha^2<576\alpha^2.
\end{aligned}
$$
这就证明 (9.1)。

### 9.4 对同源规范的含义与范围

对任意原裸状态 $a$，令 $a^\sharp$ 为固定 $B_Aa$ 的
$\mathcal D$ 最小者，并记
$$
\delta=\|a-a^\sharp\|_{\mathcal D}.
$$
因为 $\mathcal D=I+\mathcal Q$ 同时控制裸范数和左费用，
(9.1) 还给
$$
\boxed{
\mu(\mathsf f a)\le24\|a\|+25\delta.
}
\tag{9.15}
$$
故这个有限四头族内，不可能同时有
$\|a\|\to0$、$\mu(\mathsf f a)\to1$ 和
$\|a-a^\sharp\|_{\mathcal D}\to0$。
只要求小裸能量时的混合源反例，不会自动通过该同返回源规范。

本节不是 $\mathscr L\le C(I+\mathcal Q)$ 的证明；
它控制的是规范来源上的左费用。
它也没有把 $q=1$ 的上述左空间分解迁移到原
$m\ge5,\ 4d\le q\le e^{d^3/4}$。
原高孔层中对应的 $D$ 限制、左核及真实规范投影仍须完整支付，
不能从 (9.2) 的单孔 Gram 外推。

## 10. 同一有限模型中，裸费与廉价变换源共同控制全部左费

本节继续 §9 的同一个完整十一位模型，
$0<\varepsilon\le1$、$0<\beta\le1/4$、$d=4,q=1$。
常数独立于这两个小参数。
这里不要求输入源预先已经规范化。

记
$$
\mathcal P=I+\mathscr L,\qquad
\mathcal Q=(E_1^\dagger\mathsf f)^*E_1^\dagger\mathsf f,\qquad
\mathcal D=I+\mathcal Q,\qquad
\mathcal K_0=\ker B_A=\ker\mathscr L.
$$
对任意原源 $r$，取真正裸最小状态
$a=\mathsf f^{-1}r$，置
$$
\alpha=\|a\|,\qquad \mu=\|\mathcal Q^{1/2}a\|.
$$
令 $G$ 为完整右源 Gram，$J$ 为左源 Gram。
原准确的变换源是
$$
r^\flat=GJ^{-1}r.
$$
由 $G=\mathsf f\mathcal P^{-1}\mathsf f^*$、
$\mathcal Q=\mathsf f^*J^{-1}\mathsf f$，
其完整右最小费用恰为
$$
\boxed{
b_\flat:=\lambda(r^\flat)
=\|\mathcal P^{-1/2}\mathcal Qa\|.
}
\tag{10.1}
$$
这里没有交换两个源 Gram。

令 $a^\sharp$ 是固定 $B_Aa$ 的 $\mathcal D$ 最小者，
$e=a-a^\sharp$。
则
$$
e\in\mathcal K_0,\qquad
a^\sharp\perp_{\mathcal D}\mathcal K_0.
$$
因为 $\mathcal P=I$ 在 $\mathcal K_0$ 上，
$$
\mathcal P^{1/2}e=e,\qquad \|e\|\le\|e\|_{\mathcal D}.
$$
记 $\delta=\|e\|_{\mathcal D}$，正交性给
$$
\begin{aligned}
\delta^2
&=\langle\mathcal Da,e\rangle\\
&=\langle a,e\rangle
+\langle\mathcal P^{-1/2}\mathcal Qa,
        \mathcal P^{1/2}e\rangle\\
&\le(\alpha+b_\flat)\|e\|
\le(\alpha+b_\flat)\delta.
\end{aligned}
$$
$\delta=0$ 时同样成立，因此
$$
\boxed{\delta\le\alpha+b_\flat.}
\tag{10.2}
$$
这一步只反映真实 $\mathcal D$ 正交投影，不需要
$\mathscr L$ 在 $\mathcal K_0^\perp$ 上有正下界。

§9 已证明 $\mu(\mathsf f a^\sharp)\le24\|a^\sharp\|$。
又 $\mathcal D$ 同时控制裸范数与左费用，故
$$
\begin{aligned}
\mu
&\le\mu(\mathsf f a^\sharp)+\delta\\
&\le24(\alpha+\delta)+\delta
\le49\alpha+25b_\flat.
\end{aligned}
$$
因此全部源都满足
$$
\boxed{
\mu(r)\le49\|\mathsf f^{-1}r\|+25\lambda(r^\flat),
}
\tag{10.3}
$$
$$
\boxed{
\mu(r)^2
\le3026\left(\|\mathsf f^{-1}r\|^2+\lambda(r^\flat)^2\right).
}
\tag{10.4}
$$
最后使用 $49^2+25^2=3026$ 和二维 Cauchy--Schwarz。

若再记裸源 Gram $J_{\rm bare}=\mathsf f\mathsf f^*$，
(10.4) 等价于同一源空间上的真实算子不等式
$$
\boxed{
J^{-1}\le3026\left(J_{\rm bare}^{-1}+J^{-1}GJ^{-1}\right),
}
$$
或等价地
$$
\boxed{
J\le3026\left(JJ_{\rm bare}^{-1}J+G\right).
}
\tag{10.5}
$$
这些是正合同变换，不要求各 Gram 交换。

§§1–7 的两形式反例不反驳 (10.3)–(10.5)：
本节同时保留裸费用与明确变换源 $r^\flat$ 的完整费用。
在原实际 $W$ 来源中，两项都已由同一未来带加 carry 支付；
但本节的统一常数仍只在 §9 的有限 $q=1$ 模型内得到。
原 $m\ge5$ 高孔层是否有可付的同型常数继续开放。

