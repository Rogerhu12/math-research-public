# R337：真实平移留下的第三面积排除同号反射弱块架构

日期：2026-11-15。**完整原式纸面证明。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R334](R334-positive-dilations-pay-the-full-second-Gaussian-area-with-the-old-layer.md) 已在同一个真实弱圆上完成两个 Gaussian 面积的全部三矩，并保留原三条 directed 行、$\Psi$ 与指定完整一层。本稿检查另一个真实面积 $A_{-1,-2}$ 的第零外矩。

原算子的显式 $x$ 必须一起平移。新的完整项不是仅由外积分中心化得到：它恰是一个已付条件下等于 $2C/3$ 的 $[R,S]$ 外矩。对中心反射的弱基块，这使新面积等于“实际物理中心 $\times C$”的非零倍数。R331 的充分大 $L$ 分支具有 $C<0$；所有真实中心在正物理区间内。因此其十二副本及任何正四次混合不能消去此项。

结论只排除本稿明确界定的同号反射弱块架构，包括 R334 所用的该分支。没有排除一般弱单 hook 圆，也不排除加入真正 $C>0$ 的新弱块或改变局部反射结构。

主要来源：[R259 原 E8 与全部面积矩](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R317 完整 mixed 恒等](R317-exact-weak-hook-mixed-correction-and-nonnegative-branch-obstruction.md)、[R331 内常项与实际宽补偿](R331-interior-constant-and-wide-moment-repair-pay-the-new-area-and-old-layer.md)、[R332 真实平移与反射](R332-true-translation-and-reflection-pay-the-next-Gaussian-area-moment.md)、R334，以及 [R249 原 Gaussian 词独立](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md)。

## 1. 真实对象与所检查的必要门

保持 R331/R334 的同一个共振 Gaussian 端芽和固定非零参数
$$
0<t:=\kappa^2<1/100,\qquad h_e>0.
$$
沿用
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U=\Phi_{s_1},
$$
$$
W_*=aR+bS,\qquad Z_*=d_*L+e_*U,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},
$$
$$
d_*=\frac{6\kappa t}{h_e},\qquad
e_*=-\frac{\kappa(15t+1)}{4h_e}.
\tag{1}
$$
此处 $B_{-2}=W_*$、$B_{-1}=Z_*$。

对
$$
u=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u,
$$
定义待检查的真实外矩
$$
\mathcal B_0(\theta)
=I_0\{u,[Z_*,W_*](u;D)\}.
\tag{2}
$$
R259 的完整原面积接口及 R249 的词独立性表明：同一个圆通过该端芽的完整第四 ruling，必须使(2)对所有相位为零。二层面积不能由另一层或任意合法第二 gauge 的一层项抵消。

下文只使用此前已经准确支付的
$$
\mathfrak H(u;D)=0,\qquad
m_j:=I_j\!\left(u,J\{u''((f'')^2-(u'')^2)\}\right)=0,
\quad j=0,1,2,
\tag{3}
$$
及需要处的
$$
A_0(\theta):=I_0\{u,[Z_*,P](u;D)\}=0.
\tag{4}
$$
在十二副本之前的反射基块，(4)只先在 $\theta=\pi/2$ 成立；其剩余交叉相位会在第6节原样保留，不能提前删掉。

## 2. 完整 $[R,S]$ 第零矩，保留原 primitive

写
$$
p=f',\quad q=f'',\quad v=u',\quad r=u'',\quad
d=q^2-r^2,\quad A=Jd,\quad B=J(xd).
$$
完整三矩圆使 $A$ 及 $RD,SD$ 真紧，但下面的外配对化简也保留一般二次原尾。

由
$$
R(u,w)=u'w'+xJ(u''w''),\qquad
S(u,w)=J(xu''w''),
$$
直接两次求导并只对紧 outer 的系数分部积分，准确得
$$
\boxed{
I_0\{u,R(u,w)\}
=\int\left(xrr'-vr'-\frac{r^2}{2}\right)w'',
}
$$
$$
\boxed{
I_0\{u,S(u,w)\}=\int xrr'w''.
}
\tag{5}
$$
边项都含紧 outer 的端 jets；没有假定一般 $w$ 或单包二次输出紧支撑。

