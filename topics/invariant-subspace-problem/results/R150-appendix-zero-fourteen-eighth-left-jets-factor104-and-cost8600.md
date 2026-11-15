# R150：零点十四条八阶左延拓、K104与条件来源费8600

日期：2026-11-15 UTC。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

原零点的五条已付七阶左 jet 中，本次完整延拓方程保留四个独立头。全部4347个非纯目标校正及最后常核歧义均保留，最终在全部6188原来源上逐项乘回。加上十个沿全参数恒等的纯切向头，得到十四个独立八阶可延头。

由此得到共同零点阶58、49，有限公共因子 $K_{104}=sK_{103}$，最大正 Smith 指数在9至17之间。结合已经独立证明的指定无穷远阶 $114/110/110$，原目标成员性条件下的统一来源费为8600。本条不把四头包络当作完整第八连接的秩下界。

## 1. 同一原参数的第八方程

仍用原自然参数 $s$、原十七式及全部次数至多三的来源：

$$
A(s)=\sum_{i\ge0}s^iA_i:
\mathbb Q[[s]]^{6188}\longrightarrow\mathbb Q[[s]]^{4367}.
$$

[第七页](R150-appendix-zero-fifteen-seventh-left-jets-factor103-and-cost8621.md)已经给五个独立头及完整实际 cochain

$$
g(s)=\sum_{j=0}^7s^jg_j,\qquad A(s)^{\mathsf T}g(s)=O(s^8).
\tag{1.1}
$$

本次读入同一个已付七阶包，其原实际形状为 $13304\times5$。入口核对原小回执、临时 manifest、全部矩阵字节及逻辑哈希；不另选头或只取其常项。

完整共动运输保持

$$
m_j=\sum_{a=0}^j\binom ja s^{j-a}n_a,\qquad c=n_0,\ d=n_1.
\tag{1.2}
$$

来源乘子及目标单项式一起运输。若 $A_{\rm new}=T A_{\rm old}V_{\rm src}$，原目标的左 jet 为 $T^{\mathsf T}\lambda_{\rm new}$。所有原系数仍从原十七式构造。

新残差为

$$
R_8=\sum_{i=1}^8A_i^{\mathsf T}g_{8-i}
\in\mathbb Q^{6188\times5}.
\tag{1.3}
$$

先逐元素核对实际 $g_1,\ldots,g_7$ 的全部二至五次横向块为零，再形成 (1.3) 的所有原行。其2295个二次横向来源和2805个三次横向来源行确切为零。没有仅凭旧零块哈希删除高来源。

令 $Q$ 为一次横向目标上的完整七维常左核。它满足全部原行上的 $A_0^{\mathsf T}Q=0$。20个纯常左核的 $A_1^{\mathsf T}$ 作用也为零，因此最后常核的有效歧义可写作 $Qb$。待解的完整新方程是

$$
A_0^{\mathsf T}x+A_1^{\mathsf T}Qb+R_8z=0,
\quad
x\in\mathbb Q^{4347},\quad b\in\mathbb Q^7,\quad z\in\mathbb Q^5.
\tag{1.4}
$$

$x$ 包括所有一至五次横向目标，未预限其横向次数。

## 2. 完整高齐次空间与原低单位的复用

[第六页](R150-appendix-zero-fifteen-sixth-left-jets-exact-first-four-factor101-and-cost8625.md)保存的完整高、中层解矩阵是

$$
M\in\mathbb Q^{3769\times9}.
$$

其前3762行为三至五次横向校正，末7行为原头投影 $Z$，且 $\operatorname{rank}Z=7$。取完整核 $Q_Z\in\mathbb Q^{9\times2}$：

$$
MQ_Z=\begin{pmatrix}N\\0\end{pmatrix},
\qquad N\in\mathbb Q^{3762\times2}.
\tag{2.1}
$$

第六页的顶层、中层均为全部原解的双向参数化，所以 $N$ 恰为 $A_0^{\mathsf T}$ 在全部5100个高来源上的完整高校正齐次空间。旧顶层三维齐次自由量先经真实中层兼容，再保为 (2.1)，没有因本次高残差为零而丢弃。入口重新核 $N$ 的独立性及全部5100行产品。

设旧完整低右端为 $C_{\rm old}$，旧582阶原单位块为 $U_0$，其已付原解为 $X_{\rm old}$。由 $ZQ_Z=0$，旧右端的头项严格消去：

