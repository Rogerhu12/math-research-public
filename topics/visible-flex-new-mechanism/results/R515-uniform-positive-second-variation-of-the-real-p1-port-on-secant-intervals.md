# R515：任意合法正割区间上的真实 $p_1$ 二次强制正性

日期：2026-11-16。**完整纸面证明；没有执行 profile、求积、符号程序、数值秩、ODE 或开发检查。**

本稿研究 [R509](R509-five-endpoint-real-half-image-and-exact-short-bridge-boundary.md) 的真实矩阵端点在较长参考正割上的行为。结论比短盒估计更强：只要首阶 $k,\omega$ 返回并且原 $p_0$ 首阶增量为零，$p_1$ 的真二次增量在任意固定合法正割区间上都有统一下界。区间不必短，也不要求参考高度单调。

准确下界是
$$
Q(b)\ge\frac{15}{32}\int b^2,
$$
其中 $b=\partial_\epsilon k_\epsilon|_0$。它来自一个完整平方恒等式，所有分部积分端项均由两个原端点条件支付。故把短参考段单纯延长，不能把原单侧 $p_1$ 端口变成负抵消。结论只约束正割附近的二次行为，不排除有限幅值的非正割路径，也不从一个局部符号推出所有真实词不能满足 $M=0$。

## 1. 固定实际区间与原坐标

取一个固定紧区间
$$
I=[\alpha,\beta]\Subset(-\pi/2,\pi/2),\qquad \alpha<\beta.
\tag{1}
$$
角变量与原实际时间只相差一个固定常数，故 $d\sigma=ds$。更一般的合法正割分支可以先作一次整数周期平移到(1)，以后不再沿路径移动坐标。

参考 scalar 是
$$
\bar h(\sigma)=H\sec\sigma,\qquad
\bar k=0,\qquad \bar\omega=\omega_0,\qquad H>0.
\tag{2}
$$
因此 $\bar h_s/\bar h=\tan\sigma$，且
$(\tan\sigma)_s=1+\tan^2\sigma$。允许 $\alpha<0<\beta$；所有公式也适用于只在一个单调半支上的区间。由于(1)，全部显示的 $\tan,\sec$ 在该固定区间有界。

一次固定母坐标
$$
y=x+\omega_0,\qquad \varpi=\omega-\omega_0.
$$
以 $p_0^y,p_1^y,p_2^y$ 表示原 E8 在这个固定坐标中的三个原坐标。按 [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)(9)，真实密度准确是
$$
\boxed{
(M_{\rm raw})_{p_0^y}
=-\frac{k\{1+(h\varpi-k)^2\}}{2h},\qquad
(M_{\rm raw})_{p_1^y}
=k^2-kh\varpi,\qquad
(M_{\rm raw})_{p_2^y}=-kh/2 .
}
\tag{3}
$$
同时原水平关系是
$$
\varpi_s=\frac{k_s}{2h}.
\tag{4}
$$
这些是原完整密度，不是 principal 近似。全文没有在中途改变 $\omega_0$、重新锚定 $\mathsf m$ 或独立指定某个 history。

## 2. 实际路径族及本稿恰需的端点条件

设 $\epsilon\mapsto(h_\epsilon,k_\epsilon,\omega_\epsilon,\mathsf m_\epsilon)$ 是同一正长度区间上的真实光滑路径族，以(2)为 $\epsilon=0$，逐条满足(4)和
$$
(\mathsf m_\epsilon)_s
=M_{\rm raw}(h_\epsilon,k_\epsilon,\omega_\epsilon,
             (h_\epsilon)_s,(k_\epsilon)_s).
\tag{5}
$$
若它由 R508/R509 的同一完整 ruling 反馈生成，则所有原规范、profile、第三／第四恢复及真实入值都继续保留；下面的恒等式其实只需(3)–(5)，不需要把其它门先当成零。

所有路径取相同的左端 $k=0,\varpi=0$，并要求首阶
$$
b(\alpha)=b(\beta)=0,\qquad
c(\alpha)=c(\beta)=0,
\tag{6}
$$
其中
$$
b=\left.\partial_\epsilon k_\epsilon\right|_0,\qquad
c=\left.\partial_\epsilon\varpi_\epsilon\right|_0.
$$
例如左 germ 保原值、终端 $k=\varpi=0$ 准确成立的控制族自然满足(6)。只需端值；不必以更强的逐端紧支撑代替证明。

还要求原 $p_0^y$ 的首阶增量为零：
$$
\left.\partial_\epsilon
\int_\alpha^\beta(M_{\rm raw})_{p_0^y}\,d\sigma
\right|_0=0.
\tag{7}
$$
准确保持该矩阵增量为零当然足够；本文只使用其首阶后果。没有使用 $p_2$ 返回，因此结论适用于 R509 的四个返回条件，并且不多消费其中的 $p_2$ 行。

