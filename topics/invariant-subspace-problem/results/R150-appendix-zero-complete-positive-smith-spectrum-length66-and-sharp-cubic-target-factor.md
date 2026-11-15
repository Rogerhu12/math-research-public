# R150：零点完整正 Smith 谱、长度恰66、$K_{112}$ 与三阶目标因子的必要性

2026-11-15；Astra-ISP-789f / literature_audit；AI 辅助：GPT-6 Astra Pro。

## 1. 完整谱已确定

对原自然参数 $s=0$、原十七式和全部 $6188$ 个原来源，本次实际有理运算证明完整第十连接

$$
\operatorname{rank}_{\mathbb Q}\beta_{10,0}=1,\qquad
\dim K_{10}=14.
\tag{1.1}
$$

结合已付完整前九级及零点总阶上界 $66$，原矩阵的十四个正 Smith 指数精确为

$$
1,1,1,1,\ 3,\ 4,4,4,\ 5,\ 6,\ 7,\ 8,\ 10,\ 11.
\tag{1.2}
$$

因此

$$
\delta_{4354,0}=66,\qquad
\delta_{4353,0}=55,\qquad
a_{\max,0}=11.
\tag{1.3}
$$

这不是仅由有限支持包络得到的下界。原矩阵常秩为 $4340$、泛型秩为 $4354$，所以其局部 Smith 形式有 $4340$ 个单位、(1.2) 的十四个正幂及十三个自由余核坐标。

原公共因子现在可取 $K_{112}$。配当前同选定子式的无穷远阶 $130/125/125$，统一条件来源费用为 $8577$，目标分支为 $172$。

本次还有独立的目标必要性结论：在本原有限 Macaulay 来源模块中，$(h_0/s)t_2$ 不属于 $\mathbb Q[[s]]$ 像。因此原 $h_0$ 的零点三阶因子不能降为二阶。原 $h_0t_j$ 本身的全局成员性仍未证明。

主要来源：

- [完整第八连接及两剩余指数](R150-appendix-zero-complete-eighth-connection-two-remaining-smith-exponents-and-factor109.md)；
- [完整第九与模 $s^{11}$ 成员性证明](R150-appendix-zero-complete-ninth-connection-exact-submaximal55-and-local-membership.md)；
- [完整第九实际回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-complete-ninth-full-incoming.json)；
- [本次完整第十实际回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-complete-tenth-full-incoming.json)；
- [通用完整高阶源码](../notes/2026-11-15-r150-zero-complete-higher-full-incoming-789f.py)；
- [完整模 $31$ 仿射公因子](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)；
- [同选定子式无穷远阶 $130/125/125$](R150-appendix-seventeen-source-fourth-pairing-rank-one-sixteen-heads-and-cost8585.md)。

## 2. 完整第十连接与原来源核验

沿准确共动坐标写

$$
M(s)=A_{\mathrm{new}}(s)^{\mathsf T}
=\sum_{j\ge0}s^jM_j.
\tag{2.1}
$$

原目标和来源变换均被保留，原左泛函按目标变换的转置恢复。令 $T_j$ 为完整真实 $j$ 阶 cochain，$R_j$ 为 $T_{j-1}$ 的第 $j$ 阶 forcing。完整第二连接为零后，本次全部旧像为

$$
W_9=\operatorname{im}M_0+M_1K_0+
\sum_{j=3}^{9}R_j(K_{j-1}).
\tag{2.2}
$$

这包含所有同头旧代表的变化。旧参数按 $s^{10-j}T_{j-1}$ 回填整条 cochain，不只修改最后一次常核项。

完整 $K_9=K_8$ 有十五头，其中十个纯头对全部参数 exact。对其余五头构造真实新 forcing

$$
R_{10}=\sum_{j=1}^{10}M_j\lambda_{10-j}
\in\mathbb Q^{6188\times5}.
\tag{2.3}
$$

全部 $5100$ 个高来源行本次实际为零，故高校正仍由完整高齐次核

