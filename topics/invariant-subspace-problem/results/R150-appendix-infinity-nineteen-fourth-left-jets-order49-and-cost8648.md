# R150：十九条四阶左延拓、无穷远公共阶49与条件来源费8648

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿保持原自然无穷远参数、全部6188个来源和既有三阶校正规范，只加入原四阶系数及合法的三次横向四阶校正。实际精确有理计算得到九个新的四阶 leading 方向；加上十个沿全参数恒等的纯切向方向，共有十九条常项独立的四阶左零延拓。

由此，原完整最大、低一阶子式的无穷远公共消失阶分别至少49、44。同一29条完整精确 Koszul 曲线把指定子式、原来源换列、cofactor 的阶提高为78、77、72。结合已付有限因子 $K_{89}$ 以及同一子式模31次数8527，得到 $8438\le q\le8603$，三类来源成本分别为8647、8648、225；统一条件来源费为8648。

本稿没有把小包络的正增秩当成完整第四连接的下界，也不预设零点第四页的结果。

## 1. 原完整图、坐标与已付前三页

保持原十七式、次数至多三的全部来源和自然参数 $u=1/s$。在原反序及共动坐标中，写
$$
A(u)=A_0+uA_1+u^2A_2+u^3A_3+u^4A_4+\cdots:
\mathbb Q[[u]]^{6188}\longrightarrow\mathbb Q[[u]]^{4367}.
\tag{1.1}
$$
常数秩为4340，函数域秩为4354，所以常数左余空间维数27，恰有十四个正 Smith 指数。

反序后实际矩阵为 $K^\sharp$，均值为 $v(u)=(1,u,\ldots,u^5)^{\mathsf T}$。共动坐标为
$$
m_j=\sum_{k=0}^j\binom jk u^{j-k}n_k,\qquad
c=n_0,\quad d=n_1,\quad z_j=n_j\quad(2\le j\le10).
\tag{1.2}
$$
来源及目标均取该替换在各自全部原单项式上的完整诱导。若
$A_{\rm new}=T A_{\rm old}V_{\rm src}$，则原左 jet 为
$T^{\mathsf T}\lambda_{\rm new}$，不是省去高阶运输后的裸数组。

[完整第一页](R150-appendix-four-dimensional-transverse-first-connection-exact-infinity-image-and-factor70.md)、
[完整第二页](R150-appendix-infinity-full-second-connection-zero-common-order34-and-cost8675.md)及
[第三页](R150-appendix-infinity-third-connection-one-dimensional-bound-order43-and-cost8663.md)
已经给
$$
r_1=4,\qquad r_2=0,\qquad r_3\le1,
\tag{1.3}
$$
其中 $r_j$ 是原完整正 Smith 指数恰等于 $j$ 的个数。

十个纯目标泛函
$$
c,c^2,\ldots,c^5,\qquad d,cd,\ldots,c^4d
\tag{1.4}
$$
沿全参数直接杀掉全部来源。其余十个纯方向按
$$
d^2,d^3,cd^2,d^4,cd^3,c^2d^2,d^5,cd^4,c^2d^3,c^3d^2
\tag{1.5}
$$
排序。第三页已经在这十个方向及前两个横向方向上给十二条真实左延拓
$$
f(u)=f_0+uf_1+u^2f_2+u^3f_3,\qquad
A(u)^{\mathsf T}f(u)=O(u^4).
\tag{1.6}
$$
$f_0$ 最高一次横向，$f_1$ 只支持一次横向，$f_2,f_3$ 最高二次横向。本次使用原 $1088\times605$ 第三页矩阵的同一 RREF 规范，逐哈希恢复全部 $f_j$，不换用后来的扩大三次横向试验所得规范。

记 $Q\in\mathbb Q^{135\times7}$ 为同一个完整一次横向常左核，$P_0Q=0$。它作为全部4367目标上的泛函也满足 $A_0^{\mathsf T}Q=0$。

## 2. 原四阶系数及全部来源的残差分解

记 $F_k=[u^k]F(u)$ 为原十七式的系数，按横向次数写
$$
F_k=F_k^{(0)}+F_k^{(1)}+F_k^{(2)}.
$$
原十七式在共动矩中至多二次，且
$$
F_0^{(0)}=F_1^{(0)}=0,\qquad
F_2^{(0)}=d^2\sigma_2.
\tag{2.1}
$$

