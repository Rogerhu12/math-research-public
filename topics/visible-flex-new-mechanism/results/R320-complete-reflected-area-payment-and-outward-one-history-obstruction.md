# R320：反射弱核圆的完整三矩面积支付与朝外排列的一层障碍

日期：2026-11-15。**独立纸面构造与完整原式推导。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R319](R319-one-sided-weak-hook-area-obstruction-and-reflected-block-cancellation.md) 的正反两个真实完整块已经支付 $A_{-2,-3}$ 面积的全部相位第零外矩。本稿完成另外两个外矩的真实建设：使用原右尾的准确反射律，再加入明确的强 hook 三矩 profiles，可以使该面积的三个外矩对全部相位同时为零。几何保持，最终 seed 与目标度量重新固定。

与此同时，本稿不把这一正向结果记为完整第四候选。对当前“右半侧放右向曲段，左半侧取其镜像”的朝外排列，即使该完整面积和其他必要 directed 行均被付，原一层仍有严格正余量。该否定覆盖负分支点以及本稿所有新增强 hook 修正块；不覆盖把曲段朝向和反射侧重新安排的另一类。

主要来源：[R46 完整包局部化与八副本](R46-eight-packet-complete-third-order-circle.md)、[R52 四槽第三 ruling](R52-overlapping-profile-plane-complete-third-order-circle.md)、[R250 原完整面积外矩](R250-complete-circle-Gaussian-area-and-nonuniform-profile-cancellation.md)、[R308 实际弱核圆与完整三阶](R308-genuine-derivative-rank-two-circles-with-one-hook-and-complete-third-range.md)、[R317 完整弱 mixed 修正](R317-exact-weak-hook-mixed-correction-and-nonnegative-branch-obstruction.md)及 R319。

## 1. 真实对象与要支付的三个外矩

固定已经安装的真实闭 hook 几何
$$
M=0,\qquad T=\kappa_H\mathfrak H,\quad\kappa_H\ne0,
$$
以及 R317 的小共振偶芽
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad
\varepsilon=\kappa^2/4,\quad
0<t:=\kappa^2<1/100.
\tag{1}
$$
原合法 profile 区间、右锚、几何有限词和基准段均固定。

令实 profiles $f,g$ 满足三矩圆与弱 hook
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad
\mathbf I(f,g)=0,\qquad
\mathfrak H(g;f,f)=0.
\tag{2}
$$
对
$$
u=\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D=f\odot f-u\odot u
$$
有 $\mathfrak H(u;D)=0$。沿 R319，
$$
[W_*,P](u;D)=\frac{a+3b}{3}J\{u''((f'')^2-(u'')^2)\},
\qquad a+3b\ne0.
\tag{3}
$$
定义真实 cubic 原函数与三外矩
$$
w_\theta=J\{u''((f'')^2-(u'')^2)\},\qquad
m_j(\theta)=I_j(u,w_\theta),\quad j=0,1,2,
\tag{4}
$$
其中
$$
I_0(u,v)=\int u''v'',\quad
I_1(u,v)=\int xu''v'',\quad
I_2(u,v)=\int(x^2u''v''+2u'v').
$$
目标是 $m_0=m_1=m_2=0$ 对全部相位成立。它准确支付 (3)的完整 Gaussian 面积配对，不要求这个 cubic 函数本身恒零。

## 2. 反射的真实常尾及三外矩变换

先对任一紧 pair 作同宽反射
$$
\widetilde f(x)=f(d-x),\qquad \widetilde g(x)=g(d-x).
$$
置 $y=d-x$。若 $\psi(y)=u''((f'')^2-(u'')^2)$，原右锚恢复准确给
$$
\widetilde w(x)=\int\psi-J\psi(y).
\tag{5}
$$
第一项是实际总积分产生的常尾，不能先置零。其导数分别为
$$
\widetilde w'(x)=w'(y),\qquad
\widetilde w''(x)=-w''(y),
$$
而 $\widetilde u'=-u'(y),\ \widetilde u''=u''(y)$。于是
$$
\boxed{
(m_0,m_1,m_2)\longmapsto
(-m_0,\ m_1-dm_0,\ -m_2+2dm_1-d^2m_0).
}
\tag{6}
$$
$I_2$ 的 $2u'v'$ 项也必须保留，才能得到最后一式。