$$
C_h=C_{\rm old}Q_Z=(A_0^{\mathsf T}N)_{\rm low},
\qquad X_h=X_{\rm old}Q_Z,
$$

$$
U_0X_h+(C_h)_I=0.
\tag{2.2}
$$

本次又在原未缩放582行核 (2.2)。因此两列高齐次右端的解确由同源线性组合取得，不形成旧988阶或582阶完整逆。

令

$$
B=[J_0,A_1^{\mathsf T}Q]\in\mathbb Q^{1088\times592},
\qquad \operatorname{rank}B=582,
$$

其中 $J_0$ 是585个一、二次横向校正的完整低行作用。真实第八低系统为

$$
M_8=[B,C_h,(R_8)_{\rm low}]
\in\mathbb Q^{1088\times599}.
\tag{2.3}
$$

只解五个新右端；各列独立清分母后恢复原比例，先核原单位行，再保全部1088行的 Schur。实际得到

$$
\boxed{\operatorname{rank}M_8=585,\qquad
\dim\ker M_8=14.}
\tag{2.4}
$$

完整 Schur 秩为3。全部高、低齐次列都保存在该完整核中。

## 3. 四个真实头及所有原产品

完整核在原五头上的投影秩为4。采用已付五头的次序及从0起的坐标，实际头矩阵为

$$
Z_8=
\begin{pmatrix}
1&0&0&0\\
0&0&0&\gamma\\
0&1&0&0\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},
\qquad
\gamma=\frac{45270477679335313124123}
{490812321091801833381024768}.
\tag{3.1}
$$

这明确保留原来源组合，而不是把四头替成任意四个旧坐标。完整零头纤维维数 $14-4=10$，与已经精确证明的第一连接秩4给出的 $14-4=10$ 相符。

若对应完整核列为 $(x_{\rm lo},b,a,Z_8)$，则

$$
\lambda(s)=
\sum_{j=0}^{6}s^jg_jZ_8+
s^7(g_7Z_8+Qb)+
s^8(x_{\rm lo}+Na).
\tag{3.2}
$$

$A_0^{\mathsf T}Q=0$ 保持所有已付0至7阶身份；第八系数恰是 (1.4)。最终在全部 $6188\cdot4=24752$ 个原来源坐标乘回，得到

$$
\boxed{A(s)^{\mathsf T}\lambda(s)=O(s^9).}
\tag{3.3}
$$

四个头独立于十个沿全 $s$ 恒等的纯切向头。所得十四维头空间是严格存在性结论；它没有断言所有八阶可延头都在这一固定七阶族中，因而不据此报完整第八连接的正秩。

## 4. 共同阶58、49与有限因子K104

令 $c_j$ 为前 $j$ 个完整连接秩的累积和。第六页已经证明 $c_1=c_2=4$。本次十四个独立八阶可延头给

$$
c_8\le27-14=13.
$$

连同原各页，

$$
(c_1,\ldots,c_8)
\le(4,4,5,8,10,12,12,13).
\tag{4.1}
$$

原常秩4340、泛秩4354，故有十四个正 Smith 指数。其阈值1至9的计数至少为

$$
14,\ 10,\ 10,\ 9,\ 6,\ 4,\ 2,\ 2,\ 1.
$$

求和以及逐阈值最多少一，分别得到

$$
\boxed{\delta_{4354,0}\ge58,\qquad
\delta_{4353,0}\ge49.}
\tag{4.2}
$$

[完整模31仿射 gcd](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)的 $s^{66}$ 因子给特征零上界 $\delta_{4354,0}\le66$。故最大正指数满足

$$
\boxed{9\le a_{\max}
=\delta_{4354,0}-\delta_{4353,0}\le66-49=17.}
\tag{4.3}
$$

这里没有把有限域最小多项式的指数11直接搬成特征零最大指数。

其余有限公共因子不变：

$$
\boxed{
K_{104}=sK_{103}=s^{44}K_{60}
=s^{58}(s-2)^9(s+6)^9F_+^2F_-^2E_8^2.}
\tag{4.4}
$$

其次数104，最高系数仍为 $5^6$，整除全部原最大子式。本条不称 $K_{104}$ 已是完整特征零最大子式 gcd。

## 5. 原目标成员性条件下的来源费8600

