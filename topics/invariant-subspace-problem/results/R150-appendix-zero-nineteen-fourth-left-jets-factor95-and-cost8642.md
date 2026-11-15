# R150：零点十九条四阶左延拓、公共因子K95与条件来源费8642

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿在原有限参数 $s=0$ 构造十九条常项独立、保全部6188原来源的四阶左零延拓。前三页与本次十九条延拓共同给累积连接秩界 $4,4,5,8$，从而全部原最大子式在零点共同消失至少49阶，低一阶子式至少44阶。这里不假定零点第一连接的秩恰等于4。

有限公共因子升为 $K_{95}=s^6K_{89}$。结合已经独立证明的无穷远指定阶 $78/77/72$ 及同一子式模31次数8527，得到 $8432\le q\le8597$，非基、转移、目标三个来源成本分别为8641、8642、225。统一条件来源费为8642，原目标成员性仍作为明确前提。

## 1. 原零点对象与固定的三阶规范

保持原十七式、原自然参数 $s$，以及次数至多三的全部来源：
$$
A(s)=A_0+sA_1+s^2A_2+s^3A_3+s^4A_4+\cdots:
\mathbb Q[[s]]^{6188}\longrightarrow\mathbb Q[[s]]^{4367}.
\tag{1.1}
$$
[原零点秩证明](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md)
给常数秩4340、函数域秩4354。因此常数左余空间维数27，有十四个正 Smith 指数。

使用原 $K$ 和 $y(s)=(1,s,\ldots,s^5)^{\mathsf T}$，不作无穷远反序。共动坐标为
$$
m_j=\sum_{k=0}^j\binom jk s^{j-k}n_k,\qquad
c=n_0,\quad d=n_1,\quad z_j=n_j\quad(2\le j\le10).
\tag{1.2}
$$
所有来源与目标单项式均完整运输。若 $A_{\rm new}=T A_{\rm old}V_{\rm src}$，原左 jet 为 $T^{\mathsf T}\lambda_{\rm new}$，包括全部低阶目标变换系数。

[零点二十三条二阶左延拓](R150-appendix-zero-twenty-three-second-left-jets-factor80-and-cost8672.md)
与[二十二条三阶左延拓](R150-appendix-zero-twenty-two-third-left-jets-factor89-and-cost8654.md)
已付
$$
r_1\le4,\qquad r_1+r_2\le4,\qquad r_1+r_2+r_3\le5.
\tag{1.3}
$$
这些是完整连接的累积界，不是零点各页秩的等式。

十个纯泛函
$$
c,c^2,\ldots,c^5,\qquad d,cd,\ldots,c^4d
\tag{1.4}
$$
沿全参数恒等为零。其余十个纯方向按
$$
d^2,d^3,cd^2,d^4,cd^3,c^2d^2,d^5,cd^4,c^2d^3,c^3d^2
\tag{1.5}
$$
排序。与前两个一次横向方向合成十二条已付三阶 jet
$$
f(s)=f_0+sf_1+s^2f_2+s^3f_3,\qquad A(s)^{\mathsf T}f(s)=O(s^4).
\tag{1.6}
$$
$f_0$ 最高一次横向，$f_1$ 只支持一次横向，$f_2,f_3$ 最高二次横向。本次逐哈希重建原 $1088\times605$ 三阶矩阵及其完整校正规范，未用无穷远规范替换零点规范。

## 2. 原四阶系数与来源分层

原切向身份为
$$
\Gamma(s;c,d,0)=0,\qquad
N(s;c,d,0)=4d^2g(s)y(s)y(s)^{\mathsf T},
$$
$$
g(s)=-2s^2(s-2)(s+6)=24s^2-8s^3-2s^4.
\tag{2.1}
$$
令
$$
p_0=5\zeta^4-\zeta^5,\qquad
p_1=-32\zeta^3+5\zeta^4-\zeta^5,\qquad
p_2=54\zeta^2-4\zeta^3+5\zeta^4.
$$
则
$$
4g_4p_0^2+8g_3p_0p_1+4g_2(p_1^2+2p_0p_2)
=150144\zeta^6-34688\zeta^7+10264\zeta^8-1200\zeta^9+24\zeta^{10}.
\tag{2.2}
$$
按原 $N_0,\ldots,N_{10},\Gamma_0,\ldots,\Gamma_5$ 顺序，
$$
F_4(c,d,0)=d^2(0,0,0,0,0,0,150144,-34688,10264,-1200,24,0,0,0,0,0,0)^{\mathsf T}.
\tag{2.3}
$$
小源码直接从原 $J_2,J_3,L_y$ 构造四阶物理映射，核对低阶身份并逐十七式验证 (2.3)。

记 $F_k=[s^k]F(s)$。原式在共动矩中至多二次，且
$$
F_0^{(0)}=F_1^{(0)}=0,\qquad F_2^{(0)}=d^2\sigma_2,
\tag{2.4}
$$
上标表示横向次数。第四残差为
$$
R_4=A_4^{\mathsf T}f_0+A_3^{\mathsf T}f_1+
A_2^{\mathsf T}f_2+A_1^{\mathsf T}f_3.
\tag{2.5}
$$

