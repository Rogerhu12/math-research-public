# R129：九级固定扭曲的全部有理点及九次幂分母支的明确排除

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：已证明，附完整标准库有限环证书。** 对 R120 的固定曲线
$$\mathcal C:\quad y_C^2=S(x)=7x^6+12x^5-36x^4-10x^3+84x^2-72x+19,$$
有
$$\boxed{\mathcal C(\mathbb Q)=\{(-1,12),(-1,-12),(1,2),(1,-2)\}.}\tag{129.1}$$
证明使用 R126 的唯一三次域覆盖、R127 的准确秩一，以及一个只需模 $5^4$ 运算的 elliptic Chabauty 证书。全部六个模五剩余盘均被处理；没有假定已知非挠点生成完整 Mordell–Weil 格。

由 R114、R120 的实际模九挠点接口，这明确排除 R19 的非 CM 实际曲线中 $Z\in\mathbb Q^{\times9}$ 的整个分支。更一般的非九次幂分母仍不在本定理的结论内。

## 1. 实际覆盖和明确对数方向

沿用 R126、R127 的记号
$$L=\mathbb Q(r),\qquad r^3-3r-4=0,\qquad\epsilon=r^2+r-7,$$
$$
\begin{aligned}
B(x)={}&(3r^2-5r-3)x^4+(2r^2-r-6)x^3\\
&+(-9r^2+18r+3)x^2+(6r^2-17r+6)x-r^2+5r-3.
\end{aligned}
$$
R126 证明每个 $\mathcal C(\mathbb Q)$ 点都提升到
$$\mathcal D:\quad\epsilon b^2=B(x),\qquad x\in\mathbb Q,\ b\in L.$$
其证明包含齐次分母和唯一单位平方类，因此这里不是只提升整点。令 $y=\epsilon b$、$f=\epsilon B$，则 $y^2=f(x)$。

