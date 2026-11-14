# R349 — 原临界 Faber 三次行、两项 carry 与全 norm-three 投影

日期：2026-11-13。**状态：以下同一真实核上的三次 Faber 关系、两个临界
换元项、充分大普通素数的三次行单位性，以及完整 norm-three/Hirota 的
指定行投影均已证明。没有由新三次型非零推断原两个固定负矩联合非零；
主目标未完成。**

本篇接 [R336](R336-ordinary-original-zeta-as-verschiebung-and-two-full-negative-rows.md)、
[R343](R343-original-three-torsion-phase-and-two-complete-faber-observers.md)、
[R345](R345-original-degree-three-absolute-core-phase-and-middle-cartier-row.md)。
全过程保持原微分、实际可分核和原 Laurent/Faber 坐标。临界系数中的
$1/p$ 常数项必须先与微分里的 $p$ 相乘，才能约化。

## 1. 同一个真实核与三个原观察

固定
$$
E_b:y^2=x^3+b,\quad b=17,\qquad
p=6s+1>7,\quad D=d/dz,\quad x=z^{-2}+\cdots,\quad y=-z^{-3}+\cdots,
$$
$$
H=\binom{3s}{s}b^s,\qquad
\eta=\eta_p=\left(\frac{4b}{\mathfrak p}\right)_6.
\tag{1}
$$
在模 $p$ 的式子中，$H,\eta$ 都表示 R336、R345 原普通嵌入下的剩余值。
真实可分同源是 $V=[\bar\pi]\bmod p$，核多项式为
$$
f_V=P(X),\qquad X=x^3,\qquad P\text{ monic},\quad \deg P=s.
$$
需要先取特征零 Laurent 系数时，使用真实整 monic lift
$f_{\bar\pi}=P(x^3)$；它的约化正是上式。其所有系数整。

R343 的原 Faber 基为
$$
F_j(X)=\frac{D^{6j-2}x}{(6j-1)!},\qquad
F_j(X(z))=z^{-6j}+F_{j,0}+O(z^6),\quad 1\le j\le s.
$$
各 $F_j$ 是 monic degree $j$ 的整多项式，因所用阶乘最高到 $(p-2)!$。
写
$$
P=\alpha_0+\sum_{j=1}^{s}\alpha_jF_j,\qquad \alpha_s=1.
\tag{2}
$$
所有 $\alpha_j$ 整。原两行准确是
$$
\mathcal L=\alpha_1,\qquad
\mathcal Q=
\sum_{j+k=s+1}\{-18(j-k)^2-3(s+1)\}\alpha_j\alpha_k.
\tag{3}
$$
求和按有序对。原两个固定负矩的首层分别是 (3) 乘 R343 已支付的
单位周期、阶乘与共同 $H^6$；本篇不改变这些外部因子。

定义同一核的纯 polar 三次型
$$
\boxed{\mathcal K=
486\sum_{\substack{j+k+l=2s\\1\le j,k,l\le s}}
jkl\,\alpha_j\alpha_k\alpha_l.}
\tag{4}
$$
三元组同样按有序组求和。

**定理。** 原实际核满足
$$
\boxed{\mathcal K=-\eta-\frac92H\pmod p.}
\tag{5}
$$
对所有普通 $p>331$，右端是单位。完整 norm-three 的另一条准确行是
$$
\boxed{
\sum_{\substack{i+j+k=2s+1\\1\le i,j,k\le s}}
\left\{36(ij+ik+jk)-\frac{20}{3}\right\}\alpha_i\alpha_j\alpha_k
=-\frac{\alpha_1}{27}.
}
\tag{6}
$$
同一真实核的 Hirota 行还给
$$
\boxed{
\sum_{j+k=s+1}8(36jk-7)(36jk-15)\alpha_j\alpha_k=0.
}
\tag{7}
$$
这些是一个实际核上可共同使用的关系。证明 (5) 必须保留接下来的
两个临界项；不能由普通的 principal-part 乘法直接得出。

