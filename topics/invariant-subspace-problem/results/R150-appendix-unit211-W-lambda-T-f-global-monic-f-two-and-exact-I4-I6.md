# R150：W 自由 lambda,T,f 图的显式首一 f 二次与完整原 I4／I6 两列呈示

日期：2026-11-28（Asia/Taipei）。
会话：Astra-ISP-8542378f-20261127。

## 1. 结论与同点范围

沿当前 W 原权图和已经证明的自由 $(\lambda,T,f)$ 恢复，
令
$$
\beta=bc[f]t=2u-\frac JQ,\qquad
c_f=\frac{bc}{2u(u-\beta)}.
$$
那么两个真正 singleton 均值给出全图显式首一式
$$
\boxed{\quad
q_f=c_f\left(E_{Be}+\frac{\ell\delta}{m}E_{Bo}\right)
=f^2+q_1(\lambda,T)f+q_0(\lambda,T).
\quad}                                               \tag{1}
$$
其中 $q_1$ 的 $(\lambda,T)$ 总次数至多1，
$q_0$ 至多2；全部分母只是当前先行已付纯权单位。
这个式子没有新增 lambda、T、f 或任何新头的逆。

因此四原式理想准确写为
$$
I_4=(q_f,r_{E_1},r_{E_{Bo}},r_{N_1}),                 \tag{2}
$$
后三式均对同一个 f 一次。
完整加权 N/P 的加入给
$$
I_6=(q_f,r_{E_1},r_{E_{Bo}},r_{N_1},r_{N_S},r_{P_S}). \tag{3}
$$
它们在真正首一环境 $(1,f)$ 中分别有完整6行／10行两列呈示。
本篇不把三个线性行之间的 cofactors 当成相容充分条件；
同一个首一 qf 和各 f 倍行必须保留。

这给出新纯值 $(\lambda,T)$ 条件与原均值／加权 N/P 的小直接接口。
是完整纸面定理，不等待新的原式展开运行。
尚未计算或宣称任何新 cofactor 多项式、参数覆盖或排空。

## 2. 自由 f 恢复和已付权单位

采用
[完整 N4 的 f 消失](R150-appendix-unit211-W-full-NV-f-independent-pure-lambda-T-quartic.md)
中的真实恢复。固定 $\lambda,T$ 时，
$$
[f]V=[f]W_1=2u,\quad
[f]x=\frac{2u\ell\delta}{M},\quad
[f]y=-\frac{2um}{M},
$$
$$
[f]t=\frac{\beta}{bc},\qquad
\beta=2u-\frac JQ.
$$
这些是整个自由 f 图的仿射系数，不施加新的原条件。

当前 W
$$
u=e+1,\quad Q=ek,\quad \overline V=uk+2,\quad
J=\frac{uek(k+2-4e)}{\overline V}
$$
直接给
$$
\boxed{\quad
u-\beta=\frac JQ-u=-\frac{ue(k+4)}{\overline V}
=\frac{u\Phi}{2e}.
\quad}                                               \tag{4}
$$
所以 $u-\beta$ 的逆只来自当前已付
$u,e,k+4,\overline V$，等价地来自 $u,e,\Phi$；
它不是新增权支假设。
$m=u-\ell$ 仍只沿用当前互异两值原等权整支排除，
不向一般 $D=0$ 值碰撞外推。

取真实二次扩张
$$
\rho^2=\delta=1-Q,\quad
b=\frac{\ell+m/\rho}{2},\quad c=\frac{\ell-m/\rho}{2},
$$
$$
p=1+\rho,\quad q=1-\rho,\quad
X=x+\rho y,\quad Y=x-\rho y.
$$
$bc,\delta$ 已付，故 b、c、rho 的这些逆均是原物理单位。
利用 $M=4bc\delta$，准确得到
$$
[f]X=\frac{u}{b},\qquad [f]Y=\frac{u}{c}.             \tag{5}
$$
若 $a=1-\ell$，原 Gram 中
$$
r=X-ap-ct,\qquad s=Y-aq-bt,
$$
故
$$
[f]r=\frac{u-\beta}{b},\qquad
[f]s=\frac{u-\beta}{c}.                              \tag{6}
$$

