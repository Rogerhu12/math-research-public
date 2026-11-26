# R582：实际圆核背景的真实全平尾核与共振入口

**已证明；原式纸证。**

2026-11-26，Astra-new-mechanism-0105020f-20261126。本文从已完成圆核 run 的实际 17 个均值系数出发，证明其真实尾部拥有非零、在开平帽上准确为零的角频二无穷小等距种子。不是把 R569 零系数背景的种子或数值 jets 原样挪过来。纸证同时覆盖原均值系数盒，保留 R569 的起始 cell 160 和定量递推常数。本稿未运行新的科学数值；有限外端传递、核心共振、有限非圆分支和全部几何门仍须继续支付。

## 1. 实际输入和准确数学轮廓

输入为 run 45778418134、job 139767648038、source 668a3f6c6aee92b00c5ca547dd7677d257d0cdc0 的 stage 0。原日志 1042984 bytes、SHA256 7a1a626217d090742fed665049c96c4124a49b68d0d051c85fa6d305765f964d；stage-0 FINAL 21505 bytes、SHA256 a78102463e4a816d00e000c969372af423a41ee93ab4996574b16048265b9324。原日志只在原 Actions/scratch，本文仅保留必要小配置与摘要。

其前 64 个角系数全为 0。依源码顺序，后 17 个参数是：

    loga:
    -0.35001924628214787, -0.3531732092117735,
    -0.3244617668413918, -0.43706812962213554,
    -0.5435744674362258, -0.3821726524975292,
    -0.5654097637847235, -0.5041937321653266
    z:
    0, -0.0013474117462880936,
    -0.09175492884312668, -0.15680738719807807,
    -0.05955223441757437, -0.19856521037391323,
    -0.5877276747743894, 0.09658185324267708
    cap height:
    0.6747017055797783

准确解析身份取上述有限十进制数为固定实参数；后续浮点求值及其误差另记。circle p=q=.18、rounding=.2，核心圆半径 .38。径向长度 L=9/10，开柱领末点 s_c=9/250=.036，W=L-s_c=108/125=.864；帽盘半径 r_c=11/50，ell=1/5，kappa=W/ell=108/25=4.32。

参考源码为 inverse_flat_oscillatory_tail_20261126.py（SHA256 b9c778fbeafb0d9beb061b3f472b8db1661daec5a78a63eb886a8e4770574f9b）以及其绑定的 inverse_rotational_metric_20261126.py（e25dff6a411e8edc485babe6545087cfbea2b6d16cd804e6dcb51f17d8fab319）。最后 .08 的实际公式是
\[
 r_0(s)=r_c+L-s,\quad
 a(s)=r_0(s)e^{\alpha(s)},\quad
 z(s)=h+H(s)+Z(s),                                  \tag{1}
\]
\[
 \alpha=\beta P_a,\quad Z=\beta P_z,\quad
 H_s=w_0,\quad
 w_0(s)=\tfrac1{10}
 e^{-(2-\sin\delta^{-2})/\delta},\quad
 \delta=(L-s)/\ell.                                  \tag{2}
\]
H 是 R566 的准确积分定义；不把浮点求积截断变成数学轮廓。
\[
 x=(s-s_c)/W,\quad
 \lambda=-x^{-1}+(1-x)^{-1},\quad
 \chi=(1+e^{-\lambda})^{-1},\quad
 \beta=4\chi(1-\chi).                                 \tag{3}
\]
P_a,P_z 是源码的八个、次数五、内部结点 1/3 和 2/3 的 clamped B 样条组合。本文证明对盒
\[
 |c_{a,i}|\le3/2,\qquad |c_{z,i}|\le1                \tag{4}
\]
统一成立；已识别实际输入在这个盒内。最后一个多项式片为 .612<s<.9，所以本文靠帽的所有函数均在同一个光滑多项式片内。

## 2. 实际权的变换，不能冻结 r 或 a_s

