# R1055 — 原 A24 相对来源的完整二挠迹与混合除 p 返回

按根 README 第8条登记完整证明；原 notes 路径保留转向。除本篇明示的已证范围外，课题主目标仍未完成。

日期：2026-11-27 UTC。**状态：下述固定来源、完整同源迹和两条混合除 $p$ 身份已证明。** 本注不新增 canonical 中央零。它消费 [共同 A24 的完整水平加法](../notes/2026-11-16-common-a24-horizontal-product-and-relative-theta-gluing.md) 的同一个 $T$ 行相对片，而非另选 degree144 截面。原四个收缩 $S,T,U,V$、完整 Gaussian、固定 CM 系数及全 theta 结构保持。

全文为原 sigma 恒等式、完整函数域迹和 Hurwitz 整格的纸面证明，没有数学执行或素数扫描。原 $S/T/U/V$ 的其它双投影及参考配对仍使用 [R884](R884-original-t72-norm-three-heat-and-c24-h22-pairing.md)，本注不重证那些结论。

## 1. 固定原来源与 trace 规范

保持
$$
E_b:y^2=x^3+b,\quad D_zx=2y,\quad y\sim-z^{-3},\quad
X=x^3,\quad\delta^2=-3,\quad\sigma(z)\sim z.
\tag{1}
$$
$b$ 是原固定单位。置
$$
\begin{aligned}
Q_7&=7X^2-4bX+16b^2,\\
A_2&=X^2+20bX-8b^2,\\
P_-&=X^3-96bX^2+48b^2X+64b^3,\\
A_{24}&=\frac{\sigma^{24}}7(X+b)Q_7,\\
H_{48}&=\sigma^{48}X(X-8b)(X+4b)A_2P_- .
\end{aligned}
\tag{2}
$$
于是原 $T=A_{24}H_{48}$。原加法中 $m=24,n=48,g=24$，故
$$
\mathscr F(Z,W)=A_{24}(Z+2W)H_{48}(Z-W),\qquad
R_{144}(W)=\mathscr F(0,W)=A_{24}(2W)H_{48}(W).
\tag{3}
$$
第二式使用 $H_{48}$ 的真实偶性；其 degree 是 $96+48=144$，首项为 $64W^6$。

对原 canonical 标准线丛定义完整迹
$$
\mathrm T_{2,m}(\sigma^{4m}R)(z)
=\sigma(z)^m\operatorname{Tr}_{[2]}
 \frac{R(w)}{(-2y(w))^m},\qquad z=2w.
\tag{4}
$$
这里 $\sigma(2w)=-2y(w)\sigma(w)^4$。因此(4)保全部四个逆像、原 theta 乘子和绝对倍率；它满足完整投影公式及
$\mathrm T_{2,m}[2]^*F=4F$。所有后续 trace 都是特征零完整函数域迹，约化仅删除原固定有限坏集。

## 2. 原 H48 的完整四纤维返回

原已付因子是
$$
H_{48}
=\Theta(w)^2\Theta(2w)\Theta(\delta w)\Theta(3w)
 \frac{\sigma(4w)}{2\sigma(2w)},
\quad
\Theta(w)=\frac{\sigma(\delta w)}{\delta\sigma(w)}.
$$
利用 $\delta^2=-3$ 及 sigma 的奇性，得到绝对式
$$
H_{48}(w)=-
\frac{\sigma(\delta w)\sigma(2\delta w)
      \sigma(3\delta w)\sigma(4w)}
 {2\delta^5\sigma(w)^2\sigma(2w)^2}.
\tag{5}
$$
其原点首项为 $-3/\delta^2=1$，与(2)相同。

令 $z=2w$，目标坐标为 $a=x(z),c=y(z)$，并记
$a_\delta=x(\delta z)$。准确 sigma 加法给
$$
\sigma(u)\sigma(3u)
=(x(u)-x(2u))\sigma(u)^2\sigma(2u)^2.
$$
再代入
$\sigma(\delta w)=\delta x(w)\sigma(w)^3$、
$x(\delta w)=-(X(w)+4b)/(3x(w)^2)$，(5)准确成为
$$
H_{48}(w)=
\frac{\sigma(\delta z)^3\sigma(2z)}
 {12\delta\,\sigma(z)}
