# R88：pure 第四幂尾的下一项也只留下低阶历史端点势

日期：2026-11-14。状态：**已证明，独立纸面推导**。沿用 R85 的真实 R56 恢复、共同右锚和常值 scalar 端芽。令 $q=(c-\xi)^m$，$m\ge8$。除 R85 已消去的 $4m-9$ 阶外，本稿证明 $4m-8$ 阶也具有明确的准确原函数。零二阶总矩阵已经使该端点势消失；不需要把任何内部 history 设为零，也不需要先假设完整第三算子为零。

这不证明 $4m-7$ 或更高项消失，不证明完整第四成本为零或同号。首个实际 tail producer 保留的全部真实状态仍是后续研究输入。

## 1. 命题与准确系数

置

$$t=c-\xi,\qquad p=2m-3,\qquad r=3m-6,\qquad n=4m-9.$$

使用 R85 的局部改变量 $\widetilde W_H=W_H+\lambda P_H$，展开真实第二、第三 scalar histories：

$$\widetilde W_2=b_0t^p+b_1t^{p+1}+O(t^{p+2}),$$

$$\widetilde W_3=u_0t^r+u_1t^{r+1}+O(t^{r+2}).$$

全部系数都是同一真实 $s$ 路径上的函数。定义

$$\alpha_m=\frac{p^3}{8m^2(m-1)},\qquad
\beta_m=\frac{3p(3m-5)}{16m(m-1)}.$$

**定理。** 对零传入第二、第三 histories 的原始 pure forcing

$$H_4=-\frac1{16}H(Z_2,Z_2)-\frac14H(Y_q,U_3),$$

有

$$\boxed{[t^{4m-8}]\partial_s\widetilde W_4
=\partial_s\left(\alpha_m b_0^2b_1+\beta_m b_0u_1\right).} \tag{1}$$

(1) 是沿真实三角 ODE 的身份；证明使用 R85 已证的真实第一积分

$$u_0=-\frac{a_{mp}}{2a_{mm}}b_0^2,
\qquad a_{ij}=\frac{i(i-1)j(j-1)}{i+j-3}. \tag{2}$$

它不声称把 $b_0,u_0$ 当作互相独立的形式变量时仍可省略 (2)。若整条路径 $M=0$，常值端芽给 $b_0(0)=b_0(L)=0$，故

$$\boxed{[t^{4m-8}]V_4=0.} \tag{3}$$

对首轮公开计算的 $m=8$，(1) 的原函数为

$$\boxed{\frac{2197}{3584}\,b_0^2b_1
+\frac{741}{896}\,b_0u_1.} \tag{4}$$

## 2. 为何需要一个准确正交规范

仍记

$$z=\xi+\omega,\quad e=hz-k,\quad Q=1+e^2,\quad
\lambda=\frac{h_sz-h\omega_s}{h^2},$$

$$K_0=kz^2-\frac{k^2+1}{h}z,\quad K=K_0+\lambda_s,
\quad\omega_s=\frac{k_s}{2h}.$$

在本节 $I(F)=\int_c^\xi F$ 是有符号右原函数。对任意 R56 恢复场

$$Z_H=\frac Fz(A,zP+B,eA-hW),\qquad
A=\frac{W_\xi}{2}+\frac{\eta_0}{h},$$

定义

$$\psi_H=W+2Q I\left(\frac{\eta_0}{hQ}\right). \tag{5}$$

于是准确有

$$Z_H=-Y_{\psi_H}+\frac Fz\left\{
(zP+B)(0,1,0)+\frac{h(\psi_H-W)}Q(-e,0,1)\right\}. \tag{6}$$

证明是直接取 $(1,0,e)$ 方向内积并使用
$Q_\xi=2he$。括号中的余分子准确垂直于 $(1,0,e)$。

若一个恢复 profile 从 $t^j$ 开始，(6) 的余分子至少从 $t^j$ 开始，而 $Y_{\psi_H}$ 的分子从 $t^{j-1}$ 开始。与 $Y_{a t^i}$ 配对时，余分子的 $\xi$ 导数在最早候选项上仍垂直于 $Y_{a t^i,\xi}$ 的 $(1,0,e(c))$ 方向。故这个交叉项对 $P$ 的首个可能贡献是 $t^{i+j-1}$，对 $B,T_s$ 的首个可能贡献也是 $t^{i+j-1}$；$T_{s\xi}$ 经右原函数进入 (5) 后亦不早于此阶。

因此余场不影响 scalar 输出的 $t^{i+j-3}$ 与 $t^{i+j-2}$ 两项。两个余场相乘也不更早。这是一个准确的阶数结论，不是把余场完整删除或把其导数也称为正交。

