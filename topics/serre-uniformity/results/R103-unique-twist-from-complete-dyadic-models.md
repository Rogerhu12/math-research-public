# R103：III 偶立方分支的完整二进选择，四条参考曲线缩成唯一一条

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明的全参数必要条件，含有限精确数域计算。** 本文接续 [R99](R99-cube-even-branch-multifrey-and-four-fixed-curves.md)。对每个实际奇数参数 $a,b$，给出 R99 中唯一可能的扭曲因子 $d$。没有把“在同一个扩张上好约化”当作模 $p$ 同构的充分条件，也没有排除这唯一候选。

## 1. 唯一必要扭曲

沿用 R99 的全部实际假设，特别是
$$
a,b>0\text{ 奇},\quad (a,b)=1,\quad3\nmid a,\quad3\mid b,
\quad h=(a^2+3b^2)/2,\quad a^4-3h^2=Y^p,
$$
以及 $p>37$、$p\equiv3\pmod4$ 和原 $E[p]\simeq A[p]$。置
$$
K=\mathbb Q(r),\quad r^2=3,\qquad
B=B(a,h):y^2=x^3+4ax^2+2(a^2+rh)x,
$$
$$
B_0:y^2=x^3+4x^2+(2+r)x.
$$
R99 已证明存在 $d\in\{1,-1,2,-2\}$，使 $B[p]\simeq B_0^{(d)}[p]$。

**定理 103.1。** 此 $d$ 只能是
$$
\boxed{d=\left(\frac a3\right)(-2)^e,\qquad
e\in\{0,1\},\qquad
(-1)^e=\left(\frac2{ab}\right).}
\tag{103.1}
$$
第二个符号为奇分母的 Jacobi 符号。等价地，先用
$$
\begin{array}{c|c}
a^2\equiv b^2\pmod{16}&d\in\{1,-1\}\\
a^2\not\equiv b^2\pmod{16}&d\in\{2,-2\}
\end{array}
\tag{103.2}
$$
选择奇偶，再由
$$d\equiv a\pmod3\tag{103.3}$$
选择符号。

(103.1) 对任意奇参数都指定一个候选，所以它本身不是无解定理。以下完整证明 (103.2)，不把有限样本外推为局部分类。

## 2. 两个明确的三挠点域

以下数域只用于 $2$ 处的惯性比较，不与 R19 的虚二次域或 R46 的三次覆盖混同。

$B_0$ 的三除法多项式为
$$
\psi_3(x)=3x^4+16x^3+6(2+r)x^2-(2+r)^2.
$$
令 $z=3x_0$，则
$$
z^4+16z^3+18(2+r)z^2-27(2+r)^2=0.
\tag{103.4}
$$
置 $H_0=K(z)$，$x_0=z/3$，以及
$$f_0=x_0^3+4x_0^2+(2+r)x_0.$$
对 $\delta=1,2$ 定义
$$
L_\delta=H_0(w_\delta),\qquad w_\delta^2=81\delta f_0.
\tag{103.5}
$$
那么
$$
P_\delta=(\delta x_0,\delta w_\delta/9)\in B_0^{(\delta)}(L_\delta)
$$
是一个非零三挠点：直接代入曲线方程得到右端 $\delta^3f_0$，而 (103.4) 正是非零三挠横坐标条件。

精确数域计算证明 (103.4) 在 $K$ 上不可约、(103.5) 在 $H_0$ 上不可约。绝对多项式可取
$$
\begin{aligned}
P_{H_0}(t)={}&t^8+32t^7+328t^6+1152t^5-54t^4\\
&-6048t^3-1944t^2+729,
\end{aligned}
\tag{103.6}
$$
$$
\begin{aligned}
P_{L_1}(t)={}&t^{16}+2688t^{14}-503136t^{12}-184757760t^{10}\\
&-51018336t^8-1008938612736t^6\\
&+1785233613312t^4+650717652052224,
\end{aligned}
\tag{103.7}
$$
而
$$P_{L_2}(t)=2^8P_{L_1}(t/\sqrt2).\tag{103.8}$$
后一表达式的全部系数均为整数；证书同时列出展开式。嵌入 $K\hookrightarrow H_0\hookrightarrow L_\delta$ 由 (103.4)–(103.5) 固定，程序保留这些嵌入，不只比较没有标记的绝对定义多项式。

二者的域判别式为
$$
D_{H_0}=2^{16}3^{10},\qquad
D_{L_1}=D_{L_2}=2^{48}3^{20}.
\tag{103.9}
$$
在每个 $L_\delta$ 中 $2$ 上方只有一个素理想 $\mathfrak P_\delta$，其绝对分歧指数和剩余次数为
$$
e(\mathfrak P_\delta/2)=8,\qquad
f(\mathfrak P_\delta/2)=2.
\tag{103.10}
$$
因此相对于 $K_{\mathfrak p_2}/\mathbb Q_2$，局部分歧指数是 $4$，不是 $8$。