\frac{(X(w)+4b)/3+a_\delta x(w)^2}{y(w)}.
\tag{6}
$$
这里的目标 theta 因子为
$$
\frac{\sigma(\delta z)^3\sigma(2z)}{\sigma(z)}
=6\delta\,a^3c\,\sigma(z)^{12}.
\tag{7}
$$
因此(6)已把实际 canonical degree12 框架抽到 trace 之外；没有把四个 lift 各自当成同一个裸解析平移。

完整四纤维的 $x(w)$ 是
$$
F_a(T)=T^4-4aT^3-8bT-4ab=0
\tag{8}
$$
的四个根。对每个 $e^3=-b$，
$F_a(e)=-9be$ 与 $a$ 无关。沿目标不变微分求导，因
$D_zx(w)=y(w)$，得到
$$
\sum_{2w=z}\frac{y(w)}{x(w)-e}=0.
$$
用 $y(w)^2=(x(w)-e)(x(w)^2+ex(w)+e^2)$，三个互异 $e$ 给
$$
\sum\frac1{y(w)}
=\sum\frac{x(w)}{y(w)}
=\sum\frac{x(w)^2}{y(w)}=0.
\tag{9}
$$
另由 $\sum x(w)=4a$ 求导得 $\sum y(w)=8c$，故
$$
\sum\frac{X(w)}{y(w)}=8c.
\tag{10}
$$
这些等式先在一般纤维成立，因而是函数域身份；有限退化点按同一完整 trace 延拓，无须额外舍点。

对(6)用(9)–(10)，并保(7)，得到
$$
\boxed{
\mathrm T_{2,12}H_{48}
=\frac43\,\sigma^{12}X(X+b).
}
\tag{11}
$$

## 3. 同一个 A24 及相对片的 old 部分

为固定(3)中另一个因子的规范，也可直接从完整四次式求得
$$
\boxed{\mathrm T_{2,6}A_{24}=\frac1{14}\sigma^6.}
\tag{12}
$$
具体置 $f=X+b$，目标仍记 $a=x(2w)$。由原倍点公式
$4af=x(f-9b)$，四个 $f$ 满足完整四次式
$
f^4-(28b+64a^3)f^3+270b^2f^2-972b^3f+729b^4=0.
$
对其倒根作 Newton 和，准确给
$$
\operatorname{Tr}f^{-1}=\frac4{3b},\qquad
\operatorname{Tr}f^{-2}=\frac{28}{27b^2}.
$$
而(4)中的完整商为
$$
\frac{Q_7}{7\cdot64f^2}
=\frac1{448}\left(7-\frac{18b}f+\frac{27b^2}{f^2}\right).
$$
其 trace 是 $(28-24+28)/448=1/14$，支付(12)。等价的真实分解为
$$
A_{24}^{\rm old}=\frac1{56}[2]^*\sigma^6
=\frac87\sigma^{24}(X+b)^3,\qquad
A_{24}^{\rm new}=-\frac17\sigma^{24}(X+b)A_2.
\tag{13}
$$

现在定义原相对片返回的固定来源
$$
C_{36}=\frac{\sigma^{36}}7X(X+b)^2Q_7,\qquad C_{36}=z^6+O(z^{12}).
\tag{14}
$$
由(3)、(11)的同一个投影公式，
$$
\boxed{
\mathrm T_{2,36}R_{144}=\frac43 C_{36},\qquad
R_{144}^{\rm new}:=R_{144}-\frac13[2]^*C_{36},\quad
\mathrm T_{2,36}R_{144}^{\rm new}=0.
}
\tag{15}
$$
$R_{144}^{\rm new}$ 仍是同一个 whole degree144 来源，质量为零。
$C_{36}$ 与 R884 的 $A=S\Theta$ 之差准确为
$$
C_{36}-A=\frac{9b}{7}\sigma^{36}X(X+b)Q_7.
\tag{16}
$$
所以不能仅按 degree36、型零或首项一，把 $C_{36}$ 认成那里的 $A,N_{36},J_{36}$ 或一个新的 canonical 来源。

