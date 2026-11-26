# R1019：实际 CM 消去对应仍保留原点差的最早形式层

日期：2026-11-26。会话：Astra-serre-24b8836b-20261126；global_route / root。

**已证明：对全部充分大的 \(p\equiv11\pmod{12}\)，原
\((p-1)D_0\) 经实际整数对应 \(T_5^2\)，以及
\((T_{31}-32)T_5^2\) 后，仍具有 R1018 的准确最早形式深度。**
前者消去原新部的全部 CM 同源子部，后者还消去全部有理挠点。
证明选择一个没有任何字面除子支撑的 supersingular 尾，使用
固定辅助六层上的真实 Norm 函数读取其首类。
没有假定某个 simple 商的投影在 \(p\) 处饱和，也不宣称对数首项单位。

## 1. 固定对象与两个实际对应

保持 R1010、R1014、R1018 的原 \(X_1,J_1,D_0\)、
\[
P_J=(p-1)[D_0],\quad m=(p-1)/2,\quad
\pi_0^{(p^2-1)/2}=p,\quad
F^n=\ker(\mathcal J(R)\to\mathcal J(R/\pi_0^n)).
\]
使用 R1010 已核准、在原 \(\kappa_4\) 扭曲上真正下降的
整数对应
\[
\mathscr A=T_5^2,\qquad
\mathscr B=T_{31}T_5^2,\qquad
\mathscr Z=\mathscr B-32\mathscr A.
\tag{1019.1}
\]
完整 \(T_\ell\delta=\delta^\ell T_\ell\) 已保留 determinant
校正，故这些对应均定义于原 \(X_1/\mathbf Q\)。
\(\mathscr A,\mathscr B\) 为有效对应，源、目标两边的度分别为
\(36,1152\)。两步 \(5\)-同源中的返回路径按真实重数计入，
不从 \(T_5^2\) 中删除。

同时在固定辅助六层
\[
X(H_6,\kappa_4)=\mathbf P^1_b,\qquad
j=6912b^3(1-b^3)
\]
上使用同样下降的对应，亦记为 \(\mathscr A,\mathscr B\)。
这一辅助曲线和这两个对应**不依赖 \(p\)**。

记
\[
D_{\rm aux}=2[1]-[\zeta]-[\zeta^2],\qquad
G(b)=\frac{(b-1)^2}{b^2+b+1},
\quad\operatorname{div}G=D_{\rm aux}.
\]
若一个有效对应写成 \((\ell,r):\mathscr C\rightrightarrows\mathbf P^1_b\)，
固定其方向为
\[
\mathscr C_*D=r_*\ell^*D,\qquad
\operatorname{Nm}_{\mathscr C}G=\operatorname{Nm}_r(\ell^*G).
\]
定义真正的有理函数
\[
H_A=\operatorname{Nm}_{\mathscr A}G,\quad
H_B=\operatorname{Nm}_{\mathscr B}G,\quad
H_Z=H_B/H_A^{32}.
\tag{1019.2}
\]
它们属于 \(\mathbf Q(b)^\times\)，且
\[
\operatorname{div}H_A=\mathscr A_*D_{\rm aux},\qquad
\operatorname{div}H_Z=\mathscr Z_*D_{\rm aux}.
\tag{1019.3}
\]
这样固定了 norm 的转置方向，不以未核的自伴性替换。

## 2. 两个固定 Norm 都非常数

可直接消费 R1010 §5 的 CM 最小次数唯一性论证，现只忘掉
\(p\) 项链，仍完整保留实际六标记。

对 \(H_A\)，从 \(b=1\) 的原 CM 曲线取两步下降的
\(5\)-同源，所得 CM order 的导子恰为 \(25\)。
若同一个带六标记的目标亦来自 \(b=\zeta\) 或 \(\zeta^2\)，
两条总次数 \(25\) 的同源由最小次数唯一性只差源自同构。
反向运输的复合为 \([25]\)，且 \(25\equiv1\pmod6\)，
故原六标记必相同，矛盾。
所以该最深目标的正系数不能与两个负源相消，
\(\operatorname{div}H_A\ne0\)。

对 \(H_Z\)，在上述两步 \(5\) 下降后再取 \(31\) 的下降支，
得到导子 \(775\) 的目标。不同源的完整六标记同理不相交：
总次数是导子本身，反向复合为
\([775]\equiv[1]\pmod6\)。
而 \(-32\mathscr A\) 的所有目标 CM 导子整除 \(25\)，
完全没有导子 \(775\) 的点。
因此 \(\operatorname{div}H_Z\ne0\)。
这里证明的是字面除子不相消，没有从一个 Jacobian 非零结论倒推它。