前1088行包含170个纯来源和918个一次横向来源。其 $A_2^{\mathsf T}f_2$ 除一次、二次横向作用外，完整保留
$$
\sigma_{2,i}(f_2)_{c^ad^{b+2}z_l}.
\tag{2.6}
$$
2295个二次横向来源的全部残差准确为
$$
(R_{\rm hi})_{i,a,b,j,k}
=\sigma_{2,i}(f_2)_{c^ad^{b+2}z_jz_k},\qquad a+b\le1.
\tag{2.7}
$$
剩余2805个三次横向来源因所有泛函最高二次横向而在 (2.5) 中为零。这里
$$
1088+2295+2805=6188
$$
保全部原来源，未把第四页的高行 forcing 删除。

## 3. 原零点完整高核与联合低校正

允许四阶目标校正最高三次横向。一、二次横向目标共585维，三次横向目标
$c^ad^bz_jz_kz_l$、$a+b\le2$ 共990维。

写原零点常系数
$$
F_{0,i}=\sum_l(\ell_{il}+c\,b_{il}+d\,a_{il})z_l
+\sum_{j\le k}q_{i,jk}z_jz_k.
$$
三次横向校正 $\eta$ 的2295个高来源作用为
$$
(H_3\eta)_{i,a,b,j,k}=
\sum_l\left(
\ell_{il}\eta_{a,b,\operatorname{sort}(j,k,l)}
+b_{il}\eta_{a+1,b,\operatorname{sort}(j,k,l)}
+a_{il}\eta_{a,b+1,\operatorname{sort}(j,k,l)}
\right),
\tag{3.1}
$$
在低行的一次横向来源上为
$$
(K_3\eta)_{i,a,b,l}
=\sum_{j\le k}q_{i,jk}\eta_{a,b,\operatorname{sort}(j,k,l)}.
\tag{3.2}
$$
三次横向来源乘 $F_0$ 后至少四次横向，故对本次校正严格为零。

本次实际计算的是原零点 $H_3$，没有从无穷远借用其秩。精确有理结果为
$$
\operatorname{rank}H_3=988,\qquad
\dim\ker H_3=2,\qquad
\operatorname{rank}[H_3,R_{\rm hi}]=988.
\tag{3.3}
$$
规范自由坐标为164、494；全部十二个 leading 坐标在高行均可升。保完整十四维核
$$
\begin{pmatrix}Y\\Z\end{pmatrix},\qquad
H_3Y+R_{\rm hi}Z=0,
\tag{3.4}
$$
其中 $Y$ 为 $990\times14$，$Z$ 为 $12\times14$，前两列 $Z=0$，其余十二列 $Z=I_{12}$。全部2295行实际乘回为零。

保原一次横向常左核 $Q$，令
$$
J_0=A_0^{\mathsf T}|_{\text{585个一、二次横向目标}},\qquad
J_1=A_1^{\mathsf T}Q=\begin{pmatrix}P_1Q\\0\end{pmatrix}.
$$
$QB$ 是第三系数的合法歧义；它被 $A_0^{\mathsf T}$ 杀掉，且 $A_1^{\mathsf T}QB$ 的高行因 $F_1^{(0)}=0$ 而为零。

实际低矩阵为
$$
M_4=[J_0,J_1,K_3Y+R_{\rm lo}Z]\in\mathbb Q^{1088\times606}.
\tag{3.5}
$$
依次取 $J_0$、加 $J_1$、加两条齐次高核、再加全部十二条升列，其秩为
$$
578,\quad582,\quad584,\quad587.
\tag{3.6}
$$
完整低核在原十二个 leading 坐标中的像准确为九维；算法直接核对该像，独立列为
$$
e_0,e_1,e_2,e_4,e_5,e_8,e_9,e_{10},e_{11}.
\tag{3.7}
$$

对相应核系数 $H,B,C$，有
$$
J_0H+J_1B+(K_3Y+R_{\rm lo}Z)C=0.
$$
因而原四阶左 jet 明确为
$$
\lambda(s)=f_0ZC+s f_1ZC+s^2 f_2ZC+
s^3(f_3ZC+QB)+s^4(H+YC),
\tag{3.8}
$$
其中最后两项嵌入各自一、二次及三次横向目标。高低完整身份及余2805行的次数消零给
$$
\boxed{A(s)^{\mathsf T}\lambda(s)=O(s^5)}
\tag{3.9}
$$
于全部6188个原来源。再作 (1.2) 的完整目标转置运输，仍是原自然 $s$ 的身份。

九个常项与十个恒等方向独立，所以零点有十九条真实四阶左延拓。小包络没有允许所有四、五次横向校正，故其正增秩不是完整第四连接的下界。

## 4. 零点公共阶49与有限因子K95

