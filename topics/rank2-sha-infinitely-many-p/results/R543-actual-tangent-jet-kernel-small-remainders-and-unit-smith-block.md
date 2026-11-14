# R543 — 原切向物理核的两层小余量与真实单位 Smith 块

日期：2026-11-14。**状态：已证明。** 本篇将 R537 的来源核推进到原
\(J\)、\(M\) 的真实有限评价。若一个已付切向返回在原首位中为零，
其在原因子曲线上的限制必须高阶等于一个常数；
剥去这个值层后，同一正镜轴又限制下一层。
由此得到两个准确线束控制的额外物理核，且保原十三行 carry。

在显示的强窗口，这两个线束都负度，所以切向限制的每个非零
Smith 因子确为单位。这次是**物理评价后**的断言。
在此前满主阶低 \(\ell\) 临界窗中，即使强窗口略有缺口，
Clifford 界仍把额外物理核压到至多
\(b^2/64+O(b)\) 个来源方向。
所有结论条件于同一个实际因子、真实接触和已付返回预算；
没有给切向列新增中央零。

## 1. 原低 ell、同一返回及两种真实长度

保 R495、R498、R502、R517、R537 的同一实际对象，特别
$$
p=6s-1>83,\qquad
1\le\ell\le r<h,\qquad
k=2h+r-s,\qquad 0\le k<\ell,
$$
$$
S=s-r=2h-k,\qquad
\eta=\log(g/\psi)\bmod t^S,\qquad
\operatorname{ord}_P\eta=h,\qquad \eta^2=0\bmod t^S.
\tag{1}
$$
\(F\in k[t,Y]\) 为几何不可约原因子，\(C\subset X\)、
\(\kappa=C^2\)、\(\chi=-K_XC\)、\(\mathcal H_2=H^0(X,\mathcal O_X(2C))\)
均不改变。

使用 R517 的
$$
\mathcal T_2(H)=d^{-C_D}t^rQ\,
Y^2t(t-1)^2h_7^2\,\mathcal V_FH
\tag{2}
$$
或 R521 的
$$
\mathcal T_3(H)=d^{-C_D}t^rQ\,
Y^3t(t-1)^2h_7^3d^2\,\mathcal V_FH.
\tag{3}
$$
必须保其两个、三个 charge 的原返回成本。
若没有同 \(D\) 余量，就使用已经扩大的实际矩阵；
不把新列免费加入旧矩阵。

二者的非 \(t\) 前缀在 \(P\) 都为单位，且相差完整物理单位
\(Yh_7d^2\)。
对相对 \(J\) 与整个原 \(M\)，定义
$$
\boxed{
T_J=s-r-1,\qquad
T_M=s-r-14.
}
\tag{4}
$$
以下只在相应 \(T>0\) 时使用非平凡界。
(1) 保 \(T\le S\)、\(T<p\)。

**长度核对。** 相对评价 (2) 有 \(t^{r+1}\) 前缀。
其第三块被 \(\ell\le r\) 全部杀掉，
余下前两块准确长 \(s-r-1\)。
对
$$
M=c_*U_0m_{13}J,
$$
剥完整整单位后前缀是 \(w^{13}t^{r+1}\)，
即 \(t^{r+14}\) 乘原参数单位。
原第三块长 \(\ell+13\)，仍被该前缀杀掉；
前两块准确长 \(s-r-14\)。

所以 (4) 保留了原全部十三行差异，
并非先以非整方式消去 \(m_{13}\)。
\(P_{134}/U_0\)、\(Q\) 的径向项和原 Gaussian 都以完整目标单位运输。
式 (3) 得到相同长度。

## 2. 原 rational F 的有效极除子

在 \(X\) 上把原多项式 \(F(t,Y)\) 看作有理函数，定义边界除子
$$
\mathscr D=C-\operatorname{div}_X(F).
\tag{5}
$$
因此 \(\mathscr D\sim C\)，且来源
\(\mathcal H_j=H^0(X,\mathcal O_X(jC))\) 的原多项式表示
准确等于
$$
H^0(X,\mathcal O_X(j\mathscr D)).
\tag{6}
$$
这里用 \(\operatorname{div}F=C-\mathscr D\) 运输平凡化；
没有把 \(F\) 当来源中的可逆元。

