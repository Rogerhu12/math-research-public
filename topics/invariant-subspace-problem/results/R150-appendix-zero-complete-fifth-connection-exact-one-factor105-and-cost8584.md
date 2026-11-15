# R150：零点完整第五连接恰一、公共因子 $K_{105}$ 与条件来源费用 $8584$

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

## 1. 本次实际结论

对原自然参数 $s=0$、原十七式与全部 $6188$ 个次数不超过三的原来源，本次实际有理运算证明

$$
\operatorname{rank}_{\mathbb Q}\beta_{5,0}=1,
\qquad
\dim K_5=18.
\tag{1.1}
$$

这里 $K_5$ 是完整第五左头空间。计算保留全部较低阶连接像及其真实 cochain 回填，不限于固定四阶代表再加最后一次常核校正。完整前五级连接秩为

$$
(\operatorname{rank}\beta_{1,0},\ldots,
 \operatorname{rank}\beta_{5,0})=(4,0,1,3,1).
\tag{1.2}
$$

结合此前第六至八页已经核验的真实左 jet，本次得到

$$
\delta_{4354,0}\ge59,\qquad
\delta_{4353,0}\ge50,\qquad
9\le a_{\max,0}\le16.
\tag{1.3}
$$

原仿射公共因子因此提高为 $K_{105}$。配合当前同选定子式的无穷远阶 $130/125/125$，在原目标成员性成立的前提下，完整来源费用可取 $8584$，目标分支可取 $172$。

主要来源：

- [完整第三连接恰一](R150-appendix-zero-complete-third-connection-exact-one-and-twentytwo-heads.md)；
- [完整第四连接恰三](R150-appendix-zero-complete-fourth-connection-exact-three-and-nineteen-heads.md)；
- [本次通用完整高阶源码](../notes/2026-11-15-r150-zero-complete-higher-full-incoming-789f.py)；
- [原共动作用至十七阶的独立源码](../notes/2026-11-15-r150-original-comoving-jet-actions-through-seventeen-789f.py)；
- [本次完整第五实际回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-complete-fifth-full-incoming.json)；
- [同选定子式无穷远阶 $130/125/125$](R150-appendix-seventeen-source-fourth-pairing-rank-one-sixteen-heads-and-cost8585.md)。

## 2. 原方程与全部低页像

记原共动左方程为

$$
M(s)=A_{\mathrm{new}}(s)^{\mathsf T}
=\sum_{j\ge0}s^jM_j.
\tag{2.1}
$$

原目标与原来源同时经过准确的可逆坐标运输。若

$$
A_{\mathrm{new}}=T A_{\mathrm{old}}V,
$$

则回到原目标坐标的左泛函是 $T^{\mathsf T}\lambda_{\mathrm{new}}$。没有把未经运输的共动数组直接当作原左泛函。

第 $k$ 阶 cochain 是

$$
T_k(v)=\sum_{\ell=0}^k s^\ell\lambda_\ell(v),
\qquad
\sum_{j=0}^{\ell}M_j\lambda_{\ell-j}(v)=0
\quad(0\le\ell\le k).
\tag{2.2}
$$

$K_k$ 表示这些 cochain 的全部常项。已付

$$
\dim K_0=27,\quad
\dim K_1=\dim K_2=23,\quad
\dim K_3=22,\quad
\dim K_4=19.
\tag{2.3}
$$

令 $R_j(v)$ 为真实 $T_{j-1}(v)$ 的第 $j$ 阶 forcing。对同一第四头，任意两个第四 cochain 之差可逐阶减去其最低非零项，写成

$$
sT_3(v_3)+s^2T_2(v_2)+s^3T_1(v_1)+s^4v_0
\pmod {s^5},
\qquad v_i\in K_i.
\tag{2.4}
$$

所以第五 forcing 的全部代表差位于

$$
\operatorname{im}M_0+
R_4(K_3)+R_3(K_2)+R_2(K_1)+M_1K_0.
\tag{2.5}
$$