原同锚 inner 二导为
$$
(SD)''=-d-xd',\qquad
(RD)''=2(pq'-vr')-xd'.
\tag{6}
$$
把(6)代入(5)，定义
$$
Y=\int vr\,d',\qquad
Z=\int xr^2d',\qquad
W=vq-pr,\qquad
J_x=\int xWq'r',
$$
得到完整恒等
$$
\boxed{
I_0\{u,[R,S](u;D)\}=Z-Y+2J_x.
}
\tag{7}
$$

一个直接的核对是先把 $D$ 换成 $f\odot f$。此时(5)的差化为
$$
-\int vr(q^2)'+\int xr^2(q^2)'+2J_x
=Z-Y+2J_x+\frac16\int r^4.
$$
减去真实 diagonal
$I_0\{u,[R,S](u;u^2)\}=\int r^4/6$，即得(7)。这个相减保留了同一个右锚，没有将两个非紧输出分开假设为紧。

弱 hook 与旧面积的 R317 原身份是
$$
Y=-\frac23C-2J,\qquad
Z=C,\qquad
J_x=-\frac C2-J,
$$
$$
C=\int r^2(q^2-r^2),\qquad
J=\int Wrq'.
\tag{8}
$$
因此在(3)下，
$$
\boxed{
I_0\{u,[R,S](u;D)\}=\frac23C_\theta.
}
\tag{9}
$$
它一般不为零。不能把 rank-one 模块上常见的 $C_\theta=0$ 推给当前真正弱 rank-two 曲段。

## 3. 平移两个原算子，而不是只搬外矩

设 $T_s f(x)=f(x-s)$。R332 的完整原式给
$$
P^{(s)}=P,\quad
R^{(s)}=R+sP,\quad S^{(s)}=S+sP,
$$
$$
L^{(s)}=L+\frac s2(S-R),\qquad
U^{(s)}=U+s(R+2S)+\frac{3s^2}{2}P.
\tag{10}
$$
记
$$
V_*=(e_*-d_*/2)R+(2e_*+d_*/2)S.
$$
于是
$$
Z_*^{(s)}=Z_*+sV_*+\frac{3e_*s^2}{2}P,\qquad
W_*^{(s)}=W_*+s(a+b)P.
$$
完整 commutator 展开为
$$
\begin{aligned}
[Z_*^{(s)},W_*^{(s)}]
={}&[Z_*,W_*]+s(a+b)[Z_*,P]+s[V_*,W_*]\\
&+s^2\left\{(a+b)[V_*,P]
+\frac{3e_*}{2}[P,W_*]\right\}.
\end{aligned}
\tag{11}
$$
三次项是 $[P,P]=0$，不是被截断。

有
$$
[V_*,W_*]=\chi_\kappa[R,S],
$$
$$
\boxed{
\chi_\kappa=(e_*-d_*/2)b-(2e_*+d_*/2)a
=\frac{\kappa(28t^2-35t-4)}{64h_e^3}\ne0.
}
\tag{12}
$$
在本稿参数区间，括号严格负。

由弱 hook，原 $[R,P]$ 与 $[S,P]$ 分别是同一个 $J(u''d)$ 槽的 $1/3$ 与1。故(3)准确消去(11)的整个二次平移项。第零外矩没有额外外 $x$ 权，于是
$$
\boxed{
\mathcal B_0^{(s)}
=\mathcal B_0+s(a+b)A_0
+\frac23s\chi_\kappa C_\theta.
}
\tag{13}
$$
特别，若该相位已经通过(4)，
$$
\mathcal B_0^{(s)}
=\mathcal B_0+\frac23s\chi_\kappa C_\theta.
\tag{14}
$$
式(13)是后面复制计算所用的完整式。不能对每个尚未清交叉相位的基本块提前使用(14)。

## 4. 中心反射的准确结论只在模二次原尾后成立

先用辅助中心坐标 $y$。假设实际 $f,g$ 分别有确定奇偶性，并在所考察相位 outer $u$ 也有确定奇偶性；此外 $D$ 的二次密度为偶。R331 的中心偶 pair 对每个相位满足此条件；R334 两斜率基块在 $\theta=\pi/2$ 也满足。

完整三矩给
$$
PD\text{ 为紧奇函数},\qquad
RD,SD\text{ 为紧偶函数},\qquad
LD,UD\text{ 为紧奇函数}.
\tag{15}
$$
这些是原同锚结论。例如 $Jd$ 的 integrand 偶且总积分零，所以它真为奇；$J(yd)$ 为偶；$J(y^2d+2((f')^2-(u')^2))$ 因第2矩零而真为奇。

