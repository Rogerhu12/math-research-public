# 原 F0 的两个三处字：固定 degree34 返回及完整中央消费规范

日期：2026-11-27 UTC。以下特征零有理函数、Miller、theta 线束及完整读者身份已经手证。第6节记录固定小消费者的完整公开返回：两条旧rank-one投影均零，实际非零三维分量及其短式全部保留。

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
最终完整公开回执、所有新必要坐标及其严格消费范围见第6节。


## 6. 实际公开返回、完整短式与原中央输入

本节的计算已经在同一公开仓库完成，不是下一次执行的预期。
run 为 45991193171，job 为 140479142693，
源提交为 c5b9ce61389b975b1a11d1ff1ee71912a8749751；
2026-11-27 11:31:41–11:31:48 UTC 成功，
数学消费者用时 0.06458075599999802 秒。

实际脚本仍是第5节的文件名；根代理仅在提交前加入 (17) 的两个
独立手证端点断言。最终源码11389字节，SHA256 为
cd058b2e1f193f8dd380eece8149c7e21062516d21cf32bdd4f4311da4c615e2。
stdout 3135字节，SHA256 为
7f5e84c3c3ea8b30b6973ab625f38ab319fea3b29fb785b77d1e6a898104d6af；
不含末换行的 payload 3134字节，SHA256 为
8769d50741e9f9ab96099ab81c751fd750ea088ab57bcd38f328bb703216b102。
完整 job log 11482字节，SHA256 为
f263af2b141f6063d8c75870d83dc1cedbe6300a45dc3317cd1984a45c9d406c。

### 6.1 一个完整 B，而非两个独立的猜测来源

实际 B 的升幂坐标是
$$
\begin{aligned}
B(y)={}&\frac{243y}{93184}-\frac{243y^2}{93184}
-\frac{81y^3}{23296}+\frac{27y^4}{23296}
+\frac{9y^5}{46592}\\
&+\frac{27y^6}{46592}+\frac{15y^7}{23296}
-\frac{y^8}{23296}+\frac{3y^9}{93184}
-\frac{y^{10}}{279552}.
\end{aligned}
\tag{24}
$$
完整坐标 SHA256 为
cffc1c7b7ed211029fb98654ebba0f745b297411f4cc7e188f809f81214a0efe。
消费者已同时核定整个三字重建、$A_0=0$、(15) 反射、
(17) 两端点、所有 Laurent 极帽、完整五维 (22) 及其平方。

令
$$
V_-(X)=X^4+13X^3-156X^2-104X+64,\qquad
B_2^{\rm div}(X)=X^2+20X-8 .
$$
这里 $B_2^{\rm div}$ 是原四分点 division 因子，
与 (13) 的第二个字多项式 $B_2(y)$ 区分。
逐系数乘回 (24)，精确得到
$$
\boxed{
\begin{aligned}
\mathcal B_{\rm even}
 &= -\frac{\sigma^{34}x(X+4)V_-(X)}{279552},\\
\mathcal B_{\rm odd}
 &= \frac{3\,\sigma^{34}x^4y(X+4)B_2^{\rm div}(X)}{93184},\\
\mathcal B_\pm&=\mathcal B_{\rm even}\pm\mathcal B_{\rm odd}.
\end{aligned}}
\tag{25}
$$
特别，(19) 所用的是 **negative-xy** 坐标：
$$
P(X)=-\frac{3X(X+4)(X^2+20X-8)}{93184}.
\tag{26}
$$
不能去掉 (19) 的前置负号后再解释 (26)。
真实奇部首项为 $-3z^5/93184$，
真实偶部首项为 $-z^2/279552$。

### 6.2 原 finite2/17 块的实际范围

完整五维矩阵返回
$$
\mathcal H P=-P,\qquad
\Pi_{\mathcal H=+1}P=0.
\tag{27}
$$
完整矩阵的迹为 $-1$，且平方为1，故 $+1$ 块维数为2；(20)的两条独立线均在其中，已经穷尽该块。原 CM13 对全部二挠 lift 的共轭按模4的 $\omega^2$ 循环它们，所以与 $\mathcal H$ 交换。
故 R735 两个已付 rank-one 线的系数都准确为零。
剩余三维块整个非零，而不是一个漏掉的余项。
R732、R761 已在这个同一原模型上识别：
它是 $T^3+\omega$ primitive 块，
完整 finite17 标签为 $j=1,7,13$，相应九阶角色的有限单位表、
Schwartz、全权平方及点域见 R761。
由于 (26) 定义于 $\mathbf Q\subset K$ 且非零，
三次多项式在 K 上不可约，故它在三条几何特征线上的投影都非零。
这句话只识别来源系数；R761 没有证明三条裸负一值必都非零，
这里也不补上这种断言。

