# R488 — 共同 A 的 odd29 绝对核心、完整四态及实际偶深 D8 返回

日期：2026-11-14。**状态：已证明。**

本篇在 R465 的同一个六 sigma 联合上，只把固定普通 ray 再细分一次
模 $29$。四个共同输入的总和 $A$ 有实际 odd degree $29$ 标量核心；
其绝对标量平方由两个原 sigma 的完整联合支付。保原四挠中心后，
第二状态的 $A,c,d$ 核在四个完整来源中闭合。取 $A$ 的两层限制，
与原 $W$ 核进一步在三个真实且线性独立的来源上给出 $D_8$。

这些是改变原第一输出的真实限制关系。文末写出每个物理变换、全部
共同伴随和一个八字词的准确像格；来源算子乘积为一，并不使物理
像格成为全域。主目标尚未完成。

## 1. 原规范与一个固定 mod29 细分

沿用 R454、R465 的原 $b=17$、微分、普通周期和
$$
\delta=1+2\omega,\qquad
\gamma=(5+\delta)/2,\qquad
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad
\pi_{17}=-\pi_0.
\tag{1}
$$
原 sigma 的完整核心是 $-\lambda$；$\kappa$ 的赋值为一。
旧 ray 为
$$
\pi_0\equiv1428552127+2161889730\omega\pmod{2793510720}.
$$
追加 $\pi_0\equiv2\pmod{29}$，完整 CRT 给
$$
\boxed{\pi_0\equiv23776637887+77586679170\omega
                   \pmod{81011810880}.}
\tag{2}
$$
两个 CRT 增量是旧模数的 $8,27$ 倍。新类的范数余数为
$60309924679$，与新模数互素。故 R454 所用的同一个 CM ray-class
素理想定理仍给固定正密度普通子族。所有旧条件保留；与 R487 的
固定 $13,19$ 幂细分也相容，因为新增模数只多一个 $29$。

写 $g=\pi_0/\bar\pi_0$。精确同余为
$$
\boxed{
g\equiv1\pmod{58},\qquad
g\equiv27+8\omega\pmod{32},\qquad
g\equiv59+232\omega\pmod{928},\qquad
g\equiv19\pmod{36}.}
\tag{3}
$$
特别 $g^4\equiv465=1+464\pmod{928}$。
仍有 $p>19$、$p\equiv7\pmod{64}$、$p\equiv1\pmod3$，故 $p\ge71$。
下面的固定坐标分母均为单位。

## 2. 保留四个独立输入的 C29 张量

六个物理输入仍是 R465 的
$(t_1,t_2,t_3,t_4,c,d_0)$，其中前四个原 sigma 各按
$\delta,2\delta,\gamma,\bar\gamma$ 缩放。记
$$
A=t_1+t_2+t_3+t_4,\qquad
Y_s=A+c+2d_0,\qquad W=A+3\delta c+4d_0,
\tag{4}
$$
$$
R_1=4t_1-t_2,\quad
R_2=7(t_1+t_2)-15t_3,\quad
R_3=7(t_1+t_2+t_3)-22t_4.
\tag{5}
$$
使用 $d_0$ 区别原输入和 Mellin 指数 $d=p-1$。前四维矩阵是
$$
M_C=
\begin{pmatrix}
1&1&1&1\\
4&-1&0&0\\
7&7&-15&0\\
7&7&7&-22
\end{pmatrix},
\qquad\det M_C=-3190,
\tag{6}
$$
$$
M_C\operatorname{diag}(3,12,7,7)M_C^t
=\operatorname{diag}(29,60,2310,4466).
\tag{7}
$$
$M_C^{-1}$ 的首列是 $(3,12,7,7)^t/29$。