[所选自然第三连接精确秩3](R150-appendix-selected-natural-third-connection-exact-three-twentyone-heads-and-cost8601.md)已经给同一指定子式 $D$、原来源换列、cofactor 的无穷远阶至少

$$
114,\qquad110,\qquad110.
$$

同一指定 $D$ 的非零模31次数为8527，原总权为8770。置 $d_*=D/K_{104}$、$q=\deg d_*$：

$$
\boxed{8423=8527-104\le q\le8770-114-104=8552.}
\tag{5.1}
$$

保原最大列权55、成本偏移 $\delta_\ell=a_\ell-10$、最大偏移45。原来源转移为

$$
P_\ell=\operatorname{adj}(A_{I,J})(A_\ell)_I/K_{104},
\qquad A_JP_\ell=d_*A_\ell
$$

在全部4367输出成立；其分量次数界是
$\deg(P_\ell)_j\le8770-a_j+a_\ell-110-104$。

明确以 $h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A$ 为前提，原目标权界 $\tau_\nu\le64$ 保持。三个实际成本分支为

$$
\begin{aligned}
q-1+45&\le8596,\\
8770+55-110-104-11&=8600,\\
8770+64-110-104-10-8423&=187.
\end{aligned}
\tag{5.2}
$$

因此

$$
\boxed{
h_0t_\nu\in\operatorname{im}_{\mathbb Q[s]}A
\Longrightarrow
\exists y_\nu:\ Ay_\nu=h_0t_\nu,\quad
\operatorname{cost}(y_\nu)\le8600.}
\tag{5.3}
$$

未由左 jet 或有限模证书补入该成员性前提。

## 6. 九原目标读数与实际记录

原目标为

$$
t_j(s,m)=
\left(\sum_{a=0}^j\binom ja(-s)^{j-a}m_a\right)^2,
\qquad 2\le j\le10.
$$

同一共动运输后它们为 $n_j^2$。本次 $\lambda_0,\ldots,\lambda_8$ 的九个平方坐标均逐项为零。各 $9\times4$ 零矩阵的逻辑哈希均为

~~~
8cad816e890c2ae9f98b85089c1de9f39299e7a2a733ce30590edd36d2da076e
~~~

所以这组实际截断左 jet 未给九目标新的非零配对障碍；这仍不是目标成员性证明。

[实际小回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-eighth-reused-complete-high-kernel.json)对应 run43702348535、step zero-eighth-reused-complete-high-kernel，执行源码提交
964290743f53c0a8cff9b1644746740c62b14370。
数学用时9.086597736999465秒，墙钟9.188534271999742秒，退出码0；实际上限180秒、2048MiB。

[源码](../notes/2026-11-15-r150-zero-eighth-reused-complete-high-kernel-789f.py)为24859字节，SHA256

~~~
37417c1be7a2e3b6a97b5b467187725eb6acfcc528994eb66150a421717eefde
~~~

| 完整实际对象 | 形状 | 逻辑SHA256 |
|---|---:|---|
| 原第八残差 | $6188\times5$ | f71b6239ddfe9ba7bcefe44d4da0c7160e1a6575a5b4d7576efbddd6ae45d5bc |
| 完整低核 | $599\times14$ | a3c02d352e9d79bec573f50313f988ba2729c81d9532095d581c8ded89574362 |
| 四个实际头 | $5\times4$ | 453a9564a7cf165e8bc3aa9c338a725d5a501ebbae6a10c8db834e74aca202a0 |
| 全部0至8阶cochain | $17651\times4$ | e3f77a4210b49683b80761c9d56a4c813726f4d905e2ce0380742ebd62f82076 |

完整 cochain 的临时 gzip 为187354字节，SHA256
dde7ce7fcdeee9f417fc6ca46d44409c6b6f717d7d7d60b4b724c0665a407471。
数学绑定为

~~~
534c92386282dde35d7745a9893d0415f5fadf11f12fc2a1ebd94babd9671734
~~~

实际数学小回执35278字节，SHA256
6790eb6ed2da79745ed41ba479a95d61b0fae0fea04c92b39ac8bbf55a9b1cc1。
外层回执40955字节，SHA256
05d534b390673fc26d1bccb1ef84ff04a9de1896970c9dc10d6e86fe0053fa4a。

所有大数组只在同一实际作业内临时保留。旧顶层、中层消元和已付右端均未重做；全部齐次核、原来源乘子及最后常核歧义保持。