选一个实际反射中心 $C_0$，令最终 profiles 同时关于 $C_0$ 为偶函数。将 (6)用于整个已合并 pair，$d=2C_0$，立即有
$$
\boxed{m_0=0,\qquad m_2=2C_0m_1.}
\tag{7}
$$
因此只需准确清整个 $m_1(\theta)$。这不是一般算子任意平移下的矩搬动假设；(6)已从当前 cubic 的真实右原函数直接证明。

## 3. 第四谐波和剩余两个系数

写
$$
F=f'',\quad G=g'',\quad r=F\cos\theta+G\sin\theta.
$$
原 R250 全式是
$$
m_1(\theta)=\frac12\int r^2F^2
-\frac34\int r^4-\int xr^2FF'.
\tag{8}
$$
只有中间项可能含第四谐波。定义
$$
\mathcal Q_4(f,g)=\int(F+iG)^4.
\tag{9}
$$
(8)的第四谐波为
$$
-\frac3{32}\Re\{\mathcal Q_4 e^{-4i\theta}\}.
$$
所以 $\mathcal Q_4=0$ 准确删去两条第四谐波。随后 $m_1$ 只含零次与二次谐波；因 $\theta=0$ 时 $D=0$，必有 $m_1(0)=0$，故
$$
m_1(\theta)=v_1\sin^2\theta+
v_2\cos\theta\sin\theta .
\tag{10}
$$
下面先真实支付 (9)，再用四个真实正幅方向支付 $(v_1,v_2)$。没有把这几个积分当作独立可任意指定的形状常数。

## 4. 一个明确的强 hook 三矩原型

取非零实偶 $\eta\in C_c^\infty(\mathbb R)$，支撑足够小。令
$$
a=1,\qquad
b_j=\sqrt{1+\frac{k_j}{100}},\qquad
(k_1,\ldots,k_7)=(-9,-6,-3,1,4,6,7).
$$
七个 $k_j$ 和为零，所有 $b_j$ 为正、互不相同且不等于 $a$。取 $\eta$ 的支撑宽度小于这些有限中心
$$
\{\pm a,\pm b_1,\ldots,\pm b_7\}
$$
最小间距的一个严格小倍数，使所有 bump 不交。

定义
$$
f_A=\frac{\eta(x-a)+\eta(x+a)}{\sqrt2},\qquad
g_A=\frac1{\sqrt{14}}\sum_{j=1}^7
\{\eta(x-b_j)+\eta(x+b_j)\}.
\tag{11}
$$
$I_0$ 两范数相等，交叉三矩逐点为零，两个自 $I_1$ 因偶性为零。又
$$
\frac17\sum_j b_j^2=a^2,
$$
故两个 $I_2$ 也相等。因此 (11)是准确非退化三矩圆。

$f_A,g_A$ 支撑不交，故其整个实平面对 hook 不可见。这里使用的是实际函数上的
$g_A'f_A''-f_A'g_A''=0$ 与 R306 分类，不是 formal rank 声明。

记
$$
C_\eta=\int(\eta'')^4>0.
$$
由于支撑不交，原四次矩准确为
$$
A_4:=\int(f_A'')^4=\frac{C_\eta}{2},\qquad
E_4:=\int(g_A'')^4=\frac{C_\eta}{14},
$$
$$
B_4=C_{22}=D_4^{\rm mix}=0.
\tag{12}
$$
从而
$$
\mathcal Q_4(f_A,g_A)=\frac{4C_\eta}{7}>0.
\tag{13}
$$
共同正仿射缩放保持三矩圆，(13)只乘一个正因子。以下所有原型都先在最终合法区间内固定宽度与位置。

### 4.1 任意复相位均由真实实 pair 实现

若 $\mathfrak q=f+ig$，则 $e^{i\varphi}\mathfrak q$ 对应真实变换
$$
\widetilde f=\cos\varphi\,f-\sin\varphi\,g,\qquad
\widetilde g=\sin\varphi\,f+\cos\varphi\,g.
\tag{14}
$$
这里只把 (14)用于强 hook 三矩原型；它保持整个 hook 平面零及三矩圆。乘一个正实幅度也是真实选取 profiles。