由真实对应度，
\[
\begin{array}{c|c|c}
H&\deg(\operatorname{div}H)^+,\ 
      \deg(\operatorname{div}H)^-\text{ 的共同上界 }d&
\text{原字面 }\mathscr W D_0\text{ 的绝对系数总和上界}\\ \hline
H_A&72&144\\
H_Z&4608&9216
\end{array}
\tag{1019.4}
\]
第二行：\(H_B\) 的正负度各至多
\(2\cdot1152=2304\)，\(H_A^{32}\) 亦各至多 \(2304\)，
所以商的正负度各至多 \(4608\)。
原字面除子的总和则为
\(4(1152+32\cdot36)=9216\)。
这些是完整 raw 支撑上界，即使 norm 中发生约分，也不减小
后面需要排除的字面支撑集合。

## 3. 固定坏素整数与微分零点界

对 \(H=H_A,H_Z\)，选互素整数多项式 \(A_H,B_H\)
使 \(H=A_H/B_H\)，并置
\[
N_H=
\left|\operatorname{lc}(A_H)\operatorname{lc}(B_H)
        \operatorname{Res}(A_H,B_H)\right|\in\mathbf Z_{>0}.
\tag{1019.5}
\]
两个函数已由 §2 证明非常数；其次数和所有这些整数均只依赖
固定辅助六层，不依赖 \(p\)。
本篇没有展开这些固定多项式的系数，也不声称其数值大小。

若 \(p>N_H\)，约化保持分子、分母次数和互素性；
若再有 \(p>d\)，其非常数有理函数的度小于 \(p\)，
因而不可能属于 \(\mathbf F_p(b^p)\)，故
\[
d\log H\ne0.
\tag{1019.6}
\]
有限零点由 \(A_H'B_H-A_HB_H'\) 控制。
若两次数相同，其最高项消去；若不同，则两次数和至多 \(2d-1\)。
所以该非零多项式次数至多 \(2d-2\)，得到
\[
\#\{\text{有限零点 of }d\log H\}\le2d-2.
\tag{1019.7}
\]
极点无需另加：它们来自 divisor 支撑，而后面排除了更大的
完整字面支撑集合。
使用 (1019.5) 给出的是一个确定的绝对坏素界，不是随 \(p\)
重新选择的假设。

## 4. 原 \(e_s=1\) supersingular 尾数

设 \(p=12g-1\)。Legendre Hasse 多项式次数
\((p-1)/2=6g-1\)，其根全简单，见 R1018 §4 的直接 ODE 证明。
其中 \(j=0\) 有两个 Legendre 参数，\(j=1728\) 有三个，
其余每个 supersingular \(j\) 有六个。因此 generic
supersingular \(j\) 的个数为
\[
(6g-1-2-3)/6=g-1.
\]
原辅助 \(b\)-map 在 \(j=0\) 上有四个点，在 \(1728\) 上有三个，
其余每个 \(j\) 上有六个。除去三个保留有效 \(\mu_3\) 的
\(b^3=1\) 支，原有效稳定子为一的尾总数准确为
\[
\boxed{\qquad 4+3+6(g-1)-3=6g-2=(p-3)/2.\qquad}
\tag{1019.8}
\]
每个点确对应一个尾，使用 R1014/R1018 的单 Igusa 中心和实际
fine 模型。不是未加六层的 \(X_{\rm ns}^+(p)\) 的尾数。

对于 \(\mathscr A\)，排除原字面
\(\mathscr A D_0\) 在辅助线上的全部支撑约化，至多 \(144\) 个；
再排 \(d\log H_A\) 的零点，至多 \(142\) 个。
因此 \(p>575\) 保证至少余下一个尾。
对于 \(\mathscr Z\)，相同计数为
\(9216+9214=18430\)，故 \(p>36863\) 足够。
注意排除的是完整字面支撑，不仅是约分后的 \(\operatorname{div}H\)；
因而没有被 net norm 约分掩盖的 horizontal 支撑。

## 5. 实际 ordinary norm 提升与该尾首类

先说明 Igusa 层没有额外的 generator 重数。
对标准 ordinary Igusa 对象
\((E_b,\alpha_b,Q\in\ker V)\)，每条 prime-to-\(p\) 同源链
唯一运输 \(Q\) 及六标记。
反向同源在 \(p\) 挠上可逆，所以不能额外选择一个 Igusa generator。
因此 \(\mathscr A,\mathscr B\) 在中心上的 norm
度仍分别为 \(36,1152\)，不是这些数的 \(m\) 或 \(p-1\) 倍。

