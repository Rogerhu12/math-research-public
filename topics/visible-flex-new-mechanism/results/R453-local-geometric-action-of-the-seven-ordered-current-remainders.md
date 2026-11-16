# R453：七个 ordered-current 余量的完整局部几何 action

日期：2026-11-16。**完整原式纸面证明；没有执行新的求积、profile、符号程序、秩、原根恢复或研究计算。**

[R442](R442-second-history-diagonal-cubic-and-finite-part-highest-gauge-functional.md) 已把七个 current 余量写成真实第二累计尾的三次型
$\mathcal C_{\rm path}(n)$。本稿再消去这个三次型在矩抛物线上的全部累计 history：在原 whole self 为零的实际背景下，它恰等于一个只含 $h,k,\omega$ 及其前两阶导数的局部路径积分。保留真实边界后，再把这个积分降到只含一阶几何速度的形式。

这不是将七余值宣布为零。准确的新结论是公式(26)及其一阶速度形式(30)：它们给当前实际路径一个不需要重建 $m,\beta$ 或逐包逆解的完整检验。最高两个位置系数也在(33)—(34)中列出。

来源为 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md)、[R295](R295-final-grid-forces-zero-platform-matrix-and-exact-self-history-principal.md)、[R439](R439-diagonal-current-quotient-and-exact-simultaneous-cap-criterion.md)及 R442。原 whole self 的规范是 $\mathcal Q(V)(u)=\frac14[x^2]V(u^2,0)$；不以有限 profile 上的 self 值替代它。

## 1. 固定同一实际路径及定义域

固定同一个实际闭几何，保持共同右锚、原初值以及全部连接段。写
$$
h>0,\qquad
\gamma=h_s,\qquad
\nu=\omega_s=\frac{k_s}{2h},
$$
$$
z=x+\omega,\qquad
d=h\omega-k,\qquad
e=hx+d=hz-k,\qquad Q=1+e^2.
\tag{1}
$$
路径端点 $s_0,s_1$ 的 frame 和几何 jets 相同；canonical 二阶累计矩阵为
$$
m(s)=\int_{s_0}^sM(t)\,dt,\qquad m(s_0)=m(s_1)=0.
\tag{2}
$$
涉及 R439 实际 current 的结论时，保留当前真实条件
$$
T_{\rm total}=\tau_{\rm hook}\mathfrak H,\quad\tau_{\rm hook}\ne0,
\qquad \pi V=0,\qquad \mathcal QV=0,\qquad O_{\rm all}(V)=0.
\tag{3}
$$
其中 $O_{\rm all}$ 是所有真实有序 $3+2$ 自然系数。本文不把有限自然查询为零改写成 universal self 或 universal ordered 身份。

(2)是下文杀掉 $a$ 端项的条件；(1)的真实周期 jets 是杀掉最后一阶化边项的条件。R442 从 $c_V$ 到 $\mathcal C_{\rm path}$ 的识别还使用(3)所保证的原跨包场周期性。各处用途分别保留，不把任一单尾在端点设为零。

对于当前从起点选择的 $8\times12$ 宏复制母库，(1)—(3)是同一实际路径上的条件。下文不改变任何母、宽度、幅值、顺序、incoming 或独立二阶规范，也不假设所有 period range 门已经支付。

## 2. 一般矩模式的两个世界向量

对固定 $n=(n_0,n_1,n_2)$，R292 的真实第二左尾为
$$
\Pi_n=(a_nz+t_n,\ p_nz,\ \eta_nz+q_n),
$$
$$
p_n=\frac{(1+d^2)n_0+2hdn_1+h^2n_2}{8h}.
\tag{4}
$$
令
$$
y_n=t_n/h,\qquad w_n=q_n/h,\qquad
\rho_n=(y_n)_{ss}+y_n-kw_n.
\tag{5}
$$
原平台恢复方程是
$$
(a_n)_s=kp_n,\qquad
(\eta_n)_s-p_n=h^2(y_n)_s,\qquad
(w_n)_s=-k(y_n)_s.
\tag{6}
$$
并且
$$
\eta_n=-h^2y_n-ka_n-(p_n)_s.
\tag{7}
$$
采用原有向 frame
$$
T_s=kN,\qquad N_s=-kT-B,\qquad B_s=N,
$$
定义实际世界向量
$$
\mathbf U_n=F(a_n,p_n,\eta_n),\qquad
\mathbf v_n=F(-w_n,(y_n)_s,y_n),\qquad F=(T,N,B).
\tag{8}
$$
逐三分量使用(6)—(7)，得到
$$
\boxed{
(\mathbf U_n)_s=h^2(T\times\mathbf v_n),\qquad
(\mathbf v_n)_s=\rho_nN.
}
\tag{9}
$$
例如第一式的 frame 分量是
$(0,-h^2y_n,h^2(y_n)_s)$；第二式的 $T,B$ 分量分别由
$-(w_n)_s-k(y_n)_s=0$ 与 $(y_n)_s-(y_n)_s=0$ 准确消去。
这些是原场的等式，不是另外指定两个可自由控制的向量。

