# R377：完整 YY 第零角商的局部四次式、真实面积差与准确未付条件

日期：2026-11-15。**有限纸面恒等式；未运行新的求积、符号程序、参数扫描、人工测试或研究计算。**

当前偶弱圆已在同一个有限频率根上支付
[R375](R375-exact-Y-second-cubic-and-thirteen-target-control-pay-ZY2-and-YY2.md)
的完整 \(ZY_2,YY_2\) 等条件，但 \(YY_0\) 仍未支付。
本稿从原 cubic 和真实同锚输出完整算出它的额外角商：
所有 primitive 在准确 IBP 后收成一个无除 \(x\) 的局部 C² 四次多项式。
该式既不是仅 principal，也不是宣称已有圆已使它为零。

主要身份是，对真正合法的整个复输入 \(q=f+ig\)，
\[
\boxed{
K_{YY,0}(q)=\mathcal K_Y(q)
=\frac{S_{UY,2}(q)-S_{LY,2}(q)}3.}
\tag{1}
\]
这里右侧 \(L,U,Y\) 为原算子，不是任意独立控制方向。
\(\mathcal K_Y\) 的完整局部式见(13)(14)。
实输入上的该局部扩展严格为正，但实非零输入并不满足本处复三矩合法条件；不能把这种正性直接搬成真实圆的阻断。

本稿准确完成的是识别 \(YY_0\) 的完整 C² 角商及其与原面积的关系。
实际消去 \(\operatorname{Re}\mathcal K_Y(f+ig)\)、再同点支付剩余 \(\pi/2\) 值，仍是后续义务。

