# R929 — 原超几何系数的全 p² 下一位、真实对数列与 Gaussian 前缀

日期：2026-11-20。**状态：下述精确三带抽因子、模 p³ 的单位积展开、整个 n<p² 对数输入及原 Gaussian 前缀的两位恢复均已证明。没有证明四个原中央联合非零，亦没有把实际除 p 商设为零。**

本篇固定 R828 的同一个
\[
r_n=\frac{(1/3)_n}{(5/6)_n},\qquad
\log\Theta^{17}=\sum_{n\ge1}\frac{17r_n}{3n}t^n .
\]
新增内容是这些原系数在整个两位指标矩形上的下一位与再下一位；
不是重新登记 R525 的齐次低轴，亦不是给高轴另选提升。
所有单位积、谐和和及除 p 都来自显示的特征零有限式。
最后将所得数据送回同一个原 Gaussian，读取 R708/R923 所需的完整前缀和第一实际进位。
本篇没有数学数值执行、素数扫描或新的自由算术参数。

## 1. 原规范与精确三个区间

固定
\[
p=6s-1>211,\qquad q=p^2,\qquad
0\le m,a<p,\qquad n=mp+a .
\tag{1}
\]
本篇先在 R828 的共同 \(b=1\) 模型上使用
\[
t=-u^6=-x^{-3},\qquad w=z^6,\qquad \Theta=x\sigma^2 .
\]
回到物理 \(b=17\) 及第四来源时，R821/R923 已付的原单位缩放、
Schwartz、周期和 \(-17/11\) 因子继续保留；
这里不把共同坐标中的计算当成换了一条曲线或新的中央函数。

对 \(x=1/3,5/6\) 定义实际有限单位积
\[
U_x(N)=
\prod_{\substack{0\le j<N\\p\nmid x+j}}(x+j),\qquad
U(N)=U_{1/3}(N)/U_{5/6}(N).
\tag{2}
\]
条件 \(p\mid x+j\) 按 \(\mathbf Z_p\) 的赋值解释。
一个被排除的因子整体留在下述 Pochhammer 比中；
若它还含第二个 p，不在此处把该第二个 p 删去。

原分子中被 p 整除的指标是
\[
j=4s-1+bp,\qquad j+1/3=p(b+2/3);
\]
原分母中相应指标是
\[
j=s-1+bp,\qquad j+5/6=p(b+1/6).
\tag{3}
\]
于是直接抽出这些因子，在特征零准确得到
\[
r_{mp+a}=
\begin{cases}
\displaystyle
\frac{(2/3)_m}{(1/6)_m}\,U(mp+a),&0\le a<s,\\[2mm]
\displaystyle
p^{-1}\frac{(2/3)_m}{(1/6)_{m+1}}\,U(mp+a),
&s\le a<4s,\\[2mm]
\displaystyle
\frac{(2/3)_{m+1}}{(1/6)_{m+1}}\,U(mp+a),
&4s\le a<p.
\end{cases}
\tag{4}
\]

置
\[
B_m=\frac{(2/3)_m}{(7/6)_m},\qquad
\lambda_a=
\begin{cases}
6,&a<s,\\
0,&s\le a<4s,\\
3/2,&a\ge4s .
\end{cases}
\tag{5}
\]
由 \((x)_{m+1}=x(x+1)_m\)，三带的相对式统一为
\[
\boxed{\quad
r_{mp+a}
=r_a(1+\lambda_a m)B_m\,\frac{U(mp+a)}{U(a)} .
\quad}
\tag{6}
\]
这里两个外带分别使用准确恒等
\[
\frac{(2/3)_m}{(1/6)_m}=(6m+1)B_m,\qquad
\frac{(5/3)_m}{(7/6)_m}=\frac{3m+2}{2}B_m .
\tag{7}
\]
式(6)不只是一条模 p 的 Lucas 式。

### 1.1 全部额外 p 的真实相消

