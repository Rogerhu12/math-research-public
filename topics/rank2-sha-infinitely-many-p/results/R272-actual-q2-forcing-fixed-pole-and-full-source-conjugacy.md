# R272 — 原 q=2 余项的准确强迫、固定单位极与完整三层来源共轭

日期：2026-11-13。**状态：实际余项方程、全部强迫系数、原八次因子的固定极、同一有限目标上的准确共轭及模 $p^3$ 的完整来源算子均已证明。尚未证明该算子在原有限来源核上产生所需深提升，未证明原三中央导数不能同时为零。**

本篇继续 R252/R257 的原角参数及已付 conductor 的来源。
真实 $U(q)$ 不改成自由函数；完成来源上的自同构不冒称原有限次数来源的自同构。

## 1. 原函数与确定的整余项

固定 $p=4r-1\ge19$，仍取
$$
q=2(1-\sqrt{1-s}),\quad s=q-q^2/4,\quad F(q)=a(q)e^{Z(q)},
$$
$$
a(q)=\frac15(1-q/2)(1-q/4)(1+q-q^2/4)((1-q/2)^4+4).
\tag{1}
$$
这里 $Z=\log\vartheta^{68}$ 保原 theta 初值。R252 的准确公式为
$$
\mathscr L_0Z=17,\quad
\mathscr L_0=q(4-q)\partial_q^2+3(1-q/2)\partial_q,\quad
z_n=[q^n]Z=\frac{34}{n4^n}\frac{(1/2)_n}{(3/4)_n}.
\tag{2}
$$
令
$$
h_j=\frac{(3/4)_j}{j!\,4^j(4j+1)},\quad
h_+=\sum_{j=0}^{r-1}h_jq^j,\quad H=q^rh_+,
$$
$$
a_0=pz_r\in\mathcal O^\times,\quad A=a_0h_+,\quad
L_0=[\log F]_{<r},\qquad \mathcal O=\mathbb Z_p.
\tag{3}
$$
加入原固定系数域时同理。原首 carry 给
$a_0\equiv68\binom{2r-2}{r-1}/4^{r-1}\pmod p$。
在特征零形式级数中定义
$$
U_\theta=q^{-r}(Z-[Z]_{<r}-a_0H/p),\quad
U_a=q^{-r}(\log a-[\log a]_{<r}),\quad U=U_\theta+U_a.
\tag{4}
$$
于是
$$
\boxed{\log F=L_0+q^rA/p+q^rU.}
\tag{5}
$$
准确有 $U_\theta(0)=0$。R252 的原负一层只有次数
$r,\ldots,2r-1$，由 (2) 的系数比直接得 (3) 的全部首负层。
因此 $U\bmod q^{2r}$ 全部整；这正是原 $q<3r$ 窗口的实际余项。
本文不宣称 (4) 的无限级数全部整。

## 2. theta 余项的准确仿射方程

