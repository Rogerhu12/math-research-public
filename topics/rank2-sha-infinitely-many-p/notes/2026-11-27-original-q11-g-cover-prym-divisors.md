# 原 q=11 谱平方根的完整除子和固定 Prym 双 Norm

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

本文准备消费已经公开得到的原 R1036 截面及其
[准确两覆盖平方根](2026-11-27-original-q11-two-cover-lift-and-frobenius-line.md)，
求该实际函数 R 的完整零极除子，以及
[R1039](../results/R1039-original-g-cover-prym-boundary-and-frobenius.md)(22)
的真实 Prym Norm 除子。没有重新枚举任何 D，也不重新求平方根。

源码为
[scripts/consume-original-q11-prym-norm-divisors.py](../scripts/consume-original-q11-prym-norm-divisors.py)。
截至本稿写成，仅作静态审读；尚未把未执行结果称为成功。
实际公开执行回执及所得必要除子随后在本文登记。

## 1. 唯一原输入及其方向

实时输入固定为：

- run45972624090、job140416498782；
- source c5020fcd7f026ef21d4b69735b3a47b56148d258；
- request_id 2026-11-27-0918-original-q11-two-cover-lift；
- 原源码 SHA256
  812fd5e5a8899e2b47095c2eee50e22ba5b7063397121a0e44ec8801d1fe3b43；
- 完整 stdout2484字节、SHA256
  b1341ed2e07961af591c0f967d660a236a53cb8a25c492439654ccad34fb510d；
- 实际坐标摘要
  3afbc5db78bf933d28788ea282eeae2d19211a8184e3670dedd2eccbf1765a68。

程序实时读取原 run、job 和日志，同时核源、请求、源码和完整 stdout
的原始身份；不把原输出 JSON 缓存进源码或数据文件。
原程序为返回 R1031 的 W 而整体翻转一次的 R 被原样消费，
没有再取反号、重求根或改变 δ。

旧 helper 只导入已付有理函数类及原回执读取器，
不调用其 main。导入前核其完整源码摘要。
整个入口在命名的公开 Actions guard 之后才构造有限域多项式。
缺失或不符的公开回执是执行错误，不是新的数学阴性结果。

## 2. 双 Norm 在原 $-3$ 扭曲上的准确下降

仍取
$$
 C:w^2=(z^3-4)(z^3-16),\quad a=5\in\mathbf F_{11},\quad
 g=z^2+az+a^2,
$$
$$
 X=-\frac{3z}{z^3-4},\quad D=z-2X,\quad K=z^3-4,
 \qquad R=A(z)+B(z)w.
\tag{1}
$$
R1039 的原二盖为 $s^2=g$；置 $W_L=w/s$，
其真正椭圆商及模型为
$$
 W_L^2=(z-a)(z^3-16),\qquad
 x_L=\frac{z-4a}{z-a},\quad
 y_L=-\frac{3W_L}{(z-a)^2}.
\tag{2}
$$
因此 $E_L:y_L^2=x_L^3-12x_L+20$。

保持 $\delta^2=-3$，R1039(22)准确写为
$$
 N_Q=U(z)+V(z)Z,\qquad Z=\delta W_L,
\tag{3}
$$
$$
 U=-\frac1K-\frac{g(A^2-K(z^3-16)B^2)}{D^2},
 \qquad
 V=\frac{g}{3D}\left(B+\frac A K\right),
$$
$$
 Z^2=-3(z-a)(z^3-16).
\tag{4}
$$
所有 U、V 的系数在 $\mathbf F_{11}$。
这表明 N_Q 在 $E_L$ 上带有实际 δ 系数，
而在准确的 $-3$ 二次扭曲上是 $\mathbf F_{11}$ 有理函数。
不能删去 δ 再称它为原 $E_L/\mathbf F_{11}$ 上的函数。

取标准 Weierstrass 坐标
$$
 X_T=-3x_L,\qquad Y_T=-3\delta y_L.
$$
直接平方得到
$$
 \boxed{E_T:\ Y_T^2=X_T^3-108X_T-540.}
\tag{5}
$$
其反向原参数为
$$
 \boxed{
 z=a\frac{X_T+12}{X_T+3},\qquad
 Z=\frac{9a^2Y_T}{(X_T+3)^2}.
 }