outer 二次输出不能因此全部假称紧。原完整极化式是
$$
P(u,w)=J(u''w''),\quad
R(u,w)=u'w'+yP(u,w),\quad
S(u,w)=J(yu''w''),
$$
$$
\begin{aligned}
L(u,w)={}&\frac{uw'+u'w}{2}
-\frac y2u'w'-\frac{y^2}{4}P(u,w)\\
&+\frac14J(y^2u''w''+2u'w'),
\end{aligned}
$$
$$
U(u,w)=yu'w'+yJ(yu''w'')
+\frac12J(y^2u''w''+2u'w').
\tag{16}
$$
对紧偶 integrand，右 $J$ 是“奇函数加其真实半总积分”；对紧奇 integrand，右 $J$ 为偶。代入(16)，若 $u$ 的奇偶号为 $\epsilon_u$，则
$$
[Z_*,W_*](u;D)
=\text{奇偶号为 }-\epsilon_u\text{ 的函数}
+\text{真实二次多项式}.
\tag{17}
$$
这里的二次多项式由原积分决定，没有任意设置其系数。

$I_0$ 中相反奇偶的部分积分为零；实际二次尾也准确不可见，因为
$$
I_0(u,p_2)=p_2''\int u''=0.
$$
外 $u$ 紧且其支撑关于中心对称，故物理 $I$ 本身无需关于中心对称。于是
$$
\boxed{\mathcal B_0=0\quad\text{在上述中心坐标计算中}.}
\tag{18}
$$
必须随后用(13)恢复物理中心。不能由(18)直接断言任意正位置上的真实面积为零。

## 5. R331 的真实 $C<0$ 分支

R331 在十二副本以前保有关于一个中心的完整偶 pair。它已付旧面积全部三矩，并用真实内部常数使
$$
A_0(\pi/2)=0.
$$
其实际 $C$ 在该相位为
$$
\boxed{
C_b=-4W_8(J_0+J_{x,0}+Lj_0),
\qquad j_0>0.
}
\tag{19}
$$
所有宽 cutoff、三个宽矩补包和强面积修正已经包含在该身份中。它由旧面积的原恒等给出，不是只计算内部幂曲段后省略其它支撑。

R331 取充分大的有限 $L$ 取得负 $\Psi$。在同一充分大分支可同时且严格保证
$$
C_b<0.
\tag{20}
$$
本稿指的当前架构就是这一实际分支；不将(20)扩大到任意未受限制的有限 $L$ 或任意弱圆。

由(18)、(13)，把该反射基块放到真实中心 $X$ 后，在 $\theta=\pi/2$ 准确有
$$
\boxed{
\mathcal B_0(\pi/2)
=\frac23\chi_\kappa X C_b.
}
\tag{21}
$$
$X$ 是原物理坐标的中心，不是可在公式里自由重置的标签。若该完整反射支撑放在严格正物理区间，必有 $X>0$。

## 6. 十二副本：保留全部实际中心与正权

在 R331 的反射基块上，R328/R331 已给
$$
A_0(\theta)=b_0\cos\theta\sin\theta,\qquad
C_\theta=C_b\sin^2\theta+C_o\cos\theta\sin\theta.
\tag{22}
$$
$A_0(\pi/2)=0$，但不能从(22)删去 $b_0$。

对原十二完整副本，记
$$
\rho_j=\gamma_j^4=\binom{11}{j}>0,\qquad
\epsilon_j=(-1)^j,
$$
并令 $X_j$ 为该副本的**最终真实反射中心**。原等差复制使 $X_j$ 为 $j$ 的一次函数；共同最终平移仍保此性质。由(13)、(18)、(22)，逐副本完整值为
$$
\begin{aligned}
\mathcal B_{0,j}(\theta)=\rho_jX_j\bigg[
&(a+b)\epsilon_j b_0\cos\theta\sin\theta\\
&+\frac23\chi_\kappa
\{C_b\sin^2\theta+\epsilon_j C_o\cos\theta\sin\theta\}
\bigg].
\end{aligned}
\tag{23}
$$
十一差分只消去其中带 $\epsilon_j$ 的项：
$$
\sum_j\rho_j\epsilon_jX_j=0.
$$
它不消去正四次权的中心平均。因此
$$
\boxed{
\mathcal B_0(\theta)
=\frac23\chi_\kappa C_b
\left(\sum_{j=0}^{11}\rho_jX_j\right)\sin^2\theta.
}
\tag{24}
$$
所有 $X_j>0$ 时，括号严格正。没有把十二副本的中心假设为同一个数，也没有用有符号 cube 差分替代真实四次权。

