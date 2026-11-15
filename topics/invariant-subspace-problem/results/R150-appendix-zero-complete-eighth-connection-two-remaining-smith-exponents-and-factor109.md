# R150：零点完整第八连接恰一、两剩余 Smith 指数与 $K_{109}$

2026-11-15；Astra-ISP-789f / literature_audit；AI 辅助：GPT-6 Astra Pro。

## 1. 实际结论

原自然参数 $s=0$、原十七式及全部 $6188$ 个原来源的完整第八连接满足

$$
\operatorname{rank}_{\mathbb Q}\beta_{8,0}=1,\qquad
\dim K_8=15.
\tag{1.1}
$$

完整前八级连接秩为

$$
(4,0,1,3,1,1,1,1).
\tag{1.2}
$$

因此

$$
\delta_{4354,0}\ge63,\qquad
\delta_{4353,0}\ge54,\qquad
K_{109},\qquad
9\le a_{\max,0}\le12.
\tag{1.3}
$$

配当前同选定子式的无穷远阶 $130/125/125$，在原成员性成立的前提下，统一来源费用为 $8580$，目标分支为 $172$。

原九目标配对方面，本次全部 $\lambda_0,\ldots,\lambda_7$ 的九平方读数为零；$\lambda_8$ 有非零读数。第七读数在完整 $K_8$ 上的代表不变性已由前稿证明，所以本次的零值具有完整范围，不能把前一页代表的原始非零第七读数移到本页。

主要来源：

- [完整第七连接、$K_{108}$ 及平方读数不变性](R150-appendix-zero-complete-seventh-connection-factor108-and-invariant-first-square-map.md)；
- [通用完整高阶源码](../notes/2026-11-15-r150-zero-complete-higher-full-incoming-789f.py)；
- [本次实际回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-complete-eighth-full-incoming.json)；
- [同选定子式无穷远阶 $130/125/125$](R150-appendix-seventeen-source-fourth-pairing-rank-one-sixteen-heads-and-cost8585.md)；
- [完整模 $31$ 仿射公因子及总长上界](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)。

## 2. 全部旧像及原高低行

记准确共动原左方程为

$$
M(s)=A_{\mathrm{new}}(s)^{\mathsf T}=\sum_{j\ge0}s^jM_j.
\tag{2.1}
$$

全部原来源运输及目标变换转置保持。令 $T_j$ 为完整真实 $j$ 阶 cochain 族，$R_j$ 为其前一阶族的第 $j$ 阶 forcing。完整第二连接为零后，第八页的全部旧像为

$$
W_7=\operatorname{im}M_0+M_1K_0+
\sum_{j=3}^7R_j(K_{j-1}).
\tag{2.2}
$$

同头代表差按 $s^{8-j}T_{j-1}$ 逐项运输，所以每个 $R_j$ 参数都须回填该整条 cochain，而非仅最后的常核项。

完整第七 $16$ 头包含十个对全部参数 exact 的纯头和六个非 exact 头。本次直接构造后者的原第八 forcing

$$
R_8=\sum_{j=1}^8M_j\lambda_{8-j}
\in\mathbb Q^{6188\times6}.
\tag{2.3}
$$

本次实际核验其全部 $5100$ 个高来源行均为零。完整高常数校正仍由既已证明的

$$
N_{\mathrm h}:\mathbb Q^2\longrightarrow\mathbb Q^{3762}
\tag{2.4}
$$

参数化。令低常数块 $B=[J_0,M_1Q]$，其尺寸为 $1088\times592$、秩为 $582$，并记 $C_{\mathrm h}=(M_0N_{\mathrm h})_{\mathrm{low}}$。

本次完整低矩阵为

$$
\mathcal M_8=
[B,C_{\mathrm h},R_{3,\mathrm{low}},\ldots,R_{8,\mathrm{low}}]
\in\mathbb Q^{1088\times649}.
\tag{2.5}
$$

列数为 $592+2+13+12+9+8+7+6=649$。旧完整 incoming 秩为 $591$；实际计算给出

$$
\operatorname{rank}\mathcal M_8=592,\qquad
\dim\ker\mathcal M_8=57.
\tag{2.6}
$$

核向最后六个 leading 参数的投影为五维，零 leading 纤维为

$$
57-5=52=643-591.
\tag{2.7}
$$

所以

$$
\operatorname{rank}\beta_{8,0}=592-591=6-5=1,\qquad
\dim K_8=10+5=15.
\tag{2.8}
$$

全部旧像、高常数校正及完整输入头均已保留，故这是完整连接的精确值。

## 3. 原 cochain 验证

回填时，对每个 $3\le j\le7$ 加入完整多项式

$$
s^{8-j}T_{j-1}y_j.
\tag{3.1}
$$

最后的 $Q$ 校正置于 $\lambda_7$，全部新常数校正置于 $\lambda_8$。程序保留所有纯切向、一次及更高 normal 块。

本次原样复用五十一列已付实际单位解，仅新增六列单列 Dixon 求解，并核验全部低行 Schur。重建的十五条 cochain 形成 $27057\times15$ 临时矩阵；全部零至八阶原式乘回，共

$$
9\cdot6188\cdot15=835380
\tag{3.2}
$$

个有理产品坐标均为零。

## 4. 两剩余正指数及公共因子

由 (1.2)，十四个正 Smith 指数中的十二个已经精确确定为

$$
1,1,1,1,3,4,4,4,5,6,7,8.
\tag{4.1}
$$

它们的和为 $45$。另外两个指数记为 $b\le c$，则

$$
9\le b\le c.
\tag{4.2}
$$

既有特征零总阶上界 $66$ 进一步给出

