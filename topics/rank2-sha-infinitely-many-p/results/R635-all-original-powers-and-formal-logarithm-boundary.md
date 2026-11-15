# R635 — 原来源所有 p 幂的同一形式群边界

日期：2026-11-15。**状态：已证明。**

R632 已给原归一来源 \(B^p\) 的准确半径
\(R_E=p^{-1/(p^2-1)}\) 及闭边界非 Tate。
本篇证明继续升幂也不会越过这个原 \(z\) 边界：
\[
\boxed{\operatorname{rad}_z(B^{p^e})=R_E,\qquad
 B^{p^e}\notin\mathbf C_p\langle z/R_E\rangle
 \quad\hbox{对全部 }e\ge1.}
\tag{1}
\]
这对原 \(f_4,f_1,S,T\) 和质量一参考 \(H_{38}\) 都成立。
没有 \(e\le p-2\) 的限制，也没有假设原中央 \(j\) 为零。

关键不是在每个新幂中继续寻找一个同样的坏系数。
当 \(e\ge2\) 时，原 \(u\) 参数中的 sigma 幂事实上已经可在闭
\(R_E\) 指数化；阻碍来自同一个原形式对数在该边界的非零零点。
对原点阶数为零的 \(H_{38}\)，还须保全部代数因子并证明一个
严格主导的边界对数值不能相消。

## 1. 同一原来源与两个真实参数

保持 R632 的惯性素数和全部规范：
\[
p=6s-1>71,\quad b=17,\quad
L=(p^2-1)/6=s(p-1),\quad R_E=p^{-1/(p^2-1)},
\quad v_p(p)=1 .
\]
在 \(y^2=x^3+b\)、\(dx/(2y)=dz\) 上，保持
\[
u=x^{-1/2}=z+\cdots,\quad \tau=bu^6,\quad
C(\tau)=(1+\tau)^{-1/2},\quad
H(\tau)=\sum_{n\ge0}\frac{C_n}{6n+1}\tau^n,\quad z=uH(\tau).
\]
原 sigma 的同一个 \(u\) 参数函数为
\[
K(\tau)=\left(\frac{\sigma(z(u))}{u}\right)^6,\qquad
\mathscr L=\log K.
\]
对原
\[
\mathcal F=\sigma^m x^\alpha(-y)^\beta Q(\tau),\quad
d=m-2\alpha-3\beta\ge0,\quad B(z)=z^{-d}\mathcal F(z),
\tag{2}
\]
保持固定整数 \(m,\alpha,\beta\)，
\(m\in\mathbf Z_p^\times\)、\(Q\in1+\tau\mathbf Z_p[[\tau]]\)。
原五个实例的 \((m,\alpha,\beta,d)\) 分别为
\[
\begin{array}{c|rrrr}
 &m&\alpha&\beta&d\\ \hline
f_4&6&1&0&4\\
f_1&6&1&1&1\\
S&34&14&0&6\\
T&72&33&0&6\\
H_{38}&38&19&0&0 .
\end{array}
\tag{3}
\]
其中每个 \(Q\) 都是该来源的完整原因子，未作替换。
记
\[
A(\tau)=(1+\tau)^{\beta/2}Q(\tau)\in1+\tau\mathbf Z_p[[\tau]].
\]
因为 \(p\ne2\)，这里及其逆的系数都整。原正式身份是
\[
\boxed{B(z(u))=H(\tau)^{-d}K(\tau)^{m/6}A(\tau).}
\tag{4}
\]
所有分数幂均按常数项一的原形式级数定义。

以下可在 \(\mathbf C_p\) 上工作；若闭 \(R_E\) 的 Tate 性在
原系数域成立，延标量以后也成立，故所证反证足够。

## 2. 原 H 的边界缩减与全部非零零点

先加强 R632 的闭盘范数结论。
由
\[
H_n=\frac{(-1)^n}{4^n(6n+1)}\binom{2n}{n}
\]
及原二项式进位计数，若 \(a=v_p(6n+1)\)，则
\[
v_p(H_n)\ge-\lfloor a/2\rfloor.
\tag{5}
\]
具体地，\(6n\equiv-1\pmod{p^a}\) 迫使最低 \(a\) 位交替为
\(5s-1,s-1,\ldots\)；在 \(n+n\) 中至少有
\(\lceil a/2\rceil\) 个进位，除以 \(6n+1\) 后即得 (5)。
这保留了所有高阶分母。

