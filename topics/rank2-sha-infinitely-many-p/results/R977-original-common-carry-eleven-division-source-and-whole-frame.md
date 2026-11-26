# R977 — 保原共同 carry 的十一倍 sigma 来源与完整五伴随

日期：2026-11-27。**已证明：下面是同一原六 sigma 的真实 degree130 来源，保 R968 的完整共同 C/F 观察、全部整框架及四方向 CM 转移。** 它替换 R971 对 E260 投影实际为零的候选；新候选是否向 E260 非零投影仍由完整同次消费者读取，本文不预设该非零。

## 1. 保持同一共同平面的真实六输入

沿 R968/R971 固定

$$
E_1:y^2=x^3+1,\quad dz=dx/(2y),\quad
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\rho=-\nu_\sigma^{\otimes6}/84.
$$

原输入顺序仍为 $(\xi_1,\xi_2,\xi_3,x_0,c,d_0)$。
这里 $x_0$ 是第四输入，曲线函数另记 $x(z)$。令

$$
a_{11}=(2+\omega,2+\omega,1,\omega^2,1,11),\qquad
Y_{11}=a_{11}\xi.
\tag{1}
$$

六个 Hermitian 范数分别为 $3,3,1,1,1,121$，总和恰为130。
保留 R968 的原整行

$$
H_0=(1,0,-1,1,0,0),\qquad
H_1=(-1,2,\omega,1+\omega,0,0),
$$

以及 $C=H_0/\delta$、$F=-\omega H_1/\delta$。
完整 Hermitian 正交不是只比较范数；直接有

$$
a_{11}\bar H_0^t=(2+\omega)-1+\omega^2=0,
$$

$$
a_{11}\bar H_1^t=-(2+\omega)+2(2+\omega)
+\omega^2+(1+\omega^2)\omega^2=0.
\tag{2}
$$

故 $Y_{11}$ 属于同一个 $\ker C\cap\ker F$ 四输出。
与原 $S,T,W^\pm,Z,W'$ 一起使用时，不需要另换一个共同平面。
六个 (1) 的系数模2都非零；六个 odd 半特征相乘为标准 even 半特征。
其 Gaussian 合并为 degree130，六次整体旋转的角型为零。

用同一真实推前定义

$$
\boxed{\mathcal F_{11}=\frac{28}{11\omega}(a_{11})_*\rho.}
\tag{3}
$$

常数是准确的原六 sigma 常数，不是后选一个未知特征向量来归一。

## 2. 完整十一倍除法给全部22坐标

由于 $2+\omega=-\omega\delta$，原 sigma 的 CM 单位相位及
$\sigma(\delta z)=\delta x(z)\sigma(z)^3$ 给

$$
\begin{aligned}
&\sigma((2+\omega)z)^2\sigma(z)\sigma(\omega^2z)\sigma(z)\sigma(11z)\\
&\hspace{12mm}=\omega\sigma(\delta z)^2\sigma(z)^3\sigma(11z)
=-3\omega x(z)^2\sigma(z)^9\sigma(11z).
\end{aligned}
\tag{4}
$$

乘原 $-1/84$ 和 (3) 的归一常数，得到全函数身份

$$
\boxed{F_{11}(z)=\frac1{11}x(z)^2\sigma(z)^9\sigma(11z)
=\frac1{11}\sigma(z)^{130}x(z)^2\psi_{11}(x(z),y(z)).}
\tag{5}
$$

这里对奇数 $n$，原规范给 $\sigma(nz)/\sigma(z)^{n^2}=\psi_n$。
下列公式保留全部十一倍核点和其重数。写 $X=x^3$，置

$$
R_4=X^2+20X-8,
$$

$$
R_5=5X^4+380X^3-240X^2-1600X-256,
$$

$$
R_7=27X(X+4)^3R_5-128(X+1)^2R_4^3.
\tag{6}
$$

原全除法递推依次为

$$
\psi_2=2y,\quad \psi_3=3x(X+4),\quad \psi_4=4yR_4,
\quad\psi_5=R_5,
$$

