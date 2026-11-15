# R150：零点完整第七连接恰一、$K_{108}$ 与第六平方读数的准确消失

2026-11-15；Astra-ISP-789f / literature_audit；AI 辅助：GPT-6 Astra Pro。

## 1. 本次结论

对原自然参数 $s=0$、原十七式与全部 $6188$ 个原来源，本次实际有理运算证明

$$
\operatorname{rank}_{\mathbb Q}\beta_{7,0}=1,\qquad
\dim K_7=16.
\tag{1.1}
$$

完整前七级连接秩为

$$
(4,0,1,3,1,1,1).
\tag{1.2}
$$

所得公共阶、公共因子和最大正 Smith 指数范围为

$$
\delta_{4354,0}\ge62,\qquad
\delta_{4353,0}\ge53,\qquad
K_{108},\qquad
9\le a_{\max,0}\le13.
\tag{1.3}
$$

配当前同选定子式无穷远阶 $130/125/125$，条件来源费用降至 $8581$，目标分支仍为 $172$。

本次配对还有准确的范围收口：第六页出现的非零平方读数定义了完整 $K_6$ 上的一个秩一映射，其核恰为本次 $K_7$。故该第六读数不可能在第九头上给原 $h_0t_j$ 的模 $s^{10}$ 障碍。本次第七系数又有非零读数，但它在 $K_7$ 上尚不能直接宣称与同头代表无关。

主要来源：

- [完整第六连接、$K_{107}$ 及首个平方读数](R150-appendix-zero-complete-sixth-connection-exact-one-factor107-and-first-square-readout.md)；
- [完整第五连接及其全部 incoming](R150-appendix-zero-complete-fifth-connection-exact-one-factor105-and-cost8584.md)；
- [通用完整高阶源码](../notes/2026-11-15-r150-zero-complete-higher-full-incoming-789f.py)；
- [本次实际回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-complete-seventh-full-incoming.json)；
- [同选定子式无穷远阶 $130/125/125$](R150-appendix-seventeen-source-fourth-pairing-rank-one-sixteen-heads-and-cost8585.md)。

## 2. 完整旧像与全部原行

沿原准确共动坐标写

$$
M(s)=A_{\mathrm{new}}(s)^{\mathsf T}=\sum_{j\ge0}s^jM_j.
\tag{2.1}
$$

原目标与来源的可逆变换均被保留，原左泛函按目标变换的转置恢复。记 $T_j$ 为完整真实 $j$ 阶 cochain 族，$R_j$ 为 $T_{j-1}$ 的第 $j$ 阶 forcing。

同一个六阶头的全部代表差，可由

$$
sT_5(K_5)+s^2T_4(K_4)+s^3T_3(K_3)+
s^4T_2(K_2)+s^5T_1(K_1)+s^6K_0
\tag{2.2}
$$

逐阶表示。完整第二连接为零吸收 $R_2(K_1)$，故第七页的全部旧像为

$$
W_6=\operatorname{im}M_0+M_1K_0+
R_3(K_2)+R_4(K_3)+R_5(K_4)+R_6(K_5).
\tag{2.3}
$$

低常数块

$$
B=[J_0,M_1Q]\in\mathbb Q^{1088\times592}
\tag{2.4}
$$

的秩为 $582$。全部 $5100$ 个高来源行的完整齐次解由已付

$$
N_{\mathrm h}:\mathbb Q^2\longrightarrow\mathbb Q^{3762}
\tag{2.5}
$$

参数化，记 $C_{\mathrm h}=(M_0N_{\mathrm h})_{\mathrm{low}}$。

本次从完整 $17$ 维 $K_6$ 的七个非 exact 头构造

$$
R_7=\sum_{j=1}^7 M_j\lambda_{7-j}
\in\mathbb Q^{6188\times7}.
\tag{2.6}
$$

十个 exact 纯头保留在输出，其 forcing 恒零。本次 $R_7$ 的全部 $5100$ 个高来源行实际为零，故没有新增非齐次高解假设。保留所有高齐次方向后，完整低矩阵为

