# R150：零点十七条五阶左延拓、公共因子K99与条件来源费8634

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿保持原有限参数 $s=0$、完整6188来源及已经实际验证的九条四阶左 jet。原第五阶完整高行允许九个方向均继续提升；保全部高核自由量作低行消元后得到七条常项独立的五阶左延拓。加上十个恒等纯切向方向，完整零点图有十七条独立五阶左延拓，故最大、低一阶子式的公共零点阶分别至少53、47。

因此有限公共因子升为 $K_{99}=s^4K_{95}=s^{39}K_{60}$。结合独立已付的无穷远指定阶 $82/81/75$ 与同一子式模31次数8527，得到 $8428\le q\le8589$，非基、转移、目标分支成本分别为8633、8634、222。统一条件来源费为8634；原目标成员性仍作为明确前提。

## 1. 原参数、全来源及固定四阶规范

保持原十七式、原自然参数 $s$ 与所有次数至多三的来源：
$$
A(s)=\sum_{k\ge0}s^kA_k:
\mathbb Q[[s]]^{6188}\longrightarrow\mathbb Q[[s]]^{4367}.
\tag{1.1}
$$
[原零点秩证明](R150-appendix-rank-one-physical-mean-at-zero-full-critical-emptiness.md)
给常数秩4340、函数域秩4354，故常数左余空间维数27，有十四个正 Smith 指数。

使用原 $K$ 与 $y(s)=(1,s,\ldots,s^5)^{\mathsf T}$，共动矩为
$$
m_j=\sum_{k=0}^j\binom jk s^{j-k}n_k,\qquad
c=n_0,\quad d=n_1,\quad z_j=n_j\quad(2\le j\le10).
\tag{1.2}
$$
来源与目标单项式全部运输。若 $A_{\rm new}=T A_{\rm old}V_{\rm src}$，原目标坐标下的左 jet 是 $T^{\mathsf T}\lambda_{\rm new}$；不能省略该转置及低阶系数。

[零点第四页](R150-appendix-zero-nineteen-fourth-left-jets-factor95-and-cost8642.md)
已给九条真实四阶延拓
$$
g(s)=g_0+sg_1+s^2g_2+s^3g_3+s^4g_4,\qquad
A(s)^{\mathsf T}g(s)=O(s^5).
\tag{1.3}
$$
本次逐哈希重建同一低、高校正与 leading 矩阵，没有用无穷远规范替代零点规范。
$g_0$ 最高一次横向，$g_1$ 只支持一次横向，$g_2,g_3$ 最高二次横向，
$g_4=g_4^{\rm lo}+g_4^{(3)}$，其中两部分分别支持585维一、二次横向及990维三次横向目标。

已有完整连接累积界为
$$
r_1\le4,\qquad r_1+r_2\le4,\qquad
r_1+r_2+r_3\le5,\qquad r_1+r_2+r_3+r_4\le8.
\tag{1.4}
$$
另十个纯泛函
$$
c,c^2,\ldots,c^5,\qquad d,cd,\ldots,c^4d
\tag{1.5}
$$
沿全参数恒等杀掉全部原来源。这里不假定零点 $r_1=4$ 或 $r_2=0$。

## 2. 原第五系数与完整残差

