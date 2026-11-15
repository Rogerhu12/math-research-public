# R150：零点完整第四连接恰三及十九维真实第四左头

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / literature_audit；AI-assisted，GPT-6 Astra Pro。

## 1. 新结论

在原自然参数 $s=0$、原十七式和全部 $6188$ 个原次数不超过三的来源上，本次实际有理运算证明

$$
\operatorname{rank}_{\mathbb Q}\beta_{4,0}=3,\qquad
\dim K_4=19.
\tag{1.1}
$$

其中 $K_4$ 是完整第四左头空间，而非固定三阶代表只允许最后一次常核校正后所得的子空间。已付完整前三级秩为

$$
(\operatorname{rank}\beta_{1,0},
 \operatorname{rank}\beta_{2,0},
 \operatorname{rank}\beta_{3,0})=(4,0,1).
\tag{1.2}
$$

本次使用完整 $22$ 维第三头，保留完整第三连接像作为第四页的 incoming，并将其参数同步回填到第一、第二、第三阶系数。全部 $19$ 条输出 cochain 逐阶核验原式，共

$$
5\cdot6188\cdot19=587860
\tag{1.3}
$$

个原有理乘回坐标。

本次收口准确连接，不提高原有

$$
\delta_{4354,0}\ge58,\qquad
\delta_{4353,0}\ge49,\qquad
K_{104}.
\tag{1.4}
$$

主要来源：

- [完整第三连接恰一](R150-appendix-zero-complete-third-connection-exact-one-and-twentytwo-heads.md)；
- [本次完整第四源码](../notes/2026-11-15-r150-zero-complete-fourth-full-incoming-789f.py)；
- [本次实际回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-complete-fourth-full-incoming.json)；
- [第八页的既有公共阶与 $K_{104}$](R150-appendix-zero-fourteen-eighth-left-jets-factor104-and-cost8600.md)。

## 2. 原左方程与完整旧像

沿完整第三稿的原共动坐标，记

$$
M(s)=A_{\mathrm{new}}(s)^{\mathsf T}
=\sum_{j\ge0}s^jM_j.
\tag{2.1}
$$

原目标与来源的可逆运输均保留，回到原目标左泛函时用目标变换的转置。第 $k$ 阶 cochain 满足

$$
\sum_{j=0}^{\ell}M_j\lambda_{\ell-j}=0,
\qquad 0\le\ell\le k.
\tag{2.2}
$$

已付完整二阶代表 $T_2(v)$ 覆盖整个 $K_2$，其维数为 $23$。已付完整第三代表 $T_3(w)$ 覆盖整个 $K_3$，其维数为 $22$。其中各有同一十个对全部参数精确的纯头；其 forcing 恒零，可以保留在输出而不作为非齐次 RHS 重算。

令 $R_j$ 是相应真实 $(j-1)$ 阶 cochain 的第 $j$ 阶 forcing。对同一个第三头，任意两组第三 cochain 的差都可逐阶分解为

$$
s\,T_2(v)+s^2T_1(u)+s^3k
\pmod {s^4},
\tag{2.3}
$$

其中 $v\in K_2$、$u\in K_1$、$k\in K_0$。于是第四 forcing 的全部代表差属于

$$
\operatorname{im}M_0+R_3(K_2)+R_2(K_1)+M_1K_0.
\tag{2.4}
$$

完整 $\beta_{2,0}=0$ 已证明

$$
R_2(K_1)\subset
W_1:=\operatorname{im}M_0+M_1K_0.
\tag{2.5}
$$

因此完整第四连接的值域商是

$$
W_3=\operatorname{im}M_0+M_1K_0+R_3(K_2).
\tag{2.6}
$$

这一步把全部早期 cochain 自由量纳入了完整低页像。只使用最后的 $M_1Q$，会漏掉实际非零的一维第三连接像。

## 3. 全来源高低消元

与完整第三页相同，全部原来源按 normal 次数分为

$$
170+918+2295+2805=6188
\tag{3.1}
$$

行。非纯目标校正分为低 $585=135+450$ 个坐标与高 $3762=990+1485+1287$ 个坐标。

已付完整高齐次核

$$
N_{\mathrm h}:\mathbb Q^2\longrightarrow\mathbb Q^{3762}
\tag{3.2}
$$

参数化全部满足 $5100$ 个高来源行为零的高校正。它来自完整高行系统的零 forcing 纤维，包含全部四、五 normal 层与三 normal 层的共同消元。

低矩阵仍为

$$
B=[J_0,M_1Q]\in\mathbb Q^{1088\times592},
\qquad
C_{\mathrm h}=(M_0N_{\mathrm h})_{\mathrm{low}}.
\tag{3.3}
$$

完整第三结果已付

$$
\operatorname{rank}[B,C_{\mathrm h}]=584,
\qquad
\operatorname{rank}[B,C_{\mathrm h},R_{3,\mathrm{low}}]=585.
\tag{3.4}
$$

这里 $R_3$ 保留原十三个非 exact 二阶头的全部原 forcing 列，未因其商像只有一维而删去真实 cochain 来源。

本次从完整第三 $22$ 头中取十二个非 exact 头的真实 $\lambda_0,\ldots,\lambda_3$，直接计算

$$
R_4=M_4\lambda_0+M_3\lambda_1+M_2\lambda_2+M_1\lambda_3
\in\mathbb Q^{6188\times12}.
\tag{3.5}
$$

其 $5100$ 个高来源行在本次实际逐项检查中为零；这不是沿用旧代表族的支持假设。因此完整第四方程归约为

