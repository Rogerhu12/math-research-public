# R770 — 新仿射方向的实际去 Gaussian 连接与完整首提升修正

日期：2026-11-15。**状态：以下原连接、单位共振及全原列的修正递推已证明。**

R769 的合流返回使用原未改动的 $\Theta,Q$。
去掉第一个 Gaussian 后，$\Theta^\circ,Q^\circ$ 不再满足同一无源仿射方程。
本篇计算其准确误差：它在普通 $w$ 系数中有一个单位首项，
在原 carry 环中则恰是必须保留的 $p\epsilon$ 项。
随后将它加入 R769 的整个导数递推和每条原单项式，
不只修正最高导数或一个选定列。

## 1. 同一物理参数和去 Gaussian 坐标

保 R763、R769 的
$$
y^2=x^3+b,\quad x'=2y,\quad y'=3x^2,\quad
t=-b/x^3,\quad \Theta=x\sigma^2,\quad Q=1+x\zeta/y,
$$
$$
w=z^6,\quad p=6s-1>101,\quad
L=s(p-1),\quad c=[w^s]\log(\sigma/z),\quad
\gamma=pc\in\mathcal O^\times.
$$
$b=1$ 时为 R769 的原三格；固定 $b=17$ 的同样恒等式也成立。
全部固定坏素数继续排除。

定义实际单位与导数
$$
\chi=\frac{x}{zy}=-1+O(w),\qquad
\mathscr D=\frac{x}{y}\frac d{dz}
=-6t\frac d{dt}
=6\chi\,w\frac d{dw}.
\tag{1}
$$
原 Gaussian 规范为
$$
\Theta^\circ=\Theta e^{-2cw^s},\qquad
Q^\circ=Q-(p+1)c\chi w^s.
\tag{2}
$$
(2) 正是 R763 的 $\sigma^\circ,\zeta^\circ$ 定义，不是另选一个连接。
由 R614 的 $X(w)=z^2x$ 与 $Y(w)=-z^3y$，
$\chi=-X/Y$ 在次数 $<L$ 全整，且为单位；
$\Theta^\circ=X(\sigma^\circ/z)^2$ 也在该窗全整且为单位。

置
$$
f(t)=\frac{1+2t}{1-t}.
$$
直接微分 (1) 给
$$
\boxed{
\mathscr D\log\chi=-f(t)-\chi,\qquad
\mathscr D(w^s)=(p+1)\chi w^s.
}
\tag{3}
$$
因此
$$
\boxed{
\mathscr D(\chi w^s)=-f(t)\chi w^s+p\chi^2w^s.
}
\tag{4}
$$
(4) 中的 p 来自 $6s-1=p$，不能改成零后再作首次提升。

## 2. 准确无源方程与实际误差的区别

原未改动坐标满足
$$
\mathscr D\Theta=2Q\Theta,\qquad
\mathscr DQ=\frac{2t}{1-t}-f(t)Q.
$$
用 (2)–(4) 得到
$$
\boxed{
\mathscr D\Theta^\circ=2Q^\circ\Theta^\circ,
}
\tag{5}
$$
以及
$$
\boxed{
\mathscr DQ^\circ
=\frac{2t}{1-t}-f(t)Q^\circ-\mathcal C,
\qquad
\mathcal C=(p+1)\gamma\chi^2w^s.
}
\tag{6}
$$
这是同一实际解析 germ 的精确恒等式。
特别，原仿射方程在去 Gaussian 后的缺项为
$$
\boxed{
(1-t)\mathscr DQ^\circ+(1+2t)Q^\circ-2t
=-(p+1)\gamma(1-t)\chi^2w^s .
}
\tag{7}
$$
由于 $t(0)=0,\chi(0)^2=1$，
$$
\boxed{
[w^s]\{\text{(7) 左边}\}
=-(p+1)\gamma\in\mathcal O^\times.
}
\tag{8}
$$
它是这个指定原坐标的实际单位，未借未识别的低系数。
由 (5)，$Q^\circ=\mathscr D\Theta^\circ/(2\Theta^\circ)$
在同一次数 $<L$ 的窗中整；没有将其对数原函数也认成整。

同样，
$$
\boxed{
\mathscr D\mathcal C
=\{-2f(t)+(p-1)\chi\}\mathcal C.
}
\tag{9}
$$
所以后续所有系数微分都能沿 (3)、(9) 保持同一个实际来源。

## 3. 在原 carry 环中是 pε，而非可删的普通单位

