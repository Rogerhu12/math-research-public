# 原 F0 的两个三处字：固定 degree34 返回及完整中央消费规范

日期：2026-11-27 UTC。以下特征零有理函数、Miller、theta 线束及完整读者身份已经手证。旁列小消费者只读取这些固定来源，返回一个次数至多十的多项式及其真实有限二处分量；本稿不预填其尚未执行的坐标或非零谱投影。

本文是 R1040 的原四 sigma 来源
$$
F_0(z)=\sigma(7z)\sigma(\pi z)\sigma(\bar\pi z)\sigma(3\delta z),
\qquad \pi=4+\omega,\quad\delta=1+2\omega,
\tag{1}
$$
的非平凡 δ 字消费。R1040 已证明整个未平均 δ-trace 为零；不能改用其已经排掉的 norm63 old trace。

## 1. 原完整四因子与精确 Kummer frame

先取同一个 $E_1:y^2=x^3+1$ 和
$x=z^{-2}+\cdots,\ y=-z^{-3}+\cdots,\ \sigma=z+\cdots$。
记上层点为 P，下层点为 $Q=[\delta]P$；本节不把二者的坐标混写。
令
$$
X_u=x(P)^3,\quad x=x(Q),\quad y=y(Q),\quad h=1-y,
$$
$$
\kappa=-\frac{y(P)+\delta}{\delta x(P)}.
\tag{2}
$$
原 δ 加法式逐项给
$$
\kappa^3=h,\qquad
x(P)=-\frac{2\kappa}{\kappa^2-x}
=-x-\frac{x^2}{h}\kappa-\kappa^2.
\tag{3}
$$
取原 deck 生成元 $u_\delta=(0,-1)$。
在 O 比较首极，$\kappa(P+u_\delta)/\kappa(P)=\omega$，
故 (2) 指定了实际两个字符的方向，不另选 cube root。
完整关系也由二者的 divisor 和这一首项固定。

置 $t=x\kappa$，则
$$
t^3=h^2(h-2).
$$
(3) 给下列整个三维代数中的两个互逆元：
$$
\begin{aligned}
U:=X_u={}&(-4+18h-9h^2)+(12-9h)t+(6/h-9)t^2,\\
U^{-1}={}&-\frac14+\frac38t-\frac{3}{8h}t^2 .
\end{aligned}
\tag{4}
$$
所有分支都在该三维代数内保留；没有挑选一条 fiber。

沿 R1038 §13 的原完整 division 因子，定义
$$
\begin{aligned}
Q_7(X)&=7X^2-4X+16,\\
C_3(X)&=X^3-96X^2+48X+64,\\
D_{13}(X)&=13X^4+52X^3+1536X^2+1024X+256,\\
S_7(X)&=X^6+564X^5-5808X^4-123136X^3\\
&\hspace{14mm}-189696X^2-49152X+4096,\\
R_{16}(X)&=\frac1{91}(X+4)Q_7(X)C_3(X)D_{13}(X)S_7(X).
\end{aligned}
\tag{5}
$$
这是首一 degree16。原 sigma 恒等式准确为
$$
\boxed{F_0=273\delta\,\sigma^{102}x\,R_{16}(X).}
\tag{6}
$$
其中 $273\delta=7\pi\bar\pi(3\delta)$，与原四个首项完全相同。

用原 $[\delta]^*$ 的 frame $\sigma(\delta z)^{34}$，令
$$
f(P)=\frac{F_0(z)}{273\delta\,\sigma(\delta z)^{34}}
=\delta^{-34}\frac{R_{16}(U)}{U^{11}},
\qquad \delta^{-34}=-3^{-17}.
\tag{7}
$$
这个固定有理函数才是本文三个 Fourier 字的输入。

## 2. 全 trace-zero 及两个真正整词

将 (7) 唯一写为
$$
f=A_0(h)+A_1(h)t+A_2(h)t^2.
\tag{8}
$$
由整个 trace 而非原点质量，$A_0=0$。
若 $\mathsf P_i$ 表示 (2) 指定的 deck 字投影，则
$$
\mathsf P_i f=x^i A_i(h)\kappa^i,\qquad i=1,2.
\tag{9}
$$

这里系数只能在固定 Laurent 环中：
$$
A_1\in\mathbf Q[h]_{\le10},\qquad
A_2\in h^{-1}\mathbf Q[h]_{\le10}.
\tag{10}
$$
证明不靠输出拟合。$f$ 只在 $\ker\delta$ 有极、各极不超过34；
$\operatorname{div}\kappa=[\delta]^*((S)-(O))$，$S=(0,1)$。
于是 $x^iA_i$ 的极除子不超过 $(34-i)O+iS$。
再用 $x$ 在 S 为一阶零、在 O 为二阶极，$h$ 在 S 为三阶零、
在 O 为三阶极，逐端点给 (10)。除 O、S 外没有额外极。
所有系数在 (4) 的 Laurent 环，故该极条件即给显示的有限区间。