对 \(0\le m<p\)，三个比的赋值由其唯一可能的分子、分母 p 因子直接给出：
\[
\begin{array}{c|c}
\text{比}&\text{赋值为一的 m；其余赋值为零}\\ \hline
(2/3)_m/(1/6)_m&2s\le m\le5s-1\\
B_m=(2/3)_m/(7/6)_m&2s\le m\le5s-2\\
(5/3)_m/(7/6)_m&2s-1\le m\le5s-2 .
\end{array}
\tag{8}
\]
例如 \(B_m\) 的分子 p 因子在 \(j=2s-1\)，进入乘积的条件是
\(m\ge2s\)；分母 p 因子在 \(j=5s-2\)，进入条件是
\(m\ge5s-1\)。它们分别为 \(p/3\) 和 \(5p/6\)，比为真实单位 \(2/5\)。
对第一行，分母指标是 \(j=5s-1\)，进入条件为 \(m\ge5s\)。
对第三行，分子指标改为 \(j=2s-2\)，进入条件为 \(m\ge2s-1\)。
在所示范围内不会出现 p² 因子。

特别，在(4)中 \(m=5s-1\) 的 \(m+1/6=5p/6\)
不能作单位约去；其 p 正由此前分子中的 p 相消。
式(8)已经保留了这个异常列。
因而全部 \(B_m\) 及(7)中的两个外带比均整，而且
\[
v_p(r_a)=
\begin{cases}
-1,&s\le a<4s,\\
0,&a<s\text{ 或 }a\ge4s.
\end{cases}
\quad
v_p(r_{mp+a})\ge-1 .
\tag{9}
\]
这些估值先于后文所有约化。

## 2. 同一单位积的模 p³ 展开

定义实际有限数
\[
G_p=U(p),\qquad g_p=\frac{G_p-1}{p},
\]
\[
H_a^U=
\sum_{\substack{0\le j<a\\p\nmid 1/3+j}}\frac1{1/3+j}
-
\sum_{\substack{0\le j<a\\p\nmid 5/6+j}}\frac1{5/6+j},
\]
\[
K_a^U=
\sum_{\substack{0\le j<a\\p\nmid 1/3+j}}\frac1{(1/3+j)^2}
-
\sum_{\substack{0\le j<a\\p\nmid 5/6+j}}\frac1{(5/6+j)^2},
\qquad L_p^U=\frac{H_p^U}{p}.
\tag{10}
\]
上标 U 区别这些和与 R828 的原高轴 \(H_p\)；
二者不混用。每个完整块的非零剩余类各遍历
\(\mathbf F_p^\times\)，故
\[
G_p\equiv1\pmod p,\qquad
H_p^U\equiv K_p^U\equiv0\pmod p .
\tag{11}
\]
因此 \(g_p,L_p^U\in\mathbf Z_p\)。
第二个同余只用 \(p>3\) 时非零剩余类的逆平方和为零。
由(4)取 \(n=p\)，另有全精度归一式
\[
\boxed{G_p=r_p/4,\qquad g_p=(r_p/4-1)/p.}
\tag{12}
\]
所以 \(g_p\) 是同一个原系数的真商。

对第 b 个完整块，把每个单位因子写成
\((x+j)(1+bp/(x+j))\)。有限乘积的二阶展开和(11)给
\[
\frac{U(bp+p)}{U(bp)}
\equiv G_p(1+b p^2 L_p^U)\pmod{p^3}.
\tag{13}
\]
确切地，一阶和为 \(bpH_p^U=bp^2L_p^U\)；
二阶对数项为 \(-b^2p^2K_p^U/2\)，已属于 \(p^3\mathbf Z_p\)。
一阶和的平方更高。没有把这些块预先当成同一个特征零乘积。

最后一个长度 a 的块则满足
\[
\frac{\text{第 m 块的长度 a 单位积}}{U(a)}
\equiv
1+mpH_a^U+
\frac{m^2p^2}{2}\big((H_a^U)^2-K_a^U\big)
\pmod{p^3}.
\tag{14}
\]
乘完(13)的 \(b=0,\ldots,m-1\) 以及(14)，得到
\[
\boxed{
\begin{aligned}
\frac{U(mp+a)}{U(a)}
\equiv{}&1+mp(g_p+H_a^U)\\
&+p^2\left[
\binom m2(g_p^2+L_p^U)
+m^2\left(g_pH_a^U+
\frac{(H_a^U)^2-K_a^U}{2}\right)\right]
\pmod{p^3}.
\end{aligned}}
\tag{15}
\]
这在全部 \(0\le m,a<p\) 同时成立，包括(8)的异常列。
它是单位比的相对同余，故不会因原 \(r_{mp+a}\) 含 p 分母而被误用。
特别，结合(6)、(9)，可合法乘成
\[
p r_{mp+a}
\equiv p r_a(1+\lambda_a m)B_m
\{\text{(15)右端}\}\pmod{p^3}.
\tag{16}
\]
两个外带还可不乘 p，直接读取 \(r_{mp+a}\bmod p^3\)，
因为这些带中的实际乘子全部整。