$$
\mathcal M_7=
[B,C_{\mathrm h},R_{3,\mathrm{low}},R_{4,\mathrm{low}},
R_{5,\mathrm{low}},R_{6,\mathrm{low}},R_{7,\mathrm{low}}]
\in\mathbb Q^{1088\times643}.
\tag{2.7}
$$

其列数为 $592+2+13+12+9+8+7=643$。旧 incoming 的低秩为 $590$，实际新秩为

$$
\operatorname{rank}\mathcal M_7=591,\qquad
\dim\ker\mathcal M_7=52.
\tag{2.8}
$$

核的七维新 leading 坐标投影为六维，零 leading 纤维为

$$
52-6=46=636-590.
\tag{2.9}
$$

所以完整第七连接秩为 $591-590=7-6=1$，输出完整头数为 $10+6=16$。

## 3. 真实 cochain 的完整回填

对旧 $R_3,R_4,R_5,R_6$ 参数，必须分别加入

$$
s^4T_2y_3+s^3T_3y_4+s^2T_4y_5+sT_5y_6.
\tag{3.1}
$$

全部系数随各多项式整体回填；最后再加入 $\lambda_6$ 的 $Qb$ 校正和全部 $\lambda_7=(x,N_{\mathrm h}a)$。特别是纯切向块和较早 normal 块均保持，不只修改最后一次系数。

程序复用四十四列已核实际 RHS 解，仅新增七列单位求解。重建后的十六条完整 cochain 形成 $22690\times16$ 临时矩阵，并重新核验原零至七阶的全部来源：

$$
8\cdot6188\cdot16=792064
\tag{3.2}
$$

个有理产品坐标均为零。完整旧像 (2.3)、完整高齐次核 (2.5) 及完整输入头共同保证本次得到精确连接，而非固定代表包络。

## 4. Smith 阶及条件来源次数

令 $c_j=\#\{a_i\le j\}$，其中 $a_i$ 是原零点十四个正 Smith 指数。完整连接给

$$
(c_1,\ldots,c_7)=(4,4,5,8,9,10,11).
\tag{4.1}
$$

已付真实第八头仍给 $c_8\le13$，故

$$
\begin{aligned}
\delta_{4354,0}
&\ge14+10+10+9+6+5+4+3+1=62,\\
\delta_{4353,0}
&\ge13+9+9+8+5+4+3+2=53.
\end{aligned}
\tag{4.2}
$$

特征零总阶上界 $66$ 与原第八头给出

$$
9\le a_{\max,0}\le66-53=13.
\tag{4.3}
$$

保留其他有限点的公共因子，

$$
\begin{aligned}
K_{108}
&=sK_{107}=s^{48}K_{60}\\
&=s^{62}(s-2)^9(s+6)^9F_+(s)^2F_-(s)^2E_8(s)^2.
\end{aligned}
\tag{4.4}
$$

其次数为 $108$，首项系数为 $5^6$。配合同选定子式无穷远阶 $130/125/125$，令 $q=D/K_{108}$，得到

$$
8419=8527-108\le\deg q
\le8770-130-108=8532.
\tag{4.5}
$$

三支来源费用为

$$
\begin{aligned}
\text{非基来源}&\le8532-1+45=8576,\\
\text{基来源转移}&\le8770+55-125-108-11=8581,\\
\text{目标分支}&\le8770+64-125-108-10-8419=172.
\end{aligned}
\tag{4.6}
$$

统一费用 $8581$ 仍以原 $h_0t_\nu$ 的 $\mathbb Q[s]$ 成员性成立为前提。

## 5. 首个平方读数的同头不变性

本节核对完整 $K_0,\ldots,K_5$，而不只核后续保留下来的某个代表子族。记 $e_j(\lambda)=\lambda(n_j^2)$，$j=2,\ldots,10$。

