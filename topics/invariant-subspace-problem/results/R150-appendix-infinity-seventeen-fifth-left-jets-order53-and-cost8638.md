# R150：十七条五阶左延拓、无穷远公共阶53与条件来源费8638

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿从已经实际验证的九条四阶左 jet 出发，保持全部先前校正规范，仅加入原自然参数的五阶项。完整高行使九个方向均可继续提升；随后保所有高行自由量作低行消元，得到七个独立的真实五阶 leading 方向。再加十个恒等纯切向方向，原完整图有十七条常项独立的五阶左零延拓。

因此无穷远最大、低一阶子式的公共阶分别至少53、47。同一29条精确 Koszul 曲线给指定子式、原来源换列、cofactor 的阶至少82、81、75。结合已付 $K_{95}$ 和同一子式模31次数8527，得到 $8432\le q\le8593$，统一条件来源费8638，目标分支222。

## 1. 完整原图与同一九条四阶延拓

保持原反序、自然参数 $u=1/s$ 和原十七式的全部来源：
$$
A(u)=\sum_{k\ge0}u^kA_k:
\mathbb Q[[u]]^{6188}\longrightarrow\mathbb Q[[u]]^{4367}.
\tag{1.1}
$$
常数秩4340，函数域秩4354；常数左余空间维数27，正 Smith 指数共有十四个。

共动矩为
$$
m_j=\sum_{k=0}^j\binom jk u^{j-k}n_k,\qquad
c=n_0,\quad d=n_1,\quad z_j=n_j\quad(2\le j\le10).
\tag{1.2}
$$
原来源的所有次数至多三单项式以及全部目标均完整运输。若
$A_{\rm new}=T A_{\rm old}V_{\rm src}$，则原左 jet 是
$T^{\mathsf T}\lambda_{\rm new}$。

[前一第四页](R150-appendix-infinity-nineteen-fourth-left-jets-order49-and-cost8648.md)
已给九条
$$
g(u)=g_0+ug_1+u^2g_2+u^3g_3+u^4g_4,\qquad
A(u)^{\mathsf T}g(u)=O(u^5).
\tag{1.3}
$$
它们的每个完整系数均绑定实际第四页低、高校正及 leading 矩阵的哈希。本次不换用另一组四阶解。

$g_0$ 最高一次横向，$g_1$ 只支持一次横向，$g_2,g_3$ 最高二次横向，$g_4$ 最高三次横向。记
$g_4=g_4^{\rm lo}+g_4^{(3)}$，分别为585维一、二次横向部分及990维三次横向部分。

同一前稿的九维基来自原十二维基的坐标
$0,1,2,4,5,8,9,10,11$。此外，十个纯泛函
$$
c,c^2,\ldots,c^5,\qquad d,cd,\ldots,c^4d
\tag{1.4}
$$
沿全参数恒等杀掉全部来源。

此前完整连接的累积秩满足
$$
r_1\le4,\quad r_1+r_2\le4,\quad
r_1+r_2+r_3\le5,\quad r_1+r_2+r_3+r_4\le8.
\tag{1.5}
$$
本稿不用任何未付的第三、第四页秩下界。

## 2. 原五阶纯项与完整残差

原切向身份保持
$$
\Gamma(u;c,d,0)=0,\qquad
N(u;c,d,0)=4d^2g_\infty(u)v(u)v(u)^{\mathsf T},
$$
$$
v(u)=(1,u,\ldots,u^5)^{\mathsf T},\qquad
g_\infty(u)=-2u^2-8u^3+24u^4.
\tag{2.1}
$$
以 $K^\sharp$ 定义
$$
p_0=-\zeta^4-\zeta^5,\quad
p_1=5\zeta^3+5\zeta^4+5\zeta^5,\quad
p_2=-8\zeta^2-4\zeta^3-32\zeta^4,\quad
p_3=5\zeta-4\zeta^2+54\zeta^3.
$$
五阶极化系数为
$$
8g_2(p_0p_3+p_1p_2)+4g_3(2p_0p_2+p_1^2)+8g_4p_0p_1
$$
$$
=720\zeta^5-336\zeta^6+992\zeta^7-2880\zeta^8-3008\zeta^9-1760\zeta^{10}.
\tag{2.2}
$$
所以按原 $N_0,\ldots,N_{10},\Gamma_0,\ldots,\Gamma_5$ 顺序，
$$
F_5(c,d,0)=
d^2(0,0,0,0,0,720,-336,992,-2880,-3008,-1760,0,0,0,0,0,0)^{\mathsf T}.
\tag{2.3}
$$
源码分别以 (2.1) 的有限卷积和原 $J_2,J_3,L_y$ 物理映射核对 (2.3)。先前0至4阶映射的全部已付哈希保持；没有用新的五阶公式重定义先前规范。