对偶生成变量 $(a,r_1,r_2,r_3)$ 上的完整来源为
$$
\begin{aligned}
\mathcal C(a,\mathbf r)={}&
\sigma\bigl(\delta(a+4r_1+7r_2+7r_3)\bigr)\\
&\cdot\sigma\bigl(2\delta(a-r_1+7r_2+7r_3)\bigr)\\
&\cdot\sigma\bigl(\gamma(a-15r_2+7r_3)\bigr)
\sigma\bigl(\bar\gamma(a-22r_3)\bigr).
\end{aligned}
\tag{8}
$$
它属于整个张量格
$$
\boxed{\mathcal C\in
\mathcal S_{29}\otimes\mathcal S_{60}\otimes
\mathcal S_{2310}\otimes\mathcal S_{4466}.}
\tag{9}
$$
这里 $\mathcal S_{29}=\sigma^{29}L(29O)$ 保原 odd 半特征。
沿 $A$ 有三个奇 CM 系数和一个偶系数；沿三个 $R$，奇系数数目
分别为 $0,2,2$。原 sigma 半特征对非零模二 CM 单位不变，
所以 (9) 的后三轴半特征平凡。式 (7) 消掉全部交叉 Gaussian。
这是全张量格身份，不是将 $\mathbf r$ 置零后的一变量断言。

整性与 R413、R454 相同：原正式群测度整有界，(6) 是普通整
自同构；各奇偶 theta 基的首阶互异、首系数为单位。在完整张量
基中按首阶消元即得整系数，不除可能含 $p$ 的大阶乘。

原完整六输入来源在这些坐标中准确为
$$
\boxed{\rho_0:\quad
-\frac1{84}\mathcal C(a,\mathbf r)\sigma(z_c)\sigma(z_d).}
\tag{10}
$$
系数 $-1/84$、全部 $R_i$ 以及两个独立输入 $c,d_0$ 都不改变。
尤其 $A$ 深并不表示四个 $t_i$ 各自深。

## 3. odd29 的实际标量与绝对平方

对整个 $\mathcal S_{29}$ 使用 R370、R454 的奇 degree division
trace；其规范逐字是
$$
K_{29}=\frac{\bar\pi_{17}}p\,\mathscr M_{\pi_{17}},\qquad
\nu_F|_{p\mathbf Z_p}=\lambda[\kappa]_*\nu_{K_{29}F}.
\tag{11}
$$
没有将未归一 trace 或半特征另换一种归一。

为明确奇中心，设 $\mathsf JF(z)=F(-z)$，对
$P\in E[29]$ 的任意 lift $A_P$ 写
$$
A_P^{29}=a_P,\quad
\mathsf JA_P\mathsf J=b_PA_P^{-1},\quad b_P^{29}=a_P^2.
$$
则唯一满足二十九次幂为一、且被 $\mathsf J$ 送至自身逆的规范为
$$
U_P=(b_P^{14}/a_P)A_P.
\tag{12}
$$
唯一性来自两个规范之比同时是二十九次根和平方根。实际 trace
将参数送至 $gP$ 并与 $\mathsf J$ 交换，故在这套规范中没有再添
中心符号。由 (3)，$K_{29}$ 与全部 $U_P$ 交换。
在标准 Heisenberg 基上，循环移位与互异二十九次根对角矩阵的
共同中心化子只有标量，因此
$$
K_{29}=\chi_{29,p}I.
\tag{13}
$$

绝对值不从投影交织猜定。取两个原 sigma 的联合
$$
F(z,t)=\sigma(2z-5t)\sigma(5z+2t).
\tag{14}
$$
两个输出的矩阵为
$$
\begin{pmatrix}2&5\\-5&2\end{pmatrix},
\qquad\det=29,\qquad BB^t=29I.
$$
每轴一个奇、一个偶系数，恰有原 odd29 半特征；
所以 $F\in\mathcal S_{29}\otimes\mathcal S_{29}$。
两个新输出同时深恰等价于两个原输入同时深。后者给系数
$(-\lambda)^2=\lambda^2$，前者按 (11)、(13) 给
$\lambda^2\chi_{29,p}^2$。又 $F(z,0)=10z^2+\cdots\ne0$，
故严格得到
$$
\boxed{\chi_{29,p}^2=1,\qquad \chi_{29,p}\in\{1,-1\}.}
\tag{15}
$$
$\chi_{29,p}$ 是实际 trace 已定的符号；本篇不按需要选它。