置
$$
\mathscr L=q(4-q)\partial_q^2+(5-2q)\partial_q-\frac3{16}.
\tag{6}
$$
对任意 $V$，逐项微分给准确特征零共轭
$$
\boxed{q^{-r}\mathscr L_0(q^rV)
=\mathscr LV+
p\{(2-q/2)V'+rV/q-(p+4)V/16\}.}
\tag{7}
$$

**定理 1。** 原 $U_\theta$ 满足
$$
\boxed{[\mathscr L+
p\{(2-q/2)\partial_q+r/q-(p+4)/16\}]U_\theta
=\mathcal T_{p,r}(q),}
\tag{8}
$$
其中 $\mathcal T_{p,r}$ 为次数恰 $r-1$ 的整多项式，全部系数为
$$
\boxed{
[q^j]\mathcal T_{p,r}=
\begin{cases}
\displaystyle
a_0h_j\frac{80j^2+20jp+136j+17p+53}
                 {64(j+1)(4j+5)},&0\le j<r-1,\\[2mm]
\displaystyle a_0(2r-1)h_{r-1}/2,&j=r-1.
\end{cases}}
\tag{9}
$$
最高系数是 $p$ 单位。在原已整窗口有
$$
\mathscr L\overline{U_\theta}
\equiv\overline{\mathcal T_{p,r}}\pmod{q^{2r-1}}.
\tag{10}
$$

**证明。** 由 (2)、(4)，右端准确为
$$
q^{-r}\{17-\mathscr L_0[Z]_{<r}-(a_0/p)\mathscr L_0H\}.
\tag{11}
$$
单项式公式
$$
\mathscr L_0(q^n)
=n(4n-1)q^{n-1}-n(n+1/2)q^n
\tag{12}
$$
使低于 $r-1$ 的系数由原递推全消；次数 $r-1$ 也由
$a_0=pz_r$ 准确消去，故 (11) 是次数至多 $r-1$ 的多项式。
对 $n=r+j$、$j<r-1$，用
$$
\frac{h_{j+1}}{h_j}
=\frac{(4j+3)(4j+1)}{16(j+1)(4j+5)}
$$
直接算得
$$
\frac{n(n+1/2)h_j-(n+1)(4n+3)h_{j+1}}p
=h_j\frac{80j^2+20jp+136j+17p+53}
             {64(j+1)(4j+5)}.
$$
这给 (9) 内项。末项无 $h_r$，而 $2r-1+1/2=p/2$，
故得其第二行。所有显示分母和 $h_0,\ldots,h_{r-1}$ 都为单位，
末项也为单位。结合 (7) 得 (8)；因 $U_\theta(0)=0$，
其 $q^{-1}$ 项可去。在已整截断约化得到 (10)。$\square$

同一递推还给
$$
\boxed{\mathscr Lh_+\equiv0\pmod p.}
\tag{13}
$$
内项相消；最高项系数为 $-((r-1)r+3/16)$，模 $p$ 为零。
所以将原允许的 $a_0$ 改为 $a_0+pc$ 时，
$U_\theta$ 改为 $U_\theta-ch_+$，但 (10) 的强迫不变。
(9) 的模 $p$ 非齐次项不能通过重新选择这个下一位消去。

## 3. 原八次因子放回后的固定单位极

完整来源必须用 $U$。其准确方程为
$$
\boxed{
[\mathscr L+p\{(2-q/2)\partial_q+r/q-(p+4)/16\}]U
=\mathcal T_{p,r}
 +q^{-r}\mathscr L_0(\log a-[\log a]_{<r}).}
\tag{14}
$$
右边可以有一个被 $p$ 整除的 $q^{-1}$ 项；模 $p$ 时它消失。

**定理 2。** (14) 右边约化给一个确定的有理函数，在原点正则，且
$$
\boxed{\mathcal T^{\rm full}_p=N_p/a^2,\qquad\deg N_p\le r+15.}
\tag{15}
$$
在同一已整窗口，
$$
\mathscr L\overline U\equiv\mathcal T^{\rm full}_p
\pmod{q^{2r-1}}.
\tag{16}
$$
它在 $q=4$ 有准确的单位简单极：
$$
\boxed{\operatorname{Res}_{q=4}
       \mathcal T^{\rm full}_p(q)\,dq=4^{-r}\ne0.}
\tag{17}
$$
其他可能极仅在固定 $a$ 的零点，阶至多二。

**证明。** 对 $g=\log a-[\log a]_{<r}\in q^r\mathcal O[[q]]$，
(12) 给 $q^{-r}\mathscr L_0g$ 唯一负项为
$rp[q^r]g/q$，约化后为零。同时
$$
\mathscr L_0\log a
=q(4-q)\frac{a''a-(a')^2}{a^2}
 +3(1-q/2)\frac{a'}a.
\tag{18}
$$
清 $a^2$ 后此项分子次数至多十六；
$a^2\mathscr L_0[\log a]_{<r}$ 的次数至多 $r+15$。
约化后的差分子被 $q^r$ 整除。再加
$a^2\overline{\mathcal T_{p,r}}$，即得 (15)。

由原 (1)，$a(4)=0$、$a'(4)=1/4$，故在所有当前素数下均为简单根。
写 $x=q-4$，则 $(\log a)'=x^{-1}+O(1)$、
$(\log a)''=-x^{-2}+O(1)$。(18) 的极部准确为
$$
\frac q{q-4}+\frac{3-3q/2}{q-4}
=-\frac12+\frac1{q-4}.
$$
低多项式和 $\mathcal T_{p,r}$ 在此都正则。乘 $q^{-r}$
就得到 (17)。$\square$

这个固定极来自原 carrier 的真零，不是任意余项模型制造的。
但 (17) 没有证明原有限核向量乘上它后仍有极；
核向量本身可能参与取消，仍须在实际来源中计算。

## 4. 同一有限目标上的完整参数与来源共轭

取原窗口 $k=2r+s_0$、$0\le s_0<r$，写
$$
\mathcal A_3=(\mathcal O/p^3)[q,z]/
       (q^r-pz,\ z^3,\ q^{s_0}z^2).
\tag{19}
$$
其基为 $q^az^b$：$b=0,1$ 时 $0\le a<r$，
$b=2$ 时 $0\le a<s_0$。这是原加权前三块。
在此目标中，实际来源和 R252 首模型为
$$
\mathcal R=q e^{L_0(q)}e^{(A(q)+pU(q))z},\qquad
\mathcal R_*=q e^{L_0(q)}e^{A(q)z}.
\tag{20}
$$
指数取 nilpotent 目标内的有限和。对已整 $U\bmod q^{2r}$ 选任意整形式提升；
改变更高系数不影响 (20)，因为 $q^{2r}pz=p^3z^3=0$。

令
$$
D=rA+qA'\in\mathcal O[[q]]^\times.
\tag{21}
$$
形式 Hensel 唯一给 $v\in1+p\mathcal O[[q]]$，满足
$$
A(qv)v^r=A(q)+pU(q).
\tag{22}
$$
其关于 $v$ 在 $1$ 的导数为单位 $D$，故每一精度唯一。
置 $\theta=qv$。映射
$$
\boxed{\sigma(q)=\theta,\qquad\sigma(z)=zv^r}
\tag{23}
$$
是 (19) 的整自同构：三个关系分别乘单位
$v^r,v^{3r},v^{s_0+2r}$，且线性项可逆。

径向来源也必须变换。定义
$$
M(q)=v\exp(L_0(\theta)-L_0(q)).
\tag{24}
$$
该指数属于 $p\mathcal O[[q]]$，所以收敛且整。由 (20)、(22) 得
$$
\boxed{\sigma(\mathcal R_*)=M\mathcal R.}
\tag{25}
$$
在完成来源 $\mathcal O[[q]][R]$ 上定义
$$
\boxed{\Phi(q)=\theta,\qquad\Phi(R)=MR.}
\tag{26}
$$
令 $\mathcal E_*,\mathcal E$ 分别把 $R$ 送到
$\mathcal R_*,\mathcal R$。对每个原多项式 $P$，准确有
$$
\boxed{\sigma\mathcal E_*(P)=\mathcal E(\Phi P).}
\tag{27}
$$
每个原质量 $m$ 块都保留 $M^m$；它不是一个与 $m$ 无关的常数。

## 5. 完整来源算子到模 p³

置
$$
h=U/D,\quad B=1+qL_0',\quad
\mathscr E=q\partial_q+BR\partial_R,\quad
D_2=q^2A''+2rqA'+r(r-1)A.
\tag{28}
$$
$D_2=qD'+(r-1)D$。由 (22) 的二阶 Taylor 式，
$$
v=1+ph-\frac{p^2D_2}{2D}h^2\pmod{p^3}.
\tag{29}
$$

**定理 3。** (26) 的完整作用为
$$
\boxed{
\Phi=1+ph\mathscr E+
\frac{p^2h^2}{2}
\{\mathscr E^2-(r+qD'/D)\mathscr E\}\pmod{p^3}.}
\tag{30}
$$
系数都在算子的左侧。其逆准确为
$$
\boxed{
\Phi^{-1}=1-ph\mathscr E+\frac{p^2h^2}{2}\mathscr E^2+
p^2\left\{\frac{qUU'}{D^2}
 +\frac{h^2}{2}(r-qD'/D)\right\}\mathscr E
\pmod{p^3}.}
\tag{31}
$$
这些式子不除 $U$，所以 $U$ 有零点时也成立。

**证明。** 在一般单项式 $q^jR^m$ 上，令 $K=j+mB$，则
$\mathscr EP=KP$、$\mathscr E^2P=(K^2+mqB')P$。
(24)、(26) 的准确乘子为
$v^{j+m}\exp(m(L_0(qv)-L_0(q)))$。
将 (29) 代入其对数再指数化，用
$qB'=B-1+q^2L_0''$，逐项即给 (30)。
求逆时保留
$$
(h\mathscr E)^2=h^2\mathscr E^2+hqh'\mathscr E,\quad
hqh'=qUU'/D^2-h^2qD'/D.
$$
在 $1+pA+p^2C$ 的逆 $1-pA+p^2(A^2-C)$ 中代入 (30)，得 (31)。$\square$

因此第一阶不仅有 $qUD^{-1}\partial_q$，同时还有
$UD^{-1}(1+qL_0')R\partial_R$；第二阶还必须保留 (30)--(31)
的全部径向项与系数交换项。

## 6. 原有限来源及下一层障碍

R249/R252 已付 conductor 后的实际带为
$$
\mathcal V_n=\bigoplus_{\substack{0\le m\le n\\0\le j\le24m}}
\mathcal O R^mq^j.
\tag{32}
$$
(27) 成立于完成来源；(30) 中 $h,B$ 一般不在原固定角次数内。
所以没有证明 $\Phi(\mathcal V_n)=\mathcal V_n$，准确有限核比较只能写成
$$
\boxed{
\ker(\mathcal E|_{\mathcal V_n})
=\{P\in\mathcal V_n:\mathcal E_*(\Phi^{-1}P)=0\}.}
\tag{33}
$$
(31) 的完整项须在同一目标 (19) 中评价。将 $\Phi^{-1}P$
换成同次数多项式，必须另外证明真实同值和整性。

由原 $h_++4qh_+'=(1-q/4)^{r-1}\pmod p$，
$$
D^{-1}=\frac4{a_0}(1-q/4)^{-(r-1)}\pmod p.
\tag{34}
$$
(30)--(31) 因而明确给出可能取消时的真实分子：
$U\mathscr EP$、$U^2\mathscr E^2P$、$UU'\mathscr EP$ 和
$U^2D'\mathscr EP$，其中包含原低轴 $L_0$。
只计算 $U\partial_qP$ 会漏掉同阶原项。
(8)、(14)、(17) 又固定了系数的强迫和固定极，但尚未证明它们在
原 $F^2$ 核上发生足够取消。

原三中央零仍只能通过 R247/R270 等实际聚合同余加入；
它们不使 (32) 的所有列都成为中央零来源。
下一问题是在同一原核上计算 (33) 的有限来源障碍，
或将上述完整强迫与原三曲线连接比较后得到真实非零输入。

## 精确证书与依赖

[脚本](../scripts/check-q2-actual-forcing-and-source-conjugacy.py) 以符号参数核实
(7)、(9)、(13)、原 $a$ 的单位极、(29)--(31) 的一般单项式作用及逆算子；
[输出](../scripts/check-q2-actual-forcing-and-source-conjugacy.json) 保存零余项。
它们是原有理恒等式的精确证书，不是目标素数扫描。
有限来源、原 $Z$ 递推、整窗口和 source charge 分别沿用
R243/R249、R252、R173/R199/R224；R257 的实际角逆成本继续有效。
