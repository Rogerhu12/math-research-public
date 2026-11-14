# Relative Kummer Frobenius 的垂直 jet、CM 半线交换与实际 GM 配对

日期：2026-11-12。状态：固定单位、有限秩 Frobenius 矩阵、
普通/惰性的一阶垂直式及准确临界配对均已证明。
未得到临界值在无穷多个素数上的非零性。

## 1. 同一实际权一模形式的两条半线

沿用[固定除法单位模型](2026-11-12-weight-one-division-unit-relative-model.md)：
\(N=68\)、\(f=34(1+i)\)，两固定单位为
\(R_{\mathcal S}(t,Z)\)、\(R_{\rm rot}(t,Z)\)，
其中 \(t=\lambda-1/2\) 是模参数，\(Z=t_E\) 是沿纤维在 \(O\)
的正式参数。两单位在 \(Z=0\) 都等于 \(1\)，并且
\[
\partial_Z\log R_{\mathcal S}(t,0)=-N^2S(t),\qquad
\partial_Z\log R_{\rm rot}(t,0)=-N^2S_{\rm rot}(t).
\tag{1}
\]
令
\[
S_+=(S-iS_{\rm rot})/2,\qquad
S_-=(S+iS_{\rm rot})/2.
\]
原来的偶半线是
\[
M_e=M_1=c_eS_+,\qquad
c_e=\frac{\sqrt2\,17^{17/4}}{4800f},\qquad
M_e=t^4+\tfrac72t^6+\cdots.
\tag{2}
\]

需要保留另一条实际半线。
在 R47 的 \(\mathscr B(T)=\sum m!e_mT^m\) 中，
\(e_1=4/17^3\)、\(q_0=-8i17^{3/2}\)。定义
\[
\mathcal B_o(u)=
 \frac{\mathscr B(q_0u)-\mathscr B(-q_0u)}{2q_0e_1}
 =K(t(u))M_o(t(u)).
\tag{3}
\]
由同一周期归一，准确有
\[
\boxed{\quad
M_o=c_oS_-,\qquad
c_o=\frac{i\sqrt2\,17^{7/4}}{32f},\qquad
M_o=t+\tfrac12t^3+\cdots .
\quad}
\tag{4}
\]
例如 \(c_o\) 是
\((\sqrt2\,17^{1/4}/f)/(q_0e_1)\)，没有引入新的周期常数。
因为 \(\mathcal B_o\) 只含 \(m\equiv1\pmod4\)，其系数
\(m!e_mq_0^{m-1}/e_1\) 有理，所以 \(M_o\) 也有理。
它是固定代数 germ。原来的整模型还给
\[
M_e,M_o\in\mathbb Z_p[[t]]
             \qquad(p\notin\{2,3,5,17\}).
\tag{5}
\]
(4) 的三次系数只需 \(u=t+t^3+\cdots\)、\(K=1+t^2/2+\cdots\)。

## 2. 真正的有限 Kummer Frobenius exact 项

固定一个目标好素数，并在未分歧扩域完成环 \(\mathcal O\)
中容纳全部固定系数。令 \(\sigma\) 为 Witt Frobenius。
在光滑的正式邻域 \(\mathcal O[[t,Z]]\) 上取任意局部 Frobenius lift
\[
\phi(t)=t^p,\qquad \phi(Z)=Z^p+p\,a_1(t)Z+p\,O(Z^2),
\quad \phi(Z)|_{Z=0}=0.
\tag{6}
\]
\(a_1(t)\) 可以是任意整级数；(6) 没有假装是一个特征零
椭圆曲线的次数 \(p\) 自同源。

若 \(r(t,Z)\) 是上述任一归一单位，置
\[
Q_r=\frac{r^\sigma(t^p,\phi(Z))}{r(t,Z)^p},\qquad
B_r=\frac1p\log Q_r.
\tag{7}
\]
由于 \(Q_r\equiv1\pmod p\)，
\[
\boxed{\quad B_r\in\mathcal O[[t,Z]],\qquad B_r(t,0)=0.\quad}
\tag{8}
\]
这是完整整级数结论：对 \(1+ph\) 展开，
\(\log(1+ph)/p=\sum_{n\ge1}(-1)^{n+1}p^{n-1}h^n/n\)，
每项整且 \(p\)-进收敛。