路径可以有任意真实高度首变分
$\partial_\epsilon h_\epsilon|_0$。下文会直接说明为何它不进入 $p_1$ 的二次系数；不假设高度沿整个族固定。

## 3. 两个原端点条件恰给两个真实正交关系

在(2)上线性化(4)，由于参考 $k_s=0$，
$$
c'(\sigma)=\frac{b'(\sigma)\cos\sigma}{2H}.
$$
用(6)的左端值准确积分：
$$
\boxed{
c(\sigma)=\frac1{2H}
\left\{b(\sigma)\cos\sigma+A(\sigma)\right\},\qquad
A(\sigma)=\int_\alpha^\sigma b(t)\sin t\,dt .
}
\tag{8}
$$
没有漏掉高度首变分：它在(4)中乘参考 $k_s=0$，所以准确没有贡献。

由右端 $b(\beta)=c(\beta)=0$，得
$$
A(\beta)=\int_\alpha^\beta b\sin\sigma=0.
\tag{9}
$$
另一方面，(3)在 $k=\varpi=0$ 上的一阶项为
$-b/(2\bar h)$，故(7)恰为
$$
C(\beta)=\int_\alpha^\beta b\cos\sigma=0,\qquad
C(\sigma)=\int_\alpha^\sigma b(t)\cos t\,dt.
\tag{10}
$$
式(9)来自真实 $\omega$ 返回，式(10)来自真实 $p_0^y$ 行。不能只保其中一个后删去后文的端项。

## 4. $p_1$ 的实际二次系数，含完整归一

参考 $p_1^y$ 密度为零。由(3)，对同一实际族
$$
k_\epsilon^2-k_\epsilon h_\epsilon\varpi_\epsilon
=\epsilon^2\{b^2-\bar h\,bc\}+O(\epsilon^3)
\tag{11}
$$
一致成立。若只假设二阶光滑依赖，余项改为 $o(\epsilon^2)$；本稿后面用到的光滑有限控制／IFT 族具有所写的三阶余项。

高度首变分在第二项中同时乘 $k_\epsilon=O(\epsilon)$ 和
$\varpi_\epsilon=O(\epsilon)$，所以只从三阶开始贡献。这就是(11)不需要清高度端点或假高度固定的原因。

记从相同真实入值出发的 $p_1^y$ 区间增量为
$\Delta m_{p_1^y}(\epsilon)$，则
$$
\boxed{
\Delta m_{p_1^y}(\epsilon)
=\epsilon^2Q(b)+O(\epsilon^3),\qquad
Q(b)=\int_\alpha^\beta(b^2-\bar h\,bc)\,d\sigma.
}
\tag{12}
$$
因此这里 $Q$ 是 $\epsilon^2$ 的系数；真正的二阶参数导数是 $2Q$，没有另漏一个 $1/2$。

代入(8)和 $\bar h=H\sec\sigma$，得到
$$
Q(b)=\frac12\int b^2-\frac12\int bA\sec\sigma .
\tag{13}
$$
所有积分从此都在同一个固定 $I$ 上。参考尺度 $H$ 在(13)准确消去，不是被归一后遗忘。

## 5. 全区间 Green 变量与所有实际边项