\tag{6}
$$
(2)、(5)、(6)是固定同一个函数域的双向等式，
不是只比较 j 不变量。q=11 时(5)为
$Y_T^2=X_T^3+2X_T+10$。
z=a 的原分歧点准确延拓到(5)的 O；原 z=∞ 两点则由(6)
作为相应的 $X_T=-3$ 有限点保留，不在变坐标时删去。

程序将(3)用(6)得到
$$
 N_Q=A_T(X_T)+B_T(X_T)Y_T.
\tag{7}
$$
同时只由已经付出的 R 和原恒等式返回
$$
 x=-\frac{gR^2}{3D^2}
   -\left(\frac{1-w/K}{6}\right)^2.
$$
新双 Norm 的完整核对是
$$
 \boxed{
 A_T^2-(X_T^3-108X_T-540)B_T^2
 =9\,\operatorname{Nm}_{C/\mathbf P^1_z}(x)
       \bigg|_{z=a(X_T+12)/(X_T+3)}.
 }
\tag{8}
$$
这正是 R1039(23)，保留完整函数和所有极点重数。

## 3. 有限处的完整除子算法

本节统一处理 $y^2=P(T)$ 上的非零函数
$F=A(T)+B(T)y$，其中 P 平方自由。
将 A、B 通分，提取两分子的最大公因子，唯一写成
$$
 F=\frac{c(T)}{d(T)}\bigl(a(T)+b(T)y\bigr),
 \qquad \gcd(c,d)=1,\quad\gcd(a,b)=1.
\tag{9}
$$
分母首一；非零常数无关除子。
记
$$
 H(T)=a(T)^2-P(T)b(T)^2.
\tag{10}
$$
H 非零，因为 P 非平方。
对 c、d、H 作完全不可约因式分解。
对每一个不可约因子 h，置
$$
 e=v_h(c)-v_h(d),\qquad n=v_h(H).
\tag{11}
$$
由此给出整个光滑射影曲线上的有限处重数，规则如下。

若 h 整除 P，h 上只有一个分歧点。
局部 h 的阶为2，y 为均匀化参数。
因 $\gcd(a,b)=1$，若 n>0，则 a 被 h 整除而 b 是单位，
于是(10)的阶准确为1。故 n 只能0或1，
该分歧点处
$$
 \operatorname{ord}(F)=2e+n.
\tag{12}
$$
这里没有把分歧点错误地当作两条不同的约化支。

若 h 不整除 P 且 n>0，则 b 模 h 可逆。
准确的一条零支由
$$
 y\equiv-a/b\pmod h
\tag{13}
$$
给出，另支取相反数。
两支的函数阶分别为
$$
 e+n,\qquad e.
\tag{14}
$$
这是因为其乘积是(10)，而另一支的原始因子值为非零。
h 可以有任意次数；(13)在完整剩余域中定义，
不要求 h 有 $\mathbf F_{11}$ 根。
n 保留原指数，因而包含所有厚零和厚极。

若 h 不整除 P 且 n=0，两个几何支的阶都为 e。
程序以“h 的整个未分歧逆像”输出这个完整 Cartier 除子，
次数为 $2\deg h$、重数 e。
它既可为两个闭点，也可为一个剩余次数加倍的闭点；
因为权在整个逆像上相同，无需任选一个平方根来拆开。
这不是遗漏某个支，更不是把该逆像只按一个点计数。

(12)–(14)及整个逆像已穷尽有限处。
若其中总重数为0，该项只在整理后消去，
不会在计算前因分母或分支例外而跳过。

## 4. 原 C 的两个无穷点和扭曲椭圆曲线的 O

原 C 的 P 为首一六次，两个原无穷点以 $w/T^3\to\pm1$ 标记。
对(9)的原始部分，记
$d_a=\deg a$、$d_b=\deg b+3$。
若两数不同，两支的阶都是 $-\max(d_a,d_b)$。
若相等 d，则最多一支的首项会相消。
不相消支的阶为 −d，而两支阶之和是
$-\deg H$，故相消支的准确阶为
$$
 d-\deg H.