读取(15)所需的是指定 \(g_p,H_a^U\bmod p^2\)
及 \(L_p^U,K_a^U\bmod p\)，连同原 \(p r_a,B_m\) 的相应位数。
原 p 因子按(3)、(8)先作精确相消，不能先把一个含 p 的分母当成剩余域单位。

## 3. 全 p² 矩形压为三个真实块

令
\[
c_a=pr_a,\qquad \tau_a=g_p+H_a^U,\qquad
A_a^U=\frac{\tau_a^2+L_p^U-K_a^U}{2},\qquad
B_p^U=\frac{g_p^2+L_p^U}{2}.
\tag{17}
\]
式(15)即
\[
U(mp+a)/U(a)\equiv
1+mp\tau_a+p^2(m^2A_a^U-mB_p^U)\pmod{p^3}.
\]
定义次数小于 p 的三个实际多项式
\[
P_0(t)=\sum_{a=0}^{p-1}c_at^a,
\]
\[
P_1(t)=
\sum_{a=0}^{p-1}c_a(\lambda_a+p\tau_a-p^2B_p^U)t^a,
\]
\[
P_2(t)=
\sum_{a=0}^{p-1}c_a(p\lambda_a\tau_a+p^2A_a^U)t^a,
\qquad
B(X)=\sum_{m=0}^{p-1}B_mX^m .
\tag{18}
\]
所有系数整，并且
\[
P_1\in p\mathbf Z_p[t],\qquad P_2\in p^2\mathbf Z_p[t].
\tag{19}
\]
中带有 \(\lambda_a=0\)；两个外带则有 \(c_a\in p\mathbf Z_p\)，
这正是(19)的原因。

记 \(\vartheta=X\,d/dX\)，最后才代入 \(X=t^p\)。
由(16)逐项展开得
\[
\boxed{\quad
pR(t)\equiv
P_0(t)B(t^p)+P_1(t)(\vartheta B)(t^p)
+P_2(t)(\vartheta^2B)(t^p)
\pmod{p^3,t^{p^2}},\qquad R(t)=\sum_{n\ge0}r_nt^n .
\quad}
\tag{20}
\]
这里 \((\vartheta B)(t^p)\) 不是先对 \(B(t^p)\) 作 t 导数。

为支付全部被省去的项，乘
\((1+\lambda_am)\{1+mp\tau_a+p^2(m^2A_a^U-mB_p^U)\}\)
时，除了(18)以外仅剩
\[
c_a\lambda_ap^2(m^3A_a^U-m^2B_p^U)B_m .
\]
在中带 \(\lambda_a=0\)，在外带 \(c_a\in p\mathbf Z_p\)，
所以它们全部属于 \(p^3\mathbf Z_p\)。
这是三个块而非四个或更多块的准确原因。
模 p² 时 \(P_2\) 消失，留下两个真实块。

### 3.1 与旧首位的区别

式(20)的首位确给
\[
pR(t)\equiv
C_p^{R}\,t^s(1-t)^{3s-1}B(t^p)
\pmod{p,t^{p^2}},
\tag{21}
\]
其中
\[
C_p^{R}=\overline{p r_s}
=-\overline{4^{-s}\binom{2s}{s}}\ne0.
\]
这是原 \(pR\) 方程的齐次解；其 support
\([s,4s-1]\) 和低轴形状已经与 R525/R915 附B相容。
本篇不将这个首位单独当成新增结论。
式(8)另明确给 \(B\bmod p\) 的准确 support
\([0,2s-1]\cup[5s-1,p-1]\)。
新增的输入是(15)、(18)、(20)保留的真实下一位和再下一位。

## 4. 原 log Θ 的 p 倍指标不能少读一位