完整第五残差为
$$
R_5=A_5^{\mathsf T}g_0+A_4^{\mathsf T}g_1+
A_3^{\mathsf T}g_2+A_2^{\mathsf T}g_3+A_1^{\mathsf T}g_4.
\tag{2.4}
$$
记 $F_k^{(0)}=d^2\sigma_k$，其中 $F_0^{(0)}=F_1^{(0)}=0$。

前1088个纯、一次横向来源的残差记为 $R_{\rm lo}$。其构造保留：

- $A_3^{\mathsf T}g_2$ 的完整原三阶二次横向系数，以及纯三阶项；
- $A_2^{\mathsf T}g_3$ 的完整原二阶二次横向系数，以及纯二阶项；
- $A_1^{\mathsf T}g_4^{\rm lo}$ 和三次横向部分 $K_3^{(1)}g_4^{(3)}$。

这里 $K_3^{(1)}$ 是由 $F_1$ 的二次横向项给出的完整低作用。不能因为 $F_1$ 的纯项为零，就删除它对三次横向 $g_4$ 的作用。

对于2295个二次横向来源 $c^ad^bz_jz_kF_i$、$a+b\le1$，完整残差恰为
$$
(R_{\rm hi})_{i,a,b,j,k}
=\sigma_{3,i}(g_2)_{c^ad^{b+2}z_jz_k}
+\sigma_{2,i}(g_3)_{c^ad^{b+2}z_jz_k}
+\left(H_3^{(1)}g_4^{(3)}\right)_{i,a,b,j,k}.
\tag{2.5}
$$
$H_3^{(1)}$ 保 $F_1$ 的全部常数、$c$、$d$ 线性横向系数。因此高行不是只保纯二阶项的一列近似。

剩余2805个三次横向来源在本次 (2.4) 中严格为零：前四项的泛函最高二次横向；最后一项中 $F_1$ 至少一次横向，而 $g_4$ 最高三次横向。因此
$$
1088+2295+2805=6188
\tag{2.6}
$$
覆盖全部原来源。

## 3. 联合高低校正与七个独立常项

继续使用原常系数三次横向作用 $H_3:\mathbb Q^{990}\to\mathbb Q^{2295}$ 和
$K_3:\mathbb Q^{990}\to\mathbb Q^{1088}$。它们分别保 $F_0$ 的
$\ell+c\,b+d\,a$ 线性横向项及二次横向项，见[第四页完整定义](R150-appendix-infinity-nineteen-fourth-left-jets-order49-and-cost8648.md)。

实际高矩阵满足
$$
\operatorname{rank}H_3=988,\qquad
\operatorname{rank}[H_3,R_{\rm hi}]=988.
\tag{3.1}
$$
因此九个既有 leading 坐标在高行全部可升。算法保留完整十一维核
$$
\begin{pmatrix}Y\\Z\end{pmatrix},\qquad
H_3Y+R_{\rm hi}Z=0,
\quad
Y\in\mathbb Q^{990\times11},\quad Z\in\mathbb Q^{9\times11}.
\tag{3.2}
$$
前两列是原同一 $\ker H_3$，其 leading 块为零，后九列 leading 块为 $I_9$。全部2295行实际乘回。