于是，令
$$
\mathscr B_n=\mathbf U_n\cdot\mathbf v_n
=-a_nw_n+p_n(y_n)_s+\eta_ny_n,
$$
便有
$$
\boxed{(\mathscr B_n)_s=p_n\rho_n.}
\tag{10}
$$
叉积项与 $\mathbf v_n$ 正交，故这里没有漏掉 $h_s$。

R442 的真实三次矩型因此满足完整边界恒等式
$$
\boxed{
\mathcal C_{\rm path}(n)
=-4[a_n\mathscr B_n]_{s_0}^{s_1}
+4\int(a_n)_s\mathscr B_n\,ds.
}
\tag{11}
$$
在(2)下，$a_n(s_0)=a_n(s_1)=0$，所以显示端项为零。$p_n,t_n,q_n,\eta_n$ 一般并不分别为零。

式(10)还解释了平台矩阵与本三次型的差别：R295 的平台配对是
$\mathcal T(n,m)=\frac14\int\eta_n\rho_m$，而(11)使用 $a_np_n\rho_n$。仅有 $\mathcal T=0$ 不能按权重名称直接删除后者。

## 3. 固定矩抛物线时的真实三项尾值

以下固定物理 $x$，在整个 $s$ 积分中置
$$
n=n_x=(1,x,x^2),\qquad p=p_{n_x}=\frac{Q}{8h}>0.
\tag{12}
$$
这个 $n_x$ 是固定外参数的代数代入，不把它称为某个实紧包的点质量矩。求 $s$ 导数时不改变 $x$ 或 $n_x$。

另用 $y$ 作尾多项式的自变量，写
$$
W_n(s,y)=a_n(s)y^2+b_{{\rm tail},n}(s)y+c_{{\rm tail},n}(s).
$$
在 $y=x,n=n_x$ 处定义
$$
a=a_{n_x},\qquad
b=\partial_yW_{n_x}(s,y)|_{y=x},\qquad
c=W_{n_x}(s,x).
\tag{13}
$$
R73 的八矩表给
$$
a=-A_{1,m}(s,x)/4,\qquad b=A_{2,m}(s,x),\qquad c=C_m(s,x).
\tag{14}
$$
这里 $b$ 不是 $b_{{\rm tail},n_x}$。例如
$\partial_yW_{n_x}|_{y=x}
=B_{0,m}'(x)+xB_{1,m}'(x)+x^2B_{2,m}'(x)=A_{2,m}(x)$，
正是原 $A_2=C_x-(B_1+2xB_2)$ 身份；没有在求导时顺带微分 $n_x$。

略去 $n_x$ 下标，R292 的原恢复现在准确为
$$
t=\frac b2-za-\frac{p_s}{2h},\qquad y=t/h,
$$
$$
\eta=-h^2y-ka-p_s,\qquad
w=q/h=-ky-c+zb-z^2a.
\tag{15}
$$
原点态二阶密度还给
$$
a_s=kp,\qquad
b_s=pK_{0,x}-\frac{\gamma p_s}{h^2},\qquad
K_{0,x}=2kz-\frac{1+k^2}{h}.
\tag{16}
$$
第二式可直接由 R73(5)核对：
$$
p_s=\frac{ee_s}{4h}-\frac{\gamma Q}{8h^2},
$$
所以 $-\gamma p_s/h^2$ 正是原
$-\gamma ee_s/(4h^3)+\gamma^2Q/(8h^4)$。
它不是把连接段删掉后的静态式。

## 4. 累计向量配对与局部余项的精确分离

定义两项原端势修正
$$
G=b+\frac{\gamma p}{h^2},\qquad
C^\flat=c+\frac{e_sp}{h^2}.
\tag{17}
$$
本节的 $G$ 只是二阶 self 的一个系数，不是 R327 的 period 目标。

