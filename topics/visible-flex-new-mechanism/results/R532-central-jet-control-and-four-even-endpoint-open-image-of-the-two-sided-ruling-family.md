# R532：双边完整反馈族的中心 jet 配置与四偶端矩的真实局部开像

日期：2026-11-16。**原式纸证；没有执行 ODE 射击、profile 积分、符号程序、秩计算、数值检查或研究任务。**

本文接 [R530](R530-two-sided-complete-ruling-feedback-and-four-real-even-endpoint-moments.md) 的同一个 R521 正交母库与双边完整反馈。R530 已把原 $K=0$ 在两个实际半段同时支付，并以四个中心奇 E8 参数清除共同奇端入值；剩下四个偶端矩，但未证明它们的实际端映射具有开像。

这里给出一个正向控制结论：以三个**一次固定**的第三 Gram 参数精确指定中心的三个真实几何 jets，再与四个奇端条件共同求解。所得到的实际路径满足
$$
h(s)=H+O(s^6),\qquad
k(s)=vs+\frac b6s^3+O(s^5),\qquad v\ne0.
$$
在这同一完整反馈族中，四个偶半端矩对四个真实参数 $(L,H,v,b)$ 的 Jacobian 有严格非零首项
$$
\boxed{\det D_{(L,H,v,b)}(m_{p_1},m_{t_1},m_{r_1},m_{s_0})
=\frac{v^2L^7}{11520H^5}+O(L^9).}
$$
所以每个充分小的正长度点都给一份真正的四维端矩开像，不只是四个形式未知量或一张维数表。

这份开像仍在 $m_{t_1}<0$ 的区域；本文没有令其包含零，也没有构造 $M=0$。不同参数路径的最终左锚规范一般不同，不能因此把这些路径逐段接为同一个规范下的闭词。有限长度四根、实际端 germs、pose、第四累计与完整 period 均仍保留。

## 1. 保持的实际对象和唯一参数化

全部 profiles、实际正幅副本、宽度、物理位置、右锚、完整第三历史空间及合法紧几何域，均固定为 R530 的同一份对象。仍使用
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
$$
不把别的母库、旧十九／二十目标或另一份实际截面拼入本文。

固定 $\omega_c$，写 $y=x+\omega_c$、$\eta=\omega-\omega_c$。这仅是同一个右锚和 profiles 的固定坐标记法。R530 的双边真实 scalar 状态是
$$
S_+=(h,k,\omega_c+\eta),\qquad
S_-=(h,-k,\omega_c-\eta).
$$
两半的实际速度分别为 $(\gamma,\upsilon)$ 与 $(-\gamma,\upsilon)$，加速度分别为 $(a,c)$ 与 $(a,-c)$。沿 R530 的强合法紧域，
$$
C_h(S_\pm)<0,\qquad C_k(S_\pm)>0,
$$
且双边加速度矩阵
$$
\begin{pmatrix}C_h(S_+)&C_k(S_+)\\
C_h(S_-)&-C_k(S_-)\end{pmatrix}
$$
一致可逆。

继续用同一个固定 Gram 右逆
$$
\mathbf I_y(\phi_\theta,\chi_\theta^\nu)
=\sin^2\theta\,\nu,\qquad \nu\in\mathbb R^3.
\tag{1}
$$
下标 $y$ 表示全部三矩同时换到固定 $y$ 坐标；回到原 $x$ 坐标只施加一个固定可逆矩阵，不增加控制参数。$\chi^\nu$ 真紧、光滑、周期，并保两个 seed。

在这个坐标中，
$$
\mathbf w(S)=
\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right),
\qquad d=h\eta-k.
\tag{2}
$$
R530 的完整无加速度项只增加
$-2\mathbf w(S)\cdot\nu$。同一路径上的 $\nu$ 不随 $s$ 改动。

中心取
$$
h(0)=H>0,\quad k(0)=\eta(0)=0,\quad
h_s(0)=0,\quad k_s(0)=v,
$$
$$
A_+(0)=A_-(0)=\Phi_{\mathsf a},
\qquad T_+(0)=T_-(0)=0,\qquad
\mathsf a\in E_{\rm o}.
\tag{3}
$$
$E_{\rm o}$ 是 R530 已核的四维真实奇子空间
$(p_0,p_2,r_0,s_1)$，不是五维冗余坐标空间。取 $v$ 在一个远离零的固定小区间，$H$ 在正的紧区间，$b$ 在一个固定有限区间。

