# R150：零点完整第三连接恰一及二十二维真实第三左头

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

## 1. 结论与范围

本文在原自然参数 $s=0$、原十七个多项式方程和全部 $6188$ 个次数不超过三的原来源上，证明完整第三连接满足

$$
\operatorname{rank}_{\mathbb Q}\beta_{3,0}=1.
\tag{1.1}
$$

此前已付完整第一、第二连接秩为

$$
\operatorname{rank}_{\mathbb Q}\beta_{1,0}=4,\qquad
\operatorname{rank}_{\mathbb Q}\beta_{2,0}=0.
\tag{1.2}
$$

因而完整第三左头空间恰为 $22$ 维。本次给出全部 $22$ 条真实第三 cochain，逐阶核验了全部原来源的

$$
4\cdot6188\cdot22=544544
\tag{1.3}
$$

个有理恒等式。所得第三连接像的非零方向，是已付三维一次横向二阶头中的第三个规范方向；全部二十个纯切向头和前两个规范横向头都可升至第三阶。

这里的“完整”包括全部 $4367$ 个目标坐标中的常数校正以及全部早期 cochain 选择所产生的第三 forcing 歧义。它不是此前仅允许低 normal 次数校正的包络秩，也不是后续 $5\to4\to2$ 固定代表族的秩。

本次把旧上界 $\operatorname{rank}\beta_{3,0}\le1$ 收紧为等式，不提高已付

$$
\delta_{4354,0}\ge58,\qquad
\delta_{4353,0}\ge49,\qquad K_{104}.
\tag{1.4}
$$

原目标的 $\mathbb Q[s]$ 成员性仍未由这些局部左 jet 证明。

本次实际运行及源码见：

- [实际完整第三回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-complete-third-reused-full-high.json)；
- [完整第三源码](../notes/2026-11-15-r150-zero-complete-third-reused-full-high-789f.py)；
- [完整第六页及第一连接恰四](R150-appendix-zero-fifteen-sixth-left-jets-exact-first-four-factor101-and-cost8625.md)；
- [原第三低支持包络](R150-appendix-zero-twenty-two-third-left-jets-factor89-and-cost8654.md)；
- [原第八页及 $K_{104}$](R150-appendix-zero-fourteen-eighth-left-jets-factor104-and-cost8600.md)。

## 2. 原矩阵、共动坐标与左头

令 $A(s)$ 是原十七式的完整 $4367\times6188$ Macaulay 矩阵。原方程与全部次数不超过三的乘子同时按真实共动平移运输：

$$
m_j=\sum_{a=0}^j\binom ja s^{j-a}n_a.
\tag{2.1}
$$

这在来源和目标上都是自然参数环中的可逆变换。若运输后矩阵记为

$$
A_{\mathrm{new}}(s)=T(s)A(s)V(s),
\tag{2.2}
$$

则新坐标左列回到原目标坐标的规则是

$$
\lambda_{\mathrm{old}}(s)=T(s)^{\mathsf T}\lambda_{\mathrm{new}}(s).
\tag{2.3}
$$

不能把新左数组当作未运输的原目标泛函。以下在已运输坐标中写

$$
M(s)=A_{\mathrm{new}}(s)^{\mathsf T}
=\sum_{i\ge0}s^iM_i.
\tag{2.4}
$$

第 $k$ 阶左 cochain 是一组 $\lambda_0,\ldots,\lambda_k$，满足

$$
\sum_{i=0}^jM_i\lambda_{j-i}=0,\qquad 0\le j\le k.
\tag{2.5}
$$

$K_k$ 表示所有可出现的 $\lambda_0$。原常数秩为 $4340$，故

$$
\dim K_0=4367-4340=27.
\tag{2.6}
$$

由已付 (1.2)，

$$
\dim K_1=\dim K_2=23.
\tag{2.7}
$$

本次恢复的是这整个 $23$ 维 $K_2$，而非后来某个更小的固定代表族。

按 normal 次数分层，全部目标坐标数为

$$
20,\ 135,\ 450,\ 990,\ 1485,\ 1287,
\tag{2.8}
$$

全部来源行数为

$$
170,\ 918,\ 2295,\ 2805.
\tag{2.9}
$$

二者分别合计 $4367$ 与 $6188$。纯目标 $20$ 维属于 $\ker M_0$；在共动坐标中亦有 $M_1$ 在该纯块为零。其余 $27-20=7$ 个常数左头用完整规范矩阵 $Q$ 表示。

## 3. 全部二阶头及其真实 cochain 的恢复

已付二阶来源包括十个非 exact 纯切向头、三个规范横向头，以及十个对所有参数精确的纯切向头。

最后十个纯头对应 $c,d$ 中 $d$ 次数不超过一的纯目标读数。原十七式在切向平面上的纯部分含因子 $d^2$，所以这些头对整个参数函数恒为零。前十三个头则保留原先已核的 canonical first/second sections。

