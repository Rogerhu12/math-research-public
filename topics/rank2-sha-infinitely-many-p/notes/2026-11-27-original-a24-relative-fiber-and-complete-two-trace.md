# 原 A24 相对来源的完整二挠迹与混合除 p 返回

日期：2026-11-27 UTC。**状态：下述固定来源、完整同源迹和两条混合除 $p$ 身份已证明。** 本注不新增 canonical 中央零。它消费 [共同 A24 的完整水平加法](2026-11-16-common-a24-horizontal-product-and-relative-theta-gluing.md) 的同一个 $T$ 行相对片，而非另选 degree144 截面。原四个收缩 $S,T,U,V$、完整 Gaussian、固定 CM 系数及全 theta 结构保持。

全文为原 sigma 恒等式、完整函数域迹和 Hurwitz 整格的纸面证明，没有数学执行或素数扫描。原 $S/T/U/V$ 的其它双投影及参考配对仍使用 [R884](../results/R884-original-t72-norm-three-heat-and-c24-h22-pairing.md)，本注不重证那些结论。

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