## 4. 同一 C36 的范数三小返回

仍按 $\sigma(\delta w)=\delta x(w)\sigma(w)^3$ 的原规范，有
$$
\boxed{
\mathrm T_{\delta,12}C_{36}
=-\frac1{336}L_{12},\qquad
L_{12}=\sigma^{12}(13X+4b).
}
\tag{17}
$$
以下给出完整三纤维计算。目标 $a=x(\delta w)$，三个 $X=x(w)^3$ 满足
$$
X^3+(12b+27a^3)X^2+48b^2X+64b^3=0.
$$
除去目标 $\sigma^{12}$ 后，原商为
$$
\frac1{7\cdot3^6}
\left(7X+10b+\frac{15b^2}X+\frac{28b^3}{X^2}
+\frac{16b^4}{X^3}\right).
$$
完整 Newton 和为
$$
\begin{aligned}
\operatorname{Tr}X&=-12b-27a^3,\\
\operatorname{Tr}X^{-1}&=-\frac3{4b},\\
\operatorname{Tr}X^{-2}&=\frac3{16b^2}-\frac{27a^3}{32b^3},\\
\operatorname{Tr}X^{-3}&=-\frac3{64b^3}+\frac{243a^3}{256b^4}.
\end{aligned}
$$
代入恰得 $-(13a^3+4b)/336$，没有省去任何一个输入。
于是
$$
C_{36}^{\delta{\rm -new}}
=C_{36}+\frac1{1008}[\delta]^*L_{12},
\qquad \mathrm T_{\delta,12}C_{36}^{\delta{\rm -new}}=0.
\tag{18}
$$
$L_{12}$ 和(18)都保持原点质量零。低 degree 返回仍包含
$13\sigma^{12}X+4b\sigma^{12}$ 的两个真实读者，未把它们赋为常数或单位。

## 5. 原 mixed 除 p 行的准确消费

固定原共同好惰性 $p=6s-1>211$，记
$$
\mathfrak B_m(F)=\frac{D_z^{p+1}F(0)}p\bmod p
$$
作用于相应 whole degree $m$ 的质量零整来源。
其合法整性使用原 R855/R856，非由(11)的特征零 trace 单独推出。

先在特征零保 $2^{p+1}$、$\delta^{p+1}$ 和固定整提升，之后才约化：
$2^{p+1}\equiv4$，$\delta^{p+1}=(-3)^{(p+1)/2}\equiv3\pmod p$。
由(15)、(18)的**来源恒等式**，得到
$$
\begin{aligned}
B_{\rm rel}:=\mathfrak B_{144}(R_{144})
&=\frac43\mathfrak B_{36}(C_{36})
+\mathfrak B_{144}(R_{144}^{\rm new}),\\
\mathfrak B_{36}(C_{36})
&=-\frac1{336}\mathfrak B_{12}(L_{12})
+\mathfrak B_{36}(C_{36}^{\delta{\rm -new}}).
\end{aligned}
\tag{19}
$$
此处没有声称 $\mathfrak B$ 与同源 trace 无缺陷交换；使用的是同一个来源的准确 pullback 分解。

继续使用原水平加法注(25)–(28)的 $J_{r,s}$、
完整低卷积 $\mathcal C_p$，此处 $u=2,v=1$。其两个 mixed 端点现在准确为
$$
\boxed{
\begin{aligned}
J_{p,1}/p
&=2\mathfrak B_{72}(T)-3\mathcal C_p(1,1),\\
J_{1,p}/p
&=-\frac1{504}\mathfrak B_{12}(L_{12})
+\frac23\mathfrak B_{36}(C_{36}^{\delta{\rm -new}})
+\frac12\mathfrak B_{144}(R_{144}^{\rm new})
+\frac32\mathcal C_p(2,-1).
\end{aligned}}
\tag{20}
$$
所有式均在同一个原剩余域中；$\mathcal C_p$ 保原 $A_{24}$、
$H_{48}$ 的每个低 jet，未将它替成只依 charge 的函数。