在后文简记 $\chi=\chi_{29,p}$。原状态的完整 $A$ 限制为
$$
\boxed{\rho_0|_{A\in p^n\mathbf Z_p}
=(\chi\lambda)^n(P_{A,n})_*\rho_0,}
\tag{16}
$$
其中在原物理输入上
$$
t_i\longmapsto t_i+\frac{\kappa^n-1}{29}N_iA
\quad(i=1,2,3,4),\qquad (N_1,N_2,N_3,N_4)=(3,12,7,7),
\tag{17}
$$
$c,d_0,R_1,R_2,R_3$ 逐个固定。故 $Y_s,W$ 同时加
$(\kappa^n-1)A$，而 $W-Y_s$ 固定。任意原隐藏事件都须按 (17)
运输。

原四 sigma 同时深给 $\lambda^4$。用 (6) 的完整整等价与
(13)、(15)，还得到三个 $R$ 同时深的真实核心
$$
\boxed{\nu_{\mathcal C}|_{\mathbf R\in p^n\mathbf Z_p^3}
=(\chi\lambda^3)^n[1,\kappa^n,\kappa^n,\kappa^n]_*
\nu_{\mathcal C}.}
\tag{18}
$$
这里是三个 $R$ 的共同深度，不把它拆成三个未经证明的独立标量。

## 4. odd 四挠平移：保留全部中心相位

用 R416 的 canonical lift
$$
(\mathsf T_t^{(N)}F)(z)
=e^{-N\eta_t(z+t/2)}F(z+t).
\tag{19}
$$
固定 $t=(m+n\omega)/4$，$m,n\in\{0,1,2,3\}$，并记
$$
\boxed{\epsilon(t)=(-i)^{m^2-mn+n^2}.}
\tag{20}
$$
$\epsilon$ 属于一个固定的至多四次系数扩张；$p\ne2$，所有
系数仍整。实际来源和最终三态身份下降到原系数域。

对于 $N=29$ 的 $\mathcal C$，及 $N=1$ 的原 sigma，必须先取
合法 $[4]$ 覆盖：
$$
(\mathsf T_t^{(N)}F)(4z)
=\mathsf T_{t/4}^{(16N)}\bigl(F(4z)\bigr).
\tag{21}
$$
分别位于完整 $\mathcal S_{464}$ 和 $\mathcal S_{16}$。
原 $4$ 是 $p$ 单位，所以覆盖不会丢失完整普通测度或限制域。

设 $\ell=m+n\omega$。由 (3)，
$$
(g+1)\ell\equiv4v\pmod{32\mathcal O_K},
\qquad v=(7+2\omega)\ell.
$$
以 $E(1,\omega)=1$ 记原整数交错配对，则
$$
E(\ell,v)=2N_{K/\mathbf Q}(\ell),\qquad
\chi_{\rm lat}(v)=(-1)^{N_{K/\mathbf Q}(\ell)}.
\tag{22}
$$
canonical 群律为
$\mathsf T_s\mathsf T_t=e^{\pi iNE(s,t)}\mathsf T_{s+t}$。
在 (21) 上比较
$g\ell/16=-\ell/16+v/4$，格平移 $v/4$ 的作用是原 odd
半特征 $\chi_{\rm lat}(v)$。完整相位准确为
$$
\chi_{\rm lat}(v)
 \exp\!\left(\frac{\pi iN}{4}E(\ell,v)\right)
=i^{(N+2)N(\ell)}
=(-i)^{N(\ell)},\qquad N=1,29.
\tag{23}
$$
模 $32$ 代表的差给偶格周期，其在 degree $16N$ 上的交叉相位
为一。故 (23) 不漏代表改变的中心项。