令
\[
\mathcal L_\Theta(t)=\log\Theta^{17}
=\frac{17}{3}\sum_{n\ge1}\frac{r_n}{n}t^n.
\tag{22}
\]
对 \(n<p^2\)，(9)及(8)保证
\(p\mathcal L_\Theta(t)\bmod t^{p^2}\) 整。
当 \(a\ne0\)，可将(20)的系数再乘
\[
(a+mp)^{-1}
\equiv a^{-1}-mpa^{-2}+m^2p^2a^{-3}\pmod{p^3}.
\]
写 \(P_{i,a}=[t^a]P_i\)，定义不含常数项的
\[
Q_0(t)=\sum_{a=1}^{p-1}\frac{P_{0,a}}a\,t^a,
\]
\[
Q_1(t)=\sum_{a=1}^{p-1}
\left(\frac{P_{1,a}}a-\frac{pP_{0,a}}{a^2}\right)t^a,
\]
\[
Q_2(t)=\sum_{a=1}^{p-1}
\left(\frac{P_{2,a}}a-\frac{pP_{1,a}}{a^2}
+\frac{p^2P_{0,a}}{a^3}\right)t^a .
\tag{23}
\]
仍有 \(Q_1\in p\mathbf Z_p[t]\)、\(Q_2\in p^2\mathbf Z_p[t]\)。
因为(19)，乘逆分母所产生的其它交叉项均属于 p³。

但 \(a=0,m\ge1\) 时，正确式是
\[
p[t^{mp}]\mathcal L_\Theta
=\frac{17}{3m}r_{mp},
\tag{24}
\]
不能仅将 \(p r_{mp}\bmod p^3\) 再除以 p。
使用(6)的整低带及 \(H_0^U=K_0^U=0\)，准确得到
\[
r_{mp}\equiv
(6m+1)B_m
\left\{1+mpg_p+p^2\binom m2(g_p^2+L_p^U)\right\}
\pmod{p^3}.
\tag{25}
\]
这保住了(24)所需的额外一位；\(1\le m<p\) 的 m 本身是单位。

定义实际多项式
\[
\mathcal I B(X)=\sum_{m=1}^{p-1}\frac{B_m}{m}X^m,
\]
\[
\begin{aligned}
D_0(X)={}&\mathcal I B+6(B-1)\\
&+pg_p\{(B-1)+6\vartheta B\}\\
&+\frac{p^2}{2}(g_p^2+L_p^U)
\{6\vartheta^2B-5\vartheta B-(B-1)\}.
\end{aligned}
\tag{26}
\]
式(24)–(25)和
\((6m+1)(m-1)=6m^2-5m-1\)
给出完整原对数式
\[
\boxed{
p\mathcal L_\Theta(t)\equiv\frac{17}{3}
\left\{
Q_0(t)B(t^p)+Q_1(t)(\vartheta B)(t^p)
+Q_2(t)(\vartheta^2B)(t^p)+D_0(t^p)
\right\}
\pmod{p^3,t^{p^2}}.
}
\tag{27}
\]
常数项均为零。\(D_0\) 是同一原 p 倍指标列的明确值，
不是由模 p 微分方程任选的 Frobenius 常数。
特别它完整保留原 \(g_p=(r_p/4-1)/p\) 的贡献。

## 5. 原 Gaussian 所需坐标、常数及整窗

现在只取
\[
L=\frac{p^2-1}{6},\qquad 0\le M\le L-1 .
\tag{28}
\]
原形式对数在负角坐标中准确为
\[
z=uF(t),\qquad
F(t)=\sum_{n\ge0}
\frac{(1/2)_n}{n!(6n+1)}t^n,\qquad
w(t)=-tF(t)^6.
\tag{29}
\]
这里每个 \(F_n\) 在 \(n<L\) 整。
一个直接核定是：\(6n+1<p^2\)，若它被 p 整除，
则 \(n\equiv5s-1\pmod p\)；这个最低 digit 大于 \(p/2\)，
使 \(\binom{2n}{n}\) 至少含一次 p，恰足消去分母可能的一次 p。
否则分母本为单位。此处不使用 \(n=L\) 的坏端点。
所以 \(w(t)\) 有整系数和首项 \(-t\)，其实际反函数 \(t=t(w)\)
到所需阶也是整的，且与原 \(t=-x(z)^{-3}\) 相同。