1. $K_0$ 由二十个纯坐标与七个一次 normal 常核组成，故全部 $e_j$ 在 $K_0$ 上为零。完整 $\beta_{2,0}=0$ 给 $K_1=K_2$；使用完整二阶族的一阶截断可覆盖整个 $K_1$，其一阶系数只有一次 normal 块。
2. 完整 $K_2$ 有二十三个头。二十个纯头的二阶校正只有一次 normal 块。三个横向头的完整二阶校正与原规范矩阵 SHA256 a0a1c8d76f023c8d251b2c755f15afccf7798ef2359bed6e833d7d42e4cc5c8d 一致；[原目标配对回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-fifth-original-target-pairing.json) 已逐项核验它们的 $9\times3$ 二阶平方读数全零，逻辑 SHA256 为 bbc4d48ba43feb38f601eccea7cc8bba168f7c3f844630694f2d4cb08353243d。完整第三入口的 restore_second 正是逐 SHA 恢复这些列，并核验全部二十三条原二阶 cochain，故没有漏掉第三个横向头。
3. 完整第三、第四、第五实际回执分别核验其全部 $22,19,18$ 条 cochain 的最高平方读数为零；对应 $9\times22,9\times19,9\times18$ 逻辑 SHA256 分别为 66e34a91ce8be0518f921bc57e1218224053c4e8f84f6653aebe3864502e8d72、a7e5317674bf60da5a3717fdbbae12153e428537a4d3c01cda4f658d9ced8364、8ff26d072c0b6878ea76c513174ceaa5061db500d1a4c482bc398da69e08fe58。

这些基族证据可升级为对所有低阶代表的陈述。设 $0\le r\le5$，且 $\lambda(s)$ 是任意真实 $r$ 阶 cochain。取同头的已付完整代表 $T_r$，则

$$
\lambda(s)-T_r(s)=s\,\eta(s)\pmod{s^{r+1}},
\qquad M(s)\eta(s)=O(s^r).
$$

由 $r=0$ 开始归纳，$\eta$ 的第 $r-1$ 系数平方读数为零；而 $T_r$ 的第 $r$ 系数读数已经实际核验为零。因此所有 $r\le5$ 的真实 cochain 最高系数均杀掉九个平方。截断后，同样适用于每个较低系数。

现在若两条六阶 cochain 有同一个头，则其差除以 $s$ 是五阶 cochain，故二者第六系数的九平方读数相同。于是

$$
\mathcal E_6:K_6\longrightarrow\mathbb Q^9,\qquad
\mathcal E_6(v)=
\bigl(\lambda_6(n_j^2)\bigr)_{j=2}^{10}
$$

是定义在完整第六头空间上的线性映射，与代表选择无关。任何更高完整头空间 $K_k\subset K_6$ 上的实际第六读数严格等于 $\mathcal E_6|_{K_k}$。后续仍须实际核验这些头的存活及对应 leading 投影，不能把某个第六头假定为可升。

原 $h_0$ 在零点恰为三阶，$[s^3]h_0=-917294284800$。因此若存在实际 $v\in K_9$ 使 $\mathcal E_6(v)\ne0$，其真实九阶左 cochain 对相应 $h_0t_j$ 的 $s^9$ 配对系数为

$$
-917294284800\,\mathcal E_6(v)_j\ne0,
$$

而原来源配对被 $s^{10}$ 整除。这才构成本原有限 Macaulay 来源模块中的模 $s^{10}$ 成员性障碍。本次第七结果进一步判定，这个条件在该第六读数上已经不可能发生，见下一节。


## 6. 本次第六读数消失与第七读数的新范围

本次十六条真实第七 cochain 的 $\lambda_0,\ldots,\lambda_6$ 九平方读数全零。每个 $9\times16$ 块的逻辑 SHA256 为

50481f599d30321bdcddac68122c35d18c31d1ed3b5a703f678a51e074412cd3。

所以

$$
K_7\subset\ker\mathcal E_6.
\tag{6.1}
$$

第六稿已经给 $\mathcal E_6\ne0$，而
$\dim K_6-\dim K_7=17-16=1$。因此无需新的矩阵求秩便严格得到