本文在(3)后用 $\nu$ 配置
$$
\boxed{
h_{ss}(0)=0,\qquad k_{sss}(0)=b,\qquad
h_{ssss}(0)=0.
}
\tag{4}
$$
其中 $b$ 是一个真实中心三阶导数参数，不是把 $k(s)$ 释放成任意函数。除(4)外的高阶 jets 继续由原双边 ODE 决定。

## 2. 三个 Gram 参数确能配置(4)

### 2.1 必须先用完整中心历史求三个 jet 方程

记正半段完整 ruling 除去 $\sin^2\theta$ 后为
$$
\mathcal K(s)=
\mathcal F(S,\gamma,\upsilon,A,T)
+C_h(S)h_{ss}+C_k(S)k_{ss}
-2\mathbf w(S)\cdot\nu .
\tag{5}
$$
$\mathcal F$ 是 R530 的完整函数，保全部 $YC$、变化-profile chain、右尾与实际第三累计。没有把它换成 principal 项。

按原 ODE，
$$
A_s=\Phi_{M_{\rm raw}},\qquad
T_s=-\Phi_{M_{\rm raw}}\circ A+\mathcal C_{\rm orig}.
\tag{6}
$$
$\mathcal C_{\rm orig}$ 关于两个加速度至多仿射。故在计算
$\mathcal K(0),\mathcal K_s(0),\mathcal K_{ss}(0)$ 时：

- $A_s,A_{ss}$ 由原 $M_{\rm raw}$ 及当前真实 jets 给出；
- $T_s,T_{ss}$ 由(6)给出，后者只需要加速度及其一次导数；
- 不需要把任何第三历史导数作为独立控制；
- $h_{ssss}(0)$ 只在显式的 $C_hh_{ss}$ 的两次导数中以 $C_hh_{ssss}$ 出现；
- $k_{sss}(0)$ 在一阶 jet 方程中以 $C_kk_{sss}$ 出现。

由 R530 的交换对称，中心自动有
$$
k_{ss}(0)=h_{sss}(0)=k_{ssss}(0)=0.
\tag{7}
$$
因此三个完整 jet 方程对依次待定的
$h_{ss}(0),k_{sss}(0),h_{ssss}(0)$ 是一个三角系统，其对角为
$C_h,C_k,C_h$，均非零。

为构造参数，先仅在这三个原式中形式代入(4)(7)，并用(6)恢复全部所需历史 jets。令其未含 $\nu$ 的值为
$$
F_0(H,v,b,\mathsf a),\quad
F_1(H,v,b,\mathsf a),\quad
F_2(H,v,b,\mathsf a).
\tag{8}
$$
这是对原完整有限公式的 jet 评价，不是一条已经存在路径的假替代。它们是光滑的真实有限函数。随后求出 $\nu$，再由原 ODE 的唯一性证明实际解具有这些 jets。

### 2.2 三个真实配对行及其准确行列式

在(3)(4)下，$d(0)=0$，
$d_s(0)=-v/2$、$d_{ss}(0)=0$。直接微分(2)得
$$
W_0=\mathbf w(0)
=\left(\frac1{4H},0,\frac H4\right),
$$
$$
W_1=\mathbf w_s(0)
=\left(0,-\frac v4,0\right),
$$
$$
W_2=\mathbf w_{ss}(0)
=\left(\frac{v^2}{8H},0,0\right).
\tag{9}
$$
最后一行使用了待配置的 $h_{ss}(0)=0$；若保一般 $h_{ss}(0)=a$，它的第一、第三分量应分别再加
$-a/(4H^2),a/4$，不能在一般状态漏掉这两项。

把(9)作为行组成 $W$，则
$$
\boxed{\det W=\frac{v^3}{128}\ne0.}
\tag{10}
$$
所以准确取
$$
\boxed{
\nu(H,v,b,\mathsf a)
=\frac12W^{-1}(F_0,F_1,F_2)^t.
}
\tag{11}
$$
这一取法在固定参数盒内光滑，使用同一个 Gram 右逆，不在两半分别选规范。

