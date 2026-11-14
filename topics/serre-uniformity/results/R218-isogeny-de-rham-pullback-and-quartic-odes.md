# R218：由de Rham初值恢复全部同源四阶模型

**状态：已证明并已完整实算。** 对模47光滑、次数与47互素的正规化同源，源模型、目标常数模型及一个de Rham初值唯一决定所需四阶目标模型。方程只含三个标量未知量；不再为每个大素数核重复提升整个核商代数。两条实际源曲线各3326个DAG节点的全部系数已写入压缩证书。

## 1. 真实de Rham拉回中的第三个初值

令 $E:y^2=f(x)=x^3+Ax+B$，并取

$$\omega=\frac{dx}{2y},\qquad\eta=x\frac{dx}{2y}.$$

这给光滑短Weierstrass曲线的de Rham基。设 $\phi:E\to E'$ 是次数 $n$ 的正规化同源，即 $\phi^*\omega'=\omega$。则有唯一的标量 $u$ 使

$$\boxed{\phi^*[\eta']=n[\eta]-u[\omega].} \tag{218.1}$$

对奇素数Vélu核 $h(x)$，令 $s_1$ 为 $h$ 的根之和。R209的横坐标公式给准确微分恒等式

$$\phi_x\omega=(n x-2s_1)\omega-2d\left(y\frac{h'}h\right).$$

因此 $u=2s_1$。对二阶核根 $r$，同样有

$$\phi_x\omega=(2x-r)\omega-d\left(\frac{y}{x-r}\right),$$

所以 $u=r$。这些不是以KS比例猜出的常数；精确有理微分给出了其值和符号。

若先作次数 $n_1$、初值 $u_1$ 的同源，再作次数 $n_2$、初值 $u_2$ 的同源，则拉回式直接给

$$\boxed{n=n_1n_2,\qquad u=n_2u_1+u_2.} \tag{218.2}$$

故R209的常数核DAG能逐父节点求出每个复合同源的全局初值 $u_0$；不需要复合核多项式本身。

## 2. 带准确符号的Gauss–Manin联络

令源系数依赖参数 $t$，记点为 $d/dt$，$\Delta=4A^3+27B^2$。有

$$\nabla\omega=a\omega+b\eta,\qquad
\nabla\eta=c\omega-a\eta,$$

其中

$$\boxed{a=-\frac{A^2\dot A+\frac92B\dot B}{\Delta},\quad
b=\frac{\frac92B\dot A-3A\dot B}{\Delta},\quad c=\frac{A b}{3}.} \tag{218.3}$$

特别最后一式的符号是正号。

这里给出可直接检验的完整约化。记

$$H_1=-\frac{9Bx^2+2A^2x+6AB}{2\Delta},\qquad
H_2=\frac{6Ax^2-9Bx+4A^2}{2\Delta},$$
$$H_3=\frac{-2A^2x^2+3ABx+9B^2}{2\Delta}.$$

在固定 $x$ 的微分提升下，逐项求导有

$$\partial_A\omega=-\frac{A^2}{\Delta}\omega+\frac{9B}{2\Delta}\eta+d(H_1/y),$$
$$\partial_B\omega=-\frac{9B}{2\Delta}\omega-\frac{3A}{\Delta}\eta+d(H_2/y),$$
$$\partial_A\eta=\frac{3AB}{2\Delta}\omega+\frac{A^2}{\Delta}\eta+d(H_3/y),$$
$$\partial_B\eta=-\frac{A^2}{\Delta}\omega+\frac{9B}{2\Delta}\eta+d(H_1/y).$$

这些等式只需用 $y^2=f$ 和
$d(H/y)=(H'f-Hf'/2)dx/y^3$ 展开即可逐系数核对。删去恰当微分并按 $\dot A,\dot B$ 合并，就得到(218.3)。证明未依赖一个未经核准的联络约定。

## 3. 正规化同源的三变量方程

下标 $s,t$ 分别表示源、目标，源的 $A_s,B_s,a_s,b_s,c_s$ 都已知。对(218.1)应用联络的函子性，并比较 $\omega_s,\eta_s$ 的系数，得到

$$b_t=b_s/n,\qquad a_t=a_s+(u/n)b_s,$$

$$\dot u=n c_s-c_t-(a_s+a_t)u. \tag{218.4}$$

把目标联络的前两式反解为目标模型的导数，得到完整闭合系统

$$\boxed{\begin{aligned}
\dot A_t&=-4A_t\left(a_s+\frac{u b_s}{n}\right)+6B_t\frac{b_s}{n},\\
\dot B_t&=-6B_t\left(a_s+\frac{u b_s}{n}\right)-\frac43A_t^2\frac{b_s}{n},\\
\dot u&=b_s\left(\frac{nA_s}{3}-\frac{A_t}{3n}-\frac{u^2}{n}\right)-2a_su.
\end{aligned}} \tag{218.5}$$

例如源 $A_s=-1,B_s=t$、二阶核初值 $r=0$ 时，目标初值为 $A_t=4,B_t=0,u=0$。此时 $b_s(0)=-3/4$，所以(218.5)给 $\dot u(0)=1$、$\dot B_t(0)=8$，与真正核根 $r(t)=t+t^3+O(t^5)$ 的Vélu公式一致。这也直接检测了(218.3)中容易写错的符号。

## 4. 为什么所得四阶解就是实际同源变形

工作于 $R=(\mathbb Z/47^4)[i]$。固定源光滑族及常数纤维的一条与47互素的有限étale核。有限étale概形沿幂零加厚唯一提升，所以核唯一提升到所需形式邻域，其商和正规化同源也实际存在。可等价地先在未分歧47进整数环上提升，再逐项约化。

这个实际同源变形必满足(218.5)，并具有已算出的 $A_t(0),B_t(0),u(0)$。反过来，若三个未知级数已知到 $t^k$，方程右侧的 $t^k$ 系数就唯一决定左侧的 $(k+1)$ 次系数。为了求到 $t^4$，只需除以 $1,2,3,4$；它们以及 $n,\Delta_s(0)$ 都是47进单位。

因此通过四阶的解唯一，程序算出的系数必等于实际核变形的Vélu模型。此论证没有宣称在模 $47^4$ 下对任意高阶都能继续无条件除以 $k+1$；本文只使用严格需要的四阶。

每个节点直接以原始源作为 $s$，使用该节点的累积次数 $n$ 和(218.2)的 $u_0$。这样无需将误差或参数尺度沿一条长链猜测传播。源9实际参数是 $A_s=1,B_s=32+t$；CM4源是 $A_s=-1,B_s=t$。后者在R208的椭圆粗盘中的不变量是 $u_{\rm coarse}=B_s^2/A_s^3=-t^2$，不能与本篇de Rham系数 $u$ 混淆。

## 5. 实际运行、完整数据和独立比较

`scripts/p41_isogeny_gauss_manin47.py` 对两源降序DAG各3326节点，保存目标 $A_t,B_t$ 及de Rham系数 $u$ 的0至4次系数。全部运算在 $R$ 内精确执行；每个节点又核对(218.4)的所有0至3次系数以及

$$n\frac{2A_t\dot B_t-3B_t\dot A_t}{4A_t^3+27B_t^2}
=\frac{2A_s\dot B_s-3B_s\dot A_s}{4A_s^3+27B_s^2}.$$

这里只声称这些微分关系核到 $t^3$；四阶模型求导后只能提供到三阶，不虚报更高系数。

完整文件为

- `scripts/data/p41_source_j9_descending_gauss_manin_quartic47.json.gz`；
- `scripts/data/p41_CM4_descending_gauss_manin_quartic47.json.gz`。

每份记录常数DAG和两个源程序的SHA256、全部节点和已完成计数。数据在进一步比较前已原子写入磁盘。

独立的隐式方法在 $R[x]/h\,[t]/t^5$ 中使用真实除法多项式，先对横坐标求导再约化，以三轮Newton得到 $x(t)$，取 $x,x^2,x^3$ 的迹后套Vélu公式。两源各对全部2、3、4、6次分支及一条43、89次分支执行此方法，共27条，目标 $A_t,B_t$ 的五个系数全部与(218.5)一致。这个比较不由同一微分方程重复生成期望值。

源9初次3326节点的ODE运行用时2.369秒；随后独立大素数比较约两分钟。运行时间只描述本环境，不作为数学结论。比起逐节点的大核隐式提升，三变量系统消去了重复的大代数运算。

~~~bash
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=scripts \
python scripts/p41_isogeny_gauss_manin47.py \
  --constant-dag scripts/data/p41_source_j9_descending_kernel_dag47.json.gz \
  --output scripts/data/p41_source_j9_descending_gauss_manin_quartic47.json.gz \
  --direct-checks
~~~

将文件名中的 `source_j9` 换为 `CM4` 即重建另一源。R209保存常数输入；R206/R208/R216负责真实水平结构与第三类微分的局部原函数。本文只完成实际目标模型的四阶接口，不据此宣称全部高度、全部QC根或Serre绝对一致性已完成。