若 \(k=\lfloor a/2\rfloor\ge1\)，
\[
n\ge(p^{2k}-1)/6=L(1+p^2+\cdots+p^{2k-2}).
\]
所以
\[
v_p(H_n)+n/L\ge0,
\]
且对 \(n>0\) 只有 \(n=L\) 可能等号：
\(k=0\) 时 \(n/L>0\)，\(k=1\) 时除 \(n=L\) 外严格，
\(k\ge2\) 时上述几何和严格大于 \(k\)。
该加权估值随 \(n\) 趋于无穷。

原唯一端点还满足 R619/R630 已付的准确同余
\[
\boxed{pH_L\equiv-1\pmod p.}
\tag{6}
\]
这是整个原 \(H\) 的实际二项式端点，不是一个可调的形式群参数。

取 \(\varpi^{p^2-1}=p\)，令 \(u=\varpi U\)。由 \(b\in\mathbf Z_p^\times\)
及 \(p-1\mid L\)，有 \(b^L\equiv1\pmod p\)。
于是 (5)–(6) 给完整 Tate 缩减
\[
H(b\varpi^6U^6)\in\mathbf C_p\langle U\rangle,\qquad
\boxed{\overline{H(b\varpi^6U^6)}=1-U^{p^2-1}.}
\tag{7}
\]
除常数和第 \(p^2-1\) 次项以外，每个系数都严格小于一，
并且全部高尾趋于零；不是仅一个有限 jet 的同余。

约化多项式有 \(p^2-1\) 个不同非零根，导数在每个根处为单位。
逐个 Hensel 提升（即在该剩余圆盘上的严格 Newton 收缩）
给 \(p^2-1\) 个简单根；Tate 的 Weierstrass 分解以
最高范数一的次数 \(p^2-1\) 为其次数，所以没有额外根。
故
\[
\boxed{
H(bu_T^6)=0,\qquad |u_T|=R_E,\qquad z(u_T)=0
}
\tag{8}
\]
恰有 \(p^2-1\) 个非零简单解。
在严格内盘上 \(H-1\) 的范数小于一，所以不存在非零内部解。
本篇只需 (8) 中任意一个解，不需要把它另作算术挠点命名。

同时 R632 的真实代换界仍为
\[
H(bu^6)\in\mathbf C_p\langle u/R_E\rangle,\quad
\|H\|_{R_E}=1,\quad \|z(u)\|_{R_E}\le R_E.
\tag{9}
\]
这里保留正向代换；闭边界没有调用形式逆 \(u(z)\)。

## 3. 升到第二个 p 幂后，u 参数指数确实延过边界

原完整对数系数为
\[
\mathscr L_n=\frac{(-1)^n}{n}
 \prod_{j=1}^n\frac{6j-4}{6j-1}.
\tag{10}
\]
R632 的完整分母计数给
\[
v_p(\mathscr L_n)\ge-\lfloor\log_p(6n)\rfloor,\quad
p\mathscr L_n\in\mathbf Z_p\ (n<p^2),\quad
v_p(\mathscr L_s)=-1,\quad
\mathscr L_n\in\mathbf Z_p\ (n<s).
\tag{11}
\]
在 \(|u|=R_E\) 时，\(\tau^n\) 的权估值为 \(n/L\)。
因而 \(p\mathscr L\) 的唯一最小权估值项是 \(n=s\)，其值为
\[
s/L=1/(p-1).
\tag{12}
\]
所有其余项严格大于 (12)，高尾权估值趋于无穷。
为明确全部高尾而非仅低窗，\(n\ge p^2\) 时有
\[
v_p(p\mathscr L_n)+n/L
 \ge 1+n/L-\log_p(6n)>4,
\]
且右边严格递增到无穷；有限较低项由 (11) 支付。

