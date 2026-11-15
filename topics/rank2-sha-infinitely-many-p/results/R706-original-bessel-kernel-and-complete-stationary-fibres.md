# R706 — 原 wild torus 的绝对 Bessel 核、全例外与驻点公式

日期：2026-11-15。**状态：以下原角色参数、完整 Schrödinger 核、
全部例外纤维及精确驻点公式已证明。尚未由此得到原固定 theta
短块的幂次节省或原迹非零。**

R705 已将同一个原全迹识别为 $p^2$ 层 Weil 表示的单重
wild torus 投影。本篇把该投影写成完整的局部 Bessel 核：
Cayley 参数中的每个主单位纤维准确求和，两个不能用
Cayley-unit 公式覆盖的纤维也分别保留。
原相位没有改成一个任选的模 $p$ 提升。

## 1. 固定原角色与标准 Schrödinger 模型

沿用
$$
p=6s-1>101,\quad d=p+1,\quad
R=\mathbf Z[\omega]/p^2,\quad
m=34\ \text{或}\ 72,\quad r\in\mathbf F_p^\times.
$$
对 $v\in R^\times$，
$$
q_p(v)=\frac{v^p/\bar v-1}{p}\pmod p,\qquad
\chi_r(v)=e_p\!\left(\frac{mr}{2\delta}
                     (q_p(v)-\overline{q_p(v)})\right).
\tag{1}
$$
这里及以下的 $\chi_r$ 就是 R705 的 $\chi_{m,r}$。
令
$$
\mathcal T=\ker(N:R^\times\to(\mathbf Z/p^2)^\times),\qquad
\theta_r=\chi_r|_{\mathcal T}.
$$
它在 Teichmüller Hall 群上恒为 1，且
$$
\theta_r(1+p\delta t)=e_p(mrt).
\tag{2}
$$

使用 $\mathscr H=\mathbf C^{\mathbf Z/p^2}$ 的标准内积
$\sum_n f(n)\overline{g(n)}$，Heisenberg 算子为
$$
\boxed{
(\mathsf D_{(x,y)}f)(n)
=e_{p^2}(-my(n+x/2))f(n+x).
}
\tag{3}
$$
这是与 R705(20) 同一中心字符的模型。
其绝对 Weil 归一固定支持于 $p\mathbf Z/p^2$、
取值 $p^{-1/2}$ 的旧一维向量。

为明确与原样本的相位一致，若 $A\in\mathcal V_m$，则逆 Zak 为
$$
\boxed{
(\mathcal ZA)(a+pk)=
 \frac1{\sqrt p}\sum_{b\bmod p}
 A(a+b\omega)e_{p^2}(mab/2)e_p(mbk),
\quad 0\le a<p.
}
\tag{4}
$$
(4) 是酉同构，运输 R705 的 Heisenberg 算子到 (3)。
它也运输固定旧一维向量，因此没有残留可自由选择的
Weil 根单位。R704 使用同一变换分析原固定 theta 的短块。

R705 的归一 torus 向量于是成为
$$
\boxed{
\psi_r(a+pk)=
 \frac1{\sqrt{p(p+1)}}
 \sum_{\substack{b\bmod p\\a^2-ab+b^2=r}}
   \chi_r(a+b\omega)^{-1}
   e_{p^2}(mab/2)e_p(mbk).
}
\tag{5}
$$
所取 $a,b$ 代表与 R703/R704 一致，整个相位一同运输。
该向量范数为 1，真实角色为 $\theta_r$。
特别地
$$
|\psi_r(n)|\le\frac2{\sqrt{p(p+1)}}.
\tag{6}
$$
若 $4r-3a^2$ 为非平方，则 $\psi_r(a+pk)=0$；
若为零，(5) 只有一个根，不能仍按两个不同根计算。

## 2. 任意上右角单位的绝对 Weil kernel