$$
\mathcal M_4=
[B,\ C_{\mathrm h},\ R_{3,\mathrm{low}},\ R_{4,\mathrm{low}}]
\in\mathbb Q^{1088\times619}.
\tag{3.6}
$$

高层全部由 (3.2) 保留，低层则含全部原行。旧十五列单位解原样复用，只对十二个新实际 RHS 作 $582$ 阶单位求解；未重复完整逆、原大 RREF 或旧高行消元。

## 4. 精确秩与完整十九头

实际完整原行 Schur 给出

$$
\operatorname{rank}\mathcal M_4=588,\qquad
\dim\ker\mathcal M_4=619-588=31.
\tag{4.1}
$$

核向最后十二个新 leading 参数的投影维数为 $9$，其归一化零 leading 纤维维数为 $22$。因此

$$
\operatorname{rank}\beta_{4,0}
=
588-585
=
12-9
=
3.
\tag{4.2}
$$

加上十个 exact 纯头，

$$
\dim K_4=9+10=19.
\tag{4.3}
$$

(2.6) 已保全部旧像，(3.2) 已保全部高常数校正，原第三代表又覆盖整个 $K_3$。故 (4.2) 同时给完整下界与上界，不只是某个有限支持包络的秩。

## 5. 第三像参数的真实 cochain 回填

完整核中的未知量分别记为低校正 $x$、最后常核参数 $b$、高齐次参数 $a$、第三 forcing 参数 $y\in\mathbb Q^{13}$ 和新的 leading 参数 $z\in\mathbb Q^{12}$。

除将原第三 cochain 整体乘 $z$ 外，还必须加入

$$
\begin{aligned}
\lambda_1&\leftarrow\lambda_1+T_{2,0}y,\\
\lambda_2&\leftarrow\lambda_2+T_{2,1}y,\\
\lambda_3&\leftarrow\lambda_3+T_{2,2}y+Qb,\\
\lambda_4&=(x,N_{\mathrm h}a).
\end{aligned}
\tag{5.1}
$$

因为 $T_2$ 本身是完整真实二阶 cochain，$sT_2y$ 在零至三阶不改变原式零身份，并在第四阶贡献恰为 $R_3y$。其中 $\lambda_1$ 可出现新的纯切向块；本次完整保存了该块，没有把它删成一次 normal 项。

回填后的全部十九条 cochain 形成 $9589\times19$ 临时矩阵。程序重新核验全部零至四阶原方程，而非只核低 Schur。计数正是 (1.3)。

## 6. 实际证据与可恢复身份

实际运行：

- run：43702348535；job：132776011109；
- step：zero-complete-fourth-full-incoming；
- 执行来源提交：e3e8a96665af1638bbf6be05be639b4f889103d1；
- 数学耗时：约 $13.6265$ 秒；
- 源码 SHA256：18e21310a161b3fca3b61df8d263e549e1230a4c8ef90c971c8c4b00082c0642；
- 原始小回执：$63661$ 字节，SHA256 为 3c2b754618e2e90d487ca48873e27354487640158426c3c024694c4ec124decf。

主要逻辑身份：

| 对象 | 尺寸 | 逻辑 SHA256 |
|---|---:|---|
| 全部新原第四 forcing | $6188\times12$ | 89ad055b123e525840b1dfffe50001f24439c1d716089c07df6df05fd67c3a47 |
| 全部原行 Schur | $1088\times27$ | 25658e74b1f89e873e62432ce771bac57f12b25e5a8b5a8dae61ed7c349e1a68 |
| 完整低核 | $619\times31$ | 52edba0dc80b7bf56e5e966a9b24bf462b687628cda1f89903176fd268066a17 |
| 全部十九条第四 cochain | $9589\times19$ | 01f7a4b9f5810384e38953b64bfe8843e48529c6197ac1f49db5bf544a367c85 |

完整 cochain、原 RHS 和单位解仅保留在同 job 临时检查点。Git 记录源码、参数、运行身份和小回执，不上传可重算大数组。

## 7. Smith 指数及目标读数的准确范围

由完整前四级连接，

$$
\#\{a_i=1\}=4,\qquad
\#\{a_i=2\}=0,\qquad
\#\{a_i=3\}=1,\qquad
\#\{a_i=4\}=3.
\tag{7.1}
$$

其余六个正 Smith 指数至少为五。原第四包络已给累计前四级至多八，所以本次恰三没有改变已付公共阶下界；(1.4) 保持不变。

原九个平方目标在真实共动坐标中是 $n_j^2$，$j=2,\ldots,10$。十九条输出的全部 $\lambda_0,\ldots,\lambda_4$ 九行平方读数仍精确为零。该结论仅涉及这些真实左 jet 的目标配对，不证明原多项式成员性。

## 8. 下一完整第五页的来源接口

若 $T_3$ 是完整第三 cochain 族，同第四头的代表差可由

$$
sT_3(K_3)+s^2T_2(K_2)+s^3T_1(K_1)+s^4K_0
\tag{8.1}
$$

逐阶参数化。完整第五页的旧像为

$$
W_4=\operatorname{im}M_0+M_1K_0+R_3(K_2)+R_4(K_3).
\tag{8.2}
$$

$R_2(K_1)$ 仍由完整第二连接为零吸收。新 $R_4$ 参数需按 $sT_3$ 同步回填第一至第四阶；旧 $R_3$ 参数需按 $s^2T_2$ 同步回填第二至第四阶。下一页必须保留这两组实际来源，而不能回到仅最后 $Q$ 校正的固定代表计算。