先把(15)代入 $\mathscr B=-aw+py_s+\eta y$。
令 $L=b/2-za$，则 $hy=L-p_s/(2h)$，从而
$$
-aw+\eta y=ac-\frac{b^2}{4}+\frac{p_s^2}{4h^2}.
$$
因此
$$
\mathscr B=ac-\frac{b^2}{4}+py_s+\frac{p_s^2}{4h^2}.
\tag{18}
$$
再对 $y$ 用(15)—(16)真正求导。利用
$e_s=\gamma z-h\nu$，得到
$$
y_s-\frac{ae_s}{h^2}+\frac{\gamma b}{2h^2}
=-\frac{(1+k^2)p}{2h^2}
-\frac{p_{ss}}{2h^2}
+\frac{\gamma p_s}{2h^3}.
\tag{19}
$$
将(19)与(17)放回(18)，准确得到
$$
\boxed{\mathscr B=aC^\flat-\frac{G^2}{4}+\mathscr R_{\rm loc},}
\tag{20}
$$
其中完整局部余项是
$$
\boxed{
\mathscr R_{\rm loc}
=-\frac{(1+k^2)p^2}{2h^2}
+\frac{p_s^2}{4h^2}
-\frac{p\,p_{ss}}{2h^2}
+\frac{\gamma p p_s}{2h^3}
+\frac{\gamma^2p^2}{4h^4}.
}
\tag{21}
$$
特别，最后一项为正号，来自 $G^2$ 的完整平方。式(21)没有 $m$、$\beta$、第三累计或任何新增积分常数；$p$ 是(12)的真实几何函数。

## 5. whole self 的完整主项与迹