原切向身份为
$$
\Gamma(s;c,d,0)=0,\qquad N(s;c,d,0)=4d^2g_{\rm z}(s)y(s)y(s)^{\mathsf T},
$$
$$
g_{\rm z}(s)=-2s^2(s-2)(s+6)=24s^2-8s^3-2s^4.
\tag{2.1}
$$
令
$$
\begin{aligned}
p_0&=5\zeta^4-\zeta^5,\\
p_1&=-32\zeta^3+5\zeta^4-\zeta^5,\\
p_2&=54\zeta^2-4\zeta^3+5\zeta^4,\\
p_3&=-32\zeta-4\zeta^2-8\zeta^3.
\end{aligned}
$$
以 $g_j=[s^j]g_{\rm z}$，原第五极化卷积为
$$
8g_2(p_0p_3+p_1p_2)+4g_3(2p_0p_2+p_1^2)+8g_4p_0p_1
$$
$$
=-362496\zeta^5+28672\zeta^6-34304\zeta^7+
1488\zeta^8-160\zeta^9-48\zeta^{10}.
\tag{2.2}
$$
因此按原 $N_0,\ldots,N_{10},\Gamma_0,\ldots,\Gamma_5$ 顺序，
$$
F_5(c,d,0)=d^2
(0,0,0,0,0,-362496,28672,-34304,1488,-160,-48,0,0,0,0,0,0)^{\mathsf T}.
\tag{2.3}
$$
源码分别由 (2.1) 的有限卷积和原 $J_2,J_3,L_y$ 物理映射核对全部十七式；原零点0至4阶哈希均保持。

完整第五残差为
$$
R_5=A_5^{\mathsf T}g_0+A_4^{\mathsf T}g_1+
A_3^{\mathsf T}g_2+A_2^{\mathsf T}g_3+A_1^{\mathsf T}g_4.
\tag{2.4}
$$
记 $F_k^{(0)}=d^2\sigma_k$，其中 $F_0^{(0)}=F_1^{(0)}=0$。前1088个纯、一次横向来源上的完整残差记为 $R_{\rm lo}$，包含三阶、二阶物理二次横向作用、相应纯项，以及 $F_1$ 对 $g_4^{(3)}$ 的二次横向作用。不能因 $F_1^{(0)}=0$ 删除这一项。

对2295个二次横向来源 $c^ad^bz_jz_kF_i$、$a+b\le1$，准确有
$$
(R_{\rm hi})_{i,a,b,j,k}
=\sigma_{3,i}(g_2)_{c^ad^{b+2}z_jz_k}
+\sigma_{2,i}(g_3)_{c^ad^{b+2}z_jz_k}
+(H_3^{(1)}g_4^{(3)})_{i,a,b,j,k}.
\tag{2.5}
$$
$H_3^{(1)}$ 保 $F_1$ 的全部常数、$c$、$d$ 线性横向系数。

其余2805个三次横向来源在 (2.4) 中严格为零：前四项的泛函最高二次横向；最后一项中 $F_1$ 至少一次横向而 $g_4$ 最高三次横向。因此 $1088+2295+2805=6188$ 覆盖全部来源。

## 3. 完整高核、低校正与七条真实五阶 jet

沿[第四页](R150-appendix-zero-nineteen-fourth-left-jets-factor95-and-cost8642.md)保持原零点常系数
$$
F_{0,i}=\sum_l(\ell_{il}+c\,b_{il}+d\,a_{il})z_l+
\sum_{j\le k}q_{i,jk}z_jz_k.
\tag{3.1}
$$
三次横向校正 $\eta\in\mathbb Q^{990}$ 的2295个高行作用为
$$
(H_3\eta)_{i,a,b,j,k}
=\sum_l\left(
\ell_{il}\eta_{a,b,\operatorname{sort}(j,k,l)}
+b_{il}\eta_{a+1,b,\operatorname{sort}(j,k,l)}
+a_{il}\eta_{a,b+1,\operatorname{sort}(j,k,l)}
\right).
\tag{3.2}
$$
其低行作用 $K_3$ 只在一次横向来源上非零，准确为
$$
(K_3\eta)_{i,a,b,l}=\sum_{j\le k}q_{i,jk}
\eta_{a,b,\operatorname{sort}(j,k,l)}.
\tag{3.3}
$$
真实零点有理计算给
$$
\operatorname{rank}H_3=988,\qquad
\operatorname{rank}[H_3,R_{\rm hi}]=988.
\tag{3.4}
$$
原九个 leading 坐标在高行全部可升。保完整十一维核
$$
H_3Y+R_{\rm hi}Z=0,\qquad
Y\in\mathbb Q^{990\times11},\quad Z\in\mathbb Q^{9\times11}.
\tag{3.5}
$$
前两列是完整 $\ker H_3$，leading 为零；后九列 leading 为 $I_9$。全部2295行实际乘回。