对全部 \(e\ge2\)，因此
\[
\frac{mp^e}{6}\mathscr L(bu^6)
\]
在闭 \(R_E\) 的最小权估值是
\[
\eta_e=e-1+\frac1{p-1}>\frac1{p-1},
\tag{13}
\]
仍只有 \(n=s\) 取得它。
有限项的严格间隔和线性趋大的高尾还保证：可取某个
\(R_{e,+}>R_E\)、\(R_{e,+}<1\)，所有项在这个稍大闭盘的
最小权估值仍严格大于指数阈值 \(1/(p-1)\)。
故
\[
K(bu^6)^{mp^e/6}
=\exp\!\left(\frac{mp^e}{6}\mathscr L(bu^6)\right)
\tag{14}
\]
及其逆都是闭 \(R_{e,+}\) 的 Tate 单位。

这与 R632 的 \(e=1\) 临界指数不同。不能在证明 (1) 时
假称每个 \(e\) 在 \(u\) 参数中仍有同一个临界发散指数。

在任意一个边界点 \(|u|=R_E\)，唯一最小项不可能被其它项相消，
故有真正的点值等式
\[
v_p\!\left(\frac{mp^e}{6}\mathscr L(bu^6)\right)=\eta_e.
\tag{15}
\]

## 4. 原全部代数因子不能抵消该边界值

对任意 \(A\in1+\tau\mathbf Z_p[[\tau]]\)，有
\[
n[\tau^n]\log A=[\tau^{n-1}]A'/A\in\mathbf Z_p.
\]
所以保持完整 \(A\)，得到
\[
v_p([\tau^n]\log A)\ge-v_p(n).
\tag{16}
\]
我们需要比较的不是某个 \(A\) 截断，而是全部 \(n\ge1\)：
\[
\boxed{e-v_p(n)+n/L>\eta_e.}
\tag{17}
\]

令 \(a=v_p(n)\)。若 \(a=0\)，则左边至少 \(e+1/L>\eta_e\)。
若 \(a=1\)，由 \(n\ge p>s\)，
\[
e-a+n/L\ge e-1+p/L>e-1+s/L=\eta_e.
\]
若 \(a\ge2\)，则
\[
p^a/L-a
\]
随 \(a\) 严格增加，因为相邻差为
\(p^a(p-1)/L-1>0\)，其 \(a=2\) 值已经大于四。
从而 (17) 同样严格成立。
右边的完整权估值下界也趋于无穷，因此没有无限尾逼近并抵消
(15) 的问题。

记原完整乘积
\[
M_e(u)=K(bu^6)^{mp^e/6}A(bu^6)^{p^e}.
\tag{18}
\]
它及其逆都在稍大于 \(R_E\) 的闭盘 Tate；其对数是
\[
\log M_e=\frac{mp^e}{6}\mathscr L+p^e\log A.
\]
由 (15)–(17)，对每一个 \(|u|=R_E\)，准确有
\[
v_p(\log M_e(u))=\eta_e.
\]
因为 \(\eta_e>1/(p-1)\)，\(p\) 进指数在这里满足
\(v_p(\exp(t)-1)=v_p(t)\)。因此
\[
\boxed{v_p(M_e(u)-1)=\eta_e,\qquad M_e(u)\ne1
 \quad(|u|=R_E,\ e\ge2).}
\tag{19}
\]
同时 \(M_e(u)\) 始终为单位，绝不为零。
这既保留了 \(Q\) 全部系数，也保留了原 \((1+\tau)^{\beta/2}\)；
对 \(H_{38}\) 的零原点阶数情形，(19) 是必要的额外论证。

## 5. 原 z 闭边界的反证与准确半径

\(e=1\) 已由 R632 完整证明。
固定 \(e\ge2\)，反设 \(B(z)^{p^e}\) 属于
\(\mathbf C_p\langle z/R_E\rangle\)。

由 (9)，Tate 级数可与原 \(z(u)\) 合成。
将正式身份 (4) 升幂后先乘回整个 \(H^{dp^e}\)，得到闭盘身份
\[
\boxed{
H(bu^6)^{dp^e}\,B(z(u))^{p^e}=M_e(u).
}
\tag{20}
\]
左边因假设及 \(d\ge0\) 为 Tate，右边由 (18) 已经 Tate；
两边的原点形式级数相等，故在整个闭盘相等。
此步骤没有在 \(H\) 的零点处除以 \(H\)。