于是实际 normalized core 为
$$
\boxed{
K\bigl(\mathsf T_t^{(29)}\mathcal C\bigr)
=\chi\epsilon(t)\mathsf T_{-t}^{(29)}\mathcal C,\qquad
K\bigl(\mathsf T_t^{(1)}\sigma\bigr)
=-\epsilon(t)\mathsf T_{-t}^{(1)}\sigma.}
\tag{24}
$$
第二式保 sigma 核的负号。它们不是只在商掉中心后成立的公式。

完整的十六项相位表由 (20) 唯一给出，特别
$$
\epsilon(-t)=\epsilon(t),\quad \epsilon(t)^4=1,\quad
\epsilon(t)^2=
\begin{cases}1&t\in E[2],\\-1&t\in E[4]\setminus E[2],\end{cases}
\quad
\epsilon(3\delta t)=\epsilon(t)^{-1}.
\tag{25}
$$
最后一个等式使用 $N(3\delta)=27\equiv-1\pmod4$。
始终保留 $\mathsf T_{4t}^{(1)}\sigma$：它是格半特征乘 sigma，
不能当作一。相位表及 (22)–(25) 的整数核算在旁列脚本中逐项给出。

## 5. 第二状态的四个完整来源

令
$$
a_t=\begin{cases}
-\tfrac14&t\in E[2],\\
+\tfrac14&t\in E[4]\setminus E[2].
\end{cases}
$$
以下 $\tau_k$，$k\in\mathbf Z/4\mathbf Z$，是完整六变量来源：
$$
\boxed{
\tau_k:\quad-\frac1{84}\sum_{t\in E[4]}
a_t\epsilon(t)^k
\bigl(\mathsf T_{(-1)^kt}^{(29)}\mathcal C\bigr)(a,\mathbf r)
\bigl(\mathsf T_{3\delta t}^{(1)}\sigma\bigr)(z_c)
\bigl(\mathsf T_{4t}^{(1)}\sigma\bigr)(z_d).}
\tag{26}
$$
原 R465 第二状态准确是 $\tau_0=\rho_1$，不是另一个相同边际
的辅助来源。由 (24)，以及在 $c$ 轴作用后将 $t$ 换成 $-t$，
整个来源满足
$$
\boxed{
K_A\tau_k=\chi\tau_{k+1},\qquad
K_c\tau_k=-\tau_{k-1},\qquad
K_d\tau_k=-\tau_k.}
\tag{27}
$$
三个 core 在实际独立 $(A,c,d_0)$ 坐标上交换；指标相加也准确交换。
相应任意完整深度式为
$$
\boxed{
\nu_{\tau_k}|_{\{A\in p^n,\ c\in p^m,\ d_0\in p^\ell\}}
=(\chi\lambda)^n(-\lambda)^{m+\ell}
[\kappa^n,\kappa^m,\kappa^\ell,I_{\mathbf R}]_*
\nu_{\tau_{k+n-m}}.}
\tag{28}
$$
可在两边保留任意 $\mathbf R$ 测试。式 (18) 与第一轴平移交换，
故还可附加三个 $R$ 的共同深度，准确乘 $(\chi\lambda^3)^r$。

这并未把 $A$ 的限制改成四个 $t_i$ 的限制；若测试依赖原
$t_i$，仍须用 (17) 的逆变换写回。

## 6. 四态仍落在原 L 完整张量格

用 R465 的
$$
L=(2Y_s,2Q_s,2U_s,R_1,R_2,R_3),\quad
Q_s=A-29c,\quad U_s=A+c-15d_0.
$$
其原 theta degrees 是
$$
(136,3480,1020,60,2310,4466).
\tag{29}
$$
在 (26) 中记 $s=(-1)^k$。前三轴平坦参数中 $t$ 的系数分别为
$$
2(29s+3\delta+8),\quad
2(29s-87\delta),\quad
2(29s+3\delta-60).
\tag{30}
$$
写成 $\mathbf Z+\mathbf Z\omega$：
$$
\begin{array}{c|ccc}
s&2Y_s&2Q_s&2U_s\\ \hline
+1&(80,12)&(-116,-348)&(-56,12)\\
-1&(-36,12)&(-232,-348)&(-172,12).
\end{array}
$$
每一对均在 $4\mathbf Z^2$ 中；后三个 $R$ 参数为零。
因此四态全部是 (29) 的原 untwisted 完整整张量格元素。
证明保了每一个 flat twist，再用 $[4]$ 覆盖的整性下降，
不是只由总 degree 猜测单项归属。