记 $Q$ 为原135维一次横向目标上的七维常左核，令
$$
J_0=A_0^{\mathsf T}|_{\text{585个一、二次横向目标}},\qquad
J_1=A_1^{\mathsf T}Q=\begin{pmatrix}P_1Q\\0\end{pmatrix}.
$$
第四系数的合法歧义 $QB$ 保持旧四阶身份，其第五残差为 $J_1B$，高行仍为零。完整低矩阵为
$$
M_5=[J_0,J_1,K_3Y+R_{\rm lo}Z]\in\mathbb Q^{1088\times603}.
\tag{3.6}
$$
实际前缀秩依次为578、582、584，全矩阵秩586。完整核在原九维 leading 坐标中的像准确七维。

令 $e_0,\ldots,e_8$ 为同一九条零点四阶 jet 的有序基。实际独立 leading 列为
$$
e_0,\ e_1,\ e_2,\ 
e_5-\frac{906}{59}e_3+\kappa_0e_4,\ 
e_6-\frac{906}{59}e_4,\ e_7,\ e_8,
\tag{3.7}
$$
$$
\kappa_0=
\frac{243939753190408876732819759491191}
{2154926556727036759867804718400}.
$$
此规范与无穷远第五页的系数不同；完整零点回执直接核对全部来源，不靠相同秩作运输。

对相应完整核系数 $H,B,C$，
$$
J_0H+J_1B+(K_3Y+R_{\rm lo}Z)C=0.
$$
因此原五阶左 jet 为
$$
\lambda(s)=\sum_{j=0}^3s^jg_jZC+
s^4(g_4ZC+QB)+s^5(H+YC),
\tag{3.8}
$$
其中 $H,YC$ 分别嵌入一、二次横向及三次横向目标。(3.5)、(3.6) 的完整乘回和先前身份给
$$
\boxed{A(s)^{\mathsf T}\lambda(s)=O(s^6)}
\tag{3.9}
$$
于全部6188原来源，再按 (1.2) 的目标转置回到原坐标。十个恒等方向与这七个常项独立，故得到十七条独立五阶左延拓。

这是合法延拓构造；受限校正包络的两维残差不构成完整第五连接的秩下界。

## 4. 公共零点阶53、47及K99

十七个独立五阶常项给
$$
r_1+r_2+r_3+r_4+r_5\le27-17=10.
\tag{4.1}
$$
十四个正 Smith 指数之和因而满足
$$
\begin{aligned}
\delta_{4354,0}
&\ge84-r_1-(r_1+r_2)-(r_1+r_2+r_3)
-(r_1+r_2+r_3+r_4)
-(r_1+r_2+r_3+r_4+r_5)\\
&\ge84-4-4-5-8-10=53.
\end{aligned}
$$
对最小十三个正指数，将84换为78。故
$$
\boxed{\delta_{4354,0}\ge53,\qquad \delta_{4353,0}\ge47.}
\tag{4.2}
$$
只使用零点累积界，没有假定 $r_1=4$ 或 $r_2=0$。

其余有限公共因子保持，得到
$$
\boxed{
K_{99}=s^4K_{95}=s^{39}K_{60}
=s^{53}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2.}
\tag{4.3}
$$
次数为99，最高系数仍为 $5^6$，并整除原全部最大子式。$F_\pm,E_8$ 仍是[原有限因子证明](R150-appendix-projective-minor-divisor-degree-and-finite-cover-certificate.md)中的同一多项式；不称 (4.3) 为完整 gcd。

## 5. 同一指定子式的来源成本8634