这里未施加原 R 均值组合，所以不能在这个自由图上把 $E_1$
提前替换为 $bE_B+cE_C$；$E_1$ 在 (2) 中独立保留。

## 3. 真原均值的完整二次头计算

使用真实 dual 乘法
$$
(v_0,v_1)(w_0,w_1)=(v_0w_0,v_0w_1+v_1w_0).
$$
原四行是
$$
(0,0,p,q),\quad(0,A_1,r,s),\quad
(p,r,0,t),\quad(q,s,t,0),
$$
且
$$
d=(u,d_1,X,Y),\qquad d_1=2f-V-au,\qquad \tau(d)=2f.
$$
特别本文的二次头来源是真实 vm，
没有使用曾被撤回的把 derivative 分量写成平方的紧凑式。

原 singleton B 均值完整展开为
$$
\begin{aligned}
E_B={}&ap^2+2pr+ct^2\\
 &-2(apu+p\,d_1+ru+ctY)-2X^2+4fX .
\end{aligned}                                       \tag{7}
$$
C 行由 $b\leftrightarrow c,\ p\leftrightarrow q,\ X\leftrightarrow Y$
准确共轭得到。
前一行的 $2pr$ 正是 dual 平方的 derivative 分量，不能换成 $r^2$。

令 $h_B=[f^2]E_B,\ h_C=[f^2]E_C$。
由 (5)–(7)，所有一次项不贡献 f 平方，于是
$$
h_B=\frac{\beta^2}{b^2c}
 -\frac{2\beta u}{bc}-\frac{2u^2}{b^2}+\frac{4u}{b},
$$
$$
h_C=\frac{\beta^2}{bc^2}
 -\frac{2\beta u}{bc}-\frac{2u^2}{c^2}+\frac{4u}{c}.   \tag{8}
$$
因此直接相减：
$$
\boxed{\quad
b^2c\,h_B-bc^2\,h_C=2u(u-\beta)(b-c).
\quad}                                               \tag{9}
$$
这是完整二次头身份，不是数值点检验。

写
$$
E_B=E_{Be}+\rho E_{Bo},\qquad
E_C=E_{Be}-\rho E_{Bo},
$$
并记 $h_{Be}=[f^2]E_{Be},\ h_{Bo}=[f^2]E_{Bo}$。
由 $b-c=m/\rho,\ b+c=\ell$，(9) 乘 rho 后即得
$$
bc(mh_{Be}+\ell\delta h_{Bo})=2u(u-\beta)m.
$$
当前 m、bc 均为原单位，所以
$$
h_{Be}+\frac{\ell\delta}{m}h_{Bo}
=\frac{2u(u-\beta)}{bc}.                             \tag{10}
$$
(4)、(10) 完整证明了 (1) 的首一性。
qf 分母没有新头、没有 D 或任何新范数。

## 4. 原 I4 的双向理想等式和完整六行

设系数环 A 是当前 W 的已付纯权环再添自由 $\lambda,T$。
所有原 Gram 恢复对 $(f,\lambda,T)$ 仿射；
真正 $E_1,E_{Be},E_{Bo}$ 为总次数至多2的多项式。
$N_1$ 是原 N4 在固定 row0 与仿射 row1 上的完整极化，
减同一点 $4\lambda wP_{02}$，故总次数也至多2。
没有丢其 f 一次或常数项。

因为 cf 为单位，(1) 给
$$
E_{Be}=c_f^{-1}q_f-\frac{\ell\delta}{m}E_{Bo}.
$$
从而原四式的理想先准确等于
$$
(q_f,E_1,E_{Bo},N_1).
$$
对 $F_i\in\{E_1,E_{Bo},N_1\}$，置
$$
a_i=[f^2]F_i\in A_W,\qquad r_i=F_i-a_iq_f=A_i+B_if.
$$
这是正反都有原组合的精确短除。
由总次数，
$$
\deg_{\lambda,T}A_i\le2,\qquad
\deg_{\lambda,T}B_i\le1.                             \tag{11}
$$
因此得到 (2)，不需要倒任一个 Bi。