取 (8) 中任意一个 \(u_T\)。

若 \(d>0\)，(20) 左边为零，右边为单位，矛盾。
若 \(d=0\)，则 \(z(u_T)=0\)、\(B(0)=1\)，
(20) 左边恰为一；右边由 (19) 不为一，仍矛盾。
这支付 (3) 中全部五个来源，包括参考 \(H_{38}\)。

另一方面，R632 已证明对每个闭 \(R<R_E\)，
\(B^p\) 及其逆都是范数一的 Tate 单位。
继续取整数幂得到
\[
B^{p^e},\,B^{-p^e}\in
\mathbf C_p\langle z/R\rangle^\times,\qquad
\|B^{\pm p^e}\|_R=1.
\tag{21}
\]
所以半径至少为 \(R_E\)。
若半径严格大于 \(R_E\)，级数必为闭 \(R_E\) 的 Tate 元，
与 (20) 的反证冲突。故半径恰为 \(R_E\)，(1) 得证。

原未归一来源仍为
\[
\mathcal F^{p^e}=z^{dp^e}B^{p^e}.
\]
乘这个有限单项式不改变准确半径与闭边界非 Tate，
但真实首阶 \(dp^e\) 必须保留。
特别原 \(S,T\) 在 \(w=z^6\) 中的共同首阶为 \(p^e\)。

## 6. 任意含 p 的正整数幂与真实成本

同样结论不只对纯 \(p\) 幂成立。
若正整数 \(N=p^e a\)、\(e\ge1\)、\(p\nmid a\)，则
\[
\boxed{\operatorname{rad}_z(B^N)=R_E,\qquad
 B^N\notin\mathbf C_p\langle z/R_E\rangle.}
\tag{22}
\]
例如可将 \(B^a\) 代入 (2)，原数据变为
\((ma,\alpha a,\beta a,Q^a,da)\)；
其中 \(ma\) 仍为单位、\(Q^a\) 仍是常数一整级数，
上述定理逐项适用。这里的正整数假设保证 \(da\ge0\)。

R625/R627 的有限首坏窗随 \(e\) 线性后移，与 (1) 完全兼容。
那个结论只在给定有限系数区间中支付整性；
本篇证明无穷尾在原 \(z\) 闭边界仍不属于 Tate 代数。
\(u\) 参数中某些因子延伸更远，也不构成原 \(z\) 参数的反例：
真实形式对数在边界有 (8) 的多个零点，闭边界形式逆不存在。

任何把这些幂放回原多项式来源格的用途，仍须支付实际次数
\(N\)，原 \(S/T\) 的共同零阶 \(N\)，以及全部原帽、普通成本
和惰性旗标成本。该半径结论不依赖 \(j=0\)，因此它不能被
算作中央失败时新增的独立代数约束。
原固定曲线的无穷素数目标仍须处理完整中央或等价全局算术条件。

## 依赖与继续位置

- [R632](R632-original-pth-power-formal-group-boundary-and-full-kummer-range.md)：
  原 \(B^p\) 的上下界、完整 \(\mathscr L\) 分母、原正向闭盘代换
  与严格内盘逆。本篇 §§2–4 明写全部新边界比较。
- [R619](R619-original-cartier-sparse-rows-and-second-newton-block.md)、
  [R630](R630-original-full-division-corrections-and-first-nonlinear-unit.md)：
  同一原 \(H_L\) 的准确进位端点 \(pH_L=-1\bmod p\)。
- [R625](R625-original-theta-powers-integral-window-and-first-bad-coefficient.md)、
  [R627](R627-original-theta-power-first-bad-band-and-unit-two-source-prefix.md)：
  有限整窗、完整首坏带和实际原幂的来源成本。

下一条原接口是完整中央连接在 \(R_E\) 以内的真实解空间与全来源
成本；本篇未无证扩大 R622 中央解的范围，也未把局部边界当作
已证明的中央非消失。没有新增有限素数扫描。