具体地，记 $P_0$ 是纯来源对一次 normal 目标的 $170\times135$ 矩阵。其秩为 $128$，$Q$ 为完整七维右核。原第一连接的三维核基记为 $V$，令

$$
q_0=QV,\qquad P_0W=P_1q_0.
\tag{3.1}
$$

旧纯二阶校正保原来的 $132$ 阶单位子块规范。旧横向二阶三列则从已付 $582$ 阶真实单位块恢复，未重复原 $1088$ 行的大 RREF。恢复后的 $\lambda_1,\lambda_2$ 与旧规范矩阵逐 SHA 一致，并逐原式乘回全部 $0,1,2$ 阶。

全部二阶 cochain 临时矩阵为 $875\times23$，逻辑 SHA256 为

673c8c530d674fec3e0b6aa395a7e116ebd4dbe140b5c81fcbfdf1b2ccc62c74。

其二十三个头线性无关；与 (2.7) 比较，它们就是完整 $K_2$。

## 4. 为什么第三连接只需商第一连接像

设同一个 $\lambda_0\in K_2$ 有两组二阶 cochain。其差写为

$$
(0,\eta_1,\eta_2).
\tag{4.1}
$$

由 (2.5)，

$$
M_0\eta_1=0,\qquad
M_1\eta_1+M_0\eta_2=0.
\tag{4.2}
$$

因此 $\eta_1\in K_1$，而第三 forcing 的差为

$$
M_2\eta_1+M_1\eta_2.
\tag{4.3}
$$

完整 $\beta_{2,0}=0$ 的含义正是：对每个这样的真实一阶 lift，(4.3) 属于

$$
W_1:=\operatorname{im}M_0+M_1K_0.
\tag{4.4}
$$

故

$$
\beta_{3,0}(\lambda_0)
=
[M_3\lambda_0+M_2\lambda_1+M_1\lambda_2]
\quad\text{于 }\mathbb Q^{6188}/W_1
\tag{4.5}
$$

与二阶代表的选择无关。既已使用完整 $K_2$，只要 (4.4) 的全部常数校正和全部 $M_1K_0$ 都被保留，得到的便是完整第三连接。

这一步不能替换成“只保某个最后 $Q$ 项已经足够”的一般高阶断言。此处成立的原因是完整第二连接恰零；第四及以后必须加入新产生的第三连接像。

## 5. 全高层校正的精确消元

目标 normal 次数不超过二的非纯校正共有

$$
135+450=585
\tag{5.1}
$$

个；normal 次数三至五共有

$$
990+1485+1287=3762.
\tag{5.2}
$$

由于 $M_0$ 的原式至少含一个 normal 变量，前 $585$ 个校正只作用于前 $1088=170+918$ 个来源行。后三个 normal 层则可能作用于全部高来源行。

完整第六页已保存全部高行系统的九维核参数，含七个实际 forcing 参数。其零 forcing 纤维恰为二维。令

$$
N_{\mathrm h}:\mathbb Q^2\longrightarrow\mathbb Q^{3762}
\tag{5.3}
$$

为该完整高齐次核；它不是任意挑选的两个高列。已付完整核维数和原七参数投影秩，连同本次全部 $5100$ 高行乘回，证明它参数化所有满足高行零条件的高校正。

令 $J_0$ 是前 $585$ 个 $M_0$ 校正的低行矩阵，令

$$
B=[\,J_0,\ M_1Q\,]\in\mathbb Q^{1088\times592},
\qquad
C_{\mathrm h}=(M_0N_{\mathrm h})_{\mathrm{low}}.
\tag{5.4}
$$

已付 $\operatorname{rank}B=582$。本次真实检查

$$
\operatorname{rank}[B,C_{\mathrm h}]=584.
\tag{5.5}
$$

纯常数校正被 $M_0$ 杀掉，纯常数头也被 $M_1$ 杀掉；因此 (5.4) 加 $C_{\mathrm h}$ 已保留 (4.4) 的全部有效校正，未删任何高 normal nuisance。

前十三个二阶头的原第三 forcing 组成

$$
R_3\in\mathbb Q^{6188\times13}.
\tag{5.6}
$$

本次对其高 $5100$ 行逐项核实为零；低 $1088$ 行与旧第三计算的全部十三列 SHA 一致。故完整第三连接被准确归约为

$$
\mathcal M_3=[\,B,\ C_{\mathrm h},\ (R_3)_{\mathrm{low}}\,]
\in\mathbb Q^{1088\times607}.
\tag{5.7}
$$

这保留 $585+3762=4347$ 个非纯目标校正的完整效果，也保留全部原来源；没有从低支持包络猜测高层不会改秩。

## 6. 实际精确秩、完整第三像与真实 lift

实际有理运算给出

$$
\operatorname{rank}\mathcal M_3=585,\qquad
\dim\ker\mathcal M_3=22.
\tag{6.1}
$$

将完整核投影到最后十三个 leading 参数，实际秩为 $12$，核的零 leading 纤维恰为 $10$ 维。leading 像在原十三头规范中的矩阵是