## 2. Faber 常数在临界处的真实一阶分母

写
$$
x(z)=z^{-2}+\sum_{n\ge1}w_nz^{6n-2}.
$$
对 $n<s$，$w_n$ 整；第一处可能的 $p$ 分母是 $w_s$。
其准确首分母由原椭圆对数支付。令
$$
u=x^{-1/2},\quad v=-y/x^{3/2},\quad v^2=1+bu^6,\quad dz=du/v.
$$
在 $z(u)$ 的 $u^p$ 系数中，
$$
z(u)=u+\cdots+\frac{h_s}{p}u^p+\cdots,\qquad h_s\equiv H\pmod p.
\tag{8}
$$
确实 $h_s=[u^{p-1}]v^{-1}$，而 R336 的 Cartier 规范给此值为 $H$。
较低系数的全部分母均为单位。反演 (8) 时，第一处 $1/p$ 的留数
只由这一项线性贡献：$u=z+\cdots-h_sz^p/p+\cdots$。再取 $x=u^{-2}$，
得到
$$
\boxed{p w_s\equiv2H\pmod p.}
\tag{9}
$$
这是同一个原正式坐标的换元，不能用一个任意的形式参数替代。

$F_s$ 的 Laurent 常数恰为
$$F_{s,0}=\frac{w_s}{p-2},$$
因为它由 $D^{p-3}(w_sz^{p-3})/(p-2)!$ 给出。
其余 $F_{j,0}$ 在 $j<s$ 时整。因此在
$$
P(z)=\sum_{j=1}^{s}\alpha_jz^{-6j}+t_0+O(z^6)
$$
中，(2)、(9) 给
$$
\boxed{p t_0\equiv-H\pmod p.}
\tag{10}
$$
注意 (2) 的 Faber 坐标全整，而其 Laurent 常数 $t_0$ 不一定整；
这两件事并不矛盾。

## 3. 真正中间 Cartier 行到 Laurent 三阶行