R483 的同时 CM13、CM19 特征 $+1$ 也在四态中保持。
为支付这里的绝对交换：在整个 degree $464$ 上，$K_A$ 与任一
这两个 CM trace 的交织参数交换，故交换子至多标量；
非零子空间 $[4]^*\mathcal S_{29}$ 上 $K_A=\chi$，
而 CM trace 保此子空间且可逆，迫该交换标量为一。
其他五轴上的作用直接交换。所以 R483 的原五伴随
$\mathcal C_S,\mathcal C_{\rm new},\mathcal C_H$ 可以逐态使用，
不新增第一轴的虚构算术身份。

奇数 $k$ 时，原 $W$ 轴仍有 $14t$ 的平坦参数，一般只在
双覆盖后进入 degree $288$。本篇**不**把整个四态放入原
$\mathcal S_{72}$，也不声称 $K_{72}$ 已在四态上闭合。
下一节只取确实下降的三个偶状态。

## 7. 三个实际偶状态与完整 W 返回

定义
$$
e_0=\rho_0,\qquad e_1=\tau_0=\rho_1,\qquad e_2=\tau_2.
$$
由 (25)，$a_t\epsilon(t)^2=-1/4$ 对全部 $t\in E[4]$，故
$$
\boxed{e_2=-\frac14\sum_{t\in E[4]}
              \mathsf T_{t,W}^{(72)}e_0.}
\tag{31}
$$
所以三态都在原 $M$ 坐标的完整张量格中，第一 degree 为 $72$。

记
$$
H_2=\sum_{t\in E[2]}\mathsf T_{t,W}^{(72)},\qquad
G_4=\sum_{t\in E[4]}\mathsf T_{t,W}^{(72)}.
$$
R416 已付绝对
$$
K_W=(G_4-2H_2)/4,\qquad K_W^2=I.
\tag{32}
$$
$H_2/4$ 是完整二挠不变投影，其像准确为
$[2]^*\mathcal S_{18}$。在当前 ray，整个 $\mathcal S_{18}$
的核心为 $-I$：原 $g\equiv19\pmod{36}$ 使其成为标量，
非零实际锚 $\Theta(3z)$ 的 core 是 $-\lambda$
（R426 §5）。$[2]$ 是 $p$ 单位并与真实限制相容，故
$$
K_WH_2=H_2K_W=-H_2.
\tag{33}
$$
由 (31)、(32)，$H_2e_0=-2(e_1+e_2)$。代入 (33) 后得到
$$
\boxed{
K_We_0=e_1,\qquad K_We_1=e_0,\qquad
K_We_2=-e_0-e_1-e_2.}
\tag{34}
$$
另一方面，(15)、(27) 给真实两层 $A$ 算子
$$
\boxed{R:=K_A^2:\quad Re_0=e_0,\quad Re_1=e_2,\quad Re_2=e_1.}
\tag{35}
$$
按列写这两个矩阵：
$$
K=\begin{pmatrix}0&1&-1\\1&0&-1\\0&0&-1\end{pmatrix},
\qquad
R=\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\tag{36}
$$
准确有
$$
K^2=R^2=I,\qquad(KR)^4=I,\qquad(KR)^2\ne I.
\tag{37}
$$

## 8. 原三曲线行、参考行及三态的真实独立性

所有投影都取 R483 的完整第一轴投影，保其五伴随，不先忘掉
隐藏输入。由 (33)，$e_1+e_2=-H_2e_0/2$。