保 R763 同一有限目标
$$
\Gamma^+=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^{\ell+13}\epsilon^2),
\qquad \epsilon=w^s/p.
\tag{10}
$$
所需系数窗小于 $3s<L$；使用原 $\chi,t,\Theta^\circ,Q^\circ$ 的整截断。
在 (10) 上准确有
$$
\mathscr Dw=6\chi w,\qquad
\mathscr D\epsilon=(p+1)\chi\epsilon.
\tag{11}
$$
(11) 保定义理想：
$\mathscr D(w^s-p\epsilon)=(p+1)\chi(w^s-p\epsilon)$；
另两个生成元也只乘实际整系数。
所以它是整个目标上的导数，不会遗漏最高块或 carry。

在这个环中，(6) 的误差准确为
$$
\boxed{
\mathcal C=p(p+1)\gamma\chi^2\epsilon.
}
\tag{12}
$$
(8) 与 (12) 完全相容：
同一个 $w^s$ 普通单位，在原带除 p 的 Gaussian 目标中位于 $p\epsilon$。
因此模 p 的目标暂时看不到它，但首 Bockstein 和下一位必须保留它。
这里没有将 (8) 宣称为原中央非零或完整原格的非零余类。

## 4. 合流算子的完整修正递推

令 $n>0$。R769 的未改动算子记为
$$
A_0=1,\quad A_1=\mathscr D,\quad
A_{j+1}=\mathscr D\circ A_j+jfA_j
       -4nj\frac{t}{1-t}A_{j-1}.
\tag{13}
$$
它满足 $\Theta^nQ^j=(2n)^{-j}A_j(\Theta^n)$。

对实际去 Gaussian 坐标，正确定义是
$$
A_0^\circ=1,\qquad A_1^\circ=\mathscr D,
$$
$$
\boxed{
A_{j+1}^\circ
=\mathscr D\circ A_j^\circ+jfA_j^\circ
 -4nj\frac{t}{1-t}A_{j-1}^\circ
 +2nj\,\mathcal C\,A_{j-1}^\circ .
}
\tag{14}
$$
所有系数微分都按 (1)、(3)、(9) 进行。
则完整身份为
$$
\boxed{
(\Theta^\circ)^n(Q^\circ)^j
=(2n)^{-j}A_j^\circ((\Theta^\circ)^n).
}
\tag{15}
$$
证明与 R769 的完整归纳相同，但必须在
$\mathscr D(Q^\circ)^j$ 中保留
$-j\mathcal C(Q^\circ)^{j-1}$。
解出下一次幂后恰给 (14) 的最后一项；所有次数的归纳因此成立。

第一处实际差异已经在 j=2：
$$
\boxed{
(\Theta^\circ)^n(Q^\circ)^2
=\frac1{4n^2}
 \left(\mathscr D^2+f\mathscr D-\frac{4nt}{1-t}
                   +2n\mathcal C\right)(\Theta^\circ)^n.
}
\tag{16}
$$
相对直接套用 (13)，差为
$\mathcal C(\Theta^\circ)^n/(2n)$。
若 $p\nmid2n$，其普通 $w^s$ 系数为
$(p+1)\gamma/(2n)$，是单位；
在 (10) 中则精确是原 $p\epsilon$ 修正。
这个 j=2 基分量不被擅自认成原三格中一条独立可选列。

### 4.1 全部首次修正使用同一个递推

令 $\Delta_j=A_j^\circ-A_j$。
由 (12)、(14) 及定义理想的稳定性，
$$
\boxed{\Delta_j\in p\epsilon\,\Gamma^+[\mathscr D]\quad(j\ge0).}
\tag{17}
$$
这里是左系数微分算子，包含系数被导数作用产生的全部项。

记 $\mathcal E_j=(\Delta_j/p)\bmod p$，
在 $\Gamma^+/p$ 中保原 $\chi,t,\gamma$。
则
$$
\mathcal E_0=\mathcal E_1=0,
$$
$$
\boxed{
\mathcal E_{j+1}
=\mathscr D\circ\mathcal E_j+jf\mathcal E_j
 -4nj\frac{t}{1-t}\mathcal E_{j-1}
 +2nj\gamma\chi^2\epsilon\,A_{j-1}.
}
\tag{18}
$$
(18) 是原 (14) 的模 $p^2$ 结果：
最后一项里的 $\Delta_{j-1}$ 带第二个 p，故消失；
$p+1$ 约化为1。
例如 $\mathcal E_2=2n\gamma\chi^2\epsilon$。
后续项中的 $\mathscr D\epsilon=\chi\epsilon\bmod p$ 和
$\mathscr D\chi=-f\chi-\chi^2$ 均保留。
这些行不能逐 j 另行选择。

## 5. 原每一列还必须保 Q 平移