写 \(H_r=\log r\)，它在 \(Z=0\) 取零。
相应 rank-two Kummer 系统满足准确水平关系
\[
\binom{1}{H_r^\sigma\circ\phi}
 =
 \begin{pmatrix}1&0\\pB_r&p\end{pmatrix}
 \binom{1}{H_r}.
\tag{9}
\]
连接来自绝对闭一形式 \(d\log r\)，所以这是一个真正的
integrable Kummer connection 及其 Frobenius 比较；
不是只沿单一向量场指定的部分连接。
矩阵行列式为 \(p\)，其 Tate 格的指数没有被当作免费整基变换。

对两单位共享常数分量，得到秩三系统。
简记 \(H_S,H_R\) 及 \(B_S,B_R\)，并定义
\[
h_e=-\frac{c_e}{2N^2}(H_S-iH_R),\qquad
h_o=-\frac{c_o}{2N^2}(H_S+iH_R),
\]
\[
B_e=-\frac{c_e}{2N^2}(B_S-iB_R),\qquad
B_o=-\frac{c_o}{2N^2}(B_S+iB_R).
\tag{10}
\]
于是
\[
\partial_Zh_e(t,0)=M_e(t),\qquad
\partial_Zh_o(t,0)=M_o(t),
\tag{11}
\]
而 \(B_e,B_o\) 仍是完整整级数。

## 3. 系数 Frobenius 交换惰性处的两条半线

惰性 \(p\equiv3\pmod4\) 时 \(\sigma(i)=-i\)。
由 (9)–(10) 逐项得到
\[
\boxed{\quad
h_e^\sigma\circ\phi
  =p\frac{c_e^\sigma}{c_o}(h_o+B_o),\qquad
h_o^\sigma\circ\phi
  =p\frac{c_o^\sigma}{c_e}(h_e+B_e).
\quad}
\tag{12}
\]
这是真实的两条半线交换。不能在这里把 \(-i\) 当作系数
Frobenius 固定的标量。

普通 \(p\equiv1\pmod4\) 时则是
\[
\boxed{\quad
h_e^\sigma\circ\phi
  =p\frac{c_e^\sigma}{c_e}(h_e+B_e),\qquad
h_o^\sigma\circ\phi
  =p\frac{c_o^\sigma}{c_o}(h_o+B_o).
\quad}
\tag{13}
\]
所有显示的常数比都是 \(p\) 单位，但不需要猜测其具体四次根相位。

置 \(b_e(t)=\partial_ZB_e(t,0)\)。
因为 \(M_e,M_o\) 的系数有理，对 (12) 或 (13) 求第一垂直导数，
再用 \(\partial_Z\phi(Z)|_0=p\,a_1(t)\)，得到
\[
\boxed{
\begin{array}{ll}
p\equiv3\pmod4:&
 b_e(t)=\eta_p a_1(t)M_o(t^p)-M_e(t),
 \quad \eta_p=c_e/c_o^\sigma,\\[2mm]
p\equiv1\pmod4:&
 b_e(t)=\eta_p a_1(t)M_e(t^p)-M_e(t),
 \quad \eta_p=c_e/c_e^\sigma .
\end{array}}
\tag{14}
\]
本式的 \(\partial_Z\) 不是模参数方向的 Gauss–Manin 导数。

## 4. 裸垂直 Bockstein 的临界系数依赖于 lift

在 (6) 中把 \(a_1\) 改为 \(a_1+h(t)\)，仍是同一个特殊纤维
Frobenius 的合法正式 lift，并仍保持零截面。
惰性处 (14) 使
\[
\Delta b_e=\eta_ph(t)M_o(t^p).
\]
由于 \(M_o=t+O(t^3)\)，准确有
\[
\boxed{\quad
[t^{p+1}]\Delta b_e=\eta_p[t]h(t).
\quad}
\tag{15}
\]
\(\eta_p\) 为单位，所以这个剩余可以任意改变。
即使要求在 \(t=0\) 保留同一个 first-jet 初值，
选择 \(h(t)=ct\) 仍有此自由度。
两种 lift 的 Kummer 修正都满足 \(B_r(t,0)=0\)；
只指定归一化值和 CM 初值并不能消除 (15)。

普通处的差从 \(t^{4p}\) 开始，因此不影响次数 \(p-1\)。
这种差别源于准确的 CM 半线交换，不是忽略一个周期的结果。

