# R150：零点完整第九连接为零、次大阶恰55与两种剩余正谱

2026-11-15；Astra-ISP-789f / root；AI 辅助：GPT-6 Astra Pro。

## 1. 结论与原范围

在原自然参数 $s=0$、原十七式及全部 $6188$ 个次数不超过三的原来源上，本次实际有理运算证明
$$
\operatorname{rank}_{\mathbb Q}\beta_{9,0}=0,\qquad
K_9=K_8,\qquad \dim K_9=15.
$$
这里等号指原常数左头空间中的同一子空间，不是只比较维数。完整第九 leading 投影是 $15\times15$ 满秩矩阵；所有低页像及其整条 cochain 回填均保留。

零点十四个正 Smith 指数已经只剩两种可能：
$$
(1,1,1,1,3,4,4,4,5,6,7,8,10,10)
$$
或
$$
(1,1,1,1,3,4,4,4,5,6,7,8,10,11).
$$
所以
$$
\delta_{4353,0}=55,\qquad
\delta_{4354,0}\in\{65,66\},\qquad
a_{\max,0}\in\{10,11\}.
$$
公共因子可取 $K_{111}$，配当前无穷远界的统一条件来源费用为 $8578$。此外，原九个 $h_0t_j$ 已属于完整原有限来源模 $s^{11}$ 的像；因此零点全部 torsion 障碍在原目标属于 $\mathbb Q((s))$ 像的前提下已经付清。原函数域像与全局 $\mathbb Q[s]$ 成员性仍未证明。

主要证据为[完整第八证明](R150-appendix-zero-complete-eighth-connection-two-remaining-smith-exponents-and-factor109.md)、[本次实际回执](../notes/r150-infinity-remote-session-789f/43702348535-zero-complete-ninth-full-incoming.json)、[实际通用源码](../notes/2026-11-15-r150-zero-complete-higher-full-incoming-789f.py)和[完整模31总阶上界](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)。

## 2. 完整第九连接的计算

沿原准确共动坐标写
$$
M(s)=A_{\mathrm{new}}(s)^{\mathsf T}=\sum_{j\ge0}s^jM_j.
$$
所有原来源变换与原目标转置运输保持。令 $T_j$ 为完整真实 $j$ 阶左 cochain 族，$R_j$ 为 $T_{j-1}$ 的第 $j$ 阶 forcing。完整第二连接为零后，第九连接所需全部旧像为
$$
W_8=\operatorname{im}M_0+M_1K_0+
\sum_{j=3}^{8}R_j(K_{j-1}).
$$
同一第八头的任意代表差逐阶由旧完整族产生，故上述每个低页像均须保留。

完整 $K_8$ 的十五头包含十个全参数 exact 纯头，余五头的实际新 forcing 为
$$
R_9=\sum_{j=1}^{9}M_j\lambda_{9-j}
\in\mathbb Q^{6188\times5}.
$$
程序核验全部 $5100$ 个高来源行均为零。因此完整非纯高校正仍由已付的 $3762\times2$ 高齐次核 $N_{\mathrm h}$ 参数化，没有丢弃高层抵消。

令
$$
B=[J_0,M_1Q]\in\mathbb Q^{1088\times592},
\qquad C_{\mathrm h}=(M_0N_{\mathrm h})_{\mathrm{low}}.
$$
其中 $\operatorname{rank}B=582$。实际完整低矩阵为
$$
\mathcal M_9=[B,C_{\mathrm h},R_{3,\mathrm{low}},\ldots,R_{9,\mathrm{low}}]
\in\mathbb Q^{1088\times654}.
$$
列数是
$$
592+2+13+12+9+8+7+6+5=654.
$$
完整旧像的低秩为 $592$，增广后的实际秩仍为 $592$，故
$$
\dim\ker\mathcal M_9=654-592=62.
$$
核到最后五个 leading 参数的投影满秩五，零 leading 纤维为
$$
62-5=57=649-592.
$$
因此 $\beta_{9,0}$ 精确为零。十个 exact 头与这五个完整新头合为十五头，leading 投影覆盖整个 $K_8$。