直接对 $B_0^{(\delta)}$ 在这个素理想运行 Tate 算法，准确导子指数为零，即
$$B_0^{(\delta)}\text{ 在 }L_{\delta,\mathfrak P_\delta}\text{ 好约化。}\tag{103.11}$$
这里实际核验了 (103.11)；没有使用“添一个三挠点总会得到好约化”这样的错误通则。

## 3. 所有奇数 $a$ 在这两个局部域中都是平方

令 $\mathscr L_\delta=L_{\delta,\mathfrak P_\delta}$，令 $v$ 为其归一化整数赋值，所以 $v(2)=8$。

$\mathscr L_\delta$ 包含 $\mathbb Q_2(\sqrt3)$。其绝对剩余次数为二，所以也包含唯一的非平凡未分歧二次扩张 $\mathbb Q_2(\sqrt5)$。有理奇二进单位的平方类由 $3,5$ 生成：模 $8$ 的四个单位类为 $1,3,5,7$，而 $3\cdot5\equiv7\pmod8$。因此
$$\mathbb Z_2^\times\subset\mathscr L_\delta^{\times2}.\tag{103.12}$$
特别地，$a$ 与 $-1$ 在两个局部域中都是平方。

令
$$t=b/a\in\mathbb Z_2^\times,\qquad
H=h/a^2=\frac{1+3t^2}{2}\in2+4\mathbb Z_2.$$
由扭曲约定，有
$$B(a,h)=B(1,H)^{(a)},\qquad
B(1,H):y^2=x^3+4x^2+2(1+rH)x.$$
由 (103.12)，在 $\mathscr L_\delta$ 中这个扭曲平凡。故只需对全部
$$H\equiv2\text{ 或 }6\pmod8\tag{103.13}$$
判定 $B(1,H)$ 的好约化。

## 4. 四个精确最小模型和无界参数的稳定性

对 $\delta=1,2$ 及 $H_*=2,6$，Tate 算法给出以下完整数据。换元按通常约定记为
$$
x=U^2x'+R,\qquad y=U^3y'+SU^2x'+T.
\tag{103.14}
$$