更一般，对有限个这种弱反射基块及其完整复制，令最终正四次权为 $\rho_\nu>0$、真实中心为 $X_\nu>0$、该基块自己的 $C_\nu<0$。在 $\pi/2$ 的完整贡献准确为
$$
\boxed{
\frac{\mathcal B_0(\pi/2)}{\chi_\kappa}
=\frac23\sum_\nu \rho_\nu X_\nu C_\nu<0.
}
\tag{25}
$$
式(25)保留不同基块不同的真实 $C_\nu$；不需要它们相等。

## 7. R334 新强面积模块与控制器不能抵消该值

先看 R267/R334 的未复制两斜率基块。两组都用偶母包和对称中心；组数分别为 $2^{17}$、$2^{11}$，TM 反序号均为负。因此在其中心坐标
$$
f\text{ 为奇},\qquad g\text{ 为偶}.
$$
在 $\theta=\pi/2$，(15)–(18)适用，给中心 $\mathcal B_0=0$。

它的旧完整面积及三矩已零，且 R267 原 self 表给 $A_0=0$ 全角。同时，其准确四次张量是
$$
A_4=5C_{22},\quad E_4=C_{22},\quad B_4=D_4^{\rm tens}=0,
$$
所以 $C_\theta=0$ 全角。由(13)，任意真实平移不改变其 $\mathcal B_0$。正伸缩对该面积的第零矩给完整因子 $\Lambda^{-6}$，因此零值也保持；任意正四次幅同样保持零。

实际上，这些模块的整个 $\mathcal B_0(\theta)$ 在十二复制后为零。中心反射使其两个 even 相位系数为零：原 pair 的总空间权为 $-3$，中心反射将面积变号，而 $f\mapsto-f,g\mapsto g$ 保 even 相位不变。真实尾的差只为二次多项式，已由(18)准确处理。剩余两个 odd 相位在平移不变的前提下由十二副本清去。因此
$$
\mathcal B_0(\text{每个 R334 强面积模块})=0
\quad\text{全部 }\theta.
\tag{26}
$$

最后的 R280/R293 强控制宏块本身有全部72面积为零，包含当前 $A_{-1,-2}$ 的第零矩。R334 的有限频率过程保持其原 $\mathcal F_\star$，所以该零值在实际有限频率根上仍准确成立。它没有提供一个隐藏的反号补偿。

不同完整三矩块间，$XD$ 真紧，nested 输出的二次左尾与另一个紧 outer 的原 $I_0$ 正交。故以上相加是真实原式加法，不是假设微包跨 history 消失。

于是对 R334 的最终圆，(24)或(25)仍是完整 $\mathcal B_0$ 的值。最后共同正幅归一化只乘一个正四次因子，严格非零保持。

## 8. 准确结论与下一真实通道

**定理。** 在本稿小共振 Gaussian 端芽上，若弱部分由 R331 充分大 $L$ 的 $C<0$ 反射基块构成，所有最终真实反射中心均在严格正物理区间内，其余部分由 R334 的四个强面积模块及原全72零控制器构成，则该同一圆虽已完成 R334 的全部联合目标，仍有
$$
I_0\{g,[Z_*,W_*](g;f^2-g^2)\}\ne0.
$$
因此不能通过完整第四 ruling 的必要面积门 $A_{-1,-2}$。

这不是一般正区间弱单 hook 圆的否定。证明用到了真实反射结构、每个弱基块 $C_\nu<0$ 和实际中心 $X_\nu>0$；任何一个假设改变，都须重新核原式。

后继不能只把同一负 $C$ 分支平移得更远，或只增加本稿已经证明贡献为零的强模块。可用的新通道必须真正改变有序物理中心与 $C$ 的符号配置，或改变反射基块本身的中心面积值。特别，若能实际构造已付低阶门的 $C>0$ 弱块，(13)提供的是一个不同的真实方向；还必须同时支付它的宽恢复、原矩、其它面积和 $\Psi$ 成本。此项建设不由本稿的非零证明自动授予。