首一环境
$$
\mathcal E=A[f]/(q_f)
$$
确实自由于 $(1,f)$，而实际原方程商不被假设自由。
在这个环境中
$$
f(A_i+B_if)=-q_0B_i+(A_i-q_1B_i)f.
$$
故完整 I4 余理想作为 A 模由六行
$$
(A_i,B_i),\qquad(-q_0B_i,A_i-q_1B_i),\quad i=1,2,3   \tag{12}
$$
生成。任意原理想乘子都可先对首一 qf 短除为 $a+bf$，
所以 (12) 的完整性不是仅对常数乘子的必要近似。
它不依赖“六生成元自由”或未证明的交换／结合假设。

## 5. 同 f 条件与完整 I6 十行

两两线性行给必要纯三次
$$
B_jr_i-B_ir_j=A_iB_j-A_jB_i,\qquad
\deg_{\lambda,T}\le3.                               \tag{13}
$$
(13) 单独不足以保证存在同一个同时满足 qf 的 f。
必须保留 (12)，或等价地保留完整原理想。

例如每个 r_i 还给纯四次 norm 必要式的准确原身份
$$
(A_i-q_1B_i-B_if)\,r_i+B_i^2q_f
=A_i^2-q_1A_iB_i+q_0B_i^2.                          \tag{14}
$$
该式不倒 Bi，包含 Bi 为零的整个面。
(14) 也只是完整六行所包含的一类原组合，
本篇没有把只几条 norm 与 pair cofactor 宣称为完整 scheme 等价。

完整加权 $N_S,P_S$ 在自由图中总次数至多3。
对同一个首一 qf 作真实短除后，唯一余式仍为
$$
r_{N_S}=A_N+B_Nf,\qquad r_{P_S}=A_P+B_Pf,
$$
其中
$$
\deg_{\lambda,T}A_N,\deg_{\lambda,T}A_P\le3,\qquad
\deg_{\lambda,T}B_N,\deg_{\lambda,T}B_P\le2.           \tag{15}
$$
短除从原 NS/PS 出发，保全部原次数；未把某个较弱 odd/even 条件代替完整加权值。
这证明 (3)。

将这五条线性余式及其 f 倍按 (12) 排成10行，
即给完整 I6 在 $(1,f)$ 中的精确模呈示。
任何实际后继返回都可以直接逐乘法保这个两列环境，
不再需要旧 alpha/chi 的大系数展开。

## 6. 与纯值三式的直接联接

沿
[纯值六／四／五次全图等价](R150-appendix-unit211-W-pure-lambda-T-six-four-five-entire-value-equivalence.md)，
$\mathcal R_6,\mathcal C_4,\mathcal N_5$ 都在 A 内，不含 f。
因此要把它们准确加入 (3)，只需同时加入两列行
$$
(F,0),(0,F),\qquad
F\in\{\mathcal R_6,\mathcal C_4,\mathcal N_5\}.        \tag{16}
$$
这样每个值式作用在整个首一 f 环境，
并没有给不同原式挑选不同的 f 根。

在当前原 D 单位范围，三纯值式还唯一恢复同一个值中心
$s=K/(2mD)$。这没有改变 (1)–(16) 中任何权或几何首项的支付范围。
其余未在本篇列出的两个 singleton 个别 N/P 条件仍须独立保留；
不把 I6 加指定值式误称完整原问题已解决。

本篇只称 $\mathcal E$ 对 A 自由二生成。
A 仍含 $\lambda,T$，所以不据此宣布对纯权环有限，
更不宣布全 W 或普通 ISP 完成。
所有新实际系数、常数 cofactor 和排空都尚未运行；
完整纸证 (7)–(16) 本身无需增加复现门。