令
$$
J_0=A_0^{\mathsf T}|_{\text{585个一、二次横向目标}},\qquad
J_1=A_1^{\mathsf T}Q=\begin{pmatrix}P_1Q\\0\end{pmatrix},
\tag{3.3}
$$
其中 $Q$ 是原135维一次横向目标上的七维常左核。第四系数允许增加 $QB$；$A_0^{\mathsf T}QB=0$ 保持已经完成的第四阶身份，而它在第五页的作用是 (3.3)，高行仍为零。

高行消去后保全部核自由量，形成
$$
M_5=[J_0,J_1,K_3Y+R_{\rm lo}Z]\in\mathbb Q^{1088\times603}.
\tag{3.4}
$$
实际前缀秩为578、582、584，全矩阵秩586。对完整核的 leading 投影直接取秩，得到准确的七维像。

以 $e_0,\ldots,e_8$ 表示原九条四阶 jet 的有序基，七条实际独立 leading 列为
$$
e_0,\ e_1,\ e_2,\ 
e_5-\frac{107}{9}e_3-\kappa e_4,\ 
e_6-\frac{107}{9}e_4,\ e_7,\ e_8,
\tag{3.5}
$$
$$
\kappa=\frac{144423978726553054169}{204289227678729600}.
$$
这些有理系数来自同一已付规范的完整 RREF，没有另选低阶解。

记对应核系数为 $H,B,C$，则
$$
J_0H+J_1B+(K_3Y+R_{\rm lo}Z)C=0.
\tag{3.6}
$$
真实五阶左 jet 明确为
$$
\lambda(u)=\sum_{j=0}^3u^j g_jZC+
u^4(g_4ZC+QB)+u^5(H+YC).
\tag{3.7}
$$
$H,YC$ 分别嵌入一、二次和三次横向目标。(3.2)、(3.6) 及全部先前身份给
$$
\boxed{A(u)^{\mathsf T}\lambda(u)=O(u^6)}
\tag{3.8}
$$
于全部6188来源。十个恒等方向与这七个常项独立，故有十七条独立五阶左延拓。

该计算只构造合法延拓。没有把两维受限残差当成完整第五连接的秩下界；更高横向目标或不同低阶延拓是否可以升起更多方向，仍未由本次计算判定。

## 4. 完整公共阶53、47及指定82、81、75

十七个独立五阶常项给
$$
r_1+r_2+r_3+r_4+r_5\le27-17=10.
\tag{4.1}
$$
结合 (1.5)，十四个正 Smith 指数的和至少
$$
\begin{aligned}
\delta_{4354,\infty}
&\ge84-r_1-(r_1+r_2)-(r_1+r_2+r_3)
-(r_1+r_2+r_3+r_4)
-(r_1+r_2+r_3+r_4+r_5)\\
&\ge84-4-4-5-8-10=53.
\end{aligned}
\tag{4.2}
$$
对最小十三个正指数，将84换为78，得到
$$
\boxed{\delta_{4354,\infty}\ge53,\qquad
\delta_{4353,\infty}\ge47.}
\tag{4.3}
$$

由[完整 Smith 与同一29条精确 Koszul 曲线](R150-appendix-full-smith-formal-koszul-selected-orders60-59-56-and-cost8685.md)，
$$
\boxed{
v_\infty D\ge82,\qquad
v_\infty D_{\rm original\ replacement}\ge81,\qquad
v_\infty(\text{cofactor})\ge75.}
\tag{4.4}
$$
一般解析目标换列只能使用 cofactor75，不能用原来源换列81。

## 5. K95下的原来源条件成本

[零点第四页](R150-appendix-zero-nineteen-fourth-left-jets-factor95-and-cost8642.md)
已经给 $K_{95}$，次数95、最高系数 $5^6$；本稿不假定零点第五页已成。