实际求解复用五十七列旧单位解，仅增加五列实际 RHS。对 $3\le j\le8$，旧参数全部按
$$
s^{9-j}T_{j-1}y_j
$$
回填整条 cochain；最后 $Q$ 修正置于 $\lambda_8$，完整常数校正置于 $\lambda_9$。输出临时矩阵尺寸为 $31424\times15$，原零至九阶全部乘回核验
$$
10\cdot6188\cdot15=928200
$$
个有理坐标均为零。

## 3. 次大阶已经精确，余谱只两种

完整前九级连接秩为
$$
(4,0,1,3,1,1,1,1,0).
$$
所以已定的十二个正指数是
$$
1,1,1,1,3,4,4,4,5,6,7,8,
$$
和为 $45$。另外两个指数 $b\le c$ 因 $\beta_{9,0}=0$ 而满足 $10\le b\le c$。既有原全矩阵特征零总阶上界 $66$ 给
$$
b+c\le21.
$$
整数性立即推出
$$
(b,c)\in\{(10,10),(10,11)\}.
$$
于是
$$
\delta_{4353,0}=45+b=55,\qquad
\delta_{4354,0}=45+b+c\in\{65,66\}.
$$
这里次大阶等于55是精确结论，未用尚未计算的第十页。第十连接若为二，则余谱为 $(10,10)$；若为一，则余谱为 $(10,11)$。零或其他值均与已证范围不相容，但实际执行仍以全原行核验为准。

最大正指数上界为11。因此，在原目标已经另行证明属于 $\mathbb Q((s))$ 像的前提下，整个原系统的模 $s^{11}$ 成员性与 $\mathbb Q[[s]]$ 成员性等价。这个前提不能删去；十三个自由余核坐标仍须处理。

## 4. 公共因子和条件费用

保留其他有限点的已付因子，
$$
\begin{aligned}
K_{111}
&=s^2K_{109}=s^{51}K_{60}\\
&=s^{65}(s-2)^9(s+6)^9F_+(s)^2F_-(s)^2E_8(s)^2.
\end{aligned}
$$
其次数为111，首项系数为 $5^6$。

保持[同选定子式无穷远界](R150-appendix-seventeen-source-fourth-pairing-rank-one-sixteen-heads-and-cost8585.md) $130/125/125$，令 $q=D/K_{111}$。由所选模31子式次数8527及原齐次权8770，
$$
8416=8527-111\le\deg q\le8770-130-111=8529.
$$
原完整来源降度的三支费用分别为
$$
\begin{aligned}
\text{非基来源}&\le8529-1+45=8573,\\
\text{基来源转移}&\le8770+55-125-111-11=8578,\\
\text{目标分支}&\le8770+64-125-111-10-8416=172.
\end{aligned}
$$
所以原目标 $h_0t_\nu$ 若属于原 $\mathbb Q[s]$ 来源像，则统一费用可取8578；本次不以次数界替代成员性。

## 5. 第八平方读数成为同头不变量

本次十五条真实第九 cochain 的 $\lambda_0,\ldots,\lambda_7$ 九平方读数仍全部为零。$\lambda_8$ 的 $9\times15$ 读数矩阵与已付第八实际矩阵相同，逻辑 SHA256 为650e9b3bd5e9b77231d97cfb587d93aafeee4eda5091542d8588fabb91873665；首个非零项仍是目标 $j=2$、零基 headColumn 1：
$$
c_8=
\frac{313642452561212784993210751263389279882343}
{9442075040159421726339056287856000000}\ne0.
$$

前稿已证明任意真实八阶 cochain 的第七平方读数为零。任意同头的两条九阶 cochain 之差除以 $s$ 是八阶 cochain，故两者第八平方读数相同。因此
$$
\mathcal E_8:K_9\longrightarrow\mathbb Q^9,\qquad
v\longmapsto\bigl(\lambda_8(n_j^2)\bigr)_{j=2}^{10}
$$
是与九阶代表无关的非零线性映射。任何更高完整头的相应读数都是这一映射的限制。

原 $h_0$ 有三阶零点，$[s^3]h_0=-917294284800$。若某个实际十一阶头上的 $\mathcal E_8$ 仍非零，则真实十一阶左 cochain 对相应 $h_0t_j$ 的 $s^{11}$ 配对系数为
$$
-917294284800\,\mathcal E_8(v)_j\ne0,
$$
而全部原来源配对属于 $s^{12}\mathbb Q[[s]]$，这才给本有限来源模块中的局部成员性障碍。当前尚未证明这样的头能存活到十一阶；不能把 $K_9=K_8$ 延伸成 $K_{11}=K_9$。