保留 R821 的指定
\[
\kappa=34c+\Delta,\qquad
c=[w^s]\log(\sigma/z),\quad
\Delta\in\mathcal O,\quad a_\kappa=p\kappa\in\mathcal O^\times .
\tag{30}
\]
若采用 Hasse 对齐，(30)就是 R861 的同一个实际 \(\kappa\)；
不能从它的首剩余类另取一个提升。
对 R708/R923 的原首 Gaussian，直接取 \(\Delta=0\)。

常数 \(a_\kappa\bmod p^3\) 也可在本篇输入中准确读取，不必当成自由量。
因为
\[
z^2x=F(t)^2,\qquad
\mathcal L_\Theta(t)
=17\log(z^2x)+34\log(\sigma/z),
\]
有
\[
\boxed{\quad
a_\kappa=
[w^s]\left\{
p\mathcal L_\Theta(t(w))-34p\log F(t(w))
\right\}+p\Delta .
\quad}
\tag{31}
\]
所读 \(F\) 的对数只需次数 s，且 \(s<p\)，没有新的阶乘或积分 p 分母。
式(27)、原 \(F\) 的模 p³ 输入及同一 \(\Delta\) 遂给原 \(a_\kappa\bmod p^3\)。

定义完整原单位
\[
g(t)=(1+8t)\Theta(t)^{17}
\exp\{-\kappa w(t)^s\},\qquad
\Lambda(t)=\log g(t).
\tag{32}
\]
它在整个(28)窗口的整性不能仅由对数差来假定。
R614(2)、(3)、(9)直接证明
\[
W(w)=z^2x\in\mathcal O[[w]]/(w^{L}),\qquad
U(z)=\frac{\sigma(z)}z
\exp\{-(c+\Delta/34)z^{p+1}\}
\in\mathcal O[[w]]/(w^{L}).
\]
于是同一个实际
\[
g(t(w))=(1+8t(w))\,W(w)^{17}U(z)^{34}
\tag{33}
\]
是到 \(w^M\) 的整单位。用(29)的整坐标返回后，
\(g(t)\bmod t^{M+1}\) 同样是整单位。
这里直接使用 sigma 单位 U 和 W，不从来源 S 除以 t，
因此不会损失顶端一阶。
R614 的证明对原 p 单位 b 的所有系数逐项相同；
从其正文 \(b=17\) 返回本节共同 \(b=1\) 正是已付的单位缩放。

由(22)、(29)–(32)，准确有
\[
\boxed{\quad
p\Lambda(t)=p\log(1+8t)+p\mathcal L_\Theta(t)
-a_\kappa(-1)^s t^s F(t)^{p+1}.
\quad}
\tag{34}
\]
右边到 \(t^M\) 全整：
第一项仅在 \(n=mp\) 时约去一次 p，m 仍是单位；
第二项由(27)支付；
最后一项只用已证明整的 F。
保原 \(F\bmod p^3\)、\(a_\kappa\bmod p^3\) 即可读出最后一项模 p³，
其整数幂 \(p+1\) 不造成精度损失。

这给出整个 \(p\Lambda\bmod(p^3,t^{M+1})\) 的真实有限公式。
并没有把旧 R912 的 \(2p^2-p-9\) 窗或旧 p⁵ 除点输入免费延长；
本篇的坐标范围始终是(28)。

## 6. 从真实对数输入恢复原 g 的两位

以下稳定性须连同(33)的整性使用。
若 \(\widetilde\Lambda(0)=0\)，且
\[
p\widetilde\Lambda\equiv p\Lambda
\pmod{p^3,t^{M+1}},
\]
则
\[
\widetilde\Lambda-\Lambda\in
p^2t\,\mathcal O[t]/(t^{M+1}).
\]
对 \(p>2\)，\(\exp(p^2t\mathcal O[[t]])\subset
1+p^2t\mathcal O[[t]]\)，由实际恒等
\[
\exp\widetilde\Lambda
=g\,\exp(\widetilde\Lambda-\Lambda)
\]
及 g 的整性，得到
\[
\boxed{\quad
\exp\widetilde\Lambda\equiv g
\pmod{p^2,t^{M+1}}.
\quad}
\tag{35}
\]
如果未先支付 g 的整性，这个精度结论确实不能推出。