写
$$
g=\begin{pmatrix}a&b\\c&d_0\end{pmatrix}
 \in\operatorname{SL}_2(\mathbf Z/p^2),\qquad b\in(\mathbf Z/p^2)^\times.
$$
在 (3) 的规范下，
$$
\boxed{
(\mathsf W(g)f)(n)
 =\frac1p\sum_{n'\bmod p^2}
 e_{p^2}\!\left(
 \frac{m}{2b}(d_0n^2-2nn'+an'^2)\right)f(n').
}
\tag{7}
$$
(7) 的绝对常数为 $+1/p$，不是一个未定 Gauss 根单位。

证明可以直接用 (3)：
显示核严格交织
$\mathsf W(g)\mathsf D_t=\mathsf D_{gt}\mathsf W(g)$；
有限 Fourier 正交性给其酉性。
不可约性使它至多相差一个公共标量。
把支持于 $p\mathbf Z/p^2$ 的旧向量代入，
内层完整 $p$ 项只在 $p\mid n$ 时存活，
输出准确仍为该向量，故标量就是 (7)。
这同时与 R705 的绝对模型一致。

## 3. Cayley 参数及完整 Bessel 相位

对 $t\in\mathbf Z/p^2$ 置
$$
h(t)=\frac{1+\delta t}{1-\delta t}\in\mathcal T.
\tag{8}
$$
因为 $-3$ 在 $\mathbf F_p$ 中非平方，$1+3t^2$ 始终为单位。
乘法 $h(t)=a+b\omega$ 在 $(1,\omega)$ 基上的矩阵是
$$
\begin{pmatrix}a&-b\\ b&a-b\end{pmatrix},
\quad
a=\frac{1+2t-3t^2}{1+3t^2},\qquad
b=\frac{4t}{1+3t^2}.
\tag{9}
$$
所以当 $t\bmod p\ne0$ 时，(7) 给
$$
\boxed{
\mathsf W(h(t))(n,n')
 =\frac1p e_{p^2}\!\left(
 \frac m4(n^2-n'^2)
 +\frac{3m}{8}t(n+n')^2
 -\frac{m}{8t}(n-n')^2\right).
}
\tag{10}
$$
这已经是同一个角色的局部 Bessel 形式：
加法相位具有 $At+B/t$ 的标准形状，
乘法权仍是准确的 $\theta_r(h(t))^{-1}$。

全 $\mathcal T$ 并不都由 $t$ 为单位的 (10) 覆盖。
其准确不交分区为
$$
\boxed{
\mathcal T=
 \mathcal U\ \sqcup\ (-\mathcal U)\
 \sqcup\{h(t):t\bmod p\ne0\},
\qquad
\mathcal U=\{1+p\delta z:z\in\mathbf F_p\}.
}
\tag{11}
$$
$t\equiv0\bmod p$ 覆盖 $\mathcal U$，
Cayley 分母 $h+1$ 不可逆的另外 $p$ 个点是 $-\mathcal U$。
两组都不能删除。

## 4. 全主单位纤维的精确驻点求和

设 $t_0\bmod p$ 为非零。
从 (8) 直接微分，或在有限环中展开，得到
$$
\frac{h(t_0+pz)}{h(t_0)}
 =1+\frac{2p\delta z}{1+3t_0^2}\pmod{p^2}.
$$
因此原角色满足
$$
\boxed{
\frac{\theta_r(h(t_0+pz))}{\theta_r(h(t_0))}
 =e_p\!\left(\frac{2mrz}{1+3t_0^2}\right).
}
\tag{12}
$$

置
$$
A=\frac{3m}{8}(n+n')^2,\qquad
B=-\frac m8(n-n')^2.
$$
在完整 $p$ 项纤维上，
$\theta_r(h(t))^{-1}e_{p^2}(At+B/t)$
的变化因子为
$$
e_p\!\left[
z\left(A-\frac B{t_0^2}
             -\frac{2mr}{1+3t_0^2}\right)\right].
$$
故整个纤维和恰为零，或恰为 $p$ 倍任一项。
它存活的充要条件是
$$
\boxed{
F_{r;n,n'}(t_0)=0\bmod p,
}
\tag{13}
$$
其中
$$
\boxed{
F_{r;n,n'}(T)=
9(n+n')^2T^4+
 \bigl(6(n^2+n'^2)-16r\bigr)T^2+
 (n-n')^2.
}
\tag{14}
$$
这里 $n,n'$ 在 (14) 中约化模 $p$，
但存活项的相位仍在模 $p^2$ 中评价。

若 (13) 成立，则
$$
\theta_r(h(\widetilde t_0))^{-1}
 e_{p^2}(A\widetilde t_0+B/\widetilde t_0)
\tag{15}
$$
与 $\widetilde t_0\bmod p^2$ 的提升无关。
这是由 (12) 和同一个驻点方程证明的，
不是任意改变原相位。
驻点为重根时，完整纤维仍恰有 $p$ 项；
本层没有凭 Hessian 另添或删掉平方根因子。

(14) 永不为零多项式。
若它恒零，常数项先迫 $n=n'$，最高项再迫 $n=0$，
中间项则为 $-16r\ne0$，矛盾。
所以单位驻点至多四个。

将 (14) 看成 $T^2$ 的二次式，其判别式准确为
$$
\boxed{
16(4r-3n^2)(4r-3n'^2).
}
\tag{16}
$$
(16) 与 (5) 的两个原 norm-circle 判别式一致；
不能只从乘积为平方就忽略各个坐标是否真的存在。

## 5. 两组例外纤维的完整 kernel

令 $\mathsf P_{\mathcal U,r}$ 为主单位 $\mathcal U$ 上角色
$e_p(mrz)$ 的正交投影。
在 (4) 的坐标中，主单位联合特征由
$(a,b)\bmod p$ 的 $a^2-ab+b^2$ 标记。
故
$$
\boxed{
\mathsf P_{\mathcal U,r}(n,n')
 =
\begin{cases}
\displaystyle
\frac1p
 \sum_{\substack{b\bmod p\\a^2-ab+b^2=r}}
 e_p\!\left(mb\,\frac{n-n'}p\right),
 &n\equiv n'\equiv a\bmod p,\\[2mm]
0,&n\not\equiv n'\bmod p.
\end{cases}}
\tag{17}
$$
当 $n\equiv n'$ 时，(17) 中的商 $(n-n')/p$ 为真实整数模 $p$；
共同 Zak 相位在这一纤维内准确相消。

在绝对归一中 $\mathsf W(-I)f(n)=f(-n)$。
又 $\theta_r(-1)=1$，所以 $-\mathcal U$ 的贡献是
$\mathsf P_{\mathcal U,r}(-n,n')$。
它没有被并入普通的 $t^{-1}$ 公式。

## 6. 完整 rank-one Bessel 核

原 $\theta_r$ 投影是
$$
\mathsf P_r
 =\frac1{p(p+1)}\sum_{h\in\mathcal T}
                       \theta_r(h)^{-1}\mathsf W(h).
$$
结合 (10)–(17)，得到全公式
$$
\boxed{
\begin{aligned}
\mathsf P_r(n,n')
={}&\frac{
 \mathsf P_{\mathcal U,r}(n,n')
 +\mathsf P_{\mathcal U,r}(-n,n')}{p+1}\\
&+\frac{e_{p^2}(m(n^2-n'^2)/4)}{p(p+1)}
 \sum_{\substack{t_0\in\mathbf F_p^\times\\
                 F_{r;n,n'}(t_0)=0}}
 \theta_r(h(\widetilde t_0))^{-1}
 e_{p^2}(A\widetilde t_0+B/\widetilde t_0).
\end{aligned}}
\tag{18}
$$
(18) 保全部 $p^2$ 相位、两个例外纤维和可能的重根。
由 R705 的单重性，它同时严格等于
$$
\boxed{\mathsf P_r(n,n')=\psi_r(n)\overline{\psi_r(n')}.}
\tag{19}
$$
所以本篇的 Bessel 核正是原 R703/R704 的那条向量，
并非某个有相似角型但不同 tame/wild 角色的向量。

例如 $n=n'=0$ 时单位驻点不存在；
全部答案来自 (17) 的两组例外。
若 $r$ 为非平方则答案为零；
若 $r$ 为非零平方则答案为 $4/[p(p+1)]$。
删掉 $\pm\mathcal U$ 会把这一实际原 kernel 错改为零。

由 (5) 或 (18)–(19) 得
$$
|\mathsf P_r(n,n')|\le\frac4{p(p+1)}.
\tag{20}
$$
这恢复准确的全向量上确界 (6)，
没有把一个完整 projector 的界冒认为短块和的界。

## 7. 同一向量的真实 Heisenberg 自相关

还有一条不需任何指数和定理的完整矩阵系数界。
令 $g_r=G_r/\sqrt{p+1}$ 为 R705 的原归一向量。
若 $t\bmod p\ne0$，则
$$
\boxed{
|\langle g_r,\mathsf D_tg_r\rangle|
 \le\frac2{p+1}.
}
\tag{21}
$$
证明中所有相位都保留，只对存活项取绝对值：
两个支撑条件为
$$
N(v)=r,\qquad N(v+t)=r.
$$
两式相减是一条非零仿射直线。
因范数形式在 $\mathbf F_p$ 各向异性，
这条线与光滑范数圆至多相交两点。
每个项的模为 $1/(p+1)$，即得 (21)。

若 $t=p\ell$，则支撑不减少，而准确是
$$
\boxed{
\langle g_r,\mathsf D_{p\ell}g_r\rangle
 =\frac1{p+1}\sum_{Nv=r}e_p(-m[\ell,v]).
}
\tag{22}
$$
(22) 才是没有 wild 提升相位的有限域 conic 和。
不能将 (22) 对角观测的简单结构，直接用到
R703 的线性 toric period；原问题是
$\langle A_m,G_r\rangle$，而不是 (21)–(22) 这些自相关。

## 8. 对原固定 theta 权的准确意义

R704 的 Zak 展开把 R703 原和转为该同一 $\psi_r$ 的短块，
其固定平滑系数及总变差均保留。
本篇现在额外支付了：

- 该向量在标准 Schrödinger 模型中的绝对中心与 tame/wild 参数；
- 它作为局部 Bessel kernel 的完整表达；
- 所有 $t\equiv0$、$h\equiv-1$ 的例外；
- 每个模 $p^2$ 主单位纤维的准确驻点方程及绝对系数；
- 两圆交给出的真实 Heisenberg 自相关界。

单独由 (6)，长度至多 $p$ 的未归一短块仍只得 $O(p)$。
(18) 把完整 projector 化成至多四个驻点，
但其 $n$ 方向的存活相位仍保留原 $\theta_r$ 的 $p^2$ 数据。
未证明它们在指定短块中有统一幂次消去。
同样，(21) 的全空间自相关不是在原短块内的受限自相关。

因此本篇不声明新的原中央零、不声明原全迹非零，
也不把原固定 $A_m$ 换成任选基向量。
若可用一个实际短块/toric period 定理，
其角色、中心、例外及归一现在均已确定；
所得收益可按 R704/R703/R700 返回同一个原边界。

## 依赖

- [R703](R703-original-hall-phase-and-finite-fourier-return.md)：
  原 $p^2$ Hall 相位与固定 theta 样本。
- [R705](R705-original-wild-character-and-absolute-weil-projection.md)：
  完整 wild 角色、原根域次数、绝对 Weil 模型及单重性。
- R704：同一 Zak 变换与原固定 theta 的短块返回。

本篇为完整有限公式的证明，没有数值扫描、未执行的复核门，
也没有新增可重算数据文件。