### 2.3 为何正式解实际满足这些 jets

把(11)用于 R530 原双边 ODE。在中心，第一条方程(5)和 $C_h\ne0$ 先迫使实际 $h_{ss}(0)=0$；$k_{ss}(0)=0$ 由交换对称已经成立。

接着对正式解微分(5)一次。全部低阶 jets 已相同，(8)(11)使方程在指定 $k_{sss}(0)=b$ 时为零，而其该阶未知量的系数是 $C_k\ne0$，所以正式解的 $k_{sss}(0)$ 正是 $b$。

再微分一次，同理用 $C_h\ne0$ 得正式解的 $h_{ssss}(0)=0$。这没有循环使用一个未付的 profile 对称性；它使用的是原双边 ODE 已付的中心交换和上述三角 jet 方程。

由中心奇偶性及光滑性，正式解因而满足
$$
h(s)=H+O(s^6),\qquad h_s(s)=O(s^5),
$$
$$
k(s)=vs+\frac b6s^3+O(s^5),\qquad
k_s(s)=v+\frac b2s^2+O(s^4).
\tag{12}
$$

## 3. 与四个奇端条件联合，而非先后拼两条路径

采用(11)后，把正半段矩阵端值的四个奇坐标记为
$$
\mathscr O(\mathsf a,L;H,v,b)
=\operatorname{pr}_{E_{\rm o}}\mathsf m_+(L).
$$
这是已经包含 $\nu(H,v,b,\mathsf a)$、全部真实 $A,T$ 和两半 ruling 的同一个正式端映射。

在 $L=0$，
$$
\mathscr O(\mathsf a,0;H,v,b)=\mathsf a,\qquad
D_{\mathsf a}\mathscr O=I_4.
\tag{13}
$$
有限维 IFT 给
$$
\boxed{
\mathsf a=\mathsf a_L(H,v,b),\qquad
\mathscr O(\mathsf a_L,L;H,v,b)=0.
}
\tag{14}
$$
于是每条最终路径都同时满足三条中心 jet 条件(4)和四条奇端条件(14)，不是把两个分别存在的方案拼起来。

原奇密度中心为零，故在固定小参数盒上有
$$
\mathsf a_L=O(L^2),\quad
D_{H,v,b}\mathsf a_L=O(L^2),\quad
\partial_L\mathsf a_L=O(L).
\tag{15}
$$
这也可以从 $\mathscr O=\mathsf a+O(L^2)$ 及其参数导数直接看出。

### 高阶余项的统一范围

原 ODE 在固定合法紧域内光滑，(11)(14)均光滑，且 $v$ 远离零。因此(12)的余项及其 $H,v,b$ 一阶导数在所有选定小参数中一致。将 $\mathsf a_L$ 代回时，不会破坏 $h''=h''''=0$ 或 $k'''=b$，因为(11)是对每个 $\mathsf a$ 重新精确配置的真实 jet 公式。

其余高阶系数可随 $L$ 改变，但由(15)它们及参数导数有统一界，且沿 $L$ 的额外变化至多为 $O(L)$。后面端积分的 Taylor 余项因而可同时求 $L,H,v,b$ 的一阶导数；没有把一个仅逐参数成立的 $O(s^m)$ 当成可微统一估计。

中心的 $\chi^\nu$ 在每条路径上仍固定。改变 $(L,H,v,b)$ 时 $\nu$ 一般改变，本文不宣称这个参数盒里的全部路径共享相同的最终左锚 $\chi$。

## 4. 四个原偶密度的逐式 Taylor 化

记
$$
p(L)=m_{p_1,+}(L),\quad
t(L)=m_{t_1,+}(L),\quad
r(L)=m_{r_1,+}(L),\quad
s(L)=m_{s_0,+}(L).
\tag{16}
$$
此处 $p,t,r,s$ 只是四个端值的短记号，不是 profile 的 $x$ 导数。中心 $\mathsf a_L$ 无偶坐标，所以这四个值直接是原偶密度从 $0$ 到 $L$ 的积分。