原四条中央必要零成立时，可以删除第一行的
$\mathfrak B_{72}(T)$，不能删除第二行显示的任一个新余项或
$\mathcal C_p$。另外三条原 $S,U,V$ 收缩仍须使用各自实际伙伴；
本注不把它们换成(3)的相对片。

因此本注真正减少的是原 $T$ 相对端点里可明确剥离的完整
二挠及范数三 old 部分；余下的两个指定 new 读者和完整低卷积
已写在(20)，没有以环境分解增加第五条 canonical 条件。
下一步若要用有限谱，须对(14)、(15)、(18)这些准确来源给出
完整投影及其算术授权；质量零本身不提供该授权。


## 原 E3969 伙伴与全部四伙伴的完整关系及同前缀约束

日期：2026-11-28 UTC。本节只消费 R1038 已付的实际 $\Phi_{126}$，不重算它的谱或坐标。结论是原共同 $A_{24}$ 模型的完整有理关系、准确极除子、全部 Gaussian 相消及同一前缀的三角递推。新增算术条件始终是 $\Phi_{126}$ 本身的完整 canonical 加权行；不把下面的乘积或平方根另外赋予中央零。

保持 $X=x^3$，将以下原多项式全部写出：
$$
\begin{aligned}
A_2&=X^2+20X-8,\\
C_3&=X^3-96X^2+48X+64,\\
E_3&=X^3+228X^2+48X+64,\\
D_{13}&=13X^4+52X^3+1536X^2+1024X+256,\\
S_7&=X^6+564X^5-5808X^4-123136X^3
       -189696X^2-49152X+4096,\\
B_4&=X^4+40X^3+2112X^2+3136X+1792,\\
E_8&=X^8+1232X^7-58688X^6-49408X^5-439040X^4\\
&\qquad-2111488X^3-1949696X^2-851968X-32768.
\end{aligned}
\tag{A1}
$$
$S_7$ 的 $X^3$ 和 $X$ 系数均是原 R1038 的负号；下文换成 $t=-1/X$ 时相应奇次项反号。

### A. 五个实际伙伴

令
$$
A=A_{24}=\frac{\sigma^{24}}7(X+1)(7X^2-4X+16).
$$
R821、R468和R1038的原全式逐项给
$$
S=AH_{10},\quad T=AH_{48},\quad U=AH_{112},\quad
V=AH_{42},\quad \Phi_{126}=AH_{102},
\tag{A2}
$$
其中
$$
\begin{aligned}
H_{10}&=\sigma^{10}x^2(X-8),\\
H_{48}&=\sigma^{48}X(X-8)(X+4)A_2C_3,\\
H_{42}&=\sigma^{42}X(X-8)^2(X+4)E_3,\\
H_{112}&=\frac{\sigma^{112}}{13}x^2A_2B_4D_{13}E_8,\\
H_{102}&=\frac{\sigma^{102}}{13}
 X(X+4)(X-8)^2C_3D_{13}S_7.
\end{aligned}
\tag{A3}
$$
每条都是完整全纯截面，原点质量一。前三条由 R821(2)–(3)转换，第四条正是 R468(2)除去同一个 $A$，最后一条来自 R1038 的 live 126 乘积。未重新选择任何角因子。

完整相除得到
$$
\boxed{H_{102}^2H_{10}^3=\mathscr R(X)H_{48}^4H_{42},}
\tag{A4}
$$
$$
\mathscr R(X)=
\frac{(X-8)D_{13}^2S_7^2}
 {169\,X(X+4)^3A_2^4C_3^2E_3},
$$
以及
$$
\boxed{H_{102}H_{10}=\mathscr Q(X)H_{112},\qquad
\mathscr Q(X)=
\frac{X(X+4)(X-8)^3C_3S_7}{A_2B_4E_8}.}
\tag{A5}
$$
(A5)中整个 $D_{13}$ 因子准确消去；未留下一个虚假的十三挠分母。两边 theta degrees 分别为234和112。因此返回原五条来源时有准确的完整恒等式
$$
\boxed{
\Phi_{126}^2 S^3=\mathscr R\,T^4V,\qquad
\Phi_{126}S=\mathscr Q\,A\,U .
}
\tag{A6}
$$
前式总 charge354、首阶30；后式总 charge160、首阶12。