必须使用以下方向的 Miller 函数：
$$
R_1=S,\qquad R_2=-S,\qquad
h_1=(1-y)^{-11},\quad h_2=\frac{x^2}{(1+y)^{12}}.
\tag{11}
$$
它们的完整 divisor 是
$$
\operatorname{div}h_i=(34-i)O+iS-34R_i.
$$
因此标准化是**先乘 $h_i$，再平移 $R_i$**：
$$
Q_i(P)=\{x^iA_i(1-y)h_i\}(P+R_i).
\tag{12}
$$
这个方向保证只在 O 有至多34阶极；
除以 $h_i$ 会得到错误的来源。

使用同一个实际加法式
$$
x(P+S)=-\frac{2x}{y+1},\quad
y(P+S)=\frac{y-3}{y+1},
$$
$$
x(P-S)=\frac{2x}{y-1},\quad
y(P-S)=-\frac{y+3}{y-1},
$$
得到
$$
\boxed{Q_1=xB_1(y),\quad Q_2=xB_2(y),}
\tag{13}
$$
其中若 $A_i(h)=\sum_e a_{i,e}h^e$，全部系数准确由
$$
\begin{aligned}
B_1(y)&=-2\sum_{e=0}^{10}a_{1,e}\,4^{e-11}(y+1)^{10-e},\\
B_2(y)&=2^{-20}\sum_{e=-1}^{9}
 a_{2,e}\,2^e(y-1)^{9-e}(y+1)^{e+1}.
\end{aligned}
\tag{14}
$$
每项都是多项式，次数至多十。
从 $F_0(-z)=F_0(z)$ 及
$\kappa(-P)=-x/\kappa(P)$，严格有
$$
A_2(h)=-A_1(2-h)/h,\qquad
\boxed{B_2(y)=B_1(-y).}
\tag{15}
$$
这同时锁定两个完整字的相对归一，不能各自选择一个 scalar。
下文记 $B=B_1$。

两条真实标准 theta 来源于是为
$$
\boxed{\mathcal B_\pm=\sigma^{34}x B(\pm y).}
\tag{16}
$$
它们都属于同一个标准 degree34 空间；
偶部是 type2，奇部是 type5。
此处并没有 type4/type1 的另一个独立输入。

两个端点还能直接手证，作为消费者的独立必要检查：
$$
\boxed{B(1)=B(-1)=-1/1092.}
\tag{17}
$$
确切地，$R_{16}(0)=2^{32}/91$。
在 $h=\infty$ 取 (4) 的最高项，
$(r-r^2)^{11}=-3^5(r-r^2)$ 于 $r^3=1$，
给 $[h^{10}]A_1=1/546$；
(14) 遂给 $B(-1)=-1/1092$。
另一方面 $R_{16}(-4)=0$，且
$$
R_{16}'(-4)=-2^{30}3^{15}/91.
$$
在 $h=2$，$U=-4-6t-6t^2$、$t^3=0$，
故 (7) 的线性系数是 $A_1(2)=512/273$，
再由 (14) 得 $B(1)=-A_1(2)/2^{11}$。
因此实际偶部非零，而奇部对应的 X 多项式在 X=0 为零。
本稿没有预认整个奇部或其任一 Hecke 分量非零。

## 3. 保持原 degree126 及全部 σ/Miller 权

R1038 的原规范是
$$
\Phi_{126}=\frac{F_0\,\sigma(2\delta z)^2}{-3276\delta}.
$$
结合 (7)–(12)，整个两字等式准确为
$$
\boxed{
\mathsf P_i\Phi_{126}(z)=
-\frac1{12}\kappa(P)^i h_i(Q)^{-1}
 \frac{\sigma(Q)^{34}\sigma(2Q)^2}
      {\sigma(Q-R_i)^{34}}\,
 \mathcal B_i(Q-R_i),\quad Q=\delta P.}
\tag{18}
$$
其中 $\mathcal B_1=\mathcal B_+$、$\mathcal B_2=\mathcal B_-$。
未写作单值有理函数的 sigma 比率正是原 rigidified theta lift；
(18) 定义时保持整个比率和实际 lift，不以无来源的常数代替。
(2)、(11) 又提供了其全部代数 Kummer/Miller data。
该等式来自完整有理函数回乘，因此 Gaussian 也由原 sigma 比率逐项保持。