完整第二连接为零已给

$$
R_2(K_1)\subset
W_1:=\operatorname{im}M_0+M_1K_0.
\tag{2.6}
$$

故完整第五连接须取的商正是

$$
W_4=\operatorname{im}M_0+M_1K_0+
R_3(K_2)+R_4(K_3).
\tag{2.7}
$$

本次同时保留 $R_3$ 和 $R_4$ 的全部实际来源列，而非仅保其商像的维数。式 (2.4) 证明该商吸收所有早期 cochain 选择差。

## 3. 全部高来源与低来源的准确消元

原 $6188$ 个来源按 normal 次数分成

$$
170+918+2295+2805=6188.
\tag{3.1}
$$

非纯目标校正共有

$$
4347=585+3762
=(135+450)+(990+1485+1287)
\tag{3.2}
$$

个坐标。完整第三稿中已经付清高来源齐次核

$$
N_{\mathrm h}:\mathbb Q^2\longrightarrow\mathbb Q^{3762}.
\tag{3.3}
$$

它参数化全部使 $5100$ 个高来源行为零的高校正，包含三、四、五 normal 层的共同消元，未删高层之间的相消。

低常数块及高校正的低输出为

$$
B=[J_0,M_1Q]\in\mathbb Q^{1088\times592},
\qquad
C_{\mathrm h}=(M_0N_{\mathrm h})_{\mathrm{low}}.
\tag{3.4}
$$

$Q$ 保完整七维一次 normal 常核；全部二十个纯常核的 $M_1$ 作用为零。已付

$$
\operatorname{rank}B=582,\qquad
\operatorname{rank}[B,C_{\mathrm h}]=584.
\tag{3.5}
$$

十个纯头对所有参数给精确零 cochain，所有高阶 forcing 恒零。它们始终保留在输出中。完整 $K_2,K_3,K_4$ 的其余头数分别为 $13,12,9$。

本次使用完整十九维第四头的真实 cochain，直接构造九列原 forcing

$$
R_5=
M_5\lambda_0+M_4\lambda_1+M_3\lambda_2
+M_2\lambda_3+M_1\lambda_4
\in\mathbb Q^{6188\times9}.
\tag{3.6}
$$

其 $5100$ 个高来源行在本次实际逐项核验中为零。因此 (3.3) 给出所有可行的高常数校正，完整低方程为

$$
\mathcal M_5=
[B,\ C_{\mathrm h},\ R_{3,\mathrm{low}},
 R_{4,\mathrm{low}},\ R_{5,\mathrm{low}}]
\in\mathbb Q^{1088\times628}.
\tag{3.7}
$$

变量数为 $592+2+13+12+9=628$。旧完整 incoming 的秩已为

$$
\operatorname{rank}
[B,C_{\mathrm h},R_{3,\mathrm{low}},R_{4,\mathrm{low}}]=588.
\tag{3.8}
$$

本次复用原 $582$ 阶单位块及二十七个已核实际 RHS 解，只新增九个单列 Dixon 求解。所有原低行 Schur 均保留；没有重新构造完整逆或重复旧高行大消元。

## 4. 完整第五秩与十八条真实 cochain

实际完整原行核验给出

$$
\operatorname{rank}\mathcal M_5=589,\qquad
\dim\ker\mathcal M_5=628-589=39.
\tag{4.1}
$$

核向最后九个新 leading 参数的投影维数为 $8$。归一化零 leading 参数纤维为

$$
39-8=31=619-588.
\tag{4.2}
$$

由 (2.7)、(3.3) 及完整第四头覆盖，

$$
\operatorname{rank}\beta_{5,0}
=589-588=9-8=1.
\tag{4.3}
$$

加入十个 exact 纯头，得到

$$
\dim K_5=10+8=18.
\tag{4.4}
$$