[无穷远第五页](R150-appendix-infinity-seventeen-fifth-left-jets-order53-and-cost8638.md)
与完整29条精确 Koszul 曲线给同一指定 $D$、原来源换列、cofactor 的无穷远阶至少82、81、75。
[同一模31完整长度243](R150-appendix-complete-selected-mod31-infinity-length243-degree8527-and-target230.md)
给 $\deg_{\mathbb Q}D\ge8527$。原总权 $H=8770$，令 $d_*=D/K_{99}$、$q=\deg d_*$，则
$$
\boxed{8428=8527-99\le q\le8770-82-99=8589.}
\tag{5.1}
$$
保持 $\max a_\ell=55$、$\delta_\ell=a_\ell-10$、$\max\delta_\ell=45$，完整原来源转移满足
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{99},\qquad
A_JP_\ell=d_*A_\ell,
$$
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-81-99.
\tag{5.2}
$$
明确假定原目标 $b_\nu=h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A$，且 $\tau_\nu\le64$。成员性使
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{99}
$$
为多项式，并有
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-75-99.
\tag{5.3}
$$
原非基除法与完整来源转移给
$$
\begin{aligned}
q-1+45&\le8633,\\
8770+55-81-99-11&=8634,\\
8770+64-75-99-10-8428&=222.
\end{aligned}
\tag{5.4}
$$
因此
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8634.}
\tag{5.5}
$$
有限因子度增加四、$q$ 下界同时减少四，所以目标分支仍为222。没有证明目标成员性，也未把模31的余子式阶搬为特征零阶。

## 6. 实际执行及下一阶边界

[小源码](../notes/2026-11-15-r150-zero-fifth-joint-high-low-left-envelope-789f.py)
SHA256：
~~~
94151693c2a0a9b8fc0eb84d442d6742818503b3cd069bffd82f95f1b0bc1f1b
~~~
实际 run43702348535，step zero-fifth-joint-high-low-left-envelope，
执行源码提交d8f61835d88ce7fcdc458dc262742b2fb5a8d070。
共享数学30秒、实际内存512MiB；数学17.96719050699994秒，
墙钟18.06658638500039秒，退出码0。

| 完整对象 | SHA256 |
|---|---|
| 原零点 $P_5$ | 4b6813118845e3d4b44750ef494a73ed9e756256729e7a217de855ebcbcce985 |
| 完整第五低残差 | d2aa6fedd89e90fce8986ef03f8666626d4bb7aed7778eaee112bfa3f1c6f2c9 |
| 完整第五高残差 | e5f073f642e7a401f69bee84a0cc69c26c50107b78511dbcf58f60fa9c3b65e9 |
| $2295\times999$ 高增广矩阵 | f5cd63180f9a659d9b56a2a888412244d3a7420c7c98ab4d87ce7caa655a2a66 |
| 十一条完整高行升列 | d1d968dd3cf09b0db76a8aa9eac2e0acdd35c311224b7b0248e4a08e61509264 |
| 完整 $1088\times603$ 低增广矩阵 | 0acfd091c8af4d64e4b04ceab15d6fedf62bc9589a391481a0e282874ba7c12b |
| 七条完整低校正 | f614748ca57d796c015b5e1ff81f01c66f5062e5df169af00683bf7c2d31e493 |
| 七条实际高校正 | 7e2c8cace095c575b007f1a652336f0b6991aa28ea73b79daf2e33cd64706d6c |
| 七个 leading 常项 | 55db68184f78d8308414f5440998a3af153488ef49586ea33a3da9a01d8e9e4d |

原完整小回执15059字节，SHA256：
~~~
728d40e8779eba8846ebcd9455c83a7abb32b1709a1a68ff357c7960c247f413
~~~
[已推执行记录](../notes/r150-infinity-remote-session-789f/43702348535-zero-fifth-joint-high-low-left-envelope.json)
保全部输入哈希、原零点四阶规范、完整高低行乘回及实际 leading 系数。大矩阵只作同作业内临时检查点，未上传或长期保存可重算大数据。

2805个三次横向来源的自动消零仅属于当前第五页。第六页中，纯二阶项作用于已有三次横向第四系数，会在这些来源产生真实 forcing；后继必须保留。