$$
\psi_6=\frac{\psi_3}{2y}(\psi_5\psi_2^2-\psi_4^2)
=6xy(X+4)(R_5-4R_4^2),
$$

$$
\psi_7=\psi_5\psi_3^3-\psi_2\psi_4^3=R_7.
$$

所以 $\psi_{11}=\psi_7\psi_5^3-\psi_4\psi_6^3$ 给

$$
\boxed{R_{11}:=\psi_{11}
=R_7R_5^3-864X(X+1)^2(X+4)^3R_4(R_5-4R_4^2)^3.}
\tag{7}
$$

每项都在 $\mathbf Z[X]$；没有使用有限普通点插值。
$R_7$ 首系数为 $135-128=7$、次数8；(7) 的两个20次首系数分别为875、864，故

$$
\boxed{\deg R_{11}=20,\qquad [X^{20}]R_{11}=11.}
\tag{8}
$$

因此 (5) 位于完整
$V_{130}=\sigma^{130}x^2K[X]_{\le21}$，其全部22坐标就是 $R_{11}/11$，
最高第21质量列为零，第20列为一，原点阶准确为六。
它的有理系数只含固定分母11。整个来源已由 (1)、(3)–(7) 指定，
不由目标 CM 特征值反选。

## 3. 同一个原整五伴随框架

从首行 $a_{11}$ 开始，依次删除零起始指标
$5,0,1,2,3$，最后留指标4。对当前剩余集 $I$，写
$N_I=\sum_{j\in I}a_j\bar a_j$，新行仍是原 Hermitian 消元

$$
r_i=N_Ie_i-\bar a_i\,a_{11}|_I.
\tag{9}
$$

全部剩余范数链为

$$
130,9,6,3,2,1.
$$

直接展开内积给 $r_i\bar a_{11}^t=0$ 及
$N(r_i)=N_I(N_I-N(a_i))$；后续每行在先前被删坐标为零，
故同样逐对正交。把首行及五条新行组成 $L_{11}$，得到

$$
\boxed{L_{11}\bar L_{11}^t
=\operatorname{diag}(130,1170,54,18,6,2).}
\tag{10}
$$

全行在 $\mathbf Z[\omega]^6$，实际模2非零系数个数为
$(6,6,4,4,2,2)$。所以每个方向都是完整标准 even theta 空间，
所有 Gaussian 交叉项为零。准确双逆和行列式范数为

$$
(L_{11}^{-1})_{ji}=\frac{\overline{(L_{11})_{ij}}}{N_i},
\qquad(N_0,\ldots,N_5)=(130,1170,54,18,6,2),
$$

$$
\boxed{N(\det L_{11})=(130\cdot9\cdot6\cdot3\cdot2)^2
=1774094400.}
\tag{11}
$$

其素因子只有 $2,3,5,13$，与7、19互素。
在取任何边际之前，完整联合来源为

$$
\frac{28}{11\omega}(L_{11})_*\rho
\in\mathcal S_{130}\otimes\mathcal S_{1170}\otimes
\mathcal S_{54}\otimes\mathcal S_{18}\otimes\mathcal S_6\otimes\mathcal S_2.
\tag{12}
$$

(5) 是其真实第一边际；没有从边际反推 (12) 的合法性。

## 4. 完整四方向 CM 转移与条件性的目标提取

沿 R961/R971 已付原四个奇 sigma 绝对相位，
$N_\gamma\sigma=\sigma$，其中
$\gamma\in\{3+\omega,2-\omega,4+\delta,4-\delta\}$，
$N_\gamma=[\gamma]_*[\bar\gamma]^*/\gamma$。
由 (11)，$L_{11}$ 在每一种完整六重 CM 核上是双射。
重排整个有限纤维，保全部原中心和 $\gamma^{-6}$，给

$$
N_{\gamma,Y_{11}}\prod_{i=1}^5N_{\gamma,Z_i}
\left(\frac{28}{11\omega}(L_{11})_*\rho\right)
=\frac{28}{11\omega}(L_{11})_*\rho.
\tag{13}
$$