实际 (23) 的完整 $\mathcal H=-1$ 余块为
$$
\left(\frac{5888}{21},\frac{14912}{21},
\frac{1552}{7},-\frac{208}{21},-\frac{214}{21}\right).
\tag{28}
$$
它与 (26) 不成比例：后者常数项为零而 (28) 常数项非零，
任何比例只能为零，但 (26) 本身非零。
因此不能把新完整奇部改认作原 S 的单个协变导数。
这些准确结果已经消除了两种候选消费，不重复执行旧完整谱。

### 6.3 一个已知来源的真实乘子与一个真实五 sigma 输入

R735 的原首 $z^5$ 来源在 $b=1$ 上为
$$
D_-=-\sigma^{34}xy V_-(X).
$$
结合 (25)，偶部准确为
$$
\mathcal B_{\rm even}
 =\frac{X+4}{279552\,y}\,D_- .
\tag{29}
$$
此处 $y^{-1}$ 的表观极由 $D_-$ 的真实零抵消；
整个左边是原 holomorphic degree34 来源。
它仍是乘了固定有理函数的完整来源，不能将其单位泛函直接当作
R735 的裸 $D_-$ 负一矩。

另外，原 division 规范给
$$
\begin{aligned}
\sigma(4z)&=-4y(X^2+20X-8)\sigma(z)^{16},\\
\sigma(3z)&=3x(X+4)\sigma(z)^9,\\
\sigma(\delta z)^3&=-3\delta\,x^3\sigma(z)^9 .
\end{aligned}
\tag{30}
$$
三式逐项乘回 (25)，所以
$$
\boxed{
\mathcal B_\pm
=\frac{X+4}{279552\,y}D_-
\ \pm\
\frac{\sigma(4z)\sigma(3z)\sigma(\delta z)^3}
     {1118208\,\delta}.
}
\tag{31}
$$
第二项有五个原 sigma 因子，次数
$16+9+3+3+3=34$，不需要另选有限来源或重算 Hecke 矩阵。
其首项直接为
$4\cdot3\cdot\delta^3/(1118208\delta)=-3/93184$，
独立核定 (31) 的正负号。

还可将两项共同的原 $\sigma(3z)$ 保留为一个完整因子：
$$
\mathcal B_\pm
=\sigma(3z)\left\{
-\frac{\sigma(z)^{25}V_-(X)}{838656}
\ \pm\ \frac{\sigma(4z)\sigma(\delta z)^3}{1118208\delta}
\right\}.
\tag{32}
$$
括号是两个真实 degree25 来源的和，
但 (32) 本身不把除去 $\sigma(3z)$ 后的来源赋予中央零。

### 6.4 直接回到原两字、同一单位域和真实 transpose

定义第3节完整算子
$$
\mathscr T_i A(P)=
\kappa(P)^i h_i(Q)^{-1}
\frac{\sigma(Q)^{34}\sigma(2Q)^2}
     {\sigma(Q-R_i)^{34}}A(Q-R_i),
\quad Q=\delta P .
\tag{33}
$$
将 (31) 代回已证明的 (18)，得到原同一个 canonical 输入的短式：
$$
\boxed{
\Phi_{126}
=-\frac1{12}\left[
(\mathscr T_1+\mathscr T_2)
 \left(\frac{X+4}{279552y}D_-\right)
+
(\mathscr T_1-\mathscr T_2)
 \left(\frac{\sigma(4z)\sigma(3z)\sigma(\delta z)^3}
 {1118208\delta}\right)
\right].
}
\tag{34}
$$
两个 $\mathscr T_i$ 内的点、周期、Miller、$\sigma(2Q)^2$ 和
sigma 比率均与 (18) 相同；(34) 没有替换单位 cut。

因此原 $j_{126,p}=0$ 必要条件，严格给出 (34) 右侧的
**整个加权和**在同一原读者下为零。
若使用反演，原 $\mathsf P_2\Phi(P)=\mathsf P_1\Phi(-P)$，
而 native 中央测试为偶，所以可将原两字读数等同；
这只作用于完整 $\mathscr T_i\mathcal B_i$。
它不分别给 (29)、五 sigma 项、任何 primitive17 投影
或除去共同因子的 degree25 来源赋零。
后续消元的对象由 (33) 的完整 transpose 明确给定，
而不是另加未经支付的中央条件。