| $\delta$ | $H_*$ | 型 | 导子指数 | $v(\Delta_{\min})$ | $(v(U),v(R),v(S),v(T))$ | $(v(a'_1),v(a'_2),v(a'_3),v(a'_4),v(a'_6))$ |
|---:|---:|---|---:|---:|---|---|
| 1 | 2 | 好 | 0 | 0 | $(6,4,2,10)$ | $(4,0,0,0,2)$ |
| 1 | 6 | II$^*$ | 4 | 12 | $(5,4,2,10)$ | $(5,2,3,4,5)$ |
| 2 | 2 | II$^*$ | 4 | 12 | $(5,4,2,10)$ | $(5,3,3,6,5)$ |
| 2 | 6 | 好 | 0 | 0 | $(6,4,2,10)$ | $(4,1,0,2,0)$ |

所有赋值都在同一 $\mathscr L_\delta$ 的整数归一化下；没有把 $\mathbb Q_2$、$K_{\mathfrak p_2}$、$\mathscr L_\delta$ 的归一化混用。

现令 $H=H_*+8z$，其中 $z\in\mathbb Z_2$ 任意。原模型只改变 $a_4$，其改变量为
$$\eta=2r(H-H_*),\qquad v(\eta)\ge32.$$
把**同一个**换元 (103.14) 用到新模型，则
$$
\delta a'_4=\eta/U^4,\qquad
\delta a'_6=R\eta/U^6,
\tag{103.15}
$$
其余 $a'_i$ 不变。

### 4.1 好约化的两个分支

此时 $v(U)=6,v(R)=4$，所以
$$v(\delta a'_4)\ge8,\qquad v(\delta a'_6)\ge0.$$
因此新模型仍整。对任意偶数 $H$，
$$
\Delta(B(1,H))=512(1+rH)^2(1-rH),\qquad
v(\Delta)=72.
$$
同一换元除去 $U^{12}$，其赋值恰为 $72$，故新整模型的判别式仍为单位。于是整条剩余类 $H_*+8\mathbb Z_2$ 都好约化。这里允许 $a'_6$ 的单位剩余值改变；好约化由准确判别式保证。

### 4.2 II$^*$ 的两个分支

此时 $v(U)=5,v(R)=4$，所以
$$v(\delta a'_4)\ge12,\qquad v(\delta a'_6)\ge6.$$
表中的最小模型满足
$$
v(a'_1)\ge1,\quad v(a'_2)\ge2,\quad
v(a'_3)\ge3,\quad v(a'_4)\ge4,\quad v(a'_6)=5.
\tag{103.16}
$$
这些条件在改变参数后完全保留。Tate 算法依次通过加性分支的三重根和二重根步骤，并在 $v(a'_6)=5<6$ 停于 II$^*$；这是 (103.16) 的标准终止情形。在 (103.15) 下，所有已用剩余系数不变，所以同一结论覆盖整条 $H_*+8\mathbb Z_2$。

此外同一换元后的判别式赋值仍为 $72-12\cdot5=12$，II$^*$ 的九个分量由 Ogg 公式给导子 $12+1-9=4$。特别是这些分支均**不是**好约化。

因此得到完全的局部判定
$$
\begin{array}{c|cc}
& H\equiv2\pmod8&H\equiv6\pmod8\\\hline
\mathscr L_1&\text{好}&\mathrm{II}^*\\
\mathscr L_2&\mathrm{II}^*&\text{好}.
\end{array}
\tag{103.17}
$$
其无界完整性来自 (103.15)–(103.16)，不是来自多遍历几个 $a,b$。

## 5. 实际模 $p$ 同构如何强迫二进选择

若 R99 的 $d=\pm1$，则由 (103.12)，$B_0^{(d)}$ 在 $\mathscr L_1$ 与 $B_0$ 同构，故好约化。若 $d=\pm2$，同理 $B_0^{(d)}$ 在 $\mathscr L_2$ 好约化。

实际同构 $B[p]\simeq B_0^{(d)}[p]$ 限制到这些局部域，所以 $B[p]$ 的惯性作用也平凡。$B$ 潜在好约化，其有限惯性像的阶只有素因子 $2,3$。当 $p>37$，整 $p$ 进矩阵约化模 $p$ 在此有限群上忠实；于是模 $p$ 不分歧就迫使完整 $p$ 进表示不分歧，再由 Néron–Ogg–Shafarevich 得 $B$ 好约化。

结合 (103.17)，得到
$$d\text{ 奇}\Rightarrow H\equiv2\pmod8,\qquad
d\text{ 偶}\Rightarrow H\equiv6\pmod8.$$
两者是互补的，所以必且只可能按 (103.2) 选择奇偶，因为
$$
H\equiv2\pmod8
\Longleftrightarrow t^2\equiv1\pmod{16}
\Longleftrightarrow a^2\equiv b^2\pmod{16}.
$$
这证明的是 R99 同构下的必要选择。反方向的“在相同扩张上好约化”没有被用于证明两个模 $p$ 表示相同。

最后
$$
\left(\frac2{ab}\right)
=(-1)^{((a^2-1)+(b^2-1))/8}
=(-1)^{(a^2-b^2)/8}
$$
给出 (103.1) 中 $e$ 的等价写法。

## 6. $3$ 处的同一个整数迹固定符号

在 $K$ 的唯一 $3$ 上方素理想 $\mathfrak p_3=(r)$，$B$ 和四条参考都好约化，剩余域为 $\mathbb F_3$。其模型分别为
$$
B:\ y^2=x^3+\overline a x^2+2x,\qquad
B_0^{(d)}:\ y^2=x^3+\overline d x^2+2x.
$$
直接点数给
$$
a_{\mathfrak p_3}(B)=-2\left(\frac a3\right),\qquad
a_{\mathfrak p_3}(B_0^{(d)})=-2\left(\frac d3\right).
$$
$3\ne p$，实际同构使两个迹模 $p$ 相等。它们各为 $\pm2$，而 $p>37$，故必须作为整数相等。因此 $d\equiv a\pmod3$，证明 (103.3)。

每个奇偶组中恰有一个 $d$ 符合 (103.3)；由 $-2\equiv1\pmod3$，唯一值正是 (103.1)。定理得证。

## 7. 证书、范围与下一全局缺口

- [标准库 Python + 内嵌 GP 验证程序](../notes/verify_r103_dyadic_twist.py)。
- [精确数域及局部模型证书](../notes/r103_dyadic_twist_certificate.json)。

~~~sh
python3 -B topics/serre-uniformity/notes/verify_r103_dyadic_twist.py \
  --gp /tmp/pari-2.19.0/gp --check
~~~

程序从 (103.4)–(103.5) 重新构造嵌入，核验绝对不可约、$P_\delta$ 为非零三挠点、最大整环判别式及素理想分解；随后重做参考的好约化与四个最小模型。保存的是准确整数和换元赋值，不以浮点相似或无标记的域同构代替给定嵌入。PARI/GP 的整数环、素理想分解和 Tate 算法在这里均为无条件精确算法；无 GRH 或类群认证步骤。

本文依据与 R99 相同的显式曲线，所用局部标准定理为 Tate 算法、Ogg 公式和 Néron–Ogg–Shafarevich；Tate 算法的精确接口见 [PARI 官方椭圆曲线文档](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html)。全局模性、不可约及 R99 的范数筛不在这里重复。

R103 把“存在四个固定参考之一”加强成“参考由参数唯一确定”。两类模 $16$ 条件都允许实际奇数参数，符号条件也总能满足。仍需用新的全局输入排除
$$B(a,h)[p]\simeq B_0^{((a/3)(-2)^e)}[p]$$
与原 $E[p]\simeq A[p]$、精确 $p$ 次幂、原始性同时成立。单独的二进好约化域比较尚未完成这个目标。