十九个独立四阶常项给
$$
r_1+r_2+r_3+r_4\le8.
\tag{4.1}
$$
结合 (1.3)，十四个正 Smith 指数之和满足
$$
\begin{aligned}
\delta_{4354,0}
&\ge70-r_1-(r_1+r_2)-(r_1+r_2+r_3)
-(r_1+r_2+r_3+r_4)\\
&\ge70-4-4-5-8=49.
\end{aligned}
$$
对最小十三个正指数，同式70换成65。因此
$$
\boxed{\delta_{4354,0}\ge49,\qquad \delta_{4353,0}\ge44.}
\tag{4.2}
$$
这个论证只用累积秩界；没有把无穷远 $r_1=4,r_2=0$ 搬到有限零点。

其余有限因子不变，得到
$$
\boxed{
K_{95}=s^6K_{89}=s^{35}K_{60}
=s^{49}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2.}
\tag{4.3}
$$
它整除原全部最大子式，次数为95，最高系数仍为 $5^6$。$F_\pm,E_8$ 是[原公共因子证明](R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)中的同一批多项式。式 (4.3) 不称完整 gcd。

## 5. 同一子式与完整原来源成本8642

[已付无穷远第四页](R150-appendix-infinity-nineteen-fourth-left-jets-order49-and-cost8648.md)
及完整精确 Koszul 曲线引理给同一指定 $D$、原来源换列、cofactor 的自然无穷远阶至少78、77、72。

[同一模31完整长度243](R150-appendix-complete-selected-mod31-infinity-length243-degree8527-and-target230.md)
给 $\deg_{\mathbb Q}D\ge8527$。保持总权 $H=8770$，令
$d_*=D/K_{95}$、$q=\deg d_*$，则
$$
\boxed{8432=8527-95\le q\le8770-78-95=8597.}
\tag{5.1}
$$
原来源权满足 $\max a_\ell=55$、$\delta_\ell=a_\ell-10$、$\max\delta_\ell=45$。保同源转移
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{95},\qquad
A_JP_\ell=d_*A_\ell,
$$
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-77-95.
\tag{5.2}
$$
明确假定原目标 $b_\nu=h_0t_\nu$ 属于 $\operatorname{im}_{\mathbb Q[s]}A$，且 $\tau_\nu\le64$。成员性使
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{95}
$$
为多项式，且
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-72-95.
\tag{5.3}
$$
沿原非基除法与完整来源转移，三个分支为
$$
\begin{aligned}
q-1+45&\le8641,\\
8770+55-77-95-11&=8642,\\
8770+64-72-95-10-8432&=225.
\end{aligned}
\tag{5.4}
$$
因此
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8642.}
\tag{5.5}
$$
目标分支仍为225：有限公共因子次数增加六，$q$ 下界同时减少六。没有把有限域 cofactor 阶222当成特征零72，没有声称目标成员性或特征零最高系数的31单位性已证。

## 6. 实际执行与复现接口

[小源码](../notes/2026-11-15-r150-zero-fourth-joint-high-low-left-envelope-789f.py)
SHA256：
~~~
cb04c3100f2e1030db00389eeb772a24aed95adde98b601a7d17a029141b222c
~~~
实际 run43702348535，step zero-fourth-joint-high-low-left-envelope，
执行源码提交c4f6cbdaf4dea9ec59f8b542658fce5d0984ad98。
共享数学30秒、实际内存512MiB；数学9.969569411000066秒、
墙钟10.03634378400011秒，退出码0。

| 完整对象 | SHA256 |
|---|---|
| 原 $P_4$ | ea9cb900008a8239dc155a4f21238f08b6db5761c978f48e55712b9e7d6f967c |
| 原零点 $H_3$ | 44bfa088c306186f920e996e8204ef6b6b7c706196bc11f88ca1594c90e9d326 |
| 高增广矩阵 | d147f8b908118900531cf273018899ff1d5c105cf56ed7cb49c7573eb4423f02 |
| 全部十四条高行升列 | ee11dcdee6e3c6b86c478543f9d80dbcaa99c2422e1cd6a5532439285d9038f8 |
| 完整 $1088\times606$ 低矩阵 | 52b7d99766b8ed5cddae819c13514d60f8415fbc037f1b4550e8d495c99418d8 |
| 九条完整低校正 | 1e5bbdf41f1cc1e79fb5e0244f5990f112ce01bd672011162414ca6d322a2f22 |
| 九条实际高校正 | 456ef71b334c381452999237d27b4417293d477bb92375d12ffa96f07f364d7e |
| 九条 leading 常项 | 96f113100d9f452735dae33951754df0e26880f502e6829d68bf0be94cc2be27 |

原完整小回执9017字节，SHA256：
~~~
1afaf2bb91daa171829d95ce6d49cbd7a1b075ca5df5d07ecadd4347d4a3beff
~~~
[已推执行记录](../notes/r150-infinity-remote-session-789f/43702348535-zero-fourth-joint-high-low-left-envelope.json)
保全部原二、三阶规范哈希、原零点高核、全3383行乘回与其余2805行自动消零证明。实际大矩阵只作作业内临时检查点，没有重算旧正常形或上传可重算大数据。