定义原三阶 Wronskian 多项式
$$
\mathcal F(P)=
-\frac12\{P^2D^3P-3P(DP)(D^2P)+2(DP)^3\}.
\tag{11}
$$
直接以 $Dx=2y,Dy=3x^2$ 计算，$\mathcal F(P)=y\widetilde M(x^3)$，
其中 $\widetilde M$ 是整多项式，次数至多 $3s$，最高系数为 $1-p$。
它约化后正是 R345 的
$$
M=PT+3X(PT'-2P'T),
$$
$$
T=36X(X+b)(P'^2-PP'')-6(7X+4b)PP'.
\tag{12}
$$
这里 (12) 的撇号是 $X$ 导数，(11) 的 $D$ 是原不变导子。
R345 已证明
$$[X^{2s}]M=\eta,\qquad [X^{3s}]M=1.\tag{13}$$

需要准确支付从 (13) 到 (11) 的临界换元。对任意整
$\widetilde M=\sum_{r=0}^{3s}m_rX^r$，有
$$
\boxed{
[z^{-2p-1}]\,y\widetilde M(x^3)
\equiv-m_{2s}-2H m_{3s}\pmod p.
}
\tag{14}
$$
而且此 Laurent 系数本身整，所以它对整 polynomial lift 良定义。

证明可逐个单项式进行，使用真实恒等式
$$
yx^{3r}=\frac{D(x^{3r+1})}{2(3r+1)}.
\tag{15}
$$
$r<2s$ 时极阶不足，不贡献。$r=2s$ 时 $3r+1=p$，直接读取
$yx^{6s}$ 的首项得 $-1$。若 $2s<r<3s$，目标系数为
$$-\frac{p}{3r+1}[z^{-2p}]x^{3r+1}.$$
内层只读到低于 $p-1$ 的相对 jet，全部整；分母是单位，故模 $p$
为零。最后 $r=3s$ 时，内层第一次读到 $w_s$，其非整部分恰为
$(9s+1)w_s$，乘回后为 $-p w_s$。由 (9) 得 $-2H$，证明 (14)。

将 (13) 代入 (14)，得到完整三阶 Laurent 行
$$
\boxed{[z^{-2p-1}]\mathcal F(P)=-\eta-2H\pmod p.}
\tag{16}
$$
这一步没有把含 $1/p$ 的 Laurent 展开直接约化。

同一修正也能在 R345 的 norm-two 表达中看见：
若 $-z^3y=1+\cdots+Y_sz^{p-1}+\cdots$，则
$$pY_s\equiv3H.$$
因此 $y^p$ 的这个相对阶不是零，而有 $3H$ 项。
由 $R=\mathcal F(P)/y^p$ 的约化得到
$$
[z^{p-1}]R=-[z^{-2p-1}]\mathcal F(P)-3H=\eta-H,
$$
恰与 R345 的 $[z^{p-1}]R=-C_{p-1}$、$C_{p-1}=H-\eta$ 相合。
这个 $3H$ 说明，不能以“它是一个 $p$ 次幂”为由删除临界 carry。

## 4. 常数项的贡献与完整对称三次型

在 (11) 的 $z^{-2p-1}$ 行，任何正阶 regular 部分都不贡献：
两个最大 principal 极与总三阶微分至多给 $2(p-1)+3=2p+1$，
已经恰好达到目标。因此唯一的 regular 贡献来自 $t_0$ 和两个
最高 principal 项。

令 $m=p-1$。把 $P=t_0+z^{-m}$ 代入 (11)，读该项准确得
$$
-\frac12t_0\,m(m+1)(m-4).
\tag{17}
$$
它含一个 $p$，但 $t_0$ 有 (10) 的分母；其约化是
$$\boxed{\frac52H.}\tag{18}$$
因此 (16) 减去此常数贡献后，纯 polar 三阶行是
$$-\eta-2H-\frac52H=-\eta-\frac92H.$$

为核定该行就是 (4)，对有序三元组 $j+k+l=2s$ 记
$a=-6j,b'=-6k,c=-6l$，其基本对称式为 $e_1,e_2,e_3$。
(11) 的完整对称权直接展开为
$$
-\frac{e_1(e_1-1)(e_1-2)}6
-\frac34(2-e_1)e_2-\frac94e_3.
\tag{19}
$$
这里 $e_1=-12s=2-2p$。各 $\alpha_j$ 整，所以前两项模 $p$ 为零；
最后一项准确为 $486jkl$。这证明 (4)–(5)，包括全部交叉项与
ordered-triple 计数。

## 5. 新三次行对充分大普通素数是单位

R345 的固定参考曲线 $E^\circ:y^2=x^3+1/4$ 给
$\pi^\circ=\pi\eta$、$\bar\pi^\circ=\bar\pi/\eta$，所以
$$H/\eta\equiv a_p(E^\circ)\pmod p.$$
因此 (5) 右端为
$$
-\frac{\eta}{2}\{2+9a_p(E^\circ)\}\pmod p.
\tag{20}
$$
对 $p>331$，Hasse 界给
$$|2+9a_p(E^\circ)|\le2+18\sqrt p<p.$$
这个整数不可能为零，因为模九为二。因此它不被 $p$ 整除，
证明 (5) 的单位性。此处的结论覆盖全部充分大普通素数，不是由
若干有限样本推断。

(20) 是新三次型的实际非零输入。不过 (3) 的线性行和二次行
仍是不同的观察；本证明没有将新单位行直接认作它们之一。

## 6. 完整 norm-three 在旧第一行上的准确投影

保留原 $\sigma(\delta z)=\delta x\sigma^3$ 与
$\sigma(\bar\pi z)=\bar\pi\sigma(z)^pP(z)$，两种复合次序给
$$
\boxed{
P\,W(P)=\delta^{p-1}x^pP(\delta z)-p xP^3,\qquad
W(P)=(DP)^2-PD^2P.
}
\tag{21}
$$
这是先在特征零中的完整式；最后一项来自
$D^2\log P=-\bar\pi^2x(\bar\pi z)+p x(z)$。不能先删去它再处理
任意临界系数。

现在只取 $z^{-2p-6}$。它离最高极的距离为 $p-7$，严格小于
第一分母出现的 $p-1$。因此这一行的全部系数整，(21) 的 $p$ 项
确实消失；$x^p$ 的所有较低相对系数也在这段模 $p$ 为零。
右边只留下 $\delta^{-6}\alpha_1=-\alpha_1/27$。

左边的三个 principal 指标满足 $i+j+k=2s+1$，没有 regular 项。
对导数指数 $a,b',c$，$P W(P)$ 的对称权是
$$e_2-\frac{e_1^2-e_1}{3}.$$
这里 $e_1=-6(2s+1)\equiv-4$，所以它准确变成
$36(ij+ik+jk)-20/3$，即 (6)。

这条投影与 §§2–4 的临界计算不同：这里只在严格低于第一分母的
范围中删去 $p$ 项，不能把相同做法移到 (16) 的 $p-1$ 临界阶。

## 7. 同一原 Hirota 行与第二观察

真实 kernel 在特征 $p$ 满足
$$
D^2\log P=-H^2x(V).
$$
因为 $D^2x(V)=6H^2x(V)^2$ 且 $g_2=0$，得到
$$
\boxed{P D^4P-4(DP)(D^3P)+3(D^2P)^2=0.}
\tag{22}
$$
取 $z^{-p-9}$，其 principal 指标为 $j+k=s+1$；正则部分不贡献，
且与最高极的距离仍为 $p-7$，因此无临界分母遗漏。

对两个导数指数 $a=-6j,b'=-6k$，其和为 $-5$ 模 $p$。直接对称化
(22) 的权，准确得到 $8(ab'-7)(ab'-15)$；$ab'=36jk$，即 (7)。
在同一个行上，旧第二观察的权是
$$
-18(j-k)^2-3(s+1)=72jk-15\pmod p.
\tag{23}
$$
于是若两旧行同零，实际约束包括 $\alpha_1=0$、(6) 的左边为零、
(7) 与 $\mathcal Q=0$，而 (5) 的三次型仍必须是指定的非零单位。

这些关系给出一个明确的实际消元问题：必须在完整 (21)–(22) 的
全部 coefficient relations、真实核规范及 (2) 中，证明新三次型
受两指定旧行控制，才能利用 (5) 导出联合非零。本篇没有声称已经
完成这项理想归属，也没有用新行的非零取代它。

## 8. 唯一既有纤维的精确核定

以下只复用 R336 的 $p=13,b=17$，没有新素数扫描。取整 polynomial
lift $P=X^2-6X-6$。原基给
$$
F_1=X+\frac{2b}{5},\qquad
F_2=X^2+\frac{6b}{7}X+\frac{4b^2}{77},\qquad
\alpha_1=-\frac{144}{7}\equiv11.
$$
实际常数及三阶系数是
$$
t_0=\frac{82113}{637},\qquad
13t_0\equiv7=-H,\qquad H=6,\quad \eta=9,
$$
$$
\mathcal K_{\rm polar}=186\alpha_1^2\equiv3,\qquad
\text{常数贡献}=2,\qquad
[z^{-27}]\mathcal F(P)=-\frac{84528}{49}\equiv5.
$$
恰有
$$3+2=5=-\eta-2H,\qquad
3=-\eta-\frac92H\quad\text{于 }\mathbf F_{13}.$$
这些数在执行环境断开前已用有理数精确运算核定。本文全部素数的
论证在 §§2–7；此单个纤维只核常数与符号，不承担无穷推断。

本结果经仓库连接器提交小文本时，执行环境不可用；该操作是
GitHub Contents API 提交，不冒称为一次本地 git pull。