这不是对固定旧几何成本任意指定输入 phase，也不是 R156 所禁止的未证相位控制。实际选择的是新实 $f,g$，最后目标 metric 使用新的 seed。

## 5. 一个 $\mathcal Q_4=0$ 且二系数正锥为全平面的真实模块

取 (11)的两个同宽、互不交副本，分别施加相位
$-\pi/8$ 与 $+\pi/8$。把二者合成一个强 hook 三矩模块。由于
$e^{-i\pi/2}+e^{i\pi/2}=0$，其 $\mathcal Q_4$ 准确为零。

对这个模块记
$$
\mathcal S=\int(F^2+G^2)^2,\qquad
\mathcal Z_2=\int(F^2+G^2)(F+iG)^2 .
$$
(12)给
$$
\boxed{
\mathcal S=\frac{8C_\eta}{7},\qquad
\mathcal Z_2=\frac{3\sqrt2\,C_\eta}{7}>0.
}
\tag{15}
$$
对强 hook 的 rank-one 微包呈示，真实逐包分部积分有
$$
\int xF^2GF'=-\frac14\int F^3G,\qquad
\int xFG^2F'=-\frac14\int F^2G^2.
$$
这只用了各个实际实紧 bump 的端 jets，不要求其单独三矩合法。代入完整 (8)，再用 $\mathcal Q_4=0$，得到
$$
m_1(\theta)=
\frac34\left(-\frac{\mathcal S}{4}
+\frac{\Re\mathcal Z_2}{2}\right)\sin^2\theta
-\frac38\Im\mathcal Z_2\cos\theta\sin\theta .
\tag{16}
$$

对整个模块再施加四个真实相位
$$
\varphi_j=j\pi/4,\qquad j=0,1,2,3.
$$
它们保持 $\mathcal Q_4=0$，而 $\mathcal Z_2$ 依次乘
$1,i,-1,-i$。其两个系数向量是
$$
v_j=(-A_0+R_0\cos(j\pi/2),\ -R_0\sin(j\pi/2)),
$$
$$
A_0=\frac{3\mathcal S}{16}>0,\qquad
R_0=\frac{3|\mathcal Z_2|}{8},\qquad
\boxed{\frac{R_0}{A_0}=\frac{3\sqrt2}{4}>1.}
\tag{17}
$$
这是已把 $\mathcal Z_2$ 一轴准确对准实轴的四个方向。

四点的凸包为中心 $(-A_0,0)$ 的菱形，原点严格在内部。因此
$$
\operatorname{cone}_{+}\{v_0,v_1,v_2,v_3\}=\mathbb R^2.
\tag{18}
$$
也可直接核一个严格正 balance：令 $v_1,v_2,v_3$ 的权重均为 $1$，$v_0$ 权重取
$(3A_0+R_0)/(R_0-A_0)>0$，加权和为零。给任一实目标，先用两个独立列求一个实解，再加足够大的这条正 balance，便使四权全正。权的四次根就是四个真实 profile 模块的正幅度；不是以 signed 成本空间替代实际构造。

## 6. 先固定全部物理包络，再完成目标与第三 range

选择共同合法区间内的一个对称子区间，以 $C_0$ 为中心。其右半侧预留六个互不交的有限包络，左半侧留它们的镜像。有限个基本 bump 与八副本都可先缩小到这些包络，留严格空隙和两个共同外 collar。

具体选择顺序如下。

1. 在第一对包络中放 R319 的正反弱核完整块。右侧基本曲段取 $f=A(y-b)^{5/2}$、$g=w(y)$，$y=x-C_0>0$，$b<\inf\operatorname{supp}w$；原三复矩补包和八副本都先完成。左侧取真实反射，按 R308 的原多项式 ruling 再核其完整三阶，而非假定几何可反射。
2. 第二对包络预放 (11)的强 hook 原型，完成其八副本及镜像。它的 $\mathcal Q_4$ 是一个明确正数。若当前弱核对的值为 $Q_*$，选一个固定复数 $\zeta$ 满足
   $$
   \zeta^4=-Q_*/\mathcal Q_4(\text{该真实原型}).
   $$
   将该原型乘 $\zeta$，通过 (14)及真实幅度实现。原型与弱核块的支撑不交，故四次值相加，准确得到总 $\mathcal Q_4=0$。若 $Q_*=0$ 可不加此块。