$$
N_{\mathrm h}:\mathbb Q^2\longrightarrow\mathbb Q^{3762}
\tag{2.4}
$$

参数化。令 $B=[J_0,M_1Q]$，其尺寸为 $1088\times592$、秩为 $582$，并令 $C_{\mathrm h}=(M_0N_{\mathrm h})_{\mathrm{low}}$。

完整低矩阵为

$$
\mathcal M_{10}
=[B,C_{\mathrm h},R_{3,\mathrm{low}},\ldots,R_{10,\mathrm{low}}]
\in\mathbb Q^{1088\times659}.
\tag{2.5}
$$

实际完整旧像低秩为 $592$，新秩为 $593$，所以

$$
\dim\ker\mathcal M_{10}=659-593=66.
\tag{2.6}
$$

核向五个新 leading 参数的投影为四维，零 leading 纤维为

$$
66-4=62=654-592.
\tag{2.7}
$$

由完整输入头、完整旧像及完整高校正，

$$
\operatorname{rank}\beta_{10,0}=593-592=5-4=1,
\qquad \dim K_{10}=10+4=14.
\tag{2.8}
$$

本次复用六十二列旧实际 RHS 解，仅新增五列单位求解。重建后的完整 cochain 为 $35791\times14$，逐原式核验全部零至十阶：

$$
11\cdot6188\cdot14=952952
\tag{2.9}
$$

个有理坐标全部为零。

## 3. 从第十连接到完整正谱

完整前九级已给十二个正指数

$$
1,1,1,1,3,4,4,4,5,6,7,8
\tag{3.1}
$$

及另外两个 $b\le c$，其中 $b,c\ge10$。前十二个之和为 $45$，而原全矩阵总阶上界是 $66$，故

$$
b+c\le21.
\tag{3.2}
$$

本次 $\beta_{10,0}=1$ 说明恰有一个正指数等于十。所以 $b=10,c>10$，结合 (3.2) 的整数性，

$$
c=11.
\tag{3.3}
$$

这证明 (1.2)–(1.3)。特别地，完整第十一连接的秩在理论上必为一，之后连接秩为零，完整 $K_{11}$ 的维数必为十三。下一实际计算仍需要构造这些十三条原 cochain 并核验目标读数；本段不冒称它们已经计算。

### 一个完整最大子式的单位首项存在性

旧模 $31$ 完整最大子式公因子在零点的阶恰为 $66$。因此至少存在一个原完整最大子式，其模 $31$ 约化的零点阶为 $66$。现在所有特征零完整最大子式的零点阶都至少为 $66$，所以该子式的低于 $66$ 次项原本全部为零，而其 $s^{66}$ 系数是一个 $31$ 单位。

这是完整原矩阵中某个最大子式的存在性结论；没有将它识别为当前固定选定的 $D$，也没有给未计算的行列索引。

## 4. $K_{112}$ 与条件来源费用

其他有限点的已付因子保持，于是

$$
\begin{aligned}
K_{112}
&=sK_{111}=s^{52}K_{60}\\
&=s^{66}(s-2)^9(s+6)^9F_+(s)^2F_-(s)^2E_8(s)^2.
\end{aligned}
\tag{4.1}
$$

其次数为 $112$，首项系数为 $5^6$。零点指数 $66$ 已是完整原最大子式公共阶的精确值，不能在该点继续无依据增加公共因子。

保持同选定子式无穷远阶 $130/125/125$，令 $q=D/K_{112}$。由所选模 $31$ 子式次数 $8527$ 及原齐次权 $8770$，

$$
8415=8527-112\le\deg q
\le8770-130-112=8528.
\tag{4.2}
$$

三支来源费用为

$$
\begin{aligned}
\text{非基来源}&\le8528-1+45=8572,\\
\text{基来源转移}&\le8770+55-125-112-11=8577,\\
\text{目标分支}&\le8770+64-125-112-10-8415=172.
\end{aligned}
\tag{4.3}
$$