[同一子式完整模31长度243](R150-appendix-complete-selected-mod31-infinity-length243-degree8527-and-target230.md)
给 $\deg_{\mathbb Q}D\ge8527$。原总权为 $H=8770$。对
$d_*=D/K_{95}$、$q=\deg d_*$，
$$
\boxed{8432\le q\le8770-82-95=8593.}
\tag{5.1}
$$
保持原来源权 $\max a_\ell=55$、$\delta_\ell=a_\ell-10$、$\max\delta_\ell=45$，转移多项式为
$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{95},\qquad A_JP_\ell=d_*A_\ell,
$$
$$
\deg(P_\ell)_j\le H-a_j+a_\ell-81-95.
\tag{5.2}
$$
明确假定 $b_\nu=h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A$，且原目标权 $\tau_\nu\le64$。成员性使
$$
T_\nu=\operatorname{adj}(A_{I,J})(b_\nu)_I/K_{95}
$$
为多项式，且
$$
\deg(T_\nu)_j\le H-a_j+\tau_\nu-75-95.
\tag{5.3}
$$
沿原非基除法及完整来源转移，三个成本分支为
$$
\begin{aligned}
q-1+45&\le8637,\\
8770+55-81-95-11&=8638,\\
8770+64-75-95-10-8432&=222.
\end{aligned}
\tag{5.4}
$$
因此
$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8638.}
\tag{5.5}
$$
这个结论不证明目标成员性，也没有把有限域 cofactor 的阶当成特征零阶。

## 6. 实际运行与下一阶边界

[小源码](../notes/2026-11-15-r150-infinity-fifth-joint-high-low-left-envelope-789f.py)
SHA256：
~~~
0e8a04b75d85708305cbcb645da4df13348aabf3b71951cc2ff72bd05f5513ba
~~~
实际 run43702348535，step infinity-fifth-joint-high-low-left-envelope，
执行源码提交470a799c88b44f67cb1f8504f619fd4949a37137。
共享数学30秒、实际内存512MiB；数学15.752552958000251秒、
墙钟15.849811115999728秒，退出码0。

| 完整对象 | SHA256 |
|---|---|
| 原 $P_5$ | e59ea4444ce2ca2f9050de03c41d87dc9d19b536efa1c69cf4c646c9b8183751 |
| 完整第五低残差 | afa62bbdf00c6cb08bb0ac2fa24a9cefeffb456a88171e642f56c19b916aa4ac |
| 完整第五高残差 | e5f073f642e7a401f69bee84a0cc69c26c50107b78511dbcf58f60fa9c3b65e9 |
| $2295\times999$ 高增广矩阵 | 21b65f541316465321e37c197209a4002868dca296574c3393a9466f8a868687 |
| 完整十一条高行升列 | 4411183498cbdb63db83317b53436ac4deb4e374b517e22155254392cf2b3093 |
| $1088\times603$ 低增广矩阵 | c4c1d04ffba4d11e58250d5a2d7d7b273c123c09a157b9ef259a5f3ba66b3902 |
| 七条完整低校正 | b702def1494de76876628d42987f6f9069d3b63de801b6a39232513e476f1e37 |
| 七条实际高校正 | 7e2c8cace095c575b007f1a652336f0b6991aa28ea73b79daf2e33cd64706d6c |
| 七个 leading 常项 | da47f9b0b2618421c4df755f71c531a451b38026bd55444e0d76db7ad5e76d51 |

原完整小回执14709字节，SHA256：
~~~
381d159232a410c5a68a891b93dea6afe0b45e3f7a8ac7966b5470001d0b6970
~~~
[已推执行记录](../notes/r150-infinity-remote-session-789f/43702348535-infinity-fifth-joint-high-low-left-envelope.json)
保全部输入身份、同九条四阶 jet 的完整哈希、全部高低行乘回及实际 leading 系数。大矩阵只在同作业临时检查点保存，没有上传可重算大数据。

最后2805个三次横向来源的自动消零只适用于本次第五页。若继续第六页，$A_2^{\mathsf T}$ 作用于已存在的三次横向第四系数，会出现纯二阶项乘三次横向来源的真实贡献；不得再把这一组来源删除。