$$
\begin{pmatrix}I_{12}\\0\end{pmatrix}.
\tag{6.2}
$$

由 (5.5)，

$$
\operatorname{rank}\beta_{3,0}
=
585-584
=
13-12
=
1.
\tag{6.3}
$$

若把前十三个二阶头依次记为 $\xi_1,\ldots,\xi_{13}$，其中前十个纯头、后三个规范横向头，则第三连接像的准确描述是

$$
\beta_{3,0}(\xi_i)=0\quad(1\le i\le12),\qquad
\beta_{3,0}(\xi_{13})=[R_3e_{13}]\ne0.
\tag{6.4}
$$

再加十个 exact 纯头，完整第三头空间为

$$
K_3=\operatorname{span}\{\xi_1,\ldots,\xi_{12},
\text{十个 exact 纯头}\},
\qquad \dim K_3=22.
\tag{6.5}
$$

完整核向量含低 $585$ 列、最后常核 $Q$ 参数、高齐次参数和原十三个 leading 参数。源码将它们全部回填到 $\lambda_0,\lambda_1,\lambda_2,\lambda_3$，并核验了 (1.3) 的全部原式坐标。最终 cochain 矩阵为 $5222\times22$。

实际数学运行是 43702348535 / zero-complete-third-reused-full-high，执行来源提交为 184af0401948bd700ddc3dc2b202664a01454d5f，数学耗时约 $14.8815$ 秒。源码 SHA256 为

180b7f6c3a4d3c9ff560b9f9e4a590af04d00996abcba75cfeb35c1778272156。

原始小回执为 $55170$ 字节，SHA256 为

888722752a83224c2043b8a2fd2ec4f833bf4adb7f628f151ab246b9774a6607。

主要逻辑身份如下：

| 对象 | 尺寸 | 逻辑 SHA256 |
|---|---:|---|
| 全部第三 forcing | $6188\times13$ | e27d231666aeb1a0859fb03f92f5e8e4b747035621cbac5ee6e356597f1da99b |
| 完整低核 | $607\times22$ | 7f4fe6833b217f78b3ff6fe2981656bf6a51959a3cb723666e570c4c84385af1 |
| 全部原行 Schur | $1088\times15$ | 773b815d940481f69e27e0ce0fd1258d6800afe9641fb5d84a76aa241344a368 |
| 完整第三 cochain | $5222\times22$ | f43c25348aaff1fafa085d5b8a3d9b93875d8029c3674f6e011823954c763077 |

完整 cochain 和全部核留在同一 job 临时检查点；不把可重算大矩阵提交 Git 或上传 Release。源码、参数、运行来源和小回执明确指定恢复过程。

## 7. Smith 含义、已付界与目标范围

原完整矩阵有 $14$ 个在 $s=0$ 为正的 Smith 指数，另有 $13$ 维泛左核。由 (1.1)–(1.2)，前三级的准确分布为

$$
\#\{a_i=1\}=4,\qquad
\#\{a_i=2\}=0,\qquad
\#\{a_i=3\}=1,
\tag{7.1}
$$

其余九个正指数至少为四。

这与此前仅给第三秩至多一时的公共阶下界相同。因此本文保持 (1.4)、最大正指数已付区间 $9\le a_{\max}\le17$，以及既有 $K_{104}$ 费用层不变，不把准确连接收口重复登记成新的阶数收益。

对原九个平方目标，在真实共动坐标中为 $n_j^2$，$j=2,\ldots,10$。本次全部 $\lambda_0,\ldots,\lambda_3$ 的九行平方读数均精确为零。这只说明所构造完整第三左 jet 不给这些读数上的局部障碍；不等于多项式成员性，也不排更高阶或其他局部泛函的障碍。

## 8. 下一完整第四连接的合法 incoming

设 $T_2(v)$ 是本文保存的全部二阶 cochain。任意同第三头的两条第三 cochain 之差，可以逐阶写成

$$
s\,T_2(v)+s^2T_1(w)+s^3k
\quad\pmod{s^4},
\tag{8.1}
$$

其中 $v\in K_2$、$w\in K_1$、$k\in K_0$。故第四 forcing 的完整旧像是

$$
W_3=\operatorname{im}M_0+M_1K_0+R_3(K_2).
\tag{8.2}
$$

这里 $R_2(K_1)$ 已由完整 $\beta_{2,0}=0$ 吸收进 $W_1$。若在第四求解中使用系数 $y$ 消去 $R_3y$，必须同步加入

$$
\lambda_1\leftarrow\lambda_1+T_{2,0}y,\quad
\lambda_2\leftarrow\lambda_2+T_{2,1}y,\quad
\lambda_3\leftarrow\lambda_3+T_{2,2}y.
\tag{8.3}
$$

这些是真实 cochain 的整体运输；不能只改最后 $Q$ 项。本文保存的全部二阶与三阶 cochain 正是下一完整第四页的来源接口。