原切向身份保持为
$$
\Gamma(u;c,d,0)=0,\qquad
N(u;c,d,0)=4d^2g_\infty(u)v(u)v(u)^{\mathsf T},\qquad
g_\infty(u)=-2u^2-8u^3+24u^4.
\tag{2.2}
$$
令
$$
p_0=-\zeta^4-\zeta^5,\qquad
p_1=5\zeta^3+5\zeta^4+5\zeta^5,\qquad
p_2=-8\zeta^2-4\zeta^3-32\zeta^4.
$$
则原四阶极化系数是
$$
4g_4p_0^2+8g_3p_0p_1+4g_2(p_1^2+2p_0p_2)
=-328\zeta^6-272\zeta^7-440\zeta^8-80\zeta^9+216\zeta^{10}.
\tag{2.3}
$$
所以按原 $N_0,\ldots,N_{10},\Gamma_0,\ldots,\Gamma_5$ 顺序，
$$
F_4(c,d,0)=d^2(0,0,0,0,0,0,-328,-272,-440,-80,216,0,0,0,0,0,0)^{\mathsf T}.
\tag{2.4}
$$
源码从原物理 $J_2,J_3,L_y$ 映射直接构造四阶项，核对已付低阶哈希，并逐十七式验证 (2.4)。全部系数都是普通幂级数系数。

固定 (1.6) 后的第四残差为
$$
R_4=A_4^{\mathsf T}f_0+A_3^{\mathsf T}f_1+
A_2^{\mathsf T}f_2+A_1^{\mathsf T}f_3.
\tag{2.5}
$$
按来源乘子的横向次数，它完整分成以下四组：
$$
170+918+2295+2805=6188.
\tag{2.6}
$$
前两组是纯来源 $c^ad^bF_i$、$a+b\le3$，以及一次横向来源
$c^ad^bz_lF_i$、$a+b\le2$，合计1088行，记其残差为 $R_{\rm lo}$。

在这1088行中，$A_2^{\mathsf T}f_2$ 保留全部一次、二次横向作用，还保留纯二阶项产生的
$$
\sigma_{2,i}\,(f_2)_{c^ad^{b+2}z_l}.
\tag{2.7}
$$
不能沿用 $A_0,A_1$ 的纯项为零来删掉 (2.7)。

第二组高行是二次横向来源
$c^ad^bz_jz_kF_i$，$a+b\le1$、$2\le j\le k\le10$，合计2295行。其完整残差恰为
$$
(R_{\rm hi})_{i,a,b,j,k}
=\sigma_{2,i}\,(f_2)_{c^ad^{b+2}z_jz_k}.
\tag{2.8}
$$
其余三项因泛函的横向次数不足而为零。最后2805个三次横向来源在 (2.5) 中全为零：前两项的泛函最高一次横向，后二项最高二次横向；即使 $F_2$ 有纯项，也不能把三次横向降至二次。

因此 (2.7)、(2.8) 精确保留了第四页首次出现的高来源 forcing。

## 3. 三次横向校正的完整高、低作用

允许新增的四阶目标校正最高三次横向。一次、二次横向目标共585维；三次横向目标为
$$
c^ad^bz_jz_kz_l,\qquad a+b\le2,\quad 2\le j\le k\le l\le10,
\tag{3.1}
$$
共990维。

写原常系数为
$$
F_{0,i}=\sum_l(\ell_{il}+c\,b_{il}+d\,a_{il})z_l
+\sum_{j\le k}q_{i,jk}z_jz_k.
\tag{3.2}
$$
三次横向泛函 $\eta$ 在2295个高来源上的全部作用是
$$
(H_3\eta)_{i,a,b,j,k}
=\sum_l\left(
\ell_{il}\eta_{a,b,\operatorname{sort}(j,k,l)}
+b_{il}\eta_{a+1,b,\operatorname{sort}(j,k,l)}
+a_{il}\eta_{a,b+1,\operatorname{sort}(j,k,l)}
\right).
\tag{3.3}
$$
在低来源上，仅一次横向来源可能读到二次项：
$$
(K_3\eta)_{i,a,b,l}
=\sum_{j\le k}q_{i,jk}
\eta_{a,b,\operatorname{sort}(j,k,l)}.
\tag{3.4}
$$
三次横向来源乘 $F_0$ 后至少四次横向，故对本次最高三次的校正严格为零。没有以低来源压缩代替高来源条件。

[完整三次横向源码与回执](../notes/r150-infinity-remote-session-789f/43702348535-infinity-third-complete-cubic-normal-kernel.json)
已经给
$$
\operatorname{rank}H_3=988,\qquad \dim\ker H_3=2.
\tag{3.5}
$$
本次保留完整 $H_3,K_3$ 的同一字节规范和哈希，但不能只把 $\eta$ 限在 $\ker H_3$：第四页还须解 (2.8) 的非齐次条件。