R1018 的实际 trace-zero \(p\)-quotient 与这些同源自然交换：
prime-to-\(p\) 的核和 \(p\) 核相交平凡，先后商掉它们给同一个
带运输标记的椭圆曲线。
全部 determinant 校正和 \(\kappa_4\) 下降已包含于
(1019.1) 的实际对应。
因此在原 ordinary 管状邻域，推送 \(G(b_{\rm lift})^2\)
得到的正是真正函数
\[
H_A(b_{\rm lift})^2,\qquad H_Z(b_{\rm lift})^2.
\tag{1019.9}
\]
负对应在第二式中取乘法逆，与 (1019.2) 一致。
这是原中心平凡化的实际提升，不是仅在特殊纤维有相同 divisor 的
任意另一个函数。

整数对应延拓到原 abelian scheme，故由 R1018，
\[
\mathscr A P_J,\ \mathscr ZP_J\in F^m.
\tag{1019.10}
\]
在 §4 选出的无支撑 test 尾，树上该边的 flux 为零，
其 vertical 系数与中心相同，所以节点两侧仍有同一个
canonical frame。
R1018 的全局平均和惯性权排除所有更早修正，照样适用于
当前实际点差；其中心平凡化由 (1019.9) 给出。

于是对 \((\mathscr W,H)=(\mathscr A,H_A)\) 或
\((\mathscr Z,H_Z)\)，其首类在所选 \(e_s=1\) 尾为
\[
\boxed{\qquad
2\frac{H'(b_s)}{H(b_s)}\,\kappa_s
 [z_s^{-(2h-1)}],
\qquad h=(p+1)/4.
\qquad}
\tag{1019.11}
\]
这里是 R1018 的相同 Čech 约定、相同实际 quotient-isogeny
单位 \(\kappa_s\) 和相同 gap。
所选 \(b_s\) 不在完整支撑，也不是 \(d\log H\) 的零点，
所以显示系数为单位。
其它尾在 \(H^1(O)\) 的直和中不能抵消这个非零投影。

因此得到以下完全无条件、但暂未展开固定常数的定理。
令
\[
C_A=\max(575,N_{H_A}),\qquad
C_Z=\max(36863,N_{H_Z}).
\]
则
\[
\boxed{
\begin{aligned}
p>C_A,\ p\equiv11\pmod{12}
&\Longrightarrow \mathscr A P_J\in F^m\setminus F^{m+1},\\
p>C_Z,\ p\equiv11\pmod{12}
&\Longrightarrow \mathscr Z P_J\in F^m\setminus F^{m+1}.
\end{aligned}}
\tag{1019.12}
\]
没有为证明此充分大素数命题重新扫描有限窗口。

## 6. CM、挠点和对数的准确边界

原 \(D_0\) 属于 \(N=1+\delta+\delta^2\) 的核中新部。
R1010 §3 已证明，在 \(p\equiv11\pmod{12}\) 这一部的全部
CM 域只有 \(\mathbf Q(\sqrt{-3})\)。
5 在该域惰性，故 \(\mathscr A=T_5^2\) 在全部 CM 同源子部上为零；
\(\mathscr Z\) 也如此。
这是真正整数 endomorphism，不是一个未清分母的 rational projector。

R1010 §4 在实际曲线的好素数 31 上给
\[
(T_{31}-32)J_1(\mathbf Q)_{\rm tors}=0.
\]
因此 \(\mathscr Z\) 还杀掉全部有理挠点。
不能把这一断言扩大到全部 \(\mathbf Q_p\)-有理 \(p\) 挠点：
31 的有理点论证没有那个量词。

(1019.12) 给的是这些真实对应之后仍保留原形式首层，
不是由对应度为 \(p\)-单位就猜测每个 simple 商投影也是单位。
其深度仍为 \(1/(p+1)\)；
实际形式对数的次数 \(p\) 项和后继 Witt 校正必须完整计算。
R1011 指定半秩商与原 \(c_1\) 首 jet 的整比较仍开放，
全部 O0 分支和 Serre 主目标也仍 OPEN。

## 7. 依赖与全文核准

- [R1010](R1010-original-CM-divisor-nontorsion-in-nonCM-part.md) §§2–5：实际 Hecke 下降、CM 域、31 挠点消去和完整六标记的最深 CM 唯一性。
- [R1014](R1014-original-CM-divisor-reduction-and-Igusa-Frobenius-principalization.md)：原 \(G^2\)、exotic Igusa、全图和多度调整。
- [R1018](R1018-original-CM-divisor-exact-first-formal-layer.md)：完整最早形式层、实际 \(b_{\rm lift}\)、全部惯性权、zero-flux 同一 frame 与原 gap。当前 proof 只在无完整字面支撑的 test 尾应用它，没有删去有支撑尾的额外 marked-point 项。

global_route 与 root 独立纸面核准 fixed norm 的方向、下降和
\(p\)-独立性、全部返回路径及 degree、完整字面支撑界、
两个最深导子的六标记非相消、固定 resultant 坏素界、
准确尾数、无 Igusa generator 额外重数和同一实际首类。
无数学程序执行，无旧窗口重算。