继续 R769 的同一列指标 $(\alpha,\beta,\nu)$、$n=17\alpha+36\beta+102\nu$、
$J=6\nu$ 和完整多项式
$$
F_{\alpha,\beta,\nu}(t,Q)=\sum_{j=0}^{J}f_j(t)Q^j.
$$
在 (10) 中，
$$
Q=Q^\circ+h\epsilon,\qquad h=(p+1)\gamma\chi,\qquad
\Theta=\Theta^\circ e^{2\gamma\epsilon}.
$$
因此原单项式的完整来源是
$$
\boxed{
S^\alpha T^\beta U^\nu
=e^{2n\gamma\epsilon}(\Theta^\circ)^n
 \sum_{l=0}^2\frac{(h\epsilon)^l}{l!}
 (\partial_Q^lF_{\alpha,\beta,\nu})(t,Q^\circ).
}
\tag{19}
$$
这是整个 $\epsilon^2$ 目标的精确式，
既保总 Gaussian，也保真正仿射平移，不把
$(\Theta^\circ)^nF(t,Q^\circ)$ 单独冒充原列。

把 (15) 代入，得到完整合流表达
$$
\boxed{
e^{2n\gamma\epsilon}
\sum_{l=0}^2\frac{(h\epsilon)^l}{l!}
\sum_{j=l}^{J}
 f_j(t)(j)_l(2n)^{-(j-l)}
 A_{j-l}^\circ((\Theta^\circ)^n).
}
\tag{20}
$$
其中 $(j)_l=j(j-1)\cdots(j-l+1)$。
每个原列的所有系数仍由同一个 $F_{\alpha,\beta,\nu}$ 决定。
R769 的真实原零点和帽、固定分母及 p 范围继续保留。

若错误地将 (20) 中的 $A^\circ$ 全换为 A，
所漏的完整首 Bockstein 除 p 后恰为
$$
\boxed{
e^{2n\bar\gamma\epsilon}
\sum_{l=0}^1\frac{(\bar h\epsilon)^l}{l!}
\sum_{j=l}^{J}
 \bar f_j(t)(j)_l(2n)^{-(j-l)}
 \mathcal E_{j-l}((\bar\Theta^\circ)^n)
\quad\bmod p.
}
\tag{21}
$$
$l=2$ 的项因 (17) 另含 $\epsilon$ 而在 $\epsilon^3=0$ 中消失。
(21) 仍保外面指数与 $l=1$ 的混合项；
它们正会进入第二块，不能只记 j=2 的一个单位。

当 $p>204D$ 时，(20)–(21) 中的 $2n$ 和所有小阶乘均为单位，
正好落在 R769 已付的原转换范围。
较小素数仍按原实际分母读取，不扩大为固定坏集。

## 6. 实际曲线约束的同一个二阶误差

令抽象仿射导数为
$$
\mathscr A=-6t\partial_t+2Q\Theta\partial_\Theta
 +\left(\frac{2t}{1-t}-fQ\right)\partial_Q.
$$
对任意实际多项式 H，在去 Gaussian germ 上准确有
$$
\boxed{
\mathscr D\,H(t,\Theta^\circ,Q^\circ)
=(\mathscr AH)(t,\Theta^\circ,Q^\circ)
 -\mathcal C(\partial_QH)(t,\Theta^\circ,Q^\circ).
}
\tag{22}
$$
若 F 不含 Q，并令 $H_F=\mathscr AF$，
则第一阶仍是完整相容的
$\mathscr D F=H_F$；
第二阶则为
$$
\boxed{
(\mathscr A^2F)(t,\Theta^\circ,Q^\circ)
-\mathscr D^2F(t,\Theta^\circ)
=2\mathcal C(\Theta\partial_\Theta F)(t,\Theta^\circ).
}
\tag{23}
$$
当原 $e=(\Theta\partial_\Theta F)(0,1)$ 是单位时，
(23) 的普通 $w^s$ 系数为 $2(p+1)\gamma e$，
在 carry 目标中同样必须作为 $p\epsilon$ 项处理。
(23) 不允许把 F 的高接触、其一阶约束和二阶约束当作三个独立零条件。

本篇已给新三格的完整实际连接和首提升修正。
它尚未证明 R769 整个共同前缀上的改进惰性估值，
也未将原中央失败传播为新 U 的中央条件。
R750–768 的全来源、两个十三行、实际高尾及同一个修正 R 继续保持；
尤其 (21) 的完整列组合是否落全像，仍须在原来源上判定。

依赖：
[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)；
[R763](R763-positive-derivative-affine-zeta-model-and-full-gaussian-transport.md)；
[R769](R769-original-confluent-theta-return-for-positive-derivative-grid.md)。
全文是原完整方程的符号推导，没有新增数学执行或输出数据。