### B. 全部极和原点规范

所有显示比值都是 $X$ 的原有理函数。若对固定多项式 $P$ 记 $(P)_0$ 为其在 $E_0$ 上按真实重数取的全部零除子，则
$$
\begin{aligned}
\operatorname{div}\mathscr R
={}&(X-8)_0+2(D_{13})_0+2(S_7)_0\\
&-(X)_0-3(X+4)_0-4(A_2)_0-2(C_3)_0-(E_3)_0,\\
\operatorname{div}\mathscr Q
={}&(X)_0+(X+4)_0+3(X-8)_0+(C_3)_0+(S_7)_0\\
&-(A_2)_0-(B_4)_0-(E_8)_0.
\end{aligned}
\tag{A7}
$$
共同点按有符号除子消去；(A7)不要求先猜这些因子的所有根互异或互素。每个可能的有限极都完整列出，不能仅按原点质量一将它们忽略。分子分母在 $X$ 中的次数分别是21/21、14/14，所以在 $O$ 都无零极，且
$$
\mathscr R(O)=\mathscr Q(O)=1.
\tag{A8}
$$

换成原 $t=-1/X$，令 $d=1+8t$、$e=1-4t$，并用小写字母表示(A1)各首一尺度倒序多项式，例如
$$
a_2=1-20t-8t^2,\quad c_3=1+96t+48t^2-64t^3,\quad
e_3=1-228t+48t^2-64t^3,
$$
$$
d_{13}=13-52t+1536t^2-1024t^3+256t^4,\quad
s_7=1-564t-5808t^2+123136t^3-189696t^4
       +49152t^5+4096t^6 .
$$
则
$$
\mathscr R(t)=\frac{d\,d_{13}^2s_7^2}
 {169\,e^3a_2^4c_3^2e_3}.
\tag{A9}
$$
原四伙伴的 $\Theta$ 坐标为
$$
H_{10}=\Theta^5d,\quad
H_{48}=\Theta^{24}de\,a_2c_3,\quad
H_{42}=\Theta^{21}d^2e\,e_3,
$$
$$
H_{112}=\Theta^{56}H_{18}/13,\qquad
H_{102}=\Theta^{51}d^2e\,c_3d_{13}s_7/13,
\tag{A10}
$$
其中 $H_{18}$ 是 R473(2)的完整因式。故还可直接写
$$
\mathscr Q(t)=\frac{d^3e\,c_3d_{13}s_7}{H_{18}}.
\tag{A11}
$$
R473的整多项式保持全部符号；(A5)与(A11)完全相同。

对数微分在 $t=0$ 逐因子给
$$
\mathscr R'(0)=-1000,\qquad \mathscr Q'(0)=844.
\tag{A12}
$$
例如 $\log\mathscr R$ 的分子导数为 $8-8-1128=-1128$，分母导数为 $-12-80+192-228=-128$，差为 $-1000$。$H_{102}/\Theta^{51}$ 的导数是 $-460$，$H_{112}/\Theta^{56}$ 的导数是 $-1296$，所以 $\mathscr Q'= -460+8+1296=844$。这些是原点相容核，不将新的单位比值单独作为非零输入：旧 $T^{16}S^3/V^{19}$ 已有导数 $5408$，故“存在一个 uniformizer”本身不是新门。

### C. 完整 Gaussian 与唯一前缀依赖

令 $w=z^6$、$p=6s-1$，使用同一个原 $c_\sigma=[z^{p+1}]\log(\sigma/z)$。对 $\nu=S,T,U,V,E$，其中 $E=\Phi_{126}$，置
$$
m_\nu=(34,72,136,66,126),\qquad
B_\nu(w)=w^{-1}\nu(w)\exp(-m_\nu c_\sigma w^s).
\tag{A13}
$$
这些正是每个原来源按同一 Gaussian regularization 后的质量一单位。若共同模型采用 R821 的整 $\Delta$ 重标，同步按 $m_\nu/34$ 乘回该重标；下式因真实 charge 平衡仍逐字成立。