$$
b+c\le21.
\tag{4.3}
$$

所以仅余以下六种可能：

$$
(b,c)\in
\{(9,9),(9,10),(9,11),(9,12),(10,10),(10,11)\}.
\tag{4.4}
$$

这些是由已证连接及总长度得到的可能范围，不预填后续秩。由此

$$
\delta_{4354,0}=45+b+c\ge63,\qquad
\delta_{4353,0}=45+b\in\{54,55\},
\tag{4.5}
$$

且 $9\le c\le12$。

保留其他有限点因子，

$$
\begin{aligned}
K_{109}
&=sK_{108}=s^{49}K_{60}\\
&=s^{63}(s-2)^9(s+6)^9F_+(s)^2F_-(s)^2E_8(s)^2.
\end{aligned}
\tag{4.6}
$$

其次数为 $109$，首项系数为 $5^6$。

## 5. 条件来源费用

保持同选定子式的无穷远阶 $130/125/125$。设 $q=D/K_{109}$，由完整模 $31$ 所选子式次数 $8527$ 与原齐次次数 $8770$，

$$
8418=8527-109\le\deg q
\le8770-130-109=8531.
\tag{5.1}
$$

原来源降度的三支费用为

$$
\begin{aligned}
\text{非基来源}&\le8531-1+45=8575,\\
\text{基来源转移}&\le8770+55-125-109-11=8580,\\
\text{目标分支}&\le8770+64-125-109-10-8418=172.
\end{aligned}
\tag{5.2}
$$

因此在原 $h_0t_\nu$ 的 $\mathbb Q[s]$ 成员性成立的前提下，完整来源费用可取 $8580$。成员性仍未由这些次数界证明。

## 6. 原目标读数与代表范围

原九目标在准确共动坐标中为 $n_j^2$，$j=2,\ldots,10$。本次全部十五条真实 cochain 的 $\lambda_0,\ldots,\lambda_7$ 九平方读数均为零，每个 $9\times15$ 块的逻辑 SHA256 为

9985902de39ff67fb9a99762640bef9e7ec0b18ce2e567c211f8e7aee6e1f76b。

前稿已证明第六读数在完整 $K_6$ 上与代表无关，且其核恰为 $K_7$。若两条八阶 cochain 有同一个头，则它们的差除以 $s$ 是七阶 cochain，其第六读数为零。因此本次第七读数在完整 $K_8$ 上与代表无关，而实际值全零。

由截断与这一同头论证，任意真实十阶 cochain 的零至七阶九平方读数均为零。原 $h_0$ 在零点恰有三阶零点，故这些读数不能形成 $h_0t_j$ 的模 $s^{11}$ 障碍。这是由已经完整核验的低阶信息得到的范围结论，不要求预先构造十阶 cochain。

本次 $\lambda_8$ 的首个非零读数是目标 $j=2$、零基 headColumn $1$：

$$
\frac{
313642452561212784993210751263389279882343
}{
9442075040159421726339056287856000000
}\ne0.
\tag{6.1}
$$

其矩阵逻辑 SHA256 为

650e9b3bd5e9b77231d97cfb587d93aafeee4eda5091542d8588fabb91873665。

该第八读数目前只对应实际输出代表，不能直接当作完整 $K_8$ 上的同头不变量；下一页仍需保留全部 cochain 修正并读取真实原目标。

## 7. 实际证据

- run：43702348535；
- step：zero-complete-eighth-full-incoming；
- 执行来源提交：27067e0c0130ef5b1d208e3acad360a09bae52e4；
- 数学耗时：约 $33.8995$ 秒；
- 源码 SHA256：9bf405d3aa65d40a8ebeb3fc87f3e8bd686814db371657abe9794f92e59099b8；
- 原始小回执：$70304$ 字节，SHA256 为 cd4e9ff1278cd4e37b73e8bfb474d6ae66d8f7c8ac05eddca4540e73aabe553b；
- 主线外回执：$78445$ 字节，SHA256 为 255c2e155710e3d432d5a4660380679c05817259e676c4bf25d5d5e7c6e5e9b9。

| 对象 | 尺寸 | 逻辑 SHA256 |
|---|---:|---|
| 原第八 forcing | $6188\times6$ | f9db75e1faecee29be5cc05a0eb8fef7fcb0f3f378989effd3c813719244e9ba |
| 全原低行 Schur | $1088\times57$ | 144d8e51459a4fbc3cd756d470dc37dc05155f3b833c5e1d19882e225a2d10be |
| 完整低核 | $649\times57$ | dc47d8e5c101087a15240ec175593d088a8bbb1b945a45242de2b0b3d4a7595a |
| 全部十五条第八 cochain | $27057\times15$ | 1bb19f3265948b31b7d4aa641027ceae82fdbd0252bdeb8091bf6700b8a65fff |
| 原第八 leading 投影 | $16\times15$ | 1fa44eca140172ff53ef3c55e11fb0bf116ee13139271966c20e9fce221f022e |

检查点 binding 为 ae6fab6a85c2ddcfebffafa7545abfa3a20eafd4f5876f89677d22c8603bf78b；manifest 为 $27891$ 字节，SHA256 为 3936dd090a5c4500fc997a8ccf4fef3188ab49ce6228026be5ebefb4a8bc525d。完整数组仅保留于同 run 临时工作区。

下一完整第九页保留 $W_8=W_7+R_8(K_7)$，复用五十七列旧实际 RHS，仅新增五个非 exact 第九 forcing。其新低矩阵有 $654$ 列，旧 incoming 秩 $592$，零 leading 纤维维数为 $57$。后续精确连接与平方读数均以新的原全来源核验为准。