一个完全明确的有限读取方式是：在原常数域的固定整基中，为(34)各系数的模 p³ 值取实际整代表，
再除以 p，在相应有理数域或原常数数域中作精确截断指数到 \(t^M\)。
式(35)保证所得系数整且模 p² 为原值。
此处不声称用只存三位的普通 log/exp 算法也不会遭遇中间精度损失；
若采用有限精度实现，须实现这个稳定性门或逐项另付算法精度。
所有数学执行仍只可在公开 Actions 中进行。

同理，只取(27)、(34)模 p²，可恢复同一原 g 模 p。
这使用真实下一位，而非用旧首位齐次解决定一个未定积分常数。

## 7. 返回四个原完整 Gaussian 前缀与第一 carry

沿 R821 保全部固定多项式 \(f_\nu(t)\)，
\[
(q_S,q_T,q_U,q_V)=(1,36/17,4,33/17),
\quad
(m_S,m_T,m_U,m_V)=(34,72,136,66).
\]
四个原实际来源准确为
\[
\widehat\nu(w)=
\left(\frac{g(t(w))}{1+8t(w)}\right)^{q_\nu}f_\nu(t(w)).
\tag{36}
\]
这些有理指数属于 \(\mathbf Z_p\)，对常数一整单位的幂保持模 p² 同余；
原 \(f_\nu\) 与全部角因子均不截成极项。
所以(27)–(35)及实际整反函数 \(t(w)\) 给出
\[
[w^{sh}]\widehat\nu\bmod p^2
\qquad(sh\le M)
\tag{37}
\]
的完整有限读取。

取 \(\Delta=0\)，(37)就是共同模型上的原 \(g_{\nu,h}\)。
为明确返回 R708/R923 的物理规范，齐次身份逐个系数给
\[
g_{\nu,h}^{(b)}=b^{sh-1}g_{\nu,h}^{(1)},\qquad
\gamma_\nu^{(b)}=b^s\gamma_\nu^{(1)},\qquad
j_\nu^{(b)}=b^{-1}j_\nu^{(1)}.
\]
这里 Gaussian 常数和 Taylor 系数同时运输；对 \(b=17\) 为原单位运输，
第四来源再保 R923(3) 的物理 \(-17/11\) 因子。
所以下述同余、完整前缀与中央零均准确返回同一个原对象。
任意 \(J\le p-2\) 满足
\[
sJ\le s(p-2)=L-s\le L-1,
\]
故本篇同时覆盖整个单模 p 判据，尤其所有充分大 p 的
\(J_\alpha(p)=\lceil\alpha(p-1)\rceil-1\)、\(3/4<\alpha<1\)。
目标并未降成固定五块；仍读取实际全部 \(h=1,\ldots,J_\alpha(p)\)。
在这个较短应用窗中只需(27)的 \(m\le s-1\) 部分；
全矩形(8)的后段异常虽不进入这里，已在定理中完整支付。

为明确同中央条件的接口，记
\(\gamma_\nu=m_\nu pc\) 并保原 Newton 部分和
\[
\mathscr L_{\nu,H}
=\sum_{h=1}^H
(-1)^{h-1}(h-1)!\frac{p^h}{\gamma_\nu^h}g_{\nu,h}.
\tag{38}
\]
对后两源，R821(16a)在除去首 w 后将它们准确写成
原 \(U^{136}\)、\(U^{66}\) 乘有限个 \(w^iW^j\) 的整线性组合，
其中 i、j 均非负。因此 R614(18)的三个区间逐项适用：
总指标小于 \(2L\) 时至多出现一个坏因子。
更高的无限尾由 R821(16b)的整个 Hurwitz 界给出与 R614(23)同一估计。
所以四源共同保留 R614/R708 的完整尾结论：若原 \(j_\nu=0\)，则
\(\mathscr L_{\nu,H}\in p^{H+1}\mathcal O\)
于其已付 \(H\le p-2\) 范围。
本篇计算这些同一系数的两位，不把该必要式改成各系数分别为零。
特别在 \(H=2\)，实际有
\[
\frac{j_\nu}{p}
\equiv\frac{g_{\nu,1}}{\gamma_\nu}
-p\frac{g_{\nu,2}}{\gamma_\nu^2}\pmod{p^2}.
\tag{39}
\]
因此在中央为零的假设下，
\[
g_{\nu,1}\in p\mathcal O,\qquad
\boxed{\ 
\overline{g_{\nu,1}/p}
=\overline{g_{\nu,2}/\gamma_\nu}\ }.
\tag{40}
\]
(27)–(37)给(40)左边的真实除 p 商，连同右边，
不会以任意提升代替它。
更高 H 的全部 carry 仍要按(38)保留；
两位输入并不支付任意 H 所需的全部高精度。