\tag{15}
$$
再对两支分别加 $\deg d-\deg c$。
所以算法用真实 Norm 计算全部高阶相消，不截断展开、
不假设首次首项测试足够，也不丢掉 R 在原一支无穷点上的零。

(5)是三次 Weierstrass 模型，只有 O 一个无穷点。
$\operatorname{ord}_O X_T=-2$、
$\operatorname{ord}_O Y_T=-3$。
因此(7)的两项如果都非零，其阶一偶一奇，不能相消：
$$
 \operatorname{ord}_O(N_Q)=
 \min\bigl\{
 2(\deg\operatorname{den}A_T-\deg\operatorname{num}A_T),\
 2(\deg\operatorname{den}B_T-\deg\operatorname{num}B_T)-3
 \bigr\}.
\tag{16}
$$
零项忽略。有限处和无穷处合起来，正负除子次数须相等；
程序输出它们以及每个不可约因子、原支和完整重数。

## 5. 新 Norm 的真实 Picard 类

仅在(5)上，将所得零除子与极除子各自归约到
$E_T=\operatorname{Pic}^0(E_T)$，
取 O 为准确原点。
整个未分歧逆像 h=0 相对 $2\deg h\cdot O$ 的类为0；
分歧点和(13)的指定支必须保留。

对半约化除子对 $(u,v)$，采用
$u\mid(v^2-P)$、对应支 $y=v$。
若两个对为 $(u_1,v_1),(u_2,v_2)$，
令 Bézout 多项式满足
$$
 d_1=e_1u_1+e_2u_2=\gcd(u_1,u_2),
$$
$$
 d=c_1d_1+c_2(v_1+v_2)
   =\gcd(d_1,v_1+v_2).
$$
置 $s_1=c_1e_1,s_2=c_1e_2,s_3=c_2$，则合成对为
$$
 u=\frac{u_1u_2}{d^2},\qquad
 v=\frac{s_1u_1v_2+s_2u_2v_1+
                s_3(v_1v_2+P)}d \pmod u.
\tag{17}
$$
共同的相反支已由 d 消去；此式也覆盖分歧二挠的重叠。
分子可被 d 整除，且 $u\mid(v^2-P)$，
均直接由 Bézout 式和原两个对的关系得到。
它是除子相加的标准函数域恒等式，不在有限点表上猜群律。

若 $\deg u>1$，用
$$
 u_{\rm new}=(P-v^2)/u\quad\text{首一化},\qquad
 v_{\rm new}=-v\pmod {u_{\rm new}}
\tag{18}
$$
归约。其意义是对 $y-v$ 取完整主除子，
将余下交点取负。三次模型保证次数严格下降，直到
$(1,0)$ 或 $u=T-x_0,v=y_0$。
原除子的每个正重数按此群律保留，使用整数倍而非只取奇偶；
整个未分歧逆像确实贡献0。
对零、极两有效除子分别做(17)–(18)，
所得点应相同，因为差是完整主除子 $\operatorname{div}(N_Q)$。

这个公共点是本次新计算要读出的实际 Picard 类，
程序不先假设它为 O、固定边界 P 的倍数或任何旧核类。
它也不将两个相等类本身当作新的原27对非零证据。

## 6. 范围

本入口将给出实际 R 的完整除子、(7)的必要函数坐标、
N_Q 的完整零极除子和该实际有效除子的 Picard 类。
它消费已付原点，不重做原三次域的求根或高度枚举。
在原曲线与原二次扭曲之间保留(5)–(6)，
并由(8)保留实际 Norm 符号和全部厚点。

即便此新分解成功，也仅支付这个固定 q=11 函数的结构。
q=11 的原 full-eta/Cor shadow 在倒6后仍为零；
一般 q 的原两 quadric 点、27对有权评价与普通 p 的局部最高
非零都没有由一个新的有效除子类自动得到。


公开请求：2026-11-27-1015-original-q11-prym-norm-divisors；python-flint 0.9.0，无脚本参数；源码13363字节，SHA256 732332d88af3b58952a998c34c46728c9771838a58640264644cade0176622ea。入口保持既有 small workflow 的15分钟帽和单JSON完整stdout，原重型v11不改。本次尚待实际运行回执。