在任一好 ordinary 完成中，选原相容周期。
原中央测试仍是输出单位上的
$\mathbf1_{\mathrm{unit}}\langle x\rangle^{(p-1)u}$
及其首导数。若使用 (18) 下推到 $\mathcal B_\pm$，就必须对该真实
算子取完整 transpose：$Q=\delta P$、$Q-R_i$、
$\kappa^i/h_i$、$\sigma(2Q)^2$ 和 sigma 比率都在内。
不能把由此得到的测试改写成裸的负一矩，
也不能把两条 $\mathcal B_\pm$ 单独赋予原 E3969 canonical 中央零。

这是可直接继续消费的原来源关系：
新 rank-two 的实际必要行作用在 (18) 的完整两字和上；
R1040 的两联合字及所有 mixed 单位 cut，按同一字符方向同时保持。
非零 type5 投影若由下面消费者返回，只支付一个明确的已知 rank-one 来源；
其中央功能还须按 (18) 的实际权比较。

## 4. 原有限二处的完整五维消费

把 $\mathcal B_+$ 的奇部写成
$$
-\sigma^{34}xy\,P(X),\qquad \deg P\le4.
\tag{19}
$$
R732/R735 已给两个真正 rank-one 来源的首项规范向量
$$
v_-=(64,-104,-156,13,1),\qquad
v_\omega=(128,368,120,-109,11)/11 .
\tag{20}
$$
分别是 $E_{17^4}$ 与 $E_{17^2}$ 的实际完整来源。
它们的裸负一单位矩非零及共同 period 沿 R735；
这里不重做该算术结论。

所用二挠作用的绝对规范直接来自 R967 及 R1021 §15.2：
$$
q_e^2=e^2(x-e)/\sqrt3,\quad
x_e=e(x+2e)/(x-e),\quad
y_e=-3e^2y/(x-e)^2,\quad e^3=-1.
\tag{21}
$$
故 $\mathcal H=3^{-1/2}\sum_e T_e^{34}$ 在整个 (19) 上的公式为
$$
\boxed{
\mathcal H P
=-\frac1{3^8x}
 \sum_{e^3=-1}\sum_{j=0}^4
 p_j(-1)^j e(x+2e)^{1+3j}(x-e)^{14-3j}.}
\tag{22}
$$
三个根全部求和；只保 $\sum e^k=0$ 当 $3\nmid k$，
$\sum e^{3k}=3(-1)^k$。
因此结果在 $\mathbf Q[X]_{\le4}$ 中，不用另算 CM13 全纤维。
消费者同时核(17)的两个独立手证端点，随后逐列核 $\mathcal H^2=I$，并以 (20) 的两个完整向量锁实际共同符号。
随后对新的 P 作两个完整 dyadic 投影，保全部余项。
两线系数以最高两行求得，再回乘全部五行；
不能把匹配两项当作完整来源证明。

还直接比较原 S34 的协变导数：
若
$$
S=\sigma^{34}x^2P_S(X),\quad
P_S=(-128-80X-12X^2-53X^3+7X^4)/7,
$$
则
$$
\nabla_{34}S:=\sigma^{34}D(x^2P_S)
=-\sigma^{34}xy\{-4P_S-6XP_S'\}.
\tag{23}
$$
消费者保其两个 dyadic 块，检查新余项是否完整成比例。
即使返回比例，也不从原 $j(S)=0$ 直接给 $\nabla S$ 或任意乘子赋零；
原 $\sigma'/\sigma$、全部 unit cut 与连接项继续保留。
这一步针对一个实际源端一阶消元，不是重新展开整个 finite spectrum。

## 5. 小消费者与执行边界

公开消费者：[check-original-f0-two-delta-words.py](../scripts/check-original-f0-two-delta-words.py)。

源码11389字节，SHA256：
cd058b2e1f193f8dd380eece8149c7e21062516d21cf32bdd4f4311da4c615e2。

仅使用 Python 标准库 Fraction。
整个数学操作是 (4) 的三项 Laurent 代数、(5) 的固定因子、
(14) 的两个完整整词、其双向回乘，以及 (22) 对原五维空间的完整作用。
不重算旧390/378/126谱，不扫描目标素数，不缓存已运行矩阵。
输出单个紧凑 JSON，保所有实际新 B 系数、两个角型、两个 dyadic 分量、
两 rank-one 系数、原协变导数比较和全部未消余项；
输出含源码 hash 且检查小于60000字节。

源码只在 Rogerhu12/math-research-public 的公开 GitHub Actions 执行。
本稿尚未取得运行回执，因此没有写入任何实际 B 坐标或新投影非零结论。