R708/R923 的高度结果把原边界零等价为
全部指定前缀 \(g_{\nu,h}\bmod p=0\)。
式(40)也再次显示中央零本身没有把第二块设为零。
本篇尚未证明(38)与原(27)的四来源输入迫该前缀全零，
没有从三个实际块的表示数推出四个指定中央不能同时为零。
完整通常 Selmer 桥、同一无限 p 集及主目标仍为原未完成门。

## 依赖与复核范围

- R828：同一 \(r_n,\mathcal L_\Theta,t,\Theta\)、原高轴及完整 Gaussian 规范。
- R614 §§1–4、R708 §§4–7：直接作用于 U、W 的严格高度二整窗、
  原 Gaussian 前缀及完整 Newton 尾；本篇未跨越其坏端点。
- R821、R861：四固定完整来源、实际 charge、合法整 Gaussian 改变及原全部 carry。
- R915 附B：完整原连接的长窗；本篇(21)的首位与其相容，
  本篇新增的是同一 Pochhammer 系数的下一位及明确 p 倍对数列。
- R923：第四来源完整 Hall 迹及固定分母高度；原物理缩放和全部相位保持。

全文为有限乘积和原形式身份的符号证明。没有数值验证回执，
也没有把前缀读取或第一 carry 的支付标记为主目标非零。

## 附录 A — 同一原单位积的 Fermat 2 闭式

保持正文全部规范。本附录只对正文指定的
\[
G_p=U_{1/3}(p)/U_{5/6}(p)=r_p/4,\qquad
g_p=(G_p-1)/p
\]
给出一个全原始输入的下一位闭式。没有换掉 \(r_p\) 或其提升。
对现有 results、notes 的 \(r_p/4\)、相应单位积及同阶式作文本核对，
未找到下述模 p³ 闭式；R865 的既有谐和式与本附录继续相容。
全文为手证，无数学执行。

记
\[
\alpha=1/3,\quad\beta=5/6,\quad
S_\alpha=
\sum_{\substack{0\le j<p\\p\nmid\alpha+j}}\frac1{\alpha+j},
\quad
K_\alpha=
\sum_{\substack{0\le j<p\\p\nmid\alpha+j}}\frac1{(\alpha+j)^2}.
\tag{A1}
\]
各非零剩余类恰出现一次，因此
\[
S_\alpha,K_\alpha\in p\mathbf Z_p,\qquad
L_\alpha=S_\alpha/p\in\mathbf Z_p.
\tag{A2}
\]
正文的 \(L_p^U=(S_\alpha-S_\beta)/p\) 仍是同一个实际有限和。

### A.1 真实 p 因子保留后的 duplication

特征零的倍分式
\[
(\alpha)_p(\alpha+1/2)_p
=2^{-2p}(2\alpha)_{2p}
\]
在左边分别抽出 \(2p/3\)、\(p/6\)，总积为 \(p^2/9\)；
右边的两个 p 因子则为 \(p/3\)、\(4p/3\)，总积为 \(4p^2/9\)。
所以准确有
\[
\boxed{
U_{1/3}(p)U_{5/6}(p)
=2^{2-2p}U_{2/3}(2p).
}
\tag{A3}
\]
这里的 \(2^{2-2p}\) 包含这两个真实 p 因子比产生的 4，
不能只留下普通 duplication 的 \(2^{-2p}\)。