由真实水平关系 $\eta_s=k_s/(2h)$ 和(12)，
$$
\eta=\frac{k}{2H}+O(s^7),\qquad
\eta_s=\frac{k_s}{2H}+O(s^6).
$$
再令 $d=h\eta-k$、$a=h_s/h$，得到
$$
d=-\frac k2+O(s^7),\qquad
d_s=-\frac{k_s}{2}+O(s^6),\qquad a=O(s^5).
\tag{17}
$$
这些余项均有第3节的同一可微统一范围。

R73/R530 的四个完整原密度为
$$
M_{p_1}=k^2-kh\eta,
$$
$$
8M_{t_1}=2kh\eta-k^2-1-a^2,
$$
$$
8M_{r_1}
=h^{-2}\{(2kd+k^2-1+a^2)(1+d^2)-2add_s\},
$$
$$
4M_{s_0}
=h^{-2}\{d(d+k)(kd-1)-d_s^2\}.
\tag{18}
$$
逐项用(12)(17)，准确给
$$
\boxed{
M_{p_1}=\frac{k^2}{2}+O(s^8),\qquad
M_{t_1}=-\frac18+O(s^8),
}
\tag{19}
$$
$$
\boxed{
M_{r_1}=-\frac1{8H^2}-\frac{k^2}{32H^2}+O(s^6),
}
\tag{20}
$$
$$
\boxed{
M_{s_0}=\frac{k^2-k_s^2}{16H^2}
+\frac{k^4}{32H^2}+O(s^6).
}
\tag{21}
$$
例如(19)中 $2kh\eta-k^2=O(s^8)$，而 $a^2=O(s^{10})$；不能误把 $M_{t_1}$ 的首个速度修正写成 $v^2s^2$。
在(21)中，$d(d+k)=-k^2/4+O(s^{14})$，但 $d_s^2$ 的误差只是 $O(s^6)$，故保留的是后一阶数。

积分后得到本稿使用的完整 Taylor 行：
$$
\boxed{
t=-\frac L8+O(L^9),
}
\tag{22}
$$
$$
\boxed{
p=\frac{v^2L^3}{6}+\frac{vbL^5}{30}+O(L^7),
}
\tag{23}
$$
$$
\boxed{
r=-\frac{L}{8H^2}-\frac{p}{16H^2}+O(L^7),
}
\tag{24}
$$
$$
\boxed{
s=-\frac{v^2L}{16H^2}
+\frac{(v^2-vb)L^3}{48H^2}+O(L^5).
}
\tag{25}
$$
$k^4$ 的贡献从 $L^5$ 开始，已包含在(25)真实余项中，未被设成零。四个式子的 $H,v,b$ 导数保持所示阶数，$L$ 导数的余项阶数分别降一；由(15)造成的额外系数导数只给更高阶项。

## 5. Jacobian 的首项及完整消元

先把四行依序写成 $(t,r,p,s)$，参数取 $(L,H,v,b)$。将(22)作为第一主元，它是
$$
t_L=-\frac18+O(L^8),\qquad
(t_H,t_v,t_b)=O(L^9).
\tag{26}
$$
消去第一列对余三行的影响不改变下面的首项。

第二主元由(24)给
$$
r_H=\frac{L}{4H^3}+O(L^3).
\tag{27}
$$
其中必须保留 $-p/(16H^2)$ 对 $H$ 的导数；它属于上述 $O(L^3)$，并非字面零。另有
$$
r_v=-\frac{vL^3}{48H^2}+O(L^5),\qquad
r_b=-\frac{vL^5}{480H^2}+O(L^7).
$$
消掉第二列以后，第三主元仍为
$$
p_v=\frac{vL^3}{3}+O(L^5),\qquad
p_b=\frac{vL^5}{30}+O(L^7).
\tag{28}
$$

最后，未消第三列前，
$$
s_v=-\frac{vL}{8H^2}+O(L^3),\qquad
s_b=-\frac{vL^3}{48H^2}+O(L^5).
$$
前两列的消元只在此 $s_b$ 中增加 $O(L^5)$。因此最后的真实 Schur 主元是
$$
\begin{aligned}
s_b-\frac{s_v}{p_v}p_b
&=-\frac{vL^3}{48H^2}
+\frac{vL^3}{80H^2}+O(L^5)\\
&=\boxed{-\frac{vL^3}{120H^2}+O(L^5).}
\end{aligned}
\tag{29}
$$
这里 $p_b$ 虽比 $p_v$ 多两次 $L$，仍必须保留：$s_v/p_v$ 有 $L^{-2}$，删掉它就会把 $120$ 错写成 $48$。