$$
\operatorname{rank}\mathcal E_6=1,\qquad
\ker\mathcal E_6=K_7.
\tag{6.2}
$$

任何九阶头都属于 $K_7$，故任意真实九阶 cochain 对 $h_0t_j$ 的系数至 $s^9$ 均为零。由第六非零读数期待模 $s^{10}$ 障碍的这条入口已经排除；不能把第六页已经消失的方向带到第九页。

另一方面，本次 $\lambda_7$ 的读数并非全零。首项仍是目标 $j=2$、零基 headColumn $3$：

$$
-\frac{
1051738380994431656652017262356687674453679689705494126993477415343336729
}{
1012043567620074596195475571343418643710874208894989564089729024000
}
\ne0.
\tag{6.3}
$$

其 $9\times16$ 矩阵逻辑 SHA256 为

2a6afaab7424b95bb33d47361047101d5b743a55b2e841d0bbe83f093cd17407。

这里必须区分代表自由：同头七阶 cochain 可加 $sT_6(v)$，其第七读数会加上 $\mathcal E_6(v)$。所以 (6.3) 尚不能作为完整 $K_7$ 上的代表无关映射。

若该头实际升到八阶，则任意同头八阶 cochain 之差除以 $s$ 是七阶 cochain；其第六读数由 (6.1) 为零。因此八阶输出的第七读数将在完整 $K_8$ 上与代表选择无关。后续必须用实际完整第八头与原目标读数来判断，不将本次原始第七数组直接当成下一页的固定值。由于 $h_0$ 有三阶零点，新的第七读数若要形成相应障碍，至少需要正确的十阶左 jet。

## 7. 实际证据

实际运行身份：

- run：43702348535；
- step：zero-complete-seventh-full-incoming；
- 执行来源提交：381a13bb421026a0d90f2f441e33489411725680；
- 数学耗时：约 $28.7057$ 秒；
- 源码 SHA256：9bf405d3aa65d40a8ebeb3fc87f3e8bd686814db371657abe9794f92e59099b8；
- 原始小回执：$63649$ 字节，SHA256 为 e35f4944b866a1df70b94315602cf8e38f1e9139ee563946adb2d71f35a90f6f；
- 主线外回执：$71197$ 字节，SHA256 为 5daff4f9c8536cde12cf20a42066971fc13da22934f0f0ed0941bec40bcdaaea。

| 对象 | 尺寸 | 逻辑 SHA256 |
|---|---:|---|
| 原第七 forcing | $6188\times7$ | edba74765684b3f1f164f6866cab3eadd6fe18acc426ba793b7f5e883f12a664 |
| 全原低行 Schur | $1088\times51$ | 23cc3a347e79a0f5d154fe5a0d3ab48d72a85aa581b010239c8d98671dd21ae4 |
| 完整低核 | $643\times52$ | b566df519c5b0a7de0850f9346f8abee0c2fffd7d269eda822617f1d40a500ca |
| 全部十六条第七 cochain | $22690\times16$ | 9660d3d45c2d9ea74046edc9d65c106d47d4cf173743b34a8c479c080a1a6eab |
| 原第七 leading 投影 | $17\times16$ | aed0ef5a73232622a5a1b2525d36b97cc7954df379f64f2c9ffd6be6814b81a4 |

检查点 binding 为 cfad1b4c8b6ccea947e5e4bfd535f3d50b4b7dd77ead0354a9791d4fe8740a60；manifest 为 $25973$ 字节，SHA256 为 6db895320f4d2142e99f0526f3e28545e37e1cb1bf5f695a7d95b13e85842d7f。完整可重算数组只保留于同 run 临时工作区。

下一完整第八页保留全部 $W_7=W_6+R_7(K_6)$，旧五十一列实际 RHS 原样复用，只新增当前十六头的六个非 exact forcing。新低矩阵共有 $649$ 列，旧 incoming 秩为 $591$，零 leading 纤维维数为 $52$。新秩与配对结论均须等待其实际全来源核验。