对右端作 \(j\mapsto2p-1-j\)。因为
\[
(2p-1-j)+2/3=2p-(j+1/3),
\]
且被保留的单位数目为 \(2p-2\)，所有负号相乘为一。
因此右端的单位积恰为 \(\alpha\) 在块号 \(-2,-1\) 的两个完整块：
\[
U_{2/3}(2p)
=
\prod_{\substack{0\le j<p\\p\nmid\alpha+j}}(\alpha+j-2p)
\prod_{\substack{0\le j<p\\p\nmid\alpha+j}}(\alpha+j-p).
\tag{A4}
\]
这仍是特征零的准确式。

对任一整数 b，有限单位积展开及(A2)给
\[
\prod_{\substack{0\le j<p\\p\nmid\alpha+j}}(\alpha+j+bp)
\equiv U_\alpha(p)(1+bpS_\alpha)\pmod{p^3}.
\tag{A5}
\]
二阶项
\(b^2p^2(S_\alpha^2-K_\alpha)/2\) 属于 p³，
故对负块号也没有额外项。
由(A4)–(A5)，
\[
U_{2/3}(2p)
\equiv U_\alpha(p)^2(1-3pS_\alpha)\pmod{p^3}.
\]
代回(A3)并只约实际单位，得到
\[
\boxed{
G_p\equiv
2^{2p-2}(1+3pS_\alpha)
=2^{2p-2}(1+3p^2L_\alpha)
\pmod{p^3}.
}
\tag{A6}
\]

### A.2 同一个全块倒数和与原 Fermat 商

在(A3)对应的偶、奇指标上逐项取倒数，有准确恒等
\[
S_\alpha+S_\beta
=2\sum_{\substack{0\le j<2p\\p\nmid2/3+j}}
\frac1{2/3+j}.
\tag{A7}
\]
反射(A4)给右边的和为负的两个 \(\alpha\) 负块倒数和。
每个负块满足
\[
\sum_{\substack{0\le j<p\\p\nmid\alpha+j}}
\frac1{\alpha+j+bp}
\equiv S_\alpha-bpK_\alpha
\equiv S_\alpha\pmod{p^2}.
\]
于是
\[
S_\beta\equiv-5S_\alpha\pmod{p^2},\qquad
\boxed{L_p^U\equiv6L_\alpha\pmod p.}
\tag{A8}
\]

令原整数 Fermat 商为
\[
Q_p=\frac{2^{p-1}-1}{p}\in\mathbf Z.
\]
由 \(2^{2p-2}=(1+pQ_p)^2\)，(A6)–(A8)给
\[
\boxed{
g_p\equiv
2Q_p+p(Q_p^2+3L_\alpha)
\equiv2Q_p+p\left(Q_p^2+\frac{L_p^U}{2}\right)
\pmod{p^2}.
}
\tag{A9}
\]
特别 \(g_p\equiv2q_p(2)\pmod p\)。
这里模 p² 需要 \(Q_p\bmod p^2\)，不能只把其首剩余类代回。
第二位的 \(L_p^U\) 也没有被设为零。

### A.3 原 p 倍对数列的实际返回

继续正文(26)的 \(B,\vartheta,\mathcal I B\)。
把(A9)代回同一个 \(D_0\)，逐项合并得到
\[
\boxed{
\begin{aligned}
D_0={}&\mathcal I B+6(B-1)
+2pQ_p\{(B-1)+6\vartheta B\}\\
&+p^2\left\{
-Q_p^2(B-1)
+\left(\frac{L_p^U}{2}-4Q_p^2\right)\vartheta B
+(12Q_p^2+3L_p^U)\vartheta^2B
\right\}
\pmod{p^3}.
\end{aligned}}
\tag{A10}
\]
例如 p² 的 \(B-1,\vartheta B,\vartheta^2B\) 系数分别是
\(-Q_p^2,L_p^U/2-4Q_p^2,12Q_p^2+3L_p^U\)。
所以正文最容易因额外除 p 丢失的 Frobenius 常数列，
其新首修正已完全接回原 Fermat 2；
再下一位仍保同一个明确全块倒数商。

所有非 p 倍指标中的 \(g_p\) 也可按(A9)代入正文(17)–(27)，
原三带、实际单位因子和四完整来源均不改变。
这不是给 \(D_0\) 新增一个消失条件，
也不由 \(Q_p\) 或 \(L_p^U\) 的显示形式推出四中央非零。