R127 定义
$$\mathcal E:\quad Y^2=(X-e_1)(X-e_2)(X-e_3)=X^3+A_4X+A_6,$$
其中
$$
\begin{aligned}
e_1&=82-17r^2,\quad e_2=7-12r+4r^2,\quad e_3=-89+12r+13r^2,\\
A_4&=-7779-120r+1668r^2,\\
A_6&=156958-49320r-10092r^2.
\end{aligned}
$$
设 $H=4ff''-3(f')^2$、$G=f'H-fH'$。R127 已完整核验实际四次映射
$$
\psi(x,b)=\left(-\frac H{12f},\frac G{24y^3}\right),\qquad y=\epsilon b,
\tag{129.2}
$$
以及其准确微分
$$\psi^*\omega=\frac{dx}{y},\qquad\omega=\frac{dX}{2Y}.\tag{129.3}$$
(129.3) 是有理微分恒等式，并在光滑曲线上延拓。特别是在 $x=1$ 的像为二挠点、公式中 $Y=G=0$ 时，仍使用约分后正则的 $dx/y$；没有在该点将未约分的 $0/0$ 当作数值求值。

把所选原点的像二挠点 $T_2=(e_2,0)$ 平移掉才是一条原点保持的同源；在对数计算中这个平移为零。

R127 还证明
$$\operatorname{rank}\mathcal E(L)=1,$$
并给非挠点
$$P=\left(19-108r+\frac{181}4r^2,
\frac{2907}2+\frac{14625}8r-1134r^2\right).\tag{129.4}$$
$P$ 是 $\mathcal D$ 上 $x=-1,b=r^2+4r+1$ 的像；$x=1,b=r^2+2r+1$ 映为 $T_2$。

令 $L_5=\mathbb Q_5(r)$。五在 $L$ 惰性，故 $L_5/\mathbb Q_5$ 不分歧三次，整数基仍为 $1,r,r^2$。对每个 $Q\in\mathcal E(L)$，秩一给
$$\log_{\mathcal E}(Q)\in\mathbb Q_5\log_{\mathcal E}(P).\tag{129.5}$$
这里无需知道 $\langle P,\mathcal E(L)_{\rm tors}\rangle$ 的整数指数：对任意 $Q$，总有非零整数 $m$ 和整数 $n$ 使 $mQ-nP$ 为挠点，取对数再除以 $m$ 即可。后面的枚举也不会将这个有限指数子群的剩余类误当成全部剩余类。

## 2. 所有五进盘，只有三个横坐标类

$S$ 的判别式与五互素，所以 $\mathcal C$ 在五好约化。直接计数得到
$$\mathcal C(\mathbb F_5)=\{(0,\pm2),(1,\pm2),(-1,\pm2)\}.$$
没有无穷点，因为首项系数 $7\equiv2\pmod5$ 不是平方。

也可直接排除任何遗漏的非整横坐标：若 $v_5(x)<0$，则
$$S(x)/x^6\equiv7\pmod5,$$
不可能是平方。因此任意 $\mathcal C(\mathbb Q_5)$ 点均有整横纵坐标，且
$$x\equiv0,1,-1\pmod5.$$

在每个这样的横坐标盘，$f(x)$ 是五进单位，$y^2=f(x)$ 的两个局部分支由 Hensel 引理唯一确定。$b$ 反号使 (129.2) 的像变成其负点，对数和 (129.3) 的导数都反号。因此处理每个横坐标盘的一个分支就同时处理另一个分支。不存在通过任意选择平方根遗漏一半全局点的问题。

## 3. 只在模 $625$ 的整数环中计算真实对数

根差的范数只含二、三，故 $\mathcal E$ 在五好约化。也可直接看三个根在基 $1,r,r^2$ 下的模五坐标为 $(2,0,3),(2,3,4),(1,2,3)$，两两不同。程序完整枚举 $\mathbb F_{125}$ 的 $125$ 个元素和平方，得到
$$\boxed{\#\mathcal E(\mathbb F_{125})=140.}\tag{129.6}$$
所以任意 $Q\in\mathcal E(L_5)$ 的 $[140]Q$ 都在形式群中。

### 3.1 形式对数的准确误差

在短模型中取 $t=-X/Y$。有
$$\omega=(1+2A_4t^4+3A_6t^6+\cdots)\,dt,$$
其中括号内全部系数均在 $\mathcal O_{L_5}$。于是当 $v_5(t)\ge1$ 时
$$\log_{\widehat{\mathcal E}}(t)-t\in5^4\mathcal O_{L_5}.$$
完整尾界来自积分后的每一项：首个非线性次数至少五，而
$$n-v_5(n)\ge4\qquad(n\ge5).$$
因此
$$
\boxed{\log_{\mathcal E}(Q)
\equiv\frac{t([140]Q)}{140}\pmod{125\mathcal O_{L_5}}.}
\tag{129.7}
$$
这里明确损失一位五进精度，因为 $v_5(140)=1$。没有将模 $125$ 的形式参数直接除以五。

### 3.2 射影运算没有另外的精度损失

计算全部在
$$R=\mathcal O_L/625\mathcal O_L\simeq(\mathbb Z/625)[r]/(r^3-3r-4)$$
中进行。椭圆倍点和加点采用 Jacobian 射影坐标 $(U,V,W)$，仿射坐标为 $(U/W^2,V/W^3)$。程序对每一步验证：

- 射影点满足完整椭圆方程；
- 三坐标在模五后不同时为零，故没有未经处理的公式基点或公共非单位因子；
- 所有求逆的元素范数都与五互素。

最终 $[140]Q$ 的 $V$ 是单位，故
$$t=-UW/V$$
仍可在 $R$ 中求出。三个坐标系数都被五整除后，按整数代表除以五，正好得到模 $125$ 的 $t/5$；再乘 $28^{-1}$。因此唯一的精度损失就是 (129.7) 中已说明的那一位。

程序另在 $\mathcal O_L/5^8$ 从头重算，全部输出一致；正确性依据是上述有限环和形式尾界，重复计算作为交叉验证。

### 3.3 两个明确对数

均按基 $1,r,r^2$ 写坐标。计算给
$$
\begin{array}{c|c|c}
Q&t([140]Q)/5\pmod{125}&\log_{\mathcal E}(Q)\pmod{125}\\\hline
P&(60,116,47)&(20,22,24)\\
Q_0&(40,73,6)&(55,16,27).
\end{array}
\tag{129.8}
$$
其中 $Q_0=\psi(0,b_0)$，而 $y_0=\epsilon b_0$ 选为满足
$$y_0^2=f(0),\qquad y_0\equiv2r+2r^2\pmod5$$
的唯一 Hensel 根。它的实际模 $125$ 值为
$$y_0\equiv105+57r+102r^2\pmod{125}.$$
它只是在 $L_5$ 中选择的盘中心，不被宣称属于 $L$。相反，$P$ 确为上面的全局非挠点。

## 4. 两个全局消失的线性式

写实际对数
$$\log_{\mathcal E}(P)=\lambda_0+\lambda_1r+\lambda_2r^2,$$
则 (129.8) 给
$$\lambda\equiv(20,22,24)\pmod{125},\qquad\lambda_1\in\mathbb Z_5^\times.$$
对 $v=v_0+v_1r+v_2r^2\in L_5$ 定义
$$\ell_0(v)=\lambda_1v_0-\lambda_0v_1,\qquad
\ell_2(v)=\lambda_1v_2-\lambda_2v_1.$$
它们是整的 $\mathbb Q_5$ 线性式，且准确地杀掉整个全局对数直线 (129.5)。使用实际 $\lambda_i$ 定义，而非把三个模 $125$ 整数当作无限精度系数。

在横坐标盘的选定分支上，令
$$F_i(x)=\ell_i(\log_{\mathcal E}\psi(x,b(x))),\qquad i=0,2.$$
对任何来自全局有理点的提升，均有 $F_0(x)=F_2(x)=0$。

由 (129.3)，对于盘中心 $a\in\{0,1,-1\}$，
$$F_i(x)-F_i(a)=\ell_i\left(\int_a^x\frac{du}{y(u)}\right).\tag{129.9}$$
这可直接由形式群对数的导数推出，不依赖全局平方根或未计算的高度。

## 5. 完整尾界和全部剩余盘的封口

因为 $2y(a)$ 是单位，隐函数定理给
$$\frac1{y(a+z)}\in\mathcal O_{L_5}[[z]].$$
代入 $z=5T$ 并逐项积分，所有次数 $n\ge2$ 的项都有
$$v_5(5^n/n)=n-v_5(n)\ge2.$$
所以对所有 $T\in\mathbb Z_5$，都有统一且完整的尾界
$$
F_i(a+5T)=F_i(a)+5T\ell_i(1/y(a))+25\,g_i(T),
\quad g_i\in\mathbb Z_5\langle T\rangle.
\tag{129.10}
$$
更具体，去掉常数和线性项后的 $g_i$ 被 $T^2$ 整除。该式处理整个剩余盘，不仅有限多个提升。

### 5.1 排除 $x\equiv0\pmod5$

由 (129.8) 的两个实际对数及 $y_0$，得到
$$
(F_0(0),F_2(0))\equiv(15,85)\pmod{125},
$$
$$
(\ell_0(1/y_0),\ell_2(1/y_0))\equiv(4,75)\pmod{125}.
\tag{129.11}
$$
特别是 $F_2(0)\equiv10\pmod{25}$，而 $\ell_2(1/y_0)\equiv0\pmod5$。因此 (129.10) 对整个盘给
$$\boxed{F_2(5T)\equiv10\pmod{25}\qquad(T\in\mathbb Z_5).}$$
没有任何零点。取另一平方根分支时全部值反号，结论不变。

### 5.2 $x\equiv1,-1\pmod5$ 各只有已知横坐标

对两个已知全局分支，中心值准确为零：$\psi(1)=T_2$ 的对数为零，$\psi(-1)=P$ 的对数属于被杀掉的直线。导数为
$$
\begin{array}{c|c}
a&(\ell_0(1/y(a)),\ell_2(1/y(a)))\pmod5\\\hline
1&(2,2)\\
-1&(3,1).
\end{array}
\tag{129.12}
$$
每盘至少一个导数是单位。对该线性式，(129.10) 可写成
$$F_i(a+5T)/5=T(c+5h(T)),\qquad c\in\mathbb Z_5^\times,$$
其中 $h(T)\in\mathbb Z_5\langle T\rangle$。括号对全部 $T\in\mathbb Z_5$ 都是单位，所以唯一零点为 $T=0$，即 $x=a$。另一个纵坐标分支给同样结论。

这排尽全部六个剩余盘，故有理横坐标只有 $\pm1$。最后 $S(-1)=144$、$S(1)=4$，证明 (129.1)。

## 6. 对实际九次幂分母支的结论

R120 的实际模映射在这两个横坐标上给
$$x=-1\Longrightarrow j=1728,\qquad
x=1\Longrightarrow j=287496=66^3.$$
二者均为 CM 的有理 $j$ 值。因此固定 $\mathbb Q(i)$ 扭曲的九级非分裂 Cartan 曲线没有给出任何非 CM 有理点。

R114 给出的实际同构
$$E[9]\simeq A[9]\quad\Longleftrightarrow\quad Z\in\mathbb Q^{\times9}$$
以及 R120 的模解释，将 R19 的每个实际九次幂分母解送到 $\mathcal C(\mathbb Q)$。这包含负的奇九次幂、全部三族及其扭曲规范。由 (129.1)，这些像只能给 CM 曲线，与原来的非 CM 条件矛盾。

所以不仅存在一个未计算的有限阈值，而是这个分支在 R19 的全部 $p>37$ 范围均无非 CM 解。其余 $Z$ 的全局排除仍须另证，不能把本条固定曲线分类扩称为完整 Serre 统一性定理。

## 7. 可复验文件

```sh
python topics/serre-uniformity/notes/verify_r127_cubic_cover_rank.py --check
python topics/serre-uniformity/notes/verify_r129_nine_twist_rational_points.py --check
```

后一个命令使用 R127 的精确三次环运算，无外部代数软件。它从头计数两个有限域曲线、以模 $625$ 射影运算重算两个真实对数、检验全部平方根与导数、再以模 $5^8$ 独立重算。证书为 `notes/r129_nine_twist_rational_points_certificate.json`。

本证明没有计算或假定完整 Mordell–Weil 饱和格，也没有只筛一个已知子群的剩余类。全局秩一用于 (129.5)，剩余盘直接来自完整的 $\mathcal C(\mathbb F_5)$，而 (129.10) 负责每一整盘的证明。