## 3. 两个动态幂 profile 的前两阶公式

以下所有几何量均在 $\xi=c$ 求值，除非明确写出 $\xi$。定义

$$\mathcal C=\frac{KQ}{8h},\qquad
\mathcal D=\frac{Ke}{4},\qquad f=\frac{Q}{8h^2}>0.$$

这里 $f$ 只是几何权重，不是原始 profile。对指数 $i,j\ge2$ 置

$$\ell=i+j-3,\qquad
E_{ij}=(ij-a_{ij})\partial_c\mathcal C
+\left(\frac{a_{ij}}{\ell+1}-ij\right)\mathcal D.$$

若输入为 $Y_{a(s)t^i},Y_{b(s)t^j}$，准确正交 profile (5) 满足

$$[t^\ell]\psi_{H,s}=a_{ij}\mathcal C\,ab, \tag{7}$$

$$\boxed{\begin{aligned}
[t^{\ell+1}]\psi_{H,s}={}&E_{ij}ab+\mathcal L_{ij}(a,b),\\
\mathcal L_{ij}(a,b)={}&\frac{ij}{\ell(\ell+1)}\left\{
2(i-1)(j-1)f a'b'\\
&\hspace{12mm}-(j-1)(j-2)(fa')'b
-(i-1)(i-2)a(fb')'\right\}.
\end{aligned}} \tag{8}$$

式中撇号均为真实 $s$ 导数。为给出可逐项核查的推导，写 $e_0=e(s,c)$，$v_0=(1,0,e_0)$，则输入分子准确为

$$V_{a t^i}=a\left\{\frac i2v_0t^{i-1}
+h\left(1-\frac i2\right)(0,0,1)t^i\right\}.$$

由此直接计算 $P$ 的前两系数为

$$P_0=\frac{a_{ij}Q}{8h}ab,\qquad
P_1=\frac{ij(3i+3j-4-2ij)e}{8(\ell+1)}ab,$$

而 $B$ 的首项是 $ijQab/(8h)$，位于 $t^{\ell+1}$。
协变导数的首项使用

$$\nabla_s v_0=(0,h(c+\omega),e_s),$$

所以确实包含 $a',b'$，没有把移动框架当成固定坐标。
将这些项代入 R56 的 $T_s,T_{s\xi},\eta_0$，得到两个规范的差：

$$\boxed{[t^{\ell+1}](\psi_H-\widetilde W_H)
=-\frac{ij}{2}f_sab
-\frac{ij f}{\ell(\ell+1)}
\{(j-1)(j-2)a'b+(i-1)(i-2)ab'\}.} \tag{9}$$

静态部分整理成 $E_{ij}$；动态部分中
$e e_s/Q-h_s/h=f_s/(2f)$ 的两类一阶链项抵消，剩余恰为 (8)。这一计算只用原始 R56 公式和有限 Taylor 系数，亦适用于 $a$ 或 $b$ 在某点为零，不需除以 histories。

## 4. 应用到真实第二、第三链

为避免混淆原 completed 系数和正交系数，记

$$b=b_0,\qquad d=[t^{p+1}]\psi_2,
\qquad u=u_0,\qquad v=[t^{r+1}]\psi_3.$$

再置

$$A=a_{mm},\quad B=a_{mp},\quad B_1=a_{m,p+1},$$

$$H=\frac{mp(m-1)(m-2)}{r(r+1)},\qquad
\bar v=v-Hfb'.$$

利用 (6) 的余场阶数、(7)(8) 以及恢复场 $-Y_\psi$ 的真实负号，得到

$$\boxed{b'=A\mathcal C,\qquad d'=E_{mm},\qquad
u'=-B\mathcal C b,\qquad
\bar v'=-B_1\mathcal C d-E_{mp}b.} \tag{10}$$

特别 (2) 是 (10) 的准确第一积分，并且

$$\frac B{2A}=\frac{p^2}{3m(m-1)}.$$

由 (9)，原始与正交的下一系数准确相连：

$$\boxed{d=b_1-\frac{m^2}{2}f_s,
\qquad\bar v=u_1+\frac{mp}{2}f_s b.} \tag{11}$$

第三式里的 $Hfb'$ 被完整保留和移出；即使初始原 scalar histories 为零，正交第三下一系数也可能因 $b'(0)\ne0$ 而非零。这里没有给它重新零锚。

## 5. 看似能量项的准确相消

设

$$D_1=a_{m,r+1},\quad C_1=a_{p,p+1},\quad
J=\frac{p^2(p-1)(p-2)}{8n(n+1)},\quad
H_4=\frac{mr(m-1)(m-2)}{n(n+1)}.$$

把 (8) 用于完整的两项 pure forcing，并代 $v=\bar v+Hfb'$，第 $n+1$ 阶化为

$$\begin{aligned}
[t^{n+1}]\psi_{4,s}={}&
-\frac{C_1}{8}\mathcal C b d
-\frac{E_{pp}}{16}b^2
+\frac{D_1}{4}\mathcal C\bar v
+\frac{E_{mr}}4u\\
&+\partial_s\left(Jfbb'-\frac{H_4}{4}fu'\right).
\end{aligned} \tag{12}$$

关键是完整展开后留下的 $f(b')^2$ 系数**准确为零**：

$$\frac{D_1H}{4A}
-\frac{p^2(p-1)}{8(n+1)}=0. \tag{13}$$

此处既使用第三链中的 $Hfb'$，也使用
$b(fb')'=(fbb')'-f(b')^2$。省略前者会制造一个假的同号能量。

以下三个有理常数身份可直接代入 $p,r,n$ 核查：

$$\beta_m A=\frac{D_1}4,\qquad
2\alpha_m A-\beta_m B_1=-\frac{C_1}8,$$

$$\alpha_m E_{mm}-\beta_m E_{mp}
=-\frac{E_{pp}}{16}-\frac{B E_{mr}}{8A}. \tag{14}$$

最后一式分别比较 $\partial_c\mathcal C$ 与 $\mathcal D$ 两个系数即可，不需要假设它们相关。用 (2)(10)(14)，(12) 成为

$$[t^{n+1}]\psi_{4,s}
=\partial_s\left\{
\alpha_m b^2d+\beta_m b\bar v
+Jfbb'-\frac{H_4}{4}fu'\right\}. \tag{15}$$

## 6. 转回真正的 completed density

不能把 (15) 的正交 scalar 端差不加说明地当作原 period。
对完整 pure forcing 再用 (9)，准确得到

$$[t^{n+1}](\psi_4-\widetilde W_4)
=\frac{p^2}{32}f_sb^2+Jfbb'
-\frac{mr}{8}f_su-\frac{H_4}{4}fu'. \tag{16}$$

从 (15) 中减去 (16) 的真实 $s$ 导数，$fbb'$ 与 $fu'$ 项直接消去。再用 (11)，剩余原函数为

$$\alpha_m b^2b_1+\beta_m bu_1
+f_s\left\{\frac{p^2(m-2)}{8(m-1)}b^2+\frac{mr}{8}u\right\}.$$

大括号由 (2) 准确为零。这证明 (1)。这是逐项保存局部项后得到的消去，不是以正交性、倒行偶性或零总矩阵代替内部微分方程。

## 7. 端点、实际验证与未付范围

常值 scalar 端芽给 $\lambda=0$，故原 $W_4$ 与 $\widetilde W_4$ 的两个端值相同。原第二 scalar 零初值给 $b_0(0)=0$。若总 $M=0$，则 $W_2(L,\xi)=0$，因而 $b_0(L)=0$。式 (1) 的每一端项都有 $b_0$ 因子，证明 (3)。甚至不用另外要求 $b_1(L)=u_1(L)=0$。

准确核验可直接消费已发布的 tail DAG：先用真实 state RHS 验证

$$\partial_s\left(u_0+\frac{a_{mp}}{2a_{mm}}b_0^2\right)=0$$

及零初始常端芽，再检验原第 $4m-8$ density 与 (1) 右侧的差是否属于这个**已证明第一积分**生成的主理想。这样的代入有真实 ODE 与初值依据；不能推广为把所有独立 formal states 设成端值。

对 $m=8$ 的公开首轮计算，完整结构仍保留 14 个 genuine histories，且 R85 四个最低身份已经通过。另建的结构消费程序将验证本稿指定下一式，不改旧 producer、不重编 forcing、不重新选择几何路径。本文的一般 $m$ 结论由以上纸面证明给出，不把一个固定 $m$ 的计算冒作一般证明。

若幂尾前有常幅 $A_0$，完整 pure 第四响应整体乘 $A_0^4$。上面 $b_0,b_1,u_0,u_1$ 按单位幂尾约定；不混淆几何积分次数和 profile 齐次次数。有限尾、共同物理区间与后续光滑逼近的范围同 R85。

仍未得到新的正长度零第四成本环、真正第四正性泛函、$4m-7$ 后阶结论或主课题完整曲面。R83 的未知基线问题没有被两个自动消去的尾系数解决。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R85](R85-pure-fourth-leading-tail-is-an-exact-derivative.md)，以及[第二密度与正交规范补记](../notes/pure-tail-second-density-and-orthogonal-gauge-20261114.md)。