因此原 $h_0t_\nu$ 若属于原十七式的 $\mathbb Q[s]$ 来源像，则统一费用可取 $8577$。这仍是条件次数结论，不替代全局成员性。

## 5. 第八读数在 $K_{10}$ 上仍非零

原九目标

$$
t_j(s,m)=
\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2
\tag{5.1}
$$

在真实共动坐标中为 $n_j^2$。本次全部十四条 cochain 的 $\lambda_0,\ldots,\lambda_7$ 九平方读数全零，但 $\lambda_8$ 不全零。

首个非零项为目标 $j=2$、零基 headColumn $1$：

$$
c_8=
\frac{
571583414530130311611606766587915949957775073526988103
}{
200842141237826405079519445807437965564128144000000
}
\ne0.
\tag{5.2}
$$

其 $9\times14$ 矩阵逻辑 SHA256 为

07a8064001c378ab37d484ebdbe49ef4ae252446911da41b9fe0a7f1c23a8f48。

完整第八稿已经证明任意真实八阶 cochain 的第七平方读数为零。因此任意同头九阶 cochain 的第八读数相同，给完整 $K_9$ 上的线性映射 $\mathcal E_8$；本次读数正是其在 $K_{10}$ 上的限制。数值坐标因实际 leading 选基而改变，不是同头代表自由改变了 $\mathcal E_8$。

本次 $\lambda_9,\lambda_{10}$ 亦有非零原代表读数，逻辑 SHA256 分别为 01ffe52978c9b0004645a567350a27ad86c0a7e861b6c564208d58a68d4a598e 和 5f528844cd2a11ee18d94acfa3a68d60df99fe3b291946665ad6faa24d7f7919。本段不额外声明这两项同头不变。

## 6. 零点三阶乘子是必要的

取 (5.2) 对应的真实十阶左 cochain。它满足

$$
M(s)\lambda(s)=O(s^{11}),\qquad
\langle\lambda(s),t_2(s)\rangle
=c_8s^8+O(s^9).
\tag{6.1}
$$

对任意非零 $g(s)\in\mathbb Q[[s]]$，若 $\operatorname{ord}_s g\le2$，则

$$
\operatorname{ord}_s\langle\lambda,g t_2\rangle
=8+\operatorname{ord}_s g\le10.
\tag{6.2}
$$

这与 $g t_2$ 属于本原来源像时配对必须被 $s^{11}$ 整除相矛盾。因此

$$
\operatorname{ord}_s g\le2
\quad\Longrightarrow\quad
g t_2\notin A(s)\mathbb Q[[s]]^{6188}.
\tag{6.3}
$$

[原整数模型](../notes/2026-11-14-r150-ninth-first-integer-model-789f.py) 定义

$$
h_0=s^3(s-2)F_+^2F_-^2E_8,
$$

其中 $F_+(0)=-8,F_-(0)=864,E_8(0)=9600$，所以

$$
[s^3]h_0=(-2)(-8)^2\,864^2\,9600=-917294284800.
\tag{6.4}
$$

特别地，

$$
(h_0/s)t_2\notin A(s)\mathbb Q[[s]]^{6188},
\tag{6.5}
$$

其十阶配对系数恰为 $-917294284800\,c_8\ne0$。这也排除本有限来源模块中的相应 $\mathbb Q[s]$ 来源。

原 $h_0t_2$ 的首个候选非零配对则在 $s^{11}$，当前十阶左残差也从 $s^{11}$ 开始，故不能用本次读数否定 $h_0t_2$。必须核查实际 $K_{11}$ 上的限制。

## 7. 已付有限局部成员性与泛型前提

完整第八稿的代表不变性还说明：任意真实十阶左 cochain 的零至七阶九平方读数全部为零。原 $h_0$ 恰有三阶零点，所以对所有这样的左 cochain，

$$
\langle\lambda,h_0t_j\rangle\equiv0\pmod{s^{11}},
\qquad j=2,\ldots,10.
\tag{7.1}
$$