## 4. 联合高、低 Schur 与九条真实第四延拓

先对完整高行构造
$$
[H_3,R_{\rm hi}]\in\mathbb Q^{2295\times1002}.
$$
实际精确有理计算给
$$
\operatorname{rank}[H_3,R_{\rm hi}]=988.
\tag{4.1}
$$
所以原十二个 leading 坐标在高行全部可升。算法保留完整十四维核
$$
\begin{pmatrix}Y\\ Z\end{pmatrix},
\qquad H_3Y+R_{\rm hi}Z=0,\qquad
Y\in\mathbb Q^{990\times14},\quad Z\in\mathbb Q^{12\times14}.
\tag{4.2}
$$
前两列是同一规范的 $\ker H_3$，其 $Z$ 块为零；其余十二列的 $Z$ 块为 $I_{12}$。实际全部2295行乘回为零。

令
$$
J_0=A_0^{\mathsf T}|_{\text{585个一、二次横向目标}},\qquad
J_1=A_1^{\mathsf T}Q=\begin{pmatrix}P_1Q\\0_{918\times7}\end{pmatrix}.
\tag{4.3}
$$
$QB$ 是第三系数的合法常左核歧义。它不改变先前第三阶方程；由于 $F_1^{(0)}=0$，其第四作用只在纯来源，2295个高来源的作用也严格为零。

高行消去后的完整低矩阵为
$$
M_4=[J_0,J_1,K_3Y+R_{\rm lo}Z]\in\mathbb Q^{1088\times606}.
\tag{4.4}
$$
实际前缀及全矩阵秩为
$$
578,\quad582,\quad584,\quad587,
\tag{4.5}
$$
依次对应 $J_0$、$[J_0,J_1]$、再加两条齐次三次横向核、再加十二条非齐次升列。算法构造完整核后，直接取其在原十二个 leading 坐标中的像，而不是用整个核维数代替 leading 维数。

该像的秩准确为9。按 (1.5) 的十个纯方向及两个横向方向组成的原十二维基，实际独立 leading 列准确为
$$
e_0,e_1,e_2,e_4,e_5,e_8,e_9,e_{10},e_{11}.
\tag{4.6}
$$
记相应核系数为 $H,B,C$，则
$$
J_0H+J_1B+(K_3Y+R_{\rm lo}Z)C=0.
\tag{4.7}
$$
四阶左 jet 明确为
$$
\lambda(u)=
f_0ZC+u f_1ZC+u^2 f_2ZC
+u^3(f_3ZC+QB)
+u^4\left(H+YC\right).
\tag{4.8}
$$
这里 $H$ 与 $YC$ 分别嵌入一、二次及三次横向目标。式 (4.2)、(4.7) 和全部低阶身份共同给
$$
\boxed{A(u)^{\mathsf T}\lambda(u)=O(u^5)}
\tag{4.9}
$$
于全部6188来源：3383行实际完整乘回，余2805行由上述横向次数严格为零。目标与来源再按 (1.2) 完整运输，(4.9) 是原自然 $u$ 的身份。

这九条延拓加上 (1.4) 的十条恒等方向，给十九个独立常项。这里允许了完整三次横向四阶校正，但没有排除四、五次横向或更一般低阶规范变动可能进一步升起别的方向。因此 (4.5) 不是完整第四连接的秩下界。

## 5. 完整 Smith 公共阶与指定子式

十九条独立四阶左 jet 给
$$
r_1+r_2+r_3+r_4\le27-19=8.
\tag{5.1}
$$
结合 (1.3)，累积界为
$$
r_1\le4,\quad r_1+r_2\le4,\quad
r_1+r_2+r_3\le5,\quad r_1+r_2+r_3+r_4\le8.
\tag{5.2}
$$
十四个正指数的总和因此至少
$$
\begin{aligned}
\delta_{4354,\infty}
&\ge70-r_1-(r_1+r_2)-(r_1+r_2+r_3)
-(r_1+r_2+r_3+r_4)\\
&\ge70-4-4-5-8=49.
\end{aligned}
\tag{5.3}
$$
对最小十三个正指数，同式70换为65，给
$$
\boxed{\delta_{4354,\infty}\ge49,\qquad
\delta_{4353,\infty}\ge44.}
\tag{5.4}
$$
这没有单独宣称 $r_4\le3$：只有 $r_3+r_4\le4$ 已付，$r_3=1$ 的下界仍未由小包络证明。