定义
$$
\boxed{
J(\sigma)=\int_\alpha^\sigma\sin(\sigma-t)b(t)\,dt
=\sin\sigma\,C(\sigma)-\cos\sigma\,A(\sigma).
}
\tag{14}
$$
这只是原实函数 $b$ 的一个普通积分，不引入新的 profile 原函数或新的几何自由度。它满足
$$
J''+J=b,\qquad J(\alpha)=J'(\alpha)=0,
$$
$$
J'=\cos\sigma\,C+\sin\sigma\,A.
\tag{15}
$$
由(9)(10)，还准确有
$$
\boxed{J(\beta)=J'(\beta)=0.}
\tag{16}
$$
反解(14)(15)给
$$
A=\sin\sigma\,J'-\cos\sigma\,J.
\tag{17}
$$
故(13)变成
$$
Q=\frac12\int b^2+\frac12\int bJ-\frac12\int b\tan\sigma\,J'.
\tag{18}
$$

将 $b=J''+J$ 代入。两次常规 IBP 的全部边项是
$$
[J'J]_\alpha^\beta,\qquad
[\tan\sigma\,J'^2]_\alpha^\beta,\qquad
[\tan\sigma\,J^2]_\alpha^\beta,
$$
以及展开平方时同一个 $[J'J]_\alpha^\beta$。它们由(15)(16)和区间(1)逐个为零。没有使用在正割极点外不存在的端值，也没有在 $\sigma=0$ 除以 $\sin\sigma$。

逐项得到
$$
\begin{aligned}
Q
={}&\frac12\int J''{}^2-\frac32\int J'^2+\int J^2\\
&+\frac14\int\sec^2\sigma\,(J'^2+J^2)\\
={}&\frac12\int J''{}^2-\frac54\int J'^2+\frac54\int J^2
+\frac14\int\tan^2\sigma\,(J'^2+J^2).
\end{aligned}
\tag{19}
$$
例如
$-\tfrac12\int J''\tan\sigma J'=\tfrac14\int\sec^2\sigma J'^2$；
$-\tfrac12\int J\tan\sigma J'=\tfrac14\int\sec^2\sigma J^2$。
二者都保了原因子。

## 6. 完整平方身份与统一严格下界

由 $b=J''+J$ 及同一个 $[J'J]=0$，(19)恰可重写成
$$
\boxed{
Q(b)=
\frac{15}{32}\int b^2
+\frac1{32}\int(J''+5J)^2
+\frac14\int\tan^2\sigma\,(J'^2+J^2).
}
\tag{20}
$$
核对前三项，只需
$$
\frac{15}{32}\int(J''+J)^2+
\frac1{32}\int(J''+5J)^2
=\frac12\int J''{}^2-\frac54\int J'^2+\frac54\int J^2.
$$
没有使用频谱、数值特征值或某个未给的 Poincaré 常数。

于是得到本稿的完整结论。

**定理。** 在任意(1)的固定合法参考正割区间上，任意满足真实首阶端点条件(6)(7)的路径变分都有
$$
\boxed{
Q(b)\ge\frac{15}{32}\|b\|_{L^2(I)}^2.
}
\tag{21}
$$
若 $b\not\equiv0$，则 $Q(b)>0$。下界不依赖 $H$，也不需要
$0<\tan\sigma<1$、高度单调或 R509 的短盒小常数。

特别，对每一个固定且 $b\ne0$ 的光滑实际控制曲线，存在
$\epsilon_0>0$，使
$$
\Delta m_{p_1^y}(\epsilon)>0
\quad(0<|\epsilon|<\epsilon_0).
\tag{22}
$$
这两个参数符号都对应同一个正长度实际路径，未使用负时间。若某条参数曲线的首阶 $k$ 方向恰为零，(21)不替它决定更高阶首项。

## 7. 与完整 ruling 及真实端点构造的接线

[R508](R508-nonzero-second-gauge-opens-secant-exit-and-two-sided-matrix-port.md) 的同一个第二／第三规范给正规非正割出口；R509 再由四个真实返回行的 IFT 得到 $p_1=a^2$ 的局部半像。它们保全部 profile、原锚和真实 incoming。

本稿没有替换这些控制或规范。若在一个较长区间上已有同规范的光滑反馈／实际路径族，且该族保(6)(7)，则它的 $p_1$ 系数自动受(20)约束。若较长区间上反馈本身尚未支付，则(20)仍是任何未来这类实际族必须满足的身份，不能把它当成反馈存在证明。

R509 的 $p_2$ 返回条件只进一步缩小允许的 $b$；因为本稿没有消费该条件，它不能破坏(21)。四个返回行的任何真实有限 IFT 补偿也不会产生遗漏的二次项：补偿后的实际首阶 $b,c$ 仍满足(6)–(10)，而(11)已经包括了所有高度首变分可能出现的阶数。

若使用不同的真实左 history，本稿讨论的是区间的真实增量，而不是把入值重置成零。一个已经存在的负 $p_1$ incoming 当然可能与正增量相加；本文没有说那个 incoming 已可在相同完整 ruling 下提供。其它五矩、frame、位置、原 $T,V$、两端 germs 和全部 period／十三规范仍须在同一最终词中实际处理。

原 $B$ 规范、固定有限秩第二母或别的已经合法固定规范，都不会改变(3)(4)的 raw 矩阵关系。因此只要它们产生的是本稿实际路径族，(20)同样适用；不能靠重新称呼规范把同一个正二次增量变成 signed 负块。

## 8. 精确的下一步边界

(21)严排的是“延长参考正割后，再用充分小的同规范扰动取得负 $p_1$”这一条路线。它的范围比 R509 的短盒判据大，但不是任意 $h,k$ 的全局正性。

事实上一般实际高度的精确公式仍为
$$
\Delta m_{p_1^y}
=\frac12\int k^2
-\frac12\int h(s)k(s)
       \left(\int_\alpha^s
          \frac{k(t)h'(t)}{h(t)^2}\,dt\right)ds,
\tag{23}
$$
前提是同一个左端 $k=\varpi=0$。离开参考后(23)继续成立，
但(14)–(20)所用的精确正割结构不再自动成立。本文不根据二次展开给(23)的有限幅值符号，也不排除真正走出正割邻域后取得负抵消。

因此后继必须研究有限幅值、实际非恒的完整受约束路径，而不能只增加同一正割附近的参数数目或延长其时间。R512 的固定全路径线性规范方程、真实矩阵 ODE 和所有全局成本仍需同时满足。固定度量有限等距族、闭嵌入与厚度主目标尚未完成。