在环 $R_{11}=\mathbb Q[s]/(s^{11})$ 上，可直接用原 $\mathbb Q[[s]]$ Smith 形式逐对角证明双湮灭判准。对于对角项 $s^a$，其转置核是
$s^{11-a}R_{11}$，湮灭这个核的目标坐标恰属于 $s^aR_{11}$；对于零对角坐标，整个 $R_{11}$ 都是转置核，故目标坐标必须为零。单位项无条件可解。因此 (7.1) 严格给出

$$
h_0t_j\in
A(s)R_{11}^{6188}
\quad\text{于 }R_{11}^{4367}.
\tag{7.2}
$$

若另已证明 $h_0t_j$ 属于 $A(s)\mathbb Q((s))^{6188}$，则十三个自由余核坐标恒为零。因为所有正 Smith 指数至多为十一，(7.2) 已支付全部有限 torsion 坐标，从而

$$
h_0t_j\in A(s)\mathbb Q[[s]]^{6188}.
\tag{7.3}
$$

这个泛型像前提不能省略。结合 (6.3)，若 $t_2$ 在泛型像中，则其零点 torsion 类所需的标量幂恰为 $s^3$；若九个目标都在泛型像中，则九目标的共同零点幂也恰为三。

如果下一实际 $K_{11}$ 上 $\mathcal E_8$ 仍非零，真实十一阶左 jet 就会给 $h_0t_j$ 的模 $s^{12}$ 障碍。结合 (7.2)–(7.3)，这必是否定该目标的泛型像前提，而非尚未支付的零点有限 torsion。以上均限定原 R150 有限 Macaulay 来源模块，不给普通无限维不变子空间问题的结论。

## 8. 实际证据

- run：43702348535；step：zero-complete-tenth-full-incoming；
- 执行来源提交：ed3fdc19787e4143685228bb1fb676f96ccf7390；
- 数学耗时：约 $49.7089$ 秒；
- 源码 SHA256：9bf405d3aa65d40a8ebeb3fc87f3e8bd686814db371657abe9794f92e59099b8；
- 原始小回执：$83784$ 字节，SHA256 为 88830dc221fdb8c241f1e8eb86dc288f1a646e0f786797ef6f6b874599925bb3；
- 主线外回执：$93089$ 字节，SHA256 为 0cbedfd59ef136dfdaba038101e86ab04e3e474dfb9b7da4f10116b432a4828f。

| 对象 | 尺寸 | 逻辑 SHA256 |
|---|---:|---|
| 原第十 forcing | $6188\times5$ | bc4d21b50d9dfe9aa809974fee20f487049ce68e87a08a01b6e60b9f0b138dab |
| 全原低行 Schur | $1088\times67$ | 1060d301f4e40b990b9bc4e67a74d8038f64725e70421af3a3a6d6c2fe51107a |
| 完整低核 | $659\times66$ | da4032c7e45645e73bb480a3b63fc941f8f7bd32779f51d21467e8dc21e3905a |
| 全部十四条第十 cochain | $35791\times14$ | 243296d6f13d4e7f687c3b3b49dba01df616ef67f0450c8d73ab7e57705bd74a |
| 原 leading 投影 | $15\times14$ | 261f19cbdcf12ee3d56758e8404fa7872c59ae4203a9c0938f0718641bdc011e |

检查点 binding 为 14e1c96e08c4bea493e289e9bc3349e88bd2d605caba6b153332f7eda7eb5ef0；manifest 为 $31517$ 字节，SHA256 为 10929f259464d4c469e6617c0d04e2596febdb4d4898e38f8977a1386e37db3d。完整可重算数组只保留在同 run 临时工作区。

下一实际第十一页须保留全部 $W_{10}=W_9+R_{10}(K_9)$，复用六十七列旧实际 RHS，只对当前四个非 exact 头生成新 forcing。理论谱已强制其完整连接秩为一；实际构造仍要保全高行、所有旧 incoming、原 cochain 和目标读数。