暂用 $u,v,r$ 表示 profile 的自由局部 jets
$(u,u',u'')$，与(15)的几何 $y,w$ 不混用。

R295(18)—(23)从 R56 原二阶场得到
$$
(V_Z)_x=(1,0,e)\Lambda\,u'''+\mathcal Z_{\le2},
\qquad
\Lambda=-2au+Gv-C^\flat r.
\tag{22}
$$
其 whole self 有完整分裂
$$
\mathcal Q(V)(u)=\int_I\mathscr F_B(x;u,u',u'')(u''')^2\,dx
+\mathcal L_B(u),
$$
$$
\mathscr F_B=-\frac18\int\frac{kQ}{h}\Lambda^2\,ds
=-\int a_s\Lambda^2\,ds.
\tag{23}
$$
$\mathcal L_B$ 是固定紧支撑 $C^2$ 范数下连续的完整四次泛函，保留全部左尾矩、端势和线性 $u'''$ 项。

这里的系数可直接从 raw self 核对：在 $\phi=0$ 时第四 forcing 是
$-H(Z_u,Z_u)$，所以
$\mathcal Q(V)(u)=-\frac14[x^2]\mathscr P H(Z_u,Z_u)$。
这正是 R295 使用的 $-1/8$ 主系数，不需要把单个 $Z_u$ 假紧，也没有把 whole pure 极化的另一规范混入 self。

为说明余项的完整性，R295(21)保留
$$
[x^2]\mathscr P H(Z,Z)
=\int\left\{\frac{k}{2h}\int|V_{Z,x}|^2dx
+k\left[(\ell-\omega)\frac{|U|^2}{2h}+\frac{U\cdot V_{\rm tail}}h\right]
+\frac{|\nabla_sU|^2}{2h^2}\right\}ds.
$$
后两组是真实左仿射分子 $xU+V_{\rm tail}$ 的项，全部只依三矩和至多二阶 jets。线性最高 jet 项按 R295 的 $r$ 原函数分部，原函数在 $r=0$ 为零，两个 collar 的边界确实消失。故(23)没有用“低阶”一词遮去非紧尾。

在自由 jets 上定义
$$
\mathfrak T=\partial_v^2-2\partial_u\partial_r.
$$
因为
$\mathfrak T(\Lambda^2)=2(G^2-4aC^\flat)$，有
$$
\boxed{
\mathfrak T\mathscr F_B(x)
=-2\int a_s(G^2-4aC^\flat)\,ds.
}
\tag{24}
$$
迹后的式子已与 profile jets 无关。这是 canonical self 的原式迹，不把响应子空间的另一个 trace 定理直接移植到原路径。

## 6. 主定理：whole self 零后的七余完全局部化

R442 的同一实际对角多项式是
$$
\mathfrak D_V(x)=\mathcal C_{\rm path}(1,x,x^2).
$$
由(11)、(20)、(24)，在(2)的 canonical 两端条件下，
$$
\boxed{
\mathfrak D_V(x)
=\frac12\mathfrak T\mathscr F_B(x)
+4\int kp\,\mathscr R_{\rm loc}\,ds.
}
\tag{25}
$$
若不具备 $a(s_0)=a(s_1)=0$，(25)右边还须保留
$-4[a\mathscr B]$；若也取消 R442 的原跨包周期条件，从原 current 识别到 $\mathcal C_{\rm path}$ 的其他端项同样不能删除。

现在使用真正 universal 的 $\mathcal QV=0$。
式(23)使 $\mathscr F_B$ 作为自由 jet 多项式恒零。一个直接的完整理由如下：取任意固定紧 $u_0,\chi$，
$u_N=u_0+N^{-5/2}\chi\cos Nx$；它在 $C^2$ 中趋于 $u_0$。
除以 $N$ 后，(23)的完整 $C^2$ 余项趋于零，最高项趋于
$\frac12\int\mathscr F_B(x;u_0,u_0',u_0'')\chi^2dx$。
whole self 零迫该积分对全部 $u_0,\chi$ 为零；局部自由二阶 jets 遂迫 $\mathscr F_B$ 恒零。这是纸面极限证明，没有执行任何 profile 或数值序列。

所以在(1)—(3)的实际背景上，
$$
\boxed{
\mathfrak D_V(x)=4\int_{\rm path}
k\,p\left[
-\frac{(1+k^2)p^2}{2h^2}
+\frac{p_s^2}{4h^2}
-\frac{p\,p_{ss}}{2h^2}
+\frac{\gamma p p_s}{2h^3}
+\frac{\gamma^2p^2}{4h^4}
\right]ds,\quad p=\frac{1+(hx+d)^2}{8h}.
}
\tag{26}
$$

(26)是完整值，不只是高阶符号。whole self 的全部 $C^2$ 余项并未被改写成零；它们用于保证上述主项消去的严格性，而(25)已经把 $\mathfrak D$ 本身准确分为迹和局部项。

尤其，$\mathcal QV=0$ 杀掉的是(25)第一项，**并未在本证明中杀掉第二项**。从(24)单独删掉整个 $\mathfrak D$ 会漏掉(21)。

## 7. 一阶速度 action 与真实边界

对(26)中唯一的 $p_{ss}$ 分部一次，保留端值：
$$
\begin{aligned}
\int kp\mathscr R_{\rm loc}\,ds
={}&-\left[\frac{kp^2p_s}{2h^2}\right]_{s_0}^{s_1}\\
&+\int\left[
-\frac{k(1+k^2)p^3}{2h^2}
+\frac{5kp\,p_s^2}{4h^2}
+\frac{k_s p^2p_s}{2h^2}
-\frac{k\gamma p^2p_s}{2h^3}
+\frac{k\gamma^2p^3}{4h^4}
\right]ds .
\end{aligned}
\tag{27}
$$
在同一闭几何的周期 jets 下，括号两端相同；它不要求每端 $p_s=0$。若仅是一段未闭路径，则须保留乘4后的
$-2[kp^2p_s/h^2]$。

置
$$
A=\gamma/h,\qquad v_k=k_s,\qquad
B_x=\frac{p_s}{p}
=\frac{A(e^2+2ke-1)-e v_k}{Q}.
\tag{28}
$$
最后一式使用真实水平条件
$e_s=A(e+k)-v_k/2$；没有把 $d$ 或 $\omega$ 独立冻结。
于是闭路径上(26)等价于
$$
\boxed{
\mathfrak D_V(x)=
\int\frac{p^3}{h^2}
\left[-2k(1+k^2)+5kB_x^2+2v_kB_x-2kAB_x+kA^2\right]ds.
}
\tag{29}
$$
为完全显示其位置多项式性，令
$$
Z_x=A(e^2+2ke-1)-e v_k .
$$
则
$$
\boxed{
\mathfrak D_V(x)=\frac1{512}\int h^{-5}
\left[
-2k(1+k^2)Q^3+5kQZ_x^2
+2v_kQ^2Z_x-2kAQ^2Z_x+kA^2Q^3
\right]ds.
}
\tag{30}
$$
这是原状态与一阶速度的明确 action。$Q$、$Z_x$ 对 $x$ 都至多二次，所以(30)对 $x$ 至多六次；没有保留隐含分母、history 或 primitive。

其系数就是 R439 的七个原余系数。它们的全零条件等价于(30)七个积分逐一为零，仍是同一路径的联合条件，不能逐个另选一个几何后拼接。

## 8. 最高两个真实位置系数

为了与 R439 的完整物理根求值接口对接，记
$$
\mathfrak D_V(x)=\sum_{j=0}^6D_jx^j .
$$
从
$$
p=\frac h8x^2+\frac d4x+\frac{1+d^2}{8h}
\tag{31}
$$
在(27)的积分内逐项取最高两幂即可，无须重新积分或恢复原场。具体只用下表：
$$
\begin{array}{c|ccc}
& p^3 & p\,p_s^2 & p^2p_s\\ \hline
[x^6]&h^3/512&h\gamma^2/512&h^2\gamma/512\\
[x^5]&3h^2d/256&(d\gamma^2+2h\gamma d_s)/256&
(h^2d_s+2hd\gamma)/256
\end{array}
\tag{32}
$$

六次系数的四个速度贡献分别来自
$5kp p_s^2/h^2$、
$2k_s p^2p_s/h^2$、
$-2k\gamma p^2p_s/h^3$、
$k\gamma^2p^3/h^4$。
合并为
$$
\boxed{
D_6=\frac1{256}\int
\left[-kh(1+k^2)+\frac{2k\gamma^2}{h}+k_s\gamma\right]ds
=\frac1{256}\int h\{-k(1+k^2)+2kA^2+Av_k\}\,ds .
}
\tag{33}
$$
五次系数先保 $d_s$ 为
$$
D_5=\frac1{128}\int
\left[
-3k(1+k^2)d+\frac{2kd\gamma^2}{h^2}
+\frac{4k\gamma d_s}{h}
+k_sd_s+\frac{2k_sd\gamma}{h}
\right]ds .
$$
再代原 $d_s=A(d+k)-v_k/2$，得到
$$
\boxed{
D_5=\frac1{128}\int
\left[
-3k(1+k^2)d+(6kd+4k^2)A^2
+(3d-k)Av_k-\frac{v_k^2}{2}
\right]ds .
}
\tag{34}
$$
两式只在本稿显示的闭路、whole-self-zero 范围内直接等于原七余系数；未满足这些前提时，必须恢复(25)的 trace 和(27)的端项。

本文不把 $D_5,D_6$ 自行认作一个正字符，也不声称当前真实 suffix 已能分别读取它们。R439 的实际全部根评价商、原宽度与三矩输运仍是最终使用它们时必须保留的数据。

## 9. $p>0$ 的真实后果及不能推出的符号

在每个固定合法 $x$ 上，(12)给 $p>0$。由 $a_s=kp$ 及 $a$ 两端零，
$$
\int kp\,ds=0.
\tag{35}
$$
对正时长实际零矩路径，[R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)(20)还给
$$
\int k^2ds=L+\int(h_s/h)^2ds>0.
\tag{36}
$$
故 $k$ 在该路径上必须取到正、负两号；不能以 $p>0$ 将 $\int kp\mathscr R_{\rm loc}$ 当作正权能量。

例如静态状态处，(30)的密度是
$-k(1+k^2)Q^3/(256h^5)$，但一段静态状态不是满足(2)—(3)的完整闭路径。其局部符号既不证明实际余值的一号性，也不证明可在保原八矩、第三 hook、whole $E$ 和有序门时独立改动它。

(9)—(10)是两个真实世界向量的动力学，但 $\rho_n$ 由同一几何、同一 $m$ 和原初值决定，不能把它改成独立控制输入。平台矩阵的 $\int\eta_n\rho_m$、本稿 $\int a_np_n\rho_n$ 以及 R196 的严格正成本属于不同的原配对；尚需另一个完整身份才可互相推出零或非零。

## 10. 对当前 full range 问题的准确推进

本稿完成了：

- 一般真实矩模式的世界向量恒等(9)、配对导数(10)及全端项(11)；
- canonical whole self 主项迹与原七余量之间的准确差(25)，其中差项(21)完全局部；
- whole self 为零后的完整局部 action(26)、一阶速度式(30)及最高两系数(33)—(34)。

这些等式适用于当前新 $8\times12$ 母库，也适用于满足相同原几何/成本假设的其他真实输入；它们不依赖某个母的对称性或有限差分消项。

当前尚未由(1)—(3)证明(30)为零，也未证明可以在同一实际路径上任意指定其七个值。若其某项非零，还须通过 R439 的真实全部根与 suffix 求值商才能形成该固定圆的障碍；若其七项为零，也仍须支付 self 通道、原 $L_f$ 的全部 range 及同一十三行规范，不能把本 current 子问题当作整个 period。

下一准确入口因此是同一原路径的七个局部积分，而不再是未知第三 $\beta$ 或任意重锚的二阶 history。任何拟用原响应改变它的论证，仍须保 whole $E/J^+$、同一 prototype 与全部基准成本；本稿没有把已算 144 响应的核升级为完整 $\mathcal R$。