置
\[
 u=\delta^{-2},\quad s(u)=L-\ell u^{-1/2},\quad
 s_u=\tfrac1{10}u^{-3/2},\quad r(u)=a(s(u)).
                                                               \tag{5}
\]
第 3–4 节将对 u>=1000 证明 a_s<0、z_s>0。故真实图像斜率为
\[
 w_{\rm eff}(r)=-\frac{z_s}{a_s}>0,\qquad h_r=-w_{\rm eff}.       \tag{6}
\]
角频二标量方程是
\[
 (w_{\rm eff}f_r)_r-4\frac{(w_{\rm eff})_r}{r}f=0.               \tag{7}
\]
令 f=r^4 y。先在真实半径 r 中精确得到
\[
 (w_{\rm eff}r^8y_r)_r+12w_{\rm eff}r^6y=0.
\]
再用 r_u=a_s s_u<0 变换：
\[
 (P y_u)_u+\varepsilon P y=0,                                  \tag{8}
\]
\[
 \boxed{P=\frac{w_{\rm eff}r^8}{-r_u}
       =\frac{z_s r^8}{a_s^2s_u},\qquad
 \varepsilon=\frac{12r_u^2}{r^2}.}                              \tag{9}
\]
两个因子 a_s 都必须保留。只替换 w 而仍使用 r=r_0 或 r_u=-s_u，会给另一个方程。

比较权记为
\[
 P_0=u^{3/2}r_0(u)^8e^{-\sqrt u(2-\sin u)},\qquad
 \varepsilon_0=\frac{.12}{r_0(u)^2u^3}.                         \tag{10}
\]
这只是估计用的零系数权；实际 cell、DtN 和 seed 必须用 (9)。

## 3. 可逐项核对的导数估计