3. 剩余四对包络预放第5节的四个模块。使用共同最终宽度与相同八副本幅度，每个镜像取相同实 pair，所以所有加入项保持全局反射偶性。它们的 $m_0=0$、$\mathcal Q_4=0$，且 $m_1$ 向量只是 (17)的同一正倍数。平移不改这里的 $m_1$，因为其原 $m_0=0$；正缩放只乘正因子。
4. 以当前实际残余 (10)的负向量为目标，用 (18)选四个有限正权，再取四次根作为实际幅度。于是整个 $m_1(\theta)$ 对全部相位准确为零。全局仍反射偶，(7)同时给 $m_0=m_2=0$。
5. 最后作一次共同正实归一化，使 $I_0(f,f)=I_0(g,g)=1$。所有已付等式均保持。

所有目标都是先前固定真实 profiles 的有限积分；没有把不同形状积分当成独立自由参数，也没有运行求积来挑选近似根。复四次根只是一次固定有限选择，不声称它在零目标附近给光滑截面。

每个基本原型单独满足三复矩。共同相位、幅度、平移和正缩放保持这一事实；互不交完整块按平方相加。因此最终三个复矩仍全零。弱核块具有真实 $W\ne0$ 开集，新增强模块上 $W=0$，故最终仍为真正导数 rank-two，且没有偷偷增加第二个 hook。

原几何 $M=0$ 给每个完整包 canonical 二阶的真实周期；三矩给整个二阶场的包外局部化。第三 forcing 因而在不同完整块间无跨包乘积。每个块的八副本已使四条实际 ruling 准确为零，而全局 $A_fW=0$ 及右锚给弱 $\mathfrak H(g;f,f)=0$。最后对完整相位 forcing 使用
$$
\mathfrak H(\phi_\theta;f\odot f-\phi_\theta\odot\phi_\theta)
=\sin\theta\,\mathfrak H(g;f,f)=0
$$
施原 range。因此全部新 profiles 的完整三阶仍已支付，包括真实交叉通道、初值、两 collar 与 $\theta=0,\pi$ 种子。

**建设性结论。** 上述同一最终实圆满足
$$
\boxed{
I_j\{\phi_\theta,[W_*,P](\phi_\theta;D_\theta)\}=0,
\qquad j=0,1,2,\quad\text{全部 }\theta.
}
\tag{19}
$$
即整个 $A_{-2,-3}$ 面积函数已零。这里没有把三个外矩的形式数目当作独立 rank；具体两个剩余方向由 (15)–(18)真实实现。

最终固定目标为 $(X+\epsilon Y_f)^*\mathrm e$。它与相位无关，但一般不同于添加修正模块以前的 seed 目标。几何 $X$ 本身没有改变。

## 7. 朝外反射排列在完整一层仍严格失败

现在继续判断同一个真实 profiles 的下一必要门，不能把 (19)记为完整第四成功。

本节不仅适用于第6节所选权，也适用于在其弱曲段外任意添加 $W=0$ 的实强 hook 块。假设所有非零 $W$ 曲段都按如下方式反射配对：右半侧 $y=x-C_0>0$ 上
$$
f=A_\nu(y-b_\nu)^{5/2},\qquad
g=w_\nu(y)\in C_c^\infty(J_\nu),\qquad
b_\nu<\inf J_\nu,
\tag{20}
$$
左半侧取相同 pair 的镜像。$b_\nu$ 可以为负、零或正。朝向与所在半侧在 (20)中已明确固定。