应用[完整 Smith 与29条精确 Koszul 曲线](R150-appendix-full-smith-formal-koszul-selected-orders60-59-56-and-cost8685.md)：
$$
\boxed{
v_\infty D\ge49+29=78,\quad
v_\infty D_{\rm original\ replacement}\ge49+28=77,\quad
v_\infty(\text{cofactor})\ge44+28=72.}
\tag{5.5}
$$
任意解析目标的换列只使用 cofactor 的72阶，不能沿用原来源换列的77阶。

## 6. K89、同一模31次数及条件来源费8648

[已付有限零点三阶结论](R150-appendix-zero-twenty-two-third-left-jets-factor89-and-cost8654.md)
给公共因子 $K_{89}$，次数89、最高系数 $5^6$。本稿不改该有限因子。

[同一指定子式完整模31长度243](R150-appendix-complete-selected-mod31-infinity-length243-degree8527-and-target230.md)
已实际证明
$$
\deg\overline D=8527,\qquad \deg_{\mathbb Q}D\ge8527.
\tag{6.1}
$$
(5.5) 及原总权 $H=8770$ 给
$$
8527\le\deg_{\mathbb Q}D\le8770-78=8692.
$$
令 $d_*=D/K_{89}$、$q=\deg d_*$，则
$$
\boxed{8438\le q\le8603.}
\tag{6.2}
$$

保持原来源权 $\max a_\ell=55$、$\delta_\ell=a_\ell-10$、$\max\delta_\ell=45$。同一原来源转移满足
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{89},\qquad
A_JP_\ell=d_*A_\ell,
$$
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-77-89.
\tag{6.3}
$$
明确假定原目标 $b_\nu=h_0t_\nu$ 属于
$\operatorname{im}_{\mathbb Q[s]}A$，原目标权 $\tau_\nu\le64$。成员性保证
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{89}
$$
为多项式，并给
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-72-89.
\tag{6.4}
$$
沿原非基除法及完整来源转移，三类成本分别为
$$
\begin{aligned}
q-1+45&\le8647,\\
8770+55-77-89-11&=8648,\\
8770+64-72-89-10-8438&=225.
\end{aligned}
\tag{6.5}
$$
因此
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8648.}
\tag{6.6}
$$
目标分支225用特征零 cofactor72与实际模31次数下界，不把有限域 cofactor222当成特征零下界。原成员性、特征零精确最高次数及31首项单位性仍分别保留。

## 7. 实际执行与小证据

[小源码](../notes/2026-11-15-r150-infinity-fourth-joint-high-low-left-envelope-789f.py)
SHA256：
~~~
3f9b473fe0a015f11586637348ab234fd800fe0910246f43c01f5a4d5127af1d
~~~
实际 run43702348535，step infinity-fourth-joint-high-low-left-envelope，
执行源码提交0e9ddb0e6f1e6deeaad5ed8107e1d0433bc0d646。
共享数学限额30秒、实际内存限额512MiB；数学用时8.679830253000091秒，
墙钟8.736608305000118秒，退出码0。

| 完整对象 | SHA256 |
|---|---|
| 原四阶 $P_4$ | 9bfbbdf84ad15316a17c4866d5deb1e2ebca39194087f68c13e5fa14af055040 |
| $2295\times1002$ 高增广矩阵 | 446fd8035ccb2d678d6dcab9c77d4aba6a22a666c442cfe7aaaae8a131a42ad6 |
| 全部十四条高行升列 | 63999a05f0906c822bb32a2feb7216f33a6a39451335ee1db17ca83fa25d4f3c |
| $1088\times606$ 低增广矩阵 | 98945be0f33611931219574b478b6f51d90ce6c30a97671f23730234e741e044 |
| 九条完整低校正 | 4ae223668e8bcd92c9c16cfd097763ee92a451c892560e6c54c8f30e930f61ec |
| 九条实际高校正 | 456ef71b334c381452999237d27b4417293d477bb92375d12ffa96f07f364d7e |
| 九条 leading 常项 | 96f113100d9f452735dae33951754df0e26880f502e6829d68bf0be94cc2be27 |

原完整小回执8696字节，SHA256：
~~~
ac682f960fbcb89aee91e29495b5b7ee460b8d5670092dae14d7ee431f4c945d
~~~
[已推运行记录](../notes/r150-infinity-remote-session-789f/43702348535-infinity-fourth-joint-high-low-left-envelope.json)
保存所有输入身份、原三阶规范哈希、完整高低行乘回和九个 leading 常项。
两个真实矩阵阶段只在同一作业临时检查点保存；可重算大矩阵未进入Git或Release，没有重算旧正常形或大模页。