完整核中，$R_3$ 参数必须按 $s^2T_2$ 回填，$R_4$ 参数必须按 $sT_3$ 回填。若这些参数分别为 $y_3,y_4$，最后常核参数为 $b$，则在原第四 cochain 的对应 leading 组合上加入

$$
\begin{aligned}
\lambda_1&\leftarrow\lambda_1+T_{3,0}y_4,\\
\lambda_2&\leftarrow\lambda_2+T_{3,1}y_4+T_{2,0}y_3,\\
\lambda_3&\leftarrow\lambda_3+T_{3,2}y_4+T_{2,1}y_3,\\
\lambda_4&\leftarrow\lambda_4+T_{3,3}y_4+T_{2,2}y_3+Qb,\\
\lambda_5&=(x,N_{\mathrm h}a).
\end{aligned}
\tag{4.5}
$$

包括各次纯切向分量在内的全部系数均实际保存。重建出的 $13956\times18$ cochain 矩阵逐阶核验原零至五阶方程，原产品数为

$$
6\cdot6188\cdot18=668304.
\tag{4.6}
$$

因此 (4.3) 是完整连接的精确秩；它不只是本次选择的最后校正空间给出的上界。

## 5. Smith 阶、$K_{105}$ 与最大指数

设原零点十四个正 Smith 指数为 $a_1,\ldots,a_{14}$，并记

$$
c_j=\#\{i:a_i\le j\}.
\tag{5.1}
$$

完整前五级连接给出

$$
\#\{a_i=1,2,3,4,5\}=(4,0,1,3,1),
\tag{5.2}
$$

即 $c_1,\ldots,c_5=(4,4,5,8,9)$。此前第六、七、八页真实左 jet 分别给 $c_6\le12,c_7\le12,c_8\le13$；这些已经乘回的 cochain 仍是原方程的真实解，不依赖本次代表规范。

于是

$$
\begin{aligned}
\delta_{4354,0}
&=\sum_i a_i
=\sum_{j\ge0}(14-c_j)\\
&\ge14+10+10+9+6+5+2+2+1=59.
\end{aligned}
\tag{5.3}
$$

去掉最大正指数后，最小十三个正指数之和满足

$$
\begin{aligned}
\delta_{4353,0}
&=\sum_{j\ge0}\max(13-c_j,0)\\
&\ge13+9+9+8+5+4+1+1=50.
\end{aligned}
\tag{5.4}
$$

[完整模 $31$ 仿射最大子式公因子](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md) 已付原零点总长度 $66$，由同常秩单位 Schur 的特化得到特征零总阶上界 $66$。故

$$
a_{\max,0}
=\delta_{4354,0}-\delta_{4353,0}
\le66-50=16.
\tag{5.5}
$$

第八页已有至少一个正指数不小于九，因此

$$
9\le a_{\max,0}\le16.
\tag{5.6}
$$

这里没有将模 $31$ 的最大指数 $11$ 直接升级成特征零结论。

保持其他有限点已付的公共因子，本次可取

$$
\begin{aligned}
K_{105}
&=sK_{104}=s^{45}K_{60}\\
&=s^{59}(s-2)^9(s+6)^9F_+(s)^2F_-(s)^2E_8(s)^2,
\end{aligned}
\tag{5.7}
$$

其中 $F_+,F_-,E_8$ 沿原模型定义。其次数为 $105$，首项系数仍为 $5^6$。

## 6. 当前同选定子式的条件来源费用

沿[十七真实第三来源的第四配对结论](R150-appendix-seventeen-source-fourth-pairing-rank-one-sixteen-heads-and-cost8585.md)，同一选定子式及其原列替换、余子式的无穷远阶下界分别为

$$
130,\qquad125,\qquad125.
\tag{6.1}
$$

令原选定最大子式为 $D$，并写

$$
q=D/K_{105}.
\tag{6.2}
$$

[完整所选模 $31$ 无穷远长度 $243$](R150-appendix-complete-selected-mod31-infinity-length243-degree8527-and-target230.md) 已给 $\deg\overline D=8527$，而自然齐次总次数上界为 $8770$。所以