对每个 $t\in E[2]$，该 $W$ 平移在 $Y_s$ 上的平坦参数
$(37+3\delta)t$ 是格点，因为 $37+3\delta\in2\mathcal O_K$。
因此其第一轴仍下降到原 degree $34$；双覆盖后，整个 principal
部分在原 $N_7^9=-1$ 块（R476 §4）。新线和参考线都在
$N_7^9=+1$ 块，故它们杀掉 $e_1+e_2$。
在 $W$ 轴，R483 的 $\mathcal P_T$ 与 $H_2$ 交换，
而 R419 的完整身份为 $H_2T=0$。遂得完整张量表
$$
\begin{array}{c|ccc}
 &e_0&e_1&e_2\\ \hline
\mathcal P_{{\rm new},Y}
 &0&S_{\rm new}\otimes\Lambda_{\rm old}
       &-S_{\rm new}\otimes\Lambda_{\rm old}\\
\mathcal P_{H,Y}
 &0&H_{\rm ref}\otimes\Lambda_{\rm ref}
       &-H_{\rm ref}\otimes\Lambda_{\rm ref}\\
\mathcal P_{T,W}
 &T\otimes\Lambda_T&T\otimes\Lambda_T&-T\otimes\Lambda_T .
\end{array}
\tag{38}
$$
这里原规范未变：
$$
\Lambda_{\rm old}(1)=52/3,\quad
\Lambda_{\rm ref}(1)=-(1+\delta)/(2016b),\quad
\Lambda_T(1)=6\delta.
\tag{39}
$$
它们是完整五变量测度的质量；表中相同符号表示真正同一个伴随
测度，不是只比较三个质量。

三态确实线性独立。若 $a e_0+b e_1+c e_2=0$，新线行给
$b=c$，$T$ 行给 $a=0$，只剩 $bH_2e_0=0$。
而 $H_2e_0\ne0$ 可在原六个独立生成变量上直接见证：
选三个在 $W$ 中具有奇 CM 系数的 sigma 因子，例如系数
$\delta,\gamma,3\delta$ 的三个因子，分别令它们在三个不同的
非零二挠平移处为零。在零平移处这三个 sigma 都不为零；
其余三个变量取避开零除子的普通点。于是四项和只有零平移项
非零。这是完整全函数的除子论证，不是有限采样。
所以 (36) 生成的恰是八元群，且作用在三维真实来源空间上。

取更直接的完整改基
$$
u=e_0+\frac{e_1+e_2}{2},\qquad
v=\frac{e_1-e_2}{2},\qquad h=e_1+e_2.
\tag{40}
$$
则
$$
Ku=v,\quad Kv=u,\quad Kh=-h;\qquad
Ru=u,\quad Rv=-v,\quad Rh=h.
\tag{41}
$$
新线和参考线的 $Y$ 行只在 $v$ 上留下原
$S_{\rm new}\otimes\Lambda_{\rm old}$、
$H_{\rm ref}\otimes\Lambda_{\rm ref}$；
$T$ 行在 $u,v$ 上都是 $T\otimes\Lambda_T$，在 $h$ 上为零。

