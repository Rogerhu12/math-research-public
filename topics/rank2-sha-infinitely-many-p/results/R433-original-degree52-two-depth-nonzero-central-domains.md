# R433 — 同一个 degree52 小核的两深度非零中央域

日期：2026-11-14。**状态：已证明。** R430 的同一个实际小核
\(\mathcal K\) 自身含有任意深的、只有两个独立深度的真实输入域，
其总和输出 \(W=Y+X\) 的 principal 中央导数严格非零。
证明使用 R426 的实际 \(F_{18}\) 移动负矩单位，以及 R429 已付的
倒 sigma 系数；不替换原曲线、周期、共享 sigma、二次权或交替来源。

这些域的 \(X\) 为单位而 \(Y\) 深，因此不是 R430 原
\(Y\)-单位条件中央的直接子域。本文保留这一域差别，不据此声称
原 \(J'_S(0)\ne0\) 或主目标完成。

## 1. 同一小核和共同归一

保持 R430、R431 的原 \(b=17\)、sigma、普通周期 \(\Omega=\Omega_p\)，
以及 R431 固定细化 ray 上的 \(p>19\)。置
\[
\delta^2=-3,\qquad d=p-1,\qquad
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad v_p(\kappa)=1.
\tag{1}
\]
写 \(F=F_{18},G=G_{18}\)。R426 给
\[
F=z^4+O(z^{10}),\qquad G=1+O(z^6),
\]
且 \(\nu_\sigma,\nu_F,\nu_G\) 的完整普通 core 都是
\[
\boxed{\nu_A|_{p\mathbf Z_p}
       =-\lambda[\kappa]_*\nu_A
       \quad(A=\sigma,F,G).}
\tag{2}
\]
这里的 sigma 标量为 \(\lambda_\sigma=\bar\pi_0^{-1}=-\lambda\)；
没有把 degree16 或 degree34 的外部标量误用于单个 sigma。

原小核准确为
\[
\boxed{\mathcal K(y,v)
=\frac23G_{16}(y)\{G(y)F(v)-F(y)G(v)\},\qquad
G_{16}(y)=\frac{\sigma(2y)\sigma(2\delta y)}{4\delta}.}
\tag{3}
\]
它仍是 R430 的 \(\mathcal S_{34}\boxtimes\mathcal S_{18}\) 来源，
且不是为了本篇构造而选择的另一个同边际联合。

## 2. 同一共享因子的原 sigma 输入和两个深度

任取整数 \(m\ge1\)，只对 (3) 的原 \(\sigma(2y)\) 作准确展开
\[
\sigma(2y)=\delta^m\sigma(2\delta^{-m}y)
                    \prod_{h=1}^m\Theta(2\delta^{-h}y),
\qquad \Theta=x\sigma^2.
\tag{4}
\]
令
\[
a_m=2\delta^{-m},\qquad b_*=2\delta,\qquad
q_h=2\delta^{-h},\qquad c_m=\delta^{m-1}/6.
\tag{5}
\]
为免与椭圆曲线参数 \(b=17\) 混淆，本节第二个 sigma 系数记作
\(b_*\)。实际隐藏输入为两个 sigma 输入 \(a,b_0\)，第一轴
\(F/G\) 输入 \(c\)，第二轴 \(F/G\) 输入 \(x\)，以及全部
\(m\) 对原 sigma 输入 \(t_{h,+},t_{h,-}\)。保留原二次权
\[
Q_m=\Omega^{-2m}\prod_{h=1}^m
\left(t_{h,+}t_{h,-}
       -\frac{t_{h,+}^2+t_{h,-}^2}{2}\right).
\tag{6}
\]
在这些相同坐标上定义同一个有符号整联合
\[
\begin{aligned}
d\mu_m={}&c_mQ_m\,d\nu_\sigma(a)d\nu_\sigma(b_0)
             \prod_{h=1}^m
               d\nu_\sigma(t_{h,+})d\nu_\sigma(t_{h,-})\\
&\quad\cdot\{d\nu_G(c)d\nu_F(x)-d\nu_F(c)d\nu_G(x)\},
\\
Y={}&c+a_ma+b_*b_0+
                 \sum_{h=1}^m q_h(t_{h,+}+t_{h,-}),\qquad X=x,
\qquad W=Y+X .
\end{aligned}
\tag{7}
\]
两条交替分支使用完全相同的输入坐标、域和二次权。由 (4) 和原
\(\Theta\) 加权双 sigma 身份，
\[
\boxed{(Y,X)_*\mu_m=\nu_{\mathcal K}.}
\tag{8}
\]
特别 \(c_m\sigma(a_my)\sigma(b_*y)\prod_h\Theta(q_hy)
=2G_{16}(y)/3\)，所以 (8) 的常数和物理尺度完全固定。

本文只使用以下两个独立深度：
\[
\boxed{\mathcal D_{m;n,r}=
\{x\in\mathbf Z_p^\times,\quad
 a,b_0,c\in p^n\mathbf Z_p,\quad
 t_{h,+},t_{h,-}\in p^r\mathbf Z_p\ (1\le h\le m)\}.}
\tag{9}
\]
取 \(n,r\ge1\)，则 \(Y\in p^{\min(n,r)}\mathbf Z_p\)，
而 \(W=Y+x\) 为单位。所有输入系数在当前素数处均为单位。
(9) 对每一对原 sigma 分别施加相同深度，不是只要求
\(\Theta\) 的相加输出深。

定义本域真正的总和输出 principal 函数
\[
J_{m;n,r}(u)=
 \int_{\mathcal D_{m;n,r}}\langle W\rangle^{du}\,d\mu_m .
\tag{10}
\]
其质量为零：两个不参与 \(Q_m\) 的 sigma 深输入 \(a,b_0\)
质量各为零。这个质量结论对两个交替分支逐项成立，不依赖它们抵消。

## 3. 保原二次权的两变量解析返回

将每对加权 sigma 暂按其完整相加输出记作 \(\nu_\Theta(z_h)\)。
定义
\[
\begin{aligned}
\Phi_m(T,U)
={}&c_md\,U^{2m}
 \int_{x\in\mathbf Z_p^\times}\int
 \log_p\left\langle
 x+T(c+a_ma+b_*b_0)+U\sum_{h=1}^m q_hz_h
 \right\rangle\\
&\quad\cdot d\nu_\sigma(a)d\nu_\sigma(b_0)
                       \prod_h d\nu_\Theta(z_h)\\
&\quad\cdot\{d\nu_G(c)d\nu_F(x)-d\nu_F(c)d\nu_G(x)\}.
\end{aligned}
\tag{11}
\]
这里 \(U^{2m}\) 是 (6) 全部原二次权的真实缩放，不能删去。

在 \((p\mathcal O)^2\) 上 log 展开一致收敛。第 \(R\ge1\) 项
分母只贡献 \(-v_p(R)\)，其余输入整有界，故足以逐项积分；
常数 \(\log_p\langle x\rangle\) 被两个 sigma 的零质量杀掉。
于是 (11) 是这一双圆盘上的完整解析函数。

(2) 分别用于三个共深输入 \(a,b_0,c\) 及每对原 sigma，
得到准确的原域返回
\[
\boxed{J'_{m;n,r}(0)
       =(-\lambda)^{3n+2mr}\,
                       \Phi_m(\kappa^n,\kappa^r).}
\tag{12}
\]
两条分支中的 \(c\) 均有相同标量 \(-\lambda\)；第二轴 \(x\)
保留完整单位域。每对的 \(\kappa^{2r}\) 正是 (11) 的
\(U^{2m}\) 在格点的值。因而 (12) 不是仅由相同边际推得，
而是 (7) 的每个原输入逐项缩放所得。

## 4. 用固定来源的移动负矩分离交替两支

置
\[
k=(p-7)/6,\qquad R=2+6k=p-5.
\tag{13}
\]
R429 对同一 \(b=17\) 的实际展开
\[
\sigma(z)=zA_b(z^6),\qquad A_b(w)^{-1}=\sum_{j\ge0}\beta_jw^j
\]
已经证明 \((-1)^j\beta_j>0\)。因此
\[
P_k(a)=[w^k]\frac{A_b(w)}{A_b(aw)}
\tag{14}
\]
是准确次数 \(k\) 的有理多项式。数
\(\alpha_m=(-27)^{-m}\) 两两不同，所以任意 \(k+1\) 个不同
正整数中至少有一个 \(m\) 满足 \(P_k(\alpha_m)\ne0\)。
也可要求 \(m=3\ell\)、\(1\le\ell\le k+1\)。

由 (4)，所有 \(\Theta\) 的完整聚合系数为
\[
\boxed{[z^{6k}]\prod_{h=1}^m\Theta(q_hz)
                  =2^{6k}P_k(\alpha_m).}
\tag{15}
\]
这已相加所有指数碰撞，不是仅选出一组非零单项式。

考虑 (11) 的准确系数 \(T^2U^{2m+6k}\)。
两个 sigma 的正矩都从一次开始，因此 \(T^2\) 强制
\(a,b_0\) 的指数各为一，并强制 \(c\) 的指数为零。
第一支 \(G(c)\) 的质量是 \(1\)，第二支 \(F(c)\) 的质量是
\(0\)。所以该系数中第二支完全消失，不需要估计两支抵消。

第一支剩下的第二轴负矩准确是
\[
I^F_{-(p-5)}
  =\int_{\mathbf Z_p^\times}x^{-(p-5)}\,d\nu_F(x).
\tag{16}
\]
R426 已由实际正四次矩证明
\[
I^F_{-(p-5)}
 \equiv24\Omega^4(1+\lambda\kappa^4)\not\equiv0\pmod p.
\tag{17}
\]
这是当前每个 \(p\) 的单位。没有使用尚未知的固定
\(I^F_{-2}\)，也没有将 principal 分支与非主 tame 分支混同。

总 log 指数 \(R=p-5\) 为偶数，故符号是负。
多项式展开中的阶乘与矩阶乘相消，且
\(c_ma_mb_*=2/3\)。完整系数准确为
\[
\boxed{
[T^2U^{2m+6k}]\Phi_m
=-\frac{2d}{3}(p-6)!\,
       \Omega^{p-5}\,2^{6k}P_k(\alpha_m)\,
       I^F_{-(p-5)}.}
\tag{18}
\]
所有显示常数、阶乘和 (16) 在当前素数处都是单位。
按 (14) 选择 \(m\) 后，(18) 因而严格非零。
本文不声称 \(P_k(\alpha_m)\) 或整个 (18) 为单位，也不声称
其赋值随 \(p\) 一致有界。已足够得到 \(\Phi_m\not\equiv0\)。

## 5. 任意深的真实两深度域均有非零项

**定理。** 对当前每个普通素数 \(p\)，按 (14) 选择 \(m\)。
任意 \(n_0\ge1\)，存在 \(n,r\ge n_0\)，使
\[
\boxed{J'_{m;n,r}(0)\ne0.}
\tag{19}
\]
两个深度还可各自限制在任意预先给定的无限算术子列，例如
\(n,r\in4\mathbf Z_{>0}\)。可另加任意固定的
\(r\ge n+D\)，或另加 \(n\ge r+D\)；在任一这种指定区域
仍有非零项。

证明：若整个双格点集的值均为零，(12) 的非零标量使
\(\Phi_m\) 在对应 \((\kappa^n,\kappa^r)\) 上为零。
先固定 \(r\)，第一变量有无限趋于零的零点，故由一变量解析
恒等定理恒零；再随 \(r\to\infty\) 使用同一定理，使
\(\Phi_m\) 恒零，与 (18) 矛盾。无限算术子列仍以零为聚点，
证明不变。若限制 \(n\ge r+D\)，固定 \(r\) 后仍有无限这样的
\(n\)；限制 \(r\ge n+D\) 时交换两个方向。证毕。

两深度保持独立。本篇没有由二变量非零推断对角限制 \(n=r\)
非零，也没有为每个指定深度对预付非零。

## 6. 原 norm-three 三元组仍可完整保留

若选 \(m=3\ell\)，R429 的实际三元组给
\[
\prod_{h=1}^{3\ell}\Theta(2\delta^{-h}z)
  =\prod_{j=1}^{\ell}E_{26}(2\delta^{-3j}z),\qquad
E_{26}=\frac{L}{J_{12}}.
\tag{20}
\]
每个 \(E_{26}\) 都是原固定来源的单位尺度推前。
(9) 仍指全部 \(6\ell\) 个原 sigma 输入共深 \(r\)；
(12) 仍包含 core 因子 \((-\lambda)^{6\ell r}\) 与
二次权缩放 \(\kappa^{6\ell r}\)。
(20) 不许可把它改读为仅限制某个 \(E_{26}\) 的相加输出。

## 7. 与已证完整中央和域运输的准确接点

R430 的实际条件恒等式是
\[
\int\mathbf1_{Y\in\mathbf Z_p^\times}
   d\log_p\langle Y\rangle\,h(X)\,d\nu_{\mathcal K}
=-\frac23J'_S(0)\int h\,d\nu_G
\tag{21}
\]
对每个连续 \(h\) 成立。本文的非零 (19) 则位于
\(X\) 单位、\(Y\) 深、\(W\) 单位的真实隐藏输入域，
并测试 \(W\) 的中央 log。这不是 (21) 中 \(Y\) 单位域的一条
直接测试；原 \(J'_S(0)=0\) 尚未被证明能使这些域全部消失。

R431 已独立支付同一个 \(\mathcal K\) 的完整 \(W,Q_*\) core，
R435 支付原 \(\mathcal R_{16,16}\) 的双轴偶深转移。
它们可用于接续 (7) 的完整域运输，但必须同时保留
\(a,b_0,c,t_{h,\pm}\) 的条件、二次权和所有补域。
尤其不能把完整 \(W\) 推前为零，等同于 (9) 的每个子域为零。

本篇的进展是把严格非零输入放进已经具有真实两轴条件中央、
新 degree52 总和 core 和完整交替分解的**同一个**小核内。
主目标的最后交域/补域关系仍未支付。

## 依赖

- [R426：原 degree18 的完整 core 与移动负矩单位](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)。
- [R429：倒 sigma 严格非零与完整两深度聚合](R429-original-two-depth-grid-and-reciprocal-sigma-nonvanishing.md)。
- [R430：同一个实际小核与任意第二轴测试](R430-original-integral-second-output-division-and-degree18-mixed-rows.md)。
- [R431：新 degree52 完整总和 core](R431-original-degree52-full-core-and-fixed-thirteen-ray.md)。
- [R435：原 degree16 的精确双轴深度转移](R435-original-degree16-square-core-and-exact-two-axis-depth-transfer.md)。