$$
8422=8527-105
\le\deg q
\le8770-130-105=8535.
\tag{6.3}
$$

沿原完整来源除法与移列构造，三支费用分别为

$$
\begin{aligned}
\text{非基来源}&\le8535-1+45=8579,\\
\text{基来源转移}&\le8770+55-125-105-11=8584,\\
\text{目标分支}&\le8770+64-125-105-10-8422=172.
\end{aligned}
\tag{6.4}
$$

因此，**若**原目标 $h_0t_\nu$ 已属于原十七式在 $\mathbb Q[s]$ 上的像，则其完整来源可按既有同源降度定理取费用不超过

$$
8584.
\tag{6.5}
$$

本次左 jet 和次数界不替代该成员性前提，也不提供新的全局原目标来源证书。

## 7. 原九目标读数

原九目标为

$$
t_j(s,m)=
\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2,
\qquad j=2,\ldots,10.
\tag{7.1}
$$

在准确共动坐标中，它们是 $n_j^2$。本次十八条真实 cochain 的每个 $\lambda_0,\ldots,\lambda_5$ 对这九个平方目标的读数均逐项为零。每块尺寸为 $9\times18$，逻辑 SHA256 均为

8ff26d072c0b6878ea76c513174ceaa5061db500d1a4c482bc398da69e08fe58。

这说明这些实际左 jet 没有给出原九目标的相应局部配对障碍；它不证明局部或全局成员性。

## 8. 实际证据与后继接口

实际运行身份：

- run：43702348535；job：132776011109；
- step：zero-complete-fifth-full-incoming；
- 执行来源提交：71ce2b1a600a1e66cc18533a52ed80f82c238597；
- 数学耗时：约 $17.2752$ 秒；
- 通用入口 SHA256：9bf405d3aa65d40a8ebeb3fc87f3e8bd686814db371657abe9794f92e59099b8；
- 原始小回执：$48056$ 字节，SHA256 为 2a480a7fad3472bca0a73edbc70235088f536ceeaedf9326a5fb825a05c57ea0；
- 主线外回执：$54297$ 字节，SHA256 为 fea654c24230c62ec3b872e96f16982013578fee4944d90af82b2d6b5e7aab75。

主要逻辑身份：

| 对象 | 尺寸 | 逻辑 SHA256 |
|---|---:|---|
| 全部新原第五 forcing | $6188\times9$ | 456185dae6684eb031bedcae1a5f0dc06312859dc1c8a5c490c0c4d435f6d5d9 |
| 保全部原行的 Schur | $1088\times36$ | bc1a83100ea1cf30ba22ef425f0145317438bd1242f5a7a2640b8e9b9d0caf21 |
| 完整低核 | $628\times39$ | d07d50185aca163f51a63f067e3a1410abf3d9a3858ef0bae124e172d8d57f44 |
| 全部十八条第五 cochain | $13956\times18$ | a82662c2ae2f6a574ab80d28e8f46808a550f3c293f8b4c08d065962377e1bcd |

检查点 binding 为 15b340501e6d44d36583e8c22f6dd211e33ecb7234a9fcb91c0b4ce1765f265d；已核 manifest 为 $20985$ 字节，SHA256 为 adfc0d8f65fde3582d8ddbe64dc93cfa6181a385fe164af200f8e919b36ca3f3。完整数组仅保留在同 job 临时检查点，Git 保存源码、参数、运行身份及小回执。

下一完整第六页的旧像必须为

$$
W_5=\operatorname{im}M_0+M_1K_0+
R_3(K_2)+R_4(K_3)+R_5(K_4).
\tag{8.1}
$$

相应参数须分别按 $s^3T_2,s^2T_3,sT_4$ 回填全部系数。该页复用三十六个旧实际 RHS，仅新增完整十八头中的八个非 exact forcing；高来源是否为零须在新实际运行中重新核验。