还可准确支付三个状态的整个第一边际，而非仅上述投影。
在 R465(27) 的 $h=-1$ 二挠纤维中，去掉因子
$4\delta\sigma^{34}/729$ 后的多项式记作 $P(x)$。直接全式投影给
$$
\sum_{j\equiv2\ (3)}[x^j]P(x)\,x^j
=-729x^2(X+1)(X-8)(7X^2-4X+16),\qquad X=x^3.
\tag{41a}
$$
另两非零二挠点是该完整式的两个实际 $\mu_3$ 旋转，
所以三项之和准确是 $-84\delta S$；零平移项是 $-84S$。
这些是完整多项式身份，旁列脚本给出零余式。按原
$b^{-1}F_1(b^{1/6}z)$ 同次性恢复一般 $b$，常数不变。
再用 $h=-H_2e_0/2$ 及原系数 $-1/84$，得到
$$
\boxed{
\begin{aligned}
Y_*h&=-\frac{1+\delta}{2}\nu_{S(2\,\cdot)},&
W_*h&=0,\\
Y_*u&=\frac{3-\delta}{4}\nu_{S(2\,\cdot)},&
W_*u&=6\delta\nu_T,\\
Y_*v&=\nu_{\Xi(2\,\cdot)+(1+\delta)S(2\,\cdot)/4},&
W_*v&=6\delta\nu_T .
\end{aligned}}
\tag{41b}
$$
这里 $Y=2Y_s$；若用未加倍的 $Y_s$，将所有生成函数中的
$2z$ 同时换成 $z$。R465(31) 说明 (41b) 的 $v$ 第一来源恰是
$\Xi(2z)$ 的整个 $N_7^9=+1$ 部分。其余正谱仍在，
不能把这一完整边际改称仅有新 rank-two 线。
式 (41b) 只对已忘掉其余伴随的边际给相应中央零；
保伴随的原算术条件行仍严格使用 (38) 和 R483。

由此 R483 的真实参考环带差现在位于实际 $v$ 来源上。例如忘掉
五伴随后，写 $\mathcal L_{H,n}$ 为其参考投影在
$Y\in p^n\mathbf Z_p^\times$、按 $Y/p^n$ 归一的中央导数，则
$$
(-\lambda)^{-n}\mathcal L_{H,n}-\mathcal L_{H,0}
=-\frac{1+\delta}{2016b}\,
 n\,d\log\langle\lambda^2\rangle(1+\lambda)\ne0
\quad(n>0).
\tag{42}
$$
这仍没有给 $H_{\rm ref}$ 的未知导数赋值。
$R v=-v$ 给的是完整偶 $A$ 深度返回；因为它改变 $Y$，
不能把 (42) 的投影与 $A$ 限制免费交换。

## 9. 两个原物理算子及四个共同伴随

令
$$
a=(1,1,1,1,0,0),\qquad
v_A=(3,12,7,7,0,0)^t.
$$
式 (17) 可写成
$$
P_{A,n}=I+\frac{\kappa^n-1}{29}v_Aa.
\tag{43}
$$
原 $W$ 算子为 R465 的
$$
P_W=I+\frac{\kappa-1}{72}v_Ww,\quad
v_W=(3,12,7,7,-3\delta,4)^t,\quad
w=(1,1,1,1,3\delta,4).
\tag{44}
$$
完整三态上，(34)、(35) 的物理含义严格是
$$
\boxed{
\mu|_{W\in p\mathbf Z_p}=\lambda(P_W)_*K\mu,\qquad
\mu|_{A\in p^2\mathbf Z_p}=\lambda^2(P_{A,2})_*R\mu.}
\tag{45}
$$
它们对每个 $\mu\in\operatorname{span}\{e_0,e_1,e_2\}$ 成立，
包括全部原六输入事件。

共同固定的四个独立输出可取
$$
\boxed{D=4c+3\delta d_0=(Q-3\delta U)/14,\qquad R_1,R_2,R_3.}
\tag{46}
$$
从原六输入到 $(A,W,D,\mathbf R)$ 的行列式绝对值是
$137170=3190\cdot43$，在当前处为单位。$D$ 的 degree 为 $43$，
与 $A,W$ 均正交；其余三轴仍如 (7)。
实际第一输出是
$$
\boxed{
Y_s=\frac{(35+3\delta)A+(8-3\delta)W+(4-6\delta)D}{43}.}
\tag{47}
$$
因此在 $(A,W)$ 平面上
$$
\boxed{
P_{A,2}=
\begin{pmatrix}\kappa^2&0\\\kappa^2-1&1\end{pmatrix},
\qquad
P_W=
\begin{pmatrix}1&29(\kappa-1)/72\\0&\kappa\end{pmatrix}.}
\tag{48}
$$
它们逐个固定 (46)，但一般都改变 (47)。
式 (43)、(44) 同时给出原 $c,d_0,t_i$ 的全部运输；
不能仅保 (48) 而删除原输入深度或单位条件。