(A6)中的 Gaussian 和 $w^5$ 全部抵消，所以
$$
\boxed{
B_E^2=\mathscr R(t(w))\,\frac{B_T^4B_V}{B_S^3}.
}
\tag{A14}
$$
这不是独立给 $E$ 选择一个高轴。右边常数为一，故(A14)先在原特征零 formal 序列中有唯一常数一的平方根。这不是全部 ordinary 系数都在 $\mathcal O[[w]]$ 的断言。整性和精度只能在 R1051 已付的真实加权物理/PD 前缀中逐(A16)消费；不能扩大原来的有效范围。若右边为 $1+\sum_{n\ge1}c_nw^n$，则其实际系数 $e_n=[w^n]B_E$ 严格递推为
$$
e_0=1,\qquad
2e_n=c_n-\sum_{i=1}^{n-1}e_ie_{n-i}.
\tag{A15}
$$
原 $\Theta,t,B_S,B_T,B_V$ 的全部系数和所有有限极仍在 $c_n$ 中；不能把它换成只含四个高轴的自由环境解。

该递推也保 R1051 的真实物理行格。对 $n=r+sq$，$0\le r<s$，用
$\mathcal Y_{r,q}(F)=p^q q![w^{r+sq}]F$。
若 $r_1+r_2=r+s\varepsilon$、$\varepsilon=0$或1，
则乘法的准确系数是
$$
\mathcal Y_{r,q}(FG)
=\sum
p^\varepsilon\frac{q!}{q_1!q_2!}
\,\mathcal Y_{r_1,q_1}(F)\mathcal Y_{r_2,q_2}(G),
\quad q=q_1+q_2+\varepsilon .
\tag{A16}
$$
所有系数均整；多个因子的全部 carry 由重复(A16)保留。单位逆和常数一平方根的三角递推同样只除以整单位。这里是在同一个真实 source 及同一全部前缀中运算，不换原 $M$ 的像或饱和修正 $R$。

(A5)则同时给
$$
B_EB_S=\mathscr Q(t(w))\,B_AB_U,
\quad
B_A=w^{-1}A(w)e^{-24c_\sigma w^s}.
\tag{A17}
$$
这保原共同 $A_{24}$ 的实际系数；(A14)与(A17)中的同一个 $B_E$ 不可在两个方程中独立选根。

### D. 新坏条件的精确位置

R1038 §12.2 的(62)、(66)、(67)固定完整 Newton 定义及首导数，§13的(70)固定这里未乘91的实际 $\Phi_{126}$。因此 $E_{3969}$ 坏条件在(A13)的同一尺度上准确是
$$
\boxed{
0=J_E'(0)=
\sum_{h\ge1}(-1)^{h-1}(h-1)!
(126c_\sigma)^{-h}
[w^{sh}]\!
\left(
w\sqrt{\mathscr R(t(w))\,B_T^4B_V/B_S^3}
\right).
}
\tag{A18}
$$
平方根按(A15)的原常数一方向。这里 $wB_E=\Phi_{126}e^{-126c_\sigma z^{p+1}}$、$[w^{sh}]=[z^{(p+1)h}]$，所以(A18)正是原 $a_h$ 乘 $(-1)^{h-1}(h-1)!$ 的全部和；没有遗漏质量修正，因为原 $J_{126}(0)=0$，R1038(67)求导的外权项因而为零。完整尾按 R1038/R301 原界保留。每个允许有限精度都先保原 factorial、全部 $h$ 权和既定尾界，不能把(A18)改成逐 $e_n$ 零，也不能把它看作 $J_T'^4J_V'/J_S'^3$。

所以本节确将这条已付 canonical 来源接回同一个原 $S/T/V/t$ 的全前缀，并与第四伙伴 $H_{112}$ 的真实关系相容。它不扩大 R473 的函数域或已付正规化角空间，也不单独改善 R1051 的 $3M_D\log D$ 主预算。需要继续证明的是(A18)与原另外四条完整加权行在**同一个实际前缀及同一个饱和修正**下是否产生新的不可消约束，而不是再次把 $B_E$ 当自由第五列。