来源：
[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 的全部原算子、三矩、cubic 与完整变分；
[R291](R291-exact-positive-Gaussian-square-moment-is-the-leading-energy.md)、
[R294](R294-corrected-self-fibers-pay-all-angular-symmetric-Gaussian-histories.md)、
[R368](R368-two-exact-cubic-identities-and-seven-target-control-pay-the-PY-product.md)、
[R372](R372-complete-ZZ-zero-angular-quotient-and-nine-target-finite-frequency-control.md)、
[R373](R373-complete-W-square-angular-quotients-and-eleven-target-control.md)、
[R375](R375-exact-Y-second-cubic-and-thirteen-target-control-pay-ZY2-and-YY2.md)。
反演只在第6节作为代数独立核对，不作为新的几何控制权限。

## 1. 整个合法复输入与真实紧方向

沿用
\[
P=\Phi_{r_0},\quad L=\Phi_{p_0},\quad
U=\Phi_{s_1},\quad Y=\Phi_{p_2},\quad Z=dL+eU.
\]
同一个右锚 \(r_*\) 给
\[
J(F)(x)=\int_x^{r_*}F(y)\,dy,\qquad (JF)'=-F.
\]
取当前真实三矩圆 \(f,g\)，令 \(q=f+ig\)。
所有积分为复双线性延拓，**不取复共轭**。
原三个实圆条件准确给
\[
I_j(q,q)=0,\qquad j=0,1,2.
\tag{2}
\]
记
\[
u=q,\quad v=u',\quad r=u'',\quad t=u''',
\qquad C=J(x^2r^2+2v^2).
\]
在(2)下，\(Y(q,q)\) 左二次尾 \(-x^2I_2(q,q)/4\) 真零；
右 collar 也真零。所以 \(w=Y(q,q)\) 是合法的紧变分方向。

定义
\[
K_{YY,0}(q)=I_0(Yq^2,Yq^2)
+2I_0\{q,Y(q,Yq^2)\},
\]
\[
S_{XY,j}(q)=2I_j\{q,[X,Y](q;q^2)\}.
\tag{3}
\]
后者是 diagonal \(2I\) 规范；原 full-circle 面积仍为 \(I\) 规范。
不能把一般单包 \(Y(u,u)\) 的非零左尾套进紧变分。

## 2. 三个完整 cubic 与面积差身份

R259 的原第零 cubic 是
\[
F_{Y,0}(u)
=\int\left(xur^2-\frac32x^2vr^2+\frac13x^3r^3-\frac13v^3\right).
\tag{4}
\]
这是对任意紧输入成立的完整式。
与原 \(I_2=\int(x^2u''w''+2u'w')\) 同时保留的两个 cubic 是
\[
F_{L,2}(u)
=-\int xur^2+\frac12\int x^2vr^2-\frac13\int v^3,
\]
\[
F_{U,2}(u)
=2\int xur^2-4\int x^2vr^2+\int x^3r^3-\frac43\int v^3.
\tag{5}
\]
给出直接核对所需原导数：
\[
L'=ur-xvr-\frac{x}{2}J(r^2),\quad
L''=(u-xv)t-\frac{x}{2}r^2-\frac12J(r^2),
\]
\[
U'=2xvr-\frac32x^2r^2+J(xr^2),\quad
U''=(2xv-3x^2r)t+2vr-2xr^2.
\]
\(L\) 的两份 primitive 在完整 \(I_2\) 中合成
\[
-\frac12\int\{x^2r+2xv\}J(r^2)
=-\frac12\int x^2vr^2.
\]
\(U\) 使用 \(\int vJ(xr^2)=\int xur^2\)。
其余含 \(t\) 项仅对紧 \(r^2,r^3\) IBP，得到(5)；
没有删除真实左常数或省略 \(I_2\) 的一阶导项。

由(4)(5)立刻有完整 cubic 身份
\[
\boxed{3F_{Y,0}=F_{U,2}-F_{L,2}.}
\tag{6}
\]
在真正紧的方向 \(Y(q,q)\) 上变分。
R291/R368 的 \(F_{Y,2}\equiv0\)，以及 R259 的完整 diagonal 变分给
\[
S_{XY,2}(q)=DF_{X,2}(q)[Y(q,q)]
\quad (X=L,U).
\]
这里原两个 quadratic cross 配对因同一个合法 diagonal 才准确抵消。
于是
\[
K_{YY,0}(q)=DF_{Y,0}(q)[Y(q,q)]
=\frac{S_{UY,2}(q)-S_{LY,2}(q)}3,
\tag{7}
\]
证明(1)的面积差部分。
这一推导不将完整 outer/inner 不同的圆面积错误当作 diagonal。

## 3. 从原 Y 输出完整求局部四次式

原真实输出及两导为
\[
w=-xu^2+x^2uv-\frac{x^3v^2}{2}-\frac{x^2C}{4},
\]
\[
w'=-u^2+x^2ur-x^3vr+\frac{x^4r^2}{4}-\frac{xC}{2},
\]
\[
w''=\alpha t+\beta,
\quad
\alpha=x^2u-x^3v+\frac{x^4r}{2},
\]
\[
\beta=-2uv+2xur-2x^2vr+\frac{x^3r^2}{2}+xv^2-\frac C2.
\tag{8}
\]
因此对(4)的合法紧变分准确是
\[
DF_{Y,0}[w]
=\int\left[
xr^2w+\left(-\frac32x^2r^2-v^2\right)w'
+(2xur-3x^2vr+x^3r^2)w''
\right].
\tag{9}
\]

全部含 \(t\) 的项为
\[
2x^3u^2rt-5x^4uvrt+2x^5ur^2t
+3x^5v^2rt-\frac52x^6vr^2t+\frac12x^7r^3t.
\tag{10}
\]
逐项使用
\[
\begin{aligned}
\int x^3u^2rt&=-\frac32\int x^2u^2r^2-\int x^3uvr^2,\\
\int x^4uvrt&=-2\int x^3uvr^2-\frac12\int x^4v^2r^2-\frac12\int x^4ur^3,\\
\int x^5ur^2t&=-\frac53\int x^4ur^3-\frac13\int x^5vr^3,\\
\int x^5v^2rt&=-\frac52\int x^4v^2r^2-\int x^5vr^3,\\
\int x^6vr^2t&=-2\int x^5vr^3-\frac13\int x^6r^4,\\
\int x^7r^3t&=-\frac74\int x^6r^4.
\end{aligned}
\tag{11}
\]
端项都由紧 \(u,v,r\) 支付。

全部 primitive 在(9)中合并为
\[
\int C\left(-xur+\frac32x^2vr+\frac12xv^2\right).
\]
括号正好是
\[
\left(-xuv+\frac{u^2}{2}+\frac34x^2v^2\right)'.
\]
保原 \(C\) 后作一次 IBP，端项因括号的紧原函数为零，得到
\[
\int (x^2r^2+2v^2)
\left(-xuv+\frac{u^2}{2}+\frac34x^2v^2\right).
\tag{12}
\]
所以这里是准确消去 primitive，不是将 \(C\) 的尾擅设为零。
该步本身甚至只需紧 outer \(u,v\)。

为完整记录所有系数，依次以九个局部积分
\[
A=\int x^2u^2r^2,\ B=\int x^3uvr^2,\ C_4=\int x^4v^2r^2,\
D=\int x^4ur^3,\ E_5=\int x^5vr^3,\ F_6=\int x^6r^4,
\]
\[
G=\int u^2v^2,\ H=\int xuv^3,\ I_4=\int x^2v^4
\]
作记账。\(C_4\) 不同于原 primitive \(C\)。

| 积分 | 式(10)全部含t项IBP | 其余局部项 | 式(12)原primitive | 合计 |
| --- | ---: | ---: | ---: | ---: |
| A | -3 | 9/2 | 1/2 | 2 |
| B | 8 | -11 | -1 | -4 |
| C4 | -5 | 25/4 | 3/4 | 2 |
| D | -5/6 | 3/2 | 0 | 2/3 |
| E5 | 4/3 | -2 | 0 | -2/3 |
| F6 | -1/24 | 1/8 | 0 | 1/12 |
| G | 0 | 3 | 1 | 4 |
| H | 0 | -2/3 | -2 | -8/3 |
| I4 | 0 | -5/6 | 3/2 | 2/3 |

局部项表另用
\(\int xu^2vr=-G/2-H\)、
\(\int x^2uv^2r=-2H/3-I_4/3\)、
\(\int x^3v^3r=-3I_4/4\)；
每式为紧总导数，原负轴也合法。

由(9)—(12)，对整个合法复 \(q\) 得
\[
\boxed{
\begin{aligned}
K_{YY,0}(q)=\mathcal K_Y(q):=\int\{&
2x^2(u-xv)^2r^2+\frac23x^4(u-xv)r^3+\frac1{12}x^6r^4\\
&+4u^2v^2-\frac83xuv^3+\frac23x^2v^4\}.
\end{aligned}}
\tag{13}
\]
所有高阶导数及原 primitive 已准确消去。
式(13)对 C² 范数连续，是完整四次多项式，不是一个未控制的余项记号。

## 4. 实输入的平方分解及它不能推出的结论

同一个局部多项式可完整写为
\[
\boxed{
\mathcal K_Y(u)=\int\left\{
2x^2r^2\left(u-xv+\frac{x^2r}{6}\right)^2
+\frac{x^6r^4}{36}
+\frac23v^2\bigl((2u-xv)^2+2u^2\bigr)
\right\}.}
\tag{14}
\]
展开第一项的 \(x^6r^4/18\) 再加 \(1/36\)，正好为(13)的 \(1/12\)。
其余项逐项相同。

对每个非零实紧光滑 \(u\)，(14)严格为正。
若它为零，非负项 \(x^6r^4\) 的积分为零，迫 \(r=0\) 于 \(x\ne0\)；
连续性再给 \(r(0)=0\)，故 \(u\) 是紧支撑仿射函数，只能为零。

必须区分两种对象：

- 对任意实 \(u\)，\(\mathcal K_Y(u)\) 是(13)定义的完整局部扩展，具有上述严格正性。
- 与真实 \(K_{YY,0}\) 相等的(13)，本稿是在满足(2)的整个复 \(q\) 上证明。非零实 \(u\) 不满足 \(I_0(u,u)=0\)。

合法复输入中的四次式不含共轭，不能由(14)推出
\(\operatorname{Re}\mathcal K_Y(q)\ge0\)，也不能据此排除真实圆。
本稿不构造一个合法反号圆、不宣称该角商已可自由调节；
这些都需要另付真实联调条件。

## 5. 原面积究竟给了什么

当前 \(Z=dL+eU\)，旧全相位 \(ZY_2\) 面积的四次 Fourier 系数迫
\[
d\,S_{LY,2}(q)+e\,S_{UY,2}(q)=0.
\tag{15}
\]
而本稿需要的角商是(7)的差。
在原小参数 \(0<\kappa^2<1/100\) 范围，
\[
d+e=\frac{\kappa(9\kappa^2-1)}{4h_e}\ne0.
\]
所以 (7)(15)准确等价于
\[
S_{LY,2}=-\frac{3e}{d+e}\mathcal K_Y,\qquad
S_{UY,2}=\frac{3d}{d+e}\mathcal K_Y.
\tag{16}
\]
不能仅从(15)这一条加权和为零，就把差(7)设成零。

(16)不证明 \(\mathcal K_Y\) 与全部其它已付门独立；
若存在另一个完整身份，它仍须给出并按当前整个圆核实。
本稿只是把遗漏的对象明确写成(13)，避免把“C²量”自动并入已付纤维。

## 6. 正域反演的独立代数核对，含真实积分常数

本节只核算(13)，不改变实际几何或最终圆。
设 \(u\) 支撑于一个远离零的正区间，定义
\[
(\mathcal T u)(z)=z^2u(1/z).
\]
\(\mathcal T^2=1\)，且
\[
(\mathcal Tu)''(z)
=2u(x)-2xv(x)+x^2r(x),\qquad x=1/z.
\tag{17}
\]
对紧输入的真实 IBP 给
\[
I_0(\mathcal Tu,\mathcal Tv)=I_2(u,v),\qquad
I_2(\mathcal Tu,\mathcal Tv)=I_0(u,v).
\tag{18}
\]
其中
\[
\frac{(2u-2xv+x^2r)^2}{x^2}
=x^2r^2+2v^2+
\left(4uv-2xv^2-\frac{4u^2}{x}\right)'.
\]
这条完整总导数也给原右积分的准确身份
\[
\boxed{\mathcal T\,P((\mathcal Tu)^2)
=4Y(u^2)+x^2I_2(u,u).}
\tag{19}
\]
反演把左右次序交换，(19)的最后一项就是必须保留的真实积分常数；
不能对一般输入删掉。

对合法 \(q\)，\(I_2(q,q)=0\)，故(19)第一层为 \(4Y(q^2)\)。
又 \(I_2(q,Y(q^2))=F_{Y,2}(q)=0\)，polarized (19)的 nested 常数也准确消失。
全部相关内输出因这些真矩而紧，(18)遂给
\[
K_{PP,2}(\mathcal Tq)=16K_{YY,0}(q).
\tag{20}
\]
原 \(F_{P,2}=\frac43\int xr^3-2\int vr^2\) 沿真紧 \(Pq^2\) 变分，
用 \(P'=-r^2,\ P''=-2rt\)，准确得到
\[
K_{PP,2}(q)=\frac43\int r^4.
\]
所以对本节的正域合法 \(q\)，
\[
\boxed{\mathcal K_Y(q)
=\frac1{12}\int
\frac{(2q-2xq'+x^2q'')^4}{x^2}.}
\tag{21}
\]
展开(21)，将
\(\int(u^4/x^2-4u^3v/x)=0\) 及紧总导数合并，恰为(13)。
例如余下两项
\[
\frac43\int\frac{(u-xv)^4}{x^2}
+\frac83\int(u-xv)^3r
=4G-\frac83H+\frac23I_4.
\]
这是第二条独立纸面核对。

式(21)只在支撑远离零的本节域使用。
它不被搬到跨零支撑上；通用且无奇点的完整原式始终是第3节(13)。
反演也没有被授予允许的几何变换或固定 g 的控制权限。

## 7. 完整 YY0 的两条实际义务

当前十二完整副本已经清除 angular odd 项。
R294 的原精确角分解给
\[
\boxed{
\mathcal Q_{YY,0}(\theta)
=\sin^2\theta\,\mathcal Q_{YY,0}(\pi/2)
+\sin^2\theta\cos^2\theta\,
   \operatorname{Re}\mathcal K_Y(f+ig).}
\tag{22}
\]
两种角函数线性独立。因此这个完整函数全相位为零，当且仅当
\[
\mathcal Q_{YY,0}(\pi/2)=0,\qquad
\operatorname{Re}\mathcal K_Y(f+ig)=0.
\tag{23}
\]
全偶反射的 \(YY_1=0\) 与已付 \(YY_2\) 不删除(23)。

下一构造必须先处理(23)的真实 C² 基线；
若为高频末控制器扩展有限纤维，还须从起点包含该局部四次式的实际平移系数，
证明原基线确已被支付，而非仅把新的未知目标添入映射。
之后需要把 \(\pi/2\) 的完整值与全部既有目标在同一母、实际正幅列和一个有限 \(N\) 上共同求根。
本稿没有完成这些实际正锥或同点根的证明。

其它完整对称函数、零／一 history、canonical period、平台/退化flux/端芽、
同一 gauge 的 joint 条件以及 README 的固定度量、C² 嵌入、连续 reach 与幅度目标仍按 open.md 继续。
本稿完成的是(1)、(13)、(14)、(19)—(23)的完整原式身份及准确适用范围。