本节撇号全部表示 u 导数，标 s 才表示 s 导数。对 u>=1000，
\[
 t=1-x=\frac1{\kappa\sqrt u}<\frac1{128},\qquad
 \lambda=\kappa\sqrt u-x^{-1}.
\]
直接微分给
\[
 |\lambda'|\le3u^{-1/2},\quad
 |\lambda''|\le2u^{-3/2},\quad
 |\lambda'''|\le3u^{-5/2}.                                    \tag{11}
\]
例如
\[
 \lambda'=\frac{\kappa}{2\sqrt u}+\frac{t}{2ux^2},\qquad
 \lambda''=-\frac{\kappa}{4u^{3/2}}
             -\frac{3t}{4u^2x^2}-\frac{t^2}{2u^2x^3},
\]
\[
 \lambda'''=\frac{3\kappa}{8u^{5/2}}
 +\frac{15t}{8u^3x^2}+\frac{9t^2}{4u^3x^3}+\frac{3t^3}{4u^3x^4}.
\]
又 x>127/128，e^{1/x}<3，因此
\[
 0<\beta\le12e^{-\kappa\sqrt u}.                               \tag{12}
\]
令 q_l=\chi(1-\chi)、b_l=1-2\chi。对 lambda 的前三导数比为
b_l、1-6q_l、b_l(1-12q_l)，绝对值分别不超过 1、1、2。结合 (11) 得
\[
 |\beta'|\le3\beta u^{-1/2},\quad
 |\beta''|\le10\beta u^{-1},\quad
 |\beta'''|\le60\beta u^{-3/2}.                               \tag{13}
\]

若 P 是盒幅 C 的上述 B 样条组合，正基和微分系数公式给
\[
 |P_{s^k}|\le40^k C\quad(0\le k\le3).                         \tag{14}
\]
这里每次微分的系数差至多 2 倍，次数至多 5，最小正 knot gap 为 1/3，而 30/W<40；重结点的零长度项按 B 样条公式消去，不取零分母。用 (5) 的前三导数进一步得到
\[
 |P|\le C,\quad |P'|\le4Cu^{-3/2},\quad
 |P''|\le7Cu^{-5/2},\quad |P'''|\le18Cu^{-7/2}.                 \tag{15}
\]
将 (13)(15) 相乘，先对 Z=beta P_z：
\[
 |Z'|\le4\beta u^{-1/2},\quad
 |Z''|\le11\beta u^{-1},\quad
 |Z'''|\le61\beta u^{-3/2}.                                  \tag{16}
\]
记 B=Z_s=10u^{3/2}Z'，则
\[
 |B|\le40\beta u,\quad |B'|\le112\beta\sqrt u,\quad
 |B''|\le622\beta.                                           \tag{17}
\]
例如 B''=7.5u^{-1/2}Z'+30u^{1/2}Z''+10u^{3/2}Z'''；三个界的和为
beta(30/u+330/sqrt(u)+610)<622 beta。对 alpha 将 (16)(17) 各乘 3/2。

令
\[
 A=r_0\alpha_s,\qquad b=B/w_0,\qquad
 E(u)=e^{-1.32\sqrt u}.
\]
因 r_0<1/4，r_0'=-.1u^{-3/2}，有
\[
 |A|\le15\beta u,\quad |A'|\le43\beta\sqrt u,\quad
 |A''|\le234\beta.                                           \tag{18}
\]
而 w_0>=.1e^{-3sqrt(u)}，故 beta/w_0<=120E。写 l=log w_0，
\[
 |l'|\le2\sqrt u,\qquad |l''|\le2\sqrt u.
\]
利用
\[
 b'=B'/w_0-b l',\quad
 b''=B''/w_0-2l'B'/w_0+\{(l')^2-l''\}b
\]
以及 (17)，逐项得到
\[
 |b|\le4800uE,\quad
 |b'|\le9720u^{3/2}E,\quad
 |b''|\le19680u^2E.                                         \tag{19}
\]

为核对所有“小”的声明，无须数值试跑：sqrt(1000)>31.6，
e^5>142（有限 Taylor 下界），e^{1.5}>4，故
\[
 e^{1.32\sqrt{1000}}>e^{41.5}>6.4\cdot10^{17}.                 \tag{20}
\]
各个 u^m E(u)，m<=2，在 u>=1000 递减。由此 (18)(19) 给
|A|<1/100、|b|<1/100，且 beta<=E。因此
\[
 a_s=e^\alpha(-1+A)<0,\qquad z_s=w_0(1+b)>0.                  \tag{21}
\]
这是真实 a,z 的符号结论，而不是只对零系数背景的结论。

## 4. 实际 log 权的二阶小扰动

式 (9) 中 r^8=e^{8alpha}r_0^8、a_s^2=e^{2alpha}(1-A)^2，所以有准确恒等式
\[
 d(u):=\log(P/P_0)=\log(1+b)+6\alpha-2\log(1-A),              \tag{22}
\]
\[
 \varepsilon=\varepsilon_0(1-A)^2.                          \tag{23}
\]
特别 epsilon 中的 e^{2alpha} 完全抵消。

用 |A|,|b|<1/2、(16)–(19)，
\[
 |d|\le2|b|+6|\alpha|+4|A|<10^4uE,
\]
\[
 |d'|\le2|b'|+6|\alpha'|+4|A'|<2\cdot10^4u^{3/2}E,
\]
\[
 |d''|\le2|b''|+4|b'|^2+6|\alpha''|
                    +4|A''|+8|A'|^2<4\cdot10^4u^2E.        \tag{24}
\]
最后一行主项为 39360u^2E；由 (20) 得
4(9720)^2 uE<1，故 4|b'|^2<u^2E，其余项也严格被余下常数覆盖。
因此在整个 u>=1000，
\[
 \boxed{|d|<2\cdot10^{-11},\quad |d'|<10^{-9},\quad
 |d''|<7\cdot10^{-8}.}                                      \tag{25}
\]
对每个固定更高阶，直接继续微分 (22) 可得某个固定多项式乘 E 的界：x 和 1-A、1+b 的分母统一离零，P_a,P_z 在本段为有限多项式，而 w_0 的 log 导数仅按 u 的幂增长。这里不声称所有阶共用同一个常数。

## 5. 同一 160 号起始 cell 保持成立

R569 的比较权满足
\[
 (\log P_0)'=\sqrt u(\cos u-\eta(u)),
\quad
 \eta=\frac{2-\sin u}{2u}-\frac3{2u^{3/2}}
                     +\frac{.8}{r_0u^2}.
\]
在 u>=1000 可直接加强原估计为
\[
 \frac{.45}{u}<\eta<\frac{1.6}{u},\qquad |\eta'|<.0006.
\]
实际权则有
\[
 (\log P)'=\sqrt u(\cos u-\widetilde\eta),\qquad
 \widetilde\eta=\eta-d'/\sqrt u.
\]
由 (20)(24)，|d'|/sqrt(u)<1/(100u)，且
|d''|/sqrt(u)+|d'|/(2u^{3/2})<10^{-6}。所以
\[
 0<\widetilde\eta<.002,\qquad |\widetilde\eta'|<.001.          \tag{26}
\]
由 R569 同一个单调根论证，对每个 n>=160，实际 P 有唯一极大点
\[
 \alpha_n\in(\pi/2+2\pi n-.003,\ \pi/2+2\pi n)
\]
和唯一极小点
\[
 \gamma_n\in(3\pi/2+2\pi n,\ 3\pi/2+2\pi n+.003).
\]
I_n=[alpha_n,alpha_{n+1}] 是实际 P 的单谷 cell，6<|I_n|<7，
alpha_160>1000。这里 alpha_n 是实际权的根，不能借用旧 P_0 的已付根值。

还需保持 cell 中的权与势常数。记 a=alpha_n、C_a=r_c^8 a^{3/2}。在 a<=u<a+7，
\[
 \frac{P(u)}{C_a e^{-\sqrt a(2-\sin u)}}
 = (u/a)^{3/2}(r_0/r_c)^8
   e^{-(\sqrt u-\sqrt a)(2-\sin u)}e^d.
\]
其下界大于 e^{-.350001}>1/2。上界可用
(u/a)^{3/2}<1.015、
(r_0/r_c)^8<(34/33)^8<=33/25、
e^d<1.000001，故小于 2。因此仍有准确同一界
\[
 \tfrac12 C_a e^{-\sqrt a(2-\sin u)}
 \le P(u)\le2C_a e^{-\sqrt a(2-\sin u)}.                     \tag{27}
\]
由 r_c<r_0<.227、|A|<.01 和 (23)，也仍有
\[
 a^{-3}\le\varepsilon(u)\le3a^{-3}\qquad(u\in I_n).          \tag{28}
\]
下界可直接用 u<a+7、a>=1000：
epsilon>=.12(.99)^2/[.227^2(a+7)^3]>a^{-3}。
上界用 u>=a：
epsilon<=.12(1.01)^2/(.22^2 a^3)<3a^{-3}。
此处不能把 u^{-3} 的下界方向写反。

## 6. 真实 DtN 极限产生唯一一维全平标量核

现在可以使用 R569 §4 的任意单谷正权 Green/Dirichlet 引理。它不要求权有某个封闭形式，也不含 max P/min P；其 C0=49/2。由于 (26)–(28) 保持 R569 §5–6 的全部实际假设，实际 cell 的精确 DtN 矩阵 D_n 和
\[
 k_n=-D_{n,LR}>0,\qquad
 V_n=-(D_{n-1,RR}+D_{n,LL})>0
\]
满足同一对角占优界
\[
 k_{n-1}/V_n,\ k_n/V_n
 \le {\cal R}(\alpha_n),\quad
 {\cal R}(a)=512a^3e^{-3\sqrt a/2}<1/64.
\]
该步骤使用实际 (P,epsilon) 的 cell ODE；并未用旧源的任何浮点 DtN 记录。

令 y_160=1，y_n=(-1)^{n-160}x_n，x_n/x_{n-1}=rho_n。以
\[
 \rho_n=\frac{k_{n-1}}{V_n-k_n\rho_{n+1}},\qquad
 \rho_{M+1}=0
\]
向外递推，再取 M->infinity。各映射将 [0,1/32] 映入自身，导数小于 10^{-3}，所以有同一明确误差
\[
 |\rho_n-\rho_n^{(M)}|
 \le \tfrac1{32}10^{-3(M-n+1)}.                              \tag{29}
\]
这是精确 DtN 输入的截断误差，仍不包含后续数值 ODE/求积误差。

在每个实际 cell 上，用端值及其真实 Dirichlet 插值解拼出 y；通量匹配保证准确解 (8)。同 R569 的乘积估计，
\[
 |y(u)|\le C e^{-c u^{3/2}}.
\]
P 的 log 导数及各固定阶导数按 u 的某个幂增长，(25) 的扰动不会破坏 cell 内导数估计。r_u=a_s s_u，且 a_s->-1，所以 d/dr=(a_s s_u)^{-1}d/du 每个固定阶只增加多项式因子。因此
\[
 f(r)=r^4y(u(r)),\qquad
 |f^{(j)}(r)|\le C_j e^{-c_j/\delta^3}                       \tag{30}
\]
对每个固定 j 成立。它在 r=r_c 全平，且 y(alpha_160)=1，因而非零。

在所选实 cos(2theta) 对称类中，标量全平解空间恰为一维。若 f_1,f_2 都全平，则 y_i=r^{-4}f_i 及 y_i' 在 u->infinity 仅乘多项式后仍趋零，而 P->0；故常数 Wronskian
P(y_1y_2'-y_1'y_2) 的极限为 0，因而恒为 0。二阶 ODE 的唯一性给线性相关。上面的非零构造支付维数至少一。

## 7. 完整向量种子及真正可接接口

在实际近帽图 X_0(r,theta)=r e_r+h(r)e_z 上，置
\[
 {\cal A}=\frac{w_{\rm eff}(4f-rf_r)}3,\quad
 {\cal B}=-{\cal A}/2,\quad {\cal C}=f,
\]
\[
 V={\cal A}\cos2\theta\,e_r+
   {\cal B}\sin2\theta\,e_\theta+
   {\cal C}\cos2\theta\,e_z.                                \tag{31}
\]
由 (7)，A_r=w_eff f_r，再直接核对 rr、rtheta、thetatheta 三个分量，即
2 sym<dX_0,dV>=0。式 (30) 与实际 w_eff 的全平性保证 A,B,C 全部全平，因此 V=0 延拓到整个 r<=r_c 的开平盘时光滑。这是实际圆背景的非零局部无穷小等距场。非零环境刚体速度不能在开平盘上恒零。

其真实入口可取 s_*=L-ell/sqrt(alpha_160)，实际半径 r_*=a(s_*)；通过实际 (8) 再向外延伸至一个实际满足 a_s<0、z_s>0 的有限口。不能把 s_*=L-ell/sqrt(alpha_160) 的 r_* 偷换为 r_c+ell/sqrt(alpha_160)。向原 frame 模型添加的真实角列是
\[
 u_2(s)=\frac{3{\cal A}(s)}{2a(s)},\qquad
 v_2(s)=-\frac{2{\cal C}(s)}{a(s)},                          \tag{32}
\]
分别乘 sin(2theta)。它们是 R580 所缺的非多项式全平列；由 (30)，除以旧 beta 后仍全平，但不属于最后一个有限多项式片。

在一般圆 meridian 中，完整一阶方程仍是 R580 的
\[
 a_s{\cal A}_s+z_s{\cal C}_s=0,\qquad
 a{\cal A}_s+3a_s{\cal A}+4z_s{\cal C}=0.                    \tag{33}
\]
在 z_s!=0 的连接上，
\[
 \binom{{\cal A}}{{\cal C}}_s
 =\begin{pmatrix}
 -3a_s/a&-4z_s/a\\
 3a_s^2/(az_s)&4a_s/a
 \end{pmatrix}
 \binom{{\cal A}}{{\cal C}}.                                \tag{34}
\]
本稿只证明 u>=1000 的真实 z_s>0。它没有检查整个原中段 z_s 的符号；若途中 z_s=0，必须使用 (33) 支付正则传递/兼容，不能在 (34) 中隐式除零。当前圆核有限网格几何合格也不能替代该连续检查。

到开柱核心，所需条件仍为 C_core=0、A_core!=0，再按 A_core 归一为真实 p-forcing 的 1/2。尾核的一维性说明，单改种子倍数不能消去非零 C_core；必须调实际均值轮廓或一个明确的新尾相位，并重新计算对应种子/传递。若调整支撑完全在种子入口之外，尾部精确输入不变；这只限制均值调节的支撑，不冻结非径向尾部自由。

## 8. 后续计算的确切边界

下一新入口可以用上述实际 (P,epsilon)、真实 alpha_n 和 (29) 定义规范 seed，采用原已识别 circle 小配置；先输出其实际有限口 jets 和 C2 尺度，再沿实际圆 meridian 处理 (33)，找 C_core=0。应记录所有实际 ODE/求积成本以及数值误差；不能把精确 DtN 的 (29) 当成完整浮点误差证书。必要的 M/精度比较属于同一正式新 run，不在本地另开科学检查。

R582 已支付真实圆背景的非零近帽全平核及其唯一标量方向，修复了 R580 指出的有限尾列缺失。尚未支付核心返回、有限非圆预测后的非线性度量修正、整闭面的连续几何/reach 和固定 g 精化。当前强非圆 theta 路线仍按其原物理/实际终态独立继续；本稿不会改判任何旧失败或正在运行的范围。