记 \(d=0,Y=0\) 两次吹起的实际重数为
\(\mu_{d,1},\mu_{d,2}\)，相应严格例外曲线为 \(E_{d,1}',E_{d,2}\)。
R495/R537 的逐链值给
$$
v_{d,1}=\mu_{d,1},\qquad
v_{d,2}=\mu_{d,1}+\mu_{d,2}.
$$
置
$$
Z=v_{d,1}E_{d,1}'+v_{d,2}E_{d,2},\qquad
D_+=\mathscr D+Z.
\tag{7}
$$

**引理 1。** \(D_+\) 是有效除子，\(Z\) 正是 \(\mathscr D\) 的负部；
二者的支持不相交，也均不经过 \(P=(0,1)\)。
而且
$$
\boxed{
K_+:=\deg_C(D_+|_C)
=\kappa+\mu_{d,1}^2+\mu_{d,2}^2.
}
\tag{8}
$$

**证明。** 在原 \(\mathbb F_4\) 上，\(F\) 的极除子是
\(bS_\infty+uF_\infty\)，其中 \(u\ge0\)。
在有限 \(Y=\infty\) 各链及无穷远链上，
R537(17)–(18) 已逐步给出 \(v(F)\le0\)；
所以这些例外曲线在 \(\mathscr D\) 中的系数非负。
唯一可能的正 \(v(F)\) 是 \(d=0,Y=0\) 的两条例外曲线，
其值就是 (7) 中所写。故负部准确为 \(Z\)。

\(d=0,Y=0\) 的吹起邻域与原极除子及其他吹起中心不相交，
所以 \(Z\) 与 \(D_+\) 的支持确实不相交。
这一点使后文“非常数零条件排除非零常数”合法，
不能只以抽象正负部的名称替代。

普通吹起交数给
$$
CE_{d,1}'=\mu_{d,1}-\mu_{d,2},\qquad
CE_{d,2}=\mu_{d,2}.
$$
所以
$$
CZ=\mu_{d,1}(\mu_{d,1}-\mu_{d,2})
+(\mu_{d,1}+\mu_{d,2})\mu_{d,2}
=\mu_{d,1}^2+\mu_{d,2}^2.
$$
再用 \(C\mathscr D=\kappa\)，得 (8)。证毕。

若 \(F(-1/8,0)\ne0\)，则 \(Z=0\)、\(K_+=\kappa\)。
若 \(F(-1/8,0)=0\)，则 \(CZ>0\)。
因此 (6) 中 \(j=1,2\) 的限制截面在 \(Z|_C\) 有指定正零阶，
而 \(D_+|_C\) 在这里没有极；
一个非零常数不可能属于这些限制空间。

## 3. 两个 Gaussian 行先控制真实值层

令 \(\mathcal K_T\subset\mathcal H_2\) 为所选
\(\bar J\,\overline{\mathcal T_i}\) 或
\(\bar M\,\overline{\mathcal T_i}\) 的实际核；
使用 (4) 中对应的 \(T\)。

取 \(H\in\mathcal K_T\)，令 \(G=\mathcal V_FH\)。
剥第1节的完整单位及已知 \(t\) 像后，
准确条件是
$$
G(t,g e^{a\epsilon})=0
\quad\text{于 }k[[t]][\epsilon]/(t^T,\epsilon^2).
\tag{9}
$$
因 \(a\) 为单位，这等价于同一个普通值和 Euler 导数均消到 \(T\)：
$$
G(t,g)=0\bmod t^T,\qquad
(\mathcal EG)(t,g)=0\bmod t^T.
\tag{10}
$$
没有另加自由的法向输出。

由于 \(\eta^2=0\bmod t^T\)，同一正规 Taylor 展开给
$$
G(t,\psi)=G(t,g)-\eta(\mathcal EG)(t,g)=0\bmod t^T.
\tag{11}
$$
在曲线 \(C\) 上，R517 的切向恒等式是
$$
(\mathcal V_FH)|_C=e\,t\frac d{dt}(H|_C),\qquad
e=(\mathcal EF)|_C,\qquad e(P)\ne0.
\tag{12}
$$
于是
$$
\boxed{H|_C-H(P)=0\bmod t^T.}
\tag{13}
$$
这里 \(T<p\)，所以 \(t\partial_t\) 在次数
\(1,\ldots,T-1\) 上的系数都是单位；
没有使用超出原 \(s\) 阶的 ODE。

由 (6)–(8)，(13) 中的函数准确属于
$$
\boxed{\mathcal L_2(T)=\mathcal O_C(2D_+-TP),\qquad
\deg\mathcal L_2(T)=2K_+-T.}
\tag{14}
$$
当 \(Z>0\) 时，\(H|_C\mapsto H|_C-H(P)\) 在其值像上单射：
其核若是常数，必须由 \(Z|_C\) 的零条件变成零。
当 \(Z=0\) 时，核准确是 \(k\cdot1\)，这正是 R537 的真实来源核之一。

## 4. 剥同一个值层后，仍是原正镜轴

若 \(H|_C=0\)，则由原线束限制准确有
$$
H=F H_1,\qquad H_1\in\mathcal H_1.
\tag{15}
$$
这使用同一个 \(H\)；
不是在环境多项式环中选择另一个修正。
又因 \(\mathcal V_FF=0\)，
$$
\mathcal V_FH=F\,\mathcal V_FH_1.
$$

令 \(G_1=\mathcal V_FH_1\)，
在原正规坐标 \(\zeta=\log(Y/\psi)\bmod F^3\) 中写
\(G_1=g_0+\zeta g_1+\zeta^2g_2\)。
(9) 中 \(F/\zeta\) 是一个整单位，
且 \(\zeta=\eta+a\epsilon\)、\(\zeta^3=0\)。
因此 \(FG_1=0\) 准确等价于
$$
g_0+2\eta g_1=0\bmod t^T.
$$
第一分量 \(\eta g_0\) 由这个式子及 \(\eta^2=0\) 自动为零。
所以仍是指定的原正镜轴：
$$
\boxed{
G_1(t,\psi e^{2\eta})=0\bmod t^T.
}
\tag{16}
$$
这只在第1节的实际高像中使用三厚化；
未在原 raw \(\bar\Gamma\) 中删除 R502 的活 \(\zeta^3\)。

置
$$
H_T=\min(h,T).
$$
式 (16) 使 \(G_1|_C\) 至少消到 \(H_T\)。
再用 (12) 于 \(H_1\)，得到
$$
\boxed{
H_1|_C-H_1(P)\in
\mathcal L_1(H_T):=\mathcal O_C(D_+-H_TP).
}
\tag{17}
$$
其次数是 \(K_+-H_T\)，且 \(H_T<p\)。

限制 \(\mathcal H_1\to H^0(C,\mathcal O_C(\mathscr D))\)
的核准确为 \(kF\)，对应 (15) 中的 \(kF^2\)。
若 \(Z=0\)，还有真实常数 \(H_1=1\)，对应 \(H=F\)；
若 \(Z>0\)，这个常数方向被同一边界零条件排除。
这和 R537 的两种核完全一致。

## 5. 真实额外物理核的两层上界

令
$$
\varepsilon_F=
\begin{cases}
1,&F(-1/8,0)=0,\\
3,&F(-1/8,0)\ne0.
\end{cases}
$$
继续保 R537 的
\(p>8b^2+4bu\)，则来源切向核的维数准确为 \(\varepsilon_F\)，
来源返回也 \(p\) 饱和。
以下 jet 推导本身只用 \(T<p\)；
这里保较强门是为直接调用同一来源商格。

**定理 1。** 对原 \(J\) 或原 \(M\) 的相应 \(T\)，
$$
\boxed{
\dim\mathcal K_T-\varepsilon_F
\le h^0(C,\mathcal L_2(T))
+h^0(C,\mathcal L_1(H_T)).
}
\tag{18}
$$
更具体地，左侧实际额外核具有两层过滤，
其商分别单射到 (14)、(17) 的截面空间。

**证明。** 先按 \(H\mapsto H|_C\) 过滤 \(\mathcal K_T\)。
第3节控制其像；常数方向在 \(Z=0\) 时扣除一维，在 \(Z>0\) 时不存在。
其核由 (15) 表示，再按 \(H_1\mapsto H_1|_C\) 过滤。
第4节控制这个像；同样只在 \(Z=0\) 时多一维常数。
最后始终剩一维 \(kF^2\)。
三份来源关系总数正是 \(\varepsilon_F\)，得到 (18)。证毕。

(18) 不是两个小线束的直和或满射断言；
同一 \(H\) 和镜轴仍把它们联系起来。
这使它可作为额外物理核的上界，而不能据其维数任意补修正。

最直接的数值版是
$$
\boxed{
\dim\mathcal K_T-\varepsilon_F
\le (2K_+-T+1)_+
+(K_+-H_T+1)_+,
}
\tag{19}
$$
其中 \(x_+=\max(x,0)\)。
这里用了整曲线上 \(h^0(L)\le\max(0,\deg L+1)\)。

## 6. 原积分矩阵中的单位块与强窗口

记
$$
R_{\rm tan}=1+2\kappa+\chi-\varepsilon_F
$$
为 R537 的准确来源秩，并令
$$
B_T=h^0(\mathcal L_2(T))+h^0(\mathcal L_1(H_T)).
$$
在角和次数保持的同一整提升上，(18) 给
$$
\boxed{
\operatorname{rank}_k(\bar J\,\overline{\mathcal T_i})
\ \text{或}\
\operatorname{rank}_k(\bar M\,\overline{\mathcal T_i})
\ge R_{\rm tan}-B_T.
}
\tag{20}
$$
因此相应**实际整限制矩阵**至少有
\(\max(0,R_{\rm tan}-B_T)\) 个单位 Smith 因子。
去掉 R537 已知的 \(\varepsilon_F\) 个零列后，
至多 \(B_T\) 个来源方向还可能产生非单位或零因子。
本断言不需要预先假定特征零物理满列秩。

特别，若
$$
\boxed{T>2K_+,\qquad h>K_+,}
\tag{21}
$$
则两个线束都负度，\(B_T=0\)，故

**定理 2。**
$$
\boxed{
\mathcal K_T=\ker\overline{\mathcal T_i},
\quad
\text{相应原物理限制的全部 }R_{\rm tan}
\text{ 个非零 Smith 因子都是单位。}
}
\tag{22}
$$
此时其像是原整目标中的饱和子格。
证明是 (18) 加上真实有限矩阵的 Smith 形式：
模 \(p\) 已有完整来源商秩，
故没有余下的非单位因子，也没有额外特征零核。

对原 \(M\)，(21) 明确读为
$$
\boxed{s-r-14>2K_+,\qquad h>K_+.}
\tag{23}
$$
对相对 \(J\)，十四换成一。
这些是不同的充分窗；没有把相对 \(J\) 的结论直接赋给原 \(M\)。

这次像饱和来自 (9)–(18) 的真实物理核计算，
不是从 R537 的来源饱和直接推断。

## 7. 一个含证明的更强截面维数界

\(C\) 是整 Gorenstein 曲线，算术亏格
$$
g_C=1+\frac{\kappa-\chi}{2}.
$$
对任一线束 \(L\) 的次数 \(d\)，可以使用
$$
\mathfrak b_g(d)=
\begin{cases}
0,&d<0,\\
\lfloor d/2\rfloor+1,&0\le d\le2g-2,\\
d+1-g,&d\ge\max(0,2g-1).
\end{cases}
\tag{24}
$$
准确有 \(h^0(L)\le\mathfrak b_g(d)\)。

为明确奇异曲线上的适用性，给出所需 Clifford 证明。
若 \(a=h^0(L)>0\)、\(b=h^1(L)>0\)，Serre 对偶把
\(b\) 写为 \(h^0(\omega_C L^{-1})\)。
在一个光滑点选按消失阶适配的两组基。
两个阶集合的和集至少有 \(a+b-1\) 个元素，
相应乘积截面有不同消失阶，所以在 \(H^0(\omega_C)\) 中线性独立。
于是 \(g\ge a+b-1\)。
结合 Riemann–Roch 的 \(a-b=d+1-g\)，得到
\(a\le d/2+1\)。
若 \(h^1(L)=0\)，Riemann–Roch 直接给 \(a=d+1-g\)，
在中间次数范围也不超过 (24)。
当 \(d>2g-2\) 时对偶线束负度，得到最后一行。
这只使用整曲线、光滑点和 Gorenstein 对偶；不假定 \(C\) 处处光滑。

所以 (18) 的完全显式强化为
$$
\boxed{
\dim\mathcal K_T-\varepsilon_F
\le
\mathfrak b_{g_C}(2K_+-T)
+\mathfrak b_{g_C}(K_+-H_T).
}
\tag{25}
$$

## 8. 满主阶低 ell 窗中至多 b²/64 个额外方向

本节逐个考虑**已经存在**的实际候选，并明确假设
$$
D=3b,\quad u=b+O(1),\quad
\kappa=\frac{47}{12}b^2+O(b),\quad \chi=O(b),
$$
$$
\mu_{d,1}^2+\mu_{d,2}^2=\frac12b^2+O(b),\qquad
r,\ell,k=O(b),
$$
$$
2s+\ell=\dim\mathcal W_{3b}+O(b),\qquad
\dim\mathcal W_{3b}=\frac{141}{8}b^2+O(b).
\tag{26}
$$
若使用 (2) 或 (3) 的扩大预算，固定两个、三个 charge 只改变这些式子的 \(O(b)\) 项；
这不等于旧矩阵的来源已经扩大。

由 (1)、(8)、(26)，
$$
K_+=\frac{53}{12}b^2+O(b),\quad
h=\frac{141}{32}b^2+O(b),\quad
T_J,T_M=\frac{141}{16}b^2+O(b).
$$
两份小余量准确为
$$
\boxed{
2K_+-T=\frac1{48}b^2+O(b),\qquad
K_+-H_T=\frac1{96}b^2+O(b).
}
\tag{27}
$$
它们比
\(2g_C-2=\frac{47}{12}b^2+O(b)\)
小，故最终都处于 (24) 的 Clifford 范围。
因此
$$
\boxed{
\dim\mathcal K_T-\varepsilon_F
\le\frac1{64}b^2+O(b).
}
\tag{28}
$$
相应实际限制至少有
$$
\boxed{
\left(\frac{47}{6}-\frac1{64}\right)b^2+O(b)
=\frac{1501}{192}b^2+O(b)
}
\tag{29}
$$
个单位 Smith 因子。
这里用的是整个实际 \(J\) 或 \(M\) 中已付的切向子来源，
不是多项式返回前的秩。

在这个具体主阶中，
\(h-K_+=-\frac1{96}b^2+O(b)\)。
所以强窗 (21) 一般尚未成立；
(28) 不能擅自改成额外核为零。
若实际 \(\mu_d\) 或接触使 (21) 严格成立，
则应直接使用 (22)，不保留多余的粗界。

## 9. 对 forcing、两连接和完整中央的准确作用

R537 先识别了切向返回本身的全部来源关系。
本篇再把其余物理关系注入 (14)、(17) 两个小线束，
给真矩阵的单位块与剩余方向上界。
这些限制可直接用于 R524 的两连接及 R521 的边界测试，
而不需补自由 normal 数据或来源列。

尚须计算的是：原 forcing 在这同一实际像及其余原列的商中是否非零。
R521 的显示边界残数仍须杀
\(\operatorname{res}H^0(3C,\mathscr I_\eta L_c)\)；
(18) 的两个小线束并未自动证明那个杀灭条件。
R502 的实际 \(\xi\)、活 \(V_1\)、两条 carry 与低行高尾也均未删去。

原 \(M\) 的比较已经通过 (4)、(23) 保了十三行差异；
进入第二、第三精度仍使用 R479/R481 的同一个修正和原
\(d_2/G_2\)，不能只用单位块以外的环境尾。
三条原完整中央仍只属于原 \(S,T,U\)。
本篇没有把它们传播到 \(\mathcal T_i(H)\)，也没有由有限秩界宣称跨素数非零。