沿 R317，令
$$
C_d=\int(g'')^2\{(f'')^2-(g'')^2\},\qquad
D_4=\int\{(f'')^2-(g'')^2\}^2,
$$
$$
\mathcal J=\int(g'f''-f'g'')\,g''f''',
\qquad
\mathcal J_x=\int x(g'f''-f'g'')f'''g'''.
$$
完整面积第1矩为零给
$$
C_d=-2(\mathcal J+\mathcal J_x).
\tag{21}
$$
取
$$
K=\int_{\text{全部曲段}}(f'')^2(g'')^2>0,\qquad
R=\int_{\text{其余区域}}(f'')^2(g'')^2\ge0.
\tag{22}
$$
新增强模块只进入 $R$；它们的 $W=0$，不进入 $\mathcal J,\mathcal J_x$。

置 $\lambda_\nu=75A_\nu^2/16$，右侧与镜像的准确计算给
$$
\begin{aligned}
K&=6\sum_\nu\lambda_\nu\int(y-b_\nu)(w_\nu'')^2,\\
\mathcal J&=-K/3,\qquad
\mathcal J_x=-\sum_\nu\lambda_\nu\int(y+b_\nu)(w_\nu'')^2.
\end{aligned}
\tag{23}
$$
保留物理 $x=C_0\pm y$ 的两项后，中心常数准确相消，(21)成为
$$
C_d=2\sum_\nu\lambda_\nu
\int(3y-b_\nu)(w_\nu'')^2
=\frac K3+
4\sum_\nu\lambda_\nu\int y(w_\nu'')^2 .
$$
因为右侧 $y>0$，
$$
\boxed{C_d>K/3.}
\tag{24}
$$
这正是仅移动负分支点不能解决的限制。它来自同一实际面积及朝向排列，不能独立指定 $C_d$ 与 $K$。

完整全角 $m_1=0$ 还迫 $\mathcal Q_4=0$。写
$$
A_4=\int(f'')^4,\quad C_{22}=\int(f'')^2(g'')^2=K+R,\quad
E_4=\int(g'')^4 ,
$$
则其真实实部给 $A_4+E_4=6C_{22}$，故
$$
\boxed{D_4=4(K+R).}
\tag{25}
$$

若希望继续到完整第四，R317 的三个 directed 必要行也必须为零。它们并非由本稿的面积构造自动支付；若任一个不为零，已经失败。若都为零，R317 完整 local、chain、history 合成后的准确一层为
$$
[\sigma h^{-2}j^0]\mathscr R_{-3,\pi/2}
=B_\kappa\left\{
\frac{N(t)}{24P(t)}D_4+\mathcal J+\frac{7C_d}{12}
\right\},
\tag{26}
$$
其中
$$
B_\kappa=
\frac{(41t^2+27)P(t)}
{2592h_e^3(51t^2+2t+8)}>0,
$$
$$
N(t)=16+184t-1713t^2-2475t^3-4590t^4,
$$
$$
P(t)=8+114t-169t^2+231t^3-612t^4.
$$
代入 (23)–(25)，括号为
$$
\frac1{12}\left\{
\frac{2N(t)}{P(t)}(K+R)-4K+7C_d
\right\}.
\tag{27}
$$
在 $0<t<1/100$，
$$
2N-3P=8+26t-2919t^2-5643t^3-7344t^4>0,
$$
所以 $2N/P>3$。由 (24)，(27)严格大于
$$
\frac1{12}\left\{
\left(\frac{2N}{P}-\frac53\right)K
+\frac{2N}{P}R
\right\}
>\frac K9 .
$$
因此
$$
\boxed{
[\sigma h^{-2}j^0]\mathscr R_{-3,\pi/2}
>B_\kappa K/9>0.
}
\tag{28}
$$

**严格范围。** 当前朝外反射排列的真正弱 hook/rank-two 圆，连同任意上述强 hook 修正块，均不能满足完整第四 ruling。该结论保留负分支点，也不依赖第6节选择了哪一组正权。原 Gaussian 词独立性和合法 gauge 偶部商使 (28)不能由其他 history 或中心初值吸收。

## 8. 已完成内容与下一真实分叉

本稿完整实现了三阶弱核圆及整个 $A_{-2,-3}$ 面积的三个全角外矩，随后对同一朝外排列给出了严格第四否定。两项结论不矛盾：面积只是完整第四系统的一部分。

下一未排通道必须真正改变曲段朝向与反射半侧的关系。例如把右半侧改为左向 $f=A(b-y)^{5/2}$，(24)的严格号便不能原样使用。但新的面积、directed 行与一层仍须对同一实际 profiles 联立支付，不能只从一个系数变号宣布可行。

本稿不把其他 Gaussian 面积、对称乘积、零/一层全部函数、第四周期或平台条件列为已付；也不由有限三阶 Taylor 圆推出固定非零参数的准确等距族。