乘四个主元得到
$$
\boxed{
\det D_{(L,H,v,b)}(t,r,p,s)
=\frac{v^2L^7}{11520H^5}+O(L^9).
}
\tag{30}
$$
从 $(p,t,r,s)$ 改为 $(t,r,p,s)$ 是偶置换，所以(30)也就是题首给出的原四偶顺序的行列式。

固定 $H$ 正紧域、$v$ 非零紧域及有限 $b$ 盒后，首项系数有严格正下界。故存在统一的 $\delta>0$，使每个 $0<L<\delta$ 的真实端映射都局部可逆。其逆由通常有限维 IFT 给出，所有目标都在**同一个完整 $K=0$ 实际路径族**中实现。

若改用从真实左端到右端的总四偶矩，R530 给
$M_{\rm tot,e}=2(p,t,r,s)$，故相应行列式为
$$
\det D M_{\rm tot,e}
=\frac{v^2L^7}{720H^5}+O(L^9).
\tag{31}
$$
这不是八维全矩阵任意开像：四个总奇坐标在当前对称族中恒为零。

## 6. 该实际开像的位置与规范边界

(22)同时给：缩小统一 $\delta$ 后，
$$
t(L)<-\frac L{16}\quad(0<L<\delta).
\tag{32}
$$
因此本稿虽给四维开像，却**没有**把零向量放入它。每个固定小正长度点的端矩与零有一个明确的正距离。不能由非零 Jacobian、调整四个参数的数量或局部逆直接宣称存在 $M=0$。

同一个真实参数选择完成以后，仍按 R530 一次左重锚：
$$
B=A_-(L),\quad T_\ell=T_-(L),\qquad
w_\theta=BD_\theta,\quad
\chi_\theta=\chi^\nu_\theta+2T_\ell(\phi_\theta;D_\theta).
\tag{33}
$$
四奇端已清，因此 $B=-\Phi_{(p,t,r,s)}$。原二阶、第三字段逐字保持，真 collars、三交叉矩、seed 与完整 ruling 均沿 R530 的同一个证明；没有另选某个半段的规范。

若实际四偶目标以后达到零，则(33)确给 $B=0,w=0$。但改变本稿的参数时，$\nu,T_\ell$ 一般改变。故这一局部逆**不是**一份允许在全局同一固定 $w,\chi$ 下随意拼接不同端矩路径的控制表。要保持最终规范继续变动参数，还须同时保其真实端数据，不能在中途重锚归零。

同样，本文没有补付 $s=\pm L$ 各自的反射-compatible 全 germs。R530 中心的全 jet 对称不等于末端可倒行拼接。Frame、位置、完整第三端值与第四原函数的两半和仍全保；尚未得到周期词、第四完整 range 或原十三行的联合解。

## 7. 对后继有限长度问题的具体作用

与只写(30)为四个待解方程相比，本稿新增了一个严格的实际事实：四个偶端矩没有在小长度分支上被某个未显示的恒等式压到低维面；三个固定 Gram 与真实中心／长度参数能使其末值作四个独立变化。这一结论已经包含中心奇端修正对高阶 Taylor 系数的影响。

后继应继续同一个反馈分支，保留(33)的规范变化、原合法域以及完整成本，在有限 $L$ 寻找四偶零点或证明该全分支不能到达它。当前的严格负项(32)明确要求离开这份小长度范围；它不排有限幅值路径，也不授权把一条无 ruling 的八矩配平曲线替代为该分支。

### 原来源及范围

- [R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)：完整八矩(9)–(11)及真实有序第三演化(16)(17)；
- [R521](R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)：同一有限正交库、完整相位合成、第三历史与加速度行；
- [R530](R530-two-sided-complete-ruling-feedback-and-four-real-even-endpoint-moments.md)：双边实际 ODE、中心交换、四奇子空间、左重锚及四偶原式。

没有用新增数据、少数样值或形式维数支持(30)。它由上面逐式 Taylor 与完整实际参数化证明。