## 10. D8 的词关系对应一个准确像格

这里需要区别来源矩阵和物理像格。一般地，若在同一稳定来源空间
有完整身份
$$
\mu|_{P_j\mathbf Z_p^6}=c_j(P_j)_*C_j\mu,
$$
则反复限制并作同一个线性逆像，严格得到
$$
\mu|_{P_1\cdots P_r\mathbf Z_p^6}
=(c_1\cdots c_r)(P_1\cdots P_r)_*
(C_r\cdots C_1)\mu.
\tag{49}
$$
证明是将第一式再限制到 $P_1P_2\mathbf Z_p^6$，其在 $P_1$
下的逆像正是 $P_2\mathbf Z_p^6$，然后归纳。每一步都适用
完整测度恒等式，所以可同时保任意其余测试。

对交替字 $A^2,W,A^2,W,A^2,W,A^2,W$，(37)、(45) 给
$$
\mathcal C_p=(P_{A,2}P_W)^4,\qquad
\boxed{\mu|_{\mathcal C_p\mathbf Z_p^6}
=\lambda^{12}(\mathcal C_p)_*\mu
\quad\text{对全部三个实际来源}.}
\tag{50}
$$
$\det\mathcal C_p=\kappa^{12}$。任意完整 $D,\mathbf R$ 测试在
(50) 中保持，其他原输入测试按 $\mathcal C_p$ 转置。

特别 $(KR)^4=I$ **不**使 $\mathcal C_p=I$。
(50) 的域是连续变换后的像格，不是
$\{A\in p^8,W\in p^4\}$，也不是把八个原坐标条件机械相交。
其补域仍是真实存在的完整测度部分。重复 (50) 可得到任意词幂
的准确身份；本篇没有将这些补域中央值置零。

## 11. 对当前缺口的准确作用

本篇新增的是：

- 保三个 $R$ 的整个 odd29 核、实际符号的绝对平方，以及原
  $A,c,d_0$ 全深度四态；
- 原 $L$ 全张量格内的合法算术投影和三个完整偶来源；
- 真正改变 $Y_s$ 的 $A^2,W$ 两轴关系、同一来源的八元群及其
  完整物理像格；
- 原新线、$T$、rank-zero 参考行在这三个来源上的准确符号和伴随。

若三个原 rank-two 中央导数同时为零，R483 和 (38) 给相应
投影的完整条件行零。但任一混合 $A,W$ 条件仍须按 (43)–(49)
逐支运输，不能由投影零推未投影子域零。式 (42) 的非零参考差
提供真实非齐次输入；把它与 (50) 的全部补域接合仍是后续问题。

## 12. 可重现证书与依赖

精确脚本和数据：

- [check-r488-original-shared-a-core-and-even-depth-group.py](../scripts/check-r488-original-shared-a-core-and-even-depth-group.py)
- [check-r488-original-shared-a-core-and-even-depth-group.json](../scripts/check-r488-original-shared-a-core-and-even-depth-group.json)

脚本以整数、$\mathbf Q(\delta)$ 和符号 $\kappa$ 精确验证 CRT、
完整十六相位、(6)–(7)、全部 flat 系数、三个来源矩阵的八元群、
(46)–(48)。全函数归属、绝对锚和测度限制的证明已在正文给出，
不依赖有限素数样本。

直接依赖：

- [R454：odd33 规范和两个原 sigma 的绝对锚方法](R454-original-odd33-core-and-exact-residual-slope-transport.md)。
- [R465：原六输入、W 核和完整新线](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R416：全中心四挠公式](R416-original-four-torsion-core-and-exact-second-state-marginals.md)。
- [R426：整个 degree18 的实际核心](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)。
- [R476：原八维来源及完整五伴随](R476-original-complete-xi-normtwo-bridge-and-integral-eight-source-basis.md)。
- [R483：原三曲线行与非零参考环带差](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)。