令 $\Pi_{260}$ 是由 R973 的全有限算术来源及 R976 的完整一维共同核
指定的第一轴投影，先含真实第一轴 $\mu_6$ 平均。
若新同次原消费者返回

$$
\Pi_{260}F_{11}=\alpha_{11}\Phi_{260,1},\qquad\alpha_{11}\ne0,
\tag{14}
$$

则完整第一轴投影和 (13) 的等价五伴随多项式给

$$
\Pi_{260,Y_{11}}
\left(\frac{28}{11\omega}(L_{11})_*\rho\right)
=\Phi_{260,1}\otimes\Lambda_{11},\qquad
\Lambda_{11}(0)=\alpha_{11}.
\tag{15}
$$

不要求先知道所有别的 CM 分量为零。第一轴完整秩一投影本身就使联合
张量按 (15) 分解；原伴随算法保持全部实际有限 trace，而非只用质量。
在普通好位，所有固定分母和 $\alpha_{11}$ 的分子之外，完整投影整；
第一轴六阶 Amice 系数为 $\Omega_p^6$，提取它给全部伴随整性。
质量为单位时 $\Lambda_{11}$ 才是整 Amice 卷积单位。
(14) 尚未由本篇的范数或 odd 个数推出，必须读实际完整投影。
真实物理曲线、$260/17$ 的同模型权及其清分母仍按 R973，不把11的来源
归一常数与曲线 period 混同。

## 5. 原共同 carry 及每条旧混合观察都保留

由 (2)，R968 的同一完整投影
$\pi=I-\bar C^t C-(3/7)\bar F^t F$ 满足 $a_{11}\pi=a_{11}$。
原共同 carry $\mathfrak q_{n,p}^{\rm new}$ 因而对新真实边际给

$$
\int_{Y_{11}\,\mathrm{unit}}
\langle Y_{11}\rangle^{(p-1)u}
\mathfrak q_{n,p}^{\rm new}\,d\rho
=\upsilon_p^n
\int_{Y_{11}\,\mathrm{unit}}
\langle Y_{11}\rangle^{(p-1)u}\,d\rho.
\tag{16}
$$

这是 (23) 的整个四输出返回应用于一个真实输出；所有原 torsion 支及
$p$-整单位域都保留。第一轴完整 principal/CM trace-pull 只沿
$\bar a_{11}$ 方向移动，故逐个真实有限中心也保持 $C,F$。
所以 (16) 同样作用于新第一轴已投影来源。
它没有要求任意一个五伴随算子单独与测试交换。

对每条旧观察 $r$，包括 $S,T,W^\pm,Z$ 及旧 $A+c+10d_0$，
先取准确行 $rL_{11}^{-1}$，并保完整返回
$(rL_{11}^{-1})L_{11}=r$。在五伴随的实际分支
$\beta=\gamma_7^j\gamma_{19}^k$、$\zeta\in\mu_6$ 中，其连续部分是

$$
(rL_{11}^{-1})_0Y_{11}
+\frac{\zeta}{\bar\beta}\sum_{i=1}^5(rL_{11}^{-1})_i Z_i,
\tag{17}
$$

并须同时加入原 canonical division lift 的全部有限中心。
单位条件、深管和 logarithm 都读取 (17) 的完整混合式。
新来源可沿用原共同 $C,F$，不等于这些旧测试已经变成独立伴随测试。

因此本篇真正新增了一个保持原共同 carry 的真实候选、其所有22坐标、
整五伴随和完整 CM 转移。新算术投影、完整交叉余项及跨无穷素数的
中央非零仍按各自实际门推进，不以此结构结论宣布主目标完成。

## 依赖与执行源码

- R968：原 $C,F$、degree10/210 whole 核、全部四输出 carry 和真实补域。
- R971：同原六 sigma、完整 Hermitian 消元与四方向 CM 转移规范。
- R973/R976：E260 的完整有限来源和目标一维共同核；本篇只在 (14) 后消费。
- scripts/check-original-e260-six-sigma-source.py：由完整除法式构造 (7)，在原同次全部 CM 上读取目标投影，返回全 Gram/双逆、共同正交和每条旧行；实际执行回执另登记，不读取生成矩阵或向量文件。