(15) 说明单独的 \([t^{p+1}]b_e/p\) 不是目标的
lift-independent Frobenius 矩阵条目。
需要与 projective GM 坐标及其 exact 比较一并使用。

## 5. 与实际临界行的准确补偿配对

使用[真实整 GM Frobenius](2026-11-12-integral-gm-frobenius-critical-row.md)
的 \(U_p,V_p\)。两类型中它们都是整函数，
\(U_p=1+O(t^2)\)、\(V_p=t+O(t^3)\)，且分别为偶、奇。
记 \(s=1-4t^2\)、\(J_p^F=V_p/t\)，定义
\[
F_{i,p}=\frac{U_p^{p+1}}{s(J_p^F)^{p+2}},\qquad
F_{o,p}=\frac{U_p^{p-1}}{s(J_p^F)^p}.
\tag{16}
\]
两者完整地属于 \(1+t^2\mathbb Z_p[[t]]\)。
该 GM 比较已给特征零完全相等
\[
C_{p+1}=[t^{p+1}]M_eF_{i,p},\qquad
C_{p-1}=[t^{p-1}]M_eF_{o,p}.
\tag{17}
\]

惰性处把 (14) 代入 (17)。
因为 \(M_o(t^p)=t^p+O(t^{3p})\)，且 \(F_{i,p}(0)=1\)、
\([t]F_{i,p}=0\)，得到
\[
\boxed{\quad
C_{p+1}
  =\eta_p[t]a_1(t)-[t^{p+1}]b_e(t)F_{i,p}(t).
\quad}
\tag{18}
\]
这是完整精度的恒等式。
改 \(a_1\) 为 \(a_1+h\) 时，第一项增加
\(\eta_p[t]h\)，第二项准确增加同一个数，故整个差不变。
(15) 中的自由度在这里显式消掉。

实际平方关系已证明 \(C_{p+1}\in p\mathbb Z_p\)，所以目标行为
\[
\boxed{\quad
\frac{C_{p+1}}p=
 \frac{\eta_p[t]a_1-[t^{p+1}]b_eF_{i,p}}p.
\quad}
\tag{19}
\]
两个分子项可以各自不是 \(p\) 的倍数。
必须先形成准确的差，再除 \(p\)。
取局部 lift \(a_1=0\) 时，它简化为
\(-[t^{p+1}]b_eF_{i,p}/p\)，但这只是合法规范之一。

普通处 \(M_e(t^p)\) 起于 \(t^{4p}\)，所以同样得到
\[
\boxed{\quad
C_{p-1}=-[t^{p-1}]b_eF_{o,p},\qquad
\frac{C_{p-1}}{p^2}
       =-\frac{[t^{p-1}]b_eF_{o,p}}{p^2}.
\quad}
\tag{20}
\]
该分子被 \(p^2\) 整除仍来自实际中央平方与秩条件，
不是任意 Kummer connection 的一般结论。

## 6. 这份比较保留了什么

(9)、(12)–(14) 给出了两个固定 relative Kummer 单位的
有限秩 Frobenius exact 项；(18)–(20) 将这些项和真正的整 GM
矩阵配成了原来的指定临界系数。所有固定角色、CM 共轭、
初值与除 \(p\) 均保留。

剩下的量仍然取随 \(p\) 增长的模参数 jet。
目前没有把它证明为某个固定秩线性 cohomology 群上的
单个 Frobenius 条目，也没有证明其非零。
特别是固定 Kummer 类非零、\(M_o\) 的已知单位首项，
或任取 lift 使 \([t]a_1\ne0\)，都不能越过 (18) 的准确相消。

### 来源

- 固定单位、全部标签、\(c_e\)、好整模型：
  [除法单位 relative 模型](2026-11-12-weight-one-division-unit-relative-model.md)。
- R47 的实际 Borel，R45 的 \(e_1\)，及全权偶部：
  [全权 GM 临界行](2026-11-12-full-weight-one-gm-critical-rows.md)。
- 实际整 Frobenius 函数与 (17) 的完整精度：
  [整 GM Frobenius](2026-11-12-integral-gm-frobenius-critical-row.md)。
- 本文局部 Kummer 矩阵、半线交换及相消配对均直接证明，
  不把一个尚未证明的 regulator 非退化结论当作输入。