本次 $\lambda_9$ 也有非零读数，矩阵逻辑 SHA256 为e5814c5f51776dd07100af26c2b5521e4c7309020fd5df0bd384c765ce37fb11。这里只记录真实代表值，不额外声称它的同头不变性。以上均属原R150有限来源构造，未解决普通无限维ISP。

## 6. 九原目标的完整模 $s^{11}$ 成员性

此项是由已经实际核验的完整低页推出的存在性结论，不需要预先构造十阶 cochain 基。

取任意真实十阶 cochain $\lambda(s)$，即
$$
M(s)\lambda(s)\equiv0\pmod{s^{11}}.
$$
其八阶截断属于完整真实八阶 cochain 空间。前稿已证明任何这样的 cochain 的 $\lambda_0,\ldots,\lambda_7$ 均杀掉九个平方。由于 $h_0=s^3u(s)$ 且 $u(0)\ne0$，
$$
\lambda(s)^{\mathsf T}h_0(s)n_j^2\equiv0\pmod{s^{11}}
\quad(2\le j\le10).
$$
该结论覆盖全部完整左核，包括所有零头 cochain；没有只测试十五个既定代表。

令 $R=\mathbb Q[s]/(s^{11})$。对任意矩阵 $A$ over $R$，有
$$
\operatorname{im}_R A
=\{b:\lambda^{\mathsf T}b=0\ \text{for every }\lambda\in\ker_R A^{\mathsf T}\}.
$$
本处可直接取 $A$ 的 $\mathbb Q[[s]]$ Smith 形式并模 $s^{11}$ 验证，不借未知目标成员性：对角项 $s^a$ 在 $0<a<11$ 时，其左核为 $s^{11-a}R$，被所有左核杀掉恰要求目标坐标属于 $s^aR$；对角项是零或 $a\ge11$ 时左核为全 $R$，要求目标坐标为零；单位项没有限制。可逆的原行列运输保持此判准。

所以全部九个原目标满足
$$
h_0t_j\in\operatorname{im}\!\left(
A:R^{6188}\longrightarrow R^{4367}\right),
\qquad j=2,\ldots,10.
$$
这是完整原有限来源模 $s^{11}$ 的成员性，未提供新的显式来源列。所有正 Smith 指数至多11，因此若原目标又属于 $\mathbb Q((s))$ 像，十三个自由余核坐标已经为零，以上有限阶成员性便推出
$$
h_0t_j\in\operatorname{im}_{\mathbb Q[[s]]}A.
$$
函数域像仍是必要的独立前提。若后续实际十一阶头上的 $\mathcal E_8$ 非零，则第5节的障碍必须否定该函数域像前提；不能把它与本节已付的有限零点 torsion 判准混淆。其他有限点及全局多项式来源仍未处理。

## 7. 实际运行与恢复

- run：43702348535；job：132776011109；step：zero-complete-ninth-full-incoming。
- 执行来源提交：6b35510ee55c7d3a31bb987a50fafd4f531ee2a8。
- 数学耗时：40.49654567399921秒；外层耗时：40.66786737499933秒。
- 通用源码SHA256：9bf405d3aa65d40a8ebeb3fc87f3e8bd686814db371657abe9794f92e59099b8。
- 原始小回执：76694字节；SHA256：91a6381ce2acf39d205299dcf7acd21b3dc8bce2fda8c6f39870ccb208c1d737。
- 外回执：85402字节；SHA256：adc77b0324d04f9b6d527d4e16660572f0d587dc2245a680cece1f98facfbfc5。
- 检查点binding：ff22e24c8a00709a07818329c9835ce8fa98d27ee0937062c48ca0504ad274d4。
- manifest：29426字节；SHA256：a18b77544c76253598b477be606a3ce413dbeed62adc0533ddf5971fd572e5d6。
- 全部第九cochain逻辑SHA256：9b25ec2f2df34e4fc9968432fdb9f0cc9e6dfe019efd0f39445a2d063745b2f2。

完整矩阵、列解和cochain仅在同job临时区保留；源码、参数、真实run与小回执足以按历史检查点重做。下一页保全 $W_9=W_8+R_9(K_8)$、旧62列单位解，仅对五个非exact当前头计算新forcing，未预填第十实际秩。
